# -*- coding: utf-8 -*-
"""Shared data and HTML partials for the R&F Enterprise site.

Run tools/build.py to regenerate every page from these partials.
"""

import io
import os
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ----------------------------------------------------------------------
# Business facts, from the Google Business Profile.
#
# The profile lists a name, a category and a phone number. It has no
# street address, no opening hours, no website and no reviews. Nothing
# on this site may claim any of those until the owner confirms them.
# ----------------------------------------------------------------------
NAME = "R&amp;F Enterprise"
NAME_FULL = "R&amp;F Enterprise Edmonton"
TAGLINE = "Window Cleaning &middot; Edmonton"
PHONE = "825-436-7579"
PHONE_TEL = "+18254367579"
PHONE_SMS = "+18254367579"
CITY = "Edmonton"
REGION = "AB"
AREA = "Edmonton &amp; area"
HOURS_SHORT = "Call or text to book"
BASE = "https://zaddywebbuilds.github.io/RF-Enterprise-Edmonton"
MAPS = ("https://www.google.com/maps/place/R%26F+Enterprise+Edmonton/"
        "@53.5266401,-113.4926628,10z/data=!3m1!4b1!4m6!3m5!"
        "1s0x2eb99197f89b7151:0xb7814b1458ebadea!8m2!3d53.5266401!4d-113.4926628"
        "!16s%2Fg%2F11z7p6sr6t")
LAT, LON = "53.5266", "-113.4927"


def sms(message):
    """A text message link with the first line already written."""
    return "sms:%s?&body=%s" % (PHONE_SMS, urllib.parse.quote(message))


SMS_GENERAL = sms("Hi R&F, I'd like a window cleaning quote. My address is ")
SMS_QUOTE = sms("Hi R&F, I'd like a quote. Address and how many windows: ")

# ----------------------------------------------------------------------
# The photographs. Twenty five files, 301x250 or 301x199, which is why
# css/theme.css caps every box at 296px. Pages draw through pick() so no
# page shows the same one twice.
# ----------------------------------------------------------------------
IMAGES = [
    dict(key="residential-squeegee", w=301, h=250,
         alt="Window cleaner drawing a squeegee down an exterior pane",
         cap="Exterior glass"),
    dict(key="modern-home", w=301, h=250,
         alt="Modern two storey home with large windows", cap="Whole home"),
    dict(key="commercial-pole", w=302, h=250,
         alt="Cleaner reaching upper commercial glass with an extension pole",
         cap="Upper storeys"),
    dict(key="squeegee-soapy", w=301, h=250,
         alt="Squeegee pulling soap off wet glass", cap="The wet pass"),
    dict(key="sunlit-living-room", w=301, h=250,
         alt="Living room windows letting full daylight in", cap="After"),
    dict(key="ladder-upper", w=301, h=250,
         alt="Cleaner on a ladder working an upper window", cap="Second storey"),
    dict(key="cloth-polish", w=301, h=250,
         alt="Gloved hand polishing glass with a folded cloth", cap="Final polish"),
    dict(key="commercial-building", w=301, h=250,
         alt="Low rise commercial building faced with glass", cap="Commercial"),
    dict(key="frame-detail", w=301, h=250,
         alt="Cloth run along a window frame and sill", cap="Frames"),
    dict(key="pole-on-home", w=301, h=199,
         alt="Water fed pole reaching the upper windows of a house",
         cap="Pole work"),
    dict(key="brush-closeup", w=301, h=199,
         alt="Soft brush working over wet glass", cap="Loosening dirt"),
    dict(key="interior-microfiber", w=301, h=199,
         alt="Microfiber cloth wiping an interior pane", cap="Interior glass"),
    dict(key="office-view", w=302, h=199,
         alt="Clear office window looking out over the city", cap="Offices"),
    dict(key="skylight", w=301, h=199,
         alt="Cleaner reaching a skylight with a pole", cap="Skylights"),
    dict(key="screen-brush", w=301, h=199,
         alt="Brush drawn across a window screen", cap="Screens"),
    dict(key="interior-framed", w=301, h=198,
         alt="Cleaner working an interior window from inside the room",
         cap="Inside"),
    dict(key="storefront", w=302, h=198,
         alt="Storefront glass being cleaned from the sidewalk",
         cap="Storefronts"),
    dict(key="bay-window", w=301, h=199,
         alt="Bay window left clear across all three panes", cap="Bay windows"),
    dict(key="two-storey", w=301, h=199,
         alt="Two storey house with every window done", cap="Full exteriors"),
    dict(key="water-fed", w=301, h=199,
         alt="Water fed brush running over an exterior pane", cap="Pure water"),
    dict(key="retail-front", w=301, h=199,
         alt="Row of retail frontage with clean glass", cap="Retail rows"),
    dict(key="track-detail", w=301, h=199,
         alt="Small brush clearing grit out of a window track", cap="Tracks"),
    dict(key="sill-wipe", w=302, h=198,
         alt="Cloth wiping along an interior sill", cap="Sills"),
    dict(key="supplies", w=301, h=199,
         alt="Squeegees, cloths and buckets laid out", cap="The kit"),
    dict(key="before-after", w=301, h=199,
         alt="Illustration comparing a dirty pane with a clean one",
         cap="Illustration only"),
]
for _r in IMAGES:
    _r["src"] = "images/%s.jpg" % _r["key"]
BY_KEY = dict((r["key"], r) for r in IMAGES)

_used = set()


def new_page():
    """Start a page. Every pick() after this returns a different photograph."""
    _used.clear()


def pick(*prefer):
    """The best unused photograph for a slot.

    Give it the keys you would like, best first. If they are all spoken for
    on this page it falls through to whatever is still free, so a slot never
    repeats a picture already on screen. Alt text and caption travel with the
    record, so the words describe the photograph actually shown.
    """
    for key in prefer:
        if key and key in BY_KEY and key not in _used:
            _used.add(key)
            return BY_KEY[key]
    for rec in IMAGES:
        if rec["key"] not in _used:
            _used.add(rec["key"])
            return rec
    raise RuntimeError(
        "this page asks for more than the %d photographs available" % len(IMAGES))


def img_tag(rec, depth=0, cls="", lazy=True, alt=None):
    """An <img> carrying its own real pixel size, so nothing is guessed."""
    return '<img%s src="%s%s" alt="%s" width="%d" height="%d"%s>' % (
        (' class="%s"' % cls) if cls else "",
        "../" * depth, rec["src"], alt if alt is not None else rec["alt"],
        rec["w"], rec["h"], ' loading="lazy"' if lazy else "")


# ----------------------------------------------------------------------
# Services. The profile says "window cleaning service" and nothing else,
# so everything here is glass work. No eavestroughs, no pressure washing,
# no gutters, until the owner says otherwise.
# ----------------------------------------------------------------------
SERVICES = [
    dict(slug="residential-window-cleaning-edmonton", short="Residential Windows", ring=True,
         img="residential-squeegee", thumb="two-storey",
         title="Residential Window Cleaning in Edmonton",
         blurb="Inside and out, frames and sills included. Bungalows through to three storey walkouts."),
    dict(slug="commercial-window-cleaning-edmonton", short="Commercial Glass", ring=True,
         img="commercial-building", thumb="commercial-pole",
         title="Commercial Window Cleaning in Edmonton",
         blurb="Offices, clinics and walk-up buildings on a set schedule, done before your doors open."),
    dict(slug="storefront-window-cleaning-edmonton", short="Storefronts", ring=True,
         img="storefront", thumb="retail-front",
         title="Storefront Window Cleaning in Edmonton",
         blurb="Weekly or biweekly frontage for shops and restaurants. Fingerprints, salt film, the lot."),
    dict(slug="interior-window-cleaning-edmonton", short="Interior Glass", ring=True,
         img="interior-framed", thumb="interior-microfiber",
         title="Interior Window Cleaning in Edmonton",
         blurb="Winter work, mostly. Condensation marks, cooking film and whatever the dog left on the patio door."),
    dict(slug="window-screens-tracks-edmonton", short="Screens &amp; Tracks", ring=True,
         img="screen-brush", thumb="track-detail",
         title="Window Screen &amp; Track Cleaning in Edmonton",
         blurb="Screens pulled, washed and refitted. Tracks vacuumed out before they get wiped, not after."),
    dict(slug="hard-water-stain-removal-edmonton", short="Hard Water Stains", ring=True,
         img="brush-closeup", thumb="squeegee-soapy",
         title="Hard Water Stain Removal in Edmonton",
         blurb="Sprinkler spotting and mineral haze. The ones a normal clean leaves behind."),
    dict(slug="skylight-cleaning-edmonton", short="Skylights", ring=True,
         img="skylight", thumb="ladder-upper",
         title="Skylight &amp; High Window Cleaning in Edmonton",
         blurb="Stairwell glass, vaulted gable windows and skylights, reached from poles and ladders."),
    dict(slug="post-construction-window-cleaning", short="Post-Construction", ring=True,
         img="frame-detail", thumb="cloth-polish",
         title="Post-Construction Window Cleaning in Edmonton",
         blurb="Stucco splatter, labels, tape residue and the fine grit left in every track after a build."),
]
BY_SLUG = dict((s["slug"], s) for s in SERVICES)
RING = [s for s in SERVICES if s["ring"]][:8]

LOCATIONS = [
    dict(slug="window-cleaning-edmonton", area="Edmonton",
         note="From the river valley out to Terwillegar, Windermere, the Hamptons and Clareview.",
         img="two-storey"),
    dict(slug="window-cleaning-st-albert", area="St. Albert",
         note="Braeside, Erin Ridge, Oakmont and the older streets off Sir Winston Churchill.",
         img="modern-home"),
    dict(slug="window-cleaning-sherwood-park", area="Sherwood Park",
         note="Summerwood, Aspen Trails, Nottingham and the Baseline businesses.",
         img="bay-window"),
    dict(slug="window-cleaning-spruce-grove", area="Spruce Grove",
         note="Spruce Village, Deer Park, Greenbury and out toward Stony Plain.",
         img="pole-on-home"),
    dict(slug="window-cleaning-leduc", area="Leduc",
         note="Southfork, Bridgeport, Robinson and the airport corridor businesses.",
         img="sunlit-living-room"),
    dict(slug="window-cleaning-beaumont", area="Beaumont",
         note="Four Seasons, Ruisseau, Montrose and the shops along 50th.",
         img="ladder-upper"),
]

# ----------------------------------------------------------------------
# Inline SVG icons
# ----------------------------------------------------------------------
SVG = dict(
    menu='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>',
    sms='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-9 8.5 8.5 8.5 0 0 1-7.6-3.5L3 21l4.5-1.4A8.38 8.38 0 0 0 21 11.5z"/></svg>',
    phone='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.37 1.9.72 2.8a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.35 1.84.59 2.8.72A2 2 0 0 1 22 16.92z"/></svg>',
    pin='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    clock='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
    truck='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="6" width="13" height="10" rx="1"/><path d="M14 9h4l3 3v4h-7z"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg>',
    squeegee='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="12" rx="1"/><path d="M3 10h18M12 4v12"/><path d="M7 21l5-5"/></svg>',
    tag='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 12l-8 8-9-9V3h8z"/><circle cx="7.5" cy="7.5" r="1.5"/></svg>',
    chat='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-9 8.5 8.5 8.5 0 0 1-7.6-3.5L3 21l4.5-1.4A8.38 8.38 0 0 0 21 11.5z"/></svg>',
    check='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>',
    drop='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2.7S5.5 10 5.5 14.2a6.5 6.5 0 0 0 13 0C18.5 10 12 2.7 12 2.7z"/></svg>',
    ladder='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 2v20M17 2v20M7 7h10M7 12h10M7 17h10"/></svg>',
    window='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 3v18M3 12h18"/></svg>',
    star='<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.9L12 17.8 5.8 21.1 7 14.2 2 9.3l6.9-1z"/></svg>',
)


# ----------------------------------------------------------------------
# Partials
# ----------------------------------------------------------------------
def head(title, desc, canonical, depth=0, extra_ld="", og_type="website", og_image=None):
    up = "../" * depth
    img = og_image or "images/logo-og.jpg"
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="theme-color" content="#14507E" />
  <meta name="format-detection" content="telephone=yes" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-title" content="{NAMEP}" />
  <meta name="geo.region" content="CA-AB" />
  <meta name="geo.placename" content="Edmonton, Alberta" />
  <meta name="geo.position" content="{LAT};{LON}" />
  <meta name="ICBM" content="{LAT}, {LON}" />
  <title>{TITLE}</title>
  <meta name="description" content="{DESC}" />
  <link rel="canonical" href="{CANON}" />
  <link rel="icon" href="{UP}images/favicon.svg" type="image/svg+xml" />

  <meta property="og:type" content="{OGTYPE}" />
  <meta property="og:site_name" content="{NAMEP}" />
  <meta property="og:title" content="{TITLE}" />
  <meta property="og:description" content="{DESC}" />
  <meta property="og:url" content="{CANON}" />
  <meta property="og:image" content="{BASE}/{IMG}" />
  <meta property="og:locale" content="en_CA" />
  <meta name="twitter:card" content="summary_large_image" />

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{UP}css/theme.css?v=2">
{LD}</head>
<body>
""".format(NAMEP=strip(NAME_FULL), TITLE=title, DESC=desc, CANON=canonical, UP=up,
           BASE=BASE, LAT=LAT, LON=LON, OGTYPE=og_type, LD=extra_ld, IMG=img)


def ld_business():
    """No address, no hours and no rating, because the profile has none."""
    return """  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "additionalType": "https://schema.org/professionalService",
    "name": "{NAME}",
    "description": "Window cleaning for homes, storefronts and offices in Edmonton and the surrounding towns.",
    "image": "{BASE}/images/logo-og.jpg",
    "logo": "{BASE}/images/logo.svg",
    "url": "{BASE}/",
    "telephone": "+1 {PHONE}",
    "priceRange": "$$",
    "address": {{"@type":"PostalAddress","addressLocality":"{CITY}","addressRegion":"{REGION}","addressCountry":"CA"}},
    "geo": {{"@type":"GeoCoordinates","latitude":{LAT},"longitude":{LON}}},
    "areaServed": [
      {{"@type":"City","name":"Edmonton"}},{{"@type":"City","name":"St. Albert"}},
      {{"@type":"City","name":"Sherwood Park"}},{{"@type":"City","name":"Spruce Grove"}},
      {{"@type":"City","name":"Leduc"}},{{"@type":"City","name":"Beaumont"}}
    ],
    "knowsAbout": ["window cleaning","screen cleaning","hard water stain removal"],
    "hasMap":"{MAPS}",
    "sameAs":["{MAPS}"]
  }}
  </script>
""".format(NAME=strip(NAME_FULL), BASE=BASE, PHONE=PHONE, LAT=LAT, LON=LON,
           MAPS=MAPS, CITY=CITY, REGION=REGION)


def ld_service(svc):
    return """  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Service","name":"{T}","serviceType":"{S}",
   "provider":{{"@type":"HomeAndConstructionBusiness","name":"{N}","telephone":"+1 {P}","url":"{B}/"}},
   "areaServed":{{"@type":"City","name":"Edmonton"}},
   "url":"{B}/{SL}.html"}}
  </script>
""".format(T=strip(svc["title"]), S=strip(svc["short"]), N=strip(NAME_FULL),
           P=PHONE, B=BASE, SL=svc["slug"])


def ld_faq(pairs):
    items = ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
        % (strip(q), strip(a)) for q, a in pairs)
    return ('  <script type="application/ld+json">\n'
            '  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}\n'
            '  </script>\n' % items)


def ld_breadcrumb(trail):
    items = ['{"@type":"ListItem","position":1,"name":"Home","item":"%s/"}' % BASE]
    for i, (label, href) in enumerate(trail, start=2):
        items.append('{"@type":"ListItem","position":%d,"name":"%s","item":"%s/%s"}'
                     % (i, strip(label), BASE, href))
    return ('  <script type="application/ld+json">\n'
            '  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[%s]}\n'
            '  </script>\n' % ",".join(items))


def strip(text):
    """Plain text for JSON-LD and alt attributes."""
    return (text.replace("&amp;", "and").replace("&middot;", "-")
                .replace("&rsaquo;", ">").replace('"', "'"))


def topbar(depth=0):
    up = "../" * depth
    return """    <header class="osw-bar">
      <div class="osw-bar-left">
        <a class="glass-chip" href="{UP}services.html">{MENU} Services</a>
        <a class="glass-chip" href="{UP}pricing.html">Pricing</a>
        <a class="glass-chip" href="{UP}contact.html">Contact</a>
      </div>

      <div class="osw-logo">{NAME}<small>{TAGLINE}</small></div>

      <div class="osw-bar-right">
        <a class="glass-chip" href="{SMS}">{SMSICON} Text a photo</a>
        <a class="glass-icon-btn" href="tel:{TEL}" aria-label="Call {NAMEP}">{PHONEICON}</a>
        <span class="osw-avatar"><img src="{UP}images/logo.svg" alt="{NAMEP} logo" width="64" height="64"></span>
      </div>
    </header>
""".format(UP=up, MENU=SVG["menu"], NAME=NAME, NAMEP=strip(NAME_FULL), TAGLINE=TAGLINE,
           SMS=SMS_GENERAL, SMSICON=SVG["sms"], TEL=PHONE_TEL, PHONEICON=SVG["phone"])


def crumbs(trail, depth=0):
    up = "../" * depth
    parts = ['<a href="%sindex.html">Home</a>' % up]
    for label, href in trail[:-1]:
        parts.append('<a href="%s%s">%s</a>' % (up, href, label))
    parts.append("<span>%s</span>" % trail[-1][0])
    return '    <nav class="crumbs" aria-label="Breadcrumb">%s</nav>\n' % " &rsaquo; ".join(parts)


def btns(depth=0, quote_label="Text us a photo"):
    up = "../" * depth
    return ('<a class="btn btn-text" href="%s">%s %s</a>'
            '<a class="btn btn-gold" href="tel:%s">Call %s</a>'
            '<a class="btn btn-glass" href="%scontact.html">Get a quote</a>'
            % (SMS_QUOTE, SVG["sms"], quote_label, PHONE_TEL, PHONE, up))


def hero_media(depth=0, media=None, alt=""):
    """The floating panel in a hero, at the photograph's own size."""
    rec = pick(media)
    return "          " + img_tag(rec, depth, lazy=False)


def hero_small(depth, trail, h1, glow, sub, media, alt="", buttons=None):
    return """  <section class="osw osw-small">
    <div class="osw-arch"><span></span><span></span><span></span><span></span><span></span></div>
{TOPBAR}{CRUMBS}
    <div class="osw-stage">
      <div class="osw-scene">
        <div class="osw-product-aura"></div>
        <div class="osw-product-aura cool"></div>
        <div class="osw-product">
{MEDIA}
        </div>
      </div>
    </div>

    <div class="osw-title">
      <h1>{H1} <span class="glow">{GLOW}</span></h1>
      <p class="sub">{SUB}</p>
      <div class="btn-row" style="margin-top:1.4rem;">{BTNS}</div>
    </div>
  </section>
""".format(TOPBAR=topbar(depth), CRUMBS=crumbs(trail, depth),
           MEDIA=hero_media(depth, media, alt), H1=h1, GLOW=glow, SUB=sub,
           BTNS=buttons if buttons is not None else btns(depth))


def photo_strip(depth, want, wide=False):
    """A row of pictures, each captioned with what it actually shows."""
    cls = "photo-card wide" if wide else "photo-card"
    cards = []
    for key in want:
        rec = pick(key)
        cards.append('<figure class="%s">%s<span>%s</span></figure>'
                     % (cls, img_tag(rec, depth), rec["cap"]))
    return '<div class="photo-strip">%s</div>' % "".join(cards)


def service_tiles(depth, services):
    up = "../" * depth
    out = []
    for s in services:
        rec = pick(s["img"], s["thumb"])
        out.append("""        <article class="service-tile">
          <div class="service-tile-media">{IMG}</div>
          <div class="service-tile-body">
            <h3>{SHORT}</h3>
            <p>{BLURB}</p>
            <div class="row"><a href="{UP}{SLUG}.html">What's involved &rarr;</a><a class="btn btn-gold" style="padding:.5rem .9rem; font-size:.8rem;" href="{SMS}">Price it</a></div>
          </div>
        </article>""".format(UP=up, IMG=img_tag(rec, depth), SHORT=s["short"],
                             BLURB=s["blurb"], SLUG=s["slug"],
                             SMS=sms("Hi R&F, quote for " + strip(s["short"]).lower()
                                     + ". Address: ")))
    return "\n".join(out)


def sms_mock(depth=0, lines=None):
    """A text thread, which is how most of these jobs actually get booked."""
    up = "../" * depth
    lines = lines or [
        ("out", "m1", "Two storey in Terwillegar, 22 windows. In and out?", "8:41"),
        ("in", "m2", "Yep. Can do Thursday morning. I'll confirm tonight.", "8:46"),
        ("out", "m3", "Perfect. Side gate code is 4120.", "8:47"),
    ]
    bubbles = []
    for i, (side, cls, text, time) in enumerate(lines):
        if i == 1:
            bubbles.append('<div class="sms-typing"><span></span><span></span><span></span></div>')
        bubbles.append('<div class="sms-bub %s %s">%s<span class="t">%s</span></div>'
                       % (side, cls, text, time))
    return """<div class="sms-mock" aria-label="Example text message booking">
                <div class="sms-mock-head">
                  <span class="sms-mock-av"><img src="{UP}images/logo.svg" alt="" width="64" height="64"></span>
                  <span class="sms-mock-name">{NAME}<small>{PHONE}</small></span>
                  <span class="sms-ico">{PHONEICON}</span>
                </div>
                <div class="sms-mock-body">{BUBBLES}</div>
                <div class="sms-mock-foot">
                  <span class="field">Text message</span>
                  <span class="send"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M2 21l21-9L2 3v7l15 2-15 2v7z"/></svg></span>
                </div>
              </div>""".format(UP=up, NAME=NAME, PHONE=PHONE, PHONEICON=SVG["phone"],
                               BUBBLES="".join(bubbles))


def cta_strip(depth=0, heading="Send a photo, get a number back",
              sub="Stand across the street, photograph the front of the building, and text it over. That is usually enough to price the job."):
    up = "../" * depth
    return """  <section class="section">
    <div class="container">
      <div class="cta-strip">
        <h2>{HEAD}</h2>
        <p>{SUB}</p>

        <div class="cta-demos">
          <div class="demo-wrap">
            <div class="demo">
              {SMSMOCK}
            </div>
            <div class="demo-cap">Text {PHONE}</div>
          </div>

          <div class="demo-wrap">
            <div class="demo bk" aria-label="Example of picking a day">
              <div class="bk-head"><span class="bk-dot"></span> Pick a day <span class="bk-when">This week</span></div>
              <div class="bk-dates">
                <span class="d">M</span><span class="d">T</span><span class="d">W</span><span class="d">T</span><span class="d">F</span>
                <span class="bk-pick"></span>
              </div>
              <div class="bk-slots">
                <span class="slot">8:00</span><span class="slot s2">11:30</span><span class="slot">2:00</span>
              </div>
              <div class="bk-confirm"><span class="chk">&#10003;</span> Booked in</div>
            </div>
            <div class="demo-cap">Most jobs run half a day</div>
          </div>

          <div class="demo-wrap">
            <div class="demo call" aria-label="Calling R and F Enterprise">
              <div class="call-avwrap">
                <span class="ring"></span><span class="ring"></span><span class="ring"></span>
                <div class="call-av"><img src="{UP}images/logo.svg" alt="" width="64" height="64"></div>
              </div>
              <div class="call-name">{NAME}</div>
              <div class="call-status">calling<i></i><i></i><i></i></div>
              <div class="call-actions">
                <span class="cbtn decline"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.02-.24 11.36 11.36 0 0 0 3.57.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.36 11.36 0 0 0 .57 3.57 1 1 0 0 1-.24 1.02l-2.2 2.2z"/></svg></span>
                <span class="cbtn accept"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.02-.24 11.36 11.36 0 0 0 3.57.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.36 11.36 0 0 0 .57 3.57 1 1 0 0 1-.24 1.02l-2.2 2.2z"/></svg></span>
              </div>
            </div>
            <div class="demo-cap">Or just call</div>
          </div>
        </div>

        <div class="btn-row">
          <a class="btn btn-text" href="{SMS}">Text a photo</a>
          <a class="btn btn-gold" href="tel:{TEL}">Call {PHONE}</a>
          <a class="btn btn-glass" href="{UP}contact.html">Quote form</a>
        </div>
      </div>
    </div>
  </section>
""".format(UP=up, HEAD=heading, SUB=sub, SMSMOCK=sms_mock(depth), NAME=NAME,
           PHONE=PHONE, SMS=SMS_QUOTE, TEL=PHONE_TEL)


def footer(depth=0):
    up = "../" * depth
    svc = "".join('<li><a href="%s%s.html">%s</a></li>' % (up, s["slug"], s["short"])
                  for s in SERVICES)
    loc = "".join('<li><a href="%s%s.html">%s</a></li>' % (up, l["slug"], l["area"])
                  for l in LOCATIONS)
    return """  <footer class="foot">
    <div class="foot-grid">
      <div class="foot-brand">
        <div class="osw-logo" style="text-align:left;">{NAME}<small>{TAGLINE}</small></div>
        <p style="margin-top:1rem;">Window cleaning for houses, storefronts and offices across {AREA}. One crew, pole and ladder work, inside and out.</p>
        <div class="foot-contact" style="margin-top:1rem;">
          <div>{PIN} {AREA}</div>
          <div>{PHONEICON} <a href="tel:{TEL}">{PHONE}</a></div>
          <div>{CLOCK} {HOURS}</div>
        </div>
      </div>
      <div><h4>Services</h4><ul>{SVC}</ul></div>
      <div><h4>Where we go</h4><ul>{LOC}<li><a href="{MAPS}" target="_blank" rel="noopener">Google profile</a></li></ul></div>
      <div><h4>Company</h4><ul><li><a href="{UP}about.html">About</a></li><li><a href="{UP}pricing.html">Pricing</a></li><li><a href="{UP}reviews.html">Reviews</a></li><li><a href="{UP}blog/index.html">Notes</a></li><li><a href="{UP}contact.html">Contact</a></li></ul></div>
    </div>
    <div class="foot-note">Photographs on this site are illustrative, not photographs of our own jobs.</div>
    <div class="foot-bottom">&copy; <span id="yr">2026</span> {NAMEP} &middot; {AREA} &middot; <a href="tel:{TEL}">{PHONE}</a> &middot; <a href="{UP}privacy.html">Privacy</a> &middot; <a href="{UP}terms.html">Terms</a></div>
  </footer>

  <a class="float-text" href="{SMS}" aria-label="Text us a photo">{SMSICON}</a>
  <div class="mobile-cta">
    <a class="btn btn-text" href="{SMS}">Text</a>
    <a class="btn btn-primary" href="tel:{TEL}">Call</a>
    <a class="btn btn-gold" href="{UP}contact.html">Quote</a>
  </div>

  <script src="{UP}js/main.js?v=2"></script>
  <script>document.getElementById('yr').textContent = new Date().getFullYear();</script>
</body>
</html>
""".format(NAME=NAME, NAMEP=strip(NAME_FULL), TAGLINE=TAGLINE, AREA=AREA,
           PIN=SVG["pin"], PHONEICON=SVG["phone"], TEL=PHONE_TEL, PHONE=PHONE,
           CLOCK=SVG["clock"], HOURS=HOURS_SHORT, SVC=svc, LOC=loc, UP=up,
           MAPS=MAPS, SMS=SMS_GENERAL, SMSICON=SVG["sms"])


def sidebar(depth=0, photo=None, photo_cap="", extra=""):
    up = "../" * depth
    svc = "".join('<li><a href="%s%s.html">%s</a></li>' % (up, s["slug"], s["short"]) for s in SERVICES)
    pic = ""
    if photo:
        rec = pick(photo)
        pic = """        <div class="glass-card">
          {IMG}
          <h3>{CAP}</h3>
          <p>Every visit ends the same way: a walk round the outside looking at the glass from an angle, because that is where streaks show.</p>
        </div>
""".format(IMG=img_tag(rec, depth), CAP=photo_cap or rec["cap"])
    return """      <aside class="sidebar">
        <div class="glass-card">
          <h3>Get a number first</h3>
          <p>Text a photo of the building and roughly how many windows. You will get a price before anyone turns up, and that price is what you pay.</p>
          <div class="btn-row" style="margin-top:1rem;">
            <a class="btn btn-text" href="{SMS}">Text a photo</a>
            <a class="btn btn-glass" href="tel:{TEL}">Call {PHONE}</a>
          </div>
        </div>
{PIC}
        <div class="glass-card">
          <h3>Worth knowing</h3>
          <div class="info-row">{CLOCK}<div><strong>Booking</strong><br>Call or text. Exteriors run spring through to freeze-up.</div></div>
          <div class="info-row">{PIN}<div><strong>Where we go</strong><br>{AREA}, plus the towns along the Henday.</div></div>
          <div class="info-row">{DROP}<div><strong>Hard water</strong><br>Sprinkler spotting needs its own treatment. Say so when you book.</div></div>
          <div class="info-row">{LADDER}<div><strong>Access</strong><br>Poles and ladders. We do not do rope or swing stage work.</div></div>
        </div>

        <div class="glass-card">
          <h3>Everything we do</h3>
          <ul>{SVC}</ul>
        </div>
{EXTRA}      </aside>
""".format(SMS=SMS_QUOTE, TEL=PHONE_TEL, PHONE=PHONE, CLOCK=SVG["clock"], PIN=SVG["pin"],
           AREA=AREA, DROP=SVG["drop"], LADDER=SVG["ladder"], SVC=svc, EXTRA=extra, PIC=pic)


def faq_block(pairs):
    items = []
    for q, a in pairs:
        items.append('<div class="faq-item"><button class="faq-q">%s<span class="arrow">+</span></button>'
                     '<div class="faq-a"><p>%s</p></div></div>' % (q, a))
    return '<div class="faq-list">%s</div>' % "".join(items)


def write(relpath, html):
    path = os.path.join(ROOT, relpath.replace("/", os.sep))
    folder = os.path.dirname(path)
    if folder and not os.path.isdir(folder):
        os.makedirs(folder)
    io.open(path, "w", encoding="utf-8", newline="\n").write(html)
    return relpath
