# R&F Enterprise Edmonton

Static marketing site for **R&F Enterprise Edmonton**, a window cleaning service.

- **Live:** https://zaddywebbuilds.github.io/RF-Enterprise-Edmonton/
- **Phone:** 825-436-7579
- **Google Business Profile:** [R&F Enterprise Edmonton](https://www.google.com/maps/place/R%26F+Enterprise+Edmonton/@53.5266401,-113.4926628,10z/data=!3m1!4b1!4m6!3m5!1s0x2eb99197f89b7151:0xb7814b1458ebadea!8m2!3d53.5266401!4d-113.4926628!16s%2Fg%2F11z7p6sr6t)

## What the profile actually says

The Google listing gives a name, one category (*window cleaning service*) and a
phone number. It has **no street address, no opening hours, no website and no
reviews**. The site is written to match that:

- No address anywhere. Schema uses `addressLocality` only, with `areaServed`.
- No opening hours claimed. Copy says "call or text to book".
- No rating, no `aggregateRating`, no testimonials. `reviews.html` says plainly
  that there are none yet and links to the profile.
- Services are window and glass work only. No eavestroughs, gutters, pressure
  washing or solar panels, since the listing does not support them.

If the owner confirms hours, an address, or extra services, they go in
`tools/common.py` and the whole site picks them up on the next build.

## Layout

Every `.html` file is generated. Do not hand-edit them; they are overwritten.

```
tools/common.py          business facts, image catalogue, services, partials
tools/build_core.py      home, services, pricing, about, contact, reviews, legal
tools/build_services.py  eight service pages, six service-area pages
tools/build_blog.py      the notes index and eight articles
tools/build.py           runs all three, writes sitemap.xml and robots.txt
css/theme.css            the whole theme, hand-maintained
js/main.js               FAQ accordion, click tracking, header behaviour
images/                  25 photographs plus logo, favicon and share card
```

## Building

```bash
cd tools && python build.py
```

Rewrites all 31 pages plus `sitemap.xml` and `robots.txt`.

## The photographs

25 files, and that is the whole supply, so two rules are enforced in code.

**No page shows the same picture twice.** `common.py` holds the catalogue and an
allocator. Each page calls `new_page()`, then every slot calls
`pick("preferred-key")`. If that picture is already on the page the slot gets the
next free one. Alt text and captions travel with the photograph, so the words
always describe what is on screen. Ask a page for a 26th picture and the build
fails rather than quietly repeating one.

**Nothing is drawn larger than it is.** The files are 301x250 and 301x199.
`--photo-max` in `css/theme.css` caps every card box at 296px and the hero at
300px, which keeps every image at or under 1:1. Each `<img>` also carries its
true `width` and `height`. Bigger source files later? Raise those two numbers.

Grids with a fixed item count (4 reasons, 4 passes, 8 services, 8 notes) use
fixed column counts that divide evenly, so no row ends with a lone card beside
empty space.

**These are AI-generated illustrative scenes, not photographs of R&F's own
jobs, staff or equipment.** The footer says so on every page. The "R&F
Enterprise" marks visible on uniforms and kit in some shots are fabricated by the
image generator and are not the official logo. `before-after.jpg` is captioned
as an illustration. Replace these with real job photographs when there are some.

## Review popups

The popup component is built and wired up. It sits dormant because
`REVIEWS` in `tools/common.py` is an empty list, and nothing renders while
it is empty. Add entries and the popups start appearing bottom left, one at
a time, seven seconds after the page loads, with a close button that stops
them for the rest of the visit.

```python
REVIEWS = [
    dict(name="Dave M.", area="St. Albert", stars=5,
         text="Did the whole house inside and out, two storeys...",
         when="2 weeks ago"),
]
```

Up to about fifteen reads well. `area` should be a town from `LOCATIONS`.

**Only real reviews go in here.** A real customer wrote it, they are happy
for it to be on the site, and the name and town are theirs. Copy their
wording as they left it.

Inventing testimonials is not a grey area. Under the Competition Act a
false or misleading representation "to the public" covers a business's own
website, not just review platforms, and the 2024 amendments address
reviews directly. Penalties run to the greater of $10 million or three
times the benefit gained. Google also removes profiles over fabricated
testimonials found on a linked site. The fastest honest route to a full
list is to ask after each job: most people say yes, and a text asking for
a line about the work takes a minute to send.

## Contact flow

Calls and texts, not WhatsApp. `sms:` links carry a pre-written first line, and
the mock conversation in the call-to-action is a text thread. Edit `sms()` and
`PHONE` in `tools/common.py` to change it.

## Deployment

GitHub Pages serves `master` from the repository root. `.nojekyll` is committed.
