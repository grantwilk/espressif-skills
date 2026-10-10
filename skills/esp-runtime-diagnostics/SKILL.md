---
name: esp-runtime-diagnostics
description: Diagnose heap leaks, stack usage, CPU load, and task behavior in running ESP-IDF firmware with built-in APIs and trace tools. Use for memory leaks, watchdogs, stack overflows, and performance questions.
---

# Runtime Diagnostics

Add instrumentation, then read it over serial (`esp-capture-logs`).

- **Heap:** `esp_get_free_heap_size()`, `esp_get_minimum_free_heap_size()`, `heap_caps_print_heap_info(MALLOC_CAP_DEFAULT)`. Leaks/corruption: heap tracing (`CONFIG_HEAP_TRACING_*`) and poisoning (`CONFIG_HEAP_POISONING_*`). https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/heap_debug.html
- **Stacks:** `uxTaskGetStackHighWaterMark(NULL)` per task; overflow detection `CONFIG_FREERTOS_CHECK_STACKOVERFLOW_CANARY`.
- **Tasks and CPU load:** `vTaskList()` and `vTaskGetRunTimeStats()` need `CONFIG_FREERTOS_USE_TRACE_FACILITY`, `CONFIG_FREERTOS_USE_STATS_FORMATTING_FUNCTIONS`, and `CONFIG_FREERTOS_GENERATE_RUN_TIME_STATS`.
- **Watchdogs:** task watchdog and interrupt watchdog options under `CONFIG_ESP_TASK_WDT_*` / `CONFIG_ESP_INT_WDT_*`; a trigger prints the stuck tasks (`esp-decode-crash`).
- **Tracing/profiling:** application trace and SystemView over JTAG: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/app_trace.html
- **Static view:** footprint with `esp-idf-size-analysis`; RAM guidance: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/performance/ram-usage.html
- Enable options via `esp-idf-configure`; names vary slightly by version, confirm in the Kconfig reference.
