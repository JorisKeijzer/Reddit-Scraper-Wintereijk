# Label-batch batch_0134

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
Schrijf het resultaat naar `batch_0134.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1r6lfwa, 14bs3cs, 1gid4pt).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1r6lfwa ===
SUBREDDIT: r/flightattendants
DATUM: 2026-02-16  SCORE: 393  REACTIES: 66
TITEL: Ok. I may have to concede a little about the feet thing.
POST (source_id=post):
For the longest time I truly did not understand why people get so worked up about feet on planes. Every time a flight attendant posts a pic of a passenger with their shoes off the comments are:

“JAIL.”
“NO FLY LIST.”
“why are people like this.”

And I would just be like… it’s literally a foot.

Flying is uncomfortable. Your feet swell. Shoes get tight. If someone wants to take their shoes off and let their dogs breathe for a few hours, I genuinely did not care. I have never been the toe police. Even when crew would complain about people going to the lav in socks, I was like okay?? We are already in a metal tube in the sky. Pick your battles. It’s not like it’s my socks absorbing the piss on the floor. 

But.

I was working business class on a widebody international flight and this man took his shoes off.

And the smell was immediate. Undeniably feet. Not subtle. Not questionable. Just straight-up aggressive foot odor.

It hit me the second I walked past his seat. And it did not leave. It smelled the entire flight. I’m not even kidding or exaggerating. The *entire* flight. Every single time I passed his row it was a fresh wave. My stomach was literally turning. I was nauseous. I would hold my breath and speed-walk past him like I was doing a drill. Smile on my face, lungs empty, fighting for survival.

And like I said, this is business class. On a *long* international flight.

There was a passenger a row ahead of him, window seat, who had her blanket pulled completely over her head almost the entire flight. And I am almost positive it was because of his feet. I can’t prove it. But the math was mathing.

At one point another crew member walked by his row and later came up to me like, “You did not warn me.” lmfaooooo.

If your feet require a warning to the rest of the crew before entering the aisle, we have crossed into unacceptable territory.

That was the moment I understood.

I still don’t care if people take their shoes off. I’m not offended by toes. We’re all just trying to be comfortable.

But if your feet smell like they are fighting demons? Please. Contain that situation. Keep the dogs secured. Especially in business class on a long-haul flight.

Take your shoes off if you must. Just make sure your situation is under control.

I have officially seen the light.

For the AA people who understand this bit of context: he was an EP—nice guy, gave me an A&B but DAMN those dogs need to come with a warning. 😂

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[o5r6tpt] (score 86, diepte 0) I tell this story as often as I can.... 

I was coming out of a drinking destination and after takeoff a young gal ran to the back galley and proceeded to soak me, the curtain, and the floor with projectile chunky vomit. After I got her situated in a bathroom, a woman approached with bare feet. I told her there is chunky vomit all over the floor between the two lavs. She shurgged her shoulders and paraded slish-slosh right through chunky vomit in bare feet right into the piss soaked floor of the aft lav.
[o5r0lu1] (score 70, diepte 0) Sometimes when people don’t smell themselves I just want to ask if they truly can’t smell it or if they just dgaf
[o5rb4qm] (score 50, diepte 1 OP) Germs fear HER lmao. Absolutely disgusting, but I lowkey wish I had that brazen, maybe almost foolish courage 😂 I can’t flush with the toilet lid open and if my toothbrush accidentally falls on *my own* bathroom floor I’m googling how to disinfect it lol
[o5sk01e] (score 35, diepte 1) They absolutely can smell it.  I was a waitress as a teen, on my feet ALL day wearing white nurse shoes back in the 80's.  Those damned shoes made my feet stink so bad.  I was so horrified to even take them off at home, let alone in the car on my way home.  I would NEVER have taken them off on a plane, that's for sure.  It's freaking RUDE AF.
[o5receq] (score 34, diepte 0) Passenger here. Thank you for this post. I have taken my shoes off due to swelling and intense burning pain from
r/erythromelalgia. But I keep them in socks, and they are so clean, and I keep them as close to my body as possible… super self-conscious. I know people hate feet and I avoid it except extreme cases. I do not walk barefoot either; I wear slip-ons/stretchy sneakers. 

But people like this guy ruin it for all of us. Once you encounter bad feet it really does ruin it for you. 

And lastly I want to add that I understand what you mean about business class, but also cattle class would be just as bad due to tighter quarters… ugh. His poor neighbors. I wish someone had been brave enough to say something. My go-to is an innocent question: foot problems? Or something like that.
[o5r27qa] (score 20, diepte 0) Great analogy, love your writing skills. I also think, the rule you mentioned is applicable anywhere in the aircraft and not only just in the front cabin of the aircraft.
[o5rm0iv] (score 19, diepte 2 OP) I’m about to start posting my journalism degree every time I write a coherent paragraph 😂 is that really such a novelty now?
[o5rwkux] (score 15, diepte 3 OP) I’ve heard that about the em dash, which is such a shame because that’s my favorite way to punctuate lol. It mimics in-person conversation so well. And if ChatGPT is modeled after us, do we sound like AI, or does AI sound like us?
[o5rmb04] (score 15, diepte 1 OP) We need to bring back shame lol
[o5rx3b0] (score 14, diepte 3) Or perhaps an educated person who writes well. I use em dashes, too. Lots of people use them.
[o5rz99j] (score 13, diepte 4) My wife has a masters in English composition. She uses em dashes, Oxford commas, and ellipses frequently. Proper punctuation doesn't mean something is AI, it just makes reading easier. The thing is, when you get really good at writing, you use things like unique punctuation and sentence structure intentionally. Sometimes you even write things that are intentionally not correct to create voice. Your writing has voice. AI writing often lacks voice.
[o5r3wou] (score 12, diepte 0) On one red-eye from Denver, the passenger behind me put his sock-covered foot onto the back of my armrest. I discovered this because I was resting my head against the wall and I started smelling feces. I've pushed a foot off before years ago but this time I didn't. I was too angry.
[o5scs3g] (score 12, diepte 1 OP) There are some flight attendants who would do something like that, but I don’t feel comfortable putting myself in a situation where I could be written up. He was traveling in widebody business class and has status with my airline, so if he decided to complain, he’d probably get some miles out of it and I’d end up with a passenger complaint in my file. I prefer to fly under the radar as much as possible.
[o5r34er] (score 11, diepte 1 OP) Thank you! & True—probably even more so for main cabin where we’re all packed like sardines
[o5r9btv] (score 11, diepte 1) Eeeeeweeeeeewwwwww☠️
[o5rwqno] (score 11, diepte 0) Traveling with a small container of Vicks vapor rub for your nostrils can be a flight saver in these situations
[o5su5zc] (score 8, diepte 0) One time when I was deadheading on a flight, I saw this lady who was sitting across from me dig in each individual one of her toes and smell what she dug out of them. She was wearing flip-flops and she did 1 foot at a time on her lap, and she proceeded to touch the air vent and at one point almost touched me when she was asking a question and I screamed
[o5rhoah] (score 7, diepte 0) Traveler here: I had someone take their shoes and socks off and proceed to clip their toenails while singing in a tone deaf manner to whatever music was playing on their headphones.
[o5tmble] (score 7, diepte 2) It’s times like these that make me wish I didn’t know how to read.
[o5sa76w] (score 7, diepte 0) Can I ask a totally uneducated question that’s gonna sound rude but I truly don’t mean it that way?

Why didn’t you ask them to put their shoes on? As a passenger, I’d hope a flight attendant would take care of something obviously disturbing other people, versus a fellow passenger needing to awkwardly complain to get it resolved
[o5t3twz] (score 7, diepte 2) If I'd paid for the same class as he did, I would expect something to be done.
[o5s94oc] (score 6, diepte 4) I use the M dash quite a bit myself - so sad that it's the mark of chatGPT
[o5srdji] (score 6, diepte 1) I wish you could see my face 😱😱😱as I read this. OMG the absolute horror. What is wrong with people???!!!!??
[o5t4z42] (score 6, diepte 1) Last year on a flight to Amsterdam a guy sitting next to me started clipping his toenails I tried to ignore him as he took his shoes off, then his socks but the second I saw him cut one gnarly toenail I lost my mind. I said so loudly ARE YOU KIDDING ME? CLIPPING YOUR NAILS ON AN AIRPLANE? My friend next to me immediately pressed the call light. I was so pissed. This is the second time in 5 years I have seen a man’s gnarly toes. In Denver 4 years ago I was waiting for my connection and a guy in the terminal was digging gunk out of his toes.
[o5rkh1d] (score 6, diepte 0) Passenger here. My eyes were stinging on a flight within Europe once from the vile odor of feet. I checked. My shoes were on.  Neighbors had their shoes on. Aha!  It was the cheese I bought in France.  It was delicious but it stank most righteously.
[o5rk02l] (score 5, diepte 0) Many years ago I was on UAL ATL-IAH. I was seated at the window and he was on the isle seat.  During the flight, he decided it was time for toenail clipping.  Oh the joy of toenail clippings flying left and right of his ministrations.
[o5sm95z] (score 5, diepte 1) I would not allow that. The Contract of Carriage requires passengers to be fully clothed on our flights; we can use that to make people put shoes on, but you should pick your battles. I would absolutely use it to enforce the rule in this case, though.
[o5rm0a2] (score 5, diepte 0) Passengers should change into their inflight shoes just like we do, but it’s slippers made to look like a loafer 😂
[o5tm5pr] (score 5, diepte 2) Afrin makes an unmedicated Vapor Burst Inhaler that is sooo much stronger/better than Vicks!
[o5s4mcp] (score 5, diepte 0) I have given people warm wash cloths & access to the largest washroom before because of their stench. If you are impacting the health of other crew & passengers (feeling nauseated is health related) then you are a disruptive passenger and I need to intervene for everyone’s sake! 

btw - love your writing style! I do the odd comedy social media reel of a flight attendant doing rants and this is comedy gold!
[o5sfe62] (score 5, diepte 1) My question too. 

I’d beg the FA to ask him. The complaining ca go both ways. One could call, complain FA wouldn’t ask grotesque passenger to wrap up his hooves and get miles outta the airline.  That poor gal with the blanket over her head!! Ugh!
[o5sfmc4] (score 4, diepte 1) I… I can’t even fathom… I… I… I’m speechless. I’d spend the ENTIRE flight fantasizing about his horrific and painful death. What a tool.
[o5rwdgb] (score 4, diepte 0) I feel like the easy answer to this is to just wear sandals if you know you are gonna want to take your shoes off. Feet smell after they have been trapped in a shoe especially if they are sweaty. At least with sandals they are easy to slide on and off and don’t generally make your feet smell.
[o5s3133] (score 4, diepte 1) With all the inflight issues that I read now, I will have the Vicks with me when I travel on 2/22. Thanks for sharing information
[o5s2h9f] (score 4, diepte 0) I bring a pair of clean, thick, fuzzy socks that I put on every flight. And I put my shoes on over them when I go to the bathroom.

If people have a problem with that, they can kiss my ass.

This dude is foul though.
[o5t0d43] (score 4, diepte 2) What if another passenger asked you to ask him to put his shoes back on. Would that give you cover?
[o5tfc0e] (score 3, diepte 1) I've stepped in way worse, but I always have a way to clean it off.  I also wear compression socks on planes so I don't feel like I need to take my shoes off.
[o5s3ogi] (score 3, diepte 1) I just want to say that I also have EM, so I totally understand the intense burning, swelling, and pain. I usually can't take my shoes off, though, or they would swell even more and not fit back into my shoes.
[o5uq7cu] (score 3, diepte 2) why the «lol» you’re absolutely right we do! 

In all aspects of society
[o5xa27q] (score 3, diepte 1) I worked at a pizza place in my early twenties and witnessed the owner walking up and down between the (INCONCEIVABLY empty 🤪) tables clipping his fingernails. Needless to say, that pizza place is long gone.
[o5t4955] (score 3, diepte 1) I did this as well on a return flight home from Paris. Next time, I will try to insulate the freezer bag better, because leaving without some cheese from the Duty Free seems like a real shame.
[o5ufc9k] (score 3, diepte 3) I like those Thai inhalers! Also stronger than Vicks. And if the Vicks-y smell isn’t for you, boy smells makes a citrus inhaler that’s great for this too!
[o5sebw5] (score 3, diepte 0) One time a pax took her shoes off (she was wearing sandals) and was just rubbing her bare feet with her hands. Then she tried to hand me trash in MY bare hands. I was like "oh no" and went to the back to put gloves on bc I just went to heat my food up. 

If a pax takes their shoes off, that's on them. But they better not complain about stepping in urine on the lav floor bc why did you walk in there with no shoes on?
[o6g0ihq] (score 2, diepte 2) I bet they were SASS shoes. I would take mine off in the parking garage after work and have to put them in the trunk. WTH? No other shoe has ever smelled like those things.
[o6hg8g9] (score 2, diepte 2) I’ve gotta say that some people, smokers for example, cannot smell it. I live with one. Trust me.
[o5somub] (score 2, diepte 1) 🤢
[o5trw4x] (score 2, diepte 1) Erythromelalgia?  Wow!  My sympathies.
[o5u5b05] (score 2, diepte 2) You get it! I have also seen that in a terminal.
[o6oriis] (score 2, diepte 3) The flight attendants were so much nicer than me. They told him he had to keep his socks on and no personal grooming in the seat. We just ignored each other the rest of the flight. I’m still mad!
[o5tarjs] (score 2, diepte 1) If I'm planning to take my shoes off on a long flight, I stop by the bathroom near the gate to change my socks and hit my feet with a quick alcohol wipe. Entirely fixes the problem.
[o5rzyap] (score 2, diepte 0) I had to go sockless on one flight, I dozed off with a cup of water in my hand and soaked my socks. Was definitely a fast way to wake up. Luckily I was in business and had those little slippers handy still in their plastic so they were protected. Was able to shove my shoes with socks draped over them under the seat in front to let them dry. I now fly with a spare pair of socks in my personal item bag.
[o5tb0aj] (score 2, diepte 1) If your airline has those little alcohol wipes, those work great.
[o5s787j] (score 2, diepte 0) I think I flew next to this guy on a recent business class flight back from Istanbul. It was so bad I almost called the flight attendant, but then felt like a wuss for not fighting my own battles. Just as I was about to say something to him, he put his socks back on and things got better enough to the point where I could fall asleep.
[o5snd4c] (score 2, diepte 0) I have a loose cotton bag that I use for shoe storage when I fly that would mitigate this! I will pack it and then hope that any passenger whose feet stink will just accept my offer and put it on.
[o5uvpqo] (score 2, diepte 0) Maintainer here. I feel like the pilots should have made an announcement that they can smell it and will have to do an emergency pressure dump for fear of incapacitation. That or declared that they will have to return due to the threat of a chemical attack in the air system
[o600j3w] (score 2, diepte 0) You did not warn me lol
[o60ig7p] (score 2, diepte 0) shoes off but keep socks on
[o65btn0] (score 2, diepte 0) Got on a flight and an hour in a stench hit me in the face like a punch. I was gagging. I got up to walk toward the back of the plane to see if I would feel better. I did, but as I returned silent tendrils of moldy cabbage assailed my nostrils. The man in front of me had removed shoes and socks and was clipping his toenails. There wasn’t anyone else in his row as was a half full flight. The flight attendant allowed me to move.
[o6g1rdx] (score 1, diepte 3) You know what, I think they might have been. That's funny.  I think I threw them in the dumpster and bought Nurse Mates with the heart logo.
[o609ebp] (score 1, diepte 1) As a teen I used to have super stinky feet and couldn’t smell them. It went away eventually, but the only reason I knew it happened was because I was made aware, thankfully. It’s possible not to know :(
[o6o50vu] (score 1, diepte 2) Don’t leave us hanging,,,what happened next?
[o5u67hb] (score 1, diepte 1) 🤣
[o5sr9xo] (score 1, diepte 0) One time a teenager took his shoes off and it smelled like cheesy funk over several aisles. I felt so sorry for the people sitting there.
[o5uyt6n] (score 1, diepte 0) ...but you gave me amenity socks to wear during the flight
[o5vzwhr] (score 1, diepte 0) Next time, accidentally spill whiskey on your feet, sorry, and the coast will be clear 😜

Seriously, if a passenger complains because their neighbor has sweaty armpits, they have to get off… Do you really have to put up with everything??
[o5wr6x7] (score 1, diepte 0) Keep it cute and be subtle but definitely make the passenger aware that they smell bad. I keep air freshener on me at all times during work. I will politely go through and spray a few spritz. If it's as bad as you described it, the area by his seat would likely get a few extra sprays. If it's still too bad after that, I'm the FA that's comfortable enough to pull a passenger to the side and explain that they are making others in the cabin uncomfortable with their body odors. Offer a solution and help as best you can so they don't feel embarrassed or uncomfortable. I've learned that many people don't realize how bad they smell because they are desensitized to their own scents. 

Also open feet in the cabin is insane for actual health reasons. We all know these airplanes are not adequately cleaned. Someone barefoot on the plane is just asking for some type of fungal, staph or bacterial infection 🥴 not to mention, their sweaty stinky unwashed feet only add to the bacteria and germs. It's a perspective thing really. The guy who sat in the same seat on the last flight stepped in dog shit that morning and tracked residue onto the plane not you have your 5 little piggies rubbing across literal shit stains that you don't even notice because airlines use dark color flooring for a reason 💀
[o5zhnby] (score 1, diepte 0) Interesting. I take my shoes off to AVOID the feet stank. After years in combat boots, I hate sweaty, smelly feet. I always use antiperspirant w/deadorant and take my shoes off at any opportunity. Gotta let the dogs breath! And keep your socks dry folks!
[o5zlc2e] (score 1, diepte 0) Ew! Who would take the shoes off without socks on? Question, if this happened in a flight and somebody complained about the smell, would you ask them to put socks on?
[o6e309b] (score 1, diepte 0) In flight amputation an option?
[o6fv919] (score 1, diepte 0) I would just pass them a legit handful of the little sanitizing wipes… Like an almost comical amount so he gets the point.

I’m not a FA and don’t even know why this popped up on my feed, but I’d probably do this as a passenger if the smell was that bad and I was sitting next to them.
[o6gnafq] (score 1, diepte 0) Reading this from a flight to/from tropical destinations. Only have flip flops. Forgot socks. My feet are so cold.
(6 reacties met lagere score weggelaten)

=== THREAD 14bs3cs ===
SUBREDDIT: r/Fibromyalgia
DATUM: 2023-06-17  SCORE: 75  REACTIES: 66
TITEL: Tight achilles tendon and calf muscles, plantar fasciitis
POST (source_id=post):
Anyone else here deal with this? I've had fibro symptoms for many years and only recently got diagnosed with fibro, but I noticed over the last couple of months, my leg muscles have become extremely tight, specifically the achiles tendon and calf muscles. I also have plantar fasciitis, especially in the left foot.  I've been doing stretches as instructed by my providers, taking pain meds when necessary, using heating pads/ice packs. Trying to find a balance between exercise and rest. There's not much else I can do. I did a nerve conduction velocity test where they sent jolts throughout areas in my legs.  Doctor concluded he did not find nerve pain in the legs, but what I'm dealing with is very deep muscle pain throughout my legs. I'm set to see my pcp next month about my results.

My legs are almost always hurting, making it difficult to do normal everyday things I used to do effortlessly. 😔

Anyone going through a similar thing? What did you do to cope/manage it?

Edit: thank you for the tips and suggestions 😊 I'm very grateful and I got a list going of all the things I'm going to try. As this is a newer symptom for me, this is very helpful

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[joh2dx9] (score 16, diepte 0) Yep I have all of the above :) stretching, hot baths & good quality shoes/insoles are the only things I have that help. I’m not on any kind of pain meds either so everyday is just the same pain over and over again. It’s not easy
[johbtkd] (score 11, diepte 0) I get bad fascia tightening in my calves during the hotter months. Myofascial release, rest, and epsom salt soaks have helped but it’s just a consistent seasonal challenge for me.
[joh6k49] (score 9, diepte 0) I have had the same problem and I’m so sorry you’re having to deal with this. It’s miserable having to hobble around. I developed very painful plantar fasciitis while wearing Skechers w/ foam insoles. At first they felt great, but if wearing them at work all day, they did something horrible to my feet. I tried everything the docs recommend: a splint/foot brace that keeps the toes flexed to wear at night, special socks w/ built in inserts for cold packs to wear during sleep, tried massage with a spiky ball, wore open-toed compression Sox at night, and massaged my heels/ankles w/ voltaren gel. None of those really helped, though the cold feet socks seemed to help the most (and relieved my temp regulation issues—I’m always hot at night!). Finally, I got some Brooks sneakers (Ghost) and the pain went away pretty quickly and haven’t had issues since unless I wear other types of shoes that don’t have that nice cushioning. Best of luck trying to get some relief! The right shoes are def key.
[joh63l0] (score 6, diepte 1 OP) I'm sorry you deal with that:( but thank you for helping me not feel alone. This is a fairly new symptom for me, I was only recently diagnosed and prior to this, I walked around like it was nothing. I'm still getting used to all of this
[joh91sr] (score 6, diepte 0) Hi.  Unfortunately I've had this so long.  It's uncomfortable.  I would recommend continuing to do your therapy.  That's all we can do.  Take it easy.
[johz3gk] (score 6, diepte 0) Something that has been a huge help with tight/sore soft tissue area is a massage gun. I’ve  used it almost everyday for the past year. When it’s fully charged it lasts about 70 minutes and I use it while watching tv. I started on the lowest setting on the least sore part of my body slowly working my way to the sorest areas.
[joh82uo] (score 5, diepte 1) The worst part for me on orthotics is being 6’10”!  It was already hard enough to find clothes being tall, but when I started to need special shoes it felt impossible.
[joho2ou] (score 5, diepte 1) Hmm mine started after using sketchers work shoes said shoes are also falling apart at an alarming rate I've had like 5-6 months off work due to foot problems since wearing the bastards.
[joioyp9] (score 4, diepte 2) Check out Orthofeet.  They sell wide shoes, up to 4x wide in men's shoes (double wide for women).  Their shoes come with removable arch supports and extra padding if the shoe is too wide for you.

I've been having knee pain and Achilles tendon pain that have been better since I got my new sandals a couple days ago.
[joim5z6] (score 4, diepte 2) Temperature sensitivity is also a fibro thing. Seems most of us have issues with either hot or cold.
[joior0v] (score 4, diepte 0) Yeah , I've had this since I was a kid . Probably 25 years +   way before my fibromyalgia diagnosis

I've tried orthopaedic insoles and all the exercises.  The insoles can cause other problems like back pain and joint pain.  I don't use them now , really good trainers like Asics help the most.  I also have a pair of trainers I wear as slippers, this probably helps the most as I can't walk barefoot or with flat soles.
[johtw3e] (score 3, diepte 1) Ooh I did the shots in my feet! I accidentally kicked my doctor in the face while saying “fuck!” Not my proudest moment.😂
[joik072] (score 3, diepte 1) This just started for me. I didn’t get it cold weather! Never associated the two
[johl1ri] (score 3, diepte 0) I have severe myofascial pain syndrome (muscles turn into ropes of knots). If I can find the trigger/origin point, arnica gel or magnesium lotion or cannabis salve can help.
[johmjsv] (score 3, diepte 0) I had to change all my shoes once I got plantar fasciitis, never walk barefoot, even to go for a pee in the night. I also got acupuncture treatments for it and it worked amazingly. But my body reacts very well to acupuncture.
[johokzk] (score 3, diepte 0) I have tight neck muscle & calves. I just decided to try some 3:1 thc:cbd lotion for it, and after two days my neck is loosening up for the first time in years after failed TPI and muscle relaxers.
[johppxc] (score 3, diepte 1) Yeah a CBD roll on as well as edible CBD helps me a TON with muscle issues!
[johssbf] (score 3, diepte 0) Normal - this comes up every so often for me. My legs and feet are a the biggest source of pain and for a long time I didn’t get a FM diagnosis because I thought my pain was only there but it wasn’t, it was just overshadowing pain in other places. I’ve tried a lot of shoes and many home remedies… I encourage you to try things until they work for you. 

I wear crocs almost exclusively. I’m a lady and I love the Adrina style crocs… they look like a jelly/sandal and feels like clouds. These shoes really helped the leg and foot pain. When the plantar fasciitis flares I wear croc slippers all day long, I don’t even step out of bed without stepping into a shoe. If I have to pee, the shoes go on and then come off to get back into bed. This tactic helps the plantar fascia to relax and become less inflamed. Whenever you walk barefoot (especially without a carpet) it causes your feet to stretch and irritate the plantar fascia. Don’t do this. Wear a soft but supportive shoe at all times. When you are sitting on the couch, bring out some frozen water bottles (the cheap plastic disposable kind) and roll your feet on them for a little bit. This part isn’t mandatory but helps the pain a bit. If it’s winter time, put them in the fridge instead of the freezer. I reuse the same two bottles. There is also an acupuncture point on the back of your leg called [UB57](https://www.pinterest.com/pin/458733912049156517/). It’s right below the belly of your calf muscles. When I’m sitting I cross my legs and drape the top leg so that the bottom leg  knee is putting pressure on that point. It relaxes the calf and Achilles tendon. Apply pressure for no longer than a minute of two before switching. It’s deeply important you don’t push too hard or too often with FM - to avoid causing more pain. That’s why I like the crossed legs technique.
[johu9f1] (score 3, diepte 0) I’ve done stretches, shots, heating pad, etc. I find a combination of all of that plus finding the trigger points helps. One crazy thing I found was a Japanese onsen near me. It’s crazy hot, I can only stand to put my legs in, but that heat really helps. You can only do it for a short time, it’s very very hot. Basically as hot as it can be without hurting you. But I found the relief lasted days. Good luck!
[joi5qe6] (score 3, diepte 0) I have the same issue, and I've been getting high intensity shockwave treatment from my physiotherapist. It really hurts, but it's been super effective. If you can tolerate the treatment, I absolutely reccomend it.
[joh634i] (score 2, diepte 0) Orthotics help!
[joh6a12] (score 2, diepte 2 OP) In the meantime I am going to get better shoes soon, but the ones I have now thankfully offer a decent enough support
[joh77n4] (score 2, diepte 1 OP) Thank you so much for your insight 🙏
[joijbep] (score 2, diepte 2) Get you some Brooks if you can. I suffered for months then relief came pretty quickly after switching to them.
[jojysyg] (score 2, diepte 1) Thank you so much for this. As a sketchers fan with very bad planters fasciitis that has tried everything, I literally just ran to buy a pair of the ghosts! 💛💛💛
[joh9j7u] (score 2, diepte 1 OP) Thank you. I'm sorry you're dealing with this too. I'm going into physical therapy soon on top of everything else I've been doing. You take it easy too ❤️
[mlv18h3] (score 2, diepte 2) For me it hasn't changed.  I have other things,  comorbidities that are always making life, life. I hope this makes sense.
[joh9t1x] (score 2, diepte 0) Have you gotten a steroid shot for the plantar fasciitis? It hurts quite a bit (but if you did the nerve test, you’ll probably be fine!) but it helped me quite a bit. I pretty much got 1 shot every year or so for a few years. 

Then I had a kid and stopped working and now I don’t have any foot pain (which the ortho facetiously suggested I quite working to stop my foot pain 🙄).
[johbjf6] (score 2, diepte 2) I hope you are able to try one! My first orthopedic visit set me up with inserts and a prescription for shoes (at work I would rotate Danskos and my prescribed sneakers with inserts). When I still had pain, he gave me a shot. Supposedly you only need 1 shot to “fix” it, but my job was very physical and I refused surgery. 

And thanks! I wish all my pain went away but I got pregnant and had a baby and my pains changed and I got some new ones, thus is fibro. Good luck to you!
[kqlsh1t] (score 2, diepte 1) Hey!!! I’m experiencing this right now and this comment right here helped me so much! Thank you! I was just diagnosed and I’m trying so hard to understand it all.
[joidt11] (score 2, diepte 1 OP) I was just talking with my girlfriend about the time my friend had some cannabis salve and let me try it out. It is so useful! We don't have the money to do much yet, taking care or car troubles, but were getting there. I'll add this to my list. Thank you for the suggestions 😊
[jojc61b] (score 2, diepte 2) I’ve honestly gotten better results with products that contain arnica and magnesium, that’s why I listed them first.  They’re easy to find at the drug store too.  Biofreeze is a favorite of mine (arnica and Indian frankincense).  

Also, cannabis salve doesn’t have to be expensive and can be as simple as cooking some cannabis in olive oil, letting it cool and using that for a massage.  Even a small amount can help. You can get pretty far with a quarter cup of olive oil and a fat joint worth of weed.  

I hope you find something that works for you. It’s miserable to hurt all the time.
[joir1j4] (score 2, diepte 2) I found that a pair of thick soled sheepskin slippers work wonderfully for around the house
[johnlhp] (score 2, diepte 0) I had to run at work and ended up with a sore foot. I hurt all the time so I didn’t think much of it. It has never gotten well and now a year later there are time it hurts so bad I can barely walk. I keep buying different shoes and insoles trying to find relief. My chiropractor says it is my Achilles tendon and plantar fasciitis. Since adjusting my foot hasn’t been successful, my chiropractor says I should try PT. A coworker, who does not have fibro, says she was previously put in a boot for 6weeks to allow her foot to heal
[joiu3md] (score 2, diepte 2) Cloud 9 by Nature's Grace.
[johpcsa] (score 2, diepte 0) Yes, I have to stretch my Achilles daily. It's uncomfortable and seems like a waste of time. But last summer I got Achilles tendonitis and I was limping around for a long time. So I have to do the stretches.
[ltvgzsv] (score 2, diepte 3) Thank you so much! Just checked these out and they look very promising, would definitely try incorporating these in my routine, thank you again.
[johs87e] (score 2, diepte 0) Custom orthotics can really help with PF.  Never go bare foot except in the shower.  Don’t wear open back shoes/sandals.  Wear a hard soled shoe.  Wearing a shoe with a flexible sole creates more micro tears in the tendon running along the bottom of your foot.  PF is one of over 20 medical issues associated with Fibromyalgia.  I have very tight Achilles tendons too.  I’ve been in PT a couple if times just for that.
[johszfg] (score 2, diepte 0) I definitely have a lot of chronic tension. I take a muscle relaxer every night (cyclobenzaprine). Stretching etc can help, but I still need to treat this with my medication.
[joi1ub6] (score 2, diepte 0) Hey I feel you, anytime someone touches my Achilles tendon, I’m in pain for hours. I’m a 13 year old boy that has had fibromyalgia since 9. I can really have my “manhood” tested seeing all these boys around me being fine, but that’s beside the point. I used to have pain all around my body, but ever since Chiropractor, Acupuncture, and Personal Trainer, it’s been getting much better, and is usually only in my lower back, legs, feet, and last but most, Achilles tendon.
[joi30nm] (score 2, diepte 0) Yes, I went through this for a long time but I’ve finally been able to fix it. A few things have helped a lot - collagen peptides, stretching (preferably in the hot tub), massage gun and I only exercise with Altra shoes (zero drop, the paradigms fixed my plantar fasciitis) and compression sleeves on my legs. I’ve come so far with this and I’m generally pretty pain free.
[joi8jry] (score 2, diepte 0) If you can stand it Rolfing and dry needling have helped me the most. I had this back pain since the pandemic started thanks to the stress. I did everything I could think of, massage, pt, acupuncture, chiropractic, trigger point injections. I finally found an excellent dry needling therapist, we’ve been working for a year and my pain is finally becoming manageable not only back but other muscles as well.
[joi8ub9] (score 2, diepte 0) Yes. Lots of insoles, baths, Arnica and yoga.
[joid4a8] (score 2, diepte 0) I have the same, Muscle relaxers helped for years.
[joigq2c] (score 2, diepte 0) What calf stretches are you doing and how long are you holding? How often are you doing them? 
What shoes do you wear, and do you go barefoot in the house?
[joiln7y] (score 2, diepte 1 OP) I'm doing the one where you put your hands on the wall and put one foot back and one at the wall, bending the knee of the leg close to the wall to stretch the achilles tendon. I do 4 sets on each side once a day. My foot doctor didn't tell me how long to hold it so I've been aiming for 10 seconds.

The place i went to get the custom shoe inserts, he told me when looking for a new shoe, make sure it isn't easily bendable. Unfortunately we haven't had the funds to get the custom inserts or new shoes, but here soon I'll be able to. For now I dug thru my closet and found a pair of shoes that aren't easily bendable but they are old so it's on my top priority to do list to get a new pair. 

My whole life I've been going barefoot in home. I've been trying to remember not to, I have been slipping up. Right now I'm wearing slippers after just getting out of the bath. 

This symptom is new to me as I used to walk all the time with no issues and could wear whatever shoes I wanted. I also have HEDs, and I got an xray of my bone structure in my feet and it's normal, however my foot arches are still collapsing when I walk, especially the left foot, due to the hypermobility. I also pronate when I walk which also causes pain.

Edit: I also do hamstring stretches using a towel, 4 on each leg once a day, also holding for about ten seconds
[joiofvm] (score 2, diepte 2) I’d shoot for every couple hours throughout the day and a good 20-30 second hold, and the shoes and orthotics should help immensely. You can also use orthotic sandals in place of slippers if you tend to wear slippers a lot. Depending on your age, some degree of arch collapse is normal. They kind of naturally start to fall after 50 as a result of aging, and over pronation is related to the low/flat arches. Shoes and orthotics will also help immensely with this
[joioz19] (score 2, diepte 2) Also make sure when you’re doing the stretches your feet are both pointed straight ahead and your shoulders are directly over your hips with your back straight for the best stretch
[joj4uqw] (score 2, diepte 0) 100%  Couldn't even get out of bed it hurt the bottom of my feet so bad going into the back  Ankle all the way up to my calves. You can't even touch them it feels like a bruise.

I was a physical therapy for almost a year. A few months back they told me that I should leave now at this point even though I qualify forForever physical therapy according to my fibromyalgia diagnose.

Going to physical therapy helped me tremendously with not only my feet, less overall pain but having enough strength to actually feel like I was living a normal life again. 

I was beyond pissed off when the main PT therapist wanted me out.  I was very compliant and didn't bother anybody. She told me I need to start transitioning over to a gym which there are none around me.

So as of now?? I am now bed ridden again pretty much, and severe pain again most days  and I'm right back to square one. 

 It really is vital that if you have fibromyalgia that you work out. Of course we don't like to, it's a pain in the ass,  It's still uncomfortable but it beats the hell out of the alternate of  being bedridden again. 

Of course you learn techniques to do at home but it's still not enough. When you're home you tend not to do them until yourself you'll do it tomorrow. And then there are certain machines that you need that I doubt any of us have at home including one of those medical hard table beds that you need to do some of the fibromyalgia PT on.

Fortunately for me we do have a new gym that is opening close by, I'm already signed up just waiting for to open. However I have to start back again from the beginning and slowly work my way and try to remamber how to do everything.

If you can, though look on YouTube, there's a couple of great PT therapists who do work with plantar fasciitis and try to follow or ask your doctor to get you in physical therapy.  I also got steroid shots in the bottom of my feet in the beginning to help.

Crocs also helped.  Never thought I would wear them now I'm hooked with like 8 pairs.
[joj5c9o] (score 2, diepte 0) I've had some problems like you are describing, and what has helped me is magnesium (I use taurate and glycinate), and wearing SAS shoes has helped A LOT.
[jojghjf] (score 2, diepte 0) I only wear Ortho approved shoes . I have had these troubles since I was 19. Most of my clothes are cheap but my shoes are always expensive.
(38 reacties met lagere score weggelaten)

=== THREAD 1gid4pt ===
SUBREDDIT: r/BuyItForLife
DATUM: 2024-11-03  SCORE: 27  REACTIES: 65
TITEL: Looking for a comfortable and durable walking shoe for 300lb person
POST (source_id=post):
Something with arch support and won’t fall apart after a month or two of wearing.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lv4fwu1] (score 84, diepte 0) I wear a New Balance 928v3 in leather.  
You'll still have to replace them yearly, because there is no BIFL walking shoe for dudes our size.
[lv63x0t] (score 32, diepte 1) Even if you're half that weight, shoes are not BIFL in general unless you can resole them.
[lv4mlj7] (score 32, diepte 0) I'm in a similar boat as you. I went to a running store and got fitted for a pair of Hokas. They have held up beautifully and are still comfortable after a year of mostly daily wearing. They are even still comfortable after back to back 20K step days at a theme park.  If you have the option to go somewhere and get fitted, I'd recommend it. Some of the other brands and even some of the models of Hoka felt terrible on my feet.
[lv4hes9] (score 28, diepte 0) I'm 275lbs, down from 319lbs.  ON Cloudmonsters are unreal. A few years back, I had to have a bone fused in my foot. I have had foot pain ever since. The ON shoes are the first shoes that I don't have daily foot pain
[lv571n9] (score 15, diepte 1) Yeah that's going to be the trouble when you're on the heavier side of things. Unless you got that mass as a body builder, having that much body fat is really going to mess up your gait, usually leading to more friction on the soles with each step. 

It's why I stopped going for squishy sneakers for my daily wear, and spent more on resoleable leather boots. I can always resole them when they wear out, so they're much closer to BIFL, especially since it's good leather that I maintain well with cleaning and treatment every few months.
[lv4i9vd] (score 15, diepte 0) Not the same weight, but as someone with joint problems Hokas have been a dream
[lv4sgff] (score 13, diepte 1) Hmm. Wouldn't walking help this person "get healthy again?" This comment feels silly and your downvotes are completely deserved.
[lv4wgpg] (score 9, diepte 1) I wore New Balance 1080's and their predecessors for decades, but my Hokas are way better. No shoes are BIFL, but these are very comfortable for those of us who are gravitationally  challenged.
[lv4sueb] (score 7, diepte 1) Every extra 10 pounds above ideal-ish body weight puts an extra 30lbs of force on your knees when you are walking on level ground.

You’re on the buy it for life sub-Reddit; the only thing you’ve got for your whole life is your body and the best thing you can do is take care of it. 

And get those hokas, they’re awesome. 

https://www.hopkinsarthritis.org/patient-corner/disease-management/role-of-body-weight-in-osteoarthritis/
[lv593bg] (score 6, diepte 0) I've read a few places that alternative shoes/ not wearing the same pair everyday is really impactful in keeping them in good shape for longer... 


So.if your budget I'd get two pairs and switched back and forth
[lv5e7w3] (score 4, diepte 1) OP didn’t ask about exercise advice. 

OP didn’t ask for what you think their starting weight *should* be. 

You’re coming across as a fatphobic person who thought it would be a good use of your time if you provided unhelpful and unsolicited advice and judgements to someone who’s looking to buy sustainable footwear but who isn’t the weight that you believe they should be while posting this request.
[lv4wxia] (score 4, diepte 3) Running at 300 lbs. is not realistic if this person is over 20. They need a less high-impact form of exercise.
[lv4nuvg] (score 3, diepte 1) I'm currently using Speedgoat 5s and love them.
[lv5ad0d] (score 3, diepte 0) I been running a pair of brooks glycerins, they have a bunch of shoes that fall into different categories. I think mine was about stability but they lasted pretty well for a year for me, they are starting to break down after my trip overseas tho
[lv60l7j] (score 2, diepte 1) This is the right answer.  These are Pdac approved too, so if you are type 2 diabetic, insurance will cover 1 pair a year, with custom insoles.
[lv623l1] (score 2, diepte 2) OP got it anyway. That’s the internet for ya
[lv4kzfo] (score 2, diepte 0) I'm currently 287. My Orthofeet Yari held up pretty well but I think the cushioning has compressed faster than other sneakers. 

I bought the first pair a couple months before the second pair, and wore them more than the second pair. I figure I wore the first pair maybe 8 months, and the second, which is still comfortable, 4 months. On the plus side, the upper hasn't torn, and the outsole still has most of its tread. But like I wrote above I think the first pair are done, so I got some new shoes.

Hoka have been pretty good. I think they don't last quite as well as New Balance or Brooks (both of which give me back problems), but I never felt like the soles gave out and they were comfortable. On the other hand, the upper tore away from the sole toward the end of its life, and that might have happened on more than one pair. I remember it for one, but can't recall if it happened on two. They definitely lasted less than 9 months.

I just got a new pair of Saucony Echelon 9, and today is the first day I've worn them. No foot or back pain, and I was standing and walking quite a bit, 3.8 miles, nearly 9,000 steps. I think they're slightly narrow, which usually bothers me, but for some reason not this time. They felt a little odd when I first put them on, but I didn't notice anything once I started really walking in them. I just need to tighten up the right shoe a little.

Since you mention arch support, the Orthofeet are nice because they come with a set of insoles and removable arch peace. Though the Saucony suits my arch without adjustment. I guess I have an average arch.

Even though I like the Orthofeet Yari, I also got boots from them which I don't like at all. It took me a while to realize it, but they don't fit well unlike the sneakers. If I get anything from them again I'll be more careful or just stick with the Yari.

I guess I can recommend Brooks and New Balance as long as you don't have lower back problems. They reach the usual 9 month mark, and tend not to develop split uppers or feel bad toward the end of their life. I used to wear them until the tread was gone. Though the Orthofeet Yari has a nice soft outsole, which I like because it grips better and doesn't squeak in wetness, where as New Balance and Brooks tend to have stiffer treads which are a little more prone to slip and squeak on wet metal. I don't know about the Echelon 9 yet but I think it's kind of in the middle.

Someone in another post mentioned Kizik, and their Lima seems interesting. I haven't tried it but I like hands free entry, and I'll probably get a pair soon.
[lv5ueh5] (score 2, diepte 2) Yeah apparently i am the asshole here :/ Just wanted to wish him a more healthy life
[lv5wblt] (score 2, diepte 3) As a person who has a reflex to give others unwanted advice, I keep having to learn that if people don't ask it's best not to share. Because of that, it sticks out to me when I see others doing it. Apologies for my harsh comment.

You seem well-intentioned, so I will tell you this: For people who weigh 300 pounds "Please get healthy again," is something they already know needs to happen. They can't erase extra pounds *right now* and their feet need shoes that work *right now,* so when they ask for help with that second thing... comments about that first thing are not as helpful as you intend them to be.

You aren't an asshole. You just seem not to have thought about this question from the perspective of the person who asked it :) 

Now *I* just gave *you* unasked-for advice. I can't stop myself.
[lv4vqle] (score 2, diepte 0) I used to wear new balance, but after i started wearing work boots, they felt like crepe soles compared to the overall supporr I got feom the boots.  My best pair now is red wings and I wear pedag insoles for extra arch supporr.
[lv4duew] (score 1, diepte 0) You might want to aim for anything with a solid or non-EVA foam sole.  I wear Dr. Comfort myself (mostly because they have space for orthotics within) but there are plenty of competitors.
[nvh9chb] (score 1, diepte 2) You guys are dumbass. I have had my new balance and my addition walkers for 12 and almost 4:years. . 
I weight 285 my soles are fine, change your damn insole right there in the store with a fitting by fleet feet.  Change them every 2 years . They last that long , if you wash your feet once in a while.
[lv740kl] (score 1, diepte 2) You're best off looking in the refurbished section of a shoe store
[nvh8qmk] (score 1, diepte 2) You guys talk shit. I'm 285 . I have addiction walkers and new balance 928 line. 
12  years old . Soles still good, leather still good . I change insole 2 years at a time . 
My addiction walkers by brooks are 3 years almost 4. You don't keep the insoles that come in these shoes . You put fleet feet insoles in them. . A lot of these people don't wash their feet, cause they can't see them.  If you're tearing up these shoes that fast , you need to change your habits and learn to take care of shit. I walk hours every . Switch off my shoes every week...
[nvhlzj1] (score 1, diepte 3) Uh.... my shoes aren't torn up, and I absolutely do wash my feet and I can absolutely see them WTF lol. I still need to change them. 12 years is way too look for your shoes to absorb any impact when you walk. Sure they'll still look okay, but they've lost their bounce.
[nzk38r8] (score 1, diepte 4) Ignore this baboon.
[nvh7rjw] (score 1, diepte 1) Change your insoles ! Dude I have 12:year old 928s . 
Wash your feet too once in a while. Im 285 #
[ok9ea05] (score 1, diepte 2) How's the sizing on the 928 model? I wear size US 9 in the 990v6 but size 10 in the 574 model. Idk what size to order. 9 9.5 or 10.
[mxl14aa] (score 1, diepte 1) > ON Cloudmonsters

Which did you get? I'm looking their site now. I get nervous spending so much on shoes but I trust you random internet homie.
[lv6e4ta] (score 1, diepte 2) I got the gaviota 4s a year and a half ago, and they’re still holding up
[lv4joxl] (score 1, diepte 0) Would also recommend the new balance 1040 v13/v14
[nvh9x0n] (score 1, diepte 1) Addiction walkers. Almost 4 years old. My new balance are 12. 
Get fitted at a reputable store like fleet feet. Including the insoles. 
Both pair are still like new. Trade the insoles out every 2 years and swap shoes weekly . And the most important thing ! Air your shoes out keep them dry and wash your feet.
[lv5wvs9] (score 1, diepte 4) Yeah from my point of view i just saw a person who already has issues because of his weight and instead working on that he looked for a "workaround" with better shoes which won't help longterm.I agree with you that i gave unwanted advice.Shouldn't have done that.So no offense take for your comment
[lv5xq8r] (score 1, diepte 5) I appreciate your courtesy. I hope you have a lovely day :)
[lv4qpt3] (score 1, diepte 0) New Balance 993. Made in USA. They make them in wide and extra wide. I’m on my third pair. They look good too
[lv4tco1] (score 1, diepte 0) Have you looked at an injection molded PU shoe like the Lowa Renegade? Being stiffer than EVA and non-compressible they should give more support and hold up better than the typical walking/running shoe. You'll need to put in the insoles that work for you, few like most shoes they don't come with arch support but they do accommodate them well
[lv4tfyj] (score 1, diepte 0) I had a foot doctor reccomend The Beast to me. It's fantastic, comes in many wide soles as well.
[lv4vi37] (score 1, diepte 0) Shoes are very specific to the individual so you may have to try a few different brands. My husband is about 250 and does best with New Balance (he wears through hokas in no time). Here is a NB shoe that has been surprisingly great for him: [link](https://www.zappos.com/p/mens-new-balance-fresh-foam-t510v6-h2o-resist/product/9919083). He’s been wearing his current pair for 6 months with very high mileage ~ 20K steps a day and they still look great and have good cushioning.
[lv4wqyx] (score 1, diepte 0) I love New Balance, and the wide widths are not hard to find. For walking I like a cross trainer. I buy two pairs for myself on every birthday. If you use them for exercise, make sure you have two pairs and rotate which pair you wear each day. I walk at least 1.2 miles the vast majority of days.
[lv57atg] (score 1, diepte 0) If your shoes wear more on exterior, altra escalante/lone peak. If inside you'd probably like new balance.
[lv5dlvn] (score 1, diepte 0) Idk if I’ve just had good luck but every pair of reeboks I’ve owned have lasted me 5+ years. 

I didn’t necessarily wear them daily but I was overweight when I used them (i switched to a different brand for unrelated reasons). Though I’d say at some point I would wear them 4-5 days per week, and it didn’t *seem* to accelerate the wearing out process.

And for whatever it’s worth: I have extremely easily-injured feet and my sensory issues make it so that I *cannot*  handle breaking in new shoes if it involves *any* discomfort. So I’m very picky about my shoes.


(This part of the comment is not answering OP’s question, so apologies for that ahead of time. I just wanted to say a small thanks to everyone in this thread who’s handling the weight aspect of this post in some of the most mature, supportive ways I’ve seen on Reddit. Even the fatphobic/discriminatory/biased comments are handled so well and it’s very encouraging and heartwarming to see, as someone who has dealt with similar experiences and needs for good walking shoes as OP described)
[lv5gv5a] (score 1, diepte 0) Honestly - and this seems like a crazy answer - get a good pair of resolable boots. My go-to for really heavy walking days is a pair of Danners. They weigh almost 3 pounds each, but my feet feel so much better at the end of the day than any shoes I’ve ever worn. 

I replace the insoles every year with a good pair with arch support (timberland pro works, superfeet are good, too). They’re 6 years old at this point, but if you take good care of the uppers with a good, thick leather conditioner when they start to look dry, they’ll last a lifetime.
[lv5ka2h] (score 1, diepte 0) ASICS! They have great options for balance and flat feet
[lv5obl0] (score 1, diepte 0) I recommend checking out the New Balance 990 series or the Brooks Ghost series. Both offer great arch support and are designed for durability, making them suitable for walking. Also, consider the ASICS Gel-Kayano for extra cushioning and support. These should hold up well for daily use
[lv5pvbf] (score 1, diepte 0) Brooks Ghost 15

They're like walking on supportive pillows.
[lv5wbzy] (score 1, diepte 0) Brooks (adrenaline 23 gts if looking for lots stability)
[lv680wu] (score 1, diepte 0) If you have a lot of money, I’d look into going to the Good Feet store and get measured for their orthotics.
[lv68hmc] (score 1, diepte 0) Honestly, pretty much no shoes on the market have enough arch support for me (except for Birkenstocks and my beloved chacos), so I have to put insoles in everything. My favorites are Superfeet green and tread labs, but it takes some experimenting to figure out what works for you. Both insoles can last a long time, but tread labs is more on the bifl end of the spectrum as you can swap out the cover for a new one when it wears out for relatively cheap.
[lv6du0n] (score 1, diepte 0) Remember your shoes are like tires for your car. You get new tires all the time. Same with your shoes. It’s called a wearable item for a reason.
[lv6jksl] (score 1, diepte 0) I’m around 380 and I wear brooks especially since they accommodate super wide feet. Make sure you get the right width otherwise you’ll wear out your shoes extra fast, but the support it gives for me is pretty good. Not that I can go on long runs, but I wouldn’t imagine attempting to run without it.
[lv6jz1r] (score 1, diepte 0) I wear Adidas Ultraboost and they last about 5-6 months of daily wear, which for me is enough. Very comfortable and can accommodate the foot well with the “mesh” exterior
[lv6ln6z] (score 1, diepte 0) My Jordan CMFT Low’s have been amazing. Just bought another pair after wearing them daily over the past year. I do a lot of walking as a nurse and these held up so much better than any other shoe I’ve tried.
[lv6ukxx] (score 1, diepte 0) Your health should be your #1 investment. Get the best shoes, but find it in your budget to hire a personal trainer. Best investment you’ll ever make.
[lv7yttu] (score 1, diepte 0) It’s absurd how long the Brooks ghost lasts
[lv87wjg] (score 1, diepte 0) SAS shoes come in a wide range of sizes and are very comfortable. I don’t think any shoe is BIFL, unless it’s repair-able. But I have lots of SAS shoes and while they aren’t the latest fashion, they are made here and very comfortable
[lv9dsb6] (score 1, diepte 0) 300lb 💀💀💀
[lvahia4] (score 1, diepte 0) Your weight bears no role in shoe selection, so mentioning it is moot.

You buy shoes based on size which is length and width.  Arch metrics, which aren't a thing, are not part of the shoe purchase equation, so mentioning it is moot.  If you have footbed desires, you need to visit a podiatrist or feet store for custom orthotics.
[lvbsl1g] (score 1, diepte 0) Try insoles-- don't need to go for bespoke ones right away, the Dr. School's heavy duty ones helped me when I was ~260
[nvh6xhl] (score 1, diepte 0) Brooks addiction walker. Go and get fitted though. Some 2e are narrow , you may need a 4e 
They will hold up And last for years. You can also get replacement insoles for around 60 .
The shoes themselves are 130.
[lv4cg5m] (score 0, diepte 0) Hello /u/fightoffyourdemons90! Thank you for your submission! just to inform you, you may also want to try posting in /r/boots which is a smaller subreddit but might be or specialized for your request

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/BuyItForLife) if you have any questions or concerns.*
[lv4fqpm] (score 0, diepte 0) It’s not bifl unless you count that I bought 6 pairs in case they get discontinued but this is by far the most comfortable shoe I’ve ever walked in: https://www.amazon.com/Rockport-Get-Your-Kicks-Loafer

I know it doesn’t look it but it’s great
[lv62tsz] (score 0, diepte 2) Quit using logic. They only want to hear about shoes, none of which are BIFL at 300 lbs
[lvbdcdp] (score 0, diepte 3) You have absolutely no idea what the OP is or isn’t doing. Their question is what shoes are best for them *now*, where they are.
[lvc65ej] (score 0, diepte 4) Safe to assume they’re not doing much at 300 lbs
[lv4n2dc] (score 0, diepte 0) New balance. Any of the models over $120
[lv4opqn] (score -1, diepte 0) Check out Lems
[lv5u5l4] (score -1, diepte 1) 😠 OP didn’t ask for your opinion about their weight.
[lv4x6a1] (score -3, diepte 4) Or walking.Any exercise is good as long as you don't hurt yourself doing so
[lv4syc2] (score -17, diepte 2) That's why i recommended getting custom shoes because they will help him with running without pain.Sorry if this gets interpreted the wrong way.I just think that good shoes doesn't fix the problem as much as getting to normal weight will.But one doesn't exclude the other obviously
[lv4g448] (score -22, diepte 0) What's your shoe size? Your weight isn't that big of a factor to be honest. I'd recommend birkenstocks but if you've got very large or wide feet they will not work
[lv4qiel] (score -22, diepte 0) Please get healthy again 🙏. Probably not the answer you want to hear but please work on getting rid off the root of your problems instead of accepting them and working around them.You doctor might be able to refer you to a specialist making you custom shoes if necessary
(1 reacties met lagere score weggelaten)

