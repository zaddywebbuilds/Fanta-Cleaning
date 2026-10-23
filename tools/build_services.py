# -*- coding: utf-8 -*-
"""Builds the ten service pages and the six service-area pages."""

from common import (NAME, PHONE, PHONE_TEL, AREA, BASE, MAPS, SVG, SERVICES, BY_SLUG,
                    LOCATIONS, wa, head, ld_service, ld_faq, ld_breadcrumb, hero_small,
                    photo_strip, service_tiles, cta_strip, footer, sidebar, faq_block,
                    write, strip)

BUILT = []

# ----------------------------------------------------------------------
# Per-service copy
# ----------------------------------------------------------------------
COPY = {
"house-cleaning-etobicoke": dict(
    h1="House Cleaning", glow="IN ETOBICOKE",
    sub="Weekly, every other week or monthly. The same rooms, the same standard, the same crew, so the house never drifts back to square one.",
    intro=[
      "A recurring clean is a different animal from a one off. The point is not a dramatic transformation every visit, it is that the house never gets far enough from clean to need one. Each visit is shorter, cheaper and more thorough than a rescue mission would be.",
      "We work room by room in the same order every time, which is how nothing gets skipped on a busy day. You tell us once which rooms matter most and which to leave alone, and that sticks."],
    includes_title="What a standard visit covers",
    includes=[
      "<strong>Kitchen.</strong> Counters, backsplash, sink and taps, cabinet fronts, exterior of appliances, cooktop, microwave inside and out, floor.",
      "<strong>Bathrooms.</strong> Shower and tub scrubbed, glass cleared of soap film, toilet inside and out, sink, mirror, fixtures polished, floor.",
      "<strong>Bedrooms and living areas.</strong> Dusting including sills, ledges and skirting, mirrors and glass, vacuum throughout, mop hard floors, beds made if sheets are left out.",
      "<strong>Everywhere.</strong> Light switches, door handles, bannisters, bins emptied and relined, a final walk to catch anything missed."],
    extras_title="Add on when you need it",
    extras=[
      "Inside the oven and inside the fridge",
      "Inside cupboards and drawers, emptied first",
      "Interior windows and balcony glass",
      "Laundry folded, or beds stripped and remade",
      "Carpet extraction on the high traffic rooms"],
    good=[
      "Pets are fine. Tell us names and whether they are nervous, and we will work around them.",
      "Products come with us. If you prefer your own, leave them out and leave a note.",
      "You do not need to be home. Most recurring clients leave a key or a code.",
      "First visit usually takes longer than the ones after it, and is priced accordingly."],
    faq=[
      ("How often should I book?", "Most households land on every two weeks. Weekly suits busy family homes and anyone with pets or allergies. Monthly works if you keep on top of things yourself and want the deeper jobs handled."),
      ("Will it be the same cleaners each time?", "Wherever scheduling allows, yes. Familiarity is most of what makes a recurring clean good: they know your floors, your products and which cupboard the bin bags live in."),
      ("What if I need to skip a week?", "Just tell us. There is no penalty for skipping, though if the gap gets long the next visit may take extra time."),
      ("Do you clean inside the oven every visit?", "Not as standard, because it adds real time. Add it when you want it, or set it on a rotation, for instance every third visit.")],
    strip=[("images/kitchen-detail.jpg", "Kitchen counters cleaned", "Kitchens"),
           ("images/bathroom-detail.jpg", "Bathroom taps and sink detailed", "Bathrooms"),
           ("images/wood-floor.jpg", "Floor care in a living room", "Floors"),
           ("images/childrens-room.jpg", "Bedroom dusted and tidied", "Bedrooms")],
    related=["deep-cleaning-etobicoke", "recurring-cleaning-etobicoke", "kitchen-bathroom-cleaning"]),

"deep-cleaning-etobicoke": dict(
    h1="Deep Cleaning", glow="IN ETOBICOKE",
    sub="The reset. Inside appliances, behind furniture, grout, vents, frames and all the places a weekly clean never gets to.",
    intro=[
      "A deep clean is what you book when the normal clean stopped being enough. Grease that has gone sticky, grout that has gone grey, dust on the tops of door frames, a fridge nobody has emptied in a year. It takes a crew most of a day on an average home, and it is the one job where the difference is obvious from the doorway.",
      "People usually book it for one of four reasons: spring, a new baby, guests arriving, or taking over a home from someone else. All four need the same thing, which is for everything to be genuinely clean at the same time, once."],
    includes_title="What a deep clean covers",
    includes=[
      "<strong>Kitchen, properly.</strong> Inside the oven, inside the fridge, inside the microwave, range hood and filter, backsplash degreased, cabinet fronts and tops, under and behind what can be moved.",
      "<strong>Bathrooms, properly.</strong> Grout scrubbed, limescale off glass and taps, shower head descaled, extractor vent, behind the toilet, tile floor edges.",
      "<strong>Dust at every height.</strong> Door frames, picture rails, light fittings, ceiling fan blades, vents and registers, blinds, radiators, baseboards.",
      "<strong>Floors and edges.</strong> Furniture moved where safe, carpets vacuumed underneath, hard floors mopped to the edges rather than the middle.",
      "<strong>Glass and fittings.</strong> Interior windows, mirrors, switch plates, handles, bannisters and skirting wiped by hand."],
    extras_title="Common add ons",
    extras=[
      "Inside all cupboards and wardrobes",
      "Carpet and upholstery extraction",
      "Balcony or patio swept and wiped down",
      "Wall spot cleaning and scuff removal",
      "Interior window and track detail"],
    good=[
      "Allow most of a day. A thorough deep clean on a three bedroom home is not a two hour job.",
      "Clearing surfaces beforehand gets you more cleaning for the same money.",
      "Some marks are damage, not dirt. We will tell you which is which rather than scrub a finish off.",
      "After a deep clean, a recurring visit holds the standard for a fraction of the cost."],
    faq=[
      ("How is this different from a regular clean?", "A regular clean maintains. A deep clean resets. The regular clean wipes the front of the oven, the deep clean takes the racks out and does the inside."),
      ("How long does it take?", "Most homes take a crew most of a working day. Larger or heavily soiled homes can take two visits, which we will tell you before booking, not halfway through."),
      ("Can you get grout back to white?", "Usually much closer than it is now. Grout that has been stained for years may not come all the way back, and we would rather say that up front than overpromise."),
      ("Do I need a deep clean before starting a recurring schedule?", "Not always, but if the home has been neglected it is cheaper overall. One deep clean, then maintenance, beats paying rescue prices every visit.")],
    strip=[("images/kitchen-deep-clean.jpg", "Stovetop degreased", "Kitchen"),
           ("images/bathroom-result.jpg", "Shower glass and tile", "Tile and grout"),
           ("images/wood-floor.jpg", "Deep floor care", "Floors"),
           ("images/dining-detail.jpg", "Dining surfaces detailed", "Detail work")],
    related=["house-cleaning-etobicoke", "kitchen-bathroom-cleaning", "carpet-cleaning-etobicoke"]),

"move-out-cleaning-etobicoke": dict(
    h1="Move In &amp; Move Out", glow="CLEANING",
    sub="Empty unit, top to bottom, finished to the standard a walkthrough is judged by. Photos sent when we are done.",
    intro=[
      "An empty home is the hardest kind to clean, because there is nothing left to hide behind. Every mark on a wall, every ring in a cupboard and every corner of a floor is visible, and whoever inspects it will be looking for exactly those things.",
      "We clean move outs for tenants trying to get a deposit back, landlords preparing for the next tenant, and owners handing over keys on a sale. Same work, different person doing the inspecting."],
    includes_title="What is covered",
    includes=[
      "<strong>Kitchen stripped and cleaned.</strong> Inside and behind the oven and fridge where they move, all cupboards inside and out, drawers, counters, sink, backsplash and the floor underneath everything.",
      "<strong>Bathrooms to inspection standard.</strong> Limescale, grout, glass, fittings, vent, behind and around the toilet base.",
      "<strong>Every room.</strong> Closets and shelving inside, skirting, door frames, switch plates, handles, light fittings, vents.",
      "<strong>Floors.</strong> Vacuumed and mopped wall to wall now that the furniture is gone.",
      "<strong>Glass.</strong> Interior panes, sills and tracks, plus balcony glass where there is one.",
      "<strong>Finish.</strong> Photos of each room sent to you when we lock up."],
    extras_title="Often added",
    extras=[
      "Carpet extraction before handover",
      "Wall scuff and mark removal",
      "Inside every cupboard and wardrobe",
      "Balcony swept and glass cleaned",
      "Appliance interiors on a second pass"],
    good=[
      "Book for after the movers, not before. Cleaning a half empty unit means cleaning it twice.",
      "If there is a handover time, tell us. We start early precisely so these deadlines are makeable.",
      "Keys, lockboxes and concierge instructions are all normal for us.",
      "Send photos of the worst room first. That is what sets the time, and therefore the price."],
    faq=[
      ("Will this satisfy a landlord inspection?", "That is the standard we clean to. We also send photos of every room, which settles most disputes before they start."),
      ("Can you clean before the furniture is out?", "We can, but you will get a worse result for the same money. Wherever possible, book us once the home is empty."),
      ("Do you do the carpets too?", "Yes, as an add on with hot water extraction. On a move out it is usually worth doing, because carpets are the first thing an inspection looks at."),
      ("What about a move in clean?", "Same job, opposite direction. Nobody wants to unpack into someone else's dust, and an empty home is the only chance to clean it properly.")],
    strip=[("images/move-out-cleaning.jpg", "Baseboards cleaned in an empty unit", "Empty units"),
           ("images/kitchen-detail.jpg", "Kitchen cleaned inside and out", "Kitchens"),
           ("images/bathroom-result.jpg", "Bathroom to inspection standard", "Bathrooms"),
           ("images/wood-floor.jpg", "Floors cleaned wall to wall", "Floors")],
    related=["deep-cleaning-etobicoke", "carpet-cleaning-etobicoke", "window-cleaning-etobicoke"]),

"condo-cleaning-etobicoke": dict(
    h1="Condo &amp; Apartment", glow="CLEANING",
    sub="Built for smaller footprints. In, around and under everything, without an all day disruption or a crew that does not know building rules.",
    intro=[
      "Condos are not small houses. The cleaning is denser, the storage is tighter, the dust comes off a shared HVAC system, and the balcony glass does more work than any window in a detached home. A crew used to houses tends to clean the middle of a condo and miss the parts that actually make it feel cluttered.",
      "There is also the building itself: elevator bookings, loading bay windows, concierge sign in, visitor parking that runs out at nine. We work around all of it, and we would rather you told us the rules than found out the hard way."],
    includes_title="What a condo visit covers",
    includes=[
      "<strong>Kitchen.</strong> Counters and backsplash, sink and taps, cabinet fronts, appliance exteriors, cooktop, microwave, floor to the toe kick.",
      "<strong>Bathrooms.</strong> Shower, glass, tub, toilet, vanity, mirror, fixtures, extractor vent cover and tile floor.",
      "<strong>Living and sleeping areas.</strong> Full dust including sills and ledges, mirrors and glass, vacuum and mop throughout, beds made if sheets are left out.",
      "<strong>The condo specifics.</strong> Balcony door track, balcony glass from the inside, in suite laundry exterior, vent covers and the entry closet.",
      "<strong>Finish.</strong> Bins emptied and relined, switch plates and handles, a walk through before we leave."],
    extras_title="Add on when you need it",
    extras=[
      "Inside the oven and inside the fridge",
      "Interior windows and balcony glass detail",
      "Carpet or area rug extraction",
      "Inside closets and storage locker",
      "Balcony floor swept and washed down"],
    good=[
      "Book the elevator if your building needs it. We will work to whatever window you get.",
      "Tell us the concierge arrangement up front, including whether we can collect a key.",
      "Smaller does not always mean quicker. A dense one bedroom with pets can outlast a sparse two bedroom.",
      "If the building restricts certain products or wet work, say so and we will plan around it."],
    faq=[
      ("Do you work in buildings with concierge access?", "Routinely. Leave a key at the desk or put us on the visitor list, and tell us the building's rules when you book."),
      ("Can you come while I am at work?", "Yes. Most of our condo work happens in an empty suite. We lock up and message you when it is done."),
      ("Do you clean the balcony?", "The inside face of the glass and the door track come as standard. Sweeping and washing the balcony floor is an add on, and we do not work on exterior heights."),
      ("How long does a one bedroom take?", "Usually a couple of hours for a maintained suite, longer for a first visit or a deep clean. You get the figure before we book.")],
    strip=[("images/living-room.jpg", "Condo living room reset", "Living areas"),
           ("images/bedroom-result.jpg", "Bedroom made up after a clean", "Bedrooms"),
           ("images/window-cleaning.jpg", "Balcony glass cleaned from inside", "Glass"),
           ("images/floor-mopping.jpg", "Hard floors mopped through the suite", "Floors")],
    related=["house-cleaning-etobicoke", "move-out-cleaning-etobicoke", "window-cleaning-etobicoke"]),

"kitchen-bathroom-cleaning": dict(
    h1="Kitchens &amp;", glow="BATHROOMS",
    sub="The two rooms a home is judged on. Taps, tile, grout, glass and every surface in between, taken back to the finish underneath.",
    intro=[
      "Ask anyone what makes a home feel clean and they will describe a kitchen or a bathroom. These are the rooms that collect grease, limescale and soap film, and they are the rooms where the build up is slow enough that nobody notices until a guest does.",
      "Booking just these two is a sensible middle ground between a regular clean and a full deep clean. It costs a fraction of a whole house reset and fixes most of what was bothering you."],
    includes_title="What the kitchen covers",
    includes=[
      "<strong>Cooking area.</strong> Cooktop and grates degreased, range hood and filter, backsplash, the wall behind the stove and the gap either side of it.",
      "<strong>Surfaces and storage.</strong> Counters, sink and taps descaled and polished, cabinet fronts, handles and the tops of upper cabinets.",
      "<strong>Appliances.</strong> Exteriors throughout, microwave inside and out, and the inside of the oven and fridge when you add them.",
      "<strong>Bathroom wet areas.</strong> Shower and tub scrubbed, glass cleared of soap film, grout worked over, shower head descaled, tile floor edges.",
      "<strong>Bathroom fittings.</strong> Toilet inside, outside and behind the base, vanity, mirror, taps polished, extractor vent cover."],
    extras_title="Add on when you need it",
    extras=[
      "Inside the oven and inside the fridge",
      "Inside cupboards and drawers, emptied first",
      "Hard water and limescale treatment on glass",
      "Grout deep scrub across the tiled floor",
      "Dishwasher and washing machine seals"],
    good=[
      "Limescale on glass responds to repeat visits better than one aggressive scrub.",
      "Clear the counters and empty the sink before we arrive and you get more cleaning per hour.",
      "Some grout is permanently stained rather than dirty. We will tell you which before charging for it.",
      "This pairs well with a regular whole home clean on a rotation, every third visit or so."],
    faq=[
      ("Can I book only the kitchen?", "Yes. Plenty of people book one room, usually the kitchen before a holiday or the bathrooms before guests arrive."),
      ("Will the shower glass come clear?", "In most cases yes. Glass that has been left for years can hold a haze that needs a second visit, and we will say so rather than promise it in one."),
      ("Do you clean inside the oven?", "As an add on, and it is the single most common one. It takes real time, which is why it is priced separately rather than hidden in the rate."),
      ("Is this enough before a house viewing?", "For most viewings, these two rooms plus the floors is what makes the difference. If you have time for more, a deep clean is the better option.")],
    strip=[("images/kitchen-deep-clean.jpg", "Stovetop degreased", "Cooking area"),
           ("images/bathroom-detail.jpg", "Faucet and sink detailed", "Fittings"),
           ("images/bathroom-result.jpg", "Clean bathroom with clear glass", "Wet areas"),
           ("images/kitchen-detail.jpg", "Kitchen surfaces after a clean", "Surfaces")],
    related=["deep-cleaning-etobicoke", "house-cleaning-etobicoke", "move-out-cleaning-etobicoke"]),

"office-cleaning-etobicoke": dict(
    h1="Office Cleaning", glow="IN ETOBICOKE",
    sub="Desks, kitchens, washrooms and common areas, cleaned after hours or before you open, on a schedule that does not interrupt anyone.",
    intro=[
      "A small office is a cleaning problem with a timetable attached. The work itself is straightforward, but it has to happen when the room is empty, it has to be the same every visit, and nobody should ever arrive to find yesterday's bins still full.",
      "We clean small offices, clinics, studios and shared suites on fixed schedules. Same crew, same checklist, same slot each week, so it becomes something you stop thinking about."],
    includes_title="What a visit covers",
    includes=[
      "<strong>Desks and workstations.</strong> Surfaces cleared of dust, wiped and disinfected, monitors and screens dusted, keyboards and phones wiped down.",
      "<strong>Touch points.</strong> Door handles, light switches, railings, lift buttons, shared equipment and reception surfaces.",
      "<strong>Kitchen and break area.</strong> Counters, sink, appliance exteriors, microwave inside, table and chairs, bins emptied and relined.",
      "<strong>Washrooms.</strong> Toilets, sinks, mirrors, fittings, floors, and consumables restocked where you supply them.",
      "<strong>Floors and glass.</strong> Vacuum throughout, mop hard floors, interior glass partitions and entry door glass."],
    extras_title="Add on when you need it",
    extras=[
      "Carpet extraction on a quarterly rotation",
      "Interior window and partition detail",
      "Fridge clear out and interior clean",
      "Meeting room reset before a client visit",
      "Post-renovation dust pass after a fit out"],
    good=[
      "Tell us which desks are off limits and they stay untouched.",
      "After hours and early morning are both normal. We pick the slot that suits the office, not us.",
      "Consumables can be yours or ours. Say which when you book.",
      "Alarm codes and key handling are routine, and get confirmed in writing before the first visit."],
    faq=[
      ("Can you clean outside business hours?", "Yes, and most clients prefer it. Evening and early morning slots are both standard."),
      ("Do you supply paper and soap?", "We can, or we can restock what you buy. Either way, tell us at the quote stage so it is priced properly."),
      ("How often do small offices book?", "Most land on twice a week, with washrooms and bins daily if the headcount justifies it. A quiet studio might only need weekly."),
      ("Are you insured for commercial premises?", "Ask us when you request a quote and we will confirm current coverage in writing before any work starts.")],
    strip=[("images/office-cleaning.jpg", "Office desk disinfected", "Workstations"),
           ("images/entry-mopping.jpg", "Entryway floor mopped", "Entrances"),
           ("images/floor-mopping.jpg", "Hard floors mopped after hours", "Floors"),
           ("images/window-cleaning.jpg", "Interior glass cleaned", "Glass")],
    related=["carpet-cleaning-etobicoke", "window-cleaning-etobicoke", "post-renovation-cleaning"]),

"carpet-cleaning-etobicoke": dict(
    h1="Carpet &amp; Upholstery", glow="CLEANING",
    sub="Hot water extraction that lifts what vacuuming leaves behind, on carpet, area rugs and soft furniture.",
    intro=[
      "Vacuuming takes the loose dirt off the top. Everything else, the ground in traffic lanes, the pet dander, the spill from last winter, sits down in the pile where a vacuum cannot reach it. Extraction flushes the fibre with hot solution and pulls it back out, along with what was living in it.",
      "It is the single most visible cleaning job there is, because carpet holds its history in plain sight. It is also the job most worth doing before a move out inspection, a listing photo or a new baby crawling around."],
    includes_title="How a carpet visit runs",
    includes=[
      "<strong>Inspection first.</strong> We walk the rooms with you, point out what will come out and what is likely permanent, and price from that rather than from a guess.",
      "<strong>Vacuum and pre-treat.</strong> A thorough dry pass, then pre-spray on traffic lanes and spots so the solution has time to work.",
      "<strong>Hot water extraction.</strong> Hot solution injected into the pile and drawn straight back out, taking the suspended soil with it.",
      "<strong>Spot work.</strong> Individual stains treated by type, because a pet accident and a coffee ring do not respond to the same thing.",
      "<strong>Grooming and dry down.</strong> Pile groomed in one direction and airflow set up so the room is usable again sooner."],
    extras_title="Often added",
    extras=[
      "Sofas, armchairs and dining chair seats",
      "Area rugs cleaned in place",
      "Pet odour treatment through the backing",
      "Stair runners and landings",
      "Mattress surface extraction"],
    good=[
      "Expect several hours of drying with airflow, longer in a closed humid room.",
      "Older stains that have set into the backing may lighten rather than disappear.",
      "Move small items and breakables beforehand; we will move the furniture that can be moved.",
      "On a move out, book carpets after the unit is empty and before the inspection."],
    faq=[
      ("How long until the carpet is dry?", "Several hours with windows open or fans running. Keep traffic off it until it is dry to the touch, and off it entirely with shoes."),
      ("Will every stain come out?", "No, and anyone promising that is guessing. Dye stains, bleach marks and old pet damage in the backing often lighten rather than vanish. We tell you which is which before we start."),
      ("Do you clean sofas and chairs?", "Yes, with upholstery tools and a gentler solution. Some fabrics are water sensitive, so we check the care label first."),
      ("Is it safe with pets and children?", "Yes, once dry. Keep them off the area while it dries, mainly so nothing gets tracked back through it.")],
    strip=[("images/carpet-cleaning.jpg", "Carpet cleaned with hot water extraction", "Extraction"),
           ("images/evening-vacuum.jpg", "Living room carpet vacuumed", "Traffic lanes"),
           ("images/living-room.jpg", "Living room after a carpet clean", "Living rooms"),
           ("images/bedroom-result.jpg", "Bedroom carpet refreshed", "Bedrooms")],
    related=["deep-cleaning-etobicoke", "move-out-cleaning-etobicoke", "house-cleaning-etobicoke"]),

"window-cleaning-etobicoke": dict(
    h1="Interior Window", glow="CLEANING",
    sub="Glass, frames, sills and tracks, done from the inside so the daylight actually gets through.",
    intro=[
      "Interior glass goes cloudy slowly enough that nobody notices, and then somebody cleans one pane and the rest of the room looks wrong. Cooking film in a kitchen, condensation residue in a bathroom, dust bonded to the inside of a bedroom window over a winter: all of it comes off, and the room gets visibly brighter for it.",
      "We clean interior panes, the frames around them, the sills under them and the tracks they slide in, which is where the actual dirt lives. We do not work at exterior heights."],
    includes_title="What is covered",
    includes=[
      "<strong>Interior glass.</strong> Panes washed and squeegeed to a streak free finish, including the glass in doors.",
      "<strong>Frames and sills.</strong> Wiped down by hand, corners included, where most of the visible grime sits.",
      "<strong>Tracks and channels.</strong> Vacuumed out then wiped, so sliders move properly again.",
      "<strong>Balcony and patio doors.</strong> Interior face, frame and threshold track.",
      "<strong>Mirrors and interior glass.</strong> Partitions, cabinet glass and mirrors cleaned at the same time."],
    extras_title="Often added",
    extras=[
      "Reachable ground floor exterior panes",
      "Blinds dusted or wiped while the glass is open",
      "Screens removed, rinsed and refitted",
      "Skylights and high interior glass within safe reach",
      "Glass shower screens in the same visit"],
    good=[
      "Book it alongside a deep clean. The glass gets dirty again fast if the room has not been done.",
      "Cloudy sealed units are a failed seal, not dirt, and no amount of cleaning fixes them.",
      "Tell us if blinds or coverings need taking down, since that changes the time.",
      "We work from the inside only, and will say so rather than take on exterior height work."],
    faq=[
      ("Do you clean exterior windows?", "Only reachable ground floor panes from the ground. We do not work at height on exteriors, and we would rather turn the job down than do it badly."),
      ("Will the glass be streak free?", "That is the standard, and we check each pane in the light before moving on. If a pane dries badly, tell us and we will redo it."),
      ("Can you do high rise condo windows?", "The interior face, yes, including balcony glass from inside the suite. The exterior face on a tower is a specialist rope access job."),
      ("Do you clean the tracks?", "Yes, and it is usually the part that makes the biggest difference. Tracks get vacuumed first, then wiped.")],
    strip=[("images/window-cleaning.jpg", "Interior window cleaned streak free", "Glass"),
           ("images/dining-detail.jpg", "Surfaces detailed near the window", "Frames and sills"),
           ("images/living-room.jpg", "Living room with clean glass", "Living rooms"),
           ("images/bathroom-result.jpg", "Shower glass cleared", "Shower glass")],
    related=["deep-cleaning-etobicoke", "condo-cleaning-etobicoke", "house-cleaning-etobicoke"]),

"post-renovation-cleaning": dict(
    h1="Post-Renovation", glow="CLEANING",
    sub="Fine dust off every surface, sill and vent, so the work you just paid for is actually visible.",
    intro=[
      "Renovation dust is not normal dust. It is fine enough to stay airborne for days, it settles on everything including the inside of cupboards you never opened, and it comes back twice after what looks like a thorough clean. A builder's sweep up is not this job.",
      "We clean after kitchens, bathrooms, flooring, painting and full gut jobs. The approach is top down, in passes, with the understanding that the second pass is the one that finishes it."],
    includes_title="What the job covers",
    includes=[
      "<strong>Top down, in passes.</strong> Ceilings lines, light fittings, door frames and tops of cabinets first, floors last, then a second pass once the air has settled.",
      "<strong>Dust traps.</strong> Vents and registers, radiator fins, window tracks, skirting, electrical plates and the tops of every door.",
      "<strong>New surfaces.</strong> Paint spatter, adhesive residue, sticker and label removal from new glass, appliances and fittings.",
      "<strong>Inside everything.</strong> New cabinets, drawers, wardrobes and vanities, which collect dust through the whole build.",
      "<strong>Floors.</strong> Vacuumed with fine filtration, then washed, then checked once dry for the haze that always appears."],
    extras_title="Often added",
    extras=[
      "Carpet extraction after a dusty build",
      "Interior windows, tracks and new glass",
      "Second visit a week later for settled dust",
      "Appliance interiors on a new kitchen",
      "Balcony or entry washed down"],
    good=[
      "Book after the trades are finished, not between them, or you pay to clean the same room twice.",
      "Expect some dust to reappear a few days later; it is still settling out of the air.",
      "Tell us what is newly finished so we treat it gently rather than scrub it.",
      "Protective film and labels come off as part of the job, not as an extra."],
    faq=[
      ("How soon after the work can you come?", "Once the trades are genuinely done and anything wet has cured. Cleaning before the last fix means doing it twice."),
      ("Why does dust come back?", "Because fine particles stay suspended for days and settle slowly. A follow up pass a week later is common on bigger jobs, and worth budgeting for."),
      ("Do you remove construction debris?", "We clean rather than haul. Small amounts of packaging and offcuts go with us; a skip load needs a disposal firm."),
      ("Can you clean new floors safely?", "Yes, once they are cured. Tell us the finish and the manufacturer's guidance and we will work to it.")],
    strip=[("images/kitchen-detail.jpg", "Fine dust wiped from a new kitchen", "New kitchens"),
           ("images/wood-floor.jpg", "New floor cleaned after the trades", "Floors"),
           ("images/window-cleaning.jpg", "New glass cleaned of residue", "New glass"),
           ("images/entry-mopping.jpg", "Entry washed down after a build", "Entries")],
    related=["deep-cleaning-etobicoke", "carpet-cleaning-etobicoke", "window-cleaning-etobicoke"]),

"recurring-cleaning-etobicoke": dict(
    h1="Weekly &amp; Biweekly", glow="CLEANING PLANS",
    sub="The same crew, the same day, the same standard. Set it once and stop thinking about it.",
    intro=[
      "A recurring plan is the cheapest cleaning you will ever buy, per unit of clean. The home never drifts far from the standard, so each visit is shorter than a one off would be, and the price per visit reflects that.",
      "The other half of the value is not having the conversation again. One schedule, one crew who know the home, one standing slot in the calendar. Most clients forget the arrangement exists until they walk in on a Thursday evening."],
    includes_title="How the plans work",
    includes=[
      "<strong>Weekly.</strong> For busy family homes, pets, allergies or anyone who entertains often. Nothing ever gets a chance to build up.",
      "<strong>Every two weeks.</strong> The most common choice, and the sweet spot for most households of two to four people.",
      "<strong>Monthly.</strong> For homes that are kept tidy day to day and want the deeper jobs handled properly once a month.",
      "<strong>Your checklist, not ours.</strong> Rooms you want prioritised, rooms left alone, and extras on a rotation rather than every visit.",
      "<strong>One standing slot.</strong> Same day, same window, same crew wherever scheduling allows."],
    extras_title="Rotate these through the schedule",
    extras=[
      "Inside the oven, every third visit",
      "Inside the fridge, monthly",
      "Interior windows, each season",
      "Carpet extraction, twice a year",
      "Inside cupboards and wardrobes, as needed"],
    good=[
      "The first visit is longer and priced higher; it is doing the catch up work.",
      "Skipping a visit is fine, but a long gap means the next one takes extra time.",
      "Keys, codes and concierge access are normal, and most clients are not home.",
      "Tell us what changed before we arrive, like a new pet or a room being redecorated."],
    faq=[
      ("Am I tied into a contract?", "No. Plans run visit to visit. Tell us when you want to pause, change the frequency or stop."),
      ("Can I change the day?", "Yes, with notice, and permanently if a new slot suits you better. We would rather move it than have you cancel."),
      ("Is it cheaper than booking one offs?", "Per visit, yes, clearly. The home takes less time to clean when it has not been left for three months."),
      ("What happens on holidays?", "Tell us the dates and we skip or move them. Many clients book an extra deep clean before guests arrive instead.")],
    strip=[("images/floor-mopping.jpg", "Hard floors mopped on a recurring visit", "Every visit"),
           ("images/childrens-room.jpg", "Child's room dusted and tidied", "Bedrooms"),
           ("images/evening-vacuum.jpg", "Evening vacuuming in a living room", "Evening slots"),
           ("images/dining-detail.jpg", "Dining table detailed", "Living areas")],
    related=["house-cleaning-etobicoke", "deep-cleaning-etobicoke", "kitchen-bathroom-cleaning"]),
}


def build_service(svc):
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
            <img src="{IMG}" alt="{ALT}" loading="lazy">
            <figcaption>{CAPTION}</figcaption>
          </figure>

          <h2>{INCTITLE}</h2>
          <ul>{INCLUDES}</ul>

          <h2>{EXTITLE}</h2>
          <ul>{EXTRAS}</ul>

          <h2>Worth knowing before you book</h2>
          <ul>{GOOD}</ul>

          <h2>In the detail</h2>
          {STRIP}

          <h2>Questions about {SHORT}</h2>
          {FAQ}

          <h2>Often booked with this</h2>
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
        IMG=svc["img"], ALT=svc["alt"],
        CAPTION="%s across %s. Quote first, work second." % (strip(svc["short"]), strip(AREA)),
        INCTITLE=c["includes_title"],
        INCLUDES="".join("<li>%s</li>" % x for x in c["includes"]),
        EXTITLE=c["extras_title"],
        EXTRAS="".join("<li>%s</li>" % x for x in c["extras"]),
        GOOD="".join("<li>%s</li>" % x for x in c["good"]),
        STRIP=photo_strip(0, c["strip"]),
        SHORT=short_plain,
        FAQ=faq_block(c["faq"]),
        RELATED=service_tiles(0, related),
        SIDEBAR=sidebar(0, photo=svc["thumb"], photo_alt=svc["thumb_alt"],
                        photo_cap=strip(svc["short"]) + " detail"),
        CTA=cta_strip(0), FOOT=footer(0))

    html = head(
        title=strip(svc["title"]) + " | " + NAME,
        desc=strip(c["sub"])[:300],
        canonical="%s/%s.html" % (BASE, svc["slug"]),
        og_image=svc["img"],
        extra_ld=ld_service(svc) + ld_breadcrumb(trail) + ld_faq(c["faq"]),
    ) + hero_small(
        0, trail, c["h1"], c["glow"], c["sub"], media=svc["img"], alt=svc["alt"],
    ) + body
    BUILT.append(write(svc["slug"] + ".html", html))


for s in SERVICES:
    build_service(s)


# ----------------------------------------------------------------------
# Service area pages
# ----------------------------------------------------------------------
def build_location(loc):
    area = loc["area"]
    trail = [(area, loc["slug"] + ".html")]
    faq = [
        ("Do you charge extra to come out to %s?" % area,
         "No. %s is part of the regular service area, so travel is not added on top of your quote." % area),
        ("How quickly can you get to %s?" % area,
         "Same week is normal and same day is often possible if you call early. End of month moving dates are the one busy period worth booking ahead for."),
        ("Do you work on condos and apartments in %s?" % area,
         "Yes. Condo work is routine, including elevator bookings, loading dock times and concierge access. Tell us the building rules and we will work to them."),
        ("Can you work when nobody is home?",
         "Yes. Keys, lockboxes and concierge handover are all normal. We lock up and send photos when the job is done."),
    ]
    tiles = service_tiles(0, [BY_SLUG[s] for s in (
        "house-cleaning-etobicoke", "deep-cleaning-etobicoke", "move-out-cleaning-etobicoke",
        "condo-cleaning-etobicoke", "kitchen-bathroom-cleaning", "carpet-cleaning-etobicoke")])
    others = "".join(
        '<li><a href="%s.html">%s</a></li>' % (l["slug"], l["area"])
        for l in LOCATIONS if l["slug"] != loc["slug"])

    html = head(
        title="House Cleaning in %s | %s" % (area, NAME),
        desc=("House cleaning, deep cleans, move in and move out, condos, carpets and interior windows in "
              "%s. Free photo quotes from Fanta Cleaning, open seven days." % area),
        canonical="%s/%s.html" % (BASE, loc["slug"]),
        og_image=loc["img"],
        extra_ld=ld_breadcrumb(trail) + ld_faq(faq),
    ) + hero_small(
        0, trail, "House Cleaning in", area.upper(),
        "The full list, delivered in %s: regular and deep cleaning, move in and move out, condos and apartments, kitchens and bathrooms, offices, carpets and interior windows. %s" % (area, loc["note"]),
        media=loc["img"], alt=loc["alt"],
    ) + """
  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div class="content-main">
          <h2>Working in {AREA}</h2>
          <p>{NOTE} Whether it is a standing clean for a family home, a condo that needs doing while you are at work, or a unit being turned around between tenants, it is the same crew and the same number.</p>
          <p>Homes in {AREA} run the full range, from older detached houses to newer condo stock, and each asks for something different. Older houses tend to need the deep clean, the grout and the carpets. Newer units tend to need turnovers, glass and post-renovation dust. We quote from photos either way, so the price fits the home rather than an average.</p>

          <figure class="media-figure">
            <img src="{IMG}" alt="{ALT}" loading="lazy">
            <figcaption>Serving {AREA} and the surrounding neighbourhoods, seven days a week.</figcaption>
          </figure>

          <h2>What gets booked most in {AREA}</h2>
          <div class="grid grid-3" style="margin-top:1rem;">
{TILES}
          </div>

          <h2>Getting a quote in {AREA}</h2>
          <p>Send photos on WhatsApp with your neighbourhood and the service you want. If parking is tight, if there is an elevator to book, or if a concierge handles access, mention it, because those details change the timing more than the cleaning does.</p>

          <h2>Questions from {AREA} clients</h2>
          {FAQ}

          <h2>Other areas we cover</h2>
          <ul>{OTHERS}</ul>
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(AREA=area, NOTE=loc["note"], IMG=loc["img"], ALT=loc["alt"],
                      TILES=tiles, FAQ=faq_block(faq), OTHERS=others,
                      SIDEBAR=sidebar(0, photo="images/living-room.jpg",
                                      photo_alt="Living room cleaned and reset",
                                      photo_cap="Booked across " + area),
                      CTA=cta_strip(0), FOOT=footer(0))
    BUILT.append(write(loc["slug"] + ".html", html))


for l in LOCATIONS:
    build_location(l)

if __name__ == "__main__":
    for p in BUILT:
        print("built", p)
