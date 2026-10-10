---
name: esp-ota
description: Set up and inspect over-the-air (OTA) updates on ESP-IDF devices, including OTA partitions, otadata, slot switching, and rollback. Use for firmware update flows and boot-slot problems.
---

# OTA Updates

1. Partition table with two app slots and `otadata` (`esp-idf-partition-table`): `app` subtypes `ota_0`, `ota_1`, plus `data, ota`. Enable rollback if wanted: `CONFIG_BOOTLOADER_APP_ROLLBACK_ENABLE=y` (`esp-idf-configure`).
2. In firmware: `esp_ota_ops.h` (manual) or `esp_https_ota` (HTTPS download). After a new image boots successfully, call `esp_ota_mark_app_valid_cancel_rollback()`. Examples: `$IDF_PATH/examples/system/ota/`.
3. Inspect and control from the host (`otatool.py` is in `$IDF_PATH/components/app_update/`):

```bash
otatool.py -p <PORT> read_otadata                           # which slot is active/next
otatool.py -p <PORT> switch_ota_partition --slot 1          # boot the other slot next
otatool.py -p <PORT> read_ota_partition --slot 0 --output slot0.bin
otatool.py -p <PORT> write_ota_partition --slot 1 --input app.bin
otatool.py -p <PORT> erase_otadata                          # also: idf.py -p <PORT> erase-otadata, idf.py read-otadata
```

- `idf.py flash` writes the app to the first slot and resets `otadata`; later OTA images go to the other slot.
- Image must match the chip and partition size (`esptool image-info`, `esp-idf-size-analysis`).
- Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/ota.html and https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/esp_https_ota.html
