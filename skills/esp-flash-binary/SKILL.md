---
name: esp-flash-binary
description: Write, verify, and restore raw firmware binaries at explicit flash offsets with esptool, without ESP-IDF or a project (build output, merged image, or a dump). Use for prebuilt images and factory programming.
---

# Flash Binaries with esptool

```bash
# All images of a build, with correct offsets and flash settings:
cd build && esptool --port <PORT> write-flash @flash_args

# One image at an explicit offset:
esptool --port <PORT> write-flash 0x10000 app.bin

# A merged image (see esp-merge-binaries) or a full dump (esp-dump-firmware):
esptool --port <PORT> write-flash 0x0 merged-binary.bin

# Verify flash contents against files (read-only):
cd build && esptool --port <PORT> verify-flash @flash_args
```

- Never hard-code offsets (the bootloader offset differs by chip); take them from `build/flash_args` / `flasher_args.json` or the partition table (`esp-idf-partition-table`).
- Flash settings: `--flash-mode`, `--flash-freq`, `--flash-size` (use `keep` or the values in `flash_args`); `-b <baud>` for speed; `--no-stub` for ROM-only talk.
- Select among several devices: `--port-filter vid=0x303a --port-filter serial=<USB_SERIAL>`.
- Writing overwrites existing data at those offsets; to keep data, write only the needed regions.
- esptool v4: `esptool.py write_flash`, `verify_flash`.
- Docs: https://docs.espressif.com/projects/esptool/en/latest/esp32/esptool/flashing-firmware.html
