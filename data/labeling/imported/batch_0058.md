# Label-batch batch_0058

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
Schrijf het resultaat naar `batch_0058.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: roepv9, ryo66t, 1anrn7r).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD roepv9 ===
SUBREDDIT: r/bartenders
DATUM: 2021-12-25  SCORE: 60  REACTIES: 111
TITEL: Desperately need your work shoe recommendations
POST (source_id=post):
I've been in this industry for a solid 15 years, and I've owned Shoes for Crews, Dr. Scholl's, Skechers- I've used every kind of insert imaginable, I've bought comfy shoes and simply sprayed them down with waterproofing, but this new job is destroying every shoe I throw at it. I'm on marble floors all night, and the only areas that get wet and present any slip hazards are rubber matted, so at this point I'm willing to leave the non slips behind if it means my arches will stop collapsing in on themselves and my heels will go back to being round. They need to look fairly professional, and as a short female bartender in a deep well, deep cornered bar, with way too many high shelves I definitely wouldnt mind some extra heel height. Like, seriously. I'm 5 feet tall and I cant reach a damn thing. Very, very hoity toity fine dining, coursed dinner where I need to reset my patrons for every course with fresh silver and I CANT REACH. I've been googling for weeks, and at this point I'm just at the mercy of the community- what do yall think?

Edit to add: I worked this place for a couple months over a year ago, and it gave me plantar fasciitis. I've been back for less than a month and its flaring up again, so if theres anything specifically good for that, please let me know. Thanks in advance, Bartner!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hpxyc6j] (score 79, diepte 0) I just roll with Doc Martens and say a prayer every shift.
[hpxz0g7] (score 45, diepte 0) If you can wear boots I am a huge fan of Blundstones chisel toes
[hpyd92g] (score 34, diepte 2) 8 miles is the length of 2801.98 1997 Subaru Legacy Outbacks
[hpxyi0c] (score 26, diepte 1 OP) Holy crap, Docs are so heavy, you must have the legs of a god.
[hpy742o] (score 25, diepte 2) I wear docs too, the pull on Chelsea boot kind. As long as they’re a right fit (should be a bit snug at first), I have had no problem with the weight. Best support by far
[hpyd89e] (score 25, diepte 1) Any of the blundstones really. They’re light, comfortable, waterproof, and have good grip. I wore the originals for a couple years, then the chisel toes, and now the dress boots. 

I also walk 8 miles a day in them as a dog walker and they last me about a year each. Unfortunately they can’t be resoled but they’re worth every Penny.
[hpxunp0] (score 21, diepte 0) Running shoes! Hoka if you can afford them. Changed everything I knew about standing for 10 hours
[hpy99gv] (score 18, diepte 0) I'm a woman so this might not apply to everyone but I swear the best shoes are Jessica Simpson Ballet flats with the ankle straps. They are slip proof and comfy as hell and practically indestructible. I wore them behind the bar for an entire baseball season in Chicago the year that the Cubs won the world series.  A comet could strike the earth and all that would be left would be smoke, ashes, and Jessica Simpson ballet flats.
[hpyd875] (score 13, diepte 3) Same, I wear the double sole Jadens, protects my feet from liquid and glass, I can reach high up things because am smol, and my arches don't feel like they're collapsing at the end of the night. Plus, running up and down stairs when I have to get something keeps my legs super toned.
[hpyaqvf] (score 13, diepte 0) Dansko clogs. Im a short bartender too. I live and breath by my dansko clogs

They will give you an extra two inches, your feet and back never hurt, and i get a solid year out of a pair.
[hpy60hh] (score 12, diepte 0) Redwing Iron Rangers with insoles. Been re-soled once in four years. New insoles every 9-12 months. Best work shows I’ve ever owned.
[hpy3c4l] (score 11, diepte 2) I also wear boots all year round.
[hpxxkj1] (score 10, diepte 1 OP) Brilliant, thank you! They would certainly weigh a lot less, which I would appreciate!
[hpyn305] (score 9, diepte 1) Also gonna second the Blundstones rec. My first pair lasted me 4 years, while working as a barista bartender and waiter and living in NYC walking literally everywhere. You can dress them up or dress them down however you want. I wear them in the snow and in the summer. I've taken them on backpacking trips and worn them to job interviews. What else do you need?



P.S. I use Superfeet insoles with them, totally stopped all the pain I used to have after shifts.
[hpys9xr] (score 7, diepte 1) This. I add extra waterproofing so they’ll last longer behind the bar and stay cleaner. And OP- ADD COMPRESSION SOCKS if you aren’t already! They’re a serious game changer in combination with good shoes.
[hpxtdoh] (score 6, diepte 0) I use these but sadly they seem out of stock now. I do however use them with a set of custom insoles. Since buying these in 2018 I've had them resoled once and that's it.   


  
[https://www.amazon.co.uk/gp/product/B00NW8FSSG/ref=ppx\_yo\_dt\_b\_search\_asin\_title?ie=UTF8&psc=1](https://www.amazon.co.uk/gp/product/B00NW8FSSG/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
[hpzbmxi] (score 6, diepte 1) No way those are comfortable they have a thin sole
[hpyymf4] (score 6, diepte 1) Absolutely, dansko or Birkenstock shoes/insoles. It ain’t about the cushion but the support. Despite the break in period, Birks saved my lower back knees and ankles.
[hpy49km] (score 5, diepte 0) Blundstones rule
[hpyboa8] (score 5, diepte 0) Check the Vans model for the industry
[hpysego] (score 4, diepte 1) Been wearing Docs for the last few months lol best work boots I've ever had. Got a pair of Vans non slip for Xmas so we'll see how they hold up tomorrow.
[hpz691h] (score 4, diepte 2) Yeah, the soles are made of the same type of material as the supposedly slip resistant sneakers I used to wear but these grip better. And I'm clumsy as fuck
[hpznj8w] (score 4, diepte 1) --This ad brought to you by Jessica Simpson--
[hpxtvdp] (score 3, diepte 2) This is them here, they're quite cheap but they do me fine, you cut them yourself to fit your feet. Currently I use them in my work shoes, my main shoes for out and about and I'm in the process of getting another pair which I'm going to try in my snowboard boots.   


https://www.amazon.co.uk/gp/product/B00IMKPWXU/ref=ppx\_yo\_dt\_b\_asin\_title\_o00\_s00?ie=UTF8&psc=1
[hpzflhz] (score 3, diepte 1) Hoka is great! You'll just have to replace them more often since they're foamy and won't last as long as heavier footwear. 

They also make slip resistant Bondis!
[hpyra1o] (score 3, diepte 2) They also have some Chelsea boot style platforms that may help with the height, although just the regular style adds some height as well. I wear the Chelsea boot slip ons and just buff em up before my shifts to make them look more professional. You get used to the weight fast!
[hpzffq5] (score 3, diepte 1) Blundstones + Superfeet insoles for arch support. I can wear them every day.
[hpy5mlh] (score 3, diepte 0) SAS are my go to shoes
[hpy9mcc] (score 3, diepte 1) They're expensive, but they're basically construction  boots that look nice enough to wear with a suit.
[hpyi7cl] (score 3, diepte 2) Not long, I sized down and they stretch to form your feet.
[hpyuq34] (score 3, diepte 4) I don’t wear them with insoles. They are pretty uncomfortable though. Took me about 2 weeks of constant wearing for them to form to my foot. Now they’re honestly one of the most comfortable shoes I own. Id recommended using a leather conditioner or oil (depending on the oil it might darken the boot) to soften up the leather and help break them in quicker. Another shoe by redwing is the Black Smiths. Built on the same platform as the Ranger but with out the extra leather toe cap so it’s a bit sleeker. I’d also probably break them in first then add the insoles or they might hurt a bit depending on how wide your foot is.
[hpytgll] (score 3, diepte 1) To piggyback ; danskos were close but not quite right for me, the Dr scholls version were it. Slightly narrower, slightly more squish. The style took some getting used to but the height, arch, and thick sole absolutely bought my feet a few more years. Also enough foot protection without having to go boot, depending on what your environment is like. Good luck, OP. 
Also edit to say, for what it's worth I am f and older; flats, tennis shoes and day boots might be easy for a shift or two but absolutely won't serve you in the long run and will get destroyed/destroy you with any kind of real bar action. Don't sacrifice the feet and shoes you already love.
[hpynzyy] (score 3, diepte 0) I highly recommend compression socks/stockings (15-20 mmHg), custom orthotics from a reputable podiatrist, and Doc Martens in pascal leather. 

I used to wear running shoes with regular cotton socks and ended every shift in immense pain. Since switching them out for what I wear currently, I can work five ten-hour shifts in a row and feel great at the end of every shift.
[hpxtk40] (score 2, diepte 1 OP) Custom insoles? Where did you get those? I remember back in the early aughts they had those machines at shoe stores you could step on that would map your weight in your feet and order insoles for you, but I havent seen them in years.
[hpxuduz] (score 2, diepte 2) I've had 2 pairs of those boots now and each have lasted me about 5 years in total. I reckon my recent pair will last longer since I had the resole.   


One last tip I will give if you're getting sore feet is remember to moisturise, a little before a busy shift but always afterwards before you go to bed. It really does make the world of difference.
[hpxyeej] (score 2, diepte 3 OP) Ooh, thanks for the tip, that's not something I've ever considered! Ive always been afraid to lotion my feet properly before a shift, worried that I might get athlete's foot from all the moisture that can build up during a shift, but also I've never even had athlete's foot, so why not try and see if it helps? A return tip on general moisturization as a thank you- there are lotions that come in a spray bottle as opposed to a thicker cream, I keep one in my shower and mist my whole body after drying off, while standing in the tub so I dont have to worry about overspray. Rub it all in, hop out the shower and rinse the tub real quick to send any excess lotion down the drain, and no more winter dry skin! Changed the game entirely for me, because I never had the patience to moisturize my whole body before.
[hpywqq8] (score 2, diepte 2) REI carries that brand and others, and you can find good deals on clearance especially if combined with the membership coupon. Also don't forget the right socks (merino wool are a good choice).
[hq0zul4] (score 2, diepte 2) nike free runs are always at nordstrom rack and i love them!!
[hpz8bsc] (score 2, diepte 1) I came here to recommend Hoka as well! Obligatory I’m not a bartender, but I am a nurse and I average ~15k steps a day, up to 20k+ and I swear by them
[hpz2ihj] (score 2, diepte 2) They make a dress shoe cut that are my go to industry shoe. Light weight and slip resistant. They used to have shoes for life where they would resole or replace them if they got worn down
[hpyfmse] (score 2, diepte 1) Maybe I got a bogus pair, but those were the most uncomfortable boots I’ve ever had. How long did they take for you to break in?
[hpys692] (score 2, diepte 3) Yea I remember them insisting on sizing my feet at the red wing store and coming out a full size smaller than what I normally wear. I remember being really bummed because they were so expensive. I didn’t try them with inner soles though, so I’ll give that a shot. Any ones you recommend?
[hpz7alt] (score 2, diepte 5) I had the black smiths before the iron rangers. I managed to trade them in for the iron rangers after like 3 months because they were destroying my feet. I conditioned both with mink oil, shoe stretchers, etc. Maybe red wing just hates me.
[hpy86xa] (score 2, diepte 0) Birkenstock London’s with a non slip sole. Super comfy, and best non slips I’ve ever encountered.
[hpz0l57] (score 2, diepte 1) Where did you get red wings for $150!?
[hpydw53] (score 2, diepte 0) Go to a running store and have your stride evaluated. Then ask for recommendations from them.
[hpyedzd] (score 2, diepte 0) Mozo. Pricey, but actually lasted over a year before falling.apart. Very little breaking-in needed, comfortable, and no foot pain (sometimes have PF flair ups).
[hpygm6v] (score 2, diepte 0) If you don't mind boots\heavier leg ware, magnum makes fantastic nonskid shoes. As for the height thing, just ask a taller coworker for help. I'm 6'6" and often joke I got hired for height over the ability to cook
[hpxu58z] (score 1, diepte 1 OP) Also- I had never heard of the Rieker brand and I'm now doing a deep dive through their reviews- seems like they are very well loved! Thanks for the recommendation!
[hpyiqpa] (score 1, diepte 1) https://www.rieker.co.uk/rieker-mens-footwear-c1/mens-shoes-c76/rieker-36050-00-mens-black-zip-boots-p791
[hq08adw] (score 1, diepte 1) I wear Hokas as well. I was worried about slipping but I just tread lightly. I haven't had any problems with my feet or back since I made the switch. Haven't slipped and fell yet either.
[hq12fsq] (score 1, diepte 3) Good bot
[hq12g4r] (score 1, diepte 4) Thanks!
[hq12gpf] (score 1, diepte 4) Thank you, thecoffeetalks, for voting on useles-converter-bot.

This bot wants to find the best and worst bots on Reddit. [You can view results here](https://botrank.pastimes.eu/).

***

^(Even if I don't reply to your comment, I'm still listening for votes. Check the webpage to see if your vote registered!)
[hpy5csq] (score 1, diepte 0) I roll with Ecco shoes. All the styles I’ve gotten are incredibly comfortable/durable. Some have Gor-Tex as well.
[hpymavn] (score 1, diepte 1) My husband is also a bartender and swears by the slip ons! Personally I wear Docs but he keeps telling me to invest in SAS shoes.
[hpz5dut] (score 1, diepte 2) And they last forever!
[hpzgfzo] (score 1, diepte 6) Never tried Redwings but I love good leather loafers. If you have a car, driving around with thick socks and the foot heater on high to warm up the leather has helped me with break in period before!
[hq0c4n5] (score 1, diepte 6) I mean give them another shot and if they don’t work out I’m a size 11. 😁
[hq7p6sk] (score 1, diepte 2) My Iron Rangers had like almost no break in period. They are suuuuper comfortable. Im guessing you got a bogus pair or perhaps the cut just isn't right for your foot
[hpy6yhj] (score 1, diepte 0) I wear new balance slip resistant shoes at work. They are pretty much an all black running shoe with a slip resistant sole.
[hpy740b] (score 1, diepte 0) Same here, just got mozos and put supergreen insoles in em. 6 months with a happy back and happy feet. Given its a $170 dollar investment but I'm happy
[hpy7yqv] (score 1, diepte 0) it sounds like you’ll be better off finding a good custom insole to use on shoes you already prefer 

my recommendation was gonna be docs and their comfort insoles, but vans with the UltraCush insoles are amazing too if you’re looking for a lighter alternative
[hpy87zc] (score 1, diepte 0) I sucked it up and bought a $150 pair of red wings. 
Been bartending for 20 years,and I'm kicking myself in the ass for not doing it sooner. Way too many pairs of Skechers, Dr. Scholls,the wal mart special and shoes for crews,before realizing how much of a difference a well made and more importantly fitting shoe makes.
[hpzhvva] (score 1, diepte 2) The red wing store. They may have been 159.00 or 149.00. But definitely not more than that.
[hpz575j] (score 1, diepte 1) are they really slip resistant?
[hq1taul] (score 1, diepte 2) Ha! I know but it so hard to find good shoes
[hpyevml] (score 1, diepte 0) Crocs and blundstone both have service shoes that I have liked!
[hpyfao2] (score 1, diepte 0) Have a pair of palladium boots that fit like a glove, good durability, decent traction. Haven’t had the sore-foots since.
[hpyfzb2] (score 1, diepte 0) It's all about Sanita if you don't mind wearing a clog, had back problems and sore feet for months, gone, they're a little pricy but worth every penny.
[hpyhap8] (score 1, diepte 0) SIKA Bubble Steps

Best Shoes ever.
[hpyimwe] (score 1, diepte 0) Copped a pair of New Balance trail running shoes on sale for 30 bucks. Figured I could destroy them at work. They’re very comfy but man be super careful of wet tile. Since the have tread there’s not a lot of surface contact and they’re like ice skates.
[hpyk55b] (score 1, diepte 0) I’ve been rocking Redblacks! Take a bit to break in, and a bit pricy, but super high quality, all leather, give an extra smidge of height, good ankle support, professional looking, and my feet don’t feel worn out after an 8 hour shift!
[hpyqj3j] (score 1, diepte 0) Try Hoka running shoes. They're really cushioned and will add a little height.
  Also make sure you're getting enough electrolytes as that's a contributing factor to fasciitis.
[hpyqj7w] (score 1, diepte 0) I’ve been rocking crocs lately. They have some that look like running shoes & some that are clogs that don’t have holes. I’ll never to back, fashion be damned.
[hpyrn13] (score 1, diepte 0) Vans with inserts never led me wrong when I worked on concrete floors
*the sneaker style vans, with laces. Not the flat slip on
[hpyrzex] (score 1, diepte 0) I actually got a stress fracture and had to bartend in a boot for half a year due to wearing converses, would not recommend. Currently rocking some very ugly orthopedic sketchers and I feel like I’m walking on clouds.
[hpys7ta] (score 1, diepte 0) I wear Allbirds….slip resistance not great but goddamn are they the most comfortable shoes I’ve ever worn
[hpytxhx] (score 1, diepte 0) Doc Martens. They’re stylish, tough, awesome soles and ankle support. They’re around 100 bucks and last a long time. Yes they are heavy but if wore correctly they support me so much the weight doesnt bother me.
[hpyvp1f] (score 1, diepte 0) Look up SAS shoes (San Antonio Shoes). They have a store in Skokie, IL, (just outside Chicago).  I don’t think they have many locations in the country however they may sell their brand at other stores.  Most comfortable shoes I’ve ever owned. About $200 a pair, and worth every penny .
(32 reacties met lagere score weggelaten)

=== THREAD ryo66t ===
SUBREDDIT: r/retailhell
DATUM: 2022-01-08  SCORE: 120  REACTIES: 111
TITEL: WHY DO MY FEET HURT
POST (source_id=post):
this is my first job my shifts arent that long and im a teen my feet shouldn't be hurting at this age i feel like im gonna get foot cancer by 24 😭😭

&#x200B;

edit: clarifying some things, im a stocker and i dont have any breaks

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hrq0yan] (score 155, diepte 0) Retail is hard on the feet. Invest in a decent pair of shoes. They're a life saver. Shoes designed for nursing I've found to be the best. The difference they make is noticeable.
[hrq7w6b] (score 42, diepte 2) I had a pair of Hush Puppies that were the bomb. I think they're a worldwide brand?    They survived about four years, but they've stopped making that shoe and nothing in their current range is suitable.  I'm currently wearing Ascent, which is an Australian company. 

Basically make sure you get something that's fitted and with support. Also choose comfort over style everytime. My shoes are ugly as hell, but I don't cry when I get home :)

Generally a better shoe will come with a bigger price tag. I know not everyone has that option, but a bigger initial outlay will pay for itself. The pair that lasted four years cost around $200, so that was fairly decent. Most places clear our last seasons  designs, so you can sometimes get a decent pair for a decent price if you shop around online.

I've now written three paragraphs about shopping for comfortable shoes and I feel super old.
[hrq0p0a] (score 38, diepte 0) Wear supportive shoes.
[hrq0gvg] (score 28, diepte 0) You’ll get used to it. In a few years you’ll probably develop joint issues. Unless you stand on a padded mat all day, your body has a hard time with the physical requirements of retail.
[hrqalvg] (score 25, diepte 0) Do you stand all day as a cashier?

If so DO NOT LOCK YOUR KNEES. It makes your legs feel worse. I have tried it a month ago and whilst I struggle to remember to do it, my legs feel IMMENSELY better to the point that I can do stuff afterwards rather than immediately crash into bed.
[hrq2d5f] (score 24, diepte 0) Compression socks + good pair of shoes = unbeatable. If you have a blister problem, wearing two pairs of socks will prevent blisters. The friction goes between the two socks instead of ur foot and the shoe.
[hrq466p] (score 22, diepte 1) Could you perhaps suggest any particular brands, please? (I’m male by the way, if that makes any difference lol)
[hrq19y2] (score 18, diepte 0) Usually, as the others said, your shoes. Id reccomend getting non-slip skechers. They sell really good work shoes and are pretty comfortable. Even then, though, you'll still have sore feet. Just less so, to the point of tolerability
[hrqez8p] (score 16, diepte 1) I stood on padded mats for a good chunk of my retail time and those "padded" mats didn't do *anything* to stop the physical pain of standing upright at a register all day.
[hrq21st] (score 14, diepte 0) You need good shoes and a pair of Dr. Scholls insoles. Protect your feet while you’re young.
[hrqc4tj] (score 12, diepte 1) Heed this warning. Definitely don't lock your knees, you can actually pass out from doing this. Happens all the time to people who are unaware.
[hrqf1so] (score 11, diepte 0) Oh boy, I feel you. Keep in mind if you have foot issues or do long shifts at some point, your feet will always hurt to some degree. 

1. Good shoes. Make sure it allows for ankle mobility (can you comfortably roll your ankle to the side?) and it feels like you'd be fine if you were to start running in them. Running shoes are obviously pretty decent for this reason. Just make sure you get a shoe that is good for YOUR feet. 

2. Insoles! Most insoles that come with shoes suck ass. If you have flat feet, high arches, or any other issue I'd get a good pair of insoles. Or even if you have no issues tbh. Insoles wear out quick and it's best to replace them every few months (depending on how much use they get, obviously)

3. Circulation is important to prevent pain. Compression socks are your friend now. 

4. Move! Whenever you're able. Some positions like cashier won't let you walk around, but if you're stocking or something try not to stand still. It helps circulation. If you can't walk, periodically shift your weight and roll your ankle, clench and relax your foot, etc. Anything that helps get that blood flowing.

5. Have a supply of painkillers on you at least for the first month or so. Alternate ibuprofen and acetaminophen. Don't take it preemptively or else you won't know if you're building a tolerance to the pain (and you might not know if it's getting worse, either)

6. AFTERCARE. Take care of your feet!! When you get home, soak them in warm water, massage them a bit, and let them dry completely before even considering covering them again (I had really bad athletes foot from my feet sweating 8 hours a day- let the toes free whenever you can to prevent that). I wouldn't cut off calluses unless you're sure it's causing you pain. 


And... I think that's all I got. I'm sorry for your feet, my friend.
[hrq4rwl] (score 10, diepte 0) Get Danskos. They help so much.
[hrqgzee] (score 7, diepte 0) Like others have said better shoes will help. But as someone who has working in retail for 20 plus years I will tell you after 2-3 weeks you won't feel it much anymore. (Coming back after a multi month lockdown earlier this year reminded me of how brutal the first weeks are).

Standing in place all day is the worst in my experience. If you have the option to move around at work I recommend doing so. Keep yourself busy. It will help alleviate the stress you'd get standing in one spot all day.
[hrq8kbd] (score 6, diepte 4) I just got off six days straight. It's either mess around on reddit or go tackle my lawn in the unbearable humidity. Reddit is winning
[hrqoaeg] (score 5, diepte 2) Good shoes and regular breaks are a good step. Outside of work, working out regularly is also important. Stay flexible or you’ll suffer.
[hrrj7ne] (score 5, diepte 2) I swear by New Balance 990s. I have flat feet and they work wonders. Almost zero foot pain. They’re a little expensive $175-$200 but worth every penny. BTW there’s no such thing as foot cancer.
[hrqucqi] (score 4, diepte 3) If I may ask for advice. I have weird feet (very wide) I could theoretically wear a Size 8-8.5 lengthwise but usually go for 9 or 9.5 because even with Wide Width shoes I struggle with finding something. I work Wine Retail not a whole lot of walking but quite a hit of standing and depending on the day I do walk quite a bit while carrying stock. Also I'm quite heavy at 300lbs

My feet are fucking killing me and I've tried alot of different things. Sketchers, Memory Foam inlays, Shoes with Support (they were on the cheaper side though around 60-80$). 

Generally walking around at home Barefoot seems to work best for me. Never have any problems at home even when doing stuff but shortly after I  put shoes on its garbage...

Sorry for the longer post but I tried to be thorough and thanks in advance if you have any tips
[hrq2yhy] (score 4, diepte 0) Good shoes will save your feet! Take micro pauses as well - lift the toes of one foot for a second or two, then do the other. Then lift the heels. If you have a step or something, stretch your feet as much as possible. Make sure you sit on your breaks.
[hrq5xt6] (score 4, diepte 0) Hoka Bondi 7s - A little expensive but worth it! Very supportive and cushiony, my feet haven’t hurt in a long time.
[hrr1e2t] (score 4, diepte 0) First off, you HAVE to take breaks. Second, you need good shoes. I recommend 626 by New Balance.
[hrq835v] (score 3, diepte 3) Lol thanks you, I appreciate the thoroughness though. I’ve currently written two sentences, so I think that’s enough for now :)
[hrq9vse] (score 3, diepte 2) I worked for 3 years in footwear retail; are you looking for work shoes? I could make some recommendations based on what ya need them for!
[hrqmq1q] (score 3, diepte 2) I've worked retail in one version or another for over 20 years. I've found that having new balance sneakers and good socks make all the difference in the world.
[hrqmhpj] (score 3, diepte 1 OP) blisters??? that was never mentioned when i signed up 😥
[hrq9bqk] (score 3, diepte 0) New balance, been in retail 7 years best shoe I've found so far
[hrrg9l3] (score 3, diepte 1) Lock your knees never heard of that
[hrqbqjx] (score 3, diepte 0) Shoe/boot inserts are good as well like Dr. Scholl's. They're easier on the wallet than new shoes
[hrqdlrm] (score 3, diepte 0) Proper shoes. Inserts as well. I’ve always had problems with my feet even before retail. So much so I now have rx orthotics. New balance, Birkenstocks, Keen, income tax refund is going for a new pair of boots. I can’t stand what happened to my beloved docs so I’m getting either Gripfasts or Grinders. Grinders have the perfect boot for what I need but they haven’t been in stock in my size for awhile now.
[hrqe7fm] (score 3, diepte 0) hey, not sure if anyone else said this, but keeping your feet in the air/above your head (if you’re laying down) for like 15 minutes after your shift will help reduce the pain in your feet! learned that as a teen at my first job & it’s really helped me
[hrqskvq] (score 3, diepte 0) You know what's funny? I left retail for the public library field.

Nobody gives a crap whether I sit, stand, or squat doing my job.

It's almost like it doesn't matter in the slightest for performance, and retail workplace culture is just toxic capitalist bullshit.
[hrrr8jg] (score 2, diepte 4) Not who you asked, but do you have flat feet? My husband does and wears Merrell shoes.

https://www.merrell.com/US/en/barefoot-1/

He says these are the most comfortable shoes he has ever had. You can usually get coupons for them to help with the price. And they last at least a year.
[hrtultu] (score 2, diepte 4) I bought my pair when Adidas was doing an additional 50% off the outlet. They usually run a sale on their site. You can also find them on sale at Footlocker or Champs! I believe there is an additional 50% off outlet right now at Adidas. I'm in Canada, so they're a bit pricier here. Btw I'm in retail, and I'm climbing ladders and walking all day. These are now my favourite shoes!
[hrqmkcx] (score 2, diepte 1 OP) thank you, i dont wanna have cavemen toes🙂
[hrqr58j] (score 2, diepte 2) You can buy Dr Scholls shoes as well. They make a plain black shoe for those that need them for work.
[hrqg8e2] (score 2, diepte 1) New balance 928. Kind of pricey but worth it.
[hrsy8cs] (score 2, diepte 3) So the tip is not to lock your knees? I have no clue what that even is lol
[hrte9rp] (score 2, diepte 5) Ah thanks I tend to move about alot when work anyway, failing that I move my legs snout while on the spot.
[hrqnym8] (score 2, diepte 1 OP) thanks i'll try that out 😊
[hrqnuy6] (score 2, diepte 1 OP) thank you 😊
[hrqhiut] (score 2, diepte 0) Your feet and legs will hurt the first week or two regardless of the shoes you wear if you aren’t used to standing for hours a day, but it does go away. Investing in good shoes will help though.
[hrqjmab] (score 2, diepte 0) All of the advice above, but also embrace self-care after each shift. Run a hot bath with Epsom salts. Dr. Teal's has several different scents and they're great, but even generic unscented Epsom salt will help. Soak for 20-30 minutes at least. Take time for yourself when your body hurts. Rub/scrub your feet, lotion and elevate 'em for a bit after your bath. 

On that note, definitely keep up with your feet. You could get a pedicure at a salon, but I've always found it to be better to do it myself. It may not be as relaxing as having someone do it for you, but if you get decent nail/foot tools, you can soak your feet while listening to music and do a much better job. You'll learn quickly what your feet need and you'll save money. 

Retail/service industry is hard, but you can get through it and be better off by making sure to take care of yourself. I hope this helps and I wish you well. ❤️
[hrqow8f] (score 2, diepte 1 OP) thank you so much 😊
[hrqlsla] (score 2, diepte 0) I used to wear Doc Martens all the time until I had one too many foot injuries last year.  I had injured my left foot 3x before & last April was #4.  Accident at work resulted in a bad sprain in my plantar fascia so standing & walking became excruciating.  So after being out on worker's comp & back to wearing real shoes again, I found the Docs were no longer cutting it.

Skechers are GREAT.  I got some from the new ArchFit line & I love them.  In combination with Bombas socks (never knew how much of a difference good socks make until I got hold of these) & I have actually been pain free ever since.  And I am a full time retail employee, so that's saying something.
[hrqndto] (score 2, diepte 0) The first few months will be hell; invest in some nice shoes with good padding and traction, once calluses develop you won't feel as much discomfort.
[hrqo4cs] (score 2, diepte 0) Yeah, working sucks. You should try to figure out a way not to do it before your brain gets old and useless like mine.
[hrqqjib] (score 2, diepte 1 OP) amazing advice
[hrqrput] (score 2, diepte 0) My feet hurt when I was your age for almost a year, and then suddenly I couldn’t feel any pain anymore. I don’t know if that’s a bad thing, but it was so weird how sudden it was. Now I’m fine walking/standing forever. I guess it just took time to get used to.
[hrqt63r] (score 2, diepte 0) You may have flat feet and/or pronated ankles. Get a referral to a foot doctor to get custom orthotics.
[hrqt6jv] (score 2, diepte 0) I've been at my current job ~avg 35 hours a week for 10 months on solid concrete. I have one knee now that is giving me fits, particularly during this cold snap. I wear nursing shoes and they help alot, but I'm leaving retail asap because I don't want to be crippled before 40.
[hrs721h] (score 2, diepte 2) That seems... Odd? Maybe look up what the laws are where you live. I get a ten minute break in a four hour shift.
[hrr6ht0] (score 2, diepte 0) It’s all the shoes and socks you wear
[hrrcfsr] (score 2, diepte 0) Just give it a few weeks and you’ll get used to it.. a good pair of shoes and give your feet time to get stronger.
[hrrepwk] (score 2, diepte 0) Nursemates shoes are amazing for when you have to be on your feet all day.
[hrrra63] (score 2, diepte 0) Welcome to retail, my friend.

I’m nearly 25, did a couple years in hospitality and then it’s been part time retail mixed with full time school/college/uni since I was 17. Went full time at 22 when I graduated BOYYYYY do my feet hurt even more than I had imagined and already endured! 

As well as feet hurting, I worked in stores with a basement stockroom so the shins of my legs used to ache from running up and down stairs all day.

I always think it’ll get better some day, my feet will get stronger… but they don’t. Moved to a store with a store level stockroom and my leg aches have gone but feet pain still there. 

Corns, callouses, blisters are my worst enemy. Buy the COMFIEST SOFTEST SPONGIEST LIGHTEST work shoes you can. Comfortable socks also make a big difference. Cushioned insoles too! Exclusively fluffy socks and slippers when home to let those babies recover. 

For Xmas this year I received 2 x foot therapy gift sets, sliders that massage your feet and a wooden ball foot roller. It’s safe to say I complain about my feet A LOT. 

The Sanctuary Heel Balm is the BEST I have ever used in my life! Saved my feet on many occasions.
[hrrs92v] (score 2, diepte 0) I don't work there anymore because I wasn't getting good hours, but I stand by their products.  Stance Socks makes an athletic line that are built for your feet. They are both labeled as Right or Left because they are made to fit their respective feet. They also have a lifetime guarantee against holes and rips! Their socks have made a huge difference in making all of my shoes feel more comfortable. I highly recommend them.
[hrs4zqe] (score 2, diepte 0) I found that Skechers are good shoes for retail. They have the "working" shoe but I (51F) found the walking shoes with thicker soles to be very comfortable. You will have to replace about 6 months though.
[hrs805i] (score 2, diepte 0) What kind of shoes do you wear to work? That can make a huge difference. You need running shoes.
[hrsml50] (score 2, diepte 0) even if you can’t afford some nice pair of shoes, i’ve been using nike’s with some “work” insoles and they are great
[hryn6ms] (score 2, diepte 2) Ye don’t worry I had the same worries when I started, that it shouldn’t hurt because I’m young but your feet just aren’t used to being stood up for that long, it’ll get a lot easier. Not sure where you’re from but here in the UK I get my shoes from shoes4crews, they’re super comfy, pretty cheap and slip resistant
[hrsobso] (score 2, diepte 0) Get yourself a large bucket and epson salt. Soak your feet in hot water and epson salt for 15-20 mins after work. It’s a game changer
[hrviyp7] (score 2, diepte 0) I was on my feet so much at one job that I got a stress fracture (took forever to heal). It's not only about being on your feet, is about those hard ass concrete floors that are in basically every store, even if they're underneath linoleum or carpet. 

Wear insoles, and wear shoes that actually fit you. Shoes that are too small or too large will contribute to foot pain. 

When I was working on my feet, it wasn't only just about like the "innards" of my feet hurting (the muscles, etc.) but the skin on the bottoms of my feet would ache and be tender to the touch. In terms of dealing with that, Epsom salt baths really do work (also helps to relax any stiffness), but I've discovered CBD body cream/lotion will work VERY well for this, and it's much easier to do that daily than Epsom salt baths, albeit more expensive. It will not only help the skin not be tender, but it will help the muscles, too, PLUS it helps keep your feet soft and helps your heals not be so dry and crusty.
[hrrxd4t] (score 1, diepte 2) They definitely helped me. Felt boatloads better working at the first register that had this nice cushy mat compared to the days I worked on the backup register that didnt have the same amenities.
[hrqnfla] (score 1, diepte 1 OP) WHAT?? is there any way to counter that?? i dont wanna have bad joints
[hrqes5s] (score 1, diepte 3) I work in mobile retail which just means I’m on my feet half the time, so I could use something that cushions my feet and legs well, since they can get sore after a long day. But not much movement going on.
[hrsepzc] (score 1, diepte 5) I honestly dont know but I would assume so. I'll definitely check them out. Thank you very much
[hu8rbm1] (score 1, diepte 4) I'm really sorry for getting back so late on this, I totally forgot! My recommendation is Keen brand shoes. They go all the way up to 4E which is the widest size. They make great low hikers, saddles, and casual shoes with amazing support. Merrell is also a great brand but Keen is more of an outdoors brand that I find has more experience with designing comfortable shoes. I had a lot of opportunities to talk with the reps for the company when I was in retail
[hrqjmik] (score 1, diepte 2) Clive is what I got and it's a game changer. those shoes and toe socks
[j26yubo] (score 1, diepte 3) Lol not foot cancer , but plantar fasciitis is real . I'm a hairstylist and let me tell you it is painful
[hrtk2ce] (score 1, diepte 2) I swear by Adidas ultraboosts. You can generally find a sale, and they are so comfy! I can wear mine for 10+ hours on my feet and have zero pain when I get home.
[hrtmifm] (score 1, diepte 3) Thanks! Will check it out! (Btw did you buy yours online? Or where can I go to buy them at an affordable price?)
[hrutla0] (score 1, diepte 5) Nice! Thanks for the info! 👍🏼
(40 reacties met lagere score weggelaten)

=== THREAD 1anrn7r ===
SUBREDDIT: r/TalesFromYourServer
DATUM: 2024-02-10  SCORE: 66  REACTIES: 108
TITEL: My feet are always sore after serving a 6-8 hour shift :(
POST (source_id=post):
I’ve tried so many shoes from Hoaks to crocs to sketchers and I’ve tried putting inserts in my shoes. All these shoes kill my feet while I work, the soreness is mostly toward the outer part of my feet and on the soles of my feet. I do walk/stand around a lot. I just want to find good serving shoes! Please help

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kpua26b] (score 54, diepte 0) Not a server, but i run around a warehouse with concrete floors for 8 hours a day. Since I got my first pair of Brooks running shoes, my feet no longer kill me every day. Expensive shoes, but worth it imo.
[kpub18d] (score 50, diepte 0) Have you ever done custom or heat molded orthotics? Customs can be pricey, like $400 but heat molded imo are just as good usually around $40 and work great. Just put some in my snowboard boots today. Bonus is while molding them you get to walk around with a foot warmer.
[kpun43l] (score 27, diepte 0) Gotta do compression socks. It will make such a difference. And not copper fit. Real medical ones that are made for each foot, left or right. If they're good they should be a little difficult to get on but they save me when serving for hours.
[kpujvjf] (score 25, diepte 1) A podiatrist recommended Sore Dawgs inserts instead of going the orthotic route. He said they were just as effective.
[kpubceu] (score 22, diepte 0) Dansko’s saved my feet & legs. They’re a bit expensive but a worth while investment.
[kpuojje] (score 18, diepte 1) Also not a server, but I stand on my feet at a gas station all day. Also love Brooks! Game changers, the first shoes I ever bought that I didn't need inserts for to help plantar fasciitis
[kpubuio] (score 11, diepte 0) Came to say Brooks as well. Adrenaline GTS22 are great for long periods on my feet in a warehouse.
[kpuahqh] (score 10, diepte 0) Don't worry you'll get used to it, the first 20 yrs is tough though!
[kpumrbq] (score 10, diepte 2) We may be saying the same thing. The key is to get heat moldable ones. Inserts, orthotics, whatever, thick, and customizable that's the stuff I like.
[kpwzebn] (score 9, diepte 2) LPT which I wish I'd learned decades earlier: When using an add-on insole, remove the shoe manufacturer's standard issue insole before inserting the upgrade insole. This allows for a much more accurate, often less painful or painless size fit 🦶👌👍
[kpue9as] (score 8, diepte 0) Stretching your feet and legs before, during, and after your shift can help a lot.
[kpuq889] (score 8, diepte 1) I second this. Look for a 20-30 rating. And measure your calves so you can get ones that fit
[kpuxmiw] (score 8, diepte 1) Compression socks YES! Plus when you get home lay on the floor and put your butt against a wall and elevate your legs for 15min.
[kputvfz] (score 7, diepte 2) Thank you for this❤️ my foot has been killing me for weeks 😭
[kpuuayg] (score 7, diepte 1) Yes, and try to go to an actual running store. They will fit you so much better than anyone else can.
[kpuzwyv] (score 6, diepte 1) I am an ICU RN, Brooks and Nike Air Max are the only shoes I will wear. Even after 14 hour shifts my feet aren't sore, my brain is fried, but my feet are good.
[kpujxi0] (score 6, diepte 0) If you can afford it, I would see a podiatrist and get custom orthotics. They can cost a lot ($400-500), but they are so worth it. When I don't wear them for a single shift, my feet and legs are screaming. My podiatrist will do free revisions when they get worn. I've had the same pair for nearly 10 years. Absolutely worth every penny.
[kpukwsw] (score 6, diepte 0) New Balance and get some inserts made for your feet. They aren't cheap but Istg they're worth every red cent.
[kpuvqtf] (score 6, diepte 0) I like a wide toe box, like Altras. It gives more room for your toes to spread out and do their natural thing, helping your foot to function as a whole. I also do feet exercises like Katy Bowman recommends. It’s helped so much. There used to be days I couldn’t walk after getting home!
[kpugzi4] (score 5, diepte 0) Maybe try a wider shoe and add compression sleeves
[kpugztz] (score 5, diepte 0) I got the dr. Scholl’s insoles where you stand on the “foot mapping” thing. Changed my life. They’re like $60, but it was more than worth it in my experience.
[kpurjic] (score 5, diepte 0) If you’re behind a bar or a register or such, ask your boss for an anti-fatigue mat. It absorbs some of the shock so your feet and knees don’t have to.
[kpuwi9q] (score 5, diepte 0) Do you stretch before your shifts? That helps a lot. I’m almost 40 and fat AF and don’t get sore.
[kpvqham] (score 5, diepte 0) Have you tried going up a half size from your normal size shoe, or even the wide version of your size. It helped me because my feet tend to swell during my shift.
[kpw0ynb] (score 4, diepte 1) We’re usually required to wear nonslips in restaurants. Wet floors, grease and oil, random tomato on the floor. And if it isn’t required, it’s dumb not to wear them. You *will* slip at some point.
[kpunvfc] (score 4, diepte 0) I know this thread is about shoes, but do you eat right /stretch/stay hydrated? I've noticed more of a difference there than with shoes. (That said I wear Docs or Clark's with insoles and nice thick socks. We have to wear dressier shoes at my job)
[kpva42h] (score 4, diepte 0) Compression socks.  And don't wear the same pair of shoes 2 days in a row.  Shoes should rest a day to air out.  I rotate  Danske, sketchers & crocs.  As soon as the heel is worn I get a new pair.  My feet have to be taken care of.  I do 8 to 12 hour shifts on cement floors, often with no breaks.
[kputcwt] (score 3, diepte 1) Also not a server and I LOVE my Brooks!  My feet used to hurt so bad after a shift that I couldn’t sleep. I bought my first pair of Brooks 3 years and they are now the only shoe brand I wear to work.
[kpv7f5c] (score 3, diepte 1) They're not non-slip though - do you just wear normal runners?
[kpxftuo] (score 3, diepte 3) They’re definitely better than street shoes in a restaurant environment. And they’re not going to work on *everything.* Stepping on an ice cube or a big spill will probably cause you to slip. Flat treads don’t work as well. Cheap brands don’t work as well. Worn out shoes lose their slip-resistance. You also have to keep the treads free of debris. This is one of the reasons why you’ll sometimes see cooks hosing theirs off at the end of a shift.
[kpupi99] (score 3, diepte 3) That's what I was thinking. I thought having a brand name might be helpful.
[kpuu3su] (score 3, diepte 1) Do you happen to know if Dansko sells replacement insoles?
[kpuvjbi] (score 3, diepte 2) Sorry, I do not know.
[kpueaul] (score 3, diepte 0) I'm still looking for my own magic shoes. >sigh<  But I do love to come home and roll a frozen water bottle under my foot.  Helps so much!
[kpulm4q] (score 3, diepte 1) Until you find the magic shows get magic inserts! They saved me when I got pantar fasciitis.
[kpug80f] (score 3, diepte 0) Brooks are great! I love my pair but they could get kinda dirty in and around the kitchen..however its probably worth it if your feet are in pain.
[kpuq9dr] (score 3, diepte 0) I put orthotics in my Doc Martens and theyre comfy AF behind the bar
[kpuy32k] (score 3, diepte 0) I found out my feet hurt because I have “Morton’s neuroma”, essentially a thickening of nerves leading to my toes. They don’t hurt all the time, it’s just so random. You 100% need medium level compression socks. And I wear Hoka shoes at work. Elevate your feet against a wall when you get home. Keep Advil on you at all times while working.
[kpvcsxy] (score 3, diepte 0) Fitflop f-mode derby’s have been glorious. But 8 hours straight is too much for anyone. What happened to 5 hour shifts?
[kpvj2fr] (score 3, diepte 0) Whatever shoes you go with, get pedicures to keep your feet nice and nails properly trimmed. Over-trimming toenails can lead to a lot of problems with ingrown nails. Practice proper posture, especially when carrying things. (Learn what proper posture really is. You may be surprised.) Make sure your shoes are wide and long enough to allow for swelling on long shifts. And finally, make sure the shoes stay tight across the bridges of your feet, retying them as necessary if they’re laced. Having the proper fit can make a huge difference in how your feet feel.
[kpu9vw1] (score 2, diepte 0) I use Birkenstocks. Maybe that can help you.
[kpvpbtn] (score 2, diepte 4) Word. Red Wing, Danner, FP insoles. Lol
[kpuxgkj] (score 2, diepte 1) I spent a ton of money on orthotics and I hate wearing them. They make my feet hurt so bad!
[kpwtja8] (score 2, diepte 2) https://dansko.com/search?type=product&q=Insoles yes. I should be a sales rep for them these days considering how hard I love em. Legit changed my life after years of sore feet
[kpwt66a] (score 2, diepte 1) Danskos changed my life. Will never buy another brand of work shoes as long as I live.
[kpxm2iq] (score 2, diepte 1) Dansko’s destroyed my feet. Apparently they don’t make them in wide sizes, and I have Fred Flintstone feet.
[kpudv97] (score 2, diepte 0) Skechers and good compression socks!
[kpulfd2] (score 2, diepte 1) They said they tried Sketchers. Sketchers and New Balance are my two favorite, personally.
[kpue89m] (score 2, diepte 0) I used to use red wings and they made a world of difference + last forever
[kpunvkj] (score 2, diepte 0) compression socks have helped me a lot with that!! i also only wear my sketchers non-slip memory foam (the most important part) and with those two my feet are rarely sore
[kpuoyk3] (score 2, diepte 0) Adidas Ultraboost is the only shoe I can wear comfortably if I’m going to be on my feet for a long time.
[kpuq7qe] (score 2, diepte 0) Regular pedicures helped me a lot .
[kpuv37a] (score 2, diepte 0) Shoes for [crews](https://www.shoesforcrews.com/catalog/men-view-all)?
[kpuwuap] (score 2, diepte 0) I had pain in my feet after working shifts in a nursing home. Turned out I had Plantar fasciitus. I got some special insoles for my shoes, soaked my feet when I got home, and massaged the middle of my feet, and it eventually cleared up. Takes time though.
[kpvcc79] (score 2, diepte 0) Try buying construction worker style work boots. They are designed for all day standing and walking, with heavy loads.
[kpvjrsn] (score 2, diepte 0) I’m a server as well working anywhere from 5-8 hours a shift. I’ve realized it not the actual shoes but the soles in the shoe. I wear crocs and just added foot insoles inside and that has helped tremendously.
[kpy8o7d] (score 2, diepte 0) you're getting great shoe suggestions, but I'm going to add: sleep with your feet elevated above your knees. Use a pillow or a bunch of towels, but it helps immensely with being able to walk the next morning, it drains the swelling. 

also, tennis or golf balls are great for a diy-massage. just sit, roll foot on top of ball, stand to add more pressure, it feels amazing. 

combined with hydrating to avoid mid-sleep muscle cramps, I survived 12hr swing shifts on my feet for two years (then I got a better job). best of luck to you!
[krjwfv5] (score 2, diepte 0) Okay so this is really common for any job where you stand the whole time. There are a few painful conditions that can be caused by this, most commonly plantar fasciitis. I’ve had this since 2018 and have only found real relief in the last year. I’ve tried nearly everything. So here are some tips! 

First, if you can afford it/have insurance, get a referral to a podiatrist. They can diagnose your pain and help you treat it. I waited years too long. Do not wait if you can help it. In some cases they will give you a cortisone shot which gets rid of pain for months. The hope is that you take care of your feet and by the time the shot wears off, the pain is gone anyway. Unfortunately this didn’t work for me. 

Second, get good insoles for your shoes! I recommend getting a pair from PCSole on Amazon. Not crazy expensive, durable, and incredibly helpful. These things are life changing. I put them in every shoe I wear that has a removable insole.

Third, the best brands are Brooks, Hoka, and ASICS. Everyone’s feet are different, so what works for you may not work for me and so on. From what it sounds like, Hokas aren’t for you, so try ASICS or Brooks next. 

Fourth, buy a pair of Oofos sandals for home. You literally never want to go barefoot. So you need a good pair of sandals you can just slide into first thing in the morning, can wear in the shower, etc. Trust me!

Fifth, stay away from shoes with no arch support that you can’t put insoles in. So flats, heels, etc. In warmer weather try to stick to a shoe like Birkenstocks (or similar knock offs). 

Sixth, if you can afford it, buy an electric foot massager. Life changing. I’m obsessed.
[kpu92eo] (score 1, diepte 0) It goes away after a while
[kpv909q] (score 1, diepte 2) I do, we aren't require to weat non-slip shoes.
[kpvbi9u] (score 1, diepte 3) I ask out of pure curiosity - comfort>safety?
[kpx4098] (score 1, diepte 2) And Ive slipped several times in these so called nonslips. So what the point then
[kqb172d] (score 1, diepte 1) How often do you have to replace them?
[kqb56ye] (score 1, diepte 2) Since March of 2020, I've bought three pairs, so roughly every year. Not because they get less supportive or anything of that nature, just the mesh toe box ends up getting destroyed through the course of my job. Nails sticking out of pallets tend to catch my shoes, and I may or may not run over my toes with a pallet jack occasionally.
[kqbdxco] (score 1, diepte 3) Good to know. I've been happy with Asics cushiness, but feel like they wear out in less than a year. And I'm about at the point of needing to find next replacement.
[kqbf60l] (score 1, diepte 4) The last shoes I bought before the Brooks were Asics, and it was night and day as far as my foot pain. No more hobbling around after taking my shoes off after work cause my feet are killing me.
[kx2izkk] (score 1, diepte 1) I did that for 6 months and because of the drop in the heel to toe, my foot is now severely sore always in any shoe because my feet were used to walking at the angle drop of 10mm. Id suggest a lower drop shoe for all day work wear!
[kpyhstl] (score 1, diepte 3) Thank u! 🙏🙏🙏🙏
[kpw060a] (score 1, diepte 1) I could not wear Dansko's (too stiff for me), so the shoe store guy recommended Klogs. Super comfortable, popular with nurses. Love them.
[kpzy01a] (score 1, diepte 2) Oh no! I, too, have wide feet and I was really hoping to get Danskos for my next pair.
[kpzyzd8] (score 1, diepte 3) They fit except the mouth of the clog was too small. Again, it could have been my feet.
[kpy4dqu] (score 1, diepte 1) +1 for Danskos clogs. They take a minute to break in but wow they have saved my legs and back all these years.
[kpzxwjr] (score 1, diepte 1) Most girls at my restaurant wear Danskos! I really have to get a pair myself.
[kq2ydy7] (score 1, diepte 1) My mom used to work in a hospital and swore by them. She got me a pair when I was a barista and on my feet 45 hours a week and the difference was night and day compared to my old shoes
[kpufkzm] (score 1, diepte 0) I've been having the same problem lately. I actually started wearing my Merrill hikers to work, even though they aren't non slip. My feet actually feel great. Probably not the best advice.
[kpuinb8] (score 1, diepte 0) Hey dudes the Wendy’s are awesome and super comfy
[kpulbs4] (score 1, diepte 0) I love the sorel kinetic sneakers
[kpx6aog] (score 1, diepte 1) This plus water intake and stretching
[kpvi5xi] (score 1, diepte 1) This. Taking care of my feet makes such a huge difference.
[kpur4ni] (score 1, diepte 0) I absolutely love my New Balance Kaiha Road shoes. It's on shoes for crews! It's like walking on a cloud! Plus it's extra springy/cushiony.
(37 reacties met lagere score weggelaten)

