# Label-batch batch_0022

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
Schrijf het resultaat naar `batch_0022.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 31yomv, rsy855, js4l1b, 72pnt3).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 31yomv ===
SUBREDDIT: r/goodyearwelt
DATUM: 2015-04-09  SCORE: 6  REACTIES: 50
TITEL: Most Comfortable Boots? (For High Arches)
POST (source_id=post):
So I've had a pair of Iron Rangers for a while now (Worn, probably, 45-55 times). If they aren't broken in, I'd be impressed. In any case, I LOVE the look of them. However, they are NOT comfortable. I've tried several different insoles, to no avail.

My most comfortable shoes are some NB574s, and some Timberland Earthkeepers Rugged 6" Boots. Are there any equally bulky/chunky boots (comparing to Red Wing's Iron Rangers and Beckmans) that are even half as comfortable as my NB574s or Timberlands?

P.S. I have broken in two different pairs of Iron Rangers (One in my correct [Yes, correct] size of 11D, and one in 11.5D in order to fit insoles), so I really don't think they're for me.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cq6gd78] (score 10, diepte 0) White's.  All day long...White's.

Nothing compares for arch support.  Really.
[cq6iiur] (score 5, diepte 3) It's a real bummer because we're so picky and notice everything, but also Nick's does toe caps better. 

I'm mulling over the shell Dundalk's now, but I'm not sure I want to suggest to my wife I'll be buying nearly $1,000 boots.
[cq68pxp] (score 3, diepte 0) White's and Nick's are supposed to have a fairly prominent arch, and most people find them to be very comfortable, after they're broken in.  I don't own a pair, so I can't share any personal experiences.

I have similar comfort issues with Red Wings.  The only pair that I can comfortably wear all day are my 6" round toe roughout boots.
[cq6aq9u] (score 3, diepte 0) Have you tried the heat moldable insoles from Soul? Red Wings has a branded version they sell in their stores. Its what I use for my high arches, and it's great. Pricey, But when you work on your feet its worth it.
[cq6au1s] (score 3, diepte 1 OP) How much do they cost?
[cq6hn4p] (score 3, diepte 2) They do, but I don't believe the Hathorn have as significant of arch support, as that's their "budget boot" and is a world of difference from their regular line.  I'd recommend the Semi Dress or Bounty Hunter (taller semi dress with an additional piece of leather on the heelstay).

[Here's](http://www.reddit.com/r/goodyearwelt/comments/2bz0yv/a_guide_to_ordering_custom_whites_or_nicks_boots/) a guide that I put together (I am in no way affiliated with the company, just a big fan of what they do).  I also mention Nick's in there, but given some of the problems people had in the GMTO, I think I'd recommend White's over Nick's.
[cq6k1v8] (score 3, diepte 4) I agree...to an extent.  We (as a community) can certainly be overly picky sometimes and Nick's definitely does better toe caps, but some of Nick's' recent mistakes were ridiculous and unacceptable, imho.  Seriously lopsided heels and compressed paper instead of leather in a heel stack?!  That's insane.  I'd happily buy Nick's through Vermilyea Pelle any day, but aside from that, I'm not sure I would (or will) go there.
[cq7qfn1] (score 3, diepte 6) I have Nicks Cap toes that I really like. I'll try to post a review this weekend to the sub.
[cq69o6z] (score 2, diepte 0) Don't know if Alden Indys count as bulky/chunky boots, but their trublance last is very comfortable.
[cq6b9zd] (score 2, diepte 0) Like others have arch support is prominent in whites and nicks. Quick question you sure it's not width thing on the IR the last is somewhat narrow?
[cq6gkdd] (score 2, diepte 1 OP) Are they the ones who do Hathorn? 

Found this: https://www.bakershoe.com/product/hathorn-traveler-whites-boots?gclid=Cj0KEQjwxpipBRCap8PR2Om7vq4BEiQA6V7OVQFd0eM5IB1voc6fa9Hf1fXI7drd29FXNv1rHvcG0H0aAjT18P8HAQ
[cq6p751] (score 2, diepte 5) It's just so weird that they went that route though, given their business model. And to do it for/to us — the ones who will notice — is pretty asinine. 

The ironic thing is that people have been crying foul about White's for awhile now because they got bought out and their quality has to suffer because *when new money gets involved costs must be cut* or something.

And yet nothing has changed there, while Nick's has been doing god knows what.

It has definitely soured me on their upcoming service last. A pretty but unstable boot isn't worth getting.

I'm undecided on Dustin's new last. It doesn't look right to me so far, but maybe the finishing will pull it together. Plus, I'm not sure he has any leathers that fill any holes in my rotation. Waxed flesh and rambler are awesome, but not terribly different from my Katahdins.
[cq7fad2] (score 2, diepte 7) It doesn't look like it, but maybe it's modeled after it?

You can see the last [here](https://instagram.com/p/0d6Uc1Sdnl/).

A mostly finished boot can be seen [here](https://instagram.com/p/08x7N7Sdlh/).
[cq7z7bt] (score 2, diepte 11) Could be. It just worries me because there's a lot that goes into a pattern.
[cq7p9n0] (score 2, diepte 3) I may be wrong (it happens all the time), but might an orthopaedic last just mean that there is room for orthopaedic inserts?  Given everyone's feet are different, I would have to assume that Alden is not issueing a one-size-fits-all orthopaedic boot.

I don't really feel any arch support in my Indys.  It's a pretty flat footbed, if I recall correctly.
[cqbaanm] (score 2, diepte 4) This is right.  There is room to fit inserts.  There is almost no arch support natively.
[cq7u7zv] (score 2, diepte 2) I had that exact problem with Red Wings. I was literally about to come post something here about finding a different boot and I ran into this thread. Red Wings look great but they were painful to wear.
[cq84c2c] (score 2, diepte 3 OP) It's a fucking shame. I even tried a half size up to use some Superfeet blacks, and it made my feet so high in the shoe that the leather cut my foot where it bends.
[cq68xqd] (score 1, diepte 1 OP) Yeah, I've tried their moc toes on before and they seemed more comfortable. Guessing that sole is significantly better than the Iron Ranger's sole.
[cq69pxd] (score 1, diepte 1 OP) Yeah, not really chunky enough. I've never liked the look of the Indys. Their plain toes don't look too bad, but not quite as bulky as I like.
[cq6igjo] (score 1, diepte 2) I think super feet makes some too, for $30-$40.
[cq6bb44] (score 1, diepte 1 OP) Yeah, it doesn't feel tight at all. It just hurts to stand or walk for too long in them.
[cq79ql5] (score 1, diepte 6) Agreed all around.  Spot on.

I'm sure Dustin's last will end up looking great, as I have nothing but confidence in him.  That said, if it's the Dayton Service Boot last (I haven't been keeping up on this as much as I should), I'm not sure I'm very interested, as that last just didn't love my foot.
[cq7ox9b] (score 1, diepte 8) Interesting.  Looks really damn slim (narrow?) to me, and I'm generally a fan of a bit of a chunkier boot...but my expertise for judging a boot when still on it's last is severely lacking, so I'll have to reserve judgement until I can see a finished product.  Exciting either way, and I really appreciate your posting these links.
[cq7porl] (score 1, diepte 9) Sort of resembles the 1000 Mile boot in silhouette to me. It may be the angle and distortion, but the proportions feel off to me. The rear counter is tiny and the front of the boot/vamp looks oversized.

He's mentioned he has no training or books. I don't think it would have been a bad idea to pick up the standard pattern making book that everyone uses. It's a classic. It also gives a smooth, polished finish product that doesn't come from *winging it*.
[cq7qbqg] (score 1, diepte 10) Agreed on the W1K thing.  

You may be right about the downsides of winging it, yet somehow I think he'll pull it off.  I may be a bit of a VP fanboi, but somehow seems to be a bit of a genius to me.  Time will tell.
[cqa0sgz] (score 1, diepte 5) The compressed paper heel issue seems really odd to me. When I saw the post about it coming up, I called Nick's since my boots were in production and asked them if they would be using compressed paper in the heel of mine. The response was kind of a bemused "of course not." Is it possible that they used compressed paper in that one instance because they knew Dustin at VP would be refinishing the heel on that example or are there other cases?
[cqa7ih3] (score 1, diepte 6) I had that thought as well...but I just don't know.  I would ask, but I certainly don't want to create any tension between the two companies, as I like and respect both, and find their collaboration to produce some amazing boots.  

I'm just hoping it was a one time thing.
[cq6wa4i] (score 1, diepte 3 OP) Are there any available that look more like that Hathorn option though? Most of the one's on the site seem to have that cuban heel-esque look. (I know they're not cuban heels, but they resemble them a little)
[cq6y2un] (score 1, diepte 4) Yep.  Just ask for a block heel.  I don't like the cuban heel at all (and I would say that what you're seeing is, indeed, a cuban heel), so I've gotten a block heel on all 3 of my White's.  White's are generally built custom (aside from a few stock options), so you can get either a block heel or a cuban heel.
[cq72dne] (score 1, diepte 5 OP) What's the closest boot to, say, Red Wing's Iron Ranger or Beckman, and cheapest of Nick's or White's? (I love the cap toe of the IRs, but will likely want a mini lug sole like the Beckmans.)
[cq79ju3] (score 1, diepte 6) If you want a cap toe, go for Nick's.  White's' cap toes have been a bit wonky from time to time.

If you go plain toe and want a shorter boot like the Beckman, White's Semi Dress is your best bet.
[cq7399l] (score 1, diepte 3) what is GMTO? I was about to pull the trigger on some boots from Nicks before I saw this thread. Where do you get this info from?
[cq79ooe] (score 1, diepte 4) GMTO = Group Made To Order

GYW had a GMTO back in October, and because a lot of those boots were made with Chromepak (which took a while for Nick's to get), a lot of those boots have been trickling in over the past couple months.  Too many of those boots have had issues for me to be able to wholeheartedly recommend them like I used to.  They may prove themselves again, but I (and seemingly a lot of the GYW community) have been disappointed by some of the boots that they've delivered recently.

I'm getting this information from this sub and from styleforum, however styleforum has been pretty silent about Nick's.  I also own 2 pairs of Nick's, myself, but both of those were bought through Vermilyea Pelle, who acts as both the liason and quality controller for Nick's when things go wrong.  He also does the heels for the boots ordered through him.
[cq7t9bd] (score 1, diepte 5) Thanks! I guess it's time to start looking at White's.
[cq7r4hm] (score 1, diepte 4) I got my Nicks from the GMTO, and love them. I'm going to post up a review over the weekend
[cq6qj9h] (score 1, diepte 0) Alden Indy boots are technically orthopaedic shoes and provides excellent arch support in addition to being just plain super comfortable.
[cq79rq5] (score 1, diepte 1) While I like my Indys and find them quite comfortable, I don't really feel the arch support you're mentioning.
[cq7dfoo] (score 1, diepte 2) I find that weird, but Alden's Tru-balance last is one of their orthopaedic lasts and do in fact provide better arch support than other shoes. I don't have arch problems, so I can't really compare.
[lrrpn9x] (score 1, diepte 1) Hmm. I don't like the look, prefer plain toe, but that may make me try a pair.
[cq6x439] (score 1, diepte 0) Another idea...  I don't know how you feel about handsewn (moccasin construction) footwear, in general, but they are extremely comfortable.  With the right combination, they can be kind of rugged/chunky, too.

* [**Quoddy Grizzly**](http://imgur.com/a/eadDf)

* [**Quoddy Perry**](http://imgur.com/a/DKQ59)

* [**Rancourt Boots**](http://www.reddit.com/r/goodyearwelt/comments/2m2i3t/rancourt_mudguard_boots_from_brooks_brothers_sale/)
[cq71gm8] (score 1, diepte 1 OP) I actually just tried a pair of the Eastland Made in Maine (Rancourt) Monroes (Blake Boot), and they are NARROW as fuck. Not horribly uncomfortable, but too narrow for me; and it seems even the Rancourt custom mades don't come in a slightly wider width.

And those Quoddys look nice, but I really want something plain toe right now.
[cq79slt] (score 1, diepte 1) They're comfy, but they don't offer much in the way of arch support.
[cq7iml0] (score 1, diepte 0) Dude so much this. 

My White's semi dress are rotting away in my closet but they are absolutely killer in terms of arch support and comfort. I just don't like the way they look on foot - love my iron Rangers... but they're definitely a lower quality boot and leave a lot to be desired in terms of support/comfort. 

I'm taking a pretty long (~1 month) overseas trip this summer and I'm already pretty sure I'm going to have to suffer through iron Rangers as a daily driver ಠ_ಠ
[cq7p1o3] (score 1, diepte 1 OP) Yeah, I'm considering parting with them just because they hurt so much.
[cq89z6h] (score 1, diepte 4) I ended up just returning it within the 30 day period. For that price, I can't justify something that is so painful to wear.
[cq8apax] (score 1, diepte 5 OP) Have you found any alternatives you like? I know I tried the Chippewa Apaches before, and they were comfortable, but didn't have that chunky aesthetic the Red Wings have.
[cq8n72h] (score 1, diepte 6) I have some dress boots that I like, but nothing in this "rugged" style. I am going to order my own custom Bounty Hunters on Monday. I will let you know what they're like once they come in!
[cqanie4] (score 1, diepte 0) I've been wearing a pair of White's SD for the past 5 weeks, finally breaking in.  I typically wear a substantial orthotic for supination.  I went with these boots to attempt to eliminate them.  So far so good.  Been on my feet 10-16 hours a day on vacation, and while my foot pads get tired and sore, my ankles and calves are loving the support and alignment.
[cqcjhxw] (score 1, diepte 0) There are small glueable inserts i've seen in random shops here and there. Why did you size up on the iron rangers length instead of the width to fit an insole though?
[cqcm0f7] (score 1, diepte 1 OP) I'm not sure. I just thought that was the best course.

=== THREAD rsy855 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2021-12-31  SCORE: 5  REACTIES: 49
TITEL: What's one shoe that everyone else seems to love/ rave about that you just didn't like/ get on with?
POST (source_id=post):
I thought given everyone has different feet and gait cycles (and weight also plays a factor) meaning a pair of shoes someone loves can be hated by another person it might be interesting to hear which shoes people really didn't get on with but are generally loved by the running shoe geeks community. 

For me, (female, 120lbs, midfoot strike, easy pace 8-8:30 min/mile, tempo pace 7 min/mile, threshold pace 6:30min/ mile) this year, I have not gotten along with the puma velocity nitro due to just not being able to get a good heel lock despite going a half size down. The Nike Invincibles also dont work for me. For some reason, despite never having knee pain in my life from running or any other running shoes the Nike Invincibles cause me to get knee pain after a few miles. Oh and I also wasn't blown away by the endorphin speeds. They are ok but I have really narrow feet and they do fit my feet too well. I also chose to wear other shoes over them when I'm doing tempo/ threshold runs. I also sent back the Clifton 7s as the heel lock was awful and they made my legs feel like lead. Absolutely no energy return and the foam didn't even feel soft to me. 

My favourite shoes this year:
- Nike Alphafly
- Puma Liberate Nitro
- NB Rebel V2
- ASICS Novablast 2

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hqpawvl] (score 15, diepte 0) Rebel 2, too unstable and squishy as I supinate so much and I never take it past 10 miles as my legs start to hurt. Gonna take it 500km then call it a day.
[hqpdg7r] (score 9, diepte 0) New Balance 1080v10. Distinct lack of energy return for me compared to the Infinity Run. Lacing is a hit and miss and the shoe is forever present on my feet througout the run.
[hqpfmt8] (score 8, diepte 0) Novablast 2 is the most overrated shoe on here in my experience. Clunky, heavy, and don’t serve a good purpose in a shoe rotation IMO.
[hqpd8yq] (score 7, diepte 0) Kinvara. I couldn’t even force myself to like them when I snagged a good deal at $35 and I love a good deal.
[hqphndf] (score 4, diepte 1) Id also agree too squishy. No plate with it just feels like im going through the foam and hitting the road, and I dont have a problem with more minimal shoes either. Just weird shoe idk.
[hqpgawe] (score 4, diepte 0) Alphafly’s, too narrow to my liking and not as amazing for a runner as people make it out to be. I get the same response for long distance with my novablast 2.
[hqprzy8] (score 4, diepte 0) Hoka Mach 4 - super light but zero ‘bounce’ or energy return for me. Just very dull. 

Puma Velocity Nitro - nice fit and superb value but again, no bounce and insufficient cushion under the big toe joint caused me some discomfort. 

ASICS Novablast 2 - amazing design/colourway but wouldn’t describe them as having good energy return. I felt like I was sinking into quicksand and it wasn’t really what I was looking for. 

Having tried and returned/sold all the above I just kept my original shoes…

Reebok Floatride Energy 3 (daily), Adidas Solarboost 19 (long/easy runs), ASICS Evoride 2 (tempo/daily) and Adidas Adios 6 (5k race shoe). Most of my collection gets a lot of hate on here but then I didn’t really get on with the shoes that get all the hype so it just goes to show everyone is different. Go with what works for you - that’s all that matters.
[hqpcuot] (score 3, diepte 1 OP) Kudos for still taking it to 500km! Sorry it hasn't worked for you though. Always annoying to buy a shoe and it not work.
[hqppygy] (score 3, diepte 1) It was the first shoe I loved enough to buy a second pair lol. This was mostly due to the fact that it was the first shoe i didn't have to adjust to, it just fit me like I want a shoe to fit - without all the humps on the insole or extra random padding. Different strokes for different folks!
[hqpdrcf] (score 3, diepte 0) Hoka Mach 4. Very light on the feet but too squishy for running. However, they've become my go to shoe for miles of walking around town. Also, Nike Tempo Next% are great for speed days on dry pavement and when it was warm. But they suck now that's it's colder and wet or icy pavement is more common. Living in Michigan, I wish I owned a pair of Endorphin Speed Runshields right now for the speed work days.
[hqphmn3] (score 3, diepte 0) Saucony Triumph 18 - that heel slipping was something huge for me. We went separate ways 💔
[hqqaehp] (score 3, diepte 1) I completely agree with every shoe you listed and the reasons behind them.  I tried each and every one and all had/have at least 30 miles on them.  I think the biggest disappointment was the novablast.  It’s just weird because I like the nimbus lite a lot, I’m chalking it up to the geometry.
[hqpz0ga] (score 3, diepte 0) Clifton 8: I don't know whose 12W foot they are made for, but it's not mine. It's not like i have flat feet or anything, so I can only wonder why Hoka decided to use what i can only assume are stegosaurus spinal plates in the construction of the arches. How such a big, cartoony shoe is still too small is beyond me.  Now, I solely wear them at work, and the only reason i do that is because I'd feel like a sucker if I didn't use them for something.
[hqqa3bn] (score 3, diepte 0) Mach 4 and the Novablast 2. 

Both are and arguably continue to get so hyped up but I found the Mach 4 to be such a dull ride.  

The novablast 2 was a shoe that I’m super disappointed about, I put 70 miles on the shoe hoping something would change but it’s all the squish of the invincible without any of the pop.  The geometry just does not work for me.
[hqqdxxa] (score 3, diepte 0) More V3. Heavy, very controlling on footstrike, rocker is very aggressive despite being a heavy shoe which doesn't feel great at all. I also don't really like the foam tbh, I prefer lightstrike / pwrrun pb
[hqpdcu8] (score 2, diepte 1 OP) Ooft they must be bad! I've always been tempted to try them too 😂
[hqpe40o] (score 2, diepte 2) They’re very firm, have these interesting protruding cushions at the heel that feel super weird, and the lockdown was bad for me despite trying different tying methods. But I see people rave about em and their great durability that’s why I tried it out.
[hqpo153] (score 2, diepte 4) https://www.reddit.com/r/RunningShoeGeeks/comments/npytyh/kinvara_11_after_710km_52_runs/h085lro/?utm_source=share&utm_medium=ios_app&utm_name=iossmf&context=3

https://www.reddit.com/r/RunningShoeGeeks/comments/rritlj/kinvara_12_328_miles/hqgrujg/?utm_source=share&utm_medium=ios_app&utm_name=iossmf&context=3
[hqphcw3] (score 2, diepte 1 OP) Yeh the endorphin speed runshields are appealing but I heard the outsole isn't really any better than the nonshield version (also I didn't like the speeds that much anyway). It is annoying have a lot of race/ speed shoes have traction that's no good in inclement weather.
[hqpeqg7] (score 2, diepte 0) Interesting i have the inverse opinion on liberate nitro so far vs speeds compared to OP.
[hqpgkni] (score 2, diepte 1 OP) It's always interesting! My feet tend to prefer more flexible shoes so I think that could be why. Also may be to do with being lightweight but I'm not too sure about that.
[hqpgz3o] (score 2, diepte 1 OP) That's fair, I have narrow feet so I don't have an issue with the snug midfoot. I agree that you can run similar speeds in the Novablast 2 as the Alphafly I just find the Alphafly makes those speeds feel more effortless in that my HR will be lower for the same paces. Glad the Novablast works for you so well. In fairness I do all my long runs (up to 24 miles) in Novablast 2 but race in Alphafly.
[hqpjis3] (score 2, diepte 2) Would you recommend doing half marathons and marathons in novablast 2? Right now my rotation is endorphin speed 2, pro 2, and novablast 2. This is going to be my first marathon! (10 weeks from today)
[hqpjr0t] (score 2, diepte 3 OP) Yeh absolutely! I have run 24 mile runs in the Novablast with no issues at all. For a first one too it's more important to be comfortable. When you are trying to fit PRs then maybe think about running in a speedier shoe.
[hqphtzw] (score 2, diepte 1 OP) Heel slip is the bane of my life I swear! So many shoes I want to love but just can't get a good heel lockdown. The woes of having narrow feet.
[hqpql55] (score 2, diepte 0) Skechers Razor 3/3+. So much hype around them and they just feel so dull and firm. I wanted to like them, but was continuously underwhelmed.
[hqpv07u] (score 2, diepte 0) ASICS glide ride and Nike infinity react. The glide ride felt super weird to run in for me, but could be due to my mechanics/footstrike but I never quite got that “gliding” benefits people talk about. 

As for the infinity react, the cushioning just felt dead to me and I never felt the energy return. Now I just use them for walking around.
[hqq5a0h] (score 2, diepte 0) Probably my endorphin speeds. When I first got them I could see why they’re so hyped, they felt bouncy and really pushed me to go faster. Now I’ve found them to be really inconsistent. They lost that initial energetic feeling within the first 30ish miles and during some runs they don’t feel any more energetic than my ghosts, and sometimes when I lace them up one of them will feel like they’re digging into my deltoid ligament like crazy and just loosening the laces isn’t enough so I have to completely unlace them and redo the knot to get them to feel better. However, on other days I lace them up and they feel close to what those initial few runs felt like where everything feels wonderful. For the life of me I can’t figure out what makes the difference during those runs even though I’ve got 135 miles on them. They’re not bad enough that I’m going to stop using them when they’ve still got plenty of life left in them, it’s just disappointing that I can’t reliably trust them to be a true speed day shoe.
[hqr7f1e] (score 2, diepte 1) Funny thing about the Mach 4's. Took months before they became available in my size locally when they first came out. Hyped to get them, but by the time they were stocked, I had read so many reports like yours (dull, firm and unremarkable), that I gave them a pass. Enjoy Hoka trail shoes, but their road shoes aren't compelling given how quickly they pack out (among other shortcomings).

Found the Triumph 19 on sale, despite looking for a deal on the Nova 2. Still curious about the Novas, though..
[hqqbsd8] (score 2, diepte 0) Pegasus Turbo 2's. 

Never noticed too much difference from my run-of-the-mill Pegasus 37s.
[hqrcg2p] (score 2, diepte 0) Endorphin Speed 2. Would get terrible calf pain after 3 miles or so. Never had it in any other shoe. Also never had "wow" feeling to me like the Atreyu Artist or Puma Deviate Nitro does. Maybe I'm just too heavy or supinate too much for it, who knows. Beautiful shoes though, wish I could have loved them
[hqsjeby] (score 2, diepte 1) I had this when I first ran in them but once I wore them in a bit I had no more issues. They felt so weird to run in at first because they are a neutral shoe and I felt propelled forward. I did have to work on my form a lot. It’s a shame you didn’t get on with them because they are great shoes.
[hqphsv5] (score 1, diepte 3) I just did a run in Kinvaras. Have done 400s workout in them as well. I was told by many people that they are NOT durable. How can a shoe with no rubber on the bottom be durable? Its just foam.
[hqqu4q7] (score 1, diepte 2) Same. Got two extra new pairs in the closet ready to go.
[hqpdlro] (score 1, diepte 1 OP) Oh I forgot about that shoe. I didn't buy it but I tried it on in the shop and the heel collar just did not work for the shape of my ankle so it was a no go for me.
[hqrdz0r] (score 1, diepte 1) Mine got really hard quickly, they feel slow now. I’ve moved them off rotation to casual walking.
[hqphv2c] (score 1, diepte 2) The biggest advantage to the Runshield version is that they’re much warmer for colder weather. Nike Tempo Next% have Old Man Winter sucking on one’s toes. I agree that it would be nice to speed shoe with great traction. Unfortunately that adds weight which doesn’t help sell speed shoes.
[hqpi96j] (score 1, diepte 3 OP) Yeh definitely, I understand why they don't do it but it would be nice if they did. I actually wear my puma liberate nitros for that purpose as they do actually have insanely good grip and drain well if they get wet.
[hqrjyeu] (score 1, diepte 3) See if you can still find the RC Elite v1 if you want a fast shoe with great traction. I plan to get a lot of use out of it this winter.
[hqpra0t] (score 1, diepte 2) I'm honestly still getting a feel for them (the liberates nitro) I've done a track workout and a tempo run in it.  Thinking about taking it out on a shakeout tomorrow to get more familiar.
[hqq7lwx] (score 1, diepte 1) Agree. The fit is super odd. It is like way too long. Then if you go half size down it feels odd. Walking around in it feels like a cheap shoe.
[hqpip8j] (score 1, diepte 2) To be honest the lockdown was good but I felt that the area where the heel sits was too low, so my heels were always slliping out of it. The heel collar fabric was silky, tried different socks but didn't help. Might be just the combo of my heel and the shoes as many love the shoes.
[hqpxa0s] (score 1, diepte 0) The Invincible for me. Too squishy, too soft. Stability is fine but can't find much use for it besides recovery runs.
[hqq2ti9] (score 1, diepte 0) Either Novablast 2s (clunky, firm, painful at times) or Speed 2s (firm, unforgiving, bland).
[hqq6rqi] (score 1, diepte 0) Invincible
[hqqc3dc] (score 1, diepte 0) Nike Alphaflys and Vaporflys. Didn’t fit my feet well at all.
[hqre814] (score 1, diepte 0) Liberate Nitro and Rebel v2. Way too flexible and put a lot of load on my feet and calves. Developed a bit of pain in the achilles tendon as a result. I've also found that I need to focus a lot on form when running or it'll just fall apart.
[hqrja0h] (score 1, diepte 0) I didn’t care for the Peg Turbos. They were just okay. A decent daily trainer, but nothing amazing. And I hated the upper (on the 2).

Moved away from Nike and feel no need to go back.
[hqsle3l] (score 1, diepte 0) Asics gel cumulus 22, bulky, clunky and despite it being light I find it heavy

=== THREAD js4l1b ===
SUBREDDIT: r/goodyearwelt
DATUM: 2020-11-11  SCORE: 117  REACTIES: 48
TITEL: [First Impression/1 Month Review] White's MP by Baker Shoe on Black Shell Cordovan
POST (source_id=post):
**Pictures - just a few since I suck at taking photo**

[**https://imgur.com/a/DOQnwJh**](https://imgur.com/a/DOQnwJh)

**Specification**

>\- Model: MP  
>  
>\- Last: Semi-Dress (55) (Wanted Barrie but they don't do Barrie for size 5.5)  
>  
>\- Size: 5.5D  
>  
>\- Leather: Black Shell Cordovan  
>  
>\- Leather Liner: Canyon/Red  
>  
>\- Pull Loops: No Thanks  
>  
>\- Toe Cap: Medallion Dress  
>  
>\- Hardware: Antique Eyes & ~~Hooks~~  
>  
>\- Mid-sole : Double  
>  
>\- Edge: Brown  
>  
>\- Heel Base: Standard  
>  
>\- Heel Lifts: 1/4" Higher  
>  
>\- Sole: Vibram 269  
>  
>\- Sole Trim: Close Trim  
>  
>\- Embossing: ~~No thanks~~

**Introduction**

This is my first review in GYW, please be kind to me.

Up until now, like other users in GYW, I have been only looking at the subreddit and occasionally buy few pairs but never posted a review. The boots that I still use are Sagara Regent and Red Wing 9185.

Okay, why White's with Black Shell Cordovan?

To be honest, I don't know, it might be an impulse buying.

I was only looking for a good black service boots while I stumbled upon White's MP. I did look at several manufacturers such as Thursday, Truman, Grant Stone, Viberg, John Lofgren and many more. From cheap to expensive.

I didn't plan to spend USD1000+ for this. I had a budget of around USD400-500. Which was quite right for a decent constructed boots.

However, when I saw White's MP, I just knew that this is the one for me. Another reason would be because they can take my measurements and then fit the shoes to my feet. Truman boots were my 2nd choice but I was not sure of the sizing and a mixed review of QC led me to White's.

I live in Japan. Here, White's boots are twice more expensive than their retail price due to import tax. The black CXL of White's MP costs around 100k Japanese Yen which is around USD1000. OMFG.

Then, I started to re-plan my financial budget and start saving some $$. After some time I discovered about Baker Shoe on this subreddit that Kyle from Baker makes a very good fit of White's Boots. Checked the website and voila, Shell Cordovan with the same price as CXL in Japan, they have international shipping to Japan as well.

Had a dilemma in choosing a black CXL and Shell, but I chose Shell just because I never owned one and getting away from CXL crease might be nice. Boom! Emailed and Paid! How stupid of me!

I completely forgot that I need to pay the import tax as well which was not included in the invoice.

I was prepared to face my own foolishness but lucky me, Baker Shoe marked down the price so that I didn't have to pay the import tax.

Enough essays and let's get down to the review.

&#x200B;

**First Impression - from order to delivery to first try**

Emailing with Baker was great until I made the payment. Great service, detailed, fast.

When I made the payment, it was all slow and usually a reply with one sentence and few words.

A bit of a let down honestly, because I am used to customer service in Japan.

Payment made around April and COVID-19 hit us like a meteor, EMS got stopped and FedEx/DHL were to expensive to send 2 A4 papers. I used normal mail by Sea but they said it has been delayed as well and it might take 2 months to reach US.

Come July, no news from Baker and I sent another tracing using Kuroneko Yamato which costs a lot more but not more expensive than FedEx/DHL.

They got it within a week, and with recent US situation and lots of order, my boots were finished and sent to me around end of September. Yes, 2 months from tracing, 5 months from payment.

Got the package in your usual White's box and I already noticed 3 things wrong with this.

1. No hooks even though I ordered with hooks
2. Edge trim looks more Natural than Brown, was expecting a little darker.
3. No SHOE LACES!

Shoe laces are around 10 bucks, not a big deal, I can order one locally but I decided to asked them to ship a pair because I paid for it.

A bit disappoinment. I didn't expect these to happen in a pair that I paid more than USD1000.

Oh well, sending it back and forth would take time and it's not like I paid extra money for the hooks and edge trim either. I chose to go with it and maybe change it later when I need to resole/reconstruct.

I used other shoe laces from my other boots, wear my Darn Tough boots socks and put it on.

All my disappoinment before disappears and overwritten with joy, pure joy.

My Sagara was MTO as well, but the fitting didn't even come close. It fits like a fuckin glove. Glove!

Perfect! Not too big, not too small, a small breathing room around the toe. It feels kinda weird at first because it's just perfect, I couldn't even move my feet after putting it in. I never owned a boots that didn't kind of slides due to bigger than my feet (small feet problems).

Awesome! Definitely would recommend and probably buy another pair from Baker.

&#x200B;

**1 Month Review - 5 wears**

To my surprise, it only takes 1 day to break-in and it didn't even hurt that much, this hurts the least among my boots. I also didn't get Whites Bites or anything like that, not that I know how it feels like.

Each wear feels better than the previous wear. Didn't get to wear that much due to WFH and social distancing environment. Wearing them once a week when I need to go to the office.

Because of how good it fits, I am reminded by my disappoinment regarding not having hooks because taking it off takes tremendous effort (it gets easier after every wear though). Still, putting on/taking off the shoe tree also needs similar amount of effort. Sigh.

Brushing it before putting it on and after taking it off is a pleasure because Shell Cordovan shines just by brushing it.

My Japanese wife also commented the boots being very cute/kawaii/かわいい due to my small feet and medallion dress toe cap and she even wanted a black leather boots (I didn't tell her the price yet, I didn't dare. But if she do ask, I will tell her around 30k-40k Japanese Yen and redirect her to other brands/leather, lol).

To date, my best boots and I wouldn't buy another pair for few years due to this being very expensive and COVID hit our finances really really hard.

Thank you for reading!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gbxa6jf] (score 15, diepte 0) Whites has a strong presence in japan, I'd be surprised if you couldnt take them to one of the authorized dealers there to get the hooks put in.
[gbxj5ii] (score 14, diepte 0) Awesome boots. I’m not the biggest fan of the look and fit of the Barrie/MP last, so to get MP boots on the 55 last would be my first choice actually.

DHL opened the box the last time I ordered a pair of White’s, and the laces went missing then too. I know it wasn’t White’s that forgot to include them, since I had a friend in the US proxy the boots for me and the laces were there when he shipped them my way. Seems to be a very common thing with DHL for some reason.
[gbxecao] (score 7, diepte 0) They're beauties! And great review, very entertaining!
[gc0l4rx] (score 6, diepte 1 OP) yeah a bit of disappoinment but it's all good. I am happy and proud to have and wear it outside. I do agree with having better looks on the eyelet. 

However, Asian culture needs you to take off your shoes indoor. So, I won't be wearing this when visiting people's home or going to any restaurant that needs you to take off your shoes.

Also, imagine if you urgently need to go to the toilet after reaching home, happened to me.
[gbyo3xf] (score 5, diepte 1) Actually, they have notoriously great customer service. Everyone messes up sometimes.
[gbx94rn] (score 4, diepte 0) Shame about your disappointment. Every man to his taste but I love the look without the hooks.
[gc0ov6u] (score 3, diepte 2) Aye aye, I feel you as an Asian who needs to take his shoes off at my/friends homes. Got Alden tanker but I was able to get it without the hook and with eyelets. Honestly for me, its no problem. Even in humble Asian background, it gives me the smile my when I wear and take off that cordovan beauty.
[gbxa1i6] (score 3, diepte 0) Awesome review, thank you
[gbxgepr] (score 3, diepte 0) Sorry they didn't come out how you wanted but they are still drop dead gorgeous!
[gby701s] (score 3, diepte 2) Well I have both narrow (B/C) and very low volume feet, and it still felt cramped in the instep and ball in D width although the length was correct. And with a cap toe, where White’s does a true cap toe where there are two full layers of leather in addition to the celastic structuring, the toe just looks shapeless. That last works much better as a plain toe in my opinion.

My experience comes from a pair of shell cap toe MP boots that I had to return due to the shell tearing at the vamp/facing seam. A rather rare issue, but it happens. I also have a pair of Semi-Dress on the 55 last with an unstructured toe and a pair of their 300 Oxfords on the C461 last.
[gbxupn6] (score 3, diepte 0) それがハンサムなブーツですね
[gbyeyn6] (score 3, diepte 1) In Japan he isn’t joking when he says it’s expensive. Stumptown cordovan custom whites boots will easily reach 1600usd or more. I drool over some of the Japan market styles but it’s just wayyyy too rich.
[gbxul8m] (score 2, diepte 1) Came here to say this. I like without hooks even more. Especially with shell.
[gc8jrc6] (score 2, diepte 4) I love them. The sprung toe last is a little narrower up front than the 55 last, and there’s less arch support. With the sprung toe you get a nice rolling motion to your gait, which works very well especially when walking up- or downhill.

Here’s an [album](https://imgur.com/a/EI29htw) from when I first got them. I thought the heel was a little too tall, so I removed one layer of the heel stack. They look like [this](https://imgur.com/a/meMzP9p) now.
[gc0k0vn] (score 2, diepte 1 OP) Yeah, 55 last definitely not bad, very comfortable to wear.

My boots were shipped using USPS and then delivered to me via JP Post in Japan.

Is there any reason why the courier would take the laces??
[gc0kfuj] (score 2, diepte 1 OP) ありがとうございます
[gbxy6p2] (score 2, diepte 0) I absolutely prefer the visual weight of the 55 last over the barrie. Also it should be very cheap to have the hooks installed and the edge dressing changed to brown.

I am curious why you didn't use stumptown though? I've had my eye on their White's W100 Y-Tip even.
[gbyrk9o] (score 2, diepte 3) Yeah I think it maybe because they have a larger distribution? Plus redwings have been popular in Japan since forever really. Even Clinch selling for more than most custom engineer boots from brands in the US is wild to me, if you got the money it’s worth it but 2000USD is bloody expensive when you consider that Japanese salaries are generally lower. That being said if I had the money, I’d get some of their Jodphurs.
[gbz0z9a] (score 2, diepte 5) Lakota sells alden for way more actually. It's like 1300USD roughly for cordovan shoes if I remember correctly, I was living in Kyoto so I saw the prices in the Osaka store.
[gc0lvut] (score 2, diepte 1 OP) Yes, as u/peachfuzzmcgee had commented. It's very, very expensive. Although I do agree that it looks damn beautiful.

I stumbled upon [White's MP Black CX by Stumptown](https://store.stumptownjapan.com/shop/g/g5784330001018/) when I searched for White's in Japan. However, they don't have my size for the ready stock and they don't really do custom MPs.

I tried custom-ordering the Semi-Dress CXL instead and the price shoots up to almost what I paid for a Shell from Baker.
[gc1fszb] (score 2, diepte 2) Jeez, still it turned our for the best, that shell pair you picked up looks great!
[gbxyogn] (score 2, diepte 0) If you think they feel good and broken in after 5 wears, wait till they feel a year from now once the footbed has fully set and those midsoles loosen up a bit. Should be even nicer.
[gbxzmon] (score 2, diepte 0) Thanks for the review. I went to Baker's this weekend, met with Kyle, and was fitted for a pair of White's. You can buy your own edge dressing to make them brown. Baker's uses Fiebings.
[gc0ml36] (score 2, diepte 2 OP) Yeah, I understand. That's why I didn't bother them regarding the hooks and edge trim because US situation was pretty bad that time, COVID, fires, BLM. I am happy just to have the boots during Autumn/Winter this year.
[gc0mbrm] (score 2, diepte 1 OP) hmm, I wouldn't say it's veryy bad, I could understand. It's a shit show in the US this past few months, I couldn't really blame them for messing up.
[gc0m3ag] (score 2, diepte 1 OP) Thank you very much.

It's not skinny tapered, it's a [relaxed tapered chino selvedge by PBJ](https://www.okayamadenim.com/products/pure-blue-japan-12oz-selvedge-chino-pants-beige)
[gc0ns0y] (score 2, diepte 0) These look fantastic!  I'm glad you went with the medallion cap toe.  I look forward to seeing future pics of these!
[gc0kaq2] (score 1, diepte 1 OP) Thank you for reading, glad you like it.
[gc0k977] (score 1, diepte 1 OP) Yeah, there are some shops that sell custom White's over here, but I doubt they will do it for free. I think the price would be around the same as normal cobbler. I'll change it to hooks if it doesn't get easier to take it off during my resole.
[gbxe9ep] (score 1, diepte 0) Great looking pair.
[gc0l61a] (score 1, diepte 1 OP) thank you
[gc0ka5i] (score 1, diepte 1 OP) I know!! Thank you for reading.
[gc0kcn3] (score 1, diepte 1 OP) Yeah, a bit of disappointment but it's all good, I'm happy to wear it everyday if I can (not that I would).
[gby67bu] (score 1, diepte 1) This is interesting, would you mind sharing why you dont like fit of the MP last?
[gby7mhx] (score 1, diepte 3) ah indeed agree the MP looks so much better plain toe. Nice to get an opinionated response :)
[gc7i2pw] (score 1, diepte 3) How do you like their oxford? How does the last compare to the 55?
[gc2vvav] (score 1, diepte 2) I'm dying to know the answer to this

Great looking boots by the way!
[gbyfdc2] (score 1, diepte 2) Woooo that's starting in on Clinch territory. The W100 Y-Tips are 1300usd, but I can't believe how hard all the pricing is being raised. The japan red wings seem to be mostly normal price in comparison.
[gbyubzl] (score 1, diepte 4) Yeagers are a personal grail here. I believe Lakota house distributes Aldens at about US prices, but I know they run a premium in the EU market. I guess different regions get different benefits?
[gbz144i] (score 1, diepte 6) Oh wow really? I guess they're exclusively discounted in NA.
[gc3yez1] (score 1, diepte 2) Oh man didn’t know they were that much 20万円 is no joke for CXL, I’m surprised that bakes ships international since they are cutting into whites japans business. I’m glad it’s not like Alden, where you can’t ship from US retailers. My size is not common in Japan so I never bought any shoes while living in Kyoto.
[gc0mmn7] (score 1, diepte 1 OP) yesss, I cannot wait and will post a review for that as well.
[gc0m8ll] (score 1, diepte 1 OP) Great info! Thank you very much. I'll try it on other boots first before this boots, and maybe another review after that.
[gbyp1ll] (score 1, diepte 0) Great review. Post an update again in a few months!
[gc0f20c] (score 1, diepte 0) Damn that looks goood. What pant are those? It looks like chino selvedge. I like the cut very skinny taper.

Tempted but I have too many boots already and few days in a year to wear em (California and all).
[gca4lpe] (score 1, diepte 0) Great review! Love seeing small feet representation around here (I’m 6-6.5D myself). The boots look amazing.
[gevfkno] (score 1, diepte 0) Those look so good!
[gby5fnj] (score -1, diepte 0) Great boots - thanks for sharing.

Bakers sounds terrible. Bad post-purchase CS and a critical screw up on a custom make up. Personally I would never use them again.

=== THREAD 72pnt3 ===
SUBREDDIT: r/goodyearwelt
DATUM: 2017-09-27  SCORE: 14  REACTIES: 47
TITEL: [Discussion] What are some shoes that you love but rarely wear?
POST (source_id=post):
Whether it be due to discomfort, lack of occasion, or weather.

For me, it's my [Andrew Lock Monk Straps](https://imgur.com/a/nJ8DM). GF bought them for my birthday and they were my first "real" pair of shoes.

Wore them quite a few times that summer, but once fall/winter rolled around, I stored them away and never really wore them again. I tried to, but they just hurt my feet way too much, like they weren't even broken in anymore. 

Love these shoes, love the look, and has sentimental value, but I always seem to reach for another pair of shoes.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dnl6d59] (score 8, diepte 0) My [Alden x Leffot Greenwich wingtip boots](https://leffot.com/alden-x-leffot-greenwich-boots-reverse-hunting-green-chamois/) in hunting green reverse chamois.

They were an impulse buy- I saw them in the window on a visit to NYC and had to have them. Even though I sat on the trigger for a few weeks after, its not like I was filling a hole or following a plan, I just liked them.

I've had a hard time figuring out how to make them work, mostly because I need better pants and need to get more comfortable with colors that aren't dark brown. I'm hoping it'll be better this upcoming fall/winter.
[dnlbsd6] (score 7, diepte 0) I hate to say it. . .but all my shell boots. I am in jeans 99.9% of the time and I just always seem to grab something else. They sure are pretty to look at, and when I do wear them I can't get enough, just don't reach for them as often as I should.
[dnlbnz7] (score 6, diepte 1) Those Alden's are awesome, though.  You should totally bring them into rotation more.  They're great bad weather boots, too.
[dnlx5jr] (score 6, diepte 1 OP) Totally unrelated, but what size are you? :)
[dnlblii] (score 5, diepte 0) Shame about the discomfort because the pattern on those monk straps is really clean and the color is great, too.

To add to the discussion, if I don't wear something, I get rid of it.  Since beginning this hobby, I've had 14 pairs of shoes that I wore (not counting the ones that I immediately sold for not fitting) and I'm down to 7 pairs because either I moved up on quality or I just didn't like the design/pattern/last enough.  I wear all 7 pairs frequently, barring weather limitations, and now I don't have to feel bad about having stuff I don't wear.
[dnl1pt3] (score 4, diepte 0) For me it's my llama balmorals from meermin. At first I thought it was just the Hiro last that didn't fit. Then I got derbies on the Hiro in the same size that fit perfectly. Current hypothesis is that they're mislabeled 8UK's that were supposed to be 8'5 UK (anyone want them?)
[dnlcvt9] (score 3, diepte 0) Burgundy AE McAllisters. Under the right circumstances, they look amazing... parties, even a bright bar. A surprisingly adventurous color for its darkness. But I think oxblood more versatile.
[dnmadg9] (score 3, diepte 1) I originally wanted to give some advice, but neutral colored accessories with a pattern make it hard to escape the neutral color family for the rest of your outfit.

But, here's my best shot. . .

Wear a belt that satisfies 3 criteria: 1 non-neutral color (red, green, blue, whatever), 1 of the colors from the boots (khaki and..lightish charcoal?), and some texture/pattern, like a braid belt made of cloth or something.

Then dress the rest around the belt. Keep the pants on the darker side, and everything will probably be great.
[dnlk4kx] (score 3, diepte 0) My [C&J black Radnors](https://www.crockettandjones.com/radnor-black-wax-calf/). They may not be anything special to look at, but wearing those big, heavy, high boots make me feel like kicking ass and taking names, and they're really comfortable.

I bought them for those occasions where I have to walk to the office in really bad weather (storm, snow), yet still need decent looking shoes (no one notices the heavy commando lugs). Also, I wanted to have at least one pair of lugged soles, just in case.

So I wear them maybe 5, 6 times a year. Should probably have bought cheaper boots for that purpose.
[dnl4x71] (score 2, diepte 2) I'm out of town so I dont have pics but the leather really is something else. Very soft and buttery out of the box. 

These pics are illustrative - leather has a lot of character 
https://threads.dappered.com/showthread.php/22457-First-experience-with-Meermin-Mallorca
[dnpxsm3] (score 2, diepte 2) Ah, my apologies - they're labeled as 8.5 but are really 8UKs. I tried on 7.5 UKs the first time they sent them to me and they're bigger than that, but they're smaller than my 8.5UK derbies (i'm a pretty reliable 8.5UK)
[dnma1qu] (score 2, diepte 1) black oxfords are historically and currently considered a workplace essential
[dnma0p9] (score 2, diepte 1) if your shell boots are glazed and you feel like the shininess sorta doesn't work with the casualness of the jeans, (next part is just me guessing things about your wardrobe) try a pair of chinos with a v-neck instead of jeans; wear that with the boots (and since it's september, a light jacket)
[dnldsrx] (score 2, diepte 1) I wear mine all the time. I think they go with pretty much everything. Even black of you're going for that look. Only thing I don't like is the commando sole.
[dnle0gz] (score 2, diepte 0) All of my dressier shoes. I'm normally in jean like pants or chinos and I find chiseled toes don't work as well with that. Plus, I've come to the realization that I prefer rounded toes over most sleek toes for comfort. So all but a few dress shoes are on the chopping block for me.
[dnnet2z] (score 2, diepte 1) So ... where can I get the slippers?
[dnlq858] (score 2, diepte 0) Ignore the terrible, frayed pants that I've long-since thrown out, but I love these [Trickers for Ted Baker "Daniel"](https://i.imgur.com/TRq1NhO.jpg) shortwings, but my feet don't love them. 

I'm going to try having a cobbler cobble together a better fit for me. They're too wide, so my feet swims in them, and inevitably my toes slide forward and cram into the end.
[dnly1cv] (score 2, diepte 0) As the owner of a meagre 4 pairs of GYW shoes I can say that what I lack in variety and excitement—missing out on most of the interesting GMTOs etc—I gain in that I appreciate and like all my shoes in an equal manner.

Buuuut if I had to choose a pair that I can’t/don’t wear as much as I’d like, it’d probably be my [Alden shell longwings](https://imgur.com/a/SMi7c). I love these, they feel and look great, but living in a (sub)tropical climate with frequent heavy rains, shell that develops ridiculous rain-welts and markings is a source of great irritation and anxiety.

Whenever I wear them I have to check the forecast, and I frequently find myself reaching for my [invincible pebble grains](https://i.imgur.com/tZ28G9l.jpg) instead, which have been soaked in torrential downpours more times than I care to remember.

Shell is pretty, but overrated.
[dnm9ywn] (score 2, diepte 0) Anything black.  I don't wear suits and every time I try to wear black shoes I always feel like they look odd.
[dnl2p3l] (score 1, diepte 1) That's not my size but I'm interested in llama leather. Can you describe how it felt / looks or share pics?
[dno3z1o] (score 1, diepte 1) Weird. I have Hiro derbies and oxfords and these llama balmoral boots and they all fit similar. Aside from the possibility that they're mislabeled, could it be that the boots are just an example of meermins famously terrible break in period?
[dno42w3] (score 1, diepte 2) I thought that at first but when I measured the two the balmorals are about a centimeter shorter. It's a real bummer because I'd been lusting over them for a long time
[dnpgkrh] (score 1, diepte 1) If they are mistakesand truly 8.5, I'd love them. I have Meermin burgundy calf balmoral boots (in UK8.5, so I could verify the measurements), and am upset I hesitated in a Carmina pair in rubi cordovan earlier this week. Brown would work.
[dnl2nvp] (score 1, diepte 0) My Black AE park aves for 2 reason.

Its still hot in texas so i wear linen pants to work in shades of khakis mostly. I wear brown shoes with those usually. Once we get colder, my pants turn more black and grey and they'll be more in rotation.

Also, they seem very formal for the office and I don't want to "waste" them in the office if that makes sense. It's dumb and I just need to wear them more.
[dnl53wo] (score 1, diepte 1 OP) Yeah, I've been wanting to get some park aves, but I realized that I would rarely have an occasion formal enough to wear them haha.
[dnn50as] (score 1, diepte 2) True but when to most of your coworker Johnson and Murphy is high end shoes it seems a waste to wear them to the office.
[dnnqalo] (score 1, diepte 3) Eh dress for yourself
[dnnerxu] (score 1, diepte 2) Mostly for very conservative places like banks though, especially Swiss banks.
[dnnq9wu] (score 1, diepte 3) I don't think that's true at all. You can wear them casually at work with just about anything.
[dnlfd9c] (score 1, diepte 2) Thanks! I'll be working on it
[dnletc1] (score 1, diepte 1) those would look killer with dark denim or navy chinos
[dnmvmt6] (score 1, diepte 1) flannel or tweed trousers in navy, grey, brown would look sooo good
[dnplhtg] (score 1, diepte 1) I disagree, burgundy is more versatile, lots of people would consider oxblood boots to be odd-looking for instance. However, I can see why you might prefer oxblood for McAllisters, the burgundy might look almost black in more yellow or simply dimmer indoor light.
[dnldczq] (score 1, diepte 0) Iceberg Kudus.  IDK but they seem flashy as heck and its hard for me to match etc with them being color blind on almost all levels.
[dnlgh7w] (score 1, diepte 2) Yah I just have the regular dainite sole.
[dnlex1l] (score 1, diepte 0) Alden black tassel loafers, because I'm almost always wearing brown or grey suede loafers (when I wear loafers)
[dnlney6] (score 1, diepte 1) Black tassles can be incorporated into some fashion forward fits..always wanted some but I'm a safe guy so I tend to buy brown shoes..
[dnlmkpq] (score 1, diepte 0) My Crockett and Jones Weybridges in burgundy.  Absolutely love the look of these but the heel counter is murder even after a year of trying to break them in.  I can wear them for a couple of hours if I don;t have to walk around too much but otherwise I have to choose other shoes.
[dnlpgmz] (score 1, diepte 0) Allen Edmonds Jefferson shoes in brown. I bought them when I was working in a more formal office. Now I'm in a very casual office (one guy wears these most of the winter https://cdn.foodbeast.com/content/uploads/2016/03/Smores-Slippers.jpg) and they seem out of place most of the time.
[dnly7ws] (score 1, diepte 1) Pity, cos they look nice and have a great patina. Perhaps an insole or tongue pad?
[dno4dz0] (score 1, diepte 1) I'm kind of with you on shell. I find myself forgoing shell a lot when I don't know what the weather will be like. That said, my Alden horween shell gets way less spotty than my Compiel and Shinki. I just ordered chelseas in Italian shell, so hopefully they'll be okay.
[dnly35h] (score 1, diepte 0) My Durango harness boots. 

https://www.durangoboots.com/mens/country-lifestyle/durango-black-harness-boot/DB510.html?country=US&gclid=CjwKCAjwmK3OBRBKEiwAOL6t1J017skaJGqk67Vx-v4Ev-HIPmAIFUZ5HwJqgrL30uCHd_QwjSxVZhoCtmYQAvD_BwE&kwid=productads-adid%5E178113076492-device%5Ec-plaid%5E286879439711-sku%5EDB5102E85-adType%5EPLA&currency=USD

I rarely have the occasion, save for when I play a concert with a "rock" band, when I wear them with my Levi's 507 boot cut skin tight 70's rock god jeans (which I also almost never wear). It's not an "outfit" as much as it's a "costume". But it's fun as hell.
[dnm6qfv] (score 1, diepte 0) My Nisolo Emilio Chukka boots, not the nicest pair I have. Super comfortable though, they just feel dressy.
[dnme5hi] (score 1, diepte 0) AE Neumok wingtips in blue. I bought them with the idea that they would serve as a casual dress shoe option and wore them frequently initially.

But then I bought AE Strandmoks in brown with a dainite sole and I reach for those much more frequently nowadays than the Neumoks.
[dnn9dso] (score 1, diepte 0) My beloved walnut strand. Got it last year, decided to wear them for my wedding and sort of saving it. Only wear them on the carpet a few times, and when i had my suit tailored. Whenever i see pictures i tell myself that i am going to wear the shit out of them after wedding, and i believe i will.

