# -*- coding: utf-8 -*-
"""Builds the core pages: home, services, pricing, about, contact, reviews, legal."""

from common import *  # noqa: F401,F403
from common import (NAME, NAME_FULL, TAGLINE, PHONE, PHONE_TEL, AREA, BASE, MAPS, SVG,
                    SERVICES, RING, LOCATIONS, SMS_QUOTE, SMS_GENERAL, sms, head,
                    ld_business, ld_faq, ld_breadcrumb, topbar, crumbs, btns, hero_small,
                    photo_strip, service_tiles, sms_mock, cta_strip, footer, sidebar,
                    faq_block, write, strip, HOURS_SHORT, new_page, pick, img_tag)

BUILT = []


def page(path, html):
    BUILT.append(write(path, html))


# ======================================================================
# HOME
# ======================================================================
HOME_FAQ = [
    ("How do you price a job?",
     "By the window, counted off a photo. Text us a picture of the front and back of the house and say whether you want inside done as well. You get a number back, usually the same evening."),
    ("Do you do inside and outside?",
     "Both. Most people book exteriors on their own in summer and add the insides in the autumn, before the windows get shut for six months."),
    ("How late in the year can you do exteriors?",
     "Until it stops holding above freezing, which in Edmonton is usually some time in late October. Water on glass in a hard frost freezes before it can be squeegeed off, and the cold makes rubber skip. Interiors carry on all winter."),
    ("What about the white spots the sprinklers leave?",
     "Those are mineral, not dirt, and a normal wash will not shift them. They need an acidic treatment and a bit of patience. Mention them when you book so the right kit is on the van."),
    ("Do you clean the screens and tracks too?",
     "Screens come out and get washed if you want them done. Tracks get vacuumed before anything wet goes near them, otherwise you just make grey paste in the corners."),
    ("How high will you go?",
     "Three storeys from a ladder or a water fed pole. Anything needing rope access or a swing stage is a different trade and we will say so rather than improvise."),
]

new_page()

ring_cards = []
for i, svc in enumerate(RING, start=1):
    ring_cards.append(
        '<div class="svc-item p%d"><a class="svc-card" href="%s.html">%s'
        '<span class="svc-card-label">%s</span></a></div>'
        % (i, svc["slug"], img_tag(pick(svc["img"]), 0), svc["short"]))

home = head(
    title="Window Cleaning in Edmonton | " + NAME_FULL,
    desc=("R&F Enterprise cleans windows in Edmonton and the surrounding towns. Houses, storefronts "
          "and offices, inside and out, screens and tracks, hard water spotting. Text a photo for a price."),
    canonical=BASE + "/",
    extra_ld=ld_business() + ld_faq(HOME_FAQ),
) + """
  <section class="osw">
    <div class="osw-arch"><span></span><span></span><span></span><span></span><span></span></div>

{TOPBAR}
    <div class="osw-stage osw-stage-home">

      <div class="osw-scene osw-scene-left">
        <div class="osw-product-aura"></div>
        <div class="osw-product-aura cool"></div>
        <div class="osw-panel">
          <span class="osw-panel-eyebrow">Edmonton &amp; area</span>
          <h2>Windows you<br>can see out of.</h2>
          <p>Houses, storefronts and offices. Glass, frames, sills and tracks, inside and out, done with poles and ladders by people who do this all day.</p>
          <ul class="osw-panel-list">
            <li>Priced off a photo, before anyone turns up</li>
            <li>Screens and tracks done properly, not rinsed</li>
            <li>Hard water spotting treated separately</li>
          </ul>
          <div class="osw-panel-foot">
            <span><strong>{PHONE}</strong></span>
            <span>{HOURS}</span>
          </div>
        </div>
      </div>

      <div class="osw-scene">
        <div class="svc-ring" aria-label="What R and F Enterprise cleans">
          <div class="svc-ring-rotor">
            {RING}
          </div>
          <div class="svc-ring-center">
            <span class="crown">{WINDOW}</span>
            <strong>R&amp;F</strong>
            <small>Enterprise</small>
          </div>
        </div>
      </div>
    </div>

    <div class="osw-title">
      <h1>Edmonton <span class="glow">WINDOW CLEANING</span></h1>
      <p class="sub">Send a photo of the building and we will send back a price. Exteriors from thaw to freeze-up, interiors all year.</p>
      <div class="btn-row" style="margin-top: 1.5rem;">
        <a class="btn btn-text" href="{SMS}">{SMSICON} Text a photo</a>
        <a class="btn btn-primary" href="tel:{TEL}">Call {PHONE}</a>
        <a class="btn btn-glass" href="contact.html">Get a quote</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Why bother with a window cleaner</span>
        <h2>Most of the job is the part nobody photographs</h2>
        <p>Anyone can wipe the middle of a pane. What you notice a week later is the edge that was never dried, the track still full of grit, and the frame nobody touched.</p>
      </div>
      <div class="why-grid">
        <div class="why-card">
          <div class="why-media">
            {WHY1}
          </div>
          <div class="why-body">
            <span class="icon sun">{SQUEEGEE}</span>
            <h3>Edges and corners</h3>
            <p>The blade gets detailed into every corner and the perimeter is dried by hand. That is where streaks live.</p>
          </div>
        </div>

        <div class="why-card">
          <div class="why-media">
            {WHY2}
          </div>
          <div class="why-body">
            <span class="icon steel">{LADDER}</span>
            <h3>Up to three storeys</h3>
            <p>Ladder work and water fed poles. Gables, stairwell glass and skylights included, as long as we can reach them safely.</p>
          </div>
        </div>

        <div class="why-card">
          <div class="why-media">
            {WHY3}
          </div>
          <div class="why-body">
            <span class="icon gold">{DROP}</span>
            <h3>Hard water, separately</h3>
            <p>Sprinkler spotting is mineral. It gets its own treatment and its own line on the quote, because it takes its own time.</p>
          </div>
        </div>

        <div class="why-card">
          <div class="why-media">
            {SMSMOCK}
          </div>
          <div class="why-body">
            <span class="icon slate">{CHAT}</span>
            <h3>Booked by text</h3>
            <p>Photo in, price out. Most of our work gets arranged in four or five messages and nobody has to be home.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="grid grid-2">
        <a class="bx-tile" href="{SMS}">
          <div class="bx-media">
            {BX1}
          </div>
          <h3>GET A PRICE <span class="arrow">&#8599;</span></h3>
          <p>One photo of the front, one of the back. That is usually all it takes.</p>
        </a>
        <a class="bx-tile" href="services.html">
          <div class="bx-media">
            {BX2}
          </div>
          <h3>WHAT WE DO <span class="arrow">&#8599;</span></h3>
          <p>Houses, storefronts, offices, screens, tracks, skylights and post-build cleanups.</p>
        </a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Services</span>
        <h2>Glass, and the bits around it</h2>
        <p>Everything here is window work. We do not do eavestroughs, siding or pressure washing, and we would rather point you at someone who does than take the job.</p>
      </div>
      <div class="grid grid-4">
{TILES}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">How a visit runs</span>
        <h2>Four passes, in this order</h2>
        <p>It is the same on a bungalow and on a strip mall. Skip a step and you can see it from the sidewalk.</p>
      </div>
      <div class="grid grid-4">
        <div class="step-card"><span class="step-n">1</span><h3>Tracks first</h3><p>Vacuumed out dry. Wet them before this and the grit turns to paste that works its way back onto the glass.</p></div>
        <div class="step-card"><span class="step-n">2</span><h3>Scrub</h3><p>Soap and a soft brush or a strip washer, worked long enough to lift the film rather than smear it.</p></div>
        <div class="step-card"><span class="step-n">3</span><h3>Squeegee</h3><p>Blade detailed into the corners, then pulled in overlapping passes. Rubber gets changed when it skips, not when it fails.</p></div>
        <div class="step-card"><span class="step-n">4</span><h3>Dry the edges</h3><p>Perimeter, sill and frame done by hand, then checked from an angle in the light.</p></div>
      </div>
      {STRIP}
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Straight answers</span>
        <h2>The things people ask</h2>
      </div>
      <div class="faq-wide">
        {FAQ}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(
    TOPBAR=topbar(0), RING="\n            ".join(ring_cards), SMS=SMS_QUOTE,
    SMSICON=SVG["sms"], TEL=PHONE_TEL, PHONE=PHONE, HOURS=HOURS_SHORT,
    SQUEEGEE=SVG["squeegee"], LADDER=SVG["ladder"], DROP=SVG["drop"],
    CHAT=SVG["chat"], WINDOW=SVG["window"], SMSMOCK=sms_mock(0),
    WHY1=img_tag(pick("sill-wipe"), 0),
    WHY2=img_tag(pick("pole-on-home"), 0),
    WHY3=img_tag(pick("water-fed"), 0),
    BX1=img_tag(pick("sunlit-living-room"), 0, cls="bg"),
    BX2=img_tag(pick("modern-home"), 0, cls="bg"),
    TILES=service_tiles(0, SERVICES),
    STRIP=photo_strip(0, ["bay-window", "office-view", "supplies", "before-after"]),
    FAQ=faq_block(HOME_FAQ), CTA=cta_strip(0), FOOT=footer(0))

page("index.html", home)


# ======================================================================
# SERVICES
# ======================================================================
new_page()

services_page = head(
    title="Window Cleaning Services in Edmonton | " + NAME_FULL,
    desc=("Everything R&F Enterprise cleans: residential and commercial windows, storefronts, "
          "interior glass, screens and tracks, hard water spotting, skylights and post-construction glass."),
    canonical=BASE + "/services.html",
    extra_ld=ld_breadcrumb([("Services", "services.html")]),
) + hero_small(
    0, [("Services", "services.html")],
    "All of it is", "GLASS",
    "Eight things, and they all involve windows. Most jobs are two or three of them at once, which is cheaper than booking them apart.",
    media="modern-home",
) + """
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Houses</span>
        <h2>Residential</h2>
      </div>
      <div class="grid grid-3">
{HOUSES}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Businesses</span>
        <h2>Commercial and retail</h2>
      </div>
      <div class="grid grid-2">
{BIZ}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Specialist</span>
        <h2>The awkward ones</h2>
        <p>Jobs that need different kit, more time, or both. Worth saying up front when you ask for a price.</p>
      </div>
      <div class="grid grid-3">
{SPEC}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Bundles</span>
        <h2>What usually gets booked together</h2>
      </div>
      <div class="grid grid-3">
        <div class="glass-card">
          {BUN1}
          <h3>Spring exterior</h3>
          <p>Outsides, screens off and washed, tracks cleared of a winter of grit. The first one after thaw is always the biggest.</p>
          <p><a href="residential-window-cleaning-edmonton.html">Residential windows &rarr;</a></p>
        </div>
        <div class="glass-card">
          {BUN2}
          <h3>Before the windows shut</h3>
          <p>Insides and outsides in one visit, late September or so, while it is still warm enough to do both.</p>
          <p><a href="interior-window-cleaning-edmonton.html">Interior glass &rarr;</a></p>
        </div>
        <div class="glass-card">
          {BUN3}
          <h3>Handover clean</h3>
          <p>New build or renovation. Stucco splatter, labels and tape residue, then the tracks, which are always full.</p>
          <p><a href="post-construction-window-cleaning.html">Post-construction &rarr;</a></p>
        </div>
      </div>
      {STRIP}
    </div>
  </section>

{CTA}{FOOT}""".format(
    HOUSES=service_tiles(0, [s for s in SERVICES if s["slug"] in (
        "residential-window-cleaning-edmonton", "interior-window-cleaning-edmonton",
        "window-screens-tracks-edmonton")]),
    BIZ=service_tiles(0, [s for s in SERVICES if s["slug"] in (
        "commercial-window-cleaning-edmonton", "storefront-window-cleaning-edmonton")]),
    SPEC=service_tiles(0, [s for s in SERVICES if s["slug"] in (
        "hard-water-stain-removal-edmonton", "skylight-cleaning-edmonton",
        "post-construction-window-cleaning")]),
    BUN1=img_tag(pick("pole-on-home"), 0),
    BUN2=img_tag(pick("interior-microfiber"), 0),
    BUN3=img_tag(pick("sill-wipe"), 0),
    STRIP=photo_strip(0, ["bay-window", "office-view", "supplies", "water-fed"]),
    CTA=cta_strip(0), FOOT=footer(0))

page("services.html", services_page)


# ======================================================================
# PRICING
# ======================================================================
new_page()

PRICING_FAQ = [
    ("Why is there no price list?",
     "Because a window is not a unit. A sealed picture window on a bungalow takes a minute. The same size pane three storeys up behind a shrub takes fifteen. Counting them off a photo is the only way to get the number right first time."),
    ("What makes a job cost more?",
     "Height, access and how long it has been. A house that gets done every year is quick work. One that has not been touched since it was built needs the film scrubbed off before a squeegee will do anything useful."),
    ("Is the quote fixed?",
     "Yes, for the work described. If we get there and there is a storm window arrangement nobody mentioned, or the back is twice the glass of the front, we stop and tell you before carrying on."),
    ("Do you charge more for second storey?",
     "A little, because it is ladder time rather than pole time. It is in the number before you agree to anything."),
    ("Is it cheaper to book regularly?",
     "Per visit, yes. Glass that was done in spring takes noticeably less work in autumn. Storefronts on a weekly or biweekly round are the cheapest per clean of anything we do."),
    ("How do I pay?",
     "Sorted when you book. Ask and we will tell you what we take."),
]

pricing = head(
    title="Window Cleaning Prices in Edmonton | " + NAME_FULL,
    desc=("How R&F Enterprise prices window cleaning in Edmonton: counted off a photo, agreed before "
          "the visit, fixed for the work described."),
    canonical=BASE + "/pricing.html",
    extra_ld=ld_breadcrumb([("Pricing", "pricing.html")]) + ld_faq(PRICING_FAQ),
) + hero_small(
    0, [("Pricing", "pricing.html")],
    "Counted off", "A PHOTO",
    "We price by the window, not by the hour. You get the number before the visit, and it does not move unless the job turns out to be a different job.",
    media="squeegee-soapy",
) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <h2>How it works</h2>
          <p>Stand far enough back to get the whole wall in and take a picture. Do the same at the back. Send both, say whether you want insides done, and mention anything odd. That is the whole process.</p>

          <div class="grid grid-3" style="margin:1.5rem 0;">
            <div class="glass-card">
              {STEP1}
              <h3>Photograph it</h3>
              <p>Front and back, far enough away to see every window. Daylight helps.</p>
            </div>
            <div class="glass-card">
              {STEP2}
              <h3>Get the number</h3>
              <p>A price with the window count it was based on, so you can check we did not miss a side.</p>
            </div>
            <div class="glass-card">
              {STEP3}
              <h3>Pick a day</h3>
              <p>Most houses are half a day. You do not need to be in for exteriors.</p>
            </div>
          </div>

          <h2>What moves the number</h2>
          <p>Six things, roughly in the order they matter.</p>
          <ul>
            <li><strong>How many panes.</strong> Not square footage. A wall of french panes is a dozen little windows and prices like it.</li>
            <li><strong>Height.</strong> Ground floor is pole work. Second and third storey is ladder work, which means setting up, moving, and setting up again.</li>
            <li><strong>Access.</strong> Shrubs under the sills, a locked side gate, a deck rail in the way. All of it is time.</li>
            <li><strong>How long since the last one.</strong> Years of film has to be scrubbed off before the squeegee does anything. First cleans cost more than the ones after.</li>
            <li><strong>Hard water.</strong> Priced on its own, because it is a treatment rather than a wash and it does not always come all the way off.</li>
            <li><strong>Inside as well.</strong> Roughly doubles the window count, though insides go faster than outsides.</li>
          </ul>

          <figure class="media-figure">
            {PFIG}
            <figcaption>Storefronts on a standing round are the cheapest per visit of anything we do, because the glass never gets far from clean.</figcaption>
          </figure>

          <h2>Repeat work costs less</h2>
          <p>Nothing complicated behind this. Glass done last spring has a season of dust on it. Glass nobody has touched in six years has a bonded film that needs scrubbing before anything else happens, and that is where the hours go.</p>
          <p>Storefronts usually land on weekly or biweekly. Houses tend to be twice a year, outsides in spring and the full lot in autumn. Offices are mostly quarterly.</p>

          <h2>Pricing questions</h2>
          {FAQ}
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(FAQ=faq_block(PRICING_FAQ),
                      STEP1=img_tag(pick("two-storey"), 0),
                      STEP2=img_tag(pick("modern-home"), 0),
                      STEP3=img_tag(pick("bay-window"), 0),
                      PFIG=img_tag(pick("retail-front"), 0),
                      SIDEBAR=sidebar(0, photo="cloth-polish",
                                      photo_cap="Checked from an angle"),
                      CTA=cta_strip(0), FOOT=footer(0))

page("pricing.html", pricing)


# ======================================================================
# ABOUT
# ======================================================================
new_page()

about = head(
    title="About " + NAME_FULL + " | Edmonton Window Cleaners",
    desc=("R&F Enterprise is a window cleaning business working across Edmonton, St. Albert, "
          "Sherwood Park, Spruce Grove, Leduc and Beaumont."),
    canonical=BASE + "/about.html",
    extra_ld=ld_breadcrumb([("About", "about.html")]),
) + hero_small(
    0, [("About", "about.html")],
    "We only do", "WINDOWS",
    "One trade, done properly, across Edmonton and the towns around it. If a job is not glass, we will tell you who to ring instead.",
    media="residential-squeegee",
) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <h2>Why only windows</h2>
          <p>Plenty of companies will add window cleaning to a list of six other things. It usually gets done last, by whoever is free, with whatever is in the van.</p>
          <p>Glass is unforgiving in a way that most cleaning is not. A floor that is ninety percent clean looks clean. A window that is ninety percent clean looks streaky from across the room, and it looks worse in low winter sun than it did before anyone touched it. So we stick to the one thing and get it right.</p>

          <figure class="media-figure">
            {AFIG}
            <figcaption>Exteriors run from thaw through to the first hard frost. Interiors carry on all winter.</figcaption>
          </figure>

          <h2>Who calls us</h2>
          <ul>
            <li><strong>Homeowners</strong>, usually twice a year, and usually after a spring where the sprinklers have spotted everything.</li>
            <li><strong>Shops and restaurants</strong> on a standing weekly round, because frontage gets judged from the sidewalk.</li>
            <li><strong>Offices and clinics</strong> quarterly, done before opening.</li>
            <li><strong>Builders and renovators</strong> at handover, when the glass is covered in stucco splatter and nobody wants the client to see it.</li>
            <li><strong>Realtors</strong>, in a hurry, the day before photos.</li>
          </ul>

          <h2>What Edmonton does to glass</h2>
          <p>Three things, mostly. Sprinkler overspray leaves mineral spots that no amount of soap will shift. Spring thaw throws a season of road grit and dust at everything facing a street. And because we shut the windows for half the year, interiors collect cooking film and condensation marks that only show up when the sun comes back round in February.</p>
          <p>None of it is unusual. It does mean the honest answer to "how often" is twice a year for most houses, and that the spring clean is always the bigger of the two.</p>

          <h2>Where we go</h2>
          <p>Edmonton proper, plus St. Albert, Sherwood Park, Spruce Grove, Leduc and Beaumont. Further out, ask. If the job is big enough to be worth the drive we will usually come.</p>
          {STRIP}
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(
    AFIG=img_tag(pick("pole-on-home"), 0),
    STRIP=photo_strip(0, ["two-storey", "commercial-building", "storefront", "skylight"]),
    SIDEBAR=sidebar(0, photo="supplies", photo_cap="What goes on the van"),
    CTA=cta_strip(0), FOOT=footer(0))

page("about.html", about)


# ======================================================================
# CONTACT
# ======================================================================
new_page()

contact = head(
    title="Contact &amp; Quotes | " + NAME_FULL,
    desc=("Get a window cleaning price from R&F Enterprise. Text " + PHONE +
          " with a photo of the building, or call."),
    canonical=BASE + "/contact.html",
    extra_ld=ld_breadcrumb([("Contact", "contact.html")]),
) + hero_small(
    0, [("Contact", "contact.html")],
    "Text us", "A PHOTO",
    "It is the fastest way to a real price. One picture of the front, one of the back, and we can count the glass ourselves.",
    media="interior-framed",
) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <h2>Three ways to get hold of us</h2>
          <div class="grid grid-3" style="margin:1.5rem 0;">
            <a class="glass-card" href="{SMS}" style="text-decoration:none;">
              {WAY1}
              <h3>Text</h3>
              <p>Best for quotes. Send photos and we will count the windows off them.</p>
              <p><strong>{PHONE}</strong></p>
            </a>
            <a class="glass-card" href="tel:{TEL}" style="text-decoration:none;">
              {WAY2}
              <h3>Phone</h3>
              <p>Best for scheduling, or if you would rather just describe the place.</p>
              <p><strong>{PHONE}</strong></p>
            </a>
            <a class="glass-card" href="{MAPS}" target="_blank" rel="noopener" style="text-decoration:none;">
              {WAY3}
              <h3>Google</h3>
              <p>Our profile, and where to leave a review once we have been.</p>
              <p><strong>{NAMEP}</strong></p>
            </a>
          </div>

          <h2>What to send</h2>
          <p>More detail means fewer messages back and forth:</p>
          <ul>
            <li>A photo of the front and one of the back, taken far enough away to see every window.</li>
            <li>Whether you want insides done as well, or just the outsides.</li>
            <li>Roughly how long since the last clean. "Never" is a perfectly good answer and changes the price.</li>
            <li>Anything in the way: dogs in the yard, a locked gate, a code, parking that fills up by nine.</li>
            <li>Screens and tracks, yes or no.</li>
            <li>Any deadline. Listing photos and handovers get scheduled around.</li>
          </ul>

          <figure class="media-figure">
            {CFIG}
            <figcaption>Mineral spotting from sprinklers. Worth flagging when you ask for a price, because it is treated separately.</figcaption>
          </figure>

          <h2>Coverage and timing</h2>
          <div class="info-row">{PIN}<div><strong>Where we go</strong><br>{AREA}, plus the towns along the Henday</div></div>
          <div class="info-row">{CLOCK}<div><strong>Booking</strong><br>{HOURS}</div></div>
          <div class="info-row">{DROP}<div><strong>Season</strong><br>Exteriors thaw to freeze-up. Interiors year round.</div></div>

          <div class="btn-row" style="margin-top:1.6rem;">
            <a class="btn btn-text" href="{SMS}">{SMSICON} Text {PHONE}</a>
            <a class="btn btn-gold" href="tel:{TEL}">Call instead</a>
          </div>
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(SMS=SMS_QUOTE, SMSICON=SVG["sms"], PHONE=PHONE, TEL=PHONE_TEL,
                      MAPS=MAPS, CLOCK=SVG["clock"], PIN=SVG["pin"], DROP=SVG["drop"],
                      AREA=AREA, HOURS=HOURS_SHORT, NAMEP=NAME_FULL,
                      WAY1=img_tag(pick("interior-microfiber"), 0),
                      WAY2=img_tag(pick("commercial-pole"), 0),
                      WAY3=img_tag(pick("modern-home"), 0),
                      CFIG=img_tag(pick("brush-closeup"), 0),
                      SIDEBAR=sidebar(0, photo="frame-detail", photo_cap="Frames and sills"),
                      CTA=cta_strip(0), FOOT=footer(0))

page("contact.html", contact)


# ======================================================================
# REVIEWS
# ======================================================================
new_page()

reviews = head(
    title="Reviews | " + NAME_FULL,
    desc=("R&F Enterprise is a new Google listing with no reviews yet. Here is what we hold every "
          "job to in the meantime, and where to leave the first one."),
    canonical=BASE + "/reviews.html",
    extra_ld=ld_breadcrumb([("Reviews", "reviews.html")]),
) + hero_small(
    0, [("Reviews", "reviews.html")],
    "Nothing here", "YET",
    "The Google profile is new and there are no reviews on it. Rather than pad this page out, here is what we will actually be judged on.",
    media="bay-window",
) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <h2>No reviews yet, and we are not going to pretend otherwise</h2>
          <p>Plenty of new businesses fill this page with invented quotes from people who do not exist. Ours is empty because nobody has left one. If we have done your windows, the Google profile is the place to say so, and it matters more to a business this size than it would to a national chain.</p>
          <div class="btn-row" style="margin:1.2rem 0;">
            <a class="btn btn-primary" href="{MAPS}" target="_blank" rel="noopener">Leave the first review</a>
            <a class="btn btn-text" href="{SMSFB}">Tell us privately instead</a>
          </div>

          <h2>What to hold us to</h2>
          <div class="grid grid-2" style="margin:1.4rem 0;">
            <div class="review-tile">
              <div class="rev-head"><span class="rev-av a">{CHECK}</span><span class="rev-name"><strong>The quote is the price</strong><small>Agreed first</small></span></div>
              <p class="quote">If the back of the house has twice the glass the photo showed, we stop and tell you before we start, not after.</p>
            </div>
            <div class="review-tile">
              <div class="rev-head"><span class="rev-av b">{CHECK}</span><span class="rev-name"><strong>Streaks get redone</strong><small>No argument</small></span></div>
              <p class="quote">Glass looks different in different light. Spot something the next morning, send a photo, and we come back.</p>
            </div>
            <div class="review-tile">
              <div class="rev-head"><span class="rev-av c">{CHECK}</span><span class="rev-name"><strong>We say what will not come off</strong><small>Before, not after</small></span></div>
              <p class="quote">Scratches, failed seals and etched glass do not clean. We point them out at the quote rather than charging you to find out.</p>
            </div>
            <div class="review-tile">
              <div class="rev-head"><span class="rev-av d">{CHECK}</span><span class="rev-name"><strong>Ladders go where they belong</strong><small>Not on your gutters</small></span></div>
              <p class="quote">Standoffs on the wall, feet on something level, nothing leaned against eavestrough. Damage from a ladder is on us.</p>
            </div>
          </div>

          <h2>What the work looks like</h2>
          {STRIP}
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(
    MAPS=MAPS, SMSFB=sms("Hi R&F, feedback on the job you did: "),
    CHECK="&#10003;",
    STRIP=photo_strip(0, ["sunlit-living-room", "office-view", "two-storey", "retail-front"]),
    SIDEBAR=sidebar(0, photo="storefront", photo_cap="Standing rounds"),
    CTA=cta_strip(0), FOOT=footer(0))

page("reviews.html", reviews)


# ======================================================================
# LEGAL
# ======================================================================
def legal(slug, title, heading, body):
    new_page()
    return head(
        title=title + " | " + NAME_FULL,
        desc=title + " for " + strip(NAME_FULL) + ", a window cleaning business in Edmonton, Alberta.",
        canonical=BASE + "/" + slug,
        extra_ld=ld_breadcrumb([(heading, slug)]),
    ) + hero_small(
        0, [(heading, slug)], heading.split(" ")[0], " ".join(heading.split(" ")[1:]).upper() or "PAGE",
        "Short version, in plain words. Ask if any of it is unclear.",
        media="office-view",
    ) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
{BODY}
        </div>
{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(BODY=body, SIDEBAR=sidebar(0), CTA=cta_strip(0), FOOT=footer(0))


privacy_body = """          <h2>What we collect</h2>
          <p>Your name, the number or address you contacted us from, where the job is, and any photos you send of the building. That is it.</p>

          <h2>What we do with it</h2>
          <p>Quote the job, book it, do it, and follow up. Photos you send are used to count windows and nothing else.</p>

          <h2>What we do not do</h2>
          <p>We do not sell your details, pass them to marketing companies, or add you to a mailing list because you asked what something costs.</p>

          <h2>Texts and calls</h2>
          <p>If you text us, that conversation also sits with your phone network and ours under their terms. Same goes for anything you post on our Google profile.</p>

          <h2>This website</h2>
          <p>Static pages. No login, no advertising trackers. The only thing loaded from elsewhere is the Google Fonts service for the typefaces.</p>

          <h2>Your choices</h2>
          <p>Ask what we hold about you, or ask us to delete it, and we will. Call or text the number on this site.</p>

          <h2>Contact</h2>
          <p>Privacy questions go to <a href="tel:{TEL}">{PHONE}</a>.</p>""".format(TEL=PHONE_TEL, PHONE=PHONE)

terms_body = """          <h2>Quotes</h2>
          <p>A quote covers the windows described in it, counted from the photos or the description you gave us. Find more glass on the day and we stop, show you, and agree the difference before carrying on.</p>

          <h2>Access</h2>
          <p>You arrange the way in. Gate codes, dogs, alarm codes, parking. If a crew arrives and cannot get to the back of the house, we will try to reach you and otherwise reschedule.</p>

          <h2>What glass will not do</h2>
          <p>Scratches, failed thermal seals, etched or pitted panes and some long-standing mineral damage do not clean off. We point these out when we see them. Cleaning will often improve them and will not always fix them.</p>

          <h2>Screens</h2>
          <p>Old screens go brittle. We handle them carefully, but a frame or mesh already perished can tear when it comes out, and we will show you rather than quietly put it back.</p>

          <h2>Heights</h2>
          <p>We work from ladders and poles up to about three storeys. We do not do rope access or swing stage work, and we will turn down anything that needs it.</p>

          <h2>If something is wrong</h2>
          <p>Tell us within a few days and we will come back. If we damage something, tell us straight away so it gets dealt with properly.</p>

          <h2>Weather</h2>
          <p>Exterior work stops for hard frost, high wind and heavy rain. If we move your day, that is usually why.</p>

          <h2>Cancellations</h2>
          <p>As much notice as you can manage, please. A late cancellation costs a crew their day.</p>

          <h2>Payment</h2>
          <p>Terms are confirmed when you book, with your quote.</p>

          <h2>Contact</h2>
          <p>Questions about these terms go to <a href="tel:{TEL}">{PHONE}</a>.</p>""".format(TEL=PHONE_TEL, PHONE=PHONE)

page("privacy.html", legal("privacy.html", "Privacy Policy", "Privacy Policy", privacy_body))
page("terms.html", legal("terms.html", "Terms of Service", "Terms of Service", terms_body))

if __name__ == "__main__":
    for p in BUILT:
        print("built", p)
