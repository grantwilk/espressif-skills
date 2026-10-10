---
name: esp-troubleshoot
description: Fast fixes for the most common ESP-IDF, esptool, flashing, monitor, and boot failures (cannot connect, port busy, wrong chip, boot loops, no log output, build errors). Use when a command or device misbehaves.
---

# Troubleshoot

| Symptom | Fix |
| --- | --- |
| `Failed to connect ... No serial data received` / `Wrong boot mode` | `esp-enter-download-mode`; check cable (data-capable), port, power; close other serial tools |
| `Could not open <PORT>`, busy, permission denied | Another program holds it (monitor, IDE, OpenOCD). Linux: serial group (`esp-detect-device`) |
| `Serial data stream stopped` / transfer errors | Lower baud (`-b 115200`), shorter cable, no hub |
| `This chip is ESP32-C3 not ESP32` / chip mismatch | `idf.py set-target <TARGET>` then rebuild (`esp-idf-set-target`) |
| `idf.py: command not found` | Activate env (`esp-idf-activate-env`) |
| Python/tool errors, missing packages | `esp-idf-repair-env` |
| Stale or odd build errors after config/version change | `idf.py fullclean`, then `idf.py build` |
| `Component not found` / undefined reference | Add `REQUIRES`/`PRIV_REQUIRES` or the file to `SRCS`; `idf.py reconfigure` (`esp-idf-components`) |
| Windows path/length errors | Use a short project path (for example `C:\proj`), enable long paths |
| Boot loop, `rst:0x...`, brownout | Check power supply/battery first; then `esp-decode-crash` |
| `invalid header: 0xffffffff`, `No bootable app partition` | Flash erased or wrong offsets/table: reflash everything (`esp-flash-project`, `esp-flash-binary`); check partition table |
| Image too big / `app partition is too small` | `esp-idf-size-analysis`, enlarge app partition (`esp-idf-partition-table`) |
| No log output | Wrong port or baud; console routed elsewhere (`CONFIG_ESP_CONSOLE_*`: UART vs USB-Serial/JTAG); log level (`esp-capture-logs`) |
| Garbled log | Baud mismatch or wrong crystal/clock setting; match `-b` to project config |
| JTAG cannot find the chip | Driver/udev rules, probe cable, wrong `-f` config (`esp-debug-jtag`) |
| Device behaves differently after a flash | Old data in NVS/otadata: `esp-erase-flash` (ask first) |

Always gather: `idf.py --version`, `esptool version`, the exact command, full output. `idf.py diag` produces a report to attach to a bug at https://github.com/espressif/esp-idf/issues.
