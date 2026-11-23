# Label-batch batch_0125

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
Schrijf het resultaat naar `batch_0125.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 3mn7m7, r3m0l6, 1dkt4h0, 1937pit).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 3mn7m7 ===
SUBREDDIT: r/BuyItForLife
DATUM: 2015-09-28  SCORE: 118  REACTIES: 68
TITEL: [BIFL Request] Boots/shoes for being on my feet all day?
POST (source_id=post):
What is this? Yet another boot request? Yes it is. I am looking for either a pair of guys boots or shoes (personally leaning towards boots) that won't leave my feet aching after a long day on my feet at my job. I usually walk around non-stop (sans breaks and lunch) for 8 hours a day, 4-5 days a week.

 I say I am leaning towards boots because sometimes one of my ankles gives me a fit after a day or two of walking on it, and a high boot with plenty of ankle support should help a ton. I checked the sidebar and didn't fall in love with any of the boots on the list. In my case its function over form so military boots (8-10 inch boots) are going to be a million times better than a pair that barely covers my ankle.

So, any of you guys/gals have a suggestion for me?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cvggkov] (score 18, diepte 0) On mobile, so this is likely to not come across right, but there was a thread I saved for the next time I was in the market for new footwear:

http://www.reddit.com/r/LifeProTips/comments/2z5l3j/lpt_servers_chefs_teachers_retail_people_etal_how/
[cvgrdfx] (score 12, diepte 3) The quality has become absolutely atrocious. It's not what it used to be.
[cvgr1q9] (score 11, diepte 0) Dansko XP. They're made for working, not great looking, but you see people wearing them who are on concrete floors all day. I've had a pair for a year and a half and used them pretty heavily, they've been incredible. I have problems with my knee/hip/back so something very comfortable and supportive was essential. They're nonslip, rounded to rock naturally with the foot, and hold up. Honestly well worth the investment.

These are the shoes surgeons wear in 20+ hour surgeries, the ones nurses swear by, the ones veterinarians and basically anyone who's on their feet all day and on hard flooring goes with. I got my sister in law a pair after she was complaining of her back hurting after standing all day- she's a hair stylist. They're not cheap at about $150 a pair, but WELL worth it. Also, check REI for them for a better deal. 

I also HIGHLY recommend investing in some Asics for tennis shoes if you go that route, the gel is incredible. If you go for those though, a word of caution- I wore them for years and finally bought my mom a pair, she hated them at first... and after an hour she loved them and has been a convert ever since. Trying them on in stores isn't great, the gel takes a bit to heat up and then you're gold. These, too, are the shoes of surgeons. My orthopedic surgeon and I bonded over our mutual serious love of asics and how often they're worn by medical professionals. They're also not cheap at about $120 a pair but they're the best athletic-style shoe available for long-term wear.

I had a knee replacement and several problems with my pelvis/hip/spine after a bad wreck. I have trouble with those still and had to have some great shoes to help me survive long days. Those two brands I can't recommend enough. That said? THERE IS NO SHOE THATS BIFL REALLY. Sorry, no. They wear down and have to be replaced after a while. The Asics will get holes and the tread wears down, the Dansko's start showing it. I really believe both last a rather long time, but not forever. Sorry. They're still beyond worth it.
[cvgrms3] (score 8, diepte 4) Really? I wouldn't know I've had mine since the 80s
[cvgjcjn] (score 7, diepte 1) \#1 tip there is to make sure it fits. If you're on your feet all day, go to a professional, not a wal-mart (no offense OP) shoe department.
[cvgj99g] (score 6, diepte 3) Solovair has emerged as an alternative to Doc Martens with better construction, same styling, and for not too much more either.

Red Wings are a maybe. Their workboot line is alright, but most of the stuff in their heritage line is uncomfortable (barring the Postman).
[cvgiliw] (score 6, diepte 0) What is your occupation? 
Different shoes for different jobs.
[cvgisl7] (score 6, diepte 1 OP) I work at walmart, I am mainly on the floor walking all day, but it is fairly common for me to find myself working in the back moving freight when they are short on people.
[cvgpfir] (score 6, diepte 1) Ive got the same shoe but keep in mind that minimals arent very durable. It is super comfy amd my favorite shoe but my last pair lasted maybe 6 months before a hole on the mesh developed. The soles are fairly worn as well(at 9 months) By their nature they can't be resoled and i wouldnt know about the mesh. Ill note that i wore em all the time for work, exercise, hiking. Youd get more miledge(sp) if you bought a few and swapped them out. I think I got em for ~$90.
[cvgi9pv] (score 5, diepte 2) For the love of all that is holy do NOT get Bates boots. I can't comment on the others mentioned here.  Personally I wear dr martens which are quite comfy once broken in and feel quite durable but many here say they are no longer bifl.  I would check out redwings if you want something to last.
[cvghmmn] (score 5, diepte 1 OP) Guess that would be something important to state...Male
[cvgrqaq] (score 4, diepte 5) Ah, that makes sense. 

Doc Martens used to be great, but they outsourced to China in order to lower their prices. Not worth it anymore.
[cvgsxft] (score 4, diepte 6) Get Solovairs then, they make the "oldschool" Martens
[cvgo7wr] (score 3, diepte 3) From what I've seen, the Dr. Martens Made in England line is the same as their original boots.
[cvh8shn] (score 3, diepte 2) This is going to sound dumb but who exactly would be a professional shoe person? I suppose I've never trusted the people at shoe stores to actually know anything other than whether they have a certain size in the back...
[cvghwpm] (score 3, diepte 2) Ah. Darn. I only know ladies shoes.
[cvgj3mw] (score 3, diepte 0) [Lems Primal 2](http://www.lemsshoes.com/mens-primal-2-black.html) - super light, spacious, and minimal. I've had my Primals for several years and they're my favorite.
[cvglbox] (score 3, diepte 1 OP) $200 is probably my max, non-slip would be nice but other than that there are no official requirements. The main things I am worried about is my ankles and feet being taken care of.
[cvgn8n3] (score 3, diepte 0) Also look at keen.
[cvgphpu] (score 3, diepte 0) I'm not sure about shoes, but if you ever need replacement insoles, [these were pretty good for me.](http://www.amazon.com/Spenco-Polysorb-Heavy-Womens-11-12/dp/B000G1IL7M/ref=sr_1_2?ie=UTF8&qid=1443429801&sr=8-2&keywords=spenco+polysorb) The 10-15 dollar insoles at the grocery store and Wal-mart never help, but these did.
[cvgphtc] (score 3, diepte 1) **Spenco Polysorb Heavy Duty, Women's 11-12 / Men's 10-11** 

||||
--:|:--|:--
Current|$15.40|Amazon (New)
High|$16.97|Amazon (New)
Low|$11.62|Amazon (New)
|Average|$13.43|30 Day

[Price History Chart and Sales Rank](http://i.imgur.com/x3PxZ02.png) | [FAQ](http://www.reddit.com/r/PriceZombie/wiki/index)
[cvgriog] (score 3, diepte 1) Can confirm-- wife is an anesthesiologist and swears by then. Not sure if they're made for men though.
[cvgre4x] (score 3, diepte 0) Redwing Iron Rangers

You do have to break them in and allow time for the insole to mold to your foot. But after that they fit like a glove!
[cvgwlzj] (score 3, diepte 0) Thourogood boots are some of the best for being on your feet all day. Seriously comfortable and not bad looking.
[cvh3yxj] (score 3, diepte 0) The classic Doctor Martin?
[cvggkhf] (score 2, diepte 1 OP) Thanks! I will definitely check them out.
[cvgqpil] (score 2, diepte 3) Why the recommendation against Bates? I have 3 pair that have always been excellent for me.
[cvhisks] (score 2, diepte 4) I've had pretty terrible experience with them.  They're standard issue navy boots which fall apart if you look at them the wrong way and are way uncomfortable.
[cvghctn] (score 2, diepte 0) Male or female?
[cvgtjyj] (score 2, diepte 3) You can still comment on ladies shoes!
[cvgkwzk] (score 2, diepte 1 OP) A lot of these boots look really nice, but here in Texas it stays too hot for leather boots (for me at least)
[cvgq8zs] (score 2, diepte 0) I am wearing ankle-high boots made by ecco right now. They are relatively affordable (90€ in my case) and their receptor sole technology is brilliant. In addition they are fairly light for boots, made from real leather and really tough. Buying shoes is probably never "BIFL", but these will last me some years to come and I own them for a little over a year now, with several other shoes from ecco that I love as well.
[cvh4fk8] (score 2, diepte 1 OP) Yeah, I know there isn't a shoe that is BIFL by itself, but my definition is a shoe that lasts long enough and is comfortable enough that I wouldn't hesitate buying a replacement pair.
[cvgybdm] (score 2, diepte 2) Also awesome boots! I prefer the Iron Rangers for their stitched toe cap.   

It's worth noting that the IR have a smooth tread (no lugs) but I find them perfect for everyday, light duty work. I've seen people get new treads put on them if necessary.
[cvggely] (score 1, diepte 0) Since you mentioned military boots, I'll give my recommendations. I would say look into Bates (military mixed use, lots of styles and fits), Matterhorn paratrooper boot (basic military boot, lightweight, comfortable), and Rockies (similar to Bates). I have personally worn all of them and I'd say Matterhorn and Bates first. My dad is former infantry and he says Matterhorn or Rockies. Hope this helps!
[cvhj0mt] (score 1, diepte 5) Perhaps it's issue boots that are no good, I've found everything I've ever bought from them to be very high (10+ year) quality, comfort is subjective though.
[cvh6cxg] (score 1, diepte 2 OP) I would go to a professional shoe person, if there was any within two hours of me.
[cvh6f71] (score 1, diepte 3 OP) Yeah, feel free to suggest some ladies shoes. Maybe someone will stumble across this post looking for suggestions.
[cvgvsvj] (score 1, diepte 4) Buy vintage.
[cvhfvif] (score 1, diepte 4) There is still a made in england line that is basically same as the old ones IIRC. You just have to pay up.
[cvgniad] (score 1, diepte 1) Those look great!
[cvgkuju] (score 1, diepte 0) oslo boots are the shit but they are more for hiking.  I had to resole one a while ago but the things fit like no other shoes i have.
[cvgl0d9] (score 1, diepte 0) I have a pair of Danners "Williams" boots that I love, but they are a bit hard in the sole for all day on your feet.  Danner also makes military style boots, I would venture to say the American made ones are going to be well made like red wings. They have a discount club, PM me for a link if you like.
[cvgl9i9] (score 1, diepte 0) What's your price point? What kind of safety features do you need?
[cvgn9fi] (score 1, diepte 0) Merrell's Realm Lace has been good to me. They also have a boot version, which I also bought. Both are comfortable and look nice but I don't have enough wear on the boot version to recommend them yet.
[cvh4ieh] (score 1, diepte 1 OP) Yeah, I know shoes aren't going to be actually BIFL, but my definition is a pair that lasts long enough and is comfortable enough that I wouldn't hesitate buying a replacement pair.
[cvhbxf7] (score 1, diepte 2) See my above recommendation, that brand makes nothing but outstanding quality shoes, without the insane price tag that comes with most hiking boots.
[cvhdrlx] (score 1, diepte 2) Both asics and dansko have men's shoes!
[cvhfus3] (score 1, diepte 2) Nurse here - they have mens shoes.
[cvgt67c] (score 1, diepte 1) or wolverine 1000 mile shoes.  

I consider them on par with eachother, and it boils down to style preference
[cvh00hp] (score 1, diepte 3) I went with the wolverines since they had EEE sizing.

I would love to eventually get a pair of iron rangers but I'm not sure if its possible since their sizing is a bit slim width wse
[cvhkmqo] (score 1, diepte 4) I got an 11 EE IR. I have a wide foot. Not sure about EEE. I didn't know that was a thing.
[cvh2qre] (score 1, diepte 1) Can confirm iron rangers. Im wearing my worn in pair today and they are comfy as fuuuuuu
[cvieim5] (score 1, diepte 1) I bought a pair of redwings for working in a factory with concrete floors about 3 months ago, and I still haven't managed to break them in.  one 11 hour shift, and they break me in every time I try.    I've taken to wearing them on my off days to tey and ease into them, but it's taking a substantial amount of time.
[cvgszhk] (score 1, diepte 0) If it Flys with your place of work, birkenstocks have solved basically all of my footwear problems. If not, I've had some good experiences with Merrell shoes and boots
[cvgtnc6] (score 1, diepte 0) These [Blackhawks](http://www.amazon.com/Blackhawk-Mens-Warrior-Desert-Boots/dp/B001I26A1C/ref=sr_1_1?ie=UTF8&qid=1443445386&sr=8-1&keywords=blackhawk+boots) are my go-to duty boot. I've spent 42+ hours wearing them on my feet non-stop, I've never had an issue with them. They're comfortable, light, breathable, and durable. I put my boots through hell, and I've never had a separating sole or torn fabric or broken lace on these boots. I've only ever replaced them because they got dirty beyond what cleaning could fix and still look professional, or I've worn the soles down slick. Great buy, in my opinion.
[cvgtnhs] (score 1, diepte 1) **Blackhawk Men's Warrior Wear Desert Ops Boots ,Desert Tan, 10 M US** 

||||
--:|:--|:--
Current|$110.56|Amazon (3rd Party New)
High|$159.99|Amazon (3rd Party New)
Low|$49.99|Amazon (3rd Party New)
|Average|$116.77|30 Day

[Price History Chart](http://i.imgur.com/zbTEcUW.png) | [FAQ](http://www.reddit.com/r/PriceZombie/wiki/index)
[cvgxkzt] (score 1, diepte 0) I always go to Blundstone.

http://us.blundstone.com/adult-boots/558-black-super-550-series
[cvgzu54] (score 1, diepte 0) [These](http://www.amazon.com/Thorogood-Plain-Toe-Boot-Gladiator/dp/B000I7FS8O/ref=sr_1_8?ie=UTF8&qid=1443456505&sr=8-8&keywords=thorogood+american+heritage+boots) are the most comfortable boots I've ever owned. I've spent 12 hours on cement and ladders after which my feet felt great. The only downside is that the reason it's so comfortable is that the sole is soft so it will wear down quicker than average. Thorogood boots with a black wedge sole are harder so they'll last longer and they're still comfortable.
[cvh48r2] (score 1, diepte 1 OP) ohhh, those are some good looking boots, Ill have to put those high on my consideration list.
[cvh60w3] (score 1, diepte 2) I have some black soled Thorogood work boots I wear when I motorcycle. They are comfortable, rugged, and breathe enough to wear in Louisiana summers.
[cvj7rhj] (score 1, diepte 0) If you can have a look at R.M. Williams boots the last a good few decades and are really comfy
[cvxyrby] (score 1, diepte 0) A bit late, but I would suggest looking into insoles, as well. I note you are working in a walmart, and they generally have some in the pharmacy area, but I would say *don't* go that direction. Go to an REI in your area, and they will generally have Superfeet insoles. Superfeet, especially the greens and oranges are really popular among backpackers, and for good reason.

I had a problem with being on my feet all day on concrete (Started getting pretty sore under the heel), and it was mostly due to no arch support in my shoes anymore. I'm of the philosophy that you can have all the cushion you want, but it won't do diddly squat if it isn't shaped right. I'd rather have a hard sole that is shaped correctly, than have a cushiony foam that will wear out in a few months.

I ended up getting a bigger pair of greens than what fit my feet around the perimeter, but the arch was perfect. Just trimmed with a pair of scissors and I haven't had any problems since.
[cwlghwm] (score 1, diepte 0) Try [palladium boots](http://www.palladiumboots.com/men/footwear) . I bought these boots a few months ago and am extremely satisfied with them. Quality is great, they're super stylish. Great for everyday use and in all weather conditions.
[cyhpp2y] (score 1, diepte 1) My SO bought a pair about a year ago, and the fabric above the heel has completely ripped open. Disappointing, to say the least. He won't be buying their product again.
[cvh09jp] (score 0, diepte 1) Except that it's his ankle that gives him problems so he wants ankle support.
[cvgmuoe] (score -1, diepte 0) DOC MARTENS!!!
[cvgsf6u] (score -1, diepte 0) Allen Edmonds
[cvgmv9j] (score -10, diepte 2) doc martens doc martens doc martens. Very popular with mailmen in the 60's and other people who walked all day. Even though they are boots they are very comfortable

=== THREAD r3m0l6 ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2021-11-27  SCORE: 36  REACTIES: 68
TITEL: How do you maintain your weight while on your feet all day?
POST (source_id=post):
My husband asked for my help because he struggles immensely with keeping weight on especially during busy times at work. He’s training to be a sous chef at a very busy place and works long hours.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hmbkjr0] (score 65, diepte 0) This is honestly so wild to me because I can't fucking lose it. I eat like a fucking garbage disposal the minute I get home because I haven't eaten all day
[hmbc4pq] (score 45, diepte 0) Snack cakes and weed.
[hmbe48b] (score 25, diepte 1) That's a low key flex dude, you'll be glad when you're 80 and pushing 300lbs.
[hmbcoy2] (score 22, diepte 0) If you find the answer, please let me know. I've been the same weight since I was 18 despite trying to gain. I'm now 34
[hmbdu53] (score 13, diepte 0) My partner is a sous chef also and a few years realized he had dropped a bunch of weight accidentally (same reasons you mentioned long hours, and no interest in making a meal for himself when he got home after a shift, before we lived together). He started drinking protein shakes specifically designed to add mass. Like super calorie and protein packed for bodybuilders.
[hmbpxbg] (score 13, diepte 0) The only answer to this question is eat more. Upping caloric intake is the only way to put on weight. There are no shortcuts to this.
[hmbumo2] (score 10, diepte 2) Really isn't mate. It's a massive sticking point for me. I'm a scrawny git that's tried to put weight on and gain muscle for years, but really struggle to. In the lockdowns I managed to put on a stone but lost it again 3 weeks after being back at work
[hmc3baq] (score 9, diepte 3) Smoothies, they're delicious and can be as many calories as you can fit in a blender.  You can drink 3k calories in 3 minutes.  I make one with whole milk, PB, oats, banana, berries, and protein powder. 
It tastes like a milkshake.  Exercise, heavy weight lifting.  Muscle adds the most weight for density.  Look for high calorie, nutrient dense foods.  Mung beans, chicken(I do thighs cause they're cheaper), basically any legume.  It's not easy and you have to make sure to eat even when your not hungry.
[hmbbsbn] (score 7, diepte 0) Hot dogs.
[hmbjpkp] (score 6, diepte 1) Lmao yes.
[hmd0wc2] (score 6, diepte 4) Being underweight isnt any better than overweight. Especially as a guy it can be emasculating to be constantly pointed out as skin and bones while everyone else talks about how lucky you are you arent overweight.
[hme3emn] (score 6, diepte 1) Try to eat throughout the day if you can. I used to be like that. I wouldn't eat for 12 hours then finally have something at 2-3am, and I was skinny as shit. After so many hours (6 I think) your body starts eating your muscles to survive, making you more skinny.
[hmeuwta] (score 6, diepte 2) I was trying one meal a day for few months and you definitely can gain muscle and lose fat that way. It's about calories
[hmbutu5] (score 5, diepte 3) Again, some people would kill for your metabolism, I would be one of those people.
[hmbfmwq] (score 5, diepte 0) Vegan meat and quinoa. 
It helps with nutrient and weight gain 
Add some fatty ice cream too
[hmbinnp] (score 5, diepte 0) Meal shakes before (and depending on how fast you can down them, during) work does fucking wonders. Especially since getting burnt out and bitchy from overheating/sweating/headache from too much energy being used can be negated with it. 

I'd recommend huel since their RTD shakes are good but they're upping all their prices out the ass so fuck huel
[hmfcl4b] (score 5, diepte 3) That must be a really big meal
[hmbqqib] (score 4, diepte 0) Grazing. Eat throughout the day. A bit here and a bit there. Whether it's something on the line or snacks/meals you bring from home.
[hmbrftw] (score 4, diepte 0) What? Am I the only one who gains ungodly amounts of weight when they work?  I went from 148lbs to 205lbs in 4 years. I eat constantly.
[hmbypxj] (score 4, diepte 0) I'll explain what's worked for me, I'm in las vegas at the second highest grossing restaurant on the strip(mentioning because it's busy) 10 to 12 hour days. 
Morning wake up slam 32oz deli of water. Two scoops of soylent or huel+one scoop of protein powder(rotate flavors) or heat up meal prep.
Me and my crew eat family meal or go to the employee dining room together before service.
During service we burn through about 100 tasting spoons between me and other expo chef. 
I'll eat with the wife when I get home then go to the gym. If you aren't a healthy person you won't last in this field if you're really pushing. 
Hydration is the hardest part for me.
[hmca57l] (score 3, diepte 1) Yes!!! Buy the mass gainer powders, basically just protein powder with added dextrose for carbs too!! Yes, it’s not as ideal as eating real food, but OP obviously needs a quick easy way to get in lots of calories and this supplement would be great!
[hmbnkbi] (score 3, diepte 1) Why do vegan does help
[hmbn3of] (score 3, diepte 0) Beer
[hmbrw6q] (score 3, diepte 0) If he can’t eat, can he get a couple of protein drinks down per day? That would be better than nothing.
[hmc6ekl] (score 3, diepte 0) As a Sous Chef the best way to maintain a healthy weight is to eat before work, even if you need to smoke first, pack a lunch, (sandwich with your choice of meat, lettuce, tomato, onion, pickles, etc.) grab a yogurt and trail mix of some sort, this will help when you are hungry but also don’t have time to make your food. Also I would suggest a cut off point for eating for example if the kitchen closes at 11 I would stop eating at 10 and not eat when I got home. It will keep you from gaining weight due to going to be on a full stomach. In a nut shell it’s best to plan ahead. Prepack lunches and meal replacements. Make eating a priority.
[hmd28kl] (score 2, diepte 6) Exactly. As someone whos been on both sides of the coin its not fun on either. I hate seeing comments about “how lucky you are” just because you handle things differently than others.
[hmd0qe9] (score 2, diepte 4) Thats complete bullshit
[hmdfl7g] (score 2, diepte 3) Ok so here's the thing, anyone who says they "eat enough" and "never gains weight" is NEVER telling the truth. If you eat enough you WILL gain weight. Either one of two things are happening. You are either not eating enough (no true calories/ fast food, sweets, lots of sugar products) OR you have a serious health problem. The obvious answer is that you're not eating enough. 


Secondly, you NEED to work out minimum 3 to 5 times a week. If you want to see any weight gain you MUST stick to a strict diet AND workout routine. No laying around on days off. Days off are gym days. You must make time to go to the gym and lift HEAVY weight. You MUST give it your all at the gym to see any results. I was the same exact way and always wondered why I didn't gain any weight despite "eating a lot".
[hmcyzbt] (score 2, diepte 2) Uhh... What? Lol
[hmbpi4s] (score 2, diepte 0) I have this issue. Like someone else said here, protein shakes. I throw fruits and veggies in there too to make sure I’m getting my vitamins. Good to add some avocado, pb or flax oil too for healthy fats. I keep nuts, beef jerky, dried fruit and cheese on hand to gobble down when I have a moment. Then I’ll eat an easy meal when I come home, like a sandwich or soup that I’ve prepared and frozen.
[hmc87aj] (score 2, diepte 1) Work at a more demanding job. At my second restaurant I was eating fried chicken, pasta and cream sauce pretty much every day while snacking on the line and never exercised once but managed to lose 50lb in 9 months just from the intensity of the work. But yeah in every other place I've either maintained my weight or gained a few pounds.
[hmbv88e] (score 2, diepte 0) I eat one gigantic meal at the end of the day. And while I’m working I use THC, nicotine and caffeine for fuel
[hmbwzsf] (score 2, diepte 0) Lol I have the opposite issue. The first year I started cooking in a pro kitchen, I gained like 25 #’s and 30 the following year. Been fluctuating +/- 10 #’s since then.

The only thing that changed from before was that I drank more alcohol and exercised less. Ate things with more “flavor makers” such as fats, starches and salts. Since I, you know, discovered what makes flavor.
[hmdf1te] (score 2, diepte 0) I retired 6 months ago and have put on about 25 pounds, I feel like I’m carrying a sack of red onions around.
[hmes2bb] (score 2, diepte 0) I know in some regard everyone in the industry has experienced weight fluctuations, but it’s going to vary significantly from person to person based on several factors:

• metabolism/personal biology

• type of cuisine/calorie intake

• alcohol intake

• amount of ground to cover

• heat level

At some jobs I gained weight because I didn’t have a lot of ground to cover, or the cuisine was very butter and cream heavy. At some jobs I lost weight because there was so much ground to cover, and I ended up walking over ten miles a day. I’ve experienced worrisome weight fluctuations in both directions due to stress alone; once the source of stress was eliminated my weight stabilized.

One might gain weight when working in pastry, one might lose weight when cooking on a wood-fired hearth or French top stove. A laid back owner might feed the kitchen booze all night, creating habits outside of work that increase weight gain. A tight knit kitchen crew might drink together after every shift, taking in tons of empty calories. And finally, exhausted kitchen employees often eat garbage after work because they don’t feel like cooking for themselves, so after a few months of fast food and frozen dinners you’ll see the weight start to come back. (If you’re an owner and reading this, let your kitchen cook themselves a nice FREE meal every shift)
[hmiivzs] (score 2, diepte 0) When I was in a similar situation I was able to return to a healthy weight after a few months when I focused on adding healthy fats to my diet. A few of my go-to's:  a baggie of mixed nuts or a scoop of peanut butter (they sell grab and go packets of peanut butter at my grocery), a protein bar stashed in my apron that I can scarf a bite from when I have a second, a protein shake or smoothie in my locker that I chug when I have a few minutes to spare, mixing cottage cheese into my scrambled eggs, switching to full fat vs nonfat yogurt, and (if they're on sale) avocados... I cut one in half, sprinkle on lemon juice, salt, pepper, and eat it with a spoon for a two minute breakfast.

Of course your husband's mileage may vary-- and your/his doctor might have suggestions too. Best of luck!
[hmkm34y] (score 1, diepte 1) which is also a good sleep aid
[hmd1uet] (score 1, diepte 5) For real. I understand why it's hard for so many people to understand but nutrition and healthy eating can be a huge challenge regardless of how you cope.

Some people eat when they are under high stress, some people stop eating. Be kind either way.
[hmd1vq4] (score 1, diepte 5) This. My life summed up here.
[hmh33yd] (score 1, diepte 5) Yeah I am the same way. I try not to think about it too much...
[hmcdruc] (score 1, diepte 3) Fot a frien like you. Other than actually eat much more, u could try eating nuts. Any kind, thay have lots of calories
[hmck6f4] (score 1, diepte 3) Workout and take creatine. Worked for me
[hmd15xu] (score 1, diepte 6) Are you serious? Ever heard of fucking starvation? Lmao this is ridiculous.
[hmd1emx] (score 1, diepte 4) Are you saying somebody overweight enough to die from it also doesn’t have an eating disorder? Maybe I’m just completely misunderstanding you but this makes no sense.
[hmdj4nt] (score 1, diepte 4) Exactly what I would say. I've put on \~50lbs. after working out for 3 years from 150 at 6'3, and it's all been shoving food in my face and feeling destroyed after every workout. I had the exact same mentality where I was always gonna be scrawny until I started putting on weight and realized I was thinking wrong. 

My roommate is the same way, one of those "forever scrawny" guys. It's really hard to get him out of that mentality without seeing progress at the start. The best thing I did for myself was counting calories at the start, because I thought I was eating enough until I saw the numbers.
[hmcbv2w] (score 1, diepte 1) Ice cream and peanut butter
[hmch2ht] (score 1, diepte 2) I think a serving has something like 1300 calories and 40-60 grams of protein? Something insane. Would a balanced home cooked meal be better nutritionally? Sure! Is that feasible when you’re putting in 13 hour days? No!

OP if you want to really woo your husband you could get a few blender bottles and pre-portion the protein powder out for him to take with him to the kitchen each day, that’d make him smile.
[hmffuov] (score 1, diepte 1) I think you're giving advice for avoiding weight gain but op is looking for advice for gaining weight.
[hmch6w1] (score 1, diepte 0) Get hypothyroidism. Works for me
[hmchjgv] (score 1, diepte 0) Weight gane happens for most people when they get old. I'm a fat cook. But old. Wish I could drop the weight.
[hmcho0r] (score 1, diepte 0) I snack all day and pig out on my days off
[hmd1q8w] (score 1, diepte 0) You don’t.  You gotta have time to eat. Sous don’t have time.
[hmd6c2n] (score 1, diepte 0) Set timers in his phone to remind him to eat. Bring a few granola bars or cut fruit. Good cooks find a way to make time for what they need
[hmd7tzu] (score 1, diepte 0) Lost 22 pounds this year by running in off time, eating grilled chicken in one hundred different ways. If you struggle with running or walking, download Run Tempo to work on your pace. Either way, if you’re up and moving that’s a fucking win. 6-7 hours of sleep, get out and do something. You’ll feel better. Ah…well, I also have been sober for 54 days and drink a gallon of water a day minimum.
[hmdbn2b] (score 1, diepte 0) Stop actually eating everything he tastes... I know it seems a waste.. But you don't have to swallow everything you put in your mouth.

EDIT: Misread the statement.  FUCKING START SNACKING AND TASTING EVERYTHING HE CAN.  Sous Chef's have earned this right.
[hmdctak] (score 1, diepte 0) I think that's where I'm headed.
[hmdhdkt] (score 1, diepte 0) Not the best way. But weed and fried chicken late night.  Eating right before bed really helps pack the weight
[hmdhjeg] (score 1, diepte 0) Ya idk I haven't eaten in 2 days because I lose my appetite as an executive chef
[hmdjdps] (score 1, diepte 0) Constantly eating and count your calories. I used to be really scrawny and thought I was eating enough, until I started counting calories and really saw how much I was actually eating. Eat as much as you can whenever you can, doesn't matter what it is really, as long as there's a constant food intake.

Most skinny people will feel way too full at the start, but after your body adjusts you'll put on weight and the food intake will seem normal.
[hmmms31] (score 1, diepte 0) Mass gainer. I put that shit in my yogurt and in pancakes.
[hn57rqo] (score 1, diepte 0) Bring healthy snacks I always have a bag of almonds or something in my bag
[hmd1n94] (score 0, diepte 7) Holy shit none of you understand nuance. I'm not saying that starving is healthy. I'm saying it's better to be a little underweight than it is to be obese. Fuck off
[hmd1xf2] (score 0, diepte 8) Yeah but thats completely fucking dependant on how overweight vs how underweight? Like its not a clear cut fucking thing. Im sure in reality it depends case to case and unless you’re a fucking doctor how tf would you know.
[hmd2729] (score 0, diepte 9) Okay. Cool. Go die from being a fat ass.
[hmd2b2y] (score 0, diepte 10) Lmao good argument. 

Go die of starvation
[hmd23rx] (score 0, diepte 8) You also said no doctor has ever told someone they’re too skinny...... just think about that one
[hmcnb4y] (score -1, diepte 0) I read this and came to say, "shift your weight, keep your knees bent, and do stretches on line in between orders" but understanding that it's meant in a different context, I'd say cardio, even just a little bit every day will help. I've always been fairly trim, but After finishing work there's usually a period where I find I'm too keyed up still and can't sleep, so I go for a run, or do some pushups, anything that gets my heart pumping a bit. It tires me out and will help him burn off calories. Vitamins, hydration, avoiding sweets also helps, but I'd advise realistic sustainable goals at least to start.

Edit: I read this wrong, he has trouble putting *on* weight? Well, why does he need weight? I assume he's eating well. If he's keeping active and not getting sick maybe he's just a naturally thinner person? If he's not getting colds all the time or anythi g it might not be as serious as people make it out to be.
[hmd0xxu] (score -2, diepte 5) How. Who has ever died from being a little underweight
[hmcykvp] (score -3, diepte 3) No doctor has ever told someone they're too skinny, unless they have a legit eating disorder. Being overweight is so much worse than being underweight

=== THREAD 1dkt4h0 ===
SUBREDDIT: r/bartenders
DATUM: 2024-06-21  SCORE: 43  REACTIES: 68
TITEL: Do you take care or treat your feet?
POST (source_id=post):
I have noticed that the skin in bottom of my feet is yellowish and looks beaten up and dry after years of bartending. Do you take care of your feet and if so, how do you do it.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l9k59ne] (score 114, diepte 0) I whisper them the odd sweet nothin' and take them out for a meal every now and again.
[l9k6ku8] (score 82, diepte 0) Pedicures. Wool socks. Quality shoes. Go barefoot as much as possible (outside of work obviously).
[l9k6viv] (score 27, diepte 0) Yes. Proper insoles, good socks then I have a thingy to get rid of dead skin (nasty I know) then I moisturise most nights, often sometimes before work if I know my shift will be tough.
[l9k6i03] (score 20, diepte 0) I have foot issues beyond the normal wear and tear but yeah you should care for your feet. I’d recommend a pumice stone, epsom salt soaks, lotion at home. You can go get a full pedicure or my personal favorite is I go to a hot soak and sauna at my local hippie wellness center.

Good shoes and insoles of course.

At the age of 35 I was diagnosed with Gout for the first time. I will never take healthy, good feeling feet for granted again.
[l9khp8y] (score 20, diepte 2) It starts at around $40 plus tip around me. Prices vary a lot depending on how nice the place is - if you’re unsure where to start I’d ask a girl friend who has nice nails, they usually have tried a bunch of places before they settle on one place.
[l9k8r2t] (score 19, diepte 0) Lotion. Good shoes. Insoles. Massage as needed.  

Honestly while you’re at it start thinking about how you’re gonna take care of your whole body because it’s all taking a beating 😭
[l9kkck7] (score 10, diepte 1) You know you be using that microphone for the nutmeg on your toes
[l9kbln2] (score 10, diepte 0) I got a foot soaking tub I use pretty frequently. Epsom salts and soaking.
[l9kb18n] (score 9, diepte 0) Pedicures and massages monthly. Restaurant employees have a highly physical job we need to take care of their bodies.
[l9kgseo] (score 9, diepte 0) I get the most expensive pedicure every time i go. Not often, but worth it. 

Also, foot lotion. Yep.
[l9kf1yu] (score 8, diepte 1) How much does a pedicure generally cost?

Ever since spending a small fortune removing ingrowns, I'm super cautious about clipping them myself.
[l9kiia6] (score 8, diepte 0) I wear good shoes and socks, and when I come home at night I like to sit on the tub and run hot water and scrub my feet really well, sometimes using a gritty scrub or pumice stone. Then I use okeefes healthy feet or some other good lotion before bed. I try to get a good pedicure with foot massage once every month or so. Also feels good to roll your feet over tennis balls.
[l9kk4jq] (score 7, diepte 2) Where I’m from pedicures cost anywhere from $45 on up. But you could totally do a home pedicure. Just soak your feet in some hot water and bath salts. Use one of those exfoliating stones and rub the bottoms and sides. Up to you if you wanna do your nails but you can get a pedicure kit for like $5
[l9kf6o2] (score 7, diepte 1) I bought a foot massager. It broke within a year and a half but it still kinda works. Best $100 I spent ngl
[l9kiop7] (score 6, diepte 2) Anywhere from 50-200 depending how fancy you want to go. I like to splurge for the hot stone massage and paraffin wax and whatnot, and my girlfriend gets gel coat, so we end up spending like $200 when we go. 

But if you just want to maintain your feet and not make a thing out of it it’s cheaper.
[l9koauz] (score 6, diepte 3) Gotcha
[l9kiuv8] (score 6, diepte 0) I just got a foot scrub with eucalyptus and peppermint oil that I’ve been trying to use twice a week. Check out Wild Brew Wellness on Etsy…. That stuff is AMAZING.
[l9l29ly] (score 5, diepte 1) Ah, gout. The king’s disease. I’ve had my flare ups too. The pain was unimaginable in my throbbing toe but I could always work through it. Then….I twisted my ankle and had a gout flare in my ankle joint. That shit was worse than breaking a bone (repeatedly). I had a full blown high grade fever for two days.
[l9kn11u] (score 5, diepte 0) same stuff everyone else is saying but specifically the o’keefes healthy feet lotion. you can get it in a pack with the working hands and they are both so good
[l9ko8rp] (score 4, diepte 2) Wtf?
[l9kz5a9] (score 4, diepte 1) I use Badger peppermint and tea tree foot balm. I love it.
[l9kk9z8] (score 4, diepte 0) gold bond spray on the toes.  anti-fungal in the boots.  happy tootsies
[l9lgj1e] (score 3, diepte 3) got me here for sho
[l9kbq1k] (score 3, diepte 0) Comfortable, waterproof shoes, wool blend socks, comfortable insoles if the shoes need them. Showers and lotion if needed. The Army was far more rough on my feet though. I'm grateful I can wear whatever I want now.
[l9lks40] (score 3, diepte 2) Badger balm is amazing. I use the ginger & cayenne one for my elbows and wrists.
[l9l1b20] (score 3, diepte 0) I have naturally sweaty feet, been working in kitchens and FOH for 16 years. 

Buy. Good. Socks. I had a climber friend that was endorsed by Wright socks and he gave me 5 pairs 10 years ago. I still buy them at 15 bucks a pair a decade later. They work so well.

Also, get a pumice stone and scrub away dead skin.
[l9l2kkn] (score 3, diepte 0) I have a Epsom salt foot soak once a week, scrub them with a pumice stone, then finish them off with a THC infused body butter. It's heaven.
[l9nbdi2] (score 3, diepte 0) I have those rubber, studded half spheres that you use to massage your feet, I keep them in front of the bathroom sink and try to use them every night before bed.

Also, be sure to stretch out your calves and ankles.
[l9oxdu8] (score 2, diepte 1) That is some yoko ono type bizness
[l9lfcd8] (score 2, diepte 2) Autocorrect is never not hilarious lol
[l9l268r] (score 2, diepte 0) After getting a good pedicure as recommended here already, O’Keeffe’s Healthy Feet is a good way to maintain your feet. It’s from the same company that makes O’Keeffe’s Working Hands. 

Amazon has a 2 pack that contains them both.
[l9llhx8] (score 2, diepte 0) Growing up, my dad always told me that you don’t actually need to *wash* your feet - that when you shower your feet will get cleaned automatically by the soap and water that runs off from cleaning the rest of your body.

30 years later, after a lifetime of believing this and suffering through *completely avoidable* foot problems , a specialist sat me down and had the embarrassing conversation of how to actually take care of my feet. 

So yeah, I got a pair of those exfoliating gloves and some nice foot soap and actually wash them every day, then use one of those pumice stone thingies, and I got extra strong moisturiser too. There’s these squishy gel-like socks you put on for like ten minutes after the moisturiser to help it sink in, too, but I usually only use those if I’m really dry. Putting them in the freezer beforehand is great on a hot day. 

It’s a real slow process but all the issues are clearing up and it doesn’t hurt to walk anymore. 👍
[l9lq72r] (score 2, diepte 0) Moisturize, clean socks, a little gold bond, and I always wash them after work. I trim my own nails pretty easily.
[l9lunq8] (score 2, diepte 0) I’m long overdue for a mani-pedi.
[l9ncek4] (score 2, diepte 1 OP) Damn. I might have to show it to someone
[l9ng28f] (score 2, diepte 0) I started wearing flip flops behind the bar lol
[l9ng7sr] (score 2, diepte 1) I also worked at a hole in the wall bar where no one cared.
[l9nh04q] (score 2, diepte 0) I try to do stretches and foot/ankle strengthening exercises at least 3x a week. Every night after work when I shower I give myself a solid foot rub. 
I wear barefoot shoes and see a DO if any foot/leg pain arises. 
I also use this nicy Earth Thereputics foot lotion nightly that keeps my skin pretty soft, but some callous on your feet is totally healthy normal.
[l9o9vlv] (score 2, diepte 0) theragun
hydration
stretching the feet
stretching the calves
insoles
comfortable shoes
different shoes for work / not work
lotion
callous shaver
spiky foot massage balls
lacrosse balls if yr hardcore
rubber handball
heel stretcher
toe spreader
compression socks
ice footbath
epsom salt bath
RICE (rest, ice, compression, elevation)
put them dogs up above your heart for a while every day

my favorite shoes:

fp insoles gamechangers custom orthotic insoles (mold at home, $50)
zliner brand insoles
klaw footwear
asics gel venture
wide ass white restaurant crocs (i call em my mickey mouse shoes)
rainbow brand leather flipflops 
cheap recovery slides from amazon or target

advil
[l9ncc3p] (score 1, diepte 1) Lmaooo
[l9opbuc] (score 1, diepte 2) I’m in a medium cost of living area and just got one on Tuesday. $45 for the middle of the road package that included a sugar scrub and a below the knee massage. I tipped $20 because there ain’t no way I’m touching my own feet let alone a strangers feet for 30 minutes straight for $45.

I’m a dude and got my favorite color nail polish. Feels like you’re walking on clouds for 48 hours after. Gets all the yellow dead skin off.
[l9kvj8b] (score 1, diepte 2) 🤮🤮🤮
[l9kaobz] (score 1, diepte 0) Just got my first pair of insoles because I woke up one morning feeling like my Achilles was gonna pop. I also bought a massage gun, after about 10 days I was back to normal
[l9kat8l] (score 1, diepte 0) I bought some cream that eats callous because I wanted my feet to keep their girlish figure. 

Look up urea cream.
[l9xlbj4] (score 1, diepte 1) Yes to epsom salt soaking. It's been around forever because it works. Your Grandma knew what she was doing.
[l9m1ahc] (score 1, diepte 1) Seconding this, will throw out that Lacrosse balls are the absolute goat when it comes to rolling out your feet.
[l9klaz7] (score 1, diepte 0) Memory foam insoles
[l9kn54p] (score 1, diepte 1) I’ve heard so many good things about O’Keefe’s!
[l9ko3iy] (score 1, diepte 0) Epsom salt soaks once a week when i start to feel the ache. And the stink. lol
[l9ksp8b] (score 1, diepte 0) I never did anything for my feet but now that I’m married my wife has, uh, gently encouraged me to get a pedicure once a month so now I do.
[l9kv8oj] (score 1, diepte 0) No, I just bitch and moan, maybe get some new inserts.
[l9l2x78] (score 1, diepte 0) Sounds like you have athletes foot honestly. I've been bartending for 10 years straight and some of those years I've had to work 50 to 60 hours. My feet are silky smooth and I have no pain. I wear on clouds x5 waterproof at work and I wash my feet with regular body wash every day. Look these up on amazon: brand is the body shop, peppermint pumice foot scrub. Also Burts bees coconut oil foot cream. Those two products are great for when you need a little extra care.
[l9l7kdq] (score 1, diepte 0) Get orthotics!!!
[l9l8qq0] (score 1, diepte 0) Regular pedicures (every three weeks for me) and a legit foot massage.
[l9lohjd] (score 1, diepte 0) YES. We have to take care of our feet. As someone who is and has been in hospitality and nightlife for 20 yrs, and has experienced nerve damage in one of my feet from the cocktail/bottle service portion where I wore high heels everyday, I have lots to say on this.

First get good insoles and have at least 2 pairs of shoes to switch between. 

Pedicures are good because they will help with your callouses and rough skin you are experiencing.

If you work in conditions that make your feet sweat a lot or wet, waterproof socks can be a lifesaver.

Put lotion on your feet and hands at bedtime. (Our hands also take a beating)

REFLEXOLOGY- I cannot recommend this enough. Find a good Chinese reflexology location and get the hour foot massage. They will still massage your whole body, but focus mostly on your feet. And they understand the pressure points of the feet so well, you can feel the tension release all over. Plus they are usually a fraction of the cost of a massage anywhere else. Usually around $45 for the hour massage. 

An at home foot roller can be a godsend after a long shift https://a.co/d/0hGpJU7q

Also another good treat yourself investment is a theragun, or whatever brand similar. Use it on your whole body, particularly your legs after a shift. I got the Sharper Image one at Costco for $70 and it’s a lifesaver.

Hope this helps! Take care of those feet, they’re important :)
[l9lutuv] (score 1, diepte 0) I wear those overnight foot masks like once or twice a month and it helps a lot. I also wear compression socks and always have shoes with insoles.
[l9lzgdr] (score 1, diepte 0) Yes. I have a foot scrubber thing from like, tjmaxx that has a pumice on one side and a cheese grater looking thing on the other. At the end of a shower, I grate then pumice, then add body oil before drying. Your feet will be so delicate you need shoes outside.
[l9m0a8z] (score 1, diepte 0) Super late here, but I personally use Dr. Scholl’s heavy duty work insoles (the ones meant for construction workers). Got that advice from a 40+ year serving vet and I’ll never go back. Put those insoles in a pair of New Balance or Docs, and you’ll prefer standing to sitting after a while!
[l9mg564] (score 1, diepte 0) I have a peppermint foot spray that really helps - not sure where would sell it in the US, but I'm the UK you can get it from the Body Shop
[l9n1lf6] (score 1, diepte 0) FYI - sometimes athletes foot isn't burning and peeling between the toes, sometimes is thick heel skin that is faint yellow and cracks.
[l9ncwj9] (score 1, diepte 2) It's cured the same way, try some drug store stuff and rotate your shoes so the get fully dry, maybe bring spare socks & change out as needed.
[l9ok78e] (score 1, diepte 2) Soak in vinegar water
[l9njovv] (score 1, diepte 0) Aquaphor and socks at night helps
[l9nod9u] (score 1, diepte 0) Yes
[l9o9x52] (score 1, diepte 0) After a bartending shift I usually wind down with a drink and some herb while sitting at my gaming desk. I purchased a foot massage roller that I’ve placed under the desk.
[l9od4l4] (score 1, diepte 0) What goes on down there is none of my business
[l9own1i] (score 1, diepte 0) Oh dude, get a pumice stone, get yourself some expensive socks.
[l9pnbyf] (score 1, diepte 0) Pedicure once a month, lotion once in while, stretch before bed, good insoles, good shoes
[l9rmdsp] (score 1, diepte 0) If you can afford it, regular pedicures, maybe once or twice a month just to keep up with the nails and calluses! Otherwise make your shoes as comfortable as possible, gel insoles or whatever. Bad shoes will throw your entire posterior chain off.
[l9l4qok] (score 0, diepte 0) No, I get off work and go skateboard to hurt more

=== THREAD 1937pit ===
SUBREDDIT: r/Construction
DATUM: 2024-01-10  SCORE: 35  REACTIES: 68
TITEL: I got tiny feet. I also got gifted $200 boots that can’t be returned or exchanged. How do I make them fit?
POST (source_id=post):
I love these boots but they’re a bit big.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kh7971n] (score 210, diepte 0) Don’t wear boots that don’t fit, it can cause issues for health and safety. Never heard of 200$ boots that can’t be exchanged.
[kh7bfka] (score 129, diepte 0) Givem to your wife's boyfriend they'll probly fit him perfect
[kh7mrlv] (score 127, diepte 1 OP) Who do you think got me the boots?
[kh7e4pm] (score 95, diepte 0) Sell them on eBay. They’re never going to fit
[kh7hkku] (score 77, diepte 1) Maybe they fell off the back of an Amazon van
[kh7fbf0] (score 38, diepte 0) Construction adhesive. Fill em half full and put your feet in so it takes the form of them.
[kh84vzm] (score 23, diepte 3 OP) That sounds kinda gay…I’m into it.
[kh7h1x8] (score 22, diepte 2) I do a full hour of toe curls every day.
[kh8seyo] (score 21, diepte 2) If this is their policy that makes Danners a shit company.
[kh7d1sy] (score 19, diepte 0) How many pairs of socks do you have?
[kh8cvn6] (score 18, diepte 4) Just outed yourself. You're not a superintendent at all. You're an electrician, gtfo.
[kh7zxo8] (score 16, diepte 1) Expanding foam for window sills is my preferred method
[kh7y6c8] (score 15, diepte 2) I need this guy as a super on my job.
[kh8c5uq] (score 13, diepte 1) danners policy is very strict on this - if it is so much as worn outside with any creasing you’re screwed and will not even exchange - been there done that and was out of $440
[kh998zc] (score 12, diepte 5 OP) Son of an electrician. I would say he must’ve rubbed off on me but…the implication of that phrase….does not end well.
[kh7g1jc] (score 11, diepte 0) Hit the gym
[kh7gvct] (score 11, diepte 1) To grow feet?? Woah
[kh7k0ba] (score 11, diepte 0) Sell them and use the money for something that fits.
[kh8a9w9] (score 10, diepte 2) Dad?
[kh7n30d] (score 10, diepte 0) Get a boot shrinker. They have them at Lowe’s tool rental if you just need them for a one time use.
[kh99ge0] (score 9, diepte 3 OP) Still at the store. Does your mom want whole or 2%?
[kh7hg75] (score 8, diepte 3) That's just Porta potty jack off time I'm guessing?
[kh7mz91] (score 8, diepte 0) Go find a store where they sell the same item but with your size, then return the larger one.
[khaalqh] (score 7, diepte 3) It’s this policy that made me stop buying boots from a local store.  I had a pair of Thorogoods that was a bit off on one boot.  They finally exchanged but put up a huge fight.
[kh8512d] (score 7, diepte 1 OP) They don’t make xtra small condoms anymore so that’s useless.
[kh8538n] (score 6, diepte 1 OP) Gotta buy blinker fluid first.
[khabzo6] (score 5, diepte 6) If you haven't been rubbed off on by your dad then you're not taking enough fishing trips
[kh84zmw] (score 5, diepte 1 OP) Too fat for that shit. Liposuction here I come.
[kh7shtu] (score 5, diepte 0) You don’t. Sell ‘em on Facebook. I just had to do the same thing. $180 boots, brand here, sold for $80.
[kh86bg8] (score 5, diepte 0) Use the Ron Desantis boot riser method.
[kh7tei2] (score 4, diepte 1) Not sure how plausible it is but a friend once had the same issue and started posting on all the places related to that brand of boot and found someone who had a pair that was too small and they exchanged their boots. It was a backpacking boot though and those forums are always full of people exchanging gear. Can’t say how effective this option would be for work boots.
[kh7og15] (score 4, diepte 0) Ron DeSantis? Is this you?
[kh83g1t] (score 3, diepte 1) Shitty Life Pro Tip: You can do this with any number of things, including things that have broken but appear like new.
[kh85403] (score 3, diepte 1 OP) Big Ronda yeah
[kh9vpk0] (score 3, diepte 0) Sell them on craigslist or facebook marketplace as never used and buy boots that fit. I have small feet and wore boots that were too big for a year trying to make them fit. I always had blisters and developed a cyst on the top of my foot. Bought boots that fit and it was life changing.
[kh7rx77] (score 2, diepte 2) The solution is called Boot Liners.
[kh7c7o4] (score 2, diepte 0) Some sort of orthotic maybe
[kh89ae2] (score 2, diepte 1) Skip the gym!! I’ve got some foot enlargement pills guaranteed to grow you 2 shoe sizes in a month. *Adverse effects are included to but not limited to numbness and tingling, dark spots, toes falling off, and complete loss of feet.
[kh857dg] (score 2, diepte 1 OP) I can’t sell them to my boyfriend, your dad has bigger feet than this boot.
[kh7pjsw] (score 2, diepte 0) Dont' mess with your feet.... seriously. Just put them up for sale... and get another pair that fits you properly. Wrong size shoes can mess with your posture, your back, the way you walk could lead to other problems.
[kh7thpt] (score 2, diepte 0) Feet transplant.
[kh85555] (score 2, diepte 1 OP) I knew those feet in my basement would come in handy
[kh7ugv7] (score 2, diepte 0) Don’t
[kh8d5pi] (score 2, diepte 0) Go to the same doc that did your penile implant. Ask for the collagen and marrow injection.
[kh8fwcd] (score 2, diepte 0) If there a half size, some times a full size can be improved by adding insoles to bottom of boots. I have my left foot a half size bigger than right foot, I've always had to buy a size 12, instead of actual size 11.5 on right foot then adjust half a size.
[kh9mbat] (score 2, diepte 0) Bro I FUCKED up my foot trying to making too large a shoe work on my foot. DONT
[kh7c660] (score 1, diepte 1) Savage.
[kh7wwzu] (score 1, diepte 3) Foot condoms? Well yeah. He wouldn't want to be swapping sweat with his wife's boyfriend.
[kh84ydm] (score 1, diepte 1 OP) I have a single sock from 1992.
[kh7ho30] (score 1, diepte 1) And realize some gains on your wrists and ankles
[kh85209] (score 1, diepte 1 OP) Only on Tuesday’s.
[kh7psa1] (score 1, diepte 0) Ronda? Is that you?
[kh7t9vr] (score 1, diepte 0) So I haven't seen anybody ask the real questions in the comments:

-how do they not fit? Too wide at what parts of your foot?

-Are they too tall for your foot as well/do your feet have pronounced arches?

-What is the brand size of the boots/what is your brannock size?

    The only thing I was able to do without jeopardizing my foot health and on site safety was add a custom orthopedic insert from Fleet Feet ($150), because besides having small feet I have different arched and sized feet. It can't hurt. It will absolutely suck balls in heat but too pair's of socks. A single pair of hogh end thick cut boot socks from Darn Tough or a like brand could help as well but, again, not if it's hot where you are working. 

    The bottom line I if they are a full size too big there isn't anything you can do. A half size maybe you can work with but it depends on your feet and how/why they don't fit.
[kh82ywz] (score 1, diepte 0) The obvious solution is to break both feet and stretch them out so when the heal they’re bigger and the boots fit.
[kh8fpx4] (score 1, diepte 0) Just use the ol' timber stretcher, just make sure to bolt it to your feet, screws will tear.
[kh8h5hb] (score 1, diepte 0) Grow
[kh8hn4y] (score 1, diepte 0) Sell them and go to a store and buy new ones. I’m on my feet all day (10hrs), the proper boot makes a huge difference. Don’t go cheap either, a good pair can easily run you $250-$300
[kh8mc46] (score 1, diepte 0) Just heard a guy in wheelchair talk about a pair of loose boots put a blister on him that turned into something much worse (type of infection) almost lost foot and had to do wound care for almost 2 months to get it back to healing .
           He wasn't diabetic or anything just started with new loose boots and a blister.
[kh8s83t] (score 1, diepte 0) You're gonna break an ankle, sell them and buy something that fits.
[kh9skoo] (score 1, diepte 0) Sell them on fb marketplace, and buy the same brand from the kid's section. Problem solved, next question.
[kha9ko7] (score 1, diepte 0) Order the same ones from Amazon, in correct size. Return yours in new box because they sent wrong size. “I’m sorry I just need my money back because I had to go buy the correct pair because I needed them now.” It’s Amazon, fuck em.
[khaizj7] (score 1, diepte 0) Who gifts boots and doesn't ask for a size? Sell em and buy the right ones
[khax1lz] (score 1, diepte 0) Sell them and buy boots that fit. Not worth wearing ill fitting boots.  Even if you do, you’ll probably trip a bunch of times because the length is longer than you are used to.  Sounds as though they are a typical size so finding someone to purchase them will be easy.  Would be tougher trying to sell a pair that is on the small or large extreme.
[khbe0wj] (score 1, diepte 0) Maybe keep them as winter boots when you got heavy socks
[kh7gys8] (score -1, diepte 0) Sell them to your boyfriend. 

What size, brand, make? Maybe someone on here will take them off your hands.
[kh84u8k] (score -17, diepte 1 OP) As a superintendent, obviously health and safety is on the bottom of my priority list. /s

