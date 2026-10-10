---
name: esp-storage-images
description: Build and flash data-partition images (NVS, SPIFFS, FAT, LittleFS) from the host, and read them back. Use to preload configuration or files onto a device or inspect stored data.
---

# Storage Partition Images

Generate on the host (tools in `$IDF_PATH/components/`; each has `--help`):

```bash
python $IDF_PATH/components/nvs_flash/nvs_partition_generator/nvs_partition_gen.py generate values.csv nvs.bin 0x6000
python $IDF_PATH/components/spiffs/spiffsgen.py 0xF0000 data_dir spiffs.bin     # size, input dir, output
python $IDF_PATH/components/fatfs/fatfsgen.py data_dir --output_file fat.bin --partition_size 0x100000
```

- NVS CSV format and encryption: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/storage/nvs_partition_gen.html
- LittleFS: use the registry component `joltwallet/littlefs` (`esp-idf-components`).
- Let the build do it: in the project's `CMakeLists.txt` use `spiffs_create_partition_image`, `fatfs_create_spiflash_image`, or `nvs_create_partition_image`; with `FLASH_IN_PROJECT`, `idf.py flash` includes the image.

Flash an image to its partition:

```bash
parttool.py -p <PORT> write_partition --partition-name storage --input spiffs.bin    # overwrites that partition
esptool --port <PORT> write-flash <partition-offset> spiffs.bin                      # or by offset (esp-flash-binary)
```

Read back: `parttool.py -p <PORT> read_partition --partition-name storage --output out.bin` (`esp-dump-firmware`). Image size must equal the partition size from `esp-idf-partition-table`.

Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/storage/index.html
