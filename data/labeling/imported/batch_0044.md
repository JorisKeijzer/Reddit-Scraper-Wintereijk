# Label-batch batch_0044

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
Schrijf het resultaat naar `batch_0044.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(5 threads: 16gqyie, 17htwlv, ydkqgu, qxjyf5, cznhv6).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 16gqyie ===
SUBREDDIT: r/pharmacy
DATUM: 2023-09-12  SCORE: 76  REACTIES: 213
TITEL: Retail pharmacists: what shoes are we wearing?
POST (source_id=post):
I know nothing will be 100% comfortable being on your feet for that long but my Nikes just aren’t cutting it. Give me all your recommendations!

Side question: anyone wearing compression socks?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k09da2s] (score 278, diepte 0) Air Force 1’s so customers know I ain’t no joke if I ever gotta come from behind the counter 💯
[k09bn8h] (score 95, diepte 0) Hoka and ASICS
[k0a66jw] (score 80, diepte 0) Crocs because I don't give a fuck anymore
[k09hqm2] (score 63, diepte 1) Black Forces, of course
[k09c6e0] (score 42, diepte 0) Ultraboosts and bombas socks
[k095uog] (score 29, diepte 0) Brooks Glycerin 19 and compression socks
[k098n42] (score 22, diepte 0) Skechers!
[k09gjwr] (score 21, diepte 0) Hoka Cliftons. Go to a shoe store that actually does fitting and have them select a shoe for you. It doesn’t have to be Hokas, I see many good recommendations in this thread, but a good shoe store will observe how you walk and make recommendations based on your gait and foot size/shape. Then prepare to spend $150, but it’s totally worth it. Shoes are equipment.
[k09njew] (score 21, diepte 0) When I was on my feet all day, Dansko clogs were my go-to. Unmatched comfort
[k0a4lwz] (score 17, diepte 2) That alone is enough to make most people reconsider their course of action. IYKYK.
[k09a7c6] (score 16, diepte 0) Invest in your feet. I wear clarks
[k0abvlg] (score 12, diepte 1) Hoka Bondi and ASICS Nimbus. 👌

I have a pair of Brooks Glycerine in the closet to try so we’ll see how that goes. ASICS have been my go to for nearly 10 years.
[k09p55s] (score 11, diepte 1) Ultra boosts!!
[k09l6dt] (score 10, diepte 1) Specifically the Go Walks. Those were the only shoes I found that resulted in zero foot pain after 12-13 hour shifts. Cannot recommend them enough.
[k09kb1s] (score 10, diepte 1) I used to wear Clark’s, Naturalizer, Hush Puppies, etc. Now I wear Adidas UltraBoosts mainly. A world of difference. Don’t even need insoles anymore.
[k09pgvk] (score 10, diepte 0) When working a long shift, I change my shoes and socks at lunch. Makes a world of difference.
[k09jjnr] (score 9, diepte 0) On Cloudswift’s are currently my favorite shoes, but I also like Brooks.
[k09uqi0] (score 8, diepte 1) To build off of this I recommend the Brooks Ghost line. All I’ve ever worn since switching away from Nike and not once have my feet complained after working all day. Plus they have extra wide sizing which is hard to find unfortunately. My wife, MD, also prefers her Brooks while working
[k096l38] (score 8, diepte 0) Head to the good feet store and get a customized insert to put into any shoe
[k09ll4e] (score 8, diepte 1) I just started wearing hoka and yes must agree. I was using Altra which are great for me thanks to the wide toe box, but they are meant for running
[k09rsl6] (score 8, diepte 0) No love for croc gang in here. I worked 12h IV shifts and crocs with compression socks were the best for me
[k0aq10t] (score 7, diepte 1) Love sketchers.  Started wearing them straight out of pharmacy school and never looked back.  And sneakers are now considered professional (ie: business casual)if they are a solid black or brown.
[k0ajxow] (score 7, diepte 2) Recently got the gel nimbus 25 and I love them
[k0bwutx] (score 7, diepte 1) Get me 2 pairs, I want 2 pairs.
[k09gx55] (score 7, diepte 1) On-running shoes. These shoes will blow your mind. 


[https://www.on-running.com/en-us/shop/mens](https://www.on-running.com/en-us/shop/mens)
[k09uwrl] (score 6, diepte 1) 🎯
[k09uufy] (score 6, diepte 2) My tech and I (same shoe size) compared her brand-new On’s and my 2-yo bought-used Hoka Clifton 6’s in the pharmacy one day:  my stinky Cliftons still won for better cushion.
[k09syq2] (score 6, diepte 1) Surprised to have to go this far down to see Dansko! Great shoes that are comfortable and are actually made with your health in mind (see APMA approval).
[k0d48pv] (score 5, diepte 2) S[So I can get to stompin' in my Air Force Ones.](https://youtu.be/BfzsMQGqrt0?si=RqxwFeKSpvSxk2rw)
[k09f04m] (score 5, diepte 0) mu husband got me these new shoes and i love them so much - i think they're called QC?
[k09n8oi] (score 5, diepte 0) go get fitted compression socks at a medical supply store, game changer
[k0aqffy] (score 5, diepte 0) At work birkenstocks or ASICS.
[k0ayjow] (score 4, diepte 1) Ultra boosts, Yeezys and NMD. Adidas has been doing well
[k09nl4d] (score 4, diepte 0) Adidas ultra boost/eqt and Birkenstock Londons
[k0a9wci] (score 4, diepte 0) CROCS!
[k0965vt] (score 3, diepte 0) I liked Fila when working retail pharmacy. If you have bone spurs or other painful foot problems, it's best to spring for the expensive super shoes, but I don't know their name...

Compression socks are hit or miss. If you feel your feet swelling tremendously, then they are great, but they will have a ton of rebound swelling after a long day in the pharmacy. I only really use them if tendinitis in my ankles is an issue.
[k096x2h] (score 3, diepte 0) I just answered this in another comment.

I wear compression socks and work boots (they have much better support on concrete floors; commercial carpet glued directly to concrete is also terrible):

[https://www.smartwool.com/shop/mens-compression-making-tracks-print-otc-socks-sw003951](https://www.smartwool.com/shop/mens-compression-making-tracks-print-otc-socks-sw003951)

[https://www.carolinashoe.com/en/sarge-lo-6-inch-soft-toe-work-boot-16051.html](https://www.carolinashoe.com/en/sarge-lo-6-inch-soft-toe-work-boot-16051.html)
[k0bxf4s] (score 3, diepte 2) [These ones?](https://amzn.to/3Lnqqt8) Or is it a different type? Go Walk is apparently an entire line of shoes now.
[k0by8c7] (score 3, diepte 3) Yeah they really seem to have expanded but yes those look similar to the ones I had. It's like walking on a pillow.
[k0cgfsm] (score 3, diepte 1) \+1 to hoka. hoka bondi is amazing but dont get the SR. have both the SR's shell is too stiff and doesnt breathe, the bondi 7 i have wont make feet your issue any more just the knees lol
[k0jbgj5] (score 3, diepte 3) Can we all be friends? This is the energy 🔥😂
[k0c3k4a] (score 3, diepte 1) Also forces, in multiple colors to match the scrubs. Now that flu shots are back it’s time for me to get a new pair of black forces so people know better than to ask if the shot is gonna hurt
[k09eb8a] (score 3, diepte 0) Brooks Adrenaline GTS 22 👌🏻
[k09hq75] (score 3, diepte 0) Hoka's and compression socks everyday
[k09j90v] (score 3, diepte 0) Cloves!! I will wear nothing else.
[k09ts98] (score 3, diepte 2) I have an office now so find my feet under my desk, shoeless, with a massage ball under them 😅
[k09zqiw] (score 3, diepte 0) Hokas and Brooks. Yes to compression socks. 

Don’t worry about a gait analysis. I don’t put much stock in a 20 year old retail associate/long distance runner at a running store analyzing your gait, and it’s not necessary anyway. Buy the shoes that are comfortable. 

Cushy, stable, somewhere in between. What feels good to you.
[k0a3ck0] (score 3, diepte 0) Even if you don’t feel you need compression socks it’s probably a good idea to because of the risk of clotting associated with blood pooling in feet/lower legs while standing all day. Especially if your feet feel “full” or look really red after work.
[k0a9hp9] (score 3, diepte 0) Started with brooks and moved to Hokas. Hoka is much better if you get the cushioned kind. I also have a pair of all white Nike Air Max 97’s but I have Dr Scholl’s inserts in both
[k0acchp] (score 3, diepte 0) Stilettos….. so I can tower over my patients and colleagues….. JK I wear Brooks.
[k0b7e7r] (score 3, diepte 0) Red Wing Boots. Only need to drop a pallet on your foot once to appreciate a good safety toe boot. Support is very good, and it better be for boots that are damn near $300.
[k0cwfk2] (score 3, diepte 0) Not a pharmacists, Just a tech. But I used to have horrible bad pain due to the shows I was wearing, but until I switched to Brooks. They’re mildly expensive but with how much I’m working and moving there has been a massive improvement to my back pain.
[k0cksoa] (score 2, diepte 1) Brooks for the win! I found a super cute pink pair when I first started working inpatient (I know this is for retail). A lot of nurses wear Hoka, so that's also a good one for support.
[k0c60zb] (score 2, diepte 2) Agree. I used to wear Danskos but they got too heavy. I only wear sketchers now!  I love sketchers but they change the product lines so much that o can’t keep ordering the same ones.
[k0gx5v4] (score 2, diepte 1) For sure Asics. Nimbus
[k0bx30e] (score 2, diepte 2) They dont make Yeezys anymore I thought?
[k0barit] (score 2, diepte 1) Big time same!!!
[k0biz8s] (score 2, diepte 1) I second the Brooks Adrenaline. Great shoes for running, walking or simply standing.
[k09gsh8] (score 2, diepte 0) Ultra boosts and compression or tight sport socks.
[k09jls8] (score 2, diepte 0) Cole Haan shoes. Kinda pricey (can easily be over $120), but work for both work & play.
[k09k5tv] (score 2, diepte 0) Compression socks…I have before. But knee highs are usually more than sufficient. And ever since I went for sneakers, never going back. When I was hired I was told business casual, leather shoes …yeah never again. I still have my good leather shoes but I’m sticking with sneakers for comfort.
[k09l1rc] (score 2, diepte 0) Consider getting an insole consult at a running store. That helped me a lot. Now I have special insoles I put in whatever shoes I wear. Ecco Lisbons with Superfeet Orange insoles, in my case.

And yes, compression socks ALWAYS. Sockwells are my favorite sock brand. Wool blend with some fun patterns and colors.
[k09n2ic] (score 2, diepte 0) Hoka every day. I have two pairs that I alternate.
[k09ttkj] (score 2, diepte 1) Tried the croc clogs…just didn’t cut it compared to Dansko (esp XP 2.0)
[k09sbpg] (score 2, diepte 0) Dansko LT clogs. I made the switch earlier this year and I'm an idiot for waiting so long.
[k0c5uid] (score 2, diepte 2) My aunt who used to be an OR and ICU nurse for 30 years recommended Dansko when I started pharmacy school. Since XP 2.0 came out I’ve preferred them over the professional version. I haven’t tried LT yet because I’ve seen lots of comments that said LT is not as good as XP.
[k0a451c] (score 2, diepte 0) Adidas ultraboosts and compression socks. Breathable and my feet feel normal at the end of the day.
[k0a6gnm] (score 2, diepte 0) I know Hokas are popular but I got my feet fitted and was able to try Hokas for a few days and they hurt me after a 2-3 hours. Now I’m wearing New Balances 530 that are slightly bigger than my own size with heel inserts. Still hurt towards the end of the day but this is the best I’ve had so far
[k0ai91f] (score 2, diepte 0) I wear New Balance Roav and they are by far the most comfortable sneaker I’ve found
[k0awjpd] (score 2, diepte 0) I was all about Hoka but I just for a pair of New Balance Fresh Foam X and they’re awesome. 

Also, compression socks. My legs are a mess.
[k0b2w6v] (score 2, diepte 0) Off topic, but compression socks are a must!
[k0reo8y] (score 2, diepte 2) Yeah, I don't do the conventional "compression stockings or socks." Meaning, not the 20 or 30 compression. I just do quarter or crew high athletic compression socks, and they do make a difference. I find knee-high, high compression stockings to be tight and sweaty myself. I just buy 6 packs of ankle high athletic compression socks and even no show socks that I buy from Amazon.
[k0rfb56] (score 2, diepte 3) One I like:

https://www.amazon.com/dp/B09PC4T3XG/ref=sspa_mw_detail_6?ie=UTF8&psc=1&spc=MTo4MzY1NzUwMjQ0MzEzNjIyOjE2OTQ4MTY2OTQ6c3BfcGhvbmVfZGV0YWlsOjIwMDAzOTA2OTU1Mjc5ODo6Ojo&sp_csd=d2lkZ2V0TmFtZT1zcF9waG9uZV9kZXRhaWw
[k0rfebp] (score 2, diepte 4) Another I like:

https://www.amazon.com/Compression-Running-Support-Fasciitis-Athletic/dp/B07W4P8DXK/ref=mp_s_a_1_5_pp?crid=1VSUX2TMUO3BH&keywords=compression+socks+for+women&qid=1694816748&sprefix=compress%2Caps%2C199&sr=8-5
[k0uwz05] (score 2, diepte 3) I didn’t know they had these quarter socks 
Just ordered to try it 
Thanks for sharing
[k0v1a94] (score 2, diepte 5) Working in long term care I was on my feet for 8 hours straight and that was tough now I’m in independent and get to sit occasionally but still retail standing involved on busy days 
Hope all is well on your end
[k111uap] (score 2, diepte 6) I like the compression socks so much that I wear them on days off as well.
I went from 14 hours standing all day in retail to long term care, where I do a combination of sitting and standing. Some shifts are standing all shift, some are sitting all shift, some are a mix. Personally, I prefer the mix, half and half sitting and standing. 
I'm just happy to finally get lunch breaks!
[k15yg9w] (score 2, diepte 8) Actually, no. It was Rite-Aid and QFC. 
The socks make the biggest difference when also worn with good shoes. I wear Asics and Adidas with my compression socks. Good luck! Wishing you happy feet!
[k16olpe] (score 2, diepte 9) Thank you 🙏
[k09xjis] (score 1, diepte 2) I like the Ghost line as well.  Almost as much cushion, and far more color choices.

I’ve worn and run in Brooks for years (separate shoes for running and working) but just started wearing compression socks.  Game changer.  Noticeable improvement at the end of my shift.
(134 reacties met lagere score weggelaten)

=== THREAD 17htwlv ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2023-10-27  SCORE: 162  REACTIES: 181
TITEL: What are we wearing on feet today chefs
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k6prhrd] (score 66, diepte 0) I'm wearing the croc clogs from their line for workers. They're actually pretty decent
[k6q404o] (score 27, diepte 0) Bistro Crocs checking in.
[k6qhjf8] (score 24, diepte 1) this. This right here is why it infuriates me to see people wearing tennis shoes, or trainers in the kitchen. And im like 'hey, you need non slips' and theyre always like 'haha i know right?' no. I mean, you need fucking nonslips. Theres 8 walmarts every 4 miles and they dont cost shit, and they have 50 different styles, and goddamnit, WEAR NON SLIPS

or or or 'Ive never fallen before!' IT DOESNT MATTER. Ive never been in a, airplane crash. It doesnt mean no airplane ill ever be in will ever crash. Just put them on. Why, why does it matter so much. JUST WEAR THEM
[k6pxigy] (score 21, diepte 0) Slippers! (It's my day off).
[k6q2h8j] (score 20, diepte 0) wearing $15 work shoes from walmart that have gel inserts and raised heels
[k6qm1di] (score 15, diepte 2) I don't know how many kids I sent to Walmart for just thus reason

Like, no. You need nonslip shoes or you're not coming in the kitchen
[k6q7sbh] (score 14, diepte 0) Is this a real question, or do you just want everyone to know that you spent $250 on designer work shoes 🧐

They're nice, btw
[k6qk779] (score 12, diepte 0) The Birkenstock Clogs are my favorite. Along with a pair of really good socks and then a normal pair of cheap socks beneath the good pair. I buy the shoe up at least half a size or get it in wide to compensate for the socks.
[k6q9026] (score 10, diepte 1 OP) Why not both 🤷‍♂️ plus got them on sale for only $100
[k6qdnj3] (score 9, diepte 1) I’ve had a pair of those since 2020. Just wore them painting ceilings today. Put much hours in restaurants with them. Best you can get.
[k6psqkl] (score 9, diepte 0) with no venting that i can see in those, does your shoe become a swamp by the end of the day?
[k6q69y0] (score 9, diepte 0) Docs, the kitchen Chelsea boots. Can't even think about going back to clogs anymore.
[k6q7gcb] (score 8, diepte 1) Moccasins for me! A toast to you my friend
[k6pszpp] (score 7, diepte 1 OP) Lol no. The fit is pretty roomy plus I work with lots of liquids so don't want a way for them to drip in.
[k6qlqrf] (score 7, diepte 1) Cannot be beaten for the price, the little spiky bits inside wear down in a couple months buy in the mean time I love the mini massage.
[k6q533e] (score 7, diepte 0) Crocs Bistro. Can't go wrong. I have a pair of Birkenstocks and I will wear my Crocs over those any day.
[k6qaget] (score 7, diepte 3 OP) I still think they have a few left on ssense
[k6qtzhe] (score 5, diepte 1) I've had the same pair going on 4 years now. I don't have the proof to back it up but I swear those fuckers have at least 20k miles on them ..And that's being conservative. They're still going strong. The bonus is they're comfortable. It sure as hell beats being a new pair of kitchen shoes every 4-6 months.
[k6pzyc7] (score 5, diepte 1) Depends on how sweaty your feet get. I got similar ones from Shoes for Crews; after a few hours the stank could be considered a bioweapon.They're comfortable as all hell tho.
[k6qi0d0] (score 5, diepte 2) they weigh next to nothing, they are form fit to your foot, and they can be sprayed clean, inside and out. Anyone who says theyre trash just doesnt like the brand. They are absolutely objectively the best shoe for kitchen work. If your feet hurt after 8 hours of standing, it probably doesnt matter whats on your feet, they are going to hurt.
[k6qlr7v] (score 5, diepte 3) I went my whole life getting insane back pain after standing at work 10-12 hours at a time and just figured it was part of life but then when I turned 35 I bought a pair of Dr. Scholl's inserts and the pain went away completely. I wish I had known years ago how awesome they work, could have saved me years of agony.
[k6q9jgn] (score 5, diepte 2) Oh, I'd for sure scoop them for a hundo. I'm just jealous lol
[k6qrj9v] (score 5, diepte 0) Birkenstocks forever
[k6r2ad6] (score 4, diepte 1) Enjoy your day off, chef!
[k6qnnvm] (score 4, diepte 3) I work with a girl who has the unfortunate situation of kinda looking like Violette from Willy Wonka after she eats the chewing gum meal and gets to the blueberry pie for dessert. This lady wears just the most worn pair of crocs I have ever seen and she once literally slipped on water droplets that fell on the floor as she was washing her hands. boss refuses to make her wear nonslips as since there isn't any oil fryers, technically he wasn't forced to make people wear non-slips.
[k6rcln7] (score 4, diepte 1) I was always rocking some $15 Walmart running shoes with custom made medical orthotic insoles. Shoes get trashed so fast in the kitchen, why not just buy new cheapos every few months?
[k6q4ujo] (score 4, diepte 0) Danskos in brown
[k6qjv07] (score 4, diepte 2) I put Dr Scholl’s gel inserts in mine, immediately got better.
[k6qn0ek] (score 4, diepte 4) Yes. If you can’t afford custom orthotic inserts, the Dr Scholl’s $15 inserts are the next best thing. Those crocs are great but don’t have a lot of natural cushion.
[k6q7poi] (score 4, diepte 1) I have the Blundstone version, I wouldn't go a day without. Steel toes too. Crock's and slips are just a problem waiting to happen
[k6q7abf] (score 4, diepte 0) Day off with some sausage on the smoker so moccasins! Daily work kickers are a pair of Blundstone Chelsea's. Steel toes, safety rated, leather for quick cleaning, and with a good pair of insoles, they're amazing.

Hot? Yes. Heavy? Barely. Smelly? Lysol.
[k6qohax] (score 4, diepte 4) It’s an investment. Buy an $80 or $100 pair and the last at least three times longer than the Walmart bullshit. Try Birkenstock - Birkis
[k6qcs64] (score 4, diepte 0) Got some non-slip hokas 💪🏼💪🏼💪🏼
[k6rek5y] (score 4, diepte 2) Yo that. It's now Birks+wool socks season and I'm ready
[k6qjhx4] (score 3, diepte 1) The best!
[k6rmznk] (score 3, diepte 2) Someone should buy a pair of the kitchen crocs and day 1 put a pedometer on them like flair. See exactly how many step before you need a new pair. I bet it’s north of a million. On the flip side I owned a 140$ pair of Reebok “kitchen shoes” that were in full Aladdin mode after 6 days of work.
[k6ps9fh] (score 3, diepte 0) I’ve been wearing alpros, for years. I love these shoes. I have the steel toe ones. Saved me a few times
[k6qdu2f] (score 3, diepte 1) Wool socks. Even in the summer. No stink. It’s the only way
[k6px9y1] (score 3, diepte 0) The mozo pseudo-Vans
[k6q30fi] (score 3, diepte 1) Do you like those? I used to wear the mozo sharks, but after shoes for crews bought them, they haven't been the same
[k6qjyr3] (score 3, diepte 1) Yup. Even out of the industry about 2 years now I wear my last pair of Bistros as my “walk to the mailbox” shoes
[k6qw16w] (score 3, diepte 1) $250, but they will last forever, and his back, and knees will thank him 10 hours into a double.
[k6q8ved] (score 3, diepte 0) Redwing boots and Dr. Scholls heavy duty insoles.
[k6qxc83] (score 3, diepte 1) Birks for life
[k6riv84] (score 3, diepte 1 OP) Used to use those good choice
[k6rbf1h] (score 2, diepte 1) Seriously though. These things are goat
[k6qe4v3] (score 2, diepte 2) I dont remember where i got the ones Im currently rocking, but they have side vents just above the sole. the last ones from Corcs work line were ventless and damn i was sloshin by about 8pm
[k6q29i3] (score 2, diepte 0) Some shoes I got for free from the company. Hey free shoes
[k6sxg1l] (score 2, diepte 2) Shits expensive, $25 for the cheapo ones at Wal Mart
[k6rgjv9] (score 2, diepte 2) exactly!
[k6t9f6k] (score 2, diepte 3) 12 hrs /5 days per week.
[k6qgkdl] (score 2, diepte 1) See, I see so many people wear crocs bistro here, so I bought a pair. I wear them at work, and then come here and say my feet hurt from standing 8 hours and people are like "you're wearing trash, take better care of your feet". If they're trash, why is half this comment section crocs?
[k6ti8j9] (score 2, diepte 2) I was just commenting about how I have my very first pair and use them to run to the garage, mailbox, around the lawn ect
Perfect for that, super easy to slide on/off and completely waterproof (my lawn is often super wet & I live on a lake)
[k6q64fe] (score 2, diepte 0) Sketchers work shoes, wide, non-slip. I've tried a bunch of other work shoes and these are the only ones I find comfortable but don't fall apart the first year I use them.
[k6qhnlc] (score 2, diepte 2) I have the RedBack version, they are like standing on clouds but super tough and durable. Also steel toes.
[k6r6ylq] (score 2, diepte 2) Yes, ive got a jacked feet and a bad back from way too many years of 60+ hour weeks on hard kitchens floors.  I swear by these boots now.
[k6q77k7] (score 2, diepte 0) Bought some Birkenstock Tokio's at the suggestion of a coworker. They're super nice, and they'll last me a long time, but I don't think I'd spend $160 on another pair.
[k6q86hq] (score 2, diepte 0) Crocs with insoles lmao
[k6qdgyk] (score 2, diepte 0) We are required to wear safety shoes here so just your everyday steel-toed.
[k6qk06o] (score 2, diepte 0) Knock-off sketchers "no slip service industry black shoes for restaurant" available at Walmart for $15.
[k6qlu53] (score 2, diepte 0) I have a related question: what brand do you guys with 4W feet get for kitchen wear?

My partner wears a 14 WWWW, and finding shoes that don't cost a fortune, are skid/oil resistant, and will last longer than 3mo is a pain in the ass

Suggestions, please
[k6qobyv] (score 2, diepte 0) Birkis baby. 
  I’d say they are top of the shelf. 13 years experience here
[k6qorub] (score 2, diepte 0) Newbalance non slip
[k6tihyr] (score 2, diepte 1) My favorite by far
[k6tj2i6] (score 2, diepte 2) I’m surprised it took me this long tbh. And they’re so easy to clean!!!!!!
[k6qscu2] (score 2, diepte 0) Birkenstock Super Grip Professional Boston Clogs
[k6qvkgr] (score 2, diepte 0) I’m wearing my Birkenstocks but my boss just told me there’s a new rule and birks and crocs aren’t allowed starting January one (corporate). They give us a great shoe stipend but I’m so sad because they are the best shoe ever and I don’t know what to get
[k6qw84l] (score 2, diepte 2) Ugh I think someone hurt the back of their ankle at some point or something- I work for compass/bon appetit so it’s a big company, so who knows what happened.
[k6r1mtp] (score 2, diepte 5 OP) Yeah I got one when I started working there but I'm relatively new
[k6qw5pe] (score 2, diepte 0) New balance non slip
[k6r6n05] (score 2, diepte 0) Skechers cessnocks. On my second pair. They last about a year before giving up
[k6r9sg7] (score 2, diepte 0) Most the food cooked in the last year lmao that’s what’s on chefs feet
[k6rfavz] (score 2, diepte 0) New balance. 574.
[k6rnssp] (score 2, diepte 0) Snibbs but my first pair of Mozo arrive tomorrow.
[k6u5m6h] (score 2, diepte 2) Yeah. They were okay but I'm ready for a change. The first pair of Snibbs was fine for a year but the second pair has fallen apart fairly quick. I had to cut part of the sole away as it has been slowly peeling apart and it was tripping me up at work.
[k6s74ot] (score 2, diepte 0) I hate slip ons… I need my shit laced up in case I gotta do karate or skateboarding. Never know
[k6s8www] (score 2, diepte 0) I have never understood clogs in the kitchen.  If you spill a pot of boiling water, your feet will be destroyed.  I know lots of people wear them and love them.  But it goes right over my head.  I don't know what the draw is.

Wear waterproof boots and you'll be safe.  I also prefer something that gives me ankle support.

Clogs make no sense to me.  They just seem dangerous.

As a side note, if you're doing an 8 - 10 hour shift standing the whole time, you will benefit (especially in the long run) from wearing compression stockings.  They're kind of a pain in the ass to get used to, but once you get used to them, you'll be less fatigued at the end of your shift.
[k8yz16l] (score 1, diepte 1) I've had those in black for 5-6 years and if you blast em with a hose they're good as new.
[k6qnxw9] (score 1, diepte 3) Thick socks do the trick for me to prevent that sloshing. They also become the Chernobyl Elephant Foot.
[k6q38d4] (score 1, diepte 2) Yeah.  They're the only kitchen shoes I've bought that last more than a few months, but I usually replace them after a year.
(93 reacties met lagere score weggelaten)

=== THREAD ydkqgu ===
SUBREDDIT: r/Residency
DATUM: 2022-10-26  SCORE: 119  REACTIES: 178
TITEL: Best shoes for residents?
POST (source_id=post):
I’m looking to get new shoes this week (always excited for payday lol!!).
My old shoes are sketchers but pretty ill-fitted and slippery on the hospital floors for some reason.
Which is the most affordable yet comfortable shoes to wear being on your feet the whole day?
Any suggestions?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ittbd1i] (score 78, diepte 0) Birki, don't go cheap when it comes to your feet.
[itsrlbo] (score 77, diepte 0) I’m just gonna echo what I’ve heard on this sub.

Adidas Ultraboosts 100%
[itssbqx] (score 69, diepte 0) Everyone on here says ultraboosts and if you’re like me and hate them. Then I’ll just list some upper tier running brands that make great products….Hoka, On, Karhu, Saucony. 

I personally love everything Hoka and also have found the Karhu Ikoni shoes the best walking shoes I’ve ever owned. I say this as someone who runs 100 miles a week also.
[itt4r9j] (score 66, diepte 0) Crocs gang
[ittfyb1] (score 58, diepte 0) If you have a medium/high arched foot, Birkenstock Boston clogs!!  your toes are covered and you can easily slip them on and off. Once was on 24hr call and walked 30k steps, feet still felt fabulous.
[ittdzvh] (score 40, diepte 0) Allbirds. Machine washable. I’ve got a new pair every year. PGY5 General Surgery
[itt74ij] (score 31, diepte 0) Merrels. Last forever. Comfortable and stuff sole.
[ittdmp6] (score 31, diepte 0) 3inch heels mostly
[itt0wab] (score 30, diepte 1) Saucony but GO GET FITTED AT A RUN SHOP
[itt5w33] (score 30, diepte 1) 3.5 hour rounding has entered the fuckin chat
[itt9aj3] (score 28, diepte 0) I adore my Brooks. I was in so much pain on a surgery rotation standing on those concrete floors in my regular shoes. I still hurt after a 12-hour day but much better
[itssmv1] (score 25, diepte 1) A few years ago I was a patient transporter for the surgical department at my hospital. On a busy day, I’d walk 10-12 miles. Adidas ultraboosts all the way!
[itu6rmy] (score 23, diepte 1) I bought some because of the medical subs and was not super impressed. They’re just okay. Probably the best choice in that price range, but I’d rather fork out more for ultra boosts or hoka or just go with Crocs
[ittj5vi] (score 23, diepte 0) Get fitted at a running store.

That being said the most comfortable shoes I own are the new balance 860s. I need a little more stability.
[itst0ot] (score 21, diepte 0) Clarks. I got a lot of laughs for being in scrubs and dress shoes but they saved my feet and back.
[itsy0si] (score 18, diepte 0) There’s a company called SAS - San Antonio shoe company. Wore them everyday in surgery intern and even to this day. Not the prettiest, but never had feet problems since.
[itsv4qj] (score 17, diepte 0) My mom bought me the UGLIEST pair of Hoka’s when I was an intern and they were so damn comfortable that now I own 4 pairs…
[itst1n8] (score 15, diepte 1) I got some Hoka Bondis two weeks ago and I absolutely love them!!
[itt5djg] (score 14, diepte 1) I thought I was the only one…people rave about ultraboosts but I was disappointed. Too bulky, too tight under the laces (I’ve never had that problem, I can’t imagine it would work well for wider feet.)
[ittpp9z] (score 14, diepte 0) Nobody wears dansko anymore?
[ituidif] (score 13, diepte 1) They just look so terrible
[ittrp0s] (score 13, diepte 0) Custom made cowboy boots
[itt5yce] (score 10, diepte 2) Yeah, they are pretty heavy with low quality foam for the price… most people suggesting them probably haven’t tried very many running shoes. I used to work at a running store that had them and virtually everyone would chose Hoka, Saucony, etc over adidas with the exception of their high high tier carbon shoes. Same story with Nike.
[ittbn4s] (score 10, diepte 1) The ultraboost used to be pretty solid for easy mileage but they became more lifestyle than anything. I find them pretty heavy and lack upper support 

I'm still using my retired Hoka Clifton 1's, the ones with the yellow midsole 😄
[itue4a1] (score 10, diepte 1) For people with sweaty feet, if you notice your feet start smelling after wearing crocs switch to leather clogs like danskos, been great for me.
[itukghv] (score 10, diepte 1) Replying here for visibility!

Birkenstocks get their reputation for comfort primarily from the cork bed. This will shape to your foot over time, much like leather would. High quality insoles with support can mimic this benefit in many shoes.
Birkenstocks cut in half:
https://youtu.be/XxFmZ8uxRfc

As for running shoes ultraboosts get their credit from the energy return. This gap has quickly closed with improvements in foams from other brands. Hokas with their extremely high levels of cushion have shown some detriments to knees over high impact high mileage.
Comparison of ultraboosts and other similar brand shoes here (lots of useful info starting at 5:30):
https://youtu.be/EUu4smb6XRY

Basically, go find a shoe that "fits" well and feels comfortable (ultraboosts energy return/cushion won't mean shit if the shoe is too narrow). Replace the insole if needed. Get multiples and rotate shoes.

My personal favorites right now are New Balance Made in USA series (or made in UK). High quality materials and just the right amount of drip.
[ittq2gb] (score 9, diepte 2) Indeed, they are sneakers.
[itu8z78] (score 9, diepte 1) Former pharmacy tech here, with a really bad knee.

My ortho recommended Brooks and the difference in how my legs/feet felt after work was like night and day.

Invest in good shoes if your job keeps you on your feet.  It's worth it.
[ituasng] (score 9, diepte 1) Word of caution, Allbirds (and least the version I got of their “runners”) have no support and gave me chronic foot pain. I wear Brooks
[itt0ajt] (score 8, diepte 0) I'm not sure if my feet are just wierd shaped, but I never seem to find the latest "recommended work shoe" fits or works for me. 

Try things on. Go somewhere that has lots of options. Try athletic shoes, dress shoes, cowboy boots, expensive cork footbed, whatever. But make sure they fit your feet and how you walk!
[ittgwed] (score 8, diepte 1) Got my vans on but they look like sneakers…
[ittx96e] (score 8, diepte 0) Ariat cowboy boots
[itsses8] (score 7, diepte 0) I like my Cloves. They broke in really nice and now I wear them even when I’m not at the hospital. Though my meet so sometimes still ache after rounding for a long time.
[itueav2] (score 7, diepte 1) I have danskos and they’re great for the long cases. Happy with my switch from ultraboosts
[itvy80i] (score 6, diepte 2) boston clogs
[itudkn6] (score 6, diepte 1) I second this, along with good compression socks (I personally use ProCompression).
[itu0p74] (score 6, diepte 0) Got fitted for a wide size Hoka at a running store. The first time I didn’t have leg/calf pain after a long day in the OR was about a week into breaking in my Hokas. My wife actually reminded me to get the massager out for my calves but I had forgotten to use it because I didn’t have pain. Hoka for life
[ittf4j4] (score 5, diepte 1) This is the way
[ittf75x] (score 5, diepte 2) Wide foot here. They are bliss for wide feet 🦶
[itunqum] (score 5, diepte 1) Which kind?
[ittgm9w] (score 5, diepte 0) Buy shoes that EMTs wear.
[itt1che] (score 4, diepte 0) Calzuro if you do a lot of standing like rounding for a while or in the OR. Get the comfort insole. Ergonomic, only shoe where I can stand for hours and not feel fatigued. Also easy slip on and off so feet don’t get sweaty. However easy to roll your ankle. I also use hoka bondi7 which is very comfortable and great for running around the hospital but not antistatic and I still prefer calzuro for standing.
[itt4mt7] (score 4, diepte 0) Vans + insoles = ❤️
[ittxi7g] (score 4, diepte 1) This right here
[ituheet] (score 4, diepte 2) I bought a pair of Brooks as a pharmacy tech- they made it through med school and residency. I'm on my second pair now, but I still wear my first for yard work.
[ittnkr9] (score 4, diepte 1) Boots? I wear boots and Salomon shoes as a medic, guarantee you'll never get anything more durable than Salomon's, but they're pricey. The quick lace is also nice. Definitely made for function and not fashion though.
[itu6o3d] (score 4, diepte 0) Jordans
[itv6rlu] (score 4, diepte 0) Hokas for rounding, calzuro for the OR
[itv2a52] (score 3, diepte 2) This made a huge difference. Intern year had unfitted sneakers that gave me sore feet. Invested in Saucony that were fitted in a run shop where they looked at my gait and need (“a very slow 5k every day”). Never felt like I had to break them in or issues with long rounds.

Ultimately I think what matters is partly the brand, but more importantly the need and fit assessed at the store.
[ittssqv] (score 3, diepte 1) I’m impressed you can fit in 100 miles a week in residency. Well done haha
[itvtfgg] (score 3, diepte 2) Oxfords not brogues. 

Can’t remember the exact line but I think they were the whiddon cap Oxfords. In retrospect would’ve liked them more cushioned on the sides with same arch support.
[itsvtnd] (score 3, diepte 0) LL Bean duck boots, boat shoe version. Great for the OR.




https://www.llbean.com/llb/shop/19067?page=mens-llbean-boots-rubber-moc&
[itszrb0] (score 3, diepte 1) They make really good shoes
[itt0z0o] (score 3, diepte 0) Nike Pegasus 38 is my go to.
[ituz42g] (score 3, diepte 1) bikrenstocks? which ones?
[itwzxvw] (score 3, diepte 4) Suede is a type of leather, but I don't actually have an answer to your question
[ittt8gm] (score 3, diepte 1) Second!
[itua69a] (score 3, diepte 1) Key words: “I’ve got (sic) a new pair every year”. 
I’d like my shoes to not look like shit after just 1 year 😅
[ittgwkd] (score 3, diepte 0) On Clouds- has to be the Cloud Flow, others are inadequate
[ittlfvb] (score 3, diepte 0) I really like Atoms. Not a popular pick, but the brand is also not super well known. They’re soooo comfortable, even after full time use for 2 years.
[ittndmi] (score 3, diepte 0) LA Gear
[itu0qql] (score 3, diepte 2) Agreed. Once you break in any real boots, the comfort is off the charts.

I swear by my Ultraboosts too. My wide feet feel at home in most of their stuff. Less so the new ones, more the original few versions.
[ittzl5s] (score 3, diepte 0) Acsics gel nimbus
[ituij35] (score 3, diepte 0) Danskos!
[itvamb6] (score 3, diepte 1) Idk many of us are rounding or standing in the OR for hours without a break. Feeling comfortable while that happens is actually a massive quality of life shift
[itw044e] (score 3, diepte 3) first time?
[itukrh2] (score 2, diepte 1) This. Especially now that they dropped Kanye.
[itwyb8k] (score 2, diepte 3) Sorry, dumb question, but I've run with Nikes (Structures) for years, should I switch to a different brand then? I haven't heard anything about low quality shoes with them and I wasn't sure what to search for haha
[itx3752] (score 2, diepte 4) There’s nothing wrong with most Nike shoes. Just there’s better quality running shoes for the price which is why people usually switch over for their training shoes to something like a Hoka Mach and then race in Nike Vaporflys or whatever. If you like those shoes and they don’t cause you pain running then keep using them if you’re happy. If you want to talk more about shoes and stuff to try feel free to PM me I’m a big nerd on this topic
[itx3972] (score 2, diepte 5) Thank you so much!
[itszr10] (score 2, diepte 0) If you have wide feet Merrill Moab boots are excellent. They are very comfortable and hold up well over time. They are breathable so they don’t get too hot.
[itt0y2c] (score 2, diepte 0) Adidas ultraboosts changed my life
[itts6it] (score 2, diepte 2) It may depend on your foot width but I would size down on the calzuros as I found them too likely to slip off my feet while walking
[itub6gp] (score 2, diepte 2) This right here
[ituiv1i] (score 2, diepte 2) They just fit well! I use the all leather version of the jungle Mocs. Started using them when I was a third year on surgery. Still using them seven years later. Oh wow I’m getting old noooooo
[itw0poh] (score 2, diepte 3) im assuming the leather ones not the suede ones right?
[ittbg8p] (score 2, diepte 0) Vessi shoes. Waterproof. Very comfortable. I have two pairs and wear them everyday in the OR.
[ittc7ko] (score 2, diepte 0) The one admin shoved up our butts !
[itucwvn] (score 2, diepte 2) I mostly get a new pair because I collect the different colors, not because they are torn to shreds. I still wear my old pairs
[itudelh] (score 2, diepte 3) I’m just teasing. I do think that allbirds start to look a little lifeless after a few washes but I think they’re cool. Funny how trendy they were though and now I never see em anymore, Hokas are the new thing.
(96 reacties met lagere score weggelaten)

=== THREAD qxjyf5 ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2021-11-19  SCORE: 2623  REACTIES: 158
TITEL: Did I miss it? Are meat cubes over?! Here's some chicken feet.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hl9vnra] (score 488, diepte 0) FEET CUBE FEET CUBE FEET CUBE
[hl9yc1p] (score 362, diepte 0) This is more a of a feet sheet
[hla104e] (score 206, diepte 0) How many cubic feet is that?
[hl9wlf2] (score 122, diepte 0) I spent a couple weeks in Trinidad years ago where I ate many unholy things. Chicken feet being one. You literally just gnaw cartilage off the bone. I thought that was crazy enough until they brought out the bowl of fried beaks. Kind of like eating stale corn nuts.
[hl9yxew] (score 116, diepte 1) GIB FEET CUBE ༼ つ ◕_◕ ༽つ
[hl9x3pu] (score 103, diepte 1) TIL bugles are just fried chicken beaks
[hlabq0q] (score 95, diepte 1) CUBIC FEET, CUBIC FEET!
[hla2ejs] (score 81, diepte 1) Approximately one cubic feet.
[hla24h6] (score 52, diepte 0) I will never not upvote meat cubes, please keep them coming!
[hl9xjk6] (score 45, diepte 0) Damn fine chicken stock right there.
[hlakg2c] (score 44, diepte 2) One cube of feet.
[hl9zbqw] (score 43, diepte 2) Its like a lolipop..  of feet.
[hla4ndk] (score 39, diepte 1) Pheonix claws/braised chicken feet is among my favorite dim sum dishes. They're first boiled to prep them for frying which gets the skin all bubbly and chicharron-y. That texture becomes a sponge for a sweet/savory sauce that it's braised in for hours where the tendons and cartilage get all melty and tender
[hlaw219] (score 37, diepte 1) So we had meat cube, octopi cube and now feet cube.

It almost looks like a fetish list.
[hla2csi] (score 35, diepte 3) Bugles are pretty dank ngl. It’s been a long time since I’ve had some. Used to like wearing them on my fingers like I’m Freddie Kruger or some shit before eating them off one by one
[hla1gfo] (score 34, diepte 0) #FEET CUBE
[hla0mu2] (score 26, diepte 2) Now I want a beer and some bugles
[hlb9w3w] (score 26, diepte 1) Holy sheet!
[hl9x9jw] (score 23, diepte 0) All hail meat cube
[hl9xl8s] (score 22, diepte 1) I don’t like eating the feet but feet stock has its own distinct taste and once you get a taste it’s hard to come off it.
[hla8g1l] (score 21, diepte 1) I just started my chicken feet and wing tip stock this morning. Prepping for Thanksgiving.

Not in the business anymore, but still need to cook for 20+ every holiday.
[hla4s43] (score 19, diepte 1) It's relatively popular in Cantonese cuisine (braised as in [this preparation](https://www.youtube.com/watch?v=z5el7kyltSs&ab_channel=ChineseCookingDemystified)), but the Chinese also eat chicken feet in that gnawing-cartilage-off-the-bone style like as a cold appetizer salad or  even in like a crispier spicy drinking snack style. I wouldn't really call it unholy -- developed a particular fondness for the beer snack version, but the cold app style can really hit the spot, too.  
  
A little more unholy, and something I didn't try more than once, would be [rabbit heads](https://www.vice.com/en/article/xyjgv4/chengdu-is-obsessed-with-sucking-brains-out-of-rabbit-skulls). Or pigs brain, but that stuff can be delicious.
[hl9xdrj] (score 17, diepte 3) Oh don’t get me wrong I’d fuck some bugles up rn
[hlaemmg] (score 16, diepte 2) 12IN^2
[hla2sg9] (score 15, diepte 5) mmmmm boogles
[hla2kml] (score 15, diepte 1) I know we just met but I think I love you
[hl9zh3i] (score 14, diepte 0) This Kills The Chicken
[hlbtdos] (score 13, diepte 2) r/anime crossover
[hla2kpi] (score 13, diepte 4) I go through spurts where I eat them a bit and almost always with a beer.

I put them on my fingers then snort them with my nose and let go of pressure so they can fall on my tongue. You'd think it's too much salt.
[hlbt7o0] (score 11, diepte 2) i always tell my fiancee, "imagine eating chicken feet on your first date" as we both eat chicken feet lol.

or we somtimes we'll say, imagine if one of us wasn't chinese and you're just watching your chinese SO spit bones out onto their plate.
[hlary3f] (score 11, diepte 0) Just found a local person who sells dried chicken feet and my dog goes nuts for them. We had a crazy heat wave and he's a great Pyrenees so frozen towels and chicken foot popsicles really helped. I know this is off topic but I think it's a fun little anecdote. Also I LOVE THE CUBE META. KEEP IT COMING LADS
[hlaex97] (score 10, diepte 5) Dammit you guys get all the good shit. I’ve had chocolate covered flamin hot Cheetos once
[hlajxg8] (score 10, diepte 2) Always Sunny*

"Frank always makes me eat the beaks"
[hla8o6u] (score 10, diepte 1) OCTOCUBE IS BEST CUBE
[hlcy5w5] (score 9, diepte 5) I guess you might say that the cube is a bit out of your depth..
[hlanc5t] (score 9, diepte 1) uh guys... feet cube looks like it's waking up...
[hl9x7xk] (score 9, diepte 2) At least Bugles have flavor
[hla4aaf] (score 9, diepte 1) Yes.
[hlci5kl] (score 8, diepte 4) I’m 2d. It’s a square to me
[hla90xd] (score 8, diepte 4) Dont forget the corn! This is America dammit!
[hlad631] (score 8, diepte 2) The yellow feet make a beautiful golden color broth.
[hl9yu6u] (score 7, diepte 3) Salt flavored!
[hlacoj8] (score 7, diepte 4) They make chocolate covered ones in Norway, they’re insanely good.
[hla4e2s] (score 7, diepte 1) Fried beaks sounds like something out of Monty Python.
[hlc5m8i] (score 7, diepte 3) If your non Chinese date isn't spitting out bones with you it's time for the check
[hla6jox] (score 7, diepte 1) Came to say this!
[hlcaf2d] (score 7, diepte 0) 3 chicken feet = 1 chicken yard
[hlash1n] (score 6, diepte 4) They switched machines or something, they're too damn flat and not round enough to put on fingers anymore
[hl9y66x] (score 6, diepte 0) Feet stock for the feet gods
[hla51h7] (score 6, diepte 0) FEET CUBE MEAT CUBE FEET CUBE MEAT CUBE
[hlc9il3] (score 5, diepte 3) You sure about that bud?
[hld9cy8] (score 5, diepte 5) i’ve been on a cruise for 5 days with no social media activity - it’s 4 am and i’m coming down off of acid while the ship is getting ready to dock in miami and this is one of the first comments i see after opening reddit. i have a mix of emotions and thoughts about your comment that i won’t bother typing out, but just know that you gave me a little comfort and laugh in a trying time in my life

also sorry for any grammar errors, i’m still kind of tripping
[hlb2033] (score 5, diepte 2) Does it taste like feet? 🤪
[hlbyy5d] (score 5, diepte 1) One square foot
[hla7u65] (score 5, diepte 0) PRAISE THE CUBE!
[hlc9kuc] (score 4, diepte 3) Close enough
[hlak31f] (score 4, diepte 2) My fave too
[hlbkhpd] (score 4, diepte 3) I once put one in a Tiffany & Co jewelry box and gave it my my fiancé for her birthday. She had a good laugh.
[hla7c5f] (score 4, diepte 1) Fr
[hlbj1ir] (score 4, diepte 1) Cubic feet
[hla1zmw] (score 4, diepte 0) Feet cube
[hla7xrg] (score 4, diepte 0) Dim sum?
[hl9ut5q] (score 3, diepte 0) Pls god make it stahp
[hlbzhzk] (score 3, diepte 2) I literally didn't know what sub this was at first. Figured it was one of the fetish subs.
[hlbs3zg] (score 3, diepte 1) Feet³
[hlc81ov] (score 3, diepte 5) They still trumpet the finger snack "feature" on the bag. Or actually, they Bugle it. Ow. Ok, I'm done. Gee.
[hlbas43] (score 3, diepte 2) I absolutely love chicken feet. And now I want some.
[hlakwzt] (score 3, diepte 1) We got them grilled over charcoal in the Phillipines.  They were delish!
[hlbdfp1] (score 3, diepte 2) China is also the #1 importer if chicken feet. They are everywhere, including, most importantly the retail kiosks at train stops.
[hla21hi] (score 3, diepte 0) How you all making soup with feet? Just boil it with veg scraps for ~6 hrs or what?
[hla2k4o] (score 3, diepte 0) Do chicken feet *not* come in giant frozen  blocks somewhere?
[hla47ur] (score 3, diepte 0) Im making this a new standard measurement. Cubic ft now means cubic feet. Example: "Yeah mate, thats about shinty six cubic feet. No , not ft...Feet.
[hlaj2bu] (score 3, diepte 0) I love seeing these sold as "Chicken Paws" at the local mart.
[hlbf5v3] (score 3, diepte 1) Came here to say this! I laughed so hard the first time I saw them labeled chicken paws in my local Food Lion.
[hlakr5r] (score 3, diepte 0) Do you grill those, or just use them for stock, or ?
[hlaup1q] (score 3, diepte 0) good stock stuff
[hlaw73h] (score 3, diepte 0) We saw Alton Brown at a show in SLO years ago and he told this story, C&P [from here](https://archive.naplesnews.com/entertainment/theater/review-alton-brown-cooks-up-humor-pizza-and-fun-at-show-ep-919487007-334701721.html/) 

>	Brown got down to business, discussing his main points on a list he calls “A Few Things I’m Pretty Sure I’m Pretty Sure About Food.” At the top of it was: Chickens Don’t Have Fingers.

>	He told the story of how his daughter once wanted him to cook chicken fingers for a sleepover at their house.

>	“My own daughter was a user,” he said, as the audience laughed.

>	Brown complied; he bought real chicken feet, prepared them, spray-painted an old charcoal grill Rust-Oleum gold, and wheeled it up to his daughter and her friends. He then lifted the lid.

>	“It was almost like a harmony of horror,” he said.

This is a fabulous opportunity for you, OP.
[hlbfqb6] (score 3, diepte 0) Chicken paws.
[hlbp02m] (score 3, diepte 0) Last night I had a dream that I was cooking chicken feet, which is crazy because I've never touched, cooked, or eaten chicken feet in my life.
[hlchr3l] (score 3, diepte 1) Good bot.
(78 reacties met lagere score weggelaten)

=== THREAD cznhv6 ===
SUBREDDIT: r/ems
DATUM: 2019-09-04  SCORE: 403  REACTIES: 150
TITEL: Free Insoles
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[eyzephl] (score 168, diepte 0 OP) This was shared to me by a coworker. Took their survey to pick out soles and then went through the verification process. The whole thing took me 5 minutes and they should be here by the end of the week. I did however use military verification (faster probably). 

https://www.protalus.com/pages/first-responder

Proof? https://imgur.com/a/FHFT8dQ

Edit: Whoever downvoted this, fuck you and I hope you get severe plantar fasciitis "You fuck".

Edit 2: Thanks u/harron17 for popping my silver cherry.
[eyzgyqp] (score 50, diepte 0) Cheers.  Just ordered my pair.  I did the first responder verification by uploading a picture of my ID and state card and it verified in about 2 minutes.
[eyzpchp] (score 18, diepte 1) We got the same insoles!  I used my EMS ID and I’d say it took just about as long.
[eyzs5o8] (score 15, diepte 0) Nice, Thanks for the info. 

'Verifypass' took my state card without issue.
[eyzh9qd] (score 13, diepte 1 OP) Thanks for the info. Figured it may take a longer as I would assume they have to manually view the pictures. Military side it just connects to a database quick.
[ez0pkig] (score 12, diepte 2 OP) I found it funny, just had a VA appt. Today for my flat feet and plantar fasciitis and found out about this in the waiting room.
[eyzufrk] (score 11, diepte 1) (Upvoted for edit commentary) haha
[eyzu3y1] (score 10, diepte 0) Yeah just got mine sent out!
[ez1gsy9] (score 10, diepte 4) Idk man. They do this because they hold us in such a high regard (although we definitely don't deserve it). I feel like the least we can do is be honest
[ez0ypr4] (score 10, diepte 1 OP) Pass the word along, but dont tell the firefighters.
[eyzvrxo] (score 9, diepte 0) Confirmed and ordered! Verification took about 30 seconds.
[eyzh808] (score 8, diepte 1) Couldnt find it onthe canadian site :(
[ez0fhsl] (score 8, diepte 0) I was just gonna buy some too. This is so nice of them. They got a customer for life if these things are any good
[ez1gsvo] (score 8, diepte 1 OP) Only the EMTs, not the FFs.
[ez0pgmp] (score 6, diepte 2 OP) Still want to know who downvoted it.
[ez0zhqu] (score 6, diepte 1 OP) Good to hear. I know ID.me takes a minute
[ez08nii] (score 6, diepte 0) Wow it took like 10 seconds. Just used my state ID. Thanks so much!
[ez0yu1q] (score 6, diepte 1 OP) I'm actually rocking a walmart pair. They've held up decently for $20. Was only going to use them until I could order a new pair but here I am.
[ez0rnn3] (score 6, diepte 0) That was insanely easy. No excuse not to take advantage of this.
[ez1fyu4] (score 6, diepte 1 OP) And I think we are more inclined to give them our monies too for doing shit like this.
[ez1h151] (score 6, diepte 1 OP) My ROSC count says otherwise.
[eyzywd9] (score 5, diepte 0) Nice , thanks
[ez0368h] (score 5, diepte 0) Thanks!!!! Just ordered mine!
[ez05m3g] (score 5, diepte 0) Nice, thanks for the info.  Anyone used these ones before?  How are they?
[ez1hddm] (score 5, diepte 3 OP) I wouldnt admit that. Move upstate I know of a good place hiring. You like QRVs?
[ez1h434] (score 5, diepte 1 OP) Fuck the police, I start on my left.
[ez19qzy] (score 5, diepte 0) Thats a great marketing idea. First hit is always free :-) 

But seriously , if even 10% of the people that try em like em , they will make back what this cost they easy.
[ez0zfub] (score 4, diepte 1 OP) That was quick. I dont even think mine shipped yet.
[ez0zd02] (score 4, diepte 1 OP) Not bad!
[ez0zax7] (score 4, diepte 1 OP) I would hope if a bunch of people buy them (judging by free pairs available) for $80 they must be decent.
[ez3bydw] (score 4, diepte 2) A lot of people buy Dr Schols and those are the shittiest insoles on the market. But I hope these are good insoles
[ez07kki] (score 4, diepte 0) Just ordered a pair, submitted my nremt and dl.
[ez0z6b4] (score 4, diepte 1 OP) That's quick!
[ez09de8] (score 4, diepte 0) Awesome! Submitted a photo of my NREMT card, took a few seconds to approve, and overall a few minutes max to submit an order! Thanks!!
[ez0o32v] (score 4, diepte 0) Just ordered mine, can't wait to try them out my boots fucking suck
[ez1gp0v] (score 4, diepte 3 OP) You better be careful. If CJ was still allowed in these neck of the woods he may take that a certain way.
[ez1gywd] (score 4, diepte 1 OP) I'll always give you the tip.
[ez1k909] (score 3, diepte 2) I'll send it to Canada for you if you want
[ez1ndr4] (score 3, diepte 3) Yeah? I could wire you some money for the shipping.

Ill get a vpn and look into ordering some, ill get back to u if I follow through. In and out of of the back country right now.
[ez0tjsj] (score 3, diepte 1) Don't wish that evil on no one. I have plantar fasciitis, and it's a bitch.
[ez7otyn] (score 3, diepte 2 OP) I was in the same boat!
[ez0z27f] (score 3, diepte 1 OP) You needed a DL too?
[ez1a5m0] (score 3, diepte 2) No I just did a digital of my NREMT and it worked
[ez0bdqm] (score 3, diepte 0) Thank you for sharing!
[ez0poxb] (score 3, diepte 1 OP) Have you used this brand before?
[ez14r3j] (score 3, diepte 2) *wink*
[ez16s3o] (score 3, diepte 0) I just ordered mine! Thank you! I'll pass this along to coworkers
[ez1gey5] (score 3, diepte 2) https://m.imgur.com/gallery/hhHZD
[ezumujr] (score 3, diepte 0) Was able to redeem this on 9/10/19; however, they did charge me $4 for shipping (which is not bad), considering it's an $80 product for free.
[eyzm28o] (score 2, diepte 2 OP) Write them. Or ship to the US somewhere then have it sent to you.
[ez46nil] (score 2, diepte 1) Thanks for this, I’ve been hurting for a couple months but have been putting off spending a hundred bucks on new inserts. Have my upvote!
[ez0zbxs] (score 2, diepte 1 OP) Glad to hear.
[ez3cok8] (score 2, diepte 3 OP) I think the last time I used those were the ones from boot camp.
[ez06swo] (score 2, diepte 0) Wow, this is nice. Thanks OP
[ez0yxx9] (score 2, diepte 1 OP) Glad it was the same experience.
[ez0g4eo] (score 2, diepte 0) Appreciate the heads up! Just put in my order and it'll be here in a few business days :D
[ez0vjin] (score 2, diepte 0) Done. Verification took less than 10 seconds. Thanks OP!
[ez12owg] (score 2, diepte 0) Got mine no problem, verified in two hours!
Didn’t pay anything, ships in 3-5 days.
https://i.imgur.com/jI5B1xA.jpg
[ez1gxvd] (score 2, diepte 1 OP) Sounds like yours took the longest to verify
[ez19bc0] (score 2, diepte 0) They just want you to start off on the right foot ;)
[ez1ev0y] (score 2, diepte 0) Thank you for the heads up OP!
[ez1fehm] (score 2, diepte 1 OP) No problem!
[ez2gkyu] (score 2, diepte 1 OP) I gotchyu boo
[ez2ryzr] (score 2, diepte 1 OP) Wow. They're going quick. Was over a thousand left when I posted originally.
[ez8yjlm] (score 2, diepte 1 OP) My Pts usually call me a devil, this is new!
[ezb5y9u] (score 2, diepte 1 OP) Glad you caught it while some were left! They keep running out daily, but more people buy which puts more in the stock for us!
[ezv19rb] (score 2, diepte 2) Negative, I'm in CA. I was charged $4 for "First Responder Expedited Shipping" and didn't have any other options for shipping. I'm cool with it, $4 isn't bad, but it wasn't entirely free for me for some reason.
[f1m3hba] (score 2, diepte 1 OP) Some else mentioned noise, I guess its boot dependent. Mine have been fine.
[ez1h4cl] (score 1, diepte 2) I didn’t either but I checked my spam/junk and it came out
[ez0zecp] (score 1, diepte 1 OP) Sweet, you're welcome.
[ez0z7t1] (score 1, diepte 1 OP) Not a problem.
[ez1fkcx] (score 1, diepte 3 OP) Ah ok
[ez55v9t] (score 1, diepte 2) I did my NR and put my DL with it , just in case
[ez7p0m4] (score 1, diepte 3 OP) Fair enough!
[ez0yoab] (score 1, diepte 1 OP) Not a problem. See? I'm not always a salty fuck.
[ez1hame] (score 1, diepte 5 OP) Yeah, that's why I havent done it. Totally didnt cross my mind either.
[ez0ywkd] (score 1, diepte 1 OP) Hopefully theyll be here before next week for me. No idea where they ship from though.
[ez0yqj3] (score 1, diepte 1 OP) That's quick.
[ez0zd9a] (score 1, diepte 0) Done! On the way!
[ez0zq43] (score 1, diepte 1 OP) Schweet
(72 reacties met lagere score weggelaten)

