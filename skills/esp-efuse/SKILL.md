---
name: esp-efuse
description: Read Espressif eFuses (chip configuration) safely with espefuse or idf.py, and understand which burns are irreversible. Use to inspect security/USB/JTAG settings or MAC; burning needs explicit user approval.
---

# eFuses

Reading is safe:

```bash
espefuse --port <PORT> summary          # human-readable values
espefuse --port <PORT> dump             # raw blocks
espefuse --port <PORT> check-error      # eFuse error flags
espefuse --port <PORT> get-custom-mac
idf.py -p <PORT> efuse-summary          # same, via the project (also: efuse-dump, show-efuse-table)
```

Burning is **permanent** (bits only go 0 to 1) and can brick a device or close its USB/JTAG/flash path. Only with explicit user approval, after reading `espefuse <command> --help` and the chip's docs:

```bash
espefuse --port <PORT> burn-efuse <NAME> <VALUE>     # shows a plan and asks to confirm; never add --do-not-confirm unprompted
espefuse --port <PORT> burn-key | burn-key-digest | burn-block-data | burn-bit | burn-custom-mac | read-protect-efuse
idf.py efuse-burn <NAME> <VALUE>                     # also efuse-burn-key, efuse-read-protect, efuse-write-protect
```

High-risk fields (names vary per chip; check `summary`): JTAG/USB-JTAG disable bits, `DIS_DOWNLOAD_MODE` and USB-Serial/JTAG download-mode disables, secure-boot and flash-encryption enables, read/write protection bits, flash voltage.

- Practice without risk: virtual eFuses (`CONFIG_EFUSE_VIRTUAL`, `espefuse --virt`) keep values in flash/a file.
- Security programming flow: `esp-secure-boot-flash-encryption`.
- Docs: https://docs.espressif.com/projects/esptool/en/latest/esp32/espefuse/index.html and https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/efuse.html
