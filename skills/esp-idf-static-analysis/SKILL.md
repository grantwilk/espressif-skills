---
name: esp-idf-static-analysis
description: Run clang-tidy and clangd diagnostics on ESP-IDF code using the Espressif clang toolchain and compile_commands.json. Use for linting, static analysis, or fixing editor IntelliSense for ESP-IDF projects.
---

# Static Analysis (clang-tidy / clangd)

Needs the optional Espressif clang toolchain: `python $IDF_PATH/tools/idf_tools.py install esp-clang` (check with `idf_tools.py check`).

clang-tidy through ESP-IDF (config in `.clang-tidy`):

```bash
export IDF_TOOLCHAIN=clang      # PowerShell: $env:IDF_TOOLCHAIN = "clang"
idf.py reconfigure
idf.py clang-check --run-clang-tidy-py run-clang-tidy   # writes warnings.txt
idf.py clang-html-report                                # optional HTML (pip install codereport)
```

clangd diagnostics on one file with the normal GCC build's database:

```bash
idf.py reconfigure                        # generates build/compile_commands.json
clangd --check=main/main.c --compile-commands-dir=build --log=error
```

- Use the `clangd` from `esp-clang` for ESP-IDF projects; stock clangd may not understand Xtensa/RISC-V GCC flags. Point your editor's clangd at `--compile-commands-dir=build`.
- Re-run `idf.py reconfigure` after adding files so `compile_commands.json` stays current.
- Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/idf-clang-tidy.html
