# Label-batch batch_0145

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
Schrijf het resultaat naar `batch_0145.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1833mf5, wkhqfn, 1k1hp7k).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1833mf5 ===
SUBREDDIT: r/VetTech
DATUM: 2023-11-24  SCORE: 23  REACTIES: 62
TITEL: does anyone have any shoe recs that are sustainable, not ugly, and will keep my feet happy during 10-12hr shifts?
POST (source_id=post):
ive been wearing crocs non slip bc of the hype of all my coworkers but my feet just.. feel like theyre gonna fall off at the end of my shifts, especially around my ankles, and when i get home i have to hobble around bc i hurt so bad lmao. 

I also have kind of wide feet so adidas/nikes are usually not for me bc they squeeze my toes

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kamg1vg] (score 30, diepte 0) I developed hallux limitus in both of my feet from years of being a veterinary technician. Repetitive kneeling and long hours on my feet used to hurt every night until I had surgery and focused on healthier footwear during recovery. 

I wear Altra (Lone Peak, but you can pick any style) as recommended by my physical therapist. They're expensive; but they are waterproof, anti-slip, and foot-shaped. You will feel a difference if you are used to generic shoes that squish your toes together. I've had mine for 2 years now and never had to replace or repair anything even after working 12+ hour ER shifts.

I have a coworker with hip problems who swears by Kuru, which you could also try. I have no personal experience with them, but they are orthopedic.

Wishing you a pain-free future!
[kamg39q] (score 19, diepte 0) Consider trying compression socks!
[kamyivf] (score 19, diepte 0) Hands down… Hokas! I work 10 hour shifts as a vet nurse. Pain free now :)
[kan2859] (score 15, diepte 0) Cloves!!!  They’re made for nursing, lots of cute colors, waterproof, non-skid.
[kamvjd9] (score 10, diepte 0) I love my Clove shoes, a lot! Compression socks also help.
[kamfuja] (score 8, diepte 0) ASICS is what I recommend after 2 ankle surgeries and fairly wide feet and also have bad arches.
[kammh59] (score 6, diepte 1) See, I have PF and cloves leave me pain-free. It’s so individual.
[kamelkx] (score 5, diepte 0) The last time I bought shoes, I did an Amazon “try before you buy” thing. I selected 3 different pairs of various brands and did kind of a catwalk around the house to determine which ones I would keep. Shoe fashion show! 

Anyway I ended up with Saucony Triumph. They’re very squishy if you’re into that, nice and padded.
[kaneaf2] (score 5, diepte 0) Definitely get good compression socks. 

It's hard to recommend shoes because what works for one person may be absolutely awful for someone else so prepare for some trial and error. 

I had a huge success with barefoot shoes but it's not for everyone and the soles of your feet may be a bit sore from the impact if you're not used to it and have concrete floors at your workplace. They worked for me though and I went from always sore legs and feet to never feeling any discomfort. 
You can get some really cheap when on sale or off brands on Amazon. There is a kind that is literally like a thick sock with a thin sole and they are super comfy. You'd just have to buy a few different ones and see which fit you best, try to walk around your house and see how it feels.

I struggle a bit with the idea of spending a lot of money for work shoes even though I am generally all for investing in high quality items. I always have to remind myself that this is a good investment given that I'm wearing these for 12+ hours at a time and constantly being on the move. Good shoes are a game changer.

Remember, get what works for you and not what others wear or what ads tell you you need.
[kami57v] (score 4, diepte 1) I was coming here to say Altra! I also wear the lone peak and it’s an amazing shoe. The wide toe box is a game changer and they are so comfortable. Highly recommend.
[kamykyp] (score 4, diepte 1 OP) thank you sm omg. i work in ER as a triage/icu tech so shifts can be brutal esp 12+ hour ones🙃
[kamzx0o] (score 4, diepte 1) Came here to say this. I know Hokas are expensive but they are seriously sooo comfortable!
[kankwwo] (score 4, diepte 2) Yes, but I tell people I rather spend high dollar to keep my one pair of feet in good shape to justify it.

That and seriously, I love that my shoes look like a sunset.
[kan2guh] (score 4, diepte 0) I don’t have an answer for you, but I would also recommend asking a nurses subreddit :) they would probably have some good recs too !
[kapta62] (score 3, diepte 1) The Amazon try before you buy is great! I’ve also bought a bunch on Zappos to try—they don’t have the same trial option, but have a good/easy return policy (360 days for returns!) so I’ll buy 3-4 to try and return until I find what I need
[kammq3r] (score 3, diepte 2) I heard people say they love them for PF. I loved the cloves so much other than the searing pain they left me in 😭
[kanu66w] (score 3, diepte 1) i second this !! I have wide feet too and usually wear a 10 in women’s. it’s recommended on the site to half size up if you have wide feet: I got 10.5 and they fit like a dream.
[kan2wgr] (score 3, diepte 0) Cloves are pretty good (mineast a little over 6 months), but oof are they expensive. 

My go to are the croc brand tennis shoes. I wear the men's sizes, since they are made a little bit wider and don't cause any pinching like the women's size does. 
They are close toes, hella comfy, and I can hose them down with bleach since they are rubber. Just bring extra socks to work with you. They do have a bunch of small holes in them for air circulation (my feet were turning into a damp in the clogs and nonslip Crocs) 

And as dumb as it sounds....get a good pair of hiking boots. I love mine. They're water proof/resistant and literally made to be worn for long periods of time and keep your feet comfortable.
[kan41y2] (score 3, diepte 0) Hoka, Brooks, or Altra
[kapulxi] (score 2, diepte 2) I’d never done it before but it worked so great that I’ll likely do it again.
[kan3bnx] (score 2, diepte 1) I second this! I started wearing ASICS gel nimbus shoes 4
years ago after someone in the nursing community had recommended them and I haven’t gone back since.
[kapg03h] (score 2, diepte 1) Oooo love compression socks
[kams49d] (score 2, diepte 0) I have to wear steel toe shoes so I have keens. Very comfortable for 10 hours shifts but it took like 3 weeks to break in
[kan0rwu] (score 2, diepte 0) Hoka Bondi8
[kasdc0a] (score 2, diepte 1) I wear Cloves right now and am desperately searching for an alternative. They are alright, but I have serious foot pain still at the end of the day with them. They are better than wearing a cheap pair of shoes, but they are not the solution for me. I was so disappointed bc I wear a women's 12 and I LOVE that they go into mrns sizes on all their colours. But, alas, not the support I need.
[kash05r] (score 2, diepte 1) I also came to rave about my Cloves. They're slip on, comfortable, waterproof and fun colors! My feet have never felt better after long shifts.
[kan791h] (score 2, diepte 0) Compressions socks and high quality shoes made a huge difference with how my feet fell after my shift. I think that for me the biggest factor of those two was the shoes, but others have mentioned amazing benefits from true compression socks. I believe that the socks need to be 15-20 mmHg to really begin to get the full benefit of the socks.  
A lot of my coworkers wear Hokas, myself included, and love them. One recently bought a pair of On Cloud and said that he probably liked them more than his Hokas. They easily can cost over $160, but are definitely worth it. You may be able to catch the on a Black Friday/Cyber Monday sale and save some money.  
I remember seeing a lot of people talking about Clove a while back. I cannot remember if it was positive or negative though.
[kan7kq7] (score 2, diepte 0) I started wearing Xero Shoes in 2018. That is all I wear now. They are minimalist shoes and have a wide toe box. If I wear any other kind of shoes my back, knees, and hips end up hurting.
[kanc9ma] (score 2, diepte 1) On a side note, for me personally, danskos worsened my back injury (SI joint inflammation causing sciatic pain). I couldn’t tell you why though.
[kanc2it] (score 2, diepte 0) On’s. They were SO good for my back. I have a back injury and the DAY I switched to ons my sciatic pain decreased like 80-90%.
[kase9rh] (score 2, diepte 1) I made the switch to on running and now 50% of the staff wear them! They’re  Comfy from day one and didn’t really need any breaking in. Also so light on your feet!
[kankmgo] (score 2, diepte 0) I wear Hoka and Sketchers. I have plantar fasciitis and have not had issues since switching to these brands. 

I also have wide feet and wear a 8.5, but often have to size to 9 because of my wider feet. In my Hoka I get to wear 8.5. My toes aren't rambling around with the extra room sizing up forces me to deal with.

My feet are comfortable, happy, and I'm not miserable at the end of the day.

I have worked ER and IM and they (both brands) have stood the test of both services. I wore my sketchers while being a Lab assistant at a University museum (walking campus, standing, moving from one counter to the next on repeat). I recommend either.
[kaosgog] (score 2, diepte 0) My on clouds are amazing. I was wearing crocs until I developed tendinitis in the arch of one of my feet and switching to the on clouds was great. I have a flat arch, so I hate sneakers. The arch support isn’t intense so it doesn’t cause me pain and they felt comfortable right out of the box.
[kator36] (score 2, diepte 0) I really enjoy Clove , they are made for nurses and are easy to maintain , especially for our field . Check them out , they're my new favorite !
[kambwwd] (score 1, diepte 0) Welcome to /r/VetTech! This is a place for veterinary technicians/veterinary nurses and other veterinary support staff to gather, chat, and grow! We welcome pet owners as well, **however we do ask pet owners to refrain from asking for medical advice**; if you have any concerns regarding your pet, please contact the closest veterinarian near you.

Please thoroughly read and follow the rules before posting and commenting. If you believe that a user is engaging in any rule-breaking behavior, please submit a report so that the moderators can review and remove the posts/comments if needed. Also, please check out the sidebar for CE and answers to commonly asked questions. Thank you for reading!

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/VetTech) if you have any questions or concerns.*
[kandmoo] (score 1, diepte 1) Hokas and Brookes!
[kamjmnv] (score 1, diepte 1) Have you tried Birkenstocks? They also have non-sandal shoe types that I find very comfy.
[kamk7ks] (score 1, diepte 0) I wore cloves for a year and had AWFUL plantar fasciitis. (So… don’t buy those…) But I was able to fix it with a pair of oofos and after that I used asics with custom orthotics, oofos, and crocs interchangeably.

So the recommendation from me here is oofos until you feel better ❤️
[kanrjmo] (score 1, diepte 2) Same here. Cloves and wearing Hoka recovery sandals around the house, made my pain go away relatively quickly.
[kamlgzz] (score 1, diepte 0) I have spread out feet and I started with Altras, then Converse (I do really well with thin soles so Converse are PERFECT!) and recently added my Doc Martins into the rotation. Docs needed a solid beating with a hammer on the heel and a session with my boot stretcher but I 200% get the hype behind them now. They are COMFORTABLE.
[kamu0tk] (score 1, diepte 0) I have clogs and wear compression socks. Those were both game changers for me!!!
[kan1l7w] (score 1, diepte 0) Everyone thinks I’m crazy but I’ve been wearing boots and now specifically Dr Martins in kennels/being a VA over 5 years now and it’s the only thing that works. My feet and legs never hurt at all.
[kan9p31] (score 1, diepte 0) Dansko’s. They are the least ugly of the comfortable / supportive shoes out there.
[kanixv1] (score 1, diepte 0) I personally wear Vans sk8-hi MTE shoes. They have an upgraded insole compared to regular vans and the outer layer is water proof. If I get peed or puked on I can just rinse it off.  I find they have good grip on the floor and I like the ankle support of the high tops. The MTEs are a bit chunkier making them slightly heavier. I have a pair of Cloves that I wear on occasion but do not love. The sole is super cushy but they just feel awkward for me and unstable. I think the heal drop is too high for me to feel the ground well enough.  I also feel the Cloves are a bit narrow for me and I don’t have wide feet.
[kanmyy6] (score 1, diepte 0) Skechers Slip-ins Work: Summits SR - Enslee

I work in restaurants on and off between vet jobs. My last serving job required black non slip shoes… I was there for 2 weeks before I quit so I just kept wearing the shoes to my new shelter gig. These shoes have been a godsend on my feet for vetmed. They’re light, breathable, slip resistant, and cute!!

I used to get back pain so bad from wearing danskos, saucony, Nike, etc. To the point where I left a vet shift early to go to a minute clinic for muscle relaxers. My back is so thankful I switched to the sketchers. 

Also: don’t knock compression socks! Idk what voodoo magic they are but the right shoes with the right socks is *chefs kiss*
[kanosho] (score 1, diepte 0) Not a vet assistant anymore, but still on my feet 8+ hours. I like new balance. Always super comfortable
[kanrba6] (score 1, diepte 0) Hoka! All of our clients who have them ask if I love them.
[kantnmm] (score 1, diepte 0) Hokas in wide with compression socks
[kanv4qh] (score 1, diepte 0) Brooks
[kanvc0s] (score 1, diepte 0) Hokas!!! They have a lot of shoes that come in wider sizes and tend to run wide by default in my experience. They are expensive but well worth it in my opinion.

I used to be a dancer for over a decade and I definitely fucked up my feet/knees/hips as a result, if I didn’t wear Hokas (and/or Brooks) with compression socks to work every day I would truly go insane tbh.
[kao22dv] (score 1, diepte 0) I like Alegria clogs because they come in a wide version, but they are pretty expensive and don't hold up super well. If you have the budget, go for it, but I can understand why those could be deal-breakers.
[kao5bqo] (score 1, diepte 0) I have always gotten sketchers but I have found they seem to be phasing out the insoles that agreed with my feet in favor of a squishier one that's more comfortable short term but wears out quickly. I was able to find one model that works for me last year but I am not sure if I will be able to find again and may change brands.
[kao6csl] (score 1, diepte 0) Brooks! I LOVE mine but they’re expensive
[kaoudrk] (score 1, diepte 0) Hokas! And they just released a waterproof goretex version of their Clifton 9s!
[kapfyn3] (score 1, diepte 0) Home Bondi 8 are the only shoes that have worked for me! I was struggling with plantar facitis and back pain until I bought these!
[kapg8l9] (score 1, diepte 0) hokas work amazingly for me but i feel as if the cushioned heel can be a bit toooo plushy for some people. would recommend if you need more cushion. i’ve also heard great things about “on running”. both are expensive 

i would also highly recommend a nice pair of new balance running shoes (dsw!!!). they’re cute, comfy, and last long
[kapl5ox] (score 1, diepte 0) you've got a lot of great recommendations here!! i wear gales, never failed me at my gp/er combo.
[kapzozj] (score 1, diepte 0) I have very "special needs" feet. My feet are quite wide, and I need prescription orthotics for my right foot. Also, I have issues with my ankles--they roll and twist very easily. I buy a brand called Drew. They come in a width that fits my feet. They have 3 layer removable insoles. I take the insoles out of the right one so my orthotics fit, and I leave them in the left one, which provides plenty of arch support. And the heel cup that goes around the back of the heel/ankle is made of metal, which helps stabilize the shoe to help prevent ankle rolling.

They are not cheap (I think my last pair was $185), but I've never actually worn out a pair, and I think they're totally worth it.
[kaq4g74] (score 1, diepte 0) Patent dansko clogs. They can be wiped off with disinfectant and support your body
[kaqfa9v] (score 1, diepte 0) I dont work in vet tech but i use sketchers work force, non slip, waterproof, machine washable.  Amazing, they have memory foam too.  And not too expensive.  10/10 would always recommend to anyone looking for work shoes. https://www.skechers.com/technologies/collections/work-safety/
[kaqymzl] (score 1, diepte 0) I wear Skechers with removable insoles so I can put in my orthotics
[kar9jo8] (score 1, diepte 0) I swear by Tevas hiking slippers
[karkl8e] (score 1, diepte 0) Sketchers do me pretty good for long shifts
[kavr1vm] (score 1, diepte 0) brooks ghost. brooks are known for having wider toe boxes and come in wide fit also. i have wide feet and a bunion so wide toe box is a necessity for me. the ghosts are made for running for they have cushion. 

would not recommend hokas.
[kawtayz] (score 1, diepte 0) I’ve been wearing Hylos. They’re not all super cushy and huggy, which threw me a bit at first, but they’re suuuuuper sustainable and very comfortable. I can wear them for 12 hours or run in them and not have pain. I have duck feet (narrow heels, wide toes), and the toe box feels great.

Also, do some training to keep your feet and ankles strong. It helps a ton.
[kay17u9] (score 1, diepte 0) I have cloves and I love them. I bought them a year ago and have been wearing the same pair with compression socks every day I work. I have not come home with foot pain since.
[kbbf2ut] (score 1, diepte 0) Hands down easiest answer.... I have worn Vessi for a few years and i love them! Currently I have 4 pairs of cityscapes that I rotate through depending on the color I want to wear that day

=== THREAD wkhqfn ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2022-08-09  SCORE: 153  REACTIES: 62
TITEL: My whole career I wanted an office with a window instead of some dingy, corner of the kitchen shit-hole full of broken equipment, hoarded mandalines, truffle oil and saffron I can't trust the cooks to have free reign too. FINALLY GOT IT MF's!...Aaaand homeless man balls and filthy feet. Womp womp
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ijnbgff] (score 87, diepte 0) All I hear is complaints. Back to the shitty windowless closet you go
[ijnd1c5] (score 16, diepte 0) Now you know not to have or set your lunch on that bench. Congrats on the window and other benefits tho!
[ijnbkrd] (score 12, diepte 1 OP) You right...


But!  if you look closely he's giving birth to next weeks #10 can of fruit cocktail for the Rotary club's weekly banquet. 

[so, pluses and minuses](https://youtu.be/aPVLyB0Yc6I). You know how she go.
[ijne3cx] (score 12, diepte 2) Guess u can freely tan your feet and sack there too!
[ijndkp0] (score 10, diepte 1 OP) Bruh. That's my bench too. There's an amazing view of the park where all the heroin addicts shoot up and sleep >!nod off!< under the Cottonwood's. Its ethereal, I have my red bull and three Marlboro reds there every day at 4pm. sometimes a martini also >!^((warm popov)^)!<

The fuck am I gonna do now?
[ijnize3] (score 10, diepte 0) I like that your computer has a rear view mirror
[ijnkvwl] (score 10, diepte 1 OP) My co-workers idea and it's a good one. No one sneaks up on us. That guy is wicked smaht.
[ijnehlt] (score 7, diepte 3 OP) See, that's the silver lining I needed. You're a real bro, thanx man. You get the professional solute for that...👨‍🍳🤌💋 

Do they make nice bra's just for mens brain sack? I think it'd be really classy to get some sexy tan lines there. For my special lady friend.
[ijnmgb2] (score 6, diepte 2) It's okay don't be so hard on yourself you're not an asshole. Just remember that the homeless bums have as much right to the city as us that have shoes on our feet. That's what makes a city a beautiful thing, man
[ijnfvfe] (score 4, diepte 0) Just enjoy the view you goddamn ingrate!
[ijnne4w] (score 4, diepte 2) Is that a view of Hahvahd Yahd, kid??
[ijohiv5] (score 4, diepte 3 OP) Fuck, that's just not in our cards. The best we get is a Slavic squat on a filthy line after the rush but the bacon sandwiches are sick. 

Here's the secret, hoard the best looking tomato early in the day (if it's august like today you know there's a sick ass heirloom somewhere close at hand) Hide it on the top shelf of dry storage, not in the open no that fucker becomes its best self up high way in the back next to the stale rice noodles that three chefs ago brought in a full case just for a garnish on his salad special 4 years ago that no one bought. slip aside the best end cuts of the thick cut peppered bacon and only the perfect middle pieces of bread will do brunch brioche is chefs kiss 👨‍🍳🤌💋if you got it, you can hide these in your lowboy if you have one in your station. 

If you're lucky you have enough time to make a quick one yolk Mayo with a fat chunk of confit garlic(my shit is better than Hellmann's) but that back of the fridge kewpie Mayo will do in a pinch. Season the fuck outta those fat steaks you cut outta the tomato(don't skimp, heavy S&P both fucking sides) then comes the pièce de résistance only toast the bread on one side. Use the salamander, golden fucking brown now you're almost there, now's not the time to fuck around. Full attention on that toast, heard? Slather your aioli corner to corner fully penetrate ery fucking nook of the non toasted side aaaallll the way to the edge.  Both pieces. 

Stack it now. Tomatoes (at least two slices), then bacon, green leaf or romaine if you're a fucking psycho that uses the food my food eats and then set it smack dab in the middle of the biggest board in the shop and slice it corner to glorious corner. 

Squat below the line, stand over a trash can or for bonus points sit on the nearest milk crate and chew it slowly, with your eyes closed. If you've got headphones and can listen to dark side of the moon or maybe anything 70's Bowie while you do, and I swear to fucking Christ you can have a few moments of pure unadulterated freedom and maybe even a flick or a camera flash of real joy. No hoods running, no ticket machine chattering, no fucking dickhead chef judging. Just pure perfect feels. 

If it's a hot day this must be done on a box of onions that shit for brains prep cook put in the walk-in. When you stand up and walk out scream "who the fuck put onions in the fucking fridge again‽" 

4 fucking minutes. That's what we get. But if you plan it right, that's all you need. Obsess about the details plan it to the second and then use every single one.

Edit: [the automod doesn't like me](https://imgur.com/gallery/C5Jt04D) is that better?

Hey that was really nice of you u/annajbanana thanx.
[ijpkofp] (score 4, diepte 0) If you like homeless mens feet and balls that’s fine but don’t go taking them into work with you. What you do on your time is your business.
[ijnkojn] (score 3, diepte 5 OP) Thankfully not there...yet. 

No I need some sexy stuff, you know lingerie sorta stuff. A bit of hardly there straps, just some cheeky sorta tan lines when I give the old lady the strip tease. Something that really shows of the sesame seeds a bit. You hear me right? Got anything like that?
[ijo2lbs] (score 3, diepte 3 OP) Socal. Boston sux go yanks.
[ijnqtsn] (score 3, diepte 0) I worked in a large commerical kitchen that had windows all along one wall. It was amazing.
[ijotbuq] (score 3, diepte 3 OP) Heard
[ijovqu5] (score 3, diepte 4) Lol all good chef!
[ijp7cpd] (score 3, diepte 0) Still better than any kitchen view I've ever had (other than the cute servers).
[ijq8of9] (score 3, diepte 1 OP) Heard
[ijnht29] (score 2, diepte 4) Depending on your age, you may want the Nut Bra.  https://www.youtube.com/watch?v=NOiaSy643B4
[ijoszos] (score 2, diepte 2) If it's any consolation I just finished in a kitchen with a full wall of windows. The view was nice, but it got very hot very quickly.
[ijnfzb6] (score 2, diepte 1 OP) Heard. I'm never just happy.I'm an Asshole, fuck!
[ijovaws] (score 2, diepte 3 OP) Heard
[ijo2j2h] (score 2, diepte 1 OP) If only. One day. One fucking day we should all be so lucky. Of course with my ADHD I'd probably never get anything done.
[ijow64w] (score 2, diepte 2) Squirrel
[ijo4j5q] (score 2, diepte 2) I was thinking today how I wish I had a job where I could go to lunch during work for a meeting or something lol.
[ijoem8t] (score 2, diepte 2) That made me loudly chuckle, I had forgotten about that scene, you've got a good memory at least for jokes lol
[ijonchk] (score 2, diepte 0) Can I get some of that saffron??
[ijoue27] (score 2, diepte 2) Muscles? Not really. I lift heavy shit every day from place to place. MUSSELS on the other hand I can do a nice special with.
[ijorded] (score 2, diepte 0) Congrats on your ballfice.
[ijq0fg3] (score 2, diepte 0) Some people will never be happy.
[ijtjskg] (score 2, diepte 2) Well hot damn
[ijoqkzm] (score 1, diepte 2) You kinda fucking suck dude. Hope comes back to bite you.
[ijotets] (score 1, diepte 3 OP) For making a joke? What exactly is so offensive?
[ijp00cs] (score 1, diepte 3 OP) ☝️they get it. 

I love that dog. Best part of the movie, so what if UP made me cry in the first five mins? Two movies have ever done that to me. Up and saving private Ryan. When you know you know.
[ijo2ape] (score 1, diepte 1 OP) Not bad. Love these silver linings you people keep throwing at me.
[ijnxwse] (score 1, diepte 0) Grass is always greener…
[ijo26y8] (score 1, diepte 1 OP) When you're right you're right.
[ijo25kt] (score 1, diepte 1 OP) Smile and wave
[ijo525t] (score 1, diepte 0) That's just Ted you'd better get used to him he's not going anywhere, wait till you meet his fine associates who hangout there at night they sure are a lovely group of people
[ijoeey0] (score 1, diepte 1 OP) That's cool, I'm home long before nightfall. And I [no longer have a Prius.](https://youtu.be/u1j4mK6cs_A)
[ijoi3w6] (score 1, diepte 3 OP) 🤷🏻‍♂️
[ijogf3s] (score 1, diepte 0) Congrats, you’ve witnessed first hand our failed system.
[ijohtnh] (score 1, diepte 1 OP) Just now? Or everyday all day you mean? r/boringdystopia
[ijohu0u] (score 1, diepte 0) Lord knows you’d never see that working BOH. Grass isn’t always greener. Water your own side, fam.
[ijoi2l8] (score 1, diepte 1 OP) No I am BOH. this is my new exec position office. Sick right?
[ijotm6w] (score 1, diepte 1 OP) Oh!! Paella time? Did you get good ~~muscles~~ mussels?
[ijov364] (score 1, diepte 3 OP) I'm a moron. 🤷🏻‍♂️. Good looking out though.
[ijotk2p] (score 1, diepte 1 OP) Uh, well I'm still cooking. I'm the executive of a banquet facility. Is that selling out? Insisting on making a livable wage? I'm not exactly a fucking millionaire here. You're very toxic huh? That's a lot of comments to someone you hate. You ok? Need a hug?
[ijow3ay] (score 1, diepte 0) Be careful what you ask for. Could be nuts
[ijp5c66] (score 1, diepte 0) I worked in a kitchen (open) and it looked out with full glass walls. It was great, homeless people crapping, ambulances rescuing people, police arresting people, someone got hit by a bus, a large pebble shot out a bus tire and annihilated our double pane extra thick glass, and all the cosplays that went to comic con/pax
[ijtj49y] (score 1, diepte 0) Where's the balls and feet? Can't just make claims like that without the goods
[ijtjqgy] (score 1, diepte 1 OP) Pinch that picture bruh
[ijnysy9] (score 0, diepte 0) What do now?
[ijoyjd8] (score 0, diepte 1) Much like your mom, we all gotta pay the bills.
[ijp2lbz] (score 0, diepte 2) Original.
[ijnbjfc] (score -1, diepte 0 OP) Sorry for the shitty cell phone snap shot. Rest assured in person it was [glorious](https://youtu.be/236ov8LpYmI) bare footed tweeker thing of beauty.

=== THREAD 1k1hp7k ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2025-04-17  SCORE: 54  REACTIES: 62
TITEL: how to get rid of plantar fasciitis​
POST (source_id=post):
Hey everyone, dealing with relentless plantar fasciitis pain for the past 6 months now. That sharp heel pain is worst in the morning and after sitting, easing slightly with movement but flaring up again after any activity. It's really impacting my ability to enjoy my morning walks.

I've tried stretching and icing and my doctor suggested night splints, but I'm not seeing much improvement.

Has anyone successfully gotten rid of plantar fasciitis? What really worked for you? Any advice is greatly appreciated – I'm desperate for relief! Thanks!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mnm9vd9] (score 14, diepte 0) You have tendons on your feet that have been damaged. They heal a little bit every night when you aren't using your feet. However, if your feet aren't stretched at night, it heals with your muscle unextended. As soon as you put pressure on it in the morning, it extends those tendons and it rips out the healing that happened the previous night. That's that first painful step in the morning. RIP

The idea with the splint is to extend those tendons so it heals in the extended position. Then, when you put pressure on it in the morning, you are not ripping open everything that healed the previous night by stretching it with the pressure of your body. The healing happened in the extended position.

Good night splints work, but you must do it consistently for 60+ days. If you do it for less, it's going to go back to the way it was and you need to start the clock over. Do it for a few extra weeks if you can just to make sure you don't regress.

If it starts to feel good and you stop, it will regress. You need to do it for the full time.

The way I did it was wearing a stiff boot to bed and I pushed my foot against the foot of the bed to keep it properly angled. The sock/strap thing didn't really keep me in the right position all night.

This is a long-term fix. It takes commitment and it works, but most don't finish it to completion and think it failed.
[mnmiiz1] (score 10, diepte 0) Fairly sure OP is either some garbage tier karma bot or knee-deep in some weird fantasy.

Four months ago they're giving paragraph answers about how to deal with PF from a medical pro perspective.

Now they're spam posting about PF in multiple subs asking questions they clearly know the answers to.

Edit: I'm aware what I've done is strictly against the rules, I just know shit when I smell it. Will accept a ban and move on from the sub if mods decide to enforce the rule.
[mnm5odz] (score 9, diepte 0) Stretch in the morning before you get out of bed, and counter to logic, harder insoles are way better than soft insoles.
[mnm6yoc] (score 6, diepte 0) I had a bad case of plantar fasciitis and was given a foot brace and lacrosse ball to help alleviate the symptoms. I switched from steel toe boots to Birkenstock chef clogs and that also helped a lot
[mnmaaik] (score 5, diepte 1) Plantar fasciitis is from his tendon in his foot getting ripped from too much stress. It heals every night in the wrong position, then when he steps out of bed every morning, the tendon tissue rips again (painfully).

A foot massage is going to make that a lot worse.

Foot massages feel good, but it's the opposite of what you need for this condition.
[mnm6r0u] (score 5, diepte 0) I've reduced it by wearing stiff, supportive insoles and exercising every day (stretching, massaging, icing).
[mnmc707] (score 5, diepte 0) I have chronic plantar fasciitis, had surgery last year to remove a bone spur caused by PF. 


Please OP, go to physical therapy. You need to learn the proper stretches and motions to help your tendons. They might even suggest going to a podiatrist if it's really bad. It's not as simple as stretching your calves, which might do more harm than good depending on your situation. Getting proper orthotics would be great, and proper shoes are good too. But PT is the first and best step (pun intended).
[mnm4ow5] (score 4, diepte 0) Have you ever had a proper foot massage? I got my first one while in Japan after a couple days of walking around all day and starting to experience significant pain there. This tiny little lady had surprising strength and was absolutely pummeling the arches of my feet with knuckles. It was quite painful and I was getting a little anxious about the overall thing, but holy crap it completely cured it and I was fine for the rest of the week of walking all day.
[mnm6f3w] (score 4, diepte 0) What do you eat? People in this industry need to eat like strength trainers, but most starve themselves and have cigarettes for breakfast. I used to have horrible aches and pains, and occasional migraines from TMJ. My body still hurts like after a normal, physical day, but it’s not nearly as bad after physical therapy and getting my diet on track with the help of a food tracking app. Stretching is great, but you need muscles to stretch!
[mnm7bqa] (score 4, diepte 0) You need to adopt nevernude for your feet. If you are standing up or walking, wear shoes. Even at home. 

Mine went away until I got COVID in 2022, which caused ALL of my tendonitis to flare back up. 

Stretch your calves. Eat a lot of fresh cherries, if you can find actual wild cherries even better (I'm serious). I'm waiting on the two wild cherry trees in my yard this year with bated breath. The summer I ate my weight in cherries and wild cherries, my gout and my PF went away until the aforementioned COVID. Gout has stayed away TFG.

Meloxicam/Mobic really helps too if you want to go the pharmaceutical route.
[mnmofxc] (score 3, diepte 3) or just be funny?
[mnmm1i6] (score 3, diepte 1) Holy shit this feels like such obvious advice but I never realized that until I read your first paragraph. Now I feel stupid but at least assured that I can probably help some of my muscle pains
[mnmagfh] (score 3, diepte 0) I used to walk up to 25 miles a night for my job and had that shit for years.  I learned that it isn't just your feet that need stretch and massage but you need to work out all the muscles up to your knee to loosen up the bottoms of your feet.  

  My routine for a while was after my routine at the gym, I would stretch for 30 min, then go into the sauna and massage my feet and lower legs while everything was loosened up, I noticed very sore and tight muscles in odd places in my calfs and ankles and worked those out.  After a few weeks it was gone and I haven't had an issue with it since.
[mnmctkb] (score 3, diepte 0) You’ve just got to keep stretching the plantar fascia until it’s as stretchy as it was before it was injured.  Wear a brace at night, wear shoes with good arch support during the day, or get insoles designed to help with plantar fasciitis (any drug store will have these and they are cheap).  

The important thing is to keep doing it, and know it won’t happen overnight — it took me about two weeks of constantly keeping my foot in something that put pressure on the arch, and now it’s like nothing was ever wrong.  Just keep at it, it takes time.
[mnmkvmk] (score 2, diepte 2) I've been dealing with PF for a long time now

I only started really improving after I got a foot massage machine and used it morning and night every day.

I don't know what the mechanics of the massage are, but it absolutely helps.
[mnmo43u] (score 2, diepte 3) It may make it feel better. I fear if you stop using it you will start feeling the pain again though. The way through PF is to get your tendons to properly heal. I don't understand how massage is going to give you the long-term fix here.
[mnm721r] (score 2, diepte 0) How narrow are your shoes? How does it feel when you don't wear your shoes for a while?
Mine was due to the toe box of my shoes being too narrow, it changed the geometry of my foot to where it was hurting. It took a little while to get better though
[mnm72zh] (score 2, diepte 0) I dealt with it for a couple of years, a night splint is what finally helped me get rid of it. I just got a cheapo one on Amazon, it was bulky but not too uncomfortable. The key is committing to using it nightly. I got one similar to [this](https://a.co/d/9c7dle4)
[mnmah8b] (score 2, diepte 1) > nevernude 

literally dozens of us!
[mnm7sv8] (score 2, diepte 0) Cortisone shot if it’s really bad. Then you need better shoes or orthotics. And wear them! Going barefoot is the worst
[mnma0uo] (score 2, diepte 0) I got a foot massager at Five Below that I use nightly. Also compression socks if it’s really bad. 

You can Google “Toes Pose” and try it. It is a very deep stretch of your foot arch and it might be too intense for some people. But it can be a game changer.
[mnmdzio] (score 2, diepte 1) Exactly. It’s those calf muscles that are moving your feet.
[mnmbffk] (score 2, diepte 0) Get better work shoes. 

Don't be afraid to pay 120+ on em.
[mnmbiwt] (score 2, diepte 0) Stretch those hamstrings relentlessly and find better supporting shoes
[mnmcaeu] (score 2, diepte 0) Everyone’s PF is different because there are a multitude of causes. There are many points along your kinetic chain which can cause stress to your fascia. My doctor also had me do stretches and a night brace but the ONLY thing that helped was something my doctor didn’t even mention. I simply couldn’t be barefoot ever. Once I started wearing Oofos around the clock it went away completely.
[mnmepvg] (score 2, diepte 0) Took me almost a year to get fully healed.  These insoles are the only thing that made walking and standing bearable. 

https://www.amazon.com/Plantar-Fasciitis-Insoles-Orthotics-Comfortable/dp/B0DDX4623W
[mnmerfp] (score 2, diepte 0) Not a chef but had a horrific case of plantar fasciitis for nearly a year. It turned out that I had tightness through the achilles and calves that was causing it. I went to physical therapy for two Graston therapy appointments and it cured it. You can buy the Graston tool and emollient and just watch how to do it from a YouTube video. Now whenever it starts to act up I do Graston on the back of my leg and on my foot and I'm right as rain.
[mnmeu1m] (score 2, diepte 1) Also look for shoes with wide toe boxes. I love Altras for this reason.
[mnmevtb] (score 2, diepte 0) Nightly Epsom salt foot baths. Half cup in a bucket or whatever you got with hot water helped me live again.
[mnmf8aa] (score 2, diepte 0) I manage mine with stretching (which hurts like a bitch) and naproxen which is a non steroidal anti inflamatory. It helps relax the muscles in my calf and takes the pressure off my tendons.
[mnmu2g4] (score 2, diepte 0) Wearing splints on the affected foot every night is the only thing that healed it for me
[mnmwa9e] (score 2, diepte 0) I’ve had it a couple times. The only thing that worked was wearing one of those god forsaken braces/socks at night. It keeps your foot stretched at night and really helps after a week or so.
[mnmd3r7] (score 1, diepte 1) it's a subreddit about kitchen life, find a funnier relevant joke
[mob0j7u] (score 1, diepte 1 OP) Why is that?
[mob0usy] (score 1, diepte 2) Squishy insoles stretch the plantar fascia too much. Harder insoles like cork do not.
[mob0k8f] (score 1, diepte 1 OP) Which brands work best?
[modaymo] (score 1, diepte 2) I'm currently using SuperFeet. I've also used SofSole but the ones I got from Amazon weren't as stiff as the ones I got from my orthopedic clinic.
[mnn3mdv] (score 1, diepte 1) Yes, rolling my feet out every night with a tennis ball, eventually moving down to a golf ball helped me so much!
[mnm7g4j] (score 1, diepte 0) SAS shoes
[mnm9ts5] (score 1, diepte 0) I'm still working through it post surgery. Working out, good shoes and inserts (even just the heel inserts), and most importantly, stretching. 

If I stretch before and after my shift, I'm usually fine. The main stretch for me is, while kneeling, to try to push my knee over my toes as far forward as i can while keeping my foot flat. Then I guess do the other side if you have the issue in both feet. I know you said you've tried stretching but maybe you haven't tried this stretch. 

I haven't seen that stretch suggested online for PF but it really does the trick for me. I look insane doing it in the locker room or outside the restaurant but fuck it I feel so much better after work.
[mnmbksr] (score 1, diepte 0) Oh man, been there done that. Fucking awful. Tried so many things but what ended up working was a brace I got off Amazon. It stretches your foot while you sleep. Really uncomfortable but it worked. Went two years with crippling pain to having it fixed in two weeks. Take a look online and get a stretching brace. 


But honestly your biggest problem is probably being on your feet so many hours on those hard floors. I used to run kitchens 70+ hours a week. Always understaffed and overworked.
[mob0pwd] (score 1, diepte 1 OP) Did the PF cause the bone spur?
[mnmdiwa] (score 1, diepte 0) Quit restaurants. Basically gave my feet a rest. They still take a beating these days but it's not 5-6  16hr days a week in chef shoes anymore.
[mnmezp7] (score 1, diepte 0) see if you can go to a physical therapist
[mnmh300] (score 1, diepte 0) Expensive ass supportive shoes with a wide toe box and compression sleeves for my foot/ankle made a big difference. I only start to have pain when my shoes start to wear out which unfortunately is about every 9 months. Compression socks are helpful for standing so long in general but I hate wearing long socks and haven’t been able to stick with them personally. At home I have fatigue mats in the kitchen where I stand for longer periods and a pair of very plush slippers so I’m rarely barefoot for too long. There’s also some PT exercises you can do to help strengthen the muscles like calf raises and moving marbles or other small objects from one bowl to another, or gathering a towel with your toes. Gentle stretching obviously helps too.
[mnmh6vp] (score 1, diepte 0) So I didn't have plantar fasciitis but dealt with a similar problem a few years ago. I have all kinds of structural problems in my feet and one result of that is super tight achilles tendons. 

For close to a year I was dealing with constant, horrible pain and inflammation in my achilles tendons from my the top of my calf all the way through my heel. Symptoms were extremely similar, the pain was at its peak when trying to re-stretch them after resting my legs.

I went to a podiatrist, bought the $200 imported insoles that she suggested, did all of the exercises she prescribed, tried different shoes, and none of it helped.

Bought [these insoles](https://a.co/d/446VcMn) on a whim and the problem was solved quite literally overnight. I've been wearing these in my kitchen shoes, replacing as needed, for 5 years now.
[mnmigd1] (score 1, diepte 0) The first piece of advice I would give is to go get your foot/show size measured professionally.  I had horrible plantar fasciitis and went to get better shoes.  I went to a real show store and one of the attendants asked if they could measure me.  It turned out I had been wearing shoes 1 1/2 sizes too small my entire adult life.  As soon as I changed the shows, the results were instantaneous.  Coupled with some exercises for a bit and I've never had issues since.
[mnmjd0x] (score 1, diepte 0) Dansko clogs.
[mnmkbyv] (score 1, diepte 0) I found the velcro braces/stretch socks that pull your toes/ball of foot into flexion overnight to help provide some relief in passive stretching of the fascia. I pair that with breaking up scar tissue by painfully rolling the fascia over lax balls. Then maintain a daily stretching routine for your whole posterior chain - glutes, hamstring, calf, and I'd throw in your hip flexor too.
[mnmks76] (score 1, diepte 0) Get the good inserts designed for this. It stopped my pain right away.
[mnmlafr] (score 1, diepte 0) Physiotherapist
[mnmm8hn] (score 1, diepte 0) Good shoes / good fitting shoes . 
(NO flip flops!)high quality custom Insoles . My chiropractor was helpful in deep tissue manipulation
[mnmmhgo] (score 1, diepte 0) 1 hour of yoga a week is my silver bullet to health
[mnmmqm3] (score 1, diepte 0) Do the massages for months. It takes forever. Literally months.


Mine is almost gone. Started really getting serious about doing the proper foot massages and leg stretches at Christmas. 


Thats all you can really do..
[mnmp4b0] (score 1, diepte 0) I would recommend going to an orthopedist. I went to physical therapy first and it helped for a while but eventually the pain became unbearable and I went to see an orthopedist. After X-rays and an MRI they found severe plantar fasciitis, a missing tendon and my ankle bone was “floating”. It took about 4-5 months after surgery to recover but it was worth it. If the pain is bad see a specialist. I know it might seem unreasonably expensive but you may save yourself serious money and time down the road. Take care of yourself.
[mnmp9gx] (score 1, diepte 0) I wear a brace when it gets bad.
[mnmpzt7] (score 1, diepte 0) So you say you are icing but how?


I've found the best way is to take a 16 oz plastic soda bottle, fill it 3/4 with water and freeze it.  When it's fully frozen, roll the arch of your foot back and forth over the bottle.  Do this 3-4 times a day.


Otherwise, make sure your shoes have really good arch support.  Don't rely on insoles.  Make sure the shoe itself is built with good arch support.


You can tell by looking at the outside of the shoe.  The sole should be raised under your arch.  On the inside, run your fingers over the insole on the inside.  You should feel a significant raised portion where your inside arch sits.  Most shoes have no raised arch support or it's so slight it's worthless.
[mnmqbn1] (score 1, diepte 0) Super feet inserts, ofoos slippers at home. That cured mine as well as rolling it out with a roller. 
Couple months later I saw a picture of Tiger woods wearing the same slides dealing with the same thing 😂 haven’t had the issue since but I still swear by the slippers 

https://a.co/d/eKpPYQC
[mnmrzkg] (score 1, diepte 0) It took me sleeping in the boot every night for several weeks.
[mnmt1yd] (score 1, diepte 0) Stretching is very good but for me it was buying good shoes with excellent cushion and support.  I love Hokas. Others like other brands. My PF completely resolved after wearing Hokas at work
[mnmw35o] (score 1, diepte 0) Danskos.
[mnn19d7] (score 1, diepte 0) Birkenstocks. The only thing that helped me. 

They also make insoles that you can slide into shoes. I put them in my kitchen shoes.
[mnn4q41] (score 1, diepte 0) personally, i wore birks for a long time and the lack of cushion w the support made my plantar faciitis worse. now i wear hokas (i know!) with treadlabs inserts and this combo is the only way walking and standing is comfortable. everything else, i accept that it's going to hurt and do massage / ice / rest after. for full-time kitchen work, hokas aren't an option, but maybe something with more cushion?
[mnn8oov] (score 1, diepte 0) Have you tried working in clogs? They have both a wide toe box and a slightly raised heel, both of which are great for plantar fasciitis 

I also wear custom orthotics in my Hoka tennis shoes when I'm not working. 

.
[mnn8ws4] (score 1, diepte 0) r/KitchenConfidential is a place for redditors in food service to meet, gather and share with each other; cooks, service staff, managers, business owners, etc. All posts to the sub must be related to the restaurant or foodservice industry.
(8 reacties met lagere score weggelaten)

