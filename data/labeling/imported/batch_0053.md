# Label-batch batch_0053

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
Schrijf het resultaat naar `batch_0053.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1ui18ib, 4f0kh7, t89a6n, p8xddt).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1ui18ib ===
SUBREDDIT: r/bartenders
DATUM: 2026-06-28  SCORE: 4  REACTIES: 46
TITEL: Best shoes? Best insoles? My Hoka Bondi SR’s fell apart almost completely now after 1 year of owning them…
POST (source_id=post):
I used to wear Sketcher non-slip work sneakers but i’d have to get new ones every 6-8 months or so. So i decided to finally invest in Hoka’s. I really thought the Bondi SR’s would be the best option for me working 12+ hour days behind the bar… I bought them a little over a year ago paired with a pair of copper SuperFeet insoles and they were great, but within 6 months they already started falling apart - ripping/tearing/creasing, it’s crazy how fast they went to shit. My feet also constantly slide to the outsides of the shoe, giving me blisters every once in a while. Now they are basically completely ripped apart and they hurt… Still wearing them but it’s cause i have no other choice right now, i can’t decide on any other shoes. 

Also, the copper SuperFeet insoles were good at first but they were WAY too hard. Felt like they provided no cushioning… What other colors are good from SuperFeet that ACTUALLY provide cushioning? Cause at this point i’ve just been using random Dr. Scholls insoles from Amazon every 3-4 months. I wanna go back to SuperFeet but i need ones with a good amount of cushioning. I don’t have flat feet but a little arch support would be nice. 

My criteria for shoes:  
• All black   
• comfortability (all day lasting)   
• Non-slip  
• Waterproof/water resistant 

PLEASE help me, i really need some good long lasting shoes that fit this criteria. Idc what the price is.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ouc4l09] (score 50, diepte 0) If you are walking a lot and wearing the shoes daily, getting six to seven months out of sneakers is GOOD.
[ouc4mlx] (score 17, diepte 0) anti-hoka action, i fuckin hate those ugly ass expensive shoes, and how theyre marketed absolutely everywhere 

i personally swear by boots. leather and waterproof, big ol thick soles, slip proof. breaking them in kinda sucks, but thats temporary. blundstone are probably best and the chelsea doc martens are usually good, but they have lines sold at like journeys and shit that are cheap and fall apart. plus if they're boots and made of real stuff like leather and rubber, you can get them resoled if the wear gets bad
[ouccxa9] (score 12, diepte 0) having 2 pairs of shoes and wearing them every other day often lasts quite a bit longer than wearing the same pair every day, so if you find something you like try getting a second pair and rotating!
[oucqkhd] (score 7, diepte 2) If you like the look of dr martens, check out Solovair. They were the company that produced old school dr martens before they moved operations to China or wherever they're currently produced. Very high quality.
[ouc4r2c] (score 6, diepte 1 OP) damn yeah that’s true… i guess im lucky to even have gotten that much life out of em in over a year lol
[ouc7g78] (score 5, diepte 2) A year behind a bar in sneakers mustve had a protective shell built up
[oud480h] (score 4, diepte 1) Do they last.... twice as long?
[oucro4n] (score 4, diepte 0) I love my hokas. I'll spend 170 bucks every seven months on shoes as long as I don't wake up in pain
[ouc4utx] (score 3, diepte 1 OP) hmm that’s interesting! never thought of boots!
[ouc98q3] (score 3, diepte 0) Currently in Birkenstock Tokios and I really like them. I have worn Doc chelsea boots before and liked them enough to wear out two pairs. I am buying blundstones soon for the first time and based on what I’ve read I’ll like them a lot. I’ve gone through a few pairs of Hokas and they wear out way too fast for how expensive they are.
[oufts2y] (score 3, diepte 2) def more than twice! they wear out muuuuuch more quickly when worn everyday
[ougepr5] (score 3, diepte 0) I like wearing Vans Made for the Makers. They were discontinued for a few years but they’re back now
[oue996m] (score 2, diepte 3) I'm rocking solovairs up over my calf at my bar right now. I wear them every day and have for years. With good care, they'll just last and last. In fact I need to get them resoled and I'll get another five years or so out of them I bet. They're comfortable especially with insoles and they protect my feet and legs from all the gross stuff and sharp corners.
[oucgzwq] (score 2, diepte 0) I can usually get a couple years out of Dansko's more stylish products like Walker or Travis 

I hated the Hokas too, felt like the cushion was gone in 3 months and the toe box is tiny!
[oud4x9n] (score 2, diepte 1) Look interesting. My Hokas are about to be needing a replacement. I may give these a shot.
[ouejn0t] (score 2, diepte 0) Redwing Marshall cowboy boots...

Bet you can't tell i work in a line dancing joint 😅

But seriously, I love them. Comfy, non-slip, waterproof, and easy to kick off after a long shift.
[oufp8o4] (score 2, diepte 0) I love onclouds. Depending on what you’re looking for for ankle support they have higher and low tops. But they are amazing and last a long time. The best waterproof no slip shoes I’ve had In a long time!!
[oufrhmn] (score 2, diepte 1 OP) forget it, found em lol  
thanks for the rec, i’m looking into them!
[ouft04q] (score 2, diepte 3 OP) wow great!! thank you!!
[ouft0rm] (score 2, diepte 3 OP) awesome!! thank you!!
[oum5t08] (score 2, diepte 3 OP) hey! got a lot of recs for a lot of different shoes on this post. Mostly boots, i don’t think i’m ready to move to boots yet, i like sneakers. so i actually took your recommendation!! those sounded too good to pass up and i never even heard of the brand before! i actually went to a Dicks today and spent an hour trying out the different versions they had. i ended up going with the Cloudsurfer Trail 2 Waterproofs. I know they’re more “hiking” shoes but with the way i move my feet and how comfortably and waterproofing are my main focuses, these felt perfect!! hopefully they work! 🤞 

thanks so much again! i’ll report back soon with results after a few shifts!
[ounczmo] (score 2, diepte 5 OP) hell yeah! that’s why i wanted to go in store. takes days to finally come in when you order online, then you gotta test em, and if they’re not right you gotta package em and ship em back. it SUCKS. and yeah the guy working there was SUPER nice and helpful. i feel confident in these. even though they’re technically “hiking” shoes, they do seem to be more up my alley in terms of what i’m personally looking for in comfortability, style, and performance. 

and yeah they were a pretty penny but hopefully they last longer than my Hokas! lol 

thanks so much again!!🤘
[oufuboq] (score 2, diepte 0) I love my snibbs (mostly for the waterproof my service bar flooded one time and I had to stand in 1 inch  of water making drinks all night) might not be the most comfortable but I havnt tried changing the insoles yet. I do get about a year to year in half out of them before I need to replace because the bottoms wear out i do about 15k steps per shift so 30k on a double
[ouhi1ub] (score 2, diepte 1) Oh hell yeah I heard so many great things about these shoes I'm looking forward to picking up a pair
[oujbsqx] (score 2, diepte 0) Black Nike air forces.  I live in mine and I'm pretty hard on shoes and I still manage to get a few years out of each pair
[oucdquk] (score 1, diepte 2) I don’t know if you’re a guy or not, but I started buying combat boots with the zipper on the side. Mostly waterproof, fairly comfortable once you break them in. $40-50 at Walmart. Last 8 months or so of heavy duty
[ov9v5bw] (score 1, diepte 3) 5.11 ATAC 2.0 8" side zips for me. Go up half a size for better comfort. Got one of my old female bartenders to switch over to them too. The nice thing is, that when wearing pants, you can't even notice that they're boots. Just looks like a nice work shoe.
[p0sqz0g] (score 1, diepte 1) Have you ever tried Abeo brand by Walking Company? Durable and ankle support. You change out the insoles every 2-3 months. My arch is average so I get the neutral boot and inserts.
[ouhja6q] (score 1, diepte 1) Yeah OP and others, switch off your shoes every other day so you are not wearing the same pair 2 days in a row. This protects your feet in the long run and also extends the life of each shoe. I have no opinion on boots or sneakers as I use both and they both have worked well for me (i.e., boots at the club, sneakers at dive bar).
[p0srbew] (score 1, diepte 1) It sounds like the equivalent of not wearing the same bra two days in a row. The elastic needs time to bounce back. Strange reference lol
[oucocip] (score 1, diepte 0) Brunt Boots were a game changer for me
[oucplg5] (score 1, diepte 0) Everyone I work with rocks Altra Olympus. It’s been a game changer, especially since I rocked chuck taylors for about 15 years of bartending
[oulmca4] (score 1, diepte 1) Same, I have back problems likely due to a mix of genetics and working this job for so many years, so I need that extra support. Switching from Sketchers to Hokas was literally like night and day after my shifts - day one I noticed a huge shift. I invested in a second pair a month later and I try to switch between the two day-to-day to help them last longer.
[oudjfb4] (score 1, diepte 0) I loved the feel of my Hoka sr but mine also wore out in a year. Went through three pairs before I gave up on the brand.
[oudjj5a] (score 1, diepte 1 OP) damn :/ what’d you end up getting instead?
[ouf2qqy] (score 1, diepte 0) Danskos from Germany, a little on the pricier side, but I’ve been wearing them for 4 years almost daily. I was wearing merrells and had to replace them every 9 months or so, but these Danskos are legit. Super comfy, non slip, survived years of work and plenty of outdoor adventures including volcanic rocks in the Galapagos.
[ouf5t1r] (score 1, diepte 0) If you (OP or anyone else reading this) can sacrifice on the nonslip criteria, I have been LOVING the Doc Marten DMXL Chelsea boots. They are extremely light and feel like a supportive sneaker, but the leather and sole are proving to hold up really well. 

Also, for what it’s worth, I usually get about 7 months to a year out of my work Hokas, but the ones I have for casual use have lasted years. I had a pair of docs that lasted 4 ish years behind the bar but even though they weren’t uncomfortable, the change in my quality of life when I switched to the hokas was very noticeable and welcome. The balance between ultra comfort and ultra durable is hard to find, but the DMXLs have really hit that sweet spot for me.
[ouf62om] (score 1, diepte 1) I haven’t looked into whether or not there’s a way to resole or treat a shoe to make them nonslip but honestly it might be worth exploring if these seem like something that would work for you (the style is pretty bulky but my pants cover most of it and for how comfortable they are, I don’t mind)
[oufratw] (score 1, diepte 1 OP) what brand is that?
[oufs8gs] (score 1, diepte 2) I used to love Skechers no slip as well but the mesh had me with soggy toes after a long shift standing in front of the well. The first pair of oncloud after a 12 hour shift w dry toes I was hooked!! When you check out the website it also tells you length of time for optimal wear. Good luck!!
[oufs42h] (score 1, diepte 1 OP) do you know which model would be best for our profession specifically? i def need waterproof ones. nonslip i dont mind too much at this point. i just mainly need comfortability and waterproof
[oufsqfa] (score 1, diepte 2) The cloud6 waterproof are great for durability and waterproof. The model I Previously had that was more high top Is discontinued but the cloud6 or the Roger’s are good for waterproof
[ouml6hd] (score 1, diepte 4) Awesome!!! I’m so glad I was able to help, and the sales associates at dicks steered you in the right direction and you could physically try them on before buying online. Thats the worst when you order and they aren’t what you want. Wish you the best my friend, and remember sometimes it hurts the pocket for a nice pair but you make it tenfold in your work ability after. Make that money!
[oufuvvb] (score 1, diepte 0) I refuse to wear ugly shoes and unfortunately Hokas fall in that category. I tried Snibbs’ boots, but to me they’re not worth the spend. I miss the years of Vans’ comfy cush. If you can find a fit that works for you, everyone recommending Docs is right. Otherwise I would say asics or certain adidas have been my best bet.
[oufuxri] (score 1, diepte 0) I refuse to wear ugly shoes and unfortunately Hokas fall in that category. I tried Snibbs’ boots, but to me they’re not worth the spend. I miss the years of Vans’ comfy cush. If you can find a fit that works for you, everyone recommending Docs is right. Otherwise I would say asics or certain adidas have been my best bet.
[ouj05i8] (score 1, diepte 0) Ross usually has Nike Air Max shoes and I’ll throw a $60 power step insole in

That gets me about 1.5 years out of the shoes as a big guy who does 12k steps a day for work
[ouls5l5] (score 1, diepte 0) I walk on the outside of my feet, so I needed boots. The Cat second shift work boot has been great, with the Powerstep Wide Fit insoles.
[oumiwt1] (score 1, diepte 0) I work 50+ hour weeks and my redback waterproof chelseas have held up solidly for almost a year and a half now. Not cheap, vut I think I'll come out ahead of most in terms of value over time, and definitely on comfort
[ouo6npo] (score 1, diepte 0) Thorogood or Danner boots will see you through!
[ovp9rin] (score 1, diepte 0) Two pairs, maybe even four based on your shift length so you can switch them at the midpoint
[p0sqmzc] (score 1, diepte 0) I swear by Abeo brand by Walking Company. I have an average arch, so make sure I get the neutral insole with a leather boot with ankle support. And your insoles in boots like these should be changed every 2 months, complete boot change every 6. 

Shoes are not made for that many miles. I believe they are good for about 200 miles. In this job, that’s roughly 2-3 months max. The leather boots are heavy duty so insole change works. Invest in your feet. I’m telling you from the deepest part of my soul!!
[ouc7os8] (score 0, diepte 0) Custom Nike Air Force 1's

=== THREAD 4f0kh7 ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2016-04-16  SCORE: 4  REACTIES: 38
TITEL: What are the best socks/shoes for a kitchen?
POST (source_id=post):
I can't find the right shoe/sock combination, my feet always suffer. They smell bad, they hurt, the usual kitchen stuff. I'm currently using a pair of clearance rack Timberlands (leather) with running socks.

 I've tried high top leather boots (too hot) running shoes (won't stay clean) basketball shoes (both) crocs (crazy bad smell in ones made for kitchens, food falls through the holes in normal ones) just regular leather work shoes from fleet farm (probably the best so far) and skateboarding shoes (too hot/sweaty)

For socks, I literally bought one of everything from my local target, and other places. I assumed thin would be better, but it seems to be worse. I found some really expensive copper infused socks that claim to kill bacteria, and smell is my biggest concern, padding is second. Not sure what to think of those. 

Any advice is very welcome. I'm sure I'm not alone here. I hope you all have healthy happy feet! Thanks for reading!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d24ypyz] (score 19, diepte 0) Currently wearing two mismatched socks I pieced together off my floor yesterday and a pair of kswiss that are half a size too big that someone gave me. The toe of one is warped because I spilt grease on it changing out the fryers stoned as hell at 9 in the morning. Highly recommended.
[d2597iw] (score 6, diepte 0) I wear by Crocs, proper Crocs. I wouldn't be seen dead in them outside of the kitchen, but I have only ever slipped once while wearing them (on stock from the stock pan) and I used to have knee problems, now I don't!      

Socks are simple: I buy in bulk, about 30 pairs of exactly the same socks which makes it impossible to mismatch!
[d25166h] (score 5, diepte 0) I know it sounds pretty crazy, but relatively thin Marino wool socks work surprisingly well. 
There's some science behind it too, with its moisture wicking properties, evaporative cooling and whatnot.
I've always been a clog type. Berkies don't fit me well, I have a pair of Dansko Pro XPs that I continually exchange at REI.
[d24yba4] (score 3, diepte 0) http://mozoshoes.com
I was a Birkies clog user before I discovered this brand of shoe.  I'd suggest two different pair to alternate daily.  60-70 hour weeks and my feet never hurt.
[d261opv] (score 3, diepte 0) For socks, buy Dickies.  Kevlar reinforced, wicking, and bad ass.  Second best, find some decent Merino wool socks for hikers.

For shoes, I'm a firm believer in Wolverines gum-soled, laced boots.  I can run through oil spills.

Otherwise, use your own experience and needs.

Your shoes should run about $120-$150, and your socks should run 10% of the shoe.  Good socks are not cheap. Although, Dickies Kevlar will only run about $8-$9 a pair.  A steal.  (yes, I did say a pair, not a dozen.  Good socks aren't cheap.)
[d29yce5] (score 2, diepte 1 OP) I like your attitude, but I probably won't be buying those.
[d25s7zd] (score 2, diepte 1) Yep, wool socks, would recommend. Even medium thickness 'hiking' socks work well for me.
[d28fmpr] (score 2, diepte 1) Same here I wear normal shoes to and fro work and keep my kitchen crocs in my backpack otherwise never to see the outside world
[d259hvb] (score 2, diepte 0) Timberland Pro work boots with Dickies socks.
[d25lty4] (score 2, diepte 0) as someone who has wide feet, I swear by my Keens
[d2g0gzd] (score 1, diepte 1) I feel like working with grease while stoned is probably a bad idea 

disclaimer: not a cooking person, I just like hanging out here
[d2jte1d] (score 1, diepte 2) changing the fryer out in the morning probably means the fryer has been off all night, and the grease is cold
[d27z3i1] (score 1, diepte 1 OP) Not sure if that's a joke, but it just might work. The no socks thing seems crazy.
[d28bgim] (score 1, diepte 2) I'm not exactly sane
[d2500oy] (score 1, diepte 0) I really like compression socks by Gildian that go up to your calves.

I recommend http://m.zappos.com/crocs-neria-work-black

They only make them in women's sizes, so I wear a size bigger.
[d278wcq] (score 1, diepte 1) Damn those thing chew my feet up like sandpaper
[d251dkh] (score 1, diepte 0) Mozo shoe and darn tough ultralight no show sock
[d2521k9] (score 1, diepte 0) I'm awful and get away with it, but I can only wear vans. I have these disgusting bright blue vans(used to be bright anyways) that I've been wearing in the kitchen for about a year now since my SFC look-alikes bit the dust. Ive tried a few of those Walmart or Payless brands, but holy fuck do those fuck my feet up, I've never had foot and ankle pain like that before those shoes. 

So now I wear these disgusting vans. Never slipped in em(I'm a slider,) but I do have a quarter sized scar on my foot from when a glob of oil jumped out of the fryer on my foot. Ive taken some mean burns(filtering oil splashback to the face, grill cleaner/fry baskets/grill cleaner/bacon grease to the arms) but that foot burn was the absolute worst. 

 TL;DR: My favorite setup is wacky dress socks and vans.
[d259hu9] (score 1, diepte 1) I've worked in vans for a couple shifts by accident and they are horrible for me! I can handle the slip, but they just make my feet ache like no other
[d25lsxb] (score 1, diepte 2) Ive been wearing them for like ten years, maybe my feet just like them by now idk
[d29y7h2] (score 1, diepte 1 OP) I like it. I was a skater for about a decade, now it's occasional. Those shoes are made to be comfortable under the WORST circumstances. Good grip too. I was always a fan of Vans, ES, supra, DC, and of course the Osirus D3. Pretty sure that last one makes me old now.
[d2awg5r] (score 1, diepte 2) Ayyyy I skated for about a decade too. Half cabs were my shoe of choice. Idk how people skated in authentics. I'd have a hole in the side of em in like 20 minutes
[d25uf7k] (score 1, diepte 1) I do the exact same and I can attest to this. My knees feel so much better.
[d29ya4s] (score 1, diepte 2 OP) I remember having my work crocs in the back of my SUV. That is not an option. They basically made my car unusable.
[ibwg30x] (score 1, diepte 1) Proper crocs, as in their work shoes? I'm having mad knee problems standing all day.
[d25cios] (score 1, diepte 0) I wear a pair of Russell athletic sport socks, and a pair of those rubber no slip crocs you get from Walmart. Best ventilation and cleanliness I've gotten from work shoes so far
[d25qzc8] (score 1, diepte 0) Calzuro shoes are the best imho. Really, really durable and comfortable enough to wear all day. A solid bamboo, antimicrobial sock is what I use. Super cheap on amazon.com.
[d25rmif] (score 1, diepte 0) I wear kitchen crocs with one small hole pierced in the side to let some air out and regular socks. Occasionally I'll wear them round the house as well, nothing else I have is as comfortable! 
At the end of the day though, long days on your feet in any shoes is going to result in feet and smells that aren't the freshest I'm afraid.
[d25t83b] (score 1, diepte 0) Compression socks and Danskos any day of the week. Avoid buying Danskos online, (the sizes are European) any shoe store up to snuff should carry them. Comfiest, most durable shoe I've ever owned!
[d25ve98] (score 1, diepte 0) Dansko clogs and wool hiking socks over here. The socks seem to be the deciding factor. Also, if you are worried about sock smell, buy 8 or 10 pairs of the same sock and change them daily. Some people just have stankier feet than others and can't recycle socks.
[d26r8ay] (score 1, diepte 1 OP) Haha. I bought 5 dozen pairs of the same socks so I wouldn't have to sort them. Yes that's 60 pairs. And I absolutely have to change them daily.
[d26r5pe] (score 1, diepte 1 OP) Thanks. This is exactly what I wanted. I will spend a little extra to be clean and comfortable at work.
[d26c6qo] (score 1, diepte 0) I recently bought some SFC shoes and they're OK, worth the money. 

I had my last pair for two years until the toes were exploding. only up until the last month or so was it impossible to keep the treads clean for a few days. They were 35 bucks at Payless and I will greatly miss them.
[d26znw1] (score 1, diepte 0) Keens--never slipped once!  Feel great on my feet, ordered from zappos
[d272a5k] (score 1, diepte 0) Vote for Mozo, and personally I like the Sketchers Worx series, they make a model that looks like a leather cross-trainer and it's the best non-slip lightweight kitchen shoe I've worn! Then again I have very particular feet.

For socks I always go for the And1 or Puma basketball crew sock from walmart that comes in packs of 10 pair for $10 bucks. If they start to stank or get any holes I chuck 'em!
[d27ill0] (score 1, diepte 0) Socks I have darn tough hiking socks...through the rest out because I got tires of having holes...have been rotating between 10 pairs for the last 2 years not one hole yet...and they're comfy.


For shoes I have croc and Birkenstock pairs both work fine for me.
[d29xc5q] (score 1, diepte 0) I have a pair of non slip leather kitchen shoes from Klogs. They molded really well to me feet and are very comfy, the grip is outstanding. I've added heel cushions but that's just my preference. 

For socks I wear smartwool knee high compression socks. They actually really vent well even under my pants. Not much for cushion but my shoes help out. I have seen far too many varicose veins from people in stationary jobs, definitely a benefit to have compression.
[d25gqzs] (score 0, diepte 0) Usually I wear some mismatched  socks that I buy from target. And for shoes I have a pair of dansko wil. Have to say after 2 weeks of breaking them in they are my favorite pair of shoes that I have owned. They are just not fun to walk long distances in( like walking home ) but other than that I highly recommend
[d24zdy9] (score -1, diepte 0) I wear no socks only gold bond and a pair of klogs with dr sholes inserts

=== THREAD t89a6n ===
SUBREDDIT: r/bartenders
DATUM: 2022-03-06  SCORE: 182  REACTIES: 239
TITEL: What are some good remedies for achy body from being on your feet constantly and all of the repetitive motions we do? Feet, legs, back, shoulders, forearms are what gets the most achy for me. I feel like I’m 90.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hzmn2xw] (score 224, diepte 0) You need better shoes.
[hzmrrpr] (score 114, diepte 2) Well there’s your problem. I’d get something with better arch support. I’d also recommend checking out some compression socks, nurse friends recommended them to me and they are a game changer.
[hzmrf30] (score 77, diepte 0) Lots of water, stretching, and magnesium.
[hzmsxbv] (score 74, diepte 0) My fave post double shift activity is a bath with epsom salt

Edit *and vodka
[hzmnljc] (score 49, diepte 1 OP) Probably. I have worn almost exclusively skate shoes my whole life. You have any suggestions of a brand that works for you? My bar is casual.
[hzmuu8j] (score 46, diepte 3) When I first got compression socks I was beyond shocked at the difference. 100% agree!
[hzn1mi4] (score 31, diepte 4) Beyond... Socked!
[hzmsspd] (score 27, diepte 0) Rubber floor mats.  Chef shoes.  Good posture and ergonomics.  Regular massage.  Frequent stretching.  I started nursing as a shoe size 9.  Now I’m a 12.
[hzmx57w] (score 26, diepte 1) Bath vodka sounds creepier than shower beer
[hzmsz1w] (score 24, diepte 2) Kitchen clogs from shoes for crews have been my go to for a while, along with a pair of gel insoles. For backpain or other aches, I liberally use Tiger Balm. Ice packs and heating pads are also your friend. Yoga does wonders for keeping the aches away. A stretch here or there during the shift with some toe touches keeps me limber-ish.
[hzmse6u] (score 21, diepte 0) I do 10 minutes of Yoga every morning (DDPY to be exact) to deal with my elbows and Knees (though I also powerlift, which doesnt help). But for real, good shoes are the key. My life changed when I invested in some shoes with **good bridge/arch support** For work.
[hzmrnua] (score 20, diepte 1) Stretching after a long shift is key for me!
[hzmtpd4] (score 19, diepte 2) Before and after STRETCHING … WATER WATER WATER !
[hzmtzpm] (score 16, diepte 0) Same as if you were in the trades. Spend top dollar on your bed and your shoes, have an exercise routine that includes regular stretching and have a physiotherapist who you see whenever you have pain that is persistent even if it's not 'bad' yet.
[hzmvcmr] (score 15, diepte 1) FREE YOGA WITH ADRIENE

https://youtube.com/c/yogawithadriene
[hzn75fg] (score 13, diepte 2) Walking shoes, ASICS, new balance, on cloud and sketchers are good starts. Maybe formal boots if you have weak ankles too. 

Plus go see an ortho or sports med clinic and get prescription insoles. They will be pricy. Expect to spend about $150-200 for both the shoes and the inserts. But this combo will last years.
[hzn1oal] (score 12, diepte 4) Where you... Blown off your feet
[hzmvwva] (score 12, diepte 0) A couple days off
[hzmxggi] (score 12, diepte 0) Birkenstock’s and yoga with Adrien’s YouTube video of yoga for service industry. I used to be in a similar situation and that jump started my yoga practice and my work endurance is through the roof
[hzmtkvj] (score 11, diepte 0) Better shoes is huge. If your bar doesn’t have mats, ask management to provide some. I’ve also found that after 20+ years behind the stick, if I don’t get a minimum number of hours prone, then my whole body hurts. Not necessarily sleep hours but all the way laid out hours
[hzn4xp3] (score 10, diepte 3) Very important tip: under normal circumstances, no situation will become a catastrophe in the 10 - 30 seconds it takes to chug a glass of water a few times a shift.  Give yourself a moment to hydrate, breathe, and reset. 

If something does turn into a catastrophe, it was going to happen anyway.
[hzmwumz] (score 9, diepte 2) Keen’s!!! Wide toe box, great soles and completely waterproof! The insoles need better arch support, for me. Grew up skating too and love shoes like Vans and other flatter shoes for everyday stuff, but the added cushion and good arch support are key!

https://www.ebay.com/itm/255361803008?hash=item3b74bfe300:g:juIAAOSwO8Vh95e~

Good posture.

Stretch (even on shift there are one’s you can do in slower periods.

Hydrate!!!

Epsom Salt bath after work.
[hzn2276] (score 9, diepte 1 OP) I definitely bought epsom salts this week! I've never been a bath person, but I have to say, it was pretty relaxing!
[hzn7ctl] (score 8, diepte 3 OP) If it prevents my body from rapid deterioration and helps with the aches and pains, I'll fork over the cash fo sho. Thank you for the suggestions. I'm looking at shoes and reading reviews now. I appreciate it.
[hzn87na] (score 8, diepte 4) Regardless of the shoes go for the inserts. I put them in everything
[hzn2yq9] (score 8, diepte 1) Am I stupid or are you saying your feet have grown 3 sizes?
[hzn1sh5] (score 7, diepte 4) You will... Stand your ground on this
[hznaabd] (score 7, diepte 5) I am 100% shoe they will.
[hzmr0g6] (score 7, diepte 1 OP) Damn… I’m sober…
[hzneqmp] (score 7, diepte 2) You are not stupid and this is the result of 25 years on my feet.  I also got plantar fasciitis and have great orthotics in my shoes.  Your feet carry all of your weight and they get punished on hard floors.  Don’t mess up your feet or your back.  Ya got one spine for the rest of your life.
[hzmy0x1] (score 6, diepte 2) We don’t require non-slips at my bar because we don’t have a kitchen so I wear Hoka running shoes or ultra boosts. They feel just as good and don’t look as bad as a lot of the service industry stuff
[hzmqrrt] (score 6, diepte 0) Shots, weed and/or drugs of choice
[hzmt6ha] (score 6, diepte 1) At some point you get old enough where those things just make it worse and rob you of the good sleep you need to recover from a long night hustling in the well.
[hzn1uhe] (score 6, diepte 3 OP) I so badly need to be drinking more water. Its hard to get any water in during my shifts because we have been so busy lately. But I'm definitely making an effort and I got some of those liquid IV things. They seem to hydrate me faster than just water alone.
[hzn6xxd] (score 6, diepte 2) Nah just more corporate shrinkflation
[hzmvkti] (score 6, diepte 2) There are 100’s of pounds of epsom salt in those tanks! They absolutely do heal sore muscles! 🖤
[hzn2yl1] (score 6, diepte 2) Or just the result of some good old fashioned redneck engineering
[hzn2y7n] (score 6, diepte 1 OP) Ya girl quit that drank last year... Probably why I notice all the aches and pains now haha.
[hznzs4i] (score 6, diepte 0) Strength training

I injured my foot 6 years ago. It still hurts... Unless I do my daily strength training. And then I can work 12 hour days with no pain.

Calf raises, half step downs, hop scotch shit just bouncing around on one foot.
[hzn9yjo] (score 5, diepte 4) Any specific brand?
[hznealn] (score 5, diepte 4) My mom wanted to resupply me with new socks recently. Accidentally bought thigh-high black compression socks. Best mistake she ever made. Comfy as all hell.
[hzn4pt9] (score 5, diepte 3) Keeping to go cup with a straw by pos always helped me remember to drink more. Important to stretch while you’re muscles are still warm if you can, but I get it. Even if you’re exhausted, lay on your back near a wall, scooch up til your butts right against it and put your feet straight up it at a 90 degree angle. You feel the blood flow back up your legs. Gotta second compression socks and better shoes too.
[hzmttia] (score 5, diepte 0) Theragun, deep tissue massages.
[hzn2sa5] (score 5, diepte 1 OP) I'm definitely working on that haha.
[hznszej] (score 4, diepte 3) Compression socks, elevation and stretching after work have changed my life.
[hzmsa34] (score 4, diepte 2) Honestly Crocs for work are pretty great. Put insoles in them for more support
[hznerfp] (score 4, diepte 2) Check out Vans Made for Makers! Great support, non-slip, and you can still kickflip.
[hznlwki] (score 4, diepte 3 OP) I so badly want to feel like a person after work.
[hznefn4] (score 4, diepte 1) Seconding Theragun. I borrowed one from a coworker after a 12 hour wedding and it was life changing. I wish I would've known they had it halfway through instead of waiting until the very end!
[hzmyaxe] (score 4, diepte 2) My bf and I LOVE her!!! We do one of her videos every other day, and I'm always jusssssttttt the right amount of sore after. I do have bad knees and need a modified warrior pose myself, though, so I understand doing ddp.

I also use CBD creams and hot ass baths. They work wonders!
[hzn2j7g] (score 4, diepte 1 OP) ELBOWS! Thank you! I just recently started getting the elbow and forearm pain and I have no idea what to do about it. I'll look into this. I'm currently searching for new shoes. I have been a skate shoe girl all my life. I thought the Vans Pro Cush were heaven on earth when they came out, but I'm going to bite the bullet and try some different things out this year. I quit drinking last year, and I think I started to notice the toll that bartending was taking on my body because I'm not numbing the pain with alcohol anymore.
[hznjl40] (score 4, diepte 2) I presume it was a stress response to being on my feet for 12-16 hours.  I’m no physicist or engineer, but it makes sense to broaden or elongate the base to support a tall/weighty structure.
[hzmstag] (score 4, diepte 0) Sensory deprivation tank!!!
[hzmz9vb] (score 4, diepte 0) Shots
[hznegg6] (score 3, diepte 8) This thread is laced with puns
[hzpep2c] (score 3, diepte 3) 100%!!! I have good nonslip shoes with Dr Scholl inserts in them for support as well as compression socks and what a game changer those were!!!
[hzn1ovu] (score 3, diepte 3 OP) One of my co-bartenders who is about 15 years older than I am recommended Hoka running shoes to me last night. She said they're the most comfortable shoes she has ever worn for work. I have been looking at them online today, but there are so many different shoe models! Can you tell me what model you have? She has the Bondi model, but the sole on those things almost looks like a platform. The Clifton model has less of a noticeable sole. Just wondering if you have a recommendation between the two.
[hzn29so] (score 3, diepte 4) I don’t run anymore because I had bad knees from wrestling and hockey growing up and since have been in a bad car accident. However, the Hokas are the few pairs I can wear with little pain after a long day at the bar. I have both the Clifton and the Bondi, the sole looks thick but your foot sits inside of it kind of because the sole comes past the footbed. The Bondi are a little softer but the Clifton are more responsive and they feel better after a long day imo because you need a little more firmness.
[hzncr73] (score 3, diepte 4) I have the Clifton, great shoe! The sales associate at running room said they’re good for all-purpose, not just running which is why I like them.
[hzn7bbh] (score 3, diepte 2) Jesus how are your knees not destroyed? Get a good pair of water resistant sneakers, maybe with some gel inserts. My feet get tired, but no longer achey from wearing my shoes. Also for forearms, doing strength training will help with that, my arms hurt way less once i started consistently doing pullups every day. For your back, the shoes will help but make sure you aren't slouching when you're on your well making drinks, I know I used to have a bad habit of doing that
[hznl1m1] (score 3, diepte 3 OP) Say word?! 
I still can’t kickflip for shit. I never said I was GOOD at skateboarding lol
[hzneybd] (score 3, diepte 2) Honestly? Boots. Doc Martens, Solovair, Red Wings - you want ankle support, a comfortable sole, and potentially a custom orthotic insert. Something durable, too. I love my solovairs, personally. Durable as hell and I don't have any leg or back pain anymore. They don't come cheap, but still feeling like a person after work is worth it.
[hznhs2e] (score 3, diepte 2) Hedley and Bennett sk8 hi. If they’re in stock that is.
[hzn2dz2] (score 3, diepte 1) Very much this. My mom got me some timberland work shoes (steel toe, non-slip, arch support), and they have been a game changer. My feet feel supported af and my legs don't hurt nearly as much after a double.
[hzn4gfv] (score 3, diepte 4) Try to find ones without to much sugar. I like Nuun Sport , they make them with caffeine to but caffeine makes you dehydrated as well. 

Also if you are a coffee drinker try to drink 16oz of water first thing when you wake up.
[hzndpzl] (score 3, diepte 4) I'm not even joking, Pedialyte for the win. Secret bartender hangover cure
[hzng31i] (score 3, diepte 4) Liquid iv is helpful, but there is no substitute for a half gallon to gallon of water every day. I work a very busy bar and the managers will give us a quick minute or two for a hydration break as often as they can.
[hznndgi] (score 3, diepte 6) Our bartenders pull 1-2 manager shifts a week, our servers are mostly cross trained on the bar, and our two salaried managers are former bartenders. We are in a uniquely cool position
[hzn1xot] (score 3, diepte 2 OP) We are so high-volume right now, I can barely move when I get home lol. But I have been stretching the morning after.
[hzms7u5] (score 3, diepte 0) General decent diet, water, exercise, yadda yadda. 

I've been taking 50mg of CBD daily and I like a good Epson salt foot bath after work every night. I
[hzn2jsj] (score 3, diepte 2 OP) Thanks for this!
[hzmveu4] (score 3, diepte 1) these are fun but more for your mind than your achy body
[hznfw6w] (score 3, diepte 1) I find myself laying down for about 2 hours after I wake up every day and I'm very thankful for the luxury of a nice mattress and topper. 16 year veteran here.
[hzoz5e4] (score 3, diepte 2) For sure.  There’s only so many preventative measures we can take.  But in the end, there’s nothing better for the body than to get off your feet for 48 hours and not have your hands get toasted by sani water.  Read a book, play some video games, knit a scarf whatever.  Does wonders for the soul and body.
[hzn2vss] (score 3, diepte 1 OP) Definitely wanting to get into some more yoga stuff, and I wasn't aware that Birks made a non-sandal, so I'll check those out. Thanks!
[hzmzxal] (score 3, diepte 0) I have a friend with a hot tub, I also soak my feet.in warm Epsom salt baths. It gets better.
[hzn3oqo] (score 3, diepte 1 OP) The feets killllllllll. I'll start soakin'.
[hzn284b] (score 3, diepte 0) I saw a couple people mention shoes and it's 100% worth it. I spend like $100 on shoes a year and it's more than worth it. Buy good shoes and they will help you feel better and also last longer. Also I always have icyhot on me. I know that's more like putting a bandaid on  severed limb but in the moment it helps so much and on the toughest nights it'll get you though close. Oh and cocaine will also make you forget you were ever in pain.
[hzn6qez] (score 3, diepte 1 OP) I think I'm gonna get some new shoes with some of the suggestions on here. I quit the drinkin' and the cokin', which is why I probably feel all of these aches and pains now. Now its just achy body that keeps me glued to my bed instead of achy body AND crippling cocaine hangover anxiety lol.
[hzn758h] (score 3, diepte 1 OP) This better shoes suggestion from all the lifers on here got me shopping. Thanks for the suggestions!
(159 reacties met lagere score weggelaten)

=== THREAD p8xddt ===
SUBREDDIT: r/Target
DATUM: 2021-08-21  SCORE: 158  REACTIES: 201
TITEL: how do i get my feet to stop hurting?
POST (source_id=post):
i’m a new team member, and they’ve been training me mainly in fulfillment. i’m currently on my lunch break and my feet hurt so bad it hurts to walk. i’m probably gonna buy insoles once my shift ends, but do you guys have any tips?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[h9tkry6] (score 191, diepte 0) insoles and better shoes will make a different, once you get used to walking a lot more often it isn’t bad
[h9tqt96] (score 33, diepte 0) New balances baby!
[h9tpasy] (score 32, diepte 1 OP) gotcha, ty!
[h9u5psb] (score 31, diepte 2) Yeah I had to switch shoes. I take an average of 25k steps a day. Support is what you need.
[h9tnfjo] (score 26, diepte 0) You need insoles for your kind of feet (I have to use both the massaging work insoles and the arch supports) as well as some lightweight breathable sneakers. Get them as cheap as possible because they will have holes in a few months and need replacing. It also helps to chug water on your breaks, make sure to take all of them, and SIT DOWN! Do not walk or stand on breaks if you can help it. I often have to take a hot Epsom salt bath after some fulfillment shifts to help my leg and feet muscles. I usually get the cheap giant unscented bag from the pharmacy section. Feel better, you got this!
[h9u8mh1] (score 24, diepte 2) Taking Ibuprofen repeatedly over time is terrible for your liver. Get better shoes and socks and wait for your leg musculature to catch up.
[h9u9si2] (score 23, diepte 2) I highly recommend Brooks, they'll run you a bit but you can find them at any Dicks. Find a pair that fit you, try a few different ones on before you buy. Mine ran me about 130 and I've had them for 6 months, my foot pain stopped almost immediately after I started wearing them regularly. No more numb feet at the end of the day.
[h9tsrar] (score 17, diepte 0) Try nice in soles... Use that employee discount !!!

If that dont do it, u need upgrade to real nice walking shoes, like the type postal workers use...

First solution us sub 100$, the latter, you looking at like 200ish. But its your feet, bro. Thats like priceless.
[h9tmlej] (score 16, diepte 0) Better shoes I’m in Starbucks and we are constantly moving new balance and under armor have good shoes that have good support my old shoes would cause my feet to feel like they are being crushed but since I started wearing both brands my feet don’t hurt as bad very little pain
[h9txmoc] (score 15, diepte 0) Shoes make a huge difference! Go to a shoe store and let the worker know that you’re basically running your entire shift. Be prepared to spend a significant amount on shoes. Hoka are *amazing,* I have tendinitis and it’s helped alleviate the pain a lot.
[h9tscox] (score 14, diepte 0) Take some ibuprofen shortly before your shift starts.
[h9umaet] (score 13, diepte 3) I literally work at dicks now doing fufillment and i highly recommend New Balance 990v5. They are great for people with wide feet. Brooks are good too. But 990v5 is the best.
[h9ucox5] (score 12, diepte 1) We used to have a girl in fulfillment who wore crocs. It wasn’t allowed and no one ever got on her for it but I don’t know how she did it.
[h9uesu6] (score 10, diepte 2) to be fair crocs are really comfortable but idk if they’ll still be comfortable after 20k steps
[h9tuvii] (score 10, diepte 0) You can't wear old shoes - or ones that don't give adequate support and cushion.   Search on this site and you will find multiple posts about this with many many suggestions.  What works for one person's feet will not necessarily work for another.
[h9tpdkv] (score 8, diepte 1 OP) tysm <3
[h9tqzf5] (score 8, diepte 1 OP) ty!
[h9u0bp6] (score 8, diepte 1 OP) just bought some!
[h9trly4] (score 7, diepte 2) I would avoid converse. They typically don’t have a thick insole. Doesn’t provide good support. However you could do a lot worse. New balances are probably the most comfy shoes I’ve ever had. If you get insoles for the converse they might be good because the rest of the shoe is good for support.
[h9tv2cc] (score 7, diepte 0) I think the 2 biggest things will be the shoes and/or soles and just getting used to the walking.

When I started I felt the same way but that was also because I was using 2 year old sneakers I had worn daily. 

I would also ask your fulfillment coworkers what they recommend since different people will recommend different things.
[h9ub2s6] (score 6, diepte 2) I also discovered I have flat feet through working here at Target and dealt with indescribable foot pain after every shift. Had to get some special shoes and it totally fixed it.
[h9tpc55] (score 6, diepte 1 OP) oh wow, thanks for the help!
[h9tt1e0] (score 5, diepte 0) A lot of us Inbound members use Adidas NMDs. Super comfortable!
[h9tu0f0] (score 5, diepte 0) ultra boost done me justice with drive ups, also its just a matter of time before your feet get used to it
[h9tqozf] (score 4, diepte 0) Don't underestimate a good pair of work boots and insoles! My Wolverine Raiders saved my feet
[h9ut29l] (score 4, diepte 3) This, as well as your stomach and kidneys.
I say this as someone who got yelled at by my doctor for regularly taking 800mg advil AND 1000mg tylenol.
[h9u0kan] (score 4, diepte 1 OP) whoops😭😭 i’m gonna buy new shoes when i get my paycheck :)
[h9twjaf] (score 4, diepte 0) This might be strange, but until I started working at Target, I never knew I had wide feet and that I should be wearing wide fit shoes. You could double check that. After about a week of intense foot pain I went to get new shoes after insoles didn't work/help and tried on a pair wide fit shoe. Never had foot pain again. But I'm not sure if it would help at all. 

To those who may ask why I never knew I had wide feet, I've never had such an intense job where I had to be on my feet all day like that.
[h9wwfgs] (score 3, diepte 4) I have high arches and foot pain in my heels/back pain. Puma has been a great brand and I was hooked after one pair. Bonus: they grip the tile pretty well too for tight turns.
[h9v0v2b] (score 3, diepte 2) And alternate shoes when you can.
[h9wzreb] (score 3, diepte 3) This is the real pro tip, I have my comfy "break" shoes that I wear every couple days. It's wild the difference it makes.
[h9ucs8x] (score 3, diepte 2) Man oh man, you just aren’t looking hard enough for good NB’s. Caught a LOT of traction in the fashion world so mixing them in as a comfortable shoe will get you some looks while you’re saving you tootsies ;)
[h9u0hw6] (score 3, diepte 1 OP) gotcha! ty :3
[h9ua4ra] (score 3, diepte 2) Yep - shoes that are perfectly fine to wear casually are just not good enough to be walking 9-10 miles in.  The stability and support and cushioning just wear out.  Expect to have to replace them much quicker than you have ever had to in your life.
[h9tyohn] (score 3, diepte 1 OP) my shift just ended, gonna go buy some rn😮‍💨😮‍💨
[h9tz095] (score 3, diepte 0) converse/vans are a strong no from me for work shoes. new balance and sketchers are good options. docs sells work shoes that could be okay, but kind of unnecessarily expensive for the job we do imo, but saying that, my boyfriend has steel toes from them for his outdoor job and he loves them.
[h9u4698] (score 3, diepte 0) Insoles for plantar fasciitis. Look into it. It’s a common condition for those that stand on their feet all day.
[h9u4ziw] (score 3, diepte 0) I have Nike air max and then insoles in them. Feel like I'm on a cloud and they look nice
[h9u7gi3] (score 3, diepte 0) Compression socks were a big help for me and helped to prevent sore feet at the end of the day.
[h9x2mc3] (score 3, diepte 0) My GF used to get the crap Walmart shoes and was always complaining about her feet. Took her to Dicks and said get shoes that are good for walking and all day comfortable. She finally settled on some Brooks. They were around $120 I think,  but foot health and comfort are worth it.  She absolutely loves them, and regrets not getting them sooner.  She works ship from store and is on her feet all day running around Target. 
Tip:  when shoe shopping, go near the end of the day, after you have been on feet all day, your feet swell up,  so if you go near the end of day,  you'll get shoes that fit better.
[h9xaiwc] (score 2, diepte 3) Brooks Ghost seem to have the best cushion, also if you have a running store close by the Hoka Bondi 6 or 7 is a great shoe, I have foot issues and they work great for me. Your feet will get more used to the walking but it does take a couple weeks. I take Naprosyn prior to working also it keeps the inflammation down.
[h9viujr] (score 2, diepte 4) I got mine [here.](https://www.orthofeet.com/products/lava-athletic-shoe)
[h9xhz40] (score 2, diepte 6) Sorry, I definitely sent a link to the specific shoe I got for some reason. But they definitely have different sizes. Not sure about kids though.
[h9tqyvs] (score 2, diepte 1 OP) awesome, tysm!!! i was gonna get converse and maybe a pair of docs (that were already worn in), are those good choices?
[h9tr85t] (score 2, diepte 2) I wore converse for a really long time, but once I was on my feet 8+ hours a day I found they didn't support me enough even with insoles. I think Docs are a great choice! I feel like boots have worked best for me out of all the different types of shoes I've tried over the years.
[h9trgeu] (score 2, diepte 3 OP) oh wow, awesome!! i’m so glad that gives me a reason to buy the docs i want :”))
[h9u53h4] (score 2, diepte 2) I wear a pair of timberland boots everyday and I love them. I know people who wear docs, but I find them too be too heavy to wear walking around all day. And if you go converse get insoles
[h9tt4kt] (score 2, diepte 0) new balance shoes and insoles
[h9tyr6k] (score 2, diepte 1 OP) i have very narrow feet😭😭
[h9two0w] (score 2, diepte 0) I wear RedWing Moc toe boots, there are no contenders in quality and comfort. After you break them in of course lol
[h9tyq58] (score 2, diepte 1 OP) gotcha!!
[h9tz2ci] (score 2, diepte 2) Ill warn you they aren’t cheap lol, but Ive had mine for about 5 out of my 6 years at target. Not many shoes can last that long in retail 👀
[h9type6] (score 2, diepte 1 OP) tysm!
[h9u4su1] (score 2, diepte 3 OP) will do <3
[h9ufrah] (score 2, diepte 1) what brand?
[h9tyqxp] (score 2, diepte 0) As someone that has gone through that (formerly Fullfillment 2 yrs), get good running shoes, or get those cheap insoles (if your store has a pharmacy). They are a couple of bucks. People say get walking shoes, but face it -- you are nearly running the entire shift. Luckily, Target has cheap running shoes.... I've used those for a very long time. What ever you do, get something that pampers your feet.
[h9tyst9] (score 2, diepte 1 OP) my shift just ended, i’m gonna go buy some!
[h9u0r6t] (score 2, diepte 0) As a cart attendant you can buy pads for your shoes that you put inside but after about a month your feet will stop hurting
[h9u1ewu] (score 2, diepte 0) Working on concrete floors all day means as others have said means you NEED good shoes. I'd avoid going the cheap shoe route, you'd be better off in the long run investing in the good ones, less pain and hassle.
[h9x1rm5] (score 2, diepte 1) I just bit the bullet and got KEEN work shoes with a steel toes. Yes they are heavy, but they are designed for warehouse workers who are running all over concrete floors all day. I got the tip in this sub and they have been great.
[h9u1ozk] (score 2, diepte 0) In addition to good shoes/insoles, and/or until you can get them and while your feet get used to new shoes…

-Fill a water bottle about 3/4 full and freeze. Roll your feet on it after your shift to help with inflammation.

-Stretch your feet, especially before and after breaks and first thing in the morning.
[h9zxzze] (score 2, diepte 1 OP) awesome!
[h9u74zi] (score 2, diepte 0) Soak in an Epsom salts bath when you get off. It helps tremoundsly. And lace your new shoes up tighter. I realized that was one of my issues.
[h9u98bd] (score 2, diepte 0) For some people a good pair of compression socks helps too.
[h9uxasl] (score 2, diepte 1) If you'd like to pick orders, then that position would be Fulfillment Expert. It's the same duties every day where you pick orders and either bag them for order pickup or box them up for shipping out. Every store is different as far as other responsibilities but at my store we aren't expected to be register trained and the only time we deviate from fulfillment is when order pickup is slow and we help the general merchandise team with stocking.
[h9uc8c9] (score 2, diepte 0) Nice shoes are a MUST. I bought a pair of Gel Kayanos from Asic's website when they did their semi-annual sale. $160 shoes for $99. Between them and the Nimbus, it's all I wear. Highly recommended. Good luck!
[h9v2r23] (score 2, diepte 1) Seconding Asics, they're the only shoes I wear for work. I also wear Bombas socks with them but any compression socks will be helpful. I bought the foot roller we sell with the nibs on it and keep in the freezer and I love to roll my feet and then put them on a hot rice bag.
[h9ugxay] (score 2, diepte 0) Get promoted to Team Lead. Then you can sit and watch numbers on your computer.
[h9zeowi] (score 2, diepte 1) Ha team lead of what cuz I never get to sit down.
[h9uhacm] (score 2, diepte 0) You gotta get used to walking. I struggled when I started last season, my feet hurt at the end of every shift and I was in pain during breaks. Insoles barely did anything and most of the shoes I tried would be comfortable for the first few hours but couldn't hold up for the entire shift. But it wasn't that I was buying bad shoes, it was a problem that I went from being fairly sedentary to walking 9+ miles every day, five days a week.

Walking takes a certain amount of fitness to be able to do it for hours on end, even if it's low impact. You're gonna have to push through the discomfort for the first month or so until your body gets used to it. Your feet won't be nearly so sore after you've gotten used to the work load. Trust me, I was there where you are now, and all I wanted to do was prep or pack in the back because I thought I was gonna fall over and die while picking on the floor. But then one day, the pain disappeared and my fitness improved and now I no longer have issues feeling sore or pained while walking all day.

I wear [sketchers](https://www.target.com/p/women-s-s-sport-by-skechers-rummie-apparel-sneakers/-/A-54421708?preselect=54349336#lnk=sametab) usually during my shifts, the ones that can stretch so that my feet have space to expand as they become swollen throughout the day.
[h9utk9g] (score 2, diepte 0) Overtime your feet will get used to it. My feet and knees used to ache so much at first but now I’m fine
[h9uu0v0] (score 2, diepte 0) As someone who has run cross country and as a former team leader of flow/backroom/fulfillment I would suggest better shoes.   A lot of this comes down to what your feet actually are.  High arch etc etc.   new shoes will be one step of this but if your feet hurt or your knees it’s more likely your diet.   
Try eating a banana or 2 a day.  The potassium should help.  Or a multi vitamin.   Your feet hurting is generally from bruising but your body has no functionality to heal from these issues.   

If your buying an insole for your shoe your just putting a bandaid on the original issue.   Shoes have a life expectancy just like any other product and you get what you pay for in many aspects of this.   

If you want to dm directly for actual advice on this (explaining all what if’s is difficult) I can make a legit recommendation that will end up saving you money

But new balance and the other brands are just that.  Brands.  And if you know your shoe.  And your personal style then you can make the best adjustment with just that.  

A new shoe won’t always fix the issue.  But it can help alleviate it at best
[h9uu5tk] (score 2, diepte 0) I worked in a cafe when I got pregnant. I went and spent 100$ on New Balance shoes with insoles. Those things lasted five years between the cafe and Target. Highly recommend it.
[h9uvaoc] (score 2, diepte 0) Don’t wear vans, I highly recommend adidas ultra boost or Nike reacts
[h9uyg6h] (score 2, diepte 0) maybe try compression socks? i don't know if they'll help your feet, but i've noticed my legs in general don't feel as sore when i wear them.
[h9v1c6l] (score 2, diepte 0) I have different tip:

Stretch those feet out at night. Get something like a pencil, sit down at the couch, and curl your toes to pick it up. That one little stretch helps me a ton. There are others, look em up if you want more, but that plus always staying hydrated will help you recover faster.
[h9zxwby] (score 2, diepte 1 OP) will do!
[h9v34o2] (score 2, diepte 0) I tried all of the insoles, but I seriously think your feet just need time to adjust.  I wear Nike Airs, sketchers, and New Balance.  Just be ready to buy new shoes every 3-6 months.  Ya gonna wear them out fast.
[h9v384p] (score 2, diepte 0) Make sure you stretch before bed.
[h9v4ur8] (score 2, diepte 0) Did you have a sedentary job before? You have to acclinate to being on your feet more. I work in IT and recently had to do some work in one of distro centers for a month. Lots of standing and walking. The first week sucked my ass, but by week 3 is was general tiredness. Also, make sure your shoes fit right.
(121 reacties met lagere score weggelaten)

