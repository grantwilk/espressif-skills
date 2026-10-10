---
name: esp-idf-repair-env
description: Diagnose and repair a broken ESP-IDF install (missing tools, bad Python env, missing optional features like mcp). Use when idf.py errors about tools, Python packages, or the environment.
---

# Diagnose and Repair the ESP-IDF Environment

Run in order until fixed (environment active, see `esp-idf-activate-env`). `$IDF_PATH` is `$env:IDF_PATH` in PowerShell.

1. `idf.py --version`, then `idf.py diag` (writes a diagnostic report to attach to bug reports).
2. Tools: `python $IDF_PATH/tools/idf_tools.py check`, then `python $IDF_PATH/tools/idf_tools.py install` for missing ones.
3. Python packages: `python $IDF_PATH/tools/idf_tools.py check-python-dependencies`, then `python $IDF_PATH/tools/idf_tools.py install-python-env`.
4. Optional feature packages: `python $IDF_PATH/tools/idf_tools.py install-python-env --features <name>`. Names match `$IDF_PATH/tools/requirements/requirements.<name>.txt` (`ci`, `docs`, `ide`, `mcp`, `test-specific`). Optional tools (for example QEMU): `idf_tools.py install qemu-riscv32 qemu-xtensa`.
5. Whole-install repair: `eim fix` (reinstalls tools and dependencies).
6. Last resort: `eim remove <version>`, then reinstall (`esp-idf-install`).

Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/idf-tools.html
Related: `esp-troubleshoot`.
