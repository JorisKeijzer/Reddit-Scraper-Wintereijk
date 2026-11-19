# Label-batch batch_0083

## Instructies
Je bent een marktonderzoeker voor een Nederlands e-commercemerk dat koperen inlegzolen gaat verkopen. Je codeert Reddit-threads over voeten, voetklachten, schoenen en inlegzolen volgens een vast codeboek.

Regels:
- Citaten (quotes.text) zijn ALTIJD letterlijk en exact uit de bron overgenomen, inclusief spelfouten. Nooit samenvatten, vertalen of verbeteren in dat veld. nl_meaning is een getrouwe vertaling, geen reclametekst.
- Codeer alleen wat er staat. Verzin geen beroep, diagnose of situatie die niet genoemd wordt; gebruik dan null of een lege lijst.
- Scheid eigen ervaring (first_hand=true) van advies uit de tweede hand, diagnoses door vreemden en reclame van fabrikanten.
- Neem ook tegengeluiden en negatieve ervaringen mee: wat NIET werkt is net zo waardevol als wat wel werkt.
- Noteer elke vermelding van koper, magneten, acupressuur of reflexologie, ook sceptische, in 'copper'.
- Een Reddit-reactie bewijst geen klinische werking. Zet claims_risk op 'medical' bij aandoeningen of behandelclaims, 'material' bij materiaalclaims (koper, antibacterieel, geur), anders 'comfort_only'.
- medical_red_flag bij diabetes, neuropathie, gevoelloosheid, branden/tintelen, infectie, (stress)fracturen of ernstige zwelling.
- marketing_insight_nl is een hypothese voor ons merk, geen feit; beloof daarin nooit genezing of pijnvermindering.
- Is de thread niet over voeten/schoeisel/zolen (bijv. een toevallige zoekmatch), zet relevant=false en houd de rest minimaal.

## Opdracht
Label elke thread hieronder volgens het schema `ThreadLabel` in `vocscraper/schema.py`.
Schrijf het resultaat naar `batch_0083.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1jt5lon, 17c7rn7, y1yssd, 8ch25c).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1jt5lon ===
SUBREDDIT: r/army
DATUM: 2025-04-06  SCORE: 157  REACTIES: 99
TITEL: 12 mile ruck- foot insoles good idea?
POST (source_id=post):
Did a 6 mile ruck a few days ago in under 1:30 and have to do a 12 mile ruck in under 3 hours in a few days. After the 6 mile my feet were pretty beat up. Main issue is giant blister on bottom of my foot towards the heel. Does anyone use these things? Is it a good or a bad idea? Can’t imagine any cons to using them but don’t want to screw myself.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mlrolha] (score 348, diepte 0) If you haven’t already been training with it, don’t use it on the big one that counts.
[mlrs2xc] (score 202, diepte 2) You gon’ hurt.

I will live and die by Garmont NFS + Darn Tough combo.
[mlrptub] (score 119, diepte 1 OP) What if I’ve been in 6 years and the first time I rucked since basic training was that 6 mile I just did 😂
[mlrph1h] (score 98, diepte 0) Make sure to break them in.  Never introduce something new right before a 12 miler because you’ll find any issues REAL quick and then you’ll have to deal with them for.the remaining 11.5 miles
[mlrtarc] (score 88, diepte 0) Bro, what you should do is get a pair of OCP pants 1 size bigger and get this:


https://hypershell.tech/en-us/pages/hypershell-x-exoskeleton?utm_id=carriel&utm_source=pr&utm_medium=mediabuy&utm_campaign=uncrate&utm_term=Hypershell%20X&utm_content=202504


Show me in the regulation its not allowed...ill wait.
[mlrs8rf] (score 46, diepte 3) This is the way, NFM/battaan death march/ranger school no blisters
[mlrp3sq] (score 42, diepte 0) Unless you wear insoles on the regular, I wouldn't recommend this honestly. If you getting blisters toward the heels I would start by doubling up socks, "dress socks & a nice pair of regular socks", and lace up from bottom to top nice and snug. And if you still feel movement toward the heel, a couple long pieces of duct tape in the heel of the boot and help give some extra fit so your feet don't move as much.
[mls82vb] (score 31, diepte 1) Think I can sneak this in to ranger school?
[mls8sl4] (score 29, diepte 1) $10 off offer. $800 product. I actually feel insulted. That like, doesn't even cover sales tax.
[mlrqm7n] (score 27, diepte 0) Absolutely not.
[mlrs46j] (score 26, diepte 0) New thing, right before long thing, bad.
[mls8hzh] (score 21, diepte 2) If you are not cheating, you are not trying.
[mlrwwmu] (score 17, diepte 0) Oof. 

You’re inside your window for too many options.

Option 1- Drain it. Pierce it with a sterile needle and drain it. Check the thread technique in the guide linked below. Hope for the best.

Option 2- Drain it and glue it. Pierce it with a sterile needle and drain it. Then, carefully insert a little tincture of benzene. This is a liquid that serves as an adhesive enhancer, and in extreme situations (like yours) can ‘glue’ the skin back down. It will hurt like hell, but if you do it now it might ‘heal’ or at least get slightly better by the time you ruck next.

Option 3- Moleskin. Cut a donut slightly larger than the blister to relive pressure. Wear thick cushion sole socks. Pray.

Option 4- Do nothing. It might drain on its own and be okay. If not, then you deserve to suffer for not preparing properly. 😂 

If you’re interested in learning how to prepare your feet for a lifetime of faithful service then check out this [foot care guide we wrote for SFAS prep](https://tfvoodoo.com/articles/how-to-prep-your-feet-for-sfas-special-forces-assesment-selection).
[mls9swj] (score 15, diepte 2) That’s how billionaires become billionaires - saving $10 off their $800 robot legs.
[mls34o9] (score 14, diepte 4) Selection in this combo. No pain or blisters.
[mlrt9wz] (score 14, diepte 3) [https://www.amazon.com/Superfeet-Dynamic-Insoles-Unisex-Spectra/dp/B07NHFN81D?pd\_rd\_w=WLMmO&content-id=amzn1.sym.0c00971a-971c-4dda-a54c-e65f98cf0e25&pf\_rd\_p=0c00971a-971c-4dda-a54c-e65f98cf0e25&pf\_rd\_r=ED3ZWGC3FNBHZTX6C1HE&pd\_rd\_wg=93v3Z&pd\_rd\_r=061fd516-c406-4242-8d12-eb74c3318adb&psc=1&ref\_=pd\_bap\_d\_grid\_rp\_csi\_vtp\_0\_i](https://www.amazon.com/Superfeet-Dynamic-Insoles-Unisex-Spectra/dp/B07NHFN81D?pd_rd_w=WLMmO&content-id=amzn1.sym.0c00971a-971c-4dda-a54c-e65f98cf0e25&pf_rd_p=0c00971a-971c-4dda-a54c-e65f98cf0e25&pf_rd_r=ED3ZWGC3FNBHZTX6C1HE&pd_rd_wg=93v3Z&pd_rd_r=061fd516-c406-4242-8d12-eb74c3318adb&psc=1&ref_=pd_bap_d_grid_rp_csi_vtp_0_i)

  
I use these bad boys with my Garmont NFS and Darn Toughs
[mlsc5o5] (score 14, diepte 3) I mean ibolc students have been burying garmins for ages at red diamond...
[mlrxe0g] (score 14, diepte 0) I recommend setting an appointment with your PCM to get a referral for Podiatry. They'll mold an insole that's specifically accustomed to your foot. If you're in the Midwest region, Tactical Rehabilitation makes excellent insoles and they're free!
[mlrp2n4] (score 9, diepte 0) Depending on size of the blister and if it’s burst or not, throw a bandaid over it and then a piece of duct tape. Used to tell my guys to use duct tape over mole skin and never had anyone go back to using mole skin 🤷‍♀️
[mlswak3] (score 9, diepte 1) Every time I get a blister I drain it and then soak it in hand sanitizer and sleep with my foot outside the covers. Wake up in the morning to a full size callous. Find something to bite down on first

Do it at your own risk cause I'm sure some doctor out there will say that doing this will cause your foot to fall off or something. Works for me
[mlsf5c1] (score 8, diepte 1) I’d love to be the guy who triggers an update in regulation
[mlrzelg] (score 7, diepte 4) Totally agree with you on the Garmont’s and Darn Tough’s. Oddly enough though, these insoles destroy my feet.
[mlrv1wy] (score 7, diepte 0) You don’t want gel. Get Superfeet Green insoles
[mls0pwh] (score 6, diepte 5) I've never tried the NFS' with their built-in insoles tbf.  I did a lot of research and found most GBs and Rangers were using this combo, so I bought it before pre-sapper, and started running my fastest rucks ever and no real hotspots for the first time.  But it's 100% what works for you individually.
[mlrplgr] (score 6, diepte 0) I don't recommend unless you've broken them in. I know from (bad) experience.
[mlrq9x2] (score 5, diepte 1) That's not true at all. I've got really high arches and use insoles for them. Not every foot is the same. But I agree with using your broken in boots, don't change anything before a long ruck.
[mlrplti] (score 5, diepte 1 OP) About size of a quarter and hasn’t burst. You saying use the duct tape if it hasn’t or has burst?
[mls4tdm] (score 5, diepte 1) This is old school advice right here. I’ve also used sock liners instead of dress socks and my feet weren’t as wet. I did this during the Manchu March
[mlro5vj] (score 4, diepte 0) Better off just having a broken in pair of boots with whatever insoles they come with. Most added insoles are a scam and probably worse for you.
[mls6zaz] (score 4, diepte 2) Get some mole skin and good socks.
[mlrx3bm] (score 4, diepte 2) If it hasn’t burst, thread a needle and push it through the blister. Work it back and forth as much as possible so it’ll allow the liquid to drain but still keep the skin on the outside to protect the raw skin. Try to air your feet out at night too. If you put duct tape on your foot before a 12 miler, it’s impermeable and you’ll likely sweat it off and have another problem. Biggest thing for spending time on your feet under load is good boots and then good socks. Darn tough or smartwool is the way to go. Boots are shooters preference but a little late in the game for new boots. I have done a Norwegian ruck with merrel mqc’s straight out of the box though.
[mlsbo6h] (score 4, diepte 0) No. Get good socks. Your feet need to toughen up, but it helps a lot to have good socks that keep your feet dry and fill up your boot. "Good" usually means the kind that are standalone $8-$20 on the rack.

If this happens all the time you should try a different boot too.

If you've never broken in your boots properly -- get them wet and do a few short rucks so they can mold to your feet a little and that breaks in the spots that might your skin down.

12+ miles isn't a good time to experiment with new stuff so try shorter rucks if you are trying socks, insoles, boots, whatever.
[mlshjnn] (score 3, diepte 5) your nearest fleetfeet probably have them in stock, its where i got mine
[mlt933k] (score 3, diepte 7) Fleetfeet isn’t on any military base.
[mlucdjt] (score 3, diepte 9) Nah, fleetfeets are everywhere. It’s a running store. Nothing to do with the military.
[mltn9ck] (score 3, diepte 3) I’ve never been in a unit that actually did that, tbh.
[mlt8vkz] (score 3, diepte 2) Gonna have a hard time in Florida. 😂
[mlruu7t] (score 3, diepte 0) Those will shift around a LOT on your foot.

Not the same, but BacK iN BoOtCaMp I threw these in my made-by-the-blind black boots and promptly had horrid foot issues because of the movement. Do not recommend. The dr sholls machine ones that have the polymer arch aren't half bad, I'd still do everyday wear in them before you do a ruck with them.
[mlryvfx] (score 2, diepte 4) Out of stock according to the link.
[mlsdxbv] (score 2, diepte 3) I use the 670s but yeah those boots are great for road marching
[mlsj0xr] (score 2, diepte 3) Dawg everyone I know uses Fox Rivers. Been trying to convert them to Darn Tough
[mlvl95y] (score 2, diepte 3) It's not a Army requirement and not every unit institutes that as a unit requirement.
[mlru211] (score 2, diepte 0) When you’re ruck marching, don’t use insoles like Dr. Scholl’s. They’re fine for everyday walks, but when you start sweating, they actually make your feet wetter and start to slip around, which can cause more problems than help. Every time I’ve tried fancy insoles, I always go back to the basic ones.

It’s really important to keep your feet dry, so make sure to change your socks regularly. A lot of people make mistakes like using new boots or wearing double socks or thicker socks. New boots can cause blisters, so they should be broken in before a long march.

Double socks or thicker socks might feel okay at first, but they’ll actually make your feet sweat more and get uncomfortable. When you do change your socks, remember to switch the insoles from your spare boots as well. You can leave the wet insoles upside down on the rucksack flap to dry out as you walk. Good luck man🍀
[mlt9rc2] (score 2, diepte 1) Shut up, racist little bitch.
[mls3jjo] (score 2, diepte 0) Don't change your gear right before the thing that matters.

But i highly recommend wearing dress socks under your rucking socks. It'll help with hot spots.
[mlsgfy4] (score 2, diepte 4) To keep my feet dry walking through half melted slushie snow and weird frothy mud, I wore plastic bags outside of my socks, under my boots. It's an older hiking trick when you get caught with improper footwear.
[mls61bj] (score 2, diepte 0) Moleskin is a solid option, and a quick order on a pair of good Darn Tough socks. Which air assault school are you at?
[mlsm4na] (score 2, diepte 0) gel insoles are the WORST for sweaty fit. you will get the most god awful blisters with all the sliding around because there is quite a bit of give. For rucks you want something strong that will hold the shape of your arch especially since you'll be carrying weight. If you have trouble with your feet, see your PCM and get a referral for orthotics. You'll be suprised what the actual sports ones are like.
[mlsp75g] (score 2, diepte 0) Hiker friend of mine taught me a good way to deal with blisters. Take a needle and thread and put the thread through the blister from one end to the other not piercing the skin underneath. Tie it off. This creates a way for the blister to dry out and heal wothout exposing it to the elements and bacteria. Change socks consistently and I’d suggest bandages when wearing shoes but leave uncovered to get as much air in as possible. Works like a charm for me. Relieves pressure and pain.
[mlsqlo4] (score 2, diepte 0) I was one of the guys who had the immense amount of luck to get a perfect fit out of his basic training issue boots (both pairs).  Even though I was MI I had the bad luck of getting attached to SF units. PT twice a day morning PT consisting of 6 Mile ruck or 6 mile run. 4 years later those boots through good care had the softest leather ever and fit like a dream. Had them resoled 2 times. I wish I knew where they were I'm an old man now LOL.
[mlsi4vn] (score 1, diepte 6) My brother, the closest thing to a military base to me is a coast guard station with a shopette.   There's nothing military anywhere near me.
[mlud6lc] (score 1, diepte 10) Neat.  I'll look into em.  Thanks!
[mls64rv] (score 1, diepte 3) Yup.
[mlvwfr1] (score 1, diepte 4) My bad, for the entirety of my 20 year career it was a requirement for each soldier to complete a 20k road march, a 5 mile run, and pull-up assessment each year. Guess I was just in good units. (18th Airborne Corps and USASOC.)
[mlrzxo3] (score 1, diepte 2) Nothing you do will make this suck less
[mlt92e0] (score 1, diepte 2) What? For about 3 years we did a 12 mile for time (posted publicly) every 3 to 5 weeks…
[mltc6z0] (score 1, diepte 2) I did the Manchu mile (25 miles) after not rucking for 7 years. Boy was I crippled for a week after that. Cool experience though.
[mlrvc9v] (score 1, diepte 2) It’s not as helpful if it hasn’t busted open yet. But the duct tape reduces the friction. It’s not going to get rid of it or anything but it’ll make it a little more comfortable to continue rucking with
[mlrsbkf] (score 1, diepte 1) wtf lol
[mlrtako] (score 1, diepte 1) What does duct tape do for the blister? 
Is this before or after you get a blister?
[mlrvj9v] (score 1, diepte 2) Works great for hotspots, but I’ve used it for blisters too. The slick piece of tape just reduces the friction so you’re not rubbing an already established hotspot or blister and making it worse. Doesn’t really help heal it or anything.
[mlrui14] (score 1, diepte 1) duct tape (over) mole skin or do you mean duct tape instead of moleskin? sorry, wasn't really clear the way you wrote it.
[mlrp2tz] (score 1, diepte 0) Never used insoles like that but I don’t know if I’d try them out first time for a 12 miler. I’d at least try a few miles to see how they are or do something like getting a good pair of socks and sock liners and putting them inside out. I personally do that and add baby powder/leuko tape to places I normally get blisters. That methods gotten me through air assault, E3B ruck, Norwegian foot march, and edelweiss.
[mlrpen5] (score 1, diepte 0) Boots with Darn Tough socks
[mlrrkyi] (score 1, diepte 0) These are not supportive and just collapse under you. 

Get insoles that actually have shape and a firm arch.
[mmapv78] (score 1, diepte 1) Dude I have to participate in the Norwegian all of a sudden and 1SG is making me feel the pressure 

I am legitimately contemplating this
[mmazukq] (score 1, diepte 2) Bet you wont...
[mlru7bx] (score 1, diepte 0) Soak your feet in epsom salt once or twice before the 12 mile. I swear that shit is magic for feet issues
[mlrwmcz] (score 1, diepte 0) I could only use the more expensive, custom inserts for rucking.  The over-the-counter inserts made it worse for me, as they tended to slide around more, and come apart.
[mlrwpdc] (score 1, diepte 0) I used to get insoles that were fitted to my feet. I have high arches and dr scholls just aint it. Go to a store that specializes in running like the good feet store.
[mlss03v] (score 1, diepte 1) Only time I got it was trying to break in those horrible jungle boots. However the thread message is great one side and one side out and cuts down significantly on pain.
[mlt2yxp] (score 1, diepte 1) That's how my feet looked after more than a few 12-milers.
[mnkhi4p] (score 1, diepte 1) No unapproved AMAs, fundraisers, ads or surveys.
[mls923w] (score 1, diepte 2) I did maybe 25 miles through hohenfels at the end of winter. Had the combo above, and added some shopette grocery bags to keep my feet dry. Good times.
[mls9h3x] (score 1, diepte 3) wtf…seriously lol
[mlsbnma] (score 1, diepte 4) It worked heh
[mlsfzom] (score 1, diepte 3) You what?...
[mls8wv7] (score 1, diepte 1 OP) Lightning academy- Hawaii
[mls6d31] (score 1, diepte 0) I used to just turn my socks inside out. Never once got a blister. Properly fitting and broken in boots, and good socks make all the difference.
[mls8sdu] (score 1, diepte 0) You must be in air assault school at ft Benning right now.  Best for you to do is to drink water and get rested.  There's medics and a shopette for moleskin.  Too many air assault students falling out as heat casualties.
(24 reacties met lagere score weggelaten)

=== THREAD 17c7rn7 ===
SUBREDDIT: r/USPS
DATUM: 2023-10-20  SCORE: 14  REACTIES: 96
TITEL: What shoes do you all use?
POST (source_id=post):
As the question says.  I'm on my feet all day at the pdc and currently have sketchers .. not sure.. arch fit.  Have insoles.  Had them maybe more than 6 months but less than a year and they are getting worn.

What all shoes and/or insoles do you all buy when your walking and using your feet all day??

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k5o5e6t] (score 19, diepte 0) New Balance.
[k5o54fh] (score 17, diepte 0) Just bought hoka bondi sr been using green tag shoes because Supervisor is an ass but I got like pain on top of my feet now and ordered the hokas. They say it should pass the shoe test because it’s leather black and slip resistant
[k5o5mfa] (score 12, diepte 0) Hoka Bondi SR
[k5o9c67] (score 7, diepte 0) was rocking some gum bottom reeboks. just upgraded to nike Air Monarch
[k5oiphv] (score 5, diepte 1) The pain on the top of your feet could be from the shoes being too tight. At least that was my experience. The pain i was having was on the top of the foot close to my shin. Switched to Keen and the pain resided.
[k5oanu6] (score 5, diepte 0) New Balance with non slip soles. And compression socks will make a world of difference.
[k5oaulv] (score 5, diepte 1) Look at Joes New Balance Outlet online. Super inexpensive.
[k5oev8h] (score 5, diepte 0) Hoka Bondi sr
[k5oipzy] (score 4, diepte 0) Freet. Minimalist shoes. Let your feet support you like they were meant to
[k5o724u] (score 3, diepte 0) Shoes for crews. About $50 bucks super light and durable. I get new ones every 4 months but they could last longer if needed. They have many styles that fit postal requirements. (Park and loop 9.5miles)
[k5o7ht8] (score 3, diepte 0) Timbs
[k5qqrsj] (score 3, diepte 1) Everyone rockin the monarchs. Not sure why they're called monarchs. Should be called clown shoes with all the squeeking sounds they make.
[k5oli2u] (score 3, diepte 0) New Balance 608 cross trainers
[k5phu04] (score 3, diepte 0) Just bought some Reebok Men's Walk Ultra 7 DMX Max 4e Shoes. 2 weeks in and they are great. Don't know how long they will last. I used to wear the postal Approved New balance but they don't make them anymore. Nike Air Monarchs are great too
[k5o5ju1] (score 2, diepte 0) Superfeet insoles
[k5on9ov] (score 2, diepte 2) They reduce swelling in feet/legs by forcing the liquid up. It’s a night and day difference wearing them vs. not.

There’s different levels of compression too. The kind you find in most stores is the lowest. I get mine off Amazon. [SB Sox](https://www.amazon.com/SB-SOX-Compression-Socks-20-30mmHg/dp/B078P91DKY/ref=mp_s_a_1_3_pp_maf_4?adgrpid=64526320508&hvadid=635368755031&hvdev=m&hvlocphy=1021883&hvnetw=g&hvqmt=e&hvrand=6943095181313919071&hvtargid=kwd-322863230347&hydadcr=12684_13489419&keywords=sb+sox&qid=1697806888&sr=8-3) is the brand I use. 25-30 mmHg compression.
[k5o6osl] (score 2, diepte 0) New Balance 626 v2 Industrial Shoe

Around 100 on Amazon. $80-$100 in stores 

New Balance Men's MID626 Slip-Resistant Shoe https://a.co/d/gCJzTqc
[k5o7l79] (score 2, diepte 0) When I was a clerk Hoka was the only shoes that helped my feet and highly recommend them.
[k5qr3xe] (score 2, diepte 2) I'll check it out next time. I bought New Balance from Zappos for $60 when I first was hired. Looking now, same pair at Joe's is $50.
[k5oc0f6] (score 2, diepte 0) Spend money on a good pair of shoes. For clerking in the office I got SAS shoes. They have great arch support and made in USA. I think I paid about $200 after military discount or something
[k5ogldf] (score 2, diepte 0) It's funny you should ask I have been at Syracuse P&DC for 25 years and they just started enforcing leather shoe policy Leather shoes a terrible for being on your feet all day
[k5omncg] (score 2, diepte 0) SAS are the most comfortable and long lasting that I’ve found. They are godawful ugly but my back doesn’t hurt after 10 hours on my feet.
[k5opkpg] (score 2, diepte 0) 5.11 (that’s the brand)
[k5tadhd] (score 2, diepte 1 OP) Just Epsom salt in hot water and soak until almost prune?

I have wide feet too and get sore.  I love when someone crushes my foot in their palm..
[k6ip7je] (score 2, diepte 3 OP) ... miraculous?  Or like 30 lashes to the back?  =)
[k5oxr9s] (score 2, diepte 0) 97 air max and Jordan 1 highs
[k5q5n7e] (score 2, diepte 1) shoe carnival has them…..just bought them for my husband….there’s an online coupon & they ship
[k5pszjc] (score 2, diepte 0) Alexander McQueen Punk Crystal Ankle-Strap Sandals.
[k5to5jj] (score 2, diepte 2) Can confirm, I am a dad who wears shoes.
[k5rgwa4] (score 1, diepte 2) I tried loose tight everything something about rocky boots by the big toe just pushes against the bone on top of the feet my other foot is fine just left side keeps grinding. It only happens with green tag shoes . Sketchers new balance Nike monarch all feels great but green tag shoes is like extra heavy and the top of the toe area the shoes get heavily damaged
[k5p5bep] (score 1, diepte 1) Pain on top of your feet could also be tight calves. Tight calves mean your feet can't move fully while walking which creates a strain around top of foot. No joke get a good muscle roller and really roll out your calves it makes a huge difference.
[k5qjs43] (score 1, diepte 1) Just sew a green tag on the shoes.
[k5qphb1] (score 1, diepte 1) Exactly this. And if you're able to, buy some shoe insoles with them.
[k5o5lab] (score 1, diepte 0) Air Max SC’s and compression socks.
[k5o66l5] (score 1, diepte 1 OP) Compression socks??  Are they just tight??
[k5ta4ph] (score 1, diepte 3 OP) So they compress and push things up....  does that mean they are like uncomfortably tight?

I can wear calf high socks but need to lower them after awhile for comfort...

Still recommend?

I'm interested..
[k5tecup] (score 1, diepte 4) Mine are graduated compression iirc. Strongest compression at the bottom and it lessens slightly as they go up.

I’ve never found them to be uncomfortable. Feels way better than my feet pressing against the inside of my shoes and giving me blisters.
[k5o69fx] (score 1, diepte 0) I had HORRIBLE plantar fasciitis from window clerking. 9/10 hours a day standing. Tried insoles, Hoka’s, Sketchers Arch, Brooks. Bought compression socks and arch support bands. Rolled my feet on frozen ice bottles. Did stretches. I couldn’t even walk. I read a post where someone’s podiatrist recommended hiking shoes/boots until it went away. Bought myself a pair of Merrell’s and I’m completely better. I still wear them and luckily my PM doesn’t give a shit with the whole leather thing. Took about 2 months to go away fully.
[k5o7vpz] (score 1, diepte 0) New Balance 928V3
[k5o92nb] (score 1, diepte 0) Rockys I have 3 pairs I got off Amazon with green tags for the same price as 1 pair from postal sellers. Just rotate them. 1 pair is for wet weather and 2 for normal days.
[k5obt6d] (score 1, diepte 1) They saved my ass from falling a whole bunch of times currently on second pair.
[k5oks4a] (score 1, diepte 2) really ? I know they’re comfortable but they’re not slip resistant are they ?
[k5ong1b] (score 1, diepte 3) So far they been working for me
[k5qm2rk] (score 1, diepte 3) On my 8th pair, have 1 house I deliver to with a latex based paint cement porch that gets slippery after rain but no issue with slippage other than that.

They're great with insoles popped in out of the box.

Seem to have to replace them every 3-4 months but to be expected. Had sketchers previously and they fell apart in a month.
[k5ofz8i] (score 1, diepte 0) Nike ACG lowcrates. Comfortable asf for rural carrying. Looking to buy those Hoka float x's tho.
[k5ojqix] (score 1, diepte 0) Keen boots.
[k5ojrhv] (score 1, diepte 0) Hiking boots in the summer.  
Insulated boots in the winter.
[k5omyu1] (score 1, diepte 0) So if normal insoles are not lasting then try to get with a foot doctor to get better insoles that will last longer. As to shoes, find something that is comfortable and non slip for the job.
[k5omz57] (score 1, diepte 0) I was using timberland hiking boots. Was great for my wide feet. Then my wife brought me these Columbia brand boots size 13W. The Best boots so far for me!
Wish I can wear sneakers in my station
[k5pjx74] (score 1, diepte 1) I just got some Columbia shoes with outdry tech for $75 and they are comfy and much better in the rain
[k5onvd6] (score 1, diepte 0) Hoka
[k5qybz5] (score 1, diepte 1) This is the correct answer. 5.11 Tactical. It’s a cringe brand but they got some good ass boots. They also give wide boot options for my fat ass feet. Some of their shoes even come with a green label that has tricked multiple soups at my office thinking they’re the proper label. They can’t read but learned their colors thankfully. I always end up putting in an insole and always have to mend the back ankle bit, but they’re the best i’ve used.
[k5opzh2] (score 1, diepte 0) I have some Xero shoes with no insoles, and 2 pairs of boots, Origin and Red Wing with red wing insoles.
[k5oq2q9] (score 1, diepte 0) New balance I think because I have giga wide hobbit feet and I boil my feet in Epsom salt a couple times a week
[k5vtb6v] (score 1, diepte 2) Yeah massages rule you gotta take care of your feet. I remember my macho stone masonry uncle would get a pedicure once in a while. My feet look like a bible story
[k6jugch] (score 1, diepte 4) The latter lol
[k5osa4p] (score 1, diepte 0) Just bought the hokas bondi sr. Haven't tested them yet but I'm not too impressed with them. They feel cheap for $175
[k5oukdy] (score 1, diepte 0) Lotttts of people wear leather brooks including my mother that’s a city carrier. She says she loves them, they’re a bit expensive but the quality is there. Been a fan of brooks personally for years as well.
[k5oz1s0] (score 1, diepte 0) Any ROCKY brand boot.
[k5p12n3] (score 1, diepte 0) I've been wearing the "waterproof" Reeboks from the uniform catalogs but I'm gonna switch to something cheaper on my next allowance. The "waterproof-ness" only lasts about a month while they're still rock solid and you're still breaking them in. Expensive junk
[k5p1ki9] (score 1, diepte 0) been rocking nike monarchs, got 2 pairs in january on sale, still rocking them today, but its time for a fresh pair
[k5p1p13] (score 1, diepte 0) Hoka Bondi 7
[k5p6nta] (score 1, diepte 0) I have Skechers Relmont hiking boots and Columbia Newton Ridge hiking boots.  I alternate days with them to let them dry out fully and avoid my feet getting "used" to only one pair.
[k5p6sby] (score 1, diepte 0) Whatever I can find on sale. Right now I’ve got some Columbia shoes until winter
[k5panlh] (score 1, diepte 0) I'm on my feet all day at a annex. I have Ariat workboots. They meet the specifications. I use 3 in 1 insoles with them.
[k5pbavg] (score 1, diepte 0) You should be getting new shoes more frequently than that. If the tread is wearing down, it’s time for new shoes.
[k5s1whd] (score 1, diepte 1) You should wear a new shoe everyday. Nobody who carries should wear the same shoe back to back days.
[k5sl2ma] (score 1, diepte 2) I always buy 2 pair of the same shoes and alternate them everyday so they can completely air out in between.
[k5pc5em] (score 1, diepte 0) Ugh, just got my first green tags in the mail and my feet are KILLING me after three days of CBU routes, can’t imagine walking. Thorogood or something. Going back to my Nike Air Monarchs that are falling apart until I can find another pair, seems nobody around me is carrying them anymore.
[k5pdwoq] (score 1, diepte 0) Rep black cat aj 4s
[k5ph4h7] (score 1, diepte 0) I start carrying next week.  

I did a lot of backpacking in my youth.  I liked using " super feet" inserts in my hiking boots.  15 years ago they were popular with long distance hikers.  To be honest im out of touch with the current gear teck and whats hot.  

They are a completely different type of insert, in that they change the angle of your foot to the ground and provide support rather than cushion.
[k5ph697] (score 1, diepte 0) Get a doctors note. Wear whatever shoe you choose.
[k5prc6m] (score 1, diepte 0) Balenciaga Triple S
[k5pruv2] (score 1, diepte 0) https://www.newbalance.com/pd/fresh-foam-x-840f-slip-resistant/WW840FV1-47319.html
[k5q12vn] (score 1, diepte 0) https://www.catfootwear.com/US/en/prorush-sr-chukka/45927M.html?dwvar_45927M_color=P51045&ref=waterproof%20boots#q=SR%2B&start=1

Gotta change those shoes every 6 months especially if you only have one pair
[k5q1rlz] (score 1, diepte 0) ASICS are the best for your feet
[k5q8nl3] (score 1, diepte 0) Stilettos.
[k5qb90r] (score 1, diepte 0) Man I wish I could get away with wearing all these non green tags you guys have. We recently got new management and they aren't lenient about it at all.
[k5qgris] (score 1, diepte 0) I use sketchers. The memory foam insoles really help
[k5qik9r] (score 1, diepte 0) The moment, my Caterpillar work boots with steel toes are doing quite well, and have done so for like, 15 years or something.

They're in need of some repair, though, so I'm going to need to figure out if it's better to fix them or replace them.
(20 reacties met lagere score weggelaten)

=== THREAD y1yssd ===
SUBREDDIT: r/securityguards
DATUM: 2022-10-12  SCORE: 45  REACTIES: 94
TITEL: Quick, what’s on your feet?
POST (source_id=post):
What we rocking boys? Currently sporting the Nike SFV Gen 2 8” Tactical

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[is01qyi] (score 44, diepte 0) cum
[is04ano] (score 17, diepte 1) Godspeed
[is08qn4] (score 12, diepte 2) Fear me.
[is02u1k] (score 11, diepte 0) Merrell MOAB tactical 8”
[is04q14] (score 11, diepte 0) Vans
[is00bxp] (score 9, diepte 0) Dude it’s my day off and I’m at Dennys, I’m not putting on my boots! Besides I’m wearing my crocs. 😂😂😂
[is08nv6] (score 8, diepte 1) Would you look at that, all of the words in your comment are in alphabetical order.

I have checked 1,097,803,168 comments, and only 215,842 of them were in alphabetical order.
[is0booi] (score 7, diepte 0) Danner Patrol 6”.
[is08n7a] (score 6, diepte 0) Bates 10inch Jumpboots / Oilslip protection.
[is0e85m] (score 6, diepte 0) Merrell MOAB...  When your patrol is 13-16 miles with 50-75 flights of stairs, you want a lightweight hiking boot.  They're the best compromise of comfort and cost.
[is078wn] (score 5, diepte 0) Beat ass Adidas 💀
[is01267] (score 4, diepte 0) Tactical Response side zip safety toes by Belleville.
[is1fe8v] (score 4, diepte 2) Haha the niko episode was amazing.
[is04hvn] (score 4, diepte 0) Docs
[is07p4o] (score 4, diepte 0) Converse All-Stars.
[is08s9w] (score 4, diepte 0) MERRELL Wildwood
[is1fl7q] (score 3, diepte 3) All episodes are amazing but Nikko is a freaking stud. Dudes hilarious
[is038r3] (score 3, diepte 0) I am wearing dookies
[is05u6z] (score 3, diepte 0) Some tims


But I literally took them off seconds before posting this
[is09x1j] (score 3, diepte 0) I wear Danners. I have a boot for the winter. 

https://www.danner.com/onyx-3-black-hot.html
[is1iycr] (score 3, diepte 0) Merrell MOAB 2 Tactical Response (WP)
[is38jge] (score 3, diepte 0) 5.11s not sure what model specifically, but they’re 8”
[is07nya] (score 2, diepte 0) [Jordan Boots](https://drive.google.com/file/d/1OWPNT1TDOSZFfj3TNHY-jbHd06pLxUUL/view?usp=drivesdk) all the way Jordan 6 Rings, Winterized Black.
[is0c0ew] (score 2, diepte 0) Xena Workwear's omega boot. 

  Xena does for women by women safety shoes, so they have some good stuff if you have small feet or don't like big tac boots. 

The omega is basically a lightweight polishable Chelsea Boot with steel toe & electrical dissipation.   Looks good with jeans too 👍  I wear them off duty.  

I got to input into the design of the boot to make the black colour way more suitable for security & EMS, so I'm fond of it for that reason as well.
[is3k928] (score 2, diepte 2) Lol, no.  I work on a college campus and am tired of the OT....  Anyone looking for a job in southern WI?   Lol
[is0oqun] (score 2, diepte 1 OP) Your employer provided boots!?
[is0ryxg] (score 2, diepte 1) Like buffalo bill from silence of the lambs?
[is214n8] (score 2, diepte 0) Magnum boots
[is361ud] (score 2, diepte 0) Been on sale for the last 2 years

https://botach.com/tru-spec-tactical-assault-9-black-boots-w-side-zip/
[irzzyq6] (score 1, diepte 0 OP) SFB**
[is0ccm8] (score 1, diepte 0) Vans with the flame pattern
[is2soj6] (score 1, diepte 1) 100% agree, the price point is awesome to!
[is3j8vx] (score 1, diepte 1) Is this one of the sponsors from Moab
[is0eut6] (score 1, diepte 0) High techs hiking boots
[is0hhzy] (score 1, diepte 0) Lowas!
[is0p4pz] (score 1, diepte 2) Yup. I got them in orientation. You can get a new pair once your original pair gets old , you just have to turn the old ones in . 

I work nights though , so  if I want new boots id have to drive to my site on my days off to get new boots from hr, or hangout after work and wait for them to show up , so that’s a pain in the butt .
[is156j1] (score 1, diepte 3 OP) Who do you work for fam
[is9w3kd] (score 1, diepte 4) I work a federal contract .
[is0ohat] (score 1, diepte 0) 8 inch Bates Zipside Durashocks.
[is0ve5h] (score 1, diepte 2) Like I'm retired and I don't wear shoes 90% of the time
[is0zbg2] (score 1, diepte 1) Do you also get a greatcoat?
[is10ban] (score 1, diepte 2) We do get a seriously big coat for like arctic blizzard conditions. I think I’ve worn once.
[is1cidk] (score 1, diepte 0) Worn out Bates, 6 years of keeping me on my feet.
[is1dwt3] (score 1, diepte 0) Black air force lows, classic
[is1g9zk] (score 1, diepte 0) Bates gx8 love these boots but might switch to oakleys soon. Edit also looking at some Viktos johnny combats there a local business here in Wisco I love there gloves.
[is1ge7e] (score 1, diepte 0) Blauer.
[is1vl31] (score 1, diepte 0) Danner Go Devil’s
[is1z3nl] (score 1, diepte 0) lowa's
[is1zuv1] (score 1, diepte 0) Cat threshold work boot.

Water proof, steel toe, electric resistant, slip resistant

Take a bit longer to break in than other boots but we’ll worth it!
[is21zfn] (score 1, diepte 0) Magnum boots. Idk what model tho. They are the metal detector compliant ones with zips on the sides. Idk if they are still made anymore
[is27x6b] (score 1, diepte 0) The cutest slip on shoes ever. They’re grey and have flowers. 

I just left the doctor.
[is29pjs] (score 1, diepte 0) My nice warm comforter cause its my day off. When I work boots.
[is29yw4] (score 1, diepte 0) Toes
[is2pu6r] (score 1, diepte 0) on cloud
[is2q6yx] (score 1, diepte 0) Right now I have 5.11 ATAC 2.0 Boots on. Been wearing thos style of 5.11 for the last 12 years.
[is2r9ge] (score 1, diepte 0) Under armour micro G’s
[is2rag2] (score 1, diepte 0) Black timbs
[is2s1qn] (score 1, diepte 0) Rocky SV2 Predator (Tan)
[is2slyd] (score 1, diepte 0) Merrel Moab 2s
[is2sz9t] (score 1, diepte 0) Beat to absolute hell doc martens loafers cause they are comfy.
[is2whk6] (score 1, diepte 0) Ariat groundbreakers steel squaretoe 👢
[is32jdf] (score 1, diepte 0) Got some Magnum Stealth Forces. Took a bit to work in, but now they are comfy and supportive. I usually get a bad pain in my plantar fascia but these don't hurt. My only regret is I bought a pair that's slightly too big and so I need to double up on socks lol
[is35t45] (score 1, diepte 0) A blanket NO socks
[is35uoi] (score 1, diepte 0) 10 Inch 5.11 Tactical Boots
[is39vsp] (score 1, diepte 0) Belleville khybers. The water/bloodborne pathogen variant
[is3a0xt] (score 1, diepte 2) Wtf?
[is3a4jc] (score 1, diepte 0) Solomon Gortex Ultra-4 

Or some shit like that
[is3dw5b] (score 1, diepte 0) SAS work shoes. Best in the game
[is3njtr] (score 1, diepte 0) Crocs
[is3rayo] (score 1, diepte 0) 5.11 Norris sneakers, if I have to wear boots 5.11 8” atacs
[is40f6s] (score 1, diepte 0) Rocky alpha force best boots ive ever had
[is41uob] (score 1, diepte 0 OP) Ultimate Boot guide for new guards right here
[is4q6sn] (score 1, diepte 0) Men's Logandale Waterproof Boot (Steel Toe) from [KEEN](https://www.keenfootwear.com/p/M-LOGANDALE-WP.html?dwvar_M-LOGANDALE-WP_color=1017828&cgid=work_mens_boots)
[isa0f9k] (score 1, diepte 0) Black Sketchers slip on's that I was gifted when I worked at a Starbucks Bistro, but worked just fine for security.  I used to wear Doc Martens, but they're a little heavy for the duration.
[is00sbf] (score 0, diepte 0) Boots
[is0s579] (score 0, diepte 1) You must watch the unsubscribe podcast ? If not you will cum to love it. 
r/unsubscribepodcast
[is06pvj] (score 0, diepte 0) 511 fast tacs
[is0f8r2] (score 0, diepte 0) A form of black boots with a side zipper. Missing a piece of my ankle so its the only way I can wear boots without screaming when I put them on or take them off. They have the label "BATES" on the side. Best pair of boots since my military pair I've ever had.
[is0k0ir] (score 0, diepte 0) Black Nike air force ones
[is0l0s8] (score 0, diepte 0) Haix Black Eagle
(11 reacties met lagere score weggelaten)

=== THREAD 8ch25c ===
SUBREDDIT: r/army
DATUM: 2018-04-15  SCORE: 33  REACTIES: 87
TITEL: Am I just destined to have bitch feet?
POST (source_id=post):
Long story short: My feet stayed severely fucked up throughout basic training. Even after 10 weeks my boots never seemed to be broken in enough and constantly fucked my feet up. The first thing I did after graduation was buy new boots. I have a pair or Rocky boots and a pair of Garmont boots. I have tried everything I can think of and everything that has been suggested to me and my feet are STILL getting fucked up, even with better boots. Wtf can I do here? The only thing I haven't tried yet is bleaching my feet. This picture is from today after wearing stockings under my socks (another suggestion). Fml. 

https://imgur.com/sqT1sbs

Edit to add what I've tried and that I also bought better socks (Fox River): I have tried putting pads, yes female pads, in my boots to line them. I have tried the black dress socks under my green socks. I have tried Body Glide. I have tried non-adherent dressing and gauze. Foot powder. Stockings under my socks. Etc, etc. 

Edit #2: I do not think they are too large. The size below what I have now I cannot fit my foot into.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dxeuv3b] (score 36, diepte 0) Jesus, dude.

Okay, first off, your heel shows that the boot is rubbing, so you've got a lot of movement.  Are they too loose?  I can't see that much movement happening without them being too large.

Secondly, it looks like your lower heel is showing signs of heavy callusing.  That might sound like a good idea, and I used to think it was, but our medic pointed out that heavy calluses are inflexible and can crack; you don't want that.  Get a pumice stone and use it in the shower while your feet are wet.  I still get calluses on my heel and the ball of my foot, and try to use the pumice stone daily on them.  It isn't vanity, it's practical.

EDIT:  Also, if you're peeling your blisters, stop doing that.  If they've got a lot of fluid, only drain them if you must.  If so, just drain them and put a bandage or moleskin or something over them.  Leave the skin on them while they heal.
[dxeur4i] (score 30, diepte 0) Have you tried soaking the boots in hot water and then wearing them while still wet?  Also each pair of boots will give you different hot spots. Wear mole skin on those hot spots. Remember to round the corners and dust with foot powder so the edges don’t stick to your socks. Airborne ranger here so I speak from experience
[dxew5t4] (score 29, diepte 2) Are you tired of the same old military?
[dxexbhf] (score 29, diepte 3) Are you a high-speed death machine trapped in a douchebag's body?
[dxeut0u] (score 24, diepte 1) Ranger that
[dxev2rh] (score 23, diepte 1 OP) That's the thing .. they aren't blisters in the "normal" sense of them having fluid and looking like regular blisters. That is literally how my foot looked after I took my boots off. It's less like your typical blister and more like it just literally peels my skin off.
[dxeyxnu] (score 22, diepte 0) Are you female??? Cause women have smaller heels. That is why they make female boots. As a female, if I ruck in men’s boots I get bad blisters. If you are a male with thinner heels, maybe try female sized boots. 

Edit: spelling
[dxfc561] (score 17, diepte 3) > I’d soak them on a Friday and wear them on Saturday and Sunday. 

Just wear them on your weekend ruck march with your TL after soaking them.
[dxevg29] (score 15, diepte 2) What did it look like before you put the boots on?  Healthy?  You might have formed a blister and torn the skin off all in one ruck march, to be honest.

Really, that degree of blistering seems indicative of too much movement on your foot.  I never wore doubled socks or anything, and never hit that kind of blistering.

Quality of boot is important, but proper fit is *more* important.  I'd rather wear meh boots that fit properly than high quality boots that fit poorly.  Are you wearing a half-size too large?
[dxf0b3p] (score 15, diepte 1 OP) Yes, I am female.
[dxev5du] (score 12, diepte 1 OP) I assume soaking them and wearing them molds them to your feet? I haven't done that.
[dxewz9c] (score 12, diepte 2) Yes. It breaks them in faster. I’d soak them on a Friday and wear them on Saturday and Sunday. It helps to have waterproof socks.
[dxfi09g] (score 11, diepte 4) No there’s a hill to die on...
[dxfijbt] (score 10, diepte 6) CAC Card. Embrace it.
[dxeuzh1] (score 9, diepte 0) I have bitch feet as well. I cut the heel cup out of my issues boots and it’s made a world of difference. I wish I had known to cut out the heel cup while I was in OSUT. 

I’m going through phase 1 with you at OCS and my understanding is we have to wear the issued boots. But I believe we can use other boots on the rucks and land nav.
[dxf41nh] (score 9, diepte 2) A few companies make female army boots, Belleville, Rocky, Nike... If you are at a big post clothing and sales will definitely have them. The box will be marked. Ask a sales person to help, sometimes female boots are in the back.
[dxfc7wu] (score 8, diepte 0) Bitch feet aren't the end of the world. Why, I can think of someone with bitch feet that rose all the way to become president of the United States.
[dxfdkh6] (score 8, diepte 0) You need to learn about tincture of benzoin, threading your blisters, and proper boot fit. My friend, you need to read Fixing Your Feet

https://www.amazon.com/Fixing-Your-Feet-Prevention-Treatments-ebook/dp/B004K6MDZU

As a guy who has spent more time on his feet than your mom has on her knees, I recommend this book more often than just about any other for anyone who has to move out, under weight, double time.
[dxevwns] (score 7, diepte 3) It's an open secret inside tradoc how awful the newer frankenstein looking issued boots are.
[dxfcmkz] (score 6, diepte 4) Only if you have waterproof socks. You don’t want to do a footmarch with damp socks
[dxfbvzo] (score 6, diepte 3) Maybe he has extremely narrow heels. My right heel is fairly narrow and if I don't wear good, thick socks I'll get a nasty blister like that. My left foot fits every boot I've ever owned like a glove. Wish my right one was a mirror image of it.
[dxf1ej8] (score 5, diepte 1) Interesting. I didn’t realize there was a difference. How do I find female versions of boots?

That’s actually my problem. I went to fleet feet after OSUT to get my foot mapped. My upper foot is almost an XX wide and my heel is almost as narrow as you can get. I would be down to try a females boot.
[dxfcfc0] (score 4, diepte 4) god i fucking love that video
[dxewo5x] (score 3, diepte 5) Each issued boot brand fits a little differently.

I couldn't wear the old altimas issued boots. The toe box was painfully small compared to the Bellevilles or bates
[dxewfn3] (score 3, diepte 0) Rocky’s are a great sturdy boot but that back heal is tough as hell. I tried all the tricks to fix it too...nothing worked. 

Started rucking in Oakley’s. Essentially a tennis shoe feeling boot. It offers NO protection but I had zero rubbing on the heel.    That is my suggestion.
[dxfiuty] (score 3, diepte 8) The army can be dumb, but it’s impossible if you sweat the small stuff. I will be less stupid if you try to relax.
[dxg5o1r] (score 2, diepte 4) RRRRRRAAAAAAAAANNNNNNGEERRRR SKKKOOOOOOL
[dxfgtja] (score 2, diepte 4) Yeah, somebody else mentioned having wider feet.  If he wears regular width boots with narrow feet he'll end up getting something too long and it'll let his heel move too much.
[dxexz5c] (score 2, diepte 6) Just seems like there would be a bigger emphasis on issuing boots that fit. 

Once your feet are gone you’re useless.
[dxf8n5u] (score 2, diepte 2) They don't care what boots you wear in OCS.
[dxfkgwq] (score 2, diepte 2) No. State OCS.
[dxexkyu] (score 2, diepte 0) The Fox river aren't that great,  i have found some nice Black wool socks i use.
[dxey5a0] (score 2, diepte 0) You need some turbulent juice

https://youtu.be/39R9YLACjJY
[dxfbyyh] (score 2, diepte 3) Clothing sales. Where they sell clothing. Not, despite what the idiots say, "Clothing *AND* sales"... they sell clothing and sales there?
[dxfkgoe] (score 2, diepte 2) TBH: podiatrist if the issue is persisting despite your best efforts.
[dxf8gkn] (score 2, diepte 0) How secure are your boots to your feet? Are you doing the heel taps before you tie your laces? Looks like either loose boots or poor fitting ones.
[dxfc7ck] (score 2, diepte 2) The lotion works some of the time, but for the most part my issue comes from sweating all the time and excessively. Dermatologist offered me botox at one point, but botoxing my feet seemed a little extreme. So I go from wet to dry a few times a day. On the civilian side I end up in a similar circumstance but have to wear impermeable boots and a full level-a periodically. The lotion helps to soften it, but the blade basically removes the rough and hard edges from the cracks that the pumice stone pulls on when trying to remove them but without the shearing force. Once I get those off, I just use a pumice stone. Most of the time they only come up when I've had a few days in the field or a few days in level-a gear, and lotion during those times basically washes off. 

Once the cracks start (https://imgur.com/a/iQdSy taken today two weeks after last shave-down) they're small, but a pumice stone won't really do anything to them even after a long shower, so they'll end up as raised areas while the rest of the heel is smoothed down. I can get them with a rasp, but those end up taking off more than just the cracks when I use them enough to remove the cracked part, leaving me with raw spots. Once regular pumice stone use takes care of everything else, I can shave off the raised parts fairly easily without taking off any of the rest of the skin. 

I've considered just filling up my socks with petroleum jelly on the regular, but to be honest that's a tough feeling to handle and I'd feel a little too grapes of wrath for me. Also, the cracks still come with socks filled with petroleum jelly at exposures up to two weeks and that was about as much as I could handle. Cuticle oil is about the only thing that softens the cracks, but they still hold their ground pretty well against pumice stones. The amope (sp?) things aren't bad for regular maintenance, but still pretty much fall into the same problem as pumice stones, just leaving the edges of the cracks in place. Dremel with sanding bit will remove them but gets way too hot. 

TLDR: sweat too much and too regularly for my feet to remain pretty unless I just wear chanklas 24/7, which wouldn't rate well.
[dxfhdbr] (score 2, diepte 4) I went all in after a few times having them actually split. Put on an older pair of boots so that I wouldn't feel bad if it stained everything (it looked like an oil slick because of the sweating). Slipped, slid, tried different (more worn-down) socks, slid less, and tried. Basically the edges of the cracks felt like well-oiled leather instead of like cracked fingernail. So it was an improvement in a sense, but totally didn't stop them from splitting. 

2/10 do not recommend it. I basically broke down and tried the safety razor because I had an extra laying around after I doubled down on a nicer one. You've gotta be really dilligent with making sure that the blade doesn't get too loose (slice off too much). Always felt like I was adjusting a microtome when I was doing it, but it isn't all that different.
[dxfdo30] (score 2, diepte 0) I haven't worn issue boots since they were black leather. 

I've got freaking duck paddles for feet. Wide as hell, actual arches, narrow heel. Standard issue, Rockies, anything padded doesn't let me lace in tight enough to prevent heel movement. The boots I've worn for the last three years are Belleville One Xeros. Yes, men's sizes; I wear a 4W. Even then, I've got zero space on the sides, but because they're canvas, I can aggressively lace to conform to my 7 1/2 inch ankles. The last pair I bought was $145 at Clothing Sales. 

Like someone else said, colloidal bandages are the shit. I broke my big toe a couple years ago and it healed crooked. Rucking more than 3-4 miles blisters the hell out of that toe joint. Unlike a heel, I can get silicone toe sleeves, but before I discovered them, I used a colloidal bandage beforehand, and didn't blister.
[dxfw0vb] (score 2, diepte 0) It might sound crazy  but when I have to go on long as rocks or anything like that I put medical tape then duct tape over my trouble spots.
[dxgbkol] (score 2, diepte 0) After reading this thread I have a new found appreciation for my Flintstone feet
[dxgfrw7] (score 1, diepte 2) They are traditional blisters, they were just denied the opportunity to heel because the top was rubbed off. They are going to hurt like hell for awhile. I would apply a bunch of neosporin to some gauze and put a moleskin patch over it. Moleskin is life. You can buy a giant roll that will last you years.
[dxew7m0] (score 1, diepte 4) Yeah the Rocky’s are awful. 

My unit had an old sand mcraes they gave me to help out and they’re a million times better. Unfortunately they’re just not as wide as the Rocky’s so they hurt my foot in another way. Hoping I can get them stretched out before June.
[dxff6f6] (score 1, diepte 3) We are doing state OCS through the guard so they do care about the trivial stuff.
[dxgbgxh] (score 1, diepte 4) State? I lane walk every year for WA's OCS.
[dxi8g0u] (score 1, diepte 5) It’s for the Phase 1 when SC, NC, GA, FL and PR go through it together. 

I believe after that we can wear whatever.
[dxfhnkr] (score 1, diepte 1) Federal OCS? You can wear any boots you want.
[dxfkr7s] (score 1, diepte 3) Oh. Well I can't help ya haha
[dxexevh] (score 1, diepte 0) I solved this problem by buying my own boots, Rockies or Bates specifically. Still can’t ruck in issue boots.

Looks like you might need tighter boots maybe. Or some boots are more flexible than others which might help. The Rockies enhanced jungles were even easier on my feet than my old Rockies because they’re more flexible.
[dxeyjin] (score 1, diepte 0) Yeesus. Get better fitting boots, dude. That’s not supposed to happen.
[dxfi7qt] (score 1, diepte 5) Just because the idiocy is widespread, I shouldn't try to fix it?
[dxfizil] (score 1, diepte 9) I'm out, and very relaxed.
[dxf495d] (score 1, diepte 2) A few companies make female army boots, Belleville, Rocky, Nike... If you are at a big post clothing and sales will definitely have them. The box will be marked. Ask a sales person to help, sometimes female boots are in the back.
[dxfb9nz] (score 1, diepte 2) They use different lasts, which are the foot models that shoes are formed around.
[dxezfvl] (score 1, diepte 0) You know that doctors exist...for your feet. A podiatrist can make custom made insoles to put in your boots.
[dxf08y8] (score 1, diepte 1 OP) Yes, I'm aware. I was hoping that it would not be an issue once I got better boots. Obviously that is not the case.
[dxf0j1i] (score 1, diepte 0) I don't like fox river socks. Even with foot powder my feet got super sweaty wearing them, and that can contribute to blisters and other problems. Darn Tough makes the best socks hands down. And don't double sock that just makes it worse. Aside from that make sure you get boots that are snug around the heel and ankle, it looks like your heel is sliding up and down in your boots and that not good, and don't let your foot slide back and forth, but give your toes some space. It looks like you may be wearing boots that are ether to wide or a half size to large.
[dxf0zff] (score 1, diepte 1 OP) I don’t think they’re too large. Anything smaller I can’t even get my foot into. My feet sweat ridiculously bad though.. I mean, really bad. It’s pretty gross. I wonder if that’s a big part of my problem.
[dxfsih1] (score 1, diepte 2) If your feet are wet, that is a big problem. I have that problem with sweaty feet and can't get by without silk socks against the skin with wool (no cotton nor poly) outer socks if cold weather or just the silk in hot weather. I had matterhorn gortex boots for cold weather and was ok with issue or jungle (odg) for hot weather.
[dxg8h60] (score 1, diepte 2) yes that's a huge problem, moisture either from swampy fort knox type weather and/or perspiration plus friction equals blisters. I also have sweaty feet. Foot powder after baby wipes (let your feet dry first). The baby wipes help get rid of the bacteria that contribute to sweat. Make sure you're using shower shoes in public showers and scrubbing your feet with soap inbetween the toes and shit all over and rinsing them well. Let them air dry on your downtime. I also used wool socks but I used a wool blend, marketed as a hiking sock. They're not super thick but much thicker than issues socks. Look for moisture wicking.
[dxgpgop] (score 1, diepte 2) Have you tried wearing the standard issue socks? If your feet sweat, most anything in majority wool, polyester, nylon, or acrylic will just make it worse since these are all insulating material. Cotton breathes much better, it's why we don't use it for winter gear. Read the composition tag before you buy your socks, you want a sock that's at least 80% cotton / 20% poly or nylon (if you've ever worn your socks through the heel, the poly/nylon is the mesh frame looking stuff that gives it structure), but if you can't find that or better, nothing below 70% cotton / 30% poly as an absolute rule. Fortunately, I know for a fact that the cheap, issue socks tend to be at least high 70s, more depending on the maker. Unless they've changed the composition since I got out.

Definitely take some time off your feet until your blisters and stuff are healed. Make sure your boot is snug enough that your foot doesn't slide when you walk or ruck. Spend a day of your off time acclimating,  fully loosen the laces before you slide your feet in and tie them as tight as you can (within reason) and take a walk to the PX or something. If there's still slippage, or rubbing, it means they don't fit. You may not need another size, it may just be the boot and your feet. Finally, don't put powder in your boots. A lot of soldiers do it as a temporary solution, but in the long run it just makes conditions worse. Anything you apply, whether it be creams, tinactin, or powders, should go directly on your feet.
[dxf1mfw] (score 1, diepte 0) My heels used to look like that after rucks in basic.  The only thing I could do was wear the green socks with black socks, with 2 layers of moleskin on the heels of the black socks, and a double layer of bandaids on my actual heels.  Doing all of that shit in the morning made me late to formation a couple of times. 
I have narrow heels, btw.

I bought a pair of Danners after basic and that solved the problem.  Maybe you aren't getting the right size?
[dxf23fb] (score 1, diepte 0) So as a fellow chick with shitty feet, this is what I’ve found that works for me:

First, the boots I wear for rucking are boots I’ve had for a long ass time. They are pretty beat. I added a running insole to them for the arch support, which I find I need on rucks.

Then I wear a compression sock. They’re so tight it takes me like 4 minutes to get them on.

Then over that sock I wear a very thick wool sock. A nice pair. They were expensive AF but worth every penny.

Also, I always powder my feet before I put my socks on. Not a lot, but enough that I have powder between my toes.

Since I started doing this, I haven’t gotten a single blister. Or any friction burns. Got through a 12-miler last weekend with no foot issues at all :)

Good luck at Phase I. It’s not the worst. 💪🏻💪🏻💪🏻💪🏻
[dxf3nlc] (score 1, diepte 1 OP) Any specific brand of compression/wool socks?
(24 reacties met lagere score weggelaten)

