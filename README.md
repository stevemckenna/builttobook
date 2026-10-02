# Built To Book

Working repo for **Built To Book**, the contractor-facing sub-brand of Grnded Agency (Steve McKenna, Calgary). It holds the packages, positioning, website notes, CRM campaign plans and other assets used to sell websites, Google profile setup and GHL follow-up systems to local contractors and home-service businesses.

This repo is the shared source of truth for both Claude and ChatGPT. Keep it private.

## Start here

1. [AGENTS.md](AGENTS.md): the rules, brand, voice and package facts every assistant must follow.
2. [MEMORY.md](MEMORY.md): running memory of active work, decisions, contacts and glossary.
3. The docs below, as needed.

## MCP setup

- `.mcp.json` defines `leadconnector` for HighLevel and `sheets` for Google Sheets. Claude must authorize `leadconnector` to the Built To Book location before using it for GHL reads or writes. The local Sheets MCP already tests as authorized on this machine.

## Docs

All working docs are in [`docs/`](docs/).

### Offer and packages

| File | What it is |
|---|---|
| [grnded-website-ghl-packages.md](docs/grnded-website-ghl-packages.md) | The four packages, pricing, inclusions, guarantee, ownership and cancellation terms. **Only source for pricing.** Still carries the old Grnded name. |
| [btb-offer-worksheet.md](docs/btb-offer-worksheet.md) | Pains, solutions, fears, 10x ideas, pillars and the milestone map |
| [btb-offer-doc-draft.md](docs/btb-offer-doc-draft.md) | Two-version offer document (A without investment, B with) for Breezedoc |
| [btb-lead-magnets.md](docs/btb-lead-magnets.md) | Lead magnet decision: the free website mockup is the only magnet for now |

### Brand and positioning

| File | What it is |
|---|---|
| [btb-niche-profile.md](docs/btb-niche-profile.md) | Who we serve, their pains, language, fears and objections |
| [btb-positioning.md](docs/btb-positioning.md) | Alternatives, three capabilities, value themes, best-fit client, market category |
| [btb-brand-of-you.md](docs/btb-brand-of-you.md) | Steve's philosophy, world, storylines, enemies and mechanism |
| [btb-branding-checklist.md](docs/btb-branding-checklist.md) | Branding checklist status, social handles, Canva kit, on-camera look |

### Marketing and sales system

| File | What it is |
|---|---|
| [btb-launch-and-content-plan.md](docs/btb-launch-and-content-plan.md) | Launch sequence, core premise, content types, October themes, first draft posts |
| [btb-daily-actions.md](docs/btb-daily-actions.md) | The fixed daily hour of sales and content actions, with KPIs |
| [btb-outreach-acceleration-plan.md](docs/btb-outreach-acceleration-plan.md) | Short sales sprint plan: weak-website offer, prospect scoring and tool options |
| [btb-mvf-map.md](docs/btb-mvf-map.md) | Minimum viable funnel: pipeline stages, automations, DM scripts, build order |
| [btb-conversion-ecosystem.md](docs/btb-conversion-ecosystem.md) | Profile to request page to confirmation to email sequence to offers |
| [btb-golden-interview-questions.md](docs/btb-golden-interview-questions.md) | Customer interview questions and an interview log |

### Website

| File | What it is |
|---|---|
| [btb-homepage-build.md](docs/btb-homepage-build.md) | How the Unbounce homepage was built, variants, form embed and launch to-do list |
| [7-star-tiles-mockup-notes.md](docs/7-star-tiles-mockup-notes.md) | Framer mockup notes, public proof and next content needed for 7 Star Tiles & Renovations |

### Assets

| File | What it is |
|---|---|
| `assets/Built-to-Book-Visual-Identity-Guide.pdf` | Visual identity v1.0: logo, color, type and graphic language |
| `assets/btb-homepage-hero-mockup-redacted.png` | Redacted homepage hero mockup image for public marketing and email signature use |
| `assets/btb-homepage-hero-mockup-redacted.webp` | WebP version of the redacted homepage hero mockup image |

## How to keep this in sync

- One copy of everything lives here. Edit files in this repo, not in separate chats or projects.
- Before starting work with Claude or ChatGPT, make sure the assistant is reading the latest version of the repo.
- After meaningful work, the assistant updates `MEMORY.md`. Keep edits small and say what changed.
- New docs go in `docs/` and get a row in the tables above.
- Never put passwords, API keys or client personal data in this repo.
