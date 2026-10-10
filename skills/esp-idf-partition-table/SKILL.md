---
name: esp-idf-partition-table
description: Define, build, flash, and inspect ESP-IDF partition tables, and read or write individual partitions with parttool. Use when changing flash layout or touching a named partition.
---

# Partition Tables

Define a custom table in `partitions.csv` (`Name, Type, SubType, Offset, Size, Flags`):

```csv
# Name,   Type, SubType, Offset,  Size,  Flags
nvs,      data, nvs,     ,        0x6000,
phy_init, data, phy,     ,        0x1000,
factory,  app,  factory, ,        1M,
storage,  data, spiffs,  ,        256K,
```

Blank offsets are filled automatically. Enable in `sdkconfig.defaults`: `CONFIG_PARTITION_TABLE_CUSTOM=y` and `CONFIG_PARTITION_TABLE_CUSTOM_FILENAME="partitions.csv"` (see `esp-idf-configure`). Everything must fit in the flash size; the table sits at `0x8000` by default. For OTA, use `ota_0` / `ota_1` app slots plus an `otadata` partition (see `esp-ota`).

```bash
idf.py partition-table            # build only the table
idf.py partition-table-flash      # flash it alone (needs a matching bootloader/app)
```

Inspect a table on the device (read-only):

```bash
esptool --port <PORT> read-flash 0x8000 0x1000 pt.bin
python $IDF_PATH/components/partition_table/gen_esp32part.py pt.bin     # prints CSV
```

`parttool.py` (in `$IDF_PATH/components/partition_table/`) works on the device by name:

```bash
parttool.py -p <PORT> get_partition_info --partition-name nvs --info offset size
parttool.py -p <PORT> read_partition  --partition-name storage --output storage.bin
parttool.py -p <PORT> write_partition --partition-name storage --input storage.bin   # overwrites
parttool.py -p <PORT> erase_partition --partition-name storage                       # destructive
```

Ask before write/erase on devices with data worth keeping. Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/partition-tables.html
