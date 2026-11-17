# Label-batch batch_0062

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
Schrijf het resultaat naar `batch_0062.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1vrqm6w, ttxsct, 13y6n17).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1vrqm6w ===
SUBREDDIT: r/Warehouseworkers
DATUM: 2026-08-18  SCORE: 2  REACTIES: 0
TITEL: Catch up on what happened this week in Logistics: August 11-17
POST (source_id=post):
Hey everyone,

If it's your first time reading one of my posts, my name is Menachem, and I have a weekly newsletter called Logistic Pulse that breaks down the top logistics news from the past week. We're currently on week 59!

I've added a section called 'job board' with a link to over 700 warehouse jobs available in the US. Go check it out. 

Let's jump into it,

# Somebody paid $3.78 million to skip the line in Panama

Daily auctions for August transit slots through the Panama Canal's Panamax locks have averaged about $1.1 million, more than sixteen times what the same slots went for a year ago. Auctions for the larger Neopanamax locks are averaging around $2.5 million, the highest on record, with individual slots since late July hitting $3.78 million.

Two things are squeezing at once, and they're unrelated.

The first is water. The canal runs its locks on fresh water from Gatun Lake, which is currently below its long-run average, and Argus expects it to keep dropping. A strengthening El Niño tends to bring drought to Central America, and the Panama Canal Authority has already imposed three draft restrictions on the Panamax locks in the past month, with the permitted draft scheduled to fall to 47.5 feet by September 3, down from the usual 50. Fewer drafts mean less cargo per vessel and a longer queue behind it. On August 3, 113 ships were waiting for a transit slot. On January 2, there were 40.

The second is oil. The Strait of Hormuz has been disrupted since the U.S. and Israel-led bombardment of Iran began on February 28. That waterway normally carries about a fifth of global oil flows, so Asian buyers have been sourcing crude and refined products from the U.S. Gulf Coast instead, and the shortest way from the Gulf Coast to Asia runs through Panama. Energy cargo is now competing for the same slots as everything else.

Most large carriers book transit slots well in advance at fixed rates that bear no resemblance to these numbers, and only up to 30% of canal traffic goes through the daily auction. The Panama Canal Authority has characterized the million-dollar payments as temporary market fluctuations rather than a general fee increase. So the auction figure isn't a bill anyone's container is paying. It's a read on how badly some operators need to move right now, and it's the same signal that preceded the 2023 restrictions.

**What this means for you:** If you have clients importing to East Coast or Gulf ports on all-water services, this is the week to ask their forwarders about canal surcharges and transit buffers rather than the week the surcharge shows up. Draft restrictions cut container capacity per sailing, and that shortfall gets recovered somewhere on the invoice. The thing to watch is which pressure eases first, because a drought story resolves when it rains and an oil-routing story doesn't. If your inventory planning assumes normal all-water transit times into the fall, build in slack now and be honest with brands about it before they commit to a promo calendar.

# Presented by FulfillYN

[FulfillYN](https://fulfillyn.com/) is an independent 3PL matchmaking consultancy. We pair growing retail and e-commerce brands with fulfillment partners who actually fit, from a vetted network of 439 warehouses. We know which providers are built for your world and which will figure it out on your dime.

If you don’t want to waste 3 months sitting through sales calls, filling out forms, negotiating, this is the service for you.

Tell us what you ship, and we'll put you in front of 2-3 that genuinely fit.

[**Match with the perfect 3PL ➡️**](https://fulfillyn.com/get-matched)

# Fewer people are stealing your freight, and it's costing much more

Verisk CargoNet logged 677 supply chain theft incidents in Q2, down 26% from a year ago and 14% from Q1. Estimated losses over the same period went from $135.7 million to $304.6 million.

The average theft with a reported commodity value came in at $564,009, though CargoNet is upfront that a handful of extreme losses dragged that figure around. The plain reading is that much of the low-effort volume theft has dried up, while a smaller group has gotten much better at picking targets. Keith Lewis, who runs operations at CargoNet, put it as groups that aren't trying to steal more freight, just trying to identify the right shipment.

What they're picking is specific. Metal theft rose from 54 to 80 incidents, with copper still the favorite and aluminum, nickel, and tungsten climbing. Enterprise computer and networking equipment stayed a priority, along with crypto mining hardware, and CargoNet makes the point that matters for anyone touching this freight: these loads can be worth millions, and they move through the network as ordinary dry goods, with paperwork and a security profile that don't reflect what's inside. Meanwhile, beverage and grocery theft fell off sharply, auto parts and tires dropped, and seafood went up by eleven events, which is its own strange little trend.

The decline came mostly from two things going away. Fewer criminals are buying up legitimate motor carriers to book freight under a clean operating authority and then disappear with it, and there was less organized theft of unattended loaded trailers, especially in California, Texas, South Florida, and Dallas-Fort Worth. Straight theft events dropped from 488 to 378. Fictitious pickups barely moved, 165 down to 158.

Business email compromise is still the front door. One set of credentials gives someone shipment data, contact directories, and access to a TMS, enough to identify a valuable load, impersonate a party everyone already trusts, and reroute it while it looks completely normal to the broker, the carrier, and the receiver. If that sounds familiar, it's the same mechanic behind the Ceva intrusion we covered two weeks ago.

Now put Landstar next to that. On its July earnings call, VP and chief safety and operations officer Matt Miller disclosed that the company has cut its approved carrier pool from more than 100,000 in mid-2022 to roughly 64,600 today. That's a 35% reduction, over 35,000 carriers removed, and it dropped another 7% year-over-year in Q2 after a 19% cut in Q1. Overdrive reported that the effort began in response to cargo theft and freight fraud, with identity checks and tighter compliance measures layered on.

It ends up somewhere else. The Supreme Court's May decision in Montgomery v. Caribe Transport II broadened broker liability for carrier selection, and CFO Jim Todd said plainly that cases that used to be dismissed on federal preemption grounds must now be litigated. Landstar took $10.5 million in unfavorable prior-year claims adjustments in Q2, with three of the five responsible claims coming out of brokerage. CEO Frank Lonegro is asking federal regulators for clearer vetting standards, which is what a company says when it has spent four years building a process and would like everyone else held to the same one.

The market seems to be pricing it as an advantage. Landstar's insurance renewal on June 1 came in with auto liability flat and broker liability up about 3%, which is a soft outcome for a post-Montgomery renewal. Agent inquiries have picked up since the ruling landed, including an $18 million Midwest brokerage that signed on as an independent agent. And this is all happening in a tightening truckload market, with Lonegro describing capacity as having tightened significantly and conditions moving in favor of the provider for the first time since late 2022. Landstar's truck revenue rose 19% to $1.33 billion on 2% load growth, so essentially all of it came from rates.

**What this means for you:** If you broker, understand what the Landstar number implies: tens of thousands of carriers got dropped by one of the most established networks in the country, and they are calling somebody, and that somebody has a real chance of being you. On the theft side, the exposure isn't the yard; it's the inbox. BEC is now the access point for most sophisticated schemes, making carrier fraud an IT problem your ops team inherits. And if you handle metals, enterprise hardware, or anything with a fast resale market, the freight needs a security profile that matches its value rather than its BOL.

# Nobody ordered many more robots. They spent 21% more anyway

The Association for Advancing Automation put out its Q2 numbers, and the interesting part isn't the unit count.

North American companies ordered 8,940 robots in the second quarter, worth $622 million. Units were up 4.3% from a year ago. Order value was up 21.3%. Run that out, and the average robot ordered this quarter cost around $70,000, up from roughly $60,000 a year earlier. Buyers aren't adding volume so much as buying up the stack, integrating into bigger systems rather than adding another arm to the line.

The first half totaled 17,995 units and $1.166 billion, a 2% increase in units and 6.6% in value. Underneath that flat-looking topline, the customer base is shifting hard. Automotive OEM orders fell 25% in the first half, which historically would have dragged the whole market down. It didn't, because semiconductors and electronics ordered 35% more units, life sciences and pharma 32%, automotive components 24%, and food and consumer goods 17%. Non-automotive buyers were 56% of Q2 units. A3's Alex Shikany framed it as the market mix continuing to evolve, which is the polite version of saying Detroit stopped being the whole story.

Two caveats before you take that to a client meeting. A3 counts industrial robot orders across all of manufacturing, so this isn't a warehouse automation number, even though it’s reported as one. And these are orders, not installations, so they reflect decisions made a couple of quarters ago.

The piece that does translate is collaborative robots. Companies ordered 2,774 cobots in the first half, totaling $114 million, which accounts for 15.4% of all units but less than 10% of the dollars. That gap is the whole point. Cobots are the cheap, fast, low-infrastructure end of the market, and adoption is concentrated where the work is fiddly and high-mix: they were 43.7% of life sciences orders and 36.5% of semiconductor and electronics orders.

For context on the demand side, companies bought more than 36,700 robots last year, the most since 2022, and Interact Analysis found that 92% of surveyed companies plan to increase automation spending this year. GXO has invested close to a billion dollars in automating its buildings over the past five years. Amazon signed a warehouse automation supply agreement with AutoStore on undisclosed terms, which is notable mainly because Amazon builds most of its own robotics, and going outside for cube storage suggests it isn't trying to build everything twice.

**What this means for you:** The per-unit price is moving against you, so any automation quote you're sitting on has a shorter shelf life than you'd think, and a proposal you priced six months ago probably isn't the proposal you get today. If capex has been the reason you keep passing, cobots are the honest entry point rather than a compromise, and the industries adopting them fastest are the ones with messy, variable, high-mix work, which describes most multi-client fulfillment floors. And with 92% of companies planning to spend more, expect the automation question to move from a nice differentiator to a table-stakes item in RFPs.

# QUICK HITS

**U.S. retail sales came in at $763.6 billion in July, down 0.6% from June**[,](https://www.reuters.com/business/us-retail-sales-unexpectedly-fall-july-2026-08-14/) according to Commerce Department data, after June managed a 0.2% gain. The pullback is consistent with what warehouse operators have been describing all summer: retailers pulled inventory forward into May and June ahead of tariff deadlines and then went quiet. One soft month isn't a trend, but if your Q4 volume forecasts were built on spring order patterns, this is a reason to check them against what your clients are actually receiving right now.

**Teamsters California sued the state DMV on August 5 to block heavy-duty autonomous truck permits.** The 34-page complaint in Alameda County Superior Court asks the court to set aside the regulations the DMV adopted on April 28, which removed the ban on autonomous vehicles rated over 10,001 pounds. The legal argument is procedural rather than philosophical: the union says the DMV skipped a Standardized Regulatory Impact Assessment that state law requires for any rule with more than $50 million in first-year economic impact, and that it puts more than 200,000 California semi-truck driving jobs at risk. Peter Finn of Teamsters California framed the safety case around trucks up to sixteen times heavier than a robotaxi at highway speeds. The stakes are high because California matters to developers, as the state handles 40% of the nation's containerized imports and 30% of exports.

**Fura acquired High Rise Logistics, its seventh deal.** The Cincinnati broker is running a straightforward roll-up thesis: buy established books, move them onto a shared AI platform for bidding, carrier sales, and visibility, and skip the overhead stacking that usually kills these strategies. High Rise, out of Vancouver, Washington, brings flatbed, expedited, truckload, and LTL along with intermodal, drayage, and warehousing, plus a real Pacific Northwest footprint. Leadership stays on to run daily operations. Terms undisclosed. If you own a regional brokerage or an asset-light 3PL, this is the second consecutive week with the same buyer profile, and the pattern is consistent: they want your customers and your team, and they're bringing the technology.

# JOB BOARD

**Title: VP of Warehouse Operations**  
Company: Ardmore Home Design  
Location: Hacienda Heights, California, US  
Salary: $170,000 - $200,000  
[Apply Here](https://artha.link/@menachem-chayempour/jobs/vp-of-warehouse-operations-ardmore-home-design-hacienda-6aba9e82)

**Title: General Manager - Fulfillment**  
Company: iDrive Fulfillment  
Location: Phoenix, Arizona, US  
Salary: $90,000 - $120,000  
[Apply Here](https://artha.link/@menachem-chayempour/jobs/general-manager-fulfillment-idrive-fulfillment-phoenix-97e208e5)

**Title: Refrigerated Warehouse Operations Manager**  
Company: The Judge Group  
Location: Dallas, Texas, US  
Salary: $90,000 - $115,000  
[Apply Here](https://artha.link/@menachem-chayempour/jobs/refrigerated-warehouse-operations-the-judge-group-dallas-eeb661fc)

**Title: Fulfillment Operations Manager**  
Company: Fringe Sport  
Location: Austin, Texas, US  
Salary: $80,000 - $85,000  
[Apply Here](https://artha.link/@menachem-chayempour/jobs/fulfillment-operations-manager-fringe-sport-austin-75382ce4)

**Title: Warehouse Manager**  
Company: RYSE Up Sports Nutrition  
Location: Prosper, Texas, US  
Salary: $75K-85K  
[Apply Now](https://artha.link/@menachem-chayempour/jobs/warehouse-manager-ryse-up-sports-prosper-5f5b2c18)

**Title: Senior Supply Chain Coordinator**  
Company: HR Annie Consulting  
Location: Portland, Oregon, US  
Salary: $70,000 - $80,000  
[Apply Here](https://artha.link/@menachem-chayempour/jobs/senior-supply-chain-coordinator-hr-annie-consulting-portland-4fb94698)

**Title: Assistant Fulfillment Operations Manager**  
Company: Fulco Fulfillment  
Location: Dover, New Jersey, US  
Salary: $55,000 - $70,000  
[Apply Here](https://artha.link/@menachem-chayempour/jobs/assistant-fulfillment-operations-manager-fulco-fulfillment-dover-72b17000)

[Full list of job openings →](https://artha.link/@menachem-chayempour)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

That's all for this week. If you found this useful, [consider subscribing.](http://logisticpulse.com/)  
(Your data will not be shared. Subscribers' data is strictly for sending out the weekly newsletter.)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

=== THREAD ttxsct ===
SUBREDDIT: r/Construction
DATUM: 2022-04-01  SCORE: 162  REACTIES: 342
TITEL: my feet are dead. how do i stop them from sweating in my work boots?? does it go away after a while??
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[i30k21w] (score 497, diepte 0) Invest in better socks that are designed for hot weather.
[i30lf3l] (score 183, diepte 0) Some people sweat too much to get away with wearing boots like that. Those are fine boots, but apparently not for your feet. You sound like youre brand new, coupled with the weed socks and the despair in your title, i had a chuckle.
[i31711c] (score 176, diepte 1) yeah cotton socks will kill your feet

a thin wool blend sounds like it will be hot but they stay dry
[i30thkw] (score 76, diepte 0) People here keep saying “better socks” without any real recommendations. Get some Darn Tough or Smartwool socks. Preferably the 100% merino wool ones they breathe the best.
[i313tzi] (score 70, diepte 1) Yeah but how will people know im a pothead beside my red eyes and the fact that i smell like pot

Edit: in all seriousness tho my feet sweat in all weather. Even extreme cold, which is how i got frostbite the first time. What the doctor told me was that it is very important to keep your socks AND your feet clean. And change them shits at lunch if you sweat a lot.
[i31ex3x] (score 56, diepte 2) I wear rag wool over wick dry liners year round.... massive step up from cotton.

If its really hot, wet, or cold out, I'll change socks at lunch or breaks, immediate improvement.
[i30s2c2] (score 41, diepte 0) Try a pair of grownup socks
[i30k26c] (score 39, diepte 0) My feet a bad too,  get a boot dryer.  It helps keep your boots and bacteria doesn’t really build up in there if you use it every day.  Always get another pair of good boots and switch em out every other day.  You will extend the lifetime of your boots.
[i31ved2] (score 34, diepte 2) Darn tough brand is the way. I wear them year round! Also jam the compressed air shooter into your  boot while they are still on, give it a 5 second blast. It feels amazing in the summer!
[i30kqiz] (score 32, diepte 0) Like others have said, better boots, better socks. Maybe powder your shoes with baking soda as well.
[i30niep] (score 31, diepte 0) Moisture wicking socks.  I wouldn't wear novelty socks like you do for sure.
[i32jo6m] (score 30, diepte 4) Boots seem to last twice as long this way too☺️
[i30qb5g] (score 30, diepte 1) I'm one of these people, I sort of solved it by having foot powder and extra socks. I literally do an entire load of socks alone.
[i323gjs] (score 28, diepte 4) Trim your toenails
[i325lyw] (score 26, diepte 3) Yes changing your socks or (if you’re rich) having a second set of boots is a game changer
[i30w8tm] (score 25, diepte 1) +1 for darn tough. Seems ridiculous the first time you spend $25 on a pair of socks. But they last way longer than other merino socks and have a lifetime warranty. I bought some before 9 days hunting in the backcountry last year. I wore 2 pairs for the entire trip and my feet never really got gross. It was fucking bizarre. 6 months later and the few pair I bought all seem brand new still.
[i30ztq3] (score 22, diepte 3) Lieutenant Dan approves this message
[i314re0] (score 21, diepte 2) Sprinkle Gold Bonds blue on them shits at lunch too.
[i31kqzi] (score 19, diepte 2) This, the dickies work socks at Walmart come in a pack of 5 for every day of the week and they haven’t failed me in almost 5 months
[i30whmt] (score 19, diepte 0) The Spencer’s marijuana socks aren’t gonna cut it for ya
[i30zgca] (score 18, diepte 2) Extra socks are the way. Change at lunch to prevent trench foot
[i30vsx8] (score 16, diepte 1) Are you saying if I bought 2 boots with each having a 2 year expectancy, I’d get more than 4 years out of them?
[i31377l] (score 16, diepte 2) Yes, especially if you sweat a lot or use them in a wet environment. I even switch boots and socks at lunch if my feet are damp. If you do this your shoes will essentially last forever since it’s the abuse, not the use, that wears out shoes.
[i31ev1d] (score 14, diepte 2) I hated getting socks at birthdays and Xmas. As a grown man in Construction, I fucking love getting fresh socks as gifts now.
[i30sh6u] (score 12, diepte 1) Yeah fuck novelty socks. You need to go either REI or look at Underarmour. Go for hiking socks and you should be fine. If you have sweaty feet, you're gonna need foot powder.
[i320a70] (score 10, diepte 2) Thin merino if you can. 

Also, get another pair of boots and two sets of cedar shoe trees to keep in the boots when you aren’t wearing. 

Alternate boots. 

Boots last way longer, feet are happier.
[i31crnz] (score 9, diepte 3) Don't forget to do your balls as well so they don't stick
[i31bzwn] (score 9, diepte 2) And they make a few with vents near the sole. 

Yeah, I know, some people like waterproof, but have you ever had water fill up a waterproof boot? What happens then? Little bathtubs of misery is what happens.
[i310jiu] (score 9, diepte 2) Yea I sweat wearing socks in the house it sucks. But I got a boot dryer from Sportsman's and it has changed my life. Starting out with dry boots that don't smell has made my life so much better.
[i30ms4b] (score 9, diepte 0) Your boots are not breathable, make this a priority for your next pair
[i30rvoj] (score 9, diepte 0) Change socks at lunch. Buy a boot dryer.
[i30u05o] (score 9, diepte 0) Nice socks do they come in men's?
[i31lj2k] (score 8, diepte 3) Idk what I did wrong but I def had toe holes by 5 months with the Dickies. Shame too because they were pretty damn comfy.
[i32am9q] (score 8, diepte 3) Hell yeah, I wear darn tough and dickies. Love the darn tough they are my favorite!
[i31dhfa] (score 8, diepte 1) >Invest in better socks that are designed for hot weather.

Invest in better socks that won't work against you in a workers comp claim
[i30lofd] (score 8, diepte 0) I’m a sweaty dude and welded in hot temps all the time. Get some good wool socks made for hot weather they wick the moisture away
[i30xrn2] (score 8, diepte 2) Darn Tough on trail for 3 days straight hiking up a mountain with 30lbs on my back and I had the same experience. They're great.
[i3147ns] (score 8, diepte 2) Add another vote for those two brands. I am partial
to smartwool but I also own a few pairs of darn tough as well. My last pair of darn toughs got me through my last 5 years in the army and my first year of retirement. I have since thrown them away but 6 years from a pair of socks…… let’s see Walmart socks try to do that. Lots of miles. Usually work at least once a week.
[i316ajm] (score 8, diepte 0) Carharrt isn't in the business of boots get red wings or ariat bruh
[i32ewtp] (score 7, diepte 3) And the thin (polypropylene) socks over skin, with the thicker (wool) sock over them, will reduce blisters - because the abrasion happens between the socks.
[i32zn4h] (score 7, diepte 4) That’s the beautiful thing about darn toughs… they will replace them for no charge.. forever. I have about 6 pairs or so and I have had a handful replaced over the years. I definitely get more than 3 months out of them though… moisturize your feet or take the sandpaper out of your boots?
[i31dq79] (score 7, diepte 3) Avoid trench foot. Took me ten damn years to beat mine.
[i30t3pu] (score 7, diepte 0) To be honest and this is gonna sound weird. Thicker socks with moisture wicking…. If I wear thin socks they get mushy and wet. Yesterday I tried thick winter socks and they didn’t get so bad.
[i31l4jz] (score 6, diepte 2) Darn tough
[i30xhwo] (score 6, diepte 2) Yeah I agree with this recommendation. The price seemed ridiculous til I started wearing them for hiking.Those socks are amazing.
[i30vbbs] (score 6, diepte 0) It seems like you’re new to this work. The boots you have are fine, I wouldn’t worry about replacing them until they wear out. Definitely wear better socks. Work socks designed to wick sweat and provide padding for your feet. Buy a boot dryer and dry the boots every night. Clean them once a week, even if it’s just a brush or wet cloth to keep the dirt and grime off of them. They’ll last longer and be more comfortable.
[i314fje] (score 5, diepte 1) The socks maketh the man.
[i31dk7d] (score 5, diepte 3) *squish squish squish*
[i31bmau] (score 5, diepte 2) Anything woolen is a good start...
[i31yc0e] (score 5, diepte 4) Clip your toenails more often
[i31l3ln] (score 5, diepte 2) But bro, my marijuanas. How will the chicks know i smoke if they cant see my sweaty stinky weeds socks?
[i30upt5] (score 5, diepte 1) This here... boot dryer every night
[i31zm9n] (score 5, diepte 2) And if you buy FOUR boots, you get 8 years. But 4 *PAIRS* of boots gets you 16 years. 

And... Wait for it... If you buy *SIX PAIRS* of boots, you have too much money and don't need them anymore.
[i31f0jt] (score 5, diepte 1) Costco had 100% merino wool socks available for sale several times a year. Like $12 for a 4 pack of em. That’s my recommendation
[i31w433] (score 5, diepte 0) Wool socks
[i318ota] (score 4, diepte 2) It’s that air flow the fabric helps with that
[i31lm2a] (score 4, diepte 1) I love in Central Florida,  hot and muggy all year long except for our 5 days of winter weather.  I've always gotten Dickies socks.  On the worse days they'll be soaked. Usually dry though after a normal days work.  Thick too so help with preventing blisters.  I also get the black ones,  they'll never look stained from dirt and mud.  

Everyone's feet are different,  of you have normally sweat feet,  is keep a second pair to change into every day at lunch.  Working with for injuries is horrible,  it'll put you on your butt. Keep your toes mostly dry.
[i30xq0m] (score 4, diepte 1) >Some people sweat too much to get away with wearing boots like that.

Some of us sweat like that and have no choice but to put up with it... 

My feet sweat bad in just about anything......like seriously the bottoms of my feet when wearing flip flops even....but the requirements for boots at my company don't give many options either.
[i30n5ow] (score 4, diepte 1) Don’t do this. Better to sweat than to keep all of those toxins in… it’s like blocking an exhaust on a car DO NOT do this for work. No one cares what you smell like but when you go home or out DO put some on
[i30y77c] (score 4, diepte 2) Basketball socks. They breath well but have strategic padding and good support. I like the brand Stance, performance line for work.
[i30tka7] (score 4, diepte 0) Buy expensive wool blend socks. They are worth it
[i315q2g] (score 3, diepte 1) But are you going to tell us the brands for better socks ?
[i334z0m] (score 3, diepte 5) I change them three times a day and they last three times as long!
[i31pq0b] (score 3, diepte 2) Dickies "stays where you put them, industrial strength, heavy duty comfort, extra thick, sweat busting work socks"
[i32wm3f] (score 3, diepte 3) Not sure what I'm doing wrong, but the few pairs of darn toughs I got lasted only 2-3 months before developing holes in the heel or at the pads of my foot
[i316rmx] (score 3, diepte 1) Also, putting boots in the freezer for 24 hours will kill some bacteria. Not all, but it helps the smell
[i32q02u] (score 3, diepte 1) To add on to this, if you cannot afford a boot dryer you can leave them upside down over an air vent and it will work much the same.
[i30k5od] (score 3, diepte 0) You get better work boots. I know they are expensive. They are worth it. 

Get some thing that breathes.
[i3243m4] (score 3, diepte 1) A lot of people are saying better boots but thoroughgood  American Heritage is a top-of-the-line but they don’t offer any ventilation and will result in wet feet
[i31oyfq] (score 3, diepte 3) I still hate em, they usually get me some funny socks that aren't very good for actual boot use haha
[i30x8vd] (score 3, diepte 2) I second this. Hiking socks are amazing both in trail and on the job site.
[i30t5gy] (score 3, diepte 0) I wear thick wool socks with my work boots year round. Costco has multipacks of wool trail socks pretty cheap
[i316xf5] (score 3, diepte 0) Step 1: Buy merino wool socks from costco
Step 2: wear them and enjoy comfortable feet.
[i317n6x] (score 3, diepte 0) Wool or poly socks help wick away moisture. Foot powder to absorb what is left and to prevent fungal growth.
[i31ioe3] (score 3, diepte 0) Wool socks only with work boots your feet will thank you later
[i31tkgy] (score 3, diepte 0) Try some lambs wool socks
[i32nhae] (score 2, diepte 4) DO NOT put Gold Bonds Blue on the balls!
[i314fqr] (score 2, diepte 1) Better steel toes too. Something with gortex
[i31mvwp] (score 2, diepte 3) I wouldn't think it'd matter. I've had both and never really noticed except for composite being lighter and doesn't get as cold in the winter.
[i33nqls] (score 2, diepte 7) You are just working too hard then. Take a break.
(271 reacties met lagere score weggelaten)

=== THREAD 13y6n17 ===
SUBREDDIT: r/AmazonFC
DATUM: 2023-06-02  SCORE: 110  REACTIES: 308
TITEL: oh for the love of god ive been at this job 3 weeks and everyday my body (specifically legs, feet and back) be killing me. (even my days off they hurt sometimes) how do you do it and not just give up like damn?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jmldimj] (score 122, diepte 0) As an anorexic at amazon…. You need to recover properly. Hydration, sleep, and adequate nutrition are paramount
[jmmaqxp] (score 78, diepte 2) Yep, I definitely “self identified” here. Not like I have been hospitalized and received medical care for my condition and still have lingering health issues. Eat my ass?
[jmla5ls] (score 72, diepte 0) Buy good insoles and actually do correct lifting and bending techniques. Once I did that I dropped the level of pain drastically it was ridiculous. I hate that they don't tell noobies this at orientation. I had to deal with this same issue for 3 months before I talked to a 3.5 year veteran coworker.
[jmm27lx] (score 57, diepte 1) They do but no one listens
[jmmmduo] (score 30, diepte 4) You’re a moron lmfao

Being anorexic implies that they learned the hard way that they need to be well fed and and fueled to tackle the physical nature of their job at amazon. Adding that bit info would lead intelligent people to assume that they have experience working this job while malnourished, and so they have some knowledge on how to combat it.
[jml7wi6] (score 29, diepte 0) It takes time, ive been doing it three years. You get use to it.
[jmm6wdk] (score 28, diepte 0) Donut shift saved me. Go hard for 2 days then have a day off. Go hard for 2 days then have 2 days off. Made a world of difference over 4 days straight.
[jmm8qjh] (score 27, diepte 3) They shove this down our throat everyday
[jmmk0xe] (score 27, diepte 3) Eat my ass as a question really cracked me up. Imagine telling a 7/11 cashier to “eat my ass?”.
[jmmw083] (score 24, diepte 6) With each additional comment, all you're doing is showing how uneducated you are. 

Take several seats and sit down, you clown.
[jmlct2w] (score 18, diepte 0) It hurts in the beginning because of the floors. They aren’t very friendly on the body. But just like working out or doing anything physical, you get used to it after a while.
[jmm2lll] (score 17, diepte 2) Not at my orientation. They did the second month at the working well for the lifting technique. But they never mentioned getting isoles or drinking enough water or getting enough sleep. Hell they didn't even cover the stretching stuff but until later.
[jmm4yuc] (score 17, diepte 1) My manager goes through this everyday in the morning meeting. He also makes everyone stretch. Seriously tho stretching before and after work can do wonderful things for the body.
[jmlxzbk] (score 17, diepte 0) to be perfectly honest, most jobs (that include repetitive labor of moderate or greater activity) have a 30-45 day window of building your body up.  

once you get to the point of muscle memory and strength what everyone else has mentioned is key.  supportive, comfortable shoes,/insoles (change them frequently, they wear fast), hydration, nutrition, stretching and proper rest/sleep for recovery.  if it still doesn't curb matters look into transferring to a less exhausting path.
[jmme1g0] (score 16, diepte 0) The 5-600$ every week. But nah I’ve been here for 6 months now, it doesn’t get any better no matter what shoes I try, I find myself going negative in UPT more often than not, but I’m still employed?? Metaphorically I’m hanging on by a thread. Advice to you, do not let it get this bad.
[jmmd5zg] (score 15, diepte 1) Here to say the same. Amazing what the body can adjust too. Give your body adequate rest and take care of it as much as possible on your days off. Also not sure how your diet is but avoiding inflammatory foods (fast food, seed oils, greasy food in general) helped me a ton.
[jml7yao] (score 15, diepte 0) Welcome to the dark side my friend. Where we are underpaid and ruining our bodies.

I've been at my warehouse 6 years and I can confirm while you don't hurt as badly after a while as you initially do when you first get hired, you never fully get used it to. Not me anyways.

Here's what I do which may seem like a lot but it genuinely helps so much. I still get aches and pains from time to time (I have arthritis in my back and I'm only 32) but these things totally help.

&#x200B;

1. 30 mins of stretching right before I leave home for work
2. wear. compression. socks
3. make sure you drink lots of water during shift
4. bend with your knees. don't take the fast way out and use your back instead
5. when I am on lunch I take my shoes off. I will also take off my compression socks for about a minute to let my feet breathe and then put those back on while I finish my lunch with my shoes off
6. when I get home (depending how much pain I am in specifically in my back)  I'll take a hot bath and once I am out and cooled off I will roll on some Biofreeze to where ever I'm hurting
7. if my feet are hurting I will use a roller ball thing and roll the bottom of my feet on it
8. get plenty of sleep
9. just say fuck it sometimes and leave work early (if you have the time and can afford to use it)

&#x200B;

also, find shoes that you feel most comfortable in. I've tried many many brands before finding one that made my feet not hurt as badly at the end of the day.

my last tip probably depends on your warehouse management but I am at a fresh site and my managers are pretty cool at listening to us when we have concerns as long as we NORMALLY do whatever they ask. So what I mean is that usually they ask me to do something and I do it without arguing or complaining so then lets say its day 4 of my work week and I have been in pick all week and my body is just done for I will ask to be put in stow all day that day so I can have a break because for me stowing doesn't kill my body nearly as much as pick and as long as they aren't behind in pick they will usually let me stow,
[jmm4b4h] (score 14, diepte 3) When i worked there they mentioned to lift with your legs, hydrate and also get free insoles from PT. Honestly amazon was heaven compared to other warehouse jobs I've been too.
[jmmhax7] (score 14, diepte 6) Your back story is irrelevant, theirs is directly related to the post since it involves heavy damage to their body. Instead of just reading their post and moving on you decided to troll over paraphrasing for attention. No one feels bad for you.
[jmm6oy4] (score 14, diepte 0) Weed
[jmm9u9m] (score 14, diepte 0) Lots of weed the over the counter pain killers work wonders if you don't use them all the time pace yourself don't hurt yourself take vto whenever possible
[jmml0dq] (score 12, diepte 8) With your attitude no ones gonna give a care about anything you say. Glad you don't work at my location. It's not hard to see that IF you did suffer any abuse, it turned you into a pretty shitty person. Take your negativity elsewhere.
[jmlyntt] (score 12, diepte 0) I tried so much and nothing ever worked for me. Part of the reason I’m quitting. My body has been through a lot in the past and I feel like working here is just too much for me physically so I’m not gonna push it. It’s just not worth it
[jmm7c6r] (score 11, diepte 2) Be happy you don’t have those problems…
[jmllgjq] (score 11, diepte 0) I think it took me 3 months for my body to get used to the abuse lol And I worked a pretty tough job in the vet med field before that.

Get sole inserts for your shoes. Do your stretches. Eat as much healthy protein and carbs as you can so your body can recover. Rest as much as possible.

Also do not over do it. This job makes billions in profits they will be fine. Good luck.
[jmn233u] (score 10, diepte 8) Your comments just get better and better (dumber and dumber). 😂
[jmmeoer] (score 9, diepte 2) living up to your username by assuming they self identified
[jmmgc2p] (score 9, diepte 4) Lol imagine if phrasing things a certain way made other people look openly ignorant 😂😂 here’s your gold star dumb ass
[jmmmqwq] (score 9, diepte 10) your parents must have ate lead paint chips cuz there is seriously something wrong with you
[jmm82qp] (score 8, diepte 5) Uhh i forgot what it was called wherever health care or physical therapy is in the warehouse just tell them your knees hurt and ask for insoles.
[jmni8dq] (score 7, diepte 6) It's a public forum, fucknuts, you opened yourself to everyone's opinion when you made a comment. That's how reddit works, you stupid child, and deleting your comment doesn't change that
[jmlyjy5] (score 7, diepte 0) Ibuprofen until your body builds up to it the work. But don’t take it all the time. Only take it because the pain is unbearable 

After 6 months you should be good and not need it anymore. There’s a reason why they offer it at amazon for free
[jmn8zhe] (score 7, diepte 1) This! I love my donut schedule!
[jmn219t] (score 6, diepte 11) We gotta stop interacting, it will crawl back to its hole where no one likes it soon enough
[jmn1x9w] (score 6, diepte 10) At this point you're delusional. You must have taken a few good blows to the head.
[jmn4pv3] (score 6, diepte 3) Clearly he's inbred. Your uncle and mom seem a little too close? Poor little guy
[jmleb5h] (score 6, diepte 0) Welcome to planned health obsolescence
[jmmpvh3] (score 6, diepte 1) Had to commiserate with your comment. I worked at Amazon for a couple of years, and it was excellent body conditioning for my current job in large animal vet med!
[jmm2dup] (score 6, diepte 0) Epson salt bath every day
[jmmf4mf] (score 6, diepte 0) I'm 57 with about 10 surgeries in my past including knees and arms. I am exhausted after every shift but my feet and back are rarely an issue.
[jmmzp74] (score 6, diepte 0) Just get a better job with actual benefits. (It’s not a benefit if you have to pay for it by the way)
[jmlauz0] (score 5, diepte 0) You get used to being in almost constant pain. It sucks, but it's money 🤷‍♀️
[jmnmkgi] (score 5, diepte 3) Nah man, he's a redit master.
[jmlmy3v] (score 5, diepte 0) When I started picked for the second time my finger tips hurt something crazy
[jmlx2sk] (score 5, diepte 0) No clue I've been doing this for about 6 months and still come home sore.  I take as much VTO as I can otherwise just massage, strech, and epsom salt soaks.
[jmn56vn] (score 5, diepte 6) It’s not giving up. It’s moving on. 🤷🏻‍♀️
[jmn6eqw] (score 5, diepte 8) Good for you. I don’t understand why you’re getting pressed about me not wanting to work for Amazon anymore lmao it’s not your life at all. Like I said I’m not quitting I’m moving onto better things.
[jmlzn1t] (score 5, diepte 0) That's why I love working at an airhub. I'm in a tug all day driving cans to and from the planes. Easy work.
[jmm3yd3] (score 5, diepte 0) This is going to sound like some old man shit.

Get a foot bath with massage settings & some Epson salt.
[jmm5lj8] (score 5, diepte 1) Every time I Pick a heated foot massage bath I’m like, they couldn’t just gift these to everyone?
[jmm4lj7] (score 5, diepte 0) Welcome to Camp Bezos 😂😂
You kind of get use to it and kind of don’t 🤷🏻‍♀️
[jmmj8dh] (score 4, diepte 2) Totally agree with you on food intake. All that 'bad food' will make you feel sluggish all the time.
[jmmyrpu] (score 4, diepte 10) Have fun working at Amazon the rest of your miserable life
[jmmmksy] (score 4, diepte 2) what the fuck is wrong with you?
[jmnly4c] (score 4, diepte 2) Imagine identifying as a “Reddit master”
[jmlyj5x] (score 4, diepte 0) Its a couple months to build your body up to it. My feet use to hurt after the first half of my first shift of the week. Now, i go on walks after work and still dont feel a thing. The legs and back are you just building up your core
[jmn05zk] (score 4, diepte 2) I would but unfortunately I can’t afford to work only part time
[jmn53sq] (score 4, diepte 5) My hands would literally swell up every single day and having a history of heart failure I’m not risking my health  for a job
[jmm5zuw] (score 4, diepte 0) Stretch before your shift. Lift with your knees, not your back. Practice the rule “nose to toes,” which means your nose should be aligned with your toes and facing the same direction. This will minimize the risk of injury. Insoles are also a good idea, though I don’t use any. It’s up to you. 

And make sure you’re eating a balanced diet. Eat lots of protein and greens. Bring snacks to work so you have something to eat besides buying from the break room store. Those purchases will start to add up fast.
[jmmbozc] (score 4, diepte 0) It gets better..trust me. It might take months but after awhile you’ll get use to it you really have to break you shoes in
[jmml3ti] (score 4, diepte 0) Amphetamines and painkillers

Kidding ...or am I?
[jmmmc2s] (score 4, diepte 0) murrjuana
[jmls6qd] (score 3, diepte 1) What compression socks do you recommend? & what shoes did you find work for you?
[jmm79u2] (score 3, diepte 4) Free insoles from where?
[jmmmnq4] (score 3, diepte 6) AM Care.  
  
I didn't know they had insoles.  
I'm going to ask at my location.
[jmmo6k9] (score 3, diepte 7) Good luck hopefully they got some
[jmms233] (score 3, diepte 7) Most locations don't, they expensive as hell. If your site doesn't, you can spend the remainder (if any) of this year's zappos credit on insoles.
[jmmrqo6] (score 3, diepte 3) Well then you need to contact your sites safety team and let them know they suck. As a safety member myself, I touch on all of these points and more during orientations. Heck I even litterally say "your probably going to ache the first few days" as I'm explaining what helps
[jmnjbgx] (score 3, diepte 1) They don’t tell you that new safety Shoes “no slip surface” when standing on the sticky rubber pad at the stow stations will shred your cartilage in both knees if your trying to go side to side fast between bins and pod!!!

I’ve got lifetime permanent damage in both knees now since day 4 because safety never told me to that that the shoes on the mat will stick. I was going side to side trying to impress how fast I could do the work.
[jmld6wr] (score 3, diepte 0) Stretching really does help. I’ve just added in core workouts for lower back pain and I’m already seeing an improvement. Good shoes and insoles help. Hydration helps a lot, too. I also roll my muscles out using a foam roller. Doing my thighs has cut my lower back pain down to almost nothing, if I use it often enough. I try to roll out when I get home and when I go to work. 

Seriously, I’ll come home hobbling in back pain, roll out for a few minutes, and walk around totally normal.

Also do the techniques they teach us, and try not to rotate your back much when holding heavy things!
[jmpavm9] (score 3, diepte 12) lol youre literally projecting with an incredibly unfunny and ironic example so im gonna assume they not only ate paint chips but ate more than a handful of em
[jmmnfcz] (score 3, diepte 8) Why do u care so much
[jmmpsvr] (score 3, diepte 10) Ur bored so u decided to come on Reddit and bully ppl😭
[jmmw4hn] (score 3, diepte 8) No one feels bad for you because you're an ass
[jmmzn7d] (score 3, diepte 12) You must be mistaken in thinking that I give a fuck. 

Eat shit.
[jmnn1e6] (score 3, diepte 4) Ah, my mistake.  I wonder what a “redit” is then🤔
[jmm5b3e] (score 3, diepte 1) My hands are numb and tingly from picking.  I’m sure that’s good long term 🙄
[jmltpsb] (score 3, diepte 0) ZMA and sleep
[jmmzev5] (score 3, diepte 1) Change your schedule. Do part time and pick up shorter extra shifts. Four tens and three 12s are hard on even the young and healthy.
[jmn59v2] (score 3, diepte 6) Just bc it works out for you doesn’t mean it will for everyone else
(215 reacties met lagere score weggelaten)

