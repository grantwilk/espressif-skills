---
name: esp-idf-build
description: Build, rebuild, and clean ESP-IDF firmware with idf.py and find the build outputs. Use whenever compiling firmware or investigating build artifacts.
---

# Build Firmware

```bash
idf.py build              # full build (alias: all)
idf.py app                # app only          idf.py bootloader   # bootloader only
idf.py -v build           # verbose (shows compiler commands)
idf.py reconfigure        # re-run CMake (after adding/removing files or components)
idf.py clean              # remove build outputs, keep config
idf.py fullclean          # wipe build/ (after toolchain/IDF version or config-structure changes)
idf.py -B build_alt build # alternate build directory
idf.py --ccache build     # use ccache
```

Outputs in `build/`:

- `<project>.bin` (app image), `<project>.elf` (symbols, for debug/decode), `<project>.map`
- `bootloader/bootloader.bin`, `partition_table/partition-table.bin`
- `flash_args`, `flasher_args.json` (offsets and files for flashing; see `esp-flash-binary`)
- `compile_commands.json` (for clangd), `project_description.json`, `config/sdkconfig.h`

Notes:
- A successful build ends with "Project build complete". Warnings are not failures unless the project enables warnings-as-errors.
- Errors from stale state: `idf.py fullclean` then rebuild. Hints are printed after failures (`--no-hints` disables).
- Adding source files: list them in `idf_component_register(SRCS ...)`, then `idf.py reconfigure`.
- Next: `esp-flash-project`, `esp-idf-size-analysis`. Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/build-system.html
