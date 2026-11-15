# Label-batch batch_0051

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
Schrijf het resultaat naar `batch_0051.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1dxly9k, a3jaad, 17kgudb, s2mm8i).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1dxly9k ===
SUBREDDIT: r/Residency
DATUM: 2024-07-07  SCORE: 48  REACTIES: 109
TITEL: Comfy shoes for long rounds and in general the day at the hospital
POST (source_id=post):
Bring out your best recommendation people 🥺 my feet thankyou already 🌸

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lc2h0ht] (score 77, diepte 0) Hokas :) the thicc soles help my plantar fasciitis a lot.
[lc2ilvd] (score 55, diepte 0) Dumb question but does anyone wear crocs at the hospital
[lc3r4w5] (score 53, diepte 0) Air Force 1s.
Aren’t comfortable but you’ll get mad respect from the transport staff and the 24 yo with DKA
[lc3ouje] (score 50, diepte 1) Crocs are my nights and weekend shoes for maximum slip on, slip off action. Started going with a t shirt instead of a scrub top, too. As the kids would say I’m looksmaxing
[lc2lewk] (score 23, diepte 0) Ultraboosts and Rothys are comfortable to me
[lc2kkp6] (score 21, diepte 2) They truly are, but me limping around the hospital is even more unsightly 😞
[lc3i2p3] (score 21, diepte 1) Counterpoint, I switched to barefoot style shoes and have had no issues with plantar fasciitis in years. Everyone's mileage may vary and it's not for everyone but it is an option.
[lc2jpgg] (score 17, diepte 0) If you are more of a dress shoe specialty. I love my ECCOS
[lc3fxdv] (score 16, diepte 2) I mean most medicine specialties. If you are primarily in the office or wear business casual and clogs/crocs won’t work.
[lc2itkn] (score 15, diepte 1) Lol me (gas)
[lc34un4] (score 13, diepte 1) Half my class (anesthesia) wears crocs or birks
[lc384t2] (score 13, diepte 0) ive tried pretty much all shoes for the OR and what has worked for me for both standing in a case all day and also running around are Birkenstock Bostons. I get the oiled leather ones and spray those like anti-water spray and they last forever
[lc3j3lu] (score 13, diepte 0) Europe is pretty much ONs for everybody. Could be a meme like patagucci by now. But they are comfy.
[lc3ig4j] (score 12, diepte 2) I also have found Hokas hurt my feet due to too much support. More minimalist shoes have made me way more comfortable as well.
[lc34rig] (score 12, diepte 0) Hoka Bondi
[lc32j1x] (score 11, diepte 0) Many of us have been through multiple pairs of multiple shoes - danskos, crocs, brooks, new balance, birkis, hokas etc

Honestly, eventually it just gets better because your body gets used to it. And it may change what shoes feel better over time. All this to say, don’t stress about it. There isn’t a perfect shoe, and when you are busy you will forget about it - but no one has the perfect answer for everyone

I will say as a bonus, compression socks usually help about 90% of people. Another things to consider

Good luck 🍀
[lc37n5q] (score 11, diepte 0) Honestly, there is no shoe that is going to keep your feet comfortable all day.

I wear Birkenstock clogs (the professional line which are rubber) and the wide toe box and the ability to take them off and actually stretch my feet or relieve pressure off of them is what gets me through 8 hour long surgeries.
[lc339af] (score 10, diepte 3) ASICS could be a good compromise. They provide similar support to HOKAS but are a little more streamline
[lc2raeh] (score 10, diepte 2) feel like they would be the comfiest + easiest to keep clean
[lc2t6ta] (score 10, diepte 1) Me!
[lc2v41f] (score 10, diepte 0) Skechers has some nice wide shoes with good soles
[lc2ry4e] (score 9, diepte 2) Nah some the new ones look good
[lc3bbx7] (score 9, diepte 1) Yeah! I wear the non-hole ones on nights and ED shifts primarily
[lc4bibm] (score 9, diepte 1) I respect this answer and I respect you, doc!
[lc3y2eh] (score 9, diepte 0) On cloud
[lc2ioha] (score 8, diepte 1 OP) Prolly surgeons
[lc3qx6h] (score 7, diepte 0) Cowboy boots with leather insoles. Pair of tecovas all day.
[lc2yvdc] (score 6, diepte 0) Crocs
[lc3t2kk] (score 6, diepte 1) There is nothing comfier than broken-in Bostons and wool socks.
[lc48h52] (score 6, diepte 0) Brooks
[lc2izec] (score 5, diepte 1) They’re hideous
[lc3efu2] (score 5, diepte 0) Asics are very comfortable and have a wide range of colours and styles + quite affordable.
[lc3io5c] (score 5, diepte 0) Honestly I really like Calzuros, especially because I’m in and out of the OR. Great for fluids, great for standing for a while.
[lc43uyh] (score 5, diepte 0) Allbirds wool runners!
[lc49whb] (score 4, diepte 3) I had the same issue. Switched to Altra running shoes and they were perfect for rounds
[lc3ruuq] (score 4, diepte 0) ASICS gel contend, it’s like walking on clouds
[lc4gbfx] (score 4, diepte 0) Roller blades. Not comfortable but they can get from bldg a to bldg b quicker and you will probably get banned.
[lc3z25c] (score 3, diepte 4) RN here. Definitely agree with ASICS. I work and run in the Novablast line. I didn't care for Hokas. I'm also very flat footed. Tri Noosa by ASICS are also excellent.
[lc3sgbt] (score 3, diepte 3) I too enjoy zero foot pain after my adoption of minimalist footwear (heard about them first from the foot and ankle staff surgeon during M3
[lc4ywdl] (score 3, diepte 1) All the ortho residents at my hospital lmao
[lc33e7y] (score 3, diepte 1 OP) Dress shoe specialty?
[lc34zpi] (score 3, diepte 2) Try their ultimate cushioning
[lc33or6] (score 3, diepte 0) Kizik roamer - best shoe I have ever bought. Love the fact I can just slip them on especially now that I'm pregnant. Super cushy and I like the way they look. I have the marshmallow color and throw them in the washing machine periodically and they come out looking like new.
[lc3sjn2] (score 3, diepte 1) Whose sneakers? There are some which come in leather.
[lc394e7] (score 3, diepte 0) For women’s dress shoes: vionics
[lc3mk81] (score 3, diepte 0) Hokas and Cloves
[lc3ncfj] (score 3, diepte 0) Got fitted at a running store. I have wide feet and overpronate, and was wearing shoes that were a couple cm away from the right size. I've been wearing the same brand and model of running shoe for 10 years now, and getting the newer version of the same shoe when they wear out.
[lc5qycm] (score 3, diepte 1) the high top CMFTs are my favorite
[lc3um7g] (score 3, diepte 0) Woman here, I like Hoka Bondis with scrubs & Dr. Scholl’s loafers with business casual. I have very small feet so the Hokas don’t look huge on me. I’ve heard good things about on clouds too.
[lc7yf25] (score 3, diepte 0) If you’re like our division chief (former special forces, worked at the VA, an Ortho bro) you wear waterproof combat boots with custom insoles.
[lc2jzrt] (score 2, diepte 2 OP) I don’t like their look too 😫thanks still
[lc4a91p] (score 2, diepte 1) I guess I’m the only one who hates Hokas. It doesn’t help with my plantar fasciitis and it hurts my feet more than
[lc4gabk] (score 2, diepte 1) I wear Crocs and/or the plastic Birkenstocks in the OR or morgue.
[lc4m9vd] (score 2, diepte 1) I wear Oofos daily
[lc6btjh] (score 2, diepte 1) Hell yea. Technically I think you’re supposed to go for the ones without holes but if you’re not doing surgery or anything involving blood splatter I don’t think it’s a major deal.
[lc58hc7] (score 2, diepte 1) 2nd this.  Ecco makes very light shoes with good support that don't look like I just came from a Phish concert.
[lc33jf5] (score 2, diepte 1 OP) I wear sketchers.. don’t feel comfy. Can you share the link of the ones you’re talking about ?
[lc4l9cg] (score 2, diepte 1) I love my Kizik shoes omg
[lc346nv] (score 2, diepte 0) Hokas
[lc37rxt] (score 2, diepte 0) Hokas made a huge difference
[lc436h7] (score 2, diepte 1) Agree mostly. I started with Bostons, switched to oiled Londons, been rocking those for about 4 years now and love them still.
[lc3dhqy] (score 2, diepte 0) for mostly standing - clogs. for mobility - arch inserts for walking shoes.  i don't like running shoes because of the angle.  sit whenever you can.
[lc57tn7] (score 2, diepte 1) Comfiest shoes I’ve ever worn. Took me through pregnancy while doing back to back ED shifts, and not ONCE did my feet swell or hurt. I will never wear another shoe!
[lc3f0hv] (score 2, diepte 0) Allbirds, ASICS, Nike in that order for me
[lc7nntc] (score 2, diepte 1) I really didn't want to believe it, just felt like a status thing. Then I found a pair on sale. Even as I started wearing them they felt a bit weird. But after breaking them in I absolutely love mine. I don't even notice having them on, comfy AF and no pain. 

I still wouldn't pay the full price for them though, ridiculously expensive shoes.
[lc3k7ut] (score 2, diepte 0) While in the ward and in PMR clinics, I wear Vessis. They’re waterproof and easy to wash, so good when dealing with…fluids. The different models of them vary in beauty and support, but all the pairs that I’ve owned have been super comfy
[lc5shjs] (score 2, diepte 1) those DKA kids with their fresh drip 💧
[lc3tzuk] (score 2, diepte 0) I have Hokas and they were a game changer but so expensive for a sneaker. While they do help, my feet are still sore by the end of the day. So I've been in the market for a cheaper alternative and I like the STQ slip ons so far, not as much cushioning as Hokas but comfy.
[lc3vl9e] (score 2, diepte 0) Kurus
[lc47auu] (score 2, diepte 0) Sanitas
[lc49thq] (score 2, diepte 0) Dansko is king but nothing beats Gucci slides
[lc4fluk] (score 2, diepte 0) Danskos all dayyyyy
[lc4g2qw] (score 2, diepte 0) Kuru footwear
[lc5jsmu] (score 2, diepte 0) Sketcher slipons
[lc6r2ny] (score 2, diepte 0) Chuck Taylors

The pain in your soles will help you forget the pain in you soul
[lc6y1uy] (score 2, diepte 0) 1. Hoka. They're not for everyone though and the models vary widely on comfort and stability 
2. Brooks. Very solid shoes and you get a 40% discount as a physician 
3. Altra. Neutral shoes that are also comfortable 
4. New Balance. Models vary widely, find one that's comfortable for you with a stiffer sole
5. Nike Pegasus is a relatively good shoe 

There are a lot of nuances here, for example your foot type (high arch, low arch, bunion issue?, big toe joint pain?, etc) but in general you want a stiff-soled shoe with a firm heel counter. That will be the most supportive. While many people love their Hoka Bondi because of how thick and cushiony it is, it's not for everyone. Same for minimalist/zero drop type shoes. 

Wear compression socks as much as you can, it will help out. And stretch your calf and achilles daily.
[mop642p] (score 2, diepte 0) Medical student looking to learn more!
[lc2g8po] (score 1, diepte 0) Thank you for contributing to the sub! If your post was filtered by the automod, please read the rules. Your post will be reviewed but will not be approved if it violates the rules of the sub. The most common reasons for removal are -  medical students or premeds asking what a specialty is like, which specialty they should go into, which program is good or about their chances of matching, mentioning midlevels without using the midlevel flair, matched medical students asking questions instead of using the stickied thread in the sub for post-match questions, posting identifying information for targeted harassment. Please do not message the moderators if your post falls into one of these categories. Otherwise, your post will be reviewed in 24 hours and approved if it doesn't violate the rules. Thanks!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Residency) if you have any questions or concerns.*
[lc2hqq8] (score 1, diepte 0) Hoka
[lc8w3nz] (score 1, diepte 2) Phish concert got me😂
But it is the perfect descriptor lol
(32 reacties met lagere score weggelaten)

=== THREAD a3jaad ===
SUBREDDIT: r/Frugal
DATUM: 2018-12-06  SCORE: 539  REACTIES: 107
TITEL: Order a Whopper through the Burger King app while within 600 feet of a McDonald's and get it for 1¢.
POST (source_id=post):
[removed]

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[eb6osh3] (score 167, diepte 0) I just saw this and was going to post it.  This is hilarious.
[eb6p26u] (score 93, diepte 0) So you go to one restaurant to order, and then to another restaurant to get your food?
[eb6q0tc] (score 68, diepte 1) 1¢ burger $1.50 in gas.
[eb6qfak] (score 67, diepte 2) I push my car for optimal mileage. You're throwing away money paying for gasoline.
[eb6r0sh] (score 51, diepte 0) Just think.

You can buy a bunch of "burner phones" and download the apps on all of them and get free meals for a week!
[eb6rcpe] (score 47, diepte 0) The closest Burger King to me is on a corner with a McDonald’s right next door. I’m excited for this now.
[eb6rpx4] (score 43, diepte 1) You could’ve gotten 99 more whoppers for that one fry...
[eb6rb96] (score 41, diepte 0) Did this today, then used the Mcdonalds app to get $1 medium fry
[eb6rjbh] (score 31, diepte 1) burger savings: $1 \* 10 = $10

burner phone expenditures: $25 \* 10 = $250

makes sense.
[eb6sp72] (score 21, diepte 1) i've already redeemed it. now im hunkered down in my Bathroom with a few days' worth of the newspaper to read, in preparation for the oncoming diarrhea storm
[eb6rsmi] (score 20, diepte 1) Burger Phones
[eb6r4ns] (score 18, diepte 0) Is it 1 per order or one per app? I feel like I could rack up a lot of single cent whoppers with a little motivation.
[eb6tpxx] (score 16, diepte 2) From a whopper? Tf kind of bowel disease do you have
[eb6qatb] (score 15, diepte 2) Unless they're within walking distance of each other.
[eb6rf0y] (score 15, diepte 0) Is this in the US only? I'm in canada and curious if I can take advantage of this.
[eb6r31f] (score 14, diepte 1) Yes.  Many of the apps have mobile app coupons for free and/or discounted food.  So, since this is r/frugal it makes sense that a lot of people on here who eat fast food would use them.  

It also helps with order accuracy as you don't have to worry about the cashier fat fingering something and a lot of the times its ready more quickly depending on the fast food place.
[eb6r2nl] (score 12, diepte 2) I've never seen a BK not within walking distance of a McD
[eb6r88m] (score 12, diepte 3) Where I am from there is some that share parking lots.
[eb6r3mj] (score 10, diepte 1) Not every store but some some restaurants actually have good apps. Mcdonalds, for instance, often has really good deals. Back in October they had deals to get any sandwich for $1. Some of deals in December are okay.
[eb6qt2j] (score 9, diepte 3) Cheap food AND you work it off too!
[eb6sfcc] (score 9, diepte 1 OP) Similar for me. Right across the street from each other!
[eb6s4tq] (score 9, diepte 0) I'm gonna just use a location faker so I can order it from inside the BK
[eb6tzv4] (score 8, diepte 3) i honestly don't know. i think my intestines violate the law of conservation of mass, because there's no way that the amount of shit that comes spraying out my ass weighs as much as or less than a whopper. it makes such foul and eldritch noises that my haitian neighbor from downstairs insisted on performing a voodoo cleansing ritual on my toilet
[eb6s0xp] (score 8, diepte 1) I believe it's 1 per account.
[eb6s5w2] (score 7, diepte 0) I had a guy tell me this at a starbucks today while I was talking to my date about how our diets were going, like. dude. 

&#x200B;

&#x200B;
[eb6qzbk] (score 6, diepte 3) If only you could run your car on french fry grease, wait a minute.
[eb6sijl] (score 6, diepte 4) I've got a truck that runs on grease. Smells pretty good too.
[eb6rl0q] (score 6, diepte 2) If you have a android, download a fakemylocation app no need for root. And make your location at any McDonald’s.
[eb6r9zb] (score 6, diepte 1) My (Canadian) McDonald's app is given me free fries whenever my local NHL hockey team scores the first goal in the match. I've got three accounts so I enjoyed three orders of fries tonight (two for myself and one for the wife). 

I hate having different apps for things (I'd rather used the normal web interface) but in this case, giving me free shit and discounts is making me use the app.
[eb6sh64] (score 6, diepte 2 OP) Correct. One per account/app download.
[eb6rr2r] (score 6, diepte 1) Wendys is selling 1 dollar fries any size.
[eb6snl7] (score 6, diepte 2) Same!  Can I order a Whopper with only ketchup?  Lol
[eb6srr1] (score 6, diepte 3 OP) Yeah the app gives you an option to customize it.
[eb6ta7h] (score 5, diepte 2) We need a synopsis.  Where were you when you ordered?  How far away was the nearest BK?  What did you do after you ordered?  How long did it take to retrieve your prize?  What did you do immediately after receiving your prize?  HOW DID IT TASTE???  In retrospect, was it worth it?  How far would you go out of your way to do this again?

So many questions...

E:  DO YOU HAVE PICTURES????
[eb6u76l] (score 5, diepte 4) Sounds like a shit storm
[eb6sx7z] (score 5, diepte 3 OP) Was thinking about that. r/unethicallifeprotips
[eb6qxa8] (score 5, diepte 1) [Jackpot](https://i.imgur.com/qLnyJFr.jpg)
[eb6rmu8] (score 5, diepte 1) Yeah.  I use McDonalds pretty regularly.  A lot of the time they will give me a Buy one Get One Sandwich or a free large fry with a sandwich purchase.  Frugal doesn't necessarily mean that you dont ever eat fast food.  It just means you try to eat for as cheap as possible and go for the deals so yeah the apps make food cheaper.
[eb6rqez] (score 5, diepte 1) A whopper is what, $6? I've never bought a burner phone, but there's no way that is going to be cheaper than buying a whopper everyday.
[eb6sksr] (score 5, diepte 2) It would make sense. I'll give it a go tomorrow. I'm lucky my McFatkidplace and my Glutton King are right across from each other. With my luck the app will send me to some far away corporate Burger King vs. the next door franchise B.K.
[eb6snhb] (score 5, diepte 2) so go to Mcdonald’s to order burger king just to go to wendy’s to buy fries lol
[eb6t79w] (score 5, diepte 5 OP) You have to use a credit card since you pay beforehand using the app.
[eb6tgwy] (score 5, diepte 0) What a whoppertunity.
[eb6tect] (score 4, diepte 3) my diarrhea tasted pretty bad, ngl
[eb6tkwd] (score 4, diepte 4) You're the worst reporter since Geraldo Rivera.
[eb6r1gk] (score 4, diepte 2) But then you have to Frogger to get your food.
[eb6rjf3] (score 4, diepte 3) You use Reddit yet you can’t comprehend people have apps for food places? Do you live in a Reddit server?
[eb6sn3c] (score 4, diepte 2) That's four dollars less than a Bluth Frozen Banana though.

&#x200B;
[eb6sgxw] (score 4, diepte 1) wendys is 1 dollar any size
[eb6t0hw] (score 4, diepte 4) And you can really just walk in and hand them a penny? Or you gotta pay online 1 penny with your cc?
[eb6sitv] (score 4, diepte 1 OP) Was thinking about that. r/unethicallifeprotips
[eb6sdth] (score 4, diepte 0) Be careful...not all bks are doing this promotion
[eb6s4kq] (score 3, diepte 3) Wine country represent!
[eb6so8o] (score 3, diepte 3) You expect me, an avid redditor, to walk to my feeding trough?
[eb6rfge] (score 3, diepte 3) now that's frugal.
[eb6tcfu] (score 3, diepte 3) I mean, it's one banana u/JeepPilot. What could it cost? 10 dollars?
[eb6s1hw] (score 3, diepte 1) Just use a burner email instead. http://www.10minutemail.com/
[eb6rmqr] (score 3, diepte 1) been thinking about this in lieu of the $1 hash browns...
[eb6so2y] (score 3, diepte 2) No, you could get 100.
[eb6tnl1] (score 3, diepte 3) But Uncle Sam wants his whoppers too
[eb6t9zn] (score 3, diepte 6) Neat thanks I know what's for dinner tonight 😁
[eb6slik] (score 3, diepte 1 OP) Mine are right across the street from each other!
[eb6sexl] (score 3, diepte 0) I had a whopper in Mexico and it was awful lol
[eb6t3j2] (score 3, diepte 1) I had dairy queen in Mexico and it was great. 👍
[eb6sfus] (score 3, diepte 0) If you had a android phone and a way to set your location you totally couldn't abuse this...
[eb6u7t5] (score 2, diepte 4) TIL: Subway have more locations then McDonalds globally, 

* 1 	Subway 	42,998  	 US$11.9 billion
* 2 	McDonald's  37,200  US$25.413 billion
* 3 	Starbucks 	28,720 Increase US$5.24 billion
* 4 	KFC 	20,404 US$23 billion
* 5 	Burger King 	16,859 US$8.6 billion

(rabbit hole)
https://en.wikipedia.org/wiki/List_of_the_largest_fast_food_restaurant_chains
[eb6t07s] (score 2, diepte 3) Really my town only has one Burger King and no McDonald's, the closest one is  four miles away.
[eb6t54x] (score 2, diepte 2) I mean unless you're like the majority of the world and they're across try street from each other. Heres my closest four. 

https://i.imgur.com/OIyUxbO.jpg
[eb6tanq] (score 2, diepte 2) They are across the street in my city.
[eb6sfjc] (score 2, diepte 1) My local McDs is less than 100 ft from the Burger King in town.
[eb6uk3n] (score 2, diepte 7) The hell are you worrying about people’s devices lmao. Are you arguing it’s not frugal or are you arguing for people to not download apps you don’t like? You don’t even know.
[eb6vs4p] (score 2, diepte 9) There's better hills to die on lol but I agree with you for the most part. I'm still gonna download the app and do the deal but just get rid of it after. I'm sure if there's another deal like this we'll see it here.
[eb6so5s] (score 2, diepte 1) You underestimate people's fast food addictions lol. I have Arbys, Baskin Robbins, Buger King, Dickeys, Dominos, Dunkin, Fridays, McDonalds, Moes, Olive Garden, Pizza Hut, Popeyes, Red Lobster, Sheetz, Subways, Taco Bell, Wendy's and that's not including me ordering KFC and Buffalo Wild Wings pretty often from Uber Eats or Door Dash lol.
[eb6ugic] (score 2, diepte 3) haha. reminds me of Juno. love that movie.
[eb6sqto] (score 2, diepte 1) What about using a VPN?
[eb6t4sr] (score 2, diepte 1 OP) More like, you could generate a bunch of disposable email addresses and keep making new accounts... ^but ^^you ^^^didn't ^^^^hear ^^^^^it^^^^^^from ^^^^^^^me
[eb6ucjt] (score 2, diepte 3) looks appropriately rated
[eb6tfvd] (score 2, diepte 3) Shit lol I meant to write 99 more 😂
[eb6rdgi] (score 2, diepte 0) Did this last night and wa so worth it
[eb6skmk] (score 2, diepte 1 OP) One per account sadly.
(35 reacties met lagere score weggelaten)

=== THREAD 17kgudb ===
SUBREDDIT: r/BuyItForLife
DATUM: 2023-10-31  SCORE: 40  REACTIES: 106
TITEL: Comfortable walking shoes that don’t hurt after walking for 3-4 hours?
POST (source_id=post):
I’m a shoe noob so I don’t even know which type of shoes that would be. But I occasionally travel and whenever I do I am reminded of how painful my feet and soles get after walking for a while. I have shoes ranging from 20 euros to 150 euros but all are more or less the same. The shoe that feels the most comfortable is actually only 30 euros lol. 

I’m willing to spend a good amount of money if there are some great walking shoes out there. A little bit of resistance to the elements would also be nice as the netherlands weather is shit.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k77r3ag] (score 56, diepte 0) You cannot ask for comfort online.  Ever.  For any reason.  When you see Sally post here and say, "ZOMFGlolWTFBBQ, XXX shoes are the most comfortable evAR!!!exclamationpoint!!" and you run out and buy XXX shoes, what you will learn is that Sally has cavus foot, which she won't mention because why would she, and you now own some shoes that feel like they have a rock in the sole.

If you are having comfort issues with your feet, you need a doctor, not a shoe.  A podiatrist can make you some custom orthotics which go into any shoe.  There are now custom insole clinics/stores where you can go in for a similar service outside of the health care system.  Or you can visit https://www.superfeet.com/ and attempt to DIY a solution.
[k77kp4c] (score 18, diepte 0) Available in Europe:

- Mephisto: Very dowdy, but they have some neutral styles. Sizing can be odd, the French like to really fill up their shoes. 

- Blundstones: Redbacks have a better reputation here, but are less available. 

- Camper Pelotas: They’re selling them with lifetime replacement guarantees, but they will wear out. 

- Orthopedic Brands: Finn Comfort is a German one. Embrace your inner pensioner!

None of these are BIFL, mainly because of the materials in the soles and how they’re attached to the shoes. A couple more points:

- You may be a good candidate for a visit to an orthopedist. If so many shoes cause problems, you may need corrective insoles. 

- You need to get your foot measured in person. 

- Two pairs of rotated shoes will give you more miles than one. 

Good luck!
[k786z18] (score 13, diepte 2) Most running shoe specific stores can and will measure your feet, soles, and pronation accurately, and recommend an appropriate shoe.  They have a variety of stability, drop, and cushion options depending on your feet and desired use.  Running shoes work great for walking.
[k78440o] (score 10, diepte 0) We have a running store near us and that's how I stumbled upon Brooks being the absolute best shoes for me - they used to hurt all the time.  

At the store, they measure you, watch you walk to determine how your foot falls, etc then recommend a shoe based on it.  Perhaps see if such a store exists near you?
[k77wfd2] (score 9, diepte 0) I really like Hokas. I recently bought a pair of on clouds before our recent vacation where we did a lot of walking. I would really recommend either. I also bought a better pair of inserts and that helped a lot.
[k77u7we] (score 7, diepte 1 OP) Thanks for the resources and tips. I will keep them in mind. I am planning to do a deeper dive myself as well, but getting some pointers about what to look for is also helpful.
[k77v30p] (score 7, diepte 0) Check out the Hoka shoes. Won’t last more than normal running shoes but will help.
[k78rqi5] (score 6, diepte 1) Podiatrists are often quacks for their industry.
[k780c0r] (score 5, diepte 2) People can have high arches or flat feet, and corrective insoles can give extra support for both types. Walking shoes usually have insoles that can be easily exchanged for corrective ones.

You can get custom tailored ones (250€+), but there are also over the counter ones (35€)  that can help a lot if you don't have too different / extreme issue feet.

You can [test your feet type](https://heelthatpain.com/foot-arch-type-test/) yourself, and find insoles for high arches 

Walking shoes can usually be gotten in different width sizes, make sure you have the correct width.

I had been walking around for 40+ years before I found out I had wide feet with extremely high arches, and found shoes with insoles that made me finally realize how 'normal' people walk.

Even for urban shoes I now use lighter models of Meindl shoes: They're very sturdily built from good leather.
[k78hg9s] (score 5, diepte 1) Another vote for superfeet.
[k78d298] (score 5, diepte 1) Exact same comment from me. I’m now amazed by the number of people I see wearing Brooks. I feel like a member of a secret happy feet club that exists in plain sight.
[k7c3q7u] (score 4, diepte 1) >Or you can visit https://www.superfeet.com/and attempt to DIY a solution.

I highly recommend against buying superfeet unless specifically recommended by a podiatrist. I bought a pair of the superfeet blue insoles and liked them at first, but they started giving me very bad knee problems. I then stupidly bought the even higher-arched ones and those were even worse. Never again without professional guidance. Nowadays, I go for minimal arch support, which is what most of my shoes come with, and my knees feel great.
[k783y8b] (score 4, diepte 1) I heard a lot about Hokas and tried them at a running store that does show fittings. They didn't work for me. I forget what I ended up with, I think some New Balance running shoe. I tried a few different pairs on to test the fit.

I use running shoes even though I do walking. Usually I am just 6k to 12k a day, but I've had some days on vacation over 25k and it was fine.
[k7anrar] (score 4, diepte 1) Yes! I love Brooks' Ghost running shoes the best, I think they are the closest equivalent to the type of support that Hoka lovers claim their shoes give them - but for people like me for whom Hoka doesn't work.
[k78fu8n] (score 4, diepte 0) Likely less to do with the shoes you wear and more to do with other issues.  The main thing is to make sure you don't use shoes that are past their life expectancy.   Many people use running style shoes far longer than they should.   A running type shoe will have a life between 300-500 miles.  So the shoe might look fine but the synthetics in the sole are no longer providing support.

Further most people overly support and cushion their feet.    Then you have other health issues like weight.    For me my problems were solved with my feet by losing weight and moving minimal shoes to strengthen my feet.   For example I was in Europe for 10 days in July and walked on average walked 19 kms a day and had zero issues with my feet, tiredness, etc.   I wore minimal running shoes exclusively doing that and had zero pain.   But it has taken me about 4 years to get here slowly doing longer distances in minimal shoes and slowly strengthening my feet/legs over that time.
[k782y0s] (score 3, diepte 2) Higher end shoe stores measure your feet.
[k77n6ej] (score 3, diepte 1 OP) By walking I mean regular walking around an european city. So you can imagine cobblestone, pavement, asphalt and maybe even dirt. As an activity I love walking, but my feet start to hurt after 3-4 hours. I have a feeling this might be due to the quality of shoes I wear. 

I wouldn’t mind if they could also be taken on a trek but if those kinds of shoes don’t exist then regular walking works fine.
[k7asph7] (score 3, diepte 2) Yes!  Brooks' Ghost is my go to running shoe.  I have not tried Hokas but since you love the Brooks more, I see no reason to try them.  :)
[k78jxbp] (score 3, diepte 0) I'm a fan of Asics. My last pair lasted me well over 1000 kilometers before I had to replace them. They make a good variety of stability shoes for whatever your needs are
[k7axsa7] (score 3, diepte 0) I have really shitty feet that make it difficult to walk for extended periods.  My foot pain used to keep me awake at nights after long hikes

My solution:  custom orthotics from a podiatrist and extra-wide New Balance shoes (think dad model).  New Balance shoes are definitely not BIFL, but they are comfortable as Hell and available in Europe.
[k77ip5s] (score 2, diepte 0) I am on my feet constantly for work. My last few pairs I’ve went with Nike Goretex trail shoes. They’re waterproof too. I’ve never had feet pain with them, even brand new. I’ve taken them for hikes too. Maybe not bifl but idk what shoes really are.
[k77mci1] (score 2, diepte 0) What kind of shoes and walking are you looking at?
[k7b4g7g] (score 2, diepte 1) Agreed. If somebody's feet are hurting after just a few hours of walking, it's because their feet are incredibly weak. My first thought when reading this post was that literally any shoes should be comfortable for at least a few hours of walking, as long as they're the right size.
[k79emyv] (score 2, diepte 0) Cannot speak highly enough of my Hoka Bondi 8s. I’m overweight but walk a shit ton (like 15-20k steps/day) and used to have really painful plantar fasciitis and pain in my Achilles but with these bad boys I can walk for hours many days a week and my feet feel totally normal afterwards. I’ve had them for over a year and they are still like new. I think I paid like $180 USD for them
[k7a919t] (score 2, diepte 0) I own a dog walking company so I’m on my feet all day.  The best shows I have found so far are [Altra ESCALANTE 3](https://www.altrarunning.com/shop/womens-escalante-3-al0a7r71?variationId=000&utm_content=ecomm&utm_medium=cpc&utm_source=google&utm_campaign=&utm_term=) provided there’s no snow to walk through and it’s not raining.  Before I was walking only in the Brooks ghosts.  I can walk over 20 miles a day.  I don’t know the exact conditions you will be in hope this is helpful.  I like the altras over the brooks as they are lightweight and I don’t feel as tired and the cushioning in the brooks when it’s gone it’s gone and it can be uncomfortable to walk in before I get another pair in the mail.  I would also highly suggest going to a local running shoe store first to get properly sized and see if you need a neutral or stability shoe.  They have foot scanners now that tells you the proper size it’s pretty cool and whether your arch is in each foot.  I found it all really interesting so much that I took my partner in as he was getting into running and now he wears the shoes around the entire house he says they are the most comfortable shoes ever.  So I would highly suggest finding a local running store with the best technology.  I also use to be a daily runner beforehand and can say I ran farther in my altras vs brooks especially on the treadmill or concrete.  They also have a wide toe box as I am on the very line of having wide feet and I also appreciate the wide toe box.  If you go with the brooks or altras you will be happy!  The problem is there isn’t one shoe for everything.  On days it’s sunshine at work I wear my altras if its snowing and I know the sidewalks won’t be clear I wear my snow boots if it’s really raining I try a waterproof sneaker but I haven’t found one I like yet as they are very hot and not breathable so take that into account when purchasing any shoe with gore Tex or anything water resistant related.
[k7any63] (score 2, diepte 0) Adidas Ultraboost 2019 and 2020 are peak comfort for me
[k7as0ka] (score 2, diepte 0) Trail runners. I like Hoka BUT get fitted at an REI bc they can tell you which brand will fit the best for your feet.
[k7bo035] (score 2, diepte 0) I work near a hospital and see many healthcare workers every day. Most wear either Hoka or Brooks brand running shoes. If it works for them, working sometimes 12 hour shifts on their feet, one of those brands may be a good starting point. Take a visit to a local running store too, they’re usually good about helping find a good pair and even insoles that’ll help you out!
[k77nb45] (score 1, diepte 1 OP) Thanks i ll check these out
[k77nfnk] (score 1, diepte 1 OP) Sorry if these are stupid questions, but what are corrective insoles? And where can I get my foot measured in person? Do stores do that or I have to go to a specialist?
[k7c90mv] (score 1, diepte 3) I've never seen that in the Netherlands though (except for simple length/width for sizing)
[k7cb2dd] (score 1, diepte 4) In Germany, these are specialty shoe shops that provide orthopedic insoles and prescription medical foot supports. This is where older folks often buy their shoes. 

They know how to provide competent foot measurements, and the local doctors who specialize in foot issues. The NL should work the same way, but Europe can be surprising. 

Given that so few shoes work for you, it may be worth talking to a doctor before dropping a lot of money. That’s beyond my and the sub‘s pay grade, but it’s something to consider.
[k7cbgkw] (score 1, diepte 5) In the Netherlands that's where a podiatrist comes into play. There are shoe shops that have a podiatrist employed, they can usually be found in hospitals (like next to the gift shop).

>Given that so few shoes work for you

I'm not OP and don't have a problem (anymore). I found I don't need insoles - I need barefoot shoes. Since I made the switch I have no pain caused by shoes anymore!
[k7c8yeb] (score 1, diepte 2) >corrective insoles

The Dutch word is steunzolen.

>And where can I get my foot measured in person?

You'll go to a podiatrist (podoloog in Dutch). Afaik you don't have to go through your GP (huisarts) for that, but you'll find that on their website.

Please also check out my comment on foregoing the podiatrist, as only the most modern ones start recommending barefoot shoes nowadays and those were the solution to my problems.
[k77o02u] (score 1, diepte 2) I can walk forever in Altras or Brooks. Inov8 a little less but still a long way.
[k78izq7] (score 1, diepte 4) He definitely should. I have like 4 pair that I wear for different purposes. When I do adventure races I grab my inov8’s.
[k7b99wp] (score 1, diepte 4) Stg read this as keep peace with my husband and was like htf is this shoe going to come between her and her husband?
[k7itj6p] (score 1, diepte 2) Not sure about your arch, but have a look to Asics. They are lifesavers for me. I use gel nimbus and they are amazing.
[mkehk5t] (score 1, diepte 2) Old thread, but what worked for you? My feet are starting to dislike my Ghost 14 Max’s, but maybe they’re old?
[mkk1jtq] (score 1, diepte 3 OP) I ended up buying Brooks. I don’t remember the model but it was 100 or 150 euros I think. I don’t think they’re “perfect”, but they’re very very good and I like them a lot.
[mkl8j4g] (score 1, diepte 4) I will be hunting down some new ones prior to my travels. Might have lost their bounce in cushioning somewhat.
[k79bkz9] (score 1, diepte 1) You sound disgustingly like me when I read a thread full of nonsense. I reply in the same. Exact. Tone.
[k7b9iqb] (score 1, diepte 1) But then there is the argument that arch supports and orthotics weaken your feet
[k7bamfx] (score 1, diepte 2) And people can argue that either with:

1. Medical professionals
2. Idiots on the internet

I'm giving terrific advice over here and it is shining like the sun.
[k7cx5ff] (score 1, diepte 3) Kinda makes you wonder how humans coped for the thousands of years before orthotics existed.
[k7dshtv] (score 1, diepte 4) What kind of shoes are you wearing that don’t feel comfortable?
[k7bpyaj] (score 1, diepte 1) I like the Hruska shoe list. https://www.hruska-clinic.com/shoe-list/
[k77r6wc] (score 1, diepte 0) I don't know but I only use one shoes for running and walking.    
my Zoom Fly 4 for 2yrs now.
[k77sf61] (score 1, diepte 0) I'd recommend trying some high quality inserts to add cushion and support to shoes you might have chosen for other reasons. 

But obviously running shoes (trainers in UK terms) or trail running shoes are likely to have more comfort and be lighter to reduce fatigue.
[k781vom] (score 1, diepte 2) My favorites like that were lowa renegades. If you get the black on black you can wear them under dress slacks and they look like a regular shoe
[k7ank2v] (score 1, diepte 2) Maybe try a pair of Brooks Ghost running shoes? They work great for me - Hokas just didn't work for my particular feet/gait.
[k7b011d] (score 1, diepte 1) Hoka are notorious in the running world for not lasting very long.
[k782fow] (score 1, diepte 0) Check r/travel and the threads there about walking shoes. Personally I got a great pair of shoes from Clark's 2 years ago and I plan to buy more from them. They're incredibly comfortable (even though they're heels!) and I will wear them to work or on vacation. It looks like they might only be sold in North America, the UK and Ireland though.
[k7eoyqx] (score 1, diepte 1) I used to love Brooks and then I tried saucony. Tbf, I have very wide flat feet and finding any show that fits is very difficult.
[k786u9x] (score 1, diepte 0) While shoes like Hoka and Brooks are great, I like my travel shoes to be less… athletic. I’ve really loved Allbirds, specifically their wool pipers, as they look great with all types of outfits and are uber comfortable.
[k787qfr] (score 1, diepte 0) I find these very comfortable for hiking.  

New Balance Fresh Foam X Hierro V7 Gore-Tex

Wore them for a trip through Alaska in all kinds of terrain and weather, from glaciers to rainforests to urban streets.   Obviously not for deep snow, but a set of gaiters would take care of that.  

As others have said, shoe fit is a very personal thing, ymmv.
[llnxc32] (score 1, diepte 1) How long have been using On clouds for? Are they still doing good?
[llopy85] (score 1, diepte 2) Had them for a year… they’re good. I think Hokas are better… but a lot uglier.
[llu34zd] (score 1, diepte 3) Thanks!
[k7kyqcs] (score 1, diepte 1 OP) How do you know when to replace shoes? In the past I've only really replaced shoes because something broke.
[k7kz9fk] (score 1, diepte 2) The soles got worn down to the point the bottoms were almost completely smooth. They're still wearable, just not good for distance or exercise and they got pretty slippery in the rain. They're the only shoes I've ever had that didn't need replacing because something outright broke.
[k7eywbf] (score 1, diepte 2) They can down vote me all they want but that's just how it is. Most of us have weak feet in large part due to growing up wearing super cushioned shoes, and also just because our society is lazy and weak in general
[kfra5kr] (score 1, diepte 1) I walked around barefoot a lot and now my feet are flat and I have pain. How am I supposed to make them stronger and bring the arch back without corrective shoes?
[k78t68v] (score 1, diepte 0) I'm not sure about walking, but working long hours on my feet on concrete, Dansko were the most comfortable I found. They're the only shoes I could wear that I've tried where my feet didn't hurt at the end of the day.
[k7l0b7u] (score 1, diepte 1 OP) Thanks these were some really good points! I learned a lot.
[k7a9k0o] (score 1, diepte 0) Not BIFL but they do have a 6 month replacement warranty for defects. I had a pair for 7 months and after having washed them as they state how to do this on their website. The stitching at the heal padding started to come undone. They replaced the pair for me at zero cost. I didn't pay for shipping and I was told I did not have to return the old pair. I did have to send photos of the stitching but it was so easy and I am wearing the replacement pair a year later. I wear these shoes 6 days a week.
[k7afdlh] (score 1, diepte 0) Hookas are pretty comfy and also come in wide sizes if you need. Some people in my household have flat feet/no arch so I got them the Gaviota and Arahi model. These have either an H frame or J frame for stability and arch support.

The Gaviota is more cushioned and basically the Bondi but with a frame inside and the Arahi is a lighter version so similar to a Clifton with a frame inside.
(54 reacties met lagere score weggelaten)

=== THREAD s2mm8i ===
SUBREDDIT: r/ems
DATUM: 2022-01-13  SCORE: 190  REACTIES: 102
TITEL: Everyone has their thing. Mine is feet. What’s yours ?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hsfsn53] (score 81, diepte 0) Eye injuries. 

I just can't fucking deal.
[hsg1l3w] (score 52, diepte 1) One of my buddies was working a shift with me, it was his first shift ever with me and he told me at the start of it that the one thing he didn’t like was eye stuff. We got held over that day because a woman sneezed and her eyeball exploded and the sack was hanging out of her eyesocket. I tech’d.
[hsfgrkw] (score 40, diepte 0) I always cover feet with a sheet! Lol. But seriously open sores make me sick.
[hsfw7x5] (score 38, diepte 0) Skin flakes. I’m sorry. I can’t do it
[hsg493y] (score 35, diepte 1) Ahhh, the ‘ol “if I can’t see it, it’s not there!”.

I dress my stretchers with an extra 8-10 inches folded over towards the head of the stretcher. I call it the “stanky foot pocket”. When someone’s got some nasties *WHOOP* just flip that baby over their toes.
[hsgi154] (score 32, diepte 1) Grandma glitter
[hsfpem6] (score 31, diepte 0) My thing is feet too. If you know what I mean.
[hsgdasi] (score 28, diepte 3) I don’t remember the exact terminology but essentially she unfortunately had a form of ocular cancer that was causing pressure to build behind her eye. I think basically pus was accumulating in a sinus behind her eye. Fortunately, she knew this and was already scheduled to have the eye removed like a day or two later. It was a weird call. I remember when we got it we figured it would be in some dirty trailer shithole just based on the CAD data and the location we were headed to. Instead turned out to be a loveley neighborhood a few streets over. Middle aged gal, couldn’t have been nicer. She apologized for throwing up in the back of my truck. I just gave her all the narcs and Zofran that she wanted. Poor thing. Lol the docs said fuck HIPAA and took pictures on their phones.
[hsfyjy5] (score 27, diepte 0) A shit ton of phlegm that you need to suction. Only thing that makes me actively gag lmao
[hsg3oup] (score 27, diepte 0) I had a pt surreptitiously remove her colostomy bag in order to finger paint. So that
[hsgilmu] (score 23, diepte 1) STORY TIME! Had a partner who just put lip gloss on before we were about to move a patient. Since patient was some mummy-wannabe on a draw sheet, we go ahead and use that to move them. As my partner pulls the sheet taut, a snowglobe's worth of Geri-flakes fly up and a bunch get stuck in the gloss on her lips. She then starts trying to push her lips outward in a panicked attempt to keep the flakes from going into her mouth. 

Good times.
[hsfxx1f] (score 21, diepte 1) Yessss. Upper torso removed from lower torso? Cool man. That makes me hungry.

Something stuck in your eye? Omg my eyes are watering just thinking about it. Awful.
[hsftf7g] (score 21, diepte 0) I'll take an excrement infused, meemaw that lost the fight to gravity 5 days ago over feet
[hsg22xr] (score 21, diepte 1) Yeah. I didn’t realize until I became a medic how much I hated anything airway related.  I get the job done, but on every tube I’m wretching a little bit internally.  

Closest I ever came to actually puking was a guy who had been chronically smoking through his Trach.  The plastic was all melted from falling asleep with a lit cig every night so we couldn’t hook up a BVM to it.  There was an impressive amount of puss oozing out as well.  

Fuck that.  Take me back to my BLS days. Couldn’t pay me enough to deal with that again. Lmao
[hsfmoia] (score 16, diepte 0) You pull a blanket down and wrap those gnarly troll toes.
[hsgkwfs] (score 16, diepte 2) Patient parmesan
[hsfxdzc] (score 16, diepte 0) Broken teeth especially bother me, gives me a nails-on chalkboard feeling.
[hsfw5uo] (score 15, diepte 0) Fucking mucus. I can handle blood pouring out of every orifice, brain matter on the road, vomit, shit. But phlegm… fucking bye 🤢🤢

Also that sound cotton socks make when you rub them together. Cringe
[hsfwayn] (score 15, diepte 0) vomit
[hsfy8p6] (score 14, diepte 0) vomit. instant panic attack
[hsgkxxr] (score 12, diepte 4) The doctors can actually upload pictures to EPIC from their phones so it MAY have been legit.
[hsg9wag] (score 11, diepte 2) Ah the good ol bum fold
[hsg8v6d] (score 11, diepte 0) No way in hell... I'll take feet over neglected pressure wounds every. Single. Day.
[hsgabc9] (score 11, diepte 0) Scabies pt scratching furiously freaked me out BAD
[hsggv7s] (score 11, diepte 0) Old woman UTI stank pussy that has been sitting in her own filth in a nursing home. That's the worst smell in the world. I can handle shit all day. Gore never really got me. Dicks don't bother me one bit. Stanky pussy man.
[hsgcz5q] (score 10, diepte 2) Good lord. Any idea what underlying condition made that possible?!
[hsgwgp9] (score 10, diepte 5) EPIC is the perfect acronym for that purpose

"Dude, wanna see some EPIC photos? Totally gnarly, like, this chick had her eyeball *ex-plode*, I was like, bro, no way, she was like, der, yes way, and we like *chunder*!"
[hsgiarl] (score 10, diepte 1 OP) One man’s trash is another man’s treasure !
[hsfotqr] (score 9, diepte 0) Mhmmmmm, corn chips!
[hsfphfu] (score 9, diepte 0) My thing's sound effects. Here's a T-Rex "BVHRRHRHAAHHRRHA"
[hsh8bp2] (score 9, diepte 1) Dispatch show this unit out of service for eternity.
[hsg4p7h] (score 9, diepte 0) After working in health care, I am obsessed with keeping my feet and bellybutton clean.
[hsggrmr] (score 8, diepte 1) Except for that time that you are transporting the obese homeless person who is hard to position, slides down the cot, and now you have two horror show feet right in your grill for the lift.
[hsfx9lx] (score 8, diepte 0) Eye Trauma. not even like ruptured irises those are fine but anything penetrating kills me. But i have a fair trade, my partner gets eye injuries and i get ankles and feet
[hsg5txu] (score 7, diepte 2) What a great idea! I’ll have to try that next shift! Thanks. (:
[hsgetil] (score 7, diepte 1) I inhaled skin flakes once. It’s something you learn to never let happen again. I get nauseated just thinking about skin flakes sometimes lol
[hsg4rki] (score 7, diepte 0) Brain matter. And it’s like fucking glitter - it gets EVERYWHERE.
[hsg9o0b] (score 7, diepte 0) I'm pretty sensitive to smells tbh.  The old pee, vomit, poo and necrotic flesh combo of the strokes/falls who have been on the ground for days..  That will stay in my brain for what feels like days and I'll get little phantom whiffs every once in a while.
[hsgdvko] (score 6, diepte 4) Aww man that sucks! Thanks for the reply! Sounds like you took good care of her!
[hsfv7av] (score 6, diepte 0) Certain skin infections. Some of those real bad IVD necrosis cases get me.
[hsg3cwk] (score 6, diepte 1) Free parm!
[hsgau3w] (score 6, diepte 2) Forbidden parm
[hsgimms] (score 6, diepte 1) Someone understands. It's not what's underneath, it's the skin itself.
[hsge7b1] (score 6, diepte 1) The sound when you're suctioning a Tracy and the mucous plug pops
[hsg3uch] (score 6, diepte 0) Sputum. I could never be an RT.
[hsghp4w] (score 6, diepte 1) Especially when they got that god awful smell
[hsgda31] (score 6, diepte 0) I don't just get the feet. Knees and below, baby. Always swollen, warm, and covered in puss filled sores 😋
[hsh4qsy] (score 5, diepte 2) 🪦
[hsfrxoa] (score 5, diepte 0) I hope you don’t mean you have a foot fetish.
[hsft4cr] (score 5, diepte 0) Should be a Fritos bag.
[hsh363n] (score 5, diepte 2) What age does this happen? I hope I die before then.
[hsg2gwl] (score 5, diepte 0) Anything saliva. Spill your guts (literally or figuratively) all over, I'm fine. Spit anywhere in the same room as me? I'm out
[hsgdmau] (score 5, diepte 0) Teeth. And puke
[hsgijkt] (score 5, diepte 2) https://www.youtube.com/watch?v=l60MnDJklnM
[hsg5r4a] (score 4, diepte 1) people think i’m weird for not being able to watch something as little as them touching their eye. glad to see i’m not alone
[hsgbbat] (score 4, diepte 1) Hell, this is why I wear glasses and refuse to get contacts. Eyes freak me out!
[hsgzgb2] (score 4, diepte 1) Geri dust
[hsh9khj] (score 4, diepte 1) 100%. Blood, shit, and whatever is fine. Fluids stay where they are supposed to mostly. Flakes pollute the AIR.
[hsfwe1c] (score 4, diepte 0) ZOMG! Four-toed feet send me right round the bend.
[hsghije] (score 4, diepte 0) Tracheotomies 🤮🤮🤮
[hsgm29q] (score 4, diepte 0) Patients beds and furniture. Fuuuuuck no, even relatively clean peoples beds can be nasty, and we don’t really see many relatively clean people.
[hsgy0m6] (score 4, diepte 0) Trauma broken teeth fine. Teeth rotted down to nothing and or caked with food/grunk. *heaves violently*
[hsh2guu] (score 4, diepte 0) Parasites. ECT helping pull live maggots out of homeless feet/legs while the rn scraped off the muck, so the provider could see if there's anything left worth saving vs amputating. The wriggling, sliminess, the smell, the accidental crunch-squish of trying to get them out. 

Had a guy who shit worms and dug them out of the toilet and tried to hand me a ziplock bag of poopy worms after checking into the ER.
[hsi41fu] (score 3, diepte 1) It takes a special person. I have nursing students who are in love with wound care. 🤮
[hsh4wzp] (score 3, diepte 1) This lovely Christmas feeling when the flakes fall down <3
[hsfwjz9] (score 3, diepte 0) Oh God ...
[hsh31du] (score 3, diepte 1) You just made my body itch! Yuckkkk I feel so bad for these things we never think about that happen. Thank you for doing this job and helping people.
[hsgayx9] (score 3, diepte 0) Fistulas make me nauseous. Doesn’t help that the average dialysis patient can’t/won’t take care of them.
[hsggass] (score 3, diepte 0) Dude fuuuck you for making me look at that right before bed
[hsgilcp] (score 3, diepte 1 OP) Fuck me again for reading all these comments now before bed lmao barf city !!
[hsh2912] (score 3, diepte 0) It took me 3 years to be able to drink from a straw after learning to deep suction trachs. That sound of the straw sucking the bottom of the cup made me feel sick. I still generally prefer not to use straws.

Also decubs. Bleh.
[hsha419] (score 3, diepte 0) There isn't a lot that grosses me out. The only thing that comes to mind is the actual action of needles going in to eyes, but that's not something that will actually be happening in front of me at work.

That being said, there are definitely things that make me irrationally angry. The "homeless and in-pain" groan/wail is the worst.
[hshg6kz] (score 2, diepte 3) Clostridium frosted flakes
[hsfwpg9] (score 2, diepte 0) Lice. I hate em and spend the remainder of the shift subconsciously scratching
[hshguqo] (score 2, diepte 1) I was actively drinking coffee while reading this 🤮
[hsg4xbw] (score 2, diepte 0) My thing is nosebleeds..i dont know why..but that shit makes me gag..anything else I can handle no problem
[hsg9lya] (score 2, diepte 0) Fortunately very rarely if ever run into this: I can't do spoiled milk. Just can't. Instant gag.
[hsgwvuu] (score 2, diepte 1) For me it's more the fact that the stink comes from a human.

Stinky dog? Still a good boy, I'll give him a pat and then wash my hands.

Same smell coming from a human? I'm donning full PPE.
[hsgwy6b] (score 2, diepte 1) Teeth *in* puke.

Yes, I've had to fish pt dentures out of the chunder pile before.
[hsghk1z] (score 2, diepte 0) Suctioning. Anything that needs to be suctioned I’ll pass.
(22 reacties met lagere score weggelaten)

