"""Validates the plugin manifest, skill frontmatter, and skill cross-references."""

import json
import re
import sys
from pathlib import Path


class SkillValidator:
    """Collects validation errors for the plugin manifest and every skill."""

    NAME_PATTERN = re.compile(r"^[a-z0-9]([a-z0-9-]*[a-z0-9])?$")
    FRONTMATTER_PATTERN = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
    REFERENCE_PATTERN = re.compile(r"`((?:esp|esp-idf)-[a-z0-9-]+)`")
    MAX_SKILL_LINES = 60
    # Espressif tool and directory names that look like skill names but are not skills.
    NON_SKILL_NAMES = frozenset({"esp-idf", "esp-clang", "esp-rom-elfs"})

    def __init__(self, root: Path) -> None:
        """
        Initializes this validator.

        Args:
            root (Path): The repository root containing `.cursor-plugin/plugin.json`.
        """

        self.root = root
        self.errors: list[str] = []

    def validate(self) -> list[str]:
        """
        Validates the whole repository.

        Returns:
            list[str]: The validation errors, empty if the repository is valid.
        """

        self._validate_manifest()

        skills_dir = self.root / "skills"
        if not skills_dir.is_dir():
            self.errors.append("missing 'skills' directory")
            return self.errors

        skill_names = {path.name for path in skills_dir.iterdir() if path.is_dir()}
        for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
            self._validate_skill(skill_dir, skill_names)

        return self.errors

    def _validate_manifest(self) -> None:
        """Validates `.cursor-plugin/plugin.json`."""

        path = self.root / ".cursor-plugin" / "plugin.json"
        if not path.is_file():
            self.errors.append(".cursor-plugin/plugin.json: file not found")
            return

        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            self.errors.append(f".cursor-plugin/plugin.json: invalid JSON ({error})")
            return

        name = manifest.get("name")
        if not isinstance(name, str) or self.NAME_PATTERN.match(name) is None:
            self.errors.append(f"plugin: name '{name}' must be lowercase kebab-case")

        for field in ("description", "version"):
            if not manifest.get(field):
                self.errors.append(f"plugin: '{field}' is required")

    def _validate_skill(self, skill_dir: Path, skill_names: set[str]) -> None:
        """
        Validates one skill folder, its frontmatter, size, and references.

        Args:
            skill_dir (Path): The skill folder containing `SKILL.md`.
            skill_names (set[str]): The names of every skill in the plugin.
        """

        label = f"skill '{skill_dir.name}'"
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            self.errors.append(f"{label}: missing SKILL.md")
            return

        text = skill_file.read_text(encoding="utf-8")
        match = self.FRONTMATTER_PATTERN.match(text)
        if match is None:
            self.errors.append(f"{label}: SKILL.md is missing YAML frontmatter")
            return

        frontmatter = match.group(1)
        name_match = re.search(r"^name:\s*(\S+)\s*$", frontmatter, re.MULTILINE)
        if name_match is None or name_match.group(1) != skill_dir.name:
            self.errors.append(f"{label}: frontmatter 'name' must equal the folder name")

        if re.search(r"^description:\s*\S", frontmatter, re.MULTILINE) is None:
            self.errors.append(f"{label}: frontmatter 'description' is required")

        line_count = len(text.splitlines())
        if line_count > self.MAX_SKILL_LINES:
            self.errors.append(
                f"{label}: {line_count} lines exceeds the {self.MAX_SKILL_LINES}-line limit"
            )

        for reference in sorted(set(self.REFERENCE_PATTERN.findall(text))):
            if reference not in skill_names and reference not in self.NON_SKILL_NAMES:
                self.errors.append(f"{label}: references unknown skill '{reference}'")


def main() -> int:
    """
    Runs the validator against this repository.

    Returns:
        int: The process exit code, 0 if valid and 1 otherwise.
    """

    errors = SkillValidator(Path(__file__).resolve().parent.parent).validate()
    for error in errors:
        print(f"error: {error}")

    if errors:
        return 1

    print("All skills are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
