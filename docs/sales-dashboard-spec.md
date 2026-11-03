# Sales Dashboard Spec

Status: draft, started 2026-11-03. Owner: Steve. Delivered as a scheduled routine (daily morning brief plus a weekly summary).

## Goal

Results first: **meetings booked** and **proposals sent** (target 5 to 10 proposals a week). Under those, show the activity that drives them and where leads come from.

## What counts

- **Meeting:** any booked sales meeting or BNI 1-2-1, whether booked through a GHL calendar or added straight to Google Calendar.
- **Meeting outcome:** after every meeting, record whether there is something to sell: `Proposal needed`, `Referral partner only` or `No fit`. This is the step that turns meetings into proposals.
- **Proposal sent:** a proposal email in steve@grndedagency.com Sent mail (pricing, options or packages sent to a prospect), or an opportunity moved to Proposal sent (Grnded) or Offer sent (Built To Book) in GHL, counted once per prospect. Proposals often go out by email before the pipeline is updated, so the routine checks Sent mail every run and flags any proposal not yet reflected in GHL or unanswered after two days.

## Data sources

| Source | Access | What it gives |
|---|---|---|
| GHL Grnded Agency (`jryl6eycjlzYpcMBOkCb`) | Connected | Calendar events, opportunities, tags, conversations |
| GHL Built To Book (`ZGV8zr7m63uEb6IPhTSZ`) | Connected | Same |
| Gmail steve@grndedagency.com | Connected | Inbox: replies waiting, new inquiries |
| info@built2book.live | Via GHL Conversations once synced (Steve setting up) | Inbox |
| Google Calendar | Connected | Meetings booked outside GHL (many 1-2-1s) |
| Meta ads: Grnded Agency `1576121197146162`, Built To Book `1767145414396553` | Connected | Spend, leads, cost per lead |
| Google Ads | Not connected | Pending decision |
| Instagram and Facebook organic posts | To test | Posts published; DM leads via GHL tags |
| Instantly | Not yet | After the lead magnet campaign launches |

## GHL audit (2026-11-03)

### Grnded Agency

- Seven pipelines. The one in use is `001. Main Leads Pipeline` (`wFWKXKkB1tZJ1F4iVCy9`): 1 New Lead Inquiry, 2 Unable To Contact, 3 Contacted, 4 No Show, 5 Interested, 6 Sold, 7 Not Interested/Not Yet Ready, 8 Unqualified, 9 Spam.
- No meeting or proposal stages, so proposals cannot be counted today.
- 88 open opportunities: 71 in New Lead Inquiry (mostly old Facebook leads going back to July 2025), 6 Interested, 3 Contacted, 3 Not Yet Ready, 3 Unqualified, 2 No Show.
- Active calendars: Discovery Call, Book a call with Steve, Your 90-Day Pipeline Plan Session, Coaches Book A Call, 1-2-1 with Steve, Advisor 19-Minute Audit.
- GHL meetings Oct 5 to Nov 4, 2026: 12 (7 Discovery Call, 4 1-2-1, 1 Book a call). Several BNI follow-ups are booked through Discovery Call rather than 1-2-1.
- Lead source tags overlap: `bni`, `bni referral`, `source_bni_home`, `source_bni_outside`, `referral`, `referral partner`, `source_personal_network`, `source_meta_ads`, `source_social_facebook`, `source_social_instagram`, `source_social_linkedin`, `from instagram dm`, `from facebook messenger`, `src-leadwebia`, `src-scrapio`. The opportunity Source field is mostly `facebook` or blank.

### Built To Book

- Pipeline `Built To Book Sales` (`3scQVbaITnvra4WTVoaI`), nine stages including Call booked and Offer sent.
- Active calendar: `15 Minute Ads Intro Call` (`XgtLIdyZ2DZkrRVdt2Kh`).

## Proposed pipeline (same stages in both accounts)

1. New lead
2. Contacted
3. Meeting booked
4. Meeting held: proposal needed
5. Proposal sent
6. Won
7. Lost
8. Referral partner (1-2-1s with no sale, kept for referrals)
9. Nurture / not now

The GHL API cannot create or edit pipelines, so Steve edits stages by hand from this list. Stale opportunities are moved only with Steve's approval.

## Proposed source tags (one per contact)

`src-bni`, `src-referral`, `src-past-client`, `src-personal-network`, `src-meta-ads`, `src-google-ads`, `src-instagram`, `src-facebook`, `src-linkedin`, `src-cold-email`, `src-website`. Existing tags get mapped to these rather than deleted.

## Report layout

**Daily morning brief**
1. Today and tomorrow: meetings on the calendar, with source and whether a proposal is likely.
2. Needs action: meetings held with no outcome recorded, proposals due, inbox replies waiting, new leads not yet contacted.
3. Yesterday's numbers: meetings booked, proposals sent, new leads by source.

**Weekly summary**
1. Meetings booked and held, proposals sent (vs 5 to 10), won.
2. Leads, meetings and proposals by source.
3. Activity: outreach, follow-ups, posts published, ad spend and cost per lead.
4. Pipeline by stage in both accounts and what moved.

## Live setup (2026-11-03)

- **Notion:** page `Sales Dashboard` (https://app.notion.com/p/40d9ebf4f47f810f8479ee5acd3a9fcb) under 1. Projects / 1. Grnded Agency. Database `Daily Briefs`, data source `collection://c4985849-d2f5-4c9f-90f5-e588e07c1c28`, one row per brief. First row: Tue Nov 3.
- **Delivery:** Slack DM to Steve (user `U091YTV1BA8`) and email to steve@grndedagency.com, same content, linking to the Notion row.
- **Schedule:** scheduled task "Daily sales brief" (`trig_016z9UNNXrfH3uXD8H839H6p`), weekdays 6:47 am America/Edmonton, fresh session each run. Monday runs include the weekly summary. It was created without connectors; Steve must attach GHL, Gmail, Google Calendar, Notion, Slack and Meta in the claude.ai routines UI or runs cannot reach any data.
- **Pipeline cleanup:** 65 Grnded Agency opportunities in `1. New Lead Inquiry` created before Aug 2026 moved to `7. Not Interested/Not Yet Ready` (to be renamed Nurture). Six leads from Aug to Oct 2026 left in New.
- **Google Ads:** running in the Built To Book account since 2026-11-02; no connector yet. Until connected, tag those leads `src-google-ads` in GHL.
