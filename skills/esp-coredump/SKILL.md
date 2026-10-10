---
name: esp-coredump
description: Enable core dumps on an ESP-IDF device and retrieve, decode, and debug them after a crash with idf.py. Use for post-mortem debugging without a live debugger.
---

# Core Dumps

1. Enable (`esp-idf-configure`): `CONFIG_ESP_COREDUMP_ENABLE_TO_FLASH=y` (or UART), and a `coredump` partition in `partitions.csv`: `coredump, data, coredump, , 64K,` (`esp-idf-partition-table`). Rebuild and flash.
2. Reproduce the crash. The device saves the dump to flash.
3. Read and decode (ELF must match the flashed build, `esp-decode-crash`):

```bash
idf.py -p <PORT> coredump-info                 # crashed task, registers, callstack, tasks, memory
idf.py -p <PORT> coredump-info -s core.bin     # also save the raw core to a file
idf.py coredump-info -c core.bin               # decode a saved core, no device
idf.py -p <PORT> coredump-debug                # open GDB on the core
```

- Raw partition if needed: `parttool.py -p <PORT> read_partition --partition-name coredump --output core.bin`.
- UART mode: IDF Monitor decodes the dump printed on the console (`esp-monitor`).
- Clear a stale dump: `parttool.py -p <PORT> erase_partition --partition-name coredump`.
- Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/core_dump.html
