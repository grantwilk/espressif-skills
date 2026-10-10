---
name: esp-enter-download-mode
description: Put an Espressif chip into serial bootloader (download) mode, automatically or by hand, and fix "Failed to connect". Use when esptool or idf.py cannot connect to a device.
---

# Enter Download Mode

Normally automatic: esptool/`idf.py` toggle DTR/RTS (bridge chips) or use the USB-Serial/JTAG reset. If connecting fails:

1. Try esptool reset strategies: `--before default-reset` (default), `--before usb-reset` (native USB), `--before no-reset` (chip already in download mode).
2. More patience / lower speed: `--connect-attempts 20`, `-b 115200`.
3. Release the port: close any monitor, IDE serial console, or OpenOCD client holding it.
4. Manual entry: hold the BOOT button (the chip's boot-mode strapping pin; commonly GPIO0 or GPIO9, see the chip datasheet "Strapping Pins"), tap RESET/EN, then release BOOT. The chip's log then shows a download boot mode (for example `boot:0x... (DOWNLOAD...)`); verify with `esptool chip-id`.
5. No buttons: pull the strapping pin low with a wire while resetting, or power-cycle with it held low.
6. Leave download mode: esptool resets the chip after commands (`--after hard-reset`, default); otherwise press RESET/EN or run `esptool --port <PORT> --after hard-reset chip-id`.

Persistent failures (power, cables, auto-reset circuit): `esp-troubleshoot`.
Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/establish-serial-connection.html
