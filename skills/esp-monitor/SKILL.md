---
name: esp-monitor
description: Open the interactive ESP-IDF serial monitor (IDF Monitor) with log filtering, timestamps, and automatic backtrace decoding. Use for interactive debugging in a real terminal; for agents and scripts use esp-capture-logs.
---

# IDF Monitor (interactive)

Needs a real terminal (TTY). Without one, use `esp-capture-logs`.

```bash
idf.py -p <PORT> monitor                        # reset the chip and show output
idf.py -p <PORT> flash monitor                  # flash first
idf.py -p <PORT> monitor --no-reset             # attach without resetting
idf.py -p <PORT> monitor --timestamps           # host timestamps on each line
idf.py -p <PORT> monitor --print-filter "wifi:W *:I"   # <tag>:<level> list; levels N E W I D V *
idf.py -p <PORT> monitor -b 115200              # monitor baud (default from the project config)
python -m esp_idf_monitor -p <PORT> build/<project>.elf    # standalone, any ELF
```

- Exit: `Ctrl+]`. `Ctrl+T` then `Ctrl+H` lists shortcuts (reset target, rebuild and flash, pause, and more).
- With the project ELF, crash backtraces and addresses are decoded automatically (`esp-decode-crash`); core dumps too (`esp-coredump`).
- Only one program can hold the port: close the monitor before flashing from another tool.
- No output or garbage: wrong baud, wrong console (`CONFIG_ESP_CONSOLE_*`: UART vs USB-Serial/JTAG), or wrong port (`esp-troubleshoot`).
- ROM boot messages print at 115200 even if the app uses another speed.
- Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/idf-monitor.html
