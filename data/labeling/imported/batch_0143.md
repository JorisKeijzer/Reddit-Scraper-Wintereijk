# Label-batch batch_0143

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
Schrijf het resultaat naar `batch_0143.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1g31afj, gfxnik, 9ra7bn).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1g31afj ===
SUBREDDIT: r/ehlersdanlos
DATUM: 2024-10-13  SCORE: 40  REACTIES: 63
TITEL: Cute but supportive shoes!
POST (source_id=post):
Hey yall, I have cEDS and it pretty severely affects my ankles so I have to wear shoes with very strong arch support and/or enough room for my insoles, my orthopedist and phsical therapist in elementary school told me I'd have to do that for the rest of my life. I love alt fashion but I feel like all of my fits are ruined by the fact that I have to wear orthopedic sneakers all the time! Does anyone know of a brand that makes more fun shoes that I might actually be able to walk in? 😭

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lrsh62g] (score 16, diepte 0) i have hEDS, and it really affects my ankles too cause they’re extremely weak and roll easily. the best shoes i found to help me out, is the brooks levitate i wore them out the entire last year and had to get a new pair cause there was a literal hole in the shoes where the toes are. they’re expensive, but the best shoes i’ve ever found to help.
[lrsnbtz] (score 13, diepte 0) I swear by my Birkenstocks. They are the most comfortable shoes I own, and they are so cute! I have these in black and brown.
 https://dev.birkenstock.com/us/yara-waxy-leather/yara-core-oiledleather-0-eva-w_5326.html
[lrslmdm] (score 9, diepte 0) I have hypermobility (rheumatologist was too lazy to diagnose hEDS despite scoring a positive Beighton), along with metatarsalgia and permanent ankle damage from years of rolling and tweaking them in unsupportive shoes. I only wear Birkenstocks now. They make sandals, clogs, slip ons, athletic shoes and boots, are very supportive, and are considered fashionable now.
[lrsmokg] (score 8, diepte 1) My mom (where I get my hEDS) is a HUGE Brooks fan.
[lrswb9l] (score 8, diepte 0) I feel like it very much depends on what your specific needs are, as everyone who needs comfortable footwear may need something different. Personally I did a foot analysis at Fleet Feet and wear Hokas with insoles. Hokas come in so many cool designs and colors that I stopped being so bummed about wearing sneakers all the time. They even have some with embroidered flowers.
[lrt9yzg] (score 7, diepte 0 OP) Thanks for all the replies already everyone ❤️ I am diligently checking out each and every recommendation 🫡
[lrthca9] (score 7, diepte 0) Altras. Wider toe box and good arch support.
[lrsrymk] (score 5, diepte 0) Another vote for Birkenstocks! I keep several pairs to alternate around and they last forever that way.
[lrti74r] (score 5, diepte 0) Personally I use Skechers for slip-ins and work shoes (non-slip), I specifically grab the Go-Walks and similar (they have more cushon). I also swear by these off-brand dupes of combat boots (unsure of brand at the moment)! They are comfy, have a zipper down the side for easy access, and can be tied tight enough to keep my ankle stable!! Also, Vasyli + Mcpoil and Vasyli Blue are amazing orthopedic shoe inserts for people who have arch issues, and are full length (there's a half length available)!
[lruivo0] (score 5, diepte 0) I know people who find doc martens really helpful for some ankle stability
[lrsk2nb] (score 4, diepte 1) I have hEDS and we suspect my dad has it too. He swears by Brooks.
[lrsk2c8] (score 4, diepte 0) Ziera shoes and Paul Green Shoes are my go to! They’re a bit more pricey, but I just pay to have the soles replaced every few years and it keeps them in great condition!
[lrskatb] (score 3, diepte 0) I wear some Vionic shoes. They're kinda expensive but worth it!
[lrt1jix] (score 3, diepte 1) Yes! I started wearing Birkenstocks after I had a nasty leg/foot injury that took two surgeries to fix after my ankle decided it didn’t want to ankle anymore one night, I googled best shoes for a broken foot and that’s what came up - I love them!  I have super high arches too and they’re great support.
[lrtfv57] (score 3, diepte 1) I loooove my Birkenstocks, they are worth every penny! They support my feet so well and the adjustable buckle is great because sometimes my feet swell.
[lrt6yab] (score 3, diepte 0) BLUNDSTONES! I live in them fall/winter/spring. They are spendy but I’ve had mine for 3-4 years and they look new.
[lrtg2a1] (score 3, diepte 0) hokas! i feel like these are most inline with your aesthetic preferences of the suggestions thus far and i love mine. 

have you tried doc martens? also might work with your style and have comfy soles and probably enough room for an insole if sized correctly.
[lrucl5q] (score 3, diepte 1) Another vote for Altra. Also Hoka, Topo, and On. All four were strongly recommended by my podiatrist (I have giant duck feet 🦆). Those all tend to have fun colors and stuff too. Personally, I'll sometimes opt for men's hokas because I like the colors offered there better. 

I THOUGHT I was doing good wearing Brooks but holy moly the wider toebox is SO freeing and they're all supportive.

I noticed that literally every physical therapist where I go wears Hoka except for a few Altras lol. 

Also recommend getting custom orthotics from a podiatrist that scans your foot instead of doing the thing where you step down into the gloop, if possible (they're able to create the orthotics based on your foot at rest, not splayed out, and are able to manipulate your hips, legs and foot into an ideal fully corrected position.) They're expensive but sometimes some insurances cover them.  

Alternatively, orthotics like the green ones from Superfeet are good quality and have good arch support.
[lrti7aa] (score 3, diepte 0) Have you checked out the hot chocolate brand? I like how those feel. For my insoles I typically order a half size up.
[lrtj8nd] (score 3, diepte 0) Birkenstock also makes insoles that you can put in sneakers. I usually have to size up so they fit. I have used these for 20 years because I have pronated ankles. I don’t like the leather ones or cork ones so much. https://theinsolestore.com/products/birkenstock-air-cushion-full-length-insoles?variant=40275358908613&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&utm_source=google&utm_medium=cpc&utm_campaign=G20702878222&gad_source=1&gbraid=0AAAAADltLhBPZkRsnrHyss_VUmwZmfQpq&gclid=CjwKCAjw3624BhBAEiwAkxgTOnCx1c2dqsrqMY1KxR-FYTpXT8p8xma9YTR3-ksSPx93-ueZILiR7hoCM_MQAvD_BwE
[lrsk6gk] (score 2, diepte 2) they’re really the best my ankles and feet feel so supportive
[lrshf2w] (score 2, diepte 0) I model for this company!! They are amazing and I wear them daily https://wacoshoecompany.com/collections/casual-shoes
[lrsr3z8] (score 2, diepte 0) I wear Solovairs (made in the factory Docs were made in when they were still good), sized up 1-2 sizes. They are a BITCH to break in, but they are pretty and the leather is SO firm so they give me good ankle suppprt and fit my insoles.
[lrtez5c] (score 2, diepte 0) I wear docs with inserts! I can wear compression socks with them too! My ankles need all the support they can get 🥲
[lrtjhzc] (score 2, diepte 0) I swear by Propet brand for the same insole problem!  With my orthotic insoles in along with having a naturally high midfoot (tall body top of foot) and needing a heel lift under my left orthotic shoes have been a major struggle.  Never found cute dress shoes that work.  But for casual shoes or sneakers, Propet has been my brand.  Specifically the shoe models that are described as "double depth".  They essentially have 2 extra insoles that you can remove to get more room for our bulky orthotics.
[lrx7shx] (score 2, diepte 1 OP) Glad to see all the doc replies! I own a pair but haven’t really worn them because of how awful they were the first couple times but if they break in that much I’ll definitely have to give them another try!!!
[lrsf0m5] (score 1, diepte 0) The OP flaired their post as "Questions". Please keep any and all comments to **personal experiences only**. If any factual information or advice is provided, please cite a **reputable website or study** linked within your post. No one in this sub is a *verified* medical professional, and as such, we do not allow medical advice to be given or asked for. For more information on this rule, [please visit this link](https://www.reddit.com/r/ehlersdanlos/wiki/index/rules/#wiki_r.2Fehlersdanlos_rules).

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/ehlersdanlos) if you have any questions or concerns.*
[lrsjqwa] (score 1, diepte 0) I love Taos Footwear boots!
[lrxrv86] (score 1, diepte 1) Seconding these!
[lrskn85] (score 1, diepte 0) Brooks Adrenaline are the most comfortable shoes I own
[lrww6y7] (score 1, diepte 1) I have switched from Birkenstocks to a brand called Cushionaire. They are basically identical to birks EXCEPT they include a nice layer of memory foam above the cork. It’s wayyy better on the balls of my feet. They are also like 1/3 the cost on sale.
[lsbiy87] (score 1, diepte 2) Awesome! I'll check them out! Thanks!
[lrsrsae] (score 1, diepte 0) Orthofeet come with removable arch support and multiple layers of customizable insoles, so easy to remove if also have custom made ones
[lrxzgc0] (score 1, diepte 1) I’ve been trying to get those flower ones since they came out but they haven’t restocked them in forever and the resellers like doubled the price😔 i haven’t been able to wear cute shoes since i was a kid I was so excited to actually like a pair of shoes I had
[lrt9ljl] (score 1, diepte 0) i have custom insoles and they fit in most sneakers/boots! i’ve been wearing them for years and they help so much, i like doc martens because they have ankle support. i was also told that i would have to wear orthotic shoes for the rest of my life while in elementary school, traumatizing 🙃
[lrtbzi9] (score 1, diepte 0) Hi-top blundstones! Impossible to roll ankles
[lrtdw44] (score 1, diepte 0) I love my Brooks! They are amazing. Ive been wearing them for 3-4 years and my feet feel amazing in them. Also, i just discovered Timberlands and they are super freaking comfortable. I’ve been walking around in a pair for a week and my feet don’t hurt in them either.
[lrvlye6] (score 1, diepte 1 OP) Exactly the type of thing I was looking for!!!
[lrwa5o0] (score 1, diepte 2) Oh good! Happy to share! They’re pretty cool people, too
[lrtl03q] (score 1, diepte 0) Allegria has the cutest shoes. Originally nurses shoes. Removable cork insoles in their regular shoes, beautiful printed leather. Athletic shoes too.
[lrtmalv] (score 1, diepte 0) Camper shoes have gotten surprisingly cool
[lrtp0ii] (score 1, diepte 0) I just found some really amazing shoes called “Dream Shoes” on Amazon. They are so comfortable and come in tons of styles. Really affordable too.
[lrtp4je] (score 1, diepte 0) I have an orthotic I love! I usually buy double-wide shoes on Zappos (because I have a wide toe box) and need space for a high arch with my orthotics in. You could talk to your PT about ordering them. 

https://bioorthotics.com/products
[lru25fo] (score 1, diepte 0) Aetrex is my favorite for clogs, if you’re considering that style. They’re THE most comfortable ones I’ve ever had.
[lrud4vh] (score 1, diepte 0) My mom lives in her Vionics. They have some really cute ones! I personally just wear my Hokas most of the time lol. My whole family wears their Hokas the majority of the time tbh, the wide last is just perfect for preventing ankle rolling.
[lrud9vn] (score 1, diepte 1) We also put Powerstep insoles in them, specifically the “Pinnacle” kind. Expensive but really really worth it for me. Wore my Hokas with these insoles in them to Hong Kong earlier this year walking a ton and they saved my entire body lol. My feet were surprisingly perfectly fine the entire time.
[lrugk3l] (score 1, diepte 0) I've been happy with Vionics. I have flats and boots from them. In the summer, I have a cute pair of leather chacos!
[lruls53] (score 1, diepte 0) I got some shoes from the brand Windsor Smith that are platform sneakers and omg from first wear, comfortable, amazing.

Although I put some random insoles in them I had been using but the shoes themselves are pretty comfortable without. I used to wear docs every day with the same insoles in them and tried wearing them again after the Windsor Smith shoes and I can't wear docs, ever again. 
I'm interested in buying another pair of their sneakers, but the above ankle height ones and maybe some boots. 

I hope this helps !
[lruly21] (score 1, diepte 1) The brand t.u.k also has cute shoes and a few pairs I have owned have been pretty comfortable, but most of their shoes are "vegan leather", aka plastic, so they start falling apart pretty fast unfortunately.
[lruqurg] (score 1, diepte 0) I wear runners or tradie boots. That's all that can contain my pancake feat!
[lruudf7] (score 1, diepte 0) My neuromuscular neurologist recommended Chaco’s. Love them. All of them.
[lruvojs] (score 1, diepte 0) I wear barefoot shoes
[lrv6pyj] (score 1, diepte 0) i either wear doc martens or crocs. my docs are great for walking long distances and stopping me from rolling my ankles and my crocs are my standing shoes
[lrv7x57] (score 1, diepte 0) I found a pair of Vionic trainers at TK Maxx which are designed to be supportive (flat feet & ankle support). They cost me £20, RRP was £90 and would now save up for replacements when I need them, they’re *that* good.
[lrvjovk] (score 1, diepte 0) The Brooks Glycerin 20s my husband gave me are comfortable, but my feet get hot in them and they have little to no grip on wet surfaces. 

I wish I still had my Nike Air shoes. They were a thrift store find and were the most supportive and all around comfy shoes. They kept their shape for years too!
[lrwlsop] (score 1, diepte 0) Fellow alt girlie I love converses hike star shoes! They are super comfy and offer good ankle support. They constantly come out with cute designs too. My favorite cute shoe brand though is hot chocolate shoes they make ballet flats big enough for my wide feet and an insole and they are so cute. Demonias also surprisingly can be comfortable I love there platform babydoll shoes specifically.
[lrwo5sq] (score 1, diepte 0) Hokas for sneakers. They’re nice and light and super supportive. I add an insole to mine. 

For dressier shoes Vionics all the way (recced by my PT). So comfy!
[lrwrflo] (score 1, diepte 0) So you need fashionable shoes that are secretly supportive. I would try Converse or Doc Martens. Converse helped keep my ankles stable all through high school while still looking cute, and I have worn them with inserts before. I haven't worn Doc Martens, but they have great ankle support and orthotics can fit in them. My husband needs custom orthotics and he wears those a lot.

Due to a hip injury I am now more comfortable in 1.5-2" heeled boots. My current favorites are ankle boots from a brand called Easy Street. They maintain my arch well enough and provide some ankle stability.

And my unfashionable choice - Brooks Adrenaline running shoes.
[lrx8j4w] (score 1, diepte 1 OP) Had the same walking issue when I was young with walking all wrong (I had to learn to walk heel to toe instead of toe to heel) and physical therapy made a huge difference, I’ve wanted to do it again but insurance has been a pain about it. If I can get in with someone I will definitely ask again about the insoles though! I don’t wear customs, I was recommended superfeet brand and that’s what I’ve been using forever but it sure would be nice to not need to.
[lrwxklq] (score 1, diepte 0) God this may be an unpopular opinion because of how hard they are to break in but I wear Doc Martens with insoles/good socks and they are my ride or die. I've had the same pair for the last 4 years and they are beaten to hell but they work SO WELL for me.
[lrxk1vp] (score 1, diepte 0) Harley Davidson riding boots 🙏 I have a pair of Harley boots (I’m alternative) and I can wear them to walk around for hours without rolling an ankle (not like I’d actually be capable of walking around for hours 99% of the time but still)
[lrxthln] (score 1, diepte 0) doc martens!
[lrz5n2k] (score 1, diepte 0) Fitflop! Their sneakers have such fantastic arch/insole support I use the high top court shoes for dance classes. They also make a variety of super cute flats, slides, loafers, and boots. They are marketed as a fashion brand, so they come out with new colorways and designs every season. If you don't want to spring for a brand-new pair, you can get secondhand and NWT/NWOT overstock on Poshmark and eBay for cheap.

=== THREAD gfxnik ===
SUBREDDIT: r/BarefootRunning
DATUM: 2020-05-08  SCORE: 44  REACTIES: 62
TITEL: "our feet can't deal with hard surfaces" 🤦
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[fpwa9n6] (score 46, diepte 0) TIL rocks didn't exist until we invented shoes.
[fpwlsw4] (score 33, diepte 0) "Wearing shoes will protect your feet against bacteria and fungi"  


Umm athlete's foot would disagree
[fpwapg3] (score 30, diepte 2) Our ancestors were experts at encouraging game to allow themselves to be hunted only across sandy beaches and golf courses.
[fpwryzr] (score 26, diepte 0) >Meanwhile, a study by the Institute for Aging Research of Hebrew SeniorLife also shows that walking around the house without shoes has contributed to falls among the elderly in general (via Science Direct)

I just checked the source they were referencing for this statement. This is a sentence from that source. 

> Of those who reported falling, more than 18 percent were barefoot when they fell. Nearly 27 percent were wearing slippers and 7 percent were wearing socks only. 

To me, this obviously indicates that more people wore **something** on their feet when falling, and only a bit more than 18% were barefoot. Those with slippers on even fell more, and this article tries to blame it on being barefoot. That's stupid.
[fpwdjyi] (score 24, diepte 0) Only one word -bollocks
[fpwakd2] (score 21, diepte 1) It was all moss and clover and manicured lawns.
[fpwdftn] (score 18, diepte 3) This is why we never hunted hooved creatures.  They would just go for the hard ground where we couldn't follow.  We and our soft-pawed brethren (bears, wolves, big cats) just mutually hunted each other while the herbivores laughed from rocky outcroppings.
[fpwdltq] (score 15, diepte 4) "Og mad because Og not eat deer meat because deer run on rock. Og one day develop air cushion technology and Og finally eat deer!"
[fpwdpdv] (score 15, diepte 1) No, human feet can run across bollocks just fine, too.
[fpwebe0] (score 14, diepte 0) Just got to do it incrementally, and most people going barefoot right now all the time will be asking too much of their feet and ability to support them before their body is ready.

I'd say most western feet are lacking so much function that there will be more foot issues than foot improvements after this pandemic.
[fpwdyyw] (score 12, diepte 0) Bare feet populated the whole world and crossed every known surface before shoes were even thought off
[fpwo2am] (score 12, diepte 0) This reads like an Onion article.

Podiatrist Phil Vasyli says if God wanted us to go around barefoot he wouldn't have allowed us to invent shoes.
[fpwueqh] (score 9, diepte 1) The thing I can't reconcile in these findings (because the actual study doesn't seem to be available for free anywhere) is that 48% of the study participants were wearing some form of footwear (other than socks/slippers) when they fell.

Also odd that they single out "barefoot" when, in fact, 48% were wearing shoes and 27% were wearing slippers, while 18% were in slippers.

There also seems to be the implication that these falls perhaps would have been less likely to occur, had they been wearing shoes, or that the falls would have resulted in less serious injury somehow.

I hate research sound bites.

EDIT: Found the study, going to read maybe later tonight or over the weekend.

[https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3250347/pdf/nihms335799.pdf?tool=pmcentrez](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3250347/pdf/nihms335799.pdf?tool=pmcentrez)

EDIT2: It was a very short read after all. I get where they're coming up with the conclusions - much lower percentage of people claiming barefoot as usual "footwear" at home vs. 18% of all falls documented while barefoot. The thing we still don't have any insight into is what the conditions were (getting into/out of the bath or shower, getting into/out of bed, trying to put on shoes, etc.) of the falls. Regardless, I don't see how you can draw from this - given the authors' own admission that this study is unique in it's research focus - that any of the conclusions are anything more than a first look requiring additional research with more advanced and varied factors to validate the findings.
[fpwj6mc] (score 7, diepte 1) My own hypothesis about that is fast walking may likely be another uniquely modern invention. If you're in the wild I can't think of why you'd choose to walk fast when it's likely more efficient to run slow. Therefore it's perfectly OK to walk and lead with the heel at 3mph but at 4-5mph you're certainly hitting that heel pretty hard.
[fpx12hk] (score 7, diepte 0) A doctor once told me this when I mentioned that my big toe hurt sometimes and that I often went barefoot during the same appointment. 🤦🏼‍♀️My toe had actually been stepped on by a horse (through a boot) several months back, but after hearing that I didn't like shoes, the doctor had made up their mind that my pain was because we aren't meant to be walking or running on hard surfaces like pavement without shoes. 🙄
[fpwivgh] (score 6, diepte 0) This is one of the stupidest things I have ever read.
[fpws4dj] (score 6, diepte 1 OP) Yeah cause socks and slippers are fucking slippery. Bare skin isn't.
[fpwrhli] (score 5, diepte 4 OP) Vegetarians should hop on board with the podiatrists and try to rewrite prehistory by saying we could have only lived on plants because we couldn't walk anywhere with our tenderfeet.
[fpwsmt0] (score 5, diepte 1) I've been contemplating buying vivobarefoot shoes for ages but wasn't sure about whether it was worth it.

At the start of all this I started doing my dog walks without shoes and did this for a couple if weeks.  Ought some vivos and dont know if I'll ever buy normal shoes again.

Have found it fairly easy but I've never worn shoes around the house.
[fpwic3s] (score 5, diepte 0) I have a perspective on this as a barefoot runner (on pavement). I can run barefoot a long long way. My feet are very tough. I wear vibrams a lot these days (because of winter and darkness), but it's all minimalist. 

My wife started C25K and I decided I'd go do it with her (additional to my running). She liked to walk the walking parts really fast, so I'd walk them really fast too. I gave myself policeman's heel! i was so used to heel/toe when I walked, I did it when I was going fast and I hurt myself on the cement. I normally would have metered my own pace and fox walked. It hurt like hell and it took a long time to heal up. That's the only time I can recall the surface mattering.
[fpyez3s] (score 5, diepte 3) No they don't, and that's the point. If you're elderly, where are you most likely to fall? Getting into or out of the shower. So you wear shoes all day except for fifteen minutes, so you're not accustomed to being barefoot, and for those fifteen minutes you're taking high steps with wet feet on wet slippery surfaces. So now "going barefoot is dangerous" when it should be "stepping in and out of the shower is dangerous". UGH! This bullshit is so frustrating.
[fpyg078] (score 4, diepte 2) We can't actually know this. The oldest records of shoes are only 10,000 years old. Examining bone growth suggests that shoes could go back 25,000 to 40,000 years. Humans spread through Eurasia 500,000 years ago.

Regardless, those shoes of old were supple sandals preventing cuts, not providing support.
[fpwzw4i] (score 4, diepte 2) I wholeheartedly agree with you here. Walking barefoot fast is a no go, but running is awesome. I've realized that when I am walking with other people in regular shoes when I am barefoot/minimalist, they tend to walk alot faster than me, and I have to strain myself to keep the pace up.
[fpwiibv] (score 4, diepte 0) Damn, what a load of crap.
[fpwss28] (score 4, diepte 3 OP) Yeah I know for a fact because I have wood stars that I've slipped down many times with socks or slippers on. And with bare skin I don't recall any times I've slipped down them.
[fpwydgm] (score 3, diepte 1) I just nose laughed at this trying not to spit out my lunch.  Thanks
[fpx9z0f] (score 3, diepte 1) Not even remotely true. We’ve been wearing some form of shoes for eons.
[fpwtubn] (score 3, diepte 2) Yep if your body was already used to it somewhat, so your body had the function to support your feet - more of that will just make you stronger.

But if you don't have that mechanical ability to properly support your feet, and you suddenly remove that support - your body will quickly go over capacity and that will cause a problem.

Congrats on the new shoes, welcome to the club, its the best!
[fpxbi6k] (score 3, diepte 2) I agree with you. I think the weird pace and forcing it into a walk was probably the issue.
[fpwiq9g] (score 3, diepte 0) "Going barefoot is dangerous because your feet will start to deform"

Really, some may experience discomfort because the feet will start to RE-form after all those hours, days, weeks, years locked in their little tiny fashionable prison cells. 

Unfortunately, these lifestyle sites, which cater to the fashionistas of the world, rarely - if ever - talk about the ills of high heels, rather spout about how to walk safely in high heels or treat your toesies after wearing heels all day. (I'm a dude, I just literally feel sad for people every time I see them in their several-inch high stillettos).
[fpwsjln] (score 3, diepte 2) Yup, since I've starting running barefoot and walking around barefoot, I've come to realize that in most circumstances bareskin provides the best grip. Sometimes shoes can help, but for me they have mostly helped me on rough terrain like gravel (because it hurts, I haven't been doing this for long).
[fpx0djd] (score 3, diepte 1) Hang on.  Did they have a control group of people who didn't fall, and report the footwear percentages for that group? Because for example if only 5% of all people were barefoot, but 18% of the fallen were barefoot, there might be something to it.  If they had no control, then... ugh.
[fpxelr0] (score 3, diepte 1 OP) Yeah I had to because it's so ridiculous
[fpx5dn3] (score 3, diepte 0) Wood and carpet ain’t concrete, author.
[fpxhe4v] (score 3, diepte 0) This is a prime example of articles published with no value at all, just written to make up their quota.  complete hogwash.
[fpx1pb0] (score 2, diepte 1) 😂 I'd love to see people use this reasoning to argue some more highly controversial topics. I bet it'd be pretty entertaining.
[fpxe5bv] (score 2, diepte 2) Studies like this also only "measure" the footwear the patient was wearing at the time of the fall. Their long-term foot health and how that has been affected by (presumably) wearing shoes all their life is not taken into account.

More interesting would be how likely someone who has always worn shoes is likely to fall when barefoot vs someone who has always gone barefoot. Such a study could be extended to fall rates when wearing shoes between the two groups. But it would be difficult to find enough data.
[fpybq7m] (score 2, diepte 2 OP) Getting in and out of the shower? People wear shoes in their private home showers?
[fpwscqq] (score 2, diepte 0) I just ran barefoot for the first time in 4 months. 6 miles on the sidewalk. No weird pain, no blisters. All the textures added to the enjoyability, even the small pieces of gravel I would occasionally step on. Its almost like a foot massage. Ever since I started running entirely in vibrams I have been injury free. Going without them was a real treat though. I'll probably do that once a week now.
[fpwu064] (score 2, diepte 0) I literally just saw this article! So glad you posted it here
[fpxiots] (score 2, diepte 1 OP) Wow. That's a good doctor. 😬
[fpy7rwg] (score 2, diepte 1) Go be a creep somewhere else. Women don't care what "impresses" you. This is a sub for barefoot running, not weirdos pushing their fetishes on everyone around them.
[fpxihk9] (score 2, diepte 1 OP) Yeah, it just blows me away though that people will read this and think it's credible.
[fpyrszr] (score 2, diepte 0) I sent the following to author Hope Ngo at staff@thelist.com:

This article "Why you shouldn't walk barefoot around the house" may be well intentioned, but it is ill informed.

I'm 63 and have been going barefoot around the house since I started taking martial arts classes 20 years ago. My feet are in much better shape today than they were back then. Their rehabilitation was fairly rapid, since we weren't allowed to wear shoes in class. Going barefoot developed muscles in my feet I never knew I had.

I used to have fairly flat arches, but as soon as I started going barefoot more often, my arches grew much stronger, and more arched. I also used to frequently have athlete's foot, and my feet and shoes were stinky most of the time. Going barefoot cured that, since my feet aren't trapped inside warm, moist shoes all the time. Contrary to the article's claim, barefoot guards against infection, since both bacteria and fungi must have moisture to thrive, and a bare foot is a dry foot.

Walking barefoot one learns to roll the foot from outside to inside to absorb the forces of contact with the ground. Contrary to the article, much of the ground people walked on long ago was compacted and hard. Ground on trails is typically like this, and is not soft like off trail areas. Even off trail is not guaranteed to be soft, it's often dry and hard. People often have need to clamber over rocks, which obviously are not soft.

Walking with a roll to the foot enhances control of feet muscles, so that one automatically adjusts the foot conformally as required. This softens the impact to knees, hips, and lower back, and protects them, unlike what was claimed in the story.

Walking without shoes helps when developing balance, because it activates so many more muscles than walking with shoes. Elderly people especially should do balance exercises every day.

The best way to protect your feet around the house is to go completely shoeless, to allow the skin of the feet access to air, to develop foot muscles, and to improve walking skills.

Sincerely,

mutatron
[fq0tn7s] (score 2, diepte 1 OP) That's awesome! Way to be proactive!
[fpzn9h0] (score 2, diepte 0) Obvious propaganda from Big Shoe!

Lockdown orders and 20 million unemployed are bound to impact sales of foot coffins and scarethotics. 

Put your feet upon the gears of the machine!
[fpxrvyr] (score 1, diepte 2) True. Shoes were 100% around when siberia was populated and the cross to north america (theorized) was made.

Also I'm pretty sure shoes were made before boats.
[fpwrarf] (score 1, diepte 0 OP) I can't believe there's a TV show where people watch other people get their fucked up feet fixed.
[fpwzm3j] (score 1, diepte 2) Cool that you found the full study. Can't read it right now, but I agree with your points. And do they account for other medical conditions? If not, that should be seriously considered.
[fpyfayo] (score 1, diepte 2) Yeah, those percents are useless without knowing the frequencies of each type at home. Another user dug around and found the study.     https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3250347/pdf/nihms335799.pdf?tool=pmcentrez

The bigger problem is that falls are most likely to occur at times like getting in or out of a bed or shower, when people are all barefoot. But it's the activity that's the risk.
[fpwsi19] (score 1, diepte 1 OP) I had a magical barefoot run last week. Can't wait for Saturday!
[fpwt733] (score 1, diepte 0) Very good -like all of the actors too !!
[fpxhra8] (score 1, diepte 2) So glad you did! It's satisfying to read everyone's comments
[fpxhzpb] (score 1, diepte 3 OP) Yeah I like how some people even looked up the quoted material to see what it's credibility is.
[fpxrgdu] (score 1, diepte 4) Me too! Something like that is not my forte so it's awesome to be able to learn from others
[fpxsmb4] (score 1, diepte 5 OP) Yep. Good discussion on this one for sure!!! Happy running!
[fr1v5hc] (score 1, diepte 2) ooc: what was the deleted comment saying?
[frf094x] (score 1, diepte 3) Just some foot fetish creep slobbering over the stock image and carrying on about what he wants to fap to.
[fq9n5vd] (score 1, diepte 0) >our feet were actually designed for walking on softer, natural surfaces (think sand and soil), not polished hard ones

I would require everyone making this kind of statement to take a 10 minutes barefoot walk in the nearby forest (or even better, the african savanna), just to experience how fluffy the terrain is. I guess mountains also didn't exist in the past, or were forgotten to be included in the design specs of the human feet.
[fq9t1lc] (score 1, diepte 0) Loved reading the part about diminishing the fat pad by going barefoot.  My feet are so suited to going unshod now. So strong, supple and capable. Like a tough leather pillow. And I’m over 50 too!

The whole article is a joke.
[fq9wrg5] (score 1, diepte 1 OP) Yeah that's great!!! Can't beat actual experience when it comes to these kinds of silly things.
[fpwg847] (score 0, diepte 1) [https://getyarn.io/yarn-clip/1a9a43b3-5c22-45d9-bb09-36a3e0c50a17](https://getyarn.io/yarn-clip/1a9a43b3-5c22-45d9-bb09-36a3e0c50a17)

=== THREAD 9ra7bn ===
SUBREDDIT: r/BarefootRunning
DATUM: 2018-10-25  SCORE: 63  REACTIES: 62
TITEL: Myth: barefoot runners are exceptional
POST (source_id=post):
Sure, it's flattering when someone says "that's hardcore!" or otherwise expresses their amazement when they see me running unshod. I can't deny it feeds the old ego.

However, it represents a pretty serious falsehood. Whenever I've had a longer conversation with someone who's expressed their amazement I find a lot of flawed assumptions about me and barefoot runners in general.

* "I suppose you can run barefoot if you have perfect form." It's the reverse: I had terrible, injury-causing, inefficient form until I went barefoot. I leveraged my super sensitive feet to learn better form.

* "You must have tough feet." It can take a long time for your feet to really develop thicker skin and fat pads. It's certainly easier over time because of that but you'll never get there just assuming bare feet is 100% or even mostly about "tough feet." The benefits come when you work with your feet as tough as they already are even after a lifetime in shoes. That encourages the exact types of form changes needed to run safer and more efficiently.

* "I suppose your feet get de-sensitized." The other side of the "tough feet" coin. My feet are still just as sensitive as they've always been. It still hurts to land on a rock wrong. Even before my skin and fat pads built up, though, they were tough enough to not get damaged. Over time I've come to view pain and discomfort as crucial data that helps my form. I just don't freak out about it like when I started. Used to be if I stepped on a sharp rock and it hurt I'd stop to inspect my foot absolutely sure I'd see a bloody mess only to find nothing.

* "You're really brave!" I was really *desperate*. I was ready to give up running entirely because I kept getting injured and went minimalist then barefoot because I heard it could help. The real shame is that's the norm and people don't go barefoot sooner in their running lives. Instead, it's a last-ditch effort by people who've reached the end of frustration over injury.

* "I couldn't do that because [foot/ankle issues here]." I used to stand on my bare feet supinated; on the outsides of my feet. I had a A or AA width. My toenails dug in to their neighboring toes. My feet were too narrow, my ankles too weak and arches too high to go barefoot. I "needed" support because of my foot problems. If everybody needed perfect feet to go barefoot *nobody* would go barefoot. It's just like the "perfect form" argument. You don't start with that you go barefoot to help improve it.

I appreciate the sentiment when people at races express their amazement at barefoot. I can't deny it inflates the old head a bit. But for anybody out there who's new to the sub or lurking just keep all this in mind: I'm a flawed, frail, desperate, uncoordinated runner. That's at the root of my running. Putting shoes on just makes all those things worse. Taking the shoes off helps me compensate for it all.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[e8fasf6] (score 14, diepte 1 OP) My recommendation is always the same: don't *cheat yourself* out of unshod. That's my only regret looking back: I went minimalist 6 years ago but didn't go full unshod until 3 years ago. My transition from padding and structure to minimalist took a lot longer because I was cheating myself out of barefoot training.

Expose those sensitive feet to the street with all its debris and rocks and you'll start learning all you need to know. Then get minimalist shoes that are comfortable and let your feet move and expect nothing more from shoes.
[e8fkilj] (score 13, diepte 0) Continuing to run after a painful sharp rock is an important mental milestone. 

Learning to flick off tiny rocks stuck to your pad without messing up your stride is also a challenge.
[e8fbb1i] (score 11, diepte 3 OP) That's the flawed recommendation I went by, too. I started with 4mm drop neutral shoes then 0mm drop padded shoes and then Merrell Trail Glove 2s over a 2 year span. Sure, I did it but along the way I got two pulled calf muscles, metatarsal extensor tendonitis, hip and lower back pain. All those problems persisted as I kept running in my TG2s and even in my Vapor Gloves. They finally started going away when I worked in unshod.

So, you can gradually work your way down with shoes, it could take years, and you risk injury. Or, you could start working in barefoot *now* which will transition you faster and more safely.

Where people get into trouble is the "tough feet" myth. You need to totally give in to how uncomfortable it feels and how that's forcing your body to move. Don't just grit your teeth through it and assume "I guess it's supposed to hurt." That's not going to teach you anything and will lead to injury. Imagine yourself on hot coals or jagged rocks or a trail made of Legos. Your whole body reacts to that and that's where the real lessons are.
[e8g677h] (score 10, diepte 1) And differentiating between the lingering sting of a pebble that has let go, and the persistent nagging of a pebble that has *not* let go.
[e8g0bsk] (score 7, diepte 5) One thing I recomend for transitioning is this. At the end of your normal run take your shoes and socks off and carry them. Then walk or run the last quarter or half mile home. I still do this myself. I run 3.5 miles out in my sandals and then go unshod 3.5 back.
[e8fk9qk] (score 7, diepte 0) Learning how to run barefoot/minimalist allowed me to be able to run at all. For years prior I was always getting shin splints after a mile and couldn't do anything else for weeks after.

I saw all manner of podiatrist, sports therapists, the works for gait analysis and expensive custom shoe inserts. One dude told me straight up "some people just aren't made to run."

On my own, after going barefoot/minimalist and working on my form (and building callus) I participated in my first 10K. Until that point, it was the longest distance I had ever run and it was completely pain-free.
[e8g3se6] (score 6, diepte 7 OP) I've never listened to music while running even when I had shoes.

Here's the thing: if you're listening to music just because it's enjoyable to do while you're also enjoying the run that's great. However, I know too many people who use music to "get through" a workout. They try to distract themselves from the drudgery and even the pain of the workout by blasting music. They try to "zone out" and just get in their miles.

That leads to burnout, injury and frustration every time. The run itself isn't seen as enjoyable. It's an ordeal people put themselves through because they want to get in shape or check off "marathon" on their bucket list but it's not about the run itself.

Hand-in-hand with barefoot running is just the pure enjoyment of running itself. No music, no zoning out, no shoes to numb-and-dumb your feet from the ground. You're completely in the moment.
[e8g3b1e] (score 5, diepte 5 OP) You simply watch where you're stepping. It's part of what I love about it: a very mindful experience. And when you do step on something that hurts your feet will be fine. You eventually just stop freaking out about it.
[e8fr120] (score 5, diepte 1) I am far too lazy to spend hours shopping for the right shoe, and then having to do it all over again when the shoe wears out. So I figured I'd just grow my own instead.
[e8fad3f] (score 4, diepte 0) Nice write up! I’m thinking of trying minimalist running approach. With either Lunas or Xeros. Any inputs?
PS: I’ve run 10+ half marathons and am a regular 8-12k runner, with shoes till now.
[e8fp7t7] (score 4, diepte 5) A quick warning - The first few times it will *hurt*. Asphalt tends to be, well, hard, and doesn't really give in, unlike the cushioning in your shoes did. You will need to build up some callus before you can comfortably run, or even jog.

When I transitioned from regular running to barefoot running, my average running distance dropped from 7-8km to a disappointing 1.5-2km. It took me several months of slowly building it up, getting used to the technique, getting used to *listening to what my body told me* before I got back to 5+ km.

When I did, however, it felt *GREAT*. I no longer run "because I want to stay fit" or "because I need to lose weight". I run because I *want* to run, it feels good. Nowadays, I run 4x a week, and I love it.

That is something I could not have imagined myself saying less than a year ago.

I wish you the best of luck, welcome to the good life, and be sure not to push yourself :)
[e8fm3pk] (score 4, diepte 0) The fear I had before going unshod was: "Everyone will be looking at you." Which is basically true, the people who see that I am not wearing shoes are looking longer than if I would run with shoes, some even comment like: "Without shoes?!".  
This fear was the main reason for me to run the first few weeks of my minimalist "journey" in some minimalist shoes, but once I decided to just test unshod running for like 100m I never put on shoes again for running (which is currently around four month).

This is why I am starting to worry about how this will work in the winter with snow and ice, but I think I will figure it out somehow, maybe I will need my minimalist shoes for some runs, but the goal is to wear them as less as possible.
[e8frzv6] (score 4, diepte 1) I run in NYC, and the insane amount of people staring took a while to get used to. Reactions range from shock to anger lol. But as a reverse to this, anyone else find themselves staring at people's off-kilter pronation when trailing them on the sidewalk. I can't help but take notice at these things now. Seeing people walk on soles with crushed edges makes me cringe.
[e8fb0nf] (score 3, diepte 2) Helps! Thanks! I had heard from some that first go minimalist, then barefoot.. gradually condition your feet..
[e8fbhmv] (score 3, diepte 4) 👍🏼👍🏼👍🏼 looking forward to the barefoot experience. Thanks!!!
[e8g3idk] (score 3, diepte 6) Alright cool! Do you guys listen to music when running? Or would that be too distracting and get you injured?
[e8fd7f5] (score 3, diepte 0) Top three hit home for me as well. I was ready to call it quits and then found the minimal movement. It’s helped every aspect of my training and passions. Hiking, yoga, paddle boarding and running. Nice write up. Do you find yourself looking at others feet now and noticing cramped toes?
[e8fg504] (score 3, diepte 0) +1. The only “hardcore” part of me taking up running in bare feet was the radical act of approaching running as an absolute beginner.
[e8ftx71] (score 3, diepte 1) Thats actually probably the best way to do it. You arent having to unlearn mistakes and bad form from years and years of running.
[e8fu1uh] (score 3, diepte 1) Its interesting I changed from a 12mm to 5mm drop shoes and my times dropped by a minute. Something I never really thought about I only really bought the shoes because Ive had an interest in running minimalist in the back of my mind.
[e8fttd4] (score 3, diepte 0) Its easier to call someone exceptional than it is to try it yourself. Like people calling me badass for running in the rain or snow. Im just too stubborn to call a run on account of the weather. So its easier for me to run than it would be for me to not run.
[e8gvrzk] (score 3, diepte 1 OP) That's because it's a bit of both and more complicated.

When I first went unshod I thought "gotta build up tough feet" and spent two years not progressing just beating up my feet. I didn't change my form, ran inefficiently and all that friction just caused foot pain I mistook as "feet getting tougher."

I didn't really improve until I gave up the concept of "tough feet" and focused on learning how to run gently on my feet and avoiding harm. Once I did that my weekly mileage jumped and I had to re-calibrate my previous measures for long distances and pace. I was suddenly running longer *and* faster.

Now, yes, in all that time my feet have gotten tougher and it does help. But it doesn't help as much as you'd think. Most of this season I was running in huarache sandals to do long trail runs (a 50K and 27 miler) on gravel. In the last month-and-a-half was about the only time I ran mostly unshod to get ready for an unshod marathon.

That's very different from people who worry about losing "foot toughness" over the winter and arrange to do things like walk in place at a standing desk barefoot in a bucket of rocks or forcing themselves to go barefoot 100% of the time or close to it out of some fear their feet will suddenly soften.

I wear shoes and socks all winter long and huarache sandals for at least 50% of my runs. I don't stress out about keeping my feet tough or anything yet I can still go out and do 26.2 miles on city streets with my feet only feeling sore for maybe a day or two after but no damage.
[e8h7bs0] (score 3, diepte 0) They envy your genetic mutation into a more true human... it’s subconscious but their self identity as a modern upright biped prohibits them from going where we go...
[e8hlybn] (score 3, diepte 1 OP) > But I don't think our ancestors were running on concrete and asphalt

The issue I always take is barefoot is actually super *easy* on concrete and asphalt. I live in a small town where the paved surfaces are more limited and often littered with rocks from the endless miles of gravel roads all around. Clean, smooth, paved surfaces are a dream to run on. *Rocks* are challenging and our smooth, manicured modern world has nothing on nature when it comes to super challenging surfaces. That's what our ancestors had to deal with. I'm in envy of city dwellers with their hundreds of miles of smooth asphalt trails.

There's an *assumption* with concrete and asphalt that the hardness is an issue [but all the research on that in the last several decades has turned up inconclusive](https://www.ncbi.nlm.nih.gov/pubmed/?term=withnall+do+shock+absorbing+insoles). More recent research points to [horizontal braking forces](https://www.theglobeandmail.com/life/health-and-fitness/article-how-running-gait-increases-injury-risk/) being closely linked to injury. It's not vertical impact or surface hardness that's harsh on the body. It's comfy running shoes with artificial traction encouraging over-extending your legs that's far more dangerous. We've evolved to actually have amazing vertical damping in our legs and feet. We did *not* evolve super high traction.

It's a pretty serious distinction, and once you internalize it that can help make unshod running easier. Cushioned shoes came out from that flawed assumption that we have to somehow mitigate surface hardness. As a result when you go minimalist or barefoot a lot of people continue that flawed assumption with a harsh "forefoot strike" that does, indeed, make running harder than necessary because you're over-using your lower legs for pointless, excess shock absorbtion. You can land midfoot just fine. I even hit my heels with a bit of force sometimes. It doesn't cause problems with me because I keep my feet under my hips and unshod reminds me to minimize those horizontal braking forces. If you land your feet more on the forefoot just because of body mechanics issues that's fine but too many people are awkwardly forcing that move.

And you're right about it being an artform! There's absolutely an aesthetic component which is part of why I like it so much. I'd argue that all sports should be like that. In the last half century the idea of sport as art has been seriously challenged as gyms proliferate and sports became big business. People don't go out and enjoy the outdoors with sport they "workout" and put in their time at the gym or get in their miles. The attitude toward people who exercise in general is to shout encouragement and say "good for you!" because there's a perception that they're sort of sacrificing something by execising. Instead, the attitude should almost be envy: "you're out there engaged in a sport and enjoying yourself and I'm not. I wish I were doing that. Looks very pleasurable."
[e8h57n4] (score 2, diepte 7) I would say a focus on a good running form is far more important than your mileage. Since you will be adapting a different running technique, it is 100% expected that your mileage will take an initial drop down
[e8ghdn2] (score 2, diepte 6) Great simple idea, easy to gradually increase this way...
[e8g2v2g] (score 2, diepte 4) I would love to give this a shot! How do you guys run on the streets tho? There might be sharp things like glass and plastic and stuff?!
[e8g4kxo] (score 2, diepte 8) Cool thanks for your reply! It's not for distraction in my case. I love running and just love it to have some music on aswell and enjoy the run :)
[e8g4pqd] (score 2, diepte 8) Like 2 years back I got special soles made for in my shoes because I had pain when walking. They told me I have flat feets so now I have special soles I should use? Should I stop using it from now on? Will the pain go away with time? I really dont know what to do with that.
[e8g4x5d] (score 2, diepte 9 OP) Who's the "they" in this saying you needed these soles? If they're prescribed by a doctor for serious biomechanical issues I'd recommend sticking with the Dr. recommendation. However, a *lot* of people are sold on insoles or othodics for foot issues only to find their foot issues got a whole lot better getting rid of the insoles.

Feet are just like any other part of the body: exercise them and they'll get in shape.
[e8g6ta7] (score 2, diepte 10) I guess nothing serious. I don't know how to call it in english? Podiatrist maybe? Its not really a doctor. Just someone specialized in feet. I have never had any issues with my feet untill I began running way too enthousiast. To prepare for an obstacle run. So basically no experience in running for my whole life to building up to 10 kms. In just a few weeks. After that my feet started to hurt just from walking. So I went to the specialist and she got to see my feet. She said they were really flat and gave me soles with like a bobble in the middle, like a small hill if that makes sense? So nothing too serious I think. I might be better of going without them and start getting my form right. What do you think?
[e8g6toy] (score 2, diepte 7) Your cadence when running barefoot should be ca. 170-180 steps per minute, right? I usually listen to my Drum n Bass playlist, the bpm fit perfectly if you choose the right songs or longer mixes. I can recommend liquicity for poppy/electronic ears and Ram Records/Hospitality Records for bassy ears. It helps you to keep the rythm at the beginning.
[e8i4bx6] (score 2, diepte 10) Awesomee! Well guess what... I'm from the Netherlands :p
[e8fyhh5] (score 2, diepte 2) Do you run barefoot in the dark?
[e8g63lj] (score 2, diepte 3) I run not in full darkness but often in twilight.  I run a route that I also run frequently in daylight, so I know what the worst I might step on is and the best path to take to hopefully avoid it.
[e8fe8tn] (score 2, diepte 1 OP) > Do you find yourself looking at others feet now and noticing cramped toes?

I do! Makes me wince every time. I see all these deformed feet due to a lifetime in shoes now. In addition to that I really started to notice how the vast majority of runners out there have really horrible form, almost always in the form of over-striding and way too slow a cadence slouching over and looking miserable.

In many ways I admire those runners: they're right up there with me. I feel like I've found the cheat codes for running and they're all working so very much harder but achieving the same thing as me. Makes me feel lazy.
[e8fga9z] (score 2, diepte 0) When people tell me I am "hardcore" for running barefoot I tell them nope.  I am lazy.  I try any manner of things to train less yet still finish with good times and barefoot running is one of my cheating short-cuts.
(26 reacties met lagere score weggelaten)

