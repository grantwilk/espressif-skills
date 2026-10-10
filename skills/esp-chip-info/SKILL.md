---
name: esp-chip-info
description: Read chip type, revision, MAC, flash size, security state, and eFuse summary from a connected Espressif chip, or inspect a firmware image file. Use to identify hardware or confirm a target before flashing.
---

# Chip and Image Information (read-only, safe)

```bash
esptool --port <PORT> chip-id            # chip type and ID
esptool --port <PORT> flash-id           # chip, revision, features, crystal, USB mode, MAC, flash vendor and size
esptool --port <PORT> read-mac
esptool --port <PORT> get-security-info  # secure boot / flash encryption / download-mode flags
esptool --port <PORT> read-flash-status  # flash status register
espefuse --port <PORT> summary           # eFuse values (see esp-efuse)
esptool image-info build/<project>.bin   # inspect an image file: target chip, segments, flash settings, app version
```

- Omit `--port` to auto-detect, or select by identifier: `--port-filter vid=0x303a --port-filter serial=<USB_SERIAL>` (`esp-detect-device`).
- The detected chip must equal the project target (`esp-idf-set-target`); a mismatch fails flashing.
- esptool v4: `chip_id`, `flash_id`, `read_mac`, `esptool.py ...`.
- The boot log also prints chip and app info (`esp-capture-logs`).
- Docs: https://docs.espressif.com/projects/esptool/en/latest/esp32/esptool/basic-commands.html
