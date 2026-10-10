---
name: esp-idf-components
description: Create local components and manage Component Registry dependencies (idf_component.yml, dependencies.lock). Use when adding a library or structuring code into components.
---

# Components and Dependencies

Local component:

```bash
idf.py create-component -C components my_comp   # creates components/my_comp
```

- Register sources in its `CMakeLists.txt`: `idf_component_register(SRCS ... INCLUDE_DIRS ... REQUIRES ... PRIV_REQUIRES ...)`.
- Components in `components/` are found automatically; elsewhere, add to the top-level `CMakeLists.txt`: `set(EXTRA_COMPONENT_DIRS path/to/dir)`.

Registry / git dependencies (https://components.espressif.com):

```bash
idf.py add-dependency "espressif/led_strip^3.0.0"          # adds to main/idf_component.yml
idf.py add-dependency --git https://github.com/org/repo.git --git-ref v1.2 my_lib
idf.py update-dependencies                                 # re-resolve and update dependencies.lock
idf.py create-manifest --path components/my_comp           # add idf_component.yml to a component
idf.py add-dependency --component my_comp "espressif/cjson"  # add to a specific component
```

- Downloads go to `managed_components/` (do not commit). Commit `idf_component.yml` and `dependencies.lock`.
- Dependencies resolve on the next `idf.py build` / `reconfigure`.
- Publishing a component: `compote component upload` (docs below).
- Docs: https://docs.espressif.com/projects/idf-component-manager/en/latest/
