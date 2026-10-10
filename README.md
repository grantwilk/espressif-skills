# Espressif Skills

A Cursor plugin of 39 short, atomic agent skills for the **Espressif software toolchain**: ESP-IDF, `idf.py`, esptool, espefuse, OpenOCD, IDF Monitor, and related tools. Each skill holds only the commands and decisions for one task and links to Espressif's docs instead of copying them. Skills are OS-agnostic where possible and are not tied to any board or project.

> Unofficial community project. Not affiliated with or endorsed by Espressif Systems.

Out of scope: Arduino, board catalogs, and hardware design.

## Skills

Start with `esp-toolchain-overview` (shared conventions, index, safety rules).

| Area | Skills |
| --- | --- |
| Environment | `esp-idf-install`, `esp-idf-activate-env`, `esp-idf-manage-versions`, `esp-idf-repair-env`, `esp-idf-migrate-version` |
| Project | `esp-idf-create-project`, `esp-idf-set-target`, `esp-idf-configure`, `esp-idf-components`, `esp-idf-partition-table` |
| Build and analyze | `esp-idf-build`, `esp-idf-size-analysis`, `esp-idf-static-analysis`, `esp-idf-unit-test`, `esp-idf-qemu`, `esp-idf-ci` |
| Detect and flash | `esp-detect-device`, `esp-chip-info`, `esp-enter-download-mode`, `esp-flash-project`, `esp-flash-binary`, `esp-merge-binaries`, `esp-erase-flash` |
| Dump and storage | `esp-dump-firmware`, `esp-storage-images`, `esp-ota` |
| Observe and debug | `esp-monitor`, `esp-capture-logs`, `esp-decode-crash`, `esp-coredump`, `esp-debug-jtag`, `esp-runtime-diagnostics` |
| Security | `esp-efuse`, `esp-secure-boot-flash-encryption` |
| Reference | `esp-idf-docs-lookup`, `esp-idf-mcp-server`, `esp-troubleshoot`, `esp-ecosystem` |

Two skills bundle helper scripts (Python, `pyserial`): `esp-detect-device/scripts/find_ports.py` (list and filter serial ports by USB VID/PID/serial) and `esp-capture-logs/scripts/capture_serial.py` (bounded, non-interactive log capture).

Commands target ESP-IDF 6.x with esptool 5.x; skills note the esptool 4.x (ESP-IDF 5.x) differences where they matter.

## Install

Local (any machine): copy this repository to `~/.cursor/plugins/local/espressif-skills` (Windows: `%USERPROFILE%\.cursor\plugins\local\espressif-skills`; copy, do not symlink), then restart Cursor.

```bash
git clone https://github.com/grantwilk/espressif-skills ~/.cursor/plugins/local/espressif-skills
```

Public marketplace: submit the repository at https://cursor.com/marketplace/publish.

## Development

```bash
python tools/validate_skills.py   # manifest, frontmatter, size, and cross-reference checks
```

See [CONTRIBUTING.md](CONTRIBUTING.md). Licensed under the [MIT License](LICENSE).
