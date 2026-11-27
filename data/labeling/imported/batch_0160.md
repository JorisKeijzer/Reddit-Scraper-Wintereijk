# Label-batch batch_0160

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
Schrijf het resultaat naar `batch_0160.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1ju0cak, 1qlogqg, 1jvzu68, 1dsdh1y).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1ju0cak ===
SUBREDDIT: r/BuyItForLife
DATUM: 2025-04-08  SCORE: 26  REACTIES: 59
TITEL: Best sandals/slippers with arch support for daily use for 3+ hours of walking?
POST (source_id=post):
Long story short I work indoors and need to walk 3 to 4 hours a day and I usually wear sandals or slippers, but due to flat feet and foot pain, I've been looking around for other options. I tried Birkenstock, but got blisters on the sides of my heels. I got hoka recovery slides which were nice, but they offer less support than Birkenstock. Also I was reminded that they are for recovery and not actual walking for hours a day and they will not last long doing that. So I've been looking around to find something else. Any suggestions? By the way, I live in Canada.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mlyjwvh] (score 31, diepte 0) I exclusively wear Chacos in warm weather.
[mlyek9i] (score 16, diepte 0) Birks are the best. Wear them with socks to break them in and then they’ll be the best shoe you’ve ever worn
[mlycqb0] (score 15, diepte 0) I wear Dansko sandals all day around the house. The current version of them seems to be called “Maddy” - they’re slightly different from the version I originally had but also have great support. You can actually walk in them as regular shoes.
[mlydhj9] (score 14, diepte 1) The Oprah's boyfriend of your feet
[mlyrl6w] (score 13, diepte 0) Vionics is a brand of sandals with good arch supports but nothing beats my birks
[mlydhsx] (score 12, diepte 0) Berks.
[mlyfwwy] (score 6, diepte 0) You said you got blisters on the side of your heels from Birkenstocks. Were you wearing one of their models with the strap on the back?
[mlycbjv] (score 5, diepte 0) Stegmann
[mlzmxgk] (score 5, diepte 1) I wear Dansko sandals as indoor shoes in the summer and Taos or Halflinger wool slippers in the winter. I need good support and they deliver!
[mlyf9js] (score 5, diepte 0) Get something with a strap behind the ankle like Chacos or Tevas
[mm1u8tf] (score 4, diepte 1) For someone with flat feet and similar to OP, I found chacos had too high of an arch and caused me too more pain.
[mlyowyx] (score 4, diepte 0) Have you tried Oofos Recovery Clogs? A nurse friend advised me to get them for my fallen arch/fasciitis. They have been amazing. I have concrete floors in my house and I've been wearing these when at home, for at least three years.
[mlz0a2u] (score 4, diepte 0) I love Naot.  Their footbed looks similar to Birkenstocks but much more comfortable.  The styles are also less blocky.  They are spendy but last forever.  They are the only pair of sandals I've found where I can wear them all day and not get blisters or foot pain.
[mlz1pri] (score 4, diepte 0) Is there a reason wh you don’t wear walking shoes/sneakers? There are a ton of great options that nurses and servers are always recommending. Dansko clogs are also a hit with those “on your feet all day” occupations.
[pa6jo0m] (score 4, diepte 0) For arch support in sandals and house slippers, contoured footbed options (Birkenstock, Oofos for recovery, Vionic) are popular. Wearing something supportive around the house makes a big difference if you have arch or heel pain, since barefoot on hard floors adds up. Stride Soles' custom insoles are for closed shoes, so they pair well with a supportive slipper for the rest of the day.
[mlyeeo6] (score 3, diepte 0) Dansko - safely ignore any rec that isn’t Dansko
[mm0lhhr] (score 3, diepte 1) I get crazy Achilles tendon pain from my birks. It’s a real bummer.
[mlygui0] (score 3, diepte 0) I wore socks with my birks until they were comfortable
[mlyjvu7] (score 3, diepte 0) The tongue of English lacks the words I need to convey to you how truly incredible Bedrock sandals are. After years of skateboarding my feet would hurt constantly if I stood for too long. Bedrocks completely changed my life. The first week you may need to build up some calluses, but don’t be deterred.
[mm0377z] (score 3, diepte 1) Big +1 for Bedrock Sandals. I am passionate about their Mountain Clogs
[mlzey95] (score 3, diepte 1) Yup once it's warm >55° it's Chaco Time. My table line is coming along well.
[mm23y0y] (score 3, diepte 1) Forever love my chacos. If OP is getting blisters with the Birkenstocks heels, I’d recommend going for a wide width, and then the original footbed (not cloud) and no toe strap. 

The arch support shape is pretty prominent, so it’s not going to work for every foot shape, so definitely try it on first or order from somewhere that has easy returns.
[mlyx4mz] (score 3, diepte 1) I love these! I have winter and summer versions. No break in period required
[mlzhc2v] (score 3, diepte 1) My Vionics are comfortable, but I am disappointed in the poor construction for a flipflop I paid that much for. Mine started to fray after one season of wear. 


I have daily wear Birkenstock clogs that I've had for over 10 years and are still going strong.
[mlzvhoy] (score 3, diepte 0) I love many models of FitFlops but spend lots of time wearing their Surfa: https://www.fitflop.com/us/en/shop/surfa-toe-post-sandals-p-H84#001
[ohc0oeg] (score 3, diepte 0) Dr. Zac Cartun, MD here. I am co-founder of a company called Stride Soles. We make custom orthotics, but recently released a custom sandal which might be of interest to you. With 3D foot scanning and gait analysis, its a top notch personalized sandal. They also look quite similar to Birkenstocks if you are going for that look! 

DM if you'd like a discount code!
[mm2ciru] (score 2, diepte 1) I think this is the answer. Indoor only walking sneakers for work. I take online meetings on a walking pad & quickly realised that slippers and sandals don’t provide the support that runners do.
[n1hw7sn] (score 2, diepte 1) Bought my spenco sandals in 2014 and still use them today. Just pulled a wooden splinter out of them this morning and currently looking for a new pair. Seems they aren't made as durable these days.
[mlzpbng] (score 2, diepte 0) I live in my Birkies - never had them cause blisters!  I wonder if you need a different width?
[mlyozkb] (score 1, diepte 2) Haha
[mlyn1bz] (score 1, diepte 1) i tried real hard to find something better than birks and if it’s out there i can’t find it. the zermatt slippers don’t hold up as well as the sandals for obvious reasons but i finally just broke down and ordered yet another pair of sandals to just wear indoors.
[mwxsav2] (score 1, diepte 2) I didn't think the Zermatt slippers looked sturdy enough and went with the lined buckley. Works great as a slipper!
[mm1lomu] (score 1, diepte 2) I am so sorry for you for that. I can’t imagine not living in mine
[n2h3xpq] (score 1, diepte 3) What kind of arches do you have? I am reading birks have low arch
[n2h89gi] (score 1, diepte 4) I honestly don’t know lol but I find Birkenstocks very comfortable and supportive and Chaco boots, which have a higher arch, so 🤷‍♀️
[of7ewm6] (score 1, diepte 1) Thanks for the reminder, I wore socks with my other support sandals but I'll start doing that with Birkenstocks!
[mm1no5x] (score 1, diepte 1) Yep. I’ll prob be buried in mine.
[mxaemw0] (score 1, diepte 1) Chacos hurt my arches, but know many people who love them. Birks hurt my feet also- have tried them several times and they just dont work for me, sadly.
[ot22vll] (score 1, diepte 2) Have you tried Tevas?
[ny7w1dm] (score 1, diepte 1) Quel modèle de Chacos ?
[ny8p6oh] (score 1, diepte 2) Z1/Z2.
[mlylnog] (score 1, diepte 0) I wear the plastic lightweight birks! I have quite a few other arch support sandals but always reach for the birks!!!
[mm24inf] (score 1, diepte 1) Are oofos is still really squishy? I got a pair of the slides a while back, and they were just too squishy to actually do me any good (and weirdly narrow on my feet).
[mm2f6xv] (score 1, diepte 2) These Recovery clogs are firm, especially in the arch.
[of7fgwc] (score 1, diepte 2) Oofos ARE squishy, mostly meant for recovering after hard workout same with Hoka recovery slides but they're firmer with good arch support.


That's the other poster say don't don't really wear them for long walking but for shopping and all I think they're fine⁶
[mm4orek] (score 1, diepte 1) Yes oofos will change your life
[of7eav9] (score 1, diepte 1) Yes it all comes back to Birkenstocks😁


I have bad arthritis in one knee and nothing really beats Birks, but I think for walking they get dirty too soon.


Try Skechers Archfit Go Walk and I noticed a lot of nurses wearing Hoka trainers. For everyday wear I wear Hoka recovery slides, cuts down on pain and maybe good AFTER you walk.
[of7fvj6] (score 1, diepte 2) You were right you know and I think HOKAs are a good option. I see a lot of nurses and caretakers wear them
[mlzkokv] (score 1, diepte 0) Spenco flip flops did it for me. Though they don’t last terribly long.
[mlzt4xj] (score 1, diepte 0) I work indoors and outdoors, have to walk through different terrains some days to visit sites, dusty, muddy, tarred, concrete, you name it... Keeping my birks clean has been tough job so got one Crocs Echo clog. Now I am the happiest with that one. Easy to clean, Washable, absorbs some impact even if I hit my leg on something, decent enough arch support for me, got good grip as well. (Might not work for everyone though)
[mlzt5dk] (score 1, diepte 0) I work indoors and outdoors, have to walk through different terrains some days to visit sites, dusty, muddy, tarred, concrete, you name it... Keeping my birks clean has been tough job so got one Crocs Echo clog. Now I am the happiest with that one. Easy to clean, Washable, absorbs some impact even if I hit my leg on something, decent enough arch support for me, got good grip as well. (Might not work for everyone though)
[mm0p0q4] (score 1, diepte 1) Huge fitflop fan here as well!
[mm5a2oe] (score 1, diepte 1) I have lived in Surfas for so many years, and I’m really concerned because they really don’t have many right now
[mm030vh] (score 1, diepte 0) I am a big fan of Bedrock Sandals — I love their Mountain Clogs
[mm04s08] (score 1, diepte 0) I like the Haflinger clogs more than Birks.
[mm0tpey] (score 1, diepte 0) Berks are bad at first , but then they are oh so good.

My dad has been wearing them exclusively for 50+ years (he put socks on when it gets cold). Retired  ow, but he was a teacher up in front of a classroom of middle schoolers for 45 years. 

Other than Birks I like Keen’s for a lot of walking.
[mm0zlv1] (score 1, diepte 0) I bought Viakix after I saw someone recommend them on a subreddit. They are incredible. I wore them to Disney for a week and my feet felt great.
[mm1gnau] (score 1, diepte 0) I've been wearing Reef Fanning sandals for years. Not BIFL, but they do last quite a long time.
[mm20e3o] (score 1, diepte 0) Naot Kayla, I’ve walked for hours in them and not been sore and that is something I struggle with and went through a few until I found them. For example I love my birks but can’t walk very long in them before they begin to bother, same with Olukai, and Taos didn’t work for me at all. The Naot’s are magical for me but everyone’s feet are different and you have to find what works for you.
[mm2ib7q] (score 1, diepte 0) I love my reef platform slides. They are cork and because they’re so tall they conform perfectly to my feet. I have really high arches tho so not sure if they’re right for people with flat feet. They’re pricey, I think they’re like 50-60 bucks but I haven’t found anything I like more for everyday slides I can wear for hours
[mm5aapn] (score 1, diepte 1) I bought reef platforms last year probably different than what you have doesn’t probably matter. It has the cork. I love them, but my feet slip in them. Do you have that problem or a solution?
[mmbcp9k] (score 1, diepte 2) My feet def slip in them sometimes, maybe it’s the cork smoothing? But the arch support I got from them shaking to my feet was honestly worth it to me. I wear them all the time for all day and it’s not a big enough issue for me personally for them to not be my everyday.
[mm2l8us] (score 1, diepte 0) I get Orthofeet slippers and sandals, and they really help minimize pain!
[mm2obz6] (score 1, diepte 0) Kenkohs
[mm3060e] (score 1, diepte 0) Finn comfort is an expensive orthopedic shoe that is related to Birkenstock (or once was, I think). I have a lot of foot problems and find them extremely comfortable. I know you said you tried birks but these do fit differently. They also last a long time- which is good considering the price.
[nf4ym84] (score 1, diepte 1) I’ve worn Finn Comfort for years.  Are still my go-to shoe without needing orthotics.  Wish they were cheaper.
[mm37oel] (score 1, diepte 0) I wear Teva Olawahus as my indoor shoes and they're noticeably more comfortable on my bad back than almost any others, (except those Hoka recovery slides, those are magical for back pain). I find the crisscrossed straps to be more supportive than slides. The Olawahus aren't BIFL, but I've repurchased them maybe 4-5 times since I started wearing them 15-20 years, and they get worn all summer long. Pretty sturdy, except for the one pair that got chewed up by a puppy.
[mm4bi6b] (score 1, diepte 0) Clark's.
[mm5hrqt] (score 1, diepte 0) Chaco classic sandals.  Not the z cloud version, the classic z’s.  I exclusively wear them in the warmer months, no other sandal even comes close for support and durability. 

I still have my original Chacos from 2003, they’re worn  down but still kicking.  I’ve bought newer ones since then, and have yet to wear thru a pair of the classics.  I did wear thru a pair of Chaco flip flops - it took 7 years of summer wear, one year I traveled a lot and wore them about 300 days straight.  They died a valiant death when stuck in deep mud, I immediately went out and bought a second pair.  Still have them, but I now wear the classic Z’s more often.
[mm5lpzh] (score 1, diepte 0) Crocs are darn good- and so are hardliners.
[mm5lsr0] (score 1, diepte 0) Haflingers
[mm5tpk2] (score 1, diepte 0) Oofos slides. I'm 9 months pregnant and have developed plantar fasciitis. I bought Oofos, Birkenstocks, and Crocs in a fit of desperation. The Oofos are the best by far.
[mm62kad] (score 1, diepte 0) Vionics allowed me to walk for years. I had fallen arches and neuromas and I could walk in those for hours
[mxaebcw] (score 1, diepte 0) after 13 foot surgeries, the only sandal I can wear for any amount of time is Teva hurricanes.
[mye5j0p] (score 1, diepte 0) For the blisters try Body Glide. It’s a wax stick for your feet (looks like deodorant). Apply generously to the friction areas where you are likely to get rubbing or blisters before you put your shoes on and your feet will be saved!! This stuff was a lifesaver for me in Disney and for special occasions wearing heels, etc.
[nmpa66m] (score 1, diepte 0) Try Adidad Yeezy Slides make. Go for 'Pure' 2019
[nrh8c1w] (score 1, diepte 0) i got [these](https://www.walkfulton.com/products/the-house-shoe) from fulton, and truly never been happier with a purchase in my life. I've been a fan of their insoles for years, but the slippers are even better
[nz56jda] (score 1, diepte 0) I need arch support too. My sandals from Margaux have a nice, supportive footbed, and the handmade quality is obvious.
[o67eabj] (score 1, diepte 0) I don’t think you can work with open toe shoes with flat feet to be honest. If that’s a non negotiable then you’ll have to stick with the birkenstocks unfortunately, the break in period’s pretty ass but they’re still the most supportive in the long run, wear bandages on the sides or buff them down if you can? The leather can be pretty stiff. Try some powerstep ones too if you can deal with a closed top. They’re more like bedroom slippers but with a proper sole, arched. If you’re not going outside much then they should last you a good while, I think they were [on amazon](https://datagrove.vercel.app/?q=1YJMYF1185) last I checked, see if they ship to you.
[o6chqpw] (score 1, diepte 0) I don’t think you can work with open toe shoes with flat feet to be honest. If that’s a non negotiable then you’ll have to stick with the birkenstocks unfortunately, the break in period’s pretty ass but they’re still the most supportive in the long run, wear bandages on the sides or buff them down if you can? The leather can be pretty stiff. Try some powerstep ones too if you can deal with a closed top. They’re more like bedroom slippers but with a proper sole, arched. If you’re not going outside much then they should last you a good while, I think they were [on amazon](https://datagrove.vercel.app/?q=1YJMYF1185) last I checked, see if they ship to you.
(5 reacties met lagere score weggelaten)

=== THREAD 1qlogqg ===
SUBREDDIT: r/BuyItForLife
DATUM: 2026-01-24  SCORE: 2  REACTIES: 59
TITEL: Outdoor sandals with good arch support
POST (source_id=post):
First time poster here but been lurking for a bit and I thought I'd reach out to see if there are any recommendations for outdoor sandals with arch support.

I've got flat feet (barely any arch) and I tried a few pairs of Teva sandals today to much disappointment. I have also read that Tevas don't last as long anymore and would like to know if there are any brands/makes that are decent in quality these days. 

Thank you!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[o1fjt1n] (score 36, diepte 0) Try chacos. They have awesome arch support.
[o1fpgbq] (score 21, diepte 0) Birkenstocks
[o1g0r3h] (score 11, diepte 2) They honestly will outlast every other show you own and can be rebuilt to outlast everything else.   I have a 15 year old pair.
[o1fkd84] (score 11, diepte 0) I like the classic Chacos for support, with the caveat that they're pretty heavy for a sandal.

Best of luck!
[o1gelnu] (score 11, diepte 0) Check out OLUKAI sandals
[o1fw29u] (score 6, diepte 2) They are built like tanks and can be resoled.
[o1g9d1o] (score 6, diepte 2) Probs not as durable as before anymore. Still. Good arch support. And I managed to resole mine to get some extra years out of them
[o1fpgtp] (score 6, diepte 0) I wear Keen H2s.
[o1hmqym] (score 5, diepte 1) I can also endorse Birkenstock sandals. They are pretty easy to maintain when the footbeds get dirty.
[o1hp8y4] (score 5, diepte 1) Birkenstocks are great, but any time I wear them off pavement I get all sorts of sand, leaves, and rocks in them and, because of the lip around the foot bed, I have to completely remove the sandal and shake it out. Love them for regular use, but I can't imagine enjoying them on a hike.
[o1gym4h] (score 5, diepte 0) Mephisto Helen Sandal. I have 3 pairs, the oldest from 2010. They're comfortable, stylish, have great arch support.
[o1gonma] (score 4, diepte 3) I have the cork and leather ones and have had them three years. Mine are holding up great and they have excellent arch support.
[o1ga9pj] (score 3, diepte 3) Get the cork & leather ones tho, the plastic ones are nowhere near as comfortable
[o1gi6cu] (score 3, diepte 0) Are you looking for a "flip flop" style sandal or something with a bit more stable with straps?

I use reefs and they have good arch support for me but they are flip flop style.
[o1i9fb4] (score 2, diepte 8) You clearly have your own agenda here. 

I am not making any assumptions. Sending your Chacos in to be recrafted may cost more than what you personally want to pay, but plenty of people use the service and prevent their worn-in midsoles and straps from going to the landfill.  What other brand does the Chaco sandal get sold under besides Chaco and why does that even matter? Provide a link.

As for whether a PU footbed is too worn out, even if it was, it would be literally no worse for you than the flat piece of leather you are suggesting. You should probably think out your thoughts a little more thoroughly before posting. You are not knowledgeable of OP’s personal health - YOU are the one making assumptions. Stop providing unsolicited health advice to people you don’t know.
[o1hvtkn] (score 2, diepte 6) Yeah. Classic “you don’t want what you want. You should want something else.” I enjoy walking barefoot, but if someone wants a sandal with arch support, and you don’t want to offer a useful response, it is best just to the mouth shut.
[o1g2l8r] (score 2, diepte 3) 1. Some company X makes good stuff
2. Conglomerate/private equity sees that company X makes good stuff
3. Conglomerate buys company X
4. Conglomerate milks company X for money
5. Company X no longer makes good stuff and fair price
[o1qisqi] (score 2, diepte 2) Everyone is different but OP asked for recs for arch support so just thought I’d suggest what worked for me. Shoes are so hard though for us foot challenged folks. Everyone is different.
[o1hk2i0] (score 2, diepte 0) Chacos used to be good but the new ones are very poorly made and don’t last. Bedrock Sandals are what you want.
[o1hkvhh] (score 2, diepte 0) Chacos, Birkenstock, Rainbow (double layer not the single) are all supportive
[o1piaoz] (score 2, diepte 1 OP) Yeah I tried the Tirras actually. I was wearing my orthopedic shoes that day and was looking for something with similar support and I'm now wondering if that's unrealistic.
[o1irb26] (score 2, diepte 0) Tevas don't work for me, but I really love my Taos
[o1jksru] (score 2, diepte 0) Chacos. I take everywhere with me, wear most days of the year as long as. Have crunched through remnant snow in the cascades and rockies, fishing in rivers all over the west, the brutal deserts of West Texas in the summer, around Dallas, NYC, Boston etc. Just make sure you get a pair with the vibram soles, they hold up way better than the chaco brand soles I tried once. Have 2 pairs, one 12 years and the other about 5.
[o1l3fx1] (score 2, diepte 0) Orthofeet! My favorite sandals are from there. They aren't super sexy or anything but they're super comfortable for walking.
[o1ndct0] (score 2, diepte 0) Bedrock offers several different lines. Sturdier than Xero's, less brick-like than Chacos.
[o1g17ne] (score 1, diepte 4 OP) I agree - I feel like BIFL when it comes to footwear is hard to achieve. I'll try chaco to check for fit but I'm not a fann of fully PU footwear.
[o1hwtv6] (score 1, diepte 6) And yet you offered no alternative options which meet the OP’s needs. They don’t want a piece of leather and some straps. They want a sandal with arch support. Let’s stick to answering the question being asked, and not a question that is not being asked. 

There is nothing theoretical about Chacos being able to be resoled. They offer recrafting services, and people use it so they don’t have to throw away perfectly good straps and midsoles.
[o1i1e1k] (score 1, diepte 7) 1. Their repairs cost around the same, or more than same sandals sold under diffirent logo. My point is that boots with PU midsole arent meant to be repaired(even when manufacturer offers repairs) - if outsole wears out before other parts do, thats an indicator of insufficent outsole, not dourable upper. If only there was natural, dourable, biodegradable material that was used in footwear for thousands of years...
2. You are assuming that OP is correct: arch support insoles fix symptoms, not the core issue.
[o1hcnwg] (score 1, diepte 5) The above commenter is a barefoot evangelist. Look for the consistent recommendation of DIY slab of leather with ropes for every shoe question.
[o1hll67] (score 1, diepte 6) Can you show me better sandal?
[o1gkz1w] (score 1, diepte 4) So this is a good point. The Chacos that I am wearing that were made over twenty years ago might not be the same Chacos that they are making today. Those Whites boots they were making 20 years ago, that cost me five hundred bucks. They were way better boots than they are making today for seven hundred bucks. 

I think thats just how it is now.
[o1gjky1] (score 1, diepte 3) I'll back that claim up, my Chacos are over twenty years old. I also live in a northern tier state where sandal weather is like three months out of the year.
[o1khzsi] (score 1, diepte 1 OP) Will give it a shot, thanks!!
[o1fmxim] (score 1, diepte 1) The other styles that have are very supportive too! I have a pretty minimalist strappy leather sandal that has great support.
[o1hmggc] (score 1, diepte 1) I have the classic Chacos and found the support is too much for my flattish feet. It's really too bad because I like other aspects of the sandals.
[o1g261l] (score 1, diepte 2) Can you tell me more about this? I’m not sure what that means.
[o1ki54t] (score 1, diepte 1 OP) Used to have a pair of birkies but the arch was very high and hard, and it hurts.
[o1g1fpm] (score 1, diepte 1 OP) Thanks, I'll look for some to try for fit! Place I went to didn't have a lot of options sadly
[o1g3gb5] (score 1, diepte 2) Tbh with this style id just go for PPE footwear: they are like $50, preferably go for brand that manufactures locally instead of Asia like Keen. Make sure that you go for soft toe version; TPU/rubber soles are preffered over PU, but upper will fail first anyway.
[o1phxxz] (score 1, diepte 1 OP) Looking for something with straps!
[o1h8918] (score 1, diepte 0) Try the Easy Spirit brand, they have good arch support.
[o1i8htf] (score 1, diepte 0) Another vote for Birks
[o1iaa48] (score 1, diepte 0) I know you tried tevas but did you try the Teva Tirra? I have those and they have great arch support. My current ones though are about 5 years old. I expect them to last a few more years since my last ones did.
[o1iekow] (score 1, diepte 0) Oofas
[o1jgt6f] (score 1, diepte 0) 1. Archwear by Powersteps 2. Archies 3. Olukai
[o1l3onf] (score 1, diepte 0) Re: arch support, I'd seriously consider whether you need it.

https://runrepeat.com/arch-support-study

>I think long term they cause more injuries than they cure. - Paul Giblin (Running Coach)

>I don't think anybody needs a lot of arch support. Instead, most runners need to strengthen the arch and surrounding musculature to withstand the stress of running. Putting an insert underneath the arch impedes its function and acts as a crutch - restricting necessary movement and allowing the arch to weaken over time. - Jason Fitzgerald (Coach)
[o1lmgmf] (score 1, diepte 1 OP) You make a good point. I was using orthopedic shoes as a crutch. I used to do exercises to strengthen the arch and you know...over time I got lazy and it collapsed. Might go back to doing my exercises
[o1phpu5] (score 1, diepte 1 OP) Ooh first time I've heard off them, will give it a look!
[o1nw9aq] (score 1, diepte 0) Keen. They are surprisingly long lasting
[o1fz5lv] (score 0, diepte 3) 1. In theory all shoes can be resoled, but in practice PU will die due to hydrolysis, and resolling of fully synthetic shoes is rarely worth it.
2. Argument "you gotta pay for the quality" doesnt apply in this context:
- it assumes linear correlation between the price and quality which is simply false, especially in the context of brands owned by conglomerates(like Chaco)
- it assumes that product in question is fairly priced. Synthetic ones go for like $20/pair.
[o1h4hs2] (score 0, diepte 4) I am not sure what you are rambling about, but do you even own a pair? I do, and I’ve been wearing the same pair for the last 6 years. Their midsoles look and feels as good as day I bought them. I am not sure what type of sandal you recommend, but I can almost guarantee that it will not feel MORE comfort or LAST longer than my Chacos. There are other metrics which would carry subjective merit but as far as longevity, you will not do better than Chacos.
[o1h8lnu] (score 0, diepte 5) With synthetic/budget footwear we should be talking more about types, rather than brands: its standart practice for the same shoe to be sold by multiple brands with little to no changes, only diffirence being logo, and the price(well, thats what by definition final form of capitalism looks like). I have experience with other comparable models. Shoes with PU may last more than 5 years, but not in the context of daily hard use. Im not dening your experience with Chacos, Im saying that there are better options.
[o1gz0dt] (score 0, diepte 2) They can be found on sale for much less than MSRP. Bought my wife a pair for 70% off at a Shoe Carnival.
[o1gljyd] (score -1, diepte 5) Whites is owned by ABC Mart: amongst the others they also have Danner.
[o1fsjc9] (score -4, diepte 1) Owned by LVMH, id stay away from them.
[o1g1jmd] (score -5, diepte 3) I dont doubt that they were making good shoes 15 years ago. I doubt that random company owned by Wolverine corp, selling $20 sandals for $130 makes good shoes
[o1ftrfn] (score -5, diepte 0) Perect sandal has been already invented: its a slab of veg tanned, leather straps, and glued rubber sole. Search for cobbler on olx/marketplace/similar(idnt pay more than $100/pair), but design is so simple that you can DIY it yourself. As a pearson with fleet myself I found minimalist footwear to be the most comfortable.
[o1gzj80] (score -7, diepte 3) Still, wouldnt pay more than $20.
[o1fsfny] (score -16, diepte 1) $100 fir synthetic sandals is unfunny joke.

=== THREAD 1jvzu68 ===
SUBREDDIT: r/Frugal
DATUM: 2025-04-10  SCORE: 13  REACTIES: 59
TITEL: Ripping holes into shoes - the frugal thing to do?
POST (source_id=post):
Hello all. I am having a shoe issue. I don't know what's wrong with my feet but I manage to tear holes into insoles as soon as I start wearing any pair of shoes for any real amount of time. Every pair of shoes I've bought has been worn to the midsole within a year or less. I thought maybe this was the quality of shoes I was buying (cheapo 35 buck shoes) so when the last pair wore out, I spent a bit more (50 bucks) on a better brand and quality shoe. The same thing is happening.

TLDR: My question is what can I do about holes in shoes? I don't want to keep buying new shoes every 6 months. Is there a way to repair them or protect them from being ripped up by my (apparently alien) feet? Should I just buy the 100 dollar shoes?

Thanks y'all

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mmed83k] (score 111, diepte 0) Unfortunately shoes wear out in 6 months to a year. Also 50$ for a shoe is cheap in my opinion. I usually spend around 100$.

You can buy two or three pairs and rotate them and they will last longer that way.

Or buy an expensive pair that you can get resoled
[mmed028] (score 40, diepte 0) I would make sure that your shoes are the correct size so your feet can't move around which can cause friction and form holes. You can also buy new insoles for pretty cheap which may help you out.
[mmeescv] (score 30, diepte 0) I think you should see a podiatrist to see exactly how you’re walking and what’s causing the holes.
[mmeqiom] (score 29, diepte 2) More expensive shoes are often more expensive because they use higher quality materials. I think (to a certain point; I'm not talking about Manolo Blaniks or Air Jordans) that the saying really is true: don't scrimp on the things that go between you and the ground. 

I'm a woman. I have a pair of $150 Dansko walking shoes that are right on the line between dressy and casual that I bought a year ago and I have worn almost every day for hikes, going to museums, going out to lunch, (I was traveling in Europe for 2 months) and they look absolutely new and feel great on my feet. I have no plans to replace them. They aren't dressy enough for wearing to a fancy restaurant -- so I also travel with dressy sandals.

Good shoes are on that list of things that are worth investing in.
[mmee34l] (score 28, diepte 0) I think $50 is still too cheap, but failing that, swap out the insoles. Replace the insoles when they wear and not the shoes
[mmegfvr] (score 23, diepte 0) There’s not much difference between $35 shoes and $50 shoes. That kind of price difference is negligible and mainly at the whim of the retailer.

The Boots Theory applies - rather than $35 or $50 shoes, go to a reputable store that caters to athletes and mobility needs and tell them what your issues are and what you want - quality shoes with a removable insole. Spend decent money on the shoes and just get insoles from the dollar store as they wear out. The shoes will last way longer and the insoles won’t be as much of an issue.
[mmeun8f] (score 21, diepte 2) I was buying $40 - $50 shoes off of Amazon for a few years because I could not afford anything more. I worked an office job, so I was buying some casual "dress sneakers." They all wore out within a few months of wearing them. Either tearing at the sides where my toes bend, or the sole would fall off the shoe. 

After several rounds of this, I bought some Cole Haan shoes that normally run for $180 & were on sale for $110. Even on sale, it was really stretching my budget. But those shoes have lasted me nearly 2 years now. I would pretty much spend the same amount ($100 - $120) split up over a few months on shoes. So now, I just buy slightly more expensive shoes & save up for them instead of cheaping out.
[mmepooo] (score 20, diepte 2) “The reason that the rich were so rich, Vimes reasoned, was because
they managed to spend less money. 

Take boots, for example. He earned thirty-eight dollars a month plus allowances. A really good pair of leather boots cost fifty dollars. But an affordable pair of boots, which were sort of OK for a season or two and then leaked like hell when the cardboard gave out, cost about ten dollars. Those were the kind of boots Vimes always bought, and wore until the soles were so thin that he could tell where he was in Ankh- Morpork on a foggy night by the feel of the cobbles. But the thing was that good boots lasted for years and years. A man who could afford fifty dollars had a pair of boots that’d still be keeping his feet dry in ten years’ time, while the poor man who could only afford cheap boots would have spent a hundred dollars on boots in
the same time and would still have wet feet. This was the Captain Samuel Vimes ‘Boots’ theory
of socioeconomic unfairness.”  - Terry Pratchett
[mmed7wc] (score 13, diepte 0) maybe get a referral to a podiatrist or visit a specialty/prescription shoe store so that they can determine what will work best. It can be bone structure, gait, or a million other reasons...
[mmehbss] (score 13, diepte 0) Good shoes are expensive. And no shoe is made to wear every day. You should have at least two pairs to wear in rotation allowing one pair to rest for a day.
[mmf2kxm] (score 11, diepte 2) You can also replace the insoles in most shoes. Buy better insoles - perhaps go to good feet or similar and find some meant for the way you stand walk and where you put pressure. Replace those regularly as they begin to wear.
[mmejqpx] (score 8, diepte 0) My shoes cost a fortune (well to me, $200 a pair) and I get about 4 months out of them. I have serious foot issues and this is the cost of my mobility. Do not mess around with bad shoes or the wrong shoes. 

It’s my one extravagance, because if I can’t walk, I lose so much of my life.
[mmen7kh] (score 7, diepte 1 OP) I'm not sure why I thought shoes lasted longer than that tbh. Do the 100 dollar shoes offer more value in another way, even if they don't last any longer?
[mmeha3q] (score 7, diepte 0) It's just the insole that's getting a hole? If so, replace them. I routinely replace mine. There are dozens of styles to pick from.

I actually prefer the simplest, no gel, no contours, padded type.
[mmeukqv] (score 6, diepte 2) Yeah your back is less likely to get fucked up when you inevitably wear down the low quality foam.

Don’t skimp on the things that separate you from the ground: shoes, mattresses, and tires
[mmeho2p] (score 5, diepte 0) I think like others said, see a podiatrist and make sure there’s nothing odd going on. $50 shoes will probably last about 6 months if you’re using them routinely. I wear a pair of Brooks and they last me about a year with 5 sometimes 6 day a week wear. They’re about $100 but they’re the most comfortable sneaker and they last well. Brooks also has a test on their site to recommend you a style that fits you best, I take that and then search for them from other retailers at a discount. If seeing a podiatrist isn’t something you can afford check out a local running shoe store, stores geared towards that (not a chain that also sells running shoes but a store for running shoes) usually have a good understanding of fits of shoes that work best with your wear patterns.
[mmeoqbn] (score 5, diepte 0) I swear, I'm not insane, but boots are the answer 

I started buying boots. Nothing less than Carolina or Georgia quality, and spending no less than $250 on a pair. Then I add a $50 insole like a Sole or Super feet that is made to last.

How is that frugal? I'm spending $300 on a pair of boots that last 5 years+ without issues. I have have my 9" logger Carolinas for 6 years, no issues. Thorogood 8" crepe sole for 3 years, no issues. $600 between them, but that's $50 a year for each boots. And they're able to be resoled, meaning that if i wear out the sole itself, a new one can be added relatively cheaply! 

A note about crepe soles. They wear out faster than normal soles, so only get them if you need them (like you stand on concrete all day) and if you don't need ANY slip resistance
[mmehynh] (score 4, diepte 1) This! And spend +100, and they’ll last for several years.
[mmevdmm] (score 4, diepte 1) I agree. I have about 5 pairs of shoes I wear in regular rotation these days. I found that has really helped with keeping my shoes in good condition for longer.
[mmejgva] (score 4, diepte 0) There are brands of shoes, which you can expect to last for a long time, but they are unlikely to be had for 50 bucks. What you are looking for is something designed as a work shoe. Preferably leather. Typically, places that sell these shoes would be specialized shoe stores. They will make sure the shoe fits well, provide you with tips how to maintain them, etc. Might even give you warranty. But it will cost you. But then again, it will last.
[mmeoodx] (score 3, diepte 1 OP) That makes a lot of sense. I've never heard of the Boot Theory though, what is that?
[mmeq6ex] (score 3, diepte 2) The Sam Vimes Boot Theory of economics, from the novels of Terry Pratchett. A poor man buys a $20 pair of boots because it’s all he can afford, and in 6 months he wears them out and needs to buy a new pair, while a rich man buys a $100 pair of boots and then last him 10 years. Hence, the rich get richer by *not* spending money, while the poor have to spend and spend.
[mmegvfl] (score 3, diepte 0) Go to a running store and get fitted. Fits are usually free if you buy a pair of shoes. You’ll know what fits you well. I did this 20 years ago. Def worth it.
[mmel9xk] (score 3, diepte 0) This is likely the way you are walking. You should see a podiatrist for sure. Because if you are wearing them that fast you may be having a gait issue or something else is going on that will affect you further down the road.

You should also try buying shoes that are $100 or get a pair that costs more on sale from somewhere, but first go to the podiatrist to see what you need. There's not much difference between a $35 pair of shoes and a $50 pair.
[mmeqapc] (score 3, diepte 0) fwiw - we have a couple shoe dryers and it’s habit to put shoes on them every time we come home. 

is mostly to minimize bacterial odor, but would probably be equivalent to rotating two pair for longevity too.

isn’t the rotating pairs a leather shoe thing? does it do anything for synthetics?
[mmeqhgg] (score 3, diepte 0) I grip when I walk and run. I shred insoles. 

Got running sandals to fix most of it
[mmew9hz] (score 3, diepte 0) 30-50 is cheap for shoes, but a single year is still too short for this imo. this typically happens for people who need medical insoles (for example due to flat feet). your feet aren’t shaped in the way the shoes are built for, making specific areas wear down much faster. see a doctor and get some custom insoles, you’ll have to get new shoes to fit them (they increase the shoe size you need typically) but will save future shoes from the same fate, as well as generally will be good for your feet’s health
[mmeyqlm] (score 2, diepte 2) Yes, they are much better for your feet and body overall. I walk a lot at work and in general and having supportive comfy tennis shoes makes a huge difference. They last a bit longer too, but not crazy so.

I’ve always heard it’s important to spend money on high quality points of contact with the ground. Shoes, mattress, tires. It will save your body over the years
[mmfe6wc] (score 2, diepte 2) More expensive shoes made via certain techniques may last longer or are designed to have the parts that wear out easily replaceable. $100 does not reliably get you a good shoe anymore, though. 

A ballet flat, like the dancing slipper it evolved from, isn't going to last, but a decent leather oxford should have more toughness and be repairable. 

Brands like fluevog have a year's warranty plus an in house cobbler service - that's part of their excuse for charging that much.
[mmfak7o] (score 2, diepte 1) I have shoes that are years old, I wear them almost every day, and not really any holes or other issues, although the soles are definitely lower on tread but not completely worn out yet. I don’t think it’s normal to wear out a pair of shoes in 6-12 months unless you’re walking or running a 10k a day 😅
[mmgfr98] (score 2, diepte 1) ??!!  My current rotation of Converse were bought secondhand in 2013 at the latest!!  They are nowhere near worn out.  Maybe I'm an outlier as I always have several pairs of whatever type of shoe in rotation, so each pair lasts a long time?
[mmex1zx] (score 2, diepte 2) Yes then watch the sales
[mmek0k9] (score 2, diepte 0) The frugal thing to do, in my opinion, is get a pair of Salomons for $150. They’ll probably last you 18 months.
[mmekio3] (score 2, diepte 0) Get a consult with a podiatrist to see if there's an issue 

Make sure you're wearing clean socks 

Make sure you're buying the right size of shoe and tightening them properly 

Invest in some gel insoles. They're worth every penny
[mmel2fs] (score 2, diepte 0) Go see an orthopedist and get a gait analysis. Something is very wrong. 

Source, I’m a nurse.
[mmeoec2] (score 2, diepte 0) I once have an ex that would wear holes in the tips of her shoes, but on the top, and it was due to the shape of her toenail of all things, sometimes you just get bad luck lol
[mmg29wv] (score 2, diepte 0) What are you wearing?  How much do you weigh?  How do you walk?

If you can't get insight out of those questions, go see a podiatrist.
[mmggsgx] (score 2, diepte 0) I walk about 10-15 miles a week for work, plus normal daily use, and have to replace my shoes every 3-4 months. And they’re $150 for a pair. I wear them every day because otherwise my hips hurt. It’s annoying.
[mmho91g] (score 1, diepte 3) For work and other non-outdoor activities I found my tieks held up reasonably well. I’ve worn them out from 7 years but about 4 years was daily wear. I’m not sure the brand surcharge is worth it, but maybe a comparable brand of leather soled shoes for general low impact wear would be worthwhile.
[mmfhc92] (score 1, diepte 2) It might depend on what you’re wearing them for also. Investing in a good pair that can be resoled by a cobbler might be worth it in the long run.
[mmgg93n] (score 1, diepte 2) I mean if you have several shoes and each pair lasts a year, yeah duh you’d still have life left in years later. I even offered multiple pairs of shoes as a method for extending life.

But also I’d wager they are not offering good support anymore (not that converse ever offered much support), even if they look fine
[mmgh5ku] (score 1, diepte 3) I have custom orthotics, so my feet are well supported in all my Converse and sandals and workboots and flat laceups etc.
[mmgidoc] (score 1, diepte 4) Ok then I would argue that your customer orthotics are extending the life of your shoe. Same as other commenters recommending insoles. You probably should have mentioned that when arguing that shoes last years
[mmgiqkn] (score 1, diepte 5) Aha!  Never thought of that, thanks!  I have mentioned them being the thing if people say they find Converse uncomfortable.
[mmg0971] (score 1, diepte 1) Also, if you work in an office environment, have work shoes that stay at work. Wear tougher shoes for commuting, shopping and traveling around outdoors, and then change into your work shoes when you get there. Keeping "indoor only" work shoes allows them to last for many years.
[mmeqbap] (score 1, diepte 0) Sorry but $50 is still cheap shoes. You’re going to have to spend a couple hundred if you want them to last.
[mmewndl] (score 1, diepte 0) Do you wear socks? Do they get holes fast too?
[mmexops] (score 1, diepte 1 OP) Yeah I've got socks, they don't wear down as quickly, but I also have a bunch of them, so they don't get the same amount of wear and tear as the one pair of shoes
[mmf9x3k] (score 1, diepte 2) Maybe get two pairs of shoes and rotate them so one gets a break/dries out well etc while you are wearing the other. Are they wearing from the inside to the bottom or the bottom up? If it’s from inside take out the insole and put in a new one. $10-$15 and they will prolong their life. You must be on your feet a lot.
[mmex663] (score 1, diepte 0) 1) Get two pairs of shoes and alternate days wearing them.  

2) What part of the sole is wearing?  That might indicate what is going on and dictate a shoe that fits your foot better.
[mmey919] (score 1, diepte 0) This sounds more like an alignment issue with your body. If your shoes are getting worn out what's potentially happening with your joints and bones? Visiting a reputable chiropractor would be my first step, no pun intended!😆  Take your shoes with holes in so they can see them during the consult.
[mmf2s61] (score 1, diepte 0) Replacement insoles are so cheap
[mmf8hai] (score 1, diepte 0) If you are paying for quality not trend a higher end shoe has additional padding and more current technology such as shock absorption and arch support.  If it’s more expensive due to trend, then there is likely no advantage to quality.  Look at a shoes Seams and sold quality to get an idea.  
Like crocs are priced for trend.  There are a ton of similar material shoes way cheaper that are virtually the same.  When it comes to exercise shoes there can be a difference. Padding, cushioning, water protection etc.
[mmfihgm] (score 1, diepte 0) Is it only one shoe? Do you get in and out of your vehicle a lot? I know cops get a hole in the left where the ball of the foot is from a twisting motion getting into the car
[mmfjfzn] (score 1, diepte 0) Just to make sure, your not wearing the shoes 2 days in a row, right? Cause not letting them dry out will add to the destruction. 

Otherwise, better insole, check sizing, and $50 shoes are still considered very cheap. Tbh shoes are just cheap trash now, even if you spend hundreds. They should be lasting longer, but don't expect shoes to last years anymore.
[mmfyaye] (score 1, diepte 0) The real answer isn't technically frugal, but seeing a podiatrist is what you need to do. You probably need some expensive custom insoles to correct your gait. 

No Dr Scholls or expensive shoes will solve your issue. Holes getting worn into shoes so quickly, generally means you walk weird or are very gard on your feet somehow.
[mmg6vss] (score 1, diepte 0) If it’s just the insoles, you can just replace those only. If you are burning through the soles that fast too, then I think you should look into whether you are wearing shoes fit for the task (hard work requires hard shoes, and gravel/concrete will tear through softer shoes and flip flops pretty quick. You may also want to try to see a podiatrist to see if there’s something odd with your feet or gait that is causing you to wear through your shoes faster than normal.
[mmg9o9i] (score 1, diepte 0) Just keep ripping out the worn insoles and replace them.  Insoles are cheap
[mmfj8od] (score 0, diepte 2) A year ago, someone on this sub got irked with me because he was sick of seeing Vimes's Boot Theory making the rounds, and I posted it. In this case though, it literally applies! (Suck it, random redditor from a year ago!)
[mmephp6] (score -1, diepte 2) Vimes Boots Theory. From Terry Pratchett’s Discworld books. Should be enough to google.

=== THREAD 1dsdh1y ===
SUBREDDIT: r/VetTech
DATUM: 2024-06-30  SCORE: 36  REACTIES: 59
TITEL: Best shoes for being on your feet 10 hours a day? 
POST (source_id=post):
Like a lot of techs, I work 10-4hr shifts a week. Any advice on shoes? Insoles? I am chubby and have widish feet.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lb1p0ts] (score 48, diepte 0) hokas
[lb1sgp2] (score 26, diepte 0) Cloves. Plus they are waterproof and wipe clean
[lb2d2rg] (score 22, diepte 0) TBH, what helped me more than any shoe was compression socks!
[lb1tazt] (score 17, diepte 0) I live in ASICS
[lb1qty0] (score 15, diepte 0) Hokas hands down. They're the only shoes that don't make me want to chop my legs off
[lb23knm] (score 13, diepte 1) Second this! I have awful knees and hokas are the only ones that help them from hurting. Won’t buy anything else now!
[lb26qvb] (score 13, diepte 0) Crocs Idc how stupid they look, anything else will have my feet hurting at the end of the day except for crocs(never tried hokas but every other tennis shoe I have tried)
[lb2gppv] (score 8, diepte 1) This^. I'm a runner and Hokas are the only shoe I will run in. I used to wear crocs to work but as I get older my knees are also getting older so now I have several pairs for running/working/walks etc..
[lb1u9r7] (score 8, diepte 0) Hokas for the win! I've tried them all: Merrell, Asics, Brookes, Cloves, New Balance, Sketchers and I've come back to Hoka. Expensive as shit but they'll save your back, knees and feet - coming from an RVT of 27 years.
[lb24v2e] (score 8, diepte 0) i have plantar fasciitis and issues from standing on hard surfaces and brooks glycerin 21 is the shoe that saved my life but most of my coworkers wear hokas or the on running shoes? :) I wash mine biweekly to ensure theyre clean… 😭
[lb1ymqs] (score 7, diepte 0) Brookes! I have the glycerin 20 which are their super cushiony ones. I have really flat feet so I can’t do a lot of shoes but these literally feel like clouds
[lb22ut6] (score 7, diepte 0) im an outlier, but ive been wearing steel toed timberlands for a while! i work in shelter med as a surgery tech, and they're very comfortable for the amount of manual labor i do each day.
[lb230oo] (score 7, diepte 0) Hokas! They feel great, and the bounce of the shoe has kept up. I've tried Asics and Brooks, but the thicker sole/base of Hokas really has made a difference.
[lb1t85t] (score 6, diepte 0) Oofos!
[lb1zrtt] (score 6, diepte 0) Xeros! I have been wearing them since 2018 and I refused to wear anything else.
[lb3ynpt] (score 5, diepte 1) Hokas is what I wear now and wish I had worn them earlier.
[lb4wg6z] (score 5, diepte 1) I switched to hokas in GP and I am returning back to EC in a month- they work woooonddeers
[lb33wtx] (score 5, diepte 0) My suggestion instead of shoe brand is to find a good shoe store. Not famous footwear bullshit, but a serious running store.

They'll measure your feet exactly, watch how you walk, where you put your weight when you're standing vs walking. It'll take about 2-3 hours the first time for the fitting, sizing, and try outs, but they keep those measurements on record. 

I'm wearing Saucony right now and they're the best and most comfortable shoe I've ever worn. I work at an open intake high volume shelter, so very little downtime. They hold up to Rescue better than any other shoe I've had, and if you have to clean a kennel, they dry super fast.
[lb1msnt] (score 4, diepte 0) I have a pair of oncloud novas I really like but I’m not sure how long they’re going to hold up. I’m also a bigger girl with wide-ish feet. I had cloves but they were just not it for me. I have two coworkers that have hokas and they swear by them.
[lb26v6q] (score 4, diepte 1) second them. i have had a pair for about 2 years now. love them and totally worth the investment
[lb2b2uo] (score 4, diepte 1) Same. I need wide and just size up 1 and it’s perfect
[lb278cz] (score 4, diepte 0) I looove my cloves!! Expensive but worth it. I have a heel spur and plantar issues and they’re so great!
[lb3xw4j] (score 4, diepte 1) I love my compression socks
[lb2glmf] (score 4, diepte 0) Love my Dansko’s
[lb317k6] (score 4, diepte 0) I used to be a Skechers girlie until I finally gave in and got Crocs. It's now Crocs for me.
[lb5urgx] (score 3, diepte 1) I wore Danskos for years and they saved my knees, but they are kind of hard to maneuver in.  Walking dogs around the yard (on a hill with some ruts) was a struggle, and I rolled my ankles on a regular basis.  Also they are not meant for walking backwards!!

I wear Hokas now, but I did love my Danskos when I used to wear them, even with the ankle rolling!
[lb2hd8j] (score 3, diepte 0) Any stability running shoes such as Asics Gel Kayano, Brooks Adrenaline, Saucony Tempus. Etc.
[lb2ugfr] (score 3, diepte 0) Cloves everything else is inferior
[lb2y75w] (score 3, diepte 0) All my coworkers wear Cloves, some Hokas, and me and one other person really like our Balas!
[lb2zz68] (score 3, diepte 0) My orthopedic surgeon recommended brooks after an ankle fracture and I haven’t gone back! Hokas don’t really do it for me like they do everyone else
[lb38xhb] (score 3, diepte 0) Go to a really good sports shoes store (I’m in Australia - I go to “athletes foot”; or sometimes you can find shoe shops run by podiatrists that are great) and ask them for the comfiest nursing shoe they have and say you don’t care what they look like, you just want to be comfortable. Mine gave me black leather brooks sneakers (brooks is generally a great brand to check out) that are the *ugliest* shoes you’ve ever seen in your LIFE…but my feet have never ever hurt at work ever since I got them. I’ve had plantar fasciitis before and my feet have always hurt when having to stand for a long time and it’s just not a problem for me anymore at all. When I was doing overnights in emergency I used to combine them with nursing compression socks as well and the comfort is next level 💃🏻
[lb3zb6q] (score 3, diepte 0) Dansko clogs
[lb1vyno] (score 2, diepte 0) Hokas are great but I prefer my Ugg Tasman clogs. They’re rubber so perfect for unexpectedly getting peed on.
[lb2bb46] (score 2, diepte 1) I tried my xeros working ER and it’s Killed my feet. :( love them for everything else
[lb2get7] (score 2, diepte 2) I started wearing them in ER. They killed my feet at first because I wasn’t used to minimalist shoes, but once I got adjusted to them my knee, hips, and back thanked me.
[lb2n03p] (score 2, diepte 3) It was so bad I couldn’t stand otherwise I might of kept trying.
[lb21sg1] (score 2, diepte 0) Nike Tanjun with compression socks
[lb2a5vu] (score 2, diepte 0) Hokas 🙌
[lb2aqf6] (score 2, diepte 0) Hokas!!

I’m fifty-something and for the first time in my life my feet don’t ache at the end of the day.
[lb2azuy] (score 2, diepte 0) Brookes
[lb6ifnd] (score 2, diepte 1) Sammmeee
[lb6nmm2] (score 2, diepte 1) I love my Danskos, too.  I've stepped away from the clogs and do the waterproof sneakers.  With compression socks, I'll never go back.
[lbbrzsy] (score 2, diepte 2) I’ve found that if I wear grippy socks (Bombas makes good ones) that I don’t slip around in my shoes and therefore don’t twist my ankle.
[lbcfxdc] (score 2, diepte 3) That's a great idea!
[lb2n0lg] (score 2, diepte 0) Good running shoes, whatever brand suits your style and budget. They are made for high impact on hard surfaces, and the soles don't crack if you kneel a lot.  I like used because they're already broke in,  but what you like best.
[lb31e0s] (score 2, diepte 3 OP) Yeah I was surprised. They just closed about a week ago
[lb31mup] (score 2, diepte 4) Guess it’s between Cloves and Hokas then!
[lb316cv] (score 2, diepte 0) I be wearing work sketchers I love them
[lb36cij] (score 2, diepte 0) I wear New Balance. Specifically the 990 V6. I used to wear Hokas, but I have a bad ankle, and my doctor said that Hokas are really bad for ankle stability because they are higher up than other shoes (because of the cushion)
[lb36s1j] (score 2, diepte 0) Danskos & compression socks.
[lb3wdsx] (score 2, diepte 0) skechers!!
[lb4cj1i] (score 2, diepte 0) Adidas ultraboost!
[lb5oucb] (score 2, diepte 0) Danskos with compression socks!
[lb69nqy] (score 2, diepte 0) Brooks, never getting any other type of shoe brand. The toe box is wider and more comfortable and I'm not wearing holes in the sides of the toe box. The glycerins are the best so far, but my coworker has the ghost and she loves them as well. Worth the price imo (but I got mine as a birthday gift )
[lb6swsl] (score 2, diepte 0) Used to be in vet med, now I work with children. I got a pair of Skechers D’lites slip ins. They’re super comfortable and great if you’re the type to slip on your shoes instead of tying your laces every time. They’re memory foam so they conform to your feet but they’re not like the typical Skechers that bust in 4 months of wear (in my experience)
[lb1lgxb] (score 1, diepte 0) Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.

Please thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*
[m2849lq] (score 1, diepte 2) Which model do you suggest? Want to buy them for wife
[m284avq] (score 1, diepte 2) What model?
[m28ftf0] (score 1, diepte 3) I wear Hoka Bondi 8
[lb1ybxh] (score 1, diepte 0) Lol idk myself I have big feet soo I can't help you in this race.
[lb2zy6n] (score 1, diepte 1 OP) I looked for Balas and according to their website, they're shut down :(
[lb31aeq] (score 1, diepte 2) What no way! That’s sad
[lb33k2q] (score 1, diepte 0 OP) Thank you, everyone, for your input! I am considering the following: 

[Glycerin 21 from Brooks](https://www.brooksrunning.com/en_us/womens/shoes/road-running-shoes/glycerin-21/120408.html)

[Supercush Forte from Clove ](https://goclove.com/products/clove-forte-womens-sand-light-blue?variant=40072657207354)

[Kuru Kintetic 2.0 ](https://www.kurufootwear.com/products/womens-kinetic-wide-2-brightwhite-bluefog)

I actually have a pair of Hokas bondi 8 in wide. I do like them, but I'm starting to get so much heel pain in my left foot :(

