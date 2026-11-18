# Label-batch batch_0079

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
Schrijf het resultaat naar `batch_0079.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1fmirzs, bndhcj, 1elzsue, vnxjpi).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1fmirzs ===
SUBREDDIT: r/pharmacy
DATUM: 2024-09-22  SCORE: 13  REACTIES: 86
TITEL: Best tennis shoes for retail pharmacist?
POST (source_id=post):
New pharmacist never had to stand so much for as long as I do now haha. Currently I wear On Cloudmonsters but am still having foot pain after long days. I've heard Allbirds are good for standing all day but they just look so ugly to me so I'm wondering if they're worth it, any input? I've tried Hokas on in store and felt they weren't comfortable at all.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lobab4z] (score 49, diepte 0) Find the closest shoestore to you. Not Payless or any chain, go to a store with a guy who watches you walk, measures your foot, then picks a shoe for you. Prepare to spend up to $150, but just keep in mind shoes are equipment that you need to do your job and avoid several different types of joint and body pain.

Hokas work well for me, but there are other quality brands that may work better for you.
[lobh6ou] (score 23, diepte 0) Adidas Ultra Boost
[lobdaeo] (score 22, diepte 0) Fan of brooks ghost max
[lobq6ty] (score 16, diepte 0) I’d wear calf compression  to prevent swelling in the feet
[lobjk7y] (score 14, diepte 1) THIS THIS THIS.  As an ultramarathoner I get asked about footwear at work all the time and every time I'm like how should I know, I don't watch you walk and run and I'm not examining your feet.
[lob9fot] (score 12, diepte 0) Hokas are popular, but I don't like them. I prefer Asics.
[lobc0k0] (score 10, diepte 0) Sketchers have done right by me. Especially the slip on kind. They’ve definitely helped my feet.
[lobcsn9] (score 10, diepte 0) I swear by hokas. I can stand all day in the pharmacy with these on my feet.
[lobqdyj] (score 7, diepte 1) 2nd this. Tried a looooot of shoes. Ultraboost are always the end game.
[lobny1f] (score 6, diepte 1) Hokas are amazing if you have bad ankles, I have short tendons and used to have a heavy limp after 8 hours,  Hokas and compression socks and I'm good all day and not dead when I get home.
[lobdz5o] (score 6, diepte 1) Pretty sure Payless is gone for now
[locf7bu] (score 5, diepte 1) This is the correct answer. There are so many individualized factors and it’s impossible to tell you the best shoe for you. 

I’m general, you want a show that maximizes surface area contact to have more weight distribution. This doesn’t take into account for heel drop, arch support, comfort of the upper, etc. 

What you also need to do is rotate shoes. You should not be wearing the same pair of shoes each day. Foam needs time to recover, so have at least two pairs and alternate. 

My current favorite is New Balance Rebel v4. It’s extremely lightweight, cushioned, but I worry about longevity issues as it’s a running shoe.
[lobcwpq] (score 5, diepte 0) Never considered....leather dress shoes with orthotics and firm compression knee high compression socks.....for nearly 41 years
[loby5pz] (score 4, diepte 0) Altra Paradigm 6
[lobmffz] (score 3, diepte 1) These are literally my favorite and what I wear. I used to always wear cowboy boots everywhere, and wore my boots for a long time in the pharmacy didn’t even own tennis shoes as they felt uncomfortable to me but these shoes changed my life.
[lod9n7g] (score 3, diepte 1) Specifically ultra boost 1.0. Much more comfy than the later models imo
[lobjfsh] (score 3, diepte 0) The best shoe is the one that offers enough support, stability, and light enough to mess you up assuming you're fairly out of shape and also fits your feet and gait when walking and running.  Unless you can answer those questions there is no sense in all these footwear posts. You might as well ask what's the best antihistamine for a retail pharmacist.
[lobn4w8] (score 3, diepte 0) I have wide feet. 
Hoka Gaviotas are my favorite in wide. 
Can’t wear allbirds or On cloud because they are too narrow for my feet. 
I have been experimenting with Brooks Ghost and they are also very nice, but took some getting used to. 
You can buy from REI and try for couple days and return it if you dont like it. They will however let you return it for whatever reason for up to a year.
[lobp4yr] (score 3, diepte 0) I cannot stand for long periods in soft shoes. Walk or run, sure, but not stand. When I worked retail I wore Doc Martens, and now in the hospital I wear Danskos. It sounds counter intuitive, but if you have pain after standing all day in running/walking shoes you might need something with less give, not more.
[lodflln] (score 3, diepte 1) Compression socks are underrated. It gets you half way there
[locorsr] (score 3, diepte 1) Strongly suggest anything by Altra. Their shoes are actually foot shaped.
[lodhxor] (score 3, diepte 1 OP) Good question! Do you post this comment on every post with the exact same question?
[lodn6ca] (score 3, diepte 3 OP) Oh my you’re so bothered. I did look at other posts. Thank you for wondering. I was specifically looking for pharmacists who have tried Allbirds if they’re worth it and if any who currently wear On Cloudmonsters had better success with other shoes. The whole point of Reddit is to post a question and get a response which everyone else here seems to understand haha. Also by looking at your comments from your profile it does look like you copy and paste this response quite a bit! I hope you find something better to do
[loba25p] (score 2, diepte 0) Hoka bondi was recommended to me by my orthopedist as I need an ankle replacement from all the wear and tear
[lodhphu] (score 2, diepte 2) I "only" run marathons and halfs (so far), but YES. Anyone else's foot needs are going to be different from mine. I tried a pair of Hokas when everyone was first raving about them. Even went with my usual combo of neutral shoe with Superfeet insole. They messed up my knees horribly. Now, if someone's feet like neutral shoes with Superfeet blue inserts and a 5-8 mm heel drop, I can give you several recommendations (hah!)
[lobb529] (score 2, diepte 0) Brooks are pretty good for standing all day
[loehsfd] (score 2, diepte 1) I swear by Hokas. My arches are slightly flat but they’re game changers for me. I wear those shoes even on my days off.
[lodaelk] (score 2, diepte 1) I switched to a wide ghost and love them. It stopped a lot of the foot pain I was having due to the wider toe box on the end. Def recommend.
[lobeur0] (score 2, diepte 0) On Cloud or Brooks Ghost Max. Also: compression socks!
[lobgb79] (score 2, diepte 0) I like the all birds. But I don’t rly have feet problems.
[lod480u] (score 2, diepte 1) This one!! Bought like 8 pairs 2 years ago when I caught a sale 😂
[loe7xcx] (score 2, diepte 1) I've been wearing them for 5+ years and I'm never sore at the end of a long shift. Couldn't recommend them more.
[lol0jrb] (score 2, diepte 1) With compression socks!!
[locibmq] (score 2, diepte 0) I can't believe more comments haven't mentioned this, but get yourself knee-high compression socks. Shoes are completely dependent on your foot shape, arches, etc. and are very individualized what works for you. I would be crippled by now if not for my compression socks.
[lociz5k] (score 2, diepte 0) Brooks ghost foreverrr
[lody0nu] (score 2, diepte 0) Skechers were my go-to shoes (and still are) when I was standing all day. I have plantar fasciitis and the thicker heel seemed to help me out.
[lob8qa0] (score 1, diepte 0) I've tried all birds...  mine fell apart after like a year.  But I wore them everyday.  I have switched to Arahi 6 Hokas and I have an insert which helps.  I haven't had any noticeable foot pain ever since.
[loddqup] (score 1, diepte 1) I Ike them, but they are so heavy!
[lodfxdz] (score 1, diepte 1) Hokas don't work for me either. The wide cliftons are still too narrow for me. Wide new balances and altras work for me
[lodkfi9] (score 1, diepte 1 OP) So I actually did do this about a year ago and they sent me the scan results with the data but didn’t give me specific shoe recommendations for my feet! Maybe I’ll go have it done again and ask what they recommend from my results. Thank you
[loepaty] (score 1, diepte 1) Hoka store does this?
[loeqbg4] (score 1, diepte 2) Maybe? But I’d go to a store that has more than just Hokas.
[logo4z8] (score 1, diepte 1) Hokas have too much heel to toe drop for me. I wore some over a year and I liked them okay and I talked to the guy at Dick's Sporting Goods for other recommendations that were similar in the padding but different in fit/feel. He suggested Asics Pure Gel, and I tried them and liked them. I've had them for probably 7 or 8 months now and they will likely be what I buy again when I get more shoes.
[logrc3a] (score 1, diepte 2) Lol I like the heel toe drop personally. It makes running feel a little more effortless, but I also run all day at work like a shmuck.
[lokbajl] (score 1, diepte 1) Hokas and ON are my two favorites for when I float
[lohblds] (score 1, diepte 1) Are your orthotics custom made? What do you use?
[lohlh0x] (score 1, diepte 2) They are custom molded. I forget makers name. I'll find it and post
[loktr70] (score 1, diepte 3) Thank you would appreciate
[lobet69] (score 1, diepte 0) Onclouds are great when I get the correct insoles specifically for plantar fasciitis in them. Otherwise-they’re not tennis shoes-but Dansko Pro clogs with thick socks are the only shoes I can wear on my 12 hour days. The third pair i usually rotate with are orthopedic Hokas, with or without insoles.
[lobf990] (score 1, diepte 0) Whatever tennis player Tommy Paul wears.
[lofoo5s] (score 1, diepte 2) Ultraboost have sold for years now tried and true. Lol
[loftmrp] (score 1, diepte 1) Why are ultra boosts so expensive???
[lobjtdx] (score 1, diepte 0) Brooks
[lobllvz] (score 1, diepte 0) Get Cadence Insoles.
[lobomp5] (score 1, diepte 0) I wear Dr Scholls and I really like them. They make ones that are actually nice looking/dressy and they are super comfortable. Plus they are only like $70 which is nice, and they definitely hold up against my hokas and ON shoes I payed $150+ for. My feet do start to hurt after like hour 7 of standing but I think no shoe could truly stop that.
[loctg0v] (score 1, diepte 1) seconded
[loe6tz9] (score 1, diepte 1) Do you stand in one spot all day at the hospital? I assumed you would be walking around a lot or sitting
[lofdzbj] (score 1, diepte 2) When I work in the IV room I do.
[lobp5mq] (score 1, diepte 0) If you have the time try Brooks Glycerin 20. Get them online try them, if not for you then just return them
[lobsptc] (score 1, diepte 0) Brooks ghost max. Well worth every penny. I switch between 2 pairs along with compression socks from sockwell & have never had same painful legs after long shift.
[loc1x6k] (score 1, diepte 0) Oofoos shoes and Hokas
[locqdaw] (score 1, diepte 0) When you searched this sub for an answer to your question, what did you find in all the other posts that had the exact same question?
[locqnfa] (score 1, diepte 0) Not allbirds. I have 2 pairs myself. They have no support. Looks cute and easy to wash is why I got it.

For work I alternate 3 shoes. 2 are by brooks. I think I got the gts glycerin. And an asics.

I've tried hoka. Felt really tight and by the end of day my feet need more space cause they're prob a bit swollen. 

I do compression stocking only if I have 4 back to back shifts in a row. 

I also foam roll my back and my thighs. I stretch my calves against the wall. I roll my foot bed back and forth on a tennis ball.
[locrfhy] (score 1, diepte 0) I think there’s no one size fits all here, but I’ve had good luck with both Hokas and Allbirds for comfort during 12 hour shifts. I’m not sure what style Allbirds you looked at but the ones I had looked like very standard sneakers, I wouldn’t have called them ugly. Actually I think my Hokas are hideous lol.
[loct3e4] (score 1, diepte 0) I had my feet measured at a footwear store with those fancy machines, their answer was new balance freshfoam x4 or x5 in ultrawide (4e) in 1 size extra becuase of needing insoles separately!!!!
[lod41xv] (score 1, diepte 0) Real tennis shoes would not be good for standing all day zzz
[lod7cqj] (score 1, diepte 0) Also recommend compression socks and having a rotation of sneakers. I rotate between Cloud Monsters, Hoka Cliftons, and Topo Athletic Phantoms. My previous third shoe in my rotation was a pair of Altra Paradigm which the natural footbed is extremely beneficial as a pharmacist standing all day.
[lodc1rb] (score 1, diepte 0) Believe it or not under the knee compression socks help with the pain with standing for that long.
[loddo2n] (score 1, diepte 0) I love Merrell’s. They work best for ME! I’d go to Fleet Feet and get your foot scanned and see what would work for you!
[lodglni] (score 1, diepte 0) I will forever swear by [padded Cons](https://www.converse.com/shop/p/chuck-taylor-all-star-malden-street-unisex-mid-shoe/A08588F.html?dwvar_A08588F_color=into%20the%20void%2Fvintage%20cargo&styleNo=A08588F&cgid=mens-shoes-2) easily the most comfortable shoe I've ever worked in.
[lodjkiw] (score 1, diepte 0) On Cloud 5 and compression. Also New Balance 1080 are great.
[lodlql7] (score 1, diepte 0) Not tennis shoes - but I swear by the crocs neria pro II.
[lodolym] (score 1, diepte 0) I personally like hoka bondi and ASICS gel nimbus. I don’t like them for running but for standing on concrete all day the thick cushioning is the GOAT
[lodw43y] (score 1, diepte 0) Altras are pretty good for me
[loe4ul9] (score 1, diepte 0) Get a darn stool…
[loe9738] (score 1, diepte 0) I prefer wolf and shepherd. They are good. Cole Haan, Merrell  are other options. I switch between them through out week. I find lacoste very useful as well.
[loem2r5] (score 1, diepte 0) hoka bondi 8 + compression socks!!!!!
[loet9n3] (score 1, diepte 0) Most shoes can be a great shoe with the right insole. Podiatrist recommend insoles for my wide feet, flat and wearing them inside Allbirds has been excellent for me.
[loetaq4] (score 1, diepte 0) I only wear adidas Ultraboosts and my feet never hurt
[loey3jq] (score 1, diepte 0) I tried custom fitting from New balance, private shoe stores, Ascis and crocs...15 + years standing now... finally settled on Hoka's bondi 8.. the shoe takes time to conform to your foot, once broken it...feels like walking on cloud.
(9 reacties met lagere score weggelaten)

=== THREAD bndhcj ===
SUBREDDIT: r/ems
DATUM: 2019-05-11  SCORE: 149  REACTIES: 86
TITEL: Do you ever lose your feet when an unexpected incident occurs?
POST (source_id=post):
Still a fairly new medic, I like to think that I’m fairly competent. Academically and practically, I seem to perform well and have confidence in my abilities - of course there is always so much more to learn with experience, and I’m definitely not claiming to be even close to the best. 

On a regular call whilst working, I can comfortably perform a structured and comprehensive assessment, without having the need to think too much - it just flows. Whether it be a grandma down or major trauma, I’m happy with my approach. 

However, today I was driving by to pick up a gift for someone, and a car pulls out in front of a motorcyclist - all I see is his body flying and a bang, turn around and park defensively. Get my basic trauma bag from the back and head over, by this time heaps of people have gathered - if I had been on the job, and had time to think and prepare somewhat, I think it would have been smoother. I still checked the ABC’s, I focused on airway management and c-spine stabilisation for the most part, managed ang bleeds and began exposing the patient to look for injuries prior to the ambulance rocking up. Although looking back I did everything I think I could have (didn’t want to remove the helmet without another set of experienced hands, pt was being held in a right lateral position with the help of bystanders and blood was draining well, pt was breathing with no obvious abnormal sounds) - I still feel like I fucked up, I almost feel like a failure because my brain kept second guessing and chasing its tail. 

I guess I’m looking for confirmation or advice that this is normal - as I said, I’m still fairly new and gaining more and more confidence, but this kind of made me doubt my abilities. It just didn’t flow in my head. Any tips fire away, feel free to roast the living shit out of me - happy to learn anything I can from this. 


TLDR: do you ever get fucking sprung and feel like a deformed lemon would have a better thought process and treatment plan than you

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[en4lrb5] (score 246, diepte 0) If it makes you feel any better I would have called 911 and kept driving.
[en4oqu0] (score 127, diepte 0) Going to a call is a lot different than having a call happen in front of you.  

With a call, your initial adrenaline rush from tones goes down a bit, you have time to think and prepare, you have supplies, and you have an "out". Even if you're unsure about what youre doing, you can get them to someone who is. 

When it happens in front of you, your adrenaline is still there, you don't have time to prepare or think because you're already there, and you don't have the option of moving. You're stuck with the supplies and skills you have and if that's not good enough, you're fucked. 

That's my personal take anyway.
[en4qmkg] (score 107, diepte 1) Yep. Had an engine company watch a wreck happen at a red light in front of them and it took about 15 seconds before the captain finally said "Shit, we should probably do something"
[en5gsip] (score 75, diepte 2) "Just call 911 and keep going"

"We *are* 911"

"Shit"
[en4nd9n] (score 68, diepte 0) Your first mistake was having a trauma kit in your car.
[en4or07] (score 68, diepte 1) I keep a bandaid in the glove compartment for personal use
[en4mn5j] (score 50, diepte 1) Same
[en4uv8y] (score 46, diepte 1) I've been given this advice from a medic that I was looking up to. Sometimes the best thing is to just call 911.
[en59tks] (score 46, diepte 1) This....ladies and gentlemen is how u spot a seasoned EMS professional.

Hell, I swapped all the gear in my "go bag" in my car for snacks for the kids. In not gonna save a life with some bandages and cardboard. Let the fully stocked ambulance with 2 professionals do their job. Calling 911 is mine
[en4poxb] (score 35, diepte 2) Wacker
[en4ova2] (score 34, diepte 0) I feel like this is about all you could've done without risking legal liability. When you're off duty you're not operating under a medical license - you're basically limited to a first responders scope of practice
[en4v39b] (score 34, diepte 0) There’s a reason that just about every service has dispatchers trained to tell you what the incident is in as much detail as possible before sending you. The ability to mentally prepare during your response is vital, otherwise there’d be no reason to train dispatchers. Imagine if every call was just “ambulance needed at xxx Y street.” You’d probably need a minute to gather yourself and get your bearings every time you got on scene.

You don’t have that warning or prep time when it happens in front of you. It’s a completely different experience.

I treat it like skills testing, and it makes the scenario flow better. Stop, look at the scene, and get a picture of it. Take a deep breath, and think to yourself “It’s better for everyone if I’m calm. Seconds won’t kill my patient. BSI, is my scene safe.......”

By doing that it gets me in a better clinical mindset and primes me to remember everything in assessment. You never go through the full NREMT bullshit because you always get a dispatch, you know how many patients you have, you know if you need additional resources, you have a fricken ambulance. Legitimately asking myself if my scene is safe in my head puts me back to skills testing where I remember those first four steps again. Then do everything as it needs to happen. Is it actually safe, or are you in traffic? What do you see? How many patients do you have? Has someone called 911?

Now you’ve had time to change modes, you’ve given yourself a good 15-30 seconds to collect yourself, you’re calm, you’re ready to go.




It at least works well for me, your mileage may vary.
[en4xtzt] (score 32, diepte 2) Haha look at this fucking Rickey rescue
[en4zau1] (score 25, diepte 0) Most people I work with only lose their feet when they don't keep up with their insulin.
[en5b9vf] (score 22, diepte 2) ditto
[en4u97f] (score 20, diepte 1) Do ya protocols not cover you off duty? Whack
[en5z7bc] (score 19, diepte 1) Lol at first sentence... 

Our dispatchers: "med 1 respond to a sick call" 

Us: Show up and find 3 people shot
[en5knax] (score 17, diepte 4) I have some friends who do drugs occasionally and I'm in college so it just wouldn't hurt
[en62cha] (score 16, diepte 1) Wife is a nurse. When we are out in public, I drive a forklift and she works at a bank.
[en4xmds] (score 16, diepte 2) Merica. It’s so fucked makes no sense. I would hate to have to just walk by anyone in distress in fears of getting sued out the ass.
[en4xod7] (score 14, diepte 3) I’m in merica and my standing orders cover me off duty
[en4xvz7] (score 12, diepte 0) Remember that cognitive context is important. When you're working, you're in a work mindset and you are mentally preparing yourself to be at work. State dependent memory is triggered when you are in your uniform, your ambulance, etc. When you're not at work, you have to suddenly switch gears and get into a completely different mindset. 

Think about when you're doing a history of a patient. Everything the patient says you consider within different algorithms and think about follow up questions. There is a power dynamic which allows you to steer the conversation and you can ask invasive personal questions to better treat that patient in a way that would never be acceptable in your personal life. Now imagine you're talking to a friend of yours and they suddenly drop a self-harm red flag. What was a casual conversation now requires you to switch gears and put on your paramedic hat. You take control of the conversation, because that's what you do as a caring medical provider.

You're story is exactly this scenario. You had to completely shift gears and move into your work mode when you weren't in your work environment. And because of that, the mental frameworks that you have set up for yourself weren't quite there.
[en4wgh4] (score 11, diepte 1) Okay I'm glad I'm not the only one who thought this lol
[en5kynu] (score 11, diepte 1) On a call too you have a partner that can can relay any processes to you. When you’re alone all the stress can clog up your mind, and not having that second set of eyes looking out for you can be stressful! Sounds like OP still did a fantastic job regardless
[en4xql5] (score 10, diepte 1) Best thing to do in that scenario.
[en5i0h4] (score 10, diepte 2) Yeah only thing I keep in my car are cravats and burn cream, but that's for myself lol. I wanna get some narcan though
[en5k42c] (score 10, diepte 4) So when he ODs on that sweet juice known as heroin than he can stop himself from dying. 

Isnt that obvious
[en52azv] (score 9, diepte 0) It's being out of your element. Normally we have time to prepare with all steps from toning out at the station, reading about the call enroute, and then taking in the scene from a distance before we're thrown into things. Of course we feel overwhelmed when it's right there without those steps. 

The biggest thing I hate is walk ups to our station instead of calling 911. I go from enjoying down time at the hall to solo running a call until I can alert my partner and get into an assessment. Makes for such a mental cluster.
[en7u408] (score 7, diepte 2) I say garbage man.  Close enough, both pick up trash.
[en5e21p] (score 6, diepte 1) I get the why, but it's still sad that it can be the best thing to do.  Aside from the activation of the appropriate resources sooner, it helps protect you from the potential liability challenges after along with the during and after incident safety.
[en6zldy] (score 5, diepte 1 OP) I should have learned, my inner ricky rescue shone through 

But it’s just shitty tiny bag with a single tourniquet, bandages and some combines / absorbent pads, and a pair of shears. Just enough to stop a bleed if I need, rather look like a dickhead with the kit than need it and not have it. If it was my family member I’d want everything possible to be done.
[en4yxnb] (score 5, diepte 5) BLS level as far as I can tell for the one that authorizes me anywhere in the state.

I’m BLS but my standing orders at the place I work also have the info for ALS. I can’t quite work out what it means but it basically says “while working under the medical director within our service area or while responding to calls from dispatch” which is weird because it would seem to imply that if dispatch doesn’t give us the call that we aren’t authorized to act with the protocols unless in our immediate service area. Would be normal except we frequently do standby outside our service area and there’s no provision for deployments
[en4ylb3] (score 5, diepte 4) Curious if you have some documentation of this - all the education I have on this indicates guidelines do not cover you unless you're actively working for the organization (ie; on the clock).
[en4xrnz] (score 5, diepte 2) If I'm in my district my protocol covers me. 

If I'm the next city over I'm a bystander.
[en4yexf] (score 5, diepte 3) I work for one service and that’s how it is there

I volunteer for another and it literally says “While these protocols are intended to be used by providers while on duty in a [county name] County Volunteer Fire Department’s service area, providers credentialed under these protocols may render the care outlined in these protocols anywhere within the state of Texas, or while personnel credentialed in this system are actively deployed to emergency incidents outside of the state of Texas, subject to the Duty Status guideline listed below.”
[en69rff] (score 5, diepte 2) “Just about” every service. I do know several places that have shit dispatchers but they are definitely outliers

One place has dispatching through the sheriff’s office and the sheriff is supposedly corrupt as hell and views trained dispatchers as a liability. As a result dispatch literally only says “Any available ambulance for a sick person at XXX address street” and the medic crew has to figure out if it’s in their area.
[en5c26f] (score 5, diepte 0) You very likely could have saved his life. Don’t second guess yourself, you have the right instincts and responded excellently to a difficult situation most people would have gawked and ran from.
[en5im3o] (score 4, diepte 3) Why?
[en4z6h4] (score 4, diepte 5) For BLS level, “While these protocols are intended to be used by providers while on duty in [our] service area, providers credentialed under these protocols may render the care outlined in these protocols anywhere within the state of Texas, or while personnel credentialed in this system are actively deployed to emergency incidents outside of the state of Texas, subject to the Duty Status guideline listed below.”

I was told that this is interpreted in a way that authorizes us off duty.

This may be put in context by the fact that our medical director authorizes ECAs to use LMAs, which is either terrible or peak EMS based on your perspective.
[en4zljd] (score 4, diepte 6) That seems like it specifically does *not* allow for off-duty practice, but rather it covers people:

a) outside the service area

b) "actively deployed to emergency incidents" (which suggests a formal deployment in my mind, I'd be there's more detail in the "Duty Status guideline")

Also, what's an ECA? I am unfamiliar with this term, and my Google-fu only returns a UK practice level.
[en579zw] (score 3, diepte 1) This every time this.
[en5knn8] (score 3, diepte 5) Duh
[en6app5] (score 3, diepte 2) I have a go-bag, but the only stuff in it is for dealing with things that *absolutely* cannot wait for an ambulance. Gloves, masks,  NPAs, tourniquets, a shitload of gauze, shears, and a few NADS strips. Every so often, I'm tempted to get some occlusive dressings and some celox or something like that, but that's probably a bit much.
[en4zyre] (score 3, diepte 8) Ah, I thought it went from "first responder" to "EMR".

At any rate, interesting. And yeah, the fact it's a VFD does throw a wrench in it a bit. I'd still be cautious if not actually on a truck/assignment; this country is awfully litigious.
[en58330] (score 3, diepte 7) haha, nope. I’ve never heard of somewhere that requires you to change out of your work clothes for health reasons. I was required to take my uniform shirt and ID off for liability reasons during training.
[en6ev2y] (score 3, diepte 3) >BLS is just first aid CPR

I’m hurt
[en57o9d] (score 3, diepte 2) Hard to say without a detailed breakdown of assessment but motorcycle accident with ejection and altered level of consciousness, etc screams advanced airway, chest needles, and possibly pelvic stabilization
[en5286j] (score 3, diepte 1) https://youtu.be/8X_Ot0k4XJc
[en5q7qq] (score 3, diepte 0) My man I felt the same way the first time I witnessed a cardiac arrest! I was shaking so much I had to ask someone else to try to feel a pulse, it caught me so off guard and to this day I am surprised at how much we take advantage of that few minutes to get in the right headspace when a call comes in. 

I'd call your reaction normal, or we're both fucked up ¯\_(ツ)_/¯
[en6dv6v] (score 3, diepte 0) They did a study a while back (I'll have to go searching for it) on in-hospital providers following ACLS algorithms while rested and after working for set periods (8, 12, 16, 24 hours, etc.). One test group worked in a hospital room they were used to and were able to perform to a very high standard even without rest. 

A second test group used the same ACLS procedures, same amount of rest (or lack thereof), and the same equipment, but were in the ambulance bay. This second group sucked at providing ACLS, even when rested. 

Doing the same job with the same equipment in a different setting messes with providers. It's not just you. Don't sweat it. The research backs up your experience.
[en8czkd] (score 2, diepte 3) >masks, NPAs,

Homie why
[en4zs73] (score 2, diepte 7) ECA = EMR, name changed and I forget which one is current. It’s an emergency care attendant / emergency medical responder.

I know when I did my training I was told that it covers us off-duty, but this protocol is also for a VFD so I suppose we could just claim we are always on duty.
[en504pt] (score 2, diepte 9) It is still basically just a first responder. Authorized to do LMAs lol.

I am cautious in that if I don’t have equipment I don’t tell anyone I’m an EMT

Edit: and I don’t try to help unless they really need help lol
[en4zuzn] (score 2, diepte 4) That'd be nice.

I stop for actual emergencies, but always want to dip out before anyone asks my name...
[en500aq] (score 2, diepte 5) I’d probably stop for an actual emergency but I sure as hell wouldn’t identify myself as an EMT. If I’m driving home from work and see one then I would be sure to take my uniform shirt and my ID badge off before getting out of my car.
[en56in1] (score 2, diepte 6) Do you not change out of uniform at work? That's nasty as hell and would be a massive health code violation over here.
[en5wu6h] (score 2, diepte 7) I mean, I personally do because it's fucking nasty to know how many dirty things my uniform has touched, but it's not a requirement.
[en4ug4p] (score 2, diepte 1) Say you're risking legal liability - what more could they have done?
[en4xpn3] (score 2, diepte 2) Legal liability out the window?

Pulled out their LP15, 3 lead, bp, pox, 18g lock, spiked a bag, intervention as needed.
[en5a04j] (score 2, diepte 1) Even under Good Samaritan laws??
[en5ap1a] (score 2, diepte 2) Correct. Good Samaritan laws cover you for providing aid that an average, well intentioned prudent bystander would provide (bcon, CPR, rescue breathing essentially). If I witnessed an accident with ejection and the victim conked their head and was no longer breathing and I intubated them off duty on the side of the street and it resulted in them surviving, my ass would be sued in a heartbeat and I'd no longer have a paramedic certification
[en6918b] (score 2, diepte 1) You’ve got some good points about “don’t do something, just stand there.” I especially like the dialogue “in your head” - what am I seeing? Why is it like this? Who are these people? Where am I?
[en93gxy] (score 2, diepte 4) I think he had lots of chest pain!!!

Based on the location of this call, they probably were trying to avoid police showing up
[en5j5a9] (score 2, diepte 0) I get it! I’m an seasoned RN. Worked on Med surg, acute care, and urgent. I saw a man get hit while riding his bike. The car stopped and I stopped. Mind u my son was in the car also, “mom! Run go help him. It’s what u do!” But, while running over to help him, all I had was a stethoscope. It’s hard to see it happen in front of u. All I could do was the ABC’s, maintain his spine, check for other injuries and wait. After the ambulance arrived I was able to assist with monitors, and ivs. It was a pack and go! I found out later he had a hemorrhage to his brain and passed. So sometimes no matter how fast someone is there, a pt can’t be saved. All I could do was prey I helped.
[en6y8ax] (score 2, diepte 0) If I lose my $12/hr job and get sued over quite likely saving someone's life when seconds mattered I really don't think I'll care. Maybe I'm alone but that's the least of my concerns. Then again, I work in a state with common sense where someone would never be punished for doing the right thing.
[en6lvxl] (score 1, diepte 3) Im a seasoned medic...all i have in my car is a triangle bandage and gloves.

That said, what is a nads strip?
(20 reacties met lagere score weggelaten)

=== THREAD 1elzsue ===
SUBREDDIT: r/Costco
DATUM: 2024-08-07  SCORE: 480  REACTIES: 86
TITEL: My Costco feet confession
POST (source_id=post):
This happened around half a year ago, but when I went to Costco Business Center, they had mislabeled the chicken feet. It was a box weighing 40.18 pounds, with chicken feet being sold for $0.99/lb. They mislabeled the weight as 0.18lbs and we got charged $0.18 TOTAL. 

When this happened, I thought “no way they’ll actually let me pay for this and let me go through the doors”. I went through a cashier (not self checkout) and they didn’t notice. The receipt person also didn’t look very thoroughly through the receipt. I’m getting this off my chest now that it’s been a few months

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lgvizr0] (score 218, diepte 0) Those things make the most amazing chicken stock.
[lgvjn12] (score 145, diepte 0) That savings nearly paid for your membership.
[lgvjo3q] (score 141, diepte 0) Holy moly, that's a lot of stock for less than a quarter.
[lgvqhgx] (score 94, diepte 0) You've taken your foot fetish too far.
[lgvoamn] (score 67, diepte 1) Chinese dim sum have steamed chicken paws that become gelatinous or you can use it to give your stock a lot of body. It’s full of connective tissue that breaks down to gelatin.
[lgvoeo3] (score 45, diepte 1) Chicken feet that are trimmed up are called “paws”.
[lgvvqud] (score 44, diepte 0) Great, now this sub has devolved into cheap foot pics!

I'll see myself out.
[lgvk8rm] (score 42, diepte 0) "Paws?" LOL they are feet.
[lgwbjjm] (score 38, diepte 1) It's also a Thai delicacy, it's cooked in some red sauce. Loved it as a kid.
[lgvvyf9] (score 33, diepte 2) He only paid $0.18
[lgvypbq] (score 30, diepte 2) 44 lbs of bone would yield about 22-33 quarts depending on how rich you want your stock to be with no added sodium, so it’s a very clean taste and you don’t have to worry about it oversalting your dishes if you reduce it down to concentrate. 

21oz jars of BTB make 25 quarts of stock, but even the reduced sodium varieties are still pretty salty. They also don’t provide the same body for the 1 tsp in 8oz of water. Between the seasonings and yeast extract, and sugar can impact the results of your dish in an undesirable way if used in larger quantities. 

I have BTB and I make stock from scratch, but they have very different purposes in my kitchen.
[lgwc4t5] (score 27, diepte 2) Chinese chicken feet are delicious.
[lgw0qjk] (score 23, diepte 4) You... don't have to use the entire box.
[lgwtler] (score 22, diepte 1 OP) Exactly! Made so much stock and soup out of these
[lgwgk31] (score 20, diepte 1) *Cheep* was right there.
[lgvpss4] (score 17, diepte 2) looks kinda gross, but tastes insanely good.
[lgvlv4o] (score 13, diepte 1) Chicken foot soup is delicious.
[lgw0dj1] (score 11, diepte 4) 44 quarts of good stock will last you a little bit.
[lgvw2q5] (score 11, diepte 1) *OnlyPaws 😂
[lgvkkzk] (score 10, diepte 1) Clearly you have not been on the Internet very long.
[lgw5lh0] (score 9, diepte 3) With the price of previously “cheap” cuts going up, people are learning how to cook with the real offcuts these days to stretch their money.
[lgvp3sb] (score 8, diepte 1) Never tried that. Sounds good.
[lgxs6h8] (score 8, diepte 3 OP) In California
[lgvk1nw] (score 8, diepte 0) What on earth did you use chicken feet for?
[lgvxt64] (score 8, diepte 0) Oh no op, the statute of limitations for this is five years!

Lol, but honestly you did nothing wrong. Curious to see any more feet pics 😍
[lgw12sp] (score 7, diepte 1) Both are so yummy.
[lgwg9ny] (score 6, diepte 2) [and a visual for reference](https://redhousespice.com/wp-content/uploads/2022/04/braised-chicken-feet-1-1367x2048.jpg)
[lgwtg3k] (score 6, diepte 2 OP) That’s exactly what I used it for! Except at some point I realized I had way too much and was just giving them out to friends and family like it was Christmas
[lgw45y4] (score 6, diepte 1) I used to buy them for my pup when I still prepped his food. He got all kinds of stuff. Chicken or duck feet, duck or turkey necks, duck heads, pork brains. It would have been cool to be able to get stuff from Costco.
[lgw557n] (score 6, diepte 2) I recently saw “paws” or chicken feet at my local grocery store. Never saw that before.
[lgvoueq] (score 6, diepte 0) amazing bone broth for a fraction of a penny a gallon
[lgwaxeo] (score 6, diepte 0) I hear you like em young
[lgwh9gs] (score 6, diepte 0) Moved to BC in ‘95, lived in Richmond for 5 years. The different types of food I was exposed to and offered to try by my mostly Chinese classmates was unbelievable. Chicken feet, pork belly, dumplings, char siu, all types of dim sum for their birthdays, it was a glorious time that I’m so grateful for. As someone who was never a picky eater and I’ll try just about anything this slaps.

Years later I learned how to use chicken feet for broth. The collagen and connective tissue really slapped in the winter, I would freeze it in smallish blocks and add bok choy, carrots, and green onions. DELICIOUS.
[lgwj845] (score 5, diepte 1) 🎵If you take it there, I’m taking it further.🎶
[lgxvjbn] (score 4, diepte 4) 40 quarts for $40 is a steal. 40 quarts for .18 even more so. Especially for broth made from bones/skin and not super salty processed cubes/jelly. To each their own.
[lgxikg5] (score 4, diepte 2) It cost 18 cents. 44 is the number of lbs.
[lgvlqsw] (score 4, diepte 0) That’s a lot of feet!
[lgvozti] (score 4, diepte 0) That's cheap dog food
[lgwgbwc] (score 4, diepte 1) crazy that chickens, a terrestrial animal, have feet
[lgwkvct] (score 3, diepte 4) I was bored so here's the math.

40lbs of feet = 40 quarts of stock so $1 per quart.

Better than bouillon chicken = 38 servings = 9.5 quarts so 84¢ per quart assuming the $8 price is correct.

Personally I'm not paying more to process my own stock. That's assuming you have the ability to store and use 40qts of stock or 40lbs of feet.
[lgw6em6] (score 3, diepte 0) Can't buy anything for 18 cents these days.
[lgwiabs] (score 3, diepte 0) Does that say .18 cents
[lgxfc18] (score 3, diepte 0) my husband uses these for dog treats. he has a special mix he tosses them in then dehydrates them.  our dog loves them!
[lgxn86b] (score 2, diepte 2) What location/ country is this picture from?
[lgvw914] (score 2, diepte 1) Cooked the feet to eat as them selves; fried, roasted, braised, ect.   
Or used to flavor soups and stocks.   
They are not meaty but have a lot of tendons to chew on.
[lgzq2gc] (score 2, diepte 1) You better never go to cell block 1
[lgyrxoa] (score 2, diepte 0) Bro they were all celebrating when you PAID to take 40lbs of chicken paws off their hands
[lh21xj9] (score 2, diepte 1 OP) what is wrong with you
[lgvgob0] (score 1, diepte 0) Posts that do not follow r/Costco subreddit rules **MAY** be subject to removal. 

**Reminder: No vague or non-descriptive post titles, this includes questions.**

When applicable, please make sure that you're using a descriptive post title with product name(s) and/or exact question mentioned as it yields better subreddit search results. Including item number, price, and approximate location where found is also helpful as availability can vary.


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Costco) if you have any questions or concerns.*
[lh215fi] (score 1, diepte 4) Open your mind a bit
[lhlzzhs] (score 1, diepte 4) I have to have a degree of separation between what touches the dirtiness, like I don't eat the feathers either. Raising poultry makes you look at a bit differently so I support your decision!
[lh6eb6z] (score 1, diepte 4) What a strange country...
[lgx8q25] (score 1, diepte 1) This would be my dog’s six month supply of dehydrated chicken paws 😂 that’s exactly what I would do with most of those chicken feet!
[lgw0cln] (score 1, diepte 2) WikiPaws
[lgxf5t7] (score 1, diepte 1) chicken feet are used for stock preparation in kitchens all over the world on account of the high amounts of coligen in them.
[lh0v7os] (score 1, diepte 1) Chicken feet are pretty good. Marinate and pressure-cook them. They become like fall-off-the-bone ribs. Some restaurants additionally fry them to give them texture.
[lgvr1ts] (score 1, diepte 0) Dang my dog wishes I was that lucky
[lgvtwmz] (score 1, diepte 0) Cheap stock, if nothing else.
[lgvyf4n] (score 1, diepte 0) These are much better than old chicken paws
[lgvzo7f] (score 1, diepte 0) Soo… did you make soup or something?
[lgw1txr] (score 1, diepte 0) I’ve accidentally walked out without paying for water bottles. I put it at the bottom of the cart and completely forget to scan them, they didn’t notice either. I hope they’ll survive without my $5
[lgw3o6b] (score 1, diepte 0) 👣
[lgw3x4m] (score 1, diepte 0) Frozen Paws

What a terrible day to have eyes.
[lh1z6r9] (score 1, diepte 2) Paws.

why would they refer to them as paws? 

r/woosh
[lgwl7r7] (score 1, diepte 0) Did anyone else zoom in to see what the other person bought?
[lgx5k0a] (score 1, diepte 0) How do you go about getting these?
[lgxz1vg] (score 1, diepte 1) Most business centers should carry em. Call ahead to make sure they have em in stock.
[lgxhn30] (score 1, diepte 0) Sounds like a soundcloud rapper featuring an even more obscure rapper.

Yung Chicken Feat. FrozN Pawz
[lgxquwo] (score 1, diepte 0) What are you cooking that requires that many chicken feet?
[lgxs531] (score 1, diepte 1 OP) I honestly didn’t plan to buy it. Just wanted to get the box to see if I even could lol. But ended up making lots of stock
[lgxv87g] (score 1, diepte 2) Ah makes sense, I didn't know if you were a voodoo doctor or something hahah
[lgxvghe] (score 1, diepte 0) Not Costco but I just got 100 feet of 14g coated copper wire from HD for 0.01 even though it was marked for $18 on the shelf.
[lgybg9v] (score 1, diepte 1) HD does that to a product after they have clearanced an item.  They will list the SKU at .01 so it can still be sold.  Often floor personnel will tell you that you can't buy that item, just so they can.

In your case, HD most likely switched suppliers and you just got a roll of new old stock.  Someone put it in the wrong spot before and then moved it over to the wire where they thought itvm should be.
[lgy0fy8] (score 1, diepte 0) ...and you only paid $0.18 for that? dam... that would be an awesome day to make spicy chicken feet and have a party...
[lgy9plx] (score 1, diepte 0) I own chickens for eggs. I would never eat the feet.
[lgydza0] (score 1, diepte 0) Chickens do not have paws
[lgyl0jj] (score 1, diepte 0) Is that correct price? I can’t imagine the costs to package it are less than the price here.
[lgz2qwl] (score 1, diepte 0) Wait, so was that a mislabel or just how cheap they give them out?
[lgz92rf] (score 1, diepte 0) They should honor the price mistake regardless
[lgzf62u] (score 1, diepte 0) Costco Label Mgr hiding his feetish with the label as “Paws”.
(8 reacties met lagere score weggelaten)

=== THREAD vnxjpi ===
SUBREDDIT: r/AmazonFC
DATUM: 2022-06-30  SCORE: 207  REACTIES: 86
TITEL: Ayo, problem solve, what the feet doing?
POST (source_id=post):
[deleted]

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ie9wd9m] (score 124, diepte 0) I mean I understand if she took off her shoes becuz the safety shoes are uncomfortable af, but where are your socks girl????
[ie9sxib] (score 89, diepte 0) She said “I got those new steel toe feet.” 😂
[iear1ol] (score 46, diepte 0) Damn. She better be careful of the waterspiders.

Those motherfuckers will smell that shit a mile away.
[ie9vdgl] (score 39, diepte 0) Nice ninja pic skills
[ieaq8l2] (score 37, diepte 1) Socks? What are those? 😂
[ie9shts] (score 32, diepte 0) There was a girl at my building that took of her safety shoes and used the poly bags for shoes instead.
[ieavw3f] (score 25, diepte 0) What is even going on at some Amazon's?!?!?! People acting like they are at the beach or some shit.
[ie9zyka] (score 24, diepte 0) Delete! This is an Osha violation
[ieablhs] (score 22, diepte 0) She got the dogs all out lmao. I know that whole area probably smelled crazy
[iea0f3p] (score 16, diepte 0) What's that smell?!?! 😉
[iea20kw] (score 16, diepte 0) 🤮
[iea7v9x] (score 15, diepte 0) I bet that feels hella good tho lol.
[ieaceo2] (score 15, diepte 0) Thats wildd 😭🤢
[ie9zwyn] (score 14, diepte 0) Oh hell no…..
[iecdkf4] (score 13, diepte 1) Them things hurt ong!
[iealatd] (score 13, diepte 0) That floor is gross AF
[ie9yfmc] (score 12, diepte 0) ![gif](giphy|12P6AnN6DcQj1S|downsized)
[ieaq9dt] (score 10, diepte 1) Did she stick a slam label on them as well?
[ieaqla3] (score 10, diepte 0) Worse thing is those aren’t even safety shoes those just adidas lmaoo
[iebt7c0] (score 10, diepte 1) Oh god not the water spiders
[iedqi4w] (score 9, diepte 3) Found the water spider
[ie9zwsu] (score 8, diepte 1) I do that in Damageland 🤷🏽‍♀️
Dirty ass floor
[ieaqbr1] (score 8, diepte 1) What is? The feet? Or me posting?
[ieadi9s] (score 8, diepte 1) Jail!!! Straight to jail!
[ieciubf] (score 7, diepte 2) Dayum let me massage them on the clock though 🌚
[iedubef] (score 7, diepte 1) We should start an osha violation thread. Amazon edition.
[iea1f2z] (score 7, diepte 0) This is what I wish I could do
[ieak33z] (score 7, diepte 0) Never seen that at my building. But they’d definitely would be in socks! Lol I miss working there. Might go back.
[ieaqag5] (score 6, diepte 1) Yessir
[iebnygc] (score 5, diepte 1) I think that’s why it should be posted lol
[iea06v8] (score 5, diepte 0) 🤮
[ieai9eq] (score 5, diepte 0) Ahh hell no, a cave woman. 😆
[ieal8d5] (score 3, diepte 1) Dude, no
[ieatsk5] (score 3, diepte 0) Damn. 

The insides of my toes are itchy just looking at this.
[ieaxznw] (score 3, diepte 0) I did the same but outside away from everyone at lunch. (later when’s there’s have room)

Sprankle a lil bit baby powder, get some athletic socks for airflow, get steel toe running shoes for safety and increased airflow and comfort all day long. Cost like $60 total inflation adjusted. 

That way you won’t be in puddles
[ieazf75] (score 3, diepte 0) Swine feet!
[ieb07s9] (score 3, diepte 0) \*gestures vaguely in OSHA\*
[ieb5ybj] (score 3, diepte 0) Foot fetish people having a good time rn
[iebsa81] (score 3, diepte 0) These are the type of people that don't wear socks outside, then proceed to fucking put their dirty ass feet all over the carpet, furniture and whatever else. Fucking animals
[ieaqa62] (score 2, diepte 2) Gotta stick to where all the hazmats are though
[ieb5hcb] (score 2, diepte 0) That’s how they do it in India man
[ieb71o9] (score 2, diepte 0) why u snitchin

jk
[iebd0hu] (score 2, diepte 0) Put those grippers away 🤢
[iebgg4c] (score 2, diepte 0) That's nasty at least have socks for that dirty floor
[iebh9fg] (score 2, diepte 0) Throws the fuck up
[iebo90q] (score 2, diepte 0) She got steel toes

They were 100% off on Zappos 

It’d be funnier if she just had the things they make you wear over your shoes lmao
[iebt3yt] (score 2, diepte 0) EYYOOO WHAT
[iebx1t9] (score 2, diepte 0) PUT THOSE GRIPPERS AWAY !
[iedqaqz] (score 2, diepte 0) Probably going to end up with toenail & skin fungus knowing how “ clean “ that area is lol
[ie9rm0t] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[iee7mmg] (score 1, diepte 4) Honestly man, some of the water spiders in general have no chill
[iee7kn8] (score 1, diepte 3) *hops on chime*
[ieh8y4x] (score 1, diepte 2) If osha sees it on here and go to rhe building they will let the site leaser know theu are there because of what was posted on social media. Site leaders will then attempt to "hunt down" whoever posted it for violating the social media policy and fore the employee for the offence of posting it. The person commotting the actual osha violation will be "coached" or written up. Thats why i said delete.
[ieh9uwj] (score 1, diepte 3) Lol that’s a longshot
[iehab0q] (score 1, diepte 4) No its not lol people get fired for posting on social media akl the time(seen it in my building) osha violations get the building fined by Osha. You think your site leader want to explain that to their bosses? Jist want the OP to be safe and not risk a job they may need over feet pics
[iee8d9k] (score 1, diepte 2) Let’s get it
[iee7tim] (score 1, diepte 1) The dogs out
[iee7quo] (score 1, diepte 1) With that dirty ass floor
[ieaqde5] (score 1, diepte 1) That’s why I stick as far out from PS as much as I can. When I train, Jesus. PTO me out
[ieb8lkv] (score 1, diepte 1) Crusty
[iebtdjz] (score 1, diepte 1) Bro she better watch out for the water spiders
[iebdr6z] (score 1, diepte 0) Makes me wonder if they do this at our Problem solve area too 🤢
[iebfh21] (score 1, diepte 0) nice 😏
[iebodnn] (score 1, diepte 0) They catching a disease from that nasty floor
[iec2erj] (score 1, diepte 0) I’m always take my shoes off but never my socks lol
[iec2xjl] (score 1, diepte 0) Not standing on these dirty ass floors ![gif](emote|free_emotes_pack|joy)
[iec4x96] (score 1, diepte 0) That big ass knot on the side of her foot needs some attention.
[iec6qua] (score 1, diepte 0) Lmaoo
[iec9zmj] (score 1, diepte 0) 📸
[iecdhls] (score 1, diepte 0) Hurting! WHAT IT LOOK LIKE! 🤣
[iecgggm] (score 1, diepte 0) Problem solves does not claim her.
[ieck2u9] (score 1, diepte 0) Return those shoes if got from Zappos and get the puma touring safety shoes. They look like regular shoes and are bevy comfortable.
[iecknn8] (score 1, diepte 0) Id be worried to stand on that barefooted
[iecp81c] (score 1, diepte 0) Nah she tripping dirty ass floor 😂
[iecx8ms] (score 1, diepte 0) When you use the full "Amazon discount"
[iedbcsd] (score 1, diepte 0) lol she said fuck it 😂
[iedo5em] (score 1, diepte 0) Imagine being in this and seeing someone exposed you lmao 
I’d actually shit myself
[ieeev4y] (score 1, diepte 0) Listen I saw someone come in with crocs but put the safety covers over it haha
[iemmags] (score 1, diepte 0) Might as well be comfortable. 😅
[ie9zygx] (score -5, diepte 0) That's not creepy at all ![gif](emote|free_emotes_pack|disapproval)

