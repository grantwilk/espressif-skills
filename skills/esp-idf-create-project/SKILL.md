---
name: esp-idf-create-project
description: Create a new ESP-IDF project from scratch, from a bundled example, or from a Component Registry example. Use when starting a new firmware project.
---

# Create a Project

```bash
idf.py create-project my_app                 # new project in ./my_app
idf.py create-project -p /path/to/dir my_app # explicit destination
idf.py create-project-from-example "espressif/led_strip:led_strip_rmt_ws2812"
cp -r $IDF_PATH/examples/get-started/hello_world my_app   # bundled example (Windows: Copy-Item -Recurse)
cd my_app && idf.py set-target <TARGET>
```

Minimal layout (what `create-project` makes):

```text
my_app/
├── CMakeLists.txt        # includes $ENV{IDF_PATH}/tools/cmake/project.cmake
├── main/
│   ├── CMakeLists.txt    # idf_component_register(SRCS "main.c" INCLUDE_DIRS ".")
│   └── main.c            # app_main()
└── (sdkconfig.defaults)  # optional project config baseline
```

Next: `esp-idf-set-target`, `esp-idf-configure`, `esp-idf-build`.

Docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/build-system.html and examples at https://github.com/espressif/esp-idf/tree/master/examples
