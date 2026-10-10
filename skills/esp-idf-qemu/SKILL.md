---
name: esp-idf-qemu
description: Run ESP-IDF firmware in Espressif's QEMU emulator, optionally with GDB attached, with no hardware. Use for hardware-free runs of supported chips.
---

# Run Firmware in QEMU

1. Install the emulator once: `python $IDF_PATH/tools/idf_tools.py install qemu-riscv32 qemu-xtensa` (RISC-V chips use the first, Xtensa chips the second).
2. Build for a supported target (`esp-idf-set-target`, `esp-idf-build`). Supported chips and limits: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/qemu.html
3. Run:

```bash
idf.py qemu monitor              # boot the build in QEMU and show its console
idf.py qemu --gdb monitor        # terminal 1: wait for a debugger
idf.py gdb                       # terminal 2: attach (see esp-debug-jtag for GDB use)
idf.py qemu --graphics monitor   # with a display window (when supported)
```

- Flash and eFuse images are files in `build/` (`qemu_flash.bin`, `qemu_efuse.bin`); override with `--flash-file` / `--efuse-file`.
- Peripherals are only partly emulated; Wi-Fi/BLE and most analog features are not. Treat QEMU as a logic and boot check.
