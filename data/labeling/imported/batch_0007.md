# Label-batch batch_0007

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
Schrijf het resultaat naar `batch_0007.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: vhhmd4, uzxhzr, 10d2jye, 1r05m08).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD vhhmd4 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-06-21  SCORE: 27  REACTIES: 64
TITEL: Saucony Endorphin speed… what is the hype?
POST (source_id=post):
So I was wondering what you use the endorphin speeds for? And why are they regarded as one of the best shoes of 2021 (2020?). I have run about 100 miles in my pair and here are my thoughts:

They don’t work for easy days (pace 5.30min/km) for me cause I actually think they are kind of firm for slower paces. A bit unstable and clunky at times. 

I have taken them on for a half marathon (pace around 4.50min/km) and my feet hurt afterwards cause they are so snug. (HM PR 1.39 in alphaflys). Sure they were light and had good breathable upper, but still felt a bit heavy under foot and not so snappy.

I think they are best of as 5k road race shoes.

What are your thoughts on the speed? Did you also get kinda disappointed about the hype?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[id7joqa] (score 43, diepte 0) You skipped right over their intended use. 

The Endorphin line went:

Shift -----> Daily trainer

Speed ---> Speed work

Pro ------> Races
[id78ns6] (score 37, diepte 0) Not at all.  I used them for Speed work and tempo runs.  Destroyed so many records with them on Strava.
[id7eg8s] (score 33, diepte 0) I think a lot of folks on here are lighter runners and so the nylon plate provides a lot of pop and the squish of the foam provides good recovery.  I just grabbed a pair of speed 2's and I don't like them nearly as much as my pro 1's.  However I am a heavier runner 6'4" 215ish.  I find it easy to flex the CF plate at nearly any pace and it find it holds faster paced better.  The speeds are fine, just not as great as the pros.  My other favorite shoes are the sketchers razor excess+. They are so light and easy to run it, they just make it so effortless.  Great kind of everyday shoe.
[id7qrbw] (score 18, diepte 1) Hmm I feel like they should name them appropriately then, something with Speed in the name, I dunno…
[id7xm2t] (score 14, diepte 1) I would say the shifts are not all that great as daily trainers unless you need the stability. They just aren't soft enough given the stack height and intended use, which is a bummer because I like the upper and the rocker. There are other models in the Saucony lineup and other brands that I prefer. Top of mind would be the Hoka Clifton.
[id7d1s3] (score 13, diepte 1) Both of you are correct… shoes are literally a personal preference 😂
[id79fg5] (score 10, diepte 0) Have to say I had the opposite experience. Even better than I imagined. They certainly worked my legs in a new way, but felt snappier than any other shoe I've tried. Just hit a 10k PR in them this weekend. But I for sure can't do easy runs in them because they make me want to push the pace too much. 

To be fair, I'm only in my second year of running, though, so take my opinion with a grain of salt!
[id7tkfq] (score 10, diepte 1) I’m also a heavy runner (6’1” 235) and find that the speeds are good for some of my longer runs during the week and help keep my legs from feeling beat up. Not sure if it’s the plate, foam or the combo but I love throwing them on feeling fresh at the end of a run. So far haven’t had any stability issues with them, even at paces around 10 min/ mile on slow runs.
[id7avrb] (score 9, diepte 0) I actually use them primarily for long runs these days, which I typically run at 4:10 - 4:30 / km pace. I don't know what it is about them, but I tend to get a free 5-10 seconds per kilometer at that speed compared to other shoes. Even with my pair that has 750km on them. I would agree that they're a bit too narrow in the mid foot, but it doesn't cause any issues for me. They're just nice and springy, I can't quite put my finger on it, but I like it.
[id8jr4m] (score 9, diepte 2) Hard agree. PWRRUN is a terrible foam. I don’t get why people drool over the Shift and Ride and then shit all over Brooks for being boring. DNA Loft is soooo much better than PWRRUN. Almost all of the major brand’s premium EVA foam is better than PWRRUN. I haven’t tried the newest Ride 15 so maybe it’s better now. But the Shift is a dud. There’s absolutely no reason to have that much stack of such a firm foam in a “stability” shoe no less. People only buy it because it’s marketed within the Endorphin line, so they think it’s going to be a “fun” shoe. But every time I use mine, my experience is the opposite of fun.
[id8s65y] (score 8, diepte 2) Comparing the Speed to the Alphafly is hardly apples to apples. Nike litterally developed the AF to try to break the (previously thought to be impossible) 2 hour marathon. The Speed is used as a daily trainer for many and a tempo shoe for others. I use them for daily training, speed work, and long runs. 

I'd be perfectly happy to race in them, but have a few other options I use for that very specific use case.
[id8a0e6] (score 8, diepte 1) I agree. I think the Speed is a great shoe for people who don't have the speed/weight to get a carbon plate to bend. I'm a lighter runner and love the things.
[id7c8xg] (score 7, diepte 0) I just ran my first marathon in Speed 2s and was really pleased at how well they held up and that I had no blisters or other foot issues. I finished in 4:05 - so a little over 9 min/mile pace. 

I’m on my 2nd pair (and have a 3rd in the closet). I don’t use them for easy runs, but I grab them for most all of my tempo work and a fair amount of long runs. I also have a pair of the Pro 2s, but they feel too unstable for me and have given me ankle issues - hoping the wider midsole in the Pro 3 solves this for me.
[id7kpns] (score 7, diepte 1 OP) Yeah, perhaps this is my issue. Need to put some faster miles in them or speed work etc. thanks for the input!
[id7u0gu] (score 7, diepte 1) I'm out here running almost all my runs in my Pros. Probably not the greatest idea, but by far the most fun I've had running
[id8y7k7] (score 6, diepte 2) The super shoes with carbon plates are made for elite runners who aren't carrying a lot of weight. Eliud Kipchoge apparently weighs 52kg.

In my experience the foam of the Vaporfly is so soft I almost feel it bottom out. I'm a 70kg guy. The Speed does not compress in anything like the same way, for me. It always a combination of the plate and the foam. The nylon plate may be more flexible but the foam is firmer. For me it just works and wants to skip me through to toe off. Maybe it just suits my running style.
[id86yfn] (score 6, diepte 2) I've run the Pro 2 for long runs, tempo runs, pace runs, speed work, even easy runs. They work for me just fine, Speed 2 the same.
[id7xhdp] (score 5, diepte 2) I'm another heavier runner and have a similar experience to you. My only issue with them is when I'm tired and can't control my pronation. 

But that's my problem, not the shoe's.

They're my favourite of the plated shoes I've tried.
[id7fn9w] (score 4, diepte 1 OP) Great input. I weigh 68kg and I feel a bit of pop but not nearly as much as in the alphaflys at the same paces.
[id7mdda] (score 4, diepte 1) It is definitely on the firmer side of super shoes. 1 of the firmest
[id7px44] (score 4, diepte 0) They are the only shoe I’ve ever felt that were too unstable for me. Every time I tried them I got some soreness in the front of my ankle no matter what pace I used them for. I have not had that problem with the vaporfly or Alphafly.

However I love the Endorphin Pro. They are my favorite shoe for short intervals to marathon pace workouts.
[id8qmsn] (score 3, diepte 2) Optimal 400m (straightaways no turns)-10k
[id8ra8k] (score 3, diepte 2) I also felt they were going to be just hype as well.  Hell, i didnt believe the whole plated shoe stuff….then I tried them….couldnt believe how fast but with ease they made runs.  Going into 16:45 5k felt effortless compared to my Hoka Rincons.
[id7ctgw] (score 3, diepte 0) I've run a couple of interval workouts in them, but mostly use them for faster long runs. Several runs of 17-20 miles where I progressed to marathon pace (6:40). I did have pain with them before I relaced them to skip crossing between the first pair of eyelets.
[id97am9] (score 3, diepte 3) Hate the Shift. Love the Speed and Pros. 100% agree.
[id7o6i4] (score 3, diepte 0) Shoes are definitely personal preference thing, but I use Speeds for my daily, tempo, and often long run shoe. I’ve got about 500 miles in Speed 1’s and another 200 in Speed 2’s and they are the shoes I reach for first. They just work for me - they fit well and they’re comfortable for my daily miles (easy days around 8:40 min/mi), and I get the performance I need when I want to push the pace a bit (down to about 6:30 min/mi). They’re not the cushiest out there or in my closet but I’ve been perfectly comfortable going 22+ miles in them on long days. I’ve noticed the 2’s take more time to break in (or mine did anyway) and that they were a little snug until I got to about 100 miles in them but now they fit like a glove. For reference, I also have Atreyu Base Model v2, Atreyu The Artist, and Hoka Mach 4’s in my rotation currently.
[id7rlby] (score 3, diepte 0) I think the Speeds are a good shoe that can handle multiple types of runs (speed work, tempos, long runs, racing) if you only have 1 or 2 shoes. However I have a lot of shoes and felt it wasn’t my primary shoe for any of those types of runs. Here is my rotation.  

* Takumi Sen 8 - speedwork, intervals, tempos, racing
* Endorphin Pro - tempos, long runs at Marathon Pace
* Novablast 2 - endurance and easy long runs, recovery, shorter easy runs
* Next% 2 - long run at MP, racing
[id8ft1w] (score 3, diepte 1) It depends on what you are comparing it to
[id8a5zl] (score 3, diepte 0) Very disappointed. Midsole has a lot of cushion but it's firm? Total regret
[id93oqk] (score 3, diepte 0) Can we talk about Zoom Fly 4? Oh sorry wrong thread.
[ida8arh] (score 3, diepte 0) I recently smashed my half PR wearing speeds.

I almost felt like I was cheating, felt guilty almost
[ida17de] (score 2, diepte 2) one has a carbon plate the other is nylon, wouldn't that be why? I used them for workouts or long runs with some marathon pace and never had any stability issues nor felt any clunkiness, I do all the warm-ups and cool-downs with them at very slow paces, like below 6. Don't know what to say, they don't work with some people, as with the sizing I went a half size up on the 2 cos of the narrowness. Anyway I found the originals better than the 2
[id9kinm] (score 2, diepte 2) I can only confirm, that my legs don‘t feel nearly as beaten up after a hard interval session with the speeds as with previous non-nylon/carbon-plate shoes. Somehow it lessens the stress on my shins and plantar fasciitis. 
Would you think that even softer carbon-plate shoes would make this even better?
(70kg at e.g. 3:20min/km interval pace here)
[id9kwjx] (score 2, diepte 2) Asics Novablast 1 or 2 aren't too bad for easy/moderate days. They aren't really a stability shoe, but there's enough cushion and "spring" in them to help make the miles fly by. The laces are pretty great, probably my favorite on a recent pair of trainers. 

My other new shoes are New Balance [M880v11](https://www.newbalance.com/pd/fresh-foam-880v11/M880V11-MPS.html). Those are alright. Good stability and general cushion without a hefty amount of feedback. Profile is lower for a little extra drag resistance 😉
[id9mzbn] (score 2, diepte 3 OP) Thanks for the input. I actually have the novablast 1. I like it for easy/moderate days, but I don’t love them :D
[id8l696] (score 2, diepte 2) Why not?  I use them for long runs and feel like I can go forever.  Speeds are good but seem a little flatter and more limiting.
[id8o15e] (score 2, diepte 3) I think in lower stack applications like the Kinvara and Peregrine it is great because it deadens the ground feel more than a softer foam would and being a lower stack, lightweight shoe you can allow for and might even want the firmer ride. But why would you want it in a high stack shoe? It just feels like you're running on a brick.
[id8vucy] (score 2, diepte 1) I love the speed and like the adios too.  The speed is MUCH firmer than the adios...
[idc4qwu] (score 2, diepte 1) I'm really liking the Boston 10 for long, slow runs.  Adiós 6 for tempo and Endorphin Speed for long fast runs.
[id93k47] (score 2, diepte 1) Here here!
[id7xpx9] (score 2, diepte 0) If they weren’t so unstable, I’d have liked them. But I probated hardcore in them when it’s never been a problem for me in neutral shoes before. Also, the outsole on them leaves a lot to be desired in my opinion. I can’t picture running in them on even a slightly wet day. They’re a phenomenal shoe for those who they work for, but I don’t think they work for everyone.
[id8hz7y] (score 2, diepte 0) They are the up tempo shoe that many use as a daily trainer, much to the ire of genre purists on this subreddit. 

Me?  I have an issue with the term "daily trainer," as I only run three times a week, all of my runs between six and ten miles each, all with solid pace. So, for me, the Speed 2's can be worn each and every time I run. I love them for these purposes.

I can't get over how stable they are for being so light. Others in this thread are saying they are unstable - I find their stability a big strength, especially for how lightweight they are. <SHRUG.>
[id8kqry] (score 2, diepte 0) One of the best shoes I have ever run in.  Not everybody likes the same thing.
[id8sebx] (score 2, diepte 0) I use mine for speedwork (so 400m repeats or 5 minute intervals).  I'll also do parkrun in them, tempo runs and long runs if running at marathon pace or between Marathon pace and easy.  For long easy runs, I use a cushioned shoe
[id915hd] (score 2, diepte 0) It’s interesting seeing everyone’s opinion on this and that being a lighter runner could have an impact.  I’m very short, light weight and run very slow paces by most runners standards.  I run 4-6 miles on most days at a 10-11 min pace and am absolutely in love with the shoe.  It has been the most comfortable shoe I’ve used so far and I find it to be very lightweight.  It’s my every day trainer.
[id98aix] (score 2, diepte 0) Although zoomx is still king of foam, the endorphin speed has pretty much worked for me, across all paces. I mostly take it out for marathon pace efforts ie around 4-4.3/km pace but I’ve even done recovery runs in it no issues. Height 5’8 weight 65kg.
[idavaxb] (score 2, diepte 0) Obviously the shoe varies from one person to the next. Overall, I think the shoe can be used for anything. I'm on my 6th pair. use them as daily trainer covering a variety of paces, distances, and elevation. Flat 10-15 miles at 7:00 to 50k with 2700' of climbing at 7:30 to 47 miles of a 100 miler at 12:30.  

Not sure why the conversation is on repeat every other day. It a pretty good shoe especially when it can be had for $90. If it works for you great if not move on to something else.
[idcab3a] (score 2, diepte 0) They’re too firm for me to do long runs in them. My legs were beat up the first time I went past a 10K lol. Need some more cushioning for those runs. 
I do love them for shorter tempo workouts. They basically push u forward with its rocker and they’re really light on feet, which makes me want to go fast.
[id78vff] (score 1, diepte 1 OP) Thanks! May I ask what speed and distance you think is optimal for them?
[id9hjwe] (score 1, diepte 3) This makes sense to me, I am a heavy runner also, I try to stay away from high drop , super shoes ... and aim for max cusion and low drop shoes. 

My only more "srping" shoe is Adidas Boston 10
[id94a5u] (score 1, diepte 2) Seriously, I have finally found shoes I enjoy running in post Lunarglide and Lunaracer, but I could run in the Pros for speed work to long easy. And I’m heavy and flat foot. My speeds are recovery shoes because they don’t injure me at 9:00 pace like they do at 6:15.
[id7k5y9] (score 1, diepte 0) They were too soft for me, I prefer a firmer footbed when I’m running or doing tempo work.  

I use Adios 6 for tempo work, and the Boston 10 for daily and long runs.
[id7t52h] (score 1, diepte 0) Never tried them but a lot of times hype leads to disappointment. Much easier to be happy with something you have no expectations for.
[id7tqb1] (score 1, diepte 0) In the fall of 2020 when I first tried them I thought they were amazing. At the time they were my first plated shoes. After more plated shoes became available they really fell out of my rotation. They are a Jack of all trades master of none type shoe for me.
[id7x80p] (score 1, diepte 0) I love my Speeds, but they are not a daily trainer for me. They are a little too unstable for me to use every day (although I find that to be less of an issue as I get used to them) and I always end up running faster than I intend when I wear them. They just feel like they were meant to go fast.

I whip them out for my weekly social runs (a "friendly" 5k where we end up racing every time) so that I can pick up a few free seconds, and I used them for a 10k race the other day to great effect.

I can't compare them to the pros, but I can say I definitely enjoy running in them. Just use them sparingly.
[id89iv9] (score 1, diepte 0) How on earth can people find the speed firm? They feel incredibly soft for me.
[id8bs88] (score 1, diepte 0) The Speed 1s are snappy and have an incredible energy return in comparison to most other shoes…I’m so spoiled from mine. I just got the speed 2s and they have less response than the 1s, so hoping the 3s address that?
[id8dmlk] (score 1, diepte 0) Call it manufacturer differences but to me my original black Endo Speed 1's are my favorite shoe of all time. I have Vaporfly's for half marathon>above, Endorphin Pro for long run trainings, and Takumi Sen for track workouts. To this day i still use my speed 1's as my preferred 5K & 10K races. For whatever reason i feel the forward propulsion and ability to hit pace fast is better than the Takumi Sen or Vaporfly for me. I have run 3 sub 17 minute 5K's in them and have failed to do so in the Takumi Sen and Vaporfly. For whatever reason though i have a pair of the Endo Speed 1's in Neon and I don't feel the same tilting sensation. I just got a pair of Endo Speed 2's during the crazy discount and they feel much softer and i did an 18 mile progression run and that's probably how i will use them, for my biggest marathon training long runs that have me mixing easy pace w/marathon and tempo. I will say it is a bit awkward running easy miles in them but it's doable. since i use them on long training runs that mix easy miles w/tempo miles i find myself always running my easy miles 20-25 seconds too fast.
[id8ixue] (score 1, diepte 0) I’ve worn the speeds for track intervals, easy runs, tempos, long runs, hill repeats, tried them in all scenarios…
Where they absolutely sing for me is a fast long run.  My normal training run pace is about 7:30 per mile. On long runs, I’ll often do a progression run, or marathon pace, or some kind of uptempo running. When I hit 6:30s in them, I feel like I can go 10-15 miles and not even blink. 
For what it’s worth because there is a lot of discussion in the comments on this, I’m 5’10 and 160lbs
[id8jbm4] (score 1, diepte 0) These are my favorite shoe to run in, and the only reason I don't run in them all the time is because they almost feel "too good" - the energy return from the midfoot/heel (where most of the foam is) almost feels like cheating. I've ran everything from easy runs to HMs to long runs to intervals in them.
[id8nb7x] (score 1, diepte 0) Here we have somebody with a differing opinion making a big 'ol post about it.
[id8rsce] (score 1, diepte 0) Yeh I bought them because of all the hype, first time I tried them on they were so uncomfortable. Every time I wear them I get injured (worn them 3 times). They are just way too huge and clunky, and do not increase my speed. I prefer more minimalist shoes.
(5 reacties met lagere score weggelaten)

=== THREAD uzxhzr ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-05-28  SCORE: 109  REACTIES: 53
TITEL: Saucony and Nike $50 per pair in store at Fleet Feet (tons of models, colors, and styles)
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iad1s67] (score 31, diepte 0 OP) I stopped by my local Fleet Feet store in NYC (14th street) and there were two big tables and every pair of shoes were $50 each. The employees kept bringing up pairs from the basement. I bought two pairs of Endorphin Pro 2s but I could’ve bought more in different colors. Incredible selection if you can go to a store!
[iadx6hw] (score 9, diepte 1) WHAT.

What other shoes were 50 dollars?

I might as well hit up all the fleet feets in nyc.
[iad51et] (score 6, diepte 0) What an awesome deal!!
[iadc5dl] (score 6, diepte 0) I'll check out a Fleet Feet store in Seattle tomorrow and report back if they have some sweet deals.
[iad6rul] (score 5, diepte 1) Ah I’m in the city too. I took advantage of the crazy Saucony sale yesterday, so no more splurging unless they cancel my order🤞

Were they floor samples/returns or brand new? Were they all final sale?

Did you happen to see any Nike Infinity or Invincible in size 10? Any idea how long the sale is going on for?

Thanks!
[iad7jje] (score 5, diepte 2 OP) It’s in-store only but other locations might have the same deals. The employee I spoke to said they were getting rid of old models because new ones are arriving soon.
[iad7bru] (score 4, diepte 2 OP) They were brand new. I think I saw a sign that that they were final sale but an employee told me that I could exchange them if they didn’t fit correctly. He could’ve been mistaken though. My receipt says clearance. I didn’t look too closely at Nike, so all I can say is that I specifically checked for Alphafly and Vaporflys and didn’t see any. The was a designated table that only had Nike and it seemed like a good mix. They had signs that it was a Memorial Day sale so my guess is through Monday but I’m not 100% sure.
[iagcf3g] (score 4, diepte 2 OP) There were Saucony Endorphin Speed 2, Pro 2, and Triumph 19. There were a lot of Nikes but I don’t remember the models because I wasn’t as interested in them. I only checked to see if there were any Vaporflys or Alphaflys, but there weeent any. If you go can you post what models you see? A couple people asked but I didn’t have an answer
[iahvg6f] (score 4, diepte 2) What the!!!! Holy smokes
[iadz7dz] (score 4, diepte 0) Ouch. I just bought a pair of Triumph 19s a week ago from a Fleet Feet store, now they're $60 cheaper. My timing is pretty bad.

Update:  I was able to "return" the shoes I bought last week and buy them back at the new discounted price from Fleet Feet without much hassle. They were understanding given the significant price difference. Overall I've had a pretty positive set of experiences with the staff at my local store.
[iad86i1] (score 3, diepte 4 OP) There was a low to normal amount of people in the store. Probably 6 other customers and 4 employees. I didn’t see any Puma on sale. There was one stack of Saucony and one stack of Nike.
[iagneu8] (score 3, diepte 1) Thanks to this post I got a pair of Endorphin Pro 2s for $20. It feels like theft
[iad47xp] (score 3, diepte 0) Thanks for sharing! Great deals! What other models did they have?
[iad6rgr] (score 3, diepte 1 OP) They had Saucony Pro 2, Speed 2, and Triumph 19. I didn’t look too closely at Nike, but there was a whole table filled with pairs and there weren’t any Vaporfly or Alphafly. Unfortunately I’m not as familiar with Nike so I can’t remember the models
[iad56qo] (score 3, diepte 0) I wish I lived in NY lol. Local store didn't have anything :(
[iaf8x4j] (score 3, diepte 2) I called, and they're not doing anything crazy aside from price matching the Saucony website.  Sorry, Cal.  No shake and bake.
[iadowvu] (score 3, diepte 0) Has anyone checked the Chicago Fleet Feet stores?
[iafuuq7] (score 2, diepte 5) Huh then there’s a good chance my order will get cancelled too… 😔

I also stacked my order with the Amex $20 off $100 Saucony offer, so it was like $40 for the Speed 2’s!

I’m thinking about stopping by to check out the sale as a backup plan. $50 tax free is still an incredible deal.
[iafvyx4] (score 2, diepte 6) I called and they had no idea why my orders kept getting canceled but they told me my third order would ship. I’d call them.
[iag2jih] (score 2, diepte 8) Super helpful and very nice. I did have to wait a bit but they said it would ship🤞🤞🤞
[iag5gxk] (score 2, diepte 9) Thanks! Just spoke with online chat and they said my order finished processing, so it shouldn’t get cancelled🤞 

I’m still tempted to check out the sale… Maybe I should leave the wallet at home 🤣
[iagnx3x] (score 2, diepte 2 OP) Fantastic! Glad you were able to get a good deal!! I feel bad because I assumed this was happening at all locations but a lot of people are saying their store isn’t participating
[iaedbo5] (score 2, diepte 0) I just bought a pair of Nike Invincibles for $144 during [Nike.com](https://Nike.com)'s memorial day sale only to find it's $108 on Fleet Feet's website (didn't know about this store before). Pain.
[iagen1h] (score 2, diepte 0) Just went here and picked here a pair of Nike invincible for $50. So fair they still got some endorphin pro 2 in 8.5-10.5 and some triumphs
[iagnosq] (score 2, diepte 0 OP) I assumed this sale would be happening at all stores, but I’m seeing a lot of people say their location doesn’t have it. I went to the Columbus Circle store (also NYC) and they had the same models but the size selection wasn’t great. I checked the Nike models and I saw Pegasus. Sorry if anyone made a trip and didn’t find anything! I got really lucky yesterday because I only needed a running hat and almost didn’t go
[iagp7nr] (score 2, diepte 0) Dallas Fleet Feet did not do $50 or under for the Saucony, just the 40% price match from the website. But had a ton of other great deals. I snagged quite a bit more than I came for.

\- Saucony Endorphin Speed 2 price-matched website, \~$90

\- Nike Pegasus 38, $30

\- Saucony Freedom 4, $20

\- Nike running shirts, $12

\- entire box of Gu (12), $5

\- entire box of Honey Stinger (10), $5

Tons of other deals, like Feetures buy 3 get 1 free, winter gear (sleeves, gloves, hats) all $5
[iad7s6h] (score 1, diepte 3) Thanks! How packed was it when you went?

It was only Nike and Saucony? Did you see Puma on sale? If the Velocity Nitro 2’s were that cheap… I begrudgingly need to go 😢

Thanks again! 🤲
[iad8tyi] (score 1, diepte 5) Thank you!
[iaf4bur] (score 1, diepte 2) I placed three orders with Saucony and they canceled two of them! I hope they don’t cancel the third. Do you know what the deal is?
[iaftcy2] (score 1, diepte 3) Ah damn that sucks!

Did you place the orders on Friday? You used the “bgr10” or “brm10” code? They took 50% off and then the Memorial Day sale took an additional 40% off that price. 

I read those specific codes were not meant to stack on top of one another. 

Fingers crossed my order doesn’t get cancelled 🤞
[iaftush] (score 1, diepte 4) Yes I stacked the discounts. I still have one that shows pending…
[iafwvfr] (score 1, diepte 7) I guess their system automatically flagged those stacked coupon orders. 

Was customer support helpful? I’m afraid they’ll be forced to cancel it if I bring it up to them 😂
[iad7beb] (score 1, diepte 1) Do you know if this is just a NYC in store sale or online as well?  Maybe I should go in and check it out
[iadc5ra] (score 1, diepte 3) Thanks for the info!
[iad7h6s] (score 1, diepte 2) Thanks
[iah4jj2] (score 1, diepte 2) Just grabbed pro 2s and restraint myself on the speed 2s... thanks again!

Ps went to the Columbus circle one and selection was disappointing
[iadc6sn] (score 1, diepte 1) Seattle?
[iadcebe] (score 1, diepte 2) North Carolina!
[iadjlc6] (score 1, diepte 1) Before I waste my time and drive 30 minutes to the nearest Fleet Feet did you happen to go to any of the ones in the Charlotte area? 

Not that I need to buy any more Saucony shoes this month..
[iadl7xy] (score 1, diepte 2) Nah I'm in Greensboro. I work In Raleigh but won't be heading back that way until Tuesday to check. Sorry!
[iae4pq9] (score 1, diepte 1) Seriously hit me up if they do lol!
[iag1l4m] (score 1, diepte 3) Let me just quote the late great Colonel Sanders. He said, ‘I’m too drunk to taste this chicken.
[iadr1zz] (score 1, diepte 0) Do you happen to know if they’re doing this until they sell out or was it a one day thing? I’m out of the city for the weekend 😭
[iahaply] (score 1, diepte 1 OP) They said the sale is through June 3rd so you have a chance!
[iadtum2] (score 1, diepte 0) Steals!

Maybe I will try next week if I can.
[iadv6wl] (score 1, diepte 0) These are being cleared out for the same price ish from every retailer. 

They are 40% off from saucony, more elsewhere. Picked up a few pairs for my wife on Amazon for under $50.
[iae4460] (score 1, diepte 0) I've got those yellow ones
[iaewt13] (score 1, diepte 1) This is a such a good deal this rarely go on sale here in Europe except for colorway nobody likes. I assume fleet feet uses US Shoe size, so its safe to get size 8 when I’m UK 7
[iafaxm1] (score 1, diepte 1) Thanks for this -- picked up a pair for $78 because I have leftover credit from JackRabbit before the merger.
[iajeyeu] (score 1, diepte 1) Thanks for sharing just got a pair thanks to you!
[iahgyyd] (score 1, diepte 0) I stopped by the Union Square location earlier this afternoon and there was still a decent variety of both M and W Saucony. 

The Nike selection on the floor was slimmer though. Maybe 3 Pegasus and mostly Milers from what I remember. 

I’d call to ask for specific models and sizes as they have some clearance inventory in the basement

I know for sure they sold out of size 10 M of the Speed 2’s. 

PS - This was my first time really looking at Sauconys in person and they sure are ugly 😂 The uppers look pretty cheap to me and the QC isn’t the best. And the colors…
[iahvauc] (score 1, diepte 0) Whoa. What a steal!
[iau6fu8] (score 1, diepte 0) Picked up a pair of women's pro 2 for 50.  Sizes are def getting slim
[idc9qhk] (score 1, diepte 0) This is most definitely a one location thing, likely not at ur local one

=== THREAD 10d2jye ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2023-01-16  SCORE: 4  REACTIES: 50
TITEL: Long run shoe rec, what are you wearing?
POST (source_id=post):
I need a recommendation for a new long run shoe. Currently in the middle of a marathon block and ran 14 miles this morning in my OG Novablast (I was injured when these had about 70 miles on them and just got back to running late last year) and they absolutely destroyed my knees. They've been one of my favorites for shorter daily runs, but I won't use them again for distance.

Some backstory, I'm 6'5" 215 (rapidly dropping weight, was 225 a month ago). I have a ton of shoes, but not sure if any are good for marathon training long runs. I currently have Boston 11 (probably returning them, to stiff),Nike invincible 2 (not the biggest fan of these, but they're squishy), Pegasus 39 (daily trainer), adios 7 (daily trainer as well), takumi sen 8 (tempo and threshold days, plus 5 and 10k race), endorphin speed 1 (basically brand new, had just gotten them before I got hurt and never ran in them), adios pro 3 (marathon race shoe).

Any ideas to point me in the right direction? I've thought about running my ling ribs moving forward in the speeds, but not sure how well they'll do moving towards 20 miles. 

Thanks

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j4jjw3t] (score 7, diepte 0) I do like the Endorphin Speed and used them for several faster long runs last winter (when the roads where dry). My new favorite is the Adidas Prime X though. I plan to do most of my runs in them on my upcoming trip, including some tempo and marathon pace work.
[j4jw1a4] (score 5, diepte 0) I use the Asics Glideride 3 and Hoka Mach 5 for basically everything.
[j4jbnuq] (score 3, diepte 0) I like Boost, even though it's considered heavy by current standards. I usually wear the 2018 Solar Boost for longer easy runs. I'm thinking of replacing them with the Solar Boost 4, or possibly the Solar Glide 5 which has an interesting redesign that some reviewers say is an improvement. 

I'd rather put up with a little more weight than run in midsoles that don't suit my 65 year old body. When I hear a 30 or 40something shoe reviewer extolling the virtues of the latest, lightest thing, I wonder if they'd choose the same shoe 20-30 years from now.

But I was impressed with the Triumph 20 I tried at a local shop. PWRRUN+ feels pretty much the same as the PWRRUN PB in my Endorphin Pro and Speed, minus the rigid Speedroll. PWRRUN feels very Boosty, but maybe better, lighter and livelier.
[j4jik8e] (score 3, diepte 0) I've liked my Speed 2 as much for long runs as for workouts and always feel good the next day in them. The invincible seem like they'd be ideal fun what I've heard of them.
[j4jjs8w] (score 3, diepte 2) I ran my first marathon in them so hopefully they are good for you
[j4lb3ax] (score 3, diepte 2) I'm a forefoot striker and have never had stability concerns with any shoes, but if you land back on the heel it can be pretty squirrelly, especially at slower paces. I'm usually running within 30-40 sec/mi of marathon pace on my long runs and am not trying to zip around any sharp corners either. I am bringing the Invincible for the slower efforts on my trip.
[j4k0c89] (score 3, diepte 0) I've been really liking the Nike Tempo Next% for doing long runs in (did a 14.5 miler in them the other day). It's not cushiony at all but they're very comfortable. The energy return on them is excellent which should help save your knees and quads.
[j4jjddq] (score 2, diepte 1 OP) I thought about using them, but I really want to wait to use them for races and my longer tempo runs as I get on with the training block.

Have you tried any of those? They're all shoes I've considered getting, but haven't been able to narrow it down and I don't think either of the running stores sells them. The nimbus 25 do look very promising though. May pull the trigger on the triumph and see how they do, I do like Saucony, but curious which you've tried.
[j4jvxwp] (score 2, diepte 2) Fair enough with the Adios Pro.  I've run in the NB More v3 and v4 and enjoy them.  My one issue is they get a bit heavy late in the run but it's a really comfortable and smooth ride - kind of like a minivan.  I also like that there's a natural stability with them.  I tried out the Asics but the fit just doesn't work for me so I returned them.  Enjoyed the foam though.  I haven't run in the Triumph though I'm also a Saucony fan - thought about them (and may give them a try at some point)  but stuck with the More for now as I've just found them very comfortable for those easy runs.  Not as squishy as the Invincible - more of a smooth ride.
[j4jj0cl] (score 2, diepte 1 OP) The invincible are a nice shoe, but anything close to 10 and my feet sweat so much that they start to slide around in them and I get hot spots. They are a great recovery run shoe though.

I'll try the speeds for my next long run and see how that goes. I've taken them for some 10k runs and they've been comfortable at that distance.
[j4kq00j] (score 2, diepte 1 OP) I honestly haven't even considered the prime x, which is embarrassing considering I have most of the Adizero line. How do you find the ride in those? Any issues with stability?
[j4js63t] (score 2, diepte 0) The Bostons won’t stay overly stiff for very long.  I do my long runs in Boston 11 or nike zoomfly 5, recovery runs in hoka arahi or nike invincible.  I have a very similar shoe collection to you, but spend a decent amount of time treadmill running due to weather.  On the treadmill I’ll wear pegs, adios, or brooks glycerin depending on if it was a regular run that got cancelled or a recovery.

Theoretically, running in the Bostons would be a similar feel to race day in the pro 3, at least that’s the hope.  I really enjoy my Bostons, enough that I have 2 pairs waiting in the closet, and found they really became comfortable around the 40-50 mile mark.
[j4kpspe] (score 2, diepte 1 OP) I'll give the Boston another shot then. I actually like the way they feel, but have been worried about taking them over anything longer than a couple miles. I'll use them for my weekday runs and see if I can get them to open up some for the weekend.
Thanks
[j4jw608] (score 2, diepte 0) I use the Triumph. But for runs 25km of longer and/or calls for increasing paces, I use the Prime X. It keeps me fresh after runs, which I think facilitates recovery. I'm even considering using it for a marathon I'll be doing soon over the AF1.
[j4kq8st] (score 2, diepte 1 OP) You're the second person that's recommended the prime x and I'm embarrassed that I haven't considered that shoe before, seeing how many Adidas I own. Is there a difference between the prime x and the strung?
[j4krx4w] (score 2, diepte 2) AFAIK, it's only an upper update. But those who've used it say it drastically changed the shoe. However, until I actually get my own pair, I'll take those comments with some reservations.
[j7jc646] (score 2, diepte 4) Hey. Just want to share that I got the Strung at a discount. And boy, are the uppers all they say it to be. It revamped the Prime X IMO.
[j4ljkrx] (score 2, diepte 1 OP) I really like these, but I can't use them for anything close to 10 miles. I'm not sure if it's cause I  weigh more than the average runner, but 6 miles seems to be the sweet distance for me and these shoes.
[j4k7a07] (score 2, diepte 0) NB fuelcell TC for my long runs. Mine have 550km on them now so not sure how much more they can go. Before that was speeds1 might go back to speed 2 or 3 after the TC are dead.
[j4jgbl1] (score 1, diepte 1 OP) I've considered getting the triumph 20, I hear so many good things about them. The only shoes I have with boost are the Adidas nomad and it's a comfortable foam. I really enjoy the new Adidas shoes and think they're doing some great things right now.
[j4jhtnx] (score 1, diepte 0) I'll take the adios pro 3 out on long runs so that's an option for what you already have.  I'll suggest maybe some more cushioned options as well - not sure about what fits well for you in particular but the Asics glideride 3 or the Nimbus 25 that's about to come out may work nicely. Or, I'll second the Triumph 20, and add in the New Balance More V4 which is very comfortable for long easy runs (can feel a bit heavy as the miles add up though).
[j4l4gtu] (score 1, diepte 2) What kind of issues are you asking about? They feel stable once you have a good rhythm going on perfect ground, otherwise ....
[j4l552e] (score 1, diepte 3 OP) Just curious about general stability. I've never run in a shoe with that kind of stack before, so curious about running on uneven terrain and cornering.
[j4l60gf] (score 1, diepte 4) I absolutely LOVE this shoe. And I will only run it on near perfect terrain - concrete or flat asphalt. I live rural and most of my running is done on gravel, sand and dirt roads. Fortunately there's a subdivision with a concrete run path nearby and thats where I run my Prime Xs. They feel sketchy on anything else to me. You do learn to corner in them, slow and careful.
[j4lffzt] (score 1, diepte 3 OP) I'm a fore to mid foot striker as well and haven't had any stability issues in any shoes either, but just curious. I always hear people talk about stability issues with different shoes, but never found them to be much of an issue. But again these are super tall, way taller than my normal shoes
[j7vavzg] (score 1, diepte 1) How are the Zoomfly 5s?
[j7w10kr] (score 1, diepte 2) If you like your Bostons, and have narrow feet, the zoomfly are great.  I understand they are a departure from the other models of zoomfly, but I enjoy them well enough.  To me, they both more or less have the same use case and underfoot feel.

I mostly use mine on the treadmill, and they are far more quiet than my Bostons.
[j7w1wyc] (score 1, diepte 3) I love my Bostons, actually had to retire them after 500K on them that's why I am trying to look for a replacement (I could get the Boston 11s but I wanted to try something new)
[j7w26he] (score 1, diepte 4) I bought 4 pairs of Boston 11s because I love them.  But I think the zoomfly is a worthy follow up to them.

Awful lot of people on this sub don’t like them, but I think most of those people haven’t actually run in them.  If you can get them for under 100 usd I think they’re worth it
[j7w4no0] (score 1, diepte 5) I've only ran in the Boston 10s, what is the difference between the 10 and 11 for you?
[j7x40y8] (score 1, diepte 6) The upper is different,  you’ll either love it or hate it.  It’s more in line with the adios pro 3 where it’s super breathable and somewhat stiff with a more flimsy heel cup.  I liked the 10, but it just didnt transfer as much to race day for me

I use the adios pro 3 as my ideal race shoe for anything longer than a 10k, so the Boston 11 is more or less it’s training partner for me.
[j4jvr4x] (score 1, diepte 0) The more v4. It’s so comfy for like slow runs and very stable. It replaced my invincible and I never looked back
[j4kq2lg] (score 1, diepte 1 OP) I've looked at these before too. There's a running store here that sells new balance, I'll try these out
[j4ktmiw] (score 1, diepte 3 OP) I was just reading up on it when you replied. The way they make the strung upper is pretty wild and sounds like it's definitely something to be experienced. I'd like a pair, but they're awful expensive.
[j7k0jtp] (score 1, diepte 5 OP) Cool thanks for letting me know. I wouldn't mind picking up a pair eventually. I finally ran in my adios pro 3 and they are insane, so if the prime is anything like that then I definitely want a pair
[j4k4qz2] (score 1, diepte 0) Peg 39
[j4kv5pe] (score 1, diepte 0) Novablast 3 for easy pace or endo speed 3 if tempo
[j4kym5w] (score 1, diepte 1 OP) How much different are the novablast 3 from the original? I love them but they wrecked my legs yesterday on 14 miles
[j4n0lvq] (score 1, diepte 2) More stable
[j4n0zs6] (score 1, diepte 3 OP) I've never had an issue with the stability of the novablast 1, I think they just bottomed out after the first 10 miles. I think the 3 does have my stack on the forefoot though, so it might be worth exploring
[j4pjwvs] (score 1, diepte 4) me neither. but it has wider space so more suitable for various runners. same bouncy feeling. i have not had any bottoming out with either version, i weight 85kg. definitely the best easy run shoe at the moment.
[j4pkigr] (score 1, diepte 5 OP) Thanks I appreciate your feedback. I'm not sure if the novablast was bottoming out or not, it didn't feel like it at the time and I've never had an issue on a run with them before, but they wrecked my knees on that long run. I do love the show though, so I'll keep an eye on the 3 for a sale
[j4lslym] (score 1, diepte 0) Also consider the new balance sc trainer  it has replaced the invincible as my favorite long run shoe
[j4m5rye] (score 1, diepte 0) Vomero 16 have served me well as a long run cruiser
[j4mvtq3] (score 1, diepte 0) I think you’re good in the shoe department, dude.
[j4myyd7] (score 1, diepte 1 OP) Yeah I definitely have more than enough shoes, but regardless I need a shoe for my long marathon runs right now. I listed my shoes for input on if any of these would be good for that. My knees are still bothering me from yesterday, so I was hoping for input so I can avoid that again. I'm not actively looking to expand my collection, but I will if I need to find a shoe that works for me. But at the end of the day, the number of shoes I have is my problem alone (I have more that I don't or won't run in anymore too lol)
[j4n7o82] (score 1, diepte 0) As someone who is a similar size (6'4, 210lbs), I've been using the Saucony Endorphin Speed line and they are great. Nice and light with enough cushion for the pushin. I will say they do start to feel flat for me around the 250 mile mark. At least the 1s and 2s do. I have not tried out the 3s but they have a slightly thicker midsole so I'm assuming that would not be the case with those.
[j4nb9b1] (score 1, diepte 1 OP) Thanks. Have you taken them on long runs yet? They are very comfortable and I've heard of people using them for marathons, but not sure how they'd manage the 15 to 20 mile runs for heavier guys
[j4nwe6q] (score 1, diepte 0) Saucony Triumph 20. Don’t feel tired at all after a long one.
[j4lbbbh] (score 0, diepte 5) I ran 22 miles on a hilly, crushed limestone trail with them.

=== THREAD 1r05m08 ===
SUBREDDIT: r/Shoes
DATUM: 2026-02-09  SCORE: 45  REACTIES: 49
TITEL: Is there any option other than frequently buying new shoes/insoles?
POST (source_id=post):
I've tried those scanners thing you stand on at like Walmart to buy specific insoles, but within ~2 months, my shoes typically end up like this and all my socks typically get holes in the same area (these socks aren't brand new, but before i wenr to work they had no holes in them). Do I have any cheaper options?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[o4fsj54] (score 74, diepte 0) The socks are one thing - they look super thin. For the shoes, I’d recommend going to a specialized store that sells walking/running shoes. They’ll have staff that can analyze your gait and even your current shoes. Based on that, hopefully they can recommend a solution. That’s some serious wear for only 2 months!
[o4fsni1] (score 31, diepte 0) Your sock looks pretty low-grade, thin one. Get a quality one. For shoes, if you wear only one pair constantly, try buy two and rotate them.
[o4fvbfv] (score 25, diepte 0) You can visit a podiatrist where custom inserts (created/fitted to the shape of your foot) can be made for you. These inserts are indestructible. And buy better socks.
[o4fz7a7] (score 9, diepte 0) I would guess your gait pattern is probably pretty wonky. You could look into movement modalities like GOATA or functional patterns etc
[o4ft0se] (score 8, diepte 1 OP) These are definitely very thin socks, my usual ones are much thicker white socks and they last longer, I was just tired getting ready for work last night. But even my thicker socks start getting holes in them in similar places as where my soles wear down. But I'll see if I can find any of those stores nearby, wasn't aware there were stores that did that besides the standing scanning.
[o4fy612] (score 6, diepte 1 OP) Thank you, I'll have to see if I can find a podiatrist in my network. Wish I would've looked about a year ago when I had great insurance, now my insurance sucks
[o4fture] (score 5, diepte 1 OP) Yeah I don't typically wear socks this thin especially to work, was just too tired getting ready last night. I'll give the 2 pairs of shoes a try though, I don't have enough to get another pair right now but when I do, I'll definitely try that
[o4gifu5] (score 5, diepte 2) Podiatrist insoles are not like store bought insoles. The insoles are made from a cast of your foot, and may help correct the way you walk.
[o4jo2o6] (score 4, diepte 2) Buy darn tough socks, they replace them for life
[o4g0vy1] (score 4, diepte 2) Please explore a podiatrist, too. A salesperson, even a great one, isn’t going to be able to fix your gait.
[o4g5cgg] (score 4, diepte 1) This is what I was thinking. 

Op needs to check how they are walking. And get better socks and insoles. Like the cushioned plastic ones.
[o4g6wsq] (score 4, diepte 2) I'm wondering if they wear their shoes really loose. Because I do (my feet swell when I'm running), and if I get holes in my socks it's always at the ball of the foot like this. I think the looseness allows more friction.
[o4gnwkw] (score 4, diepte 3) Yeah exactly, I feel like OP’s feet are probably sliding in the shoes, causing them to get worn down
[o4gdfxi] (score 4, diepte 0) Are you rotating a few pairs or wearing the same pair every day? That makes a huge difference in wear, but I agree with others that there’s something about your gait causing this.
[o4gj2dx] (score 3, diepte 3 OP) I'll try to get a podiatrist appointment, though I don't quite understand my copay (looking at my benefit summary now)
[o4gp895] (score 3, diepte 2) Road Runner, a running shoe store, sells custom inserts for maybe $150. No insurance, it's just something they sell. And while they lack medical training, they might have some insight on why shoes don't fit.
[o4fskrt] (score 2, diepte 0) Go to a shoe store where they measure your gait and stance and weight placement they can hook you up. Foot wizards
[o4ftwjo] (score 2, diepte 1 OP) Thank you, I'll have to try to find one near me
[o4gff2b] (score 2, diepte 3) Exactly, salespeople are not drs
[o4k3yvp] (score 2, diepte 4) Heeeey so with regards to insoles, absolutely call your insurance first to verify your coverage. A lot of commercial policies do *not* cover orthotics unless there's some underlying disease or disability (diabetes, clubfeet, etc). Inserts just for comfort/convenience wouldn't fall under that and most plans list these specifically as exclusions. So while the initial appointment with the podiatrist may be covered, the med equipment may be a no go. So definitely call first and check. (Source: literally this is my job )
[o4fyr6o] (score 2, diepte 0) Cheap plastic socks will wear out fast. I know Darn Tough socks have a lifetime warranty with free exchanges if you ever wear them out.
[o4g702e] (score 2, diepte 0) You actually should only be putting 300-500 miles on a pair of shoes if you're doing a lot of walking or running. I did the math and for me that's 3-5 months.
[o4gfdmy] (score 2, diepte 0) I started buying more expensive shoes.. huge game changer. Also, buy better socks.
[o4hgo1z] (score 2, diepte 0) One, please get higher quality socks just in general. And the best long term option is to find a pediatrist to help identify issues with your gate. All insoles with wear out eventually but higher quality ones will last longer, I’ve heard good things about the good feet store if you’ve got one near you but sometimes they well just say ‘idk man, can’t help you’ and I say that from experience.
[o4m6xie] (score 1, diepte 2) Fleet feet has the scanner and can analyze your walk. I was intimidated to go at first because it looks like a store for runners but they were super kind and helpful.
[o4ikkmz] (score 1, diepte 4) We are not! And any respectable salesperson knows better than to overstep (pun not intended) that boundary. It seems almost trivial, but putting someone with undetermined foot issues in the wrong shoe could really hurt them.

Ideally, ask your podiatrist for a list of recommended footwear. Bring it to the shoefitters and they can properly fit  you.
[o4inb6b] (score 1, diepte 4) Some of them are and that’s what I was suggesting.
[o4fz1sd] (score 1, diepte 1 OP) That's perfect thank you, I'll look into getting some pairs. These aren't the usual socks I wear, I usually wear much thicker white ones that last longer but still get similar holes, but I wore the wrong ones today
[o4fzm86] (score 1, diepte 2) Darn Tough are not cheap, so just warning you. They do run sales at different times of the year, which is when I’ll pick up a pair or two, slowly displacing the cheap socks.
[o4fzvke] (score 1, diepte 3 OP) I'll be in the lookout for sales, thank you. Life warranties will be worth it even if I just have a few pairs
[o4g39oq] (score 1, diepte 0) Another vote for custom inserts! I've got a pair and they correct your posture (I think) so you're walking with your weight balanced across your whole foot versus putting your weight on those spots.
[o4g8tdh] (score 1, diepte 0) Smart wool socks are awesome. Wash and air dry.
[o4gc0dg] (score 1, diepte 0) Buy Salomon shoes, and Tommy Hilfiger socks
[o4gdsqk] (score 1, diepte 0) Try smart wool socks. They are worth the cost. They never get sweaty and keep your feet dry. They are thicker but don’t feel scratchy at all like most wool. You definitely need better socks those are atrocious. If you have better socks your shoes will also be spared
[o4gdt5t] (score 1, diepte 0) Maybe your shoes are a little bit too tight.  That looks as if the wear is caused by excess friction.
[o4gfc6i] (score 1, diepte 0) Darn Tough or Smartwool socks. A bit on the pricier side but so worth it! They also warranty their socks, my husband developed a hole in one of his socks and Darn Tough sent him a replacement pair for free!
[o4ggnb0] (score 1, diepte 0) Shoes need a break to rest and dry out. Wearing one pair all day, every day makes them die quickly. I'd get thicker socks and then rotate between 2 or 3 pairs of shoes

Does your foot shift around a lot in the shoe too? Or your feet sweat a ton? You may want to consider getting a professional fitting at a running store so you know what a shoe that fits feels like and then if your feet sweat a ton, getting breathable shoes and moisture wicking socks (or change socks during a break at work)
[o4giyy4] (score 1, diepte 0) If your feet get calluses or are a little rough on the bottoms you could look into getting a pumice stone and/or foot creams. Maybe just something to consider as a last resort if the other advice given like insoles, different socks, changing your gait, etc. aren’t working.
[o4gqrtq] (score 1, diepte 0) Liitle discoloration on the arch makes me think you have high arches.  Wear at the ball suggests low volume to me.  Similar to my feet, then.  Experiment with different lacing patterns to tighten the front end some.

I've got a pair of New Balances I wear for exercise that have high arches.  You might look into something similar.
[o4gxw90] (score 1, diepte 0) You need custom insoles because you have higher arches. Custom insoles would redistribute your weight equally along the foot.
[o4h1i0k] (score 1, diepte 0) What shoe is that
[o4hlq43] (score 1, diepte 0) I think you need thicker quality socks. I buy the brand HEAD socks. You can get them on Amazon.  I had the same problem and changing my socks to a quality pair that costs a bit more made  the difference.
[o4hpc77] (score 1, diepte 0) Not rotating shoes does you no favors. Buying and wearing through one pair every 2months at a time will cost you more than buying 3 pairs and rotating them.
[o4hs35f] (score 1, diepte 0) I use Superfeet insoles for my shoes. Great arch support. I know that REI sells them in store. I would guess that any “outdoors”/camping store would carry them. If there’s a shoe store that specializes in hiking, I would check them out.
[o4i3b5y] (score 1, diepte 0) Do you have sweaty feet?  Try merino wool socks, or other socks that help prevent sweaty feet, and wash your socks in hot water occasionally to kill bacteria if you're washing them cold regularly.
[o4ivyx2] (score 1, diepte 0) You need to see a podiatrist and get custom inserts. It is unfortunately not cheap at all. My pair lasted 5 years, then my podiatrist was able to refurbish them. Also invest in good socks & good supportive shoes
[o4lk48h] (score 1, diepte 0) Are you able to work on your gait/stance at all?

Are you a “toe walker” meaning you put your toes down first and the back of your foot down second?

Do you have very tight/sore calves that make it tricky to stand flat or to raise your toes up?

If so this may be a cheaper way of addressing this.
[o4mk0oc] (score 1, diepte 0) What brand are your shoes?
[o4ngbj3] (score 1, diepte 0) Any chance you live in an area with sandy places?

This seems excessive wear, and very "pointy". Weird

You could try leather insoles, I find them much more resilient than foam ones. They should also lessen the wear on the socks.
[og3eqo8] (score 1, diepte 0) I had a similar issue with shoes wearing out fast and foot discomfort and what helped me most was switching to better structured insoles instead of cheap replacements. I found fp-australia and it helped me get a bit more comfort and support in my everyday shoes.

