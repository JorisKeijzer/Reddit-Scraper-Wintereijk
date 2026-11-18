# Label-batch batch_0078

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
Schrijf het resultaat naar `batch_0078.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1cxz5y2, 1hf21q0, ygk1h0).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1cxz5y2 ===
SUBREDDIT: r/Construction
DATUM: 2024-05-22  SCORE: 38  REACTIES: 89
TITEL: What’s everyone wearing/doing to keep their feet from liquifying this summer?
POST (source_id=post):
Any suggestions on what kind of socks to wear or products for your feet to help cut back on the sweat and smell? Boots are on my feet for a minimum of 13 hours a day and I don’t want to be putting on damp boots for the next 4-5 months

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l55xudj] (score 82, diepte 0) Darn Tough socks are like $20. Its truly obscene.  I also gave up on wearing anything else with boots. I spent $200 one day and have been done with it. If you don't lose them they have a lifetime warranty.
[l55ytb6] (score 66, diepte 1) Two pairs of boots.  It sounds stupid, but they get to dry out and kill bacteria.
[l55zcji] (score 49, diepte 0) Wool socks in the summer sounds crazy, but they’re great. Just get the kind meant for summer, obviously
[l564veb] (score 31, diepte 2) Yes! This and a boot dryer :)
[l55y8ty] (score 17, diepte 0) Boot drier’s the way to go. Light weight hiking socks help.
[l56kk38] (score 15, diepte 1) Wool socks 100%.
[l563nkk] (score 15, diepte 0) Two pair of boots. They sometimes need a day to dry out.  I’ll wear regular shoes when I can. Safety shoes if it’s needed are cheaper than another good pair of boots.  Red wing sells lifetime socks. If they wear out, you just exchange them. They are thin enough you can wear them in summer. 

I almost always wear wool socks. The army taught me the difference between wool/cotton in any weather. Just don’t wear winter socks in 100 degree weather. Two pair of socks on really bad days. Switch them at lunch. Your feet will thank you.
[l5605c3] (score 11, diepte 1) I second Darn Tough. You won’t regret it.
[l572b2w] (score 9, diepte 3) I second the boot dryer! Essential!
[l566d0o] (score 9, diepte 1 OP) Just ordered a few pairs to give them a try. Thanks for the info!
[l56gwdk] (score 8, diepte 2) You won’t regret it, honestly one of the best purchases iv ever made. If needed you can use them for 2-3 days in a row, they wont be as comfortable and they will have a slight smell but it’s nothing compared to any standard sock.
[l560x5t] (score 8, diepte 0) Thin merino wool socks, boot dryer and rotate two pairs of boots.
[l564kga] (score 8, diepte 2) All things considered, I'd rather have feet.
[l5840k7] (score 7, diepte 2) Wool breathes will keep your feet dryer
[l560xqa] (score 6, diepte 0) Hmmm, liquifying feet, you say? Well, first of all, I'll be avoiding the puddles of nitric acid.
[l562x4n] (score 6, diepte 1) Your loss. How else are you supposed to get worksman's comp?
[l561dfu] (score 6, diepte 0) Flip flops. Just be extra careful with heavy stuff and stepping off onto a roof from a ladder. Never been cooler.
[l5682pj] (score 6, diepte 0) Anyone's who's had athletes foot knows the importance of keeping your feet dry. It's much easier to just have two pairs of boots, preferably swap at lunch or rotate daily. A can of gold bond and boot dryer for at home. Socks I like are the Nike dry fit or darn tough, don't cheap out on your feet ppl
[l5811h9] (score 5, diepte 3) Yeah, I wear warehouse shoes. They're Keens with a big composite safety toe and lots of ventilation. Low tops. Very light. I use them for most indoor work. Also easier to flex the ankles for doing work down low.
[l566erq] (score 5, diepte 1) Wool socks and liner socks year round for me.
[l57htqx] (score 5, diepte 1) 🤯alright I'll trust ya boys and try it. Mind blown. Never would have thunk.
[l55zwbc] (score 5, diepte 0) Wool socks or mesh socks
[l5683p9] (score 5, diepte 0) Never wear the same boots, or shoes, two days in a row.
This can't be understated.
They need time to dry out. And they will last much longer. Your initial investment will be higher, but in the long run, you will save money, and save your feet.
[l57rb9l] (score 4, diepte 2) Or even better, safety toe hikers.

First, they breathe better, second they’re like 1lb lighter per foot.

One lb on feet is like 5lb on your back in regards to the amount of energy it takes to move.  It adds up over a day.

When I have to wear boots I get home and every single bit of me feels exponentially worse.  Plus everything lower back-down to feet feel like I took a hammer to them.

People laugh at the thought of not wearing boots, but plenty of safe certified shoes that don’t weigh 2lb each foot.
[l58tdru] (score 4, diepte 2) If you ordered them on Amazon, be careful. Sometime last year they found a bunch of fake darn tough socks being sold on Amazon.
[l56cz8p] (score 4, diepte 1) This right here. Wool is naturally antimicrobial and handles moisture better than cotton or even synthetic material.
[l577j53] (score 4, diepte 0) 2 things I learned in the military:

80% of all injuries were reduced by introducing proper medical insoles. 

Change socks every 6 hours when doing heavy labor or hiking. 

I keep an extra pair of dry boots in the van and always have multiple pairs of socks. I also have my Chaco sandles for lunch and supply runs. Seriously, foot rot is terrible and is exceptionally painful to recover from. Take care of your feet!
[l57gz5m] (score 3, diepte 4) Came here to say this
[l590ojd] (score 3, diepte 2) Two pairs of boots lost way more than twice as long as one pair of boots
[l56sia4] (score 3, diepte 2) With a high merino wool content, best socks ever
[l58mpeg] (score 3, diepte 1) Yeah, people think it's crazy when they hear me say I wear wool socks in Las Vegas in the summer but when I take them off at the end of the day my feet are dry.
[l5ah9wi] (score 2, diepte 4) I also wear keens on larger jobsites where it stairs all day long every day, but $$$, and I don't want to fuck them up in the mud.

Makes a huge difference saving I have no idea how much weight.  But my fit but tells me 15 to 20,000 steps a day, and 56 stories of stairs.

Do that in heavy leather reinforced Dakota or whatever big name, and my 40yr old body does not like it one bit lol.
[l595cac] (score 2, diepte 3 OP) I did…hope I don’t get scammed lol
[l58zfx3] (score 2, diepte 1) The amount of love I have darn tough socks is nuts.  Prior to them I had drymax socks, high quality all cotton socks, and basically everything under $20(it was a barrier in my brain).  Holy piss knuckle they really are worth the $27 (local price)
[l56dj78] (score 2, diepte 0) Bombas socks. It’s like telling your feet you love them. $50 for 4 pair and they donate socks too.
[l57rnd5] (score 2, diepte 1) Love my bombas.  Super comfy
[l56ervt] (score 2, diepte 0) Thin Merino wool socks, icebreaker or smart wool are my go to.  Also two pairs of boots to keep the stank down.
[l56wxyy] (score 2, diepte 1) Every single construction worker should shell out the $40 for a boot dryer. I can’t understand why they aren’t ubiquitous
[l56gbo1] (score 2, diepte 0) I wear wool blend hiking socks. Wool takes a while to feel wet, and it cuts back on the smell. The hiking socks are alot thinner than the wool you're used to.
[l56kcne] (score 2, diepte 0) Wool socks, two pairs of boots, boot dryer.
[l56rq2x] (score 2, diepte 0) If it's that bad, swap into a second, dry pair of socks and boots at lunch. Fresh footwear is a beautiful thing, on a hot day. But yeah, get some lightweight Darn Toughs, and a boot dryer. The socks will help your feet stay cool, and the boot dryer will stop stench from building up in your boots.
[l56slre] (score 2, diepte 0) Always wool socks. Winter, summer. They are always the right choice. 

Also, buy a boot dryer so that your boot isn’t damp when you put your foot in there in the morning.
[l570493] (score 2, diepte 0) Wool socks. Tried it a decade ago and never looked back. Just make sure to take your insoles out each night and dust them with baking soda.oh and store your boots sole up too.
[l584o59] (score 2, diepte 0) danners and expensive hiking socks.
[l58j9ef] (score 2, diepte 0) When I’ve had to pull 13+ hour shifts, 7 days a week, I went with the tip a coworker gave me. Dryer sheets in the boots. No funk, no dampness the next morning. Also, another vote for Darn Tough wool socks. So soft and comfy.
[l5a0hpc] (score 2, diepte 0) Depends what you do but I have “summer boots” and winter. Summers are a canvas, steel toed Keen. They are a couple years old, olive green and you can fold the tops down. They are lightweight and breathable. Fucking incredible for summer. Not waterproof🤷‍♀️
[l59b9s9] (score 1, diepte 3) These boots were made for dryin'
[l59u8le] (score 1, diepte 2) Ha yeah I had to get metatarsal guards for one plant I was at a couple years ago so I’ve got 2 pairs and I switch every other day
[l595uj5] (score 1, diepte 4) Not sure if it’s a prevalent thing or not, just recall reading that somewhere lol
[l591zfw] (score 1, diepte 2) I too have very stinky feet. Almost eliminated by darn tough. And I’m more comfortable!
[l56vnh4] (score 1, diepte 1) I got a pair for free with my boots(midwestboots.com) and I was totally expecting to be disappointed.   

I wasn't.  I've now got a full weeks worth.
[l57bdvt] (score 1, diepte 1) [ Removed by Reddit ]
[l597jm3] (score 1, diepte 1) Yeah I bought 4 pairs. I'm going to pick up Some ankle socks too. Awesome socks.
[l566lmd] (score 1, diepte 1) Oh yeah its not bad to bust out the winter boot drier out in the summer!
[l563jda] (score 1, diepte 0) Workinstocks
[l56538p] (score 1, diepte 0) I work with water so I’m just used to it at this point.  I am currently rocking some fancy on cloud waterproof shoes my bro gave me cause they didn’t fit him right.   They are eh, but I prefer sneakers so usually anything “waterproof” and just new shoes every 4-6 months
[l566g1b] (score 1, diepte 0) Two pairs of boots is good, odor eaters powder is good. The best is wearing wool socks, well wool blend, 100% wool would be too much in the summer for most guys, costco did have some "weatherproof" wool blended socks that are thin enough. Wool can be completely soaked through and still feel dry and is also antibacterial.
[l56e1aw] (score 1, diepte 0) In central florida heat i was wearing Thorogoods and cabela’s wool socks doing great
[l56fmor] (score 1, diepte 0) Wool socks, boot dryer.
[l56g0ql] (score 1, diepte 0) Crocs 😎
[l56j3nw] (score 1, diepte 0) Get sock liners. I kid you not. They’re basically just very thin socks you put on before your regular pair. They make a world of difference especially if you have on muck boots or the like.
[l576ob2] (score 1, diepte 1 OP) Tell me you work in an air conditioned office without telling me you work in an air conditioned office….
[l56ssxk] (score 1, diepte 0) My boots go on the boot dryer every day after taking them off. Much less smelly and no athletes foot.
[l56vfz3] (score 1, diepte 0) Crocs
[l56wj7j] (score 1, diepte 0) I bought unlined leather boots for this exact reason and they’ve been wonderful. (Danner bull runs. Love love love these boots.) Also +1 for darn tough socks. And I put a sprinkle of foot powder in my sock before I put it on in the morning. And if you have an air compressor you should be blasting an air nozzle into your boot many times a day as a refresher
[l572fqk] (score 1, diepte 0) I wear running shoes. My employer allows them
[l5785sq] (score 1, diepte 0) Put a boot dryer where you take your boots off after getting home. They’ll be dry by morning.
[l57dkk0] (score 1, diepte 0) Smart Wool
[l57l849] (score 1, diepte 0) Carbon toe instead of steel toe
[l57mx8x] (score 1, diepte 0) I put my boots in the garage and bought a $20 boot dryer that I use every night. I'll have one until I retire.
[l57n5rq] (score 1, diepte 0) I don't wear fancy socks, but last summer, I did bring extra socks to work. First change of socks at mid-morning break, second change at lunch. Maybe a third change after I get home if I'm going to walk the dog or do work at home.
[l57qui0] (score 1, diepte 0) I'm also doing 12+ hour a day in work boots. As soon as I come in the door, I'm on the couch to shuck those suckas _off_, peeling the socks off my _pies_, and slipping into my flojos.  Best flip-flops ever, so glad I found them at Costco!
[l57s3t5] (score 1, diepte 0) Light weight wool socks.
[l58isw6] (score 1, diepte 0) I don’t care what you wear in the summer, your feet are going to sweat. I like wearing smart wool socks, going to try the darn tough next. I have a boot dryer on a timer plug. It turns on right after I get home and turns off right before I leave.
[l58s3jd] (score 1, diepte 0) Flip flops unless I'm going to be welding. I have a pair of crocs for that.
[l58v97h] (score 1, diepte 0) As a trail builder for 10 years my advice would be good pairs of wool socks and a peet boot dryer. If need be put your socks on the dryer and you can put your boots over those. It’ll kill the bacteria and dry them out. By the time you wake up they’ll be perfect.[Boot Dryer $50](https://www.farmandfleet.com/products/391380-peet-original-shoe-boot-dryer.html?blaintm_source=google&blaintm_medium=pla&gad_source=1&gclid=CjwKCAjwr7ayBhAPEiwA6EIGxLr8IwJKGqmwqyOEP7ySBwSohY_ggByx6eyZVdrcL138grJA0S18RhoCdP4QAvD_BwE&gclsrc=aw.ds)
[l58vyy2] (score 1, diepte 0) My boots go on the boot dryer as soon as I walk in the door. Always dry in the morning. 

I also will sometimes bring tennis shoes with me so I can take my boots off before the drive home. Probably excessive but it feels so good to take them off.
[l58y3wa] (score 1, diepte 0) This is the answer, I cannot recommend these enough:  Bama socks.  I get sweaty feet even just sitting in the cab, these things solved the athlete's foot I would get during consecutive 14-16 hour days during harvest (I moonlight as a grain farmer when I'm skipping out of my duties as a PM in construction)  I know them as Bama socks, seems it's more common in Canada but I did find an Amazon US link, not sure what other similar products there are.

[Canada link](https://www.marks.com/en/pdp/men-s-bama-boot-liner-socks-79611949f.html#srp?&colorCode=COLOUR_GREY) 

[Amazon US link](https://www.amazon.com/zNatoo-Sokkets-Thermal-Insulated-Socks/dp/B0BWBC7ZKQ/ref=sr_1_6?dib=eyJ2IjoiMSJ9.wQphWiNDal_22cF_6HomEc_LAExLGn5N3rXNN7tQZLpMfnaLXKqKMzYHslh5dYlp9oHW_W-dnYJV1XTqfuR6aUlrkaX582Q8h9xxfrv5-rnE9HRwOrglo2WC1ARIOCkzWgYLuXpzmkyZtchlQILJBaza2RHi0F8iwq-P_wL830RXJx_pk0HxIO6AbFOmvqc13nIuyZ9FM-NP0M-Cf9Ix3iyuz_M767_9VMs4U2isTaXnffVE99GXjIwakw_yKcPVKmS4V5d-WvtfjLIMdKQRNj-gzU9vscsPpe0uDgWAMSQ.3w60cuJtub6Y5h3Zns6txKf7r4bRwlgW6Azt6bpeLcE&dib_tag=se&keywords=bama+socks&qid=1716420124&sr=8-6)

[alternate Amazon US link](https://www.amazon.com/Bama-Sokkets-Thermal-Insulated-45/dp/B004GT9YDU/ref=sr_1_3?dib=eyJ2IjoiMSJ9._EeCsPn1DaeWBcIbNvWMftlXxPOMVBnFI_lJpGGOLiqbro-6zx-kRrXNOvi80jnvejKbgtfRpBUG63Qptz1tXJuRVDPVAy2UoX1TZwR_2-6wipMPNt0hdkByOUVDQcQQYc-095xZRPOydN6sCBznPgQBg5KlCNIqYihNZ5QSw5ll6hT1M_KXuqVbH1SUVMK4GhlwOWroisDhOASJGRvUTZlUIuH8Rchpx5euC1GHS80.MOXEpLUeKi4IDRd_8bXsqdDuSaDQ5r9WR8vr7TwHRt8&dib_tag=se&keywords=Bama&qid=1716421124&sr=8-3)

Wear your regular socks, slip these over, then into your boot.  They attract moisture better than cotton or wool, so at the end of the day I pull my feet out, these things will be soaking, and my regular socks are just mildly damp. I used to think wool was the answer, and it helps, but this is better.  I can wear these with plain cotton socks and it's better than just a wool sock.

I know it says they are an "insulating" sock (which they are, they help in winter) but they also, counterintuitively, help big time with sweaty feet in summer because of how absorbent they are.

Two downsides:  1: They are thick, so you might need to size up your boots.  2: They don't stand up very well if you're doing heavy labour in them.  The seams fall apart, especially behind the ankle, for me.  I'm a cheap farmer and just keep wearing them like that because they are still very absorbent.  So I buy several pairs at a time.  Leave them on the floor at night and they are dry in the morning (but good to swap daily).  

I recently switched to slip on boots instead of tie on, so they fit a little looser around the ankle and I think that allows some moisture to escape during the day.
[l596m64] (score 1, diepte 0) Carhart yktv
[l597a0g] (score 1, diepte 0) Boot dryer and darn tough socks.
(11 reacties met lagere score weggelaten)

=== THREAD 1hf21q0 ===
SUBREDDIT: r/Chefit
DATUM: 2024-12-15  SCORE: 4  REACTIES: 88
TITEL: Chefs, what shoes are you wearing?
POST (source_id=post):
My feet and legs are killing me doing all the hours of the day. Some have recommended the on cloud trainers but head chef says they’re crap. Any recommendations on some shoes to get please and thanks

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[m285e5t] (score 16, diepte 0) Blundstone Chelsea boots.
[m28ala7] (score 15, diepte 0) Birkenstock Boston super grip get a new pair every year or so best shoes I've found
[m284ib6] (score 10, diepte 0) Currently have a pair of Hoka non slips that have been great going on a little over a year now.
[m286v8o] (score 10, diepte 0) Hoka Bondi forever. I will never wear another shoe. I'm old (for kitchen work) and wish I found these shoes a long time ago. I run circles around the younger folk now.
[m284ndd] (score 6, diepte 0) Crocs for instant comfort, or birkies if you want to suffer greatly for a few weeks. I think crocs are more comfortable but the birks look much more professional.
[m287f4r] (score 6, diepte 0) I’ve had the same pair of Dansko shoes for years. I’ve probably walked thousands of miles in them.
[m287u08] (score 5, diepte 0) Everyone has given recs on shoes, yoga can help with foot, leg, and eventual back pain. Posture is everything.
[m286590] (score 4, diepte 0) Merrell pro mocs, ugly but comfortable af and pretty durable
[m288r08] (score 4, diepte 0) I've worn a lot of kitchen shoes. I started out with rubber clogs, went to Danskos for station work, Crocs for general kitchen wear, then moved to SFC sneaker style when I was in a casino and walked a few miles a day. I found Hokas about two years ago and live them. They're hugely more comfortable than any of the others and my feet feel good after 10 hours in the kitchen. 

The only thing I really miss about clogs, is the ability to take one foot out at a time, to stretch and cool it down.
[m28aepk] (score 4, diepte 0) I currently wear blundstones. I've had birkies before, they aren't to bad. Ive had plenty of leather birkentocks and mafesto clogs over the years. But I just chew through them so fast. I had a wicked pair of Birkenstock boots/high top lace ups. Absolutely loved them! But again I just distroyed so fast. The cork just doesn't hold up me.
[m2a6vmh] (score 3, diepte 1) Seconding the Blundstone. Just picked them up after wearing the croc clogs which I hated (and honestly weren’t very slip resistant). I put on the Blundstones and felt like I had new feet. So damn comfortable
[m2886pd] (score 3, diepte 1) 100%
[m28rxl6] (score 3, diepte 2) Lucky for you, Hoka makes a non slip version. Only downside is it's all black. I like the colors. I also run a food truck with nothing greasy, and a lot of miles on pavement. Non slips would be toast in a month for me. But if I ever transition back to a typical restaurant environment, I would happily wear the non slip Bondis.
[m2az2fx] (score 3, diepte 1) Every year? Wtf
[m2bu1iz] (score 3, diepte 2) I chef at a zoo they get worn out pretty quick
[m28j3cs] (score 3, diepte 0) My wife’s a nurse and got me on compression socks a couple years ago. Feel like I’m 20 again.
[m28tvow] (score 3, diepte 1) Big shout out to compression socks! They're not just for mental wards.
[m2kpn8s] (score 2, diepte 1) I’ve tried clogs and boots and I’ve always preferred boots. So far blundstones have been the best
[m2861af] (score 2, diepte 0) I have the birkenstock pu clogs
[m28g32f] (score 2, diepte 1) Aint lying. They are fucking atrocious looking.
[m28kotj] (score 2, diepte 3) Ive been looking for some new shoes. Thanks for the rec.
[m28ri7r] (score 2, diepte 1) How do you not go A over T without non slip soles?
[m2gnmc9] (score 2, diepte 3) Bondi SRs come in multiple colors now, you just have to order them from their website. I wanted the green, but didn't feel like waiting on shipping when the pair I tried on in the store was so damn comfortable. I'll 100% be ordering a second pair in a couple months to have a second pair to swap out on a regular basis.
[m2g9vbj] (score 2, diepte 2) My Hokas are Bondis with kitchen soles. No problems with slipping at all, grip just like my SFCs and Danskos.
[m2k9jda] (score 2, diepte 3) I will check them out thank you. I’ve recently got Danskos and although very comfortable, constantly reaching forward into the prep bench fridge I feel like my knees are on the verge of being hyperextended. I’m early 50’s and the old legs are complaining!
[m2gn4kg] (score 2, diepte 1) Just bought a pair myself last month. Best kitchen shoes I've had since the ones I was issued in culinary school 25 years ago. 30 years in kitchens and my back pain and knee pain are starting to truly fade compared to where they were before.
[m287ghy] (score 2, diepte 0) I love my Crocs on the Clock. Coworkers all wear Shoes for Crews because that’s what the boss orders. I just bought my own. They are all dealing aching feet while I walk around on my clouds.
[m2azm76] (score 2, diepte 2) I have 2 pairs and get them re-soled every year. The leather and support never diminish
[m2b000c] (score 2, diepte 3) I got cork sole birkenstocks and they last me years. Same ones?
[m28cvo2] (score 2, diepte 0) Hokas
[m28dqa4] (score 2, diepte 0) “Martin’ Klogs perfect
[m2oqzor] (score 2, diepte 1) This is what I wear and I do 70+ hour weeks and have no problem. I’ve never experienced a break in period either.
[m29zahf] (score 2, diepte 0) Crocs!
[m2a7avi] (score 2, diepte 0) Croc bistro 2  with arch support insoles.
[m2awqdz] (score 2, diepte 0) Crocs forever man, my bistros are so comfy and I can just spray them down with a hose whenever I need to clean them
[m284aft] (score 1, diepte 0) I’ve heard snibbs shoes are great, but I have not tried them. I’ve been wondering the same question though so I’ll be following. 

As of right now the crocs kitchen shoes are the best I’ve found. No matter what I’ve worn I have to change them out every 6mo because I wear through them
[m28cspe] (score 1, diepte 1) Snibbs are great, keep an eye for deals, they have some super great deals like BOGO and super clearance. Best shoe I've used in a kitchen so far.
[m2a6pl6] (score 1, diepte 1) I used to wear Blundstones but have recently switched to Rossi's. I've been getting a better lifetime on the boot. 3 Years when I used to get new Blundstones every year. Blundstones are a good choice but look at Redbacks, Rossis or Red Wings as an upgrade.
[oy7wn1h] (score 1, diepte 2) I’ve been using redbacks for years, but they don’t last as long anymore unfortunately.
[m28jy7f] (score 1, diepte 2) It ain’t a catwalk. It’s like walking on pillows and they last a couple years
[m286r65] (score 1, diepte 0) U power Gaynor + thermal socks
[m2m6xer] (score 1, diepte 4) The danskos are comfortable for standing. They’re a bit weird for crouching down, and awful if you need to walk a lot!
[ncamprl] (score 1, diepte 1) Eh.. Maybe for servers.  If you move around a lot, they work great.

but if your kitchen splashes water every night, those non slip soles will come off. thankfully Hoka warrantied mine, but it happened again.  I just used my own glue to glue them back on, but I rarely use my Hokas now.
[m287qb6] (score 1, diepte 0) Cole Haans on shoes for crews have been the best shoes I've had in years.
[m287qit] (score 1, diepte 0) SAS
[m289h15] (score 1, diepte 0) Birks
[m289lut] (score 1, diepte 0) Emmas!! Best ones I have worn. And I have tried 10+ pairs
[m289wkj] (score 1, diepte 0) My Snibbs are great and super comfortable, probably the only downside is they are not too breathable so feet will get a bit sweaty after a long day.
[m28bibs] (score 1, diepte 1) Blundstone is the way.
[m28ak1o] (score 1, diepte 0) Skechers riverbound with some high arch insoles. With compression socks my shins and feet are about as good as they can be at work.
[m9tnw5p] (score 1, diepte 1) Looking into getting these myself. How's the arch support with the insoles that come with it before you switched insoles?
[m9xd2xi] (score 1, diepte 2) They were fine before I just wanted something with higher arches for me personally.
[m2b7sqm] (score 1, diepte 4) Yep. I only get one re-soled a year
[m2ffipl] (score 1, diepte 3) Bruh told me hes feeding rhinos everything makes sense now.
[m2f48pi] (score 1, diepte 1) One pair a year for me too. Too stinky by the time the soles are worn out to be taken anywhere near a cobbler
[m28bphu] (score 1, diepte 0) They’re not for everyone. But if you find the right pair of Burkies… They rule!
[m28d66w] (score 1, diepte 0) shoes for crews clogs with high arch support insoles
[m28ddwv] (score 1, diepte 0) I ordered some shoes off of orthofeet and they're the most comfortable long hours shoes I've worn.
[m28enfe] (score 1, diepte 0) docs
[m28gxih] (score 1, diepte 0) Lots of standing? Dasko classic pros. I like the extra height and can walk fast too. 
Not so much for lots of stairs.
[m28hr9p] (score 1, diepte 0) Klogs had them  for a while too, pretty comfy and all I do is buy new inserts when needed
[m28jbiy] (score 1, diepte 0) The On Cloud, etc., brand build quality is unfortunately hot garbage IME.
[m28kn6c] (score 1, diepte 0) Crocs non slips were really hurting my feet, went Sketchers because I’m an old man and now I’m feeling better.
[m28lga0] (score 1, diepte 0) Birky boston or tokyo(?) with the rear strap cut off, last me 3 years at a time, and im a size 15uk and 130+ kg
[m28tozh] (score 1, diepte 0) The real secret is that its not about the shoes, it's about the in-soles. Personally I wear steal capped non slip safedy boots with custom in-soles which some think is overkill, but traces back to an unfortunate incident from years back involving a commis, hot oil and a hospital visit. Fortunately it wasn't as severe as it could have been but yeh, ever since then it's been heat proof safety boots for me.
[m28wotz] (score 1, diepte 0) New balance fresh foam x kaiha road changed my life. I have chronic ankle problems and these shoes make my life significantly better in the kitchen.
[m28ykj4] (score 1, diepte 0) i got some non slip sketchers with a discount my restaurant had and they’ve worked great for me
[m2977rj] (score 1, diepte 0) Birkenstock Profis. Best shoe I've found yet. The first two weeks sick but once they form to your foot they're so fucking comfortable.
[m29depe] (score 1, diepte 0) Shoes for crews
[m29hh1v] (score 1, diepte 0) SIKA FOOTWEAR
[m29o890] (score 1, diepte 0) Me and most people I work at wear skechers. Is it the best price-quality-durabulity? No. But it is very comfortable and non slip
[m29q3j4] (score 1, diepte 0) Birkenstock Tokio super grip clog. They have been great so far, I’ve had them for just over a year. 45+ hour weeks and no pain, aside from the break in period lol.
[m29t1s8] (score 1, diepte 0) Do calf and Achilles heel stretches. Quick 30 seconds before and after bed.  Also compression socks. I have worn the og dansko clogs, Crocs, birkies.

The best have been a cheap Amazon pair of 0 drop sole wide toebox barefoot sneakers (not kitchen safe) and knee high compression socks with those stretches and no more feet pain.

I had to work this week the classic 4 -12 hour shifts with my Amazon barefoot shoes and compression socks no problems. Then I had to come help for 4 hours to prep a catering in normal footwear and my feet were throbbing.
[m29xv0e] (score 1, diepte 0) Good shoes with arch support Etc but mainly you got to get exercise! Squats lunges jogging Etc lots of stretching! You are a ninja in a confined space......
[m29yo2l] (score 1, diepte 0) Van's Sk-8 Hi. I'm 54 and been been wearing them since the early 90s. Started on compression socks a few years ago, no complaints!
[m2a1d6f] (score 1, diepte 0) Shoes for Crews all the way, buy 2 pairs, change mid shift. Replace every 6 months.  The sneaker type is only about $60 a pair. WAY better than birkenstocks.
[m2a2wp1] (score 1, diepte 0) I'm rocking some birks. They've lasted me the longest by far (1½ years at this point). 

Downside is I'm more in a managerial role now and I noticed my feet get kinda sweaty and stinky by the end of my shift (honestly kind of new, never really had that experience until starting this position).

Comforts pretty great after they're broken in. I barely feel like I'm wearing shoes tbh... which is weird for the material it is.


Also whatever you end up getting, if you have the extra cash to spare, get two pairs and swap pairs every week or so
[m2a75xq] (score 1, diepte 0) Mozo natural. Comfiest shoe I’ve ever had. I’ve tried many through out the years but these have been the best. They break in within a week and I’ve been wearing my pair for over a year and there is little to no wear on the bottom of shoe. Also crazy comfortable and have great support. Only thing I’ve ever done was change the insoles
[m2a84mg] (score 1, diepte 0) I've been wearing the same Red Wings for a couple of years now. They stopped making the slip-ons, but the laced work shoe is just as comfortable with the arch support insoles.
[m2ab2ba] (score 1, diepte 0) I had tons of problems with my feet and legs, have high arches, made custom insoles, not cheap, but fixed 95% of leg and feet pain for me.
(26 reacties met lagere score weggelaten)

=== THREAD ygk1h0 ===
SUBREDDIT: r/FASCAmazon
DATUM: 2022-10-29  SCORE: 65  REACTIES: 88
TITEL: Yeeeeeo….. these 10 hour shifts are no fucking joke…. How do y’all handle the foot pain cause I’m ready to cut my feet off.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iu9dm0x] (score 15, diepte 0) Your body does adjust, I promise. 

Insoles help as well as you’re getting used to being on your feet that long. It gets easier.
[iu9z4y7] (score 13, diepte 0) Welcome to Amazon, where you suffer for your pay. 
No back or shoulder pain yet? Hand, forearm, biceps calf cramps sore neck knee pain. It will all get easier and less pain as time goes on. 
Get some memory foam insoles. It was like night and day for me. I was able to fit a thick style insert but maybe just stack the cheaper thinner ones without it getting to tight. Stay hydrated and eat bananas to keep the cramps away. 
Can't wait for the 12hr MET for peak. Its way better then then the 10hr shift now. Lol.
[iu98doc] (score 11, diepte 0) Got used to it when I was in the Army
[iuc69rf] (score 10, diepte 0) Hit the bathroom once every hour helps keep my feet from getting sore 😁
[iuc6gad] (score 10, diepte 0) Cut your feet off
[iu9zzlo] (score 9, diepte 0) You will get used to it.
[iubrqjq] (score 8, diepte 0) Your body will get “work hardened.” You’ll be good just stick it out but ya good shoes help
[iubz7j8] (score 8, diepte 0) Your body becomes numb to it lol
[iuc211v] (score 8, diepte 0) Insoles, and GOOD work shoes. Nothing from Zappos.
[iuc8rvj] (score 7, diepte 0) Insoles!!! Zappos covers them as well if you have enough moneys left over. And tbh pain killers just to make it through those last 2 hrs sometimes. It’s tuff but you’ll get used to it!!
[iucbbmp] (score 7, diepte 0) This guy
[iu91mox] (score 6, diepte 0) I worked in Kitchen before my amazon job. I just kind of got used to it. But those MET shift would mess me up.
[iu9a6jd] (score 6, diepte 0) Wear different shoes every other day till you get used to it. Sounds strange, but I wish I had been given that advice when I started. You could even switch shoes at lunch if you drive yourself or have a locker. Different shoes will create different pressure points/ weight distribution and give you a slight break.

It does get better, I promise. You kind of toughen up after the first 1-2 weeks.  Muscles in your feet will strengthen.   

I went from working 10-12s at the fc to a very stationary desk job and after only a year I realized that spending only 3-4 hours on concrete felt exhausting to my feet.  

You’ll make it. Those rod shaped foot roller/massagers were helpful, too.
[iu9bmy5] (score 6, diepte 0) Ice water dip for about 5-7 minutes when you get home. Or freeze a water bottle and roll your foot with it. Get good insoles and don't buy cheap socks, "darn tough" is a kickass brand, but they're like $20 a pair. They have a lifetime warranty though, so if you put a hole in them you can get a replacement. Any well fitting thick merino wool boot sock will do though. just make sure to get the max cushion and that they don't slide around while you walk. Don't limp/compensate it only makes the pain worse. And if you have 2 pairs of shoes change them mid shift. All that foot heat and bending makes any arch support/foam useless after 5 or 6 hours of moving around.
[iu9h68x] (score 6, diepte 0) keep some waterbottles frozen in the freezer and roll your feet on em in 15min intervals for about an hour when you get home
[iuafm1u] (score 6, diepte 2) Dude , for REAL! These 12 hour shifts DRAG on. Luckily our FC doesn't care if we have a Bluetooth speaker so I just throw on some reggae and jam out. I've only been here 6 weeks so this will be my first peak season. Although I have been picking up all the overtime I can get so I am getting used to the long weeks. Unfortunately Uncle Sam rapes my checks EXTRA hard with OT
[iu9zaxj] (score 6, diepte 1 OP) I’ve worked at Amazon for 3 years and I got used to allllll the body pains…. But the steel toed shoes are the death of me I cannot adjust to these things
[iubk1qd] (score 5, diepte 3 OP) Same I’m 26 and 145 lbs I thought it was cause I just had a baby a few months ago but it seems like everyone is struggling.
[iubl8rx] (score 5, diepte 0) Good shoes. After a month you won’t feel a thing. You just need to get used to it.
[iubpbkl] (score 5, diepte 0) Shoes and insoles. Found some that work. Still feels more like damage control tho. I also have flat feet so that’s a major part of why it hurts so much.
[iuaanx2] (score 4, diepte 1) I have had better luck with the Timberland Pro going up a half size and wide. I also been wearing heavy boot socks. My feet are starting to feel better finally. I hope the peak season is kind doing 11x 5 days. Sometimes the 12 hr shift feels like time stops for the last hour….lol
[iuaij7n] (score 4, diepte 2) Facts. I fucking hate that we have to wear them now. My site doesn't really trip about it as i see some people (including myself) that wear sneakers. I wear vans lol. But try getting some thick socks for the steel toed shoes. They really help. I got some dickies work boot socks from walmart. 3 pair for $10. They're super thick and comfortable. Hope that helps.
[iu9zyis] (score 4, diepte 1 OP) I got those stupid Zappos shoes but I agree I probably should have done more research on the pairs I was getting
[iub3qyr] (score 4, diepte 1) this is the way.
[iuan66f] (score 4, diepte 0) also, look into a pair of OshaToes, they sling on over your regular shoes instead of wearing full on steel toes
[iubj5dn] (score 4, diepte 0) I feel you. Thought id like just working 10 hours on Saturday and on Sunday to get it over with. Nah I’d rather split it up throughout the week
[iuces35] (score 4, diepte 0) Get use to it.  I'm 40 and I'm good. At first I cried then I got over it. I don't even use insoles. Two years later...lol
[iu99f6d] (score 3, diepte 0) 10 hr / 12hr warehouse work is normal…! At least in the warehouse I’ve worked at . 1-2 weeks you will be used to it ! The body adjust pretty quick dispensing on your body type lol 😂 …
[iu9vl5y] (score 3, diepte 1) I do this and it works, take the edge off for a bit.
[iu9jdwj] (score 3, diepte 0) I went to flex now I do 8 hr 5 days a week just like I like it with whatever 2 days I decided I want off
[iu9z1h6] (score 3, diepte 0) I have plantar fasciitis and have suffered from it for years. And I’m super lucky because I have it in both feet 🙄 I’ve done steroid shots, stretches, custom orthotics, blah blah blah. At this point the only thing that’s going to help me is surgery and nope, not interested. So I just deal. It’s awful. Ibuprofen helps. Cold seems to help the most so when I get home my husband gets his hands nice and cold and gives me a good foot rub. Sometimes soaking them in epsom salt helps. I really researched the safety shoes on Zappos and made sure I chose a pair that wouldn’t make my feet worse. I got some good insoles (the custom ones from my podiatrist just aren’t meant for 10 hour shifts at Amazon) and I will do calf/foot stretches on my OP throughout the day.
[iua1y4g] (score 3, diepte 2) Well then do what i did. I bought myself some work boots that weren't steel toe but you couldn't tell the difference. Take your chances. There's lots of people that don't wear them. Its all the kind of luck you have, to get caught or not.
[iua244l] (score 3, diepte 0) I highly suggest going to see a podiatrist and have them do an assessment of where pain is coming from. Also go to a good running shoe store and have them do a laser size measurement of your feet. I found out that I had actually been wearing the wrong size shoes for over 10 years until I went a few days ago turns out my feet were wider than I thought they were. Also I can do nothing but highly recommend almost anything from the New Balance fresh foam lineup, specifically the fresh foam more v3 or v4, because they are so plush and comfortable it's not even funny, or even Hoka Bondi. That is if they allow those at your location. Also there are a couple online insole brands that I would suggest you take a look at, the two I usually go to are protalus and tread labs.
[iubbteu] (score 3, diepte 0) Takes 2 months until you don’t wanna rip your feet off 24/7 anymore and about 18 months for you to start being able to ignore the pain well lol
[iubfdvz] (score 3, diepte 0) Epsom salt, it's a game changer. And just a heads up, it's going to get a LOT worse in a few weeks when peak starts.
[iubfobp] (score 3, diepte 0) Imagine….12
[iubga0w] (score 3, diepte 0) I do 530-730 and don't feel a damn thing after 6 years in FCs. 
Give it a few weeks and have more than 1 pair of shoes to rotate. Your feet will just get stronger and you'll be good
[iubmhp5] (score 3, diepte 0) Try some foot stretches and exercises, you can do a couple of them at lunch like toe curls and toe splaying. Look up other exercises online, start off slow don't rush through them. Hope this helps
[iuc2b0h] (score 3, diepte 0) Vicodin and beer
[iuc7ene] (score 3, diepte 1 OP) Going to add this to my routine lol
[iucem9s] (score 3, diepte 1) This guy fuks
[iucukfk] (score 3, diepte 0) Your feet will get used to it. ibuprofen and resting the feet well for the time being. Ive worked 12's for a year and it's definetly possible (I usually work 3 12's and 2 10's a week now, keep your head up if you can and keep at your goals every day! Be safe!
[iucxwr9] (score 3, diepte 0) I've written this guide before but it bears repeating.  
First off this is going to take a little effort on your part, so if you are lazy and can't be arsed to do something it won't work. Go on Zappos and find some approved shoes that you think you could bear to be seen in for 10 hours a day. Then find several more pairs so your time isn't wasted. 

Make sure the shoes are available in your size and width on Zappos. Write down all of these and then google search a local shoe store that carries that brand of shoe.   
\*HINT\* Any shoe that is worth its salt is going to be sold in brick and mortar stores along with online.

Now go to said store and try out those shoes, make sure you wear the same sort of socks that you normally wear to work, if you wear thin socks to work wear that type to the store. Try them all on walk around a bit, maybe you feel like they are running a bit tight in the toe box, try a wide or half size up.   
Eventually you're going to find a shoe that you think is good, or good enough.   
Place the order for the shoes on your phone on the Zappos site right there in the shoe store to be sure they are still in stock. 

Thank any shoe store sales people who have helped you out in your search, say something like "I'd like to think about it." or "I'm going to keep looking." or if you're a dick just leave all the boxes of shoes in a pile, say nothing and leave, your choice. 

&#x200B;

Once the shoes show up open the box and make sure they are the correct shoes, if you ordered an 10.5 EE make sure that's what they are. Put on some clean socks and wear them around the house for a little bit. Don't go outside, stay inside and wear them. 

If they are good wear them to work. Keep another pair that are broken in out in your car and if your feet start bugging you the last few hours ask if you can run out to your car to switch shoes real quick. Eventually your shoes will break in. Think of it this way you wouldn't go on a big hiking trip with brand new boots without testing them or breaking them in that's a surefire way to be hurting, same with work.
[iueu2ql] (score 3, diepte 0) If you are unused to walking much or have tender feet, you might consider armoring your heels with moleskin or duct tape BEFORE you develop nasty blisters. I keep a roll of silver duct tape in my trunk, next to a pile of clean socks. Slap a tape patch on the back of your heels while your feet are clean and dry, roll your socks up, boot up and go. Also, limit your in-boot time as much as possible, if you have any sort of commute I recommend that you wear comfy breathable slides both to and from, and definitely get out of your boots AND damp socks as soon you you hit the parking lot, get into something warm and dry asap. Your feet will thank you. Also, get yourself a boot drier and keep your boots on them between shifts, starting a shift with damp footwear is just asking for more pain, not to mention foot stank, athletes foot, etc.
[iu90g2o] (score 2, diepte 0) I do 12hr
[iuag4dk] (score 2, diepte 1) Same,  shits brutal and feels more than 18 hour but I love those 4 days off!
[iu954kv] (score 2, diepte 0) Voltaren, good insoles, Dr. Teals Epsom salt soak for feet, and I personally invested in a good foot massager.
[iu9y340] (score 2, diepte 1) Would you recommend going to flex if I’m only seeing half days available to pickup shifts? As in 5 hour morning interval, 5 hour afternoon interval.

No 8 hour shifts sadly.

Did get an offer for FLEX, though. Trying to decide if it’s worth it, I’ve heard you gotta work a lot of nights to make up that 30 hours. 

Kinda like my day job so i’d love your advice.
[iubdk1p] (score 2, diepte 2) I wouldn't unless you are very cool with your am and pa Because that's how I get by. plus I stay in the top 5% in picking that also help out
[iu9skyl] (score 2, diepte 0) Well I do 12 x 3 days.  No foot problems until April when steel toe required.  Tried 3 shoes, many many Insoles.    Finally last pair got wide and half size up.   Took the insoles out shoe came with and put in Dr Scholl's gel long work day insoles and that with 2 Ibuprofen b4 work way better.  Still feel I need a better insole.   Going to podiatrist next week for maybe orthotics.
[iu9t004] (score 2, diepte 1 OP) Just ordered the insoles I’ll be trying this with the medicine thank you so much. It’s definitely the shoes. I worked at Amazon for 3 years and no issues until I moved to this new location that requires the steel toe shoes and I at 7 hours in my feet are hurting which is so strange to me
[iu9twlq] (score 2, diepte 3 OP) Damn our facility just told us no more 50 hours instead we will do 4 11s so just an hour flex up for peak but we’ll see how long that lasts
[iuatkej] (score 2, diepte 2) Yes I've heard that too about those shoes.   I'll try those next.   That last 1 hr 45 min after our last break is killer.   We have this awesome PA and he will come and ask if we want a packing break and he will pack for like 10 min and I'll run around and collect totes, go get polybag rolls for stations that need them and large bag rolls for stations that need them.   That little break during the last hour is awesome .
[iubdeuo] (score 2, diepte 0) good insoles with lots of support.
[iucj13s] (score 2, diepte 3) Yeah, really good ones too. Not sure if all building do it but it doesn't hurt to ask
[iudic4k] (score 2, diepte 4) I start 11/16 so I’ll definitely be asking. Thank you!!
[iubg1s8] (score 2, diepte 0) Did you mean 12? You get used to it after a couple weeks
[iubjcck] (score 2, diepte 1 OP) Facts 10 hours standing is crazy when u actually do it
[iubjihr] (score 2, diepte 2) It really is. I’m only 27 and pretty fit too. It’s still fucked. Gonna try to change my schedule soon
[iuc84po] (score 2, diepte 1) 1 year and 4 months and my feet hurt more every day
[iuccgq0] (score 2, diepte 2) Damn you might need better insoles/shoes then.I even broke my femur and have a rod in it and I’m fine lol.
[iuc60tc] (score 2, diepte 1) Zappos sucks hella
[iucg0an] (score 2, diepte 0) Airmax or some hoka's
[iuchrhg] (score 2, diepte 0) Supportive compression socks help a bit
[iucuotp] (score 2, diepte 1) EDIT* FORGOT TO MENTION SHOES, BUY QUALITY SHOES TO PROTECT YOUR FEET. I personally don't like the free ones they let you chose when it comes to comfort.
[iusumv2] (score 2, diepte 0) i moved to pack bc of this and my life is way easier
[iu8vc6r] (score 1, diepte 0) Welcome to FASCAmazon, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. We have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/FASCAmazon) if you have any questions or concerns.*
[iuafwjo] (score 1, diepte 1) Thanks for the advice, I am gonna try this after tonight's shift
[iuawcb8] (score 1, diepte 1) This plus get a small dense rubber ball (lacrosse ball) to roll between your feet and the floor. AMCARE should have some in stock
[iu9t37k] (score 1, diepte 1 OP) Awesome I’m trying to get flex shifts too
[iu9tr00] (score 1, diepte 2) Yeah they still hurt but only a quarter and I could take more Ibuprofen after 8 hours  but I dont want to.  Need to get this under control b4 50 hour peak weeks.
[iuau12h] (score 1, diepte 4) We haven't been told yet if it changed this year. I hope that's the case.  I hate over time.
[iu9vgk2] (score 1, diepte 1) I think I'm trying a size & width up next time around, my feet are in the usual pain of being on them for a full shift. The same as walking at a fair or something for a long period of time; my feet have some sort discomfort no matter the shoe type, flip flops, heels, work.
[iua53g1] (score 1, diepte 1) I also have plantar fasciitis (and Achilles tendonitis). What shoe did you end up getting from Zappos?
[iua0r2r] (score 1, diepte 0) I recommend seeing a podiatrist *before* there may be any serious issues with your feet, and getting custom made inserts and Before/After medical records. If you have high arches or flat feet, etc., it’s a good idea to know that in advance. I had high arches but never had issues with my feet until after working for Amazon. Not seeing a podiatrist first is my biggest regret, personally. 

I don’t know which department you work in, but if you pick or cart run for Inbound… please be careful, listen to your body, stand up for yourself, set boundaries, and remember you don’t have to cart run/do indirect if you don’t want to (and especially if you’re hurting), and most importantly: don’t try to be in the top 10.
[iub5zxn] (score 1, diepte 1) I recently got my custom shoes from my podiatrist and I don’t have any pain from standing anymore. I’m a new hire so I haven’t worked my full shift yet, going to test these puppies out on Wednesday.
[iubbz7k] (score 1, diepte 0) You'll get used to it
[iubf4us] (score 1, diepte 1) The Safety guy in my building gave me a great pair of them, apparently most people don't even know to ask for them.
[iuciwl8] (score 1, diepte 2) They provided insoles for you?
[iucd0hn] (score 1, diepte 3) I have damaged ankles and knees (nerve damage) from a car accident. Sciatica that causes numbness in my feet and legs when my back muscles get too tight, and plantar fasciitis which is made worse when my feet are numb because I cannot balance correctly. I have high arches and wide feet… tennis shoes NEVER fit my feet correctly, even with a professional fitting. My arches aren’t where the arches are built into shoe inserts so they cause more pain instead of helping… I’ve wasted hundreds on inserts over the years. My feet never hurt when I’m barefoot or in something like flip flops where they aren’t restricted by shoe shape. We also found out that the hard plastic heel in safety shoes was bruising my heels. With the help of an awesome person in safety, we found a shoes that has more like a sock structure so no pressure around my heel and even the composite toe has padding. Still trying to figure out something for the footbed because structured inserts don’t work and the built in insert the arch is at my heel 🤦🏼‍♀️
(9 reacties met lagere score weggelaten)

