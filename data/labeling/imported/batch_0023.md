# Label-batch batch_0023

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
Schrijf het resultaat naar `batch_0023.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 55ers7, 2tfwps, juqnr8, 1xpj9x1).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 55ers7 ===
SUBREDDIT: r/goodyearwelt
DATUM: 2016-10-01  SCORE: 6  REACTIES: 45
TITEL: Insole questions..favorite commercial brand? do you prefer orthotics?
POST (source_id=post):
I've searched this sub and while there's some insole info and I'd like to get your opinions on your favorite brands and your usage. I've been using the orange Superfeet, which I like and they're quite pricey. I've been investing in better quality shoes and wondering if I should buy a new pair of insoles for each pair of shoes/boots. If I were to invest in orthotics,do I want a new set for each or swap between? I have a few cheaper Dr Scholls that I use if not sporting the Superfeet. Is there a less pricey alternative that you prefer?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d89wplw] (score 8, diepte 1) Is there something wrong with your feet so that you don't have arches? A lot of people wear insoles
[d8a2lzz] (score 6, diepte 0) I actually prefer the Dr. Scholls gel sports inserts over my superfeet inserts, which cost 25 vs 55 for the superfeet. I find the gel inserts with hard arch supports to be much more comfortable than the superfeet inserts, which kind of bug me around then ball of my foot. To bad I can't return the superfeet ones because I'd probably buy two more pairs of the Dr. Scholls ones with that money.
[d8ad9q5] (score 6, diepte 0) There are 26 tiny bones in the foot that must articulate while supporting your entire weight at times.  They dynamics of this is the subject of many lifetimes of worthwhile study.  No two feet are shaped or move the same way, no two feet operate in the same environment or under the same stresses.  Because of this, comfortable footwear will always be, to some degree, a trial-and-error process.

Considering that a trip to the Podiatrist, and possibly custom orthotics, will cost several hundreds of dollars with a possibility of failure.  I don't see the harm in trying a few insoles if it brings you relief.  

Look at your foot at rest with no weight on it.  This is the natural shape of your foot.  Try to select an insole that supports the natural shape of your foot, so that the stresses are applied on your feet in an even and natural way.  Make sure your shoes fit properly and do not apply stress to any part of your foot, that stress will be distributed across your foot and work against your best efforts.  Treat yourself right, sore feet will affect everything you do.
[d8a6z7l] (score 5, diepte 1) Ever work a job where you stand and walk and work all day? Ya need insoles.
[d8ag1wq] (score 5, diepte 5) I get the feeling that you know very little about how feet actually work...
[d89zg6t] (score 5, diepte 0) I use superfeet black in my shoes that don't have good support. 

Just in case you weren't aware, orthotics are covered without any doctor note requirements in FSA and HRA accounts, so you get get them at a much better pre-income tax value if you participate in a plan like that.
[d8a6xyc] (score 5, diepte 1) It's ok it took me 3 tries to get my phone to not say dr schools too
[d89xfvt] (score 4, diepte 1 OP) I do need arch support, yes. And all my Red Wings have arrived without any insoles, so something is needed for comfort from the get-go.
[d8a9296] (score 3, diepte 3) I've got bitchin socks (padded darn tough) but standing on concrete for 8hrs leaves my feet sore. Lack of arch support maybe? That's usually what hurts, arch and ball.
[d8aame6] (score 3, diepte 1) I'm not sure why people would down vote a pretty straight forward question. 

I also have no clue why people need them and would love to know as I don't have any podiatrist friends or personal experience.
[d8a22uz] (score 3, diepte 0) Anyone ever try Birkenstock insoles? 

I love Birkenstock sandals, but I don't know if their insoles would work in a leather sole boot like Redwing iron rangers.

Thoughts?
[d8a6gz0] (score 3, diepte 2) I have the RW leather insoles, in my 1907s. They are comfy, but not great. They mold to your feet so they do become comfortable but not cushion-y. I have a set of the Dr.Scholls work boot insoles in my Iron Rangers and they are awesome. Super comfy and very affordable ($9)
[d8a4677] (score 3, diepte 0) Redwing makes a molding orthotic that is red and black that I used for years. They are superbly comfortable, and were lasting me 2-3 years per pair. They are (last time i checked) $50.
[d8a778j] (score 2, diepte 4) They come in a 'one size fits all' package. Ranges from sizes like 10-13, and you trim the toe area of the insole ona  dotted line for whatever size shoe you are. I cut mine to the same size on the shoe, and it fits fine.
[d8a7dbn] (score 2, diepte 1) Thanks for sharing! Was actually considering getting a Superfeet for the comfort, but I guess Dr School is now what I will get.
[d8achby] (score 2, diepte 0) Although I find most GYW shoes perfectly supportive once the footbeds mold, I have insoles in some shoes for fit or comfort. Certainly the extra support can be helpful for a day walking.  Archmolds orange are great if the shoe has room for them as you mold them to your foot after heating. Profoot blue mold to your feet just from wearing and are great for extra shock absorption.
[d8acki7] (score 2, diepte 0) My internationally shipped (i.e. shipping back to do a return was expensive) are a bit loose. I am thinking of putting in some leather insoles to make them fit snugger. Any suggestions?

I want to stick with leather because synthetics of all types stink up real fast. And also due to the long-term durability factor.
[d8add79] (score 2, diepte 0) My orthotic insoles cost more than my shoes.  >_<
[d8alnwz] (score 2, diepte 0) I use Biolab (of Western Australia) custom orthotics developed from a foot scan because of several issues with my feet: low arches, plantar fasciitis. severe [ankle impingement](http://emedicine.medscape.com/article/85311-overview). If you feel no discomfort, I don't think it is any issue to carry on, assuming your feet are perfectly fine. A well-fitted generic insole works fine for most according to my podiatrist, just as it does with shoes.
[d8ar2u3] (score 2, diepte 0) Those of you that use inserts, how do you handle sizing? I find it hard to buy something that I can't try on and also has stitched insoles. Do you size way up so you can fit an insert on top of the existing insole?  I've ripped out insoles of shoes and used superfeet inserts in many shoes, but this doesn't really work if you are trying them on from and online retailer.
[d8b73gy] (score 2, diepte 1) Newbie with flat feet here - I doubt most leather/cork footbeds would mould enough to provide the arch support that flat feet would benefit from.
[d8c1uzu] (score 2, diepte 0) http://podpost.us/issue/march/article/five-best-orthotics-or-insoles-of-2014
[d8c60eo] (score 2, diepte 2) I've been happy with the powerstep slimtech, good support with a decent amount of give, thus not too hard, and maintains the toe room of my dress shoes.
https://www.amazon.com/gp/product/B005DIO4V0/ref=oh_aui_detailpage_o07_s00?ie=UTF8&psc=1
[d8c3h2z] (score 2, diepte 0) I really like Spenco's thin green insoles.  They're totally flat and don't offer any additional arch support (which is a plus for me). 

They've got the most bounce of any thin insole I've ever tried. They really make a difference when you're on your feet all day. They're thin enough that they don't effect the fit of shoes *that* much.
[d8awtst] (score 1, diepte 7) As far as the midfoot/arch goes, it acts like a shock absorber. There are 5 little bones all connected by muscles and the *plantar fascia*, the tendon that helps form the arch of the foot. When your foot lands, the arch of the foot does not stay completely stiff, it will sort of "move" to help redistribute the shock of impact and will "stiffen" to give a stronger base for your body to push off of and move forward in the following step.    
    
There's the "intricacies" boiled down, I'm sure you could easily find information on any number of sites that could explain it in much more detail. Perhaps you should try googling for information before making a knob of yourself.
[d8axav3] (score 1, diepte 9) If you're running on the assumption that his feet do not move for the aforementioned 8 hours, then the issue is here is not with knowledge.
[kvp8e9r] (score 1, diepte 9) Neckbeard never spend more than 10 mins on his feet before running out of breath 😭
[d8a2hlc] (score 1, diepte 1 OP) I haven't tried. I'm also curious about the Red Wing brand leather insoles. Anyone try them?
[d8a6x4z] (score 1, diepte 3) Do you have to up/down size the dr scholls?
[d8ezynn] (score 1, diepte 1) Could you link the Dr Scholls inserts you have? I'm only seeing the cheap ~$10 massaging gel sports inserts, but you said yours were around 25. Thanks
[d8f4i9d] (score 1, diepte 2) Here you go - http://www.target.com/p/dr-scholl-s-active-series-replacement-insoles-for-men/-/A-14237023?ref=tgt_adv_XS000000&AFID=google_pla_df&CPNG=&adgroup=&LID=700000001170770pgs&network=g&device=m&location=9002042&gclid=CjwKEAjwydK_BRDK34GenvLB61YSJACZ8da3qn8JJjkCbxu-2p2NN9wXTWyJiBshWsxgNhHKhzzL6hoCtXXw_wcB&gclsrc=aw.ds
[d8aqc8x] (score 1, diepte 1) I've found all their insoles to be very comfortable.  I have a pair in my workboots for the past 6 years.
[i2su494] (score 1, diepte 1) Yup, learned this the hard way
[d8ar9b9] (score 1, diepte 1) It's been a frustrating process, there isn't much info on-line.

I went to the nearest Allen Edmonds and got fitted.  I'm a hair over lengthwise 9.5D US. I only had an hour there and I'm going back to try on different size to be certain -- 10EEE Strands fit the best. (I think 9.5EE might be the best fit.)
[d8b6z6i] (score 1, diepte 1) I bought Allen Edmonds Dalton boots in 8.5 D, but got them exchanged for an 8.5 E to accommodate my Superfeet Go 3/4th insoles. I think they might be slightly too wide for my toes though... maybe I should use thicker socks.
[d8ar5qr] (score 1, diepte 0) Does a person really need to use Insoles with good shoes? I am new to a pair of Redwing Beckmans. So far the leather/cork footbed is comfortable. I do wear them (and my day to day work boots, also Redwing) with Fox River Wool socks for breathability and comfort. And I do use insoles in the work boots.

Should I consider insoles for my Beckmans or not? The Leather/Cork is supposed to mould to the foot like an insole right? And should that not last longer then a "replaceable" insole, like for the life of the shoe?

Not trying to sound like an ass like the guy below that got downvoted. I'm genuinely curious if I would need insoles down the road. aka, will the built in footbed "wear out"? And if so would it be better to start using an insole now before the footbed is fully moulded or wait until it has formed to my feet before adding an insole?
[d8bpqil] (score 1, diepte 0) Superfeet greens did wonders for me after a back injury.
[d8bzrx9] (score 1, diepte 0) I've got flat-ass feet and a relatively low volume foot. I've always wondered if I should try something, but never have.
[kwkfupa] (score 1, diepte 1) Have you?
[d8c3knm] (score 1, diepte 1 OP) Nice! Looking into Powerstep.
[d8atbi4] (score 0, diepte 3) I try and give people the benefit of the doubt (in this sub).   

Admittedly it could have been worded better but there isn't anything to clearly denote intent.
[d8axrz0] (score -1, diepte 10) The issue is he can't distribute his weight properly while standing. Pretty sure he may have gait issues, too.

There is zero reason your arch/balls of your foot should hurt when standing/walking/whatever it is he really does for his job for so long unless your foot muscles have atrophied or you are putting un-due strain on to them I.E wearing high heels, or other improper footwear.

He should see an actual podiatrist, before relying on "inserts". Because I guarantee you that there is much worse underlying cause to his issues.
[d8aqndg] (score -2, diepte 2) Downvoting for no reason? I for one have never heard of such a thing. (I suppose one reason is "is there something wrong with X" comes off as a little sarcastic? But there's a chance it's a genuine question)
[d8awxez] (score -4, diepte 8) Pretty sure we are discussing standing, not walking... But okay.

And you can handle my door knob any day of the week. :P Stay classy.
[d8arupf] (score -5, diepte 6) How are feet supposed to work, sensei? 


Seriously, either explain the intricacies of "Foot movement" or bugger off with the loaded statements. -_-
[d8a8iue] (score -7, diepte 2) No, you don't... All you need is a good pair of socks. Unless you have actual foot problems; insoles are the bane of real shoes. Especially in hot weather.
[d89wje3] (score -8, diepte 0) why do you want insoles? is there something wrong with your feet?
[d8aagvx] (score -13, diepte 4) I don't quite understand why people need "Arch support"... You should distribute the weight over your entire foot when you stand, not just on your arch/ball. Are you wearing high heels, or something? <_<

=== THREAD 2tfwps ===
SUBREDDIT: r/BarefootRunning
DATUM: 2015-01-23  SCORE: 12  REACTIES: 41
TITEL: Does anyone barefoot run IN snow?
POST (source_id=post):
By In snow I don't mean running on top of densely packed snow, such as I've seen on Youtube. I mean running through a decent amount of snow, where you're whole foot is submerged into the snow when it hits the ground

I've begun trying this, but I simply can't get my feet to stop going numb -- I feel as if my workouts are garbage now because I'm battlign the sensation of my cold feet instead of really pushing myself forward... not to mention that it may be messing up my form, which is causing blisters(see my other thread I just made for that story)

So, does anyone actually do this? Have you trained yourself to be able to run through snow fields etc? Or is it physically impossible to do this?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cnyoekg] (score 11, diepte 0) I wouldn't. There's not much point to running barefoot if you can't feel your feet/toes, and you are much more susceptible to injury. It'll just make recovery time longer.

Also, if you injure yourself during the run and you don't have backup shoes/socks, you could be risking frostbite. 

I'd stick to short runs in dry weather above 40F. I've done 30F before for short runs and it's doable, but 20F my feet just got really numb and I got blisters because of it.
[cnypr9r] (score 5, diepte 1) Wow, that could be why I get blisters when it's cold out... I never even thought of that, that it numbs the foot and changes the way I use it

Well, what are barefooters to do then? It seems abit hypocritical to be barefoot runners, but then give up running barefoot for four months out of the year
[cnyrk3w] (score 3, diepte 2) Use something really minimalistic.

I've been using Xeroshoes. You can make em yourself for a really custom fit, and I use some cheap toe socks I found online. My feet actually still get a little numb, but it's not as bad. And repeated pebble strikes on the same area won't mess up your feet bad if you're unlucky.
[cnz0uxj] (score 3, diepte 2) I've done 8 miles at 7 degrees and it went okay.   When I ran at 5 degrees with some snow on the ground, I got frostbite and giant water blisters on the bottom of my feet.   They healed up after a couple weeks. 

Eventually it was all good.   As long as there isn't moisture I can go pretty cold.   When it's super cold it is best to run on textured surfaces to keep the blood moving.   On smooth pavement it seems the feet and toes get colder faster.
[cnz1b3v] (score 2, diepte 1) It's not as bad today since we have medical facilities and antibiotics for broken skin, but historically not being able to walk/run for a couple of days puts a serious damper on survivability in a small group.
[cnyw3ec] (score 2, diepte 0) When my toes get cold, it messes up my biomechanics as I can't feel the ground properly.
[cnzer32] (score 2, diepte 0) You could check here.  Some of the people from other countries run in some pretty cold temperatures.

http://thebarefootrunners.org/threads/5th-annual-winter-challenge.17131/
[co1dx3a] (score 2, diepte 0) I use my VFF Komodo Sport on -20 without much of a problem. There's a trick when running barefoot on cold weather. You can't just jump into it, it takes a lot of training.
[co0gnsf] (score 1, diepte 3) I don't think this makes a big difference, does it? I've ran pure barefoot in snow, ran in vibrams and in fila skeletoes, all three the sensation was the same : feet go numb!

So how can a minimalist shoe protect against the snow or running THROUGH snow?
[co0h4k4] (score 1, diepte 4) Stick to paved surfaces in the winter =D

How long are your runs? My feet are usually numb for a mile or three, and then any longer they start to warm up.
[co0h8qs] (score 1, diepte 5) I like the sponge of the soil to absorb shock -- I don't think running on asphalt or smooth surfaces is natural or good in the long term for our joints

Believe me, I was running around a track one day, experiencing the 'feet bashing' as I started picking up speed, so cut onto the football field = never went back to running on hard surfaces

So thats why i actually need to trudge/run THROUGH snow. People don't plow the field where I prefer to run
[co0hnf6] (score 1, diepte 6) Well then you can't really be barefoot or minimalist on the snow. If I was you I'd find some minimalist shoes and some wool socks, and you'll be able to run everywhere in the winter. 

My only practical route where I am now is a paved road, and once I learned how to run on it I never have any foot or joint pain, the most I'll have is some muscle soreness.
[co0hsk4] (score 1, diepte 7) Well, maybe in the winter I will try running on the asphalt, since I dont have a clay track around
[co0i7rs] (score 1, diepte 8) Just try running a bit less than normal, if you don't have much pain after a run then you know ya doin it right.
[cnz19pu] (score 1, diepte 3) That's a good point the surface matters a lot.

Even on a cold day, smooth granite can absorb sunrays really effectively, and will be considerably warmer.
[cnysft9] (score 1, diepte 0) I just tried last weekend, and it wasn't great.

My first problem was that my feet went numb so I couldn't feel the ground properly.  That's not all bad, as there were patches where I had to run on pavement covered in rock salt.  That would've really hurt bad if I could've felt it.

The second problem was that my feet and legs didn't have enough jump in them, so I wasn't cushioning the landing enough.  My knees felt it the next day, as if I had gone running in shoes and heal striked my way around.

I just did the same run in some VFFs and it was a far better experience for me.  I think I will stick to that until spring hits.
[cnyt4r9] (score 1, diepte 0) I'm a pretty strong proponent for unshod running, but running barefoot in snow is just silly. Even our ancestors who rarely ever worse shoes were smart enough to have some sort of moccasin laced around their feet during the colder months.
[co0jnlq] (score 1, diepte 1) So what can we do? What kind of minimalist running solution is there for running the snow?
[co0yae7] (score 1, diepte 2) There are a wide variety of minimalist closed toed shoes to choose from but you need something to cover your feet.....either that or just move to a region of the country where it doesn't snow. I'm here in California and a "cold" day is 45 degrees.
[cnytooi] (score 1, diepte 0) Tried it. Didn't last long. Probably won't try it again. The moisture is too much when it's that cold.
[cnz0vph] (score 1, diepte 1) Snow at 32 degrees is kind of fun.
[cnywddv] (score 1, diepte 0) You could ask /r/barefoot they'd be more likely to have tried being that they don't really like any (even minimal) shoes.
[cnyxmur] (score 1, diepte 1) Well, I have done it in the past. However it took me about 1 week of walking in the snow to build up the capacity to do it. I may try doing it again, but this year, it's been hell. I simply don't have feet that can withstand the cold enough for me to run in it

edit: actually, probably like 3 weeks, but one week of morning 'training walks' to prepare for it. And it still was a big thing holding me back, but i did manage to do some 'avg' runs in the snow. I'm kind of leaning toward the consensus here and putting this in the 'thats crazy' category
[cnyxxso] (score 1, diepte 2) I ran the polar dash in Chicago the weekend before last and my feet with numb with thin wool socks and minimal shoes. I don't think it would have been possible to run that without shoes without getting frostbite.
[cnyzo0j] (score 1, diepte 0) I remember one time when it was fall, my last 5k race of the season, pouring rain, temps just above freezing, winds gusting >60km/hr, everyone was very cold before the race started. I was wearing less minimal shoes than I run in now (NB1400s) and when the gun went off, my feet felt like bricks. It was the worse "race" ever. Running through the snow...nope.
[cnz15j9] (score 1, diepte 0) Why would you think that's a good idea???
[co7075u] (score 1, diepte 1) Not necessarily.  The body will decide to start warming the area.  Its the mitochondria that warm your body and if you are not used to using them (esp in your feet) then they will get tired fast and then, yes, of course you may end up with frostbite.  Everyone should be cautious but you are really just fear mongering.  Makes me wonder why you are even in this subreddit.
[co73gka] (score 1, diepte 2) Well, I did get mild frostbite wearing VFFs in the snow, so there is that.
[co73z5c] (score 1, diepte 3) Hmm, well first of all VFF are not at all warm.  In fact some people would say that being barefoot would be better than a shoe like that because aside from being thin, they separate the toes and they retain moisture. They also are made of materials which are pretty good at heat conduction (rubber and plastic); they are effectively increasing the surface area of the foot by spreading out the toes - having the foot simply exposed to the open air might be better.  If they are at all tight then they will also restrict blood flow which is what would help keep your feet warm.  This is one of the biggest causes of frost bite.  People wearing double layers of socks in shoes fitted for one layer, or simply just shoes which are too snug from the get-go.  My experience with VFF's is that however well they fit they are always sort of tight at least in one area. They have to be in order to stay on. This is going to be true of ANY shoe that is not a true boot going up the ankle.  Obviously there is going to be a trade off between restricting blood flow and insulating the foot and most of the time a shoe with a simple pair of socks will be warmer than being barefoot.  But thinking this will always be the case is where people cause themselves trouble.  Look it up if you don't believe me.  Any survival expert you find credible will report that stuffing multi-layered socked feet into shoes not fit for that will increase chances of frostbite. TL;DR - In some shoes in some conditions you may restrict blood flow too much and not insulate enough.  

Also I did say that every one should be cautious . . . it would take time to develop the mitochondria in the extremities.  They have to learn to store energy and to use it when needed.
[cnzdh82] (score 1, diepte 0) I'd be worried about what might be hiding under that snow. If you end up stepping on something sharp, that could be bad. If you end up stepping on something sharp while your foot is numb, you could get cut and not even realize it.
[co001a9] (score 1, diepte 0) I have been doing it while wearing 5 finger toe shoes. It's been in the 20s to low 30s with about an inch or 2 of snow. I wear thermal layers, gloves, and hat. It's not that bad, you generate a lot of heat. I went about 9 miles.
[co06z31] (score 1, diepte 0) Yeah no. Wear moccasins or mukluks. It gets down to -40 where I live, barefoot in winter would be asking for amputation.
[co0g0fd] (score 1, diepte 1) I have wanted to look into other minimalist options, but I'm abit broke... I'm kind of Barefoot out of necessity -- The other pair of minimalist shoes I have have enough holes in them that makes them basically barefoot, since they're two years old(got them for $30 at CVS, Fila Skeletoes)

What would you say is the cheapest moccasin to buy online? I'm looking for something below $40 hopefully(in a very tight situation until Fall)
[co700fx] (score 1, diepte 0) I see a lot of people here saying there is not much point because of numbness and that it "messed" up their biomechanics.

I think we should treat it like we did when first going barefoot.  Try little bits at a time and allow your body to get used to it.  You do have to push boundaries of comfort at least a little.  But I have done a successful trek in 32 degree temp while the ground was very wet. It was in the woods and we brought shoes just in case.  It was only about five miles.  After a while of cold and numbness our feet actually started to warm themselves.  Its just a process that took time because our bodies had never had to do it before.  I found it really rewarding.

Anyways hasn't anyone here ever heard of Cody Lundine?  I have never seen him mentioned in this subreddit but he should basically be our patron saint.
[co7a0e9] (score 1, diepte 1) Was he famous for running in the snow? lol, I'm a genius!

JK, I think this MIGHT work. However, after asking the question on here about three times and having NO ONE suggest that they run in the snow, it makes me think that we probably can't train the human feet to be 'snow resistant'
[co7gtuk] (score 1, diepte 2) Cody Lundin is a survival teacher that has been barefoot for basically twenty years he spends his time mostly in the arizona desert which does get quite cold at night esp during the winter but its not snowy I don't think.  Best run-on sentence I ever did wrote.  Gonna keep it for posterity.  But naw man don't give up just because everyone here tries to discourage you.  I am training for winter barefoot running and I'm not yet quite able.  Most "barefooters" wear minimal shoes in winter but I hope to be able to do it barefoot one day.  Obviously it depends on what kinds of temperatures you wanna try and run in.  I think its possible to do it pretty easily down to freezing.  But beyond that might take some extra effort since we are pampered our whole lives. I don't wear shoes in winter really - I just do as much as I can barefoot. 

However look up Wim Hof -  he's a guy known as the Iceman who is known especially for going barefoot in the extreme cold.  He made an everest ascent barefoot.  He has a book which I'd love to read soon about how he trained.  You might want to take a look at it.  I have no desire to tackle everest barefoot but the book probably contains a lot of useful info for anyone wanting to increase their ability to go unshod in the cold.
[co7h9hu] (score 1, diepte 3) I can run barefoot in winter, I'm speaking about being able to run barefoot IN and through snow, and I'm not sure people can do that -- However I'll look into what you've said
[co7i120] (score 1, diepte 4) oh well, look into Cody Lundin and esp Wim Hof.
[cnz88y2] (score 0, diepte 0) If you stick with it, you'll find that after numb comes frostbite.
[cnz8oay] (score 0, diepte 0) woollen toe socks will help
[cnziyud] (score 0, diepte 0) Seems dumb because, aside from numb feet not working well, you can't see what you might be stepping on that wants to slice your foot open or impale you. This just seems super dumb all around.
[co43bnv] (score 0, diepte 0) A numb foot is a dumb foot.

=== THREAD juqnr8 ===
SUBREDDIT: r/goodyearwelt
DATUM: 2020-11-15  SCORE: 142  REACTIES: 38
TITEL: [Insoles] Comparison of some full length insoles
POST (source_id=post):
[Album](https://imgur.com/a/qhCB13O)

Insoles, insoles, insoles. Whether you’re trying to fill up a bit of space in a slightly large boot, you're looking to add arch support where none exists, or you enjoy the cloud-like experience of walking on squishy foam all day, you need an insole. 

I’m not an orthopedist. I really don’t have any clue what I’m talking about, but I can at least describe what these things are and my experience using them. You can make your own judgements on what you think will be best for your use.

The featured insoles are: 

[Superfeet Green sz 9.5-11M](https://www.amazon.com/gp/product/B0033BPBD4/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1)

[Superfeet Blue sz 8-9.5M](https://www.amazon.com/gp/product/B0011YEMDK/ref=ppx_yo_dt_b_asin_title_o08_s02?ie=UTF8&psc=1)

[Spenco Polysorb Heavy Duty sz 8-9.5M](https://www.amazon.com/gp/product/B000G1KU2Q/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)

[Spenco RX Comfort Thin sz 8-9.5M](https://www.amazon.com/gp/product/B000S6JTMQ/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)

**Superfeet**:

Insoles like the Superfeets have very stiff, plastic heel cups and arches. They add a lot of “structure” and add a lot of positional support for my foot. It’s a bit difficult to compare specific dimensions between the Green’s and the Blue’s because I have them in different sizes, but I can say that the Green’s are much more contoured. They have a much deeper heel cup, and a bit thicker arch. I’d also think the holes in the bottom allow it to absorb more impact than the Blues. In general, I’d say that if you have room in a boot for the Green’s, get them over the Blues, because they’ll give more structure. Either way, neither of them take up as much space as you’d think. Although they look thick, the actual foam in the middle of the heel cup is only 6mm thick, and the foam at the toes is about 3mm. So, although it’ll reposition your foot with all that plastic structure, your foot will still sit relatively low in the boot. If you haven't clicked on the product pages yet, keep in mind that these are around $40-50.

**Spenco**:

On the other hand, the Spenco’s are more about occupying space, and just getting a much of squishy foam between your foot and the ground. Both of them are much thicker and more flexible than the Superfeets. That yellow bit on the Spenco Polysorb is a bit stiffer than the rest of the black foam, but not a lot more. Although the heel may look similar, the Polysorb heel has about 13mm of foam, compared to 6 on the Superfeets. There’s also closer to 5mm of foam in the toes, compared to 3mm. There is a bit of foam at the arch, but it’s really just foam, not any kind of plastic structure. Moving to the Spenco RX, this is exactly what it looks like… it’s just a flat piece of 4-5mm foam, like you’d find in a pair of Nike’s. The RX Insole is about $10 and the Polysorb is about $20. 


**Thoughts on use**: 

I started buying the Superfeet’s, because that’s what was available at REI. I think they work well for cheaper footwear that doesn’t have much internal structure. I use the Blue’s in my Merrell hiking boots, and the added support is nice. That said, I’ve been using them in my GYW boots for awhile, and think I’ve come to the conclusion that it’s a bit of a mistake. Because there’s already a ton of support and structure in a GYW boot, adding a stiff insole is kind of pointless. If all I’m wanting to do is dial in the fit, and let the existing structure of the boot do it’s job, then the Spenco’s are ideal. They’re much cheaper, and they seem to work with the rest of the boot a bit better, by being much more compliant with the stiff leather footbed. 

I think that if you have a boot with a ton of arch support that is just a bit too big overall, I’d go with a Spenco RX. If you want a ton of padding, and have quite a bit of room to spare in the boot (maybe ½ size worth), the Spenco Polysorb will feel like you’re walking on a Vibram Crepe sole and will add just a bit of arch padding as well. If you have a cheaper pair of shoes (like a sneaker), or will be using them for something a bit more athletic and want something to stiffen it up and add some structure, one of the Superfeet’s is probably a good idea. Keep in mind that, if you're trying to dial in fit, but don't have much room in the ball/toe area, skip all of these, and go for a [3/4 length insole](https://www.amazon.com/gp/product/B004UKT138/ref=ppx_yo_dt_b_asin_title_o08_s01?ie=UTF8&psc=1) instead. 

Like I said, I’m no expert on any of this, but hopefully this is a bit helpful for some folks. If you want more measurements, or clarification on any of this, just ask!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gcexppx] (score 36, diepte 0) My only issue with non-leather insoles vs leather is that insoles tend to smell after a while. Meanwhile, my leather-only soles smell terrified no matter how much wear I put on them. I’m not a smelly foot guy either

Edit - terrific. Not terrified. I’m going to leave up the mistake for historical posterity, but I want it very clearly on the record that my old ass footwear smells ***terrific***
[gcf8mi0] (score 25, diepte 1) > Meanwhile, my leather-only soles smell terrified

Ha.
[gcev1wn] (score 18, diepte 0) This is a Fakespot Reviews Analysis bot. Fakespot detects fake reviews, fake products and unreliable sellers using AI.

Here is the analysis for the Amazon product reviews:

>**Name**: Superfeet GREEN Premium Insoles 

>**Company**: Superfeet

>**Amazon Product Rating**: 4.2 

>**Fakespot Reviews Grade**: D

>**Adjusted Fakespot Rating**: 1.3

>**Analysis Performed at**: 01-10-2020 

[Link to Fakespot Analysis](https://fakespot.com/product/superfeet-green-premium-insoles-f1eca716-f6e4-49dc-a1b1-b9cdeb960079) | [Check out the Fakespot Chrome Extension!](https://chrome.google.com/webstore/detail/fakespot-analyze-fake-ama/nakplnnackehceedgkgkokbgbmfghain)

*Fakespot analyzes the reviews authenticity and not the product quality using AI. We look for real reviews that mention product issues such as counterfeits, defects, and bad return policies that fake reviews try to hide from consumers.*

*We give an A-F letter for trustworthiness of reviews. A = very trustworthy reviews, F = highly untrustworthy reviews. We also provide seller ratings to warn you if the seller can be trusted or not.*
[gceye55] (score 12, diepte 0) I prefer to not use insoles, but if I have to, I've really enjoyed [Filson's cork/foam insoles.](https://www.filson.com/insole-replacement-30077.html#sku=11030077-fco-000002324)  They've been a game changer for the comfort of my LLBean boots.
[gcf9y7y] (score 11, diepte 1) I can smell fear
[gcexe5i] (score 9, diepte 0) I prefer Pedag Viva/Holiday over Superfeet. I find they are just as supportive but cheaper compared to Superfeet, don't leave any pressed markings on the insole if it's leather and also having a leather surface, they match the color of our goodyearwelt shoes better.
[gcf9179] (score 9, diepte 1) +1 for “smell terrified”!
[gch30k5] (score 7, diepte 0) Feet are all different, what works for you most likely might not work for anybody else.

If there is anyone here from germany, go to your doc get a rezept for 'Weichpolster Einlage nach Formabdruck'. These are orthopedic insoles specificly designed to your feet, you'll be granted 2 subsidized pairs per year, cost 14€ max a pair. I'm walking on those since 15+ years, kneepains and backpains are gone.

These are available everywhere but normally cost 100 upwards.
[gcexsec] (score 6, diepte 1 OP) Yeah, you're probably right. I have a Pedag Viva Mini in my C&Js, but don't have experience with the full length model. At least with the Mini, it doesn't seem to take up much space, though. Even less so than the SFs. It's more about narrowing the heel, adding some arch support, and repositioning the ball of the foot with that middle hump thing. I like it, but don't really know how to describe how it alters the fit, because they work in my C&Js that otherwise fit pretty snug.
[gcf0vl7] (score 4, diepte 2) In my opinion it's on the slimmer side.  The heel area is probably 3/8 of an inch slimming down to about 1/4 of an inch in the ball/toe.  It has good arch support and has a cupped shape to keep the foot balanced in the footbed.  [Pic here for reference](https://imgur.com/a/GE8EWlv)
[gcfe95m] (score 4, diepte 0) Anybody have experience with FP insoles and can compare them with Superfeet? I've worn Superfeet green in the past.
[gceziez] (score 3, diepte 1) How’s the thickness of those?
[gcf6kt4] (score 3, diepte 4) I don't have experience with birkenstocks, but these insoles have definitely gotten more comfortable since new (not that they felt bad-just a little stiff) and it really does feel great on the foot.  2 thumbs (or big toes) up!
[gg26zu9] (score 3, diepte 4) I'd give em a shot.  I think they might work because most of the bulk of the insert is in the heel area as opposed to the toes ( it should lock in the foot by giving it more volume and keep the shoe from sliding on the foot and feeling loose) .  It doesn't add volume to the toes much, so you shouldn't get that cramped toe feeling from pushing your toes up into the top of the toe box.  


 Filson does take returns if you slide them in and immediately decide you don't like them, and depending on where you are they might have an actual store near you now (they've expanded their physical stores quite a bit within the last 2 years in the US).
[gcfsgxa] (score 3, diepte 0) I have had bad knees from flat feet ever since I started growing a lot with puberty. Superfeet are in every one of my shoes and I haven't had problems. I put them in running shoes, vans, wolverines, everything. 

I love them.
[gcgqj4r] (score 3, diepte 0) Good post! Superfeet helped my Truman boots go from pretty much unwearable (due to their flat, hard footbed and zero arch support) to quite comfortable overall. Keep in mind I have narrow feet so was able to put the Superfeet in with no problem. The insoles aren't cheap, but  they're worth it.
[gceyq7d] (score 2, diepte 1) Yep, big fan of the Viva as well
[gcfslwi] (score 2, diepte 1) I take my insoles out and hang them to be aired out between wears. Better for the shoe and insole, I find.
[gg23yiy] (score 2, diepte 3) Do you think the filsons will work well for someone trying to fill out the boot a little? I've got some Oak Street trench boots that are about .5 size too big.
[gg2by6k] (score 2, diepte 6) I hope they work out great for you!
[hxl3o7a] (score 2, diepte 9) I may check those out.
[gcg19me] (score 2, diepte 1) I’ll have to try these, didn’t know Filson had insoles.
[gcgy2ia] (score 2, diepte 1) Been wearing FP insoles for the past year. I love them. Great cushion in the ball and heel and solid support throughout. I use them primarily in my skateboarding shoes and they are awesome. Only minor downside is the “mold to your feet” thing. Popped em in the oven for the first wear and they feel so good as they fit your foot perfectly. However, with subsequent wears they take a few minutes for your foot to warm up the insole for it to fit your foot again. For what it’s worth, FP insoles have the best energy absorption of any insole I’ve tried. Well worth it. 

I’m not a fan of whatever hard material the superfeet uses for the heel. Doesn’t feel right for me.
[gcgkq87] (score 2, diepte 1) How do you pick sizes with regards to superfeet, and which models do you use? I wear the green in athletic shoes, but I’m not sure how to adjust my sizing for putting them in nicer footwear, especially when you often can’t try them on?
[gci16aw] (score 2, diepte 2) I wear the green ones. As far as sizing I wear a 10-10.5 in most shoes, so I just buy whatever letter size that correlates with and then trim it. For most of my shoes I can just swap them without issues.  If it’s a shoe like my wolverines that doesn’t have a removable sole, I’ll take the soft insole from another pair of shoes and put it in the boot, and just kind of feel the end of the toe and how far it curls or folds and eyeball it to the super feet. It usually works without issues.
[gciv0k8] (score 2, diepte 3) I apologize, I don’t think I asked what I was actually trying to haha. 

How do you pick the size of boots to get, if you’re going to put the superfeet green in? 

Especially if the boots don’t have removable inserts, the superfeet green sure can change the fit of a boot.
[gcivtwz] (score 2, diepte 4) Ah, my bad. I tend to be closer to a size 10, so when getting boots and stuff I get a 10.5. Unless the 10 feels roomy.
[gcimxef] (score 2, diepte 0) I have had success with adding some much needed arch support to my Grant Stone Ottawa boots with "SOLE Softer Response Thin Sport Heat Moldable Custom Insoles". 

The long name and typical marketing bullshit aside, it's a thin insole with decent arch support at ~32 bucks that molds a bit to your feet and doesn't take up a lot of toe space. 

I used orthoticshop.com to find them. There's a bunch of orthotic insoles on the website.
[hq2vh2z] (score 2, diepte 3) yea, I think that's where I'm at. going to try to get some superfeet's on in person first though
[gcg8pyg] (score 1, diepte 1) I completely agree- my leather insoles never smell. So I have stopped using synthetic insoles. Pedag is a good middle ground of leather + other materials. A bit hard though.
[gcf47yo] (score 1, diepte 3) Thank you - I was looking for someone with some thoughts on cork insoles. Do you feel like the cork molds to you foot well. I’ve found my birkenstocks to be some of my comfiest shoes but not enough cushioning so I’ve been looking for an in between solution or something with both. Thanks!
[gg2b4jf] (score 1, diepte 5) Just ordered. Thanks for your help!
[hxeoymi] (score 1, diepte 6) Did these work out for you /u/hpeden? Curious what did, if anything! I've been comparing insoles for my half size big OSB trench as well. I found some but good to know options...
[hxievdg] (score 1, diepte 7) I ran into the issue of my pinkie toes getting crammed in between the insole and the side of the boot. I cut them in half so only my heel was in the insole. Ultimately I ended up just dealing with them being slightly too big and taking the insoles out. YMMV
[hxix0yv] (score 1, diepte 8) Thanks -- I managed to make mine work with the Red Wing leather footbed but it took a while to find something suitable! The true to size felt a little too snug for my tastes so I went up.
[gcgyg5b] (score 1, diepte 2) I'd give em a shot.  I've had no odor problems like some other people have commented on other insoles.
[gcf8a12] (score 1, diepte 0) I picked up some boots off of eBay that are a snag tight in the toe box. Lucky for me, they have manufacturer removable insoles. I’m thinking about picking up some 3/4 insoles and replacing the current insoles in hopes of gaining a little room back in the toe box while maintaining arch support. Sound logic?
[gcf8qa7] (score 1, diepte 1 OP) Yup. Makes sense. Just make sure there's some kind of actual insole under the removable insert, and not just some fabric lining or something. I'd probably recommend a Pedag Viva Mini as a good place to start on a replacement.
[gcf90ss] (score 1, diepte 2) What do you mean another insole, not just a fabric lining? It’s very hard, I’m pretty sure it’s just leather
[gcf9wy4] (score 1, diepte 3 OP) Yeah, I mean, just make sure there's like a solid bottom to the boot under the insert, and not just a bunch of exposed stitches or nails or something. You didn't mention what kind of boot or what construction it's made with, so I just wanted to clarify that part. Lots of weird stuff out there.
[gcfaaj0] (score 1, diepte 4) Oh I see what you’re saying. They are Chippewa-LL Bean Katahdin boots made with a 270 degree Goodyear welt. There might be some exposed stitches, but it’s the midsole stitching, similar to other GYW shoes.
[gcgexi5] (score 1, diepte 0) Use the Spenco RX Comfort Thin in most of my boots. I really like them. Take them out in the winter if I'm wearing really thick socks.
[hq2m0mo] (score 1, diepte 1) which color superfeet did you go with? I'm having the same issue with my Trumans and am looking for a solution
[hq4hmla] (score 1, diepte 2) I'm pretty sure they're blue or blue/gray ... it's been awhile. Definitely made a huge difference.
[gd62tf1] (score 1, diepte 0) I tried a pair of Superfeet Green hoping for some extra arch support and didn't find them to have any at all.
[hq2mgkt] (score 1, diepte 1) this is what I was hoping to use them for - my Trumans are lacking pretty seriously in the department but don't have a lot of room in the toe box for insole inserts. have you found something that's worked for you?

=== THREAD 1xpj9x1 ===
SUBREDDIT: r/Shoes
DATUM: 2026-11-06  SCORE: 0  REACTIES: 37
TITEL: Are these heels half a size or a full size too big?
POST (source_id=post):
It’s my first time buying heels so I have no idea if these are a half sizes or a full size too big.

Picture 1 with socks (sorry I don’t know the right translation) there’s feet can slide more so I can fit a finger comfortably in the space behind my heel.

Picture 2 without socks there’s more friction on the sole so it’s a little less so there’s still space but I can’t fit a finger.

There’s no half sizes for this pair so I either keep them and wear them with gel soles or toe pads, or I go a full size down but I am afraid it would make them a pain to wear.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[19s8pke41uwn4] (score 11, diepte 0) Way too big. Looks like a child wearing mommy's shoes to play dress-up
[19s8llhcz2w1u] (score 10, diepte 0) Both look massive
[19s8lmcotzemd] (score 8, diepte 0) I woukd try them on again  in the evening after you’ve been on your feet all day and that will usually give you a better answer. 

Looking at the picture alone I would say you can go one size down.
[19s8qpu28kjwj] (score 5, diepte 1) They’re the same size. They’re asking if they should size a full size down or half a size down 😅
[19s8rv69oidoj] (score 5, diepte 1 OP) I thought the same 😭
[19s8m29kle11d] (score 4, diepte 0) There are some things in life you need to answer for yourself.
[19s8ls039bx6o] (score 3, diepte 0) Full size too big. I wonder sometimes, not aimed at you personally, if people on here realize that you can try on shoes and different ones at that.
[19s8mswujuric] (score 3, diepte 2) So, lots of footwear company’s have different standards/sizing. With that said, almost all of them will provide a guide and it’s really easy to measure your feet at home - simply stand on a piece of paper, trace your foot and then measure the length from heel to toe. You can then use that length to match up to the retailers size guide.
[19s8mtu64ubib] (score 2, diepte 1) Get a life.
[19s8lvuet5y9u] (score 2, diepte 1 OP) I bought online so I couldn’t try them on 🥲
[19s8mvehwwwqs] (score 2, diepte 3 OP) Ok thank you, I will see if I find it for this brand!
[19s8nvag3svk5] (score 2, diepte 1 OP) Why?

Edit: Ohhh I see your comments in other posts with muscular legs calling them a man. I am very sorry your life is so miserable that you spend your time like this 🤣

What’s funnier is that you posted in a bodybuilding sub about your muscular arms, so it’s very ironic that you’re hating on other’s legs for this.
[19s8qxznl6l6s] (score 2, diepte 4) I mean, even women with muscular legs look different than man legs.  I still bet I am right about you being a man wearing heels.
[19s8t182ihv43] (score 2, diepte 7 OP) No, sorry to disappoint. Also, even funnier fact, everyone looks different. Women and men don’t all have the same looking legs even between each other 😱
[19s8s61wsn16t] (score 2, diepte 1) How is this even relevant to op’s question?
[19s8t0mr46uv8] (score 2, diepte 2 OP) Nothing, for some reason they spend their time answering to people’s post with things like (and I will copy and paste) “Doesn't look good on your man legs”
[19s8qb2e1lwoy] (score 1, diepte 3) nah fuck off fr
[19s93dv7ok3b6] (score 1, diepte 1) Only if purchased in store & different cuts/shoes vary greatly! I can wear anywhere from a 6.5 to an 8.
[19s8o88goldxf] (score 1, diepte 2) The shape of your leg and foot looks like a man's
[19s8qchssvjr8] (score 1, diepte 3) IDK it's sus you spend your life calling muscular people men. Hard to back pedal out of that one with the receipts we got.
[19s8szw4pwcsj] (score 1, diepte 6) Am I wrong though?  You're a man right?  Also, fun fact. Men and women do in fact look different, even their legs.
[19s8s0w62p8lc] (score 1, diepte 3 OP) I wear a 37 eu LOL.

“Hacking/witchcraft” 😆 they’re hidden on your profile, doesn’t mean they’re hidden from a quick search. Ain’t stalking, just exposing your shit behavior 😉
[19s8u9y37oede] (score 1, diepte 3) Got it! Thanks 😊
[19s8tc2oimtol] (score 1, diepte 0) I wouldn’t say a full size too big because they only look to be a little too big (less than half an inch). I would say a half size too big.
[19s8tnpal1ltv] (score 1, diepte 1 OP) https://reddit.com/link/1xpj9x1/video/253j1z7p420i1/player

  
This is with toe pads. That’s why I fear a full size down will hurt my feet 🤔
[19s96y00ks2ww] (score 1, diepte 0) Too big. You might get blisters.
[19s97uznzaq4l] (score 1, diepte 1 OP) Yea unfortunately they are 😔. My question is if they are half a size too big or a full size.
[19s984zj56ev8] (score 1, diepte 2) It’s hard to guess from photos. I’d try only 1/2 a size first. Since the brand doesn’t sell 1/2 sizes, I think try a full size down if it allows you to do returns.
[19s986hfnsp8j] (score 1, diepte 2) I think since the brand doesn’t do 1/2 sizes, try the full size down. If it allows returns, it doesn’t hurt to try it. If it does not allow returns, I don’t think it’s worth buying from when so many stores offer returns and refunds.
[19s8o9yhh2ytg] (score 0, diepte 3 OP) You can’t even see the shape of my foot LOL
[19s8sw2kwxpz6] (score 0, diepte 5 OP) Yeah it’s a known fact that your biological sex is determined by the look of your legs.
[19s8ubx03eke8] (score 0, diepte 2) Definitely Do NOT go a full size down. Honestly they seem to fit perfect with toe pads. I would just wear toe pads with these and not go down at all.
[19s8nvncnf2kj] (score -1, diepte 2) Ok hartzer tante
[19s8nt190mgn4] (score -1, diepte 0) Are you a man?
[19s8q5bnc5epx] (score -1, diepte 2) Its not about the muscles of the leg, its the shape and how big their foot is.  Also what kind of hacking/witchcraft are you doing to see my post history when I have that turned off.  Stalker.
[19s8la1mw37pg] (score -11, diepte 0) We need more knee high pics 😋

