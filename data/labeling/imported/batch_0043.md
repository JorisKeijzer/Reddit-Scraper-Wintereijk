# Label-batch batch_0043

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
Schrijf het resultaat naar `batch_0043.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(2 threads: 1jlt4xc, 582t6n).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1jlt4xc ===
SUBREDDIT: r/BuyItForLife
DATUM: 2025-03-28  SCORE: 86  REACTIES: 133
TITEL: Best shoes for walking/standing all day?
POST (source_id=post):
Now I'm currently searching for the **best shoes for walking/standing all day** that offer great comfort, support, and durability. I want something with good cushioning, arch support, and breathability to keep my feet comfortable throughout the day.

I've come across several options during my research, but I’d love to hear about your personal experiences and recommendations. Some options I’ve been considering include:

* **Hoka One One Bondi 8**
* **Brooks Ghost 15**
* **ASICS Gel-Nimbus 25**
* **New Balance 990v6**
* **Skechers Arch Fit**
* **Nike ZoomX Invincible Run 3**
* **On Cloud 5**

If you have any personal favorites or additional insights on these shoes or others that might be better for comfort, arch support, or all-day wear, please share!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mk68t29] (score 71, diepte 0) Medical professional on my feet for 10 hour shifts, plus I do bootcamp workouts and neighborhood walking-- by far my favorite shoe is the Brooks Adrenaline GTS. I had a local running shop watch me walk and jog (I am *not* a runner) and they recommended this shoe-- I've stuck with it for years with zero complaints aside from how I do burn through them in 6-9 months.
[mk64zt8] (score 64, diepte 0) switching shoes halfway through your day is the best way to alleviate any pain / soreness. 

fresh socks feels heavenly too.
[mk66ld8] (score 64, diepte 0) Very few redditors walk/stand all day lmao
[mk66zr3] (score 32, diepte 0) Shoes are subjective, find a running footwear store and try them on. 

For me the NB 990 v6 is excellent. Plus I got the MiUSA version to boot. I don’t particularly like supporting overseas sweat shops which is where the rest of these brands are made
[mk7l639] (score 23, diepte 1) OP if you have a Roadrunner store by you, I highly recommend dropping in for an appointment. 

They’ll measure your feet, how you stand, and walk/run then give you some recommendations on shoes along with custom insoles.  

For me, the custom insoles and the brooks that I bought have significantly helped my walking and running.
[mk64ohw] (score 21, diepte 0) Most nurses I know wear either on cloud or hoka. I think you should find a nurse group, or another profession that is on their feet all day, and ask them.
[mk6gt2o] (score 16, diepte 0) I own a shoe store and Hoka is by far our best selling brand. The Bondi is their max cushion shoe. They just updated it to the Bondi 9 and it’s selling really well. Also check out the Hoka Gaviota. It’s their max stability shoe with a boxer toe box. Great fitting shoe!
[mk7velx] (score 15, diepte 2) This is where custom insoles make a big diffrrence. They aren't cheap, but if you find yourself in a situation where you've hit max out of pocket for your medical, you can generally get them fully covered.
[mk6akm0] (score 13, diepte 0) Go to a running store to get fitted in the right shoe.

I'm a dog walker. I thought I was using decent shoes (Nike running, probably $100ish range) but was starting to have foot pain. I went to a running store to get fitted and my new shoes cured my pain in two days. 

Trust the experts. Spend some money.
[mk6djxx] (score 11, diepte 0) I bought a pair of Vivo Barefoot Primus Lite Knit and it’s been a game changer on my whole body. Knees and back don’t hurt despite hurting for like 5 years straight. My mom who is over 70 also says her pain went away. It’s amazing, when you allow the body to build muscle in your feet, it allows your feet to actually engage. This takes stress off your other muscles, tendons, and joints. 

I would say that when you’re first wearing them, alternate back and forth between those and a normal cushioned pair of shoes for the first few months because your feet and calves will be exhausted!
[mk6r0uw] (score 9, diepte 1) Dansko clogs are also popular with nurses and restaurant workers.
[mk6lv1k] (score 9, diepte 1) Fleet Feet stores (well, some of them) can scan your feet and help find shoes that fit you best.
[mk6kapf] (score 8, diepte 0) Cushion and durability are almost always mutually exclusive. The heavy foam padding in running shoes is just gonna wear down over time. I'm a nurse, and some colleagues would wear hard clog-type shoes (idk how) which last much longer. I found it best to just rotate between 2 Hokas or Brooks and replace them when the foam is down to nothing or holes develop in the mesh uppers, usually 1 year. Not quite BIFL.
[mk8x2mv] (score 8, diepte 0) Check out altra.
[mk8g699] (score 7, diepte 4) I realize I said insole, but I meant custom orthotic (which replaces the insoles).

Also, a good shoe is important, but it most certainly isn't custom.
[mk6dt8n] (score 7, diepte 0) I'm a chef and I'm on my feet all day, I picked up a pair of blundstones about 6 months ago and I'm in love. Highly recommend shoe insoles from super feet!
[mk6lz7s] (score 6, diepte 1) Yeah. I see those two and Brooks.
[mk68z0k] (score 6, diepte 0) I agree with going to a local shoe store and getting them to analyze your feet and gait.  They'll recommend shoes based on your personal feet situation.

I overpronate and have good luck with Asics Gel Kayano.  But if you don't overpronate, then you don't need a stability shoe like the Kayano.
[mk69w1g] (score 6, diepte 0) ASICS gel nimbus and Brooks ghost are both fantastic shoes - two of my favorites!
[mk6kbmn] (score 6, diepte 0) I recently found xero shoes. They’re barefoot (wide toe box, zero drop) and personally I found them enjoyable for my 12 hour hospital shifts. 

They’re not plush, so you feel your feet all day. But they don’t hurt? It’s a weird experience. 

Anyways, since I’ve been wearing them my hip and back pain has reduced a lot. But it’s definitely a unique taste
[mk6b53p] (score 5, diepte 0) As a teacher I stand/walk the entire day and often shoes with better firm structure work better for me like doc martens, birkenstocks, and dansko clogs. these are also more durable as the foam in sneakers compresses and wears down quickly for me.
[mk6oij1] (score 5, diepte 0) ASICS gel nimbus 26
[mk7t089] (score 4, diepte 1) I’ve been wearing New Balance for years, and my most recent pair of shoes I phased out recently. Went with two pairs of 990v6 - one in gray and one in black. Solid shoe and super comfortable!
[mk6qo92] (score 4, diepte 0) I absolutely love my On Cloud 5, but no shoes are buy it for life.
[mk6p9pk] (score 3, diepte 1) Believe it or not, removing the insoles was the best thing I did. It isn’t as squishy, but the support is infinitely better
[mk802vp] (score 3, diepte 2) Agreed. Probably my favorite version of the 990’s
[mkaql38] (score 3, diepte 1) Brooks Adrenaline all the way! I have flat feet and they save my life.
[mk6aw45] (score 3, diepte 0) Honestly you need to alternate your shoes . I would always wear converse yea I know garbage for your feet. I bought 3 different shoes and alternate. I actually bought 2 pumas and one pair of sketchers and both are great. Pumas have some really good sales. Sketchers is pretty good too for comfort and walking. I probably walk 20,000 steps a day. Alternating helps the wear and tear. Also you can try doing orthotics as well to add a little umpth to your feet . I highly advise to get it professionally then just going to Walmart and buying them
[mkb8en8] (score 3, diepte 1) Same! I can feel everything in my feet but they don’t hurt. And even almost 2 years later it’s a weird feeling taking off my shoes at the end of the day. I wouldn’t call it relief because my feet have been feeling relief all day? Idk how to describe it.
[mka8v8w] (score 3, diepte 1) Oh my god, I had to scroll wayyyyyy too far for this. I’ve been through every conceivable brand in recent years, and the Altra Lone Peak is absolutely perfect. Rugged, breathable, wide toe box, zero drop, excellent cushioning. It’s like the Platonic ideal “dad shoe” for me. Cannot recommend this brand enough.
[mk64130] (score 2, diepte 0) i have my meindl shoes that i wear all day and for the past 4 years they have done a great job i hope to get another 2 years out of them
[mk70e6v] (score 2, diepte 2) Did this and wound up with shoes that finally fit correctly. Always thought I was a full size smaller than I should have been wearing.
[mk675ir] (score 2, diepte 0) Saucony Triumphs are my go-to for longer runs because they have really great cushioning from heel to toe and they can easily handle 500 outdoor running miles before they need replacing. 

I know you said walking/standing, but those shoes have the best cushioning and durability of any shoes I’ve ever used.

Also, Brooks makes a thick-soled version of their Ghosts, and their Glycerins are super comfy (all Brooks, really). 

And currently I’m using a new pair of Nike air zoom pegasus for runs up to 6-7 miles, and I think they’re great. That’s a shoe I stopped using years ago, but I recently bought a part of their latest version, and I’ve been very impressed. Light and springy with a comfy upper.
[mk67r20] (score 2, diepte 0) I'm an older runner who started using Hoka and will always wear them for running unless they make some crazy drastic change to them.  Cushion is key for me to keep running.
[mk68sr9] (score 2, diepte 0) Adidas ultraboost

Source: hospital nurse
[mk9m0t1] (score 2, diepte 1) Brooks Levitate line works great for me. They are comfortable and provide good cushioning.
[mkc86ps] (score 2, diepte 1) Brooks adrenaline is a stability shoe. If your foot has neutral pronation, a stability shoe can be uncomfortable. I have a neutral foot and like the Brooks glycerin.
[mkeou3c] (score 2, diepte 1) I'm wearing my Gel-Nimbus right now.  Got them for jogging, but I found out they're awesome for walking and standing all day too.
[mk69xfo] (score 2, diepte 0) I will only ever buy Merrell Moabs.  They completely eradicated my foot pain.
[mkcwl5g] (score 2, diepte 1) I love my nike pegasus for travel and walking a lot but if daily I'd do what above said. Feet are different for everyone.
[mk7fpt0] (score 2, diepte 1) that being said, alternating your shoes and support type can be beneficial so your foot doesn't get "lazy" and you don't develop a case of planter.
[mk6fayp] (score 2, diepte 0) Don’t know if your a boot guy, but Thorogoods are incredible for long days on your feet, there is a pretty rough break in period, 3-7 days depending how much you walk
[mk6gbh0] (score 2, diepte 0) I like the gel nimbus 25 but it’s better for standing than walking. Also gets kind of warm and I’ve found the arch support wears down relatively quick. Super comfy at first though, it’s like a marshmallow. 

I use the Brooks Glycerin 21 Stealth Fit now and it’s probably my favorite shoe ever, basically a more supportive/breathable version of the Nimbus 25. All the cushion but it feels firm enough to bounce back and keep its shape over time.
[mkdzptw] (score 2, diepte 2) Oh ya, well the podiatrist store called and said they were all outta you!
[mk71wow] (score 2, diepte 1) I get this. My “barefoot” shoes completely changed my relationship with the gym. I went from 2 debilitating back-injury weeks per year to none
[mk8joev] (score 2, diepte 1) OP, heed this. You may be quite wrong in what you think may be best. However, beware - going to a barefoot shoe will initially be tough - your legs will ache in muscles you never knew existed. It will take some time for your feet and legs to adjust. Could be a couple of months. After that you will never go back to those horrible cushioned, foot squeezing, ankle bending monstrosities that were designed for aesthetics at the cost of maiming the human foot and leg.

Also, switch to toe socks from Injinji - this by itself will help a lot. Never again those toe constricting traditional socks.

If you want more info, go through some info at https://www.nwfootankle.com/patient-resources/. I am not affiliated in any way. It was something that I came across long ago and benefited tremendously from.
[mk6kq6z] (score 2, diepte 0) Blundstones get my vote.
[mk6kudy] (score 2, diepte 0) There's a very good reason that healthcare workers wear those hideous and expensive Dansko clogs.
[mk6lvsg] (score 2, diepte 0) Try them on before buying, and try to buy them with a return option in case you wear them for a day and they don't feel right, etc.

Also, none of these are buy it for life. If you are wearing them all day, every day, it's more like buy it for six months. Worth it to protect your feet, though.
[mk6rj93] (score 2, diepte 0) Don't know if you live near a roadrunner sport....but if you're able to go and get fitted for their insoles, they're like $100 but worth every penny. Used to work 12 hours a day in a kitchen and those insoles saved me man - worth the investment if you're on your feet that much.

  
That being said, I have the Asics Gel-Numbus 25 and their incredibly comfortable.
[mk6y8gn] (score 2, diepte 0) Hoka Bondis or Cliftons. I'm a hairstylist and I'm on my feet for at least eight hours a day. My muscle soreness and joint pain aren't nearly as bad when I'm in Hokas.
[mk6ypwl] (score 2, diepte 0) I build prosthetics, I see a million shoes and see how they wear and what people think about them (primarily old diabetics), I'm also on my feet 10 hours a day. I had a trusted patient who swore by New Balance 608. He said "I only have one foot and I want it to be comfortable", I took his words to heart and have been wearing 608's for 10 years. They are cushy, supportive, wide base for a good ground feel, durable. Love them! I  had a sprained ankle which inadvertently collapsed my arch, I had to add an arch support from power step (I buy from Amazon), I tried the 30 dollar ones and they lasted a couple of months, then I got the 80 dollar ones and I've had them for years, I rotate the old ones into other shoes.

Highly recommend the New Balance 608, if you need additional support, try the insoles.
[mk8ewo0] (score 2, diepte 0) can not believe it nobody mentioned birkenstock? search birkenstock healthcare shoes
[mkc5h5t] (score 2, diepte 0) To be honest... Support > over cushion. I had a job in a warehouse. It was an administrative role, but required a bit of walking around the warehouse. Around 10k steps/day.

When I first started I wore my brooks and developed plantar fascitis after a few weeks. I switched to my Lems Boulder boot which is a lightweight barefoot foot minimal boot. Doesn't have much cushion or foam. I did replace the insole with a Dr shols gel insole for impact and plantar fascitis and foot pain went away.

In short. I don't think foam runners are meant for being on your feet all day. They're comfortable, but I don't think they have the support.
[mk62uzw] (score 1, diepte 0) Hello /u/Defiant_Fix8658! Thank you for your submission! The AutoMod thought that your post might be a request type post and has changed the flair accordingly, but if this was wrong feel free to change it back!

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/BuyItForLife) if you have any questions or concerns.*
[mk62v1d] (score 1, diepte 0) Hello /u/Defiant_Fix8658! Thank you for your submission! just to inform you, you may also want to try posting in /r/boots which is a smaller subreddit but might be or specialized for your request

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/BuyItForLife) if you have any questions or concerns.*
[mk63ugv] (score 1, diepte 0) I have pairs of Nikes top running shoes, the alpha fly and vapor fly. Not sure about the BIFL durability, and the price tag is high but they are damn comfy and work well for that
[mk7fvz9] (score 1, diepte 1) Love my Sauconys. Nice wide cushiony on the bottom and form fitting and comfy on top. I’m 5ft 4 and weigh about 108 and have had them over a year and haven’t felt them flattening yet.
[mk68f5o] (score 1, diepte 0) I love brooks glycerine and that’s what I always buy.  Like others have said you should find a good store that you can try on multiple pairs to see what feels good.  I usually do this and the brooks always feel the best for me.   
My wife swears by Hokas or NB.
[mkagsu1] (score 1, diepte 1) I’m on my feet a ton. 6 month replacement is plenty long…
[mk6aamg] (score 1, diepte 0) Hoka
[mk6bdzd] (score 1, diepte 0) I’m a Hoka fan. My size 16 flat feet don’t do well with anything else.
[mk6hj8p] (score 1, diepte 0) Go to one of the server or nurse subreddits! Those folks know shoes for being on your feet all day!
[mk7508p] (score 1, diepte 1) I agree. I went from 250$ Danner work boots with a 60$ insert, to barefoot boots and I no longer have foot pain walking on concrete and rocks all day. Slowly changing out all my shoes to be barefoot.
[mkdq212] (score 1, diepte 2) Every body is unique. Barefoot shoes can be damaging for arthritis (I have PsA). I’m also a teacher on my feet all day. I alternate Kurus and Hokas (with medical insole). Not perfect, but functional
[mk72631] (score 1, diepte 1) Danners are so comfy
[mk6pakf] (score 1, diepte 0) I’m a delivery driver who walks easily 15k steps a day. My favorite shoes are the asics gel cumulus 25. On my second pair they usually last me a year before I have to get a new pair
[mk6phe8] (score 1, diepte 0) Vivobarefoots
[mk6qttt] (score 1, diepte 0) Everybody in production which include 12-15 hours of walking and standing on set wear Hokas.
[mk6tyz6] (score 1, diepte 0) I’ve found the sketchers slip ins to be super comfy and I can pretty much be on my feet all day with minimal pain. Specifically these sneakers in the link, though I’m sure any of the ones with memory foam would be good! 

https://www.skechers.com/skechers-slip-ins-glide-step-altus/150510W_WMLT.html?campaigntype=shopping&src=paidmedia&gclsrc=aw.ds&gad_source=1&gbraid=0AAAAAD-OiPJawtaZaVzqSly7vMlY3RfG-&gclid=Cj0KCQjwkZm_BhDrARIsAAEbX1EAAKpm62WjsTezWBa4G11xE3a8b317c-NZlhmTEMmAs33lCr6OrlUaAjbBEALw_wcB
[mk6u6hs] (score 1, diepte 0) Handmade boots or shoes from whites boots, nicks boots, Drew's etc. Leather shank for support, rebuildable, breathable, comfortable. It'll hurt your pocket but built to last.
[mk6wm4p] (score 1, diepte 0) New Balance Foam 880. In my 45 years these are by far the most comfortable things I’ve ever had on my feet.
[mk6y8vg] (score 1, diepte 0) If you want arch support, consider Dansko.  Very popular in the food service industry.  Hoka, Brooks and On Cloud also get my vote.  Try them all on and see which one fits your foot shape better.  Hoka fits me best due to the wider toe box.

Dansko will last longer than any of the sneaker brands.
[mk6y93q] (score 1, diepte 0) As a nurse, wearing Hoka’s is the way to go. Brooks are also very good.
[mk6ylhg] (score 1, diepte 0) I wear hoka, they help a lot with foot pain.

Sketchers caused a lot of my foot pain (plus my pregnancy) specifically the arch fit and I was replacing them every six months. Despite being close to a outlet store getting them with the BOGO deal still wasn't worth it.
[mk6yt53] (score 1, diepte 0) If you’re going to be on your feet/ walking on back to back days, I would recommend have two pairs of the same shoes.
[mk71khy] (score 1, diepte 0) I still swear by Danskos. I had a pair that lasted 10 years of 16k+ steps a day at an outdoor restaurant.
[mk72t9t] (score 1, diepte 0) Not really the best sub for this question as shoes are meant specifically not to last, theyre supposed to wear down. I just got NB x860 v14 and they’re incredible. Coming from a heavy guy who is on his feet *all* day. My other suggestion is to go to a running store like fleet feet and get fitted for shoes. Made a world of difference for me. They suggested the ghost 16, adrenaline, and x860v14. All were perfect fits I just decided on the x860v14 because I couldn’t afford all of them
(74 reacties met lagere score weggelaten)

=== THREAD 582t6n ===
SUBREDDIT: r/Frugal
DATUM: 2016-10-18  SCORE: 163  REACTIES: 132
TITEL: How do I keep my feet warm while wearing shoes?
POST (source_id=post):
I sleep in the school lounge area to save on rent and while I got warm jackets and pants my feet get cold during the night (no heat). I dont take off my shoes because im in a public area and need to be mobile. 

Any suggestions?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d8xafml] (score 150, diepte 0) 100% serious: maybe try /r/homeless
[d8x98bh] (score 147, diepte 0) Dude, I suggest you get a job and an apartment. Frugal =/= homeless.

Edit: To all the people telling me how hard they had it in college, I'm sorry. But I don't think how to survive as a homeless person is the type of content most of us come to this sub for. I'm looking for bargains on everyday things that I actually use, or ways to substitute those things for a lower cost and maybe more work on my part. Not how to keep warm while sqautting at university. This isn't /r/homeless or /r/vagabond (both useful subreddits for OP I'll wager)
[d8xbg8g] (score 89, diepte 2) It's an investment, sure... I was broke as a joke in grad school, but not homeless. I mean, if they're a student, there are solutions, even if they mean taking on a little bit more debt, it's worth it. 

Get a damn apartment, rent a room from a friend or find someone looking for a roommate. This isn't frugal, it's silly and unhealthy.
[d8x07gs] (score 87, diepte 0) When I used to have to stand on steel floors, I put down cardboard to keep my feet warm, I still do this with plywood in my garage woodshop in winter.

Buy wool socks (amazon/llbean/cabellas) The one thing I hate about Reddit is I cannot tell you who I am so I could give you a coupke of pair. This sucks.

Loosen your laces to improve foot freedom.
[d8x9gon] (score 65, diepte 1) "Saving money on rent"
[d8x771z] (score 44, diepte 0) You're homeless?

Edit: and how does a homeless guy have a girlfriend? Wtf?
[d8x66cn] (score 38, diepte 1) Definitely make sure that your laces are undone if you need to keep your shoes on. Even if they're tied loosely, they're impeding your circulation.
[d8x8oll] (score 37, diepte 0) I'd suggest getting a full-time job and doing school either part time or full time.

Your resume will thank you. 

Also, what do you eat?
[d8xow6q] (score 31, diepte 4) If you guys promote insanely dangerous behaviors to save money instead of just offering frugal advice I, for one, am out as hell.
[d8x7x59] (score 29, diepte 2) Seeing as though he doesn't have an address to avoid rent, you probably don't want to send a package to the school care of "the guy sleeping in the student lounge."
[d8xa2bk] (score 29, diepte 1) He/She may be a graduate student, with no/little funding and no time to do a job, but looking ahead to decent $$ after graduation. I've known people in similar situations who went on to have good jobs so they look at this difficult time as an investment.
[d8x0p4t] (score 26, diepte 0) wool socks. Also if position allows put pressure at the *bottom* of your shoes, this causes the body to increase circulation in your feet, increasing warm blood flow.
[d8xde08] (score 24, diepte 2) I've never heard of a grad program that didn't offer options for work arrangements to help with accommodations.

Most schools are killing for residential assistants -- which typically offers free room/board 

but hey, i guess that might not be everywhere
[d8x0uz6] (score 20, diepte 0) Multiple layers are better than a single large layer. Start with thin socks, then add a thicker pair of wool (merino if you can afford it). Then a small blanket or shawl over your feet will keep you toasty
[d8x6biv] (score 17, diepte 1) You can just ask for the address and mail it? I sent someone in another country a Christmas card across the world and we never exchanged names. Don't know if that works.
[d8xcz0q] (score 16, diepte 0) This is the level people go to in this sub to save money, how can I compete?
[d8xdcvf] (score 16, diepte 0) I didn't realize being willfully homeless counted as being frugal.
[d8xqo9c] (score 14, diepte 4) Homelessness is 100% not the same thing as being frugal. The entire goal in being frugal is to ensure you are not homeless.
[d8x5683] (score 11, diepte 0) Wool is a great answer, I use a lot of merino wool since it wicks moisture and it's smell repellant. If you have access to hot water a hot water bottle is what I use to heat myself 80% of the time. If you can boil the water even better, but you need a very good bottle to stand up to that.
[d8x831h] (score 10, diepte 3) From his post, he appears to be semi-homeless. I'm guessing he doesn't have much stuff.
[d8x6t5l] (score 9, diepte 0) One summer day, I found a full-length, genuine-wool cloak for sale for $10 at a yard sale. I purchased it and almost died of heat exhaustion carrying it home. (The house was about 3/4mi from mine and I had walked it.)

I took naps in my car when I was at university. The air was 20F, middle of winter, wind chills that were even colder. The stiff breeze would hit that cloak and just... stop. Now that's when I was walking. Obviously I didn't have stiff breezes in my car. Still, I spread that cloak over my feet and it kept me altogether warm.

I think probably the best advice I can give you for the feet themselves (I did kick off my shoes in my car) is to buy a Walmart pair of slippers that have 'hard' soles, the kind of slippers that could almost be mistaken for shoes, and wear them in the evening. I've used those slippers at home before, doing indoor and outdoor chores, and they really are nearly as serviceable as sneakers.

If you don't mind spending a little, as you *are* trying to be comfortable and you *are* saving hundreds of dollars per month, pay a good $50 or so and see if you can get genuine shearling. That'll keep your feet warm, and keeping your feet warm will keep the rest of your body warm.
[d8xsao3] (score 9, diepte 1) r/vandwellers might also have some ideas.
[d8x8ysk] (score 8, diepte 3) Student mailboxes are still a thing, right?
[d8x4wg9] (score 8, diepte 0) Wear fuzzy slippers with soles.  Get them a litter bigger than you normally would, and you can wear heavy socks with them.  If you need to get up and move, you can, just keep your regular shoes or boots where ever you keep the rest of your stuff.
[d8x4fz3] (score 7, diepte 1 OP) Nope. Its fine tho. Free water, gym, showers and a nice comfy sofa.
[d8xbou1] (score 7, diepte 2) And utilities...
[d8x8i84] (score 7, diepte 0) This is a bit odd, but it worked for me! I used to teach horse riding, which meant hours of standing around a outside, and in winter, that meant being pretty cold. I used to layer 2 pairs of socks, then a plastic carrier bag, and then put my boots on.

My feet were by no means pleasant at the end of the day, but they were toasty and warm!
[d8x9lm3] (score 7, diepte 0) Most likely, it's sweaty, damp feet that are causing the problem. the solution is definitely wool socks (and real wool, not just synthetic "thermal" socks).

And if you have somewhere to store things, I'd recommend having multiple pairs of shoes in rotation, to let sweaty shoes dry out. Something like three pairs, 12 hours on, 24 hours off should do it.
[d8x9t7u] (score 7, diepte 0) They make electric socks! Use those and charge them with the school's electricity? But also, loosen up laces and wear multiple socks
[d8xn3q8] (score 6, diepte 1) Yep. Wool socks. Get them at the camping store. 

Also, keep your shoes loose. Tight shoes restrict circulation.
[d8xqvtq] (score 6, diepte 0) This is ridiculous.
[d8x0i2o] (score 5, diepte 0) Electric heating pad? This is the time of year they do black friday sales on stuff like that... you probably have a friend who has one they never use too. I'd definitely take your shoes off though at night and let your feet breathe. Even the small amount of moisture that collects from keeping them in your shoes could be really contributing to them being cold during the evenings. Feet sweat even when they are cold. I agree with other posters on wool socks. You may try to get some slip-on shoes/sandals of some sort to quickly slide on when you need to move about. Also, sometimes late night caffeine or nicotine will constrict the blood vessels, which restricts blood flow in the smaller vessels like those in the feet.
[d8x7a56] (score 5, diepte 2) Where do you keep all your stuff?
[d8xrysh] (score 5, diepte 2) It isn't. They're very low power (a single C- or D- cell battery).

I've known a few motorcyclists and fishermen/hunters who wouldn't go outside in December without a fresh battery in their socks.
[d8xqv1y] (score 5, diepte 1) Yeah, I don't know if we need to unsubscribe and start a new sub or what. This is absolutely beyond the scope of frugality.
[d8x4a8k] (score 4, diepte 0) Got a friend or relative near by where you could crash?
[d8xbm4j] (score 4, diepte 1) I use an actual glass wine bottle and almost boiling water. Used to keep it tied up in a an old (clean!) sock but then my sister knit me a cover. I also agree on the wool socks.
[d8xoeen] (score 4, diepte 3) I'm a grad assistant and my university doesn't offer my position housing, unpaid or paid.
[d8xp2h4] (score 4, diepte 3) Grad programs in the humanities rarely offer these kinds of arrangements and accommodations. Just saying.
[d8xazar] (score 4, diepte 1) Some education programs require you sign off that you will not work or have even a part time job. They can often lead to lucrative jobs afterwards.
[d8xsgc8] (score 4, diepte 1) Complaining that a homeless person isn't generating your favorite kind of internet content isn't a *great* look. 

Just hide the post and move on with your life.
[d8yxlkp] (score 4, diepte 2) Sorry I forgot this sub was about absurd living situations, not saving a few bucks on groceries.
[d8xmj79] (score 4, diepte 2) I mean, electric blankets have been around for decades. This is the same thing but just portable.
[d8xr1zk] (score 4, diepte 2) /r/MildlyFrugal
[d8wzh2u] (score 3, diepte 0) Heat Holder socks.
[d8x6ewh] (score 3, diepte 0) Socks
[d8xc9qx] (score 3, diepte 1) This. I have a pair of LL Bean shearling-lined slippers that have rubber soles that are great for when I just need to take the trash or recycling out or whatever. They are also super warm
[d8zm0s0] (score 3, diepte 6) It's dangerous because it's extremely unstable. It's very likely that security will eventually catch on and make him leave. Then he's on the streets or in a shelter. If he has no other option that is one thing but this isn't a smart way to save money if he has another option.
[d8xmwpr] (score 3, diepte 2) That means he could be ok taking loans. 

The real college answer though is just figure out where the ac is controlled at and turn on the heat.
[d8xok3f] (score 3, diepte 1) There are many homeless students. More than you might imagine. I would not have been able to afford my university degree if I hadn't lived in my car for part of the time I was there. I was working more than full-time at a minimum wage job and taking a full course load.  Many of the months that I had an overpriced college-town apartment I was counting pennies to make it through the month.
[d8xrhgg] (score 3, diepte 3) Nice. Let's give it a shot.
[d8xw6iw] (score 3, diepte 0) I'm honestly surprised they let you sleep there consistently. Has anyone ever said anything about it?
[d8x0gvd] (score 2, diepte 1 OP) Haha thanks i appreciate the sentiment
[d8ygoez] (score 2, diepte 2) Yes, it really helps. Oh, and dry socks are a pleasure.....
[d8x9hud] (score 2, diepte 4) Sometimes I guess.  I only had a student mailbox at one out of three schools I went to, but I lived in the dorms at that one.
[d8x9tal] (score 2, diepte 3) Good call out. Sorry, didn't consider that.
[d90i9em] (score 2, diepte 4) Are you sure about that? If I worked at a hotel and received a package and there was no record of the recipient having stayed at the hotel I'd be concerned about the contents being malignant.
[d8xa1k6] (score 2, diepte 1) Send them an e-gift card to one of those stores, or ask which one is close by.
[d8yq51n] (score 2, diepte 1) This. I've learned this is really important since moving to Colorado.

In a nutshell, wearing multiple layers creates sort of a barrier, a pocket of warm air between each layer, and is warmer than a single, heavy layer. Not to mention, easier to adjust for weather changes.
[d8x616c] (score 2, diepte 0) try socks from a camping place, or ugg boots
[d8x6fs8] (score 2, diepte 0) Get some of those down booties with the outsole that lets you walk around.
[d8x7w3w] (score 2, diepte 0) Wool socks
[d8xudve] (score 2, diepte 5) "insanely dangerous" ? To sleep at a school lounge? Lets tend to the rampant cases of assault in school lounges then. Oh wait, they are actually really damn safe. OP isn't sleeping under a bridge, he is sleeping in a (probably video monitored) lounge, in a well lit and semi public space. Have you ever seen a university lounge?
[d8y48sb] (score 2, diepte 6) Yeah, I guess that happens with a comment post-scripted with "just saying" 

Seems like a lot of people wanted to refute what i said, despite the fact that "Yes" many grad programs have people/funds/grants set aside for students like OP. Of course it's not the case EVERYWHERE (that kind of goes without saying)
[d8yxn3g] (score 2, diepte 3) It's for everyone. Housed or homeless. Just because your housed doesn't give you carte blanche to exclude people who happen to be between apartments. Frugality is for every income level not just the middle class.
[d8yxu70] (score 2, diepte 5) Wow, I guess finding out that not everyone on the sub is middle class is really disturbing to you. Btw, I'm also housed and middle class. Not everyone is, though.
[d8yy6zw] (score 2, diepte 6) No, I simply go to specific places for specific content. There are other subreddits better suited for OP's situation, including /r/vagabond and /r/homeless, as well as others I imagine. Frugality is NOT the same thing as living on the street to save money. This post takes the cheap vs. frugal argument to its most absurd extreme, one I never thought I'd find on this once useful subreddit. Ask yourself while the top comments all direct OP elsewhere.
[d8x9d5z] (score 2, diepte 0) Loose shoes/slippers + thick socks or insulated slippers/boots.  Make sure they are not too tight especially if you add thick socks. If they are tight you will lose some circulation and your feet will be cold.  Sheep's skin slippers with the fur inside and the leather side out are hell of warm. You'll end up wanting to take them off after a bit in room temp.
[d8xnpk2] (score 2, diepte 0) Costco has big boxes of those hand warmer packs for $8. I think you get 40 pair?
[d8xqmqw] (score 2, diepte 1) Where would he store them?
[d8xq4j2] (score 2, diepte 0) Get a $9 nalgene bottle and a $25 sleeping bag. Fill the nalgene with super hot water. Put it by you feet and presto!
[d8xst6h] (score 2, diepte 0) Buy wool socks
[d8xwn4m] (score 2, diepte 0) Not from personal experience but I've seen a flatmate wear plastic bags over their socks. Don't know if that was to keep dry or stay warm but I'm sure that would be the cheapest way to insulate.
[d8ydizf] (score 2, diepte 1) good way to get trench foot doing that. You need natural materials, wool, cotton, that allow your feet to breathe but also stay warm.
[d8zc0br] (score 1, diepte 5) No friends or family with a spare couch to crash on? Or use their mailing address?
[d8xeb2e] (score 1, diepte 3) Could just send it to a nearby hotel with his name on it; it's not like they won't give you your package because you're not a guest.
[d8ygpet] (score 1, diepte 2) really? does reddit allow addresses. I would *SO* send this person some wool socks....
[d8yh42a] (score 1, diepte 3) Well, in my experience, yes? The person sent me their personal address in a private PM with their username, so for example /u/sweetlifeofawiseman, address, state, zip. The person really needed a Christmas card, they were going through a tough time, so I decided to send it.
[d900b0u] (score 1, diepte 4) Thanks, I never used PM....something new to try & to think about.
[d8ygs5h] (score 1, diepte 2) Honestly, I do not think reddit allows ID info - or I certainly would. Perhaps OP or a MOD would enlighten me...?
(46 reacties met lagere score weggelaten)

