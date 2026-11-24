# Label-batch batch_0137

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
Schrijf het resultaat naar `batch_0137.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1b6lqit, veld35, 1eme1ls).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1b6lqit ===
SUBREDDIT: r/WaltDisneyWorld
DATUM: 2024-03-04  SCORE: 7  REACTIES: 64
TITEL: Foot Pain + Hot Feet at Parks - What is your hack/best solution?
POST (source_id=post):
Hello,

Family and I love WDW, one of the hardest parts is navigating my incredible foot pain while at the parks. I soldier through it, but it puts a bit of a cloud over our day as I anticipate it's rapid arrival.

We do a lot of the logistical things necessary to reduce this, regular rest, genie+, ice packs, etc. I am curious if there are any products that help you or techniques you do to help give your feet some repreive at the parks.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ktcubys] (score 26, diepte 0) I bring two pairs of comfortable shoes and switch between them. 

In the weeks / months leading up to a trip I track my step counts and work them up to ‘Disney-level!’
[ktd3jeq] (score 19, diepte 0) I wear compression socks, put hydrocolloid bandages on the soft pads of my feet, gel toe separators on my pinky toe and middle toe, and wear my broken in adidas ultra boosts and this has completely eliminated hot spots for me. I have a swelling disorder so I’ve been trying to get this perfected for a while. Bonus if you soak your feet in epsom salt or ice water. I prefer epsom salt.
[ktcq4p8] (score 18, diepte 0) There's the very obvious stuff about wearing comfortable, broken in shoes but you can also try insoles that can provide more cushioning and helping with the pain.

The one thing someone told me years ago that I have made a habit of doing and seems to have helped is that you should always wash your feet at night before bed.  Even if it wasn't a hot day and you're tired so you aren't going to shower at night, fill the tub enough that you can at least wash your feet before bed.
[ktdn1mk] (score 14, diepte 0) I can’t believe no one here has mentioned this - STRETCH!!!

Your plantar fascia, in particular, gets inflamed with lots of walking, especially with repeated strikes on hard surfaces like concrete. This *usually* causes pain in your heel, but can cause pain pretty much *anywhere* in your foot. Insoles and good shoes can help a lot, but you need to stretch the muscles that point to, connect to and support the plantar fascia, as well.

I have custom orthotics, but when I learned to stretch my calves, Achilles tendon and arch several times throughout the day (in line, while taking a break, before and after the park, etc), it changed my life. My feet are HAPPY after a day at Disney!
[ktcx1lk] (score 11, diepte 0) 1: Breaking in your shoes before going

2: Investing in a good pair of shoes with lots of support, like merrels, chacos, brooks, etc. 

3: Practicing walking before going. Spend some evenings walking an hour or so plus with your kids, and the weekends adding more distance. If you're mostly sedentary and then going to 5+ miles a day you'll die. 

4: Epsom salts and Motrin - anti inflammatory
[ktcstaw] (score 10, diepte 0) Get fitted for walking shoes at a running store and stay active between trips. You shouldn't be in pain after a long park day. Maybe a little sore and tired but if you're having pain that's a different story.
[ktcqz4a] (score 9, diepte 1) I like a quick ice bath for my feet—the medium size plastic WDW shopping bags are perfect for ice, some water, and 1 foot at a time.  30 seconds in, then switch, repeat as desired.
[ktdk606] (score 9, diepte 1 OP) This is the sauce, I appreciate this, I will check out those bandages, separators, and sock.

Thanks for taking the time to clue me in on your tricks.
[ktcsu9r] (score 7, diepte 0) Build up your “foot stamina” before leaving

Broken in Hokas and quality socks

Alternate shoes every other day 

Take ibuprofen + Tylenol the second the pain starts vs. after it’s terrible and stay on them every 6 hours

Soak in hot tub at night. 

A loving partner to rub those bad boys.
[ktdnuq9] (score 6, diepte 1 OP) Such a good idea, my wife and I started morning yoga two weeks ago and I think it’s actually helping a ton. My legs are super tight, stretching is important, I’ll keep my stretching up in advance of our trip and during our trip!
[ktdqr1e] (score 4, diepte 2) It’s a great idea to do it several times throughout the day, too! You don’t need to go through a whole 15 minute stretch routine, but a quick 30 second calf stretch on each side does WONDERS for my foot pain, if it ever acts up.
[ktdkehk] (score 3, diepte 1 OP) Thanks for the reply! I’m going to bring a massage gun this time, and I think you’re right, might just front load my day with Tylenol & Ibuprofen.

Another commenter mentioned socks, I might need to spend some $ on some fancy ones.
[ktdcyz6] (score 3, diepte 0) I used to really dread foot and ankle pain at Disney too, but like everyone else is saying, I was able to resolve it with a combination of good shoes (Hokas and Blundstones for me) and training (I walk 10k steps/day).

For an underrated hack, maybe try slant boards every day for a few weeks before you go. I do 5-10 heel lifts a few times a day on mine and that's been really good for building the muscles that were previously causing me pain. And maybe look into some light wool socks designed for summer wear, removing the moisture can help prevent blisters and also keep your feet cooler.
[ktee2y6] (score 3, diepte 0) I am a long distance runner and here’s what I do:
1. Sweat resistant, compression socks (I love feetures)
2. Supportive walking shoes for first half of the day. Switch to supportive sandals whenever breaking from walking to allow feet to breathe. 
3. Gold Bond Foot Powder spray. Reapply between switching from shoe to sandal. This is a MUST. If you can’t find it, try regular baby powder. 
4. Toe separators if you have wider feet or toes that touch. 
5. If prone to blisters, preemptive use of blister bandages. 
6. Epsom salt bath at end of night for 15 mins
7. Use a tennis ball or an acupuncture foot roller after bath for 10 minutes. 
8. Before bed, apply roll on or rub on icy hot and let feet breathe. If you have the mobility, let your feet sit on the wall above your head to stretch.
[ktdjqio] (score 2, diepte 1 OP) I always do an ice bath for my feet at the end of the day at the hotel, plus a shower. 

I’m pretty fit, quite active, I believe it’s related to a structural issue in my feet that cause me more issues than most. 

I have 600$ custom inserts as well, hoping for some leads in the “in park” department in saving me from the pain. 

I appreciate the insight!
[kteo72w] (score 2, diepte 2) We would very similar. I’m also pretty fit and active but have structural issues that has led to plantar fasciitis and foot pain when I’m them all day. My podiatrist recommended calf stretches first thing in the morning, throughout the day and before bed. That has helped me a lot and relieved a lot of pain in arches and Achilles.
[ktdjzov] (score 2, diepte 1 OP) That’s a dream, I’d love to not have the pain, sadly it’s there and there pretty early. 

I have nice adidas running shoes, and 600$ custom inserts, but my feet are quickly toast. Hoping for some creative ideas for “in park” relief, especially cooling.
[ktdo096] (score 2, diepte 2) Roll or spray lidocaine would be my next suggestion
[ktdt1la] (score 2, diepte 2) Yep then not much you can do but hunt for the perfect sneakers and get ahead of the pain you know is coming, which it seems you are doing. Good luck!
[ktct3ni] (score 2, diepte 0) Epsom salt soak in the bath tub every night before bed
[kte59cj] (score 2, diepte 1) I second Merrill’s and taking ibuprofen.  Really helps a lot.  I wear Merrill’s hiking and they’re great.  The pavement is what’s killer so I recommend changing the insoles.
[ktdkvc7] (score 2, diepte 1 OP) Cooking Foot Masks! That’s a great idea and the sort of creativity I’m looking for.

I do have a structural foot issue, I have 600$ shoe inserts, but they only delay the inevitable. The tips you gave I think will help me though, thanks for replying.
[ktdkne8] (score 2, diepte 1 OP) Wool and Colder Feet is a surprise, you’re the third person that’s mentioned I need to up my sock game, I’ll definitely do that! 

Thanks for taking the time to reply.
[ktdiqc2] (score 2, diepte 0) A hot shower at the end of the day makes sure my feet get a lot of time in the hot water, then I slather on CBD cream on my entire foot including the ankle. Wake up feeling like a new person.
[ktdpmk2] (score 2, diepte 0) I have nerve damage in my feet. They’re very sensitive and I have to be very protective of them. If I can help out from my experience, buy brooks shoes (I wear ghosts) and Darn Tough socks. Darn Tough is expensive, but absolutely worth the price. Just try one pair.

I also use dr scholls insoles. Between all 3 I never have issues being on my feet all day.
[ktdsx7c] (score 2, diepte 0) It sounds like you're already doing the right things that you can do to keep your feet as pain free as possible. If it's an orthopedic issue - it's probably time to have the physician or surgeon address it. The only alternative would be to use a mobility scooter or wheelchair.
[ktdtsmm] (score 2, diepte 0) Have you tried foam rolling your feet? I think people know a bit about foam rolling legs, but ballerinas foam roll their feet from a long day of dancing and using their feet. I would do legs and feet if I were you, along with the other great tips mentioned here.
[ktdy0jd] (score 2, diepte 0) Take at least two pairs of shoes. Take 3 if you can. Every pair fits your feet differently, repetition is what causes pain and blisters. Change it up every day. You won’t stop all of it but it’ll help a lot more than you think.
[kte1nd6] (score 2, diepte 0) Rent a scooter. You’ve got a legit medical situation going on, this is what the scooters are for. 

You’re paying $600 for inserts, this is beyond us recommending Tevas and going for walks in the zero entry pools (what I usually do if my feet are bothering me).
[kte5zsh] (score 2, diepte 1) I have rheumatoid arthritis that's destroyed by knees and ankles. This is my first trip that I've accepted I need a mobility aid. It's been legitimately life changing to not have my park time limited by my pain and not be crippled every evening or needing opiates just to be able to sleep.
[kte79he] (score 2, diepte 2) Hopefully this turns out to be a great trip for you and the family!
[ktf5df8] (score 1, diepte 2) Got a foldable portable foot bucket for this best thing i ever did for my feet at disney.
[kthf3aq] (score 1, diepte 2) Same, though I just use the tub.  I fill up a shopping bag with ice, dump it in the tub with a little water.  Then I play a "game" of how long I can stand in there, until I have to jump out and stand on the towel...then repeat several times.
[ktcunih] (score 1, diepte 0) Skechers on day 1 crocs on day 2. I alternate and it works .I average around 35k steps at Disney a day.
[ktczwtk] (score 1, diepte 0) Definitely agree with the advice to switch shoes but I would go further than alternating daily--alternate within the day itself. I always bring three pairs of good, well broken in hiking sandals and switch to a different pair when we go back out after our long midday siesta at the resort. It really makes a world of difference. I also pamper my feet religiously with cooling foot masks, they're a godsend.

But I also agree with the person who said to get fitting for walking shoes at a running store. That level of severe foot pain really isn't usual and you may be prone to something like plantar fasciitis which requires a different kind of shoe.
[ktgi4l6] (score 1, diepte 2) My go to is the Volcano one by Lush but there's cheaper ones you can get at Target that do the job too!
[ktdmp67] (score 1, diepte 2) You are very welcome. I hope it brings your feet success.
[odzpxxq] (score 1, diepte 1) I realize this is 2 years old but can't hurt -- I have "Irish" pinky toes that are turned inward/sideways that have occasionally started to slip under my other toes somewhat. A thick bandaid adds the separation  I need but I've been wondering about the gel or silicone toe seperators. 

Do you wear them all day in the park? Like rope drop to park close,  15k-25k steps a day? 

Appreciate it 😊
[ktd7ufg] (score 1, diepte 0) I’m usually too exhausted and trying to keep my kids from going insane to pay attention to it. The whole “bubble effect” really helps too. Sorry not too much help.
[ktdkzhw] (score 1, diepte 1 OP) I’ll take a look at some relief cream, I bought some icy hot to take down for now, will look at CBD, thanks got reply!
[ktdnygb] (score 1, diepte 0) Goldbond makes a spray to help with sweat and also has a cooling sensation (though it won’t last). You could also try a peppermint foot balm/oil roller. Definitely another plus one on the compression socks
[ktdo02y] (score 1, diepte 0) Oofos. They’ve been better for me than any insoles I’ve tried so far. Flip flops or the slip on shoes (with or without socks)
[ktdo08r] (score 1, diepte 0) Not sure if this is exactly what you're looking for but I recommend moleskin padding on your feet to help with blisters if you get them.
[ktdoaw7] (score 1, diepte 0) Honestly, the thing that made THE BIGGEST difference for me was two pairs of shoes and switching each day. Had been to Disney a couple times before and had sore feet. My third time I brought two pairs of shoes and swapped each day. Gives them time to decompress. Worlds of difference.
[ktdqaqr] (score 1, diepte 1 OP) Thanks for this! I will check out Darn Tough socks and maybe change my shoes.

Hope you have continued pain free success! And hopefully I can join you.
[ktdpxok] (score 1, diepte 0) A pair of ON brands sneakers changed the game for me. Went from hobbling around by day three, to basically discomfort-free after a 10 day trip.
[ktdrfn0] (score 1, diepte 0) KT tape feet for more support, ice each night after parks, and advil. Wool socks work great as well.
[ktds7kg] (score 1, diepte 0) I’m literally in the hot tub every night when I get back to the resort
[ktdwdf9] (score 1, diepte 0) A foot roller!  I personally like the Triggerpoint Nano.
[ktdz2en] (score 1, diepte 0) Bombas socks and New balance fresh foam x1080 v13!!!!! Also, take a wooden foot roller and roll when you're in the park and have down time. I also soak my feet in hot water when I get back to the room.
[kte0enj] (score 1, diepte 0) Gold Bond powder in my socks works for me. I also use wool socks (pulls moisture away). The obvious thing is good shoes (Brooks, Hoka or whatever you find comfortable).
[kteam39] (score 1, diepte 3) Thanks! Leaving in the morning. It was a wonderful trip.
[kte4wwf] (score 1, diepte 0) Change out the insoles in your shoes.  It makes a ton of difference on your feet.  Also, moisture wicking socks.
[ktea7e1] (score 1, diepte 0) Along with the good socks and worn in shoes that are rotated, I always bring peppermint foot spray. I get mine from Body Shop and the cooling spray feels so nice at the end of the day.
[kteb0mr] (score 1, diepte 0) We swear by epsom salt gel. I get it on amazon and keep it in the fridge at the hotel and use it generously before bed, and a few times in the evening if we get back to the hotel earlier. I also think using my "recovery" flip flops help. Mine are knockoff Oofos, but I do my best not to go barefoot at all when at the hotel, unless I'm in the pool.
[ktec25s] (score 1, diepte 0) Insoles. Go to a podiatrist and get your feet scanned and get custom insoles made. I fucked up my feet after my last visit. Ended up walking into a hairline fracture.
[ktfcqwc] (score 1, diepte 0) Good shoes. I used to wear sandals and deny that as the reason my feet hurt. Now I wear adidas and my feet don’t hurt! 

But I also: spray aspercreme after I shower at the end of the day, soak my feet in warm then cold water in the tub at the resort (after shower), elevate my feet in bed, and when I was 17w pregnant at Disney in August (insane I know) I had my fiancé rub them while elevated and that was really nice lol
[ktgwphc] (score 1, diepte 0) Collapsible stools from Amazon. You have to carry them around but it makes a huge difference if you have a place to sit when waiting in those long lines

(I sent this while sitting on one in the line for Remy!!!)
[kthsprq] (score 1, diepte 0) Sean Hayes, on the Smartless podcast, was recently extolling the virtues of this [bad boy](https://www.amazon.com/gp/product/B01L6PKHFK/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1). Oh, man, does it do the trick for foot pain, hamstring pain, sciatica, etc.
[kti2i0u] (score 1, diepte 0) I gave my wife foot massages every night at the hotel.
[ktikjhj] (score 1, diepte 1 OP) Hey it's me, your wife
[kuedz53] (score 1, diepte 0) Yes! Have you thought about adding good insoles to your shoes?  I've tried every brand of insoles on the market. Ultimately, I switched from my custom insoles to this brand called [Fulton](https://walkfulton.com/) and nearly immediately my foot pain went away (and knee pain). These are made from cork so they mold to your arch and absorb shock/impact.
[kzx6trq] (score 1, diepte 1) Your post has been removed for breaking Rule #5.  We do not allow individuals or businesses to use this platform to directly sell to, or buy anything from, other users, including Travel Agent (TA) services provided by you or a friend/family member.  Please use the monthly self-promotion thread to advertise/solicit goods or services already available for purchase on another platform.

Please note: if your website, social media channel, and/or business (including TAs) is mentioned in your username and/or profile, your comments should not in any way mention them. Using DMs to other users to circumvent this policy will result in a ban.

Please [message us](https://www.reddit.com/message/compose?to=%2Fr%2FWaltDisneyWorld) if you have any questions.
[lbwtei0] (score 1, diepte 0) There’s a lot of great ideas already but I remember reading one older lady at one point posted that she started bringing a collapsible foot bath & Epsom salts to soak her feet at night & I think that’s genius.

=== THREAD veld35 ===
SUBREDDIT: r/Residency
DATUM: 2022-06-17  SCORE: 99  REACTIES: 63
TITEL: Different shoe options in residency - A review from a fellow sneakerhead resident
POST (source_id=post):
I have seen a lot of posts over the last few years on here and r/medicalschool about comfortable shoes or what shoes people recommend. I have replied a few times with a few different write-ups and have been meaning to sit down and do a full write-up for people looking for new shoes before residency starts. This is my opinion as someone who loves shoes and has way too many pairs. Shoes are hard because everyone is a bit different. For reference though I have fairly flat/wide feet so finding the right shoe was always a challenge. These are my opinions on shoes and I will provide some price estimates as well as other comments I have gotten from friends on their shoes as well. If anyone has any input please feel free to share or add your opinion on some shoes that I haven’t reviewed and shoes that I have. I am also male, so I am sorry ladies, but I have no reviews for heels or flats. I was not a sneaker person until medical school and had always just gone with a cheap $100 pair of whatever was on sale. One thing I will say about spending $180+ on a pair of shoes. Do your research and go try on a few different brands and styles. I hope my list can help guide you in picking a good shoe for long days in the hospital. With a lot of the shoes on this list, the price is well justified and a good shoe is worth the extra $70 - $100.

&#x200B;

**Sneakers**

**Ultraboosts –** 

Price – Retail price if you buy them from adidas is $190. On adidas’ website you can find different sales and can get them up to 40% off sometimes. I would recommend going to an outlet mall and trying on a few pairs to get a feel for them and see if you like them. I have seen ultraboosts at my local outlet mall for $100 so you can always look for a good deal there.

Sizing – True To Size (TTS) / Go half size up

Review – This is a shoe that comes up often and is usually either loved or hated. Ultraboots have been around for a while now and they have a few different versions. I have 3 pairs that I use as my beaters and wear 75% of the time I am running errands. I have had these 3 pairs for 3-4 years now and still wear them almost daily. I wore my ultraboost for surgery, it was an all-black pair so they never looked dirty. The Ultraboost DNA 4.0 and 5.0 are like the original ultraboosts. They have a primenit upper with a “cage” that the laces go through that is the original design. All of my ultraboosts are this design. The primenit upper is like a sock, so go with a TTS or even half size up. The shoe should just slip on and it will stay on without tightly pulling the laces. The ultraboost 22 has more boost in the heel. I am personally not a fan of this look but they have a similar boost design to the Yeezy 380 which is arguably the most comfortable Yeezy. The ultraboost 20 is a middle of the road between the original design and the UB 22. It has rubber on the heel for more support and thinner cage. It is similar in feel as the original utlraboosts.

Complaints – Ultraboost is very comfortable but overtime it loses support and can hurt my feet after long days. My only complaint is after a few years of wear I can’t do 18 hours of standing all day on my feet in them anymore but still wear them as my daily around town. My fiancé is a nurse and had the ultraboost 20 but did not like them as much because they did not have enough support for her during her 12 hour shifts and I have heard a similar complaint from my friend in medical school. I think part of the reason I like them so much is because I have flat feet.

Rating – 7/10

&#x200B;

**Adidas Ultra 4D –**

Price – Retail $220. But they are constantly on sale and can be found below retail on resell websites such as StockX or Goat. Right now on adidas’ website they range from $132 – 154

Sizing – TTS / Go half size up. Same as ultraboost as they use the same uppers

Review – I think the 4D is one of the coolest looking shoes out there, have a 3D printed sole, and will bring in a lot of compliments if that’s something you are looking for. The uppers on the shoe are all brought in from other adidas shoe models and you can read my review of those with the ultraboost. The 4D is a firmer sole than ultraboost and I think it is the perfect shoe for people who think that ultraboost is too squishy or does not have enough support. I have found that they still feel brand new even after having them for 2 years and wearing them at least once a week. Long days standing in them still do not hurt my feet. Over time the 3D printed sole will remain firm but continue to have enough give that it doesn’t feel hard. The next 4D I get will have the upper from the DNA or original Ultraboosts and will probably become my daily shoe. Every time I wore them in the hospital I got compliments and never had issues with the 3D sole looking dirty or getting anything stuck in it. I highly recommend this shoe and have always seen great deals on for getting them cheaper than a pair of ultraboost. 

Complaints – I have the futurecraft 4D and the upper is too thin for me. It can be flimsy at times since there is no cage on mine. Sometimes while I am walking or standing I notice my feet slip of the edge of the sole inside the shoe.

Rating – 8/10

&#x200B;

**New Balance 990v3**

Price – $185 - $210 on New Balance Website

Sizing – TTS

Review – This shoe is one of my favorites. New Balance hit a home run with this shoe, and I could rave about it for days. I got a collab pair a few years ago that was done with Kith thinking that I would resell them and not wear them. My pair looks almost identical to the 990v3 Core Navy with white and is the same shoe beside a few color changes. I decided to try them on and immediately knew I was keeping them. This shoe has it all. It is beyond comfortable, and I could stand for days without my feet hurting. They have a great styling and go with business casual or jeans or scrub pants. You can wear this shoe to your kids first birthday and everyone knows you’re the grill master about to make the best burgers on the planet or you could wear them to your 6am grand rounds presentation. It has great support and my feet never slide around in the shoe. You might be thinking, “I’m not so sure that I want to spend $180 on a pair of New Balances” but you do and you wouldn’t regret it. I would not think twice about buying another pair, but I have had mine for a year and they still look brand new, feel brand new, and remain one of my favorite shoes. New Balance has it as a running shoe but I feel like it is a bit heavy for running. It is the only pair of New Balances I own, but New Balance has other models similar with a cheaper price tag if you can’t justify the price. I have heard similar things about the 2002R which is a similar design at a lower price (\~$140).

Complaints – My only complaint is the tongue of the shoe always falls to one side or the other. It doesn’t change how they feel or cause any issues but it’s the only complaint I could come up with. 

Rating – 9.5/10 

&#x200B;

**ASICS Gel Lyte -III**

Price – $120 - $170

Sizing – TTS

Review – Asics have always been my go-to running shoes. I don’t run anymore but I used to put 500-1000 miles on a pair before I would toss them for a new pair. They have a ton of support and are very comfortable. The Gel Lyte III isn’t a running shoe but brings the same level of comfort and support that their dedicated running shoes have. The sole will form to your feet over time and they will feel even more comfortable. The Gel-Lyte III is an all-around solid shoe that is similar to the New Balance in the sense that it looks great no matter what you are wearing and doing. You can walk miles, stand for hours, or sit behind a desk and they aren’t overly flashy but you can find flashy pairs if you want. They are a friend's go-to shoe and this is what he had to say about them “I wore them when I worked on my feet at a grocery store, standing behind the checkout counter all day, I took them to Barcelona with me for my walking tour and still wear them at my desk job now”. 

Complaints – They can feel a bit bulky at first and the tongue reminds me of my OBGYN rotation. “Ultraboosts are the gold standard for aesthetic and comfort in my humble opinion” – same friend

Rating – 7/10

&#x200B;

**HOKA –**

Price – $130 - $200

Sizing –

Review – I have never owned a pair of HOKA, but I have only heard that they are extremely comfortable with good support. Input from other users would be great.

Complaints – I can’t get behind the look of HOKA. They have some newer styles that aren’t as bad but I don’t like the coloring and looks. I have some extremely “loud” and off the wall style shoes but I still don’t like the way the HOKA look.

Rating –

&#x200B;

**ON-Running Shoes –**

Price – $139 - $200

Sizing –

Review – This is another shoe that I haven’t had the chance to wear yet but know that a lot of people like. I think that they style is a lot better than HOKA but that’s also just my opinion. This is my fiancés go to work shoe and she chose to go back to ON after having ultraboosts for her days standing as a floor nurse. She said that they have more support than the ultraboost and are comparable in comfort level. Input from more people who have a pair would be helpful.

Complaints – I think that ON look like a running shoe, because they are. This decreases the versatility of them but if you are looking for an everyday sneaker that goes with scrubs or jeans I would recommend trying a pair on to see how they feel. 

Rating –

**NIKE –**

I have a large selection of Nike shoes but none of them are shoes I would wear to the hospital. I have Blazers, Dunks, and Jordans and can do a write up in the comments for anyone who would like info on any of those shoes. Nikes have been my go-to mowing shoes since I was young so I have always bought just a cheap pair for doing yard work but have never put long hours in at the hospital with a pair of Nike. 

&#x200B;

**Dress Shoes –**

I have \~10 pairs of dress shoes and they are almost all Cole Haan. I have bought Johnston & Murphy, Joseph Abboud and few other brands in the past when I had to wear business casual every day for work as a pharmacy tech and Cole Haan are hands down the best dress shoes I own. I did have a pair of Original Penguin loafers that I wore until my toes were coming out of the front, but they were not as comfortable as Cole Haan.

**Cole Haan – ZeroGrand**

Price – $68 - $200. The reason I have way more dress shoes than an anesthesiologist would ever need is because of Cole Haan’s summer sale which is going on right now. Every year I end up buying at least 2 pairs because you can get them so cheap. 

Sizing – TTS

Review – When I worked in the pharmacy in undergrad I would stand for 10 – 12 hours a day in dress shoes and my feet always hurt. Until I got Cole Haan dress shoes. These are hands down my favorite dress shoe and I ALWAYS get compliments when I wear them. I have had the same pair that I bought 6+ years ago and they still look great and are just now losing their support and hurt my feet on a long day. But that’s fine because I have 4 more that I got for $70. I cannot recommend this dress shoe enough. Pharmacy tech, hospital presentations, graduations, weddings, this is my go-to dress shoe. It goes with every outfit, and they have your classic brown, grey, blue, and black. I was iffy on the looks at first because the sole is a bit different, but I am so glad that I bought these. They have great support for 12+ hour days standing, they look fantastic with every outfit and elevate a casual outfit to a business casual outfit. Only after 6 years and working in a pharmacy standing for thousands of hours did my pair finally start to lose its support and comfort. 

Complaints – I have none with these shoes. I want to get a pair of the 2.ZeroGrand but can’t justify buying more since I still have a lot of use left in some of my pairs.

Rating – 10/10

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[icqkxml] (score 23, diepte 0) Hokas are comfortable AF. I have a running pair and two work/leisure pairs (I only wear the Mach 4s). I like the lifted heel since I have shit ankle mobility. Between crocs, cowboy boots, Birks, and Hokas, I’ll always choose the Hokas. I use to wear Brooks GTS, and ASICS Gel Nimbus before that, but neither hold a candle to Hokas.
[icreoll] (score 22, diepte 0) I prefer going barefoot. #Radiology
[ics0wq3] (score 14, diepte 1 OP) Well if your working from home, may I recommend a pair of Birkenstocks or UGG slippers
[icqlgmv] (score 10, diepte 0) I’m disappointed you didn’t add allbirds ! Most comfortable sneakers I’ve ever worn
[icrmuyr] (score 10, diepte 0) Yeezys even in the OR 

Cause even the OR deserves that turtle dove drip
[icr4x56] (score 8, diepte 0) Super-Birkis  
Super-Birkis  
Super-Birkis
[icr9lye] (score 8, diepte 0) \#TeamCalzuro
[icsdiy8] (score 7, diepte 1) Hokas are fantastic. First shoe I’ve worn without getting any foot/calf pain at the end of the day. And I’m standing in the OR for  hours some day. I have a flat arch and wide foot too
[icrzc8d] (score 6, diepte 0) I’m in the OR and sanitas clogs were a game changer for me. My back would be shredded until I got a pair of sanitas
[ics0ydp] (score 4, diepte 1 OP) Trust me, I love crocs. I still have croc pins
[icrls53] (score 3, diepte 1) Yeah, Hokas have been my most comfortable pair of shoes ever. Only downside I’ve had is that they have not made it a full year before starting to fall apart. Not sure if I got unlucky or what cuz I honestly don’t walk that much in the hospital.
[icqnq88] (score 3, diepte 0) On CloudMonster

Nike Invincible
[icr3h0z] (score 3, diepte 0) I wish something terrible would happen to all those people that wear the wooden crocs 😭😭😭
[icsoit9] (score 3, diepte 1) So are you obgyn or urology?
[ics1pzv] (score 3, diepte 1 OP) If you think I don’t have a pair of shit kickers your crazy. I just didn’t think this was the place to talk about them for the hospital. My go to “boot”, and I put that in quotes because they aren’t real cowboy boots, is Irish settler. That’s what I use on the farm and for hunting
[icrv2qa] (score 3, diepte 0) barefoot gang wya

&#x200B;

love stepping in the OR with my bare toes :)
[ics8dn3] (score 3, diepte 0) I would throw a vote in for Brooks
[ictv8je] (score 3, diepte 0) 990v3s don’t get enough love. Most comfortable good looking sneaker there is imo
[icrn131] (score 2, diepte 1) I love my birds but unfortunately don’t really have the best support for long OR cases
[icrwm73] (score 2, diepte 2) Agreed, I bought 2 pairs because of all the hype but they are not nearly as comfortable as my brooks.
[ictb4nq] (score 2, diepte 2) The On shoes tend to fall apart very quickly. They are very popular around here, and I have heard of way too many failures -often within a year.  
I myself rock my Lems primal 2 (a minimalist/barefoot style shoe)
[icr9lu2] (score 2, diepte 1) Dansko LTE or Birkenstock Tokyo
[icr1yha] (score 2, diepte 0) Yeezy 380 is good for flat foot.

Yeezy V2 is very comfortable to wear around the hospital in scrubs obviously if you are not on ER or doing procedures 

Ultraboost 19 among the best ultraboost in my opinion, but any ultraboost from year 1 should do great (made the mistake of placing a femoral Quinton while wearing all white ultraboost DNA 4.0 and got them covered with blood, but oxyclean did the magic)

Nike vaporstreet off whites are great to wear in the hospital because they are very comfortable and have a plastic covering the shoe that is very easy to clean

I like wearing J 1’s anywhere

Due to the market the sneakers are dropping in prices.
[icreofr] (score 2, diepte 0) I’ve had Hokas and onclouds. I prefer on cloud as they have more support and look cooler. The hoka slippers are crazy tho. Def must cop
[icrzd12] (score 2, diepte 1) Imma wear slippers. Maybe pink ones
[icrf80p] (score 2, diepte 0) Cowboy boots it is
[ics8vd3] (score 2, diepte 2) Nice! Everyone needs a few shit kickers, but I'm talking cowboy boots in the hospital...Nothing supports my feet better than some Ariat work hogs. I actually just got a pair of their Chelsea style boots for the hospital
[icrifx4] (score 2, diepte 0) I have always loved New Balance from shoes to running gear. Just ordered another pair, this time 990s.
[ics1sm5] (score 2, diepte 1 OP) I hope you love them! My 999v3 are hands down my most versatile and comfortable shoe
[ics1w67] (score 2, diepte 1 OP) Lol I have a few pairs of yeezy but have never been confident in my ability to keep them clean. Plus as a med student I didn’t have the money for a beater pair. Like ultraboosts but more comfortable
[icroqwr] (score 2, diepte 0) Nike Pegasus 28, grey. Have lasted a year and still have plenty to go.
[icrr7pk] (score 2, diepte 1) Yeah I've had a pair of Nike Pegasus since 2020 and the sole is still ok.
[ics68o1] (score 2, diepte 0) I wear my Yeezys at least 2 or 3 times a week. I’m IM and they are comfy as shit. Best thing I can do is every year or so I throw them in the wash and they come out looking brand new.
[icseyca] (score 2, diepte 0) I wore and continue to wear a brand I picked up in med school. Clove. They’re designed for health care workers. They are non slip, comfy, super easy to clean, come in a variety of colors, and have drawstring laces. I like them. Replaced the insoles once in my first pair, use those as my daily sneakers now. New pair to start residency on inpatient. Excited. 

For dress shoes, I have been using Clarks. Relatively affordable and pretty comfy and durable. Still looking good after a few years.
[icsyw31] (score 2, diepte 1) i got a pair of those because my old roommate raved about them (he worked in a kitchen so on feet a lot) and i was not a fan. feet hurt after a day of clinic
[icwzy0i] (score 2, diepte 1 OP) I wouldn’t have ever put my pair on if the price of the ones I bought didn’t tank for a few months. I’ve never been happier with a pair. One of the all around best shoes I own. Glad to see others have given them a shot. I really think new balance and ASICS have stepped up their game in the last few years
[icqjzb9] (score 1, diepte 0) Thank you for contributing to the sub! If your post was filtered by the automod, please read the rules. Your post will be reviewed but will not be approved if it violates the rules of the sub. The most common reasons for removal are -  medical students or premeds asking what a specialty is like or about their chances of matching, mentioning midlevels without using the midlevel flair, matched medical students asking questions instead of using the stickied thread in the sub for post-match questions, posting identifying information for targeted harassment. Please do not message the moderators if your post falls into one of these categories. Otherwise, your post will be reviewed in 24 hours and approved if it doesn't violate the rules. Thanks!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Residency) if you have any questions or concerns.*
[ictshfv] (score 1, diepte 2) What hokas do you wear? I have the same thing with my feet!
[id03onp] (score 1, diepte 3) I have the Hoka Clifton in wide shoe size. I will warn you it took a few days to break them in but after that its been really comfortable
[icqzan9] (score 1, diepte 1) Will always upvote AllBirds. Best shoe investment I ever made! I wear mine in clinic and on the floors.
(23 reacties met lagere score weggelaten)

=== THREAD 1eme1ls ===
SUBREDDIT: r/pharmacy
DATUM: 2024-08-07  SCORE: 15  REACTIES: 63
TITEL: Go to shoes for shifts?
POST (source_id=post):
What are your comfortable shoes for work? I normally work 9 to 7 at my store and I’m looking for both good shoes that won’t leave my feet unsupported or swollen at the end of the day and functional for every day out and about use! (College kid on a budget!)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lgy95e4] (score 39, diepte 0) Same schedule as you. Compression socks and Hokas
[lgz348l] (score 34, diepte 1) My feet hurt even reading this comment
[lgygi14] (score 23, diepte 0) Compression socks are a must no matter what shoe. I rotate between Hoka’s, On Cloud’s, and occasionally a pair of Altra’s.
[lgy84ao] (score 14, diepte 0) I’m an outlier but I love my vans haha
[lgy8vfd] (score 14, diepte 0) Get yourself a good running shoe. They are made for support and comfort. Personally, I really like ASICS. They’re $100+ a pair but worth every penny. Prime day I found a great pair for like $60.
[lgyrnsw] (score 12, diepte 0) Depends on your foot type:  wide or narrow? High or low arches? (Over)pronate or supinate?  Any lower back problems? 

You can get the wrong type (for your foot) of any of these brands, except maybe Altra since it is singularly wide.        So knowing your personal specs is important.  

I used to be a Dansko-only gal, but migrated to Hokas and brought the family with me. Hubs (narrow flat-foot pronator) and I (wide high-arch supinator) tried Ons and Hokas head-to-head in the shoe shop and the Hokas won for cush: Gaviota for him and Bondi/Clifton for me.  Ngl, Hokas can be in-your-face-and-take-no-crap ugly.  Ons are def what to wear with your khakis when your boss’s boss comes for a visit.  

I don’t look at Skechers anymore for my family since my son’s physical therapist voiced disapproval of the brand:  they’re cheaper but the support won’t last as long.  Brooks & ASICS are others recommended by a DPM when my kids were little.  

Get two or more pairs of your favorites and rotate them.   This is critical.  

Personal hack:  youth & men’s sizes 7 and 7.5 = women’s wide 8.5 and 9.  You’re welcome.
[lgybgjx] (score 10, diepte 0) Brooks Glycerin
[lgy99c4] (score 9, diepte 1) Just saw student on a budget. Do sketchers work sneakers
[lgymifj] (score 7, diepte 0) Danskos. I can't stand in squishy shoes. Started wearing them when I was pregnant and never went back. You can get odd colors on clearance or the basic ones for like $120, but they last forever.
[lgz74wo] (score 6, diepte 1) I’m wearing Vans for my rotations and my feet hurttttttt
[lgyadzo] (score 6, diepte 0) Ultra boost, allbirds. I hear good things about oncloud
[lgzh4rw] (score 4, diepte 2) Told yall im an outlier haha
[lgyaet5] (score 4, diepte 0) I've tried it all. I'm a runner and even my best running shoes don't do it for me as standing shoes. Crocs are the only things that work for me.
[lh1a4mp] (score 3, diepte 3) Wow you really like pain. Moved from Vans shoes to pharmacy with Vans shoes 😂
[lgzbn2p] (score 3, diepte 1) Can’t use running shoes that have a moderate rocker shape to them. 

I definitely agree. Wouldn’t wear my ASICS Superblast 2 for work bc of the shape. Any shoe with good surface area is better for standing.
[lh11bvl] (score 3, diepte 1) I love using my Crocs for my shifts. So lightweight as well.
[lgyf4vr] (score 3, diepte 0) Compression socks and hoka
[lh0nfue] (score 3, diepte 2) 2 reasons mainly, style and then just different levels of comfort. I would say I wear my Hoka Clifton most often just due to them being super cushy, where as the Oncloud Monster double as my training shoe and occasional work shoe.
[lgzwhqj] (score 3, diepte 1) I will swear by mine forever. A friend gave me a pair 2ish years ago and no sign of breaking down. I used to about cry because of the pain when I got home but these+ compression socks make it much more tolerable.
[lgy9jw3] (score 2, diepte 0) its not necessarily the shoes.  get some athletic compression socks from amazon and go to a running store and let them fit you for removable insoles.  it'll make a world of difference.
[lh0kckb] (score 2, diepte 1) What’s causes you to rotate?
[lgymrab] (score 2, diepte 0) If you search this sub for “shoes” there will be a lot of other posts with good recommendations, this is one of the most common posts in this sub
[lgyo4a0] (score 2, diepte 0) Crocs
[lh1ym53] (score 2, diepte 1 OP) Thank you! This was eye opening and helped a girl out so much!!! <3
[lh45mz6] (score 2, diepte 1) What do you recommend for wide feet? 

I keep sizing up because most shoes come in medium size
[lh7agi1] (score 2, diepte 2) Hoka Bondi or Clifton in a wide width if you need a neutral (cushion) shoe.  Gaviota (or Arahi) wide if you need a stability shoe.   

Bondi and Gaviota if you’re standing more (at work), Clifton and Arahi if you’re walking more.  

Altra Olympus deserves a nod as well.
[lgz0zaz] (score 2, diepte 0) I wear brooks with compression socks, my partner wears crocs and compression socks and my techs wear hokas, sketchers or on clouds
[lgzl1vd] (score 2, diepte 0) New balance brand running shoes but I'm a size wide with low arches.
[lgzz32b] (score 2, diepte 0) Running shoes (Brooks) with compression socks
[lgzzv21] (score 2, diepte 0) Cloves!!!!!! Literally 98% of my back pain disappeared. I’ve been wearing them for about a year now and they have absolutely changed the game for long shifts and standing forever
[lh1kmkx] (score 2, diepte 0) I know this might contradict the budget aspect at first but a pair of boots that is able to be resoled will literally last a lifetime. The leather will mold to your feet and be the most comfortable shoe you own by far!  A decent place to start is Thursdays boots or Jim Green (I love my African Rangers). This one change has solved my near constant foot pain from 12 hour shifts at the pharmacy.

P.S. As others have mentioned a good pair of socks is a must! I like Darn Tough but their lifetime warranty has meant I haven’t had to buy anymore socks since!
[lh1udut] (score 2, diepte 0) Birkenstock Tokio Super Grip and compression socks. Especially if you have high arches and need back support. I’ve been wearing these for about 15 years.
[lgzh2fi] (score 1, diepte 2) I was a Vans Assistant Store Manager for 2 years before pharmacy, I’m kinda used it by now haha. 

Definitely recommend checking out the UltraRanges (running shoe vans) or the pro skate line (more cushion)
[lgyjs1z] (score 1, diepte 0) When I had plantar fasciitis my Kurus were a godsend. Once that cleared itself up I switched to Cloves. I walked hospital halls for 12 hr shifts and stood for 8 hr retail shifts and they held up great for both. I really like their bungee style laces too
[lgykzin] (score 1, diepte 0) On CloudMonsters. Nurses recommended them to me and I finally understand why.
[lgyngh8] (score 1, diepte 1 OP) Thanks I’ll check it out!
[lgys5te] (score 1, diepte 0) Ultra boosts or on clouds
[lgyv21g] (score 1, diepte 0) Clove with split payments (only way I can afford them but worth every penny)
And honestly....crocs.

I have several issues with my legs and feet and yeah those are the only shoes I can work in without pain.  No matter what shoe you wear, you need compression socks for work.  That alone will make a big difference.
[lgz2gwt] (score 1, diepte 0) Skechers are the only thing I’ve found that I find comfortable for a full day. 

Apparently they are shit for your feet though.
[lgzafjk] (score 1, diepte 0) Shoes are very subjective and each person requires a different type of shoe. For me, I’ve been rotating New Balance Rebel V4 which I also run in. It’s important not to wear the same pair each day so I have multiple colorways.

This, combined with Sockwell firm compression socks.
[lh1yqc6] (score 1, diepte 1 OP) Why is it that you rotate them? I just wear these black Nike running shoes 24 seven every day.
[lgzk3bc] (score 1, diepte 0) Hey Dude Wally’s
[lh7xttp] (score 1, diepte 1) I got a pair after my feet started to get used to my hokas and I think I just like a really plush shoe because they weren’t my favorite! I did get a pair on sale though so I may have not gotten the ones that people rave about lol. Love that they are waterproof though because I have spilled one too many liquids on them 😂
[lh01q1j] (score 1, diepte 0) if you have really arched feet like mine, I love Dr. Scholls sneakers. The only shoes I've worn for work that don't leave my feet aching at the end of the day. I spent $160 on Hoka's that did nothing except make my feet look huge 🙄
[lh04dpq] (score 1, diepte 0) Rockport over 10 years now
[lh0apc4] (score 1, diepte 0) I rotate two pairs of ASICS. Replace every 6 months.
[lh0bu3e] (score 1, diepte 0) I really like the Gel Venture ASICS, they’re supportive and sometimes on sale.
[lh0cddt] (score 1, diepte 0) Compression socks and super feet insoles. I've found the actual shoe itself doesn't matter so much for me.  I've put the insoles into my work Crocs and it's pretty great
[lh0f1wq] (score 1, diepte 0) Hokas work pretty well
[lh0k1y7] (score 1, diepte 0) No one wears dress shoes anymore?
[lh0m1hh] (score 1, diepte 0) I have a couple pairs of Hokas, they are probably the most comfortable shoes I have bought and I can stand and walk all day without my feet getting tired, it was very noticeable how much better my feet felt in those when I first got them compared to other runners. I’ve heard ultraboosts are also great as well as some ASICS and new balance. My mom wore sketchers as a nurse and swore by them, they also tend to be more budget friendly. 

I owned a pair of On Clouds and would not recommend at all. I found the sole to be incredibly stiff (no bounce whatsoever) and they provide essentially no support whatsoever. My feet got more tired in those than my Nike SBs and Vans and I feel miserable after a day in those. They also fell apart very quickly, within 6 months they had holes in many places, but I also wore them outside in the snow which probably contributed to that. However I have shoes that are 6+ years old with no holes and I have abused those much more than my on clouds. I’ve heard similar things from other people online about this brand, they seem to be more of a fashion statement than an actual good shoe. But maybe I just didn’t get a good model or something
[lh0qcmz] (score 1, diepte 0) brooks ghost max and glycerin + compression socks
[lh0y1yq] (score 1, diepte 0) Adidas ultraboosts one size too big 🙌🏼
[lh0yhdg] (score 1, diepte 0) Gonna go against the grain on this one, but after dealing with severe foot pain for years, trying so many kinds of trainers, running, walking shoes, low dollar and crazy high dollar, I finally realized my feet felt best when I got home and took my shoes off.  So I tried some Xero shoes, total game changer.  My feet hurt the first few days and it went away.  I don't wanna jinx myself, but I haven't dealt with foot pain in several years, ever since switching.

I think people don't realize all the "support" actually makes your foot weaker and you end up with more pain, you want it strong.  An arch is one of the strongest natural supports, if you make it strong, your feet will hurt waaaaay less.
[lh0zdni] (score 1, diepte 0) I just use all birds
[lh10ulw] (score 1, diepte 0) I have a cute pair of black sketchers that I love for work. Think they are like the non-slip line?
[lh11pdx] (score 1, diepte 0) Hoka Bondi 8
[lh16x11] (score 1, diepte 0) I go for altras
[lh1qll9] (score 1, diepte 0) There are no shoes good enough.  They all wear out.  If you get a shoe with good cushioning at the store, try not to combine it with the cushioned mats at the workplace.  I've always found it difficult like you're walking on a bed.  It should be one or the other but with both it hurts my ankles.  Anyway, after a while if you stand constantly without walking purposefully during the shift, it will lead to edema and leg vein problems.
[lh1qm1d] (score 1, diepte 0) Found a good deal on Diadora’s Cellula and it’s been a game changer. All of the others usually mentioned felt either too narrow in the toe box or too “bouncy”
[lh2ct8k] (score 1, diepte 0) I use ultraboosts and air max 97s
[lh39ls7] (score 1, diepte 0) If I am closing a retail pharmacy, there is no better feeling than taking off my shoes, closing the gate, and vaping and snacking listening to music in socks. 

Even better if some old crusty person bangs on the gate and says HEEeeeEEEllLLoo like Granpa Simpson while I do the Dougie right out of their sight.
[lh3em6c] (score 1, diepte 0) Student on a budget...ummm.... was going to suggest Hoka bondi 8... but budget go to DSW to get Ascis gel 8
[lh3h6da] (score 1, diepte 0) Hokas, on cloud, new balance fresh foam on a rotation. I rotate bc I find that they last longer & my feet pretty much never hurt unless I’m on a longggg multi day stretch then it’s just inevitable.
[lh3rxmx] (score 1, diepte 0) New balance or acis
 You need compression socks if your feet are swelling
[lhcfew8] (score 1, diepte 0) Hokas or sketchers

