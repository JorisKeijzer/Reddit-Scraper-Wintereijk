# Label-batch batch_0149

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
Schrijf het resultaat naar `batch_0149.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1k1jrjf, 1p1gz92, yjjffg, 11hot78).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1k1jrjf ===
SUBREDDIT: r/walking
DATUM: 2025-04-17  SCORE: 27  REACTIES: 62
TITEL: Plantar Fasciitis
POST (source_id=post):
I’m an avid walker, but have had plantar fasciitis for about 18 months. I’ve done everything I can for it- doctor, physio, been through multiple shoes, but nothing has helped. I’m currently wearing OOFOS shoes and pushing through the pain because I love to walk and be mobile but this is hindering my walking. Has any walkers ever had this ongoing issue? And what did you do to fix it? Any walking shoes that are better than I’m wearing now?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mnmot98] (score 19, diepte 0) I’m dealing with plantar fasciitis right now and what helps is working on ankle mobility by doing calf stretches and foam rolling the calf, as well as doing heel raises.
[mnmoi2b] (score 8, diepte 0) Have you tried a cortisone injection?
And for instant relief- roll your foot over frozen water bottle- it’s free and wonderful. 
I hope you find comfort. I fully understand your pain and frustration.
[mnmpipb] (score 7, diepte 0) I cured mine by being barefoot on the grass. I started out walking then lightly jogging. It has never returned.
[mnmn8k1] (score 5, diepte 0) REST. Don’t walk through the discomfort. Take a few days off and do something for the inflammation. Find other ways to be active, like a stationary bike or focusing on arms/abs. 
 
Have you been doing strengthening exercises? One of my favorites for PF is to stand on a small towel or bathmat and scrunch the mat with just my toes. And I got high arch support insoles (I use the superfeet greens). But rest is important for you now if you’re experiencing PF daily.
[mnnvcfs] (score 5, diepte 1) I cured mine by never going barefoot. Lol. Glad your cure worked for you and mine worked for me.
[mnnc7sv] (score 5, diepte 0) Get a massage gun and massage your feet and calves morning and night.  It was life changing for me.  Same benefit as going to PT for myo-fascia release but 2x a day instead of 2x a week.  I was considering surgery when I tried this…
[mnmupbp] (score 4, diepte 1) The cortisone shot was the only thing that helped me.
[mnmsq36] (score 4, diepte 1) I second calf stretches, those muscles are connected all the way down to your feet so limbering them up will help
[mnnxl24] (score 4, diepte 1) When I had it, my doctor also told me to never walk barefoot. I basically walked on my tippy-toes all the time or wore shoes inside.
[mnnx9k0] (score 4, diepte 0) I've been able to help \~ 9/10 of my patients with PF by prescribing diligent foam rolling on the calves. Find the tender points, stay on them, breathe. It's invaluable in treatment of PF. Acupuncture also helps.
[mnmt36t] (score 3, diepte 0) I had pretty bad plantar fascitis in 2023. To the point that walking sometimes brought me to tears. It took me over a year to get rid of. I still have a little in my left foot but it's like 95% gone now and just a residual ache that flares up from time to time. The two things that helped me the most were a lot of rest of the winter (probably not applicable now but I wanted to mention it) and wrapping my feet with ace bandages. Wrap them LOOSE, not tight at all, but keep them wrapped all the time unless you're in the shower or sleeping. Wake up, wrap them before you take a single step out of bed, and wear throughout the day. Yes, it was pretty annoying and fiddly but within just three days of constant loose wrapping i started to feel a difference. The key is not tight at all, like a loose sock. 

Cutting back on salty food and drinking lots of water also helped but that's just general advice. If you can't rest 'em, wrap 'em
[mnny1bf] (score 3, diepte 1) The cream of the crop for plantar is the (green SuperFeet)\[https://a.co/d/dd7qQYT\]. They're expensive, but MAN they have kept mine at bay for years. I always have a pair in my walking/running shoes!
[mnmxqob] (score 3, diepte 0) Night splints help a lot. The only thing that fixed it was a cortisone shot.
[mnn3z3g] (score 3, diepte 0) I’m a runner, and doing heel raises fixed it for me  after a couple of weeks
[mnn7iab] (score 3, diepte 0) I recently had one too. I took a break for a month. Gave my right foot a well deserved rest. Also, what helped me was a taping tutorial by BestFootDoc - Plantar Fasciitis Taping. I felt instant relief. After 1week of taping no more pain. Just make sure that you give your feet a rest for best and fast result.
[mnmt2xm] (score 2, diepte 1) This. I wound up having to rest and wear a medical boot to minimize how much weight I was putting my foot for mine to finally go away.
[mnow24n] (score 2, diepte 2) This. With hardwood floors to boot (no pun), its orthofeet inside at all times!
[mnpcpjr] (score 2, diepte 1) asian/sumo squats healed my 5 year PF
[mnmtzt4] (score 2, diepte 0) Yes. I had a similar issue in 2020. Did PT, did the frozen water bottle thing, and so on. 

I had to drop walking and take up activities that didn’t put weight on my feet. I switched to biking & swimming for at least a year. I’m back to walking but yes, it was a long term obstacle.
[mnqipqs] (score 2, diepte 1) Idk what brand you saw at Ross, but I’ve had Superfeet insoles for many years and they’re great. They make it so I can walk. I’d highly recommend them.
[mnmua9p] (score 2, diepte 0) I have plantar fasciitis insoles that I get from Amazon.  I work from home so I wear them all day in my slippers.  I do not have to use them in my walking shoes any longer.  It rarely bothers now.
[mnqiegg] (score 2, diepte 2) I’ve had Superfeet insoles for many years (10+)and they keep me on my feet. I’d highly recommend them.
[mnop0ht] (score 2, diepte 1) My chriropractor (whom I resorted to after podiatrist didn't help much) used the stainless steel tools and the Graston technique on the fascia and it made a tremendous difference. It hurts a lot while he's scraping the fascia but it probably felt 50-60% better after the first time he did it and better every time after that. Rolled with the ice water bottle and rolled golf balls all under the foot as well periodically. Still do this when I feel it acting up. I bought one of the stainless steel fascia release/ massager tools on Amazon to do myself at home as well. You can google Graston technique on you tube for some examples ! It is used on many parts of the body on fascia adhesions! A physical therapist can do this as well, and I also have heard that dry needling helps. I had dry needling done for tennis elbow which also is very painful and it took care of it!
[mnnf9qx] (score 2, diepte 0) Oofahs highly recommend them for Plantar Fasciitis! Love my Oofas!
[mnnruod] (score 2, diepte 0) Compression socks, PT exercises and soaking my feet in magnesium flakes & hot water. Superfeet insoles.
[mnnsnpb] (score 2, diepte 0) I had to finally give up my beloved OOFOS shoes as they were much too soft and spongy. Now I am wearing New Balance 990s I believe. I have been dealing with PF off and on for 20 years. It is AWFUL. I have found rolling my feet on a frozen Coke bottle is super helpful, swimming (I know this is difficult for many) and riding the recumbent bike instead of walking has helped me tons. Definitely check out Brooks, Saconey, Hoka or NB shoes.
[mnozkno] (score 2, diepte 2) They did a fasciotomy
Basically, they just cut a little place on my foot and stretched the part that was causing the pain. I had to wear a boot for I want to say a couple of weeks. My doctor had said that most people don’t want to do the surgery because of the recovery.
[mnnxmch] (score 2, diepte 0) I have flat feet, and suffered horribly off and on for years.  Sometimes the pain was so bad I was essentially crippled.  I did exercises, iced, basic insoles etc. but nothing really helped long term.  Custom insoles from the podiatrist were way too expensive.  I eventually found a company called Upstep.com  (Google it) - they sent custom moulds to create custom orthotics which were not nearly as expensive as I expected.  I was sceptical but when I got the finished product, the pain was gone and has been ever since.  I'm wearing through them and will have to re-order soon but they have lasted around 2 years. I have no idea if this works for everybody but may be worth a try.
[mno80hf] (score 2, diepte 0) I cured my husband’s by really getting into the area of the foot it was in and breaking up the lump that had formed. It hurt him like heck but it worked. We have a chiro friend that said you basically had to just get into the muscle with your thumbs and work it out.
[mnohd8d] (score 2, diepte 0) I had it bad, tried so many different things  but what ended up working for me was yoga. Had done yoga in the past but had stopped, started it up again for totally different reasons than the fasciitis but after a few days realized it was better. Few months later and it was gone.
[mnr6n0p] (score 2, diepte 0) Vionics are the only shoes that helped me. My foot pain decreased about 50% the moment I put on my first pair. The first few weeks will cause pain in your lower body as they put your feet, ankles, and legs back into alignment. 

Barre workouts actually fixed my  PF. The first few weeks were extremely painful. I believe all the releve work (moves on tip toes) strengthen my feet. I had no idea that my feet could be pain-free again.
[mnnu4pd] (score 1, diepte 1 OP) That’s the next option for me
[mnnvqz7] (score 1, diepte 2) It gave me instant relief.  Do a bit of research. My doc won’t do more than 3 a year- it can weaken the fascia.
[mnqsgdo] (score 1, diepte 1) after maybe 3-4 injections over two years, my PF never returned. its been almost ten years. obviously just a one off case, but pretty amazing how it panned out.
[mnqnnvp] (score 1, diepte 1) My doctor told me stretching actually makes it worse
[mnmpafe] (score 1, diepte 0) Kuru brand shoes are the only ones that work for my husband. He's tried so many insoles but never had complete relief until he got those shoes.
[mnmu2yo] (score 1, diepte 0) On this topic, I recently saw some inserts at Ross. Do they really help?
[mnqd1ax] (score 1, diepte 2) +1 for Superfeet insoles... they instantly helped me with my PF and i have them in both my walking shoes and boots
[mnn25lk] (score 1, diepte 0) I had it from dancing. Tried everything and cortisone shot finally got rid of it.
[mnn5zoh] (score 1, diepte 0) I just saw the doctor for this. They recommended custom orthotics and if that wasn’t possible, power step shoe inserts. I am waiting on insurance for the custom orthotics, but got PowerSteps in the meantime and they have helped.
[mnn8mgt] (score 1, diepte 0) Ankle mobility
Calf/tib/soleus strength training 
Foot exercises, toe spacers <———
Compression socks

Shoe rotation… sneaks with higher, neutral, and lower to the ground. Heel to toe drop.  (Ex. higher (brooks glycerin) neutral saucony ride or hoka Clifton, lower, altra (Torins are good). Rotating allows for better balance, imo. You don’t a bunch, even two is good. 
Lower drop works ankle,foot,calf, shins more.
Higher is good for low leg relief, like feet calves & ankles but if you wear those too often it can place more emphasis on the hip flexors and knees. It also helps alleviate plantar fasciitis too. 

The OOFOS are great and I use mine in my house mainly as I had to work through metatarsalgia injury last year that was rough. But I use the slides not the shoes. 

Hope that helps- good luck to you!
[mnna6uz] (score 1, diepte 0) Rolling calves. Squat stretches. Super duper padded shoes. Staying far far away from zero drop footwear. No bare feet on hardwood floors at home. 
Currently wearing Asics Nimbus and Nike Vomero for walking. Pain is gone. 
For a more substantial treatment your doc can give you shots where it hurts.
[mnnc558] (score 1, diepte 0) Just dealt with my first ever bout of plantar fasciitis. What solved it for me was stretching out my calf and (I think more important) icing my heel and arch and the sides of my foot 2-3 times a day for 20-30 minutes. I also took some OTC pain reliever to try to cut the swelling.
[mnuieki] (score 1, diepte 1) Would a vibrator wand work for it as well?
[mnncuva] (score 1, diepte 0) 56 year active male with PF issues these past 2 years. I have worked through PT sessions, daily stretching and strengthening and(of course) choosing the right shoe. I wear brooks ghost 15 and they are awesome. Also, when hiking I use a walking shoe (not boot) that I find offers the support I need. 

Two years on, PF is certainly still there but it’s better. I’m off for a 5 day hike in 4 weeks time! 

Stretching, strengthening, correct shoe, resting… in that order.
[mnnjic0] (score 1, diepte 0) Ugh, yes! 7 days a week walker.  My plantar facilities has been hurting 6 months.

It has FINALLY subsided.

I went to the podiatrist and was referred for custom inserts. My arches collapse and pronate.

The inserts made it worse at first but I kept wearing them. 

I bought Archie's sandals for the house.  No walking without shoes.

I iced in the morning and after my walk. I stretched calves 2-3 times a day.  I used my massager every night before bed and then heated with the heating pad like 45 mins.

I'm honestly surprised it has subsided. I thought it never would! 

I never stopped exercising.
[mnnulwl] (score 1, diepte 0) I tried PT, home exercise, night splints, and corticosteroid injections, but ultimately underwent fasciotomy on both feet, which gave me 100% relief on my right foot and about 80% relief on my left.
[mnnwflo] (score 1, diepte 0) After years of pain and shots I had surgery. So mad I wasted 2 years treating it instead of just having the surgery and boom it was fixed.
[mnotu2u] (score 1, diepte 1) What do they do in surgery that fixes it? Was never offered this option. Thanks!
[mnp4qzj] (score 1, diepte 3) Thanks for the reply. Plantar Fasciaitis is rough!!!
[mnnwtpp] (score 1, diepte 0) I had a fairly severe case last year. I took off about 10 weeks because the doctor said it would help. It didn't. He told me I should do calf exercises, but when he saw how much flexibility I had in them, he was a little stumped. I  tried a variety of shoes and different supports with no success. I tried toe separator socks 15 minutes at a time. That helped a little. I started wearing compression supports on my arch. It helped a lot but did not cure it. I hiked 20 miles in one day. It hurt so bad when I stopped I had to hop around on it all evening. Then ice it overnight. What fixed it for good is that I walked 44 miles in a day. I haven't suffered from any pain since. I do still always wear the compression sleeve, and I never go barefoot. I am convinced the 44 mile walk fixed it. Lol
[mnoua9a] (score 1, diepte 1) This sounds similar to my situation. My chiropractor worked it with the Graston technique tools (stainless steel and cream on the foot for smooth gliding) and I saw stars and thought I'd cry while he was doing it , but walked out of the very first visit with so much relief !!!
[mnp2sxt] (score 1, diepte 0) Go see a chiropractor that uses the graston technique. It’s not painless but it will get rid of PF.
[mnpa7bp] (score 1, diepte 0) I broke my other foot and it forced me to stay off both my feet. Do not recommend but it cured me 😆
[mnpffht] (score 1, diepte 0) Give your feet rest and take some antioxidants.

I had for a brief moment a very bad problem with plantar fasciitis. I could barely walk due to the pain and even massaging my feet was extremely painful.
I was able to revert it
[mnpwf4y] (score 1, diepte 0) Have you tried the PF stretch?
[mnqk95m] (score 1, diepte 0) I’ve had plantar fasciitis off and on since 2013. I never ever go barefoot and always have on a supportive shoe. Even in my house I have “house only” orthotic slippers. I also do a ton of calf and foot stretches before and after walking .
Hope you find comfort
[mnqozqw] (score 1, diepte 0) Rest is the only thing that worked for me.
[mnt3d3i] (score 1, diepte 1 OP) I took a few months off from walking in the winter, but unfortunately I can’t rest too much as my job requires me to be on my feet 5 days a week
[mns2uvi] (score 1, diepte 0) A nurse colleague says that acupuncture worked for her. One treatment and it never came back.
[mntux6e] (score 1, diepte 0) I bought ice socks on Amazon. They have little inserts for ice packs. I wear the green superfeet inserts, or keen shoes. Pf is a real bummer.
[mnu5xup] (score 1, diepte 0) Red light therapy, and wearing Birkenstocks nonstop…
[n0tlvb2] (score 1, diepte 0) I had pf for 8 years, from standing all day at work. Still remember the day I felt the initial tear. I tried acupuncture, shockwave therapy, chiropractic adjustments, deep tissue massage, and the Graston technique. I’d get some temporary relief but it always came back.

I remembered reading how dmso was used on horses and their muscle injuries and how it draws whatever it touches deep into the body, so I figured “why not?” I had some dmso w/magnesium on hand, so I combined it with penetrex (a muscle injury cream) and castor oil (good for inflammation and has healing properties).

The first time I used it I could feel it really getting in there; like it woke up old injured tissue and nerves. I applied it four times a day, 20 minutes at a time, for about a week. Wouldn’t you know if, I was completely healed.

2 years later and I’m still pain and pf free. I know of others who have tried it as well, with great success. Sometimes it takes longer than a week (someone I know did it for 2 weeks before they noticed results), so if you aren’t seeing much of a difference initially as I did, just keep at it.
[nx3zeqi] (score 1, diepte 0) Shoes help cushion the impact but they don't stop tight calves from dumping force into your heel with every step. Started stretching my calves with a CalfPRO before walks and the persistent pain finally started dropping after months of shoe-hopping. The missing piece wasn't another shoe, it was addressing what happens upstream.
[o4r1dns] (score 1, diepte 0) I walk and run too and I dealt with PF for almost two years. I stuck with regular running shoes and focused more on wearing PF socks and using a foam roller regularly. That combo didn't magically fix it but it helped me manage the pain enough to stay active without it getting worse.

=== THREAD 1p1gz92 ===
SUBREDDIT: r/rheumatoid
DATUM: 2025-11-19  SCORE: 18  REACTIES: 62
TITEL: best sneakers for arthritic feet
POST (source_id=post):
Hi all! My mom has had rheumatoid arthritis for about 20 years now, and sometimes her feet swell up. In addition to that, she's had to get surgeries on her knee and ankle due to unrelated issues. I want to get her a nice pair of sneakers that would be comfortable for everyday use and last awhile, but I don't really know what to get. I've been reading up on Brooks shoes, but I don't know which model would be best for her conditions. I also looked at Hokas and OnClouds, but I read that OnClouds wear out quickly and Hokas aren't wide feet friendly. My mom is the type to wear the same pair of sneakers to do everything, so I want something that will last her awhile. Any help would be appreciated!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nppvs9w] (score 12, diepte 0) I recently bought some men's wide Hokas-I'm a woman. Men's shoes seem to have a wider toebox, and I have bought several pairs of men's sneakers over the years.
[nptxw2g] (score 5, diepte 1) altra’s are exactly like hokas but with a wide toe box. i am a barefoot shoe guy and i remember when i used to wear hokas. i recommend altra’s instead because they can be found at a lot of shoe stores and are a healthier alternative to hokas. (hoka’s are too skinny and deform feet)
[npr0knr] (score 5, diepte 0) The thing with shoes is that everyone likes something different. What I find comfortable isn’t necessarily comfortable for others. So you should probably take your mom and have her try on multiple different shoes and have her choose. As you can see everyone here has different recommendations.
[nprjmxj] (score 5, diepte 0) Take your mom to a running shoe store, or get her gift certificate/card from there. The salesperson needs to see her feet, and how she walks. They want to check her pronation.

Expect to spend $100-180 per pair, but they will last so much longer, and much more comfortably! 

I have RA, and run a 7.5W - 8W. I could never wear Nikes, and have regular Asics that ended up being too small, but had luck with New Balance and Brooks in wides!
[npq1hwh] (score 4, diepte 0) I wear Altra Torin 7s (in mens b/c they are little wider) and find them very accommodating for when my feet swell. I also have constant pain my feet and ankles.
[npq6e1t] (score 4, diepte 0) I have been really happy with my Hokas
[npqbmxa] (score 4, diepte 0) New Balance Fresh Foam More. I suffer from RA and it's affected my feet. I've been wearing the NB Fresh Foams for about 3½ years now. Love them. 

Whatever you get, get them fitted correctly, preferably by a smaller store where the people know what they're doing, and what they're selling.

Gimre's Shoes on Main St. in downtown Hillsboro is great, they've got another store in Astoria too. They also give a 10% discount for seniors.
[npqqari] (score 4, diepte 0) I have RA and wear Brooks Addiction running shoes. They come in wide sizes. Good balance of cushioning and support.
[npqzhbn] (score 4, diepte 0) I wear Skecher's slip ins. No bending or tying and they come in extra wide. Have always been super comfortable for me. They even have slip in sandals for the summer.
[npqc4j2] (score 3, diepte 0) I had that issue with Hokas. Left me unable to walk and excruciating pain after a day at Disney. I had to sit out the afternoon and evening with my family. The rubber sole on the side was raised so much, presumably to provide support but it was digging too much not my foot. Returned them immediately. 
I’ve been really enjoying Brooks since. I’m on my second pair now. Wear them on my daily walks and also took them on vacations that involved a lot of walking around. Never any issues and it’s like walking on clouds. I have the Brooks Glycerin 21 now (had the 20 model before these). I bought them on a recommendation from a friend who is a nurse and wears them on 12 hour shifts.
[nprdgwh] (score 3, diepte 2) They did collapse from my arthritis (PsA). I really miss all of my old high heeled shoes!
[npw4nf2] (score 3, diepte 1) I bought my first pair in 2023 and they are as comfortable now as they were then. I've since bought 3 more pairs (different colors).  Have you tried the sandals?
[npxawgg] (score 3, diepte 2) I have and they are very comfortable too.
[npq905q] (score 2, diepte 1) 2nd this. Family went on vacation this year. I was super worried about my feet/knees/hips keeping up with the walking. Got new hokas before we left, best choice i could have made.
[nppyq2r] (score 2, diepte 0) I love my Birkenstock sneakers. They've held up well and look sharp.
[nps9n3f] (score 2, diepte 1) I have Altra paradigms and I love them
[npqafni] (score 2, diepte 0) I like Lems. They have a very wide toe box and aren't bulky or heavy. They're comfortable right out of the box but they do mold to your feet over time. The leather ones hold up well, canvas ones not so much.
[nprq9fa] (score 2, diepte 1) New balance is the way to go been using their fresh foam line for years and it’s 10/10
[npqh8q2] (score 2, diepte 0) I am also using Hokas. I don't have wide feet at all. They are narrowish and my arches are collapsed, if that helps for thinking through fit. I have some kind of expensive inserts (not prescription), too. I went to a specialty store to get help with fit and choosing a style. They have been really wonderful and I recommend them to lots of folks.
[npquz52] (score 2, diepte 0) What a nice thing to do for your Mom. I’m sure she’ll appreciate that more than another Chatzky. 
I wear Sketchers slip on. Pickle ball shoes, wide toe box and they have a nice arch, so I don’t need more inserts. I did purchase a 1/2 size bigger to allow for the swelling.
[npqzizm] (score 2, diepte 0) I have kind of flat feet so I’m going to have a particular taste in shoes. Brooks Glycerin when i need a lot of cushioning and I like those more around the house because for me too much walking on cushion is almost too bouncy and I feel unstable. Check out a brand called Ryka. I wear the eco knit slip-ons in wide and I love them so much. Not totally flat but not a ton of support but for me it’s like I feel like my feet really have a grip on the ground. For structure when I need that I wear hiking shoes from Oona.
[npqztqv] (score 2, diepte 0) Love my Hokas. I also use the fleece-lined crocs as an indoor house shoe and during bad flares they're the ones I pick when my feet are too swollen for sneakers.
[nprfqdh] (score 2, diepte 0) Vionic, they're orthopedic but have lots of cool styles. I also love converse run stars. They have a large platform and big tread, super comfortable, and you can do any activities with them. I even go hiking in them!
[npro51c] (score 2, diepte 1) Yes, make this something you do together! Shoes fit and affect people’s feet and RA differently.
[nprk00n] (score 2, diepte 0) Highly dependent on the person and their foot shape. I’m a woman but men’s asics with the insoles taken out work best for me. 

Men’s shoes are wider in the toe box so better for feet that swell. I also buy a half size up so my toes don’t touch the end of the shoe when i walk.
[npruqlg] (score 2, diepte 0) Topos have a wide toe box and come in wide sizes.  I'm living in them at this point.  Buy from reputable sources to avoid problems with returns.  Good luck.
[npsty1x] (score 2, diepte 0) I have a few pairs of Salomon running shoes that I tolerate really well. I try to get them on sale for $100-ish. I find they tend to have good cushion, and my slightly wide feet fit pretty well in the regular width. I've bought direct from their website and through REI. I have 1 pair that needed a little more support inside, so I just added some $15 insoles and they're perfect.

I had to just accept a while back that I'll have to just plan to only buy/wear expensive sneakers. I sooooo miss wearing cheap slip on flats lol
[npt6x5r] (score 2, diepte 0) Look into barefoot shoes.  Then remove the insoles and replace them with arch support insoles.  

You have 2 choices.  Lots of support and cushioning.  But your feet will be like potatoes tied tightly into a shoe. 

Or have your toes free to move.  Have no heal drop.  Let your foot feel and move with the ground.
[nps5jd9] (score 1, diepte 1) Glad this is the first comment. I have Hoka’s wide toe box for men as well. But I’m a man though lols
[npq9rrw] (score 1, diepte 0) For me it is Hike Barefoot sneakers.
[nptnz0x] (score 1, diepte 1 OP) Hi! Thank you for your comment. Would you say that these still offer a decent amount of support although being cushioned?
[npve1pr] (score 1, diepte 2) Excellent support.
[npvvnuz] (score 1, diepte 2) New Balance have a wider toe box to start with and are very comfortable.  I also pull out the flat insole and add a PowerStep insole for arch support.  

For more ankle support, you can look for a trail running type shoe.
[npqf6qo] (score 1, diepte 0) I have wide feet and Hokas were unbelievably painful. Like the worst shoe I've ever worn. I know they're great shoes--my son loves them. But . . not for me. And my size is too small to wear the men's version. Brooks Glycerin GTS work well for me, along with an OTC insole my podiatrist recommended. Brooks website has a shoe finder that was helpful for me. Do keep in mind that the support in even the best shoes wears out fairly quickly. If she wears them everyday for everything I wouldn't expect any pair to remain supportive for more than a few months. My joints let me know when it's time to replace mine.
[npqwfcd] (score 1, diepte 1) Did your arches also collapse due to RA? It’s a fun new complication I’m experiencing right now and had no idea until my new rheumy said so lol
[npqlpan] (score 1, diepte 0) I’m pretty sure you can request a wide in most brand name shoes. I like the Mizuno Wave.
[npqnj6h] (score 1, diepte 0) I recently got some Dr Schools Be True sneakers. Wore them for 3 days straight on a trip. They were so good I bought 4 other colors
[npt86pj] (score 1, diepte 1) Do you wear them for every day use?
[npyje37] (score 1, diepte 1) Same. I have these and wear them all the time.
[npqtac8] (score 1, diepte 0) Hoka's. I buy a half size up from my dress shoe size.  Replace every 4 months.  They aren't cheap, but the support and comfort at max performance in those 120 days saves my body so much hardship
[npqxmto] (score 1, diepte 0) RA Hoka wearer here. I have wide feet and have had 3 bunion/toe surgeries and Hoakas have been my best friend. I would also recommend New Balance wide but if color choice is important, NB is pretty boring. I love the Hoka Bondi 8. They stretch a little but run true to size.  I'm on my third pair and I can't imagine not having them.
[npqz3io] (score 1, diepte 0) I buy brooks addiction max. Very squishy
[npuzgk4] (score 1, diepte 1) I love Ryka! I first discovered them while preparing for a trip to Disney World with the fam. Five days of walking in Florida in July... I don't think I could have enjoyed it as much without those shoes! I've even got my teenage daughter wearing them for ROTC PT days. I have flat feet, RA, and spinal stenosis. I will be a lifelong customer.
[npr14sa] (score 1, diepte 0) I’m an adidas ultra boost person. Adidas just fit my feet well. I also have Skechers slip ons and choose them for short outings when my hands or back are acting up.
[npr79lj] (score 1, diepte 0) I liked the new balance 574 V3 and I also have to hoka cliftons. I find they are both different in their own ways. Although, the hokas are not the bondi which have the rocker bottom, the Clifton’s have that rocker style on the sole which takes a while to get used to, while the new balance are totally flat. I think I like the new balance toe box better personally because I have that drift in my toes.
[nprajt4] (score 1, diepte 0) I’ve tried everything. My toes have spread out so much that I’ve had to go up a full size. Right now I’m wearing Hilma The Everywear Hybrid Running shoe in Fit 2 (wide toe box) and I love them. I got them on Sierra, where they are currently 60% off, which scares me because I think it might mean that they’re phasing them out. Good luck.
[nprdopb] (score 1, diepte 0) I wear a lot of Birkenstocks and I own some Hokas too for trying to exercise in.
[nps60oe] (score 1, diepte 0) Hokas are definitely not for wide feet. My daughter introduced me to Bronax on Amazon. They have a wide toe box and are really comfortable. Nothing hurts more (I hurt all the time) when I wear them, no matter how much I walk.  These are my new go to brand.
[npsojt4] (score 1, diepte 0) The Hokas I tried made my ankles and 5th MP joint hurt. I have short toes and high arches, so I guess they didn't work with that anatomy. It might be best to take her to a store to try shoes and she what works best for her.

 For athletic sneakers, Brooks worked best for me because they have a lot of options for different feet. For casual sneakers, I like Taos.
[npspqyj] (score 1, diepte 0) As you can see there are a
[npsqm05] (score 1, diepte 0) Hokas, and crocs at home
[npssrs4] (score 1, diepte 0) Brooks Ghosts are a solid pick too. They’re supportive but not too heavy, and they hold up well for everyday wear.
[npswu20] (score 1, diepte 0) I have bunions and overlapping toes. I wear Dr Comfort in wide or extra wide, in my regular shoe size. I wear the sneakers in fabric not leather. Comfortable and cute.
[npv2cx2] (score 1, diepte 0) Take your Mom to a specialty store that sells athletic shoes for patients like us. I ended up with On Cloud and they’re great but there are so many good ones out there it helped to have a professional fit me. Good luck.🌷
[npv8y4i] (score 1, diepte 0) New Balance. First shoes I ever stepped into without pain. They are the only ones I wear...all the time.
New Balance have not just wide but super wide (up to a 4E) shoes.
They address other issues too like my super supination.
Make sure about which model would work best. We have a shoe store here that specializes in "abnormal" feet. I hope you might too

Like who is normal, really?!?!!?
[npw3iw7] (score 1, diepte 0) Topo is the best.  Wide, naturally shaped toe box.  My podiatrist recommended them and my feet are like night and day.  Topo Vista are my favorite.
[npwfeog] (score 1, diepte 0) I have Altras because they let your toes spread out. I would suggest going to either a running store or a shoe store that specializes in measuring and fitting shoes. Those stores often allow you to walk around in the shoes for a little while before buying them. REI is another place where they have a good return policy and you can spend a little bit of time walking around in them before you buy.
[npx8m4x] (score 1, diepte 0) I wear women's wide Hokas. The most comfortable and supportive shoe I've ever worn.
[npx8y67] (score 1, diepte 1) Hoka wide toe box shoes.

https://www.hoka.com/en/us/wide/?utm_source=google&utm_medium=ppc_brand&gclsrc=aw.ds&gad_source=1&gad_campaignid=17412293923&gclid=CjwKCAiAlfvIBhA6EiwAcErpyb-VXinp2dAkGl5JCoSMKjuidZtniB0lx3BnYwYjBRS4Bo7A68PGUxoCvqwQAvD_BwE
[npyafe6] (score 1, diepte 0) Yes
[npynrq9] (score 1, diepte 0) brooks ghostmax or glycerin, new balance 1080 or Nike Vomero has wedium wide or ultrawide. I use all 3 on wide or ultrawide, my go to is the NB 1080.
[npyvwde] (score 1, diepte 0) I was able to get my walking analyzed by Fleet Feet store.  They have a floor that measures where your weight lands when you walk. Anyway, my analysis showed which models of which brands would be best for me. I ended up getting Brooks, but there were other choices in other brands.
[nq0c845] (score 1, diepte 0) I am going to get a pair of those slip on Sketchers so I don't have to bend down to put them on or do laces /,velcro etc .I have tried a pair on and they are soooo comfortable but not suitable for winter wear so waiting until Springtime.
[nq2s948] (score 1, diepte 0) New Balance makes wide shoes that are comfy. I was also able to take out the standard insole and get my custom orthotics in them. And if her feet are super tender and prone to swelling, highly recommend she see a podiatrist and try custom insoles. They help a lot!
[nq3av2p] (score 1, diepte 0) Yes
[nqan6q8] (score 1, diepte 0) I've had RA for 25 yrs as well as a fracture in my spine for 16. Bought Hoka sneakers as recommended by some nurse friends of mine, and I've had them for about 6 months. BEST things I have ever had on my feet! Great for balance and walking, and my back doesn't get extremely sore anymore standing for long periods. They are super easy to clean and if you don't like them, you can return them in any shape within the first 3 months as long as you have the original box.
[nqfvq4h] (score 1, diepte 1 OP) thanks for your comment! which style do you have? would you say that they are both comfortable and supportive?
[nr0kylw] (score 1, diepte 2) I have Graviotas and they are soooo comfy and very supportive. Like clouds to walk in. I also have trouble with balance and they have really helped with that.

=== THREAD yjjffg ===
SUBREDDIT: r/nursing
DATUM: 2022-11-01  SCORE: 1  REACTIES: 61
TITEL: Let's talk shoes! Are Clove shoes worth that pricetag?!
POST (source_id=post):
I need new shoes! I work MedSurg 12 hr shifts and my current shoes aren't cutting it.

Dankso clogs hurt like hell, even after being stretched. ,
Alegria are awesome but they don't have in-between sizes so I don't quite fit in the smaller or larger size. 
So....is the hype about Clove shoes real?! Or should I just buy a really nice running/cross training shoe?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iuoeevo] (score 7, diepte 0) I tried them and hated them as a flat-footed wide-footed person. I swear by my Altra running shoes
[iuobk49] (score 5, diepte 0) The majority of my ED wear Brooks or Hoka. You see the occasional Dansko, but only with the older nurses. 

I've had the same pair of Hoka for the last year and my feet never hurt. And I get comments about how I have the most arched feet anyone's ever seen. 

Honestly never heard of Clove or ever heard anyone talk about them.
[iup4rd1] (score 5, diepte 0) Biomechanics guy/runner turned nurse…splurge on expensive full length inserts. The shoe becomes less important. I use superfeet.
[iuow2vz] (score 4, diepte 0) Worth the price tag... debatable. I do like mine and can see myself keeping them for a long time, but I'm not sure I'd say there's anything special about them to justify the price. They are comfortable, but so are plenty of other shoes that offer more versatility than just being worn in the hospital. These do not look good outside of work lol
[iuo67r1] (score 3, diepte 2) So actually maybe the cloves would work for you because I have a super flat foot.. so we're basically opposites
[iuo7te0] (score 3, diepte 0) I've worn my Nikes to work 12 hour shifts since 2018 and never had a problem. I do wear orthortic inserts (Spence) but that's because I have flat feet and have had multiple foot surgeries.
[iuohdfk] (score 3, diepte 1) Is there any specific style of Hokas that are best for nursing?
[iuogv28] (score 3, diepte 1 OP) Lolz... can we really judge a nurse by their shoes? Probs not but hey, I'm pretty new around here.
[iuoi4jx] (score 3, diepte 2) The Bondi models are extremely popular due to the extreme foam cushion base…they also come in wide and extra wide…if you stand for 9-10+ hours a day like me the cushion is a godsend for your legs and your back. 

The 7 model is on sale right now if you want to try them and they offer 30 day returns no questions asked if you don’t vibe with them
[iur2m5l] (score 3, diepte 1) Hokas look super uncomfortable to me, I don’t love a huge amount of platform in my shoe. I wear cloves and am a “real bedside nurse” (ED)I’m not saying they’re amazing but they are fine. I think the best thing to do is exercise and strengthen your feet and arches anyway and then the shoes matter less.
[iurr61s] (score 3, diepte 5) I could be wrong, it was awhile ago. I also read that as inflammation. I need coffee
[iupqnj7] (score 3, diepte 0) No, they sick and my feet were screaming by the end of 8 hours, let alone 12. If you’re going to spend that kind of money get hokas.
[iuq3adu] (score 3, diepte 0) I really wanted to like them but were disappointing. Not breathable at all, not much cushion, had an all around clunky feel to them. They did a number on my plantar fasciitis too. I’m liking my Brooks lately instead
[iuo42xx] (score 2, diepte 0) So I was going to say hell no and that I hated them and they made my knees hurt BUT you said that dansko clogs hurt you even after being stretched so I'm assuming we have very different foot types bc my clogs are the only thing that save my back and feet lol So maybe they would work for you?
[iuo4evf] (score 2, diepte 1 OP) I guess that is an issue when discussing shoes. I have very high arches that dansko's just can't accommodate. They're so cute and easy to clean too but alas they gather dust in my closet.
[iuoajhg] (score 2, diepte 2) The new ones that came out which is the aeros I think has better insoles compared to the older versions it has no support and I have a high arch too.  So I have to change to a customized insole from dr scholl’s. It was worth it for me cause I can just wipe it if any fluid or blood get on them.
[iuo7j49] (score 2, diepte 0) I like both my Cloves and On Cloud waterproof
[iuo81p2] (score 2, diepte 0) Try Oofos (the shoes, not the sandals or clogs). They are amazingly comfortable.
[iuob910] (score 2, diepte 1 OP) In the past I have liked Brooks and Saucony so maybe it's time to return!
[iuoc26m] (score 2, diepte 1) *cries in older nurse at the ripe age of 38

well, in my ED, all the ones that do wear clogs are over 30.
[iuoc7m2] (score 2, diepte 1 OP) I love Hoka and Brooks for running. My only concern is keeping them clean because they are fabric and you're unable to wipe them, but maybe this doesn't really matter? 🤔
[iuojbp4] (score 2, diepte 2) I clean mine Hokas with Cavi wipes and it doesn’t seem to be an issue. Although, any spill onto them definitely gets on your feet which is fucking gross
[iuptss9] (score 2, diepte 2) Steal bootys from the OR
[iuqgl2e] (score 2, diepte 2) Brooks has leather ones that you can wipe down. You just have to buy them online
[iurqpmw] (score 2, diepte 3) Like 130? Two years ago. I’m due for new shoes there are feeling pretty worn (in the sole, the rest is fine) 

Also you can work your feet and create more of an arch. Ballet dancers do it all the time.
[iuojn09] (score 2, diepte 0) I have cloves with my new balance high arch inserts. Love them. I freaking love that I can take a bleach wipe, wipe them shoes down without any harm to my shoes and go about my day. 

Go to a new balance store and step on their fancy computer thingy and see which inserts they recommend, they aren’t cheap but have saved my feet, knees and back. 

I used to wear the dansko XP’s
[iuol0xd] (score 2, diepte 0) I like my super lightweight Hokas. My husband loves his Kurus. I also wore ASICS gels for many years and they were great.
[iuomkxu] (score 2, diepte 0) I’m surprised that no one has mentioned Birkenstocks yet. That’s all I’ve worn for the past ten years and I love them! I replace them every two years (put a lot of steps in each year) to make sure my feet stay happy.
[iuox40f] (score 2, diepte 2) Yeah, they might be worth looking into. Roomy toe box for sure. I get the polyurethane ones (not the leather) because I like being able to wipe them down with whatever is on hand, but the leather ones look amazing. I’d like to get those just as soon as people stop bleeding on me so often :)
[iuoxk3m] (score 2, diepte 1) Who wears their work shoes outside of work? 🤢🤮
[iuoxuj0] (score 2, diepte 2) A lot of my coworkers who wear Nike/Nobull/Brooks do.
[iupenz8] (score 2, diepte 1 OP) Oooh now this seems like the right information. I didn't even know I needed to ask for. Thank you!
[iupq8gh] (score 2, diepte 0) They are the worst. Toe box was super slim, would not recommend at all.
[iuq39cs] (score 2, diepte 0) I just started wearing a pair after I had heard good things about them.  Nope.  Not a fan.  They're floppy.  No arch support.  Feet legitimately hurt after a shift.  I'll go back to the Merrell slip-ons I've been wearing the last few years.
[iura734] (score 2, diepte 0) Doc Martens 1461!

Comfortable. Long lasting. 

And perhaps most importantly… bodily fluids run off rather than through them!
[iurndvv] (score 2, diepte 0) I have cloves and they are comfortable. I like that they are able to just be wiped down and are waterproof. But after 12 hours my toes hurt. Maybe I just got a size too small? Idk. I also have hokas and now those are very comfortable!
[iuoy57j] (score 1, diepte 2) I wore two pairs of socks and used a blow dryer to warm my clogs up and walked around for an hour. After that I had no more issues and I have arches so high the middle of my foot doesn’t touch the ground at all
[iup3a9m] (score 1, diepte 3 OP) I really wish that would help but I even had my clogs professionally stretched where the band goes over the foot and they hit the tops real bad.
[iuo934p] (score 1, diepte 1 OP) Never even heard of those. Cool, I will!
[iuoa93v] (score 1, diepte 0) Nope I hate them. Try kuru expensive but worth it
[iuoborx] (score 1, diepte 1 OP) Interesting! Ya get what you pay for though
[iuoap34] (score 1, diepte 0) I've never tried Cloves. Danskos killed my feet as well. The best shoes I have found are Brooks. I love them dearly and my back and joints do too.
[iurmwfq] (score 1, diepte 2) Hey I’m 26 and love wearing danskos to work lol. I do get teased though
[iuodbar] (score 1, diepte 2) I mean I used kiwi waterproof spray (like the kind you’re supposed to use on tents) for my brooks and honestly unless there’s gonna be a ton of liquid falling on my feet, they work really well
[iuu8epm] (score 1, diepte 2) Hoka makes leather work shoes. I just scotchguard mine.
[iuobwa3] (score 1, diepte 0) Hokas all the way!!!!!
[iuoh9xe] (score 1, diepte 1) Is there any specific style of Hokas that are best for nursing?
[iuorvqp] (score 1, diepte 3) Thanks!
[iurq7io] (score 1, diepte 2) Eh, I agree that ppl need to strength their feet and ankles but see the thing is that not everyone has arches, like myself.

Btw just curious, how much did you pay for your Cloves?
[iurqzb1] (score 1, diepte 4) Gotcha, inflation has them at $148 now for a pair
[iuov6vr] (score 1, diepte 1 OP) Oooh, sounds fancy. I have high arches and like a roomy toe box, any chance birkenstocks fit that description?
[iuow1y3] (score 1, diepte 2) I have super high arches as well and love my Birkenstock clogs. They’ve also started making a polyurethane clog that looks pretty comfy
[iuqgj5i] (score 1, diepte 3) Do they? Or do they have different pairs?
I have multiple pairs of brooks
[iuox55j] (score 1, diepte 0) I bought Cloves because they were waterproof and I can just skip them on.   I'm not on my feet a ton (home health),  but I like them (and I did volunteer at a vaccine clinic last year where I was constantly on my feet for 10 hours in the rain.  My feet didn't hurt and weren't wet by the end of it!
[iuppkt3] (score 1, diepte 2) Funny enough, they were originally designed exclusively for doctors actually. They’re great.
[iupbo8r] (score 1, diepte 0) I love wearing hey dudes for work. They are also machine washable and look nice with the jogger style scrub pant.
[iupw0aw] (score 1, diepte 1 OP) Good to know, roomy toe area is important for me. Thanks!
[iuq33lq] (score 1, diepte 1) Same.  Not a fan.
[ji8x4b7] (score 1, diepte 1) What style/model of brooks do you like?
[ji98g8e] (score 1, diepte 2) I’ve had several pairs of the Revel line, I find the heel nice and springy
[iuyp2ri] (score 1, diepte 0) I bought their 2021 clove classic shoe that is on sale and also the new clove solo. I've worn the clove classic for one day only for 12 hours and I do not think it was comfy, mind you I am also at that point when I wore it about 25 ish weeks pregnant. I have wide feet to begin with and flat feet. I tried on the clove solo and walked around for a little bit, it did not offer a whole lot of arch support. I returned them all :x  
Does anyone have recommendations for shoes that are easily wipeable that accommodates wide foot people with little to no arches? Also, what foot insoles do you recommend for people with flat feet?
[iuoysrp] (score -1, diepte 0) They look hideous. Don’t care how great they are.
[iuof6f1] (score -2, diepte 0) Cloves are complete trash and no real bedside nurse wears them imo and Hokas are the same price point but much better build and function 

Hokas for life

=== THREAD 11hot78 ===
SUBREDDIT: r/Nurses
DATUM: 2023-03-04  SCORE: 24  REACTIES: 61
TITEL: What shoes do you wear for 12hr shifts?
POST (source_id=post):
I have been looking for work shoes that are impermeable to fluids, have good toe space, and are not clogs. I have been wearing sneakers but I really have noticed how much fluids get on my feet throughout the day with patients. They need to be comfortable for the long 12hr shifts, but also safe to walk in with not slipping off. What do y’all wear?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jaul5ty] (score 25, diepte 0) Hokas, 10/10 recommend. Had a pair of cloves but they hurt my feet so bad. They’re definitely overpriced for what you get
[javu1gx] (score 20, diepte 1) Respectfully, why would you wear your work sneakers around your home? Given our line of work, that’s pretty gross 😅
[jaunbwn] (score 8, diepte 0) I wear many shoes but lately Hoka bondi 7.
[jaw3vo7] (score 8, diepte 1) Please no. Please for the love of all that’s holy tell me this isn’t actually real.
[jauja6d] (score 7, diepte 0) I love my Cloves. I have wide feet so I ordered a half size up and have been extremely pleased. I rotate between 3 pairs and my feet don't hurt at the end of the day.
[javi9un] (score 6, diepte 0) Clove- they’re waterproof. I have a pair of Hoka as well. I got a patient peed on me one time and it soaked through my shoes and socks. I have been wearing Clove since …~~’
[javivs9] (score 6, diepte 0) Another vote for cloves. Comfortable, easy to clean. Before I got them I wore ASICS and they were comfortable but body fluids! Don’t have that issue with cloves and I own 2 pairs.
[javv5pz] (score 6, diepte 0) Brooks Ghosts!!!! They're water resistant. Stopped having foot, leg and knew pain :)
[jauomlh] (score 4, diepte 0) Dansko Kane clog.
[javqrsr] (score 4, diepte 0) I think that by far your best bet is to go to a running store and have them measure your in-step, arches, and other measurables. Hokas, Altras, ASICS etc come in different shapes and what might work for you feel really uncomfortable for someone else based on the shape of your own foot. 

I think it’s important to try different shoes too. I put my foot into some Nike runners and it was squished. I went with a Hoka One Zone’s and they have a wide toebox for my feet to breathe. 

Any major town/city will have a running store in or near it. If not, highly suggest trying various pairs of shoes at your local athletic store.
[javv28l] (score 4, diepte 0) Allegria. Little dorky, but good options, most of the shoes come in wide sizes as well. And my feet never hurt
[jauzeld] (score 3, diepte 0) Allbirds. Stopped getting Plantar Fasciitis. Plus they are washable
[javtiuz] (score 3, diepte 0) Birkenstock tokios. They look like the regular birkenstock clogs but they're made of leather and have a strap in the back to hold your feet in. I have to stop myself from wearing them around the house when I'm at home.
[jaxwmey] (score 3, diepte 1) I am on my 3 rd pair - in 15 years. Wear well, space for toes and no back pain. Dansko kills my back.
[jaw69lz] (score 3, diepte 0) Hokas and compression socks. I feel like socks made more of a difference than changing my shoe!
[jawerdb] (score 3, diepte 0) I love my crocs. The professional/work ones don’t have any holes and they’re everything proof. If they get splashed with anything, you can just wipe them down with purple wipes.
[jaxep9e] (score 2, diepte 1) Agreed with this! Love my Hokas, my Cloves killed my feet. I’ll only ever wear Hokas for sneakers now lol.
[jawbw8t] (score 2, diepte 1) Which allbirds do you wear?
[jawgv6h] (score 2, diepte 2) The Runner Up Mizzles. Water Repellent. All their soles are super comfy.
[jaylbjt] (score 2, diepte 1) You can spray them with a waterproofing agent, nikwax makes a good one.  It isn’t perfect but it helps.
[jaw4bs4] (score 2, diepte 0) Kuru
[jayxyc1] (score 2, diepte 1) I agree -- compression socks and almost any pair of shoes with decent support keep my feet, legs, and back happy.
[jawc6t0] (score 2, diepte 0) Ariat Boots. Comfy and last forever, plus easy to clean!
[jaz177q] (score 2, diepte 0) Hoka Bondi SR, with Fox River anti-fatigue socks. Trust me, you’re welcome. The Bondi SR specifically is non-perforated leather, waterproof and slip proof vibram sole. They call it their workplace warrior.
[jaujoni] (score 1, diepte 0) New Balance 990v5.  These aren't cheap, $180-$200 per pair but I've been wearing the current pair long enough that I've got a couple of blood stains that are from the peak-Covid days (was proning a patient when they went wild and ripped their A-line out), so they're at least a couple of years old and are still super-comfy and supportive.

They're also very cleanable, I had a patient basically sit in my lap and have explosive diarrhea, you would even know from looking at them today.
[jayajky] (score 1, diepte 1) Came here to say this!!
[jcrysmn] (score 1, diepte 1 OP) I just got off my first shift with cloves and I had cut off circulation to my toes and blisters on my feet. I am going to give hoka a try&lt;3
[jcs62wt] (score 1, diepte 2) That’s what happened when I wore them after one shift. I gave them to a classmate of mine who had no shoes for clinicals. Hopefully hokas feel better!
[jaunhlp] (score 1, diepte 0) I honestly haven’t tried them yet but Ive been wanting to try gales. They don’t have laces so easy to wipe clean and look cushy/comfy but supportive.. anyone tried them?
[jaunk02] (score 1, diepte 0) Hoka's now  I bought 2 defy shoes and my feet hurt by the time I got home
[jauq0df] (score 1, diepte 0) I’ve tried several different recommended brands, but once I found Hokas I finished looking. The only shoes I’ve ever had where my feet actually feel pretty normal at the end of my shift.
[jauvtep] (score 1, diepte 0) Hokas clifton/Bondi or Brooks glycerin
[jazm845] (score 1, diepte 2) Good to know. Thank you!!!!
[jazolma] (score 1, diepte 3) You are so welcome.  It’s a game changer.
[javzyz7] (score 1, diepte 0) Skechers

They're not waterproof but comfortable to wear for 12 hours.
It has memory foam. It's a shoe you don't have to 'break into' .
[jawa771] (score 1, diepte 0) I went to a running store, signed up for their friends and family, which allowed me 90 days to get to know a shoe or insert. I could return anything for refund or exchange within that time.

After a few trial and errors (and a plantar fasciitis flare up) I settled with the Asics Gel Nimbus 25 and a pair of Brooks Ghost. The Asics are for work, the Brooks are for my daily walks. 

As far as waterproof, I have some Bala 12, but for some odd reason, the tops of my toes hurt after wearing them…like my toe nails ache…it’s weird, especially since I keep all my nails short!
[jawbhk4] (score 1, diepte 0) I currently have Hokas the bondi 7 I think? And I have my own insoles I put in my shoes. I think their nice, never tried any cloves though
[jawy55f] (score 1, diepte 0) I feel like I'll never find a brand I'm completely happy with but my go-tos are the Infinity Cherokee slip ons. I need a shoe that's slip resistant also a bit sturdy  by the toes since I have a tendency to stub my toes.
[jax19r6] (score 1, diepte 0) Tried all the fancy brands but ended up back in my Naturalizers.....they are wonderful!
[jax9j6w] (score 1, diepte 0) Nike slides
[jaxu5qe] (score 1, diepte 0) I just bought my 3rd pair of Cloves. I spilled betadine on them on accident and just a quick wipe and no stains (just a little on the laces but I didn’t feel doing more lol).

I have high arches and narrow feet so idk if the comfort works for everyone. But I’ve worked 3 in a row and didn’t notice any back pain post shift til after the 3rd shift.

Edit: to add I also love not having to worry about shoe laces. I can be clumsy sometimes and get sensitive to shit that’s too tight on me. They aren’t bulky either so I feel safe navigating tight spaces and like the grip. If walking onto a wet surface they don’t slide…just get squeaky for a bit.
[jaxwmoe] (score 1, diepte 0) Oofos is so underrated!! They’re the best. I stopped wearing them when I switched to cloves when I did dialysis since I probably will get a lot of blood on me.
[jaxwzzj] (score 1, diepte 0) Nursemates align velocity and compression socks.
[jay4ama] (score 1, diepte 0) Vessi
[jay4si8] (score 1, diepte 0) I have been buying OnClouds since I started working in the operating room. First month in the OR I tried wearing the Under Armor Liquify that I wore on the floor, and I was almost in tears every night with my legs hurting so bad. Switched to OnClouds and I haven't looked back. And this is with me walking 15 miles at work every week and with a repaired hip labrum and more than likely the other hip labrum torn too. Highly recommend that brand.
[jay8zmk] (score 1, diepte 0) Spent 5 years going threw shoes and never found anything that worked until someone recommended Birkenstocks. Pricy but I have had the same pair for 7 years now and I never have foot or calf pain anymore.
[jaybodx] (score 1, diepte 0) Sketchers wide toe max cushioning or go walk flex
[jayd53o] (score 1, diepte 0) 🐎👟👟
[jaydoqh] (score 1, diepte 0) Vans
[jayol11] (score 1, diepte 0) ASICS gt2000 8 Have lasted me longer than any other shoe
[jayyxra] (score 1, diepte 0) I wear Nike airs for the comfort and inevitably replace them about every 3 months
[jazp0qb] (score 1, diepte 0) Crocs baby crocs.  Sometimes a hoka.
[jb0lqkv] (score 1, diepte 0) I’m a die hard Sanita Clog girl. They’re much more comfy than danksos. And they last forever. Plus they’re much better fitted to your foot. I’m an icu nurse and can run with the code cart across the unit and run up multiple flights of stairs when a code is called.
[jb2egz1] (score 1, diepte 0) Hoka Black label
[jbkbql7] (score 1, diepte 0) I wear Keen's hiking boots.  They have offerings that are impermeable and they are designed with a wide toe box.

I've worn these for years.  I can be on my feet 12 hours and be OK when I leave the hopsital.
[jax2fdo] (score 0, diepte 2) I work in an area of nursing that’s not quite as gross as others
[jav9k0d] (score 0, diepte 0) Danskos. Can’t wear anything else or I’m a complete invalid by the end of 12 hours.
[jaweo1l] (score 0, diepte 0) I currently wear Brooks Ghost series, feels like walking on a cloud. Usually wear for a year then replace, usually too torn up anyways
[jaws2go] (score 0, diepte 0) Also, go ahead and utilize booties over your choice of comfortable shoes. Helps keep those kicks clean and also (when used correctly) helps stop spread of pathogens.
[jav89s8] (score -5, diepte 0) My bougie coworkers wear hokas or Danskos. I wear the same sneakers to work that I wear at home, to the store, to the gym. They’re aesics and they hold up great

