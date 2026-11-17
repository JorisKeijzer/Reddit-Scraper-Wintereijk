# Label-batch batch_0066

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
Schrijf het resultaat naar `batch_0066.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1iiyl7t, y2yp9y, 153nlpc, 1lwcw3u).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1iiyl7t ===
SUBREDDIT: r/Construction
DATUM: 2025-02-06  SCORE: 31  REACTIES: 170
TITEL: Work boots have cooked my feet
POST (source_id=post):
Currently on the verge of quitting the construction industry due to being forced to wear steel / composite boots ( and standing all day long hours ) which have eventually lead to my feet developing issues. 

Can anyone recommend a shoe that is more like a runner shoe but has a composite or steel cap? I have found a few online but don't know anyone that's tried them.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mb9nju0] (score 148, diepte 0) I use to have have the same issue and especially being on a ladder all the time. Went to one of those foot doctor guys and they game me orthotics. Never had an issue again and that was about five years ago. Would definitely recommend
[mb9uyn1] (score 40, diepte 1) A podiatrist. Yes, my recommendation as well
[mb9rvtv] (score 31, diepte 0) Keens Cincinnati's with Darn Tough Marino wool padded socks have been the best for me. They sell extra wide boots also. 

My whole body can feel beat up but my feet are always good.
[mbbtyv5] (score 18, diepte 2) I like foot doctor guy better. Get these fancy titles and words out of here.
[mb9pd96] (score 18, diepte 0) Get some insoles.  I like these - [https://www.drscholls.com/products/tri-comfort-insoles?variant=47566289174804](https://www.drscholls.com/products/tri-comfort-insoles?variant=47566289174804)  You can get them at Walmart for under $10.
[mb9oyqc] (score 15, diepte 0) Not sure in the USA but in canada, you must have 6 inch steel toe boots to enter a job site.  Anyone who says they don't wear boots on a job site is just silly.
[mbdea0s] (score 14, diepte 3) Personally I think this sub should be called "buildin dudes" construction comes off pretty elitist.
[mbaxee2] (score 12, diepte 1) I had Plantar fasciitis in both feet. It was because I was a poor apprentice and I did not buy proper footwear.

With good boots and medical orthotics. My feet are almost at 100% it has taken 2 years and I'm 30years old.
[mbahr4j] (score 12, diepte 1) Came here to say Keens. I've worn the San Jose's, the Cinncinati's and just got a pair of Camden's for winter. Lots of different styles and toe type options. Some are more like work boots, some are more like snaekers or hiking boots.

[https://www.keenfootwear.com/collections/mens-work](https://www.keenfootwear.com/collections/mens-work)
[mb9z22r] (score 11, diepte 1) This is the only correct answer also maybe try a wedge style or a boot with less of a heel
[mb9zv0n] (score 11, diepte 2) What kind of boots? If you're buying cheap, shitty boots it's gonna fuck your feet up, then your knees, hips, & back. Nobody wants to hear that $250 boots are the answer, but they are. Get some wedge-soled, high quality boots.
[mb9u9qg] (score 11, diepte 0) Should probably just pack it in then.
[mb9w85j] (score 7, diepte 1) There are metal free work boots that are csa approved.  Made of composite I believe.  They weigh half as much, way more comfortable
[mbba44a] (score 7, diepte 2) yes the san joses are my favorite boots!!
[mbf2i1r] (score 6, diepte 2) Same story for me, just a few years older than you are. Stretching my hamstrings helped as well. Was amazing how much pain and inflammation comes from tight muscles/tendons.
[mb9x7kk] (score 6, diepte 1) I don't think that's true I'm pretty sure they just have to be green patch csa. 

Section 23 of the Construction Projects regulation (213/91) requires that all workers must wear protective footwear at all times when on a project. Protective footwear is a safety shoe or safety boot. 

Company policies may supersede this.
[mba6ysb] (score 6, diepte 1) I agree with insoles. I use super orange feet. I am very flat footed, to the point where the end of a couple of my toes are permanently curled. Super orange feet help quite a bit.
[mb9rzvw] (score 6, diepte 0) Go to a foot Dr and get orthotics.  An engineer couldn’t figure that out?
[mb9ud5u] (score 6, diepte 1 OP) That's what my podiatrist said 🤣
[mbbab1k] (score 5, diepte 1) Regular insoles were costing me about $30-40 a month so I went to the podiatrist for a pro pair, $120 later and it actually fixed several other back issues that I thought were unrelated. Those insoles have lasted me for many many years now
[mbajf91] (score 5, diepte 1) The toe doesn't need to be steel. It can be composite as well and still meet grade 1 csa
[mbc89zu] (score 5, diepte 2) Oh My God!!! They have construction shoes for women!?!?! Thank you for the link!
[mbb26tr] (score 5, diepte 0) Redwing

go to the physical store.

and have a podatrist check your feet for any unknown issues. (like arches, twist etc)
[mbb73if] (score 4, diepte 1) You have no idea what his site conditions may be....
[mba59dl] (score 3, diepte 1) My feet would melt off if I wore insulated boots in temps above 20F.
[mbco3rl] (score 3, diepte 3) Yes.why word
[mbajq15] (score 3, diepte 3) Or swinging sledgehammers or tools, rolling or falling debris.. shoes on a job site is a terrible idea. No matter what the trade.
[mbbcide] (score 3, diepte 1) Keen San Jose’s best boots I’ve worn, so far at least!
[mbew2ev] (score 3, diepte 1) Keen's for the win
[mbap1xy] (score 3, diepte 0) Steel toe Keens
[mbdxrgq] (score 3, diepte 1) Had to scroll a while to find Red Wing. I have a pair of EH rated, super breathable, composite toe low tops that are basically sneakers from red wing. I wear them when I know there’s going to be a lot of walking or getting into weird areas. Otherwise, Irish Setters with orthotics have also treated me well.
[mbe50x3] (score 2, diepte 2) Same, has to retire mine around 4 years and probably need to go get some more
[mb9ojax] (score 2, diepte 0) I’ve worn steel toe for almost 15 years. Are you sure you’ve got a decent boot with a proper fit? Have your boots been broken in yet?
[mba9h2z] (score 2, diepte 2) Grade 1 Workboots
One of three CSA grades, Grade 1 offers the highest 
protection and is the only one allowed in construction. 
In a Grade 1 boot, a steel toe protects against falling 
objects, while a steel insole prevents punctures to the 
bottom of the foot.
Grade 1 boots can be identified by the following 
markings (Figure 13-1):
• A green triangular patch containing the CSA logo 
on the outside of the boot
• A green label indicating Grade 1 protection on the 
inside of the boot
[mbad7gx] (score 2, diepte 3) I'd rather be wearing 8 inch tall boots while rolling an ankle than shoes. They absolutely protect.
[mb9rt6f] (score 2, diepte 0) Go to an orthopedist. 

My feet started biting me after 15 years. Endless calluses that would be painful. 

Went to orthopedist, noticed I was walking primarily on insides of foot. Made some insoles to slightly roll my feet flat. 

My feet don’t hurt since then, by product is my lower back issue I was seeing chiropractor for once and awhile is gone too.
[mbbj1ny] (score 2, diepte 1) I am in commercial scaffolding and had no idea a good pair of Marino wool socks would be such a game changer. I tell my crews regularly to invest in good socks. I found a good brand on Amazon from a recommendation in this sub, and I think it was $25 for 5 pairs, and it's all I wear even off-site.
[mbj36bo] (score 2, diepte 1) Another vote for Keen. They’re light, wide, and comfortable, and have tons of safety options. Basically all I wear now for work and general life.
[mb9tr3e] (score 2, diepte 0) Timberland pro work shoes
[mbbfbij] (score 2, diepte 3) I get that coat for it and then also the waterproof spray and I’ve been cruising through the Vancouver snow this last week!
[mbgt5w7] (score 2, diepte 1) Love my setters
[mbbyual] (score 2, diepte 0) I had some composite toe sneakers, they are comfy, light and offer decent protection... but they just don't hold up like the boots do.
[mbcpmcw] (score 2, diepte 0) Get boots that fit your feet! Keens for example have a wide toe box. And go to a running store and get some custome inserts.
[mb9m3un] (score 1, diepte 0) ...not sure what you as a field engineer but as a commercial roofer I don't wear steel or composite toes at all. I wear insulated irish setter red wings year round. Not too hot in the summer and my feet haven't gotten cold once, even below zero.
[mbaip6o] (score 1, diepte 2) They aren't gortex or anything crazy from what I understand, in the warmer months I do upwards of 20000 steps a day and I'm fine. I also tend to hyperfocus on my work so maybe I just don't notice. They come without insulation as well.
[mbf5cva] (score 1, diepte 3) Under rated comment
[mbhecu8] (score 1, diepte 3) Yeah that whole rear chain(calf/hamstrings/glutes)just start pulling on eachother making the problem worse.

We are not the only ones brother. I swear the more I talk to guys about this they either currently have this problem (maybe 10%) or have had a mild to severe case of it In the past.

The electricians I work with also get tendon problems in there forearms.
[mbb05cb] (score 1, diepte 1) This. The fit is extremely important.

When I first started, I wore my leather jump boots to my first site. Only after stepping on a tinknocker insulation nail (hiding in scraps of insulation on the floor), and then having to go to the hospital to get a tetanus booster, did I invest in a good pair of work boots.

I went to a Red Wing store, and it was the first time since I was a kid that they actually measured my feet. The size was completely different than most sneakers/boots I wear, and one my feet is apparently about a half size smaller than the other. They even gave me input on the styles of boots; I wanted a certain pair, but they said only short guys, or linemen wear them, and it’ll likely cause me back problems, I tried them on anyway and could feel my lower back being strained from the boot.

I’ve had Irish Setter, Red Wing, Thorogood, Wolverine, and a pair of Avengers I haven’t worn yet. They’re all composite except the Red Wings.

I’ve personally never had a problem with breaking any boots in, except for an almost new hand me down pair of Timberlands I got that made my feet scream after only two hours wearing them. The problem typically for me has been when the boots wear out, they become extremely uncomfortable.

tl;dr: OP should get a fit test (not me, but I know there’s a lot of hefty dudes in construction that require a wide, and also just go by their regular shoe size). Also, the more you spend, the better boots they’ll be. Red Wings is a good brand, but they were probably my cheapest boots, and they wore out quickly to the point where I don’t wear them, and that was with a daily rotation of boots (to avoid smell/fungus/too much wear on a single pair).
[mb9y70m] (score 1, diepte 1) its more of a safety protection thing in the states ive had some shoeish boots that were super comfy and just as protective
[mba4hm7] (score 1, diepte 2) Shoes can't protect  5 ankle rolls.  Uneven footing easy to roll an ankle.  Also, anything with sparks or welding slag having low-cut shoes is more likely to get hot shit in it.  The toe and the shank are there, but the ankle is left unprotected.
[mb9urro] (score 1, diepte 1) Dunlop Volley make a steel cap, I wear Rossi Hercules slip-on boots which aren't too hot (just sucks that fat cunt Gina Rhinehart bought them) don't wear those padded lace ups with a zip, failing that move to Tassie.
[mbaah3i] (score 1, diepte 1) Sounds crazy, but I wear 10” tall leather boots almost year round with over-the-calf wool socks.  Only in winter do i swap for a more insulated snow boot.

Mine are from Frank’s Boots in Spokane Washington. 

If you can find a custom boot maker in Australia, that’s your ticket.  They size the boot to your foot, and should be able to work with your orthopedic doctor to make something more comfortable.

Break in is usually 40-60 hours, and after that, is smooth sailing.  My boots have lasted almost 2-1/2 years and are now ready for a resole.  Brings my cost down to about $240/year.  They’re between 6-700 brand new, but can be resoled and rebuild for less afterwards.  

[Frank’s](https://franksboots.com)
[mbc5vtx] (score 1, diepte 1) Bruhhh if you're in Australia get some Redbacks with some nice insoles!
[mb9rggp] (score 1, diepte 0) I have one thing you need, shoe inserts. Also, switch shoes when they get worn.
[mbaha9g] (score 1, diepte 1) Came here to say Keens. Theyve got a wide variety of styles with various toe types. Some are more sneaker/hiking boot style, some are more work book style.

[https://www.keenfootwear.com/collections/mens-workhttps://www.keenfootwear.com/collections/mens-workI](https://www.keenfootwear.com/collections/mens-workhttps://www.keenfootwear.com/collections/mens-workI) had the San Jose's first, then switched to the Cinncinati's. Also just bought myself a pair of Camden's for winter.

[https://www.keenfootwear.com/collections/mens-workhttps://www.keenfootwear.com/collections/mens-workhttps://www.keenfootwear.com/collections/mens-workhttps://www.keenfootwear.com/collections/mens-workhttps://www.keenfootwear.com/collections/mens-work](https://www.keenfootwear.com/collections/mens-workhttps://www.keenfootwear.com/collections/mens-workhttps://www.keenfootwear.com/collections/mens-workhttps://www.keenfootwear.com/collections/mens-workhttps://www.keenfootwear.com/collections/mens-work)

[https://www.keenfootwear.com/collections/mens-work](https://www.keenfootwear.com/collections/mens-work)
[mbahb7p] (score 1, diepte 1) Dovers were the most comfortable boots I ever wore but the soles would peel off after 4 months. 😕
[mbgm8f0] (score 1, diepte 2) I'm a framer and I wear the Kentons.  They're basically Vans with a hard toe.
[mbavrj7] (score 1, diepte 1) ^^ this
[mbdhcg3] (score 1, diepte 2) The thicker the better as far as socks go. I wore Thorlo trekking socks for decades. They were like towels on your feet. A heavy cushion and they just wick the sweat away so dry and comfy feet all day regardless of the weather
[mbccs15] (score 1, diepte 1) I love my Keens and my Twisted X work boots with the padded Darn Tough socks. I ordered two styles of Wolverines and dislike 'em both. It's best if you can go to an independent small business and try on different styles, ideally with the owner there to help you make the best choice for your feet.
[mb9u1mk] (score 1, diepte 0) Get pedicures.
[mb9u8zg] (score 1, diepte 0) Bluntstones.
[mb9ylj1] (score 1, diepte 2) Scheters has a bunch of random styles boots/shoes with composite toes. They won’t last the longest, but it’s probably as close to a running shoe with a composite toe as you’re gonna get.
[mbafbel] (score 1, diepte 2) Have you been wearing flat or heeled boots? I'd give the opposite a try if you've only been wearing one type. I personally can only wear heeled boots. I tried a pair of keens that are more hiking style boots and my back and hamstrings felt horrible, I felt borderline crippled for 6 months. Then I got some Irish setter work boots with a good insole and I feel great. My boss is the opposite, said heeled boots made his lower back feel terrible and hiking style boots completely fixed it
[mb9ud18] (score 1, diepte 0) And how many so called carpenter’s have we seen wearing sneakers. They obviously have not stepped on a nail or dropped anything on their foot. YET.  I wear all leather Timberland’s.
[mb9w0ho] (score 1, diepte 0) Get some Nicks or Franks boots. I’ve been in the trades 8 years and they’ve saved my feet and every joint above them. $600 and will last you for years, worth every penny.
[mb9yyxy] (score 1, diepte 0) Those running looking shoes are only good for carpenters who typically work indoors. If you're outdoors, you want to make sure you're not rolling your ankle and should have a higher boot. Get some insoles or just stop being so whiny.
[mb9yyy3] (score 1, diepte 0) Georgia boot company makes ergonomic boots I have to wear mine with orthotics
[mb9zzsi] (score 1, diepte 0) Get quality wedge sole boots. They ain't cheap. But they are worth it.
[mba0z3h] (score 1, diepte 0) Reebok work makes Dayod with a composite toe .... a hightop skate style  shoe used them for years doing entertainment rigging work

https://amzn.asia/d/hiT7ooQ
[mba1bv5] (score 1, diepte 0) Expect to pay low bar $180+ for a pair of boots. Merrills and Keens are two lesser known brands that I’ve turned a lot of people to. 

Go to a podiatrist and get seen, if you can’t afford to, you can also go to a store that sells specialty runner’s footwear and have them put you through a gait test for shoe recommendations. You’ll probably have to run or at least walk on a treadmill for the test. 

You’ve got something going on. Either you’re buying cheap ass shoes and paying the price or you’ve got ortho/podiatry or gait issues. Get it checked out because the issues will compound over the years until you’re not just having trouble with your feet but your back, hips, and more.
[mba1emd] (score 1, diepte 0) Reebok work Dayod composite toe ... wore these for close to 10 yrs ... worked well for me 

https://amzn.asia/d/f5auUG7
[mba4hrj] (score 1, diepte 0) My company also requires steel/comp toe boots. I also suffered pain from them. So I started buying soft toe boots. I just would look safety dead in the eye and tell them they were comp toe. When they asked to touch my new boots I told them, sure they can scuff up mine. But then they'll buy me a new pair. Haven't had a problem since lol.
[mba4mr2] (score 1, diepte 0) Are you overweight at all? Losing weight helps everything.
[mba5gw4] (score 1, diepte 0) Kean RedHook. It's basically a very light high top sneaker. Don't expect super durability but nowadays I trade durability for weight.
[mba6a0b] (score 1, diepte 0) Thorogood is the only way.
[mba6o0q] (score 1, diepte 0) I'm surprised no one has mentioned socks yet.

Lots of good advice here about orthotics and good boots, but socks matter too. 

I wear the orange toed socks from Darn Tough. It's a game changer. 
I balked at the price, but hold your nose and buy one pair. 

Cheap socks are just as bad for feet as cheap boots.
[mba92cz] (score 1, diepte 0) Are you actually standing all day or moving around all day? If I stand for 30min my back hurts.
[mbau1q0] (score 1, diepte 1) Have you tried stretching?  Cardio+stretching helped a lot with my minor back pain.
[mbbnbpc] (score 1, diepte 2) Yeah, my back honestly hurts if I stand around doing nothing.  Or just walking around a mall. I need to be active
(98 reacties met lagere score weggelaten)

=== THREAD y2yp9y ===
SUBREDDIT: r/Costco
DATUM: 2022-10-13  SCORE: 298  REACTIES: 166
TITEL: I have size 17 feet but I still want the heated marino wool socks at Costco. A little pricey at $90 but dreams are expensive.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[is5lhd6] (score 218, diepte 0) I would have thought that sasquatch hair would be more thermally protective
[is6m3pm] (score 111, diepte 2) 2 and 10 hours is a... large range
[is5oqc4] (score 60, diepte 0) Heated socks/gloves on a cold motorbike/snowmobile or on a chilly sofa are a dream worth paying for.
[is5w355] (score 55, diepte 0) Huh.  Husband is a UPS driver.  Are these legit?
[is6nf7z] (score 54, diepte 3) 4 heat settings, I figure it lasts longer on lower heat
[is68c3p] (score 53, diepte 2) For someone who is just at home and the office $90 seems outrageous. As someone who has to work outside in all seasons $90 is a small price to pay for toasty toesies.
[is6wga1] (score 47, diepte 1) I don't wear this brand but I buy Darn Tough socks that are made from merino wool. They are the best damn socks I've ever owned. My feet don't smell anymore and never have that sweatiness to them, plus they're warm. They have a lifetime warranty and made in the USA (Vermont). Expensive but totally worth each pair.

Edit: I'm dumb and didn't realize these socks are electrically heated. The Bluetooth should have tipped me off.
[is5wzlr] (score 41, diepte 1 OP) I don't know if they would last an entire shift. I think it says between 2 and 10 hours...... but it's worth a try imo
[is5lnd1] (score 40, diepte 1 OP) Lolol
[is5oizy] (score 32, diepte 0) Does anyone have these and know where the battery is located/if it would fit in womens ski boots? I’m assuming so…. But just wondering if anyone has actual experience with them.
[is5xxhh] (score 30, diepte 0) A "little" pricey? 90$ is outrageous 😬
[is62rpg] (score 25, diepte 0) If you get them please post a review! I have a side gig that has me working outside once a week year round and would be stoked if these actually worked. I've tried the hot hands boot warmers but they fit awkwardly and end up being so uncomfortable it's not worth it.
[is6yhte] (score 22, diepte 3) Its its like most electronics 2-10 means 1.75 haha
[is6fol4] (score 21, diepte 2) Good God, man.  Figured it was a typo.

Dafuq do you do for shoes?
[is6nfn0] (score 19, diepte 1) They are really long (past my calves)and the battery is at the top. Shouldn't be a problem with ski boot at all. Bluetooth control is nice so you dont have to undress to change temp or turn on/off. They are not any thicker than other wool socks that I have, and much less thick than my thickest.
[is6b3hv] (score 19, diepte 0) You have what?
[is69ee0] (score 18, diepte 0) Looks like there are only two reviews on Costco.com (one five star and one one star) both say they heat great but the one star review said they had battery problems with two pairs but had an easy time returning them for a another pair.

https://www.costco.com/mobile-warming-bluetooth-heated-socks.product.100987995.html
[is6cg11] (score 17, diepte 2) I'm glad you laughed, I'm trying to swallow some chicken here and can't.
[is6dcks] (score 17, diepte 1 OP) Feet too large for these socks. They only fit up to size 14.
[is766hw] (score 16, diepte 1) Ever heard of Minnesota tube socks? You wear 2 pair of socks with a plastic bag or a newspaper bag between. It's crazy effective.
[is6jqru] (score 16, diepte 0) Unrelated but I have size 16 check out [oddball.com](https://oddball.com) for large shoes and socks, gamechanger
[is5z270] (score 15, diepte 1) By the looks of the socks in the picture they seem pretty thick. If you are any type of performance skier and have stiffer boots thicker socks are going to suck and are going to affect response. I think you'd be better off going to Amazon and just searching heated ski socks for women. If you're just cruising green and blue groomers the Costco ones will probably be fine. The ones on amazon are cheaper than the Costco ones tho from a quick search.
[is6ugb3] (score 15, diepte 1 OP) Same man lol
[is5p6qw] (score 13, diepte 1 OP) Agreed!
[is70a8y] (score 12, diepte 3) Yeah, definitely recommend Darn Tough for socks then. They're awesome.
[is6t30p] (score 12, diepte 0) damn I'm 15 wide and have an issue finding stuff that fits. Sorry buddy. How tall are you? I'm 6'8"
[is6uirj] (score 12, diepte 1 OP) Crap....I didn't mean to out him like that lol
[is63dhu] (score 11, diepte 1 OP) But warm feet though, right?
[is6moke] (score 11, diepte 3 OP) Online only unfortunately lol
[is6n42x] (score 11, diepte 1 OP) Been shopping there for years!
[is7wu14] (score 11, diepte 0) Okay but hear me out. It’s -32 you’re a delivery man and it’s Christmas rush.
[is75x0e] (score 10, diepte 4) They're the only socks I buy!  They're worth every penny
[is7v9yc] (score 10, diepte 2) Darn Tough socks are the only way to go.  Keep me warm in the winter, cool in summer. They will probably outlast me, and if they don't Darn Tough will replace them!  Plus about 65 dollars less than the electric socks.  Maybe they wont be as warm as electric socks but they will definitely be warm enough and last waaaaaaaay longer.
[is609gx] (score 10, diepte 0) Damn these would’ve been perfect when I had an outdoor job working in -20/-30 weather
[is62rs3] (score 10, diepte 0) Thanks for telling us your foot size?
[is6dt09] (score 10, diepte 0) Fellow yeti here, finding socks that fit is a constant challenge.
[is6o3o0] (score 9, diepte 1) I have them but its not cold enough to give a good test. I bought the heated gloves from costco last year and they are great. I wore them taking my dog for a run on my ebike at -10° last winter for a few miles and my hands were warm at 10 or so MPH.
[is6cifv] (score 9, diepte 0) Heated socks??? Now this is innovation.
[is7a4ki] (score 9, diepte 0) Okay Peggy Hill.
[is6zokn] (score 8, diepte 2) To me they seem just as thick as Darn Tough ski socks and others like that. They don’t look so thick that they are going to affect response/performance.
[is6zf10] (score 8, diepte 2) lol.  Hey, he has major feet issues in the winter, so you better believe I'm filing away the brand you mentioned as well!  I feel like the hyper-technical things don't stand up well to the constant abuse.  Though...I did get him a heated hoodie a few years back that is still working.  Feet are different though, he busts through a pair of shoes in about 4 months flat.  Literally has toes poking through.
[is6t2av] (score 8, diepte 1) these arent just 'big socks' they are going to keep your toes from literally freezing and falling off.  $90 is cheap compared to new toes.
[is73zw0] (score 8, diepte 1) My husband’s also 6’8” with size 16 feet, and he loves the Weatherproof wool blend socks Costco sells - they say they only go up to size 12, but they have so much stretch!
[is70vxc] (score 7, diepte 1) 💀
[is6h2mx] (score 7, diepte 3) I would have absolutely sprung for these a few years ago when I had to wait for buses in -20 Fahrenheit or below.
[is63hqh] (score 7, diepte 1 OP) Yeah they look interesting. Not sure if it gets cold enough in KS but -20....I definitely would have bought some
[is6kc2q] (score 7, diepte 0) Not sure if I’d rather have cold feet or sweaty feet.
[is7i2av] (score 7, diepte 2) My best friend (female) growing up was a mens 13 by the time she was 14. She was also 6' tall. I've been 5'4" since 5th grade
[is91ypf] (score 6, diepte 3) Look into their full cushion mountaineering sock which has the most cushion but is also supremely thick. It’s built for most conditions and keeps you pretty warm although you might need to size up in shoes.
[is821xj] (score 6, diepte 3) True dat. I bought at least 8 pairs for work in the office. Damn things are too comfortable to wear any other sock in my office shoes. I will die on this hill that any sock is better than Darn Tough.
[is6d5ov] (score 6, diepte 3 OP) Agreed.....it definitely solves a first world problem for office workers lol
[is6dyw7] (score 6, diepte 1) you know what they say about big feet
[is73n7t] (score 6, diepte 1) THANK YOU. My husband wears size 16 and finding him shoes is such a pain!
[is6ngsv] (score 6, diepte 1 OP) The weird thing is I've had 17s since I was 14 years old....imagine that
[is6uj1c] (score 6, diepte 0) “Shoot, forgot to charge my socks” is something I never thought I’d have to say.
[is9q0qt] (score 5, diepte 3) It's easier if you pluck the feathers off first.
[is8j8fm] (score 5, diepte 4) Hello fellow (non-sponsored) Reddit fellow, I too stand by Darn Tough socks and receive no financial benefit from saying so 👋.
[is6km12] (score 5, diepte 0) I have an aversion to feet, even my own, no idea why. But I'm totally curious what a size 17 look like. My SO is size 12.
[is76kfl] (score 5, diepte 3 OP) Yeah, being 6'8" and not being good at basketball was even more horrible than large shoes lol
[is6m84l] (score 5, diepte 0) Hey fellow giant foot haver.  If you aren't familiar with it, oddball.com is the bees knees.  They only carry 14s and up.
[is7zfaj] (score 5, diepte 1) Hoe yeaaaaa
[is7s9ho] (score 5, diepte 0) app controlled socks? hope the tech support team is good for those SOCKS.

apps for socks LMAO
[is8vmiq] (score 5, diepte 0) Daughter and I each have a pair for skiing. They’re quite nice. We usually run them on the lowest setting and that gets us through most of a day of skiing. 

On cold days when we turn them up… the battery life is short. 

All the smarts are integrated into the battery pack. One of our battery packs stopped charging and the manufacturer shipped a two pack of new batteries no problem. Just had to Bluetooth pairing again. 

Remote is on your smartphone, but the temp can be set by the button on the battery pack as well. So you can set it and forget it.

Socks with bigger battery packs that can be attached to the outside of your boots are much more expensive. 

And more comfortable than putting a “Little Hottie” or similar toe warmer in your boot.
[is8ijfl] (score 4, diepte 2) That's brilliant, will definitely try it!
[is6rlfe] (score 4, diepte 2) Big wool socks?
[is6vd16] (score 4, diepte 2) Ha! Apparently he thought they were $39.99 instead of $89.99. Luckily the box is still closed!
[is7zj6e] (score 4, diepte 1 OP) Yeah it's better to have and not want than to want and not have.
[is8fra2] (score 4, diepte 0) how do you keep these clean??
[is8g1qa] (score 4, diepte 1 OP) They are washable but that's the question....how many wash cycles would they last, right?
[is8g8m0] (score 4, diepte 2) yeah thats what im thinking as well
[is8ntmd] (score 4, diepte 1 OP) Hahaha
[is848d9] (score 3, diepte 4) I'll die with you on that hill...no sock is better than Darn Tough.

 Of everything I wear,   its the highest quality garment on my body, by far.
[is9hps5] (score 3, diepte 5) I’ll be the third person to die on that hill in agreement.
[isa8l2k] (score 3, diepte 2) Add this man. He socks. Darn Tough is the bees knees.
[is8a4fh] (score 3, diepte 1) Fieldsheer makes heated gear for motorcycling, it’s legit. There’s nothing that feels colder than freezing temps at 70mph. No reasonable insulation can stop that cold from creeping in.
[is94djy] (score 3, diepte 2) huh...  maybe someone should create a sock with a layer or 2 of mylar in between 2 layers of wool.
[is6elyl] (score 3, diepte 2) Big shoes?
[is7wp9t] (score 3, diepte 1) A hog, I bet.
[is6mmvh] (score 3, diepte 1 OP) Yeah try oddball.com ....seriously.... they have some good stuff
[is6johy] (score 3, diepte 0) Good ol' Marino wool
(83 reacties met lagere score weggelaten)

=== THREAD 153nlpc ===
SUBREDDIT: r/AmazonFC
DATUM: 2023-07-19  SCORE: 87  REACTIES: 147
TITEL: My feet are KILLING ME
POST (source_id=post):
Literally crying at my station from the pain, I’ve bought three different types of insoles and compression socks but nothing works! I’m in so much pain it drives me insane

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jskcuyp] (score 63, diepte 0) I would suggest seeing a doctor,I had the same problem and it turned out I had diabetes. Once I started medicine and lowered my carb intake my feet felt so much better. My brother also developed plantar fasciitis from warehouse work and had to get a special insole made. I hope you start feeling better soon !
[jskhrsh] (score 26, diepte 0) I have 4 pairs of shoes and I wear a different shoe every day. I rotate through them, they all have Superfeet insoles (have your arch measured) and I double up on my socks, and if I get a blister I tape it. I’m also experimenting with using sports tape (think KT tape) as additional foot support.

I’m on my second month, I work the dock and I walk 11 miles per shift. My feet never hurt.
[jskitic] (score 24, diepte 0) I'd second the comment about getting medical help. It's a part of your benefits. 

Get an appointment with a podiatrist. This isn't typical for most younger people, but this is the specialist you need. They can recommend the kind of footwear you need, and they can also scan your feet to make custom insoles that are basically indestructible. Keep in mind you're not trying to win a fashion show. Oh, and composite toe is much lighter than steel toe. 

Take pain meds. You will adapt.
[jskx9wj] (score 24, diepte 0) https://preview.redd.it/a4crcemfzwcb1.jpeg?width=1290&format=pjpg&auto=webp&s=744decb0f8c5d20b367bfedfea497fb2be915f8d

These shoes are literally a game changer. They literally stopped my foot pain since the day I bought it. I was coming from Timberlands Pro boots that I bought from Zappos and they were ass. $50 will literally save you. Take my word for it. Bought it for my gf as well and literally our feet thanked us. Also I heard if you combine these with Dr. Scholls insoles from Walmart you’ll pull 60s with no issues at all. I HIGHLY RECOMMEND!!
[jsk7c9l] (score 21, diepte 0) Try putting 2 insoles together. It works for me.
[jsle6dr] (score 14, diepte 0) I pregame 600 mg of ibuprofen about 30 minutes before my shift.  It helps alot.
[jslkn57] (score 13, diepte 0) I wear some sketchers that look like safety shows but they’re not. Been wearing it since basically last year.  No one ever says anything.  I hate those safety shoes too
[jsk7prm] (score 11, diepte 0) Send the shoes back and try a different pair.
[jslcvfb] (score 11, diepte 2) How much is being pain free worth to you?? Lol

**AA turns nose up at copay, same AA misses work, turns down VET because feet hurt resulting in $400/week loss*** lol
[jsld9am] (score 10, diepte 1) A couple years in, when does my body adapt and stop hurting? Because honestly it’s just been getting worse
[jsl3p43] (score 9, diepte 1) Agreed - these are way more comfortable than all the Zappos $120 shoes I’ve gotten (4 different brands)
[jsl8tco] (score 8, diepte 0) bruhhh this job suckssss  😩
[jsmorl5] (score 7, diepte 1) I change shoes at lunch time. That way the same shoe isn't worn for more than 7 hours
[jsl7pf5] (score 7, diepte 0) I'd suggest getting those shoes someone else mentioned with a picture and also going to a doctor. Those shoes are the best I've found. The doctor might be able to get you something that helps. When I first started I was also crying in my station every day. I ended up with plantar fasciitis in both feet and going to a podiatrist. I got custom insoles, steroids and ended up getting some shots in my feet (don't remember what it was rn). After all that I finally was okay but it was a 4 month process.

I wish you luck OP. Hopefully you can figure out what is wrong.
[jslfn7l] (score 7, diepte 0) I hear ya my feet feel.like they are in fire!
[jsm8adr] (score 6, diepte 3) i recommend 4
[jsm1tww] (score 6, diepte 5) We get a pay cut yearly cause our benefits go up and wages don't. This job decimates our feet. Why should that cost be put on us.
[jsn14ah] (score 6, diepte 3) At this point fentanyl doesn't sound too bad
[jsmiwr6] (score 6, diepte 0) It's probably plantar fasciitis (and maybe tendonitis as well) and won't go away till you are able to stay off your feet to heal. I'm dealing with this right now and had been dealing with it for a couple months till I took a leave and went to the doctor. My doctor told me a minimum of 8 weeks sit down accommodation but I'm already going on 2 weeks off work with no pay and no accommodation yet. This is definitely a work related condition so people who get it should really be getting worker's comp yet I don't think Amazon wants to admit that. Good luck!
[jski4sm] (score 5, diepte 0) You’ll love the next 3 weeks
[jsnmuga] (score 5, diepte 5) Entitlement? For wanting health, safety, and treatment for the damage our bodies incur from work?

Okay, sure. I believe all people are entitled to such things.
[jsmbzo7] (score 5, diepte 2) It won’t be used other than work so most of the time it gets dirty from all the boxes and shit so I don’t mind the lettering
[jsn2ty3] (score 5, diepte 1) I second this! I suffer from neuropathy and those Zappos shoes are the worst. These bad boys have been saving me from all the pain
[jsmboe2] (score 5, diepte 1) I'm doing 800 mg and thinking about getting some percs cuz it ain't helping
[jsm10ao] (score 5, diepte 0) I’m 10+ years in, and I have flat feet (like so flat I can clap them, flat). About 7 months ago, it felt like the bones from the top of my feet were collapsing into the bottom. I went to a store called “Good Feet”. I won’t lie: the inserts are not cheap, but you get what you pay for. I got the whole set (they take FSA, yay!), and now I have no pain related to walking/standing all day. Admittedly it takes a few weeks to get used to them, but it’s so worth it.
[jspoyw4] (score 5, diepte 1) Kind of stupid how we have to do ALL this preparation just to not have to break down crying in pain at work...but good advice nonetheless, thank you 👍
[jsmo3rn] (score 5, diepte 0) This was me when I started for the first month. I'd personally try some of these before the doctor just because I couldn't afford it. But if after a month these things don't work, I'd definitely recommend a Podiatrist.

-Buy bigger shoes, I used to be able to wear 10-10.5 and be comfortable. But being on your feet this long can make them swell, I went with 4E (Extra wide) 11's and that helped a lot. Some people say go up to 1-2 sizes bigger, maybe experiment a little.

-Buy a foot massager off Amazon, I found a good one for like $40 or so. Provides me instant pain relief the second I get home. 

-Freeze some water bottles and forcefully roll your bare feet on them when you get home. 

-Try to soak your feet in hot water mixed with Epsom salt daily or every other day. 

-Take advantage of the free advil they give at Amazon. I take 2 on first break and 2 on last break (Don't do this too long, but a month or so shouldn't kill you) 

-On lunch try to eat A LOT of protein. I was eating the big METRX Bars from Walmart with like 32g of protein (They do have a good amount of sugar tho, so watch that) 

-Drink water and only water and a lot of water at work. 

-I didn't do this one but a lot of people says it helps (Change socks and even shoes on lunch break in your car) 

-Try diabetic socks, I took everyone's advice and used compression socks and my feet never hurt more in my life than on that day. Diabetic socks seemed to help me a lot. 

-Consider taking daily vitamins. I always take a Vitamin C, a Multivitamin, and a Magnesium supplement. I think magnesium is the biggest one tho. 

-Maybe try to lose weight, I've lost 20 pounds since I started and I strongly believe that's one of the biggest reasons I'm not in as much pain anymore. 

-Take advantage of your time off and leave an hour or 2 early every other day or so for a bit. But try to limit full days off as much as possible, every full day off is another day longer you'll be in pain. 

-Stretch! I try to make sure I stretch every leg muscle possible for like 10-15 seconds everyday before I even leave. I also stretch back and arms.

-Most people already do this including me. But use the bathroom and have a full bottle of water before break even starts. (I go like 30 minutes before break) That way  you get the max amount of sitting down time possible on breaks.

Good luck, I hope this is able to help someone.
[jsnjuin] (score 4, diepte 1) You got me thinking i might have diabetes 😭
[jsnni4h] (score 4, diepte 1) They got you on some lightweight dock work. 15 miles was the low end when I was dock. I’m getting 8-9 in pack.

Have a bunch of different shoes and switch out when I can. Not worth wasting my break not getting the time to rest a bit does worse for me. It’s a lot of my own money and time to spend on all of that for what little we are paid and barely making it by. Cost of living is just too high here for what we are paid. So using that much to experiment to find what works for me (or anyone doing it) to balance comfort and pain, it just isn’t feasible for all of us
[jskzgnq] (score 4, diepte 0) Its always best to just get some top tier running shoe that could pass as "safety shoes" like Asics or Brooks, then just have an insole that matches your feet. (I have flat feet so I use the overpronation insoles)
[jslv6td] (score 4, diepte 1) Send a pic 😁😁
[jsm5q5l] (score 4, diepte 0) My advice would either be stretching, losing some weight, or find another job.

You’d be surprised how much some calisthenics and flexibility exercises can affect something like foot pain. All our muscles connect and tightness in one place is going to create issues in all kinds of “unrelated” places. Foot pain could be tight hamstrings, hips, back, etc. 

If that doesn’t help, and frankly if you’re really in that much pain, finding another job where you don’t have to be on your feet all day might be the best choice for you definitely short term and long term. 

Finally, weight. Idk your situation obviously, but if you’re overweight, your feet and legs are going to be carrying that load. I lost about 15 pounds from 225 to 210 just because I could feel the extra weight I had put in in my legs and when I moved. Even if you’re not overweight or obese, consider losing 5-10 pounds of fat, you’d be surprised by the difference.
[jsmed2b] (score 4, diepte 0) Your feet are surrounded by muscle and that is likely what is hurting. When first starting at Amazon that is by far the most worked muscle and people neglect to eat more to compensate for it.

Furthermore for walking heavy roles insoles can counterintuitively be more harmful than good in my experience. Your feet muscles stretch as you walk, insoles especially with arch support tend to block muscle movement such as your arch stretching. It only doing a few thousand steps a day it wouldn't be an issue but if doing 20k+ a day which wouldnt be uncommon for many paths you are destroying your arch and your feet's supporting muscles causing overall pain.

If using an insole id suggest one that has minimal arch support if none at all, essentially just a cushion and eventually switch off entirely. Also up your calorie intake for a month or two. Your feet should be a lot more well adjusted after the fact and you wouldn't even notice feet pain after the fact. I am a diabetic who just did 2 60hr weeks in a delivery station averaging 40k+ steps a day. My feet arent even the tiniest bit sore anymore aside from me bumping my big toe at home one day.
[jsll2jk] (score 3, diepte 1) yup i had to do this. Size up and double insoles.
[jsm73u6] (score 3, diepte 2) 3 works much better
[jsmbx63] (score 3, diepte 4) I heard a friend tried 5 but his feet were swollen from being crushed inside, so maybe 4 is the sweet spot
[jskezss] (score 3, diepte 0) See podiatrist  if possible, I did after I couldn't find any relief no matter what shoes, insoles, compression socks, or any other type of device I tried.
[jskgth3] (score 3, diepte 0) do an epsom salt foot soak with hot water.
[jslf6ny] (score 3, diepte 3) No,  Amazon should provide free podiatry care to all associates.
[jsmo4rk] (score 3, diepte 5) Please bring your unicorn to work, I'll allow it. 👀
[jsnkruo] (score 3, diepte 2) It never stops, the job destroys our bodies. There are 24 hours in a day and we spend HALF of it standing up.
[jsknnl5] (score 3, diepte 0) What part of ur feet are hurting? Have u tried KT tape?
[jsln4ia] (score 3, diepte 1) Almost everyone at my warehouse has these.  And I agree,  I also got the Timberland Pro boots and they are definitely ASS! I was buying insoles every other month and nothing helped with those ASS boots.
[jsmc77v] (score 3, diepte 3) I painted mine with acrylic leather ink.
[jsp2u76] (score 3, diepte 1) Ibuprofen has some nasty long term effects
[jsnk05k] (score 3, diepte 1) Yup I do the same but with asics.  All black and no one ever says anything but in my building a lot of people don’t wear safety shoes
[jsm46u1] (score 3, diepte 0) First: see a doctor. 
Second: see a podiatrist. 
Third: see an orthopedic surgeon. 
Fourth: KT tape and bandage wrap your feet prior to work. 
Fifth: hot epsom salt bath for feet after work. 
Sixth: topical pain cream on feet. 
Seventh: Tylenol, *good* food, whey protein, concentrate powder, probiotics, vitamins and sleep.
[jsq702n] (score 3, diepte 2) I agree. We should form a union and make Amazon listen to reason.
[jsmbt6q] (score 3, diepte 0) Smoke a blunt and drink an old English
[jsmmskd] (score 3, diepte 0) Get yourself some compression socks, dr. Recommended that and was a game changer SB Soxx on Amazon are excellent
[jsmnqid] (score 3, diepte 0) You probably have plantar fasciitis or planters feet. Inflammation of the arch or heel. I've had it for over a year, I think due to the fucking safety shoes. Does it feel like you've been on your feet all day after only an hour or 2? It's horrible.  It literally got to the point where I would dig my nails into my arm out of frustration. Try icing your feet every day after work until you can see a doctor you'll notice results quick.
[jsnjr0x] (score 3, diepte 0) Me after just buying compression socks and insoles 🤡 hopefully they work for me because my feet are so done.
[jsnkcj4] (score 3, diepte 0) We have to wear safety shoes now. They hurt even more than nice running shoes
[jstm7n6] (score 3, diepte 0) Wear whatever shoes you want and put composite toe stretch overs on. Literally stretch a composite toe over your pre existing shoe of your choice! Ugly as sin but  so worth the clown look. No joke. AKA OSHA TOES.... SAFETY SHOES HURT BECAUSE THEY STRAIGHT UP MESS UP YOUR GATE. YOUR POSTURE. YOUR FEET IN GENERAL. LOOK AT THE FEET OF BLUE COLLAR CONSTRUCTION WORKERS.... DONT DO THAT TO YOURSELF. Eventually you end up w back problems too.
[jsmp9yg] (score 2, diepte 1) Do they allow us to exchange once the shoes have been worn? I've been pushing through my bruised, bloodied and falling off nails because I thought returns were for 365 days, but unused shoes only
[jsntgt7] (score 2, diepte 2) Nah. Use the zappos online chat and explain that they are defective. Have some part of them that's tearing up. They will reup your subsidy right away so you can reorder something else and they email a shipping label to return the defective shoes
[jsolotg] (score 2, diepte 2) Yes. I return shoes all the time. Work shoes. Everyone in my warehouse returns shoes. I get shoes twice a year, and the HR manager says “Return them if they don’t fit well or are defective”. But since you’ve been wearing them while crying, they’re defective now”. And keep returning them until you get a pair that fit properly. This was a huge issue in my warehouse when these shoes were implemented across Amazon in April 2021. It made many quit in my warehouse.
[jskb98x] (score 2, diepte 0) Take advil it helped me when mines were hurting last week
[jsm8ky9] (score 2, diepte 1) I took Tylenol extra strength and the pain fought through it, felt like needs were in my toes
[jsmd8q0] (score 2, diepte 2) Tylenol never works for me only advil and ibuprofen you might wanna try either of those I’m sorry your feet hurt 😭 mines felt like they were on fire that week of prime just try to keep them elevated whenever you can 🙂
[jslrexq] (score 2, diepte 1) See a doctor first. Severe foot pain could be a sign of diabetes. Diabetics should not soak their feet, it only makes it worse.
[jskh1c3] (score 2, diepte 0) How old are your shoes?
[jsmixt5] (score 2, diepte 1) This guy foots.
[jsnnviy] (score 2, diepte 3 OP) Bottom! It feels like all my weight is crushing the bottom of my feet
[jsnkee2] (score 2, diepte 1) Yes! Been using my asics for over a year now
[jslbg62] (score 2, diepte 0) I feel you on that
[jsmr5uf] (score 2, diepte 2) There is no therapeutic difference between 600mg and 800 mg, only a steep increase in your chance of developing an ulcer, as far as Percs go it’s rare a doctor will prescribe them anymore, usually they start you on gabapentin and prednisone, then force you to go to pain management which will just increase those doses, very difficult in the US to get pain meds anymore. If you buy them on the street you are.just going to end up with fentanyl
[jsnbv8b] (score 2, diepte 3) be careful using gabapentin if you're going for CDL..  you can get automatic disqualification depending on the circumstances..
[jspbk66] (score 2, diepte 1) Man I must be cursed, I only take 400mg on workdays and I gave myself a stomach ulcer. :(
[jslk39n] (score 2, diepte 0) Are you actively looking for a new job?
[jsnt6x1] (score 2, diepte 1) Just adding a disclaimer. Be careful doing this depending what area you work. You get your foot caught or ran over and they investigate and you were wearing unsafe ppe they won't cover your medical costs
[jsm8dn9] (score 2, diepte 0) I use a foot spa from Walmart with epsom salt, some light hiking socks from big 5, and shoes that aren’t fully cushy but are half supportive and half cushy because of fatigue of a too soft shoe. I also see what type of arch I have by wetting my foot and putting on a piece of paper and look for insoles based on my arch type. I used to have serious pain in my arch but it’s finally going away. For pre work routine I take ibuprofen sometimes but I use a massage gun and stretch and it helps a lot as well. If you have the resources and time I’d recommend seeing the foot doctor though.
[jsmgdsn] (score 2, diepte 0) Depending on the type of foot you have will change what type of shoe you need. I've suffered from plantar fasciitis  in the past and it took such a long time to heal. Also, I'm a big person (300 lbs). For me, the o ly shoes that helped were when I had the custom orthotics (from a podiatrist) and I used them in the skechers max cushioning (which has a composite toe) for all the walking I did. For standing,

 I like the Merrill work fulbright composite toe. I believe it was labeled superlite, but I'm not entirely sure tbh. Those were the only shoes that worked for me. 
I couldn't use the insole that the skechers came with which was why I used the orthotics. 

Merrill I could use the insole that had the flat sides, not the ones that curl up and I ended up using my orthotics again in that shoe and it's great. 

Also just a note, the way you walk can cause a lot more discomfort if you wear shoes that don't work for your feet. It can affect your knees, your hips and then your back. I have been there. And if you decide to try any new work shoe, make sure you break them in over a week first (1-2 hr first day, 2-4 hrs second day, etc). If your shoes aren't broken in, that'll kill you too. Definitely see a foot doctor (podiatrist) when you can and make sure it's not plantar fasciitis for you. 

I wish you the best of luck.
(79 reacties met lagere score weggelaten)

=== THREAD 1lwcw3u ===
SUBREDDIT: r/AmazonFC
DATUM: 2025-07-10  SCORE: 298  REACTIES: 142
TITEL: Look what they rewarded me after wearing feet & legs out for 12hrs 😆
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[n2d3g8h] (score 162, diepte 0) ![gif](giphy|9d7Cql3JjU7SROkV3o)

Did you say thank you?
[n2dc76s] (score 69, diepte 0) https://preview.redd.it/htxyff8752cf1.jpeg?width=768&format=pjpg&auto=webp&s=fc6caaa9add3196540901806f6d7d3bcf0fdc914

I got a rock
[n2d5azh] (score 52, diepte 0) ![gif](giphy|JHmXZW3xYaDGE)
[n2d4qqf] (score 37, diepte 0) My site gave out ices and I think granola bars. But the catch was that they could only choose one or the other. Crazy work.
[n2da7ml] (score 34, diepte 1) THIS GIF???? 😭😭😭
[n2d1ktz] (score 30, diepte 0 OP) It could’ve at least been the cookies n’ cream or chocolate flavor. 😆
[n2dbehn] (score 30, diepte 0) My site calls it Snack Attack
[n2df3xo] (score 28, diepte 1) My site gave out melted popsicle. Management smiled and said “🙂 wanna popsicle?” Literally juice in a bag
[n2dgvyb] (score 23, diepte 1) Strawberry is very underrated
[n2eppj5] (score 16, diepte 1) Imma attack you with diabetes….
[n2d1ara] (score 15, diepte 0) The shareholders thank you
[n2d2fww] (score 14, diepte 0) Surprise if it’s not expired
[n2dq0gh] (score 12, diepte 0) A lot of miserable ass kissers in the comments 😬 at least you got a pop tart. All I got was a jolly rancher
[n2e56n1] (score 11, diepte 0) Check expiry date on it
[n2de7r3] (score 10, diepte 1) I laughed harder than I should have. 🥴
[n2d3pfe] (score 9, diepte 0) https://preview.redd.it/pucd7bdrx1cf1.jpeg?width=640&format=pjpg&auto=webp&s=e0f9e73227b10ef956994e53a1eaec16f79f21fa
[n2drt7l] (score 8, diepte 2) Oh, that’s foul they still tried to give it to you and your crew anyways.
[n2dco5h] (score 8, diepte 1) ![gif](giphy|U67CajqFIjiDSACi5i)
[n2fsp4p] (score 8, diepte 2) It's multi site wide lol same here
[n2e88g6] (score 8, diepte 0) I kid you not, they had superhero capes and make your masks. They said we could all be superheroes together...🤣😭 I passed...
[n2gnme2] (score 8, diepte 0) https://preview.redd.it/rto1gmj915cf1.jpeg?width=3024&format=pjpg&auto=webp&s=7721831b3215bdbc977f047a7d2a557da115bb5a

This is what we got 🤷🏼‍♀️
[n2hgqk1] (score 8, diepte 1) Fuck you.. respectfully
[n2e6vzp] (score 7, diepte 1) LMFAOOO
[n2da5mj] (score 7, diepte 0) You didn't get paid for those 12 hours?
[n2foh1y] (score 7, diepte 1) Same, that or we at the same site lol
[n2ddp85] (score 7, diepte 0) Never eat any of the food they handout, that crap comes from damaged out area.
[n2efrnt] (score 7, diepte 2) Nope, selfish assholes 😔
[n2evdzr] (score 7, diepte 0) You guys get Pop Tarts ?? We got apples and oranges.
[n2gr2r7] (score 6, diepte 1) 😭😭😭😭 I hate that I get this!!
[n2g6xf5] (score 6, diepte 1) This. Handing out expired chips the other day at mine.
[n2fd6wc] (score 6, diepte 0) 12 hours on your feet for a single pack of Pop-Tarts 💀💀. Corporate really said ‘here’s your gourmet feast, now get back out there.’ 😂 Hope you at least got the good flavor!”
[n2d26kn] (score 5, diepte 0) And that check
[n2d4j7j] (score 5, diepte 0) You got paid for the day, correct?
[n2ddvh7] (score 5, diepte 0) They rewarded you with your paycheck which is wht the agreement was for when you signed up. And for those last 4 hour they rewarded you with a higher dollar amount. Ay we cant put some type of age restriction on some of these subs? 12 hours and you probably aint even sweat once. Go to one of the other big chain warehouses and see how they rewarding workers lol.
[n2dh8bz] (score 5, diepte 0) Put that hoe in a toaster or microwave for a couple seconds shiiiii
[n2e6h6o] (score 5, diepte 1) wow...not even two Jolly Ranchers?
[n2ebx0l] (score 5, diepte 0) Don’t spend it all in one place…invest a little, pay down some debt and then use the rest to enjoy yourself 😀
[n2ga1m4] (score 5, diepte 1) I prefer the fruit, tbh my FC is hot asf, so it's a little refreshing
[n2ir356] (score 5, diepte 2) No fr 😭
[n2h61i2] (score 5, diepte 0) That’s awesome and you should be at least a little bit grateful
[n2dkwwx] (score 4, diepte 1) sundae is also an underrated flavor
[n2imhc6] (score 4, diepte 1) They all call it Snack Attack, I’ve been at like 6 facilities and it’s all the same 😂
[n2ek5pd] (score 4, diepte 1) No it doesn’t 😂😂
[n2fp2hk] (score 3, diepte 1) 😂😂
[n2fsjqh] (score 3, diepte 1) Where did you get this gif?!
[n2dq7vx] (score 3, diepte 1) ![gif](giphy|3o6nULk2LmNI30VMwE)
[n2i8rop] (score 3, diepte 2) Isn't it fun being old.
[n2f5wn8] (score 3, diepte 1) What are you complaining about? Didn't you agree to all this when you signed up to be born?
[n2gp58f] (score 3, diepte 1) They didn’t reward nobody with shit they worked for it and that’s what the agreed to when they signed up and for the last 4 hours it’s only a higher dollars amount if you’re at 40 hours trying to be the smart ass here and look incredible lost I want to say something else but you’re going to report it
[n2e3906] (score 3, diepte 0) Well don’t forget you also get paid
[n2evzf1] (score 3, diepte 0) It's free.
[n2fdl2m] (score 3, diepte 0) This is that Michelin-star reward program they talked about in orientation 😂”
[n2d1500] (score 2, diepte 0) Lmaooo
[n2dhmct] (score 2, diepte 1) Lol someone here doesn't know that any incentive they put out is going to give them bonuses you're you're not really understanding at the person who's literally just like this is making like anywhere from 50 to 70k to just  mess with you
[n2ekc4m] (score 2, diepte 3) Okay on this episode of not real
[n2gw1mb] (score 2, diepte 6) I mean one of the bonuses was that they will hold your balls when you are sleeping in the bed
[n2gwqf4] (score 2, diepte 7) Not many things go over my head but I can assure you this one did
[n2db03g] (score 2, diepte 1) S'mores goes pretty hard as well.
[n2g9xcg] (score 2, diepte 1) Squid🤣
[n2da3dr] (score 2, diepte 0) You're free to turn in your badge anytime you want 🤣
[n2dhngr] (score 2, diepte 1) Working in a Fresh FC in NYC, we do get freebies sometimes usually from unwanted orders (rarely returns) or items ASM/AMs put aside to boost morale. Even in summer where being hydrated really matters being on your feet for hours on end & walking several miles.

Like bottled waters from Amazon Grocery to Poland Spring (our local area water brand) & rarely Acqua Panna/Fiji too or small snacks. I seldom attend events but once a month at least we do have one day (for nights & day shift) where there’s snacks/pizza given out.

Yeah in the long run these snacks aren’t healthy as is anything in the expensive vending machines + dubious the quality of these things, but it does keep you going.
[n2dqj90] (score 2, diepte 0) Atleast they feed you my company hit our q4 goal the first week of December and rewarded us with 4 straight weeks of OT so the higher ups could get their bonuses. Upon doing so we ran out of work from January to February lmao
[n2dz6ic] (score 2, diepte 0) Amazon loves you
[n2e4qbf] (score 2, diepte 0) I assume you were not working for free. Most businesses provide a paycheck and that's it. But I guess people just like to complain.
[n2hbyis] (score 2, diepte 1) At a SSD? 👀
[n2e98sq] (score 2, diepte 0) Pop tarts the cheapest thing you can buy. Of course it's free. It's probably expired.
[n2eakc7] (score 2, diepte 0) they gave us ice cream yesterday
[n2edn70] (score 2, diepte 0) I got a Reese‘s buttercup. I do not like peanut butter😭
[n2eeo4k] (score 2, diepte 0) They gave you a check 😂
[n2eir6v] (score 2, diepte 0) Let me get a peice.
-irs probably
[n2sgdph] (score 2, diepte 1) We keep asking for fruit 😩
[n2ff335] (score 2, diepte 0) Its more than you deserve!
[n2fmset] (score 2, diepte 0) It’s honestly insulting. They probably make literal millions from prime. But give employees a bonus?  NO cause FUCK THEM, when you just give out cheap ass snacks that likely came from damageland
[n2g08mm] (score 2, diepte 0) “Wearing feet and legs” … you mean, work?  That you get paid for?
[n2ghxqk] (score 2, diepte 0) Atleast you got a reward js
[n2qtkss] (score 2, diepte 2) 😂
[n2hw69u] (score 2, diepte 0) Its not even a smores pop tart. What a joke
[n2iadbv] (score 2, diepte 0) Yalls site is still 12s? My site did 6 10s this year
[n2jb6ci] (score 2, diepte 0) I’d be happier without the snacks if they would pay us time and a half for working holidays like most places already do tbh or at least give us the grocery discount year round instead of at Christmas lol
[n2l3qqo] (score 2, diepte 0) I don’t want the free snacks or any shirts. Just wanna complete the shift, and go home.
(68 reacties met lagere score weggelaten)

