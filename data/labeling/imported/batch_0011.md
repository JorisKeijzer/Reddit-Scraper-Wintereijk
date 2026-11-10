# Label-batch batch_0011

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
Schrijf het resultaat naar `batch_0011.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(5 threads: zq5gdd, 1aspoal, 1pwlcvj, jjg979, 19a6982).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD zq5gdd ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-12-19  SCORE: 1  REACTIES: 34
TITEL: Been having trouble finding shoes that don’t hurt my feet knees and ankles.
POST (source_id=post):
Like the post says I’m having trouble finding shoes that are not heavy and clunky and also have enough cushion to not hurt my feet on long runs.  I’m using kinvera right now unlike the weight of them but they are definitely hurting my feet.  Been struggling for a few years finding the right shoes.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j0wcwyh] (score 15, diepte 0) Don't blame the shoes, look into strength training.
[j0we161] (score 9, diepte 2) All good, but: it makes no sense that any shoe would give you some kind of pain unless there's some underlying issue you haven't mentioned yet. Either way, when it's that persistent, a shoe won't be the solution, that's for sure.

If you say „Have for a few years“ it sounds a lot like you have given it up in the meantime, though strength training should be part of every runners schedule.
[j0wh1za] (score 6, diepte 4) I'm not so sure about „Feet soreness“, but there's a ton of simple running specific exercises for both knees and ankles, but you gotta keep it up and be patient. I for example have a back issue that I take care of with some respective exercises, as soon as I drop them, it becomes a huge thing.

Hope I don't get on your nerves, I understand you ask for shoes, but really: those things are not a shoes fault and can't be solved by shoes either. Running itself isn't causing pain, but it shows what strength issues we have and will have to take care of.
[j0yh0d5] (score 2, diepte 5) I mean this is sensible advice but sometimes it really is about the shoes. That said, looking for a shoe that fixed someone else's problem is not the right approach.
[j0z7ltr] (score 2, diepte 6) > Plus, most casual runners want to be able to go out and just run a few miles. They don't want to spend the next year on very disciplined strength training so they can become the best runner they're capable of, and truly maximize their performance

That's a false dichotomy if I ever saw one.
[j0z9nb7] (score 2, diepte 6) >Can I venture a guess that you run in Altra?

No, these days I don't own any zero drop shoes, my rotation offers drops from 3mm to 9mm from all kind of brands and I'm not too dogmatic about it. I think it's a good idea to have shoes with various characteristics (foam, drop, stack height etc.) so we won't experience the same sensation over and over again.

&#x200B;

>Plus, most casual runners want to be able to go out and just run a few   
miles. They don't want to spend the next year on very disciplined   
strength training so they can become the best runner they're capable of,  
 and truly maximize their performance.

I agree that we shouldn't go overboard to the point where strength and warmup routines become an ordeal that doesn't match a casual jog around the blog, that makes no sense indeed. But it doesn't have to be that way: the routines I do before each run take about ten minutes, I run 80-90 kms or 50-55 miles per week. In my experience consistence is much more key than volume when it comes to strength training. ymmv of course.

&#x200B;

>"It doesn't make sense that a shoe would cause you pain" is just   
incorrect. The wrong shoe can absolutely cause pain. I love the Kinvara.  
 I'm 160 miles into mine and they feel wonderful. But your feet and my   
feet are shaped differently.

Oh I agree, shoes can be a pain for sure, but that's not what I said; I said if \*any\* shoe would give you the same set of issues, it's worth looking beyond the shoe, I was referring to OPs point that he was looking for a pain free running experience for several years now.

Hope I made my points a bit clearer now. :-)
[j10qgb3] (score 2, diepte 7 OP) Thank you 🙏.  BTW you run an amazing amount of mileage every week.  Wow 😮
[j10pa9p] (score 2, diepte 1 OP) Cool thanks for the shoe idea
[j0zsce9] (score 2, diepte 2) Orthotics are medical. Nothing about a simple molded insole needs to be prescribed though. The reviews alone speak for themselves!
[j0zupz8] (score 2, diepte 3) Oh okay, sorry, I did actually mix those two up (German speaker here, sometimes things get lost in translation). Thx for clarifying!
[j0zvfa7] (score 2, diepte 4) Not to worry. Sorry for the confusion!
[j10nd63] (score 2, diepte 1 OP) I’m in Canada don’t think we have road runner.  But I’m sure have something similar
[j0wd2c0] (score 1, diepte 1 OP) Not really meaning to argue but I do strength training.  Have for a few years.  And the problem has not gone away.
[j0z3nbh] (score 1, diepte 5) Can I venture a guess that you run in Altra?

Yes, strength training is good. Working on form is good. I've done plenty of both, and it's helped me a lot. I prefer a low cushion, low drop shoe so I can maintain a pretty natural gait and foot strike. But every body is put together a little differently. Not everything is a muscle strength issue.

Plus, most casual runners want to be able to go out and just run a few miles. They don't want to spend the next year on very disciplined strength training so they can become the best runner they're capable of, and truly maximize their performance.

"It doesn't make sense that a shoe would cause you pain" is just incorrect. The wrong shoe can absolutely cause pain. I love the Kinvara. I'm 160 miles into mine and they feel wonderful. But your feet and my feet are shaped differently.

Here are a few to try: Brooks Glycerin GTS, Saucony Tempus, Altra Paradigm. They are all stability shoes with plenty of cushion. They will offer much more support and protection compared to the Kinvara.
[j0zbw24] (score 1, diepte 7) It takes time to actually build the kind of strength we're talking about. If it's a muscle imbalance, that's not going to be solved in a couple weeks. It's going to take time to fix that, and then build up the running while maintaining that newly built muscle strength. 


It can be a lengthy process, especially when you consider a casual runner who just wants to run 15-20 miles per week is not going to be as diligent about strength training as a more serious runner.
[j0zi9nd] (score 1, diepte 8) I don't agree at all here – „strength training“ doesn't mean we will have to build up extraordinary amounts of muscles to cope with our training, it means balancing the lack of movement and mobility of our every day life. We are used to sit on the couch watching netflix for hours no prob, but ad hoc (before we start running) we are not able to run for an hour, even though we have the perfect tools for it. Strength and mobility training is much more about gaining our natural fitness according to our bodies than to build up muscle mass.

If you talk about serious issues like chronic muscle imbalances or the like, then that's something a physio should be asked about. But many issues (shin splints, runners knee, sore ankles etc.) feel very dramatic, but only point to the fact that we have been lazy bastards until now. And running itself won't take care about those issues, hence proper strength exercises should always be part of our training, no matter if we're ultra racers or just jog around the lake a couple times a week.
[j1154ti] (score 1, diepte 8) Haha, thank you. :-) Kudos to you for keeping it up!
[j10pxuo] (score 1, diepte 6 OP) Okay thank you
[j10pm3d] (score 1, diepte 5 OP) Where can I find the info about the types of exercises that might help?
[j1141c7] (score 1, diepte 6) One very simple way of getting started would be Bob & Brad on YouTube, there you'll find [→ a ton of running related tips and exercises](https://www.youtube.com/@BobBrad/search?query=running).

And in case you want to dive a bit deeper into running mechanics and its medical implications and how our feet and bodies interact with our shoes, I recommend checking out [→ Doctors of Running](https://www.youtube.com/c/DoctorsofRunning), who do all kinds of shoe related stuff like reviews and discussions, but from a medical / physio point of view.
[j0wiq40] (score 1, diepte 0) What other shoes have you tried? And where do they cause you pain, specifically?
[j0xfrxy] (score 1, diepte 1 OP) My first pair of running shoes I bought when I started running were Nike Pegasus 34s they felt the best.  The Pegasus 35s was the start of my discomfort running in shoes tried a saucony and they seemed to bother my knees and the saucony kinvera I have now my knees ankles and feet hurt
[j0wj343] (score 1, diepte 0) Honestly some shoes just don't work for people. You may want to try somewhere new. If you like really lightweight and Saucony I would try the endorphin speed 3, I absolutely love my speed 2s and they 3s are reportedly better. It could be anything, clearly you take care of yourself and strength train, so I could be your running mechanics, height and weight, or the shoe itself.
[j0xg8dt] (score 1, diepte 1 OP) My weight is a little too high I’m currently working on that.  Probably is something wrong with my form.  Unfortunately no one to teach me the proper way.
[j0xhxdx] (score 1, diepte 3 OP) Thank you I used to run 20 30k without much of any discomfort
[j0xinm9] (score 1, diepte 4) What shoe did you run that distance in? Now that your running has changed some I would definitely recommend a shoe with some more foam.
[j0xjuk5] (score 1, diepte 5 OP) It was the pagasus 34.  But unfortunately they wore out.
[j0xk0xq] (score 1, diepte 6) Well it wouldn't hurt to try the new 39s or if you want something that feels a little lower and firmer the Next Nature's are very nice. I like them for easy miles or track work.
[j10nxal] (score 1, diepte 7 OP) When I tried the 35s they felt narrow and uncomfortable but I heard they have wider versions.  It might be worthwhile to check them out
[j0y1p14] (score 1, diepte 0) I used to have a lot of foot/ankle pain from running.   I do a lot of runs now in the Nike invincibles and they’re probably my favorite daily shoes. I don’t really have anymore pain and I’ve been able to run a lot more than I did before
[j0yd6hy] (score 1, diepte 0) Try getting custom insoles. If you’re having knee pain, it could all come down to not having the correct support under your feet. Don’t get some stuff off the rack. Go to somewhere like Road Runner that can mold them right to your feet. Your body will thank you!
[j0zismw] (score 1, diepte 1) Custom insoles should only be prescribed by a physio or the like, the staff at running shops do not have the medical knowledge it needs to recommend them. Running shop staff making medical assumptions is a huge red flag.
[j0xgz2c] (score 0, diepte 2) I would look to YouTube, Ive had a coach, but over the summer I used YouTube to help with workouts and form. It's a great resource. Good luck on your future runs!
[j0wg634] (score -1, diepte 3 OP) I didn’t give up the strength training but I did give up the running for a year to try to heal my ankle.  Then started running again in august now I still have the ankle problem plus knee and feet soreness.

=== THREAD 1aspoal ===
SUBREDDIT: r/Shoes
DATUM: 2024-02-17  SCORE: 2  REACTIES: 33
TITEL: All-black work sneakers/hikers etc
POST (source_id=post):
Hey everyone. I’ve been living off the cheap $20-30 shoes at Walmart my whole life, and have found that they fall apart after a few months fairly consistently. They’re still wearable but the insoles get ratty and uncomfortable, then they deteriorate from there. 

I work in security, and do a *lot* of walking in the average workday, 21-32k steps a day generally.  I’m looking for something that cab stand up to this for a prolonged period of time while supporting my foot and most importantly being comfortable to wear.  Budget is $60-150 depending on the quality. 

No dress shoes or high-tops, please!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kqs7hlf] (score 4, diepte 1 OP) 1: no soliciting. 

2: why tf are you trying to sell me shoes that I can’t buy? This is not how you network

3: kickstarter, really?
[kqs7c78] (score 3, diepte 1 OP) Dude, are you serious?
[kqs5ads] (score 2, diepte 2) I think you want Hoka bondis, possibly in a wide size. They're pricy but there's nothing like em.
[kqsbzvj] (score 2, diepte 4) As an alternative to hokas, I have had a pair of Kurus for almost three years and walk in them everyday. Super cushy! I think they were $180, which was painful, but they’ve been worth it and I’ll prob buy again when needed. I have a plain black pair with like a tealish sole. I can’t remember which exact pair they are. Way cuter than Hokas imo!
[kqsy3ra] (score 2, diepte 4) Yeah they're ugly and expensive but like walking on clouds.
[kqto6xv] (score 2, diepte 0) I work at the airport (ramp, very busy) i used to only buy Nike, until i discovered New Balance , game changer! But…. Has to be 327’s … i love them so much i have 13 pair and counting!
[kqvmy84] (score 2, diepte 1 OP) No nikes.
[kqvodjt] (score 2, diepte 0) Something to consider, you’ve been spending $30 every three months. That comes out to $120/year. You could buy $250 redwings or a similar work boot that you can resole every few years and potentially have them the rest of your life if you take care of them. It’s a big purchase up front, but much less expensive in the long run.
[kqrzjhs] (score 1, diepte 0) What size shoe do you wear?
[kqrzodj] (score 1, diepte 1 OP) I could skirt by w/ 11s but can’t stand the tight toe feeling so usually wear 12 or 13 (US)
[kqs7adv] (score 1, diepte 3 OP) I’ll take them into consideration
[kqs8le0] (score 1, diepte 3 OP) The only kind available in my size and in wide are the bondi 8s, which are over budget, are kind of tacky looking and look extremely uncomfortable
[kqsqsmt] (score 1, diepte 1) I'll take 3 please
[kqs1l46] (score 1, diepte 0) You will probably be able to fit my size 45 soles (European) size but the soles are black
[kqs38lg] (score 1, diepte 0) Merrell have styles with lots of toe room in all black. Slip on or with laces.
[kqs7efx] (score 1, diepte 1 OP) Will take into consideration.
[kqwhz6e] (score 1, diepte 2) Merrell Moab is great. Don't know if they come in all black but Merrell is great. They make hiking shoes which are very sturdy for work wear.
[kqsdnkw] (score 1, diepte 0) Bates, Keen (great shoes). Rockey. Have you been to a uniform shop. Or a work boot store. I’m lucky where we live there are both.
[kqsiorz] (score 1, diepte 1 OP) I have been to neither, sadly. My uniform was supplied by employer and I’ve been clothes shopping like 4 times since I moved out, and I’ve just been getting my shoes. Which ones should I look out for ?(midwest)
[kqsjgao] (score 1, diepte 2) I really like Keen. But there are so many boot or shoe company’s that make totally what you need. Your on cement a lot I bet. So good support will really help you out. I worked in hospital doing warehouse work. Then I wore work boot with steel toe. Then in hospital I wore keens and brooks shoes. Also look into a new intersoles.
[kqtb89i] (score 1, diepte 0) I got some quite nice Karrimor all black hiking shoes I use for work. They go pretty well
[kqtbrif] (score 1, diepte 0) Steve Madden do some nice all blacks that my husband wears. Also any triple black Nikes might be an option
[kqtoejc] (score 1, diepte 0) Ps The New Balance 327’s are good for  wide feet , they have great arch support and hold up! Has to be the style 327
[kqv0bhk] (score 1, diepte 0) Nike Air Force 1s. My dad works in a warehouse and walks a lot and wears his every single day and swears by them. The stiffer leather holds up better than mesh and canvas, so they don’t “collapse” on the sides and heel. The insoles they come with have some arch support and he says they’re the most comfortable shoes he’s ever worn and that’s after wearing orthopedic shoes and Skechers for years before he discovered these.
[kqw70wa] (score 1, diepte 2) And $20 Walmart shoes are ethically made?
[kqwash4] (score 1, diepte 3 OP) The entire point of this post is trying to get away from that dingbat
[kqwkp8v] (score 1, diepte 4) You never mentioned ethics
[kqwlgij] (score 1, diepte 5 OP) You might be the most redditor redditor to ever reddit.
[kqwn5yx] (score 1, diepte 6) What? You said the entire point of the post was to get away from sweatshop shoes. You never mentioned that in your post and $60 minimum means you’d still be buying sweatshop shoes
[kqvorzs] (score 1, diepte 1 OP) I wear the shoes for way longer than 3 months they’re just uncomfortable
[kqx0yrk] (score 1, diepte 0) New Balance Fresh Foam are also very cushy. And I just got some waterproof on clouds that I wore 10.5k steps the first day that are delightful (I have many foot issues). The On Cloud 5s are reportedly ideal as well. 

Do a search in this thread for “concert” for a guy who did a comparison of several pairs for standing at concerts. There are also many threads about the same issues as yours in any given month.
[kr4v57p] (score 1, diepte 0) Salomon Speed Assaults. So lightweight and you can definitely wear easily for 10-12 hour days. 

[Salomon](https://imgur.com/a/sABNAip)
[kqs1oll] (score -4, diepte 0) I also have a trail running type of shoe that we will be offering later this year.
[kqs1fta] (score -5, diepte 0) Right, I am a size 11.5 and about to drop our new line of shoes on Kickstarter called The MATRIX Collection. Right now I only have been able to get the shoes made in sample sizes (Women 6.5 and Men 8.5. They come with two pairs of removable insoles for you to use as you get the shoes dialed into your foot size, plus they adjust in the back of the shoes for a truly 3-dimensional fit. They are better than custom made shoes! I have one woman who has had multiple surgeries on her ankle so she was wearing slides when I meet her as a client for the remodeling company that I work with to pay my bills. Unfortunately for you, I have to make them initially with white soles since the outsole supplier will make the soles in one color for a contracted price and we need  to sell 1500 pairs before we can order the soles in black. But if you want to see some cool shoes please visit my website www.PerfectFittingShoes.com. 
I don’t have a lot of reviews yet which is why I am willing to offer them out in exchange for an “honest “ review.

=== THREAD 1pwlcvj ===
SUBREDDIT: r/Shoes
DATUM: 2025-12-27  SCORE: 2  REACTIES: 33
TITEL: What shoes are best for a 65-year old woman who’s feet hurt from walking on her feet all day at work?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nw4e4mo] (score 6, diepte 0) Retirement!

$200 Hoka sneakers are famous for nurses who work hard shifts for long hours. 

Any running shoe/sneaker will offer superior cushioning, you can check the sales racks at Ross/marshalls/tj maxx/burlington for some discounted sneakers, look for a brand like Nike or adidas with a thick sole.
[nw6b8x6] (score 3, diepte 0) I walked what felt like 10000 miles delivering Amazon (52f) in my Dude’s. I love them
[nw6z9z1] (score 3, diepte 0) Danskos.
[nw4fi9r] (score 2, diepte 1 OP) What about Pegasus??
[nw4o6xh] (score 2, diepte 0) Hoka and Altra
[nw6nnoi] (score 2, diepte 1) I had a pair of Skechers with the thick soles that are shaped like Hokas, and every time I wore them I tripped. Once I tripped hard enough that I had to go to the ER. idk, they just threw my balance off. I don't have balance issues otherwise, and haven't tripped at all since I got rid of those shoes.
[nw7paeo] (score 2, diepte 2) Good to know. Guess once you recognize the shape in a different brand should try on before buying!
[nw9n5ox] (score 2, diepte 0) You may also need to look into custom orthotic insoles for better support in any shoes you wear.
[nw4i15f] (score 1, diepte 2) If you mean Nike Pegasus sneakers then yes those would work great.
[nw4n8om] (score 1, diepte 2) Look into the Altra Olympus.
[nw92v4q] (score 1, diepte 2) Broke a metatarsal and the doctor recommended Hoka's.   Thick sole but lots of support, not squishy like sketchers.
[nw4k6ol] (score 1, diepte 0) My mom likes Merell
[nw5kz57] (score 1, diepte 1) My physical therapist recommended both.
[nw6cjkn] (score 1, diepte 2) I use both and they help tremendously! I’ve had strokes and walking issues. These are wonderful.
[nw4v0vy] (score 1, diepte 0) Hokas and Docs.
[nw5bifz] (score 1, diepte 0) Hoka and On are my faves. But lots of companies are jumping in. Even Skechers now. Look at Hoka extra thick ones and start searching for similar looking bottoms
[nw6j7g2] (score 1, diepte 1) Link please.
[nw821h5] (score 1, diepte 2) Www.heydude.com
[nwa8ymx] (score 1, diepte 3) Those look fun.
[nw6eri3] (score 1, diepte 0) Easy Soirit Traveltime.
[nw7qoix] (score 1, diepte 0) I have several pairs of Ecco, even Chelsea boots with support. They are perfect for me.
[nw8ss1q] (score 1, diepte 0) I’d recommend the Hoka bondi 9 sneakers. I walk about 25k steps every 5 hours, so I’m also on my feet. I swear by [these](https://www.hoka.com/en/us/womens-everyday-running-shoes/bondi-9/1162012.html)!
[nw8ybm4] (score 1, diepte 0) Hokas, vionic, brooks
[nw97eyt] (score 1, diepte 0) Dansko Paisley sneakers.  Paisley is the design, not a print on the shoe. I'm a 50 year old retired dancer (feet and hips destroyed), and i work in film/tv production.  I'm on my feet for 14-20 hours/day, and these have changed my life.
[nw9sls2] (score 1, diepte 0) Brooks Ghost Max 2.  Try them...Also Allbirds are comfy shoes too.
[nw9tt4o] (score 1, diepte 0) My hurtin’ dogs started feeling much better when I bought some Hoka Bondi tennies. They might be a teeny bit pricey but they last and boy do they ever feel good.
[nw9zpg8] (score 1, diepte 0) Brooks Glycerin and Adrenaline, Danskos, Orthofeet all work for me.
[nwafpdq] (score 1, diepte 0) Avoid flat shoes and go for something like Hoka Bondi or Dansko clogs, they are really good for all-day walking and reduces foot fatigue
[nwagbp6] (score 1, diepte 0) Sketchers are my favourite
[nwak8g8] (score 1, diepte 0) I use Hey Dudes as my house shoes they are light and soft.
[nwb8ebe] (score 1, diepte 0) Just go for for shoes with good arch support and a cushioned sole. For long hours best ones are Hoka and and ASICS.
[nwbs12g] (score 1, diepte 0) Hoka’s and bombas compression socks save my feet and legs.
[nwcr034] (score 1, diepte 0) HalluxCare Orthopedic shoes
[nwe9gr1] (score 1, diepte 0) it depends on which area of your foot hurts and why (Does your arch ache?  are you wearing unsupportive shoes?  do you pronate or supinate?  are your feet wide and you are wearing shoes that are too narrow?)

Go to a shoe store that has personnel who are trained in how to properly assess someone's foot/old shoes and fit for new.  So a really good sports shoe store or a store that sells shoes for problem feet.  Dont buy online or at a place like DSW.

I've  had much better results in leaving my feet to "professionals" than just picking something I've heard is good.
[nwgetyn] (score 1, diepte 0) Hoka bondi sr or bondi sr, on running cloud monster 2. Wear graduated compression stockings too. I’m in healthcare and also on my feet all day.
[nwgz4gy] (score 1, diepte 0) I am a near fifty woman and also work on my feet all day. Hokas did absolutely nothing for my feet pain and had such little support I felt wobbly. I like Brooks Adrenaline.
[nwowsoc] (score 1, diepte 0) I'm a dansko and altra fan.

Something else that really helped me? Switch your shoes in the middle of your shift. Changes pressure points, gives sore spots a break. 

Compression socks and changing shoes mid shift made a huge improvement for me.
[onlvgzv] (score 1, diepte 0) Can you wear any kind of shoe at work? I have had plantar fasciitis and achilles tendonitis. I switched to Danner Trails. Not the campo...those are narrow. Plain old Trail. I also wear the Keen work boot: San Jose  stay away from the safety toe versions. Every Danner I have owned have been a pleasure for my feet even after years of use. My only complaint is that the hiking boots are warm so I only wear them in the cold months.

Danner also has a work boot but my feet don't fit in them well. Some of their models are narrower than others.

I also have insoles for my Pro Kedsbut I can't do two days in a row.

=== THREAD jjg979 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2020-10-28  SCORE: 6  REACTIES: 33
TITEL: My feet are f*cked, are there shoes for feet like mine?
POST (source_id=post):
Update: Bought Bondi 7s in wide. Returned them. Now I have the Echelon 8s in wide and I think this might be the one. I'm ordering x-wide just in case. 

Okay so! I've been running for 8 months now, at the beginning of covid I was determined to get out and crush it in any way, shape or form.

At first I ran in my air Max's because I didn't have money for new shoes. Then I thought okay, I'll buy some Nike's. I got a pair of expensive Nike runners that sucked, then I tried another pair that have historically hurt my feet, and now I'm on Nike renew because they were cheap. But I am ruining my body. 

About 2km into every run my ankles start to hurt, then it creeps to my knees, then hips and back. Looking at me you'd never be able to tell I was in pain because I'm in good shape, but I've accepted I'm doing damage. My socks usually have some blood on them and even after short runs I have new blisters. Every. Time.

Here's what I learned about my feet today from going to running room/new balance and talking to the people there. I had a 3D scan done that showed me exact dimensions of my feet. Which was sad lol.

1. My feet are flat as can be, and very, very wide.

2. I pronate inwards, so I will be needing support for sure. After my 10k yesterday my tendons on the inside of my ankle are very much inflamed and I'm limping.

3. My feet are actually wider in the middle than at the ball... which is the main issue. The girl at new balance literally said "you need to see a doctor" lmao! Anyways, I am literally bursting at the seams on every shoe, my "arch" always hangs off of the sole in the middle of the shoe making the pronation worse. I think my arch is actually further back than most shoes place them. 

4. My right foot is closer to an 11 and my left foot it a 10.5

5. My left heal is very wide, much more than my right. 

I tried on the widest shoe new balance makes I think it was the 840 6E, while my toes had lots of room I still fell off the side of the arch. Again because me feet are actually not their widest at the ball. I felt the same pinch point in my arch like always (this is where I get tons of blisters)

Essentially my joints are taking a beating everywhere at this point and I'm desperate to fix it. 

After a bit of research I've decided I think the hoka one one brand might be for me. I actually tried on a regular width shoe today that was close to fitting comfortably. The problem is no one has any wide or extra wide in stock (I'm in Ottawa). I liked those shoes because the sole is huge, there's no narrow section in the middle and it seems like they might work if they are available wider, with support. 

I'm determined to fix this issue, and I refuse to stop running in the meantime!

I'm hoping someone out there may have had a similar experience or can guide me in the right direction, I would love to run pain free for the first time!

Thanks for reading.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gacms2j] (score 11, diepte 0) I don't know what widths they come in but the Hoka Gaviota 2 is the most supportive Hoka.
[gacpj0b] (score 7, diepte 0) See a podiatrist or prdorthist that is knowledgeable about running. For example a store near me and throughout the surrounding cities in my area have pedorthists that fit you with shoes.
[gad65jn] (score 4, diepte 0) Go for the Arahi if set on Hoka. Surprised New Balance didn't work for you, they're known to run a little wider whereas Hoka is known to be pretty narrow. You might also see if you can find a pair of Saucony Guide 13 or Hurricanes that work for you. Stay away from Nike though. I fractured both feet running in them, they're just so damn narrow.
[gadl89j] (score 3, diepte 2) What!? My appt cost nothing insoles are about that process though...
[gadljhk] (score 3, diepte 4) Damn any place that forces you to buy is a bit crazy imo. Go to a running store then that isnt pedorthists?
[gadld51] (score 2, diepte 3 OP) Ya it's nuts lol, they said if I don't buy anything it's $85 for the appointment. Im honestly not going. I don't think I need an insole, I just want a professional opinion on what kind of shoe to buy and where the heck to get it lol. 

I guess I'll be ordering online and shipping back and forth until I find something.
[gadls06] (score 2, diepte 6) I assumed that would be the 3 running stores in your area? If so, I'm not too sure what else I can suggest
[gadmgit] (score 2, diepte 8) Sounds like you are in Canada so idk if you have a place called kintec? And yeah barefoot and minimalist isnt for everyone necessarily and especially if it is cold af out and you dont have the minimalist type shoes on.
[gadmpdv] (score 2, diepte 10) I tried! Hit up places near Ottawa if they arent in lockdown
[gadx425] (score 2, diepte 5 OP) I'm at MEC right now and the Bondi 7's are so comfy. I'm trying on the wide and it's still not wide enough. The double wide isn't in stock tho! So frustrating lol
[gafoxil] (score 2, diepte 1) Hoka Gaviota 2 would be better IMO. More structure and wider base.
[gae5oox] (score 2, diepte 0) Your feet will NOT like hokas. Their midfoot area is much narrower than an average person's so your foot shape is the ABSOLUTE worst for Hokas. I have feet somewhat like yours except only slightly wider and I get nasty blisters on my bottom of my foot where the Hoka midfoot area constricts around my foot. It's such a weird shape.

I've found Skechers Go-run series (such as Gorun 7+ and Gorun Ride 8) and Saucony  Freedom 3/ Triumph 17 (do they make those in wides? You want to check) work for those feet type best. Definitely not Nikes (run narrow).
[gae65uy] (score 2, diepte 1 OP) That's interesting, everything I've heard and seen has contradicted that statement. Holding up Hokas side by side with every shoe they are visually much wider throughout the middle. They are the only shoe I tried on that actually felt half decent. I just bought the Bondi 7's in wide but I have to order the x-wide to compare because they don't quite do it. They're 95% perfect though. The Arahi regular was comfy but I would also need a double wide in that one, they simply don't make it. 

I will look into the sketchers though, Saucony I've also had no luck with, still too narrow in the middle. Very odd. 

Who knew how challenging this would be. I will continue to run though.
[gafwzo7] (score 2, diepte 1 OP) Great advice, I will reach out to clinics for sure. 

The 840's I tried in a 6E and weren't wide enough. I'm honestly close with the Bondi 7's in wide, everyone is bashing Hoka and I just don't understand why, the bottoms are massively wider than anything else I saw on the shelves. No one else carried wide Brooks or Saucony with the exception of one pair of Brooks that were wide, but still no dice. 

Gonna order Bondi 7 in x-wide and see how that goes too.
[gafzj0i] (score 2, diepte 3 OP) Oh interesting! I would attach a picture but I'm a Reddit noob and don't know how, but the uppers aren't the issue! I realized I only pronate because my foot overhangs the arch on every shoe and the wider base is what I need. 

I was shocked how cushioned the bondis were, I'll update on the x-wides
[gadlnl3] (score 1, diepte 5 OP) Well ya that's what I did first. I went to three running stores, tried on every single shoe and even did 3D scans. They were all stumped lol, the lady literally said "you need to see a doctor" ahaha
[gadm3zi] (score 1, diepte 7 OP) Well I went to 2 different running rooms. One claimed to be the biggest in the country lol, still barely had any options. I also went to new balance (where I had the 3D scan done). I'm gonna checkout MEC today but I'm not holding my breath. 

Me feet aren't shaped like a normal foot where they are wide at the front, narrow in the middle, and wide again at the heel. They are wide at the ball, and even wider in the middle where my arch is. I burst at the seams in every shoe over the arch area. 

I'm definitely not comfortable trying the whole barefoot running thing, it's also snowing where I am now too so fuck that lol. I just need a shoe that is shaped like a rectangle haha!
[gadml9f] (score 1, diepte 9 OP) Ya I'm in Ottawa, just checked it out doesn't look like we got it. 

Oh well, thanks for your help man!
[gadwrm4] (score 1, diepte 4) Shit, I thought I had problems with a painful bunion until I read your situation


>I guess I'll be ordering online and shipping back and forth until I find something.

This is what I do. I could buy a fancy new pair with what I've spent on postage costs lately. I'm waiting for Clifton 6 (wide) to arrive in the post next. I got them on sportshoes.com
[gadwsnk] (score 1, diepte 5) **I found links in your comment that were not hyperlinked:**

* [sportshoes.com](https://sportshoes.com)

*I did the honors for you.*

***

^[delete](https://www.reddit.com/message/compose?to=%2Fu%2FLinkifyBot&subject=delete%20gadwrm4&message=Click%20the%20send%20button%20to%20delete%20the%20false%20positive.) ^| ^[information](https://np.reddit.com/u/LinkifyBot/comments/gkkf7p) ^| ^<3
[gae01ws] (score 1, diepte 6) Yeah sounds like a nightmare. Most shoe companys seem to be making shoes narrower & tighter with every new release, even the wides don't seem to be as wide as they once were in alot of shoes. Hope you get sorted
[gae3v9i] (score 1, diepte 1 OP) Tried them lol! No luck
[gahk8xz] (score 1, diepte 2) Hmm the other stability shoes I like are hoka arahi 4 and graviota 2 but I dont know if they are wide enough.
[gadh172] (score 1, diepte 1 OP) So I tried the Arahi but they didn't have wide. I was told Hoka is normally wider than other brands, is that true?

I wish more stores stocked wide options!

Totally agree on the Nike comment, I fractured my left foot 2 times running in them so far.
[gaffn2h] (score 1, diepte 2) Agreed with the guy above. I've run in a bunch of different brands and found New Balance to be the most forgiving for a wider foot. That being said, I'm comparing regular widths rather than wides. But New Balance has a ton of good options for wide feet that won't break the bank.
[gae2bca] (score 1, diepte 0) Can you please show us a photo of your feet? This is very interesting.
[gae37ap] (score 1, diepte 1 OP) I usually charge for those kind of pictures 🤣
[gae3i5a] (score 1, diepte 1 OP) I'm a total noob and don't know how to attach pictures :/
[gae6esa] (score 1, diepte 2) Also look into this: https://www.believeintherun.com/2020/05/11/best-wide-foot-running-shoes/

some suggestions there which may help.

I can tell you firsthand that my midfoot is a little wide for my foot type and while my feet fit comfortably in a Normal for all shoes, that one constricts my midfoot and I step on the raised arch part painfully in Hokas. A lot of people have had similar experiences to me in my running club.

That said if you bought them and tried the Wide/X-Wide and they work for you, hey, that's great news!
[gafw0r0] (score 1, diepte 0) In my opinion the NB 840 wide is usually going to be your best bet for your foot type (by what you've described). Comparable high volume shoes from other brands include Saucony Echelon and Brooks Dyad. They have straighter lasts which will accommodate your foot better than a semi curved last (which is found in most running shoes). Try to reach out to other pedorthic clinics in the area. I used to work at a couple that don't charge for assessments and can make other shoe recommendations/orthotic advice.
[gafzals] (score 1, diepte 2) Yep Hokas have a wide base but not necessarily a wide fitting upper, but whatever you find comfortable is the best call. Good luck with the Bondis! I've heard great things and enjoy my Cliftons.
[gadh760] (score 0, diepte 1 OP) Ya I have an appointment this morning but it's $500 for insoles and $85 for the appointment lol! Fml
[gad54vo] (score 0, diepte 0) Brooks Adrenaline gts 20 is a stability shoe and tends yo fit wider feet.

=== THREAD 19a6982 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2024-01-19  SCORE: 1  REACTIES: 33
TITEL: Removable insoles
POST (source_id=post):
Why do some shoes have removable insoles? I don't seem any benefit.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kij5oyz] (score 11, diepte 0) There’s no real reason to not make them removable. All companies do when they make them not removable is annoy people that want to use different insoles.
[kiitk61] (score 9, diepte 0) If a shoe gets WET… easy to remove and DRY!
[kiiu953] (score 9, diepte 0) not sure if it’s the reason behind it, but for someone with custom orthotics, it’s great to remove the insoles and then swap out the orthotics
[kij0p09] (score 7, diepte 2) It also has to do with MANUFACTURING of the shoes…
[kijg0iz] (score 4, diepte 2) So just leave it in?
[kik0kf5] (score 4, diepte 2) Insoles do not move inside the shoe
[kijco8s] (score 3, diepte 3) This is the answer. The shoe upper is manufactured and the sole is manufactured separately, they are glued together and the insole is added in after. 

In theory you could integrate the insole into the sole, but it’s probably more difficult in terms of size and having a nice cushioned insole.
[kij7zc3] (score 3, diepte 2) For a lot of us, shoes getting wet is a daily occurrence for a large part of the year. Also, in some situations it makes sense to wash your shoes to clear out the dirt or sweat and it's helpful to dry them then.
[kijk0n0] (score 3, diepte 0) They should all be removable.  As someone who uses support insoles and swap n switch between all my pairs. Nike racers are the only ones that glue them down a lot.  I hate it
[kikvxv5] (score 3, diepte 2) So glue them in...do they really cause you so much grief?
[kik702c] (score 3, diepte 4) I think you're wearing them wrong somehow
[kik6wmr] (score 3, diepte 2) Never happened to me before
[kik2z9e] (score 3, diepte 0) For starters: a lot of insoles wear down faster than a shoe. Swapping for fresh ones makes the shoe longer usable. The combo of a Inov-8 boomerang insole with my 1000km used Endorphin Speed makes them feel like new.
Second: insoles determine the inner available volume of a shoe.swapping a thicker for a thinner insole finetunes that amount of volume. There are shoes I run in without insoles because of the low volume upper
Third: Insoles can add drop and help with a quicker turnover. I have insoles with a 4mm drop and use them in a lot of shoes.
There isn't a shoe in my collection where I haven't removed the glued insole, even if I sometimes decide to keep using the provided one.
[kijxnbm] (score 2, diepte 2) Here in Ohio it's snowy and very wet out. That doesn't mean we don't go outside, it means shoes get wet.
[kikj0cn] (score 2, diepte 2) For a lot of people it happens quite often.
[kioyzs9] (score 2, diepte 2) Anyone with orthopedic insoles, which fyi is many people and some very good runners I've trained with, find removable insoles very useful.  Otherwise they have to run on double insoles, making fitting in the shoes difficult.
[kijotav] (score 2, diepte 0) I hate when they glue the insoles in.. why?? Just keep it removable so I don't have to spend half an hour ripping them out.
[kijyhh9] (score 2, diepte 0) Look under the insole, you’ll see the stitching between the upper and the Strobel layer. The insole protects you from irritation from the stitches. Many brands put more premium insoles in to have a better “step in” feel, but they compact down in 2-3 weeks.
[kik0szv] (score 2, diepte 0) Just don't remove them then. Problem solved
[kikkelc] (score 2, diepte 2) Maybe just get a hot glue gun (super cheap) and glue them down? You'd probably have to redo it after a while. Or buy some insoles like Superfeet, they have a plastic heel cup so shouldn't move around
[kioz31o] (score 1, diepte 2) All the time lmao, you must not live in a rainy region.
[kiscz56] (score 1, diepte 2) There's a thing called running in the rain. >:(
[kikvux6] (score 1, diepte 2) Most people? Are you taking a poll?
[kijusa9] (score 1, diepte 1 OP) I hate it when they are not glued in. They bother me when I run or walk. Insoles move inside the shoes.
[kik26kl] (score 1, diepte 3 OP) Yes, they do.
[kik9jfa] (score 1, diepte 5 OP) How?
[kik2a5u] (score 1, diepte 1 OP) They move inside the shoe. Rise up sometimes around the middle of the feet.
[kikavpw] (score 1, diepte 2) Depends on the insole, the inner top layer of the shoe and footstrike. I have it with very few insoles. Maybe you need thicker insoles so there isn't any room for inner movement in the shoe
[kik3rxr] (score -1, diepte 1 OP) Why do I feel like removable insoles move around when I wear such shoes?
[kiiyv24] (score -5, diepte 1 OP) That's a valid reason. And I guess it only applies to specific types of shoes.
[kijevhq] (score -6, diepte 1 OP) Most people do NOT want to use different insoles.
[kijuoes] (score -7, diepte 1 OP) I hate it when they are removable.
[kiiyr1c] (score -14, diepte 1 OP) How often do shoes get wet? Not good enough reason to create removable insoles.

