# Label-batch batch_0026

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
Schrijf het resultaat naar `batch_0026.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 14673au, 2z7c0y, 1dchjnk).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 14673au ===
SUBREDDIT: r/goodyearwelt
DATUM: 2023-06-10  SCORE: 40  REACTIES: 28
TITEL: Wolverine 1000 Mile MocToe - My Journey + Mistakes
POST (source_id=post):
Hi GYW, 

Its my routine boot care day and I was reminiscing about my first pair of GYW boots, so I thought it would be fun to show an example of how you can mess up every single thing, break all the rules of boot purchasing and care we've learned here in GYW... and still end up with a pretty great pair of boots. 

I started my journey back in early 2018, I was a 22 year old Produce manager at a grocery store and a buddy of mine was going on and on about how Wolverine 1000 mile boots were the greatest boots ever made. It peaked my interest so I did some **hardcore** research on these boots (2 google searches, and a scroll through their website). I was sold. But fuck, $400? That's a whole paycheck for me. I had moved back in with my parents after a breakup and had some disposable income but still..$400?? So, I put the idea on the back burner, and then they consumed every thought I was having. 

Fast forward to March and I was at a Nordstrom's Rack with my mom just perusing the men's shoe department... lo and behold. There was a freaking pair of 1000 miles for $199.99. Pretty much half off! Not the ones I was originally looking at but still, cant beat half price.

Now, you have to remember, I knew NOTHING about GYW/Heritage boots. I had some Timberland hiking boots from boy scouts but nothing about this side of the boot world. 

I was a 10.5 in running shoes, and these were a 10.5....perfect. I got them. Used a generic Instagram filter and showed the world.

https://imgur.com/dnAYBzt
https://imgur.com/a/fIRmgYN

After the first week of wearing these I was bummed, crushed, defeated, full of regret, because my feet were fucking swimming in them, I couldn't tighten the laces enough to keep my feet in place and they were getting scratched as all hell (which sucked because I just spent 200 hard earned dollars on them and I wanted them to look nice). I also have *atrocious* arches so the lack of any support in these things absolutely killed my feet and knees. (over the years I discovered I'm actually a 9-9.5D depending on brand)

Since I had bad knees I decided to say screw it and throw a set of SuperFeet green insoles in them that I had laying around and ya know what, it helped. Gave me about 1/4-1/2" within the boot that helped me fill it out a bit. Night and Day difference. They no longer hurt to wear. I rolled with this for a couple months but was still really frustrated about how they were creasing and folding in weird places. https://imgur.com/T0RGgLc

A couple months later I stumbled upon a reddit post that mentioned you're supposed to condition your boots to help keep the leather moisturized and extend the life...And that was the extent of the research I did. I proceeded to go on amazon and bought Doc Martens Wonderbalm and a bottle of Lexol from amazon recommended. I proceeded to condition the ever loving fuck out of these boots. When I say I over did it, I mean there was a time I was doing it after almost *every wear*.

Later, I found another reddit post that basically said "hey there speed racer slow the hell down, only do it every six months or so unless you're abusing the hell out of them in super dry conditions". I'm a PNW guy, so that didn't apply to me... and I slowed down a bit (albeit not as much as I should have).  

Its now 2023, I've since found r/goodyearwelt and other leather boot subreddits. Purchased Whites, Chippewas, Iron Rangers, and various other leather shoes/boots. I have invested in brushes and other polishes and creams too. I still wear these boots semi-regularly with that same set of SuperFeet insoles and a new set of laces. They hold a special place in my heart as the pair of boots that led me down a path of boot discovery and obsession. Although a cocaine addiction might have been cheaper....

I love them, they're not perfect, they're by far not the greatest boot ever made, but they're mine and I think they still look pretty darn nice. You can see in places where the hard insole has stretched out the toe box and creased in weird ways, but to hell with it. I think the patina and creasing makes them look loved.
https://imgur.com/DQsUWod

Shout out to all you nice folks out here on GYW that consistently and repeatedly answer the same conditioning questions, creasing questions and sizing questions out there from the noobs that are just getting in to this expensive lifestyle. I wouldn't be here without some of you guys.

https://imgur.com/kqFEmyH

If you made it this far, thanks for reading. I was just having some fun looking back at all my mistakes and naiveties.

Album I took today: https://imgur.com/gallery/Lkv3DUM

Also, what are some mistakes you made early on in your boot adventures?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jnqi6b9] (score 7, diepte 0) There’s something about the 1000 miles that are so appealing. 

There’s so many things to nitpick, but at the end of the day, you get great leather, decent soles, they’re light and comfortable. They usually age beautifully. 

When they get it right, QC is fine. 

The frustrating thing about them, the nitpicky things could be fixed for not a lot of money.  The heel rand on the 270 welts, the heel counter material and maybe the insole…those are my only real beefs with them. 

They’re like the top end of Mid level imo. I’ve got a few pairs and another pair in the mail…figured I’d try the 360 welt ones with a rubber sole. (Supposedly made by AE) 

I prefer them to red wings and the 1000 mile on sale is an amazing value.
[jnoqvrh] (score 6, diepte 0) I love my Wolverine 1000 miles. I have 3 different styles..all with leather soles. Awesome. I also have Redwings, Thursday's and Grant Stones...each have their place and purpose.
[jnorbpx] (score 5, diepte 1 OP) Thursday's are on my list next I think. I'd like a black daily wear boot. I'm torn between a pair of 8084 black IR's or the Thursday Captains.
[jnqhpiy] (score 5, diepte 0) I feel ya, bro. Here's what I've learned (after pretty much getting everything wrong). First: find your Brannock size. Second, size your foot to ball of foot (and make sure your toes don't hit the end, but that's not a problem with Wolverine). Fit first!

But after that, it's materials and craftsmanship, and you could do worse than 1000 miles!

Thanks for sharing the journey.
[jnos822] (score 3, diepte 2) Captains are great, and I love Red Wings, but IR and captains are completely different, in build, silhouette, weight, leather, and IR are like 1.75x the price of Captains. The Captain is more sleek and modern (fully capable of fitting in business casual) whereas the IR is more bulky and classic Americana, and not very business casual IMO. Either way, you cant go wrong.
[jnosoz1] (score 3, diepte 3 OP) The captains being more business casual (and price) is the reason I'm leaning towards them. I just also love my IR, but agree they're not business worthy.
[jnoxb37] (score 3, diepte 3) As a Captain owner, they're beautiful. The rubber for the sole isn't exactly primo, but it's still good stuff. Frankly, you could buy a Captain, have 150 bucks left over and save that for a pair of IRs later.
[jnp2qe8] (score 3, diepte 5) Ordered em directly from Thursday Boot Company as a birthday present for myself. Full time from clicking "Buy" to having them on my feet took less than a week IIRC because they ship from NYC and I live in Delaware. They come in a black box all pretty looking with a strong "new boots" smell. 

As for the actual act of ordering, they have that cool little function where you start punching in your address, and it autocompletes it like google maps so neither of you can fuck up the address really. You should get the usual choice of 2-day shipping or regular. Honestly, unless you live at the other end of the country and need your boots pronto, just go with the regular shipping. Then you punch in your CC info, and bam! You've bought from TBC. They WILL send you emails, but only shipping updates and when they drop new products. That's it. They're the simplest, easiest MFs I've ever ordered from. They don't force you to set up an account, they don't spam you into the next life, they just do what they say they're gonna do and ship you your shit. 

This said, if they do fuck something up, the TBC reddit is full of people saying how solid their customer service is. I've never had a problem, but they're fucking good at what they do.

Pro tip: If you get the black caps, and have normal (not wide or slim) feet, go half a size down from your Brannock. That's what I did. I'm an 8 on the brannock, wear an 8 in everything except Converse, got 7.5 black Caps, and they fit good. 

Pro tip 2: Your heels will murder you until those boots break in. You won't lose skin, but your heels might get a bit red.
[jnoyd5p] (score 3, diepte 0) I'm lucky, I guess. My work as a power plant manager is perfect for Redwings, GS, or TBC. All fir the bill for me. Just returned from a Turbine conference. Took 3 pairs of boots for the week. 😎
[jnp20cn] (score 3, diepte 0) Natural CXL Captains are back in stock BTW, and don't sleep on the Vangaurd #8 color...like I said all have a purpose and place.Redwing Moc's with wedge soles are like sneakers in my world.

Wolverine 1000 miles and TBC smooth leathers fit the business casual. But I can sneak the IR black and amber  harness in with nice dark denim and polo for business as well.
[jnqibcw] (score 3, diepte 1 OP) I've since learned my size thankfully! My newer boots have been fantastic. I just thought the journey was a funny story fully of mistakes and humor from a novice. 

I lucked out that these were only a size too big and was able to salvage them for many years of use. 

Appreciate you reading! I had fun writing it.
[jnqkpwe] (score 3, diepte 4) That’s a great deal.
[jnql19x] (score 3, diepte 5 OP) And they look pretty badass if I do say so myself. https://imgur.com/a/cwd8lu0
[jnp4oss] (score 2, diepte 5) I have really tried to love TBC company. I currently only have one pair. I have ordered and returned probably 6-7 pairs. I'm an older, short sticky dude, so the longer sleek boot design doesn't style well with me. Wider stockier boots do. So redwings, Gs's, wolverines, etc. Never had a problem with returns etc. With TBC. Always top notch.
[jnsw3q9] (score 2, diepte 3) Didn’t they discontinue the BLVD line, and are just clearing out the leftovers?
[jnpjvsi] (score 2, diepte 0) I’m so glad I realized my sizing was fucked up on a pair of desert boots rather than an actual nice pair. Props to you for still making them work though.
[jnqklhe] (score 2, diepte 3 OP) I'm from Spokane, WA where whites are from and there are a few stores around town where you can buy some of their pre made boots. I was able to get a pair of smokejumpers for $350 that fit me perfectly. They're not custom to my feet but they're damn good.
[jnql319] (score 2, diepte 6) Chonky indeed.
[job60lv] (score 2, diepte 0) Thanks for sharing good stuff! You will prolly help a lot of people.
[jnp01a9] (score 1, diepte 4 OP) Good info. I have so many boots/shoes on rotation right now that the rubber sole not being 10/10 isn't really a deal breaker to be honest. Maybe with my next bonus I'll snag a pair. How's the process for online ordering through them?
[jnqkh3g] (score 1, diepte 2) Wolverine makes the BLVD line. They’re on sale for like $80. 

Pretty sure they’re made in the same factory that TBC useds in Mexico, with the same lefarc leather…like, it’s likely the exact same boot as TBC with different lasts.

Edit. The foam insole/insert on the BLVD line isn’t built into the boot like Thursdays.
[jnszfv3] (score 1, diepte 4) Possibly. I don’t actually know. There’s still some available for cheap. 

I found it strange they even made them.  

Pretty sure it’s the same contract manufacturer Thursday uses though.
[jo6jckv] (score 1, diepte 4) Yes, discontinued. I bought a pair for $80 new from.Wolverine and immediately sold. Style and quality wasn't there. Was on par with TBC.
[jnpob3n] (score 1, diepte 1 OP) I bought a pair of Clark's DBs around this time as well but never made the connection that they were a size to big and just hated them. Also wasn't a massive fan of how they looked on me, not quite my style.
[jnqii46] (score 1, diepte 1 OP) I agree with everything you said. They're really a good fucking boot. Their biggest issue is the price vs quality. If they were around 250-300 I think they'd be a steal. But nearing the 400$ price range brands like whites and red wing are far better quality per dollar.
[jnqjwqi] (score 1, diepte 2) Whites are pushing $700 now. 

The closest comparable is red wings, imo. Red wings are a pretty great value, since they own their own tannery. 

If you look at the prices these days, the 100 miles are a solid $300-$350 boots…maybe a bit less. But there’s not many places doing CXL for cheap. 

Grant stone seem like just insane value and Truman are the next tier above too. 

I have the CF Stead rough out 1k’s and they’re great, looks like the cow tried to escape a barbed wire fence. 

I kinda geek out on the resole pics online. I’m startling to wonder if 1k’s after one of those cobbler upgrades are really things start. Two pairs of mine have almost burnt through the leather sole, so it’s almost time.
[jo6itit] (score 1, diepte 2) Wolverine having a heck of a sale on 1000 miles on their website...run discount codes...$250ish shipped with free returns...I'd take that over a $199 TBC all day.
[ku3hv3j] (score 1, diepte 3) I just got a pair for 199 with sale and cupon code
[jo6jfwy] (score 1, diepte 2) Gotta gettem on sale. Like now!

=== THREAD 2z7c0y ===
SUBREDDIT: r/BarefootRunning
DATUM: 2015-03-16  SCORE: 8  REACTIES: 28
TITEL: Barefoot for a few years, still can't run at all.
POST (source_id=post):
Hi All,

I'm new to this subreddit, not new to barefoot/vibrams.  Let me sum up...

-Weakass skinny kid with medical problems
-Flat feet, weak legs
-Got orthotics at 13 or so.  Wore them for maybe 15 years.  Feet and legs never felt right.  Always in pain.
-Woke up to the idea of barefootness.  Made the switch.  Huge improvement.  Been living in vibrams for 3-4 years now.  

So my legs have gotten much stronger.  I squat well.  I deadlift well.  I spend most of the day on my feet at work without a problem (in vibrams).  I take at lot of stairs at work and every time will sprint up a flight (maybe 20x/day).

My problem is that I still can't run at all.  After several years I still pull something in the bottom of my mid foot in less than a 1/4 mile.  Feels like a muscle or tendon snapping.  

I've tried strengthening my feet and lower legs repeatedly.  Try stretching, try good form, try to work calves and foot in the weight room which seems to go ok.  I still can't run 1 yard further than I could years ago.  Strangely, my sprint is great.  Of course I can only do a 100m maybe 2-3 times before the same muscles pull.

Has anyone had something similar?  Any tips?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cpgewl5] (score 3, diepte 0) >My problem is that I still can't run at all. After several years I still pull something in the bottom of my mid foot in less than a 1/4 mile. Feels like a muscle or tendon snapping.

How far do you try running each time? Did you gradually try to work your distance up or did you start going for a half mile or something like that and have to quit at a quarter each time?
[cpgkqdu] (score 2, diepte 0) I think that's the major arch muscle. It probably still isn't quite strong enough yet. One of my problems sounds very similar to yours, a sharp pain through the bottom middle of my foot when I run too much. I've made a lot of progress too but I think we both need to get those muscles stronger and more flexible still.

Take a look at this: https://www.youtube.com/watch?v=1iZg_e4veWk&index=14&list=LLBHzPkKUgk-MFCYeCE0kRsA

I think it's a great exercise for working out those muscles. I'm to the point where I can do that contraction on command without assistance. I hold the arch like that and essentially do calf raises with my feet hanging off the back of a stair.

Take it really easy and be sure not to overdo it.
[cpgcy7q] (score 1, diepte 0) Do you train on varied terrain? Do you walk barefoot on gravel, rocks, in sand, etc? If you only run on smooth surfaces (like concrete or a track) that might explain it. 

Otherwise my best advice is to seek the help of a PT. They could help pinpoint which soft tissue is causing problems and maybe build a treatment plan from there.
[cph0mts] (score 1, diepte 1 OP) Yeah, any terrain I can find.

Every time I've talked to a PT they've tried to cast me back up in more restrictive shoes.  I get frustrated and I leave.
[cph1f5k] (score 1, diepte 2) Tough to find a barefoot friendly PT, that's for sure.
[cpgd8xf] (score 1, diepte 0) Fore foot or mid foot striker?

You might try to alternate.

When I started running minimalist, I tried running forefoot, because, well, I was smarter than my feet.  My feet promptly told me I didn't know anything about feet, and eventually (painfully) they convinced me that I should midfoot, which works fine.

If I land too far forward on my feet, yes, after a mile or so, it doesn't feel good.  Also my ankle starts to really bother me.  Midfoot is not a problem.
[cph0o0x] (score 1, diepte 1 OP) Forefoot is what feels natural to my stride.  I've tried mid foot and it doesn't help.  Sometimes when something starts to pull I'll try to play around and find a gait that works but I've never been successful.
[cpgejxc] (score 1, diepte 0) Try landing on the outside of your foot, as gently as possible (and then pronating of course). I get something similar when I land flat footed. Also, calf raises.
[cph0ol6] (score 1, diepte 1 OP) Done both.  Nothing...
[cph0lt4] (score 1, diepte 1 OP) I have to quit at a quarter mile max each time.  I never get past that.  No fat guy here either, so I should be able to do a mile in my sleep.
[cph0nj1] (score 1, diepte 2) Right, but did you try working your way up to it slowly, or do you try seeing how far you can get each time?
[cph19jb] (score 1, diepte 3 OP) Pulled my left foot yesterday on step #5 and had to pull up.  Pretty shitty for several years of trying to fix this.
[cph1ly5] (score 1, diepte 4) Alright, next step in troubleshooting I can think of is looking at trigger points. While not necessary, something like a Theracane is handy, and you can get a manual that shows trigger point pain referral patterns (so if you're experiencing pain in the bottom of your foot the spasm causing it could be somewhere in your leg) and see if it's that. I find for myself a point on the outside of my leg at the midpoint of the shin seems to relate to tension I have in the bottom of my foot.
[cph4f97] (score 1, diepte 5 OP) Hmmm, that's interesting.  Going to look into that.  Thanks.
[cpgikyz] (score 1, diepte 0) Congrats on your progress so far!  It sounds like you're doing great.

When you're walking barefoot, you're probably heal striking gently and then rolling forward to your forefoot and pushing off.  That builds up a ton of great muscles and is a great place to start.

When you start running, a heal strike is going to send a big jolt up your leg, so (at least in my case) your body adjusts by landing fore or midfoot.  This is where it gets tough though - your calves have to pull on your ankles (I am not a physio lol) to keep your heal from smashing down.  That puts a ton of new tension on your tendons and muscles and could be the source of the pain.

In my case, I just started with really short distances and worked my way up slowly.  You can try mixing concrete and grass into he same run, as you'll probably go back to heal striking on the grass and that will take a bit of strain off your feet.
[cph0smr] (score 1, diepte 1 OP) Thanks man.

Right on the calves thing, which is why I've put so much effort into trying to strengthen them with weights.  

Yesterday I went for a run and my left foot pulled on step 5, my right foot 3 steps later.  No way to shorten my distance at all.  It's so frustrating.  I can squat 225 no prob, DL 325 (all barefoot of course) but can't even start the smallest training for a jog.
[cpgqxii] (score 1, diepte 0) Go to a physical therapist.  I am in a similar position to you, I had bad feet as a kid, they prescribed orthotics, I never wore them because they were painful.  I've been working on my feet for years, including barefoot running.  I went to PT for a shoulder injury, the place does walk-ins without a doctor's note, so when the shoulder injury was over, I asked them to work on my feet.  Been a few weeks and I am already seeing huge improvements.  I feel like 10 years ago this wouldn't have been an option.
[cph0uor] (score 1, diepte 1 OP) May I ask about the cost and the treatment you've gotten?  Every experience I've had has been me paying a $35 copay to tell them that I refuse to wear orthotics in closed shoes.
[cph1y4l] (score 1, diepte 2) I have had similar bad experiences.  I just finally found the right person to help.  I am telling you, I am not cured yet, but I feel like I have made more progress in the last 3 weeks than in the last 3 years of doing exercies I saw on you tube.
[cpguoac] (score 1, diepte 0) It may have nothing to do with your feet. All of our nerves, tendons and muscles are connected and if one things isn't working, you may feel it somewhere else as something has to take up the slack. If a muscle in my body isn't working properly, feel it in my left foot / ankle.  Try something new, find a Muscle Activation Techniques [MAT](http://muscleactivation.com) expert in your area as they may be able to figure out if you have one (most likely many) muscles not working correctly and need to be re-activated. You may have some biomechanical unbalances (muscular / skeletal) that are causing you issues. Strengthen your weak spots.
[cph0voz] (score 1, diepte 1 OP) Thanks.  I've thought about this as I know I have anterior pelvic tilt which I'm trying to correct (same thing anyone with a desk job has).
[cph1er7] (score 1, diepte 2) Glutes and quads are weak, right? plus lower back etc...trust me, I'm still working on that. Strength training is key.
[cph4ghf] (score 1, diepte 3 OP) Not weak as much as imbalanced.  I'm sure my hip flexors are tight.
[cph4jik] (score 1, diepte 4) I bet your hip flexors tight because you glutes ARE weak.
[cphmzrf] (score 1, diepte 0) May be a stupid question, but are you actually running barefoot, as in skin to ground? Or are you running in Vibrams all the time?

From what I can gather it is the latter.

This is important as putting anything on your feet dulls the feedback you are getting.

Protection is sometimes necessary but I would recommend actually running barefoot to begin with to find a way to run without pulling the muscles you mention. 

Only then try to translate that form to running in vibrams.
[cpi58bf] (score 1, diepte 1 OP) That's a good question.  It is mostly vibrams.  I'm in vibrams all day for work, when I get home I go barefoot, when I run it's mostly mostly vibrams but I have tried barefoot.  Barefoot seems to make it worse actually.
[cpli7gy] (score 1, diepte 0) Maybe this is a dumb question, but is there a way that you can run period? What I mean is, if you go back to regular padded shoes, can you run?

Can you walk around on the balls of your feet with no problem? What about fast walking in vibrams? I am curious as to what your form is when you run because I can't really picture how this can happen. How long is your stride? I know you said forefoot more natural, but have you tried to land more mid foot?

When you see stairs next time, do calf raises on that by putting your toes on the stair and then lowering yourself. 

Are you sure what your hearing is a muscle pulling?

Maybe get a lacrosse ball and roll your feet out before you go to stretch them? 

And lastly, do you notice a difference between grass or cement?
[cqctacs] (score 1, diepte 1 OP) Thanks for the reply.  I didn't see this until just now.

Can't run in padded shoes.  That's even worse.

I can walk ok in vibrams.  Not well and I can't last more than a couple of miles.  My running stride isn't that long.  I've tried forefoot, midfoot, and everything I can think of without any luck.

Calf raises are good.  I do them liberally.  Hasn't improved anything yet, maybe even worsened.

Not sure what's pulling.  Tendons, muscles, etc.. .  But it feels like nails in the bottom of my mid foot.

Tried the rolling and stretching.  That definitely makes it worse.

No difference between grass and cement, or really any surface.

=== THREAD 1dchjnk ===
SUBREDDIT: r/thenetherlands
DATUM: 2024-06-10  SCORE: 8  REACTIES: 27
TITEL: Locatie voor wandeling op blote voeten? (ZH)
POST (source_id=post):
Beste allemaal, 

Vorig jaar heb ik voor het eerst met mijn goede vriendin een wandeling op blote voeten gemaakt, in de Pan van Persijn in Katwijk. Misschien niet voor iedereen een aantrekkelijk idee, maar voor ons een hele leuke manier om de natuur nog nét iets intenser te beleven. Deze locatie is bijna volledig onverhard, met paadjes van koele bosgrond, afgewisseld met zand, gras, en mos. Dat loopt heerlijk op je blootjes. Ons zijuitstapje naar de naastgelegen duinen, met paden van fijn schelpengruis, was minder comfortabel. 

Nu willen we graag opnieuw zo'n wandeling maken, maar liefst op een plek die we nog niet kennen. Het valt echter niet mee om een geschikte locatie te vinden: we reizen met het OV, en hebben maar één dag, dus onze actieradius is beperkt (een uurtje met de trein, misschien anderhalf, vanuit Leiden). Ik ben me bewust van het bestaan van verschillende speciaal ingerichte blotevoetenpaden, maar die liggen volgens mij allemaal buiten ons bereik. Bovendien, wandelroutes -op zich- zijn niet moeilijk te vinden, maar het is niet alsof er een waarschuwing bij staat "let op, schelpen- en grindpaden". 

Heeft iemand de gouden tip voor een leuke wandelplek voor ons? 

Bij voorbaat dank!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l7ye9l3] (score 21, diepte 0) In Twello (bij Deventer) is een blotevoetenpad: https://bijbuitenpost.nl/blotevoetenpad/. Maar dat is misschien net wat te ver weg?
[l7ywvxe] (score 14, diepte 0) Zeker! De duinen net ten noorden van Noordwijk kan je dat ook prima doen. Uitgestrekt duin/boslandschap van Noordwijk tot Zandvoort. Pak de bus of auto en start bij de duinweg en loop de duinen in en volg waar je voeten je willen brengen. Je kan zelfs een rondje doen en via het strand weer teruglopen. 

Verder natuurlijk Meijendel tussen Wassenaar en Den Haag, waar je ook voldoende op blote voeten kan lopen maar mijns inziens net iets minder.
[l7z1n9y] (score 7, diepte 0) Vanuit Driebergen-Zeist, Maarn, Ede-Wageningen, Wolfheze en Oosterbeek loop je gemakkelijk het bos in. Ze liggen allen aan de spoorlijn Utrecht-Arnhem en Oosterbeek, het verste station is 1u30m treinen vanuit Leiden. In Driebergen-Zeist ben je binnen 1u3m. Ik ben niet meer in die regio dus ik weet niet meer zo goed hoe de paden eruitzien, maar het merendeel is bospad. Bij de heide heb je meestal een zandpad zonder gruis. Misschien zit er ook een leuke wandeling bij de [NS-wandelingen](https://www.ns.nl/dagje-uit/wandelen).
[l7z61qz] (score 5, diepte 0) Probeer de soesterduinen!
[l7yf5rf] (score 4, diepte 1 OP) Ja, precies... Zulke paden zitten verspreid door het hele land, behalve bij ons in de buurt. Op een paar kleintjes na, dan. 

Vandaar dat ik eerder op zoek ben naar "gewoon" een leuk stuk bos om te wandelen, waar de paden niet vol grind, gruis of ander scherps liggen.
[l7zqa34] (score 4, diepte 1 OP) Dat ziet er goed uit. Een beetje dezelfde "vibe" als de Pan van Persijn, maar uitgestrekter. En lekker dichtbij, wat ook een pluspunt is. Dank voor de tip!
[l7zpm1s] (score 4, diepte 1 OP) Ik heb even rondgekeken op google maps, en dit ziet er heel mooi uit. Bedankt voor de tip!
[l7zpeqc] (score 4, diepte 1 OP) Wow, dat ziet er mooi uit daar, zeg! En inderdaad goed bereikbaar. Deze past aardig bij wat ik in gedachten had, aan de foto's op google maps te zien. Dank je wel!
[l7yx9h8] (score 3, diepte 0) Ik ben redelijk bekend met die omgeving, al ben ik er de afgelopen jaren amper geweest.

Katwijk Zuid heeft in de duinen idd veel schelpen paadjes. Daar ben je waarschijnlijk geweest.

Katwijk Noord is denk ik niet heel veel beter, al kan je de helft van de wandeling mooi over het strand doen op blote voeten. En de duinhelft heeft wel gedeeltelijk een zandpad.

Wassenaarse slag: er is een geasfalteerde fiets/wandelpad met daaromheen schelpen en zand paadjes. Lijkt me wel te doen. Natuurlijk ook weer strand. Probeer misschien vooral het bosachtige stuk ten zuiden van de toegangsweg.


Nog een tip: doe een beetje voorverkenning met Google Street View photospheres.
[l7zbv1b] (score 3, diepte 0) https://www.wandel.nl/routes/7-mooie-blotevoetenpaden/

https://wandelblog.nl/blotevoetenpaden/

https://www.dewandeldate.nl/tips/blotevoetenpaden-nederland-en-belgie

Even wat linkjes voor je verzameld. Er schijnt een blote voetenpad bij pannenkoekenrestaurant Klokshuys in Brielle te zijn!
[l7znlvv] (score 3, diepte 1 OP) Enorm bedankt voor de moeite! Ik had zelf al een aantal van dit soort lijstjes gevonden, en het viel me op dat hoe verder je bij Leiden vandaan komt, hoe mooier, langer en "natuurlijker" de paden worden, terwijl wat er bij ons in de buurt zit vooral kortere, meer "kunstmatige" paden zijn. 

Wat we zoeken is niet zo zeer een blotevoetenpad als zodanig, meer een mooie boswandeling met toevallig prettig aanvoelende, onverharde ondergronden. We zijn allebei gek van plantjes, beestjes, paddenstoelen enzovoort zoeken, en het gevoel van heerlijk vrij door de natuur lopen in het algemeen. Toen we dat vorig jaar op blote voeten deden merkten we dat we door die zintuiglijke ervaring nog veel meer opgingen in dat "bosbad"-gevoel. 

Zo'n pad klinkt ook best leuk, maar de nadruk ligt meer op de natuurbeleving dan op het ervaren van zoveel mogelijk verschillende ondergronden. 

Evengoed zal ik eens kijken of er iets interessants tussen zit. Nogmaals heel erg bedankt!
[l7zp5kg] (score 2, diepte 1 OP) Dank voor de tip, vooral dat van die voorverkenning! Dat maakt het een stuk makkelijker om te zien of de locatie een beetje aan de wensen voldoet.
[l82ydtb] (score 2, diepte 0) Gegeven jullie enthousiasme voor blootvoetslopen, mag ik je vragen of jullie bekend zijn met zgn, barefoot schoenen?

Zo nee:barefoot schoenen zijn schoenen die ontworpen zjn om zo dicht mogelijk de ervaring van het lopen op blote voeten te benaderen door een hele dunne en flexibele zool te hebben zonder verhoging voor de hielen (hak). Ook hebben ze extra ruimte voor je tenen of zelfs aparte tenen (zie merk vibram). Je voelt 100% de details van de ondergrond waar je op loopt, maar je bent wel beschermd.

Ze zeggen dat het beter zou zijn, maar ik loop er nu sinds een paar jaar op puur omdat ik het lekker vind lopen. Er zijn winkels in NL die gespecialiseerd zijn in barefoot schoenen zodat je een keer kan kijken wat er allemaal op de markt is. Mogelijk dat dit een compromis kan bieden zodat elke wandeling jullie dat blotevoetengevoel kan opleveren :)
[l83uhy2] (score 2, diepte 1 OP) Ik ken ze wel, en heb wel eens een paar van die vibrams geprobeerd, maar heb eigenlijk nooit een paar kunnen vinden dat ik er ook leuk uit vond zien voor in het dagelijks leven. 

Maar speciaal als wandelschoenen is het zo'n gek idee nog niet!
[l84va4z] (score 2, diepte 2) Wat de Vibrams betreft, eens. De meeste trekken voor mijn gevoel onnodig de aandacht door de gekozen kleuren en daar heb ik ook geen zin in. Ik heb echter een paar CVT-Hemp Vibrams gekocht die heel discreet khaki gekleurd zijn. Soms hoor ik iemand aangeven dat ze initieel dachten dat ik op blote voeten liep.

Daarnaast heb ik een paar "normale" barefoot schoenen waar je eigenlijk niet iets bijzonders aan ziet, gewoon modern (donker blauw leer, witte zool) en die gebuik ik eigenlijk continu behalve wanneer ik expliciet netjes/professioneel gekleed wil zijn, dan draag ik klassieke schoenen. Ik ben er blij mee, loopt heerlijk.
[l83mv5c] (score 2, diepte 0) In de tuin van het Kröller-Müller Museum ligt een blotenvoeten wandelpad. Zelf niet perse mijn ding, maar het beviel mn vriendin goed. Overigens loop je er wel in een half uurtje doorheen, dus maak er geen grote omweg voor.
[l7zr5pd] (score 1, diepte 2) Veel plezier!
[l80f85w] (score 1, diepte 2) Ik woon in Ede, bossen genoeg in de omgeving! Als je nog uitgestrekter wilt tussen Ede en Apeldoorn heb je de hoge Veluwe.
[l80j394] (score 1, diepte 3 OP) Dank! Ziet eruit alsof je vanaf station Ede-Wageningen zo het bos in kunt lopen, klopt dat? En wauw, als we de juiste trein pakken is het maar iets meer dan een uurtje om er te komen.
[l80mldr] (score 1, diepte 4) Ja, dat klopt inderdaad. Ik woon er in de buurt haha. Het echte groene hart, kijk maar op Google maps met de satelliet view.
[l85b2lu] (score 1, diepte 4) [Yep,](https://www.bezoek-ede.nl/natuur-actief/routes/1292581696/wandeling-door-de-sysselt) De Sysselt. [Mooie omgeving](https://www.wandeldingen.nl/de-sysselt/). Ik heb hier mijn autisme diagnose gekregen (nee echt, zit in een leefgroep ergens in het midden). Het station wordt op dit moment verbouwd dus misschien moet je wel eerst uit de bouwput zien te komen.
[l85bppx] (score 1, diepte 5 OP) Nou, dit wordt hem denk ik. Ziet er geweldig uit! Nou nog even overleggen. En hey, als je ergens de komende maand twee figuren op hun blootjes door het bos ziet lopen, zwaai dan even :)
[l859jol] (score 1, diepte 3 OP) Heb je misschien een linkje naar die "normale" schoenen, of iets vergelijkbaars? Klinkt als iets dat wel eens goed zou kunnen zijn voor m'n rug :)
[l85h1ve] (score 1, diepte 4) Tuurlijk. Ik heb het even nagekeken, de "normale" schoenen die ik gekocht had waren de Vivobarefoot Addis Men Navy bij barefootandmore.nl met witte zool (want mooier). Ik zie ze niet meer in het donker blauw (Navy) staan, maar bijvoorbeeld wel in het donkergeel/beige bijvoorbeeld, ook vrij beschaafd: [linkje](https://www.barefootandmore.nl/addis-men-spicy-mustard.html).

Je kan anders even kijken welke merken wat voor soort uitstraling of stijl hebben en of er eentje is die je wat meer aanspreekt. Ik ben zeker geen specialist, maar ik heb het idee dat Vivobarefoot bv. zeker een paar modellen heeft waarvan je echt niet kan zien dat het barefoot schoenen zijn.
[l85odfy] (score 1, diepte 5 OP) Zo op het eerste oog kan ik op die site best wat leuks vinden dat bij me past! Dank voor de tip en de aanzet, ik denk dat ik hier werk van ga maken!
[l85ppki] (score 1, diepte 6) Andere tip: ik ben bewust in hun fysieke winkel geweest, omdat ik wilde zien en voelen waar we het over hebben. Laat maar weten of je geslaagd bent en zo ja met wat als je wil. Niet belangrijk, maar gewoon uit nieuwsgierigheid:)
[l8awqoe] (score 1, diepte 1 OP) Toch een leuke om in gedachten te houden, want het Kröller-Müller an sich past ook heel goed in onze overige interesses. Dit keer gaan we voor de "puur natuur"-boswandeling van een paar kilometer met verrekijker en picknickmand, maar het Kröller-Müller-museum wordt hiermee wel erg interessant als bestemming voor een volgend uitstapje ergens deze zomer. Bedankt voor de tip!
[l8bm4gs] (score 1, diepte 0) Let wel op dat het nadelig is voor je gezondheid. Je loopt erg snel ergens in, en beschadigd/infecteert jezelf zeer snel (HPV's, hielpijn bijvoorbeeld - naast het risico van langzaam je voet te vervormen en je voet boog te verliezen//doorzakken dus). Men loopt niet voor niets al sinds we rechtop kunnen staan op een soort schoeisel.
[l8brl6f] (score 1, diepte 1 OP) Interessante stelling. Ik lees juist overal dat het heel goed is voor je lichaamshouding, je spieren, je rug, enzovoort. Iets met "je voetzolen zijn net zo gevoelig als je handen, en je tastzin zorgt ervoor dat je lichaam zich aanpast aan wat je onder je voeten voelt.", en "omdat je loopt 'zoals moeder natuur het bedoeld heeft' in plaats van met een schoenzool tussen jou en de grond gebruik je, en train je, spieren die als je schoenen draagt minder benut worden."

Over ergens in/op gaan staan of mezelf verwonden maak ik me niet zo druk. Ik werk met kinderen, en één ding dat me opgevallen is is dat ze bijna allemaal graag op blote voeten lopen, en dat kinderen die dat doen een stuk beter uitkijken waar ze stappen dan kinderen die hun schoenen aanhouden. Voor volwassenen zoals wij geldt datzelfde; juist omdat je tastzin "aan staat" let je heel goed op waar je je voeten neerzet, juist ook als je door de bush-bush loopt. Je wil immers niet op een dennenappel of distel gaan staan, toch?

Daarnaast heb ik al jaren geleden al gelezen over onderzoeken naar voet- en rugklachten over de hele wereld, en de opvallende resultaten die uitwezen dat in landen waar men hooguit een paar slippers bezit, platvoeten, hamertenen, hallux valgus enzovoort nauwelijks een issue zijn. De rode draad is "hoe meer je op blote voeten loopt, hoe beter je algehele motorische gezondheid."

Ik waardeer het oprecht dat je je zorgen deelt, daar niet van. Maar ik kan me eerlijk gezegd nauwelijks voorstellen dat het klopt wat je zegt, en herken me er op basis van mijn eigen ervaringen ook niet in. Mag ik vragen waar je je informatie vandaan haalt? Ik zou me graag nader informeren.
[l8bvz6c] (score 1, diepte 2) Het ligt er een beetje aan in welke hoek je zoekt en natuurlijk hoeveel je het belast en hoeveel je loopt. Als ik zo kijk is het aan de ene kant aangeraden inderdaad, en aan de andere kant af (de typische online voor/tegen kamp dat 't afschreeuwt tegenover elkaar). 

Ik haal mijn info niet direct uit een blad of iets dergelijks, maar heb tijd geleden uitgebreid staan zoeken naar goede wandelschoenen en hardloop schoenen, en daar kom je natuurlijk de andere kant van de munt tegen. Slechte ondersteuning is grotere kans op hielspoor etc etc. 

En mbt hamertenen, hallux valgus etc etc, is met goede schoenen ook geen problemen. 

Ik denk dat het ook niet helpt dat ik nog geen 3 maanden terug mezelf heb moeten laten inenten tegen tetanus, omdat ik (met dunne vans weliswaar) op een roestige spijker ging staan. Dat gaat dwars door je vlees als je eventjes niet oplet, met een eventuele infectie daar naast gelaten. Je legt wel veel vertrouwen in dat je mede mens er geen puinhoop van het wandelpad maakt, en daar zou ik niet mijn vertrouwen leggen.
[l8c4csi] (score 1, diepte 3 OP) Oef, dat klinkt heel vervelend, ik snap dat je mede door je eigen ervaringen zo je bedenkingen hebt. 

Maar dan deel ik toch ook graag mijn eigen ervaring, de "andere kant van de munt", al komt het wel een beetje dichtbij om dat zo "openbaar" te doen. Ik wilde al heel lang een keer zo'n wandeling maken, en het is bij de gratie van die vriendin van me dat ik het ook echt aandurfde. Ik was bang voor rare blikken en onbegrip, mede omdat ik als kind ben gepest als ik bijv. sandalen droeg. Waarom, geen idee, maar het was destijds "niet cool" ofzo, en het zit heel diep. 

Ik wilde wel, maar durfde niet, en ging daarom stiekem 's nachts in het donker op pad om op m'n blootjes door het gras te lopen, als ik (bijna) zeker wist dat ik niemand zou tegenkomen. Maar in haar vond ik iemand met wie ik zoiets "geks" kon delen zonder me te schamen, en ze begreep me. En onder de streep, "Eén iemand op blote voeten in het bos is een krankzinnige, twee mensen op blote voeten in het bos doen aan een stukje 'natuurbeleving' ", dus gingen we er samen op uit. Ik ben haar nog steeds intens dankbaar dat ze dat voor me wilde doen, en daarnaast blij verrast dat niemand die we tegenkwamen raar opkeek of opmerkingen maakte, hoe bang ik daarvoor ook was. Goed, ik durf nog steeds niet in m'n eentje overdag, maar m'n irrationele angst is wat verminderd.

Maar daarnaast, hier komt-ie: twee jaar voordat dit begon te spelen kreeg ik van de dokter te verstaan dat ik een kilo of 20 moest afvallen om van m'n slaapapneu af te komen. Dat is me gelukt door m'n dieet aan te passen en door héél veel te gaan wandelen, soms wel 10 kilometer per dag, zeven dagen per week. Op een paar degelijke wandelschoenen. In mijn enthousiasme ben ik inderdaad te ver gegaan, en heb ik een hielspoor opgelopen, wat me tot op de dag van vandaag parten speelt. 

Maar afgelopen zomer heb ik, behalve die ene wandeling met z'n tweetjes, ook in m'n eentje best wat kilometers op m'n blootjes gemaakt. 's Avonds en 's nachts in het donker, weliswaar, maar toch. En het is me opgevallen dat hoe meer ik dat deed, hoe minder last ik had van m'n hielspoor. Sinds de herfst inviel en het te koud werd voor zulke strapatsen kwamen de klachten weer terug, maar inmiddels heb ik weer een paar wandelingetjes gemaakt (ondanks het kwakkelende weer), en wordt het weer minder. En m'n (bijna veertigjarige) rug is er ook zéker niet ongelukkig mee.

Kort gezegd, op basis van mijn eigen ervaring heb ik de indruk dat het niets dan heilzaam is om op blote voeten door de natuur te lopen. Het ergste wat me overkomen is, zelfs "blind" in het donker (wat in 'jouw perspectief' misschien wel het ultieme risico is), is dat ik een doorntje of splintertje uit m'n zool moest peuteren. En dat terwijl ik toch ook best (overdag) drukbezochte plekken heb bezocht, met een reëel risico op glassscherven en wat niet meer.

Mijn eigen ervaring sluit dus volledig aan bij wat ik lees over het onderwerp. Wat jij zei in je eerste bericht over vervormde voeten, doorzakkende voetbogen enzovoort komt totaal niet overeen met wat ikzelf heb meegemaakt, integendeel. Dan ben ik toch heel benieuwd wat "het andere uiterste" is. Wat hebben anderen meegemaakt, dat ze zeggen dat dit écht geen goed idee is?

