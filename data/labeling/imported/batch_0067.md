# Label-batch batch_0067

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
Schrijf het resultaat naar `batch_0067.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1qkt9tp, 1iiqigl, u5k1df, 1hkxtti).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1qkt9tp ===
SUBREDDIT: r/Costco
DATUM: 2026-01-23  SCORE: 168  REACTIES: 133
TITEL: Has anyone purchased the Insoles from Costco?
POST (source_id=post):
I've had my current insoles and my dogs have been barking more than usual lately. I'm looking for some new ones. Has anyone tried them? What did you think?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[o191a2y] (score 272, diepte 0) If you have a real foot issue, just shell out for orthotics from your podiatrist.  They’re stupidly expensive, but have truly changed my life as someone with very flat feet.
[o195ymc] (score 67, diepte 3) What a joke insurance truly is. 

“Oh, you can’t walk without pain?  Sorry, we can’t afford to give you $4-500 to hopefully help you, but thanks for paying us $1,000 a month!”
[o193ce4] (score 53, diepte 2) Mine were $300 a few years ago as a reference, easily worth it to be able to walk and stand for more than 5 minutes again
[o19brsn] (score 49, diepte 4) \#LuigiWasRight
[o1925xx] (score 44, diepte 0) Took me a second to figure out why your dogs barking mattered with getting shoes.
[o192blu] (score 39, diepte 0) I have purchased several insoles from "Fit My Foot" and they are simply terrific. I have very high arches and can get sore heels and arches without proper support, and they have done the trick. They were recommended by my podiatrist who said that the worst that could happen is they don't work, and then you'll be out $100, instead of getting custom orthotics for $600.
[o193g4v] (score 34, diepte 2) I paid about $500 for a pair at my podiatrist office. Insurance didn't cover for me.
[o19226k] (score 31, diepte 0) If I keep telling myself “they’ll come to my region” every year it’ll eventually come true… 

https://www.costco.com/fitmyfoot-schedule.html
[o192nlz] (score 25, diepte 1) How expensive is stupidly expensive?
[o19lurm] (score 19, diepte 4) It's all so shortsighted too.  Yep, we won't dish out $500 for orthotics but your poor gait and posture could lead to life altering knee, back, and hip issues that could cost hundreds of thousands of dollars.  Those issues lead to poorer lifetime career outcomes that could lead to having to quit working and existing on poor public funding.  Some CEO will get an extra yacht from enough denials so at least you can be happy for them, right?  Everything about our system is backwards.
[o19cxs5] (score 17, diepte 3) I developed some plantar fasciitis last year and was amazed how much that generic off-the-shelf orthotics changed my life.

Now I know how Jesus felt on *Curb Your Enthusiasm* when Larry gave him the orthotics
[o194551] (score 13, diepte 1) I don’t know why but I have always *hated* that phrase lol
[o194fap] (score 12, diepte 2) My insurance didn’t cover it and it was $750 in a HCOL area.   Some of the best money I’ve ever spent.
[o198sc7] (score 12, diepte 1) I have also purchased from them. I have two. One from WIIV, which was bought by Dr Scholls and changed to Fit My Foot. The second is from Fit My Foot itself. 

I'm a nurse and worked in the hospital until relatively recently. These insoles were fantastic. Them paired with compression stockings and not wearing the same sneaker days in a row, helped reduce feet and leg fatigue as well as back pain. 

Plus I STILL have my insoles that are still in usable shape.
[o1936k3] (score 10, diepte 3) IIRC (got them as a kid when it wasn’t my money) I paid like $800.
[o19m3xe] (score 9, diepte 2) It's an old saying. "My dogs are barking" means "My feet hurt".
[o1919hs] (score 8, diepte 1) "Dogs" are a slang term to refer to feet, especially when they are in pain.
[o193n0m] (score 8, diepte 1) I have a drawer full of inserts. I was so desperate I’d try anything. My podiatrist help me with a few issues and recommended knee radiographs. I ended up having bone on bone and a knee replacement the next year. 
Foot pain resolved within a year afterwards.
[o192g1u] (score 8, diepte 1) If I remember correctly, they’re around $85
[o194lv0] (score 8, diepte 1) Lmao what does quality of a shoe have anything to do with the insoles within the shoes? You realize people buy insoles bc of their foot shape. You can have the world’s best quality shoes but have terrible comfort bc of the shape of ones’ feet.
[o194pol] (score 8, diepte 0) PT here.  I'm very wary of any OTC insoles, because the vast majority are just too soft.  Specifically brands like Dr Scholls.  Yeah, they may feel nice, but if you can squish it with your fingers, your body weight will flatten it and there is no support.  

As for these, the scanning thing is neat but unless you are able to find and keep your feet in [subtalar neutral ](https://www.medbridge.com/blog/what-is-the-value-of-subtalar-neutral-for-diagnosis-and-orthoses)during the scan, it's scanning in the wrong position.  So if you have fallen arches, your new orthotic will be molded in the fallen position and not correct a darn thing.  

If you have issues, go see an orthotist/prosthetist.  They can help.
[o191v66] (score 7, diepte 1) Ditto.
[o191fb9] (score 7, diepte 0) How much are they charging for a pair? A family member of mine might consider these if they're competitive to the $50-70/pair over the counter kind.
[o193dgl] (score 7, diepte 1) So what brands do you buy?
[o195dgy] (score 7, diepte 0) Has anyone answered their question on how these insoles are? I’m fully aware there a many and better options out there.
[o191bdl] (score 6, diepte 1) It’s an expression for tired feet.
[o192yza] (score 6, diepte 1) The details people add 😂
[o195pjv] (score 6, diepte 0) Just an FYI, that's what I think they call a "road show." It's when some outfit buys permission to set up a kiosk for their product line at Costco (like Cutco Knives, massage chairs, pianos, etc.). So I don't know what the guarantees are on these things or if Costco even has anything to do with them beyond being convinced they're up to whatever standards they have for outside vendors.
[o196vrg] (score 6, diepte 0) Dang, Costco really letting all the vendors in. I had to pass a bunch yesterday that were all trying to get my attention. I don’t like it.  Car key, solar, smoothies, T-Mobile, new windows, water delivery, and the bamboo sheet lady.
[o190sbx] (score 5, diepte 0) I got 2 pairs for my work boots and I love them. Better than any store bought ones I've tried.
[o192vfg] (score 5, diepte 2) Im also curious about this \^
[o19j8xh] (score 5, diepte 4) Bruh….Plantar is no joke.  Wait till you get custom orthotics and your feel feel like they are in the clouds :)
[o193cyh] (score 5, diepte 2) They can be around $1000 if your insurance doesn't cover them (most don't).
[o19dv1x] (score 5, diepte 2) When you first get them, they will be uncomfortable while you relearn how to walk on your new insoles. The whole point is that it is giving your feet support in ways that you haven't experienced before and that will inevitably be uncomfortable for a while.
[o198egn] (score 5, diepte 1) So the alternative to a custom solution is a universal neoprene insert that feels nice and squishy when I pinch it in the store, but goes dead flat when I put my 185lbs on it? Cool.
[o19e7xi] (score 5, diepte 0) I developed Plantar Fasciitis and had to see a Podiatrist. He recommended insole supports after my PR was under control. I asked about The Good Feet store in my area, but he said they’re wildly overpriced. Advised me to get PowerStep insoles and gave me a pair. They worked out really well. I’ve had back problems for years, and these helped tremendously. Bought more pairs for my shoes at about $35 each, back in 2023. Just checked and Amazon is selling them for about $52, under the name PowerStep Pinnacle Maxx Orthotic Insoles.
[o19n2qi] (score 4, diepte 5) I was literally just texting my mom about this in reference to vaccines. Because the US is changing their vaccination schedule, there's a chance that some vaccines will no longer be covered by insurance. But why would the insurance company do that when the cost of the vaccine is far less than the cost of treating the disease? 

Same goes for birth control (in reference to those religious companies that were granted an exemption from requiring their insurers to cover it) - it's way cheaper to cover birth control than a pregnancy, delivery, and birth (although then they get a new customer, so more premiums, I guess).
[o19cwha] (score 4, diepte 2) The crime is that these are priced for those who have insurance. A market price would never be that high for plastic foot pads.
[o194c1u] (score 4, diepte 1) If you get them prescribed and insurance doesn’t cover see if you can write them off as medical expense on your taxes. Of course now medical expenses have to exceed 10% of your income but none the less…
[o19499j] (score 4, diepte 0) $535 for full shoe inserts and it's night and day how good they are compared to store bought ones.  Also I roll my foot when I walk so the outside back corner of the heel wears out faster.  They added extra padding in the insole to fix that.  You can't get that with over the counter insoles.
[o197iad] (score 4, diepte 1) Explains why powersteps are my favorite otc insoles.
[o19nxvo] (score 4, diepte 0) Worst tasting sample ever
[o191cg0] (score 3, diepte 1) It's an expression. Dogs mean feet in this context.
[o19scqn] (score 3, diepte 6) Same and we have a single story house.  I had to setup a bunch of objects to help me walk to the bathroom in morning.  I’m talking 10 steps from bed to bath.

Been 6 years pain free for me.  When I first saw the podiatrist, he said let me give you a cortisone shot so we can check your gait because I could not even walk 5 steps.  I don’t why we do it to ourselves but glad it’s fixed now :)
[o19yyz6] (score 3, diepte 5) Grimshaw v. Ford Motor Company explains their faulty rationale IMO. They reckon it's cheaper to spend money on the fewer high $ instances after than offer hundreds per claimant. I'll bet they are also factoring in that most people will opt to pay for it themselves then have it lead to further pain (so it never gets to the expensive level)
[o19pulb] (score 3, diepte 4) I’m going on 2.5 years with mine.  My podiatrist said they’d refurb the softer parts if/when they wear down, but I haven’t done that yet.   Admittedly, I do work from home, so I’m not wearing shoes with the insoles every day.  My Birkenstock slippers are sufficient enough for my pittering around the house, albeit not nearly as good as the insoles.
[o19785y] (score 3, diepte 2) I’m on 2.5 years with mine, and my podiatrist said that if I notice the softer parts wearing down, they can refurb them for me.  Still haven’t taken them up on that yet.
[o196o3j] (score 3, diepte 1) I’m gonna go against the grain and give a negative recommendation to orthotic inserts from a podiatrist. I’ve tried several through the years and they’ve consistently been uncomfortable/hurt my feet. Maybe things have changed but the ones I’ve tried were all super hard and did not help.
[o19gbj4] (score 3, diepte 1) Thank you for posting that! I have never seen them at any of the three stores I go to weekly. So I checked the schedule and they are in my state… but it appears they **only** go to the two stores that are in the “new money” neighborhoods. What a joke.
[o19bziz] (score 3, diepte 2) It reminds of the scene in Planes, Trains and Automobiles when they are the airplane. So gross!
[o193gim] (score 3, diepte 0) I got them and the fit is nice. They weren’t quite what I needed because my foot issues are with my sesamoids (ball of foot). These insoles are full length and have great arch and heel support, but  for the front portion of the foot it’s just a pretty standard insole. If all I needed was arch support, I think these would be great. For my specific situation I ended up with custom orthotics from a podiatrist.
[o195pc5] (score 3, diepte 0) I got a pair and theyve been pretty good. Have had foot issues for the past 12, 13 years and they are pretty comfortable
[o198x0h] (score 3, diepte 0) I don't bother with these things anymore, as much as I wasted owning half a dozen. I've discovered a brand, Oofos. These suckers are incredible, they may not all be super stylish, but it's not about looks, as much as comfort. Highly recommend to grab a pair of any style. Once you enjoy one, you'll buy the full array of form factors.
[o190qrv] (score 2, diepte 0) > I've had my current insoles and my dogs have been barking more than usual lately

Wut
[o191q2a] (score 2, diepte 1) It is an American slang saying about your feet in reference to my dogs have been barking more than usual lately. Dogs = feet
[o19waii] (score 2, diepte 7) Does it ever go away?

I got complacent and didn’t wear the orthotics for a month and it flared up again.  Do I need inserts for life?  I really like wearing sandals.
[o1adfhj] (score 2, diepte 8) Mine went away. Then I got it in the other foot and that eventually went away too.
[o19koj5] (score 2, diepte 4) I didn’t have insurance at that time so that was the cash payment out of my pocket, maybe they gave me a discount knowing I didn’t have insurance
[o19npl2] (score 2, diepte 6) At least for the vaccines, they must’ve determined that the probability-adjusted cost of paying for treating the virus/condition is lower than paying for the vaccine.
[o19qjhb] (score 2, diepte 5) It's because by the time that the lifelong issue appears, you will be on medicare and not their insurance anymore (Or medicaid if the issue fuck you up so bad and put you on disability).
[o1aenmh] (score 2, diepte 5) Their logic is that in a couple years, you'll switch jobs, or your employer will switch carriers.  Your health problem is no longer their issue.
[o1ag84o] (score 2, diepte 6) You're not wrong and when things get too upside down for all of them you'll get dumped on the taxpayer or cast into the darkness of having health issues and no insurance.  Insurance companies are absolute parasites offering little and taking so so much.  The whole idea of how we do it is backwards.
[o194hu8] (score 2, diepte 3) Thank you!
[o19uslz] (score 2, diepte 2) If theyre prescription, there's a chance your insurance covers it. My cost was negligible, and i go back every year to get new ones cuz i wear em out despite them being firm. Soft insoles, like what you get at stores, feel nice but break down so fast cuz they dont actually offer support.
[o19plct] (score 2, diepte 2) Depend on the material. I have been through 3 pairs so far.

* Memory foam pair. This lasted about 3 yrs with daily use. Also it's the least expensive one. I have to replace it because it no longer supported my feet properly. This is not the kind that OP posted but properly coming from the podiatrist. 
* A carbon fiber with the front foam padding. The carbon fiber part pretty much last forever but the foam padding needs to be refurbished after a couple years. But you can also ignore it since the important support is in the carbon fiber.
* A pure carbon fiber one. This only goes down to my arch. And there's no front part at all. So it cannot truly replace insole if you need some soft pad in the front of the shoe. Last forever on this one too.

I suggest you get it. Maybe try it with memory foam first if they have it? You just need to make sure it's podiatrist that do the measurement for the mold. It's critical that the insert supports you back to a proper alignment.
[o19jkt9] (score 2, diepte 2) Road shows ain’t what they used to be. My store just does car keys.
[o19bllp] (score 2, diepte 1) I'm still confused why they needed to add that detail.
[o1a2lmo] (score 2, diepte 3) Learned something new today, thanks.
[o1a4177] (score 2, diepte 3) Thank you. Never heard this saying before. Wonder if it’s regional?
[o19acns] (score 2, diepte 2) Yes--I forgot I purchased from them when they were called WIIV as well! Photo of my foot on a letter sized piece of paper and then 3D printed insoles arrived a week later. I also had a pair made with the merino wool for my ski boots and they are great.
[o196why] (score 2, diepte 2) My feet started feeling better when I shelled out for shoes that were all cork / leather underfoot.  They took the shape of my feet after a while and they fit like custom leather socks.
[o198q97] (score 2, diepte 2) Many podiatrists sell power steps as the first try effort for foot pain.
[o19m2nt] (score 2, diepte 1) The water delivery people at my Costco are always super rude too. I said I just drink tap water and the lady literally said, “Oh, ew!” Okay lady, you can give me the money for your special magic water then 🙄
[o1a9fef] (score 2, diepte 2) The windows & doors guy was standing in middle of the cart exit the other day telling people "don't be lazy!"
[o198so0] (score 2, diepte 0) I haven't seen them at my store but I would definitely try them
[o18zl3i] (score 1, diepte 0) Posts that do not follow r/Costco subreddit rules **MAY** be subject to removal. 

**Reminder: No vague non-descriptive post titles or availability questions.**

When applicable, please make sure that you're using a descriptive post title with product name(s) and/or exact question mentioned as it yields better subreddit search results. 

**Including item number, price, and approximate location or region where found is also helpful since product availability can vary.**


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Costco) if you have any questions or concerns.*
[o1901nf] (score 1, diepte 0) [yep](https://old.reddit.com/r/Costco/comments/1qbal1v/fitmyfoot_experience_anyone_tried/)
[o19l66o] (score 1, diepte 5) It’s vicious.  And I let it get really bad.

You seen that [Nervive ad with the guy who looks like low-rent Lewis Black](https://youtu.be/9wEr8WF4ICY?si=Dlj2jZj4P0ErQdbh)?  The guy getting out of bed and going down the stairs with no pain really spoke to me.  I was afraid I had something really wrong.
[o1astlm] (score 1, diepte 8) It does go away so hang in there.  Are you wearing the brace at night?  Something like this -> https://a.co/d/8kIXzQB

My regimen for making it go away was icing every night by rolling both feet over frozen water bottle for 10-15 minutes.  That calmed the inflammation down for the day.  Then wearing those braces at night and orthotics during the day.  In a couple months it was completely gone so I stopped icing and brace then.  Wore orthotics for couple months and now only wear orthotics when I know I’ll be on my feet for hours or when walking/running for exercise.  Been pain free for more than 3 years now so it’s possible for you to be pain free also.  Just manage it vigorously for now and it will pay down the road.  Stay in good health 🙏🏽
[o1a82dk] (score 1, diepte 4) I caused my own fasciitis (or maybe just sciatica issues) a few years ago due to wear slippers inside during the winter!

I just went with some cheap($12-$20) Walmart, Dr. Sholz stuff, it might’ve taken four months to get back in the swing of things, but it was a real wake up call. I needed to get out of my work truck and start taking some steps during the day!
(48 reacties met lagere score weggelaten)

=== THREAD 1iiqigl ===
SUBREDDIT: r/AmazonFC
DATUM: 2025-02-06  SCORE: 26  REACTIES: 133
TITEL: How do u guys manage foot pain
POST (source_id=post):
I do mixed pack singles and have bought my own composite toe shoes with memory foam insoles. It didnt really help so now i have 3 more insoles i use at the same time and the pain is still the same.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mb7ybs9] (score 20, diepte 0) I don’t manage it. I live with the pain
[mb7rg92] (score 11, diepte 0) Does it feel like a railroad spike in your heel or are you talking about some other pain?
[mb7zrjj] (score 11, diepte 0) Look into compression socks. They'll keep your feet from getting swollen, which can help with pain a lot.
[mb7xmtj] (score 10, diepte 0) Epsom salt baths. Massage and rest.
[mb7sy1o] (score 9, diepte 0) A lot of the times when standing in the same place it can make your feet hurt regardless of insoles, you can try walking in place or ask if you can water spider or tote run for a quarter or2
[mb89h4b] (score 7, diepte 0) Started doing elevated calf raises on a regular basis to strengthen the muscles and tendons in my feet.
[mb8e9ok] (score 6, diepte 0) You really need to get shoes that fit well. I can't stress this enough. I walk 25k steps a day. Keep trying different shoes from Zappos until you get a comfortable pair. Any shoe that has a hard toe should be bigger than your normal shoe and wider
[mb8azhm] (score 5, diepte 0) for those who are suggesting pain killers: be careful it is not advisable to take them everyday..long term effects: liver and kidneys disease. Get some good shoes will help. If the pain persists mayb u still having bad shoes or insoles
[mb7t88a] (score 4, diepte 0) there many comfortable safety shoes i bought sketchers from a Store called the academy sports and out doors and they comfortable never had paid.
[mb83o89] (score 4, diepte 0) Well working for Amazon now 5 years, foot pain no longer exist. Over time it does get better.
[mb8cof0] (score 4, diepte 4) First year was bad, second year not as bad, but would be sore after working 10 hours. 3rd year feet were finally use to the warehouse work being on your feet for 10-12 hours a day.
[mb9j274] (score 4, diepte 1) This is such a good point. I overused ibuprofen for chronic migraines when I was a teenager and into my early 20s, and now I cannot handle any NSAIDs even years after quitting. I cannot eat spicy food either, which I used to love when I was younger. It messes up your stomach lining!!
[mb91e5x] (score 3, diepte 2) I read this is caused by having the laces too tight and my pain definitely subsided after loosening mine. I did not think they were tight at all but I loosened about a finger length all the way down and it made a huge difference
[mb82mht] (score 3, diepte 0) For me it was so bad I was taking a bunch of ibuprofen 500mg. It was really unhealthy but I got me through the day sometimes
[mb8aeto] (score 3, diepte 2) It legit gets better, like I said. I have worked for Amazon for 5 years.
[mb8dh43] (score 3, diepte 5) Your feet calluses are probably harder than obsidian
[mb85fbq] (score 3, diepte 0) If these are new shoes you basically just have to break them in. Took a month or two but now my feet don't really hurt anymore after shift. Now it is just everything else.
[mb85oby] (score 3, diepte 0) Vicodin
[mb8bru3] (score 3, diepte 1) This is the way
[mb8bov0] (score 3, diepte 0) Appropriate feet support , I have flat feet so it’s easy for me.  It’s generally  people do not  how properly support their arch on their feet but most people don’t realize until they get to Amazon and work long hours .

Best find the safety shoes that work for you .

Trust me , I have been at Amazon for 9 years .
[mb8khp9] (score 3, diepte 0) Wide shoes at least half size too big.
[mb8mh6z] (score 3, diepte 0) Go to a podatrist and see if you have flat feet or heel spurs. If you do then prescription inserts will work much better than regular inserts. That's what I use. I have to get new shoes and inserts every 3 months as they lose their support and my feet start hurting again.
[mb8vx9m] (score 3, diepte 0) I had foot pain and no matter what insoles I used. Nothing helped.  until I went to a foot doctor and they told me my arches were very low, and said it was plantar  fasciitis. The only thing I do now is buy the inserts for plantar fasciitis,  the half inserts, and ive never had foot pain since.
[mb92ag5] (score 3, diepte 0) I went to a podiatrist and a couple months of physical therapy and my feet felt 100 percent better. I got a half size up in a EE (extra wide toe box) from Zappos with specially recommended insoles that have additional support at the toe for my specific issue. Use your benefits and go see the foot doctor. The PT included a massage every week that was worth the $$. It cost $30 a visit as my copay.
[mbaiush] (score 3, diepte 0) Memory foam insoles suck on the concrete floor. Dr. Scholl's athletic gel insoles. All my work shoes, or boots are always wide, instead of medium. Also, invest in a home foot massager. I prefer the boot style that does compression on my calves and feet.
[mbanpxs] (score 3, diepte 0) Get yourself one of those cheap foot massager from Walmart the one with bubbles and get some Epsom salt with menthol in it and soak your feet in a mixture of warm water with Epsom, don't forget to thank me later.
[mb7r5kf] (score 2, diepte 0) https://a.co/d/gUFpSuG used these they have helped a lot.I do amnesty and walk  a lot but after buying these don’t feel foot pain
[mb8bqy5] (score 2, diepte 1) Glad I’m not the only one, except mine goes through the top my foot
[mbbvdrz] (score 2, diepte 2) Google Morton’s neuroma.
[mba1rge] (score 2, diepte 1) This is what my feet feel like, plantar fasciitis. Use epsom salt soaks, icing for 15 mins multiple times a day, and rolling out the bottom of your foot with a lacrosse ball
[mbe2bk6] (score 2, diepte 2) I have mine handles with custom orthotics. Was trying to point OP in the right direction. Soft and squishy is not the way.
[mba2zat] (score 2, diepte 3) Now that's an even bigger issue, because amazon gives you $120 credit on there to buy work shoes. I would go to your HR or Wellness and ask for help getting that going. 

They also cover a $65 pair of insoles that made the shoes I had before this comfortable for the whole day.
[mbeqi4z] (score 2, diepte 2) i used my credit last year and bought two pairs on zappos.
[mb7vzcr] (score 2, diepte 0) get yourself a foot roller to use before and after your shift. also soak you feet in a bucket of warm/hot water with epsom salts at least a couple times a week.
[mba025l] (score 2, diepte 1 OP) I do that already but the pain stops pretty much as soon as I clock out
[mbamgl2] (score 2, diepte 2) Look into metatarsal guards and a dr note.
[mb896iw] (score 2, diepte 1) Same.
[mbbvp6g] (score 2, diepte 1) I got compression sicks but I felt like they caused me more pain🥲
[mb7zubh] (score 2, diepte 0) Time and really good shoes
[mb80mwe] (score 2, diepte 0) Like others. Epson salt, compression socks. Looks into free hinge health physical therapy
[mb81zj8] (score 2, diepte 0) Thugging it out
[mb89z34] (score 2, diepte 1) did it get better or did you just become numb?
[mb8c6y6] (score 2, diepte 3) And do you have to wait 5 years for it to get better or did that happen sooner?
[mb8m8wb] (score 2, diepte 3) I've been here going on 5 years and it got tolerable, not better. I think I just killed the nerve endings from constantly being in pain.
[mb85t8m] (score 2, diepte 0) Rubber toe protectors. Game changer.
[mb86nwe] (score 2, diepte 0) I had my dr give me a steroid shot every six months
[mb86q62] (score 2, diepte 0) I second the sketcher through Zapos, but  add compression socks.
[mb87bkb] (score 2, diepte 0) Tylenol is ur best friend
[mba5f4e] (score 2, diepte 1) i do this also but my reason is to get blood flow in my legs and feet
[mb9r9ej] (score 2, diepte 2) I'm in the same boat. If I attempt to take Ibuprofen I get so nauseous and actually end up pucking
[mba0bfu] (score 2, diepte 3 OP) When i did stow and took ibuprofen I got dizzy
[mb8b5z3] (score 2, diepte 0) What pain?
[mba15or] (score 2, diepte 1 OP) The ones I have r reebok I haven't heard of gel pads I just have gel insoles
[mbfabrz] (score 2, diepte 2) Yeah gel insoles is what i meant :)
[mb9cbtc] (score 2, diepte 0) Idk but the foot pain started when safety shoes got implemented. Cause 2 years prior i never felt so much pain in my feet.
[mb9fvop] (score 2, diepte 0) By not having any
[mb9odb3] (score 2, diepte 0) 3 more that you use at the same time?! First you need to consult someone, so you can get proper fitting insoles. Next, it might not be just your feet per se, but also your calves and back, stretch your calves out like you’re a runner (YouTube will help). Diet, water, vitamins, rest all those things can help with muscle fatigue and the aches, so be aware of what you’re putting in your body
[mba2brb] (score 2, diepte 0) New role or new job. My pain never got better just worse. After foot orthopedics and steroid injections I had enough. Standing this long on hard floors is not natural.
[mbh2ias] (score 2, diepte 1 OP) Ill try that. I didn't know u could put pictures in comments so when I got back to slaveazon on Monday I'll show how the ergo mats r placed
[mbb8kd3] (score 2, diepte 0) go to the doctor and start working out, you'd be amazed at how great you feel during the shift if you do a full body stretch before leaving the house and eat a banana.
[mbbcruq] (score 2, diepte 0) I'm in the same situation as you, and I'm gonna quit in May. Make plans to find a better job and use career choice. The pain will never go away and if you get injured you risk spending thousands of dollars in physical therapy and surgeries. It's not worth it.
[mcoup5q] (score 2, diepte 4) Career choice, look it up on atoz and look for CDL
[mbbw222] (score 2, diepte 0) you need roll on biofreeze. I put it on my feet every single morning before my 10 hr shifts, they also make spray
[mbfq3zy] (score 2, diepte 0) I spent a lot of money on many shoes and insoles and none of them.worked...I just learned to live with the pain 😢
[mb7p9ln] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.com/invite/t7jARCs) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[mbihmdg] (score 1, diepte 2) My go to temporary solution is magnilife foot creme with the usual compression socks and ankle brace
[mbd57lr] (score 1, diepte 1) I just went to the doctor over this, plantar fasciitis and was sent to get x rays because there might be some nerve damage. Sent to orthopedic and might need injections :) try different shoe insoles, stretch before work, during work and after. If you still deal with it I would def suggest going to the doctor for it.
[mbgzsgr] (score 1, diepte 3 OP) Today it felt like standing on spikes even with 2 500mg naproxens and 6 ibuprofen but usually it's just like swelling pain.
[mba04s0] (score 1, diepte 1 OP) I did ask that be4 and haven't gotten a response yet
[mb90sny] (score 1, diepte 1) You're so right, I got Sketchers this year with our zappos credit and they are the only pair that's been comfortable out of the box all day.
[mba06wk] (score 1, diepte 2 OP) Idk how to even use zappos
[mbh0l4l] (score 1, diepte 4 OP) When i first started in October I somehow got the black and red reabok shoes for free in the mail but they were so heavy the pain was even worse.
[mbeqyl3] (score 1, diepte 3) That's what I did this year, though i liked the sketchers so much after I wore them I have yet to wear the other pair (those are carharts)
[mb993b7] (score 1, diepte 1) My feet hurt every time I get on the operator picker after 3 hours. A hot shower helps me
[mbasqsy] (score 1, diepte 1) Yep. Have an ingrown toensil that actually went through the skin on my big toe kniwing I wouldn't get paid time off for it. Now get Arthritis in by ankle but still walk all.day picking. Yes, I'm that stupid.
[mbgzdma] (score 1, diepte 2 OP) Pick was so bad that I got an accommodation from my doctor to go back to pack singles. I was just about to start getting write ups until they fired me
[mbgztzk] (score 1, diepte 2 OP) And me
[mbhmv3m] (score 1, diepte 3) I got a magnesium spray that temporarily helps ... honestly, a warm Epsom salt fost soak with a few drops of an essential oil will help too
[mcov5xa] (score 1, diepte 4 OP) The pain usually goes away as soon as I clock out
[md302ci] (score 1, diepte 5) 😅... I have a magnesium spray I occasionally keep in the car. It temporarily helps
(76 reacties met lagere score weggelaten)

=== THREAD u5k1df ===
SUBREDDIT: r/AmazonFC
DATUM: 2022-04-17  SCORE: 144  REACTIES: 130
TITEL: Welp my feet are back to hurting again with these safety shoes.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[i52ghzs] (score 72, diepte 0) I've dropped well over 100lbs and my feet, knees and back stopped hurting. 1 week in saftey shoes my feet, knees and back are hurting again. At least I can't sue Amaz if something drops on my foot.
[i52etrx] (score 63, diepte 0) You have 1 year to exchange them. Do it.

And buy work boots, imho.
[i52ovx7] (score 36, diepte 1) Those Avenger boots are comfy as hell, they’re the best I’ve gotten so far. They are soft like memory foam and fit my wide-ass foot. The rest all gave me a blister on my toe.
[i52qcw6] (score 34, diepte 1) I wish we could sue Amazon because of the safety shoes 😒
[i52fjqd] (score 29, diepte 0) They are the worst.  I’m actually laying here and I haven’t been able to sleep because I’m in so much pain.  I have four pairs of safety shoes and they’re all awful.  Next step is trying more insoles.
[i543k23] (score 25, diepte 3) See, this is the problem. What works for one person, may not work for another. The whole thing just sucks. I've been wearing my raggedy Skechers for almost 5 years, with never a problem. I want them back :(
[i53f6d5] (score 24, diepte 2) No but im fast af boi
[i53dhdq] (score 21, diepte 1) I've tried like 6 different shoes, and they are all fucking absolutely terrible and extremely heavy
[i52me0p] (score 20, diepte 0) Haven’t worn mine all week and they haven’t said shit to me
[i53liuf] (score 15, diepte 2) They suck for sure, but it's a normal thing in a lot of warehouses
[i53ygy7] (score 14, diepte 2) No way! I got the avengers and wanted to cut my feet off and throw them across the building they were so painful. I suffered for 2 weeks before returning them, and now have the merrells with like three levels of those Spenco insoles and stay relatively pain free.
[i52sts2] (score 14, diepte 2) That's not what I gathered from the info.

Why would they give you a year if it was meant for unused?
[i52pmoz] (score 13, diepte 0) Shoulda got sketchers bro im chillin
[i52s9yu] (score 13, diepte 0) Y’all should go to a foot doctor or a high end shoe store I get little to none pain with my timberland pros
[i52vgng] (score 13, diepte 0) In my opinion, these composite toe clogs of mine are causing injuries that I didn't have before, shin splints, plantar fasciitis, knee and hip pain.  I don't wear lace up anything, I have the highest arches/insteps in the world
[i52vgpo] (score 13, diepte 0) You mean clown shoes
[i53pe24] (score 12, diepte 2) i got the reebok sublite comp toes with blue soles (slip-resistance)

the traction sorta feels flat but makes it tolerable  to tread lightly in any surface inbound due to its stiff build yet doesnt take away from how solid it is as a overall work shoe cause of its comp toes. Pretty balanced shoe and i notice when i wear a different pair which is tighter, it makes my toes prone to calluses on the outer edges when i walk all the time.
[i53ow1i] (score 12, diepte 3) i was today years old when i realized that other warehouses didn’t always have to wear safety shoes. but then again i work at an amazon air
[i52k2uc] (score 11, diepte 1 OP) I was wearing vans with the original insoles and my feet were comfortable it felt like I was wearing shoes, I get safety shoes with the insoles also and it felt like was walking bare foot on steel makes no sense
[i52wepx] (score 11, diepte 1) Same here
[i54zpf2] (score 11, diepte 1) The point of the policy is to eliminate your ability to collect workman's comp if you do get hurt, not to protect you.

They don't actually care if you crush your foot as long as they can just fire you and not have to pay the medical bills, which they can if you were electing not to utilize provided safety equipment in violation of your employment contract.

Remember, all policies protect Amazon in some way, not you.  Don't open yourself up to legal/financial punishment just to make a point.
[i543c9u] (score 11, diepte 0) I've seen more people have issues with these shoes than before we had to wear them. I've seen so many people hobbling around, going to AmCare due to foot pain and blisters, etc. I induct a lot, and having to stand for hours on end in those shoes is NOT fun. 

Why is it now our feet are a concern for them? I would think if our foot safety was that important, they would have been mandatory from the very beginning ![gif](emote|free_emotes_pack|shrug)
[i52l2sw] (score 9, diepte 2) gross, thank god it’s not like that at my site lol 💀 maybe they’ll chill after awhile
[i53o3hg] (score 9, diepte 0) I like how ppl don't put what their actual job is when they say the safety shoes don't bother them. I work at traditional sort FC picking and no way I can do my normal 25k+ steps in these kinds of shoes. I've worn safety shoes for over 20 years at my other job and I know what is possible for me. Disregard the fact that the padding in your shoes is gonna be running out every 2 to 3 months. It just doesn't make sense for this kind of work.
[i52thla] (score 8, diepte 1) Vans? Comfortable? 😐
[i53dmuw] (score 8, diepte 2) I have Asolo's. They are alot but worth it imho.
Also carhert and timberland and red wings are good too.
Also for work shoes, hiking, running, etc... you want to buy a half size to 1 full size bigger then your foot. Your feet swell by the end of the day and you will get rubbing if you buy the ones that fit snugly vs a roomy shoe.

Heavy is what makes the shoes better. There's more support and cushion then a tennis shoe.
[i5541vs] (score 8, diepte 3) They're terrible if you have to do alot of walking
[i52rhvu] (score 8, diepte 1) Z-Liner insoles, expensive  - but so worth it.
[i52u940] (score 8, diepte 2) Bruh
[i52ks9p] (score 8, diepte 1 OP) As soon as you walk through the door it’s like 6 people in yellow vests hawking down everyones shoes
[i54ycjo] (score 8, diepte 1) You arent joking, last week on thurs as we were leaving and walking out I turned to my homie and said look back at the doors and count how many people you see limping out and we both busted up laughing lmao holy shit our poor little feet :(
[i52s5es] (score 7, diepte 1) Thought their policy is unused only
[i52qkop] (score 7, diepte 2) They can't do that forever.  Just bring in your regular shoes and change inside.
[i53mscq] (score 7, diepte 0) Your pain does not matter. Only the customer matters.
[i555und] (score 7, diepte 2) I'm at a point to where I'd be willing to sign a waiver. Let me where my regular sneakers, and if I get injured or whatever it's all on me 😂
[i53w3i5] (score 6, diepte 4) I used to work at a different warehouse after I quit Amazon and returned. They are definitely needed for sure
[i52kjhi] (score 6, diepte 0) i’m still not wearing mine lol
[i52mpty] (score 6, diepte 1 OP) Only way I’d smash my foot would be my own fault
[i53rexp] (score 5, diepte 2) Walgreen insoles for working on concrete floor, $14 . And replace them every month
[i543q85] (score 5, diepte 1) Our building has been mandatory since January, and we have a few people who are still wearing their regular sneakers. One of the managers said, don't come to Controls and let me see your feet. Just stay away if you're wearing regular sneakers lol
[i52ocwn] (score 5, diepte 0) I wear em all the time at my FC they're not enforced but I wear them cause I don't want a big box to mess up my toes 😅
[i533ht4] (score 5, diepte 0) They are so clunky. I keep tripping on the stairs because the toe is so big. I actually feel less safe in them.
[i52v3n4] (score 4, diepte 1) What does the height of the boot have to do with it? Does it affect comfort or safety?  I'm assuming you mean height by 4.5"  I looked at some Danner shoes and it says 3" and I was wondering what the 3" is about. I pick yoga pants and pajamas all day.  Yes, sometimes there's a case of Monster Energy beverages but I'm in more danger of toe injury at my home. My Ariat composite toe clogs are giving me shin splints and major foot pain when before I was pain free
[i53mj2w] (score 4, diepte 0) Shoe companys are so dumb, they should have foam or fabric on the toebox inside so my feet doesnt keep on hitting straight metal
[i53r7w8] (score 3, diepte 1) And you might try wearing the right socks.  Make sure they are long enough. Consider getting plus size socks otherwise your socks will wedge against your toes and rub.  I like timberland hiking socks (for men) because they wick away the sweat and are long enough.
[i53ym62] (score 3, diepte 2) Happy cake day !!! :)
[i52p9xq] (score 3, diepte 0) Get blister proof socks, and get decently made or professionally made insoles, your feet will ache, but man it's so much better, I genuinely spent a couple days wages just to get them made and it's the best decision i've made
[i54cnu7] (score 3, diepte 4) Guess I know what I’m doing come next year
[i53abyu] (score 3, diepte 1) First day with these on and I'm already feeling the shin splints coming, I'm trying to be conscious of how much I stress them but still hurts more than my light weight shoes
[i53ushp] (score 3, diepte 1) That's right Mr big stuff.
[i53vjd4] (score 3, diepte 2) If that's what you got from that, I'm sorry.
[i54wj40] (score 3, diepte 1) I worked in Factories and production facilities since 2002, usually having to wear full leather steel toes, sometimes metatarsal guards doing hot work, ESD compliant anti static shoes for electrical work, and none of those felt as weird as the "amazon approved" shoes do. 

The best ones from Zappos I have used were the Reeboks, however zappos rarely has my size in stock. I Said screw it and used my previous job's shoes, Timberland Pro ESD shoes. Not a fan of doing work in low top shoes, no ankle support.
[i53vxua] (score 3, diepte 0) Back when I worked at Amazon I got a pair of Danner’s for my safety shoes and after breaking them in there was 0 pain. Since then I’ve only worked jobs that require work boots and none have caused me any pain. I think the issue is mostly with people getting crappy safety shoes and not some solid work boots
[i54xdtn] (score 3, diepte 1 OP) Eyes
[i53dyp2] (score 2, diepte 2) I've worn vans my whole life and easily find them the most comfortable shoes
[i55qodh] (score 2, diepte 3) No i have these: 

https://www.zappos.com/p/avenger-work-boots-foundation/product/9250510
[i5568sd] (score 2, diepte 4) i think the most ive done was about 10hrs (2shifts) a day and being on your feet all the time esp being a picker will do that 

these shoes are alright just cause i mostly just do 5hr shifts but im not sure if i should switch to my asics or get new runners if that helps 

the only thing i like about these pairs is i dont have to worry about stubbing my toes and theyre fairly dense which deters cold when im in the chilled section
[i549g51] (score 2, diepte 3) Lol go and ask they change it at the begging of the year
[i537s5f] (score 2, diepte 2) Will check them out.  Thank you so much for the suggestion.  😀
[i539nva] (score 2, diepte 3) They saved my feet & back, literally
[i53rtls] (score 2, diepte 3) Those won't last 2 weeks - I'm still wearing my Z-Liners a year later for $30 . . . choice is yours.
[i53surx] (score 2, diepte 4) They work for me but I'll have to try Z liners
[i53pmkc] (score 2, diepte 1) Couldn't you sue on the grounds the saftey equipment you're forced to wear is causing damage?
[i54acgr] (score 2, diepte 2) If they could prove it, but burden of proof is on the complainant. Unfortunately even with proof the case would probably get it dismissed, claiming that the risk of injury is greater without them. Which they can use accident claims to back as those claims out number documented claims against safety shoe use. 

__Best__ one could hope for honestly, would be getting doctor to write accommodation to not wear safety shoes. In which they *may* get Amazon to honor if the employee signs a liability waiver…
[i54b3xw] (score 2, diepte 3) Yea, that's a valid point. I see a lot of people complaining about these shoes.
[i52j4vk] (score 2, diepte 0) The shoes I got have been solid for me. Danners I think Is the name. Like night and day from the running shoes I was using.
[i52wmg0] (score 2, diepte 2) I have yest to see this,  UT I do walk in 30 minutes before my shift starts.
[i53qr6p] (score 2, diepte 1) I believe that wholeheartedly
[i53slud] (score 2, diepte 2) Danner...sorry
[i556vi5] (score 2, diepte 4) Im not your bruh guy
[i53fe5r] (score 2, diepte 1) The composite merrell moabs are even better. I have all three... hiking, steel and composite
[i53vnw8] (score 2, diepte 2) I totally agree with what you're saying
[i53thcd] (score 2, diepte 1 OP) What did you smoke today?
[i53w740] (score 2, diepte 0) opposite for me, whatever composite toe nikes i got when i was hired were nice asf, got insoles with the spare change, they're pretty much the only shoes I wanna wear now

yeah there's 5lbs of shoes on my feet but the amount of cushioning? i don't want to ever feel my feet, those are just gonna have to be my daily beaters now and my two pairs of "nicer sneaks" feel like there's nothing on my feet
[i5494bs] (score 2, diepte 0) How do they check if you're wearing them?
[i549zn3] (score 2, diepte 0) The problem is shoes feel to heavy for me for all the walking i do 60miles on average working only 40 hours lol
[i55d38f] (score 2, diepte 0) Get insoles, wear quality thicker socks, and go a half size bigger! That’s what really helped me.

Edit: I got my socks at Duluth trading. I really felt the socks made a huge difference, as silly as it sounds.
[i52d92j] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. We have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[i55q6iu] (score 1, diepte 2) [these ones?](https://www.zappos.com/p/avenger-work-boots-breaker-black/product/9368718/color/3)
[i6e2k1g] (score 1, diepte 3) If you are not 100% satisfied with your purchase from Zappos you can return your item(s) for a full refund within 365 days of purchase. (Returns must be unworn, in the state you received them, and in the original packaging.) Some items ship with an attached security tag. Merchandise returned without the original security tag attached or a damaged tag may not qualify for a refund. For more information on returns, please see the Zappos Shipping and Return Policy.
(48 reacties met lagere score weggelaten)

=== THREAD 1hkxtti ===
SUBREDDIT: r/Construction
DATUM: 2024-12-23  SCORE: 272  REACTIES: 129
TITEL: Man with no arms is a skilled electrician using his feet
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[m3hx9a8] (score 151, diepte 0 OP) The group in the venn diagram of gay electricians who have a foot fetish are going to love this
[m3hzs5g] (score 65, diepte 1) You pay by the foot.
[m3hymh4] (score 43, diepte 0) Imagine calling for an electrician and a man with no arms shows up.
[m3i15gc] (score 41, diepte 1) It’s just a circle
[m3hxvxg] (score 41, diepte 0) What’s he do on a ladder?
[m3hxlrf] (score 39, diepte 0) As long as I don't have to pay by the hour
[m3hzyak] (score 39, diepte 0) I expected it to end with the dude having two hands both with beer cans in them..
[m3i0ic4] (score 39, diepte 0) He's no handyman.
[m3i2qd8] (score 29, diepte 0) And he still doesn't sweep up after himself ..
[m3ijqru] (score 25, diepte 2) He hangs upside down from his cock
[m3igjyy] (score 14, diepte 2 OP) Well played... well played
[m3idkle] (score 13, diepte 1) Is this a what a footjob is? I’ve heard of people getting them, but never had one personally.
[m3ifyf8] (score 13, diepte 1) Osha said he can have 1 point of contact so he's good
[m3id6kk] (score 12, diepte 2) I would trust a skilled man with no arms before I'd ever trust the m************ that built my house again
[m3i4hqc] (score 11, diepte 1) You must be a shit supervisor at JCH Sheet Metal. Not impressed by a guy with no arms 😂😂😂
[m3i3u76] (score 9, diepte 1) No gloves either
[m3i8r72] (score 9, diepte 0) "Gotta wear steel toe boots on this job site"
[m3hz0rm] (score 8, diepte 1) They feel off the instant he picked up a broom
[m3hyejz] (score 8, diepte 0) No boots, no hard hat, no safety vest. Get off of my job
[m3i0w6y] (score 8, diepte 1) With the other foot
[m3i5h5v] (score 7, diepte 1) Unfortunately that would be a serious liability issue. Couldn't imagine something going wrong or an accident and having to explain to my insurance that the guy had no arms and was using his feet.
[m3i60b0] (score 7, diepte 1) I mean, he *IS* an electrician...
[m3i14bt] (score 6, diepte 1) Lmaooooo
[m3i5p6z] (score 6, diepte 2) 🤣🤣🤣 the standards are high! No excuses! Make your shift!
[m3isjpb] (score 6, diepte 0) Electricians will do anything to not have a broom in there hand
[m3i8e8b] (score 5, diepte 1) S tier edit
[m3i2do5] (score 5, diepte 3) It's literally 12 minutes old and is most upvoted comment. Stop shit commenting for internet points.
[m3kyf2p] (score 5, diepte 2) You, too, can avoid destroying your body by chopping off your arms!
[m3i7jr6] (score 5, diepte 3) If you got time to post on Reddit you got time to cut some metal
[m3j54js] (score 5, diepte 1) he’s a footyman
[m3itwog] (score 4, diepte 2) I’ve had one. Just the one, and it was surprisingly nice.
[m3i20ur] (score 4, diepte 2) You glorious beast!
[m3i2hzk] (score 4, diepte 2) At least this guy doesn't want handouts...
[m3ijvf9] (score 4, diepte 1) He wouldn’t be able to point the finger at anyone if he makes any mistakes.
[m3i5u1k] (score 4, diepte 0) Don’t come to US because OSHA will make him hear boots. Then he is screwed. Awesome he is able to enhance his feet to do amazing work.
[m3jckab] (score 3, diepte 3) Don’t need opposable thumbs when you have an opossum dick.
[m3k40g7] (score 3, diepte 1) He will never have to do Overhead work, on a ladder/lift, or low work with bent back or knees...  he's found his way to avoiding all the long term body problems the trade brings
[m3hyhqe] (score 3, diepte 0) i wanna see the porta potty video though..  omg that sounds gross.. but yeah how tf
[m3iokhq] (score 3, diepte 3) Lmao love it
[m3hza4t] (score 3, diepte 0) Not borrowing his tools
[m3hzu2k] (score 3, diepte 0) Bullshit. 

They never show them picking up the tools,  running the wire,  anything.

It's sit here, we'll place the tool in your toes,  take the shot and edit for views. 

These piss me off because it's a lie for emotional blackmail for views.
[m3ibnnc] (score 3, diepte 4) I am using the talk and type feature while working a double shift. I came in 1 hour early, even though I was shot six times #MadeMyShift
[m3i7hhq] (score 3, diepte 2) If *BE* impressed if he was actually doing half the stuff they make it look like he is doing. 

One of my kids is a double amputee for context.
[m3jcuap] (score 3, diepte 1) Pretty sure that would be a reasonable accommodation.
[m3ll6h2] (score 3, diepte 0) That quite a feat...
[m3ib31w] (score 2, diepte 2) Hands or feet he should have license and do final revision. If he manages that then insurance can't do anything about it (although they'll for dure try)
[m3hzpxv] (score 2, diepte 0) How does he clip his toenails?
[m3r3h6u] (score 2, diepte 2) His Mouth?
[m3i35d2] (score 2, diepte 1) Picking up the tools? That's way easier than operating them like this. Obviously, someone else ran the wire for him, he didn't pretend he did that? Are you dumb?
[m3igryj] (score 2, diepte 2 OP) You got the acronym wrong but nice call back
[m3i44lh] (score 2, diepte 1) I mean couldn't he technically sit on a really thick rubber mat?
[m3i0u1k] (score 2, diepte 0) I'd love to see a safety guy come up to him on a site.  Do they tell him to put on boots or footys
[m3i4cnv] (score 2, diepte 1) I seem him doing drywall too I think. Or at least smoking crack before staring to work.
[m3i4jqa] (score 2, diepte 2) Hey he needs a little pick me up so what we all do sometimes.
[m3i5f7n] (score 2, diepte 1) 🤣🤣🤣 So true!
[m3iarpn] (score 2, diepte 1) How's he supposed to sweep with no arms?! 

/s
[m3jg6wz] (score 2, diepte 2) They would make him wear boots while walking then he could take them off to do his work in one area. Pain in the ass but I doubt that would stop him.
[m3ilcvx] (score 2, diepte 0) Okay this is pretty good, kind of a heel move to promote your armless work, also seems like he’s working from the sole, which not a lot of contractors do so props, it’s easy to lose yourself in the lock step of life  … all in all this man’s 2’ taller than most of his competitors! He’ll surely rise above the rest when he comes toe to toe with his competitors
[m3iy517] (score 2, diepte 1 OP) Good thing you're not JMH sheet metal
[m3kvtpc] (score 2, diepte 2) No no he’s better than you too.
[m3iskxw] (score 2, diepte 1) *Electricians will*

*Do anything to not have*

*A broom in there hand*

\- D0n\_kebals

---

^(I detect haikus. And sometimes, successfully.) ^[Learn&#32;more&#32;about&#32;me.](https://www.reddit.com/r/haikusbot/)

^(Opt out of replies: "haikusbot opt out" | Delete my comment: "haikusbot delete")
[m3me3c3] (score 2, diepte 0) At least homie has an excuse for not sweeping up
[m3i1fa0] (score 1, diepte 1) It’s a pretty simple Venn Diagram. Two groups: gay, and foot fetish.

In the middle where they overlap you get electricians.
[m3kb1mw] (score 1, diepte 3) Right like I understand not wanting to sit on your butt and collect disability but losing both of your arms at an early age should warrant some kind of compensation like or at least a career change but I get he doesn’t want his knowledge going to waste it’s conflicting because 1 don’t take hand outs 2 if he didn’t have an insurance or savings we can’t just give him free checks for life fs 3 he lost both of his fuck arms
[m3lc1w7] (score 1, diepte 4) https://imgur.com/gallery/l7kXQIM
[m3k3k4n] (score 1, diepte 2) He bites the rungs


Chomp, step, step, release, chomp, repeat
[m3hyaun] (score 1, diepte 0) Who wants a panel 3" AFF?
[m3hydqn] (score 1, diepte 0) Call me crude but I just have to ask.. did he electrocute his arms to death? I must know.
[m3hzo2j] (score 1, diepte 2) Ha! True that. The amount of trash the fker leave in a single 3x5 blows my mind. I have a silicone sink-drain stopper that I stick on the end of my shop vac so it only picks up sawdust and no solids. I'm not weighting down my vac with electricians trash. Then I pick up my wood scraps and leave the room exactly as I found it.
[m3hygii] (score 1, diepte 0) Here’s proof, boys.
[m3j2h9a] (score 1, diepte 2) But it's be his insurance that handles that anyway not yours?
[m3j2tsj] (score 1, diepte 3) Not necessarily and you'd still have to declare to yours either way if it happened on your job site.
[m3ig0u0] (score 1, diepte 1) "well at least he wont make that mistake again."
[m3ijk57] (score 1, diepte 1) I've known some fromer linemen with one arm and one with no arms. He held a stick in his mouth to type. Live front transfomers were a bad idea.
[m3hz5ud] (score 1, diepte 0) Imagine having to borrow tools from this guy on a hot day
[m3icuu0] (score 1, diepte 5) https://youtu.be/bnHisRxQXgA?feature=shared
[m3jguwr] (score 1, diepte 1) It's also low voltage
[m3kvxpd] (score 1, diepte 1) You have not seen the farmer with no arms then? 

He fucking does everything himself. 

They are just super inventive. Any idea of limits dissapeared after I saw the american farm dude.
[m3i0d54] (score 1, diepte 0) Still won’t clean up after he’s done working…
[m3iyx0a] (score 1, diepte 1) A goated user name with a goated comment. I’d give an award if I had one
(52 reacties met lagere score weggelaten)

