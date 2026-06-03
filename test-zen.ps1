$headers = @{
    "Content-Type" = "application/json"
    "Authorization" = "Bearer public"
    "x-opencode-client" = "pluely-test"
    "x-opencode-session" = [guid]::NewGuid().ToString()
    "x-opencode-project" = "global"
    "x-opencode-request" = [guid]::NewGuid().ToString()
}

$body = @{
    model = "minimax-m3-free"
    messages = @(
        @{
            role = "user"
            content = "Say OK"
        }
    )
    stream = $false
    max_tokens = 10
} | ConvertTo-Json

Write-Output "=== Testing OpenCode Zen API ==="
Write-Output "URL: https://opencode.ai/zen/v1/chat/completions"
Write-Output "Model: minimax-m3-free"
Write-Output "Auth: Bearer public"
Write-Output ""

try {
    $response = Invoke-WebRequest -Uri "https://opencode.ai/zen/v1/chat/completions" `
        -Method POST `
        -Headers $headers `
        -Body $body `
        -ContentType "application/json" `
        -TimeoutSec 30

    Write-Output "=== SUCCESS ==="
    Write-Output "Status: $($response.StatusCode)"
    Write-Output "Response:"
    $response.Content | ConvertFrom-Json | ConvertTo-Json -Depth 10
} catch {
    Write-Output "=== ERROR ==="
    if ($_.Exception.Response) {
        $statusCode = $_.Exception.Response.StatusCode.value__
        Write-Output "HTTP Status: $statusCode"

        $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
        $errorBody = $reader.ReadToEnd()
        $reader.Close()
        Write-Output "Response body:"
        try {
            $errorBody | ConvertFrom-Json | ConvertTo-Json -Depth 5
        } catch {
            Write-Output $errorBody
        }
    } else {
        Write-Output "Error: $($_.Exception.Message)"
    }
}

Write-Output ""
Write-Output "=== Done ==="
