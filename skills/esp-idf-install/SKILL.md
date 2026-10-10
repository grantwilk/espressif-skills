---
name: esp-idf-install
description: Install ESP-IDF and its toolchain on Windows, macOS, or Linux using the ESP-IDF Installation Manager (EIM). Use when ESP-IDF or idf.py is not installed.
---

# Install ESP-IDF

Use EIM, Espressif's installer. Do not duplicate its docs; follow them.

1. Official guide per OS: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/index.html
2. Get the `eim` CLI (details: https://docs.espressif.com/projects/idf-im-ui/en/latest/cli_installation.html):
   - Windows: `winget install Espressif.EIM`
   - macOS/Linux: `brew tap espressif/eim && brew install eim`, or download the binary from the EIM guide
   - Arch Linux: the `eim-cli` package from Espressif's pacman repo (see the guide)
3. Install:
   - Interactive: `eim wizard`
   - Scripted: `eim install -i v6.0 -t esp32c3 -n true` (`-i` version(s), `-t` target(s), `-p` install path, `-n true` non-interactive)
   - Offline: `eim install --use-local-archive <archive.zst>`
4. Verify with `esp-idf-activate-env`: `idf.py --version` must print the version.

Notes:
- Prerequisites (Git, Python, build tools) are checked by EIM. On Windows `--install-all-prerequisites true` installs them; on macOS/Linux install them yourself first (see the OS page in the guide).
- Extra features (for example `mcp`, `pytests`, `docs`): `eim install --idf-features <list>`.
- Windows USB drivers: `eim install-drivers`.
- Alternative: the VS Code / Eclipse extensions or `install.sh` / `install.bat` + `export.sh` in a cloned `esp-idf` (see `esp-ecosystem`).
