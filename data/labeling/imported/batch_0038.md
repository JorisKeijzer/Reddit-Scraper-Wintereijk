# Label-batch batch_0038

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
Schrijf het resultaat naar `batch_0038.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: hib5u7, 58whh3, 1xlgr7l).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD hib5u7 ===
SUBREDDIT: r/Frugal
DATUM: 2020-06-29  SCORE: 1606  REACTIES: 225
TITEL: Cheapest ATT plan for 1 line? Currently my T-Mobile doesn’t work in Alaska. Paying 75$ a month for no reception. ATT website isn’t straight forward for pricing. Photo of phone I found 30 feet deep diving for laffs.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[fwfbfwc] (score 618, diepte 0) I can’t help you with your phone service but I can help you stay hydrated.  If you’re on Lowell Point there is a random garden hose coming down the mountain, across the road from Storm Chasers Marine, that has the worlds best ice cold water. I have no idea how long the hose is. Or where the source is. It makes no sense as to why it’s there but it is, and I go to it every time I’m in town. I tell everyone I know. Fill up every jug in your possession.

EDIT: It’s been added to Google Maps

https://www.google.com/maps/place/The+Greatest+Water+on+Earth,+13560+Lowell+Point+Rd,+Seward,+AK+99664/@60.07665,-149.445401,15z/data=!4m2!3m1!1s0x56c79dbd373fc0f1:0x658ab50c141ac1b6?hl=en-US
[fwfc43h] (score 232, diepte 1 OP) This is the wholesome contact I come here for
[fwf3u0s] (score 159, diepte 0) Cricket (at&t network) is $55 a month for unlimited everything. They do have cheaper plans as well if unlimited isn’t important to you.
[fwf3z6k] (score 158, diepte 0) I've switched from sprint to Google fi and it has been good to me. Way cheaper.
[fwfjac9] (score 125, diepte 1) I think I found it!

https://www.google.com/maps/@60.0764951,-149.4453845,3a,15y,320.44h,83.01t/data=!3m6!1e1!3m4!1sQe8JRAj8An8UUXCNsjAhrA!2e0!7i13312!8i6656
[fwfjl2i] (score 117, diepte 2) That’s it!  That’s the hose!
[fwfgtr2] (score 82, diepte 2) I'm amazed this poster readily drinks from a hose of unknown source.
[fwffffn] (score 69, diepte 1) >I have no idea how long the hose is. Or where the source is.

It might be some mountain dweller pissing directly into your mouth?
[fwff2m9] (score 57, diepte 1 OP) Now if you know of any halibut fishing holes that are under 50 ft deep, you could really up my spearfishing game here.
[fwf3ytp] (score 54, diepte 0) Pretty sure that if that phone had been submerged long enough to be a home for barnacles, it's probably not going to be a good long term option.

Also - your TMobile phone might be able to work on the ATT network.
[fwf4ejz] (score 47, diepte 1) Same. My wife and I love fi. Bonus: if it doesn't work for you, there's no contract!
[fwfmpch] (score 40, diepte 3) Please keep us posted on this hose. I am intrigued
[fwf6dkk] (score 39, diepte 1) I’ve been very happy with Cricket, too.
[fwfg6l7] (score 38, diepte 1) r/HydroHomies
[fwf8j8y] (score 28, diepte 1) I agree with Cricket, I'm also in Alaska and it works great so far! I think it is $80 for both my husband and I, unlimited everything also.
[fwf6swk] (score 28, diepte 0) Mint is amazing. Not sure if it works in alaska
[fwf8gdk] (score 25, diepte 1) Mint is great but I doubt it will work in Alaska since it uses the T-Mobile network.

For those that are wondering, I pay $240 a year for unlimited talk, text and 8 GB of data per month (which I rarely use all of). Greatest phone plan I've had
[fwf9xhf] (score 25, diepte 1) Then boil it up nice and you’ve got yourself a nice seafood dish
[fwfbkcg] (score 23, diepte 1) the only options here in alaska are att, verizon, or gci. i’m in alaska with a cricket group of 5 unlimted and it’s $125 total per month. it’s att towers just throttled to 3mbps. i found the other 4 people online.
[fwf4lml] (score 22, diepte 2) We so got pixel 3s off of eBay In near new condition for a fraction of the price. Best phone move yet.
[fwf7m2n] (score 22, diepte 0) Throw the phone in a bag of rice
[fwfp8br] (score 22, diepte 3) Live a lil.
[fwf5rgb] (score 21, diepte 1) Don't cancel the plan till they unlock the phone for ya though.
[fwf7khf] (score 21, diepte 0) r/nocontract

Take a look at mvno like redpocket, h2o wireless etc for some good deals..
[fwg1uq0] (score 17, diepte 2) Inb4 it turns out the hose is a makeshift improvised septic tank leading to the ocean from whosever house owns it.
[fwfc04v] (score 17, diepte 0) Cell Phone Plan Comparison Chart Update Q2 2020! https://reddit.com/r/NoContract/comments/gsen5a/cell_phone_plan_comparison_chart_update_q2_2020/ 

courtesy of /u/stetsdogg
[fwfa9l6] (score 16, diepte 3) The 3s are stupid cheap for the money because the 4s came out so quick.
[fwf71l1] (score 16, diepte 1) OP said T-Mobile doesn't work.  So Mint on T-Mobile's towers won't work either.
[fwfjfpm] (score 16, diepte 1) On turnigan arm (on the highway going south from anchorage) there is a pipe that come out of the rocks that provides glacial water. Its difficult to describe the place exactly, but it will be on the left side of the road when reading south. Sometimes you will see others pulled off there filling gallon jugs. If you decide to try and find it please be careful! That road is very dangerous (especially during tourist season).

I almost forgot about your phone service: Get Verizon if ya can, 40 bucks a month for unlimited talk/text and 10 gigs. Month by month plan
[fwfdksi] (score 14, diepte 2) Cricket uses ATT towers
[fwfqgrh] (score 14, diepte 2) what about the godamn halibut hole! Isn't anyone gonna help this man on what's really important here. They gave you delicious water, but no gawd dam 'but hole.
[fwfx9rn] (score 14, diepte 3) Strange magical forest water > boring water
[fwf9wb9] (score 12, diepte 0) AT&T Prepaid. I pay $55/month out the door for unlimited everything. You just lose the tethering, which I don't use.
[fwfrqcq] (score 12, diepte 3) All this man wants is to get in somebodies ‘but hole.
[fwfy7qd] (score 12, diepte 2) I can confirm that the water is delicious and cold.  We filled up there on our trip last summer when we lived out of our Subaru for 60 days.
[fwf6xtw] (score 11, diepte 1) cell phones don't use satellites.............................
[fwfh724] (score 10, diepte 2) THIS IS REALLY IMPORTANT! Make sure it's unlocked!  CALL 611 BEFORE YOU SWITCH!  Plus, if you plan on keeping your number, don't cancel service.  Just bring your account number and pin to whoever you want to change service to.  You transferring your number will cancel the service for you.
[fwfp5lo] (score 10, diepte 2 OP) I know that mystery glacial water hose that used to come out of the mountain cliff between Indian and Girdwood. I’d drink from there sometimes in high school.
[fwfclh8] (score 10, diepte 0) My understanding was that living in Alaska, and living frugally are mutually exclusive concepts.
[fwf9grp] (score 9, diepte 1) I have Sprint...and I can barely get calls or look at any of the Apps on the iPhone 6s. I'm sick of their B.S. I have 13 months to go, and I am considering paying an early termination fee, hands down.

I would imagine the service isn't going to get much better now that T-Mobile & Sprint have merged.
[fwfahjl] (score 9, diepte 2) I got Sprint to wave the early term fee by complaining that I had basically no service at work and needed their booster at my house. Granted this was maybe 5 years ago and I had been their customer for 7 years or so.. gave them the line that I didn't want to leave, was their anything to be done to improve service, etc. I don't think I even got escalated, she just waived it and cancelled my plan with over a year left on the contract. Saw the light at Google Fi and would never go back.
[fwff5q8] (score 9, diepte 2 OP) You got yourself a stew, baby!
[fwg0jz9] (score 9, diepte 2) Wow I e never traveled to the west coast.... 

Google earth has mapped so much of the world and I just started clicking around and couldn’t stop... man oh man Alaska is beautiful.
[fwfd5mg] (score 8, diepte 3) Lol! Didn't think of that 😉 We're legally married, so there's a contract for that one!
[fwfec7k] (score 8, diepte 2) I’m on their absolute lowest plan (3 GB) at $180 for the year, $15 a month. Love those savings.

Only downside is it’s hard to leave because you have to pay up front to get that price. Don’t plan on leaving but I could imagine a scenario where it’s a problem.
[fwf869x] (score 8, diepte 0) Can you get visible there? Verizon subsidiary.
[fwfyojr] (score 8, diepte 4) Uncontrollable diarrhea <not having diarrhea
[fwff7xb] (score 8, diepte 1 OP) They can work if you fish and hunt for some of your food.
[fwfkhbe] (score 7, diepte 3) I second not cancelling your old service until your number has been ported but I would double check to make sure your old service is, in fact, cancelled and not just assigned an arbitrary new number.
[fwfkcxg] (score 7, diepte 4) >The 3s are stupid cheap for the money because the 4s came out so quick.

??? What on earth are you talking about? Google has released a new smartphone in the fall every year for at least 7 years in a row, almost exactly the same month.

> The [Nexus 5] was unveiled on October 31, 2013;

> The Nexus 6 was unveiled on October 15, 2014, with pre-order availability since October 29, 2014, and a delivery date in early November.

>Nexus 5X (codenamed bullhead) ... [was] [u]nveiled on September 29, 2015, it is a successor to the Nexus 5.

>[The Pixel and Pixel XL] were announced during a press event on October 4, 2016, and serve as the first smartphones in the Google Pixel hardware line, succeeding the Nexus line of smartphones.

>[The Pixel 2 and 2XL] were released on October 19, 2017, and serve as the second set of smartphones in the Google Pixel hardware line.

>The Google Pixel 3 landed on October 18, 2018 in the US, and November 1, 2018 

>Pixel 4 and Pixel 4 XL are Android smartphones from the Google Pixel product line, serving as successors to the Pixel 3. The phones were officially announced on October 15, 2019 and released in the United States on October 24, 2019.
[fwfd10b] (score 7, diepte 2) I know what you were trying to say, but it can be misconstrued depending on the reader, so I will clarify - there is no contract either way!
[fwf9f0y] (score 7, diepte 1 OP) Yes.  Did you lose your phone in the ocean? How many D pics are on this thing? If you guessed right, I’ll send it back to you.
[fwf8iy0] (score 6, diepte 1) US Mobile has plans on the ATT and Verizon networks as well. I pay 36/mo for unlimited calls / texts and 5GB of data. Unlimited is like 45/mo I think, but I don't need it.
[fwfj7ky] (score 6, diepte 1) Thanks for the mention :) Hope that helps people, the spreadsheet is awesome. Compares 223+ cell phone plans.
[fwf9dks] (score 5, diepte 1) To add to this you can get into a cricket group and have it cost $25
[fwf8oxe] (score 5, diepte 0) I pay like $35/month prepaid ATT - unlimited talk and text, 1GB fast data then slow data (stuff like Google maps and email works no problem for me after I hit my cap).  

Its the cheapest provider that I can find that can accept my area code - TMobile backs service for lots of them (like Mint and Ting I'm pretty sure) and TMobile doesn't service my area code, so I can't port my number.  I live in a different state from my area code, but I want to keep my phone number for sentimental reasons.  

I think rates vary by region, I'm in the Pacific Northwest.
[fwfpsr1] (score 5, diepte 2) A true hero!
[fwfbz39] (score 5, diepte 0) Look into visible.  Runs on Verizon and if you join a group from reddit, it can be $25/mo.
[fwfhb4j] (score 5, diepte 1) Frugal is very relative. It can be applied everywhere.
[fwfpxln] (score 4, diepte 1) Another happy cricket switcher.  Att gives the best coverage in our area, so when contact was long over, we made the switch.  I have a few niggles with some of their policies, but overall happy enough to stay.  I'm on an old 8gb @ full speed plan (until throttling) and can't complain.
[fwfc1wc] (score 4, diepte 3) THANK you....I am going to try this!!!!
[fwf7fhc] (score 4, diepte 2) Oops! You are totally right, I just read AT$T by mistake. Mint wont work.
[fwf6txv] (score 4, diepte 0) I pay $40 a month for Teltik. Unlimited text, talk and data. Uses Tmobiles satellites. 

I actually got ATT fiber installed recently and the guy who visited was asking which phone plan I had to try to sell me a cheaper plan. After telling him how much I paid and what I got for it, he just put his notebook down and gave up lol
[fwfj0wn] (score 4, diepte 1) Yes, came here to say this.  red pocket has att coverage for non-att price.
[fwfqtkx] (score 4, diepte 1) H2O sucked in Oklahoma. Wife wanted to go back to ATT.
[fwfp0z0] (score 4, diepte 1) In my head I read this in a thiccc Northern accent.
[fwfv1ke] (score 4, diepte 1) So I was to to plan a trip to Alaska, what town would I need to visit to drink out of this magical hose?
[fwfitu5] (score 4, diepte 1) Yo- thank you!!
[fwftmv1] (score 4, diepte 0) What about Verizon? I have pre-paid 3GB with all else unlimited, hot spot from that data, WiFi calling, and one month of roll over all for $35. The website says $40 but if you are cool with checking the box for auto billing they will do $35. Never had an issue with the auto billing system. Where I am Verizon is about all that works everywhere. There are cheaper plans but it is only cheaper by $3 at best and that was 1GB less if I remember plus was a company using Verizon towers, that puts your data priorities under pre-paid and that’s already under the main Verizon group...
[fwg51mz] (score 4, diepte 0) Hey bro nice shell phone
[fwfcan1] (score 3, diepte 1) Same, it has been way cheaper than paying for a single-person plan. But my service has been absolutely horrendous in SoCal. Lord help me if it's an overcast day as well, call drops 7-8 times a day, easy.
[fwfgwvs] (score 3, diepte 1) I love Mint! Switched over recently and can’t believe how much I used to pay
[fwfnvug] (score 3, diepte 1) Mint or Ting is what I'd recommend.
[fwfr996] (score 3, diepte 2) H2O runs on att towers. Possibly lower priority than direct att line based on congestion in the area ? Coverage wise should have been same (not sure on roaming though).
[fwfs09a] (score 3, diepte 3) Deprioritization so bad in areas you can't check email.  First time around, 90% of my calls would disconnect at the 15 minute mark.  Support entirely clueless. Texts occasionally takes days to arrive because you know the tubes are full.  Various other chaos.

Security is atrocious.  The account port-out pin is the same for every single customer - 1212 and not changeable and no secondary security eg email confirmation.  In other words, if I know your phone #, and Visible account number(which is an incremental value ie increased likelihood of being guessed given a bit of info, or I could just borrow your phone for a min if left out and unsecured), I could port out your phone number to any other provider and you could do jack-shit about it.
[fwfeydc] (score 3, diepte 1) Same, but I pay $40 before taxes & fees. I’ve been signed up for over a year. 

I have a smart phone and would hit the data cap if I didn’t have WiFi at home, but I don’t know what my limit is - sorry! They text me if I hit it. Did that once before I figured out the house WiFi was flakey.
[fwfbz9d] (score 3, diepte 1 OP) I saw it in a kelp bed. Lots of life growing on it
[fwfcuo7] (score 3, diepte 0) Nice limpets stuck to the case there.
[fwfxoy7] (score 2, diepte 2) I've been using US mobile, and yeah pay around 35 a month for what would be 60 on verizon
[fwfhuvc] (score 2, diepte 1) I’ve been paying 15 bucks for 2 gigs bc of covid so I really can’t complain. It’s a lil slower than att, because att customers take priority, but it’s the same lines. Coverage is 100% the same (according to them)
(144 reacties met lagere score weggelaten)

=== THREAD 58whh3 ===
SUBREDDIT: r/Frugal
DATUM: 2016-10-23  SCORE: 969  REACTIES: 210
TITEL: I Followed The 'Boots' Theory of Socioeconomic Unfairness & Finally Spent $$$ on Shoes.
POST (source_id=post):
> “The reason that the rich were so rich, Vimes reasoned, was because they managed to spend less money.

> Take boots, for example. He earned thirty-eight dollars a month plus allowances. A really good pair of leather boots cost fifty dollars. But an affordable pair of boots, which were sort of OK for a season or two and then leaked like hell when the cardboard gave out, cost about ten dollars. Those were the kind of boots Vimes always bought, and wore until the soles were so thin that he could tell where he was in Ankh-Morpork on a foggy night by the feel of the cobbles.

> But the thing was that good boots lasted for years and years. A man who could afford fifty dollars had a pair of boots that'd still be keeping his feet dry in ten years' time, while the poor man who could only afford cheap boots would have spent a hundred dollars on boots in the same time and would still have wet feet. 

> This was the Captain Samuel Vimes 'Boots' theory of socioeconomic unfairness.” 

&nbsp;

In a previous post, I asked about clearing the mental hurdle on spending more than a certain amount on shoes because when I was growing up, I never owned a pair of shoes above a certain price. 

I work in a office setting where I pretty much wear dress shirt, dress pants and dress shoes daily. Today, I ponied up to purchase 2 new pairs of Allen Edmonds dress shoes and the appropriate accessories to maintain them.

* Identified which pairs of shoes I wanted
* Purchased discount gift cards
* Bought today during a sale with discounted gift cards


This was the sale ad. I got the Park Avenue in Dark Chili and McAllister in Walnut. Both with dainite soles.. https://i.imgur.com/TBF3Vwj.jpg

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d93ri1o] (score 176, diepte 0) Well done, and a wave to a fellow Pratchett fan :)
[d93sw8h] (score 61, diepte 0) Congrats! I hope the shoes work out for you. I recently did something similar: I spent about $100 on a pair of good hiking boots for work and hiking (~$80) and a pair of wool socks (~$10). I love them both so far! Very comfortable and supportive. I was going to buy a pair of boots that were only $35 that were quite uncomfortable and lacked support, but several of my friends talked me out of it and said I'd be better off spending more money on a better pair instead. More durable, more comfortable and supportive (so fewer foot and back problems in the long run), etc. Very glad I did.   

I know an $85 pair of boots isn't really a whole lot of money, and there are certainly much nicer and more durable boots I could have gotten for $200 or more. But right now I don't have the money to spend on boots like that. One day, though! Either way I'm very happy with my new boots and all the reviews on Amazon (4.5 stars out of 5) say they're very durable and everything so I  think I'm good.   

How did you decide on what dress shoes to buy? I might need some new ones soonish. And what are discount gift cards?
[d943uol] (score 47, diepte 1) The philosophies of Vimes and Weatherwax are central to my life.
[d93webu] (score 46, diepte 0) we recently did this for my husband.  he really loves one particular style of slip-on loafers, and so he's bought cheap ones that he can work in (he works in a kitchen) but they fall apart within months.  he's had them from $20-50 and bought them over and over, then wears them till his socks are sticking out and he's tripping over the broken soles.  finally for his birthday i got him a really nice ecco pair in his style that was comfortable with a good grip on the sole.  he hasn't had to buy any shoes this year and all they take is a quick cleaning and buff to look brand new.  it hurt spending over $200 on the one pair, but it's definitely paid off and he can make them look spiffy for a night out anytime.  when the soles start to go in a couple years the cost of resoling them should be far cheaper than buying a new pair, also.
[d9471jp] (score 29, diepte 3) For Vimes, read in this order:

Guards! Guards! 

Men at Arms

Feet of Clay

Jingo

The Fifth Elephant

Night Watch

Thud! 

Snuff

The philosophies and questions raised by the early ones focus on how to be a good man in a corrupt world,  while the later ones focus on themes of how one should use power to protect those with none. The best writing and the grandest themes are found,  in my opinion, in Jingo and Night Watch, while the absolute best story for the buck is The Fifth Elephant. The stories really do build on each other,  though, so I would strongly recommend reading them in order. 

Granny Weatherwax novels explore similar themes of doing right regardless of circumstances, especially when you don't know the right course and must depend on instinct and principles in the face of uncertainty. Witches Abroad is a masterwork, weaving dozens of cultural stories into a meditation on the nature and power of stories. The Weatherwax novels don't need as much backstory as the Vimes stories, so jumping around is OK,  though I would recommend reading Witches Aroad,  Carpe Jugulum,  and Lords and Ladies in order.
[d947owh] (score 29, diepte 1 OP) Definitely was not an inexpensive purchase. Most of frugal would cringe at what the price turned out to be.

Because the shoes and accessories were on sale, it "only" came out to $622 after taxes. What really helped for me was I purchased $600 worth of gift cards for $463. So in total, I spent $485 for two pairs of AE firsts, appropriate accessories to maintain them and sales tax when only the two pairs of shoes themselves would have run me $490 not including tax during the sale.
[d9458ih] (score 29, diepte 0) I'm 34 years old. When I was 17 I needed new winter boots and asked my mom to get me some for Christmas. I really wanted some Lands End boots because they should last a long time. 

I still wear those exact boots every winter. My only regret is that 17 year old me chose pink.
[d946r9l] (score 28, diepte 3) http://www.lspace.org/books/reading-order-guides/the-discworld-reading-order-guide-20.jpg

Read the Witches series for Weatherwax, and the Watch series for Vimes.
[d93y4hb] (score 26, diepte 2) Wool socks are probably only for hiking.
[d9412cg] (score 26, diepte 3) That totally makes sense. 

It may be worth your money to buy a cheap pair for him to alternate with. The cheap pair will also last a bit longer.

Another option is to buy a used version of that same shoe (or another model by the same company) from eBay. 

I hope my advice isn't condescending D:
[d93yvnp] (score 25, diepte 0) First of all, YAY FOR TERRY PRATCHETT.

Secondly, it's definitely better to buy good quality, lasting shoes. In the long run, you spend less not only on shoes but also on your foot health (and oftentimes on the rest of you health too.)

Unfortunately being a woman it's a bit more complicated for me than just 2 pairs of dress shoes, but I have built up a wardrobe of appropriate business casual shoes bought frugally that will last and last - a pair of black ballerina flats (leather, well padded), a pair of black heels (leather, well padded with insoles in there to help my poor feet), a pair of black loafers (suede) and a pair of black ankle boots (also leather.) Each of these pairs of shoes can be worn for business casual or for more casual outfits, is comfortable, and is going to last - the heels I've had the longest and they've survived a long time already.

Women's footwear has 1,000,000,000,000 options, many of which are super appealing, but ultimately kinda useless and not worth the money. Are there shoes that are visually more interesting than my black ones? Yeah, for sure, but I'm not going to pay 40$ for a pair of shoes that I can only wear with one pair of pants and one other colour.

tl;dr invest but also PLAN and make sure that your shoes match everything
[d942ock] (score 24, diepte 0) "Captain is such a dashing title, I've always thought.' She gave him a bright, brittle smile. 'I mean, colonels and so on are all so stuffy, majors are pompous, but one always feels somehow that there us something so delightfully dangerous about a captain."
[d949shj] (score 22, diepte 2) I'm glad that you (seem to) know that being frugal doesn't always mean being cheap. Those shoes will pay off dividends to you for years in comfort, style, and orthopedic health.

I'm actually saving up for a pair of Danners boots myself.
[d93y52l] (score 22, diepte 5) So basically you're making this up. Why do people feel the need to do this?
[d93xrhh] (score 21, diepte 1) How are you making do with 1 pair of socks for work?
[d94fglk] (score 20, diepte 3) Do you wear dressshoes 5 days a week 10 hours a day? I bet they are this guy's work boots. Uncomfortable shoes can make your day pretty miserable no matter the style.
[d940zr2] (score 20, diepte 2) yeah i know but we don't have another 200 to spare, you know?  in the future though, this will be a method we use.  thanks for looking out.
[d93y8j4] (score 17, diepte 1) He isn't wearing the shoes back-to-back, is he? If he "rests" the shoes 24 hours between wears, allowing the pair to dry, they will last a lot more wears.
[d93ytcx] (score 17, diepte 1) This depends heavily on where you live. I have never, in my life, seen a decent pair of shoes at a thrift shop.

Additionally, your foot imprints on the midsole, which means you pretty much immediately need to send them for recrafting once you buy them second-hand. And, frankly, I've heard too many foot fungus horror stories to risk it myself.
[d9442w6] (score 16, diepte 0) My Nan used to say "buy cheap, pay twice." It's the same principal, right?
[d93wk26] (score 15, diepte 1) I agree that buying good shoes should mainly be to prevent injury due to crap shoes.  I made this mistake in the past and had heavy foot and ankle pain.  I might have saved money buying cheaper but cost much more in productivity lost.
[d942gw0] (score 15, diepte 2) I'm a little skeptical that resting them for ten to twelve hours at night wouldn't be enough.  Everything I've seen on this can be traced back to an advertiser or a magazine that wants me to buy more shoes!
[d944qpq] (score 15, diepte 0) My boss noticed that my shoes were crappy, so one Christmas he bought me a pair of Mephistos. I've worn those shoes almost daily for ten years now and they are still going strong. They may have cost $350, but averaged out over ten years it's only $35 a year for the best shoes I've ever owned.
[d943gwt] (score 14, diepte 1) I read somewhere (pretty sure it was here), that "never be stingy when it comes to buying stuff that separates you from the ground, and that includes mattresses, and shoes".
[d94h1xe] (score 13, diepte 3) Cheap fake leather work shoes are $50-100 and last 8 months and smell like hell the second you sweat in them. These will last op a decade or longer and the sole can be replaced when it wears out. 

I spent the money on real leather just to stop having smelly shoes. Huge difference
[d942yvb] (score 13, diepte 3) What kind of socks are you wearing? 

I've started getting some of the performance wool clothing (including socks) and I can go a week on them with no notable smell.

Icebreaker socks also have a lifetime warranty now, so I'm not worried about wearing them out.
[d9453qf] (score 12, diepte 3) You cheap out on buying the most comfortable and high quality rugs and doormats‽ *gasps*
[d942zbk] (score 12, diepte 3) Personally I'm less of the opinion that resting is required, more that multiple pairs will extend the lifetime by allowing a rotation
[d945y1c] (score 11, diepte 5) Darn Tough wool socks also have a lifetime warrant
[d93uim3] (score 11, diepte 0) I too have two pairs of Allen Edmonds. The ability to have them resoled is the best part.
[d946tyi] (score 11, diepte 1) My husband got a North Face jacket for his 17th birthday. He outgrew it after college and gave it to me. Granted, we live where winter lasts only three months, but the jacket is like new and is 30+ years old!
[d94a7hg] (score 10, diepte 4) Here's another version, which includes both the order of publishing, and separate story lines, and includes the final discworld book of The Shepherd's Crown (it makes me sad to type final...)  http://www.epicreads.com/blog/the-official-discworld-infographic/
[d93y2pk] (score 10, diepte 2) Not the person you asked, but I have the same question. I go through two pairs of socks most days at work.
[d942qru] (score 10, diepte 3) My advice is common fashion advice (you can go to /r/goodyearwelt to check). However, a cursory Google search failed to shoe any scientific evidence supporting this advice. Now, I'm not really sure what to believe.
[d93zw92] (score 10, diepte 2) >I've seen several pairs before, but they've always been extremely worn down.

Or dry and cracking. Or loafers. I'm not sure what's worse.
[d9479ix] (score 10, diepte 1) I've also heard "buy it nice or buy it twice."
[d948ss4] (score 10, diepte 0) Be warned, this is the same rationalization people make when buying $100 designer t shirts and jeans.  Often statements are made that they "fit" better etc.
[d946ey9] (score 9, diepte 2) Which books are these? I've loved everything I've read by him.
[d946rvw] (score 9, diepte 3) The Discworld series by Terry Pratchett. Easily my favourite series. I suggest starting with *Guards! Guards!* -- if I'm remembering correctly, earlier in the series he was kind of just dicking around, so the earlier books are kind of all over the place. But *Guards! Guards!* will get you started on the Vimes/Night Watch arc, which is easily my favourite.
[d946xic] (score 9, diepte 5) Sweaty feet here too, I have 2 pairs of the same shoe that I wear on alternate days , as I heard letting the shoe dry for 24 hrs help to reduce bacteria & odour , seems to help...
[d93zyc1] (score 9, diepte 6) One time I went to the store and there was a model there and she said I was handsome and gave me her number and then everyone clapped and chanted my name and then the manager came out and gave me $5.
[d93xn65] (score 9, diepte 0) I work from home, and buy my own office furniture. I bought a cheaper computer chair when I first started, with very little warranty on it (about $60). After a few months, the hydraulic pump that raised and lowered the seat gave out, and I decided I wasn't about to get stuck in a cycle like this.

My current chair is a replacement that cost $0, because the warranty I purchased for the previous chair covered the entire cost. I have a warranty on this one as well, and if any tiny hint of wear happens to it, I will be trading it in. 

Never buy cheap for things like this. You'll end up spending way more than you saved.
[d946wn8] (score 9, diepte 2) My boss is generous, but then again he can afford to be generous considering how much he is worth.
[d947j8d] (score 8, diepte 7) Into the wool, which is now not in contact with your foot.
[d944dln] (score 8, diepte 4) I wear the heels out of every socks I own. Are you telling me I can keep getting these icebreaker socks replaced when I wear out the heels?
[d947dul] (score 8, diepte 4) I cheaped out on a doormat once. I had to mop every other day.

NEVER AGAIN
[d942mvr] (score 8, diepte 4) nope!  totally great suggestions.  thanks!
[d93xsx2] (score 8, diepte 0) Good on you. FYI, Allen Edmonds shoes are not unusual to find at Goodwill and thrift stores for only a few dollars
[d94an4e] (score 8, diepte 2) or "not rich enough to afford cheap things."
[d94ab2b] (score 8, diepte 0) Obligatory /r/buyitforlife pitch...
[d945l0m] (score 7, diepte 4) I work on film crews. Boots all day. Indoors, outdoors, summer or winter. I'm almost always wearing wool, but my feet sweat a lot. I take my boots and socks off at lunch and then I puton a new pair of socks after lunch. Best feeling, but I wish my feet didn't sweat so much.
[d94c5si] (score 7, diepte 6) I wore darntough socks for two years working outdoors 14-20 hours a day 20 days a month in North Dakota. Never needed to request a new pair. Quality socks made in a lot of different weights so you can find pairs for all seasons.
[d9447s9] (score 7, diepte 2) Hmm. Cars, check. Airplanes, check. 

Floors, chairs, yoga mats, toilets, couches, rugs, doormats, trampolines? Some, maybe. I suppose I shouldn't take the metaphor too far.
[d93wwze] (score 7, diepte 2) He's lying
[d946ihe] (score 6, diepte 1) If you want to be fashionable, obsolescence applies to shoes as well.

Luckily, the standards of good-looking dress shoes for men haven't changed much in a few decades, though time and place may affect what's trendy.
[d94852p] (score 6, diepte 1) Talking in the third pers[o](http://i.imgur.com/J2vR6Oe.jpg)n are we Sybil? ;)
[d94bfe9] (score 6, diepte 0) It's also called, "being penny wise, but pound foolish."

For those that don't know, it means like what your example says, Boots spends money on cheap shoes to pinch some pennies now, but he'll just to have to spend more money within a few months to replace the cheap and broken shoes, So he may end up spending $100 over the course of a few years, whereas had he just spent $50 one time on good boots that last a few years, he would have saved himself that extra $50...and the shoes may even last longer and save him even more. 

Some people care so much about how many pennies they're saving, that they don't see the bigger picture and realize they're actually spending more in the long run. My parents have this problem, especially my dad. They will buy the cheapest crap, just to end up having to replace it a lot sooner and more often than had they spent just a little bit more and bought a higher-quality item.
[d94e7qe] (score 6, diepte 0) Can we please dispel this myth that cost is a correlative to quality? I'll give an example.

I used Kershaw pocket knives for years. They were made in the US using US steel. Then, over 4 years, they switched 70% of their manufacturing and steel sourcing to China. Those knives are trash now. Useless. And yet they upped their prices. 

Please folks, don't just look at price.
[d9470y3] (score 5, diepte 4) Awesome. Thanks!
[d949bns] (score 5, diepte 4) Night Watch was the heaviest hitting and most memorable Discworld book I've ever read. It really stands out on its own, and remains my favorite in the series.
[d945sxz] (score 5, diepte 5) Try wearing dress socks underneath the wool and see how it works for you. It will help keep the moisture off your feet.
[d94bj5c] (score 5, diepte 7) http://www.zerowastehome.com/2013/02/how-to-darning/

http://theradicalhomemaker.net/farm-views-and-politics/how-to-darn-wool-socks/
[d943cyj] (score 5, diepte 6) Yes, I think this was the point I was making about this advice.  That it might just be total rubbish. :)
[d945ibk] (score 5, diepte 1) Ecco shoes are great,  and some of the most comfortable I own.   The problem is that the soles go out while the uppers still look great. 

As I recently learned, local shops won't resole these because of the way the soles are bonded to the shoe.  There are a couple of places online who say they can do it (http://www.nushoe.com/ecco-shoe-repair.html) but I haven't tried that because I was able to get new shoes for not a lot more.

I don't know which shoes you bought,  but I've never paid more than about $100 on amazon for ecco loafers - I checked my order history and the last two pairs I bought were $75 each (vs. 140 at the store)....but you may have gotten a different/better shoe.

Edit - to clarify,  nushoe.com cost to resole is $75 plus shipping http://www.nushoe.com/traveler-nucraft-shoe-repair.html.  Might not be worth it for you.
[d94ba2g] (score 5, diepte 1) Chairs are even worst, because health-issues come in to the calculation. Back-issues and sympoms originating from blood circulation can become very costly on the long run.
(146 reacties met lagere score weggelaten)

=== THREAD 1xlgr7l ===
SUBREDDIT: r/BuyItForLife
DATUM: 2026-11-01  SCORE: 124  REACTIES: 198
TITEL: Men's winter slippers that feel like a warm cloud
POST (source_id=post):
I'm tired of spending $25-$50 every year for a pair of basic house slippers. I used to have a pair of UGGs back in the day that were fantastic but I've heard their quality is no longer top tier. I tried glerups but I found them too boxy and just didn't fit right. Most shearling insoles are nice to first step into but the synthetic materials make my feet sweat without fail. I do love sheepskin but am hesitant to spend much more than $100 as genuine sheepskin flattens significantly over wear and time.

So what do you guys recommend for the most comfortable/warm house slippers for this cold season? I'm not exactly looking for a buy it for life  
recommendation but certainly something that can at least last a few years especially at a premium price. Cheers!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[19s016ve71ryd] (score 189, diepte 0) Wicked Good by LL Bean. I average a decade on a pair.
[19s02h8lw3utg] (score 68, diepte 0) Glerups and I am not a “slipper guy” … but I am now
[19s0361mdsfk0] (score 43, diepte 1) It's not controversial, everyone hates this suggestion.
[19s01k31br5c2] (score 26, diepte 0) You should look up the UGG scandal and look at Since 74 - the original Ugg makers.  I have 3 pairs of Since 74s and wear them every day.  Love them.
[19s03gprvdneo] (score 23, diepte 1) I was NEVER a slippers guy until I tried Glerups. They keep my feet warm but never sweaty
[19s01r6y5iaio] (score 22, diepte 1) Had mine for almost a decade. The inside isn't fluffy anymore but the outside still looks new
[19s01fqcat3ut] (score 21, diepte 1) I have 3 different pairs and I just rotate them depending on my mood. I’ll wear them from October to April non-stop.
[19s09zm3dkuyp] (score 21, diepte 1) I had them and really liked them. Ordered a new pair last year, same size, yet they were too tight. I compared the rubber bottoms of the new against the bottom of the old and it was a half inch shorter.  
Then they charged me $10 to return them. I’d been a life-long customer but that really pissed me off.
[19s03l2y3mim8] (score 20, diepte 1) As an Aussie, the "UGG Since 1974" or "Ugg Australia" brand are pretty much the only ones worth dropping BIFL money on. They're botb Australian made, and the Ugg Australia brand operates their own tannery. (I've had a Since 74 pair for the last 6 years and they're still in great condition) 


The US Ugg brand (owned by deckers) seems to have way lower quality in terms of materials and manufacturing. 


Ultimately, it also depends on how you want to use them. If you're wearing them to the beach to chuck on after a surf, they're going to be a disposable item after a few years of wear. If you're pottering around the house, they'll last forever.
[19s02pknha1fo] (score 19, diepte 0) Olukai. I love in Oregon I love my slippers I can wear them in the rain.
[19s02qnjucs01] (score 19, diepte 0) I have wide feet and have had the same problem for years. This year I ended up buying a pair of sneakers dedicated for inside the house only. You may want to go that route
[19s0aaaedp0at] (score 12, diepte 2) You can buy replacement shearling insoles relatively inexpensively - if yours are able to be taken out - it can give new life to them.
[19s01p8zi5134] (score 12, diepte 0) I’ve had my Birkenstock Zermatt (suede) slippers since 2022. Wear them literally all day almost every day (work from home) and they are still so comfortable and supportive. They make a shearling lined version that I’ve been eyeing, but they also have a slightly cheaper version with a cozier top, cushy bottom, and shearling lined as well. I’ve had the Kirkland Signature version of Ugg slippers the last couple years, but I notice if I wear them throughout the day and walk around the house, my back hurts. So I don’t think they’re as supportive even if warm.
[19s02tm76sczl] (score 10, diepte 2) When mine get like this I bust out the super fluffy socks
[19s04mts5vutd] (score 9, diepte 2) Do you ever clean and brush it? Mine is still fluffy.
[19s022zumpqyq] (score 9, diepte 0) I’m very happy with my Minnetonka moccasins.
[19s09e2yfedhd] (score 9, diepte 1) Only slippers I have owned that don’t stink after a few months. Just smell like a barn which is acceptable.
[19s01kjtuohxd] (score 8, diepte 2) Putting a third vote in for these
[19s05gddt6ldu] (score 8, diepte 1) I call them my winter flip flops
[19s038vf4tigz] (score 8, diepte 2) Loooool I’m cracking up. It is super ugly but I have the stinkiest feet ever and it’s so nice to have a shoe that insulates but dries quick after a wash, with socks that do the same and are anti-stinky.
[19s07r0u97nb7] (score 8, diepte 3) Because they are wool
[19s07p1pyacap] (score 8, diepte 0) North Face thermoball bootie! I had a pair since 2017 and i just replaced them a few days ago for another pair!
[19s08mtug4vyb] (score 7, diepte 2) Thank you for this- I have had my UGG slippers for 30 years and now I can finally lay them to rest because I can replace them
[19s1fw17ajzy8] (score 7, diepte 0) I wish I knew slippers that aren’t hot. Everything I buy is hot fleece foam bullshit that makes me sweat.
[19s0xu5e8zhdx] (score 6, diepte 2) Even though there’s capacity, they don’t make a lot of that stuff in America anymore.
[19s01u0909k8y] (score 6, diepte 0) Controversial but lined crocs with nice merino wool socks
[19s03ua7gd7ep] (score 6, diepte 2) >They keep my feet warm but never sweaty

Yes! how do they do it?? Gotta be the felt.  They're miraculous!
[19s04o1ife400] (score 6, diepte 1) >I tried glerups but I found them too boxy and just didn't fit right.
[19s13vn7lqymd] (score 6, diepte 0) Sorel leather house shoes. Five years and still going
[19s04g4c3pmtg] (score 5, diepte 1) This should be higher up. I have different ll Bean slippers but I average close to 10 years with them
[19s0i4pl002ww] (score 5, diepte 1) OP mentions in the post that they didn't like Glerups.
[19s02v65ien5x] (score 5, diepte 0) Glerups. I love them. They are shaped well and they keep my feet a perfectly comfortable temperature. 

Slippers I had before these may have been soft but had no decent form and they either did nothing to keep my feet warm or had them sweating in 5 minutes.
[19s04pxeps6v5] (score 4, diepte 3) Nope not at all but I've worn them a lot.
[19s02qgko2cap] (score 4, diepte 1) I also have these and they're amazing.
[19s03affplhvn] (score 4, diepte 1) Mine developed a hole in less than 3 years. I liked them though. 

I only wear them in winter in the backyard.
[19s06p8lyzsuc] (score 4, diepte 1) I got a pair last year. I wear them year round basically (they’re my inside shoes). I’ve almost worn them through, but they’re amazing
[19s03al7wvtfk] (score 4, diepte 3) LOL. I exclusively wear wool socks for that very reason.
[19s02gzoreshu] (score 4, diepte 0) Olukai moloa slippers. Spendy, but worth it.
[19s0i56cez1z8] (score 4, diepte 3) Usually barefoot
[19s0dfxl7hfb4] (score 4, diepte 2) They're amazing. Bought myself a pair, then bought pairs for my Dad and son. Then my wife picked up a pair. Everyone thinks they're amazing. And you have the option to fold the backs down. I highly recommend these!
[19s04pdptuk78] (score 4, diepte 1) >I tried glerups but I found them too boxy and just didn't fit right.
[19s05667vzf7p] (score 4, diepte 0) I’m going to toss Kyrgies into the ring. My son and I love ours. Since they are made with felted wool, you won’t have the issues you mentioned when wearing synthetics. They have many options, most of them for under $100, plus if you’re a new customer, there’s a 15% discount to be had 

https://kyrgies.com
[19s07zwnn7744] (score 4, diepte 1) Second these, honestly sometimes they are a bit too good and my feet get sweaty. Still worth it. You can routinely fine them on sale too.
[19s094lxwokow] (score 4, diepte 0) I don't know if they'll be BIFL, but I've recently picked up a pair of Kirkland (Costco) brand shearling slippers, and I have been absolutely loving them.
[19s1gl8x7yt36] (score 4, diepte 1) I swear slippers have two modes: falling apart in three months or surviving an entire generation.
[19s1g8xk0a400] (score 4, diepte 0) My uncle gave me a slipper fuzzy-lined version of Birkenstocks, I will frequently wear them to the store without realizing because they’re so comfy
[19s1b1ltlf2dd] (score 3, diepte 1) I was gonna say the Boston Sherpa lined, but the Zermatts are a really good choice, too.. more "housey" for sure
[19s02yc93fow4] (score 3, diepte 1) My acorns are in near tatters after 2-3 years, maybe a familiar story of declining quality and private equity
[19s12siul7r9c] (score 3, diepte 4) Wow. And they don't get stinky? Wild! I may have a new item fory Christmas list. 

Thank you!
[19s03afwqnkqr] (score 3, diepte 1) Atra, Topo, Brooks? Who's your go-to for wide feet?
[19s05cpq9lccl] (score 3, diepte 2) Atra is good for wide feet. They’ve also got wide toe-boxes which are supposedly good for preventing both bunions and bunions pain 

Brooks generally isn’t good for wide feet. They also don’t have wide toe-box shoes
[19s0bpbl9xqrl] (score 3, diepte 3) Altra has been a godsend for my arthritic big toes. Lems is another good brand for this specific purpose.
[19s08b5eq56m9] (score 3, diepte 2) I switched to Altra’s a few year ago for running and it’s made a huge difference.
[19s0906tv0vk3] (score 3, diepte 2) Brooks EE width. I've had success with New Balance also but I was fitted for Brooks several years back and once I found something that works it is very hard to switch brands.
[19s02vg1ffsub] (score 3, diepte 0) Crocket & Jones Albert Slippers or New & Lingwood Eton Slippers - both are genuinely BIFL as long as you look after them
[19s05ia4b3gsi] (score 3, diepte 0) Ll bean shearling lined. Yw.
[19s06n90brver] (score 3, diepte 0) LL bean moccasins, shearing lined, bison leather. My slippers for life. I’m on my third pair in 20 years and basically wear them daily as slippers/house shoes. Love them.
[19s01fjparutc] (score 2, diepte 1) Got a pair of Ugg bedroom slippers for a Christmas gift almost 9 years ago.  They will need to be replaced soon but to last almost a decade?  Worn every single day?  Not too shabby imo.
[19s1603h0wath] (score 2, diepte 2) i had a pair about 5 years ago. the footbed was matted and meh after one winter, they looked great, were kinda warm, but i didnt have much luck with an insole or anything. 

ive switched to just wearing adidas comfort slides and whatever weight of socks suits me best for the season. i wear them a ton,  the cushions will wear on me after many months and i can get another pair for 15-20 bucks
[19s05liahucap] (score 2, diepte 1) My go-to slippers. I put in good arch supporting inserts; this also tightens up the fit. I use a suede brush on the slippers’ exterior.
[19s0sco6yfxs5] (score 2, diepte 1) I got a leather repair kit and it's relatively easy to take the whole slipper apart, gently wash all of it, and sew them back together with new shearling insoles. This is the leather bottom booties. The leather already has holes awled in it, it's an easy lay-up 🙂
[19s0z4dgfc1q8] (score 2, diepte 1) I wear them out in one year which is why they only have a one-year warranty these days. 

They don’t have the longevity they once had.
[19s01xqd10c75] (score 2, diepte 1) I like the NF Thermoball but they are not BIFL, there is a cardboard layer that gets wet really easily and when it does they are basically done.
[19s1qqndj9mtd] (score 2, diepte 2) Thank you so much for this info! My wife wants a pair of Uggs for Xmas so I'm gonna be thrilled to give her some decent ones! Have a question if you have time - I was looking for the Made in Australia Uggs and have come across two websites (for USA shipping) - originalaustralianugg.au and sheepskindownunder.com which was the international shipping page redirected from uggaustralia.com.au

Are these both legitimate websites (to your knowledge)? Because they don't seem to be the same thing, but they are both using the Ugg brand. Would really appreciate it if you had any insight, thank you again for what you already shared!
[19s1r1xgiij0g] (score 2, diepte 3) No idea, sorry man. 


In Australia, Ugg is a genericised trademark, so anyone can use it.
[19s1s1s6l71z9] (score 2, diepte 4) No worries, figured it was a bit too hyper-specific for someone to be an expert on lol. I want to trust the first site, but it seems shadier with no actual mention of materials used or anything, so I’ll probably just stick with the second couple. Thank you again!
[19s01zks429xh] (score 2, diepte 0) [Acorn slipper socks.](https://www.acorn.com/collections/best-sellers/products/the-original-acorn-slipper-sock?_su_rec=DK1P86C2xQDddTvvby21yOiGLo1xe60LG7EbxDQ8lSoBJxdvBErnZ4iEt37YooZpsxuT8eXNmecyEDYiADAVTGrdFN-NwM7NQCnng3cUkKUvYEqKZKqphJm98NPWrIR8j4vEEyMKK6aRZpZ2AO0osW0d_q4ev0AqjHnh9XddG2PYL3yO0meDfif7V6z2cGvlFi6zAiECl2nz8cl35hbvMhWzXirnuznBZRNvzTbbX8n-IUVMiFECAvafQgrETucW8jdAsOeCbDlCZa-oOMn0JelUivdCmwcGb398erbyW6xMFmIP0T8CKM9SV2G-g6XEaOWRWm1WfU3L9gxmXTw3YBH-AS73kHyGfTMjxZQ&_su_rec_id=1a6b7282-235b-40a7-a7d0-c8b37ddc8a65-1793574414)  I’ve had mine about 15 years, same pair, other than the soles darkening they are the same as when new. Definitely a bifl item. Very warm and comfortable, I’ve given many away as gifts.
[19s07w2cnccsj] (score 2, diepte 1) These looks very similar to kyrgies
[19s18jt2ree9u] (score 2, diepte 5) Wool is natrually antibacterial and does a great job at keeping odors down. If needed it can be spot cleaned and left to dry in the sun, which deals with everything but the worst odors.

I have a pair of glerup boots as house slippers and wear them nightly with socks during the colder months.
[19s0fy1k7bnib] (score 2, diepte 1) I like mine but will say they've only held up decently for me. I've had mine 3 seasons and am about ready to replace them. I've got a few large holes in them at this point and the bottom has started to separate. 

Also worth noting that some wool often ends up coming out when I take them off leaving fuzzies throughout the house.

All that said, I'll likely buy another pair. Maybe two so I have a pair to slip on for stepping outside.
[19s0i9xk6o4hu] (score 2, diepte 1) I have a pair and they're really great
[19s0ialuidnlx] (score 2, diepte 1) Wouldn't work for me, my feet need to breathe!
[19s03008aez0g] (score 2, diepte 0) Nothing is softer and comfier than Crocs Mellow Recovery Slides and Oofos slides. (Sorry not winter but in house)
[19s05bw3wfu82] (score 2, diepte 0) Vionic had very supportive slippers
[19s06y4k41ebn] (score 2, diepte 0) I bought my parents some Minnetonka sheep lined moccasins. After digging for reviews, enough people seem to get a decade out of them and buy again
[19s07z4yi8dz6] (score 2, diepte 0) Quoddy's [dorm boots](https://www.quoddy.com/collections/holiday-slipper-closet/products/1763131) are extremely comfortable and warm. I've been wearing the same pair during the fall/winter season for 3 years now.
[19s0vbnqpx0oy] (score 2, diepte 0) I love my Birkenstock slippers
[19s14f6bel7ep] (score 2, diepte 0) Am I their private equity now, but my Birkin stock cork sold shoes are the best I’ve ever had. Rubber outsols and they’re not blazing hot on the inside, but they also give me foot support in a way that other house shoes never do
[19s1e9ckpvnpe] (score 2, diepte 0) I've been walking around the house on these for nearly 10 years now.  
[https://www.otto.de/p/haflinger-lemmi-lammfell-hausschuhe-stiefel-unisex-hausschuh-CS077H0VB/?variationId=S077H0VBD6KJ#](https://www.otto.de/p/haflinger-lemmi-lammfell-hausschuhe-stiefel-unisex-hausschuh-CS077H0VB/?variationId=S077H0VBD6KJ#)

Here's an Amazon listing for a slightly sharper price : [https://www.amazon.de/-/nl/dp/B004UPIDWI?dib=eyJ2IjoiMSJ9.JbasQ-nDvbQGeVRBwMvyDr2Jro1qSmC6aCY1z\_M\_SmYOkpRCfR5MKj7UyJASg4JZru\_83P1qUA1c9JdH95xl-ThssBAg0t2EcKClNyUjQp4JOFgsgJJWRrMfbVqM4-HLzTMSXka850Pw6FTNmHo4Y9c1-0z4krGWH5K1F2VToxL01L\_jpD4RjF0jgKSJO4x4id1u0GRZHsuqWo65j81bdE5-xuVsI0K8GqPlccQGV91eVA1UWYthSW7Um28yk5xLsp1RiQfkbyE8DgUeK7pLGlsApkNzwMH8sZq5QlGnno8.R5W8TPgwCrrsa3uV5Jkv\_NRaz8uDMQPGwJbS3NUAAAY&dib\_tag=se&keywords=Lammfell%2BHausschuhe&qid=1793639280&refinements=p\_n\_size\_two\_browse-vebin%3A1872403031&s=shoes&sr=1-15&th=1&psc=1](https://www.amazon.de/-/nl/dp/B004UPIDWI?dib=eyJ2IjoiMSJ9.JbasQ-nDvbQGeVRBwMvyDr2Jro1qSmC6aCY1z_M_SmYOkpRCfR5MKj7UyJASg4JZru_83P1qUA1c9JdH95xl-ThssBAg0t2EcKClNyUjQp4JOFgsgJJWRrMfbVqM4-HLzTMSXka850Pw6FTNmHo4Y9c1-0z4krGWH5K1F2VToxL01L_jpD4RjF0jgKSJO4x4id1u0GRZHsuqWo65j81bdE5-xuVsI0K8GqPlccQGV91eVA1UWYthSW7Um28yk5xLsp1RiQfkbyE8DgUeK7pLGlsApkNzwMH8sZq5QlGnno8.R5W8TPgwCrrsa3uV5Jkv_NRaz8uDMQPGwJbS3NUAAAY&dib_tag=se&keywords=Lammfell%2BHausschuhe&qid=1793639280&refinements=p_n_size_two_browse-vebin%3A1872403031&s=shoes&sr=1-15&th=1&psc=1)

Yes, they're over your budget. But they're worth it.  
Otherwise look if you can find them at a discount somewhere.

Brand : Haflinger  
Model : Lemmi Lammfell
[19s26bitna1tw] (score 2, diepte 1) I feel you. I wind up kicking mine off after like, half an hour.
(113 reacties met lagere score weggelaten)

