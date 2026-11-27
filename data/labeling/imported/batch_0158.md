# Label-batch batch_0158

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
Schrijf het resultaat naar `batch_0158.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 158w08p, 1d0apgx, 1sdeoa4).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 158w08p ===
SUBREDDIT: r/Biohackers
DATUM: 2023-07-25  SCORE: 64  REACTIES: 119
TITEL: Does barefoot shoes actually have benefits or just gimmick?
POST (source_id=post):
Lately I've been seeing a lot of hype around "barefoot shoes" from family and friends - those minimalist shoes with thin, flexible soles that mimic being barefoot. Brands like Vibram, Xero Shoes, and Vivobarefoot are becoming really popular. [Though online discussions are quite mixed](https://biohacking.the.select/posts/wdqm). 

But I'm skeptical if these shoes actually provide any benefits, or if it's all just clever marketing. The claims seem almost too good to be true - improved posture, stronger feet, reduced injury risk, better running form. Is there any science backing this up?

Has anyone made the switch to barefoot shoes and noticed real improvements? Or do you think the benefits are overblown? I'd love to hear some first-hand experiences before I take the plunge and invest in my own pair!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jtc9cs4] (score 43, diepte 0) Barefoot running has been around for a while now and it was made very popular by the book, Born to Run. If you’ve been using a shoe that has cushioning or any drop you shouldn’t jump into barefoot running right away because you will mess up your feet
[jtce1gc] (score 27, diepte 0) Personal anecdote I'm an very active person (sports, working out, hiking, running, ect.) and I've struggled with various foot and knee pains throughout my life. After I transitioned to barefoot shoes most of those pains went away. 

I still rotate in regular running shoes for long runs, but for shorter runs and day to day activities it's only barefoot shoes for me.
[jtd216k] (score 19, diepte 2) As someone who converted completely, without problems I can share my experience.

I walked in barefoot shoes for about 3 years, regularly switching to normal shoes, which after a while felt really weird, so i simply stopped, once the old normal shoes were outworn.

This year i started to train for my first ever half marathon and after being able to run 10-14 miles without problems i thought, maybe it is time to switch to barefoot here as well. 

Wanted to start slow and did my first 6 mile barefoot-shoe run...BOI i never had such a muscle ache...took me 4 days to recover completely. Second run was fine...switched back to running shoes for testing purposes and it hurt my feet...now i am completely fine running the same distance in my new shoes after my 5-6th run. 

Learning: always start slowly and stick to it.

If it is healthy? I 100% believe so, because you can tell the difference in your ligaments, joints and muscles. You walk more stable and you have no accidents in twisting your ankle ir whatever.
[jtcbhe3] (score 19, diepte 0) Do you like to be barefoot? I could hardly stand to wear shoes before barefoot shoes were a thing and even went about a year only wear soleless slippers instead of actual shoes. I hated walking because my feet hurt in basically all regular shoes. Since exclusively wearing barefoot shoes, I love walking and my feet don't hurt all the time.

If you're happy with the shoes you already wear, why make the switch? If you have an especially wide toe box or other complaints related to wearing traditional shoes, try them.

I will say that aside from barefoot shoes matching my particular feet, I have way better balance and ankle mobility in barefoot shoes than any shoes that have more than a super minimal sole.
[jtcf5os] (score 18, diepte 2) Most people start out with zero drop shoes and then transition to barefoot shoes.

If you haven't run in zero drop shoes before you'll want to start out doing low distance and slow speed to give your body time to adjust. If you already have traditional running shoes keep using those as your primary and rotate the zero drop shoes in a couple times a week.

Calf and ankle strengthening exercises are suggested as zero drop is more taxing on the calf and ankles (compared to high drop shoes, high drop shoes are more taxing in the knees and hips).

Single leg balancing exercises are also suggested.

Eventually your balance and ankle/calf strength will increase to the point where you'll be able to rotate your zero drop shoes in more.

The process is the same for zero drop traditional shoes to barefoot shoes.
[jtcbcgs] (score 12, diepte 0) Barefoot or barefoot shoe on dirt or grass ->good

Barefoot or barefoot shoe on pavement -> bad
[jtcb7j2] (score 11, diepte 1 OP) how did you ease your way into barefoot running? be great if you could share some advice or first hand experience!
[jtcwh6e] (score 10, diepte 0) Could the benefit of barefoot shoes actually come from the wide toebox (most of them offer it) and the zero drop? I would argue having shoes with those two features even if they aren't barefoot is a big improvement. If you disagree with those two points, I would love to hear why!

Something to consider is also the environment that we leave in: If you're in a city with concrete or hardwood under your feet all day long, there's a case to be made for adding back a bit of cushioning.
[jtcyoc2] (score 9, diepte 1) Barefoot running has been around for a lot longer than that.
[jtch6g4] (score 9, diepte 0) Barefoot (in a short term) promote mid-front foot striking, which is not nessesary "better" but you engage calves much more for cushioning, which is much more natural as far as human anatomy goes.

Long term - the more space and grip your toes have - the better balance and neural connections you are going to have. Might be important when you are 80+
[jtcjh1m] (score 9, diepte 0) There is evidence for and against. I'd say basically we humans are likely designed to have a natural foot position, not inches of cushioning between us and the ground.  On the flip side, we are probably not designed for tons of cement walking either.  I love going barefoot or with minimal cushion for most walking around but I do wear normal shoes for high impact sports.  For running, you will want to transition very slowly and carefully and it's much better to do it on natural ground, not cement.  Cement is just unnatural for us all the way around.  Running on the beach or dirt trails is better.  Also some people have already messed up their feet or ankles badly and that may complicate things for them.  If your ankles are damaged and not aligned correctly, you may not be able to safely go without support anymore.
[jtd5eug] (score 8, diepte 0) Ive ton a ton of research on this...

Its not all roses. Some people make their feet worse by going barefoot/minimal. Some dont. Some people feel fine initially when they do it only to get injured long term from doing it with things like plantar fasciitis. 

Just as we werent designed to wear shoes we werent designed to walk on concrete. Our bodies didnt live as long either. So you need to make some concessions and figure out what works for you. 

After looking at the research out there, I chose to wear hokas which are the opposite of barefoot. Our bodies/joints wear after years shoes or barefoot...I am trying to protect from that wear for as long as possible so in my 80s or 90s my knees dont hurt from hitting the pavement extra hard.
[jtcbk4q] (score 7, diepte 0) I’ve been running barefoot on the beach lately. My knees don’t hurt nearly as much as when in shoes on the sidewalk. Maybe there is a thing to barefooted running
[jtcgty5] (score 7, diepte 0) I bought the original five fingers when they first came out, wore them for a couple of years… My reaction: meh. Seriously. Didn’t notice any difference other than feeling (a lot) the pebbles and “imperfections” on the ground, which was rather uncomfortable. The newer generation of barefoot shoes seem to have thicker soles, which in my view kind of defeat the “barefoot” point. 
I now wear normal shoes according to the training I’m doing (running, HIIT, training).
[jtcbc9n] (score 6, diepte 1 OP) switching to barefoot shoes is supposed to make your feet and joints stronger tho. sounds like might actually help with joint problems in the long term according to this [discussion](https://biohacking.the.select/posts/wdqm)
[jtcqmy5] (score 5, diepte 2) natural cushioning for the type of environment we evolved in. Grassland.
[jtccyj5] (score 5, diepte 2) I wear absolutely nothing but barefoot shoes for going on 10 years now with the one exception that after doing 3 miles of small to medium sized boulders, I accepted that I could use one pair of shoes with more cushioning. I got a pair of Altra Lone Peaks, which are super cushioned compared to all my other shoes, but if you look at the sole, they're still designed quite similarly to barefoot shoes. My day to day shoes are Lems Boulder Boot and my running shoes are Lems Primal 2.  
I could maybe see barefoot shoes helping with knee pain, but the thing that really helps with any knee pain I might have (especially from running) is weightlifting (okay, and now that I mention it, I do actually have a pair of weightlifting shoes which definitely aren't barefoot style).
[jtdsxyc] (score 5, diepte 1) I wore pure minimalist/barefoot shoes for running for many years and eventually started developing toe pain. I've since moved to shoes with zero drop and a wide toe box, and some padding, and my toe pain has disappeared. A few brands I like: Altra running shoes, Bedrock sandals.
[jtcp2u3] (score 4, diepte 2) I've experienced the complete opposite. I used to roll my ankles often-  since I was in middle school it was a common injury for me (I am now 31). I *rarely* roll my ankles after switching to barefoot shoes, I've been wearing them for about 4 years now.
[jtdzc8r] (score 4, diepte 2) I would go on a run in shoes, then put on vibrams and do a block to cool down. Then 2. Then 3, etc until I could do 5-6 miles barefoot. You really need to develop your calf and foot muscles in new ways, from the ground up, which I think helped my posture. when I was in top barefoot shape (only doing 4 miles per run on average), my calves were more cut than when I was regularly doing half marathons in shoes
[jtci30t] (score 4, diepte 1) Could it be because of wearing unnatural shoes?
[jtckwjt] (score 4, diepte 1) I've been barefoot for most of my life. Only wearing shoes when I leave the house, which is seldom.   
I've never had any issues from being barefoot. Your soles harden and your toes widen and you adapt.
[jtcc65v] (score 4, diepte 1 OP) i have the same problem! i wear very well cushioned shoes to run and i often get knee pain during or after my runs. so my friends suggested barefoot shoes for walking to strengthen knee joint and correct walking/running form
[jtcno91] (score 4, diepte 0) I've done six marathons in vivobarefoot shoes. Took almost no time transition. 

Had heaps of problems before, especially with knees.

I dont believe cushioned shoes are good for anybody
[jtcpha5] (score 3, diepte 1) +1 on this comment. Just want to add that the book also talks about running light. Your body needs to adjust the amount of force at different points if your foot and legs. The book also talks about needing a sole. So take it slow and really feel your way into it.
[jtcbh4i] (score 3, diepte 1 OP) natural cushioning haha
[jtcbsdq] (score 3, diepte 1 OP) my friends recommended me to wear barefoot shoes cause i keep having knee pain after runs. they suggested i should try barefoot shoes to correct my running form. I also have quote wide feet so the extra wide toe box is a bonus! do you wear barefoot shoes for day to day and training as well?
[jtdw284] (score 3, diepte 2) I really recommend starting with zero drop shoes. Altra are good, as are Skora. Both have wider toe boxes. The first time I ran in altras my calves and ankles were on fire. You have to ease into it and wear them for walking a ton before you try a run, and don’t plan a long first run. You’ve also gotta be diligent about stretching as you acclimate. I didn’t stretch enough and developed shin splints. Now I only wear zero drop, never went all the way to barefoot because I like more padding between me and the concrete I’m always walking on. But I love zero drop and they really work for me. They worked to change my foot drop and gait (heel striker).
[jtce4ba] (score 3, diepte 2) I’ve had other friends do this and it helped them. Do you have access to a highschool or middschool track? They are usually soft and help with knee issues too.
[jtcbf2i] (score 2, diepte 1 OP) Really? is it cause of training in barefoot shoes or just walking day to day wear that damaged their ankles and feet?
[jtcrrt2] (score 2, diepte 1) Why is this getting downvoted? They are just giving their experience. This is the problem with movements like this, people get way too evangelical about the idea and refuse to acknowledge any other perspective.
[jte8ty3] (score 2, diepte 2) Thanks. I thought the same.
[jtcv1a3] (score 2, diepte 2) No, I broke my foot…
[jtcizah] (score 2, diepte 2) Would suggest you start out slowly and don't run on pavement at least for a while and see how it goes.  One important thing is to transition very slowly, you have a lifetime of unnatural movement behind you, those muscle will need time to rework and you'll need time to learn proper foot movement again.
[jtjoptz] (score 2, diepte 2) They can allow you an opportunity to improve muscle tone and posture.  If you’re used to a lot of external support, you may have some tiny sore muscles after a couple of hours of just standing and walking normally.  

Do not start running in them on the first day, unless your old sneakers also offered very little support.  If you don’t yet understand how healthy your muscles in your feet are, you’ll end up sore or even mildly injured.  

Honestly, this is normal, you should be able to have healthy feet and ankles.  Most people only need strong structural sneakers for challenging situations, like running on concrete or other surfaces with no give.
[jtcjhms] (score 2, diepte 1 OP) someone asked about the five fingers in [this discussion](https://biohacking.the.select/posts/wdqm), seems like they are still quite popular!
[ju16ivy] (score 2, diepte 2) The issue is that the human foot was designed to tolerate natural conditions and super hard flat cement, etc are not natural.
[jtcm6ui] (score 2, diepte 0) They’re for sure my favorite gym shoes I’ve ever worn. The contact with the floor is absolutely better than pretty much any shoe. Would never wear them running or anything high impact though, you really feel everything
[jtcqtr9] (score 2, diepte 0) I've always had massive issues with my gait.  Bad posture, bad balance, one bad knee, super high arches that a podiatrist insisted required special orthotics, and for the last 2 years a sprained ankle/broken foot combo that wouldn't stop heal.  Switched to barefoot shoes 3 months ago and have seen massive improvement in pain on the bad knee, foot and ankle during that short time.  Not a runner so can't comment there but I've been quite impressed.  Kind of obvious now that I think about it as I've always been most comfortable barefoot or wearing unsupportive sandals in daily life, so they seem well-suited to my issues.
[jtcr23z] (score 2, diepte 0) I love my five fingers; been wearing them for the last decade or more at this point - can’t remember the last time I put on a ‘real’ pair of shoes.

They’re probably not for everyone and do take a bit of getting used to but I find them so much more comfortable to wear all day long; also don’t get tired feet in the same way I used to before switching (don’t get me wrong, can definitely tell that I’ve been walking all day, but it’s a different less painful ache when doing so).
[jtd64zs] (score 2, diepte 1 OP) Curious to hear more about your experience with five fingers! quite a nice shoe! there are some other people asking about it in this [discussion](https://biohacking.the.select/posts/wdqm). Perhaps you could share a bit of your experience with the guys who are asking in this biohacking group chat?
[jte5not] (score 2, diepte 0) I switched because of severe leg pain I developed after Covid when I would work a full day on my feet and almost immediately I felt better. The symptoms were all connected to the type of shoes I’d been wearing, but I’m not sure why Covid brought that to the surface — the systemic inflammation it causes could perhaps have unlocked a lot of “dormant” issues I didn’t even realize were there before. I only wear barefoot shoes now for work, and I also use toe spacers when at home which are awesome for helping to stretch out the dorsal fascia. I feel a major difference using both of these, so it’s definitely not just hype. 

“Normal” tennis shoes give an unstable posture and the rest of your body has to constantly adjust to being on this “rocking chair” sort of ground…the design of our modern shoes is potentially causing postural imbalance, pain and tension, and all sorts of musculoskeletal problems. I also don’t think getting them molded by a professional is any better unless you just want to pay these people large sums of money. There is so much faulty science and research in our society that is ruining people’s personal judgment and making them doubt their own senses and innate experience. 

It’s the base of the shoe and the narrow, confined design that is impeding the freedom of the foot and it’s ability to spread out and ground your body with a solid foundation. Modern shoes cause a lot of chronic fatigue because the body is constantly adjusting to that instability. That is what I determined from my own experience, but not all modern designs are going to be a bad as others. It’s funny because the last “sports shoes” of that variety I used before going to barefoot minimalist designs were On Clouds which everyone told me were soo great… but they have this huge base which is filled with empty space? It feels like you’re standing in a bounce house. I tried them out and developed even worse pain than before… then I started asking myself, “why would I want to walk on clouds? I need to be on the solid earth. This doesn’t make sense.” 

Made the change and I’ll never look back. Not all barefoot minimalist shoes are the same either, so like anything explore a variety of brands to find what works best for you.
[jtjj4xb] (score 2, diepte 0) I just prefer the way they feel.  I originally had some old puma motorcycle shoes i wore around and They weren’t truly zero drop, but they were closer than anything else i had worn.  When i sprinted in them i had to run different (or else hideous pain).  I just liked the way it felt and ever since I’ve always opted for flexible minimalist shoes.  I thought i would give you my take just from preference over any real benefit.  I just felt more nimble, responsive, which is fun.
[jtcompb] (score 1, diepte 2) I noticed I rolled my ankle more. There isn't a lot of support at the ankle and because your foot is more defined it's easier to twist it.
[jtciso5] (score 1, diepte 1) I had no problems but since I have never used excessive ankle support, my ankles are strong.  I also do not recommend it for those with severe ankle issues, I know a few people whose ankles just collapse easily, it may be too late for them to be able to live without ankle support.
[jtcnh95] (score 1, diepte 2) Start out extremely, extremely low mileage / effort barefoot once you feel comfortable enough running in minimalist shoes. If you’re comfortable running 8 miles normally then you’ll want to start at just a quarter mile or less to start around a soccer field or the infield of a track.

I used to race barefoot back in high school cross country and it really was a challenge to build up at a slow enough rate to avoid plantar injuries. You really need to build up extremely slowly running in soft grass and I can’t emphasize that enough.
(83 reacties met lagere score weggelaten)

=== THREAD 1d0apgx ===
SUBREDDIT: r/Biohackers
DATUM: 2024-05-25  SCORE: 34  REACTIES: 107
TITEL: Began noticing purple veins all over the side of my feet. Is there a way to save my vascular system?
POST (source_id=post):
I have lots of hours of standing up in my job, but still i don't believe it's healthy. Man in his mid 30s

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l5mcmsr] (score 49, diepte 0) Wearing compression stockings, especially considering how much standing you do, will help prevent these from worsening. Basically the valves in your veins become fatigued and the compression helps to shunt blood toward deeper veins with better functioning valves
[l5mwpjx] (score 33, diepte 2) Yeah I mean...  biohacking = hacking biological processes, what are you expecting? 

People are trying to improve issues that come with having a body made of flesh living in an universe with passing time.
[l5m8e9r] (score 27, diepte 0) normal aging.
[l5mgwyd] (score 25, diepte 0) BPC 157 greatly helps repair, it still might not remove the physical appearance, but will upregulate new growth of micro capillaries.
[l5mnsod] (score 24, diepte 0) you are ok. that is completely normal. If you are noticing this AND feeling to bad about that probably the stress you are having are more problematic that those little vains.

just a suggestion. You will get old. Try to not old like crap, but also dont go crazy about getting old.

I dont speak esperanto.
[l5mqokk] (score 22, diepte 1) Compression socks are so helpful. My vascular surgeon recommends them for everyone. 

They make my legs feel amazing especially on days I stand a lot - going to concerts, walking the dog, house maintenance days. They don’t have to be crazy compression either - I think the compression on mine is only 10mmHg
[l5mt86w] (score 20, diepte 0) Eat lots of high-quality protein and collagen to support the structure of your vascular system. Bone broth is great for that. Increase your intake of vitamin C, as it partakes in collagen synthesis. Vitamin C from food sources is superior to any supplement, no matter how 'fancy' it sounds (i.e., liposomal vitamin C, vitamin C with bioflavonoids, etc.).
[l5mubki] (score 14, diepte 1) This sub in a nutshell:


This thing happening to me how can I stop it?


Thing that is happening: normal biological processes.
[l5mrq25] (score 13, diepte 0) The bioflavonoid Rutin
[l5myxz8] (score 9, diepte 3) *laughs in spacetime*
[l5oabmn] (score 8, diepte 2) Makes sense, excess dietary protein contributes to aging via mTOR dependent pathways and increased systemic inflammation which can directly contribute to cardiovascular degradation. Getting excess protein to reduce aging only works if you're actually malnourished, otherwise it's total bro-science that contradicts the available evidence.
[l5nguap] (score 7, diepte 1) Lol i'm 23 and i have it too
[l5mh7pc] (score 7, diepte 1 OP) Does it promote angiogenesis to feed cancer cells as well though?
[l5mnvkf] (score 7, diepte 1 OP) Makes some sense
[l5n4lwv] (score 7, diepte 0) amputate.
[l5mwk6f] (score 6, diepte 2) Is it still good to use them even if standing doesn’t make your legs/feet hurt?
[l5ou8ff] (score 6, diepte 4) That's true to a certain extent. As far as I'm aware there isn't any evidence for significantly increased autophagy in humans with reasonable IF schedules (bear in mind it's usually seen in rodents in 24-48h of fasting, which scaling to humans' lifespans/metabolic rate would be more akin to a fairly long extended fast, though it's hard to make the case that any direct comparison is particularly valid on this subject).

The evidence for improving metabolic parameters and reducing inflammation is stronger, though I'd be hesitant to claim it can fully offset the negative effects of a high protein diet unless you have direct evidence of that (I'd be very interested to see it if that's the case).

There is certainly more nuance to the situation, eg the particular amino acid profiles of the protein one consumes seems to be significant (see the evidence around methionine deficient fasting mimetic diets), but I don't think it's overly reductive to say that for most people excess protein in the diet helps drive aging and does more harm than good.
[l5n9pwc] (score 6, diepte 0) Compression socks
[l5mtvv1] (score 5, diepte 2 OP) Raynaud's is when your hands and feet are always cold during winter and don't get proper circulation? I had that since a kid
[l5mz0az] (score 5, diepte 3) yeah, me too! Covid is giving it to some people new and making it worse for those of us who already had it 😔
[l5mtyqx] (score 5, diepte 1 OP) I've heard of pine bark extract before yea
[l5n3ph2] (score 5, diepte 0) Normal
[l5njjwz] (score 4, diepte 4) It increases the blood supply to cancer, potentially. Don’t fuck with it.
[l5nkce5] (score 4, diepte 4) all growth is contraindication with cancer, even a protein shake. It upregulates mtor.
[l5mtrvd] (score 4, diepte 0) Hesperidin or Hesperidin methyl chalcone. Also take grapeseed or pine bark extract.
[l5nvwhe] (score 4, diepte 8) BMI of 15? Have you considered part of the issue is stemming from you being drastically underweight?
[l5mto0y] (score 3, diepte 1) vascular changes at the extremities are common with long covid, also new onset Raynaud’s, neuropathy, capillary constriction, discoloration/livedo/“covid toes”

come to r/covidlonghaulers

anecdotally, flushing niacin helped me a bit
[l5lydws] (score 3, diepte 1 OP) Well didn't have those protruding visible veins at 25. So i guess it worsened. And i won't comment on the breast joke bro. Hehe. It's just a sidefoot with a bit of heel
[l5m24gn] (score 3, diepte 0) Might require compression socks or similar, but recommend speaking to a medical professional first.
[l5nnaj0] (score 3, diepte 3) I personally don’t think pain is the only sign of a vascular issue.
[l5ml98s] (score 3, diepte 0) Look into vitamin k2
[l5ms79g] (score 3, diepte 1 OP) What is it's source? And what form/brand you recommend
[l5nur8k] (score 3, diepte 1) This. Rutin is powerful.
[l5nozmy] (score 3, diepte 1) Confirmed, had this same problem around the base of my penis, amputation completely solved the problem. ✂️
[l5o41ao] (score 3, diepte 2) I think dry brushing can help/massage. Also laying down with your legs up a wall for 5-10mins then stand up and you will feel the blood rush back down. I do this a couple of times if I've been standing alot
[l5p9732] (score 3, diepte 0) I have these to some extent in my feet as well and am also mid 30’s male. I also stand most of my shift at work and walk 10k steps a shift usually. 

More recently I have the appearance of bluish veins in my calves and shins - not varicose and not quite spider veins. I’ve always had vascular legs from being overweight and then becoming lean and doing a lot of running/biking but now these veins are not very aesthetically pleasing. 

I went to a vascular DR. They did some ultrasounds and some exams. Diagnosis- congratulations you’re getting older. Wear compression stockings and we can do sclerotherapy procedure if it really bothers you. I’ve found that angle of lighting like someone else mentioned is a big part of it - I am somewhat fair skinned.
[l6hyy1b] (score 3, diepte 0) I second foot massage. I have those veins too, I mean I had them, it greatly improved after I started massaging them. I do it myself every night. I use any light and fast absorbing moisturizer ideally scent free so to have as less ingredients as possible. I vigorously rub the moisturizer into my feet, ankles and calves, massaging them as best as I can, basically everything down from the knee joint. Then 30 seconds / 1min later I use a kitchen towel to remove excess moisturizer and while doing so I also use the towel in a vigorous rubbing motion.   

The idea is to improve the blood flow and massage as deep as you can. I got this idea from a face moisturizer with snake venom. I bought this moisturizer thinking it was probably a sham but I did feel tingling and burning sensation on my face. Then I started reading why snake venom helps improve the skin and its because it sort of "burns" the skin promoting better blood flow. Then I said I can just massage my face or any part of the body to do that. I also exercise with weights 2-3 times a week, do yoga and some cardio. And I use an intranasal red light device, it helps to break up clusters of red cells and improve the blood flow.
[l5m5pxn] (score 2, diepte 1 OP) Yeah that's what they are. I guess i need to improve my vascular system especially in my extremities
[l5mlufb] (score 2, diepte 5 OP) I walk 5 miles a day.
[l5ngqhx] (score 2, diepte 2) Where do you get them?
[l5nmh5n] (score 2, diepte 3) Lots of options - running stores often carry them. I got one pair of my favorite rainbow heart compression socks from my vasc surgeon and I also bought a pack on Amazon.
[l5nj7ta] (score 2, diepte 3 OP) How is it flawed,.and if it is why is it contraindicated with tumours
[l5mqbt3] (score 2, diepte 0) Honestly it’s a lighting thing.

I noticed the same thing and I freaked out but it’s because my foot was in the right lighting. I made some friends try it and the same thing happened. Don’t worry about it. Your vascular system is fine.
[l5o58fh] (score 2, diepte 2) Shew that was a close one
[l5nggpi] (score 2, diepte 5 OP) It definitely will the following months and years 😭
[l5ne4y0] (score 2, diepte 1 OP) Skin has NOTHING to do with the deep vascular and nervous system in western medicine. They treat everything superficially. In the real body, everything is connected in a holistic manner.
[l5nrwny] (score 2, diepte 0) AKG (AKKG) or another NO provider
[l5pq0ah] (score 2, diepte 0) Really HIIT where you’re pushing your VO2 max and promoting angiogenesis.  Betaine and high polyphenol foods like berries and pomegranates that promote nitric oxide.  Fasting - not like 16-8 but like 72 hrs once a month, to promote chaperone mediated autophagy and clearance of damaged cell tissue.  Cold water immersion.  Anything to increase vascular elasticity.
[l5q2x80] (score 2, diepte 1 OP) Did you try those for your own vascular health? What's your opinion about the controversy on long term fasts?
[l5u93ci] (score 2, diepte 2) I did this stuff for high blood pressure not spider veins but yes and it helped a lot, no longer taking medication.   I personally did 18-6 daily fasting for a long time with one 24 to 36 hr stretch every week.  I would do longer stretches cutting weight.  The big caveat here is that I’d always do one high carb cheat day a week as well.  Other than electrolytes the big concern for me with long fasting was shifting hormonal responses and eventually storing more fat, the cheat day seemed to help with that.  I think we evolved to fast, and it’s a huge benefit if people do it correctly.
[l5rbvf7] (score 2, diepte 8) Yeah. Just find them, train them and you'll be g2g. YouTube reflexology, or find gorigori reflexology. Gorigori uses tools. To dig deeper
[l5lvo4f] (score 1, diepte 0 OP) My grandfather had this but like in his 70s+ not 30s. (I also had a heavy case of covid in 19. Idk if it played a role for peripheral microvascular health....  .
[l5mtp5l] (score 1, diepte 2) Here's a sneak peek of /r/covidlonghaulers using the [top posts](https://np.reddit.com/r/covidlonghaulers/top/?sort=top&t=year) of the year!

\#1: [I Feel This Tweet in my BONES](https://i.redd.it/c81xgzmmhqxa1.jpg) | [82 comments](https://np.reddit.com/r/covidlonghaulers/comments/1371p9g/i_feel_this_tweet_in_my_bones/)  
\#2: [The lack of urgency in finding Long COVID treatments is FRONT PAGE NEWS.](https://i.redd.it/r7vas4fw66lc1.jpeg) | [115 comments](https://np.reddit.com/r/covidlonghaulers/comments/1b1ivmw/the_lack_of_urgency_in_finding_long_covid/)  
\#3: [Six months ago I was 3.5 years into Long COVID and failed to walk next door. Today I successfully ran a half-marathon. Keep going. #longcovidawareness](https://www.reddit.com/gallery/196ouu2) | [169 comments](https://np.reddit.com/r/covidlonghaulers/comments/196ouu2/six_months_ago_i_was_35_years_into_long_covid_and/)

----
^^I'm ^^a ^^bot, ^^beep ^^boop ^^| ^^Downvote ^^to ^^remove ^^| ^^[Contact](https://www.reddit.com/message/compose/?to=sneakpeekbot) ^^| ^^[Info](https://np.reddit.com/r/sneakpeekbot/) ^^| ^^[Opt-out](https://np.reddit.com/r/sneakpeekbot/comments/o8wk1r/blacklist_ix/) ^^| ^^[GitHub](https://github.com/ghnr/sneakpeekbot)
[l5o479f] (score 1, diepte 3) Ginkgo biboba is good for circulation
[l5n7weh] (score 1, diepte 1) And now I can't unsee it 🤣
[l5m5chu] (score 1, diepte 0) These appear to be “spider veins” which are suggested to be damaged capillaries. They are more than likely harmless. If you are concerned or if it gets worse rapidly then go see a doctor.
[l5ml5mx] (score 1, diepte 2) Exercise may help.
[l5ml7yo] (score 1, diepte 3 OP) What kind
[l5mljjg] (score 1, diepte 4) Walking

Leg raise

Lunge

Ankle circles

Calf raises

Running <- Spider veins may not go away with exercise, but physical activity can definitely be beneficial because it eases the discomfort and provides overall health benefits.
[l5pdntw] (score 1, diepte 4) Rebounding.  Also are you wearing high quality shoes for your standing job?
[l5q8dmb] (score 1, diepte 4) Yup and if you notice something, get ahead of it, but safely.
[l5o97e1] (score 1, diepte 3) Amazon, every kind you could imagine
[l5nj1y2] (score 1, diepte 2) that's a flawed question. don't take if you have cancerous tumors.
[l5pqfmk] (score 1, diepte 3) Strong angiogenesis is a risk regardless. At the high end, take the oncogenic effects of cardarine, probably attributable to angiogenesis. You *may* be fine. But if you have the wrong mutation it’s much harder for your body to catch and fix.
[l5mhm38] (score 1, diepte 0) Serrapeptase
[l5osn2k] (score 1, diepte 3) The claim that high-protein diets contribute to aging and inflammation via mTOR activation is a bit over-simplistic. While an over abundance of mTOR activation is linked to growth and aging, it doesn't tell the whole story. Intermittent fasting can induce autophagy, a process that cleans up damaged cells and mitigates the negative effects of mTOR activation.

Research indicates that intermittent fasting, even with high protein intake, can reduce inflammation and promote longevity. Autophagy protects the body against the potential issues of high protein consumption while supporting muscle repair and growth, especially in active or aging individuals. And most of all, this is the historic pathway of ancestral heath.
[l5pnrgh] (score 1, diepte 5) Thank you for mentioning methionine deficient fasting mimetic diets ..googled it ..interesting ...understand a little on the importance of methionine reduction....only knew abt calorie deficits ..what do u advise ..
What does 24 to 48 hrs if fasting on animals scale to in humans's spans ?
[l5pns1m] (score 1, diepte 5) Thank you for mentioning methionine deficient fasting mimetic diets ..googled it ..interesting ...understand a little on the importance of methionine reduction....only knew abt calorie deficits ..what do u advise ..
What does 24 to 48 hrs if fasting on animals scale to in humans's spans ?
[l5prze3] (score 1, diepte 6) In terms of protein intake I'd just try and figure out what's required given your age/gender/fitness goals etc and try not to massively overshoot (a lot of processed foods especially have added protein since people are conditioned to think protein = good).

Re fasting and autophagy, it's hard to make a guess at how that might scale from rodents given the number of factors involved. Personally I think IF is a good idea in general (esp IF where the feeding window is early in the day since that's been shown to increase the benefits likely due to how the circadian rhythm interacts with insulin sensitivity). For autophagy imo it's a good idea to do an extended water fast once or twice a year (potentially more often if you have weight to lose, or preceded by a bulk if you're closer to underweight). Personally I feel like 5-7 days is the sweet spot between likelihood to cause significant autophagy / immune turnover, having relatively low risk for most people, and being mentally achievable for those adapted to shorter fasts / IF.

There's not as much evidence for these specific recommendations as I'd like but it seems in line with the research and what clinicians who recommend fasting practice (eg the Buchinger Wilhelmi clinic). Not too sure about fasting mimetic diets in particular since I've never tried to do one, but both Buchinger Wilhelmi and Valter Longo out of USC sell meal kits for it that one could probably recreate at home from the ingredients (iirc they're crazy overpriced so wouldn't recommend purchasing).
[l5uom6d] (score 1, diepte 3) Could you point to evidence that suggests a higher protein intake is likely to be a causative factor in decreasing longevity? 

Wouldn’t it also be caloric dependent. You can lose or maintain weight and improve body composition on a high protein diet, does that still contribute to systemic inflammation and cardiovascular degradation in that context? Particularly if a higher protein diet helps with their satiation and adherence to better calorie balance

If optimising protein intake (~1.6g per kg/bw) leads to an increase in body composition (more lean mass relative to fat mass), would the aforementioned negative effects outweigh the potential positive effects that consist of improved metabolic health, insulin sensitivity, higher BMR etc?

I was under the impression that as we age we become more anabolic resistant, so wouldn’t higher protein intake be a tool to help older adults improve/maintain their lean body mass, which would help longevity?
[l5uqjbx] (score 1, diepte 4) Been a while since I was digging through papers but this review seems to hit most of the bases: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6562018/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6562018/)

At a high level the thinking is that excess protein keeps your cell metabolism in a growth oriented state (via mechanisms like mTOR activation), which prevents it from spending enough time in a repair/cleanup oriented state. 

Excess calories and fat mass also cause many health problems and reduce longevity, but that doesn't necessarily mean that getting excess protein is a good thing. If the choice is between getting excess calories from refined sugar and excess protein the protein is likely to cause less problems, especially short term. That doesn't mean either one is optimal for longevity though.

There is some evidence that increased protein for elderly adults can help reduce frailty and do more good than harm, but for adults between full development and around retirement age excess protein isn't beneficial (was assuming there aren't many 70 year olds reading my comments).
[l5uuu60] (score 1, diepte 5) Cool thanks for the link, I will have a read! 

With your second paragraph, you mention excess protein keeps the cells in a growth state, but is this still the case with when you are consuming a high protein diet in the context of a caloric deficit? A weekly calorie deficit increases your overall rate of weekly autophagy, as does other things such as exercise. So you could still consume high protein but still be in a catabolic state. 

If you don’t get excess calories from protein then you have to get excess calories from another macronutrient (assuming we’re controlling for calories here). That means from carbs (which all eventually get broken down to glucose) or fats (which are more easily stored as bodyfat, since your body doesn’t need to go through a complicated process to convert them to lipids). Protein also has a potential positive where you burn more energy breaking it down then carbs/fats (thermic effect of food). 

So what would you replace excessive protein with, fat or carbs? 

Personally I think the problem lies in the whole excess in the first place, rather then a particular macronutrient
(49 reacties met lagere score weggelaten)

=== THREAD 1sdeoa4 ===
SUBREDDIT: r/Biohackers
DATUM: 2026-04-05  SCORE: 555  REACTIES: 89
TITEL: A bacterial infection from cat scratches can cause brain fog, rage, insomnia, and foot pain for years. Nobody tests for it.
POST (source_id=post):
Bartonella henselae. The bacteria behind cat scratch fever. 15 to 40% of cats carry it depending on age and flea exposure. Most doctors think the infection is mild and self-limiting. In some people it isn't.

It's an intracellular pathogen. Hides inside red blood cells and the endothelial cells lining your blood vessels, including the ones in your brain. Your immune system can't see it properly. It sits there causing chronic neuroinflammation for months or years.

Edward Breitschwerdt's lab at NC State has been documenting this for over a decade.

The research:

A 2019 case study: a boy developed sudden psychosis and seizures from confirmed Bartonella in his blood. Treated with antibiotics. Resolved.

A 2024 review from his lab called Neurobartonelloses: emerging from obscurity catalogued the full neurological damage - encephalitis, peripheral neuropathy, cerebral vasculitis, psychiatric symptoms including psychosis.

A 2024 study from Columbia and NC State tested 116 people. Patients with psychotic disorders were three times more likely to have Bartonella DNA in their blood than healthy controls (43% vs 14%, p=0.021).

A 2021 pilot study at UNC and NC State found the same thing. 65% of schizophrenia patients had Bartonella DNA, 8% of controls.

Two independent research groups. Two separate patient populations. Same result.

Why testing misses it:

Standard testing is an IFA antibody test. But Bartonella hides inside cells and your immune system may never mount a detectable antibody response. The Columbia study proved this directly — the antibody test could not distinguish patients with psychosis from healthy controls. The PCR could. Same blood, same patients, different test, different answer.

A negative IFA does not rule out Bartonella. It rules out a detectable antibody response. Those aren't the same thing.

Better tests: enrichment PCR or droplet digital PCR (ddPCR). Most doctors have never heard of either. You have to ask.

The symptom pattern:

* Brain fog that started suddenly, not lifelong
* Rage or irritability that doesn't fit your personality
* Anxiety or panic that SSRIs don't touch
* Insomnia — the wired kind, not the tired kind
* Unexplained foot pain (endothelial inflammation and peripheral neuropathy)
* Linear raised marks on shins or thighs (look at your legs)
* Headaches that track the same timeline

Any one of these means nothing. Four or more with cat or flea exposure warrants testing.

The antibiotic clue nobody talks about:

If you've ever taken antibiotics for something unrelated  dental infection, UTI, sinus infection and your brain fog temporarily improved, that's meaningful. Random antibiotics can partially suppress Bartonella. Most patients and doctors read this as evidence that the dental issue was the problem. It can also be evidence of a bacterial cause hiding underneath.

Treatment:

Chronic Bartonella requires targeted antibiotics for weeks, not days. The specific drugs and duration vary by species, severity, and individual response. This needs a doctor familiar with intracellular infection protocols. Herxheimer reactions (feeling worse before better) are common as bacteria die off.

Conflict of interest note:

Breitschwerdt co-founded Galaxy Diagnostics, one of the labs offering enrichment PCR. He discloses this in every paper. The conflict is real. The data is also real. The Columbia team is independent. Read the disclosures and make your own call.

What to ask your doctor:

* Enrichment PCR (BAPGM) or ddPCR testing, not just IFA
* Cat scratch history, not just "do you have pets"
* Whether any prior antibiotic course coincided with symptom improvement

Bartonella isn't responsible for every case of brain fog. It's worth checking when the symptom pattern fits and the fundamentals have already been addressed.

**SOURCES COMMENT:**

* Breitschwerdt EB et al. Bartonella henselae bloodstream infection in a boy with PANS. J Central Nervous System Disease. 2019. DOI: 10.1177/1179573519832014
* Lashnits E et al. Schizophrenia and Bartonella spp. Infection: A Pilot Case-Control Study. Vector-Borne and Zoonotic Diseases. 2021. PubMed: 33728987
* Bush JC, Robveille C, Maggi RG, Breitschwerdt EB. Neurobartonelloses: emerging from obscurity. 2024. PubMed: 39369199
* Delaney S et al. Bartonella species bacteremia in association with adult psychosis. Frontiers in Psychiatry. 2024. DOI: 10.3389/fpsyt.2024.1388442
* Breitschwerdt EB et al. One Health Zoonotic Vector Borne Infectious Disease Family Outbreak Investigation. Pathogens. 2025. DOI: 10.3390/pathogens14020110
* Breitschwerdt EB et al. Bartonella Associated Cutaneous Lesions in People with Neuropsychiatric Symptoms. Pathogens. 2020. DOI: 10.3390/pathogens9121023

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[oei8hbo] (score 98, diepte 0) If you've had or think you've had cat scratch disease, you should also get a dilated eye exam. It can mess with your retina too and can lead to vision loss.
[oei4dmd] (score 52, diepte 0) 🎙️ CAT SCRATCH FEVAAA
[oei9w6m] (score 46, diepte 0) There is a somewhat famous researcher from Italy, Dr. Tarello, that researches these CFS-like symptoms from bacterial origin, which are transmitted by animals. You're talking about a specific strain, Bartonella, but there are others.


Tarello's proposed treatment is, and I kid you not, low dose arsenic-based therapy. In fact he treated himself with it, when he contracted this illness from the sick animals he used to handle.
[oei2vv8] (score 33, diepte 0) I suspect I have Bartonella. Is there a way I order this test on my own? I doubt my doctor would order it.
[oeid86o] (score 20, diepte 1 OP) She was always just misunderstood :(
[oei6mlm] (score 19, diepte 1 OP) I am working on building a resource on r/whatisbrainfog that will find this out and document it for free, bare with me.
[oeid0d1] (score 19, diepte 0) So the crazy cat lady trope isn’t unfounded 🤔
[oeia8s5] (score 18, diepte 1 OP) It's a far more complex science than people would like to believe, there should be more coming out about it in the next 10 years.
[oeivv2h] (score 16, diepte 1) Look for doctors that treat Lyme disease, specifically llmd. They have the most experience with bartonella, since sometimes it’s comorbid with Lyme disease.
[oeibqqp] (score 16, diepte 0) Thanks for sharing your work with us here.
[oei1bdg] (score 15, diepte 1 OP) I have personally had this and gone through this and it changed my life.
[oejehji] (score 14, diepte 1) If they decline to order a test, ask them to please document in your chart your concerns and that they are declining to investigate further. That will change their tune real fast.
[oei97wg] (score 14, diepte 1 OP) Never thought of that, thanks for the input.
[oeitq1u] (score 14, diepte 0) It’s really a tricky disease. I tested positive from it and I am almost certain i got it from a bad scratch from a feral cat years before. It was part of a LYme coinfection panel. There is a book by a LYME DR in NY called Why cant I get better? And in it it has a list of symptoms that match my nerve issues that I developed in the past few years. It does go dormant but still shows up on my tests and I don’t know what to do about it but I’m kinda suspecting my nerve symptoms-twitches and spasms were caused by it.
[oej5w2u] (score 13, diepte 0) did you know it has been shown that living with a cat can put you at higher risk of gaining schizophrenia? very fascinating stuff
[oeic4eh] (score 11, diepte 1 OP) Thanks for your kind words. It really does mean a lot to me.
[oei4rs5] (score 10, diepte 1 OP) I am sure there are sites online but I have not tested the best one, so I can't really say. You can tell your doctor you have been exposed to cat scratches and show him this article, it is pretty solid medically.
[oelv656] (score 9, diepte 1) Arsenic actually saved my life.  

I had acute promyelocytic leukemia and one of the standard treatments is arsenic trioxide + ATRA (vitamin A derivative).  

Classic Paracelsus: the dose makes the poison.
[oej37g4] (score 9, diepte 0) I had “cat scratch fever” from a feral cat when I was 11. Had to have surgery and my lymph nodes are all screwed up to this day (I’m 50). It’s no joke. Have had a lot of weird health issues since.
[oei2otk] (score 8, diepte 2) Thank you for posting this 🙏🏻
[oej71ov] (score 8, diepte 2) Happened to my kid. Permanent black spot on his vision.
[oen6f7o] (score 8, diepte 4) lol ... yeah the huge team of eye doctors and infectious disease specialists were all wrong (along with the months of medications and endless eye exams).
[oeicoyp] (score 8, diepte 0) Is this same you can get from ticks?  If so I believe there is a test but I’m not 💯.
[oejuyxx] (score 8, diepte 0) If told my doctor to test me for this he would look at me like I was insane. Not a chance would he take me seriously… 😔
[oei2wxe] (score 7, diepte 3 OP) My pleasure. I wrote a really long story and then people told me it's too long so I am going to keep my posts concise and to the point. I get carried away sometimes.
[oeidgjk] (score 7, diepte 1 OP) There's evidence Bartonella can also be tick-borne, but the evidence is debated. My exposure was clearly cat related so that's what I focused on.
[oeihui6] (score 7, diepte 0) I'm in the process of being tested for this along with Lyme and various others. My doctor suspects long COVID + maybe some other underlying infections. I had no idea cat scratch fever was a thing until they mentioned it a few weeks ago. I grew up with cats and got scratched up really badly by a barn cat when I was about 9 so we'll see...
[oeiid5s] (score 7, diepte 1 OP) Keep us updated. This is I believe one of the most important posts if people take decide to spread it.
[oei6ab6] (score 6, diepte 0) How can i be tested for these in france, doctors seems to don't know about 90% of tests that exist.
[oeibu80] (score 6, diepte 0) CAT SCRATCH FEVER IS REAL OMG WHAT
[oeild1o] (score 6, diepte 0) If I have to go I want it to be Mr. Fluffykins who takes me out
[oepzdit] (score 5, diepte 2) there is also toxoplasmosa, which can be acquired from cat feces. there is a lot of rabbit holes to go down foe the curious, but it leads to risky behavior in humans, and 4/5 motorcycle crash victims are purported have toxoplasmosa. in mice, it causes even more bizarre behavior: mating near cat urine
[oej2bj8] (score 5, diepte 0) Excellent post, thank you very much for sharing your research.
[oeietsp] (score 4, diepte 1) I liked Strangle Hold.
[oeiccqi] (score 4, diepte 1 OP) Tip of the iceberg. There seems to be a lot of information doctors may have missed. Hope these articles can help them and all of us.
[oeihh5s] (score 4, diepte 0) Are you familiar at all with /r/POIS? What are your thoughts about it? 

I personally experience somewhat debilitating brain fog, as most do, starting day 2 and 3 after orgasm. Can come and go and can last for a couple days to weeks for some.
[oeik518] (score 4, diepte 2) Will do. Thanks for posting this, it's super helpful.
[oeittoj] (score 4, diepte 0) In case someone tests positive, do antibiotics not completely clear the bartonella from the body? Which antibiotic is the appropriate one?
[oeiv3vn] (score 4, diepte 0) Here is the test company my Integrative Dr used. It was a test panel with all the co-infections included; Bartonella, Babesia, Burgdorfi etc. https://igenex.com/test-directory/
[oela34x] (score 4, diepte 0) Fantastic and generous post, OP. I self-diagnosed some years ago. I had a small pea sized lump/bump on the side of my face near the ear, which can be a tell. Had terrible fatigue. A few weeks before that, my cat got one claw into an old closed pierced-ear hole (same ear). I sent my doctor info so she took me seriously and prescribed a couple weeks of antibiotics, which seemed to take care of it (I hope).
[oejh4kp] (score 3, diepte 1) Most primary care doctors can easily order this blood test.
[oeqpzlh] (score 3, diepte 2 OP) Some say it's the future of medicine and some say it is hocus pocus. I think most people are afraid of coming out and saying what works for them because science doesn't have specific citations. This is something I have also studied for a few years but patience is a virtue.
[oeii7cy] (score 3, diepte 1 OP) i am not but this is something I will research and come back to you on. Never even knew this was a thing, sorry you are all hurting over there. This might become a new category on the site r/whatisbrainfog  if there is demand for it.
[oek1w01] (score 3, diepte 0) I have pains all over (diagnosis is fibromyalgia) that come and go and a persisting foot pain. I was scratched by different cats several times in the past 25 years.

My fibro(?) pain gets a bit better when I take amitriptyline (tricyclic "antidepressant"). Would amitriptyline improve things in this way, for someone with bartonella henselae?
[oepm4tn] (score 3, diepte 0) I got scratched by a feral resort cat when I was in Jamaica years ago, and a few years later developed insomnia that resolved on its own eventually, anxiety, and then somewhat sporadic foot pain (both feet) and now hands...
[oei9t0z] (score 2, diepte 1) Immunologue!
[oel0k0n] (score 2, diepte 3) Did they also use a blood test to confirm?  Ty
[oemcmfa] (score 2, diepte 4) It is most likely macular degeneration due to toxoplasmosis.
[oeic4l7] (score 2, diepte 2) You have awarded 1 point to Hi\_there4567.

---

^(I am a bot - please contact the mods with any questions)
[oeicl44] (score 2, diepte 0) ![gif](giphy|lnCggcJbfrY8E)
[oeik5ck] (score 2, diepte 2) Hello Sureokgo,

You have been awarded a point for your contribution! New score: 14

---

^(I am a bot - please contact the mods with any questions)
[oeivjbj] (score 2, diepte 0) Following your project for updates
[oej2ewf] (score 2, diepte 1 OP) Thank you, sharing is caring please pay it forward.
[oej2f36] (score 2, diepte 2) You have awarded 1 point to cavaillon\_666.

---

^(I am a bot - please contact the mods with any questions)
[oej2f5d] (score 2, diepte 1) Hello cavaillon\_666,

You have been awarded a point for your contribution! New score: 1

---

^(I am a bot - please contact the mods with any questions)
[oelss5v] (score 2, diepte 1) It is most likely due to either bartonella or toxoplasmosis
[oejzw9i] (score 2, diepte 0) Crazy cat lady is a meme for a reason...
[oek8810] (score 2, diepte 0) Could this cause uveitis? My cat tested positive for Bartonella exposure and I developed PIC / MFC with anterior uveitis with a year 

Also — would hospitalization with constant IV antibiotics (Zosyn) for 2 days kill Bartonella? I was recently in hospital so hoping the Zosyn killed two infections with one stone :)
[oekg2xc] (score 2, diepte 0) How bad can it mess up with the eyes? My doc thinks I have Uveitis, but no indicators showing that it could be Uveitis. That's what he currently thinks. 
I also have stretch marks on my body that don't really look like stretch marks, and they often disappear and get back. 
I was badly scratched from a Kitten as a Kid, and then again 2 years ago from a stray cat. But I have all kind of problems, from gut, pain, fatigue, and eyes. And the gut and eyes are really messed up.
[oel6mip] (score 2, diepte 0) >Linear raised marks on shins or thighs (look at your legs)

Does this mean something else specifically, or is it just AI babble for "hmm yes a cat scratch may be a scratch from a cat"
[oeogodd] (score 2, diepte 0) I actually had Cat Scratch Fever for a year when I was in preschool because they could figure out exactly what was going on me with, got me over my fear of blood work at a young age having it tested weekly. My lymph nodes stayed swollen and hurt and to where I never wanted to eat. When they finally sent me to a specialist the doctor literally looked at my mom and said do you have a cat she said yes he said get him declawed fully. Never have got sick from a cat scratch sense but also have never read things that could lie dormant or the effects years later.
[oeqm289] (score 2, diepte 0) Wow, thank you for the information!
[of4l5nn] (score 2, diepte 0) Whats the name of the test/how can i test for it?

Im 35 now. When I was 16 I was scratched and still have a pimple there.

Always thought I have adhd and insomnia. Would love to find out if its something else
[oehz8oz] (score 1, diepte 0) Welcome to r/Biohackers! A few quick reminders:
- **Be Respectful**: We're here to learn and support each other. Friendly disagreement is welcome, but keep it civil.
- **Review Our Rules**: Please make sure your posts/comments follow our guidelines.
- **You Get What You Give**: The more effort and detail you put into your contributions, the better the responses you’ll get.
- **Group Experts:** If you have an educational degree in a relevant field then DM mod team for verification & flair!
- **Connect with others**: [Telegram](https://t.me/biohackerlounge), [Discord](https://discord.gg/BHsTzUSb3S), [Forums](https://biohacking.forum/invites/1wQPgxwHkw), [Onboarding Form](https://go.meiro.cc/0721334)

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Biohackers) if you have any questions or concerns.*
[oejasqq] (score 1, diepte 2) Stranglehold literally has a stranglehold on me
[oeo0vxf] (score 1, diepte 1) Got it from the kitty next door
[oei986t] (score 1, diepte 2) You have awarded 1 point to Treefrog\_Ninja.

---

^(I am a bot - please contact the mods with any questions)
[ofhk96f] (score 1, diepte 1) Hey

I used to get scratched almost every other day by feral cats as a teen, I had eye exam and they found scarring from what they assume is either genetic or from previous viral infection. I don't have vision issues but would love to know more about this. It has been like 10 years since i had cats not sure if i shoul worry about it. What is the treatment?
[ofmqm5q] (score 1, diepte 1) That is wild. More people should be informed about these.
[oeic4ni] (score 1, diepte 1) Hello Hi\_there4567,

You have been awarded a point for your contribution! New score: 1

---

^(I am a bot - please contact the mods with any questions)
[oeik5aq] (score 1, diepte 3) You have awarded 1 point to Sureokgo.

---

^(I am a bot - please contact the mods with any questions)
[oejsans] (score 1, diepte 1 OP) Thank you. Looking forward to your feedback on it.
[oejscjh] (score 1, diepte 2) You have awarded 1 point to The-Beautiful-Baku.

---

^(I am a bot - please contact the mods with any questions)
[oejscl6] (score 1, diepte 1) Hello The-Beautiful-Baku,

You have been awarded a point for your contribution! New score: 1

---

^(I am a bot - please contact the mods with any questions)
[oejv87b] (score 1, diepte 1) Lol ya was thinking this
[oek98tn] (score 1, diepte 0) Cat scratches are the leading cause of cat scratch fever.
[oel8ied] (score 1, diepte 2) Thanks, but that returns many different symptoms, most of which do not fit the description. Are you referring to anything specific?
[oel8ij8] (score 1, diepte 3) You have awarded 1 point to Sureokgo.

---

^(I am a bot - please contact the mods with any questions)
[oelcuzq] (score 1, diepte 4) OK thanks
[oeld3h3] (score 1, diepte 5 OP) Yeah I wish I could write a blanket super article that applies to everyone and cures all but not possible.
(16 reacties met lagere score weggelaten)

