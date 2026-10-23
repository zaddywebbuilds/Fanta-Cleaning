# Fanta Cleaning

Static marketing site for **Fanta Cleaning**, a house cleaning service in Etobicoke, Ontario.

- **Live:** https://zaddywebbuilds.github.io/Fanta-Cleaning/
- **Phone:** +1 647-451-5976
- **Address:** 24 Kingdom St, Etobicoke, ON M9P 1W2
- **Google Business Profile:** [Fanta Cleaning](https://www.google.com/maps/place/Fanta+Cleaning/@43.6955471,-79.5181012,17z/data=!3m1!4b1!4m6!3m5!1s0x882b313a58e5fb79:0xe9356a5decb88331!8m2!3d43.6955471!4d-79.5181012!16s%2Fg%2F11nvy82fz6)

## Layout

Every `.html` file in the repo is generated. Do not hand-edit them; they are
overwritten on the next build.

```
tools/common.py          business facts, service catalogue, shared partials
tools/build_core.py      home, services, pricing, about, contact, reviews, legal
tools/build_services.py  the ten service pages and six service-area pages
tools/build_blog.py      the blog index and twelve articles
tools/build.py           runs all three, then writes sitemap.xml and robots.txt
css/theme.css            the whole theme, hand-maintained
js/main.js               FAQ accordion, click tracking, header behaviour
images/                  18 photographs plus the logo, favicon and OG card
```

## Building

```bash
cd tools && python build.py
```

That rewrites all 37 pages, `sitemap.xml` and `robots.txt`. Change the copy in
`tools/`, never in the HTML.

## Changing business details

Phone number, address, hours, service area and the service catalogue all live at
the top of `tools/common.py`. Edit there and rebuild; every page picks it up.

## Previewing

```bash
python -m http.server 4178
```

Then open http://localhost:4178. Open the files directly and the relative asset
paths will not resolve.

## Deployment

GitHub Pages serves `master` from the repository root. `.nojekyll` is committed so
Pages publishes the files as they are.

## The photographs

There are 18 of them and that is the entire supply, so two rules are enforced
in code rather than by hand.

**No page shows the same picture twice.** `tools/common.py` holds the
catalogue and an allocator. Each page calls `new_page()`, then every slot calls
`pick("preferred-key")`. If that picture is already on the page, the slot gets
the next free one instead. Alt text and captions travel with the photograph, so
the words always describe what is actually on screen. Ask a page for a 19th
picture and the build fails rather than quietly repeating one — that is the
check, so keep any new section inside the budget.

**Nothing is drawn larger than it really is.** The files are 406x406 and
374x246; there is no larger master. Enlarging them is what made them look soft,
so `--photo-max` in `css/theme.css` caps every box that holds a photograph at
368px, the width at which the smallest still renders 1:1 in a 3:2 frame. Every
`<img>` also carries its true `width` and `height`. If you ever get bigger
source files, raise `--photo-max` and the whole site uses the extra detail.

Because of this the homepage lists its services as links rather than a second
photo grid: the rotating ring above it already spends eight pictures on those
same services, and 18 will not cover both. `services.html` carries the full
photo grid.

The images are AI-generated illustrations, not photographs of Fanta Cleaning
staff, equipment or completed jobs. They are used as generic interior imagery.
Do not caption them as documented work or real employees.
