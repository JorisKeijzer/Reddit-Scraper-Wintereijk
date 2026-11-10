# Label-batch batch_0009

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
Schrijf het resultaat naar `batch_0009.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: wjezfl, l730w4, 1213a2h, 1crsus0).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD wjezfl ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-08-08  SCORE: 173  REACTIES: 40
TITEL: Went this morning to see if my local Fleet Feet had any Saucony Endorphin Speed 3, they did, and now I do.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ijgvcf0] (score 17, diepte 0 OP) Definitely didn’t **need** any more running shoes, but with all the stir about some Fleet Feet’s having Speed 3’s already I went to “try them on.” 

Luckily I had $45 in rewards so I left with them! 

Excited to give them a real try, the test jog felt great! Much more stable than the 2’s with a little more toe room. So far only weird part was they seemed to be a little higher on the lateral arch than the 2’s. I decided to throw some insoles in them (same ones I use in my 880v12’s) to fix that feeling.

Edit: hijacking my own top comment to say I wrote a little inspection write up here based on a question someone asked. I didn’t want to waste your guys’ time with a whole new post: https://www.reddit.com/r/RunningShoeGeeks/comments/wjezfl/went_this_morning_to_see_if_my_local_fleet_feet/ijhjao1/?utm_source=share&utm_medium=ios_app&utm_name=iossmf&context=3
[ijhjao1] (score 7, diepte 0 OP) u/135patriots asked about the uppers so here is my small beginners write up on first impressions comparing it to my 1 and 2s without actually using them yet. 

Okay so the padding is not thicker necessarily, nor is the more of it it is different though. 

I am looking at the 1, 2, and 3 all side by side. 

The 1 and 2 are nearly identical when it comes to the padding in the uppers. 

The way I would explain it is the 1 and 2 have uniform padding around the ankle. It’s basically the same thickness around the entire back of the shoe and ankles. If you were to run your finger down the inside of the shoe on either side it’s nearly the same all the way down to the heel cup if that makes sense. 

The 3 is only thicker around the top collar and on the very back where your achilles would be. So if you were to run your finger inside the shoe from collar to heel cup, the padding is only thick for about half an inch or less then thins out. Much like a standard padded collar on shoes if that make sense at all haha! Like a pencil thick ring of padding around the collar. 

The 1 and 2 have a slightly thicker tongue too it feels like. Not much but a little. However the 3’s tongue is wider. 

The lacing and eyelets in the 3 is actually extremely similar to the 1, not much different than the 2, but if you look at all 3 together it looks a lot like the 1 from above. 

The fabric in the 3 has a softer feel, although still feels synthetic-y if that’s a word. But a little softer than the 1, 2. It doesn’t seem like it will be any hotter though. 

They have added a little strip of plastic/vinyl along the tips of the toe, I would assume for durability if you toe drag a little. 

The heel cup and up the back of the Achilles feels a tad stiffer than the 2 but not much and very similar to the 1. 

That’s about all I got for the uppers. 

As for the midsole and sole that’s the biggest change for sure. Different look, wider base, and the plate seems wider as it is slightly exposed now on the outside edges of the shoe, which probably added to the better stability. Looking at the shoe from above and below you can just see that it is wider too, especially in the heel which I think will also assist in that stability compared to its predecessors.

Oh! And comparing the insoles from the 2 and 3 on top of each other the 3 toe box is slightly bigger, not a ton so those of you with narrower feet should still be fine, but an extra mm or so to help those of us with wider feet but not quite “wide”
[ijh50vr] (score 6, diepte 0) Any thoughts on the upper? Looks like a bit more material/padding around the collar, Hope I'm wrong. 

It seems like the 3 is moving ever so slightly in the direction of versatility. I'm cool with it given that versatility has been (imo) the shoe's hallmark and party trick. Just hoping they keep the upper minimal in exchange for more midsole and stability.
[iji6xbq] (score 4, diepte 3) I was just out in Spokane last month for, get this, a Fleet Feet conference. Cool area!
[ijh71sn] (score 4, diepte 3 OP) Agreed! 

I also think their goal is more versatility this time. I think the idea was originally a speed shoe, or lower cost race shoe but so many people loved the predecessors and were using them as daily trainers anyway, why not tweak it a bit and go that route with it. As long as they don’t start making drastic changes I like the path they went with the 3 so far. 

A light weight stable shoe that can do races, speed work, but also is comfortable for slower days and longer runs. Yea please! 

Too me it has almost all the perks and versatility of like the NB 880, but lighter weight. My guess is the only trade off would possibly be that a shoe like the 880 would be more durable saving some $ in the long run (no pun intended). 

That’s just my one main example to compare it to though, as the 880 is my favorite non-Saucony shoe.
[ijhbr9w] (score 4, diepte 0) That black and gold colorway is a beaut.
[ijh5t5s] (score 3, diepte 1 OP) I didn’t notice personally, but once I get home I can compare them better side by side and let you know. 

I know just specifics-wise the 3 is 5 grams heavier, which isn’t a ton (roughly the weight of a piece of printer paper after a quick Google search), so I don’t *think* the upper would have much more heft. I am guessing the extra weight comes from the wider toe box and slightly more stack height (0.5 mm higher in heel and toe)

https://www.reddit.com/r/RunningShoeGeeks/comments/wjezfl/went_this_morning_to_see_if_my_local_fleet_feet/ijhjao1/?utm_source=share&utm_medium=ios_app&utm_name=iossmf&context=3
[ijhgiod] (score 3, diepte 1 OP) Honestly I was hoping for the Fleet Feet exclusive at first, but the more I look at these ones the more I really love the look. 

The other plus side to black colorway is they tend to stay looking nicer a little longer.
[ijieh4p] (score 3, diepte 4) The foam is softer and there just seems to be too much shoe. Not a weight issue just a volume one. The tongue is also garbage. The Pro 3 on the other hand is excellent.

I’ll wear the S3s more before making a final decision.
[ijjbo7v] (score 3, diepte 7 OP) Got about 4.5 miles in once my wife was home. 

I am definitely happily melancholy about them at the moment. 

Like I really enjoy them, they are comfortable and extremely stable, but I feel like they feel too different from the 2’s. 

Like I don’t dislike them as running shoes, but they don’t feel like a pair of Endorphin Speeds. To me it’s like Speed and Triumph had a baby. Which some people will probably really really love. 

I would have preferred the underfoot feel to be a lot more like the 2, and just fix the stability issues. 

I feel like they still shine brighter the faster you go, similar to the past models. I purposefully ran one slow mile, one tempo mile, then the rest of the run I just went with what felt comfortable. The tempo mile felt best on my feet by far, but that’s how the 2’s are for me too. 

I definitely need to give it more time, and like I said I personally do like them, but I will hold finally judgement until I can fully break em in a bit more.
[ijh7hgl] (score 2, diepte 1) What area? The other was Houston.
[ijh7rbm] (score 2, diepte 2 OP) Spokane Washington (far eastern side of the state). We have four Fleet Feet locations in the area. They all share a Facebook Page so I sent them a message this morning and they said one of the locations got a small handful of just a few sizes. Luckily they had my size.

Was hoping for the FF colorway the other poster had, but beggars can’t be choosers and by the time I use these up there should be plenty new choices I hope haha.
[ijj9joa] (score 2, diepte 5) Yea, I enjoyed the visit. Wish I had brought my bike, the cycling is probably amazing. The guy that owns the stores out there is a great dude and runs an awesome operation.
[ijjefw1] (score 2, diepte 6 OP) I haven’t rode a bike in quite a while, but it is definitely fun. Especially the centennial trail (which actually goes right behind the main Fleet Feet location here above the river).  You get a little bit of everything on it. 

City, forest, river, freeway lol. Go far enough east and you hit lake Coeur D Alene too
[ijh6d2y] (score 2, diepte 2) Cool, thanks! I don't care about the weight so long as it stays in the same ballpark. And if the midsole can add even more bounce+cushion while maintaining a decent level of stability we'll once again have a phenomenal shoe on our hands.
[ijhjfx8] (score 2, diepte 1 OP) Did a little write up in a different comment below, tagged you too, but just incase the tag didn’t work letting you know haha!
[ijh8l0s] (score 2, diepte 0) Wish this brand made 4EE sizes in their shoes.
[ijh9zzx] (score 2, diepte 0) so lucky. no fleet feets near me
[ijhf685] (score 2, diepte 0) It’s so funny how so many people use new balance insoles in these shoes. I used 1080v11 insoles in my speed 2’s and so did some other and now you did with these. I really don’t like those high arches, freaking sucks, otherwise great shoes
[ijhiqby] (score 2, diepte 0) Welcome to the club amigo.
[ijiepmh] (score 2, diepte 0) nice shoes
[ijkmz1y] (score 2, diepte 1 OP) Black.
[ijknloc] (score 2, diepte 0) Sweet color
[ijzw0ef] (score 2, diepte 2) Sweet thx. I figured but just thought I’d ask. Looks like I might have to just order the shoe because my half up is a common size. Waiting for Run Detroit to open so I could call and see if they have any left in my size.
[iopgu04] (score 2, diepte 2) Thank you for looking.  When I looked again they were back at the same price.  This was after I purchased them at $10 lower. I wonder if it was a website glitch.  Saved $10, had coupon, and got cash back!
[iji7koy] (score 1, diepte 4 OP) Haha I remember seeing posts about that on the local Fleet Feets IG. I think there was like a group photo and a run by the River. 

Born and raised here, it has its ups and downs like any city, but it has so much to offer. As a smaller metro area we get all the perks of a larger city when it comes to businesses etc etc, but don’t have to deal with the traffic. Also drive any direction from downtown for 15 to 20 min and you’ll hit hiking, a lake, a river, etc etc.
[iji6pfb] (score 1, diepte 0) Took mine on their maidan voyage yesterday and I wasn’t that impressed.
[iji6uj7] (score 1, diepte 1 OP) Interesting. Did you have the 2’s or 1’s beforehand?  

Like I mentioned they felt good in the test run, but that was like one block. I am hoping once my wife gets home I can go out 5 miles or so on them.
[ijibqhh] (score 1, diepte 2) Yes I have run in probably 10+ pairs of 1s and 10+ pairs of 2s. I was pretty beat up yesterday so I’ll give them 50 miles before I decide to buy another pair.
[ijicjlo] (score 1, diepte 3 OP) What would you say, just based on the one run, it’s missing or you didn’t like?
[ijifit7] (score 1, diepte 5 OP) Thanks for sharing!! 

“More shoe” is definitely one thing I noticed. 

Like I said I haven’t tested it on a real run yet and I am not nearly as experienced as many people around here, but I definitely agree that despite not feeling any heavier it just feels bigger. I get you there for sure! 

The foam does feel different to me, but I can’t tell if it’s firmer, softer, or just different to me yet. Probably take a run or two to figure that out. 

I tried comparing all three by just jogging in my house lol, and it’s hard to tell, but the 3 feels less spongy to me but still soft, but I think that could be partially due to the wider heel, I think part of the sponge of the 2 for me was the narrow heel so more squish in a concentrated area (while walking or purposefully landing on the heel to test). I dunno how to explain it lol. I do tend to be slightly a forefoot striker though, so the foam on shoes is always harder for me to relay to people with a mid foot to heel strike. And the 1 I have has too many miles to be a real comparison. 

Definitely try to give shoes a good fair amount of miles before really placing final judgement though too!
[ijigc2o] (score 1, diepte 6) Yeah, they are different for sure. Well enjoy the miles on them!
[ijkd0ta] (score 1, diepte 0) Are those black or charcoal?
[ijzq7tl] (score 1, diepte 2) Did you size up with the new and/or older speeds ?
[ijzo8je] (score 1, diepte 0) Did you size up w/the 3’s ?
[ijzpar0] (score 1, diepte 0) And/or did you size up with the speed 1 or 2 as well. I use to get a full size up but the last pair of saucony’s I bought I only went up a half size
[ijzv2xw] (score 1, diepte 1 OP) I bought the 3 in the same size as I did the 1 and 2. 

I almost always half size up. 

My normal daily shoes like my Vans or walking shoes are all 11.5, and all of my running shoes (with the exception of Nike) are 12.
[ik1hdgp] (score 1, diepte 3 OP) I like em, but in a different way than I like the 2. 

I want to give them more miles to break in, because they are a bit stiffer and despite being roughly the same weight they feel bulkier. Almost more like a dedicated daily trainer than a pace or race shoe. 

Everything on the she is wider than the 2 which fixes the stability issues the 2 has, but that makes me wonder if the wider nylon plate is what makes it feel stiffer. 

I’m hoping once the plate has been bent and pounded around a bit things will soften up a tad.
[iljtckk] (score 1, diepte 0) Just got my size 11's in the mail, same size as multiple speed 2's that I've owned, and they're way too small.  Toes smashing against the front. Feels like they're a size 10! Wonder if I got a defected pair.  Anyone else have this issue? May just have to return for 11.5's, which I've never worn in any shoe. If anything I occasionally size down to a 10.5.  Weird!
[imsu589] (score 1, diepte 0) why are saucony endorphin CHICAGO speed 3 cheaper?
[in8ba1l] (score 1, diepte 1 OP) When I look currently they show the same price 🤷🏻‍♂️
[iopuzz4] (score 1, diepte 3 OP) Nice!

=== THREAD l730w4 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2021-01-28  SCORE: 15  REACTIES: 39
TITEL: Nike Air Zoom Pegasus 37 - anyone else not get on with them?
POST (source_id=post):
I bought a pair of Peg 37's in the Black Friday sales and intended to put them in my rotation as everyday trainers. I've done about 70miles (112km) in them and I find them uncomfortable, especially at faster paces. In particular I get a pain in my left foot around where the tongue area is (I've tried different lacing etc). The bottom line is that I'm pretty disappointed by them as they seem to be highly regarded in some quarters. 

Just wondering if anyone else has found the same?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gl4ecyp] (score 8, diepte 0) they didn't work for me either, 3 black toenails, knee, hamstrings, hips... pain everywhere, same as you, thought that it was coz I wasn't strong enough or I wasn't running fast enough. got a pair of 1080v10 and everything changed.
[gl4dtmm] (score 5, diepte 1 OP) Funny you should mention the Novablasts. I currently run my easy days in Saucony Triumph 17s and they are the most comfortable running shoes I've ever owned and they're coming up to 500 miles.  I'm been torn between just getting a replacement pair (if it ain't broke etc) or trying the Novablasts. I've heard they are 'very' springy.
[gl4cq4n] (score 4, diepte 0) I never complained about it for the same reason as it is one of the highly recommended ones. I started running few months back and I always thought the pain could be because of my previously sedentary lifestyle. But then I recently got asics novablast. Man, they way they hug my feet.
[gl4uuby] (score 4, diepte 2) Do it. Don't torture yourself on runs, they're supposed to be enjoyable not a chore
[gl4oc8m] (score 4, diepte 0) Currently I’m into my third week off due to this shoe. I got an ache in the arch of my left foot, I barely add 20km with them.
[gl4q93v] (score 4, diepte 0) I love my pegs personally. Everyone's foot and fits a little different so might be best to try another pair.
[gl4fjz8] (score 3, diepte 1 OP) Funny you should mention the 1080s as this was my second choice! Hmmm ... could I justify two new pairs?
[gl4iuva] (score 3, diepte 0) I'm prone to achilles problems -- so not entirely the shoe. But I couldn't even walk in them without lighting up my left achilles at the insertion point. I bailed on them after ~30 miles of trying and ended up having to take about 2 weeks off as a result.
[gl4lvq4] (score 3, diepte 0) When I got them I hated them, they just made my legs feel really heavy after a couple of kms. After about 50km they softened up and I have no issues now and actually enjoy running in them.
[gl4lx65] (score 3, diepte 0) They work great for me, took 50 miles to break in the shoes but they’re now incredibly versatile and comfortable. Don’t worry, not everyone gets on with them, maybe try and sell them to fund another pair of trainers?
[gl71fuc] (score 2, diepte 2) Yes you can, I just got a pair of triumph 18s and I like them but not as a 1080 replacement so I'm about to buy my second 1080s pair

Edit: between the novablast and the 1080, IMO the 1080s
[gl9brm8] (score 2, diepte 1) I follow marathoner Ben Parkes and really value his opinions ! He LOVES the 1080s and hates the peg37 so I say get the 1080s - I’m waiting on mine to come in but got them based on his review and several videos mentioning them
[glc6bnu] (score 2, diepte 2) So do I, Ben and Sarah, nicest runners couple on YouTube. I was hesitating amongst the 1080, triumphs, infinity and Clifton 7, so between Ben and a little pole that I made here ended up with the 1080 and man, I couldn’t been happier, I got the black color.
[gl60a65] (score 2, diepte 1) They destroyed my achilles as well. I thought it was me and didn't switch shoes until I had tendonosis and had to take 2-3 months off of running. I run in the vaporfly now with no trouble.
[gl4m4fn] (score 2, diepte 0) I recently bought the peg 37 shield version and they don’t work for me either. I find the upper very stiff, especially around the ankle. After only 8 km I already had a massive blister where the outside of my ankle touches the shoes. Did not like the ride at all either, shoe felt very heavy. Maybe I got too spoiled with light weight shoes (Dynaflytes, Endorphin Speeds, Peg Turbo 2, and Next %). Wearing them when walking the dog now, perhaps they soften up...
[gl4qwsy] (score 2, diepte 0) I've never enjoyed the pegs; got a pair of the 37s and they just felt constricting in my midfoot, an issue i've never had with any other shoe.
[gl4qy1h] (score 2, diepte 0) I tried them on around the house and didn't feel like they fitted well at all, probably the worst fitting shoe I've ever tried. Heard some people saying they were ok despite that but I decided to return them instead of chancing it
[gl58ccv] (score 2, diepte 0) I ran 400 miles in my pair and wasn’t really thrilled.  They never really excited me and running always felt like a chore in them, at any speed. 

Funny the other poster mentioned it but it’s the only pair of shoes to give me the dreaded runner’s black toe nail.
[gl538id] (score 1, diepte 2) The Triumph 17 didn't work for me last year because of fit.  It's definitely my feet rather than the shoe, but I ran about 20 miles in them and returned them.  I have the Novablast in my rotation this year and will confirm the midsole is very springy, while still feeling softer to me than the Triumph did.
[gl5es2p] (score 1, diepte 2) Triumph 17 is GOAT for slow or recovery runs, but they are way too heavy for any sort of higher pace running. I used them for 350 miles as my long run shoe, but now they are my recovery shoe. Nearly 400 miles and they feel pretty close to new still.
[glefkhn] (score 1, diepte 3) got the black too! didn’t realize i purchased the narrow option on running warehouse though so i sent them back and am waiting on the regular width /: so excited to try them though - i love when the new versions come out cause the previous versions go on sale lol
[gl4ukqf] (score 1, diepte 0) Didn't work for me. Forefoot too narrow, hurt like hell and felt awful. Squishes the wrong part of my feet.

Saucony/Skechers/Reebok/Adidas/Asics/Brooks are great for me. Nike is a hard pass.
[gl4wt1z] (score 1, diepte 0) I enjoyed running in the peg 30,31,34,35, and kinda 36. The 37 was a no go for me. Too soft in the heel and the firm forefoot made for an odd ride where it felt like I was sinking backwards in the middle of my stride. I’m a mid-foot and efficient striker through my stride so I was caught off guard by this shoe. Was a shame too, cause I enjoyed the Pegasus line
[gl53ifa] (score 1, diepte 0) I never could get the Pegs to work for me.  I feel like the arch support on them is just too pronounced for me to get comfortable.
[gl59byh] (score 1, diepte 0) Didn't work for me at all which is a shame because the 36 was great for me and the 37 was a downgrade rather than an upgrade. At least I got a nice colourway so get plenty of use out of it as a casual shoe.
[gl5f72m] (score 1, diepte 0) I loved mine since day 1, I have 400 miles on mine and I think they'll last another 100. Longest lasting shoe yet!
[gl5hftu] (score 1, diepte 0) I actually like mine, I have two pairs of the BE TRUE. I tried the tempo next first and those gave me lots of ankle pain.
[gl68emg] (score 1, diepte 0) I didn’t like the fit and heel slip, but I tended not to notice at faster paces, which is where I placed it in from now on. This is really different to yr experience. The Peg 37 was a miss overall I can’t lie. The Saucony Ride 13 seems like a better choice that would serve the same purpose.
[gl6biie] (score 1, diepte 0) Personally I am quite disappointed with this shoe. It is a bit too firm and lacks the cushioning I need for easy/recovery days. And I find it too clunky and heavy for faster days. On top of that, I never really find it comfortable to run in them despite putting in 100km in them. Unfortunately, I have to relegate the shoe for gym work and it works find
[gl7ajpk] (score 1, diepte 0) I loved the 35s - and just grabbed a couple of 36s at the outlet because of the bad rep the 37s have - it’s a real shame because the Peg has been a safe bet for years. 

My most recent horror shoe was the SL20. Short and shallow toe box messed up my big toe really bad.  None of the glowing reviews mentioned it either. They had to go to the great shoe hand-me-down after 10km.
[gl89984] (score 1, diepte 0) I’ve persevered with my 37’s for 400k and still don’t really like them. Have always irritated the outside middle of my foot and hasn’t gotten better even through I kept trying to tell myself it had. 

Last run in them was about a month ago and they rubbed the top of my toes a bit and I haven’t touched them since. Wanted to like them but just can’t.
[gl8p1xf] (score 1, diepte 0) I have a pair I'm sending back right now! Hated these shoes. Wanted to live them, but had the worst inner foot arch blisters and ankle slippage. Opted for the Vomero 15s instead.
[gl96ynm] (score 1, diepte 0 OP) Interesting to get so much feedback, glad that I'm not alone. I know that each person's view is subjective and one person's dream shoe is another person's horror shoe. I really wanted to like this shoe and since I've stopped going to running shops to buy shoes (due to lockdown) and began to buy them on spec from the internet, this is the first pair I will have to sell/get rid of.
[glasj53] (score 1, diepte 0) Sometimes they feel great, most of the time they don't. I have a love/hate relationship with that pair of shoes. The 36s feel much more reliable to me in the Peg lineup.
[glawafd] (score 1, diepte 0) I didn’t like them. There wasn’t anything that stood out as being awful, but it reminds me of the Ultraboost: cushioned and soft, but heavy and dreary. It didn’t feel particularly smooth and comfortable like the Infinity React. It just felt like a Turbo 2 without the liveliness and midsole comfort. Maybe I’ll give them another shot sometime, as I was wearing them while recovering from a marathon.
[glaxru2] (score 1, diepte 0) I managed to get 450K on them but hated every part of part of it. It felt stiff and narrow on my feet. I dont even know what to make of the upper.
[glcbifv] (score 1, diepte 0) I'm still not sure how I feel about them after 100 miles. The first like 20 miles in them caused me to get pains EVERY time I wore them though, I feel react needs time in it to settle down. After that, I seem to have a lot fewer issues, but it's hit or miss.

Sometimes they're super comfortable and work great, nice and springy, no issues.

Other days, the lockdown just doesn't work, I either get heel sleep, or I tie them way too tight and due to the thin tongue, my feet cramp up.

Really 50/50 on them, think I'm gonna try the ZoomX Invicible's, maybe Novablasts, 1080s or even Endorphin Speeds next.
[gld6p5u] (score 1, diepte 0) I was also having pain on top of my foot near the tongue area and I thought it was a lacing thing but eventually took the whole lace out and walked around briefly to realize I was STILL having pain. for me, the Seam at the bottom of the tongue was too tight and was pinching. I literally just cut through that seam to loosen it and have had way fewer issues since
[h04k8fp] (score 1, diepte 0) I just bought some from Nike.com for $60.  Ran 5 miles first day and they did good.  Did a 20 mile run the second run and the upper area of the tongue was pressing into my upper foot/ankle area.   So much so I thought maybe I had them shoes tied too tight.  Stopped for a second and loosened the shoe but still felt the tongue pushing in.  It’s weird because there isn’t much material there and it’s floppy so doesn’t seem like it should be a big deal.

=== THREAD 1213a2h ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2023-03-24  SCORE: 101  REACTIES: 39
TITEL: Adizero SL - people in hurricane prone areas should be building their homes out of lightstrike
POST (source_id=post):
For some context, ~155lb/70kg, avg 180spm, midfoot strike. 3 runs in the shoe total, 15km longest run.

Got a discount code and needed a new daily trainer, so I took a punt on this shoe. From humble beginnings the SL had been elevated to the adizero line, I had high hopes.

First things first, the ride: I was expecting firm, but having not run on a lightstrike midsole before, this was abrupt. Firm. Firm to the point that I question how someone at Adidas whipped up that first batch of lightstrike, tried it, and thought "that's what runners want."

Some people like a much firmer ride and that's cool, IMHO in the case of the SL midsole it's a rock solid block of unyielding TPE. This midsole could prop up the UK economy. The lightstrike used in this shoe is so dense it has a gravitational pull. Worryingly, various reviewers cite this midsole as softened compared to other shoes using lightstrike (in the same way that steel is softer than tungsten I imagine).

Fit: so this is kinda ironic. This shoe fits me better than any other shoe I have ever worn, and that's only very slight hyperbole. The last is perfectly shaped for me, TTS it's like they used my foot to make the mold. Upper is well padded and comfortable, absolutely no problems. Exactly what I want in a daily trainer. It's definitely a slightly more snug fit, so half a size up wouldn't hurt.

Uses: for me, worthless as a daily trainer, can't get past that granite midsole, I will very likely never run in this shoe again. That said, it wouldn't be a terrible speed shoe at a budget friendly price point (£110 RRP, so probably 60-70 on sale). No problems picking up the pace on strides, once you're up on your toes the lightstrike pro 'puck' in the forefoot starts to work a bit harder.

Conclusion: in the year of our lord two thousand and twenty three, there are just way too many good daily trainers out there for this shoe to be competitive. If lightstrike is your jam then you're in luck, otherwise there are simply better options available for a similar price

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jdk5vfi] (score 27, diepte 0) Made me chuckle, great review. Completely agree, lightstrike pro is incredible but with normal lightstrike you may as well just run barefoot on the concrete and save yourself some money if you ask me.
[jdlhanq] (score 13, diepte 1 OP) I'll review that next. My foot's 0.3mm stack height could be harsh, but the weight saving might balance the equation
[jdlij2g] (score 11, diepte 1 OP) The problem is that I feel I can only write a review like this for a shoe I really don't like, so producing more requires me to buy the worst shoes I can find and subsequently hate them. That said, I could write a love song for the Deviate Nitro 2 *chefs kiss
[jdk8rmg] (score 10, diepte 0) My experience with lightstrike is very different, same weight as you, I’m at 263km in them. Lots of bounce and support and some really great squish where the lightstrike pro is caged. 

I’ll toss a review of the shoe up at the end of this week.
[jdkcqm1] (score 8, diepte 0) 😝 this is how I felt about Boston 10. I thought $62 was a steal, until I strapped the bricks on
[jdklfkv] (score 8, diepte 0) It aint much but ….TAKE MY UPVOTE !!! WRITE MORE REVIEWS !!!
[jdlrp0a] (score 7, diepte 1 OP) Thanks. As I said in another reply, more reviews requires more bad shoes, which isn't how I want to spend my money. I could become the anti-Seth James DeMoor where I rate every shoe a 1/10, but I reckon the chance of brands sending me their shoes for free so I can slander them is not great.
[jdk6h2y] (score 6, diepte 0) Then when the houses get knocked down and the lightstrike ends up in the ocean, they can skim it out and make new shoes out of it, and say it’s ocean plastic!
[jdkgo64] (score 6, diepte 0) Feel the same way about the Adios 7 I bought during the Eastbay liquidation. At least they were only about $40 all in
[jdlhz8h] (score 5, diepte 2 OP) That's a hot take on the Takumi Sen, I haven't seen a bad word about it until I read that
[jdli967] (score 5, diepte 1 OP) If it was some kind of blind test, like I had no idea what I was wearing and just had to go run 10km in an unknown shoe, I would've said that it was not a running shoe
[jdklcpb] (score 4, diepte 1) Have you also run in the Adios or Bostons?  I’ve been eyeballing a pair for a daily, but can’t quite tell if they’d be redundant or fit in with those two.
[jdl30zh] (score 4, diepte 1) Same with me with the Takumi Sen. Think it’s lightstrike pro but the underfoot feeling is two strapped on boards.
[jdkijvs] (score 4, diepte 0) thank you for helping me to convince myself not to buy the boston 11s that are on sale atm...
[jdlrgco] (score 4, diepte 1 OP) "Adizero SL. Made to walk. Our fastest walking shoe"
[jdk7yp2] (score 3, diepte 0) Most hilarious post written!
[jdkmpl4] (score 3, diepte 3) Heard that was an issue with the 11, luckily I still have some 10s to run in.

I was mostly hoping that the SL could replace the Boston in being a little more than the Adios for daily runs but not quite as chunky as the Boston.
[jdlhml5] (score 3, diepte 1 OP) Fair enough, all jokes aside I think individual biomechanics have a lot to do with how the shoe behaves and feels for you. For the right person the shoe has plenty of good things going for it
[jdlcfmq] (score 3, diepte 1) I bought those too. Have no idea how anyone enjoys running in them. Painful upper and hard midsole.
[jdlis4l] (score 3, diepte 1 OP) A bit more compression in that midsole and it's a great shoe, the way it fits really makes me want it to work
[jdlj6ys] (score 3, diepte 0) On point.
[jdllldo] (score 3, diepte 0) Can you write more reviews on bad shoes? This was hilarious!
[jdlq086] (score 3, diepte 0) Enjoyed the description here! Agree with your assessment of lightstrike as a running foam. At least it's quite light and makes a decent foam for a walking shoe...
[jdkm8uc] (score 2, diepte 2) The adios 7 I’ve heard is excellent for track work, the Boston 11 I started to put miles in and the upper tore.
[jdle57a] (score 2, diepte 4) Adizero SL  is my go to tempo and interval shoe, I’ve done a 25km long run in them no issue, and a couple easy runs.
[jdlbv27] (score 2, diepte 3) Adios for intervals and Boston for tempo has been a great combo
[jdmmli7] (score 2, diepte 2) god damn it. the deal was too good and your review pushed me over the edge.
[jdl5jh2] (score 2, diepte 0) 190Lbs here. I compress this shoe more but it’s interesting to hear how someone lighter than me feels in these.

I completely agree with the fit. It’s almost perfect.
[jdlydac] (score 2, diepte 0) 173 cm and 60kg runner here:

I might get downvoted here, but I’ve really enjoyed running in the Adizero SL (bear in mind I really like the Boston 10 myself and both shoes offer a similar ride). It’s not a ‘fun’ shoe, but it’s dependable as a daily trainer and offers some pop when I increase the pace. I do prefer firmer riding shoes, and the Lightstrike does soften up after a while (I think even quicker than the Boston 10s), and perhaps my biomechanics and foot strike suits this shoe, so each to their own I guess. I might try some other softer and bouncier daily trainers when I retire my Boston 10s (but they are practically indestructible haha)
[jdm3gsq] (score 2, diepte 1 OP) Yea I'm being heavy handed and making sweeping generalisations for the sake of humour, if you like the ride then it's a solid, fairly priced daily workhorse. I think it's just at the extreme end of the spectrum, most would probably find it too firm
[jdlykxt] (score 2, diepte 0) One of the best daily trainers I’ve tried imo. Fits perfect on foot, get outsole, and isn’t really as firm as you’re describing. The bostons are firm, the SLs feels like a different version of likestrike. To each their own. I think it’s a great shoe
[jdm48dx] (score 2, diepte 1 OP) Objectively I don't disagree with anything you've said. Fit is great, no complaints about the outsole, and it's not as firm as I describe (I compared it to tungsten and recommended it should be used as a building material).
[jdk513f] (score 1, diepte 0) Hi there! Thanks for sharing your experience with your running shoes on r/runningshoegeeks. To make your post more helpful to others, please try to include the following information:

- The size and fit of the shoe
- The type of running you used the shoe for (e.g. road, trail, track)
- The distance ran in the shoe (e.g. 10k, half marathon, etc.)
- Your personal experience with the shoe (e.g. comfort, durability, support)

For detailed reviews who have run more than 30 miles(48km), please use the "Review" flair. For first run experiences, please use the "First Run" flair. For a few runs done, please use the "Initial Thoughts" flair. This information will give others a better understanding of your experience with the shoe and help them make informed purchasing decisions. Thanks again for sharing!

Note: This comment has been locked to ensure that the information remains at the top of the comments section and is not buried by other comments.

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/RunningShoeGeeks) if you have any questions or concerns.*
[jdmytfd] (score 1, diepte 3) Don’t get me wrong, it’s very fast, but it’s incredibly firm compared to like the VF for example
[jdnmfwr] (score 1, diepte 4) I thought they were firm when I first got mine but mine feel great now. I think it requires a break in period.
[jdp9so3] (score 1, diepte 4) im just glad to hear theyre doing you good. im looking forward to trying them out!
[jdn9xsu] (score 1, diepte 1) i bought the boston 11s despite the high amount of negative comments ive read here and they turned out to be pretty great

i enjoy them much more than my ultraboosts. ran a couple of 25Ks and had no problems at all
[jdnxbio] (score 1, diepte 2) thats good to hear! i ended up buying them since the deal was so good so i hope i have as good as a time with them as you have.
[jdm3rzf] (score 1, diepte 2) no worries I really enjoyed the banter please make more reviews like these ;)

=== THREAD 1crsus0 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2024-05-14  SCORE: 40  REACTIES: 37
TITEL: Triumph 20 insoles in Superblast! If this is wrong, I don't want to be right. 
POST (source_id=post):
Holy forking shirt. 

I had some arch pain and was rotating Powerstep insoles in all my shoes for a bit, so I had a huge stack of OEM insoles. The thick, bouncy, PowerRun+ insoles from the Triumph 20 were sitting there and I decided to pop them in my Superblasts (~175 miles on the SB). 

It's like a recovery shoe that you can step on the gas at any moment and still feels great at speed. The stack is probably ridiculous, and I'm sure some engineer types will tell me this is not how the shoe was designed and this is stupid. Save it, it feels amazing so far. I will keep doing this until (if) it doesn't. No weird stability or fit issues, just even more versatile now as a legitimate pillowy recovery shoe. 

Just sharing in case you wanted to give it a shot or have done something similar.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l40heg4] (score 11, diepte 0) I put my old triumph 20 insoles in my Boston 12 and it made it so much more comfortable. It made the narrow mid foot actually comfortable
[l4089wl] (score 10, diepte 0) I wish more people would customize their shoes. I’ve cut heel flare off of shoes before.
[l41uc24] (score 9, diepte 2) Yeah if you don’t the upper would crush your foot
[l40rljy] (score 5, diepte 2) I use leukotape-p, usually 4 strips, starting at the bottom of the foot in the arch on the medial side, and rigidly extending it over the medial malleolus and on the side of the foot. I'm sure there are youtube videos and such--I'm using a taping method I learned from my PT/DC.
[l40qdjt] (score 5, diepte 0) I regularly swap insoles. Just taken the Triumph 20 insole and put it in Adios Pro 3s - which basically turns it into a Prime X Strung. Might try a run in it later this week. lol
[l412gkd] (score 4, diepte 1) I have a pair of the Prime X Strung, and I also have a pair of Triumph 20s... 🤔

I'm not sure I have the ankle strength required to tame the resulting monster!
[l4124k8] (score 4, diepte 0) They should sell the pwrrun + insoles separately
[l407f7k] (score 3, diepte 0) I run in custom orthotics, and while I have a pair specifically crafted for low profile shoes, I still did not want to put it in my asics metaspeed edge paris. Instead I tape my arches when wearing that shoe and swapped out the insole for the hyperburst TPEE insole from my Skechers Speed Beast and it is an awesome combo!
[l40azm7] (score 3, diepte 0) I have hoarded those insoles from previously worn shoes. They are so good. Another bonus is they fill out the shoe if you have a little too much volume
[l40wg3t] (score 3, diepte 2) Ride 15/16 I believe
[l40r6fr] (score 3, diepte 0) I’ve done this with the PEBA insoles from the Shift 3. I loved it. Only issue is the upper volume got squeezed and I got all kind of purple toe nails.. would suggest going half size up if this is the plan.
[l417qwe] (score 3, diepte 0) You are einstein bro, i just took the insoles from
My guide 16 and put it into superblast. Feels godly atm
[l405ua6] (score 2, diepte 0) I did something similar with the insoles from the Ride 16 in the Speed 3’s. I had arch pain while running in the Speed’s but after switching the insole it seemed to help. I’m also not sure how bad of an idea this is.
[l48aehx] (score 2, diepte 2) Also a good point. This is actually why I opted not to use my racing orthotics in them. Even though my racing ones are very thin, I am concerned that the forefoot varus post on them will impact the geometry of the plate. Taping my arches and using the stock insole from my skechers alpha tempo seems to be working well so far. The Skechers insole just adds a small bump under the medial arch.
[l40h6wi] (score 2, diepte 1 OP) Nice. What other models use the pwrrun plus insoles?
[l40cuo7] (score 2, diepte 0) I had to do something similar with my Adizero SL's. I was getting blisters in my arch after every run with them so I swapped the insoles for some old Skechers insoles I had sitting around and now they're great. No more blisters!
[l41glgy] (score 2, diepte 1) I have both of these. Did you take the insoles out of the B12 before putting in the T20 insoles?
[l43cus9] (score 2, diepte 1) Amazing I just went and swapped my T20 insoles out with my B12’s. They feel fantastic, can’t wait to give them a test trial!!
[l40wvn4] (score 2, diepte 0) I do something similar with my OG Alphaflys.  The arch causes blisters even though I have high arches.  I ripped out the glued insole (which isn’t much of one) and slipped in another.
[l41zwzo] (score 2, diepte 0) I needed a temporary insole for my wedge sole chelsea boots, while the replacement insole was in the mail. I put in the Triumph 20 insoles and the boots felt like running shoes. In fact I did a short run in the boots with the insoles and that felt great. Those Triumph 20 insoles are wild.
[l46sdwo] (score 2, diepte 1 OP) This is great. Keep us in the loop, and good luck!
[l4042oi] (score 1, diepte 0) Hi there! Thanks for sharing your experience with your running shoes on r/runningshoegeeks. To make your post more helpful to others, please try to include the following information:

- The size and fit of the shoe
- The type of running you used the shoe for (e.g. road, trail, track)
- The distance ran in the shoe (e.g. 10k, half marathon, etc.)
- Your personal experience with the shoe (e.g. comfort, durability, support)

For detailed reviews who have run more than 30 miles(48km), please use the "Review" flair. For first run experiences, please use the "First Run" flair. For a few runs done, please use the "Initial Thoughts" flair. This information will give others a better understanding of your experience with the shoe and help them make informed purchasing decisions. Thanks again for sharing!

Note: This comment has been locked to ensure that the information remains at the top of the comments section and is not buried by other comments.

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/RunningShoeGeeks) if you have any questions or concerns.*
[l40ok0g] (score 1, diepte 1) Wait, tell me more about taping for arch support.  I have some Magic Speed 3s I haven't run in yet (got them at an insane price) because I can't get an orthotic in.  I usually wear Superfeet Run Comfort Thin (blue) in my Novablast 3 and my Endorphin Speed 3 and am nervous of running without any support at all.
[l40zqx2] (score 1, diepte 3) Off to the depths of youtube I go....  Thank you.
[l47ksox] (score 1, diepte 1) Interesting point. Gotta wonder how custom orthotics or aftermarket insoles affect the specific design and cushioning system the manufacturer had for the shoe.
[l416qos] (score 1, diepte 2) Guide 16
[l42fdit] (score 1, diepte 2) Peregrine, Endorphin Shift 3
[l4hdry8] (score 1, diepte 1) I need to do this with my ride 15 insoles! That Boston 12 midfoot crushes me, though the pain usually goes away a few miles in.
[lv6s00f] (score 1, diepte 1) Did you have the pwrrun foam insole or thin formfit ones?
[lv7jz37] (score 1, diepte 2) The pwrrun insoles. The ones that come with the triumph 20
[l40io53] (score 1, diepte 0) I tinker with my insoles all the time! It helps with cushioning as well as width management. The best thing i have is a removable underlay i got with the peregrine 10. Just inserting then beneath the normal insoles raises the height just a little bit for my rebel v4s, making them almost a perfect fit for my feet.

In addition, boomerang insoles are good as substitutes insoles for certain shoes that might be slightly less cushiony for my liking. These thicker insoles increase shock absorption and protection from rocks while at the same time reduce sensitivity to ground (negative effect). So don't forget to mix and match to your desire, and end up possibly turning your great shoes into perfect ones.
[l43fe99] (score 1, diepte 2) Have the same, I dread running downhill on cumbered roads with PXS but works like magic on uphills and flats
[l421aiv] (score 1, diepte 0) \*looks at my xodus 2 ultras\*

I haven't used those shoes much, but those insoles are something you won't find in any other shoe. I wonder how they will feel in other shoes
[l42zz08] (score 1, diepte 0) This is the way!

The nicest insole out there combined with roomy Asics (Superblasts even more so)! I moved my T20 insole into the Noosa. Surprisingly, can still feel the rise on the inside of the hill of the insole.
[l45v0h7] (score 1, diepte 0) My nimbuses felt too hot after a couple of miles so I swapped the insoles with my noosas and that made all the difference! Noosas are more comfortable and no heat issues with the Numbused as well. Win-Win!
[l461wnw] (score 1, diepte 0) Do the opposite take the insoles out the Superblast and put it in the Triumph and you'll see what a rubbish shoe that is without the insoles!
[l4dvvjv] (score 1, diepte 1) I actually removed the insoles from my Triumph 20 as last resort and put in my insoles from my Endorphin Speed 2 and FINALLY the Triumph 20 went from making my forefoot numb after 4km to the best daily/long run shoe ever.
[l46s368] (score 1, diepte 0) TLDR - I made a Prime X Strung.

OK, so I've just done a 10k run in my new hybrid supershoes. Put the Triumph 20 insole into my Adios Pro 3s.

Some trade-offs/pros & cons.

The AP3s had been giving me serious pain around the cuboid/outside of arch. PB in HM, but too painful for longer.

The T20s were...meh. Just felt like a brick - didn't particularly feel cushioned.

Well, the experiment was something else. Did the exact same route as yesterday, same weather conditions.

The energy return/bounce is now insane. Most fun shoe I've run in, like a NB Supercomp Trainer V1, but wilder.

The insole is about 7mm, so the stack has increased and there was more stability issues.

They also weighs 33/35g, as opposed to 10g for the AP3 one. Could definitely feel the extra weight as it's all underfoot. Now weighs the same as NB SC Elite V4, but that feels lighter.

I had upper/lacing issues with the AP3 - no issue now, as the extra volume makes it fit like a glove - albeit, probably just too much. I'll try thinner socks.

Didn't actually feel that much more cushioned...but that return.

No cuboid pain. 

Got a HM in two weeks and I may give them a proper outing.
[l8l6ie2] (score 1, diepte 1 OP) How was DIY Adios Prime X setup for the race (and other runs)?
[l8lp4g3] (score 1, diepte 2) Didn’t race in them. Too unstable for me. Tried a 10 miler in them and decided the experiment was over. Cuboid pain came back, which is definitely an issue with the AP3 as no problem with other shoes.
[l47duro] (score 1, diepte 0) my ride 15 insoles are the same powerrun+ insoles and I use them with my gel 30s 😊
[l47ki6c] (score 1, diepte 0) I still use insoles from 2014 ASICS Cumulus, somehow they totally eliminate hot spots, etc in all my shoes.
[l4duupp] (score 1, diepte 0) I put Speed 2's insoles on top of my Speed 3's and they are fantastic.
[l47653x] (score 0, diepte 2) Thank you. Thing is, I regularly swap insoles but never thought about using the T20s because of the extra weight.

