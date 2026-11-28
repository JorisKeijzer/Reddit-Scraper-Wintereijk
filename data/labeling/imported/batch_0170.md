# Label-batch batch_0170

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
Schrijf het resultaat naar `batch_0170.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(5 threads: 15ob6ne, 1hqgf1n, 1cpddub, sz7kpx, sk0ni3).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 15ob6ne ===
SUBREDDIT: r/Chefit
DATUM: 2023-08-11  SCORE: 17  REACTIES: 58
TITEL: I have gross sweaty smelly feet and need new shoes.
POST (source_id=post):
So I looked through old posts and didn't find anything specific for this issue. I've had birkenstock clogs for like 8 years and they've finally worn out. 

I love them but I have bad sweaty feet and they got rank by the end of shift. They have zero air flow outside of taking them off.

I'm also teaching culinary now, so I really only need something non slip, but would prefer some protection from spills and shit falling on my feet. 

Cost not an issue if they will last a year or two. 

Suggestions?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jvqpbhn] (score 20, diepte 0) Listen, buy more than one pair of the same comfortable shoe. After wearing a pair for one day, give them two days to dry/air out. Get shoes that breathe and wear socks. Hell, take extra socks if you work long shifts. 

Once a week, take a soak if not your body too, at least soak your feet in a small tub with a capful of bleach. 1/3 Cup of you are filling a tub for about 30 minutes. Dry yourself and maybe use foot powder.
[jvr7qld] (score 7, diepte 0) So, I thought I had to just live with my super smelly feet, like oh well, just my lot in life. I got a real bad infection after I broke my leg and they put me on really intense antibiotics and it had the unintended side effect of getting rid of the foot smell! I mean, my feet don’t smell like roses after a 10 hour shift, but before it was like raw sewage. Apparently I had a fungal infection.
[jvs2b8d] (score 6, diepte 1 OP) They make ones specifically for chefs.
[jvrha82] (score 5, diepte 1) Get a boot dryer and store your shoes on them. Sounds odd for Birkenstocks, but it helps a LOT. 

Highly recommend a Peet Dryer
[jvrkb9h] (score 5, diepte 1) Wool, not cotton. Wool.
[jvru7t0] (score 5, diepte 0) Not a chef but used to cook at a shitty restaurant. Y'all are wearing Birkenstock clogs in the kitchen? I feel like I would slip and bust my ass in about 30 seconds.
[jvsincw] (score 5, diepte 0) Get rid of performance socks and find the closest to 100% cotton socks.  Your feet will thank you.  I've been wearing Birks for 20 plus years with no issues.  Ditched the wicking socks or performance socks and now a non issue.
[jvtmtk5] (score 4, diepte 1) Soak my feet in bleach? Am I reading this correctly?
[jvsbss5] (score 3, diepte 3) Also, your problem is probably shitty socks more than anything. [These MFs changed my life](https://www.bonds.com.au/explorer-original-wool-crew-3-pack-black-synw3w-blk.html)

But I prefer the merrell pro Mocs. Fucking excellent shoe
[jvuxiii] (score 3, diepte 3) Epson salt will work just as well and it isn’t toxic.
[jvr2wrw] (score 3, diepte 0) I had a pair of red wings non slips that lasted me 5 years, they were great. Waited to long to replace them and couldn't wait so I have something else now, but the only issues I ever had with them were day 1 breaking them in, and one hell week where it wouldn't have mattered what shoes I was wearing, my feet would have hurt.
[jvrfosy] (score 3, diepte 0) I get the same issue. Get yourself some antiperspirant for your feet for when athletes foot flares up and spray for your shoes
[jvs4bpc] (score 3, diepte 2) Wow that interesting. So non slip etc? TIL. thanks
[jvs5fqk] (score 3, diepte 3 OP) Yeah, they are super nice. The soles are made of cork and you can replace them every few months. Mine FINALLY gave out where your foot meets your toes, where they bend.
[jvrzuqs] (score 3, diepte 0) I used to wear Birkis exclusively too for about 15years. I couldn't get more than a year out of a pair. They always split at the piviot point between my foot and toes. One year, they just stopped fitting me right and I bought Crocs and have never gone back. They're under $50 and last more than a year. I was concerned about my feet sweating too, but they have better airflow that the Birkis did.

It's worth a try, even if you hate them at least you're not shelling out $100+. Also any socks with polyester in them make my feet smell horribly too. Natural fibers are the way to go.
[jvreg67] (score 2, diepte 1 OP) Not a bad idea. Yeah, I have a footbath at home that I use every couple of days and use foot powder. Socks that are for sweaty feet..etc. Im just an extra sweaty dude.
[jvs5qgf] (score 2, diepte 2 OP) Never knew these were a thing. Might just get one anyways!
[jvuhl3m] (score 2, diepte 2) It’s 1/3 cup for a full tub, super diluted
[jvrenn0] (score 2, diepte 1 OP) Yeah, im usually fine outside of work. But A trip to the foot dr may also be in order.
[jvvzanp] (score 2, diepte 4) I'd also wager to say taking photos and then getting an antimicrobial to treat it is probably also not the route to go. Diagnosing based off photos isn't impossible, but it is questionable. 

Side note: you may also want to be more intentional about washing your feet day-to-day
[l5oe099] (score 2, diepte 4) Try certain DRI deodorant on your feet. It closes the sweat glands. I do this for my feet in the summer. I only use it for it's intended purpose once a week. I'm a petite person who doesn't sweat a lot, except for my feet. Worth a shot. It might take more than one application to work, so keep that in mind
[jvszsqi] (score 2, diepte 1) No not cotton or wool. Bamboo socks are far superior. They take a little longer to dry but they're great.
[jvtr259] (score 2, diepte 4) I'm not a chef but I do know Birkenstocks. If you like wearing them, my advice is:

* Get two pairs and alternate them so the footbed dries out between wears — it may seem extravagant to have two pairs but they will both last longer than if you bought two pairs in sequence
* Cork sealer on the exposed sides (not the footbed) every 4-6 months or whenever it's not shiny anymore — that will keep the part where your foot bends from breaking down
* Clean the footbeds at the same time with sandpaper or a flathead screwdriver to rough up the suede — a screwdriver works great for getting to the inside of clogs. Don't use soap and get them wet, just scrape them off
[jvsbnz6] (score 2, diepte 0) I used Ecco non-slip leather shoes. Super comfy and breathable. I also used Dr. Scholls spray powder. The Odor X one was life changing.
[jvsq0xc] (score 2, diepte 0) I switched to thinner socks, like dress socks and it helped a bunch.
[jvsuubd] (score 2, diepte 0) I did Birkies for a couple years but I walk funny so I always cracked them within a year. Rolled my ankles too many times in Danskos. My boss bought me a pair of knock off Chuck Taylor’s from shoes for crews once and I’ll be honest, I really liked them. I’ve since started getting all my moon slips from them. I’m in a pair of aluminum toe short ankle boots right now. Sixty to eighty bucks every other year, usually because the waterproofing starts giving out, and I’m golden. I was recently diagnosed with Morton’s neuroma (pronounced excruciating foot tendon pain) and when I brought my shoes in to get sized for inserts the doc said what was in there was just as good as what I was going to buy. Can’t say they’re right for you but give them a look. They even have some dress shoe styles that are non slip. My current Chef swears by them. Good luck!
[jvtg27a] (score 2, diepte 0) Hoka makes a super comfortable leather upper nonslip. 

Not cheap, but comfort. Breathability.  Superior build. Black on black.  Also comes in wides.
[jvw28gr] (score 2, diepte 0) I’m not a chef. But I used to work in a fish processing plant so we would have to wear waterproof boots, and they would constantly be drenched in water and fish guts. 

My feet would fucking stink bad. 

The three things I did to help that is 

1) get a boot dryer or prop your shoes up against a floor fan so they dry out quickly. 

2) spray the inside down with a disinfectant spray. I make my own with rubbing alcohol and a few drops of a essential oil in a spray bottle. 

3) Wear wool hiking socks. I like the brand Darn Tough.

My feet no longer stick. And I haven’t had athletes foot in years.
[m4nlsyn] (score 2, diepte 0) I went to the doctor for a callous on my foot, yaddy yadda she said I have nail fungus and I honestly thought my toenails were not terrible but thicker than most...blah blah my mom has thicker nails so I thought it was hereditary and my feet being smelly I thought was sweaty feet from work shoes.  I went to a podiatrist and after 3 treatments of laser therapy and 9 months later, no smelly feet it was the fungal infection I didn't know I had.  Now my nails are almost grown out from 9 months, I can clearly see a difference.  I change shoes between 2 pair and have a fungal spray so it doesn't come back, wool blend socks and baking soda foot bath once a week.  I'm only trying to help by giving my story, it could just be the socks, maybe the shoes got wet and didn't dry properly...good luck!!!
[l2kqc48] (score 1, diepte 2) Mmmmmmm My KindA Guy Deffo!!
[jvykmtr] (score 1, diepte 4) Good socks and some insoles you can change every couple months, too. Makes a huge difference in your back and your knees. And you won't be hobbling around on your first day off.
[jvuq04v] (score 1, diepte 2) 1 capful for a foot tub.
[lp38kau] (score 1, diepte 4) they pour bleach in your city watery and well water.... look it up.
[jvrugj7] (score 1, diepte 2) You just might have athletes foot. Try using some lotion for that for a while see if it helps.
[jvs2hvv] (score 1, diepte 3 OP) I don't think so, my feet are fine outside of my work shoes.
[jvs1ti1] (score 1, diepte 2) you can go online for like 40 bucks, take pics of your feet, send it in, they diagnose and prescribe what you need. cheap, easy, takes 30 minutes, like one od the other guys said you can get an antibiotic and get it to go away. i took one and literally the skin on the bottom of my feet peeled off. best feeling ever.
[jvs2q7b] (score 1, diepte 3 OP) I don't have any actual issues with my feet. I'm nearly sure of it. I just sweat a LOT. Lol
[jvrfsmb] (score 1, diepte 0) Also socks are important. Try to invest is some good cotton socks.
[jvrgebi] (score 1, diepte 0) Blundstones. No explanation needed.
[jvs28ye] (score 1, diepte 1 OP) Nope. Birkenstock clogs are great, id you clean them and replace the soles, they are fine. The material of the shoe itself just got worn out and cracked. They actually have a lifetime warranty, I just want something new.
[jvs1b43] (score 1, diepte 0) I used to wear Birkis exclusively for about 15 years. I couldn't get more than a year out of a pair. They always split at the piviot point between my foot and toes. One year, they just stopped fitting me right, and I bought Crocs and have never gone back. They're under $50 and last more than a year. I was concerned about my feet sweating, too, but they had better airflow that the Birkis did.

It's worth a try. Even if you hate them, at least you're not shelling out $100+. Also, any socks with polyester in them make my feet smell horribly, too. Natural fibers are the way to go.
[jvs6xz3] (score 1, diepte 0) Try chlorophyll in a pill. I used to have to leave my shoes out side. Did it for a couple of weeks haven't had to again since. I am a big guy 6'4" 270 so I go through work shoes about every 6 months. Insoles are the secret. Safety shoes tend to be uncomfortable. Comfortable shoes aren't safe.
[jvs99da] (score 1, diepte 0) I've tried it all. For me personally, only thing that works is normal running shoes.

I know they're not no slip, or safe at all, but God damn are they comfy and breathable
[jvvytnv] (score 1, diepte 1) Or better yet, merino wool socks. 

While I might not be a chef (here for the knowledge), I often spend 12+ hours on my feet with my work and have found that quality lightweight wool socks (even a 50/50 blend) in addition to rotating shoes means I no longer have smelly shoes. And I do wear waterresistant, non-slip shoes for work which don't breathe well so I definitely would stink them up in the past
[jvtjv6q] (score 1, diepte 0) Mozo, good quality multiple different styles. Best nonslip tread I’ve had.
[jvts7fd] (score 1, diepte 0) Blundstone gang
[jvtu7qi] (score 1, diepte 0) This is going to sound crazy...

I had the same problem for a long time.

First of all I don't like clogs. I've spilled hot oil and burnt Alfredo in my clogs too many times. I also do a lot of prep and portering so I'm stomping on boxes and juggling heavy cans and need good toe protection.

I wear some pretty heavy steel toe boots I got from shoes for crews. I also like the cushioning and ankle support. My back is grateful! Been doing this for years now.

That did NOT help my foot odor one bit, obviously!

BUT I've discovered that wearing quality breathable boot socks with moisture wicking, along with exfoliating my feet in the shower has completely fixed the odor problem. My feet even sweat less, and I'm stomping around in boots in a hot as hell kitchen! Whoda thunk it!?
[jvtv7bp] (score 1, diepte 0) Birkenstock Boston supergroups are the way. 
Why birk ever released those abomination of a rubber clog I will never understand. Everyone swear by rubber shoes until you’re sitting on a milk crate next to a guy when he takes his off.
They’re pricey but it’s worth it.
[jvu9rq6] (score 1, diepte 0) I cracked the code a couple of years ago: I fill a large Flairasol continuous spray bottle with 70% alcohol and spray my feet and in between my toes before I put on socks every morning, then spray my socks before I slip on my sandals. My feet and socks never stink, and my shoes always smell like they are new.
[jvvvgbr] (score 1, diepte 0) I had the same issue. I had some croc knock off's that I made last almost 5 years. Towards the end, my feet were rank, all the time. To the point I was embarrassed. Got new shoes (real Crocs this time), smell went away. I think you just have old shoes. The cool thing with Crocs is they are solid rubber and I can wash them if they start to smell. You'd be surprised how much bacteria will build up in an unwashed shoe. That's just my experience tho
[jvwxx5y] (score 1, diepte 1 OP) Oh I washed these once a week. Lol
[l2kpyfe] (score 1, diepte 0) Mmmmmm Wish I Could Enjoy Sniffing Your Socked Feet After A Long Hard Shift/Day!! Then Remove Them Sock's And Basically Lick Your Sweaty-Smelly Barefeet Clean & Dry For Ya!! Bet They Would Taste Outta This World!!
[lcvtadp] (score 1, diepte 0) People can have smelly feet without having fungal infections, some of y'all in these comments are too much 😭
[ll68tsi] (score 1, diepte 0) https://deoxsole.com

For stinky shoes 😉
[jvspve4] (score 0, diepte 2) You def need new work shoes fam
[jvrnxs1] (score 0, diepte 0) I think a top issue is the shoes are NINE YEARS OLD!!
[jw6d27w] (score 0, diepte 0) Crocs!!!

=== THREAD 1hqgf1n ===
SUBREDDIT: r/Chefit
DATUM: 2024-12-31  SCORE: 4  REACTIES: 58
TITEL: Just started in a kitchen. Need some non slip shoes. 
POST (source_id=post):
Googling this brings up so many different types. What do you all recommend? Need some non slip shoes/boots for kitchen work. Open to getting third party insoles too.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[m4p8hes] (score 24, diepte 0) I went to a website called shoes for crews and picked up a pair for 40 bucks that lasted a whole year before my career pivoted. 

If you're looking for an affordable option I'd start there.
[m4pns9c] (score 17, diepte 0) Whatever you do, don't go with Vans. Their non-slip shoes may as well be ice skates. That being said, I wear Vans.
[m4p8lyn] (score 14, diepte 0) I was always a fan of Birkenstocks with the cork footbed. Once the bed molds to your feet they were the most comfrotable kitchen shoes I ever owned.
[m4pchy6] (score 8, diepte 0) Admins.  We need a pinned post
[m4pktce] (score 5, diepte 0) All I’ll say is don’t get the doc martin non slips unless you want bloody feet for 2 months while you break them in 💀
[m4pcbig] (score 4, diepte 0) Shoes for crews new balance. Nice arch support!
[m4pim0w] (score 4, diepte 0) birkenstock makes a black pair with gray non-slio soles.  have to order them online, and they are expensive, but if you take care of them, they last a long time.
[m4pz39p] (score 4, diepte 0) Dansko XP 2.0 and Sanita
The new Dansko clogs havent held up like my older ones, but the XP 2.0 has been great so far.

Sanita is the original maker of Dansko, they WERE Dansko before it got sold.
[m4q13w5] (score 4, diepte 0) Kitchen non slips from walmart. 35 dollars. Comfy as fuck
[m4pek01] (score 3, diepte 1) Skechers McAllen is my go to. Always buy extra when goes on sale. Add insoles. Feels like walking on cloud.
[m4pvtq6] (score 3, diepte 1) I’ve been wearing the Bloodstone clogs for a few years now.  They work great for me!
[m4pbop4] (score 3, diepte 1) Took me ages to get used to them but I agree birkies are the way forward.
[m4qm3hf] (score 3, diepte 1) This. You can take them to the cobbler and they’ll repair the soles for you. Costs about $60 but saves you from buying new shoes yearly and is much better for your foot health!
[m4q0ef5] (score 3, diepte 0) Crocs
[m4p7xa6] (score 2, diepte 0) I recently switched to sketchers and they are affordable and comfortable. Also have many different styles. In the past I used crocs, or Birkenstocks.
[m4q3ep0] (score 2, diepte 1) I've always had bad experiences with Skechers. The cleaners and degreasers seem to disassemble them.
[m4pybfa] (score 2, diepte 1) That's a decent shout.
[m4pie45] (score 2, diepte 1) Wow, those bondis look hideous 😱
[m4pvb6m] (score 2, diepte 2) IDC what they look like. I've got a kitchen floor that's like a skating rink in standard non-slips by the end of the night and my Hokas don't slip even slightly. Plus with some high quality insoles to correct my flatfootedness they feel like walking on air.
[m4qhgvv] (score 2, diepte 3) Luckily our floor doesn't get too bad. Only hazard is a Floormat the owner insists on putting before the kitchen entrance. When water gets under that thing it's a deathtrap, no matter how good your anti slip is 🤦‍♂️
[m4puj0p] (score 2, diepte 1) Me too
[m4q35x5] (score 2, diepte 1) Skechers are shit too, cleaner/degreaser breaks their glue down and they fall apart prematurely.
[m4q3ij4] (score 2, diepte 0) I have birkenstock pu clogs and like them. They are super comfortable to stand in, less comfortable to walk than sneakers tho. Also they are awesome to clean. I got them for 40€. Not the birkies though, heard bad stuff about them
[m4qa4an] (score 2, diepte 0) Super Birkis
[m4pn3ox] (score 1, diepte 1) Thirding sketchers. I'm a big guy, i get around 18 months out of them.  No skid is good enough i run on dirty tile without worrying.
[m4q09j0] (score 1, diepte 1) 4thing sketchers here. They are by far the most comfortable work shoe I've used. 

I've been primarily birkenstock my whole life but changed after my last set opened up at the heel less than 6 months in.
[m4q3cq1] (score 1, diepte 2) The only downside to my birks was the leather strap stretched. Caused my feet to slip more and I burned through some socks from the constant friction. Get tighter fitting first and be patient.
[m4q8smi] (score 1, diepte 2) They always were
[m4rvo8u] (score 1, diepte 1) I love birks but I recently had to switch due to the tread wearing down to fast.
[m4wi57b] (score 1, diepte 1) They were comfy for me but gave me cracked heels due to them drawing all the moisture out of my foot. 

I swear by steel toecap boots that are decent. Not the cheap cardboard ones
[m4pehxo] (score 1, diepte 0) Under $100:
Anything from Shoes for Crews
Crocs
Sketchers
Birkis 

Over $100:
Birkenstock Bostons (strapless)
Birkenstock Tokyos (strap)
Hoka Bondis (new school)
Danskos (old school)

Boots:
Blundstone
Redbacks
Docs (what I’m currently rocking because Blundstone quality control is iffy)
[m4pidk5] (score 1, diepte 0) Crocks!  
Got an expensive pair and danskos early on in my career, working less hours, and they were fucked after 3 months. Now I wear crocks and I'm good with a pair for like 6 months if not more
[m4rfve8] (score 1, diepte 1) I knew a girl who wore brand new ankle high Docs for a 5h hike... bloodbath 🙊
[m4r4oxc] (score 1, diepte 2) They all are. Let's be real. Even birkis are trash. They last a decent amount of time and they are moderately comfortable, but when it's their time to go they have a catastrophic failure while you're carrying a 30qt pot of boiling oil or something. That's why I wear Vans. At least they're comfy when you're nt sliding around. I keep my kitchen very clean and I don't have a deep fryer to get oil everywhere, so they work for me. I've been on the clean side of the pass for long enough to have forgotten the importance of true non-slip shoes though.
[m4ppdks] (score 1, diepte 0) I used several different type of shoes, from crocs, shoes for crews, Payless, bondi sr, and right now I’m using dc martens boots and I love them!!!! I think I will never go back to not using doc martens.
[m4pr01z] (score 1, diepte 0) Blundstone classic slip on boots are amazing if you can afford the $200 price. You will get a VERY long life out of them.
[m4pskoe] (score 1, diepte 0) Birkenstock Bostons or Tokyo if you want a heel strap. My love for these bad boys cannot be overstated.
[m4q3xiw] (score 1, diepte 1) How are the fit on the Bostons? True to size or size down?
[m4q63xx] (score 1, diepte 2) True to size. I'm a size 12 in 99/100 shoes. These are size 12 fore me. I love my kitchen Bostons so much, I'm actually breaking in some civilian Bostons right now.
[m4yr3xh] (score 1, diepte 3) How much room do you have in the back against the heel? I'm hearing different recommendations on sizing, some saying flush in the back is perfect and also a gap in the back is what you want.
[m51ryb7] (score 1, diepte 4) There's a little room in the back. The heel cup is super deep, so it self aligns perfectly. Little room in the front, little room in the back. 🤌
[m4pup10] (score 1, diepte 0) Do not buy cheap shoes, you’re on your feet for long periods of time so you should invest in good shoes
[m4pv7gk] (score 1, diepte 0) Lots of good options out there, I was always a fan of Danskos
[m4pyno1] (score 1, diepte 0) Timberland PRO.. . I fought with Plantar Fasciitis for years, and tried many many brands of non- slips. I never had a problem with it again after wearing these.  I bought 2 pair at a time so they would get equal wear day to day and it worked out wonderfully.
[nrwn94b] (score 1, diepte 1) They do have crocs non slip
[m4q72u1] (score 1, diepte 0) Birkenstock Boston Clogs. They have a non slip sole, are incredibly comfortable - I stand in mine for 18+ hours straight no problem - and last for years.
[m4qd34t] (score 1, diepte 0) Sketchers will have a discount, they don’t care or check if you actually work for that place. Also there’s a binder with all the discount codes, or as always, google is your friend.

Personally, docs ftw. They’re meant to be slip resistant, grease resistant, water resistant, basically you can walk through hell with them. Not cheap, and if you’ve never worn them before, breaking them in takes time.
[m4qozzk] (score 1, diepte 0) [Profi-Birkis](https://www.birkenstock.com/us/profi-birki-polyurethane/profibirki-core-polyurethane-0-pu-u_3866.html). If you have a high instep and Danskos won't do it, go this these. You can take the insole out and throw them in the dishwasher when they get too gnarly. 

As a bigger person, I recommend against anything from Crocs. They destroyed my knees and the movement in the shoes made the "non-slip" sole parts peel right off.
[m4qp4w9] (score 1, diepte 0) Vangelo on Amazon is an excellent discount option. I had a pair last me for years. 

Don't waste money on insoles you can pick up from the pharmacy - what you need to do is get a pair of custom orthotics. They **will not** be cheap, but your knees and back will thank you for years to come.
[m4qtpro] (score 1, diepte 0) Just get super birkis. Bostons and the one with the straps don’t last longer than a year if you really work hard and danskos are good for your back but the sole is literally wood. That shit hurts your knees, ankles, and toes so bad while you’re getting used to it. Doc martens are like bowling balls in your feet and are only 25% nonslip at best. Blundstone is 20% of the quality that they used to be and red back is 10% of their former quality. Crocs are good but they’re hot, super birkis are also hot. Every tennis shoe like kitchen shoe I’ve ever tried breaks in less than a year
[m4qunnb] (score 1, diepte 0) Shoes for crews, and arch support insoles with deep heels, gel in the heel and under the ball. Shoes might last a year, expect to go through 4 sets of insoles. Don’t make the mistake of wearing crocs like I did, took my feet 5 years to recover.
[m4qw47o] (score 1, diepte 0) Buying my first Sanita clogs felt like buying my first Japanese knife, I could again enjoy the same tasks that were tedious at times. Got Sika clogs as well to rotate them sometimes (presumably it's better for your feet) and they are just as great, however I find them just a little bit sturdier, so when I have to cover a longer distance my go to is Sanita. If I mostly have to hold the line on my shift I want Sikas on my feet.
[m4rb7bb] (score 1, diepte 0) Shoes for crews. Especially since you’re just starting out. You’ll want something comfortable, can get wet, and easy to clean.
[m4reb8j] (score 1, diepte 0) Big recommend on slip-on shoes. You’re gonna step in stuff and you can quickly spray off your shoes in the dish pit.
[m4rkjh1] (score 1, diepte 0) https://www.reddit.com/r/Chefit/s/g2PaXWEbqk

https://www.reddit.com/r/Chefit/s/DB0kHdKUdU

https://www.reddit.com/r/Chefit/s/bXzm89wFCA

https://www.reddit.com/r/Chefit/s/8x7OZ49wg0

https://www.reddit.com/r/Chefit/s/N7PgSDyX8M

https://www.reddit.com/r/Chefit/s/QrbqQe0Vug

https://www.reddit.com/r/Chefit/s/QyalflDH1v

https://www.reddit.com/r/Chefit/s/9vl8XcakBB

https://www.reddit.com/r/Chefit/s/DQVeE7ICon

https://www.reddit.com/r/Chefit/s/duaAnJE5Fx

https://www.reddit.com/r/Chefit/s/pqAR9Sv6T5

https://www.reddit.com/r/Chefit/s/TyWnn2VeZa

https://www.reddit.com/r/Chefit/s/YcxAkXmfKm

https://www.reddit.com/r/Chefit/s/zIdyJoIPwO

https://www.reddit.com/r/Chefit/s/2tnpLCsYfJ

https://www.reddit.com/r/Chefit/s/gcrw9mMXVO

https://www.reddit.com/r/Chefit/s/0WHXaBpxdK

https://www.reddit.com/r/Chefit/s/GRDIppJjox

https://www.reddit.com/r/Chefit/s/8S2ACejsBH

https://www.reddit.com/r/Chefit/s/tWtr1IryC0

https://www.reddit.com/r/Chefit/s/AGOuNbWgxo

https://www.reddit.com/r/Chefit/s/60IvZexMks

https://www.reddit.com/r/Chefit/s/Nf0KbY7TGQ

https://www.reddit.com/r/Chefit/s/vB3nplsFhs

https://www.reddit.com/r/Chefit/s/SJ6wLgd9Tt

https://www.reddit.com/r/Chefit/s/L23cxI1rzk

https://www.reddit.com/r/Chefit/s/3B1Rx1hEQV
[m4s0azf] (score 1, diepte 0) redbacks are pretty solid, remember to change your boots every 6 months, your feet will thank you later if you hang around in the trade for a good number of years, they are tax deductible
[m4tfpbi] (score 1, diepte 0) Mozo is the best I’ve used. Shoes for crews has them. I use the “MOZO Natural”. If you wore vans growing up, these are an extremely comfortable version of them.
[m4tq3p3] (score 1, diepte 0) Birkenstocks with the super grip sole. Ive used a lot of shoes in my carreer and these are a game changer, they suck you to the ground lol.
[m4tq5t7] (score 1, diepte 1) And the cork insoles in them are a game changer ofc.
[m4w4xn7] (score 1, diepte 0) Birkenstock don't wear anything else.
[m4xqoqq] (score 1, diepte 0) Skechers chef shoes. I have wide feet that get achey easy. Only shoes that keep me going 14 hrs a day
[m4ynocd] (score 1, diepte 0) I was wearing brunt work boots and those were like skates. I switched to doc martens nonslip and i love having traction in the kitchen again🤩

=== THREAD 1cpddub ===
SUBREDDIT: r/Serverlife
DATUM: 2024-05-11  SCORE: 37  REACTIES: 58
TITEL: Best relief for foot pain after shift?
POST (source_id=post):
What are some of your go to foot pain relief after a long shift? I walk about 10k to 13k steps in a shift. I have decent shoes and just ordered some shoe inserts. But still by the time I get home I'm waddling from my truck into my house. It last a couple days, but when I work consecutive shifts I have no relief what so ever. Please tell me your ways!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l3k5g16] (score 39, diepte 0) Get some slippers with arch support, tumeric supplements and advil. Also compression socks while you’re working helps a ton! And for that many steps you should have multiple pairs of work shoes to rotate through to give your shoe time to reform, or the support won’t be as good the next day.
[l3l6koz] (score 22, diepte 1) Seriously, compression socks. My feet used to absolutely kill after 20k steps a night. Buy compression socks.
[l3k88lk] (score 17, diepte 0) First: Spenco 3/4 insoles

Second: Wedge pillow

I've (63f) been in the industry since 1980. Trust me.
[l3kwyyg] (score 17, diepte 0) Lay on the floor, butt up against the wall, put your legs on the wall, let the pain drain away.
[l3l03k2] (score 13, diepte 0) Roll your feet with a spiky ball. Hurts so good.
[l3kzlwt] (score 10, diepte 0) Get 1 gallon ziplock freezer bags

Fill a bag 1/3 full of rubbing alcohol.  Add another third of water.   Burp out the air and seal it

I like it put in inside another bag, and then all into one more  for a triple seal.

Make 2 of these

Put in freezer overnight.    It will form a super cold icy slush.


When you come home lay them on the floor and ice your feet 10-15 on/ 10 min off.   Repeat a few times.

When done, refreeze and use the next day
[l3kwy16] (score 9, diepte 0) When you get home, lay down in the floor with your butt against the wall and legs up in the air on the wall. Hold for 15 min and then go on living your life.
[l3l43zj] (score 7, diepte 0) Certainly! Here's the corrected version:

A little bit unrelated, but it reminded me of a funny story, so I’ll share.

I was getting ready for work, and my girlfriend had some socks with grippy things on the bottom that she got for Christmas. I thought they were meant to help massage your feet, so I wore them to an 11-hour shift, thinking they would really help me. I could feel my feet getting hotter and hotter by the minute, but I just thought I’d power through the pain because surely it’s working.

I got halfway through my shift, and they were burning—like I mean, burning, as if I were stepping on hot stones. I had no other pair of socks, so I just tried to take it easy and hobbled around the restaurant.

Later, when I got home and took my socks off, my feet were bright red and hot to the touch. I asked my girlfriend, “What's up with those masseuse socks you got for Christmas? They’re killing me.” She replied, “I don't know what you're talking about. I haven’t got socks like that.” So, I showed her the socks, and I could have died when she said, “These are self-heating socks. They use pressure points to keep your feet warm.” My feet were burning for a week straight after that shift. The only plus side is I literally don’t get cold feet now, ahaha.
[l3l1opv] (score 5, diepte 1) Damn reform?! I have so much to learn it’s not even funny
[l3l18fi] (score 5, diepte 0) Grab a cold beverage and soak in a hot bath with epsom salts.
[l3kjjs2] (score 4, diepte 0) After work and maybe before, find a staircase with steps tall enough that you can hang off it. 

Barefoot or in socks, stand on a step facing the stairs so the balls of your feet are at the edge. 

Let your weight down so your feet curl inward then stand on your tiptoes. 

Alternate between the two, working up to 30 seconds in each direction, then work back down to one second. 

Man, this takes a lot longer to verbalize than demonstrate XD
[l3lmsk2] (score 3, diepte 2) I prefer the compression socks without toes. Then wear looser socks over the toes. I use plantar fasciitis sleeves and ankle socks.
[l3lo1ss] (score 3, diepte 1 OP) I never thought about the multiple work shoes thing!
[l3na6b3] (score 3, diepte 1) 50000% some days I would do it for like 10 mins
[l3m1rxt] (score 3, diepte 1) This for me, but it's a frozen bottled water.
[l3lf1wt] (score 3, diepte 0) I love an ice bath. It’s not the most pleasant, but it lessens the inflammation. Also be sure to really really really stretch your calves.
[l3kdbi1] (score 2, diepte 0) Nice long stretch before and after your shift
[l3ownc2] (score 2, diepte 1) Makes a good bonding exercise with coworkers. Lineup along the wall and hold hands <3
[l3l6iu7] (score 2, diepte 0) I take a hot bath and that seems to help a lot
[l3lckyp] (score 2, diepte 0) Mine went away entirely when I got some wide foot zero drop sole shoes. I can feel the gravel in my driveway through the paper thin sole, but they've fixed my foot and knee pain. YMMV
[l3m1ehw] (score 2, diepte 1) ice baths are under rated, they do a lot of good for your entire body. i’m a big cold shower fan after a long day of work.
[l3lpst1] (score 2, diepte 0) Compression socks help like crazy.
[l3n226x] (score 2, diepte 1 OP) I smoked some when I got home, but still hurt lol.
[l3mtrhr] (score 2, diepte 0) Finding the right shoes for your foot is the only real way to avoid discomfort. 

I have wide flat feet. Every year for the past 4 years, I get a new pair of birkenstock professionals and spend 1 month hammering the arch down and breaking them in. The only reason I ever buy a new pair is because I wear the soles out so fast.
[l3n1o0r] (score 2, diepte 0) Arch support is a must for some people.
[lrx3y8e] (score 1, diepte 1) I would add that OP should get a good pair of insoles. Slippers/Shoes are made without much arch support as it's for the average person without pain, not people working long shifts. I bought Stride Soles which has been a life saver for me. It was really easy to purchase and go through their process. I work some long shifts and also work at a clinic in my off-time so i'm on my feet ALOT.
[l3km7im] (score 1, diepte 0) I bought two of those old school gray bus basins from Sam’s Club. I do alternating cool/warm soaks for twenty minutes, always ending on cold. I put ice cubes in the cold water. It does wonders for me.
[l3knrme] (score 1, diepte 0) Decent shoes aren’t good enough. These are the only pair of feet you’ll ever get, take care of them!!!! Dansko clogs, new balance 626 and hoka all have great non slips. 

However this works for me, elevating your feet above your heart. Helps the blood come back and away from your feet. If you’re standing all day it’ll pool and can lead to very very painful almost swelling like pain. Everyone’s feet are different so YMMV,
[l3ktsgy] (score 1, diepte 1) Reddit automatically removes shortened links.
[l3m15e0] (score 1, diepte 1) amazing tip!
[l3mppq0] (score 1, diepte 1) Excellent idea. Add some Epsom salts for extra relief. That magnesium will absorb straight through your skin.
[l3lmnsz] (score 1, diepte 1 OP) Holy crap, that sounds terrible!!
[l3lbxxn] (score 1, diepte 0) Legs up the wall.
[l3lf67g] (score 1, diepte 0) Fill bathtub with just a few inches of cold water and empty 3 or 4 ice cub trays into it.  Stand in this miserable ice water for a few minutes.  It helps if you can shuffle your feet or gently walk in place, to get the blood flowing.   It feels horrible when you're doing it, but it helps to diminish the foot swelling, and feels great afterwards.
[l3lmaf9] (score 1, diepte 0) Quick feet ice bath then soak them in hot water and Epsom salt and massage a bit. (Give a bit of time on between)
But a few seconds in the ice may helps tremendously
[l3lrcd8] (score 1, diepte 0) Whiskey and a chair
[l3m1pit] (score 1, diepte 0) I take about 17,000 steps at work and I wear solely hokas. This is coming from someone who had bilateral foot problems and these are the only shoes that my feet don’t KILL in
[l3m2dl2] (score 1, diepte 0) I've heard a blunt works wonders, but that's not my go to.  For me, the best thing I can do is take preventative measures, rather than remedial.  If I idle in one spot for too long, my feet will hurt way more.  Always be moving, not just because it helps you stay on top of your shit, but also because feet are a lot less sore after work when they've actually been in use the whole time.  If pain is still a problem, gently rubbing them while soaking in warm water helps a lot.  That and just propping them up on a pillow.
[l3n20o1] (score 1, diepte 1 OP) I'm always moving except maybe for 10 min the shift. I get off at 3:30am though so when I get home they hurt and I go to sleep. I massaged them after work last night and that seemed to help with the pain today.
[l3m4yzh] (score 1, diepte 0) Weed and beer
[l3m7fqr] (score 1, diepte 0) Weed 🤷‍♀️
[l3noht6] (score 1, diepte 2) I've got flat feet, I feel you!
[l3mdja8] (score 1, diepte 0) Marijuana and a good pair of custom molded slippers
[l3migxe] (score 1, diepte 0) Compression socks during shift!!!
[l3mqdx7] (score 1, diepte 0) I used to have a bunch of servers from different restaurants  come over to my house for a 'foot party'. 

We had a couple of those heated bubble massagers that you fill up with water. We had a couple of buckets that we would put hot water & Epsom salt in. 

There'd be four or five of us sitting around watching a movie while we were soaking our feet...
[l3nc6h0] (score 1, diepte 0) I can relate! Sometimes I use a vibrating massager on them for a while and it does help quite a bit.
[l3njvxf] (score 1, diepte 0) Wear compression socks for sure, this was a game changer. Also I got a hand-held foot massager to give them some love before bed. On really bad days I use ice packs that wrap around my feet/ankle. Amazon sells em. After icing I’ll soak my feet in a little bucket with hot water and epson salts.
[l3nk9lb] (score 1, diepte 0) If you have flat feet like me, get a pair of oncloud shoes. They’re pricy, but they are amazing. 

Also a massage therapist friend of mine said always sleep with a pillow between your knees for anyone with a job that has them on their feet for long hours.
[l3nmily] (score 1, diepte 0) After 13 years, I am seeing a chiropractor Monday.
[l3noxzb] (score 1, diepte 1 OP) Hope it goes well! I saw one after a car wreck. I should go again
[l3nrrvf] (score 1, diepte 0) Compression socks, and keeping your feet elevated. Especially if you sit down as soon as your shift ends (to drive home). Do some light stretching before getting in your truck.
[l3nv3l1] (score 1, diepte 0) A portable foot massager( for after work)good shoes, good socks.
[l3ogf2a] (score 1, diepte 0) I bought ice pack slippers. I keep them in a gallon bag in the freezer. After really bad shifts, I put them on (with socks) and elevate my feet.
[l3pch4z] (score 1, diepte 0) My SO recently got me this warm foot bath/ massager thing because I have the exact same problem & it’s been working wonders so far
[l3kkcek] (score 0, diepte 0) Sit
[l3lv1w7] (score 0, diepte 0) Peppermint foot spray. I get mine at The Body  Shop.

I am not a server but regularly go to Disney World. My husband is currently using some at a rock festival. Yesterday he walked 13 miles. So far today he's done 6 miles and the concerts haven't started.
[l3meslj] (score 0, diepte 0) Inserts yo
[l3ohx2q] (score 0, diepte 0) You need better shoes. I have zero foot pain after getting my alegria shoes.

=== THREAD sz7kpx ===
SUBREDDIT: r/AmazonFC
DATUM: 2022-02-23  SCORE: 13  REACTIES: 58
TITEL: How bad do your feet hurt at the end of your shift with these safety shoes?
POST (source_id=post):
Laying in bed right now and my feet are throbbing in pain. I bought insoles for my safety shoes because the shoes had absolutely no support on my feet but even with the insoles my feet still kill me at the end of the work day. How many hours do you work a day? Do your feet feel the same way?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hy25v2x] (score 16, diepte 0) Why do I end up limping out the building
[hy2bdum] (score 11, diepte 0) "Acceptable" safety shoes barely start in the price range for the voucher, but everyone just goes for free even though they were going to tear up their regular shoes on the concrete anyways.
[hy268ji] (score 10, diepte 2) At this rate ima need handicap parking

I
[hy261d9] (score 9, diepte 1 OP) Lmao i am laughing, that was me today after pallet jacking for 10 hours. I was moaning in pain with every step
[hy27vfr] (score 8, diepte 0) They don't. I put insoles in mine and I bought em a half size bigger because of the composite toe. I didn't even have to break them in. I wear the Reebok Sublite
[hy2mfq4] (score 8, diepte 0) Posting the beat hack to ever exist for amazon. BUY COMPOSITE OR STEEL TOE SHOE PLUG INS. They sell them on Amazon its pretty much a cap that you put in your regular comfy non feet killing shoes, it essentially makes any shoe safety shoes and thier like 30$ bucks.
[hy24du2] (score 5, diepte 0) My first day wearing them reeboks was terrible. I can’t even walk at the end of my shift. It’s better if you buy insoles but it’s sucks bcoz the insoles are like half the price of the shoes.
[hy25q9g] (score 4, diepte 3) I think it’s mandatory on 1st every Amazon warehouse. They need to offer better shoes tbh.
[hy294th] (score 4, diepte 4 OP) Right? Even tho we get them for free, with the price tags on those shoes you would think they would have better foot supporting shoes
[hy2cxsa] (score 4, diepte 0) I bought a pair of safety sneakers on my own and it was the best thing I ever did. They were $50 on Amazon and they are so much more comfortable than the two pairs I got from Zappos.  

 https://www.amazon.com/dp/B0917KMY1X/ref=cm_sw_r_apan_glt_i_C7MD44RDBJT0BF1V9FSY?_encoding=UTF8&psc=1
[hy251lu] (score 3, diepte 1 OP) Omg my first pair was also the reeboks. Not only did the shoe run on the smaller side, it was rubbing against my pinky toe and the back of my ankle. By the end of the day i had blisters everywhere!
[hy25f4w] (score 3, diepte 2) I don’t know how I’m ever gonna get through the days coming up. They’re going to be mandatory at my site starting in April. I’m not looking forward to it.
[hy25mvb] (score 3, diepte 3 OP) Oh man, they made it mandatory at our site at the beginning of this month. All i can say is prepare yourself, especially if you work doubles. I definitely miss wearing my gym shoes for those long hours. Ugh.
[hy3rb43] (score 3, diepte 0) Our mandatory shoes start next month. How I can hang will depend on whether or not I stay at Amazon. 

Reading all the reviews, I'm fairly certain it's not going to end well for me. :-(
[hyiav6i] (score 3, diepte 1) I hate composite/steel toe shoes. I went yesterday to a prehire appt to return to Amazon until August as a backup incase the job I want doesn’t go through. .
I used to work at Amazon for years.  They checked rehire status, then did my i9 and badge photo. And then the guy gave me a paper and said these shoes are now required. And I asked since when. And he said they just rolled it out site wide, mandatory. And I said oh… I’m good I don’t want the job anymore lol I’ll find something else. And the HR guy said yeah I don’t blame ya I wouldn’t do it either. I wish they stated it clearly now in the application process. I wouldn’t have applied then. 

I’m sure the main reason is to save Amazon money on insurance premiums for general liability etc. But the job sucked in comfortable shoes. And you can find a job that pays the same or more without killing your feet.
[hy42hd3] (score 3, diepte 0) Mine are so comfortable. The timberland pros. I wore them at my air site comfortably for 40 hours a week and I wear them at my current job for 40-70 hours a week.
[hy25g1o] (score 2, diepte 2) Damn sorry to hear that. I got the wide one plus the 50$ insole but holy fawk mate, by the end of my shift it feels like stepping on hard cement.
[hy28iyn] (score 2, diepte 2) I’ve got the reeboks right now, they aren’t horrible for me but they aren’t necessarily the most comfy thing in the world either. Usually by the 6 hour mark my feet are hurting
[hy24le5] (score 2, diepte 0) I recommend wearing them around the house and to the store to help you get used to them. No matter what though it always feels like I’m walking around with bricks on my feet since the can’t “break in.”
[hy258kx] (score 2, diepte 1 OP) I have been wearing them for almost a month now, but exactly what you said it still feels like i can't break them in!
[hy26dpg] (score 2, diepte 0) I’d really recommend the Danners or the Carolina’s. Danners especially.
[hy2jmq5] (score 2, diepte 2) boot brands. I love Danner. I prefer them for my hiking boots.
[hy6vhxd] (score 2, diepte 3 OP) Wow i actually like those!!! Thank you for sharing, i will prbly try these out! I gave you a silver reward, cuz thats all i have on me lol thank you!
[hy2ntqs] (score 2, diepte 0) 0 Pain. I bought myself New Balance 412 work shoes with alloy toe from Zappos with Dr Scholls heavy duty support for 200lb+ when i am 160lbs & it works fucking wonders especially since i am flat footed. i do 10 hour shifts & walk almost 40k+ steps every day at work.
[hy2st3g] (score 2, diepte 0) You might need a gel insert for added shock absorption.  If you’re overweight you might benefit or have ankle pronation issues you might need one that adds stability
[hy3lcoh] (score 2, diepte 0) I always walk with a limp i hate these will mandatory soon at my building
[hy645z5] (score 2, diepte 1) The sneakers are fantastic, the anti fatigue insoles are pretty amazing. I opted for the boots this last time, they’re not nearly as comfortable and taking a little longer to break in and so much worse after an entire day as OB water spider.
[hy4qc5n] (score 2, diepte 0) I work 10 hours, I wear the Tim’s pro, I have a Doc Martin platform boot, and then I switch out with tennis shoes sometimes. The trick is I never wear the same shoes for more than a few hours on my break I changed them. And I buy really good socks. I like the Columbia ones. And the copper infused ones that I got at Home Depot
[hy5rst0] (score 2, diepte 0) My size is barely available for shoes so i'm pretty limited atm. I currently have reebok shoes (with gel insoles) also taking 3 pain killers every night (im aware of the damage) but i still feel pain and limp while walking out lol
[hz74zmc] (score 2, diepte 0) HORRIBLE. I got half a size up, my toes still rub the top of the shoe. My feet feel 10x heavier. I legitimately look and feel like Ronald McDonald.
[hzx4b7l] (score 2, diepte 0) Gel insoles make my feet burn . Air pillows or orthodics are the way to go or if they really want our feet to be so safe then how about having specially designed and fitted custom made shoes instead of wasting all my time off trying to find a pair then try the pair then return them then hunt some more and it's all unpaid time . Talk about time theft
[hzx4iju] (score 2, diepte 0) To be fair my feet hurt anyway cuz I eat too much crap and drink too much soda
[hy23j8c] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. We have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[hy26l0m] (score 1, diepte 1 OP) Are those insole brands?
[hy3milr] (score 1, diepte 2) Boot brands! I’ve never needed insoles with either of them.
[hy30ym6] (score 1, diepte 1) Dude those  rad i wish they made them for women.     But i am only like a 4 in boys.
[hy3otxe] (score 1, diepte 2) They have them in women's too 👍
 https://www.amazon.com/dp/B09177VPS4/ref=cm_sw_r_apan_glt_i_TQJAKN0T79D8N65F265R
[hy5psgn] (score 1, diepte 3) Thank you so much. I have not been able to break in the  reebocks for anything.
[hy5tlnm] (score 1, diepte 4) No problem trust me I was fed up with the Zappos too and thank you so much. That's my first award. It's greatly appreciated 👍
[hy6z0lh] (score 1, diepte 4) Yeah no problem. I found they worked better for me so I'm happy to share the info. Trust me I appreciate the award, thanks so much 👍
[hy8qu0i] (score 1, diepte 1) Why didn’t I get the 200+ lbs one??? Is it literally just thicker? I have dr scholls and my feet hurt so bad that I don’t want to move when I’m off.
[hzawrj6] (score 1, diepte 1) I bought the 200lbs+ based on ur advice and it’s saving my feet right now. I feel minimal pain with them now especially since I’ve got constant pain in my heels currently
[hy2vreb] (score 1, diepte 0) Depends on how much I walk this week wasn’t too bad just under 22 miles usually it’s a lot higher but the slow season has it okay
[hy35p0d] (score 1, diepte 0) Literally never. Rebocks and half a size up
[hy39z3o] (score 1, diepte 0) Following as my building has yet to mandate the new shoes. I have the flattest feet possible and I am on edge about this new standard. If anyone that has flat feet could give any feedback to how the shoes are affecting them I would be very appreciative!
[hy3lrge] (score 1, diepte 0) I take my boots off in my car during break it helps me
[hy3p0ub] (score 1, diepte 0) Not at all. Female, Ariat boots with a composite toe I believe. Once they were broken in and I got used to them being heavier than normal shoes, it was a cakewalk. Year and a half later I need some insoles for them but that's it.
[hy3v1ug] (score 1, diepte 0) Mine never hurt after I bought my shoes lmao
[hy4pi0v] (score 1, diepte 1 OP) Where did you buy yours?
[hy401xk] (score 1, diepte 0) Very Bad ! Insoles and all ....
[hy4sasr] (score 1, diepte 1 OP) Are the safety shoes mandatory at your site?
[hz2os8l] (score 1, diepte 2) Not yet but I wear them
[hy4usrs] (score 1, diepte 0) I got Timberland Pros with anti fatigue sole and after a week long break in, pain is minimal
[hy6u3vo] (score 1, diepte 1 OP) Oh goodness! That sounds extreme lmao
[hy7gcnc] (score 1, diepte 2) yea i hope workwear brands start going for smaller shoe sizes i hear all about comfortable boots but they're so huge lmao
[hyc044t] (score 1, diepte 0) None. Get some good insoles
[hzx5sdx] (score 1, diepte 1 OP) 😂😂 right? We should fire them for TOT lol
[i61ckz5] (score 1, diepte 0) I’m still wearing my comfy sneakers. They don’t say Nike or adidas and are black. They are just comfy orthofoot.com. I doubt safety will check or notice. No way my big foot is going into a pair of steel toe high heel shoes.

=== THREAD sk0ni3 ===
SUBREDDIT: r/FASCAmazon
DATUM: 2022-02-04  SCORE: 31  REACTIES: 58
TITEL: Best shoes for work that amazon gives free Skechers wolverines timberland cat Carharrt n a few other, these have really best insoles cats are ok but not the best. And these brands have good ankle support and orthopedic insoles. I worked for a major shoe depart out here on the east cost back then.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hvibncv] (score 9, diepte 0) That thing looks painful.
[hvilwzx] (score 5, diepte 0) Redwings 1907 only. Change my mind
[hvjwhux] (score 4, diepte 0) Name and brand of shoe / boot ? I agree , zappos selections sucks @$$
[hvl22h7] (score 4, diepte 0) The timberland pros are probably the best, most comfortable work shoes I've ever worn. Far superior to shoes for crews
[hvkzbnj] (score 3, diepte 2) We work at Amazon , so no 🤪
[hvjx71d] (score 3, diepte 0) The 5.11 hiker boots have been my fav thus far from Zappos. They hug the ankle nice and tight but not painful and can honestly say can work in them for 10-12 hrs with way less pain compared to anything else I’ve had.
[hvmcmy2] (score 3, diepte 0) And they don't look like clown shoes, that's a plus.
[hvo8h9z] (score 3, diepte 1 OP) No they are light actually and the orthopedic insoles are very nice they are Skechers made for work
[hvl6g3n] (score 2, diepte 2) Never lmao. The day construction workers are convinced, I will be too. Not to mention their poor build quality
[hvl32kg] (score 2, diepte 1) Go with anything timberland pro, especially the ones that look like tennis shoes. Our fc have us 120 for shoes, so you'll have enough to get some insoles too
[hvluqss] (score 2, diepte 1) Dude they’re the fucking best. I’ve had 5.11’s on the ambulance but these are a cut above
[hvlhd1n] (score 2, diepte 1) I agree, I love mine
[hvluo58] (score 2, diepte 0) The 5.11 hiking ones are the most comfortable shoes I own, no joke
[hvpph4m] (score 2, diepte 0) I personally went with a pair of 8" Moxie Trades (boots). Super comfy.
[hvq0q92] (score 2, diepte 1 OP) Really
[hvi4815] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If you are interested in learning or asking about anything related to covid leaves and its process, please visit our [Megathread](https://www.reddit.com/r/AmazonFC/comments/s1m1qr/all_about_covid_leave/). We also have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/FASCAmazon) if you have any questions or concerns.*
[hviehpy] (score 1, diepte 1 OP) No it’s very comfortable very comfortable u should see the reviews on them
[hvih8tu] (score 1, diepte 0) Nah I rock the Danner sneaker. I wore Danner boots in way worse environments in Danner boots. I’m gonna get the really cute Thorogood sneakers they have too.
[hvj9wdu] (score 1, diepte 1 OP) O ok
[hvl36o7] (score 1, diepte 1) Timberland pro
[hvlbrps] (score 1, diepte 3) Had mine for 2 years, very little wear an tear-just around the toes. I heard red wings last forever tho
[hvm4a4t] (score 1, diepte 1) But they don’t have a safety toe 😬 I got Irish setter moc toes cause it’s the closest thing
[hvnxqpd] (score 1, diepte 2) And? They aren't going to audit our shoes lol
[hvp11us] (score 1, diepte 3) Yea but I can’t get the credit on Zappos for them 😂 I might get some when I have a extra $350 😂
[hvotfum] (score 1, diepte 1 OP) Nice red wings are good also
[hvj3w06] (score 1, diepte 0) I don’t have anything to compare it to but I got the tennis shoe style timberland pros and they were soooo much lighter and more comfortable than expected
[hvjkzym] (score 1, diepte 0) they probably are comfortable! i ended up getting the white reeboks they have because they didn’t look ridiculous but im not sure how comfortable they are. i have flat feet and standing in bad shoes really sucks
[hvjyspy] (score 1, diepte 1 OP) Hmm not cool flat feet
[hvl350f] (score 1, diepte 3) It totally does, dudes a dumbass😂😂
[hvm23v9] (score 1, diepte 5) I love my timbs! I got narrow feet so I gotta wear 2 pairs of socks tho😂 which ones did you get? The Reebok boots are comfy roo
[hvotaau] (score 1, diepte 2 OP) Facts your right Skechers Radford
[hvkzgz8] (score 1, diepte 0) I'll have to try these out next time, I just got some keens that are really good though
[hvl01gj] (score 1, diepte 0) Can’t confirm
[hvl3qul] (score 1, diepte 1 OP) Skechers
[hvmh4yr] (score 1, diepte 2) Which ones you get?
[hvmig7x] (score 1, diepte 3) The day one safety drivetrain ones
[hvot7wu] (score 1, diepte 4 OP) Witch timberlines guys drop a picture
[hvot5ki] (score 1, diepte 1 OP) What they look like drop a picture
[hvmn5x1] (score 1, diepte 1 OP) Facts
[hvml7u8] (score 1, diepte 0) I’ve been using the carharrt shoes since last June with no issues.
[hvmn8xf] (score 1, diepte 1 OP) Sweet I have a pair I paid out pocket for my self for work also
[hvn8djg] (score 1, diepte 0) If you have falling/fallen arches, 3M Futuro makes an adjustable arch support that straps on to your foot that is incredible.   The great thing about them is, unlike an insole, you can wear them pretty much all the time with any footwear or even barefoot.  I had $300 custom orthopedic insoles that don't work as well as these do, and they cost like $14 for a pair.

I'm a DSP driver, my feet take a ton of abuse...  I could not do this job without these.  I can't speak highly enough of them.
[hvniqio] (score 1, diepte 1 OP) Really u gotta picture of them
[hvnu8rs] (score 1, diepte 0) i got black reeboks and they're surprisingly not super awful. definitely can't wear ankle socks because they rubbed my ankles the first day but now they're fine. i also drive an OP all day so i can't say much in terms of having to walk in them all day, but compared to most other safety shoes i've worn, they're good enough 😅
[hvo87h0] (score 1, diepte 1 OP) I had the Reebok work shoes they are ok but they hurt my feet I couldn’t wear them shoes I don’t think they are to good actually cause the lil rubber sole at the bottom will come off fast n there not so good walking in snow
[hvo7djx] (score 1, diepte 0) Y’all feet don’t feel heavy walking around with those big boots. Making your feet hurt at the end of the night?
[hvs1ia6] (score 1, diepte 2) They come with orthopedic insoles?
[hvwa96j] (score 1, diepte 3 OP) Yes they do
[hvpk5am] (score 1, diepte 0) Rockports.
[hvpohab] (score 1, diepte 1 OP) no Skechers
[hvq0y3h] (score 1, diepte 2) Surprisingly, yes lol. It was an extra $12 after credit but well worth it
[hvkxeq8] (score -2, diepte 1) Waterproof. Can't you read?

