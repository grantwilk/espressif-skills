---
name: esp-idf-migrate-version
description: Upgrade a project to a newer ESP-IDF release (or downgrade) with the migration guides and a clean rebuild. Use when moving between ESP-IDF major or minor versions.
---

# Migrate a Project Between ESP-IDF Versions

1. Install the target version beside the old one (`esp-idf-manage-versions`) and select it.
2. Read the migration guide for the release: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/migration-guides/index.html (also the release notes on https://github.com/espressif/esp-idf/releases).
3. Clean state: `idf.py fullclean`; if options were renamed, keep `sdkconfig.defaults`, delete `sdkconfig`, then `idf.py set-target <TARGET>` (`esp-idf-set-target`).
4. Refresh dependencies: `idf.py update-dependencies` and commit `dependencies.lock` (`esp-idf-components`).
5. Build and fix: `idf.py build` (`esp-idf-build`). Typical breaks: removed/renamed APIs, Kconfig renames, component splits, new default settings.
6. Re-run tests and size (`esp-idf-unit-test`, `esp-idf-size-analysis`), then flash and boot-check (`esp-flash-project`, `esp-capture-logs`).
7. Tools change with the version: ESP-IDF v5.x ships esptool v4 (`write_flash`), v6.0+ ships esptool v5 (`write-flash`). Update scripts and CI (`esp-idf-ci`).

Pin the exact version in CI and docs (`idf.py --version`).
