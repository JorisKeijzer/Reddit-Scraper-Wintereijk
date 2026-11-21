# Label-batch batch_0107

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
Schrijf het resultaat naar `batch_0107.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 12epb5m, z6fb5s, e57acb).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 12epb5m ===
SUBREDDIT: r/retailhell
DATUM: 2023-04-07  SCORE: 123  REACTIES: 74
TITEL: The worst part about retail: foot pain
POST (source_id=post):
When I started working in Jobs that required standing, I was shocked that people had to put up with that pain.

I have a nice pair of work shoes that cost 200 dollars (most expensive piece of clothing I own) and yes it helps alot, however it only reduces it.

How do y’all deal with foot pain?

Edit: I have good shoes. SAS shoes which are really popular among workers, and old people, in texas.
200 bucks for work shoes man.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jfcf7du] (score 52, diepte 0) Insoles in the shoes can help tremendously, and if you ever have the spare time and money some massage places offer 30 minute sessions and you can absolutely ask for just 30 mins of foot/leg massage. Also never underestimate a good foot soak in warm water with epsom salts. Peppermint oil is great for foot pain as well, Lush has a crème called Pink Peppermint that saved my feet when I worked at Target. Lots of potential solutions! Source: worked retail for 8 years and am now a massage therapist.
[jfd6byw] (score 46, diepte 0) I don't understand why standing is required by retail employers. It's honestly torture.
[jfd5mh8] (score 19, diepte 2) I like it a lot! Much better than retail, and the pay is great during the busy months. I like the quiet and I like helping people feel better. Anytime I get a client who works retail I’ll ask if they want any extra attention to their feet/legs because oh lord do I remember how sore my feet were after a retail shift lol
[jfckps2] (score 17, diepte 0) I wear doc martens. I used to wear sneakers but that didn't give me any support. Sometimes I use a lavender mint foot cream after showering right before going to bed
[jfcrrep] (score 17, diepte 0) It never really goes away. At its worst, it feels like I'm just jumping up and down on knives. You just muscle through and get your feet up as often as possible. Inserts help, padding, shoes that are a size too big and wide. I have to wear the widest shoes I can find because my feet are wider than they are long. Also cutting off the hard dead skin on the ball of your feet and O'Keefs Healthy Feet help make cracks go away.
[jfclf2i] (score 14, diepte 0) See a podiatrist. You may need to get orthopaedic inserts made for your shoes. Off the rack insoles might help in the interim, but they are no match for ones that are specially made for both your feet and the duty you’re preforming.

I’m waiting on just that. I’m covered by work benefits but it’s still going to be about $100-$200 out of pocket for a whole new footwear setup when all’s said and done.

The way to save a bit is to get footwear that you can resole when they wear down. They’re more expensive upfront, but they also last wayyyy longer so they end up being way cheaper.

I have some proper work boots that I’ve had for almost a decade now that have finally started to wear through and will need to be replaced after 3 new soles.

Paying $60 every couple of years to get them resoled worked out to a total expense of about $380 over 9.75 years. Or I could have shelled out $100-ish every 1.5 years for a total cost of $600, which is almost the difference in cost of a whole new pair of the same high quality work boots.
[jfct7zc] (score 10, diepte 0) I went from retail to a physical 12-hour shift job and honestly wearing Nike’s has made it very bareable. I wear the kind that have no hard plastic the sole of the shoe is like a rubber and the top feels like a net so it almost feels like i’m not wearing shoes. No clue what the name of them are though but I love them
[jfd5p59] (score 9, diepte 0) At this point I don't notice my feet hurting until I go home and take my shoes off/get off my feet. Probably not a good thing lol.
[jfdu7w2] (score 9, diepte 1 OP) You have to move around a lot, like when you’re stocking, and bagging a bunch of items.
[jfd1ix7] (score 8, diepte 1) I really am surprised how comfortable my Dr.Martens have been. Once in awhile I have unusual foot pain but I also have no arches. Forget about wearing anything with a heel for a 8 hr shift. I’m usually limping after 1.5 hrs.
[jfdr5j6] (score 7, diepte 0) When I worked at UPS during peak, boots were a requirement.  I stood on metal grates for hours in the sort aisle.  After that I had to run across the warehouse filled with rows and rows of trucks to deliver what they called “miss loads ” to the drivers before they left.  I was in so much pain.  I bought numerous styles of boot’s including inserts and padded socks, but nothing helped.  In my desperation I started questioning every passerby as to what footwear they had. After nearly $500 spent and many tears.  Timberland… people swore by it.  I bought a pair and discovered why.  I’ve given all those other boots away, but these,  I can’t part with.
[jfcyo58] (score 6, diepte 1) How do you like being a massage therapist?
[jfd4gai] (score 5, diepte 2) Proper boots like Doc Martens will mould to your feet over time. If you need trainers find a running store that does gait analysis - they'll normally do it for free and guide you to the right structured models.
[jfdaj80] (score 5, diepte 0) Definitely invest in better shoes and insoles. I've had the same style of New Balance for 15+ years. Boring, expensive, but comfortable (hubbycalls them my "nun" shoes!). I get a new pair about once a year, the same kind. (They just reorder when I call). I'm salaried, often 15 hr days, 6 days. Lots of miles. But my feet seldom hurt. Because I have a bunion, the shoe store will stretch that area before I start wearing them.
[jfddpz0] (score 5, diepte 1) All the yes. I wear Merrell’s. Expensive, but worth every penny.
[jfdxo4a] (score 5, diepte 0) I worked retail for 20 years in a large store, so I walked a lot. I wore dress shoes every day and as long I did not wear the same shoes two days in a row, my feet were fine for most of the day. I also purchased an at home foot spa and used that often. I used and still use a pumice stone on my feet every day in the shower.
[jfdfprr] (score 4, diepte 1) This. In my later years I ended up getting a neuroma because I wore shitty shoes in retail. They don't go away.
[jfejynt] (score 4, diepte 1) Same here. My feet don't really hurt much throughout my shift, but once I get home and sit down for a bit, they hurt so, so much, often into the next day. It's probably about time to replace my shoes. The foot pain usually lets up for a while when I get new shoes, but as they wear out, the pain increases.
[jfdz80c] (score 4, diepte 0) I honestly think my feet are so fucked up from 16.5 years in retail that they barely hurt anymore 

it's my back and knees that are killing me
[jfd3yz6] (score 3, diepte 0) Personally I discovered that I had been wearing shoes about one and a half size too small after working retail and standing in my feet all day. Also, Dr. Scholl's.
[jfde390] (score 3, diepte 0) I learned one thing is standing in one place despite having a standing pad on the floor doesn't do much to help with fatigue. You got to keep moving in some way or fashion. Stretch your body and stretch the feet. Tiger balm, OTC Pain relief and a massaging heat pad go a long way for me. The occasional foot spa with epsom salt helps a lot as well. Prop and raise those feet above your heart to get the blood pumping to those areas. Foot massages helped me a lot aswell. I bought some OTC Orthotics and started to exercise a bit more. Overall, goes a long way.
[jfdlozh] (score 3, diepte 0) Depends on what your problem is! I wasted so much time and money! Come to find out that it's the memory foam shoes that caused my issues in the first place. I do best with shoes that have no support. I was super naughty for a week and wore water shoes to work. I was at my wit's end. I tried so many gimmicks! Before I figured it out.
[jfdoi1i] (score 3, diepte 0) Compression socks, great shoes, insoles, tens unit at night, and foot baths.
[jfdy3zm] (score 3, diepte 0) I mostly wear Hoka and Brooks sneakers. They’re both expensive, but well worth the money. You can also buy less expensive sneakers that have removable insoles and then get a good set of arch supports from Amazon. Not the cheap floppy ones you get at the drugstore, the good ones are not very flexible and run about $30.
[jfepmtp] (score 3, diepte 1) I worked in a curvy lady’s store for 9 years where you had to wear stylish shoes——Crocs and Earthies saved my feet! Back in the day Crocs had some cute wedges and strappy “heels” that would pass the dress requirement.
[jfeaffn] (score 3, diepte 0) I keep walking, I don't stop 😂🤣 just keep moving so you don't feel the pain 😂
[jfed9gu] (score 3, diepte 0) I've been doing this for over 2 decades. Start by embracing the pain.... 😉. I use some inexpensive orthotic insoles and usually stick with work shoe brands/lines that focus on retail/food service/hospitality. Clarks, Skechers, Nunn Bush all make comfortable shoes appropriate for even dress situations. But first, confirm your shoe size. I didn't realize it, but I was getting the wrong size for a long time. 

Also, try not to stand. Stay moving if you can. Much of your pain comes from trying to relax while on your feet. You might lean or rest on something in an unnatural way putting even more stress on one joint just to relieve another. Your body was made for motion so embrace it. If you have an area of responsibility.....walk it. Constantly. I put in about 5-7 (10 on Black Fridays)  miles during an 8 hour shift. 

You should stretch, do some yoga, soak your feet in Epsom salt, give yourself a massage. But at the end of the day, embrace it. You will get used to it. 😕
[jfeee2g] (score 3, diepte 0) I work in a large home improvement store and make frequent trips from one end to the other. My feet are usually killing me by the time I go home. 

For me, massaging my feet and stretching really helps. When I get enough money saved up, I plan on getting better shoes. Currently I’ve been wearing Skechers with memory foam and they are no longer effective. Haven’t even had them a whole year.
[jfcu6sd] (score 2, diepte 0) I highly, highly recommend Dr. Scholls gel inserts for Work. They have saved my feet a lot of pain, and on a day when I'm walking around a lot, they hardly ever hurt at the end of the day!
[jfcwuaa] (score 2, diepte 0) The human body can get used to even the most insane things, my feet just stopped hurting. My pacer phone app. usually records around 20k-30k-40k steps a day.
[jfd5zfx] (score 2, diepte 0) Yeah Insoles, really good chance your arches have fallen. Happened to me. Insoles for proper arch support keep your foot muscles from being over extended.
[jfef7x6] (score 2, diepte 1) I have a pair of new balance that I have killed over time. 
Most boring wonderful shoe ever.
[jfdymtd] (score 2, diepte 0) I have found danskos and dr Martens to be my favorite work shoes. I am on my feet all day and moving, recently got some new balance and they are ok.y feet don’t hurt but they aren’t as comfortable as my old danskos (my dog ate them and I almost cried) and got some crocs -and they are my least fave
[jfhtey3] (score 2, diepte 1) Mine are just numb. Painfully so if that makes sense.
[jfe6xxu] (score 2, diepte 0) I used to have foot pain until I tried Crocs! Not much pain now.
[jfeywrd] (score 2, diepte 0) I got used to it. Been at a retail job for 9 years now and it's just a constant.
[jfgguzp] (score 2, diepte 0) I take a ton of advil and get shoe inserts lol
[jfx2962] (score 2, diepte 0) Time. I was very sore in the first couple weeks of my retail job but beyond that, as long as you work pretty consistently, the pain definitely eases a lot.
[jj0tl6l] (score 2, diepte 0) I use the circulation slippers after work and my feet feel so much better. It’s a device that stimulates the muscles to increase the blood circulation in the feet and legs. I got it from tens-relief. Shop you can google it…
[jfcpxoq] (score 1, diepte 0) Insoles and I rotate the shoes I wear. I’ve got Doc Martens, Keds, and Crocs.
[jffvd45] (score 1, diepte 1) I am having a hard time finding shows that are not hard plastic. In fact I have only managed to find one pair
[jfd0ed0] (score 1, diepte 0) Insoles are useful, orthopedic shoes are useful, but I've been getting bad knee and hip pain. They have compression straps for knees that I wear at work but they don't sell anything for bad hips.
[jfd1tsd] (score 1, diepte 0) Foot exercises!
I spend my couch time stretching my feet and wiggling my toes and I have massage balls and and an Achilles tendon rocker.
[jfd9pwq] (score 1, diepte 0) I literally wear clearance Walmart shoes with $3 insoles, but the insoles help a lot and espom salt baths are absolutely needed and they especially help me. I probably take 2-3 baths or soaking my feet with Epsom salt and the matching bubble bath soap, and it just helps to relax
[jfde779] (score 1, diepte 0) I work 11 hour shifts where I have to stand for 10 of those hours, my converse are my best friend.
[jfdkxsq] (score 1, diepte 0) Try a supplement called Acidophilus Acid it really helps the foot pain.  I’ve bought it at Walmart.  I usually get the Natures Made brand.  It’s less than $8.00.
[jfdnpnn] (score 1, diepte 0) The only shoes I’ve found that don’t leave me with crippling foot pain are Skechers. It can be a bit tricky to find nice, work appropriate ones but worth it when you do. I’d love it if they did cuter styles that were more my taste - but they are worth wearing for the difference it makes to my feet 👣
[jfdpfx5] (score 1, diepte 0) The expensive shoes
[jfdtitn] (score 1, diepte 0) You’ll get used to it and if you’re smart you’ll get out while you can.
[jfe5ttv] (score 1, diepte 0) Brooks with 2 pairs of inserts. Honestly Brooks has helped me so much. I've noticed a lot of people have wider toe boxes and still squeeze into regular or regular wides to without realizing they need a wider width, which is what I used to to do. But a lot of brands don't offer extra wide(let alone wide). So we squish our feet in thinking we can just break them in.
[jfe78tw] (score 1, diepte 0) I work for a shoe brand whose shoes i hate 😓 but im not allowed to wear my more comfortable sneakers since dress code is I have to wear the brand from head to toe. I get how you feel
[jfefa7o] (score 1, diepte 0) I swear by Skechers tbh. My feed might be a little sore but nowhere near the pain in other shoes
[jfej3m3] (score 1, diepte 0) As a 21 year old retail worker with horrible plantar fasciitis, this thread was one that I desperately needed to see.
[jfej7wc] (score 1, diepte 0) Rocker bottom shoes
[jfeka8n] (score 1, diepte 0) Good insoles and invest in a foot bath. Hot water, epsom salt, and some nice aloe socks after rubbing on tiger balm at the end of a long work day is absolute heaven.  

Sleep with your feet elevated and invest in some good compression socks to reduce swelling which will help reduce the pain as well.
[jfem6bh] (score 1, diepte 0) The last time I had foot pain it started right around 3 quarters of the way into my shift. It hurt so bad that I could barely walk or put wait on my foot.
[jfeqh3y] (score 1, diepte 0) I tried all types of shoes. Came across Hokas. It was a game changer.
[jfervbw] (score 1, diepte 0) I had an outdoor job for 3 years and wore boots because tennis shoes would just get murdered by everything wet. I had genuine timberlands and then these merrell boots with vibram soles. So comfortable! Worn down to nothing. 

Back to retail and back to new balance tennis shoes. I’ve had bunionectomies on both feet (and the second one was after a year in retail with 8 weeks off for recovery - no, retail did not cause them nor did my shoes) and need wide shoes for standing all day. But even mobile shifts demand more than the outdoors work, that concrete is hard!
[jfgab1v] (score 1, diepte 1 OP) It doesn’t hurt as much as it did when I started
[jffad80] (score 1, diepte 0) If you can find them they have a dr.scholls machine tgat will give you a decent mapped insole that helped me alot
[jffc4il] (score 1, diepte 0) Working 14 years now on my feet and the only time I've got foot pain is if I've worn bad shoes. The last few years I've been wearing hiking/walking shoes to work, the type you get at outdoor/camping/hiking stores and it works perfectly for me.
[jffjp7l] (score 1, diepte 0) Sounds like bad shoes.  Never had an issue walking before lol
[jffkrsv] (score 1, diepte 0) I have plantar fasciitis. $600 custom built orthotics. $300 shoes from that good shoe store in town. I'm fine at work, but once I get home I'm hobbling around like a geriatric wino.

Why the ever loving fuck can't we have chairs?
[jfflkrs] (score 1, diepte 0) I've worked retail for 18 years and don't have feet pain thankfully. For me its a fucked up back and shoulder.
[jffmx5i] (score 1, diepte 0) I’ve been using a massage ball that helps relieve the pain in my arches temporarily. I just roll my arch over it for awhile and use my body weight to control the pressure. It hurts to use, but it’s that good type of pain, and afterwards the tension in my arches subsides. If you haven’t already tried using one I’d recommend it as a temporary solution.
[jfg9d2l] (score 1, diepte 0) I recommend rolling a tennis ball under your feet and sitting with them a little raised - helps for me, hope it does for you <3
[jfgc8kp] (score 1, diepte 0) Take a sitting break helps a lot. Depending on where you work a lot of places have to allow a 10 min break every 4-5 hours. They just don’t tell employees cause that effects productivity. See if your job has a similar policy
[jfgf6u1] (score 1, diepte 0) I have the worst feet... don't spend $200.  Buy Skechers and replace them every 3 months.

I'm on my feet 10 hours a day.  Yes it sucks having to replace shoes that still "look" new, but the support in them are completely gone no matter how much I spent on them after about 3 months.  If I try to wear them longer, I suffer.

Since skechers run $40 to $50 per pair, you're still paying $200 for the year anyway, but you got fresh shoes every 3 months.  It does make a difference.

The "arch fit" are really good if you need the extra arch support.  If you don't, you can spend less on the "go walk" styles.

Whatever you decide to spend, or whatever brand you decide to get, they are going to wear out fast if you're on your feet all day.

The bonus with skechers is there's no break in time.  Day one out of the box I felt better, and I no longer have crazy foot pain.  I still get foot fatigue on the rough days, but I'm able to walk when I get home (if you know, you know).  I consider this a win.
[jfgzdcu] (score 1, diepte 0) It's possible some of you might have bilateral plantar's Fibromatosis. I dealt with severe foot pain for years  before my diagnosis and often wondered why my feet hurt so bad by the end of a shift but my coworkers seemed fine. Unfortunately getting a diagnosis doesn't really change anything because there are no injections or surgeries for that. In the mornings I could barely stand on my feet because of the pain and stiffness so I learned to do some preventative care - I take a tramadol and flexeril before bed and that helps a lot. Weirdly I've developed another symptom over the past year. The bottom of my feet are swollen when I wake up and it feels like I'm walking on bubble wrap if I'm in my bare feet.
(4 reacties met lagere score weggelaten)

=== THREAD z6fb5s ===
SUBREDDIT: r/Construction
DATUM: 2022-11-27  SCORE: 11  REACTIES: 73
TITEL: Back of feet rubbing on boot pretty bad, not able to get new ones just yet, any redneck engineering solutions? Bandaids didn't work out well.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iy11d6t] (score 66, diepte 0) Mole skin
[iy17vp0] (score 33, diepte 0) Ok so this is a legit thing. You're broke can't afford $200 boots.  Buy athletic tape. The stuff for hockey sticks. Tape up your foot where it's wearing on ya. Put on your socks. Give it a go.
[iy18903] (score 19, diepte 1) Man where the fuck is he supposed to find a mole to skin in this economy?
[iy1a8lr] (score 13, diepte 1 OP) Got some in the pantry, didn't even think of it. Thank you so much.
[iy1ao07] (score 12, diepte 2) Economy has nothing to do with it. Better get his ass out into the woods and start looking for mole hills.
[iy1etwo] (score 11, diepte 2) This is 100% the answer, I work in the oilfield and keep a cpl extra rolls of pre wrap and athletic tape to give any poor bastard that’s brand new and wearing new boots. The pre wrap goes fast so get some extra of it. Put that on before the tape and it’s a game changer. Good luck buddy!
[iy1iwf3] (score 9, diepte 3 OP) Thank you, and good of you to help out people in this situation.
[iy12vrn] (score 8, diepte 1) 2nd this
[iy155xx] (score 8, diepte 0) Mole skin.
[iy1g5ug] (score 8, diepte 0) Double socks could also help.  Like, thin “dress” socks or else fancy polypropylene hiking socks under thicker potentially wool-blend socks.
[iy3cc9k] (score 6, diepte 2) If you have dress socks or a thin, tight sock... wear it under your regular socks.
[iy1agat] (score 6, diepte 1 OP) Yeah I'm getting new ones ASAP, these were a gift which I'm really appreciative of, been trying to make them work. Luckily my company reimburses us $200 for boots so I'm gonna get some soon.
[iy1encd] (score 4, diepte 1) This is the way
[iy257gu] (score 4, diepte 3) He ain’t gotta go all the way out there. He can just come to my backyard.
[iy26a1q] (score 4, diepte 3 OP) Is this a valid excuse to be late for work? Cause I'll totally tell my foreman I'm running late looking for fuckin moles and shit.
[iy1a61d] (score 4, diepte 1 OP) It's not money but I'll get right on that.
[iy1fbtp] (score 4, diepte 0) Vaseline on the hotspot; Duct tape over the vaseline.
[iy2639y] (score 3, diepte 1 OP) Will definitely buy this for the future.
[iy15j8i] (score 3, diepte 0) I bought a pair of helly hansens that did that and I returned them, it was the third time I bought those shoes and the previous pairs didn’t do that, hey new ones even if you have to settle for used ones. A guy has to be comfortable or that will ruin and drag your days out
[iy16egf] (score 3, diepte 1) This is what we always used back in the day
[iy2mz4u] (score 3, diepte 4) Kt tape is another great solution, it's a bit smoother, no need for pre wrap ( unless you prefer it) and sticks better in my opinion. Plus you can stretch that shit for days.
[iy1grpr] (score 3, diepte 0) Knee-high nylons or other thin silky socks under your work boot socks will help reduce the friction and blisters. Used to do that when I was in the Army and had new boots.

Also second the suggestions of athletic tape or mole skin
[iy1hkle] (score 3, diepte 1 OP) Thank you. Maybe I'll do that and then I won't have to wear pants tomorrow as a bonus!

But I'm definitely gonna double sock and use bandage tape.
[iy5pmyt] (score 3, diepte 2) On the socks. They make 'sock liners' usually silk or synthetic. You can find them through outdoor stores and I'm sure Amazon and such. I wear them in the summer both on jobs and when backpacking.  They not only reduce friction, but help wick sweat so your skin doesn't get all wrinkled and tear easier. 

For the over sock, if you don't have them get wool socks, or mostly wool socks. Cotton socks are absolute fucking garbage.  My preferred brand is Darn Tough, but there are plenty of other brands that are similar.  Yes they are expensive. Darn Tough has a lifetime guarantee though as do some of the others. There are also cheaper wool socks.  Still like $8 a pair probably at the cheapest, but so, so much better. 

Other than that, what everyone else said. Moleskin, friction tape, the band aids that are designed for blisters, etc.
[iy1ikbi] (score 3, diepte 0) Plastic water bottle, cut out the bottom and a heel shape and tape to your sock with your foot in it and them slip on your boots, been there! easiest fix and saves you.
[iy1l228] (score 3, diepte 0) Those gel sleeves that figure skaters wear are the answer.
[iy1m9ia] (score 3, diepte 2) Crs cross ankle gel sleeves.  I looked to see what they're  called.
[iy124ed] (score 2, diepte 0) Triple socks
[iy12psf] (score 2, diepte 0) You’re just going to have to tough it out for a while. Bring a change of socks to work and let the blisters dry on lunch and change socks. Get some burn cream with analgesic for the pain. Good luck
[iy2zzpi] (score 2, diepte 4) You're making your own conditions.
[iy15t3p] (score 2, diepte 0) Make mole skin your friend
[iy1686t] (score 2, diepte 0) Duct tape
[iy1bf3z] (score 2, diepte 0) Put Vaseline on your foot where it rubs. No more friction, so no more blister forming.
[iy34dc7] (score 2, diepte 2) You're welcome bud! I know its tough out here, hopefully they throw you a lip Christmas bonus!
[iy1ls5g] (score 2, diepte 1 OP) I'm gonna have to look into that just out of curiosity.
[iy27l7t] (score 2, diepte 0) Neoprene beer coozie. Cut it down 1 side and it fits perfectly on the foot. Put your sock over it and done!
[iy3ambi] (score 2, diepte 0) Moleskin
Just curious about why this is happening. Are they new boots or just what you had to start with?
[iy586rv] (score 2, diepte 2) Well they gotta get broke in and there’s only one way to do that. There are lots of good tips here.
[j2816qp] (score 1, diepte 4) Fuck man, changing mole skins daily... Your yard has to be pretty fucked.
[iy15fr6] (score 1, diepte 0) Double socks, or triple… varying thickness
[iy15k61] (score 1, diepte 0) Piece of leather, glue
[iy3mcp2] (score 1, diepte 4) Pre-wrap under the athletic tape too 👌🏽
[iy180ew] (score 1, diepte 0) Double sox
[iy1ci7x] (score 1, diepte 0) 2nd skin and wrap with athletic tape.
[iy1griw] (score 1, diepte 0) Silicon heel protectors… they work well for other shoes, so maybe??
[iy5trqo] (score 1, diepte 3 OP) Thank you. 😎
[iy1jgll] (score 1, diepte 1 OP) I never would have thought of that. I'm gonna try it just to see, I've got some gauze and tape that I'm gonna use but I'm definitely gonna try that, thank you.
[iy1v11n] (score 1, diepte 0) Thick socks and tighten them boots
[iy1yczp] (score 1, diepte 0) Two pair of socks
[iy215qk] (score 1, diepte 0) Double up on the socks
[iy23cxr] (score 1, diepte 0) Leukotape
[iy24w6h] (score 1, diepte 0) Double socks
[iy26mdz] (score 1, diepte 0) Two pair of socks.
[iy26u64] (score 1, diepte 0) Short term: hockey tape. Long term: heel wrap
[iy27wq1] (score 1, diepte 0) If you're on a budget 
Turn your socks inside out before putting them on 
(Fuzzy side out)
[iy29trz] (score 1, diepte 0) luekotape is what you need. It is far superior to moleskin or athletic tape. I have hiked hundreds of miles with heavy pack as a back country guide and this is the only stuff that will stay attached to where ever you put it.
Most pharmacies or a physiotherapist office will have it as well as stocked online.

https://www.amazon.com/BSN-Medical-BEI076168-Leukotape-Sports/dp/B07KB5KSB2
[iy2ffy1] (score 1, diepte 0) Whenever I get a blister or anything from my boots I just throw some duct tape on it
[iy2lyau] (score 1, diepte 0) What size feet you gonna get?
[iy2qc38] (score 1, diepte 0) People already said it but I'm gonna say it again. KT tape (kinesiology tape). It's stretchy and really sticky. I get the off brand stuff and it works fine
[iy30ly2] (score 1, diepte 0) There’s blister pads - like band aids but it’s a thick pad of gel. Two pairs of socks helps with the friction to sometimes
[iy33r1c] (score 1, diepte 0) folded napkins give enough space between the boot and you for the skin to heal and the heel to break in
[iy3g95n] (score 1, diepte 1 OP) New boots, a gift.
[iy3fwdc] (score 1, diepte 0) in the military we used mole skin
[iy3kt47] (score 1, diepte 0) Double ur socks up.
[iy3mnhz] (score 1, diepte 0) Reddit let’s get OP some new boots. Let’s make this happen. Who’s in?
[iy3oxnj] (score 1, diepte 0) Heel cups. They are for women but they could work
[iy3pjj1] (score 1, diepte 0) I like luko tape. It's the middle ground for athletic tape and mole skin. Works better then both of these for hot spots. A roll of it should be relatively cheap. Athletic stores maybe even Walgreens and the like might have it.
[iy40xcm] (score 1, diepte 0) Try removing the insoles btw. Some are springy and make the foot move up and down. Also increased depth may position your foot better.
[iy474a2] (score 1, diepte 0) These bandaids [https://www.band-aid.com/products/blisters-footcare/hydro-seal-blister-cushion-bandages-heels](https://www.band-aid.com/products/blisters-footcare/hydro-seal-blister-cushion-bandages-heels)

and athletic tape over it and all around your heel and ankle to keep it in place all day.
[iy4bzee] (score 1, diepte 0) Cotton pads worked for me did it too late tho got a scar from it
[iy4emu2] (score 1, diepte 0) If their tyevups use a heel slip knot verry efficient
[iy5ioto] (score 1, diepte 0) Mole skin is made for this. Dr Scholls. Walgreens etc
[iy17zfm] (score -5, diepte 0) Second option. Stop being poor you pleb

=== THREAD e57acb ===
SUBREDDIT: r/solotravel
DATUM: 2019-12-02  SCORE: 26  REACTIES: 73
TITEL: Does hiking shoes really help city walk fatigue?
POST (source_id=post):
I'm about 20 lbs over the "ideal weight" for my height.  Sometimes when touring a city, after walking a whole day (20k-30k steps according to my phone), the bottom of my feet area bruised, causing me to limp the next day.  This is especially true if I carry a 15 lb back pack.  Different shoes bruise my feet in different spots.  So far, my solution is a cushioned pair of sneakers, and use Dr Scroll's insoles for extra padding.  If If my feet get bruised too much, I'd take the insoles out so the next day I'd bruise a different spot instead.

I heard somewhere that a good pair of hiking shoes would help.  Is this true?  Do hiking shoes have extra cushioning that sneakers don't, so it it would bruise my feet less?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[f9ihwzn] (score 48, diepte 0) Listen to your body.

Never walk until your feet ar bruised. You could be damaging your joints. Hop on a bike or a bus. 

You need shoes with good arch support and you may need orthotics. They're expensive, but so is hurting your feet in the long run.
[f9i5p6y] (score 13, diepte 0) hiking shoes help, but we all have different needs.  I find that my ankles are annoyingly small compared to my shoe size, I often find it hard to get things to lace right because of that and my shoes move around and I get lots of blisters.  for me its a polar opposite thing, i either want a good hiking sandal that I can more or less trap to my foot and know its not going anywhere, or I want a full blown hiking boot that I just feel fit me so much better in terms of being able to lace them right so they don't rub against my skin all day.  As far as inserts go for general every day shoes, I have never had a lot of success with the store bought ones, they just don't do the job, it costs money, but going to a running store and having custom made inserts done I think is the way to go if your going to be walking that much, its worth the investment
[f9ijmul] (score 12, diepte 2) Get Darn Tough socks. I just picked up a couple of pairs and they are the most comfortable socks I've ever worn. They're merino wool as well so they reduce odor and are quite breathable, and Darn Tough socks are exactly that - darn tough. They even provide a lifetime guarantee.

The light cushion seems to get the best reviews from hikers and onebag travellers.
[f9ixs8i] (score 12, diepte 0) (U.S.A. here) 
I went to a speciality shoe store where they provided medical grade orthotics, prosthetic assistance etc. it was a free appointment & after my evaluation I was fit for a pair of high arch shoe unsolved w/ a 1 mm lifter as my hips are unbalanced - best $65 I ever spent. I had them placed in a pair of inexpensive walking shoes. I move them to different shoes for work, travel shoes, gym etc. 

Game changer!

My lower back doesn’t hurt as much. I can walk for much longer without pain in my knees & feet. 

Invest in yourself now or pay for it twice over in the future.
[f9ierrd] (score 11, diepte 0) And wear some good 100% woolen socks with it. For me the difference is more in the socks than the shoes
[f9iiems] (score 5, diepte 0) How old are your shoes? Even good hiking shoes have a life of 400-600 miles. The footbed wears out. 

Also, how do you walk? Are you rolling your feet or stomping on the heel or ball of your foot? I suspect your stride isn't helping you.
[f9iukkh] (score 5, diepte 2) I didn’t think I walked much but after having been counting my steps recently I clear an easy 50km a week this equates to 1600 miles a year, therefore a 4 Month old boot is at or near the end of its life
[f9im3um] (score 5, diepte 0) You want a high quality walking shoe and yes they'll definitely make a difference. I just got my first pair of Hoka's after trying several other brands and honestly they're a big improvement over anything I've tried. Brooks and Saucony also make great shoes so those are good options as well but for me Hoka have been the best. If you can go to a proper shoe store where they'll watch how you walk and measure your feet and they'll recommend something for you that would be best.
[f9iannr] (score 4, diepte 0) Try Hoka Clifton’s , these shoes are great road shoes that have saved my feet! Hiking shoes vary just like road shoes in support you’re just going to find a more intense tread. There are good options out there tho!
[f9igfw1] (score 4, diepte 0) Try to get some custom fit orthotics, it really made long walks way more comfortable on my feet.
[f9jebxm] (score 4, diepte 1) I deffinitely agree with this. I got plantar fasciitis from ignoring the pain in my feet. I found orthapedic insoles to help a lot.
[f9ikmcf] (score 4, diepte 0) Your feet are just weak.  Get a bread roller and stand on it, rolling the undersides of your feet.  It'll hurt, but it's just mashing up all those stiff little muscles, loosening them.  

I now like pretty minimal walking shoes, like Sanuk's or Van's.  I need my toes to be free to splay out as I walk.
[f9ifs3f] (score 3, diepte 2 OP) I'll remember that.  There're lots of different models, is there one you recommend?  For example:

* What's the diff between Hoka Clifton 4, 5, or 6?
* What's the diff between Hoka Cliftons vs Hoka One Ones?
[f9ifvc4] (score 3, diepte 1 OP) Thank you.  A diff thread recommended "hiking socks", which mostly look like wool socks but $18 a pair.  I think I'll give it a shot.  Thanks again for this.
[f9igp79] (score 3, diepte 2) If you’re not actually walking on trails, try lightweight hiking socks (still wool, but they won’t be so thick that you need to wear one size up in shoes).
[f9ipyrb] (score 3, diepte 3) My husband bought these. They are warm but slide down the calves after a while:(
[f9iks3l] (score 3, diepte 1 OP) Yeah, I do have weak feet - I work in an office and live in suburbs, where I dive everywhere.
[f9izzcu] (score 3, diepte 2) I know you meant "drive", but I'm imagining somebody diving to the ground and rolling a few yards/meters across lawns and down the sidewalk before standing up and doing it again to get around town, instead of just walking.
[f9im0p0] (score 3, diepte 0) Try getting yourself a pair of soleless shoes (I.e Vibrams) and strengthen your feet. Getting padded shoes is likely only going to exacerbate foot issues by avoiding the underlying problem. 

I got Vibrams after gaining 20lb on the couch from a fractured ankle. Both physio and the doctor supported that idea, and I had noticeable improvements in my balance and foot strength.
[f9jb1x9] (score 3, diepte 1 OP) That's great advice.  If $65 can resolve this problem for me, I'd jump on it in a heartbeat.  Do you know the name of the specialty shoe store you went to?  Maybe it's a chain and I'll have similar luck in California.
[f9i6cz3] (score 2, diepte 1 OP) Thank you, I really appreciate this.
[f9ib3cm] (score 2, diepte 1 OP) Is there a specific model you like?  They range anywhere from $100 to $200 on Amazon.  Also, should I get it one size bigger, so I have the option to put in some Dr Scroll's insoles without it squeezing my feet?  Does it matter when I'm using it, that it's slightly too big?  Or is "the right fit" pretty important in walking shoes?
[f9igzdw] (score 2, diepte 2) I would definitely recommend trying a pair on! These are the shoes Dr’s recommend to physical therapy patients because of how much support they have. The Clifton 6 is what I have but most of them are pretty similar. They also come in wide, I have a generally slim/long foot, but I found that I had the perfect fit in a wide. I would say fit is probably the most important! I used to lose toenails doing long backpacking trips and it wasn’t for years that I realized my boots were entirely too small when I went downhill!! Show places near you should be able to fit you pretty accurately even if they don’t carry that brand
[f9ii3c4] (score 2, diepte 3 OP) This is super helpful, thank you.
[f9idoew] (score 2, diepte 1) My mother swears by hokas. I’m partial to oboz for long walking shifts. We both have bodies that demand good shoes on concrete. To each their own ;)
We both wear them without any additional inserts (but I did get help sizing mine from REI). They’ve done wonders for our feet and back/hip/foot alignment in different ways. I love mine so much I wore them bar hopping through the city once. Everyone laughed until I was the only one left still walking strong.
[f9ii098] (score 2, diepte 3 OP) Thank you for the tip.
[f9ijp4y] (score 2, diepte 3 OP) Thank you.
[f9imnh2] (score 2, diepte 3) +1 for darn tough, pretty much the only socks I wear now. $20/pair is tough to swallow but they are the best damn socks I've worn. Warm yet breathable and can wear for a few days without any stink.
[f9jl545] (score 2, diepte 5) Haha sorry I should’ve been more clear. I don’t often wear them back to back. But if you have a few pairs you can rotate through while traveling and wear more than once without a wash.
[f9ioey4] (score 2, diepte 2) Do you have access to a Costco?

4-pair for $18.99

 [https://www.costco.ca/kirkland-signature-men%e2%80%99s-trail-sock%2c-4-pair.product.100464537.html](https://www.costco.ca/kirkland-signature-men%e2%80%99s-trail-sock%2c-4-pair.product.100464537.html)
[f9jbc7l] (score 2, diepte 3 OP) I don't have a Costco membership, but I recently bought these socks, they're nice and warm, but it doesn't mention cushion.   [https://www.amazon.com/gp/product/B071H6KZ27](https://www.amazon.com/gp/product/B071H6KZ27) 

Also, are these socks similar?  They both advertise as "trail socks", with the second one mentioning "cushion".

 [https://www.amazon.com/Pembrook-Wool-Trail-Socks-hunting/dp/B06ZY6NT3J/](https://www.amazon.com/Pembrook-Wool-Trail-Socks-hunting/dp/B06ZY6NT3J/) 

 [https://www.amazon.com/Enerwear-Merino-Blended-Blister-Trail/dp/B07K9T52LX/](https://www.amazon.com/Enerwear-Merino-Blended-Blister-Trail/dp/B07K9T52LX/) 

&#x200B;

Thanks again for the help.
[f9ihycx] (score 2, diepte 1 OP) Thank you.
[f9ii5kl] (score 2, diepte 1 OP) This is helpful.  Thank you.
[f9iit4q] (score 2, diepte 1 OP) I don't think I walk enough to be close to those miles numbers.  I have no idea how I walk, I think I'm rolling on the bottom of my feet, but not super sure.
[f9jcpwx] (score 2, diepte 3) This is illumination... I also walk a ton and it’s hard to believe that my shoes aren’t suppose to stay with me that long. It’s no wonder a new pair of shoes feel so good when I first wear them!
[f9ijpjl] (score 2, diepte 0) I usually pay around 50 euro for a pair of hiking shoes, wear them every day just in regular life. I had a few bad ones recently that just didn't break in, then bought a pair for 90 that were super comfy straight off. I've never had a better pair of shoes before! Well worth it! (I also hate shoe shopping so ones that last longer for me are worth the price.) My friend got a pair of insoles a sport shop too, which he swears by. He just has some good runners, but you can buy insoles that you cut to size which he says are great if you suffer with fallen arches. Ask a shoe shop person though cause as some others have said it depends on your own foot needs.
[f9ijxqk] (score 2, diepte 1 OP) Thank you.  I just read that walking shoes are different from running shoes.  Your 90 euro shoes, are they walking or running shoes?

Also, the self cutting insoles, is it pretty similar to the Dr Scholls gel insoles?
[f9qf26k] (score 2, diepte 2) I'm not sure about the insoles... My mate got them in a sports shop but that's all I know. They were about 30 euro. 

Mine are walking shoes/hiking shoes. Not boots as Ive gotten before. The last ones I got were boots but theyre not needed for just walking around cities, really just if you're hiking and want extra ankle support.
[f9iyv3g] (score 2, diepte 2) Try getting Yamuna Balls to stretch and strengthen your feet. You just stand on them, but it helped me to change my walking gait and be be able to walk correctly for the first time in my 44 years. You can also take them on a trip to help relax your foot muscles after a long day.

I wore orthodics  for years, got a bad stress fracture from them, and was in physical therapy for years. Finally found a naturopath that recommended the yamuna balls and they have literally changed my life.
[f9iqdwo] (score 2, diepte 1) That is what my osteopath recommended too. Orthotics will do more harm in a long run because the foot muscles become weak overtime.
[f9jbxut] (score 2, diepte 1 OP) Thanks for the tip, really appreciate the help.
[f9jbdu1] (score 2, diepte 1 OP) Thank you for this, I really appreciate the help.  Hoka's seem to be the universal answer, you guys have convinced me.
[f9ina0d] (score 2, diepte 0) I’d recommend a pair of boots with good ankle support. If you’re not in too hot a climate I’d try a pair of Karrimor leather uppers with Vibram soles, I find them fairly good on hard ground and reasonably affordable. Different things work for different people, it might pay to be more conscious of your gate if you’re not used to being on your feet all day.
[f9io79j] (score 2, diepte 0) I live in hiking/walking shoes.  If you are doing city walking you shouldn't need full on hiking boots with full ankle support.

If you get into hiking shoes (I love Merrells) they have plenty of padding and are normally a bit higher cut to give you a bit of ankle support.  Another option is to look at trail running shoes.  I would be suggesting something with a stiffer sole than your average pair sneakers.

Just go try on a few different brands and see what feels good and pair it with a good pair of socks.  Merino is expensive but worth it and last forever if looked after.
[f9jckl2] (score 2, diepte 1) I love that last sentence... goes for everything about your health.
[f9iysgd] (score 2, diepte 0) City walking - Adidas ultra boost. 

You can thank me later. I’ve used them on three continents with great success;  and they look fantastic to boot.

Hiking / villages - La Sportiva has been great to be on many cities, trails, and mountains. Some have reported limited life span depending on activity.

Take one of each. If you use them correctly they will last a long time.
[f9jbo67] (score 2, diepte 1 OP) Thanks for the tip, this is very helpful.
[f9iz80h] (score 2, diepte 0) I find that wearing my birkenstocks in warmer weather (with socks so I can avoid blisters) and wearing either good runners or hikers with birkenstock insoles in cooler weather helps me a lot! I’m also on the heavier side and Birks have been my lifesavers! They’re mildly expensive (my Arizona sandals were $125 CAD and the insoles about $50 CAD), but they’re super worth it.

However, I still get tired achy feet after a few days of heavy walking, that’s when I take a rest day. I’ll stick to busses, catch a show, or just go to cafes and people watch/catch up on life (send emails to friends family etc, flip through social media, find things to do on future days).
[f9j3thm] (score 2, diepte 0) Invest in custom orthotics (not just the generic dr. Scholls brand), invest on good shoes (I use hokas!)-- I had a podiatrist tell me I have feet problems (bunions, flatfeet)-- which lead to ankle, knee, hip problems- your feet are unique to you! I went to a walking/running shoe store where staff are trained to film me walking on a treadmill, and advise what kind of shoes to buy depending on the support that the soles gave (bounciness?)
[f9j8gmn] (score 2, diepte 0) I love a good pair of running shoe with a wide structure and some compression socks for city walk and climbing stairs. I do this as my job and I don't feel any pain or soar. But everyone's different so you should talk to a specialist.
[f9jfowt] (score 1, diepte 4) Wearing socks more than one day? Can't imagine that..
[f9jbirw] (score 1, diepte 3 OP) Are you referring to these guys?  I know they're not Yamuna brand.  Also, do you just stand on them and roll them on the bottom of your feet?  Also, how is it different from just a tennis ball?

 [https://www.amazon.com/Kieba-Massage-Lacrosse-Myofascial-Therapy/dp/B017V7UKW2/](https://www.amazon.com/Kieba-Massage-Lacrosse-Myofascial-Therapy/dp/B017V7UKW2/)
[f9jhaqq] (score 1, diepte 4) Nope, it's these:

[Yamuna Ball](https://www.amazon.com/Yamuna-Body-Rolling-Foot-Wakers/dp/B000PJTXT0/ref=sr_1_4?crid=NZSQTEJ9BQIW&dchild=1&keywords=yamuna+balls&qid=1575373922&s=sporting-goods&sprefix=Yamuna%2Csporting%2C1316&sr=1-4)-4

It comes with a video to show you how to use them, but basically you just stand on them, moving the center all around your foot, from your heel to the ball of your foot in three tracks (inside, middle, & outside of foot. You can also do calf rises and toe stretches (ball of foot 9n the floor & toes on the ball).

It may hurt at first because if your muscles are weak they will be tight.
[f9kds3e] (score 1, diepte 5 OP) Thanks for this, really appreciate it.
[f9jbesy] (score 1, diepte 3 OP) Hah, yeah, I meant drive.  But it would be awesome if I dived everywhere.
[f9jbkdd] (score 1, diepte 1 OP) Thank you for the tip, I appreciate it.
[f9jbmrz] (score 1, diepte 1 OP) Thank you for the tip, I really appreciate it.
[f9jbt3b] (score 1, diepte 1 OP) I just went to Birkenstocks' website, and seems like their insoles are a hybrid of arch support / ortho stuff, and just cushion.  How do you compare that to Dr Scholl's, both the custom arch support link below, and the $12 gel insoles?

 [https://www.tekscan.com/applications/dr-scholls-kiosks](https://www.tekscan.com/applications/dr-scholls-kiosks)
[f9jceie] (score 1, diepte 2) I personally haven’t had luck with the custom ones, and the gel ones give me blisters so I’ve given up on them as well. I like the Birk insoles (mine are the “das blaue fussbett” ones) because they help with arch support and shock absorption (the cork absorbs shock and helps with limiting the bruised feeling). They saved my butt both while traveling and while working long hours on my feet. I can’t even imagine how many kilometres I’ve put on them, and they’re still like new.
[f9jcx0h] (score 1, diepte 3 OP) That helps, thank you.  When you buy shoes, do you buy them slightly bigger so you can fit Birk insoles in without squeezing your feet?  And when the insoles are not in, does the empty space bother you?
[f9jzqqq] (score 1, diepte 4) So far, I’ve only used them in shoes that were already slightly too big, or had already been well worn (and thus were stretched out). I don’t really take them out- I’ll switch them between pairs of shoes but once I’ve started to wear shoes with them, I don’t wear them without the insoles. 

My suggestion would be to find somewhere nearby that sells them (I went to softmoc) with a few pairs or your shoes to see how they fit. There’s different sizes of insole as well, so trying them on is handy for that. If you already have a pair of birks, you’ll likely need the same size insole as the shoe.

When I buy new shoes now, I always try them on with the insoles to make sure they’ll fit. Out of all my shoes (bought before & after buying the insoles) there’s only two or three pairs that they don’t fit, and that’s because the shoe barely fits me as it is (bought on a super sale so wasn’t that concerned with the fact that they’re about a half size too small 😬).
[f9ke83s] (score 1, diepte 5 OP) Thanks for the tip, really appreciate it .
[f9jbvwi] (score 1, diepte 1 OP) Hokas are super recommended in this thread, I think I'm going to get a pair.

Custom orthotics, how do you feel about those Dr Scholl's "custom machines"?  I feel like they take the "close enough" approach, where they measure your feet and fit you for one of their 10-ish orthos.

 [https://www.tekscan.com/applications/dr-scholls-kiosks](https://www.tekscan.com/applications/dr-scholls-kiosks)
(10 reacties met lagere score weggelaten)

