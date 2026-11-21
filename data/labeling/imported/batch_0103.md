# Label-batch batch_0103

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
Schrijf het resultaat naar `batch_0103.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1orjfip, 13gw9j5, 1dgr65b).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1orjfip ===
SUBREDDIT: r/travel
DATUM: 2025-11-08  SCORE: 145  REACTIES: 249
TITEL: How do you travel with someone with plantar fascitiis?
POST (source_id=post):
My partner has plantar fasciitis and just wants to relax in general. He doesn’t plan any of our vacations so I do, but then he complains whenever we’re on sightseeing. He asks me constantly «when’s the next bench? When does this end?» and it irks me because it’s my first time in the area as well. 

I keep on telling him to sit down whenever there’s a bench and go out of my way to find seats for him on bus and trains (while I stand),  but sometimes he’ll walk anyway and then he complains that he tried to walk until it hurts and then he’s grumpy. 

Most of the time he wants to stay at home gaming. That’s fine; but I want to actually experience the country I’m in and I don’t need him with me. But still, he wants to join sometimes and every time he does, it’s making me miserable. He thinks it’s a me problem because don’t understand that people want to relax on vacation. 

How do you guys solve this type of dilemma?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nnqgu5f] (score 1033, diepte 0) >How do you guys solve this type of dilemma?

You might not want to hear this but I think it's really simple: You stop travelling with him. You travel solo until he gets the plantar fasciitis solved.

I am a maniac walker and when I got hit with plantar fasciitis it absolutely destroyed my ability to travel. I had never been so debilitated in my life. It was horrible.

But, I saw some great doctors, updated my footwear and I'm 100% cured. I'm back to my usual 20,000+ steps per day with zero issues.

Good luck to your partner getting this cured. It's not going to happen simply complaining about it though and playing video games...

Good luck.
[nnqiyvv] (score 305, diepte 0) Sounds like this doesn't have that much to do with his plantar fascitiis. You guys just have different travel styles and interests. 

I think you need to just go alone.
[nnqtgtv] (score 255, diepte 1) I agree with this completely. Plantar fasciitis is very manageable, and while the appropriate shoes can be pricey, they are worth every penny in order to be able to live life the way I want.
[nnqrfiy] (score 173, diepte 1) She wants to travel and he wants to go on vacation
[nnqg5n5] (score 103, diepte 0) Get him to go to see a physio and try to get rid of the plantar fasciitis. I get it on and off and it responds to calf strengthening exercises done consistently (for me… he should see a PT to check his issue is the same). Game changer to be able to get rid of it! Comes back every time I slack on the exercises for a few months…

Tbh I actually find plantar fasciitis is comparatively fine if walking and staying moving, it’s when you’re standing still eg in a museum that it’s an absolute bitch.
[nnqk20k] (score 98, diepte 0) I don’t actually think this is a plantar fasciitis problem tbh—I think there’s a difference between people who like to travel and people who like to vacation. It sounds like you want to sightsee and enjoy the culture of the country you’re visiting, and your husband sounds like someone who’s better suited for sipping on a coconut at a beach resort in Bali or something.

I’d personally split up—you only have so many vacations in your lifetime. If you want to see the world, you should go see it, and maybe your husband can get himself to a resort at the same time so you guys can both enjoy your ideal vacation.
[nnrsb3g] (score 87, diepte 3) Physical therapist here; plantar fasciitis can also be prevented to some degree by doing regular stretches.
[nnqgf6j] (score 78, diepte 0) leave him at home/at the hotel. you aren't attached at the hip, you can each do your own thing
[nnrjsg7] (score 57, diepte 2) Yes it is but it takes time.  Sometimes months.
[nnr86x7] (score 54, diepte 1) This!!!

I had plantar fasciitis as well and it’s completely cured. Completely gone!!! 

This is a manageable thing, SO doesn’t want to do the work to manage it, they’d rather stay in pain and miserable
[nnqk6wp] (score 49, diepte 1 OP) You might be right! I think he’s possibly using the condition as an excuse when the fact is he doesn’t like certain activities I’ve planned, like sightseeing.
[nnqfmv8] (score 33, diepte 0) Travel without them.
[nnqu4mu] (score 30, diepte 0) I don’t think this has anything to do with plantar fasciitis. That’s just the excuse he is using because he doesn’t actually want to do/enjoy the activity (regardless of the pain) but has some sort of FOMO about you doing it without him. I’m suggesting this because I have a friend who sounds exactly like your husband and after several trips that were just ruined by their constant whining and us confronting them they admitted that they hate the idea of the holiday but hate the idea of missing out more. 

I’d suggest travelling without him, or booking a resort where he can stay there all day and you can go out and adventure. 

You also do have to consider if there is a more nefarious intention behind this because expectations from a partner should be different to a friend - is he coming along to ruin it for you because he doesn’t enjoy it and also doesn’t want you to? It may not be as conscious a decision as that but the reality is all of us sometimes go and do something because our partner enjoys it and we want to see them happy - going along and complaining about it and making it miserable isn’t really in the spirit of that.
[nnralqd] (score 27, diepte 2) You won't believe what cured mine... after 18 months of different shoes, stretching, massage, ice, socks, etc., I went cross-country skiing on several longish outings during the month of February, and otherwise do nothing else and I average over 10k steps every day with no pain.
[nnsd8pc] (score 25, diepte 5) I found "chicken catchers" to work great. ([Like this ](https://youtube.com/shorts/abVn7ViRV-U?si=qh6yBwvl4TtUYKUB)but you need to go at half the speed). 

Also [wall calf stretches ](https://www.youtube.com/watch?v=f1HzSAuB-Vw)are really good. 

You should stretch every day and also before and after doing any walking. Shoes also make a huge difference. Go to a **real** running store and get fitted for shoes that match your gait.
[nnrc63f] (score 23, diepte 2) For me it took PT, icing, and never walking barefoot or in shoes without good support or my orthotics again, even at home. Plus slowly ramping up activity - no more long early spring walks after an inactive winter. 😄
[nnsduhx] (score 21, diepte 2) TBH OP's bf doesn't sound like they're actually interested in participating in the trips that they want to take. Especially if they're saying something like "vacations are supposed to be for relaxing" and would rather stay home playing video games than experiencing new things with OP.
[nnr3217] (score 19, diepte 2) For me, it was shockwave therapy and that stupid sock.

i was already in supportive footwear when it started.
[nnsfqi7] (score 15, diepte 7) Unfortunately shoes make a big difference. I do a lot of walking around outdoors on sidewalks, so I have to replace shoes every 6 months. I can tell when it's time to get new ones because my feet and hips start to hurt.
[nnqtkej] (score 15, diepte 1) Mind if I ask what your treatment regime is besides supportive footwear?
[nnrmuwi] (score 14, diepte 3) Now is a good time to start. Most people take months between trips anyway.
[nnsf5ak] (score 14, diepte 5) Definitely calf stretches - do them a few times a day and ideally for the first time before you get out of bed. Also roll your feet with a physio ball (or ball hockey ball, etc). When you hit a spot that's particularly sensitive, stay there and bend your foot around it. 

Look into physio exercises to strengthen your foot muscles, especially in your arch. For example, one is to "walk" barefoot across a room but only move your legs by scrunching up your toes/arches to kind of inchworm your feet along. It's a bit hard to describe.
[nns1ng5] (score 14, diepte 2) Same. 4 weeks in a boot, custom inserts in my shoes. Never had a problem again (15 years now)
[nnr4e3h] (score 12, diepte 2) Yep. As you get older, traveling with one injury or strain or another becomes the norm anyways, and people need to learn to manage it for themselves and of course advocate for what they need with their travel partners. But it’s no one else’s job. I’ve done dozens of trips with various injuries or maladies (late 30s).
[nns3j07] (score 11, diepte 4) Any that you recommend? I’ve been hit with PF for the first time in my life this year.
[nnqfgxd] (score 10, diepte 0) What about those hop on / hop off tour buses or a guided bike tour?
[nnqmrkm] (score 10, diepte 1) Yeah this is true, I currently have it myself. The condition is worst after you wake up or stay still for a longer duration. Completely fine when you move a bit.
[nns0o1p] (score 10, diepte 3) Oh no! I shouldn’t do that thing that’s worth doing because it takes time!
[nnr891y] (score 10, diepte 2) I went to PT, did exercises, and had soft tissue manipulation.
[nnrkaa6] (score 10, diepte 2) For me, it was constantly pushing my feet into tennis balls (self massage), stretching my calves using a few different stretch positions, and gradually increasing my walking distance. I have switched to a hard rubber spiky ball used for massage now, and it's better than the tennis ball. Other things that might help are home ultrasound devices and red light therapy. You have to make sure not to over-do either of those two therapies to get the best results.
[nnqlslb] (score 10, diepte 0) You can 💯 cute this with physiotherapy. He should spend the money and get his life back.
[nnrordt] (score 9, diepte 4) I have had great luck with Powerstep Insoles: 
https://powerstep.com
[nnqs6m2] (score 9, diepte 1) Exactly. He's just different (wanted to say lazy but people really ARE different). I got plantar fasciitis too and I'm able to travel and walk and whatever. (I got special socks too, and exercises. And I'm "good" with pain.)
[nnqgcos] (score 8, diepte 0) You do not travel with someone who is in physical pain.
[nnsdqk3] (score 8, diepte 6) Yes, obviously there are stretches “all over the Internet”. That’s why I asked the person who said they were a PT for any specific recommendations they may have. Glad you were able to pick yourself up by your bootstraps or whatever. Happy for you.
[nnr6oka] (score 8, diepte 2) In addition to footwear, we got some runner rugs to cover the main paths across our tile and hardwood floors, with extra padding underneath. Before that I had to stop walking barefoot for a while.
[nnrjbid] (score 8, diepte 2) This!!!
[nns7mee] (score 8, diepte 1) I thought this too. Even if he gets his pf under control (mine was brutal but was thankfully instantly cured with hard inserts from a podiatrist), it sounds like he might just prefer a more leisurely travel style. Have you ever traveled with friends? It could be nice to find people to go with so you each can have a buddy with your energy!
[nnqjp2f] (score 8, diepte 0) I went to an old school podiatrist for my PF.  He taped my foot up and omg - instant relief!  By that I mean, the non stop throbbing - stopped.  In a couple weeks, the inflammation was noticeably less, and my activity capacity way improved.

The podiatrist let me know my problem was structural and would keep recurring (fallen arches, loose tendons).  I could continue taping as needed or get custom lifts.  However, surgery would only temp address the problem, and ultimately scar tissue would likely make it worse, because of the looseness of the tendons themselves.  

I didnt really like taping up the foot every day and the long term cost was larger than the initial up front cost for the lifts, so went with the custom lifts.  I can take them in and out of my shoes, so dont have to buy expensive ortho shoes - regular lace up sneakers with a wide toe do just fine.

That was 4 years ago.  The lifts are still doing their job and I wear them every day.  I miss going barefoot or wearing comfy slippers - but the feet can easily jog a couple miles.  I did a lot of repair work to the eaves soffits and roof of our house this summer - all ladder or angled roof work.  Had to monitor that carefully as pitched inclines can bring back the PF.  But 4 years ago, I could barely do grocery shopping so all in all, I feel a bit like I won the mobility lottery.
[nnrj4ni] (score 8, diepte 0) SOLO TRAVEL!
[nnqg28t] (score 7, diepte 0) I hope that he is seeing a podiatrist to address his plantar fasciitis.  It really limited my ability to do anything.  Have you tried doing bus or Segway tours?  I love the walking and getting lost part of travel, so you should try to have just few hours each day where you get to solo adventure.
[nnr13yg] (score 7, diepte 2) Given it's only been a year did he enjoy sightseeing before then? You need to decouple his health issues from his travel preferences.


A person who loves to travel but is limited by solvable feet problems would be absolutely gutted and very motivated to address this ASAP. 


From what you're saying it doesn't seem like your partner is that person.
[nnrs3il] (score 7, diepte 2) "He didn't have this issue before we were married."

Now, now he is developing ways to control who dosthe chores. This is not a travel problem. This is a problem with people who change the rules after marriage. Good luck.
[nnrlkbd] (score 7, diepte 2) Oh look we have a Redditor who knows better than a doctor!
[nnqgob4] (score 6, diepte 1 OP) He has been seeing a physician and physical therapist and gotten special shoes. I even took him to a shoe store to get him special shoes during the trip. 

We also brought a hiking chair with us so that he could sit whenever. But he just seems so unhappy throughout it, and even when he’s sitting he’s like «when is it done? I’m in pain». 

It’s really hard to enjoy a vacation this way. I left him in the hotel in the morning, and we met up for lunch and he joins me for activities until dinner but still he complains whenever we walk. We also had three days where he stayed at the hotel gaming… I’m not sure if there’s any point in going on vacation together then?
[nnsgl1u] (score 6, diepte 7) You're welcome! I know it can be annoying to keep up with these little physio exercises but they really work if you give it some time.
[nnt5q9l] (score 6, diepte 5) Tight calves are a sneaky source of pain, so calf stretches and using a tennis ball or other massage ball to roll out the trigger points. Use that same ball to roll out your foot as well, but be gentle if the PF if flaring up. 

Don’t be walking around your house barefoot, invest in some house shoes like Birkenstocks or recovery slides like Hoka Oras. It’s especially important when I’m cooking in the kitchen or doing chores around the house to be wearing something supportive. 

Voltaren is a topical anti-inflammatory pain reliever that’s available OTC in the US now. You’ve got to apply it a few times a day, but you’re basically massaging your foot to apply it, so that really helps out. I like to use gloves to apply since I don’t need the pain reliever for my hands. It’s not something that I need all the time now, but I always keep some on hand.
[nnt3sar] (score 6, diepte 4) And the other!!!
[nns4dpp] (score 5, diepte 2) So, beyond plantars fasciitis, I have severe leg damage from being hit by a car, arthritis in my knee, and sympathetic pain in my legs/hips/back from walking with a limp. In short, I'm a mess!

You know what *never* happens when I'm on vacation? I never whinge at my partner about "how much longer?" I don't complain endlessly about my pain levels, and I try very hard not to let my disability be the focus of our days. I do my stretches, I wear my orthos, I bring a cane in case I need it, I take painkillers before we leave the hotel and bring some to take later on. When we wrap up for the day, I soak my feet in ice water, maybe scam a massage from my husband if it's really bad.

For your husband to be foisting his share of the domestic labour onto you over plantars fasciitis is mental. If it is *that* debilitating, that he can't even do his share of housework, how does he hold down a job? 

You say he is going to physio; is he doing the exercises every day? Icing his foot? Taking anti-inflammatories? Does he have night splits/braces? After a year (which is abnormally long for an active P.F. flare-up), what are his doctors/therapists saying? Is he a candidate for steroid injections or even surgery? If it isn't getting better after a year of consistent treatment, he may need more serious intervention.

My guess is that he's being lazy with following his treatment plan. He doesn't *want* to do housework or take long walking adventures. He would rather sit on his ass playing games. Having a pain issue gives him a pass to be a layabout. Personally, I would plan a solo trip full of walking and use the time to consider this whole situation. If this is how he handles a nerve inflammation, what kind of partner will he be if he has a more serious injury or ailment? What if *you* became incapacitated or ill for an extended period of time? Would he step up the same way you are, and shoulder all of your domestic duties without complaint, or would he complain about how hard it is as your house became a disaster zone?

You're right to be questioning why you two are even vacationing together if this is how it's been for a year, with no end in sight.
[nnu02vb] (score 5, diepte 4) My wife's physical therapist did \*all\* the necessary work to get rid of her plantar fasciitis - including teaching me how to tape her foot for one of our vacations. That taping did a world of good for her on that trip - I was skeptical at first, and then amazed
[nnrt98u] (score 5, diepte 7) Yes I tried that method it’s just gotten worse lol
[nns3wij] (score 5, diepte 2) I didn't see why she should be restricted to group tours. 

She's an experienced traveller, she can figure out the solo aspect on her own.
[nnsf1tz] (score 5, diepte 3) That!!!
[nntbiey] (score 5, diepte 2) I'm a gamer who loves to travel. It's not a correlation
[nnqlr7l] (score 5, diepte 1 OP) Yeah. He doesn’t give any input during the planning process, and he doesn’t suggest that he and I should have separate vacations but I think that’s the best way forward.
[nnr6gsg] (score 5, diepte 0) Leave him at home. If he insists on going, plan for him to stay at the hotel or do things he is willing to do while on his vacation. In the meantime, live your best life.
[nnqk35h] (score 4, diepte 3 OP) That’s beyond the point .. we’re done with the vacations.
[nnqg8ci] (score 4, diepte 0) Does he do any stretches and wear a plantars fasciitis brace to sleep? When I get flare-ups, stretching a couple of times a day and wearing a brace to keep my toes from pointing down when I sleep, make a *huge* difference. Quality walking shoes are essential. Maybe he could consider getting fitted for orthopedic insoles for P.F., too.

If he doesn't want to manage his pain levels and just wants to relax at the hotel all day, you guys might be happier splitting up for part of the day. You don't need to drag him along if he's just going to make things miserable. Have breakfast together, you go off and have an adventure, and you two can meet up later in the day or for dinner.

But he really should do the work and make the small investment into taking care of his foot pain. There's no need to be suffering the way he is.
[nnseaud] (score 4, diepte 6) Thank you! I haven’t tried the chicken catchers yet, so I’ll have to add it to my routine. Wall calf stretches and calf raises have been the most helpful of what I’ve tried for sure. You’re absolutely right about the shoes. I know my sneakers are falling apart at the seams, but trying to save up for a good pair gets harder and harder.
[nnsfl4j] (score 4, diepte 6) Thank you so much this is incredibly helpful!
(204 reacties met lagere score weggelaten)

=== THREAD 13gw9j5 ===
SUBREDDIT: r/solotravel
DATUM: 2023-05-13  SCORE: 172  REACTIES: 186
TITEL: What 1 pair of shoes work the best for the solo traveler/backpacker?
POST (source_id=post):
I've traveled extensively solo and have never quite nailed the shoe question. I only like traveling with one pair (on my feet) and tend not to wear (or bring) any socks. Trying to keep my Osprey Farpoint 40-ltr pack light and portable. I've worn All-Birds a couple times and took Olekai on my recent trip to Australia. My trips are mostly urban with lots of walking (20K steps per day average). Fellow solo travelers, what do you recommend?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jk28dt5] (score 86, diepte 0) I use the Merrell nova mids in black. Cross between hiking boot and sneaker.

since you're a barefooter....highly recommend the superfeet insole with antimicrobial coating to keep the stank down.
[jk38r2v] (score 53, diepte 4) For Japan specifically, you will need socks because you are often asked to remove shoes.
[jk3gr3y] (score 50, diepte 0) I just have to ask, how do you keep your shoes from becoming ultra stinky if you wear the same pair every day and barely ever wear socks? I've never met a person who didn't use socks who's shoes didn't smell like bad gorgonzola from the other side of the room. Also when I've found myself with no other options than to go sockless in the same pair of shoes for a few days, I have to wash the shoes after because they're just too stinky after just those few days. 

Is there a tiny tiny population of people who don't get sweaty feet like, ever? Or do you just not care about the smell?
[jk4erlj] (score 40, diepte 1) Can't believe I had to scroll this far to find this comment. Like WTF?! Wearing the same shoes every day without socks is fucking disgusting. It's like wearing the same pair of socks every single day without washing them. Socks absorb sweat but you can change and wash socks. It's much more difficult to wash shoes...especially if you only have one pair.
[jk2a6p0] (score 38, diepte 0) You don't specify your gender. But as a woman I'd like to contribute:

Scarpa Rapid trail runners for closed shoes.

Teva Verra sandals for hot weather climates.
[jk2xk2z] (score 31, diepte 2) Honestly, imo you should invest in good socks too. Nice cushiony socks can save you from plenty of soreness.
[jk2vun4] (score 30, diepte 0) This gets asked so frequently especially under “r/onebagger,  :) have you searched the subreddit?
[jk38m1b] (score 28, diepte 4) I’m in Japan right now, take socks
[jk26458] (score 27, diepte 0) Personally use New Balance 574s when away cos of how comfy they are and can still be worn more smart if ever needed. Them and a pair of sliders is all I usually take
[jk3a23g] (score 22, diepte 2) Reaching hard af, lol.
[jk34oss] (score 22, diepte 1) Or if OP is female, /r/HerOneBag might have suggestions.
[jk3lqkn] (score 21, diepte 1) I’m sorry but those shoes CANNOT be worn smart, respectfully.
[jk2h710] (score 19, diepte 0) If you’re urban I’d just go tennis shoes and bring socks, call it a day. Granted, I have terrible fashion sense but they are the most comfortable for walking around on concrete.
[jk2qne4] (score 18, diepte 0) Confused why solo traveling would require different footwear than traveling with another person or a group. What am I missing?
[jk2iorx] (score 15, diepte 2) I have been using Vessi's for over a year now to travel regularly. Specifically the weekend sneaker because it looks more casual unlike a lot of their other models.

Pros:

-the waterproofing is legit. I stood in 2 inches of water in my bathtub when I first got them as a test and my feet stayed completely dry. Since then I've used them to walk through rainstorms, stepped in puddles, trudged through mud, and crossed streams with no wetness in my shoe. Basically, as long as you keep the water level below the ankle your foot will stay dry

-as mentioned above, it can handle mud and dirt pretty well which makes it usable for some light hiking if you like to do nature stuff on your travels

-pretty comfortable to walk around all day, I've pulled 14 hours of walking around being a tourist and have felt fine afterwards

-very breathable, I wear socks and my feet don't get hot when I'm going around tropical climates

-yet can be pretty warm too if you add some thicker socks for a cold environment

-it's pretty easy to find a 20% off coupon on YouTube since they advertise a lot with creators

Cons:

-while the weekend sneaker looks less sporty than other models, it's not the most "fashionable" shoe. You won't get away wearing it to a formal event. I wish they removed the checkered pattern and just made them a solid color. But it's passable in most situations, especially the black and white models

-it's fine to walk around in for hours if you're taking regular breaks, not so much if you'll be standing for hours. I wore them to a rainy music festival once where we stood for around 8 hours with only a couple breaks and my calves were killing me at the end

-they use a "sock like" design or a soft exterior which means they don't provide a lot of support on bumpy ground and you can easily end up bending your foot a lot. I wore them on a 2 months stint I did through central America in a lot of towns that had cobblestone roads. I had to catch myself a lot because I'd accidentally step in between two stone and my foot would bend in the shoe since it's soft (edit: this is my greatest complaint for reference)

-despite what the advertisements claim, they can only handle light hiking on well maintained trails. If you're going to do something more intense or on bumpy ground then Vessi's will not cut it, you will need actual hiking shoes

-they don't have the best traction when it gets icy and slippery so if you're going somewhere that you know it will snow or ice a lot while you're there then you should consider another shoe 

Overall, I would recommend them as a go to travel shoe but definitely keep the limitations I mentioned in mind. If they ever made a hard shell shoe with the same waterproofing and breathability I'd immediately get it but alas I do with what they provide
[jk2y137] (score 15, diepte 0) Lol I work selling all these more upscale brands of shoes to people who travel all over the place so this is fun to answer. 

Sandals: anything Teva. They're the best brand and better than Chaco sandals in my opinion. The XLT2 is my favorite since it offers more support than a foam based sandal with better tread as well. Someone mentioned Bedrock sandals which are good too because of the Vibram sole design. 

Casual sneakers: I like All birds because they're lightweight and easy to pack. I also find them very comfortable. The wool runner mizzle is my recommendation because it's water resistant, has extra grip for tread, and looks pretty minimalist/stylish. I walked around Spain, Portugal, and France with only a pair of those in January and they were great. Some other shout outs are the Hoka Mach 5, the New Balance fresh foam, Brooks adrenaline, and Altra lone peak if you want a trail runner with better grip. 

For backpacking: Zamberlan has some pretty good backpacking boots but they're very heavy and expensive. We sell some to folks going to do the AT, the Camino, or some other big trek. Honestly an Oboz Sawtooth mid is fine for backpacking/hiking. The Nucleo high by La Sportiva is also a good back packing boot.
[jk343wn] (score 13, diepte 0) Blundstones! I’ve brought them on both my solo ventures. Although they are more suitable with socks… They were great as casual/walking shoes, but also worked well as hiking shoes! They also last forever.
[jk2rhc9] (score 12, diepte 0) I always change shoes and socks daily.Depends on the climate for what types of both I use.A sick foot can make a trip a miserable experience and even cause lifetime problems.
[jk3tq3y] (score 10, diepte 1) Big second for a pair of Merrell’s. They’re breathable but somehow still reasonably warm if you need them to be and the pair I have are waterproof which is huge if you step in a puddle and only have the one pair of shoes. They’re also extremely comfortable and the hiking boot soles make them well suited for both walking around a city and light hiking to moderate trail hiking.

The one drawback is they are not exactly the most attractive shoes on the market. You pretty much look like you’re walking around in a pair of hiking boots all day.
[jk354p4] (score 9, diepte 2 OP) Sorry for forgetting gender. I’m a guy
[jk29mvz] (score 8, diepte 0) Birkenstock has slide sneakers that are very comfortable especially when walking. Vionics are also great. I also suggest vessi as they are waterproof.
[jk2my8b] (score 8, diepte 1) I'll add Jambu for women. I've worn these walking so many miles without pain. They are great for traveling and walking in warm to temperate climates.
[jk52h6e] (score 8, diepte 1) Exactly. Plus, this is not good for your health.
[jk2clyx] (score 7, diepte 0) Hoka Bondi 8.  Handles the stairs of seaside cliffs of Sicily to the sidewalk cobbles of all Europe.  And washable!
[jk3jryw] (score 7, diepte 1) Really? For me converse always hurt after a day of walking. I feel like they dont give any support at all, but yeah YMMV
[jk2cblz] (score 6, diepte 0) Scarpa boots. I bought some in 2003 and they’re still going strong, done thousands of kms. Only had to replace the laces.
[jk2h6yf] (score 6, diepte 0) Bedrock sandals. I wear them absolutely everywhere, except colder climates.
[jk4pfww] (score 6, diepte 4) Dang what's with all the down votes? I'm sorry.
[jk2ir2l] (score 5, diepte 1) which edition?
[jk2nu0h] (score 5, diepte 0) Chacos & a pair of Innov8 shoes. The chacos pack flat and my Innov8s do as well. Super light, have tread for hiking but good cushion for urban walking. I've actually ran adventure races in the Innov8s. Love them.

Edit: I'm actually doing a 2 month trip next month. Starting in Iceland and ending in SEA so I need 2 extremes to do everything.
[jk2r31g] (score 5, diepte 0) Can't recommend the Altra Lone Peaks enough. Fantastic shoe that lasted me well over 500 miles a pair.
[jk3k9ba] (score 5, diepte 2) Had the same reaction, Converse are awful for walking
[jk26tp9] (score 4, diepte 1 OP) Savvybackpacker site would agree with you. Socks or sockless?
[jk4ua26] (score 4, diepte 5 OP) Ok, good call on the socks. Thanks. Wearing socks does open up my choices of shoes (Hoka? NB?) and hopefully does not drive up the sweat factor too much.
[jk2a68l] (score 4, diepte 0) I wear [these shoes](https://www.kohls.com/product/prd-3233736/sonoma-goods-for-life-freer-mens-dress-shoes.jsp?prdPV=1&color=Cognac) which are crazy comfortable. I've walked 40k+ steps a day in them without any pain or issues. Versitle enough for when you want to dress nice. Can't be your only shoe if you plan things like hiking though. I have never tried them without socks so can't comment on that.
[jk2wkj6] (score 4, diepte 0) Love my altra lone peak.
[jk32jg4] (score 4, diepte 0) How can you wear a shoe without socks? I find that so weird, I mean don't you transpire in your shoes, doesn't it become uncomfortable??
[jk4ve5c] (score 4, diepte 2) They aren’t too heavy actually. I feel like they’re lighter than most boots. Plus, they were the only shoes I brought (minus sandals) so I didn’t have to carry them around or store them away.
[jk36t7t] (score 4, diepte 0) Asics Gel Kayano or NImbus depending on foot structure
[jk4olw6] (score 4, diepte 0) Hokas!! They have a lot of different styles catered to different needs so it's best to try em all on, maybe do a gait analysis at a running store to find out if you over pronate or over supinate. I over pronate and the hoka gaviotas are the only sneakers I've ever worn that don't necessitate a fancy corrective insole for me. If you have pain in one specific part of your foot after a ton of walking then you likely have a gait problem (or the shoes you're wearing just suck)

The no socks thing though... why not just get two pairs of wool socks (quick drying, more durable, don't stay sweaty) and rotate between em? You can wash the pair you just wore in the sink and let em dry while you sleep. I personally can't understand people who don't wear socks with sneakers but that's me. It's like going commando but for your feet. Unless you're a sandal guy (hoka does make some very sneaker-like sandals!) In which case fine lol

https://www.hoka.com/en/us/mens-sandals/hopara/195719186241.html?source=shoppingsite_PLA_1106534-CTHY-10.5&kpid=1106534-CTHY-10.5&utm_source=google&utm_medium=pla&gclid=CjwKCAjwjYKjBhB5EiwAiFdSfvUiz-duXVR4h-Lg7toCIGmnT-CZkO7oOWyVi31kphpjZqC7Co9RrBoCEWgQAvD_BwE&gclsrc=aw.ds
[jk26zpo] (score 3, diepte 2) Ah yea may not be the best then. I’ve been in cooler climates mostly.
[jk2t38f] (score 3, diepte 3) I got curious and Googled for myself.  Well-reasoned thoughts on footwear to take to Japan link below.  I also remembered correctly: if you end up wearing sandals, bring socks.

https://medium.com/japonica-publication/the-five-things-to-buy-before-your-trip-to-japan-42d0e1ec9d82
[jk3dii7] (score 3, diepte 5) > New Balance 574

And consider slip ons - *much* easier
[jk41f8v] (score 3, diepte 4) As others said, plenty of socks. Onsens, all lodging, and some restaurants require the removal of shoes.

If you don’t have any, they sell at 7-11.
[jk2fnc5] (score 3, diepte 0) I love my Nike Tanjuns. They handled Peru like a beast, including Wayna Piccu.
[jk2g233] (score 3, diepte 0) Onitsuka Tiger. Super comfy! I have an ultraboost, but for some reason, I feel like my onitsuka’s comfier.
[jk2lj05] (score 3, diepte 0) I wear Black Lugs Mid boots and have for several years and countries. I upgraded them with better laces and insoles and did some waterproofing.  They are my go to for any terrain and weather.
[jk2m89i] (score 3, diepte 0) Merrell lightweight, breathable hiking boots
[jk2npb7] (score 3, diepte 0) Any type of Salomon , not having to do up shoelaces is great , super comfortable , stylish & a great all round durable shoe . I personally wear the XT rush’s
[jk3nqjy] (score 3, diepte 1) Is 500 miles a lot though? It is the equivalent of 3 months of normal walking in my city.
[jk37dog] (score 3, diepte 0) Whatever you choose it’s still worth packing some blister tape and Gold Bond powder, plus socks of different thicknesses. Even my most comfortable shoes can fail me after a few days walking over 20k steps.
[jk56x56] (score 3, diepte 2) It's not that I don't believe you, I just don't understand how that works. And if it's actually true and actually works, I'm jealous af.
[jk25p0s] (score 2, diepte 0) I’ve been using these for the last 3 years and they’ve been fantastic. Well worth the price tag, look fashionable, and good for walking in urban cities and most kinds of terrain. The only downside is that they take up space if you pack them, but I’m usually wearing them.

https://www.drmartens.com/uk/en_gb/2976-yellow-stitch-crazy-horse-leather-chelsea-boots-dark-brown/p/27486201
[jk25vj8] (score 2, diepte 1 OP) Definitely fashionable! Never thought of a shoe like this. I guess I should have noted that I’ll be in a warm climate (Japan in summer).
[jk37blk] (score 2, diepte 4 OP) Those are good tips. Sandals can be comfy but the sock thing would be tough to endure. Also part of my thinking is the easy on/off benefit as one is removing shoes often.
[jk4wcji] (score 2, diepte 5) You’ll need to wear socks
[jk6i1vo] (score 2, diepte 2) Nah man 574s are their own category now. They trendy for some reason
[jk27gbj] (score 2, diepte 0) Sperry's for most everything, can dress up/down, slip on/off, socks/raw dog, no slip transitioning between surfaces, can get wet, adjustable laces around the heel, sold everywhere(replaceable) and if you need a pair of walkers or boots the Sperry's pack flat although on the heavier side.

Downsides are uneven surfaces like rock, gravel, trails(roots) and ice. Not good for long distances.
[jk27mjw] (score 2, diepte 1 OP) Sperry’s used to be my go-to a while back. They can face anything. Haven’t thought them in some years but I might give them a try. Thanks.
[jk29ujh] (score 2, diepte 1 OP) Good suggestions. I’m looking closely at Vessi. Have you worn them to travel?
[jk2ct1j] (score 2, diepte 1) Can you post a link to the ones you’re referring to? Thx
[jk2a8qi] (score 2, diepte 0) FitFlop Rally sneakers with socks, and a pair of flip flops for ganky hostel showers
[jk2eskq] (score 2, diepte 0) Hiking boots is my preference. Right now I have Merrel but before that I had a "whatever brand" I bought in Taiwan. I switched when my feet were getting more tired than usual, which means I threw them out too late 😂.

I think that with that walking amount they will last 6 months or less.
[jk4d9zp] (score 2, diepte 2) They will get soaked! I got caught in the rain in NYC and they were soaked immediately. They also don’t have a lot of thread so I wouldn’t use them to hike. You’ll never be able to get up a smooth rock. With that said they are my first and only travel shoe. They’re super comfortable and breathable. Lighweight and the uppers are soft enough to push down in a bag.
[jk2tq48] (score 2, diepte 1) These are pretty much the solo traveler starter pack. Easy to wear but I don’t know how y’all wear those in cities.
[jk2i440] (score 2, diepte 0) I suggest get  [Insoles](https://www.amazon.in/Frido-Trimmable-Insoles-Replacing-Existing/dp/B09RV5MGQ2/ref=mp_s_a_1_1_sspa?crid=2R5U11CYQXEUM&keywords=gel+foot&qid=1684028468&sprefix=gel+foot+%2Caps%2C268&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9waG9uZV9zZWFyY2hfYXRm&psc=1)

That makes my walk even more comfortable
[jk2jv85] (score 2, diepte 0) You really need to try different types of shoes, as getting the right fit for your feet is essential when you're doing that much walking.

I personally use Scarpa Cyrus GTX hiking boots for trips where I'm expecting to do a lot of walking as they're very comfortable for me, and look presentable. I prefer boots that provide ankle support and have somewhat firm soles over running shoes with squishy soles, but other people have the opposite preference.
[jk2jwvu] (score 2, diepte 0) I usually wear North Face Vectiv hiking shoes. Seems pretty good as an all-purpose kind of shoe.
[jk2kcmq] (score 2, diepte 0) Likely not helpful but I wore the Pierre Hardy all white laceless shoes for a 3 week trip in Europe/UK. Only shoe I brought along w my one bag and I was able to dress it up and down, go sock-less most days. Did about 30 K steps per day. Out until 4 am daily. Never let me down.
[jk2mknv] (score 2, diepte 0) Hokas are very comfortable and lightweight, so you could also bring sandals, too
[jk2o2ut] (score 2, diepte 0) Merrill
[jk2ox7l] (score 2, diepte 0) The ones nurses use to stay on their feet all day everyday and retail staff wear to walk on concrete floors all day. 

As a traveler you will likely be walking all day everyday quite a bit.

Hoka Bondi maximum cushioning running shoe.
[jk492pc] (score 2, diepte 1) I had to look these up cause I've never heard of them, and oh man are they ugly but they look comfy af
[jk2sju8] (score 2, diepte 0) I have a pair of Altra lone peaks and swear by them. Very low/no cushion (my PT said not to wear high cushion shoes like Hokas after my knee replacement). I’m on my third pair of lone peaks and will continue to buy them into infinity. Great for almost any situation and durable.
[jk2xs5s] (score 2, diepte 0) Male

Black Nike Pegasus
[jk32s52] (score 2, diepte 0) Running shoes
[jk4je5b] (score 2, diepte 1) I have worn mine for over a year, every single day--was in India a month, perfect! slipped on and off easily for the temples, and very comfortable...
[jk8wytx] (score 2, diepte 3) Hah yeah I sometimes wear cowboy boots for solo traveling for similar reasons. They really aren't that different functionality-wise, just a bit of a different aesthetic I guess.
[jk3516d] (score 2, diepte 0) I love Converse. They go with me on every trip.
(105 reacties met lagere score weggelaten)

=== THREAD 1dgr65b ===
SUBREDDIT: r/BabyBumps
DATUM: 2024-06-15  SCORE: 46  REACTIES: 171
TITEL: What shoes are you wearing?
POST (source_id=post):
25 and a half weeks here and my feet are on fire.

I already have somewhat flat feet and I think pregnancy has made them even flatter and more sensitive.

It doesn’t help that I’ve never really taken care of my feet or bothered to wear good shoes or good insoles. I used to wear doc martens boots and cutesy keds sneakers but they’ve all stopped fitting. I had a pair of kiziks sneakers I destroyed, not sure if I should get another pair.  

Lately I’ve only been wearing a pair of birdies flats because I feel like the only shoe I can deal with is a slip on but OH MY GOD they are so uncomfy it’s killing me. Anytime I’m on my feet for more than a few minutes the pain and foot fatigue sets in. I used to like walking around barefoot at home but I can’t do that either. My feet are absolutely on fire.

I’m 37, so in general I should probably be wearing more supportive shoes for old lady feet but I don’t know where to begin. 

For those of you with foot pain exacerbated by pregnancy, what are you wearing to stay comfy?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l8ruazg] (score 72, diepte 0) My crocs are the only thing that fits me now… but they’re comfy, so it’s fine
[l8rt729] (score 40, diepte 0) I find my feet are happiest with the combo of compression socks + something with more firm/molded/supportive footbed like Birkenstocks
[l8rxrpp] (score 26, diepte 0) I just got ASICS gel nimbus ! They are like walking on clouds. I’ve been having bad heel pain in everything else
[l8s84vp] (score 22, diepte 0) Crocs and Kizik sneakers. Kiziks are a game changer, I got them specifically for pregnancy when I was just a few weeks along; you can put them on without bending over, you just step into them. They are so comfy!
[l8s4sbt] (score 20, diepte 1) I second the croc sandals/slides. Really comfy. I add flower or pearl gibbets when I’m going somewhere more fancy and get compliments. 🤣
[l8s7nxj] (score 19, diepte 0) Hokas!! The hokas are like walking on a cloud. 100% worth the money. For sandals I have fake Birkenstocks. This combo has worked really well.
[l8ry45g] (score 18, diepte 0) I was a nurse before kids. Comfy shoes are my thing. Hokas are incredible. So worth the price. I wear Oofos flip flops around my house. They aren’t cute so I don’t wear them out of the house. They are amazing for everyday wear. I typically wear Birkenstock sandals when I leave the house.
[l8seje9] (score 13, diepte 1) I’m a week postpartum and my Kiziks are essentially the only pair of shoes I’ve worn since like, halfway through the third trimester.
[l8t399w] (score 10, diepte 1) I just bought myself of third trimester Birkenstocks and I am so happy I did
[l8s1tl2] (score 10, diepte 1) Second ASICS!  I love them so much.  Just a heads up, sometimes I go a whole size up on them from my regular shoe size.  It was recommended by the associate to do that and it’s honestly way more comfortable.  One of their lines is specifically for flat feet but I can’t remember which.
[l8s1wgq] (score 9, diepte 0) Another vote for Birkenstock sandals — and OOFOS clogs for work!  The OOFOS are admittedly p ugly, but I work on my feet all day as a nurse and I appreciate the cushion (also getting harder to bend over and tie shoes, so slip on shoes are preferred)
[l8t5jm7] (score 7, diepte 1) Yup, I did off brand Crocs from Amazon with added nice insoles. Pure comfort and good fit the whole time, even if they don't look amazing
[l8skwwu] (score 7, diepte 1) I lived in my Kiziks from like 28w until I was a year pp. I literally wore them out!
[l8snpp2] (score 6, diepte 1) Yup. Croc sandals. I have some cute platform ones that i wear to work and they are so comfy. I also have flat feet and I love all my crocs.
[l8rv7se] (score 6, diepte 0) Compression socks and Birkenstocks
[l8s6iju] (score 6, diepte 0) Vionics are amazing. I wear their slides around the house and it helps with back pain a ton. Also love Birkenstocks and Hokas.
[l8rxnhd] (score 5, diepte 1) No shame I wore compression socks with my Arizona Birkenstocks to my last Pre-Natal appointment
[l8sr561] (score 5, diepte 2) Asics, also sized up a whole size, using a shoe horn that came with my husband's dress shoes to get them on.
[l8sjop8] (score 5, diepte 0) Skechers slip ons
[l8tq998] (score 4, diepte 2) Too hot for Birks? Do you mean because of the sun exposure? I slap on some sunscreen and wear my Birks out all the time, and its 110 degrees currently.

Is that not recommended?
[l8t6x73] (score 4, diepte 2) I have the regular cork birks but figured they wont fit at some point or become uncomfortable so i bought a white pair of the Arizonas the foam version. Very comfy but do not go on long walks in those as the hot feet and rubber created the worst blisters of life. 🥲
[l8t2yk2] (score 4, diepte 1) I got Hoka Bondi’s in a size up + wide fit for work and have been loving them!
[l8sjhtx] (score 4, diepte 1) Everyone in the comments saying Birkenstocks, i have no idea how you find them comfortable. Zero cushioning and support, like walking on a plank of wood all day. I can barely wear mine not pregnant 😂
[l8tlo3h] (score 4, diepte 0) It’s all about the Kiziks ! They are really comfy and I got a nice black pair so even tho they are sneakers I was wearing for work stuff and getting away with it. But the main thing is that you can slip them on, which makes SUCH a difference later in the third trimester
[l8tryet] (score 3, diepte 3) Oooooh I mean the clog versions!! Clogs plus compression socks in 90 degree Fahrenheit weather is no fun.
[l8t5z0l] (score 3, diepte 1) Ugh I wish my feet still fit in my Birkenstocks 😭 definitely seconding the compression socks! You can get ankle height if it’s just your feet that need help!
[l8rttwa] (score 3, diepte 0) People will tell you they're ugly but I honestly love them! Merrell clogs, and it sounds like you might need to go up at least a half size from your normal: [https://www.amazon.com/Merrell-Womens-Encore-Moccasin-Espresso](https://www.amazon.com/Merrell-Womens-Encore-Moccasin-Espresso)

Sadly during this pregnancy I bought the fabric merrell clog a half size up thinking that would do me for summer... The opening for your foot is much tighter than the leather ones, and they leave my foot a little misshapen and unhappy. 

Also, cheap, cheerful and very effective- but also ugly: crocs. They feel wonderful.
[l8toy9t] (score 3, diepte 2) I just ordered some of the sandals!
[l8s6ge6] (score 3, diepte 1) I can’t fit my classic clogs anymore but my lite ride crocs have been my go to!
[l8smtu2] (score 3, diepte 1) Yup. I’ve been wearing some random cushion Amazon slides for the last 8 weeks basically because it’s the only thing that fits with all my swelling. I get a really light nude color so it kinda blends in with whatever I wear lol
[l8ssr0n] (score 3, diepte 1) Came here to say crocs 😂
[l8t56pk] (score 3, diepte 1) I just got my first pair of crocs! They’re the best!
[l8tabcm] (score 3, diepte 1) Also wore crocs. Wore them before pregnancy, all throughout as I got bigger, and I still wear them 5 months postpartum. Comfy af!
[l8rvn68] (score 3, diepte 0) The only shoes that fit me in my closet are my hey dudes so I’ve just been wearing those. It’s not fashion but neither is anything else I squeeze onto this body
[l8rxkz2] (score 3, diepte 0) I’m 38+6 weeks and it’s now just Birkenstocks on the loosest setting 😂

I was able to wear my all birds until 36 weeks and now my feet are too swollen unless I have compression socks on and it’s first thing in the morning.
[l8sqora] (score 3, diepte 1) This! By the end of my pregnancy none of my cute shoes or sandals fit so my asics were my way to go. So comfortable. I use gel 360
[l8s79rn] (score 3, diepte 0) These are my favorite shoes ever. I have three pairs. I suffered from plantar fasciitis for a couple years and these are light a delightful foot massage as I walk. 

[https://www.vionicshoes.com/rejuvenate-recovery-sandal.html](https://www.vionicshoes.com/rejuvenate-recovery-sandal.html)
[l8sxg7s] (score 2, diepte 1) Yeah I miss my Birkenstocks, it got too hot here though. Hubby got me some crocs to replace them tho :)
[l8tsbha] (score 2, diepte 4) Oh, silly me. That makes so much sense!
[l8ti7s2] (score 2, diepte 1) I wore knock-off birks from target my ENTIRE pregnancy. They were worn to shreds by the end.
[l8vfj4v] (score 2, diepte 2) i have 2 pairs of the sandals and i love them! so cute
[l8sri12] (score 2, diepte 1) Did you have to size up or just stick with your normal size?
[l9b62ht] (score 2, diepte 2) I did end up having to go up a size
[l8xar03] (score 2, diepte 2) Yes! I have the Bondi’s as well! Should have included that in the original comment. They really are the best
[l8u6umz] (score 2, diepte 1) Kiziks + insoles were definitely a game changer. I got them early on since I had bad sciatica and it hurt bending over/getting back up to put on shoes. They’re easy to slip on while still being stylish. I got them in wide to accommodate for swelling. I still use them postpartum since they’re so easy haha
[l8sb2v4] (score 2, diepte 0) ONs and Birkenstocks!
[l8sc4k7] (score 2, diepte 0) New balance 574s in a half size up!
[l8sd3dd] (score 2, diepte 0) I wore running shoes because I needed the support. Got elastic shoelaces for putting them on, highly recommend!
[l8shzxk] (score 2, diepte 0) My feet have hurt since about 22 weeks or so. It's BAD now at 32 weeks. I got some house shoes on amazon and I LOVE them. I wear Hoka Bondis outside of the house.

shevalues Orthopedic Sandals for Women Arch Support Recovery Flip Flops Pillow Soft Summer Beach Shoes https://a.co/d/cCQa5dC
[l8sj8uc] (score 2, diepte 0) I basically wore only my foam nike slides the second half of pregnancy, if it was cold i might wear socks too or i had one pair of comfy joggers with memory foam soles. I needed something with cushion and bounce to absorb impact to save my feet knees and back. Amazingly after 2 weeks postpartum i can wear any shoes and my problems have resolved now that i don’t have a massive baby crushing me from the inside 😂
[l8taplm] (score 2, diepte 1) I second the skechers! They were the only shoe that actually stretched appropriately when my feet started to swell last summer. I still wear them now!
[l8slqde] (score 2, diepte 0) Tevas are the only things I can comfortably shove my fat feet in currently
[l8swj5o] (score 2, diepte 0) Hokas recovery flip flops!
[l8swnfd] (score 2, diepte 0) Wow- Hi twin!!! I’m 37, just hit 26 weeks and have been on the couch for 2 hrs bc my feet hurt so bad from wearing flip flops at my baby shower! 

I JUST discovered compression socks, which have really helped, but it’s time to step up my insole game…
[l8t0n4a] (score 2, diepte 0) On sneakers (on cloud). I was given a pair. 
Asked for another pair in the hospital while I was in labor. They are more expensive than anything I would buy for myself but honest to God they are the best shoes I have ever owned.
Soooo comfy. Helped get me through my pregnancy. I will never go back.
[l8t1h8i] (score 2, diepte 0) My feet are a mess. Lol. I have low arches AND neuropathy in one foot and through the toes. If I wear tight shoes, my toes feel like they're on fire! Shoes with good cushioning but specifically wide toe boxes have been getting me through my pregnancy.

I'm a fan of Altra sneakers for good arch support and a natural toe box shape. But if you search wide toe box/natural toe box shoes, there are some great options that give great relief with toes feeling too cramped.
[l8t66qf] (score 2, diepte 0) Look up cloud slides on Amazon! Order a size up from your normal shoes size. PLEASE DON’T SLEEP ON THIS - do yourself the favor and order them now! 

This is ALL I wear for late pregnancy and it will literally feel like you’re walking on clouds!!

Hint: read reviews and opt for the good ones. You deserve it!! Good luck mama
[l8telho] (score 2, diepte 0) Birkenstocks were my saviors from like 20 weeks to 40 weeks
[l8ubpwx] (score 2, diepte 0) My hospital physio told me not to wear flats or any shoes without arch supports. She basically said to just wear running shoes so I’ve been wearing those since about 26 weeks. She even told me to put insoles into my slippers if I was to insist on wearing slippers in the house.
[l8yn89z] (score 2, diepte 0) I have pretty flat feet too & my feet got extremely swollen during pregnancy. The combination that worked for me was - compression socks, putting my feet/legs up on the wall for 15 mins morning & night and then getting really supportive sneakers. I got one pair for indoor use only & one pair for outdoors. Both On Cloud - Cloud 5 sneakers. I recommend but tbh any pair or comfy sneakers. House sneakers are the best & I wish I started that years ago!! 

Oh I also started magnesium supplements and would alternate days of soaking my feet in a hot bucket with Epsom salts or magnesium flakes or soaking my feet in an ice bath for as long as possible - normally like 5 minutes. Hope you find some relief soon!
[l8v6mm1] (score 1, diepte 2) Yess I’ve never wanted to wear the normal crocs, but I bought a few pairs of cute crocs sandals and they are SO comfy and actually pretty cute.
[l9bphfz] (score 1, diepte 3) Good to know! Thank you.
[l8ukj8m] (score 1, diepte 1) I’m also wearing my crocs! but fuzzy crocs, I’m 90+ degree weather lol. Worth it
[l8rw2pq] (score 1, diepte 0) Currently obsessed with my rothys clogs. They're so comfy, slip on so I don't have to bend over, and look fine with leggings and a tee or maternity jeans and a nice top.
[l8rwv8c] (score 1, diepte 0) I’ve been wearing my Akk sneakers and rainbow flip flops basically all pregnancy. The Akk sneakers are like $40 on Amazon and slip ons. I can walk in them all day.
[l8rza58] (score 1, diepte 0) I lived in my Birkenstock's and Veja's through my pregnancies. Try to put your feet up when you're resting. Xx
[l8rzx81] (score 1, diepte 0) I went to the shoe carnival near me and brought some flats. That’s all I wear really
[l8s1wi2] (score 1, diepte 0) Crocs and ugg clogs. The ugg clogs are amazing but kinda weird for summer…still the most comfortable shoe I own
[l8s1x4j] (score 1, diepte 0) I’ve just been wearing my Birkenstock sandals which have been supportive and adjustable when my feet feel like baked potatoes
[l8s4a3y] (score 1, diepte 0) I’ve been wearing new balances 530. They’re comfortable because they’re wider than what I’m used to but I know there’s more comfortable options out there 😅

I’ve also been wearing some off brand “Birkenstock” footbed sandals (??) since they’re adjustable on the top and I can make it wider if my feet get swollen.
[l8s5zur] (score 1, diepte 0) Hey Dudes were my go to. I had a pair that looked like a casual all white shoe plus the usual hey dudes. For sandals, I wore Birkenstocks and just loosened the straps
[l8tywbp] (score 1, diepte 2) I love my kiziks but they were feeling way too tight. Ordered a new pair in a half size up and in wide and it’s soooo much better.
[l8sc6g7] (score 1, diepte 0) Dr. Scholls brand skate shoes (basically slip-on Vans but with good insoles) that I found in a thrift store and have been pretty comfy.  

Now that it’s hot though, I’m wearing my Tevas a lot.
[l8sczbk] (score 1, diepte 0) Crocks lol and slides from Walmart that’s all I fit in those days
[l8sd347] (score 1, diepte 0) Birkenstocks~
[l8sdlgd] (score 1, diepte 0) I wore birkenstock sandals. Adjustable, great support…totally worth it. They can be expensive but I got them off their sale stuff so they weren’t bad.
[l8se2os] (score 1, diepte 0) 17 weeks, in the UK where it's pouring with rain every single day. I'm wearing Tommy Hilfiger wellies which I only bought last year. I worry I might go up a shoe size during pregnancy, so I'm making the most of them while I can.
[l8sgesd] (score 1, diepte 0) I would recommend looking into Hoka therapeutic slides, they have helped me so much with my pregnancy when it comes to feet pain. And for everyday wear I would get regular Hoka’s. They feel amazing on my feet!
[l8sgsjr] (score 1, diepte 0) I wore backless loafers, Minnetonka slippers and Solovairs(doc martens). My crocs were too small weeks 33-until about a week after birth. 

Compression stockings!! I wore them exclusively at the end and post partum.
[l8shrj0] (score 1, diepte 0) Birkenstocks because it’s hot out and I refuse to bend down to tie shoes
(93 reacties met lagere score weggelaten)

