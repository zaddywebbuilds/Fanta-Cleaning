# -*- coding: utf-8 -*-
"""Builds the notes index and every article."""

from common import (NAME, NAME_FULL, PHONE, PHONE_TEL, AREA, BASE, SERVICES, BY_SLUG,
                    SMS_QUOTE, head, ld_breadcrumb, ld_faq, hero_small, photo_strip,
                    cta_strip, footer, sidebar, faq_block, write, strip,
                    new_page, pick, img_tag)

BUILT = []
D = 1  # every article lives in /blog/

POSTS = [
dict(slug="how-often-to-clean-windows-edmonton",
     title="How Often Should Windows Get Cleaned in Edmonton?",
     date="2026-09-12", pretty="12 September 2026", read="4 min",
     img="two-storey",
     teaser="Twice a year for most houses, and the spring one is always the bigger job. Here is why.",
     service="residential-window-cleaning-edmonton",
     body=[
      ("", ["The short answer is twice. Outsides in late spring once the sprinklers have been running a few weeks, then the full lot in September before the windows get shut for the winter.",
            "The longer answer depends on what is pointed at your glass."]),
      ("Spring is the big one", [
       "Winter leaves a specific mess. Road grit gets thrown up by traffic and sticks to anything facing a street. Salt spray does the same at ground level, and it leaves a film that dries milky rather than gritty. Then the thaw comes and runs all of it down the glass in streaks.",
       "On top of that, nothing has been washed off since October. Six months of it is sitting there bonded on. A spring exterior clean is always slower than the autumn one, and it is the visit most worth paying for."]),
      ("Autumn is about the insides", [
       "By September the outsides are still reasonable if they were done in spring. What has changed is the inside, where a summer of open windows has let dust settle on the frames and tracks.",
       "Doing both faces in one visit in late September is the most efficient booking of the year. It is warm enough for exteriors and you go into winter with the glass clear, which matters more than people expect once the sun drops low in January and comes straight through at eye level."]),
      ("Where twice is not enough", [
       "Houses on a main road or a gravel lane need three. So do acreages west of the city, where field dust on a windy week undoes a clean in days.",
       "Anything with a sprinkler hitting it needs more attention than frequency will fix. That is a mineral problem and no amount of washing prevents it. Move the head."]),
      ("Shops are a different calculation entirely", [
       "Frontage is weekly or biweekly, year round, because it is hand height on a public sidewalk. Winter is the busy season for it, not summer. Salt and slush from the road do more in a week in February than dust does all August."]),
     ]),

dict(slug="sprinkler-spots-on-windows",
     title="Your Sprinklers Are Wrecking Your Windows",
     date="2026-09-20", pretty="20 September 2026", read="3 min",
     img="brush-closeup",
     teaser="Those white rings are mineral, not dirt, and the fix is not a better window cleaner.",
     service="hard-water-stain-removal-edmonton",
     body=[
      ("", ["Every June we get the same call. The windows were cleaned three weeks ago and there are white rings all over the south side of the house.",
            "Nobody did a bad job. The sprinklers are hitting the glass.",
            "Edmonton water is hard. When a sprinkler sprays a hot pane in the afternoon, the water evaporates in minutes and leaves behind the minerals it was carrying. Do that twice a day, every day, through July, and the deposit builds into a visible crust that soap will not touch. It is sitting on top of the glass, not in the dirt layer, so a normal wash goes straight past it."]),
      ("It gets worse the longer it sits", [
       "Fresh spotting, a season or less, comes off cleanly with an acidic treatment and some dwell time. Two or three seasons and it will lighten but probably not disappear. Beyond that the mineral starts to etch into the surface of the glass itself, and at that point it is damage rather than dirt. Nothing cleans it off, because there is nothing left on top to remove.",
       "This is the main reason we ask people to mention sprinkler spotting when they book rather than on the day. It is a treatment with its own time and its own price, and on a bad elevation it can take as long as cleaning the whole rest of the house."]),
      ("The actual fix costs nothing", [
       "Go out while the sprinklers are running and watch where the water lands. If it is hitting glass, change the arc or move the head. That is the entire solution and it takes ten minutes.",
       "We would rather tell you that than sell you a mineral treatment every summer for the next decade."]),
     ]),

dict(slug="why-windows-streak",
     title="Why Windows Streak",
     date="2026-09-28", pretty="28 September 2026", read="4 min",
     img="squeegee-soapy",
     teaser="Four causes, and only one of them is the cleaner being careless.",
     service="residential-window-cleaning-edmonton",
     body=[
      ("", ["A streaky window is annoying in a way a dirty one is not, because somebody just worked on it. Usually it comes down to one of four things."]),
      ("The glass dried before it was finished", [
       "Direct sun on a warm day will dry soap on glass faster than anyone can squeegee it off. Once it dries you are no longer moving water, you are smearing a film, and the harder you work the worse it looks.",
       "The fix is working the shaded side of a building first and coming back round. On a hot July afternoon there are elevations that simply should not be attempted until the sun moves."]),
      ("The rubber has gone", [
       "A squeegee blade is a consumable. A fresh one is square-edged and pulls water cleanly. A worn one is rounded and skips, leaving a thin line behind every pass. It happens gradually enough that someone using it all day can stop noticing.",
       "Blades get turned and changed through the day. It is the single most common cause of a streak on an otherwise competent job."]),
      ("The edges were never dried", [
       "Most streaking is not in the middle of the pane at all. It is a half inch around the perimeter where water sat in the frame and ran back down after the squeegee went past.",
       "Drying the perimeter by hand after the squeegee work is what separates a window that looks clean from one that looks clean from an angle too. It is also the step that gets skipped when someone is rushing."]),
      ("It is not actually a streak", [
       "Sometimes the marks are between the panes, not on them, which means the seal on the sealed unit has failed and moisture is getting in. Cleaning will never touch it. Sometimes it is a scratch catching the light. Occasionally it is mineral etching.",
       "A decent cleaner tells you which of these you are looking at before taking money for it. If the marks are in the same place after two cleans, that is what is going on."]),
      ("How to check properly", [
       "Look at the glass from an angle, not straight on, with light coming across it. Straight on in flat light, almost any window looks fine. From the side in low sun, everything shows. That is how we check our own work, and it is why the last five minutes of a job are spent walking round looking at windows sideways."]),
     ]),

dict(slug="the-track-is-the-bit-that-matters",
     title="The Track Is the Bit That Matters",
     date="2026-10-04", pretty="4 October 2026", read="2 min",
     img="track-detail",
     teaser="Clean glass sitting in a dirty track does not stay clean. A short argument for doing the boring part.",
     service="window-screens-tracks-edmonton",
     body=[
      ("", ["Here is the thing nobody wants to pay for.",
            "You can clean a pane perfectly. Genuinely, properly, no streaks, dried edges, the lot. If the track underneath it is full of grit, the first decent rain washes that grit up the inside of the glass and you have dirty streaks running down a window that was spotless yesterday.",
            "Tracks hold everything. Road dust, poplar fluff, dead flies, sand from the winter, and in older houses a surprising amount of paint grit. All of it sits in a channel at the bottom of the window waiting for water."]),
      ("Dry first. Always.", [
       "The mistake, and it is a common one, is spraying the track and wiping it. What that does is turn dry grit into wet paste, push it into the corners, and leave a grey tide line that dries hard.",
       "It has to come out dry. Vacuum, with a crevice tool, corners included. Then and only then does anything wet go near it. Takes an extra minute per window and it is the difference between a clean that holds for months and one that looks tired in a fortnight."]),
      ("While you are in there", [
       "Check the weep holes, the small slots at the front of the track that let water drain out. Blocked, they let the track hold water, which is how you end up with mould in the corners and a sill that rots from underneath.",
       "Two seconds with a brush. Nobody ever does it."]),
     ]),

dict(slug="when-its-too-cold-to-clean-windows",
     title="When It Is Too Cold to Clean Windows Outside",
     date="2026-10-11", pretty="11 October 2026", read="3 min",
     img="ladder-upper",
     teaser="Roughly freezing, give or take, and here is what actually goes wrong below it.",
     service="interior-window-cleaning-edmonton",
     body=[
      ("", ["People assume exterior window cleaning stops in winter because it is unpleasant. It is unpleasant, but that is not the reason."]),
      ("Water freezes faster than you can squeegee it", [
       "Below freezing, a film of water on glass starts to ice over within seconds of going on. You cannot pull it off with a squeegee because it is no longer liquid, and what you get instead is a thin layer of ice that dries to a white haze when it eventually sublimates. The window ends up worse than when you started.",
       "There are cold weather additives that drop the freezing point, and we use them on storefronts through the winter because frontage cannot just stop for five months. They buy you a working range down to around minus ten on a sunny morning. Below that it stops being viable."]),
      ("Rubber goes hard", [
       "Squeegee rubber stiffens in the cold. A stiff blade does not conform to the glass, so it skips, and you get the line-per-pass problem that no amount of care fixes. Blades get swapped far more often in October than in July for exactly this reason."]),
      ("Ladders and ice", [
       "The honest one. Setting a ladder on frozen ground, on a surface that might have a skim of ice under the snow, at height, is not a risk worth taking for a window. We stop exterior ladder work well before we stop pole work."]),
      ("So what is the season", [
       "Exteriors run from the thaw, usually some time in April, through to the first sustained hard frost, usually late October. Some years we get into November. Some years a cold snap ends it in the third week of October.",
       "Interiors run all year, which is why the winter half of our work is almost entirely inside. If you want both done in one visit, book late September and you will comfortably get it."]),
     ]),

dict(slug="what-window-cleaning-wont-fix",
     title="What Window Cleaning Will Not Fix",
     date="2026-10-18", pretty="18 October 2026", read="3 min",
     img="before-after",
     teaser="Four things that look like dirt, are not dirt, and will still be there afterwards.",
     service="hard-water-stain-removal-edmonton",
     body=[
      ("", ["Worth knowing before you pay someone, because a cleaner who does not mention these is either not looking or hoping you will not notice until they have gone."]),
      ("Fog between the panes", [
       "If the haze is inside the sealed unit, the seal has failed and moist air is getting in. There is no access to that surface without breaking the unit apart. Cleaning does nothing. The window needs the glass unit replaced, which is a glazier's job, not ours.",
       "You can usually tell because it does not change at all when the glass is wiped, and it often looks worse on a cold morning."]),
      ("Scratches", [
       "Usually from someone dry-scraping a pane, sometimes from a builder, occasionally from a dog. They catch the light and read as dirt until you run a fingernail over them. Polishing them out is specialist work and costs more than it is worth on most domestic windows."]),
      ("Etched glass", [
       "Long-standing mineral deposits eat into the surface. Once that has happened the damage is in the glass rather than on it. Treatment will lift whatever is still sitting on top and the ghost of the spotting stays. We check for this before quoting hard water work, because the difference matters and it is not always obvious until the first pane is done."]),
      ("Perished screens", [
       "Mesh goes brittle in the sun and frames warp. A screen can be perfectly clean and still look grey because the mesh itself has degraded. Washing it will not bring it back, and an old one sometimes tears just coming out of the frame. We show people rather than quietly refitting a torn screen."]),
      ("", ["None of this is a reason not to get the windows done. It is a reason to want someone who says so up front rather than at the end."]),
     ]),

dict(slug="builders-clean-what-it-involves",
     title="What a Builders' Clean Actually Involves",
     date="2026-10-24", pretty="24 October 2026", read="4 min",
     img="frame-detail",
     teaser="Why new-build glass costs three times a normal clean, and why dry-scraping it is a disaster.",
     service="post-construction-window-cleaning",
     body=[
      ("", ["A post-construction window clean is barely the same trade as a regular one. Almost none of what is on the glass is dirt, and almost none of it comes off with soap."]),
      ("What is actually on a new window", [
       "<strong>Manufacturer labels</strong> and the adhesive under them, which has usually been baked on by a summer behind glass.",
       "<strong>Stucco and parging splatter</strong>, which dries like cement and is the single worst thing on the list.",
       "<strong>Paint flecks and primer overspray.</strong>",
       "<strong>Silicone smears</strong> from the sealing crew, which smear further if you attack them wrong.",
       "<strong>Concrete haze</strong>, a fine mineral film left when concrete dust gets rained on. Looks like the glass is frosted.",
       "<strong>Drywall grit</strong> packed into every track."]),
      ("The part that goes wrong", [
       "All of that has to come off with a blade. The mistake, and it is a costly one, is scraping dry.",
       "Dry glass plus a blade plus a hard fleck of stucco equals a scratch, and on tempered glass it is unforgiving, because fabricating debris sitting in the surface gets dragged across it. You can scratch an entire elevation in about ten minutes. Replacing a wall of tempered units costs many times what the clean did.",
       "Done properly, every pane is soaked first, the blade is new and kept wet, and it is worked in one direction. Slower, and the only way that does not end in a conversation with the builder's insurer."]),
      ("Sequencing it", [
       "Book after the last trade. Not between them, or you pay twice and the second clean is nearly as bad as the first.",
       "The stucco crew is the one that matters most. If they have not been yet, wait. And if landscaping is still to come, expect the sprinklers to spot everything once they are commissioned, so a short touch-up afterwards is normal on bigger builds.",
       "On larger projects we do it in two passes, one at lock-up when the worst comes off and a final one before handover."]),
      ("What it costs", [
       "More than you expect, and roughly three times what the same house will cost the following year on a normal clean. The money is in removal time, not washing time. The washing part at the end is the quick bit."]),
     ]),

dict(slug="windows-before-listing-photos",
     title="Get the Windows Done Before the Listing Photos",
     date="2026-10-30", pretty="30 October 2026", read="2 min",
     img="sunlit-living-room",
     teaser="A cheap job that changes every interior shot in the set. Realtors work this out quickly.",
     service="residential-window-cleaning-edmonton",
     body=[
      ("", ["Photographers shoot interiors toward the windows, because that is where the light is. Which means every wide shot of a room has a window in it, usually blown out slightly and usually in focus at the edges.",
            "Dirty glass shows in those shots more than it does in person. Spotting reads as noise, the film across the pane kills the contrast of whatever is outside, and the room looks dimmer than it is."]),
      ("The maths is not complicated", [
       "A window clean on an average house costs a fraction of one price reduction. It takes half a day. And unlike staging or paint it affects every photo in the set at once, including the exterior shots, where clean glass reflects sky instead of looking grey.",
       "If the listing is going up in spring, it is doing double duty anyway, because the house needs the post-winter clean regardless."]),
      ("Timing", [
       "Book it two or three days before the shoot, not the morning of. That leaves room to come back if a pane needs a second look, and it means nobody is working round a photographer.",
       "Say it is for listing photos when you book. It changes which windows get the most attention, and we will prioritise whatever the camera will be pointed at."]),
     ]),
]


def article(p):
    new_page()
    svc = BY_SLUG[p["service"]]
    trail = [("Notes", "blog/index.html"), (p["title"], "blog/%s.html" % p["slug"])]
    sections = []
    for heading, paras in p["body"]:
        if heading:
            sections.append("          <h2>%s</h2>" % heading)
        run = []
        for para in paras:
            if para.startswith("<strong>"):
                run.append(para)
                continue
            if run:
                sections.append("          <ul>%s</ul>" % "".join("<li>%s</li>" % b for b in run))
                run = []
            sections.append("          <p>%s</p>" % para)
        if run:
            sections.append("          <ul>%s</ul>" % "".join("<li>%s</li>" % b for b in run))

    ld_article = """  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BlogPosting","headline":"{T}",
    "datePublished":"{D}","dateModified":"{D}",
    "image":"{B}/images/{IMG}.jpg",
    "author":{{"@type":"Organization","name":"{N}"}},
    "publisher":{{"@type":"Organization","name":"{N}","logo":{{"@type":"ImageObject","url":"{B}/images/logo.svg"}}}},
    "mainEntityOfPage":"{B}/blog/{S}.html"}}
  </script>
""".format(T=strip(p["title"]), D=p["date"], B=BASE, IMG=p["img"],
           N=strip(NAME_FULL), S=p["slug"])

    others = [q for q in POSTS if q["slug"] != p["slug"]][:3]
    more = "".join(
        '<article class="service-tile"><div class="service-tile-media">%s</div>'
        '<div class="service-tile-body"><h3>%s</h3><p>%s</p>'
        '<div class="row"><a href="%s.html">Read &rarr;</a></div></div></article>'
        % (img_tag(pick(q["img"]), D), q["title"], q["teaser"], q["slug"])
        for q in others)

    html = head(
        title=strip(p["title"]) + " | " + NAME_FULL,
        desc=strip(p["teaser"]),
        canonical="%s/blog/%s.html" % (BASE, p["slug"]),
        depth=D, og_type="article", og_image="images/%s.jpg" % p["img"],
        extra_ld=ld_article + ld_breadcrumb(trail),
    ) + hero_small(
        D, trail, p["title"], "", p["teaser"], media=p["img"],
    ) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <p class="note-pill">{PRETTY} &middot; {READ} read</p>
{BODY}

          <figure class="media-figure">
            {SFIG}
            <figcaption>{SSHORT} across {AREA}. Text a photo and we will price it.</figcaption>
          </figure>

          <div class="btn-row" style="margin:1.4rem 0;">
            <a class="btn btn-text" href="{SMS}">Text a photo</a>
            <a class="btn btn-gold" href="../{SSLUG}.html">{SSHORT}</a>
            <a class="btn btn-glass" href="tel:{TEL}">Call {PHONE}</a>
          </div>

          <h2>More notes</h2>
          <div class="grid grid-3" style="margin-top:1rem;">{MORE}</div>
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(PRETTY=p["pretty"], READ=p["read"], BODY="\n".join(sections),
                      SFIG=img_tag(pick(svc["thumb"], svc["img"]), D),
                      SSHORT=strip(svc["short"]),
                      SSLUG=svc["slug"], AREA=strip(AREA), SMS=SMS_QUOTE, TEL=PHONE_TEL,
                      PHONE=PHONE, MORE=more,
                      SIDEBAR=sidebar(D, photo_cap=strip(svc["short"])),
                      CTA=cta_strip(D), FOOT=footer(D))
    BUILT.append(write("blog/%s.html" % p["slug"], html))


for post in POSTS:
    article(post)


# ----------------------------------------------------------------------
# Notes index
# ----------------------------------------------------------------------
new_page()

cards = "".join(
    '<article class="service-tile"><div class="service-tile-media">%s</div>'
    '<div class="service-tile-body"><h3>%s</h3><p>%s</p>'
    '<div class="row"><a href="%s.html">Read &rarr;</a><span style="font-size:.78rem;color:var(--c-ink-soft)">%s</span></div>'
    '</div></article>' % (img_tag(pick(p["img"]), D), p["title"], p["teaser"],
                          p["slug"], p["read"])
    for p in reversed(POSTS))

index = head(
    title="Notes | " + NAME_FULL,
    desc=("Short pieces on window cleaning in Edmonton: how often, sprinkler spotting, streaks, "
          "winter limits and what a builders' clean involves."),
    canonical=BASE + "/blog/index.html", depth=D,
    extra_ld=ld_breadcrumb([("Notes", "blog/index.html")]),
) + hero_small(
    D, [("Notes", "blog/index.html")],
    "Notes", "",
    "Things we end up explaining on the doorstep often enough to be worth writing down.",
    media="office-view",
) + """
  <section class="section">
    <div class="container">
      <div class="grid grid-4">{CARDS}</div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">The work</span>
        <h2>Around a window</h2>
      </div>
      {STRIP}
    </div>
  </section>

{CTA}{FOOT}""".format(CARDS=cards,
                      STRIP=photo_strip(D, ["cloth-polish", "screen-brush",
                                            "sill-wipe", "supplies"]),
                      CTA=cta_strip(D), FOOT=footer(D))

BUILT.append(write("blog/index.html", index))

if __name__ == "__main__":
    for b in BUILT:
        print("built", b)
