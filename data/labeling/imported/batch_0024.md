# Label-batch batch_0024

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
Schrijf het resultaat naar `batch_0024.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(5 threads: 2xx58w, owa4jt, 17h0w41, 4ni93b, ggjmvx).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 2xx58w ===
SUBREDDIT: r/BarefootRunning
DATUM: 2015-03-04  SCORE: 7  REACTIES: 36
TITEL: Best Minimalist shoe for Barefoot 'Walking'?
POST (source_id=post):
To follow up from the questions I asked in my last thread(which was a great success), I am wondering : What is the best minimalist shoe for long walking?

Soon I'm going to need to walk three miles to the nearest bus stop, then ride the bus for awhile, then walk another mile, then stand around/move around, and then return home! All in all, it's probably 4 miles there, 4 miles back, but also may be more walking around. 

The problem is this : Some of the minimalist shoes that people think look nice, MAY NOT be useful for walking and performance. I actually want to be able to walk / break into a barefoot run when the energy allows, and not just have a shoe that looks normal or office worthy

So, I figured Merrell's would work, only to have people tell me that they're basically a 'stiff' shoe -- And not just another poster who pointed out that they have a very stiff mid that makes it hard to walk naturally -- since the walking is kind of front, mid, back, or at least allowing all parts of the feet to hit the ground, whereas these shoes are kind of designed for going at a fast clip, ie, not intended for people who 'push off'

Anyhow, I'm wondering, has anyone been in a similar situation? Needing to 'walk commute' somewhere or just walk around a lot, and if so, do you have a minimalist shoe to recommend? Obviously VFF's would work for pure performance, but ideally I would want something that looks like Merrells, but has a bit more freedom 

I'm actually a bit worried about the daily mileage alone, but sadly bad choices/other things have put me in a situation where this is necessary(it would be easier to run this distance daily than to walk it, if you know what I mean)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cp4dsc5] (score 6, diepte 1) Strike with your heel while walking. Running is different.
[cp4pvns] (score 3, diepte 1) The purpose of a minimalist shoe is to promote a natural gait. Your body naturally heel strikes at low speed just as it strikes fore foot at high speed. Forefoot steps at low speed is essentially goose stepping.
[cp46ygn] (score 2, diepte 0) I would think that most any shoe would be able to handle this requirement... I live without a car in a city, so most of what I do is walking, and all of the shoes I have lasted years. I use Vivobarefoot Dharmas mainly, with Vivobarefoot Aqua Lites also making occasional appearances. I also thru-hiked the Appalachian Trail (2185 miles) using Merrell Trail Glove 2s and each pair (I went through three) lasted between 500-1000 miles of trail before getting pretty blown apart.

Further, walking to work and back isn't really a high-performance activity. In my humble opinion, you're overthinking it. Get something that you think is comfortable. Both Vivobarefoot and Merrell have been good to me, though I prefer the Trail Glove 2s for more athletic endeavors.
[cp5056g] (score 2, diepte 2) > hich will end up being around 1500km (~900 miles). I've been trying to figure out what shoe to get.
> I compared the Merrell Trail Glove and the New Balance Minimus (MT10 V2 Trail) at REI, and I have to say that I liked the fit of the NB Minimus so much more. I thought the Merrell Trail Glove had a bit too much bridge support for me, and was creating a pressure point. I'm concerned about wearing a hole in my sole before I reach the end, though. It seems like with your experience with the AT, I'd definitely be in the danger zone, but then I expect the AT is a whole lot more rough than the Camino most of the time.

One thing I've also been hearing from multiple sources is the 'stiff' mid of the Trail Glove, so that people feel like they can't walk naturally. I've been thinking on this a lot, because there's some posters who report good experiences with it, and then others who talk about the bridge/mid being too stiff and putting pressure on their feet -- like yourself

I think the problem could be the 'height' or the developed arch in some people's feet. As I said before, my feet have gotten ugly since taking up barefooting in 2009 -- One of the things is that there's a bit of a 'dome' on top of the foot now, like the muscles are so strong the foot went from relatively flat to quite tall

Anyhow, guess that doesn't help you with your problem, just thinking out loud here
[cp4d2sf] (score 2, diepte 1) Well, part of it is that I'm going to be walking to a community college, I'm a bit nervous already as I'm going to be older and broker than most of the kids, plus just other issues that make me not want to risk wearing Vibrams around there

But I do agree, Vibrams are the best and I think opened up a new world for all of us. Maybe in 10 years I can wear them everywhere, but now I kind of want something that is 'less weird'
[cp4bls3] (score 2, diepte 0) I find walking and running in minimalist shoes to very different.  Running in Vibrams works fine.  Walking in Vibrams is very slow.  Walking with a forefoot step is slow.  Way too slow if I need to get somewhere.  I find that I need more padding for walking than for running.

I have not tried many shoes for walking, but I have a pair of Innov8 shoes that I like.  Zero rise, but some padding to making walking more quickly possible.  Otherwise it seems like walking quickly in Vibrams is like speed tiptoeing.
[cp4mfiy] (score 2, diepte 2) That's my experience as well.  I've done lots of barefoot and minimalist walking and healstrike feels great to me.
[cp4cxhf] (score 1, diepte 1) Sigh... thats' why I love this sub and the barefoot community in general! Very encouraging, and yes I think I was overthinking it. I've had quite a bit of set backs and I think that's made me begin seeing everything as a massive obstacle -- I appreciate your thoughts

I was concerned about Merrell Trail Gloves actually, now that you've said you carried out such a long walk with them, MUCH longer and more difficult than my planned daily walks, that definitely eases some fear

HOWEVER... I should add that my concern with the minimalist shoes wasn't that they just 'hold up', but that they don't cause any kind of foot pain or unnatural kind of thing happening in the foot -- Yes any shoe can handle the miles, but my concern is being able to not suffer from foot pain or injuries
[cp4hung] (score 1, diepte 2) I wore trail gloves around town for most of last summer, and I found the soles to wear out quickly, although it seems I tend to heal strike quite badly when walking as opposed to running, and the heals wore through very fast. I haven't looked into it, but I wonder if the road gloves or another model have harder rubber and might suit better?
[cp50331] (score 1, diepte 3) Hmmmm, so they wore out pretty fast, do you mean that they actually wore all the way through so that you were pretty much walking barefoot on cement? If so, that's a very bad sign for a walking shoe -- Thanks for sharing your experience
[cp50vmb] (score 1, diepte 4) I didn't get all the way to foot on concrete, but the black rubber on the sole was worn out and part way through the yellow on the patch where i heel strike. Still have some life in them, but they wore quickly with daily use in the city. Otherwise they held up well on the rest of the shoe. I don't think it was terrible performance, but not as good as i hoped.
[cp4i1dm] (score 1, diepte 1) I don't mean to jack the thread, but I've been doing unending research on long-distance lightweight shoes. I'll be walking the Camino de Santiago from Le Puy, which will end up being around 1500km (~900 miles). I've been trying to figure out what shoe to get.

I compared the Merrell Trail Glove and the New Balance Minimus (MT10 V2 Trail) at REI, and I have to say that I liked the fit of the NB Minimus so much more. I thought the Merrell Trail Glove had a bit too much bridge support for me, and was creating a pressure point. I'm concerned about wearing a hole in my sole before I reach the end, though. It seems like with your experience with the AT, I'd definitely be in the danger zone, but then I expect the AT is a whole lot more rough than the Camino most of the time.
[cp5bjlh] (score 1, diepte 3) No worries man - I appreciate the feedback anyway. If I do that many miles in a minimalist shoe, I doubt the arch support will become *less* of a problem for me. If the NB Minimus is deemed (likely) durable enough, then I'll probably go ahead with that.
[cp47b54] (score 1, diepte 0) VFFs are very comfortable to walk in. They have loads of options wrt sole tread / thickness and material / for comfort or performance. There are currently 20 different types of VFFs on the vibram site, many more than Merrell options. Why look like Merrells? Is it because of the separated toes?
[cp4dykv] (score 1, diepte 2) I wore mine to and from work ..a business setting (they were grey / black) and matched my grey suit and if people stared, I really didn't care. I was new but no biggie. You may be more self conscious the than needed as they may not really care at all. And if they do, they are not the king of people you want to spend too much time around.
[cp4hop2] (score 1, diepte 3) As much as possible I want to blend in because sadly, most people are really judgmental and looking to criticize anything that's not 'cool'(srs). I wish it wasn't that way, and maybe you're in a bit more of an enlightened place than I am, but in my experience, people are angry at you if you're different than how they think you should be/how they are
(really, I've had people get mad at me for just reading before or not wanting to socialize... Like, a lot of people)

But... That being said, your philosophy is better than mine, maybe someday I can have a 'dont care' attitude, but... then again it's tricky. I think for now I need to find a minimalist shoe that looks normal
[cp48ycu] (score 1, diepte 0) Love my Zemgear...if I'm shod, this is it.
[cp4cstv] (score 1, diepte 1) Walking is actually very similar to running. You knees are still bent on landing because your feet are landing nearly underneath you. Think of walking while pushing your hips forward. I see your thinking quite often and I used to think that way as well. Barefoot walking fast is possible.
[cp4dgrc] (score 1, diepte 2) Is it? I actually can't get beyond the average human walking speed, like I find that I cannot get to my destination(3 miles away) in less than an hour

Please share any tips or experiences you have with barefoot walking since I'm definitely interested in being able to barefoot walk much faster
[cp54ukz] (score 1, diepte 3) The key is feet landing under or nearly under you and knees bent. When people usually walk, they straight leg their landing. You can't do that barefoot. Think of your leg muscles as shock absorbers. If your leg is completely straight, then your muscles can do nothing to absorb the shock. It's in lockout. It feels a little weird at first to walk with the knees more bent and it takes practice, but it is fast. The next step to going faster is "pushing" your hips forward. I'm not sure how else to describe it. This helps to keep up your upper body with your legs so that your feet land beneath you. If your feet land in front of you, then you're likely straight legging it and heel striking. If you're walking with bent knees and feet landing underneath you, then it doesn't even really matter if you heel strike, because your leg muscles will absorb most of the shock.
[cp5dqpn] (score 1, diepte 4) I will have to try this.  I think I'm going to look like a person with a new pair of legs for a while.  Thanks!
[cp64p73] (score 1, diepte 4) Rabbit, I just got back from a morning walk in my fila skeletoes, and as I was walking I was thinking -- What got you interested in this? Do you do a lot of 'barefoot' walking? 

I'm just wondering because it's been a subject I'm kind of interested in, as every once in awhile I wonder what would happen if I did 'long distance' barefoot walking -- either way, interesting thoughts
[cp67e10] (score 1, diepte 5) I've hiked the Appalachian Trail in about 110 days using conventional running shoes when everyone was telling me that wouldn't work and that I needed boots. I'd love to do a long distance trail again only with minimalist shoes or even barefoot when the surface allows for a fast walk. Until then, I pretty much only wear minimalist shoes even in winter, so walking form is often on my mind.
[cp4daa2] (score 1, diepte 1) haha @ speed tiptoeing

I admit that walking in Vibrams does make me sometimes feel like a maniac -- Like I suddenly get the feeling that I look crazy because I'm moving my legs too fast, but I think because I walked in them for so long, that I can walk pretty well in them

Though... now that you mention it, I did notice for awhile that I forefoot striking while walking, which is probably not how most humans walk, lol

I'll look into the Innov8's, but I still am waiting for someone to weigh in on New Balance Minimus's or whatever they are called -- To me they seem to look like the most 'gym shoe'y' of the minimalist shoes, and that's kind of what I'm going for as far as looks go -- But they just don't have a lot of reviews on Amazon compared to Merrell's, and I think maybe only one person mentioned wearing them in my last thread, so I'm really anxious to hear someone's experience with them(with walking)
[cp4dvnm] (score 1, diepte 1) I've never had issues walking in them and don't really think about how I walk. I just let my brain figure it out. Per Inov-8s, I find they have a narrow forefoot.
[cp5dkoi] (score 1, diepte 2) I have very wide feet, and I don't have a problem with them.  Yours must be wider.
[cp4h5jm] (score 1, diepte 0) I'm outta running shoes and sandals and into Vans or regular sandals for walking
[cp4ikah] (score 1, diepte 0) As long as it's not offroad, I highly recommend New Balance's MR10V2's. Super comfortable, super light, pretty much perfect. I'm about to order my 3rd pair.

Get them in black for the casual look.
[cp4k2qi] (score 1, diepte 0) I like my Skoras for walking and running. They are 0-drop and pretty flexible. I usually take the liner out, but if I am doing a lot of walking on hard surfaces I can put it back in.
[cp4ncw7] (score 1, diepte 0) I do everything in my Lems Primal. They're great for walking with the insole in. Just enough padding that I'm comfy, but thin and flexible enough that I still feel free.
[cp4px2x] (score 1, diepte 0) I like the Achilles by vivo  barefoot. Easy to keep clean and super breathable. Like secure sandals. I love them
[cp4umg9] (score 1, diepte 0) They aren't really barefoot shoes and much as "minimal" style, but I love my Nike Free 5.0's for walking. I walk my dog about 8 miles a day on sidewalks (she's not much for running on the leash).  

At a slow pace I have a really hard time avoiding heel striking.  I find New Balance Minimus style shoes would cause a noticeable amount more fatigue in my feet and knees than the Free's with their extra cushion.
[cp5djtq] (score 1, diepte 0) Vivobarefoot Gobi's have been my daily shoe for the past 6+ months and they work great. Not the best traction on ice but I have good balance so I haven't slipped even once, but they do have terrible traction on ice... That's the only negative I have to say about them.
[cp5fim2] (score 1, diepte 0) I think Vivobarefoot EVO Pure would fit your needs/wants. It's such a shame they're not selling the Aqua Lites anymore, it got discontinued just before I found barefoot/minimalist shoes. :/
[cp6voop] (score 1, diepte 0) I do a fair bit of run/walk . Mostly I have been using NIKE Fre5.0's. I run naturally on my forefoot - but walk on my heels. I have been finding that the NIKES have insufficient cushioning under the heel for walking - but are good for running. 

I believe that what is required for running AND walking is a shoe with a lowish heel/toe drop but with plenty of cushioning overall. I have recently bought a pair of Skecher Go Run 4 which has all this but have not walked much in them as yet. Running wise they seem very goo - nice and light -- but I am concerned about how much life I will get out of the sole.
[cp974sj] (score 1, diepte 0) I've found anything works once your feet have adapted. Initially Feiyues weren't very good for me, but after wearing VFFs for 6 months, and going back to Feiyues they worked fine (even when I didn't lace them up). Now it really doesn't matter. I simply don't wear shoes that mess my feet up. 

Vivobarefoot shoes might be a good option for looking normal while at the office but allowing you to break into a run. Unfortunately the soles tend to wear out.

=== THREAD owa4jt ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2021-08-02  SCORE: 3  REACTIES: 35
TITEL: New Long Run Shoes
POST (source_id=post):
Hi All,

I post here a lot (sorry) but you guys are great so looking for more advice. I'm currently doing about 20 miles a week of structured training including tempo work and VO2Max intervals, with a long run Sunday looking to up my mileage gradually.

Yesterday i did my longest run yet a slow 14km run (under 171bpm) took me around 1 hour 30 in my old Brooks Ghost 10's (around 6:15minutes/km). The Brooks are worn out to be honest so it’s my own fault I’ll admit. Im experiencing pain in my knees today. Wondering if it’s to do with the high drop of the ghosts (~12.4mm) and maybe a possible lack of a bit of cushioning in a worn out shoe. I’m only 70kilos in my mid 20’s. Think I mainly heel strike with a low cadence, long stride. 

Want to protect my knees at this early stage so looking for something with maybe a bit more cushioning, possibly a lower drop to take the strain off my knees a bit??? And a fair bit of stability (which ruled out the novablast 2’s initially but still open to it if you think they are stable enough as I do like the sound of them). I run in the rebel V2’s for slowish tempo runs as they’re super cushioned and get on well with them. Thinking maybe the 1080v11’s, Brooks Glycerins or even possibly More V3’s. Open to suggestions. 

Any advice?
Thanks all.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[h7f2z13] (score 9, diepte 0) Shoes won't really matter too much at these distances and I have never experienced drop making an observable difference, so just run in what's enjoyable.

The knee pain is going to be more of a product of your distance and perhaps speed being more than you can handle. At 20 miles a week, 14km is almost half your weekly volume — I'd be aiming for about 25 to 30%. I don't know what your max HR is, but if you're scratching 171, that feels like a marathon pace effort and that's not the kind of thing you want to be doing when targeting a new long distance. And even if you ignore that, if you do [these stretches](https://coachjayjohnson.com/sam_pdf/) diligently, you can probably get away with some irresponsible running.

Lastly, long run shoes are oddly specific and it's often more about geometry and energy return over raw cushion — you want the cushion for recovery days. Seth James DeMoor on YouTube has good recommendations for shoes like these and if I were in the States I'd be picking up the Skechers Max Road 5.
[h7ev6z8] (score 4, diepte 0) Second the 1080v10s/11s. A great shoe and a workhorse. Long runs, tempos, longer session efforts, they're great. I also got the Nike Invincible and Asics Novablast 2s. The nike's are super cushioned (more cushioned that both Asics and the 1080s) but love both!
[h7f2jq9] (score 4, diepte 0) I can reccomend Asics Glideride 1/2 as one of the best long run shoes out there. Unfortunately this is the only type of runs they're really great for.
[h7gm3i6] (score 3, diepte 0) I am not an experienced runner but I own the NB 1080v11, Endorphin Speed 2, Vaporfly Next%2 and soon the Novablast 2 (ordered last week). In my opinion the 1080v11 is a very comfortable and stable shoe with great cushion (also amazing breathable upper mesh). And that's it, no significant energy return or bounce to the 1080v11. I usually run in the shoes during recovery runs or easy runs. It's probably not the most cushioned shoe on the market but it's a great all-around shoe. I plan to add the Novablast 2 for those type of runs in the future if it's also a comfortable shoe. 

For long runs I prefer to use the Endorphin Speed 2. Just an amazing shoes which fit my feet since day 1. Good stability and great bounce. My legs and knees don't feel any sort of pain during or after the runs. Though it's probably due to my warm up and stretching afterwards (and stretching on rest days). I recommend getting a foam roller and a yoga mat to practice some stretching exercises after your runs. New shoes wont necessarily save you from injuries! ;)
[h7eq6sl] (score 2, diepte 0) If you liked running with the Ghost 10, why not try the 13 (or newer 14) and see how that works for you? That's already a fairly heavily cushioned shoe and I've been using it on long runs of 20km+ for ages. You mentioned stability, which would then be the Adrenaline if you stick with Brooks, but you should really try to get a gait analysis at a specialty running store before you make that decision. It sounds like your current shoe is probably just completely dead at this point, but not necessarily that you need a very heavily padded shoe like a Glycerin. Try on a few different pairs at a running shoe store and see how they feel. Probably any new shoe will feel like a padded dream compared to an old beat-up one.
[h7eqkag] (score 2, diepte 1 OP) Thanks for your reply, I got on well with the ghosts for years, but after buying the Rebel V2’s it made me realise there’s softer & lighter shoes out there now than the ghost’s. I really like the feel of the Rebel’s I just feel as though I would want something slightly more stable than them which was leaning me towards the Novablasts as my long run shoes. Also the issue of the knee pain, not sure if it’s from a worn out shoe or whether it’s from such a high drop. What do you think of Novablast 2’s as a long run/bit of a recovery shoe for my case?
[h7hbu1f] (score 2, diepte 2) No experience with them myself, so I couldn't give you an informed opinion beyond what I've read online (mostly all positive btw). Ultimately, it's really just what feels right for you but you've done the right thing in swapping out your older shoes anyway. There's a very high probability that the knee pain was caused by a broken-down midsole (which you'd never be able to visually see), more so than the high drop. I've made the mistake before of pushing a shoe too long because the parts I could see all looked fine. But with cushioning/midsole worn away, it did a number on my knees... the issues went away almost as soon as I got new shoes.
[h7j2zew] (score 2, diepte 3 OP) Thanks very much, sounds like I did the right thing retiring the Brooks! Probably nothing wrong with the drop for me, purely just worn out shoes
[h7et8zh] (score 2, diepte 0) How about looking into Mizuno? Wave Rider series are very comfy shoes for the everyday run/longrun. Lots of stability and cushioning IMO. I have fractured both legs at separate times during soccer and other fun stuff, so I am somewhat picky about my shoes. I am 73kg and running +/- 25 km a week for now. Looking to ramp up my numbers tho :)
[h7eul5y] (score 2, diepte 1 OP) Will have a look at Mizuno never really even given them a thought before, might also have a look at puma now they’re up & running again.
[h7eurip] (score 2, diepte 2) Yes do that! Mizuno dont get enough love on this sub, Not really sure why. Keep us posted about what you decide on.
[h7ewub7] (score 2, diepte 3 OP) Thanks I will do, I’ve read reviews of the ghost 14’s and people have said they have gotten more & more cushioned every year and I’m still on the ghost 10’s, so I might just transition over to the glycerin 19’s for the slightly lower drop and bit more cushioning. Then I will have a long run & recovery shoe in one possibly. The Novablast 2’s still interest me and so do the 1080’s. I just like with Brooks you get 90 days to wear the shoes in and you can still return them, can’t beat that!
[h7f16ei] (score 2, diepte 3 OP) Thanks I’ve been reading some reviews on runrepeat and it sounds like the novablasts are the right choice for me. Going to go through with them I think
[h7f355h] (score 2, diepte 4) You might want to go for the nova 2, the nova 1 was notoriously unstable.
[h7f3vhw] (score 2, diepte 5 OP) Thats exactly what I’m planning to do, thanks very much for your comment
[h7f3xqe] (score 2, diepte 4) They're a great choice and a fantastic shoe. I have 570km on mine and they aren't showing any signs of slowing down yet!
[h7piel0] (score 2, diepte 2) Both a well cushioned and versatile. The differences imo would be that the novablast is more of a 'fun shoe'. The 1080s also has a more pronounced rocker within the shoe which helps with efficiency when it comes to your long runs and recovery after sessions. The upper is a little softer in the 1080 - with more of a knit feel compared to a mesh upper in the novablasts. 

You really couldn't go wrong with either shoe - I love them both, although I'e just bought the novablasts so its hard to say if I have a preference as I'm onto my second pair of 1080s
[h7f2oni] (score 2, diepte 1 OP) Thanks for that I’ve never tried ASICS but currently leaning towards novablast 2’s out of all of the options. Will take a look at those before I go through with it…
[h7f2zzj] (score 2, diepte 1) 20 miles is 32.19 km
[h7f3uf4] (score 2, diepte 1 OP) Thanks for your comment. My weekly distance is about 32km. 14km was done on Sunday so that’s less than 50% of my weekly mileage, and my max HR is around 198 so sub 171 is a comfortable effort for me, nowhere near race condition so I do think I’m going about my training right, but you’ve got me with the stretching I’m guilty of doing none of it. My warmup and cool downs are a brisk walk at the start & end of my run and that’s it!
[h7hzmyv] (score 2, diepte 1) Thanks for the stretch link! This is very helpful!
[h7i5ea3] (score 2, diepte 2) I preach the gospel of Jay Johnson to all who will listen!
[h7f9uj0] (score 2, diepte 0) the new balance lerato is a great choice for long mileage. hard wearing outsole with a stable geometry not as extreme as the other racers, same fuelcell as the rebel v2 + a moderately aggressive plate shape.
[h7fcbnh] (score 2, diepte 0) I've been super happy with the Maxroad 5 for long runs. I know they're a Skechers brand, but they're seriously worth a look. Tons of cushion, but lighter weight than most shoes in the same class.
[h7fdyai] (score 2, diepte 0) Glycerine 19
[h7et9h9] (score 1, diepte 1) 25 km is 15.53 miles
[h7ewn3x] (score 1, diepte 1 OP) Thank you! How do the novablasts compare to the 1080’s? Purely want a cushioned long run shoe, have other shoes for tempos etc, which would you pick? Novablasts have got such a good rep this year which makes me want to try them…
[h7f2j0o] (score 1, diepte 1 OP) None of the above. 😂👍 the only thing I can say is that I’ve built up to it. Last week I did 11km as my long run with other training in between. Probably 17miles last week, this week 20 Mile week with the 14k
[h7f42va] (score 1, diepte 3 OP) It’s something I need to start doing definitely. Will start looking into it this week
[h7f44mj] (score 1, diepte 2) You're doing a 14k long run in a 20 mile week? That's almost half your weekly mileage in one run! That's way too much. U should be increasing the frequency of your runs instead and keep your long run to 25%-30% of your planned weekly mileage.
[h7f5kby] (score 1, diepte 3 OP) Monday Rest, Tuesday VO2Max intervals around 6-8km, Wednesday 3k recovery, Thursday or Friday is 5K Tempo, Saturday Short Recovery around 4k, Sunday Long Run 10-15k depending on how far I’ve gone in the week
[h7hzm7s] (score 1, diepte 1) Thanks for the stretch link!
[h7fe77l] (score 1, diepte 1 OP) Thanks for the reply, i saw Seth James Demoor praise them a lot they seem really great, I've gone for the Sister version of the Asics Novablast 2's! They're my first time trying Asics so will be interesting to test them out, had huge hype! Seem similar-ish shoes... Thanks so much.
[h7feeux] (score 1, diepte 1 OP) Thanks for your reply! This was a tight battle with the Novablast 2's. I've bought the Asics to test out, if I don't get on well with them then I will be going for the Glycerin's. Reading reviews on runrepeat swung it for me to go to the Asics finally
[h7j2wrx] (score 1, diepte 1 OP) Thanks for your comment advice taken onboard! Appreciate it
[h7f13yh] (score 0, diepte 2) The Novablast is a significantly better shoe.

=== THREAD 17h0w41 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2023-10-26  SCORE: 24  REACTIES: 34
TITEL: How many of you run in orthotics and what issue did they fix for you?
POST (source_id=post):
Having some recurring calf issues and looking to it sorted out once and for all

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k6k7koo] (score 7, diepte 0) Knee pain, and shin splints.
[k6lvwds] (score 7, diepte 2) More sustainable and probably more fun yes. But easier ? And cheaper than 40 bucks you replace once every few years?
[k6la8rd] (score 7, diepte 0) Weirdly high arches.  I'm in my 40s, have been through pregnancy, and when my wet feet hit the ground, my footprint does not have a piece connecting the heel and the ball/toes.  Custom orthotics are a godsend for preventing stress fractures.
[k6l1pn3] (score 4, diepte 0) I've had a few instances of post-tib tendonopathy, and I find using an off-the-shelf insole just gives my ankle that bit more support. It allows me to get running more, sooner. I'm doing this with a physiotherapist guidance, but it was actually my suggestion, his thought was if it feels good then use it. Once I no longer have any symptoms and am back to my normal volume etc and gently ween myself off them.    


I'd potentially also just use them for longer runs and events regardless of my post-tib symptoms now. I'm not getting any younger (40yrs) and that tendon is just a recurring issue for me the last few years. I actually really like the feel my Endorphin Pro 3 with the insoles, and I recently ran a 34km trail race in the Tecton X with the insoles.
[k6kk2eu] (score 3, diepte 1) shin splits because supination?
[k6kn8l0] (score 2, diepte 2) Pes planus and overpronation. No suppination.
[k6lergm] (score 2, diepte 1) Address your underlying muscle issues.  Far easier and cheaper.
[k6mf6n3] (score 2, diepte 4) I wouldn't necessarily say that, you're still using your intrinsic foot muscles even with orthotics. Orthotics just aid in distributing the forces associated with running more easily. Anecdotally speaking I tore my posterior tibial tendon in my left foot several years ago running collegiality and orthotics have been a huge contributor to me being able to run again. I still also incorporate regular strength training 5-6 x a week with running which has also helped with my overall stability. That being said I think it completely depends on the person and I do believe that most podiatrists and even physical therapists tend to over-prescribe them to people who don't need them in the first place.
[k6ncx8p] (score 2, diepte 3) 40 bucks?! I wish... I had cheap (around 90 USD) orthotics before and they hardly helped. My current ones are made by someone specialised in runners, and they are in a league of their own when it comes to support, and price (around 250usd).
[k6kqypu] (score 2, diepte 0) I'm thinking about starting and wondering whether orthotics or stable shoe would be better for my overpronating flat feet. my shoe dealer says stable shoes 😅
[k6ocxdu] (score 2, diepte 1) same. i use the superfeet running insole and it’s worked wonders for me. my podiatrist more or less instructed me to keep strengthening the muscles around the area but said i would continue to need the support since it’s such a reoccurring issue.
[k6k6pzf] (score 1, diepte 0) ✋. 

Helps with my lower back.
[k6rab6a] (score 1, diepte 4) Yeah, custom orthotics are pretty expensive, but have the most evidence based research behind them currently of working. I think they're worth it in my opinion if it gets people back to running again which isn't the norm nowadays with the prevalence of chronic diseases/obesity. Of course orthotics just like running/rotating through different drop shoes should not substitute regular strength training. There's a fine balance...
[k6ncome] (score 1, diepte 2) Tried that of course. For 2 years. Did not work and I was limited to 10k runs because of it. Orthotics allow me to run more v and further. And fun fact: because I can run more now, my feet became way stronger and I can do 20k runs without orthotics if I need to now.
[k6ku9k6] (score 1, diepte 0) Overpronation, I find that they help :)
[k6l2yet] (score 1, diepte 0) I wear an insert in one shoe due to a limb-length disparity of a \~1cm. It definitely helps with my gait and stride, but my calf was sore for months while my body adjusted to the insert.
[k6l5v8c] (score 1, diepte 0) Long runs and speed work yeah, over pronation causing shin splints. General walking around or recovery runs I don’t tend to wear them
[k6m9uuw] (score 1, diepte 0) One nearly fully collapsed arch — wear superfeet to help save my feet. Haven’t had an issue in many years. Worth it.
[k6mcga3] (score 1, diepte 0) Overpronation, knee pain, shin splints

i've run with orthotics for the past 6 years and its been life changing
[kj790vt] (score 1, diepte 1) Ive been dealing with the same thing, as I have an inch difference between my legs. how long did it take you to notice a difference using the orthotics? my podiatrist wants me to get them & im a month out from running but am unsure
[kj9gl7y] (score 1, diepte 2) instantly
[kjc5knu] (score 1, diepte 3) and they're personalized ones? not storebought?
[kjc9r9w] (score 1, diepte 4) yea custom made for my needs
[k6n4nb1] (score 1, diepte 0) This year I had severe pain on the outside of my left foot after a race, it was initially suspected as a metatarsal stress fracture but then was ruled out via 2 x-rays and a CT scan. I ended up with orthotics to relieve the stress/pain on the area to avoid getting injured again but was advised not to run in them by my doctor
[k6ndcvh] (score 1, diepte 0) Pronation.   Can't live without 'em.
[ka9iat9] (score 1, diepte 1) Same here. Is see Novablast in your bio. Work okay with orthotics? I have Clifton 8's and they have been fine, but looking to change it up.
[kaw83iy] (score 1, diepte 2) Yes!  I use orthotics in all runners and NBs are the most forgiving upper and last for that.  For some brands I size up 1/2, but not NBs.  Good luckemote:free\_emotes\_pack:feels\_good\_man
[k6nhn3z] (score 1, diepte 0) Overpronation caused all sorts of things. Haven't had issues since I got them (it's been 3 or 4 months) but I do have to remain careful. I'll probably add some strength, stability, and core work soon to help out.
[k6nzz2k] (score 1, diepte 0) I use mine to add a hint of stability to neutral
shoes. No particular issue.
[k6oh017] (score 1, diepte 0) Paid $200 for.mine, didn't notice a big change, my shoes and my technique were bad.
[k6pmp50] (score 1, diepte 0) Weirdly high arches! I used to have knee problems, ankle problems, shin splints, etc But to address it I didn't just rely on orthopedics, I also went to the physio that made me get rid of my heel striking, and started weight training and cross-training. Ever since the weight training (which was the last thing I added), I haven't gotten injured. A side effect of the orthopedics which I don't hear many people talk about is that they made me buy bigger shoes (since they accommodate my high arches I need to get more clearance on top) and having more room for my toes to sprawl has been so nice
[k6q0atk] (score 1, diepte 0) If you do invest in orthotics start with ProTech insoles for $40-50 don't go for the overpriced "custom" insoles from a podiatrist. They aren't custom and will cost $500+.
[k6lx350] (score 0, diepte 3) The ability to walk without pain is priceless.  Orthotics are nothing but a bandaid solution.
[k6kt463] (score -1, diepte 0) I‘ve gotten some to help with calf pain on one side where I pronate. I don‘t pronate on the other side. They kinda helped with the calf pain but in return fucked up my hip flexers and lower back. 
Right now I‘m unsure whether to use them or not since I‘m now struggling with another problem. 
In my case I think the solution is to strengthen the muscle imbalances which seem to be the cause of these issues rather than rely on a insole to fix a problem which then creates the next one. 

I would analyse your biomechanics and your running form first and and try to figure out if there is something wrong going on before getting insoles but I’m no pyhsio or anything in that regard so what do I know. Do what feels right

=== THREAD 4ni93b ===
SUBREDDIT: r/BarefootRunning
DATUM: 2016-06-10  SCORE: 4  REACTIES: 34
TITEL: Want to start barefoot walking, can't find shoes that fit my wide feet?
POST (source_id=post):
I want to transition into barefoot walking and then running, but I can't find any shoes that are flexible and wide enough to accommodate my gigantic feet. Whenever I wear stiff shoes that crunch my toes up I get burning, sharp pains running up my feet into my legs and I feel like the shoe is going to burst open.

When I was a teenager I always wore shoes in boy's sizes despite being a girl because women's shoes are too narrow for me. I'm a women's size 8 (men's 6.5) so my feet are average but I was measured at a D width.

I've tried the New Balance Minimus and almost every style from Altra. The Minimus is too tight around my arch and the sole is stiff. Altras are way too short and inflexible for me. I've been wearing Birkenstocks in regular (Wide width for women) but they'll still a little too inflexible and don't let my toes spread enough. 

I was thinking about ordering a pair of Nike Free Run 2s in a men's size because I've heard the toe box is pretty wide. Does anyone know about this Nike model?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d444r4r] (score 12, diepte 0) Seconding Vivobarefoot, but how about ... y'know ... barefoot?
[d44bpwn] (score 9, diepte 1) This title is fucking hilarious.
[d44z6bo] (score 6, diepte 2) guys how can i spend $200 on shoes that mimic not wearing shoes
[d448guz] (score 5, diepte 0) I believe [Lems Shoes](http://www.lemsshoes.com/) are quite wide in the toe box. I don't own any of them myself, but it might be a good place to start.

Additionally my SO also had an similar issue simply because she had been buying shoe sizes too small for her. Try to choose a shoe size such that the widest part of your foot is at the widest part of the shoe. Judging your shoe size based on how close your toes are to the front edge of the shoe really doesn't work well, especially if your feet are of the wider sort, with short toes. Here's a [more thorough guide](http://www.munroshoes.com/customer-care/fit-your-foot) if you're interested.
[d444jnh] (score 4, diepte 0) http://www.softstarshoes.com/ - you can send them a tracing of your feet plus they already have a lot of wide sizes
[d44mxui] (score 3, diepte 7) Yeah I've found firstly most attendants have no real idea what they are doing, and secondly they tend to ignore width unless you specifically ask them for wide. Even then, there's usually nothing available, or "wide" equals "not a 12 year old's foot". The third factor ignored and this is my problem, is that the natural shape of my foot should be much wider at the toes than at the ball of the foot and the Brannock device only measures at the ball of the foot.
[d448quz] (score 3, diepte 0) > Want to start barefoot walking, can't find shoes that fit my wide feet? 

Um, have you considered not looking for shoes? I mean, the word barefoot does imply that your feet are bare.

If you absolutely need something on your feet, and can't find a minimalist shoe that fits, you might want to look at sandals. In many cases, you can send them a trace of your foot so a custom-sized sandal can be made for you.
[d44jexu] (score 3, diepte 1) > word barefoot does imply that your feet are bare

That's not how this works!  That's not how ANY of this works!
[d44eos5] (score 3, diepte 0) I have a similar problem.. I've been wanting to try skiing, but I can't find a snowboard that fits.
[d44re69] (score 3, diepte 0) I second Softstar; also, Lem's are nice and wide and excellent quality!
[d4517ek] (score 3, diepte 0) Are you open to hauraches? Particularly when walking, they aren't sure she big transition, since you've probably work sandals before. I'm new to barefoot/minimalism, but I love my Jerusalem Cruisers from Shamma, particularly because they give my wide forefoot and  toes plenty of room.
[d454xpu] (score 3, diepte 0) People are being assholes to you for saying you want to walk barefoot while asking for a shoe recommendation.  I agree that the word barefoot is out of place here and that you should use the word minimalist but I don't think they need to be such assholes about it.

For shoe recommendation I'd add myself to the list of those mentioning Vivobarefoot.  The shoes aren't cheap but they last and they are a good company.  I go barefoot everywhere I can.  But in stores and at work I wear vivos.
[d446o89] (score 2, diepte 1) If OP is concerned with width Vivo may no longer be the way to go. The newer models, beginning with the Ra/Gobi II, are significantly narrower than what they put out a few years ago. 

For forefoot width, Vivos now run 3-4 sizes narrower than previous releases.
[d44f6yw] (score 2, diepte 3) Brannock devices also measure your foot size. Not your shoe size. Usually shoes are a half to full size bigger.
[d44fg72] (score 2, diepte 4) We'll, the idea is that if you're a size 8 the manufacturer will make a shoe that fits your foot, and call it a size 8 too. Unfortunately you can't control what a manufacturer does, and because of last designs and loose manufacturing tolerances we get listed sizes that don't often conform to real shoe sizes. Sometimes a specific shoe will be a perfect 5/6/7 but be over- or undersized in other sizes. 

But since the 1920s the Brannock device has given accurate foot sizes.
[d4f7abs] (score 2, diepte 2) FWIW, I measure as a 4 but feel most comfortable in a 5.5.
[d454xgd] (score 2, diepte 1 OP) I want a pair of Lems but they're sold out in my size right now.
[d45y47w] (score 2, diepte 0) Isn't D a normal width ?

My experience : My foot length is Male US 8.5, but  because i have a wide and bulky feet, normally i had to go between 2 to 2.5 size up in 'normal shoes' and i have tried the following :

Vibram Five Finger : i can wear 8.5 or even go down to 8 on some model, width is not a problem as it expands to whatever your feet width is.  
Vivo Barefoot Evo and Neo : i need to go 0.5 size up.  Width is no problem, but it tends to be a bit short.  
Inov-8 : I need to go up to 1 size up.  it is quite narrow.  
SoftStar : well .. it is almost tailor made, and can have width by request, so no problem there, but it is quite expensive.  
Xero : i'm size 10 by their measurement.  It is quite narrow, not a problem, but you feet may spill over to the side if your feet is too wide.  
Nike free 3 : go 1.5 size up.  very very narrow, i lost pinky toe nail several times on this shoes.  
Sockwa : 1 size up, length issue, width no problem.
[d443v8q] (score 1, diepte 0) I think you should try [Vivobarefoot](http://www.vivobarefoot.com). Super flexible, wide, and comfy. Models for both casual, running, and more.
[d4453ij] (score 1, diepte 0) Vivobarefoot are pretty wide. However, since I've been wearing minimalist for 4 years my feet have gotten more muscular (more volume to them), and I find most vivobarefoot to be a little "short" in the midfoot (height-wise). I wear Vivobarefoot stealth 2's, but even those are borderline. Everything else I tried had that problem of tightness in the midfoot for me. [Here was my review post about 4 pairs of Vivos](https://www.reddit.com/r/BarefootRunning/comments/4ddckx/minireview_of_4_pairs_of_vivobarefoot_shoes/). I wore lots of NB Minimus when I first started wearing minimalist shoes, but at this point they're to tight for me as well.

This summer I'm mostly wearing Xeroshoes Z-Trail sandals and I like them a lot. 

A couple of pictures:

https://i.imgur.com/IcH4cie.jpg

https://i.imgur.com/864fhZU.jpg


Also I've tried SoftStar shoes in Wide (the Dash RunAmoc), and they were good too, but they're pretty expensive for what they are imo. They don't win any big points in style either. Size wise they're certainly wide enough.
[d445l93] (score 1, diepte 0) Definitely consider our [Core](http://skora.cc/allcores). My pair is coming up on 750 running miles and they've been my everyday shoe for the better part of a year as well.
[d459l6b] (score 1, diepte 1) I recently tried the Skora Phase and found it slightly narrow for my feet. They were nearly comfortable, but after running in them a little bit I started to have discomfort in my inner and outer toes from the pinching. I usually wear Lems, which seem to be slightly wider and very comfortable for me. Please consider making a wider version of your shoes, and maybe taking inspiration from the Lems last (larger toebox). You seem to have an amazing shoe here, I envy everyone who can wear it comfortably.
[d45bunw] (score 1, diepte 2) Do you think going up half a size would have helped?

I do typically prefer to Core for my wider feet, FYI. Phase is probably our most narrow. They're all built on the same last, but upper differences make a difference.
[d446psd] (score 1, diepte 0) Not a zero drop shoe, but for walking around these are by far the most comfortable pair I have tried.  Make sure to get your size in wide.

https://smile.amazon.com/gp/product/B015XCR174/ref=oh_aui_detailpage_o01_s01?ie=UTF8&psc=1
[d448sx8] (score 1, diepte 1 OP) I was wearing an 8 for a long time, and then for about a year I decided I was a size 7 because of a shoe store employee's very, very inaccurate eyeballing of my shoe size. I was measured with a Brannock device recently at a size 8, I don't know how accurate that is though.

I have very strangely shaped feet. My toes are incredibly long for a wide-footed person, and nearly the same length save for my fourth and fifth (pinky toe), which are shorter than the first three. Sometimes even going an entire size up (a women's 9) is more comfortable than even a half-size to keep my toes from being scrunched up.
[d4497ja] (score 1, diepte 2) > I was measured with a Brannock device recently at a size 8, I don't know how accurate that is though.

Brannock devices are very accurate, but it's the style, shape and manufacturing peculiarities of individual shoe manufacturers that makes their sizing differ from 'real' sizes.
[d44g4bw] (score 1, diepte 5) I think there's probably been a "creep" over time too. I worked in a specialist shoe store many years ago and in training they told us to always go at least half a size bigger than the reading. Probably because manufacturers have slowly shifted sizes and lasts over time.
[d44i5cg] (score 1, diepte 6) That could also just be a rule-of-thumb to split the difference between foot sizes early in the day and late in the day when feet swell. 

The first time as a customer I paid attention to what the Brannock device said was the first time I realized that for so many years salesmen were ignoring the wideness of my feet and shoving them into shoes they had in stock that always ended up making me uncomfortable. (And what did I know - ever since I was a kid foot discomfort of some kind or other was utterly normal.) But the first time I put on shoes **that actually fit me** was a revelation - and sad to say it didn't happen until I was nineteen. 

Starting with Cub Scouts I'd backpacked frequently and at the end of the day I'd have crippling pain in my feet and just assumed it was somehow normal. When I finally realized I had extra wide feet thanks to reading the Brannock I did some pre-internet research and ended up sending foot tracings and multiple-point foot measurements to Limmer Boots in New Hampshire and eventually got back the heaviest - and most comfortable - full steel shank leather boots I'd ever worn.
[d455hmx] (score 1, diepte 1) I want to get into roller derby but I can't find a blindfold that fits.
[d454z77] (score 1, diepte 1 OP) Yes, I was considering going for the basic Xero Shoes or trying a Luna sandal. I don't like the idea of having a thick toe post though.
[d458f1i] (score 1, diepte 2) Yeah, toe post is a concern. The nylon on mine seems pretty mellow, but well see with long term use how I like it.
[d468i9o] (score 1, diepte 3 OP) That's good. I would rather a small nylon string than a giant rubber or thick fabric toe post.
[d46evjb] (score 1, diepte 4) It is a strip that is folded, so it tucks between your toes like a V, but the nylon is quite thin and flexible, not a stiff nylon like the straps themselves. They've obviously customized that part of the sandal for comfort.
[d468h0t] (score 1, diepte 1 OP) In US women's sizes, D width is considered a Wide width. D is normal width for US men's sizes. B is considered normal for women's shoes, but narrow for men's shoes. 

I'm not a full D width, but my midfoot and toes are on the wide size for women's shoes so I like to get men's shoes because they're slightly wider. Still need to size up a half or full size sometimes. My heel is very slim so slippage is always a problem with closed back shoes.

Very extensive recommendations, thank you! 

I was looking into the Nike Free Run 2. Was going to order a pair of men's size 7s (women's 8.5) because people complain they're too wide, good sign for me.

=== THREAD ggjmvx ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2020-05-09  SCORE: 10  REACTIES: 33
TITEL: Which shoes did you buy with the intent of making them your “daily trainers “ but ended up giving you buyer’s remorse because they were horrible .
POST (source_id=post):
Did things  just go down-hill after you tested them out? 

For me, a pair of epic react flyknits from 2016 that had a  sock-like apparatus . I remember they felt so good in the store, and then after a week I had cuts all over my heel.  I Returned for saucony zealot iso and my feet couldn’t  have been happier.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[fq2jt1x] (score 8, diepte 0) Hoka Bondi. Not Hoka’s fault, I went from the much firmer 10mm Nike Epic React to the 4mm marshmallow that is the Hoka Bondi, and decided that their maiden voyage would be a scheduled 8 mile marathon pace tempo run.
 
A lesson was learned that day.
[fq1tczw] (score 5, diepte 0) Asics Kayano 25s.

Second time Asics has done this to me. I bought the 25s because I loved the 22s-24s so much, and they were horrible.

No plan on going back to Asics any time soon.
[fq1vd7w] (score 4, diepte 0) Hoka One One Clifton 6. 

People rave about those shoes and I really wanted to like them, but the last was in such a weird angle for my foot that I never got comfortable in them. 

I had a lot of problems with pain on my instep from landing over some of the rubber on the edge. It’s probably less of a problem with the shoe overall and more of a problem with how it fit me.
[fq5irab] (score 4, diepte 2) Clifton is a firmer shoe, the Bondi is a sofa cushion, so the move from a firm Nike to a pillowy Hoka made for an awful run.
[fq1p3yf] (score 3, diepte 0) Skechers Gorun ride 8 hyper. I was excited to try due to all the great reviews of the 7 and the "hype" around the 8 going to hyperburst. I gave up on them at about 50 miles. Just way to firm for me (and I like firm shoes). 
Will still give hyperburst another try. Awaiting the release of the razor 3 flow tr this fall.
[fq1ryaa] (score 3, diepte 0) Brooks launch 5.  Based on specs and store feel I thought I'd like it.  I have to force myself to use them now.
[fq29592] (score 3, diepte 1) Agreed, I used them all the way back to the 15’s, and that will be my last pair for a long time. 

They were heavy and ran about 1/2”-3/4” longer than every other pair before it.

I still got miles out of them, but never enjoyed it.
[fq1vcmf] (score 3, diepte 0) Kinvara 8 (or was it 9?). Made them walking around shoes and went back to the Epic React Flyknit, which I still love.
Also Adidas Ultraboost.  Again, fine for walking around, but when I run in them my arches ache terribly. Pureboosts and Bostons are fine, but the Ultraboosts tear me up for some reason.
[fq2nhuh] (score 3, diepte 0) Too many to remember (so many Hokas) but the one that sticks out is the Pearl Izumi EM Road M 2. Worst shoe I ever bought.
[fq2yttp] (score 3, diepte 0) Second on the Epic Reacts. They are okay for short recovery runs but for some reason my knees hate them.
[fq35emg] (score 3, diepte 0) Pegasus 36 not a forgiving ride at all and gave me knee pain.  Ultraboost so soft but too soft for running.  Infinity React were pretty nice but felt a bit clunky with the wide forefoot.  None of these were horrible, just not what I would want as daily trainers.
[fq42kdg] (score 3, diepte 0) Brooks Levitate 2. All the reviews I read said they weren’t good, yet I bought them because they were on sale. Major regret.
[fq893hs] (score 2, diepte 1) I would have to agree with you on the GRR8, was disappointed in how firm it was compared to all the other shoes with hyperburst & the 7. I actually retired it a lil sooner than you like barely 20miles. Plus the lacing design sucked for me, I couldn't get it to have comfortable hold for me.

 Also, regret the NB beacon 2. It didn't do anything for me and just felt flat n my feet was slapping the ground for every run.
[fq3cro3] (score 2, diepte 1) That rubber edge is why I will never try Hoka again. Seems to be a common issue with lots of runners yet they haven’t addressed it in any of their models. Strange.
[fqabb8g] (score 2, diepte 2) I have this problem too, but I find it only happens after heavy use for a while, and only certain shoes of Hoka.. it seems like a production error? Because I had something similar with another pair of shoes I love, I wore them out, replaced with a new pair that suddenly has a small plastic thing on the heel causing friction blisters on my foot. But I’ve been using the same shoe for years, so I don’t understand why this specific pair causes it.

My workaround for this is to use sports tape on the skin area where I’m prone to blistering
[fqb0va4] (score 2, diepte 1) Same for me! Determined to enjoy them (the weird instep thing is less prominent than it was), but was definitely uncomfortable for a few runs.
[fq1y4y2] (score 2, diepte 0) Hoka Clifton 5 - just felt weird.
Nike Pegasus 35 - felt like brick on my feet
Reebok Floatride Run v1 - upper so loose my feet were falling over the sides
NB 1080 v8/9/10 - 8 was meh, 9 was better and 10 better still. Just not very exciting or as cushioned as I would like.
Reebok Floatride Run v2 - get an odd pain in the ball of my left foot, no idea why.
Reebok Floatride Harmony 3.0 - loved the Floatride Energy, these just aren’t comfortable and are just heavy and stiff.
[fq1yoe1] (score 2, diepte 0) Pegasus 36- I bought, ran, exchanged sizes- repeated this like three time could not find a size that fit and just didn't enjoy the run experience.
[fq64xcg] (score 2, diepte 2) Most running stores will let you exchange after a few runs, and if you buy directly from Nike you can return shoes for any reason for 30 days, even if they're used.
[fq8a61y] (score 1, diepte 2) I have the nb beacon v3 on my want to try list. Never ran beacon, had 1080v10 and really like how they felt. Unfortunately, I had blister issues with the knit upper and swapped them out for something different.
[g7pxs2s] (score 1, diepte 1) What do you run in now?
[g7pxzhc] (score 1, diepte 2) I have Altra Torin 4, Reebok Floatride Forever, and Kinvara 11
[fq5i53u] (score 1, diepte 1) They let you return them after running in them?
[fqat58b] (score 1, diepte 3) Nice one
[fq702z0] (score 1, diepte 2) Yes for all of them basically told them it didn't fit and I wanted exchange.
[fqat2t8] (score 1, diepte 3) Interesting, I was under the impression that you could only return unused
[fqc4gtt] (score 1, diepte 4) Ran approx 2 days in each of them so like 15-20 miles in each when I returned they didn't care at all. I made sure to check the return policy too...
[fq5i1t7] (score 1, diepte 1) Forgive me for asking, but what lesson was learned? Did you just not like the cushion of the Hokas? I'm looking to replace my Pegasus 34s for some Hoka Cliftons
[fq3b4f9] (score 1, diepte 1) I loved those Pearl Izumis. Not fast but found them to be a good training shoe. Got 700km out of them and now they are a yard shoe.  


Why did you hate them?
[fq3cfm7] (score 1, diepte 2) A bit too stiff for me, but more than that they cut the living heck out of my arches. Tried wearing them down over 50-odd miles, but the problem persisted. Had to give up on them. Shame since I liked the other PIs I had run in (still wish they kept the running line).
[fq3bsai] (score 1, diepte 0) Hoka Clifton 1.  I actually enjoyed my first run in them, so much that I immediately ordered a second pair.  But the toe box didn't quite agree with my feet, and the more I ran in them the more issues I had.  I ended up selling the second pair, and the first gets used vary sparingly.

Interestingly, the similarly-specced speedgoats have been great for me.  

Kinda the opposite was the New Balance Propel.  I bought a pair because they were really cheap and well reviewed.  I hated the way they fit and nearly returned them, though I liked the midsole and seemed to run pretty efficiently in them (if a bit slow).  I ran in them occasionally, then they sat in the closet and I kinda forgot about them.  Few months later I found them again, tried them on, and they felt a lot better!  Now they're my favorite easy day shoe.
[fq3utxq] (score 1, diepte 1) Propel were awful for me. Too loose and too soft. They gave me calf/ankle issues
[fq5w4y0] (score 1, diepte 0) I see a lot of people commenting Hokas here, interestingly for me, I know that any of the Hoka shoe models I try feels good for me. Almost any shoe feels okay or me, but I noticed I have a preference for light and cushion-y shoes for my basic staple runs.

My worst shoe buy though, was the very new adidas SL20. I really WANT to like adidas shoes, a lot of fast runners in my group swear to adidas, plus the continental outsole has a deadlock grip on the road, completely unmatched by any other shoe. The looks and fit is nice as well. But.. it feels like there’s something hard in the outer edge of the midsole, extending up on the midfoot upper, that unfortunately rubs very hard against my peroneus tendons and as a result, after using them for longer threshold runs, I developed a peroneal tendonitis. I recovered fast because I early recognized the sensation that something “felt off” and took one week with complete rest. But once I stick my feet in those shoes, it starts to hurt right away.. shame though because I wanted to like those shoes and the grip they have is the best I’ve ever felt :(
[fqepzs8] (score 1, diepte 0) Altra Escalante 1.  They were insanely comfortable to put on and walk around, but the upper was so soft that I felt like I would turn my ankle going around bends.  Also the zero drop made my legs work harder for the same speed as my other shoes, but I realize that depends on the person.

