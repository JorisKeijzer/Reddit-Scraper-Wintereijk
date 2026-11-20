# Label-batch batch_0092

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
Schrijf het resultaat naar `batch_0092.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 4ang7b, 1u97zro, yrkknr).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 4ang7b ===
SUBREDDIT: r/AdvancedRunning
DATUM: 2016-03-16  SCORE: 36  REACTIES: 218
TITEL: Winter of /u/YourShoesUntied - March 16 2016
POST (source_id=post):
Hello everyone! This week, /u/yourshoesuntied laces up and answers some Qs. Like always, feel free to share your latest training, ask any questions you might have, or just participate in the general discussion.

* ARTC jerseys. If you missed out we'll do another one for the fall. 

* [Fill out the 2016 race sheet if you plan on racing anything at all](https://docs.google.com/spreadsheets/d/1692ovX8uCJKcZEBdsHSQY85PP8J3RoJ4xyu-QHwHUYg/edit#gid=0)!

_______________________________________

**How/when did you start running?**

> In April of 2012 I picked up running as a way to cope with a long-term relationship that ended suddenly and to lose all the weight I had put on after neglecting myself for years. I found myself weighing over 260 lbs, heavy smoker, chewed tobacco, very heavy drinker, and used a lot of different drugs. It was a pretty dark time in my life. I used to be very athletic in high school (wrestler & bodybuilding) but I let it all go to hell for another person and I decided to get my shit together again. After deciding to start up running because it was a cheap (yeah right!) option, I entered my first 5k with a friend and finished around 37:xx. Having a highly addictive personality I was hooked instantly. Once is never enough and over the last four years it's grown into who I am.

**PRs?**

* 1 mile - 5:55

* 5k - 21:55 (it's been a few years)

* 10k - 47:33

* Half - 1h:41m:15s

* Marathon - 3h:55m:xx's (total guess based on my ultra paces I've never officially done a full)

* 50k - sub 5h:00m:xx (unofficial)

* 50 Mile - 9h:59m:07s

**Favorite shoes to train or race in?**

> I've fallen in love with the ASICS Kayano line. I'm on my 4th pair in the last year. Currently I'm trying out NewBalance 860v5's. Still not sure about those yet.

**Favorite weather to train or race in?**

> Give me a sunny 50F day, slight breeze, and I'll run any time, any where, any distance.

**Next Race?**

> Next race is the Yamacraw 55k in Sterns, Kentucky on April 9th. I've got a 24 hour race in Black Mountain, North Carolina, May 21st where I'm going to attempt 102.3 miles. Then a 100k in June. A few more shorter ultras each month leading up to my official 100 miler at Tunnel Hill in Vienna, Illinois in November.

**Goals this year?**

> Too many!

> 'A' goal is to go sub-20 hours at my 100 miler in November. I've got a pacer who is capable of sub 17 hour 100 milers so I'm really hoping he can get me through it in one piece and on time.

> 'B' Goal is to place in the top 10 at a large ultra. I'm a chronic mid-pack ultra runner and last year was the first year I started seeing myself finish in the top 25% range of races so I know I'm capable of doing better.

> 'C' Goal is to maintain my run streak. I started back in December of 2014 and I just passed my 460 day milestone so I'm really looking forward to see how long I can keep it going.

> 'D' Goal is to put in a 111 mile week (more than likely the week of my 100 miler). It's not that important but I'd just like to see it happen.

**Proudest Accomplishment?**

> I'm pretty proud of a lot of the things I've done when it comes to my running but the moment that stands out the most is last April when I finished the Yamacraw 55k. I had just made the cutoff by ~10 minutes and it was terrifying racing the clock. The thing that makes me proud isn't really the dismal time I finished with but was the fact that I finished at all. The race had a ~50% DNF/dropout rate because more than half of the people who started couldn't physically finish. The RD said it was a good course for first timers so I hopped in expecting it to be cake. It was all a lie. It was nothing but ~35 miles of mud and climbing and water crossings. They even ferried us in a boat at one point. I'm a dry, flat lander and at that point had never climbed anything taller than a 50' hill. Going up the side of mountains was shear torture. I willed my way through that race on adrenaline and fear and came out alive. Finishing a large ultra that tough, with that many people dropping out really lit a spark in me and showed me that never giving up really does pay off. Proudest moment...crossing the Yamacraw 55k finish line.

**Things you do outside of running?**

> I'm a homebody when I'm not running. I love spending time with the gf and our 6 y/o daughter. There's never a dull moment. I'm one of those people who has to constantly have some sort of project going. I'm not good at sitting idle. I love doing yard work like cutting the grass, landscaping, trimming hedges, etc. I'm also a house flipper and love doing maintenance/contracting work on properties when I get the chance. I am an architectural & structural draftsman by trade so drawing things all day allows me to have the knowledge to fix things in real life. There's something satisfying when you get done with a home you've remodeled or a landscaping project.
Recently got into bike commuting after fixing up an old road bike that I found in a dumpster. It's been a side hobby to customize it bit by bit and make it unique. Plus it's been a nice addition to my running when I need a bit of cross training. ...That's probably enough for now.

**Things that interest you outside of running?**

> I love reading but I'm horrendously slow at it. I really get into two different types of books: Zombie/apocalypse themed books and ultra distance running books. Go figure. I've got a nice library growing with both themes but it's taken me years to get to this point. I also am interested in drawing. It's something I've been good at my entire life and I don't have a lot of time anymore to sit down and dedicate my nights to my art but I'll get back to it someday. I've been dabbling with the idea of doing coding and stuff like that. The thought of knowing how to do it a little seems fun but I'm intimidated by it for some reason. I'd love to be able to tweek programs and alter things like subreddits to make them function better but, again, learning to do it takes time and I'm a bit intimidated by the process.

**Favorite subreddits?**

> I spend 99% of my time over in /r/running but I'm making an effort to get around to ALL of the running subs more often. Other than running subs, I pretty much lurk around over in /r/bikeporn, /r/bicycling, /r/CatsStandingUp, /r/fittofat (to make myself feel better), /r/holdmyfries, /r/goatparkour, /r/penmanshipporn, /r/reallifedoodles and the great /r/trashy. I like to spend my lurk time being entertained.

**Origin of your username?**

> I wanted to have a username that was easily recognizable and fit in with the general theme of the subs I frequented. Nothing too creative or mysterious, I just thought it would be funny to tell people my username in real life and after hearing me say it, they'd look down at their feet.

______________________________________________

**Race Report Recap**

* /u/warmupwarrior ran a [23 second PR in the 3200](https://www.reddit.com/r/AdvancedRunning/comments/4a8qor/general_discussion/d0yb8mn)

* /u/cross1212 and /u/itsjustzach brought [home the money in the 10k/5k races in Northeast Ohio.](https://www.reddit.com/r/AdvancedRunning/comments/4ad4b5/workout_of_the_week_the_ice_cream_sandwich/d0zbx3b) and here is /u/itsjustzach 's [write up](https://www.reddit.com/r/AdvancedRunning/comments/4ad4b5/workout_of_the_week_the_ice_cream_sandwich/d0zwe99).

* /u/ProudPatriot07 was [third overall female in her trail 5k.](https://www.reddit.com/r/AdvancedRunning/comments/4a8qor/general_discussion/d0yh2kk)

* /u/bwalkernc set [a 10k PR](https://www.reddit.com/r/AdvancedRunning/comments/4ad4b5/workout_of_the_week_the_ice_cream_sandwich/d0zcpjh)

* /u/Spectralblr ran [a 10k as well.](https://www.reddit.com/r/AdvancedRunning/comments/4ad4b5/workout_of_the_week_the_ice_cream_sandwich/d0zbizj)

* /u/RunRoarDinosaur ran [a marathon.](https://www.reddit.com/r/AdvancedRunning/comments/4ad4b5/workout_of_the_week_the_ice_cream_sandwich/d0zd3gw)

* futureman_pm ran [the Shamrock 5k](https://www.reddit.com/r/AdvancedRunning/comments/4ad4b5/workout_of_the_week_the_ice_cream_sandwich/d0zccag). 

* /u/VincentClortho ran a [muddy trail 5k.](https://www.reddit.com/r/AdvancedRunning/comments/4ad4b5/workout_of_the_week_the_ice_cream_sandwich/d0zwe99)

______________________________________________

**General Questions:**

1. Fast [5k/10k](https://www.reddit.com/r/AdvancedRunning/comments/49z8la/list_of_the_fastest_5k_and_10k_road_races_in/) races and [Marathons](https://www.reddit.com/r/AdvancedRunning/comments/4afnjr/are_there_any_fast_latemayjune_marathons/). What is the biggest or fastest race in your area? Have you participated? Why or why not?

2. Pick one of two running conditions: Running in the morning and finishing just before sunrise or running in the evening and starting at sunset.

3. Have you ever run back to back races? [Ed Ches has quite a few times.](https://www.reddit.com/r/AdvancedRunning/comments/4a4itz/one_guy_cant_anchor_a_dmr_35_minutes_after/) What distances do you think would be the best to run back to back? Which would you struggle with the most?

4. [What is your favorite warm weather treat?](https://www.reddit.com/r/AdvancedRunning/comments/4ad4b5/workout_of_the_week_the_ice_cream_sandwich/) It can be a food or a drink.

5. Anything else you'd like to add?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d11uv5q] (score 12, diepte 0) SHOES!!! Thank you for being crazy.

1. So many big races here. I did two of the premier events last year, Cherry Blossom and MCM.

2. Finishing around sunrise is definitely better. Getting to see the sun come up and see the lights reflected in the Potomac in the morning is great.

3. I did a 5k/10k double. It was pretty fun, but I think I'd rather have the 10k first. I think budgeting my running energy would be a little easier if I got the longer race out of the way first.

4. One of my new guilty pleasures is Flying Dog Dead Rise Ale. It's a pretty light summer ale with Old Bay added. If that sounds disgusting, it's really not.

5. [I get to run with Meb!!!](http://www.endurancesportswire.com/meb-keflezighi-commits-to-2016-credit-union-cherry-blossom-ten-mile-run/) And to think, I almost didn't sign up this year, but I got a free entry through work.
[d11xwb5] (score 9, diepte 0) Another ultra dude.  It's very interesting actually to read or hear about how many people have come into running ultras from "very dark times" and/or addictive lifestyles.  Good luck with preparations this year for your (first?) 100. Looks like a good course for sub-20.
[d11ztwg] (score 9, diepte 0) Nice, u/yourshoesuntied you are inspirational, and I also am obsessed with Asics Kayano!

1. New Bedford Half Marathon, and Falmouth Road Race are the biggest closest races.  I have never run them.  Falmouth is at like 9 or 10am in the middle of the summer which is just the stupidest planning ever and I refuse to do that. I might run the New Bedford half (it's this Sunday) but that's only because there's a bib available for me to use (I'd remove the chip) since I'm not prepared to run my best. Next year I'd hope to run 86 or better....
2. Morning based on the effect it has on the rest of my day, but there's nothing quite like running at night!
3. Yes in college obviously.  There were a handful of times where I raced 3 times in one day.  A few where one race was the night before and another race (or two) was the next day.  I found same day more doable/easier than back to back days, because I always kind of felt weird, like my legs were in the middle of recovery from that night's sleep or something and they weren't ready for that rude awakening...
My best triples were: Conference - 5:13 mile (2nd place) 1:39 600m (3rd) anchor 4x800 2:21 split (1st and I missed our conference record by .01.  Totally my fault because I can run much faster and was lapping everyone...but no one told me the record/we were close/etc)  We didn't know until an official was like hey, look at this and I was just like faaaaaaaack. (9:47 was our overall which wasn't our best) 
Next was our home meet the year prior, 4:56 in 1500m (win) 2:19 in 800m (win plus broke 34 year old school record) then anchored or 4x400 because long story some brat left and we were going to scratch and I said hell no, not at our own meet, so wore trainers and ran a 71 LOL split and because of those points, [we won our first ever track meet.](http://www.corsairathletics.com/sports/w-track/recaps/040911aaa.html) yes that's me in the picture SORRY FOR THE LONG STORIES but I have my first track workout since march of last year tonight and I am soooo pumped and feeling nostalgic. 
4. Chocolate milk, iced tea, iced coffee, grapefruit juice (esp in pop form) I crave all of these during summer long runs interchangeably.
5. I think I've written enough XD
[d1220lo] (score 8, diepte 3) This makes me feel warm and fuzzy inside. I'd say if people judge their own sanity by wearing a WWSD (What Would Shoes Do) bracelet, I've done something right with my life.
[d11vzg9] (score 8, diepte 0) /u/YourShoesUntied, I'm jealous of all the ultras. I've done one but can't decide on doing more or focus on shorter events.

1. Fastest races in my area are all in the 5k/10k range (unless you count Gate River 15k a few hours to the north), and they're all put on the by same running store. I've done quite a few but I think this next season (starting in the fall) I'm going to try and race all of them.

2. Running in the morning every time. With the time change I'm now finishing right before sunrise already.

3. I did it a few times while I was racing triathlons in college. I'd do two sprint races in one weekend or a tri and then a 5k race the next day. I think the races definitely have to be shorter to be able to do the back to back.

4. Really awesome gelato place right down the street from us. It's not uncommon to load the family up after dinner and head down there.

5. Working my way though the *Racing Weight Cookbook*. They have some pretty good recipes in there but I can tell my pickiness as an eater is holding me back from some. I'll just need to work on getting over some of my food aversions.
[d120mbz] (score 8, diepte 0) That Yamacraw 55k performance really is something to be very proud of, /u/YourShoesUntied. "Racing the clock" sounds really exciting but also really scary.

1. Some guy ran 2:03:02 at a marathon (edit: not "marthon") near me a few years ago. I have not participated, but will in about a month.

2. Starting at sunset, probably. I'm not an evening person, but looking back on my training, I'm much more capable of the latter.

3. Aww yeah I have. 5k/HM and it was a blast, but very difficult because of the elevation profile of the half. One of my prouder moments was stopping to tie my shoe during the 5k and still winning by over 30 seconds. I imagine something really fast and something really long would be really tough to pull off two good performances. Like a mile and a marathon.

4. Those Ninja Turtle ice cream things. Da bomb.

5. I'm super burned out. I think I will still do Boston, but I haven't been training at all. I need to take several steps back, do other physical activities, and get back to the point where I want to run again, because right now I don't.
[d121vs4] (score 7, diepte 2) I thought about riding to work after a really hard workout this morning and told myself "Shoes would do it" and then promptly decided that it was a terrible idea. I judge the soundness of my ideas against your particular brand of crazy.
[d11viu1] (score 7, diepte 0) Very cool to learn more about how you got into running, /u/yourshoesuntied. Wow, sub 20 100 miler... can't wait to hear how training goes leading up to the race in November!! 

1. I have no idea what the fastest race in my area is, or the biggest. But when I lived up north, my first half was the Philadelphia Marathon. I also returned the following year to do my first full. Enormous! Lots of crowd support. Amazing race experience.

2. Early morning, for sure. I like getting a jump start for the day!

3. I've done the Runner's World Festival "Hat Trick", which has you do a 5k on Saturday morning and then the 10k starts an hour and a half after the 5k  start, and then a half on Sunday morning. It was amazing and fun and exhausting but awesome - I didn't race-race any of them, but I had goal times that were faster than my typical comfortable/easy pace, so it was manageable. Pacing was difficult - I wanted to go hard enough to get a good workout but not *so* hard that later races would be unpleasant. I would love to do the Goofy challenge at Disney one day!

4. FROYO. But I eat it in the winter, too. 

5. Feeling good after the marathon! Good training for ultras. Did a "speed" workout yesterday that helped shake out the last of the pain, and walked a lot. Still a bit tight in the quads and calves, but definitely not anything like after running a marathon to PR!
[d11vldj] (score 7, diepte 0) hey YSU, you are pretty much famous on this sub, did you know that?
[d11vt04] (score 7, diepte 0) Crazy story, congrats on finding a passion and sticking to it! Seems like you really turned your life around.

1. Since I run for high school, I traditionally don't do races outside of the season. Though, a few years ago when I didn't do track in the spring, I trained and ran in the Marine Core Half-Marathon. I had never done a race that long before, and it was a very popular race as any Marine Core race tends to be, but it was an amazing experience and the race went perfectly. I haven't done a race that long since, but I'd like to this summer between the end of school and the start of college. Someone hold me to that.

2. Running in the morning for sure. Even though I am pretty bad about waking up early, it's much more satisfying to know that I finished my run and have the rest of the day ahead of me. Then I don't have to worry about what I eat or feeling tired after a long day at school. Plus, I find sunrise the most beautiful time of the day.

3.  I run the 1600 and 3200 usually on the same day at lots of meets. Usually quad meets however, because I am almost guaranteed not to PR if I double. It's good training and builds toughness, but after the speed of the mile, my legs feel much heavier even a few hours later in the 3200.

4. Cold glass of chocolate milk. (Not sponsored, I swear)

5. Hoping to get a lot of beautiful runs in during Spring Break in Costa Rica! Anyone ever run there?
[d11w6b6] (score 7, diepte 0) I instantly subscribed to /r/CatsStandingUp. Thank you, /u/YourShoesUntied.

1. The biggest race in my area is the Half Marathon of the Sun. It has only happened twice so far, but quickly became the state's running event of the year. I ran it both times and didn't do well in them, but still love the race.
2. One of my life goals is to get to a place where I can always get enough sleep every night and still run in the morning, as early as possible. I can't imagine anything better, honestly.
3. I have not. I have run races on back to back days, though. And done quite well in both, thank you very much. They were 5ks. I would love to do back to back 5k, one after the other. I don't think I would do particularly well, but it sounds like fun. I love HMs, but wouldn't run two back to back.
4. My morning smoothie. I've cracked the code and come up with the perfect smoothie for me. I add some new stuff from time to time, but the core recipe is just flawless to my taste buds.
5. I seem to have developed a stress fracture on my right tibia. Going to a runner-specific orthopedist next week to try to be sure. My insurance doesn't cover it and I'm afraid this will cost me a fortune with all the x-rays, bone scans, etc. My marathon is 99% cancelled at this point and my life is over.
(207 reacties met lagere score weggelaten)

=== THREAD 1u97zro ===
SUBREDDIT: r/walking
DATUM: 2026-06-18  SCORE: 889  REACTIES: 198
TITEL: Attention heavy walkers! DO NOT GET PLANTAR FASCIITIS!!!
POST (source_id=post):
I’ve always been a heavy walker my entire life. I’m talking an average step count that has consistently been over 15,000 steps a day throughout the years I never had foot problems. Ever. My feet could handle anything I threw at them.

Then this season came around. I had a goal: get shredded for summer. I wanted to burn as many calories as possible, so I started pushing my walking even harder. For months, I was doing 20,000–30,000 steps a day. I was losing a ton of weight, feeling great, and I thought my body was handling it just like it always had.

Then I started noticing something strange.

After around the 10-mile mark, I would start feeling pain on the bottom of my foot, around the arch and heel area. At first, I didn’t think much of it because I had always been someone who walked a lot. I figured it was just soreness and that my body would adapt.

But it didn’t.

Every single day was the same. I would walk, hit around 10 miles, and the bottom of my foot would start hurting. Then the next day I would do it again. The pain never really went away. It just slowly got worse and worse over time.

This wasn’t something that happened overnight. It developed after months of consistently putting massive amounts of stress on my feet. I kept pushing through it because I didn’t understand what was happening. I didn’t know it was plantar fasciitis. I just thought I needed to tough it out.

Looking back, that was one of the biggest mistakes I ever made.

After about three months of the pain getting progressively worse, I finally figured out what it was: plantar fasciitis.

I’ve had it for about five months now. I’ve spent the last two months aggressively treating it, and thankfully I’m finally at the point where I’ve almost completely gotten rid of it.

But the biggest thing I’ve learned through this entire experience is this:

Preventing plantar fasciitis is 100 times easier than trying to fix it after you already have it.

A lot of people don’t realize how common this actually is. Around 10% of people in the United States experience plantar fasciitis at some point in their lives, and among heavy walkers, runners, and people who put serious mileage on their feet, that number is closer to 30-50%

The crazy part is that my plantar fasciitis probably wasn’t caused because I suddenly became a heavy walker. I was always a heavy walker.

The real issue was my footwear.

My whole life I always wore comfortable shoes. Then I bought a pair of shoes that I thought were fine. They didn’t seem terrible at first, but it wasn’t until I started walking 10 miles a day in them that I realized how bad they actually were.

Technically, I had already bought another pair of shoes because my old comfortable ones were worn out. That pair also wasn’t comfortable enough. So now I was stuck between two different pairs of shoes that I had already spent money on.

My mindset was: “I already bought these. I can’t just waste money and buy another pair. I have to make these work.”

That was one of the biggest mistakes I ever made.

If I could go back in time, I genuinely would have spent $10,000 on shoes before allowing myself to develop plantar fasciitis.

Because after what I’ve gone through these last five months, the money would have been nothing compared to the cost of dealing with this injury.

For months, I could barely walk. I couldn’t play sports. I couldn’t do the things I enjoyed. I lost a very high-paying job because my foot couldn’t handle the physical demands. I spent thousands of dollars trying different shoes, physical therapy, doctors, insoles, KT tape, compression socks, and basically every possible treatment I could find.

This has honestly been one of the hardest things I’ve ever had to overcome.

And what makes it even worse is how scary plantar fasciitis can be. You hear the horror stories about people who have dealt with it for 10, 15, even 20 years. People who tried everything, even surgery, and still couldn’t get their foot back to normal.

Something that seems like “just foot pain” can completely change someone’s life.

That’s why my biggest advice is simple:

Don’t get plantar fasciitis in the first place.

The good news is that for most people, preventing it is actually pretty simple and easy

If you are someone who walks a lot, runs, or puts serious mileage on your feet, these are the three things I would focus on:

1. GOOD FOOTWEAR.

This is the biggest one.

After doing dozens of hours of research, talking to marathon runners, ultra marathon runners, people who run 50-mile and 100-mile races, and watching countless videos from runners all around the worldfrom the United States, Tokyo, China, Australia, Spain, Europe, and Africa the ASICS Gel-Nimbus 28 kept coming up again and again for extremely long-distance running.

When I finally tried them on myself, I immediately understood why.

They are one of the most comfortable shoes I have ever worn.

I would personally recommend them, but everyone’s feet are different. There is no single perfect shoe for everyone.

My biggest advice is: don’t be afraid to spend time in a shoe store. Try on five, ten, even more pairs if you need to. Go to different stores Walk around in them. Don’t just buy something because it looks good or because someone recommends it. Find the shoe that feels the best on YOUR foot.

Other shoes I really like for walking:

Hoka Bondi 9    
Hoka Clifton 10    
New Balance 990  

I personally would be more cautious with some Brooks models because they didn’t work well for me.

For road walking, those are the types of shoes I would look into.

For trails, you obviously need something different. I really like the LOWA Renegade. I discovered these after talking to someone who climbed Mount Kilimanjaro, and these were the boots they recommended. The second I put them on, I understood why. They feel incredible.

The merrill moab 3 was also great I use those to hike up Mount Marcy a few years ago and they were fantastic 

I would also maybe consider something like the Altra Lone Peak for trails, but im not super familiar with trail shoes so im not sure 

2. STRETCH YOUR CALVES.

A lot of people underestimate how connected everything is.

Tight calves put more stress on the plantar fascia, so stretching consistently can help.

You can look up Athlean-X plantar fasciitis stretches on YouTube, or do the classic stair stretch:

Put the ball of your foot on the edge of a step, drop your heel down to the ground, and take your opposite foot and bring it to the second step the step above the foot that you’re stretching and take your whole body and put your weight  towards the foot above it on the stairs and really stretch it out

Do it once in the morning and once at night, or before and after long walks.

3. STRENGTHEN YOUR CALVES.

(Very important)

Do single-leg calf raises on a step.

Go all the way down into a stretch, then all the way up. Do it until you can’t do another rep.

Three to four sets on each leg.

Do this twice a week. Even once a week is sufficient and better than nothing.

You can do both-leg calf raises too, they much easier and they will still help, but single-leg calf raises are better 

you would do three sets as many reps as you can all the way down all the way up on the stairs until you can’t go no more 2-5 min rest between sets three sets to 4 sets twice a week even once a week would probably be sufficient 

If someone gave me this advice before I ever got plantar fasciitis, it honestly would have been worth more than any amount of money.

It would have saved me months of pain, thousands of dollars, and a huge amount of frustration.

The biggest lesson I learned is that your feet are the foundation of everything. If you are someone who walks, runs, works on your feet, or has big fitness goals, investing in your feet is one of the smartest things you can do.

Because once your feet stop working, everything stops.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ose9l0r] (score 452, diepte 0) This reads like an AI output
[ose2tna] (score 393, diepte 0) All great advice that can be coupled up into a couple points: wear good "gear" and don't overdo it! The latter is very important, especially when you are in your 50's like me!
[osegq2k] (score 333, diepte 1) "I got plantar fascitis and here's what it taught me about b2b sales"
[osea533] (score 299, diepte 0) Why is this written like a linkedin post?
[osewyo7] (score 141, diepte 1) 10 mile long post
[ose71a9] (score 129, diepte 0) this is too long mate
[osed6q8] (score 112, diepte 0) Why the chatgpt post?
[oseonci] (score 99, diepte 0) These AI posts are so obvious at this point. Hope the subreddit doesn’t get filled with these
[ose4h16] (score 74, diepte 0) Another pro tip (when I gave myself plantar fasciitis): make sure you're replacing your shoes, insoles, or inserts regularly. Once you hit the 450-500 mile mark, it's time for some sort of replacement.
[osek1ve] (score 70, diepte 3) Because this post is just AI generated slop.
[osftmg1] (score 60, diepte 1) Getting so tired of these long ass AI posts everywhere
[osfatay] (score 45, diepte 1) Yep I'm not reading something that OP didn't consider worth writing
[oseya9u] (score 44, diepte 3) Using AI to tidy your words means its gonna sound like AI. Which is what most of LinkedIn is written with
[osetfqv] (score 41, diepte 2) Yes, but they are trained. Overdoing it means you are not trained enough to do what you are doing. Hence, the plantar fasciitis.
[osi9ytv] (score 37, diepte 1) You know what's even better advice? If you start feeling pain in your body that you didn't previously experience, and it doesn't get better within a few days or a couple of weeks, and you have no idea what it is, see a doctor. There's no good reason for "pushing through" pain when you don't know what's causing it. That's the first advice that should be given.
[osgyo1k] (score 29, diepte 1) I was like "something feels off about this post" and you've nailed it. The one sentence paragraphs and "cliffhangers" 😭.
[oser7wj] (score 24, diepte 2) LMAO
[osevgb3] (score 23, diepte 0) Reads like AI slop hmmmm. Had it once when I was overdoing it, too much too soon. Now I was 25k daily no issues. Always wear skechers, my feet hate anything else! Learned that the hard way. And rolling my feet was a huge help too.
[ose88ie] (score 21, diepte 0) People tend to forget that fitness works by stressing your muscles and tendons, then giving your body time to recover so it can adapt and come back stronger. The problem is that many endurance athletes keep piling on the stress with little to no rest. Instead of getting stronger, they continue breaking down muscles and tendons until an injury shows up. The lesson is simple: rest & recovery is part of training. Rest is what allows adaptation to happen.
[osff4wt] (score 20, diepte 1) The gear is sooo important! I would do 10km walks in converse sometimes and ended up with planters fasciitis and it sucked. Reflexology and proper footwear was the only thing that helped!
[osfjncv] (score 20, diepte 2) This is literally the stuff that shows up on my LinkedIn feed. God help us.
[oseciqi] (score 20, diepte 0) Foot slings/braces that keep your foot flexed at a 90 degree angle while sleeping are a godsend for healing PF.
[osh5lt9] (score 19, diepte 2) I just don't understand it.

Not every sentence needs it's own line.

It's dumb.
[ose5spo] (score 18, diepte 0) There are pains to push through and pains to heed. Differentiating one from the other is the path to success. Nicely written guide!
[osgpq79] (score 18, diepte 2) Are you fucking kidding me?
[oseg3n0] (score 16, diepte 1) This right here is the number one way to help PF.  If you seriously have PF do this first, not most of what OP says.
[osfgqfz] (score 14, diepte 8) Bro let this be a lesson. Authenticity is better. No one cares about grammar issues - it’s better than robotic tone.
[ose6xeh] (score 14, diepte 0) I had PF so bad I had to crawl from a chair to wherever I was going in the house.  I used to nearly cry as it hurt so much and took so long to heal. I don't wish PF on anyone. For me it was excess weight at that time combined with walking way too much like the OP did. Now that my weight is optimal, I am not as worried, but it can still happen to someone who looks fit.
[ose8xzl] (score 11, diepte 2) It took a long time. I completely scaled back my walking, so I focused on exercises that wouldn’t put any load on it (eg cycling, sitting weight training, swimming without harsh push offs on the walls). I’ve bought shoes with arch support and ankle support (as my arches are higher, so for me ASICS are key). No walking at home on bare feet, at any time, always on slippers with foam support) and a lot of stretch exercises specifically for this. I would do 2-3 rounds a day.. icing, and a lot of patience. The first steps in the morning are the worst, so before you get out, warm up those feet with some stretches and then put the slippers on. Everything from A to Z has to become a bible. Until now, I barely wear heels. I’ve dealt with 2 x fasciitis, 1 x gout under my foot (I was on crutches for about 7 weeks) and now with tendonitis. It’s frustrating, but with patience and care you can get rid of it. Do not walk through it, buddy.. not worth it.
[osem7uz] (score 11, diepte 0) This is a good summary of how PF actually develops - not a sudden injury but a slow accumulation of load that the tissue eventually can't absorb. The jump from 15,000 to 20,000-30,000 steps daily is exactly the kind of volume spike that pushes a tissue past its tolerance ceiling before it has time to adapt.

One note on the calf raise protocol: the full drop off the step is excellent for general PF and mid-portion Achilles problems. If anyone reading this has pain specifically at the back of the heel where the Achilles attaches - rather than under the heel - skip the downward phase and do raises from flat ground only. The insertion doesn't tolerate that stretch under load the same way.

The core message is right though. The tissue's capacity to handle load is the thing that determines whether high walking volume causes problems. Footwear changes how load is distributed, calf strength changes how much reaches the fascia, but neither replaces building the tissue itself.
[osfc9cb] (score 9, diepte 6) No you didn’t it’s all garbage
[osez5bk] (score 9, diepte 2) Yeah right.
[osev0nq] (score 9, diepte 0) Tight shoelaces caused mine. It prevented ankle mobility and my calf and instead foot was taking all the force repeatedly.

Don’t tie your shoe laces too tight.
[osffyxt] (score 9, diepte 0) Wow, so AI
[ose5xww] (score 8, diepte 0) Been there done that.. even though I was always was wearing proper walking shoes. It’s horrible, but can be reversed. Now dealing with tendonitis, got it whilst prepping for my trek to Mt. Everest. Another fun injury to deal with! Too much, too fast, too enthusiastic. Boring is good. Keep it boring and consistent.
[osfgjev] (score 8, diepte 3) My guy, it is what we in the industry call *a joke*.
[osectie] (score 8, diepte 0) Also a lot of foot pain gets misdiagnosed as plantar fasciitis when it’s actually something else. My podiatrist kept saying I have plantar fasciitis but I found out recently I actually have an accessory navicular bone that attaches my tibilias posterior tendon which may be inflamed.
[ose2cj9] (score 7, diepte 0) This was so detailed and helpful thank you, hope you’re plantar fasciitis free soon!
[osexmlv] (score 7, diepte 0) Altra sneakers are zero drop heel and offer a wide toe box so they’re designed for proper support and foot placement. Been amazing for healing and post plantar fasciitis. 

Also -the toe stretchers were the most effective treatment for PF  and they are inexpensive
[oseivj6] (score 6, diepte 2) How come you are getting so many downvoted, I don't understand?
[osfe4rf] (score 6, diepte 8) How long did it take you to “run” that thru AI? Try thinking for yourself
[ose9a5b] (score 6, diepte 0) I have it now and it's having a seriously negative affect on my wellbeing. Can you tell me what treatments ultimately helped you? I feel like I am very much at the beginning of a long journey.
[osez20f] (score 6, diepte 0) Funny enough Asics and Hokas made my foot pain 1000x worse, while I could walk 20,000 steps in my Brooks no problem. Just goes to show that everyone's foot is different and you have to find what works for you!
[oseok6q] (score 5, diepte 4) Awww damn man I thought I was good at spotting them I feel so dumb. Thank you for telling me! Friggen AI 🤮
[osf60s0] (score 5, diepte 6) Aw. Fuck. I'm sorry, shit now I feel bad. You know I think that your heart and effort did get thru to me originally and I didn't initially judge it that way. 

I'm sorry I should have waited to hear your answer, and I honestly learned a lot from your post and do appreciate it. I'm sorry I hope people read your response, so that you don't have to deal with the hell of misdirected hate comments I know what that can be like and if it happens remember to turn off notifications so you can stay sane. 💖
[osgpw5t] (score 5, diepte 5 OP) Hey buddy, I find it extremely disrespectful that you would sit here and say this is an ad. I put a lot of work into this post to help other people and a lot of research to find the right shoe not getting paid a dollar for this shit and I literally specifically said don’t listen to me or anybody else on a shoe recommendation. Try on 10+ pairs yourself and make sure you find the absolute most comfortable one for you. I said that that shoe the Asics is not gonna be a good fit for everybody. Try on many shoes and make sure which one feels the most comfortable. If you wanna try on the Asics nimbus fine try on at least 10 other shoes to compare them to first I’m not making a dollar from this post. I’m trying to help other people and you’re being a completely disrespectful by sitting here saying this is an ad. Do you know how many hours of extensive research I had to do to come up with this shoe?
[osh6rw3] (score 5, diepte 2) The problem is that using AI for the 5% (as you put it) of tidying and structure has made the whole thing totally read as AI.

I've been using AI for hiking and mountaineering boot recommendations and it is all way too familiar (my AI loves Lowa Renegades too).
[osgn5qm] (score 5, diepte 1) At least there's an AI summary, lol
[oseatuv] (score 5, diepte 0) Adding onto your excellent post: shoes for recovery after walking.  Oofos or other high quality recovery sandals.
[osf5al2] (score 5, diepte 0) That’s a lot of walking (and typing)
[osgau80] (score 5, diepte 0) So this is AI and I’m not even sure…why? One would need to urgently create an AI post about this? This behavior is strange.

Nonetheless. I had to get PF surgery last year after about a year of horrible pain with no relief. Now it’s much better, but the recovery! Jesus! It was months and months and months of recovery. I’m walking mostly normal now and I kind of can’t believe it. I buy new shoes every new year and every end of June (it’s new shoe time, baby!). PF, like reading a long, weird AI post, is such unnecessary suffering.
[ose5nva] (score 4, diepte 0) I'm not planning on it.
[ose9np4] (score 4, diepte 1 OP) I just started a new job so I didn’t work there long enough to qualify for a short term disability they didn’t exactly fire me for missing days of work due to this injury but what they did do is wait for me to make one mistake and fired me then bought me personally I don’t think they fired me for the one mistake I made because it was very small I think they fired me because of the days I missed because of my injury. But they pretended to fire me for something else that’s how the game goes.
(164 reacties met lagere score weggelaten)

=== THREAD yrkknr ===
SUBREDDIT: r/Military
DATUM: 2022-11-10  SCORE: 2602  REACTIES: 180
TITEL: Chinese PLA rocking Yeezies and Air Force 1s while your feet get blisters and a bit of swelling in boots.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ivubk8m] (score 1038, diepte 0) That’s a very casual man being squished
[ivumb3k] (score 1022, diepte 1) Legally the Chinese military cannot take a photo without there being some form of human rights violation.
[ivu2dv1] (score 331, diepte 0) yea, betcha there are no counterfeits in China and these are totally legit
[ivuccvo] (score 295, diepte 0) So what’s going on with old man at the bottom lol
[ivucp30] (score 264, diepte 1 OP) Human sandwich, or China's unique way to deal with covid lockdowns
[ivuqxys] (score 225, diepte 2) Good thing that's never an issue for them.
[ivudzuh] (score 174, diepte 0) When I was in the army you could only wear approved foot wear, while simultaneously the PX would sell just as many boots that "looked reg" but weren't. Learned this the hard way. Also pt shoes required arch support, I am partially flat footed. I could run like the wind in my Chuck Taylors but they weren't on the approved list so I had to wear shoes/boots that fucking hurt constantly. Now I have ankle,knee,hip,lower back,upper back and neck issues, but by golly I fit regulations!!
[ivun5gr] (score 161, diepte 2) Yeah is it really a counterfeit if it’s made with the same materials by the same person in the same factory, just sold in a sketchy manner for a cheaper price?
[ivua9yc] (score 150, diepte 1) I mean they do make them there
[ivui4oj] (score 143, diepte 0) What the hell is going on here?
[ivv69r6] (score 114, diepte 1) I'm not sure

But it's funnier if you imagine them repeating "the power of Xi compels you!"
[ivv7bq9] (score 93, diepte 3) Actually, it is surprisingly difficult.

Since the CCP does not consider the Uighur to be humans, anything they do to them is not a human rights violation.
[ivv23oy] (score 69, diepte 2) You just made all of that up.
[ivurdig] (score 67, diepte 1) Get that VA % when you get out my man
[ivv2okj] (score 62, diepte 3) Don’t worry they don’t have that phrase in the Chinese language.
[ivut9ck] (score 56, diepte 2) Finally got my 100% last spring. It's made a world of difference
[ivvi68y] (score 53, diepte 2) Don't you mean Hunan Sandwich?
[ivv0l4y] (score 52, diepte 3) Makes it seem kind of stupid that we collect these things like some sort of super status symbol.

Everything is a collectable now. Shoes, pants, shirts, hats, etc.... What is next? Collectable phones and socks???

These guys are wearing them as their work shoes.
[ivu5djz] (score 52, diepte 0) I wonder how many PLA would just love the CCP to be gone if they got to keep their bennies and had immunity to citizen retaliation.
[ivvdf16] (score 46, diepte 2) “More weight”
[ivuqggx] (score 36, diepte 1) Was going to point out you won't get much swelling in your boots if you're standing on comfortable homles person
[ivvcfn8] (score 33, diepte 4) You get social points for being a good communist citizen.  The points get you nothing.  Not having points gets you re-educated.  Or dead.
[ivwaavg] (score 32, diepte 4) Sounds almost like Turkey dancing around a war crime against Armenia. Just need the CCP to say something a bit like, "Never happened, but they totally deserve it," with a poker face.
[ivuyhcm] (score 32, diepte 4) Don't stop, reapply for everything that's wrong with you, when you show up for the eval appointment AGGRAVATE THE SYMPTOMS SO THE DOCTOR CAN SEE HOW BAD IT GETS!! Also, don't sugar coat anything talk about it in brutal honestly so you can actually get your compensation. If you take a vehicle to a mechanic he cannot fix the fault if he cannot find the fault.
[ivv53nc] (score 31, diepte 2) To be fair lol, if anyone were ever to post the PLA doing something good (say a photo of the PLA helping during the 08 earthquake) they’d be asked how many social points they were after.
[ivv74yw] (score 30, diepte 4) Air force 1 is pretty cheap shoe if you compare it to work or military shoes.
[ivuf8tm] (score 29, diepte 0) Shouldn't have parked there old man.
[ivuti8w] (score 26, diepte 3) Nice man. I’m at 60% myself. It’s really helpful
[ivuo9k6] (score 25, diepte 0) So I can get to stompin in my air force ones 🎶
[ivupqly] (score 18, diepte 4) Nike/Adidas QC is actually worse than the QC I’ve seen come out from the rep factories, especially the higher tiers. Not all reps are created equal though.
[ivuk385] (score 18, diepte 0) This looks like some Cultural Revolution "struggle session" shit.
[ivvau8x] (score 16, diepte 3) What are social points and where can I spend them?
[ivvg2am] (score 14, diepte 5) Im at 50% for PTSD and 10% for GERD. but there is not a whole lot else wrong with me. I did apply for OSA via a supplemental claim. but I have been waiting since August for that one.
[ivv8oq2] (score 13, diepte 4) Jokes on you there's already collectable phones and socks!
[ivvum4v] (score 13, diepte 3) Distasteful sammy
[ivv4al8] (score 13, diepte 2) I think they are trying to redefine lockdown...
[ivutck1] (score 13, diepte 1) I have a hard time believing you have tried all the boots and your chucks, notorious for no support, are more comfy than say… Garmonts or even Nikes.
[ivuypsm] (score 13, diepte 0) Well, it's just bad form to torture someone without comfortable shoes.
[ivwcb1m] (score 12, diepte 3) The YouTube channel laowhy86 explains tons and tons of flaws within China at nearly every level. The guy himself lived there for ten years and says he saw the country change for the worse in that timespan.
[ivwhpqy] (score 12, diepte 4) Not just a Crucible reference, [it's fact](https://www.masshist.org/beehiveblog/2021/09/giles-corey-pressed-to-death/#:~:text=After%20two%20days%20of%20this,words%20were%20%E2%80%9Cmore%20weight.%E2%80%9D).
[ivujq7s] (score 11, diepte 0) TikTok army is fully equipped for posing.
[ivuo4q3] (score 10, diepte 3) However it probably wasn't QC'd so it may be defective, so maybe?
[ivvxvyg] (score 10, diepte 7) Sure blame it all on education.

If you think a totalitarian dictatorship that tramples over human rights every chance they have is not an enemy to the free world, that's the true educational failure.

At the end of 1940s we've all collectively looked at Auschwitz and said never again. And yet when it's Uyghurs getting packed into a concentration camp having their hair harvested, raped and tortured we turn a blind eye. And no it's not a rumor. We have plenty of photos, video evidence that proof it's a very real issue.

If you truly genuinely think a country that runs a concentration camp is not our enemy, well, what more can I say.
[ivvn51r] (score 10, diepte 1) They're trying to liberate land and property from a witch. But only if he confesses.
[ivwy8hr] (score 10, diepte 1) Blatant human rights violations in the name of preventing COVID spread.
[ivujt2h] (score 10, diepte 0) They run the factory where they are all made that's why they get the 5 finger discount.
[ivvr726] (score 9, diepte 5) Military boots are in the realm of 150-200 bucks, not that much more
[ivuawk4] (score 9, diepte 0) Theyre all on chit from the blisters
[ivvorwr] (score 9, diepte 1) They are thankfully finally figuring out people have different feet. The air force you can damn near wear Chuck Taylor’s in uniform as long as they’re brown. Army as long as it berry compliant I think but even then who checks. Marine Corps selection still sucks they’re a diehard for needing the EGA on our boots even though it wears off .2 second after wearing them.
[ivuynox] (score 9, diepte 0) It's China. We all know those shoes are fake.
[ivvzspw] (score 8, diepte 5) Have you shown him this new DBZ collectible swatch watch collection? I picked up the perverted hermit Master Roshi one to replace my swatch charlie brown watch for the time being.

https://www.swatch.com/en-us/swatch-x-dragonballz.html
[ivvx35f] (score 8, diepte 5) Nah I've seen them as the enemy well before 2008.

Well, potential threat back then. Now a full fledged enemy.
[ivw4dvv] (score 8, diepte 6) Why the fuck have you not filed for tinitus?
[ivux1ei] (score 8, diepte 2) Dude I was enlisted, all I could afford were New balance. Never even heard of Garments. The issued army boots were god awful, had to use gel insoles just to make them tolerable and they only lasted 6 months max, Oakley boots were outlawed by first sergeant for "being too flashy" even though they were all tan. I was armor maintenance and we were supposed to be issued steel toe boots but that magically never happened. And like I said, I'm partially flat-footed so having high tops with a foam insert makes all the difference.
[ivvz0j5] (score 7, diepte 9) >implying I don't consider Saudi Arabia, Iran, etc enemies of the free world
[ivw9qjz] (score 7, diepte 3) TO BE FAAAAIIIIRRRR
[ivw5fkv] (score 7, diepte 7) Well. I would have to lie about it.
[ivux0ib] (score 7, diepte 1) No parking lol.  And I think they are militia according to their ranks
[ivuyfi5] (score 7, diepte 0) Not when you're rocking Lowas baby 😎
[ivvz9k0] (score 6, diepte 11) You really like blaming it all on educational failure eh
[ivw857b] (score 6, diepte 19) And your argumentative style being…?

What I've been seeing is condescending, multiple repeated needless personal insults that is irrelevant to the conversation at hand. Trying to position yourself as an intellectual superior to make your argument more sound? Is that your approach to conversations? Cuz it's VERY convincing
[ivw2n4l] (score 6, diepte 2) The sign is a no parking sign and probably has nothing to do with the situation. Looks like a guy leaving covid lockdown for the reasons you stated.
[ivv8f04] (score 6, diepte 2) Hahaha indeed
[ivvkjh1] (score 6, diepte 1) I feel like I'm always the only person to recommend Lowas and I feel 100% vindicated by your comment.
[ivw12oy] (score 5, diepte 6) I don't think it would be a good idea to show him those, he might choose the watches over rent. 


His car is decked out with dbz stuff too, like seat covers and shift knob and such. 

I'm surprised he doesn't have any visible DBZ tattoos, I'm afraid to ask.
[ivw6782] (score 5, diepte 7) hahaha he will find these soon enough probably.....
[ivvwfqq] (score 5, diepte 6) Na you get to commit suicide via a bullet to the back of the head and your family gets an all expense paid one way ticket to Siberia.
[ivwy115] (score 5, diepte 5) Actually I think the points can move you to the front of the line for COVID lockdown food deliveries. They also get you special deals on travel tickets and other perks.
[ivvpht1] (score 5, diepte 3) There's no true reason to do free PR for the *enemy* other than monetary gains.

Or they kidnapped your family and force you to do so. Which isn't impossible coming from the Chinese dictatorship.
[ivwjwse] (score 5, diepte 2) As a result of his refusal to plead, on September 17, Corey was subjected to the procedure by Sheriff George Corwin, but he was steadfast in that refusal, nor did he cry out in pain as the rocks were placed on the boards. After two days, Corey was asked three times to enter a plea, but each time he replied, "More weight", and the sheriff complied.
[ivuwtld] (score 5, diepte 0) When you don’t do shit in the field, you wear yeezies and AF1s.  Keep rockin them stupid ass shoes and pulling bullshit training China
[ivv2ecx] (score 5, diepte 1 OP) yes, they're paying me in AliBaba vouchers
[ivvy481] (score 4, diepte 4) I work with a guy that has a different pair of DBZ socks on everyday. I've never seen him wear the same pair.
[ivxghdu] (score 4, diepte 5) Can I exchange reddit karma for social points? 

I don't mind a second education but getting deaded is not an option at the moment for me.
[ivuhkts] (score 4, diepte 0) I’ve had bruises on my feet since boot camp
[ivwhcv8] (score 4, diepte 0) What the actual fuck is going on in this picture
[ivw429r] (score 3, diepte 17) Well if you want to argue that having an active concentration camp that does organ harvesting, torture, rape, a giant internet firewall that requires a every citizen to use a VPN to bypass, information control to a point some of the citizen denies the Tiananmen Square massacre, every after they've left China and is shown footage of said massacre is as bad as evicting some illegal immigrants back to where they belong, having police abuse their power against African Americans…enough to mark em as an enemy of the free world…I got nothing to say!

And remember the cop who murdered Floyd is facing his consequences. Meanwhile all the LE who commit atrocities in China will never get what they deserve because they are well protected by the system in place.

Heck all the beaten disappeared Hong Kong students, not even mentioned in the news, forget about finding who's responsible for it.

The journalist who was shot anf partially blinded for life by HK Police, while fully knowing they are shooting at the press, same thing. No police officer will ever have to answer for the atrocities they've committed under Chinese ruling.
[ivwe7jr] (score 3, diepte 20) This is a good thread, but it's getting kinda stale. They're pretty much saying you're throwing random (although factual and understandable) points and events that don't necessarily correlate with one another other than "China Bad" at a board and saying "reply to that". Their "you're not educated well" points are repetitive I can tell and obviously condescending, so I feel you there, at this point there's no real conversation to be had unless it's just back and forth on the same argument until someone throws a straw man
[ivwjm8j] (score 3, diepte 8) Do you have ringing in your ears at least some of the time?
[ivy7cnz] (score 3, diepte 10) I wouldn't really call it lying. 

I mean if you didn't have it prior to joining the military claim that shit.

For me at least it comes and goes. Gotta have white noise and shit to tune it out.

Nowhere near what I'd call actual tinnitus. But guess who got 10% out of it?
(86 reacties met lagere score weggelaten)

