---
name: esp-erase-flash
description: Erase an entire flash chip, a region, or a single partition (NVS, otadata, storage) on an Espressif device. Use to factory-reset data or recover from corrupt state. Destructive; ask first.
---

# Erase Flash (destructive: ask the user first)

```bash
esptool --port <PORT> erase-flash                     # whole chip (also: idf.py -p <PORT> erase-flash)
esptool --port <PORT> erase-region 0x9000 0x6000      # a byte range (start, size; both multiples of 4096)
parttool.py -p <PORT> erase_partition --partition-name nvs   # one partition by name
idf.py -p <PORT> erase-otadata                        # reset OTA slot selection to the factory/first app
```

- After a full erase the device has no bootloader or app; reflash everything (`esp-flash-project` or `esp-flash-binary`).
- Erase does **not** change eFuses (`esp-efuse`) or secure-boot/encryption state.
- Back up first when data matters: `esp-dump-firmware`.
- Typical uses: clear stored Wi-Fi/settings (`nvs`), unstick a bad OTA state (`erase-otadata`), start clean before factory programming.
- `--force` overrides protections on secured devices; do not use without being told.
- esptool v4: `erase_flash`, `erase_region`.
- Docs: https://docs.espressif.com/projects/esptool/en/latest/esp32/esptool/basic-commands.html
