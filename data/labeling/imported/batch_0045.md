# Label-batch batch_0045

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
Schrijf het resultaat naar `batch_0045.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: tr6rmu, 18qm2ms, bzozza, vvd7hh).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD tr6rmu ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2022-03-29  SCORE: 1221  REACTIES: 149
TITEL: This is how I work being 198cm/6.4 feet
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[i2l20se] (score 254, diepte 0) I stack two 3" butcher blocks under my cutting board. Although, this is a better way to fight swamp ass!
[i2l1fzn] (score 174, diepte 0) If you’re goin’ wide you need some cut off Jean shorts.
[i2lg4lg] (score 108, diepte 1) Oh I can go wider
[i2lkjkk] (score 89, diepte 0) This way people have access to your balls from behind, God bless.
[i2l2yy1] (score 45, diepte 1) I do a combo of both lol
[i2mcfyc] (score 43, diepte 2) The shorts don’t prevent me from doing what I need to do.
[i2lc345] (score 37, diepte 0) This seems smarter than doing The Quasimodo like I do
[i2l4u8u] (score 36, diepte 0) I've seen tall chef put a 4 or 6.inch under their cutting board, maybe worth a shot
[i2m6eil] (score 35, diepte 1) This dude could also wear something more breathable than jeans, absolute mad lad. I'd be sweating my balls off if I wore  jeans in the kitchens I worked in
[i2lgo63] (score 31, diepte 0) As a tall guy myself this is low key the most genius thing I’ve seen in a while. I have no idea why I’ve been doing this hunchbacked.
[i2nzkpy] (score 31, diepte 2) Normal workplaces: "You made a dick joke I'm going to HR"

Kitchen: "let me readjust your anal virginity real quick"
[i2l8vjw] (score 30, diepte 1) Hotel pan upside down on a towel, board on a towel on that.
[i2ne8is] (score 28, diepte 3) But you gotta take em off every now and then. You gotta take em off, son!
[i2maei3] (score 24, diepte 0) We have a 6’5” baker and when we redid our kitchen we made his workbench sized for him. A little uncomfortable for everyone else but everything else is a little uncomfortable for him.
[i2lk3sm] (score 23, diepte 0) The power stance. Helps with back pain too.
[i2lz2rb] (score 22, diepte 0) That’s the power stance bro. Rest of the staff sees me standing like that they know I mean business.
[i2mkl9n] (score 21, diepte 2) Well, the jeans are an important part of the outfit, they really go well with his hiking sandals and socks....
[i2ngj07] (score 18, diepte 4) You’ll blow the crotch out them shits
[i2lz77s] (score 16, diepte 1) And there’s definitely nothing white trash about that
[i2ma4se] (score 16, diepte 1) Have fun standing like this doing prep for a few hours. Just put an upside down crate or gastro/hotel pan under your cutting board.
[i2mj4q1] (score 16, diepte 1) Kanchō!
[i2l2lyu] (score 15, diepte 1) "Jorts"
[i2lodhj] (score 15, diepte 1) Just make sure you keep some awesome fray on them.
[i2negqf] (score 13, diepte 1) If I'm being honest, this is about how low I can get.
[i2l5fc7] (score 12, diepte 2) I as well do a combo.
[i2l5k4a] (score 12, diepte 1) Gotta angle that air mover to blow up your pants leg.
[i2m21ak] (score 11, diepte 1) Plus with a power stance everything is more powerful.
[i2lr7fs] (score 9, diepte 2) That’s why I specifically said cut off’s instead of jorts. Gotta have the fray.
[i2lgfca] (score 9, diepte 0) Same here my tall brother 😂😂
[i2lyrlk] (score 8, diepte 2) If your jean shorts don’t make a fringe rug blush are they really jean shorts?
[i2nbhv8] (score 8, diepte 1) Lol, I just hunch under the hood and apply cheese like I'm feeding baby birds.
[i2llhyt] (score 8, diepte 0) Spread them cheeks chef I’m cumming in!
[i2noe96] (score 7, diepte 2) I’m so clumsy though! I feel like I’d end up knocking it over.
[i2o974b] (score 7, diepte 3) Stack up 4 or 5 boards (or however many you have to spare) with a wet towel in between each one. Way more stable
[i2nkn5z] (score 6, diepte 3) 1-2 glass racks with towels. But as the day goes on, this guy knows what’s up.
[i2njtmj] (score 6, diepte 2) Fucking was the dress code in Chili's when I was there
[i2oc2yd] (score 6, diepte 1) Imagine my embarrassment after having my legs hacked to a more sensible length!
[i2m8jw1] (score 6, diepte 0) 198cm is 6.6 feet.
[i2l0diy] (score 5, diepte 0) I do this move a lot. mostly to chat with serving staff
[i2nf0sz] (score 5, diepte 2) Needs a Gibson and an amp.
[i2lqjq4] (score 5, diepte 0) Why I can’t go back to the restaurant industry. Fuckers have me in a full neck bend looking down on a 3ft counter,shits annoying



Edit: by annoying I mean my neck is in a full fucked  up position permanently now
[i2m3bi4] (score 5, diepte 0) This is how you get cup-checked with a towel.
[i2mhhmk] (score 5, diepte 0) i always feel bad for the taller ones. cracking their heads off the hood vent, always having to reach for the higher stuff for everyone. you folks should get hazard pay.
[i2ngdoy] (score 4, diepte 2) Might try this.
[i2n9wa8] (score 4, diepte 1) 6.4 ft = 6'6"
[i2mk5je] (score 4, diepte 1) I'm at 5'6, the tallest woman in the kitchen. The shortest person in our kitchen is maybe 5'0? I swear to God I had a heart attack watching our dishie stand on the tippy top of the stepstool to hang up the pots. I almost grabbed him round the middle to put him back on the ground. I know the feeling, wanting to do everything yourself, but sweet jesus I can grab those pots like I'm picking fruit. He shouldn't have to do that.
[i2ny8dq] (score 4, diepte 2) Don't tell me how to live my life.
[i2p2ez3] (score 3, diepte 1) I do this at places with workbenches that are way too low, luckily now I work in a kitchen designed for people who are 6ft.
[i2ob1kq] (score 3, diepte 1) I'm pretty sure Anthony bourdain has a tutorial on that using a meat fork
[i2oodjd] (score 3, diepte 1 OP) Asserting dominance in the kitchen !
[i2m3k49] (score 3, diepte 0) I think you're on to something here OP..

To clarify: I am also 6'4"
[i2m3k7f] (score 3, diepte 0) Standing at 6'5" myself, I deeply relate to this,
[i2m7xho] (score 3, diepte 0) You know If I did that I’d bet my coworkers will try to kick me in balls just for the fun of it.
[i2m8d4j] (score 3, diepte 0) I'm the same height. In my kitchen they call that my "power stance"
[i2m8w0x] (score 3, diepte 0) Power stance so everyone knows you don’t mess around
[i2mj1ig] (score 3, diepte 1) Aw that's so sweet
[i2ngave] (score 3, diepte 0) I'm 6'3", it's not that bad.
[i2ntmjd] (score 3, diepte 0) The worst part about being tall in a kitchen is the counters are usually right at dick level. That's generally not an issue until you have to pull some plastic wrap on a low humidity day and you get a nice shock directly to your junk. That's pretty annoying.
[i2qco6x] (score 3, diepte 0) ikr. We giraffes get no respect.
[i2mfcdy] (score 2, diepte 1) Cut em tight. Jeados.
[i2s38dl] (score 2, diepte 3) I fucked a bag of combos once cause I thought the dust would add friction.
[i2pcvl9] (score 2, diepte 2) My old job dark blue Jean's was part of the dress code belt and a tucked in work shirt it got very sweaty some days
[i2l364y] (score 2, diepte 0) Do you ever round up to 200cm?
[i2ld1af] (score 2, diepte 0) I’ve raised my primary prep counter, stand like this, and out my board on an inverted dish rack to raise it up about 4 inches. The struggle is real.
[i2lytmq] (score 2, diepte 0) I used to do this as a dishie back in the day. Hunching over the sink for hours at a time was killing my back until I figured out this power stance.
[i2m4fbc] (score 2, diepte 0) Towel, buspan, towel, cutting board, save your hips dude
[i2ndjhs] (score 2, diepte 2) 6.4 ft = 6’4.75”
[i2nde0o] (score 2, diepte 1) 6.6 ft is 201 cm
[i2m9vog] (score 2, diepte 0) To clarify, 198cm is 6'6 but OP wrote 6.4 which is correct but causes confusion
[i2majwe] (score 2, diepte 0) Much better than leaning over so the food is closer to the face. I always encourage newbie’s to nip that in the bud. That neck and shoulder pain will stay with you. And you just look like a blind idiot
[i2mam1l] (score 2, diepte 0) And apparently a ton of women find this sexy on tinder. In fact, this picture should be on your tinder profile...
[i2mh69l] (score 2, diepte 0) Dude I’m 6’4” as well. I know your struggle brother.
[i2mhtqg] (score 2, diepte 0) 5"8 is the like chef 6"0
[i2mij8b] (score 2, diepte 0) You’ve got long balls Larry.
[i2mz9m7] (score 2, diepte 0) Hips will not last with that pose.
[i2n3436] (score 2, diepte 0) 198cm is 6'6, just so you're aware
[i2nc9l1] (score 2, diepte 0) Bro I feel you. Counters were not made for us giants. Sinks neither, my back fucked me so hard. Grill was reasonable somehow though, that was interesting...
[i2nu12s] (score 2, diepte 1) Your penis is supposed to be INSIDE your pants.
[i2oc9p9] (score 2, diepte 0) A lot of people have to work by spreading their legs.
[i2ombhk] (score 2, diepte 0) had to do this at my old job for comfortable work surface height. I'm 6 feet tall. It should not be that way.
(69 reacties met lagere score weggelaten)

=== THREAD 18qm2ms ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2023-12-25  SCORE: 145  REACTIES: 142
TITEL: First, he blocks off a breaker box with a shelf and hangs it seven feet off the floor.
POST (source_id=post):
Second, he hangs a shelf from a shelf and leaves the shelf above it clear. “I NEED MMOOAARRRR RAAACKKS!!”
It’s him!!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kevs0yz] (score 149, diepte 0) Well, it's not a breaker box, so that's good.  It's most likely a controller for a walk-in, exhausting, or something similar.  Breakers have to be at a reachable height from standing.
[kew2ady] (score 142, diepte 2) I’m mean we don’t need to see any more. We’ve seen, and it’s not a breaker box and can be blocked
[kevtjxs] (score 141, diepte 0) It’s a control box, not breaker. Can block that.
[kew995k] (score 104, diepte 0) These fucking  posts 🤦
[kewd9vh] (score 86, diepte 4) I’m saying to you, and we’re saying to you, it is a control box, and therefore a shelf can be in front of it and the same rules don’t apply to it as they would a breaker panel. I’m not sure you understand what a control box is. No one here reacting to that comment is under the impression you’re not sure if it’s a control box. You’re being downvoted because you’re still questioning the other part. You’re doubling down because you made this post and don’t want to feel silly
[kewhxef] (score 62, diepte 0) is this the same guy complaining about his crackhead coworker ? just give it up man and move on
[kewjuvp] (score 55, diepte 3) I mean you're posting about this person every couple days at least, he was just confirming that you're in fact 'that guy.'
[kewkqmi] (score 51, diepte 8) You sound like a real fire retardant.
[kewg70c] (score 46, diepte 6) You’ve been at the same place since 1995?
[kewi4nl] (score 42, diepte 1) checked post history, it’s you 

i get you’re upset about this person but either ignore it & stay at your job or *QUIT*
[kevudi5] (score 38, diepte 0) Is this part 74 of the meth chef chronicles ??
[kewijq0] (score 35, diepte 8) Still working salad bar
[kewcdnw] (score 35, diepte 2) Except this clearly isn't a breaker box. Your reasoning doesn't make sense. That box won't be touched unless the electrical gets completely redone
[kewf1zk] (score 34, diepte 6) Hi, electrician here. That’s not really a problem. Might be a bit annoying someday, but not a code or safety violation. Stand down soldier.
[kewe93i] (score 33, diepte 4) I don't care what your maintenance guy says. I know what "qualifications" you need to get that job. And I KNOW exactly what the fire marshal would say. Both my mother and father are electricians and I grew up working for them. You just want to be right.
[kewg1et] (score 32, diepte 0) Lol, spent awhile as a building inspector, control box can definitely be blocked. All good on that front.
[kewjfaf] (score 31, diepte 8) You talk about meth a lot
[kewa7c3] (score 30, diepte 1) For me this post is just giving idiot line cook who thinks he knows everything. Not only is he just very wrong, he’s just dismissive about being wrong. You’re right these people are exhausting and an absolute pain to work with.
[kewqy08] (score 27, diepte 0) Man just move on. From the downvotes you're getting it would appear this saga has run it's course.

Either talk to someone in charge about your coworker, suck it up and deal with it, or change jobs.
[kewhlwy] (score 26, diepte 7) Got 'em
[kewmoxi] (score 24, diepte 5) Well regardless of all that, if this guy bugs you so much and management doesn't seem bothered by it just start putting out feelers elsewhere. It's not hard to cop a job in this industry, as evident by your coworker lol
[kewhybv] (score 22, diepte 6) So let me see if I have this right. Because it changed from the way it used to be, it's now wrong? Your boss might be an idiot, I don't know, but you seem to be projecting how you see him on everything he does. It's common, you see the worst in people you hate, but you're letting it bleed into your interactions with others. Currently, I'd guess you're just as unpleasant to be around as your boss
[kewwecc] (score 21, diepte 4) You’re the definition of insufferable.
[kex0jo1] (score 21, diepte 0) Seems more like this guy is on meth instead of the co worker if I see the comment section jeez.
[kex13g1] (score 20, diepte 6) >Do you have a suggestion to fix it then??

My suggestion would be to worry about the stuff that's real, and worry less about the stuff that people tell you is just in your head.

And that's honest advice. Not jumping a bandwagon here. You said you have PTSD. This stuff irks you a lot. People tell you it's not as big of a deal as you perceive it to be. 

Instead of worrying about it in the first place and to add to that argue against those people in the second place, maybe just take a step back. Chill, do what you are good at and enjoy.

If you honestly think it's a dangerous situation alert management, if they won't listen, the fire department. But I think you and me both know it really isn't the hazard you make it out to be.

And if he's really such a crackhead that fucks up your head all the time, go elsewhere. It's not worth it.
[kewqid5] (score 20, diepte 5) Don't like a comment? Keep on scrolling! You are such a hypocrite, you'll say one thing than contradict yourself IN THE NEXT COMMENT. Truly baffled you can think someone else is an idiot when you can hardly function on a social level
[kexm6ca] (score 19, diepte 1) Looks like a GE Transfer Controll switch. Should be little to no reason to open it. Just a sensor to sense if the ac went out it tells the generator to turn on.
[kews3fw] (score 19, diepte 2) You sure you're not the one on meth?

Never seen someone this angry on Christmas day.

Perhaps take a moment and then change everything about your life.
[kewyigi] (score 18, diepte 9) Plot twist: OP is the tweaker and OP built the shelf just to go on a tweaker rant on Reddit and then tweak out in the comments about himself because tweakers be tweaking.
[kewhrqj] (score 17, diepte 6) They don’t need to be accessible. I haven’t touched the one in my kitchen since we moved in. Breaker box on the other hand I’ve gone almost monthly.
[kewfqh4] (score 17, diepte 6) Why you so mad about being incorrect? Would I do this, no. But as stated, it’s not a breaker and doesn’t need rapid access.
[kewkycu] (score 17, diepte 2) Yeah you are literally the very person you hate. "Never ending excuses... fast answers... zero logic" is you in this post. Like FYI, lots of times control boxes are IN THE WALL. So by your logic, the wall is in the way too, right? Also, the fucking box can come apart, they could still easily access that
[kewq84t] (score 16, diepte 2) Your attitude is shit, he is just trying even tho he sucks. You are much worse
[kewqdg7] (score 15, diepte 4) The right exit doesn't come bud just grow a pair and move the fuck on. Also nobody fucking cares that you're sober anymore. Stop drinking it up like it's some badge of honor or testament to your character
[kewmtdt] (score 15, diepte 8) Different things have different importance and some things can be blocked while others cannot.
[kewkkxf] (score 14, diepte 4) Usually when I see a train wreck like you, it's fun to walk down a bit and see more of it. Let me tell ya bud, your train wreck just doesn't stop. You constantly complain about the most miniscule stuff, or about your job, which, for some reason, you haven't left! You're a cook dude, EVERYWHERE is hiring. If you sincerely have no other options, get a new line of work because you aren't going to last, or you're going to be that guy that everyone hates working eith
[kex65lj] (score 14, diepte 9) Probably still doesn't get offered or invited to post shift drinks...
[kewr9pt] (score 14, diepte 8) Also I love I tried to calmly explain something to you and you just read boss and ranted about that rather than any of the actual substance I said. You should be an excavator with how well you dig holes for yourself
[kex2w04] (score 14, diepte 6) >Insufferable: adj., too extreme to bear; intolerable; having or showing unbearable arrogance or conceit 

This is how the Oxford dictionary defines the word “insufferable”, by the way. It doesn’t mean someone is intoxicated, just annoyingly arrogant or unbearable.
[key0dr2] (score 14, diepte 8) Ok then it’s a mental health disorder and you need professional help. I’m not even trolling. I’m worried about you.
[kexw7tf] (score 14, diepte 0) Can we please ban this shit now?
[kewctt9] (score 13, diepte 1) Well it's not a breaker box. The fire Marshall won't care.
[kewprn6] (score 13, diepte 10) You willingly worked with someone you got trauma from for 14 years? I have a feeling you're not much holier than him based on context. Yes you're sober good for you, but I imagine the 10 years you weren't he didn't complain about your alcoholism
[kex0zoc] (score 13, diepte 8) You’re all over the place. Now you’re upset people need to put holes in a wall to hang shelves? You’re really reaching every which way just so you don’t have to admit you fucked up and you’re trying to find some way to articulate something reasonable to be upset about, but making less sense each time. Ranting about meth over and over, holes..it’s getting wild
[kexnf9v] (score 13, diepte 5) Here's the thing. You said a "control box is a breaker box"

Is it in the same family? Yes. No one's arguing that.

As someone who is a scientist who studies electrical systems, I am telling you, specifically, in science, no one calls control boxes breaker boxes. If you want to be "specific" like you said, then you shouldn't either. They're not the same thing.

If you're saying "electrical control systems" you're referring to the taxonomic grouping of electric systems which includes things from themostats to telephone switches to breaker boxes.

So your reasoning for calling a control box a breaker box is because random people "call the grey boxes breaker boxes?" Let's get thermostats and water meters in there, then, too.

Also, calling someone a human or an ape? It's not one or the other, that's not how taxonomy works. They're both. A control is a control and a member of the electrical box family. But that's not what you said. You said a breaker box is a control which is not true unless you're okay with calling all electrical systems breaker boxes, which means you'd call thermostats, phone switches, and water meters breaker boxes too. Which you said you don't.

It's okay to just admit you're wrong, you know?
[kewl3a0] (score 13, diepte 5) if you don’t like it, you can also change jobs
[kew01cx] (score 12, diepte 2) Collecting data from your past posts proves you're the problem.
[kexkfou] (score 12, diepte 2) Cool but what about the snacks?
[kewqrpr] (score 11, diepte 6) How does looking at words you posted publicly make someone creepy? If I read one of Jane Austin's books then, am I a creep? Was my entire history class creeps?
[kexvqbq] (score 11, diepte 4) Guaranteed that you’re the one on meth. Maybe he is but you definitely are too. 

If you aren’t on meth you need to find a mental health professional tonight.
[kexzyl2] (score 10, diepte 6) We’re all hiding something. That’s the human condition. What YOU are hiding is your drug use or brain damage from previous drug use. One of the two.
[kewt232] (score 10, diepte 4) Again, instead of confronting him why he is doing something wrong, offer to teach him ahead of time. This is about your approach and not about his reaction to being singled out.

Edit:

Explaining why you do things is essential; each job I've had in my 22 years in this industry has employed at least one obscure procedure that would be scoffed at anywhere else. Sure, it is quicker to cook two single pieces of bacon vs. Six pounds at a time, but not for a large production or prep work. Maybe they were scrutinized for spoilage at their last position (we've all encountered that), or perhaps they simply don't know how to cook that amount of bacon at once.
[kewumcr] (score 9, diepte 6) No, but again, it’s the way you’re explaining and blaming. 

“Everything is wrong with him. Why doesn’t he get it. Useless.”

Your attitude towards others speaks volumes. Let go of the anger and resentment you have. You can take my advice or not, but being kind and showing a helpful hand is always more productive than putting others down; once you learn that, your growth will begin.
[kewpxm9] (score 9, diepte 8) All you can say is he does meth but you're sober, just shut up dude. Also get your story straight, are you waiting for him to filter out or has it been 14 years?
[kewwccx] (score 9, diepte 6) Lol what’s wrong with you? You’re talking about logic, but yours is literally “if something used to never be somewhere, and then something is, that means it’s not allowed to be there”

Buddy..how do you not understand how little sense you make. You realize you could have just googled this, right? But even if you didn’t know “there wasn’t a shelf there and now there is” is some of the most batshit insane reasoning I’ve ever heard. Meanwhile, you’re trying to criticize other people’s, which also doesn’t make sense, because the logic you’re speaking of is simply stating an objective fact, that this box can be blocked and is not the same as a breaker box. 

admitting you made a mistake is much easier than doubling down on it
[kew7nrn] (score 9, diepte 0) As a Reefer i’m not touching it unless it gets cleared out. As most others would
[kexo67y] (score 9, diepte 5) Plus everyone knows they’d just make up whatever the fake “maintenance” person would say to feel right.
[kexzny0] (score 9, diepte 6) I don’t believe you at all but ok dude
[kewv11x] (score 9, diepte 0) Some folks just be complaining just cuz they can, just move on a find a new gig.
[kewv54l] (score 9, diepte 0) Wth kind of "kitchen" are you in with this snackbar?  Are these for the employees?

M&m's, Reeses, chips, Keeblers, fresh-washed apples and oranges...

And even if that rack isn't on wheels, it's still movable.
[kewp1ix] (score 8, diepte 6) Yeah ot wasn't about sobriety, I very clearly said your attitude is shit and if all these things upset you this much, you're going to be a bad employee or break. Also stop being so critical of vices. You can not like that he does drugs but quit the bitching
[kewk2ox] (score 8, diepte 2) The alleged junkie is weird, no doubt
Some of his choices and actions are wild
But pls chill bro
If you have skills - you're in demand RN
So float on and find somewhere else
[kexvukw] (score 8, diepte 4) Every comment I see you post is you swearing up and down that you’re clean and sober but my eyes are telling me otherwise.
[kex85xm] (score 8, diepte 7) Right this guy's shit doesn't stink, he knows everything about kitchens and food, I guarantee everyone he works with trys to show him how to do things and he just goes I know more than you and does it differently than everyone else.
[kex1wgk] (score 8, diepte 6) Lmfao you’re the only person that’s saying it can’t be blocked off. Literally the only one pushing that idea. Not a single person has agreed with you.
[kewpls4] (score 8, diepte 0) Wow fall back kiddo…
[key7ik1] (score 7, diepte 8) I’m confused how this could be a copy pasta, but regardless, it wasn’t meant as a response to me it would seem. Where did you get the idea it is a copy pasta?
[kewjla3] (score 7, diepte 7) Once was apprentice
Def a control box for the Walk-In or whatever else has a GE PLC or something
[kewjsu2] (score 6, diepte 4) That's a thing ppl do on Reddit
Are you new here bro?
[key1lcm] (score 6, diepte 6) I’m just trying to let you know because maybe you want to actually send this comment to the right person; you replied to me with this comment when it seems pretty clearly to be meant for someone else as it doesn’t make sense or relate to anything I typed. Just sending this again because the first time I let you know it looks like you downvoted it for some reason so I believe there is some confusion here
[keyaafb] (score 6, diepte 10) Oh word. It still seems to be meant for another person but thanks. Downvoting every comment is a pretty strange move btw
[kex6l43] (score 6, diepte 6) Let us know when you reach China. Because that’s the reason I see that you keep digging.
[kex21m0] (score 6, diepte 0) Jfc dude quit. Meth head chef ain’t getting any better and apparently you would rather just put up with it.
[kez6our] (score 6, diepte 0) Every now and then an OP chooses not to delete their L and I appreciate that for the content.
[kewuwhx] (score 5, diepte 7) The creepiest. How dare you read something readily available for everyone.
[kewn91j] (score 5, diepte 2) Maybe instead of asking him why he does something in a negative connotation, offer to show him the correct way to perform the task. Not only will he learn, but your life will improve by contributing to a work environment focused on being a team and developing one another.

Edit: removed a word.
[kezew5f] (score 5, diepte 8) >I'll go block all the motherfucking things all over the place then. Fuck. We will see how they like that.

Hey no offense but with every passing update to this saga, I'm more and more convinced you're actually the methhead in the building.
[kex0iv4] (score 4, diepte 6) So move on. Teaching environments aren’t for you. Find a place where you can put your head down and ignore the rest of the world since your head is too far up your ass to see your own faults.

Being four years sober is a huge accomplishment, but means JACK SHIT if you’re choosing to live your life this miserably while projecting past faults onto others. Thirty-three years in this industry means even less when unwilling to grow with any team or contribute to overall growth. 

I feel sorry for everyone in your life if this is your ongoing approach to any sense of ineptitude.
[kezh9iy] (score 4, diepte 10) >not a drop to drink

I said meth.

>Why do you even get on reddit then??

"Why even use reddit if you aren't going to praise me specifically?" Okay, methy.
[kex29bz] (score 4, diepte 3) Plot twist.   He’s a schizo and is really both people in the story!  We got a real Fight Club situation here.
(54 reacties met lagere score weggelaten)

=== THREAD bzozza ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2019-06-12  SCORE: 1261  REACTIES: 140
TITEL: Mine are the peppers. My sous is the flames. The two of us cover prep and service for 7 nights a week. Hot feet bois
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[eqv4iqw] (score 181, diepte 0) Just my opinion, but hate them. I'm a boot  guy! Ankle support!
[eqvadc7] (score 62, diepte 0) Laughs in Guy Fieri
[eqv2q07] (score 60, diepte 0) Crocs? I just bought a pair of Birkis, super comfy, although I see so many people wearing these.
[eqvndtl] (score 55, diepte 1) you mean for the cross over dribble?  If you are doing anything besides standing and spinning, you are in the shit.
[eqvxca3] (score 42, diepte 2) I'm always in the shit! Unlike most HC's I'm hands on and outwork my guys. For that reason I get respect and loyalty. I have a solid staff of 8 plus years.
[eqw1y6m] (score 40, diepte 4) It's a local pub. Roughly 240 seats with the new outdoor patio and additional bar seating. My kitchen stayed the same size while adding 100 plus seats. We get shit done while keeping up standards and quality. My guys rock. And I make sure they know it. We hit 2 m last year.
[eqvg5ni] (score 36, diepte 1) Let's just say if I had to work 7 days a week I'm gonna stop looking before I cross the street...
[eqvisqx] (score 34, diepte 0) Do y’all hold hands and sing kumbaya too? Put your shoes on and get back to work!!

Edit- This is a joke. Just for fun. Not serious. I was imitating a super duper serious manager. Once again just a joke. Love y’all stinky mother fuckers, keep your knives sharp and your hands clean.
[eqvms67] (score 28, diepte 0) I wear a pair of orange Mario batalli edition bistros. My third pair, I fucking love the bistros, I miss the version with the open vent on the toe, I can't find those anymore. These crocs are like cleats, just unparalleled grip, plus if they dirty and you feeling cheeky, whip them into the dishwasher at the end of the night, and they are good to go. 

Anytime somebody questions me and my choice of footwear, I remind them that two professions get these gems: cooks and doctors.
[eqvcewl] (score 26, diepte 1) Birki gang!!
[eqvkz6h] (score 26, diepte 0) Best things to wear in the kitchen.

Dropped something hot? Slip em off quick, no messing with laces.

Dirty crocs? Spray them on pot wash or even better stick them through at the end of the night. 

Non slip, so fricking comfortable, sure they look terrible but who cares in BOH anyway?
[eqw0r6g] (score 23, diepte 3) I now respect you as a person.
[eqveo56] (score 21, diepte 4) Yup, first weeks hell, then one night you are done cleaning and writting your prep list for the morning and you suddenly realize, your feet, they.... dont hurt, much, lol.
[eqw6blt] (score 21, diepte 5) Yeah and the hardest workers are probably making .02% of that between em
[eqw73xs] (score 21, diepte 6) Yeah and I stay hourly as well and at less than 3% . Seriously though most average 16 to 18 an hour. Except the part timers and preppers.
[eqw7m1d] (score 20, diepte 8) That's bullshit bro. Start shopping around! Even my prep people make over 10.
[eqvev6q] (score 20, diepte 0) You work 7 days a week? Why?
[eqvn19w] (score 20, diepte 2) I stopped looking both ways a long time ago. It saves so much time!
[eqvl1xc] (score 19, diepte 1) 💲💲💲💲💲💲💲💲💲💲💲💲💲
[eqvee0g] (score 18, diepte 3) For real though after about a week of breaking in it feels like I’m walking on air with those bad boys. And when they get all gunked up the insoles come out and they can go right through the dishwasher. Great investment.
[eqwt4jb] (score 17, diepte 1) These two are on a journey to Flavor Town
[eqw7bca] (score 15, diepte 7) That is a decent wage, I was hired as a dishwasher, immediately got put on salad and now know every station both lunch and dinner and still only make 9.50
[eqw8074] (score 13, diepte 8) My owner used to have multiple pizza shops and wanted to pay that way. He finally figured out to get quality people you need to pay a decent wage.
[eqvv3oz] (score 11, diepte 4) Feet don't hurt, legs don't hurt, back don't hurt after 12 hours on my feet. Best $100 I ever spent. Go to any hospital and look at the feet of the veteran nurses. All wearing Birkis.
[eqve4vp] (score 10, diepte 2) UNITE
[eqvfb6i] (score 10, diepte 1) Danskos > Birks > Crocs
[eqvevlx] (score 10, diepte 0) Thanks I hate them
[eqvrf4y] (score 10, diepte 1) I'm not in the kitchen life anymore, but anyone makes fun of your crocs you can get the last laugh when their feet are all fucked up or they wipe out holding a hot pan because they were too tough to take care of themselves.  I worked in a union mechanics shop for a while and people might joke about PPE but they sure as hell wear it.  No one thinks you're tough when you get a workplace injury, they just think you're stupid and a danger to others.
[eqw8mkb] (score 10, diepte 1) I think the grip is their poorest aspect. 

Source: I stood on a French fry, it mashed into the sole and I nearly broke my neck.
[eqvgjio] (score 9, diepte 3) Yeah i've got high arches too. One of the reasons I went with Danskos. I'd say 90% of my kitchen wear them.
[eqvgv2d] (score 8, diepte 1) I think OP meant between them they both cover seven days a week.
[eqveur7] (score 7, diepte 5) Soooo true, my feet and back were killing me the first few days but it’s well worth the pain
[eqvygnc] (score 7, diepte 2) Danskos destroyed my hip and gave me corns. Not made for those with wide feet...
[eqvkss8] (score 7, diepte 1) If one more person says cute crocs to my birks I'm gonna write birks in white across the front
[eqvldyq] (score 7, diepte 2) Silver sharpie lol
[eqxo2k5] (score 7, diepte 1) Guy and Fieri's Excellent Adventure
[eqvldub] (score 7, diepte 0) I currently am wearing the ones with pots and pans etc
[eqwavxp] (score 7, diepte 2) Alright, after some fond memories of stepping on diced tomatoes other squishables, you have a point. When the treads (which can be a bitch to clean without high pressure water) are clean, the grip is great. When overstuffed,there is a good decrease in traction.
I do think that that is common amongst non slips,  because having stuffin the treads causes slips and falls, but croc bistro's have a pretty narrow and shallow tread to start with.
[eqwxxfs] (score 7, diepte 0) Gotta love the kitchen industry.....cover prep and service seven nights a week. What other industry would that be acceptable?!? And for what we get payed? Yet we don’t even blink an eye.
[eqw6nk7] (score 6, diepte 2) I personally love my blundstones because they are super comfortable for me, just happens that they are in style, so that’s a plus. But if you think there’s a cheaper alternative please let me know! They do kinda break the bank :(
[eqwlh0c] (score 6, diepte 2) Not sure what Crocs you're wearing but they definitely don't retain sweat
[eqw08o3] (score 6, diepte 0) Guy Fieris formal attire
[eqx3mgt] (score 6, diepte 1) Which is the fucking issue! So many of brag about this shit when we should be trying to change it. This industry is fucked.
[eqvqyqw] (score 5, diepte 1) Blundstones are form over function though.
[eqvfzln] (score 4, diepte 2) I've heard good things about Danskos too, I went with Birks because of the arch support.
[eqvlfub] (score 4, diepte 2) Knowing Birkis it would wipe right off
[eqwmtuw] (score 4, diepte 3) Crafstmans work boots. Steel toed. $50
[eqwnhlv] (score 4, diepte 2) I like to live on the edge and see if ppl are still able to detect a little tongue in cheek roasting of our fellow comrades. In my kitchen, if ppl aren’t roasting you and being condescending then they’re probably mad at you for real.
[eqwi441] (score 4, diepte 1) >keep your knives sharp and your hands clean. 

I’ve gotta start using this
[eqwiezj] (score 4, diepte 1) I can't stand them myself. Get way too hot and retain every drop of sweat over a 12-16 hour shift, nothing's more uncomfortable than soaking wet feet for 8 hours. 

Give me good leather lace-ups with arch support and a good non-slip sole any day of the week over that crap.
[eqwnigj] (score 4, diepte 1 OP) I’m down a cook and I’m the owner and chef so it’s on me to cover those shifts until I hire someone. Hopefully this week!!
[eqvgnzh] (score 3, diepte 4) Ahh interesting, I might pick up a pair
[eqvyh3i] (score 3, diepte 3) Danskos are the shit. Comfortable and they actually last me a year working behind a bar (used to boh, still lurk here).

Birks only last me about 8 months usually and anything cheaper I can destroy in about 2 months.
[eqwpret] (score 3, diepte 3) I've got danskos. They are 8/10 for me. Pros: durable. Cons: nonslip is weak, a touch narrow, and goofy looking. I wanna try birkis next. Still a good shoe tho
[eqwxxx6] (score 3, diepte 3) danskos gave me stress fractures in both feet.
[eqw6zd2] (score 3, diepte 1) I love my birkis, I left the industry 2 years ago and I still wear them around the house, for minor yard work and I bring them camping to wear inside cabins.
[eqwk9cm] (score 3, diepte 1) I just got a new chef and we bonded immediately because we had the same birkis on.

Birki nation out here.
[eqwq06y] (score 3, diepte 8) PA
[eqy5le7] (score 3, diepte 2) 5 years military. Just more comfortable for me. Never had an issue. 26 years of kitchen time. Just my preference I guess.
[eqx4wwe] (score 3, diepte 4) Don’t you have some veggies to cut or something?
[eqwk1f5] (score 3, diepte 1) I just bought some and I'm excited for them to come! I always used to wear crocs, switched to boots for awhile and I'm excited to be coming back to crocs. My boots were Doc Martens so literally anything else will probably feel miles better lol
[eqvyc29] (score 3, diepte 0) I have a pair with the tomato splattered graphic! I love these so much
[eqwj0r0] (score 3, diepte 0) Sorry can’t wear this here , go home and change
[eqv07hm] (score 2, diepte 0) These are the best shoes. I have had mine for 7 years. Once tried different shoes, and got my back and feet hurting. These are just the best.
[eqxtyej] (score 2, diepte 5) Can confirm, crusty old nurse lurks here for the Craic, wears Birkis to work
[eqvyof0] (score 2, diepte 4) Had some Rockports our school gave us, garbage shoe, didint even last a summer.
[eqy1vm4] (score 2, diepte 3) I have narrow feet and Danskos fucked up my toes.  I gave up after 6 months.
[eqy20k3] (score 2, diepte 3) Wow, I have a pair of casual Merrells, I didn't realize they made kitchen shoes as well.
[eqyb0et] (score 2, diepte 4) [It's these that I wear](https://www.merrell.com/US/en/jungle-moc-ac-pro-work-shoe/31898W.html?dwvar_31898W_color=J45360#cgid=merrell-pro&start=1). They're extremely comfy, I just wish they lasted longer.
[eqwq986] (score 2, diepte 8) Just outside of Pittsburgh
[eqwz84u] (score 2, diepte 10) Moon township
[er2xicn] (score 2, diepte 16) We're doing well. Others are chains or dives. Although a new place opened down the road from us. Farm to table with all local libations.
[eqx686l] (score 2, diepte 1) Ugh... hot fucking feet
[eqvz66p] (score 2, diepte 1) You need to add the sarcasm tag otherwise your humour gets lost sometimes! 

It's not really hard /s
[eqwnt2j] (score 2, diepte 3) Clearly not as you had to edit it to explain your self.
[eqzh8od] (score 2, diepte 1) Fucking first time I dropped boiling liquid on regular shoes, I immediately learned why slip ons were better. Fuck that noise.

They just retained the water and what I tried to just walk off became a huge welt. And then I finished my shift because I hate myself apparently.
[eqvsnu2] (score 2, diepte 1) Croc Bistros (have a band in the back) or Croc On-The-Clock (complete back).
[ernpkl8] (score 2, diepte 2) 8 day late thumbs up for you.
[eqw45zu] (score 2, diepte 0) Why are you working seven days a week?
[eqwcg4l] (score 2, diepte 0) Hate the shoes, love the design. Makes the shoes totally worth it. For how much yall on your feet,  do they offer all day comfyness and support? As well as being slip proof? I love shoes and am curious.
(61 reacties met lagere score weggelaten)

=== THREAD vvd7hh ===
SUBREDDIT: r/pharmacy
DATUM: 2022-07-09  SCORE: 84  REACTIES: 133
TITEL: Show off your shoes! Work shoes, that is!
POST (source_id=post):
Everyone who is on their feet all day or needs good shoes with excellent support, what works for you?  What's comfortable?  What do you recommend?

(I'm an older student - this for my upcoming APPEs and beyond)

&#x200B;

ETA - you all have been providing such great suggestions!  Thank you!  Please continue to reply if you wish. This will be helpful for lots of people! :)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ifj6md0] (score 106, diepte 0) Adidas Ultra Boosts
[ifj4h2t] (score 48, diepte 0) Hokas
[ifj5sb5] (score 41, diepte 0) on top of shoes, i highly highly recommend getting  dr scholls or some kind of insert AND compression socks. i work 12 hour shifts and my knees, back, legs don't hurt. i will say i do a lot of core/back strengthening exercises so that may play a part too lol
[ifjcsrn] (score 30, diepte 0) So this is a question where I excel. I've been an ER vet tech for 25+ years. I had foot surgery 2 years ago and the orthopedic doctor said I had some of the worst foot arthritis he had seen. Too many years of 12 hour shifts and an addiction to ridiculous heels in my off hours. 

I have a high arch so ymmv. 

Hoka One Ones had a nice cushion and are very light but didn't really have good arch support. 

Recently, I have alternated between a pair of Brooks Ghost 12 and Ryka Devotion (on sale on Amazon for $45 in certain colors). Both of these have great arch support and are very padded but I have had to get the wide in both shoes as they seem very narrow. 

I loved Danskos and Sanitas and wore them for many years. Alegria is similar but a lighter shoe overall. These are all fantastic but since my surgery I have had to add foam innersoles since they are not very cushiony. Be careful as they have a thick sole and I have seen a few people twist their ankle by slipping with these shoes. 

Sketchers have several lines that are super comfortable but they seem to wear out faster than most of the other brands. Catch them on clearance at the outlet so you can afford to replace them faster. 

Hope this helps.
[ifjbuto] (score 24, diepte 1) Compression socks are the best
[ifj4c9x] (score 16, diepte 0) Adidas ultra boost or brooks ghost
[ifj92in] (score 14, diepte 1) Hokas are the best work shoes I've ever had. Noticed all the nurses were wearing them and that it probably was for a reason... not just a flex or status symbol type thing.
[ifje467] (score 14, diepte 0) Cole haan. Some of their designs look very professional and are super comfortable.
[ifjemmn] (score 13, diepte 0) Crocs when I was working IV room and now switched to vivo barefoots.
[ifjq209] (score 10, diepte 3) There are compression socks made of material that’s slightly thicker than stocking material (compression stockings?), so comparatively much thinner than sports type compression socks. I have ones from Mediven that I used my FSA funds to pay for and they work great in the Vegas heat.
[ifjpqxq] (score 9, diepte 2) What if you live in the hellscape that is Texas? I can’t bring myself to wear them even in the few moments to and from my car.
[ifjenxp] (score 9, diepte 1) Def team compression socks.
[ifjgean] (score 9, diepte 1) really love those pairs for work! my soles felt different if i wear other shoes than those.
[ifjd7iy] (score 9, diepte 0) Danskos, Brook’s Ghosts, Hokas, On Clouds, Adidas Ultra boost. I like to change it up so my feet don’t fatigue as quickly
[ifjrjwf] (score 9, diepte 0) One of my co workers wears fucking dior $1000+ shoes to work. I’m like wtf why. 

He says he didn’t buy them for them to sit there. He says they’re comfortable so 🤷‍♂️
[ifjf1vu] (score 8, diepte 1) What brand of compression socks do you wear in the summer? They make me so hot!
[ifje4cz] (score 8, diepte 0) HOKAS. I can run a marathon in them or stand on my feet for 8 hours.
[ifjk0tx] (score 8, diepte 0) As a pharmacist that has joint damage and gets injections in his ankles. Trust me, hoka bondi’s are the shoes my physical therapist recommended to me, and it made a huge difference in ankle and heel pain, on top of that seeing an orthopedist and getting custom insoles is next. I can’t walk without them
[ifjeg66] (score 7, diepte 0) Nobody's mentioned Birkenstocks yet so I will. I switched from wearing running shoes at work to Birkenstocks about a year and a half ago and they've been great in combo with compression socks...I have very little low back pain and I work mostly 12 hour shifts. The only drawback is most of the clog styles don't have a back strap on them so you could lose a shoe if you work in hospital and have to run to codes or something, but there are a couple clog models with a back strap if that's important to you.
[ifjgbqz] (score 6, diepte 2) aw damn that sucks. i work in retail and the a/c is blasting all day so the heat doesn't bother me at all. i am using [these](https://www.amazon.com/gp/product/B01MZ877G5/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) and [these](https://www.amazon.com/gp/product/B082HZ4TV3/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) (i like the first ones better since they're thicker and more heavy duty feeling)
[ifjlghl] (score 6, diepte 0) [Altra Paradigm 6](https://www.altrarunning.com/shop/mens-shoes-road/mens-paradigm-6-al0a5471?variationId=000)

[Procompression Socks](https://procompression.com)
[ifjllxr] (score 6, diepte 0) Once you go Hoka you never go back 😎
[ifjwluz] (score 6, diepte 0) Birkenstocks……. Straight up all I will wear any more.
[ifj4ll6] (score 5, diepte 0) Black yeezys
[ifj7ksw] (score 5, diepte 2) Just like any ultraboosts. They do just fine and my legs and feet don’t hurt
[ifj50dv] (score 5, diepte 0) Demonias

Kidding, I use Nike’s. The Winflos to be exact
[ifj61t8] (score 5, diepte 0) Crocs!! 

The work line that don’t have the holes, specifically. They’re ugly as sin but sooo comfortable!
[ifj6wcr] (score 5, diepte 0) Crocs, specifically the literide clog. My coworker also has them and says it eases his chronic back/knee pain.
[ifj8wte] (score 5, diepte 1) Just to add to this, I wear like a size 10 women's and have had good luck with alegria keli and klogs naples. Dansko is good if you're walking a lot on flat surfaces, but I find them very hard if standing in one place for long periods of time. (Retail pharmacist weighing in here.)
[ifjsipf] (score 5, diepte 1) I, too, have a high arch. The problem I’ve found is that I don’t do well with inserts because they take up what little precious vertical space I’ve got in the shoe to begin with. What shoes have you found that tend to be deeper? My podiatrist told me most of his patients have flat feet, so he didn’t really have any suggestions for me. Thanks fella!
[ifjg03w] (score 5, diepte 1) Came to mention these! If you get the Bend Low style, they won't fall off because they're sneaker-style. Leather, so they wipe off. Love mine in the ER.
[ifjlvyo] (score 5, diepte 0) Brooks Glycerin 19

Or Ecco, depending on the day
[ifk0c6c] (score 5, diepte 0) Doc Marten boots

Yes I know it's weird but I have high arches and my feet have previously developed hairline fractures. I need stiff soled shoes and docs work for me. 

They can look nice with dress pants or punky with a skirt or dress. 

Added bonus: protection for your foot if something is dropped ie 500 count metformin.
[ifj2ks3] (score 4, diepte 0) For mens shoes. Cole Haan Zerogrand
[ifj3br9] (score 4, diepte 0) On cloud are a life saver. Get two pairs and alternate between them. 
Even Hokas might be good.
[ifk6j7z] (score 4, diepte 3) Why? My feet always hurt and dr suggested them. I started wearing them and haven't had problems since. They have limited colors and styles but are very comfy for lots of walking and standing long hours.
[ifj7amn] (score 4, diepte 0) I'm a female so if you prefer women's shoes then this will be more applicable:

* Alegria
* Doc Martens
* Dansko
* Cole Haan
* Brooks tennis shoes

These tend to be more expensive, but you can buy them on Poshmark, eBay, Mercari for cheap. That's what I do. I've gotten so many pairs of affordable shoes that are barely worn or brand new through those sites.
[ifj8n58] (score 4, diepte 0) Every chance I got to where scrubs on APPEs I wore my J’s. These days I like to rock my off-whites at work from time to time.

Btw I was an older student too!
[ifjavs0] (score 4, diepte 0) Whatever is on clearance at DSW. Feet gonna hurt either way.
[ifjihxx] (score 4, diepte 1) I switched to Xero Prio a couple of years ago for work, can't go back now.  I used to always have foot pain after running around all day at work.  I was always the type to never wear shoes at home or outside around the house.  So I figured trying some "barefoot" shoes might work.  My feet hurt a little for a week getting used to them, but ever since, no more foot pain!!  No more weird calluses on sides of feet/toes.   I have very high arches, so going with no support seemed odd, but it really works.

If somebody is the type that rips their shoes off when they get in the door because their feet hurt, it's worth trying IMO.
[ifjga0c] (score 4, diepte 0) I love my Brooks.
[ifjbq9j] (score 3, diepte 1) I love my on clouds! So sad I might have to retire them soon cause I’m wearing them out.
[ifkhz1h] (score 3, diepte 5) I won from the raffle from adidas… maybe real? Not sure. Maybe I wear the wrong size then?
[ifj67m2] (score 3, diepte 0) Nothing really. I have big ass feet and ive tried clogs, skechers, nike. I thought of getting danskos but they seem out of my price range and I don't want to spend that much and be disappointed
[ifj71so] (score 3, diepte 1 OP) And honestly, that's why I started this post.  I didn't want to spend a lot on shoes til I knew how people felt about them.  This post is really helpful!
[ifjaku2] (score 3, diepte 1) Check out the website Footprints.com. They have clearance Danskos and also Sanitas, which are Danskos for the European market. 

Also carry Merrell and Keene. 

Since they're clearance items they have mostly really large and really small sizes.
[ifjyo46] (score 3, diepte 2) Absolutely agree that Dansko clogs are only good if you’re walking about a lot. Standing in place in them hurts. However, their non-clog style shoes are amazing. Alegria is even better IMO. I also wear a women’s size 10. 

Another heads up for Cole Haan zero grand shoes: if you wear a wide shoe (like me) get a men’s pair. (Same goes for sneakers.) The fit a little wider.
[ifj7cjs] (score 3, diepte 0) Danskos
[ifj8qlm] (score 3, diepte 0) Clarks hiking boots…cannot compare
[ifjg6gg] (score 3, diepte 0) Yeezy 350 v2s
[ifjktod] (score 3, diepte 0) Doc martens work boots if you're clumsy.

Red wings if you want to look presentable.

Timberlands if you want to flex.
[ifjnzja] (score 3, diepte 0) Brooks sneakers (I'm partial to the Launch) and Sockwell compression socks. The socks are thick, but more breathable than the polyester kind.
[ifjo7b8] (score 3, diepte 0) I get insoles.  And pretty much rock anything that I can take the original insoles out.  Mostly Nike dunks/Jordan’s
[ifjtqwf] (score 3, diepte 0) My coworker has EDS and wears brooks or NB when she’s on a budget. Normally she has old lady orthopedics custom fit. I go NB
[ifjvxyx] (score 3, diepte 0) New balance and orthotics
[ifjwqef] (score 3, diepte 0) Solomon trail runner's
[ifkxrqq] (score 3, diepte 0) If dress shoes are required, Allen Edmond with orthotics.
[ifj308z] (score 2, diepte 0) For me personally, I use black Versace high top shoes for work.
[ifj5ukc] (score 2, diepte 1) Yeezy doesn’t work well for long standing
[ifjygbu] (score 2, diepte 3) Maybe the type I am wearing isn’t good for long standing. I am using the 350 v2
[ifk003e] (score 2, diepte 4) I also wear 350 v2. Are yours real or replica made in China?
[ifl9ems] (score 2, diepte 1) Question for any one with leg hair using compression socks. So I know it might be different material but when I wear the long adidas socks for too long idk how to explain it but like it hurts my hair? Like I guess being compressed for so long it’s just not comfortable. Would these have the same issue or is the material bareable? Also have been wanting to shave my legs again anyways but would like to know just in case
[ifj6gt9] (score 2, diepte 0) Altra Torin Luxe. They're soft and wide.

If you haven't already invested in them, compression socks are a game changer!
[ifl0msl] (score 2, diepte 1) Only correct answer, a combo of stylish and comfortable.
[ifj6rfz] (score 2, diepte 0) I use sketchers go walk sneakers, but I replaced the laces with no-tie stretch laces. I would have gone for the lace-less go walks, but they didn't have enough give for my taste.
[ifj99q7] (score 2, diepte 0) Cloves! made for healthcare, don't need to tie them, easy to clean, good support. I wear them for my long retail shifts as an intern and now on my APPEs (when allowed)
[ifjbk1c] (score 2, diepte 0) DC villains
[ifkebhe] (score 2, diepte 1) Came here to say the same, the zero grand line specifically. I feel like they're a step above wearing running shoes in terms of being professional but they're confortable
[ifjg6iw] (score 2, diepte 0) Sketchers slip resistant shoes. I have wide feet so not many shoes fit me already but these come in wide and they slip on and off easily which is a bonus. I've used them for a better part of a year and I typically do not feel fatigued wearing them after 12 hours.
[ifjhmtg] (score 2, diepte 0) UGG house slippers.
[ifjk04u] (score 2, diepte 0) Dansko's Kane clogs. Can't do sneakers. I love the freedom and cushion of Crocs but am finding my feet getting sore. Traditional danskos are too tall, tight, and stiff for me, but the Kane clogs are the perfect blend of cushion and support without being constricting or rolling my ankles.
[ifjoqyt] (score 2, diepte 0) Jambu Wildflower Encore with PowerStep inserts.  Haven’t had a plantar fasciitis flare in years. 


(https://jambu.com/item/wildflower-encore-vegan-flat-for-women/JB18WFE)
[ifjpfqc] (score 2, diepte 0) My new favorite is Spenco - I’ve been wearing their slip on sneakers for just over a year now. Also Vionic, Dansko/Sanita, Birkenstocks, and my Brooks sneakers. 
Within 1 year of getting my license I had plantar fasciitis in both feet, so learn from my mistake and start wearing good shoes now!
[ifjqsl8] (score 2, diepte 0) OnCloud
[ifla3l0] (score 2, diepte 1) Which NB?  I was thinking the 860 or 880
[ifjui8h] (score 2, diepte 0) Sanita clogs :) I absolutely swear by these
[ifjvxf6] (score 2, diepte 0) Dansko
[iflasq3] (score 2, diepte 2) I wear size 16 wide so I buy once of the 3 or 4 models available in that size lol.  I have trail runners right now and they are exceedingly comfortable.
[ifm3fia] (score 2, diepte 1) Are they good for walking around? I’m in a hospital and don’t just stand, but walk around all day
[ifm3qrj] (score 2, diepte 2) I stand and walk all day. But I would recommend getting the ones with a back strap. I pretty much only wear Birkenstocks like exclusively. If I could afford their boots it would be a game changer for me
(53 reacties met lagere score weggelaten)

