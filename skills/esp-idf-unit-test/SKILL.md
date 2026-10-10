---
name: esp-idf-unit-test
description: Run unit and integration tests for ESP-IDF code (Unity on target, pytest-embedded, or host/Linux builds). Use when writing or running automated firmware tests.
---

# Test ESP-IDF Code

Pick the layer, then follow the docs (test structure changes between versions): https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/unit-tests.html

- **On-target Unity tests:** write a test app with `unity` test cases, build it as a normal project (`esp-idf-build`), flash and run it (`esp-flash-project`), read results with `esp-monitor` / `esp-capture-logs`.
- **pytest-embedded (automated on hardware or QEMU):**
  1. Install the plugins into the ESP-IDF Python env: `pip install pytest-embedded-idf pytest-embedded-serial-esp` (add `pytest-embedded-qemu` for QEMU, `pytest-embedded-jtag` for JTAG). Exact set: see the docs above.
  2. Build the app, then: `pytest --target <TARGET> --port <PORT>` (QEMU alternative: `esp-idf-qemu`).
- **Host (Linux target) builds:** run logic without a chip. `idf.py --preview set-target linux`, then `idf.py build` and execute `build/<project>.elf`. See https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/host-apps.html
- Keep pure logic in components with no hardware dependencies so it can run on host.
- In CI see `esp-idf-ci`.
