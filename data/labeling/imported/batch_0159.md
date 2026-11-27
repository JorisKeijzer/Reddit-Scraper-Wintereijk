# Label-batch batch_0159

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
Schrijf het resultaat naar `batch_0159.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1678cdl, 1ds76aj, p2l2yr).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1678cdl ===
SUBREDDIT: r/Biohackers
DATUM: 2023-09-01  SCORE: 76  REACTIES: 80
TITEL: Huberman: "Yes, there's some evidence for grounding. Is it super strong evidence? No, it's not. We don't really know what it is about placing one's feet onto the earth that is producing the positive effects that were observed in those studies."
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jyo7k64] (score 61, diepte 0) The evidence is thin, but it's free and I suspect the placebo effect of being outside, breathing fresh air and your feet touching cool grass is powerful.
[jyotfsz] (score 27, diepte 1) If there's no specific physically measurable effects, my bet is on that it's similar to the psychological benefit of looking at plants and trees.

We've lived in nature for a long time. In an evolutionary sense, it's our "home." So my guess is that we could simply just be wired up in such a way that it
makes us feel better.

Thinking of this, I wonder if the psychological benefits of having plants in a room are (partially) replicable with plastic plants? I really suspect a big part of the effect is just the shape and color.
[jypbhuv] (score 18, diepte 0) We are electric beings. Connecting to earth is shown to change our voltage. It must be doing something.
[jyoblmd] (score 16, diepte 0) I have to admit that while it sounds like woo, I feel better when I spend time barefoot in grass. I like to sit outside in the morning and leave my bare feet in the grass. I feel better when I do that than just sitting outside and not having my feet in the grass. I'm not sure why it works but I just feel a happy calmness from it.
[jyphwka] (score 14, diepte 2) I've heard that part of the mood-improving effect of being in nature could be from bacteria in the soil producing certain chemicals. I don't think it's too far-fetched considering what we know about how the gut microbiome influences the brain. I can't remember the particular species of bacteria thought to produce this effect.... anyone know what I'm talking about?
[jyor208] (score 12, diepte 0) What don't people realize that anything that borders on the "woo" or has any type of benefit that could also allude to there being a higher power - the benefit of prayer, innate "psychic" ability will never get the Peer Review that will satisfy the masses.

There's a book I'm reading that discusses just that: when their team of scientists found evidence for "psy" ability, they were immediately shut down, couldn't publish or were made to look crazy.

My point is, if something like grounding works for you, don't stop doing so because The Experts say it is placebo, pseudo science, blah blah. Because these types of topics will *never* be published positively in any journal accepted by The Experts.
[jyov6hk] (score 12, diepte 0) I'm not sure "evidence" is needed other than trying it. If it feels good carry on doing it. If it doesn't feel good no need to persist. There is no "cost" or "downside" involved. It's a bit like going up to someone sitting on a beach and telling them "There is no peer-reviewed evidence that sitting on a beach is good for you". Which may be true, but also completely irrelevant. People sit on beaches because it makes them feel good. The subjective feeling is all the evidence you need.
[jyoso8w] (score 11, diepte 1) Well of course not! Big pharma and biotech can’t invoice you for walking on the earth. 

If no profit can be made, those giants won’t consider it legitimate in the eyes of western medicine. Agency capture prevents actual studies and peer reviews that’d support these theories from ever seeing the light of day.
[jyqvunu] (score 10, diepte 0) I believe in grounding, just as I believe in the power of the water, especially the ocean can have on you.

These are the energies that surround us. 

When we die, our energy doesn't just disappear into thin air, instead it is changed and becomes part of the world's energy.

It is kind of hippie dippy, but I believe in these as a natural way to reconnect.
[jyp0831] (score 8, diepte 1) I'd say if there's a blind factor, it's that your feet skin has a lot of nerves, and the varied / subtle / spiky feeling of normal ground versus in a shoe is very benefitial to your body

that said, i like when i touch grounded metal parts.. i always get a chill and feel a tiny bit more relaxed
[jyplinu] (score 8, diepte 1) n=1 is significant enough if you are the 1
[jyozzm7] (score 7, diepte 2) what about grounding on earth in a bad urban setting ?
[jyplh8q] (score 7, diepte 3) Keeping an open mind is indeed a virtue; keeping a mind so open that your brain falls out is not.
[jypmxz7] (score 6, diepte 5) I love being condescended to by conspiracy theorists with no grounds for feeling superior.
[jypcrit] (score 5, diepte 3) Yeah we should run a study on grounding in berkeley downtown. Or grounding in San Bernardino in the ghetto. That’ll mess you up for weeks
[jyp071t] (score 5, diepte 1) Biophilia hypothesis/effect. Pretty well studied. There's wisdom in telling people to touch grass.

I'm not remotely convinced that the proposed mechanisms behind grounding is real/valuable, and I think anyone who picks up fads like that is probably less critical than they should be.
[jyrflom] (score 5, diepte 1) To me, that's the mechanism. We're really proprietary. It's common knowledge that we get reflexive pupillary dilation when we see infants. But these aren't the only scenes that do it \[source below\]. Pictures of forests elicit the same response. Even the color green - like just a flat green square - elicits a greater response than other colors.

To me it seems reasonable that if something finds itself in the niche it evolved into, it would feel more comfortable than if it perceived itself to be in a totally alien environment. If we know that when one sense perceives a context more similar to that in which it and its progenitors evolved, an indicator of a calming response is elicited, it's not a huge leap that the touch sense perceiving standing on the forest floor could feel nice.     

And things feeling nice, or rather, pushing the subjective state away from stress, is well understood to be physiologically positive.      

Source on the pupil info: Stanford BIO150 by Robert Sapolsky, available free on YouTube.
[jypnsoa] (score 5, diepte 1) >My point is, if something like grounding works for you, don't stop doing so because The Experts say it is placebo, pseudo science, blah blah.

thats a great point except that people who already believe crazy shit have already long been ignoring anything resembling general knowledge or "scientific consensus". 

like there are some people who believe that the sun cures diseases and some people believe drinking their own piss gives them magical powers.  i don't think you need to be concerned about these folks coming across a paper that says you shouldn't drink your piss, and then suddenly stop doing it.
[jypdj00] (score 4, diepte 4) hehe,

on a more serious note, there are dense urban areas (mostly concrete) where people have some tiny backyard, so you'd get natural grounding (to an extent) in a familiar setting
[jyq10bb] (score 4, diepte 3) This would be the test. If it's only about an electrical connection to the earth (like these snake oil devices being sold suggest) then laying down on a bare concrete basement floor would have the same electrical grounding. 

It's probably more to do with just feeling good from being out in nature and connecting to the greater web of life.
[jypf650] (score 4, diepte 1) You realize this is exactly the same kind of thinking that flat earthers use, right?
[jyphh2g] (score 4, diepte 1) Okay. Does that invalidate the research into mainstream treatment?
[jyormo4] (score 4, diepte 0) Grounding outside is free so why not do it,

Grounding inside is cheap an easy, I use a grounding mat at my office desk its $20 to buy and will probably last a lifetime. There seems to be a positive for better blood flow, so why not just do it whilst I work.
[jyqazwu] (score 4, diepte 0) Grounding allows electrons to flow into your body. Your body and brain runs on electricity. To suggest grounding wouldn’t have any impact is actually the insane position.
[jyp0o3b] (score 3, diepte 3) Doubt it'd feel great tbh
[jyqvg3f] (score 3, diepte 3) Yeah it's one of the best parts about gardening :)
[jysij07] (score 3, diepte 5) I mean, if you shit in your yard alot or something? 

I don't have dogs and I have modern plumbing 😉
[jyqewsp] (score 3, diepte 2) Is that you Neo?
[jyw0ycx] (score 3, diepte 2) Bioelectrical signals are a movement of ions, and electricity is the movement of electrons (kinda). Ions can be effected my adding or taking away electrons. 

The planet and everything on it is in a large electromagnetic field (that the "kinda" because electricity flow is more an effect of a field than moving electrons). Things inside this field can get charged more or less than other things, but the electrical field always wants to even out and have all things be equal all the time. We call this "returning to ground". That is why your sub-panel on your home literally has a ground rod driven into the ground under it and a copper wire connecting the two.

The reason we have modern civilization is from our ability to charge up different materials with a greater charge and other material and control that amount of difference and rate of flow. A computer chip is simply that control on a high granular level. 

The body also becomes charged one way or another. And our bioelectrical systems is affected by changes in electrical fields and charges. We know that radio frequency excites neurons. Not new age mojo, its simple experiments recreated a number of times and labs all across the world. 

When we "ground" ourselves, we are literally returning the body to a neutral charge and we know, though grade school earth science experiments, why and how that works.

How this topic is controversial in anyway melts my brain : /
[jyrma0v] (score 2, diepte 5) It definitely is not an insulator and conducts electricity pretty well. Maybe even better than a ground.
[jyrthct] (score 2, diepte 5) They exist
[jyrmm4s] (score 2, diepte 4) unsealed concrete is an option for grounding if you don't have access to a grassy area. you can also ground in a bath if your pipes are metal.
[lmcc4ti] (score 2, diepte 4) Honestly, for me it is weird. You see, I have chronic pancreatitis  and have some level of inflammation almost all the time. There are various supplements i ve found helping throughout the years that really help in lowering inflammation. 

I live near some river and when I sit there, barefoot, somewhere after 10 minutes my inflammation starts dissipating and my pain lessens by a lot. It doesnt happen when I wear shoes. The thing is it helps as much as taking an aspirin which helps me a lot when flareups arent that bad. 

I have no explanation. If I walk barefoot on concrete it doesnt work as much as on soil. It truly feels amazing.
[jyse4b6] (score 2, diepte 1) I'm curious, would you have called sun exposure a placebo effect if not for reseach into Vitamin D production?
[jyty51g] (score 2, diepte 5) curious
[jyohand] (score 2, diepte 0) body charge is important, we know that polyester around the testicles will actually make you sterile because of the charge it produces. Most of the time you're grounded so it's only slightly beneficial. [https://pubmed.ncbi.nlm.nih.gov/8279095/](https://pubmed.ncbi.nlm.nih.gov/8279095/)
[jypjqsi] (score 2, diepte 2) it was also confirmed in humans. 

https://www.eviemagazine.com/post/polyester-underwear-contraceptive-men-study
[jypv9sh] (score 2, diepte 3) >Did you get your booster too, like a good boy?

Great, you’re one of these.  Fucks sakes.
[jyt4one] (score 2, diepte 1) Could you share the name of the book you’re reading on this please?
[jyowilu] (score 2, diepte 0) If you understand/ work with electricity and know a bit about bioelectrical body systems I think it's pretty obvious why.
[jypwc1a] (score 2, diepte 1) No, it's really not. You don't have w to go outside to be electrically connected with the Earth.
[jyrfrry] (score 2, diepte 2) They’re everywhere. Static energy is a build up of “free electrons”
[jyqncen] (score 2, diepte 0) I haven't read any studies or watched the video but I can tell you without a doubt in my mind that buying a grounding blanket has been one of the best purchases of my life.

I used to experience so much pain in my knees, mostly from years playing hockey and now being moderately overweight. After one night, I had less pain in my knees. After one week, the pain was gone. I haven't had knee pain in months.

Sidenote that I DID also use red light therapy for anywhere from 5 minutes to 30 minutes per day on my knees but haven't done that in about 2 months.

I think both worked and I'm very thankful.

I think the company I bought from was Earthing Harmony or something but I'm sure there's plenty of companies. My wife and I just sleep on it on our mattress. 

The tingling sensation is kinda weird but I read that not everybody feels it. I find it really interesting that the most "tingly" parts, at least for me, were areas that I used to get pain (i.e. knees and feet).
[jysp133] (score 2, diepte 1) There is something magical about sea water. Don’t know what it is but you just feel GOOD. Same with bare feet on ground. And outside time in general.
[jyq2pkv] (score 1, diepte 4) Isn’t concrete a good insulator
[jysrdtl] (score 1, diepte 6) Hm ok
[jyqhqvv] (score 1, diepte 4) Business idea: conductive shoes
[jyrtg00] (score 1, diepte 4) You could dig up the top layer of grass, and lay an electrical insulator below it.

Then have blinded, randomised groups stand on either the insulated grass barefoot, or the regular grass nearby.

That should get you some pretty good data 🤷‍♂️
[jyp7mk9] (score 1, diepte 2) Isn't marble a fairly strong insulator when compared to other types of flooring such as..... Moist earth?
[jysxsij] (score 1, diepte 2) That's a good question. The research in sunlight and vitamin d is pretty extensive as far as I know and the correlation is well documented. What I'm saying somewhat mirrors what he's saying. I think the evidence is thin, it needs to be studied more, but we should do it anyway because it's free, easy and anyone can do it.
[jytd6gh] (score 1, diepte 3) You didn't answer my question?
[jytdtnx] (score 1, diepte 4) I'm sorry, I thought I did. Without the studies, I would have chalked it up to placebo.
[jypb738] (score 1, diepte 1) Could be the sunlight exposure
[jyp02m0] (score 1, diepte 1) He's not talking about electrical grounding.
[jypeay7] (score 1, diepte 1) This is a hilarious study of dogs in underpants. I don't see any reason to believe that it has anything to do with humans, electric charge, or grounding.
[jz9ifz8] (score 1, diepte 3) It was *not* confirmed that polyester will make you sterile because of the charge it produces. They had these guys wear a tight polyester sling for *nearly five months* before they stopped producing sperm. We already know that heat is a factor in sperm production, and they didn't control for that at all.
[jyxv588] (score 1, diepte 2) Real Magic
[jyrva1y] (score 1, diepte 1) Care to articulate the obvious part?
[jywdidc] (score 1, diepte 3) How does your feet being on earth ground you any differently than touching a doorknob inside your house? And what “bioelectrical signals” are you talking about, the cardiac cycle? Synapses are determined by the potential due to specific Na and K ions, but the neurons have pumps specifically working to create charge. That’s all to say you never really even clarified why it’s obvious that being grounded actually will effect you and how.
[jywkkqo] (score 1, diepte 4) I did explain why its obvious to me. It won't be obvious you because you are lacking information that makes it obvious

Key concepts again:

Electricity is a field. EM fields effect action potentials by opening voltage gated calcium channels. 

Open VGCC's are neuroexcitatory.

Grounding anything, electronics, radio towers etc only works with continuous contact, to the actual ground by way of physical contact or a a conduit bridging the gap. 

-Not sporadic contact like a static discharge, 

-or partial grounding with some insulators in way. 

Time has a real effect. Synapses have memory and so do calcium channels. There's zero effect in the brain from a momentary static discharge conversely the longer the brain is without and excitatory stimulus, the greater the calming effect.
[jywoj1d] (score 1, diepte 5) You mentioned disparate ideas but nothing that shows why “grounding” a human is beneficial - why would it be any more beneficial vs keeping a human at a potential of -50mV? Science is about finding answers to seemingly non-intuitive conclusions.
[jyyh8vy] (score 1, diepte 6) I clearly stated why grounding humans beneficial. EM fields altars action potentials in the brain and body with deleterious effects. 

So before I answer any more questions I want you to answer one for me. Why when I clearly stated the benefit did you say to me that I didn't state the benefit when I did?
[jyyle4j] (score 1, diepte 7) An EM field would be in effect despite grounding. Plus, the assertion that it is deleterious is not backed by any evidence. I didn’t have to look up any thing because I’ve learned this in my secondary education - which also brings to light that none of this is obvious for a layman from primary education. Your confusion on the terms is further evidence of that.
[jyylk81] (score 1, diepte 8) 3 questions. You haven't answered any of my questions yet.
[jyyn5dl] (score 1, diepte 9) I answered your two questions that you listed? Let me simplify it for you - why when the researchers who authored this cannot explain a mechanism of action, but yet you still insist that it’s obvious? Even the researchers are not asserting WHY it works, yet you somehow know better and it’s obvious?
[jyyrpm3] (score 1, diepte 10) Yes you partially answered and confirmed what I thought. 

That you are not looking for understanding you are looking for an argument. 

This way if being closes off inquiry and sharing.

If you think I misunderstand something, or using wrong terms, you are not trying to help me. There is no partnership, no openness, no self reflection.

For example you are ignoring step two of the scientific method. You are certain about what you think you know, making assumptions and misinterpretation about what I'm saying because you are projecting your assumptions about what I think over what I'm actually saying.
[jz02rst] (score 1, diepte 11) Dialogue is fine, I’m not here to be your partner or walk you through basic concepts. Only thing obvious here is that you lack foundational knowledge on the topic as well as the basic principles of the scientific method - oftentimes “obvious” answers are the wrong ones, and they still require explanations beyond circular reasoning like you’re using.
[jz92ri4] (score 1, diepte 13) That’s not at all what I said, but it’s clear that reading comprehension is not your strong point. Those who know the least think they know the most, and that definitely applies to you in this case.
(24 reacties met lagere score weggelaten)

=== THREAD 1ds76aj ===
SUBREDDIT: r/diabetes
DATUM: 2024-06-30  SCORE: 6  REACTIES: 60
TITEL: Walking/tennis shoes | what are my fellow diabetics wearing? | Seeking recommendations
POST (source_id=post):
So yeah, nothing to ask about spiking sugar levels in this post 😛

Ok, I lied🙃.
There’s a direction relationship to how walking helps lower spiking levels, fast.

Seeking recommendations for walking/tennis shoes to wear for my walks around the block or on an all day outing that is mostly walking.. I have flat feet and also wear prescription orthotics. Bonus points if you also use them, kindly mention that in your feedback. Not all shoes accommodate them well so it would be good to know.

I’m open to spend upto $200 USD.

Many thanks 🙏🏻

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lb0o7ob] (score 12, diepte 0) Hoka Clifton 9. Your feet will thank me later. 💕
[lb0w24i] (score 9, diepte 0) I wear Brooks Ghost running sneakers. My wife use to manage a running store and she recommended them. You can find them pretty much everywhere for like $99-$150. I set up a recurring charge at Amazon and get the same pair every 6 months
[lb0oj52] (score 7, diepte 1) I love my Hokas!
[lb0e8js] (score 5, diepte 0) I don't wear orthotics YET.... BUT, I am getting ready to go have custom lift made for my left shoe as I have a leg length discrepancy. I also have Spastic Quadriplegic Cerebral Palsy and the shoes I wear are highly recognized in that community by people who were AFOs and orthotics etc. I wear Billy shoes. [Billy Footwear ](http://billyfootwear.com). They zip up. They do have shoe laces to tighten how they feel on the foot, but the zip to put on and take off. 10/10 recommend.
[lb0iw3f] (score 5, diepte 1 OP) Thank you for your reply. It is appreciated. 

So there’s a “it depends” when wearing slip ons. With flat feet, and using orthotics, the heel has to stay put, and typically slip ons does not provide that support. Ideal shoe is one with laces that you can cinch and tighten.
[lb0ozdn] (score 5, diepte 2) They’re the best! I bought them as a T2 diagnosis present for myself actually lol.
[lb0scpn] (score 5, diepte 0) Honestly I wear Birkenstocks almost every day. I have their sneakers and several pairs of sandals. I regularly walk to work and back (2.5mi ish each way). On the athletic side, I wear On Clouds, with a 1/2 insole orthotic from Birkenstock under the removable sole. I have collapsing arches and am prone to plantar fasciitis and they’ve been a real game changer.
[lb12vg7] (score 5, diepte 0) I wear whatever shoes I want- but I spend a pretty penny on gel insoles meant for working on your feet all day.  I have feet so flat you could use them as levels. I also did 3 miles in 6in platform gogo boots last weekend with only some calf cramps from mild dehydration lol.

 My tip is to buy your shoes half a size up so you can buy thicker/more helpful insoles to stick right in any pair you own and the wear in period is basically null because your insoles take up that half a size with their bulky gel-y goodness.
[lb1m7sq] (score 5, diepte 0) Brooks!  So cushiony they almost threw me off balance at first.
[lb1rhdw] (score 5, diepte 0) I really love my Hoka Clifton 9 sneakers.
[lb0eoej] (score 4, diepte 0) Hello! Fellow diabetic with flat feet, but no orthotics. I live in a city and walk everywhere, or as my friends like to say, take unnecessarily long walks. 

First tip: give a few different pairs. Cycling through a few different shoes will ensure that they all last longer and you don't put too much wear on one pair too quickly. 

Some of the shoes I cycle through include:

* Adidas Cloudform Pures - They're lightweight and super comfortable, and you can typically find them at great prices at Costco (usually in the fall) and Marshalls/TJMaxx/DSW. 
* Toms - I love Toms for walking, work, pretty much everything. They have some support inside but nothing too intense. They're easy to slide on and off and come in a lot of different styles/builds. You can wear them without socks, but they can get smelly pretty quickly. I will also say that if you walk on the sides on your feet, these will wear super quickly on the sides. I also am not sure how accommodating they would be for orthotics, but they have a variety of styles that might work!
* Allbirds - These are so comfortable and sustainable! I wear the Wool Loungers, but the Tree Loungers probably make more sense for summer walking. My friend (also with flat feet and orthotics) wears the Tree Runners and Tree Dashers and has pretty much replaced all the shoes in his wardrobe with some version of Allbirds. They are easy to clean, have replaceable insoles, and you can occasionally find them at Nordstrom Rack for a good price!
[lb0fyrm] (score 4, diepte 0) Spend a third of that on Skechers Hands-free Slip-ins.
[lb0m174] (score 4, diepte 0) I recently bought a pair of Brooks Women’s Ghost Max Cushion Neutral Running & Walking Shoe, and they're probably the most comfortable pair of walking shoes I've owned. Experiencing very little fatigue and my toes aren't squished, really love that they offer wides and Xtra wides cuz I have a hard time finding those. Kinda pricy though.
[lb1cn07] (score 4, diepte 3) Absolutely the best!
[lb2x9xn] (score 4, diepte 1) I have definitely been converted. Picked up a pair of Hokas for my job and I wear them at least 42 hours a week with no issues
[lb1bq7o] (score 4, diepte 0) My podiatrist recommended Hoka. I had a pair for running and they were great. 

I wear Adidas because I already had a couple pair and they fit my custom orthotics.  Don't have flat feet but do have an arthritic toe.
[lb26sfd] (score 4, diepte 0) Skechers.  Always Skechers.  I have a pair of Nike, but they aren’t nearly as comfortable.
[lb0i67m] (score 3, diepte 0) I go into REI and buy a nice pair of hiking shoes. Insert my own gel insoles.

I walk between 5-10 a day most days.
[lb0k98e] (score 3, diepte 0) I really like new balance sneakers.  Supposedly they can accept orthotics, but I don’t use them so can’t offer personal experience there.

I am very particular about how the back of my shoe hits my heel and also have a high instep and new balance shoes seem to fit my feet well.
[lb3885b] (score 3, diepte 1) Hokas are the best! Try all the different types on. They're all a little different
[lb1potn] (score 3, diepte 1) I’ve been thinking about Birkenstocks but I tried some on in store and they hurt to even stand on! It felt like my arches (I have flat feet) were being forced to curve in a weird way. But it’s contradictory to me because I’ve heard Birks are so good for flat feet and super comfy. Did you have to break your Birks in?
[lb1ajxy] (score 3, diepte 0) Stompy Timberland boots with insoles. I've walked 500 miles and after replacing the soles i will walk 500 more, just to be the man that walked a thousand miles to lower my blood sugar.
[lb1ecdz] (score 3, diepte 0) My feet are sore a LOT due to working in steel toes on concrete. I have mild neuropathy, plantar fasciitis, and an arthritic bone spur on my right 2nd/3rd toe base.  When not at work I love my moab 3 hiking athletic shoes.  They have the stability I need and they have a very firm sole, unlike many of the athletic shoes out there with their marshmallow soft soles.  I love them.  They are not cheap but well worth every penny to me.
[lb1vdup] (score 3, diepte 0) Brooks, new balance, and Hoka.  I am a retired surgical nurse, and my feet were in clogs throughout my career.  I am all about stability, comfort, and cushion for my feet. They have taken a beating from all that standing.  I walk 5 miles a day, 5 days a week, on a trail or track. I rotate my shoes from day to day.
[lb22dba] (score 3, diepte 0) Lots of great suggestions but I would recommend going to a running store. Fleet Feet is one near me and they have a lot of stores. They’ll scan your feet, check your stride etc. I never knew I had a narrow foot until I went there and was wearing a totally wrong size.  I’ve gotten a few great pairs from them and they’ve all been Disney tested so they’re great for long hours on your feet
[lb28x85] (score 3, diepte 0) I’m on my third pair of sketchers slip ons. Great support for my neuropathy inflicted feet
[lb1cs73] (score 2, diepte 1) Trail runners? Or actual hiking shoes? I didn’t see any hiking stuff that wasn’t heavy-duty and ended up with trail runners that have been great for walking and non-hardcore trail walking/hiking.
[lb241ip] (score 2, diepte 2) Most often hiking shoes. My knees are too bad for any kind of running.
[lb25mg3] (score 2, diepte 3) Trust me - I'm not running! It was the type of shoe that was recommended to me at REI for lighter hiking. I'm not in the market for new shoes yet - but was curious if you were talking about lightweight shoes or heavy duty hiking shoes. I have either [these exact shoes](https://www.altrarunning.com/en-us/trail/womens-lone-peak-8/AL0A85ND.html?dwvar_AL0A85ND_color=419) or a close model.
[lb794nr] (score 2, diepte 3) A T2 diagnosis present!!
What a brilliant idea!!
I’m going to start thinking what I could get for myself!
[lbbaaqp] (score 2, diepte 5) I absolutely agree!

Don’t know why I haven’t thought about it before!
[lb0ye43] (score 2, diepte 1 OP) Thank you for your comments. I will research all of Birkenstock’s offerings to see which solution could work for me.
[lb1wzil] (score 2, diepte 2) I swear by birks as a flat footed individual. Yes, there is a breaking in period, which for me has always been quite uncomfortable. But once they fit, they fit like a glove!
[lb0waiz] (score 2, diepte 0) I currently wear Topo Athletics Phantoms and Terraventures as my walking/daily shoes. 

I also used to wear orthotics but saw a chiropractor and did foot exercises for a few years to help with flat feet and wide feet and that helped my feet go back to normal and allowed me to switch back to normal shoes.
[lb0xsff] (score 2, diepte 1 OP) Thank you for your input. It is appreciated. 

I will research the shoes you listed. More importantly, will call my podiatrist to see what exercises I need to perform. Don’t even know there’s a possibility to go back to normal footwear without the use of orthotics.
[lb1455c] (score 2, diepte 0) New Balance. They come in extra wide if you need it.  The higher the number the more support you get.  I have worn the 921’s for years.   They have a roll bar in them. My podiatrist recommended them to me when I was working as a waitress. I’ve had bunion surgery and some other issues with both my feet. Best shoe for me. Hope you find something that works well for you.
[lb1meq6] (score 2, diepte 0) New Balance 990’s are the best!! But very done several trips with them where I’m walking over 15k steps a day and they never fail me! For sport sandals, I wear my Teva’s which I’ve had almost 10 years. They’re still awesome and provide great support.
[lb1slj8] (score 2, diepte 0) I’m on my second pair of Nike Motivas. They’re wider in the toe box area of the foot. I use mine for everyday, trips like Disneyland and also cardio at the gym. They’re really comfy, made for walking too
[lb1vooj] (score 2, diepte 1) Apologies,  I forgot the orthotics.   Yes, I wear them due to ankle and knee surgeries.  I pull out the shoe inserts and use my own orthotics.
[lb1zkm1] (score 2, diepte 0) I used to always buy New Balance,  but, in 2022, I bought a pair of Skechers.   They are the most comfortable shoes i have ever worn.  Added bonus, they are under $50.

[https://www.amazon.com/gp/product/B07FKVC82C/](https://www.amazon.com/gp/product/B07FKVC82C/)
[lb4qfwa] (score 2, diepte 1) I ageee to go a running store! RoadRunner Sports will do the same! I have wide feet and they helped me find the perfect show and insert.
[lb22xi7] (score 2, diepte 0) I’ve got odd wide feet and I personally wear Nike Pegasus 40s. They are the only wide shoe I’ve found that actually fit my feet properly. The other suggestions are probably better but if you needed something else to add to the list of shoes to try out, maybe. 

Seems with shoes when you find the one that fits you just right, it’s worth sticking with them. So far after a little over a year, there is a pretty small amount of wear on the tread despite my constant walking, and absolutely none of the top half has come apart at all. No loose threads. Nike definitely puts a lot more care into their higher end running shoes, my previous $70 set fell apart in about 6 months. This set was about $150, not a single thing but tread wear.
[lb267s3] (score 2, diepte 0) I wear Lems, Birchbury and Luna Sandals exclusively. I’m a big believer in a wide toe box and zero drop being much healthier than all the support modern shoes provide. A good book on this subject is “Born to Run.” I’ve had Diabetes for 14 years and have zero problem with my feet.
[lb272wc] (score 2, diepte 0) I like the Brooks Adrenaline GTS myself.
[lb28hhu] (score 2, diepte 0) Not wearing orthos, but the Merrell MOABs that are shoe fit rather than boot fit are great all purpose walking shoes.
[lb2c3st] (score 2, diepte 0) My toes don't touch each other, so a 4E/H shoe is imperative.   So far, Underarmor makes one that suits.
[lb2ivzx] (score 2, diepte 0) I have 5 pair of Brookes GTs and i love them!!  I’m a nurse and on my feet a lot.   I have a variety of colors… that’s why 5.  Not because they wear out
[lb2maog] (score 2, diepte 0) Go try some Avia or Athletic Works slip on shoes.  These were the closest to comfort as my diabetic insoles.  I no longer pay the $200 every year for 3 insoles and ugly shoes.
[lb2p14q] (score 2, diepte 0) Hoka
[lb2s3xq] (score 2, diepte 0) I have very flat feet and overpronate. Hoka Arahi are my fave shoes. I’m on my 4th pair.
[lb2wqro] (score 2, diepte 0) [orthofeet.com](http://orthofeet.com)
[lb2zj02] (score 2, diepte 0) Skechers Slip-Ins Go Walk.
[lb44wmj] (score 2, diepte 0) New Balance 990 series! Great support and easy on the feet and come in various wide configurations
[lb4w15v] (score 2, diepte 0) There is a brand of walking/running shoes called On and I swear by them they are a little pricy between 100 and 200 dollars but they are like walking on clouds. I usually get last years models if they have them in my size to save some money.
[lb6det0] (score 2, diepte 0) Adidas Ultra Boosts. Basically all I wear at this point. I have a few different ones I rotate and I wear them until they’re burned out, or fiancée yells at me that they’re too stinky.
[lb6x94l] (score 2, diepte 0) I love my Asics.
[lb7dhw3] (score 1, diepte 4) It’s a shitty thing to be diagnosed with a life time illness, why not celebrate your lifestyle changes you’re about to make? 💕
[lb6pygt] (score 1, diepte 1) Hi, I’m Vetted AI Bot! I researched the **'Skechers Men's GO Walk Evolution Ultra Impeccable Sneaker'** and I thought you might find the following
 analysis helpful.

 **Users liked:**
* Extremely comfortable for wide feet (backed by 3 comments)
* Great for all-day walking and travel (backed by 3 comments)
* Easy to slip on and off (backed by 3 comments)

 **Users disliked:**
* Material snags easily, affecting appearance (backed by 1 comment)
* Inconsistent sizing, runs large (backed by 3 comments)
* Lacks durability, wears down quickly (backed by 3 comments)

 

 Do you want to continue this conversation? 

 [Learn more about 'Skechers Men's GO Walk Evolution Ultra Impeccable Sneaker'](https://vetted.ai/chat?utm\_source=reddit&utm\_medium=comment&utm\_campaign=bot&q='Skechers Men's GO Walk Evolution Ultra Impeccable Sneaker' reviews) 

 [Find 'Skechers Men's GO Walk Evolution Ultra Impeccable Sneaker' alternatives](https://vetted.ai/chat?utm\_source=reddit&utm\_medium=comment&utm\_campaign=bot&q=Find best 'Skechers Men's GO Walk Evolution Ultra Impeccable Sneaker' alternatives) 

 This message was generated by a (very smart) bot. If you found it helpful, let us know with an upvote and a “good bot!” reply and please feel free to provide feedback on how it can be improved.
 

 *Powered by* [*vetted.ai*](https://vetted.ai/chat?utm\_source=reddit&utm\_medium=comment&utm\_campaign=bot)
[lb35d0o] (score 1, diepte 0) I'm in the UK so my recommendation may not be hugely helpful to you but I wear sketchers. I started wearing sketchers when my mum recommended them because she's a nurse in the NHS and many of her colleagues wear them. They're the most comfortable trainers I've ever had. Once my kidneys were screwed, I switched to the sketchers wash a wools. The uppers in these are made of wool and they're amazing because if my feet swell, they just kind of expand to deal with it. The biggest plus is that even if my feet swell a lot, they don't rub at all. The skin on my feet is incredibly delicate and the wash a wools have meant that I can relax knowing that they're not going to damage my feet.

Bonus points for the fact that they come with a wash bag and when they get mucky, I just bung them in that and chuck them in the washing machine.
[lb3f4ed] (score 1, diepte 0) I have flat feet and used orthotics for the longest time. Then I discovered Barefoot shoes and it has been nothing short of life changing. I could barely walk for 5 mins before the pain crept in. A month into barefoot shoes and I could easily walk 30 mins without any pain. It's been two years into barefoot shoes now and my arches are actually stronger, and I can go up to 25k steps without any foot pain.
[lb468yg] (score 1, diepte 0) I've been wearing Ryka almost exclusively for maybe 20 years. They're always true to size and fit like a glove right out of the box. All that cheering aside:
1. I've never used orthotics so can't speak to how they'd work there.
2. My work/lifestyle since I've been wearing them has not involved very prolonged standing. (My first career was another story but I wore work boots there.)
3. They didn't make dress shoes.
(2 reacties met lagere score weggelaten)

=== THREAD p2l2yr ===
SUBREDDIT: r/Fibromyalgia
DATUM: 2021-08-11  SCORE: 91  REACTIES: 60
TITEL: Pain in feet?
POST (source_id=post):
Does anyone else have almost constantly painful feet?
The pain is really difficult to describe, but I'll try.

My heels feel like I've been standing with all of my weight on them, or like I've been standing on cold concrete for hours. 

The sides of my feet feel like they are constantly bruised. 

The muscle between the balls of my feet and my toes gets really sore and I often have to stand on tip toe to stretch it.

I've tried pain reliving gels and Deep Heat but nothing really helps. 

Any advice? (I'm in the UK)

Edit: I've just ordered metatarsal foot pads so I'll post on the sub if they're any good 
Thanks for all the advice

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[h8kwubg] (score 15, diepte 1) I tried both Lyrica and Cymbalta. I gained 50 pds in 1 month on Lyrica and tried to kill myself. With Cymbalta, I had horrific nightmares. Like I was under water watching children drown in one and in another I watched a man murder a baby and paint the room with its blood. I noped right out of those drugs. Believe it or not Crocs shoes have been a blessing in disguise. They make sandals and flats. Only thing I can wear and walk in all day and my feet don't hurt. amitriptyline has also helped alot.
[h8ktrsg] (score 12, diepte 0) Yep. My fibro pain started in my feet then moved on to my hands. Are you on anything specifically for the fibro. I had a combo of cymbalta and lyrica that worked really well for me though not everyone has good luck with cymbalta. I also by accident bought some yoga socks which have a slight compression band in the middle and they are WONDERFUL. This were on clearance in the cheap section at target but you might google yoga socks and give them a try. I also had to wear some kind of crazy compression leggings when I had a kidney stone removed and those felt great too so you might try regular compression socks. I also have gotten incredibly picky about my shoes since my pain developed. I was an avid flip flop wearer and now I rarely wear them as having to use my toes to anchor the shoes is too much. I look for supportive type tennis shoes and I prefer them snugger around the top of my foot as that seems to give me better support and less pain. Good luck
[h8l7052] (score 7, diepte 0) Yes. But for me, it turned out to be caused by undiagnosed RA. I lived for many years with an incomplete diagnosis, simply because my blood work and X rays are normal. The autoimmune arthritis types are commonly seronegative with normal blood work (1 in 3 have normal blood work at time of diagnosis). The only way to fully rule out autoimmune arthritis as a possibility is to get ultrasound or MRI on affected joints when you have symptoms. Images should be reviewed by rheumatologist. If this testing hasn't been done for you, please mention this to your doctors as a concern, and get more thorough testing.
[h8l03qu] (score 6, diepte 0) Yes oh lord yes. I’m a huge fan of hot baths or foot baths with Epsom salts. I also make my own magnesium brine spray that I use at night when they start feeling painful, swollen and somehow itchy under the skin.
[h8l4ofs] (score 5, diepte 3) Venlafaxine is a cousin to duloxetine (cymbalta). It has really helped me. I asked about it having read it was used to treat ADHD (which I am trying to get diagnosed with so I'm ineligible for any meds)  and my GP prescribed it to me. Its the only thing I've tried where I can tell if I have/haven't taken it as I feel so much more sore and crappy. Due to the ADHD, I have never even brushed my teeth every day but I'm going on about 8 weeks of not missing a single dose (a few were late but none missed!).

I've tried:

* amitriptaline
* sertraline
* fluoxeitine
* escitalopram
* pregabalin
* gabapentin (took it at the same time my dog was, he had better luck with it than me the lucky bastard.)
* duolexitine
* venlafaxine

and the only one that did much of anything was the venlafaxine. Keep trying meds if your guts can cope with it. the only side effects I've had from venlafaxine is jaw clenching, reduced appatite (at first but I see this as a plus as I was previously always hungry) and I get tired about 8-9 hours after my dose (I take it at 2pm with my lunch).

Edit: and don't be afraid to keep trying meds. I had to take many months off to recover emotionally after trying a few and getting nothing. I nearly didn't keep trying which I am very glad I did both because I did find something but also because I overcame that worry!
[h8li9vk] (score 5, diepte 3) I was working as a cashier when I first got sick, so was on my feet all day. One thing that helped a little was using one of those bubbly foot baths with epsom salt. I'd also put lavender and mint essential oils, just because it smells nice and felt a little spa-like. My model has bubbles, heating, and vibration.

As a side note, keep an eye on your paracetamol intake. I took acetaminophen for about 10 years. It worked really well, but then I started getting rebound headaches. Many pain meds can cause rebound headaches. I think I was a little too complacent because it was over the counter. I took it on a schedule rather than as needed. My body didn't ever get much of a break from it. Now if I take anything containing acetaminophen, I get ringing in the ears and feel really sick.
[h8l0aqo] (score 5, diepte 0) Yes, I get this pain as well.
Since starting gabapentin last December, the pain is mostly localized to my left heel and into my arch a bit. Before, both of my feet hurt from my toes to my heels. 

I do also wear comfy shoes or the pain is just worse. 

Foot soaks and pain relieving creams never seem to help me either. So, Im not really sure I've got any great advice, especially if you don't take well to medications.
[h8l0nig] (score 5, diepte 0) Yep, I have that too. I got sent to a podiatrist because I apparently have incredibly flat feet, but arch support has done nothing for the majority of the pain. No solutions, just solidarity.
[h8l7awb] (score 4, diepte 1) I hope you were thoroughly screened for RA...my hand and foot pain turned out to be caused by RA that did not show up in blood work or X rays. The hand and foot pain has me concerned for you, it is the most common symptom for RA. Please read my other reply in this thread to make sure you have been fully screened for autoimmune/inflammatory arthritis types. They get missed often, especially when docs blame those symptoms on the fibro.
[h8lhwrc] (score 4, diepte 0) Man, when I stand up after not being on my feet for a while it’s baaaad. Like mornings especially. It feels like the skin on the top of my foot is being pulled and stretched. It only started recently. And I feel like my feet are just straight up bruised on the bottom. They’re so ridiculously sore, like I was dancing for hours and just took off my heels or something.
[h8l5jpc] (score 3, diepte 0) This is my primary issue. Pain and stiffness in my heels, ankles, and feet.
[h8m1qtn] (score 3, diepte 1) are xrays enough? my rheum xrayed basically my whole body and found nothing except a $300 bill.
[h8lacow] (score 3, diepte 0) Always, I always have sore feet. The bones on the top of my feet hurt and the pads on the bottom ache...my husband massages them for a bit at night (I'm very thankful) but I would like to go somewhere for a full hour or more of strictly a foot massage. At least that hour would be f**king awesome!
[h8le683] (score 3, diepte 0) Oh, I feel you on this.  I have constant pain like a giant hand gripped my foot and squeezed really hard and every bone aches.   Plus it feels like I worked a 12 hour shift on my feet and like the bottoms have been hit repeatedly with a 2x4.  I have to keep a fan on them at all times, sometimes ice packs when they get extra bad.

I can't wear socks or regular shoes, only crocs with bare feet.  The pain is terrible.  I went to a podiatrist to rule out that the bones are indeed not crushed (kidding on that, but did get them checked out).  He did a thorough exam and did x-rays and could find nothing.  My rheumatologist had no answer either, other than fibro and plantar fasciitis.

I got one of those boots for plantars and did the foot stretching exercises they say cures it.  My rheum dr also gave me injections in my feet which were so painful it took my breath away.  He also put me on prednisone.  None of it helped.

If I'm on my feet for more than a few minutes, it's really painful and they start getting red and swollen and it's only getting worse.

If you find something that helps with your foot pain, please let me know.  I'll try anything at this point.
[h8lgk4t] (score 3, diepte 0) Yes! My feet pain is always worse when I wake up in the morning and when I’m laying down before bed. You are not alone❤️
[hcwbdch] (score 3, diepte 0) Newly diagnosed here (but suspected it for awhile) - yes, foot pain is a big thing for me. It always feels like I’ve walked 20 miles in terrible shoes. Especially if I haven’t been on them for awhile.
[h8ky0sd] (score 2, diepte 2 OP) I am on cymbalta but my Dr stopped Lyrica yrs ago bc it apparently is less efficacious long term. 
The only pain relief I use rn is paracetamol. I have IBS-D too, so codeine etc is too harsh. 
I have some support type socks so I will definitely try them, and I do wear better supporting shoes. 
It's just so difficult to get describe and seems weird to have 3 different types of pain at the same time. 
Thanks for the advice though.
[h8l6ek5] (score 2, diepte 4) I second the benefits of venlafaxine (Effexor ER). I am on that with Gabapentin and have had considerably less pain. Fibro sufferers are prone to plantar fasciitis. There are socks, shoe inserts, etc that tend to help some people. I had great relief from having the trigger points in my feet worked on by my osteomanipulation doctor. She got both feet and hips relaxed and I could walk and sit again without tears.
[h8odrn7] (score 2, diepte 5) I'm have been on amitryplatine but didn't take it properly only when I had a particularly bad day with pain. I have severe dry eye and made it ten times worse so I stopped. I wasn't waking up in pain but I was waking up for water and eyedrops. Defeated the purpose.


Was prescribed the alternative to Cymbalta (not at home so can't see the name). Jesus, all my pain was gone but my mind didn't like it and it's really bad for your liver taking it long term! I've small children to mind so it's not for me. 

My thinking was this isn't going away and I can't take meds the rest of my life. I'm 34.
[h8oe6vf] (score 2, diepte 4) You said what I was saying. X
[h8ob2nl] (score 2, diepte 2) I’m trying to get off the lyrica because of the weight gain. It’s been a godsend the last 18 months or so, but the pain effects are slowly wearing off and I’m up 65 lbs. 

Cymbalta is absolutely terrible, I had a really bad reaction as well.
[h8ohmrl] (score 2, diepte 3) I was depressed already cause I was fat, gaining 50 pds really sent me over the edge. So I was even more fat and still  in pain. Only now the dr was saying oh lose weight and you will feel better. Whatever.
[h8oad2s] (score 2, diepte 2) I am impressed you have managed to keep the same six pairs that long. Something in my house eats socks and then I turn around and have 10 single socks with no mates. It also goes through periods where it likes to eat my son’s underwear
[h8olgcr] (score 2, diepte 3) So here's the weirdest part: there is an underwear goblin, and a hanes sock goblin in my house, but I have never so much as even had to look for the other Bombas sock match mate in the laundry. I dont understand these goblins. But I kinda feel like if socks and underwear are satisfying their sacrifice needs I'm okay with it because I'm terrified to know what they would start taking if I guard the socks and underwear better 😅  

TL dr: Sock/underwear goblins are a legit threat, but Bombas socks are goblin proof in addition to being made by a B Corp who donates a pair for every pair sold. Also, Bombas people, I'd love a job that I can do from home. Hmu
[h8l2oyk] (score 2, diepte 0) UK too, honestly I've found nothing. A foot bath (like an electric 1970s style one)  can be helpful as can compression socks. I tend to buy ultralight trail running shoes as they are grippy for when I get dizzy, supportive and so beautifully light. Honestly other than insoles which you probably already have tried - I either have to stay off of my feet or stay moving as I have more problems standing still than walking. You can get massage pads for foot circulation I think? Not tried these but I have a shiatzu back massage pillow that I will occasionally use for my feet.
[h8l3k37] (score 2, diepte 0) I always wear slippers… all year round. I found since I started doing that, it’s helped a bunch!
[h8l915c] (score 2, diepte 1) Yep. I just recently at 35 years old, FINALLY had my blood work show up but I have been diagnosed since 23.
[h8n3tfp] (score 2, diepte 2) No. X rays do not show signs of inflammatory arthritis. All they do is check for permanent joint damage (such as osteoarthritis, or joint erosion from another arthritis type). Normal X rays is a good thing, but it does not rule out arthritis as a possibility, not at all.
[h8ndd8q] (score 2, diepte 2) Ger a better doctor, one that was born after 1990 younger doctors know xrays are pointless unless diagnosis of broken bones😤
[h8l82o3] (score 2, diepte 0) Yes it isn’t like the most common thing experience with fibro but many do like you and me, it gets agonizing at times.
[h8ldwgc] (score 2, diepte 0) I stand about 6~ hours at work, not a lot I know, but enough to where it feels like I'm walking on bare bones.
[h8ofaxb] (score 2, diepte 1) Like you've been dancing in heels for hours is such a good way of describing it.
[h8lil4i] (score 2, diepte 0) Dollar tree has magnesium foot gel, it is amazing!! It’s like $20 on Amazon so I was super thrilled to find it for $1.
[h8m3tkr] (score 2, diepte 0) Yes. The higher my inflammation the worse my feet hurt. Shoes with thick foam bottoms are my savior. Which I can't believe I'm even saying because I've always hated shoes. I love going barefoot. But not anymore, if I'm upright I've got one of these on: 

https://www.newbalance.com/fresh-foam/

https://www.keenfootwear.com/p/W-ELLE-BACKSTRAP.html?dwvar_W-ELLE-BACKSTRAP_color=1024712&cgid=womens_footwear_sandals

https://www.oofos.com/ (they're ugly but these have the most cushion I've found so far) 

I also get my hips and ankles adjusted regularly by a DO or good highly recommended chiropractor. The body was made to move and people in pain don't do much moving, we should all stretch out daily but sometimes that hurts too.
[h8m5jss] (score 2, diepte 0) I feel like my feet are stuck in cement.
[h8zvfxb] (score 2, diepte 0) In my 30's I was diagnosed with plantar fasciitis and then a series of issues with most of my joints. Much later i found out that was actually the start of FM.

Over the years it always seemed that I was experiencing chronic tendonitis. So I learned to treat it with RICE. Rest, Ice, Compression, Elevate.

It's been a long road to my FM diagnosis but I still get the best relief when I treat my aches as tendonitis.

I've since added lots of hot baths and plenty of stretching. It's never going away but it helps more than anything else.
[h8phfxn] (score 1, diepte 5) Yep. It's a bit annoying to set up the foot bath in a comfy spot, but other than that, it does help.
[h8lcd3d] (score 1, diepte 2) good advice. I just had my new doctor run some tests to see if I have RA too. My mom has it, my feet hurt quite often (on top of all other joints, but also bone and muscle pain), but it feels like I am wearing ankle weights all the time now. My rheumatoid factor was checked a couple years ago and it was fine, but now my joints are more painful. My last doctor would only do 2 xrays. One of my thumb and shoulder. He said it looked like osteoarthritis in my right thumb, but my shoulder was probably a rotator cuff injury that I don't remember injuring or something.  I'm 36F, dont really overuse my joints. We will see!
[h8nun1q] (score 1, diepte 1) Okay so Bombas have the slight compression in all of their socks. They look pricey, but Ive literally had the same 6 pairs (I'm a minimalist lol) for 4 years. I used to have to replace my Hanes socks every 6-9 months. They are absolutely worth the investment
[h8l6txv] (score 1, diepte 0) Y’all, I just received new boots that provide the best support I’ve had in ages to help as I return to teaching elementary music in person. My heels are still a bit tender, not used to the support or level of activity. However, I don’t feel drained like I used to due to foot pain. The company is called Kuru.
[h8njznd] (score 1, diepte 3) oh come on.... okay, must have seen ANOTHER shitty rheum that doesn't believe in seronegative RA then. god. that pisses me off. i've seen so many providers and none of them want to treat me. 

thank you, i had no idea..
[h8ntcj6] (score 1, diepte 4) You're welcome! I was diagnosed by my 4th or 5th rheum, after years of hearing "your blood work and x rays are normal, you don't have arthritis". So I really feel for you, and am pissed for you too. I hope the next rheum is one who listens better!
[h8nk46c] (score 1, diepte 3) why the hell do they not know how to do their damn job??????? don't yall go to school for like 12 years??!?!!!?
[h8nn35l] (score 1, diepte 4) I was born with this affliction, seen my share of health professionals.
[h8laslz] (score 1, diepte 0) Yeah, especially during flare ups. I don’t know why exactly but working out helped a lot with that, and the less I sit down the less my feet tend to hurt. I also pretty much only wear Birkenstocks now which I find to be very comfortable:)
[h8lc3po] (score 1, diepte 0) Yes. I have plantar fasciitis, a bone spur in one heel, and arthritis in my big toe, and it has been acting up horribly. I went on an anti-inflammatory for two months and it helped a ton, but as soon as I went off it, bam, right back to the horrible pain. Stretches and massage help a little.
[h8ll70u] (score 1, diepte 0) Yes. Just now starting to attribute it to fibromyalgia
[h8lz5xc] (score 1, diepte 0) Yes.  Just have to live with it or have someone who can massage it constantly.
[h8m3f6w] (score 1, diepte 0) I thought my foot pain was just fibro, but an x-ray and a bone scan say I have osteoarthritis in the balls of my feet. I tried insoles but they just made the rest of my feet hurt instead. 

Now I have a new pain all along the inside of one arch (and radiating up into my ankle), so I'll be bringing that up at my next appointment. It never ends!
[h8mafnc] (score 1, diepte 0) Yes. It used to be excruciating. 

I found the less active I was the more it got worse. Not in the short term, but long-term. Like if I skip walking every day for months and then try to go on vacation where I’ll walk a lot, I’ll end up in a lot of pain. If I keep my level of activity up overall, then on busier more-walking days I do better. 

And also: good shoes. I searched high and low for the most comfortable shoes I could find. I have favorite sneakers, favorite boots and favorite sandals, so all seasons are covered 😂

Everyone is different. I hope you can find some relief.
[h8mhxg9] (score 1, diepte 0) Do you have high arches as well?
[h8ml5tp] (score 1, diepte 0) I stopped wearing socks a long time ago, because having that fabric on my feet was uncomfortable. If it’s super cold I wear “diabetic socks” with a wide elastic top I get at Dollar Tree. 

I wear Sketchers Go Walk series for shoes. I get ones you can slip on and get them a little larger than I usually wear to reduce any chafing. A nice thing about the shoes is they are machine washable.
[h8mlvx6] (score 1, diepte 0) Always!  I wish there was help but even my Cryoderm gel isn't working much anymore.
(9 reacties met lagere score weggelaten)

