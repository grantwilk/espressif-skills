---
name: esp-idf-size-analysis
description: Analyze firmware flash and RAM usage per component and source file, and diff two builds. Use when a build is too large, RAM is tight, or after a size regression.
---

# Firmware Size Analysis

Build first (`esp-idf-build`), then:

```bash
idf.py size                                   # summary: IRAM/DRAM/flash by memory type
idf.py size-components                        # per component (library)
idf.py size-files                             # per object/source file
idf.py size-components --format json2 --output-file size.json   # formats: default text csv json2 tree raw
idf.py size --diff path/to/old/project.map    # compare against another map file
python -m esp_idf_size build/<project>.map    # standalone tool on any map file
```

Reduce size: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/performance/size.html (compiler optimization for size, disable unused features, lower log verbosity). RAM: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/performance/ram-usage.html

- The `.map` and `.elf` in `build/` hold the raw data.
- Compare against the app partition size from `esp-idf-partition-table`; a build that outgrows its partition fails at link/flash time.
- Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/idf-size.html
