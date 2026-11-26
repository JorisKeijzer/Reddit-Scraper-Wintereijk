# Label-batch batch_0152

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
Schrijf het resultaat naar `batch_0152.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 100vkei, sa6nf0, zq8i48, yg06yz).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 100vkei ===
SUBREDDIT: r/Residency
DATUM: 2023-01-01  SCORE: 18  REACTIES: 60
TITEL: Best shoes for bunions?
POST (source_id=post):
Yes, bunions…very sexy topic. But I desperately need a shoe upgrade so my back and feet stop killing me while standing for hours on rounds. 

I recently dropped $$ on Brooks Ghosts which I deeply regret, they were comfy at first but by the end of the day my bunions really hurt. I can’t return them now so I’m hoping they will stretch over time but I’m not sure it’s worth the daily pain (if anyone has shoe stretching tips I’m all ears).

Usually shoes that work well for bunions have a wider toe box. I know a lot of shoes come in a wide width option, but the rest of my foot is actually quite narrow so just getting a wide width isn’t always the solution; even if it accommodates my bunions it makes the rest of the fit weird. I’ve been wanting to go to a running store so they can do the foot analysis and all that but I just haven’t had time. Hoping someone else has also struggled with this and found a good shoe already. 

Any suggestions? 

(Looking for women’s shoes if that matters, though at this point I’m willing to try whatever)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kr3kv9r] (score 29, diepte 0) If you're dealing with bunions, the New Balance Women's Fresh Foam Roav V1 Sneaker is a great choice. Its wide toe box and cushioned support provide relief and comfort for sensitive feet. Plus, its stylish design means you can walk confidently without sacrificing style. Perfect for all-day wear!
[kk0blr6] (score 22, diepte 0) I purchased my third pair of altra's, this time Lone Peak 7. The first day I had them I wore them barefoot.
I have knock on wood never gotten a blister from any of my Altras.
They give my wide feet space to be feet.
I like that this shoe has cushion but not a massive amount, it's not like walking on a platform. The shoe it's self feels very stable and supportive. The traction allows you to walk or run and prevents slipping but is not so treaded out that it catches and holds onto things. It is also lightweight and airy.
[j2kaekn] (score 14, diepte 0) Altras have a very wide toe box, you have to generally size down a bit
[j2k5inl] (score 9, diepte 0) Shoe stretching tips: there’s actually a device you can buy to stretch shoes.
[j2k6vv7] (score 9, diepte 0) I have bad bunions.  Men's shoes are the way to go.

I also wear the creepy toe shoes when not at work because they pull everything straight and it's like magic how good my feet feel.
[j2khui1] (score 9, diepte 0) Also have bunions. I used to wear a woman's 8.5 but found a men's 8 always had more room in the toebox. Never turning back.

Could be an option for you as well!
[j2k4nuj] (score 8, diepte 0) The only shoes that have ever taken me through all week with no pain are crocs
[kgh1647] (score 7, diepte 1) Here are Few options for you Shoes with Bunions

**Orthofeet Siena Women's Walking Shoe:** Designed specifically for foot conditions like bunions, these shoes offer a wide toe box, excellent arch support, and comfortable cushioning.  
  
**Hoka One One Bondi 8:** Known for their plush cushioning and supportive design, these sneakers are a great choice for those with bunions who prioritize comfort.  


**New Balance 990v5:** A classic comfort shoe with a wide toe box and good arch support, the 990v5 is a reliable option for everyday wear.
[j2mhrkp] (score 7, diepte 0) You can get a gel toe cushion to wear between your first and second toe to help straighten the first toe - literally we had buckets of them in the Ortho clinic and I would take them for friends, family, to use as stress toys, etc.
[j2ki7tq] (score 6, diepte 1 OP) Should have realized there’s a device for everything
[j2kokk9] (score 6, diepte 0) Hokas all the way, even the regular fit has a fairly wide toe box in addition to wider sizes. I got them bunions too…and I can wear Hokas for 12+ hours without having them get all angry and painful.
[j2lv9j6] (score 5, diepte 1) Sell them feet pics and upgrade to custom orthotics
[j2k90ag] (score 4, diepte 0) Sorry to hear about your feet. The ghosts were absolutely a lifesaver for me and got me through residency with still some life in them.  Any running shoe store should test you out and offer a trial run after which you could return or exchange if you're not happy
[j2lsz2b] (score 4, diepte 0) DM me your bunions? Maybe I can help
[j2n9bal] (score 4, diepte 1 OP) They’re pretty impressive, not sure if you could afford it $$$
[j2mgfq1] (score 3, diepte 2) I honestly just get the classic clogs. I have chunky toes and bunions from years of dancing and i have more than enough room for these dawgs.
[j2khlbk] (score 3, diepte 1 OP) Is there a certain one you’d recommend?
[j2l3ve3] (score 3, diepte 2) I’d second Altras. Make sure they’re one of the models with wide toe boxes, not all of them have them. Also each model gets a weird amount of changes with each version, so you’ll notice some models are loved and then the next version comes out and they’re hated, so ensure it’s the right model and version. Also their hiking shoes are inherently wider than the running ones, but you’ll make a decent amount of noise walking haha. 

I have multiple but my absolute favorite are my Lone Peaks. If there is an REI or like a Dick’s near you I’d try them on cause I’ve had some makes I loved and others I returned within a week.
[j2l5yu8] (score 3, diepte 0) A podiatry resident recommended hokas to me for my bunions lol
[j2ny9od] (score 3, diepte 2) Does anyone actually like seeing bunions though? I thought foot fetishists only went for pretty feet.
[j2n0osb] (score 3, diepte 0) Big fan of Lems and Xeros. Both zero drop but have large toe boxes to help with this. Xeros are more barefoot if you're in to that. Both are my shoes for the hospital/clinic.
[j2n0t71] (score 3, diepte 1) Also great if you have issues with plantar fasciitis
[j2khsuf] (score 2, diepte 1 OP) Are there certain ones you’d recommend? I was looking at reviews for the On the Clock crocs and some people specifically said they were too narrow for their bunions
[j2kikxv] (score 2, diepte 2) Literally any of them.  None are particularly attractive,  but they all straighten the big toe and hold it in the correct position.
[j2wh96o] (score 2, diepte 3) Big facts in this paragraph. I’ve also noticed some inconsistencies in their sizing with each model; the lone peak 4 was the most perfect shoe for me, but the 5 and 6 in the same size leave my poor little feets either sloshing around or getting awkwardly pinched. Definitely not a pair of shoes you want to order online, go try them on in the store
[j2kie2f] (score 2, diepte 1 OP) Definitely something I’d try, thanks! Any specific ones you like?
[j2kl6mn] (score 2, diepte 2) I recently switched to Merrell and enjoy their men's hiking and work shoes. 

Whatever brand you go with, it's just important to go in person and try different pairs. You start to get a feel for the one that suits you most (esp if you're going to be standing or rounding for hours).
[j2kj9fs] (score 2, diepte 0) Me: sucks when you are a guy with wide feet and have bunions.    I use a shoe stretcher on wide shoes which helps though
[j2kjkw0] (score 2, diepte 0) Partner had bunions and swears by Birkenstocks
[j2spi8f] (score 2, diepte 1) true that! Have been using hokas for almost all outdoor/indoor activity for the past 6 years without regret...
[j2kxaqz] (score 2, diepte 0) Altras of any type are your best option because of the wide toe box, plus a good set of Powersteps Pinnacle insoles; bunions are biomechanical and usually due to flat feet so you need arch support. If you over pronate, Hokas or another rocker-bottom to prevent biomechanical stress will help overall. 

But honestly, giving my podiatry opinion here, if they're bothering you so much, you might be better off with a surgical fix. If your IM angle isn't too out of whack, you might be able to get away with a head procedure with minimal down time. Docs are always on our feet which will ultimately make it worse long term and then you're looking at a more involved surgery.
[j2mxr8u] (score 2, diepte 0) Xero Prios. Wide toe box, zero drop, 4mm sole. Very minimalist. May require an adjustment period, but my feet have seriously never felt more comfortable standing all day.
[j2nbvwu] (score 2, diepte 2) I decided on them because I had issues with poor ankle stability and fibular head pain. The zero drop has helped a lot with this. My fiancé got me into them after it helped her plantar fasciitis over time. 

It would make sense to me for zero drop to help with lower back but I haven't done any research in regards to it. But I would think a higher heel would put you into a little more lordosis/anterior pelvic tilt.
[j2nu633] (score 2, diepte 0) The only thing that stopped the ache of my entire body was San Antonio Shoes.  Decidedly unsexy.  “Old Lady Shoes” for real, but the Mary Jane style isn’t too too ortho looking.  I have narrow heels and a 20-30 degree bunion on my right foot.
[kh2os11] (score 2, diepte 0) These are my Favorites against Bunions  


Overall:  
  
**Hoka One One Bondi 8:** Maximalist cushioning and a wide toe box provide ample space and comfort for bunions.

  
Merrell Trail Glove 5: A comfortable and flexible option with a roomy toe box, suitable for casual wear and light walks.

  
Dansko XP 2.0 Clogs: Supportive footbed and adjustable closure offer a customizable fit and alleviate pressure on bunions.
[j2k25m8] (score 1, diepte 0) Thank you for contributing to the sub! If your post was filtered by the automod, please read the rules. Your post will be reviewed but will not be approved if it violates the rules of the sub. The most common reasons for removal are -  medical students or premeds asking what a specialty is like or about their chances of matching, mentioning midlevels without using the midlevel flair, matched medical students asking questions instead of using the stickied thread in the sub for post-match questions, posting identifying information for targeted harassment. Please do not message the moderators if your post falls into one of these categories. Otherwise, your post will be reviewed in 24 hours and approved if it doesn't violate the rules. Thanks!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Residency) if you have any questions or concerns.*
[j2ly6jo] (score 1, diepte 2) I have wide and flat feet and normally wear a Women’s 8-8.5. I ordered a size 9 on-the-clock pair and i wear them with thick Bombas socks all the time and everywhere. Even on a long flight. Lol.
[jja65a7] (score 1, diepte 1) Late here but second this. My Crocs are the perfect shoe for comfort. Just not necessarily perfect for style
[jzqxcvs] (score 1, diepte 1) Can you link the device?
[lro8401] (score 1, diepte 1) Or you could just put a couple pairs of thick socks and a hairdryer to where they are tight.
[j2khwqh] (score 1, diepte 1 OP) Any specific ones you like? 
Those individual toe shoes are hard for me to look at lol
[j2kirfh] (score 1, diepte 3 OP) Oh I meant in terms of work, non-toe caressing shoes. But honestly that sounds amazing
[j2mil8a] (score 1, diepte 1) I buy youth shoes or men shoes and they're wider. I don't have bunions but I have wide feet. 


Also, wearing compression socks for rounds can help with tired feet
[j31i5mk] (score 1, diepte 1) I've never heard of or know what the creepy toe shoes might be, care to link a generic one so I know what to look for? Thanks!
[j32vnbo] (score 1, diepte 2) Google vibram five fingers.  : )
[j2ki25n] (score 1, diepte 1 OP) Yeah it’s a bummer, so many people like them. Not sure when I’ll be able to muster up the energy to do anything more than order a shoe online lol, but yeah that’s probably the best idea
[j2kq0gq] (score 1, diepte 2) I personally mainly wear ultra boost DNAs (comfiest shoes I own for my wide feet), but have a pair of road running altras that are better than any other running shoes I've had
[jsjhgwp] (score 1, diepte 3) Are dnas really for wide feet? I have mild bunions and have been thinking to change my ultra boosts which I've used for 3+ years since they seem a bit tight, even with a.largee.sizem I am able to wiggle my toes comfortably but not sure
[jsjx4fr] (score 1, diepte 4) They're not great for it but def better than other shoes. I just started surgical residency and noticed my bunions hurting more with ultraboost DNA so I've been wearing altras daily and it's been much better
[jsl6bm2] (score 1, diepte 5) Got it, will need to check out altras and hokas as well. Thanks for the tip!
[k708cbq] (score 1, diepte 2) Paradigm— great arch support!
[j2nku9x] (score 1, diepte 1) I wore these not in the healthcare field, but in professional kitchens: the Birkenstock rubber clogs have removable insoles so you can just buy those again when you wear them out, plus you can put extra cushioning in them if you want. They are easy to clean and best of all they were GREAT for my bunions. I second the poster who recommended wearing something like Vibram FiveFingers in your downtime, those have been so good for my feet.

https://www.birkenstock.com/us/super-birki/superbirki-core-polyurethane-0-pu-u\_3866.html
[j9flsj4] (score 1, diepte 1) Which Hokas do you have?
[j9flzny] (score 1, diepte 2) I have the Clifton, but my plan is to get the Bondi next bc it has a thicker sole/cushion!
[krp1890] (score 1, diepte 3) Do it! They are amazing …
[lkk9tqd] (score 1, diepte 1) I havee hoka cliftons and this is LAUGHABLY wrong. They have a narrower toebox than the average shoe. Even my tiny foot is crying in 2x my size.
[m7homtk] (score 1, diepte 2) You should try hokas Stinson 7. I have 2 pairs of them, and although I want to try something different this time, I'm very afraid they won't work as well as my Hoka Stinson 7. Tip: buy a half a size smaller than you usually wear.  I'm thinking maybe this time I would try altras but I love the mont blanc boa on green, and they are always out of them when I go look.
[m7jg19j] (score 1, diepte 3) i got adidas ozweegos and im never getting any other type of shoe. 

  
the break in period is a bit misleading, but besides that i love them. 

they start out very comfortable and then they slowly get more and more uncomfortable for a few months until they're fully broke in. and then after that it's heaven on your feet.
[j2kqfvr] (score 1, diepte 0) General and maybe not helpful advice but I advise my patients to wear a well shod shoe with a wide toe box.  Brooks and Hoka are usually the top recommendations. 

Unfortunately, non-op options aren't great for bunions. You can try pads or toe spacers but there isn't really anything great. Surgery is the (hopefully) definitive fix but it isn't the best procedure we do. Lots of controversy about the best approach and depends on patient factors. I lean towards MIS.  Lapidis is OK but the non-union rate is underreported I think. 

Best of luck!
[ma94yrg] (score 1, diepte 1) Would like to know who you are. Im looking for a surgeon for MIS. I will go to any state for a good doctor.
[ma9cccq] (score 1, diepte 2) Lots of good surgeons out there who do MIS. Open bunions do pretty well too. Look for foot & ankle trained orthopedic surgeon near you, I'm sure you can find one nearby
[j2ksjso] (score 1, diepte 0) Bunions often form as a result of flexible arches, so I would recommend semi rigid insoles. I use powersteps personally. Second I would recommend a toe spacer for between your great toe and 2nd toe.
[j2n9t40] (score 1, diepte 1 OP) Appreciate the professional advice! Definitely going to get those insoles. I’m sure surgery is in my future but it’s hard to find a good time for that. I tried Hokas on in store once and found they kinda hurt my arches but I’m pretty sure I overpronate, so is that pain “good”/corrective and something I should push through?
[j8tnfvx] (score 1, diepte 1) >Powersteps Pinnacle insoles

GReat answer, I've just bought a pair of Altras and ordered some try-at-home camper peus , for a similar problem (hallux) which I probably have since I was a teenager (mid 30s now).   


Do you recommend replacing the altras insoles with the poweresteps? The Camper insoles apparently don't count as parefoor as they have some drop towards the toebox (I'm very new to this so I don't know how this affects biomechanics of a bunion, but keen to improve this by switching insoles. 

 I basically need to replace all of my shoes , so casuals, home shoes, hiking, padel...  yikes what a pain in the wallet.

There's a Chiropody practice nearby that does custom cast insoles and they analize your gait etc and the price is around 250 british pounds. Is this worth it in your opinion as a podiatrist or better probably stick with the poweresteps and hope I can get surgery before midlife :D 

Thanks in advance!
[kb5pmhc] (score 1, diepte 1) Mine have gotten much worse with time. The bone is sticking out so far it makes my foot look broken
[j2l3ri4] (score 1, diepte 0) Once I bought Topo Athletics, I've never looked back. Wide toe box, great shoes (also a runner, use these exclusively now). Cannot recommend highly enough. Topo Ultrafly's have been my favorite for the past 4+ years
[j2n6n1f] (score 1, diepte 1) Yep that true!
[kg4sv3u] (score 1, diepte 1) Are they good?
[krp1fm3] (score 1, diepte 2) Yes!!
[ksizw5a] (score 1, diepte 2) The best thing that ever happened to my feet was Hokas. Getting a black pair for the OR next
[n4y7j93] (score 1, diepte 1) Hi! I’m an RT and I wore Hokas for 2 years and ended up with bunions and tailor bunions on both feet. My podiatrist said my hokas were awesome but I realized that my compression socks caused the pain and bunions!! I switched to open toe compression socks and it helped with the pain a lot. 
That’s a little tip from me to you my friends!
[j2lerqn] (score 1, diepte 0) I have bad bunions and swear by Sketchers.
[j2lhwra] (score 1, diepte 0) New balance wide width or wide Merrell clogs, until you can have them surgically corrected.
[j2lk426] (score 1, diepte 0) Birkenstock Profi Birkis. Very wide toe box.
[j2o5w9z] (score 1, diepte 2) I pay a pretty penny 😇
[kb5p81d] (score 1, diepte 3) A friend just two days ago was talking about selling feet pics. I laughed, I have serious bunions. Is this really a thing ?????
[j2m04ow] (score 1, diepte 0) My podiatrist recommended new balance shoes, 860 or 880.
[jbq871k] (score 1, diepte 1) Hi. Which model do you wear? V11 V12 or V13?
[j2muvep] (score 1, diepte 0) Wide-toe shoes, nothing pushing them together.
[j2n8tj0] (score 1, diepte 1 OP) Curious about how you decided on zero heel drop, I get lower back pain really fast while standing and I’m wondering if zero drop would help with that ? Unfortunately would eliminate a lot of options already suggested here
(20 reacties met lagere score weggelaten)

=== THREAD sa6nf0 ===
SUBREDDIT: r/VetTech
DATUM: 2022-01-22  SCORE: 92  REACTIES: 60
TITEL: Feet and body aches when home :( I can go so hard during my shift, on my feet, running around like a headless chicken and then as soon as I’m home and have sat down and relaxed, when I get up again woah my feet are so sore and I can feel the aches. Anyone else?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[htrggko] (score 33, diepte 0) What shoes are you wearing? And how long have you been working for?
[htrh6x2] (score 16, diepte 1 OP) Crocs lol and compression socks when I remember to, I am going to look into hokas and other brands and a little over a year
[htrixfc] (score 13, diepte 0) Same!  I like a nice hot soak in Epsom salts.  Dr. Teal's Eucalyptus salts are my favorite, they help soothe my chronic allergy congestion as well.
[htrhr55] (score 12, diepte 2) I also wear Crocs. I’ve found them to be the most comfortable option for me, because my feet really swell. It took me a few months before my legs and back stopped killing me after a full day 😂
[htrj771] (score 11, diepte 0) I had terrible trouble with plantar faschiitis and other foot fun.  I switched to a light weight hiking shoe make by Altra, the model s the Lone Peak.  They're not for everybody, but these things literally changed my life.
[htrmoz5] (score 8, diepte 2) Hokas are a literal life saver. Before wearing them, I felt like my feet bones were going to burst out of my feet! But now I actually have energy to get through the day AND my body doesn't feel like dying when I get home - I actually have energy to cook dinner, take care of my own pets or run errands. They're expensive, but you can't put a price on  your health!
[htrmga6] (score 7, diepte 0) This used to happen to me. It was so incredibly painful to walk after I relaxed a bit after my shift. I switched to Pumas last year and it hasn’t happened since. I don’t use any fancy insoles but something about them was a game changer.
[htrqdc4] (score 5, diepte 3 OP) Yeah like my body has definitely gone through the adjustment period, it’s not nearly as bad as when I first started, but on the days we are really busy it’s still pretty bad lol
[htrqmgm] (score 5, diepte 1 OP) Did someone recommend this to you or did you just do research yourself? I feel like I have plantar fasciitis sometimes but idk
[htrsrfz] (score 4, diepte 4) Same! Some days I feel like I’ve been hit by a train 😂
[htrqi31] (score 4, diepte 3 OP) Yeah I keep hearing really good things. There’s just so many shoes to chose from and so many ppl swear by diff brands
[httlk2c] (score 4, diepte 4) I used Hoka one ones for my hard road running for a while and I regretted not buying them sooner. Now I'm wearing down my Hoka trail shoes and they badly need replaced so I'm thinking the croc life or another pair of hokas. Save receipt and claim it as a work deduction ❤️
[htrqqml] (score 4, diepte 1 OP) Epsom salt baths are life
[htslrft] (score 4, diepte 2) I hike a little bit, and found that shoe on the Appalachian Trail sub.  It's one of the most popular hiking footwear out there (based on a poll every year).  Again, they're different.  They have a "wide toe-box", so the fit is very different.  I swear they feel like wearing a tough bedroom slipper.   Most nice running shoe stores carry them, as well as REI.
[htrsqyv] (score 4, diepte 0) Yep same here. Coming back from lunch I have the same problem lol and I wear good shoes and compression socks. When I used to work in boarding and would get 20,000+ steps a day on my days off I’d be so sore I could barely walk (but back then I wasn’t wearing good shoes either) recently I splurged and got myself a leg massager for $200 and it’s helped so much. Definitely recommend it’s worth the investment!!!!!
[htt41fd] (score 4, diepte 0) I read somewhere (it was the internet so who knows if it’s legit) that if you stand for more than 10 hours at a time you should switch between two or three pairs of shoes bc the support needs time to bounce back between wears. I’ve switched to a paid of pumas, asics, and danskos and my feet have felt much better. My lower back pain is not as prominent either. 

Something else I just learned about- if you can spare the $22/month, Planet Fitness has these hydro massage beds. You can get them in 10 minute intervals, and it’s like hot water jets up and down your back. You can focus the areas you want, the strength, and how fast it moves. Even if you don’t use the gym, it’s worth the $22 for the massage beds alone!
[httb169] (score 3, diepte 4) Just gotta find what works for you. If you already wear sneakers, however, Hokas are an easy jump; they're a smidge taller than normal sneaks, but holy crap do they have so much more shock absorption. You can step on a syringe and not even feel it in your shoes.
[htu8jh5] (score 3, diepte 4) Hoka One One Bondi 7s are my go-to. I'm an LVT at an equine surgery center, and there's some days I'm on my feet nonstop for 16 hours a day. Would not be able to make it without my Hokas, for sure!
[htsjl1g] (score 3, diepte 2) I can't reccomend hokas enough, they are absolutely amazing specifically the bondi line.
[htsq6mu] (score 3, diepte 1) AMEN!!! If you can find a CBD blend that would be amazing too! Absolute life saver in my house!
[htrqp3w] (score 3, diepte 1 OP) Wow interesting, thanks for the input!
[htrrwke] (score 3, diepte 0) I had the exact same problem when I was a vet tech, so I decided to try some new shoes out. I went with Adidas Ultraboosts and it was like night and day! My feet, knees, hips, and back no longer hurt and they lasted me forever. I also recommended them to my mother, who has plantar fasciitis, and she loves them! If you want to get them a little bit cheaper, definitely buy an older model because they're basically the same thing anyway and I'm not a huge fan of the way the ultraboost 22's look
[htrt1s5] (score 3, diepte 0) I have the same problem. I have plantar fasciitis with heel Spurs. Compression and decent arch support helps but it’s never fully healed
[httkphn] (score 2, diepte 3) What line of Hokas do you recommend?
[htszi2p] (score 2, diepte 2) Do you have a particular brand you like?  I feel like there are a lot of snake oils hiding amongst the potential real deals.  Not sure how to chose a legit CBD product.
[htrsuz3] (score 2, diepte 1) Do you know what kind of pumas they are?
[htrt904] (score 2, diepte 1 OP) Thank you for this!
[htrtdo0] (score 2, diepte 1 OP) I work in boarding currently but help out in treatment a lot and am hoping to become a vet assistant soon. Busy days in boarding are no joke on my feet
[htu4tcp] (score 2, diepte 2) My podiatrist taught me how to tape my arches. I put vet wrap to some great use 😂
[htrx5qg] (score 2, diepte 0) I use specially made soles in new balance shoes to make this not happen. I'm still tired after a day of work but my body is totally fine. Tried crocs once. My body (feet, knees, hips, back) tried to die.
[hts0el7] (score 2, diepte 0) get inserts! the combination of compression socks and inserts really really helps reduce the pain at the end of the day.
[hts9bos] (score 2, diepte 0) Sounds like you need new shoes and to figure out what (if any) triggers you have. My triggers are NSAIDs (I can take an Advil here or there but after 3 days in a row I swell.) And ingesting too much sodium (I had a brief phase where I was eating a lot of chips. Realized my feet hurt at the end of the day when I ate them)
[htswlkr] (score 2, diepte 1 OP) I have wide feet too fml
[htsyhda] (score 2, diepte 0) I learned the hard way from years of fast food work that shoes are important, but so are insoles and physical therapy. Podiatrists can give you prescription inserts that are way better than dr scholls, and tailored to your issue. Physical therapists can guide you in exercises and stretches to strengthen your feet and leg muscles, keeping the pain at bay. You might think they're strong already, but if they were, you wouldn't be in so much pain after work no matter how much you walked/ran that day.
[httr2j6] (score 2, diepte 0) 1st - visit a podiatrist if you can (we shut down elective procedures recently).  Mine helped me immensely.  Bunions run in my family and I wanted to prevent them.  She found that I was very flat footed and set me up with inserts to correct it.  Such a fucking game changer.  She also had a lot of shoe recommendations and samples.  I was that kid who could barely run a mile, now I run just for a fun fitness routine.  

2nd - get better shoes with good support.  The problem is this is deeply personal.  I love wearing sneakers and do not so well with clogs or crocs.  

3rd - good socks.  I used to use crappy socks from Amazon but switched to bombas and a few sets of compression socks.  My feet no longer feel hot and nasty at the end of the day.  

4th - invest in aftercare.  Epsom salt soaks.  Moisturizers.  Fuzzy socks and slippers.  I even have leg warmers.  

5th - drink enough water and get enough electrolytes/vitamins through out the day.  I used to get horrendous leg cramps that would keep me up all night.  

6th - I’m not sure what your lifestyle is like but see what kind of activity you can add into your day.  I work out and try to keep fit.  I honestly think that weight loss and fitness have impacted me the most.
[htu22u9] (score 2, diepte 0) Those voting Hoka, which ones?
[htwaru6] (score 2, diepte 1) Bondi keeps getting mentioned
[htrtnu1] (score 1, diepte 2) You’re welcome!! I don’t need a lot of foot support, but the cushy insoles have been amazing.
[htrtg0p] (score 1, diepte 2) I started with the Softride Sophia Women’s running shoe but the top layer didn’t hold up super long. Not the thickest material. I just got the Jada Women’s sneaker with the softfoam insoles. Both have been super comfortable but the Jada sneakers are holding up better.

Edit: misspelled a word
[httl3zb] (score 1, diepte 1) Same. I go through periods of time where my heels are super painful, and then recover. I use SuperFeet insoles and they help a lot.
[htsy81g] (score 1, diepte 1) This is what stopped my leg pain as well. Compression socks being a huge part of that combo for me.
[hts3qki] (score 1, diepte 0) Time for new shoes!
[htscbhs] (score 1, diepte 0) I have the same issue. I will hurt literally from head to toe. After work my shoulders, back, hips, knees and feet hurt and I usually can't get up off the couch after I get home so I just sleep on the couch instead of going to bed. I've also been getting crazy headaches after work that turn into migraines sometimes and I don't get much sleep on the nights I have migraines.
[htsdhbg] (score 1, diepte 0) I splurged and bought danskos for this reason. Expensive shoes. Worth twice their cost
[htsdyxz] (score 1, diepte 0) I have severe back pain along with plantar fasciitis. I use Merrill's walking/hiking shoes (not boots). They are a little more on the expensive side, but they have worked wonders for me. They have also done well throughout my pregnancy thus far - no ties, anti-slip soles, ankle protection, etc. My back pain has gone after I've started using the same shoe type (and added in a Turmeric supplement) for the past 6 years.

I'm now 8 months pregnant and I've worked through the whole pregnancy so far. These shoes have still prevented the plantar fasciitis from acting up. I'm having some ankle swelling and back pain related to the pregnancy but not otherwise.
[htsf497] (score 1, diepte 0) Not just compression socks, but also the sleeves for your calves. They have been left changing for me.
[htsqlak] (score 1, diepte 0) My biggest game changer was finding a shoe that truly fit the WIDEST part of my foot! You can have the best supports and blah blah blah but if the shoe “fits” your foot but doesn’t FIT the widest part of your foot even after breaking them in to stretch? 😬 nah my dude. BIG NAH!
[htt9bpe] (score 1, diepte 2) Have you considered Vessi’s?? They are rather fitted but I ordered a half size up and then they stretched to my foot and from then on I was GOLDEN
[htto6wn] (score 1, diepte 2) I have to use inserts so when I bought new sneakers I had to search for a wide toe box to accommodate them.  Thankfully you can google search this pretty easily.
[htsu00w] (score 1, diepte 0) Shows with good support.  I had a similar problem when I wore crocs.  Now I wear running shoes.  Supportive insoles, lightweight flexible soles.
[htt9e8x] (score 1, diepte 0) Lots of good recommendations here. There are some days where my hips and thighs are sore. Good thread. Thanks for bringing this up, op. Hope you have more painless workdays.
[htth6rb] (score 1, diepte 0) YES!!!
[httl5wl] (score 1, diepte 0) If you can it might be a good idea to see a podiatrist. And then custom orthotics, compression socks/stockings, and good shoes (I like my ~professional~ Birkenstock’s) Your posture might also be affecting your feet!
[htu0vtd] (score 1, diepte 0) everyone here has awesome advice. make sure to keep hydrated too! water works wonders.
[hu56c58] (score 1, diepte 1) I loved the one ones
[htu3944] (score 1, diepte 0) Would recommend the working line of crocs (they look like clogs), you get a good inch of cushion to work with. I used to have insane pain after a long day at work but after swapping to those I haven't
[htujezk] (score 1, diepte 0) I’m mostly fine while I’m working, but the second I sit in the car it all hits me and I get exhausted. I also have chronic pain which doesn’t help on top of being on my feet all day. Good compression socks help some (especially if they have added arch support) and topical magnesium (I use theraworx foam) works wonders for soreness and muscle tension.
[htuu2uh] (score 1, diepte 0) Idk how to help because I'm literally experiencing this right now lmao
[htux2fa] (score 1, diepte 0) since i’m on my feet all day, i like to sit 90 degrees up the wall so my feet are completely vertical for about 20 minutes, it helps with blood circulation not only in your legs but also for your organs!
[htvbuzg] (score 1, diepte 0) Put some Dr. Schol’s gel inserts into your crocs. They will support your arches better than the crocs, while the crocs give you the cushion that you need. Edit: I hate autocorrect

=== THREAD zq8i48 ===
SUBREDDIT: r/cna
DATUM: 2022-12-20  SCORE: 25  REACTIES: 60
TITEL: What are your favorite shoes to wear during long shifts
POST (source_id=post):
I am a somewhat new C.N.A and I've been struggling with feet pain during 12 hour shifts. My facility doesn't allow crocs Sadly so I've been looking for some good shoes to keep my poor feet alive. What shoes have been a life saver for your work days? Any recommendations for brands or shoe styles will be appreciated.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j0wvjs7] (score 33, diepte 0) I wear sketchers with memory foam and compression socks. My legs never hurt on my 12s
[j0wue7o] (score 14, diepte 0) Hoka Bondi 7s are my faves. My coworkers wear OnClouds as well and love them.
[j0ww0kh] (score 10, diepte 1 OP) Do sketchers run true to size in your experience? I need to get me some compression socks as well, thanks for reminding me :)
[j0x289q] (score 10, diepte 0) I’m dating a podiatrist and she always recommends Hokas! I have them and wear them for 12-16 as an RN now and love them!
[j0x0d59] (score 9, diepte 0) Hokas, specifically bondai 6’s or 7’s. However, I think compression socks make the BIGGEST difference and that’s a hill I’ll die on.
[j0wux09] (score 8, diepte 1 OP) I've been looking into the Hokas! Heard a lot of good things about them? Do they fit true to size? I'd have to order online because I haven't found them in store near me sadly.
[j0x5omg] (score 7, diepte 1) Just got a pair of these and 10/10 recommended. Life changing!!
[j0xx7dw] (score 6, diepte 1) i second this. ive used the sketchers sport w memory foam and without laces for convenience. been using for 8s and 12s for a year now and have no complaints. about $40 or so and worth it!
[j0wzpk8] (score 6, diepte 0) Brooks ghost
[j0wwhvr] (score 5, diepte 2) They do! I also ordered mine online. I wear a 9-10 in women’s and I have super wide feet and the 9.5 Wide fits perfect for me.
[j0y7fuf] (score 5, diepte 0) Crocs, sorry 😭
[j0x0l1p] (score 4, diepte 0) My slip-on vans.
[j0x1g7n] (score 4, diepte 0) I love my cloves!
[j0yu2cv] (score 4, diepte 0) i wear Dansko clogs with compression socks and my feet rarely hurt after my shifts. they’re a miracle.
[j0xhtb6] (score 3, diepte 1) I recently bought the Hoka Bondi as well, and found them to be super supportive for my feet. I feel as though the front of the shoe is naturally wider than others such as my Brooks 14. Therefore, I went down half a size :)
[j0wvfjq] (score 3, diepte 0) Dansko Professionals (clogs)
[j0wvw37] (score 3, diepte 0) I invest in Hoka! Like walking on air. My feet rarely hurt.
[j0xd43j] (score 3, diepte 0) i use the bistro crocs, they don't have holes but still are crocs so its super comfy!!!
[j0zqr4s] (score 2, diepte 4) I have the newest Bondi's and absolutely love them. My wife works in surgery and had recommended them. I've worn Brooks and OnClouds as well. The Brooks were good, but my OnClouds were absolute trash. Not nearly enough support in their shoes IMO. 

Check retailers around your area for discounts for healthcare workers. A shoe shop in my city offers 20% off for us.
[j0xjyzt] (score 2, diepte 2) I love how the front of the shoe is made too! The squarer toe helps relieve foot cramps for me.
[j0ymryz] (score 2, diepte 2) I would say they are true to size! :)
[j0z5m7x] (score 2, diepte 1) Compression socks is great advice :)
[j0x5e9r] (score 2, diepte 0) Go to a running shoe store where they measure your feet and gait and get shoes there! Going to a fleet feet and buying shoes and inserts there lowkey changed my life not even gonna lie. I found Altra shoes there which have an extra wide toe box and my feet feel much better now, it made a HUGE difference. If anyone else has terrible bunions look into Altra shoes lol
[j0xcp38] (score 2, diepte 0) I wear on-clouds best shoes I've ever had, real pricey tho
[j0xzcws] (score 2, diepte 0) Hey dudes.
[j0y2bmv] (score 2, diepte 0) New Balance Fresh Foam V4, these things sole is soooo thick it kind of makes the shoe look ridiculous but it is super comfortable right when you stick your foot inside the shoe.
[j0zpg71] (score 2, diepte 1) They’re my favorite too and the Nike outlet frequently has them on sale.
[j0zlbuq] (score 2, diepte 0) Birkenstocks saved my feed when I entered nursing.
[j10tm17] (score 2, diepte 2) Why would you think ANYONE would wear sandals to work?? Try a simple internet search of Birkenstocks
[j10je8v] (score 2, diepte 0) Crocs are disgusting. No one should be walking around with holes in their shoes. Hokas are great.
[j0xm0wq] (score 1, diepte 2) Ordered the Bondi 8 hokahs, I don’t reccomend the 8 because my feet still hurt and I’ve only had them for 3 months.

I’m gonna try the 7 I hear those are better. I like cloves but not enough support. But they’re slip resistant
[j0xu45n] (score 1, diepte 3 OP) The Bondi 7s are out of stock in just about every color in almost all sizes besides the peach everywhere I looked. If you find somewhere that has a lot in stock let me know please 🙏
[j10xcuh] (score 1, diepte 1) I got the Hoka Bondi SR’s and they are absolutely amazing! I have Bondi 7’s too and they’re great but the SR’s are even better.
[j0wvghi] (score 1, diepte 0) Dansko Professionals (clogs)
[j0z6sad] (score 1, diepte 1) Agree
[j0zylpq] (score 1, diepte 1) Yeah, Hokas are the best. I recommend them to everyone in healthcare that I know
[j0x8e4u] (score 1, diepte 0) I have found now that I am working 12’s , KIZIKS work best for me. Even better then my Hokas which I absolutely love.  Well worth the price.
[j0xejlo] (score 1, diepte 0) Sketchers and compression socks are the savior of my shifts
[j0xw27x] (score 1, diepte 0) whatever shoes… just get CUSTOM orthotics!!! literally saved my feet/back/everything!! also recommend from an actual podiatrist
[j10x2cv] (score 1, diepte 1) I love crocs. It’s the only shoes that I wear at work
[j0y8ntt] (score 1, diepte 0) I wear the Nike Pegasus Zoom’s and my feet never hurt after working a stretch of three 12’s!
[j0y99i4] (score 1, diepte 0) I used to wear new balance, I love them. My partner got me Vessi runners and I'll probably never go back. They are pricey but your feet with thank you. 

Also, compression socks are a game changer.
[j0yqmb4] (score 1, diepte 0) If you overpronate like me, the HOKA Gaviota 4s are a game changer! My husband also just bought me my first pair of Cloves for Christmas, so we'll see how they stack up with insoles.
[j12n4in] (score 1, diepte 3) …just did …they’re sandals just like thought. why are you wearing sandals at this job?
[j13zwtg] (score 1, diepte 4) I’ve seen plenty of doctors wear these 

https://www.evoosense.com/products/unisex-boston-suede-footbed-clog?variant=42e9d5af-87f9-4dc4-bacc-bc8b792d4daa&gclid=Cj0KCQiA-oqdBhDfARIsAO0TrGFRpYl-siroVD6fKc_GtTl8OXRMB_SsNbtBULokGLGrAGPoobz2eG8aAoXdEALw_wcB

Not exactly a sandal
[j16csvm] (score 1, diepte 5) ok that one is a mule. still not a shoe for this job! yall really wear mules for this job???
[j112877] (score 1, diepte 2) yeah birks dont just make $150 sandals….
[j0zufpp] (score 1, diepte 0) [Gait Happens](https://gaithappens.com/?fbclid=PAAaZFuFXm0pOvrcd_3rJx8cShPDSYJPr_NNGGQNqtU1VpvBQwJBsHwVOTugY)

Highly recommend looking into strengthening your feet and transitioning to barefoot shoes. Your feet will be healthier and happier.
[j0zycmw] (score 1, diepte 0) My Hoka Bondi 7’s have saved me from so much pain. They’re expensive but worth every penny
[j105qwe] (score 1, diepte 0) New Balance Fresh Foam More V3 or the newest one, the More V4. They are the softest shoes I’ve ever worn.
[j107s7c] (score 1, diepte 0) Brooks!!!!
[j10a27m] (score 1, diepte 0) crocs! fuck your facility! this job is tough and it’s important to be comfortable which is why we wear scrubs so why tf can’t you wear crocs???
[j11f4gi] (score 1, diepte 0) Merrell shoes
[j12nyd3] (score 1, diepte 0) Honestly for me it’s not the shoes but the memory foam insoles. I can wear any shoes I want with them! They are just the SOF COMFORT women’s from wal mart. 

For context: I work 2 16s back to back (weekend package) and never *ever* come home with achy feet.
[j0xdxsa] (score 0, diepte 0) I wear Sketchers or Crocs nursing clogs.
[j0yhytb] (score 0, diepte 0) Clove
[j0yunol] (score 0, diepte 0) Cloves! Run true to size. I love them.
[j10ahqe] (score -1, diepte 1) so sandals??? who tf wears sandals to do this job? unless there is a different kind of birks i don’t kno about

=== THREAD yg06yz ===
SUBREDDIT: r/AmazonFC
DATUM: 2022-10-28  SCORE: 86  REACTIES: 60
TITEL: Got them secured. My feet have been feeling dead these past few weeks
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iu64fft] (score 62, diepte 0) Amazon should go ahead and sponsor these shoes because everybody and their momma has them. 😂
[iu64w0e] (score 14, diepte 1 OP) Ha ha yeah I saw the post earlier about these shoes. They look nice and alot of people apparently have em. Definitely down to give these a go.
[iu71p4t] (score 14, diepte 2) I think people want to wear them for the comfort part? Don’t be so narrow minded not everyone gives a fuck about fitting in we just don’t want to come home with blisters on our feet lol
[iu7j1cj] (score 8, diepte 2) My site is only 1 per year, timberland pro only lasted me 6 months
[iu7ncwt] (score 7, diepte 5) On standby to downvote your next post
[iu66fjn] (score 6, diepte 1 OP) Furuian Steel Toe Shoes for Men Lightweight Indestructible Work Sneakers for Women Puncture Proof Comfortable Slip On Safety Shoes for Industrial,Coustruction https://a.co/d/cgxDJsV
[iu7anvg] (score 5, diepte 0) anyone know how i order my zappos shoes? i think im allowed another pair by now, been over a year
[iu7lwcf] (score 4, diepte 3) The fact that you’re so uptight and worried about what people wear is sad asf
[iu6nncl] (score 4, diepte 1) Sell them on ebay or mercari
[iu754g1] (score 4, diepte 0) I didn’t know these were safety shoes, i thought they were some hype shoes 😂
[iu7e0wj] (score 4, diepte 1) 2 a year
[iu89bl8] (score 3, diepte 5) It auto applies. Just make sure you get all the way to just before the part where it asks for your card to charge it
[iu8tdhb] (score 3, diepte 0) Your feet would do better if you got some Redwings
[iu7ya69] (score 2, diepte 3) You sure? My place said once a year but I got the discount as soon as June 1st hit
[iu7za28] (score 2, diepte 4) where do i find the discount 💀
[iu81wmm] (score 2, diepte 5) It should show up when you go to check out on “zappos at work”.
[iu7pp13] (score 2, diepte 1 OP) Women too
[iu7sgcl] (score 2, diepte 0) I was struggling with the zappos garbage shoes. Went to Redwing and got sized by their 3D scanner. They also have a digital weight pad you walk on for the computer to pick up where most of your weight sits in your feet. System recommended shoes and different options for my feet and the fact that I walk on concrete floors. I spent 150 bucks but worth every penny!
[iu8ea09] (score 2, diepte 2) Typical.
[iu9gt4t] (score 2, diepte 0) $50+ for some made in china, most likely wouldn’t actually save your toes if something with substantial weight fell on them doo doo ass shoe. Pass on that.
[iua2jih] (score 2, diepte 0) Damn, no wide sizes. 😤
[iu63sgy] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[iu7paei] (score 1, diepte 1) With sticky Cheeto fingers
[iu65t1x] (score 1, diepte 0) Do you have a link to these?
[iu69tv7] (score 1, diepte 1) https://www.amazon.com/Furuian-Lightweight-Indestructible-Comfortable-Coustruction/dp/B095X161G6
[iu90ley] (score 1, diepte 1) Safety shoes are designed to protect against sudden impacts up to like 75-100lbs iirc, and even then they might flex inwards. They might be able to hold more weight if the weight is applied slowly but even then we're talking like an extra 100-200lbs. A PIT weighs several thousand pounds, absolutely nothing will stop it from obliterating your feet.
[iu91bc4] (score 1, diepte 2) Which is why I said what I said. There’s a video of the shoe being ran over though lol
[iu94m0v] (score 1, diepte 3) Didn't realize there was a video. Lmfao, they BARELY touched the tip of the toebox with the tire's edge, so there was hardly any pressure being applied. 5,400lbs my ass LMAO
[iu9781e] (score 1, diepte 4) Yeah it’s an actual joke.
[iu6hsvc] (score 1, diepte 0) Are they comfy?
[iu7bve0] (score 1, diepte 1) You need FP insoles
[iu7zkqb] (score 1, diepte 1) Same I thought they were some adidas
[iu8p2ym] (score 1, diepte 6) thank u both
[iu90krj] (score 1, diepte 4) Yeah I tried again and it’s only going to give me $30 off instead of the whole price
[iuau067] (score 1, diepte 5) Oh damn. When did you get hired?
[iu7mqfq] (score 1, diepte 0) Are these for men? Only
[iu8dp2u] (score 1, diepte 1 OP) Own cash
[iu8vsgs] (score 1, diepte 1 OP) Anything is better than the total bricks that I currently wear
[iu94xlb] (score 1, diepte 0) Can I get these with Zappos?
[iu9inet] (score 1, diepte 1) Nope
[iu9koi9] (score 1, diepte 0) I need a new pair so bad. Recently got some major blood blisters on my feet and im not havin fun 😂😂
[iu6fceu] (score 0, diepte 0) I have these. Listen order dr scholl’s heavy duty, breaking these shoes in I can’t explain how painful it is if you don’t have dr scholls
[iu6oa9b] (score 0, diepte 0) I wonder if these are any good for people with flat feet
[iu6xjpi] (score 0, diepte 0) Advice: order a half size bigger because your feet will probably swell after standing for so damn long. Works for me pretty well
[iu7e8dl] (score 0, diepte 0) What the name of the shoe tho?
[iu7k44s] (score 0, diepte 1) Just type in safety shoe or composite shoe in the Amazon app search and they'll pop up. They're so many "off brands" that sell these shoes.
[iu7jfft] (score 0, diepte 0) If no one ask you how fast you can run in those shoes...
[iu7pc9f] (score 0, diepte 0) What brand is that ?
[iu8c0nm] (score 0, diepte 0) Is this on Zappos? Looking to use my discount on these but don’t see them. Or do you need to buy these with your own cash?
[iu69u7v] (score -1, diepte 0) https://www.amazon.com/Furuian-Lightweight-Indestructible-Comfortable-Coustruction/dp/B095X161G6

I would not recommend running your shoe over with a car/PIT though… idk what their trick is but that’s a good way to lose your toes.
[iu688iw] (score -3, diepte 1) This.
[iu72gjq] (score -5, diepte 2) “This.”
[iu7jtys] (score -5, diepte 0) I was the first to wear these at my FC when the safety shoe rule started and now everyone has them. 😂😂
[iu7vfsn] (score -6, diepte 4) Just like everyone is uptight and worried about my opinion 🤣
[iu6nqsp] (score -35, diepte 1) Only reason people wear em is because they are follower, they see other wear em and want to join in the band wagon. Only a few genuinely like them for its aestethics not because it's what's hot and popular. Also they have an element of the nike huraches and nearly resemble yeezys 🤣

