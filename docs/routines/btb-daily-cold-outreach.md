# Built To Book daily cold outreach drafts (scheduled routine)

Reference copy of the scheduled task prompt, saved so it can be reviewed or reused as a structural template. The live task is the source of truth; if it changes, update this file.

## Summary

- **Purpose:** each weekday, draft (never send) short cold emails to prospects from a Google Sheet, each about one verified problem on the prospect's own website.
- **Schedule:** weekdays at 8:00 am, America/Edmonton (cron: `0 8 * * 1-5`).
- **Runs as:** a Claude scheduled task. Each run starts a fresh session.
- **Sending mailbox:** info@built2book.live (Gmail drafts only; Steve reviews and sends).
- **Prospect source:** Google Sheet "Built To Book Cold Outreach Prospects" (https://docs.google.com/spreadsheets/d/12OU_w-AtxamqSwRrV7fPdY64G1o1nLW0u6CtYCATg4o/edit). The routine works through rows already in the sheet; it does not source leads itself.
- **Connectors it relies on:** Gmail, Google Sheets (plus a browser to open prospect sites).

## Structure (the reusable pattern)

1. Check the inbox for replies, bounces and unsubscribes; update the sheet.
2. Take the next batch of unsent rows, ordered by priority.
3. Visit each prospect's site and verify the problem is real before writing.
4. Assign a persona so emails to different roles read differently.
5. Write one short email about one problem and its fix.
6. Plain-text URL rules and signature rules.
7. Create Gmail drafts only, verify them, never send.
8. Update the sheet, then give a short summary.

## Full prompt (verbatim)

```
Daily Built To Book cold outreach (drafts only, never send).

1. First check the info@built2book.live Gmail inbox for replies to earlier outreach. Mark those rows replied, bounced or opted_out in the sheet (any "unsubscribe" or "stop" = opted_out, never email again).

2. Open the Google Sheet "Built To Book Cold Outreach Prospects" (https://docs.google.com/spreadsheets/d/12OU_w-AtxamqSwRrV7fPdY64G1o1nLW0u6CtYCATg4o/edit). Take the next 15 rows where status = unsent. Order by gap priority first, then tier, then sheet order.

   Gap priority (highest first):
   A. No website / social or link page only / Google Business website link is broken
   B. Website down, Account Suspended, hosting error, parked domain, or the page will not load
   C. Site shows "Not secure" / no SSL
   D. Contact or booking form is broken (error page, PHP error, 404, dead submit) when a form is supposed to exist
   E. No contact form or online booking on an otherwise live site
   F. No tracking / no ad pixel (only when A to E do not apply)

   Skip or deprioritize (do NOT draft these unless nothing higher is left in the whole sheet):
   - No tap-to-call button alone
   - Dead call button alone when the phone number is still visible as plain text
   - Minor copy typos, missing homepage phone, careers@ as the only email

3. Before writing, open the prospect's website yourself (type the domain into the address bar). Confirm the main_gap is still true. If the sheet says "no form" but the site is actually down or suspended, use the worse problem (site down). If you cannot find a real A to E problem, skip the row and set status = skipped with a short reason in notes. Do not invent a tap-to-call pitch to fill the quota.

4. Assign a persona: Owner/Operator (info@ or name@ addresses, or blank role), Office/Ops Manager (office@, admin@, dispatch@), or Marketing Lead. Emails to different personas must read differently.

5. Write one short email per contact about ONE problem and its fix. Structure:
   - Name the specific problem you saw on their site, in plain words.
   - Say in one sentence what it likely costs them (in plain terms, no numbers or stats).
   - Say we offer low-cost fixes for exactly this, and say what the fix is.
   - One call to action: reply "yes" and I'll show you the fix, or a 15-minute call.
   Pitch ONLY the fix for that problem. Do NOT mention ads, Meta, Google Ads, the video offer, or other services unless the problem itself is about ads or tracking. Do not list other services.

   Problem to fix guide:
   - No website (social or link page only) or broken Google website link: a simple one-page site with their services, area, and a quote form to their inbox.
   - Website down / Account Suspended / will not load: get the site back online and keep it stable.
   - No SSL / "Not secure": set up the security certificate so browsers stop warning visitors away.
   - Broken contact or booking form: repair or replace the form so enquiries reach them again.
   - No contact form or online booking: add a simple booking or quote form that goes straight to their phone or email.
   - No tracking or ads at all / No ad pixel: set up tracking so they can see where calls and leads come from. Ads may be mentioned here only as an option once tracking is in place, never as the main pitch.
   - Tap-to-call alone: do not pitch this. Skip.

6. URL rules (hard):
   - When you name their website, write the bare domain only as plain text, for example greenvictory.ca or www.built2book.live
   - Never paste a Google redirect URL (anything starting with https://www.google.com/url?q=)
   - Never paste a link copied from Google Search, Google Sheets hyperlink tool, or a "Copy link address" on a search result
   - Do not turn the domain into a hyperlink. Leave it as plain text in the draft body and in the signature
   - Our site in the signature must be exactly: www.built2book.live (plain text, no https:// required, never a google.com/url wrapper)

7. Copy rules: plain language, no em dashes, no hype, no guarantees, no made-up stats, no fake testimonials, no pricing beyond saying it's low cost. Subject line references their problem or business, not ads.

8. Signature (exact format, with real line breaks, plain text only):

Steve McKenna
Built To Book
www.built2book.live

Built To Book (Grnded Agency)
3317 41 Street SW, Calgary, AB
You're getting this because your business email is listed publicly and I thought this might be relevant. Reply unsubscribe and I won't email again.

Do not put the signature on one long line. Do not hyperlink any of those lines. Do not add logos or HTML styling.

9. Create each email as a Gmail DRAFT from info@built2book.live. Do not send anything. Steve reviews and sends drafts himself. Before you finish, open each draft and confirm none of the body or signature contains google.com/url. If any draft does, delete that draft and recreate it with plain domains only.

10. In the sheet, set status = drafted, sent_date = today, and put the subject and the problem used in notes for each row. If you upgraded the gap (for example from "no form" to "Account Suspended"), update main_gap to match what you actually saw.

11. Finish with a short summary: how many drafts were created, which companies and which problem each one addressed (with the priority letter A to F), rows skipped and why, and any replies or unsubscribes found.
```

## Notes for reuse in another brand

- Reuse the structure above only. Do not carry over Built To Book wording, offers, signature, address or sheet.
- Swap in the new brand's sheet, sending mailbox, signature, offer and gap list.
- Keep the guardrails: drafts only, verify the problem on the live site before writing, one problem per email, plain-text domains, opt-out handling.
