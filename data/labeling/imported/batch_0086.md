# Label-batch batch_0086

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
Schrijf het resultaat naar `batch_0086.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 17q0eea, g0ixnq, 16u2jug).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 17q0eea ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2023-11-07  SCORE: 21  REACTIES: 81
TITEL: My feet stink
POST (source_id=post):
It's been a struggle. I've tried different powders, sprays, and inserts. I've tried different materials for my socks, and I'm sure to wash them daily. However, my feet still stink. I smell them now. It's a horrid combination of doritos and cat piss.
Yes, I know this isn't a sub about feet. I figured yall would have some useful insight

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k88vidz] (score 58, diepte 0) Cat piss smell means ammonia. Usually means you are burning protein for fuel. Up your fat or carb intake is the simple answer but probably a reassessment of what/when you are eating is needed.
[k88xmvr] (score 47, diepte 1 OP) I was not expecting that answer. I have gone more keto heavy in the past couple of years in an attempt to lose weight.
[k89vsos] (score 31, diepte 2) Keto is definitely noticeable in smell
[k88y1rm] (score 24, diepte 0) See your doctor.  If your feet haven't always been extra stinky, it could be something else. A quick Google tells me it could be anything from athletes foot to diabetes.

That said, I buy two pairs of work shoes and switch between them every week. If you sweat a lot and work a lot the shoe sweat never dries and causes a lot of the smell. Shoe deodorizer also helps.
[k895w6k] (score 19, diepte 2) It's both. 

Op- I'd recommend getting some bloodwork done, as this can be a sign of underlying issues other than just dietary. 

The first thing that I would suggest is drinking more water. Dehydration leads to stronger smelling sweat.
The next thing is have anti microbial socks, and change them throughout the day. 

The next thing is buy non scented odor eliminators for your shoes, they made a huge difference in my hockey skates. 

Good luck!
[k890nc4] (score 18, diepte 1 OP) As stupid basic as it sounds, I have never thought about having multiple pairs of work shoes just to give them the opportunity to dry out. I change my shoes a couple times a day for that reason, but it never occurred to me that the shoes I spend 10+ hours a day in need to be swapped. I have more than 20 pairs of shoes and only 1 for work.

Big brain
[k8amfno] (score 14, diepte 4) Ketones are obvious, whether sweat or breath or pit smell.
[k89w5be] (score 12, diepte 3 OP) I've heard about it affecting your breath, but nothing else
[k89faws] (score 10, diepte 0) I just want to commend you for having the courage to post this.
[k891ecp] (score 9, diepte 1 OP) Been doing this for 25 years, and it never occurred to me. My brain is feeling smooth... like butter
[k88tp7v] (score 6, diepte 0) maybe try one of those shoe dryers, chances are it is because of your wet ass shoes.
[k88uq67] (score 5, diepte 2) yea and that soaks into your soles, getting rid of that moisture everyday will help.
[k88uaki] (score 5, diepte 0) Try putting baking soda in your shoes and shaking it around, you’ll probably need to do this about once a week.
[k8911t8] (score 5, diepte 0) Always have at least 2 pair of shoes and alternate days.
[k88tz0f] (score 3, diepte 1 OP) They only get wet from my sweaty ass feet
[k8a7mby] (score 3, diepte 1) This!!! I used to use Odor Eaters spray, and it made my feet smell like cat piss how OP described. BAKING SODA worked. I poured a little in my shoe and gave it a shake. In less than a month, my problem was gone.
[k8bgl8l] (score 3, diepte 4) There’s such a thing as “keto crotch”… or so I’ve been told, I love bread and beer
[k8912ez] (score 3, diepte 1) Yo? Do you know if this is limited to ingested protein or also from atrophy?
[k8ar79a] (score 3, diepte 1) You know, that's a GREAT point. When I was a gym rat, I noticed my shoes smelling bad and was like damn, that's never been a problem. 

I eventually had to start adding vinegar to my laundry for my gym clothes. Never, ever would thave thought of a high protein diet causing such things. Just chalked it up to the hard work alone.
[k88xu25] (score 3, diepte 0) Hang your shoes and take out the insoles when you get home. 

Also change your insoles at the halfway point of your shoes life. 

I also have foot odour at work, and I hate to say it, but you’ll probably need to buy shoes at a higher rate than your counterparts. I also get athletes foot every two months. Tough actin tenactin is the best for that. 

I got a new pair ever 3 months. Where I have buddies who keep them till they fall apart.
[k8aqdn5] (score 3, diepte 2) Not just for drying out. Unless you have custom insoles I bet you have some pressure points. I rotate between 3 pairs right now. One cushiony but not as supportive for long days, a basic elastic lace sneaker and Chelsea boots. And I use a charcoal insert for the smell.
[k89tlld] (score 3, diepte 2) Your shoes staying outside are a huge contributor to the problem. With foot odor, moisture is your worst enemy. Unless you live in the desert, there is always more moisture in the air outside than in your house.
[k8amz8j] (score 3, diepte 9 OP) Not with that attitude! Resell them as "gently used" for $2 each, and now it becomes a $30 a month habit. You're talking me into it, Chef. Your logic is undeniable.
[k8ax93f] (score 2, diepte 2) I too have suffered like you. What worked for me and ended my woes was getting two pairs of work boots, and I change my socks half way through the day cause fresh socks are one of the best feelings and I alternate my boots every day. I highly suggest you toss all your old socks and shoes and start fresh. Buy cotton socks, not synthetic. Synthetic materials hold onto smells in the worst way and while they might smell fresh when they come out of the wash, as soon as they warm up they'll stink like you never even washed them l. Socks should be replaced pretty frequently too, i replace most of my socks every 6 months (with the exception of fun socks that I don't wear every day). I Also recommend a shoe drying rack, the kind with a built in fan that blows warm or cold air into your shoes. I toss my shoes on there when I get home and they are always fresh and dry by the morning. Massive game changer!
[k8de6pj] (score 2, diepte 3) Also helps to take them stinky bastards off first thing when you get home.
[k89vzwm] (score 2, diepte 3 OP) I only started doing that with this pair in the past week or so, but I can see that being a contributing factor if I keep it up.
[k8aksei] (score 2, diepte 5 OP) I'm down with any excuse to get all new shoes. I usually change my socks along with my shoes daily. When you say wearing socks twice, do you mean ever, or without washing? People who wear unwashed socks on the reg are fucking psychopaths
[k8alic0] (score 2, diepte 6) I agree they’re nuts, and I meant without washing.
[k8alqmm] (score 2, diepte 7 OP) Heard, Chef. I was temporarily jealous of your sock budget.
[k8ama27] (score 2, diepte 8) Sock prices are insane these days for even the most basic. I wish I could afford to always wear a fresh pair, but I can’t afford a $3/day sock habit lol.
[k8adh29] (score 2, diepte 2) Go wool. Look up why wool works.   Below is a quick link.

Wool will allow water wapor to pass through it, cotton absorbs only

Also. Try taking unscented kitty litter in old socks. Put them in your shoes to absorb the moisture.

https://www.woolmark.com/industry/research/wool-is-naturally-breathable/
[k8aiiha] (score 2, diepte 0) Try salicylic acid along with the other tips here. My feet would get rank after 15 hours standing/walking around  in the heat (more so than colleagues) and it turned out I had athletes foot. It can spread all over your body (including your scalp and armpits) but ever since switching to a soap (and moisturizer) with salicylic acid I smell SIGNIFICANTLY better
[k8al0dh] (score 2, diepte 1 OP) Salicylic acid in my soap? Can I find that over the counter, or does it need a prescription?
[k8alhyq] (score 2, diepte 3 OP) Dope, thanks
[k8aszq6] (score 2, diepte 0) Are you wearing cheap vinyl/plastic shoes that don’t vent well? Might be worth considering shoe upgrade
[k8b2r1p] (score 2, diepte 3 OP) Similar to a super birki
[k8avghk] (score 2, diepte 0) Try bamboo socks. Worked for me
[k8avqtv] (score 2, diepte 0) I think maybe I saw this suggestion above once or twice but I want to emphasize it: shave off the dead skin. You don't need a pedi to do it. Ask your lady friend (I had to ask my mom 😁) where to get a foot scraper. It's basically a cheese grater for your callouses. Stick your foot in a trash bag and go to town. Then do the other one. Maybe come back again the next day, but getting rid of the dead skin helped me.
[k8avwu4] (score 2, diepte 1 OP) I have a microplane I use pretty regularly
[k8awksl] (score 2, diepte 2) Ahh, well, shit. Then you're beyond my ability to help. Sorry, but good luck figuring it out!
[k8bamag] (score 2, diepte 0) Buy new shoes and use a Shoe dryer/ boot dryer every single day. You can’t get the smell out but you can keep it under control if you never let your shoes stay sweaty overnight.
[k8bcojm] (score 2, diepte 0) Are your feet ever like super red and sensitive and hurt but not like rashy?
[k8bfjz3] (score 2, diepte 0) Do you wash your insoles on a weekly basis? Washing insoles and putting foot powder in my socks AND my shoes helps combat a lot of the sweat
[k8bgvjy] (score 2, diepte 0) “My head hurts, my feet stink, and I don’t love Jesus.”

Something I’ve encountered with people o worked with in construction, standing up on the shower and letting water run down your body and over your feed isn’t washing them; you gotta scrub those bitches. 

That being said, I’d like to echo getting a blood test to make sure it’s nothing serious if this is a new development.
[k8bu0k7] (score 2, diepte 0) Scrub your feet -- don't just run soapy water past them; have multiple pairs of shoes and rotate them with powder in them and dry them; dump blue bottle gold bond in them when you wear them; get antifungal spray/cream for your feet; soak your socks in soapy, acidic solution and change them throughout the day.

I've been out in 100 degree whether drilling gas wells,  and paving roads and found success using that strategy.
[k8by26z] (score 2, diepte 0) its just athletes foot. smelled it my whole life from time to time. throw your shoes in the laundry machine with detergent then air dry. your socks might need some bleach or lysol in the rinse cycle. buy wool socks although more expensive check costco for deals are better at wicking sweat and smells. if after a shower you still stink you will need to do a tub soak of white vinegar also from costco. put a chair in that shower and just sit and soak for 15 mins.
[k8cejoi] (score 2, diepte 0) Moisture that doesn't get a chance to dry out fully is generally what leads to bacterial growth, which is usually what stinks. Get a second pair of work shoes if you sweat a lot, and alternate them every single day. That way each pair has a longer amount of time to dry out in between shifts. If you're using impermeable clogs, you can just use odor eater inserts and change them daily instead the same way.
[k8cuvo7] (score 2, diepte 0) Are the shoes gross?
[k8a82ba] (score 1, diepte 2) What kind of socks do you wear?

And how old are your insoles and shoes?

Are they open clogs like Birkenstocks, or closed shoes?

Can you get a product called Pimafucort where you are? It’s prescription only where I am but it’s a tricyclic anti fungal with cortisol steroid in it and *super* effective.
[k8ak5hp] (score 1, diepte 3 OP) I wear cotton more often than not, but sometimes synthetic.
My insols are a couple weeks old
They're Kloggs. Very similar to a Birki, just lighter and more flexible
I'm not familiar, but will look. Texas
[k8cwmy3] (score 1, diepte 4) Cotton socks are not recommended for stinky feet. You need moisture wicking sports socks, not moisture absorbing cotton socks. Even better if they have silver infused in them. 

[something like this](https://www.amazon.com/Silver-Infused-Athletic-Dress-Socks/dp/B081S915WN)
[k8c1koy] (score 1, diepte 4) Your sweat, and some people have sweaty feet which makes them smell bad
[k88xud2] (score 1, diepte 0) I have had good luck with dr scholls odorx foot powder. Just a small shake into my socks, give them a shake, and good to go.
[k8cflkk] (score 1, diepte 2) Yeah the multiple pairs thing makes a huge difference, I have quite stinky feet and I try not to wear the same shoes multiple days in a row and it has really helped.
[k89n1p8] (score 1, diepte 2) The shoes last a lot longer too.
[k89c8jt] (score 1, diepte 0) Tea tree oil
[k89lia7] (score 1, diepte 1 OP) I have some for other things! Thank you
[k89jkwq] (score 1, diepte 0) a few things have worked for me:

1. Using Mouthwash to wash my feet at night.  Sounds weird, but if you get the kind with alcohol in them, it will kill any odor-making bacteria.  Just make sure you use some lotion after a shower to keep your feet from drying out too bad.  They smell like mouthwash after too, so thats what i smelled, not the stink (always gave me a chuckle too)
2. Baking soda in shoes.  I did this before and after shifts.
3. Light baking soda in socks when you know its gonna be a sweaty day.  Really does help, even if its every day.  

4. Some kind of foot-scrubber.  I had one of those sandal-looking scrubbers for a while, but just ended up using a loofah.  


If none of that works, go to a doctor.  They can definitely help and get to the bottom of it.  

If I could get my shit figured you, you got this dawg.  My dad's girlfriend quit coming over because of me, but it can be fixed I promise
[k89ldjz] (score 1, diepte 1 OP) Dude... that fucking rough. My shoes live outside. I have yet to run people off. I'm digging the multi-pronged attack
[k8a89rw] (score 1, diepte 4) Especially if it rains. I made that mistake once. No amount of cleaning will ever get the funk out once you do that. I had the stinky feet issue for years. I tried the powders and odor eaters and all that, nothing helped for years. Then what I did was threw away all my socks and shoes, and got new ones. As soon as I’d get home, I’d take my shoes and socks off and take a shower and made sure to never wear the same socks twice, and never wear my shoes without socks, not even for a minute. That’s literally all I did, and the problem has never come back almost 20 years later.
[k8aqylx] (score 1, diepte 10) Lol, you raise a very valid point.
[k89mz8i] (score 1, diepte 0) Wash feet daily.
Change socks often, never wear twice.
Try a nightly vinegar/water soak. Google starting ratios and what to build up to
[k89okdu] (score 1, diepte 0) a lot of good suggestions here but have you ever gotten a pedicure? i found that along with anti fungal, regular changing of socks diet etc etc.. pedicures help a lot and feel great
[k89v9ev] (score 1, diepte 1 OP) My lady and I have been talking about it, and my biggest hang-up has been the smell. One more reason that it must be done
[k8a9m10] (score 1, diepte 2) I definitely can relate. I would maybe just wash your feet prior to going. I see folks with diabetic foot conditions at times, who absolutely must have good foot health and often can’t do it themselves. If you haven’t seen it before it can be tough to look at (*** no judgement. diabetes sucks. i’m type II) The techs see it all, though. 

Once you get through your first one and they get through all the layers of dead skin etc, the next time you go back the smell won’t be as bad. And then each visit + your home routine will continue to improve.

Try some of the dieting advice and other suggestions too, but don’t be discouraged or embarrassed. All kinds of people with all kinds of feet get them.

I remember saying to myself I could actually “feel the floor” in my bare feet after my first one 


My feet used to turn my socks yellow, and crust / stick to my feet. Peel…Truly horrible. Shoes outside and all that. So glad I do t have to deal with it anymore.

Slip your tech a $10 you’ll be fine! Good luck! You will thank yourself.
[k8ajsgs] (score 1, diepte 3 OP) Thank you. You made me feel better about myself and the process. My feet aren't that bad, just sooooo sweaty all the time. I definitely don't feel as bad about them having to be by my feet.
[k89yt4o] (score 1, diepte 0) Do you live near the beach? I would always walk barefoot in the sand every now and then to exfoliate and dry my feet.
[k8a5g7j] (score 1, diepte 1 OP) I wish homie
[k8a0ipg] (score 1, diepte 0) Have you tried merino wool socks?  I switched to these full time and I swear the odor of my feet was reduced greatly.  I work a desk job so not as strenuous but I alway had a minor issue with foot smell.  You can get lighter weight ones; wool does not have to mean " uncomfortably warm in summer".
[k8a5ldi] (score 1, diepte 1 OP) I haven't tried wool. I have noticed cotton is way better than synthetic, but I've been hesitant to try wool because I'm in Texas
[k8a4bry] (score 1, diepte 0) Not a kitchen worker. The shoes I used to use made my socks and feet damp. I started using geox sneakers and work boots (diadora with geox technology). Since using those shoes my feet stopped smelling. When I use hiking boots after a long walk, the smell is back. Is important to let your feet to breathe. Don't know if you have that brand in the US, but maybe some use that kind of technology.
[k8a6cka] (score 1, diepte 0) Got a pair of sandals?  
Put em on, grab a box of baking soda and step outside, cover your feet, top and bottom in a healthy coat of baking soda.  
Walk around a bit, until you feel your feet get slick/wet.   
Then go rinse it off in the shower.   
Your sandals and feet will not smell anymore.   
Repeat weekly until smell is completely gone. (If feet cracked or dry, use lotion).  
Replace shoes and socks as needed.   
U can use baking soda in your shoe too, walk around with it and a sock on. Then dump it all out, replace your sock and you should be good for a few days.   
Takes multiple steps to get rid of it, but eventually it'll stop/slow down enough that you can handle it with simple odor eater spray.
[k8alcr5] (score 1, diepte 2) Totally over the counter, you can even get it on amazon. Just look for salicylic acid soap and you'll find a ton. [I've been using this one in a different scent](https://www.amazon.ca/Neutrogena-Clear-Grapefruit-Scent-Salicylic/dp/B00ET044TK/ref=sr_1_10?crid=1RQY9MHQVKSR7&keywords=salicylic%2Bacid%2Bsoap&qid=1699404625&sprefix=salicylic%2Bacid%2Bsoap%2Caps%2C141&sr=8-10&th=1)
[k8apuno] (score 1, diepte 0) I lived in the deep south (until recently), worked 10hrs a day with no A/C, and sweated my dick off. So much so, that it wasn't unheard of for me and my fellow coworkers to change clothes halfway through the day just to be fresh(er). I'm telling you, these things work. I had 2 pairs of work boots. I would wear one pair of boots for about 3 days before I'd swap them out for the other. And while one pair wasn't in use, I'd stick 2 of these deodorizer in each individual shoe. NO FUCKING SMELL! Even got compliments from one lady for "always smelling like Downy" lmao they actually smell like clean Charcoal. Game changer

https://www.amazon.com/gp/aw/d/B07NYTTV4C?psc=1&ref=ppx_pop_mob_b_asin_title
[k8apv0p] (score 1, diepte 0) Get a second pair of shoes and cedar shoe horn, leave the shoe horn in a pair for 24 hours at a time and switch out every other day. Also check with a doctor if it’s fungal related you could get prescription cream.
[k8atw1f] (score 1, diepte 1 OP) Kitchen clogs
[k8axhp6] (score 1, diepte 2) What material? Open back ?
[k8cm9qk] (score 1, diepte 2) Czech glass foot file. Bona Fide Beauty makes a nice one.
[k8az7yl] (score 1, diepte 0) 20 minute warm water and bath salt bath for your feet. Get a pedicure. I dealt with the same issue. The cracks in the dead skin in your feet are holding on to bacteria.
(4 reacties met lagere score weggelaten)

=== THREAD g0ixnq ===
SUBREDDIT: r/bartenders
DATUM: 2020-04-13  SCORE: 240  REACTIES: 81
TITEL: Since I've gone from being on my feet behind the bar for 12-hour shifts to being at home, and ideas how to handle the inevitable feet pain when we go back to work lol?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[fna0uhl] (score 245, diepte 0) I’m just wondering wtf is gonna happen when I have to go back to working. I’ve been sleeping 9pm-5am like a fucking freak
[fn9us4b] (score 74, diepte 0) If you have a ball of some sort (lacrosse, baseball, dog toy etc) roll the ball under your feet while standing with most of your weight on ball. It's basically the same as foam rolling other parts of your body. Peace and health to you friend.
[fnap2u8] (score 47, diepte 1) Yes. For real. Why the fuck am I waking up naturally at 6 am? With the sunrise?? What is this???
[fn9yvnz] (score 29, diepte 0) Compression socks!
[fn9x9vi] (score 28, diepte 0) I’ve been thinking about the same thing lol. At first I was missing my job so so much, but now I’m just like, meh. Maybe I want to find another career. We have some great managers, but one of my four managers literally hates me and treats me spitefully for no reason. Being yelled at, questioned, blown off and even straight up ignored when I have a legit need are things I don’t look forward to going back to as much as I love my bar.... so that’s probably how I’m gonna handle the feet pain, to answer the question. New job. :c
[fnbhdk4] (score 25, diepte 2) Wtf is up with you guys?

I'm going to bed at 6am..

My sleep cycle from work just got extended to being a few hours later 😫
[fna1w57] (score 24, diepte 1) This is very funny. Have an upvote.
[fn9wzfa] (score 21, diepte 1 OP) Thanks, that's actually some helpful advice! Gonna have painkillers at the ready when I'm back at work, too!
[fna8bqi] (score 20, diepte 0) I've been walking about 15km a day so hope to go back to work with legs of steel.

I might add that I'm in Sydney where the government hasn't fully locked us down yet.

A 3 hour walk in the middle of the day followed by 8 hours of videogames and wine... Gotta say I'm enjoying the quar. Even bumped into a few regulars on my hikes and did some responsible social distancing small talk
[fn9y0hv] (score 19, diepte 2) If you work 4/5 times a week and take painkillers each day, you're gonna have some bigger issues than aching feet.
[fna0c8f] (score 16, diepte 0) I’ll get downvoted for this but:

Be in better shape, period.

Run, walk, exercise.  You have plenty of time to start
[fna0h54] (score 15, diepte 1 OP) I have arthritis, and I'm in pretty good shape despite that! Mostly looking for ways to manage the foot pain since I'm not used to it every day anymore. Thanks for the suggestion though!
[fnakw36] (score 15, diepte 1) I've been going back and forth.  I was doing that for one week, then another week I was back to my late hours, and now it's somewhere in the middle, more like my roommate.  I don't know what the fuck is going on.  This has never happened before.
[fna9scm] (score 12, diepte 1) No mats?!? That sounds dangerous!
[fnac3u1] (score 11, diepte 3) I mean yeah, but we washed ours every night and mopped. Still better than someone spilling booze on a busy night and a bartender slipping in it.
[fna3r91] (score 10, diepte 0) Buy the best shoes you can possibly afford. My crazy ex boss wouldn’t let us have bar mats so we had to work on hard tile. Even with Danskos and inserts I had serious shin splits nearly nightly. 

I bought two frozen ice boot things I used to use after rough shifts. Stagger home, boil in an Epsom salt tub, take a handful of Advil and sleep in those frozen boots. The compression and the cold would help immensely. 

Keep in mind I’m middle-aged, have a herniated disc and mild scoliosis. This is likely overkill for anyone younger and healthier.
[fn9zkfq] (score 9, diepte 0) Make sure you have good (and correct) inserts in your shoes. Go to any of the ortho-stores or a high-end running store and they will be able to tell you what type of arch you have and match you with inserts made for your feet. 

Keep on your feet. Being out of work doesn't mean being on the couch. Take regular walks and hikes. Myself, I'm starting to run again, trying to lose some of the weight I have put on being in the industry. We're all likely to be out of work for an amount of time that will allow for full body makeovers. If you don't come back to work at least a little healthier, will you be happy with how you spent this opportunity we have been given?

Also, like a commenter below - take the time to assess if you really want to go back. Plenty of people love this industry and would do anything for it. They have jobs they love and are passionate about their work. Would I be happier elsewhere? I'm not sure, but I think so. I'm taking this time to explore my options.
[fnaksd9] (score 9, diepte 0) I've wondered how I'm going to carry a crate of beer on my shoulder even once, let alone several times a night.  The heaviest thing I've lifted in the last month is a cheeseburger.
[fn9y6ez] (score 8, diepte 3 OP) Did I say every day? Lol.
[fnafclb] (score 8, diepte 3) What if I take 4/5 in one day? BOOM. Lawyered.
[fna0y1p] (score 7, diepte 2) Having arthritis puts you in a whole other category completely and idk how much help a bunch of bartenders are gonna be for that.  But, always good to look for solutions.  Hope you get behind the bar ASAP!
[fnb2cmq] (score 7, diepte 1) Seriously, my wife has been expressing concern because I keep waking up early to tend to the cats and make her coffee before she goes to work (she works in healthcare).

I tell her, well what the hell do I have to sleep in for? I’ll just take a nap if I’m tired!
[fnax4td] (score 7, diepte 5) That.... doesn’t sound very safe either lol
[fnbc2ak] (score 6, diepte 5) I have literally walked my sleeping schedule around the clock.  Woke up at midnight last night/this am.  Its 5pm here and I'm fixing to turn in.
[fnbtpbh] (score 6, diepte 3) This.
[fna2fh3] (score 4, diepte 2) This is good advice. A golf ball works best for me though
[fnabxvz] (score 4, diepte 1) Came here to say this. Coupled with decent shoes I've had much less foot and leg pain after long shifts!
[fna2j33] (score 4, diepte 0) Yoga. Can't stress this enough. I do yoga for at least an hour 3-4 times a week. Lots of downward dogs will stretch your feet out. With arthritis you may want to look into alternative diets as well. I used to have all sorts of issues. Pain meds and doctors visits were getting real annoying, but then I found the specific carb diet. Basically you cut out disaccharides and polysaccharides (no bread, rice, sugar, beans, etc[it's not a keto diet]) because they cause inflammation and other issues. I could go super deep into why but this post is already long enough. I eat unbelievable amounts of fruit and meat, and have no more knee pain. As soon as I eat a single goddamn slice of bread or a potato all my inflammation comes back in my wrists, knees, wherever. People are going to read this thinking I'm hyping up some "diet fad" but I'm not. It's not for everyone,  just something else to look into. Good luck.
[fnaiu8t] (score 4, diepte 1 OP) Don't have a garden or own a car, don't live near anywhere I could hike and I'm in the UK where we can't go out (even daily exercise outside is discouraged and limited to 15 mins).

There's no way I could replicate standing up for 12 hours solid on a shift even if I wanted to do that for no money lol!
[fnavhs7] (score 4, diepte 0) My lower back has started hurting from sitting/laying too much whereas before it hurt from walking/standing so much. Turns out I just have a shitty spine
[fn9xrnx] (score 3, diepte 0) Take a tennis ball (or sorta) puto it on the ground and make little and Big circles with your sole of the foot
[fnaeywg] (score 3, diepte 1) I wear Jordan socks, as they are fitted, has built in shock absorbtion and a slight compression effect. (brother in law owns a basketball store and he gave me that tip)

https://www.amazon.com/Jordan-SX5854-010-JORDAN-ULTIMATE-FLIGHT/dp/B073WFF16N/ref=mp_s_a_1_3?dchild=1&keywords=jordan+ultimate+flight&qid=1586796100&sr=8-3
[fna151z] (score 3, diepte 3 OP) Thanks! Walking around so much is actually really good for keeping my joints from losing range of motion, but obvious I can't replicate so many hours of being on my feet when I'm at home. I figured people might have some tips and tricks!

Hope the same for you too! 😊
[fnb9m39] (score 3, diepte 2) I'm in the same boat. I was waking up at 4-6am the other week. Now, it's like 9:30-10:30.
[fnbxt7k] (score 3, diepte 3) Same!
[fnaq1tf] (score 3, diepte 1) I’ve been forcing myself to stay up until my regular sleeping time (around 4ish) because I know whenever this is all over, If I slept like a normal person, it would be hell on me to get back to it. Some nights have been tougher than others...
[fna39va] (score 3, diepte 0) Toe spacers my friend. Tell everyone about toe spacers.
[fnbh1sx] (score 3, diepte 2) I've literally never worked in a place with bar mats. Most places don't have them here.
[fnakj0k] (score 3, diepte 0) My super gnarly foot callous came off a couple days ago. Looks great, but oh man, there’s gonna be pain.
[fnanacd] (score 3, diepte 0) I remember when I got my first real kitchen job and how I used to just come home go straight for the tub use my peppermint foot scrub (which did help), and just weep as I soaked my feet and calves. Part of the problem I realize now is my non slip shoes sucked, and had zero arch and ankle support. Get some good insoles, or get just better fitting shoes then I did. And honestly that peppermint foot scrub really helped get blood flowing again, I would've been way worse off without it.
[fnb2hps] (score 3, diepte 0) Compression socks. Compression socks compression socks compression socks.

You’ll thank me.
[fnbuqgd] (score 2, diepte 2) Tennis balls too!
[fnb8v4q] (score 2, diepte 1) Frozen water bottle is my go to!
[fnbs9ax] (score 2, diepte 1) Bitch it on the ground
[fnag7qt] (score 2, diepte 2) Shoes are extremely important. Get some shoes that aren't too soft, aren't too heavy and lets your feet breathe. Hot feet means sore feet, sweaty feet will give you all kinds of foot problems. I buy shoes that are made for factory workers, as they are made to be worn all day, are non slip and are pretty hard to wear out. You can get them in a lot of different designs and without steel toes.

Have two different pairs of shoes and keep one pair in the cooler, change mid shift. Change socks as well, if they are damp.
[fnbaa8j] (score 2, diepte 3) In the past month, I've gone anywhere from waking up from 4 - 6am, to my normal working hours, where work starts at 10pm and I wake up between 3 and 7pm.
[fnbfojp] (score 2, diepte 6) Yup, I also worked that job for the better part of a decade. At that time, if I stepped out into the sunlight, I'd instantly goosebump. That's how good it felt.
[fnat1av] (score 2, diepte 1) THIS. 

My Yoga Toes and my foot roller are the only reasons I still have functioning feet.
[fnad4m4] (score 2, diepte 0) Google some excersises designed to strengthen lower legs, ankle, and foot muscles! Do them while you watch TV for a few hours @ night and the soreness will come right back!
[fnadg5o] (score 2, diepte 0) I do a combination of rolling the soles of my feet, compression socks for longer shifts, orthotics, and Crossfit shoes. I have a lot of foot issues - extremely flat feet, a birth defect and 2 serious old injuries to one foot/ankle, and a fibroma in my other foot - so it's been a journey of trying to find the right combination that works for me.

Rolling: The previous owner of my home left a metal foot roller that you can put in the freezer to cold roll the bottoms of your feet. [Kind of like this](https://smile.amazon.com/GoFit-Polar-Roller-Plantar-Fasciitis/dp/B01B6QSD7S/ref=sr_1_3?dchild=1&keywords=metal+foot+roller&qid=1586795214&sr=8-3) It helps for after a long shift.

Compression socks: These things are great. I prefer the ones with a medium level of compression (20-30 hhmg) and while they don't eliminate the development of foot soreness, they do help mitigate it and shorten the recovery time. 

Orthotics: If you have health insurance, custom fit orthotics might be beneficial. Mine were paid for through my insurance and help tremendously with foot pain after a long shift but I have unusual feet. 

Crossfit shoes: I've found runners are too squishy and flatten out from standing in one place (like the service well) for too long and sneakers aren't supportive enough. A decent pair of Crossfit shoes was only about $60 and they have the comfort of a running shoe, but a firmer heel. For me, they have the stable feeling of a good boot, but the flexibility and lightness for running around the restaurant, crouching to get this or that, leaning over the bar, stretching for top shelf stuff, whatever. I don't actually do Crossfit, but the shoes are the best I've worn behind a bar.
[fnaeqjb] (score 2, diepte 0) I started doing instacart for the money but its kept me on my feet
[fnai5r8] (score 2, diepte 0) Be on your feet now. Do yardwork, play videogames standing up, get a hobby that you have to be standing for. Dink with your car, hike, just stay on your feet and stay fit then you dont have to worry about going through that pain again.
[fnbvsva] (score 2, diepte 1) Same here exactly!
[fnb85n9] (score 2, diepte 0) Soaking my feet/legs in the hottest water I can possibly stand with Epsom salts always helps me after a long shift! I also wear a bunion protector sleeve under my socks at work. It really helps me because I tend to put a lot of my weight on my big toes when I stand at work all day
[fnbeinv] (score 2, diepte 0) Insoles bruv. Game changer
[fnbfrax] (score 2, diepte 0) I hear those millennial boots are pretty comfortable  and get the job done.  I don't know what the real name for them are, but you probably know which boots I'm referring to.
[fnbhapy] (score 2, diepte 0) Thanks for reminding me 🙄
[fnbkffv] (score 2, diepte 0) Before I started bartending I was a barback at my most recent place of work. Bar backs at my bar don’t usually last too long, because everything we need was down a flight of about 20 stairs in the basement. Keg/beer room, syrups/juices, liquor, fruit, ice, literally everything the bar needs is down that dreaded flight of stairs. Weekends were usually busy as fuck since we were a popular spot downtown that everybody wants to be at, so half the job is up and down those stairs. 


After a few months of wearing cheap non-slips, my knees, hips, and leg muscles would hurt for a few days. Eventually I was experiencing pain mid shift, so I decided to find some better shoes. I spent $90 on a pair, and lord have mercy on my sole (lol) the pain went away after breaking those shoes in. Super comfortable and I felt like a brand new man, really never experienced the pain again. 

Moral of the story; save the money and invest in a solid pair of shoes and maybe some inserts. Quality shoes will last a long time and a 9 hour shift will feel like a breeze.
[fnbw839] (score 2, diepte 0) I think we are all just going to have to suck it up, unfortunately, no matter your fitness level. All of us are gonna be in extra pain the first week or so back before we return to a “normal” amount of pain.
[fnef1gk] (score 2, diepte 0) If you have any resistance bands/therabands around there are exercises meant for dancers to strengthen ankles/feet. I do those sorts of exercises daily (was more like weekly back when I was working/leaving home). Cirque\_physio on instagram has some really good ankle/foot strengthening exercises. Keeping your feet/ankles warm and moving around daily will certainly help. Giving yourself foot massages, wiggling your toes a lot, all good stuff.
[fnc7u8t] (score 1, diepte 2) Oooh there an idea!!
[fnbhkf8] (score 1, diepte 2) Those look really nice. I’m getting some!
[fnbi19f] (score 1, diepte 3) Anything to help those poor feet, right :)

They are very nice and they last a lot longer than a pair of cheap socks.
[fnbauah] (score 1, diepte 4) I remember when I used to wake up at 7pm. I had a truly overnight job that ended at 7-8am. Good times.
[fnbcdts] (score 1, diepte 5) Yeah... I've done it for years.  For more than five years now, my earliest shift has been at 5pm, with late shifts starting at 10.  I've always been a night owl, so in some ways it's good for me, but it's also really worn me down a lot.  If I *could* go outside now, I'd be enjoying the sun.
[fnbuxbj] (score 1, diepte 2) Foot roller?
[fnbvjsa] (score 1, diepte 3) It’s this wooden thing you put on the floor and then rub your feet all over. It’s amazing. [This is the one I’ve got.](https://www.amazon.com/TheraFlow-Massager-Relieve-Plantar-Fasciitis/dp/B00SMJIYNG)
[fnbymp4] (score 1, diepte 4) OOH 😍. Thank you!
[fnaolob] (score 1, diepte 1) Came here to say this. The best shoes you can find, AND get your feet scanned. The inserts that are made specifically for your feet are THE BEST.
[fna42t3] (score 1, diepte 0) I’m getting soft.
[fna4yqg] (score 1, diepte 0) You remember that scene in Brubaker where the guys stand on bottles? 
Try that!
[fna9rek] (score 1, diepte 0) Check this out at Amazon.com
Superfeet Black Premium Insoles https://www.amazon.com/dp/B000XY9NYW/ref=cm_sw_r_other_apa_i_BYiLEb3WGKTC8
[fnajpzz] (score 1, diepte 0) Get a box of tissues
[fnbdjyc] (score 1, diepte 0) Go for some long walks if you’re in a place that allows it...do a 10 minute tabata of jumping rope.
[fnbivii] (score 1, diepte 1 OP) Aww I'm sorry haha!
[fnbs8ce] (score 1, diepte 0) Fpinsoles my brother
[fnbuk60] (score 1, diepte 0) Try walking. I hear it's good for walking.
[fnc9hid] (score 1, diepte 0) Mother fuckin' compression socks.
[fnabkmd] (score -6, diepte 2) Sounds clean. Bar mats are truly disgusting.
[fnacizr] (score -10, diepte 4) I dont have bar mats at my current place, but all the bartenders are sub 30. Ice skating behind the bar is a game and on busy nights it can actually be helpful.

=== THREAD 16u2jug ===
SUBREDDIT: r/bartenders
DATUM: 2023-09-28  SCORE: 27  REACTIES: 81
TITEL: Let’s talk shoes…
POST (source_id=post):
25f and I work at a sports bar. It’s football season, and I have some crazy hours. I currently am wearing sketchers nonslip shoes. They’re good. Not great. I want something with a lot of support. I also wear docs from time to time, but they get super hot. I’m talking 18 hour shifts open-close, running around like crazy, 7-9k in sales a shift… I’ve been reading about blundstones, but are the boots bulky/hot??? Also was looking at nonslip tennis shoes from either keen or Birkenstock. Maybe no matter what the shoe is, my feet will hurt after an 18 hour shift 😭

Recommendations are appreciated!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k2iptvv] (score 36, diepte 0) Blundstones are great but they are definitely hot because they are waterproof! are you allowed to wear sneakers? You should definitely consider a Hoka if so - the Bondi style is very supportive and the only shoes that don’t give me fatigue in the shins after a day of running around.
[k2iue6a] (score 21, diepte 0) Vans now makes shoes specifically for industry! They have a whole line. It's called the makers. Everything has insoles and non slip soles. Love them. I bought a pair in 2019 and they lasted me thru 3 years of ice storms, floods, and slippery kitchen floors!
[k2ipfs8] (score 18, diepte 2) Well if you work 18 hours no matter what shoes you wear your feet are going to hurt .
[k2jo884] (score 17, diepte 1) Damn I chewed through vans industry shies every 6mo… I just stopped buying them. Comfy but cheap material. I got some steel toed doc martins instead
[k2in45f] (score 16, diepte 0) Honestly, you could probably search this sub for that. This gets asked daily.

I'm going with: Solovair + Superfeet (green) insoles.
[k2j2mhh] (score 15, diepte 0) You can check out this thread here: https://reddit.com/r/bartenders/s/tSrF0XNTs7

Or this one: https://reddit.com/r/bartenders/s/q8DmFWFvjW

Or this one: https://reddit.com/r/bartenders/s/jx3czwNaVq

Or this one: https://reddit.com/r/bartenders/s/XFJGIYAcQp
[k2irgx5] (score 9, diepte 0) Hokas are comfy and breathable
[k2iv4l8] (score 7, diepte 1) Blundstones forever.
[k2iniiu] (score 6, diepte 0) You work 18 hour shifts ? how is that even possible ?
[k2ivsz3] (score 6, diepte 1) *Blundstones and the right socks are how I should put that. I work outside day job and tend at night. Wool socks no matter the weather in the field and behind the bar.
[k2kbpxj] (score 6, diepte 1) I personally would swap shoes halfway through! Usually start with vans and finish with docs since people are going to be drunk and also closing the bar can get messy, so being water proof is key, especially when your brain has disintegrated into mush.

Also idk which docs OP has but mine are the Chelsea boots, and I didn't find the normal lace up boots that comfy tbh. Them coming out with platform vegan Chelsea boots was a wish come true!!
[k2j07fv] (score 6, diepte 0) Crocs mercy work clog. My feet feel amazing in them and they’re non slip closed toe. I have back problems and plantar fasciitis and can work doubles in them with no problem.
[k2itx21] (score 5, diepte 0) Just buy multiple pairs of shoes. Avoid dr scholls imo. Everyone has a brand but i think rotating 3 pairs of whatever is the answer
[k2ip06k] (score 4, diepte 1 OP) 9am-close. We get an hour break. It’s just for busy season so I guess like 17-18 hours depending on how long cleanup takes.
[k2ipbri] (score 4, diepte 0) Is Shows for Crews still a thing? Used to get great boots for behind the bar from there.
[k2j8juu] (score 4, diepte 1) I just bought a pair of [these](https://www.vans.com/en-us/shoes-c00081/sk8-hi-reissue-uc-made-for-the-makers-shoe-pvn0a3mv5v7w?cm_mmc=GPF-_-google-_-merchantcenter-_-VN0A3MV5V7W&utm_id=go_cmp-19615470172_adg-_ad-__dev-m_ext-_prd-VN0A3MV5V7W_VN%3A0A3MV5%3AV7W%3A095%3AM%3A1%3A_mca-8181713_sig-EAIaIQobChMI-5PY07jMgQMVL3FMCh2B8AEOEAQYAyABEgLOIPD_BwE&utm_source=google&radscid=19615470172&gclid=EAIaIQobChMI-5PY07jMgQMVL3FMCh2B8AEOEAQYAyABEgLOIPD_BwE&gclsrc=aw.ds) because of a rec from this sub and I love them. They were instantly super comfortable. Feel super stable and are relatively supportive with a nice removable insole. Water resistant, non slip and lightweight. $95. Highly recommend
[k2j0vul] (score 4, diepte 0) I swear by on cloud waterproof. I have multiple pairs in the same color, the super broken I’m ones I wear when I’m not at work, save the new ones for only at work. Worked the last two seasons two blocks away from an NFL arena behind a bar that didn’t have mats. They saved me. For longer shifts, maybe have two pairs of really supportive shoes to change the pressure points
[k2jfz9o] (score 4, diepte 1) Aw but why search when you can get someone else to do it for you 😩
[k2js8qh] (score 3, diepte 2) I wore Docs all thru my 20s and then I just couldn't anymore....they are so hard on my ankles and heels. Even with breaking them in. I guess it really depends on your feet and your movements, ay?
[k2j90ru] (score 3, diepte 0) Blundstones are all I wear. They’re not hot, I just wear ankle socks. Protects my feet from allllll the bullshit.
[k2iyf33] (score 2, diepte 3) I’ve gone through 3 pairs since 2014. Good to have a daily driver.
[k2tdpch] (score 2, diepte 1) Seconded Hoka. They make non slips and they are incredibly comfortable.
[k2jyqab] (score 2, diepte 1) This! OP please read this!

It's way better for your feet to change up your footwear (keep a pair at work and change during the day even)
[k2ljx95] (score 2, diepte 2) This is a good idea! 18 hours is too long for one pair
[k2kvrv6] (score 2, diepte 1) Came here to recommend crocs as well. They’re the best I’ve found in 17 years of wearing non-slips.
[k2j5a82] (score 2, diepte 0) You need orthotics!!!!!!!!! Get custom made ones. Foot problems gone.
[k2jbw46] (score 2, diepte 0) VIBRAM SOLED ANYTHING.

My preference is Merrell Moab 2. They have Vented or Waterproof, Low-top or Boot.
[k2k7xxe] (score 2, diepte 0) Non slip new balance. Model 626. They're ugly as sin but great for your feet. I've been wearing them for work for about 3 years now.
[k2l2c7n] (score 2, diepte 0) crocs (from the actual website) are pretty good! they don't hurt my feet (not in a noticeable way, but after a 12 hour shift, my feet are GONNA hurt. they're less than $50, and they're like all rubber. so you can rinse them off easily. also they don't soak up water like other non slips. i cannot STAND that feeling. if you step in water in the crocs, you'll be fine. 
the only con: they smell? not noticeably, and i guess depending on your restaurant, they are a bit stinky. but that is generally true of all non slips, so i wouldn't let that put you off. i also bartend and wear these shoes
[k2lqmlk] (score 1, diepte 3) It’s true but you’re just trying to mitigate the damage at that point
[k2iu0c0] (score 1, diepte 1) Airports and casinos
[k2itxad] (score 1, diepte 1) It is. Went from bar to kitchen and I swear by then. Next best thing in similar price point is New Balance trail runners for behind the bar.
[k2jpsgq] (score 1, diepte 1) They are and they’re awesome! They have some white converse looking ones that I’m a fan of! My other pair of shoes are some non slip birks!
[k2ix1km] (score 1, diepte 2) Blundstones are truly amazing - they are my winter shoes!
[k2jq8iq] (score 1, diepte 1) If ur broke look at rock rooster Chelsea’s. around $100-$120 super cushy and hold up.
[k2k2dt7] (score 1, diepte 1) I went with Blundstones direct competitor, Redbacks. Also made in Australia, thicker/softer foam sole, cheaper.
[k2m42mn] (score 1, diepte 1) Merrel Jungle Mocs.
[k2l1wz1] (score 1, diepte 2) I started doing it to avoid my feet stinking lol but yeah it turned out to be a gamechanger. Never got blisters since doing it
[k2jiske] (score 1, diepte 2) Same shoes bro, they’re amazing
[k2jsdog] (score 1, diepte 2) I have them too!!!! Love them!!!!!!!
[k2ltlxn] (score 1, diepte 2) This was me. I thought they were my go-to shoe until I tried docs. My feet and legs don't get fatigued near as fast in my boots.
[k2lulzw] (score 1, diepte 3) I also have different comfy but not work shoes to go home in - these are what I would wear to work too, since I live in London and there's so much walking involved in changing at some stations.

I do develop plantar fasciitis every time I start working in hospitality, so maybe my feet are just very sensitive
[k2m75z9] (score 1, diepte 2) Great idea! I do this sometimes on my long event days. The only thing that hangs me up is bringing a second pair of shoes is just ONE MORE THING I have to stick in my backpack for a long shift. I hate carrying that shit around on the train.
[k2q2qmw] (score 1, diepte 3) Can you not leave it somewhere at your work place? Tbf I did have a lot of stuff in the pub, just in case I forgot something lol
[k2r152m] (score 1, diepte 4) No, we don't have a staff area, or enough space to make that happen. And my 2nd job is always off site so we also don't have the ability to do that. Jansport xl backpack for the win
[k2kf0zb] (score 1, diepte 1) Second the on waterproof. I’m on my third pair, but only because I wear them out working behind the bar. Third pair in 3 years. Great and comfortable with good tread.
[k2j3fgq] (score 1, diepte 0) Bates boots. I work in a place that's poured concrete floors with no floor mats and they haven't let me down yet. The pair I own are composite toe so I've got some protection without being super heavy. They're actually incredibly light, much better than Docs. I generally work about 8-9 hour shifts and my feet/knees rarely hurt at the end of the night anymore. 

To my understanding they're primarily used by cops and paramedics so it makes sense that they hold up well. They also have a side zipper which is convenient.
[k2j4on5] (score 1, diepte 0) I rock the sketchers no slip with Dr Scholls inserts. It’s a little pricy but it’s absolutely worth it
[k2j6b2l] (score 1, diepte 0) I got some all black New Balance that work well for me with insoles from a podiatrist, would highly recommend going that route if you have any issues with all the miles you are eating up.
[k2j8hfv] (score 1, diepte 0) I swear by timbs. Either the beef and broccolis or the constructions. Unlaced. Yea boiiiiii
[k2jeyn2] (score 1, diepte 0) Hoka Salomon and Sorel are good options! you can get non slip hiking boots that look like nice/casual.
[k2jhoe7] (score 1, diepte 0) I actually do wear Docs every day, but I also have three broken toes right now, haha, and they're the only shoes that don't hurt (I got good insoles for them!) after a 12hr shift. 

Usually, when I'm not in pieces, I wear a combo of Docs, Hoka Bondi SR's (they're made for folks in the bar/restaurant industry/nurses. Completely leather, stain-proof, slip-proof, totally worth the money!), Blundstones, or high-top Vans from the Makers line. I like to change it up based upon the outfit I'm wearing for the night, and also the season - though lbr, it's always hot af when you're bartending.
[k2jk442] (score 1, diepte 0) The Guard
Oil and slip resistant
Waterproof
Great support 
Military/Resistance look 
6 months plus

I sold shoes for 10 years. I use to fit people’s feet for specific shoe types. For the price these have been outstanding. I work long shifts and I assume I am heavier than you are and they hold up well. Arch and foot type will play a part in any shoe that you wear. Shoes size could be an issue as I believe they are men sizes only.  So it’s a size and half difference. A 7 men’s is an 8 and half women’s plus width. You can find them at Walmart. FYI other models in the same brand are not even close. It needs to be the Guard or Pilot if you can find it. Bright green box. 

Make that money! 

https://interceptorboots.com
[k2ohuae] (score 1, diepte 2) Hi, I’m Vetted AI Bot! I researched the **'Interceptor Litefast Zippered Tactical Boots'** and I thought you might find the following analysis helpful.

**Users liked:**
* Boots are comfortable and lightweight (backed by 4 comments)
* Boots provide good ankle support and traction (backed by 4 comments)
* Boots fit well for those with wider feet (backed by 3 comments)

**Users disliked:**
* Boots run large and loose (backed by 1 comment)
* Boots fall apart quickly (backed by 1 comment)


If you'd like to **summon me to ask about a product**, just make a post with its link and tag me, [like in this example.](https://www.reddit.com/r/tablets/comments/1444zdn/comment/joqd89c/) 

This message was generated by a (very smart) bot. If you found it helpful, let us know with an upvote and a “good bot!” reply and please feel free to provide feedback on how it can be improved.

 *Powered by* [*vetted.ai*](http://vetted.ai/reddit)
[k2jo25s] (score 1, diepte 0) Pumas fit me best. I have high arches.
[k2jwa7p] (score 1, diepte 0) I’m a sneakers nerd
[k2jzc4i] (score 1, diepte 0) Real talk, my Blundstones are the most comfortable boots I've ever worn. They don't get hot imo (the sides are breathable), but they are a bit bulky; it's something I've gotten used to, though. I paired them with some good insoles and I dunno about an 18, but I could do a 10-12 and not hate myself the next day.  
  
I will say this.. the anti-slip coating wore off after about a year of steady use. I thought I was king shit until I started sliding around in 'em, so do be careful. Luckily I'm at a new gig where that isn't such an issue and I think they'll get a few more years in before I need to retire them.
[k2k41k6] (score 1, diepte 0) I’ve owned one (1) pair of blundstones that were genuinely THE single most uncomfortable pair of shoes I’ve ever put on my feet lol, and after that experience I straight refuse to even TRY the brand again haha
[k2k7g3j] (score 1, diepte 0) Merrell tactical shoes are awesome
[k2k8ffz] (score 1, diepte 0) i usually wear chelsea boots from ganni, super comfortable and sturdy once you've broken them in. or buffalo london sneakers.
[k2kjfcp] (score 1, diepte 0) I used to just go to pay less get the same 15 dollar non slip boat shoe looking things. Wear them till I pivoted out of the sole and by another pair. I’m 250 lbs I wear through $200 shoes as quick as 20
[k2kqys1] (score 1, diepte 0) I have 1 pair of adidas ultraboost 22 that look disgusting because of coffee and what not dripping on them, but they saved my ankles from evaporating can only recommend. They've been my go to work shoes for a while sneakers wise.
[k2kuteg] (score 1, diepte 0) I wear a pair of black Brooks on shift. They’re breathable and I’ve noticed a difference in my back pain since I started wearing em.
[k2kxo6q] (score 1, diepte 0) Hoka work shoe is the best answer, hands down.
[k2l2w9w] (score 1, diepte 0) I have the poly comb docs- the fabric breathes better!
[k2l9ol8] (score 1, diepte 0) Fp insoles made a big difference in my fila work high tops, as far as foot, ankle and back pain reduction. They lasted roughly 6 months until my heel started splitting through. I’m trying z liners now and they’re still breaking in but so far I like the fp insoles better.
[k2lb77x] (score 1, diepte 0) i wear new balance x shoes for crews and they’re amazing. i always bring a change of socks on long days, makes a huge difference halfway through.
[k2lhtht] (score 1, diepte 0) Hokas
[k2lt39i] (score 1, diepte 0) I highly suggest taking a look at Snibbs. They are pricier, but your feet won't ache.
[k2mmzpe] (score 1, diepte 1) I have a pair of snibbs and I really don't like them. They are slip on shoes despite the fake appearance of having an actual lace and the non slip is still not as non slip as a legit work shoe. 

My opinion though n
[k2lvkyl] (score 1, diepte 0) Honestly the most comfortable shoe I ever had for this job was the dansko clog from the collection meant for nurses. They’re not exactly the most attractive shoe but they certainly were easier on my feet and back
[k2m765d] (score 1, diepte 0) Bluestones are not that hot at all. Just get the right socks for the season. I have two pair.  It my favorite work boot right now is the danner 8” bull run. They’re uninsulated and but tough leather and I can do anything in them.
[k2mn8dy] (score 1, diepte 0) Not sure if this was said yet but a pair of compression socks can also help a lot, did work for me in addition to a good shoe.
[k2muyqt] (score 1, diepte 0) Shoes for Crews… cole haan miles textile wingtip oxford
[k2ns63n] (score 1, diepte 0) Strongly recommend Redbacks. Lighter than blundstones and easy on the feet. Just a little pricey but they pay for themselves quickly
[k2nzjrh] (score 1, diepte 0) Fila Non Slips on Amazon are the best work shoes for price point IMO.
[k2ohgfi] (score 1, diepte 0) A quality insole like Dr. Scholls has saved my feet from eternal damnation on long bar shifts. Also, this is cheaper than a new pair of shoes if you like your current setup, but want some added cushiness and support.
[k2oudb0] (score 1, diepte 0) Hoka nonslip
[k2q4w2o] (score 1, diepte 0) I like the canvas skate shoe from shoes for crews. I add. dr scholls inserts.
[k2qeiim] (score 1, diepte 0) IMO, stick to Blundstones and proper socks. Regardless of weather or location, wool socks r a must-have, great for outdoor work and bar tending time. Helps tons, no joke.
(3 reacties met lagere score weggelaten)

