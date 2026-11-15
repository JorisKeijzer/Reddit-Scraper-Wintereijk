# Label-batch batch_0050

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
Schrijf het resultaat naar `batch_0050.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1mbz6ko, 1bl7wu1, spa8c9).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1mbz6ko ===
SUBREDDIT: r/BuyItForLife
DATUM: 2025-07-29  SCORE: 75  REACTIES: 111
TITEL: Recommendations for 10-15k daily steps walking shoes?
POST (source_id=post):
I started a job recently training service dogs, and we walk about 10-15k steps per day. The company gives us a $100 stipend to buy walking shoes. I’m normally just in Chucks day-to-day but I’m interested in buying something that isn’t just going to get worn out and thrown away. I have flat feet from a foot surgery, and most “walking shoes” have so much excessive arch support it kills me. I want something with cushion, or that will mold to my feet, but with low arches. I’m looking into RedWing Chelseas maybe? I like that they slip on because we have to change shoes during the day and I don’t want to mess with a ton of laces. I just don’t know if the kinds of shoes I’m looking at are good for lots of daily urban walking. Anyone have any recommendations please?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[n5q1uxc] (score 189, diepte 0) Go to a running store.  They will check your gait and arches, then recommend a few shoes for you.
[n5pzuw0] (score 107, diepte 0) Can’t go wrong with HOKA or Brooks. Expensive but worth it imo.
[n5q1rpy] (score 50, diepte 1) Hokas are comfortable but their outsoles are extremely soft.  They wear out twice as quickly as the other running shoe brands
[n5qbhnk] (score 39, diepte 1) OP, this right here is the best advice you’re gonna get here besides “shoes aren’t BIFL, especially running/athletic shoes.” 

People can tell you what worked for them, but you won’t know what’s going to work for you until your feet have been analyzed! It also helps to have a pro explain how they should fit, because they don’t all wear the same by design (ie. an “open toe box” shoe is going to feel like it’s too big if you’re used to cross trainers.) In my experience basically everyone that works at a running shoe store is at least mildly obsessive about shoes and will hook you up!
[n5q54l4] (score 23, diepte 1) This. Makes all the difference.
[n5q08oo] (score 22, diepte 0) I like my asics gel kayano 31s
[n5q2lbi] (score 18, diepte 0) I work in an environment we’re folks are on their feet all day. 95% of the footwear is Brooks and Hoka. 

I’ve worn Brooks for years. They’re not BFL but they’re about the best you’ll get. I put mine in the washing machine when they get dirty. I replace them when the outsole is nearly worn smooth (6 months). 

I can easily do 15k steps a day in them and my feet don’t hurt. 

As others have said, go to a running store and get fit.
[n5qaqgz] (score 15, diepte 1) I have severe plantar fasciitis and my Brooks have saved me so much pain. I was a little wary of dropping $150 or whatever on shoes but absolutely worth it. Love mine so much.
[n5qbl5p] (score 14, diepte 2) I buy the brooks ghosts for ~$90 when they go in clearance at the end of the season before the new model releases. Ghosts aren't the trendiest but they've been coming out with much better colorways lately and they've saved my feet!
[n5q34tz] (score 14, diepte 0) You want flat, go Lems or some other barefoot shoe. They have almost 0 arch support. I have the Lems Primal 3s and just did 12 miles with them today. Have had them for a year and they still look brand new.
[n5q6n6y] (score 14, diepte 0) Altra if you want a zero drop and wide toe box. I have beat up several pairs (Lone Peaks for trail and Escalante for pavement) and they last a really long time for me.
[n5qbeec] (score 13, diepte 2) I walk around 12k-14k daily and this is definitely true. My Clifton 8s wore down super fast compared to my old Asics. I barely got 300 miles out of them before the tread was completely smooth. Super comfy, but I definitely have to replace them more often.
[n5q7lac] (score 13, diepte 1) Brooks!
[n5q71p0] (score 9, diepte 0) I’ve switch from Brooks to Altras. The wide toe box is awesome, especially for my wide feet and the outsoles are more durable than a HOKA. Definitely recommend!
[n5q83zf] (score 8, diepte 2) Wearing Brooks Glycerin Stealths right now. Probably best shoes I’ve ever had.
[n5q48jp] (score 8, diepte 0) New balance 990s
[n5qstqs] (score 7, diepte 1) I'm a dog walker, it's not unusual for me to hit 5-10 miles a day. I jave tried Hokas, several pairs. They're awful. The only pair I'm keeping are their recovery ones, the rest make my feet, knees, and hips hurt. I'm more comfortable wearing Keds than I am in Hokas, which is frankly ridiculous 

Personally I'd go with something that has more room in the toe box, so your feet can better expand and flex like they would if you were barefoot. It will be better long term. If you have a good cobbler in your area, I'd get a pair of Birkenstocks and then get them resoled as needed
[n5tmm8s] (score 7, diepte 1) As a runner, pay full price at a store that allow return on USED shoes within 30 days. Those recommendations are kind of blah... taking shoes out for spin for 30 miles... you feet will tell you which ones you want to get.
[n5q3obl] (score 7, diepte 0) Go to a running store and try some on. I’ve tried brooks and hoka. ASICS work the best for me. I’m an avid walker who averages 12-15k steps a day.
[n5qa40j] (score 7, diepte 0) New Balance 990 v6. As cushioning, more supportive and more durable than Hoka from my experience with both. Also more versatile outfit wise. I burned through my two pairs of Hokas way too quickly. Hoka and Brooks are super over rate imo. I’m also a big fan of Karhu’s running shoes specially their Ikoni trail runner but found them to be less durable than NB 990s.
[n5qc2lp] (score 6, diepte 2) Agreed- but if you buy on their website they have a great warranty/ refund policy
[n5qizem] (score 5, diepte 2) I went through my pairs of Hokas so fast, outsoles lasted 3 months of about 10K steps per day. 

Both of pairs also tore quite easily around the toes once in their lawn care retirement home. They were both purchase, main shoe, yard work show and in the trash in under 6 months. 

Comfy but definitely not good if you care about longevity.
[n5qyyn8] (score 5, diepte 1) The running store nearby recommended me the Brooks Ghost 15 when I asked for the right shoes for my Japan trip, 25000 steps a day mostly walking in the city. They are amazing, especially compared to all other pairs I own. Light, well-cushioned and supported. Would definitely buy again, if they weren't still good.
[n5rmkn5] (score 5, diepte 1) Also ask about insoles
[n5qan3d] (score 5, diepte 1) Came here to suggest Lems too. Right around $100 so within stipend range. Flat arches, wide toe box, breathable, look good, good sole grip. No complaints for using them as a work show!
[n5qahgs] (score 4, diepte 1) I agree with Brooks! Hoka’s hurt my feet
[n5q08c9] (score 4, diepte 0) I have the (Red Wing 3141 Heritage Chukka)[https://www.redwingshoes.com/heritage/mens/work-chukka-03141.html]. They are 8-9 years old and one of my favorite pair of boots. I barely take care of them and they handle anything I throw at them that you can find on city streets (NYC and Chicago). I’ve also taken them to Paris and walked all over it. 

The thing I’d be worried about is wearing them every day for this use. They need breaks and time to rest or they will just wear out faster. A decent pair of sneakers (I’ve done Hoka, Saucony and Brooks) will get you about 6 months with 10-15k a day. Adidas with the continental rubber outsole may get you another month or two. 

But two pairs of sneakers per year (or rotating two pairs) might weather a little better than putting all those miles on the same boots every day all year with few breaks.
[n5q93vy] (score 3, diepte 2) Ya love em or ya hate em
[n5s8mjg] (score 3, diepte 3) I think those are the same I’ve got. Do they have the big, chunky, cushiony goodness on the bottom? I feel taller when I wear them lol
[n5quu7h] (score 3, diepte 1) New Balance 530’s would be my choice. I’ve had mine over a year, wear them every day, and they’re still in great condition.
[n5rz99l] (score 3, diepte 1) I got “fitted” at a new balance store once and I’ve had those shoes for almost 2 years now and still my most comfy shoe. Worth the $160
[n5q4375] (score 3, diepte 0) I can’t work with steps as a unit of measurement because it’s different for everyone.  How many miles or km is that for you?

I’m currently wearing Brooks Ghost running shoes. They are incredibly comfortable to me, not only due to the cushioning, but also because they have the widest toe box of any shoe I’ve worn. I average 3 miles per day but some days up to 5 miles. 

Tread and support break down over time in all athletic shoes, so there is no such thing as BIFL in this category. Brooks recommends replacing theirs every 500 miles, but I wear mine for 1,000 which is right at a full year for me.
[n5q4wmn] (score 3, diepte 1 OP) According to PokemonGo I walk about 50km per week
[n5v33ll] (score 3, diepte 1) I only buy Altras because of their wide toebox and zero drop.  Everyone raves about Hokas but their toebox too narrow.
[n5qb3h6] (score 3, diepte 0) A lot of people are recommending sneakers on here but I honestly recommend boots with a bit of an arched last depending on the shape of your feet.  Running shoes make my legs hurt compared to non squishy sole shoes, I wore vans like hell for years but was amazed by how much longer I could walk after I broke in my iron rangers then my whites packer boots.  I'd recommend getting an insole if you also stand a lot instead of just walking, but spend some time finding the right boots for you.
[n5qjlp9] (score 3, diepte 0) I went to the Asics store and was recommended the gel kayano by the store assistant as he noticed that I need more support in my feet. Definitely a little pricey but is very comfortable as I walked 10-20k steps in Japan and even Universal Studios where I barely sat.
[n5qwi2t] (score 3, diepte 2) I don't think leather shoes are great for running or walking 15k steps a day with the horrid smell from sweat.
[n5s48r7] (score 3, diepte 0) How it fits your feet is too individual, but I will recommend buying two pairs and swapping out every day.  It'll make them last more than twice as long.
[n5sjlvs] (score 3, diepte 0) My best advice is to get 2 pairs and switch them out every couple days. They’ll last longer and I always feel like they stop being “as comfortable” by the 5th day if I use them for longer use every day
[n5qc9p4] (score 2, diepte 1) You can get pretty close with shoes that can be resoled.
[n5rki83] (score 2, diepte 1) I agree. I’ve had New Balance Fresh Foams and ASICS Gel Kayanos before. Both really good but the asics are so much more cushiony, and I have plantar fasciitis so that helps a lot.
[n5ro2j4] (score 2, diepte 1) Asics were good but due to cost cutting for extra profit margin over the years, it has become shite in comparison to a pair of Lowa Renegade.
[n5shwlo] (score 2, diepte 1) This is the correct answer.  Good luck op
[n5qalol] (score 2, diepte 1) This is the only answer. NB 990s (esp the V6 which are as cushioned as Hokas) and the top of the line all day on your feet no fuss and as BIFL as a running shoe will get. Not a coincidence that so many dads gravitate to them after years of buying various shoes. They’re the truth
[n5q51sj] (score 2, diepte 0) When it comes to shoes, BFL is a difficult category because they will always wear out with use- especially a lot of use.
Best advice is to go to a shoe store (walking or running) and have them map your gait. It’ll recommend insoles and then you just add those to any other shoe you’re wearing so the shoe itself lasts longer and you can swap out for new insoles when they wear out and your feet start hurting. 
I did this about 8 years ago when I was bartending full time and it made a huge difference for that “custom fit” with literally any shoe I wear. 
There are also companies that will recycle old shoes so you don’t have to throw them away if that is a concern.
[n5vuc8b] (score 2, diepte 1) I wear Altras and I thought the wide toe box is so ugly, but it’s been worth it for the comfort. I definitely wear them with my custom insoles from a podiatrist.
[n5q7dxv] (score 2, diepte 0) So I have flat feet and bad knees, I have had good luck with new balance 530, brooks adrenaline and under armour Slipspeed mega running shoes.   Also most Merrell shoes work great including the Encore Breeze for summer and the Encore Ice for winter.
[n5q93r2] (score 2, diepte 0) I’m fond of Danner waterproof hiking boots. Many models you can have resoled, they have a generous toe box, and if you’re training service dogs, I suspect you may be in some wet grass/puddles, so the waterproofing should be prioritized imo.
[n5qa4pb] (score 2, diepte 0) I suggest you go to a shoe store and try it on. The most important thing is to find the shoe that fits your foot shape. Then you can choose whether it is more cushioning or more supportive based on your needs.
[n5qagjx] (score 2, diepte 0) Here with the Brooks rec. And there is no BIFL for shoes like this. By nature they will wear out.
[n5qn9j9] (score 2, diepte 0) You have to get yourself measured, ideally in a dedicated shoe store.

  
Not all shoes come in all sizes and shapes.  What you want is to get measured, and then they tell you what your options are.

  
The shoes that are extremely comfortable on me, that I can wear and walk 30,000 steps, might give you blisters in just a few minutes even if our feet are the "same size", because they might be different shapes.  My toes might be wider, your heels could be larger.

  
Brand recommendations are really only useful for general quality control, but even then many brands have a fantastic model and a terrible cheap model.
[n5r1idl] (score 2, diepte 0) I second what people are saying about getting your gate checked but, you might do better with a hiking boot. They are sturdier than a walking shoe, they are designed to be worn for 10-20 miles a day, and are better for cold or wet climates. 

If you are In The USA REI has a phenomenal return policy!
[n5r5ojy] (score 2, diepte 0) Sketchers. They're amazing.
[n5snz99] (score 2, diepte 0) Get some real walking shoes. Go to a running store and try on a bunch. Find what feels great.   
Not Chucks.  
Probably not Red Wings.   
I love Altras.  
And if you want something that lasts, ask the clerk at the store. They know which shoes wear out quicker than others (it's not just brands but different models).
[n5v3dw1] (score 2, diepte 0) If you have foot issues I recommend visiting a Podiatrist, Pedorthist and/or orthopedic shoe store that can get you fitting for proper OTC or custom orthotics and appropriate shoes for them.  Life changing.
[n5v3gl2] (score 2, diepte 0) If you have foot issues I recommend visiting a Podiatrist, Pedorthist and/or orthopedic shoe store that can get you fitting for proper OTC or custom orthotics and appropriate shoes for them.  Life changing.
[n5pyttr] (score 1, diepte 0) Hello /u/PigeonsInSpaaaaace! Thank you for your submission! just to inform you, you may also want to try posting in /r/boots which is a smaller subreddit but might be or specialized for your request

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/BuyItForLife) if you have any questions or concerns.*
[n63vdj1] (score 1, diepte 3) Brooks are always available and are cheap on Amazon. Best shoes in my opinion.
[n5sbems] (score 1, diepte 1) Arch supports are BIFL when they have lifetime warranty and refits
[n5t4iss] (score 1, diepte 1) I live in Brooks Ghost 16s. I waited until the 17s came out this year then purchased a few pairs of the 16s on sale to get me through the next year or 2.
[n5v09sq] (score 1, diepte 1) I LOVE my Hoka Cliftons! I have two pairs that are still in great shape after 2 years & 1.5 years. I walk about 13k everyday.
[n5q03pv] (score 1, diepte 0) Sketchers wide fit slip one are one of the most comfortable shoes I've ever worn
[n5q1a3m] (score 1, diepte 1 OP) What kind of rest? In theory I could alternate between the new shoes and my chucks, and then get another pair once my stipend comes around again
[n5q31g4] (score 1, diepte 2) Just a day off is fine to let the leather air out and relax. Rotating with the Chucks would work.
[n5uadm8] (score 1, diepte 2) Word I’ll look into those
[n5q42bl] (score 1, diepte 0) I also do over 10,000 steps every day. I have wide feet and I love New Balance. I buy them when they're on sale and replace them every 3 to 6 months when they start to wear out. 

Also important to own at least 2 pairs of shoes so you can switch them out each day.

You have specific needs and you should probably go somewhere for a professional fitting. If you wreck your feet due to improper support, you will not be able to do your job.
[n5qs6xn] (score 1, diepte 1) At outlets the 990v4 is $119 rn too!
[n6ys860] (score 1, diepte 1) 200 bucks omg….
[n5q670a] (score 1, diepte 0) I love my OnClouds for getting in 10k steps a day. But everyone's feet are different so I would recommend going to a running store or maybe REI and seeing what feels best.
[n5rz1u4] (score 1, diepte 1) I had the lone star 6s and they were great.  Really great.  But, I replaced them with version 8 and they were much poorer quality…materials peeling apart after 8 weeks, sloppier fit, the construction squeaks with gait.  They’ve been demoted to lawn duty as punishment.  I should have known since some of the materials in the toe in the 6s were sewn while the 8s are glued.  Switched to Brooks and I like them every bit as much as the LS6s.
[n5q75lv] (score 1, diepte 0) I used to walk 20k steps at work in my docs, leather on the toe has been polished but they're still going strong 2 years later. Plus the leather looked nice and I have the nonslip soles
[n5qaz68] (score 1, diepte 0) Hoka Cliftons fit my feet the best and I can stand all day or go 15k steps for multiple days without issues. I am on my 3rd pair since switching from Brooks Ghost, which is also a good choice. I give the Clifton a 9/10 and the Ghost a 8/10.
[n5qc63e] (score 1, diepte 0) I love my Altras! Added Superfeet insoles for my mild plantar faciitis.
[n5qclsn] (score 1, diepte 0) Personally fit arch supports is the best way to go. Fit in any running/walking shoe
[n5qctsk] (score 1, diepte 0) Merrell running shoes are my go to, about 6-8 miles a day on the retail floor, only last a year.
[n5qd7ng] (score 1, diepte 0) I work from home and walk my dogs 4-6 miles a day so my steps end up in that range. I really like the Brooks Ghost these days and I previously chewed through a couple pairs of On Cloudswifts which were really comfortable and lasted well, but squeaked like crazy.
[n5qdwmk] (score 1, diepte 0) You can also buy 3 pairs of adidas to last the year? I have mostly noticed wear on the inside. It may cost less than one pair of hokas.
[n5qmx0f] (score 1, diepte 0) Walk 35k a night for 6 nights a week. Although there isn’t any standard best, the New Balance 990 V6s with a pair of Dr Scholl insoles are literally life changing. It doesn’t even feel like you’re walking. But they’re expensive (almost $200 from NB) so look on other sights. I got an ugly brown pair for $120.
[n5y34z2] (score 1, diepte 1) Wow! Can I ask (in a general way) about what kind of walking you're doing? City, hills, paved paths? I'm visiting one of my favorite cities and still only getting about 17-18k steps a day in. In my tiny hometown, I'd have to walk around it 20 times. Would love to get my steps up at home.
[n5qsvon] (score 1, diepte 0) I've been rocking Hoka Bondi 8s and they are fantastic. I've had them since Christmas and they are just now starting to show signs of wear.
(39 reacties met lagere score weggelaten)

=== THREAD 1bl7wu1 ===
SUBREDDIT: r/BuyItForLife
DATUM: 2024-03-22  SCORE: 34  REACTIES: 110
TITEL: Steel toe shoes. My feet hurt!
POST (source_id=post):
I need some recommendations on steel toe shoes. Not a fan of big boots. My last two pairs of Timberlands just get absolutely destroyed. Don’t get me started on Reebok. lol Any help is much appreciated

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kw44r50] (score 42, diepte 0) For work boots that you're going to be wearing 8-12hrs a day, best advice is not to skimp on the price. Get a quality brand for $200-$250 no less!
[kw3mqq5] (score 26, diepte 0) Red Wings
[kw3f3ue] (score 24, diepte 0) I wear lots of Keens but not their steel toes. I've heard they're comfortable though. Not especially durable.
[kw3nke8] (score 14, diepte 0) Red Wings
[kw47ozf] (score 14, diepte 0) Red Wing if you go to the store and have them help sizing boot and insert. Mine going strong after years of hard use and hundreds of combined miles walking on concrete. Just replace the inserts when they start to feel worn.
[kw3il3d] (score 11, diepte 1) Keens are great. I've been rocking the slip on carbon fiber toes for about 5 months, no complaints. Not my first pair of keens
[kw3jfii] (score 10, diepte 0) I own a pair of wolverine. They are boots but they felt like high top shoes and they have held up the best for me.
[kw3fory] (score 8, diepte 0) Check out the Red Wing Worx line.
[kw50cec] (score 7, diepte 1) Redwing sales people are awesome at fitting you with the best shoe.   Then the guy even waterproofed mine after the sale.
[kw40f5g] (score 6, diepte 0) Keens when we were contracting overseas. Worked great, large toe box, worth every penny
[kw3j3xa] (score 5, diepte 2) I wear almost nothing else, because of their wide, tall toe box. Altras and Topo Athletic are good too, but they don't make work boots.
[kw3kret] (score 5, diepte 0) Loved my Irish Setters. Love my Ariats. Keens are the most popular at my work.
[kw6hphc] (score 3, diepte 1) I had some keens and they were comfortable but they destroyed my arches if I was doing a lot of walking in them.  Just beware.
[kw8b3z1] (score 3, diepte 2) Yeah, they're pretty flat inside. I add insoles from SOLE. Some people use SuperFeet or Currex.
[kw6r27t] (score 3, diepte 1) This Is what I’ve got. I’m not too hard on them so I might not be the best to speak to durability but Ive been wearing them most days for a few years and they’re very comfortable
[kw5l8rl] (score 3, diepte 1) I have always heard great things about wolverines, but mine didn't last nearly as long as my timberland pros. It was probably due to the amount of salt water they were exposed to but I was pretty bummed.
[kw7qdvq] (score 3, diepte 1) Another vote for Red Wing. They also make composite toes (no metal) that you can walk onto a plane without taking off (assuming TSA pre-check in the 'states). Those come in walking shoe models as well as work shoes.
[kw3yrev] (score 3, diepte 0) My son-in-law raves about Thurogood 8-inch fly boots.
[kw567lx] (score 3, diepte 3) That surprises me... 6 inch or 8 inch? The sewn sole of the 8 inch seems to hold up well for me
[kw654k1] (score 3, diepte 4) The 8” still have the Vibram sole while the 6” do not anymore. The 6” without is a joke for the price. I am wearing endurance ones and they hold up fine. My boondocks were $60 more and were worse.
[kw4cik5] (score 3, diepte 0) What’s your requirement? Many employers (though, not all) have a specific requirement, like ASTM F2413. Also, some employers will provide an annual stipend. Do you fall into any of these?
[kw4wff3] (score 3, diepte 0) I love my ariat cowboy boot shitkickers.
[kw561mi] (score 3, diepte 0) Justin, square toes. Best boots I've ever had, 2 pairs in 12 years, and I work 60-80/wk
[kw3ijs9] (score 2, diepte 2) I think you'll like Keen steel toe boots.  I work in a chemical factory, very durable and comfortable.
[kw4zr7k] (score 2, diepte 1) I’ve been bouncing through different brands of hard toe boots for a few years and am really liking my Keen Utility boots.  I alternate between 2 pair and keep them on a dryer and so far they’ve lasted longer than carhartts and still look decent.  My work environment is hard on them (lime dust and lots of heat)
[kw5k0xc] (score 2, diepte 1) I wear them for the wide toe box. I haven't had them in steel toes.. Durability has been as good as any in that price range for me.
[kw5ky5r] (score 2, diepte 2) For wide toe boxes, I've also had Altras and Topo Athletics. I actually prefer Topo Athletics for hiking boots. But neither of them make steel-toed work boots. :-/
[kw57100] (score 2, diepte 4) 8 inch. Mix of shop/cement floor and outdoor/groundskeeping work. Everything else about it seems to be fine, but the tread is peeling off of the heel at the back. I had been using shoe goo to glue it back in place but that only lasts a week or two. Gave up and bought of blundstones recently after glowing reviews from coworkers, now I’m only wearing the boondocks when I need the extra ankle support working in the woods
[kw4dwpm] (score 2, diepte 1 OP) We get $100. Also they’re pretty lenient as long as it has some kind of steel or composite
[kw4h8j1] (score 2, diepte 0) r/NicksHandmadeBoots
[kw4j6ez] (score 2, diepte 0) Wore steel toe boots for 27 years, tried Redwings, Timberland, Keen, and a few others. I always kept coming back to Wolverine Durashocks. Durable and very comfortable.
[kw4rwi2] (score 2, diepte 0) Buy high end \[certified\] composite toe instead.  They weigh less, insulate better from cold, and are just slightly less rigid.
[kw55bhf] (score 2, diepte 0) Not sure if you could use these, but the composite toe Sketchers are very comfortable and quite light. The problem I always had with Red Wings and the like were just how heavy they wore on my feet by the end of the day.
[kw56vev] (score 2, diepte 0) If you find a pair that works, buy two. Rotate every single day. Take your boots off after your shift, put on something more comfortable, and throw some shoe trees in. You'll be shocked at how much longer every thing lasts. It's an investment at the beginning, but it's far cheaper down the road.
[kw57mux] (score 2, diepte 0) What kind of work are you doing? That would help a lot for recommendations.


I have a pair of canvas steeltoe boots, because I climb a lot and work in hot weather. They’re super light, have flexible soles, and don’t feel like boots at all. They still have toe protection and have lasted multiple seasons. Brand is Fugu, I got mine before they started selling in the US so check on the quality.

I have a pair of leather boots that I used for working with fire (no steel toes allowed), and they were $400. Worth every penny; they’ve lasted and are super comfy now that they’re broken in. I can tromp around hillsides and walk on coals and don’t worry about my feet. 

They’re both totally different shoes, but perfectly suited for what I use them for.
[kw3f9xq] (score 1, diepte 1 OP) Yeah I’m hard on shoes. Always have been
[kw3iozj] (score 1, diepte 3 OP) Ok cool. I’m looking at some now
[kw45t00] (score 1, diepte 3) Hm, I guess it depends on the sole compound. They have several. The soft rubber used in the Targhee boots and shoes doesn't last long, though it's grippy and comfortable. So the work boots might be different.
[kw4akiz] (score 1, diepte 1) Another vote for keens. Think I own 4 pair now, probably been through about 10. And then never really did, I just use them in the lawn.
[lpvt4l0] (score 1, diepte 2) By destroyed your arches, do you mean you have middle of the arch pain that feels like if you ran or jumped up and down on your feet, your arch would snap in half like how a matchstick would? Or they're just sore like how your calf would if you walked on them for long?

Weird analogy i know, but I bought a shoe that's .5us size smaller than my regular size, couldn't fit my feet so i removed the sole... Now that it's fine I was able to use them, even tip toe in them... And then when I went home i experienced an almost sharp pain in the middle of my arch that made me walk cautiously.

Up to now I'm still experiencing it, so I just moved slower at work to not aggravate it.

I bought fp insoles and am waiting for them but honestly I don't think I can hope much that they'd work for me.
[kw3qpzt] (score 1, diepte 0) Avoid DeWalt, the most uncomfortable shoes I've ever had the displeasure of owning. I do like my Timberland Pro boots, no idea if they make a shoe version.
[kw3x39q] (score 1, diepte 0) Could look into composite. Also, a chance your previous boots simply didn't fit right.
[kw3yjks] (score 1, diepte 1) I was going to say, the boots might not fit correctly.
[kw3yhc2] (score 1, diepte 0) My feet used to hurt in safety shoes so much, I had to take sick leave and go to orthopedist.
 
Luckily, I was able to find a safety shoe that I wear all day without any issues (if stinking feet isn’t taken in to count).
 
[Sievi](https://www.sievi.com/uk/) is my go-to brand, as they are available everywhere here, but what works for one, doesn’t necessarily work for others.

One thing that was superduper important, was changing the default inner sole to one that supports my high feet arch. I have special soles in my cross-country ski boots and rollerblades also. I suggest you go to a specialist to measure your feet shape to better understand where the issue is. Money spent on wellfare of your feet is going to pay itself back by tenfold with less health problems down the line. You need to walk with your legs the rest of your life.
[kw50i0a] (score 1, diepte 2) Haven’t been impressed with the boondocks. Sole started peeling after 8 months.
[kw47bsp] (score 1, diepte 0) Not bifl if only one pair, but i wear a different pair every day. Timberland Pros.
[kw47goq] (score 1, diepte 1 OP) Yeah I didn’t think abt that. Definitely won’t last for life but I get good pointers from yall lol
[lbo47w5] (score 1, diepte 2) Yeah, your insoles need ~24 to decompress. You can get a lot of additional miles out of your shoes and feet just by rotating two pairs.
[kw554i9] (score 1, diepte 1) I wear them too. I’ve never even noticed that there is a steel toe in there.
[kw4f6d6] (score 1, diepte 2) Then you have lots of options. BIFL does not necessarily mean comfortable. Is your stipend a one time deal or an annual thing?
[kw4fgt6] (score 1, diepte 3 OP) Its annual. My last two pairs were the timberland pro powertrains. They last just shy of a year too
[kw57duk] (score 1, diepte 4) I’d look at Keen. I’ve found their selection is pretty good. I personally favor a larger toe box and remove their insoles for less or a heel lift - but that’s my preference. Their boots last me over a year of daily use of 6-8 hours without overstraining my calves before moving on to another pair.
[kw4gldn] (score 1, diepte 0) Have you tried timberland pro? They are legitimately better than timberlands
[kw4kpt1] (score 1, diepte 0) I like wolverines a lot.
[kw4sfwe] (score 1, diepte 0) Redwing makes a safety toe sneaker. Very comfortable.
[kw4sigc] (score 1, diepte 0) I also wear Keens. It’s roomy toe boxe, removable insoles. They do make some steel toes that feel more like hiking boots if you don’t need heavy duty. But my daily is the San Jose boot.
[kw4t311] (score 1, diepte 0) Georgia boot has been my go to lately, Thorogood has had some QA issues with me and bottoming out quickly.
[kw4ts7y] (score 1, diepte 0) Red Wing is the gold standard in my field. They last people 5+ years and quality is exceptional. If you're allowed to have a composite toe, (fiberglass/carbon fiber,) they're all much more comfortable.
[kw4u8aa] (score 1, diepte 0) Redwing Kingtoe line with composite toe in the largest width available is the best I've found.
[kw4x5jb] (score 1, diepte 0) I’ve been very happy with my steel blue 532s (composite toe). Put ‘em through hell fora couple years and they are in great shape. Very comfy too
[kw4x6h5] (score 1, diepte 0) Wolverine raiders for boots.  Wolverine rev vent ultrashock for tennis shoe type.  Best work shoes I've ever had my rev ultra shocks are going on 3 years.
[kw4x8o3] (score 1, diepte 0) If you can use carbon fiber toe boots, it's so much better than steel. No getting your toes cut off like steel toes can, light, more comfortable. Keen makes some very nice work boots.
[kw4y5pv] (score 1, diepte 0) I have been wearing timberlands for the last six or seven years and I love them redwing makes A Chinese version of their work shoes that are reasonable and decent
[kw50nvs] (score 1, diepte 0) Red wing. They come in extra wide if you need that.
[kw54zr2] (score 1, diepte 0) My husband likes Red Wing. He works 12 hour shifts, sometimes 80 hours a week. People's feet are unique, though, and so what works for someone else may not work for you. He did say that He doesn't have to break in the Red Wings Red Wing like he did the Timberlands.
[kw8ixe9] (score 1, diepte 1) I second Sketchers, my company requires steel toes shoes and I've found that the Sketchers last and are comfortable
[kw55ta2] (score 1, diepte 0) Thorogood boots are awesome, if you are looking for a wedge sole style boot they are the way to go.


First pair of work shoes I have ever had where I feel like I can stand all day and not even really notice it.
[kw7nm2z] (score 1, diepte 1 OP) Really?! Definitely worth the money. That’s impressive
[kw7pgsy] (score 1, diepte 2) Yes sir, and the square toe allows for some adjustment through the day to increase comfort. I would suggest tuff toe depending on your craft, I climbed on ropes, so my toes were always against something to position myself.
[kw56iex] (score 1, diepte 0) Buy metatarsal boots. They are awesome and super comfortable. Safer as well.
[kw56yts] (score 1, diepte 1 OP) Excellent idea
[kw58gmm] (score 1, diepte 0) Get resolable boots from somewhere like redwing, thorogood, nicks, or whites. You will only have to pay to resole them if you take care of the leather
[kw5c7qq] (score 1, diepte 0) $20 insoles.
[kw5d4p4] (score 1, diepte 0) [Nick's](https://nicksboots.com/).
[kw5dtio] (score 1, diepte 0) Belleville  boots  from their website are good I'm o. My 3rd pair in 6 years going on 7
[kw5f9e3] (score 1, diepte 0) I’ve been working construction practically my entire adult life and I’ve had just about every brand of boot out there. A typical boot usually lasts me about a year, except Thorogood. I’ve had my current pair going on 3 years now and they just won’t die. By far the best quality boot I’ve ever owned. Not only that they have a rebuild program that you can send the boots in to get resoled and reworked. Also they are made in America unlike most boots these days.
[kw5fk88] (score 1, diepte 1) I will add they you will be cussing me the first week you wear them because the break in period is a bit rough but in my opinion that just speaks to the quality of the materials.
[kw5gjz5] (score 1, diepte 0) Carolina 8 inch loggers. I've worn Tims and redwings and the Carolinas were the best boots I ever wore. I was working 16 hours shifts for the railroad so I have beat the absolute shit out of some boots, and you can't go wrong with the Carolinas
[kw5ie7m] (score 1, diepte 0) Have you looked into wide boots?  My feet feel way better with some extra wiggle room.  


Also, Rocky's boots have always treated me well and I can't recommend them more.
[kw5igdc] (score 1, diepte 0) Most of the military guys I've worked with over the years buy Rocky SV2 boots if they have to buy their own.

I'm a fan of Garmont, but I can speak to their steel toe variants.
(35 reacties met lagere score weggelaten)

=== THREAD spa8c9 ===
SUBREDDIT: r/BuyItForLife
DATUM: 2022-02-10  SCORE: 56  REACTIES: 109
TITEL: Comfortable and cushiony shoes for walking on pavement 10KM/couple hours a day (UK)
POST (source_id=post):
I walk a fair amount in constant bursts. Usually about 5k at a pace of 8:30m/k two to three times a day. All around the town where I live on pavement. I like really cushiony shoes otherwise the soles of my feet start to hurt. Things like Sketchers have been great but they don't last long before the sole wears out and my foot comes through the bottom (about 3 months). I've also been using Mammut shoes which last a good bit longer but they aren't quite as soft. Is there something that has that lovely cushion but doesn't have a sole that wears out super quick? I did look in to some running shoes like what New Balance offer but it looks like they would wear down too quick. (800K running, assuming it lasts a bit longer walking, that's still only gonna be 3 or 4 months). I don't like bulky shoes/boots as they are stiffer and always feel more awkward to walk in. Also they are never as padded in my experience.

What am I missing here? Why are all the "walking shoes" that I try on in outdoor stores not cushioned enough? Regardless of cost nothing seems to match that cushiony part of Sketchers. 

I did try looking around on the subreddit but I couldn't find anything that really hammered on the cushion-y-ness of the shoes. It's less about lasting a long time, and more about lasting an ok amount of time with lots of bounce I guess? 

Another thing I've tried before is insoles, but I've never really found anything good there either. They always end up pushing your foot up against the top of the shoe uncomfortably, or they don't have enough cushion. Most likely because the shoe isn't designed with you adding one in mind. 

Extra pluses, having a more subdued design is great. I'll get trainer looking trainers if I have too, but something that comes in all black, or nice flat colours, is definitely a plus. 

As for price, I'm not too worried. If they are good then I'll pay it. 

Thanks for any replies!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hwdthck] (score 43, diepte 0) Hokas are my favorite but I don’t think any shoes that aren’t boots will ever be BIFL. the soles will eventually wear away and need to be replaced. But hokas stay responsive long after that happens imho :)
[hwdtdem] (score 17, diepte 0) I strongly recommend going to a running store and getting properly fitted for shoes. Everyone’s anatomy is a little different, and I had terrible knee problems until a few years ago when I went to a store and they put me in shoes that were proper for ME and MY stride.

Since then I have gotten a new pair every 1,000 miles or so. There is a particular model of Brooks that is just ~*chef’s kiss*~ for me, but might be horribly uncomfortable for you.
[hwej2q4] (score 14, diepte 0) I would recommend getting New Balance, removing the insole, and replacing it with a SuperFeet insole.  My podiatrist best buddy recommended this and it has changed my walking life completely!
[hweqnm7] (score 11, diepte 0) Have you tried minimalist shoes? Seems counterintuitive but if you’re feet are acclimated they’ll last awhile and they helped reduce my back and knee soreness
[hwfu3zh] (score 10, diepte 0) You need to realign your brain with the facts.  People who legit walk/run will NEVER have BIFL footwear.  EVERY pair of shoes designed to accommodate walking/running have a finite lifespan.  Every brand has a value but the general rule is 500 miles = trashcan regardless of your opinion on the topic based on the appearance.  If you want the best advice, you will go to your local running store and/or the running store in the closest city.

They can perform a gait analysis and if there are pronation issues, they can recommend shoes to accommodate that issue as us common people do not know which lines/brands dead with XXX pronation issues.  They can also recommend that Brand X or Line Y of Brand X should be good for XXX miles vs. your current brand that is good for YYY miles.

TLDR:  Find your answer at a running store, not the internet & realize shoes for sport are expendable
[hwfi6gq] (score 7, diepte 4) Jd sports isn't a running store, it's a sports fashion retailer and nothing they sell will last
[hweawy7] (score 6, diepte 0) I have plantar fasciitis and I have a very high arch. The soles of my feet hurt too. I got a pair of vionic slippers to wear at home and a pair of vionic sandals and I wear them everyday and walk around in my city. I went to a podiatrist to get custom orthotics and I put them in my running shoes after taking the insoles out. I am also supposed to stretch but I’ve been lazy about it. All this helps me hope it helps you!
[hwf8u2v] (score 6, diepte 2) They’re a game changer. I like the green ones but the carbon ultra thin are also nice if you don’t want a thick insole. And NB had some very squishy shoes if you want a thick outsole.  They manufacture all shoes to have removable insoles which is fairly unique these days.
[hwek7tg] (score 6, diepte 0) Adidas Ultraboost are the comfiest cushioniest sneakers I’ve owned. 

I worked for a sneaker retailer for 5 years
[hwduedm] (score 5, diepte 1 OP) I would definitely love to do this, I need to find somewhere nearby that does it and actually does it well. Thanks for the recommendation.
[hwdumh7] (score 5, diepte 1 OP) Yeah, as I said in the thing it isn’t really BIFL, just something that lasts longer then 3 months before it falls apart. I’ll take a look at Hokas. Wondering if there’s anywhere nearby that I can try some on.
[hwdx2f8] (score 5, diepte 0) Have you tried Allbirds? Not sure about their bifl aspect, but they are the most cushioned pair of shoes I ever had. It’s like you walking on the clouds. Their signature wool runner model is the one I’d recommend. Although they came up with other styles recently such as water repellent ones etc.
[hwen7qh] (score 5, diepte 1 OP) Ahh interesting, ok. I’ll take a look at them and see. Thanks for the idea. Not seen superfeet before. They definitely look good.
[hwf9g7w] (score 5, diepte 3 OP) I was looking at the green running ones. That’s also pretty cool about NB. Makes me extra sad that the NB outlet store near me has closed down. Would have made it very easy to try some on.
[hwf2pxh] (score 5, diepte 0) Damn I miss my zeetas. They were amazing. I pounded pavement in three different countries, over 5 years and barely felt the cobblestones etc.

 Sometimes you can find a NIB pair pop up on Poshmark. Zeetas were so good and long lasting they ended up going out of business :/
[hwfccny] (score 4, diepte 2) Local running store should stock them :) they also have nicer suede editions - I love those because they’re slightly more fashionable haha
[hwfisrt] (score 4, diepte 4) Hoka.com

30 DAY GUARANTEE + FREE SHIPPING & FREE RETURNS
×
Don’t take our word for it, ask another runner. Better yet, try a pair for yourself. Take them for a run, or two or ten. If you are not completely satisfied, you can return or exchange them within 30 days of the original purchase, no questions asked. What have you got to lose?
[hwdwqe2] (score 4, diepte 0) Based on personal experience I would recommend shoes with natural rubber sole: long lasting and comfortable. Durability will also depend on your gait and weight.
[hwe4rni] (score 4, diepte 0) Money no option if you are looking for a durable sports shoe then innov8 have graphene enhanced soles [news article link](https://www.advnture.com/features/what-is-graphene-and-why-are-trail-runners-talking-about-it) and [innov8 website link](https://www.inov-8.com/g-series)
[hwe58w7] (score 4, diepte 1 OP) Ahh the all magical graphene solving the worlds problems.  😂

Those all look pretty well priced compared to the Mammuts and everything else I’ve looked at. I’ll definitely do some reading and looking in to those to see how they fair. Thanks!
[hwen06l] (score 4, diepte 1 OP) Ultraboost has come up twice now, so that’s definitely one for the radar! Thanks for the suggestion. If you worked in sneaker retail that’s a good sign to take the advice 😂
[hwekgnt] (score 4, diepte 0) If money isn’t an issue, go ultraboost. I can walk 11 hours on them all day and not feel pain. Pricey but amazing shoes. Do NOT get Skechers with memory foam. After a while it falls apart, gets all nasty and they just aren’t comfortable at all.
[hwewoa3] (score 4, diepte 0) Have you tried Asics? Hopefully you can find some colours you like, but they are more often than not bright sneakery colours :P
[hwgi2df] (score 4, diepte 0) on clouds
[hwdxyv3] (score 3, diepte 2) Think Clarks desert boots etc. I have a 5 year old pair of Astorflex Greenflex boots that have seen it all and held up as well as my pair of Red Wing Iron Ranger boots. Very comfortable sole and uppers. Obviously comfort is subjective, so try them and see
[hwdy7im] (score 3, diepte 3 OP) Got it, thanks! I appreciate the answer a lot and will take a look.
[hwdxkq6] (score 3, diepte 1 OP) I have not heard of them before, but even if they don’t turn out to be a long lasting shoe I love their design and will probably get some anyway. Thanks for the recommendation!
[hwuosr1] (score 3, diepte 1) I endorse this…they actually don’t last for longer than a few years, but feet don’t hurt after walking for 12 hours a day. As long as your not gonna be stepping on wooden pallets or sidewalk curbs all days your good.
[hwe635k] (score 3, diepte 2) If you do end up getting some I expect an update in 12 months! Might tempt me into buying if it’s favourable :-)
[hwe6coy] (score 3, diepte 3 OP) Will do for sure! They sound interesting.
[hwfafns] (score 3, diepte 1) I had planter fasciitis about 6 years ago,
Went to a chiropractor and had 6 sessions of a laser machine on my foot.  (Something about increasing the blood flow!). Never had had ANY pain since.
[hwemuhh] (score 3, diepte 1 OP) Yeah I’m very familiar with sketchers. They are what I used for a while, just replacing them every few months when they wear out. I’ll take a look at the ultra boost. They look pretty nice.
[hweppz0] (score 3, diepte 2) If you can, try getting them on sale. I paid MSRP because the colorway I wanted was newer and harder to find but sometimes you’ll get lucky and find decent 25%+ off on some pairs.
[hwexcwm] (score 3, diepte 1 OP) I did take a look at them as they had come up on the other threads I checked. You are right, very bright colours. They are in the list to try out with the other recommendations from others. Not sure where I can try some on though.
[hwf2fub] (score 3, diepte 0) Altra
[hwf43yr] (score 3, diepte 0) Maybe something different than what you are thinking, but I have some Nicks boots and with the leather sole there are very comfortable. I have used them all day on concrete walking around a factory. 

&#x200B;

I have the Urban Loggers, but the Falcon is also a nice boot.
[hwf5skp] (score 3, diepte 0) Art company. The style is usually loved or loathed but personally I love them. I have a pair of Skylines worn every day for 6 miles round trip commute 5 days a week for over 5 years and the sole isn't really worn down at all. I've replaced the insoles but I always need to do that for specific orthopedic insoles. I've also got a pair of boots and sandals all of which are lasting me almost 10 years. They're a great shoe producer if you like the style that is.
[hwfodk8] (score 3, diepte 1 OP) I’ve tried, I tried plenty of “walking shoes” that weren’t padded or cushy. Basically through all of school and uni. I’d always try different brands or shoe styles each time it was time to change shoes. Always had sore feet at the end of the day and just assumed that’s just life when you walk a bunch. Tried sketchers once, for the couple months the first pair lasted my feet were in heaven. Soreness just went away. 

Realised that walking shoes just don’t do it for me. Mammut have been the best ones that seem a bit more cushy then the rest, but even they aren’t as heavenly to walk in. They just last a lot longer so I’ve been making the trade off.
[hwflb13] (score 3, diepte 0) Maybe its my flat feet but I could walk 5m in clogs and stand all day. But I'm the sick kinda person who'd wear flip flops or go barefoot if I could.
[hwfp6q2] (score 3, diepte 0) I find shoes that you can remove the insole and replace with Scholl gel insole, I have bought them in the UK
[hwh0p1f] (score 3, diepte 1 OP) I did say in my original post it’s less about lasting a long time and more about lasting an ok amount of time. I’m just looking for something that lasts longer then 3 months. This subreddit just seemed like a good place to ask about this type of thing. Finding high quality products, even if they aren’t *truly* BIFL. The idea of going to a store to do a test is definitely a good idea that’s come up a couple times. I wanna definitely do that if I can.
[hwh1i90] (score 3, diepte 1) Brooks are the best, most comfortable shoes I've ever had.
[hwfllbx] (score 2, diepte 2) I second Brooks, they are insanely comfortable walking shoes that are well built.
[hwfpy4r] (score 2, diepte 1) I love Hokas for comfort, but they don’t last for me at all. I walk a about 3 miles a day (which is not that much) and they are worn out in 4-6 months.
[hwfa949] (score 2, diepte 4) Honestly I haven't noticed much difference in the waterproofness either, both can take splashes or a few puddles but not too much. The warmth is another added bonus especially in winter, the insole and upper is wool so it's warm and cozy.
[hwfazea] (score 2, diepte 6) It's still comfortable because of the breathable fabric
[hwfc2rv] (score 2, diepte 7 OP) Awesome, that’s good to hear. I think I’m definitely gonna pick some up just to have, regardless of their ability to fill the role I’m after. Bonus points if they can though.
[hwe9h3k] (score 2, diepte 0) Sketchers comfort really is unmatched ime.   I'd just get their walking shoes and replace as needed.
[hwebp5m] (score 2, diepte 1 OP) I have totally done that before. Just go through 4 or 5 pairs a year. They are very comfy.
[hwebx7n] (score 2, diepte 1 OP) Thanks for the info and recommendations! I’ll take a look at those. I’ll have to look in to stretches too, wonder if that’ll help me long term.
[i78r1lh] (score 2, diepte 3) Hey Just wondering what NB you have? I get some knee pain and side of the foot pain so I am looking for a supportive NB shoe for work. I hate somewhat flat feet too.
[hwhdc4e] (score 2, diepte 3 OP) Yeah I’m really starting to think I need to travel a bit further and go to a proper running store, not the local JD Sports, but that’s gonna be a day trip.
[hxyg7h7] (score 2, diepte 1) Which superfeet insoles do you recommend for everyday wear? I’m in the market for some heavy duty ones that are still suitable for casual shoes.
[iucs4lj] (score 2, diepte 1) Super agree w this, I’ve done both new balance and ultraboosts by adidas also with the blue superfeet insole. Loved both for walk 4-6 miles a day on pavement and asphalt for over a year. I get nerve pain in my left foot (Morton’s neuroma) so a wide toe box and cushion help on pavement, and the superfeet gave support with some comfortable flex still
[hwf73iy] (score 2, diepte 2) Make it 3, I came to say the same. Also check the Ultraboost 21 , it’s even more comfy since it kind of hugs the foot.
[hweq1yl] (score 2, diepte 3 OP) The website offers you 20% off if you sign up for their newsletter thing (can just go to the spam email). I plan to try and get to a store at some point though to try some things out, so hopefully there will be some discounts.
[hweqf8j] (score 2, diepte 4) So the one thing you should know is that UB are pretty tight to get on initially but after the first day or two I’ve been able to just slip into them with minimal effort. It’s just the shoe hole(?) that’s a bit tight. 

oh and… avoid water. Don’t go splashin in puddles.
[hwer329] (score 2, diepte 5 OP) Hmm… avoiding water will definitely be difficult. I go walking rain or shine regardless of the water. Also I getcha. Shoe hole will be tight 😂
[hwerhim] (score 2, diepte 6) Rains not the biggest issue. Mostly just deeper water. Puddles may get in because it’s a knit shoe. Very comfortable but it’s downside is being a very holey shoe. I walk in the rain often because I live in the swamp here in Florida. 3/4 of the year is raining. Tread lightly in puddles if unavoidable. You don’t want a splash to cause wet sock.
[hwerpru] (score 2, diepte 7 OP) Right. Lots of puddles and rain in the UK. I’ll definitely have to take it in to consideration when choosing. Still look really nice though. Hard choices.
[hwerbs8] (score 2, diepte 1 OP) I haven’t. That’s an interesting idea. I don’t have back or knee problems personally, purely the soles of my feet that I worry about with some shoes. I’ll still take a look though, thanks!
[hwf71x0] (score 2, diepte 1 OP) Looks interesting! I’ll see if I can find somewhere to try them.
[hwf7bdw] (score 2, diepte 1 OP) I can’t find anything when I search for zeetas or nib? Sucks that they went out of business though.
[hwf39vr] (score 2, diepte 0) Sketchers and other super flexiblee soled shoes are horrible for me and leave me with lots of foot pain.

I have moved into low rise hiking shoes for long distance walking.  much more durable and much better for my feet
[hwf865w] (score 2, diepte 1 OP) The 1773 blue planet looks like it has sold for days 😂 

I don’t hate the style though, another good one for the list. The idea of replacing the insoles that shoes coke with is something I hadn’t thought about until someone recommended superfeet. I’d always gotten those ones that went on top of the sole that was already there. Thanks!
[hwha46i] (score 2, diepte 2) Maybe it's your feeg. Maybe you need an Orthotic sole too.
[hwfoum1] (score 2, diepte 1 OP) Damn, definitely jealous of that ability. Without the cushion there my feet really feel it.
[hwjpiji] (score 2, diepte 2) This is the shoe, they come in many color combos and for both men and women sizing. If you have wide feet, they might not work as well, but regular width do well. https://www.danner.com/men/hike/trail-2650-3-charcoal-goblin-blue.html
[hwhdmny] (score 2, diepte 1 OP) I’ll take a look and see what they have. They do have a lot of clogs 😂
[hwg54da] (score 2, diepte 0) I have been really impressed with my Brooks running shoes. The have an online questionnaire that helps you find the right fit for their shoes and your needs and so far I’m loving them. They were recommended to me by a lot of other active people and so far they’ve been great. I’m a nurse and I’m on my feet for a lot of hours and do a lot of walking. Don’t know if these shoes are BITFL, but definitely a good shoe to look into.
[hwhdpd3] (score 2, diepte 1 OP) Brooks has come up a few times so that’s definitely pushed them higher on the list. Definitely a good one to consider. The questionnaire sounds great too, definitely gonna take that when I get a chance. Thanks!
[hwhdg3d] (score 2, diepte 1 OP) Not heard of that brand before, thanks! Definitely gonna take a look at them. They seem pretty good on first look and that’s a good recommendation.
[hwhd9ql] (score 2, diepte 1 OP) They look pretty unique! Thanks!
[hwnyhn2] (score 2, diepte 2) tbh I don't love their look so much as the comfort of them. the price kinda sucks too but you do get what you pay for.
[hwhd7hj] (score 2, diepte 1 OP) The cushy part is definitely interesting. All the shoes I’ve tried that aren’t so cushy have always caused the pain but the super cushy ones like the sketchers are pain free, at least for the walking that I do. You’re not the first person to mention it though so I’ve got some looking to do on it. I’ll take a look at the Nikes 😂
(40 reacties met lagere score weggelaten)

