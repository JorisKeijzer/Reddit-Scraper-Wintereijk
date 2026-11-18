# Label-batch batch_0075

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
Schrijf het resultaat naar `batch_0075.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1nx9n7t, 1ikzppz, 124aedv).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1nx9n7t ===
SUBREDDIT: r/Teachers
DATUM: 2025-10-03  SCORE: 24  REACTIES: 96
TITEL: my feet hurt
POST (source_id=post):
I started my first year of teaching, my feet hurt and I have never felt this before. The bottom of my feet are also peeling and idk why. Has anyone else experienced this? What shoes do you wear? Do you recommend getting insoles?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nhltew3] (score 38, diepte 0) I personally recommend hokas. Go to a running store and get fitted :) it is so worth the expense!
[nhm0l3o] (score 20, diepte 1) I have plantar fasicitis from so much walking at school.  A podiatrist recommended Hokas or Brooks, PLUS going to a shoe store and get inserts.  Made a world of difference between limping and getting back to being able to walk 10k steps per day.
[nhlvh18] (score 18, diepte 0) Okay. Everyone is recommending Hokas and they are fabulous shoes BUT they aren’t for everyone. I walk mainly on hard floors and my feet were BURNING by the end of a shift. So I took them back and got Brooks. Wonderfully amazing and I get a new pair every six months. Make sure you get a half-size bigger than you need as your feet will swell. 

That’s the first part. The second is your socks. You NEED to be wearing compressions socks. ALL OF YOU. I would wear a second pair of regular ankle socks over them to make my shoes fit better. 

Sincerely, 
An ICU RN who once walked 11.5 miles during the same goddamn shift around the same 275m x 50m circuit. (My pedometer measures in miles but the measurements along the hallway are in metres.)
[nhlvgeg] (score 16, diepte 0) You may be developing plantar fasciitis, so in addition to supportive shoes with good insoles, you could stand on a tennis ball every day for a few minutes to loosen the tissue; or if you’re lucky enough to have a partner who massages feet, ask them to focus on your arches and heel.
[nhm096e] (score 15, diepte 1) I developed plantar fasciitis from wearing ballet flats all day when I started teaching. Birkenstocks saved me.
[nhlu5d2] (score 7, diepte 0) It’s gonna sound crazy but I wear a lot of sandals because I do well as close to barefoot as possible. In winter I make sure I have some super comfy sneakers with good soles but with a low drop and wide toe box.
[nhmiak9] (score 6, diepte 1) I started wearing compression socks around a year ago and my feet don’t hurt everyday like they used to. It’s amazing.
[nhmbph1] (score 6, diepte 0) Hokas, Dansko, Clark's, Birks are what I wear. Spent a small fortune on shoes, but my plantar fasciitis went away and my feet are happy all day. I also got a foot spa with heat and bubbles for Christmas. Got some nice foot soak stuff for the spa. Use that a couple of times a month and I'm a pretty happy camper.
[nhm4v85] (score 5, diepte 1) Dawgs 3 strap sandals in ALL the colors.  Maine winters? Wear boots to school and change to the dawgs!
[nhnhtcy] (score 5, diepte 1) To the person who said I need to lose weight, I’m 5’2 and 125 pounds, so you’re completely wrong but thank you for this teachable moment.

That was an INCREDIBLY poor deduction from my post. Your response shows a clear lack of reading comprehension aggravated by your lack of ability to not parrot others’ equally poor statements. 

You can take this opportunity for reflection. Analyse what could have made believe something so completely off the mark from what was written. Please also reflect upon why you thought your comment needed to be said at all. You’ve likely gone your whole life surrounded by people who were frustrated by your communication, but over time, learned to ignore it which you likely accepted as tacit approval because again, your deductive abilities are limited and skewed. 

This is your chance to learn and grow.
[nhlyct6] (score 5, diepte 0) I'm not a teacher, but I was a waitress, and also worked at Dairy Queen for 10 years. I found that SAS shoes are amazing. SAS comfort shoes, Dream is the style I go for. They're slip on, so there's no worries about tripping over laces. And they LAST. 1 pair lasts me for 3+ years. Did I mention I'm also fat?  I will always recommend SAS.
[nhm56ma] (score 4, diepte 3) I'm of a completely healthy weight and Hokas saved my legs.  This comment is absurd.
[nhnk40q] (score 4, diepte 2) Have you ever worn tight shoes, walk around, took them off, and couldn’t put them back on at all or it hurt really badly? I think this would be a good example to help explain this. 

When your feet swell it’s because of many reasons but logically speaking, a lot of it has to do with gravity. When you stand up and walk, gravity makes the fluids in your body to your feet. When you sit down and your feet are below you and bent, this inhibits your body’s ability to draw those fluids back up. 

Both of these equal swollen, owie feet normally. Just normal, healthy feet. You can begin to imagine how bad it can get if your have other factors (even stress) SO

Everyone, regardless of health status, needs compression socks. They even come in cute colours!
[nhlt0mb] (score 3, diepte 0) Gave yourself a hot foot. 🔥  Time for expensive sneakers. I say Hoka Bondi or New Balance Fresh Foam. Plan on $150.
[nhmp5jx] (score 3, diepte 2) I’m a bodybuilder and I would rather be fat as fuck than as stupid as your comments are.
[nhm5n0m] (score 3, diepte 5) Fortunately I don't let the opinion of 14 year olds dictate my decisions
[nhm64tw] (score 3, diepte 7) Similarly,  no one asked for your opinions on their footwear.



OP, try the Hoka Bondi 9. Saved me from years of pain.
[nhm73lc] (score 3, diepte 1) Highly recommend Altra for zero drop and wide toe box
[nhlw1tq] (score 3, diepte 1) I had that pretty bad. Got the insoles recommended by podiatrist and just got cheaper ones from Amazon when it came time to replace.
[nhm7hft] (score 3, diepte 2) Yes, I have loved my birkenstock sandals for ages  and, relatively recently, shoes and boots as well. Their chelsea boot is my favorite winter footwear now.
[nhm4ndm] (score 3, diepte 0) Hokas are amazing. They are expensive but worth the money.

The peeling could be a variety of things, including the fact that your feet are sweating more than you’re used to and your skin is damp, resulting in all over peeling or some sort of fungal situation, or that your feet are getting a lot more friction from you standing and walking more and you’re kind of blistering or rubbing off layers of dead skin. Mine did this as well when I first started teaching on the balls of my feet the flats of my heels and the flat part of my big toe and it wasn’t deep blisters, but it would just be these flat pieces of skin that would peel off and it was literally just that my body wasn’t used to moving that much in that way And after a few months, my feet toughened up and it was fine
[nhm6fma] (score 3, diepte 0) I had to buy 2 new pair of school shoes, after coming home with aching feet from standing most of the day. Dressy shoes are not for teaching.
[nhm85x4] (score 3, diepte 0) In addition to investing in sensible shoes, consider placing anti-fatigue mats at the front of the classroom, running parallel with the boards. Another consideration would be to get a blood test. Diabetes can cause foot issues.
[nhmb33z] (score 3, diepte 0) I second everyone else's advice of wearing good shows. However a large part of your issue is probably just plain not being used to standing for hours at a time. Your body will adapt and get used to standing all the time eventually.
[nhm092u] (score 2, diepte 4) Are you a teacher? What do you wear! Would love recommendations while running after eloping students!
[nhltx0l] (score 2, diepte 0) I was getting foot pain my first year too, about 2 years ago. I researched and almost accidentally went the extra-support route, and eventually settled on barefoot shoes. Thin soled, very flexible, wide (if that’s an issue for you), and “zero drop” (meaning no heel which is extremely important.) I never get foot pain anymore unless I injure my leg or something and so am walking funny, other than that I’m feeling so much better!
[nhmv85g] (score 2, diepte 1) This! Switched to barefoot shoes too and love them. They take a bit of time to adjust, but real complaints after 3 years besides they're not the most comfortable to bike to work on everyday.
[nhnvtfm] (score 2, diepte 2) Birkenstocks and Chaco sandals all day for me! I regret every day I try to mix it up with other shoes
[nhqgaow] (score 2, diepte 4) Judging by your avatar, you’ve never worn a pair of too-tight heels for too long;)

I’m happy your feet don’t swell noticeably but they do swell. It isn’t any more avoidable than your spine compressing as you walk during the day only to stretch back out at night.

I’m happy your feet are okay now, but please keep it in mind.
[nhqiis9] (score 2, diepte 5) Lol, you are correct, I have not worn heels. Pretty much running shoes the last 30 years. Mid 40’s now so I figure some shit like that might pop up soon. The change from retail to teaching has been good for my feet though. I don’t walk near as much now as I did when managing a 200k square foot building. At least I know what to do now if it does! Here’s to happy, healthy feet for all of us!
[nhlwcge] (score 2, diepte 0) Don’t cheap out on your shoes. 

Go to a running store and get properly measured. Standing on concrete all day sucks. 

Brooks
Hokas
New Balance
Chacos

Go more for comfort than style. Your body will thank you later.
[nhlyau4] (score 2, diepte 0) Next week at work, try to be mindful of how you’re standing, and where you’re placing pressure on your feet.  I catch myself putting all of my weight on one foot absent mindedly.  Even sitting sometimes, we dig our feet into the ground subconsciously as a way of dealing with the stress of the job.
[nhm5fy2] (score 2, diepte 0) I use sketchers (especially the slip ins). Some of their “bobs” collection are dressy enough to pass as dressy tennis shoes and/or they have flats style options
[nhm6nac] (score 2, diepte 0) You have great shoe recs here. 
Peeling feet?
Baby Feet brand foot peel on Amazon (or other beauty supply). Buy at least 2 packs (each pack is for both feet, you’ll want to do another peel in 4-6 wks).

1. Soak feet for 5-10 min in warm/hot water. 
2. Dry & put feet in peel bags. Wear 1.5-2 hours ( it says 1, I always do 90-120 minutes).
3. Soak feet again to rinse & dry. 
NO LOTION!
4. Try to soak feet for a few minutes every day to loosen skin- then the shedding will begin!
NO lotion while shedding. 

Do another peel in 4-6 weeks… magic feet!
[nhmb935] (score 2, diepte 0) Buy some Danskos
[nhmc5c5] (score 2, diepte 0) I love Dansko clogs.
[nhmjjqu] (score 2, diepte 0) I had sore feet for my first couple of years, then I started wearing Crocs and the last 20 years have been pain-free.
[nhn7u95] (score 2, diepte 0) I'm a huge fan of Vionics shoes inserts and used to use copper shoe inserts or copper compression arch sleeves when I played competitive soccer, tennis, and ran cross country. BTW my family is prone to feet issues (bunions, heel spurs, arch issues, blood flow issues, overheating) so I'm always searching for the next best thing.
[nhnm4bv] (score 2, diepte 0) I had a stool at the front my classroom. There is no reason you can’t sit for part of the day. I also had an iPad that streamed to the projector so I could teach from it. The kids could write answers on it that would show up on the board. They loved it. Then, when it’s time to walk around the class to give individual attention, your feet aren’t killing you.
[nhm6iwu] (score 1, diepte 8) So you admit that you’re fat? Be honest here.  We’re all friends.
[nhm6qdd] (score 1, diepte 9) Like I said, I'm quite a healthy weight. Really tall and skinny build. I'm also certainly not your friend.
[nhm6vzi] (score 1, diepte 11) Nah, I'm good.
[nhm57sv] (score 1, diepte 1) But doesn’t the thin sole hurt your feet when walking on concrete and other flat surfaces?
[nhmvbu2] (score 1, diepte 2) I use them too. It's an adjustment for sure, but once you adapt, it's not bad at all!
[nhmxg0h] (score 1, diepte 2) At first you will be sore if you’re used to very thick shoes but then your feet just get stronger.
[nhpy16a] (score 1, diepte 2) Not at all! Well, there is an adjustment period, but it’s all about how you walk. If you think about it, your feet are used to hitting the pavement hard when walking outdoors, but at home, when you’re truly barefoot, you step more lightly. You just have to get used to walking with a lighter step on concrete. Now it doesn’t bother me at all. In fact I feel annoyed now when I wear my thicker soled barefoot shoes, and sometimes even come home with foot pain.
[nhmfjop] (score 1, diepte 2) Fire drills must be fun 😜
[nhmrdy5] (score 1, diepte 3) Grab the boots and coat on the way out the door! Luckily they have done FIVE DRILLS already this year.
[nho43ks] (score 1, diepte 1) I second this too if it works for you^ in the winter I wear my moccasins bare foot and the kids have never said anything and when I change in to my boots to go outside I just pretend my sock fell off in my boot 😂
[nhluu62] (score 1, diepte 0) Kuru
[nhluvrl] (score 1, diepte 0) I teach 1st grade and rarely sit down. I also exercise everyday and the shoe that withstands all that are the New balance fresh foam 1080v14. They are awesome and I do over 12000 steps a day. I only use those shoes until I don’t feel the bounce. I end up with my feet not hurting. When I get home I use the oofos sandals to recover my feet. I highly recommend them.
[nhlw5u3] (score 1, diepte 2) Yeah, prescription insoles are the way to go
[nhm146m] (score 1, diepte 1) Sounds like you need to lose weight.
[nhm43yi] (score 1, diepte 1) I love my brooks.
[nhm87l1] (score 1, diepte 1) Give me some more info on the compression socks, why?
[nhqe3rc] (score 1, diepte 3) I actually haven’t ever had that. I’ve had my feet hurt from being on them too long but never swelling. I usually wear my shoes semi loose and always buy them about a half size big. I’m on the low end of the bmi scale though so maybe that affects things. The majority of my adult life has been working on concrete floors(retail for 15 and teaching the last 5) and the most steps I’ve had is 35k in a day(black Friday).  At least I know now if they start swelling what to do. Thanks!
[nhtwave] (score 1, diepte 6) Agreed:)
[nhqe74b] (score 1, diepte 3) Do you have a brand suggestion? I’m so down to try anything to help my pain.
[nhni9wi] (score 1, diepte 1) I got Hoka's and don't find them as great as everyone else. I had terrible big toe blisters after a long day and many miles at Disney.
[nho380x] (score 1, diepte 1) Kuru shoes online.
[ni1ogu2] (score 1, diepte 1) I'm getting the compression socks, thanks!
[nhlweto] (score 1, diepte 0) Birkenstock or Taos shoe girl here!
[nhm2n5e] (score 1, diepte 0) TreadLabs inserts are amazing, and you can pick the arch height.  Also, get yourself a massage gun and pound the crap out of the bottoms of your feet when you get home.  I wouldn't be able to continue walking if I didn't have the massage gun.
[nhmavun] (score 1, diepte 0) This is expensive, but worth it. The first time I experienced sciatica and I was in so much pain. I was at a study program in Belgium and had to leave early. I got these arch supports and I instantly felt better. It’s a store called The Good Feet. Mine were $1,000 twenty years ago, and I have no idea what they are now. But it was the smartest thing I’ve ever done in my career teaching.
[nhmazjg] (score 1, diepte 1) My feet are incredibly narrow and I have 0 arch
[nhn0g46] (score 1, diepte 0) Go to a running store. Have them size and for you. Spend $200 or more.
[nhn9g6t] (score 1, diepte 0) Merrell jungle mocs with spenco inserts. good socks.
[nhn9zj7] (score 1, diepte 0) Get nurses sneakers
[nhniuft] (score 1, diepte 0) First job on your feet?
[nhnj8nl] (score 1, diepte 0) If you find out that it is plantar, just know that you can do about with physical therapy. I still do the exercises I learned there when my ankles or soles flare up. And remember, ice is your friend.
[nhnkosk] (score 1, diepte 0) i know the feeling.

custom orthotics have helped.
[nhnolfo] (score 1, diepte 0) I have one of these at home and one in my desk at school:
https://www.walmart.com/ip/5440153180?sid=84f92787-f03a-4c66-b0b4-cfdbf49dbde8

Rolling my foot on it a couple times a day helps my feet quite a bit.

I also really like Oofos flip flops - they're designed for runner recovery and really make my feet happier.
[nhnsa2s] (score 1, diepte 0) I thought it was just a normal part of teaching to barely be able to walk when I get home lol. After reading these comments I guess not
[nhnuq08] (score 1, diepte 0) Are you reasonably fit?  If so,  then this is a concern.  If not,  then this has an explanation and a solution.
[nho360s] (score 1, diepte 0) I had to get a cortisone shot for plantar fasciitis, had hokas, Brooks, etc but Kuru online was the only shoe to calm down the PF
[nho3wg9] (score 1, diepte 0) I switch between Korean budget Crocs and New Balance. I've never tried Hoka it's a bit out of my budget. I normally spend $20-$50 on shoes - feet have been pretty healthy.
[nho3yat] (score 1, diepte 0) Sketchers are your best friend
[nho86hm] (score 1, diepte 0) Honestly, I find as long as I rotate my shoes and wear compression socks - I can wear essentially any shoe. My favorites are Sketchers X Jen Stark, Air Force Ones, Chuck Taylors, and Adidas. My Chuck Taylors and Sketchers are by far the comfiest!
[nhoah7n] (score 1, diepte 0) Adidas Ultraboosts or Hokas 

you could probably find ultraboosts cheaper
[nhpj4xv] (score 1, diepte 0) I got some “Skechers Women's Max Cushioning Endeavour Canova Sneaker” and they’ve helped a lot. 

I have a structural problem in my left foot due to an unaddressed top foot injury from over a decade ago. Arch started collapsing so I got fitted for some really expensive insoles. Arch stopped collapsing but all the pressure and pain moved to my toes, so I was still miserable. Had to find some shoes with evenly distributed support bc I noticed a lot of “arch support” shoes just have the heel really high up with no support near the toes. Basically felt like walking in heels.

My new shoes did give me sore legs for a few days, almost like I’d been to the gym squatting. But now they feel great. The pressure is off my feet and being supported by my calves instead of my heels and toes getting tormented.
(20 reacties met lagere score weggelaten)

=== THREAD 1ikzppz ===
SUBREDDIT: r/Frugal
DATUM: 2025-02-08  SCORE: 35  REACTIES: 95
TITEL: Sweaty feet driving up my heating bill.  How can I keep them dry and toasty?
POST (source_id=post):
Folks, I'm running out of ideas.  Heating costs went up 30% this year after going up 20% last year.  I literally cannot afford it.  I've been keeping my place cool, but usually my feet end up wet and absolutely freezing, so I'll end up turning on the heat needlessly.

I tried electric socks.  Food powder to absorb moisture.  Socks that are supposed to keep your feet dry.  Wearing slippers.  Warming my feet in hot water to warm them up.  

Any other ideas?  I don't wear shoes indoors, but I'm thinking about getting a pair of indoor only shoes.... even if it ends up a little swampy.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mbqlwca] (score 305, diepte 0) Merino wool socks
[mbqn5lu] (score 120, diepte 0) I’m a little confused.  Do you normally have very sweaty feet?  You could put antiperspirant on them, it won’t hurt.
[mbqmtxk] (score 73, diepte 1) This is the answer. Wool will keep you warm even when it gets wet AND is anti microbial. If you are just wearing then indoors, find 100% wool. Nylon is added to socks for durability, you don’t need that for around the house
[mbqmri6] (score 66, diepte 0) Wool socks can absorb 3X their weight while still feeling dry and will help keep you warm even when wet.

If you have hardwood or tile floors I recommend slippers.
[mbqo1wt] (score 59, diepte 0) Plantar hyperhidrosis is a medical condition. Have you already gone through the online treatments?
[mbqs4t0] (score 51, diepte 0) Talk to a doctor, can be a bunch of medical things that cause your feet to sweat when it's cool. It could be a simple fix like some supplements or something. Otherwise I'd go for wool socks and a blanket where you're sitting and slippers if you have to stand up.
[mbrzg7a] (score 39, diepte 1) To the top. Weird that the top 20 suggestions aren't -stop your feet from sweating-

12%+ clinical antiperspirant is the way to go. Not only will your feet be warm & dry your shoes won't be the optimal environment for fungus either. 

Feet sweat for grip, just like hands do... only problem is we wrap them up in shoes so the water can't evaporate. Or you unwrap them & the evaporating water carries away a ton of heat. I used to be able to torture my bedmate by touching them with my toes, now they are perpetually comfy. 

OP if you are averse to antiperspirant for some reason there are a couple of electric treatments to cut down sweating.
[mbqodj7] (score 25, diepte 1) This. 
I also rock a Snuggie and I love it. 
(Some places also have hooded pullover blankets now too. I dream to one day own such a thing.)
[mbqtzj1] (score 25, diepte 1) Wool socks and wool slippers and done.
[mbs7a50] (score 19, diepte 1) Darn Tough.

Yes, it feels weird to spend that much on a pair of socks. 

No, you won't regret it.
[mbqos5m] (score 18, diepte 0) A heated throw over your feet when you are sitting in one place. They use very little electricity compared to a space heater.
[mbrni8p] (score 15, diepte 1) Merino socks, and spray the feet with antiperspirant before putting them on. 


I have to do this even in winter. Still sweaty by the end of the day, but then I go home and change socks, so it's all good.
[mbrkivm] (score 12, diepte 2) Costco has some decent ones that are 85% wool. There not expensive... I want to say about $15 for a 4 pack. They are a must for me once the weather starts getting chilly. It's the only way my feet stay warm in the winter.
[mbrpm36] (score 10, diepte 3) Never again. I bought a pack thinking they would be nice but they are garbage compared to Smartwool and Wigwam socks. Feet were freezing in temps that my normal smartwool socks handle with ease.
[mbqn3vs] (score 10, diepte 0) I wear wool slippers
[mbr2v5f] (score 9, diepte 0) Could you be diabetic? Cold & wet feet could be a symptom of nerve damage. To warm up soak them in warm/hot water and put fresh socks on. Slippers that are wool lined or make your own (can be hand sewn and made from old jumpers or blankets). Use a tennis ball or roller to keep the blood pumping around your feet if you aren't mobile & check for low laying drafts such as baseboards gaps.
[mbquxyb] (score 8, diepte 0) I own the bottom floor of a duplex. My floors are cold. I am thinking of putting a second rug pad on the throw rung in my bedroom.

I wear wool socks in the winter. They can be washed in the drying but have to be hung dry. I also wear Ugg Ansley slippers around the house. It makes a huge difference in keeping my feet warm.

I don't have central heating, only through the wall heating in my living room. I dress in layers to stay warm.

I do not perspire at all. It would be helpful in the summer but I do not have to worry about my feet being wet from that.
[mbrzkqh] (score 7, diepte 0) BedJet. There is no way I could sleep with socks on. I bought my wife a BedJet for Valentine's Day last year, it's not cheap .. BUT ... It will save you from your high electric bill and will pay for itself in no time. It will blow nice warm air right on your feet.
[mbvenf2] (score 6, diepte 5) Just remember:  MERINO WOOL.  They are not thick socks, like other wool socks.
[mbrvewy] (score 6, diepte 1) That's what I do at night to warm up my feet. I sleep better if I'm a little cold but cold feet keep me awake.
[mbqp4lh] (score 6, diepte 0) Iron supplements.
[mbqsx7z] (score 6, diepte 0) A woman I know told me her doctor reccomended she spray her feet with anti-perspirant.
[mbrq837] (score 5, diepte 4) That's interesting because they're my favorite. They keep my feet warm and have lasted a few years with no issues.  But I don't do any outdoorsy stuff with them so maybe that's why.
[mbqmwjo] (score 5, diepte 0) Is it your hard floor? Use a rug?
[mbr07uv] (score 5, diepte 0) Wool socks, alpaca socks, see a doctor.
[mbr78z4] (score 5, diepte 0) Lots of people are saying wool socks. Yes, but also no. If your feet sweat when they get too warm but it's too cold to go without socks then you need TWO layers of socks. 

First a pair of THIN cotton socks. These will wick away any sweat to help keep your feet dry but they won't provide much warmth other than reducing contact with cold surfaces. Over these you put on a pair of wool socks. Preferably a pair that have  a ribbed texture (think about how the cuff of most socks has  the vertical striped texture - you want that, nice chunky thick ribs). These will trap air in the little pockets within the knitted texture that gets warmed by your body heat, this keeping your feet insulated. And because they keep your feet insulated, they will prevent the cotton socks that are wicking away the sweat from getting that cold clammy sweaty feel. 

Keep more pairs of cotton socks than wool and if they start feeling icky, remove them and swap out for a fresh pot and put the wool socks back on.
[mbreda2] (score 5, diepte 0) Wool socks.
[mbsjlnq] (score 4, diepte 4 OP) Thanks for the specific brand recs!  I'll give these a try!
[mbqn129] (score 4, diepte 0) when you're home are you staying in one place, primarily? my parents keep what they call a milk house heater in their tv room at floor level that keeps foot-level air warmer. and I have a little square ceramic heater I keep on the floor behind my desk chair (I'm at my desk most of the day) that blows the warm air under my chair and desk. I keep the door to my office room slightly ajar for circulation, but the little heater seems to do the trick. also a humidifier (cool air humidifier is fine) can help hold the heat in a room - this is what my parents have in their tv room - a cool air humidifier and the electric milk house heater.
[mbx2izv] (score 4, diepte 2) there's also the concepts of:
- rotating shoes daily with another pair 
- having a fan to dry out your shoes 
- never let the shoes sit wet for long periods
- change socks mid day or after long walks or activities
[mbsdv60] (score 4, diepte 0) My wife has rice bag slippers, put them in microwave. Some American Primeval shit, but it works.
[mbqopsl] (score 3, diepte 1) Yes upvote, I also add hey dudes which are my indoor shoes only 😝
[mbu34zj] (score 3, diepte 1) Darn tough socks.
[mbqokc3] (score 3, diepte 0) Wool socks or an electric blanket. With my electric blanket, I keep my heat at 60. I love it and so do my kitties… it’s cut my electric bill dramatically so his year!
[mbqomjh] (score 3, diepte 0) I got some really great cabin socks from Nordstrom rack. They’re so toasty, but breathable, plus they have rubber threads on the soles.
[mbqtyp0] (score 3, diepte 0) My dad used to wear two pairs of socks and let the inside socks with moisture to the outside socks. He would also sometimes put powder in the socks as well.
[mbquzx4] (score 3, diepte 0) Try some movement exercise
[mbqx7m8] (score 3, diepte 0) Wool socks, friend.
[mbqywe5] (score 3, diepte 0) I have a similar issue with the wet socks so I don't wear shoes or socks inside. Feet don't get as cold bc there's nothing wet clinging to them
[mbr8d75] (score 3, diepte 0) Wool socks + sized up Stegmann or similar wool slipper.
[mbrt5kj] (score 3, diepte 0) Wool socks, then a pair of cheap thermal socks, I get mine from Daiso for like 2$, and then a pair of house slippers on top of that. My apartment runs cold and I was having freezing toes all winter until I started this.
[mbruph6] (score 3, diepte 0) Get some slippers? Sheepskin lined ones will help keep your feet warm and wick away moisture
[mbrz3uv] (score 3, diepte 0) I have a heated floor/foot mat for under my desk. Combined with merino wool socks (and only merino wool socks), my feet are toasty without needing to turn up the heat in the entire house, or add a space heater to the office. They're pretty inexpensive too!
[mbs3g4c] (score 3, diepte 0) have you seen a podiatrist?
[mbvlw6e] (score 2, diepte 2) Maybe add a silk liner sock too...
[mbuhvrg] (score 2, diepte 4) Costco online currently sells Wigwam through the Costco Next program.
[mbqsjwj] (score 2, diepte 1) They are life changing.
[mc3mlhe] (score 2, diepte 3) Agreed.  Darn Tough brand are excellent
[mbu409i] (score 2, diepte 1) The 100% wool lasts way longer than the 85% wool for some reason
[mbqt1b2] (score 2, diepte 0) I wear a pair of slippers, that are close to shoes in look and build quality, and a thick pair of merino wool socks in the winter.
[mbqun0m] (score 2, diepte 0) Merino socks with soles, indoor shoes.
[mbqyzj4] (score 2, diepte 0) Slippers
[mbr6bln] (score 2, diepte 0) Antiperspirant. 

Get some speed stick, spread it on the bottom of your feet.
[mbvgpcx] (score 2, diepte 1) I agree, ***except*** that the socks closest to your feet should be thin BAMBOO, not cotton. Cotton will hold on to all that moisture but the bamboo wicks it away.
[mbrycno] (score 2, diepte 0) Socks and sandals
[mbumog0] (score 2, diepte 1) Same -- I LOVE my heated floor mat under my desk. Well worth the $35 or so, going strong in its 5th winter now. I also wear wool socks + felted wool or shearling slippers (make sure they are real shearling and not synthetic) in the house all winter.
[mbsoj80] (score 2, diepte 0) You could get botox in your feet.  Will stop the sweating.
[mbu1g02] (score 2, diepte 0) Just like Lieutenant Dan told Forrest Gump https://youtu.be/BpGWc27KLSE?feature=shared

Change your socks.  It is INSANE how much of a difference a fresh pair of socks makes.
[mbu9el9] (score 2, diepte 0) I’m a merino wool socks gal.

My partner does socks plus house shoes (a pair of Ugg boots. I know exactly where he is if he walks in the house).

We can keep the thermostat at 62 (and I drop it to 58 when solo.)
[mbxvuly] (score 2, diepte 0) deodorant on your feet and wool socks
[mbv7l1b] (score 1, diepte 2) these socks last forever. if you can afford the initial cost, these are an excellent choice.
[mc11h1o] (score 1, diepte 2) I really wanted to like my darn tough socks. But they are just too tight in the toe box and don’t quite fit right. Wore them a couple times and now they just sit in the drawer.
[mc264vf] (score 1, diepte 3) I believe Darn Tough has a different brand for very large/wide feet, Wide Open. Might be worth reaching out.
[mbryprt] (score 1, diepte 2) Me too.  It’s made a huge improvement in my leg pain
[mbr0945] (score 1, diepte 0) I wear wool socks with ll bean wicked moccasins when it’s super cold. Feet stay nice and warm and dry. It also helps to get up and get moving periodically. 

Please check with your doctor about the sweating and cold feet. It could indicate more serious issues.
[mbrigpx] (score 1, diepte 0) Electric plug in heat pad on the couch, at your desk, and in bed. Plus wool socks in winter / cotton socks in warmer months.
[mbrr5wv] (score 1, diepte 0) Disposable foot warmers. I buy a few packages each winter from Costco and put them on my toes inside my slippers and have toasty warm feet.
[mbrrofh] (score 1, diepte 0) I found a pair of almost new Uggs on Marketplace. They are my home slippers now
[mbrsgek] (score 1, diepte 0) I wear alpaca wool socks and change them a couple times a day. (Any) Wool won’t absorb as much sweat/ oil or get stinky as quickly as other socks, so I just leave them out to dry and wear them again for part of the next day or two before washing.
[mbrxue9] (score 1, diepte 0) Drysol is a prescription anti sweating medication and it's like $10-15 without insurance
[mbvygjn] (score 1, diepte 2) We are removing your post/comment because of affiliate or referral content. This includes:

- Affiliate links.
- Referral links or codes
- Offers to share either directly or in direct messages.

 Please see our full rules page for the specifics. https://www.reddit.com/r/Frugal/about/rules/

If you would like to appeal this decision, please [message the moderators by clicking this link](http://www.reddit.com/message/compose?to=%2Fr%2FFrugal&subject=Removal%20Appeal&message=Author%20would%20like%20to%20appeal%20the%20removal%20of%20their%20post%20because) within one week of this notice being posted.
[mbs33pj] (score 1, diepte 0) The ULPT answer is sell them sweaty feet pics
[mbsjd7r] (score 1, diepte 1 OP) I'm going to try these, actually.  Thanks!
[mbsecm0] (score 1, diepte 0) Down-filled slippers.
[mbsr2v7] (score 1, diepte 0) Keep them off of the floor as much as possible.  That where all the colder air is.

When I'm sitting down, I raise mine off the floor, keeps them so much warmer.
[mbsymm5] (score 1, diepte 0) Hot water bottle for the cold
[mbtcotf] (score 1, diepte 0) Slipper socks - they're extra thick and cushioned, but pull on like socks to keep your ankles warm
[mbtijoa] (score 1, diepte 0) I also change my socks when I get home. I do wear indoor shoes. I second the wool socks.
[mbtitx1] (score 1, diepte 0) Get rechargeable hand warmers and an electric mattress pad. Warms you up quickly!!! Also they do make heated vests.
[mbtn77j] (score 1, diepte 0) Wear a thin pair of socks and cover them with a thick pair of socks. When you get cold, change socks. Rotate your footwear so they always dry out. Hot water bottles under feet when relaxing at home.
(22 reacties met lagere score weggelaten)

=== THREAD 124aedv ===
SUBREDDIT: r/pharmacy
DATUM: 2023-03-28  SCORE: 88  REACTIES: 95
TITEL: My feet are killing me, I have this sharp pain at the back of my foot and I have no idea how I’m gonna go to work tomorrow and stand all day again.
POST (source_id=post):
My feet really hurt

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jdylffo] (score 54, diepte 0) Give yourself a foot rub and bend and flex your foot to stretch and relax the muscles. Epsom salt soak may also help. If you have any pain on the sole of your foot, especially as you walk or put pressure, then step on a tennis ball and use it to rub the sole of your foot. You could also freeze a water bottle and roll the bottle back and forth with your foot. Elevate your feet and put the pillows under your knees too so they aren't locked. If you have ace bandage then wrap your feet snuggly and elevate your feet. You could also wear compress socks while working, although I haven't tired that before.

Dansko shoes have saved my legs and back. I have flat feet so being on my feet 12hrs is tough. With those shoes, it's absolutely no problem. For me, they are well worth the price. They look like clogs, but I just get the all black ones and my pants cover them anyway. I also used them when I started APPEs in school. I did 12hr shifts running around hospitals. I'm so glad I got them after seeing all the nurses in the hospital wearing them. 

Absolutely recommend. I will never use anything else for work. I know your pain and I'm sorry. Hope you feel better and I hope you try those shoes.
[jdz110l] (score 51, diepte 0) Sit on a stool. If anyone says anything, DARE THEM to put it in writing. They can't retaliate against you for having an injury. Bring up the ADA and they will shut up real quick.
[jdzb93c] (score 40, diepte 2) Larry Merlo
[jdyqsba] (score 25, diepte 1) I tried it all: adidas, Asics, hokas, compression socks, stretching, ibuprofen, icing, massage machine, roller ball. You name it I tried it.

Nothing worked. I moved to California and have a stool to sit on. Magically my chronic foot pain disappeared.

Literally it's inhumane to make someone stand for 8 hours straight.
[jdyj3en] (score 22, diepte 0) Urgent care. Doctor’s note.
[jdynfqa] (score 21, diepte 0) You have planter fascitis. The shoes you are wearing have no arch support.  

The long term solution is to go to a quality shoe store, get measured and fitted professionally. Buy a quality pair of leather shoes like SAS. Try different brands on to find what's comfortable for you.

In the meantime, go to the Dr Scholl's display like at Walmart and purchase arch supports for planter fascitis. I know you want soft to walk on, but what you need is a hard arch support.

You also need to do daily exercises until you get good shoes. The best one is get a cold can of pop, sit in a chair, barefoot, can under your arch and roll it back and forth stretching the muscles in your arch to lessen the pain in your heel.

I've been wearing SAS shoes for years, no more problems since.  Always wear shoes, don't go barefoot or wear flip flops.

Source: voice of experience.
[jdyjgly] (score 14, diepte 0) Hoka bondi's
[jdylknc] (score 12, diepte 0) I get it too, compression socks hoka one one, ibuprofen best I got. Won’t eliminate it completely but might Atleast make it bearable.
[jdyn696] (score 10, diepte 1) I do all of that and it helps tremendously. I also wear oofos recovery sandals at home
[jdyqosw] (score 8, diepte 1) Not necessarily plantar fasciitis. For that, the pain was on the bottom of my foot by my heel. If the pain is on the back of your foot by your heal, it could be Achilles tendonitis or posterior tibial tendonitis. Ask me how I know.... 

Make sure you are not only stretching your feet and calves, but also your hamstrings. I agree with all the recommendations above. Good advice!! One exercise you can do is put a wash towel under your foot and try to scrunch it up with your toes, then unscrunch it with them.     You can also roll a frozen/cold golf ball under your foot to try to massage/stretch it. The can works better if it's really sore though.
[jdzu6c1] (score 8, diepte 0) Call in, go to the doctor, get a work note for special accommodations
[jdzqvst] (score 7, diepte 2) 8 hours? I’d take that over my 12 😅…
[je39hat] (score 6, diepte 3) I sometimes take an empty 60 dram vial into the backroom and roll it under my foot at work when my feet are killing me lol
[jdzaqy7] (score 6, diepte 2) I just need to lose weight as well I’m fat lmao
[je0ka9w] (score 6, diepte 1) While this is the best and most helpful advice it’s honestly not realistic. When I worked retail I worked in a “low volume” pharmacy which everyone just assumed meant I twiddled my thumbs all day. No, it meant I had less staff so I had to be in 7 placed at once instead of someone who works in high volume and has 3-4 techs with them. I’m in California so ive always gotten a lunch but if I didn’t, beyond that there wasn’t really ever time to sit — I’d sit down and 15 seconds later there would be a question at the window, or a vaccine, or I have to go do some kind of tech work.
[je0whzt] (score 5, diepte 2) I love rolling a tennis ball 🎾 under my feet at the end of the day.
[je52xvs] (score 5, diepte 6) Then you sip 20 times per day as needed
[jdyrrb2] (score 5, diepte 2) Oh I agree fully I get this knife like sharp pain in the center of my heel. Idk what to do, I don’t know how so many pharmacists and techs and assistants can stand all day I sure can’t.
[jdz9h9i] (score 5, diepte 1) I just bought some hoka arahi 6 shoes and my feet feel a lot better.  I need better compression socks.  I tried Feetsure Plantar Faciitis at the store and they felt great.  Right now I just use Bombas cuz they keep sending me free socks.
[jdyp0l7] (score 5, diepte 0) Plantar fasciitis potentially? Get a lacrosse ball and massage it out every night. It will hurt, but it works. There are foot stretching apparatuses you can sleep with that help as well. Lastly, freeze a few Dixie cups full of water. Once frozen, tear the top layer off and massage onto the heal prn. Obviously, NSAIDs as you see fit.
[jdyrn6n] (score 5, diepte 0) Hokas are good but damn my feet never hurt when I wore crocs.  

I miss wearing them so much
[jdyj56a] (score 4, diepte 0) Orthopedics hella cloud shoes
[je3rack] (score 4, diepte 4) And then put it back into the vial stash
[je4pnuf] (score 4, diepte 5) Lololol, no, then I pour some Dr Pepper into it and it's my fancy cup of the day
[jdzc86y] (score 4, diepte 1) Crocs actually [makes some shoes](https://amzn.to/3Zn9WoT) that you might be able to wear to work.
[jdzrumt] (score 4, diepte 0) I've had a variety of foot ailments through my 25 years in hospital pharmacy. Thanks USP 797 for no cushion floor mats in the anteroom, thus standing on epoxy covered cement all day long. (Yes, I'm aware there are autoclavable floor mats. Our sterile processing department won't do it.)

I used every major brand of running shoe and got the maximum support/cushion model. That would usually help but then I would have that week where I knew the shoe gave up and said you're insane, I'm done supporting you and it was time for new shoes accompanied by a week plus of plantar foot pain. Sometimes it was knee pain. Other times back pains. I tried custom orthotics and those were fine but having them for every single pair of shoes is expensive or I was just too lazy or forgot to take them out and they didn't always fit the shoes I changed them over to.

Then I saw a post somewhere on social media about minimalist shoes and how disconnected we are from any type of biofeedback with the thick soled running or support shoes and devices. Gentleman mentioned how the feedback of walking and even running with no support caused you to fix your gait and strengthen the small muscles in your foot, ankle and lower leg. It made sense to me. Through the evolution of humans over time it's only in more recent history where we've had these thick soled shoes. 

I tried a pair of one of the brands of minimalist shoes. I started slowly, just wearing at home and then to work bringing a back up pair of shoes. There were some tough days where I switched back to my running shoes. But then there were those days where I gutted it out and I realized that I was naturally trying to walk in a way that didn't make the soles of my feet ache. Then slowly but surely the pain subsided. I kept pushing and started to wear the minimalist shoes on the 3 and 5 mile walks I would take with my wife. I've even worn them chasing my sons around a cross country running course. (I make CC a spectator sport) I log 3-5 miles myself as I sprint and run around cutting through the middle of the course to cheer them on at multiple points. No foot related pains.

I haven't looked back. That was three years ago. I still have that first pair of shoes. I'm slowly wearing through the sole. I inquired about a new pair of inserts from the company I chose because I had worn out the insert. They sent me new for free. I've since bought another pair because I liked the new colors they had and wanted to switch it up. But I still throw on those original ones from time to time.

Foot pains, back pains, knee pains, all of them gone. Get over the current pain and ailment. Then start to strengthen your foot, ankle and lower leg by learning to walk again without the thick soled shoes. Your body will adapt. Then you won't need all those thick soled support products again. Try the minimalist shoes. It worked for me. 

If anyone is interested in hearing more, shoot me a DM and I'll share brand information or respond if you have any questions.
[je092sj] (score 3, diepte 2) It’s anything you want it to be, if you’re brave enough.
[je0j2te] (score 3, diepte 3) Lol I’m mildly overweight too…. Need to lose like 40-50 lbs. 😭
[jdypa38] (score 3, diepte 0) May be the shoes. I currently wear Kuru, and I love them.They have extra cushions, even at the arch or your feet. They're kinda expensive, but really worth it. I've had mine for a year now and my feet have never hurt in them.
[jdzpcox] (score 3, diepte 1) heck yeah another Kuru fan in here 😎

Seconding this recommendation, I just bought two new pairs after my foot pain started creeping back and I realized it had been over a year since my last purchase. Currently in the middle of an exchange since the slip-ons are too short for my feet, but otherwise I have had nothing but love for these guys.

They also offer wide widths of most of their styles for folks who need that sort of thing.
[jdytvp9] (score 3, diepte 0) Slightly lower price point options than Hokas are On Cloud Monster and various New Balance styles. Fleet Feet charges MSRP but you have 60 days to return/swap out. Good luck
[jdzuykr] (score 3, diepte 3) The way I laughed.
[je13ant] (score 3, diepte 1) Submit for a medical accommodation through HR
[jdz778p] (score 3, diepte 0) See a podiatrist. The many things that go wrong when a person stands eight hours a day, every workday, will make you wish you were dead. G-Defy shoes work for be. 

Signed, another voice of long experience. (Heel spurs, plantar fasciitis, flat feet)
[jdzkvy0] (score 3, diepte 0) Go drag a stool from photo back to the pharmacy. Sit!
[je0sxp5] (score 3, diepte 1) Just curious what brand do you like in the minimalist shoes?  I've been considering giving them a try and am kind of at a loss, a lot of the brands on amazon seem like the junk brands that have flooded amazon in so many areas with made up names.  Thanks!
[je07a5j] (score 3, diepte 0) I developed tendonosis of my achilles tendon, tore a tendon in one ankle, and ruptured a tendon which led to a dislocated toe due to severe hammer toe. All from not having good arch supports. I still work, but many days me feet kill me. 

Long term invest in good shoes even if they're expensive,  you only have one pair of feet. Short term, soak them in a good hot water Epsom salt soak. I got a foot tub for not a lot that I used almost nightly, it really helped a lot
[je0jh4v] (score 3, diepte 0) Custom orthotics. I had plantars fasciaitis and peroneal tendonitis (which was the worst of the two, I limped everywhere) from constantly changing directions in our understaffed pharmacy that did not resolve until I had custom orthotics. Worth every penny.
[je0on8f] (score 3, diepte 0) I had a pain in my ankle and went to the doctor, he saw that I wasn't standing correctly and probably I had old worn shoes that contributed to the problem.  I got new shoes and arch support and the problem went away almost immediately.

At WalMart, they have this machine you stand on in socks and they test how your foot is pressuring the floor, then they recommend a correct orthotic for you.  It was the doctor that recommended using it and just getting what they suggest.  They were a bit pricy like $60 a pair but worth it.
[je1ab93] (score 3, diepte 0) I recommend Clove shoes! tbh, it’s not like the shoes will dramatically impact the pain/comfort but as a “former” sneakerhead who’s tried almost every brand out there, i found the comfort and support to be among the most consistent. (at least, in a retail setting)

i’m an overall fan of stuff like Flyknit on shoes but the lack of support some of them have end up hurting my feet more because of how much i end up moving around.

treat yoself. $100-200+ on shoes might seem like a lot but it’s a worthwhile investment when you’re on your feet so much. i know this doesn’t address your issue directly but i think it’d help in the long run
[jdyl3s9] (score 2, diepte 1) Arch support pads in my shoes have really helped my feet and knees
[jdzbu6h] (score 2, diepte 1) [These ones?](https://amzn.to/3Kds0O1)
[je5l2q4] (score 2, diepte 7) You're good. Too good.
[je7gvhx] (score 2, diepte 8) That's what my patients say when they start with 5 days of oxycodone. I eventually see it filled for 30 days 😂
[jdymnyx] (score 2, diepte 0) Compression socks ftw.
[je30b54] (score 2, diepte 1) Thought that is what I have. Got X-rays; heel spurs on both feet. The even match : )
[je3484w] (score 2, diepte 2) Did they recommend surgery?  Change of diet? That's no fun 😭
[jdywkfb] (score 2, diepte 1) Hokas even in wide were too narrow for my bunions (which I'm sure are not helped by standing 8hrs everyday). Crocs with insoles are where it's at.
[jdyumcm] (score 2, diepte 0) I definitely get 1 90 min massage each month.  I also have a foot bath at home that helps relax.  Currently I wear a very good pair of all black under armor sneaker.  light weight and gives firm support.  Ive also worn plantar fasciitis inserts that  really helped.    Stretching helped as well!
[jdywnv5] (score 2, diepte 0) Seconding the frozen water bottle. Ice, ice baby!
[jdz4pls] (score 2, diepte 0) Hi, I feel you. Been dealing with foot pain for over a decade and didn’t do anything (other than get carried into urgent care) until I fell on the stairs. Instead of steroid shots, I opted for physical therapy…and it helped A LOT. I’m not completely better but I know what to do to avoid a flare up. You can look up videos for calf stretches online. Icing the area also helps. 

In addition, having a podiatrist measure my feet and recommend insoles has helped a lot.
[jdzlknu] (score 2, diepte 0) I wear Skechers arch fit shoes, I bought the weird braces that hold your feet in a flexed position while you sleep, I wear Oofos sandals in my house, I have a roll foot massager thing I found on Amazon that I keep at work. I dealt with Plantars fasciitis for about 6 months a few years ago, using everything above finally got rid of it. I don’t use the braces anymore, and I sit for part of my shift now when my feet start talking to me. 

If it’s really bad, go to the doctor, get a note and maybe a steroid.
[jdzlumr] (score 2, diepte 0) Sit on a stool if you need to. Explain you will need to go home sick if required to stand all day….
[jdzncdx] (score 2, diepte 0) Which shoes are you wearing?
[jdznfne] (score 2, diepte 0) For all of us who refuse to stop wearing flip flops.  I can’t recommend Dr Comforts flip flops they have excellent arch support
[jdzqqyy] (score 2, diepte 0) When I was doing APPE i had to go over the other side and buy some dr. scholes cause my feet hurt as well. Have you tried that?
[jdzuiqi] (score 2, diepte 0) Agree with those saying rub and stretch your feet. I also agree about a stool. I also suggest you go to a podiatrist. Even something as simple as plantars fasciitis can lead to requiring surgery if not treated properly. My wife got some insoles for her shoes from the podiatrist that have basically cured it.
[je04ni0] (score 2, diepte 0) Can you get special shoes? It used to hurt to even drive home at the end of the day.
[je071cr] (score 2, diepte 0) Get a Foam roller and roll every part of your body

Stretch everything and take your time doing it

Tennis ball/cold soda/ frozen Dixie cup, rub the bottom of your foot or back of your leg 

Take OTC naproxen if you aren't already on an NSAID

Sleep with your feet elevated 

Get "zero elevation" shoes with arch support. They'll prevent stress on the plantar and Achilles tendon

Ice bath if you're really feelin it 

Compression stockings 

Use a stool!
[je0iu4q] (score 2, diepte 0) I used to get terrible heel pain, was ignoring the old shoes I was wearing. It was so bad that I was trying to stand on my tippy toes at the counter because I couldn’t bear the pain of standing and walking 😅 Switched to Sketchers max cushion a couple months ago (didn’t want to splurge for Hoka’s, figured I’d try the cheaper option first and if it sucked then I’d move on, but we’re &gt;3 months in and still going great so far) and started wearing compression socks and it’s gone. Can’t say that’ll fix it for you, but a new pair of shoes and maybe some compression socks might help.
[je0j00b] (score 2, diepte 0) I had to see a foot and ankle specialist and he recommended Tuli cups (silicone heel cushions) and Pulse orthotic inserts by PowerStep. They helped tremendously inside a Merrell hiking shoe. Definitely use the frozen water bottle.
[je5hvrv] (score 2, diepte 2) Went to a podiatrist for diagnosis. They did a laser scan of my feet and then sent off for custom orthotics. I need to go back this year before my insurance restarts and get another for some custom mocassins. They accidentally double billed me the first time so I actually got the second pair after they met my deductible for free, fully covered by my insurance (and I met my deductible months ago already this year). First pair was around 200-300 dollars but worth every penny. Lasts 10 years.

They had initially put me on specialty orthotics for high arches, but I was burning through them so fast they determined that I was running around on my feet too much for those to be practical (because specialty orthotics only last 6months, but mine were lasting 2 months at most for me).
[je0mxov] (score 2, diepte 0) It’s not much, but I wore compression socks and changed them at lunch. It seemed to help
[je0s8fl] (score 2, diepte 0) What if you sit at least 12 hours a day?
[je15dlx] (score 2, diepte 0) Kind of sounds like a heel spur. Take an anti inflammatory and look into shoes with good arch support as this can be related to plantar fasciitis. Unfortunately foot pain is common when you’re on your feet all day. I personally never call out unless I have a raging fever and/or vomiting/shitting.
[je307mh] (score 2, diepte 0) The most important stretch you can do is to flex your foot with your knee straight. Most PF is caused by overly tight gastrocnemius muscles (according to my podiatrist). You can stretch with a belt or long strap. Either sitting or lying, put the strap under the ball of the foot and flex the foot toward your knee. You should do this stretch at night and also in bed before getting up in the morning. Ice and ibuprofen are your friend.
(26 reacties met lagere score weggelaten)

