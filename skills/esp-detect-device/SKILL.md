---
name: esp-detect-device
description: Find which serial port an ESP32 or other Espressif chip is on, identify it by stable USB identifiers, and fix driver or permission problems on Windows, macOS, and Linux. Use before any flash, monitor, or debug action.
---

# Detect an Espressif Device

Ports change between machines and replugs. Detect every session; remember stable identifiers (USB VID/PID, USB serial number, MAC), never the port.

1. List ports with identifiers (needs `pyserial`, present in the ESP-IDF environment):
   `python scripts/find_ports.py` (this skill's folder; add `--json`, `--espressif`, `--serial <text>`, `--first`)
2. Or let esptool probe: `esptool chip-id` (no `--port` scans all), or filter: `esptool --port-filter vid=0x303a --port-filter serial=<USB_SERIAL> chip-id`
3. OS-native view:
   - Windows: `Get-PnpDevice -PresentOnly -Class Ports` and Device Manager
   - Linux: `ls /dev/serial/by-id/`, `ls /dev/ttyUSB* /dev/ttyACM*`, `lsusb`, `dmesg | tail`
   - macOS: `ls /dev/cu.*`, `system_profiler SPUSBDataType`
4. Confirm it is an Espressif chip and which one: `esp-chip-info`.

Recognize by USB ID:
- `303A:1001` = chip's built-in **USB-Serial/JTAG** (serial + JTAG; USB serial number is the chip MAC). Other `303A:xxxx` = Espressif native USB (for example ROM/TinyUSB CDC).
- Board-maker bridge chips, not Espressif: CP210x `10C4:EA60`, CH340/CH9102 `1A86:7523` / `1A86:55D3`, FTDI `0403:6001` / `6010` / `6014`. A bridge on a port does not prove an ESP is attached; run `chip-id`.

Fixes:
- Linux permissions: add your user to the serial group (`dialout` on Debian/Ubuntu/Fedora, `uucp` on Arch), then log out and in. JTAG access needs udev rules (see `esp-debug-jtag`).
- Windows drivers: `eim install-drivers`; bridge chips may need the vendor VCP driver. macOS: CH34x may need a vendor driver.
- WSL: USB is not passed through by default; use `usbipd-win`.
- Nothing listed: try another cable (many are charge-only) and port; enter `esp-enter-download-mode`.

Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/establish-serial-connection.html
