# -*- coding: utf-8 -*-
"""Builds the eight service pages and the six service-area pages."""

from common import (NAME, NAME_FULL, PHONE, PHONE_TEL, AREA, BASE, MAPS, SVG, SERVICES,
                    BY_SLUG, LOCATIONS, sms, head, ld_service, ld_faq, ld_breadcrumb,
                    hero_small, photo_strip, service_tiles, cta_strip, footer, sidebar,
                    faq_block, write, strip, new_page, pick, img_tag)

BUILT = []

# ----------------------------------------------------------------------
# Per-service copy
# ----------------------------------------------------------------------
COPY = {
"residential-window-cleaning-edmonton": dict(
    h1="House Windows", glow="INSIDE AND OUT",
    sub="Glass, frames, sills and tracks on everything from a bungalow to a three storey walkout. Priced off a photo before anyone turns up.",
    intro=[
      "Most houses here get done twice a year. Outsides in May or June once the sprinklers have been running and the thaw grit has settled, then the full lot in September before the windows get shut for the winter.",
      "A first clean takes longer than people expect, especially on a house that has never had one. Years of film does not come off with soap and a quick pull, it has to be scrubbed loose first. After that, every clean is quicker and cheaper than the one before."],
    includes_title="What gets done",
    includes=[
      "<strong>The glass.</strong> Scrubbed, squeegeed and detailed into the corners, then the whole perimeter dried by hand.",
      "<strong>Frames and sills.</strong> Wiped down, which is where most of the visible dirt actually sits.",
      "<strong>Tracks.</strong> Vacuumed dry first. Wet them before the grit is out and you get paste in the corners that works its way back onto the glass.",
      "<strong>Screens, if you want them.</strong> Pulled, washed, dried and put back on the right window.",
      "<strong>A walk round at the end.</strong> Looking at the glass from an angle in the light, because that is the only way streaks show."],
    extras_title="Things people add",
    extras=[
      "Hard water treatment where the sprinklers have been hitting the glass",
      "Skylights and gable windows, reached by pole",
      "Garage and shed windows, usually forgotten",
      "Storm windows taken out and done separately",
      "Patio and french doors, which are mostly glass anyway"],
    good=[
      "You do not need to be home for outsides. Insides, someone has to let us in.",
      "Move anything breakable off the sills before we arrive and the job goes faster.",
      "Shrubs tight against the wall are the usual hold-up. Trimming them back helps more than you would think.",
      "If a pane is already cracked or the seal has gone, tell us. We would rather know than find out."],
    faq=[
      ("How long does a house take?", "Half a day for most, outsides only. Add the insides and it is usually a full day for a two storey."),
      ("Do you move furniture?", "We will shift a chair. Anything heavier, or a cabinet in front of the window, is better moved before we get there."),
      ("Will you do the inside in winter?", "Yes, interiors run all year. It is the outsides that stop once it is below freezing."),
      ("What if it rains afterwards?", "Clean glass sheds rain without spotting. It is dirty glass that streaks when it gets wet, so a shower the next day is not undoing the work.")],
    strip=["bay-window", "sunlit-living-room", "pole-on-home", "sill-wipe"],
    related=["interior-window-cleaning-edmonton", "window-screens-tracks-edmonton",
             "hard-water-stain-removal-edmonton"]),

"commercial-window-cleaning-edmonton": dict(
    h1="Commercial", glow="GLASS",
    sub="Offices, clinics and walk-up buildings on a set schedule, done before your doors open so nobody has to work round us.",
    intro=[
      "Commercial glass is less about difficulty and more about timing. The work is straightforward. Fitting it into a building that has staff, clients and a parking situation is the part that needs organising.",
      "We work to a fixed round, usually quarterly for offices and clinics. Same day of the quarter, same crew, invoiced the same way each time so it stops being something anyone has to think about."],
    includes_title="What a visit covers",
    includes=[
      "<strong>Exterior glass</strong> to the height we can reach from poles and ladders, which is about three storeys.",
      "<strong>Interior glass</strong> including partitions, internal doors and meeting room walls.",
      "<strong>Entrance doors.</strong> Both faces, plus the push plates and handles that collect every fingerprint in the building.",
      "<strong>Frames, sills and tracks</strong> through the whole run.",
      "<strong>An invoice that matches the quote</strong>, with the visit dated, for whoever does your books."],
    extras_title="Often added",
    extras=[
      "Internal glass partitions on a separate, more frequent round",
      "Post-fitout cleanup after a renovation",
      "Skylights and atrium glass within pole reach",
      "Hard water treatment on sprinkler-hit elevations"],
    good=[
      "Before opening is usually easiest for everyone. Evenings work too.",
      "Tell us about the parking before the first visit, not on the day.",
      "If there is a fob, an alarm code or a sign-in, we will sort it once and it stays sorted.",
      "Quarterly suits most offices. Buildings on a busy road need more."],
    faq=[
      ("Can you come outside business hours?", "Yes, and most clients prefer it. Early morning is the common one."),
      ("Are you insured?", "Ask when you request a quote and we will put the current certificate in writing before any work starts."),
      ("How high can you go?", "Three storeys or so, from ladders and water fed poles. Towers need rope access, which is a different trade."),
      ("Do you invoice monthly?", "We can set it up either way. Say what suits your bookkeeping when you book.")],
    strip=["commercial-building", "office-view", "commercial-pole", "sill-wipe"],
    related=["storefront-window-cleaning-edmonton", "interior-window-cleaning-edmonton",
             "post-construction-window-cleaning"]),

"storefront-window-cleaning-edmonton": dict(
    h1="Storefronts", glow="ON A ROUND",
    sub="Weekly or biweekly frontage for shops, cafes and restaurants. Fingerprints, salt film and whatever last night left on the glass.",
    intro=[
      "Shop frontage is judged from the sidewalk by people deciding whether to come in. It also gets dirty faster than anything else we clean, because it is at hand height on a street.",
      "Which is why storefronts go on a round rather than being booked job by job. Same morning every week, in and out before you open, and it costs less per visit than anything else we do because the glass never gets far from clean."],
    includes_title="What a round covers",
    includes=[
      "<strong>All street-facing glass</strong>, both faces where we can get to them.",
      "<strong>Entrance doors</strong>, including the push plates, handles and the kick panel at the bottom.",
      "<strong>Frames and the bottom rail</strong>, where the salt film builds up over winter.",
      "<strong>A quick pass on any interior glass</strong> you want included, like display cases or a vestibule."],
    extras_title="Worth adding in winter",
    extras=[
      "More frequent visits from November to March, when salt spray is constant",
      "Hard water treatment where a sidewalk sprinkler hits the glass",
      "Vestibule and inner door glass",
      "Signage faces, where they are glass or acrylic"],
    good=[
      "Early mornings are standard. We are usually gone before staff arrive.",
      "Winter is the busy season for frontage, not summer. Salt is worse than dust.",
      "A standing round means you stop having to ring anyone.",
      "Tell us if there is a stretch of sidewalk we should not block."],
    faq=[
      ("How often do shops book?", "Weekly for food and retail on a busy street. Biweekly for quieter frontage."),
      ("Do you work in winter?", "Frontage, yes. We use a cold weather mix and work in the warmest part of the morning. Below about minus ten it stops being workable and we move the visit."),
      ("What about the salt line along the bottom?", "That is the worst of it, and it is part of the job rather than an extra."),
      ("Can we skip a week?", "Tell us and we skip it. Nothing is locked in.")],
    strip=["retail-front", "storefront", "sill-wipe", "office-view"],
    related=["commercial-window-cleaning-edmonton", "hard-water-stain-removal-edmonton",
             "interior-window-cleaning-edmonton"]),

"interior-window-cleaning-edmonton": dict(
    h1="Interior", glow="GLASS",
    sub="The winter half of the job. Condensation marks, cooking film, and the patio door the dog uses as a window.",
    intro=[
      "Interiors are what we do when it is too cold to be outside, and there is more to them than people expect. A house shut up from October to April builds a film on the inside of the glass that nobody notices until the sun comes back round in February and lights it up.",
      "Kitchens are the worst of it. Cooking vapour travels further than you would think and settles on every pane in an open plan. Bathrooms get the condensation marks. And every house with a dog has one door at nose height that needs its own attention."],
    includes_title="What is covered",
    includes=[
      "<strong>Interior panes</strong> washed and squeegeed, not just wiped, which is what leaves the haze.",
      "<strong>Sills and interior frames</strong> by hand.",
      "<strong>Interior tracks</strong> vacuumed and wiped.",
      "<strong>Patio and french doors</strong>, both faces of the glass where we can reach.",
      "<strong>Mirrors and internal glass</strong> if you want them done while we are in."],
    extras_title="Often added",
    extras=[
      "Blinds taken down and rehung so the glass behind can be done",
      "Skylights from the inside, by pole",
      "Stairwell and vaulted glass",
      "Shower screens, which clean like windows and usually need descaling"],
    good=[
      "Someone has to be in, or leave a key.",
      "Clearing the sills first gets you more cleaning for the same money.",
      "Condensation marks on the inside usually clean off. Fog between the panes does not, that is a failed seal.",
      "Winter is the quiet season for this, so booking is easier than in June."],
    faq=[
      ("Can you do interiors in the middle of winter?", "Yes. It is most of what we do from November through March."),
      ("Will the marks between the panes come off?", "No. If the fog is inside the sealed unit the seal has failed and the glass needs replacing. We will tell you which windows those are."),
      ("Do you do blinds?", "We will take them down and put them back so the glass can be done properly. Cleaning the blinds themselves is a different job."),
      ("Shoes?", "Off at the door, or covers on. Whichever you prefer.")],
    strip=["interior-microfiber", "sunlit-living-room", "sill-wipe", "bay-window"],
    related=["residential-window-cleaning-edmonton", "window-screens-tracks-edmonton",
             "skylight-cleaning-edmonton"]),

"window-screens-tracks-edmonton": dict(
    h1="Screens", glow="&amp; TRACKS",
    sub="Screens out, washed and back on the right window. Tracks vacuumed dry before anything wet goes near them.",
    intro=[
      "This is the part most people skip, and it is the part that undoes the rest. A clean pane sitting in a track full of grit will have dirt streaking down it within a week of the first rain.",
      "Screens are worse. A screen with a season of dust in the mesh cuts the light coming in more than a dirty window does, and every time the wind blows it washes that dust back onto the glass you just paid to have cleaned."],
    includes_title="How it is done",
    includes=[
      "<strong>Screens come out first</strong> and get labelled, because they are not interchangeable and a screen in the wrong frame never sits right again.",
      "<strong>Washed flat</strong> with a soft brush and rinsed, not scrubbed upright, which stretches the mesh.",
      "<strong>Dried before refitting</strong>, so they are not going back wet onto clean glass.",
      "<strong>Tracks vacuumed dry.</strong> Every time. This is the step that matters.",
      "<strong>Then wiped out</strong>, corners included, with the weep holes checked and cleared."],
    extras_title="While we are there",
    extras=[
      "Rollers and sliders checked, so the window actually moves again",
      "Weep holes cleared on units that have been holding water",
      "Storm windows pulled and done separately",
      "Screen frames straightened where they have been bent"],
    good=[
      "Old screens go brittle in the sun. Perished mesh can tear coming out, and we will show you rather than quietly refit it.",
      "A screen that has never been out may be painted in. We will not force it.",
      "If a window has stopped sliding, it is usually the track rather than the mechanism.",
      "Doing screens and tracks with a glass clean is cheaper than booking it on its own."],
    faq=[
      ("Can you do screens without the windows?", "We can, but it rarely makes sense. The grit from the screens ends up on the glass."),
      ("What if a screen tears?", "We will show you and tell you what a replacement runs. Frames that are already perished sometimes do not survive coming out, which is why we check before pulling them."),
      ("Do you repair screens?", "No. We will tell you what is wrong with it and you can get it rescreened."),
      ("How often?", "Once a year with a spring clean is plenty for most houses.")],
    strip=["screen-brush", "track-detail", "frame-detail", "supplies"],
    related=["residential-window-cleaning-edmonton", "interior-window-cleaning-edmonton",
             "post-construction-window-cleaning"]),

"hard-water-stain-removal-edmonton": dict(
    h1="Hard Water", glow="SPOTTING",
    sub="The white spots the sprinklers leave. Mineral, not dirt, and no amount of soap will shift them.",
    intro=[
      "Every summer the same call comes in. The windows have just been cleaned and there are still white rings on the glass on the sprinkler side of the house. They are mineral deposits left behind when hard water evaporates off a hot pane, and they sit on the glass rather than in the dirt layer.",
      "A normal wash removes dirt. These need an acidic treatment, worked over the glass and given time, then flushed. It is slower, it is priced separately, and it is worth knowing in advance that very old spotting does not always come all the way back."],
    includes_title="How it works",
    includes=[
      "<strong>We look first</strong> and tell you what is likely to come off. Fresh spotting usually goes completely. A few years of it often lightens rather than disappears.",
      "<strong>The glass gets washed normally first</strong>, so the treatment is working on mineral and not on dirt.",
      "<strong>Treatment applied and worked</strong>, with dwell time, across the affected panes.",
      "<strong>Flushed and squeegeed</strong>, then checked from an angle in the light.",
      "<strong>A second pass</strong> where it is needed, which on bad panes it often is."],
    extras_title="Related work",
    extras=[
      "Glass shower screens, which scale the same way",
      "Storefront glass hit by a sidewalk sprinkler",
      "Advice on redirecting the sprinkler head, which is the actual fix",
      "Treatment on a repeat round, to stop it building again"],
    good=[
      "The real fix is pointing the sprinkler somewhere else. We will say so rather than sell you an annual treatment.",
      "Spotting that has etched the glass is physical damage and will not clean off. We check for this first.",
      "South and west elevations are usually the worst, because the water dries faster.",
      "Catching it in the first season is much easier than in the fourth."],
    faq=[
      ("Will it all come off?", "Fresh spotting, usually yes. Several years of it, usually not completely. We tell you which you have before quoting."),
      ("Why is it priced separately?", "Because it is a treatment with dwell time, not a wash. On a bad elevation it can take as long as cleaning the rest of the house."),
      ("Can it damage the glass?", "The treatment, no, used properly. The spotting itself can etch glass if it has been left for years, and that damage is already done."),
      ("How do I stop it coming back?", "Move the sprinkler head, or change its arc. That is genuinely the whole answer.")],
    strip=["brush-closeup", "squeegee-soapy", "before-after", "cloth-polish"],
    related=["residential-window-cleaning-edmonton", "storefront-window-cleaning-edmonton",
             "commercial-window-cleaning-edmonton"]),

"skylight-cleaning-edmonton": dict(
    h1="Skylights", glow="&amp; HIGH GLASS",
    sub="Stairwell windows, vaulted gable glass and skylights. The panes nobody can reach, which is why they are always the dirtiest.",
    intro=[
      "High glass gets cleaned when somebody finally gets annoyed enough about it, which is usually years. Because it faces up or sits above a stairwell it collects more than the rest of the house and shows it more, since the light comes straight through.",
      "Most of it we reach with a water fed pole from the ground or from inside. Some of it needs a ladder. A few are genuinely not safely reachable, and we will tell you that instead of having a go."],
    includes_title="What we can reach",
    includes=[
      "<strong>Skylights</strong> from inside by pole, and from outside where the roof pitch allows it safely.",
      "<strong>Vaulted and gable glass</strong>, the triangular panes above a front entry or a great room.",
      "<strong>Stairwell windows</strong>, usually the single most noticeable window in a house.",
      "<strong>Second and third storey exteriors</strong> by ladder or water fed pole.",
      "<strong>Atrium and transom glass</strong> in commercial entries."],
    extras_title="Usually booked with",
    extras=[
      "The rest of the house exteriors, same visit",
      "Interior high glass while the pole is up",
      "Light fittings and fans at the same height, if they are in reach",
      "Screens on high windows, which rarely get done otherwise"],
    good=[
      "Pure water through a pole dries spotless, which is why it works at height where you cannot squeegee.",
      "Roof pitch and what is underneath decides whether a skylight gets done from above or below.",
      "We will turn down anything that needs rope access or a swing stage.",
      "Tell us about high glass when you ask for a price. It changes the kit we bring."],
    faq=[
      ("How high do you go?", "About three storeys. Beyond that it is rope access work and we do not do it."),
      ("Do you walk on the roof?", "Only where it is a safe pitch and there is a sensible way up. Otherwise it is done by pole from below."),
      ("Why does pure water not leave spots?", "The minerals are filtered out, so when it dries there is nothing left behind to dry into a spot. That is the whole trick."),
      ("Can you do the inside of a skylight?", "Usually, by pole from the floor. Very high vaulted ones sometimes cannot be reached safely, and we will say so.")],
    strip=["skylight", "ladder-upper", "pole-on-home", "water-fed"],
    related=["residential-window-cleaning-edmonton", "commercial-window-cleaning-edmonton",
             "interior-window-cleaning-edmonton"]),

"post-construction-window-cleaning": dict(
    h1="Post-Build", glow="GLASS",
    sub="Stucco splatter, labels, tape residue and a track full of drywall grit. The clean that makes finished work look finished.",
    intro=[
      "Builders' glass is a different job from a normal clean and gets priced that way. Nothing on it is dirt. It is stucco spots, paint flecks, silicone smears, the glue from the manufacturer's label and a fine mineral haze from concrete dust that has been rained on.",
      "It also has to be done carefully. New glass scratches, and half of what is on it has to come off with a blade. Done wrong you hand the client a house with hairline scratches across every pane, which is a far more expensive problem than a dirty window."],
    includes_title="What the job involves",
    includes=[
      "<strong>Labels and stickers</strong> off, with the adhesive residue after them.",
      "<strong>Stucco, paint and silicone</strong> removed, soaked first and taken off wet so the glass is not scratched.",
      "<strong>Concrete haze</strong>, which needs a mineral treatment rather than soap.",
      "<strong>Tracks and sills</strong> cleared of drywall dust and grit, vacuumed before anything wet.",
      "<strong>Frames wiped</strong>, including the gap where the trim meets the unit.",
      "<strong>Full wash and squeegee</strong> after all of that, which is where the job finally looks like a window clean."],
    extras_title="Often needed too",
    extras=[
      "Screens, which arrive dusty and usually still wrapped",
      "Skylights, normally the worst panes on a new build",
      "A second visit after the landscapers finish",
      "Interior glass partitions on a commercial fitout"],
    good=[
      "Book after the trades are finished. Cleaning between them means paying twice.",
      "Tempered glass scratches more easily than people think. Anyone scraping it dry is doing damage.",
      "If the stucco crew has not been yet, wait. That is the messiest stage for glass.",
      "Tell us it is a new build when you ask for a price, because it is slower work than a normal clean."],
    faq=[
      ("Why does this cost more than a regular clean?", "Because most of the time goes on taking things off the glass rather than washing it. A builders' clean can take three times as long as the same house would the following year."),
      ("Will scraping scratch the glass?", "Not if it is soaked first and the blade is new and kept wet. Dry scraping is what causes scratches, and on tempered glass it is unforgiving."),
      ("When should we book it?", "After the last trade and after the stucco. Ideally after landscaping too, or the sprinklers will spot it all over again."),
      ("Can you do it in stages?", "Yes, and on bigger builds that is normal. One pass at lock-up and a final one before handover.")],
    strip=["frame-detail", "cloth-polish", "track-detail", "supplies"],
    related=["commercial-window-cleaning-edmonton", "window-screens-tracks-edmonton",
             "skylight-cleaning-edmonton"]),
}


def build_service(svc):
    new_page()
    c = COPY[svc["slug"]]
    short_plain = strip(svc["short"]).lower()
    trail = [("Services", "services.html"), (strip(svc["short"]), svc["slug"] + ".html")]
    related = [BY_SLUG[r] for r in c["related"]]

    body = """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
{INTRO}
          <figure class="media-figure">
            {FIG}
            <figcaption>{CAPTION}</figcaption>
          </figure>

          <h2>{INCTITLE}</h2>
          <ul>{INCLUDES}</ul>

          <h2>{EXTITLE}</h2>
          <ul>{EXTRAS}</ul>

          <h2>Before you book</h2>
          <ul>{GOOD}</ul>

          <h2>On the job</h2>
          {STRIP}

          <h2>Questions about {SHORT}</h2>
          {FAQ}

          <h2>Usually booked with this</h2>
          <div class="grid grid-3" style="margin-top:1rem;">
{RELATED}
          </div>
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(
        INTRO="\n".join("          <p>%s</p>" % p for p in c["intro"]),
        FIG=img_tag(pick(svc["thumb"]), 0),
        CAPTION="%s across %s." % (strip(svc["short"]), strip(AREA)),
        INCTITLE=c["includes_title"],
        INCLUDES="".join("<li>%s</li>" % x for x in c["includes"]),
        EXTITLE=c["extras_title"],
        EXTRAS="".join("<li>%s</li>" % x for x in c["extras"]),
        GOOD="".join("<li>%s</li>" % x for x in c["good"]),
        STRIP=photo_strip(0, c["strip"]),
        SHORT=short_plain,
        FAQ=faq_block(c["faq"]),
        RELATED=service_tiles(0, related),
        SIDEBAR=sidebar(0, photo_cap=strip(svc["short"])),
        CTA=cta_strip(0), FOOT=footer(0))

    html = head(
        title=strip(svc["title"]) + " | " + NAME_FULL,
        desc=strip(c["sub"])[:300],
        canonical="%s/%s.html" % (BASE, svc["slug"]),
        og_image="images/%s.jpg" % svc["img"],
        extra_ld=ld_service(svc) + ld_breadcrumb(trail) + ld_faq(c["faq"]),
    ) + hero_small(
        0, trail, c["h1"], c["glow"], c["sub"], media=svc["img"],
    ) + body
    BUILT.append(write(svc["slug"] + ".html", html))


for s in SERVICES:
    build_service(s)


# ----------------------------------------------------------------------
# Service area pages
# ----------------------------------------------------------------------
AREA_COPY = {
    "Edmonton": [
        "Edmonton gives glass a hard time for a city that looks clean. The river valley throws dust at everything on the south-facing slopes, the spring thaw puts a season of road grit on anything near a main road, and half the houses in the newer neighbourhoods have sprinklers pointed straight at the windows.",
        "Older parts of the city bring their own problem, which is sash windows and storm windows that have not been out of their frames in decades. Newer builds out in Windermere and the Hamptons are mostly big sealed units, easier glass but a lot more of it and usually higher."],
    "St. Albert": [
        "A lot of mature trees in St. Albert, which means a lot of poplar fluff in June and a lot of leaf litter in the tracks by October. The older streets around Sir Winston Churchill have houses with more, smaller panes than the newer builds out in Erin Ridge.",
        "Sprinkler spotting is common here too. Big lawns, long arcs, and glass that catches the overspray on the south side."],
    "Sherwood Park": [
        "Mostly newer housing stock, which means big sealed units, two and three storey elevations and a fair number of vaulted gable windows above the front entry. Those are the ones that never get done.",
        "The Baseline businesses are a different job again, mostly frontage on a busy road, which gets dirty fast and benefits from a standing round rather than a once-a-year clean."],
    "Spruce Grove": [
        "Spruce Grove and Stony Plain sit out where the wind picks up field dust, and it shows on west elevations. Exteriors here usually want doing twice rather than once.",
        "Plenty of acreages on the way out too. Those are bigger jobs with more glass and often a long gravel drive, which we factor in rather than surprise you with."],
    "Leduc": [
        "Leduc has newer subdivisions with a lot of glass and the airport corridor businesses, which are two quite different kinds of work. Southfork and Bridgeport are mostly two storey with big front windows.",
        "The commercial side out toward the airport tends to want quarterly rounds done early, before staff arrive."],
    "Beaumont": [
        "Beaumont is a drive but an easy one, and the newer streets have the same big-window, two storey builds as Sherwood Park. Gable glass above the entry is common and almost never cleaned.",
        "The shops along 50th are on a busy enough road to want frontage done regularly rather than seasonally."],
}


def build_location(loc):
    new_page()
    area = loc["area"]
    trail = [(area, loc["slug"] + ".html")]
    faq = [
        ("Is there a travel charge for %s?" % area,
         "No. %s is part of the normal run, so it is in the price rather than on top of it." % area),
        ("How soon can you come out?",
         "Usually the same week. Spring is the exception, when everyone books at once and it can run to two or three weeks. Autumn interiors are easier."),
        ("Can you work when nobody is home?",
         "For exteriors, yes, as long as we can get to the back. Leave the gate unlocked or send the code. Interiors need someone to let us in."),
        ("Do you do businesses in %s as well as houses?" % area,
         "Both. Storefronts tend to go on a weekly or biweekly round, offices quarterly."),
    ]
    tiles_src = [BY_SLUG[s] for s in (
        "residential-window-cleaning-edmonton", "interior-window-cleaning-edmonton",
        "window-screens-tracks-edmonton", "storefront-window-cleaning-edmonton",
        "hard-water-stain-removal-edmonton", "skylight-cleaning-edmonton")]
    others = "".join(
        '<li><a href="%s.html">%s</a></li>' % (l["slug"], l["area"])
        for l in LOCATIONS if l["slug"] != loc["slug"])
    local = "\n".join("          <p>%s</p>" % p for p in AREA_COPY[area])

    html = head(
        title="Window Cleaning in %s | %s" % (area, NAME_FULL),
        desc=("Window cleaning in %s by R&F Enterprise. Houses, storefronts and offices, inside "
              "and out, screens and tracks. Text a photo for a price." % area),
        canonical="%s/%s.html" % (BASE, loc["slug"]),
        og_image="images/%s.jpg" % loc["img"],
        extra_ld=ld_breadcrumb(trail) + ld_faq(faq),
    )
    tiles = service_tiles(0, tiles_src)
    html += hero_small(
        0, trail, "Window Cleaning in", area.upper(),
        "%s %s" % (loc["note"], "Houses, storefronts and offices, priced off a photo."),
        media=loc["img"],
    ) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <h2>Working in {AREA}</h2>
{LOCAL}

          <figure class="media-figure">
            {FIG}
            <figcaption>{AREA} and the streets around it. Exteriors from thaw to freeze-up, interiors all year.</figcaption>
          </figure>

          <h2>What gets booked here</h2>
          <div class="grid grid-3" style="margin-top:1rem;">
{TILES}
          </div>

          <h2>Getting a price in {AREA}</h2>
          <p>Photo of the front, photo of the back, and say whether you want insides doing. If the back gate is locked or there is a dog, mention it, because that changes the day more than the glass does.</p>

          <h2>Questions from {AREA}</h2>
          {FAQ}

          <h2>Other places we go</h2>
          <ul>{OTHERS}</ul>
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(AREA=area, LOCAL=local,
                      FIG=img_tag(pick("modern-home", "two-storey", "bay-window"), 0),
                      TILES=tiles, FAQ=faq_block(faq), OTHERS=others,
                      SIDEBAR=sidebar(0, photo_cap="Booked across " + area),
                      CTA=cta_strip(0), FOOT=footer(0))
    BUILT.append(write(loc["slug"] + ".html", html))


for l in LOCATIONS:
    build_location(l)

if __name__ == "__main__":
    for p in BUILT:
        print("built", p)
