"""MCP server that stays alive even without a graph. Replaces the global opencode MCP config."""
import sys, json, os
from pathlib import Path

GRAPH_PATH = Path("graphify-out/graph.json").resolve()

def load_graph():
    """Load graph, return (G, communities) or (None, None) if not found."""
    from graphify.serve import _load_graph, _communities_from_graph
    if not GRAPH_PATH.exists():
        return None, None
    try:
        G = _load_graph(str(GRAPH_PATH))
        communities = _communities_from_graph(G)
        return G, communities
    except SystemExit:
        return None, None

def build_graph():
    """Build graph from current directory using AST extraction."""
    from graphify.extract import collect_files, extract
    from graphify.build import build_from_json
    from graphify.cluster import cluster
    from graphify.export import to_json
    from graphify.detect import detect

    out = Path("graphify-out")
    out.mkdir(exist_ok=True)

    result = detect(Path.cwd())
    code_files = []
    for f in result.get("files", {}).get("code", []):
        p = Path(f)
        if p.is_dir():
            code_files.extend(collect_files(p))
        else:
            code_files.append(p)

    if not code_files:
        return {"status": "error", "message": "No code files found"}

    extraction = extract(code_files, cache_root=Path.cwd())
    G = build_from_json(extraction)
    communities = cluster(G)
    to_json(G, communities, str(GRAPH_PATH))
    return {"status": "ok", "nodes": G.number_of_nodes(), "edges": G.number_of_edges()}

async def main():
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp import types

    G, communities = load_graph()
    server = Server("graphify")

    @server.list_tools()
    async def list_tools():
        tools = [
            types.Tool(
                name="graph_status",
                description="Check if the knowledge graph exists and get build status.",
                inputSchema={"type": "object", "properties": {}},
            ),
            types.Tool(
                name="build_graph",
                description="Build the knowledge graph from the current project's codebase.",
                inputSchema={"type": "object", "properties": {}},
            ),
        ]
        if G is not None:
            tools += [
                types.Tool(
                    name="query_graph",
                    description="Search the knowledge graph using BFS or DFS.",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "question": {"type": "string"},
                            "mode": {"type": "string", "enum": ["bfs", "dfs"], "default": "bfs"},
                            "depth": {"type": "integer", "default": 3},
                            "token_budget": {"type": "integer", "default": 2000},
                        },
                        "required": ["question"],
                    },
                ),
                types.Tool(
                    name="graph_stats",
                    description="Return summary statistics about the knowledge graph.",
                    inputSchema={"type": "object", "properties": {}},
                ),
                types.Tool(
                    name="god_nodes",
                    description="Return the most connected nodes in the graph.",
                    inputSchema={"type": "object", "properties": {"top_n": {"type": "integer", "default": 10}}},
                ),
                types.Tool(
                    name="get_node",
                    description="Get full details for a specific node by label or ID.",
                    inputSchema={"type": "object", "properties": {"label": {"type": "string"}}, "required": ["label"]},
                ),
                types.Tool(
                    name="get_neighbors",
                    description="Get all direct neighbors of a node with edge details.",
                    inputSchema={"type": "object", "properties": {"label": {"type": "string"}}, "required": ["label"]},
                ),
                types.Tool(
                    name="shortest_path",
                    description="Find the shortest path between two concepts in the knowledge graph.",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "source": {"type": "string"},
                            "target": {"type": "string"},
                            "max_hops": {"type": "integer", "default": 8},
                        },
                        "required": ["source", "target"],
                    },
                ),
                types.Tool(
                    name="get_community",
                    description="Get all nodes in a community by community ID.",
                    inputSchema={"type": "object", "properties": {"community_id": {"type": "integer"}}, "required": ["community_id"]},
                ),
            ]
        return tools

    def _ensure_graph():
        nonlocal G, communities
        if G is None:
            G2, c2 = load_graph()
            if G2 is None:
                return None, None
            G, communities = G2, c2
        return G, communities

    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
        if name == "graph_status":
            if GRAPH_PATH.exists():
                g, _ = load_graph()
                if g:
                    return [types.TextContent(type="text", text=json.dumps({"exists": True, "nodes": g.number_of_nodes(), "edges": g.number_of_edges()}))]
            return [types.TextContent(type="text", text=json.dumps({"exists": False}))]

        if name == "build_graph":
            result = build_graph()
            nonlocal G, communities
            G, communities = load_graph()
            return [types.TextContent(type="text", text=json.dumps(result))]

        g, _ = _ensure_graph()
        if g is None:
            return [types.TextContent(type="text", text=json.dumps({"error": "No graph found. Call build_graph first."}))]

        if name == "query_graph":
            from graphify.serve import _query_graph_text
            result = _query_graph_text(g, arguments["question"], mode=arguments.get("mode", "bfs"), depth=arguments.get("depth", 3), token_budget=arguments.get("token_budget", 2000))
            return [types.TextContent(type="text", text=str(result))]

        if name == "graph_stats":
            from graphify.serve import _score_nodes
            return [types.TextContent(type="text", text=json.dumps({
                "nodes": g.number_of_nodes(), "edges": g.number_of_edges(),
                "communities": len(communities) if communities else 0,
            }))]

        if name == "god_nodes":
            from graphify.serve import _score_nodes
            top = _score_nodes(g, top_n=arguments.get("top_n", 10))
            return [types.TextContent(type="text", text=json.dumps(top))]

        if name == "get_node":
            from graphify.serve import _find_node
            result = _find_node(g, arguments["label"])
            return [types.TextContent(type="text", text=json.dumps(result))]

        if name == "get_neighbors":
            from graphify.serve import _find_node
            n = _find_node(g, arguments["label"])
            if not n:
                return [types.TextContent(type="text", text=json.dumps({"error": "Node not found"}))]
            nid = n.get("id", n.get("label"))
            neighbors = []
            for _, trg, edata in g.edges(nid, data=True):
                neighbors.append({"node": trg, "relation": edata.get("relation", edata.get("label", "related"))})
            return [types.TextContent(type="text", text=json.dumps(neighbors))]

        if name == "shortest_path":
            from graphify.serve import _find_node
            src = _find_node(g, arguments["source"])
            tgt = _find_node(g, arguments["target"])
            if not src or not tgt:
                return [types.TextContent(type="text", text=json.dumps({"error": "Source or target not found"}))]
            sid = src.get("id", src.get("label"))
            tid = tgt.get("id", tgt.get("label"))
            import networkx as nx
            try:
                path = nx.shortest_path(g, sid, tid)
                return [types.TextContent(type="text", text=json.dumps({"path": path, "length": len(path) - 1}))]
            except (nx.NetworkXNoPath, nx.NodeNotFound) as e:
                return [types.TextContent(type="text", text=json.dumps({"error": str(e)}))]

        if name == "get_community":
            cid = arguments["community_id"]
            if communities and cid in communities:
                return [types.TextContent(type="text", text=json.dumps({"community_id": cid, "nodes": communities[cid]}))]
            return [types.TextContent(type="text", text=json.dumps({"error": "Community not found"}))]

        raise ValueError(f"Unknown tool: {name}")

    async with stdio_server() as streams:
        await server.run(streams[0], streams[1], server.create_initialization_options())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
