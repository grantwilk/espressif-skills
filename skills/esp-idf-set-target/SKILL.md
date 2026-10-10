---
name: esp-idf-set-target
description: Choose or change the chip target (esp32, esp32s3, esp32c3, ...) an ESP-IDF project builds for. Use when starting a project or when the build targets the wrong chip.
---

# Set the Chip Target

```bash
idf.py --list-targets            # supported targets (add --preview for preview chips)
idf.py set-target <TARGET>       # e.g. esp32c3
```

- `set-target` **deletes `sdkconfig` and the CMake cache**, then regenerates them from `sdkconfig.defaults` (and `sdkconfig.defaults.<TARGET>` if present). Keep intended settings in `sdkconfig.defaults`, not only in `sdkconfig`.
- Fixed per-checkout alternative: `export IDF_TARGET=<TARGET>` (PowerShell: `$env:IDF_TARGET="<TARGET>"`) before the first configure.
- The selected target shows in the `idf.py --help` header ("Selected target") and as `CONFIG_IDF_TARGET` in `sdkconfig`.
- Verify the connected chip matches: `esp-chip-info`.
- Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/idf-py.html
