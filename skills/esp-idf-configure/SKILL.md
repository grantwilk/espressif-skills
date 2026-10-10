---
name: esp-idf-configure
description: Configure an ESP-IDF project (Kconfig options, sdkconfig, sdkconfig.defaults) interactively or non-interactively. Use when changing log levels, flash size, features, or any CONFIG_ option.
---

# Configure a Project (Kconfig)

Interactive: `idf.py menuconfig` (TUI; `/` searches; needs a real terminal).

Non-interactive (agents, CI) — keep settings in version-controlled **`sdkconfig.defaults`**:

```text
CONFIG_ESPTOOLPY_FLASHSIZE_4MB=y
CONFIG_LOG_DEFAULT_LEVEL_INFO=y
```

1. Edit `sdkconfig.defaults` (per-target overrides: `sdkconfig.defaults.<TARGET>`).
2. Regenerate: delete `sdkconfig` (existing values override defaults), then `idf.py reconfigure`.
3. Check result: `grep CONFIG_NAME sdkconfig` or `idf.py config-report` (JSON in `build/`).

Other:
- Capture current changes as defaults: `idf.py save-defconfig` (writes only non-default options).
- Extra defaults files / alternate config: `idf.py -D SDKCONFIG_DEFAULTS="a.defaults;b.defaults" reconfigure`, or `idf.py --preset <name>` (`CMakePresets.json`).
- Option names, ranges, and help: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/kconfig-reference.html
- Commit `sdkconfig.defaults`; usually do not commit `sdkconfig`.
- Changing flash size or partition options can require `esp-idf-partition-table` updates.
