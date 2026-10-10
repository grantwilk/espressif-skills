---
name: esp-idf-manage-versions
description: List, install, switch, rename, and remove multiple ESP-IDF versions with EIM, and check which version a project uses. Use when changing or comparing ESP-IDF versions.
---

# Manage ESP-IDF Versions

```bash
eim list                               # installed versions, selected one marked
eim install -i v5.5.1,v6.0 -t esp32c3  # add versions (comma-separated); -t chip target(s)
eim select <version>                   # make a version the default
eim run "<command>" <version>          # run one command in a specific version
eim rename <version> <new-name>        # rename an install
eim remove <version>                   # delete one version
eim purge                              # delete everything (ask first)
```

- Current version: `idf.py --version`. Release list and support windows: https://github.com/espressif/esp-idf/blob/master/SUPPORT_POLICY.md
- Import an existing install described by a `tools_set_config.json`: `eim import <config.json>`.
- Switching versions changes `esptool`, `idf.py`, and Python deps. After switching, rebuild from clean: `idf.py fullclean`.
- Upgrading a project's code: `esp-idf-migrate-version`.
