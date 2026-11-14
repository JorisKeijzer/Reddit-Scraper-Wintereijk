# Label-batch batch_0041

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
Schrijf het resultaat naar `batch_0041.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: c19c1u, 9a3y0x, 1oxf7vt).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD c19c1u ===
SUBREDDIT: r/Frugal
DATUM: 2019-06-16  SCORE: 603  REACTIES: 167
TITEL: Don't skimp on footwear
POST (source_id=post):
If you have a job that requires you to be on your feet a lot,  consider shoes with good support a necessity,  not a luxury.  As soon as you are able, buy a second pair. Rotating between 2 pair allows them to dry thoroughly and will extend the life. The long term medical benefits will be worth it,  too.
But remember,  expensive does not necessarily mean quality. Do a little research before you buy.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[erbxpy3] (score 228, diepte 0) Adidas Ultra Boost

Nike Air Prestos

ASICS Gel Lyte V

These are the most comfortable models I can find when it comes to being on your feet everyday. I walk anywhere from 15,000-20,000 steps a day.
[erbquun] (score 114, diepte 0) Good advice for anything between you and the ground: shoes, mattress, desk chair, and car tires. Quality is important.
[erc9uuw] (score 48, diepte 0) Terry Pratchett had a great bit on boots "The reason that the rich were so rich, Vimes reasoned, was because they managed to spend less money.

Take boots, for example. He earned thirty-eight dollars a month plus allowances. A really good pair of leather boots cost fifty dollars. But an affordable pair of boots, which were sort of OK for a season or two and then leaked like hell when the cardboard gave out, cost about ten dollars. Those were the kind of boots Vimes always bought, and wore until the soles were so thin that he could tell where he was in Ankh-Morpork on a foggy night by the feel of the cobbles.

But the thing was that good boots lasted for years and years. A man who could afford fifty dollars had a pair of boots that'd still be keeping his feet dry in ten years' time, while the poor man who could only afford cheap boots would have spent a hundred dollars on boots in the same time and would still have wet feet.

This was the Captain Samuel Vimes 'Boots' theory of socioeconomic unfairness.

Terry Pratchett, Men at Arms"
[erbye7r] (score 43, diepte 1) I was talking to a friend yesterday. I do ultraboosts when I can at work. I also have a pair of cole haan chelseas that are pretty comfy. He said he heard asics are real good too. I told him to give sketchers a try. Everyone at my barber shop rocks sketchers for that reason I assume.
[erbwwwb] (score 38, diepte 0) The same for socks.  It is amazing how good a pair of socks can feel.  I bought some Golden Toe “Fluffies” and they have been life changing!
[erc0iqc] (score 33, diepte 0) Don't cheap out on socks either. Every time I've bought cheap socks, I've had foot pain even if I'm wearing ergonomic shoes.
[erc38gz] (score 32, diepte 0) Bad feet?

NEW BALANCE 990S.

They may cost $140 and look kind of old-man-ish... But MY GOD if they didn't fix every single foot problem I had, almost immediately.
[erci345] (score 23, diepte 0) Having so much trouble finding women's dress shoes that are comfortable. I would throw everything I own out if I could find a good pair.
[erbz0sn] (score 22, diepte 1) Cosigning these words-of-wisdom. This rule goes double for ladders!
[ercchni] (score 20, diepte 2) Never co-sign; you’ll be liable for the payments if OP defaults!
[erc9orr] (score 18, diepte 2) I'd highly recommend Blundstone boots if you ever get tired of the Cole Haan pair!
[ercn7f8] (score 17, diepte 1) I once forgot my socks on the way to my job as a host and had to buy some from Macy’s since it was the only store on my way. They had Ralph Lauren socks on sale (still expensive, but cheapest I could find from there) and I’ve had these same socks for 5 years now and bought another pack because I love them so much. Seriously they make a huge difference and I had no idea until then.
[erbpzs0] (score 16, diepte 0) I sure agree! Great advice. Of course, I had to get sore feet, sore legs, sore hips, sore everything, before it sunk in.

As a sideline, I walk dogs for three hours or so each weekday afternoon. Some of that time is traveling from one dog to the next. Walk time is 3 to 5 half-hour dog walks. Anyone with a dog knows walking one is more like a saunter. They stop every few feet to sniff and whatnot.

But even with my gentle sideline, my shoes wear out in 4 to 6 months. They cost $100+, so I would put off getting a new pair: "Oh, I've got a few more weeks in these shoes.," NO!

Gradually end up with everything aching, feet to neck. Even headaches. 

I'm now totally convinced it's smart and a health necessity to get new shoes before the current pair stop providing adequate support. It's way more frugal. Saves me time because I don't require nearly as much recovery time. Saves money because I have the luxury of shopping sales.
[ercfs2m] (score 14, diepte 0) Dr. Martins leather shoes are my go to for my medical field job. I'm not a fan of the dansko clogs nearly everyone wears. My coworkers call them my "witchy boots" but they are so comfortable and the leather keeps me protected from spills.
[erc3sqs] (score 13, diepte 0) There are some things in life regarding which I am never frugal. Beds and footwear are on the top of that list.
[erclhww] (score 12, diepte 1) Anne Klein I-Flex is great! 10+ miles a day, and my feet are fine.
[erc6wn6] (score 11, diepte 1) Wigwam Ironman Thunder Pro socks are just the best. So breathable, quick drying! $12.50 a pair is ridiculous but worth it IMO.
[erbxgis] (score 11, diepte 0) Can I pitch in the call for good socks? Not only are they cushioning your feet and wick away sweat, but good compression socks can do a lot to stem the inevitable effects of gravity on your leg veins.
[erchexg] (score 11, diepte 1) I swear by my danskos but I think it is important they are sized appropriately for clogs. Many people end up with a size too small bc they are used to how tennis shoes fit. This ends up hurting the feet. If someone isn't willing to wear loose clogs, or if they don't like the style, get whatever works for you! Good choice with the leather btw! I hate seeing healthcare workers in fabric shoes.
[ercqm34] (score 11, diepte 1) I have arthritis, but am only 28, so I’m super picky about my shoes in terms of them having to be comfortable, but also stylish. Also I live in a super expensive cost of living area, so money in general is always tight. All that being said, I highly recommend checking out Ecco and Clark’s and investing in comfortable work footwear. 

Heels are tricky, but if you’re looking for comfy flats, those are my go to brand. I can’t really wear heels often anymore, but when I do, they’re Ecco booties. 

If you’re looking for work appropriate “sneakers,” I highly recommend Cole Haan zero grand, AllBirds, or [Ecco](https://us.ecco.com/women/soft-7/). Don’t let the price on Ecco or Cole Haan steer you away...they’re truly an investment. I’ve lived in my Cole Haan shoes for the last 4 years and they’re still in fantastic shape. They’re super lightweight and I wear them at work, traveling (they’re my go to traveling in Europe shoe), etc. The Eccos are my recent discovery after getting plantar fasciitis. I balked at the price, but once I tried them on, I was sold. The arch on these is better than my running shoes, they look sleek with a pair of cropped black pants, the leather interior means no sweaty feet, and for the first time in years I’m able to forget about my foot pain while at work. 

I wish I had invested in these shoes when I was in my early 20s vs. saying “wow these shoes are only $30...sold!” It would’ve saved me so much money in the long run in terms of podiatrist visits, physical therapy, lack of sleep and productivity due to pain, etc. Comfortable + cute shoes do exist and are 200% worth spending money on.
[erbryz2] (score 10, diepte 1 OP) The beauty of this sub is that it is filled with "common sense."
Sometimes things will appear that I had not exactly thought through before and sometimes it's something that reaffirms and helps me be more confident in my decisions. 
Btw, I didn't downvote you and won't.
[ercds0k] (score 10, diepte 2) Really?  It's one of the most tiresome cliches on this forum.

And, for what it's worth, I'm wearing 5 dollar shoes that I bought in January.  Still in good shape.  Shoes are ancient, ancient, beyond ancient, prehistoric, technology, and the brand names don't have a monopoly on it.
[erck5xi] (score 10, diepte 1 OP) Women's dress shoes are tricky.
My wife is in retail sales and dresses more casual. She likes some of the skechers for work. They don't have the running shoe look yet offer good support she says.  Good luck.
[erbwk8w] (score 9, diepte 0) Thanks thought I needed some new balance
[ercaylg] (score 9, diepte 1 OP) That's excellent! I don't remember ever having heard that before,  but it pefectly explains the struggle of the down trodden and less well to do.
[erco6yz] (score 8, diepte 1) Adidas pureboost is last year's model and is €50 cheaper than ultraboost. Slightly less comfortable, but a better purchase imo.
[erciju6] (score 8, diepte 2) You spend roughly a third of your life on it and as someone has stated, get a mattress protector. The place we just bought our bed from guarantees the warranty for ten years if we use it but at $1800 they better warranty it
[ercyvyp] (score 8, diepte 2) Bought Danskos a year ago. They are huge, heavy, ugly and expensive but I can go all day in those and at night when I take them off, I feel like I was never even on my feet. On casual fridays I still wear them with my jeans because they are just so damn comfortable.
[ercjydd] (score 8, diepte 0) How do you identify a quality pair of shoes versus overpriced branded crap? I don't mind the concept of spending a lot on quality, but really just don't know what to look for.
[erbr8ji] (score 7, diepte 2) On your feet all day, I bet. That's hard.

I did just a one-off gig that required standing in a limited area. Very tough.  I washed dishes for a family having a big party. Heck, I wash dishes at home every day. How difficult can it be?! 

What I hadn't factored in was standing and moving around--just a bit--in such a small area, mostly in front of the sink. No cushioning, just the regular kitchen floor. Next day my legs and hips were *sore!*

Doing that, standing on a hard floor day after day, must be really rough. Glad you got good footwear.
[ercxsob] (score 7, diepte 2) > I told him to give sketchers a try

Sketchers are overpriced, and made of very low quality materials. Not to mention they rip off many popular sneaker designs by big name brands like Adidas and Nike.
[ercb9i1] (score 7, diepte 2) If you treat it right, rotate it occasionally, and keep a mattress protector on it, a good bed can last many years.
[ercdpfb] (score 6, diepte 2) Yes, within a week and a half no more sore feet, ankles, knees, hips. Neck pain disappeared. A real eye-opener.
[ercanih] (score 6, diepte 3) thanks for the recommendation. I will def need another pair of shoes soon. I have one black and one brown pair shoes. I have a crappy pair of black oxfords that i need to replace and I would like a different pair of brown (darker shade) so I am looking around
[ercohe0] (score 6, diepte 2) You can find a lot of ultra boost on the GOAT app for under retail
[ercb3k1] (score 6, diepte 1 OP) I've been guilty in the bedding department.  It might be time for me to rethink that.
[erd490o] (score 6, diepte 0) Brooks running shoes are definitely worth a purchase. All of their models are supportive and good for the feet. Higher end Asics and New Balance are also good, but you have to research to find out what they are.

A good shoe will be fairly firm. You shouldn't be able to fold the shoe up like a taco, that means the shoe is too soft and is unstable. 

Good fit is just as important as buying a good shoe. Good shoes cause pain when they are not the right size. A shoe that fits well will make your feet the happiest, and increases the life of the shoes. There are a gazillion variables to fitting shoes, but these are the essential ideas:

- Size numbers are just guidelines. There is no absolute standard and your shoe size varies from brand to brand, and even varies within brands. This is the hardest thing for most people to get over. An 8 in one brand could correlate to a 9.5 in another.
- You should have a finger to thumbs width of space between your longest toe and the end of the shoe. It may seem excessive, but this reduces the risk of getting plantar fasciitis, black toe nails, hammertoes, and hallux valgus (which leads to bunions).
- Width is important as well. Your feet shouldn't be pressing against the sides of the shoes or wiggling from side to side. Many shoe brands make different widths.
- Heel sliding is actually okay. Shoes should not hold your heels in place.

I would also recommend an arch support. They do cost a lot however, and many people buy worthless junk (including "custom" hard plastic inserts) instead of quality inserts. I recommend the brands Sole, Kneed, and Cadence.

I work at a comfort shoe store with a medical professional, so I've seen everything a bad pair of shoes can do to your feet.
[erbqcls] (score 5, diepte 1 OP) I learned the hard way. too, working in a paper mill.
[erccoc2] (score 5, diepte 1) Did your problems go away after getting better shoes? I share some of these problems and it wouldn’t surprise me if it was down to my choice of footwear.
[erd20vf] (score 5, diepte 1) Agreed! Quality socks are wonderful!

I like wearing no show socks with my running shoes and Vans (Their Ultra cush shoes are so comfy!) I absolutely LOVE Smartwool’s no show socks. They’re actually no show, unlike so many others. They STAY IN PLACE! They don’t slip. I don’t have to adjust them. They’re comfy, and quick drying. 

I currently have 7 pairs. I found 4 pairs at Nordstrom Rack for $9.99 each, 2 pairs at REI on sale for $9.99 each, and one pair full price at Nordstrom for $13.95. They are so worth it! I got rid of all my other no show socks. The first two pairs I purchased are still holding strong over a year later. 

I’m so happy I decided to spend the $9.99 on my first pair. ❤️
[erdn5xn] (score 5, diepte 4) They're not exactly "low price". The Skechers store by my place sells their shoes for around $50-$100 CAD. For the same quality, you can buy shoes at Walmart for half that price. Skechers is just overpriced crap charging way more than what they're worth.
[erctq3w] (score 5, diepte 4) GOAT sells new and used. They work as a middleman where the seller ships to their authentication warehouse where they check for fakes. Then when they authenticate that they are real they ship them your way!
[erd1krs] (score 5, diepte 2) Good socks support your feet.
[ercyqxe] (score 5, diepte 1) I recommend Dansko - you might have to try on a few styles and sizes until you find one that works, but I rotate between Dansko clogs, Dansko sandals and sneakers now, and my feet have never been happier.  6pm sometimes has some good deals on them.
[ercjxyo] (score 5, diepte 0) If you're just standing or walking without much weight, consider minimalist shoes - I use a standing desk at work and love vivo shoes. They look good, and the minimal sole keeps your calves/core more engaged while still protecting your feet from glass/rocks
[ercxt3u] (score 5, diepte 0) I finally bit the bullet and got me a pair of birkenstock clogs. It took about a week for them to adjust to my feet (or the other way around), but now I can't imagine a more comfortable shoe. Kicked my plantars fasciitis to the curb.
[erbs38b] (score 4, diepte 0) As someone who does 20k steps a day for work, couldn't agree more
[erbyfxo] (score 4, diepte 1 OP) Well played :)
[ercsiba] (score 4, diepte 3) Im always scared to purchase second hand because i dont know if its fake. Any tips?
[erbyp6c] (score 4, diepte 0) Brands and models that are worth the money?
[erc9h5p] (score 4, diepte 0) Yes! I ended up with a stress fracture in my foot from teaching preschool without adequate arch support. Now I'm obsessive about taking good care of my feet.
[ercz6c3] (score 4, diepte 2) I have RA, and have problems with feet also. You should check out dansko brand. A lot of RNs wear the clogs, but they have so many styles. Also, besides having an outlet of their own i have found some at Dillard’s outlet and also at goodwill. They are seriously so comfortable I had a brand new pair of their waterproof ones that I wore walking around NYC and had no problem!!

https://www.dansko.com

https://outlet.dansko.com

https://www.shopgoodwill.com
[ercw5uy] (score 4, diepte 0) Insoles are your friend, too.
[erbtfb3] (score 3, diepte 3) You do get used to it to some extent. Its also not so bad if you're moving around even a little bit, and you kind of figure out how to shift your weight when you're not. My feet are still a bit sore at the end of each shift but it doesn't linger anymore at least
[ercyb7p] (score 3, diepte 5) I actually have insoles I wear. It helps but after 12 hours 🤷🏻‍♀️
[erbtigh] (score 3, diepte 0) 100 percent agree - I bought a highly rated pair of Merrell boots to use in our crazy Wisconsin winters and they've been worth every penny. I got a pretty good deal on them on Amazon but they also were recommended by several websites and ranked well on Amazon too. They've definitely allowed me to bike to work on days I might otherwise have driven because they keep my feet so warm, so I think they've paid for themselves a bit too.
[erc8y99] (score 3, diepte 2) I admit I walk a lot in them but don't stand a ton in them. In the winter I keep a pair of shoes for wearing around the office. I wear them with darn tough socks (which are also a fantastic "buy it once" item), but the combo gets awfully warm in a heated office (mostly in the afternoon when the sun peaks shines in my window). I don't know much about either of their shoes. Another thing is that I did have to break in the boots before they were super comfortable.
[ercbstb] (score 3, diepte 4) Allen Edmonds is a good option. Expensive upfront but lasts a long time if maintained.
[ercyk20] (score 3, diepte 3) I work on my feet all day in Blundstones, best purchase I’ve made
[erdklot] (score 3, diepte 2) Many skechers are very flexible which may not be great if your foot needs a bit more support. Great casual shoes, not great all day support shoes
[ercq5zp] (score 3, diepte 3) Search adidas official eBay store and they have cheaper adidas boost shoes. Also look on twitter for adidas fan accounts and you’ll find accounts that regularly update with discounts!
[erd0qqx] (score 3, diepte 3) Those are also not formal enough.

No sneakers
[ercy7zd] (score 3, diepte 1) Do you have a shoe recommend which doesn't have a tall platform or tall heel (thick bottom)?   I usually drive a manual car and big thick comfy shoes are a personal problem for driving.  If I have more flat feet is the solution custom insoles?
[ercaofs] (score 3, diepte 1 OP) The safety toed work boot I prefer is wolverine. About $150 on amazon.
New balance, Nike, Adidas, to name a few are better value than what you'll get with shoes that cost a third to half those brands at normal retail.
My local outlet has buy one get one half price on most of those brands. 
There are some trendy companies that look stylish but don't give my feet the support they need, so price alone doesn't mean good for me.
[erct8vs] (score 3, diepte 1) Sorry. The new models are $175 now.
[ercymk5] (score 3, diepte 1) I have bad feet and now only wear NB with copper fit balance insoles. Work, hiking, walking whatever, I'm in NB.
[ercumsp] (score 3, diepte 1) And safety gear if you ever need any.

A dollar saved isn't a dollar earned if your protective equipment fails when you need it most.
(100 reacties met lagere score weggelaten)

=== THREAD 9a3y0x ===
SUBREDDIT: r/Frugal
DATUM: 2018-08-25  SCORE: 724  REACTIES: 161
TITEL: What to Look for When Buying Good Shoes on the Cheap
POST (source_id=post):
I work at a podiatry clinic. Feet are so important, and a lot of people don’t take care of them as well as they should, which is a shame because so many foot and toenail issues are preventable. I also know that orthotics and orthopedic footwear can be prohibitively expensive, especially if you don’t have insurance. I started teaching patients what to look for when buying shoes themselves so that they can try to find deals at thrift stores or malls etc., and I thought I’d share here in case it might help other frugal people. I'm sorry if this isn't allowed here! 


The first thing you should do is **trace both feet on to a sheet of paper**-- this way, when you do go shopping for shoes, you have a quick little thing handy that you can just put the shoe on. If the shoe’s width or length doesn’t match the sketch, forget about it. Write down the measurements from your toe to heel and the width at the widest part for your own records. If you find that your feet swell because of edaema, of if one foot is significantly larger than the other (due to surgery, pregnancy, weight changes, etc.), consider making multiple sketches at different times of the day for a week to see if there are any drastic changes.  


If you can, try to **get yourself sized properly.** Just walk into any shoe store and have them measure you-- or, if your insurance covers visits to the podiatrist, get sized there if it’s affordable for you. FWIW, a lot of chiropodists/podiatrists might not charge you for sizing and treat it like a consultation, but YMMV and it's always worth calling a clinic to ask about that. Write all your sizing information (including the width and ball measurements) on your own sketch, and make sure you label what sizing system they measured you with (ex Drew Shoes sizing vs standard sizing etc.); also, keep in mind that a lot of different companies have their own specific sizing, and ask if your podiatrist has different measurement devices for different companies. If not, just visit multiple stores to be sized. Patients have done well with New Balance shoes in particular, so if you can find deals on those they’re worth it. Nikes and Reeboks aren’t the greatest, just because they’re more for the aesthetics rather than actual comfort and foot health. Also, it’s worth writing down your measurements in both men’s and women’s shoes, particularly if you prefer men’s shoes but have smaller feet, or like women’s shoes but have larger feet.


Once you’ve found a shoe that you like and that matches up to your sketch, you have to see whether or not it’s a good shoe. 

* Pick it up and **notice how heavy it is.** Generally speaking, you’ll want a shoe that’s light so that it’s not cumbersome to walk in. This doesn't mean that you should pick a Chuck Taylor over a proper set of shoes, just that if you think that a shoe will be too heavy for you to walk in comfortably, consider something else.
* **A good shoe cannot bend in the middle, but the front where your toes are needs to be flexible**; if a shoe can bend in the middle (imagine trying to fold it in half, bringing the toe box to the opening of the shoe), you need to put it down and ignore it forever. This is the most important thing to look for in a shoe so please be mindful.
* This isn’t necessary, but if you feel like you need more ankle support and can afford it, **see if the area around the opening of the shoe is rigid.** To do this, pick up the shoe from the back so that your fingers are around the area below the opening and the shoe is just horizontal as if it was on the floor, and pinch. If the shoe is rigid in that area on the sides and on the back of the opening, that’s pretty decent ankle support.


After you’ve done all that, **try the shoes on**, remembering that you shouldn’t be able to fit a finger behind, that you should be able to wiggle your toes without anything pinching anywhere, and that you must have enough room for the ball of your foot. Make sure you walk around in them a bit, and that you're not slipping out and that there's nothing that's scratching you or being ridiculous on the inside. You absolutely do not need to buy shoes that are two sizes bigger, and you shouldn’t rely on breaking the shoes in to make them fit. You need to find shoes that fit the first time you try them on, so that you don’t waste your money or hurt yourself. It's also important to check your sizing at least once a year, just in case it changes for whatever reason.


Also, it’s worth keeping in mind that **lace-up shoes are the most supportive, but if you need to use bungee cords or velcro straps for whatever reason, those are better than slip-ons** for most people. It’s also better to try on shoes towards the end of the day after you’ve been up and about for a bit, and make sure you wear the sock type you plan on wearing most often with those shoes. If you plan on eventually getting insoles, I usually recommend that patients take out the existing insoles so that they’re not being pushed out of their shoes, but otherwise just make sure the depth of the shoe is deep enough to accommodate two layers if you’re really insistent about it. 


Anyway, I hope this helps someone out on this sub. :)

EDIT: added bold text to make this easier to skim and fixed formatting.

EDIT 2: added information on feet changes due to pregnancy etc.

EDIT 3: adding that this info is for everyday footwear, not athletic shoes that you'll plan to run miles with or play tennis for hours in. Also adding clarification to my comment on shoe weights.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[e4so2a6] (score 138, diepte 0) Men, don’t ever buy glued dress shoes.
[e4spu58] (score 69, diepte 0) I'm pretty frugal, but I always find investing in good quality shoes has been worth every penny. I'll happily shop at a thrift shop for most things, but buy good shoes at retail or an outlet (Ecco outlet has been great). 

I find great, long lasting brands with good arch support well worth the money. I'll happily spend $80-140 on a pair of good shoes that will last over a year, often several years. 

Also, I have read that European sizing is standardized, so you're best off figuring out your European shoe size.

Excellent brands I like: Dansko, Ecco, Earth, FitFlops, and I just got some lovely ASICS running shoes and really like them so far. I read reviews and if reviewers mention the shoe has good arch support, I will check them out. That's usually a great sign.
[e4stg7a] (score 64, diepte 1) Yup, always look at the stitching around the soles too. A lot of cheap boots have fake stitching on the edge of the sole, look at the bottom and see that the stitching goes all the way through.
[e4sxacz] (score 46, diepte 1) Sahm = Stay at home mum
[e4sltcr] (score 40, diepte 0) Good to know! As a sahm I often don't wear shoes for days at a time, I often wonder if I should buy sneakers to wear at home, do you think its worth it or ia going barefoot ok?
[e4ss6j5] (score 39, diepte 0) You mentioned that the shoe shouldn't bend in the middle. What about shoes like the Zero shoe or other "barefoot shoes" that claim to provide really good support for hiking, etc. I ask because I've been wanting to buy the Zero Trail shoes for a while...
[e4szwz0] (score 34, diepte 1) Fantastic point. I remember having foot and knee pain when I was just a teenager. The podiatrist gets me custom inserts, fancy shoes, etc (all covered by insurance, but it was close to $1,000). No help at all.

Switched to zero-drop shoes for 100% of my running and 95% of my walking needs, and I haven't seen a problem in 10 years. Interesting...

But then again, how can you expect a salesperson (of orthotics, or fancy support shoes) to fairly consider an argument against their whole industry?
[e4t2xkv] (score 32, diepte 3) You are shopping at the wrong places if you thing Red Wing are the only choice for quality welted boots.

Check out /r/goodyearwelt for a LOT of brands.
[e4sul7k] (score 31, diepte 0) Purely anecdotal, but I'm relatively active and run quite a bit.  New Balance far and away has the best running/walking shoes on the market.  I've been primarily relying on them for over 15 years now, and while I do buy an occasional pair of Nike or Adidas running shoes, New Balance's fit better, feel more supportive, and last over twice as long either Nike or Adidas.  

I can't stress enough the lasting twice as long.  When my Nike or Adidas shoes wear out it's usually because of a body stitching rip/eyelet tear/sole separation that has rendered the shoe completely unusable.  When I get rid of a pair of New Balance shoes, there's a good bit of wear, maybe a small tear in the seams, but it's mostly just because I've had them for a while and they're looking pretty beat up.  I'm maybe worried about them not supporting my feet as well, but that's just speculation, because they still feel comfortable and nothing's falling the fuck off of them.

If you're looking for a pair of running shoes that are top quality, I'd say go for New Balance. If you're looking for budget quality, like for mowing lawns or for the occasional playground trip with your kids, I'd say go for Brooks.  That's what I've bought for my yard work shoes for roughly the same amount of time, and with occasional heavy use each pair has lasted 4-6 years.
[e4t0cof] (score 27, diepte 2) Can confirm, was the best man at a destination wedding in Florida,  Groom informs me morning of that the “Camel” color shoes were not part of the suit rental he had picked up for me.  I buy some $90 “Camel” color dress shoes from JC Penny’s put them on an hour before the ceremony and as I’m walking down the isle the trim around the base of the shoe comes off on both shoes!  It was 100 degrees plus, but still!  I successfully returned them for a full refund.
[e4snzjz] (score 23, diepte 1 OP) The podiatrist at my clinic regularly does this to clients as part of routine nail care. It's crucial to maintaining foot health, and patients are better for it. I will say, though, that pedicures at nail salons and the like won't be as good; they won't be able to do as much as a podiatrist would, and you don't know how clean the instruments or foot baths are. A lot of patients come in with infections that can easily be blamed on nail salons, so be careful. If you're diabetic, I would advise you stay away because you've to take extra care with injuries and cuts and all that, and it's best to work with someone who's aware of how to handle diabetic patients. If you *have* to go to a salon, try to book  the first appointment because it's when the tools are the cleanest, but if you can afford to go to a podiatrist/chiropodist who offers nail care to manage your callouses etc., I would look into it because it really is worth it.
[e4t11nf] (score 22, diepte 2) conventional, good quality, "supportive" shoes make my feet hurt like hell and being barefoot instantly relieves that pain. just reading OP's comments makes my arch hurt.

my husband had expensive orthotic inserts for years and all they did was collapse his arches even more.
[e4sv052] (score 21, diepte 1) Me too. Poor footwear contributes to knee pain, back pain etc. I just found Danskos this past weekend at Nordstrom rack for under $20.
[e4t04n5] (score 19, diepte 1) OP is addressing people with the sort of unhealthy heel-heavy walk caused by modern shoes with excessive padding, because the *vast* majority of people don't walk the way human feet evolved to. If you're used to walking with your weight on your toes, then some of the advice (avoid lightweight or over-flexible shoes, don't walk barefoot on hardwood) doesn't apply. However, if you haven't extensively worn barefoot shoes before, it's going to be difficult to adjust. Walking the way you're used to will quickly become painful.
[e4so6rh] (score 18, diepte 3 OP) As long as you're being mindful of cleanliness and know when to talk to a podiatrist, I think you'll be fine! :)

Oh, and more advice, try not to shave the day of your pedicure. It's easier for bacteria to work their way in the day you've shaved!
[e4t1b8y] (score 17, diepte 2) That's about 99%of all boots. To get a proper welted (?) boot, Red Wings at $300 is about your only choice.
[e4sx6ow] (score 16, diepte 3) I hope it's ok if I chime in here.

Wool is a genuinely comfortable material at most temperatures.  However since you say you're in Texas, you might look for a supportive sandal, something along the lines of Birkenstock.   I have had a lot of success in reducing foot and leg pain by wearing Sanita sandals, which have less arch support but more shock absorption than Birkenstock.
[e4snocd] (score 16, diepte 0) Curious - does having pedicures (particularly the removal/filing of dry skin and calluses) help foot health?
[e4syfy6] (score 15, diepte 2) Thank you!
[e4sslit] (score 13, diepte 2) Gosh, I don't know why but this is something that has never occurred to me. I'm also a stay at home/part time work from home mom and I have not thought (until now) that walking around barefoot on hardwood floors all day is probably a big contributor to my leg pain. I like those wool clogs, but I am in west Texas where I cannot really exaggerate how **hot** it gets. Are those shoes comfortable year round in hot climates or is there a sandal you recommend? Thanks :)
[e4t6vqp] (score 13, diepte 3) I don't know that I agree with you, but "the anti-vax of shoes" made me laugh so hard.
[e4t4nws] (score 13, diepte 2) I disagree. If you're walking incorrectly (heel-heavy), you are better off learning how to walk correctly, instead of trying to compensate for the walk with padded shoes etc.
[e4ssb2q] (score 12, diepte 1) I've learned this the hard way. So true
[e4t3uh9] (score 12, diepte 4) Yep. I’ll stand by Chippewas any day of the week. A super unsung hero of the GYW world. You can invariably grab a pair for around $150 new when they hit a holiday sale. 

As far as proper dress shoes, eBay is a treasure trove. So long as you’re okay with not being mint condition, you can pick up something very nice for under $50. In fact, you can even get quality Allen Edmonds for ~$25.
[e4so23t] (score 11, diepte 2) Thanks. I actually contacted a podiatrist here that said they don’t do that. I go to a clean salon. Thanks for not making me feel guilty about my treat :)
[e4sxcun] (score 11, diepte 1) This. Shoes are designed to protect your feet from the extremes of temperature and puncture. Flexible shoes allow the foot to function the way nature intended. One of the worst things you can do for your feet is to put them in stiff, highly supportive shoes.
[e4sl6sf] (score 10, diepte 0) Thanks, awesome advice.
[e4t5tb5] (score 10, diepte 1) Shoes, mattress, tires. Don't skimp on the things that connect you to the ground.
[e4t8wak] (score 10, diepte 2) I am a MD PhD in medicine, although I have no special training in podiatry or orthotics,  this comment makes the most sense to me.  Arch support? No mid foot flex? What garbage!  And don't walk barefoot at home? That's the only time during the day that my foot gets natural exercise for all its intrinsic muscles.
[e4t14mw] (score 10, diepte 1) I hate wearing shoes. Ever since I started buying my own shoes it's mostly been a line of lightweight, zero-drop shoes. I like being able to bend and flex my feet. If the activity calls for it I will wear heavier shoes;I have a good pair of hiking boots for all my hiking/working needs. 

The most important thing with zero-drop shoes is making sure you don't walk with a heel drop or slam your foot down when walking.
[e4t1z4o] (score 9, diepte 0) Can't bend in the middle?  All running shoes, ever?  You lost me there.
[e4t1lz4] (score 8, diepte 3) I recommend buying lightly used pairs on eBay! You have to go digging, but I found a size/manufacturer that fits me like a glove
[e4tbbtv] (score 8, diepte 3) Right. It's like saying, don't walk! Better use a wheelchair, it will support your body better!

What? No! Use your legs! Use your feet! That's what they're for - otherwise they will atrophy!
[e4t50l6] (score 8, diepte 3) We're not in disagreement at all. It's absolutely better to learn how to walk correctly. That doesn't mean it'll be easy or painless.
[e4t0o2c] (score 8, diepte 0) > A good shoe cannot bend in the middle, but the front where your toes are needs to be flexible

>see if the area around the opening of the shoe is rigid

I wear Nike RN Frees and you can not only bend them in the middle, they bend in all directions. The opening is not rigid at all with no supporting plastic, they fit more like a sock. They are still the best shoes I've ever owned. 

My Altras have zero drop so they bend from back to front. They are terrific shoes that I've worn for running marathons. I don't think the things you think are important for foot health are actually important factors when selecting shoes. 

In fact, when buying shoes for my daughter, I refuse to buy high support stiff soled shoes. Wearing stiff unyielding shoes makes for weak feet and poor running form.
[e4t0zfa] (score 7, diepte 4) I tend to walk on the balls of my feet and do not experience the impact from hard surfaces usually.
[e4t15ky] (score 7, diepte 1) Most likely because they have zero arch support.
[e4t4qj5] (score 6, diepte 4) Don't land with the heel, that's not how you're supposed to walk.. Land with with a mid or front of the foot, that's where the "springs" are :)
[e4tavc6] (score 6, diepte 2) When I was having foot pain caused by excessive walking in cheap shoes at my retail job, I went to a Good Feet store to see if they could help. The woman I spoke to there had me try on their hard plastic arch supports that you're supposed to wear all the time, even at home. They were incredibly uncomfortable for my feet but I figured she knew best, so I was considering buying them anyway. When I found out they cost upwards of $500 (and they're not even customized!) I ended up passing, but for a long time I thought I must need more arch support, even though the pain I had was primarily in my toes.

Ended up buying some $30 Skechers sneakers with high flexibility and no real arch support but good padding in the insoles, and never had that problem again. I realized that they were treating everyone as if they walked on their heels, while I put most of my weight on the toes/ball of my foot so their solution didn't work for me. And there still don't seem to be many real resources out there for people who walk this way.
[e4syteo] (score 6, diepte 1) Agree. My New Balance runners seem to last forever.
[e4suuus] (score 6, diepte 0) Thanks so much for this! I'm taking my elderly mother shoe shopping, and this was very helpful!
[e4t08eg] (score 6, diepte 0) I've grown to hate footwear personally.  I have narrow heels so it's very hard to find shoes that fit - I've had two pairs of shoes in my life that didn't give me blisters on my heels when I walk.  Getting custom made shoes is a bit out of my price range.

If you do happen to see this do you have any recommendations?  I end up wearing a lot of flip flops but that doesn't work year round living in Minnesota :(
[e4t1a66] (score 5, diepte 1) SAHM who is usually barefoot - if there's no issue with your feet I would recommend staying barefoot and letting your feet be free and unrestricted. it is better to focus on improving posture / natural gait to relieve any foot pain
[e4t85u9] (score 5, diepte 2) They can fake stitching on the top and bottom.

Don't trust your eyes on that one. You have to do research.
(115 reacties met lagere score weggelaten)

=== THREAD 1oxf7vt ===
SUBREDDIT: r/BuyItForLife
DATUM: 2025-11-15  SCORE: 1692  REACTIES: 151
TITEL: Employer Pays For Shoes & Socks, I Will Never Need To Buy Socks Again In My Life.
POST (source_id=post):
Every year we get a subsidy for 110 bucks off shoes and accessories, insoles and socks. I've already got 3 pairs of perfectly good shoes, so I've been stocking up on socks. Darn Tough are offered, so it was a no brainer. I get 4-5 pairs every time. Haven't even gone through the last set.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nowty1p] (score 814, diepte 0) Having so many pairs of identical socks was such a game changer for me. Your mornings are about to start going about 10% smoother every day. Such a good brand, too!
[nowug08] (score 198, diepte 1) Are you my husband? Identical socks and underwear. Two less thinks to think about every day.
[nowuwr8] (score 186, diepte 2) Once you start to go "cartoon character closet" mode you can't go back. I have 6 identical black T-shirts hanging in my closet and if I get that in every color I could be done buying shirts for years
[nowtz9w] (score 139, diepte 0) Free socks might be the coolest job perk I've ever heard
[nowtmew] (score 123, diepte 0) What line of work if you don’t mind my asking
[nowttgs] (score 117, diepte 1 OP) Warehouse/delivery.
[nowvzkh] (score 88, diepte 3 OP) About 7 identical Carhartt K87 black tees hanging in my closet. Cartoon character wardrobe is freeing.
[nowwcxo] (score 78, diepte 3 OP) They do dabble in socks. 😅


Nah, Amazon. They own zappos, so we get a subsidy through them. 


The socks are a silver lining to the rest of the gig.
[nowu5wv] (score 45, diepte 1 OP) It definitely makes the gig more palatable 😅.
I have noticed less foot pain since I've switched over which I was surprised by.
[nowv6fn] (score 43, diepte 2) For a socks company?
[nowu33p] (score 39, diepte 0) Dude I have these exact socks, they’re beauties. Be careful when washing because they’ll go from pristine white to gray fast af and lose all that contrasted beauty.
[nowuryx] (score 33, diepte 0) Unrelated: I met the owner of Darn Tough at my work and she is a pip! Literally one of the most interesting and kindest ladies I’ve met.
[nowvtkh] (score 25, diepte 2) I checked your post history and no, you are not my wife, despite the fact that your husband would 100% make a joke like this.
[nowxk2q] (score 20, diepte 1) I have two colors of socks—gray and dark brown. After washing them, I toss them all into a bin. In the morning, when I’m trying not to wake my wife by turning on the lights, even in the dark and before coffee, I know that if I grab three socks, I’ll have at least one matching pair.
[nowvhcj] (score 19, diepte 2) Decision fatigue is a real thing.
[noww0yw] (score 18, diepte 3) Ah, yes - I know the multiples of the same black (and white) shirt. And of course the same pants and same sweater in multiple colors. It’s really hard to argue with the logic.
[nox8vzx] (score 17, diepte 4) Yep. Carhartt Force tshirts, Old Navy tech chino pants, Duluth everything else. Black or dark gray everything, I’m basically Batman.
[nowv3cz] (score 16, diepte 2) I'd probably give them a soak in OxyClean every now and again if they start looking dingy.
[noxgot9] (score 13, diepte 4) been shopping w zappos for over 20+ years & they have the best customer service i’ve ever encountered. And not with some weird ℒℐ𝒱ℐ𝒩𝒢 𝒪𝒰ℛ 𝒞𝒪ℛℰ 𝒱𝒜ℒ𝒰ℰ𝒮 ⁣kool-aid energy.  More like an “oh bummer, lemme see what i can do” vibe. 

don’t know if it’s from overall company culture, hiring great people, or what. if their office was in my neighborhood, i’d bring over some cookies at Christmas.
[nowuwci] (score 13, diepte 2 OP) Now I just need to find underwear 😅, then my mornings would be seamless.
[nowucwz] (score 13, diepte 1 OP) Yeah I've noticed a bit of that with the first batch. Would you recommend washing them separately in their own load?
[nox1afs] (score 11, diepte 2 OP) Who needs a pension when you can have 20 dollar socks for free?!
[nowvacn] (score 11, diepte 1 OP) Always good to hear positive vibes and stories about business owners these days, makes me more comfortable with the purchase and support of the company. What line of work has you meeting the owner, if I may ask?
[nowyckw] (score 9, diepte 2) Wait you throw individual loose single socks in a bin?! I have never seen this or heard of such a thing.
[nox65r9] (score 9, diepte 2) ah, so you're the person from my statistics class word problems.
[nowujsw] (score 9, diepte 1) They are darn tough. The best brand ever.
[nowwvg2] (score 9, diepte 2) Check out r/laundry, they've got all the best tips for stuff like this.
[nowugt1] (score 9, diepte 0) I did that for myself. All my socks are DT.
[nowy55o] (score 7, diepte 3) Nice pun. (You could buy seamless underwear.)
[nox0ply] (score 7, diepte 2) Irrc some executive said sth like i typically make 2 good decisions a day. I dont want to waste it on picking out my clothes.
[nowyw0c] (score 7, diepte 1) My paid retirement plan looks stupid now!
[nowuq94] (score 6, diepte 3 OP) More so the identical socks than specifically the crew socks, sorry if that was poorly worded.


It allows me to just pair the worn out and ripped ones together, so I don't need to send in a otherwise perfectly good sock for the pair.
[nox4p1h] (score 6, diepte 3) I have an entire large drawer full of Costco white tshirts from multiple multi-packs. They're a nice heavy material and very cheap at the same time, so I'm quite happy to wear them doing almost anything. Day to day kicking around tshirts, DIY tshirts, undershirts, whatever. Wish they did them in different colours tbh because a white tshirt is like my uniform at this point.
[nox5swu] (score 6, diepte 4) It sounds like a game ruiner to me lol. As I’m folding my laundry, whenever I find a sock I just throw it on a pile of clean socks and then when I’m done putting all the other laundry away, I pair up the socks and fold them into each other so each pair is stored together. I feel like loose socks in a bin would throw me off when I’m getting ready.
[nowvnh1] (score 5, diepte 3) 😂😂
[nowykpv] (score 5, diepte 4 OP) I'm glad someone actually recognized the pun :3
[noww5rq] (score 5, diepte 3) He’s converted me (just to a much lesser extent)
[nox40kc] (score 5, diepte 3) It’s a game changer
[nowz9sa] (score 5, diepte 1) All my socks are the same so they pair easily. In a family of 4. I hate laundry.  Its one less person to worry about.
[noxhoww] (score 5, diepte 2) Darn Tough socks are the real deal. I see you have one good choice, but if they’re offered, go for some of the padded merino wool hiking socks and merino wool crew socks. They are superior to anything else I’ve ever put on my feet, and they adapt to heat really well. I spent the last 20 years in Texas, much of it outside, and I wouldn’t wear anything else.
[nowvkmb] (score 5, diepte 2) Oh for sure! I already love the socks and love them even more now. She has a summer home in the town I live in and first time I met her we chitchatted for over a hour!

I’m in retail.
[nox0jg7] (score 5, diepte 0) For anyone with wide feet that wants Darn Tough socks, they have a sister company called Wide Open. They are amazing just like Darn Tough, but made for people with wide feet/calves.
[noxmjoi] (score 4, diepte 5 OP) Zappos was very well known for having an amazing company culture back in the day, don't know how much has changed since Amazon purchased them though.
[noww2si] (score 4, diepte 3 OP) I'd wager same as socks. Once you find what works, why switch up?
[noxx09l] (score 4, diepte 5) Carhartt Force t-shirts are fantastic.
[nox118j] (score 4, diepte 3 OP) Save think for important think need.
[nowy8uj] (score 4, diepte 1) Same. I’ve added to my collection over the years. Little treats for myself or as “souvenirs” from travel.
[noxpv8d] (score 4, diepte 0) And they have a lifetime warranty so these socks will still be in your life once you've retired! Then you'll get to tell stories about how you got those socks at your old job and you just got a new pair since the old ones wore out.
[nowu0nx] (score 3, diepte 1 OP) Yeah I always get the crews, super comfy and utilitarian, and it makes warranties much easier.
[noxlnko] (score 3, diepte 4) Rit dye might be your friend
[nowxgbq] (score 3, diepte 2) Why think more if can think less.
[noxfqf3] (score 3, diepte 2) Pigeonhole principle in action!
[noxol8l] (score 3, diepte 4) I don’t know I’d wear any merino wool except Darn Tough at this point. Everything else has let me down.
[nox78hi] (score 3, diepte 1) I discovered the military discount for DT through GovX and it is a game changer.

You have to buy a minimum of 2 of the same pair at a time, but the discount is worth it.
[nox0xqe] (score 3, diepte 2) Darn Tough makes sock for wide feet called Wide Open! Just in case you need a wider size when you eventually wear holes in these (which will take years).  You can send in your warranty socks, then when you get the email you can chat with a representative and have it switched to Wide Open.
[noxkuti] (score 3, diepte 0) Jurassic Park’s Ian Malcom when he’s asked if he ever gets bored with his grey/black wardrobe.

“Not at all. I find it liberating. I believe my life has value, and I don't want to waste it thinking about clothing," Malcolm said. "I don't want to think about what I will wear in the mornin”

I don’t recall if he did the math in the book, but it adds up
[noxmyyv] (score 3, diepte 0) One question, why white? 

Maybe it is just me, I seem to be a magnet for dirt, and white socks are such a pain to keep looking good.
[noxo783] (score 3, diepte 1 OP) Honestly? I really wanted black, but they only offer white crew socks (through the subsidy), only black pair are quarter ankle which I don't like. However, the whites really grown on me, and they keep their color well enough, especially up near the colored bands, so they never look dirty. 


I also don't generally wear them around the house (I had just gotten home, and the heat hadn't kicked in yet), so they see the inside of my shoe, and then the hardwood for a few seconds before getting thrown in the wash.
[nowth3p] (score 2, diepte 0) Envy
[nowwk9a] (score 2, diepte 4) Oh, smart! I'm glad I asked — I hadn't thought of that.
[nox1qcl] (score 2, diepte 5) > Are guys really matching their underwear to their outfits

no.  or at least I've never considered it.

I have six of the same pair, myself.
[noxlafu] (score 2, diepte 3) People always tell me I'm like a Lego character
[nowwrzp] (score 2, diepte 1) 10%? Try 12%!
[nox6q5d] (score 2, diepte 4) But if you matched them you wouldn’t have to grab 3 at a time lol. Idk maybe I should try it and find out if loose socks is actually the superior method. I do use a boxer bin and I don’t really fold them I just kinda put the good ones on top so I can reach in and grab a pair without thinking. Highly recommend.
[nowzbz5] (score 2, diepte 1) This! About a year ago I threw out every sock I owned that wasn't my favorite brand and style. I only buy those now and it's so much easier. No more matching and no more missing pairs. If I lose one I just have an uneven number of identical socks until I lose another one.
[noxmtl3] (score 2, diepte 3 OP) There was a couple merino wool options actually, from Feetures. Wasn't super sure about the brand but I may try em out next time.
[noxa8im] (score 2, diepte 2) Wash them on cold (ideally delicate) and air dry them
[nox391q] (score 2, diepte 2) For a few years I gave myself a pair for birthday and Christmas:
[nowwacg] (score 2, diepte 0) Now you just gotta get all the other jobs with lifetime set ups and you’re good
[noxn9ez] (score 2, diepte 3 OP) I mean that's why it's tagged with the "Still sold" tag. This sub as I understand it isn't about strictly old stuff, it's about finding & sharing stuff that is BiFL. 


Darn Tough is just one such brand that people have good luck with, which is probably why you see it so often.
[nox1g8a] (score 2, diepte 3 OP) Oh good to know! I'll def try that out on the future.
[noxhih2] (score 2, diepte 1) if you’re on your company’s health insurance plan, see if it offers rewards for physical/wellness activities. My plan with United Health Care does cash rewards for things like step count tracking, or scheduling a yearly physical, etc.
[nox0m5v] (score 2, diepte 0) These the spongebob socks bro
[noxj0vn] (score 2, diepte 1) This was a perk of working for an athletics department at a university. We got paid very little but they covered clothes for us and required us to wear them. I still had some of them a decade later.
[noxohbf] (score 2, diepte 2) Ah I see, that explains it.

It is a pain the subsidy system limits the goods you can purchase. 

At least they offer a good brand. I know several people who swear they last and last.
[noxpdql] (score 2, diepte 1 OP) Yeah I shortly worked for Columbia and they were the same. Decent discounts though, but no free stuff.
[noxq0gb] (score 2, diepte 1 OP) Oh man I look forward to that 😊
[nowtr53] (score 1, diepte 0) Nice choice. Especially to get all the same kind — just smart.
[nowvjkm] (score 1, diepte 3) Same reason as socks… even with only two variations, you likely have one you prefer… even with two colors of the same cut/style/brand, you will likely make the decision to match your outfit or not wear the same color as the previous day.
[nowvwhw] (score 1, diepte 4) I just ended up getting a bunch of the dang soft line from Duluth in a bunch of different colors. I’ve found I don’t tend to grab a specific color more often, but I hardly ever wear any of the other pairs I have at this point.
(74 reacties met lagere score weggelaten)

