# Label-batch batch_0157

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
Schrijf het resultaat naar `batch_0157.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1cj693v, 1djlvdy, 1q8791e).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1cj693v ===
SUBREDDIT: r/Biohackers
DATUM: 2024-05-03  SCORE: 112  REACTIES: 248
TITEL: What is the best supplement to improve blood circulation to the extremities, especially the feet? 
POST (source_id=post):
My feet are always cold and I always want to place them near a space heater.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l2dxyw1] (score 212, diepte 0) I work for a vascular surgeon. Nothing helps that except exercise. Walking is your best friend unless you have a blockage of course
[l2dzmwy] (score 83, diepte 1) Anytime anyone suggests exercise around here, they get down voted... Apparently they all want magic pills 😆
[l2e0n2k] (score 54, diepte 1) Walking is deff underrated. Cardio and calisthenics as well
[l2dtuaj] (score 43, diepte 0) Citruline, niacin
[l2duiia] (score 41, diepte 0) I exercise all the time and it hasn’t helped me, but I have Reynauds. Try a calcium channel blocker.
[l2dwp2k] (score 27, diepte 0) L-Arganine (nitric oxide),
L-Citruline,
Beet Root Powder (natural forms of the above two supplements mentioned),
Cialis,

Now if your issue is just cold feet, it could be because of a number of issues. People who fast often, even intermittently, will often complain of colder appendages especially fingers, hands, and feet.

Your issue may not be blood circulation so much as it is metabolism and fat distribution. You might benefit from some other supplements that raise core temperature like Cayenne Pepper, Ginseng, Green Tea Extract, but that may not sufficiently elevate your temperature and even then it may make you too hot while keeping your feet relatively cold.

To be honest, nothing is gonna beat having some dope socks :)

Experiment with them, but I recommend wool for an external sock, and something light and wicking (cotton or synthetic) as a sock “liner”. If you want just a comfortable all around single sock solution, maybe try “Darn Tuff” or “Bombas” depending on your style and desires out of a sock.

Also, consider compression socks. If you have poor circulation as you’re suspecting then compression socks are literally the best line of defense.

You can also research similar therapies for neuropathy as it may tangentially benefit you with nerve function AND circulation:

So things like acetyl l carnatine, alpha lipoic acid, matcha tea, turmeric can all be helpful. Lastly you can also benefit from items that improve circulation in feet like vibrating feet pads or the use of a massage gun. 10-15 of intense vibrational action daily will help improve circulation and it will improve nerve function and blood flow over time.


**Best of Luck!!!**
[l2edn6j] (score 24, diepte 2) While I agree, sadly some people are too sick to even do daily walks, like me for example. So in this case a pill with few to none side-effects would be great, since my hand and feet are almost always cold.
[l2ea0wm] (score 19, diepte 2) I've been going to the gym for several years and I've seen so much more change in 4 months of doing calisthenics
[l2eh961] (score 18, diepte 3) Try yoga or chair yoga. You don't need to walk. Follow a Youtube video...it's free.
[l2ectqu] (score 13, diepte 1) Citrulline works
[l2ewsq7] (score 13, diepte 6) I'm sure you don't mean it or aren't aware of it, but saying things like you just said is literally gaslighting, which, sadly, a lot of people with ME/CFS are confronted by, even from doctors. If you're interested, you could read up on the WHO, CDC, NIH, NICE, read the [NICE guidelines for ME/CFS](https://www.nice.org.uk/guidance/ng206), follow experts like [Prof. Dr. Akiko Iwasaki](https://twitter.com/VirusesImmunity) for some insides into immunity research in terms of ME/CFS or get into the upcoming [UniteToFight2024](https://unitetofight2024.world/) conference, which will be the biggest conference for ME/CFS there has ever been. There is still a LOT of stigma and misinformation around when it comes to this illness. Some experts call it the medical scandal of the century.

You simply cannot train or positively think yourself out of this illness or get better by accepting it. Trust me, all of my symptoms got psychologised for the first 6 years until I got the proper diagnose, and I've constantly worked via psychotherapies, psych. ergotherapy, rehabs, pain therapy, psychopharma, endless programs and courses plus meditation, affirmations, breathing exercises, yoga, tai'chi, you name it I've tried it, with the result that I'm not just physically but now also psychologically much worse off. So far there are no treatments, no medications except a few off-label options that may work for a few people, nothing but one recommendation that is recommended and officially accepted by every expert and doctor who knows and understands this illness: (strict) pacing. Meaning that you don't do more than you can't recover from until the next day.

Please, if you know someone with CFS, do your research before saying things like you said. You probably mean it well, but it's literally gaslighting. And please do not ever force them or push them to exercise and do anything they can't recover from until the next day...suicie rate is much higher with this illness and you could put people into being 24/7 bedbound, not able to go to the bathroom or feed themselves.
[l2fbnph] (score 13, diepte 3) I love calisthenics also - found Joe Wix on Youtube during covid times and I bang out his hotel room workouts often.  I can be way more consistent with that vs going to any gym.

My poor blood circulation in my feet is a huge bummer in my surfing and brazilian jiu jitsu hobbies.  I’ll work on foot calisthenics I guess?
[l2dyyq4] (score 12, diepte 0) Get your thyroid checked
[l2epbau] (score 12, diepte 0) If you're concerned about blood flow to the extremities, don't smoke cigarettes, don't chew, don't vape, don't Zin, don't chew Nicorette gum or take lozenges or sprays. No nicotine. It's a vasoconstrictor. Narrows and constricts your arteries, leading to less blood flow.
[l2e0mcj] (score 11, diepte 2) What? 🙀 there isn’t any magic pills??? Fuck me I’m on the wrong thread.
[l2eiywe] (score 11, diepte 4) Sadly not possible, but thanks for the suggestion. Would immediately do that stuff if it were possible.

And before others tune in, here's why: I have severe ME/CFS, need to lie down at least 23h per day and the little energy that I have left I have to use to go to the bathroom, brush my teeth sitting down, heat up food sitting down, type a bit on reddit. Anything beyond that, even drinking a bit more tea and having to go to the bathroom more often, will lead to severe worsening of my symptoms, mainly the fatigue and what I can do, with a chance of lasting worsening. Due to PEM (post exertion malaise) as one of the main symptoms, there's also no way to train yourself out of it...I've tried that for 6 years until I got the proper diagnose.
[l2eyq6m] (score 10, diepte 6) As I said to the other person, you may mean well, but you have no idea what you are talking about. Chronic fatigue is not the same as Chronic Fatigue Syndrome. There are also no meds for CFS, only off-label options that work for very few people and are usually targeted towards the immune system, plus the co-morbidities like histamine/MCAS, fibromyalgia/SFN, CMD, POTS,... There is a lot of ongoing research into the pathophysiology, mainly in the area of neuroimmunology. Some experts call it the medical scandal of the century.

I've lost 10 years of my life to this illness, the first 6 years I got told it's all psychological, so I did everything I could with psychotherapy, rehabs, psych. ergotherapy, pain therapy, meds, great diet, sleep, massages, yoga, tai'chi, strength training, I literally did a strength coach certification and nutrition coach certification when I was mild....you name it I probably did it. The result is that I'm now physically severely ill, and also psychologically much worse. That's PEM (Post Exertion Malaise) for you.

Again, please inform yourself before spreading information such as you just did, that's literally harmful to people with this illness.
[l2f10v7] (score 10, diepte 6) Please stop saying these things to people with CFS/ME.  Being told to "eat right and exercise " is exactly the reason why there is such a high rate of suicide in these patients.
[l2dukiv] (score 9, diepte 0) Exercise. Exercise. Exercise. Just go for a long walk every day.
[l2e0iv6] (score 9, diepte 0) If you're a man, try Cialis. It's a erectile dysfunction drug but also has other benefits such as improved blood flow to extremities.
[l2f4lvl] (score 8, diepte 7) Sorry you’re going through this. Respect for correcting this person in such a friendly and respectful manner. I hope you have happiness soon however that may be
[l2elqqp] (score 8, diepte 4) Oh you just reminded me...I ran out of a few supplements and cold feet and hands got worse again. I need to double check but I think it was the kelp (iodine rich).

Dying? Well, likely significantly faster than other people who can do all the healthy basics. There's also much worse chances of surviving other serious illnesses when dealing with ME/CFS.
[l2ebk8c] (score 8, diepte 0) This may seem odd. But have you checked your ferritin levels? After starting to work out like crazy my levels dropped because my muscles were exhausting the iron in my blood. I started to get numbness and tingling. My ferritin was way low. Started supplementing with iron and I’m good to go.
[l2e0p4w] (score 7, diepte 2) You can’t beat Raynauds. You can treat the symptoms. I wear gloves into the spring & fall & that seems to help my hands. My dr really talked me out of trying calcium channel blockers. She said there’s too many side effects.
[l2f0kij] (score 7, diepte 2) If someone has poor blood circulation, recommending them vitamin k supplements is a ridiculous mistake. Vitamin K, both K1 and K2, regulate the coagulation cascade of the body, ie, they make blood clots. More vitamin k means easier to produce bloods clots, and in someone with poor blood circulation to the legs this means increased risk of deep vein trombosis and pulmonary embolism.

You should not suplement vitamin K unless advised by a doctor.
[l2e0vpp] (score 7, diepte 3) You're looking for the meth and ecstasy thread
[l2eggqg] (score 7, diepte 1) I do (and take) almost everything recommended here. Lots of daily exercise. Thyroid is fine. My feet are still cold. I think I'm just one of those people.
[l2ezrx6] (score 7, diepte 1) I can vouch that this works for women too! (You’ll just have a harder time getting a prescription, but it’ll easy enough for men to get it at the drop of a hat, and a friend / family member might help.)
[l2h81e0] (score 6, diepte 3) Increases nitric oxide which is important for vasodilation/cardiac health, respiratory response and there are various things that deplete NO in the body. So it’s just a really good amino acid. It’s one that I’ve seen good results with among many supplements I’ve tried.
[l2ek1sz] (score 6, diepte 5) Have you tried amphetamines or Wellbutrin? The latter did amazing things for me after I was diagnosed with CFS. Hang in there.
[l2fayp6] (score 6, diepte 8) Very kind of you, thank you. Literally makes me emotional haha <3
[l2e3e43] (score 6, diepte 2) Possibly yes. If you have a blockage in your legs, when you exercise the muscles demand more blood flow and walking cause cramping in calves or buttocks if one is present. I’m not saying that’s what it is but it would not hurt to have it evaluated. What you’re describing is claudication.
[l2eftgw] (score 6, diepte 0) Sauna works wonders for me
[l2euf6y] (score 5, diepte 1) High dose niacin treats Reynaud’s too.
[l2fc7rl] (score 5, diepte 1) Citrulline yes, arginine is not very efficient however. Beer root powder(or just plains beets) is an amazing vasodilator as well.
[l2f1ccl] (score 5, diepte 5) Please ignore these commenters telling you to "just exercise".  It's like tellimg someone in a burning buiding to "just think positive".
[l2f9qde] (score 5, diepte 5) I feel you, I have POTS syndrome after being really sick with COVID. I would look into research peptides. I've experimented with a few but still haven't found one. BPC did make me feel a little better and I'm looking into trying PT-141.
[l2eyckx] (score 5, diepte 4) Due to science, CFS/ME equals 20 years of life less than average.
[l2en0vc] (score 5, diepte 2) Reynauds maybe
[l2ejum7] (score 5, diepte 0) QiGong.
[l2erkcn] (score 5, diepte 0) Maybe cayenne pepper?
[l2dtkin] (score 4, diepte 0) Exercise. Lift weights and go for a run.
[l2dtqc0] (score 4, diepte 0) Korean ginsing supposed to be good.
[l2hh0op] (score 4, diepte 1) Yep I no longer wake up with my arms or hands asleep since I added this.
[l2e3sp4] (score 4, diepte 3) Didn’t mean to imply it was reversed and no longer genetically present. Just that it was for the most part phenotypically less present. Just murder me for the semantics though.
[l2elmzp] (score 4, diepte 2) This is not terrible information. Lots of tumeric brands are contaminated with lead chromate for color.

Best to get brands that do lab testing. I just ordered some nootropic depot curcumin because of this. It is more expensive, but I am wary of the cheaper brand tumeric supplements.
[l2escqf] (score 4, diepte 1) I believe Arginine helps my chilblains in toes and I feel warmer in extremities and overall. The increased blood flow can give me a headache at times though. Aside from exercise it has had the clearest result for me.
[l2e1rds] (score 4, diepte 3) Excercise is the magic pill.
[l2e4z4y] (score 4, diepte 4) 100% agree.
[l2fa3h8] (score 4, diepte 8) Thanks for asking and the curiosity. One of the cardinal symptoms of this illness is called PEM (Post Exertion Malaise), which means an unproportional worsening of fatigue and other symptoms after exertion, depending on severity, and which can be lasting. Imagine it like having a moderate to severe flu...you may be able to "activate" yourself to get out and go for a walk or buy some groceries to make soup, and you may actually feel better for a while, but at one point you'll completely crash and will have significant worsening of several symptoms for a while. For CFS that worsening can last, literally until you pass away.

The rehabs and especially the pain therapy were always resulting in very severe worsening for a couple weeks and then significant lasting worsening. Most of these therapies and rehabs and whatnot were initially helpful for my mental-emotional wellbeing, had some positive effects on some of my personality traits, how I deal with certain emotions and such, but they did not only not help with my physical symptoms but due to the overexertion actually made me physically much worse, and due to that, psychologically much worse. Add on top the constant setbacks, crushing of hope, worsening of symptoms, loss of friends, job, relationship and future outlook, the gaslighting and traumatic experiences with doctors, the total lack of support and therapies.
[l2fbufr] (score 4, diepte 6) Yeah POTS is not to be underestimated. Even though that's very easy to diagnose, took the doctors 8 years until I had the diagnose. Having tried a couple meds and upping my salt drastically, the only thing that helps significantly are compression stockings.

I have some peptides noted on my list of things that seemed to have helped a few people before. Though that was someone who has/had CFS and took them for a different reason, though likely a comorbidity: Peptides LL-37 & BPC-157 - [https://forums.phoenixrising.me/threads/me-cfs-patient-goes-into-remission-after-taking-elixir-of-youth-gdf11.79778/page-2#post-2272282](https://forums.phoenixrising.me/threads/me-cfs-patient-goes-into-remission-after-taking-elixir-of-youth-gdf11.79778/page-2#post-2272282)

Lot's of strength and best of luck on your journey!
[l2e2un4] (score 4, diepte 1) When I walk it feels like my calves are going to explode.
The pain cripples me, would this be vascular?
[l2e4qzo] (score 4, diepte 5) Yep! L5/s1 damage, I have fasciculations down the backs of both legs 24/7.
It feels like micro fireworks going off constantly.
That might sound weird but that's how I can only explain it.... Maybe like diet coke running through my veins fizzing and popping.
Strange!
[l2elr9c] (score 4, diepte 4) Do you wear compression socks?
[l2ejfj0] (score 4, diepte 0) I found nattokinase helps
[l2esh7c] (score 4, diepte 1) I was thinking along the same line. A vasodilator may help but movement will be key.
[l2e9ah0] (score 3, diepte 1) Yes, I was coming over here to say this. Red Ginsing is good. But exercise as stated in another response is probably best.
[l2eup6g] (score 3, diepte 1) It has helped my cold hands and feet
[l2h3lvn] (score 3, diepte 2 OP) What does citruline do, just general vasodilation?
[l2h3ldt] (score 3, diepte 1 OP) What does citruline do, just general vasodilation?
[l2du01b] (score 3, diepte 0) Cialis and EPO I guess?
[l2ew3qs] (score 3, diepte 4) Omg don’t be so dramatic 😂
[l2e4y1q] (score 3, diepte 1) Or vitamin k2? K2 cleans up calcium in the arteries
[l2dv7ro] (score 3, diepte 0) more clothes. not just on your feet. body makes blood move away from extremities when cold.
[l2e3hkm] (score 3, diepte 4) Gotcha 😉
[l2enjbn] (score 3, diepte 5) It's over bro, just keep using the feet warmer..

With this mindset of nothing will work for chronic fatigue it's over anyways till you change this mindset regardless of what your conventional doctor told you.

Study food, eat right, exercise/move you're body, practice mindfulness!!! I noticed a lot of CFS meds are related to chemical imbalances so these things will be key. 

Also note you're conventional doctor is not trained in any of those 3 things and will not be able to offer you the guidance needed in that regard as they are in fact not messiahs.
[l2gqv8c] (score 3, diepte 6) Thanks for the suggestion. I've tried that. Makes me jittery and doesn't help. Kinda like coffee does to me.

I'll try it again though in the near future to at least try to combat some of the PEM. From my research of recovery stories somewhere in the 3 digits, supplements and even B12 IVs and such seem to have helped very few people, even complete stacks for the mitochondria involving D-Ribose, CoQ10, PQQ and so forth. Dr. Myhill from the UK is a big proponent of these, plus a ketogenic diet, though in the Myhill facebook groups I've observed over months and months, there seem to be very few people who benefit from the things she suggests. Same with a bunch of these "clinics" who advertise for treating CFS, Fibro and so forth. I've yet to see more than a handful of people who seem to have benefited from that to the degree where they were able to get their lives back, and it's unclear whether they had actual ME/CFS.

I've also read about some research and development of a medication in Japan if I remember correctly, which targets specifically the mitochondria, but haven't heard of any news in that regard.
[l2e3rhd] (score 3, diepte 3) It absolutely feels like claudication, they did an ultrasound but couldn't find anything but the pain hasn't gone away.
Standing and walking aches like hell.
Maybe I should get a second opinion.
Oh I do get palpitations daily for around 5 years too.
Still undiagnosed.
[l2e3w6e] (score 3, diepte 4) Could be neurogenic claudication. So you have any lower back issues
[l2ea00z] (score 3, diepte 1) Can massage work as well?
[l2em489] (score 3, diepte 2) Same, I workout 5 times a week and walk daily and my fingers turn purple from warming them up under warm water bc they’re so cold to begin with.
[l2f9co4] (score 3, diepte 1) I have POTS syndrome and sometimes I can't exercise because of the symptoms and I have to stay reclined. Any other suggestions when walking is not an option?
(224 reacties met lagere score weggelaten)

=== THREAD 1djlvdy ===
SUBREDDIT: r/Biohackers
DATUM: 2024-06-19  SCORE: 59  REACTIES: 129
TITEL: What shoes are you wearing for long walks/ being on your feet for long periods? 
POST (source_id=post):
Looking for something with more support than barefoot shoes but less than hokas for example

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l9cl5bk] (score 65, diepte 0) A very important thing people overlook is wearing the same shoe everyday. If you are on that shoe all day it is going to compress slightly. You need to rotate your shoes to let them decompress and air out. This will not only extend the life of your shoe but your feet will thank you!
[l9bvsge] (score 42, diepte 0) Hoka… my feet have 0 pain when I wear them
[l9bw66q] (score 27, diepte 0) Brooks! I only wear Brooks for long walks.
[l9c1rka] (score 21, diepte 0) Vivo barefoot
[l9cr7k7] (score 20, diepte 1) This really is the move. I always rotate my shoes between shifts. When I was pregnant, I even would swap them halfway through the day!
[l9cej8v] (score 14, diepte 0) Xero
[l9c78g2] (score 12, diepte 0) Prescribed insoles are a game changer.

They make every shoe or boot great for long walks or standing or running.
[l9d5oo4] (score 11, diepte 1) Hoka’s truly changed my life. I hope their quality doesn’t get worse over time
[l9d4cck] (score 10, diepte 2) I am a big fan of Brooks, the ghost or adrenaline. That is what I wore when I was on my feet all day working retail. I had 2-3 pairs of them and made sure to never wear the same shoe two days in a row.
[l9cqv5f] (score 8, diepte 1) Yeah, I have different shoes for different parts of my life and different seasons, so there's a lot of rotation. I have a street sneaker, casual boot, walking/hiking shoe, gym shoe, casual sandal, dressy boot and shoe for work (daytime and evening), rain boot, winter boot, kayaking sandal, light hiking sandal. But they last years, since there's variation day to day, so it's not like I'm buying these all at once...
[l9d14ef] (score 8, diepte 0) Altras
[l9bwsy9] (score 7, diepte 0) Altra Olympus 5, especially if you have wide feet.
[l9bzlwt] (score 7, diepte 0) Kuru Quantums


I have very high arches, and these are the only shoes I've ever owned in my life that I don't have to add orthotics to. I'm also a nurse, and I have zero foot pain after a 12 hour shift in these. Better than Brooks or Hokas for me.
[l9cqy0f] (score 7, diepte 0) I work 12s and am on my feet for pretty much all of it... then most days off, I hike or putz around doing farm chores on my property. 

The secret is having several \*different\* pairs of comfortable shoes. So if I work two days in a row, I wear my Sanitas clogs (highly recommend, way better than Dansko) the first day, then my Birkis the next day. Three in a row, I throw my crosstrainers in for added variety. Then at home, I rotate between Blundstone boots and Birkenstocks. Sure, I own a lot of shoes, but each pair also lasts longer this way, too. 

Also do not sleep on good quality compression socks! That's half the battle right there. My absolute favorite are Wellow, but they're pricy when not on sale.
[l9d733t] (score 6, diepte 1) Totally depends on the shoe. Tree/Wool Runners are comfy but a bit soft and aren’t great for long walks. 

Tree/Wool Dashers however are among my favorite for walking. Easy to slip on, look nice from gym to office, breathable, and imo they are super comfy and supportive. I can walk miles and miles per day on work trips and Tree Dashers and either some Hokas or On Clouds are in every travel bag. 

There’s a medium heel-toe drop on Tree Dashers so if you like zero-drop for running (my preference), they’re not ideal. But for walking, that extra support is perfect
[l9bub27] (score 6, diepte 0) Earth runners
[l9diw69] (score 6, diepte 2) I have read on running forums that they aren’t great for running. Lots of people saying they only get 200 miles or so out of them (the bounce goes away). Others saying 600+ miles. Seems like some agreement that they are better for walking than running.
[l9c48xo] (score 6, diepte 0) Altra paradigm 6 for walks and runs and Thursday lowtop sneakers at work. At home I wear croc slides inside and outside the house.
[l9d0vbr] (score 6, diepte 0) Altra is my goto trainer and daily. I have like 6 pair currently in rotation...everything from boots, recovery/long run shoes, to go fast carbon plates. Still mix things up a bit and have a couple pair of Hokas, 3 pair of Asics, Brooks, Topos, and some Ons.
[l9c6em8] (score 5, diepte 0) I’m a huge fan of on running shoes! Most comfortable shoes I’ve ever had
[l9cxbs0] (score 5, diepte 1) Where can you get them from in the UK?
[l9cz9ro] (score 5, diepte 2) Podiatrist
[l9dlm6k] (score 4, diepte 2) Tree Dashers have been my go-tos for the past couple of years if I have to standing or do a lot of walking. Just got some On Running Cloudmonsters and Hoka Clifton 9’s and they both seem very good too.
[l9dovfs] (score 4, diepte 3) It still blows my mind how quickly hardcore runners wear out sneakers.
[l9drkw2] (score 4, diepte 2) Ghost and Ghost Max
[l9cviw9] (score 4, diepte 0) Housework - compression socks and Birkenstocks. Gotta love that cork!

Walks or runs - Brooks launch
[l9d7y9q] (score 4, diepte 0) On Cloud Eclipse!
[l9bpe7b] (score 3, diepte 0) Allbirds are okay…
[l9cld8g] (score 3, diepte 1) Same, big daddy!
[l9d4umk] (score 3, diepte 1) This, the Bondi 8 changed my life.
[l9dme1y] (score 3, diepte 3) They have a hierarchy of models. The higher end you can push 3-400 miles depending on your weight. Mid tier is 20-300 miles. It’s like a soft car on a car for traction. Soft, less mileage. I wear the stability version of Hoka’s, so they are a little firmer, but still only moderate mileage.
[l9dr7cr] (score 3, diepte 4) Right? That’s like a new pair every 6-12 months? Maybe even less?
[l9c63eq] (score 3, diepte 0) Just bought a pair of Bedrock “barefoot” style sandals from REI the other day, I’ve put some miles on them already and they’re really comfortable!
[l9ffedz] (score 3, diepte 3) I wear Saucony Ride 14s and now have 10 of them because they are no longer available. The 15s and up aren’t quite as stiff and give me some issues with my heels. I’ll likely move to Brooks when these are all worn out. I walk / run about 5-7 miles a day.
[l9dwz07] (score 3, diepte 1) Never really thought about that , thank you
[l9dk6ok] (score 3, diepte 1) “Putz around” 😝. Love it. I say same thing
[l9d83zs] (score 3, diepte 1) God I love my Birks for around the house, they are so perfect!
[l9d4a2b] (score 3, diepte 0) Brooks
[l9d6hqd] (score 3, diepte 0) Rotation is key! I rotate workboots, depending on what Im doing (asphalt, mud, concrete, etc.); walking i wear either Brooks Ghost Max or Crocs, depends on where im at and what im doing like we cant wear workboots into the office so we wear shoes or slides in, or theme parks i wear my shoes; running i wear Brooks Glycerin, only time wear them is to run.  I also only wear socks on long runs and workboots, i can go sockless up to 6 miles and my cycling shoes are sock lined.
[l9d8kf0] (score 3, diepte 0) Run on clouds, Saucony, Adidas comfortable cushion versions.
[l9e892e] (score 2, diepte 3) I love those Cole Haans. That's an awesome shoe for a guy. I have a shoe that looks exactly like the woman's version, but the Cole Haans seem so much more comfortable. I had been thinking about replacing the ones I have with those.
[l9f3zhv] (score 2, diepte 5) lol bro. I run 80-90km a week. means a 200 mile should is gonna last me 3 months
[l9dm7gy] (score 2, diepte 2) I have Hokas too . They don’t last as long as they used to just a few years ago . Still the most comfortable shoe for me .
[l9dl8ur] (score 2, diepte 1) Which model?
[l9e7yqa] (score 2, diepte 2) Adrenaline for longer walks (they’re light and have great stability) but Beast for more strenuous walks (they’re heavier but have the best stability).
[l9fw94y] (score 2, diepte 1) I used to be in constant shin & foot pain till I walked in a Road Runner store almost crying because I was at my wits end. The salesman gave me a pair of Brooks to try & that’s all I have worn since. I would be happy if they brought back the Glycerin 19 version. Every version of the glycerin has since stunk in comparison.
[l9ge6ju] (score 2, diepte 2) Please send your comments to Brooks!  They listen!  I am a Ghost and Ghost Max fan.  One of my doctors at the VA suggested I buy Brooks.  My feet were healing from plantar fasciitis. Told me to invest in good quality shoes and she said Brooks are the best!
[l9hhg08] (score 2, diepte 3) I have . I’ve begged . I bought every pair I could find . I have plantar fasciitis & flat feet & the glycerine 19 gts were superb . I do wear the adrenaline gts & have bought every variation of the glycerine 20-22 gts but they’re too wide . I’m glad Brooks worked out for you too!
[l9c7g7q] (score 2, diepte 1) I wear Kuru Atoms for the gym--love them, on my second pair.
[l9fcqav] (score 2, diepte 1) Did you slowly break into them like the website says, or was it instant relief?
[l9g18ds] (score 2, diepte 2) I personally didn't have to break mine in, but I didn't have foot problems like plantar fasciitis, not sure if that matters. I tried both styles and kept the Atom because they are lighter and have a mesh upper, so they are better for my gym activities. I have super high arches, a narrow heel, and somewhat wide forefoot, and the regular width is perfect for me. The wides are really wide for anyone who needs that. And even though I have Superfeet insoles for a lot of my shoes, the insoles on these are truly amazing, better than any insoles I've ever tried.
[l9hidca] (score 2, diepte 3) Ty!
[l9dyy58] (score 2, diepte 1) Bedrocks are amazing
[l9cammu] (score 2, diepte 0) Hoka
[l9ehm9u] (score 2, diepte 3) I have the Clifton 9’s which are also very good although slightly firmer according to the Hoka website.
[l9dxthq] (score 2, diepte 1) Only brand I buy now.  I've owned several different of them, love them all so far.
[l9ggdyh] (score 2, diepte 2) Same, I have 8 or 9 pairs
[l9chogo] (score 2, diepte 0) I'd say the insole is just as - if not more - important than the shoe. Superfeet insoles are amazing IMO.
[l9fdqch] (score 2, diepte 1) I'm so onboard with this. I can be on an intense hike and the rest of my body feels great but my feet are failing.
[l9crrg8] (score 2, diepte 0) San Antonio Shoes (SAS)
[l9d1vgg] (score 2, diepte 0) I love Orthofeet best ever hands down.
[l9dax09] (score 2, diepte 0) I work at a standing desk all day and I use a pair of Adidas running shoes. I find if I go barefoot I get heel pain. The shoes have never been outside and I only use them inside.

As per walking I do the same thing. I find those types of shoes offer the best support but not too much and are light
[l9depez] (score 2, diepte 0) Chacos
[l9dixvc] (score 2, diepte 0) You will never find me in anything other than Fivefingers, of various types. That’s been my only shoe for close to a decade.
[l9dvvaz] (score 2, diepte 0) The orthotics are even more important than the sneakers.
[l9dyb9t] (score 2, diepte 0) Lems
[l9e936b] (score 2, diepte 0) A good pair of boots, I have Redwings and Irish Setters.
[l9f2zz4] (score 2, diepte 0) Brooks adrenaline for me. Never knew my feet hurt until they didn't.
[l9eb6e0] (score 1, diepte 4) Same. I can get 300-400 miles out of each pair when I rotate them with a few other pairs.
[l9fbsgp] (score 1, diepte 6) What's typical wear out for you? What generally goes first? What brands do you like/dislike? My bro in law runs so I'm kinda interested
[l9dl5dn] (score 1, diepte 1) Hoka Clifton 9 is very good. On Running Cloudmonster and All Birds Tree Dasher 2 are very comfortable for lots of standing/walking.
[l9e3t6x] (score 1, diepte 1) Which types?
[l9bwc24] (score 1, diepte 0) 30 year old one strap leather flippers
[l9bwjwl] (score 1, diepte 0) new nike runners
[l9f5191] (score 1, diepte 1) these are the only shoes that don’t cause me pain. I’ve even tried brooks and hokas
[l9cjkqs] (score 1, diepte 1) Same!
[l9c3wf8] (score 1, diepte 0) Whatever shoe you normally wear, with superfeet insoles
[l9e0c2f] (score 1, diepte 1) Unfortunately, on cloud qualify went down the drain in the last few years. My first on clouds cloud 5 that i have purchased before they became popular in the US (2014?) lasted me over 3 years of walking/traveling around the globe. The next pair started breaking siren after a year. Now the pair i have purchased last December, is already all teared up in multiple places, and I only used it for walking. This is my last pair...
[l9c8acx] (score 1, diepte 0) Obōz Sawtooth X Low (Women's) for walking and day hikes, but they're beginning to wear out. Not sure what I'm going to get next.
[l9c9e8v] (score 1, diepte 0) New Balance walking shoes
(51 reacties met lagere score weggelaten)

=== THREAD 1q8791e ===
SUBREDDIT: r/Biohackers
DATUM: 2026-01-09  SCORE: 63  REACTIES: 129
TITEL: Why do some people living indoors have cold hands and feet? Is there any deficiencies going on in them?
POST (source_id=post):
In winter, me and my dad always have warm hands and feet. While my mom, sister and brother have always got cold hands and feet despite staying indoors.

Is there any reason behind this? Does deficiencies cause it? I yes, then which supplements to take?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nylcovv] (score 107, diepte 0) Its probably blood flow
[nylf87n] (score 90, diepte 1) Cancer. Probably cancer. Frozen-hand-cancer. Deadly. 1 week, max.
[nylkpes] (score 61, diepte 0) **Raynaud Syndrome (aka: Raynaud's Phenomenon). Runs in my family.**
[nylncmf] (score 44, diepte 0) Hypothyroidism can cause this. It feels cold from the inside, not just like cold air.
[nylvw5h] (score 33, diepte 2) Thyroid is just one of several causes.
[nyljcq0] (score 29, diepte 0) It can be caused by a ton of different things. Some are nutrient deficiencies and then there's also the vague endocrine/autoimmune/neurological stuff that affects the blood vessels themselves that's been severely understudied cause it disproportionately affects women. 


Its also considered a normal gender variance. Part of that is men and women have different body comps of muscle & fat which innately will change how the body manages heat, part of is is some evolutionary suspicion of why the body might intend for women to manage heat differently. So it isn't innately suspicious , but the carve out is that the autoimmune problems and nutrient deficiencies in question also tend to affect women more. Is itor just health problems we've normalized? Who's to say? Not the medical establishment, which until covid and ozempic preferred to pretend endocrine research was nigh impossible 


They could get a blood panel to see if they're deficient in anything otherwise unless it's really bothering them it doesn't really matter. Wear socks, drink water, occasionally try to stand up or shake your body up to get blood moving, avoid stress. I find keeping the my house at a temp other people find reasonable and then using an electric blanket actually works better than turning up the whole house to my preferred range. I think because I can apply head directly to the veins and bypass my bodies garbage temp regulation entirely
[nymcewn] (score 23, diepte 0) Are yall the same bmi? My chubby friends: warm hands n feet. My skinny friends: cold hands n feet.
[nyltmmr] (score 19, diepte 1) Exactly, hypothyroid = cold body temperature partly due to vasoconstriction. Fixing the thyroid and metabolic system resolves it.
[nylhzsf] (score 16, diepte 3) Oh, so you mean it is probably not the well known frozen-hand-cancer everybody is talking about??
[nylgy3g] (score 14, diepte 2) I’ve had it for years now. Probably all my life.
[nylwrmu] (score 14, diepte 2) I was born with it and my thyroid is fine. There are many different causes.
[nym1npx] (score 14, diepte 4) I am 47 years old and have had extensive blood work done for other issues for decades. I can assure you that my thyroid is fine. 

Please go outside and take a big breath of fresh air.
[nypjlm9] (score 14, diepte 1) My doctor put me on cialis for the winter months for Reynaud’s and my life is changed! It’s incredible to not have freezing, stiff hands and feet.
[nylzt4d] (score 13, diepte 0) Iron deficiency
[nyloa2v] (score 12, diepte 0) Could be overreactive sympathetic nervous system?
[nyliae5] (score 11, diepte 4) Unless I’ve been dead for the last 22 years, that’s possible too
[nylvfcp] (score 10, diepte 3) 1. It’s ancient medicine, been around for longer than we can imagine.
2. Many plants and herbs can and do have medicinal value.
3. Placebo is a powerful thing.
4. I get the pushback, truly, western medicine is more robust and yes backed by actual science, but 
5. We can just DO BETTER in our responses. This is online, but still at least 1/3rd of us hopefully are actual people on the other end of the comments. And for the 2/3rds or whatever the estimate is now that aren’t actually people, it would be so nice to train these things to be nice. But I hear you, truly.

Personally I’m not a big follower or practitioner of Easter medicine TBH, but I would love to know what was in that Gypsy magic TCM potion because I have Raynauds and feel like a lizard person. My internal temperature tends to be low and whatever it is outside is what I’m more in sync with. What were these herbs?!?!
[nymhvcx] (score 10, diepte 4) Complete bs, If you dont have the knowledge of basic physiology, atleast don't spread false information. 3 are measured in standard thyroid function test: t3, t4 and tsh. Measuring just one in isolation is meaningless. No doctor would ever just measure 1 marker alone. Further tests are done if those 3 values are not normal.
[nylavsq] (score 9, diepte 1) Cool, cool. Just for reference, how exactly are you taking 20 GRAMS of Vitamin C throughout the day?
[nylajww] (score 8, diepte 3) Of course they do, but "stagnant chi" is bullshit.
[nylcmxx] (score 8, diepte 4) I mean it’s just the way they say stuff. It means low circulation in American.
[nymnn8t] (score 8, diepte 3) Broadly speaking, overactive stress response (cortisol) causes excessive adrenaline which = vasoconstriction and cold extremities. Fixing the metabolic (thyroid, mitochondrial) system will address the underlying cause for the overactive stress response.
[nym0oho] (score 8, diepte 0) I suffered from cold hands/feet for years, did some research and started supplementing with iron, zinc, magnesium, copper, boron, selenium, B1, B6, B12, C, D3, K, etc. and drinking plenty of water. My symptoms go away unless I get lazy with the supplements. Do your own research to learn the dosages and schedules as some are toxic above certain levels, for example iron. I asked gemini to produce a table of the best dosages and dosing schedule for the top supplements, then asked it to add my specific supplements to the table. IANAD.
[nylcd3s] (score 7, diepte 1) 20 fucking grams mate? 
Go take a scooper for your creatine, generally thats 5grams
[nylecls] (score 7, diepte 1) You’re just providing your experience, sorry others are being rude about it. Thanks for sharing!
[nylwy15] (score 7, diepte 2) This. When I worked an intense remote job and was sitting for most of the day, every time I took a cold shower my feet and hands would turn blue and I would be unusually cold. Now that I’m unemployed and have been eating better my metabolism is 10x better and I never feel cold (where I live the lowest temp comes to about 10 Celsius, so not extreme)
[nylpigc] (score 7, diepte 0) Hormones probably. My brother and mother have thyroid issues and I’m in early menopause and we are all cold. 🫡
[nylx46v] (score 7, diepte 0) I'm sure a major contributor is thyroid. I've noticed a significant difference in how cold my hands and feet are within a day of fasting (negative) and taking a few drops of lugols 2% iodine (positive). And most of the time I'm the warmer one in my family.
[nymnid9] (score 7, diepte 0) For me, i grew up smoking cigarettes and drinking coffee. Both were causing my veins to constrict very intensely (is that how you say this? Not my native tongue).
I grew up thinking something was wrong with my body, always having extremely cold hands and feet.
Quitting smoking and quitting vaping nicotine made me realise nicotine is a big factor. Then same with caffeine when i cut that. Cutting both out of my routine caused my hands and feet to be normal again, always.
Smoking is bad.
[nylce1s] (score 6, diepte 2) No
[nylbbgd] (score 6, diepte 1) If its truly 20g you should be worried about your kidneys
[nylc1i5] (score 6, diepte 4) Yeah this sub gets so weird at times
[nymo9ml] (score 6, diepte 2) My thyroid tests were all in optimal range (not just normal) as of October. So "usually" doesn't apply in my case.
[nymaolq] (score 6, diepte 0) I take stimulants for ADHD and they are notorious for vasoconstriction. My feet definitely feel cold a lot.
There are supplements for vasodilation like nitric oxide, beetroot, citrulline, arginine etc.
Most erectile dysfunction pills are vasodilators as well.
[nymk5ya] (score 6, diepte 0) Could be hormones, could be low body fat, could be nothing. I'm cold all the time, but dont have any imbalances or thyroid issues. I wish it was because of low body fat 😆 but nah. My bf is warm all the time, so thats nice:)
[nymrgzq] (score 6, diepte 0) I have pernicious anaemia, meaning I cannot absorb oral  B12 properly. 

Whenever I go too long between B12 injections I get terribly cold feet, so cold they even stay cold all night wearing socks in a warm bed. 

This may not be the cause for most people, but it can be worth checking out.
[nynhgpb] (score 6, diepte 0) Thyroid and low metabolic rate.
[nylcci7] (score 5, diepte 2) Yeah and most of the 20grams won't even get absorbed anyways.

I don't even know if 5g would get absorbed. 
Only if it was spread throughout the day
[nyl8630] (score 5, diepte 1) Nothing screams /biohacking more than TCM and a "stagnant chi"...
[nylcjc8] (score 5, diepte 5) Something gets extremely lost within the biohacking name and im not sure how
[nym4kck] (score 5, diepte 5) Ok, apologies that was an assumption on on my part. I found raw ginger very helpful before/during/after cold exposure. Either as tea or just chewed.
[nym3vzw] (score 5, diepte 2) How to repair it with concrète steps?
[nymttsg] (score 5, diepte 4) Yes I had all markers tested. I understand you're trying to help, but this is a Biohackers forum and I have gone above & beyond in testing, have goals to get all markers in optimal range, and am not the average patient who takes a doctor's "good enough" as gospel. My thyroid is perfect across testing at multiple points in life and my cold hands/feet is caused by something else (and frankly bothers my husband more than it does me lol).
[nylum3n] (score 5, diepte 0) Thyriod
[nyma40z] (score 5, diepte 0) Thyroid or blood sugar issues
[nylbbbm] (score 4, diepte 1) Taking large doses of Vit C for long periods might deposit calcium into your arteries. Look it up.
[nyla3uz] (score 4, diepte 2) If it work it works dude. Herbs are legit.
[nynlimq] (score 4, diepte 5) K - whoosh.
🌷
[nymtbt5] (score 4, diepte 5) Lots of people are linking it to covid, i never had an issue but post covid the tip of my middle finger on my right hand and a couple of toes on my left foot are affected in cold weather. I can go out in the snow  barefoot no problem, yet randomly ill touch something cold and my finger tip goes or ill go barefoot on a cold surface and my toes go! Very weird!
[nyrt11g] (score 4, diepte 2) Guess the stiffness goes elsewhere !
[nym5l1u] (score 4, diepte 3) Remove anti-thyroid and anti-mitochondrial things. Repair thyroid and mitochondria directly. There's many resources on how to do this.


The 3rd picture on this post is for restoring thyroid health:
https://www.reddit.com/r/Biohackers/comments/1q7peah/uncovering_the_secrets_of_womens_health/
[nym0x54] (score 3, diepte 3) Yes there are diminishing returns but it’s not so simple that you piss it all out, plenty of research on it when I did a deep dive
[nynjikb] (score 3, diepte 3) Its one of those things that has mixed results from studies. High doses of vitamin C helped tremendously with my sciatic pain, since I read those studies I stopped once the pain stepped. It mentioned long term big doses. Im sure short term is fine.
[nylbnmc] (score 3, diepte 5) That is so sweet, god bless you my friend :)
[nylah9d] (score 3, diepte 0) Could be due to the external temperature of the environment vs the internal temperature of the individual. There is to many variables here. This thread is ridiculous.
[nylu517] (score 3, diepte 2) More simply, vasoconstriction due to excessive adrenergic signalling.
[nynan21] (score 3, diepte 2) So wrong.  There is no cure for reynalds and nothing know that really improves it much.
[nynkjif] (score 3, diepte 3) Thats true if you believe what modern medicine tells you. But it might be naive to accept everything from modern medicine.
[nyocw1i] (score 3, diepte 1) This! I have this along with an aunt, and three of my kids. It sucks.
[nysicm2] (score 3, diepte 3) Ha, I’m a lady :) The pharmacist was really confused why I was picking up Cialis for me.
[nyn8bdj] (score 3, diepte 0) Hypothyroidism symptoms. 97.3 is my usual BT.
[nyp4mpm] (score 3, diepte 0) Reynauds

Pernio/chilblains (ask me how I know, FML)

Circulation issues
[nylafw6] (score 2, diepte 1) Do you definitely intend to write that you take 20 **grams** of vitamin C?  That‘s a huge dose!

[https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/expert-answers/vitamin-c/faq-20058030](https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/expert-answers/vitamin-c/faq-20058030)
[nym0mne] (score 2, diepte 2) Yes it is. Look into dr Klenner, dr levy, Linus Pauling etc. Humans lost the ability to produce vit c due to environmental reasons we have the genes we just can’t use it.
[nym1fqq] (score 2, diepte 2) I did just now and it says the opposite that it can help prevent it..?
[nylh7fv] (score 2, diepte 1) Ridiculous and a bit scary. I bet it’s literally down to individual variation in blood circulation and thermoregulation (blood pressure, capillary density and diameter, subcutaneous fat, activity level, etc.). 

But no let’s find a pill for your relatives’ cold hands.
[nyrblsr] (score 2, diepte 3) You have dying too? I've been gutted about having dying ever since I learned it's a thing aged about 7. Totally incurable too.
[nym4yh6] (score 2, diepte 1) This. Are you thinking of the lupus spectrum of auto-immune diseases or other?
[nym3e1o] (score 2, diepte 4) Okay, perhaps you need to work on your reading comprehension. I take cold showers because in my house we do not have hot showers. That is in no way related to what I said.
[nymkv0g] (score 2, diepte 2) Can you eloborate on this?
[nys9bsq] (score 2, diepte 3) You can supplement "active thyroid hormone" which is called liothyronine (T3). This can be bought otc as NDT (natural dessicated thyroid). NDT contains T3 as well as thyroxine (T4) which is inactive. 


The active form is key. Cells use the active form. 



Doctors ususlly prescribe thyroxine (T4) which isn't recommended to use stand-alone.
[nynm52v] (score 2, diepte 1) If you did a thyroid test to assess your thyroid then they're notoriously unreliable. A doctor can conclude that it's fine when it isn't. Low thyroid (hypothyroid) always causes cold temps. If you look at the first 2 images on this post you can see if you recognise anything else listed:


https://www.reddit.com/r/Biohackers/comments/1q7peah/uncovering_the_secrets_of_womens_health/
[nynlwpb] (score 2, diepte 0) I had a new brand of Ginko Biloba years ago. My fingers got really hot for a few days and then I never had any issues again. Thanks step-mom I had back then. Miss ya.
[nyof18h] (score 2, diepte 0) Selenium.  

Get a full blood panel then  work from there
[nyyggcx] (score 2, diepte 0) I used to always have cold feet. Then I started exercising regularly, especially running, 3-4 times a week. The coldness in my feet disappeared for approx 20 years. I had to stop my running hobby 5 years ago due to other causes. Now my cold feet are back. For me at least it was a circulation issue.
[nyl49i8] (score 1, diepte 0) Welcome to r/Biohackers! A few quick reminders:
- **Be Respectful**: We're here to learn and support each other. Friendly disagreement is welcome, but keep it civil.
- **Review Our Rules**: Please make sure your posts/comments follow our guidelines.
- **You Get What You Give**: The more effort and detail you put into your contributions, the better the responses you’ll get.
- **Group Experts:** If you have an educational degree in a relevant field then DM mod team for verification & flair!
- **Connect with others**: [Telegram](https://t.me/biohackerlounge), [Discord](https://discord.gg/BHsTzUSb3S), [Forums](https://biohacking.forum/invites/1wQPgxwHkw), [Onboarding Form](https://go.meiro.cc/0721334)

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Biohackers) if you have any questions or concerns.*
[nyroyt7] (score 1, diepte 4) It's easy and natural to be dismissive of far-flung people's, but the more you understand the ancient cultures of the East the more you're humbled by the wisdom and insight they had and have..probably from stability of culture through great periods of time, versus the West.

I was walking down the street with a kid when I was 5 or so, and asked him why he talked funny.  He said 'I have a speech impediment.', I said '..there's no such thing.'  I carry that lesson with me (for 40 years now) as a basic example of how we tend to dismiss as nothing, what we don't immediately intuit or understand.
[nys4abq] (score 1, diepte 5) ![gif](giphy|7SOdwNYHzCI7ygrLw7|downsized)
[nymm3ag] (score 1, diepte 5) You'll find that testing TSH alone is standard in many places. If they do look at T3 & T4 then they usually ignore rT3. There's also the issue of measuring free v total T* which gives different interpretations. It's not necessarily as simple as you present it.
[nys3lrv] (score 1, diepte 5) Unfortunately they will just do one if you ask for a thyroid test at times.
(51 reacties met lagere score weggelaten)

