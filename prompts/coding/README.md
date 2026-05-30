# 🤖 Open AI Hub

> A free, community-driven, version-controlled library of prompts,
> skills, and Markdown files for LLMs and AI systems.

[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub Stars](https://img.shields.io/github/stars/jaypkallega/open-ai-hub?style=social)](https://github.com/jaypkallega/open-ai-hub/stargazers)

---

## What Is This?

**Open AI Hub** is a community-driven repository where anyone can
contribute, improve, and depend on high-quality prompts, skills,
and AI instruction files.

Unlike social prompt platforms where content ages and breaks silently,
every asset here is a **living document** — versioned, compatibility-tested,
and maintained by the community over time.

- **Free for all** — CC-BY-4.0 license, forever
- **Version controlled** — every change is tracked with a changelog
- **Model-aware** — every asset records which models it works on
- **Community governed** — contributor tiers reward both creators and maintainers
- **CI protected** — automated validation on every submission

---

## Quick Start

Find a prompt you need → copy it → use it in your LLM of choice.

Browse by category:

| Category | Description |
|---|---|
| [`prompts/coding/`](prompts/coding/) | Code review, debugging, refactoring |
| [`prompts/reasoning/`](prompts/reasoning/) | Logic, analysis, problem solving |
| [`prompts/creative-writing/`](prompts/creative-writing/) | Storytelling, copywriting, ideation |
| [`prompts/data-analysis/`](prompts/data-analysis/) | Data interpretation, reporting |
| [`prompts/agents/`](prompts/agents/) | Multi-step agent instructions |
| [`prompts/roleplay/`](prompts/roleplay/) | Persona and role-based prompts |
| [`prompts/general/`](prompts/general/) | General purpose prompts |
| [`skills/claude/`](skills/claude/) | Claude-specific skill files |
| [`skills/gpt/`](skills/gpt/) | GPT-specific skill files |
| [`skills/gemini/`](skills/gemini/) | Gemini-specific skill files |
| [`skills/llama/`](skills/llama/) | Llama-specific skill files |
| [`skills/model-agnostic/`](skills/model-agnostic/) | Works across all models |
| [`community-picks/`](community-picks/) | Top-voted by the community |
| [`experimental/`](experimental/) | New submissions under review |

---

## Example Asset

Here is what a fully documented asset looks like.
Every submission follows this standard:

> 📄 [`prompts/coding/python-bug-finder.md`](prompts/coding/python-bug-finder.md)

```yaml
title: "Python Bug Finder and Explainer"
version: "1.0.0"
status: "stable"
tested_on_models:
  - model: "claude-3-5-sonnet"
    result: "works"
  - model: "gpt-4o"
    result: "works"
```

Every asset includes:
- ✅ Semantic version number
- ✅ Status in the lifecycle (`draft → stable → deprecated`)
- ✅ Model compatibility record
- ✅ Example input and output
- ✅ Full changelog

---

## How To Contribute

1. **Fork** this repository
2. **Create a branch** — `git checkout -b add/your-prompt-name`
3. **Write your asset** with the required YAML front matter
4. **Open a Pull Request** — the PR template guides you through every field
5. **CI validates** your metadata automatically within seconds
6. **A reviewer approves** and your asset is merged

Every submission must include:
- A complete YAML front matter block
- At least one `tested_on_models` entry
- A `changelog` entry for the current version
- An `example_input` and `example_output`

Read the full guide: [`CONTRIBUTING.md`](CONTRIBUTING.md)

---

## Asset Lifecycle

Every asset travels through a trust pipeline:
draft → experimental → reviewed → stable → deprecated → archive/


| Status | Meaning |
|---|---|
| `draft` | Work in progress — not yet submitted |
| `experimental` | Submitted and CI-validated — awaiting human review |
| `reviewed` | Approved by a Trusted Contributor |
| `stable` | Battle-tested, community-validated, safe to depend on |
| `deprecated` | Superseded — use the replacement linked in the changelog |

Nothing is ever deleted. Deprecated assets move to [`archive/`](archive/)
and are preserved permanently.

---

## Contributor Tiers

We reward both **creation** and **maintenance** separately.

| Tier | Title | How To Earn |
|---|---|---|
| 0 | Contributor | First merged PR |
| 1 | Trusted Contributor | 5+ merged PRs + 50 Karma |
| 2 | Recognized Author | 150 Karma + 80 Contributor Score + nomination |
| 3 | Core Maintainer | Nominated by existing Maintainer |

See [`GOVERNANCE.md`](GOVERNANCE.md) for the full scoring table.

---

## Community

- 💡 **Have a prompt idea?** [Open an Issue](https://github.com/jaypkallega/open-ai-hub/issues/new?template=new_prompt.md)
- 🐛 **Found a broken prompt?** [Report it](https://github.com/jaypkallega/open-ai-hub/issues/new?template=bug_report.md)
- ⭐ **Like this project?** Star the repo to help others find it
- 🔒 **Found harmful content?** See [`SECURITY.md`](SECURITY.md)

---

## Important Files

| File | Purpose |
|---|---|
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to submit assets |
| [`GOVERNANCE.md`](GOVERNANCE.md) | Contributor tiers and scoring |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | Community standards |
| [`SECURITY.md`](SECURITY.md) | Reporting harmful content |
| [`LICENSE`](LICENSE) | CC-BY-4.0 |

---

## License

All assets in this repository are licensed under
[Creative Commons Attribution 4.0 International (CC-BY-4.0)](LICENSE).

You are free to use, share, and adapt any asset as long as you
give appropriate credit.

---

<div align="center">
Built by the community, for the community.<br>
<a href="https://github.com/jaypkallega/open-ai-hub/stargazers">⭐ Star this repo</a>
 · 
<a href="CONTRIBUTING.md">🤝 Contribute</a>
 · 
<a href="https://github.com/jaypkallega/open-ai-hub/issues">💬 Open an Issue</a>
</div>

