# Label-batch batch_0129

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
Schrijf het resultaat naar `batch_0129.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1siykri, bz8q6o, 1glwb4b).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1siykri ===
SUBREDDIT: r/hiking
DATUM: 2026-04-11  SCORE: 6  REACTIES: 67
TITEL: Problematic feet, which shoes?
POST (source_id=post):
My feet hate hiking. I’ve tried three different shoes over the last three years: Topos, Altras, and Hokas. They’ve been professionally fitted and chosen based on all the recommended metrics (little bit big to account for swelling, wide versions, etc).

Here are my issues:

\-Persistent blisters, never in the same places

\-Annual loss of toenails (5 in 2025, never fewer than 1)

\-Plantar fasciitis in one foot (new in 2025 but still present)

\-General ache and soreness, which is the least of my problems 

I treat hotspots early and put in a heel lock as needed. The last heel lock I did gave me such a severe blister that it healed with hyperkeratosis. I put supportive inserts in my shoes once the PF developed, but I can’t tell if they’re helping. I wear smartwool or Darn Tough socks. 

I’m curious if I’m missing something in how I’m handling my feet. I’m committed to trail runners, not boots, and open to brand recommendations if you’ve got a silver bullet shoe.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ofntw4y] (score 22, diepte 0) Jfc, go bigger and the shoes should feel good immediately. Toe nail loss should basically never happen.


Are you doing mountaineering shit in trail runners? What kind of terrain are you moving over?
[ofnziv2] (score 13, diepte 0) Regarding the socks and blisters, I usually wear liner socks too.
[ofnzumc] (score 10, diepte 2) half to a full size up is the normal way to go. You can still achieve lockdown w/a bigger shoe. Maybe you have a really narrow foot.. You might want to try some of the Euro brands like Sportiva, Dynafit, Scarpa and see how they feel. 

Your foot should be locked down but not pinched. Lace 'em up tight but you shouldnt have to strangle your foot or ankle if using a heel lock. 

Something is not right here, obviously. I hate to ask this stupid question but are you tying your shoes tight?
[ofnrwnx] (score 9, diepte 0) Genuine question: why are you committed to trail runners vs boots?
[ofntt6h] (score 7, diepte 0) So they aren’t runners but they also aren’t boots. 

But the Danner 2650 saved my hiking season when Altra ruined the Lone Peak. No blisters, no foot pain as someone who also has some PF issues, great traction.
[ofns9bd] (score 6, diepte 1 OP) I find boots too heavy and hot. I don’t need the ankle support and I want to cry shoving my feet back into them after long days backpacking. I do own a pair that I like, but only in cold or snowy weather. They’re great when it’s cold!
[ofofj0v] (score 5, diepte 3 OP) My feet are actually tragically wide, and super flat. Yes, I’m lacing very snuggly.
[ofo6sad] (score 4, diepte 2) Is your foot pizza slice shaped? Mine are.... I have a hard time finding hiking shoes because if the shoes are tight enough in the heal, my toes rubs and my toenails suffer. If the shoes fit in the toes, my feet slide around and I get blisters..

The Xero Mesa 2 and Terra flex are the only shoes I haven't had that trouble with. I love them.

However they are barefoot shoes and don't have any support. 

You have to train your feet to wear them... but that will help your PF and foot pain anyway. And I mean like serious foot exercises... like single leg calf raises with weights on an angle board or edge of stairs. Walking around barefoot and on your tip toes as much as possible. You also need to stretch your Achilles. Resistance bands are very helpful. Roll you feet with a spikey ball to help with the PF.

I hope you can find shoes that work for you.
[ofnwss8] (score 4, diepte 0) Scarpa zodiacs, they’re the most comfortable boots I’ve ever worn. No breaking in period, never had a blister.  
You need to change the style of shoe you’re wearing if multiple brands in the same category yield same results.
[ofntsyd] (score 3, diepte 1) Maybe worth checking if your gait is causing some of these issues? I had similar problems with random blisters until I realized I was landing weird on uneven terrain. Also those insoles might actually be making things worse if they're changing how your foot sits in the shoe - I know few people who had to go back to basic insoles because the fancy ones created new pressure points

  
For what its worth I switched from trail runners to approach shoes for technical stuff and it helped a lot with toe issues. Not boots but more protection than regular runners
[ofotiz0] (score 3, diepte 4) Your feet swell and slip forward just a wee bit anyway going downhill. You really should buy your Altras or whatever hiking shoe 1/2 to 1 size bigger and cinch it down. Not everyone can wear the flatter shoes. You may want to try a lightweight boot like Lowa or other.
[ofp2zgx] (score 3, diepte 1) This.  Wool/darn tough socks as one layer, and a thin, really low friction sock over the top.

The goal is to make the point of lowest friction the sock to sock surface, not the sock to skin surface.
[ofof9cn] (score 3, diepte 0) This sounds crazy, but it worked for me (I’m crazy btw): Start walking barefoot. 

I had bruised the heel of my foot skiing and it as not getting better no matter what I tried. So since I couldn’t comfortably walk with shoes on, I just started going barefoot. Initially short dog walks on smooth pavement (our street had been recently resurfaced). Walks got longer, my feet became stronger and calluses developed so I essentially got used to walking barefoot and the feet became desensitized to rough surfaces and terrain. Plantar fasciitis went away and on terrain hikes I could wear my hiking shoes again.

Now I can do both comfortably, and have discovered the joy of barefoot hiking - I do it whenever I can
[ofowi6b] (score 3, diepte 1 OP) I’ve thought about it. I take Chacos as camp shoes since my tortured feet need to breathe at the end of the day, and I’ve strongly considered hiking in them when my feet are at their worst.
[ofnutaa] (score 2, diepte 1 OP) I’ll take a look, thanks for the recommendation!
[ofnuoll] (score 2, diepte 1 OP) Just normal trail with a 30 pound pack.  Rocky and uneven often, but nothing I’d call extreme. If I go bigger the shoes will be a full size larger than my typical shoe, so I’d be slipping around in them like clown shoes. If that’s the right trade I’ll made it, but I feel like I’m clumsy enough without that much extra shoe in the toe.
[ofoczia] (score 2, diepte 3) Team pizza-shaped feet.

I call them triangled shaped.

I have been in Nike Zegamas for multiple years now.

They are narrow. They have the little arch sling that helps stop you jamming your toes in the front of the shoe.

And, damn, they have stick. Even when the tread is warn down, they have incredible stick. Which makes sense if you think about Nike creating shoes to have good stick on slick, smooth basketball courts. Getting good stick on the rocks and changing terrain of trail is much easier.

The uppers are very soft, which ensures good overall fit.

The only thing I think I am going to change up in my current pair is the laces. I do have to heel lock and with the shape of my feet, the heel lock ends up sawing through the laces / tearing apart the upper eyelets.

No tie laces from Nathan really helped save my road shoes. I need to get some into my trail shoes as well.
[ofofoul] (score 2, diepte 3 OP) I would describe them as very wide hot dog buns. Super flat, no arch, basically one width the whole way down. Maybe slightly narrowing at the heel, but not a lot.
[ofpexf9] (score 2, diepte 4) Have you worked with a PT to build foot/arch strength?
[ofqzsj4] (score 2, diepte 1) I sized up a full size and my feet were rubbed raw because there was too much room.

I sized up a half size and I lost toe nails because my feet kept slipping forward and knocking into the toe box.

I went with my regular size and the boots fit snug, but perfect. No more blisters, no more bruised toe nails.

My point is everyone, and every shoe is different.
[oftwu5t] (score 2, diepte 2) Haha, i always thought the thin liner was the first layer on your foot; en then the big sock. And when i know i’ll get blisters in one spot; i put a bit of kinesio tape on the spot; prevents blisters too!
[ofoc8ut] (score 2, diepte 0) For the toenails. Have you tried going up a half size? Your feet swell as you walk sp they need bigger shoes. I recently bought new hikers. I went to REI and spent over an hour trying different brands and sizes and walking up and down that rock thing trying downhill, uphill and side angles. I walked 6 5 miles this weekend in brand new boots with no hotspots.
[ofodnv2] (score 2, diepte 1 OP) Yes, I buy a half size larger than I normally wear (dependent on the shoes, some fit at larger or smaller sizes and I go up from there).
[ofrg5c6] (score 2, diepte 3 OP) Thank you! Never heard of Wrightsocks, but I’ll take a look.  The slant board is part of my gym routine.
[ofpi8x9] (score 2, diepte 1) How are you keeping rocks and stuff out of the sandals? I've tried hikes in my Z Cloud 2's and was having to constantly walk funny to dump out pebbles and any little thing that got in them.
[ofrivvf] (score 2, diepte 2) I wear the Z/ Cloud 1s, possibly different. Peebles usually fall back out, but maybe a couple times a day, I have to remove something. It's analogous to tying my shoelaces. It does take some getting used to, but I almost never get blisters. The wide strap is better for me; the regular strap lets my little toe stick out too much. I broke my little toe into the outer metatarsal that way! But I've also broken my ankle in sloppy Altras, and feel a lot more secure on my platform in sandals.
[ofp9659] (score 2, diepte 0) I never suffered as you did, but my transition was innov8 270 gtx (or something)  to new balance hierro V4 or 5 to brooks divide 3 (twice) to brooks cascadia (16 and later 19).

The last 2 (divide and cascadia) were game changers in terms of foot comfort with the cascadia 19 being the best of the lot.
[ofpnrr4] (score 2, diepte 0) I know you wear Smartwools or Darn Toughs (A+ for DTs), but are the socks too thick for the shoe?
[ofoix0f] (score 1, diepte 1) so awesome. No idea how they can feel so good without feeling squishy. I also wear Altra and Hoka. Pretty sure the 2650s have given me the least amount trouble, and right out of the box. I’ve done 15 mile days without much to complain about. 

Darn Tough socks help a ton, or that sock that comes with its own liner, can’t remember the name. 

I still lose 1-2 toenails a year, but that’s more from jogging or walking every day.
[oftow7o] (score 1, diepte 4) The right shoe can depend a lot on your [foot type & volume](https://anyasreviews.com/best-barefoot-shoes-foot-type/). And plantar fasciitis is typically a symptom of calf tightness/issues that happens to show up in your foot vs being a foot problem.
[ofrgbxd] (score 1, diepte 5 OP) Yes. I did PT for like 6 months and still do the exercises at home/the gym.
[ofrih5k] (score 1, diepte 6) Have you progressed them?
[ofonr61] (score 1, diepte 2) My hiking shoes are a full size up, technically 1.5 sizes, I think. And they’re Altra Olympuses, so they’re already pretty roomy to begin with. Altra have different feet shape for the different models, so some are more generous than others with the width. I do like my Topos, they’re just not as secure as I want on my feet to do any serious hiking with them. 

For your plantar fasciitis, Superfeet insoles work really well for me (the green variety), but I have fallen arches and not actually flat feet. And I have to size up to get the arch to hit in the right spot and trim the toes back. Treadlabs work well in my daily shoes, and they have different arch heights, but I don’t trust them as much for high mileage days. 

It takes some experimenting with different options to find the one that works for you. Buying from a store that allows returns (within a reasonable timeframe) even for shoes and insoles that get used really helps.
[ofqwt7b] (score 1, diepte 2) A 30# pack vs a 20# pack can be the cause of blisters in my case. It could also be leading to some of your other foot issues. A size up is very common in hiking shoes. If I don't size up, my big toe will bang the front of the shoe on downhills. A heavier pack will emphasize that. 


Depending on your for shape, those shoes with wide toe boxes may not be right for you even though they're popular with the majority. La Sportiva Wildcats or similar might be worth trying on at the store.
[ofnu72y] (score 1, diepte 0) None of those three brands work for my feet either. I wear sportiva Bushidos. My feet like saucony peregrines too although not for hiking.
[ofo182u] (score 1, diepte 1) I had similar issues with Topos and Altras so I came to say Saucony Peregrines worked for me! It is my fav hiking shoe now.
[ofobr83] (score 1, diepte 1) This answer makes sense.  Normal trails with rocks, roots, fallen limbs, carrying a pack, none of the trail runners work for your feet.  I’d be trying a mid boot, try on with liner and hiking socks, then you have the advantage of putting the heel lock around your ankle, as intended, not the top of your foot.  I tried it with hiking shoes and created some pretty intense pain across the upper top of my foot.
[ofnx4a1] (score 1, diepte 0) If you can, see a physiotherapist who can address gait issues, etc.
[ofnxlch] (score 1, diepte 1 OP) I’ve been in PT off and on for the last 3 years. I tore my ACL in 2023 and did a year of PT, then did about 6 months over the last year for the plantar fasciitis. Is “I get blisters all the time” something a PT can deal with independent of other issues? (Side note: my foot issues predate the torn ACL, I wore boots back then with the same results)
[ofny5mp] (score 1, diepte 2) Yes! I have been seeing a physio for years for patellofemoral pain syndrome. One day I mentioned for a new exercise that it hurt my big toe that I have random problems with. She asked to take a look, figured out the issue with my toe, also noticed early signs of potential bunion development on the outside. She had me put my shoes on, felt how my toes fit in them, assessed my gait, etc. and helped me find a new pair of shoes. I’m not sure if every PT is trained in this, I honestly just got lucky
[ofu4xtm] (score 1, diepte 3) Might be better that way?

I do the opposite because the thin socks i have dont deal with sweat well.
[og1o85k] (score 1, diepte 4) Whoa I've always gone liner underneath my wool socks but they always bunch up around my toes on downhills so I'vehated liners. I gotta try your way
[ofo0qzr] (score 1, diepte 0) Make sure your shoes are big enough first. My preferred sho is the Xero Shoes Xcursion Fusion. They are minimalist boots.
[og22zb2] (score 1, diepte 2) I started sizing up pretty aggressively (1-2) sizes, and that made flats better for me, but I was bunching my toes in the downhill. I tried the heel lock, and was unimpressed. I don't see this idea mentioned enough... It was a tip from the military, but I didn't need it back then so I almost forgot it. Don't lace the bottom pair of eyelets, maybe 2. This way there is more support in the mid foot, and it's tight enough to prevent the slide forward. It was a game changer for me
[ofoe8ni] (score 1, diepte 0) For losing toe nails, typical recommendation is a larger boot and/or boot with larger toe cage. For me, I switched to Keens. I don't know trail runners. Try a larger pair. They should be snug, not tight.

For blisters, your socks sound good. Might help to check you feet halfway through. Apply bandaids or moleskin to hotspots. Change socks. I assume you keep your feet dry.

For Plantar fasciitis, try stretching. A podiatrist can give you a shot of cortisone that helps. 

Your foot sound worse than anything I've ever seen. I'd probably try a few things and go to a podiatrist. Good luck.
[ofofbc8] (score 1, diepte 1 OP) I should’ve said that I’ve seen a podiatrist. She sent me to PT, which I went to for about 6 months. They gave me all the exercises and stretches and did dry needling. I’m still exercising and stretching. I’ve seen my regular doctor to check on the toenail regrowth (I lost a big one this year because of trauma) and the hyperkeratosis.
[ofoj633] (score 1, diepte 2) You did more than me with your docs. I had one shot of cortisone that really helped. I would also stretch. Condition seemed to go away, though I do pay attention to how I walk. When walking to work, sometimes I slow down and make sure my foot is relaxed, toes are spread, and foot is comfortably planted.

The Keens helped too, but I've only had them about 1 1/2 years.
[ofzv15f] (score 1, diepte 1) Yep I was gonna say this but not so extreme

OP can wear barefoot sandals and start to walk slower, be more cognizant of where he walks and strengthen his feet.
[ofomzr3] (score 1, diepte 0) Have you tried Saucony? I went through many brands of shoe, and those are the only ones I hike in now. 

REI carry Saucony in their bigger stores but not their small stores. If you get them at REI you can exchange them after trying them for a few days if they're not right for you (I got a size too small, wore them for a week, then REI let me swap for the half-size up)
[ofow4ko] (score 1, diepte 1 OP) I actually wear that brand to run! Or I did before my plantar fasciitis kicked off, I’ve avoided running since then. I’ll check out their trail shoes.
[ofp6uu1] (score 1, diepte 2) Have you tried a slant board? I got one to work on stretching out my calves and two of my friends with PF got the same one and both felt like it was pretty life changing. 

Also, have you tried Wrightsocks? They’re a double layer blister reduction sock and I love them. 

Saying all of these things, I’ve recently developed blisters and foot pain that the socks and the slant board are not tackling. I’ve never been prone to blisters and now BAM, all blisters all the time. It’s weird. 🤷‍♀️

I hope you find relief.
[ofrx1sr] (score 1, diepte 2) > plantar fasciitis

Btw you can eliminate plantar fasciitis by applying verapamil gel. It takes a few weeks (almost two months for me) so it's a drag to do, and after rubbing it in it needs to be covered with a large bandaid. Verapamil gel isn't easily available; I had to get it made up at a compounding pharmacy. There are online compounding pharmacies which can supply it but it's less costly if you can find a local one.

Funny aside: verapamil gel is used for relief of Peyroni's, so my jars were labeled "apply to penis as directed" lol .. but it did fix my pf some years ago, with no recurrence!
[ofow9k5] (score 1, diepte 0) Sandals changed my life
[ofowvc5] (score 1, diepte 2) If you're already hauling Chacos, just try it. I like the Z Cloud Wide Strap for hiking. I literally never ever get blisters in Chacos
[ofoxene] (score 1, diepte 3) Also really loving the Merrill Trail Glove; I'm hauling these two shoes on an upcoming thruhike
[ofrxsfz] (score 1, diepte 3) I have quite wide feet and it's been a very difficult and expensive journey finding shoes that fit for daily wear, let alone work for hiking and backpacking. Lone Peak in a wide just happens to be the exact shape of my foot and I like them. I was trying sandals as they don't rely on the upper part of a shoe and give me much more freedom for width. I haven't been able to find a sweet spot between them letting debris in and feeling cranked down.
[ofoxgq6] (score 1, diepte 0) Did you try on hiking boots perhaps? They’re heavier, and are not as light as trail runners, but generally have more leather on them, leather will naturally conform to your feet..

My lineman boots will never accompany me on a hiking trip, but they fit like a glove. After a week or so break in, they’re great..

I know there are some traditional hiking boots still out there…

Oh, and Topo also has some of their stuff in wide. I have wide ultraventures or whatever by Topo, and they’re awesome summer hiking shoes.
(20 reacties met lagere score weggelaten)

=== THREAD bz8q6o ===
SUBREDDIT: r/Disneyland
DATUM: 2019-06-11  SCORE: 24  REACTIES: 67
TITEL: best shoes for walking around for the WHOLE day at disneyland???
POST (source_id=post):
what are good shoes for spending the whole day at disney?? usually when i go it feels like my feet are going to fall off! i can never find the right ones. im a girl with kinda wide feet .. pls help :))))

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[eqqzw1d] (score 38, diepte 0) Adidas ultra boost.  Light and soft.
[eqr6vfz] (score 22, diepte 0) Everyone’s feet are different, but I find that if I change my socks at least once in the middle of the day, it refreshes my feet a bit.
[eqr1gjp] (score 11, diepte 0) Basically you want good support and not too much pressure on any point of your feet.  I’ve had some shoes that are really tight on my toes and result in blisters easily. 

So look for good ankle support, don’t tie laces too tight and you should be set. Good socks help a ton as well. Nikes are good. Thats what I wear.
[eqrleqy] (score 11, diepte 1) Lol I always throw in 2 pairs of socks in my backpack before heading to the park.
[eqs0qoa] (score 9, diepte 0) i swear by teva's. ive worn them the past 3 times ive went to disneyland and theyve been great everytime. just bring some bandages as they can sometimes rub after getting on the water rides because they can get slippery
[eqr1gtz] (score 8, diepte 0) OluKai Ohana flip flop/sandal.  They have arch support and are really comfy.  I wear them 99% of the time I am in the park.  

Opt for the men's version if your feet are too wide for the women's.  I've got both styles b/c I am a women's size 11/men's size 9 so I grab whatever color I can find on sale.

If you have a Nordstrom Rack in your area, check there first because they will sometimes have some on sale for $35-$45.  They have them on the end caps in the shoe department and they will be hanging with other brands so you have to take a good look at what they have.

They retail for $64.95 but they are also an item that goes on sale during the Nordstrom Anniversary sale in the summer.
[eqrlv4q] (score 8, diepte 0) I always stick with Adidas Ultra Boost for the park. They’re kind of pricey at $180 but I always wait when they go on sale. Sometimes you can find them for $100-$120. You can try Eastbay they always have them on clearance and shipping is free.
[eqs4m72] (score 8, diepte 0) Adidas Ultraboost seems to be very popular here.  Do any of you that own them have a comment on how well they dry after a Splash Mountain or Grizzly River Run?
[eqrtz1d] (score 7, diepte 1) It’s like walking on air. They are so cushiony, lightweight, and breathable.
[eqs0kzi] (score 7, diepte 1) Yes. The best comfort ever.
[eqrncs1] (score 6, diepte 3) Sometimes I even throw in a pair of sandals so I don’t get my socks and shoes wet on Splash Mountain lol!
[eqreapt] (score 6, diepte 0) ultra boost, if you’re on a budget buy insoles
[eqrqptb] (score 5, diepte 1) Only problem that I have with Nike is that sometimes people don't realize they wear a wide, and Nike doesn't really carry wide shoes so they end up buying too large a shoe just to fit wide comfortably and end up with way too much room in the toe box.
[eqsfo5c] (score 5, diepte 0) I'm a big fan of the Sketchers Go walks.
[eqsa3w9] (score 4, diepte 1) Literally came here to say this! Loved my everyday ones so much I got a pair just for work. Walked around all of Tokyo Disneyland/Disney Sea and pretty much all of Japan in January in my pair and never had my feet hurt!
[eqrn9ta] (score 4, diepte 2) It makes such a huge difference!!
[eqrtsgo] (score 4, diepte 0) I’ve worn Adidas Ultraboosts, Adidas Nite Joggers, Nike Metcons and Vans ample times. Both Adidas options have left my feet feeling the best, both at the end of the day and the day after. 

Not Disney, but I also wore my ultraboosts last summer on a 10 day trip to the East Coast, where I averaged 13 miles walked each day. I had zero issues with them.
[eqsma8e] (score 4, diepte 0) I usually wear dr martens when i go to Disneyland, which is usually a 14 hour day for me. Every other shoe ive worn makes me feet hurt half way through the day
[eqr2eea] (score 3, diepte 0) Ultra Boost
[eqr7a52] (score 3, diepte 0) I have wide feet, and got my feet properly measured. I was a full size less, double wide! New Balance shoes ordered via Zappos. I did 8 days at WDW with happy feet.
[eqr7shc] (score 3, diepte 0) Find some comfy shoes and grab good insoles. I have RedWing and Doc Marten boots with Superfeet insoles.
[eqrjyls] (score 3, diepte 0) It's not even the walking that kills you, it's the standing. I carry flip flops with arch support in my backpack and change out part way through the day and then back at night. It helps a ton.

I'd go with a lightweight sneaker.
[eqry3ur] (score 3, diepte 0) Ultra boost if it’s cool, vionic sandals if it’s hot. Most importantly, remember “Eat up? Feet up!” If you are eating try to have your feet up, on another chair, on a friend, whatever you can find. Those few minutes a few times a day will make a big difference.
[eqwln1q] (score 3, diepte 1) I was skeptical of these - but they were incredible! I actually had Go Run Skechers - they were inexpensive and the most comfortable shoe in my stash. I'm a little on the chonky side and out of shape, so I wanted footwear that would provide some padding and comfort. I switched days between Ultra Boosts and the Skechers and the skechers, amazingly, were the better shoe for me. Did five days in the park.
[eqsqsw4] (score 3, diepte 0) Allbirds. Thank me later.
[eqt5etz] (score 3, diepte 0) Anything that's light, supportive, and not springy, like a trail running shoe. Springy shoes get exhausting over time because they make your foot work a teeny tiny bit more with each step.

I like my Fila ones.
[eqtnvu0] (score 2, diepte 1) 100%.
[eqtmz8v] (score 2, diepte 3) Sketchers makes the best wide shoes IMO.
[eqrxaz5] (score 2, diepte 1) I second this. They make a model with a thinner strap too that I love even more because it is personally cuter to me.
[eqr1sk0] (score 2, diepte 0) Look at Brooks tennis shoes, which are made a little bit wider in the toe box. Lots of cushioning and great arch support. If not those then check out Mizuno's. Equally amazing! Otherwise, I wore my Asics last year and they were fine. I wore them all day, but it was the fact that I was spending 5 days in the same shoes that became a problem.

If you're not looking for a tennis shoe, maybe try out some sandals by Vionic, Clark, Merrell or Keen. Merrell are a little too stiff for my feet and Vionic has too high an arch support. Everyone's feet are different, though, so you might want to check out a couple different options.
[eqt0fom] (score 2, diepte 1) You made me Google the definition of "bogan" and now I feel like such a bogan for not knowing the word...
[eqrntra] (score 2, diepte 4) That’s a good idea!! That is definitely the worst - wet feet in wet shoes that just won’t dry.
[eqrmkzj] (score 2, diepte 2) All my life I thought I was a 7-7.5 W and suffered with what I could find locally, mostly Payless. Then I found out cheap mass produced shoes for most "normies" was my problem. Now, I regularly spend the money on quality shoes in 6-6.5 WW and feet have never been better. Plus I have many more style choices and the last longer.
[eqrcbxl] (score 2, diepte 0) No help with specifics, but I do find that if I am going for more than one day, changing my shoes helps sooooo much. It seems that my body gets tired of even the most comfortable shoe, so when I wear one pair the first day and another the second, then switch back and forth after that, my body is much happier.
[eqrd2xw] (score 2, diepte 0) I always either wear my Birkenstocks - the ones with the strap that goes around your toe, not the classic two-strap ones- or I wear some Nike gym shoes with orthopedic inserts. To be honest, those inserts are probably what save my feet whenever I go. I use them for my long work days on my feet as well, and I’m able to go for hours and hours with minimal pain at the end of the day.
[eqrhsww] (score 2, diepte 0) Merrell shoes are great for that. I originally started wearing them when I did a hike in Iceland across an old lava field. It was basically a long hike across jagged rock. They handled that job and every job since, including Disney trips. I never have problems with my feet. I used to get bad blisters when wearing other shoes for that sort of thing
[eqri3qx] (score 2, diepte 0) I really do think this is totally a matter of personal preference, however, my life changing 5-days-in-a-row at WDW and the far easier DL jaunt have been Toms and Allbirds. I have wide feet too and can’t do a “normal” Toms. I have to do the Avalon Or Alpargata (I think?) and ANY Allbirds are great.

I do even better if I pack both and alternate shoes each day, but even if I don’t, I have zero issues and it used to be the worst thing about going to Disney was hobbling around the next day.

Good luck! I hope you find your life changing shoe too!
[eqrl085] (score 2, diepte 0) The last time I went to DL I wore Clarks flip flops. I don't like closed toe shoes in hot weather. They have some cushion to them. For an athletic shoe, New Balance generally runs wide.
[eqroopn] (score 2, diepte 0) I wear Brooks, but I would say any good pair of running shoes should work. It’s a marathon not a sprint :)
[eqrp4x9] (score 2, diepte 0) Depending on weather I switch between casual sneakers (skate shoes, like vans, I do not recommend for everyone but they work for me), Birkenstock’s, and Chacos *but* I used to wear my adidas to the parks and those were usually pretty great for all day wear.
[eqrxi7f] (score 2, diepte 0) I have wide and flat feet. I’ve used adidas ultraboost or Nike epic reacts both very comfy. Nike epic reacts are at the top of the list at the moment though.
[eqs7ii7] (score 2, diepte 1) I endorse Tevas as well! I switched up between 2 different pairs each day and never had a problem. Sandals also help keep your feet nice and cool!
[eqs2po9] (score 2, diepte 0) Im for sure in the minority about this, but Converse has a Chuck Taylor line i think referred to as the Vintage line or something similar, but they have extra padding in the soles. I really like them because  
a) the dry pretty fast  
but also  
b) you can loosen and tighten them much more than just about any other shoe, and when your feet inevitably swell because of the heat and the sore-ness, it's nice to have that as an option.
[eqs3r8w] (score 2, diepte 0) Any supportive Nike running shoe for me.
[eqsb00b] (score 2, diepte 0) cushioned water proof sandals.  Avoid the fuzzy or fabric sandals, and go with a synthetic with a soft sole.  This way you can just wipe off if you happen to get wet on a ride, but remain light and airy.  And yes, I do shorts/tshirt/sandals in december at disneyland.  Must be the canadian blood in me.  I have a pair of columbia and a pair of merrells that I use for this purpose.
[eqsbgya] (score 2, diepte 0) All I can think about is that one modern family episode when they go to the park and Gloria decided to wear heels and refused to take them off until Jay bought her those soft fuzzy Minnie slippers!
[eqsj6p3] (score 2, diepte 0) My son and I prefer Salomon trail running shoes, XA Pro 3D. Reasonably light, good support, durable and the kevlar lacing system with the slide so we never have to worry about tying shoes or catching on something. Have made several trips to the parks with these.
[eqt2opc] (score 2, diepte 1) Absolutely 100% this. They're fantastic.
[er72nqb] (score 1, diepte 1) Best. Shoe. Ever.
[eqr18wq] (score 1, diepte 0) Nike Roshe, bang for the buck shoe ~$40-70 depending on where you get it and what color you get. 

Good foam sole and mesh upper so “wide” feet aren’t to much of an issue, plus the upper being 100% mesh allows your feet to cool and air out for comfort.
[eqsweig] (score 1, diepte 2) I agree Nike is not for people with wide feet.  My feet are wide and I find adidas fits better.
[eqr3qfr] (score 1, diepte 0) I have dead flat wide feet. When I went to Disneyland my feet absolutely killed me! 

I am going to Disney world next year and will be taking my zero drop/barefoot thongs (flip flops). I find that my feet are more comfortable barefoot. So these are the closest to that without looking like a bogan.
[eqt4kmt] (score 1, diepte 2) hahaha
[eqrlixt] (score 1, diepte 1) What kind of new balances did you order?
[eqrm9p8] (score 1, diepte 2) Similar to these, sooooo comfy. https://www.zappos.com/p/new-balance-ww877-silver/product/8302415/color/632
[eqrr79r] (score 1, diepte 3) I used to have the same issue. Now I stick to New Balance and Saucony and pick them up whenever I see them on Woot.com
[eqrvz50] (score 1, diepte 1) Seconding ultra boost!
[eqtn8ah] (score 1, diepte 1) I love my tevas in the summer too, I get the leather so they don’t Chaf as much
[eqs95yo] (score 1, diepte 0) I've been happiest with Ecco sandals. Got the at nordstrom before a recent trip because the shoe salesman highly recommended them. I don't really like sneakers so they are perfect for my style https://m.shop.nordstrom.com/s/ecco-flowt-strap-sandal-women/5038511?origin=category-personalizedsort&breadcrumb=Home%2FWomen%2FShoes%2FSandals&color=black%20leather
[eqsby9a] (score 1, diepte 0) Brooke’s
[er30pha] (score 1, diepte 1) Not springy *like* a trail running shoe, or not springy, for example, go with a trail running shoe?
[er3t63v] (score 1, diepte 2) No, Anything that's light and supportive such as a trail running shoe, and not springy.
[eqtmlvp] (score 1, diepte 0) Walking shoes, not running shoes. Your foot steps differently running vs walking. After I realized that and bought a pair of new balances intended for walking, athletic shoes are finally comfortable. (I don’t have wide feet but very long toes and big feet for my size)
[eqx65j4] (score 1, diepte 0) I usually wear some nice broken-in Clarks sandals. Don't make the mistake of buying shoes specifically for a day at Disney and not having worn them for weeks prior to get them nice and broken in.
[er33tx4] (score 1, diepte 0) I just got a pair of Altra Lone Peak 4s and they are my favorite shoes ever. Nice wide toe box so your toes have room. Have not taken them to Disneyland but I just wore them for a week of vacation in Washington State that included both hiking and urban walking and my feet rarely hurt at all. I got mine from Amazon but REI often has coupons and has a great return policy if they don’t work out. 

The other thing is to buy sneakers up at least a half size. I wear a 7.5 in normal shoes but have an 8.5w in my Brooks sneakers. Makes all the difference.

=== THREAD 1glwb4b ===
SUBREDDIT: r/weddingplanning
DATUM: 2024-11-07  SCORE: 45  REACTIES: 67
TITEL: My boyfriend is getting cold feet before the wedding, how can I deal with this?
POST (source_id=post):
My boyfriend (37M) and I (34F) have been together for almost 6 years, living together for 3 years. Last year around Thanksgiving he talked to me about marriage and we decided to get married by Christmas this year. This year earlier we had a few discussion about house and kids, and he seemed fine, he even arranged for his parents to come over (they live abroad) during Christmas so they could attend our marriage ceremony. However, now as the days come closer by, his parents' plane tickets bought. He suddenly shuts down and won't have any discussion at all about the wedding and won't engage in any wedding planning with me. Whenever I ask him he would simply say "you decide" or dodge the question all together with a silly laugh or a hug. Last week I was too frustrated so I asked him what his deal was, he then told me he is having terrible cold feet suddenly and he is anxious about marriage. He told me it's not about me, he is happy with me and doesn't have any problems with me, but he is afraid of his own immaturity. He said that he has never really thought about marriage before me, but he had changed his mind after we got together and thought it would be nice to start a family with me. But as the days approaching fast he gets so scared, of commitment or something else, he doesn't know. I asked him if he would like to cancel the wedding, he said it's not that he doesn't want to get married, he just needs time to get over his emotions. I asked how long and he said won't be long. I told him that's ok, since I don't want to pressure him to do something he doesn't want to do. So right now, I have put the marriage planning on hold and give him a break to think things over. But while waiting, now I'm the one feeling devasted and heart broken. All my expectation and excitement crushed , the disappointment and heartbreak and I am having crying urges everyday. It's been just a week but I am having trouble getting over these sad emotions, I feel so lost and really need some of your advice on how to proceed with him and this relationship.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lvxnwhh] (score 170, diepte 0) Did he propose? You are engaged or no?
It all sounds like you have been too easy and convenient for him. Too generoud and understanding.
He's a 37 years old, all grown man. He has been with you for 6 years and lived together for 3 years.
I don't think it's something he can get over - simply he does not want to marry you it seems.
[lvxqgpb] (score 156, diepte 0) This man is almost 40. You guys are not a super young couple in their early 20s getting married. If he is mature enough now he will never be mature enough. Did he actually propose or did you guys just start planning a wedding?
[lvxlswv] (score 87, diepte 0) he is a 37 year old man.. youve been together 6 years... if he is not ready to get married this is not going to change. If marriage is important to you, with so much love, you need to move on and find someone who wants the same things as you. as the saying goes, 'you're not asking for too much, you are simply asking the wrong person'. I hope things work out for the best for you either way
[lvxnf6e] (score 86, diepte 0) He’s 37, when will he be ready? When he’s 60? 

If you really want marriage and to start a family YOU should really reevaluate this relationship and decide whether or not waiting forever for this man is something you want to do. Take care of yourself here, not him.
[lvxo2v0] (score 62, diepte 0) I'm also a woman in my mid 30s, struggling with infertility because we waited too long. Have a really good think on if this person is ready to get married and have kids, because you don't have time to waste if not. If he doesn't want the same things then you don't have much time to start over and still have children.
[lvy0f2z] (score 42, diepte 0) My now-husband found the concept of the wedding overwhelming as we drew nearer to the date, though he couldn’t articulate why. I booked him in with a psychologist/therapist, and told him it was a non negotiable - he needed to work through whatever it was stressing him out, talking to me wasn’t working, and it was casting a dark cloud over the impending marriage. He did some weekly sessions and it helped him immensely. Maybe this is something your fiancé could look into.
[lvxtwbn] (score 40, diepte 1) As a couples therapist, I can’t stand this trope. This is awful advice.

Op, cold feet is a common experience for many people. Ask him if he is willing to go therapy or talk to someone about it. It’s hard for you to be on the receiving end of that. But that doesn’t mean he’s a lost cause or the wrong person.
[lvxrsuz] (score 21, diepte 2) Respectfully, it seems from some of your other posts that you DO want to be proposed to, and he still hasn’t. You’re giving this man way too much power of your life and your decisions.
[lvy626f] (score 20, diepte 2) I'm not a couple's therapist although in another lifetime I was studying for a doctorate in Clinical Psychology. I ending up changing course, but I still have great interest in the field.

This is not terrible advice. If at 37 years old, six years into a relationship and 3 years living together, a person is still not ready to make the commitment to marriage (and it's not a situation where all along, both parties agreed that they wanted to be together but were uninterested/rejecting the concept of a legal marriage)--something is very wrong.

Yes, he should go into therapy about this, but OP needs to consider her position here. All that time together, and this is only now just coming out? If OP wants kids, her biological clock is legitimately ticking despite all the advances in fertility treatment and despite the fact that she could very well be normally fertile. Still, assisted reproduction if a possibility for her is not a fun process as any couple that's been through it will attest to. 

But much more than that is how compatible they really are with their life goals and basic values, and how good of a marriage prospect he really is. Unless OP is genuinely happy to continue in the unmarried state--knowing her partner isn't "all in" in the way she wants to be and wants him to be. Not in the way that was her expectation.

So there's theoretically a lot to unpack here, and maybe a lot of therapy and a lot of communication and a lot of mutual introspection  will fix things. But life is only so long, and the process of coming to terms here could easily be a long one. As a therapist you surely know that therapy is not magic, that you get out of it what you put into it, and that it doesn't come with assurances for any particular outcome or that the outcome will be what you wanted it to be going in. And that all therapists come with their own set of biases, inherently, no matter how hard one tries to be impartial. These are givens of life and human nature.

So trope or no, there is this concept of cutting your losses and knowing when to move on. Because maybe it could work out, and maybe it couldn't and won't...but finding this out could take a good long while if OP doesn't set herself a deadline here. Note, I'm not saying that she should end the relationship immediately although it would be a reasonable *option*, all things considered. But my take from a lifetime of experience is that if nothing else, she needs to see  if he can sort this out in a timely manner and she needs to examine what she wants and needs out of her own life, to the extent that she has control over it. OP needs to figure out what she needs. She needs to figure out if her SO can be the person that will meet what she needs from a partner, going forward. And she'd be well advised to set *herself* a timeline in which to decide if those needs are being met, or not. And act accordingly in her own self-interest. 

Even if he could still, theoretically, be her person, there's more than one person on this planet for everybody. If he can't be the person she needs him to be now, it's possible that her limited time on this earth is best spent pursuing other prospects (including, but not limited to relationship and marriage prospects).
[lvy4a1x] (score 16, diepte 1) Exactly. I would absolutely get my eggs frozen if I were OP, and NOW.  Even that is not a guarantee. Or, if you are ready to get pregnant now, see how he feels about that? Is it just marriage that is off the table? Would he want to stay in the relationship and coparent?
[lvxrihd] (score 16, diepte 0) Are you okay with never getting legally married to him? 

He’s 37. You’ve lived together for 3 years. If he isn’t ready now, when will he be? Especially if you want children, I would ask him to go to couples counseling.
[lvydo3s] (score 15, diepte 2) >As a couples therapist, I can’t stand this trope. This is awful advice.


>Op, cold feet is a common experience for many people


And those people keep you in business later?
[lvy8s4q] (score 13, diepte 2) I dont find it to be a 'trope'. he sounds like a man child and many people arent super keen on needing couples therapy before they get married. You make money off of convincing people their problems can be solved, where im just speaking from experience that if a man is suddenly scared of commitment its prob not the right one, and hes likely not down for therapy.
[lvxm9eg] (score 13, diepte 0) Boyfriend? So you’re not engaged? How were you expecting the wedding to happen by next month without concrete plans? He is 37 years old. If he’s not ready now, when will he be? This would be a major issue for me and I would feel upset that my time was wasted for so long.
[lvy7zui] (score 13, diepte 1) Kudos to you for how you handled your situation. I'm glad to hear your now-husband was receptive and able to work through his issues, from the sounds of it.
[lvxy7xx] (score 12, diepte 2 OP) I am just so confused. I feel so lost because he is the one that proposed marriage and now he is the one getting cold feet. I have no idea what is in his head and the uncertainty is just eating at my emotions. We never had much problems, we rarely fight and we don’t cheat( at least I didn’t see any evidence of him cheating). I never seen any commitment issues with him before this.
[lvxs0kd] (score 11, diepte 0) You know your relationship best, but honestly, why wouldn’t he be ready?  You’ve been together 6 years, living together for 3.  Marriage really doesn’t change much, your everyday life will be the same.  It’s really odd he is having cold feet.  Almost like he isn’t ready to fully commit to you.  

There’s really no reason he should be having these emotions if you have a stable relationship.  I’m sorry, OP.
[lvyobzi] (score 9, diepte 2) > Op, cold feet is a common experience for many people.

Also, when I think about it--so-called "cold feet" such as OP's partner is displaying isn't really all that common, at least not in relationships that are going to become happy marriages. What's common and normal is being nervous or anxious about the wedding itself and having wedding related worries. But the key difference is that these anxieties are related to the actual wedding. Not to the concept of marriage itself or being married to your fiancé, or to married life. But the two get confused. 

Maybe OP's partner really does just need a chance to work through some fears about how being married will affect their relationship, in order to be ready to make that commitment. It's impossible for us to know. But they're on short time until the planned wedding. It's supposed to happen in a matter of weeks. And from other comments, apparently this unrest about marriage isn't new. 

Sounds like there needs to be a postponement at any rate.
[lvxy5x8] (score 9, diepte 3) Sounds like he did propose. He proposed the idea of starting to plan a wedding and they discussed and agreed. Not an elaborate proposal, but sounds like he’s the one who started the convo.
[lw2inu1] (score 8, diepte 1) The fact that she referred to him as boyfriend rather than fiancé makes me think there was no proposal
[lvxzoyh] (score 8, diepte 0) Not that there hasn’t been any guy who bought an engagement ring and still backed out or got cold feet… buuut I think for some, the EXERCISE of getting the ring can sometimes serve as an opportunity for them to reflect and consider why exactly they think they want to marry someone. This avoids this kind of situation because they’ve already processed those emotions (hopefully).

With that said, personally I wouldn’t continue down this path with him. Take a step back, stop all planning and decide for yourself what it means that he’s not ready to get married after the years you’ve spent together. 6 years is really a good enough time to get to know someone so if he’s still unsure at this point, well, that might not be good news.

Keep your head up, you got this.
[lvxzpp3] (score 7, diepte 2) tysm for not instantly jumping to breaking up like everyone else in these comments 🫠 reddits favorite thing to do is tell people to break up w their partner
[lvyfpyl] (score 7, diepte 1) I totally agree with this. Nothing will really change in terms of processing and avoidance if he doesn’t address his concerns. He’s just spinning. I’d need a solid plan that included therapy to better understand what the issue is and how to move forward, even if it’s coming to the conclusion your dreams are incompatible.
[lvxs8rw] (score 6, diepte 0) Sounds like y'all need a conversation about "marriage". What he expects, what you expect, etc.

Perhaps he's just having one of those, "oh fuck, I'm the adult and I'm getting married that can't be, I'm still 27, 17, I'm a teenage groom". 🤣🤣🤣

>he just needs time to get over his emotions.

He seems to be openly communicating. He's not looking to cancel the wedding. He's just having all kinds of normal feelings leading up a big life change. 

>It's been just a week

Breathe. It's been a week. If your wedding is planned for this December, there shouldn't be much to be planned at this stage. Give it the weekend, go on a date, and have fun with each other, no wedding discussion.
[lvys9mw] (score 6, diepte 1) Mine was anxious about the wedding because he didn't want to show deep emotion (love for me, joy of us getting married, grief his parent was not alive to witness it) in front of many people. But it's not the same, he didn't have cold feet, mentioned nothing of commitment. That would've made me so sad and scared. But for him too therapy helped, and I don't think for this fiancé the problem will magically resolve itself on its own. I wouldn't wait and give him space anymore without knowing his plan/steps because it sounds like he doesn't have any
[lvyghgl] (score 6, diepte 0) "I asked him if he would like to cancel the wedding, he said it's not that he doesn't want to get married, he just needs time to **get over his emotions**. "

Is that how he phrased it? Because you don't... get over your emotions. You process them. You don't ignore them. 

If that's how he phrased it, I'd honestly put an end to this uncertainty bull shit, take some control back, and just break up with him. You don't want to be with someone who isn't fuck yea about marrying you. Some conflicting feels are normal, but like... you don't **get over** your feelings.

You don't mention kids - the commenters do - but if you want kids, he is actively harming your window of motherhood by dicking around and not being mature enough to process and be aware of his emotions.
[lvyvage] (score 5, diepte 5) So my sense is that you have two options here. Option 1, the option you seem likely to take, is to push on despite this and wait for that societal pressure to kick in that will make him marry you. Not because he really wants to, but so as not to lose face and have his parents who are coming from abroad (?) berate him if he backs out. In short, he feels like the wedding is an obligation for him now. Do you want to marry somebody that's marrying you out of a sense of obligation, and his fear of social disgrace being even stronger than his fear of marriage?

Your other option is to stop trying to figure out what's going on with him, and start figuring out what's going on with you. Are you satisfied with the status quo? Are you accepting of a marriage that's fear-based and not love and commitment based? I'm not saying he doesn't have real feelings for you, but he has other things going on too. You can't fix that, though. You have to make some choices about what you will and won't accept. Rather than face up to his uncertainties and fears and work through them, or at least start working through them, he's avoiding them and dumping them squarely on you. Are you going to accept the emotional dump and live with it, or are you going to do a "me-focused" approach and tell him that the wedding is postponed indefinitely until he gets some help. And if you want him to get help, then you're best to separate from him physically and live apart until you two figure this out. If you still live together and neither of you makes a change, things will continue as they are. He gets to have his cake and eat it too. You get to feel miserable.
[lvye4t4] (score 5, diepte 0) At 34 years old I would not give him the luxury of being confused after six years and three living together.  I'd move out temporarily and let him figure things out on his own. If he thinks counseling will help him he can decide. Depending on how long that takes I would make him no promises I'd still be around.
[lvxq045] (score 4, diepte 1 OP) We are Asians, so we don’t really go through the stage of getting engaged before wedding. He proposed the idea, and we discussed things through, and our parents know and give us blessings. Wedding is planned for this Christmas.
[lvyqno3] (score 4, diepte 3) You're six weeks out from the wedding and he's shut down on you and doesn't want to communicate beyond saying he's anxious about marriage.

He may well go through with the marriage due to social pressure, but he's probably not going to get past these feelings without some kind of active intervention. Not just waiting for it to go away. Meanwhile you're feeling in limbo and miserable. 

If he loves you and wants to be with you, he doesn't get to shut down on you and avoid. On the one hand, this is not something you can force him to push past. On the other, he's being deeply unfair to you. Have you told him just how much his recent attitude and behavior is affecting you? And that you need him to see a therapist and confront his fears before you can feel confident about marrying him?
[lw0xjme] (score 3, diepte 1) It's not an age thing. If he's not ready to marry her, he will never be.
[lw04za6] (score 3, diepte 1) He wants to leave the door open, yep.
[lvxwcnr] (score 3, diepte 0) Aww, this is horrible.  But don't give him all the power here.  You're in "wait and see" mode, and I can't even fathom the stress this is causing.  

Take your power back, meaning don't let him unilaterally decide whether or not you get married in a couple months.  

Tbh, this doesn't sound promising long term, but if you truly love this guy, what would happen if you told him you're postponing the wedding?  It's tough and not the norm, but it's certainly not unheard of.  This gives you time to process all this, decide if it's worth working on, and then getting couples counseling.  Also, it's a bit easier to say postpone rather than cancel.  Cancel implies full break up, and you may not be ready for that.
[lvxxhyl] (score 3, diepte 0) Is he willing to go to couples therapy with you? Have you known from the start of the relationship that he never considered marriage?
(36 reacties met lagere score weggelaten)

