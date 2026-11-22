# Label-batch batch_0119

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
Schrijf het resultaat naar `batch_0119.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1m58j1r, eu7g58, 673pqf).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1m58j1r ===
SUBREDDIT: r/cna
DATUM: 2025-07-21  SCORE: 42  REACTIES: 70
TITEL: So what type of shoes are we wearing? (My feet hurt! 12hr shift)
POST (source_id=post):
I hate these shoes! They were okay for 3 months- but had a hectic weekend! Never had the chance to sit down during shift. Any recommendations for shoes? Something breathable, wide foot friendly, 12+ hours on feet?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[n4a673o] (score 24, diepte 0) Insoles are where it’s at. Superfeet, the orange ones.
[n4a5vc3] (score 21, diepte 0) I’m
Not a fan of brooks either

Hoka Clifton’s and compression socks
[n4a5r51] (score 9, diepte 0) I go between my brooks and my cloves. The brooks are 1000000% worth the price tag
[n4alhkd] (score 8, diepte 1) My podiatrist recommended me the blue ones for my plantar fasciitis. What’s the difference with orange?
[n4a9hlf] (score 7, diepte 0) I’m living the Ortho Feet life and they last well beyond anything else I’ve tried. This job gave me plantar fasciitis and they’re the first shoes to give relief. Highly recommend them if you’re always in pain in your heels and knees, and they’re slightly cheaper than the trendy ones(still will run you over $100 but mine have last over a year).
[n4bxwyo] (score 6, diepte 1) Yo, my Hokas were the best. But I’m ngl, my facility runs into some sticky floors (urine, juice spills, etc) TELL ME WHY THE LITTLE RUBBER PIECES ARE STARTING TO PULL OUT OF MY HOKAS 😭 Waste of $150, I do not recommend them for CNA use, maybe running or hiking. I just tried on a pair of Lululemon Blissfeels, I am buying them with my next check 😭
[n4abv2x] (score 6, diepte 0) I loved my New Balance Fresh Foam
[n4anlu3] (score 5, diepte 2) I have plantar fasciitis as well. My podiatrist recommended the orange ones. They are high impact every day ones so I think the idea is that they are good for my feet even after my PF has calmed down
[n4awy5o] (score 5, diepte 1) Crocs arent allowed at most facilities
[n4a852l] (score 4, diepte 0) Docs with an in sole
[n4atmuj] (score 4, diepte 2) Crocs has a line for healthcare. It is a solid shoe clog, just like Dansko clogs but more comfortable.
[n4aq3ic] (score 4, diepte 0) Skechers!!!
[n4dfpwq] (score 3, diepte 2) How long have you had the hokas? Running shoe internals typically break down before anything external so if they start falling apart it usually means they're overdue for an upgrade. Glue is also massively inconsistent on most shoes so it's possible it was a manufacturing defect and you could reach out to support.
[n4a69dz] (score 3, diepte 0) I wear crocs. Not crazy about the little bead things on the soles, but they're super breathable and can be dried easily
[n4aap9e] (score 3, diepte 1) Try the baya clogs they’re just a bigger croc version but way more comfortable and they have cool colors
[n4b3jmm] (score 3, diepte 4) Mesh shoes can be just as gross (to me at least). I'd much rather change my socks and wipe my shoes down with a purple top wipe than change my socks and still have to wear the wet / gross mesh shoes. 

They make closed crocs though, so it's the best of both worlds
[n4b68qc] (score 3, diepte 6) I do see what you're saying, and I understand why the ones with holes are banned in a lot of places (sharps and stuff like that). I've even seen people wear them without socks (I agree that's unsanitary, but that's their choice). The floor is nasty no matter what type of shoe someone wears. If it touches the floor, it either gets trashed or goes in the linen barrel. No five second rules honored here. 

I used to be anti crocs, but after wearing new balances and several other types of mesh shoes, being able to easily wipe them down after my shift (or as needed) is a huge plus. That being said, I do my best to keep stuff from touching me or my shoes, but sometimes it happens, and it's just nice to be able to wipe it all down. I also keep a separate laundry basket for my scrubs to keep them from mixing in with my regular clothes.
[n4aahjb] (score 3, diepte 0) Crocs .. tried the expensive stuff like three times and always come back ..
[n4aamis] (score 3, diepte 0) I wear Brooks Trace 3 rn because they were on sale, the tongue refuses to stay in place but they keep me comfy. I stand by Hokas though
[n4adiza] (score 3, diepte 0) Crocs with compression socks put an end to after shift pain.
[n4afgxx] (score 3, diepte 0) Non slip, water resistant shoes. I used to wear shoes like yours until a catheter bag spilled all over my shoe once.  I can’t find the exact model but here’s the link to a similar style that’s very close: 

https://www.skechers.com/work-relaxed-fit-squad-chaos-sr---rodey/108181W_BLK.html?campaigntype=shopping&src=paidmedia&gclsrc=aw.ds&gad_source=1&gad_campaignid=16706650483&gbraid=0AAAAAD-OiPLwdz-OeIO31GnS5GMTdRawg&gclid=CjwKCAjwp_LDBhBCEiwAK7FnkoXxuOQEu0qyKPxjJ1WVc7-c-k-gQv_mCDLmPkMSKrsl-fWvrRUefhoCNg4QAvD_BwE
[n4gy01o] (score 2, diepte 1) I was so excited to splurge on a pair of voices.  They felt amazing for a couple weeks, then like any other shoe.  After about a month I started getting symptoms in my feet that point to f***ing peripheral neuropathy 🙃  I asked a couple other girls at work who I knew owned some about them (noting that they weren't wearing them at the time).  Both responded with something like 'they were amazing at first.. but soon made my feet hurt worse than any other shoe'
[n4cvq57] (score 2, diepte 2) Hokas are also too soft and mess with your ankles.
[n4b6hmg] (score 2, diepte 2) Fr normal soles are terrible. Only reason I ended up with docs was they last longer then teniss shoes
[n4heom9] (score 2, diepte 4) Plus the most important factor. Drip 😎
[n4oswu1] (score 2, diepte 1) I love Ortho Feet. I have their slippers and wearing something on my feet at home really helps keep my feet rested in general.
[n4acd5v] (score 2, diepte 0) Hokas+Compression socks
[n4cowu7] (score 2, diepte 1) I love crocs but our facility won't allow them. At first it was "no holes" found ones without holes so they fussed about "no heel" despite me literally having the strap around my heel 🙄
[n4aeyyu] (score 2, diepte 0) Saucony FTW 🙌 Even with having EDS and FMS/ME and DDD they work.
[n4ah8xc] (score 2, diepte 0) Financially not the best decision; but I usually buy 2-3 pairs of the same kind of shoe. I have 3 pairs of these[these](https://www.vans.com/en-us/p/shoes/ultrarange-5140/ultrarange-neo-vr3-shoe-VN000CWEUUI).  


I got them on sale though. Sometimes I do 16+ hour shifts, and I still find them bearable. They’re not waterproof though.
[n4glp0u] (score 2, diepte 1) Underrated!! I get mine at costco so theyre super affordable too. Combined with compression socks its a godsend. Lots of my coworkers wear sketchers too, were j not willing to throw $150 on shoes thats at high risk of getting nasty dirty when theres a MUCH cheaper option that does the job j as well
[n4ostt4] (score 1, diepte 3) Hokas make more than just Cliftons. Stability and balanced designs are ankle supportive. Gaviotas 💚
[n4hhqpl] (score 1, diepte 3) I actually bought them around the beginning of this year, I’m not surprised to hear this. I’ll definitely look into their support team, thanks!
[n985bk9] (score 1, diepte 2) Omg, mine have started to do this and I was like what is happening… thank you for solving the mystery. I’m trying cloves now.
[n5642wo] (score 1, diepte 1) It angers me how nurses are treated. 12 hours without a break? CMON.
[n4ansmd] (score 1, diepte 3) Sounds like a bad justification to getting dookie on your piggies but go off twin
[n4aoi72] (score 1, diepte 4) I tried to get them to change it but i guess they prefer to risk losing a settlement on a technicality
[n4atybz] (score 1, diepte 4) Google is not hard to use and it is free where you are. https://www.crocs.com/c/shop-by/activity/healthcare-shoes?gclid=Cj0KCQjwyvfDBhDYARIsAItzbZEYLg0MN3rAiimBECWe0darM3kZ9mwPN42hqbnqWkPB_u5jL0wPDicaAoR6EALw_wcB&adid=ppc_google_us_brand_healthcare_searchgooglebrandwork_x_x_x&ef_id=Cj0KCQjwyvfDBhDYARIsAItzbZEYLg0MN3rAiimBECWe0darM3kZ9mwPN42hqbnqWkPB_u5jL0wPDicaAoR6EALw_wcB%3AG%3As&s_kwcid=AL%214035%213%21445627795438%21e%21%21g%21%21crocs+for+healthcare&gad_source=1&gad_campaignid=29649880
[n4b3w04] (score 1, diepte 5) Could you be any more condescending? I said two comments above, what you’re talking about. But go off twin
[n4bgyoc] (score 1, diepte 6) I got you 👍
[n4ax15i] (score 1, diepte 1) Crocs aren't allowed at most facilities
[n4b2vb4] (score 1, diepte 2) That's a bummer. Most types of crocs are allowed in mine
[n4b3164] (score 1, diepte 3) Its the open-ness of them. Open shoes are unsanitary.
[n4b3s43] (score 1, diepte 5) Also gotta think about the other way around. What could you be exposing the pts to? All sorts of lovely things like to live on feet.

That being said, I personally dont care what you wear as long as they are non-slip. Im just pointing out the motives behind them being banned most of the time.
[n4aqkzg] (score 1, diepte 1) i 100% second this, especially with scholl innersoles
[n4gvg2n] (score 1, diepte 3) they last so long, are shower proof, being run over by a hoist proof and good for ur toes!!
[n4bmkx2] (score 1, diepte 3) Behaviors such as name calling, sexual comments, being generally overtly hateful, spamming another user, general inappropriate/unhelpful comments or posts, or being unnecessarily hateful, condescending, discouraging, or unprofessional to our profession, to nurses, or towards residents/patients will not be tolerated. Posts or comments found to violate any of the above will be removed.

Inappropriate comments made that are found to be racist, homophobic, transphobic, xenophobic, negative towards the homeless community, hate towards anyone’s physical appearance, including weight, or containing hate towards any marginalized group will be removed. Repeated instances may result in a permanent ban.

Comments that are inciting violence, suggestive of committing abuse/neglect, suggesting falsification of employment documents/job experience/resumes, HIPAA violations, suggestions of poor conduct at work, or grossly unprofessional will be removed. 

Please remember that there are folks from other countries, races, religions, political backgrounds, languages, etc. than yourself. Refrain from posting or commenting anything related to religion (or forcing beliefs on anyone), politics, or highly divisive statements that have the potential to insult or upset someone. Be cognizant of other’s beliefs and culture.
[n4aovpr] (score 1, diepte 1) Same. So comfortable.
[n4bro18] (score 1, diepte 1) Also have these in wide and I love them
[n4gn1f5] (score 1, diepte 1) Definitely #1 for me fresh foam new balance with a road runner steel reinforced shoe implant usable for multiple other shoes
[n5894hg] (score 1, diepte 1) What kind of hokas for wide feet especially?
[n58thut] (score 1, diepte 2) I wish I could remember which ones I got because I also have wide feet, but I’ve had them for so long that all identifying marks have been rubbed off. I BELIEVE they were a Bondi model but I can’t say with certainty. They are very flexible though, so I want to say they would all fit and be comfortable.
[n4ad5y5] (score 1, diepte 0) Brooks, Cloves, Docs, and my knockoff Hokas (Allswifit? They look the same). I cycle through my shoes constantly because of how many hours I work. I also sometimes buy the Walmart runners, and they're not bad. Tried the Stand+ (formerly Gales), hated both styles I tried. I have a couple pairs of Crocs, they're usually for when I'm extra swollen from too many days in a row. Compression socks are a must, as well as insoles.
[n4ajohf] (score 1, diepte 0) My Hokas were my life saviours
[n4b6oiw] (score 1, diepte 1) Same!
[n4ak1j3] (score 1, diepte 0) On cloud
[n4akuwh] (score 1, diepte 0) What’s good for people with insoles and wide feet? I got the hoka bondis in wide but they’re too tight with my insoles in. Should I try the extra wide or a different shoe?
[n4b6hhy] (score 1, diepte 1) Have you tried on an extra wide? I normally have a narrow foot but has to return my first pair of Bondi 9. I got a wide and went up a size and they are the most comfortable shoes I have ever worn and my legs are not tired at the end of a shift albeit an 8 hour shift, not 12.
[n4b6o2k] (score 1, diepte 2) I just saw you asked about the extra wide. Definitely give it a try. At the time I bought them I was wearing an AFO brace and would remove the Hoka insole to put the brace in. A couple weeks after wearing the Hokas I didn't need the brace anymore. Good luck!
[n4amukn] (score 1, diepte 0) Crocs. But not the kinds with the holes. They’re the ones they make specifically for working. I have tried shoes all the way from $170 Hoka Clifton 9s to $20 Walmart brand and these crocs make standing for long periods of time so easy I have to remind myself to sit. And they were like $40 (or $60 can’t remember but waayyyyy cheaper than my Hokas)
[n4amuvp] (score 1, diepte 0) Save the hassel of worn shoes every other month and get Nike, New Balance, or some Brooks. They cost more but theyre worth the comfort
[n4aozbo] (score 1, diepte 0) Love my Hokas!
[n4axnml] (score 1, diepte 0) Flat canvas shoes. So much of your job is advertising
[n4b3lwo] (score 1, diepte 0) Adidas ultraboost DNA, the only thing that gets me through busy ER night shifts
[n4bifgl] (score 1, diepte 0) Hokas changed my life. They are pricey, but absolutely worth it.
[n4bru8a] (score 1, diepte 0) I recommend going to a running shoe store and get fitted- game changer for me and kept me from having to spend over $100 on shoes I’m not even sure about
[n4bwj9e] (score 1, diepte 0) ON
[n4bzco1] (score 1, diepte 0) skechers slip ins with compression socks. the compression socks are a life saver.
[n4etwh2] (score 1, diepte 0) Brooks GTX, custom insoles and compression socks
[n4ffsvu] (score 1, diepte 0) When I worked as an aide, my Adidas were my BFF. I am in sterile processing and brooks are my go to.. compression socks always..
[n4m3mua] (score 1, diepte 0) Crocs!
[n4mcizr] (score 1, diepte 0) compression socks and a pair of oncloud cloud monsters
[n4aatpy] (score 0, diepte 1) Crocs are likely not compliant with your facility’s infection control/workplace safety guidelines, unless they’re closed toed clogs. 

Also, gross
[n4gy2jv] (score 0, diepte 2) Pretty sure it's because they look trashy af and not anything to do with safety
[n4an1u3] (score -2, diepte 2) If theyre like other places, they word the rules all stupid like and specifically say Crocs which is a brand and not a shoe 😉
[n4abh4e] (score -4, diepte 1) Crocs are likely not compliant with your facility’s infection control/workplace safety guidelines, unless they’re closed toed clogs.

Also, gross

=== THREAD eu7g58 ===
SUBREDDIT: r/Construction
DATUM: 2020-01-26  SCORE: 29  REACTIES: 70
TITEL: Timberland Pit Boss killing my feet - Recommend another brand?
POST (source_id=post):
Just spent a day working in a tight mechanical room and left with blisters on the backs of my heels, front and underside of my feet. I think it's time for new boots. I've had Timberland Pit Boss. These have been ok for site walks on concrete, deck, and dirt. I've almost always worn them with thick wool llbean socks.

I need suggestions for: a steel or composite toe 6" boot and insoles. For insoles I've used Superfeet orange. I've looked at Thorogood, Carolina, Danner, and Keen. I've read mixed reviews on RedWings durability. I'm willing to spend up to $250ish if I can find something nearly as comfortable as my LL Bean Cresta Hiking Boots. What do you like?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ffm89gr] (score 27, diepte 0) Red Wing King Toe. Easily best boot I have worn. And yes I have had red wings in the past with questionable durability so I understand your concern, but these have taken beatings day in and day out. RedWings nowadays are hit or miss. But Concrete, mud, stone, mortar, epoxy, nothing has done anything besides small scratches or stains. 1.5 years and still totally waterproof too. Most guys on site have them and enjoy them. 

I did an 8 mile hike in them and had no blisters or soreness besides the pain you get from hiking 8 miles unprepared (forgot to turn around at the fork and made a loop instead, so 4 miles turned to 8)

Also the toe is super roomy. You will not have crunched feet under the toe, and the tread has not worn down either.
[ffm7oe2] (score 11, diepte 0) It almost sounds like you are not wearing the right size boot. People's feet change with age and, uh, milage. You may want to go have them properly sized again. 

Also, I switched from the Superfeet inserts to the Keen K20's a few years ago and couldn't be more pleased. The Superfeet are great for running - in running shoes - but suck for working in boots.
[ffmtj5o] (score 8, diepte 4) It’s an insole, not a boot
[ffmhvc1] (score 8, diepte 1) Plus one for the king toe.
[ffm8wuz] (score 7, diepte 0) Georgia Boot.
[ffmhml2] (score 7, diepte 0) I've been wearing the Thorogood American Heritage emperor toe 6 for about a year and a half and they feel great still. At the end of a 12hr + day I don't even notice them. No insole other than what comes with the boot and darn tough socks.

I can't compare to the specific hiking boot you use, But my Thorogoods are more comfortable than any of the 5 pair of Salomon hiking boots or shoes I use.
[ffm9jgv] (score 6, diepte 1 OP) Thanks. I'll get resized this week. Also, the K20's look nice.
[ffmh3sb] (score 5, diepte 0) Chippewa super loggers. Expensive but it’s a real boot ! I do heavy road construction. Mainly utility work ,  constantly in mud ; I lay asphalt almost nightly.. jack hammering , the whole nine .. full blown wear and tear on these boots and I get an ENTIRE YEAR out of them .. with most other brands I barley get 7-8 months of heavy use. By far the best boot I’ve ever worn. They keep my feet dry in the mud and warm in the cold . Definitely worth the 320$
[ffmcue1] (score 4, diepte 0) I’ve never worn a more comfortable boot than keens, but the trade-off is that the bonded soles aren’t as durable or as repairable as a full Goodyear welt on a traditional boot.
[ffmfqvt] (score 4, diepte 0) Redwing Irish Setters are the absolute most comfortable boot I've worn. They felt more broken in than the year old boots I wore into the store.
[ffmhp7a] (score 4, diepte 0) White's Boots. Expensive but well worth it. Will last you 3x longer than the boots you just mentioned.

[https://whitesboots.com/](https://whitesboots.com/)
[ffmpnnl] (score 3, diepte 1) I actually wear a redwings TruHike or something? True hiker, or some variant of that.

They're all sorts of comfortable, waterproof, composite toe. I wear them on a mix of concrete, shot rock, dirt and gravel 8 hours a day, 6 days a week. A few scratches and minor cuts in the leather from my haphazard "my steel toe is almost as good as a hammer" way of working, but with a little mink oil every few weeks I haven't had any issues. Still waterproof after ~1.5 years.
[ffmpn03] (score 3, diepte 1) Best boot ever. I'm a farmer, one pair will last a whole year without leaking through. Aluminum toe for protection. I replace the insoles twice, as the stock insoles are junk imo. Can't go wrong and won't break the bank
[ffnduua] (score 3, diepte 2) They are worth ever penny. I promise. Make sure you have someone that knows what they are doing to trace your foot. Personally, I would go to their factory in Spokane. A few of my friends and I spent $600 on a pair. Comfy AF.
[ffmhpgv] (score 3, diepte 0) Red Wing.  Red Wing.  Red Wing.  You won't be disappointed.
[ffmw7sw] (score 3, diepte 0) [Thorogood Boots.](https://www.thorogoodusa.com/) When Red Wings started getting too expensive for me, I found these. Quality is on par with the best out there, made in USA, and they're super comfortable. I have a pair of the [American Heritage 8"](https://www.amazon.com/gp/product/B000I7H41S/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) with the composite toe, this is my brand for life.
[ffnb86x] (score 3, diepte 0) Thorogood boots are the best I've found. They're comfortable right out of the box - no break in period. Red Wings killed my feet for the first few weeks until I go them broken in. I seriously can't recommend them highly enough. When a pair failed on me Midwest Boots fixed them for free. 

[Link](https://www.midwestboots.com/product/TH804-4200-GWP501.html)
[ffncfpx] (score 3, diepte 0) Thorogood for sure. I’ve had a few different set of red wings but switched a couple years ago. Worth it. So much more comfortable.
[ffninsw] (score 3, diepte 0) Thorogood has been my go to for a long while. I've tried red wings, timberland's, diehards and a few others. But I also walk steel more than anything so YMMV.
[ffmdhpn] (score 2, diepte 2) No problem. The K20s will probably only last 12-18 months before they need to be replaced. But at $20/pair, who cares?
[ffmf99i] (score 2, diepte 1) I’m going to second the Red Wings. Even the Irish Setter work edition is worth every penny
[ffmf5xa] (score 2, diepte 0) Bruh......

http://www.redwingshoes.com/red-wing-shoe/3506-red-wing-shoes/3506-red-wing-mens-6-inch-boot-brown

They are a little portly....they feel great even after 10 or 12 hours on your feet. Provide waterproof, electrical hazard, a composite toe with extra room, and puncture resistance. I've been wearing mine for over a year and love them.
[ffmflba] (score 2, diepte 0) Get a pair of moc toe danners. Takes a minute to break in, but worth it.
[ffmfwz3] (score 2, diepte 1) Moc toe danners is the answer, love mine!
Edit: a word
[ffnbnnm] (score 2, diepte 1) Also on the Danner Moc Toe train here. Have had at least 1 pair in my rotation while I try other brands out (I always have 2 serviable pairs and switch every other day. They last a hell of a lot longer that way). I am almost at the point where it will just be 2 pairs of Danners. The do take a little while to break in, but they are a sturdy boot and, once broke in, are as comfortable as slippers.
[ffnolea] (score 2, diepte 1) There’s usually a handful of pairs on ebay that are blems to be had well under $200. I picked up two pairs and you would never know ow they weren’t 2nds.
[ffofjvy] (score 2, diepte 1) 100%. Super comfortable after you break them in and oil them. I’ve had my pair I don’t wear to work for 7 years now
[ffnee64] (score 2, diepte 1 OP) These? [https://www.thorogoodusa.com/product/804-4655/](https://www.thorogoodusa.com/product/804-4655/) Heritage – 6″ Composite Safety Toe – Emperor Toe Maxwear Wedge. Thanks.

My hiking boots are amazing. I've had them for 9 years and I wear them constantly when I'm not at work. They feel like slippers.
[ffncfxs] (score 2, diepte 1) Damn!! $400 a pair is steep. I get it, if they're worth it, than it's not that big of a deal, but it's hard to part with that chunk of change in one shot.
[ffnhlhn] (score 2, diepte 3) I believe you!
[ffnkrbd] (score 2, diepte 3) When I was a grunt in Korea, I had a custom pair of boits made. Tailored just for me. They are STILL a great pair of boots 20 years later. I get it.
[k4n5lt6] (score 2, diepte 4) Thank you for your service sir!!
[fg1k1iv] (score 2, diepte 1) Yeah, those are like the west coast version of Limmer Boots. Super expensive but super well made and durable.
[ffmkayo] (score 2, diepte 0) Timberland Pro is much more comfortable. They also wear out quickly. It’s a good trade off. I’d rather buy a new boot every six months than wreck my feet.

Keen has the same trade off. Comfortable, but they fall  apart.
[ffnor2p] (score 2, diepte 1) Like walking on air.
[ffng3o7] (score 2, diepte 0) Couple of tips for the younger folks in regard to boots. 1) always have 2 serviceable pairs. Rotate them daily. Your boots will last considerably longer (even more than the 2X longer that basic math will tell you). 2) Treat the boots like any other piece of equipment. Clean and oil them regularly and they will last even longer. 3) Buy your new pair about 2 months before you need them. Wear them around town, around the house, walking the dog, etc. Your feet will be greatful that you broke them in in small chunks over time. I usually buy mine in Fall, so I am not wearing boots in the summer/spring/warm weather. 4) keep a spare pair of laces or 2 in your truck/lunchbox/etc. You never know when you'll need them. 5) If your knees, ankles, hips, back or feet start getting sore regularly and you can't pinpoint why, it's time for new boots (or at least resole and change insoles if the uppers are in good shape). 6) Expensive boots ($150 - $200) are well worth it and will last for years if you take care as prescribed above. 

Source: Spent the last 19 years in work boots, on jobsites, working.
[fgbourp] (score 2, diepte 1 OP) Thanks. I got the Keen Utility boots in a shorter wider width than the Timberlands. My feet are wide and I've got high arches. The toe box and comfort of these felt awesome in the store. 

The Redwing king toe dug into the top of my foot where the steel toe meets the leather and in the back where my ankle bone is.

They didn't have the emperor toe Thorogoods and the regular ones kept digging into my small toe even at wide widths.
[ffpexcr] (score 1, diepte 5) Maybe help educate people before you tell them to shut their mouths.
[ffq8650] (score 1, diepte 6) *We were talking about apples and you came into the room like the Koolaid Man shouting* **oranges**

 Don't try and pin this on me
[ffnandv] (score 1, diepte 2) I have a pair of the Irish Setters and am not that impressed. I have had multiple pairs of Danners and loved them. The I.S. are comfy like slippers out of the box, bit break down rather quickly. Danners take a few weeks to break in, but last for SO long.
[ffnk6su] (score 1, diepte 2) I bought a pair of beat to fuck 6in King toes in a thrift shop for $15 and have never looked back. Comfortable and the shell wears really well along with the laces, best laces. I'm a little bias because they're a Minnesota union company. When you buy them just make sure you get the ones made in the USA.
[ffo26bn] (score 1, diepte 1) Yeah, I’m a custom stair builder so I’m up and down stairs with a pouch all day sometimes. I only wear the red wings. Anything else I’ve tried, and I’ve tried a lot, doesn’t measure up.
[ffmca2n] (score 1, diepte 0) Steel blue if they're availiable best boot I've ever worn
[ffmca55] (score 1, diepte 0) Outside work, like in the dirt and stuff, I use my 8” Wesco Jobmaster, Indoor, this is just what’s comfortable for me but, my Georgia Boot Romeo Slip on 😂😂 low or high top, if you can get past how they look, they’re a pretty comfortable anytime show with moderate grip and decent price
[ffmd459] (score 1, diepte 0) Took me 3 pairs of work boots to find a good pair. Justin work boots are about $200 but it’s the best pair of boots I’ve ever had. My Carolinas were the second best pair I’ve ever had and those are a little easier on the wallet. Never tried Carhartt but a lot of guys at work seem to like them. Worst pair I had was Caterpillar brand.
[ffme2oq] (score 1, diepte 0) Been wearing the wolverine I-90 for the past 6 months and I love them
[ffmxj3g] (score 1, diepte 1) Mine lasted about 4 years. Just last week I noticed the seem on my right boot had ripped. Still wearing them just now one boot isn't waterproof.
[ffnbf67] (score 1, diepte 1) I just posted the same (sorry I didn't catch your post first). I love my Thorogoods and have had the exact same experience as you. Darn Tough Socks are also the ticket. Kirkland Wool socks are a pretty close second, but they don't wear nearly as well as Darn Tough socks do...
[ffno5i1] (score 1, diepte 2) Those boots feel like slippers. Thorogoods are my most comfortable boots.
[ffno93i] (score 1, diepte 2) https://www.midwestboots.com/product/TH804-4367-GWP505.html

I wear the 8", which they apparently stopped making within the last year or so.

I've got 2 pairs, so luckily I can just get one resoled and wear the other.
[ffoig4a] (score 1, diepte 2) Those are pretty much it yeah, mine arent wedge and went with the darker color variant but the rest is the same
[ffnyl57] (score 1, diepte 1) I wear the 9 inch loggers mainly for the reason of needing 12 triples E's. Had them since October and love them. Brake in was about 60 ish hours.
[ffnkgpm] (score 1, diepte 2) boots that are tailored to fit your feet are going to be more comfortable than boots that are mass produced to fit an average sized foot

like wearing a pair of pants that you buy off the rack that kind of hang off you vs a pair of pants tailored to fit your waist and butt and legs so they look nice and are more comfortable.

[https://www.charlies-design.com/wp-content/uploads/2017/10/Bad-Fit-vs-Good-Fit-2.jpg](https://www.charlies-design.com/wp-content/uploads/2017/10/Bad-Fit-vs-Good-Fit-2.jpg)

tailored boots and clothing is definitely the way to go if you can afford it.

would love a pair of steel toe boots tailored to fit my feets, sadly out of my price range.

getting pants and shirts and suits tailored is pretty cheap though.
[ffoheco] (score 1, diepte 3) My Chippewas are damn close. Lots of size options
[ffndryi] (score 1, diepte 1) Danners are $175 and after initial break-in (they are admittedly tough out of the box), they are the most comfy boot I've tried. 19 consecutive years in construction boots to my credit. What I normally do is buy a pair and wear them as "walk around" boots for about 2 - 3 months before they make it to the jobsite. It's well worth it. I have a "retired" pair that are 6 or 7 years old that I use for yard work.
[ffmkw8a] (score 1, diepte 0) The Carhartt 6" safety toe hikers are my ride or die. To the point where I'm considering getting them resoled vs getting another pair (the uppers are fine, the sole is starting to pull away after 5+ years of use).
[ffn2rn9] (score 1, diepte 0) When I changed industries I had to completely change the type of boots I was wearing. After trying 3 or so different kinds out and returning them, I found the Irish setter kasotas. They've been great boots for walking 10+ miles a day on concrete and have held up well. That being said, I'm a pipefitter in high tech so they're not getting too dirty or beat up bad in the clean rooms so my review on durability might be different than someone working in the elements. I was always a Georgia guy as an operator/truck driver but those couldn't hang once I moved to this world.
[ffn2y97] (score 1, diepte 0) I hear lots of good things about RedWings but I know they get pricey, I personally have Carolina's which sometimes give me blisters on the side of my foot but thats all, there decent but after 4 months the sole is falling off since they are glued on not sewn or anything like that
[ffn309d] (score 1, diepte 0) I get about 2 years out of a pair of redwings beating on them hard (fair disclosure I dont pave) the way I look at it they run me $2 a week. $2 a week is well worth it to be comfortable all shift, especially considering my shifts occasionally run 20+ hours.
[ffn43au] (score 1, diepte 0) My go to Boot is the Georgia slip on 8” . These  last 2 years every time, if I re-soled they’d still be on my feet. These boot require zero break in and very little maintenance. I do rub them down with Bee Wax before I wear them.  I’ve tried many other brands, Red Wing , Timberland, Wolverine , And the best part is that they only cost $130..
[ffna5fv] (score 1, diepte 0) Had Redwings for years and switched to Oboz hikers almost exclusively. I ended up going back to a work style boot for outside work and after way too much shopping around and trying things on I ended on the Timberland Pro ripsaw. By far the most comfortable work boot I've ever had and I will never get another insole besides the tim pro's. I put them in another pair of carolinas that were complete trash to walk in and it made a world of difference besides them being too tight now(had I known this I would've gotten half a size bigger...or really not gone with the carolinas at all).
[ffnh0tk] (score 1, diepte 0) it's a shame UGG doesn't make steel toe boots
[ffniepk] (score 1, diepte 0) Check out some danner brand. They make military boots and are very comfortable, wear good and have a replacement policy. Best money you’ll spend for your feet
[ffnkqvs] (score 1, diepte 0) Might want to post your weight (if your not shy) I'm 250 and I know I shred boots people that are 180 say last a long time.

I personally avoid steeltoes unless I am in a situation that really needs them. I have tried a lot of the boots listed (redwings chippawas, etc) and my fav are swat style boots Magnum response II's but if I am wearing steel toes I enjoyed a pair of DR Marten ironbridges that I found on sale.
[ffp7mah] (score 1, diepte 1 OP) >weight

Never thought about that. I'm \~180. My company requires steel or composite toe.
[ffp8bwd] (score 1, diepte 2) Yeah the extra weight and what ever tools your trade requires really does a number on footwear.

I do mostly residential construction and for me the trade-off of safety for lighter boots was a no brainier that's why I wear the light swat style boots. 
But if I am in the shop, doing heavy equipment or lot clearing I will wear some of my chunky steel toes.
[ffpfxtf] (score 1, diepte 0) My previous two pairs were red wings and very comfortable, but heavy (steel toe) and took a while to break in.  This go around I went to a Red Wing store to get another pair and the sales guy convinced me to try on a pair of Irish Setter Crosby's.  Had them for about 8 months now and they have gotta be the most comfortable boot I've ever owned and they're much lighter (aluminum toe).
[ffpgtsk] (score 1, diepte 0) Nobody has mentioned [these Keens](https://www.amazon.ca/KEEN-Utility-Hamilton-Waterproof-Carbon/dp/B07FMDRVLX/ref=asc_df_B07FMDRVLX/?tag=googlemobshop-20&linkCode=df0&hvadid=356329057575&hvpos=1o3&hvnetw=g&hvrand=5646387143383404845&hvpone=&hvptwo=&hvqmt=&hvdev=m&hvdvcmdl=&hvlocint=&hvlocphy=9000433&hvtargid=pla-799256913793&psc=1) I have very wide feet and have always had problems with toe crunch and heel rubbing. These boots are the best thing I've ever worn at work. They are warm on cold concrete with insulated souls, and not too hot in the summer. Supportive yet soft. I smiled every time I put them on for a few weeks. I will be buying them again and again I think. I've worn this one pair for about 18 months most days doing everything from demo to cement work to framing and they're well scratched up, but still in excellent shape otherwise.
(4 reacties met lagere score weggelaten)

=== THREAD 673pqf ===
SUBREDDIT: r/army
DATUM: 2017-04-23  SCORE: 25  REACTIES: 70
TITEL: Why do my feet hurt so fucking much
POST (source_id=post):
I'm a soldier in my 12th week of training. My feet are killing me after our last 15 km / 15kg+rifle. I had people in my platoon sprinting the last 100 meters while I'm sure my feet were going to break if I tried that. Is it my socks? I have ABL issued socks just like everyone else. I need to be able to do 32km but at this rate I`m more likely to injure myself. How do I train this?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dgne972] (score 141, diepte 0) Have you tried not being a bitch?
[dgneuoq] (score 69, diepte 0) You'll build your slave feet overtime, keep pushing forward.
[dgnef09] (score 64, diepte 1 OP) i cri
[dgnvf13] (score 37, diepte 4) There are other armies?
[dgni6yw] (score 26, diepte 3) He's not in the US Army.
[dgnj9wc] (score 24, diepte 1) Is there a class for this skill?
[dgnk44t] (score 21, diepte 3) Less qq more pewpew
[dgnej4x] (score 17, diepte 0) OP, what exactly is hurting your feet?  Blisters on your soles, or is it like the tendons in the soles of your feet or something, or what?

Look, definitely do not be a sick call Ranger about it, but if it's a persistent problem, go to sick call and ask the PA about it.  Be sure and ask them specifically, is this something normal and you just need to sack up, or is it indicative of a problem?

Nine miles is not that long to just *walk*, by any stretch; people *run* further than that.  Go see if your shit is all fucked up, and if it isn't, you need to grab your sack and man up about it.

But definitely go get the word of a PA about it.
[dgnf19t] (score 17, diepte 1 OP) Thanks for the motivation. I'm just afraid the the jump from 15 to 32 is too much. Or maybe my mind will push me through like it always does
[dgnfnvo] (score 16, diepte 2) qq
[dgneo49] (score 16, diepte 1) If you're getting blisters like that your socks are probably bunching, or your boots are too tight or too loose.
[dgo0at9] (score 15, diepte 2) ranger
[dgnewtq] (score 14, diepte 3) lol

No, just not taking care of your feet.
[dgnkpde] (score 14, diepte 2) That sounds like it could be a potential muscular issue. If it's pain like cramping pain, try increasing potassium into your diet. I like bananas. 

Your tendon issues could be tendinitis. Does it feel painfully right and like it won't expand/stretch in the full motion? If that's the case you need stretching + recovery time. 

There are also legit foot issues that you could have. My twin brother had a problem where the bone on the top of his foot kept growing and they had to break and cut it because he was getting to the point where shoes were painful. 

Also, you need to read Fixing Your Feet. 

https://www.amazon.com/Fixing-Your-Feet-Prevention-Treatments/dp/0899978304

It'll teach you how to prep and care for them. His stuff works.
[dgnfs3y] (score 12, diepte 4) And he's a bitch.
[dgneuel] (score 11, diepte 2) I have the same thing from time to time, I've taken to stretching my feet and ankle out extensively starting a few days prior to movement.
[dgnr00r] (score 10, diepte 1) ELIabitch
[dgnfni4] (score 9, diepte 4) If your feet hurt at the top then you need wider boots.
[dgneqr9] (score 8, diepte 1 OP) No blisters whatsoever. Pure pain at the top of my feet and not precisely the achilles tendon but a part below it. I thought this would be over by now but I realized that this pain never stops no matter what I do. Our weekends aren't enough to fully heal my feet either. Thanks for the feedback. I'll check in with my unit doc when I arrive there.
[dgnetll] (score 8, diepte 0) Some people have bitch feet. 

Did you never walk outside without shoes? What about over gravel? Ever wear soccer/football cleats for hours a day? Never even worn work boots before? 

You probably have bitch feet with little to no callous on them. Rough em up!
[dgnezoq] (score 7, diepte 1 OP) Thanks fam. Reassuring
[dgnf284] (score 6, diepte 3 OP) This could be key. Thanks dude
[dgnhh03] (score 6, diepte 2) As a medic, there are two different schools of thought here. Ideally, you keep your feet soft. Unfortunately that's not always realistic, which is why I encouraged my guys to get them tougher.
[dgo5kic] (score 6, diepte 5) Yeah I'm in the U.S. Army. Haven't heard of the previously mentioned one.
[dgnf93j] (score 6, diepte 0) It could be stress fractures. How much swelling do you have? More than normal?
[dgnl28o] (score 6, diepte 0) When my feet hurt it was because my boots were tied too tight.
[dgo29cj] (score 6, diepte 0) Aight so this girl I went through AIT with was like a big runner in college and studied exercise science. She said the best way to stretch your feet is to freeze a water bottle. Like the plastic ones and put that shit on the ground and use it to roll the arch and heel of your foot out. It like brings down swelling and stretches it out. 
Also when you're just chilling and not walking does the top of your foot still hurt. Like does it hurt to move your toes up. To basically move any of the little bones in your feet? Like to wiggle your toes doe it hurt or to curl your foot like even without shoes. Does it hurt to run on and walk on without running? If you take your hand and push on the top of your foot does it fucking hurt. Or is the pain because your foot is super tight and doesn't feel like it's able to stretch out? Does it hurt when you put pressure on your heel when you walk. 
Lastly I would get something hard like a shaving Cream bottle and roll out your calf and ankle. It might help the Achilles pain. If you're in training which I don't remember cause my memory is fucked. Get a bag of ice and out it on said hard object to roll out foot.
[dgnes8a] (score 5, diepte 1 OP) What boots do you have? I don't have blisters though.
[dgnew69] (score 5, diepte 2) Don't wait until you get to your unit if it feels like you aren't going to graduate because of it, though.
[dgnf5k5] (score 5, diepte 4) Ok, then yeah, I'd wait until you graduate AIT and get to your unit.  Last thing you want is a doc to find an issue and you get stuck as a holdover in TRADOC.
[dgo058b] (score 5, diepte 3) Wow, actual advice instead of calling OP a bitch.  I'll be damned.
[dgnf2gb] (score 5, diepte 1) Calluses aren't really good.  I have pretty callused feet and thought that was a good thing until our medic pointed out that calluses can split and take you off your feet for a while.  Get a pumice stone and use it on any calluses.
[dgnji4i] (score 5, diepte 2) I guess I could see this both ways. 

Though I think the chances of soft feet breaking down, are far greater than calluses splitting. To each their own I guess.
[dgntp2n] (score 5, diepte 4) They "require" it?  lol.  i dont know about that.
[dgng0z2] (score 5, diepte 1 OP) I haven't really paid attention to swelling really. I'll keep an eye on it this week.
[dgnn007] (score 4, diepte 2) Pain at the top of your feet: the laces are too tight. You need to skip an eyelet.  If you can't do that for whatever reason, another way you can do it is to loosely lace the foot portion and then tie a knot on both sides so it stays looser on your feet but tight on your ankles.
[dgngvxf] (score 4, diepte 2) You would know, i.e. your foot ballooned so much it took a few minutes to peel it out of your boot.
[dgpe48s] (score 3, diepte 1) The last road march of Infantry OSUT was fucking murderous for me. I almost shit myself and my feet were destroyed. But over the next year I actually became a real Infantryman and stopped being a bitch. It's harsh, but sound advice.
[dgneddh] (score 3, diepte 0) Like the other user suggested; don't be a little bitch.
[dgnehm7] (score 3, diepte 0) Bitch
[dgnezkx] (score 3, diepte 3) I mean, we only have your feet to go on. Can't be sure.
[dgneyax] (score 3, diepte 3) Yeah, good point.  Stretching can be important for some people.
[dgnezan] (score 3, diepte 3 OP) That was the last one for our training here thanks for the concern. We only have exams for the final 2 weeks. Five seven joint and a couple more drills.
[dgnfznl] (score 3, diepte 3 OP) My unit
[dgo6by3] (score 3, diepte 2) Get inserts maybe?
[dgng489] (score 3, diepte 0) Go shopping for new boots and get a knowledgeable professional to help determine if they actually fit properly.
[dgng6z2] (score 3, diepte 0) Try a massage ball to unknot the muscles in the bottom of your feet. That's what helped me as we worked up to 25 mile rucks (only about 40lbs)
[dgnqehh] (score 3, diepte 0) [sry for ur pain](https://media.giphy.com/media/10hfegXGKVRVNm/giphy.gif)
[dgnyqd6] (score 3, diepte 0) If you can, buy gel insoles to put in your boots. They help so much with the pain. They wear out just like the soles in your boots so you should be replacing them every month.
[dgojxu1] (score 2, diepte 5) Here for you. In all seriousness though make sure you're changing your socks pretty regularly and make sure your boots are properly fitted and if they aren't consider getting something better than just the GI boots. Get some moleskin for hotspots as well.
[dgoi78f] (score 2, diepte 4) What a twist...
[dgo7qby] (score 2, diepte 1) I second this. You can use quite a few things to roll/massage the bottom of your feet. I suggest:

1- Frozen bottle of water. 
2- Tennis ball 
3- Golf ball - - - Hurts soo good! ( ͡° ͜ʖ ͡°) 

Consider rolling your calf muscles with a ["The stick" ](https://www.amazon.com/Stick-Self-Roller-Massager-Travel-Stick/dp/B0028BSFIS) and your thighs with a [foam roller](https://www.amazon.com/gp/aw/d/B00XM2MXK8/ref=mp_s_a_1_3?ie=UTF8&qid=1493010596&sr=8-3&pi=AC_SX236_SY340_FMwebp_QL65&keywords=foam%2Broller&dpPl=1&dpID=41YRzs0ZsCL&ref=plSrch&th=1&psc=1). 

Between rolling and stretching you should feel better. Otherwise, I would get that checked out. 

Also, take some Motrin and hydrate!
[dgnockw] (score 2, diepte 0) MOS? 

What boots are you wearing? Are you allowed to purchase other ones?
[dgntzqm] (score 2, diepte 0) Stretch them calves.
[dgojxvp] (score 2, diepte 1) Are you a 68W?
[dgo2w12] (score 2, diepte 0) Buy non issue boots,  and insoles. Stretch.  Like the water bottle method that was just talked about.
[dgoqgfy] (score 2, diepte 0) Eat more green veggies. Bell peppers, peas, and broccoli specifically. Milk won't fucking do it for you, that shit leeches as much calcium as it puts in. But dark green veggies have a lot of calcium and vitamins to help with bone strength and they even help with plantar fasciitis. 

If you really want to pamper your feet, get some super fucking thick smartwool or darn tough socks. Your feet might get hot but the wool can take it. Trust in the wool. These shits are $25/pair for a reason. They should be thick enough that your boots feel snug. Cotton's too thin for rucking imo, you end up having to overtighten the boots and that restricts your ankle movement.
[dgohzto] (score 1, diepte 3) No, you're still a little bitch, just a little bitch with big blisters. Take a knee, drink water, change your socks, rub some dirt on it, mainline some Ibuprofen and drive on.
[dgorsay] (score 1, diepte 4) Experiment with lacing your boots differently. Check out /r/goodyearwelt thread https://www.reddit.com/r/goodyearwelt/comments/2gm4ka/how_do_you_lace_your_boots_specifically_iron/ here for some different techniques.  

Also, google heel lock, ladder lacing, over/under....there's a bunch of different techniques.  It may feel like a pain in the ass lacing and un-lacing your boots five different ways for an hour, but it is key when you have a pair of boots that hurt your feet.
[dgoaeni] (score 1, diepte 2) You definitely have plantar fascitis.
[dgodzka] (score 1, diepte 2) Is it worse in the morning when you wake up? I have had a few different feet issues. One being plantar facitis. You can freeze a few golf balls and roll them under your feet. Also get a towel or something with not a lot of give and flex your feet. Tie a knot at the end and stick it under a door frame and flex the other way too. Or ask your roommate to hold it. The other thing it could be is pressure on your low back. Google cobra position for yoga, now modify it. You want to be in the same alignment as that position- but only use your forearms, everything else on you should be slack; your waist, hips, legs, feet all should be tension free. Hold for 10 secs Repeat. 

Not a Dr. But have had feet issues for days and this is what helps.
[dgp5v2p] (score 1, diepte 2) Sounds like you might be tightening the fuck out of your boots. Try wearing sock liners too
[dgnf93y] (score 1, diepte 3) Binary marches.
[dgp1pns] (score 1, diepte 2) Lacrosse balls are legit too.
[dgo9tjv] (score 1, diepte 0) Get a lacrosse ball and roll out your feet. Google Kelly Starrett.
[dgoaadl] (score 1, diepte 0) How old are your boots? Are you flat footed?

If old, replace and break in, if flat footed buy some dank inserts. If you aren't flat footed, buy dank inserts anyway. 

You may have plantar fascitis (your feet have deep tissue ouchies) especially if it's hurts when you walk barefooted, in which case you need to massage your feet when you wake up, after PT, during lunch, after work, and before you go to bed. Again, dank inserts and possibly compression socks, although I don't know the efficacy of those, never gave or used. It's gonna hurt when you massage them, deal with it.
[dgoeuba] (score 1, diepte 0) "It's because you've never used them before, Neo"
[dgoifbg] (score 1, diepte 0) What i want to know is who has ever rucked and not had their feet and shins kill? Zero?
[dgok1fu] (score 1, diepte 0) Yeah
[dgo59o5] (score -1, diepte 0) Drink a tall glass of man the fuck up. That usually works.

