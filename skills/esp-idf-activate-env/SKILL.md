---
name: esp-idf-activate-env
description: Activate the ESP-IDF environment so idf.py, esptool, and the compilers are on PATH, including in non-interactive or agent shells. Use when idf.py is "not found" or at the start of a session.
---

# Activate the ESP-IDF Environment

Every new shell needs activation. Details: https://docs.espressif.com/projects/idf-im-ui/en/latest/after_installing.html

1. Source the script EIM wrote into its tools directory (the install output and `eim list` show the location):
   - bash/zsh/sh: `. <tools-dir>/activate_idf_<version>.sh` (fish: `activate_idf_<version>.fish`)
   - PowerShell: `. "<tools-dir>\Microsoft.<version>.PowerShell_profile.ps1"` (Windows also has an `IDF_PowerShell` desktop shortcut)
   - It must be **sourced**, not executed.
2. Or run one command inside an environment without activating the shell:
   `eim run "idf.py build"` (optional second argument selects a version: `eim run "<command>" <version>`)
3. Choose the default version: `eim list`, then `eim select <version>`.
4. Verify: `idf.py --version`, then `esptool version`.
5. Undo: source the matching `deactivate_idf_<version>.sh` / `...PowerShell_deactivate.ps1`.

Notes:
- Activation prints a banner. When a tool needs clean stdout (for example an MCP server), discard it: `. <script> *> $null` (PowerShell) or `. <script> >/dev/null` (bash).
- Variables set: `IDF_PATH`, `IDF_TOOLS_PATH`, `IDF_PYTHON_ENV_PATH`, `ESP_ROM_ELF_DIR`, `OPENOCD_SCRIPTS`, plus tool dirs on `PATH`.
- Cloned-repo installs: run `export.sh` (bash/zsh), `export.ps1` (PowerShell), or `export.bat` (cmd) from the `esp-idf` folder.
- Use the ESP-IDF virtualenv's `python`; mixing in a system Python causes "package not found" errors.
