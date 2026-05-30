import os
import sys
import yaml

# ─────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────

REQUIRED_FIELDS = [
    "title",
    "version",
    "status",
    "category",
    "type",
    "author",
    "created",
    "last_updated",
    "license",
    "description",
    "tested_on_models",
    "changelog"
]

VALID_STATUSES = [
    "draft",
    "experimental",
    "reviewed",
    "stable",
    "deprecated"
]

VALID_TYPES = [
    "prompt",
    "skill",
    "template",
    "doc"
]

VALID_CATEGORIES = [
    "coding",
    "reasoning",
    "creative-writing",
    "data-analysis",
    "agents",
    "roleplay",
    "general"
]

# Folders and files to skip — not asset files
SKIP_DIRS = [
    ".github",
    "docs",
    "archive",
    "community-picks",
    ".git"
]

SKIP_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "GOVERNANCE.md",
    "SECURITY.md"
]

# ─────────────────────────────────────────
# VALIDATION
# ─────────────────────────────────────────

errors = []
files_checked = 0

for root, dirs, files in os.walk("."):

    # Skip unwanted directories
    if any(skip in root for skip in SKIP_DIRS):
        continue

    for file in files:

        # Only check markdown files
        if not file.endswith(".md"):
            continue

        # Skip governance files
        if file in SKIP_FILES:
            continue

        filepath = os.path.join(root, file)
        files_checked += 1

        # Open and read the file
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Check YAML front matter exists
        if not content.startswith("---"):
            errors.append(f"{filepath}: ❌ Missing YAML front matter block")
            continue

        # Parse the YAML block
        try:
            parts = content.split("---", 2)
            if len(parts) < 3:
                errors.append(f"{filepath}: ❌ YAML front matter not closed with ---")
                continue
            metadata = yaml.safe_load(parts[1])
        except Exception as e:
            errors.append(f"{filepath}: ❌ Invalid YAML syntax — {e}")
            continue

        if not isinstance(metadata, dict):
            errors.append(f"{filepath}: ❌ YAML front matter is empty or not a mapping")
            continue

        # Check all required fields exist and are not empty
        for field in REQUIRED_FIELDS:
            if field not in metadata or metadata[field] is None:
                errors.append(f"{filepath}: ❌ Missing required field '{field}'")

        # Validate status value
        status = metadata.get("status")
        if status and status not in VALID_STATUSES:
            errors.append(
                f"{filepath}: ❌ Invalid status '{status}'. "
                f"Must be one of: {', '.join(VALID_STATUSES)}"
            )

        # Validate type value
        asset_type = metadata.get("type")
        if asset_type and asset_type not in VALID_TYPES:
            errors.append(
                f"{filepath}: ❌ Invalid type '{asset_type}'. "
                f"Must be one of: {', '.join(VALID_TYPES)}"
            )

        # Validate version format (must be X.Y.Z)
        version = metadata.get("version")
        if version:
            parts_v = str(version).split(".")
            if len(parts_v) != 3 or not all(p.isdigit() for p in parts_v):
                errors.append(
                    f"{filepath}: ❌ Invalid version '{version}'. "
                    f"Must follow X.Y.Z format e.g. 1.0.0"
                )

        # Validate tested_on_models has at least one entry
        tested = metadata.get("tested_on_models")
        if tested is not None:
            if not isinstance(tested, list) or len(tested) < 1:
                errors.append(
                    f"{filepath}: ❌ 'tested_on_models' must have "
                    f"at least one entry"
                )
        
        # Validate changelog has at least one entry
        changelog = metadata.get("changelog")
        if changelog is not None:
            if not isinstance(changelog, list) or len(changelog) < 1:
                errors.append(
                    f"{filepath}: ❌ 'changelog' must have "
                    f"at least one entry"
                )

        # Validate license is present and not empty
        license_field = metadata.get("license")
        if license_field and str(license_field).strip() == "":
            errors.append(f"{filepath}: ❌ 'license' field is empty")

# ─────────────────────────────────────────
# RESULTS
# ─────────────────────────────────────────

print(f"\n📋 Files checked: {files_checked}")

if errors:
    print(f"❌ Validation failed with {len(errors)} error(s):\n")
    for e in errors:
        print(f"  • {e}")
    print("\nFix all errors above before your PR can be merged.")
    sys.exit(1)
else:
    print("✅ All asset metadata is valid. Good to go!\n")
    sys.exit(0)
    