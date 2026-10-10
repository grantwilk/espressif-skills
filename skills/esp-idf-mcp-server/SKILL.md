---
name: esp-idf-mcp-server
description: Enable and configure ESP-IDF's built-in MCP server (idf.py mcp-server) so an AI client can build, flash, set target, and clean. Use when connecting an editor or agent to ESP-IDF over MCP.
---

# ESP-IDF MCP Server

Built into `idf.py` (ESP-IDF 6.0+). Tools exposed as of v6.0.1: `build_project`, `set_target`, `flash_project`, `clean_project`. For everything else (monitor, debug, eFuses) use the shell skills.

1. Install the Python deps once: `python $IDF_PATH/tools/idf_tools.py install-python-env --features mcp` (or choose the `mcp` feature at install time). Without it the server exits with "MCP dependencies not available".
2. Register it with the client. **stdout must contain only MCP JSON**, so discard the activation banner. Example `mcp.json` (Windows PowerShell; adapt the script path on other systems):

```json
{
  "mcpServers": {
    "esp-idf": {
      "command": "powershell",
      "args": ["-NoProfile", "-NonInteractive", "-Command",
        "$p=(Get-ChildItem \"$env:IDF_TOOLS_PATH\\Microsoft.*.PowerShell_profile.ps1\" | Sort-Object Name -Descending | Select-Object -First 1).FullName; . $p *> $null; idf.py mcp-server"],
      "env": { "IDF_MCP_WORKSPACE_FOLDER": "${workspaceFolder}" }
    }
  }
}
```

   macOS/Linux: `"command": "bash"`, `"args": ["-c", ". <tools-dir>/activate_idf_<version>.sh >/dev/null 2>&1; idf.py mcp-server"]`.
3. `idf.py mcp-server -C <project-dir>` sets the project explicitly; otherwise `IDF_MCP_WORKSPACE_FOLDER` is used.

Check from a shell: pipe an MCP `initialize` request into the command and confirm the first stdout line is JSON. `eim run "idf.py mcp-server"` prints a banner on stdout, which can break strict clients.
