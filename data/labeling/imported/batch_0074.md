# Label-batch batch_0074

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
Schrijf het resultaat naar `batch_0074.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: qjg147, 1hp61xv, 16nyj3d).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD qjg147 ===
SUBREDDIT: r/AmazonFC
DATUM: 2021-10-31  SCORE: 42  REACTIES: 109
TITEL: I’m in afe pack and my feet absolutely kill me, and to make matters worse , I weigh over 200lbs so it’s like my weight is on my feet. What can I even do to reduce the pain?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hiqc26u] (score 55, diepte 0) I’m an overweight lady so I understand this. I invested in a goo d pair of shoes that take care of my feet. Try out some insoles too and see what helps. 

I also soak and ice my feet (the ice is mostly for plantars Fascitis in my foot). I also bought a foot roller to roll the muscles in my foot and loosen them up. That helps a lot!  You can also take a towel or resistance band or belt and help stretch out your foot. 

Other tips is Tylenol and sleeping with your feet elevated. Inflammation causes a lot of pain in the feet so mild pain killers and elevation will reduce inflammation and reduce the pain. 

You can do one of these or mix and match. Find a combo that works with alleviating the pain.
[hipx5ie] (score 40, diepte 0) I lost 20lbs and it made a huge difference. Being in your right weight is honestly the best thing you can do. In the meantime get some good socks, comfortable shoes, and wear insoles.
[hir7f6d] (score 30, diepte 1) Just a word of advice. You shouldn’t take Tylenol every day. Acetaminophen will damage your liver with prolonged use.
[hipwvqo] (score 19, diepte 0) Lose weight is the best option you have
[hiq28bk] (score 16, diepte 0) Insoles insoles insoles! Try ones for plantar fasciitis. Cheaper than shoes! Can use them in multiple shoes! Maybe compression or thick socks too.
[hiq80yo] (score 14, diepte 0) I've worked at Amazon for 3 months in single pack

I weigh like 180
I wear compression socks
I take anti inflammatory pills along with bog standard pain killers before and during my shift.
I bought expensive ass footwear that are designed to be stood in all day
I bought some highly recommended insoles
I soak my feet in an ice bath with Epsom salts everyday when I get home

Yet my feet fucking kill all day still :(

Pretty sure my last option is to pretend I'm now permanently wheelchair bound and roll my ass in everyday instead
[hiq6uzn] (score 13, diepte 3 OP) Tell me something I don’t know, I can’t lose it overnight, so for the time being I’m looking for alternatives.
[hir9jxx] (score 12, diepte 2) Also ibuprofen will damage your testicles if taken often.
[hiqacjo] (score 10, diepte 1) Careful with the painkillers - I'm not a Dr, but Ibuprofen should be easier on the liver than Tylenol - but take some care with both. Yes - I'm sure they're needed... please take care to press through the upcoming peak season with your body intact.
[hirkq1q] (score 9, diepte 2) I personally have members of my family who use to take BC powders and Tylenol every day for "pain." "Do you stretch everyday? Do you exercise?"

Always the answer "no." But they feel pain so they're gonna drug themselves up till they don't, meanwhile their muscles are tighter than a nuns puss causing them immense pain that could be minimized with a simple daily stretching routine aka self physical therapy.

I even have grandma's who continue to pay a chiropractor for weeks of "adjustments" only to go back in a couple months to do it again. It's like bro, how the fuck do people get this way? So tragic watching your own family do dumb shit and refuse to change or listen to anything you gotta say.
[hiq6q1a] (score 8, diepte 0) In the same boat, I’m a picker tho, if you can lose some weight even like 10/15 lbs makes a huge difference and if you can get a pair of adidas ultraboosts theyre super comfortable
[hiqhv2h] (score 8, diepte 0) Make sure you have proper fitting footwear. I never realized I had WIDE feet until I started working for AMAZON. 

Also, you feet can swell as much a 1/2 a size during a long shift. Always pack a second pair of shoes/sneakers and keep them in your car. If it gets "that bad" you can always run out on break and change them.

I'm 50 lbs overweight, so I get where you are coming from. I truly thought working for AMAZON was going to make the weight fall off me. 

I love my job, but I haven't lost a single pound. I take 3 Advil, wait two hours, then take 3 Tylenol to get me through. There are people larger than me. I have no idea how they do it.
[hiqfhkt] (score 7, diepte 2) Insoles make all the difference. If you e ever seen the Dr Scholl’s machine (usually at big box stores, like Wal mart) you stand on it and it will tell you your pressure points and what insole number to buy. They’re more high end and go for about $60, they’re different than the other ones they sell but they’ve made a world of difference for me. I feel less fatigued and no pain. You can also buy them with your HSA/FSA account if you have one. Other than that, use baby powder or gold bond, you don’t want blisters.
[hipwi3a] (score 6, diepte 0) Get better shoes/comfy
[hiqsvgv] (score 6, diepte 0) As a 5’2 dude who’s weak af and 230 pounds, I strongly recommend sole’s for your shoes, maybe even just get new shoes overall that properly fit. Stretching is also super important. Yea it’s annoying that they bitch at you a lot about stretching but it helps. Since you’re in pack, make sure you really stretch out the calfs and quads, ankle rolls, and some wrist rolls. Hydrate alot and pace yourself as well. The work isn’t going anywhere, and you don’t want to hurt yourself in the process. Also, if you’re new at your building, it’ll take about 3-4 weeks after your first day for your feet to get used to it. It’s tough but you eventually reach that point. On my second and third day of stowing, I was basically collapsing and felt everything in my lowerback, feet and hips. If these things still don’t help, then you can try a lidocaine patch/cream for your feet or even compression socks. Hope this helps.
[hiqika5] (score 5, diepte 2) Amazon will buy you comfortable shoes
[hiqv74c] (score 5, diepte 2) Use the zappos coupon Amazon provides for insoles, and go to crossover healthcare if you're where they are. Low key it's one of the best and least used Amazon perks. It's very cheap for Amazon employees.
[hiq71io] (score 5, diepte 1 OP) Thanks :)
[hiqimve] (score 5, diepte 3) You could be flat footed
[hiqdx32] (score 5, diepte 0) Other than weight loss, the best thing you can do is invest in a good pair of shoes and insoles, get some biofreeze for your feet after work, and when you’re working try to walk around and stretch. Standing in the same spot all day will definitely hurt your feet.
[hiqi9te] (score 5, diepte 0) Ask your safety team about getting some safety shoes, each AA gets a $110 credit to Zappos w free shipping included. The shoes will need to be broken in and they’re not attractive but they are free and designed for work. I believe insoles are also eligible.
[hiqmsfy] (score 5, diepte 0) Same as everyone else is saying about shoes, but my own advice is to get shoes a half size bigger for the swelling for work. If you end up getting steel/composite toes like others suggested, 100% make sure you half size up. 

Go for a short walk every hour (keep under 5 minutes between scans), it helps take the weight off and provided me some relief while I got used to standing all day.

There are places you can go get custom insoles for your shoes where they will take imprints of your feet and they will make some tailored to your body and activity. These are covered by your benefits - you would need to pay up front then submit for reimbursement. 

It sucks at first, I remember when I started my feet hurt so much I could barely deal with the pain walking all the way to the break room because it was the opposite side of the building - I ended up taking my breaks sitting on a step stool at my station instead 🙃 (probably not allowed but nobody saw/said anything about it to me). 

It is just work hardening though! You will get used to it and the pain will get better in time. Also, since you're standing all day you probably will lose some weight working at amazon as well. 

Good luck!
[hiquo7s] (score 5, diepte 2) You know when you pack theres people putting items in the walls behind you ya ask to train in that
[hipwom7] (score 4, diepte 1 OP) Yes I know, but it’s worse when you’re close to obese >~<
[hiq9hu0] (score 4, diepte 1) Bro

![gif](giphy|wCG00aS1PTQys)
[hiq775w] (score 4, diepte 1 OP) I will try that out , thanks!
[hirc9ka] (score 4, diepte 1) God bless compression socks. Ironically I buy mine on Amazon
[hirn4m3] (score 4, diepte 1) Ultraboosts really helped me too
[hiqei3w] (score 4, diepte 0) Weight training with emphasis on legs.  This will take some of the pressure of just your feet and will also help you lose weight.  Win-win.  Oh and you'll just overall feel better.  Win-win-win.
[hiqf3jy] (score 4, diepte 0) Soooooo. I grew up working in my dad's shoe repair shops, then owned my own for years.

The best over the counter insoles we ever carried were a older version of these-

Powerstep- Pinnacle Arch Support Insoles
 https://www.amazon.com/dp/B000KPKMX0/ref=cm_sw_r_apan_glt_fabc_J84MQAYJ7PVN8BTHACZV

I have those in my shoes right now and they're great!
[hipwrn2] (score 3, diepte 1 OP) I’m working on buying some but for now, I’m pretty much fucked
[hiqksdz] (score 3, diepte 0) I know everyone is saying shoes and they are right, you definitely need better shoes, however, another thing that could help is back support. I got a back support brace that made me stand up straight and that helped me with my stance and then my feet hurt way less. 

Supportive shoes, compression socks with arch supports and a back brace makes a dream team. I'm on the outer limits for my weight to height ratio at 6' and 175 so I definitely feel heavy and my feet suffer tremendously when I don't wear my support gear.
[hiqu4ii] (score 3, diepte 1 OP) Thank you very much!
[hiqmwxi] (score 3, diepte 0) Ask to train for rebin trust me it helps your feet a lot
[hiquwyb] (score 3, diepte 2) Rebin is the people who take the individual items from the grey trays and put them into the chutes for the afe packers to pack. In my FC the rebin side doesn’t have the anti fatigue ergomats. So rebin was worse on my feet. I wear double socks. It’s better cushioning, but just remember to loosen your laces to compensate for the increased size of your foot with two socks on.
[hiquhuv] (score 3, diepte 0) Double socks
[hir2l3n] (score 3, diepte 0) squats
[hir6nrc] (score 3, diepte 1 OP) Well sir/ma’am that’s one way to put it
[hir6cmm] (score 3, diepte 0) Lose weight..
[hir6lho] (score 3, diepte 1 OP) Work in progress…
[hir86pg] (score 3, diepte 0) Buy some Ultraboosts.
[hirg7pl] (score 3, diepte 0) My feet never killed me when I was in AFE (I’m 180 and I moved around too much) but being in single pack made me realize how much back pain I was in. Like I was throbbing after several hours in that space. I got my shoes through Zappos and boy did it make a difference
[hiri77u] (score 3, diepte 0) Easiest thing that's a huge help for me is just taking off my shoes in my car on break, and keeping an extra pair of socks on me to swap when putting them back on. I rotate days on Aleve, Tylenol, and Ibuprofen.
[hirplmi] (score 3, diepte 0) That place is torture to the feet.  I do just flex and feel it after a 3-1/2 hour shift
[hirwoyt] (score 2, diepte 2) For right now, wear your work shoes only for work; the soles will become impacted over time. When you are done work, immediately change into a different pair, and only wear them for work. An insole can help stave off having to buy new shoes right away, but not for long if you've already worn the shoes down. Change the insoles at or before the recommended time...that info will be on the insoles' packaging, but you yourself will be able to tell better than a chart when you need to replace them. And, if you've never worn them before, only buy one pair at first so you can see how well they work for you (or if you need a different kind.) 

Regarding medication, that's up to you. I had Plantar Fasciitis and had the "warts" removed by a doctor. I've also got diabetic neuropathy and was on Neurontin for it but it didn't really help; they just kept upping the dose. My husband then learned about Lyrica from a podiatrist (at a party, no less) and they suggested that it might help. WOW, did it help! You can only get it by prescription, but it's generic, finally. I had a place on my chin which was numb ever since I was 16, but the nerves grew back because of the Lyrica! So that's another option to explore if you aren't getting any relief. As for the acetaminophen and ibuprofen, everyone's already addressed that, but please do be careful! 
 
I really do hope that you find relief soon! Good luck! (Source: I was a CNA for 15 years and *always* on my feet.)
[hisdfrd] (score 2, diepte 2) Amazon has a shoe program that pays 110$ towards shoes check it out
[hist3y9] (score 2, diepte 2) Take advantage of Amazon's Zappos shoes program. I have the Sketchers and they are comfy as hell.
[hiqskx8] (score 2, diepte 3) 🤣🤣
[i5r52d6] (score 2, diepte 2) safety will get bored of checking shoes soon enough.  Stay strong
[hisl2ik] (score 2, diepte 1) Just Sayles this today from a post about 'the best life-changing $100 you could spend' - and it was about insoles.

https://www.reddit.com/r/AskReddit/comments/qjp0n0/what_item_under_100_significantly_improved_your/hirebnc?utm_medium=android_app&utm_source=share&context=3
[hiqbp9i] (score 2, diepte 2) I take Ibuprofen every working day 3 lots every 4 hours everyday without fail, I only usually use paracetamol (Tylenol) with it when my feet are especially hurting. I think I may just have terrible circulation in my legs and feet no matter what so to be honest most people should be fine doing all the above remedies, I'm just one of the unlucky ones who's feet swell after a few hours of standing lol
[hisghre] (score 2, diepte 2) Oh I hope my response didn’t come off as me recommending to take it every day! I only take pain killers on days that are particularly bad.
[hiv52nj] (score 2, diepte 1) Is there any way you can ask to get accommodations? Its as simple as having an ergo mat at your station!
[hiqh95x] (score 2, diepte 1 OP) Yes for sure ! My feet feel completely different once I start walking around and stuff it’s crazy
[hisozzw] (score 2, diepte 2) Transfer to pick if you can, honestly. My knees are not so great and they start to hurt bad if I stand in place for more than 3-4 minutes but I do pick with no problems because theres a lot of pacing back and forth
[hiqolyx] (score 2, diepte 1) What brace did you get? I'm thinking about getting one because I have terrible lower back pain and sciatica. I pop ibuprofen/Tylenol beginning and end of shift.
[hiry8sx] (score 2, diepte 2) It was one from walgreens in their sports medicine aisle. I don't remember the name/brand because it was two years ago.
[hiqu02o] (score 2, diepte 1 OP) What is that?
[hiqupuc] (score 2, diepte 3 OP) Ohhh I see
[hir1k1q] (score 2, diepte 3) It’s the pressure of standing of in the same spot all day that’s hurting OPs feet at least when you rebin you get to move a bit
[hiqwobp] (score 2, diepte 1) Unless you’re in one the few sites with mats for rebin your feet are gonna hurt a hell of a lot more
[hiqtxhh] (score 2, diepte 1 OP) Thank you!
[hirdm9c] (score 2, diepte 2) My feet hurt after 8 hours with one pair of shoes but not with the other, you want get some really comfortable running shoes with a lot of foam, if you wanna go all out get the super effecient nikes that allowed athletes to break marathon records by like 5% time. My smart watch show me salking 24000 steps after 8 hours thats basically half a marathon at 11.5 miles.
[hir8a7z] (score 2, diepte 0) I weigh 280 lbs and have fallen arches (flat feet). My right foot has plantar fasciitis. I used to have it in my left foot and am praying it doesn’t come back. 

I’ve been on the floor for just over a month. While it has gotten a little better, I am pretty useless after a shift. I can only really do things on my days off. Every night I ice my feet with these ice packs that are foot shaped. Then I soak them in hot water with epson salt.  Next, I use a foot massager for a bit. When I get into bed, I use a robe belt and stretch my feet. When I sleep, I put my plantar fasciitis foot in a brace. I stretch my feet again when I wake up. I also do this sort of lunge maneuver throughout the day to make sure I stretch my feet. 

I bought two pairs of new balance 1080v11 and super feet orthotics for flat feet. I was reading that it’s important to rest running shoes for a day or two between heavy use to give the shoe time to bounce back and dry out. I have also lost 20 pounds since I started. 

I know this sounds like a lot, but my foot pain has gone from a 10 while on shift to a 6. I hope it continues to get better, but I can handle a 6. My site is supposed to require safety shoes in January so I need to start breaking mine in soon. That is going to suck because I average 24k steps per shift.
[hirlo3w] (score 2, diepte 0) I pull my old soles out and get 2 more to put in
[hirrc0k] (score 2, diepte 0) I’m overweight as well, but I can tell you eat since I’ve started exercising regularly and shed a few pounds, my feet don’t start hurting until the end of my last shift every week. I also bought some Dr. Scholl’s insoles for extra comfort.
[hirvk0f] (score 2, diepte 0) Get better shoes
[his0k2k] (score 2, diepte 0) The only shoes I wear are Vionics. They properly align your feet, pretty sure they are good for overweight folks, too. These shoes have great arch support and a deep heal, they are extremely comfortable for my old feet. I have overpronation, before Vionics I had terrible knee and foot pain. With these shoes I have no pain. I buy from vionics.com or on payments through QVC. QVC as videos if you're curious about them, just search Vionics pick a shoe and there should be an explanation and video.

 They are expensive, my High Top sneakers look like boots, easy to put on and take off with a side zipper, laces too. My sneaks cost $140, flip flops, slippers, etc run about $70 unless on sale.

I got my free Zappos and an insole , tried first night and they killed me, lol.
I strongly suggest anyone with knee pain to check out vionics. I wear these to work:

https://www.qvc.com/Vionic-Nubuck-Side-Zip-High-Top-Sneakers---Shawna.product.A368548.html?sc=PRODFEED
[his7l2s] (score 2, diepte 0) I use “easyfeet” shoe insoles and no longer have foot pain.
[his8l0y] (score 2, diepte 0) I am a big girl too. Some people use insoles but wide size shoes worked for me. I always feel bad when I see my fellow ladies in pain. Have a nice day.
[hiscib8] (score 2, diepte 0) Get FITTED for shoes so you know you have the exact size you need. Then get dr scholl's insoles they help a lot. The most important thing you can do is change your socks on your lunch break. 

Only other thing you can do is apply powder to your feet if your prone to athletes foot.
[hism6bs] (score 2, diepte 0) Wear boots, or at the very least get some good insoles. I'm hovering around 350 myself and I do Amnesty, by the end of my work week my feet are killing me so I know the pain. I nabbed myself some really nice Rebook boots with insoles with that Zappos credit and it definitely made a positive difference. That whole Zappos thing is definitely one of the few net positives of working for these clowns.
[hismh3s] (score 2, diepte 0) I was at 230 before I started . Now I'm at 205. The conditioning will help (2 to 3 weeks). 

Invest in running shoes (ASICS or New Balance.) And gel inserts if it's too bad. When you start to lose weight (garunteed) it will get better.
(35 reacties met lagere score weggelaten)

=== THREAD 1hp61xv ===
SUBREDDIT: r/AmazonFC
DATUM: 2024-12-29  SCORE: 0  REACTIES: 101
TITEL: Forcing us to wear uncomfortable shoes will force my worker’s compensation claim….ive worked here 6 years tried every shoe and they all hurt.  
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[m4f1nap] (score 23, diepte 0) You're just now having it become mandatory?
[m4f3hit] (score 20, diepte 2) No one's forcing you to work at Amazon, or in a job position that requires composite toe shoes. Go work elsewhere if it's such a big deal
[m4f5rao] (score 16, diepte 0) You are not getting workers comp 😂
[m4f2ivy] (score 15, diepte 0) Sounds like you're measuring your feet wrong and are buying the wrong size.

You also need to find out your arch type and buy the right insole vs some generic insole.

Wide toed shoes may help too once you find your right size.

Get a brannock device and follow their instructions on the website
[m4f8d2k] (score 11, diepte 3) ![gif](giphy|xTiTnANmge5QWzfcMU|downsized)
[m4fctuj] (score 11, diepte 1) I would bet that they aren’t because every comment saying try wider shoes or slightly bigger size has no reply to it. This person just doesn’t wanna wear the safety shoes and they making a big deal about it like a child.
[m4f4l5y] (score 10, diepte 2) Get wide width safety shoes so they won’t fit so tight when you put in insoles. That’s what I do.
[m4f36uu] (score 10, diepte 0) No one's forcing you to work at Amazon. Get a job that doesn't require composite toe shoes.
[m4f7ffz] (score 10, diepte 0) This has been mandatory since about 2021? Go talk to safety about getting comfortable shoes. You usually have to go a size up.
[m4f20ks] (score 9, diepte 0) We had managers walking around stepping on AAs shoes to see if they’re safety approved. I say “had” because I reported that shit real quick lol
[m4fat3y] (score 8, diepte 0) Then go find a job that doesn't require you to wear PPE you don't want to wear. Safety shoes are provided to you free every year. Most companies don't do that. Tons of companies require safety shoes. 

Zappos offers hundreds of styles. You can also purchase your own from elsewhere. If you can't find one you are comfortable with me, that's a you problem. It's purely you being stubborn and throwing a toddler tantrum. 

It's also about the only specific dress code policy Amazon has.
[m4faa2t] (score 7, diepte 3) You actually believe that?
[m4f67yr] (score 7, diepte 2) You can get an accommodation for normal shoes.
[m4f53ws] (score 7, diepte 1) I have always bought my safety shoes a half size too big. That way when your feet swell from walking or standing, there is space for them to swell up. Never buy your regular shoe size or you will have a very hard time getting by
[m4f5ylp] (score 7, diepte 2) Lmao okay? Companies are allowed to change requirements.
[m4f8i1r] (score 7, diepte 2) It's because of insurance costs. People get the shoes or get a new job.
[m4fag79] (score 7, diepte 2) They probably paid out a lot of $$$ for injuries sustained at the warehouses, so changed policy.
[m4f4h2x] (score 7, diepte 0) Bro if you can't work in a place that requires safety shoes don't fucking work in a place that requires safety shoes. Like it's not a difficult proposition. It's a requirement you don't have to work here.
[m4f598x] (score 7, diepte 0) Every job has some form of dress code. Instead of trying to threaten them to get free money, go work somewhere else.
[m4faby8] (score 7, diepte 2) Shit company with shit metrics, but the safety shoes make sense.  Run that stow ladder into or over your foot, and it’ll be a bad day.  Drop something heavy on your foot, and workers comp + OSHA will have a field day.
[m4f66xc] (score 6, diepte 0) Imagine getting upset because a job is requiring SAFETY SHOES
[m4f8s0k] (score 6, diepte 0) Have you tried a wider size?
[m4fdbed] (score 5, diepte 2) So when someone hurts their toe from that now we can file injury claim
[m4fey1d] (score 5, diepte 5) Look at my comment history. I shit on Amazon nonstop, but the shoes are fine. I have worked here for years also, and I tried a couple of different pairs until I found one that worked for me. You are just being difficult. 3 years ago, before they added more shoes, you actually had an argument, not anymore, though.
[m4fe5cp] (score 5, diepte 2) OSHA requirement as a PPE since 2021

https://preview.redd.it/otl95fsp6v9e1.png?width=223&format=pjpg&auto=webp&s=17050fd2c57b4f561c13f7d05c22bcf15057db06
[m4f7j8f] (score 5, diepte 0) You can buy your own shoes, or wear over shoes. I went and got custom made orthotics from a pediatrist to make my boots not hurt my feet.
[m4f5axw] (score 4, diepte 2) Not sure that is legal. The use of a hammer. I wouldn’t say anything and let them hit my toes with a hammer. A lawsuit waiting to happen
[m4f7rxq] (score 4, diepte 2) Once I saw it happen, my instincts just said “NOPE.” 😂
[m4fj3h4] (score 4, diepte 2) I’ve worked here since 2019(4 FC’s), and they’ve always been required. It’s hanging on the front doors for christ sake. PPE is required in Amazon’s warehouses. 
When my facility launched this year we had to wear it all- boots, gloves, glasses, hard hats or you couldn’t enter. Period. 
I guess if you’d had followed the requirements to begin with, this wouldn’t be such a big deal. 
Amazon is even willing to give you shoes, because of the amount of what it saves on safety. Avoiding crushed broken toes and feet are a fair trade off for proper safety shoes.
[m4f69jp] (score 4, diepte 0) You do know that there is a large variety of shoes available, in wide and half sizes even. Insoles also exist and so do podiatrists. 

I went to a podiatrist and payed nothing because Amazon's insurance is so good. I didn't even need to get a referral to see them. Insoles and feet stretching exercises recommended by the doc fixed my issues.

It sounds like you just need to be more proactive about your life and body.
[m4f9pd1] (score 4, diepte 0) It’ll still be a cheaper claim than if/when you drop or drag something heavy on/over your foot.
[m4f0ykm] (score 3, diepte 0) Insoles?
[m4f6tsi] (score 3, diepte 1) No one who is neither my parent nor partner is going to get that close to me. In fact, now is a great time to catch COVID.
[m4f9vat] (score 3, diepte 2) This is the way.  1/2 to 1 full size up, and wides, if available.  Lace well and wear good cushioned socks.
[m4fkk4w] (score 3, diepte 1) Mine have been infinitely more comfortable after I got a Tread Labs insole to match my arch height and activity level
[m4fpz6u] (score 3, diepte 4) And? Tax avoidance is legal. The alternative is for Amazon to require you to buy your own PPE, just like other jobs sometimes require employees to provide their own equipment and supplies. Individuals could try to deduct those costs on their taxes but most wouldn't get a cent back since their itemized deductions wouldn't exceed the standard deduction.
[m4f3jif] (score 3, diepte 0) Have you tried these??
https://www.amazon.com/gp/aw/d/B0B4JJRT6N?ref=ppx_pt2_mob_b_prod_image
[m4f74vd] (score 3, diepte 0) Just ruptured my achilles and I'm pretty sure walking 18-25 miles a day in shit ass shoes added to it.
[m4fd8ln] (score 3, diepte 2) It's on you because you are not selecting the right size shoes, insoles, or doing feet exercises. People like you are whiney, entitled babies who think the world revolves around them. See a [podiatrist](https://www.webmd.com/diabetes/podiatrist-facts); highly unlikely, but you may have something wrong with your feet.

https://preview.redd.it/j5ccjsgu5v9e1.png?width=1080&format=pjpg&auto=webp&s=288af0214f9b0b4479e69ff654653127d9cec273

[Self Care](https://www.mumstheboss.co.uk/2023/05/06/self-care-tips-if-you-are-on-your-feet-all-day/)
[m4fevf1] (score 3, diepte 2) You don’t traverse on foot through a warehouse where there people are carrying items or moving pallets with jacks?

Also, most warehouses require a standard of footwear.  Along with construction, it’s why so many steel toe/composite toe options exist.

Amazon is an asshole of a company, but requiring safety toe shoes/boots makes sense
[m4fbewj] (score 3, diepte 0) Do what I did and get accommodations for it. 

I tried all their shoes too and even in my normal shoes they have to be fabric because my toes press against the side until there's a hole even in wides. 

I explained it to my doctor, gave the necessary paperwork and now I am able to use those plastic covers instead.
[m4ferrs] (score 3, diepte 0) Horseshit. I have two pairs of Amazon paid for Reeboks that do not hurt my feet. It took a couple tries but exchanges were easy, the right shoe weight was a game changer. Its only been mandatory a couple years so you're full of shit trying every shoe 😂😂. Don't be an idiot, either leave or try again, and stop whining like my cat when she's hungry.
[m4fmrnu] (score 3, diepte 0) You’ve been working for the company 6 years and didn’t do career choice so you can leave for good?

Stfu and get back to work.
[m4f9yj0] (score 2, diepte 2) Did you remove the standard insole before putting in the ordered insole?
[m4ffabp] (score 2, diepte 2) Select Insoles and wider shoe size to begin with ...

https://preview.redd.it/57y7052t7v9e1.jpeg?width=1295&format=pjpg&auto=webp&s=833f9102ab9c40436933f9c77c60a161d189adeb
[m4fd07z] (score 2, diepte 4) Believe what?
[m4fhx7h] (score 2, diepte 5) Someone hitting your toes with a hammer, what else
[m4fj23n] (score 2, diepte 6) It’s Amazon I wouldn’t put it past them.
[m4fk7k3] (score 2, diepte 3) Also striking composite toes with a hammer can weaken them potentially making them less effective when they are actually needed
[m4f32su] (score 2, diepte 0) Get mesh flex steel toe shoes
[m4fp0k0] (score 2, diepte 4) What's wrong with a company trying to cover their asses in a lawsuit? If you were running a business wouldn't it make sense to protect it financially?

Amazon has twice as many AAs in it's FCs as pre-Covid. Many are dumb. Many are glued to their phones. Other than worker's comp, should Amazon be liable if someone picking one handed because they're holding their phone drops a heavy item on their foot? Or someone somehow runs a loaded pallet jack over their own foot (yes, both have happened at my building)? There's nothing wrong with protecting people from themselves and others.

It doesn't matter if "they can afford it". No business is going to make a practice of rewarding people for their own stupidity or hiring lawyers and making payouts for situations where it's cheaper to try to lower incidence rate.
[m4flekp] (score 2, diepte 3) The FCs have required it since 2019

SC since 2021

SSD since 2022

Not sure about DS or fresh 

But yeah they've been around for a while
[m4fm9z9] (score 2, diepte 4) Even the locker I worked at 2yrs ago made them mandatory. And Whole Foods, when we were Amazon online shoppers, made us order Shoes for Crews(slip resistant). This isn’t new by any means
[m4fnbb7] (score 2, diepte 2) That's what happens when you shouldn't be working at a warehouse. You're proving my point. Hundreds of thousands if people wear the dumbass shoes just fine. A few people are too soft to do so. Go work somewhere else.
[m4f58av] (score 2, diepte 0) Damn they’re putting those ASC members to work lol. We do nothing over here
[m4f5xb3] (score 2, diepte 0) Dude you can buy your own comfortable safety shoes. Mine that I bought last year are still in the box in my closet I used them the first week and I said I can’t do this. Went on Amazon and ordered my own
[m4fgmh2] (score 2, diepte 1) I did that too. Paid over $500 for them. they were the worst insoles I ever had.
[m4f7pfv] (score 2, diepte 0) I am literally sitting here icing my foot as I read this. $280 worth of shoes and insoles, It’s rough. Even with the composites/aluminum.
[m4ffi36] (score 2, diepte 0) I highly recommend trying [these](https://www.zappos.com/p/mens-reebok-work-fusion-flexweave-cage-composite-toe/product/9348048). 

I went through many safety shoes and these are the only ones that don’t bother me. Even recommended them to a coworker who was also complaining and he would not stop talking about how comfortable they were and how I saved him from quitting lol.
[m4fik6b] (score 2, diepte 0) Then get a job that doesn’t require composite shoes. That’s pretty standard in a lot of warehouses.
[m4fky2w] (score 2, diepte 0) 6 years and you can't find a single pair of comfortable safety shoes? I smell bullshit.
[m4fmjfl] (score 2, diepte 0) I am starting to want to join the Amazon strike
[m4ezobw] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.com/invite/t7jARCs) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[m4fhrfs] (score 1, diepte 2) I doubt that's occurring. But if it is, please report that to management.
[m4fjbt7] (score 1, diepte 2) That's assault, do not consent and make a stink. There are other ways to check for safety shoes basides stepping or hitting shoes with hammers.
[m4fsiuw] (score 1, diepte 2) Security is a contracted company. It's hard to believe Amazon would give them the responsibility for checking safety shoes. If they slack off, misidentify or skip over unallowed shoes and someone gets hurt, Amazon would be liable. I've also never seen a hammer in the hands of anyone except Facilities and RME.
[m4gfwgw] (score 1, diepte 2) That's not happening. Security has no role in ensuring people are wearing safety shoes. 

Operations, safety and PXT are the ones checking at the entrances.
[m4f2f12] (score 1, diepte 1 OP) The managers here are wearing black Air Force’s and Vans in our facility!
[m4f2lk9] (score 1, diepte 2) That is……wild. 🤔
[m4fhnrm] (score 1, diepte 2) Managers are held to the same standard.
[m68crav] (score 1, diepte 2) They hurt for a few days until your feet get back into the right shape. Then they're the best insoles
[m4fc2kc] (score 1, diepte 0) My toe nails literally fell off  from those so called safety shoes  😂
[m4fckfd] (score 1, diepte 0) There’s tons of different shoes just try to find one that fits better for you, I suggest to wear them a little bit once you get it to wear them
[m4frcmk] (score 1, diepte 1) I agree about the wright. After I sorted for the shoes that fit me and stykes I'd want to wear I narrowed down by which one's were lightest. That doesn't mean they'll be comfortable (one year I did two exchanges before getting a comfortable pair) but lighter is better if walking around a lot.
[m4ffodh] (score 1, diepte 0) It's on you because you are not selecting the right size shoes, insoles, or doing feet exercises. People like you are **whiney, entitled babies** who think the world revolves around them. See a [podiatrist](https://www.webmd.com/diabetes/podiatrist-facts); highly unlikely, but you may have something wrong with your feet.

https://preview.redd.it/ffchhap68v9e1.jpeg?width=1295&format=pjpg&auto=webp&s=566156e99a98172aee9b95c8d72c5f0efb9bf4ec

[Self Care](https://www.mumstheboss.co.uk/2023/05/06/self-care-tips-if-you-are-on-your-feet-all-day/)
[m4ffzcz] (score 1, diepte 0) be lucky i have to wear metatarsal shoes. i wish we could wear our composite toes again
[m4fi6ig] (score 1, diepte 0) Then get your own safety shoes or get a different job.
[m4fjdjp] (score 1, diepte 1 OP) #pedo
[m4frpin] (score 1, diepte 1) A union isn't going to be able to negotiate for the right to not wear safety shoes in a warehouse, just so you know.
[m4geqje] (score 1, diepte 1) The union isn't going to get rid of safety shoes. In fact, they are very pro safety shoes. 

https://teamster.org/personal-protective-equipment/
(17 reacties met lagere score weggelaten)

=== THREAD 16nyj3d ===
SUBREDDIT: r/Construction
DATUM: 2023-09-20  SCORE: 1921  REACTIES: 97
TITEL: Always mind your feet
POST (source_id=post):
He ended up being returned to earth safely.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k1hksx8] (score 271, diepte 0) rip this dudes knee pieces
[k1i5ate] (score 171, diepte 0) That happened in our area once to a kid working on banners. The boy was standing on the banner when the plane snatched it up. Took the kid up a hundred feet then he came loose. He didn't  make it.
[k1hf7tb] (score 139, diepte 0) Jesus.  That's the second one of these in not too long.  Watch your feet is right.
[k1hpuvt] (score 87, diepte 1) Ankle, Hip, spine RIP
[k1io48u] (score 69, diepte 1) I hate to say this. But uuhhh happy cake day?
[k1k0ulp] (score 66, diepte 4) Flipped upside down and I flew away screaming
[k1htgw3] (score 66, diepte 0) OMG, I thought the guy on the step ladder was going to get brained.  You need to be ready to move out of the fucking way, not fixed on a ladder with a load like that incoming.

Then mister step on it... fuck.  Rope attached to large moving vehicles should be handled  like poisonous snakes--as little as possible.
[k1jg31d] (score 61, diepte 1) This is my last resort
[k1is9f3] (score 52, diepte 3) He said he hated to say it.
[k1ifcfz] (score 46, diepte 1) Great illustration of why you never wrap a tagline around any part of your body (intentionally or unintentionally). 

Also, wear hardhats.
[k1i7lva] (score 41, diepte 1 OP) I don’t know too many details. He did survive though.
[k1jw655] (score 38, diepte 1) Happened to a guy I knew. They didn’t reattach the tag line to the hook, so when he was flying up some wire mesh he used a piece of nylon rope. It was caught under something and when the crane picked up the load, it snapped out and wrapped around his neck and took him 30 feet in the air before the crane operator stopped because he thought something was wrong. Came loose and fell on a yodock and is paralyzed for life.
[k1jjprn] (score 31, diepte 2) Suffocation
[k1hqxds] (score 28, diepte 1) The only reason to kill the cameraman would be if he had kept filming while his buddy was being flown away by his shoelaces.
[k1jkah3] (score 27, diepte 3) No breathing
[k1i4r0z] (score 22, diepte 0) Wow. Any idea how that ended.
[k1k2pfm] (score 20, diepte 5) Du ne nu ne ne nu nu ne, du ne nu ne ne nu nu ne 🎶🎶🎶🎶
[k1id75c] (score 18, diepte 1) Yup.  Sometimes, it's the only way.  It's some damn expensive concrete.
[k1iassp] (score 17, diepte 0) WTFuck is up with the shit edit?? Is that an AI thing that thinks “good part over now”?? JFC
[k1huqzs] (score 16, diepte 1) How you see this and immediately think about a boss being a dick is wild. I’d bet there’s a 95% chance that you hate your boss and think they are all evil people.
[k1ia3j4] (score 14, diepte 2) Happy to hear that. Some jobs can kill you so quickly. He got lucky!
[k1k70jb] (score 13, diepte 2) Elevation
Start screaming 
Now I get a cheque from WSIB-hee.
[k1j6vlh] (score 13, diepte 3) lol

Cake days are far more important.
[k1izog6] (score 13, diepte 0) Come on!      
No one stops filming there.
[k1iuug4] (score 12, diepte 1) Looks pretty chiropractic to me.
[k1irhcw] (score 12, diepte 2) Yes, it's a tag line.  You can handle it, but should as little as possible and be aware of where it is at all times--as if it were a poisonous snake.  

When people do as you suggest, and handle it casually, like any other rope, that's when shit goes sideways and what might normally be a simple entangle results in a fatality or loss of hand or foot.  

Helicopter didn't loose control, the guy waived him off and he took off as signaled.
[k1jodzh] (score 11, diepte 2) Never have any kind of loop in the end either
[k1kxhsx] (score 11, diepte 6) This is my plastic fork
[k1k7xtf] (score 9, diepte 1) In a osha 30 class right now. I'm on week 6. There has been no mention of helicopters.
[k1hjmct] (score 8, diepte 0) r/killthecameraman
[k1iynjt] (score 8, diepte 0) Ouch. To be fair, I don't remember helicopters being covered in OSHA 30.
[k1khclk] (score 7, diepte 2) A few weeks back.  The guy who got caught by a tagline from a tower crane and was hoisted about 30 floors up.  I think it was in Canada.

Lemme see if I can find a link.
[k1ks2bl] (score 7, diepte 5) Nice
[k1inx08] (score 7, diepte 1) It’s a rope attached to the load aka a tag line.   Unlike what you say they are meant to be handled and guide in the load.  Caution obviously still nesscessary but in this case the helicopter lost control.
[k1hstyp] (score 6, diepte 2) Agreed.
[k1ie4so] (score 6, diepte 1) ...and u/VideosThatEndTooSoon
[k1ixw96] (score 6, diepte 3) I’m not worried about handling poisonous snakes. I’m not going to eat them. It’s the venomous ones I’m staying away from.
[k1ku5t5] (score 6, diepte 3) I was a formwork carpenter 25+ years ago and the job I was working on, a standing fixed crane dropped a full kibble of concrete on top of a couple of carpenters and steelies. 2 dead and the others critically injured. That was a bad day.
[k1mxyje] (score 6, diepte 2) Woah woah woah dude no.. give him a tug
[k1na5e8] (score 6, diepte 4) Lmao. We all know you really meant tug.
[k1mpw2q] (score 5, diepte 3) I tell the new guys, "pretend as if the guy in the crane is intentionally trying to kill you..."

Same with forklifts, loaders, dump trunks, etc. Keep one eye on them and GTFO of their way.  Especially if you're in a vehicle.  A loader will back right over your F150 if you stop in the wrong spot on certain job sites.  You are like an ant and they're giants--don't get stepped on.
[k1my03t] (score 5, diepte 3) Hug meant to say hug
[k1ijibh] (score 5, diepte 0) Alexa, play Free Bird
[k1jtv50] (score 5, diepte 0) Ended way too soon
[k1lat7u] (score 3, diepte 1) This dudes knee fucks
[k1horz0] (score 3, diepte 0) That’s one way to make it to the job site.
[k1hvxqz] (score 3, diepte 0) “Safely” meaning not dead.  I’m sure his knee/hip/ankle felt great after that!
[k1icqod] (score 3, diepte 1) If you're in the bight, it doesn't have to have a loop *tied* in it, it can make its own.
[k1kxx24] (score 3, diepte 4) Yep that's scary and sad. I've worked in a sawmill, logging and commercial fishing. Lucky to not see anything first hand but heard plenty of stories. Anything overhead, spinning, ropes, belts, big machinery and vehicles, you need to have very good situational awareness and be thinking all the time that if something goes wrong where's my escape route. Never get between things you can't stop or attach yourself to something moving. Among a million other things lol
[k1iaqe3] (score 3, diepte 0) It that like a yard a load??
[k1ienr5] (score 3, diepte 0) Oh my God is he okay? Absolutely nightmare situation.
[k1jrfhb] (score 2, diepte 1) Where's the other one?
[k1hxk0p] (score 2, diepte 3) I didn't get it until this second part. Valid.
[k1ltk39] (score 2, diepte 3) You don't love it when you're about to drift a load exactly into place and some dumb ass yanks on the tagline because he's to ignorant to understand what the big brain in the crane is doing?!?!
[k1m4zc0] (score 2, diepte 4) Hah, I'm more likely to be the guy on the tag line end, but yeah, don't try to muscle the load--that's what the crane/helo is for!  Just hold it and keep it from spinning or oscillating/swinging, and try not to do too much.

Have you ever seen a tag line in a loop like that?  I can't recall seeing such but I suppose it gives it extra weight. Seems fucking dangerous.  Better to put a bag weight on it, if needed.
[k1m63v1] (score 2, diepte 5) There should never ever be a knot in a tag line.
[k1mq04a] (score 2, diepte 2) Seen a lot of dudes get downvoted for that
[k1jr8dc] (score 2, diepte 0) On my helicopter pick they told us once I see the hand signal I’m gone idc if your hands on the unit etc. Sure enough this pilot saw the signal and just took off. Do you have the video of him being returned to sender 😆
[k1lb0so] (score 2, diepte 0) where's the rest of the video? OP, don't leave us hanging!
[k1ldo5i] (score 2, diepte 1 OP) Sorry, I’m guessing guy filming panicked when his coworker got lifted.
[k1ua3ff] (score 1, diepte 2) Cuz a hard hat sounds help how in this situation
[k22n5sn] (score 1, diepte 7) cut my check into pieces, Uncle Sam and child support
[k1iupo7] (score 1, diepte 2) I'm not sure if the helicopter lost control. I'm unsure of what's really going on, but by opening and unloading the bucket, the weight on the helicopter lowers quite quickly. It thus automatically tends to lift. 

I'm by no means a helicopter specialist, but I'd say ideally the helicopter puts the bucket on a stable structure before it's emptied, then lifts it once it's empty.

Also, the guy should not stand on a ladder for that. One could attach a second rope to the handle to open it.
[k1jwecz] (score 1, diepte 2) That’s one of my biggest pet peeves in high rise construction is watching guys stand all over those without looking at them. I try to tell them often this right here is what could happen.
[k1huxi8] (score 1, diepte 0) Well. He ded
[k1hw4em] (score 1, diepte 0) Danger Pay!
[k1hwl68] (score 1, diepte 0) Yikes. 

Did the tag line have a loop in it? What numbskull is rigging this?
[k1kzmws] (score 1, diepte 2) How?
[k1vis3y] (score 1, diepte 4) Now it's your cake day big boi
[k1lrev7] (score 1, diepte 2) Garver buckets can be the only option a lot of the time. Never used one with w helo tho.
[k1ic6os] (score 1, diepte 0) "Keep your feet out of the bight!"
[k1ig9j4] (score 1, diepte 0) Go on now get…..
[k1jma1k] (score 1, diepte 0) Seeding a pipeline RW?
[k1jna2i] (score 1, diepte 0) If the tag line had a loop in the first instance this isn't ideal. Maybe it was just the unique arrangement of the line as it made contact with the ground and his leg.

Fun times. He'll not forgot that world-view anytime soon.
[k1k430h] (score 1, diepte 0) r/Unexpected!
[k1kb44n] (score 1, diepte 0) Sometimes tag lines do more harm
[k1kw7pq] (score 1, diepte 0) The old Urban Legend of finding a scuba diver found by firefighters in the middle of a Forrest. 
Scooped up from the surface of a lake by a super scooper and dumped into a Forrest fire.
[k1kymca] (score 1, diepte 0) Quickest concrete pour. Fake
[k1odg05] (score 1, diepte 1) He opened the hopper and it poured out...hes not taking his time...
[k1l8y82] (score 1, diepte 0) I just love video shorts. Have a down vote and a block. :)
(18 reacties met lagere score weggelaten)

