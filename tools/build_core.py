# -*- coding: utf-8 -*-
"""Builds the core pages: home, services, pricing, about, contact, reviews, legal."""

from common import *  # noqa: F401,F403
from common import (NAME, TAGLINE, PHONE, PHONE_TEL, AREA, BASE, MAPS, SVG, SERVICES,
                    RING, LOCATIONS, WA_QUOTE, WA_GENERAL, wa, head, ld_business, ld_faq,
                    ld_breadcrumb, topbar, crumbs, btns, hero_small, photo_strip,
                    service_tiles, wa_mock, cta_strip, footer, sidebar, faq_block,
                    write, strip, HOURS_SHORT, ADDRESS_LINE)

BUILT = []


def page(path, html):
    BUILT.append(write(path, html))


# ======================================================================
# HOME
# ======================================================================
HOME_FAQ = [
    ("Do you bring your own supplies and equipment?",
     "Yes. Vacuums, cloths, mops and products all come with the crew. If you'd rather we used your products, for a scent or a surface you're particular about, just leave them out and say the word."),
    ("How do I get a price?",
     "Send photos of the home on WhatsApp, or call and describe it. You get a quote before anyone shows up, and the price is agreed before we start work."),
    ("Can you come on short notice?",
     "Often yes. We work seven days a week, so same week slots are common. Call early in the day for the best chance of a same-day visit."),
    ("Do I need to be home?",
     "No. Plenty of clients leave a key, a lockbox code or a concierge instruction. We lock up and message you when the job is done."),
    ("What areas do you cover?",
     "Etobicoke first, then Toronto and the west GTA: Mississauga, North York, Brampton and Vaughan."),
    ("Is it the same crew each time?",
     "For recurring cleans we keep the same people on your home wherever we can. They learn the quirks of the place, and you stop having to explain them."),
]

ring_cards = []
for i, s in enumerate(RING, start=1):
    ring_cards.append(
        '<div class="svc-item p%d"><a class="svc-card" href="%s.html">'
        '<img src="%s" alt="%s" loading="lazy">'
        '<span class="svc-card-label">%s</span></a></div>'
        % (i, s["slug"], s["img"], s["alt"], s["short"]))

home = head(
    title="House Cleaning in Etobicoke &amp; Toronto | " + NAME,
    desc=("Fanta Cleaning is a house cleaning service in Etobicoke. Regular cleans, deep cleans, move in "
          "and move out, condos, kitchens and bathrooms, offices, carpets and interior windows. "
          "Free quotes, open 7 days a week."),
    canonical=BASE + "/",
    extra_ld=ld_business() + ld_faq(HOME_FAQ),
) + """
  <!-- ============================================================
       OS WINDOW hero
       ============================================================ -->
  <section class="osw">
    <div class="osw-arch"><span></span><span></span><span></span><span></span><span></span></div>

{TOPBAR}
    <div class="osw-stage osw-stage-home">

      <div class="osw-scene osw-scene-left">
        <div class="osw-product-aura"></div>
        <div class="osw-product-aura cool"></div>
        <div class="osw-panel">
          <span class="osw-panel-eyebrow">Etobicoke &amp; Toronto</span>
          <h2>Clean spaces.<br>Happy faces.</h2>
          <p>Homes, condos, rentals and small offices, cleaned by a crew that finishes the edges. Regular visits, one off deep cleans and move out work, all on one number.</p>
          <ul class="osw-panel-list">
            <li>A price agreed before we start</li>
            <li>Quote back the same day, usually within the hour</li>
            <li>Open seven days a week</li>
          </ul>
          <div class="osw-panel-foot">
            <span><strong>{PHONE}</strong></span>
            <span>{HOURS}</span>
          </div>
        </div>
      </div>

      <div class="osw-scene">
        <div class="svc-ring" aria-label="What Fanta Cleaning does">
          <div class="svc-ring-rotor">
            {RING}
          </div>
          <div class="svc-ring-center">
            <span class="crown">{LEAF}</span>
            <strong>FANTA</strong>
            <small>Cleaning</small>
          </div>
        </div>
      </div>
    </div>

    <div class="osw-title">
      <h1>Etobicoke <span class="glow">HOUSE CLEANING</span></h1>
      <p class="sub">One crew, one standard, every visit. Regular cleans that hold up, deep cleans that reset a home, and move out work that passes a walkthrough. Free quote by photo, seven days a week.</p>
      <div class="btn-row" style="margin-top: 1.5rem;">
        <a class="btn btn-whatsapp" href="{WA}" target="_blank" rel="noopener">{WAICON} Free Quote on WhatsApp</a>
        <a class="btn btn-primary" href="contact.html">Book a Clean</a>
        <a class="btn btn-glass" href="tel:{TEL}">Call {PHONE}</a>
      </div>
    </div>
  </section>

  <!-- ============================================================
       WHY FANTA
       ============================================================ -->
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Why Fanta</span>
        <h2>A home that is actually clean, not just tidied</h2>
        <p>Tidying is moving things around. Cleaning is the grout, the baseboards, the top of the door frames and the inside of the oven. The difference is obvious a week later, which is the whole point.</p>
      </div>
      <div class="why-grid">
        <div class="why-card">
          <div class="why-media">
            <img src="images/residential-cleaning.jpg" alt="Cleaner vacuuming a bright living room" loading="lazy">
          </div>
          <div class="why-body">
            <span class="icon sun">{SPRAY}</span>
            <h3>Every Room, Every Visit</h3>
            <p>Kitchens, bathrooms, bedrooms, floors and the bits in between. Nothing gets skipped because it was done last time.</p>
          </div>
        </div>

        <div class="why-card">
          <div class="why-media">
            <img src="images/move-out-cleaning.jpg" alt="Baseboards cleaned in an empty unit before handover" loading="lazy">
          </div>
          <div class="why-body">
            <span class="icon steel">{KEY}</span>
            <h3>Built for Handovers</h3>
            <p>Move outs, tenant turnovers and listing prep, done to the standard a walkthrough is judged by.</p>
          </div>
        </div>

        <div class="why-card">
          <div class="why-media">
            <img src="images/kitchen-deep-clean.jpg" alt="Stovetop being degreased during a deep clean" loading="lazy">
          </div>
          <div class="why-body">
            <span class="icon gold">{CHECK}</span>
            <h3>Price Agreed First</h3>
            <p>You get a quote from photos before anyone arrives. No hourly surprises at the door.</p>
          </div>
        </div>

        <div class="why-card">
          <div class="why-media">
            {WAMOCK}
          </div>
          <div class="why-body">
            <span class="icon slate">{CHAT}</span>
            <h3>Quote by WhatsApp</h3>
            <p>Photos in, price out. Most quotes come back the same day, often within the hour.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================
       Two feature tiles: media on top, words underneath
       ============================================================ -->
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">A look at the work</span>
        <h2>Before the visit, and after it</h2>
      </div>
      <div class="grid grid-2">
        <a class="bx-tile" href="{WA}" target="_blank" rel="noopener">
          <div class="bx-media">
            <img class="bg" src="images/property-exterior.jpg" alt="Well kept Etobicoke home with a tidy exterior" loading="lazy">
          </div>
          <h3>GET A QUOTE <span class="arrow">&#8599;</span></h3>
          <p>Send photos of the home on WhatsApp and get a price back today.</p>
        </a>
        <a class="bx-tile" href="services.html">
          <div class="bx-media">
            <img class="bg" src="images/living-room.jpg" alt="Modern living room left clean and reset" loading="lazy">
          </div>
          <h3>SERVICES <span class="arrow">&#8599;</span></h3>
          <p>Regular cleans, deep cleans, move in and out, condos, kitchens, bathrooms, offices, carpets and windows.</p>
        </a>
      </div>
    </div>
  </section>

  <!-- ============================================================
       SERVICES grid
       ============================================================ -->
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Services</span>
        <h2>What we do across {AREA}</h2>
        <p>Pick the one you need, or ask for a few at once. Most homes book a deep clean first and then settle into a regular visit.</p>
      </div>
      <div class="grid grid-3">
{TILES}
      </div>
      <div style="text-align:center; margin-top:2rem;"><a class="btn btn-glass" href="services.html">See all services</a></div>
    </div>
  </section>

  <!-- ============================================================
       Gallery
       ============================================================ -->
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">The detail</span>
        <h2>Where the time actually goes</h2>
        <p>Anyone can run a vacuum down the middle of a room. The difference shows in the edges, the glass, the grout and the corners of a home people stop noticing until they are wrong.</p>
      </div>
      {STRIP}
    </div>
  </section>

  <!-- ============================================================
       What you can count on
       ============================================================ -->
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Our standards</span>
        <h2>What you can count on</h2>
        <p>Plain commitments, no fine print.</p>
      </div>
      <div class="grid grid-3">
        <div class="review-tile">
          <div class="rev-head"><span class="rev-av a">1</span><span class="rev-name"><strong>A price before we start</strong><small>No hourly creep</small></span></div>
          <p class="quote">You approve the quote first. If we find more than the photos showed, we tell you and agree the change before carrying on.</p>
        </div>
        <div class="review-tile">
          <div class="rev-head"><span class="rev-av b">2</span><span class="rev-name"><strong>We finish the job</strong><small>Including the awkward part</small></span></div>
          <p class="quote">Behind the fridge, the top of the frames, the shower track. We'd rather stay the extra twenty minutes than leave it obvious.</p>
        </div>
        <div class="review-tile">
          <div class="rev-head"><span class="rev-av c">3</span><span class="rev-name"><strong>Walk it with us</strong><small>Before we pack up</small></span></div>
          <p class="quote">If you're home, we walk the place together at the end. If you're not, you get photos. Anything missed gets put right.</p>
        </div>
        <div class="review-tile">
          <div class="rev-head"><span class="rev-av d">4</span><span class="rev-name"><strong>Open seven days</strong><small>Early starts, evening slots</small></span></div>
          <p class="quote">We work around school runs, shift work, handover times and listing photos. Tell us the window and we will fit it.</p>
        </div>
        <div class="review-tile">
          <div class="rev-head"><span class="rev-av e">5</span><span class="rev-name"><strong>Careful in an empty home</strong><small>Keys, codes, concierge</small></span></div>
          <p class="quote">Plenty of our work happens with nobody there. We lock up, report in and leave the place exactly as we found it, minus the mess.</p>
        </div>
        <div class="review-tile">
          <div class="rev-head"><span class="rev-av a">6</span><span class="rev-name"><strong>Your home, your rules</strong><small>Products, pets, rooms</small></span></div>
          <p class="quote">Rooms you want left alone stay untouched. If you want your own products used, leave them out and say so.</p>
        </div>
      </div>
      <div style="text-align:center; margin-top:2rem;"><a class="btn btn-glass" href="reviews.html">Reviews &amp; feedback</a></div>
    </div>
  </section>

  <!-- ============================================================
       FAQ
       ============================================================ -->
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">FAQ</span>
        <h2>Frequently asked questions</h2>
      </div>
      <div class="faq-layout">
        <div class="faq-deco">
          <div class="deco-media"><img src="images/bathroom-detail.jpg" alt="Bathroom faucet and sink being detailed" loading="lazy"></div>
          <div class="deco-media"><img src="images/bathroom-result.jpg" alt="Clean bathroom with polished glass and tile" loading="lazy"></div>
          <div class="deco-tag"><span class="dot"></span>Glass, tile and grout</div>
        </div>

        {FAQ}

        <div class="faq-deco">
          <div class="deco-media"><img src="images/window-cleaning.jpg" alt="Interior window being cleaned streak free" loading="lazy"></div>
          <div class="deco-media"><img src="images/dining-detail.jpg" alt="Dining table detailed to a streak free finish" loading="lazy"></div>
          <div class="deco-tag"><span class="dot"></span>Windows, frames and tracks</div>
        </div>
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(
    TOPBAR=topbar(0), RING="\n            ".join(ring_cards), WA=WA_QUOTE,
    WAICON=SVG["wa"], TEL=PHONE_TEL, PHONE=PHONE, HOURS=HOURS_SHORT, SPRAY=SVG["spray"],
    KEY=SVG["key"], LEAF=SVG["leaf"],
    CHECK=SVG["check"], CHAT=SVG["chat"], WAMOCK=wa_mock(0), AREA=AREA,
    TILES=service_tiles(0, [s for s in SERVICES if s["slug"] != "recurring-cleaning-etobicoke"]),
    STRIP=photo_strip(0, [
        ("images/kitchen-detail.jpg", "Kitchen stovetop and surround detail", "Kitchen surfaces"),
        ("images/bathroom-result.jpg", "Shower screen and tile left clear", "Showers and tile"),
        ("images/wood-floor.jpg", "Polished wood floor in a living room", "Floors and carpet"),
        ("images/childrens-room.jpg", "Child's bedroom dusted and tidied", "Bedrooms"),
        ("images/window-cleaning.jpg", "Interior window cleaned streak free", "Glass and sills"),
        ("images/office-cleaning.jpg", "Office desk disinfected after hours", "Office spaces"),
        ("images/entry-mopping.jpg", "Entryway floor being mopped", "Entryways"),
        ("images/carpet-cleaning.jpg", "Carpet cleaned with hot water extraction", "Carpet and rugs"),
    ]),
    FAQ=faq_block(HOME_FAQ), CTA=cta_strip(0), FOOT=footer(0))

page("index.html", home)


# ======================================================================
# SERVICES
# ======================================================================
services_page = head(
    title="Cleaning Services in Etobicoke &amp; Toronto | " + NAME,
    desc=("Every service from Fanta Cleaning: house cleaning, deep cleaning, move in and move out, condos "
          "and apartments, kitchens and bathrooms, offices, carpets, interior windows, post-renovation "
          "and recurring plans across Etobicoke and Toronto."),
    canonical=BASE + "/services.html",
    extra_ld=ld_breadcrumb([("Services", "services.html")]),
) + hero_small(
    0, [("Services", "services.html")],
    "Everything We", "CLEAN",
    "Ten services, one crew, one invoice. Most homes book two or three at a time: a deep clean with the windows, a move out with the carpets, a regular visit with the oven every few months.",
    media="images/living-room.jpg",
    alt="Modern living room cleaned and reset",
) + """
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Around the home</span>
        <h2>Cleaning services</h2>
        <p>Recurring or one off, occupied or empty.</p>
      </div>
      <div class="grid grid-3">
{INSIDE}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Specialist work</span>
        <h2>Detail services</h2>
        <p>The jobs that need equipment, patience or both.</p>
      </div>
      <div class="grid grid-2">
{OUTSIDE}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Bundles</span>
        <h2>What people usually book together</h2>
      </div>
      <div class="grid grid-3">
        <div class="glass-card">
          <img src="images/move-out-cleaning.jpg" alt="Baseboards cleaned during a move out" loading="lazy">
          <h3>The handover</h3>
          <p>Move out clean, interior windows and a carpet pass. Everything a walkthrough or a listing photo picks up on.</p>
          <p><a href="move-out-cleaning-etobicoke.html">Move out cleaning &rarr;</a></p>
        </div>
        <div class="glass-card">
          <img src="images/kitchen-deep-clean.jpg" alt="Stovetop degreased during a deep clean" loading="lazy">
          <h3>The reset</h3>
          <p>Deep clean through the whole home, kitchens and bathrooms taken back to the tile. Usually booked in spring or before guests arrive.</p>
          <p><a href="deep-cleaning-etobicoke.html">Deep cleaning &rarr;</a></p>
        </div>
        <div class="glass-card">
          <img src="images/kitchen-detail.jpg" alt="Fine dust wiped from a kitchen surface after a renovation" loading="lazy">
          <h3>After the trades</h3>
          <p>Post-renovation cleanup with a window and floor pass, so the finished work is actually visible.</p>
          <p><a href="post-renovation-cleaning.html">Post-renovation &rarr;</a></p>
        </div>
      </div>
      {STRIP}
    </div>
  </section>

{CTA}{FOOT}""".format(
    INSIDE=service_tiles(0, [s for s in SERVICES if s["slug"] in (
        "house-cleaning-etobicoke", "deep-cleaning-etobicoke", "move-out-cleaning-etobicoke",
        "condo-cleaning-etobicoke", "kitchen-bathroom-cleaning",
        "recurring-cleaning-etobicoke")]),
    OUTSIDE=service_tiles(0, [s for s in SERVICES if s["slug"] in (
        "office-cleaning-etobicoke", "carpet-cleaning-etobicoke",
        "window-cleaning-etobicoke", "post-renovation-cleaning")]),
    STRIP=photo_strip(0, [
        ("images/bedroom-result.jpg", "Freshly made bed in a clean bedroom", "Bedrooms"),
        ("images/floor-mopping.jpg", "Hard floor mopped through a hallway", "Hard floors"),
        ("images/carpet-cleaning.jpg", "Carpet cleaned with hot water extraction", "Carpets"),
        ("images/office-cleaning.jpg", "Office desk cleaned after hours", "Offices"),
    ]),
    CTA=cta_strip(0), FOOT=footer(0))

page("services.html", services_page)


# ======================================================================
# PRICING
# ======================================================================
PRICING_FAQ = [
    ("Why are there no prices listed on this page?",
     "Because an honest number needs two minutes of information. A three bedroom semi with pets is not the same job as a three bedroom semi that was cleaned last week. Send photos and you get a real figure, not a starting-from price that changes at the door."),
    ("How fast do quotes come back?",
     "Usually the same day, often within the hour during working hours. Weekends included."),
    ("Is the quote fixed?",
     "The quote holds for the work described. If we arrive and the job is clearly bigger than the photos showed, we stop, show you, and agree the difference before carrying on. We never add to an invoice after the fact."),
    ("Do you charge by the hour or by the job?",
     "By the job for most cleaning work, so you know the cost in advance. Recurring plans are priced per visit."),
    ("What affects the price most?",
     "Size of the home, how long since the last clean, whether it is occupied or empty, pets, and extras like inside the oven, inside the fridge or the carpets."),
    ("How do I pay?",
     "Payment is arranged directly with us when the work is booked. Ask when you get your quote and we'll confirm what is accepted."),
]

pricing = head(
    title="Pricing &amp; Free Quotes | " + NAME + " Etobicoke",
    desc=("How Fanta Cleaning prices house cleaning in Etobicoke and Toronto. Free photo quotes, price "
          "agreed before we start, no hourly surprises."),
    canonical=BASE + "/pricing.html",
    extra_ld=ld_breadcrumb([("Pricing", "pricing.html")]) + ld_faq(PRICING_FAQ),
) + hero_small(
    0, [("Pricing", "pricing.html")],
    "Know the Price", "BEFORE WE START",
    "Send photos, get a figure, decide. Nothing begins until you have agreed a number, and that number does not move unless the job does.",
    media="images/kitchen-deep-clean.jpg",
    alt="Stovetop degreased during a deep clean",
) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <h2>How a quote works</h2>
          <p>Three steps, and the first two cost you nothing.</p>

          <div class="grid grid-3" style="margin:1.5rem 0;">
            <div class="glass-card">
              <img src="images/dining-detail.jpg" alt="Dining table being detailed" loading="lazy">
              <h3>1. Show us</h3>
              <p>Photos on WhatsApp, or a quick description on the phone. Rooms, rough size, and anything unusual.</p>
            </div>
            <div class="glass-card">
              <img src="images/kitchen-detail.jpg" alt="Kitchen surface detail after a clean" loading="lazy">
              <h3>2. Get a number</h3>
              <p>A price for the work as described, with what is included spelled out. Same day, usually within the hour.</p>
            </div>
            <div class="glass-card">
              <img src="images/entry-mopping.jpg" alt="Entryway floor mopped at the start of a visit" loading="lazy">
              <h3>3. Pick a window</h3>
              <p>Choose a day and a start time. We work seven days a week, early starts included.</p>
            </div>
          </div>

          <h2>What a price is built from</h2>
          <p>Every quote comes down to the same handful of things. Knowing them helps you tell whether any quote, ours or anyone else's, is reasonable.</p>
          <ul>
            <li><strong>Size and layout.</strong> Square footage, number of bathrooms, number of floors and whether there are stairs.</li>
            <li><strong>Condition.</strong> A maintained home and a home that has not been cleaned in a year are different jobs, and pretending otherwise is how surprise invoices happen.</li>
            <li><strong>Occupied or empty.</strong> Empty units clean faster but get judged harder, because there is no furniture hiding anything.</li>
            <li><strong>Scope.</strong> Inside the oven, inside the fridge, inside cabinets, interior windows, carpets: each one adds time, so each one is priced, not assumed.</li>
            <li><strong>Pets and people.</strong> Shedding, litter areas and heavy traffic all add time, especially on carpets and soft furniture.</li>
            <li><strong>Access.</strong> Elevator bookings, parking and walk-up distance cost time on condo and apartment work.</li>
          </ul>

          <h2>Recurring work costs less per visit</h2>
          <p>A home cleaned every two weeks never gets far from clean, so each visit takes less time. Weekly, biweekly and monthly schedules are priced per visit and come in under a comparable one off clean. Landlords and small offices with several properties are quoted as a block.</p>

          <figure class="media-figure">
            <img src="images/office-cleaning.jpg" alt="Office desk being disinfected after hours" loading="lazy">
            <figcaption>Office work is usually quoted per visit on a fixed schedule, after hours or before opening.</figcaption>
          </figure>

          <h2>Questions about pricing</h2>
          {FAQ}
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(FAQ=faq_block(PRICING_FAQ),
                      SIDEBAR=sidebar(0, photo="images/bedroom-result.jpg",
                                      photo_alt="Freshly made bed in a clean bedroom",
                                      photo_cap="Quoted, cleaned, done"),
                      CTA=cta_strip(0), FOOT=footer(0))

page("pricing.html", pricing)


# ======================================================================
# ABOUT
# ======================================================================
about = head(
    title="About " + NAME + " | Etobicoke House Cleaning",
    desc=("Who we are: a house cleaning crew based at " + ADDRESS_LINE + ", cleaning homes, condos and "
          "small offices across Etobicoke, Toronto and the west GTA, seven days a week."),
    canonical=BASE + "/about.html",
    extra_ld=ld_breadcrumb([("About", "about.html")]),
) + hero_small(
    0, [("About", "about.html")],
    "A Local Crew for", "YOUR HOME",
    "Fanta Cleaning is based in Etobicoke and cleans homes, condos, rentals and small offices across the west end of the city. Clean spaces, happy faces, same crew every time.",
    media="images/property-exterior.jpg",
    alt="Well kept Etobicoke home with a tidy exterior",
) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <h2>Why the same crew matters</h2>
          <p>Most cleaning companies send whoever is free. You spend the first twenty minutes of every visit explaining the home again: which floor cannot take water, where the spare bulbs live, which door sticks, which room the baby sleeps in.</p>
          <p>Fanta works the other way around. On a recurring plan you get the same people, and after two or three visits nobody needs telling anything. That is the entire reason recurring cleans come out better than one offs, and why they take less time.</p>

          <figure class="media-figure">
            <img src="images/residential-cleaning.jpg" alt="Cleaner working through a bright living room" loading="lazy">
            <figcaption>Regular visits mean the same crew, who learn the home instead of starting from scratch each time.</figcaption>
          </figure>

          <h2>Who we work for</h2>
          <ul>
            <li><strong>Homeowners</strong> who want a standing clean and somebody reliable for the bigger seasonal reset.</li>
            <li><strong>Condo and apartment residents</strong> who need the work done properly in a small footprint, around building rules.</li>
            <li><strong>Landlords and property managers</strong> who need units turned around fast between tenants, with photos to prove it.</li>
            <li><strong>Realtors</strong> getting a property camera ready before listing day.</li>
            <li><strong>Small offices, clinics and studios</strong> that need cleaning around their opening hours, not during them.</li>
          </ul>

          <h2>How we work</h2>
          <p>Quote first, always before anyone arrives. We bring our own equipment and products, and we will happily use yours instead if you leave them out. We finish by walking the home, in person if you are there and by photo if you are not.</p>
          <p>If something was missed, tell us within a couple of days and we come back. That is cheaper for us than losing a client, and fairer to you.</p>

          <h2>Where we work</h2>
          <p>Etobicoke is home, so that is where we are fastest. From there we cover Toronto, Mississauga, North York, Brampton and Vaughan. If you are just outside that ring, ask anyway.</p>
          {STRIP}
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(
    STRIP=photo_strip(0, [
        ("images/property-exterior.jpg", "Detached home exterior in Etobicoke", "Etobicoke"),
        ("images/living-room.jpg", "Condo living room cleaned in Toronto", "Toronto"),
        ("images/bedroom-result.jpg", "Bedroom cleaned and made up", "Mississauga"),
        ("images/wood-floor.jpg", "Wood floor polished in a North York home", "North York"),
    ]),
    SIDEBAR=sidebar(0, photo="images/childrens-room.jpg",
                    photo_alt="Child's bedroom dusted and tidied",
                    photo_cap="The rooms that matter most"),
    CTA=cta_strip(0), FOOT=footer(0))

page("about.html", about)


# ======================================================================
# CONTACT
# ======================================================================
contact = head(
    title="Contact &amp; Free Quote | " + NAME + " Etobicoke",
    desc=("Get a free quote from Fanta Cleaning. WhatsApp " + PHONE + " with photos, or call. Based at " +
          ADDRESS_LINE + ", open 7 days a week."),
    canonical=BASE + "/contact.html",
    extra_ld=ld_breadcrumb([("Contact", "contact.html")]),
) + hero_small(
    0, [("Contact", "contact.html")],
    "Tell Us What", "NEEDS DOING",
    "Photos are the fastest route to a real price. Send them on WhatsApp and you will usually have a number back within the hour.",
    media="images/entry-mopping.jpg",
    alt="Entryway floor being mopped at the start of a visit",
) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <h2>Three ways to reach us</h2>
          <div class="grid grid-3" style="margin:1.5rem 0;">
            <a class="glass-card" href="{WA}" target="_blank" rel="noopener" style="text-decoration:none;">
              <img src="images/dining-detail.jpg" alt="Dining table being detailed" loading="lazy">
              <h3>WhatsApp</h3>
              <p>Best for quotes. Send photos of the home and anything specific you want handled.</p>
              <p><strong>{PHONE}</strong></p>
            </a>
            <a class="glass-card" href="tel:{TEL}" style="text-decoration:none;">
              <img src="images/floor-mopping.jpg" alt="Hard floor being mopped" loading="lazy">
              <h3>Phone</h3>
              <p>Best for scheduling and short notice jobs. Call early for same day availability.</p>
              <p><strong>{PHONE}</strong></p>
            </a>
            <a class="glass-card" href="{MAPS}" target="_blank" rel="noopener" style="text-decoration:none;">
              <img src="images/property-exterior.jpg" alt="Etobicoke home exterior" loading="lazy">
              <h3>Google Profile</h3>
              <p>Find us on Google, check the hours and leave a review after your visit.</p>
              <p><strong>{NAMEP}</strong></p>
            </a>
          </div>

          <h2>What to include in your message</h2>
          <p>The more of this you send, the more accurate the quote and the fewer back and forth messages:</p>
          <ul>
            <li>The service you want, or just a description of the problem.</li>
            <li>Property type and rough size: condo, semi, detached, office, number of bedrooms and bathrooms.</li>
            <li>Photos of each space, including the parts you are worried about.</li>
            <li>Whether the home is occupied or empty, and whether someone will be there.</li>
            <li>Pets, and anything in the home that needs handling carefully.</li>
            <li>Dates that work, and any hard deadline like a handover or a listing shoot.</li>
          </ul>

          <figure class="media-figure">
            <img src="images/move-out-cleaning.jpg" alt="Baseboards cleaned in an empty unit before handover" loading="lazy">
            <figcaption>If there is a deadline, say so in the first message. Handovers and listing shoots get scheduled around.</figcaption>
          </figure>

          <h2>Where to find us</h2>
          <div class="info-row">{PIN}<div><strong>Address</strong><br>{ADDRESS}</div></div>
          <div class="info-row">{CLOCK}<div><strong>Hours</strong><br>Open 7 days a week</div></div>
          <div class="info-row">{HOME}<div><strong>Service area</strong><br>{AREA} and the west GTA</div></div>

          <div class="btn-row" style="margin-top:1.6rem;">
            <a class="btn btn-whatsapp" href="{WA}" target="_blank" rel="noopener">{WAICON} Message on WhatsApp</a>
            <a class="btn btn-gold" href="tel:{TEL}">Call {PHONE}</a>
          </div>
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(WA=WA_QUOTE, WAICON=SVG["wa"], PHONE=PHONE, TEL=PHONE_TEL, MAPS=MAPS,
                      CLOCK=SVG["clock"], PIN=SVG["pin"], HOME=SVG["home"], AREA=AREA,
                      ADDRESS=ADDRESS_LINE, NAMEP=strip(NAME),
                      SIDEBAR=sidebar(0, photo="images/kitchen-detail.jpg",
                                      photo_alt="Kitchen surface detail after a clean",
                                      photo_cap="Send a photo, get a price"),
                      CTA=cta_strip(0), FOOT=footer(0))

page("contact.html", contact)


# ======================================================================
# REVIEWS
# ======================================================================
reviews = head(
    title="Reviews | " + NAME + " Etobicoke",
    desc=("Fanta Cleaning on Google: rated 5.0. Read the profile, leave a review after your visit, and "
          "see the standards every job is held to."),
    canonical=BASE + "/reviews.html",
    extra_ld=ld_breadcrumb([("Reviews", "reviews.html")]),
) + hero_small(
    0, [("Reviews", "reviews.html")],
    "Judge Us on", "THE LAST JOB",
    "Our Google profile is young, so there is nothing here worth dressing up. What we can tell you is exactly what every visit is held to, and where to say so if we miss it.",
    media="images/bathroom-result.jpg",
    alt="Clean bathroom with polished glass and tile",
) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <h2>On Google</h2>
          <div class="glass-card" style="margin:1.2rem 0;">
            <div class="rev-head">
              <span class="rev-av a">{STAR}</span>
              <span class="rev-name"><strong>{RATING} out of 5 on Google</strong><small>{COUNT} review so far</small></span>
            </div>
            <p class="quote">&ldquo;Great job!! Esther and her team are professionals; they are on time, very experienced, very knowledgeable with their products and equipments and reasonable priced. I'm very pleased with their work, definitely recommend and would surely hire them again.&rdquo;</p>
            <p style="margin:0;"><small>A R Prit, on our Google Business Profile</small></p>
          </div>
          <p>That is the whole of it. One review, from one customer, left where anyone can check it. If we have worked on your home, a review there is the most useful thing you can do for us, good or bad. If something was wrong, tell us first and we will come back and fix it.</p>
          <div class="btn-row" style="margin:1.2rem 0;">
            <a class="btn btn-primary" href="{MAPS}" target="_blank" rel="noopener">Open our Google profile</a>
            <a class="btn btn-whatsapp" href="{WAFB}" target="_blank" rel="noopener">Send feedback on WhatsApp</a>
          </div>

          <h2>What we hold ourselves to</h2>
          <p>Until there are more reviews here to read, this is the honest version of what you are buying.</p>

          <div class="grid grid-2" style="margin:1.4rem 0;">
            <div class="review-tile">
              <div class="rev-head"><span class="rev-av a">{CHECKTXT}</span><span class="rev-name"><strong>The quote is the price</strong><small>Agreed before we start</small></span></div>
              <p class="quote">If the job turns out bigger than the photos showed, we stop and show you before doing anything that changes the cost.</p>
            </div>
            <div class="review-tile">
              <div class="rev-head"><span class="rev-av b">{CHECKTXT}</span><span class="rev-name"><strong>Missed something? We return</strong><small>No argument</small></span></div>
              <p class="quote">Tell us within a couple of days and we come back and put it right. That is cheaper for us than a bad review, and fairer to you.</p>
            </div>
            <div class="review-tile">
              <div class="rev-head"><span class="rev-av c">{CHECKTXT}</span><span class="rev-name"><strong>Photos on empty homes</strong><small>Proof, not promises</small></span></div>
              <p class="quote">Turnovers and move outs finish with photos sent to you, so a landlord in another city can see the unit without driving to it.</p>
            </div>
            <div class="review-tile">
              <div class="rev-head"><span class="rev-av d">{CHECKTXT}</span><span class="rev-name"><strong>Your home, your rules</strong><small>Products, pets, rooms</small></span></div>
              <p class="quote">Rooms you want left alone stay untouched. If you want your own products used, leave them out and say so.</p>
            </div>
          </div>

          <h2>The work speaks first</h2>
          {STRIP}
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(
    MAPS=MAPS, WAFB=wa("I'd like to leave feedback about a job you did for me:"),
    CHECKTXT="&#10003;", STAR=SVG["star"], RATING="5.0", COUNT="1",
    STRIP=photo_strip(0, [
        ("images/bathroom-detail.jpg", "Bathroom faucet detailed", "Bathrooms"),
        ("images/kitchen-detail.jpg", "Kitchen stovetop detail", "Kitchens"),
        ("images/wood-floor.jpg", "Polished wood floor", "Floors"),
        ("images/move-out-cleaning.jpg", "Unit cleaned between tenants", "Turnovers"),
    ]),
    SIDEBAR=sidebar(0, photo="images/office-cleaning.jpg",
                    photo_alt="Office desk cleaned after hours",
                    photo_cap="Office accounts"),
    CTA=cta_strip(0), FOOT=footer(0))

page("reviews.html", reviews)


# ======================================================================
# LEGAL
# ======================================================================
def legal(slug, title, heading, body):
    return head(
        title=title + " | " + NAME,
        desc=title + " for " + strip(NAME) + ", a house cleaning business operating in Etobicoke, Ontario.",
        canonical=BASE + "/" + slug,
        extra_ld=ld_breadcrumb([(heading, slug)]),
    ) + hero_small(
        0, [(heading, slug)], heading.split(" ")[0], " ".join(heading.split(" ")[1:]).upper() or "PAGE",
        "The plain version. If anything here is unclear, ask us and we will explain it in a sentence.",
        media="images/wood-floor.jpg", alt="Polished wood floor in a cleaned home",
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
          <p>Only what we need to quote and carry out your job: your name, the contact details you message us from, the property address, and any photos or notes you send about the work.</p>

          <h2>How we use it</h2>
          <p>To prepare a quote, schedule the visit, do the work and follow up afterwards. Where a job finishes with completion photos, those are sent to you and kept only as long as they are useful for that job.</p>

          <h2>What we do not do</h2>
          <p>We do not sell your details, we do not share them with marketing companies, and we do not add you to a mailing list because you asked for a quote.</p>

          <h2>Messaging services</h2>
          <p>If you contact us through WhatsApp, that conversation also sits on WhatsApp's own servers under their terms, not ours. The same applies to any review you leave on Google.</p>

          <h2>This website</h2>
          <p>This site is a set of static pages. It does not ask you to log in, it does not run advertising trackers, and the only third party it loads is the Google Fonts service used for the typefaces.</p>

          <h2>Your choices</h2>
          <p>Ask us at any time what we hold about you, or ask us to delete it. Call or message the number on this site and we will deal with it.</p>

          <h2>Contact</h2>
          <p>Questions about privacy go to <a href="tel:{TEL}">{PHONE}</a>.</p>""".format(TEL=PHONE_TEL, PHONE=PHONE)

terms_body = """          <h2>Quotes</h2>
          <p>A quote covers the work described in it, based on the photos and information you provide. If the home turns out to be materially different from what was described, we stop, show you, and agree any change with you before continuing.</p>

          <h2>Access and scheduling</h2>
          <p>You arrange access, whether that is being there, a key, a lockbox code or a concierge instruction. If a crew arrives and cannot get in, we will try to reach you and reschedule.</p>

          <h2>Your belongings</h2>
          <p>We treat what is in a home as yours unless you tell us otherwise. Nothing is thrown out that has not been pointed out for removal. If you are unsure about an item, leave it and tell us.</p>

          <h2>What we do not handle</h2>
          <p>We do not handle hazardous waste, including paint, solvents, fuel, asbestos, chemicals and pressurised containers, and we do not work on exterior heights. Ask before the visit and we will point you to the right trade.</p>

          <h2>If something is wrong</h2>
          <p>Tell us within a couple of days of the visit and we will come back and put it right. If something is damaged while we are working, tell us straight away so we can deal with it properly.</p>

          <h2>Cancellations</h2>
          <p>Let us know as early as you can. Short notice cancellations cost a crew their day, so please call rather than leaving it.</p>

          <h2>Payment</h2>
          <p>Payment terms are confirmed when you book, along with your quote.</p>

          <h2>Contact</h2>
          <p>Questions about these terms go to <a href="tel:{TEL}">{PHONE}</a>.</p>""".format(TEL=PHONE_TEL, PHONE=PHONE)

page("privacy.html", legal("privacy.html", "Privacy Policy", "Privacy Policy", privacy_body))
page("terms.html", legal("terms.html", "Terms of Service", "Terms of Service", terms_body))

if __name__ == "__main__":
    for p in BUILT:
        print("built", p)
