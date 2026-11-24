# Label-batch batch_0133

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
Schrijf het resultaat naar `batch_0133.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 178ztcc, tcwtf7, ssofe0).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 178ztcc ===
SUBREDDIT: r/pharmacy
DATUM: 2023-10-16  SCORE: 24  REACTIES: 66
TITEL: It's shoe time again whats your favorite brand?
POST (source_id=post):
Context: I work inpatient at a large hospital often in a clean room. 

Usually I buy Sketchers but my left foots bugging me and my right foot has the plantar fasciitis. I've heard Brookes before?  But they're rather expensive. And the sketchers have historically been cheaper for me. But recently I've come across these "xero" brand shoes that claim to feel like being barefoot? (Notably I never have issues with my feet when barefoot at home all day no matter what I seem to be doing.) And I'm tempted but I'm concerned they won't be durable enough to warrant the purchase. 

What shoes do you like to wear for your hikes through the hospital/retail space and what do you think is good for the cleanroom? (I stand to compound just can't sit) 

Thanks! 
-A CPhT

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k539wyc] (score 41, diepte 0) Hoka
[k53ovth] (score 20, diepte 0) Do you wear compression socks? I feel like those are just as important as the shoes
[k533qfc] (score 16, diepte 0) I’ve had plantar fasciitis for over a decade. Getting fitted for insoles by a podiatrist had helped a lot. I put them in all of my shoes. I also did some physical therapy after a recent sprain and they taught me calf exercises that have really helped. You can search them online. Icing the bottom of your feet with a frozen bottle of water works wonders!
[k53bo8o] (score 15, diepte 0) My current faves are Hokas; the wide foot ones.
[k54nqgz] (score 12, diepte 2) Get compression socks they’re life changing if you’re standing all day
[k53xjn9] (score 12, diepte 0) Hoka or On Cloud…. Both pricey but worth it
[k54uhmr] (score 11, diepte 2) i personally enjoy these posts cuz new ppl could have just joined to provide new insight 🤷🏻‍♂️ and others could have changed their mind. this place always infested with fun sucking haters 🤭
[k54kk3o] (score 8, diepte 2) Look into some of the work Crocs. No holes.
[k539nil] (score 7, diepte 0) If you plan on wearing a barefoot style shoe (xero or vivobarefoot) and you haven’t worked your way up by training your feet, then you are in for a world of hurt. Being barefoot around the house is not the same as working barefoot. I have friends that have worn Xero and they like them as a cheaper alternative to a barefoot shoe. They are pretty durable and should last a while if only wearing them in the hospital.

I wear Vivobarefoot. They have gotten very expensive but I love the feel of the ground and putting on booties is so simple. If you can build up the foot strength I would highly recommend Vivobarefoot. I have been wearing the same pair of Ra II for about 6 years at work. Looking to get another soon but the leather has held up great for how much I have used them.
[k54acwh] (score 6, diepte 0) Hokas 🤝
[k53fnft] (score 5, diepte 0) Dr. Comfort hands down. It helped that we sold them and got a great discount. Also available in extra wide which works great for my flipper feet.
[k54f5oc] (score 5, diepte 1 OP) Eh, I expect more variety than the "hospital or retail" question every 6 hours ;3 

I didn't see the thread last week. If you don't like the question you don't have to participate.
[k54fd11] (score 5, diepte 1 OP) My socks have a little extra padding and compression lines but are not "compression socks"
[k54bgqk] (score 5, diepte 1) I second the On Clouds. My mom would second the Hokas. 

See if you can’t get them with Amazon Wardrobe. It’ll give you 7 days to try them before deciding which ones you find more comfortable.
[k545soi] (score 5, diepte 0) Crocs are the best for me, to deal with plantar fasciitis. Hokas are next best and I use them to alternate every couple days because the crocs don't have much ankle support. Brooks hurt when I first tried them but I've broken them in and they are nice to alternate with the Hokas sometimes. You need atleast 2-3 good pairs to switch between.
[k560hmo] (score 4, diepte 1) They’re ugly, and take a while to break in, but they sure do get the job done.
[k548xjd] (score 4, diepte 0) Kuru shoes have saved my feet and I have chronic bilateral peroneal tendinitis that is far too eager to flare up
[k53onqy] (score 3, diepte 1) Any of their dress shoes or Their arch support insoles inside a pair of new balance. Also their compression socks are the most comfortable
I miss my discount
[k54vixr] (score 3, diepte 3 OP) Honestly, I'm getting alot of opinions I've never seen before and I've seen this question asked pretty frequently over 7 years in the profession. 

It's been very interesting got some leads to follow
[k54v7we] (score 3, diepte 3 OP) I might give that a go
[k54evaa] (score 3, diepte 1) I wore Dansko for so long, but when they started making them more cheaply, I just couldn’t wear them anymore. I have a very old pair that are not work appropriate anymore because they are so old and dirty that I just can’t give up for casual wear. They used to be so good!
[k54ddsi] (score 3, diepte 0) Even Skechers (which used to be a cheaper brand) are expensive now.

Hoka is my current favorite.  My RN husband says that a lot of nurses and other hospital staffers wear them, too.
[k54haic] (score 3, diepte 0) Hokas and compression socks are my current combo.
[k54xwtr] (score 3, diepte 0) Don’t think they’ve been mentioned but Kuru’s have been great shoes for me. Be sure and rotate the shoes between days or every 3 days.
[k550peq] (score 3, diepte 0) Hokas
[k551q7k] (score 3, diepte 0) Rockports
[k55407j] (score 3, diepte 0) Altra are my go to.
[k56p7w6] (score 2, diepte 2) You can slowly adjust your feet to them by walking in them for a couple hours a day and then going back to a normal shoe. There are probably YouTube videos about beginning to wear barefoot shoes.
[k53ml19] (score 2, diepte 0) Merrel Moab. Also, Best brooks, were the ghost 12 but they discontinued them in like ‘19 🥺. What size do you wear? I have a pair of Moab that still have a lot of life left, but itching for a new color
[k56l493] (score 2, diepte 1) Compression socks are a must. I use Bombas. Save your calves and feet from all those long hours standing.
[k53unir] (score 2, diepte 0) I love my Akk, I get a good year or 2 out of a pair. I work 40+/week retail CPht. So I'm pretty hard on them. I get the knitted memory foam slide on one's. And they are cheap enough that replacing isn't a big deal either. They also breathe well and are very lightweight.  Just a good shoe.
[k53wwtw] (score 2, diepte 0) Vionic are my favorite.
[k56cvmc] (score 2, diepte 2) As mentioned, the "work" version don't have holes. They are often slip resistant too!
[k5eihrm] (score 2, diepte 2) Croc pros are non slip and don't have holes
[k547zei] (score 2, diepte 0) I like Hoka with super feet arch supports.
[k56zq7p] (score 2, diepte 1) Came to upvote but yes, they take a while to break in but worth it
[k54bxnh] (score 2, diepte 0) I like Dansko.
[k56u182] (score 2, diepte 1) I prefer Sanita to Dansko. I have wide feet and the Sanitas are just more roomy.
[k54dyrw] (score 2, diepte 0) Brooks adrenaline gts with a Spenco total support insole.
[k56hlig] (score 2, diepte 0) I wear Hokas, but they can run pretty narrow. 
If I'm only doing a half shift or something I wear sketchers go walks; because the Hokas do pinch my toes a bit so having something with a wider toe box to change it up is nice. One of my rotation sites let me wear crocks which was kind of fun because it was the middle of the summer.
[k56kmf2] (score 2, diepte 0) On Cloud. The only ones I don’t even have to use inserts with
[k54fno9] (score 1, diepte 1 OP) Yeah I had the booties in mind, I usually wear hiking shoes but they can be hard to get some booties over the sole :/ 

These barefoot ones are like totally new to me. 

How does one train their feet for these?
[k56o6zh] (score 1, diepte 1) More specifically, [these Hokas](https://amzn.to/3Q1daf4)
[k5d0ah9] (score 1, diepte 4) I got some of [these socks. ](https://a.co/d/3t19Qc4) I like them because they aren't just boring black or white. Not that anyone sees them under my slacks anyway, but they make me happy.
[k54fx7o] (score 1, diepte 1 OP) My concern with crock's is all the holes usually? That doesn't pose an issue for cleanroom use? 

Also hokas are a new one seeing alot of shoe brands I don't often hear of this time.
[k5krqwf] (score 1, diepte 3 OP) How do they stay on your feet exactly? They seem cheaper than alot of the others recommended
[k552qkq] (score 1, diepte 2) I have five all bought 10+ years ago. I use them on rotation - and love them.
[k54g7ll] (score 1, diepte 1 OP) Quality also seems to have gone down on Skechers :/ I only got about 8 months out of them before I noticed a small tear along a seem :/
[k54l9ib] (score 1, diepte 0) Yeezy 350 v2
[k55spu3] (score 1, diepte 0) I've been rocking Altras and I just ordered a pair of Lems.  We'll see how they go
[k561lbz] (score 1, diepte 0) Brooks! Currently wear the brooks adrenaline and they are so comfy.
[k562lpb] (score 1, diepte 0) Hokas and Onclouds are both hideous. Adidas ultraboost are a check for both style and comfort and for context I’m Nike everything else when it comes to shoes and athletic gear.
[k56ogp5] (score 1, diepte 0) Crocs  are the only thing that work for me. I can run a half marathon in brooks but they don’t work as well as good ole crocs when standing all day
[k570frm] (score 1, diepte 0) I rotate between Hokas, Altras, and Allen Edmond wingtips. You can never go wrong with a well made pair of dress shoes
[k571mv6] (score 1, diepte 0) As a 62 year old pharmacist in retail, I’ve tried a bunch of options. Right now I’m wearing Brooks Ghost but what I can’t do without is my Spenco cross trainer insoles. The Spenco insoles give me that extra support and cushion!
[k571y59] (score 1, diepte 0) Crocs with socks all day every day
[k57fgrd] (score 1, diepte 0) cloves!!!
[k57g7bt] (score 1, diepte 0) If you have plantar fasciitis, you most likely need better support with insoles.
[k57pbl4] (score 1, diepte 0) Clarks
[k57ub8o] (score 1, diepte 0) I’m surprised that Birkenstocks have not come up yet. It’s the only thing I wear. I just got Montana’s and they are so comfortable. But bostons are bomb too!
[k57y4uw] (score 1, diepte 0) I think compression socks make a bigger difference for me. I use bombas because they have a higher cotton percentage which helps with sweaty feet. Synthetic blends are usually cheaper so I recommend trying those first if you don't have sweaty feet. Imo Hokas aren't all that, but I do have wide feet and the wide sizes still feel narrow.
[k59b55v] (score 1, diepte 0) Compression socks and on cloud shoes with extra padded insole (road runner sports)
[k59eqv7] (score 1, diepte 0) I bought a brand off a facebook ad called “softsfeel”…..   best 37.99$ in my ten years of pharmacy… 50+ hours a week… 
Promise, not a single ache in the 8 months ive been using them….
[k59zikw] (score 1, diepte 0) Lots of suggestions for you to check out. I’ll add if you have a Fleet Feet nearby or another gods running store, get your feet and gait analyzed. I like Brooks adrenaline, launch, and levitate, but they haven’t been doing the job lately - plantar fasciitis keeps trying to flare up. I ended up with a pair of Karhu that are very supportive. They use data from the Fleet Feet scanners in the shoes. 

I second compression socks. Sockwell are my favorites- actually cute, come in wide calf, have a decent amount of wool in them. 

I also love Birkenstocks. I bought a pair of the new lightweight Danskos, but don’t love them like my old made in Poland Danskos. 

If you can swing 2 pairs, alternating shoes could help, too.
[k5d1g2p] (score 1, diepte 0) I've got a pair of New Balance 928s that have lasted for at least 2 years, though I desperately need a new pair. I also got an orthotic insert of some kind or another. They've definitely been great, they haven't fallen apart at all, just getting a little too flat in the cushion. Though, come to think of it, maybe I'll try to hunt down the insert I got and get another pair of those first. 

I just walked into a Brown's Shoe Fit store and said "I need shoes for standing all day at work" and the helpful staff brought me different pairs of shoes until I found the ones that felt the best. For a long time I had no idea what the name of the shoe I got was, until now when I need another pair and I had to go searching for it.
[k5eempo] (score 1, diepte 0) I wear dansko. I think theyre ugly af but Im very comfortable
[k53iu3t] (score -3, diepte 0) Do you expect different answers than last week?

=== THREAD tcwtf7 ===
SUBREDDIT: r/walmart
DATUM: 2022-03-13  SCORE: 43  REACTIES: 66
TITEL: You people have foot pain working at Walmart ?
POST (source_id=post):
After 8 months working I still have foot pain, I got use to having foot pain when I get home. I added insoles to my redwings boots, which helped a little. I started using my Adidas shoes but doesn’t feel as safe and tight as using boots. Any suggestions on the foot pain or shoes to use. I just ordered a pair of Skechers afterburn energy

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[i0g272q] (score 20, diepte 0) Do what you have to do take care of your feet or *WARNING!*  [this](https://drive.google.com/file/d/1-bRnuuoxkb5-XhPSPHDVdcBd5YjsL_SR/view?usp=drivesdk) could happen. This is the end result of all the walking I did for Walmart. I developed a callous on my foot that busted open and wouldn't heal. That was due to becoming diabetic because of all the sweets and sodas I consumed while working nights and trying to keep my energy up. The callous ended up getting infected and my toe (and the bone behind it) had to be removed.

Now I'm diabetic, have neuropathy, and am always in pain. I'm working on getting my disability because I can no longer this kind of work.



TLDR: take care of your feet, no matter what.
[i0g3dyt] (score 17, diepte 0) Use the dr.scholl's insole machine. It was night and day for my feet. I had blisters on blisters but once I used the machine to get my number it pretty much cured my problem. They're pretty expensive but they were worth every penny.
[i0g3yrk] (score 10, diepte 0) Asics shoes
I have tried every brand on the planet
[i0gazge] (score 8, diepte 1 OP) Thanks for your advice appreciated, and good luck
[i0ge6eg] (score 8, diepte 2) Thanks. That pic was 3 years ago and it's healed up pretty good.
[i0g1hkz] (score 6, diepte 0) I honestly found the best solution was to wear shoes with real rubber soles. Walmart shoes uses plastic that offers no support. They used to cause me discomfort on the concrete floor. Spend the money for the shoes. Also look at getting shoe inserts.
[i0g3s22] (score 6, diepte 0) I work 60 hours a week on those awful awful floors. I've worn many different kinds of shoes over my 7 years, but my feet still hurt. Skechers are hands down the best. I wear the arch fits. So damn comfortable and if you have a Shoe Department(actual shoe store) near you they're cheaper than buying them at a Skechers store. 60 to 70 dollars. 

Only downside is because of how much I'm on my feet each day, roughly 12 hours, they don't last. I generally have to buy a new pair every 3 months.
[i0g5z2g] (score 6, diepte 1) Gotta second those Sketches arch fit shoes. I just got a pair a week ago. They've been so much better than the new pair of Pumas I'd gotten shortly before I decided to apply. Only been at Walmart for 6 weeks now (ogp/personal shopper so literally walking the whole store all day just doing picks) but the pain was unbearable. The inner medial bone or whatnot just below the main ankle bone on my left foot was becoming swollen and extremely painful around it. After wearing the Sketchers arch fit shoes that swelling is gone. They have a nice amount of cushion in the heal and feel almost bouncy and it's been great. My feet are still sore after work, but its not as bad as before and on my days off I don't feel it anymore.

I also have really wide feet (as a female) at the ball and middle of my feet (even some wides aren't wide enough or are wide in the heal which I don't have an issue with) and I was able to get a pair in wide that fit great.
[i0g87ks] (score 6, diepte 0) My feet usually hurt some, but my back has the worse pain.
[i0g6229] (score 5, diepte 1) It can be as easy or hard actually as finding the right sneakers.   Problem is which one.  I got pain on the big toe and ball of my foot and kept buying new sneakers til I found one that solved it.  I got zero drop sneakers.  They don't slant down towards the toes.  Instead they are aligned flat so it's more like walking barefoot.
[i0hcitx] (score 5, diepte 1) We don't have one of those machines but I can totally vouch for the Dr Scholl's.
[i0g975f] (score 5, diepte 1) Damn I just copped some on sale sketchers from Zulily* something about flexfoot 4.0 or something idk. I only paid like $45 Soo
[i0gb7s1] (score 5, diepte 1 OP) I usually work in the back room moving pallets
[i0gvvsk] (score 5, diepte 2) Inserts, inserts, inserts, can’t tell you enough, get them.

I got myself a good pair of work boots and I put inserts in it with solid plastic bits that support the arch in my foot, I can’t tell you how much it helps.

Wear knee pads too, if you’re doing any kind of work on the ground, those concrete floors are not fun, and they will destroy your knees, I’m only 20, but my body is already getting messed up a bit from working retail.

Wear gloves too, my gloves saved my wrist from being sliced open by something one day, didn’t even know about it until I saw the gash in my glove.

And I’ll say it again, kneepads, you might be the only one in the store wearing them, but guess what, you won’t be going home with sore knees like everyone else.
[i0hnacq] (score 4, diepte 1) Holy shit. I'm terrified I'm becoming diabetic. I have a lot of numbness in my feet all the time and my feet always hurt. 

Did you have any warning signs?? I'm normal weight now and was underweight when I started working here, though I suspect my weight gain is largely muscle since my thighs and calves are fucking rock hard.
[i0h0iwr] (score 4, diepte 0) I do have a few questions before I give any specific advice.

Where in your foot does it hurt?

What type of pain is it?

Are there things you do that make it hurt less or more?

What style of boots do you wear?

Have you tried any NSAIDs like naproxen or ibuprofen?
[i0hrxsp] (score 3, diepte 2) Nope. I was 135 when I was diagnosed. I slowly started gaining weight when I started medication. I'm currently 195 and been in this weight range for a few months.
[i0hsau1] (score 3, diepte 2) The 3 biggest signs are peeing a lot, always thirsty, and family history. Never hurts to get checked.

The foot thing could just be shoe related. I'd try arch supports.
[i0hcm8r] (score 3, diepte 1) Same here, and good shoes.  You pay for your shoes one way or another.
[i0hw04b] (score 3, diepte 1) Preach. They’re absolutely expensive but holy crap it’s worth absolutely every penny. First month without them was hell. Last six months with them. I don’t notice anything with my feet. My back is a different story though. Gotta keep that sucker stretched out. Lol
[i0jm1pj] (score 3, diepte 1) It’s actually toe pain. Like big toe to middle foot on one foot. I think I stubbed it really hard awhile ago and it’s sensitive. Also, I got sneakers from Walmart super center I don’t work at and just realized after 2 months the inside the shoe thing is coming out. I am going to try inserts and buy more shoes
[i0g46n9] (score 3, diepte 0) If you're in a normal store idk why you would need boots lol. I wear New Balance shoes because my feet are a dumb shape, my current ones were like $150 and it's worth it.
[i0gtlvi] (score 3, diepte 0) Can I piggyback off of this? I get knee pain in one of my knees that goes away when I buy a new pair of cheap shoes. Good brands for walking around all day?
[i0iev8w] (score 3, diepte 0) A lot of talk on here about inserts and Dr. Shoels.   Yea, these are all great.   Before you do that, find shoes that FIT you well for the activity you will be doing.   After 15 years at walmart pounding those floors, good fitting appropriate shoes will go a long way.

Also, get good inserts.   :)
[i0g26oy] (score 2, diepte 0) Losing weight can help but if that’s not the issue then sketchers could certainly help. Not all sketchers are the same but they make some very good shoes.
[i0g6o9q] (score 2, diepte 1 OP) Yeah I need to loose some weight
[i0kk8tt] (score 2, diepte 3) Welp, im going to put down my candy right now.
Thanks.
[i0kkg8l] (score 2, diepte 4) I still eat sweets, just not as much. It's all about moderation.
[i0g9tm8] (score 2, diepte 2) They do have cheaper shoes, I bought some on Amazon a couple years ago and they were junk. Never heard of the flexfoot though.
[i0g6kt7] (score 2, diepte 0) I work 12 hour shifts at a DC. I wear Hoka one one bondi 7, and my feet have never hurt since.
[jmxxk6z] (score 2, diepte 2) Yeah I don’t work at Walmart anymore so idc if anyone knows. They are Mizunos. They are running shoes. Very very good quality. After wearing them almost every day for a year and a half, they are still going good for foot support. Unfortunately some of the bottom part is starting to fall off but it still works great. Would highly recommend them
[i0ht8vo] (score 2, diepte 0) I tried so many shoes for work and always had foot pain. I got some ASICS shoes and problem solved. Best shoes for work
[i0k0ckz] (score 1, diepte 1) Seconded. I didn't use the machine, but I learned many years ago that a good pair of Dr. Scholl's makes a MASSIVE difference. I'm not even using good shoes, just some cheapie shoes I bought in the store due to am incident involving a customer letting his dog shit in my aisle while I was downstacking.... Anyways, even with cheap whatever shoes, with the insoles they've been fine for me. But, if you need it, it's definitely worth investing in some good quality shoes. Far cheaper than having to deal with medical issues down the road.
[i0ha4jr] (score 1, diepte 2) Companies make garbage shoes to sell at department stores, you always get what you pay for with shoes
[i0hcphc] (score 1, diepte 1) DC sells shoes called trase. I've been ordering the same shoes for close to 10 years, just in different colors. On their website they can go for anywhere between 20 to 60 bucks.... I usually wait for them to hit 20 before I buy them but they are really good with the Dr. Scholl's inserts
[i0gb9u2] (score 1, diepte 1 OP) Would look into it
[i0ghv3g] (score 1, diepte 0) Not after I got into good shape from throwing the truck. I just wear airforce 1's all day and don't feel a thing lmao
[i0gnub3] (score 1, diepte 0) I have been wearing Nike Air VaporMax for the last few years. When I first started working at Walmart my feet hurt constantly and when I woke up in the morning it was hard to walk due to the pain. After buying my first pair of VaporMax the pain completely went away. The pair I just bought were a little over $200 after tax, but for me they are more than worth it. I hope you find shoes that work well for you!
[i0h6fu9] (score 1, diepte 1 OP) Thanks
[i0goin8] (score 1, diepte 0) Just go all out on a good pair of tennis shoes or boots if you need them. It’s so very worth it. I cannot stress enough how much it is worth it. If I had known how effective my new pair of shoes would be in eliminating(not reducing, eliminating) my constant foot pain in every step and every moment there was weight in them, I would have paid 4x what they cost.   That no joke either. I was always hurting when I was walking. It’s just so worth it. It took about 2-3 days of wearing the new shoes for my pain to go away.
[jmxhjb3] (score 1, diepte 1) what shoes are they? sorry for digging this up
[jmy31jj] (score 1, diepte 3) Thank you for your time ❤️
[i0gyqeb] (score 1, diepte 0) Soak your feet in warm water with Epsom salt every day,  elevate them afterwards while relaxing.
[i0gzrcn] (score 1, diepte 0) I just went to my local running shoe store, and they fitted me for a dhoe that has the proper cushion and support for me. Everyone's feet are different, so everyone needs different amounts of support and cushion. Lots of these specialized stores carry brands that aren't as well known, but are just as if not more durable than stuff like Nike or Adidas. They're expensive, but worth it. I got a pair of Sauconys and love them and also really liked the Brooks I tried at the store. Highly recommend if you can afford the $100-$150
[i0h0kdr] (score 1, diepte 0) I'm not sure which line of Nikes these are but I got them from an outlet in clearance a while back and they definitely are great comfort wise, only downside is they are starting to fall apart and I don't think this product is still being made. So I picked up some Nautica sneakers and after one night I knew if I wore them again for work I'd end up having blisters. So back to these for now until I can find something else
[i0h1dhp] (score 1, diepte 0) I've found the sketches work brand to be pretty good, I got some non steel toe shoes which are extremely sturdy and my feet ache only occasionally, usually when I use one of the bad jacks that don't pull the weight as easily
[i0h4tm1] (score 1, diepte 0) Toe shoes are amazing at relief
[i0h9hqd] (score 1, diepte 0) I started wearing the New Balance old man sneakers with the foam soles, and that helped alot. Also look up Plantar Fasciitis stretches for heel pain specifically.
[i0hencu] (score 1, diepte 0) I sit down every chance i get.
[i0hfbvn] (score 1, diepte 0) This is one of those things you need to spend as a luxury purchase. Do not skimp and get cheap shoes. If you have a Dicks sporting goods or another sporting good store, I suggest checking out some good tennis shoes or running shoes with great insoles.
[i0hg01c] (score 1, diepte 0) Skechers arch fit. Literally saved my life.
[i0hg0v7] (score 1, diepte 0) Every day. Got good shoes but they only do so much when you spend 8 hours a day walking on concrete
[i0ht7u5] (score 1, diepte 0) Feet, ankles, knees, back, neck, head. You fuckin name.it man.
[i0hvjsu] (score 1, diepte 0) Honestly I could barely stay on my feet for the first month. It was soooo bad. I wear new balance and adidas cause big feet, but honestly what saved the day for me were the numbered dr scholls inserts. That weird machine in the pharmacy section told me what number and it took a little bit getting used to it and breaking it in but I’ve had absolutely no issues ever since. I even worked a 12 hour shift with no problems. Dr scholls inserts are a god sent    Probably the only reason I was able to keep working standing on that concrete floor for 8 hours.
[i0i3nj5] (score 1, diepte 1 OP) I would definitely try those insoles, I was about to get them today
[i0i53d3] (score 1, diepte 0) Yo!!! I have had foot pain for about 4 months. First two months there is did good. But I work in OGP, so my steps per day (tracked) are between 14k and 25k. Walking almost 12 miles a day 5 days a week will give you foot pain. I have insoles, orthotics and new shoes specifically designed for walking… still foot pain
[i0i6xjk] (score 1, diepte 1 OP) Did you try de scholls insoles ?
[i0vg1im] (score 1, diepte 2) Yep. I have dr schools insoles and I have some new orthotics… doing literally everything I can, including stretching, to make sure it’s not nearly as bad as it could be
[i0if72r] (score 1, diepte 0) Get the Dr Scholls “work” insoles, or use the machine to get customized ones. 1000000% worth it. Use them in a pair of hey dudes and never have blisters. Maybe minor discomfort but that’s about it
[i0jb75e] (score 1, diepte 0) Adidas Ultra Boost or adidas NMDs that have the signature adidas boost they’re so squishy super durable too
[i0jo21t] (score 1, diepte 0) I used to go home and sleep in a chair with my feet in buckets of ice water.  But my planter fascia was tearing.    Best shoes for me were new balance 1123....the replacement 1540 sucks big time.   Bates enforcers for boots do me well in winter...I have on sketchers right now.  Its about finding what shoe/boot works best for you on concrete.  My worst was brooks defiance running shoes...comfy when not on concrete...murder on feet when at work...as in with in a hr i could hobble at work or wear them all day anywhere else with no prob.
But keep up on insoles...or bite the bullet and see a podiatrist and get the good insoles as a coworker does.
[i0jym0m] (score 1, diepte 0) Look up plantar Plantar Fasciitis to see if that's the kind of pain you are having.    If so, I have found that the stretches recommended for it really help.   Most can be done while laying in bed or sitting.    Good shoes are important for this too.
[i0kjzsv] (score 1, diepte 0) This may sound weird, but get the *cheapest* walmart brand jogging shoes you can. Like, $9.
They won't last that long, but the soft foam and lightweight cheapass material go perfect with the rock solid surface of the sales floor. It's like walking on a cloud all day!

The grip wears off fast but i get a new pair every other month. The only other thing i ever wear are boots if i know it's going to be a very active day/bad weather.
[i0llugu] (score 1, diepte 0) I get more wrist pain then foot pain
[i0mdzyu] (score 1, diepte 1 OP) A coworker that works in frozen has pain in his fingers 😢
[i0odf96] (score 1, diepte 0) Fulton insoles were a game changer for me. They mold to the shape of your feet, so they're able to adapt to your body and make your feet feel way better by the end of the day. I actually wrote their customer support team and told them I worked at Walmart, and they gave me a discount... you're welcome :)
[i0grmcx] (score -15, diepte 1) Sound like you might have just been overweight

=== THREAD ssofe0 ===
SUBREDDIT: r/AmazonFC
DATUM: 2022-02-14  SCORE: 25  REACTIES: 66
TITEL: Zappos shoe recommendations? My feet are killing me.
POST (source_id=post):
I ordered my safety shoes from Zappos. They’re called SKECHERS Work Max Cushioning Elite SR Composite Toe and I got them in black. Boy was that marketing a lie. There was not cushion at all like walking on concrete barefooted. It felt like there were arches in the heel and toe of the shoe and a divot where the arch should be. The reviews made it seem like the shoe would be great for me but that wasn’t the case. Safety shoes are mandatory and I have a week before I have to return back to work. I want to exchange my shoes before I have to go back. Do y’all have any shoe recommendations or should I purchase insoles and try to tough it out ?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hwyx550] (score 16, diepte 0) I bought the Keen vista energy. I haven’t worn them to work yet, but I’ve been wearing them around the house and they seem pretty good so far.
[hwyxdgo] (score 15, diepte 0) Honestly, after exchanging 6 pairs I gave up and bought my own from somewhere else. The shoes at Zappos all suck and deform your feet. If you don't want to to shell out your own money for shoes your best bet is just to continue to exchange them til you find a pair you like. I bought a pair of DYKHMILY shoes from Amazon for $56. Majority of my facility wears them.
[hwyx4p0] (score 14, diepte 0) ALWAYS purchase insoles for whatever work shoes you're getting. The concrete floors do a number on your feet.
[hwz7f0i] (score 13, diepte 0) The Reebok work shoes suck ass too btw like walking on the fucking concrete floor.
[hx3avgm] (score 9, diepte 1) Trust me, wearing them around the house means nothing.
[hwz55zf] (score 6, diepte 1) This is extremely difficult for me findingones that work. It's hard to find mostly flat ones. I can't have any built in arch support on my one foot.
[hwza35t] (score 6, diepte 0) Timberland pros
[hwzfw2s] (score 6, diepte 0) Timberland pros with some dr scholls heavy duty inserts
[hwzcbxd] (score 5, diepte 0) Any kind of Skechers destroy my feet!  I’ve been really happy with my keens - enough that I bought 2 pairs and rotate them. Make sure you buy a size up from your normal street shoes since feet expand and insoles can also help.
[hwz4fbd] (score 4, diepte 0) Timberland Pro Drivetrain are great so far
[hwzgxh2] (score 4, diepte 1) The insoles in them are laughable
[hwyxfjl] (score 3, diepte 1 OP) Which insoles did you buy?
[hx07zdg] (score 3, diepte 1) Same. Feels just like regular sneakers!
[hwz5dle] (score 3, diepte 0) For Zappos shoes I go with the men's  Irish Setters. Make sure you get shoes a size up then your normal size it makes a big difference. 

I heard some good things about the red wings and carhartts boots too.
[hx0hbga] (score 3, diepte 1) I wore those on my first two shifts and by the end of the second night my feet were literally throbbing on the drive home it was absolute hell. I had to PTO my third shift cause I couldn't walk.
[hwzgixt] (score 3, diepte 0) Cheap but comfortable safety shoes from Amazon and amazing insoles from zappos. That's the best way to do it.
[hwzv2cy] (score 3, diepte 0) I got a pair of reebok through zappos and they were awful. I tried inserts. No help. I got a pair of Merrell safety shoes. Still wearing around the house but they seem good
[hx02x39] (score 3, diepte 0) I like the half soles that are heel and arch only Dr Scholl's.   If you are a new employee it not just the shoes.   You have to get used to the shoes, also  standing so many hours and using muscles you normally don't.   It took me 3 weeks which is 3 12 hour nights a week x3 to get used to it.   I always even now take 2 ibuprofen b4 work.
[hwz0lyi] (score 2, diepte 2) Insoles are very specific to your feet.  They can make a huge difference… if they are the right kind for YOU.
[hwzb5nb] (score 2, diepte 3 OP) Thanks!
[hx08di4] (score 2, diepte 4) I would suggest going to Walmart and doing the shoe insole thing that measures your feet and shows where you put weight on your feet. More expensive but I put them in my shoes the same day I got them and pain was instantly gone.
[hwyyi51] (score 2, diepte 2) I've only had my new shoes + soles for a week, but so far the ones from Zappos seem to work. I also got Skechers btw
[hwzrr8t] (score 2, diepte 1) I got these too and wore them today. 5 hour manual pick (walking) on cement and they were pretty great. A little heavier than my regular shoes but comfortable.
[hx3ls5b] (score 2, diepte 2) https://www.redwingshoes.com/accessories/footbeds/Shaped-Comfort-Footbed-96317.html?cgid=footbeds I’d recommend these!! When I was working at a animal feed company we got boots from this company as well with insoles, the insoles last me 2 years.
[hwz4y83] (score 2, diepte 0) The shoes really don't matter, need to get insoles.
[hx0yng8] (score 2, diepte 1) I really wanted the Irish setters but none were available in my size. I kept checking back for like 2 weeks. The wingshooters look great.
[hx1d44u] (score 2, diepte 2) Yea wearing them almost made me walk out and quit cuz they made my feet hurt so bad especially since I’m flatfoot and my right foot hurts so bad.
[hwzsn4f] (score 2, diepte 1) They don’t make ‘safety’ shoes.
[hwzs0sp] (score 2, diepte 1) I like the Keen Vista Energy so far.
[hwzfxec] (score 2, diepte 0) I purchased the sketchers work rad from Zappos based off reccomendactions after the timberland pro. We're killing my feet and they're no better . My feet hurt within half the 10 hour shift and to top things off , the material on left side was rubbing against my skin and sliced me up by the 10 hour shift. I can't win with these Zappos shoes smh
[hwzkbw9] (score 2, diepte 0) Reebok Flexweave Floatride. Extremely comfortable and I didn't need insoles. They come in several colors, but they only have black on the Zappos at Work site. It's worth it to spend your own money if you can.
[hx10u6b] (score 2, diepte 0) Keen Vista Energy are the best in 5 pairs ive owned.  Just get a gel insole for additional shock absorption.
[hx194eg] (score 2, diepte 0) Nautilus ones are comfy and cushioned
[hx38qfw] (score 2, diepte 0) I have heard from several Associates that the Amazon essential shows are comfortable. I have some Reebok Hi-Top which are pretty good.
[hwywjr5] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If you are interested in learning or asking about anything related to covid leaves and its process, please visit our [Megathread](https://www.reddit.com/r/AmazonFC/comments/s1m1qr/all_about_covid_leave/). We also have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[hwyxqs3] (score 1, diepte 1 OP) Do you think it’s best to purchase some from Zappos or head to a store and get something like Dr. Scholls?
[hx2drhe] (score 1, diepte 1 OP) I’ll have to check them out. Thanks!!
[hwz277a] (score 1, diepte 0) I loved the timberland pro, the caterpillars were ok and the new balance 589 I got aren’t too bad either
[hx2xep6] (score 1, diepte 2) Make sure to get a size up then your normal size it helps reduce some of the pain from the new shoes. 

Yeah i had to wait a bit before mine was available
[hx3hmcz] (score 1, diepte 2) I have the wing shooters.  Love them.  Wear them on days off as well..   great boots
[hwz9h8v] (score 1, diepte 0) Hoka One One
[hwzad79] (score 1, diepte 0) I bought Reebok shoes. Same size I usually wear but wide width. 

Shoes made with an extra wide toe box that gives my toes plenty of room.
[hwzcmgf] (score 1, diepte 1) Same!! The width makes it super comfortable but they still kill me at the end of the day. I think I need insoles
[hx2e4u4] (score 1, diepte 1 OP) It’s a shame because I used to love sketchers and my non work sneakers are sketchers and very comfortable! So far The keen brand keeps getting recommended so I’ll try them out.
[hwzhcue] (score 1, diepte 0) I don’t mind the Reebok work shoes (the knit material ones that look like running shoes). Didn’t want to wear all black kitchen shoes or boots so those work out well. I suggest switching shoes and getting insoles. Insoles seem like biggest difference to help wear and tear of feet.
[hx07ysj] (score 1, diepte 0) Timberland pro radius. Wore them to work thinking of have to wear them in. Nope. No blisters, no pain, didn't have to get insoles. My previous shoes were the timberland pro reaxion. Those shoes/boots were a pain from the get go. Terrible insoles- super painful feet even after I got better insoles. Also blisters the first two weeks. With the radius they get a bit sore, but nothing like the reaxion. Definitely recommend.
[hx0euyq] (score 1, diepte 0) My Danners are both nice (got a waterproof winter pair and a tennis style summer pair now) but I 100% had to swap out the insoles. I need more support than most default insoles offer. If the shoe otherwise fits well, I'd get some insoles for them that fit your foot. They're usually really only worth swapping if the size is wrong or the toe box is cramped.
[hx0y9hl] (score 1, diepte 0) I got the reebok military boots and some good insoles. The ones that come with the shoe are crap and killed my feet after one day. Took a bit to break in but I was also getting used to walking 15+ miles a night. I just bit the bullet and got them on my third week. They aren't required at my FC but I wear them everyday because I move around pallets all day and they are great. Did 18 miles last night in them.
[hx1qf7q] (score 1, diepte 0) I got Wolverine Rev Durashocks. I grew up around where they are headquartered and I know that Wolverine's mainline of shoes and boots are top shelf stuff. In Michigan, you either got Redwings or Wolverines for work, those were the two top shelf workshoes. So the quality is good. Still gonna pop some insoles in.

My recommendation is for Wolverines, either sneakers or boots. They're tough and meant to be worked in, and also not terribly expensive.
[hx1ym6f] (score 1, diepte 0) I got the 5.11 work boot and they are pretty comfy, they look pretty cool to so that’s a plus
[hx2djor] (score 1, diepte 0) The Reebok work series is pretty comfy to me, my first pair were the timberland pros or something like that..shoes not the boots.
[hx37xup] (score 1, diepte 0) Timberland Pro Reaxion or Drivetrain plus buy insoles.
[hx3e2c4] (score 1, diepte 0) I’ve got the avenger work boots for women. Felt broken in right away. Comfy.
[hx3e3xm] (score 1, diepte 0) I absolutely love my Thorogood Union Series and my Rebook Sublites, the later of which are a lot lighter. I'm glad I have both. I wear them more off work then I do at work!
[hx3h19i] (score 1, diepte 0) I got the keen ones, they were more than $110. I ended up paying $10 out of pocket but they are comfortable they just had to be broken in
[hx3kdwt] (score 1, diepte 0) Wolverine low top shoes. The are light and have ALOT of padding on the top and sides.   Goto wal mart to that dr Scholls machine get your numbers and you are set. Thank me later BB
[hx3llxz] (score 1, diepte 0) Get flip flops bro
[hx3ln02] (score 1, diepte 1) „oɹq sdolɟ dılɟ ʇǝ⅁„
[hx3mdyq] (score 1, diepte 0) Your best bet is getting them, reselling them for the market price and then buying a really comfortable pair like I did
[hx3qlkf] (score 1, diepte 0) My Cat shoes are heavenly. Also even if they aren't Zappos, Survivors at Walmart are composite boots and they have lasted me since 2016. The only thing I've had to change was the laces.
[hx3v3ma] (score 1, diepte 0) Is there any shoes that ARENT hard on the front?
I want some flexible shoes, and the shoes I have just aren’t flexible enough.
[hx410z4] (score 1, diepte 0) What does Dai Tenko  wear ?
[hx4twnk] (score 1, diepte 0) I always get the Timberland Pros. Not only are they the best looking ones but also very comfortable
[hx58yfr] (score 1, diepte 0) I use barefoot shoes , brand Merrel.... my point being , the fluffier the shoe ≠ better.
[hx5al3m] (score 1, diepte 0) I’ve been wearing the Nautilus ones for a while and they feel like walking on clouds.

