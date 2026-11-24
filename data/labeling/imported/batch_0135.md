# Label-batch batch_0135

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
Schrijf het resultaat naar `batch_0135.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: wdvl3i, 41k8r6, yhi1dx).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD wdvl3i ===
SUBREDDIT: r/Chefit
DATUM: 2022-08-01  SCORE: 177  REACTIES: 65
TITEL: A Guide to Shoes and Foot Care for Hospitality Workers
POST (source_id=post):
***A guide for foot care and shoes in the hospitality industry.***

*Hello, let me briefly share a little information about myself. I have worked in the industry since high school. I have been in almost every role in our industry, from busser and dishwasher to server, banquet server, prep cook, line cook, supervisor, and manager. I was a busser when I started, quickly working up to the dishwasher and Steward roles, and then on to other positions and eventually management. During that time, I have worked in mom-and-pop restaurants, food trucks, chain restaurants, fast food, upscale dining, fine dining, hotels, resorts, theme parks, and other venues. I have carried a 90-page binder detailing how to survive a shift in the industry that I created throughout my career to each employer I work for; It has grown to include other topics, but the guide I post here is the original roots of that document. It's all about foot care and shoes.*

*I have spent the past year curating new information, trying out shoes, and researching information for this guide, and I am now sharing it with all of you in the hopes that you find it beneficial.*

**^(NOTICE: INFORMATION CONTAINED WITHIN THIS GUIDE IS PROVIDED AS OPINION, IT IS NOT LEGAL OR MEDICAL ADVICE, AND SHOULD NOT BE TAKEN AS SUCH.)**

**IF YOU OR SOMEONE YOU KNOW IS EXPEIRECNING A MENTAL HEALTH CRISIS OR JUST NEEDS SOMEONE TO TALK TO**, I ENCOURAGE YOU TO **REACH OUT TO YOUR LOCAL MENTAL HEALTH RESOURCES**, IF YOU **LIVE IN THE UNITED STATES OF AMERICA, DIAL 988 FOR HELP NOW**. (YOU ARE NOT ALONE.)

# FOOT CARE AND HYGIENE

**Proper hygiene is necessary**; you should clip your toenails every week to prevent ingrown ones. Make sure to clip toenails straight across and leave them long enough so that the corners lie loosely against the skin at the sides—no over-trimming of nails and no pointy V-shapes. Also, wash your feet daily, especially after a long shift or when your feet have become wet throughout the work day. If I had a choice between washing them before or after, I would choose after the shift. Keep some lotion around to use on your feet at least once a week; it helps, trust me. Finally, don't knock the pedicures, I get one at least every six months, and they can help your feet feel better, I promise.

According to the Cleveland Clinic, the cause of ingrown toenails can be hereditary, from trauma, due to improper trimming, ill-fitting footwear, improper pedicures, and poor circulation. You can treat an ingrown toenail on your own in some cases. [Here are the steps provided by the Cleveland Clinic in their guide](https://health.clevelandclinic.org/how-you-can-prevent-and-treat-painful-ingrown-toenails/).

Soak it and wait, soaking the toe in warm water with Epsom salt or a mild detergent, then applying an antibiotic ointment and bandage to the area.

Removing it yourself if there's no infection. Soak the feet in a very warm bath with Epsom salt. This will help soften the skin and reduce inflammation. Using clean nail-cutting tools, you can then attempt to clip the affected area and apply an antibiotic ointment. If treating the ingrown toenail is something that can no longer be done, or you are uncomfortable doing so yourself, it's time to see a podiatrist.

Never ignore an infected ingrown nail. According to the Cleveland Clinic, ignoring the infection can cause it to spread and lead to severe complications, especially if you suffer from poor blood flow, an impaired immune system, or neuropathy of diabetes (previously referred to as diabetic neuropathy).\*[^(\*INFORMATION PROVIDED BY THE CLEVELAND CLINIC, DR. STOCK, and DR. BOTEK)](https://health.clevelandclinic.org/how-you-can-prevent-and-treat-painful-ingrown-toenails/)^(.)

The use of foot powder is a key to feeling comfortable when wearing shoes during long shifts at work. Foot powder also aids in eliminating foul odors and bacteria, as well as excess moisture, and it can help those who sweat heavily or experience an overheating sensation when wearing work shoes. I highly recommend using foot powder daily. Many foot powders come in different versions. Please consult a physician before using any foot powder labeled as "medicated" foot powder. 

# PAIN MANAGEMENT

***Pain management for sore or hurting feet is sometimes necessary***; for sore feet, you want to use over-the-counter **NSAIDs or Non-steroidal anti-inflammatory drugs** such as **ibuprofen**, **aspirin**, or **naproxen**.\*\*\*

The RICE Method is a recovery routine recommended by the American Podiatric Medical Association. Dr. Gabe Mirkin first coined the mnemonic RICE in 1978. It stands for Rest, Apply, Compression, and Elevation.

When using **the RICE method** the steps are as follows:

1. **REST**, stay off sore or injured feet; excessive use can prolong or worsen the pain or injury.
2. **APPLY** an ice pack as soon as possible, and keep icing for around forty-eight (48) hours, keeping the icing to no longer than twenty (20) minutes at a time.
3. **COMPRESSION**, use compression bandages or wraps to help relieve prolonged pain, but remember not to cut off your circulation simultaneously.
4. **ELEVATE**, it's advice as old as time, elevate sore feet, it does help. When you get home from work, try elevating your feet for thirty 30 minutes, even if you do nothing else; this can help ease any foot or leg pain you may have.

If possible, try to take your breaks somewhere you can sit down and get off your feet. It's small, but it can help you get through a long shift. Condition yourself and you're feet to be better prepared for long shifts of standing and walking. Try to take a five-minute walk every day. When you can do it without your feet hurting afterward, up the time to ten (10) minutes, and keep adding five (5) minutes to the walk until you can consistently walk for thirty (30) minutes a day without being winded our having your feet hate you. Slowly, your feet will grow stronger, and it will help condition them for the long shifts.

Stretch your feet before and during the shift; things like toe curls and other stretches can help; [check out this guide from Harvard University's Medical School on various foot stretches you can do before a long shift](https://www.health.harvard.edu/staying-healthy/exercises-and-stretches-for-foot-health).

Soaking sore feet in Epsom salt can help provide relief. It does several things. It helps reduce inflammation of the feet and lower legs, as well as exfoliate the skin; it also helps reduce bacteria on the feet, cleaning them and providing a fresh feeling and reducing odor-causing bacteria. See additional information and guidelines for soaking feet in Epsom salt below:

* When soaking feet in Epsom salt, **keep the water between 92°F/33.3°C**  **and 100 °F/37.7** **°C**.
* A basin, foot spa, or other people-safe and bacteria-free container can be used, preferably one large enough to hold both feet. You should **fill the container with water just above the ankles**.
* Using around half or three-quarters of a cup of Epsom salt per soak would be best. Ensure you **soak for around twenty (20) to thirty (30) minutes**.
* Be mindful that soaking you're feet in Epsom salt will draw out moisture from the skin; it is recommended that you use a good foot lotion after drying your feet.

\***^(DO NOT SOAK YOUR FEET IF: YOU ARE DIABETIC AS IT CAN BE LIFE-THREATENING, OR IF YOU HAVE OVERLY DRY SKIN AS THIS COULD CAUSE DAMAGE TO YOUR SKIN; IT IS ALSO RECOMMENDED NOT TO SOAK FEET THAT HAVE CRACKED, BROKEN, OR EXPOSED SKIN OR WOUNDS AS IT CAN RESULT IN INFECTION AND/OR DELAYED HEALING.)**

^(\*\*)**^(CAUTION: NOT ALL EPSOM SALT IS INTENDED FOR HUMAN USE. WHEN SHOPPING FOR EPSOM SALT, LOOK FOR THE DESIGNATION "USP" ON THE LABEL. THIS INDICATES ITS BEEN SCIENTIFICALLY TESTED FOR HUMAN USE AND IS SAFE TO USE ACCORDING TO THE FDA.)**

**^(\*\*\*USE OF NSAIDS AND OTHER OTC PRODUCTS CAN CAUSE ADDICTION, IF YOU OR SOMEONE YOU KNOW NEEDS ASSISTANCE IN LOCATING ADDICTION RESOURCES CONTACT THE SAMHSA's NATIONAL HOTLINE AT 1-800-662-4357)**

# SHOES

Quality over quantity, investing in quality shoes is vital, and when I say quality, I don't necessarily mean expensive. You can get quality shoes that are inexpensive by shopping around thrift markets, used clothing/shoe stores, or even sales. Bottom line, don't keep buying those $10-$20 knock-offs from Walmart every few months just because they are cheap. If you need to save up to afford a good quality shoe, then do so, but make it a goal and get the shoes; I promise it will make it 100% more bearable.

If you need an insole after one use, that's probably not the shoe for you. That one size fits all or "custom fit" insoles from Dr. Scholl's station at the local grocer or pharmacy are not a permanent fix to sore feet; at best, they are a stop-gap solution and an incredible money sink at $10-$50 a pop. No, insoles are not bad. A quality insole from an Orthopedic specialist is the kind of insole I would recommend. It will be much more expensive, but it was last three or even four times as long as a generic store-bought insole, and what's best is that it will be 100% guaranteed to be the best option for your feet, no guesses on sizes, styles, or features needed.

Proper fitting shoes are a must. The shoes should not be loose, as this is a safety hazard, and not too tight as this is painful. You should be able to slip a finger between the top of the shoe and your foot with ease.

New shoes should be at their peak comfort about one week into wearing, and they should not be more painful to wear as time goes on. It can take roughly a week of 6-10 hour shifts to break in new work shoes properly, however, if on day one of wearing a new shoe you have blisters, your feet are swollen, or you are experiencing pain that is enough to warrant taking aspirin or soaking your feet. It's probably not a good choice to keep wearing the shoes.

When should you replace a non-slip shoe? 

Generally speaking, you should replace non-slip shoes when the outsole has worn down and is offering less than the width of a quarter in depth. Like tires, outsoles will wear down over time and eventually lose their non-slip properties. 

What should you look for when determining if a shoe is non-slip? 

Below you will find some examples of non-slip treads. They typically have a patterned design with numerous crevices that help the shoe generate friction and stick to the ground rather than hydroplaning over it and causing a slip or fall. 

**EXAMPLES OF NON-SLIP TREAD**

[EXAMPLE 1](https://www.srmax.com/images/products/sr-max-edison-black-mens-oxford-outsole.jpg) | [EXAMPLE 2](https://cdn.shopify.com/s/files/1/0855/0718/files/anti-slip-tread-768x768.png?v=1596047300) | [EXAMPLE 3](https://emerilsfootwear.com/wp-content/uploads/2021/02/ELWODIZL-001-SOLE.jpg)

# SOCKS

Wear appropriate socks with your shoes. They are padded for heavy walking, lightweight for hot environments, quick drying or moisture wicking for wet or humid climates, or a mixture of these features. As far as socks are concerned, what is advertised is usually correct. Still, watch out for sales gimmicks. Not all manufacturers are created equal.

The fabric of your socks matters! Everyone is different, and as such, we will all have different needs and preferences for socks. Below you will find some general guidelines about some of the more common sock fabrics to pick from in the industry.

Here is a list of fabrics you should generally avoid. However, don't discount them entirely; for some, these fabrics might be comfortable: Acrylic, Silk, Spandex\*, Nylon, Rayon, Cashmere, Polypropylene, and Tencel.**^(\*SPANDEX CAN BE BENEFICIAL IN COMPRESSION SOCKS, IT IS RECOMMENDED YOU CONSULT A PHYSICIAN BEFORE WEARING COMPRESSION SOCKS AS THEY CAN CAUSE LONG TERM INJURIES FOR SOME.)**

Keeping a second pair of socks in a bag or locker at work can be beneficial, as switching socks that have become soaked or damaged can be the difference between a good day and a bad one. When looking at the proper fitting for socks, it is always better to skew upwards in size rather than purchase a smaller sock. Socks should act as a second skin helping regulate heat and moisture. As such, a proper fitting sock shouldn't keep reminding you that you are wearing socks after you put them on.

Compression socks can help, especially for diabetics, but you should consult a medical professional before long-term use of compression socks. Heavy use of compression socks has been known to cause long-term injury.

|MATERIAL|PROS|CONS|
|:-|:-|:-|
|**Cotton**|**Cotton socks dry quicker** than most other fabrics.|Cotton tends to feel softer than other materials.|
|**Polyester**|**Very lightweight**.|Higher **fade resistance** compared to natural fabrics.|
|**Wool**|**Natural** fabric.|**Breathable, good insulator of heat and cold**.|
|**Merino Wool**|**Soft and comfortable**.|**Forms to the foot**.|
|**Bamboo**|**Very soft**.|**Environmentally friendly**.|

**^(\*PLEASE CONSULT YOUR PHYSICIAN WHEN CHOOSING APPROPRIATE SOCKS AS A DIABETIC.)**

# RECOMMENDED SHOE BRANDS AND GENERAL NOTES

[**INTERNATIONAL MEN AND WOMENS SHOE SIZE CONVERSION TABLE**](https://i.pinimg.com/originals/3a/f0/09/3af00948978879de88e56c139c31d93f.jpg)

|**BRAND**|GENERAL SIZING|NOTES|
|:-|:-|:-|
|[Birkenstock](https://www.birkenstock.com/us/professional/)|**W:** 4-12.5 (Offers Half Sizes) **M:** 6-15.5 (Offers Half Sizes)|Offers **Regular/Wide** and **Medium/Narrow** fittings. Offers **both men's and women's** work shoes. Hospitality shoes are **exclusively Clog-style**. ***Cheapest price is $79.95***\*|
|[Crocs for Work](https://www.crocs.com/c/shop-by/activity/work-shoes)|**W:** 4-12 (No Half Sizes) **M:** 4-17 (No Half Sizes)|*Does not state if different sizes come in different fittings such as wide or narrow.* Offers **both men's and women's** work shoes. Styles come in **both traditional shoe and Croc** style. ***Cheapest price is $39.99***\*|
|[Shoes for Crews](https://www.shoesforcrews.com/)|**W:** 2.5-11.5 (Offers Half Sizes) 12-16 (No Half Sizes) **M:** 3.5-11.5 (Offers Half Sizes) 12-17 (No Half Sizes)|Offers **Regular** and **Wide** fittings. Offers **both men's and women's** work shoes. Shoes come in **different styles**. ***Cheapest price is $21.25***\*|
|[Redwings](https://www.redwingshoes.com/)|**W:** No Clear Sizing **M:** No Clear Sizing|Offers **Regular** and **Wide** fittings. Offers **both men's and women's** work shoes. Shoes come in **different styles**. ***Pricing is unclear.***\*|
|[New Balance](https://www.newbalance.com/men/shoes/work-shoes/)|**W:** 5-10.5 (Offers Half Sizes) 11-13 (No Half Sizes) **M:** 7-12.5 (Offers Half Sizes) 13-18 (No Half Sizes)|Offers **Standard, Wide, Extra Wide, and Extra Extra Wide fittings for men** and **Standard, Wide, and Extra Wide for women**. Offers **both men's and women's** work shoes. Shoes come in **different styles**. ***Cheapest price is $94.99***\*|
|[San Antonio Shoemakers (SAS)](https://www.sasshoes.com/)|**W:** 4-12.5 (Offers Half Sizes) 13 (No Half Sizes) **M:** 6-15.5 (Offers Half Sizes) 16 (No Half Sizes)|Offers **Slim, Narrow, Medium, Wide, Extra Wide, Extra Extra Wide fittings for both men and women.** Offers **both men's and women's** work shoes. Shoes come in **different styles**. ***Cheapest price is $139.99***\*|
|[Skechers](https://www.skechers.com/men/shoes/work-safety/)|**W:** 5-9.5 (Offers Half Sizes) 10-13 (No Half Sizes) **M:** 5-11.5 (Offers Half Sizes) 12-16 (No Half Sizes)|Offers **Medium and Wide fittings for both men and women**. Offers **both men's and women's** work shoes. Shoes come in **different styles**. ***Cheapest price is $49.00***\*|
|[Klogs](https://klogsfootwear.com/hospitality-collection-1/)|**W:** 6-6.5 (Offers Half Sizes) 5-15 (No Half Sizes) **M:** 5-15 (No Half Sizes) 10.5|11.5 (Offers Half Sizes)|
|[Dansko](https://www.dansko.com/womens-shoes-clogs)|W: 4.5-15 (Offers Half Sizes) M: 4.5-15 (Offers Half Sizes)|Offers Narrow, **Medium, and, Wide fittings for both men and women**. Offers **both men's and women's** work shoes. Shoes come in **different styles**. ***Cheapest price is $125.00***\*|
|[Keen](https://www.keenfootwear.com/work/)|W: 5-9.5 (Offers Half Sizes) 10-11 (No Half Sizes) M: 7-11.5 (Offers Half Sizes) 13-14 (No Half Sizes)|Offers **Medium and Wide fittings for both men and women**. Offers **both men's and women's** work shoes. Shoes come in **different styles**. ***Cheapest price is $140.00***\*|
|[Snibbs](https://snibbs.co/)|W: 5-10.5 (Offers Half Sizes) 11 (No Half Sizes) M: 7-11.5 (Offers Half Sizes) 12-15 (No Half Sizes)|Unclear on types of fittings offered. Offers **both men's and women's** work shoes. Shoes come in **different styles**. ***Cheapest price is $135.00***\*|
|[Blundstone](https://www.blundstone.com/mens-work-boots)|W: 6-8 (No Half Sizes) 9-12.5 (Offers Half Sizes) 13-17 (No Half Sizes) M: 4-6 (No Half Sizes) 7-11.5 (Offers Half Sizes) 12-15 (No Half Sizes)|Unclear on types of fittings offered. Offers **both men's and women's** work shoes. Shoes come in **different styles**. ***Cheapest price is $224.95***\*|
|[Alegria](https://alegriashoes.com/)|W: 5-11.5 (Offers Half Sizes) 12-14 (No Half Sizes)|Unclear on types of fittings offered. Offers **primarily women's shoes**. Shoes come in **different styles**. ***Cheapest price is $98.95***\*|
|[Timberland](https://www.timberland.com/timberlandpro.html)|W: 3-4 (No Half Sizes) 5-9.5 (Offers Half Sizes) 11-15 (No Half Sizes) M: 3-11.5 (Offers Half Sizes) 12-15 (No Half Sizes)|Unclear on types of fittings offered. Offers **both men's and women's** work shoes. Shoes come in **different styles**. ***Cheapest price is $110.00***\*|
|[Xelero](https://www.xeleroshoes.com/)|W: 5-10.5 (Offers Half Sizes) 11-12 (No Half Sizes) M: 7-12.5 (Offers Half Sizes) 13-14 (No Half Sizes)|Unclear on types of fittings offered. Offers **both men's and women's** work shoes. Shoes come in **different styles**. ***Cheapest price is $139.99***\*|

**^(\*PRICING IS BASED OFF OF THE CHEAPEST NON-SALE PRICE LISTED ON THE STORE WEBSITE AS OF AUGUST 9th, 2022. IF YOU BELIEVE A PRICE CHANGE HAS OCCURRED OR YOU WISH TO CHANGE THE PRICE LISTED, SEND ME A PRIVATE MESSAGE HERE ON REDDIT AND I AM MORE THAN HAPPY TO ADJUST THE PRICE ACCORDINGLY.)**

**^(EDIT: VERSION 2 OF GUIDE. I WILL CONTINUE TO KEEP THE GUIDE UPDATED TO THE BEST OF MY ABILITY, IF YOU HAVE A CHANGE TO RECOMMEND OR HAVE QUESTIONS ABOUT THE GUIDE OR RELATING MATERIAL, PLEASE FEEL FREE TO SEND ME A PRIVATE MESSAGE.)**

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iikssyf] (score 24, diepte 0) Amazing write up! I would like to add Keens, which used to be a hiking shoe but now make excellent non skid kitchen shoes. The last time I ordered from them the shoes ran small in womens sizes.  But I’ve been alternating two pairs of oxfords for 3 years. I can’t wear clogs because of a history of plantar’s fasciitis but sturdy lace-up oxfords work for me. Bonus is they can work for FOH.
[iikttlf] (score 15, diepte 0) Just so you know — Dansko was the brand used by a European company called [Sanita](https://www.sanita.com/) in the US market. They sold the Dansko brand to the Chinese and now Danskos are made in China.

If you want the European manufactured clog, you want to buy Sanita.
[iikt7n7] (score 14, diepte 1 OP) Thank you! I’ve spent a very long time putting this all together and I’ll release a free eBook sometime before the end of the year that is my original 90 page PDF + a years worth of interviews and research. But people are always asking on the subs and the info in this guide is kind of like the crash course of the knowledge on the topic I’ve accumulated. :)
(71 reacties met lagere score weggelaten)

=== THREAD 41k8r6 ===
SUBREDDIT: r/running
DATUM: 2016-01-18  SCORE: 14  REACTIES: 65
TITEL: plantar fasciitis - massaging with a ball, but how long till you saw recovery? complete recovery?
POST (source_id=post):
I was searching past threads and apparently using a golf/tennis/baseball will do wonders. But is that a temporary fix or is there a way to like completely undo what  plantar fasciitis has done to my feet?

I haven't ran in like 3 weeks and i'm quite annoyed at the idea of losing progress and having to work on getting my respiratory system/endurance back to where it was. (My furthest was 6 miles, I don't plan on going over 7).

any other exercises that you enjoy doing to keep your heart rate/respiratory system up and maintained while waiting for the feet to feel better? And no I sadly have no access to a pool.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cz30iil] (score 5, diepte 0) I don't have any first-hand experience, but just posting to say, be careful.  Not what you want to hear, but my mother has had chronic plantar fasciitis for a couple decades shortly after taking up running.  Most cases aren't chronic, but you only have one pair of feet, so take care of them!

As to one of your questions, I would advocate cycling.  It has been a great benefit to my running endurance and easier on the body.
[cz34bqs] (score 5, diepte 1) I'll add to this: freeze the golf ball before hand. Works like a charm.
[cz3bmv7] (score 4, diepte 2) I personally like the stand on it method.
[cz34igq] (score 4, diepte 0) Mine took a long time to heal, probably around 3 months. Rolling on a golf ball didn't seem to make much difference in my case. I would suggest no rushing back to running until it feels 100%
[cz3ac45] (score 4, diepte 0) My problem stems from my calves.  If I press on the inside of my calf just behind my shin I can feel the pain all the way down to my feet.  I focus more work on them than on my feet. I changed a lot of how I train and recover.  I use the foam roller before running and mix in static stretching and warm up runs.  I have a hard stick roller for after my runs and then bought a small TENS machine that I put on my calves.  Ice baths for my legs after long runs.  I'm not 18 anymore so I can't expect my body to recover like it used to without a lot of help.  After my Ultra I had to take 2 months off completely, start training from scratch to build back up and didn't get recovery for a year.  Best of luck on recovery.
[cz3kuo7] (score 4, diepte 0) I literally just had plantars, I had it for about 4 days. What I did was used a tennis ball on my arch for 2 mins 3 times a day and I put no pressure on my foot, walked with crutches. I also would straight my foot multiple times a day to a 90 degree angle to stretch out the fibers. After 4 days of doing that I was all good on the fifth day, I did continue to massage it though to just make sure and on the sixth I went for a light jog focusing on striking on my forefoot. Hope you recover quick Plantar Fasciitis sucks
[cz36zcw] (score 3, diepte 1 OP) eh hopefully it doesn't have to come to a doc visit but thanks for the input! agh! hope it doesn't happen to either of us again for that matter.
how did PF start up for you? was it just too much distance or bad posture
[cz31uqz] (score 3, diepte 0) I wouldn't call it a temporary fix.  It can help break up some of the scar tissue in the foot and alleviate the pain.  Any time I start to get pain in that area, I'll use a golf ball and it takes care of it pretty quickly.
[cz3d4ke] (score 3, diepte 0) 15 months.

Biggest thing I can tell you: work to get better. For awhile, I assumed resting would fix it and did not run. 

Stretch, strength, ice, massage. Repeat.
[cz3jtkp] (score 3, diepte 0) I've had it in my right foot since October.  I woke up one morning and couldn't really walk, it was pretty painful.  After about two weeks it was 80% better.  After about a month it was 90% better.  After two months it was 95% better.  Now at almost 3 months it's 98% with just the slightest twinge every now and then.  So I saw a lot of improvement early on but the full recovery was pretty drawn out.  I've been running anyway since about 3 weeks after it happened.  I tried it and found that running didn't seem to make it any worse that I could tell, so I kept running, maybe 15 mpw since it happened.  Also riding a bicycle to make up for how much my running slacked off.  I also focused more on strength training but I found that lunges make my foot worse so I don't do those.  

Good luck with your feet!  It will get better just be patient and if something hurts stop doing it!
[cz3mgfv] (score 3, diepte 1 OP) nice great to hear thanks !
[cz33xe4] (score 2, diepte 1 OP) that's a good point to bring up! thanks I'll have to look back into Cycling
and ah sorry about your mom having to deal with a chronic version of this! wish her the best- and thanks for the input!
[cz31p6u] (score 2, diepte 0) > I haven't ran in like 3 weeks and i'm quite annoyed at the idea of losing progress and having to work on getting my respiratory system/endurance back to where it was.

I know that feeling! I got plantar fasciitis in September and it was extremely frustrating to not know what to expect in terms of recovery. There is tons of rather conflicting info out there on how to treat it and its prognosis. I wound up needing to take about 6 weeks completely off (like 3 rounds of taking two weeks off and then slowly starting back up and re-injuring it). Since mid-October I've been able to ramp my training back up very slowly without any problems, but am still a bit disappointed about the fitness I lost. 

I did mention the PF to my (marathoner) doctor at my annual physical, and she mentioned that insoles might be helpful if I had flat feet-- I don't, so she said just rest and a slow return to running would be best. Might be worth getting checked out by a doc if it's still troubling you in a month or so.
[cz33vik] (score 2, diepte 1 OP) thanks will do, any particular method of rolling the ball under your feet that helps?
[cz34gz5] (score 2, diepte 2) Nope, just at my desk at work and rolled my foot all over the ball.  Just make sure you use a lot of pressure (ie, it should kind of hurt).
[cz35i8o] (score 2, diepte 1) **Due North Foot Rubz Foot Hand and Back Massage Ball Green**  (9%  price drop)

||||
--:|:--|:--
Current|$5.49|Amazon (New)
High|$7.00|Amazon (New)
Low|$3.59|Amazon (New)
|Average|$6.03|30 Day

[Price History Chart and Sales Rank](http://i.imgur.com/yWZttBD.png)

**Due North Foot Rubz Foot Massage Roller** 

||||
--:|:--|:--
Current|$11.89|Amazon (New)
High|$11.99|Amazon (New)
Low|$10.20|Amazon (New)
|Average|$11.92|30 Day

[Price History Chart and Sales Rank](http://i.imgur.com/JrvhB7R.png) | [FAQ](http://www.reddit.com/r/PriceZombie/wiki/index)
[cz36ena] (score 2, diepte 1 OP) do you think switching to barefoot running would have helped?
thanks for the links will look into!
[cz3be6o] (score 1, diepte 2) As far as I can tell it was about pushing my speed too fast on a long run. I had worked my weekly long run up to 12 miles, so I decided I was ready to do a half marathon distance as my long run one week. But it was the first time in months the weather had gotten cool enough for me to really run comfortably, and I was so psyched about achieving 13.1 miles for the first time that I kind of went all out on the second half of the run. The funny thing is it was an awesome run, I was so happy with myself and felt great during it, and then about an hour later I couldn't walk on one heel because of the pain :-/  

I've heard that bad form/weaknesses up the chain can definitely impact it though; foam rolling my calves and thighs seems to have helped and my doc recommended calf strengthening once symptoms have abated. Hang in there, hope you're feeling back to normal soon!
[cz3cquh] (score 1, diepte 3) Similar experience here. It was a longer fast run that have me pf. I am still recovering after about 3 months. I think it's healing. I still run and it still hurts in the morning but not as much as it did before. 

I am doing the strassburg sock, rolling, and stretching calves before and after run. Rotating between shoes with support and altra(brand of minimalist shoes). 

I took 14 days off and it didn't help at all.
[cz3jgwj] (score 1, diepte 3 OP) haha very nice, very ambitious of you to jump up to a 13.1 mile in one day.  But yeah that feeling of ugh, I did so well now I have to sit on the sidelines.

thank you!
[cz35ccg] (score 1, diepte 3 OP) ah thanks!
[cz3jecr] (score 1, diepte 3 OP) nice
[cz36zk5] (score 1, diepte 1 OP) thanks!
[cz3dr9y] (score 1, diepte 1) Before I got PF I couldn't fathom someone saying 3 months was a quick recovery. Mine lingered for 2 years and has just gone away in the last 6 months. 

My advice is the same as everyone else in this thread, take it easy and don't push yourself. If you feel like you can run 5 run 2 instead.
[cz3e3jq] (score 1, diepte 2) After mine went away, I've now developed something _else_ wrong with my foot which has been lingering for ~4 months thus far. Even walking can drop down to a limp at the moment. 

Stupid feet, one have one job...
[cz35htm] (score 1, diepte 0) PF struck in late September. Tried to fight through it for two weeks and had to give in. Tried to just stay off of it as much as I could and added more cycling through October and into Nov. It seemed to get worse. Early December I started rolling it and being more careful to stretch it every day, and as of early Jan I'm working back up the running.

I believe my old shoes/insoles were largely to blame. Instant relief when I changed. I was reluctant to do so as they were still in pretty good shape but the slight loss of arch support wrecked me, as far as I can tell.

This http://smile.amazon.com/gp/product/B002QEY6NK  and this:  http://smile.amazon.com/gp/product/B00T69CWFW  are must haves. The first week of using them a few times a day was pretty rough but after a few weeks it's night and day difference.
[cz36rc1] (score 1, diepte 2) For me personally no. I say that because of how I felt walking barefoot in the mornings on the more painful days really, and how much better it felt to put temporary dr scholls inserts into my "street" shoes during this loooong recovery. I feel much better with a tight shoe that has solid arch support.
[cz371m3] (score 1, diepte 3 OP) I could stand for walking, but Idk how arch support is for running. I was using Nike frees originally 

but will do!
[cz3bppf] (score 1, diepte 2) Personally, my plantar issues are the lowest when I'm in more barefoot shoes in my day to day life. 
These were a god send when I was marathon training:

http://www.sanuk.com/womens-sandals/yoga-sling-2/SWS10001.html?dwvar_SWS10001_color=GRY#start=1&cgid=women-sandals-yoga-mat
[cz3csit] (score 1, diepte 3 OP) oooh fancy, they look comfy- thanks! and how long did it take you to get ouf that?
[cz35whn] (score 1, diepte 0) Currently have slight PF in left foot. Weirdly though, I started feeling it after a lifting session in the gym wearing converse, maybe that was it? I have no prior exp with PF (started running just a couple of months ago), but I keep my fitness up with cycling and swimming.
[cz3732q] (score 1, diepte 0) I had a similar experience to you. Started running from scratch in Dec 2014, got to 10Km distance by May, then got PF bad. I think from adding some sprints in - over stretched the arch.

Tried desperately to keep some fitness, but mine took three months to heal properly despite trying everything I could and buying several strapping devices. I don’t think anything sped up recovery.

Have been running again for two months and am back to previous form.

IMO there's pretty much bugger all you can do to make it heal. Its incredibly frustrating, I feel your annoyance.
[cz39xgn] (score 1, diepte 1 OP) blahh :P sorry to hear you had to deal with that too.
was it easy to catch up and get back into your old time/distance after 3 months?
[cz3s0hj] (score 1, diepte 2) Yeah the fitness comes back if you work hard obviously. I just found it annoying to have to build up again. All those hard earned miles lost.
[cz38ola] (score 1, diepte 0) Best of luck with recovery Dom!
[cz39wdv] (score 1, diepte 1 OP) thanks!
[cz3bwkv] (score 1, diepte 1 OP) thanks!
[cz3asj6] (score 1, diepte 0) I got rid of most of my PF with one of those sleeping boots, pretty cheap ($20?) on Amazon.
[cz3bx0g] (score 1, diepte 1 OP) interesting looking into it!
[cz3cqb9] (score 1, diepte 2) Ah, night splint is what they're called. Worked great for my wife's plantar as well.
[cz3csoa] (score 1, diepte 3 OP) thanks!
[cz3bkg2] (score 1, diepte 0) I used to get it alot when I switched to minimalist shoes. My feet weren't strong enough to withstand the shock. That and I was too far forward on my strike. Have you ever heard of the 'drunken flamingo' stretch? It's turned my feet around for the better. Just stand on one foot, other foot raised  up a bit, and let yourself wobble a little. The muscles and tendons in your feet'll being tensing and flexing as they stabilize you and get get a nice work out to boot. Switch feet. Close your eyes for hard mode.
[cz3jfet] (score 1, diepte 1 OP) > drunken flamingo' stretch?

interesting, thanks i'll look into it! :) 
haha close my eyes for hard mode
[cz3bmdw] (score 1, diepte 0) I do several things to try to ward off/heal plantar flair ups:

1. tennis or lacrosse ball under my feet
2. exercises to break up the plantar-- take a towel and use just your toes to bunch it up
3. Foam roll my calves
4. Get professional massages as needed

As for exercise--biking, yoga, or dance can be a nice alternative.
[cz3jeow] (score 1, diepte 1 OP) thanks!
[cz3bpe7] (score 1, diepte 0) I (25M, if that matters) struggled with PF the last half year (there was always a slight inkling that something wasn't 100% for over a year before it got really bad) and I'm finally getting over it.

Rest (not running) drove me crazy. I tried walking and cycling, but I never felt like I was getting a good enough workout and walking still irritated my feet. After about a month of that, I saw a doctor.

My primary physician offered little comfort. He pretty much gave me the "usual" solutions (rest and a tennis ball) but offered to refer me to a podiatrist. I took the referral. The podiatrist taped my feet using the low dye method, suggesting that pain would reduce by at least 50%. The tape couldn't get wet (I showered with bags on my feet, which was a bit annoying) but lasted for about a week. It pretty much cured my left foot but my right was still bothering me. Progress! but you need two feet to run...

I went back about a week later to get taped again. By then, my insurance approved my orthotics so I got casted for those. Unfortunately, the second week of tape didn't really help. 

Now it's Christmas time, so I'm away visiting family. During this time, still with a hurt foot, I pretty much decided that when I get back I'm going to get a shot to stop the pain and let me get back to running. Screw it, I can't wait any longer! I'll pick up my orthotics and schedule an appointment with a nurse. 

But when I went in, the nurse told me to give the orthotics a couple weeks before coming back. Let me tell you, I was absolutely amazed how much the orthotics helped! The new orthotics along with me getting a lot better about [stretching](http://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/media/medical/hw/hwkb17_077.jpg) every time I was in the shower (morning and then after PM workout) have eliminated almost all of the pain!

So now I'm back out there. I'm slower than I was, but I'm just happy to be running. See a doctor if you can. Hopefully the taping method helps you entirely and you're back out there in two weeks. If not, maybe the orthotics will help.

**TL;DR: See a doctor (podiatrist) if you can. I wish I did sooner.**
[cz3cucc] (score 1, diepte 1 OP) thank you ! glad it all worked out for you! haha :)
[cz3dlr7] (score 1, diepte 0) Mine started bothering me a few years ago and a friend recommended gel heel cups to put in my shoes. It worked for me. They're about $8 at a pharmacy. 

Plantar is one of those things where different things work for different people. The $8 heel cups are a lot cheaper than the $25 sock. 

Also, freeze a water bottle and roll out on that, too. 

I've heard that some plantar pain can stem from weak glutes and core. Might help pass the time being able to get some cross training and strengthening in addition to what others have suggested.
[cz3ehtf] (score 1, diepte 1 OP) interesting, thank you for the insight! :)
[cz3gxlx] (score 1, diepte 2) I hope you feel better soon!!
[cz3hzec] (score 1, diepte 3 OP) thanks :D
[cz3h3ec] (score 1, diepte 2) The heel cups worked for me also.
[cz3hyu5] (score 1, diepte 3 OP) interesting, thanks! :)
[cz3hlul] (score 1, diepte 0) The golf ball has been my best friend. It has been the only way that I could possibly run - I roll the golf ball after every run and every time it feels tight. I don't know that I'd be able to continue running without it. My PF came after surgery to repair a tendon and will likely never go away so my case is probably not what you wanted to hear but at least it's a chronic case that is not stopping me from running!
[cz3jux3] (score 1, diepte 1 OP) thanks!
[cz3misu] (score 1, diepte 1 OP) thanks! :)
[cz3lvmx] (score 1, diepte 0) When you sleep, you will want your foot and ankle to be at a 90 degree angle
[cz3mezj] (score 1, diepte 1 OP) like toes pointed up? k thanks!
[cz3mj16] (score 1, diepte 2) Yep! Had to sleep with a cast for months and this is basically what it did. Your feet will want to curl at night according to the podiatrist I saw
[cz3mwyv] (score 1, diepte 3 OP) gotcha! :)
[cz3nkm6] (score 1, diepte 0) I had it for about 4 months, tried the golf ball, another ball with spikes, the splints you use to sleep and exercises. Finally, I got active release therapy and they also had this metal thing to scrape my sole. It was incredibly painful, but the plantar fasciitis just went away after a week.
[cz3noqb] (score 1, diepte 1 OP) :o
thanks!
[cz3no1a] (score 1, diepte 0) PF struck me about 3 months ago- I was feeling great on a run and ran 13 miles when I should have only done 6. Stupid.

Saw a sports doctor about it- gave me a few stretches to try, nothing too different than you'd see online, but recommended NOT stretching cold. As in, jog a little bit and warm up before doing stretches. I also got some Dr. Scholl's Active inserts for running, and other heel cups for everyday use. Can run just as good as ever, and actually completed my first Half in 1:44 yesterday. Most noticeable in the morning and when I'm walking barefoot. The effects haven't gone away, but it's manageable. Feels better when I run actually; first mile or two is tight but then I stretch and loosen up, and it's smooth sailing.
[cz3nra8] (score 1, diepte 1 OP) thanks for the input i'll look into the soles.
but I mean will it matter if i'm flat footed?
[cz46pyc] (score 1, diepte 1 OP) no I haven't but I shall strongly consider that, thanks!
(1 reacties met lagere score weggelaten)

=== THREAD yhi1dx ===
SUBREDDIT: r/cna
DATUM: 2022-10-30  SCORE: 33  REACTIES: 64
TITEL: Feet and legs so swollen and tender after work that I can’t walk.
POST (source_id=post):
How do you guys manage the pains and aches? I wear wool socks to avoid blisters and extra wide shoes because my feet are very wide. I am absolutely useless after a shift, everything hurts so much.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iueooz8] (score 77, diepte 0) Do regular cardio.
[iudyrrs] (score 41, diepte 0) I bought Doc Miller XL calf sleeves 20-30mmhg. They’re $18
[iuf6ent] (score 39, diepte 1) This should have all the upvotes. Everything else is a bandaid. This solves the underlying problem. 

Would add, watch diet and work towards a healthy weight if applicable
[iufgh8f] (score 23, diepte 1) I used to feel dead after my 3rd shift... I was overweight.

This year I hit the gym, lost 40lbs, and have started jogging.

I just finished a run of 8 12s in a row and felt pretty fine
[iuffhrq] (score 19, diepte 2) I found it really helpful to also do calf raises and squats during a shift. It takes 20 seconds to do 20 calf raises and really get fluid moving. Let your muscles be your natural PCDs!
[iudvxo6] (score 16, diepte 0) I switched to Crocs about 8 years ago. I worked in kitchens for long hours on hard floors sometimes standing in one spot for a long time and sometimes running around. I left work one day and had to take my sneakers off in the parking lot to wobble to my car and I cried when I got in because my feet hurt so bad. Bought a pair of crocs and have never looked back. I wear them 5 days a week as a CNA and on my days off when I’m running errands. (I have set work ones and set home ones.) I wear the Baya ones at work because the holes aren’t cut out of the clog in the front so there’s more coverage.
[iufjf9o] (score 14, diepte 3) Yes! Not nearly enough people realize that muscle contraction is responsible for a ton of venous blood flow
[iue0o2o] (score 13, diepte 0) Might look into orthopedic insoles as well, you can go to any drug store usually and find the Dr scholls machine that will map your foot. And recommend the right insole for you.
[iudy9w1] (score 11, diepte 2) You may find compression socks or sleeves helpful too. I don’t like them because I already sweat a ton at work and don’t want any extra layers but I work with others who wear them. I freeze a water bottle with water and roll my foot on it as well after long days, you can do the same with a tennis ball. Helps release tension. Good luck!!
[iuekvj9] (score 11, diepte 1 OP) I’m going to get some. They look great and have a good range of sizes. Thank you!
[iue6grc] (score 9, diepte 0) I wear compression socks and love my crocs but be careful bc they're dangerous around water spills 😆 I've definitely busted my ass once or twice from slipping. I have a pair of Danskos that actually are good too but I like the crocs more
[iuel2t2] (score 9, diepte 0) Compression socks are amazing!!! Also, I would recommend ASICS! They are very comfortable and the kayano ASICS are great for people with a wider foot.

They may be a little pricy, but you can get 40% off for being a healthcare worker! You just have to submit proof of employment
[iudxl24] (score 7, diepte 1 OP) I will have to try crocs. I’ve definitely cried from the pain and wobbled around. I just feel like there has to be a better way and I don’t want to be lazy at work to achieve it. Thank you.
[iugrl9i] (score 6, diepte 2 OP) Yes, I’m pretty heavy right now. I’ve always pushed myself to
The point of pain at my jobs but it’s been unbearable with this new job, probably because I weigh the most I ever have. Sounds like losing weight is the real solution. 

Happy for your with your weight loss and fitness journey.
[iuepng1] (score 5, diepte 2) Compression socks with the bistro style crocs, plus hanging my legs up on the couch while I stretch my arms is amazing
[iue6pe9] (score 5, diepte 0) Wear compression hose.  Make sure you buy really good work shoes.
[iuf1cwo] (score 5, diepte 0) Compression socks and sketcher go walks. Feel like an old lady tho I’m 21 😂
[iuf4nyv] (score 5, diepte 0) I wear Hoka's Bondi 8s and have zero problems. I've recently been trying out compression socks as well.
[iuelluh] (score 3, diepte 1 OP) I haven’t seen one of those machines in my area yet. But I will start calling around. It’s something I’ve always wanted to try. Thank you!
[iuemkm8] (score 3, diepte 2) Really call anywhere with an in store pharmacy.
[iuek6ao] (score 3, diepte 2) Those are good. They're what my orthopedist gave me with my inserts.  What's next is making sure your feet have the right support though.   You may have high arches or other such things going on.  If you can go to one of those foot support stores to get a set of inserts that suit your foot type.   And like I said, get compression hose. You can wear them with your wool socks if you want.
[iuelq59] (score 3, diepte 0) crocs and compression socks 😌
[iugrflz] (score 3, diepte 1 OP) My kryptonite. Guess I need to get over it.
[iuflj2i] (score 3, diepte 0) I feel you. I am currently 18 hours in to my 24 hour shift and my feet are K I L L I N G me🥲
[iue50rk] (score 2, diepte 4) Crocs are great for sweaty feet. Mine still get sweaty but with the holes on top if I walk fast enough I can feel the breeze come through. And lord knows I’m walking fast unless I’m charting or peeing.
[iuggkkr] (score 2, diepte 2) I tried the as-seen-on-tv "Walk-fit" insoles, they come with 3 levels of inserts and although they felt odd at first.  Sorta like I was walking on smooth stones under my arches. I couldn't believe the difference at the end of a 12hour shift. So much better.

That was 20 plus years ago and were much cheaper then the dr Sholes inserts from the machine. I use them in all my shoes,boots etc. Even my hip pain went away.
[iueldhh] (score 2, diepte 1 OP) Oh my goodness. My clumsy behind would definitely fall as well 😂 I’m going to get some crocs on my next paycheck. Thank you!
[iuejq30] (score 2, diepte 1 OP) I have been wearing new balance shoes. I don’t know if those are considered good. They aren’t cheap tho
[iuekfcp] (score 2, diepte 3 OP) Okay, I will try that next. Thank you!
[iui92pv] (score 2, diepte 2) Loved my New Balance when I was doing floor nursing, but I found getting a rotation going for shoes, being religious with wearing compression socks, and minding the cardio all helped me out.  I’d suggest doing the New Balance one day, Crocs or Danskos the next, etc.  I found it didn’t matter how great my shoes were if I was wearing the same ones every day.  And it sounds ridiculous that you won’t be as tired if you work out more, but getting myself into a bit better condition and dropping a few pounds made a HUGE difference.  Don’t be a caregiver that puts yourself last - we are all guilty of it from time to time! ❤️
[iuelrek] (score 2, diepte 1 OP) Thank you! 40% off is amazing and Thank you for the wide foot tip ♥️
[iug13ib] (score 2, diepte 2) Altra’s are also great for wide feet. Totally made my 12 hour shifts easier. And I think they also have a pretty nice discount through ID Me.
[iuhmeqj] (score 2, diepte 2) Way to go!
[iui3gqv] (score 2, diepte 2) Start small at first. Go light on your days off, then build up. Sounds counterintuitive when your legs are screaming, but running or even brisk walking really does help. Elevate your legs after work (like 2 or 3 pillows if you don't want to throw them up against a wall).
[iug6uak] (score 2, diepte 1) Are you talking about those new Skechers go walk? I’ve been looking at those online. Have you had yours long and how are they holding up? The shoes I wear are the absolute worst for the job. I seriously need to switch.
[iuhil5z] (score 2, diepte 2) I bought an older gen. I can see them lasting for a shorter amount of time than regular shoes but I only wear them in the ward so I don’t think they’ll wear that much. Totally worth the price. Before I started compression socks and sketchers my legs and feet would kill. Now I literally don’t feel a thing. Now my back pain just feels even stronger :))
[iugre27] (score 2, diepte 1 OP) I’m sorry girl 😢 I hope you get some good rest afterwards
[iufna2j] (score 2, diepte 0) Compression socks and good sneakers will help you out tremendously!!!
[iufp82m] (score 2, diepte 0) Compression socks are a MUST! I like the brand Sockwell. They're a little pricey ($30 per pair) but they last for years even with constant use and they keep their compression even after hundreds of washes.
[iug1nco] (score 2, diepte 0) Crocs and compression stockings!
[iug82e8] (score 2, diepte 0) "For substantial health benefts, adults should do at least **150 minutes** (2 hours and 30 minutes) to **300 minutes** (5 hours) a week of **moderate-intensity**, or 75 minutes (1 hour and 15 minutes) to 150 minutes (2 hours and 30 minutes) a week of vigorous-intensity aerobic physical activity, or an equivalent combination of moderate- and vigorous-intensity aerobic activity. Preferably, aerobic activity should be spread throughout the week.

Adults should also do **muscle-strengthening activities** of moderate or greater intensity and that involve all major muscle groups on **2 or more days a week**, as these activities provide additional health benefits."

\-Physical Health Activity Guidelines for Americans: https://health.gov/sites/default/files/2019-09/Physical\_Activity\_Guidelines\_2nd\_edition.pdf
[iugnktp] (score 2, diepte 0) Pro Compression “marathon” socks. 
Saved me. 
My fat little cankles would collect after every 12 hour shift. I tried sleeves but they didn’t do the trick. 
It was recommended to me after a knee surgery by my physical therapists to wear knee high socks. Like magic the pain in my surgery knee and all the swelling was better.
[iuguljc] (score 2, diepte 0) Start to see a massage therapist regularly
[iuh48jd] (score 2, diepte 0) Try using compression socks and eating less salt.
[iuh6i1z] (score 2, diepte 0) Compression socks + look into r/BarefootRunning shoes. 

[Going to repost so I don't have to say the same thing over.](https://www.reddit.com/r/AskMenOver30/comments/yatkws/do_you_have_any_suggestions_for_walking_shoes/iteti1q) 

TLDR - Barefoot shoes are actually great, someone was able to actually walk I think 70k+ steps a day for a week or month or so, need to still watch that video. 

For me walking my measly ~15k steps 3 times a week - as my only cardio because I'm a couch potato outside of work right now - I am more tired mentally and my back hurts after a shift. 

Have never complained about my feet, legs, lower back in my three or four years wearing barefoot shoes. 

Look at older people's feet if you're in LTC, you will eventually have their same gait, and foot shape as you continue to wear normal shoes.
[iuhhmrm] (score 2, diepte 0) Tylenol 8hr Pain Reliever before work or at lunch on shift.
[iuhhxt8] (score 2, diepte 1 OP) Had no idea that there was an extended release Tylenol. Sounds amazing. Thank you
[iuhkp7l] (score 2, diepte 2) You're welcome! I just discovered it a couple months ago myself and it has helped soooo much. I no longer hobble around stiffly due to achy joints or try to "walk light" 😂 to ease the painful pressure on my soles. 
I compared both labels and the muscles aches and pain and arthritis types appear to be the same thing except arthritis costs slightly more.
[iuht5kl] (score 2, diepte 3 OP) Yeah that’s very cool I think I’m a fan for life of that one. What a gem! I’m happy to hear that it brought you some much needed relief. Thank you for sharing what has helped you. 💖
[iuiiz0i] (score 2, diepte 0) Get in good shape. Honestly, make fitness your first priority. However I realize you can't do that until you feel way less sore/in pain. In the mean time, I suggest....   
Cutting out processed food, high salt food, high fat food especially red meat, cheese/dairy as it is proven to cause inflammation, get your labs drawn and see what your B12 and D are doing: low levels of both of these can cause joint pain. Take a magnesium supplement. Stay HYDRATED (90 oz a day). Get adequate rest, 7-8 hrs ideally. Take hot epsom salt baths, have a partner massage you or get a regular professional massage. Do YOGA and stretch before and after shifts. Wear compression socks and get good shoes, I reccommend HOKAS.  
I was in the same boat; my C-Reactive Protein level and homocystine levels were both high and I was so much in pain after starting this job. After doing everything above that I mentioned, they have dropped 6 months later and I'm usually about a level 2 in pain versus an 8. Hope that helps!
[iue1491] (score 1, diepte 3 OP) Frozen water bottle is a great idea! I will have to try the tennis ball too. I tried compression socks but had to switch to wool socks because my feet sweat and I’ll get blisters without them.
[iuj5s8u] (score 1, diepte 3) That’s awesome! Having custom made New Balance was recommended to me by a dr, but I don’t see myself shelling out the $$$ for that. The GoWalk shoes looks super comfortable. I will probably bite the bullet and get some in a couple of weeks.
[iuj7co7] (score 1, diepte 4) They are from heaven! The soles are great, and easily machine washed:) the cons r looking like an old person
[iufw0ts] (score 1, diepte 0) Compression socks, arch support, and shoes with a thicker sole. I like Skechers with a sole that's at least an inch thick. Something about the extra padding helps keep my feet from feeling so busted. I've also learned that it's okay to sit down and get off of your feet. And if you work at a facility that makes you feel awkward/uncomfortable for needing a 5 minute breather, it's time to go. You'll always be able to get work as a CNA.
[iugj0zr] (score 1, diepte 0) Support socks. Every day.
[iugm76s] (score 1, diepte 0) Regular cardio and Ted hose - also bring a change of socks and find supportive shoes
[iugo6rh] (score 1, diepte 0) Start running.

I wear Brooks for jogging, but Nike Air Force 1s to work, and I feel fine.
[iuh0lzd] (score 1, diepte 1 OP) That sounds heavenly not sure I can afford it though
[iugyaiz] (score 1, diepte 0) Compression socks and then when I go to bed after work, elevate legs on 2-3 pillows (enough so my legs are above the level of my heart).
[iugzrre] (score 1, diepte 0) Regular cardio, compression socks, drink plenty of water, and invest in a good pair of shoes
[iuh0oom] (score 1, diepte 0) I wear compression socks and Hokas. I really didn't want to spendtgat much on shoes but within a few weeks, the difference was amazing.
[iuh4hyb] (score 1, diepte 0) Get yourself some compression socks
[iul9h7f] (score 1, diepte 0) Kinda in the same boat, I figure I need to lose weight to ease up the pressure on my joints. 6ft 250lbs 38yr male, wear Hoka Bondi 7 with custom podiatrist insoles with smart wool compression socks, I still ache
[iufn33h] (score -3, diepte 0) Mix lemon 🍋 with honey, cayenne pepper, turmeric and organic ground cinnamon. On an empty stomach. Then drink a cup of hot water slowly. It helps with inflammation. Changing your diet might also help. Lower your salt intake. Also go to the Dr. It could be something serious. I wish you well

