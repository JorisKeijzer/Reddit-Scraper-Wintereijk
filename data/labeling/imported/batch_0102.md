# Label-batch batch_0102

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
Schrijf het resultaat naar `batch_0102.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 144buzx, 1xlwo9b, 17wh9qx).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 144buzx ===
SUBREDDIT: r/Disneyland
DATUM: 2023-06-08  SCORE: 417  REACTIES: 621
TITEL: What do you guys do to make your feet not hurt after a day in the parks? I wear Nike running shoes and am in decent shape but my feet and legs are always so sore. I see people wearing Vans and I would for sure be limping at the end of the day. How do you guys manage?!
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jnelm8w] (score 309, diepte 0) I like to put some of those squishy Dr scholls things in my shoes, bonus is that you can walk around telling everyone you’re “gellin”
[jnetlpk] (score 249, diepte 0) Compression socks are magical. I wear them after distance running, so I thought why not wear them after Disney. It speeds up my post Disney recovery and cuts down on swelling.
[jnekcty] (score 233, diepte 0) You push through the pain. I can’t imagine that after a full day in Disney that someone’s feet don’t hurt. Before we went to Disney World two years ago I started researching comfortable shoes for Disney and a few people recommended Allbirds. I bought a pair and broke them in and can agree they are some of the most comfortable. I’m on my second pair and just spent two days in Disneyland and DCA and my feet still hurt.
[jnf1ulf] (score 147, diepte 1) I’m imagining Mickey Mouse yelling at me like a drill instructor when my feet start to hurt. 

“Ha ha oh boy you better push through the pain”
[jnemeze] (score 140, diepte 0) Lots of walking ahead of time to prep. Bring at least two pairs of comfortable waking shoes that are already broken-in and switch them off at least daily.

I tend to do mid-day breaks back to my room, so I'll take off my morning shoes, apply some foot cream to feet and sore muscle cream to legs and elevate my feet for an hour or so. Check for any areas of rubbing any apply moleskin. Then put on the other pair of shoes before heading back to the park for the evening. If you're feeling fancy switch socks mid-day too.
[jnen64z] (score 96, diepte 0) I bring a lacrosse ball with me on every trip. Roll the ball back and forth on each foot for a couple minutes. Does wonders.
[jneltge] (score 84, diepte 0) Adidas Ultraboosts
[jnenwj3] (score 78, diepte 1 OP) I wish they sold these in the park. I would buy them!
[jneuf0q] (score 66, diepte 1) Changing out socks mid day with my shoes was a game changer. Your feet just feel more refreshed. Plus you get that little extra cushion of a fresh pair, buying new socks for the trip if you are feeling extra fancy. 

I basically try to get ahead of the pain because I know it's going to come. So I'm elevating my feet when I get to the room on day 1 and staying plenty hydrated even if the aches haven't set in yet.
[jnerdna] (score 66, diepte 0) Hoka's for the win!
[jneos2w] (score 62, diepte 0) The key is to change shoes half way through the day. I wear Nike running shoes as well, but will switch over to a pair of Oakley flip flops for a couple of hours, then back to the shoes. I’ve never had an issue since I’ve started doing this. Also, for multi-day trips, never wear the same shoes consecutive days.
[jnezuyb] (score 57, diepte 1) Compression socks for sure! Though I wear them in the park, then take a break when home/hotel before putting them back on.
[jnes8fw] (score 46, diepte 2) Some hotels across the street sell them in the little convenience stores. I think Tropicana or park vue if I remember correctly.
[jnfo48o] (score 42, diepte 2) I don’t think it’s the walking so much as the standing.  I’m a distance runner and rarely if ever do the bottoms of my feet hurt from going 12+ miles, but after a day at Disney?  Hoo boy.
[jnemo07] (score 39, diepte 0) I don’t have a shoes suggestion, but I can recommend a mint lotion for that night!! 
Nothing will feel better than warming up a washcloth, slathering your feet with the lotion and just sitting there. A Carmel Apple helps the relaxation process but is not necessary 😉
[jnenstn] (score 38, diepte 0) I am an immensely large human (6'6", 350+ lbs) and find that socks make the bigger difference on how much my feet hurt at the end of the day. I wear either Vans if I'm going a day or two or well cushioned Hokas if I'm going for a few days. My feet always hurt a bit, but nothing too bad by any means. Wearing a quality sock is the way. Something like a merino wool (non winter) sock is heaven. Bombas is my go to.
[jnenx5h] (score 36, diepte 0) Crocs….yes I said it.

Most comfortable and versatile shoe I’ve ever worn to Disneyland.
[jnen49b] (score 34, diepte 0) How has no one mentioned icing the dogs?!? 

Absolutely the most important thing, go back to the hotel, ice the feet for 30 minutes. Wake up the next morning good to go. 

Also insole inserts.
[jnf53ir] (score 32, diepte 0) If you're feet DON'T hurt at the end of the day, you aren't doing Disney right, lol.
[jnf6rpy] (score 32, diepte 0) I’m a mail carrier, that’s how I prepare
[jnf6y75] (score 29, diepte 2) Walgreens is like a block away....
[jnfah4z] (score 28, diepte 2) “Only two things come from Texas, haha!”
[jnfz4w5] (score 26, diepte 3) This. I’ve done a lot of standing in the park as a guest and former CM and that’s what hurts your feet.
[jngbm0g] (score 22, diepte 1) I take a couple of long pairs and wear them in the room in the evening after showering. Total game changer.
[jnfhzm6] (score 17, diepte 1) How much walking do you do in normal life? If you walk enough generally, you can go all day at Disney without your feet hurting. I recently spent all day at Disneyland and DisneySea (two days in a row) and was fine. But if I have gone a while without as much walking and suddenly spend all day walking, my feet will hurt.
[jnen8rl] (score 17, diepte 0) Lots of sitting down!!! Finding the right shoe is very important.
[jnenhc4] (score 17, diepte 0) Yeah, I’m very active and in pretty good shape, but my legs ache after a long park day. I wear running shoes and compression running socks, but it’s not enough. My last couple trips (I go 2-3 days at a time every other month or so), I proactively take Advil - after I eat breakfast, then again every six hours. That does the trick. I generally do not ever take meds unless I MUST, but this is what has solved the problem for me. Otherwise I get what feels like shin splints from my ankles up my shins, and my hips feel like they’re about to implode. 

I’m 46. In my 30s we’d go to WDW for a week at a time, and I’d wear flip flops… and I was really overweight and never exercised back then and I didn’t feel like it was strenuous then! It’s really weird, but I guess that’s what aging does to you. 🤷🏻‍♀️
[jnfa8eo] (score 16, diepte 1) The prep and broken in shoes make a huge difference for me.

I usually walk for exercise but I really ramp it up about a month before Disney then the week before Disney I slow things down a little bit so I'm nice and fresh. I also make my kids join me for some of my Disneyland training.
[jneulz2] (score 15, diepte 1) YUP. Best shoes ever. I call them my cloud shoes. Plus they’re cute too!
[jneqw8x] (score 15, diepte 1) This is what I do as well. The added benefit is it also gives you an alternate if your shoes end up wet due to a water attraction or weather. Or just wear the flip flops for that water ride.
[jnewx1z] (score 14, diepte 1) I highly agree with shoe insoles.   You need to find the right ones.  I have feet trouble and now I don't.
[jnfixyv] (score 13, diepte 3) There is a target just down the street on harbor too.
[jneo4hm] (score 13, diepte 0) My husband has Hokas (he wears them for work) and he absolutely adores them. He said his feet didnt hurt at all at the end of the days and we were there for 5 days. A cheaper alternative (which have become his off work shoes) is new balance fresh foam. They're a thick sole just like Hokas.
[jneq95b] (score 13, diepte 0) Advil to keep the feet swelling down. A change of socks (or two) can make a huge difference. Walking around with socks moist from a ride or sweat can really hurt your feet after a while, and a new pair really freshens up your feet regardless
[jnes1ss] (score 12, diepte 1) I do the same. I wear a combo of Vans, Chacos and running shoes to the parks and I’m usually good doing this nightly.
[jner4av] (score 12, diepte 0) As someone who has healed from plantar fasciitis fairly recently, I recently went to the park from rope drop to close wearing a pair of Hokas and I had 0 pain the day of or the next day!
[jnevxg7] (score 12, diepte 0) I bought some Hoka walking shoes. I used to wear Nikes to the park and my feet would be throbbing by the end of the day. With my Hokas I can walk all day and my feet never get tired.
[jnf44re] (score 12, diepte 1) Not true (the fastest marathons ever run were in Nikes, the Nike Pegasus has been a staple training shoe for years, I know ultrarunners who swear by the Wildhorse), but it is worth noting that *running* shoes are not really the best shoes for miles and miles of *walking*. Running shoes are designed for pushing off of the ground and absorbing the high impact when you land. Walking is mechanically very different.

The style of the shoe matters more than the brand. (Though I guess all Hokas are similar in that they have a ton of cushion, as far as I know).

I personally do best in minimalist shoes like Lems Primals, but your mileage may vary. Honestly,  the best thing you can do to be more comfortable walking in Disneyland is to walk more every day.
[jnelct5] (score 11, diepte 1) I just can’t wear idiot future shoes.
[jnf7vgf] (score 11, diepte 1) Or you can get straight-up Dr. Scholl’s shoes! I have numerous pairs, in flats, booties, and sneaker styles. I have never had to break them in and no pain after a full day in the parks!
[jngb4ik] (score 11, diepte 3) Normally I will go for a walk that is 2-3 miles, and I'll do that 3-4 days a week. I also might go on a weekend hike 4-8 miles. It varies.

Leading up to Disney I will double or triple the amount I walk. Depending on my time, etc. Two weeks before I'll try to do a few days with 8-9 mile walks more if I can swing it. The week before leaving I'll drop down close to my normal schedule, and won't walk at all (well, no long walks) a couple days before arriving.

At Disney I will walk a lot. I usually average 11-12 miles. I think the furthest I've gone is probably around 14-16 miles in a day. I'm always the one to do bathroom runs for the kids; trip to drop something off back in the room; etc. so I always get more distance than my wife and kids.

One thing to note is that the Disney walking includes every step I take during the day. At home I'll go out and just walk for 2-3 hours straight just to get the miles in. In Disney there are lots of breaks.
[jnfhry6] (score 11, diepte 1) Came here for this answer. Disneyland is the only place I wear my crocs. My feet never hurt.
[jnfh3ub] (score 10, diepte 3) that's where i bought mine last year when, after several days of Star Wars Celebration and the parks, my feet couldn't take it any more.  best $9 i spent that trip (and luckily my hotel was just a stone's throw from Walgreens)
[jnf8vyi] (score 10, diepte 1) YES! A lacrosse ball and toe spacers to really stretch everything out haha
[jnepwkx] (score 10, diepte 0) I am a sandals person. Unless it’s cold out I prefer sandals for theme parks the vast majority of the time. I just find the ones that are comfortable and work for me: 

- Sanuk Yoga Mat sandals
- Tevas
- Chacos
- Birkenstocks 

And if it’s a multi-day trip I’ll rotate them. All are broken in, most are waterproof so I never have to switch for water rides (exception being Birkenstocks unless I’m wearing the EVA sandals). If I know I’m gonna be in the parks *allllll* day long, these are usually what I’ll reach for. They’re also usually my Disney World shoes, my Knotts shoes, my Universal shoes, etc. 

And granted if I do wear sneakers I have adidas sambas, some chunky new balance kinda dad lookin shoes, some Reebok club c, Iand I have worn converse all day without regretting it.

BUT, I walk a lot on the reg so a day at Disneyland rarely makes me sore in general.
[jng2wwf] (score 10, diepte 1) THIS!!! They help so much.
[jneve7w] (score 10, diepte 0) Massage gun on the soles of your feet at the end of the day.
[jnga33a] (score 9, diepte 2) Mickey Mouse? Try my mom when I was a kid crying my feet hurt. 
"Stop crying. This is the happiest place on earth!"
Good times...
[jnekwzc] (score 9, diepte 0) Crocs 🫣
[jnflcev] (score 9, diepte 1) Why is this not the top answer?!. Crocs sell way more than just clogs too. I have a pair of flops, a pair of loafers and a few pairs of the clogs and they're all the most comfortable shoes I own.
[jnepeva] (score 9, diepte 0) I wore Vans to the parks but I feel I must confess they were the comfycush variety. My old feet could not hang with the traditional.
[jngogmd] (score 9, diepte 1) You and hospital nurses would be who I’d want shoe recommendations from when it comes to spending all day on your feet
[jnfaxpl] (score 9, diepte 0) Teva’s are my jam, I could walk all day in them.
[jnfisv0] (score 8, diepte 2) I usually walk 3 to 3.5 miles daily. But add another couple miles just being on my feet.
[jnf7p6g] (score 8, diepte 2) They would cost 3 times what they would outside the park please don't give them anymore ideas
[jnerm6c] (score 8, diepte 0) Different muscles are used for different things. The muscles you use for bicep curls are not the same muscles you use for leg curls. And the muscles you use for leg curls are not the same muscles you use for standing all day. So being in good shape doesn't necessarily mean that you have built up the right muscles required for standing all day.

I work at a desk all day, so I'm mostly sitting. But I bought a standing desk so that I can practice standing all day in the weeks leading up to going to the parks.

Also, Dr.  Scholl's shoe insoles are a must.
[jnf0k3w] (score 8, diepte 0) Nike is style over performance on running shoes. Get some from a real brand like HOKA, Brooks, ASICS, or Saucony
[jnfzulg] (score 8, diepte 1) Now that is a physically demanding job.  Thank you!
[jnffsjl] (score 7, diepte 3) A long block, after walking out to the street, but yes, there is a Walgreens and CVS right across the street from each other.
[jnff4he] (score 7, diepte 1) This is the way. I have a little medicine kit of just foot care. I workout for a living, and even my dogs get to howling at the parks. Walking all day on cement plus salty foods is a recipe for swollen feet. I pack Ibuprofen, corn pads, kinesiology tape, the works. I bring those yoga socks that spread your toes out to sleep in, and keep my feet elevated on a pillow. My bunion is appreciative 😂
[jnfjm9g] (score 7, diepte 1) I thought I would see this as a top comment! Icing the pups at the end of the day after wearing inserts resets them and it’s so easy to grab a bucket or two of ice from the hotel and ask for extra ice bucket bags and put your feet and ice in there.
[jnenjad] (score 7, diepte 0) SKETCHERS!!!! and don't wear thick socks. And vitamins B12
[jnesakl] (score 7, diepte 0) I always bring more than one pair of shoes. Switching each day helps a lot. Also, every chance I get, I lay on my back with my butt against the wall and legs up, resting on the wall. It helps drain blood from your feet and reduce swelling. I sometimes do it in long lines.
[jngy7qz] (score 7, diepte 1) What kind do you like? There are so many of them and I don't know which are legit.
[jneyp5w] (score 7, diepte 0) Go to a running store and get fitted for shoes even though you may not run. Life changing experience
[jngjljv] (score 7, diepte 0) Alcohol
[jnem9fn] (score 6, diepte 2) I was so upset when I tried on my first pair! Finally convinced my husband to try after seeing how completely fine I am after a Disney day. He, too, is now pissed. But wears Crocs at Disney and has no pain!
[jngfotv] (score 6, diepte 3) Yup, I managed at bars and cafes, and would end up behind the cash register when we were short staffed. Standing in one place usually sucks worse than walking, but Dr. Scholl’s shoes never disappoints. I work at a desk now, but I still swear by them when I do weekly treks around the city or when I go to theme parks.
[jnet25h] (score 6, diepte 1) This and good socks. I always buy new nike socks. Swap socks part way through the day and I start long walks a couple weeks before to prep them. I have several shoes that go to the park. I choose 2, one to wear in and one in my bag with the socks. They go into the locker. If weather is questionable I have back up wet weather shoes in the car.
[jnerc0h] (score 6, diepte 0) I literally wore converses and I was there for like 12 hours. Definitely sore but nothing I'm not used too. It's probably cuz we are a glutton for punishment lol
[jnf8tse] (score 6, diepte 1) I bought Hoka’s for my trips to Disney! Definitely helped my legs and feet last longer before being in pain…but still hurt after 12+ hours of walking for 2 days lol
[jnfi2rr] (score 5, diepte 4) Yeah my hotel was right near that corner so I know the area a little. Hopefully OP sees this.
[jnfady9] (score 5, diepte 2) Yeah, I wore Dr. Scholl’s shoes when I worked retail and as a baker, lifting and moving lots of heavy things, etc. They do the job.
[jnfb9jf] (score 5, diepte 1) I’ve had no pain wearing Adidas Ultraboost. I’m a healthy 21yo athlete but I had shin splints in the past and they don’t flare up at all. Even my dad who’s broken his ankle and kneecap before had no issues with Ultraboosts.
[jnfe2tz] (score 5, diepte 1) I bought these SPECIFICALLY for Disneyland and only wear them when I go there. These shoes are life savers.
[jnh2ccg] (score 5, diepte 2) As someone whose feet get absolutely murdered by Vans, I could never even contemplate wearing them to Disneyland. More power to you
[jnfk8ny] (score 5, diepte 1) My family hates crocs but I wear either crocs, good inserts, or the walking converse but when it comes to the crocs I joke at the end of the day, “raise your hand if your feet hurt!”. Everyone raises their hands but me and they all get mad.
I finally got my husband on the crocs game so he can wear them on our next trip, he hates that he loves them 😂
[jnfmehh] (score 5, diepte 2) Socks for normal walking and take them off for water rides.
[jner1h0] (score 5, diepte 0) Crocs!!!
[jnexr1f] (score 5, diepte 0) Aspercream and good insoles.
(551 reacties met lagere score weggelaten)

=== THREAD 1xlwo9b ===
SUBREDDIT: r/solotravel
DATUM: 2026-11-02  SCORE: 385  REACTIES: 290
TITEL: Quitting everything at 25 to solo travel in search of a sense of purpose – is it a good idea?
POST (source_id=post):
I'm 25 and seriously considering packing up and solo travelling for a full year because, honestly, I feel like I'm searching for something more to life. I've recently quit my full-time job for personal reasons and picked up casual work because I feel like I need a complete change of direction. After two years of working full-time, I've realised that the traditional working life isn't necessarily something that suits me, at least not at this stage of my life. I've also had a really difficult time with friendships throughout my life. I've often felt left out, forgotten about or eventually cut off by people I genuinely thought would be in my life forever. I look around and see everyone else building friendships, relationships and memories, and sometimes it feels like I'm just watching life pass me by. I always imagined that by 25 I'd have people around me who genuinely cared, a close circle of friends and a sense of belonging. Instead, I feel quite disconnected and, at times, like I'm just existing rather than actually living.

Career-wise, I actually am happy with what I've achieved. After years of unemployment, struggling to get my foot in the door and honestly feeling pretty unemployable, finally securing a full-time job was something I never took for granted. I worked hard, stuck it out for two years and managed to save around $100k USD, which I'm incredibly grateful for. But looking back, I feel like I've sacrificed so much of my time and personal life for it. I've missed out on friendships, made sacrifices that I can't get that time back for, and experienced a lot of disappointment and pain along the way. And for what? I feel like I've given so much of myself to work, only to end up feeling alone and disconnected anyway. I'm proud of what I've accomplished, but I also feel like I've reached a point where I don't want my entire twenties to revolve around working and saving money. Part of me just wants to stop putting my life on hold and actually experience the world.

I think solo travelling appeals to me because I want to feel like I'm actually living again. I want to experience new things, meet different people, form genuine connections, make memories and hopefully discover something about myself along the way. I want to have stories to tell and experiences to look back on, rather than feeling like I've spent my twenties just working and watching everyone else live their lives. Maybe I'm looking for a sense of purpose, maybe a fresh start, or maybe I just need to get out of the environment I've been in for so long. Has anyone travelled solo in their mid-20s while feeling a little lost or unsure of what they want from life? Did it help you find a sense of direction or give you a different perspective? I'd really appreciate hearing honest experiences, particularly from people who felt like they needed more out of life.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[19s16ck27xvab] (score 527, diepte 0) Spoiler alert: you won’t find “it”, because “it” doesn’t exist. But if you can swing it financially, go for it - you’ll have fun. It’s always better to travel when you’re young and able.
[19s18sexlglut] (score 472, diepte 0) I’m not sure what makes anyone believe that quitting a job is the way to find themselves. What it usually creates is a new kind of anxiety: no income, no direction, and a deeper sense of isolation.

I’m all for exploring and traveling. But wherever you go, there you are. A new backdrop doesn’t change the person standing in front of it.

Do the hard things now, while you’re young. This is the time to build a career, when you can afford to take risks and change course. Switch jobs until you land on one that brings you joy. A beach won’t make your passion appear. Purpose rarely arrives in a moment of stillness. It shows up when you’re in the thick of things, adjusting in real time and pushing forward on the days you have nothing left.

Wishing you great success.
[19s1c1gfi9n6r] (score 185, diepte 1) They will still be young in a year’s time. Seeing the world and exposing yourself to different cultures, people and ideas is also a way to be inspired and find purpose. Better to take a year away at 25 while they have the time, health and money than to miss the opportunity due to responsibilities and commitments taking over as they get older.
[19s18uhvz0uxt] (score 99, diepte 0) You say that you feel "alone and disconnected" and that you want to "form genuine connections." Honestly, solo travel is not going to solve these problems for you. You're going to feel just as alone and disconnected as a solo traveler, perhaps even more so if you don't have a home to go back to. You will definitely form connections with people, but they're not any more genuine than a connection you could make at home. In fact many people complain about how fleeting and ultimately superficial are the connections they make with other travelers. I'm not saying you shouldn't travel. I'm not even saying it's not possible to feel a sense of connection while solo traveling. I'm just saying you should temper your expectations from what you're going to to get out of it.
[19s1bm1neme8w] (score 96, diepte 1) Also if you go travelling and find you've discovered that "it" is travel itself, this is a trap!!
[19s1e25s1ufmr] (score 87, diepte 2) You make a fair point, and I agree that travel can broaden you. A planned year abroad at 25, with savings and a way back in, is a very different thing from what I was describing: quitting a job out of restlessness and hoping a new place will supply the answer.

My concern is about *why* someone goes. Traveling toward something, like curiosity, a skill, or an experience, can be life-changing. Traveling away from something, like a job that feels hard or a sense of being lost, tends to bring the same questions along for the ride. Inspiration can come from anywhere, but direction usually gets built through the daily work of trying things, failing, and adjusting.

You’re right that the window for travel closes as life fills up. But the early years of a career are a window too, and they compound. Both matter. I’d just say go with a plan and a purpose, rather than as a search for yourself.
[19s15o44jvau9] (score 83, diepte 0) Me, I went when I was 25 - wasn't happy with many aspects of my life - work, friends, dating, hobbies, health, addictions. I only went for 2.5 months to Central America but it blew my mind. It set me off on a wild path. I am 39 now, back in the corporate world for a year now in my original country. I am older, wiser, spent almost 10 years living abroad, have had a myriad of jobs, experiences and adventures to last a lifetime.

I'd do it again if I could. The alternative is just working in the corporate world and developing my career more, getting a mortgage, living in the evenings/weekends, going on holidays etc.
[19s15r2t6i080] (score 67, diepte 0) 100% do it, you won’t regret it.   
I took off 9 months last year to to US, Canada, Africa, Middle East & South America. Time of my life.
[19s22ujsjkbs3] (score 49, diepte 0) Dude you gotta remember 99.9% of people on reddit are the most uninspiring, pathetic people humanity burps up. Most of these comments are going to tell you to keep being miserable because guess what misery likes the most...Most of these commenters have never even tried to live life to the fullest or take a risk. I'm your same age and about to quit a high paying job to do the same thing. On my deathbed I'm likely not going to be wishing I heeded the advice of FadingRockStar or some other internet incel. Don't let people's envy and lack of fulfillment in their own lives get in the way of yours.

Climate change. AI. Wealth inequality. Pandemics. Wars. American democracy is over. Shit can hit the fan at any moment. You're only alive once and it goes by fast. Might as well live before the Epstein monsters send drones at us. All in all, don't listen to the advice of anyone. Do you and don't look back. It's your life and your decision.
[19s3bgd98wx40] (score 45, diepte 0) I did exactly that for 10 months and let me tell you - whatever you think you’ll find out there, is already inside you.

I backpacked across Europe and Asia and imma keep it real - if you can take serious time to go travel you absolutely should.

But if you’re running away to try and find something, there’s a good chance you won’t. 

Taking space and time for yourself is important. Traveling and seeing the world is important. Getting away from the noise is jmportant.

But wherever you go, that’s where you are. It’s still you, and whatever you have inside you, everywhere, all the time.

You don’t NEED to leave to find it. It can help, but it’s not out there.
[19s1nb0cdk9sz] (score 31, diepte 3) Well said, travel to something, not away from something. Applies for most things in life. 🙌🏽
[19s1srxvkw0pu] (score 31, diepte 2) I completely agree. I am one of those people that needed to "escape" my corporate life in London at 24. I smoked cigarettes, smoked weed in the evening with my housemate, hardly exercised, was miserable at work, had no romantic life and didn't understand why, had friends but didn't understand what was wrong in my life. So 
turning my life upside-down for 2.5 months of solo travel was incredible emotionally and spiritually: the freedom, the adventure, the risks, the onslaught of new experiences - learning Spanish, learning salsa, doing home stay in Guatemala, Linkin up witn randomers and having long conversations with people from all walks of life who also decided to travel, scuba diving, spending a lot of time alone on public transport and wondering streets alone - all of these were so eye-opening, so different to what I thought was possible, so different to my own habits, so removed from all that I can experience working in an office in London and going back to the same home every day. 

My problems were not solved, of course. But little by little, over years they improved. But my heart and my soul were awakened, and I realized that other lifestyles were possible. I think this is THE major epinaphny I had - seeing with my own eyes the potential, and physically meeting others who lived different to what I everyone else was doing back home,.and having the time to sit and chat to them - really it was seeing other examples of people doing things differently. It gave me courage to try my own way. 

I think we all ought to chase random dreams we have (but staying financially responsible) and also put ourselves in situations so different to the norm just for the sake of exposure, to see the possibilities we have. 

I wrote in another comment here what jobs I did and where I spent my time.
[19s1nve7i52u8] (score 27, diepte 2) Lol why?
It's like an addictive expensive and time-consuming hobby
[19s1a9spxwp0h] (score 27, diepte 0) This isn't the sub to ask this question, people here are going to reflexively say yes without considering the details. Solo traveling especially for a year isn't going to solve any of the issues you mentioned. You sound like you need community and a strong foundation, solo travel is straight up the opposite of that. I do think you should take a long vacation to clear your head though, but a year is just kicking the can down the road and likely harmful to your professional life.
[19s1jd80gmsv8] (score 25, diepte 1) I think you’re right in the sense that this is probably the reality for most people and I agree that changing surroundings doesn’t inherently resolve whatever internal struggles or uncertainty you’re carrying, but it very well can for a certain type of person. However I think there’s a distinction to be made between people who are “running away” and people who are genuinely fulfilled by the prospect of simply picking up and leaving. Believe it or not there are people for whom the freedom, uncertainty, and experience of being somewhere unfamiliar can be incredibly emotionally and spiritually fulfilling, and bring out aspects of the self that were previously suppressed, and this is true whether they are running or seeking. A new environment IS capable of doing that for some people. It’s simply not in alignment with everyones path to find purpose or direction through building a career or pushing through the conventional milestones we’re told will eventually bring us fulfillment. That shoe does not fit everyone, which is wheres individual differences come into play. Nobody can determine what kind of person someone is, what they need to feel fulfilled, or what will give their life meaning aside from said person themselves. What many perceive as an irresponsible escape can genuine be the most enriching decision another person ever makes.
[19s18ir2ditno] (score 24, diepte 2) At first I had a few wild years, and then I found one profession that allowed me to work remotely and move around a bit.  
In chronological order: freelance Google ads campaigns for 2 small businesses in Guatemala & Honduras, Google ads/digital marketing for a Spanish language school (for foreigners) in Guatemala for 6 months, 2.5 months marijuana trimming in California, tour guide for G Adventures in Central America for 6 months, bookshop in Guatemala for 2 months, freelance English teaching in Guatemala for 5 months, marijuana trimming again in California for a month. Also in between trips I had a few months of contract digital marketing work in London as well as some customer service tech support for Lenovo lol.  
  
Then I became a freelance online English teacher and spent almost a decade doing that while living in Guatemala (5 years), working remotely for a few months in Brazil, Kenya, Tanzania, Israel, and then I spent 1.5 years in Rwanda, plus a couple of years of visiting family in England and still working remotely.
[19s1mgcncxqck] (score 24, diepte 1) I agree.. As much as I love solo travelling.. It got romanticized so much to the point that it is seen as a fix to everyone's frustration. It is not. Personally I've became a happier person when I realized I can still find joy and love in my everyday life - even when i am not traveling.

As much as I want OP to experience how great solo travel is... I think it would be better to start small.. Instead of quitting your job - how about do an extended vacation like a couple of weeks or even a month. Learn from that while still making money, then use that knowledge gained to plan a longer trips. 

I understand burnout happens and we want a change in scenery, but reality is you have so many years ahead of you and you need financial stability so you can keep doing these solo trips in the years ahead. $100k saved seems a lot (congrats OP) but in these times a single emergency could take out most of it. You don't want to approach your 30's with very minimal saved and invested. That puts so much stress in a person - unfortunately i've seen it too many times with my peers.

I was once just like you, but in my case i found out I can still solo travel extensively while keeping my day job.
[19s1t04kn4xwj] (score 21, diepte 3) As the saying goes, wherever you go, there you are.
[19s1of2ommf1f] (score 18, diepte 0) You will just carry the weather with you.  If you are not happy where you are you still won't be happy in a different location.
[19s1644rzrdep] (score 15, diepte 0) To be honest, travelling is one of the best things you can ever do for so many reasons. 

But, with that much saved, maybe it's better to put a bunch of it aside or invested into something solid so you can get the full experience while travelling by leaving far far cheaper. Otherwise you might just be spending money living like a tourist in hotels and not to say that there's anything wrong with that but if you're craving more connection, novelty and spontaneity, I've personally found that budget travelling is an awesome way to do that.

Anyway, here's a few quick tips I've picked up after leaving the UK at 27 with about 5k saved 

1. You're never too young or old to travel   
2. Stay in the moment and get off your phone as much as you can. Physical media like cameras, an old game boy, a damn frisbee, can all be way more fun that our expensive rectangles and are good conversation or activity starters.   
3. If you go to the capital cities go early in the morning to avoid the crowds if you want any chance of a good photo.   
4. Check out the not so popular places too, the second or third biggest cities are great in many countries.   
5. Facebook Groups are underrated - join a bunch and make some friends in places  
6. If you're american, you might not already know that most of the world uses whatsapp so get used to using that every day, it's great.   
7. Don't be a dickhead.   
8. Be tidy, always. But especially in shared spaces. I mean being tidy is definitely a good thing for your own sake anyway  
9. Don't be so focused on an end result and instead just focus on enjoying and accepting what comes.   
10. Don't be a dickhead. 

Travelling is fucking amazing, do it!
[19s1cbda5b543] (score 13, diepte 0) Do whatever fuck you want, do you really take people’s opinion here seriously? Tomorrow you will forget 99% things that are written here.

You feel it you do it, you don’t feel it you don’t do it.  
Peace & Love
[19s1entlhocrm] (score 13, diepte 0) Lol the finding yourself and purpose is such a cliché.

Just go, have fun. You'll probably gain a bit of confidence and have the feeling that you found yourself. In the end you're just the same person but in a different place
(249 reacties met lagere score weggelaten)

=== THREAD 17wh9qx ===
SUBREDDIT: r/hiking
DATUM: 2023-11-16  SCORE: 148  REACTIES: 256
TITEL: Boots fit well except pinkie toe is feeling squished… the size up feels a little too big but my pinkie toe doesn’t hurt. Is it worth stretching the boots or just getting the size up even if they feel more like clown shoes?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k9h4q0u] (score 1152, diepte 0) possibly this shoe is not for you.  You need one with a wider toe box?
[k9h5hi7] (score 435, diepte 0) Imagine hiking 20 miles with your pinky toe jammed into your boot. Find something wider that fits comfortably
[k9i5ngy] (score 315, diepte 1) Exactly this, buy a wide size or a brand that fits wider.  I like Merrell or Keens for my wide feet.
[k9h5jxn] (score 169, diepte 0) See if the boot comes in a "wide" size. Otherwise, you may to find a different boot.

I've never worn "wide" sizes in my life, but went to REI a few days ago for new boots and when they measured my feet with my thick hiking socks on, turns out wide was exactly what I needed.
[k9i8nux] (score 85, diepte 1) Altras have wide toe boxes and are fantastic hiking shoes. They are very forgiving to break in too (just another option for OP)
[k9ha1ke] (score 68, diepte 2) Kia ora, I’m nervous about getting boots you know are too small. Also those socks looks pretty thin. Finally the fact that the tramp is only two weeks away is not enough time to break them in properly. So, knowing stuff is expensive here, what I would do is get a pair that fits well in the heel and that can lace up really well so you have less wiggle room. Your feet and hands will swell SIGNIFICANTLY if you are tramping, so it’s great to have a bit of extra room. I really wish I had bought a size up as of course I had not just walked 10km the day I tried on boots. Now I get callouses when I walk and they can be painful. Also I would invest in silk liners and socks with much more cushion to fill in the boot for a secure fit. Then at lunch you can swap into lighter socks, when you’re warmer and your feet have swollen, since it’s still a bit chilly in the mornings depending on where you are. Be sure to bring blister protection and wool to protect your feet and have fun!
[k9h8zsd] (score 68, diepte 0) This means the shoe does not fit well.
[k9hg2nc] (score 54, diepte 1) Did this on one of my first long hikes about 35km on day one. It hurt a bit, but I kept going. My pinky toe looked like a mini black pudding. I couldn't walk the next day. So, I had to call off day 2. 

Safe to say, I've learnt a lot about how to properly size my boots since then.
[k9hbcoa] (score 52, diepte 0) You need different boots.
[k9hdhmw] (score 34, diepte 0) Sounds like these particular boots aren't a good fit (in either side)
Try several different brands, styles etc.
[k9jde13] (score 25, diepte 3) It’s Altra’s or bust for me, even the wide sizes in most other brands are not wide enough for my feet
[k9i8u1n] (score 25, diepte 2) I love my Altras! Perfect for my Fred Flintstone feet.
[k9hglp7] (score 24, diepte 0) Get a wider toe box or go up a size. You can always wear 2 pairs of socks if needs be. Also, your feet will likely swell a bit with long days of hiking, so those shoes will be even tighter at the end of the day. 

It's a mistake I will not make again. It cost me a $250 pair of boots & most of the skin from my pinky toe.
[k9ilt70] (score 22, diepte 2) Love me a Merrell though currently eyeing Keens as well to replace my now-too-large Moabs. 

My feet aren’t too wide and my Moabs were actually TOO roomy for some time (and jamming my toes going downhill), but that was more a sizing thing. My pinky toe kind of hooks a bit under the adjacent one of shoes are too tight, which leads to pain. My usual stopgap is wrapping a band aid or similar around it. Feels weird at first but keeps things spaced and less crushed.
[k9hjw55] (score 21, diepte 2) I’ve used shoe stretchers on my Salomon hiking boots. My take was that while they did widen the toe box enough to be much more comfortable I developed blisters on my pinky toes about 60-70miles into my hike. I also noticed much more discomfort and swelling on my pinky toes at the end of the day. My conclusion was that I need different boots. I did however use cheap shoe stretchers from Amazon, one of which broke trying to widen the tough material. I would suggest not buying the cheapest tool if you went that route. 
In the past I’ve used Altra mid-ankle lone peaks, and never once had a blister through hundreds of miles. Downfall was that the waterproof material lost integrity after a little over 100miles. Those get expensive to replace. Which brings me back to wanting to stretch the 3 pairs of Salomon I got on clearance 😂
[k9iya6x] (score 17, diepte 3) My feet are between regular and wide, so we're in the same boat. I've only ever had Keens because I love them and they're so comfortable for me. Absolutely no foot squishing but they're not clown shoes.
[k9h7z2p] (score 17, diepte 1) If your toes are squished, aside from possibly getting blisters, you may also lose toe nails, especially if you are off on a long tramp.

As others have recommended, you need to look at wide fit shoes, or just shoes which are simply made wider. You didn't mention Merell, who also have some wide fit boots/shoes. I am not sure where you are based, but if interested you could check out the Merell nz website for stockists to see if any near you, assuming that is where you are based off the language used.

I find wearing shoes "too big" leads me to tripping over steps a lot. Maybe I am just clumsy though 😀
[k9j0rww] (score 17, diepte 2) https://cdn.runrepeat.com/wp-content/uploads/2015/05/shoelacing_infographic_12_techniques.jpg

Try the Wide Forefoot lacing in this diagram. I use it in combination with the heel slipping lacing for my duck feet and it helps a lot.
[k9hkwij] (score 16, diepte 3) You heard the Hand. The King's too fat for his shoes. Go find the shoe stretcher... now!
[k9hwm8j] (score 16, diepte 0) I personally prefer “barefoot”/ minimalist/ zero drop hiking boots for this reason (vivobarefoot and zero shoes are well known, Merrill also has some) . They have wide toe boxes. And I’m personally an advocate for the other benefits of these kinds of shoes. 

They do take time to break in and adjust too (my core and back needed a lot of strengthening). So it wouldn’t be a solution for you right now, but I highly recommend looking into them!
[k9i9ubf] (score 15, diepte 1) Yes, Altra, Keen, Merrell, and I think that Keen and Maybe Altra can even provide wide sizes. Pretty much the only thing I’ll wear, and my hiking boots are all Keen Targhee 2.
[k9he9zy] (score 15, diepte 0) Depending on where you are (I assume NZ or Aus?) I would find somewhere that seels wider shoes. I have wide feet, and the brands I have used that work are Altra (boots or shoes) and Topo (shoes only). Hoka also have some good wide-footed options, and Nnormal is a brand of trail runners that is new but has a bent towards sustainability
[k9hklz6] (score 14, diepte 3) If you go this route stretch the boot much wider than you would assume normally. I also soaked my boots in water before hand to help soften the material and let them dry around the stretching tool. The soaking part was a suggestion from an Army buddy that use to stretch his boots by wearing them in the shower which softened the material then he would keep them on and let them dry around his foot through the day. 
Final pro-tip is to not lace up the bottom couple loops. I start mine half way up.
[k9i6f5c] (score 13, diepte 1) I also have never worn “wide” shoes either, but when I first tried on boots at REI I found I wanted a wide toe box and high arch so I got a pair of Oboz. Even after breaking them in I got terrible blisters on my toes, so I went back to REI in search of something even wider.

I tried all of the recommended brands and found that while brands like Altra and Hoka have wide toe boxes that they curve inward near the toes in a way that my feet don’t so my toes still ended up squished. I ended up buying Merrell Moabs in wide. I was shocked because in any other shoes I don’t (tennis shoes, dress shoes, etc.) wear a wide, but the wide Merrells work well as long as I    keep the laces tight everywhere except by my toes
[k9i9hpx] (score 12, diepte 3) I love mine too! They are great for all feet and just allow your toes to spread but keep your heel locked in.
[k9ib6wb] (score 12, diepte 2) I was going to recommend altras. I tried using them for a while but I have a high arch and little feet so they were all wrong for me but the toe box is perfect for someone who needs that extra space! I have friends who have wider/flatter feet who swear by altras
[k9ija8v] (score 12, diepte 2) Did the same, and lost the toenail a couple months later. Replaced the boots with Altras. Lesson learned
[k9ip0y3] (score 11, diepte 3) Have you looked at Topo Athletic shoes? Similar super wide toe box as Altras, but they actually have support. They are also not zero drop, but do have a pretty minimal drop, and I find them to be more durable than Altras.
[k9h6zjb] (score 11, diepte 0) Where are you located? The Kathmandu socks suggest nz or Australia. If nz try out hunting and fishing. I have a pair of deer stalking boots for my fan shaped feet. They're great for super uneven terrain. They've survived the worst terrain, from skree slopes to mud bogs and river crossings and still feel new.  Whenever I'm not in the rough stuff and have a clearly defined track I honestly just wear under armour trainers. I've done a few hikes in them and they've never had a problem over wet rocks and such and the only times I've slipped I would have slipped regardless.
[k9inx6v] (score 10, diepte 2) Don’t forget Topo athletic :)
[k9ham1m] (score 9, diepte 0) Get difrent boots that fit the shape of your foot to avoid a lifetime of painful impacted toes
[k9jhqv2] (score 7, diepte 4) OMG I LOVE my Keen hiking shoes! At first, the bone near my pinky toe was hurting, but that has since gone. They are the most comfy shoes ever! I got my Daughter the same one too. She uses orthopaedic insoles in hers and they work out well. We’re going for the boots next. Youngest Daughter has the toddler sandals.
[k9iguvp] (score 7, diepte 2) Flippin love Altras. I’ve had 2 pairs that helped me finish the 48, 4ks in NH. Comfortable as F.
[k9jgdl7] (score 6, diepte 3) I have had the same pair of keens hiking boots for 5 years, the only shoes I've ever owned that lasted more than 1.5 yrs.
[k9k201n] (score 6, diepte 4) They also are much higher quality than Altras.
[k9j9c4k] (score 6, diepte 3) Sadly, we don't have REI  in Australia or New Zealand.
[k9hos6c] (score 6, diepte 0) You know what they say: If the shoe doesn't fit, don't wear it.
[k9hsda5] (score 6, diepte 1) Imagine that! A hiking sub, and people ask about shoes and boots. The least important aspect of hiking.
[k9j5lfa] (score 5, diepte 2) ^This! 
Wide boots for the win!
[k9jgsjd] (score 5, diepte 3) My feet are too wide for Merrils. Extra commented I've had the same pair of keen hiking boots for over 5 years. They're still 100% waterproof. I highly recommend them!
[k9j6t2s] (score 5, diepte 3) Ah yes - Topo too!!
[k9hjydl] (score 5, diepte 1) This right here.
[k9honk2] (score 5, diepte 0) I would go with a totally different, wider, shoes!! I have wideass feet and alta lonepeaks have seriously changed my liiiife
[k9hw1e0] (score 5, diepte 0) Your feet will swell when hiking so too tight shoes will most likely give you more problems than just with the pinky toe.
[k9hxio4] (score 5, diepte 0) Get a boot brand that offers a Wide option.  You don’t need longer, you need wider, and a boot stretcher isn’t going to cut it, IMO.
[k9hygiw] (score 5, diepte 0) I wish shoes didn’t have such a pointed toe box. Feels so counterintuitive to squish our toes into a shape they don’t belong in. Pointy and aimed inwards…wack.
[k9j8s4j] (score 4, diepte 2 OP) FYI these are merrells
[k9jylet] (score 4, diepte 4) My partner is obsessed with zero drop, wide footbed shoes and also goes through a lot of running shoes. His favourite shoes by far are Altra, road and trail.
[k9kdt4n] (score 4, diepte 4) I love my Altras. If you ever want a more flexible / barefoot style Xero shoes are amazing.
[k9jhn4o] (score 4, diepte 2) +1 for Keens if you need a wide toe box.
[k9hoeq7] (score 4, diepte 2) I have high in shoe and device didn’t help, lost money and time
[k9ji3uk] (score 4, diepte 1) But hiking boots are about fashion. You wouldn’t want your toes to breathe and look uncool right?
[k9hj7qg] (score 4, diepte 0) You might try going to a real shoe store, certainly measuring your feet and really getting something that truly fits your unique feet. There's something else there without going custom I'm sure that gives you the width or the toe box you need etc
[k9lgc0s] (score 3, diepte 3) I have worn through probably 20 pairs of Keen shoes. Takes a lot to get me to buy from another brand, and I got them specifically because of the wide toe box
[k9jq8gw] (score 3, diepte 3) But are they a designated wide size, or regular fit? I have wide feet and have found that only certain models of Merrell shoes and boots are available in wide. I love my wide Moab Speeds, but have the same issue as you with my pinkie toe in a regular width Moab.
[k9iox2c] (score 3, diepte 3) So what I do with some of my shoes is add in an arch support. You can customize a shoe that gives you everything that way.
[k9k4gfs] (score 3, diepte 5) I like them so much better.
[k9ixbtx] (score 3, diepte 2) Second Keen boots. I never even had to break them in.
[k9j88s2] (score 3, diepte 3) Woah, this is awesome!!!
[k9jhegv] (score 3, diepte 3) One of the workers at REI actually changed the lacing to something like that for the Oboz and it did help (just not enough)! I should try that for my Merrells though when I’m wearing really thick socks or when my feet are swollen!
[k9i3r8r] (score 3, diepte 1) I love my Topo boots, but I haven’t used them in really rough terrain.
[k9hz67l] (score 3, diepte 0) Not sure what brand you're looking at, but I've always had this problem with hiking boots (and most shoes really). My solution has been to wear Brooks waterproof trail running shoes (granted, I also usually trail run instead of hike). Brooks have the widest toebox out of what I've tried (I also get them in wide). Hope this helps!
[k9h4kyt] (score 2, diepte 0) Are other boots out of the question?
[k9jagwq] (score 2, diepte 3) Try Meindl. They're the widest of the wide brands I believe. It's what I've got for my support wide feet.
[k9ipcjo] (score 2, diepte 4) I tried that but I ended up going with a different pair that wasn’t zero drop. I can check what I have when I get home but the altras were just not right for my feet unfortunately
[k9jaec3] (score 2, diepte 2) This! Altra Lone Peaks are the only thing that fits my wide ass feet.
[k9j6qcm] (score 2, diepte 3) Unfortunately Vasque was too narrow for me - I think I might have tried a wide as well, but everyone is different.
[k9isegy] (score 2, diepte 2) Merrell also provide wide sizes on top of their already wide toe boxes
[k9j6lkm] (score 2, diepte 3) Right!? I can put in a new pair of Keen Targhee 2 (wide) and head out for five miles or whatever.
[k9hwnwz] (score 2, diepte 1) Altra.

Their durability is not good, but they're the only shoe that doesn't do exactly this to my feet.
[k9i1ae7] (score 2, diepte 1) Lowa renegades are great and they have wide sizes.
[k9i3mzx] (score 2, diepte 1) try a merrell wide fit boot.
[k9hqnqm] (score 2, diepte 0) Boots don't come in standard widths. If the length is right but the width isn't then you don't need to size up you need a different make/model. A professional fitter will be able to tell you which boots are wider fitting.
[k9hr3rm] (score 2, diepte 0) Go up 1/2 a size
[k9hv3i4] (score 2, diepte 0) Get a different brand entirely with a wider toe box in a size that fits you
[k9kjri5] (score 2, diepte 1) LOVE my barefoot hiking shoes. So comfortable from day one (but I was used to barefoot shoes). 

Just as a comment for people who aren’t familiar with barefoot shoes. The shoes themselves don’t need breaking in. Like you said, it’s the strengthening/adjusting of our own body parts and posture that can take time to relearn.
[k9kjwmf] (score 2, diepte 2) Yes! Thank you for adding this clarification! So well said!
[k9hyn3p] (score 2, diepte 0) You need a wider shoe dude. RIP pinky toes.
[k9i0j9k] (score 2, diepte 0) Sadly, 99% of shoes are not foot-shaped.
[k9i4rcp] (score 2, diepte 0) Need a wide fit boot. Going up a size may end up giving you blisters from your foot sliding around in the boot.
(190 reacties met lagere score weggelaten)

