# Label-batch batch_0035

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
Schrijf het resultaat naar `batch_0035.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1214li3, 1llr90i, 1ajptgq).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1214li3 ===
SUBREDDIT: r/Frugal
DATUM: 2023-03-25  SCORE: 3814  REACTIES: 360
TITEL: Sorry if this has been mentioned before but as a woman with small(er) feet, I definitely do this to save some money.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jdkd5od] (score 680, diepte 0) I know it’s a splurge - but as a hockey fan, I save money by purchasing extra large youth jerseys rather than adult jerseys for my local team.
[jdkg5et] (score 514, diepte 0) I wear a size 4 US shoe. I have to shop in the kids section on the regular. Yes kids shoes are cheaper than adults but even the expensive brands aren’t made to last. For example most designer kids shoes are not made from leather (shoots angry looks at Michael Kors who makes kids shoes that are appropriate for adults but the damn things are pleather and shredded in my closet over the winter!) some kid versions don’t have arch support like the adult version (Sperry Topsiders) either. Then you get the rare and amazing brands like Dr. Marten and Uggs who make both kid and adult shoes from the same quality materials.
[jdkvke9] (score 356, diepte 0) Youth boys sized nikes instead of women’s 🤌🏻
[jdkn084] (score 237, diepte 1) Frugality is knowing when to save money and when to enjoy it! It's about doing it deliberately and meaningfully.
[jdkj4md] (score 172, diepte 1) Kids shoe sizes are crazy!  They start sized by age in months, suddenly they are regular number sizes, they go up to 13 then you start over at 1, then there is the wacky transition to ladies sizes (and higher prices). Ughhhhh like being a parent needs to be HARDER. 🤦
[jdkl70z] (score 156, diepte 3) pretty sure it's because kids sizing graduates to mens sizing.  kids/youth go 1 through 6, then pick up in mens sizing at size 7.

womens sizing is the weird one!
[jdklfm9] (score 142, diepte 1) yeah I wear ladies 8, so I can get away with wearing kids 6 or 7 depending on the style. so many big name sneaker manufacturers have terrible quality control when it comes to kids shoes, i had a conversation with a sales associate at foot locker about it, apparently its a whole thing.
[jdkdukb] (score 137, diepte 0) I get large tee shirts from the kid’s section sometimes. 

Suddenly, I feel like Angela from The Office 🤣
[jdknor0] (score 136, diepte 2) And strangely boy’s athletic shoes seem to be built better than girls even the same brand.
[jdkfi1j] (score 122, diepte 0) So a child 6 is larger than a ladies 6? How does that even make sense?
[jdm7qs4] (score 118, diepte 1) They probably have a slightly wider toebox, which is healthier too
[jdkofsm] (score 116, diepte 3) It's just the Pink Tax.
[jdkkcj1] (score 79, diepte 0) I have size 11-12 feet and I have no choice but to go to the men's section. Fortunately this means I am a size 9-10 mens which has a lot of offerings and I don't have to buy formal shoes which will never fit my feet so I can't wear them no matter what. They also make the same sneaker colors as in the Women's department these days.
[jdlhbl5] (score 63, diepte 2) All US shoe sizing is crazy.  Why is a women’s 10 a men’s 8?!?  In Europe, it is just one scale for everyone.  Babies start at size 18 or so, kids sizes are in the 20s and early 30s.  The bigger your feet, the bigger the number. My mind is blown at its simplicity!
[jdkqyw8] (score 60, diepte 1) Most the time with other brands the child sizes do take a hit in quality so do keep that in mind.
[jdkkgbq] (score 57, diepte 2) But that's what I mean.... 

So toddler sizes go up to 13 and then when you move up to kids sizes they start over at 1. So why doesn't it start over again when you go up ladies? How is a kids 6 bigger than a ladies 6? That's the part I just don't get.
[jdkxcry] (score 56, diepte 4) I've worked in a shoe store for 15 years, you are correct
[jdmb1jo] (score 56, diepte 3) Yes! I remember at 10 years old convincing my dad to buy me the boy running shoes and not the girl ones. They felt better and LIGHTER on my feet. The employee at Foot Locker took my side. 😁
[jdkbcgh] (score 54, diepte 0 OP) You can do this with other brands as well.
[jdkznfv] (score 49, diepte 0) This is me, buying the size 16 childrens' leggings at Target because they are significantly cheaper than the adult ones haha.
[jdl17kd] (score 42, diepte 0) This is a great tip but one thing to keep in mind is that kids shoes are not made to be nearly as durable. They are often made of a cheaper foam than their adult models that will break down/wear out quicker. So if you’re going to be wearing them all the time be frugal and invest in a pair that will last.
[jdmbgl9] (score 41, diepte 2) I need to look into this cause I have wide ass feet
[jdldpvf] (score 34, diepte 1) I try doing that but they’re just too short for my monkey arms 😩
[jdkly3p] (score 34, diepte 0) This topic comes up from time to time. Foot length isn't everything. 

I happen to be a perfect boys' size 6 but cannot wear standard women's shoes. My feet are extra wide and also have high arches. For dress shoes the only 
brand that fits are Naturalizer.

Don't damage your feet by trying to make do. Podiatry is expensive.
[jdma6iv] (score 32, diepte 3) EU shoe sizing makes SO MUCH more sense! My only issue is they rarely make half sizes, and my best fit is usually a 37.5, which doesn't exist (unless converted from US sizes).
[jdmc2an] (score 32, diepte 4) The first time I went shoe shopping with my husband before marriage he thought I was crazy when I walked into the men’s section and started looking for my size. Women’s size 8 is also a men’s size 6 so when they say “kids sizes” they mean men’s, it just so happens that “men’s sizes” start above 6
[jdkps8o] (score 32, diepte 1) I buy some men footwear too and l feel like it’s so well made and cheaper than the cheap women’s shoes. I bought amazing leather loafers in the slippers section for half the price of the glittery synthetic ones in the women’s section.
[jdmh2mf] (score 31, diepte 3) Try a men's! Subtract 2 from your size
[jdl4x52] (score 30, diepte 4) That explains it! I wish there was one universal shoe size chart for all ages, genders, and that could be used in every country
[jdm24n5] (score 29, diepte 5) There's another explanation for girls sports shoes being built worse than boys sports shoes?
[jdkit4g] (score 28, diepte 0) 😭😭😭😭 I'm a size 10.

And my 10yo now wears a ladies 7. I miss kids shoe prices!!!

Kids size is ladies minus 1.5 or 2. Depends on the brand of shoe and the width.
[jdl5vxi] (score 26, diepte 1) I’m also a size 4 and a 2 in kids. Totally agree on quality of kids shoes. I get the Uggs, flip flops and slippers from kids but buy the rest in size 4s from Nordstrom. The quality is a lot better!
[jdl0d21] (score 25, diepte 0) I don’t. Between the plantar fasciitis and the back pain, I’m all about those sweet orthotics, which strangely don’t come in child sizes.

You know that makes me crazy, though? There’s no reason flats can’t be supportive. Stop making me feel massive pain to be cute or formal, it’s mean.
[jdm7vth] (score 24, diepte 1) For extra petite women, clothes sizes for tweens is the best! Cheaper and no hemming needed. Just need to be careful to not look like a child.
[jdmghj0] (score 22, diepte 7) *looks at inferior quality basketball shoes for girls vs those made for boys*

Ah yes, it's because girls do ballet.
[jdmb90c] (score 22, diepte 1) My very small mom buys her bras in the teen section, she gets like 3 of them for $18, I'm lucky if I can get one for less than $45.
[jdklp90] (score 20, diepte 4) Ahhhhhh that would make more sense then!
[jdmbwjy] (score 20, diepte 7) Who knew we had differently style feet?
[jdmcoik] (score 20, diepte 6) I proceeded to pick an all white version of my size in each men’s and women, showed him the difference in how they were constructed and the price difference on top of that, and he was shook. Can’t blame him for not realizing a problem that never affected him before.
[jdmg2cf] (score 18, diepte 3) They more than likely are produced in the same factory or exactly the same way in a different factory. Also, "oh no, whatever will the professional sports players and team owners do without my money" why would anyone give a flying fuck about professional sports teams raking in more or less money? The owners will still be rich and the players will still be rich for about 3 years after retirement, some knock off jerseys aren't going to change that.
[jdmmsnc] (score 18, diepte 1) I’m a small man and I buy youth xl clothes all the time. Some of my best work pants are under armour youth xl golf pants. So good that I got another pair - two pairs for less than the price of one pair of small men’s of the same pants. I think the pockets hold a little bit less than what I’m used to but that might just be gold pants in general.
[jdkm11o] (score 18, diepte 0) Youth 4.5 here.  Nothing like getting Asics and Reeboks for 1/3 of what my friends pay!
[jdmmx9p] (score 18, diepte 2) she’s a little Oriental? wtf?
[jdl0bkh] (score 16, diepte 2) All the mens stuff is really well made. But you are right you can't get women's slippers like that without paying a fortune. Although I am pretty sure the running shoe companies make each shoe the same for men and women because its literally the same shoe in different colors and sometimes the same colors the mens sizes are just bigger than the womens for a lot of sizes there are crossover sizes and I believe the shoe is literally the exact same thing they just throw a mens size number on it vs a womens size number. There are even a bunch of brands that have a unisex size on them and a mens and womens size.

When buying on amazon the mens 9-10 is almost always less expensive than equivalent womens size, sometimes by a lot of money.

Children's shoes aren't made in the same way that adult shoes are and they do fall apart faster plus they have less support. Also the weight of an adult is usually not the weight of a child so you are putting more pressure on the shoes than they are designed for. Children's shoes are designed to be used for less than a year because the child will grow out of them by then but some people keep things like a pair of uggs forever.
[jdmhun2] (score 15, diepte 1) Yep. Kids are physically different both in development and weight. The durability of the shoe does not even have to be the same.  My sister will only do this with shoes like flip flops or Crocs.
[jdkk77k] (score 15, diepte 1) You wear a mens 7 which is easy to find on clearance
[jdl0t6k] (score 13, diepte 1) Pretty sure I had a size 9 womens when I was 10. I was also an early bloomer.

When I was a kid, kids sizes only went up to size 4, if you were bigger, it was on to either Men's or Women's sizes. God help it if you were a 4.5 because that didn't exist even at the specialty store. Now I've seen kids sizes in 6-7.
[jdl0xoq] (score 13, diepte 1) New balance makes many widths in different sizes even sizes you don't find normally.

Children's shoes are less supportive and built for smaller bodies in general. Yes people with smaller feet tend to have smaller bodies but if you are buying a child size 4 that's probably made for a 50lb child and even if you are a 100lb adult you are overloading that shoe with your weight. The shoe will most definitely wear faster and fall apart faster and it won't be good for your feet.

Children's shoes are also made to grow out of, and if you intend to wear them for a few years they just wont' hold up.
[jdkjxuf] (score 12, diepte 1 OP) I would if I could!! I see you like The Office, as well! It’s one of my favorite shows.
[jdlhbbk] (score 12, diepte 5) Yeah like Inches or Centimeters! Would make life so simple.
[jdl44cf] (score 12, diepte 1) The child size is in male and the adult size is female. (Subtract two for the female child’s size).
[jdlajz0] (score 11, diepte 0) This also applies to vans and chucks.  They’re usually about half the price in the kids section.  Just be prepared for a teen to tease you about having toddler straps on your shoes.
[jdmjcd4] (score 10, diepte 6) You're telling me my little boy wants to pay more for shoes than my little girl?
[jdmhc4i] (score 10, diepte 5) I have big feet (40/41 Euro, size 10 US) so I'm an ideal candidate for getting men's shoes. However, they don't seem to fit right, especially the back heel.  Even when the length and toe box are _perfect_, the backs of my feet aren't secure in the shoe, and it feels like the shoe is going to come off. It's uncomfortable.

Oh, and the arch is always off.
[jdl465f] (score 10, diepte 1) So, your 10 yo could wear a kids 5 no?
[jdlqxvk] (score 10, diepte 1) I have plantar fasciitis too. I just bought a pair of Naturalizer dressy sandals (they’re flat) for a wedding next weekend. I’ve only tried them on so far, and they’re awesome. My podiatrist recommended this brand for dress shoes. Look for the ones that list the Contour+ technology in the description. Expensive, but potentially worth it. I value comfort more than price. I used a coupon code through Microsoft Edge’s shopping tool, so that helps a bit. If you’d like, I can follow up after next weekend and let you know how it went.
[jdlwply] (score 9, diepte 1) but almost every pair of shoes is in sizes 5-8 in women's, I have such a hard time finding shoes in store for my clown feet (size 10)
[jdmk7mz] (score 9, diepte 6) There are ways to lace running shoes to mitigate heel slip. Google “heel lock lacing” or “runners knot.”
[jdm7pum] (score 9, diepte 0) This can definitely work. But, as a woman whose feet haven't grown since she was 12, it's more miss than hit. In my experience, shoes made for kids are less durable, lower quality, and it's almost impossible to find designs that aren't childish (colors, glitter, bows, butterflies, comic book characters etc). It was my only option for a while, though, and if you're on a tight budget it's definitely an option.
[jdmb0uv] (score 8, diepte 2) The quality is not just as good, these are made with cheap labor and cheaper materials. Some may be passable, but most of them are crap. 

You are also contributing to copy-write infringement and theft. These companies are ripping off logos and likenesses without license.
[jdmzad4] (score 8, diepte 2) Don't even need to be extra petite. I'm 5'6 (so technically above average even if I am short for my family) with an athletic build, and I often buy clothes from the kids/tweens sections. I also buy small shit from the men's section. Got some really nice cardigans on clearance from Men's Wearhouse, way better quality than women's at a fraction of the price.

Did hurt my feelings a bit when I bought a sports bra from the kids' department and it was too big.
[jdkjz1g] (score 8, diepte 0) Size 9, boooo.
[jdlg5ao] (score 8, diepte 1) I’m a women’s 11 and men’s sizes are too wide at the heel for me. Sometimes that’s all I have though.
[jdll816] (score 7, diepte 1) Just wish they didn't look so "kiddy" like Skechers.
[jdm62qf] (score 7, diepte 1) I do this too! I don't like how big adult jerseys are
[jdmbrov] (score 7, diepte 2) Really? As a 6-7 I've had the opposite problem, there's too many 8-10 and maybe two 7s, and one 6 if i'm especially lucky that day
[jdljlos] (score 7, diepte 2) It's really time shoe manufacturers made more women's sizing. I have a few friends who are over 6 feet tall who are women and struggle to find cute shoes in their size. I've also noticed shoe manufacturers making shoes smaller.

I used to be an 8 or 9, and now I am a 10. Yet my old shoes fit fine, even one's I hardly ever wear. It seems to be the cheaper brands that are the worst for this.
[jdm786a] (score 7, diepte 3) Feet do tend to spread out over time
[jdmp5da] (score 7, diepte 3) Yeah, Nike's tend to be narrow almost all the time.
[jdmm30n] (score 7, diepte 2) You married a small rug?
[jdkwssu] (score 7, diepte 0) Try them on in person, I can fit them but the ones I’ve tried on have felt comparatively cheap (to the same adult version) or uncomfortable because they lack support and are mostly just flat.
[jdlvqez] (score 6, diepte 1) I bought my converse high tops in a kid’s size. I don’t wear them every day, but they’ve held up for a few years now. Cheaper than adult sizes. Plus they’re a super fun pattern (dinosaurs lol) and always get tons of compliments.
[jdmllyi] (score 6, diepte 2) I have those same ones I think - always a huge hit when I wear them to work (I teach elementary school)!
[jdmci0q] (score 6, diepte 1) What size does an XL youth equate to in mens roughly?
[jdkvjyz] (score 6, diepte 2) Same! Total comfort show for me - it’s the best :)
[jdmbb11] (score 6, diepte 1) I used to buy my bathing suits and underwear in the kids section. Back when Body Glove was big, they cost about half as much. Also, I couldn't find character underwear in the ladies department. 😄
[jdn1uv4] (score 6, diepte 1) Have you tried the  American Doll store? You know if the t-shirts are too racy in the normal kid’s selection…
[jdmdqoc] (score 6, diepte 3) The kids sizes flow into men’s sizes rather than women’s. So youth 6 is equal to men’s 6 which is equal to women’s 8
[jdkier1] (score 6, diepte 0) Is this really really true??? I will be so happy if it is
[jdmy96i] (score 6, diepte 4) I don’t think men’s go smaller than a 7 and I wear a 5 in women’s 😩 but my feet are sooo wide
(275 reacties met lagere score weggelaten)

=== THREAD 1llr90i ===
SUBREDDIT: r/Frugal
DATUM: 2025-06-27  SCORE: 215  REACTIES: 347
TITEL: I’m very frugal and don’t like getting pedicures. I feel like they are a waste of money and can lead to infection. With that said, what’s the best way to remove dry skin around the feet? Hot water/salt soaks are not doing much for me.
POST (source_id=post):
I’m very frugal and don’t like getting pedicures. I feel like they are a waste of money and can lead to infection. With that said, what’s the best way to remove dry skin around the feet? I already do hot water/salt soaks but they are not doing much for me. I moisturize my feet too. But My feet are still hard, and dry. Particularly around the heel. What’s the most frugal, but also effective way to remove this dryness?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[n01no3w] (score 444, diepte 0) I am assuming you have tried pumice stone or similar tools after the soak?
[n02hv9u] (score 227, diepte 1) This seems to be the part of the foot soak they're missing. 

Soak + Pumice Stone + Foot Peel Masks + Moisturizer = baby soft feet
[n01p079] (score 211, diepte 0) This product called Baby Foot. You wear the booties for an hour, then for about a week it slowly sheds…I know, sounds gross. But it works, I have elephant like feet. Also, put petroleum jelly on your heels at night.
[n01t3ec] (score 146, diepte 1) Just don’t use it if you plan on wearing sandals in the next couple of weeks as your feet look ghastly until it’s done peeling!
[n01p36q] (score 131, diepte 0) They make a Urea cream with 40% concentration specifically for dry, callused feet.  There are a lot of affordable ones on the market under $20.
[n01ns30] (score 94, diepte 0) Kerasal! Use it every night for a week, then once a week thereafter. 

Also helps to keep an exfoliating paddle in the shower NOT a metal rasp, one that’s like a big emery board. It helps slough away softened dead skin without taking too much.
[n04pc6l] (score 63, diepte 3) Baby foot!!! $20, but it’s so effective. You’ll need to wear socks for at least a week, as your skin will complete shed like a snake.

Also highly recommend the “cheese grater”, aka the thing salons use for callous removers. Just be sure to clean it properly, etc to prevent infections.
[n01uo5q] (score 56, diepte 0) My wife literally bought a foot sander.  She puts sticky sandpaper circle on the end and she sands it away after a soak.  


Wild to me.  


I offered my orbital, she didn't find it funny.
[n024vdt] (score 52, diepte 2) I do one at the beginning of fall and another mid-spring, and give myself monthly pedicures as well to keep the crust at bay. My feet immediately start to rebuild calluses the minute I remove dead skin and require continual maintenance.
[n061cvh] (score 35, diepte 4) Also, you can use a single "glove" on just one foot, then when done switch to the other foot. Takes twice as long but you double the use!
[n01wdmh] (score 32, diepte 0) I am professional pedicure nail tech. 


You want to soak your feet on very warm water, and scrub with pumice stone. That's the official answer.


If it's like an inch thick, you might need a professional to whittle it down using a special blade.

But if you serious, use Sand paper. It's cheap, easily available, and works magic. I would start with 400 grit if you're able to handle that
[n01nu6j] (score 31, diepte 0) Foot peels. Target has a good one, or baby feet is another kind. They're my favorite!
[n028krb] (score 30, diepte 1) This. Urea in lotion is magic. I use the Eucerin advanced repair cream that has a lower concentration of urea, and my feet are baby smooth.
[n01ogzk] (score 28, diepte 0) Dollar Tree has pumice stones.
[n02519n] (score 27, diepte 4) I've used the Baby Foot brand foot mask half a dozen times without issue. The one time I used a random brand off Amazon, I got a chemical burn on the tops of my feet all the way up to ankles. Looked like I was wearing red socks. Do not recommend.
[n03e20b] (score 27, diepte 2) Urea is not urine
[n01wiz9] (score 26, diepte 3) There are much cheaper foot peels available on Amazon- they all do the same thing.
[n02fi9q] (score 24, diepte 4) I feel like chemical peels are something I'm not willing to go cheap on, particularly since there are so many fraudulent companies on Amazon that do things like sell counterfeit products and manipulate reviews.
[n02gil5] (score 22, diepte 3) This is my pattern as well - I do my best to maintain the rest of the time with exfoliation and at-home pedicures. But twice a year, I also do a foot mask/peel to do the heavy lifting.

And seconding what everyone is saying - be prepared for peeling feet for a couple weeks and plan accordingly!
[n02tabs] (score 20, diepte 4) Now I’m wondering is this that stupid pink tax or do men get a discount *just for being men?*
[n03jwqy] (score 19, diepte 2) Do you have any specific foot peel masks you recommend?
[n06dzm9] (score 19, diepte 5) Oh wow that’s clever! Like a double header of frugality haha. Thanks for the idea
[n03n5rz] (score 19, diepte 1) My husband used to use one of those. I actually convinced him to start getting pedicures and it's like night and day. His feet were really bad - plus he has diabetes and his feet crack. They are downright presentable now. He's really enjoying having pretty, soft feet.

Just to say: I think it can be worth splurging on the pedicure, if your feet really need it. Doesn't have to be every two weeks. But be good to your feet.

I don't want to be the one on frugal encouraging non-frugality. But I do think taking care of yourself, when you can, isn't a waste of money.
[n01nq23] (score 18, diepte 0) See a podiatrist to find the cause. 

If it is just how your feet are, use a pumice stone after you wash your feet.
[n023j32] (score 17, diepte 1) I use kerasal or petroleum jelly at night and then Saran Wrap my feet and put on heavy socks. It is GOAT at softening feet, I need to start doing it with my hands.
[n02n4qc] (score 17, diepte 3) You can use one on both feet. That's how I do it anyway. Takes more time, but saves a little money.
[n01uwuw] (score 17, diepte 1) This is *magic* and it works incredibly well. I was so grossed out, lol. I did one a few months ago and my feet are still pretty soft because I've been moisturizing.
[n05o1x1] (score 16, diepte 5) Eww to the dead skin all over your bedding, but it's your bed so you do you.
[n02r5lb] (score 16, diepte 4) I have found my people who understand! Haha
[n01rl20] (score 16, diepte 0) if your heal is really dry and hard, file /grate or use pumice on it dry where it is the hardest. get rid of whatever you can but don't go overboard if it becomes a bit sensitive stop.

then put on them oil/butter (olive or shae or coconut ....etc) or if you prefer lotion . let it sit. if you can put in these silicone coated socks or just put plastic bags.

then soak . in just water or with salt or epsom salt. wash your feet.

then scrub gently (loofah , scubbing glove)

do that several times maybe once a week and it should solve the issue.

one thing you must know is that better shoes will help .
[n05vpef] (score 15, diepte 7) I fucking live for peeling it off lol
[n05vg9z] (score 15, diepte 3) Ignore whatever brand. You just want one with Glycerin Acid in it. CVS/Walgreens usually have a few options, all way more affordable than whatever $20 option is being pushed by another commenter
[n02b67g] (score 15, diepte 2) lol no, it's odorless in its original state.
[n02s65p] (score 15, diepte 1) I second this.

My husband has rough feet due to his type 2 diabetes. One of the many doctors recommended urea cream with %20 and above concentration. We ordered a 40% one off amazon and I picked up a 20% one for myself.

Applied it for the first time yesterday and i can already see results 👍
[n01t2te] (score 15, diepte 0) Glycolic acid - squirt on toes and places calluses form after every shower.  Then all other ideas on weekly slough offs.  I still get pedis for ingrowns but can stretch time between this way.
[n05obi8] (score 14, diepte 6) It peels in sheets, really, and I’m a picker. You reckon that a) I’m getting in with loose skin anyway and b) everyone isn’t already shedding in their beds? 

You know what dust is made of, right?
[n02o22c] (score 14, diepte 2) This sounds amazing but I can’t sleep in socks
[n02icn4] (score 14, diepte 3) The men’s version is a few bucks cheaper
[n01soyl] (score 13, diepte 0) I get a pedicure every few months. I just get the basic with gel polish. They're pretty economical if you cut out the extras like hot towel wraps that will burn the heck out of you and the leg massage. I pay for the gel polish because I know I won't be back for a while.


I also trim my toenails before I go and tell them not to cut at all. They can scrape and file the nails.


So basically I get a foot bath where they file my nails, trim the skin from around the nails, scrub the bottoms, and paint.
[n01u50w] (score 12, diepte 2) Very true!!! Also, it is $25, so not the cheapest option. It is a low-work option without lots of scrubbing.
[n025ddd] (score 12, diepte 5) I’ve used many other brands without issue, including the cheap Amazon ones. You may have an allergy to an ingredient in some, but I wouldn’t say that everyone will have the issue you had.
[n01rk5f] (score 11, diepte 1) Thats my advice, exactly! (See above...mine is just more wordy). I use a greasy stick thing that has salicylic acid and put silicone heel wraps on at night. The paddle thing is the best! I put a link in my post
[n031ye5] (score 10, diepte 6) That first part is actually so real though. 😆 I’ll be like “oh no, my feet are a little rough,” and my husband has to be, “these cracks are half an inch deep now, should I do something? I’m probably fine.”
[n02wc0v] (score 10, diepte 3) There's a discount version at the Dollar Tree. Doesn't work quite as well, but for $1.25 you can afford to do it more often.
[n01w42r] (score 10, diepte 0) I’ve found pumice stones to be meh. I bought a nano glass foot file thing and it’s honestly so good. I use that and amlactin on my feet. They look great.
[n04gt8k] (score 9, diepte 1) Pumice NEVER worked for me. I think it might work for people who don't suffer as much dry skin as I do.
[n028lwk] (score 9, diepte 2) Not at all.
[n01w4fo] (score 9, diepte 0) If you don’t want to go to get a pedicure, perhaps get a treatment at a podiatrist. My feet feel baby soft after I’ve had a treatment, they have all the tools to make your feet amazingly soft and healthy. Plus all guaranteed sterile and medical grade instruments. No polish of course.
[n022h9q] (score 9, diepte 0) I work with podiatrists and they suggest no more than a gentle pumice stone at the end of your shower- follow it up with some lotion. Cut your nails following the nail bed (so the shape of each nail may be different). Never cut your cuticles, just push them back if they bother you.
[n02bh9d] (score 9, diepte 0) Try lotioning your feet at night after a warm shower and wear socks to keep the lotion on. Should help quite a bit
[n05wejp] (score 8, diepte 7) Peeling is the best part. I'm probably not doing myself any favors though, because sometimes i peel off a piece of actual skin. Hurts like a mofo!
[n04fu3v] (score 8, diepte 1) Urea is insanely effective.
[n01pawf] (score 8, diepte 0) Pumice stone does nothing for me. I Korean food peels from TJ Maxx and it (all my built up skin) comes off within a couple days. 5-6$ for a three pack, fresh skin without all the work. Then you can use a moisturizer routine to maintain.
[n0217zt] (score 8, diepte 1) I got one -- it is great.
[n05vv45] (score 7, diepte 8) Says we can’t, but I do what I want 😂
[n02v38o] (score 7, diepte 3) You can spread Vaseline or Vicks Vapo Rub on your heels and wrap your feet in cellophane and then put socks over that during the day for a few hours. I usually do about 4 hours minimum. Walk carefully!
[n02a5zz] (score 7, diepte 3) I've used a couple other cheaper options from Amazon, but they do not work quite as well as Baby Foot.
[n02y1ry] (score 7, diepte 5) may just be harsher because they know our feet have to be REAL bad for us to care lol

orrrrrr the pink tax.
[n027ehj] (score 7, diepte 0) Lol the judgment and ignorance is completely unnecessary. Nobody cares if you dont get a pedicure and professionals are in business giving out infections so stop being an ass.

Stop salting your feet 🙄 you obviously need to hydrate. Most people use lotion. An oil soak helps. If you've really fucked them up some people have to have surgery to remove callus cores.
[n02xbrc] (score 7, diepte 0) Honestly, I inherited extremely dry and rough heels from my mom. (Seriously, I kind of wish I had a picture of my mom's feet and how bad they were). The only way I have found to keep them under control is a pedicure a couple of times a year. 

Also bare feet = dry feet. I keep socks on almost all the time. 

I found I was spending a lot of money trying to find some product to solve this issue when none of them came close to the effectiveness of a pedicure every 4-5 months.
[n01noo4] (score 6, diepte 0) If you have good health insurance you can see a podiatrist regularly.
[n036orw] (score 6, diepte 1) Use the exfoliating paddle on dry feet, not wet, then morturize a lot.
[n01oivl] (score 6, diepte 0) I’m a hill billy. But the best tool is a random orbit sander with like 80 grit. It is actually very gentle. But fast. I do that maybe 1 time a month on the really heavy calluses. Then after shower put on aquafor and socks. 99% better with only 5 min of effort.
[n027rvs] (score 6, diepte 1) I didn't think they nickle and died these. The leg massage is always a nice surprise lol
[n04hi45] (score 6, diepte 2) The Ordinary's glycolic acid is perfect for this.
[n02dww5] (score 6, diepte 0) I use an orbital sander. It sounds super scary, but takes about a minute per foot and one sanding circle lasts a year or so. I have separate sanding circles for my feet and my projects. Not for everyone, I’m sure, but I tried everything else (gels, ‘cheese grater’ things, pumice, hot wax in baggies etc.). After sanding, I slap on some cutemol or vaniply and some socks for an hour or so.
[n02isa5] (score 6, diepte 0) This started as a tactic to declutter all the lotions I ended up with under the bathroom sink that I didn't really like but also couldn't just justify throwing away. I just lotion my feet with whatever lotion is available every single night before bed. It's very easy, and they have never been so soft.
[n03yyo6] (score 6, diepte 1) There have been a few cases of salons not properly sanitizing tools. It isn’t common, and it doesn’t happen in places that follow the proper procedures.
[n04zrck] (score 5, diepte 4) I don’t bother wearing socks after it, too hot here for that nonsense, still works great.
[n03o9el] (score 5, diepte 3) same! these foot peel masks have been a lifesaver!
[n03euzc] (score 5, diepte 1) Walmart sells a Korean version of Baby Foot and it's $2.50 a pair and it worked very well. Highly recommend, though you WILL peel for the 2 weeks after. Make sure you moisturize and wear socks
[n03uv9w] (score 5, diepte 3) I know it comes out of my bearded dragon's butt though
[n01r77d] (score 5, diepte 0) Urea foot cream and socks at night. Use an exfoliating mitt/cloth like a Korean exfoliating washcloth (also known as an “Italy Towel”) to scrub your feet in the shower/bath/after a soak. It’ll all come off over time and it’s probably $20 for both the cream and the cloth which will last you ages.
[n03220g] (score 5, diepte 1) I have one made by Scholls, the shoe insert company. It works amazing after a shower
[n050ziv] (score 5, diepte 2) If he is diabetic, his insurance may cover dry pedicures and nail trims at a podiatrist office
[n02heqx] (score 5, diepte 1) Maybe don’t use racist stereotypes? And learn to spell.
[n01zn6t] (score 5, diepte 1) Even with socks my skin gets dry especially during winter consider yourself lucky.
[n02buts] (score 5, diepte 1) Lmao that was my thought too. This is a post in a sub called “frugal”. OP could have posted this without the first two sentences and probably no one here would have recommended getting a pedicure, like one of the most non-frugal things someone could chose to do for their feet 😂
[n02bss3] (score 5, diepte 0) I use a stainless steel foot rasp. Earth therapeutics for 8.99 I think. It doubles as a grater for felsnaptha in the laundry room.
[n02xyro] (score 4, diepte 1) Yeah. OP might also look up athletes foot. There are creams for it, Costco was about 5 bucks for two tubes to treat it.
(325 reacties met lagere score weggelaten)

=== THREAD 1ajptgq ===
SUBREDDIT: r/Frugal
DATUM: 2024-02-05  SCORE: 164  REACTIES: 347
TITEL: Are Hoka shoes worth it?
POST (source_id=post):
I work a manual job on concrete. So that means I have to buy new shoes every 3 ish months otherwise my knees hurt. I buy new shoes on clearance for 20 to 30 usd or 80 to 120 USD a year. But Hoka shoes cost about 150 on average so to be worth it they would have to last me over a year. Are they any good?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kp2mqov] (score 443, diepte 0) Shoes are something worth the cost, especially if you're on your feet all day. As to whether they are good for your job I can't say, but as a general rule you don't skimp on good shoes.

Go to a local running store if you can and try some on, they'll let you walk/run/etc and see how they feel.
[kp2oenx] (score 144, diepte 0) maybe you need shoe pads instead?
[kp2x5jg] (score 117, diepte 1) I second going to a running store. I really thought I wanted a pair of Hokas until I actually tried some on. I know they are super comfortable to some, however, I needed something with more cushion.
[kp3loik] (score 84, diepte 2) More cushion than Hoka?

Does such a thing exist?
[kp2nia5] (score 67, diepte 0) What work do you do.    There are tennis shoes and work shoes and boots.   I would get some true workboats with good support.   If I am on concrete all day.   I have a good pair of hiking boots with Vibram soles that I can go anywhere in.
[kp2qpdd] (score 53, diepte 1) This should be higher. Good shoe pads improve comfort by 20-30% easily (don't quote me on the numbers) for less than $20
[kp3o4d1] (score 51, diepte 2) I second this - I tried on Hokas and the arch support hit my foot in a weird place, so I didn’t get them. I went with Brooks instead.
[kp2noul] (score 34, diepte 0) Good work boots with orthotic insoles ($25) that you replace regularly are a better bet 
I’m partial to Carolina boots and my coworker swears by Georgia boots. They last us about a year or more, would last longer if not exposed to water all the time but that’s life.
[kp2p9gd] (score 34, diepte 0) I love mine, and my podiatrist wears them also. If you wear them every day, it is wise to change them and get new ones for six months after wearing every day as per my podiatrist otherwise for occasions, they can last quite a long time.
[kp2q9de] (score 27, diepte 0) My advice is to buy the previous year versions when they go on sale or clearance. Many in my circle swear by Hokas. I don’t wear them, but I always buy my sneakers once the newest models come out - because they discount previous models drastically. Which makes me laugh - like shoes - who would’ve thought people are in line for the newest versions as if the technology has improved in 3 months. Anyway, perhaps even buy multiple pairs then to spread out across your year since you’re on your feet so much.
[kp2q56w] (score 26, diepte 0) Hoka shoes are very comfortable and cushioned. For runners, the suggested time for replacement is 300-500 miles 

I usually get new shoes 2x a year. It’s worth the money to keep my knees and hips healthy. 

Also, I usually get mine on Black Friday. They are usually last season’s shoe, but I’ve bought new $150 shoes for $60 on Black Friday.
[kp47vma] (score 23, diepte 3) My hubby can only do Hokas. He has a strange gait, and the Hokas keep him from doing it. When he did Brooks, they made his toes numb. Lol.

You can always buy from REI. They have a generous return policy.
[kp391x8] (score 19, diepte 3) I think it's very hard to generalize this. Maybe the quality is bad and they'll wear out soon but the fit and comfort are very personal. What fits for me could give you back problems, and vice versa. A few years ago I bought random insoles from target for $15 and they were great for running for me, and lasted over a year.
[kp3psrg] (score 18, diepte 3) Haha yes! I have really jacked up feet (along with everything else)...I ended up with Nike Zoom X Invincible Run 3 shoes (just copying the name off of the actual shoes so not sure otherwise but Google should be able to help). The guy at the running store suggested them and they are AMAZING (of course this is a whole YMMV situation)
[kp368ve] (score 18, diepte 1) To build off this, find a store that will "scan" your feet.   That'll tell you a lot about the smaller details of the shoe you need to look at.
[kp40o7y] (score 17, diepte 3) All the running shoes have varied levels of cushion and support throughout their models.  Hoka's tend to aggressively rock forward and have a larger drop (distance between heel and toe) than a lot of others.  I personally prefer Brooks.
[kp2pk3y] (score 17, diepte 0) Hokas didn't work for me and my feet are still in pain after 9 hours of standing in one spot. Your results may vary. :'(
[kp2wtpw] (score 16, diepte 0) Personally, I think that Hoka sneakers are too cushioned to last but YMMV. Their recovery shoes though? Worth every penny. 10/10 will buy again but don't expect to need to anytime soon.
[kp2qfvb] (score 15, diepte 1) Even better when you use multiple ones and change every now and then.
[kp2s22b] (score 14, diepte 1) Agreed!! I do barefoot shoes BUT i do use a pair of FP Soles sometimes ($20 for the king foam ones that I use) and they’re great! 

For even more support (but more expensive) I loved my Super Feet soles when I was doing retail and standing all day, true game changer! Those non-slip shoes went from exhausting to comforting once I added those Super Feet soles
[kp3iuqf] (score 14, diepte 1) Standing still is actually more taxing on your legs than walking. I used a standing forklift for a job, and it was awful because you had to stand still in one spot. The relief when I could finally get out and walk around was amazing. I'm not sure any shoe could really counteract this. Were you able to find anything that worked?
[kp4invt] (score 12, diepte 4) In the Nordstrom Rack website..Hokas are cheaper. Return policy is pretty good as well. You can also return it, to any physical Nordstrom store.
[kp2srmc] (score 12, diepte 0) I usually buy $60 ASICS as walking shoes. I stole a pair of Hokas from my mom, and all future walking shoes I buy will be Hokas. Mine are trail runners, and I could go for hours without my feet hurting. I’m super cheap, but I fricken love this brand.
[kp4b53z] (score 11, diepte 4) In my experience, Hokas have more long term cushion that's more sturdy, if that makes sense. You don't instantly feel it but it lasts.
[kp3sd05] (score 11, diepte 2) Do we get commission after they upload them online? Or is that priced in?
[kp30gpr] (score 11, diepte 1) I agree.  I have a pair of Ariat waterproof boots that have lasted me longer than any other pair.  Like all quality items, they have a higher cost up front but they are easily the comfiest boots I’ve ever had.  They come in Wide which is essential for me and hard to find in women’s shoes.
[kp3a289] (score 11, diepte 2) I totally endorse Super Feet insoles. I used to have prescription orthotics, now i use SF in every pair of shoes. 

I have converted a couple of coworkers, too. One woman (mid 20s) had terrible caved in ankles - it hurt me just to watch her walk. I asked her if her feet bothered her, and recommended SF. The change in her foot posture was astonishing! She was very happy and her feet were too.
[kp3j37z] (score 10, diepte 2) I change shoes and socks at lunch.


During break I use the spikey roller ball.


It helps but not 100% gone.
[kp3k13e] (score 9, diepte 2) I rotate shoes in general. I have arthritis. So maybe try something like that. I keep 3 pairs of shoes in my vehicle 🤪
[kp3p2g0] (score 9, diepte 2) Get two pairs so they can air out. I just learned that sweat can break down glue.
[kp3h5bx] (score 9, diepte 1) >It’s worth the money to keep my knees and hips healthy.

A repaired or new one of any of those costs more than you'll ever spend on shoes.
[kp3uazs] (score 8, diepte 3) I love both these brands. I’m eager to try On clouds next.
[kp4ky1q] (score 8, diepte 5) REI gives you a full year to return them. Lol. We returned a pair after 4 months because they broke down faster than we expected (we expect about 9 out of a pair of Hokas for my hubby). Also the Brooks were about two months old when we exchanged them for full value. And the only ever seem to have black at our REI, which sucks because my hubby loves obnoxious colored shoes. 🤣🤣🤣
[kp2xc6m] (score 8, diepte 0) I love Hoka Bondi’s, best work shoe I’ve ever had that wasn’t a Red Wing Heritage boot. Your older self will thank you if you quit buying cheap shoes and start buying good ones.
[kp304t3] (score 8, diepte 0) I'm a marathoner with a history of genetic knee issues.

I ***swear*** by my Hokas. The Bondi are my go-to's for race day.
[kp31f6i] (score 7, diepte 2) Any of the major brand insoles that are less than $40-60 are probably not good. Dr. Scholls etc are terrible for you
[kp49hyc] (score 7, diepte 2) Do you alternate between 2 pairs of shoes so you're not wearing the same pair every day? Shoes need time to breathe between wears to last longer....
[kp2ulyh] (score 7, diepte 0) HOKA shoes are _absolutely_ worth it BUT you don't have to pay $150 for them!  Last year's models are often available for much less.

I made a [site where you can compare prices on running shoes](https://runningshoescore.com), including searching by brand.  Looks like right now, for example, you can pick up the [HOKA Rincon for under $100](https://runningshoescore.com/products/mens-hoka-rincon-3), for example.

The Bondis are some of the best for long work-day shoes, but unfortunately I don't see any on sale right now - you can set an alert and get notified if the price drops.
[kp34hiw] (score 6, diepte 2) Try on cloud or cloud on brand ones. They seemed good too.
[kp3u6u1] (score 6, diepte 3) How long do they last?
[kp2vatw] (score 6, diepte 1) I don't think he's pouring concrete; rather it's just the surface he's standing on all day while doing his job.
[kp60orw] (score 5, diepte 4) I like my Hokas for the cushioning but my Brooks seem to work better for my feet/stride. I second going to a shoe store and asking a specialist.
[kp39zin] (score 5, diepte 1) I've been wearing Merrell Moab shoes with Vibram soles and they've been very good for my feet. My wife broke her heel and the doc recommended Hoka as something that she could wear while she was healing. She swears by them and the cushioning looks great, but I don't know how long they'd last with rigorous wear. The Merrells feel good and last me a long time. I buy the Merrells when they go on sale, but Hokas are so hot right now, you don't see many sales.
[kp3j89l] (score 5, diepte 2) I got my boys Hoka and they are a great shoe and soft.   They are probably the best overall shoe out there because of cushion.    Lasting for average use, not running, and wearing every day they have lasted my kids 1.5 years.     We are going back to New Balance 1540 in our family because of more support for over pronate feet.
[kp2nmuh] (score 5, diepte 0) Maybe try some of the new balance shoes on sale in their outlet website joe's ? 

They are well made like hoka but not so expensive.
[kp4c87h] (score 5, diepte 3) The custom fit Dr. Scholls worked better for me than my $300 prescription orthotics. I’m talking about the ones that you buy after standing on a machine at Walmart that maps your foot.
[kp3oamb] (score 5, diepte 2) For real, my out-of-pocket maximum is like $6,700. That's a lot of shoes!!
[kp2teu9] (score 5, diepte 0) ASICS and brooks are a good cheaper alternative to hokas. They are comfy and will support you're feet just the same.
[kp2u03a] (score 5, diepte 0) If there’s a fleet feet or other specialty running shoe store they should be able to measure your foot and arch for free and give you some options based on your measurements and needs. May want to consider investing in some physical therapy to strengthen any joints that get beat up in your job as well since it could pay off long term.
[kp2uc99] (score 5, diepte 0) 1St I'm going to say that Hoka shoes are pretty amazing. I've been walking on a treadmill 5-6 days a week for about a year and the hiking shoes I've been wearing were always kinda hard even with $25 insoles.

I found a pair of Hoka at a local liquidation place for $70 and I can walk longer and further wearing them without any fatigue to the bottom of my feet.

Would I pay 140 for them next time. Yes probably.
[kp5k84r] (score 4, diepte 2) How is that relevant? I can’t imagine you’ve been wearing them to work on a concrete surface for 27 years.
[kp67jiv] (score 4, diepte 3) If you like Hokas - On is a step below. I’ve tried them twice because I like the style but went back to Hoka both times. Now I even have Hoka slides for my tile floors and Pilates. Love them as well
[kp39b2g] (score 4, diepte 1 OP) Damn so there is nothing I can do about needing to change shoes? I guess the way I do it is cheapest so I'll just stick to that.
[kp43vj6] (score 4, diepte 1) Would you happen to know where your friends get their discounted Hokas?
[kp2wizt] (score 4, diepte 0) I am a long time, long distance runner with horrible feet. It was the genetic luck of the draw. Didn’t stop me from running though! But I have learned a thing or two about shoes….
Hokas are absolutely worth it. My toes give them 12/10. However, wearing them for a year is not a good idea. ‘Getting your monies worth’ is going to impact your knees and body.
The best thing you can do with a limited budget is what you are already doing- rotating shoes out more regularly. For me, that’s 500 miles max.
Don’t buy the $20-30 ones. But you don’t have to buy the $150 ones. Go to a discount sports store and ask someone that works there for assistance. Take your time trying on pairs.
Also, invest in a pair of Super Feet insoles.
[kp2wrlt] (score 4, diepte 0) I love buying my shoes in used/like-new condition from eBay or poshmark. A quick search shows that there’s some Hoka’s available for as low as $30-$40 after shipping

I’ve never tried Hoka’s but I buy Vivobarefoot shoes this way and those retail for like $170 so I understand the pursuit 😭 

I usually buy it and try it from Amazon, return it for free, then buy it again cheaper from one of the sites I mentioned.

As someone else mentioned I also highly recommend you get inserts, perhaps even before you try new shoes.

For you I’d recommend the “super feet” brand in the green, orange or “berry” color. Each color is a different model and not every model is compatible with running shoes. The ones I’ve mentioned retail $50-$60 but you can find them for like half-off on eBay, and i recommended those particular styles because they have plastic on the bottom that stabilizes your foot, I wore them with steel toe boots and they help SO much with the fatigue. You can find these on Amazon, REI, dick’s sporting goods etc if you want to try them before committing.
[kp466gj] (score 3, diepte 5) Plus if you can find something that fits your foot... Something is better than nothing. And a cheap gel insole that takes up nearly the correct volume may last longer than a more expensive foam "fit to feet" type insole. 

Short of getting a bespoke fitted orthotic, I'm not convinced there's that much difference in the off the shelf offerings. Sure, mo money mo better, but there's gray areas.
[kp433z9] (score 3, diepte 4) Years. I haven't thrown out one pair yet, and I've been using them at least 10 years.
[kp38rc2] (score 3, diepte 1 OP) I've tried that, it only extends the life of the shoe by one month at best. The ones I buy are about 10 so it's not really worth it.
[kp2pcgm] (score 3, diepte 0) As another person said, get good insoles. It'll add an extra layer of padding to your feet. I personally use Keen ones, the thickness kind they have. And also good socks.
[kp2pgv0] (score 3, diepte 0) They're worth it if you have broad feet  and need a lot of arch support. They're really popular with overweight/fat people like my dad and sister. My mom and I are skinny and have narrow feet, so I'm really limited to specific asics or Nikes like the Pegasus.
[kp44pxi] (score 3, diepte 1) The pain was somehow worse after switching to Hokas. I would do all kinds of mini stretches and calisthenics to make it through a regular shift at the hotel I worked at. Pop an anti-inflammatory, soak my feet, roller ball and manual foot massage with cannabis balm when I came home. Anti-friction balm and compression socks were a must any day I had to work.
[kp3upw1] (score 3, diepte 3) American health care is fucked up.
[kp3cbt1] (score 3, diepte 2) I gotcha re read post I thought it was in concrete lol
[kp2xq5i] (score 3, diepte 0) Don't go with a brand for brand sake - go to a store and try on as many shoes as you can. Go with what's most comfortable and durable. 

I personally love Xero Shoes, and detest Hoka's. Other people are the other way around. Only way to find out is to try them all!
[kp2xscr] (score 3, diepte 0) Theyre all the rage on the Appalachian trail, if that tells you anything!
[kp2z6p6] (score 3, diepte 0) Yes. I only get Hokas for running. After I get too many miles on them, I delegate them to my everyday shoes and get a new pair for running.
[kp31qlk] (score 3, diepte 0) Also putting in a rec for Brooks ghost series, these aren't the snappiest runners but are meant as a low and slow daily runner. The sole of mine are just fine after 500+ miles
[kp33dxc] (score 3, diepte 0) I absolutely love my Hokas, they are super comfortable even when I’m on my feet for long periods at a time. I have the Clifton 9 and they are worth every penny.
[kp34syi] (score 3, diepte 0) Hokas go on sale for $80-100 through Woot, Dicks Sporting Goods, and even Amazon. If you want a pair wait for a sale dont buy them at $150
[kp37d0h] (score 3, diepte 0) Shoes For Crews.
[kp3qram] (score 3, diepte 0) If you're in the US, there's a website called "Woot" that routinely has Hokas and higher end Asics (better than Hoka to me) for %20-%50 off. You do have to sign up for their emails to get notified of the new sales, as inventory changes constantly, not just when an item sells out. I just got a pair of $150 Asics for $100. Still the most expensive tennis shoes I've bought, but I thought it was justified because it was a great deal AND my knees have been getting creaky lately.
[kp68b4o] (score 2, diepte 4) Good to know. Thank You.
[kp3otct] (score 2, diepte 2) My Ariats with the steel shank lasted me over five years! And they looked good.
[kp2nsl2] (score 2, diepte 0) Shouldnt the company reimburse or provide you with the shoes? Look into that first
[kp39dwp] (score 2, diepte 4) My more expensive ones actually wear out quicker than my cheapies ever did. Compare a pair of superfeet or something like that to dr. Scholls and they are night and day
[kp2or7h] (score 2, diepte 0) My Hokas don't last a year, but they are the one pain-free option for me (and I'm harder on shoes than most people). I think all running shoes have a lifespan, and I'm not sure the top-level Brooks, Hoka, etc., necessarily have a longer lifespan. One thing you might want to consider is whether some kind of orthotic like a PowerStep might help your shoes last longer. Also, Hokas (and other shoes) come in many different styles for different feet types - so just buying the one on sale may not always get you to the best option. If you have a local running store I'd go there and explain your question and budget and find out their ideas.
[kp2otoe] (score 2, diepte 0) Yes they are worth it. I have a few pairs and work in landscape, walk a lot and they are great! Make sure to get an insole for greater comfort! Good luck
(287 reacties met lagere score weggelaten)

