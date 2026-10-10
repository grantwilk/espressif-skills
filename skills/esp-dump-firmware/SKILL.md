---
name: esp-dump-firmware
description: Read ("dump") flash contents from a device to files (whole chip, a region, or a named partition) and inspect the dump. Use to back up, compare, or analyze what is on a device. Read-only.
---

# Dump Firmware and Flash Contents (read-only)

```bash
esptool --port <PORT> flash-id                              # note "Detected flash size"
esptool --port <PORT> -b 921600 read-flash 0 0x400000 full.bin   # whole chip: size in bytes (4 MB = 0x400000)
esptool --port <PORT> read-flash 0x10000 0x180000 app.bin   # one region
parttool.py -p <PORT> read_partition --partition-name nvs --output nvs.bin   # a named partition
```

Inspect:

```bash
esptool image-info app.bin                                   # needs a COMPLETE image (a truncated dump fails with "End of file reading segment")
esptool --port <PORT> read-flash 0x8000 0x1000 pt.bin        # partition table (default offset 0x8000)
python $IDF_PATH/components/partition_table/gen_esp32part.py pt.bin   # table as CSV (offsets and sizes)
python -c "d=open('full.bin','rb').read(); open('app.bin','wb').write(d[0x10000:0x10000+0x180000])"   # slice a partition from a full dump
```

- A dump is bytes, not source: matching it to a build uses the same image (`esptool verify-flash`, or compare hashes). Symbols need the matching `.elf` from the original build.
- Flash encryption on: dumps are ciphertext. Read-protected or secured devices may refuse reads.
- Dumps contain user data (NVS: Wi-Fi credentials, keys). Treat as sensitive and do not commit.
- Restore a dump: `esp-flash-binary`.
- esptool v4: `read_flash`.
- Docs: https://docs.espressif.com/projects/esptool/en/latest/esp32/esptool/basic-commands.html
