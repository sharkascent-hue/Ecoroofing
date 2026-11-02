#!/usr/bin/env python3
"""Builds the Eco Roofing site: every page shares one header, footer and set of sections.
Edit the content below, then run:  python3 build.py   (writes the .html files next to this script)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://ecoroofinganddrivewayrestorations.com'  # change to the new domain when it's bought
PHONE, TEL, EMAIL = '087 130 6744', 'tel:+353871306744', 'ecoroofingandrestoration@outlook.com'
WAURL = 'https://wa.me/353871306744'
NAME = 'Eco Roofing'

# ---------- icons ----------
def svg(body, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>'
I = {
    'arrow': svg('<path d="M5 12h14M13 6l6 6-6 6"/>', 'arr'),
    'arrowup': svg('<path d="M7 17L17 7M8 7h9v9"/>'),
    'phone': svg('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>'),
    'mail': svg('<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/>'),
    'pin': svg('<path d="M12 22s-8-6.6-8-12a8 8 0 0 1 16 0c0 5.4-8 12-8 12z"/><circle cx="12" cy="10" r="3"/>'),
    'check': svg('<path d="M20 6L9 17l-5-5"/>'),
    'chev': svg('<path d="M6 9l6 6 6-6"/>'),
    'x': svg('<path d="M18 6L6 18M6 6l12 12"/>'),
    'left': svg('<path d="M15 18l-6-6 6-6"/>'),
    'right': svg('<path d="M9 18l6-6-6-6"/>'),
    'bolt': svg('<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>'),
    'shield': svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>'),
    'quote': svg('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>'),
    'star': svg('<path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>'),
    'clock': svg('<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>'),
    'house': svg('<path d="M3 11l9-8 9 8"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/>'),
    'wrench': svg('<path d="M14.7 6.3a4 4 0 0 0 5 5L22 14l-8 8-2.3-2.3a4 4 0 0 0-5-5L2 10l8-8z" transform="scale(.9) translate(1.3 1.3)"/>'),
    'layers': svg('<path d="M12 2l10 5-10 5L2 7z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/>'),
    'drop': svg('<path d="M12 2.7l5.7 5.6a8 8 0 1 1-11.4 0z"/>'),
    'chimney': svg('<path d="M3 12l9-8 9 8"/><path d="M15 6.5V3h3v6"/><path d="M5 10.5V21h14V10.5"/>'),
    'gutter': svg('<path d="M3 6h18v3a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3z"/><path d="M17 12v9M7 15v2M11 15v4"/>'),
    'storm': svg('<path d="M19 16.9A5 5 0 0 0 18 7h-1.3A8 8 0 1 0 4 15.3"/><path d="M13 11l-4 6h6l-4 6"/>'),
    'roof': svg('<path d="M2 12L12 3l10 9"/><path d="M6 8.5V5h3"/><path d="M5 12v9h14v-9"/>'),
    'hammer': svg('<path d="M15 12l-8.5 8.5a2.1 2.1 0 0 1-3-3L12 9"/><path d="M17.6 15L22 10.6M20.9 11.7l-4.6-4.6a3 3 0 0 0-2.1-.9h-1.8L10 4l1.8-1.8h3.5a6 6 0 0 1 4.2 1.8l2.6 2.6"/>'),
    'chat': svg('<path d="M21 11.5a8.4 8.4 0 0 1-12.3 7.4L3 21l2-5.4A8.4 8.4 0 1 1 21 11.5z"/>'),
    'search': svg('<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>'),
    'broom': svg('<path d="M19.4 2.6l-7.8 7.8"/><path d="M11 9l4 4-3.5 8.5L3 13z"/><path d="M7 17l-2 2"/>'),
    'leaf': svg('<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.4 5.2-6.1C9.6 14.4 12 13 13 11"/>'),
    'recycle': svg('<path d="M7 19H4.8a1.8 1.8 0 0 1-1.6-2.7l3.9-6.7M11 19h8.2a1.8 1.8 0 0 0 1.6-2.7l-1.2-2.1M14 16l-3 3 3 3M8.3 13.6L7.1 9.2l-4.4 1.2M9.3 6.4l1.1-2a1.8 1.8 0 0 1 3.1 0l3.8 6.6M13.4 9.6l3.9 1.1 1.2-4.4"/>'),
    'fb': svg('<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>'),
}
WA = '<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.7c-2 0-4-.5-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.7 10.7 0 1 1 16 26.7zm5.9-8c-.3-.2-1.9-1-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7 0a8.8 8.8 0 0 1-4.4-3.8c-.3-.6.3-.5 1-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.7 3.7 0 0 0-1.1 2.7 6.4 6.4 0 0 0 1.3 3.4 14.7 14.7 0 0 0 5.7 5c2.1.9 2.9 1 4 .8a3.4 3.4 0 0 0 2.2-1.6 2.8 2.8 0 0 0 .2-1.6c0-.2-.3-.3-.6-.5z"/></svg>'
HOUSE_SVG = '<svg class="house" viewBox="0 0 400 260" fill="none" stroke="#fff" stroke-width="22" stroke-linejoin="miter"><path d="M10 250L170 40l160 210"/><path d="M215 60l45-35 130 225"/><path d="M290 70V20h34v95"/></svg>'

# ---------- content (from ecoroofinganddrivewayrestorations.com; roofing only) ----------
SERVICES = [
    dict(slug='roof-repairs', name='Roof Repairs', short='Roof Repairs', icon='hammer',
         card='repairs-card.jpg', img='repairs.jpg',
         summary='Expert repairs for leaks, storm damage, slipped or broken tiles, ridge tiles and flashing. We find the root cause and fix it properly, with a free inspection first.',
         h1='Roof repairs Dublin.', lead='Leaks, storm damage, missing tiles and worn flashing repaired properly, across Dublin, Wicklow, Kildare, Meath and Louth.',
         eyebrow='Roof repair specialists', h2='Small problems fixed before they get expensive.',
         body=['Even minor roof damage can lead to major problems if it is left. We repair everything from missing or broken tiles to storm damage and persistent leaks, for homes and businesses across Dublin and the surrounding counties.',
               'Every repair starts with a thorough inspection to find the real cause, whether that is a cracked ridge tile, deteriorated flashing or damaged felt underneath. We use quality, eco-friendly materials so the fix lasts.',
               'We arrive on time, work efficiently and leave your property clean and tidy. All repair work is guaranteed and carried out by fully insured roofers, and you only pay for the work that is genuinely needed.'],
         feats_title='The repairs we carry out every week', feats_eyebrow='Roof repair services',
         feats=[('drop', 'Leaking roofs', 'We trace where the water is really getting in and repair the source, not just the stain.'),
                ('roof', 'Slipped & broken tiles', 'Missing, cracked and slipped tiles and slates replaced to match your roof.'),
                ('storm', 'Storm damage', 'Wind and storm damage made safe quickly, then repaired properly.'),
                ('shield', 'Flashing & ridges', 'Worn lead flashing and loose ridge tiles renewed and re-bedded.')],
         close=('Roof repairs', 'Repaired right, the first time.', 'From a single slipped tile to serious storm damage, we inspect properly, explain what we find and repair it to last. Free inspection and an honest quote before any work starts.')),
    dict(slug='roof-replacement', name='Roof Replacement & Re-roofing', short='Roof Replacement', icon='roof',
         card='replace-card.jpg', img='replace.jpg',
         summary='Complete roof replacement and re-roofing with natural slate, concrete or clay tiles: old roof stripped, timbers checked, new membrane, battens and covering.',
         h1='Roof replacement & re-roofing Dublin.', lead='When a roof has reached the end of its life, a full replacement is the most cost-effective long-term fix. Built to last decades.',
         eyebrow='Roof replacement', h2='A new roof, done properly from the timbers up.',
         body=['When your roof has reached the end of its lifespan, a complete replacement is the most cost-effective long-term solution. We re-roof houses and commercial buildings throughout Dublin and the surrounding counties.',
               'We work with natural slate, concrete tiles, clay tiles and modern alternatives, and we will advise on the best choice for your property, budget and the look you want, favouring eco-friendly and sustainable options where we can.',
               'Every re-roof is done properly: old materials removed and recycled where possible, timbers inspected and repaired, new breathable membrane and battens fitted, then your new roof laid, all in line with Irish building regulations.'],
         feats_title='Every stage of your new roof, handled', feats_eyebrow='What’s included',
         feats=[('layers', 'Strip & recycle', 'Old tiles and felt removed and recycled wherever possible.'),
                ('house', 'Timber check', 'Rafters and timbers inspected and repaired before anything goes back on.'),
                ('shield', 'Membrane & battens', 'New breathable membrane and treated battens fitted throughout.'),
                ('roof', 'Slate or tile finish', 'Natural slate, concrete or clay tiles laid and finished to a high standard.')],
         close=('Re-roofing', 'A roof that will see out the decades.', 'From period terraces in the city to modern homes in the suburbs, we deliver a weatherproof new roof with a clear quote and timeline up front.')),
    dict(slug='flat-roofing', name='Flat Roof Installation', short='Flat Roofing', icon='layers',
         card='flat-card.jpg', img='flat.jpg',
         summary='Modern flat roofs for extensions, garages and dormers in EPDM rubber, GRP fibreglass and torch-on felt, designed to last 25+ years.',
         h1='Flat roofing Dublin.', lead='EPDM rubber, GRP fibreglass and torch-on felt flat roofs for extensions, garages, dormers and commercial buildings.',
         eyebrow='Flat roof installation', h2='Flat roofs that stay watertight.',
         body=['Flat roofs need specialist knowledge and the right materials to stay watertight. We install modern flat roofing systems in EPDM rubber membrane, GRP fibreglass and torch-on felt for homes and businesses across Dublin.',
               'Whether it is a kitchen extension, garage, dormer or commercial building, we tailor the system to the job for strong weatherproofing and insulation. Our flat roofs are designed to last 25 years or more with minimal maintenance.',
               'We build proper falls into every flat roof to stop water ponding, one of the most common causes of failure, and finish with quality edge trims and upstands. Installations come with manufacturer-backed warranties.'],
         feats_title='Flat roofing systems we install', feats_eyebrow='Flat roof services',
         feats=[('layers', 'EPDM rubber', 'Single-piece rubber membranes with a long, low-maintenance life.'),
                ('shield', 'GRP fibreglass', 'Seamless fibreglass roofs with a clean finish and long guarantees.'),
                ('roof', 'Torch-on felt', 'Multi-layer torch-on systems for tough, cost-effective flat roofs.'),
                ('drop', 'Drainage & falls', 'Correct falls and outlets so water runs off and never ponds.')],
         close=('Flat roofing', 'Built not to pond, leak or lift.', 'Extensions, garages, dormers and commercial roofs, installed with proper falls, quality trims and a manufacturer-backed warranty.')),
    dict(slug='slate-tile-roofing', name='Slate & Tile Roofing', short='Slate & Tile Roofing', icon='roof',
         card='slate-card.jpg', img='slate.jpg',
         summary='New slate and tile roofs and expert repairs in natural Irish and Welsh slate, concrete and clay tiles, including reclaimed slate for period homes.',
         h1='Slate & tile roofing Dublin.', lead='Natural slate, concrete and clay tile roofs fitted and repaired by skilled roofers, from period homes to modern builds.',
         eyebrow='Slate & tile roofing', h2='Traditional craft, modern standards.',
         body=['Ireland has a proud tradition of slate and tile roofing, and we preserve it while using modern best practice. Our roofers have years of experience with natural Irish and Welsh slate, concrete tiles and clay tiles.',
               'We fit new slate and tile roofs and carry out expert repairs, from authentic restoration with reclaimed slate on period properties to new tiled roofs on modern homes.',
               'Slates are cut and graded precisely and fixed with copper or stainless nails and hooks for longevity, over breathable underlay to prevent condensation. A well-laid slate or tile roof can last 75 to 100 years, one of the most sustainable roofing choices there is.'],
         feats_title='Slate and tile work we do', feats_eyebrow='Slate & tile services',
         feats=[('roof', 'Natural slate', 'Irish and Welsh slate, cut, graded and fixed by hand.'),
                ('house', 'Period homes', 'Reclaimed slate sourced to match older and protected roofs.'),
                ('layers', 'Concrete & clay tiles', 'New tiled roofs in the profile and colour you want.'),
                ('wrench', 'Slate & tile repairs', 'Slipped slates and broken tiles replaced to blend in.')],
         close=('Slate & tile', 'A roof that lasts a lifetime.', 'Fitted with the right fixings and breathable underlay, a slate or tile roof can last 75 to 100 years. Get expert advice and a free quote.')),
    dict(slug='felt-roofing', name='Felt Roofing', short='Felt Roofing', icon='layers',
         card='felt-card.jpg', img='felt.jpg',
         summary='Torch-on and pour-and-roll felt roofing for flat and low-pitch roofs, sheds, garages and commercial roofs, with a 20+ year lifespan.',
         h1='Felt roofing Dublin.', lead='High-performance torch-on felt roofs for garages, sheds, extensions and commercial flat roofs.',
         eyebrow='Felt roofing', h2='Cost-effective felt roofs, built to last.',
         body=['Felt roofing is one of the most popular and cost-effective choices for flat and low-pitch roofs in Ireland. We install and repair high-performance torch-on and pour-and-roll bitumen systems.',
               'Modern felt is a long way from the basic material of the past. We use premium SBS-modified bitumen felts with excellent flexibility and UV resistance, giving a lifespan of 20 years or more when properly installed.',
               'From small sheds and garages to large commercial roofs, we prepare the deck properly, lay underlays and cap sheets correctly and detail every upstand, pipe and edge, all to manufacturer specification and fully guaranteed.'],
         feats_title='Felt roofing services', feats_eyebrow='Felt roofing',
         feats=[('roof', 'Torch-on felt', 'Multi-layer SBS-modified felt systems, torched on by experienced roofers.'),
                ('house', 'Garages & sheds', 'Leaking garage and shed roofs re-felted, often in a single day.'),
                ('layers', 'Commercial roofs', 'Larger flat roofs re-felted with minimal disruption.'),
                ('wrench', 'Felt repairs', 'Blisters, splits and lifted edges repaired properly.')],
         close=('Felt roofing', 'Bone dry, year after year.', 'Honest advice on repair versus re-felt, competitive pricing and work done to manufacturer specification.')),
    dict(slug='fascias-soffits-guttering', name='Fascias, Soffits & Guttering', short='Fascias, Soffits & Guttering', icon='gutter',
         card='gutter-card.jpg', img='gutter.jpg',
         summary='Maintenance-free uPVC and aluminium fascias, soffits, gutters and downpipes in white, black, anthracite and rosewood.',
         h1='Fascias, soffits & guttering Dublin.', lead='Rotting timber and leaking gutters replaced with maintenance-free uPVC and aluminium roofline.',
         eyebrow='Roofline', h2='A roofline that protects your home and looks new.',
         body=['Fascias, soffits and guttering protect your home from water damage and give the roofline a clean, finished look. We supply and fit quality uPVC and aluminium roofline across Dublin and the surrounding counties.',
               'Rotting timber fascias and blocked or leaking gutters can cause damp walls, foundation problems and timber decay. We remove the old roofline, check the rafter feet and timber, and fit new maintenance-free fascias, soffits and gutters.',
               'Choose from white, black, anthracite grey or rosewood to suit your home. Every system is fitted with proper brackets, joints and outlets so rainwater is carried safely away.'],
         feats_title='Complete roofline protection', feats_eyebrow='Roofline services',
         feats=[('house', 'Fascias & soffits', 'Maintenance-free uPVC boards that never need painting.'),
                ('gutter', 'Gutters', 'New seamless-look guttering that carries rain away properly.'),
                ('drop', 'Downpipes', 'Downpipes placed to keep water off walls and foundations.'),
                ('wrench', 'Repairs & cleaning', 'Leaking joints fixed and blocked gutters cleared.')],
         close=('Roofline', 'Transform the look of your home.', 'Our roofline packages give excellent value and real weather protection. Ask for a free quote and colour options.')),
    dict(slug='chimney-repairs', name='Chimney Repairs & Pointing', short='Chimney Repairs', icon='chimney',
         card='chimney-card.jpg', img='chimney.jpg',
         summary='Chimney re-pointing, lead flashing renewal, cowls, capping and full rebuilds, stopping one of the most common causes of damp in Irish homes.',
         h1='Chimney repairs Dublin.', lead='Re-pointing, lead flashing, cowls and rebuilds to stop leaks and damp at the stack.',
         eyebrow='Chimney repairs', h2='Stop the leak at the stack.',
         body=['Chimney problems are one of the most common causes of roof leaks and damp in Irish homes. We re-point stacks, renew flashing, fit cowls and caps and rebuild chimneys where needed.',
               'Over time the mortar joints in a chimney break down in the Irish weather and let water into the brickwork. We rake out the old mortar and re-point with a durable, weather-resistant mix.',
               'We also renew lead flashing, the critical joint where the chimney meets the roof, using traditional leadwork for a watertight seal. All chimney work is done safely from proper scaffolding.'],
         feats_title='Common chimney problems, properly fixed', feats_eyebrow='Chimney services',
         feats=[('hammer', 'Re-pointing', 'Crumbling mortar raked out and re-pointed to keep water out.'),
                ('shield', 'Lead flashing', 'Leadwork renewed where the stack meets the roof.'),
                ('chimney', 'Cowls & capping', 'Pots secured, cowls fitted and unused flues capped.'),
                ('house', 'Rebuilds', 'Cracked or leaning stacks taken down and rebuilt.')],
         close=('Chimneys', 'Damp gone for good.', 'Free inspection, an honest assessment and photos of the work from up on the scaffold, so you can see exactly what was done.')),
    dict(slug='roof-cleaning', name='Roof Cleaning & Moss Removal', short='Roof Cleaning & Moss Removal', icon='broom',
         card='clean-card.jpg', img='clean.jpg',
         summary='Moss, algae and lichen removed safely with soft washing or careful cleaning, then a biocide treatment that stops regrowth for up to five years.',
         h1='Roof cleaning & moss removal Dublin.', lead='Moss, algae and lichen removed safely, then treated to keep your roof clean for years.',
         eyebrow='Roof cleaning & treatment', h2='A clean roof looks better and lasts longer.',
         body=['Ireland’s damp climate is perfect for moss, algae and lichen, and over time they hold water, block gutters and damage tiles. Our roof cleaning restores your roof’s appearance and extends its life.',
               'We assess your roof and its material first, then use the right method, from gentle soft washing for delicate slate to careful mechanical cleaning for concrete tiles, removing years of growth without damaging the roof.',
               'Afterwards we apply a professional biocide treatment that kills remaining spores and helps prevent regrowth for up to five years. It is environmentally responsible and safe for surrounding plants when applied by our trained team.'],
         feats_title='How we clean your roof', feats_eyebrow='Roof cleaning',
         feats=[('search', 'Roof assessment', 'We check the roof type and condition before choosing a method.'),
                ('broom', 'Moss removal', 'Moss and lichen removed by hand and soft wash, not blasted.'),
                ('drop', 'Biocide treatment', 'Eco-conscious treatment that stops regrowth for up to five years.'),
                ('gutter', 'Gutters cleared', 'All the debris cleared from gutters and downpipes after.')],
         close=('Roof cleaning', 'Like a brand new roof.', 'A clean roof drains properly, avoids frost damage and transforms the look of your home. Book a free roof inspection today.')),
]
PAIRS = [('p1a.jpg', 'p1b.jpg', 'New battens on, ready for tiles', 'Finished grey tiled roof'),
         ('p2a.jpg', 'p2b.jpg', 'Membrane and battens around the Velux', 'Finished red tiles with Velux'),
         ('p3a.jpg', 'p3b.jpg', 'Re-roof under way', 'New interlocking tiles and ridge'),
         ('p4a.jpg', 'p4b.jpg', 'Tiles going on', 'Completed roof and dry ridge')]
REVIEWS = [
    ('Seán Murphy', 'Drumcondra, Dublin 9', 'Roof repairs', 'Absolutely brilliant job on our roof. Had a bad leak that two other companies couldn’t fix properly. Eco Roofing came out, found the problem straight away and had it sorted within the day. Very clean workers, fair price, and the roof hasn’t leaked since.'),
    ('Aoife Byrne', 'Blackrock, Co. Dublin', 'Roof replacement', 'We had our entire roof replaced and couldn’t be happier with the result. The team were professional from start to finish, arrived on time every morning and kept the site spotless. The new slate roof looks stunning.'),
    ('Padraig O’Sullivan', 'Swords, Dublin', 'Flat roof', 'Had Eco Roofing install a flat roof on our new kitchen extension. The whole process was seamless, from the initial survey to the final inspection. The GRP fibreglass system comes with a 25-year guarantee. Excellent value.'),
    ('Siobhán Kelly', 'Rathmines, Dublin 6', 'Slate roofing', 'Our Victorian terrace needed specialist slate work and Eco Roofing were perfect for the job. They sourced matching reclaimed Welsh slate and the craftsmanship was outstanding. True professionals.'),
    ('Ciarán Doyle', 'Bray, Co. Wicklow', 'Felt roofing', 'The lads did a great job on our garage flat roof. It had been leaking for years. New torch-on felt system installed in one day, and it’s been bone dry ever since. Very reasonable price too.'),
    ('Niamh Walsh', 'Malahide, Dublin', 'Fascias & guttering', 'Had all new fascias, soffits and guttering fitted around the house. What a difference! The old timber was rotting. Now the whole roofline looks brand new, and the team were very tidy and respectful of our garden.'),
    ('Declan Fitzgerald', 'Lucan, Dublin', 'Chimney repairs', 'Our chimney was causing damp in the bedroom for ages. They re-pointed the entire stack and replaced the lead flashing. Problem solved. They even showed us photos of the work from the scaffolding. Very transparent.'),
    ('Orla McCarthy', 'Greystones, Co. Wicklow', 'Roof cleaning', 'The roof cleaning service was incredible. Our roof was covered in moss. After the clean and biocide treatment it looks like a brand new roof. We’ve had neighbours asking who did it.'),
]
AREAS = [('Dublin', ['Dublin City', 'Drumcondra', 'Rathmines', 'Clontarf', 'Swords', 'Malahide', 'Lucan', 'Blackrock', 'Dún Laoghaire', 'Tallaght']),
         ('Wicklow & Kildare', ['Bray', 'Greystones', 'Wicklow Town', 'Naas', 'Celbridge', 'Maynooth', 'Leixlip']),
         ('Meath & Louth', ['Navan', 'Ashbourne', 'Ratoath', 'Dunboyne', 'Drogheda', 'Dundalk'])]
STEPS = [('Free inspection', 'We inspect your roof, find the real cause of the problem and photograph anything that needs attention.'),
         ('Honest quote', 'We explain what we found, recommend the right fix and give you a clear, transparent written quote. No hidden costs.'),
         ('Quality work', 'Our insured roofers do the job properly with eco-conscious materials, recycle what we can and leave your property spotless.')]
SERVICE_OPTS = [s['short'] for s in SERVICES] + ['Other']
FAQ = [
    ('How much does a roof repair cost in Dublin?', 'Small repairs such as replacing slipped tiles or re-sealing flashing usually cost a few hundred euro. Bigger repairs and replacements depend on the size and condition of the roof. We inspect for free and give you a clear written quote before any work starts.'),
    ('Is the roof inspection and quote free?', 'Yes. Inspections and quotes are free and there is no obligation.'),
    ('What makes you an eco roofing company?', 'We use sustainable, recyclable materials where we can, recycle old tiles, slates and felt instead of dumping them, use environmentally responsible roof treatments, and repair rather than replace when a repair will do the job.'),
    ('Does roof cleaning damage the tiles?', 'Not when it is done properly. We choose the method to suit your roof, soft washing for delicate slate and careful cleaning for concrete tiles, and never blast at high pressure. A biocide treatment then keeps moss away for up to five years.'),
    ('Which areas do you cover?', 'All of Dublin, plus Wicklow, Kildare, Meath and Louth, including Bray, Greystones, Naas, Celbridge, Maynooth, Navan, Ashbourne and Drogheda.'),
    ('Are you insured and is the work guaranteed?', 'Yes. We carry full public liability insurance and all our work comes with a guarantee.'),
]
AREA_TOWNS = [t for _, ts in AREAS for t in ts]
KW = 'roofers Dublin, eco roofing Dublin, roof repairs Dublin, roof replacement Dublin, flat roofing Dublin, slate roofing Dublin, felt roofing Dublin, roof cleaning Dublin, moss removal Dublin, chimney repairs Dublin, fascias soffits guttering Dublin, roofers Wicklow, roofers Kildare, roofers Meath'

AREA_LD = ','.join(f'{{"@type":"Place","name":"{t}"}}' for t in ['Dublin', 'County Wicklow', 'County Kildare', 'County Meath', 'County Louth'] + AREA_TOWNS)

# ---------- building blocks ----------
from PIL import Image
_DIMS = {}
def dims(f):
    if f not in _DIMS:
        with Image.open(os.path.join(ROOT, 'img', f)) as im: _DIMS[f] = im.size
    return _DIMS[f]

def pic(p, f, alt, chip='', cls=''):
    """A photo box shaped like the photo itself, so nothing gets cropped."""
    w, h = dims(f)
    c = f'<span class="chip">{chip}</span>' if chip else ''
    return f'<div class="ph fit{" " + cls if cls else ""}" style="aspect-ratio:{w}/{h}" data-clip><img src="{p}img/{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy">{c}</div>'

def faq_ld():
    import json
    return json.dumps({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]})

def head(p, title, desc, path, kw=''):
    canon = SITE + '/' + path
    fonts = 'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap'
    return f"""<!doctype html>
<html lang="en-IE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw or KW}">
<meta name="geo.region" content="IE-D"><meta name="geo.placename" content="Dublin"><meta name="geo.position" content="53.3498;-6.2603"><meta name="ICBM" content="53.3498, -6.2603">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#ffffff">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/img/v3.jpg"><meta property="og:url" content="{canon}"><meta property="og:locale" content="en_IE">
<link rel="icon" href="{p}img/icon-192.png"><link rel="apple-touch-icon" href="{p}img/icon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin><link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="preload" as="style" href="{fonts}" onload="this.onload=null;this.rel='stylesheet'"><noscript><link rel="stylesheet" href="{fonts}"></noscript>
<link rel="stylesheet" href="{p}assets/style.css?v=3">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"RoofingContractor","name":"Eco Roofing","alternateName":"Eco Roofing and Driveway Restoration","url":"{SITE}/","telephone":"+353871306744","email":"{EMAIL}","image":"{SITE}/img/v3.jpg","logo":"{SITE}/img/og-logo.jpg","address":{{"@type":"PostalAddress","addressLocality":"Dublin","addressRegion":"Co. Dublin","addressCountry":"IE"}},"priceRange":"€€","areaServed":[{AREA_LD}],"knowsAbout":["Roof repairs","Roof replacement","Re-roofing","Flat roofing","EPDM rubber roofing","GRP fibreglass roofing","Felt roofing","Slate roofing","Tile roofing","Chimney repairs","Fascias, soffits and guttering","Roof cleaning","Moss removal"]}}</script>"""

def brand(p, cls='brand'):
    return f'<a class="{cls}" href="{p}" aria-label="Eco Roofing home"><img src="{p}img/mark-sm.webp" alt="" width="480" height="318"><span class="wm"><b>ECO <i>ROOFING</i></b><small>Roofing specialists · Dublin</small></span></a>'

def header(p, active):
    def on(k): return ' class="on" aria-current="page"' if k == active else ''
    menu = ''.join(f'<a href="{p}{s["slug"]}/"><i>{I[s["icon"]]}</i>{s["name"]}</a>' for s in SERVICES)
    subs = ''.join(f'<a href="{p}{s["slug"]}/">{s["name"]}</a>' for s in SERVICES)
    svc_on = ' class="on"' if active == 'services' else ''
    return f"""<header class="hdr"><div class="wrap">
{brand(p)}
<nav class="nav" aria-label="Main">
<a href="{p}"{on('home')}>Home</a>
<a href="{p}about/"{on('about')}>About</a>
<div class="dd"><a href="{p}services/"{svc_on}>Services {I['chev']}</a><div class="menu">{menu}</div></div>
<a href="{p}gallery/"{on('gallery')}>Gallery</a>
<a href="{p}roofers-dublin/"{on('areas')}>Areas</a>
<a href="{p}contact/"{on('contact')}>Contact</a>
</nav>
<a class="tel" href="{TEL}">{I['phone']}<span data-cfg="phone">{PHONE}</span></a>
<a class="btn btn-blue qbtn" href="#quote" data-quote aria-expanded="false" aria-controls="qdrop"><span class="q1">Get a free quote</span><span class="q2">Free quote</span> {I['chev']}</a>
<button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span></button>
</div>
{qdrop(p)}
</header>
<nav class="mnav" aria-label="Mobile">
<a class="ml" href="{p}">Home <small>01</small></a>
<a class="ml" href="{p}about/">About <small>02</small></a>
<div class="macc"><button class="ml mtog" type="button" aria-expanded="false">Services <i>{I['right']}</i></button><div class="subs"><a href="{p}services/">All services</a>{subs}</div></div>
<a class="ml" href="{p}gallery/">Gallery <small>03</small></a>
<a class="ml" href="{p}roofers-dublin/">Areas we cover <small>04</small></a>
<a class="ml" href="{p}contact/">Contact <small>05</small></a>
<a class="btn btn-blue" href="#quote" data-quote>Get a free quote</a>
<a class="btn btn-ghost" href="{TEL}" style="margin-top:12px">{I['phone']} Call {PHONE}</a>
<div class="mfoot">Dublin, Wicklow, Kildare, Meath &amp; Louth</div>
</nav>"""

def select(name='service'):
    return f'<select name="{name}" required><option value="">Choose a service</option>' + ''.join(f'<option>{o}</option>' for o in SERVICE_OPTS) + '</select>'

def form(p, kind='quote', title='Request a free quote', sub='Free, no-obligation written quotation. We aim to respond to every enquiry within 24 hours.'):
    if kind == 'callback':
        fields = f'''<label class="f"><span>Name</span><input name="name" autocomplete="name" required></label>
<label class="f"><span>Phone</span><input name="phone" type="tel" autocomplete="tel" required></label>
<label class="f full"><span>Email</span><input name="email" type="email" autocomplete="email" required></label>'''
        btn = 'Request a callback'
    else:
        email = '<label class="f"><span>Email</span><input name="email" type="email" autocomplete="email" required></label>' if kind == 'full' else ''
        svc_cls = 'f' if kind == 'full' else 'f full'
        fields = f'''<label class="f"><span>Name</span><input name="name" autocomplete="name" required></label>
<label class="f"><span>Phone</span><input name="phone" type="tel" autocomplete="tel" required></label>
{email}<label class="{svc_cls}"><span>Service</span>{select()}</label>
<label class="f full"><span>Message</span><textarea name="message" placeholder="Tell us about the problem or project" required></textarea></label>'''
        btn = 'Get a quote'
    return f'''<form class="formcard" data-form novalidate>
<h3>{title}</h3><p class="sub">{sub}</p>
<div class="fmsg" role="status"></div>
<div class="fgrid">{fields}</div>
<input class="hp" name="botcheck" tabindex="-1" autocomplete="off" aria-hidden="true">
<button class="btn btn-blue" type="submit">{btn} {I['arrow']}</button>
<p class="fnote">Your details are kept private. See our <a href="{p}privacy-policy/">privacy policy</a>.</p>
</form>'''

def qdrop(p):
    """Quote panel that drops down from under the header."""
    f = form(p, 'full', 'Get a free quote', 'Free inspection and an honest written quote. We reply within 24 hours.').replace('<form class="formcard"', '<form class="formcard" id="quote"')
    perks = '<ul class="qperks">' + ''.join(f'<li>{I["check"]}{t}</li>' for t in ['Free inspection', 'Honest quote', 'Fully insured', 'Eco-friendly']) + '</ul>'
    f = f.replace('<div class="fmsg"', perks + '<div class="fmsg"', 1)
    return f"""<div class="qdrop" id="qdrop" aria-hidden="true" data-lenis-prevent><div class="wrap qdgrid">
<div class="qdside"><span class="eyebrow">Free quotes · no obligation</span><h3>Tell us about your roof.</h3>
<p>Free inspection and a clear, transparent quote with no hidden costs. Serving Dublin, Wicklow, Kildare, Meath &amp; Louth.</p>
<a class="qdl" href="{TEL}">{I['phone']}<span><b>Call {PHONE}</b><small>Talk to a roofer directly</small></span></a>
<a class="qdl wa" href="{WAURL}" data-href="whatsapp" target="_blank" rel="noopener">{WA}<span><b>WhatsApp a photo</b><small>Quickest way to a price</small></span></a>
<a class="qdl" href="mailto:{EMAIL}">{I['mail']}<span><b>Email us</b><small>{EMAIL}</small></span></a>
<button class="qdx" type="button" data-qclose>{I['x']} Close</button></div>
{f}</div></div>"""

def footer(p):
    svc = ''.join(f'<li><a href="{p}{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)
    return f"""<footer class="ftr"><div class="wrap">
<div class="cols">
<div><div class="fbrand">{brand(p, 'brand')}</div>
<p>Family-run, eco-friendly roofing across Dublin and the surrounding counties. Fully insured, free quotes and quality craftsmanship on every roof.</p>
<span class="h247">{I['leaf']} ECO-FRIENDLY ROOFING</span></div>
<div><h4>Useful Links</h4><ul><li><a href="{p}">Home</a></li><li><a href="{p}about/">About Us</a></li><li><a href="{p}services/">Services</a></li><li><a href="{p}gallery/">Gallery</a></li><li><a href="{p}roofers-dublin/">Roofers in Dublin</a></li><li><a href="{p}contact/">Contact Us</a></li></ul></div>
<div><h4>Services</h4><ul>{svc}</ul></div>
<div><h4>Contact Info</h4><ul class="ci">
<li>{I['phone']}<a href="{TEL}" data-cfg="phone">{PHONE}</a></li>
<li>{I['mail']}<a href="mailto:{EMAIL}" data-cfg="email" style="word-break:break-all">{EMAIL}</a></li>
<li>{I['pin']}<span>Serving Dublin, Wicklow, Kildare, Meath &amp; Louth</span></li>
<li>{I['clock']}<span>We reply within 24 hours</span></li></ul></div>
</div>
<div class="base"><span>Copyright © <span data-cfg="year">2026</span> Eco Roofing. All rights reserved.</span>
<nav><a href="{p}cookie-policy/">Cookie Policy</a><a href="{p}privacy-policy/">Privacy Policy</a></nav></div>
</div></footer>
<div class="fab"><a class="ph" href="{TEL}" aria-label="Call {PHONE}">{I['phone']}</a><a class="wa" href="{WAURL}" data-href="whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp us">{WA}</a></div>"""

def scripts(p):
    return f'''<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.18/dist/lenis.min.js" defer></script>
<script src="{p}assets/site.js?v=3" defer></script>'''

def page(path, active, title, desc, body, intro=False, kw='', ld=''):
    p = '../' * path.count('/')
    head_html = head(p, title, desc, path, kw)
    if ld:
        head_html += f'\n<script type="application/ld+json">{ld}</script>'
    if intro:
        head_html += '\n<script>try{if(!sessionStorage.getItem("eco_intro")||/[?&]intro/.test(location.search))document.documentElement.classList.add("intro")}catch(e){document.documentElement.classList.add("intro")}</script>'
    loader = ''
    if intro:
        # intro: the logo is there straight away, green leaves blow in and swirl into it, then the screen slides away left
        loader = f"""<div id="loader" aria-hidden="true">
<div class="box"><img class="mk" src="{p}img/mark.webp" alt="" width="1100" height="728">
<div class="word"><b>ECO <i>ROOFING</i></b><small>Roofing specialists · Dublin</small></div></div></div>"""
    intro_js = ('<script>' + open(os.path.join(ROOT, 'assets', 'intro.js'), encoding='utf-8').read() + '</script>') if intro else ''
    html = f'''{head_html}
</head>
<body>
{loader}{intro_js}
{header(p, active)}
<main>
{body(p)}
</main>
{footer(p)}
{scripts(p)}
</body>
</html>
'''
    out = os.path.join(ROOT, path, 'index.html') if path else os.path.join(ROOT, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('wrote', os.path.relpath(out, ROOT))

# ---------- sections ----------
def phero(p, crumb, h1, lead, img, extra=''):
    trail = ''.join(f'<span>/</span><a href="{p}{u}">{t}</a>' for t, u in crumb[:-1])
    return f"""<section class="phero">
<img class="bg" src="{p}img/{img}" alt="" fetchpriority="high">
<div class="wrap">
<div class="crumb"><a href="{p}">Home</a>{trail}<span>/</span><b>{crumb[-1][0]}</b></div>
<h1>{h1}</h1>
<p class="lead">{lead}</p>
{extra}
</div></section>"""

def marquee():
    items = ['Roof repairs', 'Re-roofing', 'Flat roofs', 'Slate & tile', 'Felt roofing', 'Roof cleaning & moss removal', 'Chimneys', 'Fascias & guttering', 'Free quotes']
    s = ''.join(f'<span>{t}</span>' for t in items)
    return f'<div class="marquee" aria-hidden="true"><div class="track">{s}{s}</div></div>'

def feats():
    f = [('leaf', 'Eco-Friendly', 'Sustainable materials'), ('quote', 'Free Quotes', 'Honest, no hidden costs'),
         ('shield', 'Fully Insured', 'Public liability cover'), ('pin', 'Local Experts', 'Dublin & 4 counties')]
    cards = ''.join(f'<div class="feat"><i>{I[a]}</i><div><b>{b}</b><span>{c}</span></div></div>' for a, b, c in f)
    return f'<section class="sec tight soft"><div class="wrap"><div class="feats" data-reveal="group">{cards}</div></div></section>'

def services_grid(p, title='Roofing done properly, the eco-friendly way.', head=True, only=None):
    cards = ''
    for i, s in enumerate(only or SERVICES, 1):
        cards += f"""<a class="scard" href="{p}{s['slug']}/"><img src="{p}img/{s['card']}" alt="{s['name']} in Dublin by Eco Roofing" loading="lazy">
<span class="num">0{i}</span><span class="go">{I['arrow']}</span>
<h3>{s['name']}</h3><p>{s['summary']}</p><span class="tlink">View service {I['arrow']}</span></a>"""
    hd = f"""<div class="sec-head"><div><span class="eyebrow">Our roofing services</span><h2 data-split>{title}</h2></div>
<a class="btn btn-line" href="{p}services/">All services {I['arrow']}</a></div>""" if head else ''
    return f'<section class="sec" id="services"><div class="wrap">{hd}<div class="sgrid s4" data-reveal="group">{cards}</div></div></section>'

def stages(p, soft=True, n=4):
    items = ''.join(f"""<figure class="stage"><div class="pair" style="--ar:{dims(a)[0]}/{dims(a)[1]}">
<div class="half" data-clip><img src="{p}img/{a}" alt="{ta}" loading="lazy"><span class="tag l">During</span></div>
<div class="half" data-clip><img src="{p}img/{b}" alt="{tb}, Eco Roofing" loading="lazy"><span class="tag r">Finished</span></div></div>
<figcaption>{tb}<span>{ta}</span></figcaption></figure>""" for a, b, ta, tb in PAIRS[:n])
    return f"""<section class="sec{' soft' if soft else ''}" id="work"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">Stage by stage</span><h2 data-split>From bare battens to a finished roof.</h2></div>
<p>Real re-roofing jobs, photographed while the work was under way and again when it was finished.</p></div>
<div class="stages" data-reveal="group">{items}</div></div></section>"""

def eco_band(p):
    pts = [('recycle', 'We recycle', 'Old tiles, slates and felt are recycled wherever possible instead of going to landfill.'),
           ('leaf', 'Greener materials', 'We source sustainable, recyclable materials and long-life products that need replacing less often.'),
           ('drop', 'Safe treatments', 'Our roof cleaning treatments are environmentally responsible and safe for your garden.'),
           ('wrench', 'Repair first', 'If a repair will do the job, we repair. We never sell you a new roof you don’t need.')]
    cards = ''.join(f'<div class="card"><span class="ico">{I[a]}</span><h3>{b}</h3><p>{c}</p></div>' for a, b, c in pts)
    return f"""<section class="sec deep eco"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">The eco promise</span><h2 data-split>Better for your home. Better for the planet.</h2></div>
<p>Quality roofing doesn’t have to cost the earth. Here’s what makes us different.</p></div>
<div class="cards" data-reveal="group">{cards}</div></div></section>"""

def steps():
    s = ''.join(f'<div class="step"><div class="n">0{i}</div><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(STEPS, 1))
    return f"""<section class="sec soft"><div class="wrap">
<div class="center" style="margin-bottom:48px"><span class="eyebrow">How we work</span><h2 data-split>Simple, honest and tidy.</h2></div>
<div class="steps" data-reveal="group">{s}</div></div></section>"""

def reviews(n=8):
    r = ''.join(f"""<div class="review"><div class="stars" aria-label="5 stars">★★★★★</div><q>{t}</q>
<div class="who"><span class="av">{nm[0]}</span><div><b>{nm}</b><span>{place}</span><br><span class="job">{job}</span></div></div></div>""" for nm, place, job, t in REVIEWS[:n])
    return f"""<section class="sec deep"><div class="wrap" style="position:relative;z-index:2">
<div class="sec-head"><div><span class="eyebrow">Customer reviews</span><h2 data-split>Trusted by homeowners across Dublin.</h2></div>
<p>What our customers say about the work, the tidiness and the price.</p></div>
<div class="rgrid" data-reveal="group">{r}</div></div></section>"""

def faq():
    q = ''.join(f'<details class="qa"><summary>{a}<i>{I["chev"]}</i></summary><p>{b}</p></details>' for a, b in FAQ)
    return f"""<section class="sec soft" id="faq"><div class="wrap split" style="align-items:start">
<div><span class="eyebrow">FAQ</span><h2 data-split>Roofing questions, answered.</h2>
<p>The questions homeowners ask us most. Anything else, call us on <a class="blue" href="{TEL}"><b>{PHONE}</b></a>.</p></div>
<div class="faq" data-reveal>{q}</div></div></section>"""

def areas(p, more=True):
    a = ''.join(f'<div class="area"><h3>{I["pin"]}{t}</h3><div class="chips">{"".join(f"<span>{x}</span>" for x in xs)}</div></div>' for t, xs in AREAS)
    return f"""<section class="sec"><div class="wrap">
<span class="eyebrow">Areas we serve</span><h2 data-split style="max-width:20ch">Roofers for Dublin and the surrounding counties.</h2>
<p>Based in Dublin, we cover the whole county plus Wicklow, Kildare, Meath and Louth.</p>
<div class="areas" data-reveal="group">{a}</div>
<div class="callcard" data-reveal><div><h3>Not sure if we cover your area?</h3><p>Give us a call and we’ll let you know straight away.</p></div>
<a class="btn btn-white" href="{TEL}">{I['phone']} Call {PHONE}</a></div>
{f'<p style="margin-top:22px"><a class="tlink" href="{p}roofers-dublin/">Roofers in Dublin: every area we cover {I["arrow"]}</a></p>' if more else ''}
</div></section>"""

def cta(p):
    return f"""<section class="cta">{HOUSE_SVG}<div class="wrap">
<div><span class="eyebrow">Free, no-obligation quote</span><h2 data-split>Ready to sort your roof?</h2>
<p>Tell us about the job and we’ll come back to you within 24 hours with a free inspection and an honest price.</p></div>
<div class="btn-row"><a class="btn btn-white" href="#quote" data-quote>Get a free quote {I['arrow']}</a><a class="btn btn-ghost" href="{TEL}">{I['phone']} {PHONE}</a></div>
</div></section>"""

def talk(p):
    return f"""<section class="sec"><div class="wrap"><div class="talk">
<div class="badge" data-reveal>{pic(p, 'feature2.jpg', 'New red tiled roof by Eco Roofing')}
<div class="in"><span class="eyebrow">Prefer to talk?</span><h3>Speak directly with a roofer.</h3>
<p>Honest advice and a free quote for your roof. No hidden costs and no pushy sales.</p>
<a class="btn btn-blue" href="{TEL}">{I['phone']} Call {PHONE}</a></div></div>
<div data-reveal>{form(p, 'callback', 'Request a callback', 'Leave your details and one of the team will call you back.')}</div>
</div></div></section>"""

# ---------- pages ----------
def home(p):
    trust = ''.join(f'<li>{I["check"]}{t}</li>' for t in ['Free inspections & honest quotes', 'Fully insured', 'Work guaranteed'])
    return f"""<section class="hero hvid">
<video class="bg" poster="{p}video/hero-poster.jpg" data-poster-m="{p}video/hero-m-poster.jpg" autoplay muted loop playsinline preload="auto" aria-hidden="true"><source src="{p}video/hero-m.mp4" type="video/mp4" media="(max-width:760px)"><source src="{p}video/hero-m.webm" type="video/webm" media="(max-width:760px)"><source src="{p}video/hero.webm" type="video/webm"><source src="{p}video/hero.mp4" type="video/mp4"></video>
<div class="wrap">
<div>
<div class="gbadge">{I['leaf']}<span><b>Eco-friendly</b> roofing · family-run · 15+ years</span></div>
<span class="eyebrow"><span class="lg">Dublin · Wicklow · Kildare · Meath · Louth</span><span class="sm">Dublin &amp; surrounding counties</span></span>
<h1>Dublin’s eco-friendly <span class="blue">roofing experts.</span></h1>
<p class="lead">Roof repairs, re-roofing, flat roofs, slate and tile, chimneys, guttering and roof cleaning. Fully insured, honest prices and quality craftsmanship, with less waste on every job.</p>
<div class="btn-row"><a class="btn btn-blue" href="#quote" data-quote>Get a free quote {I['arrow']}</a><a class="btn btn-ghost" href="{p}gallery/">See our work</a></div>
<ul class="trust">{trust}</ul>
</div>
<div class="hcard">
<span class="live"><i></i>Free inspections</span>
<h2>Free roof inspection &amp; quote</h2>
<ul class="ticks">{''.join(f"<li>{I['check']}{t}</li>" for t in ['No obligation, no hidden costs', 'Honest advice: repair before replace', 'Fully insured, work guaranteed', 'Reply within 24 hours'])}</ul>
<a class="btn btn-blue" href="#quote" data-quote>Get a free quote {I['chev']}</a>
<a class="btn btn-ghost" href="{TEL}">{I['phone']} {PHONE}</a>
<div class="hrev"><span class="stars">★★★★★</span><q>Had a bad leak that two other companies couldn’t fix. They found the problem straight away and had it sorted within the day.</q><span>Seán Murphy · Drumcondra</span></div>
</div>
</div>
<div class="scroll">Scroll</div>
</section>
{marquee()}
{feats()}
<section class="sec" id="about"><div class="wrap split">
<div>
<span class="eyebrow">About Eco Roofing</span>
<h2 data-split>A family-run roofing company built on trust.</h2>
<p class="lead" style="color:var(--ink)">Eco Roofing is a family-run business in Dublin with over 15 years’ experience, known for reliable work, quality craftsmanship and honest, transparent pricing.</p>
<p>We do everything from a single slipped tile to a complete new roof, for homes and businesses across Dublin, Wicklow, Kildare, Meath and Louth.</p>
<p>What sets us apart is how we work: sustainable materials where we can, old roofing recycled instead of dumped, and a repair-first approach that never sells you more than you need.</p>
<div class="callrow"><a class="btn btn-line" href="{p}about/">More about us {I['arrow']}</a>
<div><small>Prefer to call?</small><a class="num" href="{TEL}">{PHONE}</a></div></div>
</div>
<div class="collage">
<figure data-clip><img src="{p}img/tall.jpg" alt="New red tiled roof by Eco Roofing" width="{dims('tall.jpg')[0]}" height="{dims('tall.jpg')[1]}" loading="lazy"></figure>
<figure data-clip><img src="{p}img/c1.jpg" alt="New tiled roof on a Dublin home" loading="lazy"></figure>
<figure data-clip><img src="{p}img/c2.jpg" alt="Flat roof installed by Eco Roofing" loading="lazy"></figure>
<figure data-clip><img src="{p}img/c3.jpg" alt="Red tiled hip roof with new ridge" loading="lazy"></figure>
</div>
</div></section>
{services_grid(p)}
{eco_band(p)}
{stages(p)}
<section class="sec"><div class="wrap split">
<div>
<span class="eyebrow">Why choose us</span>
<h2 data-split>Quality roofs, honest prices, no mess.</h2>
<ul class="ticks big">{''.join(f"<li>{I['check']}<span><b>{a}</b> {b}</span></li>" for a, b in [('15+ years’ experience.', 'Thousands of happy customers across Dublin.'), ('Fully insured.', 'Full public liability insurance and health and safety certified.'), ('Skilled craftsmen.', 'Traditional skills and modern techniques on every roof.'), ('Guaranteed work.', 'We stand behind every job we do.'), ('Local knowledge.', 'We know Dublin’s housing, weather and building regulations.')])}</ul>
<div class="callrow"><a class="btn btn-blue" href="#quote" data-quote>Get a free quote {I['arrow']}</a><div><small>Prefer to call?</small><a class="num" href="{TEL}">{PHONE}</a></div></div>
</div>
{pic(p, 'feature.jpg', 'Eco Roofing re-roofing a house in Dublin', I['shield'] + 'Fully insured & guaranteed')}
</div></section>
{reviews(6)}
<section class="sec soft"><div class="wrap split">
<div>
<span class="eyebrow">Get in touch</span>
<h2 data-split>Free inspection, honest quote.</h2>
<p>Tell us what’s going on with your roof and we’ll get back to you within 24 hours. No obligation and no hidden costs.</p>
<ul class="ticks"><li>{I['phone']}<a href="{TEL}" data-cfg="phone">{PHONE}</a></li><li>{I['mail']}<a href="mailto:{EMAIL}" data-cfg="email" style="word-break:break-all">{EMAIL}</a></li><li>{I['pin']}Dublin, Wicklow, Kildare, Meath &amp; Louth</li></ul>
</div>
<div data-reveal>{form(p, 'full', 'Get a free quote')}</div>
</div></section>
{areas(p)}
{faq()}
{steps()}
{cta(p)}"""

def services_page(p):
    details = ''
    for i, s in enumerate(SERVICES, 1):
        details += f"""<div class="sdetail">{pic(p, s['card'], s['name'] + ' in Dublin by Eco Roofing')}
<div><div class="bign">0{i}</div><h2 style="font-size:clamp(1.6rem,2.6vw,2.2rem)">{s['name']}</h2><p>{s['summary']}</p>
<ul class="ticks">{''.join(f"<li>{I['check']}{f[1]}</li>" for f in s['feats'])}</ul>
<a class="btn btn-blue" href="{p}{s['slug']}/">View service {I['arrow']}</a></div></div>"""
    return f"""{phero(p, [('Services', 'services/')], 'Roofing services in Dublin.', 'Roof repairs, re-roofing, flat roofs, slate and tile, felt roofing, chimneys, fascias and guttering, and roof cleaning, across Dublin and the surrounding counties.', 'v2.jpg', f'<div class="btn-row"><a class="btn btn-blue" href="#quote" data-quote>Get a free quote {I["arrow"]}</a><a class="btn btn-ghost" href="{TEL}">{I["phone"]} {PHONE}</a></div>')}
{services_grid(p, title='What we do.')}
<section class="sec soft"><div class="wrap">
<div class="center" style="margin-bottom:60px"><span class="eyebrow">In detail</span><h2 data-split>Every roofing job, done properly.</h2></div>
{details}</div></section>
{eco_band(p)}
{reviews(4)}
{steps()}
{cta(p)}"""

def service_page(s):
    def body(p):
        feats_html = ''.join(f'<div class="card"><span class="ico">{I[a]}</span><h3>{b}</h3><p>{c}</p></div>' for a, b, c in s['feats'])
        paras = ''.join(f'<p>{x}</p>' for x in s['body'])
        others = [o for o in SERVICES if o is not s]
        ce, ch, ct = s['close']
        return f"""{phero(p, [('Services', 'services/'), (s['name'], s['slug'] + '/')], s['h1'], s['lead'], s['card'], f'<div class="btn-row"><a class="btn btn-blue" href="#quote" data-quote data-svc="{s["short"]}">Get a free quote {I["arrow"]}</a><a class="btn btn-ghost" href="{TEL}">{I["phone"]} Call {PHONE}</a></div>')}
{marquee()}
<section class="sec"><div class="wrap split">
<div><span class="eyebrow">{s['eyebrow']}</span><h2 data-split>{s['h2']}</h2>{paras}
<div class="callrow"><a class="btn btn-blue" href="#quote" data-quote data-svc="{s['short']}">Get a free quote {I['arrow']}</a><div><small>Prefer to call?</small><a class="num" href="{TEL}">{PHONE}</a></div></div></div>
{pic(p, s['img'], s['name'] + ' in Dublin by Eco Roofing', I[s['icon']] + s['name'])}
</div></section>
<section class="sec soft"><div class="wrap">
<div class="center" style="margin-bottom:48px"><span class="eyebrow">{s['feats_eyebrow']}</span><h2 data-split>{s['feats_title']}.</h2></div>
<div class="cards" data-reveal="group">{feats_html}</div></div></section>
{talk(p)}
{stages(p, n=2) if s['slug'] in ('roof-replacement', 'slate-tile-roofing', 'roof-repairs') else ''}
{reviews(4)}
<section class="sec"><div class="wrap split">
<div><span class="eyebrow">{ce}</span><h2 data-split>{ch}</h2><p>{ct}</p>
<ul class="ticks"><li>{I['check']}Free inspection &amp; honest quote</li><li>{I['check']}Fully insured, work guaranteed</li><li>{I['check']}Eco-friendly materials and recycling</li></ul></div>
<div data-reveal>{form(p, 'full', 'Get a free quote').replace(f'<option>{s["short"]}</option>', f'<option selected>{s["short"]}</option>')}</div></div></section>
{steps()}
<section class="sec soft"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">More services</span><h2 data-split>Other ways we can help.</h2></div><a class="btn btn-line" href="{p}services/">All services {I['arrow']}</a></div>
<div class="sgrid" data-reveal="group">{''.join(f'<a class="scard" href="{p}{o["slug"]}/" style="min-height:300px"><img src="{p}img/{o["card"]}" alt="" loading="lazy"><span class="go">{I["arrow"]}</span><h3>{o["name"]}</h3><span class="tlink">View service {I["arrow"]}</span></a>' for o in others[:3])}</div></div></section>
{cta(p)}"""
    return body

def about_page(p):
    vals = [('leaf', 'Sustainability', 'Eco-friendly materials and methods, recycling where possible and minimising waste on every project, to protect your home and the environment.'),
            ('star', 'Quality craftsmanship', 'Every job gets the same attention to detail, whether it’s a small repair or a full replacement. We never cut corners.'),
            ('chat', 'Customer satisfaction', 'From the first quote to the final clean-up, we communicate clearly, work efficiently and make sure you’re delighted.')]
    why = [('15+ years’ experience', 'Over a decade and a half in roofing, with thousands of satisfied customers across Dublin.'),
           ('Eco-friendly materials', 'Sustainable, recyclable and environmentally responsible materials on every job.'),
           ('Fully insured', 'Full public liability insurance and health and safety certified to the highest standards.'),
           ('Local knowledge', 'Deep knowledge of local architecture, weather and building regulations.'),
           ('Skilled craftsmen', 'Experienced tradesmen bringing traditional skills and modern techniques together.'),
           ('Guaranteed work', 'Comprehensive guarantees on all our work. We stand behind every project.')]
    return f"""{phero(p, [('About', 'about/')], 'A family-run roofing company built on trust.', 'Quality craftsmanship and sustainable roofing across Dublin and the surrounding counties for over 15 years.', 'v4.jpg')}
{marquee()}
<section class="sec"><div class="wrap split">
<div><span class="eyebrow">Our story</span><h2 data-split>Quality roofing, less waste.</h2>
<p>Eco Roofing was founded with a simple aim: the highest quality roofing, with as little impact on the environment as possible. As a proud family-run business based in Dublin, we bring a personal touch to every job.</p>
<p>With over 15 years in the roofing industry, our team has built a reputation for reliability, quality craftsmanship and honest, transparent pricing, for homeowners and businesses across Dublin, Wicklow, Kildare, Meath and Louth.</p>
<p>What sets us apart is our commitment to eco-friendly practice. We source sustainable materials, recycle old roofing wherever we can and keep looking for ways to reduce our footprint, without ever compromising on quality.</p>
<div class="btn-row" style="margin-top:26px"><a class="btn btn-blue" href="#quote" data-quote>Get a free quote {I['arrow']}</a><a class="btn btn-line" href="{p}gallery/">See our work</a></div></div>
{pic(p, 'feature2.jpg', 'New tiled roof by Eco Roofing', I['leaf'] + 'Family-run since day one')}
</div></section>
{feats()}
<section class="sec"><div class="wrap">
<div class="center" style="margin-bottom:48px"><span class="eyebrow">Mission &amp; values</span><h2 data-split>What guides every job we do.</h2></div>
<div class="cards c3" data-reveal="group">{''.join(f'<div class="card"><span class="ico">{I[a]}</span><h3>{b}</h3><p>{c}</p></div>' for a, b, c in vals)}</div></div></section>
<section class="sec soft"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">Why choose us</span><h2 data-split>Six reasons homeowners pick Eco Roofing.</h2></div></div>
<div class="cards c3" data-reveal="group">{''.join(f'<div class="card"><span class="ico">{I["check"]}</span><h3>{a}</h3><p>{b}</p></div>' for a, b in why)}</div></div></section>
{stages(p, soft=False)}
{reviews(4)}
{steps()}
{cta(p)}"""

GALLERY = [f'g{i:02d}.jpg' for i in range(1, 19)]
def gallery_page(p):
    g = ''.join(f'<a class="tile" href="{p}img/{x}"><img src="{p}img/{x}" alt="Roof by Eco Roofing, Dublin" width="{dims(x)[0]}" height="{dims(x)[1]}" loading="lazy"></a>' for x in GALLERY)
    return f"""{phero(p, [('Gallery', 'gallery/')], 'Our work.', 'New roofs, re-roofs, flat roofs and repairs. A look at recent jobs by the Eco Roofing team.', 'v3.jpg')}
<section class="sec"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">Gallery</span><h2 data-split>Recent roofs.</h2></div><p>Tap any photo to see it full size.</p></div>
<div class="boxes" data-reveal="group">{g}</div></div></section>
{stages(p)}
{cta(p)}"""

def contact_page(p):
    return f"""<section class="phero chero">
<img class="bg" src="{p}img/v2.jpg" alt="" fetchpriority="high">
<div class="wrap chgrid">
<div class="chhead"><div class="crumb"><a href="{p}">Home</a><span>/</span><b>Contact</b></div>
<h1>Get a free roofing quote.</h1>
<p class="lead">Tell us about your roof and we’ll come back to you within 24 hours with a free inspection and an honest, no-obligation quote.</p></div>
<div class="chform">{form(p, 'full', 'Send us a message', 'Free, no-obligation quote. We reply within 24 hours.')}</div>
<ul class="clist">
<li><a href="{TEL}">{I['phone']}<span><small>Call us</small><b data-cfg="phone">{PHONE}</b></span></a></li>
<li><a href="{WAURL}" data-href="whatsapp" target="_blank" rel="noopener">{WA}<span><small>WhatsApp</small><b>Send us a photo of the roof</b></span></a></li>
<li><a href="mailto:{EMAIL}">{I['mail']}<span><small>Email</small><b data-cfg="email">{EMAIL}</b></span></a></li>
<li><span class="nolink">{I['pin']}<span><small>Areas</small><b>Dublin, Wicklow, Kildare, Meath &amp; Louth</b></span></span></li>
</ul>
</div></section>
{areas(p)}
{cta(p)}"""

def dublin_page(p):
    towns = ''.join(f'<span>{t}</span>' for t in sorted(set(AREA_TOWNS)))
    return f"""{phero(p, [('Roofers in Dublin', 'roofers-dublin/')], 'Roofers in Dublin you can trust.', 'A family-run Dublin roofing company covering the whole county plus Wicklow, Kildare, Meath and Louth. Repairs, new roofs, flat roofs, chimneys, guttering and roof cleaning.', 'v1.jpg', f'<div class="btn-row"><a class="btn btn-blue" href="#quote" data-quote>Get a free quote {I["arrow"]}</a><a class="btn btn-ghost" href="{TEL}">{I["phone"]} {PHONE}</a></div>')}
{marquee()}
<section class="sec"><div class="wrap split">
<div><span class="eyebrow">Local Dublin roofers</span><h2 data-split>Dublin roofs, fixed properly.</h2>
<p>We work all over Dublin, from Victorian terraces in Rathmines and Drumcondra to family homes in Swords, Lucan, Malahide and Blackrock, and out into Wicklow, Kildare, Meath and Louth.</p>
<p>Dublin roofs take a beating from the weather. Most of our calls are for leaks, slipped tiles, chimneys letting in damp, worn flat roofs on extensions, rotting fascias and roofs covered in moss. We find the cause, fix it properly and give you a written quote before any work starts.</p>
<p>And because we are an eco-friendly roofer, we repair before we replace, recycle what we take off and use materials that last.</p>
<div class="chips big">{towns}</div>
<div class="callrow"><a class="btn btn-blue" href="#quote" data-quote>Get a free quote {I['arrow']}</a><div><small>Prefer to call?</small><a class="num" href="{TEL}">{PHONE}</a></div></div></div>
{pic(p, 'feature.jpg', 'Roofers re-roofing a house in Dublin', I['pin'] + 'Dublin &amp; 4 counties')}
</div></section>
{services_grid(p, title='Roofing services across Dublin.')}
{areas(p, more=False)}
{reviews(4)}
{faq()}
{cta(p)}"""

COOKIES = [('eco_intro', 'Session storage', 'Remembers that the opening animation has already played, so it only shows once per visit.', 'End of session')]
def cookie_page(p):
    rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in COOKIES)
    return f"""{phero(p, [('Cookie Policy', 'cookie-policy/')], 'Cookie policy.', 'How this website uses cookies and similar technologies.', 'v5.jpg')}
<section class="sec"><div class="wrap article">
<p>This page explains how we use cookies and similar technologies on our website. Cookies are small text files stored on your device when you visit a website. For how we handle personal data, see our <a class="blue" href="{p}privacy-policy/">Privacy Policy</a>.</p>
<h2>Essential</h2>
<p>Essential storage enables basic functions and is needed for the website to work properly. It does not identify you.</p>
<table><thead><tr><th>Name</th><th>Type</th><th>Description</th><th>Duration</th></tr></thead><tbody>{rows}</tbody></table>
<h2>Statistics &amp; marketing</h2>
<p>This website does not currently set any analytics, advertising or tracking cookies. If we add analytics in future, it will only load after you give consent, and this page will be updated.</p>
<h2>Third-party content</h2>
<p>Fonts are served by Google Fonts. See <a class="blue" href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google’s privacy policy</a>.</p>
<h2>Managing cookies</h2>
<p>You can block or delete cookies and site data at any time in your browser settings. The site will still work; the opening animation may simply play again.</p>
<h2>Contact</h2>
<p>Questions about this policy? Email <a class="blue" href="mailto:{EMAIL}">{EMAIL}</a> or call <a class="blue" href="{TEL}">{PHONE}</a>.</p>
</div></section>
{cta(p)}"""

def privacy_page(p):
    return f"""{phero(p, [('Privacy Policy', 'privacy-policy/')], 'Privacy policy.', 'How Eco Roofing collects, uses and protects your personal information.', 'v6.jpg')}
<section class="sec"><div class="wrap article">
<p>Eco Roofing (“we”, “us”) respects your privacy. This policy explains what personal information we collect through this website and how we use it, in line with the GDPR and Irish data protection law.</p>
<h2>Who we are</h2>
<p>Eco Roofing, Dublin, Ireland. Email <a class="blue" href="mailto:{EMAIL}">{EMAIL}</a>, phone <a class="blue" href="{TEL}">{PHONE}</a>.</p>
<h2>What we collect</h2>
<p>When you send a quote request, callback request or message, we collect the details you give us: your name, phone number, email address, the service you are interested in and your message. We do not collect any other personal information through this website.</p>
<h2>How we use it</h2>
<ul><li>To respond to your enquiry and arrange a roof inspection or quotation.</li><li>To carry out and follow up on work you have asked us to do.</li><li>To keep records required for accounting and legal purposes.</li></ul>
<p>Our legal basis is taking steps at your request before entering into a contract, and our legitimate interest in replying to enquiries. We never sell your information.</p>
<h2>How long we keep it</h2>
<p>Enquiries that do not lead to work are deleted within 12 months. Records relating to completed work are kept for as long as the law requires.</p>
<h2>Your rights</h2>
<p>You can ask to access, correct or delete your personal data, restrict or object to how we use it, or ask for a copy. You also have the right to complain to the Data Protection Commission (dataprotection.ie).</p>
<h2>Cookies</h2>
<p>See our <a class="blue" href="{p}cookie-policy/">Cookie Policy</a>.</p>
</div></section>
{cta(p)}"""

if __name__ == '__main__':
    T = ' | Eco Roofing'
    pages = []
    def P(path, *a, **k): pages.append(path); page(path, *a, **k)
    P('', 'home', 'Roofers Dublin | Eco-Friendly Roof Repairs, Re-roofing & Roof Cleaning | Eco Roofing',
      'Eco Roofing: family-run, eco-friendly roofers in Dublin. Roof repairs, re-roofing, flat roofs, slate and tile, chimneys, guttering and roof cleaning across Dublin, Wicklow, Kildare, Meath and Louth. Free quotes.', home, intro=True, ld=faq_ld())
    P('services/', 'services', 'Roofing Services Dublin' + T, 'Roof repairs, re-roofing, flat roofing, slate and tile, felt roofing, chimney repairs, fascias and guttering, and roof cleaning across Dublin.', services_page)
    for s in SERVICES:
        P(s['slug'] + '/', 'services', s['h1'].rstrip('.') + ', Wicklow & Kildare' + T, s['summary'], service_page(s),
          kw=f"{s['name'].lower()} Dublin, {s['short'].lower()} Dublin, roofers Dublin, eco roofing Dublin, {s['short'].lower()} Wicklow, {s['short'].lower()} Kildare, {s['short'].lower()} Meath")
    P('roofers-dublin/', 'areas', 'Roofers in Dublin | Local, Family-Run & Eco-Friendly' + T, 'Family-run roofers covering all of Dublin plus Wicklow, Kildare, Meath and Louth. Roof repairs, new roofs, flat roofs, chimneys and roof cleaning. Free quotes.', dublin_page, ld=faq_ld())
    P('gallery/', 'gallery', 'Roofing Gallery: Recent Jobs' + T, 'New roofs, re-roofs, flat roofs and repairs by Eco Roofing.', gallery_page)
    P('about/', 'about', 'About Us: Family-Run Dublin Roofers' + T, 'Eco Roofing is a family-run Dublin roofing company with 15+ years of experience and a commitment to eco-friendly practice.', about_page)
    P('contact/', 'contact', 'Contact Us: Free Roofing Quote Dublin' + T, 'Get a free roofing quote from Eco Roofing. Call 087 130 6744, WhatsApp or email ecoroofingandrestoration@outlook.com.', contact_page)
    P('cookie-policy/', '', 'Cookie Policy' + T, 'How the Eco Roofing website uses cookies.', cookie_page)
    P('privacy-policy/', '', 'Privacy Policy' + T, 'How Eco Roofing handles your personal information.', privacy_page)
    with open(os.path.join(ROOT, 'sitemap.xml'), 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
            f'<url><loc>{SITE}/{x}</loc><priority>{"1.0" if not x else "0.9" if x in ("roofers-dublin/", "services/") else "0.6" if "policy" in x else "0.8"}</priority></url>\n' for x in pages) + '</urlset>\n')
    with open(os.path.join(ROOT, 'robots.txt'), 'w') as f:
        f.write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
