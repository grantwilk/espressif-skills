---
name: esp-idf-docs-lookup
description: Find authoritative Espressif documentation, API headers, examples, datasheets, and issue trackers for a given ESP-IDF version and chip. Use when you need to confirm an API, Kconfig option, or chip behavior.
---

# Find Authoritative Docs

Pin the version and chip. URL pattern: `https://docs.espressif.com/projects/esp-idf/en/<stable|latest|v6.0.1>/<TARGET>/<section>/<page>.html`. Sections: `get-started`, `api-guides`, `api-reference`, `security`, `migration-guides`.

```bash
idf.py docs --no-browser -t esp32c3 -v v6.0.1 -sp api-reference/system/log   # prints the URL
```

Local sources (always match the installed version):

- Headers and doxygen comments: `$IDF_PATH/components/<name>/include/`
- Examples: `$IDF_PATH/examples/` and the registry (https://components.espressif.com)
- Config options: `idf.py menuconfig` search, or the Kconfig reference page (`esp-idf-configure`)
- Tool help: `idf.py --help`, `idf.py <command> --help`, `esptool <command> --help`

Elsewhere:

- Chip datasheets and technical reference manuals: https://www.espressif.com/en/support/documents/technical-documents
- esptool, eFuse, secure-boot tools: https://docs.espressif.com/projects/esptool/en/latest/
- Component manager: https://docs.espressif.com/projects/idf-component-manager/en/latest/
- Bugs: https://github.com/espressif/esp-idf/issues; forum: https://esp32.com
- Release notes and migration: `esp-idf-migrate-version`

State the ESP-IDF version when citing behavior; APIs change between releases.
