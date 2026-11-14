# Label-batch batch_0036

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
Schrijf het resultaat naar `batch_0036.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: n1vtv3, jsa24q, qmq6eg).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD n1vtv3 ===
SUBREDDIT: r/BuyItForLife
DATUM: 2021-04-30  SCORE: 324  REACTIES: 277
TITEL: Comfortable everyday shoes?
POST (source_id=post):
Hello! 

I walk about 10,000-20,000 steps a day at work & I'm looking for comfier shoes. 

I have heard many people say adidas sambas last them years but are they comfortable? 

I had a pair of $60 nike tennis shoes I wore of 6 years without any tearing but recently threw them out because they hurt my feet. 

Now I'm wearing a pair of adidas tennis shoes (memory foam) I got for $30 2 years ago and they are the best pair of shoes I've ever had but I know I will need to start replacing shoes more often. 

I had a pair of sperry memory foam, and they were amazing but they made my feet sweat horribly because there was no way to ventilate the sweat since they aren't made of mesh like most tennis shoes are. 

I'm also curious about insoles, do you use them? Are they meant to make your shoes last longer? 

Tldr; looking for a new pair of shoes for daily use that are comfortable

Edit: wow! I did not expect this many comments. Thank you all for the help! I will definitely be going to a new balance store to be sized and then hop around to a few different stores like Adidas & sketchers to see what I like.

Edit 2: After reading comments here & researching barefoot/minimalist shoes, I will also be giving those a try! I've read it's good to switch up different shoe types to work more muscles in your feet so they don't become week later in life. Thanks again, it's interesting to see what you all recommend!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gwfn6te] (score 226, diepte 0) Hiking shoes. They’re made for long distance walking. Buy a stiff pair that’s made for long distance (keen and oboz are best imo) as well as superfeet insoles. Merrill are decent as well. 

These will last a couple years and will protect your feet. 

Bit expensive but they’re cheaper than foot surgery.
[gwfmqiz] (score 172, diepte 0) Go to a New Balance store for a proper fitting. Their most durable shoes are any of the “Made in” series, such as the 990 and 993.
[gwg5pq8] (score 151, diepte 0) Remember, "BIFL" shoes still need to get resoled after a lot of wear. The only durable/BIFL part of a shoe is the upper. Treads get worn, insoles rip, supports break down. 

In your case it is probably better to buy a comfortable shoe under $100 every year instead of looking for a $200 shoe and stretching it out to 2 years.
[gwfrz7n] (score 96, diepte 0) Adding to the New Balance & ASICS recommendations, I’d also say Birkenstocks.  Not really shoes but great for walking.

Also, shoes are not BIFL
[gwg8nfp] (score 61, diepte 1) I swear by superfeet insoles. I bought a new pair yesterday. they lasted longer than the soles of the shoes.
[gwg4csw] (score 50, diepte 0) I like hoka
[gwfmhwx] (score 39, diepte 0) I wear Made in the USA New Balance 998. They cost about $150-200, but are worth every dollar. I buy two pairs at a time and alternate so they last longer. Good shoes are an investment in having good feet later in life. You aren't invincible. Treat yourself kindly, because if you wait until your feet become a problem it may be too late to fix them.
[gwfv7yo] (score 34, diepte 0) You're not spending enough money.  With the amount you're walking, $100 should be your bare minimum, and you shouldn't be afraid to go up to $200.

I used to be a big New Balance fan, but I've recently gotten into Asics and have been very happy with them.
[gwgmsvh] (score 33, diepte 2) Well-made hiking shoes that will last are not the same thing as comfortable. The shoes are time and true, but constantly wearing stiff hiking shoes that lock up your feet for the most wicked of environments will send OP to foot surgery quicker than imaginable.
[gwg62xs] (score 25, diepte 1) Solomon hiking shoes are phenomenal but pricy as well
[gwfyx4y] (score 25, diepte 0) I love Ecco, they're pretty much all I buy
[gwg6ot2] (score 24, diepte 1) Pro Tip - Get fitted at New Balance by a Certified Pedorthist (make an appointment) and if you like the shoes, buy them. Next, go to eBay and put in a search for those exact shoes. If they aren't there (new) for a good price now, they will be. Save the search. When they come up in the size you need, buy one or more pairs. I've been doing this for years and have saved over $1000 thus far!
[gwgbggs] (score 22, diepte 1) I can second this. I've had a pair of the Made In England's for 5 years and still wear them.
[gwfo0w8] (score 21, diepte 0) By all means do not buy a cheap pair of shoes, if you’re on your feet all day, it’s going to affect the rest of your body.
[gwgeg6c] (score 21, diepte 0) Brooks. Extremely comfortable & great support.
[gwgay14] (score 20, diepte 1) Also New Balance Fresh Foam 1080s 

There is different letters after 1080s V or other letters, it's all good 

Have 2E and 4E 

These shoes score near the top of any top ten reviews on YouTube
[gwgc9yi] (score 20, diepte 1) Solid advice.
[gwfxk0o] (score 18, diepte 1) New balance are the best (for my family). They have some cheaper ones that look nice, but don’t have the same support/length of life. I, personally, love their trail shoes. I’ve had a couple of pairs that have lasted me for a number of years with heavy use. I hope you find what your looking for!
[gwg1zl5] (score 18, diepte 2) Big fan of New Balance, but I despise the way they turnover models in a way that makes it next to impossible to get very similar shoes the second time around.
[gwgaa2h] (score 15, diepte 1) Oboz baby. I love mine.
[gwg8bss] (score 14, diepte 1) Is it Merrill or are you referring to Merrell? Just to be clear, for OP. 

I bought a pair of Merrell Moab 2 because I was walking a lot during the day: very comfortable. They're hiking shoes so if on the one hand they're built like a tank, on the other the soles are a bit too hard for me, and I can't wear them in late spring/summer. They're too warm. But they're quite affordable.

If you want to spend (a lot) more I am loving the Adidas NMD. My understanding is that part of their soles have the Boost material and I've never had anything more comfortable; they're perfect for warm weather and it's like walking on pillows. Any Adidas model with the Boost soles will do for you, I believe. 

Downside: they cost a lot here in EU (~€130) and I'm still sour because I didn't buy 2 pairs and not one, when I found them for half the price 4 years ago.

In general, if you need comfort but you don't need necessarily protection, I would look at running shoes and specifically A3 shoes, the most cushioned. I've read of people with back, knees and feet problems that went for the Hoka shoes for extra cushioning. However, not the most understated shoes.
[gwgp2ny] (score 14, diepte 3) Merrills and similar-style hiking shoes are not like this at all. They are quite soft and comfortable. These are not really a BIFL item though.
[gwh1jmu] (score 14, diepte 1) To piggyback off of this. You really cannot buy a modern sneaker as a buy for life product. The foam wears down from use especially in the midsole which is why the OP is really having pain. The shoe specifically is almost always the first thing I look at in the runners that I work with when they start having foot ankle knee pain if nothing else has changed.

Something that you're standing in for 8 to 10 hours every single day is totally different then something that you wear maybe two or three days out of the week and mostly sitting in.
[gwgbddb] (score 13, diepte 3) Well I don't believe any pair of shoes/boots is truly bifl. However I think two years is a great lifespan for a $200 pair. I have worn out two pairs of the quest 4d gtx and am currently wearing the Guardians for work and love them.
[gwgt73a] (score 12, diepte 4) I wear their trail running shoes as everyday sneakers. Not BIFL but I’m not sure that’s a reasonable expectation for a shoe like this. After 1-2 years they get converted to yard work shoes.
[gwg0xze] (score 12, diepte 0) Mephisto. These are some of the most comfortable shoes on the market and they last even longer than they say!

Expensive, but you'll still have them in 15 years.
[gwg5mfo] (score 12, diepte 0) As other people have stated, sneakers aren’t really BIFL, but with that said, really any New Balance or a pair of Adidas Ultraboosts are both great options.

Both are very well made, comfortable, and relatively durable.
[gwg8gue] (score 11, diepte 2) Solomon are extremely comfortable but not BIFL in my experience (edit: mine lasted 2 years). Do you have a specific model that has held up for you?
[gwfp03i] (score 11, diepte 0) Vans slip ons with ultra cush insoles. 

Edit: Stop downvoting me, I’ve been wearing mine every day for three years and still going strong, most comfortable shoe I’ve ever owned.
[gwg52v3] (score 11, diepte 0) Saucony
[gwgl9wd] (score 10, diepte 2) > superfeet insoles

some pricey insoles those are my friend.
[gwgmdus] (score 10, diepte 1) I use this strategy with my brooks. They're the most comfortable shoe I have for around 6 months, they dont last a full year because I walk a ton on concrete floors so that destroys the cushion. Love them until the last week when i know it's time to replace them
[gwg8i7w] (score 10, diepte 0) Ever since I’ve switched to barefoot type shoes I’ve had decreased back pain, a nice stride on my step, not a single ankle twist, and I don’t get weird nerve punches anymore. Also, my posture has significantly improved.

For work, I went with the Lems ninetofive, and for running/leisure, I went with the Altra Escalante 2.5. For hiking, I have Altra Superior 3.0. For winter boots, I’ve gone with Manitoba’s Mukluks.

The reason why I have separate pairs for each occasions is simple: if I were to wear hiking shoes in the urban setting the soles would shed right down very quickly due to the softer rubber meant for gripping rocks/terrain. The Escalante or any running shoe for that matter have harder soles than hiking due to the nature of hitting hard pavement rather than very diverse terrain.
[gwggao3] (score 9, diepte 2) I just got some Fresh Foams, time will tell how durable they are, but I can attest to their comfort!
[gwgb3j4] (score 9, diepte 1) Danner is my choice for BIFL boots.
[gwg4xay] (score 8, diepte 1) I'm a nurse and bought Birkenstock trainers and shoes. They are the utter best I've had for work.
[gwgifwc] (score 8, diepte 3) Birks have a cork sole that does take a short time to break in. They're harder than sneakers but once you break them in they're amazing. Sometimes after a long work day where my feet are sore I'll slip my birks on and my feet will feel better from the custom shaped support they offer.
[gwh1t2p] (score 8, diepte 1) fyi, i know nobody reads the sidebar here, but “BIFL” can also mean “lasts a long time compared to the typical lifespan of that product type” in this sub even if it’s not technically “for life”
[gwgp8t6] (score 8, diepte 1) Yes this is a great suggestion, these are super comfortable, good support. As for which model it depends on how your foot is, and how you walk.

These are great shoes for comfort, walking, maybe some running. They are not great for lateral stability in my opinion because of all the foam and bounce.

Like any shoe they will wear out, so don't expect them to wear forever.
[gwgpn5s] (score 7, diepte 3) First rule of running shoes - Color doesn't matter! 😂😂
[gwgiifo] (score 7, diepte 2) Superfeet Green FTW. I put them in all my shoes (except my Birks)
[gwgndw7] (score 7, diepte 3) 60 day money back comfort guarantee. So if you don't like a version or the brand, no risk take them back.
I'm a fan of the orange version.
[gwgbn73] (score 7, diepte 1) I (and many people I know) use hiking shoes as work boots 'cause they're basically the same thing but not steel toed. The only thing I'd warn you about is ventilation, like you said in your post. I currently have [these](https://www.keenfootwear.com/p/M-TARGHEE-II-WP.html?dwvar_M-TARGHEE-II-WP_color=1008417&cgid=activity_hiking_mens), and they're great but (maybe because they're waterproof) leave my feet pretty damp if I'm doing any physical activity. 

u/Ok_Presentation_5329 mentioned Merrells too; my daily wear shoes have been Merrells for years and I really like them. They started getting kind of beat up and I bought a second pair so Merrell didn't stop making them before I needed a replacement; here's a [picture](https://photos.app.goo.gl/kGu5mUUTsJf98AHH8) of a new one next to a 4-5 years of daily use one (which, as far as I can tell, still has as much support as I need for normal activity).
[gwge4oz] (score 7, diepte 3) Yep, the last pair of Asics I loved and bought, I bought 3 more pair for this reason, just in case.
[gwh2d2b] (score 7, diepte 1) I love Hoka but I wear the shit out of them and have to rebuy annually, may not be BIFL, but my go-to shoe right now.
[gwg6xni] (score 7, diepte 0) Goodyear welted shoes and boots can last 10+ years if properly maintained. So far, every comment replying to your question has mentioned shoes that will last 3 years, tops. Check out r/goodyearwelt
[gwghja7] (score 7, diepte 0) I've worked in kitchens nearly my whole life. I'm on my feet constantly moving at least 8 hours a day but some days are 10+. I also require non-slip. The only pair of shoes that have held up and are extremely comfortable are Ecco. They are pricey, but I have had the same pair of "Helsinki" model for over 8 years. Many many hours in extreme and long conditions. They show very little wear and I only polish them twice per year. I have another pair of sneakers that are Ecco. I bought them used on eBay, 4-5 years ago. I wear them any time I go out. Very little wear as well. Don't think I will ever buy another brand of shoes again! Ecco, BIFL!
[gwghud0] (score 7, diepte 0) Consider buying 2 pairs of similar shoes and rotating between them. Your feet will thank you, and the reduced wear and tear will allow them to last much longer. Plus I’ve heard that giving a pair of shoes a 24hr break lets them dry out and the foam re-expand and stuff. Good luck!
[gwgbqe6] (score 6, diepte 2) +2 on Merrell (one for each foot). I'm in the 25k-30k steps/day range and they've been great.
[gwgowin] (score 6, diepte 1) For the last time, he was **not the true villai**\- oh, wrong sub.
[gwg5laj] (score 6, diepte 0) Hoka. Most comfortable and supportive shoes I've ever worn and I've worn a lot. They're also one of the few shoes that I don't need to use an insole in.
[gwg63nj] (score 6, diepte 0) Are sneakers/trainers okay for your job? I REALLY love my Nike Infinity Reacts. I wear them all day long.
[gwgd2ap] (score 6, diepte 0) Xero shoes. They are actively not "comfortable" but are better for your foot strength and health, after about a week of slight discomfort of the "barefoot" feel they are the only shoe I like to wear. My feet never get sore anymore.

I farm and do lots of walking on uneven hard ground so they get plenty of use under hard conditions.
[gwggaxz] (score 6, diepte 0) BIFL shoes? Probably not a thing. Lots of good recommendations on here for long-lasting shoes though. However, Red Wing boots are definitely BIFL. May need a resole after a decade or two, but they will last forever. Unsure of your work environment, but boots can work with most attire requirements, as long as the wardrobe suits.
[gwgl0ng] (score 5, diepte 2) I do this as well. I am an avid runner and I have probably save close to what you have over the years. I don’t need the newest running version of my running shoe. I mean what has really changed other than it now comes is bright red versus dark reds?
[gwh9o9t] (score 5, diepte 1) The next gen "dad" shoes... Noooooo
[gwh3tsh] (score 5, diepte 5) Haha same here! Use my old ones for cutting the grass
[gwh6jbk] (score 5, diepte 6) Fellow dad
[gwgdm5l] (score 5, diepte 2) Yours and the US military’s. 

Not a bad choice.
[gwgibv1] (score 5, diepte 1) Seconding Keen, I have safety toe boots and shoes that I swap out for work depending on weather (specifically the Detroit, which also comes in soft toe varieties). I'm on my feet for 8+ hours a day sometimes, on concrete floors. They've never made my feet sore, and they require very little breaking in. The original pair is still going strong at nearly 3 years old, and I'm not easy on them!

I love them so much I'm slowly replacing all my other shoes with Keens as they wear out, already got some flat vans-style sneakers and some sandals, amongst others.

For any other shoes, Superfeet insoles, I like the green ones!
[gwg1s98] (score 5, diepte 0) Allbirds
[gwgszgu] (score 5, diepte 2) Idk I think it depends on a lot of things. My brother wore his Ultraboosts for well over a year and he completely abuses his shoes. Plus, there are obviously a few different iterations of Ultraboosts now so the model could make a difference.

Also worth noting in my brother’s case, his shoes were COMPLETELY toasted by the time he decided he was going to get a new pair. So, it also depends on how beat they get before you decide to replace them lol
[gwgmf8y] (score 5, diepte 1 OP) I haven't heard of this, thanks!
[gwhrq69] (score 4, diepte 3) I found out about Superfeet when I was in the Navy, all the guys that had gone to BUD/S swore by them (along with the Bates 922R boots) and I've used them for the past ~13 years since then. 

I will put them in almost every single pair of shoes that I own, because having a proper support structure just feels so much better than squishy foam. Anecdotal, but they really seem to help me avoid planar fascitis and shin splints when I start to run more (especially in boots). 

The manufacturer recommends new insoles every year or so, but I've had sets last me for 5+ years without any noticable difference from new, usually being replaced for sanitary instead of functional reasons. 

Hands down, they are excellent and I highly recommend them. I am a 10.5-11 and I'll usually get the size 11-13 and cut them down to fit.
[gwgnwpn] (score 4, diepte 4) So you're telling me that with enough park rangers, they could stomp out Yellowstone and end the threat to humanity?
[gwgipev] (score 4, diepte 2) Have you tried some wool socks with them? My daily wearers are waterproof all-leather boots and as long as I wear them with a sock that has >50% wool my feet do not get damp. 

Edit: Light or medium weight wool, not thick insulating socks.
[gwgcdaq] (score 4, diepte 3) They're firm but I wouldn't say hard. I spent a lot of time kneeling in my last job (working with kids with physical and intellectual disabilities which required supporting them to dress and undress, put their shoes on etc) and had no issues with it. It also completely cured my plantar fasciitis.
[gwfwbet] (score 4, diepte 0) I think those $60 Nikes are actually pretty good, they just don’t last long

Edit: actual advise though, my $60 Hi-Tec all leather hiking boots lasted me a decade, and were super comfortable to walk in after breaking them in. The model is the Altitude IV
[gwg0ftn] (score 4, diepte 0) I am on my feet a big part of the day (elementary teacher, roughly 10-15k steps a day) and Danskos are my go to!
[gwgg07y] (score 4, diepte 1) Seconding the Mephisto recommendation. They are expensive, but worth it. I walk a lot for work and mine are currently about four times the age that the Merrells I wore before getting them lasted (My Mephistos are almost 4 years old, Merrells typically lasted me a year). They've been resoled once so far, I will probably get them resoled again this year. The fact that they can be resoled is essential to their BIFL status. You're not going to get that out of most $100 shoes (there are none that I know of and I have looked around for them).
[gwgaw98] (score 4, diepte 0) Look for the [APMA](https://www.apma.org/Patients/CompanyList.cfm?navItemNumber=544) Seal of Approval on any shoes you get.
(223 reacties met lagere score weggelaten)

=== THREAD jsa24q ===
SUBREDDIT: r/Frugal
DATUM: 2020-11-11  SCORE: 2711  REACTIES: 271
TITEL: The best stock comes from the cheapest ingredients: chicken feet, vegetable scraps, and parm rinds.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gby56xe] (score 273, diepte 0) I like to use the carcass from rotisserie chickens. They come pre-seasoned and make yummy stock.
[gbydtrm] (score 272, diepte 1) Poultry stock (for me) - I use the leftover carcass, any extra fat, liquids and skin and throw it into a large stock pot with salted cold water to cover.  I add carrots, onions, celery and garlic cloves (I leave the peel on - cut out any gross bits) - for spices I use a couple of bay leaves, fresh pepper, parsley, thyme, rosemary and sage.

Bring to boil and reduce heat to simmer.  Simmer on medium heat stirring occasionally for 4-6 hours depending on quantity.

I strain all of this hot - twice.  Once through a large strainer and once through a small strainer.

Put into containers and refrigerate until fat rises to the top and hardens (I usually leave it for 24 hours).  Scrape/skim off fat and freeze or use.  

The stock looks like a jelly when it's cold - it is not a liquid.  

That is my basic poultry stock I've been making for 30 years.  I use it for soups, stews, rice, and basically anything that requires poultry stock.

I rarely do beef stock because I only use it in my shepherds pie (kids and husband don't like beef soups and stews).

I also do veggie stock a few times a year - but that is more based off of what scraps/spices I save and what's on the edge of bad in my fridge.  The only real tip for veggie stock is don't add fresh mushrooms - it makes the stock smell musty IME.
[gbybe8v] (score 169, diepte 0) Can someone give me some pointers on making stock? I've tried roasting bones, I've tried adding more / less / varied seasonings, I've tried adding and removing meats / skin / fat / veggies, I've tried higher / lower temps for longer / shorter, and the end result is always mediocre at best.

My results thus far involve a mountain of effort for very little reward. The cash cost to just start with bouillon is far cheaper than the effort to start from scratch -- at least in my experience.

EDIT: Wow! Thanks for all the advice!
[gbye1xo] (score 141, diepte 1) After years of throwing them out, I literally just discovered this two weeks ago. Unreal how quick you can make a chicken soup with one.
[gbxxm4x] (score 103, diepte 0 OP) I know that people here are familiar with making soup from leftover carcasses and vegetables, but so much more flavor can be found for next to nothing.  I get chicken feet from my farmer's market for $1/lb.  Nothing in the world improves your chicken stock like throwing chicken feet into it.  The end result is rich, thick, and full of collagen.  I also put in a few parmesan rind pieces because I want to use this stock as a base for a pasta dish when it's done, and they'll just crank it up another notch.
[gbyhw6q] (score 60, diepte 2) Here's a fun one, since you make a gelatinous stock, if you grab some dumpling wrappers from an Asian grocery store you can use them to make homemade Xiaolongbao
[gbyliq2] (score 45, diepte 3) You can't really do that with chicken. You need pork bone stock because the gelatin content is higher and it's more solid at room temp. 

Also, as someone who made XLB at home, I would generally recommend avoiding it. It is one of those things that involves a LOT of effort and the product is likely to be medium at best.
[gbyrwxq] (score 41, diepte 2) Agreed. And pressure cooker makes unreal stock in less than an hour.
[gby4qeh] (score 38, diepte 1) They’re delicious. I marinate them in Korean bbq sauce and some other sauces for an evening, then throw them in the slow cooker on high for four hours. Then throw them in the oven for 15mins at 425F to crisp the skin, and then eat them slowly over two weeks or so as late night snacks with a drink. You can’t eat them fast because they take time to eat, so perfect to satisfy my late night cravings.
[gbyd9m2] (score 37, diepte 1) Costco $4.99 all day :)
[gbymd62] (score 37, diepte 2) In professional kitchens the stock is usually made without added salt.  It will be added as the dish with stock is prepared as some ingredients in the dish may have salt in them or spices used to finish the dish may have salt in them. Easier to control the final outcome.
[gbyqo52] (score 36, diepte 4) Only step i would add to that is to first roughly break the carcass apart and throw it in a hot oven on a baking tray for 30-45mins. The more browning on that carcass, the more delicious roasted flavor in the soup.
[gbyn10k] (score 33, diepte 1) The biggest lesson I've made making stock is that nothing replaces the right balance of salt.

I make veg stock, but a big game changer for me was when I started using tomato paste. Another important thing I've learned is that an average stock can make a great soup, so I don't stress too much about the stock.
[gbyfb1k] (score 30, diepte 1) Parmesan rinds add some flavor? Never thought of that use for em.
[gbyjkwi] (score 27, diepte 3) you say that like that's better
[gbyh7hk] (score 27, diepte 2) I keep bags of scraps in the freezer to save up for stock. So when I'm chopping up vegetables, I add the end pieces and extras to the bag. Same with chicken bones and other scraps. Then, I make stock once I have enough accumulated. 

Like OP, I add in chicken feet to round it out and maybe an onion and some garlic, but other than that, it's all just discards I've been saving up. (I get mine from an Asian market.)
[gbykeyh] (score 27, diepte 1) Most people forget to add salt, legit this is the difference between chicken water and stock.  If you ever look at the ingredients in bullion it's mostly salt for a reason.
[gbyw04e] (score 25, diepte 3) Yeah, I was always taught never to add salt to a stock before reducing, as you run the risk if over salting. You can always add salt but you can't remove it.
[gbyh9rd] (score 24, diepte 3) I've only heard negative reviews of adding broccoli stalks (anything brassica for that matter) to stocks. You don't find a bitter or unpleasant taste from them at all?
[gbyphyx] (score 24, diepte 3) Take chicken carcass, remove any excess chicken scraps, keep aside for the actual soup (a cup or so per 6 cups of soup). Put in a pot with saved veggie and herb scraps (celery and onion and carrots are best, parm rinds are amazing, parsley etc). Cover with water bring to a boil and then let it simmer until the bones are clean, and then some. Like 4 hours. Strain everything off then run it through some cheese cloth. Boil longer to concentrate if you want.

For soup: follow your favorite soup recipe and throw in the stock instead of some of the broth or water.
[gbyjlsl] (score 23, diepte 3) I use kosher salt - but I don't think it matters that much because of the long cook time - the large crystals dissolve completely in the initial hard boil.

I've used iodized salt in a pinch too and haven't noticed any real difference.

I use 2 or 3 tsp for a turkey carcass and 1 or 2 tsp for a chicken one - all done by eye.  I have never measured any of my ingredients for stocks.
[gbydq4t] (score 22, diepte 2) Okay good, thanks
[gbz8zj0] (score 20, diepte 4) That's why the junk pieces of the chicken works best. Chicken feet and wing tips have a pretty high gelatin content.
[gbynhsm] (score 19, diepte 2) Would you care to point towards a recipe? Sound tasty.
[gbyvqrv] (score 19, diepte 1) There was an interesting discussion on stocks in one of the cooking subs where there was a pretty big divide between professional cooks and home cooks on what "stock" should mean. A lot of home cooks are used to the "stock" you buy at the store that is basically ready-to-go soup broth and so they are underwhelmed when they follow a lot of recipes for stock which produces something that is comparatively bland. With professional chefs, really all they are trying to do is distill the flavors out of the meat, bone, veg, etc. They're not really trying to season it to taste yet because (1) they may not know what they're doing with it but also (2) there is a good chance they're going to be reducing it so if they fully seasoned it now it'd be over-seasoned when they are done cooking.

There isn't one right answer IMO, but keep that in mind as you look at recipes.
[gbyegz3] (score 18, diepte 1) Same!! With skin and everything for extra collagen
[gbz0jr4] (score 17, diepte 4) I'm gonna barf
[gbyv1j5] (score 17, diepte 3) Sooo much delicious soup from my instant pot!
[gbye5wv] (score 17, diepte 2) I don't understand? $1 buys the feet and the rest are scraps otherwise thrown away. I've never seen this amount of stock at the store for a dollar. Freeze veggie scraps from the week if you don't eat enough to start the stock before they go bad.
[gbyqeda] (score 16, diepte 3) To continue in case you want an actual recipe, take a yellow onion and a carrot and a celery stalk, chop up smallish and brown them up in a little butter in a stock pot. Once they are cooked, pour in a splash water/broth and scrape off all the yummy flavor bits. Add in 6 cups of liquid, more veggies if it’s not to your liking, mushrooms, herbs (sage, oregano, parsley, thyme, rosemary, s&p pretty much anything you’d want in a roast chicken), the reserved chicken bits. Cool until stuff is done to your liking. If you want noodles or rice add those in in the last half hour before eating (make sure to scoop it all out when you serve so it doesn’t get soggy and gross in leftovers). 

Some veggies aren’t good to use for stock (broccoli for example) but if you want them in your soup go for it. It’s a great way to clear everything out. Zucchini and other squashes make great soup.
[gbyq7bn] (score 15, diepte 3) Because each finger has like four bones, and most of the flavor is there. My favorite part is the palm, that has a big glob of tendons that’s fun to chew. Gosh I sound like a villain from Odysseus.
[gbyhrrr] (score 15, diepte 0) Baby, you got a stew going
[gby93ek] (score 14, diepte 0) I've been using my pressure cooker to make [pulled pork](https://nomnompaleo.com/post/111934821818/pressure-cooker-kalua-pig) from a 5 lb. shoulder. After I remove the cooked meat, I use the leftover liquid as a stock for bean & vegetable stew. Nothing goes to waste and it all tastes great.
[gbybqi7] (score 14, diepte 1) Parmesan crusts
[gbybwgz] (score 14, diepte 1) I agree. I don’t think this saves any money. It might work for large families who have a lot of scraps around at any given time. Or homesteads where there is a lot of bones plus veggie processing to be done.
[gbyffoq] (score 14, diepte 1) Adding mushroom does alot for the flavor of mine and luckily? I forget about the mushrooms in the fridge about 20% of the time so they are too earthy for me to want to eat raw but they are great in stock.  

Bay leaves are great.  

Also salt.  The premise stuff generally has salt in it giving the flavors something to bounce off of.  Before salt homemade usually tastes blander.  

I just use whatever is in the freezer bucket so if there is no onion I’m not going to buy one.  Mine is usually baby carrots that dried out too much in the fridge, celery ends, mushrooms, chicken skins and bones, mushrooms and bay leaves.  I cook it for 3-4 hours adding salt bits at a time the last hour,  and the cool in the fridge.  The next day I strain into containers and freeze.
[gby8vde] (score 13, diepte 1) I don't know how to cook them myself (because I suck at cooking everything; I'm working on it, lol), but I just wanted to confirm that chicken feet are delicious on their own. Next time you see it on a menu, give it it a go!
[gbyaqka] (score 13, diepte 0) I eat my cheese rinds. Is that bad?
[gbyw82i] (score 13, diepte 2) My tip: take a laddle of stock and dump a huge pinch into it, then taste. It’ll be very salty, but you’ll also get a sense of how much flavor is in the stock, and then you can salt the pot enough to hit that point.
[gbybazm] (score 12, diepte 0) What are parm rinds?
[gbyh6j7] (score 11, diepte 1) I just can't mentally get past the whole 'eating feet' thing hahaha I'm sure it's delicious, but I don't want to knowingly eat feet!
[gbxzj4q] (score 11, diepte 1 OP) I've never made any other recipes with them.  You should give them a shot though- once you get over the ick factor, they can be really good!  Personal preference always has a say, though.  I prefer chicken feet that are crispy, whereas most places around where I live have them braised and soft.
[gbybo6w] (score 11, diepte 1) I’m not squeamish but I’ve seen live chickens and I don’t think I could ever trust that they are 100% clean.
[gbyhgde] (score 11, diepte 2) Thoughts on using sea salt vs. iodized table salt? I feel like sea salt would be better. How much do you use?
[gbyvlez] (score 11, diepte 2) >Adding mushroom does alot for the flavor of mine

Raw mushrooms are one of the things I refuse to add to stock - it's OK to add them into the soup or whatever your making, but I find it makes stock taste musty (for lack of a better word).
[gbye2mw] (score 10, diepte 2) People can judge me, but there is some real sharp cheesy flavor in those things. Provided it ain't gonna kill me, I'm not gonna stop.
[gbyhjun] (score 10, diepte 3) It’s not that it isn’t very cheap to make, its that broth is not at all valuable in the first place but can take a lot of storage and time.

You can make broth for 8-15 cents per cup using only bouillon (without trying to be frugal, I’m sure you can find a cheaper or sale version) so all the space the scraps and the broth take up plus the time spent making it don’t seem very worth it for the average person. I can see how it would be valuable for a lot of people though, who happen to already spend time on long stints of cooking and always have lots of freezer and pantry space, or use a lot of broth.

This is from my experience as a household of 2-3 with one average fridge/freezer combo and a closet sized pantry. I want to try again though with a plan to use it right away and see how I feel about it then. I have often tried it as an excuse to use the scraps rather than an intentional source of an ingredient that I need. I will make some beans with it next time I have enough scraps.
[gbyifga] (score 9, diepte 2) they last that long after being cooked?!?  weeks?
[gbyk6ta] (score 9, diepte 5) Storing all the scraps and bones when you don't have a lot of fridge/freezer space. The cost of leaving your stove on for that long if you are watching the gas/electric bill. The time spent prepping, as well as cleaning the pot and all the dishes associated with this including utensils, the strainer, intermediary bowls and whatnot, the final storage containers as well as all of your food contact surfaces. Then there's the possibility of doing some small step improperly and giving yourself or others food poisoning which is another hidden opportunity cost/risk.

All of that, or I could buy a carton chicken stock for 2$.
[gbz34yx] (score 9, diepte 3) No difference whatsoever. Sea salt is "nicer" because of the crunch of the crystals, but dissolved they are chemically identical. If you have iodized on hand, salting liquids is the best use for it, IMO.
[gbzan17] (score 9, diepte 5) Sure but that's going to dilute it. The point of reducing is to reach a desired concentration.
[gbypql3] (score 9, diepte 1) Not just for frugal's sake, it's the secret to a really good stock even if you have to pay more for them! Chicken feet have tons of collagen that's good for you skin and joints! They add richness and body to the soup! They are quite traditional. 

I get that they may be too weird for some people to work with, but it's not something one adds just because they are cheap.
[gbyxb0y] (score 9, diepte 1) It's a common asian food 🤷‍♀️
[gbzltuz] (score 9, diepte 0) So i was reading through a lot of the comments and nobody seemed to mention vinegar?  I learned a long time ago in an old cook book, you add a about a tablespoon of vinegar to your stock. It enriches the flavor, and the acid leeches more minerals and calcium from the bones... to make that stock more nutrient packed. Does anyone else do this?
[gbygz0p] (score 8, diepte 2) they are awesome- asparagus bottoms and broccali stalks too
[gbyq5rg] (score 8, diepte 3) Yea...I’ll be honest, I eat them over like a month with no issues. I was a little embarrassed to admit that in my first post. There’s very little moisture after blasting in the oven so that’s probably why? Not a scientific conclusion.
[gbyl05e] (score 8, diepte 4) Honestly, I don't think you're wrong. It's really only useful if you use a fair amount of stock. We use a lot, so I make broth/stock sometimes and save it. I think it tastes better than store bought bullion and it saves me a few bucks on boxed broth.
[gbz9it0] (score 8, diepte 4) You're not wrong, but frugal foodies exist, and when it's done right, a homemade stock is infinitely more tasty.
[gbyko8o] (score 8, diepte 4) I can get behind that, I like doing stuff by eye, too. Thanks!
[gbzp0ld] (score 8, diepte 4) Sea salt now has microplastics in it. Yummm!
[gbymwrz] (score 8, diepte 1) What I tend to do is keep a few big Ziploc bags in the freezer, and toss in whatever veggie scraps I end up with, along with chicken bones/skin. When a bag's full, I toss it into my slow-cooker on low for 6-8 hours with a few spices. It's decent stock every time. The one thing I've realised is that I *always* forget to add salt.
[gbyely7] (score 8, diepte 0) Cheapest chicken parts where i live are usually the legs, is never the feet.
[gbyn8m7] (score 7, diepte 4) Comfort zone challenge for you! Order the chicken feet!
For added surprise ask them for fung tsao.

Or show them this -> 鳳爪
[gbyifto] (score 7, diepte 1) Best blonde chicken stocks are made with chicken feet. Roast them first simmer for a good few hours, or less depending on quantity. Then remove everything in the stock. And reduce by half. Makes a beautiful base for any gravy or sauce.
[gbyvz32] (score 7, diepte 1) Just a note for people using feet for the first time:

They may come pretty sandy, so always give em a good rinse. You can also clip the claws with scissors so that you don’t get poked.

You can instantly taste the difference between a feet stock and non feet stock IMO, and I much prefer the former.
[gbz3uwb] (score 7, diepte 5) Lol fair, don’t blame you. Barf away.
[gbydkai] (score 7, diepte 1) I mean, it's fine if youre okay with eating dirty wax/paraffin.
[gbydrxp] (score 7, diepte 1) Me too 😇
[gbyifcy] (score 7, diepte 4) What I do is just save all my vegetable scraps in a zip lock bag in the freezer. Then I'll take whatever bones, usually rotisserie chicken, throw everything into a slow cooker. Add some water and then you have a broth with minimal effort the next day.
[gbzls05] (score 6, diepte 6) Suddenly I'm wondering why the hell I decided to read thru all this while eating 🤢
[gby4yap] (score 6, diepte 0) Pig’s feet are great for stock too!
[gc05665] (score 6, diepte 5) Since it’s a rotisserie chicken isn’t it already roasted?
[gc08dgf] (score 6, diepte 6) If you roast just the bones it deepens the flavour.
[gbzkias] (score 6, diepte 2) As a side note:

If you are using chicken bones, you must make the stock in a separate step from the actual soup. Chicken carcasses have lots of tiny bones and other bits you definitely don't want in your stew. (I learned this the hard way!)

Other kinds of large bones, like ribs, you can just cook with your stew (e.g. in the Crock-Pot) and remove them before serving.
[gbyuate] (score 6, diepte 4) Stock can be easily frozen in sour cream containers.  This way it gives you the 2 cups you need for a single recipe.

I typically make a soup/stew on day 2 of the stock and freeze leftovers into pot pies.
(192 reacties met lagere score weggelaten)

=== THREAD qmq6eg ===
SUBREDDIT: r/Frugal
DATUM: 2021-11-04  SCORE: 340  REACTIES: 264
TITEL: How to keep feet warm when working in a cold room?
POST (source_id=post):
I've been trying to avoid over-doing it with the heating this winter (not just for money, I also hate the dry air that comes with it).

&#x200B;

So far it's not so bad, cozy even, but the one thing that drives me crazy is how cold my feet get when sitting at my desk. Wool socks don't seem to make a dent at all, as if my feet can't even produce their own heat! They seem to get cold even when the rest of me is uncomfortably warm.

&#x200B;

So far the next best thing is sitting in my chair cross legged with a blanket over my lap, but I can only sit like that for so long.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hjbbwo7] (score 351, diepte 0) Insulate your feet from the floor.  Put a folded blanket or comforter under your desk and put your feet on it.
[hjbhg2j] (score 170, diepte 0) Couple things here to help taken from many years guiding snowshoeing, whitewater kayaking, and SUP.

1. Footwear. Nice warm socks and insulated shoes/slippers/boots are great, but you have to keep them LOOSE. If you cram your thickest pair of wool socks into your regular shoes, you will restrict blood flow (which is what keeps you warm). The same goes for lacing your shoes too tightly.
2. Warm the whole system, particularly the core. If you have longer socks, that helps too, but the most critical part is your core. If your core is cold, your body will shunt blood flow from your extremities until your important bits are warm enough. It does create a bit of a feedback loop though, as there is still blood going to your cold extremities before coming back into your heart and lungs, so keep your core temp up!
3. Avoid vasoconstrictors and dilators! stimulants like caffeine and Adderall are vasoconstrictors that reduce the volume of blood that can flow at once. I still take my adhd meds though, otherwise I end up on reddit in the middle of the day... wait a second.... Vasodilators, like alcohol, increase blood flow all over your body, including your skin. This may give you a momentary flush of warmth, but ultimately just facilitates the loss of heat. Definitely don't mix the two unless you like exploding heart syndrome (ok, that may be a bit hyperbolic in most cases, but mixing uppers and downers is not great for your body).
4. Use something warm (warm water bottle, heating pad, etc.) and place it around your calves/behind your knees rather than directly on your feet. Let your socks keep insulating your toes and add heat to the thinner skin and larger blood vessels. Here's a [short article](https://www.army.mil/article/215456/talk_to_the_hand_army_researchers_developing_tool_to_warm_hands_without_gloves) about how the US Army is using this method. I know some paddleboarders in Canada that paddle through the winter (as long as the river isn't frozen) that use chemical hand warmers like this, but particularly on their belly (again, gotta keep the core warm first).
5. moving around will help increase blood flow. For best results, use vigorous movement that doesn't make you sweat. temperature exchange works both ways, so just forcing warm blood into your toes and cold blood back to your core will still trigger your body to focus on "survival"
6. Ninja edit - drink more water. Staying hydrated is super important for thermoregulation. Most of us are chronically dehydrated anyway, and in the winter we don't notice it as much because we aren't sweating, but the air is also usually drier.
[hjbcty1] (score 129, diepte 0) If you're at a computer, put the case down by your feet.  It's amazing how much heat they put out.  Seriously, they're a space heater that happens to have a mouse & keyboard.  Just be aware computers like to pick up dust - you will need to clean the case regularly.
[hjbag7j] (score 86, diepte 0) I am amazed how cozy by normally cold feet are in wool fleece lined slippers. Mine are from LLBean and are worth every penny. Fake fleece is nowhere near as warm.
[hjc81qh] (score 74, diepte 1) Yes. I go with warm socks and substantial slippers. Works for me but YMMV!
[hjb5s13] (score 55, diepte 0) LL Bean fuzzy slippers. Not cheap but worth the investment.
[hjc3xj9] (score 50, diepte 1) This.  
  
No.2 is the big ticket that most people ignore. A simple fleece vest can make a world of difference over just a hoodie or long sleeve shirt
[hjb8mve] (score 46, diepte 0) Heating pad
[hjbc5b4] (score 37, diepte 0) Get up and walk around often.  Need to keep the blood flowing.
[hjbdyxl] (score 35, diepte 0 OP) This is why so many office workers keep a small space heater under their desk. You could also use an electric heating pad or blanket.
[hjc4wn0] (score 29, diepte 1) Thank you for explaining why my feet are cold in thick wool socks and warm ass slippers.
[hjciust] (score 24, diepte 1) I was just coming on to say this!

I also wrap a blanket around my chest so the length covers my legs and feet too, leaving my arms free if I need them out to work/game.
[hjbogap] (score 24, diepte 0) I use my dog.
[hjdf05m] (score 23, diepte 2) To add to this....good quality merino wool socks will keep your feet warm and also help them "breathe". Synthetic materials may cause your feet to sweat making the socks and lining of your shoes soggy and eventually cold.
[hjbh7s6] (score 23, diepte 0) I use an electric heat mat like this https://www.americanfloormats.com/heated-floor-mats-heavy-duty-boot-warmers/. Shop around, mine wasn’t this expensive. I like to put something between it and my hardwood floor to avoid damage, and I use one of those plug-in switches with a light to remind me to turn it off after hours.
[hjcmw5r] (score 21, diepte 1) Or hot water bottle! Old school and it WORKS
[hjc3knx] (score 20, diepte 2) I just take a shit outside at the Wendy’s
[hjc6qel] (score 19, diepte 1) Love my LL bean wool-lined moccasins, one of the best gifts I've gotten in several years.
[hjbdvxn] (score 19, diepte 1) Genius!
[hjc9dyv] (score 18, diepte 2) I swear I took my meds today. I guess my work just isn't as captivating as a stranger's cold feet? Oof. I need a new gig.
[hjc7tfl] (score 17, diepte 1) The middle of the 3rd point was perfection ha
[hjb69zn] (score 16, diepte 1) This. Maybe ask as a gift. They will last for years and make a huge difference.
[hjcrwwo] (score 15, diepte 1) I've been guilty of firing up hyperpi for a bit of extra heat in the past.

if you have a decent gpu then mining makes a bit of sense in the winter.
[hjcxafu] (score 15, diepte 2) In college when I didn't pay for electricity I would do this. Made a few hundred that is now worth a few thousand. Currently hodling
[hjboyiz] (score 15, diepte 0) Question: do your toes get so cold that they turn white and numb?
[hjcmfny] (score 14, diepte 1) Or get one of those heating pads for dog cages, they're made to stay on the floor. Personally, I've been looking at a heat lamp/sunlamp for me and my cats now that winter is settling in here. They get the sunlight feel, I get the it too, and if I get a therapy light for me, none of us have to get SAD
[hjdgcn6] (score 14, diepte 1) To add to "if you work at a computer...". I love putting a heating pad under my feel. I also get cold feet easily.
[hjcns87] (score 14, diepte 1) That happens to me, I've self-diagnosed this as Reynaud's syndrome. Some people get this in their hands instead/as well. For me it basically means that preventing my feet from getting cold is super important because once they're cold it's a quick slide into numbness and then extremely difficult to warm back up.
[hjcdtz1] (score 14, diepte 1) I've heard of this, but with rice instead of popcorn.

Edit: uncooked rice that is...
[hjb9tpp] (score 13, diepte 0) How about some UGG type cozy boots?
[hjbk1g6] (score 12, diepte 0) I have an office that is CRAZY cold.  One of the things that helps is taking a water bottle and filling it with hot tap water.  I place it between my thighs ore under an arm and it makes a difference.  As I understand it there are major arteries in these areas and it warms the blood and brings that heat throughout the body.  I would try also resting it in ewe em your feet.  I hope it helps.
[hjdbanl] (score 11, diepte 2) Slippers and socks do it for me too. Pants tucked into my socks if they're a bit loose.
[hjcp8ge] (score 10, diepte 1) I have sheepskin lined leather slippers from LL Bean that I bought off of eBay for about half of what they go for new. I’ve had them for *years* and the inside lining under my feet has begun to wear down. I bought some sheepskin liners from Amazon and we’re back in business. They keep my feet nice and cozy.
[hjbc6wf] (score 10, diepte 0) Minnetonka moccasins
[hjbjjsc] (score 10, diepte 0) Get a warm blanket you don't use much. Fold up into pouch and insert heating pad. Feet can go on top, under or inside pouch depending on toastiness desired. I use binder clips to secure the pouch to the floor protector so I never have to look for it or refold the thing.
[hjbu4zq] (score 10, diepte 0) Popcorn bags are my go-to for staying warm in Winter. You can sew together a [cute bag](https://imgur.com/a/iPlm9hP) or just use an old sock. All you have to do is fill it full of popcorn kernels and put it in the microwave for 3-4 minutes. They won't pop; they just get hot. You could set one on or under your feet while at your desk.
[hjcg77i] (score 9, diepte 1) I am partial to Ugg slippers. Had a couple over the years, and it can be freezing in the room, and my hands will be so cold I have a hard time using the keyboard without hugging a hot coffee cup every few minutes, but my toes are in toasty town. Again - they ain't cheap, but totally worth it.
[hjdfkkn] (score 9, diepte 1) Agree that wool socks PLUS a good natural fiber slipper is the only thing that knocks the chill off of my feet.
[hjbosf8] (score 9, diepte 0) For me the best thing I can do to warm up my feet is wear a really good wool hat. An old mentor of mine used to say “of your feet are cold out on a hat” it works for me.
[hjdfn21] (score 8, diepte 3) For extra warmth, layer.  Wear a pair of thin cotton socks underneath your wool ones.
[hjdaqlj] (score 8, diepte 1) Actually illegal (code violation) in some places!
[hjdj2ra] (score 8, diepte 1) I totally put my toes under my dog when we are on the couch.
[hjcxnd9] (score 8, diepte 2) Exactly! I grew up with cherrystones, but it can be a lot of things: rice, peas, lentils, ... Whatever you have lying around in your pantry. And you can also warm it up in the oven.
[hjc5ls9] (score 7, diepte 1) I was given a pair as a teenager that are still keeping my feet toasty as a 42 year old, they last quite a while.
[hjci5ub] (score 7, diepte 1 OP) My family has always been big fans of the shearling slippers from LLB. To buck the trend I went with felted wool slippers from Glerups - they are freaking great too.  Worth considering if you are in the LLB price range.
[hjbtnxa] (score 7, diepte 1) Go to a bathroom that's further away, maybe take the stairs
[hjc4h6b] (score 7, diepte 3) Good walk to keep your feet warm
[hjbejkz] (score 6, diepte 0) If you don't want to go all out with buying shearling lined slippers, you can find shearling insoles to put in your shoes/slippers for around $10.
[hjbjxbx] (score 6, diepte 0) Wool thick socks. Got one my self and use it always during winter, loved it so much ended up buying few more. They were like $10 but worth it. And they also had non slip thingy under it. 

When it gets too cold I turn on the small heater I got in the garage where I sit to do some work if I’m doing it out.
[hjdbn77] (score 6, diepte 1) I had a friend do this with dried corn from the feed store. It’s a lot cheaper, it’s just not very good quality and might need to be cleaned, but it works great.
[hjc55u7] (score 6, diepte 0) >as if my feet can't even produce their own heat! They seem to get cold even when the rest of me is uncomfortably warm.  


You might want to get this checked out. Not likely to be urgent (unless it is a recent and rapid change, and worse in one foot), but bad circulation is a issue that should be addressed and not just camouflaged.
[hjci8s9] (score 6, diepte 0) I have a hot water bottle that I fill with super hot water and rest my feet on it. They stay nice and toasty for at least an hour and then warm for a couple hours after.
[hjbzowc] (score 5, diepte 3 OP) The sperry ones or the high top ones?
[hjcnnoc] (score 5, diepte 1) I bought one about a month ago and it’s on my foot rest. I wear socks and rest my feet on the heating pad. 

Ahhhhh….
[hjbamv3] (score 5, diepte 0) Wool shearling-lined slippers. I think mine are from Acorn? They also make down booties that would def keep you toasty.
[hjdjq9l] (score 5, diepte 4) You should also ensure you aren't tying them too tight, if your feet are squished in super tight the blood flow is restricted. 

New insole may also help, I remember as a kid my grandfather used yesterday's newspaper to make his own insoles along with the wool socks as well.
[hjbl4p7] (score 5, diepte 0) Change socks a few times a day.  Once they sweat a bit, it just causes cold feet.
[hjbnq2l] (score 5, diepte 0) This is weird but works for me in the winter. A pinch of cayenne pepper in each sock in the morning. But only once a week.
[hjcwzgr] (score 5, diepte 2) Don't know if it's mumbo jumbo but it's supposed to increase blood circulation, works for me.
[hjd5lk2] (score 5, diepte 3) Does it work in condoms?
[hjd7ohn] (score 5, diepte 0) Put on a hat.

Not joking.
[hjbfsiu] (score 4, diepte 1) Yeah. I got a pair of these this summer and only just started wearing them recently because they’re too warm most of the time.
[hjbs0cq] (score 4, diepte 2) That's what I have and i barely notice it's there. And i don't get cold. If you do you'll appreciate the bonus.
[hjcmigf] (score 4, diepte 1) I miss this now that I have a laptop. But I run a hdmi cord to the TV screen now so I could do this still...
[hjbjfcm] (score 4, diepte 0) Specifically, **merino** wool is your friend, especially if you get sweaty feet. Make sure it’s legit and you’ll be very happy with the difference in my experience.
[hjbphz9] (score 4, diepte 0) They're a bit pricey, but I highly recommend a Far InfraRed Heating Pad. They are the bomb and unlike a standard heating pad, the Far InfraRed actually penetrates several inches into your body. 

My wife swears by hers after a day in the OR at the hospital. 

Another benefit is they do not have high levels of EMF and release beneficial Negative Ions. I pulled a back muscle racking a server last year and that Far InfraRed pad was better than any pain killer. Plus it made me sleep very soundly.
[hjcb2n6] (score 4, diepte 0) If you have any pets, train them to sit on your feet
[hjcgl8a] (score 4, diepte 0) Consider the fact that you might have [Reynaud's Syndrome.](https://www.gwapodiatry.com/library/how-podiatrists-treat-cold-feet-from-raynauds-disease.cfm)  If you do, speaking from experience, once your fingers/feet get cold, it will take a long while to warm them back up, unless you're able to soak them for a good 15 minutes in a basin of hot water.

1) use a timer or software to make you get up and move for about 10 minutes every 45 minutes.

2) Thigh high socks as your base layer sock.  Makes a huge difference.

3) look into getting a footrest with a heater in it.  At work I  have a Fellowes Climate Control Footrest and it makes a huge difference in comfort.

4) Look into getting a heating pad or hot water bottle if you can't do the footrest, or you'd like something useful all over the house.
[hjcn7dx] (score 3, diepte 1) YES! I got one last year and wish I'd done it sooner. I use it during the day and also use it by my feet under my blankets at night. Game changer!
[hjdd45w] (score 3, diepte 1) I put dry rice in a sock, tie off the end, and microwave it. It gets really hot and holds heat well. Smoosh it around to find the heat in the center when the outer layer of rice cools. Re-nuke as needed.
[hjbrih7] (score 3, diepte 1 OP) Is it worth it to get the ones that are more sperrys shaped or the ones with the high tops?

I think my ankles get pretty cold too but I can see that getting annoying too.
[hjcqr8w] (score 3, diepte 2) I have the high top ones. I have two pair that I got off of eBay and I’ve had them for many, many years. I love them. Recently had to get sheepskin inserts though, as I’ve work out the liner.
[hjc7pyx] (score 3, diepte 1) I paid $70? For a pair last year. Amazing what they do. Regret not splurging for them sooner.
[hjeuqtv] (score 3, diepte 3) Also change your wool socks regularly to stay dry.
[hjc4hwm] (score 3, diepte 3) Dude not cool! I was gonna go there!
[hjcalnh] (score 3, diepte 2) Those sound cozy! When I need a new pair I might have to point hubby in that direction
[hjbcfqn] (score 3, diepte 0) One of those really small personal heaters aimed at your feet. I know lots of people who put those on the floor of their cold offices. 

The foot warmers that hunters use for really cold days.
[hjbd4gq] (score 3, diepte 0) Tbh, the quality of some Walmart products have gotten so much better. I purchased fuzzy slippers from them for $15 and they’re great
[hjcic7x] (score 3, diepte 2) ps: and I have those wonderful llbean slippers and no, they are not enough in my cold house!
[hjcnyah] (score 3, diepte 1) Fascinating!
(179 reacties met lagere score weggelaten)

