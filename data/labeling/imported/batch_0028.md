# Label-batch batch_0028

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
Schrijf het resultaat naar `batch_0028.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 3oq438, eu6imt, qksd7l).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 3oq438 ===
SUBREDDIT: r/goodyearwelt
DATUM: 2015-10-14  SCORE: 11  REACTIES: 305
TITEL: Discussion of a General Nature/Questions That Are Basic/What's On Your Feet 10/14/15
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cvzjzk0] (score 9, diepte 1) Can I get it in a marbled brown roughout, with 4 eyelets and three speedhooks, open lacing, chisel toe, and a ridgeway sole?
[cvzg7rg] (score 9, diepte 0) [today](http://i.imgur.com/8EmPl9Q.jpg)
 

[faded "nice shoes" novelty shot](http://i.imgur.com/6pEf0KX.jpg)

Edit: lol @ everyone in mfa shoe thread who is questioning my gender.
[cvzfo32] (score 8, diepte 0) Going to post the GMTO today and I fully expect everyone to want a different color.....yay

hint its a navy shell jodhpur

Wearing the bison today
[cvzg1xz] (score 8, diepte 1) That is the most unsubtle hint I've ever seen.
[cvzetde] (score 7, diepte 0) Getting slammed with boots this week, Carmina Shell Jumpers arrived last night, Rider Dundalks coming on thurs, Viberg x SF shipping out this week, and a Rancourt MTO could arrive anytime now...all this after I was trying to make an effort to start buying more shoes instead of boots
[cvzg3b6] (score 7, diepte 0) So I got my olive nubuck Vibergs last night, and to celebrate having the sizing fit perfect, I decided to take my dog for a long walk in them.

I absolutely tore up my right heel on them in just like, 4 miles. So much so that I couldn't even contemplate wearing them today- so instead, I'm wearing my most comfortable pair of boots- like $70 Chippewa Apaches.

No pictures yet (it's fairly dark here by 5pm now). I will see about taking a couple shots at lunchtime if I can find a spot, otherwise on the weekend.
[cvzfj2g] (score 6, diepte 0) WSIAWT: [#8 bergs](http://i.imgur.com/3htEaiGh.jpg)

GD: Unimpressed with everyone during last night's debate. I like what Sanders wants to accomplish I just don't believe he'd be able to even if elected. Asking for donations in his closing remarks felt weak. Clinton is leaning way too hard on the fact that she's a woman. Chafee literally made me laugh. I think O'Malley might have some kind of green energy plan but I'm still not sure. Also not sure on whether Webb felt like he had enough time to respond. /s
[cvzjqhi] (score 6, diepte 1) Nice boots!  It looks like your office chair has been touching them inappropriately though.
[cvzei7k] (score 5, diepte 1) I like the fatigue boots except for the weird two-screw-speedhooks.  Just feels odd to me.

I think the blazer looks good. Not too long at all.
[cvzew5f] (score 5, diepte 1) How many cards could be jammed into the card holder?
[cvzfjrh] (score 5, diepte 2) This sounds so dirty.
[cvzhyip] (score 5, diepte 1) That just sounds awful...
[cvzff6s] (score 5, diepte 1) ['Tis but a scratch.](https://media.giphy.com/media/hl1teFHQSnzcA/giphy.gif) You should be able to make those look a decent bit better with some conditioner, brushing and maybe a spoon.

Did the ol' chair wheels get ya?
[cvzfnaq] (score 5, diepte 1) As much as I like what Bernie as saying, I just don't know if he'll be able to accomplish what he wants to.  But out of all of the candidates I still think he's the best candidate simply because he focuses on the issues.
[cvzhxy9] (score 5, diepte 1) Those look pretty sweet. Maybe I just haven't been paying attention, but I don't think I've seen many makers (aside from RW obviously) using leather from S.B. foot.
[cvzfxe5] (score 5, diepte 0) [Feet](http://imgur.com/YMVNlp2)

[Body](http://imgur.com/oitsjl5)

[Crotch](http://imgur.com/o91L8O2)

Discussion of a General Nature - Neighborhood shirts are the coolest and best fitting shirts on me.

Questions that are basic:  Why the F has no one done a review of their tan derby horse hides yet???
[cvzedxt] (score 4, diepte 0) Grabbed a pair of the apolis fatigue boots in cognac (looks like burgundy to me though) last night from eastdane with the 25 percent off coupon. The price came to about 250 and I figured with free returns, why not. I could like them. I could hate them. 

For some reason, I'm debating getting a pair of the Golden fox boondockers. I want a pair of something to not give **any** fucks about and these seem like a good candidate. Plus 65 bucks is a borderline laughable price. 

Came dangerously close to ordering the horween Essex Stan smiths last night. Didn't pull the trigger tho. 

Edit: Proud future owner of the Stan Smith's.  Got them in size 11 even though my Rod Lavers are 11.5, but I've heard that the Stans are a bit wide while Lavers are narrow. Pus the Lavers were too big on my right foot.  Fingers crossed!

[Last night] (http://imgur.com/CsUPraF). Got [this our legacy blazer] (http://imgur.com/rwjuC08) back from shortening the sleeves and finally [tried it out] (http://imgur.com/l4NBzlI) despite my apprehension to wear it. I think it worked out OK. The jacket feels a touch long in the body, but maybe most of my other jackets are just a bit shorter. [First good pants/shoe shot] (http://imgur.com/3N1qBPW) with my jods.
[cvzjwun] (score 4, diepte 2) It is worth noting that presidents can rarely accomplish things on their own, but the bully pulpit can steer the country in a way no other can.

He won't be able to spend everything he wants, but progress towards those goals isn't nothing, especially as it will be difficult to roll back that progress. It can be very difficult to take things away from people that they like.
[cvzfxd5] (score 4, diepte 0) [Oakstreet Bootmakers Trench Boot in S.B. Foot Tannery Copper Rough n' Tough](https://instagram.com/p/80nPWrhYbt/?taken-by=wilsonandwillys) at a local shop.
[cvzipv9] (score 4, diepte 0) **WSAIWT:**  [Viberg Tan RO Service Boots](http://i.imgur.com/EFpTpc8.jpg?2)  (decided to pack my dslr today...)
[cvze5zl] (score 3, diepte 0) WAYWT: [Trickers](http://i.imgur.com/LBkD7gvh.jpg) with speckles on speckles.
[cvzfgge] (score 3, diepte 1) Yes. Embrace the speckles
[cvzej4v] (score 3, diepte 0) First off, I appreciate the title.

* **WSIWT:** [Rider Boot Calf Dundalks](http://i.imgur.com/lJoPz21.png)
* **Leather Things:** Finished up a [few shell cordovan card holders](http://imgur.com/a/HwXTo). Horween #8, Horween Natural, and Shinki Hikaku Brown.
* **Wood Things:** If you're ever in the market for wood related gifts or need something for a female counterpart, [check out my college roommate's stuff](http://prestonmade.com/bangles/nashville). I thought this was cool enough to share. It is a solid walnut bangle with a guitar string inlaid into it. He also does some [wood prints](http://prestonmade.com/prints/) (I bought one but just need a frame for it), cutting boards, and [fishing nets](http://prestonmade.com/nets/vermillion).
[cvzgyeb] (score 3, diepte 2) I'm at 8 with mine (including a keycard that's probably 1.5-2 cards thick) if that helps 

Edit: and like 5 bills too
[cvzejpk] (score 3, diepte 0) **SQ**: Is Meermin's *full brogue wingtip derby boot* in dark brown country calf [(idArt=4587)](https://www.meermin.es/articulo.php?idArt=4587) the best sub-$300 sleek beginner boot for casual wear (slim denim) that also can be dressed up?
[cvzi5fp] (score 3, diepte 3) Yeah, unfortunately, that budget won't give you many alternatives besides Meermin. There is [Shoe Passion](http://www.shoepassion.com/) in Berlin and within your price range, might want to check them out.
[cvzekgs] (score 3, diepte 0) On my feet: [Alden](http://i.imgur.com/VkkzQk8.png)

Discussion of a general nature: Received the Shetland sweater I posted about last week. Fits well and is pretty nice, very tempted to order another one. Also got this J crew merino cardigan to replace a J crew factory cotton one I wore into the ground and then got lotion all over it when I got my haircut a few weeks ago. I really did not want to get lotion rubbed on my hands, but I appreciate the excuse to upgrade my cardigan game.

DoaGN2: I have become a "regular" at the Dunkin Donuts by my office. I'm scoring a senior citizen discount, free donut holes, and amazing service. Dunno why, but this makes me really happy.
[cvziedk] (score 3, diepte 5) Lol. "Don't worry they're already moisturized"
[cvzjtgh] (score 3, diepte 5) > I already got a handy this morning, thanks.
[cvzeoaj] (score 3, diepte 0) Wow! I'm loving these [Irish Monkey Boots ](http://i.imgur.com/aPWx3k4.png) from Junkard. Anybody know of a similar style with equivalent color from a more recognizable and available brand? I don't know or see much about this Junkard Company...?
[cvzevy4] (score 3, diepte 0) [Today - Chippewa Engineer Boots](http://i.imgur.com/O61CdDIh.jpg) -- [Full Outfit](http://imgur.com/a/FRFlW)
[cvzf4b9] (score 3, diepte 0) Got my EG Rosewood Galways, and they are a perfect fit and flawless construction. $927 shipped from Montana (it's bumped up $150 in the past week...) which for a pair of EGs is an unbeatable price. Not something I'd recommend to everyone, but I wanted something with heavy-duty tread for when Dainite won't do.

Couple of things, just spec-wise, that weren't immediately clear from the specs or from other people's reviews, in case others want to buy these.

* The shaft of these is unlined. Wasn't specified one way or the other, I just didn't know.
* The shaft acts as lining under the vamp. I had assumed that where the vamp and shaft met, the shaft would just stop below that. So while the ankles only have one layer around them, the foot does have two layers.
* The tongue is half-gusseted.
* It is a half-sock liner.
* The sole layering is: upper (it is Veldtshoen), welt, midsole, outsole. The heel has no stack, just a solid rubber heel nailed on.
[cvzhzno] (score 3, diepte 2) There aren't a ton because Red Wing owns S.B. Foot Tannery. I'm kind of shocked to even see another brand using the leather.
[cvzibf7] (score 3, diepte 3) Especially one of the flagship RW leathers.
[cvzglor] (score 3, diepte 1) Pure laziness, haha, at least for me. I did a mini review inside of a GD, but I can flesh it out and make it its own post if wanted
[cvzhkdz] (score 3, diepte 1) Monks look great!  Sockless or no-shows?
[cvzg9vo] (score 3, diepte 0) WSAYWT: [My ass-kicking boots](http://i.imgur.com/Hxd50CV.jpg) 

It would be interesting to know who made these. Bought them off ebay marketed as vintage veldtschoen boots. Definetly not veldtschoen but unquestionably vintage. Markings show only the size and possibly the last but Google didn't give any answers. Quite sure they're british made though.

Edit: 
Simple question: i need some recommendations what pants to wear with my [black french army double buckle boots](http://i.imgur.com/u0VdxWO.jpg) boots. Usually i wear skinny black jeans tucked in but would appreciate new ideas.
[cvzgqwu] (score 3, diepte 0) Wearing [my first pair of iron rangers today,](http://i.imgur.com/sSgnMEY.jpg) courtesy of /u/sklark23 (my wife's boots fit great btw.)

I'm off today, so I'm watching the debate, hauling off trash and probably going to do a little thrifting.
[cvzj6em] (score 3, diepte 0) Viberg did send me replacement laces for the boots and very promptly as well, it is fantastic CS on their part which echos what /u/les_diabolique said about having a dedicated person. They were great.
[cvzjbi2] (score 3, diepte 0) Got a new pair of Tricker's seconds from ebay and I'm very pleased with them except something I've noticed only today:

http://imgur.com/bO3BQPB

The sole is very excessively trimmed in the toes and leaves only little material in front of the welt stitching. Is this something to be concerned about? The stitching on the outsole is in it's usual place.

EDIT: Thanks, guys. That's reassuring! I'll post a review of these to show everything that could have made these seconds.
[cvzos0l] (score 3, diepte 1) truman
[cvzq1sy] (score 3, diepte 0) Freshly delivered [EG Camden in hazel antique](http://i.imgur.com/9tkH05b.jpg). These are tough to get on for my right foot. Does it get easier?
[cvzvoa6] (score 3, diepte 0) So, this [*poll*](http://imgur.com/Dutm1xQ) popped up on our intranet page today.  The [*results*](http://imgur.com/hMFwAPz).
[cvzhy4e] (score 2, diepte 2 OP) Can do! I have two other ones and they're actually a bit short in the arms, fine in the body.
[cvzgpq2] (score 2, diepte 1) Pant deets?
[cvzhm8h] (score 2, diepte 2) Epaulet
[cvzeanf] (score 2, diepte 0) [I did an outfit grid with RM's]( http://imgur.com/pjs51VI) for a fit from a few days ago, put me on MFA front page pls. [Here's two](http://imgur.com/u3yoHBp) [shots](http://imgur.com/s7adEoo) of me trying sitting fit pics on my bed instead of my normal standing ones. It doesn't really get the boots which is crappy, but the light in my room is good. Also, daylight savings is in effect in Adelaide now, so GD's are posted around 12.30 am, which means I can't really contribute as much as I want.
[cvzeg3b] (score 2, diepte 0) Felt not so great last night so I went on a little retail therapy. Picked up some whey, a blender bottle and climbing chalk for gym things and a pair of earbuds for train rides. 

More interestingly I backed TS's lambswool shirt from their maritime collection. 19oz was too hard to resist. 

Meeting the ex tonight to swap clothes and keys and things. Then off to New Orleans on Friday for a solo photography trip. 

[riders today](http://imgur.com/enY7EsG) while we play with canons new [HDR broadcast monitors](http://imgur.com/F6E4Zke)
[cvzhjgy] (score 2, diepte 4) Maybe try eating a tone of saltine crackers while lifting and you can just spit the powdered cracker on your hands?
[cvzhuif] (score 2, diepte 2) Meermin seems like a no-brainer, yes. But getting the boot style right , not so much.
# Conditions
* price: < 300€ (~ $340)
* location: some German city
* session: winter
* person: male, twenty-something wearing basics: slim jeans/chinos with a parka over a sweatshirt/sweater, sometimes layered with shirts
* use: casual: university; mostly just outside for a short ~5 min walk to the bus station

# Possible styles
*  ~~american work boots~~: seem way too clunky for Europe
* ~~hiking boots~~: too clunky
* service boots: didn't really find sleek ones (Alden, Viberg) in that price range
* derby boots: only casual enough with brogue(?) there was a past [discussion](https://www.reddit.com/r/goodyearwelt/comments/2c453j/review_battle_of_the_budget_boots_part_2_meermin/cl53lup) about Meermin's then *tan country calf cap toe derby boot*, and /u/6t5g didn't recommend it for denim or versatility
* chelsea: more like a fall boot(?), want winter. Meermin only has suede, which isn't ideal for f/w (insulation), even with sprays to make it water-proof. sizing harder for pull-on boots and Meermin doesn't offer free returns
[cw03dki] (score 2, diepte 3) > service boots: didn't really find sleek ones (Alden, Viberg) in that price range

Have you considered Dayton? Or are they out because you can't afford to wait for an MTO? $550 CAD. They have sales occasionally too.

What about Markowski? Do they have anything?
[cvzeqql] (score 2, diepte 1 OP) DoaGN is here to stay.

You better bring D Holes to the trunk show bro.
[cvzgwy1] (score 2, diepte 3 OP) ;)
[cvzgbrj] (score 2, diepte 4) [Head massage](https://youtu.be/Dn4pqQWAOd4)?
[cvzgk45] (score 2, diepte 3) Just say no massage. My nail place does a shoulder massage and hand massage (no extra charge), I say "no massage please" if I'm not feeling it that day.
[cvzt032] (score 2, diepte 6) Gross
[cvzh2q5] (score 2, diepte 4) I miss Mohamed so much. I'll take YouTube videos of Turkish music over awkward hand massages every time
[cvzeyfh] (score 2, diepte 1) I think [Rider Boot Co](http://riderboot.com/product-category/rider-boot-co/) does but the images aren't showing up for me. Anyone else?

**Edit:** [Found them](http://riderboot.com/shop/rider-boot-co-monkey-boot-rev-kudu-snuff/). Definitely a different color but would be good construction at a sale price. Had to find it by hovering over all the page until I found the right name.
[cvzfxpw] (score 2, diepte 1) I know Tricker's have done some beautiful monkey boots in many different colors and leathers but can't find them available anywhere right now.
[cvzkxge] (score 2, diepte 1) [Enzo Bonafe](http://us.skoaktiebolaget.se/collections/enzo-bonafe/products/enzo-bonafe-alpine-boot) does a similar style.
[cvzety8] (score 2, diepte 0) I like boots season. Wearing [Viberg Service Boots tan latigo](http://i.imgur.com/PtcHKbd.jpg), flat waxed laces are not bad on these.

All this talk about getting Massdrop Rider shipping notification made me irritated because I don't get any and their warehouse is just across the river... probably that's why tho :(
[cvzfxwe] (score 2, diepte 2) It's just as you described. Lace them up carefully and make them flat haha
[cvzf4bx] (score 2, diepte 0) [Meermin Suede Chelsea and Gustin Chinos](http://imgur.com/tzUXB3T.jpg)

[Pic 2](http://imgur.com/8kTpqHQ.jpg)

They're not perfect but I decided not to deal with sending them back, I think the color will even out with age and maybe some brushing
[cvzo2js] (score 2, diepte 2) It's more that my two boots are slightly different colors and textures... Plus some other flaws in the boots. After wearing them today I think it's going to be fine though
[cvzv53c] (score 2, diepte 2) Yeah the variation is wild. For some reason, under pot lights in my building's elevator, they look like garbage, but then outside or in natural light, they are amazing. I'm actually really happy with them and now I'm in love with Chelseas which is the last thing I needed.
[cvzfaxb] (score 2, diepte 0) On the feet - [RW IR](http://imgur.com/jeGabxh) using my iPhone 5 so the cranky potato phone photo. 

GD- Olive Dundalk are on the way and should be home by tomorrow. Anyone else get shipment notification

GD 2 - bought [this](http://imgur.com/uNjF1zr) awesome schott caf1 jacket from eBay for a great price after looking for a jacket for almost 2 months.
[cvzfl4i] (score 2, diepte 2) I have a bunch of chair wheel scratches, but those all pale in comparison to whatever caused this one. I remember feeling at the time it happened thinking, "oops, that's gonna leave a mark." But because I didn't look at them at that moment, I completely forgot what I bumped into that caused it.

Oh well.

I'll see how it looks after applying conditioner the first time. I'm not too worried about it.
[cvzl9cc] (score 2, diepte 2) Yes sir, not even two weeks from receiving them.
[cvzfdjz] (score 2, diepte 0) **On my feet**: [McTavisheseses](http://imgur.com/OEUb5ER). [On my whole self](http://imgur.com/v3RzICm).

**GD**: I used coconut oil on these guys a few days ago, I think I'd recommend against that on brogued shoes. There are just so many places for it to get caught, and I think some of it actually started to mold. I made sure to brush the crap out of them to make sure to get anything off, but from here on out, I'm switching to Lexol for my conditioning.
(245 reacties met lagere score weggelaten)

=== THREAD eu6imt ===
SUBREDDIT: r/goodyearwelt
DATUM: 2020-01-26  SCORE: 13  REACTIES: 163
TITEL: Are We Screwing Our Feet?
POST (source_id=post):
Hey all.  I’ve been excited (okay, obsessed) with building out my boot collection, until running into a wall.  I started reading about the benefits of minimalist shoes which promote a more natural, barefoot-style way of walking.  AKA “Zero Drop” footwear.  Apparently wearing flat (no heel) shoes with ultra wide toe boxes can prevent and/or fix many joint and spinal issues.  It made me question every single pair of boots I own, and am eyeing to purchase.  I want a pair of chunky-healed White’s goddammit!  But, could it be that we’re all screwing our ankles, knees, and lower backs with this fetish?

You can checkout some of the articles I read: [Lose Your Shoes](http://sock-doc.com/lose-your-shoes/) and [The Best Batefoot Shoes...](https://primalhacker.com/blog/barefoot-shoes).  A google search would turn up many others, and many pertain strictly to running shoes, but it’s clear the concept applies universally to all footwear.

Some examples of the companies making footwear for the barefoot way of life are [Prime Trotter](https://primetrotter.bigcartel.com/products), [Vivo Barefoot](https://www.vivobarefoot.com/us), [Lem’s Shoes](https://www.lemsshoes.com/collections/all-mens-products), [Softstar](https://www.softstarshoes.com/adult-shoes.html).

No, these are not boots you dream of owning, or donning at work, or at your next party.  Some are downright embarrassing!!  But ... knee braces, walkers and wheel chairs aren’t making it to the cover of GQ or Vogue either folks.

Thoughts?  Any other brands you know of, along the lines of Prime Trotter, that are striking the balance?  Most importantly, does White’s or Truman do zero-drop?!!  (Don’t answer that).

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ffm03qv] (score 135, diepte 0) Hey, physiotherapist weighing in on this - to my knowledge there is no established, proven link between footwear and spinal issues. Orthotics and shoe type can make small changes, enough to ease a painful and inflamed joint in your ankle, knee, hip or back, but only for 6 weeks or so. All the research that I've read that showed a difference only showed one for 6 weeks, and differences disappeared by 12 weeks.
The human body is so adaptable, so don't let it worry you. Do whatever floats your boat!
[fflxjno] (score 134, diepte 0) Didn't vibram get a class action law suit for hyping the benefit of "barefoot" running?
[ffm4k3y] (score 76, diepte 2) Part of that is because most people didn't start off slow and transition into that style of running. It takes months for the body to adapt and strengthen muscles and tendons that have not been used that way before.
[ffm2oxg] (score 68, diepte 0) So you read a couple articles and became converted to the barefoot lifestyle? 

For those who’ve looked at the research on this topic, there’s little to no scientific evidence that the barefoot trend actually improves anything.
[ffm2god] (score 67, diepte 1) Yes. It’s absolutely awful for most people.
[ffm996w] (score 45, diepte 2) Oof, this article has all the hallmarks of snake oil sales. Just about every paragraph has assertions that deserve a Wikipedia “citation needed”. 

As someone who has flat feet and overpronation, I can say authoritatively that orthotics improved my foot pain significantly. There’s lots of properly randomized studies with supporting evidence that a quick google search will turn up, here’s just [one from the NIH](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4742336/).
[ffm6jro] (score 44, diepte 1) Jumping off of this point, I have heard from orthopedists that varying shoe type and activity helps keep the body from over-adapting, promoting a balanced physique. 

Love to have your opinion on this as well.
[ffmfoqd] (score 40, diepte 2) > I'm a board-certified chiropractic physician and clinical nutritionist with a passion for true natural health care.

Scam.
[fflxe8z] (score 28, diepte 0) I don't know about long term but my feet and my body in general feel way better after transitioning from cheaper shoes/boots to what I'm wearing these days. I agree that a wide toe box is great, and has helped my feet issues - squeezing into narrow shoes isn't good for your feet in general. Now going sans heel, not sure about that even if it is better for you (I prefer a heel to my flat sneakers when it comes to comfort so who knows). As someone with collapsing arches and collapsing metatarsals, the barefoot thing wouldn't work for me anyway.
[ffm3fcd] (score 28, diepte 2) Just in case anyone thought this is crazy that a lobby for that would be real, that lobby [does exist](https://www.opensecrets.org/orgs/lobby.php?id=D000023989), though I don't know of them doing anything about this particular issue. Seems like there's a lobby for every established business
[ffm8jqt] (score 28, diepte 4) Yeah, there are benefits, but it takes some work. I ran cross country and track through college. One thing we did was barefoot running, often after a hard workout. But we did it in soft grass and built up how long we ran for.
  
Personally, I can see a benefit to wearing multiple kinds of shoes. I mix it up wearing boots, running shoes, hiking shoes, and very flat sneakers. But most of my day is in work boots, so there is that.
[ffmde0b] (score 25, diepte 2) That's been my anecdotal experience. 

When the barefoot craze hit, I checked it out and got into it. Figured I'd give it a shot and see if it was worth anything, as my back always hurts. I was running 5k's every week. Trained for a few months with vibrams and barefoot, eventually did a few 5k both ways. It was better after months of training, and even switching back to running shoes I noticed a greater understanding of where I should land my feet for the most efficient and least stressful running style, so that was nice. 

However, for daily use, at work, walking and standing around, I still couldn't do a flat shoe without getting back pain. Having some heel is critical for me if I'm going to be standing around for hours, since you can't constantly be adjusting your center of balance and pressure.
[ffm714y] (score 25, diepte 0) I've run in low drop / zero drop shoes for about a decade now and the only noticeable improvement was in the strength of my feet. And that was a result of changing my running form to a forefoot strike from a rear strike, which was enabled by zero drop in my case. Trying barefoot shoes seemed to offer no incremental benefit.

I don't think the same applies to walking as the mechanical advantage of eliminating heel strike while running isn't present when walking. The same holds true of reducing the forces applied to your joints.

I do use Xero and Vivo Barefoot runners but that's about width and fit as well as the cushion being in the insole so I am not throwing out the whole shoe every 6 months (just swapping the insoles).

TLDR: zero drop makes sense for running, and as long as you aren't running in your boots it's not an issue IMO. "Barefoot" is just marketing.
[fflxcji] (score 23, diepte 0) I think people need to stress out a bit less about their consumer choices. While I think some things are obviously bad for your feet and posture (wearing stiletto heels every day, having little space for your toes in most of your shoes, etc), there's no need to question your whole life or panic.
[ffmjf3a] (score 23, diepte 3) Lol, "chiropractic physician?" Chiropractors aren't doctors.  Also "nutritionist" means literally nothing.
[ffm7ixw] (score 22, diepte 3) I gave the five fingers a go in 2011 for a few weeks.  I remember two things: my calves were sore as shit and bruising my feet stepping on rocks   I knew a fair amount of people who gave the vibram a go but none made it over a month.
[ffm502l] (score 22, diepte 1) This. 

It seems like a good idea anecdotally but it’s not supported by evidence. The barefoot “movement” is not much more than a marketing campaign to sell more shoes, books, etc.
[ffmmjvk] (score 19, diepte 0) Well, as usual, the people on the extreme ends of this are idiots.

Going barefoot is not the panacea for anyone with any foot woes. Modern life and society have entrenched cushioned and structured footwear into our lives and it’s simply not realistic nor necessarily beneficial for everyone to convert away from that type of life. That’s why people hurt themselves so often when they dive into this fad too quickly and drop out rates are high. But that’s the equivalent of going from being a slob on the couch into a CrossFit.

Having the medical claims removed and being fined for them was the right thing, because they overextended the claims, and agencies are serious about what gets put on labels. But pointing to that removal to show it’s all marketing bullshit is as obtuse as saying Trump didn’t do anything unsavory because he didn’t explicitly ask for quid pro quo on tape. There’s more to the story than that if you care to pay attention. 

That said, the benefits of training with less structured footwear absolutely has potential benefit for many, and is not “all marketing bullshit”. People who think it is must truly be blind to all the gargantuan marketing efforts put out by Nike/Adidas/whatever other entity you want to think of that’s vested in high amounts of cushioning. And yes that includes physicians - most are friendly and nice people but from extensive experience in my day job, I can tell you that they are just as subject to fads, marketing, biases, and being irrationally influenced like anyone else.

I’ve run marathons and several shorter races and found that integrating those ugly things into my training really did improve my form and bio mechanics. Calves and feet definitely were very sore easing into it, but so are any muscles that you wake up from dormancy.

TL;DR: Good if used judiciously. Too ugly for day-to-day use.
[ffm3gsr] (score 16, diepte 0) I've had flat feet all my life, had a bunion removed in a foot that now has 3 screws and is now coming back, plantar fasciitis, and bone spurs in my heels. My feet suck. I've worn the zero drop shoes (I still have some Reeboks that I kinda like), flip flops, deck shoes, and have gone through several types of prescription custom orthotics. The orthotics helped some in my boots I had to wear in the military, but since I've spent the cash on higher end boots, my feet haven't been happier. I have almost no foot pain, aside from the heel spur from time to time. I didn't have that relief from any of my "flat footed" zero arch and zero drop type shoes.
[ffm1d1z] (score 14, diepte 0) There is no provable benefit to minimalist shoes. If you like em you like em, but it's a marketing campaign to sell shitty shoes.
[ffmfbo4] (score 13, diepte 2) They settled the lawsuit and agreed to not make any claims about the health benefits of their shoes *unless new scientific evidence proves otherwise*. They haven't made any claims about the health benefits of their shoes since and the lawsuit was 6 years ago.

That being said, if you're really worried about your foot and back health you should probably just ask your doctor to ask what shoes will be best for your health. Online articles that aren't well sourced or aren't from reputable sources probably aren't going to give you good medical advice.
[ffoskcs] (score 13, diepte 3) > Barefoot running is the only way to run without long term injury.

No, it’s not. Don’t make shit up
[fflwnf6] (score 10, diepte 0) They are ugly alright. I tried the barefoot running thing when it first caught on (literally barefoot). It was interesting. Considering I’d plop my feet into cowboy boots for work right after my runs, I don’t think I ever gave it a truly fair shake and have a weak lumbar to this day likely as a result of heels. In my youth I rarely wore anything with a heel.
[ffmnz71] (score 9, diepte 2) So does the scam chiropractic lobby.
[ffmvozy] (score 9, diepte 4) My buddy had a pair of those in college. The only thing I remember is His feet smelled so fucking bad.
[ffmjsbo] (score 9, diepte 2) Or maybe its because he seems nearly fanatical about a new "lifestyle" choice that he decided on after reading a few really poorly written and poorly sourced "articles" that he found online, written by fake doctor scam artists.
[ffm62nc] (score 8, diepte 2) I don't personally use orthotics because I am lazy ( I should). Not really in a position to truly argue this sort of thing because I'm not a doctor. My personal opinion is that yes, orthotics aren't the be all, end all - but they do have their place. I do think that actual therapy of the foot is a good thing to pursue either way, orthotics or not, I'll give you that.
[ffmyxlz] (score 8, diepte 1) The entire chiropractic industry is a scam. Please see a real doctor if you are having issues. Orthopedics may be necessary to alleviate whatever it is that took you to get looked at, but go to a real doctor, not a scam chiropractor.
[ffmjpqt] (score 7, diepte 3) I have high arches and I got custom orthotics about 2 months ago. They have made a huge difference. My feet don't hurt if I stand or walk a lot anymore.
[ffofelf] (score 7, diepte 5) I remember seeing these on someone in jeans... on the subway!
[ffm6met] (score 7, diepte 0) One thing I've never really heard people talk about with regards to the "barefoot" thing is all of the debris, hazards, or general differences on the ground. The barefoot shoes are supposed to be as close as possible to being without shoes, so not much of a sole to absorb anything. Seems like any imperfection is going to be felt, potentially all the way up your back. When I wear my Chucks I can barely tolerate walking on gravel, and I feel every bit of debris that may be on the ground. My Red Wing Work Chukkas have a thick ass Atlas sole and they absorb about everything. Barely feel when I step on gravel or other rocks and debris. Depending on your work situation those "barefoot" shoes could actually be a detriment. 

Just keep in mind that everybody is different, and that means every body is different. What helps one person can be a total hinderence for another. If doing the barefoot thing is good for you that's awesome. Best thing to do would be get a pair, try 'em out, and see how it goes.

With my zero amount of arch those types of shoes only exacerbate all of my foot, knee, and back issues. Plus working in a factory those things won't fly with OSHA.
[ffma6yc] (score 7, diepte 0) Not a doctor, physio, podiatrist, etc. so take what I have to say with a grain of salt.
I’ve been interested in low-heel footwear for a while, and much of my understanding of the “bare foot” movement so far (and pretty much all other “return to ‘nature’” trends) has been that while it may be ‘better’ in perfectly “natural” conditions, it likely won’t work out super well for most people.

I see it kind of like washing your hair. Teecchnicallyyy you “should” only shampoo your hair once a week or less. In ‘natural’ conditions, the scalp generally does a decent job at keeping itself “clean” by washing simply with water. However, for better or for worse, shampooing has become an, often daily, ritual for many. Over time, our scalps have gotten used to such vigorous cleaning and adjust sebum production to compensate. So if you were to suddenly stop shampooing, you’d get greasy as fuck, fast. And if you have dandruff, psoriasis or any other condition that actually requires daily/regular maintenance, you’d probably suffer needlessly too.
Personally, I went through the whole “no-poo” journey a long time ago, and only shampoo every few weeks now. It was worth it for me, BUT I could do this because I: 1) don’t have any underlying scalp issues, and; 2) didn’t shampoo much to begin with. In general, I don’t recommend it to most people, even though I appreciate the benefits. If you do want to try it, you really need to take it slow and it’s gonna suck for a long time until it gets better.

I see barefoot footwear in a similar light - sure, going “back to nature” is cool and all, but it seems like it can be one hell of a gruelling process for those of us who are accustomed to heeled footwear, potentially being downright painful or even dangerous for people with certain foot/joint conditions.
I know a lot of people who swear by toe shoes etc., but they didn’t have any underlying issues before starting, took it slow and didn’t wear much heeled footwear to begin with. 
So maybe they work for some people, but there’s a lot to consider and it looks like it’s definitely not for everyone.
[ffmnjvk] (score 6, diepte 3) Most doctors are highly misinformed about this, unfortunately.
[ffn3rsx] (score 6, diepte 3) I inadvertently wore mine on a 6 mile hike over soft & packed dirt, rocks and concrete.  I was very surprised at how my feel felt afterwards - really good.  I had been wearing them for weeks prior so a little adjusted to them.  I just became very aware of where I placed my feet on the hike; stepping on the points of rocks were a no-no.

Running is different.  Uncomfortable because I am used to heel striking like in regular runners.  Vibrams require a different way of running which does take much more time to develop
[ffmoxay] (score 6, diepte 3) It's this.

If you like minimalist footwear, by all means wear it! But don't evangelize it by posting a bunch of scam articles.
[ffmka96] (score 6, diepte 2) Slightly off-topic but this convo reminds me of character classes in video games. In this case, we would be going for a "Naturalist" class where the character runs barefoot, eats paleo diet, and wear organic cotton / wool clothing. Doing all three grants some unique perks and unlocks a special achievement.
[ffmc0gh] (score 6, diepte 0) I'm skeptical of the high heels on whites outside of the wildland/logging context. They put your feet in an odd position when you are standing on hard flat surfaces.

There are options though outside the weird world of barefoot shoes. How about these quoddy boots? 

https://www.quoddy.com/collections/mens/products/camp-boot
[ffnefns] (score 6, diepte 0) I’m new to this sub. This is funny, why are y’all hardhatting OP?
[ffmf7wd] (score 5, diepte 4) I had a pair since that time, did a 5k, a 10k and all  the training that goes with it in the 5 finger. Honestly, can't say they are noticeably different. It's all marketing
[ffps5m4] (score 5, diepte 5) I convinced myself it was satire when I read it earlier
[ffor9hm] (score 5, diepte 3) That is not supported by the science. The only injury I eve sustained in my two decades of running was whole training in barefoot running shoes.
[ffmcsaq] (score 5, diepte 0) I love my Unshoes Forager. Check them out. They are a minimalist moc. Leather. USA made.

https://www.unshoesusa.com/collections/closed-toe/products/forager-brown

They are great for summer wear, or a slipper for winter. I think they look cool with just shorts but they are acquired taste.
[ffmxmq8] (score 5, diepte 1) >I just had my feet scanned at the chiro yesterday, after which her assistant tried to sell me $300 orthotics.

Why did you have that done? Are you having foot or ankle pain?
[ffnk0t8] (score 5, diepte 1) I've been on this sub a long time and I've never seen this level of brigading before. I see nothing wrong with OP's question or any of his answers. Kind of disheartening. Open discussion on this sub died a little more today.
[ffpqcbx] (score 4, diepte 4) You realize how extremely racist this is, right?
[ffmm10s] (score 4, diepte 2) I don't know what OP expected. This is a high quality (mostly) traditional shoes and boots enthusiast sub. Coming here and discussing the merits of barefoot shoes is like going to r/malefashionadvice and trying to discuss the merits of wearing a track suit everyday.

No shit people are going to be a little weirded out by that idea.
(123 reacties met lagere score weggelaten)

=== THREAD qksd7l ===
SUBREDDIT: r/ChronicPain
DATUM: 2021-11-02  SCORE: 145  REACTIES: 146
TITEL: Did you know there are no joints in your feet?
POST (source_id=post):
Had my first visit with my new internal med doc today. Felt more like being interrogated as a murder suspect. This guy was excessively intent on degrading me, diminishing all of my symptoms, and making me out to be a liar. 

So, this doc was so aggressive and consumed by his intentions, that while I'm trying to get a few words out when asked about my joint pain, I mention my feet. He immediately exclaims "I'm a little confused about your story here.... I asked you about joint pain and you brought up your feet!? There aren't even joints in your feet!" I burst out laughing and tried to interject, but he was already going off on explaining what exactly joints are-- to the invisible 2 year old in the room. 

Bummed 'cus I was looking forward to today in hopes of progress. I just can't get over that statement though. " There aren't even joints in your feet!" Bahahaa. Wow...

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hiyf11c] (score 105, diepte 0) Well, gee, I wonder what it is that's inflamed, painful, and seems to be located in the intersections between my foot bones, then. Ghosts?
[hiyj1od] (score 86, diepte 0) There are more than 30 joints in your feet. Wtf
[hiypbel] (score 74, diepte 1 OP) So bizarre to hear a doctor say so confidently that there aren't. I didn't know there are as many as there are, but I did know there's a bunch. I asked my 7yo when she got home from school if she thought she had joints in her feet. With no explanation of what a joint is or anything, she looked at me like I was crazy, took her little boot off and said while wiggling her toes up and down, "Uhh... Daddy.... My toes can move". Haha.
[hiyp369] (score 62, diepte 1 OP) Exactly! There be demons in them there feet. An exorcism must be necessary.
[hiyyos8] (score 52, diepte 0) I just googled joints of the feet. Nice image. The text says the foot is made up of "26 bones and 33 joints that must work together. Even small changes can cause issues." I'm sorry to say, this doctor may need a medical school review.
[hiz1wmv] (score 43, diepte 0) Why be a doctor if you are just going to demean people that need help? I just do not get it.
[hizpdg2] (score 31, diepte 2) My favorite one..I get ear infections all the time. Go to new PA and get told "adults don't get ear infections. " So why are you giving me antibiotics for my non ear infection?
[hiz040x] (score 28, diepte 0) That's pretty much how all of my appointment for joint pain have gone. Always an interrogation followed by insane, factually incorrect statements. Apparently only people above 65 can get osteoarthritis, you can't be in pain if there's no indication in a sed rate, it's not swollen if it isn't red, and periods are the cause of everything.
[hiyjq9c] (score 27, diepte 0) Woah, dude. Where'd he go to medical school!?
[hiyom05] (score 21, diepte 1) Online degree.
[hiyqsar] (score 20, diepte 2 OP) Hehe. Intersections? This guy probably would've said they are 'bendy spots' in my bones .
[hiz7c0j] (score 20, diepte 1 OP) I can't wrap my head around it either. Seems there are far more who are arrogant narcissists simply there because that's where the money is and /or they have a superiority complex and are trying to make themselves feel above everyone else. Not all docs by any means. But it would be really interesting to quantify and look at the statistics. Its really sad that one has to even consider these questions .
[hiz665w] (score 19, diepte 2) Obviously your feet hurt due to all the ghosts in them. Perhaps you need to call Ghost Hunters.
[hiyq42t] (score 19, diepte 2 OP) Yup. Took a Udemy course.
[hiz2105] (score 18, diepte 1 OP) Hmm... Yeah, I guess I can see how that can be taken to mean that there are no joints in the feet then, right? Review definitely necessary.
[hiyzbtk] (score 18, diepte 0) welp i guess the joint i had fused and had to have 3 surgeries on in my foot is just fake then. good to know
[hiz36m2] (score 17, diepte 1 OP) Oh absolutely. It's a psychiatric issue. He even said if I would just decide I want to live a normal daily life and try harder then I wouldn't be in pain or sick all the time. Your experience sounds miserable btw
[hiz0if1] (score 16, diepte 0) Please, if you can, find another doctor. Yikes.
[hj00lt9] (score 16, diepte 1) Power tripping. I had a doc "explain" to me that my symptoms were being caused by pregnancy and the reason my tests were negative was because I "was too early to detect". I'd only had said symptoms for 1.5 years. Apparently twice the length of human pregnancy is "too early". It's three years later and, this won't be a surprise to anyone with a brain, no baby.
[hizs4so] (score 15, diepte 1) It's a power play, to "put you in your place", so to say. It's abusive and I detest doctors who are bullies.
[hiz5ezr] (score 15, diepte 0) I bet he’s the type to believe women pee from their vagina too. Jesus, did this guy skip cadaver dissections in med school? He understands less about anatomy than a 6th grader
[hj0amk0] (score 13, diepte 2) No baby?! But you have all the symptoms! There must be a baby somewhere! Have you checked all the rooms in your house? Maybe they're just hiding really well.
[hiz4zhx] (score 12, diepte 1 OP) Why does this seem to be the standard perception and bx doctors have? Empirically it certainly isn't sound. I primarily studied physical science and geospatial science in college. Heavy reliance on data. Even in those fields it's well known and accepted that data does not always = truth and we don't know everything. Isn't medicine a science? Shouldn't these facts be accepted in the medicinal branch of the sciences as it is the others?
[hiyok7e] (score 11, diepte 1) Junctions?
[hj0qyh8] (score 9, diepte 3) 😂😂😂😂adults don’t get ear infections that’s fucking hilarious.
[hiz58ja] (score 9, diepte 1 OP) I definitely will. Might need to go out of town unfortunately. Thank you for your support and concern. It's much appreciated!
[hizu4ml] (score 9, diepte 0) It might be worth forwarding this story to the AMA to follow up with. He could be a sociopath posing as a dr to the degree that he is faking his qualifications.
[hiz9y9a] (score 8, diepte 0) Shame you didn't record the visit and conversation. That would be seriously eye opening for people who don't understand what so many with chronic pain deal with.
[hizqkii] (score 7, diepte 2) bruh i’ve had a lot of doctors say a lot of stupid things but the lack of basic anatomy and understanding of the body is just like how are they practicing???
[hj0i3ox] (score 7, diepte 1) Don't forget that if you're fat, it must be the extra weight causing the pain and keto/intermittent fasting will 100% fix it.
[hize684] (score 7, diepte 0) C’s get degrees and this guy is a perfect example.  Shoot. I think I’d find out what medical school he went to and I’d tell them what he said.
[hj00xxm] (score 7, diepte 1) Seriously. Anyone who doesn't believe that feet have joints shouldn't be allowed to practice medicine.
[hj000et] (score 6, diepte 2) Smart kid. Also yeah, so many docs assume that their first assumption is right and refuse to be corrected. Like what???
[hizh2v7] (score 6, diepte 0) OMG, I think I would have gotten up and walked out.  That Dr. is a nut, obviously, he must have mistaken you for a fish or something.
[hj0i2qr] (score 6, diepte 0) Please tell me you googled "joints in feet" for him 😂😂😂
[hj1y736] (score 5, diepte 3) I was told by a PA at planned parenthood that "periods are not caused by hormones"....
[hizian1] (score 5, diepte 1) Wait just a darn minute! I'm getting older, but I haven't made it to 65 yet, although I don't have periods any more. Taking all that into account - I suppose my doctor was completely wrong when diagnosing me with osteoarthritis? Sheesh!
[hiz6an1] (score 5, diepte 0) Some doctors are not worth the paper their degrees are printed on. This guy is obvs one of them.
[hizrhg3] (score 5, diepte 0) Lol.  Good luck and make sure you review him to try to warn others
[hj0nic6] (score 5, diepte 0) The joints between the tarsal bones of the foot are known as the intertarsal joints. The specific intertarsal joints of the foot include the subtalar joint, talocalcaneonavicular joint, calcaneocuboid joint, cuneonavicular joint, cuboideonavicular joint, and the intercuneiform joint.
[hj0k7bn] (score 4, diepte 3) So they can shout obscenities at your feet!
[hj0qtma] (score 4, diepte 2) Are you sure that a homeless guy didn’t hit your doctor over the on his way in and take his white coat and name tag? This has to be a joke. How the fuck do your toes bend. Do your feet have bendy bones in them? Honestly this mf should lose his goddamn medical license.
[hizytve] (score 4, diepte 2) I'm 29 and have been dxed with osteoarthritis since 24
[hj07bhv] (score 4, diepte 0) I can't stand patronising docs and specialists..
[hj1ipfy] (score 3, diepte 4 OP) And here I thought I had yelling at my feet and calling them nasty names down to  a fine art. Maybe they just need to hear it from someone else
[hj0t2we] (score 3, diepte 2) So clearly I have a purple ghost in my left big toe. How cute. All I ever wanted for Xmas!
[hj7e96d] (score 3, diepte 4 OP) So what, are they caused by little period fairies that show up and sprinkle period dust on your Uterus? I mean come on. Lol
[hj1n006] (score 3, diepte 3 OP) She amazes me everyday :-) 

Yep. It does seem like there is a large proportion of just that sort. They hear nothing beyond their own perspective and assumptions. Their pedestals are so high they've lost sight of the ground and everything outside of themselves is hidden in the clouds. Am I off base in saying that one who is as described above might be referred to as nothing but airhead? Hehe
[hj32stk] (score 3, diepte 3) Yup, the exercise thing irks me as well.  I know physical therapy can be helpful but it isn't always, and what works for one person doesn't necessarily work for another.  It's too simplistic for doctors to blame weight or lack of exercise when there are so many other factors that could be causing the problem.  Seems like doctors and other medical professionals who are willing to look outside the box are few and far between.
[hj0k9jo] (score 3, diepte 2) See:  Dr Ryan Santin.
[hj4euhj] (score 3, diepte 3) Idk, I've moved five times since my migraine started so 🤣🤣🤣. He also refused to believe I'd never had sex so he's a lost cause. As in *points at my partner who brought me in* "Yeeeah, riiight".
[hj1r74s] (score 3, diepte 2 OP) Seriously!? That's really bad. What type of person do you have to be to talk with someone who is suffering from chronic illness, with or without a lab backed diagnoses, and feed them the most far fetched shit you can pull out of your ass simply to hurt the hurting for the sake of your own ego? I guess one obvious answer would be a doctor. Lol. But seriously, on a deeper level. It's so... I dunno, sadistic might be one word that could be used.
[hj0sjme] (score 3, diepte 1) Power and money
[hj59xgs] (score 3, diepte 1 OP) It truly is. I don't think I'll ever go to the doctor again without recording it. This was essentially the straw that broke the camels back for me I guess. People need that serious eye opening so badly. I'm sure the majority of us have been experiencing the different perceptions, stigmas, etc which lead to shit treatment since day 1 of life with chronic pain.
[hj56p72] (score 3, diepte 1 OP) I am going to look in to this. I have no problem with doing whatever I am able to to try and make sure nobody else has to deal with something like this from him. He's dangerous. What I've said here is only the tip of the iceberg of what all was said and the way I was treated. So thank you for this. Any other ideas on further action I can take are very welcome.
[hj03x2k] (score 3, diepte 0) I would find a new doc that took medical school seriously bc there are definitely joints in the foot 😅 I've had an inflamed Metatarsophalangeal joint before and needed steroids and a shot + rest to heal it. I got it bc I went from working in shoes all the time to becoming pregnant and being barefoot at home for 10 months+ lol
[hj58jy7] (score 3, diepte 1 OP) Oh dear. That's just what you needed. And you're sure it wasn't just the flexible spot in your bone that was inflamed? Hehe. What is this thing you refer to as a joint?
[hj5kxt2] (score 3, diepte 2) Good point, my surgeon that specializes in orthopedics of the foot diagnosed me and I'm sure she was lying just to stab someone 😏😉
[hj1j50x] (score 2, diepte 3 OP) Gotta be the case. A whole episode of my feet in night vision. That'd do the trick for sure!
[hj4f92h] (score 2, diepte 4) Nope, but you would be being incredibly polite. I've got some, uhhh, **better** names for a few of my (ex) docs. Just because you went to school for a decade doesn't make you infallible. Yet so many develop God complexes.
[hj1ocyz] (score 2, diepte 3 OP) I would have to say that is completely plausible. In fact I hope that's the case and the real guy shows back up cus you're right, he should lose his license. Sooo crazy
[hj2ywm7] (score 2, diepte 2) It's mostly because they just don't want to actually have to take the time to do their jobs even though it would mean more money for them. They have a lot of biases and they just let them keep getting in the way without caring who gets hurt.
[hj38wuk] (score 2, diepte 3 OP) It's so sad. Kick a person when they're down, have been down for a long time, and are going to continue being down. I wish I could bring attention to the abuse which somehow led to some sort of reformation. I'm sick, tattooed and on disability though. Whose gonna listen to me other than all you wonderful folks?
[hj3bk0f] (score 2, diepte 3 OP) I'm sorry to hear that. You're so young to have to deal with that. Did you have to go through hell to get your dx or did you quickly find one of the good ones? If you don't mind me asking of course
[hj2z8pe] (score 2, diepte 2) Yep, just starve yourself and all the pain will go away. It totally won't cause more pain. /s

No, but seriously, I'm very small and doctors have still told me to just lose weight or "just exercise" as if being even more underweight would somehow help. Clearly 110lbs is actually obese. And for people who do have that issue for real, its the pain or disorder that's causing it, not the other way around.
[hj4g7zc] (score 2, diepte 3) I mean he also managed to graduate from medical school believing there is a magical timer in the brain that stops migraines. As in "It's impossible for a migraine to last longer than four days, 72 hours and not one second longer". Like a migraine doesn't stop just because too much time has passed, also those aren't the same length of time. And he argued against giving me IV magnesium because "it'll hurt the baby". Like dude, pregnant people are supposed to increase their magnesium intake you imbecile. Oh and "Pain is **NOT** an emergency". Like yes it can be, but also have you heard of this thing called dehydration? That can be caused by pain induced intractable nausea and vomiting? That is an emergency. 

My parents got the ego part covered. They only believe in diagnoses that can be tested for or easily seen. And by "tested" they mean labs and imaging. Lucky me, that means my vitamin D and eczema. Though ironically they don't believe in my low vitamin D, but do believe in my anemia. That I haven't had in a decade, ever since I stopped growing. And they definitely don't believe in mental health stuff (that they definitely don't lump being trans into, of course not /s).
[hj91wed] (score 2, diepte 4 OP) This guy did the same to me over my migraines! He asked how long my migraines last and how often I have them. I told him "they can last anywhere from 1 day to 2 weeks and I normally only get a break of 1-7 days in between if I'm lucky. I do still have a headache when I get break day's but they're not as bad." Is all he had to say was "No. That's impossible" and off he went on another tangent. I'm going 'hold on a second here.... It is possible because that's what I've been experiencing for the last year. There's these things they call Chronic Migraines dumbass.   


Really sorry to hear about your parents. It's hard enough when doctors treat you like shit about your reality. But family is a whole 'nother deal all together. One of the most freeing things a person can do is to open the paradigm they're operating out of to the perspectives of others. Somehow find a way, any way, to relate their own experiences to the truth of others perspectives in order to allow it to become a truth in their own paradigm. If you want, you can tell them that- courtesy of Mr. Tormented (Or even better yourself). Hopefully you aren't offended by me saying, and maybe you're already thinking this, I dunno.. But they are probably too far lost in their narrow mindedness to even be able to make sense of it.
(81 reacties met lagere score weggelaten)

