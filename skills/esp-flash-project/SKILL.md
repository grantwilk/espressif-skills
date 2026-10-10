---
name: esp-flash-project
description: Flash an ESP-IDF project to a device with idf.py (all images, app only, bootloader, or partition table), optionally followed by monitor. Use to deploy a build to hardware.
---

# Flash a Project

Environment active, port known (`esp-detect-device`):

```bash
idf.py -p <PORT> flash                 # build if needed, flash all images, then reset
idf.py -p <PORT> app-flash             # app only (fastest iteration)
idf.py -p <PORT> bootloader-flash      # bootloader only
idf.py -p <PORT> partition-table-flash # partition table only
idf.py -p <PORT> -b 921600 flash       # faster baud (drop if unreliable)
idf.py -p <PORT> flash monitor         # then show serial output (needs a TTY)
```

- Set `ESPPORT=<PORT>` / `ESPBAUD=<baud>` to drop `-p` / `-b`.
- Flash offsets and files come from `build/flasher_args.json`; changes to partition table or flash settings need a full `flash`, not `app-flash`.
- Agents: avoid `monitor` (needs a TTY). Run `flash`, then `esp-capture-logs`.
- `--trace` shows tool interactions for bug reports; `--force` skips security/compatibility checks (use only when told).
- Encrypted devices: `idf.py encrypted-flash` / `encrypted-app-flash` (`esp-secure-boot-flash-encryption`).
- Errors: "Failed to connect" -> `esp-enter-download-mode`; others -> `esp-troubleshoot`.
- Flash prebuilt files without the project: `esp-flash-binary`.
- Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/idf-py.html
