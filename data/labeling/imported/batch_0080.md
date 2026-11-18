# Label-batch batch_0080

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
Schrijf het resultaat naar `batch_0080.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: qne0y1, 5t1c3j, aau13a).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD qne0y1 ===
SUBREDDIT: r/bartenders
DATUM: 2021-11-05  SCORE: 15  REACTIES: 85
TITEL: Favorite shoes for bartending?
POST (source_id=post):
I currently have Fluevogs and Shoes for Crews that I wear most often but am not totally satisfied with them. Looking for something with more arch support.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hjg14zy] (score 27, diepte 0) Vans made for the makers 2.0 high tops

Non slip, stain resistant black leather, and good support with the included insoles. Might not be the best for people with very wide feet.
[hjfsq4b] (score 17, diepte 0) I wear doc martens, not arch support but they are really helpful, I get bad hip pain from sneakers.
[hjfho6l] (score 16, diepte 1 OP) R u ok
[hjgtqmv] (score 9, diepte 0) Blundstones with insoles
[hjfupch] (score 6, diepte 0) All black New Balance 626.  

Theyre non-slip and feel like walking on pillows.
[hjfzz7q] (score 6, diepte 0) Boots, combat style. Nonslip, water resistant, composite toe and lighter than most work boots.
[hjh1cql] (score 5, diepte 1) I have pretty wide feet but I just order a size up for vans and they’re pretty comfortable
[hjgpjpk] (score 5, diepte 0) Rainbow crocs. You might get an occasional wet foot but the comfort is unmatched and customers liked them too
[hjfl0m9] (score 4, diepte 0) Buy shoes that fit your feet correctly, then replace the insole with one that supports your feet correctly. One shoe does not fit or support all or even most.
[hjh0sxk] (score 4, diepte 2) Mine are still kicking after 6 months or so.
[hjh3xm6] (score 4, diepte 0) Air force 1's
[hjfkrcj] (score 3, diepte 0) Hoka 7s. Pricey but 100% worth it
[hjgysjx] (score 3, diepte 1) Yep, put some inserts and you're golden. It's nice not getting your feet wet by dish
[hjgz7rf] (score 3, diepte 1) I do the same.  Low Docs with quality inserts. Works wonderfully. They’re over a decade old and going strong.
[hji1hfo] (score 3, diepte 1) The Docs for work are crazy good bar shoes. Extra insole, extra flex in the mid foot, and a nonskid sole that even grips my bar floor which is wet marble. They're so good that I have another pair as my daily driver.
[hjgr7xw] (score 3, diepte 2) Not op, but I’ve been using the made for makers as well for about half a year with no issues so far.
[hjg8wz5] (score 3, diepte 0) All about the insoles. Goodninsoles make the difference
[hjhf47f] (score 3, diepte 0) Doc Marten makes a nonslip version of the 1460’s and those will last me 4+ years a piece. And no, they’re not that heavy.
[hjj4er3] (score 3, diepte 1) Dude I was so nervous when I bought my docs for work cause everyone said there would be a gnarly breaking in period, but I honestly never experienced it. Wore them for 8-10 hours from the get go and I kove them.
[hjfggmo] (score 2, diepte 0) Skechers arch fit is decent
[hjfgtbg] (score 2, diepte 0) Classic vans but no arch :(
[hjhkabx] (score 2, diepte 1) Docs for me. My next pair will be the high tops without laces, I think they’re called the Shelby’s. Because after a long day the last thing I want to do is unlace my boots and pull on the sides to loosen the laces (because I wear them all the way tightened)
[hjh6k6o] (score 2, diepte 1) This is the way
[hjgm3hr] (score 2, diepte 1) Have you had enough time to test the durability of these? I saw a lot of reviews saying they fell apart quickly, which stopped me from paying $80+ for them
[hjipclb] (score 2, diepte 2) I think that really just depends on your environment and hours worked. If you're full time or pulling over time on the regular and your gig is rough on shoes then you should expect to replace your insoles and even most shoes every six months to a year. 

My gig is pretty low wear on shoes but I've had them for two months and the only change from brand new is the slight creases in the leather that are bound to happen.
[hjgda7t] (score 2, diepte 0) Dr Martens 1461 with molded soles. Its the perfect shoe
[hjgerxv] (score 2, diepte 0) My Addidas All Pros (the shop didn't have sambas that were big enough) have been great if you go for a more casual look. I'm usually looking at 10-12 hr shifts with almost no aches at the end & they're easy to maintain. Just wipe the faux leather down with a damp rag & hit the whites with scrubbing bubbles foam once a month to keep them looking fresh.
[hjgo6m6] (score 2, diepte 0) Iron rangers
[hjlou2d] (score 2, diepte 2) The key (IMO) to Red Wings for daily wear is to have at least two pairs. They need a day to rest in between wears, otherwise they fall apart much faster. I’ve been rotating between two pairs for about 3 years now, and they don’t look even close to coming apart. The only thing I’ve had done on them is re-gluing the heel piece of leather on the insole, but even then my local cobbler did it for free.
[hjhul2d] (score 1, diepte 1) Hoka 7 what?  I use hokas for running, but I've never seen a slip resistant one.
[hlhs80w] (score 1, diepte 1) New balance nonslip shoes are great. Dr. Scholl …. Doc martins (but pricey)… Skechers lol
[hjfovba] (score 1, diepte 0) Something nonslip that fits then add superfeat, don’t get that cushiony dr scholls shit
[hjhbpcs] (score 1, diepte 2) I have one with a canvas upper that zip up on the inside and seriously.. they are amazing. Comfy from day 1.
[hjj4a1k] (score 1, diepte 1) Yeah I just converted to docs and I'm never going back. I did love my sketches for work but they never lasted as long as you want them to for the price
[hjfssu7] (score 1, diepte 0) When we had a curbside patio and people were also allowed back inside, I was doing between 10 000 and 20 000 steps per workday, and Adidas Nite Joggers saved my life with their Boost cushioning (looks like styrofoam or clouds).
[hjh6l7v] (score 1, diepte 2) ##This Is The Way Leaderboard  

**1.** `u/Flat-Yogurtcloset293` **475775** times.

**2.** `u/GMEshares` **70700** times.

**3.** `u/Competitive-Poem-533` **24597** times.

..

**279531.** `u/Teocinte` **1** times.

---

^(^beep ^boop ^I ^am ^a ^bot ^and ^this ^action ^was ^performed ^automatically.)
[hjie4yu] (score 1, diepte 3) This is the way
[hjhs0fe] (score 1, diepte 1) Igor  my new balance from shoes for crews and I love em
[hjfz70q] (score 1, diepte 0) Nike roshe
[hjhfwwo] (score 1, diepte 1) Wow i have never considered working in boots. I go for the complete opposite with very light, breathable shoes. Very much not waterproof but they dry quickly.
[hjhotff] (score 1, diepte 2) I almost exclusively wear these. I can polish them up if needed. We stand on our feet for hours and I've learned what works best for my feet. 

When questioned or made fun of by staff I always reply "My feet are dry and don't hurt at the end of shift" smile and they don't bother me again about it.
[hjhrw38] (score 1, diepte 2) Non-waterproof shoes are an absolute no-go. I wear hikingboots, they are waterproof and a little more comfortable than combatboots, and worth every cent.
[hjruv66] (score 1, diepte 2) I’ve been wearing mine 35-40 hours a week for 7 months and they are still going strong. Only gripe is that the laces are so long and I need insoles. Love them though.
[hjh0pfp] (score 1, diepte 1) Came here and said this too
[hjhs1gb] (score 1, diepte 1) Yes and no. I now have hikingboots, they keep my feet dry even if I stand in 15 cm of water (yes, I tried), and that helps a lot. Keeping your feet dry helps a huge deal.
[hji7j30] (score 1, diepte 2) I was talking about arch support. Like if you put good insoles in all kinds of shoes, they can help with foot problems.
[hjgbmfj] (score 1, diepte 0) Rockport boots
[hjgf1ju] (score 1, diepte 0) Adidas Falcon or anything with the same sole! I'm on my third pair and would never replace them.
[hjgg3ja] (score 1, diepte 0) I wear military surplus boots. They’re breathable and only $35 so idc if they get fucked up. People always compliment them too for some reason. Lol
[hjgioai] (score 1, diepte 0) Do fleuvogs make a no slip grip shoe? I live by the slip proof shoe, so I love Boston birks with the proper grip and keep bistro crocs in the rotation
[hjgldl3] (score 1, diepte 0) i’ve never been happier than i am with my vans for makers
[hjgyjyz] (score 1, diepte 1) As in Red Wings? For arch support I'm not so sure...
[hjhprzx] (score 1, diepte 2) I was born with foot defects on both feet (clubbed) so for me they’re perfect. Guess I didn’t consider I’m weird lol I just read the title and first half of the post
[hji3zsc] (score 1, diepte 3) I mean if I wasn't broke id love a pair of Red Wings they're great boots, but they don't have any sort of arch support until they break in
[hk1l6ur] (score 1, diepte 4) They still don't really after. The depression isn't really deep enough. Insoles are a thing though.
[hjhkmll] (score 1, diepte 1) Whew I had a pair but man they’re expensive. Only lasted a year before I blew them out
[hjgs1fy] (score 1, diepte 0) New Balance 327, the grip is crazy non-slip and light as air. Didn’t need arch support insoles and to me are perfect for long hours.
[hjgssxb] (score 1, diepte 0) Nike free flyknit. Won’t work for every food but they’re so comfy for me. Problem is they wear down rather quickly so I get at least 2 (sometimes 3) pairs every year
[hjgvxyr] (score 1, diepte 1) Also same.
[hjhhn34] (score 1, diepte 1) Blundstones always!
[hjhkf15] (score 1, diepte 1) How do the soles hold up?
[hjgvykm] (score 1, diepte 0) Redback boots.  Oil rated slip resistant, injected molding for the soles, decent variety of styles, comfy as fuck, and last.  Only bummer is they are a bit pricy.  150ish a pair depending on style.
[hjh0o61] (score 1, diepte 0) Hedley and Bennet vans sk8 hi. They sell out super quick and don’t come around often but hot damn these shoes are PERFECT
[hjha8dn] (score 1, diepte 0) Been wearing new balance comp 100s for like a year now, still in wearable condition for the most part and they’re super lightweight. I use bar mats so I never slip but they have awesome grip on the mats!
[hjhbwrr] (score 1, diepte 0) A brand called Bala makes a nice sneaker designed for nurses - but I’m a barista and rotate these with my vans. Would think they’d be good for anyone else who stands all day.
[hjhc9zz] (score 1, diepte 0) I’ve been wearing black leather keds champions for years.. they just work well for me.
[hk1lmfg] (score 1, diepte 1) Do you have a link? The only pair I found was a pair with insulation and "winter soles"
[hk40mvb] (score 1, diepte 2) [here they are](https://www.drmartens.com/us/en/p/24382001) they also come in chelsea
[hjhg6yr] (score 1, diepte 0) Snibbs
[hjhk0n0] (score 1, diepte 0) I wear black on black nikes, they’re not non slip but we have mats so I’m going for comfort while I can
[hjhl23o] (score 1, diepte 0) This is very interesting as I went for a trial shift tonight where I was told I must wear smart leather shoes, which in my opinion are quite prone to slipping. I wore black and was told next time to arrive in brown leather shoes.

When I first started bartending I used to wear smart shoes but the reality is they're not very practical and are beaten by trainers every time. They also get destroyed very quickly if the bar floor gets sticky which is not uncommon on the weekends.

The bar I did the trial at had extremely high standards. It was a hotel and Idris Elba and Andy Serkis was there (no i didn't meet them). I naively didn't know what I was getting into as I have only ever worked in what is by comparison more casual  places.

So yeah op i would say trainers for grip and mobility.
[hjjim64] (score 1, diepte 1) If you're in a scenario where you need smth that passes as formal, Cole Haan Zerogrand range has some stuff that can have you covered without complete foot annihilation
[hjjiw4m] (score 1, diepte 2) Good to know but I think I will decline the job offer and work somewhere more casual.
[hjhpu06] (score 1, diepte 0) I have Keen kitchen shoes. They have that Frankenstein look that kitchen shoes tend to have, but they’re non-slip and sturdy af.
[hjhwdzq] (score 1, diepte 0) Sketches babbyyyy
[hji0fgg] (score 1, diepte 0) Doc Marten oxfords (not brogue lol) for the five star and Adidas for the dive bar, never had to mess with insoles !
[hji4e4o] (score 1, diepte 0) Blundstone’s or Allbirds.
[hji7a34] (score 1, diepte 0) The Hedley and Bennett Vans are pretty rad. Slip resistant. Stain resistant. I've bought three pair so far.
[hji7u0g] (score 1, diepte 0) Slides to set up, boots for serving.
[hji9h9q] (score 1, diepte 0) I use the emeril lagasse shoes and they’re the comfiest pair I’ve ever owned, just replaced my first worn out pair
(6 reacties met lagere score weggelaten)

=== THREAD 5t1c3j ===
SUBREDDIT: r/Frugal
DATUM: 2017-02-09  SCORE: 152  REACTIES: 84
TITEL: Shoes for 12 hour days on concrete floors
POST (source_id=post):
I am about to start a new position at a warehouse that will have me on my feet for 12 hours a day.  I am worried my feet will start aching mid day every day.  Does anyone have any shoe suggestions to make life easier for me?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ddjinzl] (score 109, diepte 0) Get two pairs and switch from day to day. It will make them last much longer and there will be differences between the pairs that will reduce the development of sore spots. 

I work 12 hour days in extreme heat on concrete and walk over 20 miles a day.
[ddje20k] (score 52, diepte 0) Insoles.  Because you will most likely need steel toes. And even "comfortable" steel toes have nothing on wearing insoles.  Source : work in a warehouse 12 hours a day.
[ddk1dew] (score 48, diepte 3) I was gonna guess that.
[ddjtymm] (score 42, diepte 2) Wear your favorite slippers in a pair of Moon Shoes.
[ddjzhv0] (score 34, diepte 2) Pretzel bakery.
[ddjs0dk] (score 33, diepte 0) Add me to the insoles crowd.  The kind I like are called Superfeet, and there's a variety of them for different types of duty.  They mold themselves to your sole over a couple of days.  Their site tells you where to buy them, but Redwing shoe stores carry a private-label version that's really Superfeet.
[ddjfonq] (score 26, diepte 0) My wife is a server, so we googled "shoes for waitresses" and found amazing shoe suggestions. We got her Clark's at 1/2 price at JCP and they are super mega comfortable. There's Dansko as well, and others, that are made for what you do.

Just, of course, don't cheap out on shoes (but look for sales!)
[ddjypf7] (score 25, diepte 2) Sounds like he works in literal hell
[ddjxg5v] (score 21, diepte 1) I used to switch shoes and socks in the middle of the shift if I knew it was going to be 12 plus hours
[ddjt92y] (score 20, diepte 1) What do you do??!
[ddjfddb] (score 17, diepte 1 OP) Actually, steel toes aren't required.  I can wear whatever I want as long as it's not open toe.
[ddk3a6f] (score 15, diepte 1) At first I was confused as to why you were married to a computer.
[ddju5a6] (score 12, diepte 2) Steel factory comes to mind given the conditions they mentioned.
[ddk0g60] (score 11, diepte 3) Amazon?
[ddjdc81] (score 9, diepte 0) Will you be moving around and walking or standing still? If youre standing still its against the law of they dont put a cushion standing may down. 

Before anyone gets at my throat, thats the employer law by me. Idk where OP is. But if your standing in one stop a good pair of shes and a mat to stand on will help.
[ddjfejf] (score 8, diepte 1 OP) I believe moving around.  It's in a Walmart Regional DC.
[ddjzrxc] (score 8, diepte 1) Clark's +1
[ddjn2k9] (score 8, diepte 0) Crocs makes a shoe that kind of looks like a chuck taylor. I think they only sell them online now. But they are like 30 bucks and they are the most comfortable and durable shoe i have ever owned. They feel brand new even after a year of daily wear. And they are antimicrobial so they wont smell bad.
[ddjpxmh] (score 7, diepte 2) Dr. Scholes!
[ddjhdnn] (score 7, diepte 0) Redwings, wolverines, or any other Goodyear welter boot would be a good investment.  If you can't spring for a buy it for life boot, at least get some orthotics like Superfeet.  Don't mess around with off brand stuff like Dr. Scholl's, or any of that gel deal, shell out $50 for a real orthotic and your feet will thank you.
[ddk7sso] (score 7, diepte 4) That's about right. I worked at a fulfillment center  in crisplant  (order packaging) for about a month, made me wish I was a picker. I hated it, but the pickers seemed more cheerful.
[ddjwb6c] (score 7, diepte 0) Hey OP. I used to be an Amazon picker. It was 10 hours a day of moving around fast. 

Get two pairs of sneakers, same size and color. If you have the money, one of them should be steel toe. 

Buy supporting insoles to give you additional strength and socks to absorb sweat, because at hour five your arches will start to ache and at hour six you can feel the wetness around. At hour 10 you won't want to move. At hour 12 you'll want to quit. 

Also buy baby powder to absorb odor every night, spray disinfectant to clean inside and out, and good shoelaces so you don't break or trip over them as you work. 

You need work gloves too.
[ddkrz3f] (score 6, diepte 4) Orthodontists are for braces for your teeth. Podiatrists are foot specialists that can get you the custom orthotics
[ddk01cx] (score 5, diepte 1) I found the best insoles and it was unexpected. You see the ones that look all fancy, like walking on pillows, and think that's the best option. I did too until I found this style. I'm not sure of the brand but I know many different ones make them. They are pretty solid, almost no cushioning but before you put them on for the first time you bake them in the oven and then mold them to your feet. The difference is unbelievable and I'll never go back
[ddjh4ll] (score 5, diepte 0) I like Payless Safe-T-step shoes.
[ddjye8s] (score 5, diepte 2) Well, mine do.  Came with the product documentation.  I'm buying them through Red Wing (it's Red Wing branded), but it's a Superfeet product.
[ddjfirp] (score 4, diepte 0) Pretty much anything under the Hoka One One brand will feel heavenly.
[ddjz9uz] (score 4, diepte 1) Got a link, or a name for them?
[ddjpopc] (score 4, diepte 0) Crocs. Extremely comfortable when worn with socks. Without socks can cause blisters.
[ddk19ia] (score 4, diepte 0) I just spent the week walking 10-20 miles a day on concrete for work and I have Keens. These are for women but they make them for men too: http://keenfootwear.com/product/shoes/women/presidio

Cannot recommend them enough. I don't normally walk that much but my feet feel okay aside from a single blister. They're now 3-4 years old and still holding up. I didn't think they were very cute at first but I no longer care, they're cute enough for that level of comfort! Not cheap, but far better than four pairs of $25 shoes would have served me these last several years. 

Edit: I'm tired, math is hard. Better than 4 pairs of $35 shoes.
[ddjz2nw] (score 3, diepte 1) My coworker has a pair of steel toe sneakers that she swears by.
[ddk1y6y] (score 3, diepte 2) I have flat feet.  I wear insoles specifically to hold my arch up.  If I moulded a pair to my feet then I may as well just have flat ones.
[ddjh8w9] (score 3, diepte 0) The best thing to do if your going to be on your feet all day is to buy a pair of insoles. I recommend buying SOLE insoles, they may be a little bit pricey but it is worth it. For boots, I would recommend timberland, wolverine or red wings($$$)
[ddjtrlj] (score 3, diepte 0) This comes up a couple times on reddit. Another thread suggested [Danskos](https://www.dansko.com/Home).

Find the kind you want and shop around
[ddklgtp] (score 3, diepte 1) If he's in a warehouse, more than likely he'll have access to dessicant packages. Much better for shoes.
[ddjwpwz] (score 3, diepte 0) Although it's about $200, Adidas Ultra Boosts are the most comfortable shoes. Period.
[ddjzbx3] (score 3, diepte 0) The New Balance 860 is $125, and amazing. Combine it with the New Balance Stability Arch for $45 and you have the best damn thing on the whole damn planet.
[ddjzct5] (score 3, diepte 0) My go to shoes are New Balance brand or shoes for crews. Those provide fantastic support and then inserts on top of that make 12 hours a breeze. 12 hours are my short days. I'm a professional Chef and a substitute teacher at a k-12 school. Working 60 hours a week I can say I rarely complain about my feet.
[ddkq68h] (score 2, diepte 4) I have extremely flat feet and didn't get prescribed orthotics until I was 21. They let me walk twice as long before my feet are hurting.
[ddjfjh3] (score 2, diepte 0) Check to see if you have an SAS store around you. They make extremely comfortable shoes and could probably get you a shoe that will benefit your long standing hours.
[ddjh31h] (score 2, diepte 0) Bring another pair of shoes (not identical to the shoes you wear to work) and switch mid-day if your feet start to feel the effects of standing so long.
[ddjjtkq] (score 2, diepte 0) I recommend Thorogoods if you are considering boots. They're so comfortable and supportive. Run about $150 but will last several years.
[ddjytbm] (score 2, diepte 0) I'm a nurse and I swear by my Keen Work shoes. Very comfortable, nonslip, and fairly waterproof. I've had my current pair for about 4 years and they're just starting to wear out. Also, I don't do insoles. I have a Rolfer who helps me with proper walking techniques.
[ddjyws7] (score 2, diepte 0) Keen Presidio were my favorite shoes when working at a standing on concrete all day job. Was a dog groomer for 10 years.
[ddkdckk] (score 2, diepte 0) Superfeet indoles or inserts. Find a runner's shoe store and have them truly fit you for the type of support you need. They can watch you walk and tell you if you over pronate, need mid foot stability, etc. Once you know what you need you can shop around.
[de6mzvy] (score 2, diepte 1) I know it's been two weeks since you commented, but have you ever looked into custom orthotics?
[ddmir3x] (score 2, diepte 0) I'm a big Keen fan - I need to wear steel toe equivalents and stand on concrete as well.  I also use superfeet insoles and also Powerstep insoles (even better arch support).  Good luck!
[ddklfss] (score 1, diepte 3) Orthotics.
[ddk6vn4] (score 1, diepte 2) In that case my suggestions is skechers gowalks, I love these shoes, it's my only pair of shoes that I've found super comfortable without insoles lol.
[ddklfd8] (score 1, diepte 2) Brand?
[ddkvbnb] (score 1, diepte 3) I'm guessing it could be Brahma or Chrome.

https://www.walmart.com/ip/Brahma-Men-s-Grate-Steel-Toe-Skate-Sneaker/27420222

I wear these as work shoes and I'm on my feet and moving around 8-10 hours a day and I find them to be comfortable. People here might argue with me about the fact that a shoe from Walmart actually works.

Could also be Keen

http://www.zappos.com/p/keen-utility-destin-mid-black-gargoyle/product/8382763/color/55057

Caterpillar

http://www.zappos.com/p/caterpillar-brode-steel-toe-black/product/8101144/color/3?zlfid=191&ref=pd_detail_2_sims_sdp

ETC...
[ddklf5q] (score 1, diepte 3) Then you'll need to go to an orthodontist and get actual prescribed orthotics. Your feet will love you.
[ddkleff] (score 1, diepte 2) Your conflating insoles with orthotics.

Insoles are soft and are to provide visioning. Think, a pillow for your feet and you'd have a decent analogy.

Orthotics on the other hand, are stiff because they provide support. Much like the arched backs on chairs support your mid/lower back.

Could you provide some additional information on what your raving about?
[ddkes7q] (score 1, diepte 1) I used to sell these. They are way more expensive than they should be. We'd get commission for selling them in a non commission based store.  Look into better brands
[ddli12i] (score 1, diepte 2) So your saying she has a rack?
[ddjku1h] (score 1, diepte 0) What's the old saying? Don't go cheap on anything between you and the floor. Shoes, tires, matress.
[ddjmkke] (score 1, diepte 0) I have a pair of thorogood boots with the wedge sole. I know they are 150.00 a pair, but they have lasted me three years, plus I can get them resoled. I work it a Warehouse.
[ddjsygq] (score 1, diepte 0) Nursemates! I'm on my feet in them as a server +/- 45 hours a week, 6-10 hour shifts. They come in a variety of colors and styles, leather uppers and non-slip soles, and virtually no break-in period required. My last pair lasted 14 months of constant wear.
[ddjxg1g] (score 1, diepte 0) Powerstep brand inserts and they are cheapest on eBay :)
[ddjy3fp] (score 1, diepte 0) I really like Vionic insoles. https://www.vionicshoes.com/

I had a 12 hr job with a concrete floor and miles of walking on pavement. I tried many kinds of shoes, boots, insoles, and the like. Vionic insoles in two pairs of shoes are the best.
[ddjymb4] (score 1, diepte 0) In addition to insoles, also look for good socks.  I tend to wear nursing socks with compression through the calf, but I have health concerns.  YMMV.
[ddjys3p] (score 1, diepte 0) I'd recommend two pairs of Brooks and orthotics.
[ddkof3k] (score 1, diepte 1) Yeah, I worked the better part of a decade in restaurants, standing for 10+ hours a day and New Balance were a godsend.
[ddk0o2g] (score 1, diepte 0) Try as many shoes as you can before purchasing. 

It took me years to realize that you don't have to "break in" shoes before they're comfortable (assuming you have a somewhat normal foot). I spent a lot of money on inserts before a friend at the shoe store made me try on a couple dozen pairs. Manufacturers use different "foot models", and your foot will be closer to some than others.

Also shoe shop at the end of the day, after standing for several hours - your feet won't be the same size as they were in the morning.
[ddk0vgh] (score 1, diepte 0) I am and have been on my feet on concrete for 10 years. My podiatrist recommended Altra Provision Walk shoes. I think they are the best I've ever had. Even my cardiologist thinks they are great. The brown ones cost a lot less than black. $58.00 on Amazon.
[ddk175a] (score 1, diepte 0) Also keep in mind it will be tough on your feet the first weeks but it gradually gets better as your body adjusts.
[ddk34ll] (score 1, diepte 0) Adidas pure boost shoes are so comfy
[ddk7i8h] (score 1, diepte 0) I find nothing beats my Merrells for standing all day. My son works in a restaurant and the new shoes he bought didn't handle the all day work and he switched to Merrells and it worked for him as well.
[ddk8v0l] (score 1, diepte 0) Good pair of shoes that fit correctly. I swear by compression work socks by Duluth.  I wear these socks & a pair of Danners working lumber. On and off forklift all night.
[ddka3at] (score 1, diepte 0) Dansko's. Surgeons/nurses swear by them.
[ddkb83s] (score 1, diepte 0) I used to work in a plant that made auto parts working 12s. I had a pair or timberland and a pair or wolverine boots that I switched out every day.  Worked well for me. I also had good thick work socks to go with them.  I liked the gray ones.
[ddkd0gj] (score 1, diepte 0) They're called boots. Big rubber soles. Check em out.
[ddkdv8t] (score 1, diepte 0) Crocs saved my feet(they are completely flat, I have zero arch whatsoever). Found a pair for $12. They are hideous but they seriously saved my feet.
[de6q7ai] (score 1, diepte 2) I never had the money for them or health insurance (I have insurance now). I even went to a podiatrist and she freaked out when she saw that I had no arch at all. Also had those Dr. Scholl's custom ones and they killed my feet.
[ddkm2kf] (score 1, diepte 0) I'm all for getting better shoes and what not. But how about you get better legs. 
I mean do some leg exercises. Build up those leg muscles. I'm a fan of leg extension and the leg press.  Plus I sometimes stand in the sides of my ankles.
[ddkouvh] (score 1, diepte 0) After a visit to a foot specialist (surgeon not podiatrist), I started using Aetrex insoles per his recommendation. They also make shoes, but their insoles work well with most shoes. You need to know whether you have flat or high arches and whether you pronate or supinate. Figure this out and get appropriate insoles.
[ddkprc6] (score 1, diepte 0) Go to a specialty shoe store and tell them what you'll be doing. It will be expensive but this isn't something you want to cheap out on. The problem is with a job like yours your shoes will be torn to shreds so keep that in mind as well.
[ddks1hf] (score 1, diepte 0) I've been a restaurant manager for 20 years. Once I got moc toe boots I've never gone back. Redwing, Chippewa, etc... the cost 50% more and last 3-4 times as long as the shoes I used wear.
[ddksibr] (score 1, diepte 0) Dansko clogs are beloved by retail workers, surgeons, chefs, nurses, and waiters for being stable, durable, and non-slip with awesome arch support. If you have to wear a specific shoe type, I recommend aetrex insoles. They're the best things if you don't have a prescription. If you've got $200-$300 to spend, MBTs are great for standing/walking if you don't have an inner ear imbalance.
[ddmgxiy] (score 1, diepte 0) Under Armor Boots
(2 reacties met lagere score weggelaten)

=== THREAD aau13a ===
SUBREDDIT: r/ems
DATUM: 2018-12-30  SCORE: 548  REACTIES: 84
TITEL: Show up to find a jaundice, cool, diaphoretic, extremely lethargic pt with a pressure of 70/40. I look at family and ask what his medical history is, they say, "uh... he has psoriasis on his feet."
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ecv3v0q] (score 184, diepte 1) His feet must really bother him
[ecv23fa] (score 174, diepte 0) “Ooooohh! You meant you wanted to know about the kidney failure?” As we’re pulling into the ED
[ecv4cz4] (score 125, diepte 0 OP) also forgot to mention that when i was on scene i said to family, "how long has he been like this?" they responded "about 3 days."  wtf is the matter with people man come on............
[ecv2f0t] (score 123, diepte 0 OP) Came back to the ED a couple hours after we dropped him off and his pressure was 50/20.  Family was outside of his room crying and there were a bunch of nurses at the nurses station talking about him.
[ecv8lcj] (score 114, diepte 1) Oh, that! Well, that's not history, that shits going on right now.
[ecvakcj] (score 108, diepte 2) No he doesn't have that anymore he takes medicine for it.
[ecv2dj9] (score 94, diepte 0) Don’t take those socks off. Seriously. Don’t. Inhaling dead foot flakes is worse than inhaling asbestos.
[ecvdkat] (score 88, diepte 3) Fucking right. 

“Do you have an cardiac history” 

“Umm...no.”

(Wife 20 mins later) “He takes lisinopril, Plavix, Coumadin, metoprolol, and that box with cords running from his chest is his LVAD.”
[ecv2gyn] (score 68, diepte 0) Psoriasis location has a direct correlation with lower blood pressure.  I’ve also been told, “he wears glasses” affects heart rate.
[ecv9skk] (score 66, diepte 1) One of my favorite holiday one's was this past Christmas Eve. Elderly male fell getting out of his chair, hit his head on a coffee table. Not quite unresponsive, but close. Vitals are all more or less good but he ain't waking up to anything. I'm thinking head bleed. Can smell alcohol, ask if he's had anything to drink. Family says he had a few. Trauma alert, whole 9 yards.

Get him into ER and as we're leaving, I hear the son tell the doc "he drank 3/4ths of a 1.75 of vodka"
[ecv6076] (score 66, diepte 0) “I see here you are taking glucogen. How long have you had diabetes?!” “Oh, I don’t have that anymore. I just eat better and it all went away.”  (While drinking big gulp orange soda)
[ecv65by] (score 59, diepte 2) Thats sum real bad psoriasis
[ecvaak9] (score 57, diepte 0) Patient altered, posturing, divergent pupils, chest contusions, pale, diaphoretic, rate 170, bp 90/60

"He has a master's degree, he's very well read"
[ecvdkli] (score 49, diepte 3) “Do you have any medical history?” 

“No” 

“What medicines do you take?”

“Metoprolol, lisinopril, Ativan, aspirin, . . .”
[ecvc6io] (score 47, diepte 5) You'll smell it through the socks if he's gangrenous. And if you're going as cellulitis, it'll at least be a little red above the ankles. 

Cully's ambulance rules: no work vaginas and no unnecessary foot unsheathing.
[ecvc9sq] (score 44, diepte 1) I just go for meds first anymore. Everybody's just so healthy until you get in their med list.
[ecv8m8b] (score 43, diepte 4) diabetic gangrene and sepsis at the feet?
[ecv66i5] (score 42, diepte 1) Ha when im on my death bed at the ripe old age of 50 im gonna tell them my only medical history is a stigmatism
[ecvf3tp] (score 35, diepte 4) Or worst yet “yeah he takes little white pills. They’re called herpabercaderka or something”
[ecvgaod] (score 35, diepte 4) What medications you take?

I dunno, there's like five of them and one of them is Green I think.
[ecv7hpe] (score 33, diepte 1) Oh I don’t have diabetes 

(Tops out on home scale)
[ecvbxk6] (score 32, diepte 0) "I see, no medical problems. Where are his medications?"
[ecvluf9] (score 32, diepte 1 OP) Where'd you take your EMT, Harvard?  Yale?
[ecvvprm] (score 30, diepte 7) That's literally the story.  People call phenobarbital "peanutbutterballs".
[ecv8a42] (score 30, diepte 3) Well that's some whacker shit if I've ever heard it. If theres no other signs of trauma I don't think it's possible that anything you havent discovered of there feet may be the cause.
[ecw784e] (score 25, diepte 8) Well you had me on the edge of my seat for the whole thing.
[ecvqo4n] (score 24, diepte 2) TRAUMA NAKED
[ecvoh29] (score 24, diepte 3) My suggestion would be to start by learning the suffixes. Like, -pril medications (captopril, lisinopril, ramipril) are ACE inhibitors, -alol/olol (labetalol, metoprolol) are beta blockers, -zolam (alprazolam, midazolam) are benzos. If you learn general classes, it's not terribly important the difference between alprazolam and midazolam right this second, but knowing what class of drug it is points you in the right direction. I'd also download medscape or something similar on your phone, it can be accessed offline and you can usually look up drugs there by brand name or generic.

Quick Google found this https://pharmafactz.com/medicine-prefixes-suffixes/ which looks like a decent list to start with.
[ecvhp0p] (score 21, diepte 5) That reminds me of the old story about "Penutbutterball" for the epileptic patients
[ecv7zie] (score 21, diepte 1) Why would they take the socks off?
[ecvhn9w] (score 21, diepte 0) Liver failure causes itching lesions on the feet. I'd be willing to bet he was undergoing MSOF due to liver failure. Your mention of jaundice makes me suspicious
[ecvjs78] (score 20, diepte 3) Stage5
[ecvdr7n] (score 18, diepte 5) There was a guy in a neighboring county that complained of some pain in his feet, and was using a wheel chair. This was at some sporting event and the medics offered to take a look, because he normally isn’t in a wheel chair. Lo and behold, necrotizing fasciitis of both feet.
[ecv92h5] (score 17, diepte 1) Are you sure this wasn't a SNF ?
[ecvkvbq] (score 17, diepte 1) Reminds me while in training my instructor said "I figured out how to completely prevent type 2 diabetes, it's called a treadmill"
[ecvo3mt] (score 16, diepte 2) Pffft that's nothing.

I got my Paramedic at Bovine University.
[ecw94ce] (score 15, diepte 4) “So he has end stage heart failure and hypertension?”

“Oh no, not anymore. The medicines cured that” 

“I don’t think you understand how medicines work”
[ecwky6d] (score 13, diepte 4) Or worse

"Do you take any medications"

"No"

"Are you prescribed anything? Are you supposed to he taking anything"

"No not right now"

"Just to be sure, do you take pills at all?"

"No!"

"Oh okay, well I found this medication list with your name on it"

"Oh yeah I forgot about those"


And there's usually like 10 meds minimum at least, not a minor thing at all
[ecvinki] (score 13, diepte 6) Your ambulance rules have just become mine. Thank you for your service 🙏
[ecvgynx] (score 13, diepte 6) Potentially finding the source of the sepsis HOWEVER I wouldnt blame the medic for not doing it but 100% the admitting nurse should do. They can yield valuable information but I agree if sbp is in the 50s it's not very high on my "to do" list as hes septic and needs broad spectrum abx, you can figure out the source later.
[ecvcv0k] (score 13, diepte 2) Yep! If the family even hesitates for a second when I ask about Hx then I just head straight for the bathroom cabinet haha
[ecw9gtr] (score 12, diepte 3) I ask for medical history in no less than three different ways with every patient, and some of them still don’t get it. 

“What’s your medical history? Is there anything you’ve been previously diagnosed with by a doctor? Is there anything you’re currently taking medications for?”

“Nope”

“Okay. Do you take any medications on a regular basis?”

*hands over Kroger bag full of pill bottles*
[ecv7ibj] (score 11, diepte 0) I DONT FEEL SO GOOD HONEY
[ecvsc38] (score 10, diepte 6) Lmao please do tell
[ecwpigv] (score 9, diepte 8) i have an epileptic dog who is on Levetiracetam. we give him the pill rolled up in Peanutbutter so he doesnt spit it back out.
[ecvpq0n] (score 9, diepte 6) Work vaginas?
[ecvlobl] (score 9, diepte 2 OP) it was at home.
[ecw6qcq] (score 8, diepte 2) This is why I prefer to ask 'Do you have any medical issues?'.  You'd think 'medical history' is hardly a particularly esoteric term but I've found that patients (and family) tend to give a more complete response to 'medical issues'.
[ecw9c0q] (score 8, diepte 8) This. Also, deliveries. Don't sleep with coworkers, don't catch babies, don't check and see if they're coming, don't look and see if there's vaginal bleeding (take their word for it). No work vaginas in any fashion.
[ecw7bsi] (score 8, diepte 2) *astigmatism. 

That's the name of the condition. You don't have a singular "stigmatism".

Don't worry, I fucked that one up until I saw it in writing, too.
[ecvkyps] (score 8, diepte 2) Do you have any sources that would help to learn common meds and what they are for.
[ecvxt8r] (score 7, diepte 2) Trench foot in 2018 is no joke.
[ecvv81w] (score 7, diepte 2) Hey at least he would’ve been fed right?
[ecw9l2f] (score 7, diepte 0) I hate this shit. Then you give report to the nurse and the family pipes up with all this info you didn't have- and the nurse is just glaring at you
[ecwanyz] (score 7, diepte 0) Halfway to the hospital "oh, there's something I should probably let you know." "What's that sir?" "About 15 minutes before you got here I took an entire handful of my anti-depressants all at once"
[ecwa52x] (score 6, diepte 4) Same.  I just prefer to replace 'history' with 'issues'.  

You know what's even better?

*hands over unlabelled Ziploc bag full of loose pills*

'Th-thanks...  Well, here's hoping your nurse has lots of pharmacist friends.'

Honestly, some people.
[ecv88h3] (score 6, diepte 2) Full assessmeqnt 

Guy's AMS. Symptoms might be secondary to a trauma
[ecvra8x] (score 6, diepte 5) r/scrubs
[ecw86pc] (score 6, diepte 3) Go Moos!
[ecw2aof] (score 5, diepte 7) I believe he means don't bang your coworkers
[ecvaidt] (score 5, diepte 5) I just don't understand what checking someone's feet could possibly due for someone who needs agressive sepsis care?
[ecvi7gf] (score 5, diepte 6) I got sepsis once from a foot infection. EMS didnt find it. Nurses in the ED did. Didnt really affect the outcome of my case but still would be nice to know.
[ecvogwn] (score 5, diepte 7) I did as well in my early teens from a small scrape. Fortunately I figured out what was going on prior to any assessments, but it would have been relatively easy to miss the red steak running up the inside of my leg.

*Edit* streak, not steak...
[ecwpr9r] (score 5, diepte 3) Read it as “a stigmata” at first and was like “well, shit man thats serious!”
[ecw78gu] (score 5, diepte 2) Skilled nursing family
[ecwiyoq] (score 4, diepte 4) This is why I always ask those two questions in reverse order. What do you take? Why do you take it?

Which inevitably leads to, "Because the doctor told me to."
[ecwl6xy] (score 4, diepte 5) I ask if they have medical history, have they ever been diagnosed with anything, do you have any heart problems, lung problems, kidney problems, and do they have any (organ system that I suspect) problems, do they take medicine or pills on a regular basis for anything 


A little excessive but I tend to get the answers I need through this route of questioning
[ecvoyh0] (score 4, diepte 8) You might want to cook that steak a little longer I'd its running up your leg
[ecw7ubr] (score 4, diepte 1) That's when you add after every medication they list "and what medical condition are you taking that for?"
[ecwjic7] (score 4, diepte 1) Gee, if we'd only thought of just flat out asking them directly. No way they could completely fuck up answering a direct question.
[ecz8ult] (score 3, diepte 9) I'm tired from OT and read that you had an epileptic dog named Levetiracetam and I just had this image of you opening the door to the back yard and yelling "Come on Levetiracetam! Here Boy! It's dinner time!" while the neighbors stare on with much bewilderment and it really amused me. Then I re-attained literacy.
[ecvpkfq] (score 3, diepte 4) Thank you for writing this!!! We just started pharma in Paramedic school! :D
[ecwn81v] (score 3, diepte 3) I'm not blaming the patient, nor being lazy or incompetent.  I'm pointing out that your method of asking a direct question with the expectation of problem solved is simplistic, optimistic at best and most likely futile.
[ecw3p1k] (score 3, diepte 0) Unrelated, but I'd like to thank all y'all. I had several panic attacks this week, and by the third one I was sure something was up with my heart. I spent Thursday night in the emergency department and everyone there was excellent, despite junkie hordes screaming about a three hour wait at 4 AM.
[ed7hcbq] (score 1, diepte 3) *screams internally*
[ecwpsyg] (score 1, diepte 5) i randomly found this somehow - but https://www.[drugs.com/imprints.php](https://drugs.com/imprints.php) lets you describe a random pill, and then the site tells you what it is.
[ecw0wz8] (score 1, diepte 9) Lol, infected with cows. Medicine is a strange business.
[ecw2ov5] (score 1, diepte 6) I just don't understand why you wouldn't want to do a thorough assessment of your patients.
[eczaj8j] (score 1, diepte 7) You already know, or have a very strong field impression, that the pt is septic. You know that what they need is broad spectrum antibiotics,so  call a sepsis alert, get a line, fluids, etc. What difference is it going to make if you know the exact cause of the sepsis or not as far as your treatment of the pt, or even the hospital's immediate treatment of the pt? They will find it almost immediately at the hospital when they change the pt into a gown. Sepsis alerts need load and go since we do not have antibiotics on the truck. I just don't see the benefit of getting every single piece of clothing off if it is taking time that could be spent getting to the hospital and getting a line secured to get antibiotics started asap. Sepsis requires aggressive and immediate care on the side of the hospital and the pt needs to get there asap. They can figure out the cause when they get there after antibiotics are in.
[ecyg602] (score 1, diepte 5) Sure thing man, good luck.
(4 reacties met lagere score weggelaten)

