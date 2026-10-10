---
name: esp-toolchain-overview
description: Index and shared conventions for all Espressif toolchain skills (ESP-IDF, idf.py, esptool, espefuse, OpenOCD, IDF Monitor). Read first for any ESP32 or Espressif software task.
---

# Espressif Toolchain Overview

Scope: Espressif's **software** toolchain only. Not board selection, hardware design, or Arduino.

## Conventions (used by every skill)

- Commands run from the **project root** with the ESP-IDF environment active (`esp-idf-activate-env`).
- `<PORT>` is the serial port: `COM3` (Windows), `/dev/ttyUSB0` or `/dev/ttyACM0` (Linux), `/dev/cu.usbserial-*` or `/dev/cu.usbmodem*` (macOS). Never reuse a port from an earlier session; it changes between machines and replugs. Find it with `esp-detect-device`.
- `<TARGET>` is the chip: `esp32`, `esp32s3`, `esp32c3`, `esp32c6`, ... (`idf.py --list-targets`).
- Set `ESPPORT` / `ESPBAUD` env vars to avoid repeating `-p` / `-b`.
- Docs URL pattern: `https://docs.espressif.com/projects/esp-idf/en/<stable|latest|v6.0.1>/<TARGET>/...`. Prefer the version the project uses (`idf.py --version`).
- Every tool has `--help`; trust it over memory when versions differ.

## Version Notes

- **esptool v5+** (ESP-IDF v6.0+) uses hyphenated commands: `esptool write-flash`. **esptool v4** (ESP-IDF v5.x) uses `esptool.py write_flash`. Check with `esptool version`.
- `idf.py`, `espefuse`, `espsecure`, `parttool.py`, `otatool.py` ship with ESP-IDF; `esptool`, `idf-monitor`, `idf-size`, `esp-coredump` are Python packages in the ESP-IDF environment.

## Which Skill

- **Set up:** `esp-idf-install`, `esp-idf-activate-env`, `esp-idf-manage-versions`, `esp-idf-repair-env`, `esp-idf-mcp-server`
- **Project:** `esp-idf-create-project`, `esp-idf-set-target`, `esp-idf-configure`, `esp-idf-build`, `esp-idf-components`, `esp-idf-partition-table`, `esp-idf-migrate-version`
- **Quality:** `esp-idf-size-analysis`, `esp-idf-static-analysis`, `esp-idf-unit-test`, `esp-idf-qemu`, `esp-idf-ci`
- **Device:** `esp-detect-device`, `esp-chip-info`, `esp-enter-download-mode`, `esp-flash-project`, `esp-flash-binary`, `esp-erase-flash`, `esp-merge-binaries`
- **Observe:** `esp-monitor`, `esp-capture-logs`, `esp-decode-crash`, `esp-coredump`, `esp-debug-jtag`, `esp-runtime-diagnostics`
- **Read device data:** `esp-dump-firmware`, `esp-storage-images`, `esp-ota`
- **Security and fuses:** `esp-efuse`, `esp-secure-boot-flash-encryption`
- **Problems and lookup:** `esp-troubleshoot`, `esp-idf-docs-lookup`, `esp-ecosystem`

## Safety

Ask the user before anything irreversible or destructive: `espefuse burn-*` / `idf.py efuse-burn*`, enabling secure boot or flash encryption, `erase-flash`, overwriting a device that holds data worth keeping, or flashing a device that is not clearly a development unit. Reading is always safe.
