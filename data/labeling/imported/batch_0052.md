# Label-batch batch_0052

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
Schrijf het resultaat naar `batch_0052.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(2 threads: xj4eyu, rp05ja).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD xj4eyu ===
SUBREDDIT: r/pharmacy
DATUM: 2022-09-20  SCORE: 41  REACTIES: 101
TITEL: My feet are on fire 🔥 at the end of my shift
POST (source_id=post):
I am a pharmacist for 9 years. Not only do I have to deal with customers who make my life hell, but when I come home from a long shift my body is a wreck, and especially my feet are killing me 😱

Any tips on how to get rid of foot pain?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ip6k9e1] (score 41, diepte 0) I love to put voltaren gel on my sore feet. I wake up like new.
[ip6tkj8] (score 39, diepte 0) If you haven't had your feet fitted, do so.  Make an appointment with a podiatrist for inserts and ask who they would recommend you go to for shoes.

Compression socks.  Here again, go to a professional.  Try your local medical supply store or scrub store.  These too need to be fitted.  A thicker sock over these helps too.

Make sure to take the inserts, compression socks, and regular socks to the shoe store for your fitting.

Have at lease 3 pairs in order to rotate them.  Yesterday's, today's, and tomorrow's.  Allowing time for your shoes to air out and recover saves your feet and the shoes too.

Lastly, move.  Standing still all day is probably the worst thing to do for your feet.  Rock back and forth, heal to toe multiple times daily.  Lean sideways, back and forth.  Stretch your feet.  These are things you can do while standing in front of a computer all day.

edit - I'm an overweight, 21 year CPhT.  Very, very rarely do I need to break out the Aleve for my feet or back.
[ip6dgwu] (score 33, diepte 0) Wear good shoes with custom, DPM fitted orthotics.
[ip7i4sw] (score 28, diepte 1) This is really the only way. I don't understand why retail hates their pharmacists and techs so much that they insist on making people work in the least ergonomic way possible. We are giving away our knees, feet, and health to these organizations that literally scorn us.
[ip7679j] (score 27, diepte 0) Sit on a stool while at verification, which is likely 70% of your workday.
[ip6ivuw] (score 22, diepte 1) Yes, and throw in some compression socks too! 
If you can elevate your feet after your shift that should help too. I don't work long days on my feet anymore but an adjustable bed with your legs elevated is amazing! 
An anti fatigue mat might help too if you aren't already using one.
[ip6y6hg] (score 17, diepte 0) Compression socks should be a required part of the work uniform in my opinion. Night & day difference in foot pain, muscle pain, and leg fatigue after a 12 hr shift.
[ip6pv4k] (score 16, diepte 0) ASICS for life
[ip717zc] (score 12, diepte 1) I second all of what tra-k said. It’s life changing! I was suffering from horrible plantar fasciitis along with Achilles tendinitis until I made those changes. I can stand 12 hours now without pain. It’s like I got new feet 😂
[ip8avik] (score 11, diepte 2) I have only one tech for most of the day, and alone for at least 2 hours a day. I don’t get a chance to sit on a stool. I’ll break it out sometimes, but invariably the exact moment my butt hits the stool I’m being called somewhere else. 

2 more years and I’m done with this bullshit.
[ip6ot6p] (score 9, diepte 0) Good shoes! Brooks Ghosts were a lifesaver for me.
[ip723c0] (score 8, diepte 0) Compression socks and a better pair of shoes. Danko's, Clarks, Skechers, Crocs, whatever works for you. May take several trial pairs to find the one for you.
[ip72qak] (score 8, diepte 0) Compression socks and my on clouds, I have hokas too but I find my feet hurt more with hokas
[ip6yzto] (score 7, diepte 0) Worked 10 hr midnights. Getting off at 0800 i would limp to my car.
Bought sketchers and added good insoles problem totally gone. I suffer from wide, high arch feet.
[ip9a772] (score 7, diepte 0) Agree with properly fitted shoes, insoles etc. I wear new balance sneakers which are one of the few brands that come on extra wide and have a high drop heel which relieves pressure on my Achilles. However, I’ll be honest, I have plantar fasciitis in both feet, severe Achilles tendinitis in one foot, I spent 6 months in PT and did all the supportive shoe things, stretching, strengthening etc but still could barely walk after a 13 hr shift. The only thing that has helped is sitting during my shifts which for me meant finding a different job unfortunately 😕 Standing in the same place for 13 hours just isn’t something our bodies were designed to do.
[ip6vxz7] (score 6, diepte 1 OP) 👍
[ip9504v] (score 5, diepte 3) Let them. If it's not this it'll be something else. A retail pharmacy just isn't worth your health.
[ip8cwpl] (score 4, diepte 2) Soles for me. The tops of my feet rarely hurt.
[ip6uc9c] (score 4, diepte 0) I bought shoes that don't make my feet feel like they're about to fall off. I also wear compression socks every shift.
[ip7czmz] (score 4, diepte 0) This seems so unpopular but I bring my own stool to QT and QV1 especially in the morning. I also have on compression socks and a a few good pair of sneakers I have on rotation.
[ip8anjm] (score 3, diepte 1) Do you put them on the soles or tops?  I tried it once on my arch and I didn’t feel a thing, I thought maybe my skin was too thick in my feet
[ip6wtd1] (score 3, diepte 0) Fire like in a hot sensation or pain?

If it's the former then it might be athletes foot or another type of fungal infection
[ip8vg2u] (score 3, diepte 3) Congrats 🎉🎉🎉

Sorry it has to end this way
[ip928fl] (score 3, diepte 2) customers complain when they see us sitting down 😒 they think it equates to being lazy
[ipadliy] (score 3, diepte 3) Have you heard customers say that? I've heard management say that customers would have that perception, but I've never heard it expressed directly by customers. I'm in a hospital job in which I can sit ~30% of the time now. My legs are still smashed by the end of the day but it's a lot better than community pharmacy days.
[ip7el0b] (score 3, diepte 0) If your feet feel like fire, be sure your Glucose is at a good level. Possibly get your A1C levels checked OR it could be from standing all day. 
(Type of shoe that works for your feet may be the answer) For me. It’s all about the right shoe.
[ip7gkbh] (score 3, diepte 0) Lol all of these posts about inspector gadget shit like shoes and compression stockings. The only thing that worked for me was actually sitting down on the 10-14 hour shifts.
[ip7n7gi] (score 3, diepte 0) Grab you a pair of hoka bondi’s
[ipafe4w] (score 2, diepte 1) Thats literally what I just put on my feet like 15 mins ago! Hahaha
[ip7mxj5] (score 2, diepte 1 OP) >0% of your workda

Can you recommend a good brand for insoles?
[ipd2vej] (score 2, diepte 1) I bought a pair of Danskos based on my wife's suggestions.  They worked like a miracle and well worth the investment.  My thigh/upper leg numbness went completely away.  A neurologist found nothing wrong with my leg....
[ip8b8kl] (score 2, diepte 1) Hokas have been the only shoes that have worked even somewhat for me. They’re a little tight around the heels though and I start getting callouses if I work too much.
[ipa5fkl] (score 2, diepte 3) When people say things like this to me, I throw it right back at them (with a smile). “Did you get to sit down at any point during your workday today?” I also like “I try to eat/pee at least once during my 12-hour shift” if they bitch that they had to wait five minutes 🙃
[ip7a120] (score 2, diepte 0) Get soft pads
[ip92ok7] (score 2, diepte 1) Well if they don't let you sit down you got to use other means
[ip97n6m] (score 2, diepte 2) As a guy with 15 years of standing for 14 hours a day, it was the biggest difference maker, and honestly without my hoka's and orthodics. I can't walk any sort of distance anymore. Ankles with start hurting within a couple hundred yards. I picked them up upon my physical therapist and orthopedist's recommendation. I looked down, and they we both wearing them (they don't work together, two separate offices). If they trust it, why shouldn't I?  It made a huge difference on feet pain, but the custom orthodics they fit me for made a huge difference on ankle pain as I have super flat feet.
[ip7n8h1] (score 2, diepte 0) Haven't seen it mentioned, but shave the calluses down on the soles of your feet. Or get a pedicure. Excess callus build up on the bottom of feet can cause burning like pain.
[ip8an7m] (score 2, diepte 0) If you can get a Dr to write you a note, the reasonable accommodation department will hook you up with a stool, headset, monitor arm etc.
[ip8m7tk] (score 2, diepte 0) When you find a good pair of shoes: buy two. Half way through your shift change shoes. No joke. It helps!
[ip9lwlc] (score 2, diepte 0) Hoka shoes! Changed my life! Went from knee problem and sore feet to feeling like a new person.
[ipb4zll] (score 2, diepte 2) Which Hokas? I love the Bondi but I’ve also had good experiences with the Clifton. The Bondi has more cushion, however. They are a game changer.
[ipafkbs] (score 2, diepte 0) Get a stool to sit on
[ipge97f] (score 2, diepte 0) [Alegria](https://alegriashoes.com/) shoes changed my life. My feet would hurt so bad at the end of my 14 - 16 hour days in an independent retail pharmacy (working alone) that it would hurt for the sheets to touch them when I finally crawled into bed. It takes a bit of time for your feet to acclimate, but it's worth the wait.

As others have mentioned, diclofenac gel and also lidocaine ointment.
[ipacr8f] (score 1, diepte 3) I never heard of this.  You apply it to soles of feet at night? Then put socks on ?
[ipabjn7] (score 1, diepte 1) A little off label use there I see what you’re doing 😉😉😉
[ip9n06c] (score 1, diepte 1) I love my Brooks. I have had them for two years now and they still have awesome support.
[ipa9kqn] (score 1, diepte 1) 1000x
[ipb595j] (score 1, diepte 2) Asics Noosa Tri. Best shoe out there. Adidas Swift Run also lighter than air.
[ip9jus2] (score 1, diepte 1) best shoes?
[ip9jzoj] (score 1, diepte 2) I wear Kuru. Barely have to break em in.
[ipg7606] (score 1, diepte 1) Yep. If your employer doesn't provide compression socks, or the special shoes or inserts you need, get a podiatrist to prescribe them, and don't forget to take them off your taxes.
[ip8s051] (score 1, diepte 2) Ive used scholls of the rack primarily.  One of my best tech friends had 500$ insoles made did not work any better then retail insoles.
[ip7nble] (score 1, diepte 1 OP) Maybe they don't provide enough structure and support.
[ipagbv8] (score 1, diepte 4) I’ve heard other pharmacy workers tell me that, I think in a store survey a customer complained about it. But I don’t sit at the pharmacy so I never heard it directly towards myself.
[ipf6q4k] (score 1, diepte 2) >We are giving away our knees, feet, and health to these organizations that literally scorn us.

Can you imagine what it's like in minimum wage jobs?!
[ip7ndb6] (score 1, diepte 1 OP) Can you recommend any?
[ip7e3i9] (score 1, diepte 0) Compression socks, properly fitted shoes and diclofenac gel.
[ip92jk1] (score 1, diepte 1) literally the best shoe i’ve owned, I have wide feet too so it’s hard to get nice shoes and they have a wide variation that helps a lot!

typically My feet with other shoes will hurt after walking or hiking for an hour bc i have probably the flattest feet possible and wide feet but these, i hiked for 2 hours and walked for 3 hours and had 0 pain
[ipc17b4] (score 1, diepte 3 OP) I haven't tried custom orthotics because of the price. Several hundred dollars are too much for me. Have you by any chance tried [cushifix](https://cushifix.com) insoles? Looking for someone who can tell me if they are good or not.
[ipc8so4] (score 1, diepte 4) I’ve tried many otc insoles (some help for heel pain) but most were ok at best. Then I tried the plastic ones that you can get custom fitted for at a shoe store. They were hard and uncomfortable. I haven’t tried the one you mention. But my orthopedist said I can try these custom orthotics they make at the Tulane institute of sports medicine (they treat nfl players there) or option 2 is get my ankles fused. I opted for the orthotics. They mold your feet and follow the rx for what the dr wants. And build the orthotic on the computer, lift where it needs to be done, use various densities of what ever foam it’s made of. And once it’s made they fit it to your shoe. A little stiff at first, probably want to use a half size larger shoe to fit comfortably. But the way it corrected my ankle geometry, the ankle pain I was getting was gone. Only while wearing it, so if I go back to normal tennis shoes I’ll still have the pain
[ip85hv2] (score 1, diepte 0) Super feet insoles. Never looked back.
[ip89afb] (score 1, diepte 0) Lots of good tips here. I'd also recommend just changing your center of gravity. I stand too far back on my heels and I ended up with some really bad heel pain over the years. I'd recommend leaning forward to where you're on your balance is on the balls of you feet. Rotate as needed. That's usually enough for me to keep the pain away.
[ip8b2n5] (score 1, diepte 0) I used to work at a zoo and had to wear boots. I cannot stress how important a quality pair of shoes/boots are with custom gel inserts molded to your feet. Expensive? Yes, worth it YES. I walked on average 8 MILES per day in boots and my feet felt fine after getting quality footwear and insoles.
[ipc0mbr] (score 1, diepte 1 OP) >re than one good pair and switch them e

Have you by any chance tried [cushifix](https://cushifix.com) insoles? I'm trying to find out if they are good or not.
[ip8hu36] (score 1, diepte 0) I know this sounds silly but GOOD SHOES. Not clogs, not Nikes, good SUPPORTIVE tennis shoes. Most people don’t have enough support for their foot type. I personally love the hoka one one brand bc they are hi cushion and offer support options for both types of gates. It is also sometimes beneficial to have more than one good pair and switch them every/ every other day to allow the cushioning to rebound. This is not an ad or anything lol I just love my hokas and need them to work all day. It’s not going to completely end all pair and discomfort but it is a very important start
[ip8j49i] (score 1, diepte 0) Wear better shoes I like skechers
[ip8rd5u] (score 1, diepte 0) Memory foam insoles? And 
Knee braces
[ipc0axz] (score 1, diepte 1 OP) I think I need something that gives my foot stability and arch support. Someone mentioned [cushifix](https://cushifix.com) insoles have tried these?
[ipczdwa] (score 1, diepte 2) I think they’re very similar ideas but try and see what works for you
[ip8rked] (score 1, diepte 0) Inserts
[ipbzvjf] (score 1, diepte 1 OP) Someone mentioned these [cushifix](https://cushifix.com) in the chat, have you tried them?
[ipcqr6f] (score 1, diepte 2) My personal problem is I don't get much arch support and have like plantar fasciitis, so I especially need the arch bit. These are pretty similar to the ones I use: 

 Plantar Fasciitis 3/4 Length Insoles, High Arch Supports Orthotic Insoles, Men/Women, 1 Pair, Flat Feet, Over-Pronation, Heel Spur Pain Relief Shoe Inserts for Walking Running Sport https://a.co/d/fBiYigx

They're a stuff plastic piece that doesn't run the full shoe length (but they have those too) and it just slips in under whatever insert your shoes normally have from the manufacturer. They've helped me immensely and I notice a difference if I walks round at home without shoes for a while because after a couple hours the arch of my foot is killing me to where I'd have to walk on the outside of my foot otherwise. So I often wear them at home for comfort, too. I highly recommended them if you need the arch support.
[ip8w84w] (score 1, diepte 0) Adidas ultraboost. One of the few pairs of shoes I’ve had that I can wear all day without my feet hurting
[ip915oz] (score 1, diepte 0) I went to PT. They told me to get new shoes based on my feet and ankles. I have hyper mobile joints and flat feet. Got myself a pair of brooks with arch support and a heel that isn’t flexible. My feet and ankles have never been so good. 

If you’re having issues, highly recommend getting a referral to PT for you specific recommendations
[ipbzo3v] (score 1, diepte 1 OP) >vere Achilles tendinitis

That's so true, we are not meant to stand in one place for hours! 

Is your foot pain now completely gone or do you still deal with it?
[ipchha5] (score 1, diepte 2) I still deal with it, but I’d say it’s about 90% better and I usually only have issues if I overdo it, wear bad shoes(no flip flops/flats/heels etc), or pick up the occasionally retail shift(full time hospital now, per diem retail) 😆 I could probably clear it up more by avoiding those things and being more diligent with my PT exercises. 

I was a competitive Irish dancer for 16 years before starting pharmacy school so I can’t blame pharmacy entirely for my foot problems but it made them considerably worse. Switching from retail I went from barely being able to walk for most of the day to being back in dance classes three days a week as an adult. Switching jobs obviously isn’t a feasible option for everyone but I think it’s bullshit that retail pharmacist can’t have actual chairs and the chance to sit during the day.
[ip9b3th] (score 1, diepte 0) Sorry you have to deal with mean people all day.
[ipbzcq3] (score 1, diepte 1 OP) 🙌🏻 Luckily we have some nice customers too :-)
[ip9b4gg] (score 1, diepte 0) Go to a running shoe store and get fitted for the right pair of shoes. I am in a different profession, but on my feet most of the day, getting the right shoes was one of the best things that I ever did. I currently wear black leather Brooks addiction walkers. They look quite professional.
[ip9fx2x] (score 1, diepte 0) Soak them in Epsom Salts and warm/hot water.
(19 reacties met lagere score weggelaten)

=== THREAD rp05ja ===
SUBREDDIT: r/pharmacy
DATUM: 2021-12-26  SCORE: 83  REACTIES: 101
TITEL: Shoes for long hours of standing
POST (source_id=post):
Can you help me choose good brand of  sneakers for long hours of standing? 

I like sneakers with memory foam, not with stiff insoles. I tried many skechers before, but the insoles/foam tend to disappear few weeks later. Brookes 13 wasn't comfy. 


Also what other advice you can give ne that help with long hours of standing? 

Location is US and I am overweight 165lb if it matters. 

Thank you!


Edit  I am roaming shoes stores right now checking your recommendations. Also i am going to order some insoles! 

Thank you all!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hq1er5d] (score 84, diepte 0) Adidas ultraboost. I used to have so much heel pain until I switched to those.
[hq1erns] (score 39, diepte 0) I work in an IV room at my hospital and stand all day. I have Hokas. I got them when I was at retail as well and just kept them up here. About two years in. Plus half of our hospital wears them. I also have a pair of ASICS for non work use that are thick and comfy.
[hq1r9dg] (score 25, diepte 1) Thread over along with the other million times. Adidas ultraboost + compression socks by sockwell is the best combo. You’ll never change.
[hq1ekd2] (score 20, diepte 0) high end asics with podiatrist insole...i wear cumulus or nimbus because I don't pronate
[hq1l4dc] (score 15, diepte 2) They're like the thickest sole on the market
[hq1jhl8] (score 15, diepte 1) My Hokas were honestly life changing.

Now that I've tried them I don't think I'll ever be able to settle for lesser shoes.
[hq23x2n] (score 15, diepte 0) Dansko has the best long term support of any shoe I’ve worn. Did wonders when I used to work standing up all day.
[hq1u83b] (score 14, diepte 0) I know you say you don’t like stiff insoles but in my experience they prevent pain so much better than memory foam. The memory foam feels great when you first stand up in them but doesn’t give your feet the support they need to actually last the whole day. The stiff insoles don’t feel like anything special when you first stand up but they actually support your feet all day and prevent pain. I have a great pair of stiff insoles (ABEO) and I can put them in almost any shoe and be fine all day.

For non-shoe things that help, the more you can move throughout the day the better. I go up on my toes, prop a foot up against the counter, squat to grab something off a low shelf instead of bending over, stand with my feet turned out for a while, etc. Standing in one place with your feet in one position all day just kills you. Compression stockings are helpful but are more helpful if you’re having trouble with swelling I think. This is semi-shoe related but if you have multiple pairs of different shoes (not multiple pairs of the same shoe) and switch each day I think that helps as well, especially if you’re on a long streak with no days off.

I also was overweight and when I started working out and losing weight TBH I did notice a big difference. Partially the weight loss (less pounds my feet have to hold up lol) but I think a big part too was that I built a ton of muscle in my core and legs. I think building the muscle and increasing muscle tone helps support my body as well and I’m not just dumping all my weight into my feet. Kinda like how if you pick up a kid who doesn’t want to be picked up and goes dead weight they feel so much heavier than picking up that same kid with their regular muscle engagement.

Sorry for the novel! I used to have a ton of trouble with foot pain so I’ve thought about it a lot/tried a ton of expensive shoes. The most helpful things to me were stiff insoles, exercise, and moving/shifting as much as I can during my shift.
[hq1ug0n] (score 11, diepte 3) I could see why people wouldn’t like the tight sock feel of them. I haven’t had an issue with feet swelling since rotating between 3 pairs of compression socks, so it is a little hard to relate. I don’t think there is a shoe out there that helps if you get that bad of feet swelling. At some point you deserve to sit down in a chair to be off your feet for a second. If you’re retail and your higher ups won’t let you have one, get a doctor on board and get a note stating you need a stool. Your feet health is so important. Don’t let them destroy you.
[hq1kx0c] (score 11, diepte 2) Stiff insoles doesn’t sound like Hokas? I came here to recommend them as well. Hokas with compression socks = life changer.
[hq1tm28] (score 11, diepte 0) I wear leather dress shoes with "super feet" inserts, makes all the difference, no pain even after 5x11 hour shifts. I try to at least look like a doctor even if I dont feel like one when I go into the bathroom at walgreens and someones smoking meth in the stall.
[hq1e1kg] (score 10, diepte 0) Hokas
[hq1j0y9] (score 10, diepte 0) New Balance and try the Brooks 21.  One of the issues with memory foam insoles is the foam will break down quickly.  Another drawback is if you have a problem with your feet, memory foam will will not help to correct this problem.  Which will not help you.  Go to a shoe store that scans and measures your feet.  They will be able to see the problem areas you have and make personalized recommendations.  It may be you will have to ditch the memory foam and get use to stiffer insoles to help solve any issues you have.  Another possible answer is to wear compression stockings.  These are also best to have measured.  Go to a health care uniform store.  They have experienced people to help and usually a great selection.
[hq1s58e] (score 8, diepte 2) I tried the Adidas but that stupid sock inside it is also tight if your feet swell, and on top of socks, it's terrible, unless I need to go a size up.
[hq1fxo0] (score 7, diepte 1 OP) Yeah a lot of my coworkers wear them and recommend them.  but I tried hoka at the store, I liked that they were wide and roomy but  didn't like the stiff insoles. The store staff said hoka doesn't come with memory foam 😔
[hq1f4iq] (score 6, diepte 1 OP) Do you recommend certain insoles? I tried scholls machine and the recommend insoles were not great
[hq1se1r] (score 6, diepte 0) Hoka would be my brand recommendation.

I have arthritis in my feet and Hokas, combined with my custom orthotics have been a lifesaver. 

https://www.hoka.com

If you stand in one spot a lot, an anti-fatigue mat will help as well.
[hq26wlf] (score 6, diepte 1) I’ll second danskos
[hq1jm10] (score 5, diepte 0) I wear what I hike in, which is Altra Lone Peaks. 12 hr shifts no problem.
[hq1vqn3] (score 5, diepte 1) ahh the spicy cloud
[hq2tdi9] (score 5, diepte 0) I wear allbirds + compression socks! Makes all the difference—my feet used to hurt so badly as a student on rotations when I wore Nikes and regular socks :(
[hq1j9es] (score 4, diepte 2) My podiatrist put me with Orange insoles, especially because I had a foot injury while starting the pharmacy job. 
They're not memory foam because I need the actual support (versus just sinking in the foam), but they're pretty flexible and cushy
[hq3f9mr] (score 4, diepte 5) Real talk, work slow downs are legit warranted until stools are allowed and provided
[hq3ipg5] (score 4, diepte 1) Also love the dansko. It takes a little bit to get used to the harder insole but they last. Also no matter what shoe you choose, expect to replace it every 6-9 months of you are working full time. 

Also compression socks help a ton
[hq2yh4y] (score 4, diepte 0) As long as youre ok with looking stupid... crocs. Not the regular ones they make workplace ones too. They look awful but oh man they are SO nice to stand in for 10+ hour long shifts.
[hq2y44a] (score 3, diepte 2) Get Adidas Ultraboosts then. They have added more and more foam to the newer model years and the 21' is considered one of the most cushioned compared to similar shoes (Max Cushion running shoes).

I personally think the 19's have the best balance of springiness and cushioning. I like my 20's for when I want an extra squishy cushioned step, but I default to the 19's for the support.

The Boost foam actually provides some support unlike memory foam that just compresses down without meaningful springback.
[hq2ysp1] (score 3, diepte 2) I think you’re treating memory foam insoles as a band-aid for sore feet, where the cure would be to train your feet to be more comfortable on harder surfaces. I used to have sore feet too, but switched to flat shoes with thin soles and never have issues now. I like Olukai and Allbirds. Things like Converse (may not be dressy enough though) Altra and Uggs would all be good too.

The other trick is to switch shoes halfway through the day - kinda resets your feet!

Wouldn’t it be better to not need special insoles and be comfortable than to need special insoles and still have sore feet anyway?
[hq1jmpp] (score 3, diepte 1) These.
[hq2vb9d] (score 3, diepte 4) yeeesss I thought I could stop my aching feet and the start of a varicose vein by using compression stockings, but it turns out that old fashioned sitting down works best. Never tough it out!
[hq1uzi5] (score 3, diepte 3) It’s for this exact reason I ended up switching to Yeezy boost 380. Looser, but still plenty of boost.
[hq6ao9l] (score 3, diepte 1) Wouldn’t recommend this if you’re a pharmacist and you stand around checking. It kills you slowly as your feet sink into the boost.

If you’re a tech or in a role where you’re on the move, then Ultraboosts are unmatched, specially the ones before the UB 19s.
[hq21mrh] (score 3, diepte 1) I've also heard great things about Hoka. People have told me that Hoka are awesome if you have to walk a lot, but Brooks beat them out if you have to stand a lot. Gf just got me a pair of Brooks for Christmas and I can't wait to try them.
[hq1heew] (score 3, diepte 0) On running
[hq1k58y] (score 3, diepte 1 OP) I went to shoe fitting store. They measured everything and chose the shoes. I felt it was a little bit rushed and didn't help that much. They didn't provide much info.  they also said that it doesn't matter if it has memory foam or not. The girl was very young so may be she didn't have enough experience?  i might have to try another store.
[hq1s3oe] (score 3, diepte 2) Try a runner's store since athletic shoes generally are the best for pharmacy work.  An orthotics store is a good choice also.  Another option you can try is rotating your shoes.  I've have 3 pairs I rotate every day.  You could try this with less expensive or expensive shoes.  By rotating the shoes you allow time for them bounce back, air out, and they last longer.  You also want to choose shoes with a wide toe box, if you don't have a rather narrow foot. Choose shoes that lace up so you can loosen the laces during the day as your feet swell.  The shoes with elastic do not allow for you to make adjustments.  Another idea is to check out the various ways to lace the shoes.  Runners have developed myriad of lacing designs to help them run in shoes for marathons.
[hq1uq7q] (score 3, diepte 3) I also found, over the years, that changing shoes mid-day gave me a boost...would change the compression socks too, if I had the time, and wipe my feet with a 'baby wipe'.  It's a nice little self-care break; I'd return to the floor with a 'jump in my step'!
[hq1qr8n] (score 3, diepte 0) Atoms. Used to need insoles but have been very comfortable standing for ten hours since getting them.
[hq1xnh2] (score 3, diepte 0) I am an avid lover of ultraboosts but ASICS offers 50% off for certain medical professionals when you confirm your status with sheer I’d. I purchased the gel
Nimbus 23 and they are so comfortable they are cushiony and almost form to your foot. They aren’t stiff I wear them all day every day and have no
Issues and they are probably the most comfortable shoes I’ve worn.
[hq3wv4m] (score 3, diepte 1) I couldn't get used to the clog type Danskos, but they make a ballet flat with about a 1/2 inch heel that is amazing. Haven't had foot pain since I switched. 

I bought like 6 pairs when the walking company had them on sale for $50
[hq2blv4] (score 3, diepte 0) I'm surprised that no one has mentioned **SOCKS**!!


I've found the "Darn Tough" brand of socks that you can buy on Amazon to be some of the best socks for standing all day. Even with the best shoe and insole, these socks make a noticeable difference. They aren't cheap ($25/pair) as they were first marketed to runners to give them a little more cushion. Since then they have come out with some that are more appropriate for office use.


Now, here is the kicker on the price: **They have a lifetime warranty!** Check out the user ratings for them at Amazon.
[hq2p8jd] (score 3, diepte 0) I’ve just come in here to throw in the Nike Pegasus. 

Many Nikes are trash, but the Pegasus is a true running shoe, very soft. It is not for overpronators. But for those with a neutral stance or a bowing out stance/underpronator/supinator (like me), Nike Pegasus is an amazing thing.
[hq35ntw] (score 3, diepte 0) Saucony. I use my Perigrine 10’s which are meant for trail running. Super comfortable with ample cushioning to handle rocky trails and pharmacy floors alike lol.
[hq1niaq] (score 2, diepte 2) I always wore superfeet brand the green ones until I got pregnant and went to the podiatrist for custom ones... also I replace my shoes about every 6 months
[hxbx0iq] (score 2, diepte 4) Do they fit true to size for you? I wear 10 in ultra boost but 9.5 in most other shoes just curious what u think size wise
[hq3g99i] (score 2, diepte 1) This. I needed a new pair of shoes and decided to try brooks this time instead of ultra boosts. I have so much more heel pain that it’s about to justify buying another new pair of sneakers
[hq477k2] (score 2, diepte 1) I love my ultraboosts! Does anyone know how they compare to Hoka? Thinking of getting some to rotate
[hq1kd31] (score 2, diepte 1) This, Merrek Moabs for me.
[hq22b32] (score 2, diepte 0) Hokas are what pretty much everyone in my hospital wears. I’ve always worn my yeezys and they have been great.
[hq24r79] (score 2, diepte 0) Hoka Clifton
[hq26srb] (score 2, diepte 0) I wear adidas ultraboosts with dr schols custom orthotics (440 model) with compression stockings.
[hq550ig] (score 2, diepte 1) That's the holy trinity
[hq2b2hj] (score 2, diepte 0) Not a pharmacist, but listen: Dansko clogs.  I know of nothing comparable.
https://www.dansko.com
[hq54xns] (score 2, diepte 1) Yes
[hq2ffqz] (score 2, diepte 0) Ultra boosts. Hands down.
[hq2fhi0] (score 2, diepte 0) I wear nursemates, my favorite being the align series. They're only about $90 but you can catch them on sale for $50-$60 sometimes which is when I spring for them. They typically last me about eight to fourteen months before they start to show signs of needing to be replaced, which is usually that my knees start hurting on the days I wear the oldest ones. 

I actually need to replace a pair now, but lots of people in here recommending Hoka so maybe I'll give them a go this time.

The thing that keep my feet from hurting aside from these shoes, though, are compression stockings. My feet are always sore no matter my shoes if I don't wear them for my 13-hr shifts.
[hqcv8kl] (score 2, diepte 2) SC, i wish they would here, but that would screw us over staff wise since most stores would need another pharmacist to help cover some shifts, and my district only has 4 floaters for like 13 stores.
[hq2r30h] (score 2, diepte 0) My advice is to rotate your shoes
I use ASICS, and chuck Taylor's and as gross as it is, there were days I'd find it amazing to run in only my socks. 
Everyone's feet are different from arches to width. My foot dr said go after your shift, when your feet are the most swollen and do a proper fitting.
[hq34agq] (score 2, diepte 0) Haflinger clogs are great. Especially if you have problems with Plantar fasciitis.
[hq34xp1] (score 2, diepte 0) On Cloudflow shoes. Probably the most comfortable pair of shoes I’ve ever worn.
[hqc9ufl] (score 2, diepte 1) Looove Saucony. I just bought a new pair, Axon in Blaze/Royal. They are snazzin.
[hq36tyo] (score 2, diepte 0) I got a pair of Skechers with the memory foam soles and damnnnnn they are good
[hq3qqda] (score 2, diepte 0) I have been wearing Kuru for the last year and they are the best
[hq5q6fk] (score 2, diepte 0) Pick 2 different types and alternate them by shift. Sometimes I even changed mine mid shift
[hxc70ca] (score 1, diepte 5) UB21 was a bit tighter, but the 380s were not loose enough for me to size down. Only a smidge less tight! I still recommend same size as UB.
[hq1s3lx] (score 1, diepte 1) Totally agree about foam. The orthotic inserts are very stiff (made too order for YOUR feet) and are awesome.
[hq1r5ww] (score 1, diepte 0) Danner boots
I rotate between my boots, Nike huaraches, and air max. I switch shoes daily.
[hq1rchc] (score 1, diepte 0) Anyone have experience with Nike ZoomX Invincible shoes? and if I am choosing hokas, which one should I buy?
[hq55j5x] (score 1, diepte 1) What. This is terrible
[hqcacqe] (score 1, diepte 1) This sounds astoundingly like retail pharmacy hell. Either way, God Bless.
[hq1ykbn] (score 1, diepte 0) Not shoes but balega blister resist socks have pretty good padding that can act like memory foam insoles
[hqc9ehk] (score 1, diepte 2) Fourth 👍🏻 for the Danskos. I bought my first pair over 5 years ago after I got my dream job, and they are still brand-new looking. Definitely the best shoe I've ever gotten for the money. I'm also a huge fan of any/all of the Skechers Max Cushion kicks. They feel like I'm standing on a very sturdy marshmallow. I have freakishly high arches and these two shoes have been winners for me.
[hqda1tm] (score 1, diepte 1) YES, a must have.
[hq24nif] (score 1, diepte 0) I love my cheapo Dr. Scholl's, they're still in great shape after almost half a year. Got rid of all my heel pain
[hq4uo0t] (score 1, diepte 1) These hurt my feet so much I was crying when I got home that night.  The bottom back of my heel hurt for weeks after. It almost felt like a hammer had been taken to the back of my heel.  I love the look but gave them away because they were trash for me.  I now wear puma with stiff insoles.  They aren’t the best but worlds apart from the pain from Hoka   I had been wearing dress shoes with wedge heel. I wore them for 15 years with no issue and Walgreens management forced me to stop wearing them bc they had a peep toe.  Never been the same since.
[hq2m8aj] (score 1, diepte 0) The softest soles with the thickest memory foam I’ve found are Pumas, but beware they run narrow.
[hq2obgm] (score 1, diepte 0) New Balance 990 v5 or Brooks Beast 20.  Im a 13d normally and wear that for the 990s but found I needed a 14 with the Brooks.  I switch between the different pairs every couple of days and find that helps too.
[hq2p12p] (score 1, diepte 0) I wear docs with dr scholls custom orthotics. Best decision of my life. I shit you not, after 8 hours of standing I have no pain. I too am overweight
[hq2pze3] (score 1, diepte 0) I wear vionics! They have worked really well for me and I work 13 hour shifts!
[hqca1mj] (score 1, diepte 1) Where are 13-hour shifts still legal? I've done my share of 12's but California put a stop to that some time ago.
[hqhhxrk] (score 1, diepte 3) God bless. I did retail for almost 14 years. That's apparently how long it took to fully remove my soul.
(25 reacties met lagere score weggelaten)

