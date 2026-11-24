# Label-batch batch_0132

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
Schrijf het resultaat naar `batch_0132.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1uqrfuq, xr9gkx, 17785w6).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1uqrfuq ===
SUBREDDIT: r/BuyItForLife
DATUM: 2026-07-08  SCORE: 92  REACTIES: 66
TITEL: Women’s Shoes with Wide Toebox but Narrow Heel
POST (source_id=post):
Went to the doctor for ongoing issues I’m having with my feet and was told a big part of my problem is my foot shape and the shoes I’m wearing. I wear a 7 1/2, my width at the toes is pretty large relative to my length, yet they are significantly more narrow at my heels. Struggling to figure out shoes/brands that are good for this issue that still look cute (I’m 20 so would prefer to avoid shoes with an old lady vibe if at all possible, though I’ll make the sacrifice if it prevents pain 😭)

TLDR: Need shoes with wide toebox/narrow heel that are still cute/stylish for someone early 20s

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[owadare] (score 68, diepte 0) Altra shoes would be good. Designed with a wide toe box but normal heel. I also find ON cloud shoes to be comfortable though they don’t advertise themselves as wide toe box shoes. I also wear a 7 1/2 and their cloudhorizon trail shoes are my current favorite walking shoe.
[owa2nk5] (score 47, diepte 0) I don’t know what you’re style vibe is but my feet are what I call pizza slice shaped, tiny heel wide toe, and I have found duckfeet shoes to be very accommodating to my foot shape. They are handmade leather shoes. My winter boots are by them are they are at least 8 years old now. Despite them being dirty, they are in great shape. They make sandals and Mary Janes, and other style shoes too. Duckfeet.com is where you can find them.
[owaxwvi] (score 17, diepte 1) Also give Topo Athletic a try! Same toe box. Normal sneaker heel to toe drop.
[owa46zz] (score 15, diepte 0) And it might be as simple as adding a heel pad. People used to customize shoes a lot more but you can still find pads that stick to the inside of the shoe designed for the back of the shoe where it would gap open and for the bottom inside heel where you might need a little more padding at the bottom of your heel near the sole.
[owa8igs] (score 14, diepte 0) Same.

I wear Born and Alegria shoes, but I am an old lady.

I find styles that hold the shoe in place can help me. Mary Janes, ankle straps, Oxford-style lace up shoes keep my foot where it needs to be in the shoe instead of the back of my foot sliding around.

Good luck.
[owafjlv] (score 14, diepte 0) Birkenstock shoes and boots (not the sandals) have an ample toe box and are exceedingly comfortable. 

If the heel is loose you could just use one of those heel inserts. I’ve got narrow heels too and I love my Birkenstock boots and shoes.
[owastkz] (score 13, diepte 0) I have pizza feet and I switched to barefoot shoes a few years ago. [Anya's Reviews ](https://anyasreviews.com/)has lot of cute options and reviews. I wear Barebarics zings as my standard fashion sneaker, [Harlem Shoes](https://harlemshoes.com/category/women) or Naturalizers for heels, Lems for tennis shoes, Shapen sandals/flats - there's a lot of options out there.
[owa2vt8] (score 11, diepte 0) Look into Vivobarefoot or Lems. Both do wide toebox designs without looking like orthopedic shoes. Vivo especially has some styles that pass as normal sneakers. For the narrow heel issue you might need to add a heel grip pad since most wide toebox brands run wide all around.
[owa6g8w] (score 10, diepte 0) Barking Dog blog reviews all sorts of comfort and orthotic shoes for women - they are a great resource! Not necessarily BIFL but definitely focus on comfort and function (still with an eye to attractiveness too!)

https://www.barkingdogshoes.com
[owah86f] (score 8, diepte 1) I second Altras!
[owc5ni6] (score 8, diepte 0) As a narrow heeled person I have found that heel pads do not work nearly as well as tongue pads. Heel pads force your feet forward in the shoe, whereas tongue pads--- well I don’t know exactly how they work, but they don’t do that!
[owant3d] (score 7, diepte 2) Third for Altra. I have bunions that make my normally narrow feet, wide at the footpad. Altras fit just fine no tightness at the top and no sliding at the heel.
[owajcvi] (score 6, diepte 1) I wear exclusively Lems now and love them. They've added a lot more styles over the recent years. They all have wide toe boxes, but some are wider than others. Some have a more fitting heel too, so if you have a dealer in your area go and try some on first.
[owa2spq] (score 5, diepte 0) Sounds like you got hobbit feet, no offense. My ex had same problem and found some barefoot style shoes that worked, the toe box is wide like a duck foot but the heel cup actually holds. Look for brands that do anatomical foot shape, not just "wide" sizes cause those are just wider everywhere. Not much help on the cute part but black leather ones can look decent with slim pants
[owb7stb] (score 5, diepte 1) Opened this thread to recommend altras.
[owbavde] (score 5, diepte 1) I'm going to try Altras. I bought a pair of Topos that also have s nice wide toe box but have trashed them in 2 months. Could be a fluke but they weren't cheap
[owar9dw] (score 5, diepte 0) You might not have wide toes, just natural human feet that haven't been mutilated by fashionable shoes.  Barefoot shoes are the easiest way to search for shoes that are foot-shaped, but many brands don't have much cushion.  

Are you looking for running shoes or dress shoes?  I found some great ballet flats that have a human-foot-shape on Etsy.  https://www.etsy.com/listing/1771035575/white-leather-barefoot-ballerinas
[owatdze] (score 5, diepte 0) No idea about stylish and cute, but Ryka shoes are designed for women with that specific last--wide toe box and narrow heel. They are the best fitting shoes I've found.
[owdiynl] (score 4, diepte 1) I have the same foot shape that OP describes and wear 3 pairs of Duckfeet in rotation and they’re perfect.
[owavone] (score 4, diepte 1) Second ON for good pizza slice feet
[owao9ua] (score 4, diepte 0) Saucony uses lasts with a wide toe box and narrow heel and makes a lot of various casual and athletic styles.  Prada also uses similar lasts for many of their styles (sorry they’re pricey but there’s a good used market for them).
[owb703l] (score 4, diepte 0) Altra and Topo shoes have a wide toe box. I have narrow heels and haven’t had too much problems with either brand, though I normally lock my heel in with a runner’s loop.
[owa2qqm] (score 3, diepte 0) I have similar feet and I really like Born shoes.
[owanysh] (score 3, diepte 0) The only brand of what I call dress shoes that have fit like that I have ever found (I have A heel and EE toe) is Naturalizer, as far as style goes YMMV.
[owe1e8d] (score 2, diepte 2) Which Topo style. Surprised because that’s never happened to me.
[owd999i] (score 2, diepte 1) They’re not BIFL though. Altras wear out extremely fast. They’re so comfortable and accommodate my toe box, but you hardly get any mileage out of them. They’re not cheap, either.
[owanyrb] (score 2, diepte 0) Thanks for posting this and to everyone for commenting. I always wore heals with an ankle strap as any other shoe comes off my heel.  I will look at these brands
[owaotrh] (score 2, diepte 0) I’ve had good luck with bzees and some styles of Skechers. Everything else just slips off my heels. Bzees seem to fit my foot shape though, somehow
[owfmt41] (score 2, diepte 1) I have duck feet, too, and discovered Bzees a few years back. Now I buy ONLY Bzees and Ariat. The Ariats need to be 1/2 size larger, or wide. You can wash the Bzees!!
[owav0qx] (score 2, diepte 0) Naturalizer are ok with style. They'll get you through your corporate work day. 

Hokas are my choice for an athletic shoe. Good wear and comes in a ton of colors.

I just bought a couple pairs of birkenstock sandals (gizeh flowers) and they've been fine for the office (we are way more casual in summer) and I get a ton of compliments on them.
[owaxjja] (score 2, diepte 0) If you are looking for sneakers, I love Topo Athletic. They have a very side toebox and is super comfortable. They are a smaller company so less known to people. 

Altras have zero drop where as Topos have normal drop.
[owb6rl8] (score 2, diepte 0) I have the same problem and I find Bared to be great! They are expensive but actually cute. Margaux has a style of ballet flat that tightens so you can get the wide width but still tighten it enough it doesn’t slide off your heel.
[owb8o8c] (score 2, diepte 0) I have flipper feet as well and keens gave worked for me
[owe1ex5] (score 2, diepte 0) Rykä!! I love them and have sales fairly often
[owab3fq] (score 1, diepte 0) If you're into hiking/trail runners and active looks, I find keens to have really wide toe boxes by default and they also make wide sizes. 


I'm about to hit 30 and I really don't wear anything that doesn't lace if I need to be walking or moving a lot. There's a lot of different lacing patterns where you can adjust the width and tension through the foot by threading the laces in different ways, and I need that adjustability to be comfortable.
[owac7mx] (score 1, diepte 0) Not BIFL, but if this is a real health need, get Athletic shoes from Altra and check out dress-ish shoes from Baer, Birkenstock, and Keen.
[owg75zz] (score 1, diepte 3) Ultraadventure. The back started wearing down after a month and a half. Got more worn down and some on the outside when traveling. Granted i was walking 10+ miles a day for a week. But I've never had shoes break down like this, not even when i used to walk marathons. 
Could just be this style of course
[owket4c] (score 1, diepte 1) Second this, but I love the sandals we well as the shoes/boots. Also love their more stylish line, Papillio (spelling?)
[owcvjdk] (score 1, diepte 1) seconding naturalizer! their shoes are very, very comfortable

I have a wide and flat feet so almost all shoes, even running shoes, hurt my feet. but Naturalizer has been amazing
[owapib9] (score 1, diepte 0) I wear barefoot shoes from Merrill most of the time but they’re not BIFL unfortunately. Keep in mind that we’re conditioned to think that stylist shoes have some pretty specific shapes to them and shoes that are actually good for foot anatomy don’t fall into those styles. You might have to redefine what you think of as stylist to find shoes your feet will like. Good luck.
[owayaap] (score 1, diepte 1) Man remember that few years right after the PE buy out when Merrill made business casual shoes?

I still have chelsea boots and slip ons from that era. They were amazing
[p0nq6se] (score 1, diepte 1) Dress shoes please !! Any suggestions? I need them for work. Classy.
[p0npovn] (score 1, diepte 1) What do you wear for professional purposes? Like for work.
[p0nqmlu] (score 1, diepte 2) If I’m going more business a pair of Shapens (their poppy sandals are good flats) or an actual pair of flats. Usually I can just wear fashion sneakers though.
[owat823] (score 1, diepte 0) I got a pair of new balance runners that were a wide but had lots of padding in the heel that holds my foot it. They ended up being white and not that ugly (usually all my runners are). I did spend well over 200 on them though but now I'm not dying when I walk
[owgiizd] (score 1, diepte 1) I second this, very comfortable and not too expensive.
[owato6a] (score 1, diepte 0) This [substack](https://substack.com/@beyondbarefoot?utm_source=share&utm_medium=android&r=1lzh6a) posts all about shoes like that, in a wide variation of styles and price points
[owaunpc] (score 1, diepte 0) My feet are like this, and I like Ryka for athletic shoes and Vivala for dress shoes. Both brands seem to fit right out of the box.
[owb2ll7] (score 1, diepte 0) magical shoes from Poland
[owbeyzn] (score 1, diepte 0) barefoot shoe wearer here, i've tried a few different barefoot shoes/wide toe box

my favorites have been splay shoes, they make a more trendy style knock off vans essentially, or some that looks like basic keds style. go with anything casual shoes. plus, look at their clearance, you can find great options in there for really reasonable prices.

https://splayshoes.com/

sandal wise, i tried xero, but didn't enjoy them, ended up with earthrunners, very minimalist, just a foot bed a strap, but feels like you're wearing nothing. which was what i coveted.

https://www.earthrunners.com/

boot wise i landed with jim green x rose anvil barefoot ranger boot, these have been pretty great and they shine up well with the nice leather i use this boot for anything, it's my dress shoe as well.

https://jimgreenfootwear.com/
[owbhbd2] (score 1, diepte 0) I've got a skinny heel and prefer a roomy toe box. Heel size matters less in boots and backless shoes, so those are easier to find. Sorel is a good, comfortable boot brand, but you might have to fool around with size.

In sneakers, I usually go up a half to a full size to get the toe box right. I care less about length and more where the cinch and toe wiggle are. I like my heel to not be slipping everywhere, but it doesn't crazy matter so long as I can cinch comfortably right around my arch and wiggle my toes a bit. Boxy sneakers work better as you might imagine, but you can often just creep up the shoe sizes until you get your heel, arch, and toe wiggle. Currently for fashion sneakers, I have Fila and Saucony, and for work sneakers, I have Merrell.

For heels, I like Dr. Scholl's which is absolutely insane because wtf, Dr. Scholl's. It's usually a very rare style I like because then I'm balancing the blister risk and where the straps hit along with wanting leather, not pleather. When they make a style I like, I buy up. I can only handle backless sandals and prefer a wide strap or two with a 2" or less difference between the platform and heel, and I do prefer a platform for that height boost without the discomfort.

Hopefully that gives you some leads, but remember to throw shoe size kinda out the window with laced shoes and boots. You can buy longer until you get your room or it's just no longer feasible.
[owbzlty] (score 1, diepte 0) I'm not going to suggest what is stylish for a young lady, but I will suggest you search for any brand name, your size, and add D, DD or Wide. Lots of brands have wide options, they don't always call it that

Hope your feet feel better soon, good luck in your search!
[owc3rgn] (score 1, diepte 0) I have narrow heels as well and I use tongue pads under any shoe that has tongue and laces. Actually I use them in my Merrell clogs as well. If you find a shoe that is wide enough at the toes but a bit too wide in the heels you might find that a tongue pad solves the problem.
[owc7k1m] (score 1, diepte 0) Hey OP, would you be willing to draw us a photo of your foot shape? Like all I can picture is an elongated trapezoid. I feel that we could help better if we have an image to go off of
[owc8glj] (score 1, diepte 0) You’re looking for a combination last. When I sold shoes I liked the brand AGL for this foot type.
[owcc47u] (score 1, diepte 0) Another vote for Altra
[owd247a] (score 1, diepte 0) Vans or any skate shoe really.
[owd4g9m] (score 1, diepte 0) I recently got some white leather sneakers from Birkenstock that are super cute! (31F, size 8, I got a size 39)
[owe30sv] (score 1, diepte 0) Merrill Agility Peak 5 is a trail running shoe I’ve been wearing as everyday shoe for years. Great color-ways — some are really fantastic . There’s still a good amount of them online even though the “6” is out now (but not nearly as cute : (. )  I’ve never seen this shoe in stores in the US for some reason, but they were all over the place when I was visiting New Zealand.
[owef96m] (score 1, diepte 0) If you want something funky, try Fluevog. Enneagram is especially good for a wide toe box.
[oweioge] (score 1, diepte 0) If you shop at Nordstom, it is my understanding that they will still customize a shoe fit with things like padding at the heel.
[oweko7d] (score 1, diepte 0) I’m a huge fan of Origo! Their shoes aren’t flashy but they are very well made.
[owev2n9] (score 1, diepte 0) Bedrock mountain clogs. Resole-able. My wife loves my first pair so much that I had to buy a second pair for myself. My oldest pair of Bedrock sandals (also stolen by wife) is nearly 10 years old, haven’t needed a resole yet. I don’t know what you consider as cute subjectively, but this is all the rage for cadaver lab attire changing frequency for my school (postgrad). I’ve seen undergrads wearing them too. https://bedrocksandals.com/collections/bedrock-mountain-clogs
[owex27q] (score 1, diepte 0) Hanwag has deveral bunion models of shoes and hiking boots
[oweydsp] (score 1, diepte 0) In sneakers, I use the runners loop to help secure my heel. I also skip lacing in the first pair of holes nearest the toes, so I get a little extra toe space that way.
[owfg8jd] (score 1, diepte 0) Lems and altras. Now that lems has really expanded their styles (winter boots, 9 to 5 shoes, etc) I have ditched all my other shoe types and brands. I have a couple pairs of altras for serious hiking, Lems for everything else.

They have wide toe boxes, regular heels, and zero drops. This is all the pros of barefoot style shoes without a) looking goofy as hell b) having no protection between your foot and city streets or c) getting into woo woo connecting with the ground spiritually style beats. Just the stuff that works. When I finally got into Lems, I actually had to size down because I had been wearing too big of a size to get the shoes to fit my feet shape better.
[owfippm] (score 1, diepte 0) I don’t know which country you are in but I love The Merchant. 🇳🇿
[owfwgrt] (score 1, diepte 0) If you’re looking for hiking/walking shoes specifically I recommend the salmon elixir activ!! everyone says salmons run narrow but this pair has a wide toe box. I have the same issue as you and got these and love them :) and they’re not ugly lol
[owm7igp] (score 1, diepte 0) I’ve had good luck w Saucony sneakers and running shoes for this shaped foot
[ox6yuyk] (score 1, diepte 0) Perhaps a shoe subreddit  
Would be best to ask in
[oxiyg72] (score 1, diepte 0) Hi! 😊 Your foot structure of wide forefoot with relatively narrow heels is actually more common than people think. A lot of shoes are built for more uniform foot proportions, so it's understandable that you're struggling.

Where are you based? If you're ever in Singapore (or elsewhere in Asia), we'd love to help. At Oleah Handcrafted (www.oleah.co), we work with women who have exactly this challenge by combining a roomier toe box with complimentary fitting adjustments, including custom heel grips where needed, to help prevent heel slippage while keeping enough room at the front.

If you're based elsewhere, let us know which country you're in—someone in the community may be able to recommend brands that are more accessible locally. Wishing you all the best in finding something that works! 💛
[oxs2lwp] (score 1, diepte 0) Does anyone have heel brand suggestions for this type of foot. The suggestions I’ve seen are kind of ugly/ sneakers.
[owaydhp] (score 0, diepte 0) Try Birkenstocks or Vionics!

=== THREAD xr9gkx ===
SUBREDDIT: r/Frugal
DATUM: 2022-09-29  SCORE: 48  REACTIES: 66
TITEL: Cold feet?
POST (source_id=post):
I have Raynauds, and chronically low blood pressure and poor circulation. My feet can go numb and start hurting in the cold. Honestly when it starts dipping below 70 degrees I get cold, and so do my feet. I live in the Northeast US (sobs in snow).

I don’t have much money right now, but I’m looking for a warm pair of socks. I’m actually allergic to wool and break out, so I can’t wear wool socks.

Fluffy socks are nice but my feet are still kinda cold, and I can’t wear those to work. It seems like I may need something tight and warm to keep the heat in. 

I don’t know if compression socks would work well or not. I saw they have electric heated socks but they are really expensive. Health tips to manage this would actually be appreciated too.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iqdui2c] (score 67, diepte 0) I have Raynauds! The answer is hiking socks, from a outdoor store. They’re usually rated to a certain degree of cold, some brands make ankle socks and not just calf length, so you should be able to find some for work. I literally have a bucket of fluffy, hiking, and thick ankle socks, and a bucket of gloves, and one of scarves…
[iqdl93j] (score 20, diepte 0) Can you get a spot heater for under your desk? If you work at a desk. 

&#x200B;

Tight compression socks will probably not work well, they will restrict the blood flow even more. Those are good for people standing/waling all day who who tend to get the legs swollen by the end of the day.
[iqdm0ia] (score 16, diepte 0) Silk works really well for warmth.
[iqe8i8u] (score 15, diepte 1) Seconding hiking socks! All mine are tight, black and ankle length so you wouldn’t even know they’re hiking socks but they’re very comfortable and much warmer than regular cotton socks.
[iqdzyml] (score 14, diepte 1) I'm sure you mean well with this suggestion but as the IT guy for many many cold office buildings over the years, please for the love of god OP do not bring in a space heater. Even the nice ones are horrible for destroying electronics on the same outlet and that's not even accounting for the extra heat.

I'd so much rather anyone cold get an electric blanket if absolutely necessary.
[iqds3mh] (score 13, diepte 1) I agree with silk. OP, do you think you could handle thin silk socks and medium wool socks over it without it touching your skin?  It's also worth trying compression socks that aren't overly tight to see if that helps circulation as well.  Whatever you do, stay away from cotton socks.  The key is getting something that will also keep your feet dry.  

Living in the NE US also, I deal with Raynaud's on my hands and have poor circulation too.  I have found that wearing warm or insulated items don't matter until my hands/feet are already warmed up unless I'm doing physical activity (shoveling snow).  You didn't say what kind of work you do, but are you able to use something to warm your feet while at work, such as a hot water bottle, small space heater, electric blanket or even going so far as a warm foot soak?  If none of those work, maybe brisk, frequent walks to get blood flow going could help.  On really rough days, I've even stuffed Hot Hands into my shoes.

And don't forget to keep your core warm with layers and/or vest, even a hat if you can.  If using a hot water bottle on your feet is weird, maybe even tucking that on your core could help too.  Drinking hot liquids helps too.  I know the pain of the cold and I hope you find warmth!
[iqdnsmf] (score 10, diepte 0) I’ve read that it’s actually better to wear loose clothing when it’s cold, because more warmth comes from air trapped between layers. If you have cold feet it might work to get shoes that are slightly big? I don’t know how annoying that would be, but either way try to have more space inside your shoes (like not cramming in your foot with thick or multiple layers of socks on). My dad has reynauds and I know it’s really painful and hard. Sorry :(
[iqdpjv3] (score 9, diepte 0) Wear two pair?  The insulation effect will be higher.
[iqe9mmb] (score 9, diepte 1) Came here to say this, they don't even have to be fancy expensive hiking socks. I got some cheap ones on Amazon and they are great for hiking and keeping my feet warm when the temps drop.
[iqe1b40] (score 9, diepte 0) I have a friend with Raynaud's who's allergic to wool and has the same trouble with cold feet.  I got her a pair of Thermup electric heated insoles a few years ago, and she says they're great.  You trim them (per marks on the insoles themselves) to your exact size and can wear them in any shoes or boots.  They have several temperature settings and are waterproof.  They're machine washable, but don't need washing anywhere near as often as socks (assuming you wear socks when you wear your shoes/boots) so last a lot longer, and they use lithium-ion battery packs that strap to your ankles rather than having to fit in the shoe.  For her they've apparently been a pretty good long-term solution.
[iqdpvvn] (score 8, diepte 0) I'm not allergic to wool but find it itchy so I'll wear a pair of cotton socks with wool ones over them. You get the benefit of layers of insulation too. Bonus frugal points because you can buy the cheapest wool ones. You could triple layer with nylon knee highs. 

I haven't looked at prices for heated socks but you might get them cheaper through hunting supply sellers rather than other places. 

Since circulation is an issue I'd definitely give compression socks a try.
[iqev7rw] (score 7, diepte 2) They can actually prescribe viagra off label for Raynauds. It increases blood flow to extremities
[iqdtukc] (score 6, diepte 0) I also have Raynauds.  Talk to your doctor about medication.  If your feet are going numb and hurting, it’s time for medication.
[iqe86bv] (score 6, diepte 0) I’m also allergic to wool and find layering thick socks and then wool often helps because there’s really nothing in my experience that’s as warm for as little money as bulk buy store/generic brand hiking socks. Depending on your allergy though that may not be an option, I’ve also used socks and fuzzy slippers, and those small reusable click hot packs layered in my socks/slippers
[iqdqs11] (score 5, diepte 1) Regular socks with fluffy socks on top would be my choice.
[iqfnfgv] (score 4, diepte 4) Here’s the secret: a lot of doctors suck.
[iqemxea] (score 4, diepte 0) heavily insulated winter hiking boots, waterproof ones get even warmer
[iqdfuy3] (score 3, diepte 0) You need a reliable source of heat for your feet. A hot water bottle could probably help you too if heating boots or blankets are out of budget.

That's only good when you're at home and not moving around though. I don't have any advice on good socks, sorry. Maybe try layering them?
[iqfxxh6] (score 3, diepte 2) How does a space heater destroy electronics? By using too much energy or from heating up the electronics surrounding it?
[iqe1k7p] (score 3, diepte 1) Compression socks help improve blood flow, they do not restrict blood flow. They do need to fit properly for this to work.
[iqe7uk9] (score 3, diepte 1) Alpaca, too. My local outdoorsy shop is selling alpaca socks these days.
[iqdokd8] (score 3, diepte 0) Have you tried Alpaca socks? They are my favorite!
[iqdzvpm] (score 3, diepte 0) silk under MERINO wool

Plug-in heating pads for when you are stationary, variable control at hand

Go to bed with a hot water bottle in a towel cover/bag
[iqdf5ke] (score 2, diepte 0) I wear Real Tree socks. Sold on Amazon.
[iqidqaj] (score 2, diepte 3) Both of these things are true, but usually the too much energy pull is the bigger issue.
[iqgo64u] (score 2, diepte 2) It’s pricey but I second the silk socks under wool socks since my skin is sensitive to wool. I also have silk leggings to go under my thick wool leggings which I wear winter camping, it works really well.
[iql5tg9] (score 2, diepte 2) Can confirm this works plus isn't terrible for my foot comfort!
[iqdpkho] (score 2, diepte 0) Do you sit at a desk? Take advantage of having a medical issue and get the business to allow you to put a heater under the desk. I think thicker soles on your shoes would be the goal. When my feet get cold, it is most often from the cold floor transferring through the soles, not the loss of heat from my feet. The good news is that the chunky sole look is trending right now. Or get platforms.

(My Raynauds is in my hands, but I have occasionally found my feet to be slightly sensitive.)
[iqe12zm] (score 2, diepte 1) Two other suggestions for a desk job: A standing desk (ideally sit/stand) and taking frequent breaks. Sitting is terrible for circulation.
[iqdqhkm] (score 2, diepte 0) Don't waste your time with electric socks, they give out half way through the day. 

I have super thick socks, think hunting section at sporting goods store. The biggest problem is that my shoes don't fit with socks that thick. They are good for my slippers.  I keep a cheap pair of lined slippers under my desk, and I keep my feet off the floor (on the chair wheels instead). 

I feel your pain and your cold!
[iqex9vx] (score 2, diepte 3) Lmao that’s hilarious. Apparently my doctors want me to suffer…
[iqg35vc] (score 2, diepte 1) Adding for OP.. You can shop the clearance section at a place like REI or Dick’s, or try steep and cheap or backcountry websites for marked down hiking socks. They can be expensive
[iqgf65j] (score 2, diepte 1) I use a fired women’s pair them a larger mens pair on top for bed. Zippo also makes a refillable/reusable hand warmer so you’re not buying disposables all the time.
[iqduj30] (score 2, diepte 0) I usually wear 2 pair of socks and slippers with fuzzy lining inside the whole thing. Keeping my feet as far from the cold floor as possible really helps me. I have been known to bring magic bags to work, microwave them and set my feet on them.
[iqdwd6j] (score 2, diepte 0) My grandma had Raynauds and she wore compression socks. Long ones to just under her knees.
[iqdzau1] (score 2, diepte 0) As I've gotten older, my feet gets really cold in the winter. I've found that for me, what works best is wearing cheap polyester dress socks, then wearing thick cotton socks over that.
[iqf9f6o] (score 2, diepte 1) These sound amazing
[iqee4o6] (score 2, diepte 0) The problem with Raynauds is there is very little circulation to the toes/fingers so thick socks that work on others don’t work for us because they’re insulating cold feet that aren’t producing much warmth to insulate. Better to buy a plug-in type heating pad and warm them from the outside. You can keep one under your work desk. A bucky microwaveable buckwheat pillow is great for the house where you may settle in many different spots. If you’re moving around a lot the dollar store had those warm hands shake to activate packets. Or warm the feet first and insulate over already warmed feet.
[iqev9ny] (score 2, diepte 0) I find if my feet are cold...my socks are just as cold.  I started tucking them under my dogs belly.  Lol..they dont mind!  Try rubbing them, get up and move a bit if youve been sitting.
[iqfap3w] (score 2, diepte 0) I have Raynauds, too.

If you can, get yourself a pair of thigh high socks and then wear another regular pair over them.  

It makes a huge difference in comfort to have warmth all down your legs.
[iqfox8k] (score 2, diepte 0) The same people that make “hot hands” make “Cosy toes”. They’re air activated foot warmers. Thin and stick to your socks to keep them in place. Paired with some silk socks or hiking socks it might be a winning pair.
[iqfs6ne] (score 2, diepte 0) [https://costplusdrugs.com/medications/tadalafil-5mg-tablet/](https://costplusdrugs.com/medications/tadalafil-5mg-tablet/)

Not to give medical advice because I am a nurse and I am not a physician. I have a few patients with raynaud's phenomenon and the doctor that I work with (a specialist, not a primary care physician) prescribes Cialis. This is where you could buy it at the lowest cost. It works for most patients – and you do not need a higher dose so a higher strength can be cut and have if you need to and save even more.

Best wishes to you.

https://clinicaltrials.gov/ct2/show/NCT00822354

This note was created with Dragon Medical, a voice recognition software. Occasional incorrect words may have occurred due to the inherent limitations.
[iqg1edh] (score 2, diepte 0) Petroleum jelly rubbed in and two sock layers is the only thing that works for me.
[iqgltgs] (score 2, diepte 0) My daughter bought me heater socks that have a rechargeable battery. Must have!!
Also, a heated mattress pad is better than a heated blanket IMO. Reynauds Sucks! And people who say to add more layers are delusional. It’s a cold burning from the inside. Layers don’t matter
[iql666z] (score 1, diepte 1) Hot water bottles! One for each foot!
[iqif0t0] (score 1, diepte 1) I typed a longer response a little higher up but space heaters under desks are a bad mix in all situations. Standing desk or an electric blanket are more appropriate solutions and definitely things most businesses will gladly approve.
[iqdrqr9] (score 1, diepte 0) Silk, alpaca, quiviut, Australian possum. These are all really warm natural fibers.
[iqdunxp] (score 1, diepte 1) I was told there’s no medication for Raynauds besides a gel to rub on your skin?
[iqeaehz] (score 1, diepte 0) I found a pair of inserts yesterday specifically for insulation in your shoes. Uh look up on amazon, for thermal shoe inserts.
[iqej2pt] (score 1, diepte 0) I use a heating blanket at home. If you work at a desk maybe you could bring one in?
[iqejanx] (score 1, diepte 0) What kind of work do you do where you can't you wear "fluffy" socks to work?

If you *can* manage to wear thicker socks at work, also consider going up a half shoe size, so that the socks (and your feet) aren't compressed. Much warmer.
[iqewh3j] (score 1, diepte 0) Sheepskin shoe inserts are amazing for keeping boots warm
[iqf2t4q] (score 1, diepte 0) I have a leather and fleece vest I wear in winter in Canada.  You might have good luck with hiking socks and moccasins
[iqf98o1] (score 1, diepte 0) Heyyy fellow raynauds friend. 

I use a generic plug in heating pad that I purchased with my HSA account from the HSA online store. I simply plug it in at my desk and keep it on low and cover my feet with it. 

I use an electric blanket at home. 

Compression socks will help with the circulation but you’ll still feel cold. 

When I don’t want to use so much electricity at home, I use microwave heating pads that are filled with rice, corn or dry beans. They work really well.
[iqfnqms] (score 1, diepte 0) No one is mentioning vapor barrier clothing. 

There are specialty "vapor barrier" socks, but I'm too cheap. I find that wearing long plastic bags (like bread bags or newspaper bags) over a thin liner sock, and under a thick sock keeps my feet comfortable and *toasty*.  Your feet are slightly damp when you take off the socks, but not swampy. 

Much of the heat you lose is from evaporation, which is a powerful coolant. You will realize just how much when you take the vapor barrier off, and your feet get cold immediately.
[iqfrvfy] (score 1, diepte 0) Heat holders are the best brand socks I’ve found for winter with raynauds. They are super soft and thick. They are a bit pricy online but you can usually find them for around 7$ a pair at academy. Best money I’ve ever spent on winter socks and I work outside year round.
[iqfv461] (score 1, diepte 0) I have raynauds, cold exposure is your friend! Can wear the thickest socks in the world and still have cold feet because there is no blood reaching them. 
I used to get uncomfortable hands/feet under 70 degrees wearing layers. I started taking consistent ice baths and have almost entirely fixed the symptoms. If I get lazy and skip them I notice my feet toes start going numb again quick.  Sauna/ice bath contrast therapy is what I do and I can’t recommend it enough
[iqfwakj] (score 1, diepte 0) I'm allergic to wool as well. I purchased some alpaca socks and gloves last winter. Holy crap they were too warm at times. I don't have raynaud's but poor circulation. My feet were almost always cold. 

I bought them on Etsy from Enchanted Meadows Paca. I can't link the store or my comment will get booted.
[iqgrv1d] (score 1, diepte 0) Depending on your footwear you could try adding sheepskin insoles, I have some in my blundstones and they really help my feet stay warm in the winter. I bought some that you basically cut to size of your insoles and they were way cheaper than the blundstone branded sheepskin insoles.
[iqhgno5] (score 1, diepte 0) I hope you find some good hiking socks! Since a lot of them contain wool I was reading about wool allergies and found [this](https://pubmed.ncbi.nlm.nih.gov/28350041/). It’s possible that wool isn’t an allergen and it’s the coarse fibers or residual substances like lanolin that cause the contact dermatitis.
[iqu7pii] (score 1, diepte 0) Check with your doctor to see if you would benefit from prescription compression stockings. Your insurance may even cover them.
[iqfoqi3] (score -2, diepte 0) Reynauds is a symptom imho. Have you tried TTFD, b12 shots/ iron supplement and a good multivitamin with methylfolate. Health is not the place to be frugal. This sounds like anemia. Trying to help fyi not criticize.

=== THREAD 17785w6 ===
SUBREDDIT: r/Frugal
DATUM: 2023-10-13  SCORE: 22  REACTIES: 66
TITEL: My shoes for flat feet are too expensive
POST (source_id=post):
I work at a warehouse full time and have the flattest feet imaginable. Like rectangle footprint flat feet. The best shoes I've found to not have horrible foot pain are Vionic Orthaheels but they are $109 dollars. Are there any non arch, flat footed, stand all day people here with a good recommendation for affordable shoe options? Thanks in advance.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k4rfes0] (score 114, diepte 0) If you can afford your shoes at all, get them. Shoes should not be where people skimp because if you mess up your feet, it messes up the rest of your body.  You know how they say “no hoof, no horse”?  Same idea.  Take care of your feet as best you can.
[k4rbozc] (score 58, diepte 0) My insurance covers my inserts - if it’s an option for you.
[k4rfud4] (score 25, diepte 0) Shoes.tou need ARE frugal.
If the brand is reliable and holds up, just bite the bullet.

(Mine are more expensive than that, FWIW. But it's that, or surgery in the not too distant future. So. Good shoes it is.)
[k4s82jh] (score 22, diepte 1) Exactly this. Two areas you shouldn’t skimp on are the things you spend 8-ish hours a day in— your shoes and your mattress.

Your body will thank you.
[k4ras9w] (score 11, diepte 0) Flat foot insoles can be pretty good. Especially with trainers with good soles. They're pretty cheap. Some people like the gel. The cushioned ones breathe better.
[k4suryr] (score 8, diepte 2) Your mattress is where most people skimp on... Memory foam.... Will change your life
[k4ri4zs] (score 8, diepte 0) Try a Podiatrist, I had custom inserts made and they are worth their weight in gold. Unfortunatly, they cost their weight in gold. But, they kept me working another 10 years.
[k4rjyvj] (score 8, diepte 0) I have orthotic insoles that you can put in any shoes they’ll fit in. They’ve lasted me probably 15 years so far.

If it doesn’t gross you out, you could also look online for a lightly used pair of the Orthaheels. Personally I don’t care about having second hand shoes but I know some people do.
[k4rkhg1] (score 8, diepte 0) I'm a vionics convert. And I have $300 orthotic insoles for my tennis shoes. I don't regret using this money, but I can understand if that's too much for you. Tbh, I feel like $109 for decent shoes isn't bad. One thing to make your shoes last longer too is to get two pairs and alternate them each day so they can air out.
[k4rca42] (score 7, diepte 0) I have moderately flat feet and was having foot pain/tiredness.  I had to get custom orthodics made.  It helps my feet from getting tired standing all day.

If possible, I would spend the money on getting orthodics... maybe not custom made, but ones for flat feet like Superfeet.  Reducing the pain for your feet is money well spent.
[k4sca6e] (score 7, diepte 1) Agree.  I'm dealing with extreme pain from plantar fasciitis bc I wore the cheap shoes for years.
[k4rizqb] (score 7, diepte 0) Find a way to spend the $109; you work on your feet, your whole body will thank you...
[k4rthzo] (score 7, diepte 0) It’s worth checking if they give a stipend for work boots, some companies will. 
Also, did you know that work boots qualify as a tax write off for self employed and traditional warehouse workers? 
Have you tried the bionic orthaheel inserts?
[k4swpb5] (score 5, diepte 0) Look for like new pairs on poshmark/eBay/three up etc. people buy shoes all the time and only wear them once or twice. 

Otherwise, buy the shoes.
[k4rezk1] (score 4, diepte 0) Try Keens.  Wide toe box, I don't notice that they have an arch, really supportive in my view, and durable in my view.  Also rugged materials in many of them so they are protective.  However they are also in about that price range.  They go on sale from time to time, either at REI, or on their website, or I have seen them on steepandcheap and other clothing outlet websites.
[k4rk680] (score 4, diepte 0) Check Ebay for Naots.  At the store they are expensive but gently used on Ebay they are much more reasonable.  Best shoes my wife has ever worn.
[k4tp8r8] (score 4, diepte 1) If you can find a store that accepts returns that would be great. I too have very flat feet.  I had heard such wonderful things about Hoka that I bit the bullet and paid a good amount for them.  They hurt my feet so bad that I literally couldn't walk for 2 days.  Thank goodness REI would accept return.  I bought another pair of New Balance sneakers to wear with inserts.  I have heard great things about Vionics from a niece who also has very flat feet but have not tried them yet myself.  Take care of your feet...they work hard for you!
[k4sb6mm] (score 4, diepte 0) It’s not worth the pain that bad shoes will bring if you work on your feet all day. It will cost you way more in the long run. Vionics are great shoes. Consider looking into orthotics.
[k4rb74e] (score 3, diepte 0) Get flat foot insoles and trim them to fit if needed. I got 4 pair, 3 from walmart and 1 from amazon, and trimmed them to fit in my shoes, and they work great. Much cheaper than getting specialty shoes and the insoles are transferrable if need be.
[k4tq9fg] (score 3, diepte 1) I use superfeet, at this point I think I’ve tried every off the shelf insert around. These ones have lasted a long time. Most get compressed after 6 months or so and become useless.
[k4rdas3] (score 3, diepte 0) My Dad had flat feet and he worked on his feet.  He was particular about brands, but it’s been years.  I DO know that his situation improved when he got inserts from the Podiatrist.
[k4sgdov] (score 3, diepte 2) Dr. Scholl’s plantar fasciitis inserts, or the Walgreens brand. Saved my poor feet. Working on concrete for decades w/o proper support. I wear Skechers shoes and replace them every 6 months or so.
[k4sv12a] (score 3, diepte 1) What about Brooks or Hoka?
[k4rpxlo] (score 3, diepte 0) This is one area you should splurge. It'll get more expensive later in life if you cheap out on shoes, with leg and foot problems.
[k4sibbb] (score 3, diepte 0) I'm not the most frugal person, but a well made comfortable pair of shoes at that price is reasonable.  Some things you don't want to skimp on and your feet are one of them.  Cut something else.
[k4xkn17] (score 2, diepte 1) Seconding the podiatrist. Sometimes all they can do is tell you to wear supportive shoes and/or orthotics, but sometimes things like exercises can help.
[k4rilz4] (score 2, diepte 0) I routinely buy those 4E wide shoes from the standard brands of shoe makers at like discount shoe stores and have some good experiences with them. 

Buy the wide under armour athletic shoes they are $60 typically for me. I have had the least amount of pain on my super flat feet from that brand.
[k4soo7w] (score 2, diepte 1) This! I have plantar fasciitis and Naot brand shoes are amazing! I get mine on ebay and can almost always find some open box ones for below half what they cost anywhere else.  


I work at Walmart as an online grocery picker(I shop for online orders all day) so I am on my feet all day and walk 8-10 miles a day(hey it's free exercise while I work) so I can't afford to have aching sore feet. Naot shoes are the only ones I can wear and not be miserable.
[k4txzsp] (score 2, diepte 3) Brooks have 4E
[k4vmzma] (score 2, diepte 3) My husband has super wide feet and the running store suggested hokas! He loves them
[k4vp83p] (score 2, diepte 4) Thanks for the suggestion. Seems I will be checking out both Hokas and Brooks.
[k4rupju] (score 2, diepte 0) I just helped my mother buy some shoes and she has the flattest feet I’ve ever seen.  

Check out Hoka Shoes (Arahi 6).  They’re a bit pricey but so worth it if you’re flat footed.  They also have a ton of cushioning which is perfect if you’re on your foot all day.  I recommend buying directly from their website bc of their excellent free return policy.  you can try them on for 30 days and you can return them no questions ask even if you wear them everyday for 3 weeks.   If you want something cheaper just buy their Arahi 5 which is last years model. 

Another brand you can try Brooks Running Shoes (Adrenaline 23).  You can also try their Adrenaline 22 which is on sale.  Brooks return policy is 90 days free return no questions ask even if the shoes are worn out.  

Before buying on their website, I recommend trying both shoes on at Dickssportinggoods so you have an idea what size to order.  Dickssportinggoods doesn’t offer the same return policy as buying directly from the company reason why I recommend buying online.
[k4s3ldj] (score 2, diepte 0) I’m extremely flat footed and also worked in a warehouse during college. I tried to cut corners and wear older sneakers, etc. - fucked me up. Ending up spending a lot more on time and money with medical. 

If you can get cheaper shoes that still work - great. If not just look at those shoes as a way for you to earn money and support your health
[k4sjxx4] (score 2, diepte 0) It looks like that brand sells inserts, you can put them in any shoe. Google says they’re around $35.
[k4tcjkf] (score 2, diepte 0) I just checked eBay and you can find them much cheaper there! Hope this helps you!
[k4tw5xr] (score 2, diepte 0) Does your work offer a reimbursement plan or a service to order your shoes through? I also work in a warehouse and we get an annual budget for shoes ($150).
[k4tx5nt] (score 2, diepte 0) The best way to correct flat feet is to work out barefoot. Your feel are flat because shoes prevent you from properly using your foot muscles.
[k4u7dvs] (score 2, diepte 0) Do exercises to improve foot strength and correct the imbalances causing the flat feet. That way over time you can lose the shoes.

Which by the way quality shoes are always going to cost that.
[k4uz7b9] (score 2, diepte 0) Does your employer have a health FSA or HSA plan? Your doctor might okay these shoes as reimbursable.
[k4rchra] (score 1, diepte 0) Idk about affordable, vivo barefoot have lasted me a long time so far and imo very worth it
[k4rk8fc] (score 1, diepte 0) You can buy Vionic insoles and put them.in any shoe. They sell a few different styles.
[k4t17nq] (score 1, diepte 2) Decent pairs of either brand are more than $109
[k4t1zaf] (score 1, diepte 2) I have wide feet so I can only use New Balance. I'd love to try those brands because I've heard great things but I don't think they'd be wide enough. I like Vionics for sandals (and I'll probably get a pair of their heels). Great support for the other types of shoes.
[k4svdub] (score 1, diepte 1) Brooks Beast
[k4rxw4r] (score 1, diepte 0) Aisics
[k4sa95d] (score 1, diepte 0) So I'm not sure if this would work for you, but you may want to look into zero drop shoes or barefoot shoes. There's a range in how thin or thick the soles are (depending on whether they see designed for you to feel the ground or not) but they generally all are very flat and have wide toe boxes. 

Lem's is one of the bigger brands. I've got their boots and they are great. I've also got some Whitin sneakers that I like, but those may be too thin for your needs.
[k4scd7w] (score 1, diepte 0) Spenco orthotic insoles are great. They make any shoe better.
[k4sx6nl] (score 1, diepte 0) Flat feet are caused by weak muscles and over stretching of the ligaments in the feet. so splurge on the proper insoles for your warehouse job, but don’t skip feet exercises, those will help preserve/ improve the strength and comfort in the long term
[k4tbt0f] (score 1, diepte 0) I’m glad you’ve found a comfortable shoe. But there may be an even better one out there! Or maybe not! But it’s worth exploring. Get fitted for quality shoes and inserts at a reputable shop. Like marathon sports. Don’t go to a shoe store, go to a running store! Find your perfect combo then start scouring eBay for retail returns. That’s how I afford my hokas. They are basically brand new, might have a scuff or two, and like half the price! 
  
I hope you see this u/stinkfistian, because shoes are so incredibly important. Your long term mobility depends on wearing quality, supportive footwear. I have major problems with my hips and back, and my hokas are amazing for me. With my orthotics!!
[k4u0d5q] (score 1, diepte 0) Does your employer help
At all 
If you
Have flat feet they may contribute as
It’s maybe a potential
Disability.  ?
[k4u40hy] (score 1, diepte 0) Laughs in $600 inserts.
[k4u4rzd] (score 1, diepte 0) Vionic arch support insoles are $39.99.
[k4u4vc9] (score 1, diepte 0) As someone who works on her feet on hard cement floors I agree with others. Don't skimp on shoes. I'm still looking for something that doesn't kill my feet and in return my hips and back. Unfortunately I'm required to wear steel toe which makes it harder to find a comfortable pair of shoes.
[k4u7145] (score 1, diepte 0) I have super flat feet and converse are my jam. Wear them for double bar shifts all the time.
[k4ubtbx] (score 1, diepte 0) Get some good orthotics and put those in whatever shoes you want. My podiatrist recommends PowerSteps. You still need reasonable quality shoes, but $50 New Balances work. Alternative do you have decent insurance and can you get your doctor to prescribe orthotics? I have custom ones now and they are sooooo great.
[k4ulnjk] (score 1, diepte 0) That is just how much shoes cost these days if you do not want to have foot pain. I can rarely find cheaper. But it is less than paying for a doctor. 

The best deal I have found is to try on some Merrell and Brooks at the store (my preferred brands for walking), find which are best for my feet and then try to find last year’s version on line at a discount because they update them every year. I recently got a nice pair of Merrell’s because DSW is selling “3’s” for $100 but Sierra was selling the “2’s” for $50 with free delivery to the store nearby.
[k4umbut] (score 1, diepte 0) If you're in the U.S. try to order shoes on black Friday or cyber Monday to see if there are any deals
[k4vadmr] (score 1, diepte 0) Buy the vionic shoe inserts and change from one she to another.
[k4vhciw] (score 1, diepte 0) Idk what kind of safety shoe requirements your work has, but if there aren’t any, I have good luck with outlets for end-of-season running shoes at a discount. Look for the models built for “stability” to get arch support. 

Because of congenital deformities, I have one flat foot and one exceedingly flat foot with bunion and arthritis. I prefer New Balance to Brooks—Brooks made a design change to the Adrenaline several years ago to prevent knee pain, which then screwed up my shins and ankles—but YMMV. I don’t know if Brooks has corrected the design since. I’d suggest going to a sporting goods store to get an idea of how your preferred brand is sized before you order online—I’m a 9 in normal people shoes, but a 10 wide in New Balance.
[k4wpsjm] (score 1, diepte 0) If the $109 shoes prevent you from developing future health problems, which WILL cost more, then the $109 shoes are the frugal option here. Don't skimp out where your health matters.
[k4xx0gf] (score 1, diepte 0) I have had same issue. Lady at foot store recommended certain kind, they still hurt.
[k4xxf1t] (score 1, diepte 0) Get the shoes that work. Hell, if there are more expensive shoes that work but last longer, get those. Good shoes are worth the investment in normal times, but ESPECIALLY if you work on your feet, and ESPECIALLY if you have a medical need. Scour the internet for sales or coupons first, and charge them if you really have to, but get what you need, it’ll be worth it in the long run.
[k4yi2f5] (score 1, diepte 0) I will always pay for good shoes. I worked retail for a number of years and I would wear ill fitting fast fashion shoes that eventually messed up my feet. Now I always buy quality shoes that fit. In my opinion, it’s worth it.
[k5088c0] (score 1, diepte 0) My son has the same problem he swears by Vessi shoes they are also waterproof
[k5176n6] (score 1, diepte 0) Make yourself sandals. Buy feet insoles and tie with wires to your legs. I am genius
[k9u6aty] (score 1, diepte 0) I know this is a month out, but wanted to comment. I have been wearing Asics Gel Kayano for several years. They are made for overpronation and very comfortable. If you don't get the newest model on their website, they are typically discounted. Right now they are $99 with 25% off for Black Friday. I definitely recommend them.
[kup91a7] (score 1, diepte 1) We are removing your post/comment because of commercial/ad-like content. This includes:

- Linking to commercial sites, defined as a site which sells products/services through a cart, subscription, or booking appointments/trips. Talking about a site or product is fine, just don't link to it.

Please see the full rules for the specifics. https://www.reddit.com/r/Frugal/about/rules/

If you would like to appeal this decision, please [message the moderators by clicking this link](http://www.reddit.com/message/compose?to=%2Fr%2FFrugal&subject=Removal%20Appeal&message=Author%20would%20like%20to%20appeal%20the%20removal%20of%20their%20post%20because) within one week of this notice being posted.
[k4ui7hx] (score 0, diepte 0) If you don’t need safety shoes. Go with converse

