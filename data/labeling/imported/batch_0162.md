# Label-batch batch_0162

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
Schrijf het resultaat naar `batch_0162.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1qa2jac, 1pq5wxf, 1mjhsop).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1qa2jac ===
SUBREDDIT: r/Teachers
DATUM: 2026-01-11  SCORE: 13  REACTIES: 59
TITEL: Slip-on shoe recommendations for teaching in your third trimester?
POST (source_id=post):
Hi! I hope this is OK for this sub—I’m hoping for some guidance/experience from people who have worked as an educator while pregnant. I’m a high school librarian, and I’ll be 32 weeks (8 months!!) on Monday. The struggle to tie my cute, cushy little white Dr. Scholl’s sneakers every morning is just getting to be too much—what recommendations do you have for some comfortable slip-on alternatives?

I’ll be on my feet a lot generally, but especially in the next 2 weeks as we kick off a new semester of research instruction and PBL. (I’ve also ordered some compression socks, which I’m hoping will arrive soon.) Arch support and/or footbed padding are the way to my heart and sole. All recs appreciated!!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nyzkink] (score 45, diepte 0) Sketcher slip ins!!! I couldn’t reach my feet if I wanted to.
[nyznr3s] (score 30, diepte 0) I teach middle school. When I was pregnant I had terrible swelling. I gave up and wore Crocs. 

I bought the silliest pair I could find. 

They were wonderful. The kids thought they were hilarious. My coworkers thought it was genius.
[nyzo7hi] (score 25, diepte 0) I love Birkenstock clogs. I wear them all winter.
[nyzkg78] (score 18, diepte 0) Kiziks!
[nyzsxnv] (score 11, diepte 1) Kiziks are even better! Sketchers are a second fave though.
[nyzy8o9] (score 9, diepte 1) Yeah, I’m your third trimester nobody would say anything if you showed up in bunny slippers.
[nyzp72w] (score 9, diepte 0) I swelled so badly that I couldn’t wear anything but my Birkenstocks with the straps loosened.
[nyzlpg0] (score 5, diepte 0) I embraced my inner 80 year old woman and got velcro shoes 😂 I also had a pair of sperrys that I put a gel insert into and that worked pretty well for me.
[nyzsyhd] (score 5, diepte 1) Second these ^^ currently 8.5 months and they haven’t let me down
[nyzt1b5] (score 3, diepte 1) I just discovered these a month ago and I'm obsessed with them. I bought two pairs and my kid ended up getting a pair for herself. I'm never going back to another brand of sneakers and snow boots.
[nyzte1l] (score 3, diepte 1) This and they come in wide and extra wide, game changers
[nz00qgw] (score 2, diepte 1) Adding another support vote for the Sketchers option! I ordered a half a size up
[nyzklo2] (score 2, diepte 0) Hi try the Vivaia shoes (I think they're Korean shoes but they do ship international), comfiest shoes I have and no need to add any extra padding
[nyzl8mz] (score 2, diepte 0) Hey, I’m 32 weeks today! We’re almost due date twins! 

A lot of my teacher friends swear by Danskos. I personally just loosened my sneakers and am wearing the same shoes in an easier to put on version, haha.
[nyzme7w] (score 2, diepte 0) My baby was due in August so those first 2 weeks of school were brutal. I wore slip on sandals from Amazon, the brand was cushionaire and they were fabulous because they were adjustable!
[nz01agi] (score 2, diepte 1) Currently 30 weeks pregnant and asked for birk clogs for Christmas for this reason! Have been great but I’m also still wearing my vionic booties which are still extremely comfortable and I can pull them on with one hand.
[nyzr8a6] (score 2, diepte 0) Stegmann. They make WAY more than just the boiled wool felted clogs they’re famous for. Cork footbed, fits my custom orthotics. 

And they make my size 10 feet not look massive so that’s a win.
[nyzubgm] (score 2, diepte 0) Kiziks. Wore them through two pregnancies and even though I could go back to "regular shoes" now that my youngest is over a year old, I bought another pair of Kiziks instead. They're great for when your hands are full of toddler/baby/stuff and still need to put on your shoes or you need to put shoes on fast to run after someone.
[nz03q1j] (score 2, diepte 0) Kuru makes really comfy shoes. I wasn't pregnant, but they kept my back from hurting.
[nyzxssy] (score 1, diepte 1) They’re perfect! I still use mine, and have bought even more pairs since having my baby
[nyzxw4b] (score 1, diepte 1) I came to say Kiziks too!!! 

They’re SOOO comfortable. I have the plain white ones with laces but I slip them on and off.
[nz2bqpq] (score 1, diepte 1) I have 3 pairs! Comfy and cute! Love them! Now I’m annoyed by any shoe that requires me to actually sit to put them on.
[nyzs4it] (score 1, diepte 1) I second this!
[nz00v7m] (score 1, diepte 1) I hate the step ins! By the end of the day, the back of my heel hurts so bad from that hard plastic piece. Skechers have been my go to shoes for so long I don’t know what to do now 😭
How do you keep your heel from hurting?
[nz01j2v] (score 1, diepte 1) I just order my regular skechers a half size up and they slip on and off easily.
[nyzp2lv] (score 1, diepte 1) Had a baby in June. I have two pairs of Nike Air Maxs that I love, and this is what I did. Just keep them tied a bit loose and slip your feet in.
[nyzth9m] (score 1, diepte 1) Sketchers also makes a boat show that is great.
[nyzluxv] (score 1, diepte 0) Orthofeet!! You can customize with free inserts & arch supports. I taught in them during my last pregnancy and they were fantastic.
[nz0shdc] (score 1, diepte 1) Yep! After the Dr Scholls sneakers, this is second best!
[nyzoqx0] (score 1, diepte 0) I wore slippers because nothing else fit lol
[nyzqd2r] (score 1, diepte 0) Dansko clogs, especially the line that has embedded cushions.  I LIVE in these.  Easy on and off but stay on my feet just right.
[nyzscbo] (score 1, diepte 0) Cloudies!
[nyzsnsa] (score 1, diepte 0) You can buy stretchy shoelaces for your regular shoes to make them slip-ons! I have used "Xpand No Tie Elastic Shoelaces" in my daily wear sneakers and they worked great. (Disclaimer: they did wear out after about 5 months of everyday use, but well worth the $10 for me!)
[nyztnru] (score 1, diepte 0) Nike Fly Ease! All I wore for my 3rd pregnancy and was great post partum when I had my hands full
[nyztt30] (score 1, diepte 0) Danskos
[nyztx15] (score 1, diepte 0) I've been wearing those knock off UGG clogs from Amazon and they are surprisingly comfortable. Currently 27 weeks pregnant
[nyzwkj0] (score 1, diepte 0) Kiziks were great when I was pregnant but I had to add inserts for extra arch support
[nyzzz73] (score 1, diepte 0) Instead of buying new shoes (unless you need better shoes, then I've got recs for days), you could buy some Lock Laces and replace the tie laces in your shoes with those. They're only $10-$12 a pair, extremely durable, and easy to install by watching their YouTube tutorial video. If you order through their site, they even do bundle deals on multiple pairs.
[nz00kuh] (score 1, diepte 0) I’m pregnant and in my third trimester too! Does anyone have recommendations for winter shoes especially? I live in Utah. I have Birkenstocks which have definitely gotten lots of use but looking for more of a cold/snow shoe when I’m out at recess duty.
[nzm2vjm] (score 1, diepte 1) Kizzik has a hiking boot called the Wasatch I believe. I have a pair that are super comfortable and good on ice.
[nz00wz6] (score 1, diepte 0) Another vote for sketchers slip-ins! I got hooked after I had a surgery where it was hard to bend over for a while. I wear them all the time now!
[nz00y7g] (score 1, diepte 0) I have slip on crocs that are super comfortable!
[nz03zii] (score 1, diepte 0) Sperrys or tieks
[nz04sta] (score 1, diepte 0) I teach middle school and have loved Birkenstock Boston clogs (the Amazon version) with both of my pregnancies
[nz058ky] (score 1, diepte 0) I LOVE the Taos slip-ons. Pricey, but so comfortable that I wear them every day. Amazing footbed and arch support. In my opinion, super worth it.
[nz05xue] (score 1, diepte 0) Compression socks and "recovery slides"
[nz05yxm] (score 1, diepte 0) Nike has a pair of accesible sneakers that you step into!
[nz08mqg] (score 1, diepte 0) Crocs for the win! I was a nurse and wore them while on my feet all day and most of the other nurses wear them too! I didn't know it at the time, and I don't know why it didn't occur to me, but they are orthopedic shoes. That's why they're so expensive
[nz099an] (score 1, diepte 0) Sketchers slip ons (I got the wide fit while pregnant) and crocs. Those were pretty much my options by the end.
[nz0aepe] (score 1, diepte 0) I got sketchers brand crocs - loose for my giant feet and had more arch support than regular crocs. Didn't have to bend down to put them on
[nz0ah3x] (score 1, diepte 0) Danskos if you can afford them. 

I also wore Keens for most of my third pregnancy
[nz0igsg] (score 1, diepte 0) I’m really enjoying my Rothy clogs right now. You can get them with studs, with a buckle, or just as is. I have the unadorned ones. Very worth the price.
[nz0ngn4] (score 1, diepte 0) I’ve only been heavily pregnant in the summer and I wore Birkenstocks and crocs sandals exclusively. If it was winter I would wear Kiziks, Birkenstock Bostons but like the big buckle lined or Boston rivets OR the platform teddy shearlijg which are ridiculous but so cute, backless UGGS like the Disquette, Crocs Dylan Platform Lined Clog
[nz0nkp3] (score 1, diepte 0) Definitely Sketchers slip ins.
[nz0zsa6] (score 1, diepte 0) Sketchers.
[nz106rq] (score 1, diepte 0) I have a pair of white slip on On Clouds that I made work with basically every outfit I had! Those things saved me and kept me on feet teaching 8th graders until 36 weeks when sweet summertime hit.
[nz1fukh] (score 1, diepte 0) I lived in Kiziks during my third trimester! I have since purchased them every time a friend is pregnant or injured and can’t bend well.
[nz1j8ia] (score 1, diepte 0) Literally whatever you can find!  I had 1 pair of men’s flip flops I could wear.
[nz2hhhp] (score 1, diepte 0) Crocs
[nz4gal4] (score 1, diepte 0) Depends on your budget, but Olukai shoes are my favorite shoes I’ve ever owned. I recommend these if you like a standard “Vans-style” slip on: https://olukai.com/products/pehuea-luxe-womens-suede-slip-on-shoes-tapa?variant=42628795433059 

and these if you like a bootie (my favorite shoes I’ve ever owned): https://www.dsw.com/product/olukai-hawaiiloa-manu-hope-sneaker-boot---womens/604574?activeColor=259&size=8.5&width=Medium&cm_mmc=CSE-_-GPS-_-G_Shopping_PLA_PMAX_Boots_Booties-_-&cadevice=m&gclsrc=aw.ds&gad_source=1&gad_campaignid=21497709831&gbraid=0AAAAADRIb9RURwJvZRpF7SDuZUYPt49Oa&gclid=Cj0KCQiAsY3LBhCwARIsAF6O6XhL9vlP7JV5mk75aVO0UUaUkxLyFnTPlSbBur2TB9g0ASMpO9UJV70aAokpEALw_wcB

=== THREAD 1pq5wxf ===
SUBREDDIT: r/AdvancedRunning
DATUM: 2025-12-18  SCORE: 13  REACTIES: 59
TITEL: Dealing with super shoe fatigue
POST (source_id=post):
Curious if anyone has advice for dealing with the fatigue that comes from the low stability nature of super shoes. I did a workout this morning in super shoes and aerobically I felt fine, muscularly I felt great, but it felt like I was struggling to stabilize through my ankles, especially with the small amount of camber on the road. My ankles and feet feel exhausted now, though I definitely think I have less fatigue in other parts of my body. 

  
Is the solution just running more in super shoes? Right now I'm only using them for one workout a week because of cost + mainly they beat my legs up so much. Should I use them more than once a week?

  
The rest of the time I'm running in stability shoes with green superfeet insoles. These don't fit in my alphafly's. 

  
Wondering if anyone else has overcome this / anyone has good advice.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nurt6wd] (score 85, diepte 0) The solution is not running in super shoes and pulling out a more stable supershoe on race day.
[nurx34o] (score 33, diepte 0) Not all super shoes are unstable.
[nuwaq7p] (score 15, diepte 2) but if the 'supershoes' are not suitable for your overpronation then all that research is irrelevant to you....
[nusgtjg] (score 13, diepte 2) Superblast 2 are excellent up to marathon pace. Legs always feel better when I use them for my long runs. Super stable and still have pop to them.
[nus9kad] (score 13, diepte 0) I run in super shoes or super trainers everyday. No issues. Better running economy and reduced impact from the premium foam. Win win.

You should do foot and ankle mobility exercises so you can learn to not run in stability shoes. Stability shoes have extra support, which adds weight to a shoe. Extra ounces on a shoe will impair your running economy.

In the meantime, if you want a faster shoe that offers more support for track sessions, check out the ASICS Megablast, Sauciny Endorphin Pro, and New Balance Supercomp Elite 4. These all have premium foams, but added stability compared to shoes like Vaporfly, etc.
[nutrtv8] (score 11, diepte 4) This only really matters when you're winning races/prize money. If this is OP's first time in super shoes then it's safe to assume they're not winning races/prize money at the moment.
[nurv332] (score 10, diepte 0) there are single leg form drills you can consider, e.g.,  single leg RDLs with body weight then later with dumbbells/kettlebells. ankle range of motion exercises, balance drills using a bosu ball,  banded ankle exercises and tode exercises
[nuru9rj] (score 9, diepte 0) I’d try a different shoe. It is hard to know from just trying it on but maybe you need something a little less aggressive/more stable? I’m thinking like the metaspeed edge or sky, but you should at least try on a few shoes and see how they feel.
[nust0ki] (score 8, diepte 0) Stability shoes give you weak feet and ankles so you aren’t able to run strong in super shoes. Ditch the stability shoes for neutral shoes and slowly build up leg strength so you can run in anything.
[nuruak8] (score 7, diepte 0) Maybe try mixing it up by running on some trails or even some grass?  That would help strengthen the areas that are becoming fatigued.  I’m probably half road and half trail and haven’t ever had an issue with super shoes for road or trail (I have and use both).
[nusdmpy] (score 7, diepte 0) I do think trail running is a really good way to strengthen your ankles and train yourself  neuromuscularly to adapt to uneven terrain.
[nuslx6h] (score 5, diepte 3) I second the Superblast 2s. I credit them with saving my season.
[nusksat] (score 5, diepte 1) Running in a new shoe that you aren't adapted to on race day is a great way to get injured.


You definitely don't need a plate to run well, and if OP can't find a comfortable one then it may mean they'll perform better in a more comfortable non-plated option.
[nusmpr7] (score 4, diepte 2) Absolutely the Superblast 2
[nuuebdt] (score 4, diepte 2) Asics Superblast 2 as mentioned and the Megablast. Megablast is a better SB2 imo (and a lot of other people agree). I've raced 3 Half marathons in the MB this year and set 3 PRs. I'm sure I would be quicker with a carbon plated shoe but the Megablast has served me well.
[nurt42p] (score 3, diepte 0) I only wear them for races.
[nuuqx40] (score 3, diepte 3) I’m staring at both my SB2 and MB at the moment, trying to decide which ones to slip on for my workout. They’re both awesome (I prefer the MB)
[nuv5f07] (score 3, diepte 4) Which did you go with? I usually wear Megablast and EVO SL for faster workouts (threshold to 10K pace) and SB2 for long runs, tempo and steady stuff. Just finished a workout with the EVO SLs and they felt good (I'm sure the MB would have been just as good).
[nuvex2u] (score 3, diepte 2) Adidas Adios 9
[nuvdm7v] (score 3, diepte 1 OP) my coach cited a study and said that training in super shoes for speed work helps with adaptations and means you run faster in the super shoes on race day than if you were throwing on a new pair of shoes. 

Also I believe there are other studies that show that it reduces recovery time from speed sessions. Less familiar with the second one.
[nuwkmi1] (score 3, diepte 2) First, take studies with a grain of salt. There are not a lot of running studies that apply to most people, just because of how these studies are done and the limited pool of runners they do study.

Second, not all "super shoes" are the same. It'd be surprising if you could go from stability shoes to Alphaflys without issue. Work your way up. There are other "racing" shoes out there that aren't considered "super" but might help you build up the muscles you need to stabilize yourself

I'm a big fan of the Saucony Speed line. They use a nylon plate, instead of carbon fiber. Very light, less stable than most shoes, but not nearly as unstable as what most people consider super shoes.
[nv3glo9] (score 3, diepte 2) All irrelevant if you're running like a wobbly deer
[nuwepmq] (score 3, diepte 2) A killer exercise for lower leg stability is standing on one leg and drawing the alphabet in the air with the other with closed eyes. You will wobble a lot and work all small stabilizers below the knee. It sounds like nothing but you will really feel it. I deadlift 200kg/440lbs and had crazy soreness after each session for the first couple of weeks. It eliminated all the problems I experienced with the EVO SL in a few weeks.
[nus0hgf] (score 3, diepte 0) My first taste of unstable supershoes was with the Adidas Adios Pro 2. I felt like a baby giraffe, wobbling all over the place. Years later, I can now run in that same model of shoes (and similar shoes) without much issue. Through repetition and practice I became better at landing more precisely with my stride.

But even after these improvements, there are moments where certain shoes feel unstable. My most stable "supershoes" are the Saucony Endorphin Pro 3 and Endorphin Elite 1 models. There is virtually no wobble in these for me.

So you can practice until you become better at managing your footstrike or you can try out a typically more stable model of shoes.
[nuu9htg] (score 3, diepte 0) I have to do almost all my running in plated shoes due to Hallux Limitus and the inability of my big toe to bend so I've experienced these same issues, had various ankle issues, and tried almost all supershoes.

I would recommend trying the Saucony Endorphin Pro 4 (especially whilst they are currently on big offers).  Their foam is slightly firmer than many, especially in the rear foot, but this combined with a wide centred platform gives you much better stability through the stride. Also they are incredibly comfy shoes, proper uppers, great for wider/high volume feet too. They are by far the most proper shoe like of the supershoes whilst still being far quicker than people give them credit for (context I'm currently a 35-36 min 10k runner so not plodding along).
[nusj7n0] (score 2, diepte 3) I’ve been looking at these and also now the megablast. Going with the evo SL for the moment but the first time I ran with them they gave me tibialis posterior tendinopathy due to the lack of ankle support!
[nusjv01] (score 2, diepte 4) Yeah the SB2s are way more stable than the Evo SLs. I have both in my rotation and know exactly what you mean with the stability issues. SB2s are as stable as you can get.
[nuz9x7e] (score 2, diepte 6) That’s fine but the number of shoes that are above the 40mm stack height would end up excluding a whole ton of shoes that normal people are wearing.  

Including the Hyperion Max 3.  Which Des Linden wore to run the NYC Marathon in November (she was pacing a regular dude).  If a pro runner is going to wear a “prohibited” shoe for a regular runner running time, I’m going to go out on a limb and say that the rest of us are probably OK to do as well.
[nuvb8yt] (score 2, diepte 5) Well, I’m actually away from home & these are the only two shoes I brought (it was an easy choice)! 

I wore the Superblast this morning because I wore the Mega yesterday. 

I typically wear MagicSpeeds for my workouts, or a carbon plated shoe that I’m considering for upcoming races. 

If you had to buy one pair, I would recommend the Mega’s because they’re just amazing.
[nuvdats] (score 2, diepte 1 OP) any advice for more stable or wider super shoes?
[nuvf0ju] (score 2, diepte 2) I don't know any that are inherently 'wider', but, the Hoka Rocket x3 has stability elements.
[nuwc8nk] (score 2, diepte 2) The most stable ones I’ve found are Adios Pro 3 (RIP) and NB Sc Elite 4. I’ve run a 50 mile ultra in the SC4 and had no issues. It does run a little short, so maybe go a half size up.
[nuwqrz3] (score 2, diepte 2) Hoka Rocket x2 or 3
NB Elite v4 (comes in widths)
Saucony Endorphin Elite v1 (not v2)
Saucony Pro v4
Adios Pro 3 
Hoka Cielo x1 v1 (not the 2.0)
[nuszvmt] (score 2, diepte 0) What’s your PR and what shoes are you wearing OP? That’s important to the suggestions you will get. There’s years of research now that still shows a good benefit all the way to 8min/mile. From there to 9min its still close to 1% benefit (so, way less than the 4+% for 5min pace) but specifically research has shown either an insignificant benefit or sometimes a negative effect at 9:40 pace and slower.

There are more firm and stable super shoes out there you could try if you’re in the range where you’re still going to see a good benefit. Honestly a good option is just ordering old model super shoes off StockX, the OG pairs are way more stable and firm than the pillows of today. 

FWIW, the two fastest shoes I have, Puma R3 and Saucony EE2 cause me separate issues. Pumas make my calf and Achilles really, really tight and sore after, without fail, and Saucony makes the balls of my foot start to go numb 20min in. But, I run very fast in them and it’s just a trade off I accept. I think as they get faster and faster it’s similar to road cycling where bikes have gotten insanely light and serious crashes have increased. There’s ultimately a trade off between high end speed and injury risk. Have to determine how worth it those extra seconds to minutes are for you!
[nuvd45d] (score 2, diepte 1 OP) high 70s for the half, so definitely running fast enough for super shoe benefits. 

I think I'm hearing a lot that I should get a more stable super shoe! thanks
[nuvce0j] (score 2, diepte 1 OP) \~6 min/mile or so, so definitely not slow.
[nuwn432] (score 2, diepte 0) For the road camber, I switch sides of the road throughout the run (with traffic/facing traffic).  If I stay on the same side it definitely is a problem.  Same with a track workout, I try to change directions periodically.  This applies to all shoes.
[nusex51] (score 1, diepte 1) Which shoes without a plate / “crazy foam” have you found good? I’m assuming the adidas evo SL doesn’t qualify. I’ve tried the brooks Hyperion tempo and the plain adidas SL and they’re ok but it definitely makes teaching those faster paced intervals more difficult
[nutgpl5] (score 1, diepte 3) Isn't there a World Athletics cap at 40mm for road race shoes (with the Superblast 2 being at 45mm)?
[nuvafys] (score 1, diepte 5) Sounds about like what I do. That said I can pick it up to 3k or mile pace in basically anything these days
[nuve46v] (score 1, diepte 1 OP) I do a lot of trail running and have good balance and strength through my feet and ankles. I think you're correct though that I need to mix it up; likely by adding in more runs with less stable shoes that maybe aren't super shoes.
[nuve0rv] (score 1, diepte 1 OP) I do a lot of strength work and have excellent balance, just apparently not while running. 

I think it's likely because I have adaptations due to how often I've ran in heavily supported shoes that don't let my feet overpronate. 

  
This is probably the better of two evils, because the alternative is crippling post tibial tendonitis :/
[nuwwab4] (score 1, diepte 3 OP) that's awesome, I'll try this out! Thanks.
[nv0wk61] (score 1, diepte 2) The widest ones I know of are the Altra Carbon Vanish 2. Very stable also.
[nv5jykm] (score 1, diepte 2) This just out from Yowana! https://youtu.be/X1fk59eMjR0?si=dqJAhK2bTyuBMQNf
[nusfmlp] (score 1, diepte 1) Might a super trainer like the Saucony Endorphin Speeds (I do tempo & faster work in them and race in Endorphin Pros) give OP most of the muscular benefit of supershoes without the instability?
[nus6im0] (score 1, diepte 0) I literally have no knowledge regarding this issue, but...

Could the experience of "wobble" be related to slower pace/longer ground contact time? I'm thinking "pogo stick"... standing in place on a pogo stick is going to feel wobbly but bouncing reduces the time on the ground you have to wobble?

(Disclaimer: I've raced in Adios Pro 3, but only worn them in training for very race specific sessions. I have about 40km on my new Adios Pro 4 and racing in them on Sunday for the first time. I have not experienced ankle problems in either.)
[nuuwx5i] (score 1, diepte 1) Basically my experience. Going fast they feel great. Slow I'd stop and take them off it just feels like I'm going to roll my ankle.
[nus7qtl] (score 1, diepte 0) I wear minimalist shoes for my non running activities.   This has strengthened my feet and ankle muscles.   The super shoes are a little less stable, but I've never had issues.   I would get used to running in them more.  I normally do at least 1 workout a week sometimes 2 in super shoes.   I find it helps with recovery.  My first few runs in them the stability was a very noticeable, but now they just feel like normal shoes when I'm running.  Walking is still a little awkward is some shoes I own.
[nusn0pe] (score 1, diepte 1) That’s really interesting advice about the minimalist shoes, what kind of shoes specifically?
[nusdd7k] (score 1, diepte 0) A little bit of an aside, but related... Have you all seen some of the videos of some of front of the packers running in their super shoes... Alot of them are having serious ankle roll and somehow it doesn't seem to hinder them.
[nuve78j] (score 1, diepte 1 OP) Agree. I think I'm heavily dependent. I am not going to ditch the stability shoes all at once, but I will try and throw in less stable shoes (or remove my insoles) for my shorter runs and try building it up.
[nutfjfi] (score 1, diepte 0) i’ve noticed the same thing before, aerobically fine but the ankles feel worked after...those shoes really load the small stabilizers, especially on uneven roads,,, i found it better to use them sparingly and keep most runs in more stable shoes so the feet adapt slowly without forcing it too fast
[nutlm83] (score 1, diepte 0) Lookup foot shortening exercises. I have naturally very flat feet and weak toes. I used to wear stability shoes with the green superfeet insoles, but I weaned myself off. 

My daily routine is roll out the arch with a tennis ball, then move myself across the carpet with just the toes.
[nutn1ey] (score 1, diepte 0) i ran into something similar when i first rotated super shoes in. aerobically they felt great, but my feet and ankles were way more taxed, especially on cambered roads. for me the fix was not using them more often, but being more selective about when and where i used them. flat routes and workouts that were more straight line made a big difference. i also found that keeping most easy and moderate mileage in more stable trainers let my feet recover so the super shoe sessions felt better. some basic foot and ankle strength work helped too, nothing crazy. i think once a week is fine if that’s all your body tolerates right now, there’s no real upside to forcing more if it leaves you beat up.
[nuuwpos] (score 1, diepte 0) What pace were you running at? I'd rather run barefoot than in my alpha flys for anyislowrr than 5 min kms. I just feel so stupidly unstable. Going faster they feel great. Some are also more unstable than other with alpha flys being on the more unstable end. Also going from stability shoes to probably the most unstable shoe I've ever encountered is funny and means you probably don't need stability shoes.
[nuvcr94] (score 1, diepte 2) Probably the stability shoes then since you aren't used to using your ankles and feet the same way in the rest of your training. You are just used to basically the entire other side of the spectrum. Other super shoes also are more stable so that could play into it as well.
[nuzb5l4] (score 1, diepte 0) If you’ve got your heart set on a plated shoe and need something more stable, try the Asics S4 (that’s the name of the shoe-not an abbreviation). It’s designed for people working on a sub 4 marathon time, so it’s a bit less light, a bit more comfortable and a lot more stable because it is made for people who will be on the course for longer and they will be more likely to have some form breakdown due to fatigue.  It’s not a stability shoe as in something with medial support, but it’s built TO be stable for runners who will need that extra support in the closing miles of a longer race.  

The New Balance SC Elite v3 and 4 are quite stable-but not quite as much as the S4.  I haven’t run in the 5, so idk.  The Endorphin Pro 4 is also pretty stable.  

You’ve already got great suggestions for strength work and other shoes.  Keep in mind the strength work you need to do isn’t in brute strength.  You could squat 600lbs and still struggle with this.  You need to strengthen all the little wiggly stabilizer muscles that are responsible for keeping your body in line when you’re on an unpredictable surface.  Those are the muscles that are getting fatigued.  Balance stuff.
[nvc8u25] (score 1, diepte 0) possibly warm up in other shoes and just do session in super shoes.

I would lean to less running in them if unstable, but also be checking out other brands of super shoes if can get some thing that works better for you.
[nvhbaom] (score 1, diepte 0) If you absolutely must run in super shoes; you need to spend time preparing your feet and ankles. Incorporate exercises that focus on ankle mobility, and strengthening the muscles around the ankle and feett to build resilience.

Also don't run solely in carbon plated shoes, alternate with traditional running shoes to avoid overuse injuries.
[nvhcwyx] (score 1, diepte 0) I don’t know why anyone is not asking this. What is your total mileage for your super shoes? I find they only last to 300 kms. Whereas, trainers can get up to 600kms
(6 reacties met lagere score weggelaten)

=== THREAD 1mjhsop ===
SUBREDDIT: r/CampingandHiking
DATUM: 2025-08-06  SCORE: 16  REACTIES: 59
TITEL: I had plantar fasciitis for six years, and nothing helps with treating it
POST (source_id=post):
I can’t enjoy hiking, and it’s frustrating I tried every form of treatment and seeing a ton of doctors to no avail.

I tried the following:

* Calf raises
* Calf stretches
* Hamstring stretches
* Immobilizing my foot in a boot for two months
* Wearing insoles in shoes and buying Brooks shoes
* Heat and ice packs for foot
* rolling foot on golf ball

I just hate it whenever I post anything related to plantar fasciitis online, I get a ton of conflicting advice. I been to PT, several different podiatrists, and orthopedics, and they were all also equally clueless sadly.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[n7b6lh8] (score 11, diepte 0) Not a doctor, just someone who also suffered through this.  The ortho guy I was referred to gave me a steroid treatment as part of PT.  Unfortunately I've quite forgotten what the drug was, but it helped enough to where the stretching combined with switching to Hoka's fixed things for me.  It's rough, I hope you find a solution.
[n7b8to5] (score 7, diepte 0) I know you said you tried everything, but want to throw it out there in case you haven't tried it: Extracorporeal Shockwave Therapy. It's the same thing used to break up kidney stones. I had terrible PF, and that was the only thing that worked for me. Not going to lie, hurts like all get out while getting it done, but after a couple treatments, my PF was gone, and it hasn't come back. I've done it on my hips after surgeries (once my pins were removed), on my TMJ, on my SI joint, my achy knees. It's amazing. At the time when I was getting it, insurance did not cover it, but I happily paid out of pocket. Worth looking into! I am also one who stopped walking around barefoot and wear house Birkenstocks. Brooks made mine worse. Custom orthotics made mine worse. I own a lot of Birkenstocks now 😆
[n7bcij7] (score 6, diepte 0) Have treated 100s of cases of plantar fasciitis successfully with acupuncture and gua sha. Also often includes footwear reccomendati9ns to wide toe box and zero drop with minimal arch support
[n7b94k2] (score 5, diepte 1) Ha! Hokas were the root of my issue.
[n7b9ysc] (score 4, diepte 1) It would have been a cortisone shot.  That does the trick for some people, but for many others it just masks the pain for a few weeks or months until it comes back.
[n7b6mgz] (score 4, diepte 0) I’ve had it three times and it sucks. I swear, the best thing for me in helping it heal and keeping it from returning has been a pair of Birkenstocks which I wear around the house. 

When it was really bad, the Birks plus one of those nobly foot roller things that you’ve probably already tried were the only things that helped me.
[n7bn1ue] (score 4, diepte 0) I ended up ignoring all my doctors advice and just going barefoot as much as possible and never wearing rigid soled shoes. All the custom inserts and special shoes just made it worse. I haven't had any plantar fasciitis pain in almost a decade now.
[n7bafkr] (score 3, diepte 1) Birkenstocks fixed my plantar fasciitis, too. I had it for almost two years and began to think it would never go away. Had a couple of cortisone shots and inserts my podiatrist made but neither helped that much. My wife was the one who pushed me to get a pair of Birkenstocks as I really don't like their looks. I've worn them ever since as basically house slippers. I fucking love how they make my feet feel better after a long day. 

Wanted to add that I have a bone spur on the front of my heel because of the two years of irritation. I can't feel it but it looked creepy in X-rays....
[n7bdpla] (score 3, diepte 1) I got some cheap NOBOs (think marshmallow like slides) from Walmart and they healed mine too. I rarely walk around the house barefoot and haven’t had a flare up in a year. 
I think the house shoes for recovery are the answer for sure.
[n7b8l30] (score 3, diepte 0) I have gotten rid of my PF. What really did it for me and it sounds crazy but I bought some Archies arch support flip flops and I wear them ALL THE TIME in the house. Straight out of bed. I only take them off when showering. I also have custom orthotics that I wear in my tennis shoes for exercise but I had those long before I got the flip flops. Good luck to you.
[n7bl2xe] (score 3, diepte 1) Just had my 3rd session today... It is noticeably getting better... I think a couple of more sessions and it'll be OK.

I'll check out birkenstocks for general use.
[n7bbf2k] (score 3, diepte 0) Acupuncture relieved a lot of inflammation I had with Plantar fasciatis. TMy foot/heel really hurt after treatment for a day, and then next day pain was gone. Now I just focus on prevention
[n7bbo4v] (score 3, diepte 0) Go to a new PT

Try more barefoot walking, barefoot shoes. It’s a workout for your sole and it will hurt (dose accordingly) but you need strong feet. They’re not going to get strong floating around a cushy shoot or mashed into a firm insole or high boot. Furthermore it’s not just soles but toes ankles calves hips like the whole shebang can be thrown off by bad feet. Sorry it sucks. A PT and/or a trainer can get you moving better and give you new things to work on.
[n7bbzzi] (score 2, diepte 2) Lol fair enough, I switched to them for work shoes.  I have heard before that Hoka's made things worse for some folks.
[n7ba3ql] (score 2, diepte 1 OP) I heard steroid treatments can often make it much worse though
[n7bp4ue] (score 2, diepte 4) Go to an orthopedic center and get seen/treated. Don't suffer another six years on the whims of one doctor. If you've done the work on alternate options it's time for a shot.
[n7bod5e] (score 2, diepte 2) Hey, that's awesome 👏🏻🙌🏻! I'm happy to hear that it has been working for you, too. I had never heard of it, but my chiro said I should try it on my scar tissue for my hips, and I was shocked when he said it would help my feet as well. My podiatrist never mentioned it as a modality to try. I hope that a few more sessions gets you fixed up! For the Birks, I know it seems obvious, but make sure you're getting the right width/size. If you're able to find a store near you, they're very helpful!
[n7bb6xa] (score 2, diepte 0) Check out Knees over Toes on YouTube. It will open up a lot of similar videos where you’ll see different exercises that will probably address the real issue.
[n7bbdsw] (score 2, diepte 0) I had it bad from a pair of shoes and overuse (went too far too fast)

I would loosen it by putting my foot against a pool or hot tub jet. 

It took forever to heal but eventually did.
[n7bkldn] (score 2, diepte 1) Came here to say acupuncture. That and doing (hot) yoga helped a lot.
[n7bdqkq] (score 2, diepte 0) My PF was so bad I could barely walk some days. I had it for a decade. I stopped going barefoot at home and wear Birkenstocks in the house. I also got fitted for insoles. Due to a high arch I needed a 10.5 size instead of my normal 11.5. Every insole I had the support in the wrong spot. Those two changes cleared it up in about 3-4 months.
[n7bks2p] (score 2, diepte 1 OP) A steroid injection could cause the fascia to completely tear though
[n7bvbxd] (score 2, diepte 2) I've had four. No issues.
[n7bva7z] (score 2, diepte 1) Ditto.  Took a while for my feet to strengthen up but haven’t had issues in years and hike/run even more now than in the past.  In addition to being barefoot and minimalist shoes, I found balance exercises to strengthen my feet really helped.
[n7bb4w4] (score 1, diepte 2) It wasn't a shot, two weeks of pills to calm the inflammation down
[n7bc0tu] (score 1, diepte 2) A doctor can help you with this.

My experience was steroid pack (week of pills) along with large doses of ibuprofen AND also PT got me over the pain hump so I could work on my problem area. Pain management is for doctors to help you with. Everyone has different circumstances and needs.
[n7bjmhy] (score 1, diepte 3 OP) My doctors oppose me getting steroid or surgery though. They are terrified of those things backfiring
[n7bc25n] (score 1, diepte 2) Op 
I understand 
I’ve been (right foot injury) in a lot of pain for a year. I work a high volume 30k plus steps a night.
My days off are often recovery and I haven’t been on a long trek for the entirety.

I have shoes for my house and I stoped wearing flip flops I’m from Hawaii so this kills me 

Have you heard of OOFOS they’re so ugly but man a god send in the am. I have an inside pair and an outsides

I’ve also had steroid shots that did absolutely nothing. 

I have PF and dumb ass bone spurs from
An injury that I never took care of. 

I feel like I’m rambling. I also have this socks from Feetures and tbh I don’t know if they help or make it worse. 
My suggestion is this.
Take small little treks. 

My doctor has told me I need a different job. I’m having a rough time with my lack of working out or hiking and I just wanted to share that you’re not alone. But please get yourself those dorky slides 
Changed the game.
[n7bqvof] (score 1, diepte 2) I got a couple of shots in each foot four years ago and I've had zero pain since. 

Go to a foot doc. Get treated. You don't have to be in pain.
[n7bu7wo] (score 1, diepte 3 OP) I already saw podiatry numerous times, and they weren’t helpful
[n7bkxie] (score 1, diepte 1) Cortisone if it's the same thing I got. I can't remember if it was one or two rounds, but afterwards the pain was just gone. Over a decade later and it hasn't come back.
[n7b84cr] (score 1, diepte 0) A very long shot but if you are around either Boston or Minneapolis, I have a body worker rec who has been really awesome for my various soft tissue ailments.
[n7b9wb2] (score 1, diepte 0) I don't see cork soled house shoes on your list. That's what saved me.
[n7bcjg0] (score 1, diepte 0) I had the same issue until my podiatrist gave me heel steroid injections and it changed my life.
[n7be74e] (score 1, diepte 0) I had it and HOKAS plus Superfeet cured it. Now I walk around barefoot inside my house no problem. But walking anywhere I wear HOKAS.
[n7beviu] (score 1, diepte 0) PowerStep Original Insoles - Arch... https://www.amazon.com/dp/B005AFHKEO?ref=ppx_pop_mob_ap_share

You’re welcome!
[n7bfnul] (score 1, diepte 0) I have had that bad in both feet at different times, The first time I got  cortisone shot it worked almost immediately and has been a permanent fix, the other foot took a few days but its all better now.
[n7bxv8a] (score 1, diepte 2) Mine ruptured on a hike after a cortisone shot.  It caused a bunch of other problems after.  The risk seems small but it is so not worth it, imho.
[n7bhl69] (score 1, diepte 0) Had no idea what it was so I googled it that suuuucks you gotta deal with that 😵‍💫

My sister apparently has extra bones in her feet that causes her pain, she started wrapping her feet with athletic wrap and it was a huge game changer. I know it's a different ailment but it can't hurt to try? Best of luck op
[n7bhmmy] (score 1, diepte 0) I had this problem too.  Had shots, orthotics 2x.  I finally figured out that shoes with preformed arches hurt my feet now I only wear Chuck Taylor’s or shoes with no support.
[n7biwcs] (score 1, diepte 0) I also haven't found a permanent fix for mine, yet, but taping my foot with kinesio tape [like this](https://www.youtube.com/watch?v=i8W1u4EM63w) helps me when I want to go hiking anyway.
[n7bjk8k] (score 1, diepte 0) I had an incredible PT and chiropractor to treat mine. It took months of PT, proper chiro care, and cupping. 

Look up a video on yt called “The 6 Foot Drills” and do them.
[n7bkg08] (score 1, diepte 0) Have you tied rolling it with a lacrosse ball or other ball?
[n7bki82] (score 1, diepte 0) wearing those ugly Dansko shoes helped me
[n7bmxr9] (score 1, diepte 0) Birkenstocks saved the day for me.  I wear them constantly at home, and make sure my other shoes are really supportive.
[n7bnpmu] (score 1, diepte 0) Buy a Dorsi Flex and go slow.  I’ve fixed me and 3 other people with it.
[n7bp54n] (score 1, diepte 0) I didn't see shin and calf massage in that list. It's sometimes caused by tight lower legs!
[n7bss6p] (score 1, diepte 0) Not sure if this is applicable to you, but I also had crippling PF and it has almost gone now. What did I do? I lost 40lbs
[n7bu5vj] (score 1, diepte 1 OP) I am 6’0” and 150 pounds. I am not overweight
[n7bvgna] (score 1, diepte 2) yeah - that is why I said it might not be applicable
[n7bv2n6] (score 1, diepte 0) Mine was caused by a calf issue and a weak glute. I did some sessions with a kinesiologist who specialized in neurokinetic therapy. It was soooooo  helpful.
[n7bvlvt] (score 1, diepte 0) I work as a nurse and had horrible plantar fasciitis for over a year that made me limp around for my long shifts. Tried different shoes, ice rolling, etc. I found an amazing PT who found knots in various areas in my calf. She would do dry needling 1-2x weekly for maybe 6 weeks. This would release the knot and help with the heel pain. Also found that the muscle that had the most tension was a muscle that runs down the back of your calf to the big toe called the flexor hallucis longus. she taught me stretches such as squatting down and leaning into the toes and using a Thera band to flex the big toe. I now of course have PF in the right foot but left foot has been pain free!
[n7bx7u4] (score 1, diepte 0) Had it for over a year due to a ground fall climbing - go find someone that does acupuncture with e stim on your knee. Yes, Your Knee.

None of that worked for me either. Go get pricked by someone who knows where to stick it :-)
[n7c1lng] (score 1, diepte 0) I've read through all the comments up to this moment. I've tried everything everyone's listed including OP's listed treatments. I have thoughts to share:

PT will take you up the chain of muscles in your legs from bottom to top, strengthening and stretching along the way, over the course of several weeks. If your calves and ankles are strong and flexible, you can jump ahead and work on your outer hips / IT bands. Meanwhile stretch your soleus every few hours and the entire dorsal side of your lower half 3-6 times a day,or whenever it feels like it's tightening up.

Get yourself several pairs of knee-high compression socks. Inflammation/fluid pools in our feet, the compression encourages it to keep flowing back up. This is immensely helpful and so easy!

Get yourself a stability sock like this one: https://a.co/d/7VShSPj (sorry it's apparently out of stock). The key is to have the ability to keep as close to a right angle (or less) as possible. The braces that have a plastic right angle under the foot are a scam. The tension has to come from the anterior / front of your foot. Wear this every night while you relax and to bed if you can.

Ask for dry needling. Brace yourself, this is very painful. But a moment's pain in exchange for an active lifestyle is worth it. I prepare by having a subject to talk about to my therapist, so I can focus on that instead of the pain. Pick something that you can focus on, and be prepared to use it, you will need it.

Oofos slides are best for recovery, move on to Birkenstocks or something harder *after* you have recovered. 

Before you get up from any chair and especially before you get up in the morning, warm up your ankles and calves by rolling your ankles in both directions 20-30 times each way.  Especially in the morning, stretch as well, all the way up the backs of your legs from bottom to top including into your lower back.

Lastly, for all the ladies out there, Plantar Fasciitis is a *classic* symptom of perimenopause. *NO ONE WILL TELL YOU THIS*. If you are nearing or past 40 and you develop PF, know that HRT can be a very helpful part of your treatment protocol. If you aren't treating your hormonal imbalance, you will be fighting an uphill battle for months. (Ask me how I know.)

If I had to pick one thing out of this line up to do- dry needling hands down. Don't sleep on that one, it truly is very effective.

Scams: cupping, candling, custom orthotics 

All the best, OP.
[n7br8x5] (score 0, diepte 1) Came here to say this.  My podiatrist gave me a specific one and a discount code. I have them in all my shoes now. After a year it’s almost completely gone. Mine was so bad that the vibrations of the car just driving on the highway it would be irritated
[n7bp6qx] (score 0, diepte 0) Is surgery an option?

I had PF for over a year. Injections, acupuncture, dry needling, wearing shoes everywhere, not wearing shoes everywhere, PT, nothing helped. This might sound crazy, but I decided to stop all treatment and just accept it. I then ran a marathon. Within a week after the race, my PF was gone and hasn’t come back. My PT speculated that the run severed some nerves that were causing the pain. Since then I’ve read accounts of others having the same experience. 

I wouldn’t take my account as medical advice, but maybe look into surgery.
[n7brk78] (score 0, diepte 0) Switching to barefoot style shoes fixed mine. You’re probably suffering from a wide midfoot like me. 

/r/BarefootRunning can help.
[n7c3gsm] (score 0, diepte 0) I, too, once had plantar fasciitis. Nothing seemed to help until a friend recommended a chiropractor. I usually thought of them as quacks, but I gave it a shot. They took x-rays and found out that one side of my hips were 3 inches higher than the other. I always had issues with my feet, knees, and sciatic nerve, and the doctor said this was what most likely causing it. Twice a week for 3 months, I got adjusted and did stretches daily. This was about 6-7 yrs ago, and I haven't had any issues since.
[n7bge5z] (score -1, diepte 0) Never go anywhere without shoes on. Get the steroid injection in the foot. Not the pills. Get very very firm/hard full arch supports. I had custom carbon fiber ones done at first, then they didn't last very long. I have some Redwing inserts for plantar fasciitis that have been amazing and going on 5 years now. Highly recommend.

