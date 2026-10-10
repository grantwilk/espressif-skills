---
name: esp-merge-binaries
description: Merge bootloader, partition table, and app images into one flashable binary (raw, hex, or UF2) for release, factory programming, or web flashing. Use when you need a single firmware file.
---

# Merge Binaries

After `idf.py build`:

```bash
idf.py merge-bin -o merged-binary.bin -f raw       # one image, flash at offset 0x0
idf.py merge-bin -f raw --pad-to-size 4MB          # pad with 0xFF to the flash size
idf.py merge-bin -f hex                            # Intel HEX; -f uf2 for UF2
idf.py uf2                                         # UF2 with all images (uf2-app: app only)

cd build && esptool merge-bin -o merged.bin @flash_args    # same, without idf.py
```

- Flash a raw merged image at the offset it was built for (default `0x0`): `esptool --port <PORT> write-flash 0x0 merged-binary.bin` (`esp-flash-binary`).
- Only images listed in `flash_args` are merged. Data partitions that are not part of the build (NVS, storage) stay out unless added (`esp-storage-images`).
- Keep the matching `.elf` and map with every released binary (`esp-decode-crash` needs it).
- esptool v4: `merge_bin`.
- Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/idf-py.html
