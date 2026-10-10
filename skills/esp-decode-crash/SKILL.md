---
name: esp-decode-crash
description: Turn a panic, Guru Meditation Error, abort, or watchdog log with raw addresses into function names and source lines using the matching ELF. Use when firmware crashes or reboots unexpectedly.
---

# Decode a Crash

1. Capture the crash text (`esp-capture-logs`). Typical markers: `Guru Meditation Error`, `abort() was called at PC 0x...`, `Backtrace: 0x...:0x... 0x...:0x...`, `Task watchdog got triggered`, `Stack canary watchpoint triggered`, `Brownout detector was triggered`.
2. Use the ELF from the **same build** that is flashed: `build/<project>.elf`. The boot log prints `ELF file SHA256: ...` to compare; `esptool image-info build/<project>.bin` also shows the build identity. A different ELF gives nonsense.
3. Decode:
   - Live: `idf.py monitor` (or `python -m esp_idf_monitor -p <PORT> build/<project>.elf`) decodes backtraces automatically.
   - Offline, from pasted addresses (PC and backtrace PCs; the part before each `:`):
     `<toolchain>-addr2line -pfiaC -e build/<project>.elf 0x4200abcd 0x4200ef01`
     where `<toolchain>` is `riscv32-esp-elf` (C-series, H-series, P4) or `xtensa-<chip>-elf` (ESP32 `xtensa-esp32-elf`, S3 `xtensa-esp32s3-elf`). Same prefix as the compiler for the target.
   - Addresses in ROM (very low, for example `0x4000xxxx`): pass the chip's ROM ELF (`ESP_ROM_ELF_DIR`, `esp-rom-elfs` tool) with `--rom-elf-file` in `esp_idf_monitor`.
4. Interpret: `LoadProhibited` / `StoreProhibited` = bad pointer, `IllegalInstruction` / canary = stack overflow or corruption, `InstrFetchProhibited` = bad function pointer, `Task watchdog` = task starving or blocking.
5. For full state at the crash, use a core dump (`esp-coredump`) or a debugger (`esp-debug-jtag`).

Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/fatal-errors.html
