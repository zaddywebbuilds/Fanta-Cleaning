# -*- coding: utf-8 -*-
"""Builds the blog index and every article."""

from common import (NAME, PHONE, PHONE_TEL, AREA, BASE, SERVICES, BY_SLUG, WA_QUOTE,
                    head, ld_breadcrumb, ld_faq, hero_small, photo_strip, cta_strip,
                    footer, sidebar, faq_block, write, strip,
                    new_page, pick, img_tag)

BUILT = []
D = 1  # every article lives in /blog/

POSTS = [
dict(slug="how-much-does-house-cleaning-cost-in-etobicoke",
     title="How Much Does House Cleaning Cost in Etobicoke?",
     date="2026-09-08", pretty="8 September 2026", read="6 min",
     img="kitchen-deep-clean",
     teaser="Why nobody honest quotes a flat number over the phone, and the six things that actually move the price.",
     service="deep-cleaning-etobicoke",
     body=[
      ("", ["Ask five cleaning companies what a three bedroom house costs and you will get five answers, three of which will change once someone actually sees the place. That is not always dishonesty. It is that square footage on its own tells you almost nothing about how long a home takes to clean.",
            "Here is what genuinely drives the number, so you can judge any quote you are given, including ours."]),
      ("1. Size, but less than you think", [
       "Square footage sets a floor on the time. What sets the ceiling is the number of bathrooms and the number of floors. Bathrooms are the slowest rooms in any house by a wide margin, and a second one adds more time than another bedroom does. Stairs slow everything down, because equipment has to be carried rather than wheeled."]),
      ("2. How long since the last proper clean", [
       "This is the single biggest variable and the one most quotes get wrong. A home cleaned every two weeks takes a fraction of the time of the same home untouched for a year. Soap scum, grease and limescale all harden with age, and hardened residue is scrubbing time, not wiping time.",
       "It is also why a first visit is usually priced higher than the ones that follow. The first visit is catching up. Everything after is maintaining."]),
      ("3. Occupied or empty", [
       "Empty homes clean faster, because there is nothing to work around. They also get judged harder, because with the furniture gone every mark is visible. Move out and turnover cleans are priced on that higher standard rather than on the easier access."]),
      ("4. What is in scope", [
       "Inside the oven, inside the fridge, inside cabinets, interior windows, balcony glass, carpets: every one of these is real time and should be listed in the quote rather than assumed. A cheap quote that leaves them out is not cheaper, it is smaller. Ask what is included before comparing two numbers."]),
      ("5. Pets, people and traffic", [
       "Two adults who work late do not generate the same mess as three children and a shedding dog. Pet hair in particular is time, because it bonds to upholstery and carpet and has to be lifted rather than swept. Mention pets when you ask for a quote and the number you get will hold."]),
      ("6. Frequency", [
       "Recurring work costs less per visit, because each visit is shorter. Weekly, every other week and monthly schedules all price below a comparable one off. If you are deciding between a single deep clean and a schedule, the honest answer is usually one deep clean to reset, then a schedule to hold it."]),
      ("So what should you actually do", [
       "Take photos of your kitchen, your bathrooms and any room you are worried about. Send them with the number of bedrooms and bathrooms and whether the place is occupied. Any competent cleaner can price that accurately within the hour, and you avoid the quote that changes at the door."]),
     ]),

dict(slug="deep-clean-vs-regular-clean",
     title="Deep Clean or Regular Clean: Which One Do You Actually Need?",
     date="2026-09-15", pretty="15 September 2026", read="5 min",
     img="residential-cleaning",
     teaser="One resets the home, the other holds it there. Booking the wrong one is how people end up disappointed.",
     service="deep-cleaning-etobicoke",
     body=[
      ("", ["Most disappointment with a cleaning company comes from booking the wrong product. Somebody pays for a standard clean, expects the oven to come out looking new, and is unhappy with work that was done exactly as described. The two jobs are genuinely different, and the difference is worth two minutes of your time."]),
      ("What a regular clean is for", [
       "A regular clean maintains a standard that already exists. It wipes the front of the oven, clears the shower glass of this week's soap film, dusts the surfaces people see, vacuums and mops. It is fast because the home has not been allowed to drift.",
       "It is the right booking if the home was deep cleaned recently, or if it has been looked after and you simply want the time back."]),
      ("What a deep clean is for", [
       "A deep clean resets a standard that has slipped. It takes the oven racks out and does the inside. It scrubs grout rather than mopping over it. It gets the tops of door frames, the vents, the ceiling fan blades and behind the furniture that can be moved.",
       "It is the right booking if nobody has done those things in over a year, if you have just taken over a home, or if guests are arriving and you want the whole place to feel the same."]),
      ("The honest sequence for most homes", [
       "One deep clean, then a recurring schedule. The deep clean does the catch up work once, and the schedule holds it for a fraction of the cost. Paying rescue prices every visit because you never reset is the most expensive way to buy cleaning.",
       "If budget means picking one, pick the deep clean. A regular clean on a home that needs a deep clean will leave you unhappy, and it will not fix the things that were actually bothering you."]),
      ("Three questions that settle it", [
       "<strong>When was the oven last cleaned inside?</strong> If you cannot remember, you want a deep clean.",
       "<strong>Is the shower glass clear or hazy?</strong> Haze is limescale, and limescale is deep clean work.",
       "<strong>Can you write your name in the dust on top of a door frame?</strong> Then the dust is at every height, and a surface clean will not touch it."]),
      ("What it costs in time", [
       "A regular clean on an average three bedroom home is a few hours. A deep clean on the same home is most of a working day, sometimes more. That gap is the whole difference, and any quote that prices them the same is describing the same job twice."]),
     ]),

dict(slug="move-out-cleaning-checklist-etobicoke",
     title="The Move Out Cleaning Checklist Landlords Actually Inspect",
     date="2026-09-22", pretty="22 September 2026", read="6 min",
     img="move-out-cleaning",
     teaser="The rooms and details a walkthrough stops at, in the order an inspection usually works through them.",
     service="move-out-cleaning-etobicoke",
     body=[
      ("", ["An empty unit is the hardest thing to clean, because nothing is left to hide behind. Inspections are also predictable: they look at the same places in roughly the same order, every time. Work the list in that order and you stop guessing."]),
      ("The kitchen, which decides most of it", [
       "<strong>Inside the oven.</strong> The first thing checked and the most commonly failed. Racks out, interior degreased, door glass clear.",
       "<strong>Behind and under the appliances.</strong> Pull the fridge and the stove where they move. Both hide a year of crumbs and grease.",
       "<strong>Every cupboard and drawer, inside.</strong> Emptied, vacuumed, wiped, including the tops of the upper cabinets.",
       "<strong>The sink and taps.</strong> Limescale off, drain clear, no standing residue in the overflow."]),
      ("The bathrooms, which decide the rest", [
       "<strong>Grout and silicone.</strong> Scrubbed rather than mopped over. Discoloured silicone sometimes needs replacing, not cleaning, and that is worth knowing before the inspection.",
       "<strong>Shower glass.</strong> Soap film and limescale removed so it is genuinely clear in the light.",
       "<strong>Behind and around the toilet base.</strong> Consistently missed, consistently checked.",
       "<strong>The extractor vent cover.</strong> Dusty vents read as neglect even when the rest is spotless."]),
      ("Everywhere else", [
       "<strong>Skirting and door frames.</strong> Wiped by hand, including the tops.",
       "<strong>Closets and shelving, inside.</strong> Including the rail and the top shelf nobody reaches.",
       "<strong>Switch plates and handles.</strong> Where fingerprints accumulate for years.",
       "<strong>Window tracks and sills.</strong> Vacuumed first, then wiped, or you just smear it.",
       "<strong>Floors, wall to wall.</strong> Now that the furniture is gone, mop to the edges rather than the middle."]),
      ("The things people forget", [
       "Light fittings and the inside of shades. The balcony door track. The inside of the washing machine drawer and seal. The top of the fridge. The radiator fins. None of them take long, and all of them are visible to someone looking for a reason."]),
      ("Timing it properly", [
       "Clean after the movers, not before. A half empty unit has to be cleaned twice, and you will pay for both. If there is a handover time, say so when booking so the day is planned around it.",
       "Finish with photos of every room. They settle most deposit disputes before they start, and they cost nothing to take."]),
     ]),

dict(slug="how-often-should-you-clean-your-house",
     title="How Often Should You Actually Clean Your House?",
     date="2026-09-29", pretty="29 September 2026", read="5 min",
     img="floor-mopping",
     teaser="A realistic schedule by room and by task, for people who do not want to think about it again.",
     service="recurring-cleaning-etobicoke",
     body=[
      ("", ["Most cleaning advice is written for people with nothing else to do. This is the version that assumes you have a job. The principle is simple: a few things need doing often, most things need doing occasionally, and a handful of jobs need doing twice a year and are then forgotten about."]),
      ("Weekly, without fail", [
       "<strong>Bathrooms.</strong> The one room where a week's gap is visible and a fortnight's gap is a scrubbing job.",
       "<strong>Kitchen surfaces and the cooktop.</strong> Grease that sits gets sticky, and sticky grease is a different job.",
       "<strong>Floors in the rooms people walk through.</strong> Entry, kitchen, hallway.",
       "<strong>Bins and bedding.</strong> Both for the same reason: smell builds before you notice it."]),
      ("Every two weeks", [
       "<strong>Dusting at every height.</strong> Sills, ledges, shelves and the tops of frames.",
       "<strong>Vacuuming the whole home</strong>, including under what moves easily.",
       "<strong>Mirrors and interior glass.</strong>",
       "<strong>Switch plates, handles and bannisters.</strong> The things everyone touches and nobody cleans."]),
      ("Monthly", [
       "<strong>Inside the microwave and the fridge.</strong>",
       "<strong>Behind and under the furniture that moves.</strong>",
       "<strong>Skirting boards and door frames.</strong>",
       "<strong>Shower head descaled and the extractor vent wiped.</strong>"]),
      ("Twice a year, and then forget about it", [
       "<strong>Inside the oven.</strong> More often if you roast regularly.",
       "<strong>Carpets, properly extracted.</strong> Once before winter, once after.",
       "<strong>Interior windows, tracks included.</strong>",
       "<strong>Inside cupboards and wardrobes, emptied.</strong>",
       "<strong>Mattresses turned and the surface cleaned.</strong>"]),
      ("What this looks like if somebody else does it", [
       "A home on a biweekly plan gets the weekly and fortnightly list every visit, the monthly list rotated through, and the twice yearly jobs booked as add ons when they come due. That is the whole system, and it is why a recurring visit costs less per hour of result than a one off rescue.",
       "If you are doing it yourself, the only rule that matters is this: never let the bathrooms and the kitchen slide. Everything else is recoverable in an afternoon. Those two are not."]),
     ]),

dict(slug="condo-cleaning-guide-toronto",
     title="Cleaning a Condo Properly: What Houses Do Not Prepare You For",
     date="2026-10-06", pretty="6 October 2026", read="5 min",
     img="living-room",
     teaser="Shared air, balcony glass, elevator bookings and the five square feet that make a suite feel dirty.",
     service="condo-cleaning-etobicoke",
     body=[
      ("", ["A condo is not a small house. The cleaning is denser, the dust arrives differently, and the parts that make a suite feel grubby are not the parts that make a house feel grubby. Crews used to detached homes consistently clean the middle of a condo and miss the rest."]),
      ("The dust comes from the building", [
       "Shared HVAC moves air between units, which means your dust is partly everyone's dust. Vent covers and return grilles collect it fast, and they are at eye level, so they read as neglect quickly. Wiping them is thirty seconds and changes how the whole suite looks."]),
      ("Balcony glass does more work than any window", [
       "A balcony door is the single largest piece of glass in most suites and it faces weather on one side and cooking on the other. The interior face, the frame and the threshold track together make more visual difference than every other window combined.",
       "The track is the part that matters. Vacuum it first, then wipe, or you are just making mud."]),
      ("Storage density is the real problem", [
       "Condos store vertically and tightly. Entry closets, under sink cabinets and the laundry nook are packed, so dust and spills sit undisturbed for years. Cleaning the open floor of a suite while those stay untouched is why a place can be freshly cleaned and still feel off."]),
      ("The building has rules, and they cost time", [
       "<strong>Elevator bookings.</strong> Some buildings require one for any service visit. Find out before the day.",
       "<strong>Concierge access.</strong> Leaving a key at the desk is normal, but it has to be arranged in advance.",
       "<strong>Visitor parking.</strong> Often gone by mid morning, which pushes the start time.",
       "<strong>Product and water restrictions.</strong> A few buildings restrict wet work in common areas, so plan the route in and out."]),
      ("The five square feet that decide everything", [
       "The entry. It is the first thing anyone sees, it takes every shoe in the building, and it is the smallest area in the suite. Mopping it properly, wiping the door, the handle and the closet track takes a few minutes and sets the impression for the whole place."]),
     ]),

dict(slug="how-to-prepare-for-a-cleaning-visit",
     title="How to Prepare for a Cleaning Visit (and Get More for Your Money)",
     date="2026-10-13", pretty="13 October 2026", read="4 min",
     img="dining-detail",
     teaser="Fifteen minutes of preparation turns a cleaning visit into more cleaning and less tidying.",
     service="house-cleaning-etobicoke",
     body=[
      ("", ["You are paying for cleaning time. Anything a crew spends moving your things around is time not spent on surfaces, and it is the most common reason people feel a visit under delivered. Fifteen minutes beforehand changes the result noticeably."]),
      ("Clear the horizontal surfaces", [
       "Counters, the dining table, bedside tables, the bathroom vanity. Not tidied into neat piles, actually cleared. A counter with six items on it gets wiped around. An empty counter gets wiped properly, and takes less time doing it."]),
      ("Deal with the floor", [
       "Shoes, toys, laundry, charging cables and pet bowls. Vacuuming a clear floor is fast. Vacuuming around obstacles is slow and the edges get missed, which is exactly where dirt lives."]),
      ("Say what matters most", [
       "If the bathrooms are the thing bothering you, say so. A crew working a standard order spreads time evenly, which is correct unless you have a priority. One sentence redirects the whole visit.",
       "Say what to leave alone too. A home office mid project, a child's room, a shelf of fragile things. Rooms left alone stay untouched, and nobody has to guess."]),
      ("Handle the pets", [
       "Tell us their names, whether they are nervous and whether doors need keeping shut. Vacuums frighten most animals, and a stressed dog in a small home slows everything down for everyone, the dog included."]),
      ("Sort the access", [
       "Key, lockbox code, concierge instruction, alarm code and parking. Most cleaning happens in empty homes and none of it is unusual, but it has to be arranged before the day rather than over the phone while a crew waits outside.",
       "If a building needs an elevator booked, that is the one thing worth doing a week ahead."]),
      ("What not to bother with", [
       "Do not pre clean. People do, and it is money wasted. Do not strip beds unless you want them remade. Do not move heavy furniture; we will move what is safe to move and leave what is not."]),
     ]),

dict(slug="carpet-cleaning-what-to-expect",
     title="Carpet Cleaning: What Comes Out, What Does Not, and How Long It Takes to Dry",
     date="2026-10-20", pretty="20 October 2026", read="5 min",
     img="carpet-cleaning",
     teaser="Honest expectations for hot water extraction, including the stains nobody can promise to remove.",
     service="carpet-cleaning-etobicoke",
     body=[
      ("", ["Carpet cleaning is the most visible result in this trade and the one most oversold. Extraction does a great deal, and it does not do everything. Knowing the difference before you book is the whole of being satisfied afterwards."]),
      ("What extraction actually does", [
       "Hot solution is injected into the pile under pressure and immediately drawn back out, taking suspended soil with it. Vacuuming removes what sits on top. Extraction removes what has worked its way down, which on a traffic lane is most of it.",
       "A proper job is four stages: dry vacuum, pre spray and dwell, extract, groom. Skipping the pre spray is how a carpet comes out wet rather than clean."]),
      ("What reliably comes out", [
       "<strong>Traffic lane soiling.</strong> The grey paths between rooms, which are ground in dirt rather than stains.",
       "<strong>Most food and drink spills</strong>, if they have not been there for years.",
       "<strong>Pet dander and hair deep in the pile.</strong>",
       "<strong>General dullness.</strong> Carpets usually come back a shade or two lighter, which surprises people more than the stain removal does."]),
      ("What often does not", [
       "<strong>Dye stains.</strong> Red drinks, some inks and certain foods bond to the fibre rather than sitting on it.",
       "<strong>Bleach marks.</strong> That is missing colour, not added dirt. Nothing brings it back.",
       "<strong>Old pet accidents in the backing.</strong> If it has soaked through to the underlay, cleaning the surface lightens it and the smell returns in humid weather.",
       "<strong>Sun fade and wear.</strong> Worn fibre looks dull because it is damaged, not dirty."]),
      ("Drying, realistically", [
       "Several hours with airflow. Longer in a closed humid room, and longer again in a basement. Open windows, run fans, and keep shoes off it entirely until it is dry to the touch.",
       "A carpet that is still properly wet the next day was over wet during cleaning. Done correctly it is damp, not soaked."]),
      ("When it is worth booking", [
       "Before a move out inspection, because carpet is the first thing an inspection looks at. Before a listing photo. After a renovation. And twice a year in a home with pets, which is less about appearance than about what is living in the pile."]),
     ]),

dict(slug="kitchen-grease-and-limescale-guide",
     title="Grease and Limescale: Why Your Kitchen and Bathroom Resist Cleaning",
     date="2026-10-27", pretty="27 October 2026", read="5 min",
     img="kitchen-detail",
     teaser="Two different problems that need two different approaches, and why scrubbing harder makes one of them worse.",
     service="kitchen-bathroom-cleaning",
     body=[
      ("", ["The two rooms people most want clean are the two that resist it hardest, and for opposite reasons. Grease is organic and sticky. Limescale is mineral and hard. Treating one like the other is why a whole afternoon of scrubbing sometimes achieves nothing."]),
      ("Grease: the problem is time, not effort", [
       "Cooking vapour lands on every surface in a kitchen, not just the ones near the stove. Fresh, it wipes off. Left for months it oxidises into a sticky film that grabs dust, and that combination is what gives old kitchens their tacky feel.",
       "The fix is dwell time, not pressure. A degreaser needs minutes on the surface to break the film down. Spraying and immediately wiping just moves it around, which is why the cloth comes away brown and the surface still feels tacky."]),
      ("Where grease actually hides", [
       "<strong>The wall and cabinet sides next to the stove</strong>, which nobody treats as kitchen surfaces.",
       "<strong>The range hood filter</strong>, which is usually the single worst item in the room.",
       "<strong>The tops of upper cabinets</strong>, where vapour settles and stays.",
       "<strong>Cabinet handles and the fronts around them</strong>, where grease meets hands."]),
      ("Limescale: the problem is chemistry, not elbow", [
       "Hard water leaves mineral deposits as it evaporates. On glass it is the haze that will not wipe off. On taps it is the white crust. On a shower head it is the reason half the jets have stopped aiming straight.",
       "Scrubbing it with an abrasive scratches the surface and gives the next deposit more to hold on to, which is why aggressively cleaned shower glass fogs up faster each time. It needs an acidic treatment and dwell time, then a gentle wipe."]),
      ("The one that cannot be fixed", [
       "Glass that has been left to scale for years develops etching, where the mineral has pitted the surface. The haze is then physical damage rather than deposit, and no product removes it. Repeat treatments improve it; nothing restores it. Anyone promising otherwise has not looked closely."]),
      ("The practical routine", [
       "Wipe the cooktop and surround while the kitchen is still warm from cooking, when grease is softest. Squeegee shower glass after use, which takes ten seconds and prevents the problem entirely. Everything else is recoverable; those two habits are what stop it recurring."]),
     ]),

dict(slug="cleaning-with-pets-in-the-house",
     title="Cleaning a Home With Pets: Hair, Odour and the Things That Actually Work",
     date="2026-11-03", pretty="3 November 2026", read="5 min",
     img="evening-vacuum",
     teaser="Why pet hair defeats ordinary vacuuming, and where the smell is really coming from.",
     service="carpet-cleaning-etobicoke",
     body=[
      ("", ["Homes with pets do not need more cleaning so much as different cleaning. Hair behaves unlike dust, and odour almost never comes from where people think it does. Both are solvable, and neither responds well to simply doing the normal routine more often."]),
      ("Hair weaves rather than settles", [
       "Dust settles on top of fibre. Hair works into it, especially on upholstery and low pile carpet, where static holds it in place. A vacuum pulling air across the surface lifts dust and leaves hair behind, which is why a room can be vacuumed and still look hairy.",
       "What works is agitation first: a rubber brush, a squeegee blade drawn across upholstery, or a beater bar on carpet. Lift the hair out of the weave, then vacuum it away. The order matters more than the equipment."]),
      ("Where it accumulates", [
       "<strong>Where the air stops.</strong> Under furniture, behind doors, along skirting.",
       "<strong>Fabric that is never moved.</strong> The back of a sofa cushion, under the bed, curtain hems.",
       "<strong>Textile edges.</strong> Carpet against skirting, where hair compacts into a line.",
       "<strong>Car boots and entry mats</strong>, which then reload the house."]),
      ("The smell is in the soft things", [
       "People clean hard surfaces and wonder why the smell persists. Odour lives in textiles: carpet backing, upholstery foam, curtains, bedding and the pet's own bed. Hard surfaces hold almost nothing by comparison.",
       "Masking it with scent makes it worse over time, because you add rather than remove. The only durable fix is washing or extracting the textiles, and replacing the pet bed more often than feels necessary."]),
      ("Accidents need to be treated, not cleaned", [
       "Urine that reaches carpet backing or underlay is a chemistry problem. Surface cleaning lightens the mark and the smell returns in humid weather, because the residue is still there reactivating.",
       "It needs an enzyme treatment with enough volume to reach as deep as the accident did, and enough dwell time to work. Under treating is the most common mistake, and it is why the same spot keeps coming back."]),
      ("A workable schedule", [
       "Agitate and vacuum traffic areas and favourite spots weekly. Wash the pet bed and throws every couple of weeks. Extract carpets and upholstery twice a year. Treat accidents the day they happen rather than the week after, which is the single highest return habit on this list."]),
     ]),

dict(slug="post-renovation-dust-guide",
     title="Why Renovation Dust Comes Back Twice (and How to Beat It)",
     date="2026-11-10", pretty="10 November 2026", read="4 min",
     img="wood-floor",
     teaser="Fine particles stay airborne for days. Here is how to clean around that instead of fighting it.",
     service="post-renovation-cleaning",
     body=[
      ("", ["Everyone who has cleaned after a renovation has had the same experience: a thorough job, a spotless room, and a visible film on every surface two days later. It is not a failed clean. It is physics, and planning around it is cheaper than repeating the work."]),
      ("Why it stays in the air", [
       "Drywall and plaster dust is extremely fine and extremely light. Large particles fall within minutes; the fine fraction stays suspended for days, circulating on every draught, and settles gradually long after the trades have gone.",
       "This is why the second pass exists. The first clean removes what has already landed. The second removes what was still airborne during the first."]),
      ("Work top down, and wet", [
       "Start at the ceiling line and finish at the floor, or you will clean the floor twice. Use damp cloths rather than dry ones, because a dry cloth launches fine dust back into the air and you have just relocated the problem.",
       "A dry sweep of a dusty floor is the single worst thing you can do in a post renovation clean. Vacuum with fine filtration instead, then wash."]),
      ("The places that hold the most", [
       "<strong>Vents and registers.</strong> They keep feeding dust back into the room every time the system runs.",
       "<strong>Window tracks and sills.</strong> Where draughts deposit it.",
       "<strong>Tops of doors and frames.</strong> Flat, invisible and never checked.",
       "<strong>Inside new cabinets and wardrobes.</strong> Open through the whole build, dusty throughout.",
       "<strong>Radiator fins and light fittings.</strong> Warm surfaces attract and hold fine particles."]),
      ("Sequence the job properly", [
       "Clean after the trades are genuinely finished, not between them. Cleaning a room that still has a tradesperson returning to it means paying twice for the same work.",
       "Change filters afterwards. Running the HVAC through a renovation loads the filter, and a loaded filter redistributes what it cannot hold.",
       "Budget for a follow up pass a week later on bigger jobs. It is a short visit and it is the one that actually finishes the job."]),
     ]),

dict(slug="cleaning-products-you-should-never-mix",
     title="Cleaning Products You Should Never Mix, and Simpler Alternatives",
     date="2026-11-17", pretty="17 November 2026", read="4 min",
     img="bathroom-detail",
     teaser="A short safety list worth knowing, plus why most homes need three products rather than fifteen.",
     service="kitchen-bathroom-cleaning",
     body=[
      ("", ["Most homes have a cupboard full of products, most of which overlap, and two of which should never meet. This is the short version of what matters, written for people who just want their bathroom clean without reading a chemistry text."]),
      ("The combinations to avoid", [
       "<strong>Bleach and ammonia.</strong> Produces chloramine vapour. Many glass cleaners contain ammonia, so this happens by accident more often than on purpose.",
       "<strong>Bleach and acid.</strong> Vinegar, lemon, and most limescale and toilet bowl products are acidic. The combination releases chlorine gas.",
       "<strong>Bleach and rubbing alcohol.</strong> Produces chloroform and related compounds.",
       "<strong>Different drain cleaners, one after the other.</strong> They react violently in a confined pipe and can force material back up."]),
      ("The rule that covers all of it", [
       "Never mix anything with bleach, and never layer one product on top of another without rinsing in between. Rinsing is the whole safety margin, and it takes seconds. If a surface needs two treatments, rinse and dry between them.",
       "Ventilate while you work, even with products that seem mild. A sealed bathroom concentrates vapour fast."]),
      ("What most homes actually need", [
       "<strong>A degreaser</strong> for the kitchen, which handles everything cooking produces.",
       "<strong>An acidic descaler</strong> for the bathroom, which handles limescale and soap film.",
       "<strong>A neutral floor cleaner</strong>, because most floor finishes are damaged by anything strong.",
       "<strong>A disinfectant</strong> for the touch points and the toilet.",
       "That is four products. Most of the rest of the cupboard is one of those four with a different scent and a higher price."]),
      ("Surfaces that need care", [
       "Natural stone, including marble and some granite, is etched by acids, so no vinegar and no descaler. Waxed and oiled wood dislikes anything alkaline. Unsealed grout absorbs whatever you put on it. Painted surfaces lift under solvents.",
       "If you are unsure what a surface is, test in a corner and wait. Ten minutes of patience beats a permanently dull patch in the middle of a floor."]),
      ("The part that matters more than the product", [
       "Dwell time. Almost every product works better if left on the surface for a few minutes before wiping. Most people spray and wipe immediately, then conclude the product is weak and buy a stronger one. It usually was not."]),
     ]),

dict(slug="spring-cleaning-checklist-etobicoke",
     title="A Spring Cleaning Checklist That Is Not Just the Usual List",
     date="2026-11-24", pretty="24 November 2026", read="5 min",
     img="bedroom-result",
     teaser="The jobs worth doing once a year, in the order that stops you doing any of them twice.",
     service="deep-cleaning-etobicoke",
     body=[
      ("", ["Spring cleaning lists usually read like a regular clean with more enthusiasm. The jobs actually worth doing annually are the ones nobody does monthly, and the order matters, because half of them create mess that lands on the other half."]),
      ("Do these first, because they create dust", [
       "<strong>Ceiling fans, light fittings and shades.</strong> Everything you disturb lands below.",
       "<strong>Vents, registers and radiator fins.</strong> A winter's worth of circulated dust.",
       "<strong>Tops of wardrobes, cabinets and door frames.</strong>",
       "<strong>Curtains and blinds.</strong> Washed or wiped, and left to dry before anything else starts."]),
      ("Then the interiors nobody opens", [
       "<strong>Inside cupboards and wardrobes, emptied.</strong> The one chance a year to find what is in there.",
       "<strong>Inside the oven and behind it.</strong>",
       "<strong>The fridge, including the seals and the drip tray.</strong>",
       "<strong>Under the beds and behind the larger furniture.</strong>",
       "<strong>The washing machine drawer, drum seal and filter.</strong> The source of most mystery laundry smells."]),
      ("Then the soft things", [
       "Carpets extracted, upholstery cleaned, mattresses turned and surface cleaned, and every throw and cushion cover washed. Textiles hold a winter of closed up air, and this is the step that changes how a home smells rather than how it looks."]),
      ("Then glass and floors, last", [
       "Interior windows with the tracks vacuumed first. Then hard floors, washed to the edges. Doing these before the dusty jobs means doing them twice, which is the most common sequencing mistake there is."]),
      ("The seasonal extras for this climate", [
       "Winter salt tracks into entryways and damages hard floors and carpet near the door. The entry mat, the hallway runner and the first few feet of floor inside every exterior door are worth a proper treatment once the salt season ends.",
       "Window tracks collect grit through winter and then hold meltwater, which is how they end up mouldy by April. Clear them out before the weather warms rather than after."]),
      ("Being realistic about it", [
       "This is a weekend of work in an average home, or most of a day for a crew. Splitting it across two weekends is fine, as long as you keep the order: dust high, interiors, soft things, glass and floors last. Out of order, you will be cleaning the same floor three times."]),
     ]),
]


def article(p):
    new_page()
    svc = BY_SLUG[p["service"]]
    trail = [("Blog", "blog/index.html"), (p["title"], "blog/%s.html" % p["slug"])]
    sections = []
    for heading, paras in p["body"]:
        if heading:
            sections.append("          <h2>%s</h2>" % heading)
        # Consecutive runs that open with <strong> become a list, in place.
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
    "image":"{B}/{IMG}",
    "author":{{"@type":"Organization","name":"{N}"}},
    "publisher":{{"@type":"Organization","name":"{N}","logo":{{"@type":"ImageObject","url":"{B}/images/logo.svg"}}}},
    "mainEntityOfPage":"{B}/blog/{S}.html"}}
  </script>
""".format(T=strip(p["title"]), D=p["date"], B=BASE, IMG=p["img"], N=NAME, S=p["slug"])

    others = [q for q in POSTS if q["slug"] != p["slug"]][:3]
    more = "".join(
        '<article class="service-tile"><div class="service-tile-media">%s</div>'
        '<div class="service-tile-body"><h3>%s</h3><p>%s</p>'
        '<div class="row"><a href="%s.html">Read &rarr;</a></div></div></article>'
        % (img_tag(pick(q["img"]), D), q["title"], q["teaser"], q["slug"])
        for q in others)

    html = head(
        title=strip(p["title"]) + " | " + NAME,
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
            <figcaption>Need this handled instead of read about? {SSHORT} across {AREA}.</figcaption>
          </figure>

          <div class="btn-row" style="margin:1.4rem 0;">
            <a class="btn btn-whatsapp" href="{WA}" target="_blank" rel="noopener">Get a Free Quote</a>
            <a class="btn btn-gold" href="../{SSLUG}.html">{SSHORT}</a>
            <a class="btn btn-glass" href="tel:{TEL}">Call {PHONE}</a>
          </div>

          <h2>More from the blog</h2>
          <div class="grid grid-3" style="margin-top:1rem;">{MORE}</div>
        </div>

{SIDEBAR}
      </div>
    </div>
  </section>

{CTA}{FOOT}""".format(PRETTY=p["pretty"], READ=p["read"], BODY="\n".join(sections),
                      SFIG=img_tag(pick(svc["thumb"], svc["img"]), D),
                      SSHORT=strip(svc["short"]),
                      SSLUG=svc["slug"], AREA=AREA, WA=WA_QUOTE, TEL=PHONE_TEL,
                      PHONE=PHONE, MORE=more,
                      SIDEBAR=sidebar(D, photo_cap=strip(svc["short"])),
                      CTA=cta_strip(D), FOOT=footer(D))
    BUILT.append(write("blog/%s.html" % p["slug"], html))


for post in POSTS:
    article(post)


# ----------------------------------------------------------------------
# Blog index
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
    title="Blog | " + NAME + " Etobicoke",
    desc=("Practical guides on house cleaning, deep cleans, move outs, carpets and seasonal resets in "
          "Etobicoke and Toronto, from the crew that does the work."),
    canonical=BASE + "/blog/index.html", depth=D,
    extra_ld=ld_breadcrumb([("Blog", "blog/index.html")]),
) + hero_small(
    D, [("Blog", "blog/index.html")],
    "Notes From", "THE JOB",
    "What we have learned keeping homes in shape across the west end. No filler, no listicles, just the things clients ask us on site.",
    media="property-exterior",
) + """
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Articles</span>
        <h2>Guides and checklists</h2>
        <p>Written from the work, not from a keyword list.</p>
      </div>
      <div class="grid grid-3">{CARDS}</div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">The work itself</span>
        <h2>Around an Etobicoke home</h2>
      </div>
      {STRIP}
    </div>
  </section>

{CTA}{FOOT}""".format(CARDS=cards,
                      STRIP=photo_strip(D, ["kitchen-detail", "bathroom-result",
                                            "window-cleaning", "carpet-cleaning"]),
                      CTA=cta_strip(D), FOOT=footer(D))

BUILT.append(write("blog/index.html", index))

if __name__ == "__main__":
    for b in BUILT:
        print("built", b)
