---
name: esp-secure-boot-flash-encryption
description: Plan and check secure boot, flash encryption, and related production security on Espressif chips, including the key and signing helper commands. Use when hardening firmware; every step needs explicit user approval.
---

# Secure Boot and Flash Encryption

**Irreversible on real devices.** Never apply to a development unit without approval; test on a spare chip or with virtual eFuses first (`esp-efuse`). Back up generated keys: losing them can make devices unflashable.

Check current state (read-only): `esptool --port <PORT> get-security-info`, `espefuse --port <PORT> summary`.

Plan (follow the docs; steps differ per chip and mode):
1. Read the guides: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/security/security.html, secure boot v2 https://docs.espressif.com/projects/esp-idf/en/stable/esp32/security/secure-boot-v2.html, flash encryption https://docs.espressif.com/projects/esp-idf/en/stable/esp32/security/flash-encryption.html
2. Choose **development** mode (reflashable) before **release** mode (one-way).
3. Generate keys with the project's helpers (stored outside the repo):
   `idf.py secure-generate-signing-key`, `idf.py secure-generate-flash-encryption-key`, `idf.py secure-generate-nvs-partition-key`; sign/verify: `idf.py secure-sign-data`, `idf.py secure-verify-signature`. Lower-level: `espsecure <command> --help`.
4. Enable via `esp-idf-configure` (`CONFIG_SECURE_BOOT*`, `CONFIG_SECURE_FLASH_ENC_ENABLED`), build, and first-boot flash.
5. Flash later builds with `idf.py encrypted-flash` / `encrypted-app-flash` where encryption is on (`esp-flash-project`). Plain `esptool write-flash` of unencrypted data will not run.
6. Audit with `get-security-info`; production USB/JTAG lock-down is an eFuse step (`esp-efuse`).
