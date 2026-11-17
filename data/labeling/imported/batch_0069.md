# Label-batch batch_0069

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
Schrijf het resultaat naar `batch_0069.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 11coapw, 17crc22, vfj5jb).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 11coapw ===
SUBREDDIT: r/electricians
DATUM: 2023-02-26  SCORE: 64  REACTIES: 123
TITEL: What's the most feet of pipe you've put up in 8hrs?
POST (source_id=post):
Personally I tend to do around 250-300 in a day, usually including supports. I'm sure I've run more on an easy pre-hung rack.

Reason being, I've got a guy telling me he's done 5000ft, and does 1000 regularly. I'm pretty sure 5000 is an impossibility as that's more than a stick a minute, and 1000 would be one hell of a day under the most ideal of circumstances in my experience. I'm thinking he's bs'ing me really well.

Or am I just a shitter? Foremen have seemed content with my production rate over the years, but I generally don't pay much attention to what other guys are accomplishing and just focus on my own work. I know I'm not the one buying the contractor's yacht.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ja44pl3] (score 209, diepte 0) Bro there’s days where you can put up 30’ and be successful, and days where 1000’ might be slow. We don’t have a fucking quota to hit so just do the best you can.
[ja478yg] (score 100, diepte 0) Trunk line in a large building down the main hallway, you can put up 1,000’ every 100’ you go with straight pipe. Can we all agree that pipe goes up quick when you don’t bend it?
[ja4khag] (score 58, diepte 2) If a stick is 10 ft and he put up 500 sticks, a stick a minute for 8-10 hours straight. And he did all that without a rack? I'm sure he did all the drilling for support with his huge dick at the same time too.
[ja45fgv] (score 56, diepte 2) No clue, don’t keep track of stuff like that. It doesn’t really matter anyway because every time you run pipe is gonna be a different situation. Could be a 6 tiered rack of 3/4emt, or underground 4” rigid. I focus on if I stayed busy or fucked off that day and that’s all im concerned with
[ja4aq58] (score 52, diepte 0) I had a guy like your mister 5000ft.  We were working together in the same project. Everything was up high off of lifts, and pipe was being installed in perling. 

I've made my lift efficient as possible with couplings connectors straps screws etc, all readily accessible.  And would install as much as I could oer reachable section, install straps, and move the lift/basket down 10-15ft.

And after a couple of days my foreman is wondering why I'm installing 25% of the conduit the other guy is.  And I watch him and he's in 1 spot putting on couplings, pushing it down the perling, add coupling push it down etc. No straps, conduits picking up debris as he's pushing them through, and I can see occasionally that they are not staying in order.

So I get petty and start initialing every box and coupling, which took like 20 minutes during break while smoking.

We start pulling wire and more often than not we cannot get a line or fish tape through without breaking apart fittings. Or they end up in the wrong box etc. And this guy tries blaming me because he's so much better because he got so much more done.

Until I told the foreman how all my shits labeled, and has had no issue pulling at all.

So now he not only has to go back and strap everything anyway. But every time we have to stop there are now 3-6 guys waiting every time a fitting has to be opened up.

So high numbers are a achievable if you don't give a shit if it's done right and you are leaving the pulling for someone else. But completing everything to spec, with no mistakes might take longer on some jobs than others.
[ja4bxk6] (score 50, diepte 1) Exactly. I’ve worked with commercial guys who do 300 feet a day but it all looks like garbage.
[ja4m2th] (score 48, diepte 2) Also 300' could be nothing if a rack is set up and it's all straight. 300' with bends and building a rack would be a completely different situation.
[ja48rd6] (score 44, diepte 1 OP) Yeah, that's an ideal run, especially if you have an apprentice do the rack part of it.

This guy tried telling me he did 5000ft without a rack. Meaning one run. And it was a straight run. I don't think he remembers how many feet are in a mile, or else this was the longest parking garage in existence :)
[ja44uea] (score 30, diepte 0) He is full of shit. 500 in a day is a fantastic rate.
[ja4shdf] (score 27, diepte 3) This is why I love electricians..math don’t lie my brother. People do.
[ja4ansq] (score 18, diepte 2) He’s just out right lying to you and gas lighting your achievements. I can’t stand how 80% of people at the job show up only for a competition. All the fancy clothes, and gear and stickers n shit. Fancy glasses. Fkn welder caps for no reason. It’s become a fashion contest and competition for most of these idiots. Practice your craft until you master every part of your technique and procedures for phases of the electrical build. 

I’d love to have this jacks ass say some dumb shit like this to me at the job. I’d embarrass the hell out of him with an audience. He’s claiming 50 bundles bro. Yea, maybe from the graybar delivery off the truck and on a fkn rack, sure. I’m an absolute beast and my record is 8 bundles in the air on a 10 hour day. Single run, red pipe. I don’t count 2 or 3 tier trunk lines down a hallway. You’ll put up 160’ per 10’ ya go with that shit. This dudes a fkn clown. He’s probably ass hurt cuz your eating pipe up like no one’s business.
[ja48z08] (score 18, diepte 0) 20' sticks of pvc in a trench.... a lot.
[ja4b1ns] (score 15, diepte 3) Amen. 100' rack with bends and obstacles in an exposed ceiling might be a ton one day.

&#x200B;

the next its a straight run above hardlid, 100' of that rack is slow partner. Get busy
[ja4mmpp] (score 15, diepte 1) Raceway is not installed if it isn't properly coupled, connected, supported, and secured. Throwing pipe up in the air isn't installing. I fucking hate working with guys like that. If it isn't 100%, ready for wire pull, and would pass any inspection, you aren't doing your foreman any favors by throwing up hundreds of feet a day. It's just more rework for the next guy coming behind you fixing your work, more likely than not having to redo lots of the pipe because you left no good plan on how to strap what you threw up.
[ja5jnhy] (score 15, diepte 0) I work ina hospital..30’ in 8 hours is my 1000’ a day lol
[ja45zhp] (score 14, diepte 3 OP) Good philosophy. Respect
[ja62564] (score 13, diepte 1) I worked for a company a few years ago that had just started implementing a “metrics tracking” policy. between teaching their entire workforce how to use these metrics, how to record them on paper each day, and deciding what a “good” or “bad” performance would actually mean for an employee on a day to day basis or over a few months or a year, it was definitely just a massive distraction at best and a huge detriment to morale when you ended up the poor crew running a bunch of larger conduit through some obstacle ridden area and didn’t put up 80’ an hour (minimum) like the standard expected of everyone regardless of circumstances.  

I’m glad I’m not there anymore and I’m not sure if they stuck with the system or not.
[ja4d6n9] (score 13, diepte 1) Must be a straight run with set screw couplings
[ja4co1t] (score 13, diepte 3) Stickers and welding caps made me laugh 😂. Some dudes are just dying to be iron workers.
[ja64mv1] (score 12, diepte 2) My experience is someone sold them on this tracking tool. Because they paid for it and a boss bought in. They have to use it for a while before it slowly dies.
[ja64g99] (score 11, diepte 1) Ain’t that the truth. I’ve had days where 2 sticks was an act of god due to trade conflicts, material shortages, etc….
[ja4avog] (score 11, diepte 0) It depends on where it's being installed and how many bends and the trade size of the conduit. Also whether it's in an area that has seismic requirements or not. 1000' is feasible for easy locations. I remember doing 700-800' of 3/4" (19mm) EMT per day off a scissor lift with a nice warehouse floor to travel on. That was screwing it to the Q-deck (hollow, not concrete filled). Straight sections were probably 40-50' and then a couple of bends at the device drops, but the bends were easy. Mostly 90 degrees, with some pull box offsets or simple kicks the depth of the Q-deck ribs when changing direction.

The only reason I remember how much I was installing is that I has this conversation with my foreman:

Me: "You need to order more 3/4" EMT."

Him: "I just got 3000 feet yesterday. You're the only one using it."

Me: "Yeah, I'm burning through it."

Him: "How much are you putting up per day?"

Me: "About 800 feet."

Him: "..."
[ja4jkki] (score 11, diepte 0) We use to hit an easy 1000’ when I first started in big stores/ warehouses. Back when you could run it on and in the cue decking. You could stay in the lift and slide in the deck from one spot. Get a couple hundred up in 30 minutes if it was a long straight shot. 

Then they made it code to get 1.25” off the deck for roofers. The strut/hangers/caddies take a lot longer.
[ja542yy] (score 10, diepte 1 OP) We supposedly had someone die from that a few years back. It was a plumber's job, but he was just chucking pipe down a rack until one went further than expected, blew out a window, and someone got cut in half 40 floors below by the window. So guys say at least.

Obviously not an issue on every job, but one more thing to be careful of if you're in that position to be chucking pipes down rack runs.
[ja4wibv] (score 9, diepte 2) That's bullshit. I've ran over 600' from a scissor lift but it was mostly straight once I got everything aligned, was bang-on Caddy clips to roof steel, and set-screw steel couplings. That was full-on humping it. Only way he could run that much would be throwing parallel PVC in a pre-dig ditch with someone else bringing him pipe.
[ja49g09] (score 9, diepte 1 OP) She said she laughed you out the room when she saw it was 0.1ft.
[ja5bvvv] (score 8, diepte 3) Agreed.. I did a rack with 75 ¾ and like 52 1 ¼
Needless to say I pretty much put up one or 2 supports a day and banged out a ton of footage.
[ja5vo2n] (score 8, diepte 4) My personal favorite is a guy that’s done nothing but mc and boxes for like a year….. still got a no dog clipped on his hard hat.
Probably doesn’t even know how to set up a table bender.
[ja6i6rh] (score 8, diepte 3) In his defense though, records are set on days where you work way more than 8-10 hours.
[ja45f3o] (score 7, diepte 1 OP) It used to be 500, he just 10x'd it, it's like the fish you caught that goes from 2ft to 20ft after a few years I think.
[ja4hexf] (score 7, diepte 0) I’ve ran through over 5000 feet of pipe in a day before too, it was for underground tho and was running a fuck ton of parallel feeders. Easy to rack up the numbers when it’s straight runs. But like everyone said, every day/job is different, sone days I put up 100 feet in a day and think I put in a good days work.
[ja7s955] (score 6, diepte 1) Me and 3 guys spent two weeks putting up about 30' a day.

4 Parallel 4" above grid ceiling in a school, a ton of offsets and  36"x 36" pull boxes as needed.  Any tiles/grid removed had to be back up at the end of the day (2nd shift) as school was in session during the day.
[ja56fr7] (score 6, diepte 2) PVC in a trench.  If it's already distributed ao all you do is glue it and drop it in you could do a couple thousand feet easly
[ja4i9ut] (score 6, diepte 1) Shoot I’ve put 2500 or so in a few hours with a 28 stack of 20’s.
[ja4d9b2] (score 6, diepte 0) You’ll get to a point where you don’t even hear clowns who bs like that. I can’t count how many dudes I worked with who brag about their production, then you actually work with them they are usually below average. The guys who are truly talented and efficient don’t have to brag on themselves.
[ja69zbh] (score 6, diepte 1) I’ve worked on a few hospital additions, it’s a fucking jungle up above those ceiling tiles.
[ja645bk] (score 5, diepte 2) Yea, it really varies on so many factors. If someone is bashing you instead of showing you how it's done they are a dick.

One time I told an apprentice to hurry up and find the short circuit and he mouthed off back to me. I told him to move and I would find it in less than a minute. I found and repaired it in 33 seconds. Another apprentice timed me. 

Moral of the story, show them you can do it, then teach them how.
[ja53o51] (score 5, diepte 4 OP) Yet drinking a gallon of lead and using a stick to hit yourself in the head with are a lot cheaper than all their swag. Could be ironworkers for far cheaper.
[ja6pqhj] (score 5, diepte 3) Hilti gun.   No drilling.   But that much is highly unlikely
[ja48whv] (score 5, diepte 0) Ask yo mom
[ja4oz6w] (score 5, diepte 2) She said 1.2 inches huh, well bless her heart.
[ja4p582] (score 5, diepte 1) I’m glad I’m not the only one that was like shit 10,000’ in a 20’ wide pit before lunch? You sick?
[ja5yu1s] (score 4, diepte 1) Yeah like right now I’m going room to room installing conduit for low voltage runs for the data guys (spec on this building).

I’m getting maybe… 4-5 runs done per day if I have zero other tasks, a run ranging from 10-30 feet. This is with fire caulking and I’ll often need to go through another room in each run to get to the cable tray in the hallway. It’s all not exposed so I’m not needed to be pinpoint perfect.

Tons of offsets, saddles, and a few junction boxes as well. 

I’m still an apprentice so I know I’m not the fastest. But I can’t even see how it’s possible to hit even 1000 in a day even if it was totally straight. So it’s good to hear this lol
[ja4awgf] (score 4, diepte 2) 5280’ bro………I measure miles of wire and pipe on every job I go. But, that’s the whole fkn job.
[ja4k0cc] (score 4, diepte 1) This would make sense for what the OP was about. Lmao. I had a really good day once when I was a third year and cleared a mile of 4" pvc with just myself in the trench and my foreman bringing me pipe, rebar and cards all day. Best I've ever come close to was a 1/4 mile of 1 inch, on prehung racks, all straight pipe, and there was 20 of them. That's more measuring spacing, tightening straps and it was compression couplings as well, than it was actually putting up or being pipe though.
[ja4qk5o] (score 4, diepte 0) 5000 feet is one stick every 57 seconds non stop for 8 hrs. You still gotta strap it, screw it down, put on couplings, and gather material
[ja5lkcj] (score 3, diepte 2) 1170', every stick was essentially a 4 point saddle.
[ja5zbn3] (score 3, diepte 2) Why should that be important to me? Does it come with extra pay or something to keep track?
[ja4hq4y] (score 3, diepte 0) Lots?

I’ve installed 1000’s some days and less than 30’ others. Footage doesn’t matter so much as getting it right the first time.
[ja4hu0a] (score 3, diepte 0) Moving 5k feet of pipe in a day maybe, running it? No. He probably came from a company that did directional boring and ran 5k feet with a ditch witch
[ja4jza5] (score 3, diepte 0) I’ve only worked 1 job where my pipe was in the 3000ft range. Walmart warehouse, 3 racks, 30 pipes on the rack total. Other than that, there’s days where 30 ft is a struggle.
[ja8je6g] (score 3, diepte 2) Yeah man, but if you can run pipe ina hospital you can run pipe ANYWHERE. It’s like working on expert mode at all time.
[ja842c9] (score 3, diepte 1) Legit man. I’ve had days where getting 2 sticks bent and snaked up into a busy ceiling was a major achievement lol. Jealous of new builds, remodels and additions can be rough.
[ja7jqva] (score 2, diepte 4) I wear a welders cap because it keeps my hair cleaner.
[ja8i9m4] (score 2, diepte 5) Also see many guys wear them to hide the fact that they have little to no hair.
[ja4apde] (score 2, diepte 0) Depends on what you mean. I’ve done probably a thousand in a half day. But that was pvc in the ground. Not emt, which is my guess where you’re getting at.
[ja7ltqf] (score 2, diepte 1) I think that’s what OP needs to start calling the guy, Mr 5000.
[ja4d6lm] (score 2, diepte 0) You have to think how much faster something goes with scale too. Like is he saying every stick counts so if you have a 30 pipe rack and you move 10 feet that day that you ran 300 feet? If so, someone doing a straight run of 20- 4" and then 15 smaller pipes on a scissor lift can put up 1000'. But no way someones putting up 5000' of even reasonably ok looking pipe. Maybe in a drop ceiling?
[ja4ir0v] (score 2, diepte 0) Just last week I ran 1200’ of 1” in 10 hours all the way across a warehouse for exhaust fans
The week before that I did 900 in 40 😅 it depends on the day and the task straight shots with 4point saddles easy money. More calculated bends take longer.
[ja550ag] (score 2, diepte 1 OP) I feel that last bit. We used to be able to run right off of ceiling grids on top, easy with caddy clips, but now it's all got to be off rod, and I've got a crick in my neck that makes looking straight up difficult.
[ja60z4a] (score 2, diepte 1) Yep, I’ve burned through a few thousand in a day like this. Working off a massive all terrain lift with multiple systems being run all together straight into the deck
[ja55ak6] (score 2, diepte 1 OP) Yeah that's a nice easy one there.

Even doing 1000' regularly strikes me as ridiculous. Those are rare occurrences, like yours.
[ja55rye] (score 2, diepte 0) About 1600ft is my record. Big rack. Working off a lift. I had already installed the strut supports, and it was a straight run. Measured the edge of the first strut strap, had a spacer for the rest. Slammed it in.
[ja56hu8] (score 2, diepte 0) I would say you’re fine with 250-300 feet. It really depends on what size and type you’re running. For example, my first company ran a lot of 3/4”, 1”, and 1-1/4” EMT. Going though a few bundles a day was pretty normal. The company I work for now runs a lot of 2-1/2”, 3”, and 4” IMC and RMC. Installing under 100’, sometimes even less that 50’, is very common.
[ja5hg9t] (score 2, diepte 0) I have done 2k in one eight hour period but only because we had probably 12-15 conduits being run the same route with the same bends from the same lift.  It was still a hell of an 8 hour show.
[ja646c0] (score 2, diepte 0) 10'
[ja6du0i] (score 2, diepte 1) Master bundle is 2000 feet, normal bundle is 100
[ja64h3g] (score 2, diepte 0) I love that you’re competative.  Feelin it.  Same here.

But I really doubt that.  I outwork everyone around me and with hangers, blah blah blah blah am at best 100 feet a day.

Do you just do straight runs or do you have help?

If it’s true, im super impressed
[ja6r078] (score 2, diepte 0) Not much. I'm an electrician not a plumber. :p

\#EUlife
[ja41z7f] (score 1, diepte 0) If you are *NOT* an electrical professional:

* **RULE 7:**

* DIY or self help posts **are Not allowed**. They belong here: /r/AskElectricians /r/askanelectrician /r/diy /r/homeowners /r/electrical.

* **IF YOUR POST FITS INTO THIS CATEGORY, REMOVE IT OR IT WILL BE REMOVED FOR YOU.**


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/electricians) if you have any questions or concerns.*
[ja64clu] (score 1, diepte 1) I agree...
[ja61qi3] (score 1, diepte 5) Lmao….here we go…let’s do this.  How about “clipboard tony”…the jackass apprentice holding the sign in morning meeting sheet during the Monday morning safety meeting?  Thinking he’s on his way to the top?
[ja7ayo4] (score 1, diepte 2) He’s full of shit or someone else put up all his supports, hangers or clamps
[ja64ke5] (score 1, diepte 1) Truth
[ja554um] (score 1, diepte 1 OP) It was a single pipe run without a rack in the ceiling with him shooting rods the whole way... He's a good bs'er that's for sure.
[ja54tnu] (score 1, diepte 1 OP) 120 does sound low though, unless that's including everyone doing panels, switchgear, material handling, whatever, from start to finish?

I've certainly had sub-150 days running pipe, but it usually leaves me a bit disappointed unless there was a clear reason (and there usually are).
[ja4hhno] (score 1, diepte 0) Like 80
(46 reacties met lagere score weggelaten)

=== THREAD 17crc22 ===
SUBREDDIT: r/AmazonFC
DATUM: 2023-10-21  SCORE: 46  REACTIES: 118
TITEL: Will my feet ever get better?
POST (source_id=post):
I just hit 3 months of working at amazon in picking. I do 4 10s. The first week was HELL for my feet. I could barely walk by the time I was out. 

For the 3 months I’ve been here I have not worked a 40 hour week. It ranges from 30-38 hours. I am always using PTO or UPT to leave early or take a longer break. My feet still aren’t used to it. I have great insoles, I soak my feet in epsom salt and warm water when I get home from work. It’s horrible. Will they ever get better? How can I handle the pain and push through the whole shift?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k5rzyyq] (score 56, diepte 0) Been here 8 years, define “better” 

Eventually you just get used to the pain
[k5rxveo] (score 35, diepte 0) Make sure your shoes are not tight or too loose. If you can feel the sides of your shoes with your feet you need to size up. Drink lots of water
[k5rwnl6] (score 26, diepte 0) Short answer : yes . Long answer. Your doing everything right. Keep doing epson salt, consider compression socks. Maybe get a foot roller. At 3 months , You are right there. Pain will start to diminish. Not go away, but tolerance. Also , what type or shoes are you wearing ? Maybe you need more ankle support. Speaking for myself. Sneakers sucked. I needed boots to give my ankles more structure which was the cause of a lot of foot pain.
[k5s3mob] (score 17, diepte 0) Maybe new shoes and a Tylenol. That’s what I do and I’m fine and I’ve been doing 12s.
[k5s4mwm] (score 17, diepte 0) You really might need a different pair of shoes. I highly suggest the skechers with the memory foam. it changed my entire day.
[k5s3upa] (score 15, diepte 1) Yes boots are so much better for me. Go for wedge soled boots, wool socks, and compression socks.
[k5spwyc] (score 13, diepte 1) Yup going on 4 years here, took about 2 years.
[k5s6t85] (score 11, diepte 0) I use 8" boots for the ankle support. 
I'd occasionally get blisters on my toes while breaking my timberlands in, so I'd wrap the sores with blister tape and gauze.
I recommend lidocaine spray or cream for the pain, and gauze wrap with antibiotic ointment for the sores. 
Keep your feet dry with foot powder to prevent bacterial growth.

The timberland pro insoles are really cushioned and thick, they've been my favorite.

Yes it gets better, it was a matter of breaking my shoes in, as well as skin callus thickening.
[k5sdrdp] (score 9, diepte 0) I always suggest at least 2 pairs of shoes. Giving a pair of shoes 24 hours off between shifts does wonders for your feet and the shoes last way longer. I learned this working in restaurants. 

When I go to 12 hour shifts for peak, I will be switching shoes at lunchtime. Thanks to Amazon buying me a pair of shoes every year and the shoes lasting longer. I am now up to 4 pairs. I do think one of them is ready to be retired, though. 😥

Also, try to put your feet up above your head for 20 to 30 minutes each evening. I tend to lay on the floor with my legs laying up against the wall. I was actually really shocked at how much this helped me when I tried it.
[k5sk5m6] (score 7, diepte 0) Yes it does, but if you're in this situation after three months, then something is really wrong with the shoes you're wearing. For reference, it only took me 2 weeks to adjust to the hard warehouse floor and for my foot pain to go away. It's normal to have minor pain in your feet after working 10 hours, but not to the point where it's unbearable, like in your situation. I'd definitely recommend trying out different satey shoes, like ones from New Balance that have wide sizes for more room for your toes, and provide great support and comfort. It sounds like your safety shoes are incompatible with your feet, so don't ignore the problem. Also, get lightweight safety shoes that look more like sneakers and have a composite toe rather than steel toe. The lighter your safety shoes, the better for you while working. Do not get heavy ass work boots that weigh you down, especially if you walk a lot. Hope this helps!
[k5sr2rp] (score 7, diepte 0) Thicker socks. I got some wool socks at Costco recently. Not too thick but enough, also offer arch support and compression. 

Ibuprofen right before I head into work. 

Lotion after work and really do slow, firm strokes where it hurts. Those mini massages help.
[k5sx0v1] (score 7, diepte 0) You may be developing plantar fasciitis. Get some compression socks, a massage ball for your feet, biofreeze and do foot strengthening exercises and stretching everyday
[k5se1pf] (score 6, diepte 0) About one more month or so and you'll no pain. Make sure to  use a stair machine and or cardio on the weekend this will strengthen you
[k5sg4gy] (score 5, diepte 0) Use composite toes instead of steel toes , buy compression sock and roll your feet on a frozen water bottle for 3 mins each side ,helps me alot
[k5sb4ho] (score 4, diepte 1) Same. I got boots, and the ankle support was game changing.
[k5sctsg] (score 4, diepte 1) Compression socks help a lot. I also ice my feet.
[k5ta7mz] (score 4, diepte 1) Compression socks are the way. They keep your feet from swelling up inside your shoes and keep that blood pumping through your legs.  I have not had pain in my feet since adding in the compression socks.  (Also, I've tried a ton of the insoles, and the expensive superfeet are not my favorite.  The Timbaland pro anti-fatigue insoles are where it's at.  And as a long-time hater of reebok, they make some of the best zappos composite toe sneakers.)

 As a former fitness instructor, and a female in pretty decent shape, my coworkers started making fun of my compression socks bc I'm always in spandex shorts and tanks with giant socks and work shoes.  I doubled down with fun designs.  Now other people have started asking about it and we are building a compression army!
[k5sbvo6] (score 4, diepte 0) my feet are numb so i dont feel any pain
[k5sfr14] (score 4, diepte 0) As with the being a second pair of shoes also bring a change of socks to change out during lunch it makes a world of difference. It helped me during the last half
[k5sqxss] (score 3, diepte 3) You should really consider wearing a compression sock anyway. 10 hours on your feet is too long and not healthy.
[k5swhpb] (score 3, diepte 1) Foot roller is soooo helpful I had bad pain on my foot and I could barely put any pressure on it so I decided to use a foot roller and it helped out a ton
[k5u1tbc] (score 3, diepte 2) Yep compression socks are a must I wear them too & also prevents from getting ugly spider veins..
[k5v9s0v] (score 3, diepte 1) This is what helped me. most people just tighten them suckers down. I tighten till the shoe barley hugs my feet then tie off and pain went away
[k5tpvb0] (score 3, diepte 1) Lidocaine
[k5v2h7i] (score 3, diepte 1) 7 in March. I just got diagnosed with plantar fasciitis. And I recently found out I have slight arthritis in my lower back. 

I'm 29.
[k5t9ijs] (score 3, diepte 1) Is it from zappos? Exact name of them? I need a back up plan for when they ban these cheap "do the best" safety shoes lol
[k5vh6b3] (score 3, diepte 2) Someone lost their toes to those
[k5s4qtd] (score 3, diepte 0) I do feel the pain, but I let it pass like they are there for work.
[k5sb48m] (score 3, diepte 0) I got plantar fasciitis from working at Amazon so sometimes it does get worse. But it’s gone now, but yeah you definitely will want good insoles for this job.
[k5t1mql] (score 3, diepte 0) I use socks that are not too tight, and they do wonders. My feet don't hurt at all what hurts, though is my lower back for standing a lot, lol. I do go to the break room once in a while to sit.
[k5vtqy2] (score 3, diepte 0) SUPERFEET OR POWERSTEP INSOLES.

SUPERFEET IF YOU'RE ON THE HEAVY SIDE.
POWERSTEP INSOLES PROVIDE A LITTLE MORE CUSHION.

IF YOUR ANKLES HURT, YOU NEED BOOTS THAT PROVIDE 6-8 INCHES OF ANKLE SUPPORT + INSOLES.


MY FEET ARE VERY PICKY WITH SHOES AND I'M OVER 200LBS, A GOOD PAIR OF CHEAP BOOTS THAT PROVIDE GREAT ANKLE SUPPORT ARE Interceptor "Force" boots. SOLD AT WALMART. 

THEY'RE UNDER $40.
[k5sf2h7] (score 2, diepte 2) I just wear two pairs of socks with soft insoles , gets the job done and feet don’t hurt
[k5tla6j] (score 2, diepte 1) I love boots, but with the safety toe, they are so heavy in Pick. But I also have a bad knee and already have to 'tell' it to lift twice as high with regular shoes to get it high enough to clear the step. No insurance atm so I personally can't afford to go get an accommodation just yet .
[k5xo02d] (score 2, diepte 3) I put it on religiously but you will be dependent on it if you don’t use other methods and you don’t want to be deep because the bottles run super small. Because I have plantar fasciitis I use a mix of lidocaine, padded support band and 2 insoles per shoe. I also use it to numb other areas that hurt ie. Knees, hands, wrists.

I think each person has to find their method bulk . It’s a learning process for foot pain relief.
[k5vwmss] (score 2, diepte 5) You're mistaken. The issue wasn't that they weren't purchased from zappos. The issue was the safety certification, the dothebest shoes don't meet the ASTM F2413 safety standard.
[k5t9paf] (score 2, diepte 1) Man, I miss the simplicity of just having to wear slip-resisitant shoes in the food industry. I personally never had to worry about foot pain since we didn't have to wear steel/composite toe shoes
[k5tnar1] (score 2, diepte 1) 12 hour shifts from peak? You folks really are still under this idea the economy isn’t in shambles this year eh?
[k5txcew] (score 2, diepte 2) I don't pick the hours. That's OPs job. We got a real nasty one right now. If we work 11 hours, we get a 3rd paid break. If we get that 3rd break, that OPs manager is going to make us "work for it" by making us work 12 hours.
[k5spu2k] (score 2, diepte 0) Give it a year or 2.....
[k5tqze2] (score 2, diepte 1) And lidocaine numbing cream. It feels like I’m spamming the thread but you guys have to know because it is a blessing because it doesn’t get better for everyone . It’s used by people that wear heels for extended time and can be used to numb other body parts in pain
[k5symiv] (score 2, diepte 0) I wear double socks. The first layer is a thin compression type sock with lots of arch support and the outer layer is a thick workboot type sock that provides a lot of cushion. Loosen the laces on your safety shoes to make room and you should be able to make it. Also Aleve helped me for a while.
[k5tdnnw] (score 2, diepte 0) 3 years of doing picking (actually walking to retrieve the items) and my feet still bother me from time to time. You just kind of get used to it. Also, the Reebok Fusion Flexweave are the shoes that don’t hurt my feet. I went through about 5 pairs of safety shoes finding some that actually worked. Get them a bag size up to allow room .
[k5tiliu] (score 2, diepte 0) Doesn’t sound like great insoles if you’re still in that much pain. Could also be a posture problem, your feet are too wide for your shoes, not using anti-fatigue floor mats when you can, etc.
[k5tpwfz] (score 2, diepte 0) Lidocaine
[k5ub0fv] (score 2, diepte 0) If you don’t want to feel any pain try heroin
[k5rux6t] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[k5ur5ip] (score 1, diepte 4) Second this..standing essentially in 1 place for 10 hrs has my calves full of spider veins...sooo attractive.
Sincerely wish I heeded Dr advice to wear compression socks...
[k5tdbj7] (score 1, diepte 1) Boots or the hoss basketball shoes on zappos are the best compared to all the regular shoes on there
[k5tvott] (score 1, diepte 2) have to go with composite toe
[k5u371f] (score 1, diepte 3) Those are heavier than steel toe to me
[k5w8g0f] (score 1, diepte 4) it's a fact that composite toe shoes are lighter
[k5wl9zt] (score 1, diepte 5) You can say that all you like, but my feet tell me a different story. Perhaps bc steel toe actually fit like they should and composite dont.
[k68564s] (score 1, diepte 7) You don't know how many brands I've tried. Happens when one of your family members was a shoe store manager for years.
[k5upxvf] (score 1, diepte 3) ... I didn't say that I wore boots. I said that I love boots. I wear reeboks. I'm not 100% dumb like many people I work with.
[k5urehg] (score 1, diepte 2) You don't have insurance yet? I thought everyone got insurance from "day 1"
[k5v08ax] (score 1, diepte 3) Seasonal atm.
[k5tq4zc] (score 1, diepte 1) Lidocaine (numbing cream) will save your life, my friend.
[k5vgs7c] (score 1, diepte 1) Yep. My shoes were way too tight. I had to loosen those bitches.
[k5um1cs] (score 1, diepte 2) This shit relieved the pain for a few seconds and then felt worse than before I put it on.  At least for me, anyway.
[k5y3o41] (score 1, diepte 4) Good points, I didn’t think about using it on other areas.
[k5tqc4h] (score 1, diepte 2) Filter skecher in the section that shows approved shoes
[k5ux3ja] (score 1, diepte 2) I have had a couple pairs of Skechers Uno's, and I will keep buying them for work.

And yes, Zappos. If you wear something NOT from zappos.com/amazon and you get injured, you are gonna be the blame. Do it to protect your ass in all regards.

P.S. those do the best shoes got somebody's toes chopped off. Throw that shit away, lol
[k5v1yiv] (score 1, diepte 3) Wth lol, how the hell did their toes get chopped off? What fell on them? I work in pack.
[k5vho5c] (score 1, diepte 4) Idk but there's a few threads about it. Here's one:
https://www.reddit.com/r/AmazonFC/s/Qusj6YibJr
[k5w2fv8] (score 1, diepte 6) But all the shit from zappos does. So technically, even though I didn't say that was the problem, that was part of the problem. If you buy your shit from zappos at work, you don't have to worry about it.
[k5vh12c] (score 1, diepte 1) I got those shoes with "do the best" on them. They're comfortable now that they're broken in and I have good insoles. It's a pain in the ass though because they always set off the metal detectors. :/
[k5wulcw] (score 1, diepte 3) Wow... Just what I needed to hear. Ty.
[k5t9ltb] (score 1, diepte 1) I keep hearing of this "plantar fascitis". How do you know for sure when you have this ? I had excruciating foot pain for the first week, then second week I bought the cheap shoes everyone wears and no more foot pain.
[k5trl2g] (score 1, diepte 2) There’s an online test for it I believe (if you don’t have time for a podiatrist ) to test where your pain is in your foot to determine but lidocaine is a good staller
[k5scha5] (score 1, diepte 0) Definitely different pair of shoes if all of those things aren’t helping enough, you actually get 2 free pairs per year so if you log back onto Zappos you should be able to get a 2bd pair
[k5t4mxp] (score 1, diepte 1) How? Where do I find the code?
[k5usno9] (score 1, diepte 1) Yes great advice...also I do Hatha yoga for at least  30 min b4 shift and 1-2 hrs on off days.. .idk how much it helps but I know it is better than the lame stretching they do in stand-up. Esp when most people aren't even stretching properly. Also a few mins b4 and midshift aren't sufficient.  Stretching needs to be done intermittently throughout shift. And not that pathetic 30 sec break during pick where they ask if u want mental or physical break..like anything really productive can be done in 30 sec...
[k5tqla2] (score 1, diepte 1) Some people have undiagnosed plantar fasciitis which makes it difficult but numbing cream would help ease the agony
[k5ujtkf] (score 1, diepte 2) She could have that problem, but from my experience it's usually the safety shoes that are the number one culprit. I am assuming that once OP gets out of work and puts on regular sneakers like most of us, her foot pain goes away right? The fact that OP is going to such lengths to escape foot pain, I doubt lidocaine will help, but she can try it. I'd still recommend her trying out different sneaker-like safety shoes though, it can't hurt.
[k5sofa7] (score 1, diepte 0) The only issue I have is callus on the heels of my foot. I try to soak my foot in epsom salt every other day. I’m still trying to find something more effective though.
[k5u3ez0] (score 1, diepte 2) I’ve tried that, Tiger balm, and pomada dragon. Didn’t really notice a difference. Tiger balm probably helped the most but that smell…
[k5srvr4] (score 1, diepte 0) Highly suggest compression socks and trying different insoles or even shoes. Even if you have good ones, they may not be fully supporting you the way you need.
[k5st0i1] (score 1, diepte 0) Ibprofen
[k5su3ir] (score 1, diepte 0) It helps if you just shove your feet through the concrete up to the ankles and drag them around like sand.
[k5tr3sg] (score 1, diepte 1) I also have plantar fasciitis but I use lidocaine instead of biofreeze
(41 reacties met lagere score weggelaten)

=== THREAD vfj5jb ===
SUBREDDIT: r/AmazonFC
DATUM: 2022-06-19  SCORE: 92  REACTIES: 117
TITEL: Feet painn
POST (source_id=post):
I would honestly genuinely enjoy coming to work my 10 hour shifts if my feet didn't hurt as bad as they do, that is the only thing that ruins my entire day.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[icw5h2j] (score 67, diepte 0) Been working at Amazon for 2 years now, it doesn’t get any better you just learn to ignore the pain better.
[icw5up2] (score 45, diepte 0) A few pairs of shoes that you rotate throughout the week, gel shoe inserts, extra cushion socks. I bought my Zappos pair of composite toed shoes and a few pairs of safety shoes from Walmart. 

I have a tennis ball that I roll underneath my feet after work for about 5 - 10 minutes & a foot massager bath that I use in the middle of my work week. They help.
[icwb873] (score 23, diepte 1 OP) Oh wonderful
[icw9z3v] (score 21, diepte 0) ^ I second all of that. The pain lessens a bit but it’s still going to be there every day. It’s all about giving your feet TLC after work/on days off.
[icwbssi] (score 13, diepte 2) First I cut out sodium and the pain in my knees and feet went away . Then I cut back in sugar like soda and Red Bull and candy all the fun stuff. Then it went away after a few days. I did start drinking a lot more water. It worked for me.
[icwixe3] (score 12, diepte 1) I actually had to make my own custom safety shoes because my feet hurt so bad. Took a pair of cheap safety shoes, cut them open, took out the steel toe, and stuffed them into a pair of Vans. Sooo much better 🤣
[icwabfx] (score 11, diepte 0) Been working for 4 months and I got use to the pain after 3 weeks of working there, now my feet don’t hurt anymore
[icyiu75] (score 10, diepte 1) Adding your original comment, you should always replace the insoles on shoes since it is usually the thing manufacturers cheap out on. And instead of just using a tennis ball, use a frozen water bottle since the cold helps with pain and it numbs your feet a little.
[icwadrx] (score 10, diepte 0) I just started two weeks ago and I am in agony every single day. Working 1 more day tomorrow and it's the 4th work day of the week so I'll be off after and man it is probably going to be Hell. I will buy gel insoles today and hope for good change. The Dr. Scholls Heavy Duty insoles have not helped. :/
[icwim7d] (score 10, diepte 0) yes and its much worse with these safety shoes. with my shoes before my feet NEVER hurt. now its worse.
[icy8d25] (score 9, diepte 2) But on the plus note your feet has this numbing feel that it doesn’t bother you as much. Especially once you fully break in your shoes. One thing I’ve learned with the composite toe shoes is to not tie them too tight have them on looser and I don’t have as much of a problem.
[icwb02p] (score 7, diepte 1) Same here
[icwstgj] (score 7, diepte 0) Every 2-3 weeks I get a foot massage done and do some at home in between. Soaking my feet with Epsom salt and then massaging it really helped me! I’ve also been hitting the gym a lot more so it could be my feet are getting used to it.
[icwvqkl] (score 6, diepte 0) I really enjoyed my hokas before they made us wear safety shoes
[icx34a7] (score 5, diepte 1) I’m generally on my feet for about 13 hours (RT and have to be in early/late) It does get better from when you first start. I could barely walk my first few weeks after. Years in and there’s som mild pain some nights but mostly just an ache when you get home. I use comfortable boots but no inserts. Definitely doable but it’s rough at first.
[icwbd9x] (score 5, diepte 1 OP) I think I just need to adjust to it again, I'm trying to not give up on myself lol I think after a paycheck ill be remotivated.
[icwbh9f] (score 5, diepte 2) Tbh  all you can do is try to get your feet comfortable,
[icwad04] (score 5, diepte 0) You might want to change your diet. My feet hurt after 10hr shift. After I changed my diet there was no pain at all.
[icwbqsf] (score 5, diepte 1 OP) If you end up buying the gel ones, let me know how they work for you! I was looking into getting some. I saw some reviews saying the dr scholls men's insoles are better so I might get those.
[icwctmo] (score 5, diepte 0) doc martens safety shoes!!! my feet used to hurt every day coming home from work but now literally never after buying the docs
[icxinkv] (score 4, diepte 1) When I worked at an FC I did four 10 hour shifts walking around the whole time scanning. I was used to it after about a month. Now I work at a sort center standing in one spot doing customer returns. I’m blessed lol
[icx433s] (score 4, diepte 4) Have you never had a nice beef stew with carrot and celery? Or an onion and squash off the grill? Deicious
[icwfu35] (score 4, diepte 0) Get some new insoles and I swear by this next tip: take a big bowl of ice water and repeatedly dip ur feet in it. Only until it is uncomfortable. Then bring ur feet out and allow them to become comfortable again, and then again, dip ur feet. Do this several times after u get home from work and take anti inflammatory medication(if ur dr allows, and it’s safe). It REALLY REALLY helps
[icygl8l] (score 4, diepte 5) What safety? We have people running around not wearing safety shoes at all in my facility. 😂
[icy8gh8] (score 3, diepte 2) I can’t imagine 13 hour shifts like 10 hours are hard enough.
[icxiddz] (score 3, diepte 3) Heavy duty is good for walking. The athletic ones are better for picking/quick movements.
[icwcino] (score 3, diepte 2) I remember someone telling me that they would take over the counter pain relief and it kind of worked but mainly trimming there toe nails helped a lot because if it’s even slightly long it can cause your toes and entire foot to hurt too but try those just incase one of those is the problem
[icxf7ci] (score 3, diepte 4) That is not allowed and safety will fire you for that
[icx6nbu] (score 3, diepte 0) Use the safety toe caps with a comfortable pair of normal shoes
[icxua2g] (score 3, diepte 0) There is a trick… bring another set of shoes, and halfway through shift, switch them. Your feet will feel better again.
[icymedh] (score 2, diepte 2) I thought 12 hours was the maximum permitted
[id03z17] (score 2, diepte 3) 12 hours on the clock. If you work off or are salaried it doesn’t matter. Many of our Ops and up work 15ish hour days
[icwl1sl] (score 2, diepte 3) The pain didn't go away, your body is just depressed now and it's a deeper/stronger pain so you stopped feeling your normal pains!

 #VegetablesTasteLikeSadness
[id0rsfi] (score 2, diepte 1) Yeah, the Heavy Duty by Dr. Scholls did not work out for me either.  The heel area worked ok, but not so for the balls of my feet...
[icwprr9] (score 2, diepte 3) Yoooo toenail maintenance is very real lol it’s so true, keep ‘em trimmed short or they’ll mess your whole foot up
[id9dh44] (score 2, diepte 7) Seriously. I'd love to follow suit, but I know my luck, and the moment I don't wear my safety shoes, they'll crack down and I'll get written up.
[icxy8cs] (score 2, diepte 2) There's actually steel toe inserts that are sold on Amazon.
[icwoicv] (score 2, diepte 0) Memory foam insoles or insoles with gel work wonders for me. A good pair will keep my feet comfy till near the end of shift.
[icww1iq] (score 2, diepte 0) This is why we need chairs at our stations. We arent mules!!!
[icwz2oe] (score 2, diepte 0) Double sock, and use aspercream foot lotion, and then soak your feet in epsom salt after your shift, it’ll change your life
[icxd8v0] (score 2, diepte 0) I had the same issue a few months wearing work shoes, but if your FC/Sort Center has turbo toes try them! I used to have a hard time just getting past a 5hr shift and now I can do that easily as well as the 10hr shifts. They look funky, but boy do they make my feet feel so much better.
[icxmi0e] (score 2, diepte 1) I have plantar fasciitis as well and am trying something this week that seems to be working. I bought a pair of Superfeet Green insoles as well as a couple of plantar fasciitis night splints that I put on for an hour or so after work and longer on days off. I also have a shiatsu foot massager that I use before going into work. And finally I take 400mg ibuprofen around 1st break and 400mg more at lunch. This is only my first week doing all of this, the first day was a little rough but I want to say day by day it's getting a little better. Hope some part of that is useful.
[icxigtn] (score 2, diepte 0) O Keefes healing foot cream also does wonders if you put it on overnight. Really helps heal your feet. Noticed a good difference when I started using it.
[iczgx6c] (score 2, diepte 1) That's exactly what I do,it works too
[icw4839] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[icydal7] (score 1, diepte 2) That paycheck is good for making you forget about the pain.
[icwbhi5] (score 1, diepte 1 OP) What kinds of changes did you make? I have a bad habit of not eating much on my work days which is probably not the best.
[icwlh3s] (score 1, diepte 4) Vegetables are fucking delicious. Steam broccoli , cooked carrots or even regular carrots . So many types of vegetables are delicious but you were probably brainwashed as a kid to believe they aren't.
[icxv6mv] (score 1, diepte 5) Guys chill it was a joke 😂 ya'll take shit too seriously. Who doesn't love vegetables? I'm half vegan
[icwsfvd] (score 1, diepte 2) I got Dr Scholls gel insoles today for eleven bucks. No idea what to expect. I'll let you know if I can remember to but generally try to experiment and buy different ones to see which are best for your feet in particular - I had the Dr Scholls recommended and went for heavy duty and they didn't help
[icyg1fh] (score 1, diepte 2) Got gel ones with built in arch support.  If you are picking or walking a bunch a change of shoes or inserts mid day can sometimes help
[id1hwu2] (score 1, diepte 2) Gel ones didn't seem to make too much a difference but they were decent. Not sure yet. I bought very thin gel ones from Dr. Scholls. Going to try thicker gel ones from a different brand soon perhaps
[icyxtvt] (score 1, diepte 1) Get superfeet insoles gel insoles are a gimmick your feet need support not a couch
[idc5hh1] (score 1, diepte 2) On the other hand, having great initial success with these:  https://a.co/e3XyTE2

Feet still tired, but HUGE reduction in pain.  Thick socks, so the shoes need to wear loose, one way or another:  laces or sizing.  & I replaced the insoles with MegaComfort Personal Antifatigue Mat insoles (probably not the best, but well reviewed & better than what Timberland put in my previous pair--I didn't even try these Timberland insoles yet...).
[idc5u6t] (score 1, diepte 3) Apparently, laundry softener a strong recommendation to keep the socks "working" best, along with washing them inside out.

Also. The MegaComfort PAM insoles showing very early signs of the foam separating from the fabric layer facing the sole of my right (dominant) foot.  Makes me really wonder about their durability--but, they still feel significantly better than every other insole set I tried so far!
[icwsn41] (score 1, diepte 2) You might be onto something….. I’m going to give this a try thanks for the advice 🥹😭
[icwufcz] (score 1, diepte 3) I’d suggest getting a size smaller of the safety shoes, that way the inserts will fit better into the shoes you intend to put them into. I managed to find a pair of cheap safety shoes for like $27 on google, and it was worth every penny lol.
[icycm89] (score 1, diepte 7) I went lvl1 to level 4 in less than 5 months
[icyke1e] (score 1, diepte 8) How? Did you have previous experience?
[icyl55k] (score 1, diepte 9) I have a degree, but no previous experience with Amazon
[icygbf3] (score 1, diepte 5) I’ve already spoken to safety. They didn’t care.
[id051wk] (score 1, diepte 6) Yea safety at ours said it was ok until people in suits came to visit 😊 no longer allowed
[id2qpx2] (score 1, diepte 7) People in suits, huh?
[id8wo8v] (score 1, diepte 6) Seriously.
[icxnk2i] (score 1, diepte 4) Smaller? I sized up a half size so that the insoles would fit. Sizing down will likely hurt the feet more
[icyh373] (score 1, diepte 5) Sorry, I meant to say half a size smaller. And the reason I said this is because the steel toes are actually quite thick, and I had a bit of trouble actually getting it to fit inside the shoe. Worked out in the end though. Found a video on YouTube that I followed when I made mine. Just used a pair of vans instead of Nikes. 


 [How to make your own steel toe Nikes](https://youtu.be/JIDm37_Pwc0)
[id3bimv] (score 1, diepte 3) Link?
[icwvp1p] (score 1, diepte 0) It’s that and my lower back
[icx4daj] (score 1, diepte 0) Stay away from inflammatory foods. Things like sugar and dairy cause your joints to swell. Your diet doesn’t have to be clean. Just eat whole foods that are free of “natural flavors” and enriched flour.
[icxb27o] (score 1, diepte 0) I been here 5 months and the foot pain I felt when I started compared to now is night and day. It still aches but its so much more tolerable
[icxb8k5] (score 1, diepte 0) Spenco supports
[icxcgo1] (score 1, diepte 0) That and having to use the stairs due to elevators malfunctioning. Both my legs and my feet feel like snapping after every shift now.
[icxdqxa] (score 1, diepte 0) I'm in agony with Plantar fasciitis after working with safety shoes, the shoes themselves were comfy but the soles are hard and I have flat feet, this problem havent gone away since leaving the dept and is actually getting worse no matter what I do, I use K-tape now to hp support them but 🤷🏻‍♀️
[icxw448] (score 1, diepte 0) I bought a pair of these and wear them with my brooks. My facility doesn’t seem to care and at least so far I don’t regret my purchase (have only used them a couple times so far). https://a.co/d/hOzhOgU
[icxwbie] (score 1, diepte 0) You should see what my safety shoes did to my feet before I broke them in 😩
[icy2e07] (score 1, diepte 0) My feet were in constant pain when first starting. Tried gel inserts and every other insert until i found Dr. Scholls walking on air memory foam. I also do a lot after work. First, every single day soak my feet in hot as you can stand water for 15-30 minutes until your feet just start to wrinkle, pumice stone every 2-3days,, add epsom salt every 2-3 days, and immediately after any soak, put an ice pack on for 15 minutes per side repeat ice pack on each side several times, then i put on Flexitol Heel Balm or any other super concentrated moisturizer and massage, apply it again before bed, wear socks to bed, wash in the morning and apply Ban roll on antiperspirant for the sweat. Now my feet only start hurting in about the last hour or 2 of working. Its a lot but so worth it!
[icy46t8] (score 1, diepte 1) Also found a nice trick no one ever taught me, i just thought about it one day lol.  When choosing your shoes BEFORE even try them on, take out the shoes original insert and step onto that. I noticed that even the comfy regular sketchers i used to buy, my pinky toe bunion hung over the side so i was actually making my bunion worse, got the wide fit and tried that and it fits perfectly and feels even better!
[icy5jov] (score 1, diepte 2) One last thing lol! I'm going to be applying this when my custom fit orthotics arrive from the foot doctor. I found a video from a kinesiologist on youtube i can't remember which but it makes total sense!  Only use your orthotic when you feel the pain and swap it out for the original or even better, memory foam insert. When you wear an orthotic, you become dependent on it just like a drug, its just alleviating the symptoms and building up your foot muscle so that you HAVE to wear it to feel relief. Anyway, just my 3 cents ![gif](emote|free_emotes_pack|joy) Hope it helps! ![gif](emote|free_emotes_pack|thumbs_up)
[icy8pt5] (score 1, diepte 0) Roll a frozen water bottle over your feet after every shift. I have severe arthritis in my feet- it does help
[icy8tpk] (score 1, diepte 0) My last job caused me intense foot pain. The bottoms of my feet were all bruised up. I got [some of these insoles](https://fpinsoles.com/), and they helped tremendously. I saw them in a Facebook ad, so I was apprehensive to try them. In the end, I'm glad I did because these insoles have been life savers.
(35 reacties met lagere score weggelaten)

