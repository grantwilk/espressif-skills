---
name: esp-capture-logs
description: Capture serial log output from an Espressif device for a bounded time to the console or a file, optionally resetting the chip first, without an interactive terminal. Use for agents, scripts, CI, boot logs, and reproducing issues.
---

# Capture Logs (non-interactive)

Bundled script `scripts/capture_serial.py` (this skill's folder; needs `pyserial`, in the ESP-IDF environment). It never blocks forever.

```bash
python scripts/capture_serial.py --port <PORT> --seconds 15 --out boot.log                 # fixed time
python scripts/capture_serial.py --port <PORT> --reset --until "app_main" --seconds 30     # reset, stop on match
python scripts/capture_serial.py --vid 0x303a --serial <USB_SERIAL> --timestamps --out run.log   # pick port by identifier
```

Exit codes: `0` ok / matched, `1` no matching port, `2` cannot open port, `3` `--until` never matched.

Workflow for "does it boot / what happened":
1. `--reset` capture ~10-20 s; read the whole boot log.
2. Search it for `E (`, `W (`, `Guru Meditation`, `abort()`, `Backtrace:`, `rst:0x`, `Brownout`, `assert failed`.
3. Crash found: `esp-decode-crash`. Add more detail with `esp-idf-configure` (`CONFIG_LOG_DEFAULT_LEVEL_*`) or at runtime `esp_log_level_set("<tag>", ESP_LOG_DEBUG)`.

Notes:
- Log format: `<level> (<ms since boot>) <tag>: <message>`.
- Reset side effects: opening a port can reset the chip (USB-Serial/JTAG, DTR/RTS wiring). `--reset` does a standard EN pulse; if the board lacks auto-reset, press RESET.
- Port busy: close monitors/IDE consoles/OpenOCD clients using it. Found no output: wrong baud (`--baud`), or console not on this port (`CONFIG_ESP_CONSOLE_*`).
- Alternative inside ESP-IDF: `python -m esp_idf_monitor` needs a TTY (`esp-monitor`).
- Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/log.html
