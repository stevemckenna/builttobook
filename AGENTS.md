# AGENTS.md: Built To Book

> **Shared instructions for every AI assistant working in this repo** (Claude, ChatGPT, Codex or any other). This repo is the single source of truth for the Built To Book project. `CLAUDE.md` simply points here, so there is only one copy of these rules to maintain.

> **About this project:** Built To Book is a sub-brand of Grnded Agency (Steve McKenna, Calgary). It sells websites, Google Business Profile setup, GHL CRM and follow-up systems to established local contractors and home-service businesses. Brand promise: **Websites built to win the next job.** Everything produced here should be capable, direct and dependable: plain language, specific proof, one obvious next step.

---

## Memory System

At the start of every session, read `MEMORY.md` (repo root) before doing anything else. Use what you find to inform your work. Don't announce what you found, just be informed by it.

When asked to "remember this," write it to `MEMORY.md` immediately and confirm it has been saved.

**Auto-update rule:** After any meaningful piece of work, update `MEMORY.md` without being asked. Record what was done, decisions made, and anything worth carrying into the next session. Use the format already in that file.

**Where things go (two tests):**

- Does it prescribe behavior? ("always," "never," "before doing X, do Y") → this file (`AGENTS.md`).
- Does it describe a fact that could change? (status, decisions, pricing, contacts) → `MEMORY.md`.
- When unsure, suggest which file it belongs in and ask to confirm.

**Working in a shared repo:** Both Claude and ChatGPT may edit these files. Before editing, make sure you have the latest version. Keep edits small and focused, and say in the commit message or your reply what you changed and why. Never silently overwrite another assistant's decisions: if a change contradicts something in `MEMORY.md`, flag it to Steve first.

---

## Brand Identity (read first)

Built To Book replaces Grnded Agency as the **client-facing brand** for this project. Grnded Agency remains the parent company behind it, but prospects, packages, websites, CRM campaigns and sales assets all carry the Built To Book name.

- Do not use "Grnded" or "Grnded Agency" in client-facing copy unless Steve asks (legal, billing or ownership wording may be an exception, so ask).
- The package document (`docs/grnded-website-ghl-packages.md`) still uses the old brand. Treat its offers and pricing as current, but rewrite the brand name when reusing any of it.
- Steve has decided **Lead System is the most popular package**, not Online Starter. The package document still labels Online Starter "Most Popular"; ignore that label and use Lead System.
- Creative direction is v1.0 (September 2026). Trademark and domain clearance must be completed before launch. Flag this if a task involves publishing, buying a domain or printing.

---

## Preferences

- Professional but conversational. Write like a contractor talks: short, direct, useful.
- Keep responses concise unless more detail is requested.
- Give one strong recommendation. Offer alternatives only when asked.
- **Never use em-dashes or double dashes.** Use commas, periods, semicolons, colons or parentheses.
- Bullets for lists; explanations in natural paragraphs.

---

## Rules

- Ask clarifying questions before starting a complex task.
- **Voice first:** before writing any client-facing content, apply the voice rules below.
- **Use:** specific, useful, candid, confident, local.
- **Avoid:** disruptive, cutting-edge, leverage, funnel hacking, AI-powered, and marketing theater in general.
- Lead with the result and give every asset one dominant next step. The primary conversion goal is **Request a free mockup**.
- Prove it with real work: projects, reviews, credentials, service areas, specific results. Never invent testimonials, reviews, credentials or results.
- Pricing comes only from the package document. Never quote a number from memory; re-check the source.
- When drafting emails, match the formality of the message being replied to, and check for an existing thread with that recipient before starting a new one.
- If unsure about something, say so. Don't guess.
- Before publishing, sending or spending anything on Steve's behalf (Gmail, GHL, Unbounce, Meta, Kit, Slack), confirm with him first.
- For Framer mockups, publish the mockup after Steve approves and share the live Framer website URL, not screenshot-only links. Screenshots are useful for review, but the handoff link should be the published Framer URL. Every mockup handoff should include a desktop version and a mobile version, either as viewport-specific preview links/screenshots or clearly labeled viewing instructions when the live Framer URL is responsive.
- **GHL MCP:** Use the repo `leadconnector` MCP from `.mcp.json` for Built To Book. It uses HighLevel's Claude-specific OAuth endpoint. In Claude web, the existing custom connector appears as `GHL` and is already connected to `https://services.leadconnectorhq.com/mcp/anthropic/v2`; do not try to add a duplicate connector with the same URL. Always pass the Built To Book location id explicitly: `ZGV8zr7m63uEb6IPhTSZ`. Do not use an old global `highlevel` private-token MCP for Built To Book unless Steve confirms it is newly authorized to this location.
- **Google Sheets MCP:** Use the repo `sheets` MCP from `.mcp.json` for Google Sheets work in this project. The local server lives at `C:\Users\SteveMcKenna\.gsheets-mcp\start-mcp-sheets.mjs` and exposes spreadsheet find, create, metadata, read, write, append and clear tools. If Claude cannot use Sheets, first check `auth-status`; as of 2026-10-01 the local token tests as authorized.
- **GHL forms:** the GHL API cannot create or edit forms. Give Steve a field spec and Custom CSS to paste into the GHL form builder, and say plainly that he has to build it. When styling GHL forms, follow the `ghl-form-styling` skill if you have it (no html/body selector prefixes, no CSS variables, always pair color with opacity 1).

---

## Asset Map

This repo is the source of truth for what exists and where. All working docs live in `docs/`.

| Asset | What it is | Go here when... |
|---|---|---|
| `assets/Built-to-Book-Visual-Identity-Guide.pdf` | Visual identity v1.0: brand foundation, logo, color, type, graphic language, applications | ...designing or writing anything visual, or checking brand rules |
| `assets/btb-homepage-hero-mockup-redacted.png` and `.webp` | Redacted homepage hero mockup image for public marketing, website previews and email signature use | ...showing the free mockup concept publicly without exposing a real prospect's private details |
| `docs/grnded-website-ghl-packages.md` | The four packages, pricing, inclusions, guarantee, ownership and cancellation terms, client onboarding steps | ...describing an offer, quoting a price, or writing sales copy |
| Website wireframes (Miro): https://miro.com/app/board/uXjVHgkBTEw=/ | Desktop and mobile homepage wireframes (6 sections each) plus Implementation Notes frame | ...building or reviewing the website |
| `docs/btb-homepage-build.md` | How the homepage was built, where it lives in Unbounce, form fields, and the launch to-do list | ...changing the homepage or preparing to launch it |
| `MEMORY.md` | Running memory: active work, decisions, contacts, glossary | ...starting any session |

The full list of working docs is in `README.md`. New assets (copy, campaigns, templates) are saved to `docs/` with a clear name and logged in `MEMORY.md`. Add a row here when a new asset type becomes permanent.

---

## References

| Resource | Read when... |
|---|---|
| Visual Identity Guide, sections 01 and 07 | Writing any copy or choosing tone |
| Visual Identity Guide, sections 03 to 05 | Designing pages, emails, social or decks |
| Package document | Naming, pricing or scoping any offer |
| Miro Implementation Notes frame | Building or changing the homepage |

---

## Brand at a Glance

- **Name:** Built To Book (written as three words, capitalized as shown)
- **Promise:** Websites built to win the next job.
- **Pillars:** Capable, Direct, Dependable.
- **Audience:** Established local contractors and home-service businesses whose work is stronger than their current website. They want more qualified inquiries, not jargon.
- **Logo:** Block-built B plus a booking checkmark. Primary lockup on Concrete or white; reversed lockup on dark fields; mark only for social avatars on a dark square. Clear space at least the width of the check stroke. Minimum width 150 px (lockup) and 24 px (mark). No stretching, rotating, shadows, recoloring pieces, or placing on busy photography.
- **Colors:**
  - Jobsite Ink `#151A18`: primary type, dark fields
  - Blueprint Blue `#2E6171`: trust, information, structure
  - Signal Green `#C7F36B`: primary CTA and booked state only
  - Safety Orange `#F26B38`: urgency and small alerts; keep rare
  - Concrete White `#F4F3ED`: primary canvas
  - Balance: Concrete/white 46%, Ink 26%, Blue 15%, Green 10%, Orange 3%
  - Best contrast: Ink on Concrete, White on Ink, Ink on Signal Green
- **Type:** Arial Black for display, Arial for body. H1 44 to 64 px, H2 30 to 40 px, H3 20 to 24 px Arial Bold, body 16 to 18 px, utility 12 to 14 px Arial Bold.
- **Interface:** Square, stable controls, 8 px maximum radius (4 to 8 px typical). Green for primary action, blue for informative states. No soft bubbles or decorative capsules.
- **Graphic language:** Blocks, checks (only for action, completion, proof, booked outcomes), subtle blueprint grids.
- **Photography:** Real finished projects, crews in context, tools in use, marked vehicles, local environments. Wide, well-lit, room for copy. Avoid staged handshakes, generic skylines, hard-hat portraits on white, dark stock overlays.

---

## Offers at a Glance

Full detail lives in the package document. Every package = one-time setup + monthly management plan.

| Package | Setup | Monthly | Due today |
|---|---|---|---|
| Google Ready | $297 | $147 | $444 |
| Online Starter | $597 | $197 | $794 |
| Lead System (Most Popular) | $997 | $297 | $1,294 |
| Local Authority | $1,997 | $497 | $2,494 |

The homepage wireframes feature **Lead System** and **Local Authority** as the primary offers, with a secondary path to compare the two.

---

## Website Build Rules (from Miro Implementation Notes)

Build the homepage as one continuous page in this order: **Hero, Lead System + Local Authority, Outcomes, CRM + Automations, Process, FAQ + CTA.**

- **Conversion goal:** Primary is request a free mockup. Secondary is compare Lead System and Local Authority.
- **Mobile first:** same offer depth as desktop, vertical package comparison, persistent primary CTA.
- **Content required before build:** 3 strong project images, service categories, credentials and reviews, service area.
- **Qualification fields:** name, company, website URL; package interest and budget; lead volume, urgency, current CRM.
- **Tracking:** form start and completion; CRM contact created; first response and booked call.

---

## Creating New Assets

When asked to create a new asset (page, campaign, sequence, one-pager, proposal template):

1. Confirm the goal, audience and single next step before drafting.
2. Apply the voice rules, color rules and package facts above.
3. Save finished work to `docs/` with a clear name.
4. Log it in `MEMORY.md` under Active Projects, add it to the table in `README.md`, and add a row to the Asset Map if it becomes a permanent asset type.
