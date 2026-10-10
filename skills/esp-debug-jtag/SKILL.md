---
name: esp-debug-jtag
description: Debug Espressif chips over JTAG with OpenOCD and GDB (built-in USB-Serial/JTAG or an external probe), including halting, reading registers, breakpoints, and flashing through OpenOCD. Use for live debugging, hangs, and hardware bring-up.
---

# JTAG Debugging (OpenOCD + GDB)

Connection:
- **Built-in USB-Serial/JTAG** (many newer chips, for example C3, S3, C6, H2): the USB cable is enough; config `board/<TARGET>-builtin.cfg`.
- **External probe** (ESP-Prog, FT2232H-based, J-Link): wire it per the docs; for example `-f interface/ftdi/esp32_devkitj_v1.cfg -f target/<TARGET>.cfg`.
- Several probes attached: `-c "adapter serial <USB_SERIAL>"` (`esp-detect-device`).
- Drivers/permissions: Windows built-in JTAG works with the default driver (`eim install-drivers`); external FTDI probes need the WinUSB driver on the JTAG interface (Zadig). Linux: install udev rules https://github.com/espressif/openocd-esp32/blob/master/contrib/60-openocd.rules into `/etc/udev/rules.d/`, then reload.

Non-interactive check (halt, read, resume):

```bash
openocd -f board/esp32c3-builtin.cfg -c init -c halt -c "reg pc" -c resume -c shutdown
```

Interactive session:

```bash
openocd -f board/esp32c3-builtin.cfg        # terminal 1 (GDB server on :3333); or: idf.py openocd
idf.py gdb                                  # terminal 2: GDB with the project ELF (gdbtui, gdbgui variants exist)
```

Useful GDB: `mon reset halt`, `thb app_main`, `c`, `bt`, `info threads`, `p <var>`, `x/8xw <addr>`, `mon program_esp build/<project>.bin 0x10000 verify`.

Flash through JTAG (no serial): `openocd -f board/esp32c3-builtin.cfg -c "program_esp build/<project>.bin 0x10000 verify reset exit"`.

Tips: build with `CONFIG_COMPILER_OPTIMIZATION_DEBUG=y` for readable stepping; the serial console and JTAG can run at once on USB-Serial/JTAG; OpenOCD and GDB must match the target chip.

Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/jtag-debugging/index.html
