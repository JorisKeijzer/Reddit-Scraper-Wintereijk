# Label-batch batch_0061

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
Schrijf het resultaat naar `batch_0061.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: y66yyf, 1owc5zu, 1o89m34).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD y66yyf ===
SUBREDDIT: r/Serverlife
DATUM: 2022-10-17  SCORE: 76  REACTIES: 96
TITEL: What can I do to stop my feet from aching while serving?
POST (source_id=post):
So I am a bartender / server. On Thursday’s I serve, Fridays and Saturdays I am bartending. This past Saturday I worked the entire day from 11:30AM to 10:30PM, and my feet were hurting so bad it shot up through my back I felt like I couldn’t walk. At my restaurant there is no back for the bartender so I have to make all the drinks for everyone including me, take all the orders, run all the drinks, & I get no help running my food so I am always running back and forth constantly. 

I tried to get insoles from Walmart but they aren’t helping. I have non slip sketchers that I usually wear but I also tried crocs and it’s the same thing… when I work 5-6 hours no pain, but 10-12 my manager says it looks like I walk with a limp. Ibuprofen nor Tylenol help either lol…

Help a sister out is there anything I can do? Any shoe recommendations? I’m only 22 and I feel like my serving years are going to be cut short bc of my feet. 

Thanks in advance!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iso6ydo] (score 78, diepte 0) Ask your manager for mats. If you’re behind the bar you should definitely already have them but they’re better on your feet than the hard ground.
[isnsubt] (score 69, diepte 0) Not even about shoes babe get yourself compression socks and feel the immediate difference.
[isofqen] (score 51, diepte 0) Honestly I started wearing doc martens while serving and it really helped. I used to have lower back pain and my feet would ache a lot, but wearing doc martens helped a lot. I also used inserts. They’re pricy but they’ve lasted me a long time
[isohbff] (score 25, diepte 1) Solid advice. They are not fun to clean after a double,  and I don't pull mine for single shifts, but they make a huge difference long term.
[isojxqv] (score 19, diepte 1) came to comment this exactly. changed my life and i was able to get around quicker because my shoes felt like a part of my body. go for the non slips if u get them! first week or so sucks but after that they fit like a glove. they are $$ but it’s worth it to be comfortable and be pain free
[isnv8pn] (score 17, diepte 1) Compression socks for the win!!!!! Also sometimes when I get home, I put a heating pad on my lower back (like you would with period cramps)… it might not work for everyone and I know it’s not your feet, but it helps my whole body feel a little bit better somehow. I have no scientific explanation or anything but somehow it helps the strain on my feet too. But yes, compression socks! I wear the knee high ones
[isob5d6] (score 17, diepte 3) you didnt have to make this weird...
[isomifa] (score 17, diepte 0) get orthotic insoles. i went to a podiatrist who told me that the insoles you buy from the store are basically garbage. i bought powerstep insoles from the doctor, about $60, you can buy them on amazon too. work wonders. also stretching your feet before your shift helps.
[isoudeh] (score 14, diepte 1) Same, I wear non-slip, steel toe Doc shoes at work. They look cute, are easy to clean, and you can drop a keg on them on not feel a thing. It took a few tough days to break them in but they are easily the comfiest work shoe I’ve ever owned
[isok2nm] (score 12, diepte 2) Yes!!! And if you can, get the children’s size. That saved me a lot of money and the quality is just as good.
[isodu0p] (score 11, diepte 0) I've leaned that switching shoes halfway through the day sometimes helps. I'll even go back and forth a few times. I also got these arch support bands that helped.
[ispbgka] (score 10, diepte 1) That helps but in this industry it is good policy to count on your feet hurting.
[isoulwf] (score 9, diepte 2) Yup, I got the oxford style in a children size and they are about $55 if I remember correctly. They haven’t been worn out hardly at all even after two years of serving in them
[ispjtno] (score 9, diepte 1) Same! I wear the original Doc Martens and I placed a set of $50 super feet insoles into them and I literally cannot express enough the difference when wearing them all day (double shifts) vs other footwear makes while I am bartending.  We do not have mats behind our bar (it’s too narrow and oddly shaped For mats)
[isp9pur] (score 9, diepte 0) HOKA brand work shoes.  This is your answer.
[isnx3rl] (score 8, diepte 1 OP) So I’m 5’5 and I weigh about 195 according to google I should be like 150. I have a muscular build though so I don’t look overweight but I do know I want to lose a few pounds for sure. Could that have something to do with it?
[iso1wfn] (score 8, diepte 2) I’m 5’5 and 157 F and my feet hurt as well lol. so idk if it’s exactly weight? I have very skinny coworkers who also have their feet hurt. Could be issues with your own foot and stuff like the arch and stuff. I use dr. scholls inserts as well and my feet do tend to hurt at the end of my shift. I read online elevating them can help. If it’s noticeable you should probably see a doctor, and of course trying lose weight only if you want to.
[iso8gz4] (score 8, diepte 1) I'm 5'2" and 108lbs and my feet hurt like ass.
[isp3vt1] (score 8, diepte 0) I do stretches before a shift and after.

Makes a world of difference.
[isnws9b] (score 7, diepte 0) > I’m only 22 and I feel like my serving years are going to be cut short bc of my feet.

I mean this in no disrespectful way... But there's not any other way to ask. 

What is a range on your weight?

I'm 37, wear Sketchers, walk 20k steps per day (my goal) and have been in the industry since 18 years old, and I have no problems with shoes being the issue.  My knees fucking hurt every night and my back does as well.  But never been called out by a manager for it.

Also, and I don't know how to spell it, scyaitc pain? [it feels like this](https://www.ansellchiropractic.com.au/wp-content/uploads/2016/09/disc-nerve-pain-256x300.jpg) my brother has it, luckily, I don't.
[iso193t] (score 6, diepte 0) I don't know which Sketchers you have but these I highly recommend:
https://www.skechers.com/work-relaxed-fit-max-cushioning-elite-sr/108016.html
[ispkoi9] (score 5, diepte 2) They have work ones that are non slip
[ispw0uv] (score 5, diepte 1) I use them too!!!! I got them 1 size bigger for my socks, as here it's COLD AS HELL, and it helped me a lot. No pain, no slip, faster serving and happier meître. Had to save like a racoon before winter, ngl, but i've been going 3 years without needing any new shoes, so i saved triple the amount.
[isp5rqa] (score 5, diepte 0) Compression socks and birkenstocks
[ispljrr] (score 4, diepte 2) And your legs. Idk I'm used to it now, in that I can go all day mostly walking and not really feel it that much until Friday.
[isov838] (score 4, diepte 0) Compression socks and work crocs! They are so ugly but so comfortable and I immediately noticed a difference. I usually work 11-13 hr shifts and aside from the blisters I initially got from them, my feet rarely hurt during or after work.
[isp8qs7] (score 4, diepte 0) Darn tough socks and hoka brand slip resistant shoes for work. They are expensive but worth it
[isq8f53] (score 4, diepte 1) This is ABSOLUTELY the answer!! 
HOKA Bondi SR are the perfect solution.
[ispulju] (score 4, diepte 0) Switch shoes every 6 hours or so. It’s not a cure but it will help.
[isr4i44] (score 3, diepte 2) I'm going to point you to my comment directly to OP. I'm on mobile and have no idea how to link a comment though so looking at my comment history would be easiest.

 IDK your age or anything, but if heat in your lower back is helping with foot and leg pain it sounds more like it's a back issue to me. I would have argued against me a few years ago but got sent to PT last year for sciatica and found out how much stretching and strengthening exercises for your core and especially back can help with leg and foot pain. Proper arch support is important as well, of course.
[iso5q9y] (score 3, diepte 0) Birkenstocks.  With the cork bottoms that conform to your feet.
[iso5rw8] (score 3, diepte 0) Compression socks changed my life. 
Edit: I had to leave serving bc of my back. Im 41 tho: so you have a few more years. Get those compression socks!!!
[ispnbis] (score 3, diepte 3) It's always my lower back that's the worst at the end of an extra-long shift. I had a bunch of spinal taps as a kid and there is scar tissue.
[isodv4k] (score 3, diepte 0) I've leaned that switching shoes halfway through the day sometimes helps. I'll even go back and forth a few times. I also got these arch support bands that helped.
[isp4ojz] (score 3, diepte 1) Are doc martens non slips? And the children sizes are non slips too?
[isp4yfo] (score 3, diepte 2) I’m not sure, to be honest I didn’t know that they had specifically non slip shoes until now. I know that all doc martens have a lot of traction. I’ve used the children’s size ones for two years and they work better than the non slip shoes I had before
[ispvwgo] (score 3, diepte 1) I'll second this. They have a canvas version that breathes as well with roughly the same support. It's what I've Ben rocking for years.
[isr6l45] (score 3, diepte 1) I’m a doc marten person too! I have short wide feet and danskos were too narrrow and I would always roll my ankles. I’ve been wearing docs for 10 years serving now… had to switch out a few pairs because the soles were worn down and no longer non slip. I always order straight from the doc marten website but they just don’t last like they used to. Either way I can get a few years out of “work” docs and then retire them into everyday docs.

Docs are great but fair warning… breaking in docs sucks wear them for at least a week before you work a full shift in them!
[isoijp6] (score 3, diepte 0) Orthotics if your insurance plan covers them
[isp0pdq] (score 3, diepte 0) Compression socks that go up past your ankles! I use a compression ankle brace and inserts myself under a pair of tall boots (doctor martens). after work i try to treat my feet extra nice.
[ispag60] (score 3, diepte 0) So I've served for many, many, years, and I've always made sure my feet are the #1 importance.  Shoes make the difference, and I honestly love Ecco's, for women and men, and yes keep a couple or a few pairs on you.  I have 3 pairs at my full time job and 2 pairs of inserts and switch them all out sporadically.  Then comfy tennis shoes or crocs for walking there and back.  Also footbaths at night with Epson salts and etc.. are incredible.  You can find cheap ones on Amazon for $40 or so.  Good luck, don't work too hard!
[ispddca] (score 3, diepte 0) Hoka
[ispnkc5] (score 3, diepte 0) Good shoes are a plus, but I also found out the way you walk is just as important, after a leg injury a physical therapist that was rehabbing me, had me walk on a treadmill and absolutely showed me how my walking was wrong, after he got me to start walking correctly for the first month or so I had to actually remind myself to keep my feet straight and walk “with a purpose” not stroll or shuffle, picking up my feet and heal to toe, allowing my ankles to actually pivot fully which helps pump the blood through the feet and up the leg, after about 3 months muscle memory made it almost hard to walk wrong again, this didn’t just help my feet but it helped my knees, hips and back, sure after a long day I’ll be a bit sore, but definitely not needing pain meds like I used to, learning to change how you walk is definitely hard but long term it may save your joints, where as medication will get you by but it’ll mask the pain which is telling you you’re damaging stuff
[ispo7yw] (score 3, diepte 0) **Red vine leaf extract.**

It takes at least 6 - 8 weeks to kick in, but I've been taking it daily for 3 years and I went from chronic pain and swelling to having brand new feet, legs (and as a result, no more lower back pain). 

2 pills a day for 8 weeks, then dropped down to 1 (but you can stay at 2 pills if needed).
[ispogi1] (score 3, diepte 0) Superfeet insoles, blue or green helped out tremendously with my  Sketchers. Feet still throb but nowhere near as bad as before.
[isr7g6g] (score 2, diepte 4) Hips for me. I snap crackle and pop after a long shift.
[isq7lu2] (score 2, diepte 2) I would agree with this if you’re talking about platform boots, but I got oxfords and they don’t add any extra weight at all.
[isor7wr] (score 2, diepte 0) Plenty of good advice already posted, mine is that ya just get used to it over time. Before I started serving I was a grocery store supervisor for three years, so I was on my feet and walking/running 40 hours a week.
[isp2mkv] (score 2, diepte 0) Snibbs. They are expensive and sorta ugly, but worth it. They don't help much anymore bc now I work at a place that I have to climb up and down sets of 13 stairs, and nothing helps my poor feet after 8 hours of that.
[isp5pwo] (score 2, diepte 0) Some solid advice here. I would get your feet tested at a shop that does orthotics. You might be paying $100-$200 for a pair of shoes, but they'll make a huge difference.
[isrzvqo] (score 2, diepte 1) Game changers.  I work on what is essentially a concrete floor and could barely walk by the end of service.  Switched to hokas and it’s night and day difference.  Best investment.
[issrx0g] (score 2, diepte 1) Thirding this. However hoka people - my shoes come untied constantly!! I’ve tried the runners knot. What gives?
[isphapw] (score 2, diepte 0) Blundstones have been a godsend for me. No pain even on long shifts. I switch out my insoles every few months, I just get blundstone ones.
[ispk8fg] (score 2, diepte 0) So I have an old pair of Doc Marten’s (seriously, I swear by them) and I want to buy some insoles for them but currently I wear a pair of compression stockings (knee-high, you can find them on Amazon pretty cheap, just get the light compression, probably better for you than the super tight ones at this level) and then a second pair of ankle high socks for cushioning. I have weak ankles that tend to roll and the docs help a lot with that. I still get a lot of knee pain though.

First thing first, get a good pair of shoes. Check if your company offers shoes for crews, they’ll order the shoes for you and take the cost out of your next 3 paychecks, no interest. Don’t settle for a cheaper pair, I remember buying a pair of sneakers at the same time as a coworker. Mine were $50, hers were $200, mine wore out after a couple of months and so I bought the $200 pair and they lasted me a couple of years. Docs are about the same price but the 3 paycheck split is really helpful.

Compression socks are great, like I said, pretty cheap on Amazon.

Then get yourself a really good set of insoles. I haven’t done enough research yet to recommend a specific brand but I know insoles are important af. 

Also look up a few stretches to do before and maybe during your shift, the ones for sciatic pain are really good for back/hip/leg pain.

During your shift, also pay attention to make sure you’re not locking one or both knees or leaning too much on one side or something. 

Also, I carry edibles with 5mg thc content (if you’d prefer, cbd doesn’t get you buzzed or high but tbf 5mg thc isn’t enough to impare me) and they help with pain and the occasional nausea/heartburn.

Best of luck, I know it’s hard to be young and be hurting. Not only is it scary af (how are we gonna feel at 40 or 50??!) But people also don’t take you or your pain seriously. Hang in there!
[ispqgwe] (score 2, diepte 0) Sensitive question, but, how is your weight?  When I was overweight, if I spent the whole day on my feet, they would be killing me.  I lost quite a lot of weight, and now I can walk or stand for ages, and while my feet certainly don't feel great, they also don't hurt.
[ispv0jx] (score 2, diepte 0) I am so glad you're listening to your body early on!! Please do mind your feets, young service folk! Learn from my mistakes -- I wound up with bad arthritis and a bone spur in my big toe (meaning I can't wear most shoes anymore) from wearing the wrong shoes for so many years.

You definitely need mats behind the bar if you don't have them already. That will help at least partly. 

Second, make sure you don't skimp on shoes. It's tempting to buy the cheap shoes, but go to a specialist shoe store if you're able -- we have one here for runners, nurses/doctors, service folk, and everyone who needs extra cushioning or support. They take extra time to measure your feet, to listen to your situation and any foot issues, and then they offer you several pairs that are the best fit for your needs. 

Long service shifts are brutal, no doubt. Because you're so young, it's a bit surprising that you're having such intense pain now, which makes me wonder if you have or are developing an underlying physical issue in your feet/legs/back. It's totally okay, also, that you may simply not be built to work such a long shift; I have definitely done my share of doubles and BDs, but in the later part of my career, I had to set a boundary of no doubles unless it was an emergency or something because I just didn't have the stamina anymore. And it was harder on me physically than I'm willing to sacrifice for a restaurant job, if that makes sense.
[ispvlwk] (score 2, diepte 0 OP) Thank you so much everyone!! Such great advice I feel so much better!!
[itk0754] (score 2, diepte 1) Sounds like something I could use
[isqoa7v] (score 2, diepte 0) I’ve had similar problems. I use to have two different pairs of sneakers. Different styles and when I alternated them every other day it wasn’t as bad. 

I have bought a pair nonslip Birkenstocks. A little pricey but **100%** the best work shoes
I’ve ever had. This past week I worked 14 hours Thursday, 14 hours Friday, and then 11 hours on Saturday. Friday night my feet were a little sore but I wasn’t limping or anything. I got home and put them up for like 20 mins and was fine.
[isqup19] (score 2, diepte 0) I will tell anyone who listens to buy two pairs of the new balance non-slips shoes from the shoes for crews website and alternate between them. I don't serve anymore but I still own a pair - they're quite nice
[isqxbrk] (score 2, diepte 0) You need to invest in expensive shoes I learned my lesson cheap shoes won’t cut it. Try some Brooks or Asics
[isqyyey] (score 2, diepte 0) cbd
[isr231y] (score 2, diepte 0) Blundstones are amazing. Look for new or slightly used ones on Poshmark if you don’t want to pay full price. They’re pull ons so tight for a couple days but then sooo comfy and light and they last forever! I also just started wearing knee high compression socks to every shift AND doing a 20-30 min foot bath with massagers and apple cider vinegar after most shifts. Sooo helpful and my bartender feet don’t smell either bahaha
[isr8hdx] (score 2, diepte 0) I was gifted a foot massage machine for my birthday and it’s a game changer. Compressed my feet, kneeds the bottom, it’s heated. Pure bliss. Coming home after a long shift, lighting a joint throwing on some tv and sticking my feet in that bad boy is absolutely chefs kiss
[isreetx] (score 2, diepte 0) Lots of good advice here. You should also see a doctor to make sure everything is OK. 

If there aren’t mats behind the bar, that’s the biggest thing along with QUALITY work shoes.
[isrgvgp] (score 2, diepte 0) Spend the money on good shoes. I know it sucks, but they feel better and they last longer. Skechers have a good variety for nonslip shoes
[isrmmi8] (score 2, diepte 0) Not even being sarcastic. Get a different job.
[isrq9ho] (score 2, diepte 0) Better shoes and compression socks
[isrdbzg] (score 1, diepte 1) Came here to say this too!
[ispsgnq] (score 1, diepte 1) Buy Docs because you like them and they’re awesome, not to serve in.

You will feel the extra weight with every step.
(25 reacties met lagere score weggelaten)

=== THREAD 1owc5zu ===
SUBREDDIT: r/Target
DATUM: 2025-11-13  SCORE: 250  REACTIES: 96
TITEL: Reaction to the rumored “10-4” policy (employees must greet customers within 10 feet)
POST (source_id=post):
I get that this 10-4 thing might be about stopping shoplifters, but it’s a weird vibe as a shopper too. I normally get a seasonal job at Target but not sure now?

You can tell when someone’s being made to interact. It feels forced, and no one likes feeling like part of a script.

Let your employees breathe. Most of us just want to grab what we need and go. If I need help, I’ll ask. Promise.

Source: [https://www.hissingkitty.com/complaints-department/target](https://www.hissingkitty.com/complaints-department/target)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nop10cw] (score 89, diepte 0) Greeting/acknowledging guests on the sales floor is always something you were supposed to do.
[nopmmve] (score 89, diepte 0) It’s sort of annoying that the Target overlords think we can’t decide for ourselves which guests want interaction. there are clearly guests who do not want to be bothered. Idk if it’s just the store or part of the policy but I saw a post where it said to wave at guests. I will not be doing that. If a store employee waves at me I’m going to think they have something to tell me aside from just “how’s it going? Can I help you with anything?”
[nop47up] (score 43, diepte 0) It’s not rumored, it’s in motion. But personally I think it’s blowing up to be bigger than it actually is. We’re always supposed to greet guests and be friendly, that’s been a Target thing.
[nop37bu] (score 37, diepte 1) Thank you! I've been screaming this all week. People have the memory of gold fish tho and can't seem to recall life before COVID.
[nopmt4n] (score 34, diepte 0) They told us it was because Red Lobster started it and saw an increase in sales and reviews. 

I asked that ETL if we were a restaurant about to go under. ​
[noqh4yl] (score 26, diepte 1) I actively avoid stores who force their employees to bother customers.
[noq7jt1] (score 22, diepte 2) Life before COVID, targets metrics were weren’t so cut throat that there was a razor thin margin. Talking to 2 maybe 3 guests can easily cause a fulfillment team member to miss an Order Pick up goal. It’s not an issue of DOING IT, it’s the issue that it’s another task on top of the already strict and nearly unattainable goals.
[nopr9ta] (score 22, diepte 0) My gripe with it is that it’s an unmeasurable metric. They aren’t gonna know if I talked to everyone so I just don’t understand it. They remind us to stand at the ends of our lanes each Christmas too. So I feel like they didn’t need a rule just a “hey guys remember to be friendly.” Would have surfaced
[nopa7gy] (score 21, diepte 1) This is blowing up like it is because as the rule reads, it's completely impractical and essentially non-enforceable without getting very, very weird about it.  

  My TL mentioned this rule to me by name today for the first time while I was there on my day off after having already worked 7 days in a row, while we were busting our asses to finish pushing on their incredibly unrealistic schedule, and I laughed in his face, and he laughed back!  

  Everyone knows how fucking ridiculous it is. If I followed every TL, ETL, and our SD around on any random given day, they wouldn't be following this rule even half of the God damned time. Idk if your store just isn't as busy as ours or what, but no one who is there to push can afford to be interacting with literally every customer that comes within a few foot radius of us, **and everyone knows that because fucking no one including those in charge are actually doing it**.
[nopqn03] (score 21, diepte 2) Had to explain to the ETL the difference between a sit-down traditional restaurant and a department store like Target.
[nop82ng] (score 15, diepte 0) This is such a non- issue that people are freaking out about. 
It's our job to engage with Guests, to help them, and be friendly. 
Now that is a policy, it's a coachable conversation. That's pretty much the only difference.

I always say hi, or good morning, to the Guests. I smile when I can.
I encourage my FF to be helpful and greet. Most of them already do.

I have no idea why this is blowing up like it is.
[nopqeo2] (score 14, diepte 1) Yeah the new, young, hotshot CEO of red lobster spoke in Minnesota a few months ago and target loved it
[nopie7p] (score 13, diepte 2) There was life before COVID?
[nopujvg] (score 13, diepte 0) I was at my local target at 7:30 am and no less than 6 employees said good morning to me even though I purposely did not make eye contact. It was nice the first couple times but it became a bit annoying.
[nop7ady] (score 11, diepte 1) It's actually better than when they ruled that we had to not just smile but ask every guest 'Can I help you find something?' every time they came close..guests would be asked over and over and it became annoying
[noq7v6k] (score 11, diepte 1) For some reason too, waving feels like you know the other person. That was what I liked about GUEST was that it was more subjective if someone obviously didn’t want to chat and shop at the same time. 10-4 just reads like corporate bullshit
[noq2v3q] (score 11, diepte 0) Couldn't have said it better myself. 

Everywhere I go as a customer, I know why I'm there, I know what I'm doing, I usually know approximately where I'm going, and I know I can ask an employee for help if I need it.

I do not need my hand held, nor do I need to be patronized by everyone working there. This is a business transaction, not a positivity service.
[nopuj9d] (score 9, diepte 0) Nobody is enforcing this.  For them to do so they’d have to be out of the offices and on the floor.
[not60md] (score 8, diepte 2) I’ve worked retail on-and-off for 13 years, and I am still to this day the type of customer who will literally turn around and walk out of a store if the floor employees don’t leave me alone. Then refuse to shop there again. 

Businesses REALLY need to get the picture the most customers *don’t* want to be spoken to.
[noq0edv] (score 8, diepte 0) I feel like this would be something Europeans would make fun of Americans for, like the policy. I don’t like it because, as a policy, it’s very much up for leader discretion. Like, they can use it to justify getting rid of TMs they just don’t like. It’s also just arbitrary shit to push it as a quantitative sort of measure for friendliness when targets issue right now doesn’t begin with TMs not saying hello to *every* guest.
[norj0y3] (score 8, diepte 0) The biggest problem with mandatory smiling is corporate failed to consider why engagement is low. They didn't once ask TMs why they aren't smiling or greeting because it would lead to corporate being told that skeleton crews and too much workload doesn't make a positive environment. 

Funny how those paid most at the top are too far distant from those paid least at the bottom don't understand this.

In another Reddit post some creepy guys are using 10-4 as an excuse to flirt/harass female TMs. It's interesting that Target has training for guest interactions so you don't escalate a situation where the guest is rash, active shooter training, and even training that reshapes the term 'soft skills' to be about following management without question, but no training for if a guest is harassing a TM.
[noquckp] (score 7, diepte 0) I tend to agree, i actively avoid stores where the employees are *too* friendly
[noqznrc] (score 7, diepte 0) A hello never stopped shoplifters at my store. 🙄
[noq5ym0] (score 6, diepte 0) This has nothing to do with shoplifting and everything to do with too many customer reviews saying team members “didn’t acknowledge them” or “weren’t friendly” enough. And it goes along with why they call customers “guests” because they are a guest in our “home” or something along those lines. But I’ve seen a lot of customers get very uncomfortable or flat out ignore you when trying to greet them.
[norg6k2] (score 6, diepte 0) Someone should make a stealth game of working at target while actively avoiding customers from getting within 10ft of you
[noqk6m2] (score 5, diepte 3) Those in charge aren't doing it **to literally every single customer that comes within a few foot radius of them, every single time, 8 hours a day, 40 hours a week, every week of the year**. I'm not saying you've never seen a single person in charge ever talk to a customer. Try actually responding to the point being made.
[nou3oq7] (score 5, diepte 3) I remember the mall where I grew up had this store called Buckle that I went into once and never again because the girl literally would not leave me alone after I told her several times I was just looking. She kept grabbing random things and bringing them to me like "I think this would go great with your style!" Like, omg go away!
[normp54] (score 5, diepte 2) Just protest the policy or maliciously be compliant, seek out every guest just to greet them regardless of how much work you get done
[normapy] (score 5, diepte 1) This is why we Americans are seen as weird by Europeans.
[norkmr7] (score 5, diepte 1) Correct, which is why we don't need to be mandated to smile. 

Did you not consider that metrics, workload, and skeleton crews may be the reason why TMs are focused less on smiling and more on getting the work done?
[nov1tf9] (score 5, diepte 1) When I hear guests complaining while im doing fufillment, it's never about "nobody smiled at me or acknowledged me" it's always about "I've been waiting 20 minutes for someone to come back to unlock this item" or "I walked across half the store and you are the first person I've seen who works here, can you help me"
[nort521] (score 5, diepte 0) New policy’s like this are why Target is going to continue to go downhill. We’re running on Skelton crews, freight is constantly rolling to the next day bc flex needs backup (freight rolling is not great ever but especially in a store that takes 7-10 trucks a week). Flex has to inf items bc the they want the POT prioritized rather than inf it seems. Personally, I think it makes sense to actually find the item and the order goes slightly late, bc at least the guest is getting their order. I’d imagine it’s more frustrating to see your cold medicine or other otc items were cancelled bc the tm had to rush  the cart to finish before it went late, bc the item is in the back, but it’s not pushed, making it take longer to have to go check the line/repacks to try and find it. TMs are more inclined to inf it bc at least they made the pick time (and lately it seems like they’re still going late no matter how much backup is used. 

Having to acknowledge and greet guests while trying to do this only takes a few seconds, but when you’re expected to do it constantly, that’s a lot of wasted time on your carts. When I have to jump into opu because they need backup, I’m getting stopped pretty frequently when I’m rushing around trying to finish the cart on time because there’s no TMs actually on the sales floor bc they’re all picking carts💀.
[nou4g8q] (score 4, diepte 3) This! For many of us, it's not the expectation of helping guests in and of itself.
[nosqf0w] (score 4, diepte 2) Oooooo.  Covid!!  Sounds like an opportunity for malicious compliance.  Every team member puts the mask back on.  It was so nice not being forced to smile all day long because of the mask.  Seriously.  8 hours smiling and chatting with guests on a lane hurts my face.
[noq2n29] (score 4, diepte 1) ![gif](giphy|mEsqfG9Zbuj7CDsroa|downsized)
[nork9jt] (score 4, diepte 1) Are you saying autistic people shouldn't be hired at Target if that can't follow this policy? 

If corporate has to mandate smiles they may be failing to acknowledge why TMs aren't smiling in the first place.
[nornu0l] (score 4, diepte 3) I explained to a guest I have 30 things to do right so the CEO who does his one thing poorly can be paid better than me at my expense.
[nosg70k] (score 4, diepte 0) Look, Target is desperate at this point.

They decided that politics were too hot for them to try anything anymore and to deal with corporate screw ups, they decided to take it out on the team members with hour cuts the last few years.

This has led to catastrophic customer service and shabby looking stores. So they decided rather than fixing it with more hours, to get an easy publicity win to save the brand by making sure people get help when they are in the store.

They used to do this in the 2010's only it was within 6 feet.  I remember this because it cost me a raise. They just don't realize they don't have the same team member trust they once had to make this work.
[not24mk] (score 3, diepte 1) Yes.  And it may be that everyone defending this intends on ignoring the written policy and following the previous GUEST policy.

Do you remember any news stories or complaints online about GUEST?  I don't.  Because it was normal and natural customer service.  Why did they change from that?  They made a change, and made a big announcement for a reason

What is the actual written policy for 10/4?
[nop72sr] (score 3, diepte 0) lol, still 5 stars.
[noqnx33] (score 3, diepte 5) Are you following these people around their entire shifts? Like literally wtf are you even talking about? You literally can't know how they behave outside of the incredibly specific circumstance if you watching them.   

  And personally, I've definitely seen all 3 SDs at the locations I've worked at not only walk by a guest without acknowledging them, but I have seen all of them **actively avoid interacting with a guest**. Not because they're shitty employees, but because they were *on their way to do something else*. Because we're working while we're at work. We don't exist like NPCs solely for talking to the guests. You being in denial of how absurd this is almost makes it feel like you don't work the floor ever.  

  Like literally imagine working a timed OPU already nearing the red when you hopped into it, and then having to talk to *literally dozens upon dozens of people, because working fulfillment you are running all over the store as fast as possible while there are customers everywhere*. Like if you tell me that in that situation, you would talk to literally every last customer you come near, I flat out just won't believe you. This isn't how any employee at any Target or any other store I've ever worked at for that matter behaves in real life on the ground, unless they think they're being watched closely, which is never going to be for long anyway.
[nopycss] (score 3, diepte 1) at least from what i've seen the direction has been not to coach tms yet on this, and to just lead by example and recognize those that are doing it. That'll probably change if they stick with the initiative but like this is an "airpods" rule that will have wildly different interpretations and enforcement depending on store
[noqnp3z] (score 3, diepte 3) This made me LOL
[normu66] (score 3, diepte 1) Big brother is watching
[nor0mod] (score 3, diepte 1) THIS. My front end TL and I were discussing just this today and how 10-4 would become grating real fast.
[normgss] (score 3, diepte 1) Tbh it’s only a matter of time until “team member” just becomes “butler”
[nou6e2b] (score 3, diepte 1) >But I’ve seen a lot of customers get very uncomfortable or flat out ignore you when trying to greet them.

And unfortunately those aren't the ones doing surveys
[noqhh3x] (score 3, diepte 0) Maybe if they did more for AP they wouldn't have such an issue with shoplifting? You know... the people who's job it is to prevent shoplifting from happening? Crazy.
[norm1e2] (score 3, diepte 2) I remember near one holiday season my SD was telling me to wrap all the TVs that was being plopped on my floor while also having a bucket load of stuff to do in tech.

AP came out to ask why the TVs weren’t wrapped and I said “well I got a laundry list of stuff that in need to do as the closing tech guy as well as help guest ~~clogging up~~ seeking help”. Within a few minutes he got the SD to wrap the TVs.

It got so bad at times that some other TMs were “encouraged” to come and help wrap TVs. And it’s not like I was slacking, no I was running end to end of tech and entertainment helping people as I did my push/1 for 1s or if the opener decided not to show up, I’d have that workload too.
[norll63] (score 3, diepte 0) As both a long time retail/ food worker 90% of people do not like to be bothered when shopping or eating I myself do not like when the server asks me every 5 mins of everything is ok I'm trying to enjoy the meal I don't like when someone asks if I need anything every 10-25 ft of distance while shopping.... I gauge persons as they come in and keep an eye out if they need help or if they are looking for something I'll even inform them of deals or such that's going on either in site or apps just as a mention and that's it I don't bug them because they're trying to go about their day ON TOP OF ABOUT 50% ARE ANXIOUS/ ANTISOCIAL just literally trying to get in and get out I myself know I'm just going for specific items only in and out (as a customer) lots of times about 40% are either on their phone not paying attention or so focused they're not listening or paying attention to those around them.... it's simple they'll ask for help when needed.... I ask for help when needed.....
[nornumu] (score 3, diepte 0) The signs now taped throughout my store says it's a little more than rumored. Not that it's a policy they are realistically going to be able to enforce in any way.
[noppytn] (score 2, diepte 2) I can't believe my job is making me smile and say hello 

Putting in my two weeks as we speak
[noq6jyj] (score 2, diepte 3) Good luck performing at your next, last, job.
[nornkoz] (score 2, diepte 1) Right but it’s annoying because you never know. There’s one etl at my store that has complained about an tm not getting truck done “because she stops for every guest when she doesn’t need to.” And other ones that are on our butt for not greeting everyone. It’s annoying because some leaders will do a “you have to greet every guest (wink)” and that’s worse than just a subjective rule because now some people feel even more confused about what they’re supposed to do. But obvious asants
[nou7juu] (score 2, diepte 7) How often are district and regional in your store? Cause you're talking like they just work there every day, which has never been the case in any of the stores I've worked at.
[nopadx1] (score 2, diepte 0) I mean am I the only one that doesn’t reallllly care all that much? I mean given I am inbound and customers now aren’t going to reallly be my problem but hey. At every seasonal job I’ve had it was expected to at least acknowledge customers in a way
[nopjkhr] (score 2, diepte 0) Walmart has had the 10 foot rule since Sam Walton was alive.   It is not like Target is going to post armed guards on every aisle to ensure your compliance.
[normzhe] (score 2, diepte 3) Nononono we’re the same! We sell food! /j
[normwx9] (score 2, diepte 2) Well then maybe he can explain it lol 😂
[nopv4oz] (score 2, diepte 0) This isn’t rumored, there was a company wide email this week proudly talking about it
(51 reacties met lagere score weggelaten)

=== THREAD 1o89m34 ===
SUBREDDIT: r/BuyItForLife
DATUM: 2025-10-16  SCORE: 50  REACTIES: 95
TITEL: Open back house slipper/shoe for extreme arches?
POST (source_id=post):
I really dont want to have to wear actual sneakers with an insole inside all the time. I bought one of the arch support house shoes on amazon but its not nearly high enough. Has anyone found anything that is good for indoors thats not like a traditional sneaker or running shoe? Really doesnt seem like theres many options

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[njtalde] (score 165, diepte 0) You probably need to have a shoe insert - maybe one specifically made for your arch issue. Then you can put it in whatever shoe or slipper you want.
[njtafkw] (score 105, diepte 0) Have you tried Birkenstocks? I consider I have *fairly* high arches and they have molded to some pretty solid arch support.
[njtce8a] (score 40, diepte 0) You need to look at Oofos. They're technically recovery sandals, but feel like a cloud.
[njtdxac] (score 34, diepte 1) This. I have house Birkenstocks that only wear indoors.
[njte8wc] (score 16, diepte 1) Their arch looks more severe than mine and Birkenstocks don't even touch my arch.
[njtflr9] (score 15, diepte 0) I’ve found that high arches don’t need arch support at all, that’s not where the pressure is going! People with flat feet need arch support more than people with high arches… You need heel and toe support so.
A high arch tends to “Supinate” or roll outwards. Therefore Arch support has little or no effect and can worsen alignment issues.
[njv2goz] (score 12, diepte 1) I can highly recommend SOLE soles with the MET pad (Get the red one). They're home-moldable and have saved my feet, and by extension my back. I have wonky arches too. They're made with EVA and kinda stiff so they're super easy to swap around.
[njtiuyc] (score 11, diepte 2) Same! They're my 365-house slippers <3
[njtesc0] (score 11, diepte 0) I put my custom orthotics right inside my Ugg slippers. It works!
[njtezqj] (score 9, diepte 2 OP) yea lol i can tell by looking at them its like half the height i need. my arch is insane
[njtbipu] (score 9, diepte 0) i have high arches and wear my birkenstocks 24/7 in the house. they take a bit to wear in but once they do they're molded to your feet and provide perfect support
[njth275] (score 9, diepte 0) Look at slippers from a brand like Vionic. They specialize in arch support 100% recommended
[njtpgio] (score 8, diepte 1) I have high arches and roll inwards. I absolutely need arch support.
[njtx2zk] (score 7, diepte 1) My high arches do need support. Otherwise, I walk on the outside of my foot and mess up my knees. Per a medical doctor who diagnosed my tendinitis caused by not supporting my arches.
[nju5a6r] (score 7, diepte 0) I question if any slipper is BIFL, but I have some Keen Howser slippers that are very comfortable with someone who has a high arch and are quite durable. Keen soles in general I find to be hard wearing. They are slip on, but not backless. I find the backless shoes get too loose with a high arch because you put more pressure at the top of the opening. 


Mine are 3 years old, I've worn them outside way more than I should and still holding up great.
[njvnhzg] (score 6, diepte 2) Sole makes (made?) moldable flip flops that might do the trick for you, op. The Sole stuff tends to be pretty good for high arch feet.
[njtdo15] (score 6, diepte 0) Any vivobarefoot shoe will do: [https://www.vivobarefoot.com/](https://www.vivobarefoot.com/)

The best support for your arches will always be the muscles and tendons of your foot
[nju6zhk] (score 6, diepte 1) I'm a big fan of Wildlings
[njtl3ro] (score 6, diepte 0) You should start with a physical therapist also.
[njuyqkc] (score 6, diepte 0) Your feet are FUCKED my friend. Im sure you know.

Go to an actual podiatrist or a cobbler (The Red Wings are neither of those.) They'll help you out. No commercially available slipper will probably even hold the inserts you need.
[njtf5ob] (score 5, diepte 1) These were recommended to me by a podiatrist. Higher arch and soft like crocs. They really helped me.
[njuz08e] (score 5, diepte 2) Crazy to me that a podiatrist would recommend them.
[njx1cl3] (score 5, diepte 4) Because they’re just not allowing the foot to function properly. Short term, they’re fine, but for plantar fasciitis, you’re going to want to do specific exercises and stretches and elongate the Achilles. A slight heel can help take some stress off the Achilles if walking a lot, but overall, your wife should be listening to and working with a physical therapist more than a podiatrist.
[njurzo8] (score 4, diepte 3) I'm following this, and specifically you because we have very similar feet
[njtfl96] (score 4, diepte 1) I had a pair of Birkenstocks that lasted only about 3 years before they were completely worn out. I replaced them with a pair of knock off soft moc sandals and now 8 years later they’re still in fine shape.
[njtfuea] (score 4, diepte 1) I think oofos are the answer too. Or hoka recovery slides, but I do think oofos have higher arches.
[njtgzpj] (score 4, diepte 0) Crocs
[njub4jl] (score 4, diepte 0) Look at some barefoot or similar brands. Maybe you have a store nearby where you can try different models and types?
[njuktvj] (score 3, diepte 2) Yeah Birkenstocks are way way too flat for my feet, was surprised to see this so high
[njuzaqr] (score 3, diepte 1) So much bad advice here.  (Not yours though).
[njuexjx] (score 3, diepte 1) Is this a high arch thing, or just thing for people who have feet?
[njv7j6k] (score 3, diepte 0) If you have a high arch, you want the opposite of arch support, you want a custom orthotic that has a cutout under your first metatarsal to allow your arch to drop down. 

Worth seeing a podiatrist who can assess you for a cavovarus foot deformity
[nk3cyfi] (score 2, diepte 4) It’s true, but my physical therapist said I need a high arch for insoles to start with and one that would not compress over time, birks can’t offer that in either regard bc the arch doesn’t start high and does compress/mold to your foot. That’s a problem for me with high collapsing arches. I wish!
[njv3pdp] (score 2, diepte 2) sometimes those inexpensive buys surprise us - I have a 20+ year old pair of $5 fake crocks with barely a crack while my real crocks are showing wear at 3 yrs. Always take it as a win!
[njtb7l1] (score 2, diepte 0) You’re not gonna find anything like slippers that have the support you need, best bet is to get boat shoes like dockers and use a really good insert.
[nju0uy3] (score 2, diepte 1) Anything with a cork bed yeah, great for any foot
[njwzuyj] (score 2, diepte 3) Why?  My wife’s podiatrist recommended them for her plantar fasciitis.
[njvhr2e] (score 2, diepte 2) I've got both but prefer the Hokas. The oofos make my feet feel hot and are too cudhiony. The good news is neither build up static electricity like Crocs do for me.
[njv7o0c] (score 2, diepte 2) neat, they actually have normal shoe prices and better colours

Didnt know they existed before now!
[njvqwrb] (score 2, diepte 4) I love how the internet insists that you can't be a certain way because...something something something. 


I have high arches too. With inward camber, and never wear tight toe boxes. My feet are long and narrow. So even narrow shoes are not tight on me.


Same as oily hair/skin and the trend to tell people that you are wrong if you was your hair daily.  Yeah, I prefer not to break out in head acne because not washing doesn't stop oil production.
[njy7yqu] (score 2, diepte 5) Your definition of tight toe boxes and theirs might be entirely different though.
[njtie6m] (score 2, diepte 0) Halflinger makes some great ones.
[njv8017] (score 2, diepte 2) If you have feet you have muscles and tendons in them

Most people are oblivious to the normal range of motion of a foot so its not something thats easy to explain in text
[nju27mz] (score 2, diepte 0) I don’t have any recommendations for you, but my footprints look exactly like that and I feel your pain.
[njucv5c] (score 2, diepte 0) This is probably a stupid question, but how did you get this analysis of your foot/pressure? Something from a doctor or so feature on a scale or something?
[nk0uyee] (score 2, diepte 1 OP) a running shoe shop local to me had some equipment to step on
[njuj8v1] (score 2, diepte 0) Are you a ninja turtle?
[njx7jbw] (score 2, diepte 1) There are different types of high arches.  The type that needs the solution you described is in the minority. 

So yes see a doctor.
[nk0vblt] (score 2, diepte 1 OP) 😂😂😂
[njt9is2] (score 1, diepte 0) Hello /u/ZiostShadow! Thank you for your submission! just to inform you, you may also want to try posting in /r/boots which is a smaller subreddit but might be or specialized for your request

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/BuyItForLife) if you have any questions or concerns.*
[nk3ckc7] (score 1, diepte 3) Because you have to wear them in. They mold to your feet over time. Not sayings it enough to compensate, or at all the right choice, but they come very flat and the arch becomes more prominent once you break them in and it molds to your foot
[njut6h6] (score 1, diepte 1) I have similar arches to OP and wear Birkenstock house shoes and they do pretty well. Still not as nice as my normal shoes with custom insole, but they let me be comfortable in my own home
[njwpiko] (score 1, diepte 1) I recommend Shearling Kyotos to everyone. The most perfect house shoe.
[njx1tqj] (score 1, diepte 1) I would say, with high arches the heel of the birks are too low.
[njw5tiv] (score 1, diepte 1) Yes, this is exactly what I did
[njtdzci] (score 1, diepte 1) They make slippers. Just got mine a couple weeks ago and they are very nice.
[njv9rgj] (score 1, diepte 1) Absolutely. I recommend them to everyone and give them as gifts. They are fantastic.
[njvggsh] (score 1, diepte 3) I don’t wear narrow toebox shoes. Thanks for attempting to diagnose me over the internet via somebody trying to sell stuff though.
[njyum6g] (score 1, diepte 4) If it's not a traditional "barefoot type" shoe (unlike crocs which are not marketed as a barefoot but it's a wide toebox), it's almost certainly a narrow toebox shoe

I merely stated the facts. whether you think I attempted a personal diagnosis is up to you
[njzr5mg] (score 1, diepte 6) they are running shoes, far from any anatomical shape, and are generally bad for the feet

https://youtube.com/shorts/Qq2KkUl98hg

the spring action will lead to body accomodation and once you take it out, you risk injuries to the muscles that are not normally used when practising running on said shoes. they generally make our body worse compared to barefoot running, unless they are ever so slightly cushioned for runners that primarily run on concrete or asphalt (plus they're banned from competitions as far as I know).

I'd list all the papers I've gather but it's a Reddit discussion, it will be pointless regardless of what proof I share

Do not base your knowledge on market demand and brand trends. Scihub is here for a reason.
[njztqk3] (score 1, diepte 7) Literally every single “bad shoe” in that short you posted is a racing shoe, most of which cost $200+ USD and nobody would ever think of wearing as an everyday shoe. Nice disingenuous argument you have there, I’m not wearing a Saucony Endorphin Elite as a walking shoe.
[nk03lxm] (score 1, diepte 8) You mentioned "Veloci", I used what you have mentioned. If you go on their site, those are the main shoes they promote. At least don't use arguments that go against what you say.
[njtfn01] (score 1, diepte 0) Oofos has been a life saver for me. I honestly wish they made some non slip shoes so I could wear them at work
[njtwjev] (score 1, diepte 0) Whatever you wear, please stretch your feet too
[nju65ze] (score 1, diepte 0) Crocs
[nju8n8v] (score 1, diepte 0) My feet are a lot like yours and the only thing I have found that works for me is Oofos slides - they make shoes and maybe even slipper type things now but I haven’t tried them.
[nju9b6d] (score 1, diepte 0) Crocs
[njubqn9] (score 1, diepte 0) Olukai makes a very comfortable loafer, they last forever, too. I have really high arches and they are one of the only comfortable slippers I’ve ever tried on.
[njuhlag] (score 1, diepte 0) I love my Lusso Cloud slippers. They’re pricey (150$+ with shipping) but if it isn’t the most comfortable slipper I’ve worn, I’ll eat my shorts. They feel really high quality, I’ve only worn them for about a year now but so far they’re great for outdoors and indoors.
[njujgor] (score 1, diepte 0) Many folks will recommend Ofoz. I love my [Oboz Whakatā Coast slippers](https://obozfootwear.com/en-us/product/all-gender-whakata-coast?utm_source=google&utm_medium=cpc&utm_campaign=17622857468&utm_content=136154647337&utm_term&gadid=607295741465&gad_source=1&gad_campaignid=17622857468&gbraid=0AAAAADj2Ifrz3DNQwflES5kojDGH4mzyl&gclid=CjwKCAjwr8LHBhBKEiwAy47uUst1BEfdDXS9N1DZ3WxtMDWnhXUx9TsKPNtjLcfvezN_lmEEyIIAsxoCJYkQAvD_BwE) (That's O'B'oz with a "b"). The arch is great, the cushioning feels like firm foam rubber, and it's very stable. I like to wear them with socks because my feet get a bit sweaty. They have changed the game for me.
[njulaha] (score 1, diepte 0) I have high arches and my physical therapist (who is a doctor) recommended Orange brand insoles and seeing a podiatrist if needed. Orange did me very well, the arch is high
[njus7tp] (score 1, diepte 0) Spenco sandals got rid of my plantar fascitis.
[njuvrpl] (score 1, diepte 0) Physical therapy and walking/standing classes.
[njuygk7] (score 1, diepte 0) Toe socks with Archie's thongs
[njuyuh2] (score 1, diepte 0) Are you doing any foot, ankle hip exercises? I have very high arches as well. I get a bit of the outside of my foot contacting though, so not as severe as you.  What worked for me obviously may not be right for you? But slowly adjusting to barefoot / minimalist shoes and doing foot exercises helped me immensely.   It was presented to me that orthotics and all of the extra arch support options worked to weaken the foot, which made sense to me. If you’re not allowing the foot to function naturally, it’s going to weaken.  This can make the arch problem worse and ultimately not help the situation.   [https://gaithappens.com](https://gaithappens.com) is one of the resources that helped me.
[njuywtp] (score 1, diepte 0) I have crazy high arches too. I LOVE Vionics! Also, Haflinger great.
[njv0yhi] (score 1, diepte 0) Do you feel pain somewhere?
[njv5b5t] (score 1, diepte 0) Geometry of my feet is pretty similar to yours. Hoka Recovery slides for the win!
[njzwv78] (score 1, diepte 3) Not true.

https://claude.ai/share/1cb72547-d756-4bef-bdbc-a8ddd1a280e0
[njvcsx6] (score 1, diepte 0) Dansko clogs
(19 reacties met lagere score weggelaten)

