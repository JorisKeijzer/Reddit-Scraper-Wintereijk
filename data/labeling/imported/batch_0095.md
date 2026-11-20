# Label-batch batch_0095

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
Schrijf het resultaat naar `batch_0095.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: omt709, 81qdgf, 8nwzdn).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD omt709 ===
SUBREDDIT: r/running
DATUM: 2021-07-18  SCORE: 109  REACTIES: 80
TITEL: Why do doctors always recommend orthotics?
POST (source_id=post):
Every time I've been injured and gone to a doctor, they have recommended orthotics (incidentally, different types/brands every time). The running shoe manufacturers and most running advice I've read/heard claims that most running shoes are supportive enough nowadays that you don't need orthotics. So what is the reason doctors consistently recommend orthotics?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[h5nas01] (score 69, diepte 0) Maybe you need them, or maybe you're in the wrong shoes. After years of hip and knee pain, and ignoring the drs advice to get orthotics, I tried them. I was in the wrong shoes but couldn't afford new ones, and orthotics were a less expensive lifesaver.
[h5n67uk] (score 64, diepte 0) This must be a regional thing. In my town, it’s about hip strength. Uneven hip strength is the problem and strength training is the prescription. In the town in Texas I lived it was orthotics. In LA it was bone Spurs being the problem.  Multiple people in my running groups have had stories about their common diagnosis each place. You may just be in a part of the country where this is the norm. It’s sometimes practice by practice. Not regional. So ymmv. I’ve had the only luck with strength straining and rest as a solution to my issues.
[h5ny3fq] (score 56, diepte 0) Doctor here, the truth is most don’t know any better. Most of us aren’t trained that well to deal with feet and/or mobility issues, especially in healthy people. Most are either under the mistaken impression that orthotics are going to help OR too lazy to think about alternatives. Contrary to some, medical doctors do not get paid for prescribing these things so it isn’t financially motivated. 

Your best bet is physio, sports medicine or orthopaedic surgeon. Foot physio is the treatment for foot pain from running, supportive footwear can help in the meantime; you should also be stretching and massaging your soles regularly (frozen water bottle or lacrosse ball on the floor works very well for this.)
[h5n7i68] (score 53, diepte 0) I just went to see an orthopedic surgeon and he said my running shoes are good for my feet and that I don’t need the insoles I bought. Either all the doctors you’ve seen are trying to sell you on something they don’t actually sell, or maybe they all say that because you need orthotics.
[h5nlw1w] (score 47, diepte 1) Sometimes it depends on environmental factors, too. For instance, where I am in Florida, a lot of people solely (heh) wear flip flops and similar shoes with no support causing issues long term. Providers in the area might see a common issue with everyone's feet because of it, whereas you wouldn't see it as much in a place where people actually wear /real/ shoes.
[h5oniud] (score 21, diepte 2) This is so interesting because now there is a new theory that strengthening your feet and walking under your own strength is better than overly supportive shoes. Or maybe it isn't the lack of support in flip flops, but more the unnatural movement they require to hold them on? So curious on this one.
[h5ounyx] (score 14, diepte 3) It's the fact that you're curling your toes holding the flip flop in place while the whole landing of the foot is weird to also keep them on. Plus the upstream effects too the hip
Not an issue really in full sandles.
[h5njp4b] (score 14, diepte 1 OP) With the exception of a physical therapist, everyone has also told me that as long as my shoes are comfortable, there's no reason to switch. But for whatever reason, the orthotics are still essential. Seems a bit contradictory.

I should mention that I have tried orthotics and, while I will admit they were comfortable, they did not prevent injury.
[h5nm9x8] (score 13, diepte 1) If they sell them in the office.  Otherwise they don’t make money off orthotics.
[h5ontrv] (score 10, diepte 1) Podiatrists aren't MDs?!?  Mind BLOWN. I never knew this.
[h5niqg2] (score 9, diepte 0) I’ve had a couple of chiropractors over the years suggest these “foot levelers” that my podiatrist and ortho have deemed as garbage. Based on the copious amounts of literature and advertising in their offices, I have to imagine they get some type of kick back or commission from that particular company. My insurance paid for them in full so I have a pair for my walking shoes but almost never use them, they seem to do more PF harm than good. It always reminded me of going to the running store to get new shoes and trying to be sold on the extra inserts after I’ve settled on a pair. 

On the other hand, my ortho and podiatrist recommended custom orthotics for me since my arches are VERY high and I was having a lot of referred pain due to imbalances/weakness. I have to say, once I got those a lot of the things I was going to the chiro/ortho/pod stopped. I think mine is an extreme case an obviously not a generality, just sharing. Unless they’re custom, they’re usually just crap. Especially (IMO) if they’re suggesting different types/brands all the time.
[h5n749u] (score 8, diepte 0) I have not found that to be the case.
[h5not57] (score 8, diepte 0) A good podiatrist has been an absolute godsend for my ability to run long distances without excessive blistering, pain, and injury. I’d recommend and expert in the area of feet.
[h5nxjkr] (score 8, diepte 0) Not all problems are caused by support and fixed by shoes alone.

My podiatrist had be adjust the way I laced my shoes and determined I needed to wear inserts for about 12 weeks. These inserts changed the way the weight is distributed across my toes. I had a minor injury and after this time I could wean off of the inserts if I wanted.

He did sell them at his office, but gave me the name of them because they are cheaper online. He said some insurance covers them, some don’t (which I think is why they are sold at the office but that’s a guess).

I would trust a board certified podiatrist who is examining your feet over an article giving running advice. Everyone wants to run pain free, so if inserts help, great! If they don’t help you, good for you!
[h5ong1e] (score 8, diepte 1) Yeah I recently learned that podiatrists aren't medical doctors... wtf
[h5necvp] (score 7, diepte 1) That's reminds me of how different regions of the country have different methods and consequent success rates at treating cancers, hospital infections, etc. You'd think they would just pick the most successful method and everyone would be doing it but unfortunately it doesn't usually work like that in medicine. As with most things, you usually get a small percentage of people that are doing an excellent job, and large swath of people doing a mediocre/not quite scandalous job, then the lower end of that being deemed negligent
[h5ndgmz] (score 6, diepte 0) That's what they're taught in school/business, possibly 30 years ago when they were in school, and because that is part of their business model. It's kind of like how you go to the dentist because you have cavities and they try to sell you a toothbrush or whatever, even though what you really need is to stop eating sugar. The real irony is most people need less orthotics/support etc. and that's actually what's causing the problem in a lot of cases, but you can't sell that. NWfootandankle on YouTube has some good vids on this.
[h5nmfbj] (score 6, diepte 0) I went to a doctor, and all he did is suck blood from my neck. Don't go see Dr. Acula.
[h5p2rwh] (score 5, diepte 1) >LA it was bone Spurs being the problem. 

To me, this alone suggests it's anecdotal or perhaps a particular clinic over diagnosing something. Bone spurs are a relatively uncommon problem in runners, whereas strength training and orthotics are relatively common proposed solutions to any lower extremity injury.
[h5p80ik] (score 5, diepte 3) 100% correct. I’d also add that a good podiatrist can and should watch you walk and run in your running shoes during the appointment. 

When other foot/ankle issues arise, they can treat those. They should do a better job than a PCP because they’ve had much more training on it.
[h5p5wzw] (score 5, diepte 2) [Anyone can get into podiatry school. *George* got into podiatry school!](https://youtu.be/0yFEWgimK-Y)
[h5oq8h4] (score 5, diepte 1) For any issue or pain that develops from sporting activity I don’t comment about it and just refer to a Sports focused Physiotherapist or if I think the pathology warrants it, a Sports MD.
[h5njyk3] (score 4, diepte 0) They make money off of them.
[h5nouqd] (score 4, diepte 0) What doctor? Your primary care provider or a podiatrist? A podiatrist will be able to tell you if you actually need orthotics because of flat feet, collapsed arches etc. or if your injuries don’t have anything to do with the exact shape/type of your feet. 

I have very flat feet (if I walk on the beach, my entire foot is visible in my footprint) and I *need* the orthotics I got from a podiatrist. My feet swell and knees ache without them. They even improve my posture. If they were somehow taken away from me, idk if running would be in the cards anymore. 

I’d really recommend seeing a podiatrist and bringing your running shoes with you for them to look at if you haven’t, a good one won’t try to sell you anything you don’t need. (And on a related note, of course shoe manufacturers will claim that their products are so good that you don’t need orthotics.)
[h5npiig] (score 4, diepte 0) I tried every combination of shoe & orthotics I could find. I finally went with a minimalist shoe from Merrell and ran slow for about a year. Haven't had discomfort since (aside from getting old).
[h5o0nak] (score 4, diepte 0) “When you’re a hammer, all you see are nails.”

   Sure, lots of runners can benefit from orthotics and tons of padding, but I and many others just needed to strengthen our feet and run with a more natural stride and strike.
[h5o3t61] (score 4, diepte 0) Ask the PT for strengthening excercises instead and get a second opinion.
[h5nm27h] (score 3, diepte 1) Maybe go to a sports medicine doc or podiatrist or someone who works with athletes?  I think most doctors don’t have much training in chronic sports related injuries.
[h5nrrll] (score 3, diepte 2) True. The podiatrist I went to when I broke my foot sold them right out of his office.
[h5nvuzs] (score 3, diepte 3) Ok, then, I agree in that case.  Did they help you?  

I’m not sure how stark laws don’t prevent this kind of thing.  I don’t understand them very much but stark laws are in place to prevent doctors from ordering tests or treatments that financially benefit the doctor.
[h5nwf7g] (score 3, diepte 4) I didn't spend money on them. The doc suggested them but since I was in a walking boot, I didn't see the point and he never brought them up when he cleared me to ditch the boot so I figured the original time was trying for an upsell.
[h5nlg3u] (score 3, diepte 0) Because some people need them. If you have a true issue like collapsing arches or over pronation orthotics are a great way to correct the imbalance.
[h5npu6e] (score 3, diepte 1) What exactly do they do that a PT or PCP can't do?
[h5piaic] (score 3, diepte 1) (Your username seems to indicate titles are important to you, so it’s interesting you brought this up)

They are *doctors*, just not medical doctors.  They have a DPM and nowadays go through a surgical residency alongside general surgeons.   Cause I think people were confused by your comment.
[h5o7g5r] (score 3, diepte 0) I had plantar fasciitis 25 years ago and was prescribed orthotics. I have since ran 75 marathons pain free with them. The same inserts.
[h5otk2q] (score 3, diepte 0) 99.9% of people do not need orthotics or motion control shoes despite being told they do.
[h5r01vf] (score 2, diepte 3) Yeah, flip flops may be minimal, but they don’t exactly promote a totally natural walking gait.
[i2a7v7o] (score 2, diepte 3) I think it can be both. Posterior tendonitis caused my arch to weaken orthodics miraculously corrected it. Without them I could barely walk. I still have had to strength train and rehab my feet. Won't need the orthodics always however my super high arch on right foot and pronation require orthodics when artistically skating, my sport
[h5w4ha6] (score 2, diepte 4) You're spot on. 16 years old went to doctor for ADD symptoms and they gave me amphetamine salts which in turn gave me long term ADD lol. Went back to the doctor for anxiety induced by those drugs, instead of taking me off them he gave me tranquilizers/benzos to curb the edge. All i really needed was diet/exercize but telling someone that doesn't fulfill their agenda.
[h5w6l2i] (score 2, diepte 5) >All i really needed was diet/exercize

The thing that really blows my mind is that most doctors get like 2 hrs training in nutrition in med school. So it's no surprise they are focused on drugs or don't have good information about diet, it's simply not something they are trained for and yet for some reason people expect them to be experts on it.
[h5pb6yn] (score 2, diepte 2) I found that hard orthotics were terrible for my foot problems and working out the knots and stretching eventually got me back to normal.

I think orthotics are over prescribed, but you can't argue with results, if you like them. My wife doesn't run but uses them to align her knees. But other shoes with support work for her too.

When my feet/plantar fascia flare up, I take it easy, stretch stretch stretch and rely on foam shoes like crocs etc. I think ultimately stretching is the key for most of it. More flexible children don't usually have these problems, after all.
[h5ngeyu] (score 2, diepte 0) What type of doctor are you going to?
[h5nh4qn] (score 2, diepte 0) I’m not sure what you expect from them. If you get lucky and find one that’s a runner he maybe able to help otherwise, its try different shoes, orthotics or what I hear the most quit running.
[h5nl1b6] (score 2, diepte 0) I’ve had a similar experience. And the orthotics I bought made my knees hurt. I was used to less arch support. More arch support made things worse.

There is no doubt we need to replace our running shoes regularly (3-4 times per year). When they break down, our arch collapses and our leg gets out of alignment.

I stopped buying Nike Air running shoes because the air cushion would deflate on the medial side, causing knee pain.
[h5obzob] (score 2, diepte 2) Interesting. I have low arches. Essentially flat feet. But the alignment of my knee is based on walking with very little arch so whenever I wore shoes with lots of arch support or used orthotics, it made my knees hurt. And yes, I think you’re right. The science of podiatry has a ways to go.
[h5nohj4] (score 2, diepte 0) Doctor as in a general practitioner? Or specifically a podiatrist 

My understanding of orthotics is that they help with alignment (for example a collapsed arch rotates your entire foot inward which is bad for the ankles)

Next time a doctor recommends this, you could ask “what specific problem would an orthotic solve” or better yet try to get referred to a podiatrist.
[h5nqcsz] (score 2, diepte 2) It’s just another area of expertise. They know a lot more about exact biomechanics of what happens when you walk, run, etc. Also expertise in how to modify shoes and insoles to make you move in a way that avoids the problems you may experience.
[h5nrpgs] (score 2, diepte 0) Because when you’ve thrown enough shit at the wall, some of it sticks. Same premise as mentioned above with physician recommendations. I’ve worked as a respiratory therapist for almost 20 years now and have seen blanket/generic regimens prescribed to patients and some more tailor-fit to the individual. Unfortunately, some of the logic is regionally-biased, some is because trends and research constantly adjust, and the other reason (what I deem more common) is the notion that “*everyone* does it this way because everyone *does* it this way”. 

If a doctor literally guessed “orthitics” and was right at one point in time, well that’s gonna be the ace up the sleeve for the next patient that s/he sniffs to be the same
[h5nup8i] (score 2, diepte 0) Running shoes are not customized to your feet - your gait, etc. If you have a custom orthotic then your comfortable shoes are customized to your feet.
[h5ny1kv] (score 2, diepte 0) What I don’t get is the need for the fancy insoles like SuperFeet.   Why do they try and sell me these with every pair of shoes?  If every pair of shoes actually needs them, why aren’t the shoe manufacturers making better shoes?  

Custom orthotics given by a medical professional may be different, idk.  I wear an insole cut from a sheet of $2 foam in my left shoe only, because it’s an inch shorter and the imbalance bugs my hip.   But I get like six insoles from a $2 sheet so….what’s the point of $60 insoles?
[h5o6sx7] (score 2, diepte 0) check out r/footfunction if you’re still looking for solutions. that sub completely changed my life. i’ve struggled with flat feet, bad posture, neck and tmj pain since childhood, but less than a year ago i started incorporating advice from the sub into my daily routine (walking barefoot more often, physical therapy exercises to build foot strength and restore flexibility, etc) and the results have been astounding!! i am living every day virtually pain-free, which i didn’t think would ever be possible for me. good luck!!
[h5q5ah5] (score 2, diepte 1) Agreed. I've had orthotics for about 15 years. If I stop wearing them, I get plantar fasciitis pain. If I do wear them, it goes away. These are custom orthotics, not off the shelf.
[h5odda4] (score 2, diepte 0) My son gets orthotics even for new shoes. He tried running without them and said when they start to feel broken down then he’ll put the orthotics in. His knees hurt every time. His arches just need that much extra support to keep his knees happy
[h5p8k58] (score 1, diepte 2) I can’t disagree with that. The group was all middle age or close to it guys. So I could see an active lifer wouldn’t get Spurs. Good point.
[isqbtbg] (score 1, diepte 1) What kind of strength training did you do
[isqkvkw] (score 1, diepte 2) Mostly started lower body. Had to increase flexibility first. So stretching. Then hip strength. Crab walks, scissor leg raises with weights on ankles for the hips. Then I could start the real work. Bar squats, pelvic thrusts. And trunk pulls (like a two handed pull cord movement) got me feeling MUCH more balanced. What’s so interesting that my glutes were never really working before. Did so much work with the thighs that my ankles and feet were taking a lot of impact that my glutes could have helped with. I’m much more balanced now and don’t know how much was stretching vs lifting but combined it’s completely changed my perspective on lower leg pain and foot discomfort.
[h5q3x7d] (score 1, diepte 2) I think you're getting medicine confused with online forums like r/running.
[h5telgc] (score 1, diepte 3) Unfortunately it happens everywhere, medicine or not. I always try to remember there was a time when most doctors not only smoked cigarettes, but plenty actually recommended and shilled  them.
[h5o07q5] (score 1, diepte 1) I had the same issue. High arches and I basically got trapped in an orthodics cycle. Eventually, I found a physio that specialised in feet and he gave me exercises on foot strengthening and showed me how to tape my foot when in pain. That helped a lot. After a while, I switched myself to barefoot shoes and that helped me the most. YMMV. I really don't think the science of foot mechanics is as far as podiatry and orthopedic surgeons believe it to be in.
[h5oe9sj] (score 1, diepte 3) I think the foot physios seem to have the most knowledge so long as they're not selling you anything.
(24 reacties met lagere score weggelaten)

=== THREAD 81qdgf ===
SUBREDDIT: r/Teachers
DATUM: 2018-03-03  SCORE: 17  REACTIES: 78
TITEL: Teachers, what kind of shoes do you wear to work?
POST (source_id=post):
I am new to the profession and feel like my shoes are always the downfall of my outfit. I am not one to wear heels, I have tried a few times but halfway through the day it feels like my feet are going to fall off. I tried ballet flats, but they always rub the back of my heels raw. Lately I have settled on what I think are semi professional sneakers. I am much more comfortable and happy in those. I am interested to hear if others had any suggestions!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dv4dpwo] (score 16, diepte 0) If you want to wear flats, save up and splurge on a pair of Tieks. I’ve got two pairs and after four years they still feel like walking on clouds. 

edit: yes, they are pretty goddamn expensive, but worth it. Seriously. Italian leather is like butter.
[dv4cjzb] (score 10, diepte 0) Sneakers. 

Starting at 37 weeks pregnant I wore slippers and no one cared. I probably could wear slippers all day forever as long as I stay in my classroom.
[dv4cug2] (score 9, diepte 0) I generally did flats or Vans sneakers. My kids really paid attention to shoes, and thought it was cool I wore the same kinds they did.
[dv4dil1] (score 9, diepte 0) I have cranky high arches and have had success with Vionic, Birkenstock, Allbirds (slip on, not sneaker), and doc martens Chelsea boots with orthotics for support. I’ll occasionally wear low profile white sneakers in the spring.
[dv4cxdk] (score 7, diepte 0) I have three different colored pairs of converse with insoles for support in them. I can walk around my classroom all day and be fine! I got ones that are our schools color and wear them on Friday’s when we have to dress in school attire.
[dv4dyoc] (score 7, diepte 0) I love wearing Toms and birkenstocks to work. I love fashion and dresses so sometimes, I wear lower, wedge heels. Bridgeport comes up with some comfortable designs. Then, I always bring a backup pair of flats in case I have to switch them up. I avoid hard leathers for flats because they take too much to work them in. AND FLAT BOOTS! I live in Canada and outdoor recess supervision is so much easier when I just wear a pair of boots instead of shoes.
[dv4ezu9] (score 6, diepte 1) This is so true, classic Adidas are in, so are Chucks. I usually wear flats like [these](https://www.payless.com/product/75884.html?dwvar_75884_color=black) because I find them comfortable and they go with most of my outfits. However, kids definitely take notice if you’ve got on cool, trendy shoes.
[dv4nd7f] (score 6, diepte 1) Holy cannoli! I just looked them up. I don't think I can spend $200-300 on flats! Do they last forever?
[dv4dm0w] (score 5, diepte 0) My favorite pair are Red Wing boots, worth every penny. They are comfortable and they look professional.
[dv4f8j6] (score 4, diepte 1) Came here to recommend Tieks. I have yellow (school colors are blue and gold) and a rose gold pair that go with everything. The customer service is amazing at helping you find the perfect fit. Mine took me a few weeks to break in on one spot because I think my right foot is a tiny bit wider than my left, but after that they are molded perfectly to my feet! I wear them with skirts, jeans, leggings, slacks... and they feel amazing!!
[dv4k2xf] (score 4, diepte 2) They definitely are. And nice username!
[dv4jrlh] (score 4, diepte 1) Tieks are definitely worth the money. I held out for a long time before I got my first pair, but then I got a second color within a year. My husband got them for me for Christmas!
[dv4goba] (score 4, diepte 0) Sketchers.  Have sneakers to casual dress by them and they're great.
[dv4i25n] (score 3, diepte 1) I wear vans too. I have a couple pair of Toms, but can’t wear those every day.
[dv4d44h] (score 3, diepte 0) I wear keds, boots, or comfy ballet flats (when it’s warm out). Last year I wore Converse a lot.
[dv4d6fm] (score 3, diepte 0) I wear slip on Vans pretty much every day. I stopped wearing flats my last trimester of student teaching five years ago. No one has ever had any issues with my shoes. Wear what’s comfortable for you.
[dv4no0c] (score 3, diepte 2) Yes! I’ve had mine for four years and aside from a little cosmetic wear, they’re as good as the day I bought them. Trust me, it’s an investment you’ll thank yourself for...
[dv4lkri] (score 3, diepte 1) I same with Toms! I have a few pairs and works with dresses or pants.
[dv4f479] (score 3, diepte 0) Redwing boots
[dv4f8ni] (score 3, diepte 0) Blundstones — super, super comfortable!
[dv4h2sy] (score 3, diepte 0) I mostly wear Keds and Toms, and then some boots with no/low heels. If I want some heel, I usually pick wedges since they are way more comfortable than high heels. I save high heels for only a few days of the year when I want to be extra fancy!
[dv4jrzt] (score 3, diepte 0) Sanita professional clogs, my friend. I can easily move all around the classroom all day, and I have no foot/leg pain at the end of the day. (Dansko makes them, too.)
[dv4k8ku] (score 3, diepte 0) I generally wear Sketchers Go Walk. I think I have the Go Walk 2s. We aren't allowed to wear sneakers at my school, but since mine are black and I wear black socks, no one has really noticed. Really comfortable.
[dv59c06] (score 2, diepte 1) That’s definitely my winter choice, but as soon as it’s above 10C I live in my birkenstocks :)
[dv4fsv5] (score 2, diepte 0) Keds
[dv4g3l7] (score 2, diepte 0) I wear Dansko, but not the clogs, a heel style, most of the time. I also wear cowboy boots on occasion (Texas girl here). I'm not a huge fan of flats, oddly enough. They end up really hurting my heel and making my plantar faciatus flare up. Same with vans. I use aot of insoles in most of my shoes.

Don't be cheap with shoes. That's one thingive learned. I am saving up for Tieks and some other high quality pairs because I am tired of being in pain.
[dv4gqx4] (score 2, diepte 0) I have flat feet, but my outfit is usually dressy jeans and a shirt+tie so I try to wear my wingtips as much as I can...

On lab days when I am going to be standing for 8 hours straight I have some super comfy black sneakers with amazing arch support cause feet pain is no joke
[dv4hj9m] (score 2, diepte 0) Vans, Nikes, & Pumas so far this year. Shoes are a huge deal to HS freshmen.
[dv4k8j5] (score 2, diepte 0) Toms, Converse, Sperrys boat shoes, or flat boots. No heels ever- did it once during student teaching and never again.
[dv4khfa] (score 2, diepte 0) Dr Martens all day everyday! They go with my style, are super comfy once worn in, and they make me feel like a badass who can handle anything!
[dv4lbsr] (score 2, diepte 0) I wear brown cowboy boots to school every single day of the year, unless I wear the black slacks and tie on occasion, in which case I wear the black boots.

I’m a guy who teaches at community college though, so this answer may not have been incredibly helpful. Lol
[dv4lcn8] (score 2, diepte 0) Toms tennis shoes
[dv4np2p] (score 2, diepte 0) Toms, birkenstocks, Sperrys
[dv4og0z] (score 2, diepte 0) I'm flat footed and prefer flat shoes. My go-tos are chucks or Toms/Bobs. The lacey Bobs are my favorite for a dressier look, while my chucks are my Friday shoes.
[dv4oyje] (score 2, diepte 0) Crocs are very comfortable and cheap.
[dv5r2nr] (score 2, diepte 0) I wear slippers. Yes, actual flip flops. On the rare cold or very rainy days I might wear converse. (Hawaii) For you, may something from shoes for crews?
[dv62vqz] (score 1, diepte 1) I bought a pair of Vionics 2 weeks ago....BEST investment ever!!  We're not allowed to wear sneakers and Vionics are dressy enough and feel like wearing supportive running shoes.
[dz7ncgw] (score 1, diepte 2) How have the Allbirds worked for you? I am so interested but I can't tell if I'll be able to style them in a way that looks professional.
[dv57lhh] (score 1, diepte 1) I can second the Red Wings.  Mine are comfy, professional looking, and still going strong after a few years unlike others I've had.
[dv4jsb8] (score 1, diepte 1) Thank you! I’ve been wondering if tieks are worth the money.
[dv4qhma] (score 1, diepte 3) Maybe I will. thanks!
[dv4pyo7] (score 1, diepte 1) Do you know if these will work with arch supports? I have keen's now and while my feet love them for their comfort and support, they look hideous.
[dv4q7pu] (score 1, diepte 2) Not sure....maybe buy a size up?
[dv4r37s] (score 1, diepte 3) Shoot. They're way too expensive to try things that may not work.
[dv6n210] (score 1, diepte 1) Are these the teal bottomed ones?
[dv6omrr] (score 1, diepte 2) Yep.
[dv5a97n] (score 1, diepte 1) Love my Toms. There are several pairs under my desk right now (at least until I no longer have to wear my winter boots outside).
[dv4e1om] (score 1, diepte 0) I'm blessed with the ability to wear any footwear and not feel any discomfort so long as they fit me right. Ive worn everything from Sanuks to cowboy boots to white nubucks to running shoes and more. Just depends on my outfit, how I feel that AM, and what, if anything, I have planned after school. 

It really just depends on you. But I highly recommend getting sized and fitted properly. Keep in mind, different styles for differently. I'm a regular width with cowboy boots, but need a slightly wider shoe when I wear sneakers or else they hurt like hell if I walk too much.
[dv5jvld] (score 1, diepte 2) Yes! I wait until it’s a bit warmer, but those are in heavy rotation as well.
[dv4fmsp] (score 1, diepte 0) I'm currently wearing some comfy leather shoes i got at academy,  they're by Magellan
[dv4h0kn] (score 1, diepte 0) I wear sneakers with custom orthotics.  It's all I can stand to use now.  I've been teaching for 24 years and seem to spend most of the day on my feet.
[dv4h0kw] (score 1, diepte 0) I used to be all cute and wear adorable heels all the time. Until they completely screwed up my tendons and I got really bad achilles tendonitis, plantar fasciitis, and peroneal tendonitis (yup that's a thing, who knew).

It's running shoes with inserts now. I have one pair of professional black shoes that also support my feet well enough. Every once in a while I'll try flats or heels again, and my achilles will flair up right away.
[dv4i0cj] (score 1, diepte 0) Comfy flats or cheap black canvas shoes from target.  My school is very informal though. It's not unusual to see teachers wearing sweats.

In the winter I wear short black boots/booties too.

I also wear black jeans or jeggings almost every day, although ive just now found a nice pair of dress pants !  (Although sometimes I feel overdressed in those )
[dv4ivg9] (score 1, diepte 0) I wear flats. It's hard to find good ones that don't eat your ankles, but the Walmart ones are great. They feel like slippers; they do fall apart quicker than quality shoes but for $6 who cares.

Also, Clarks are really good but expensive.
[dv4j2is] (score 1, diepte 0) My favorite is to wear boots with no heel.

I also wear flats, though I am careful to find ones that don't rub. My "test" for flats is that they need to have a flexible sole, but not the type that practically curl up on their own. When I find a style that works, I buy like 5 pairs and then repeat the process several years later when they are all worn out.

Sneakers are against our dress code without a medical need. Nobody will care if it's a once off thing, like you plan to walk your kids outside for a project our something, but not an everyday thing.
[dv4jhf7] (score 1, diepte 0) I tried ballet flats too and the kids kept saying "Mr. J, since when do you dance ballet?" 

Slip on dress shoes are TNT.
[dv4jxbc] (score 1, diepte 0) I really like Sperrys boat shoes. They have like 2 inchs of cushioning inside.
[dv4k6tt] (score 1, diepte 0) Since I usually dress up, I invested in a pair of Allen Edmonds years ago. Expensive at the time but by far the best purchase I've made. For more casual wear, just a comfortable pair of sneakers with support. I've also found that getting some nice socks like Fits or Stance increased my comfort significantly.
[dv4kvnq] (score 1, diepte 0) Depending on my mood (and outside temperature) I choose between Doc Marten‘s and Converse Chucks in various colours and styles, they‘re all endlessly comfortable. I used to have some cool and comfy Clarks shoes, too,  but unfortunately they‘re too far gone now to wear them to work.
[dv4lm49] (score 1, diepte 0) in the beginning of the school year when it’s still hot I wear dressy sneakers. In fall, winter, and early spring I wear boots, up to 2 in heel. I like to dress up so that works for me. I hate flats because they rub my heels too ;(
[dv4m7zs] (score 1, diepte 0) I wear vans basically every day. Heels or flats may look more professional on me, but in the end, I always go for comfort. We're standing and walking around for most of the day, so it's not worth being in pain because of the shoes I'm wearing.
[dv531ck] (score 1, diepte 1) Did I offend someone?
[dv4qvom] (score 1, diepte 0) I bought a pair memory foam Sketchers because I'm broke and cheap. They are my "mom shoes".
[dv4tp4n] (score 1, diepte 0) I mostly wear Birkenstocks (sandals in the summer and clogs in the winter). A higher quality tall brown boot is also important for me because I like to wear them with skinnies. Some of the outdoor clothing companies make good, reliable options that still look cute. Many of my other teacher friends swear by Dansko, but I've never personally worn them.
[dv4wir8] (score 1, diepte 0) I either wear black leather shoes or joggers, depending on the day
[dv4xxac] (score 1, diepte 0) Toms or Bobs, every day.
[dv4z7tq] (score 1, diepte 0) I wear black, wide fit, no slip mary janes.
[dv4zqkb] (score 1, diepte 0) When I wasn't supply teaching and I had my own class I used my runners.  It was reception (Kindergarten) so it wasn't a huge deal.  Now that I am supplying and back in home I wear Blundstones.  They are crazy expensive but pretty much the only ones (or the 30 I tried on) that could provide me support and were comfortable.  The first week is rough but once you wear them in they are wonderful.  Plus, kids can accidently step on your feet all day and you can't feel it.
[dv51e26] (score 1, diepte 0) I got some great inserts, and now can wear any darned shoe I wish!
[dv51snk] (score 1, diepte 0) I little of heal support is lovely and actually gives a little relief Comfort shoe brands like Clarks, Naturalizers, etc. actually have a decent range of styles now.   I also add the inserts you can get in the drug store (even if I wear Converse, I think they are too flat without support).
[dv5aijj] (score 1, diepte 0) Timberland lounger slip on...best decision I’ve ever made. 

http://www.blair.com/p/156279.uts?src_code=209N&cid=pl_bl_google_pla_gen&gclid=CjwKCAiArOnUBRBJEiwAX0rG_WPEWnR_2myOAP5dbbONGfsrNC7Ha0Gmy_GnppCBbXKLRhd09rA75hoC6J8QAvD_BwE
[dv5e04z] (score 1, diepte 1) I wear Timberland boots (the dressy ones, not the construction work ones). So sturdy and comfortable!
[dv5hjl7] (score 1, diepte 0) Kork-Ease - I own two pairs of the Velmas and they’ve seen everything.
[dv5l8rd] (score 1, diepte 0) If your flats are rubbing, they aren't broken in. You need some moleskin or something else to provide a barrier until they are (or some keysocks).

I wear birks, Brooks running shoes, keen flats, clarks, etc. I have annoyingly wide feet so a lot of shoes just don't work for me. I also have custom orthotics which are a life saver but understand the cost can be a barrier to many (my insurance covered them).
[dv5tumd] (score 1, diepte 0) Sneakers are what I usually roll with if I can get away with it.  My current principal gets really anal about stupid stuff though so I have to wear nicer shoes (although at this point my sneakers are nicer than my dress shoes).  I shopped around until I found a pair of shoes that look like loafers on top, but have a sneaker bottom.  I can't remember the brand, since I only wear them at school and leave them at school all the time though.
[dv64cc2] (score 1, diepte 0) I like the memory foam keds. I also have flats made by Nike and Puma.
[dv65gfv] (score 1, diepte 0) I wear nice looking sneakers, usually converse in a neutral color (I've got dark blue at the moment), with some insoles to make them more supportive. I've got a bad knee on one side and a bad foot on the other, so I really can't afford to be wearing nonsupportive shoes. I haven't hand anyone say anything about it.

Get some insoles and some nice looking sneakers (and make sure they stay nice looking) and you should be fine!
[dv6n3zl] (score 1, diepte 0) Vionic and Birkenstocks. Also, compression sleeve on one foot to help with Plantar Fasciitis

=== THREAD 8nwzdn ===
SUBREDDIT: r/army
DATUM: 2018-06-02  SCORE: 5  REACTIES: 78
TITEL: Best general running shoes for pt/pt test?
POST (source_id=post):
Ok so I'm currently in 68w ait and don't have a way to go to a real running shoe store where they can measure my gate and all that so even though that's definitely the best idea it's not an option available to me. Here's some info to help

$130 budget (lower the better)

I'm running mostly slow distance runs (10-11/min pace 8 miles) but I really would like a shoe that would give me the best advantage during the pt test.

It's super fucking hot here at fort Sam  like it hasn't dropped below 103 all week. So shoe would be preferably breathable.

I'm still kinda overweight (185, 5'11)
I have bad flat feet but I got them to make me some custom in souls that have been a tremendous help so that shouldn't be a problem.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dzz1t9g] (score 66, diepte 0) Yeezys
[dzyzv12] (score 25, diepte 0) First of all, run shorter distances but faster.  Second, this is an impossible request.  Get an Uber and go to a running store.  Or tell your psg that you need new running shoes but don't have a way to get to a running store because you're only phase 4 or whatever the issue is.  Running shoes are *impossible* to do remotely.
[dzz2clf] (score 13, diepte 0) They still make Heelys, right?
[dzz0blg] (score 9, diepte 1 OP) I asked got told to kick rocks

Lol my first sergeant doesn't believe in short distance runs we legit never run less then 5 miles (that's pretty rare) we sometimes do this thing we're we run a mile do like CD 1 then run 2 miles then do CD 2 run 3 miles (the way back to the pt field) then do the recovery drill. We're expected to do shorter faster paced runs on our own time.
[dzz0vro] (score 9, diepte 2) I really doubt your AIT PT runs are 5+ miles. It would put your pt sessions at an hour and a half to two hours with average run speeds and all the other PRT crap that has to be done while under the watchful eye of TRADOC.
[dzyzqqj] (score 7, diepte 0) Updog.
[dzz1tgv] (score 7, diepte 3 OP) Wake up is 0400, fall in is 0430. Pt generally starts 0450, We do 5 count prep drill on run days takes 10 minutes, were running right around 0500. Run for about 1:30 to 2 hours. Chow is at 0730 so we have plenty of time to come back get dressed and go to Chow. 

This is definitely not typical of 68w ait. 
delta company just has a very high standard compared to the other companies. Last cycle they started with 311 whiskeys ended with 187. Like 70+ of those all achieved honor grad or a 300 on there pt test.
[dzz00fs] (score 6, diepte 2) Not much dog, you?
[dzz0mrj] (score 5, diepte 0) I am an 11A I am 6’0 and 201lbs. I enjoy running spartan races and marathons with my wife. I’d say my favorite running shoe is the

Salomon Unisex S-Lab Sense 6 Running Trail Shoes Racing Red/White/White 11 https://www.amazon.com/dp/B01GQUX8Q0/ref=cm_sw_r_cp_api_i_PQEeBb928Y0K6

But for PT I wear 

New Balance Men's M1080GY7 Typhoon/Hi-Lite 10.5 B US https://www.amazon.com/dp/B01M2D66TZ/ref=cm_sw_r_cp_api_i_WSEeBbKWYCRNK


And 

ASICS Men's Gel Venture 5 Running Shoe, Silver/Light Grey/Royal, 10.5 M US https://www.amazon.com/dp/B00NUZD0M2/ref=cm_sw_r_cp_api_i_MTEeBbRPH6CTK

With all three equipped with these.

Salomon Men's Quicklace Kit,Black,One Size https://www.amazon.com/dp/B00AQRUL7E/ref=cm_sw_r_cp_api_i_xUEeBbASMY5P7

The Salomon shoes are incredible, and the laces make any shoe better. I’d say go with the ASICS and save the money as no shoe at a beginning level adds that much advantage. That beings said I do feel a lot more spring after each stride in my S labs, that’s why I run my races with them. 

Just PT as much as you can. If it’s to hot go to the pool and swim laps, I only run 3 times a week and I swim on the off days only resting Sunday.

Goodluck.
[dzz2vr9] (score 5, diepte 0) What even is this post? 8 mile ait runs? 185 at 5'11" is overweight?
[dzz5i1y] (score 5, diepte 1 OP) I went to the doctor for left ankle pain and he told me it was my peroneus brevis tendon and that it was being stressed cause I was overweight and gave me a nutrition sheet lol. 

Tl;dr: went for a profile Dr gave me a diet.
[dzzhrx1] (score 4, diepte 2) > I asked got told to kick rocks

Fuck AMEDD
[dzz6aib] (score 4, diepte 3) You're a no-go at this station
[dzz0mwb] (score 3, diepte 1 OP) http://pixar.wikia.com/wiki/Dug ?
[e0046un] (score 3, diepte 3) Hes not even close to overweight.
[dzz6bex] (score 3, diepte 4) "sgt major daily" this thread keeps getting better
[e004dtb] (score 3, diepte 2) I mean do you have like stick arms and legs and a gut? I cant figure out how 185 at 5'11 would be overweight. Thats, at the worst, an average weight for that height
[dzz40r6] (score 3, diepte 0) I use the [On Cloudflow](https://www.runningshoesguru.com/2017/01/on-cloudflow-review/)

I like them a lot. I went to a running store and they fitted me for a few pairs of shoes. All the ones I tried on were great but I liked these the best. I have a neutral gait when I run.

Saucony and Brooks are both nice as well. I would have bought Brooks if I didn't buy what I have now.
[dzz72kr] (score 3, diepte 0) I swear by the altra escalantre.  Neutral shoe.

It is extremely flexible, great cushioning, lightweight, great grip, and the toe box is actually shaped like a foot.  It feels like you are wearing socks.  Great shoe for a run.

It is a zero drop heel though, so it takes some getting used to if youve never used shoes like that before.  More of a strain on your calves.  Make sure to get used to the shoe before running a PT test.
[dzzifxw] (score 3, diepte 0) I prefer a Scott's race shoe.  You'd be amazed how much of a difference using a light weight race shoe can be over a heavier shoe on a 2 mile Sprint.
[dzz0287] (score 2, diepte 3) Has this ever happened to you? Someone says “Hey, how are you?” and then you start talking about your life.

“Oh, today is horrible. I have so much to do, and my son is sick, and I saw the price of gas is going up again, and…..”

Clearly, telling your life story is NOT the correct response to “How are you?” And today, you’ll learn different ways to respond to “How are you?”


In the US, you’ll hear “Hi, how are you?” or “How are you doing today?” or if you’re in the south “Hey, how y’all doin?”

You’ll hear this ALL the time! The server at the restaurant, the cashier at the store, your colleague you pass on your way to your desk. Everybody asks “How you doing today?”

And if you’ve noticed, nobody really answers. I mean a real true answer.
[e00rkcl] (score 2, diepte 4) >  delta company just has a very high standard

ECHO
[e00hsfe] (score 2, diepte 3 OP) Ik I'm literally in the medical Mecca for the military and they tell me to pretty much go fuck myself for the next 2 months when I ask for help with a problem I have medical documentation of. Idk it's just kind of ironic.
[dzz0deh] (score 2, diepte 1 OP) Yo how do I get a pair of those if I send you $200 you think you could cop me a pair.
[dzz0jlp] (score 2, diepte 2) for only $200? 

yeah, i think i could make that happen.
[dzz1w50] (score 2, diepte 3 OP) Shit I'll make $350
[dzz6h4r] (score 2, diepte 5 OP) I'm a dumbass
[dzzcu8m] (score 2, diepte 6) Nah you're just an inexperienced pri'.  You'll get there, probably.
[e00arkc] (score 2, diepte 1) This
[dzztf5t] (score 2, diepte 1) I switched from Salomons to On Cloudflow with no regrets. I miss my Innov-8s sometimes though
[e00d84f] (score 2, diepte 1) https://www.roadrunnersports.com/rrs/product/shoe-dog.jsp?cm_mmc=vanity-_-shoedog-_-na-_-na
[e00nuga] (score 2, diepte 2) Nice. There you go OP.
[dzz4tp5] (score 2, diepte 0) You think it’s hot now?! *laughs in July camp bullis carrying casualty down recycle rock* 

There’s probably stores in SA you could check out once you get phase V
[dzz5apa] (score 2, diepte 1 OP) Thanks I've used the site before and that's probably the best temporary fix
[dzz7yrv] (score 2, diepte 1 OP) I'm assuming you've switched over to a minimalist style of running.  How hard was it? And what kind of improvements/disimprovements did you notice?
[dzzy9co] (score 2, diepte 0) Toe shoes
[e000eql] (score 2, diepte 0) Work on running on the front of your foot, it'll save you from having bone problems regardless of the shoe you have.

Purchase expensive shoes, but only wear them for PT.  You should, in theory, be able to keep them for about 6 months at a time depending on how dirty your PT is.  If you need to wash them, take out the insoles before getting them wet.  Replace the insoles before replacing the shoe.  You still need to replace the base every 6 months or so though.

Get the same kind that they outfitted you with at basic training.  I know that sounds lame but they did measure your foot before giving them to you.  Even if it's not a perfect shoe, it should work well enough to get you through AIT.

Despite what most people are going to tell you here, running for distance is a requirement of your MOS, even if just for garrison.  It won't DIRECTLY improve your PT time, but it will improve your overall cardiovascular ability and endurance which then will make the PT test seem very short.
[e2s113l] (score 1, diepte 5 OP) 1sg foster recently left but captain kaahiue is still here and he still is really awesome.
[e00gsc3] (score 1, diepte 3 OP) I do lol I'm not worried about my run. Last one was 14:41 (definitely not good but not terrible either) I just want a good pair of running shoes that will helpe max out the pt test and make those long distance runs a little bit easier on my ankles and feet.
[e00isai] (score 1, diepte 4) If you're looking to shave seconds from your pt test, you're looking for racing flats.  Racing flats are no good for daily pt, so...

Save your money until you can get to a running shoe store and let the employees figure it out.  Tell them your pace, weekly mileage, and terrain (pavement, probably?).  Bring your current running shoes so they can check the wear patterns.  Tailored shoes will protect you during training runs, which will result in a better apft.
[e2s14fw] (score 1, diepte 5 OP) Ds Kendall is one of the best nco's Ive met so far.
[dzyzvsd] (score 1, diepte 0) https://imgur.com/r/ffxiv/M60dA
[e02mg9o] (score 1, diepte 2) Now that’s funny. I guess if the shoe fits and works then it’s all good.
[e0gde63] (score 1, diepte 1) God I love my fellow servicemen 😂
[dzztck7] (score 1, diepte 2) Does this doctor even lift?
[e00hkpy] (score 1, diepte 3 OP) Lol, no I'd say my arms are slightly bigger then average. Idk I lost 40lbs in bct so I still sort of look fat due to excess skin so maybe it was that, but he told me my optimal wait was 170-175 so...
[dzz2yeg] (score 1, diepte 0) Can you guys leave base yet? There’s a Fleet Feet in the quarry that will treat you well.
[dzz57qf] (score 1, diepte 1 OP) No still in phase 4
[dzz6aeu] (score 1, diepte 2) That makes sense. PT test before gold phase. Shoes are meant to be worn and run around in before you buy them. When is your PT test and can you make it in your current shoes until you hit gold phase? My biggest advice is to not buy shoes at the PX. They’re not going to have the customer service to really help you. The shoe selection tends to be lacking too. 

https://www.runnersworld.com/gear/g20854929/how-to-buy-the-right-running-shoes-0/
[dzz7ge7] (score 1, diepte 3 OP) I have an assessment mile this Monday. I'm not really worried about it though I think you gotta run like a 7:30 mile and I run a 7:00 mile everyday. I have a diagnostic one in like 3 weeks and a real one in like 6. So I'd have plenty of time to break them in.
[dzz6bj7] (score 1, diepte 1 OP) Yeah those seem really nice. I'm little worried about ording them offline though. How was the sizing on them?
[dzzmnn2] (score 1, diepte 2) I'd say they're true to size, I got measured when I bought them. They gave me a half size up though.
[dzztzaf] (score 1, diepte 2) I have some Salomon water/hiking shoes that are great. I've never tried their running shoes but I'm really enjoying the On pair I have.
[dzzze0f] (score 1, diepte 3) I had to switch from the Salomon Speedcross as it was more of a trail running shoe and all the road running was wearing it out.
[dzz4lic] (score 1, diepte 0) Runner’s World used to have a good shoe finder tool on their website. Not sure if is still there or not, but it took into consideration your body weight, average weekly mileage, what terrain you run on most, and a couple other things to give you a list of 2-5 possible shoes.
[dzz59a2] (score 1, diepte 1 OP) I'm gonna die ik.
[dzz50f1] (score 1, diepte 0) oakley boots
[dzz540k] (score 1, diepte 0) Go to 6pm.com and you can get last year’s model of all different brands of shoes for about 30-60% off, sometimes more. That should help keep good running shoes in your budget.
I personally prefer to run in Brooks, but I would highly recommend getting the gait test and fitted for shoes as soon as you can.
[e002fvn] (score 1, diepte 2) I wouldnt consider the altras a minimalist shoe.  They have a lot more cushioning than minimalist shoes do.  I prefer it that way.  The altras do have that feel of running barefoot though due to how flexible the shoe is, the large toe box, and the zero drop heel.  Even the pattern of the sole mimics a foot.  Transitioning to a zero drop shoe took some getting used to.  At first i had extra strain on my calves and achilles, but now it is fine and my running form is a lot better.  The shoes forced me to stop heel striking.

I buy new running shoes about every 3-4 months.  The altra escalante is the only time I've repurchased the same shoe.  If you have a shop in your area that carries them definitely go try them out.

The one con I have for those shoes is they are not great for sprints, or sports, or really anything that requires you to change direction while running.  They have no support, instead fitting like a pair of socks.  This means when you go to change direction, or stop quickly, your foot will slide off the sole.  Definitely have a different more supportive shoe for anything other than distance running.
[dzz7kc9] (score 1, diepte 0) I ordered these but had to return them due to them being a little too small so I haven’t tried them yet.

https://www.altrarunning.com/men/vanish-r

I heard this guy talking about them on a podcast and how he wears them so I thought I’d give them a try. He runs 100 miles at a 7 minute pace. Obviously it’s not all the shoe but I figured I’d try them. They are a minimalist shoe so I’m not sure if that’s your thing or not.

https://www.runnersworld.com/news/a20859058/how-zach-bitter-broke-the-u-s-100-mile-record/?amp&
[dzz7vg3] (score 1, diepte 1 OP) Thanks, they seem really interesting I just don't think I'd be able to adjust to something like that quick enough I've been using these shitty Nike shoes for the past month and a half and was using the shoes the army gives you before. Both are very heel focused shoes.
[dzzcw2h] (score 1, diepte 0) Oh hey also try reading this reddit.com/r/army/comments/8l3ho7/a_brief_rarmy_guide_to_the_2_mile_run/
[e00hz5t] (score 1, diepte 1 OP) Yeah I've never used a real racing shoe. The ones I have now are these Nikes I got as a dumbass civilian cause I thought they looked "cool" and there clunky as hell.
[e00q2uc] (score 1, diepte 2) Yeah race shoes, look stupid and will probably come in some bright color. But a lightweight shoe makes a huge difference.  Make sure to get something that fits your foot properly.  The PX should have something that will work for you, just bring your phone and look reviews on https://www.runningshoesguru.com/.  But a person at a running shoe store, like fleet feet can get you into the perfect shoe for you.
[e00h7oo] (score 1, diepte 1 OP) If by measured you mean an old Asian lady glanced at my feet then handed me a pair. But yeah I was thinking about just getting another pair of Asics they really weren't all that bad. Also that's the philosophy of why we run those long distances it's because as 68w it's much more important that you have the stamina to carry a casualty however far it may be to go rather then being able to Sprint a 2 mile.
[e003gi9] (score 1, diepte 0) Saucony kinvara series
[e00eu43] (score 1, diepte 0) Nobody can tell you the best shoe for you over the internet. You should visit a running shoe store and ask them to do a gait analysis. They will recommend shoes from there.

Everyone is different. Don't fuck up your feet.
[e00h8j0] (score 1, diepte 1 OP) Wish I could
[e00lw2i] (score 1, diepte 0) 185 at 5'11" is overweight? I know it breaks the ht/wt scale, but I'm 5'8" and was 185 and passed tape by a landslide.
[e010n3j] (score 1, diepte 1 OP) Idk I don't think I'm overweight tbh but the Dr that saw me did.
[e00r0fm] (score 1, diepte 0) Nike Pegasus 35s.
[e01h65p] (score 1, diepte 0) Worst case the PX or clothing and sales. As long as you buy from a reputable company. I'm sure there is a fleet feet in SA that can get you the ideal shoes for your gait/feet.
[e010j3x] (score 0, diepte 5 OP) Yo if your echo you know we take that left when you guys run back to the cta.
[dzz662c] (score 0, diepte 2) You can't run on the weekends?  After class ends?  Sprints, guy.  Do them.
[e00tx6n] (score 0, diepte 0) Stop being fat though... I like Asics nimbus and Saucony kinvara. Just realized you're probably a guy but you can find good deals on similar shoes all over the internet https://www.asics.com/us/en-us/gel-nimbus-18/p/0010255946.9701?utm_source=google&utm_medium=pla&CAWELAID=120223060000098457&gclid=Cj0KCQjwgMnYBRDRARIsANC2dfmG5a-2R1754m6jPgMabtr3pFkO-EpTMoebKrOlVdM9tUhljsUYnUwaAhvOEALw_wcB
[dzyzz60] (score -2, diepte 1) "Updog" is a made-up term based on a wordplay of the colloquial expression "what's up, dog?" that is commonly used as a practical joke to elicit the question "what's updog?" from someone, to which the prankster typically responds with the punchline "Nothing. What’s up with you?


The exact origin of the joke is unclear. On December 6th, 2000, Ars Technica Forums member Col. Forbin submitted a variation of the prank to a thread titled "jokes that make you groan and/or wanna smack your forehead."
[dzz1pif] (score -2, diepte 1) RIP Shoefitr

Edit: what's with the downvotes?
[dzz2ptg] (score -9, diepte 2) That’s sir not man.

