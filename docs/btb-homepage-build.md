# Built To Book Homepage: Build Notes (updated 2026-10-01)

**Where it lives:** Unbounce page "Built 2 Book - Home Page" (client "Steve McKenna", client id 5678976, page uuid 4d5a0fe5-9c01-4978-be67-eef8056e3503). Variant B, "Built To Book Homepage v1 (staged)", is the champion (100% traffic). Variant A is the original hand-built blank page (discarded). Live URL: https://try.built2book.live/home. Variants B and C are set to noindex.

**Important:** Variants B, C and E are MCP-managed. They cannot be edited in the Unbounce builder. All changes go through Claude (update_variant_from_html) or by supplying updated HTML. Edits are staged until the page is published.

**Source of truth for design:** Miro wireframes (6 desktop sections plus Implementation Notes). Brand rules from the Visual Identity Guide v1.0 (Arial Black / Arial, not the Archivo Black / Inter used in the wireframes).

**Section order (Variant B):** Hero, trades strip, founder band, Lead System + Local Authority (October bonus banner above the cards, launch guarantee below), Outcomes (three jobs, before/after), CRM + Automations, Process + concept directions, FAQ, Close (GHL form embed), footer. Mobile: sticky bottom CTA.

**Form:** the close section embeds a GHL form (form id UeaJ18kaNNqe9LyQkGOW, "Built 2 Book Homepage Form"). The old Unbounce form script (btb-form) is dead code and can be removed.

**Chat widget:** the live GHL website uses the site-level chat widget `Built To Book Website Chat` (widget id `6abe848ed2e8beb1e4c344d9`). It is selected under Website Settings, not added as a custom body tracking script. Verified 2026-10-01 on `https://www.built2book.live/homepage` and `https://www.built2book.live/built-to-book`: one `chat-widget` source (`WEBSITE`), visible launcher, and open panel with the Built To Book welcome message. Proof screenshot: `docs/btb-chat-widget-proof.png`.

**Copy sources:** prices, inclusions, guarantee, cancellation terms and October bonus come from `docs/grnded-website-ghl-packages.md`. No testimonials, reviews or case studies were invented; hero image and concept cards are labeled placeholders.

## Changes 2026-10-01: GHL Chat Widget

- Created GHL live chat widget `Built To Book Website Chat` in the Built To Book location.
- Set the prompt to: "Have a question before you request a free mockup? Ask here."
- Set the chat title to `Built To Book` and the intro message to: "Ask a question or tell us what is holding back your website, Google profile, or follow-up. We will reply as soon as we can."
- Kept name and phone as required contact fields. Attachments and voice notes are off. Notification sound is on. Agency branding is off.
- Left the compliance notice and required consent checkbox on, with SMS and email reply consent wording.
- Attached the widget at the GHL website settings level for the `built2book.live/homepage` site.
- Removed the duplicate direct body embed after verifying the site-level widget was loading, so only one public widget renders.
- Opened the widget on the live page without submitting a test message. A full end-to-end test still needs Steve's review.

## Changes 2026-10-01: BW Plumbing Mockup Images

- Uploaded `bw-plumbing-home-desktop.png` and `bw-plumbing-home-mobile.png` to GHL Media Storage.
- Published the GHL homepage at https://www.built2book.live/built-to-book with those two images in the hero, replacing the old "Your project or crew photo goes here" placeholder.
- Saved a proof screenshot at `ghl-hero-after-publish.png` in the repo root.
- Staged the same hero mockup treatment in Unbounce active variants B, C and E. Variant B and E replace the placeholder hero card. Variant C adds the mockup visual beside the existing text-only hero.
- Unbounce was not republished. Public visitors at https://try.built2book.live/home will not see these Unbounce hero changes until Republish is clicked.
- Later on 2026-10-01, removed the green "Desktop and mobile concept preview" overlay from the GHL hero mockup custom code and published the page. Verified live at https://www.built2book.live/built-to-book; proof screenshot saved at `docs/btb-ghl-hero-no-label-proof.png`.
- Also on 2026-10-01, ChatGPT checked all Unbounce variants. Variants B, C and E had the green mockup label in their staged custom HTML, so a staged CSS hide rule was added to each custom HTML block. Variant A had no custom HTML mockup placeholder, and Variant D had no `.mock-label`. Staged previews for A, B, C, D and E all verified with no `.mock-label` rendering. Unbounce was not republished.

## Variant E: "Built To Book Homepage: Interview Voice (Feast or Famine)" (staged 2026-09-30)

Copy drafted from Steve's own answers in the coaching interview with Michelle Nedelec (see `docs/btb-golden-interview-questions.md`), written in plain trades language with no tech words. Challenger, 0% traffic, not published, noindex not set. Variant id 326597957, letter e. Reuses Variant B's stylesheet and the same GHL form embed.

Section order: hero, trades strip, "Sound familiar?" (five pain cards), "If nothing changes" (dark band), "You sound like one of us" (Steve's story plus plumber quote), "What we do" (three cards), how it works (four steps), close with GHL form, footer. Mobile: sticky bottom CTA.

Headline: "Booked out one month. Wondering where the work went the next." Close: "How soon do you want your weekends back?"

Deliberately left out: pricing and packages, any guarantee, stats, the October bonus, and the founder headshot (it is embedded in Variant B and was not copied). The founder line "Built in Calgary by Steve McKenna" is text only.

To confirm before publishing:
- The plumber quote ("Man, you sound like one of us.", attributed to "A local plumber, on our first call") reads as a testimonial. Steve to confirm it is fine unnamed, or swap it.
- "Text back within a minute" comes from the package details; confirm the wording.
- Replace this draft copy with owners' exact words once 3 to 8 interviews are done.

## Variant C: "Built To Book Contractor Growth Audit (Guarantee + 3-Tier)" (staged 2026-09-30)

Steve supplied the copy (8 sections). Challenger, 0% traffic, not published, noindex. Variant id 326596655. Same GHL form embed.

Section order: hero (tag, headline, sub-headline, paragraph, CTA), free mockup 4-step process, three jobs, value stack ($3,850+) and three pricing tiers, two guarantees, October $350 bonus bundle, FAQ (3 questions), final CTA with form.

Claude-written copy (Steve's brief left these blank): headline "10 Qualified Quote Requests in 60 Days, Or We Work For Free"; sub-headline "A done-for-you website, Google profile and 60-second follow-up system for local contractors, mocked up before you spend a dime."

Differences from the package doc and earlier decisions (all from Steve's supplied copy, flagged to him):
- Adds a Tier 3, Market Dominance ($4,997 + $997/mo, $5,994 due today), which is not in the package doc.
- Labels Local Authority "Most popular" (earlier decision: Lead System).
- Guarantee #1 is a 60-day results promise (10 qualified quote requests or work free); earlier decision was on-time launch only, never a results guarantee.
- Uses unsourced stats (80% of visitors lost, 55% of contracts go to first responder) and "5-star Google reviews".
- Bonus copy says first 5 contractors "per local area".
- Emojis and editorial notes from the brief were left out; check marks used instead. Em-dash removed from the lead-magnet body copy.

## Changes staged 2026-09-29 to Variant B (after Steve's decisions)

- **Hero:** one line under the intro: "Live job photos from CompanyCam on your site, and follow-up that books the quote."
- **CompanyCam widget:** added to Lead System launch includes ("uses your CompanyCam account"); Local Authority inherits it via "Everything in Lead System"; footer line says Online Starter also includes it. Steve confirmed the client supplies their own CompanyCam account.
- **Now Hiring page:** not on the page. It stays an add-on, with scope and price not yet set.
- **Launch guarantee:** block below the package cards. On-time launch (first month of management free if the agreed date is missed, counted from receipt of all required materials); approve the design before go-live, revisions within the package's pages and features.
- **October bonus:** moved from the fine print to a banner above the package cards. Wording: first five businesses that sign up in October; ends October 31. No remaining-spots count is shown, since none is tracked.
- **Founder band** under the trades strip: photo (Steve's headshot, small inline image), "Built in Calgary by Steve McKenna", two true lines about running trade businesses. No phone number (Steve chose to leave it off for now).
- **Not done (by decision):** prepay option (conflicts with the month-to-month decision).

## To do before or after publishing
- Republish Unbounce when Steve wants the B, C and E mockup hero changes live. The green "Desktop and mobile concept preview" label is already hidden in staged previews across all variants. Check desktop and mobile, especially the headshot and hero mockup framing.
- Variant C: Steve to confirm the flagged copy differences (Tier 3, guarantee, most popular label, stats), then give it a traffic share and publish (needs Steve's OK).
- Variant E: Steve to confirm the plumber quote and minute text-back wording, then decide on a traffic share and publish (needs Steve's OK). Decide whether it should carry pricing or the headshot.
- Real content: credentials and reviews, service area, service categories, Privacy and Terms pages.
- Test the GHL form end to end (contact created, notification fires).
- Test the GHL chat widget end to end (contact created or attached, notifications fire, routing is right).
- Privacy and Terms pages, then add footer links.
- Domain and trademark clearance, then remove noindex.
- Add tracked links per traffic source (see `docs/btb-lead-magnets.md`).
- Update the Notion package page with the CompanyCam decision.
