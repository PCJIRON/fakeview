# Graph Report - .  (2026-06-03)

## Corpus Check
- 212 files · ~292,261 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1090 nodes · 2540 edges · 50 communities (49 shown, 1 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_UI Completion Components|UI Completion Components]]
- [[_COMMUNITY_Provider & Settings Configs|Provider & Settings Configs]]
- [[_COMMUNITY_Core App Configuration|Core App Configuration]]
- [[_COMMUNITY_API & Overlay Components|API & Overlay Components]]
- [[_COMMUNITY_macOS AudioSpeaker|macOS Audio/Speaker]]
- [[_COMMUNITY_Keyboard Shortcuts|Keyboard Shortcuts]]
- [[_COMMUNITY_NPM Dependencies|NPM Dependencies]]
- [[_COMMUNITY_Dashboard Pages|Dashboard Pages]]
- [[_COMMUNITY_Platform & Shortcut Manager|Platform & Shortcut Manager]]
- [[_COMMUNITY_Linux Audio Capture|Linux Audio Capture]]
- [[_COMMUNITY_Windows AudioSpeaker|Windows Audio/Speaker]]
- [[_COMMUNITY_Tauri Backend Core|Tauri Backend Core]]
- [[_COMMUNITY_Chat Components|Chat Components]]
- [[_COMMUNITY_Speech Recognition UI|Speech Recognition UI]]
- [[_COMMUNITY_Database & Storage|Database & Storage]]
- [[_COMMUNITY_System Prompts|System Prompts]]
- [[_COMMUNITY_UI Base Components|UI Base Components]]
- [[_COMMUNITY_Response Settings|Response Settings]]
- [[_COMMUNITY_Screenshot Features|Screenshot Features]]
- [[_COMMUNITY_App Layout & Routing|App Layout & Routing]]
- [[_COMMUNITY_License & Promotion|License & Promotion]]
- [[_COMMUNITY_Audio Recording|Audio Recording]]
- [[_COMMUNITY_Rust Capture Module|Rust Capture Module]]
- [[_COMMUNITY_Chat History DB|Chat History DB]]
- [[_COMMUNITY_Audio Visualization|Audio Visualization]]
- [[_COMMUNITY_Activation Shortcuts|Activation Shortcuts]]
- [[_COMMUNITY_Drag & Drop|Drag & Drop]]
- [[_COMMUNITY_Theme & Styling|Theme & Styling]]
- [[_COMMUNITY_Tauri Window Management|Tauri Window Management]]
- [[_COMMUNITY_Pluely API Client|Pluely API Client]]
- [[_COMMUNITY_Custom Cursor|Custom Cursor]]
- [[_COMMUNITY_Completion Hooks|Completion Hooks]]
- [[_COMMUNITY_Markdown Rendering|Markdown Rendering]]
- [[_COMMUNITY_Utility Functions|Utility Functions]]
- [[_COMMUNITY_Version Management|Version Management]]
- [[_COMMUNITY_Clipboard & Copy|Clipboard & Copy]]
- [[_COMMUNITY_Menu Items|Menu Items]]
- [[_COMMUNITY_Build Configuration|Build Configuration]]
- [[_COMMUNITY_Tauri Capabilities|Tauri Capabilities]]
- [[_COMMUNITY_Migration Scripts|Migration Scripts]]
- [[_COMMUNITY_Dev Provider Config|Dev Provider Config]]
- [[_COMMUNITY_Window Management|Window Management]]
- [[_COMMUNITY_Chat View Components|Chat View Components]]
- [[_COMMUNITY_Analytics|Analytics]]
- [[_COMMUNITY_Rust Speaker Module|Rust Speaker Module]]

## God Nodes (most connected - your core abstractions)
1. `cn()` - 102 edges
2. `Button()` - 48 edges
3. `useApp()` - 39 edges
4. `String` - 29 edges
5. `Header()` - 24 edges
6. `AppHandle` - 20 edges
7. `String` - 19 edges
8. `R` - 19 edges
9. `get_stored_credentials()` - 18 edges
10. `compilerOptions` - 18 edges

## Surprising Connections (you probably didn't know these)
- `deactivate_license_api()` --calls--> `get_stored_credentials()`  [INFERRED]
  src-tauri/src/activate.rs → src-tauri/src/api.rs
- `validate_license_api()` --calls--> `get_stored_credentials()`  [INFERRED]
  src-tauri/src/activate.rs → src-tauri/src/api.rs
- `handle_toggle_dashboard()` --calls--> `show_dashboard_window()`  [INFERRED]
  src-tauri/src/shortcuts.rs → src-tauri/src/window.rs
- `CardAction()` --calls--> `cn()`  [EXTRACTED]
  src/components/ui/card.tsx → src/lib/utils.ts
- `CardFooter()` --calls--> `cn()`  [EXTRACTED]
  src/components/ui/card.tsx → src/lib/utils.ts

## Import Cycles
- 1-file cycle: `src-tauri/src/activate.rs -> src-tauri/src/activate.rs`
- 1-file cycle: `src-tauri/src/api.rs -> src-tauri/src/api.rs`
- 1-file cycle: `src-tauri/src/speaker/commands.rs -> src-tauri/src/speaker/commands.rs`
- 1-file cycle: `src-tauri/src/capture.rs -> src-tauri/src/capture.rs`
- 1-file cycle: `src-tauri/src/lib.rs -> src-tauri/src/lib.rs`
- 1-file cycle: `src-tauri/src/shortcuts.rs -> src-tauri/src/shortcuts.rs`
- 1-file cycle: `src-tauri/src/speaker/linux.rs -> src-tauri/src/speaker/linux.rs`
- 1-file cycle: `src-tauri/src/speaker/windows.rs -> src-tauri/src/speaker/windows.rs`
- 1-file cycle: `src-tauri/src/speaker/macos.rs -> src-tauri/src/speaker/macos.rs`
- 1-file cycle: `src-tauri/src/speaker/mod.rs -> src-tauri/src/speaker/mod.rs`
- 3-file cycle: `src/lib/index.ts -> src/lib/storage/index.ts -> src/lib/storage/shortcuts.storage.ts -> src/lib/index.ts`
- 3-file cycle: `src/lib/functions/ai-response.function.ts -> src/lib/index.ts -> src/lib/functions/index.ts -> src/lib/functions/ai-response.function.ts`
- 3-file cycle: `src/lib/database/chat-history.action.ts -> src/lib/index.ts -> src/lib/database/index.ts -> src/lib/database/chat-history.action.ts`
- 4-file cycle: `src/lib/storage/index.ts -> src/lib/storage/shortcuts.storage.ts -> src/types/index.ts -> src/types/context.type.ts -> src/lib/storage/index.ts`
- 4-file cycle: `src/lib/storage/ai-providers.ts -> src/types/index.ts -> src/types/context.type.ts -> src/lib/storage/index.ts -> src/lib/storage/ai-providers.ts`
- 4-file cycle: `src/lib/storage/index.ts -> src/lib/storage/stt-providers.ts -> src/types/index.ts -> src/types/context.type.ts -> src/lib/storage/index.ts`
- 5-file cycle: `src/lib/functions/index.ts -> src/lib/functions/pluely.api.ts -> src/lib/storage/index.ts -> src/lib/storage/shortcuts.storage.ts -> src/lib/index.ts -> src/lib/functions/index.ts`

## Communities (50 total, 1 thin omitted)

### Community 0 - "UI Completion Components"
Cohesion: 0.05
Nodes (55): Audio(), AutoSpeechVAD(), AutoSpeechVADProps, Files(), Completion(), Input(), MessageHistory(), MessageHistoryProps (+47 more)

### Community 1 - "Provider & Settings Configs"
Cohesion: 0.05
Nodes (46): CreateEditProvider(), CreateEditProviderProps, CustomProviders(), AIProviders(), Providers(), CheckoutResponse, GithubIcon(), XIcon() (+38 more)

### Community 2 - "Core App Configuration"
Cohesion: 0.06
Nodes (46): AI_PROVIDERS, STORAGE_KEYS, SPEECH_TO_TEXT_PROVIDERS, AppContext, initialState, Theme, ThemeProviderContext, ThemeProviderProps (+38 more)

### Community 3 - "API & Overlay Components"
Cohesion: 0.13
Nodes (46): ApiConfigError, Client, OverlayProps, SelectionCoords, AppProvider(), ThemeProvider(), Model, ApiConfigError (+38 more)

### Community 4 - "macOS Audio/Speaker"
Cohesion: 0.07
Nodes (38): AggregateDevice, AtomicU32, AudioFormat, Ctx, DictionaryOf, HeapCons, HeapProd, Retained (+30 more)

### Community 5 - "Keyboard Shortcuts"
Cohesion: 0.13
Nodes (39): MoveWindowTask, check_shortcuts_registered(), exit_app(), get_registered_shortcuts(), handle_audio_shortcut(), handle_focus_input(), handle_move_window(), handle_screenshot_shortcut() (+31 more)

### Community 6 - "NPM Dependencies"
Cohesion: 0.05
Nodes (42): dependencies, @bany/curl-to-json, class-variance-authority, clsx, cmdk, lucide-react, moment, @radix-ui/react-dialog (+34 more)

### Community 7 - "Dashboard Pages"
Cohesion: 0.09
Nodes (19): Audio(), getOsInstructions(), Dashboard(), AlwaysOnTopToggle(), AppIconToggle(), AudioSelection(), AutoScrollToggle(), LanguageSelector() (+11 more)

### Community 8 - "Platform & Shortcut Manager"
Cohesion: 0.12
Nodes (26): App(), CursorSelection(), DEFAULT_SHORTCUT_ACTIONS, getPlatform(), isLinux(), isMacOS(), isWindows(), ShortcutManager() (+18 more)

### Community 9 - "Linux Audio Capture"
Cohesion: 0.12
Nodes (26): Direction, get_default_monitor_source(), get_input_devices(), get_output_devices(), SpeakerInput, SpeakerStream, WakerState, Arc (+18 more)

### Community 10 - "Windows Audio/Speaker"
Cohesion: 0.12
Nodes (26): find_device_by_id(), get_input_devices(), get_output_devices(), SpeakerInput, SpeakerStream, WakerState, Arc, AudioDevice (+18 more)

### Community 11 - "Tauri Backend Core"
Cohesion: 0.10
Nodes (24): ActivationResponse, Model, StorageResult, CreateEditDialog(), CreateEditDialogProps, DeleteSystemPrompt(), DeleteSystemPromptProps, GenerateSystemPrompt() (+16 more)

### Community 12 - "Chat Components"
Cohesion: 0.18
Nodes (29): apply_noise_gate(), calculate_audio_metrics(), check_system_audio_access(), get_audio_sample_rate(), get_capture_status(), get_input_devices(), get_output_devices(), get_vad_config() (+21 more)

### Community 13 - "Speech Recognition UI"
Cohesion: 0.06
Nodes (30): app, macOSPrivateApi, security, windows, build, beforeBuildCommand, beforeDevCommand, devUrl (+22 more)

### Community 14 - "Database & Storage"
Cohesion: 0.12
Nodes (20): CursorSelectionProps, ScreenshotConfigs(), VadConfig, getPromptTemplateById(), PROMPT_TEMPLATES, PromptTemplate, SENSITIVITY_PRESETS, SensitivityPreset (+12 more)

### Community 15 - "System Prompts"
Cohesion: 0.11
Nodes (18): Model, PluelyPrompt, PluelyPrompts(), PluelyPromptsResponse, CardAction(), CardContent(), CardDescription(), CardFooter() (+10 more)

### Community 16 - "UI Base Components"
Cohesion: 0.23
Nodes (26): InstanceInfo, activate_license_api(), ActivationRequest, ActivationResponse, CheckoutResponse, deactivate_license_api(), get_api_access_key(), get_checkout_url() (+18 more)

### Community 17 - "Response Settings"
Cohesion: 0.13
Nodes (16): cn(), ModeSwitcher(), ModeSwitcherProps, Warning(), WarningProps, DropdownMenuCheckboxItem(), DropdownMenuLabel(), DropdownMenuRadioItem() (+8 more)

### Community 18 - "Screenshot Features"
Cohesion: 0.14
Nodes (18): PlatformSpeakerInput, PlatformSpeakerStream, AudioDevice, list_input_devices(), list_output_devices(), SpeakerInput, SpeakerStream, Context (+10 more)

### Community 19 - "App Layout & Routing"
Cohesion: 0.09
Nodes (21): compilerOptions, allowImportingTsExtensions, baseUrl, isolatedModules, jsx, lib, module, moduleResolution (+13 more)

### Community 20 - "License & Promotion"
Cohesion: 0.11
Nodes (13): generateConversationTitle(), AttachedFile, ChatCompletionState, ChatConversation, ChatMessage, AttachedFile, ChatConversation, ChatMessage (+5 more)

### Community 21 - "Audio Recording"
Cohesion: 0.14
Nodes (10): QuickActions(), QuickActionsProps, CreateSystemPromptProps, Badge(), badgeVariants, buttonVariants, Input(), ScrollBar() (+2 more)

### Community 22 - "Rust Capture Module"
Cohesion: 0.16
Nodes (18): RgbaImage, capture_selected_area(), capture_to_base64(), CaptureState, close_overlay_window(), MonitorInfo, SelectionCoords, start_screen_capture() (+10 more)

### Community 23 - "Chat History DB"
Cohesion: 0.30
Nodes (18): App, AppHandle, Box, Error, R, Result, String, WebviewWindow (+10 more)

### Community 24 - "Audio Visualization"
Cohesion: 0.11
Nodes (17): aliases, components, hooks, lib, ui, utils, iconLibrary, rsc (+9 more)

### Community 25 - "Activation Shortcuts"
Cohesion: 0.24
Nodes (13): buildEnhancedSystemPrompt(), blobToBase64(), buildDynamicMessages(), deepVariableReplacer(), extractVariables(), getByPath(), getStreamingContent(), processUserMessageTemplate() (+5 more)

### Community 26 - "Drag & Drop"
Cohesion: 0.25
Nodes (9): getDatabase(), createSystemPrompt(), deleteSystemPrompt(), getAllSystemPrompts(), getSystemPromptById(), updateSystemPrompt(), SystemPrompt, SystemPromptInput (+1 more)

### Community 27 - "Theme & Styling"
Cohesion: 0.14
Nodes (13): bugs, url, description, homepage, keywords, license, name, private (+5 more)

### Community 28 - "Tauri Window Management"
Cohesion: 0.22
Nodes (8): HeaderProps, EmptyComponent(), EmptyContent(), EmptyDescription(), EmptyHeader(), EmptyMedia(), emptyMediaVariants, EmptyTitle()

### Community 29 - "Pluely API Client"
Cohesion: 0.23
Nodes (6): AlwaysOnTopToggleProps, AppIconToggleProps, AutostartToggle(), AutostartToggleProps, Label(), Switch()

### Community 30 - "Custom Cursor"
Cohesion: 0.30
Nodes (10): createConversation(), DbConversation, DbMessage, deleteAllConversations(), getConversationById(), migrateLocalStorageToSQLite(), saveConversation(), updateConversation() (+2 more)

### Community 31 - "Completion Hooks"
Cohesion: 0.21
Nodes (11): AudioState, get_app_version(), init(), run(), AppHandle, Arc, JoinHandle, Mutex (+3 more)

### Community 32 - "Markdown Rendering"
Cohesion: 0.18
Nodes (10): compilerOptions, allowSyntheticDefaultImports, baseUrl, composite, module, moduleResolution, paths, skipLibCheck (+2 more)

### Community 33 - "Utility Functions"
Cohesion: 0.31
Nodes (8): Theme(), useTheme(), useSystemPrompts(), SystemPrompts(), DropdownMenu(), DropdownMenuContent(), DropdownMenuItem(), DropdownMenuTrigger()

### Community 34 - "Version Management"
Cohesion: 0.28
Nodes (7): deleteConversation(), getAllConversations(), UseHistoryReturn, UseHistoryType, AttachedFile, ChatConversation, CompletionState

### Community 35 - "Clipboard & Copy"
Cohesion: 0.22
Nodes (9): devDependencies, @tauri-apps/cli, tw-animate-css, @types/node, @types/react, @types/react-dom, typescript, vite (+1 more)

### Community 36 - "Menu Items"
Cohesion: 0.29
Nodes (6): description, identifier, permissions, platforms, $schema, windows

### Community 37 - "Build Configuration"
Cohesion: 0.29
Nodes (6): description, identifier, permissions, platforms, $schema, windows

### Community 38 - "Tauri Capabilities"
Cohesion: 0.33
Nodes (5): useCopyToClipboard(), CopyButton(), CopyButtonProps, Props, ResultsSection()

### Community 39 - "Migration Scripts"
Cohesion: 0.33
Nodes (5): DEFAULT_QUICK_ACTIONS, ChatConversation, ChatMessage, DEFAULT_VAD_CONFIG, useSystemAudioType

### Community 40 - "Dev Provider Config"
Cohesion: 0.40
Nodes (5): getStatus(), Header(), Props, STATUS_CONFIG, StatusType

### Community 41 - "Window Management"
Cohesion: 0.40
Nodes (5): scripts, build, dev, preview, tauri

### Community 42 - "Chat View Components"
Cohesion: 0.50
Nodes (3): migrations(), Migration, Vec

### Community 43 - "Analytics"
Cohesion: 0.50
Nodes (4): author, email, name, url

## Knowledge Gaps
- **301 isolated node(s):** `recommendations`, `$schema`, `style`, `rsc`, `tsx` (+296 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `cn()` connect `Response Settings` to `UI Completion Components`, `Provider & Settings Configs`, `Utility Functions`, `Tauri Capabilities`, `Dev Provider Config`, `Tauri Backend Core`, `Database & Storage`, `System Prompts`, `Audio Recording`, `Tauri Window Management`, `Pluely API Client`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **What connects `recommendations`, `$schema`, `style` to the rest of the system?**
  _301 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `UI Completion Components` be split into smaller, more focused modules?**
  _Cohesion score 0.05198537095088819 - nodes in this community are weakly interconnected._
- **Should `Provider & Settings Configs` be split into smaller, more focused modules?**
  _Cohesion score 0.05333333333333334 - nodes in this community are weakly interconnected._
- **Should `Core App Configuration` be split into smaller, more focused modules?**
  _Cohesion score 0.06095481670929241 - nodes in this community are weakly interconnected._
- **Should `API & Overlay Components` be split into smaller, more focused modules?**
  _Cohesion score 0.1346938775510204 - nodes in this community are weakly interconnected._
- **Should `macOS Audio/Speaker` be split into smaller, more focused modules?**
  _Cohesion score 0.07474747474747474 - nodes in this community are weakly interconnected._