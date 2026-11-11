# Label-batch batch_0018

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
Schrijf het resultaat naar `batch_0018.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: ioe28d, ikmndr, xauybp, zi8a87).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD ioe28d ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2020-09-07  SCORE: 6  REACTIES: 28
TITEL: Need a speedwork shoe recommendation!
POST (source_id=post):
Hey all! It's been such a pain trying to find a good speedwork shoe for me, so I'm turning to you guys for my next pair as I've no clue what to try next.

Current daily trainer: Adidas Solarglides 19, amazing fit and great for joy-runs. Doesn't really cut it as a race/speed shoe.

What I've tried and why they were returned:

* Pegasus 37 - Great shoe. Did my fastest paces in these shoes, but they were too narrow and they hurt my feet(and knees) over time. Also the airbags started to feel like little pebbles underneath my feet.

* Solarboosts 19 - way too soft and roomy on the top foot. Too squishy and my foot floated around too much to get a good launch

* Hoka Clifton Edge - Nice shoe, but couldn't see myself catching speed in them. Slightly too narrow and toe box was cramped. I enjoyed the rocker feeling in these as I felt on auto-pilot sometimes, but that also is another reason they didn't cut it for speed shoes.

* Brooks Ghosts - Nope. Just nope. Not a fan of Brooks after trying other pairs as well.

* Ultraboost 18 - Fits my slightly wide foot, but a tad too heavy and I keep hearing that UBs don't make great speed shoes. I do love the boosts on these though, they are even more noticeable than my Solar Glides. These weren't returned, but are my daily walking shoes...they are at the end of their cycle though.

*  Adidas SL20 - Currently on trial. A bit too narrow, stiff, and my foot gets really hot in these(or has hot spots). My heel slips out, but if I do a runner's knot I have heel pain the next day after my run and I think it's due to the stiffness of the show. I kinda miss boost too, I like the launch forward feeling.

I'm hoping I get recommendations to brands that allow to try them and return them if they don't workout.

EDIT: Thanks all! I ordered a pair of the Bondi 2s since their price is enticing, but if they don't work out I have my eyes on Brooks Hyp Tmpo, Saucony Endo Speed, and the Adidas Bostons!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[g4da4j8] (score 14, diepte 0) Brooks Hyperion tempo, Saucony endorphin speed, Nike zoom fly 3
[g4da6i8] (score 10, diepte 0) Hoka rincon
[g4da5eg] (score 6, diepte 0) Saucony Endorphin Speed? Or Kinvara? Kinvara has low stack height, the Speed has the nylon plate and speed roll that is made to pick up the pace. 

I can’t imagine trying to do anything fast in the Edge or any Cliftons, holy hell... if you like the way Hokas feel in the upper and midsole you could try the Rincons, they can do speed work. 

For Brooks, did you try the Hyperion Tempo? Really solid tempo shoe.
[g4dvnn8] (score 5, diepte 0) For wider feet, I would consider the New Balance Fuelcell Rebel as another mentioned. It’s a great speedy shoe thats good for faster paces. Could be a race day option depending on distance. It’s a good rec also thanks to it’s spacious forefeet area which should fit nicely. I would also consider Skechers Razor 3. Light, fast, tad cushioned. Great choice for speed work.
[g4daiud] (score 3, diepte 0) I tried the Adidas Boson 8 for this but it didn’t work for my wider foot. I switched to the Saucony Kinvara 11 (ordered the wide variety) and it’s been great so far for my speedwork
[g4g4d4t] (score 3, diepte 4) I order most of my shoes from Fleet Feet (or by them in store). They have a 60 day, no-questions-asked, refund policy. Even if you've put 100 miles on the shoes, they'll take them back.
[g4doz11] (score 2, diepte 1) Just bought it... It's an amazing shoe for the price 👍
[g4gs7ma] (score 2, diepte 1 OP) This is the one I purchased to try next as the Edges were surprisingly comfortable. I blame the website shoe recommendation questionnaire as whatever I put in told me the Clifton Edges were the best...I should have checked with you guys first.
[g4da9u0] (score 2, diepte 0) If you’re missing boost, then Adidas Boston is your choice. It just took me around 100 miles to break them down, but my foot is a little wide.
[g4gv8wq] (score 2, diepte 1 OP) Prior to the 100 miles, did they feel narrow? I'm wondering if I should just order wide?
[g4gvyx9] (score 2, diepte 2) They’re narrow, it took me some time to pair them with right socks too. For reference, my perfect fit is NB, Nike are ok, but sometimes feel narrow in the middle. We don’t have Adidas wide versions here in Europe, otherwise I would definitely get a second pair in wide. Also I heard that Boston 9 upper is better and doesn’t fit so tight. Hope this will help.
[g4gwqbu] (score 2, diepte 3 OP) It does. I just realized we don't get wide here either for Adidas. Thanks for the input!
[g4dbxr4] (score 2, diepte 1) +1 to Kinvara 11 wide! Great do it all shoe that can pick up the pace when needed.
[g4deo06] (score 2, diepte 1 OP) I wanna try saucony so bad, but I think they have a strict policy on only accepting returns of unworn items?
[g4dmg1s] (score 2, diepte 2) I think runningwarehouse.com has a good return policy?
[g4dp4h8] (score 2, diepte 2) Running warehouse you can definitely return them
[g4d9z8m] (score 1, diepte 0) Rc 2.0 adidas for speed
[g4gsmum] (score 1, diepte 1 OP) I haven't tried the Tempos yet, I tried the Ghosts and Levitates so far. I hated the levitates, they were too big and didn't really add anything to my run. I ordered the Ghosts one size smaller and they were too small haha, but they also didn't do well on a sprint test versus Mizuno Waverunners at the time.

Do you know if Brooks normally run big, or did I just get an odd one with the Levitates? For Saucony, which of the two have better support and some type of energy-return/boost if anything?
[g4gxck5] (score 1, diepte 4) Also, if you’re like Boost bounce you might like Saucony Pwrrun+ foam. It’s a TPU foam as Boost but lighter (what should Adidas do already a long time ago). For a faster day shoe it will be Saucony Freedom. Other mention worthy option is Reebok Run Fast, Reebok is a part of Adidas group and share some similar feelings.
[g4e74g5] (score 1, diepte 3 OP) Thanks for confirming, but they are sold out of Speeds until Nov 12 :(

EDIT: It doesn't seem like their return policy is as great as I had hoped, but better than nothing! From the website:
>To receive an exchange or refund for the full value of your purchase, products must be returned in new, store-bought condition within 90 days from the original invoice date.
Products returned in used or worn condition within 90 days from the original invoice date can be exchanged for another item, or are eligible to receive a store credit for the full value of the purchase. Please note that while we want you to be happy with your purchases, an excessive number of used returns within a twelve-month period may limit your eligibility for exchanges or store credit.
[g4e1pzm] (score 1, diepte 2) I really prefer the Fastwitch over the Kinvaras (honestly I really disliked the Kinvara 10s, felt like running on wood blocks) for speed work. Just got the Hoka Rincons and love them for the easy run I did. Gonna try them out for some speed tomorrow so I'm excited to see how they do. I'll probably get a couple more pairs if they do well.
[g4dnl1f] (score 1, diepte 0) If you still can find a pair of new balance fuelcell rebels, go for it! Otherwise, look no further than the brooks hyperion tempo
[g4dnnqz] (score 1, diepte 0) If you want boost, Boston 8 or 9. Saucony Endorphin Speed is also incredibly popular
[g4e3wes] (score 1, diepte 0) Razor 3 or Reebok run fast. You won't be disappointed.
[g4f37cm] (score 1, diepte 0) Damn bro you return a lot of shoes. The sl20 should be excellent workout shoe for you though. Honestly the endorphin speed is better for long temp/progression run.
[g4gc4gf] (score 1, diepte 1 OP) You're right. I'm not proud of it, but I'm chasing that shoe that I'm excited to put on and go. I usually give them 10-15 miles before I make my decision. The SL20s were supposed to be my final stop as adidas fits me the best usually, but I literally had to stop before 3 miles yesterday because my feet were in so much pain
[g4fidi0] (score 1, diepte 0) I've only ran in Nike but the Zoom Fly 3 is a fast shoe - I actually have to save it for fast runs because it's almost impossible NOT to run fast in it.
[g4k9v1p] (score 1, diepte 0) Saucony freedom 3.  PWRN+ is like boost on roids.

=== THREAD ikmndr ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2020-09-01  SCORE: 1  REACTIES: 28
TITEL: Shoe recommendation for my first Marathon and some long runs until race day
POST (source_id=post):
I just saw a post with a very similar question, didn't post there coz at the end, the question is a bit different.

I need a shoe for my first marathon, I would also use this shoe for some long runs until the race day. At least a 30km and a 35 km long run. so the shoe would have around 100km before race day, is this ok?

My target realistically speaking is to finish under 5 hours, so ill be running slow 6'30/km? 6'50"/km?

Currently, my rotation is a pair of pegs 37 (easy, tempo and long runs) and beacons  2 (tempo and long runs) both shoes are ok but I don't think that I would be able to finish a marathon with any of them. farthest run so far was a half a week ago on the beacons and everything hurt for a week

My first option is endorphin speed.  But, should I go for something more cushioned? 

Vaporfly, alphalfy, endorphine pro, any carbon plated shoe won't make any sense.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[g3lyi2i] (score 5, diepte 0) New Beacon v3 is awesome, I ran 17mi hilly run with a 3mi tempo at the end on Saturday and my legs felt fresh afterwards and absolutely fine the next day. I've got 250mi on my pair and they still feel pretty plush and responsive.
[g3m6opi] (score 5, diepte 0) Why do you think you won't finish with the pegs or beacons?  Do you need more midsole?

The pegs and beacon are in the mid-20's (mm thickness) midsole stack height.

There are a number of good shoes with stack heights in the high 20's to low 30's that won't break the bank:

1. Hoka Rincon:  31 mm, nice / light for long runs and race.
2. Hoka Clifton:  29 mm, little heavier than rincon, but better outsole and will last longer.
3. Asics Novablast:  32mm, similar weight to Clifton, but springier feel than either Hoka.  May not be good for people that need stability.
4. New Balance 1080v10:  30mm
5. Saucony Endorphin Speed:  33mm, lighter than almost all of the above.  Seems like your best bet.
6. Saucony Endorphin Shift:  38mm, but heavier than the speed.

FYI the speed does have a plate (just TPU, not carbon).  This seems like actually the best of the list....based on durability, cushion, and weight.
[g3lp6nd] (score 3, diepte 0) Speeds feel awkward for me at slower paces and I honestly don’t think you really need a pair like that. They’re great, don’t get me wrong. I’ve set 1:27 half split during a workout (2 x 8mi @ marathon pace-ish) and yet I feel like they’re an overkill for me. I’m happy with them, I just don’t think they’re necessary for me. 

Saucony Ride or Triumph would do the job for half the price if you’re lucky to find a sale.
[g3lu8wz] (score 3, diepte 2) Anything slower than 8:30min/mi feels awkward. I have no problem running at that speed otherwise, so it’s definitely shoes for me. 

I have a pair of Cliftons and they do cause me blisters for anything longer than 10 miles.
[g3mifnq] (score 3, diepte 2) >My legs need a bit of help.

How so?  Are they beat up?  Fatigued?

Cushion only really helps if your legs feel beat up from repeated impact.  As you log more miles and longer runs, this will decrease.  Cushion will help not feel beat up and maintain your from at the end of the race.

If your issue is muscle fatigue, then more cushion won't help.  The only that helps that is more miles and longer runs.
[g3mmiwe] (score 3, diepte 4) Increasing mileage, adding cushion, and adding in strength training should help.
[g3lx2gv] (score 2, diepte 3 OP) Lol, that's my tempo pace
[g3lu5eu] (score 2, diepte 0) Saucony Endorphin Speed is a solid shoe.
[g3m578p] (score 2, diepte 1 OP) I have the v2 and I didn’t felt that way after a 22km, but today ran a 10k and felt pretty good pace was about a minute and a half faster than on the 22km though but I can tell that I wouldn’t be able to finish a marathon on that pace
[g3m7ien] (score 2, diepte 2) The new Fresh Foam X in the v3 is alot more plush and responsive than the regular fresh foam in the v2.

Do you have a neutral gait or do you pronate/supinate at all? Beacon doesn't have much support baked in so I can see it beating up your legs after a while if your gait isn't fairly neutral.
[g3mey9n] (score 2, diepte 3 OP) I can’t really tell, I don’t know about a shop in my city with people that know their stuff or the machine that analyze the stride. Most of the workers are young girls with no running experience or fashioned kids with less running experience or old ladies that wanna sell, I mostly buy online, after watching a lot of reviews, asking here...
[g3mh8dg] (score 2, diepte 4) You can look at the sole of a well worn pair of trainers and compare it to a guide like this:

https://treadlabs.com/blogs/insoles-reach-your-stride/34786373-what-are-your-running-shoes-trying-to-tell-you

Most people are fairly neutral or have a tiny bit of either pronation or supination. Some people pronate or supinate to more extreme degrees and need a more supportive/stability trainer.
[g3mlxhx] (score 2, diepte 6) You should be fine in neutral trainers. Im neutral with a hint of supination and have no issues. The Beacons have a drop of 6mm vs 10mm in the Pegs which might be why they beat you up a bit over the longer distance.

If you like the fit of the New Balance it might be worth trying the 1080s. They come high recommended and are an 8mm drop. They are well cushioned and have a rocker design to them to help push you forward without the clunkiness of a plate at lower speeds.
[g3mktpv] (score 2, diepte 3 OP) Yep, beat up. That’s the perfect definition. Especially on my knees even though that I don’t move up a lot, I try to stay as close to,the ground as posible.
[g3mobof] (score 2, diepte 5 OP) I have 2 more months of training, I’m on week 10 of a 19 weeks program. Strength program is where I need to improve, find a better routine that won’t fatigue me more.
[g3mx8ae] (score 2, diepte 0) For a low speed marathon, I'd want whatever the neutral version of the Brooks Adrenaline 20 is.

I can run forever in that shoe at your pace and not feel beat up afterward. Their guide rails only help if you need them, so maybe try them on if you can.

And doing a marathon in a pair of shoes with 100k on them is the right idea.

Good luck.
[g3n99al] (score 2, diepte 0) My favourite shoe is the NB 1080 V10. It can do it all really. Other one to recommend is the Triumph 17 (not the 18) as it is very, very similar to the 18 but is on sale these days.
[g3ssfx6] (score 2, diepte 0) Sounds like you want to get through the run with a goal to finish rather than stress about speed. To be super honest the pegs should be able to get you there. But if you need a more cushioned long run shoe, there are a few that come to mind. I've been doing a bit of reading to try and look at replacing my recovery day shoes eventually, which currently is the brooks glycerin 16. And those shoes are really really comfortable, and at your target pace should provide a really easy ride. Feel free to look at newer versions of that one as an option. I am leaning toward the glycerin 18 as my next recovery + long run shoe (although my other shoes are also fine for long runs) because it adds a slightly wider base and I tend to heel strike.   


Another option might be the Hoka Clifton 7. I have never worn them but the reviews seem pretty favourable, they should be pretty comfortable, not too heavy, and otherwise good for longer runs. But some people have heel issues with the Hoka which has scared me a little.   


For the most part I think strength training but also giving your knees and legs time to rest will help with endurance, because the shoes you have should be totally fine to carry you to the finish, especially if you slow your pace a bit, focus on form, hydrate properly (seriously, drink more water, not just before and during the race, but every day leading up to it from now), and just take it easy. But yes, the Brooks Glycerin 16 (so maybe go try the glycerin 18) has been a really good shoe for me, and a friend ran his first 100k in them, so it can be done.   


Also you can easily run a marathon in shoes that have 200, 300, 400kms done in them, and it's a good idea to go on some longer easy runs (although maybe not 35kms, maybe just go for a couple of 20-25k runs) in them to get used to the feel etc.
[g3lsb8x] (score 1, diepte 1 OP) What's for you slower paces?

I looked into the Triumph 18 but they are about the same price as the speed, maybe 10 euros cheaper, also heard that are too heavy for long runs. 

Maybe cliftons?
[g3mj8a8] (score 1, diepte 5 OP) Looking my running shoes I’m neutral, but I do have an old pair that I used to walk and it looks like neutral with a tiny supination. But most of my shoes are worm in the center and mostly in the front
[g3me20a] (score 1, diepte 1 OP) I think so, they are maybe not cushioned enough? My legs need a bit of help.

Out of the list I have considered all but the rimcon, I had the tempo next% on the list too but at the end  my final list was speed, shift and 1080v10 and because of the weight the speed was the winner.

Thanks
[g3mpa4j] (score 1, diepte 0 OP) To be honest I liked the speed and the shift, 1080s as the last resort in case I couldn’t find the endorphins here. But It looks like a solid option.
[g3ohlsm] (score 1, diepte 1 OP) Thanks
[g3p6t0h] (score 1, diepte 1 OP) What’s the difference between the 1080v10 and the 1080v10 London edition? Among all my options the 1080 is the only one recommended for slow paces.
[g3p7swl] (score 1, diepte 2) The colour. They are the same shoe but just different colours. They are good for slow paces yes, but you can easily pick the pace up in them as while they are cushioned, they are probably the most firm, cushioned shoe if that makes sense. Definitely not firm, just firmer than the usual options like a Clifton or Triumph
[g3p86zl] (score 1, diepte 3 OP) That’s what I though, thanks.

Found a reviews site with some weird categorization. One of the categories is pace, the 1080 says:  > 5:30 min/km, 4:30-5:30 min/km, With the triumph 18 it only says 4:30-5:30 min/km. Speeds says < 4:30 min/km. I don’t know it’s probably all bs. They tag the speed as a short max 10k speed shoe.
[g3ojstc] (score 1, diepte 0 OP) Oooh boy, triumphs have entered the list to make everything more complicated.

Final list so far 

1. Endorphin Speed. If I was faster there would be no doubts and this would the winner

2. Endorphin shift. I like the high stack, doubting because of the weight and if it’s cushioned enough, 4mm drop maybe is too low?

3. Triumph 18 or 17, about the same price here. Doubting coz the weight. 

4. 1080v10, cheaper for them. Last resort.
[g3t3mun] (score 1, diepte 1 OP) When I decided to sign up I thought that a sub 4hr was doable taking my 5k as reference, after 4 weeks of training I was like sub 4hr is imposible but 4:15-4:30 is doable. Time passed, few weeks ago I was like let’s be real, 4:30-sub5:00 would be a great achievement. These days after snooping some people strava and talking with some guys my expectations are really low, finishing would be great, sub5hr would be even better but been honest with my self in order to finish ( time limit is 7 hr) I still have to work a lot. Specially the no running part, strengthening, stretching and foam rolling are my weak points, last week I hurt my self during a foam roll + stretching session and missed last long run to recover. 

I’m on week 10, until now everything felt good and doable but long runs are getting too long, all remaining are above 27k, 2 30k and 1 35k. Also had my first HM and ended too beaten up, maybe coz I used the beacon instead of the pegs, but I had run 2 times 19.5 km before and didn’t feel that bad, I shouldn’t felt that way because of an extra 2k? Basically this is why guessed that I need something new for race day and long runs,  if the beacons belted up was a 9 on a scale of 10, and pegs is normally a 7, maybe something more suited for long runs would be a 5?

Thanks for you comment and tips i will look into the glycerin ofc, as you can see nothing is under control :)

Btw looks like the marathon is gonna be cancelled, but, next November 8th I’m running 42.2k even if I have to circle my block coz of a new lockdown.

=== THREAD xauybp ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-09-10  SCORE: 6  REACTIES: 28
TITEL: Any opinions on running shoes for my first marathon?
POST (source_id=post):
4 weeks out from 1st marathon!

I've run a half before, in my trusty Infinity React (1.0) - loved 'em. I own a pair of Pegasus 38 but my running start was from a pair of Asics GT-2000. I've liked all of them enough, with my least favourite being the Pegs. 

5'10 - about 185lbs. Currently running at 5:20-5:30/Km on a half marathon pace - "slow"/LSD pace is 6:00/km and I can plod along at that pace for about 28-33KM with no issue in the Infinity React. Knees tend to hurt towards the end of the day on longer runs and some paced-up runs (5:00-5:05/KM), but otherwise, just a bit of hip tightness. 

Papa needs a new pair of shoes. Firstly, as a gift to myself and secondly, something that I feel comfortable training in until Oct. 9th where they will be put to the real test. Money isn't really an issue, so any suggestions helpful. I've been eyeing the following:

\- Infinity React 3.0

\- New Balance 1080v12

\- Vaporfly Next%

\- Zoom Tempo Next%

\- ???????

If anyone needs more stats, let me know!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[inw5fi9] (score 24, diepte 0) Wear what you’ve been doing your long runs in. 

You don’t need special shoes for your first.
[inwbao3] (score 24, diepte 2) There is an old saying, nothing new on race day!  I’d say get a new pair of the shoes you do long runs in, and break those in during the weeks leading to the race.
[inwbnz6] (score 12, diepte 0) I wouldn't change what I'm used to a month before race day. If I were you, I'd get the same pair you have now (or something similar), get them soon and run all my remaining runs on them. Don't worry too much about performance on your first marathon.
[inw55ef] (score 5, diepte 2) I am not Elite. For the half I'm running tomorrow, I'm targeting around roughly your time, and I'm wearing my Vaporflys.  They are a dream to run in and your legs will thank you later.  I have not regretted the purchase at all.
[inxnuta] (score 5, diepte 1) I personally think this is bad advice for someone who doesn’t have experience running in unstable shoes, even the endo speed 3 is a lot more unstable than something like the 1080v12. You’re right that a marathon is a long race, why would a first timer run it in an unstable race shoe?
[invu3l6] (score 4, diepte 0) Saucony Endorphin Speed 2 would get my vote. Nice pop from the nylon plate but not too rigid like a carbon fiber plate can be. The speedroll technology is nice. The midsole foam is superb. They were recently on sale for a fairly steep discount since the Speed 3 entered the market. I have a pair of Next %2 as well, but I think the endorphin speed is a better option given your time frame and pacing.
[inw2j7f] (score 4, diepte 0) Vaporfly.  If money isn’t an issue why wouldn’t you go with the premier Marathon shoe.  I love mine.  I wear my old pair on tempo days now, so it’s not like a one and done situation either.
[invsxw0] (score 3, diepte 0) I'm in the same boat. around 185 lbs and running 5:30 marathon pace.
I'm looking at the Endorphin pro 3 first. But having to convince my wife I want 250 euro schoes rather then 100 euro shoes will be a huge task.
otherwise I'm looking at discounted Vaporfly or Alphafly's.
[inw1tdy] (score 3, diepte 0) New balance RC elite v2, ain’t gonna make you faster but your legs will thank you
[inwsq5j] (score 3, diepte 3) This👆👆
[inwp94i] (score 3, diepte 0) If money is not an issue, I would go for a shoe with «superfoam». Marathon is looong and your feet will thank you. They are not just for the elites, studies show that non-elites can benefit even more from supershoes. Nike Vaporfly or Alphafly, Saucony Endorphin Pro 3, Adidas Adios Pro 3 (or 2), Asics Metaspeed Sky+, NB Fuelcell Elite v2, Saucony Endorphin Speed 3 etc.
[invtwsj] (score 2, diepte 1 OP) What are you running in now? How are your feet/how is your stride in terms of foot movement?
[inw2uld] (score 2, diepte 1 OP) I’m more worried about them being targeted towards elite runners (very much not me). 

I love the idea, big Nike guy and they’re the ones I’ve been eyeing. I’d be so concerned about buying them and having expensive, but good looking shoe-rack tenants lol
[inw3wb6] (score 2, diepte 2) Yea, reasonable concern, but I’d still try em.  I have found they still feel really nice around that pace and it’s easy to pick it up a bit…they want to go fast.  My 2 cents
[inw43zs] (score 2, diepte 2) You'd have to adjust to the narrow midfoot on the sole of the Vapes. I don't recommend this so close to the race. The Pro 2s have had great discounts, as the Speed 2s, as another person recommended. Ideally you would have jumped at the shoe change a bit earlier but you'll be fine. Have fun!
[inw75k3] (score 2, diepte 1 OP) I guess I should have mentioned the Infinity are starting to reach end of life. Since I need to buy a new pair, I figured I would check if there's something out there I should check out more seriously than just going with what I know.
[invu6oe] (score 1, diepte 2) now I'm running in puma Deviate nitro v1 with around 300km on them.
No idea about stride, I just put on my shoes and go running. Sorry I can't be more specific.
[invue4c] (score 1, diepte 3 OP) Sometimes you just gotta do the thing and not think about it!!

I've only recently started looking into my stride and that type of stuff in hopes of slight improvements.
[inwfro7] (score 1, diepte 1) Second this one. If you’re getting at your first marathon you can’t go wrong with these. The pop is nice. I have the Nike AlphaFly 1’s and your pace seems more suited for the Saucony Speed 2’s. Best of luck!
[inw2841] (score 1, diepte 0) Is there a running store near you where you can try out a few pairs? If so I highly recommend that. Tell them the shoes you've liked, what you're looking for and what you're considering and they should be able to help you try a bunch of shoes on.
[inw2kww] (score 1, diepte 1 OP) There is but they’re so crazy out of stock at all their locations it’s insane!! 

Size 10 is popular apparently.
[inw2xld] (score 1, diepte 0) If you’re still planning to do all your training runs in the next shoe you get, I’d hesitate to get a plated shoe. Of the ones you’ve listed, the 1080 seems solid. You’ll be able to keep your legs healthy on your training runs, keep your injury risk low, and it should more than last through your marathon. You could try and get 2 shoes on sale tho, like a daily trainer in an older version of the 1080, then try to grab an older version of a speedier shoe with a plate for race day on sale too.
[inw4017] (score 1, diepte 1 OP) Thanks for the input. Really good insight about 2 pairs - I thought about that too, because I’ve heard rave reviews of the 1080s, and plated shoes. Nike almost always has a sale on a Next% shoe from previous gens
[inwgrfv] (score 1, diepte 0) I'd probably try the new endorphin pro 3. Everyone raves about them. But 1 month out is risky. If you buy a new shoe make sure it works on a long run before the actual race.
[inwzddz] (score 1, diepte 0) Vaporflies. There's plenty of deals online rn or you might get lucky at a Nike outlet. But make sure you run in them a few times before your marathon to get used to how they feel, etc. You could easily do a marathon in Endo Speed 3's or Pros 3's (softer than it's predecessors apparently), too.
[inx5tig] (score 1, diepte 0) Go with what you know, for my 1st marathon I did my long training runs in hoka carbon x2's, about 3 weeks before the race I bought a 2nd pair and broke them in on my intermediate runs. They worked perfectly. I've got another marathon on October 8th and I'm doing the same exact thing but this time with Altra Vanish Carbons
[inzntg6] (score 1, diepte 0) Alphafly. Just put a couple of runs in them before the marathon.
[ix5rbhs] (score 1, diepte 0) Try the New Balance Fresh Foam 1080 V11. In fact, if you want to run for a long time, it's a good idea to train with cushioned shoes. Save your light, minimalist shoes for races. I had been using XXXX Cumulus as a trainer, but these 1080s do a better job of absorbing impact than those. The only reason I took away one star is because the heel design has an underpronation pitch when you stand up. No big deal for people who land on their forefoot and don't use much heel. If it bothers you, it's easy to fix with heel inserts. Most runners overpronate, so shoe makers build some underpronation into their shoes. The middle sole is neutral and has a lot of padding.

https://office-turn.com/trep?depo=B08BNDN74W

=== THREAD zi8a87 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-12-11  SCORE: 20  REACTIES: 28
TITEL: Have any other pronators found that stability shoes make things worse?
POST (source_id=post):
That’s been my experience so far… I used to run in Nike Vomero 14’s but they got old and I started experiencing a slight twinge behind my medial malleolus so me, being the paranoid freak that I am, immediately started searching stability shoes since I know I pronate and that maybe that’s why my ankle was starting to hurt. 

I settled on a pair of Brooks Adrenaline GTS and found that my ankle pain has gotten even worse these past few months… I’m talking I can barely run two miles without developing pain. 

Yesterday I went to the store to buy a new pair and decided to try the Brooks Ghost 15’s and wow, I was able to run over four miles relatively pain free!! I am seeing a physical therapist and dealing with my tendinitis as it is but it looks like the shoes that were supposed to help me based on “science”* really just… made things worse. Has anyone else experienced this?? I’m so pumped about being able to really run again.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[izq4asp] (score 20, diepte 0) My primary issue is when there's an overly aggressive arch.  I think I personally prefer (with limited sample size) shoes that are neutral but are inherently stable, but not necessarily a stability shoes.  In any case, having variety in your rotation is probably good, unless you know for sure your body mechanics work with only certain platforms.
[izq4dcp] (score 13, diepte 0) Wear shoes that are comfortable not ones that claim to reduce injury via changing your gait. It's just marketing bollox.
[izq7j58] (score 11, diepte 2) Saucony Endorphin Shift is a stable neutral shoe.
[izq6wet] (score 8, diepte 0) Doctors of Running recently posted about the benefits of neutral stable shoes.
[izq81cc] (score 8, diepte 0) Yes. They should only be prescribed by doctors. I ran in Nike Frees just fine for five years(I didn’t know they were minimalist-it’s what ALL of my friends wore in 2012). Then my dad got me a pair of Wave Inspires in 2016 as a gift. I didn’t know anything about pronation. All he told me was that the guy at Dicks said they have the most “support.” I was skeptical, mostly because they were butt ass ugly Optimus Prime looking bloated fuckers, but I tried them out and they were ridiculously comfortable. Took those things like 1000 miles over the next two years. 

My next shoe was a Brooks Ghost. Started getting pain and finally learned about pronation. Turns out I was supinating hardcore and I have a high arch rigid foot. Over two years in Wave Inspires, I had subconsciously conditioned myself to land on the outside edge because the super medial arch ever so slightly disrupted my gait forcing me to take the easiest path(to the lateral side). Three years after switching back to neutral and literally dozens of different models later, I still struggle to find a shoe that is flexible enough to pronate properly. I’ve developed a BONE SPUR on my right arch on the big toe bone. 

The only shoes I can run in when it acts up are the NB Rebel V2. Love me a shoe with zero arch support and soft foam. Fuck motion control. Fuck stability. Feet are meant to walk unimpeded dang it! I’m biased as hell though obviously lol
[izq6gl9] (score 5, diepte 2) The only one I can personally talk about is the new balance SC Trainer.  Not a stability shoe, but because of the way it's designed, it helps keep the foot in a stable(ish) position (for me anyway). I cycle this with a set of Hoka Arahi 6, which is a light-stability cushy shoe.  

Here's a video talking more about neutral stable shoes. https://youtu.be/yF6-Rf22iPU

It's all subjective, though.  Just got to find what works for you.
[izq58nw] (score 5, diepte 0) I ran for years in Brooks adrenaline because that's what the running store guy said I needed because he saw me overpronate.  I had ongoing issues for years which I thought was just part of running, until I gave up on them when they ruined the shoe with the adrenaline GTS 8, and I found some killer sale on Nike pegasus in my size and just bought them on a whim.  I was actually going to buy inserts for them or something, but just tried them stock and I instantly realized that I had been running in the wrong shoe all along.  Since then I wear nothing but neutral shoes and I haven't had a single issue -- and I'm a huge guy and run high mileage and do stupid shit.

I can't do low drop shoes though.  Even the Saucony standard trainers at 8mm aren't great for me.
[izq4p8w] (score 4, diepte 1 OP) What “stable” neutral shoes do you have in mind? I wanted to try the Hoka Clifton’s but they didn’t have my size in the store but the ones I tried on did feel even more secure than the ghosts if I’m being honest… although that could’ve also just been because they were a half size too small and run a bit narrower lol
[izrceb0] (score 4, diepte 0) Completely. For some people, a very minimalist shoe-- once you adjust to it-- that gives you great contact with the ground can actually really help pronation. This is what worked just for me personally.
[izr21rl] (score 3, diepte 2) The Hoka mach 5 is incredibly stable if you're looking for something that can pick up the pace as well.
[izq4hgp] (score 3, diepte 1 OP) I’ve learned my lesson haha. Don’t fix it if it ain’t broke
[izq8l3u] (score 3, diepte 0) Yes with my asics gt now I brought the endorphins which is the complete opposite to stability shoes and I haven’t had a issue since
[izq7859] (score 2, diepte 3 OP) Absolutely, thanks though! I’ve only been hearing about ghosts and Clifton’s and wasn’t sure what else is out there
[izqbe4a] (score 2, diepte 2) I used to only run in “stability” shoes (eg Hoka Arahi). Eventually tried Hoka carbon X and haven’t looked back. Better performance and no knee/shin issues. Added saucony speeds to my rotation this year. 

I did work on being more forefoot/mid strike which has also helped
[izqrmsk] (score 2, diepte 2) New Balance Fresh Foam v4 is the best neutral stable shoe I’ve found (second to the Endorphin Shift)
[j6d6rdr] (score 2, diepte 1) Asics GT2000 are the worst offenders for that. Tried them a few times and they always tore my arches to bits
[izq8sgf] (score 2, diepte 1 OP) Oh my god you just brought me back to my high school days😭 I don’t remember which ASICS I had but they were STIFF and I had horrible shin splints every time I wore them
[izq9315] (score 2, diepte 2) Horrible ride with them too 🤣 no energy return they did the job tho but it did cause ankle pain and stiffness
[izsa2x7] (score 2, diepte 0) Yes and no. What I found is that overpronation is often times a symptom of something more generally wrong with form. I've had much more success addressing my form in a holistic sense rather than slapping a stability shoe band aid on my feet.

The thing that has helped me the most by FAR with all of my joints, every little twinge, and just overall comfort level while running is: building strength. 

If you have stronger muscles up the chain to deal with the impact forces then your joints and tendons don't have to do as much of the work. This also keeps your body in better alignment so that forces aren't being applied on your joints at sub-optimal angles. (A professional can probably phrase that better than I did but I hope you get what I'm saying.)
[izu99jf] (score 2, diepte 1 OP) I used to be a weightlifter and now do CrossFit so I’m not worried about my general strength, haha. I’m not jacked or anything either. My legs are super curved so looking at them in a mirror I’m not surprised that my ankles are angled the way they are 😭 

But I do see your point and I see a lot of running pages have been starting to emphasize cross training a few times a week for that reason!
[izr27mp] (score 1, diepte 2) My situation is very similar to emptythevoid. I have a pretty bad case of flat feet and overpronation on my left and the wrong shoes will cause pain for any longer running sessions. 

I find neutral shoes with wider platform help a lot for my stability needs. The most recent examples that work best for me have been the Hoka Mach 5 and NB SC Trainer. I recently got the Novablast 3 but it hasn't been working out so far because the midfoot is not wide enough, will probably return them.
[j09o6cu] (score 1, diepte 2) I wouldn’t say the Clifton’s are inherently stable. I put around 170 miles on the 7’s and had to retire them after that. It may be different with newer models, but the midsole was pretty narrow. I enjoyed them as a daily trainer, but my right foot over pronates more than my left and, over time, the eva foam couldn’t hold up to it. The foam on the inside of my right shoe ended up collapsing faster than the foam on the outside, to the point where my shoes were uneven and running in them left blisters all through the inside of my right foot.
[izqr02t] (score 1, diepte 1) Do you use any other trainers? I'm 100kg and do about 50km/week. After doing this for 4 months I've started to experience pain in my midfoot and calf, deeper in the leg than muscle pain. I have found the invincible 2 to be really good for cushioning and protection. Also have Kayano 29, which, like OP has stated, often causes me pain. Have the 1080 V12, which isn't cushioned enough but very versatile; and my favourite runner is the endorphin shift.
[izrqqsu] (score 1, diepte 2) I usually get whatever neutral shoe I can find on sale, heh.  I'll wait until I see something decent for under $60 bucks and buy like a dozen pairs of them.

Right now I'm on Saucony Ride but I put heel lifts in them.
[izqhrw8] (score 1, diepte 1 OP) It’s been four months 💀💀
[izrch10] (score 1, diepte 1) Fellow Nike Free runner here! This is my daily shoe, would literally wear nothing else if they made a more winter friendly upper version.
[izs734k] (score 1, diepte 2) You'd be very cold!
[izva9wi] (score 1, diepte 2) Nice! Well I'm glad strength isn't the issue for you. Hope you are able to find some shoes that work.
[j6d6ncy] (score 1, diepte 0) I ran in "support" shoes for years without issue, but when I started getting back into proper running, I started getting aches and pains after long runs. I asked a podiatrist for advice and she said it's all about comfort, and stability/support shoes are shit. Running in Adidas Bostons for distance/speed and am relatively pain free.
[izq7jq8] (score 0, diepte 0) Yes— but even with orthotics/insoles, they help in the long term but for the first few weeks, they really hurt. It takes time to correct imbalances but it’s worth it

