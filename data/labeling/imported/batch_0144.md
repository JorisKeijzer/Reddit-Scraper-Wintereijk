# Label-batch batch_0144

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
Schrijf het resultaat naar `batch_0144.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1vj1sjp, seucwp, 17pbe4n).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1vj1sjp ===
SUBREDDIT: r/BuyItForLife
DATUM: 2026-08-08  SCORE: 77  REACTIES: 62
TITEL: Walking shoes for someone who walks 5+ miles a day on pavement and concrete?
POST (source_id=post):
Hi all,

I'm currently rocking some no-name Chinese shoes off Amazon because they're cheap and I'm wearing through a pair of shoes in about three months. What would y'all recommend for someone who walks 5+ miles a day on concrete/asphalt (sidewalks and roads)? Looking to spend probably 80-100 per pair, and I need something that I can put custom orthotics in.

Thanks in advance!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[p2hy8rx] (score 73, diepte 0) Do you have several pairs that you rotate? This is a key factor. Do your best to have at least 2 pairs so that you aren't wearing down the same pair day after day.
[p2ifcwf] (score 69, diepte 0) Brooks Ghost or Brooks Glycerin.

You can find last years model on sale for about $100 on amazon. 

Fiancée is an avid walker and she likes the Brooks Ghost Max and Altra Torin.
[p2ikhvg] (score 46, diepte 0) In three months at 5 miles per day that is 450 miles. You are at the upper limit of what is typically the lifespan milage of a pair of walking shoes. Buy two or three pair and rotate them every day. You probably won't get more milage out of them but you will go longer period of time between needing new shoes.

At a unfortunately much more significant price point but more in line with this subreddits name you can find boots and walking shoes that are made to have the sole replaced. Typically those will have a much longer lifespan than your cheapo shoes or any shoe in you $80-100 price range. Essentially you would probably need to triple your budget. Unfortunately the Vimes Boots Theory is in effect here.
[p2lkvde] (score 28, diepte 2) Yes because there is esponential wear. Wearing your same pair of shoes every day puts more stress on them then if they get a day to air out, decompress and stop being warm.
[p2hxkb2] (score 20, diepte 0) I would look at hiking shoes with vibram soles. They’re built to protect your feet from impact and the vibram soles last longer. I like my Merrell Jungle Mocs a lot for walking the dog around the neighborhood, and also for travel.
[p2inekx] (score 20, diepte 1) Seconding the Brooks Ghost. I work for a distributor in grocery stores walking 10-14k steps every work day and lifting product (not forgiving floors) and ever since I bought a pair, I’ve been converted. Used to religiously buy Nike Pegasus for years. Had a pair of New Balance 1080’s that were really nice but got about a year of use of out them. Heavy usage mind you but they also weren’t good stability for the lifting aspect of the job. They’re also definitely out of OP’s price range. Ghost have been a sweet spot for budget and longevity imo.
[p2lgux6] (score 14, diepte 1) Does this actually extend longevity? If 1 pair of shoes lasts for example, 6 months then 2 pairs would mathematically last 12 months. Does rotating actually extend the life past this
[p2iruyp] (score 10, diepte 0) Brooks Adrenaline GTS 25
[p2kol4i] (score 9, diepte 2) Thirding Brooks Ghost. I know it’s not recommended, but I had a pair that lasted 7 years and still looked/felt basically new when I decided I probably should buy new running shoes
[p2kq8kt] (score 9, diepte 1) also, the cost to re-sole would likely surpass OP's budget as well.  \~20-25 years ago I took a pair of boots in to get re-soled and it was like $98 plus tax...a brand new pair were $110.
[p2u3bq3] (score 7, diepte 2) This is moreso for leather shoes/boots, particularly ones used in wet environments.  Allowing leather to fully dry really helps extend its lifetime
[p2kno8j] (score 7, diepte 1) This, and replace them every six months.
[p2jfpx6] (score 7, diepte 0) I've gone through manybpairs over the years for this exact issue.

Brooks, Hoka, On, New Balance, and others.

In my experience the New Balance 1080 and Hoka Bondi are the most comfortable if you're on your feet all day.

They're over hour budget, but you don't need padded inserts. 

The suggestion to rotate them daily is a good one.
[p2i23da] (score 5, diepte 0) We put many miles on Clark's and Born. Vibram hiking shoes from a good outdoor company might also be good - depends on terrain. 

The one frustration is the fused sole. But your budget won't reach the kind of shoes that you can replace the sole (I think)
[p2iwwzr] (score 5, diepte 0) I just bought 2 pair to swap out: Brooks Ghost Max 3s and Hoka Bondi 9s. The Ghost Max 3s lasted me 3 years on their own, but I don't walk as much as you.
[p2hwh9s] (score 4, diepte 0) Get a pair of Altras from Sierra.
[p2j5yoa] (score 4, diepte 1) I would’ve agreed with you three years ago, but something really strange has happened to ASICS.  Their quality fell off a cliff. They just fall apart after 4 to 6 months.
[p2ly9ll] (score 4, diepte 3) Fourthing Brooks. Just don’t order online for whatever you end up getting. Go somewhere and try on shoes.
[p2ru64f] (score 4, diepte 1) Solid option. Long lasting and durable. The “Toyota/Honda” brand for shoes
[p2m0xnf] (score 4, diepte 2) Good boots are $250+ and the soles will last 3-5 years minimum, even on heavy use
[p2kphrc] (score 3, diepte 1) Danner 2650s are great too. I've worn them for years and have been able to find them on sale for $50 - $110.
[p2of3fo] (score 3, diepte 1) Came here to say exactly this.
[p2pqybf] (score 3, diepte 1) Emphasize everything everyone else said about these. I used to work at a running store and Brooks is incredibly solid. Last 300-500 miles in running speak but just really well long lasting shoes that won’t have your feet killing you after a long day.
[p2qytfx] (score 3, diepte 1) I got Altra Torins when I worked at a big box store during the holiday busy season. I saw them recommended by lots of retail workers, warehouse workers, nurses, etc. They’re great for a full day of walking on hard concrete floors and lifting boxes. Good padding without feeling too squishy or having an excessive amount of drop. I do a lot of hiking in super-minimalist shoes so I’m sensitive to soles that feel too thick like Hokas. 

But more recently, I’ve been working in food service and picked up the black leather nonslip variant of the Altra Torins. Felt great to wear, but the glue on the sole started to come apart after only a couple months. I suspect that the outsole simply isn’t designed to hold-up against wet floors. 

Also, in general Altra has a reputation for not being especially durable. So I’m not sure they would qualify as BIFL. Personally, I don’t expect athletic shoes to be BIFL, but I was still a little disappointed with them. But I have yet to find a better shoe with similar fit and comfort.
[p2utw5t] (score 3, diepte 1) How do the Ghost fit? True to size or small? Overall does the brand run true?
I'm ready to hit order on a pair online because there's so many people supporting the Ghost style. I love my hands free Kizik shoes but I can make traditional shoes work for the most part if they really are as comfortable as everyone says.
[p2wb3d0] (score 3, diepte 2) I’d say TTS.

 I’m a 10.5 and have no issues. 

Brooks 10.5
Saucony 10.5
ASICS 10.5 
NB 10.5
[p2jecam] (score 3, diepte 1) I’m hypermobile too and I’ve been wearing the Ghost for years. The Ghost Max and Hokas are too cushy for me, but are there other shoes you like?
[p2j1apw] (score 3, diepte 0) New balance 928 is the greatest walking shoe ever made. Add some arch support if ur flatfooted and ur good for the year.
[p2j8qnp] (score 3, diepte 0) ASICS or Brooks would be great! Brooks if you need more support/structure, but I found it to be too much support/structure with custom orthotics. 

If they’re out of your budget, both Brooks and ASICS offer a pre-owned gear section that can be useful. In my experience, they’re shoes that were worn very little (someone didn’t like them, or ordered the wrong size). They’re about half the price of a new pair.
[p2keiar] (score 3, diepte 1) I had foot pain from an overuse injury and old shoes. Like, had to get an x-ray the pain was so bad. The moment I tried on a pair of Hoka, I had instant relief. They provide so much support!

Its a good idea to go somewhere to try on the different shoe recommendations and find the one that works best for your foot!
[p2knfhm] (score 3, diepte 0) I personally like an Asics gel nimbus, however a few things. Everybody’s choice for shoes is different based on their feet and I would suggest not taking anyone’s advice snd go to an actual running store that fits you. And that way too if it turns out that they’re not good,they usually have a good return policy. Also, I hope your know that no running shoes are by for life.
[p2ls6y2] (score 3, diepte 0) I've been a new balance devotee for a long time, but had many folks tell me to try hoka, so I did. Their site recommended Clifton's, and they are simply the most comfortable shoe I've ever worn. I use them for walks, but also for Disney days, which see about 7-10 miles each trip, and I go 1-2x a month.

I bought a pair of Brooks and they were so uncomfortable that I ended up having to go home and change my shoes. I found the arches to be much too high.

You don't mention why you need or this, but Hokas have a removable insole, which is nice.
[p2m6sh0] (score 3, diepte 0) So, I often do 20k steps per day on concrete and I use boots. 

My recommendations would be:

* Jim Green 719 - good value at less than 300 euro, resoleable, etc. 
* Red Wing Iron Rangers - these are also so popular than you can often find a good deal second hand

A few things to note:
* If going second hand, you either want a pair that is ALMOST new, or size up to make room for sole inserts as they will not conform to your feet specifically. 
* If you want a softer tread (these kinds of heritage boots are notably harder to walk in than sneakers), size up and get a sole insert. (Personally, I like the harder tread, but YMMV) 
* If you also need them in the office, avoid the Iron Rangers - the sole is hard, and really sounds loud in an office environment 
* Even with boots, having 2 pairs to switch between is "best practice", so it's a bit of an outlay. :/ 

That being said - I used to switch shoes once a year due to the number of steps I do, and since going to boots a few years ago, I haven't had to switch out anything. 
... Mind you, I HAVE spent a ton on boots because I love them, so there's that. 😅
[p2muwzr] (score 3, diepte 0) No such thing as a BIFL walking/running shoe. You'll get about 400-500 miles out of each pair. Lots of suggestions already ITT.
[p2xzauk] (score 2, diepte 3) Ty!! I always wondered about this and now I know
[p2of4ii] (score 2, diepte 2) City walking, sidewalks/pavements and gravel paths. 

I travel a lot, and walk around a lot of cities. Average about 10 miles/16km per day. 

Some of the models are a little chunkier, and I'll brave a cheeky dirt path now and again, but honestly for off-road I prefer the vibram shoes with a good tread.
[p2k492g] (score 2, diepte 2) Yep. The running store I frequent recommended converting from Brooks (for the last 5 years) to ASICS. They felt great but then the outsole started detaching from the the next layer after about 4 weeks.
[p2zwhzd] (score 2, diepte 1) Love the ghost wide fit.

Another good one is Tapo, depending on how much drop you need, most of it seems good. But as always try them on first if possible.
[p2qoqb7] (score 2, diepte 1) Lol what? 450miles per pair of shoes is ridiculously low. These have to be budget shoes
[p2ow5p9] (score 2, diepte 2) I got fitted at a running store so I’ve done my due diligence, but good call out for anyone else looking at my rec. Thanks!
[p2jg8ag] (score 2, diepte 2) I've worn the Ghost Max since 2023 and before that it was Brooks Beasts but I need a much wider toe box so I only wore those for a couple years. It was Saucony before that but I don't remember which ones. I'm really lucky that I have a fantastic local Run/Walk store that I've trusted for decades.

You might want to try on the Ghost Max again? The ones I tried on today were much stiffer than my 2023 ones but I still liked them for the roominess in the toe. My tendency to supinate is my biggest problem and most of my tendonitis occurs in the outside of my feet.
[p2jadl1] (score 2, diepte 0) I like brooks for walking. Not buy it for live as it's a shoe and it will wear but I have put thousands of miles in my glycerin 21 with no major damage just normal wear
[p2jvdko] (score 2, diepte 0) Mephistopheles walking shoes
[p2kdhec] (score 2, diepte 2) That is such a bummer! I’m sorry to hear that. I got a pair of Runoffs for Christmas 1997, and have worn nothing else since. Still have that pair.
[p2k1nf9] (score 2, diepte 0) I don't really worry about it, personally. I just buy comfortable shoes - often Asics or Columbia lately. I have a pair of Asics GT 2160 that have lasted about ten years, though not worn continuously. Probably something like 2,500 ye olde miles on them, give or take.
[p2kr0dt] (score 2, diepte 0) I used to have a job walking all around a concrete hellscape of an outdoor warehouse compound - 9.5 hours a day, non-stop walking and lifting/carrying 50+ pound items, rain, sun, wind and snow. I BURNED through shoes! The best luck I had was a pair of wedge moc work boots, they were uncomfortable initially but once they broke in they felt like a hiking boot and the soles were so thick that I actually was able to keep them for just over a year.
[p2ksewj] (score 2, diepte 0) New Balance usually lasts me a long time.  You will get the glue separating the body from the sole at some point, but you can very easily glue that back on; I've done that a few times.  

You will also get to the point where your sole is worn down to the foam (or worse).  That is also an easy fix; use the same glue that you used to fix your sole/body separation and glue on some rubber pads.  These'll wear more quickly than your normal soles, but they are also stupidly easy to replace.  You can stretch the life of the shoe immensely by doing this.  

I've got a pair of 483V3s that I've had for six years, and have put easily 1000 miles on.  They would have been trashed a few years back if I didn't see the glue hack here on Reddit.  

I also have some Asic GT-1000s with the same mileage; the body there didn't separate from the foam like new balance, but the sole seemed to wear more quickly.  Still an easy fix.  It's gotten to the point where the side of the body is starting to wear out so I think these guys are destined for the trash pile in a few hundred miles.  

Great shoes overall though.  Did a number on the back of my ankle at first, but eventually it settled in.
[p2ky13i] (score 2, diepte 0) I walk the dog on pavement 3–4 miles daily.

Saucony Men's Cohesion 14 Trail Running Shoe, $60. My Powerstep Pulse low volume full insoles fit fine. Great for my supination.
[p2l0ubk] (score 2, diepte 0) If you’re putting your own insoles in them you can get away with any decent sneaker. you don’t need to spend money on the fancy stuff it’s gonna wear out in 6 months no matter what. Just get one that’s a little stiffer for walking, the more flexible running style will hurt. When I was a dog walker I swore by Nike Pegasus with superfeet green insoles.
[p2lg9w3] (score 2, diepte 0) Thinner soled Ecco sneakers with FP Insoles Elite 3mm.  Been a server for 20 years and it’s been a body saver.  

Strengthen your feet too.  Shoes are a tool, not the answer.
[p2p1561] (score 2, diepte 0) Definitely not BIFL but I bought some Nike Prominas and I’ve had them over two years. Super thick sole. They don’t look particularly great. But they have no signs of wearing down. I walk way less than you but they have durability and on sale are around $50-60 in most cases.
[p2po1iz] (score 2, diepte 0) Been averaging 20k per day with Nike p6000s. The arch support is incredible. I used to wear new balance 530s but I can’t go back to them anymore, though I do rotate between them here and there
[p2qvelz] (score 2, diepte 0) new balance 574 classic sneakers, mephisto for work shoes (mens)
[p2syl5t] (score 2, diepte 0) Hoka Bondi SR have been very durable for me and I'm heavy ish.
[p2tr5ak] (score 2, diepte 0) I’d go to a running store and ask to try a couple different pairs a shoe designed for medium-long run training.

Basically there are training and race counterparts for each distance category… the training counterparts may feel a little less responsive (e.g., no carbon fiber plate in the sole) though can last longer due to foam type and are easier on the knees.

You should be able to find something that will both last you a long time and be super comfortable / easy on your knees (will almost feel a little mushy if you have not tried a shoe like that before).

New balance 1080s are what I have for middle distance 5-15k training sessions and they are awesome!
[p2w29s5] (score 2, diepte 0) I bought a pair of Hoka Cliftons last week.  Worth every penny.  This year's model and last years are the same size (according to google) so you can figure out what size fits and then order the last year's version 10 and save $50.
[p2x03e3] (score 2, diepte 0) Addidas Ultra Boost 5x for $52 on Ebay shipped.  Bought my second pair yesterday.
[p2zkkvj] (score 2, diepte 0) Brooks but use the website’s shoe finder module to see which are best for you. I started with Ghost and those weren’t good for me. After a lot of previous trial and error I used the module recommendation and found the more supportive styles work for me. There are specific models that have more space to accommodate orthotics.
[p375zfl] (score 2, diepte 0) Sketchers Uno Street are the most comfortable shoes for me with wide feet. 

Warning: They are of terrible quality and I need to buy a new pair every summer. Luckily I can find them 50% off on Amazon regularly.

 One holiday trip I walked over 500k steps and daily max 44k steps, no blisters or problems with the sketchers. 

Currently I have 3 new pairs of them waiting for use.
[p2huaze] (score 1, diepte 0) Hello /u/ThePastyGhost! Thank you for your submission! just to inform you, you may also want to try posting in /r/boots which is a smaller subreddit but might be or specialized for your request

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/BuyItForLife) if you have any questions or concerns.*
[p2mm6vf] (score 1, diepte 1) What do you use those shoes for if i may ask?
[p2i77oz] (score 1, diepte 0) High end Asics, and pick one depending on your pronation. Cumulus 27+ (27 or 28) for example if you have a neutral pronation are my go to.
[p6mmgdu] (score 1, diepte 1) Brooks 18?
[p2nhj49] (score 1, diepte 1) This shoe will mess you up if you’re not an over pronator, please get fitted at a running store to confirm this is correct amount of structure for you (I worked in running stores for many years)
[p2kd4bz] (score 1, diepte 1) Gave me my one and only case of planter fascitis after taking them on a 3 day business trip.  $300 for 3 months recovery.  (Yes they were broken in for 3 months prior to the trip.)
[pf0wecw] (score 1, diepte 1) Which brand/model of wedge/moc work boots did you have?
[pf1nfr8] (score 1, diepte 2) I honestly can't remember, there was a 6 year period where I bought 3+ pair per year and I always tried something different, trying to find what worked best. I also had to buy at least one pair for winter(snow, sleet and -10°F).

Thorogood or American Heritage, are both brands that are coming to mind...maybe. I remember they were on the pricier side(for me) $200 or more.
[p2mw2vu] (score 1, diepte 0) Is there 4E wide versions for these reccos?
[p2n83op] (score 1, diepte 0) I’m an ER nurse, I spend 12 hours walking on hard linoleum every work day. I swear by New Balance shoes and natural fiber compression socks.
[p2nbwvn] (score 1, diepte 0) VIBA shoes are so comfortable. I rotate them with Brooks athletic shoes.
(8 reacties met lagere score weggelaten)

=== THREAD seucwp ===
SUBREDDIT: r/Nurses
DATUM: 2022-01-28  SCORE: 30  REACTIES: 62
TITEL: Shoes!!
POST (source_id=post):
Okay what shoes are nurses wearing.  I have a stress fracture on my right foot and I think it's from my shoes and working. I'm trying to research the best shoes but would like recommendations. History of sore knees and feet. 23 years in Nursing

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hulurbt] (score 26, diepte 0) I wear dansko clogs, and I'm considering trying their new shoe that's a gym shoe style. As important is what kind of socks you're wearing. I like wool blend knee high compression socks. My favorite are from Duluth and they have extra cushion on the sole with compression in the arch/vamp and a non compression toe box. The compression socks took care of the majority of my foot pain.
Something I learned from my construction worker hubby is to have at least three pairs of good work shoes. Allow each pair to rest and dry out for at least 24-48 hours before wearing them again. This makes those expensive shoes last so much longer, and reduces odor.
Good luck.
[hulpxy5] (score 15, diepte 0) All of us have different feet. If you want the best shoes for YOU and not someone else, go to a running speciality store and be fitted based on your size, gait, etc.
[hultdkx] (score 13, diepte 0) HOKAS, on my 2nd pair of same shoes
[hulvux0] (score 8, diepte 1 OP) Thanks for the advice! I do wear compression socks but not cushions enough on the bottom. I don't know how to much money I have invested in shoes and socks to try to find the right pair but I love the idea of having several pair of shoes and switching them out that's one thing I do not do, I wear the same ones over and over. I will look into those wool socks thank you
[hulp8ln] (score 7, diepte 0) I loved my Brooks Levitates and I currently have a pair of On monochromes! My feet hurt a little more in the Ons I think, but I also have poor posture a super flat feet, so I hurt in everything by the end of the day lol
[hulrpq2] (score 7, diepte 1 OP) I've done that with my workout shoes never thought to find shoes there for nursing. Definitely would be a different pair of shoes because I have worn my workout shoes and I'm dying by the end of shift with my workout shoes.
[hulyiwv] (score 7, diepte 0) Hokas
[hulympu] (score 6, diepte 0) I wear Nurse Mates, but I’ve heard very good things about Hokas.
[hunhz4s] (score 6, diepte 0) Hoka One One Bondis are the absolute best. Like walking on clouds, super supportive yet still light. No pain after 3 12’s in a row. (They’re also the shoes I run races in, so they’re bad ass)
[hulto15] (score 5, diepte 0) I love Sanitas. Most people think I'm crazy...
[humj01q] (score 5, diepte 0) I think the rotating shoes is really the best answer.  None are perfect. A coworker swears by Oofos clogs and their recovery sandal at home. Another loves their Sketcher (the really tall ones I forget the name). I had a pair of Reikas that were awesome until the foam died. Right now I'm slowly killing myself in a pair of slip on Sketchers and thicker wool socks because the compression are just too thin and slippery. I liked Crocs but the 2nd time I slipped on wet floor I switched to tennis shoes.
[huo6sr7] (score 5, diepte 0) Anyone saying it depends on the person is correct. I can't wear Dansko but I see others doing it. My last hospital's IR nurse wore square toe cowboy boots with his scrubs because that was comfortable for him. 

But for me? Keen trail shoes. Good traction, water (urine) proof, super tough, comfy and wide enough for my Hobbit feet.
[huo5b5u] (score 4, diepte 2) They will give you HOKAs.
[hum5vvg] (score 4, diepte 0) Adidas Ultraboost are the best, they helped me a lot, I Bought like 4 different pairs
[huokx5v] (score 4, diepte 1) I second this. They are so comfortable.
[hun99x5] (score 4, diepte 0) My vascular access team walks for miles a day. About half the day shift is rocking Hokas right now, myself included. They're kinda magical.
[humajqn] (score 3, diepte 2) You also might need to see a podiatrist?
[hulx2lk] (score 3, diepte 0) I wear Keen.
[hulyywa] (score 3, diepte 0) I mostly wear Dansko clogs, not the XP (those are too narrow in the toe box for me). I’ll bounce between these and a pair of New Balance 574s.
[hunaqoc] (score 3, diepte 1) Rotating half way through the day and proper, supportive insoles. 

Think about the mileage you do every day and the hard surfaces you walk on. Those soles need time to rebound and recover. 

Don’t forget a change of socks - padded hikers are awesome.
[hunaccb] (score 3, diepte 0) Hokas. Helps my knees and back. I switched to an older pair after a painful long stretch. Haven’t looked back.
[huo55b2] (score 3, diepte 0) Hokas. They look like 90s Yamaha jet skis. 

But they are the closest to guaranteeing that your feet will be saved.
[hum6jza] (score 2, diepte 0) Having seen a lot of these threads on different nursing forums, the two I see recommended most often are Hokas and Brooks. They're also on the list my podiatrist gave me. I wear cushy ankle socks over compression socks and a low profile Merrell hiking shoe with custom orthotics.
[humrcbe] (score 2, diepte 0) Crocs or Hoka One One.
[hun92dn] (score 2, diepte 0) Hoka One Bondi 7. I used to wear Nike Rosche's and my feet would HURT. As soon as I switched to Hoka's I've never had problems with my feet. They're honestly the best. Plenty of marathon runners wear Hokas. They look chunky but they're lightweight. Chefs kiss.
[huofgdc] (score 2, diepte 1) Agreed love mine, about to buy my third pair, each last me about 6-8 months.
[hunxa2v] (score 2, diepte 0) With knee pain, you may want to stay away from soles that are too squishy. I found they tend to make the knee move around a bit more than a harder sole, which just aggravates the knee problem/pain.
[hunyour] (score 2, diepte 0) I wear a new balance Walking shoe fitted with the help of the shop that sells me running shoes. Whatever shoes I wear I take out the factory inserts and transfer my podiatrist made orthotics
[huorkk6] (score 2, diepte 0) Switched from Dansko’s to hokas. Very happy with the switch.
[hw92nt9] (score 1, diepte 3) My podiatrist gave me recommendations for shoes and shoe inserts and all were spot on.
[hup4zva] (score 1, diepte 2) Some stores carry non-running shoes as well. Things like trail runners, hikers, or work shoes/boots. For example, I wear work boots and have done so while loading trucks for UPS and while working retail. Heavier, yes, but good ankle support, waterproof, safety toe, and a build made for standing and walking on hard surfaces all day. I also have Superfeet Green inserts.
[huoosda] (score 1, diepte 1) Is there a subtype of Hokas or a specific type?
[hupra77] (score 1, diepte 2) I went to a running store at nearby college town, they analyzed my walk and foot arch, then recommended styles accordingly. After about a year, I ordered same pair off amazon. They ran about 150$usd. #WORTHit
[huo70fy] (score 1, diepte 1) That's the only thing I wore when I worked bedside.
[hum3b0q] (score 1, diepte 0) Right now, it's Nike Maxx Air that I wear. I'm actually going to look for something different next time. The bottoms of my feet often hurt by the end of my shift.
[hum6e67] (score 1, diepte 0) I prefer a neutral heel and a solid upper to protect against splashes or dropped sharps. Currently I'm wearing Crocs but have rocked some New Balances.
[hum8flr] (score 1, diepte 0) Currently, k-swiss tubbies. Otherwise, asics.
[humaq1c] (score 1, diepte 0) G-defyers. Great for support and stability to a little fat girl here!  Pricey but very effective.
[humpd0l] (score 1, diepte 1 OP) Just reading the reviews on these shoes and I think I'm going to try them. The rocking sketchers use to to the trick but the stopped making them.
[humq0vq] (score 1, diepte 0) I have a pair by the brand Klogs and they are the best. Not as clunky as danskos. Im afraid to wear anything porous because I'm notorious for spilling things and getting thrown up on lol
[humqys1] (score 1, diepte 0) I like brooks too, any sort of running shoe but no foam sole. That always made my heels hurt. I’ve found taking care of my body and exercising helps more than just the shoe, some leg and core strengthening helps take some of the impact off just the feet and then legs up the wall for 10-15 min before bed always helps me :)
[humy8gb] (score 1, diepte 0) I love my crocs.
[hun2gzy] (score 1, diepte 0) My Saucony tennis shoes are soft inside and uber supportive. I can't wear anything else.
[huop6db] (score 1, diepte 1) I found some that had the number 7 after them. Are those the ones?
[hunqjkr] (score 1, diepte 0) I am an odd ball because my hokas started hurting my feet after a few months of wearing them. I love my Nikes…don’t know what kind they are though
[hunsufb] (score 1, diepte 0) I LOVE my Algeria shoes, but they squeak after wearing them for a couple months and they do look a little bit like clownish which may be partially because I have big feet.
[huof1a5] (score 1, diepte 0) Brooks I love
[huojt66] (score 1, diepte 0) Saucony! I swear by them for my icu shifts.
[huokdx3] (score 1, diepte 0) I like my Ryka brand
[huomx92] (score 1, diepte 0) https://www.keenfootwear.com/p/W-KANTEEN-CLOG-SOFT.html

Keen Kanteen duty shoes. I love them.
[huooaui] (score 1, diepte 0) New Balance
[huopec5] (score 1, diepte 0) Does it make a difference if you have flat feet what brand to get?
[huotrjg] (score 1, diepte 0) Doc Martens. Used to have steel toes to deal with wheelchair tippers, but now I just have a pair of regular leather shoes. They're durable and easy to clean. The made in England ones are good quality and last for a long time.
[huov20f] (score 1, diepte 0) I swear by asics!!! I’m on my second pair. They really helped with my back pain
[huoztq4] (score 1, diepte 0) Lems
[hupisd1] (score 1, diepte 0) I have worn Brooks for the last year and cannot express how amazing they are. I put on my other tennis shoes outside of work and question how I even wear anything besides Brooks. The amount of comfort they give you along with less leg/back pain. 100% recommend
[huq295v] (score 1, diepte 0) Grey’s Anatomy Merideth Soft Walks.
[huqdf81] (score 1, diepte 0) KURU! Y'all, for real we sleeping on Kuru.

Before nursing, I was die-hard Brooks for my running shoes. But they hurt my feet when I became a nurse, and I got schooled by the folks at Marathon Sports (as in Boston) about the difference between running and standing in one spot for a prolonged period of time, and how it changes shoe needs. Got my first Hoka Cliftons on their recommendation, and that's what I used my first two years.

Then I saw an ad for Kuru and thought why not try them. Y'ALL. They have this patented thing called the KuruSole where they have slits in the sides of the heel box that causes the heel box to collapse in a round shape around your heel instead of pushing the fat pad under your heel out to the sides. Let me tell you, it is everything.

I have extremely high arches, to the point that I've always had to lace my shoes in fancy ways or my instep will go numb. And my Kuru Quantums are the first shoes I've ever owned in my entire life that I don't need to add additional arch support to. I got some Atoms too, just because they're gorgeous, but I prefer the Quantums for work.

In addition to that, I would add not rotating your shoes, but replacing them on a regular basis. Don't wait until they're worn to threads. I count my shoes as a scheduled, budgeted expense and get new ones every six months (yes REALLY). That works out to about $25/month. I just think of it as a subscription service to myself lol.

[https://www.kurufootwear.com/technology](https://www.kurufootwear.com/)
[huqn7y9] (score 1, diepte 0) Adidas ultra boost. 4 years old now holes on the top but comfortable as hell I won’t wear anything else in or out of the hospital. Even have boost hiking boots.
[huwql7l] (score 1, diepte 0 OP) Loved all the advice given. I wear compression sock but going to add cushion and I ordered new shoes. Love my Hoka for working out so going to get some for work and ordered new G defyer. Thanks everyone
[humojgg] (score 0, diepte 0) Nurses wear the most funniest shoes, when they are passing by you can notice them. I'm sorry u need to look for your shoes size!!!😊

=== THREAD 17pbe4n ===
SUBREDDIT: r/pharmacy
DATUM: 2023-11-06  SCORE: 1  REACTIES: 62
TITEL: i’m here at work and jus received an rx for oxy/apap 10/325 1Q6H prn foot pain #120 🥱
POST (source_id=post):
me personally, i feel this is too strong of a medication and too high of a frequency for foot pain.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k84a1lo] (score 43, diepte 0) Do you know what their foot pain is from? What if they have a legit injury?
[k851pdf] (score 37, diepte 2) It’s the largest tablet size but certainly not the most oxycodone you can take. 

You also have literally no idea what is happening to this person or other things that have been tried. Foot pain could mean a million things which could be crippling. The patient could have cancer with bone mets. 

Did you check the PDMP? Was this their first opioid rx?
[k852vlc] (score 37, diepte 0) So the patient went to their PCP, got referred to a pain specialist, was examined thoroughly, diagnosed, and then prescribed treatment. But you looked at one sentence on your screen and, knowing nothing else about the patient, decided the patient doesn’t need it. 

When people bitch about pharmacists, you’re the one they’re bitching about.
[k845eo7] (score 22, diepte 0) Let me guess they also didnt try anything else prior or didnt send anything else as adjunctive pain therapy
[k853psi] (score 20, diepte 2) AmazIng. The guy who is a dick to his patients is a dick on the internet too. Who would’ve imagined 🤷🏻‍♀️
[k85m0vw] (score 19, diepte 2) Dude you're a technician and you're making these judgments? You should really back off lol This is nowhere near your wheelhouse. I'm a tech, too. This is not our business, this is on the pharmacist.
[k85oq3r] (score 15, diepte 3) Thank you from a bone-mets having CPhT. Holy shit this stuff pisses me off. The sheer audacity is astounding, especially from a fellow tech.
[k855azn] (score 12, diepte 4) Advocating for patient care? That thing we’re supposed to do for a living?
[k84y2x8] (score 11, diepte 0) >7 days and >50 MME for a new condition, just say no. Unless they've been titrated to this dose for something like a significant surgery or amputation.
[k87wiaw] (score 11, diepte 0) People are pressed because there are people that are legitimately not drug-seekers and have legitimately tried non-opioid pain options and opioids might be the only way they experience any sort of pain relief. When you have chronic pain, you most likely have cycled through doctors, have had your pain dismissed, and have spent thousands (if not more) on treatments that didn't work. 

It's easy to think just because you might not need this medication that must mean a person with non-cancerous pain doesn't need it. I'd ask you to maybe spend time with chronic pain patients and speak to pain doctors that understand opioids have their place in medicine before you cast judgments about people's scripts. 

May I ask the reason you became a pharmacy tech? Do you not want to help the general public live a fulfilling life? Do you not believe sometimes the benefit(s) outweigh the risk(s)?
[k84j19f] (score 9, diepte 1) You're right, we DON'T KNOW the patient. From what's been told, the only prior med hx is that they received tussionex from the same pbr. 

Per pharmacist judgement, OP could either fill, refuse to fill and give the script back to the patient, or send out a message to Dr to clarify script. 

If I'm not 10+ pgs deep in the queue, I'd either call the dr office or have an intern be on hold for script verification. 

Namely speaking, why I wouldnt fill this, if you're not in crutches/ assisted mobility or otherwise in extreme pain and your c2 opiate script's only diagnosis is for "foot pain," I'm not buying the veracity of that script and want to talk to the doctor first.
[k85p1mp] (score 9, diepte 4) Sorry to here that, hope things are going well! 

I hate when people are confidently wrong and it is worse when they work in or around my field. OPs silence is telling
[k84x3td] (score 8, diepte 1) Believe it or not, pharmacists also went through college and received their Bachelor's often Masters and have Doctorates.

I work at a hospital and the amount of times providers rely on the pharmacy for dosing and scheduling would surprise you, healthcare is a team game.

Catching outliers, mistakes, red flags, those are the duties of a pharmacist and by extension the entire pharmacy. The tech was absolutely right to question that large of a script.

Mofine 1 pound, to go.
[k895pwt] (score 8, diepte 3) From someone with severe chronic pain who masks well and has better and worse days, thank you. It’s so discouraging to have to hope and pray that medical professionals won’t dismiss my well-documented conditions based on a short interaction and their preconceived biases. I think (hope) this particular post may be a troll post, but unfortunately this attitude exists in much of society.
[k8a5pa2] (score 8, diepte 2) Do you think that maybe he was able to walk in *because* he takes that medication?
[k84ed7e] (score 8, diepte 0) That foot better be amputated.
[k8812u8] (score 7, diepte 2) The same way you have every right to comment on a public forum means I have every right to comment.

When you post a blanket statement that lacks nuance or perspective on a public platform, then when someone raises a legit concern and you tell them to "move along and don't comment," are we being intellectually honest and fair, here? When we receive constructive criticism, should we just tell the person, basically in harsher words, to fuck off?

No one is denying that you have knowledge of medications and that you have probably seen patients of all walks of life. And it is shitty when drug-seekers have scripts for medications they do not need. I can say as a chronic pain patient it's even shittier when we are denied medications that actually relieve our pain, and all we are trying to do is live a "normal" life.

I am very well aware that medications have different effects on people. Maybe I will stop being "so gullible" when you gain some perspective & don't let the bad patients cloud your judgment of the good patients.
[k85uj8b] (score 6, diepte 4) You're the one who started a whole post about something you know NOTHING about and is none of your business. Just do your job and stop judging people.
[k8762y9] (score 6, diepte 5) I have crps in my foot and I walk in just fine. 

I absolutely know I get judged when I get my pain medications because I "look fine"
[k88o72i] (score 6, diepte 2) There’s a good chance they can walk like that because their pain is well controlled. God forbid!
[k89kk9x] (score 6, diepte 0) Well it's a good thing you're just a tech and not a pharmacist so stfu and just do your job. Id tell you to kiss my ass and get you fired if you fcked with my pain script I need for chronic pain. There are people like you who don't know where the details of your job begin and end and whether or not someone needs it is definitely outside of those parameters. If I ever found out any techs were lying to me about my meds I would have you fired and take legal action.
[k876ce6] (score 5, diepte 2) I have crps and walk in just fine. So I guess you would deny me my medications. 

Sadly my foot looks like [this](https://www.reddit.com/r/medizzy/s/ehr9cyfRwG)
[k8956nj] (score 5, diepte 0) Bro stfu and don't be a judgy cunt. I worked as a tech and I have health issues. It's not your fucking call for a reason
[k8apxi7] (score 5, diepte 0) What a judgy piece of shit tech
[k85ahkl] (score 4, diepte 1) Are you a pharmacist? You do realize that pharmacists have responsibility, both ethically and legally, when dispensing opioids? And that we are a member of the Healthcare team? There are guidelines surrounding use of opiates. Giving a patient a starting dose >50 MME is not appropriate.
[k84ylvh] (score 4, diepte 0) He is probably allergic to ibuprofen
[k85444d] (score 4, diepte 4) *I came looking for booty.*
[k85m417] (score 4, diepte 1) This person is a tech lol
[k84fb5c] (score 3, diepte 1) Post/comment removed. Users who are active in subs that support the illicit acquisition or use of controlled substances are not welcome in this sub.  Users asking how to acquire controlled substances illicitly or otherwise controvert the law will likewise be banned.  Posts that take a permissive view toward the illicit use, trafficking, or production of controlled substances will be deleted.
[k8461s4] (score 3, diepte 1 OP) of course not and then the same person jus brought in a tussionex rx.. these doctors irk me somtimes
[k8966gd] (score 3, diepte 7) Again, you started at a lower dose and titrated up, as is appropriate. Sounds like your doctors did it right and there are no flags here. Prescribing initial high doses of Percocet and also Tussionex at the same time from the same provider is red flag city.
[k8cu42j] (score 3, diepte 3) This right fucking here. My pain is WELL MANAGED, WITH my meds. Without them I promise I'll be filling out disability paperwork. But I don't want that. I want to be treated, I want to have a good quality of life. I want to be able to go do things with my 8yr old son. His mother is worse than I. Her pain is not well managed. In order for her to be able to go do anything (take our son to a county fair for ex.) She has to make sure she doesn't do anything strenuous the prior couple days, then after ONE day of walking around, she has the next roughly week of crying and barely being able to move without her walker. So fuck this bitch ass tech, and fuck all the rest of the pharmacists and worthless judgemental doctors. Those are the people I wish pain on. Go through what some.of us go through and I PROMISE you'll be singing a whole new tune.
[k8axj3l] (score 3, diepte 2) And who are you to decide what treatments are appropriate for which patients?? Isn’t that the freakin’ doctor’s job?!?!
[k89kkdg] (score 3, diepte 0) That's what I was taking post cervical fusion. But there's so many variables to determining what someone's dose should be. 

No one can look at this information provided, and make any level of accurate assessment. So it makes sense to go with doctors judgement here. 

Logically, ethically, and morally. But let's keep trying to make BS claims about a standard dose being to much.
[k8a46ek] (score 3, diepte 0) This type of judgment is unnecessary. Every joint in my body is bone on bone & I look fine to 99.9% of people,  including my family, because I've learned to mask to make YOU all feel comfortable! All society does is judge, judge something that they know nothing about. Sickening abelist society. 
Karma has a way to coming back at those who judge others and I hope you remember this when it does!
[k8ab3gw] (score 3, diepte 0) You know nothing and have no 1. Experience  2. Theoretical knowledge. 

Do your f. Job. Make the pills. And keep the mouth shut.

Any issues ring the prescriber, not reddit.
[k8bmv2l] (score 2, diepte 2) It's as though these doctors have more to understand about their job than you do, having mastered only your own.

You have a job because people come to you for your expertise, not your opinion on icecream flavours. If you're concerned, call the doctor, then do your expertise, there is no need to be a bitch to vulnerable patients.
[k8aem8e] (score 2, diepte 6) You should be dismissed from your job. You're obviously not doing it.
[k88kgtj] (score 2, diepte 4) I went from percocet 5 from a podiatrist straight to fent 25mcg from a pain management after he referred me to them.  

Hope you save some lives!
[k8959no] (score 2, diepte 5) So you admit that you started on a lower dose of opiates than the patient in this scenario is.

Please understand that healthcare is multifaceted and opiates are extremely addictive. The lower dose you can be on to control your pain the better. There is no reason to start someone who is opioid-naive on >50 MME per day.
[k8ke746] (score 2, diepte 9) You would be able to figure that out via PDMP.
[k880bjh] (score 2, diepte 2) Remain civil, interact with the community in good faith, don't post misinformation, and don't do anything to deliberately make yourself an unwelcome pest.
[k8ct5bq] (score 2, diepte 0) Yo. Let someone blast you in the barefoot with a hammer. Please let them. also who tf are you to judge their pain. It's cocksuckers like you making my life as a chronic pain patient fucking miserable. Because I don't look like I'm in pain, I must not be right? Fuck you.  Judgemental underqualified bastard.
[k8dofpx] (score 2, diepte 1) Amen my dude! Chronic pain sufferers unite!
If i could add to the OP: get someone to hit you with a sledgehammer to to back n see how ya like that. Or just jump off a roof and fuxk up your back and leg completely. Then go nicely to get some miracle medicine ibuprofen from your nice little pharmacy and hand in yo 2weeks notice. (Can say from almost decade of experience that having a totally fucked up back + 3 fractures in leg that the sweet ibuprofen doesnt do shit) neither does oxy. NOTHING CURES THE PAIN. THERE. IS. ALWAYS. SOME. My first time gettinc 200ug fent in ambulance, that barely took the edge off from my worst possible pains. JUST THE EDGE and only for several hours.. Go bitch about yo judgy ass to fb or some shit. Go to the hospital judge the docs. Shit anything else, but an innocent pain sufferer thats a fucking low blow. Sure i dont know the customer either how do i know he or she is innocent blablah.
[k8gk4xx] (score 1, diepte 2) Because someone cannot have chronic pain for years and also get a virus at some point? I take pain meds for years. At some point, I will need to get cough medicine after filling my meds. 

I will say though, this one DOES sound a little odd. Tussionex is an odd option to pick for someone you just prescribed percocet to. 
However, the answer is to do your due diligence and call the doctor to validate the rxs are BOTH legit, check the PDMP for other suspicious fills, see method of payment (cash or insurance?), ask the patient some questions just to get more info about the needs for both meds, etc.
[k8euxz7] (score 1, diepte 6) I'll dig up where you work and make your life 'fun'
[k888ddi] (score 1, diepte 4) Remain civil, interact with the community in good faith, don't post misinformation, and don't do anything to deliberately make yourself an unwelcome pest.
[k88d8dq] (score 1, diepte 3) Per my comment, if you come into my pharmacy with basically 0 med history with only a new Rx for a 30ds of a c2, I'm gonna need to verify with the doctor. Different story if you have a history of C2 prescriptions. 

Couple of questions: what's the ICD code on your prescriptions? Did you take anything else for your crps before moving onto opioids? 

If the Rx has the ICD code for CRPS and I see you've gotten a non-controlled pain med in med profile, then you're going to the waiter queue and I'll be on hold for the doctor's office. 

If not, you're gonna have to wait for me to finish some of the things on the queue before I can contact the doctor's office or hope I have an intern I can use instead.
[k88mdge] (score 1, diepte 5) Great! You answered some of the questions I had for the doc/ prescriber since you didnt have the ICD code and didn't have any non-controlled med history. 

The doc was prescribing within scope (podiatry (specialty care) with referrals to pain mgmt) and the doc prescribed you perc 5 prior to perc 10.
[k895ltk] (score 1, diepte 6) This was 6 years ago and nothing happened.  

If multiple pain management doctors did it for physical therapy I don't see the issue.
[k8jz5i5] (score 1, diepte 8) I glad you double check with the doctor and I see your point, but maybe he was using another pharmacy before yours. Was judged and refused the upped dosage so he came to your pharmacy.
[k8c3r8i] (score 1, diepte 6) My MME is 4320.  It took me a while to get there but this MME 90 limit is insanely low for opiate tolerant people. A stupid arbitrary number created by one man
[k8cgdhj] (score 1, diepte 7) The point is this is not an opioid tolerant person.
[k8ckcz5] (score 1, diepte 8) How do you know? They told you so?
[k8crgxv] (score 1, diepte 9) It was mentioned in a comment. I obviously don't know for sure as this is not my patient, but my comments are under the assumption that this is the initial dose on an opioid naive patient, if I did not already make that clear enough.
[k8cdfkz] (score 1, diepte 3) As a fellow CRPS sufferer, I feel your pain. I do have a limp and how noticeable my limp is is circumstantial. Some days it's mild, other days it's extremely obvious. It's hard enough dealing with the condition, having people judge you is absolutely downright horrible.
[k8jy8dw] (score 1, diepte 2) I suffer from severe pain in my legs due to an extremely rare deformity; I have suffered with this since I was 12 years old. I have learned to mask my pain because ppl got tired of hearing about it. I started with otc meds when I was younger and would get codeine when my hips and knees would dislocate just from putting my socks on (which happened daily). As I got older, the pain got worse as my ligaments and tendons, when the dislocations started cutting them. So, if I came to your pharmacy with the meds I have been on for years now, you would refuse me if I didn’t come in using a wheelchair or walker? I have worked hard to get out of my wheelchair and walker and only use my cane when I know I have to walk a lot or walk on uneven ground. You need to rethink your profession, it. Is pharmacist like you make ppl go to multiple pharmacies just to get their meds filled to get the relief, even if it is just a mild relief.
[k8k9cas] (score 1, diepte 3) In your situation, as you've been "using these meds for years," you would have a patient profile that has your patient medical history. So I don't see a problem here. 

If you don't have a PMH with the pharmacy (as all chains do share patient profiles), then I'll treat you as a new patient. 

To make my my previous comment as simple as possible, if you are a new patient coming into the pharmacy, then I want proof. 

If you don't give me proof, then I am calling the Dr to verify the Rx. 

If you don't want to wait for me to verify the Rx with the Dr, you can take your hard copy C2 prescription back.
[k90wz74] (score 1, diepte 4) That make sense. OP of this post is being judgmental of the patient here and that is what most of us are mad at, because we already get judged by other people, doctors, clinics etc.
[k8jrnw0] (score 1, diepte 3) Thank you, I’m glad you wouldn’t have a person like this in your pharmacy.
[k86sbm5] (score 1, diepte 2) do you also question people in disabled parking spots if they don’t have a visible disability?
[k8az9xa] (score 1, diepte 2) You do know these medications increase sensitivity and decrease threshold ?

Have you heard of tolerance ?

The tablets you make are designed to be a bandaid, not a cure.

They will always make it worse in longterm.

If you want to be a pain specialist, you did the wrong course.
[k8giwsh] (score 1, diepte 2) Have you ever thought that maybe the reason they are able to walk in is because the med is actually working? Not all pain is going to be visible. Actually, most is not. You won't see all pain patients in wheelchairs and on crutches. 

I wonder if maybe they have more than one pain area and the doc just put foot on there. 

I think with this one you just have to give it extra scrutiny and look up the PDMP for sure, and maybe call the doc who wrote it just to cover your butt and ensure you did your due diligence.
[k84nabq] (score 1, diepte 1) Above threshold and not accepting new patients.
[k84nvg2] (score 1, diepte 0) Man, they gave me less for a broken back.
[k8omxb0] (score 1, diepte 1) No one believes you.
[k8ov3t2] (score 1, diepte 2) Even with the imaging. It’s annoying. It’s more, ik it’s excruciating but I’m not comfortable because it’s not cancer. So.
(26 reacties met lagere score weggelaten)

