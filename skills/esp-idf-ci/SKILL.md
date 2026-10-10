---
name: esp-idf-ci
description: Build ESP-IDF projects in CI with the official Docker image, the esp-idf-ci-action GitHub Action, or a scripted EIM install. Use when setting up or debugging firmware CI.
---

# ESP-IDF in CI

**Docker image** (pin the tag to the project's version; tags like `v6.0.1`, `release-v6.0`):

```bash
docker run --rm -v "$PWD:/project" -w /project espressif/idf:v6.0.1 idf.py build
```

Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/idf-docker-image.html. In GitHub Actions, run the job in the image with `container: espressif/idf:<tag>`, then `. ${IDF_PATH}/export.sh` before `idf.py` steps.

**GitHub Action:** https://github.com/espressif/esp-idf-ci-action

```yaml
- uses: actions/checkout@v4
- uses: espressif/esp-idf-ci-action@v1
  with:
    esp_idf_version: v6.0.1
    target: esp32c3
    path: .
```

**No container:** `eim install -n true -i <version> -t <TARGET>` then `eim run "idf.py build"`.

Typical steps after build: `idf.py size | tee size.txt`, `idf.py merge-bin -f raw` (one flashable file, see `esp-merge-binaries`), upload `build/*.bin`, `build/<project>.elf`, size report. Keep `dependencies.lock` committed for reproducible builds. Flashing hardware from CI needs a self-hosted runner with the device attached (Docker on Linux: `--device=<PORT>`).
