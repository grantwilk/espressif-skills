# Contributing

## Skill rules

- One task per skill, folder `skills/<name>/SKILL.md`; `name` in frontmatter equals the folder name.
- `description` says what the skill does and when to use it (include trigger terms).
- Short: at most 60 lines. Commands and decisions only; link to Espressif docs instead of copying them.
- OS-agnostic. Use `<PORT>`, `<TARGET>`, `<USB_SERIAL>` placeholders; never hard-code a port or machine value.
- Toolchain only: no Arduino, no board catalogs.
- Destructive or irreversible steps (erase, eFuse burn, secure boot, flash encryption) must say to ask the user first.
- Reference other skills by name in backticks.
- Verify commands against `--help` of the current ESP-IDF and esptool and check every URL before submitting.

## Workflow

1. Branch from `main`: `git switch -c <topic>`.
2. Make changes; run `python tools/validate_skills.py`.
3. Open a pull request; CI runs the same validator.

Bump `version` in `.cursor-plugin/plugin.json` only when cutting a release.
