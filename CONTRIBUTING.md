# Contributing to Open AI Hub

Welcome. This repository is a community-driven library of prompts,
skills, and Markdown files for LLMs and AI systems. Every asset here
is a **living document** — not a static post. It has a version,
a changelog, and a compatibility record that the community actively
maintains over time.

---

## The Core Principle: Prompts Are Code

Treat every prompt or skill file the way a developer treats source code:

- It has a **version number** (`1.0.0`, `1.1.0`, `2.0.0`)
- It has a **changelog** explaining every meaningful change
- It has a **compatibility record** tracking which models it works on
- It gets **deprecated** when superseded, not silently deleted
- It can be **forked** with full attribution to the original author

---

## Version Bump Rules

| Change Type | Bump | Example |
|---|---|---|
| New `tested_on_models` entry or typo fix | Patch `Z+1` | `1.0.0 → 1.0.1` |
| Prompt improved, behaviour unchanged | Minor `Y+1` | `1.0.1 → 1.1.0` |
| Prompt restructured, behaviour changes | Major `X+1` | `1.1.0 → 2.0.0` |
| Fork of another asset | Starts fresh | `1.0.0` |

---

## Asset Status Lifecycle
draft → experimental → reviewed → stable → deprecated → archive/


- **draft** — work in progress, not ready for review
- **experimental** — submitted, unverified, no stability guarantee
- **reviewed** — passed human review, safe to use
- **stable** — battle-tested, community-validated
- **deprecated** — superseded by a newer version, moved to `archive/`

---

## Before You Submit

1. Read this file fully
2. Read `CODE_OF_CONDUCT.md`
3. Search the repository to ensure your asset does not duplicate
   an existing one — if it improves one, fork it instead
4. Test your asset on at least one named LLM before submitting

---

## Folder Guide

| Asset Type | Folder |
|---|---|
| System prompts, role prompts | `prompts/ategory>/` |
| Model-specific skill files | `skills/<model>/` |
| Reusable prompt templates | `templates/<type>/` |
| Guides and documentation | `docs/` |
| Untested / experimental submissions | `experimental/` |

### Categories for `prompts/`
`coding` · `reasoning` · `creative-writing` · `data-analysis` · `agents` · `roleplay` · `general`

### Models for `skills/`
`claude` · `gpt` · `gemini` · `llama` · `deepseek` · `model-agnostic`

---

## File Naming Convention

- Use `kebab-case` — all lowercase, words separated by hyphens
- No spaces, no uppercase, no special characters
- Good: `python-bug-finder.md`
- Bad: `Python Bug Finder.md`, `pythonBugFinder.md`

---

## Required YAML Front Matter

Every asset file MUST begin with a YAML front matter block.
CI will automatically block your PR if any required field is missing.

### Required Fields
- `title`, `version`, `status`, `category`, `type`
- `author`, `created`, `last_updated`, `license`
- `description`
- `tested_on_models` — minimum one entry
- `changelog` — minimum one entry matching the current version

See `docs/guides/metadata-schema.md` for the full schema with examples.

---

## Submission Workflow

### Step 1 — Fork the Repository
Click **Fork** on GitHub to create your own copy.

### Step 2 — Create a Branch
```bash
git checkout -b add/your-prompt-name
```
Use prefixes: `add/`, `fix/`, `update/`, `deprecate/`

### Step 3 — Create Your Asset File
Place it in the correct folder with the correct filename.
Add the complete YAML front matter block at the top.

### Step 4 — Open a Pull Request
Use the PR template. Fill in every section completely.
Incomplete PRs will be closed with a request to complete the template.

### Step 5 — CI Validation
Automated checks run immediately. Fix any failures before
requesting human review. The CI checks:
- YAML front matter present and valid
- All required fields populated
- Semantic version format (`X.Y.Z`)
- File in correct folder
- At least one `tested_on_models` entry
- At least one `changelog` entry

### Step 6 — Human Review
A Trusted Contributor or above will review within 7 days.
Recognized Authors receive review within 48 hours.

### Step 7 — Merge and Earn Karma
Once merged, you earn +15 Karma (reviewed folders) or +5 Karma
(experimental). See `GOVERNANCE.md` for the full scoring table.

---

## Fork Attribution Rules

If your asset is based on or derived from an existing asset:

1. Set `forked_from` in your YAML to the original file path
2. Set `fork_changes` to describe what you changed
3. Check the Fork Attribution box in the PR template
4. Start your version at `1.0.0` — it is a new lineage

The original author automatically earns +5 Karma when you cite them.

---

## Adding Compatibility Data to Existing Assets

You do not need to be the original author to help.
If you test an existing asset on a new model:

1. Open a PR adding a `tested_on_models` entry to the YAML
2. Include the model name, result, notes, your handle, and date
3. If it breaks, add a `broken_on_models` entry instead
4. You earn +3 Contributor Score for each accepted entry

---

## Deprecating an Asset

If an asset is outdated or superseded:

1. Change its `status` to `deprecated`
2. Add a `changelog` entry explaining why
3. Open a PR — Core Maintainers will move it to `archive/`
4. Never delete files — they stay in `archive/` permanently

---

## Contributor Tiers

See `GOVERNANCE.md` for the full tier table, scoring rules, and privileges.

| Tier | Title | Key Requirement |
|---|---|---|
| 0 | Contributor | First merged PR |
| 1 | Trusted Contributor | 5+ merged PRs + 50 Karma |
| 2 | Recognized Author | 150 Karma + 80 Contributor Score + nomination |
| 3 | Core Maintainer | Nominated by existing Maintainer |

---

## Questions?

Open a GitHub Issue with the label `question`.
We are a friendly community — no question is too basic.