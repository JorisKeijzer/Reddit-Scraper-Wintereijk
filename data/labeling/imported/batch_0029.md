# Label-batch batch_0029

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
Schrijf het resultaat naar `batch_0029.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 8vqao0, ojg63w, ez7zu7).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 8vqao0 ===
SUBREDDIT: r/goodyearwelt
DATUM: 2018-07-03  SCORE: 93  REACTIES: 87
TITEL: John Doe Shoes Buy 2 Get 1 Free Review
POST (source_id=post):
Link to the Album: https://imgur.com/a/M7gvjlq

**Background & Previous Experience**

This is my first review, so here's hoping the links work right. I ordered these 3 pairs of boots from John Doe Shoes. They are MTO and part of a “Buy 2 Get 1 Free” deal. 

I was pretty impressed with the brown waxed flesh Starks I initially bought from their sample page. They don't quite look or age the same as my Nick's brown waxed flesh boots, and the leather is noticeably thinner. Still, the construction was pretty good. The only issues out of the box were the cheaper materials, a protruding piece of leather trim that I had to cut off the ankle, and some uneven points in the welt. I wear them to work constantly, and, aside from the apparently fiberboard insoles needing some odor treatment, they have held up well for the past few months. With my previous experience, I felt that it was pretty safe to try the deal. 

**Pricing, Turn Around and Shipping**

I was able to buy all 3 pairs for $475. The turn around time was right within their estimate of 6-8 weeks IIRC. I ordered these 3 pairs on the 15th of May, and I received them late last week. However, I had some concerns as soon as they were delivered. The shoe-boxes had just been stacked together and wrapped in shrink wrap. They didn't contain any shipping materials, and the boxes were totaled. 

**Materials & Construction**

I originally ordered the Harlow in brown shark, the 420 Brogue in brown waxed flesh, and the 420 Cap-toe in blue waxed flesh. However, the blue waxed flesh was actually out of stock, and I was allowed to change it to black shark at no extra cost. I ordered their formal, studded, and commando rubber soles. All of these pairs have a Goodyear welt. 

The leather is noticeably thinner than it is on any of the other shoes or boots I own. I can say from personal experience that the brown waxed flesh on my starks ended up wearing differently than my Nick's, and I really prefer the worn in look on the Nick's. I have no other experience with shark skin, but it is definitely thicker than the waxed flesh. It has a dry, almost cotton-like feel to it. The color is very dark and dull. I think the black shark is more attractive than the brown.

Aside from the leather, there appears to be some type of visible foam midsole that I assume can be removed and replaced with cork in a resole.  Also, it appears that the insole is fiberboard with a thin layer of leather stitched to it. This is not uncommon at this price-point in my experience. Still, I wonder how well it would stand up to excessive moisture or resoling. 

**Sizing**

I ordered size 9D, which is my Brannock. These boots appear TTS. I have somewhat irregular feet with a narrow heel, high arches and long toes. I usually end up with either a loose heel or insufficient toe room. It is rare that I have a good heel fit and enough room in the toe-box.  Around the foot, the JDS last actually fits me better than most. It is one of the reasons that I was impressed with their Starks. 

However, the ankle is very loose.  It occurred to me that the backs of these boots are fairly straight, unlike every other boot I own with a curve around the heel. With the laces tied tight enough that the tops of the shaft are touching, I am able to easily fit four fingers inside and touch my heel. As a result, the shaft rubs against the ankle while walking. I have no doubt this would be painful if having to walk in them over a distance. 

**The Good**

I was certainly less than pleased with the shipping conditions, but my initial reaction was good. I really admire the look of the black sharkskin in particular. Overall, they don't look bad at first glance.

For the most part, the welts look alright (except for what I note below). The staining on the welt and soles is nice. In particular, I like the look of the formal rubber with the darker break between the rubber and heel. 

The buy 2 get 1 free deal is also a positive. I was able to get 3 pairs of Goodyear-welted, MTO boots for just under $160 USD per pair, and they arrived on-time. Sharkskin at this price is certainly rare.

**The Bad**

The major complaints: At first, I thought that it was just the stitching that was slanted around the heel counters of the waxed flesh boots. After some palpation, I realized that the heel counters themselves are also crooked. They push into the sides of my heels a bit, and I would imagine I would blister pretty badly if I actually wore them hiking. There also appears to be some broken stitching between the welt and upper on the toe of one of these boots. The pull loops are also slanted.

When looking inside the boots, I noticed the cuts in the lining near the bottom of the tongue. On the black shark boots, a piece of the leather upper is sticking out and jabs into the foot. On the brown pair, there is another cut with some loose stitching. I also realized that the boot lining appears to be only stitched to the upper at the top, and the front is attached with adhesive. A bottom corner actually popped off when I ran my finger along the cut with the broken stitches. The adhesive appears fairly weak. I would imagine that the lining could become loose with the heat, friction, and sweat while walking.

The leather and pad that is glued over the rear of the insole was also done improperly. As a result, it is loose and billowy, and has bunched up to the side in a couple of the boots. It is uncomfortable to stand on as a result.

The minor complaints: There are several noticeable cosmetic defects, some of which I assume are related to the shipping conditions. There are some small abrasions, slanted and missed stitches, and crooked leather cuts on the upper. The shafts of 2 of the boots were initially pushed down into the boot, which caused them to wrinkle and stretch a bit on the side. However, the shafts also seem to be just a bit crooked. 

One of the toecaps on the black shark is shorter and not parallel to the other boot, which bothers me. The BWF has a toe cap that is slightly shorter, but this is barely noticeable. 

While I initially thought some of the residue inside of the shoes looks like dried gum, I later realized it is actually adhesive and dye that has been smeared on the lining. While I was not able to scrub it all out, I imagine that some acetone would do the trick (though I worry what the might do to the adhesive.) I also noticed that some of the nails aren't pushed very fair into the heels of the boots, but I'm not sure that this would ever become an issue. 

I also am not much of a fan of the brown shark. Unlike the photos on their site, it is actually very dark and dull.  I wonder whether or not it would be possible to bleach and re-dye a lighter shade of brown.

**Conclusion**

Overall, while some of these issues are pretty minor, I found the majors ones were enough to request a return label and refund. I do have to give JDS credit that they were willing to send me a label to ship these back to them (despite their no refund or exchange policy). While these are admittedly cheaper shoes, I don't see them as much of a deal. At this price range, you can find Allen Edmonds or Red Wing seconds with less problems. You'd also be getting full leather insoles, cork midsoles, thicker rubber soles, and sturdier leather. It is also just my opinion, but I can't help but feel that these look cheap the more I look at them. 



*Edit: Formatting*

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[e1ptmw1] (score 72, diepte 0) For anyone that missed it, OP and the owner of John Doe had an exchange [here](http://www.reddit.com/r/goodyearwelt/comments/8vj3gi/-/e1nter7) yesterday. Based on the voting it looks like everyone thought OP was full of shit and John Doe was being improperly attacked. After this review I have to say that the complaints were actually pretty restrained.
[e1puyhk] (score 47, diepte 1) Review justifies his comments. These look terrible
[e1pr7oc] (score 44, diepte 0) To be honest, after the last thread, I was prepared for this to be excessively picky or blown out of proportion. But this stuff is really not acceptable for any maker aiming to make good shoes, budget or not.

I hope JDS will take this as impetus to improve.
[e1qhj72] (score 35, diepte 6) Just some free advice... in situations like this, anything that you say other than "I am so sorry, we will fix this" looks really bad. 

I knew nothing about your company before today. Okay, you sold some crappy product. Sure. That happens. You're still trying to dunk on OP about some trivial Horween remark, though. It's just exceedingly amateurish. Exceptional value can only get you so far as a company - exceptional product, or exceptional service is what folks on this sub are looking for, I'd wager. You offer neither. Just get off your bullshit and make it right.
[e1pvfs2] (score 31, diepte 1 OP) Yeah, I honestly didn't think I was implying anything with the initial post. I thought the response was a bit harsh, and I can't say that I understand why.
[e1pxc6w] (score 31, diepte 2) > I can't say that I understand why.

Personally, the official account smelled like shit from the start. The classic bit about "not spending on storefronts, advertising, *influencers and ambassadors*" is such bullshit. It always means that's it's a brand new cash-grab social media brand. 

These kinds of social media brands really get-off and get customers with a combination of /r/murderedbywords and [the bullshit asymmetry principle.](https://en.wikipedia.org/wiki/Bullshit#Bullshit_asymmetry_principle) A link to their product gets posted, people start talking about it, someone (you) comes along with a scathing review, but without pictures. So the official account comes out of the woodwork saying you're basically full of it and all sorts of other marketing material. The product shots look pretty good and the prices are great so people are more likely to jump to be on the side of the company since it looks like you're out to get them rather than simply offering up your honest review of the products you received. 

It's why I hate all of these kickstarter/social media brands with a fucking passion because nearly all of them are built on lies and bullshit. "We don't pay for *influencers* or *ambassadors*" fuck off.

That's a pretty harsh comment but I have a real issue with brands astro-turfing communities like GYW like this brand is.
[e1pxys7] (score 29, diepte 0) Doesn't look like the owner has anything to say here..

Edit: good on you for not leaving it alone after that last post. I actually checked them out when j saw that link. Glad I didn't go forward after seeing these.
[e1q2a42] (score 22, diepte 0) Thank you for your contribution to this forum. It is experiences like yours that really help people out. This is what makes GYW so great.  
  
I can't believe the JDS rep could (presumably) handle these boots and make those statements. The exchange was grossly mishandled and this post is the final nail in the coffin.  
  
I work in an attention-to-detail trade and I need to feel happy to point at my work and say to myself 'I did that'. I would want people to WANT to use my work and feel good about it.  
  
But for a shoemaker, what could be worse than a customer refusing to wear your shoes? Not because of the design or materials, but because the craftsman was simply not good at what he does? How could a self-respecting *craftsman* create something like that and want to call it his own work, let alone *sell* it?  
  
I've defended JDS in the past because of the price point. But these are simply unwearable.
[e1pnpus] (score 21, diepte 1) IMO the massively uneven toe caps warrants a return, even for a $160 pair of shoes.

A defect that glaring would render them unwearable for me
[e1q39fp] (score 19, diepte 0) Please don't buy this garbage.
[e1q4nha] (score 19, diepte 0) Thank you for posting this with pics. This kind of thing is why forums like these deleliver value.

Every single one of these pairs is pretty bad.

I watched the thread yesterday with interest and also felt like the comment that got the down votes implied that they were dishonest about their leathers.

Then they attacked you and literally wrote that they suspected that customers damage merchandise to justify returns on unreturnable product.

They might be honest about their materials but that was horrible and looks even worse given these pics. Not ever worth a purchase IMO.

Edit: not saying all their shoes are gonna be bad, but you should not just get what you buy, but also believe in the brands that you choose to buy from
[e1pxw2y] (score 17, diepte 3 OP) Guess we will see if you're right. If this post suddenly gets bombed with downvotes, it makes the astroturfing accusation more believable. Still, I want to give the benefit of the doubt and hope that the owner was just having a bad day. Did have some pretty long blocks of implied accusations against me that were unfounded, though.
[e1pyb9c] (score 17, diepte 4) I just hate it when companies come in and try to start shit with people offering their reviews and thoughts. I don't think you said anything factually incorrect in either your comments or in this post but the official account felt the need to come out and basically say "no you're wrong we make good products" while peddling objectively false statements like "we use the absolute best quality leather for our uppers." Even in the product shots you can tell that's false. 

Add to that bothering to look through your post history and *their order history* I'd be okay with banning the official account outright.

Good on you giving the benefit of the doubt. Everyone has bad days but I still remember how this sub blew up when Brett Viberg threw some shade at Truman boots on Instagram. A company account (not a personal account like on IG) directly engaging with a paying customer to try and defend their brand is some serious bullshit imo.
[e1pieww] (score 14, diepte 1 OP) While I agree about the low expectations cosmetically, I can't agree when it comes to something that affects wearing them (like the slanted heel cups). Still seems to me like a better deal to buy the Allen Edmonds or Red Wings.
[e1q6xeu] (score 13, diepte 3) > Probably emphasized on purpose

I feel like the structural issues were underemphasized personally. Overall a pretty amazing set of three lemons. JD did give them a return label for what were final sale items, so credit where it's due, but that doesn't change shipping those out.
[e1q5nvq] (score 13, diepte 0) First of all, as I always say to the people who make reviews of our shoes here. Thanks for taking the time to write and post it.

Certainly, what happened yesterday was out of proportion and at one point I wrote that I was sorry if my replies were getting you some unwanted messages or hate, I was just trying to defend my company from the implication that we might not be using Horween leather, which was not true at all.

So, I'll start by replying to the review.

Those boots look bad, it's the first time I see the pictures and I can understand your disappointment, I have to own this mistake and offer you an apology for implying these defects you were claiming might not be true or even go as far as thinking some defects were inflicted by you. 

Two things happened for me to get to that point. It has happened in the past that customers damage the shoes in order to get a refund or exchange on footwear that wasn’t covered by a return policy like sample sale shoes. Secondly on the email there were two things that were really hard for me to believe a ripped lining and chewing gum. I was imagining like a really nasty cut in the shaft and real chewing gum, so when I read that, I discredited it. Nonetheless as the OP wrote we were quick to send a return label for final sale return merchandise, without any further questions or giving him a hard time.

Lessons we as a company have learnt and concepts we would like to clarify.

I have said it several times, we accept criticism, it pushes us to be better and this will be no different.

If you browse through other reviews, you ‘ll see it’s the first time we get defensive, we are very open towards customers’ claims.

We have a history with the OP, where he once wrote that we raised the prices when we launched the 3x2 deal, which wasn’t true, then implying that we might not be using Horween leathers and again it wasn’t true, finally the issue with the boots, which turned out to be true, but at that time I didn’t have the pictures. So, it was all stacking up to make me think, maybe this guy has some kind of beef with our company. 

The boots the OP got, do not represent what people usually get from our company. On yesterday’s post several customers wrote about how pleased they are with their John Doe Shoes, that’s what people get and that’s what we pursue. If you take the time to browse through the reviews in our website, you will find that unlike some other small companies with 6000 5 star reviews and like 2, 4 star reviews. We “have one star” reviews or two stars reviews. Because we post every single review we get, regardless of the number of stars and whether we consider it to be a fair review or not (we have got one star reviews because UPS left the package under the rain even thou the guy thought the shoes were amazing), it doesn’t matter, it is posted. Suffice to say that for every 1 or 2 stars review we have dozens of 5 star reviews.

Having said that, we definitely have to get better in our QC, I don’t want people to think of JDS as a gamble, like. Surprise! You got a perfect shoe or wow you got an unwearable boot. 

We aim to be a different company, now I see lots of messages bashing us as the typical make a quick buck company, an Instagram company, a “our shoes should be priced at one billion dollars but thanks to our direct to consumer approach you can get them for $199, no wait with code “summerishereyay” you can get them for $150” company. If you take 5 minutes to browse through our Instagram, our reddit posts or website you’ll find that’s not who we are. 

We re not trying to be another brand, as some have implied, we have always been transparent of what you are getting. We have never said ooh we are at the same level as this or that brand. We are improving that’s for sure, but there’s still a way to go. In the meantime, our proposition value is that you will get a good shoe with leather uppers that are not found at this price range. For some people that will be attractive for some others it won’t. And at the end of the day I do think we have a stellar customer service, maybe not the fastest one, but you get to speak with the owners and we are fair and honest people with whom it’s always easy to find solutions whenever there’s an issue, because yeah we make mistakes, but we don’t hide form them we own them, we get better and if possible we ask customers to let us right our wrongs.
[e1pwnsu] (score 12, diepte 2) It's difficult to tell how they were lined up, but I don't see how *anything* in that image of the toe caps is acceptable. The quarters are off, the toe caps are uneven and crooked, and it looks like even the tongue wasn't attached straight.
[e1pt14v] (score 12, diepte 0) I feel like I’m Whitney Houston in the movie The Bodyguard. But you saved me and this entire sub. 

I would lose my shit and seek mental help  if this happened to me.
[e1q2ol0] (score 12, diepte 1) Don't be buying any pairs. 

Might have to go after Grant Stone tho.
(68 reacties met lagere score weggelaten)

=== THREAD ojg63w ===
SUBREDDIT: r/goodyearwelt
DATUM: 2021-07-13  SCORE: 35  REACTIES: 81
TITEL: GYW FAQ: I have wide feet, help?
POST (source_id=post):
**What are GYW FAQs:** They are, you guessed it, frequently asked questions in the daily Questions Threads. The idea of these mega-threads is to get a lot of answers for everyone's benefit.

**Today's Question:** I have wide feet, what are brands that sell wide sizes?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[h51p9t9] (score 31, diepte 0) For the w i d e boys, listen up. Yes, I know those Carmina monk straps look incredible. Yes, those Carlos Santos wholecuts and Vass balmorals are unbelievably sexy with their chiseled toes and fiddle waists. You browse Standard & Strange, Division Road, Mr Porter, and other stockists who only stock D width. "What's this," you say. "A 30% discount, on shell no less. It'll be a crime not to buy it. I'd just need to go up a size to accomadate my fit." 

**STOP.** No, your fat-ass shovel-shaped duck feet isn't going to feel good in those. You're going to get metatarsal pain. Your little toe is going to want to fuse with the second last toe. Your big toe is going to get ingrown toenails. "Nice boots", your podiatrist says, "now take off your socks and let's look at those bunions."

This comes from a place of love. I've fucked up several times, baited by a good discount in the Weekly Steals and Deals. I know what it feels like to see posts on reddit/instagram/styleforum praising an almond last, then looking down at your pecan-shaped feet. So HODL. HODL for your dream MTO with custom lasting. HODL and learn a third language so you can communicate in Indonesian/Chinese/Korean for those *blessed* workshops to make exactly what you want. HODL for Grant Stone shell Brass in EEE. HODL for Wesco and their god-damned 6 month wait time and pray the summer wildfires doesn't destroy Eugene. HODL for the fit.

Anyway onto my recs. I'm brannock 10EE. Best fitting would be White's 9.5EE on 55 last.

**White's, Nick's, Wesco**: obviously. Though I do have to say that White's and Wesco MP toes might be iffy. Baker's recommended me 9F on MP vs 9.5EE on 55. White's also does a combo last for weirder shaped feet.

**Grant Stone**: Again, obviously. IMO their Leo last EEE increases the toebox height and heel width a tiny bit too much. This should be the #1 pick for wide-footed bois, esp with their free shipping and returns.

**Rancourt and Quoddy**: Comfortable because of the construction allows for a lot of lateral flexibility. Their EE is still too narrow in the toebox IMO, and widens the heel too much. But if I didn't get EE, the edge of my foot literally hang outside the edge of the sole.

**Red Wing**: 8 last on 10EE is pretty good. Moc toe and Chukka lasts tend to be narrow in the toe. This is to be wary of in other popular moc toe brands like Thorogood, Danner, or Chippewa.

**Allen Edmonds**: If you live in a city with their retail presence, walk-in and try on. They've got too many lasts to deal with. I have a pair of 10EE on discontinued styles that work okay.

**Meermin**: they ass

*A note on loafers:* I've tried many pairs of loafers over the past year. They've never worked out. Loafers wide enough for my toes basically leaves the rest of my foot free-hanging. Loafers that fit the rest of my foot nicely make my toes feel like they're being pushed into a cone with every step. For now I pray for my Wesco Romeos to fill the slip-on shaped gap in my heart.
[h51eh6x] (score 25, diepte 0) Oh this is right down my alleyway. 

If you're a wideboi because you're fat like me, I would say wide sizes can be helpful in a number of ways. I should note you should be aware that sometimes a wide last is only really wide at the ball of the foot, rather than adding volume overall to places where you may need volume, so it's always worth giving a shoe a try before committing to it (be sure you can return). 

Brands that offer wide sizes tend to do so in limited models and sizes (creating multiple wide lasts is expensive when maybe 10% of shoe buyers buy wide). I personally own wide sizes in Grant Stone (tend to be very generous given their stamped width - an E fits close to an EE, for example, but Leo and Alexander last can be a bit tight in the instep), Rancourt (tends to be TTS), Thursday (very limited selection), Canada West (extremely generous fit), and Danner. Other brands I know to carry wide sizes include Alden, Allen Edmonds, Red Wing, Parkhurst (602 last is E-width, they also have an EE width coming out). If you're looking for dress shoes with more generous volume I'd look towards British shoemakers that offer wide sizes (Herring, Loake, Church's, etc.), as some of their wide offerings can be very helpful for people with a lot of volume in the midfoot.
[h522vak] (score 15, diepte 0) https://www.reddit.com/r/goodyearwelt/comments/btngrd/the_wide_feet_guide_goodyearwelt_options_for_ee/

Going to leave this here and answer any questions.

Just FYI wide feet =/= fat. I am a ~~EEEE and am nowhere near overweight. It can, but also genetics plays a role. Your body type is a part. Multiple people I've talked to have gone up a width or two after years of backpacking.
[h521w4q] (score 12, diepte 1) I'm 53. I finally reached that point in my life where wisdom kicked in, and I'm never buying another pair of shoes that doesn't fit, again. Preach it, brother.
[h51ij84] (score 11, diepte 0) Red wing, Nicks, Whites, Wesco, Frank's, Truman, Rancourt, Quoddy, Viberg, Grant Stone, Yuketen.

There are also many manufacturers don't don't sell wide widths but have voluminous or wide lasts, e.g. William Lennon or John Lofgren.
[h51hiv8] (score 10, diepte 1) Wideboi? 

Not sure how I feel about that title. 

Maybe hefty horizontals? Wide waddles? Or (my personal favorite) MEGAtarsals? 

Funny enough Redwing is a brand my family supported for a long time. They were the only company to offer work shoes in wide sizes locally before the advent of the internet. As my family historically has wide feet the good sales folks always were friendly enough to kept stuff in stock just for my folks.

Edit: The last sentence didn’t make any sense lol.
[h53anst] (score 8, diepte 0) I just want to echo what others have said: DO NOT BUY SHOES TOO NARROW FOR YOUR FEET. 

On top of that, understand that your size will change as you get older and or add or subtract changes in your lifestyle. 

The biggest hurdle I had was variety. I really liked White's but I needed more 'adult' shoes for work and lifestyle. This led me to AE and Alden for oxfords. 

Don't settle and keep looking until you find what clicks.
[h52u44u] (score 7, diepte 1) No reason to spend $300-600 on a pair of shoes/boots that don't fit. The stretcher may not make them fit or it may damage the shoes. Then you're just left with a pair of shoes you can't return or sell.
[h539pmn] (score 7, diepte 0) I am E width in the toes but narrow everywhere else. Sticks for ankles. Narrow heels. Low instep. Real duck feet.


Finding lasts to accommodate my foot shape has been very challenging. I hope this helps some folks. The following lasts accomodate lower insteps, narrow heels and wider forefoot. Ankle room varies. For wider feet, look for E width and up.


* Alden 379X
* Alden Modified (has a higher instep though)
* Viberg 2020
* Viberg 2040
* Viberg 2055
* Whites 38 Swing
* Whites 55
* Whites 5050
[h53b5dz] (score 6, diepte 0) I'm a 15eeeeee in tennis shoes (new balance) Franks sized me at a 13.5FFF, baker's sized me at 13FFF but told me to go with Franks sizing. Baker's also told me to size up for bounty hunters, so I have 2 pairs of custom 14FFF boots on the way. I did the try on pair with 14FF and they were just almost wide enough. 

I saw some custom JK Boots that were FFFF width or wider on one of their videos, so there's that if you need it.
[h54bmxw] (score 6, diepte 0) OK does anyone deal with high volume feet? I did taekwondo for 10+ years and walk around barefoot a decent amount, so the calluses result in a really "tall" foot. I feel pressure along my instep typically, even when the width is accommodating.

Shoes that have worked in width but cause volume struggles:

* Viberg 9.5E was way too low volume, but the right length (possibly slightly short? But the toes didn't feel cramped or anything). Viberg 10E is ever so slightly too long, but still slightly too low volume.

* Carmina Llubi last, 9.5UK is the right width but also slightly low volume.

* Meermin HOK last, same story.

* Quoddy 11E and 11D are both more or less fine width-wise (the construction stretches to accommodate width pretty easily), but low volume. I can't use their insoles comfortably, for example.

Even most high top sneakers cause problems and require extensive unlacing before they'll fit (if they do at all).
[h51r8ln] (score 5, diepte 2) I've been trying to convince my dad to just pay an extra $50 for Red Wings over what he buys now for work to get a size that'll work for him instead of sizing up a bunch in other brands. He told me if I found a deal to just buy it and send it to him though, so maybe I'm convincing him.
[h51s3cr] (score 5, diepte 1) There is wide and then there is wide.  I have a 12F in Nicks/Whites, which means I haven’t been able to find a pair of Viberg/Grant Stone to fit me.  I have to stick with the fully custom PNW guys or Rancourt / Quoddy’s, although in my experience Quoddy’s are much more comfortable.  

So if you have wider than D, yeah this list.  But if you have very wide, or very high instep, it isn’t as easy.
[h51o3vm] (score 5, diepte 0) /u/rioc45
[h51wcaw] (score 5, diepte 1) I'll be honest if the entire answer to this FAQ was just tagging rioc it would absolutely be appropriate
[h51t1q4] (score 5, diepte 0) I'm 10.5E Brannock.  Comparisons have been made to Fred Flintstone.  I've lost count of how many shoes/boots I've bought that weren't comfortable or with which I've had to accommodate for width by buying a longer size, so there is a not insignificant expense having flippers like these.

This hasn't always been the case, but thankfully in the GYW world most manufacturers now make wider sizes.  Unfortunately, it's often made to order so there may be a delay before you receive them.

* Tricker's - This is the brand I've had the most luck with for in-stock, standard width footwear.  I have shoes of theirs on the 4444 (size 9) & 4497 (size 9.5) lasts that are plenty roomy for E-width feet.
* John Lofgren - M-43 boots (size 9.5), built on a Munson last, are comfortable in standard width.  Their combat boots aren't quite as much so.
* Alden - The Trubalance last (size 10E) is wonderful.  If I had my way, every GYW greenhorn would be required to buy a pair of Indy boots as an initiation into this weird hobby of ours.  The Van & Leydon lasts are both too narrow in E width.  These lasts tend to favor a more oval shaped foot.  My primary complaint about Alden is their system of using a combination last (i.e. E width forefoot, C width heel).  If I had my druthers, they'd use the same heel for E width & D width shoes.  As it is, when the forefoot is comfy, the heel is loose.
[h545fes] (score 5, diepte 1) Thank you!

I’m a a skinny as hell 12.5E. I’ve just started buying E if it’s available or EE from here on out
[h539bdl] (score 5, diepte 0) An option that I haven't yet seen mentioned mentioned: RM Williams 'H' width. Usually only on a few models, but pretty much every option if you order through https://bootsonline.com.au/ .
[h55pzau] (score 5, diepte 1) Are your feet cubes?
[h51zcf1] (score 4, diepte 2) As GenX, I hear Duran Duran every time I see 'wideboi.' It amuses me.

I would also say that, although they have limited full GYW selection, Florsheim has w and ww selections. The fancy boots don't come in it, but the imperials do. 

I just got my first pair of Allen Edmonds at EEE, and they might actually be the first pair of shoes I've ever put on that didn't hurt. They were wider, as far as I can tell, than normal- the blucher tops almost touch before lacing. (I'm never sure what's up with sizing, because a Brannock shows me as a C width, but there's no way I can put one on.) 

Wolverine World Wide has wide sizes for a good chunk of their lines- sperry, caterpillar, etc. 
Thorogood does too. Carolina Boots/Corcoran, as well. I've never found anybody who does a 4E with a steel toe, alas.

Finally, totally not GYW, but as GenX, I was very happy to learn that Vans makes a few styles in wide for the custom orders.
[h51hmtv] (score 4, diepte 0) i have been told I have 4e or wider feet. I have a couple pairs of custom fit Wescos. One pair is jobmasters for a work boot that i've had for a couple years. They are the most comfortable pair of workboots I've ever owned, and recently had them rebuilt. The other pair is their romeos.

For occasions where i need to dress up i have a pair of dunhams which is a New Balance brand. I doubt they are goodyear welt though.
[h52lpaz] (score 4, diepte 3) It does, but it isn't terribly wide in the ball.
[h529kd6] (score 4, diepte 1) I dunno, I have big dumb fat feet as well and I find Meermin's HOK last to be a great fit for me. I wear a 10.5EE or 11E in White's and 11 in HOK is great. The heel is pretty snug but there's tons of room in the instep and toe.

(unless you meant they ass in other ways)
[h51qxlp] (score 4, diepte 0) As a former fat guy who lost a ton of weight but not a millimeter of foot width, I can also co-sign my best fitting non-sneaker shoes are wide width Grant Stone, Allen Edmonds, Red Wing, and Ferragamo (not GYW but it’s worth tossing in for good looking loafers). I absolutely recommend Grant Stone. I absolutely do not recommend AE any more.
[h52qdsv] (score 4, diepte 1) I have to second this opinion on the Alden Indy. 

Funny enough those were my first GYW item. It opened a whole new world and established a high  bar for other footwear to meet.
[h522ebb] (score 4, diepte 0) Good tips here!  I would add that if you like vintage shoes - I do enjoy vintage longwings - then older Florsheim Imperials (like made in the USA 93602) can be found in E and in EEE, which are comfortable for wider feet  (I should warn you all to stick to vintage here...I tried on a pair of new Florsheim Imperials recently - made in India - and they were nowhere near as roomy...and the quality of the shoe was dodgy).  Also vintage Nettletons Traditionals (made in the USA) are comparable in quality and my pairs are even wider lasted than Florsheim.  I have a pair of Nettletons Traditionals that are sized as E but they are close to Florsheim's EEE fitting in terms of room in the ball of the foot.
[h51td17] (score 3, diepte 3) Maybe. Even a half step (or stumble?) counts as moving in the right direction!

In my family it was the other way around. My parents had to convince me. They did so with a discontinued pair of welted work boots decades ago. They became so comfortable and took tons of abuse and grew better looking for it. 

Man I miss those boots! Little did my parents know that pair started an obsession with handmade leather items.
[h52060p] (score 3, diepte 3) Congrats on finding a non-painful pair!

It’s a tough journey finding good sizing. The Alden Trubalance was that for me so I often try to use it to replicate fit. I think that’s what stalls me from going with boots said to be narrow or even ID makers who get talked a lot about lately. I just want a good comfortable fit. I’m tired of sore feet.
[h536gcv] (score 3, diepte 2) Ditto. Same for RUI, which felt even roomier for me (10E with high instep). Will be able to report on ROD soon (taking a gamble on the Chelsea shell MTO), should be same as HOK.
[h53dn5h] (score 3, diepte 1) Hello wide size buddy (ew that's weird). To add to this, the leathers not gonna stretch that much. Me trying to shove my duck feet in a D width hoping it will stretch to accommodate EE was a dark and painful point in my life.
[h52yuvy] (score 3, diepte 3) Comfort is kind. 

Build is starting to seem like prince or minister to me lol. 

My second was the Iron Rangers. Man those were tight at first. I had to break them in but if I were to buy another in the 8 last I’d go with E. 

The Alden Indys were SUCH a different experience. It’s ruined so many other boots for me.    Still don’t understand the neocork hate but different strokes…
[h544db9] (score 3, diepte 4) Half size down from Brannock is usually good for the Trubalance. I’m 10.5E & the 10D felt pretty good to me. My local guy recommended I go with 10E so that’s what I did. I wear my thickest Darn Tough boots socks with them.

All that said, Grant Stone is a good option too by all a accounts. I’ve never had any myself, but I’ve admired a number of things they’ve made.
[h5364f1] (score 3, diepte 2) The choice of shoes is very limited in the case you have wide or uneven (in width) feet, especially if you're not in the USA where they're more accommodating. Furthermore there's a great lack of testing opportunities for the shoes before you buy them so this further turns it into a roulette. In my experience shoe stretchers (quality ones) are quite effective and I wish I learned about them sooner.
[h545hxz] (score 3, diepte 1) Rancourt perhaps? Not the exact aesthetic, but their weltline or full strap loafers are much more refined than the usual beefrolls
[h54gr16] (score 3, diepte 1) Dear lord. Post pics when they arrive. O\_O
[h53d12w] (score 3, diepte 0) not specifically wide feet but The Vintage Future (he's on gyw somewhere) made a youtube video that will give you a boot fit spiritual awakening
[h547g72] (score 3, diepte 0) Canada West WM Moorby are wide. Mostly 2E I think. Work great for me, iron rangers would not cut it
[h58t0qf] (score 3, diepte 1) Hey dude wow you dropped some wisdom for me. I also did taekwondo for 10+ years. I knew it would contribute to having widebois but I never realized that it also messed up the volume for me too lol. So I hope someone with more experience can answer this for us lmao
[h52ljme] (score 2, diepte 2) I've heard the HOK last is really the only generous last Meermin has... but I'm too skeptical to gamble on it
[h52jq3q] (score 2, diepte 1) It sound like we have similar size feet, I wear a 10 EE on the whites 55 last and can’t wear rancourts comfortably. Do your self a favor and find a western store that sells Anderson Bean and try on a pair. I have broken in pairs of Whites and Nicks but Anderson beans are on another level!
[h540shl] (score 2, diepte 1) What about Alden Trubalance?
[h51pvwk] (score 2, diepte 0) I measure at 10.5ee heel to toe or, get this, 11.5d heel to ball. 

After years of toughing out okay-but-not-great fitting wide shoes, I switched to longer shoes, to much better results.

Basically: start with your heel to ball measurement. If you’re still wide, seems like most GYW brands can help you: Alden, AE, Grant Stone, Rancourt, etc.
[h52xj6e] (score 2, diepte 2) I wish they were mine, though if that were the case, because they're so comfy, I would have had more disappointment than I have in my subsequent purchases.  My first GYW footwear was, like so many others, the Iron Ranger.  I like my 8111s, but despite being the correct size they were never really that comfortable.

My Indy boots were significantly more expensive, a cost which I don't think is reflected in the construction or materials, but which is very much money well spent when considering only the most important variable: comfort.
[h530itp] (score 2, diepte 4) Agreed. I love them so much I’m considering a pair of snuff suede with the mini lug.

I’m 10.5E Brannock & after trying on at least 4 other pairs, settled on 9.5EE.
[h52r5c9] (score 2, diepte 1) Ditto here. Not fat and have wide feet. 

Most of my family are not fat, and a few members are skinnier than me but have wider feet.
(39 reacties met lagere score weggelaten)

=== THREAD ez7zu7 ===
SUBREDDIT: r/goodyearwelt
DATUM: 2020-02-05  SCORE: 113  REACTIES: 76
TITEL: Lasts for Duck Feet
POST (source_id=post):
I know I'm not alone in this judging from the number of posts and comments about it. I have low-volume Birkenstock-shaped feet with thin ankles. Sizing up for width makes the fit sloppy and loose, but [sizing for the right length and volume is murder on the toes](https://imgur.com/a/YQpuaf6). So finding the right last is important.

&#x200B;

Anyone with similar feet want to share their experience, to share and compare your favorite lasts?

&#x200B;

I'll start:

&#x200B;

The [toe shape of the munson last](https://imgur.com/a/xSXO5zO) fits well, but I need to use an insole and tongue pad to fill the extra volume. It has a broad, asymmetrical toe in the style of a [Birkenstock](https://imgur.com/a/3B4V5lo), but not as dramatic. The munson last has a little bit of toe taper on the medial side that compromises the fit just slightly, but makes it look a lot less weird than my [Altras](https://imgur.com/a/NUvdzYE). Here's a [top-down photo](https://imgur.com/a/dMutDpE).

&#x200B;

Viberg's curvy [1004 Cantilever last is a great fit](https://imgur.com/a/0a9vpgm) in both shape and volume. The elongated toe makes it look less blobby than the munson. [Top-down photo.](https://imgur.com/a/3DHtAqz)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[fglkl4f] (score 32, diepte 0) I've got similarly shaped feet and Alden's modified last is a great fit.

The shape is a little old fashioned and very rounded, but they're my most comfortable shoes.
[fgllejo] (score 12, diepte 1 OP) I expected the Alden Modified to show up in this thread. From what I’ve read, it sounds perfect for this foot shape. 

How would you describe the fit compared to some of the other lasts/shoes mentioned?
[fgllil4] (score 11, diepte 0) Yes, that's my feet as well, and I like this post. The cantilever last feels really good on my feet and it's a shame they added a whole lot of taper to it for their updated "2020" version. 

As for other lasts, I've only got ideas from oogling

* Not all munson lasts are executed in the same way. [John Lofgren's M43](https://i.ebayimg.com/images/g/41UAAOSw9zxeB5wt/s-l500.jpg) appear to have minimal toe tapering. [Another pic](https://eastwestapparel.co.uk/wp-content/uploads/2018/06/John-Lofgren-M43-Boots-Natural-Roughout-5.jpg)
* Heschung's [Odéon last](https://www.pediwear.co.uk/images/shoes/heschung/8943_alt2_oo.jpg) appears to be quite minimally tapered and is described as having a snug heel and roomy forefoot
* Two alden lasts that have already been mentioned
* Yuketen makes boots that are [described as being "semi-modified"](http://tum.is/tumgur/tumist/AgACAgIAAxkBAAMoXjqq3WQkJmFl8XpdFlMJ08CjW1wAAo2tMRuBZ9FJU7XzOZU-nsHJYMsOAAQBAAMCAAN5AAPy1AEAARgE.jpg). Not really sure what they mean by that, but it looks curved, but also quite long and narrow. Nevertheless I'd like to try.
* White's boots have a last the call the [swing last](https://pic.pimg.tw/frederic0713/1379763643-498433241.jpg), a type of munson last. [Here it is in a C-width](https://eastwestapparel.co.uk/wp-content/uploads/2019/05/Swing-Last-Semi-Dress-2.jpg) but you can get it in any width.

edit: Maybe /u/adrs1157 sizing [post contains some good](https://www.reddit.com/r/goodyearwelt/comments/7t1whc/manufacturer_last_sizing_thread_2018/dtcd9pn/) suggestion, including Alden 379x and C&J 365.
[fgloyld] (score 11, diepte 0) I have exactly the same problem (compounded by the fact I have very large feet).

The best luck I've had is getting a *combo* last custom pair of White's boots which are 13E in the toe and 13D in the heel (#55 last)

I just got a pair of cheap red wing 875s which are too narrow in the toes and I'm going to try stretching them and seeing if that's another route to take; it's research if you will.

Please don't delete this thread mods.
[fglm02j] (score 10, diepte 2) If you are in europe (a guess based on foot-shape and time of posting) there is a store in Paris that has a large selection of modified last Alden boots and it's called [Anatomica](http://anatomica.fr/souliers.html). I hope to go there some time...
[fglrjbc] (score 8, diepte 0) Alden's TB, and Barrie, and; Grant Stone's Leo all work for my duck feet. I would imagine Alden's Modified, White's' version of Barrie, and Viberg's new 2020 (based on the Cantilever) would also fare well. But of note, volume fitment is more so a patterning issue than a lasting one. Even on the same last, different patterns could have closer eyelet stays which would be bad for lower volume feet. Paying attention to that and going with a pattern with wider spacing for the eyelet stays should help with cinching down to compensate for lower volume without the need for inserts.

(edit: typo)
[fgmnw52] (score 7, diepte 0) A few of you have mentioned whites 55. Here’s a comparison between a 55 last and a 38 swing last. You can see in these pictures what a true duck shaped last is. The 55 certainly is not. 


https://imgur.com/a/n4YzVJh
[fgmhh3g] (score 5, diepte 1) Trubalance and Barrie for my wide toes :D
[fgluwqk] (score 5, diepte 2) Might determine this belongs in Questions thread. I second that this should stay up as a standalone post and be made a part of the compendium.
[fglzuyq] (score 5, diepte 1 OP) If:
- Your big toes press together (or overlap) when you stand barefoot with your feet together
- Your foot is wider at the end of the pinky toe than across the ball of the foot

Then you definitely have duck feet. If only one of those is true, maybe semi duck feet ;)

Most wide sizes add width across the ball of the foot, which isn’t helpful for me. Like you said, it just makes the fit sloppy. That’s why I want to find the right last shapes.

The munson last might be a good fit for you. It’s shaped like a work boot, but carries its width further forward so it doesn’t squish the little toe.
[fgo5nqd] (score 5, diepte 0) I've had a few beers and own a few boots in the popular lasts in this thread so I'll rank mine by most to least accommodating of my own wide + duck feet based on my experience.

1) White's 38 Swing Last 9.5EEE - as people have said and shown in this thread the toe box is bonkers big.

2) AE Higgins Mill - I went for 10.5EEE and they're actually really comfortable; I wear them to work all the time. I could probably fit 10EEE but I bought used

3) Red Wing Iron Ranger 8 Last 10EE - smaller toe box sometimes feels too tight, but only worn about 10 times

4) Red Wing Beckman 8 Last 10EE - ranked lower because mine are somewhat roomier in the heel than my IRs and fit me worse overall, but the toe box is fine

I just picked up some PW Minor Batavian boots for pretty cheap on eBay in 10EE (they arrived today actually!) and they fit really well at first with just enough room everywhere. Maybe by summer they'll be my new favorites.
[fglneae] (score 4, diepte 2) I don't think I have shoes in any of the lasts you mentioned, but it has more toe space and a narrower heel than my Truman boots, Wolverine, Alden Barrie or Tricker's.

It also has a narrow middle, which is good for my high arches.
[fgmibni] (score 4, diepte 1) Yep. Alden trubalance is hands down the best last for my duck feet.
[fgm30f3] (score 4, diepte 1) For some reason the C&J 365 last's taper hits my left toe.

No such problem in the same size on Heschung's Odeon last.

John Lofgren's M-43 works well for me; the toe area is very foot-shaped.

I have Yuketen's Angler Boot half a size too big but they're very spacious in the forefoot and round at the toe, very comfortable.

I'd add a recommendation for Heinrich Dinkelacker's Buda last (probably the best fitting last I've ever tried) and Rio last. Any Budapester is great for 'duck feet', with high toe walls and a round, spacious forefoot.
[fglqnx1] (score 4, diepte 0) Mods, can this stay up?

Some not-quite duck feet lasts: Vass P2, Red Wing 8, Viberg 2040.
[fglusfu] (score 4, diepte 0) I have similar feet. The Lofgren Combat Boot (custom last) & M-43 (Munson last) both fit well. Tricker’s 4444 & 4497 lasts both fit well in terms of the face-down, though volume may be a concern.
[fgmc63t] (score 4, diepte 0) There's two mentions of Red Wing's #8 last in this thread, which confounds me. I have iron rangers in 12 EE and they are still narrower then most D width boots. #8 is not for wide feet and definitely not for duck feet!
[fglu596] (score 3, diepte 0) Elston last. Oakstreet bookmakers use it in their trench boots. Roomy toe box without feeling like clown shoes.  I wear a 12EE in iron rangers an an 11.5 in OSB.

Edit - I got the last name wrong
[fglxqy2] (score 3, diepte 0) Thank you thank you for posting this thread and giving me some ideas
[fgly1je] (score 3, diepte 0) Alden Barrie and Modified, Carmina Detroit
[fgmgatq] (score 3, diepte 0) White's 38 Swing Last has been the best fitting last for my duck feet. It's wide in the toe box and starts to taper at the instep/waist/heel. I love the fit but it is not a pretty boot to look at. The toe spring is on the ridicules side.  

A few of you mention the Trubalance last but I disagree. It definitely has a wide and roomy forefoot but the toe tapers in width and height.
[fgmicc2] (score 3, diepte 0) This post bums me out. A lot of great options but most aren't available in EEE width.
[fgqvbwx] (score 2, diepte 3) I've been there. It's eye-wateringly expensive to the point going to New York and getting them there is cheaper.
[fgphcr7] (score 2, diepte 2) \+1 for modified last. I have v-shaped feet that are overall narrow (according to the Brannock device) but often suffer from cramped toe boxes. Meanwhile larger shoes don't provide enough support for my mid-foot. I just visited Moulded Shoe in NYC and was blown away at how well the Modified last fit. Very different from my other (even narrow-lasted) shoes. I normally wear Barrie-lasted 10.5C boots, and Modified 10.5C boots provided much better arch support.
[fglvb5c] (score 2, diepte 1) I don't think I've seen it quite clarified yet by Sambam or anyone else, only speculated upon, but I believe the "Combo" last that I've seen mentioned a few times is a last that they tack on leather pieces to change the width in a certain area.    


i.e. in your case they would use a full 13 D last and tack leather pieces in the toe to get extra width.
[fgm8h7g] (score 2, diepte 2) Mods be like, THIS GOES IN THE QUESTIONS THREAD!!!!
[fgm05tz] (score 2, diepte 1) ^ This is the right answer OP.  Oakstreet Bootmakers is what you want for duck feet.
[fglx0ti] (score 2, diepte 0) Alden Modified last will work - as others have said.  Depends on where you are based but those in Asia or EU are not cheap and you're looking at 1k for their shell models.

If you want a slightly different alternative that is tailor made for your foot, look at Officine Creative , especially - Anatomia 16.

This is slim in the ankle and waist with a wide flared toe / ball.  Does not look odd on the foot - great last.   Extremely comfortable.  Probably the most comfortable boot I own.  

Negatives depending on your view:

1) It's blake or Blake rapid (I can't tell diff) not Gyw although some models are supposedly hand stitched.

2) it's hand finished / treated.  This means no break in,  but probably also means these are not boots to go trekking in and won't take a beating.  They're  town boots if you like.

Sizing is odd.  I'm dead on a Brannock 10 and take euro 42 in these with toe wiggle to spare.

Edit should add you can often find them on sale at 30% discount at Italian online retailers.
[fgm0n12] (score 2, diepte 0) I had to give up on Viberg's 2030 last for this reason.  I have big wide toes, and there is no taper from my ball to my big toe like others.

I found Viberg 1035 works well for me.

Other lasts that work for me are Redwing 8 last (Iron ranger), Alden Barrie, Crocket and Jones 365 last (Islay).
[fgm59zu] (score 2, diepte 0) Have you tried Tricker's 4497S (Stow)? I would say it's slightly wider in the forefoot than Alden TB, and about the same fit at the heel.
[fgoz1v2] (score 2, diepte 1) I second this. Very accommodating last. 
I feel the English country type lasts are all (most) quite good for this reason.
[fgm88qm] (score 2, diepte 0) Only goodyearwelt shoes I occasionally wear are 
Allen edmonds strands in 8.5 EEE, and wolverine 1000 mile 8.5 (maybe 9)EEE

I hate my feet sizing.  not to mention I'm completely flat footed
[fgm9oqr] (score 2, diepte 0) Great write up! I'm still searching for a perfect last for bunions.
[fgmbuqj] (score 2, diepte 1 OP) Ouch—my condolences. The heartbreak of bunions is that once you get them, even the properly-fitting lasts that could have prevented them no longer fit. 

The only maker I know of that has a bunion-specific last is [Hanwag](https://www.hanwag.com/handcrafted-with-passion/our-special-lasts/).
[fgo1x72] (score 2, diepte 1) Rancourt or Venetian loafers?  They'll do larger/custom sizing.
[fgmfkpy] (score 2, diepte 0) I mean, doesn't *everyone* have duck feet? I'm not saying yours aren't duckier than average, but the Birkenstock is made to follow the natural form of the human foot. Most shoes squeeze our feet into an unnatural shape, which is something I try to avoid. A wide toe box is the healthiest option for anybody. 

I'm not a boot expert but I just want to make sure everyone knows Birkenstock makes boots also. Their stuff is nice quality but not the most fashionable at times.
[fgmh5al] (score 2, diepte 0) Alden's Barrie, Trubalance, & Modified lasts are definetely worth exploring for this foot archetype. I personally prefer a dressier/sleeker toe shape, so the Trubalance and Modified lasts arn't really of interest to me asthetically, but the comfort factor is there in abundance. Barrie is quite roomy and comfortable without being overly bulbous, though it is still a far cry from what I would call sleek.
[fgmi18o] (score 2, diepte 0) You're not alone, my Altra-wearing, duck-footed brother!  I run (almost exclusively) in Altra Escalantes these days.  I have a high instep, though.  Stuff that works for me:

**Viberg:**

* 2040: E width. Based on a Munson last.

* 2045: EE width. Fits similar to the 2040, but a little larger in every proportion.  Has some toe-spring.

**Whites:**

* 55 (AKA semi-dress last): This last seems to work for a variety of foot-shapes, since it comes in a variety of widths.  I find it to be comfortable.

**Zonkey:**

* Sailor: One of my favorite, most comfortable, and most attractive lasts.  I'd say it fits kind of like the Viberg Cantilever, insofar as the curvature and room for the big toe, yet it looks slim and elongated.
[fgmjksa] (score 2, diepte 0) I wear Altra trail runners and they employ a “foot shape” concept. It’s made a night and day difference for me. I know it’s not dress shoes but its worth checking out for your running/hiking needs.
[fgmkxlr] (score 2, diepte 0) Just get better feet, man.


Kidding aside, seems like the Trubalance last from Alden would work well. I don't have the same feet (I have really narrow feet) but it seems like Whites would be able to help you out here as well. They usually want a tracing of the foot so they can get it just right. Just spitballing here as well, but Viberg 1035 might not be bad, either.
[fgmqagx] (score 2, diepte 1 OP) Wow. Are the middle and right boots both 38 swing last?
[j3waatp] (score 2, diepte 2) My IRs are a D width but in a perfect world I'd probably want an E or EE. The heel fits well, but with how the midfoot+toebox fits I can't wear my thickest socks.
[fgmqwuw] (score 2, diepte 0) Thank you for posting about this. I have a the duck foot and have struggled for years finding the right shaped shoes. I recently got a pair of Allen Edmond's in 10.5 EEE on the 1757 last. Its still a little narrow in the toe box and I've had to add insoles to keep my heel centered as it wants to wiggle around too much. Overall this last isn't perfect for me but is better than 95% of the shoes I've tried in the last year.
[fsqrcco] (score 2, diepte 1) Not that I'm aware of, [Nick's has their #4 toe](https://youtu.be/xWESSPTU7TY) and Wesco has their [Boss/round toe](https://builder.wescoboots.com/images/catalog/BOOT_CATALOG.pdf). 

For what it's worth Wesco's Boss/round toe has been very accommodating for my moderately high volume duck feet and my Hendrik's with their MP toe is just barely enough with the insert removed; I unfortunately can't say the same for Nick's #3 toe which is a shallower/lower #4 toe.
[i988mxo] (score 2, diepte 0) I know this is an old thread but for those still looking, Jim Green in South Africa makes very wide, duck-shaped lasts. I have a narrow heel and super wide toe box and find the JG very comfortable. I think the shape might change as you get into smaller women’s sizes but for size 39 and above these are fantastically comfortable and not hideous.

https://jimgreenfootwear.com/store/rambler-vellie-fudge-crazy-horse/
[ksqe0ie] (score 2, diepte 1) >Companies just don't make footshaped boots honestly.

True dat.
[fgmzt6q] (score 1, diepte 2) Upvote for Buda :) best last for me along with trubalance
[fgna2og] (score 1, diepte 2) Quite possibly - there is a charge of $50 to get it done and I'm not sure if that involves a completely new last or as you say, adding strips of leather to a pre-existing last.

Either way, it worked pretty well.
[fgltvkz] (score 1, diepte 1) Why wouldn’t it be allowed to stay up?
[fglsef5] (score 1, diepte 1) A pattern can't adjust for volume at the ball, no? Unless we're talking about lace to toe boots. And definitely not the heel.

I agree that Trubalance and Barrie have minimal big toe taper, but I think the volume at the heel is more than most are looking for here. Leo may work for you but to me it's more almond than anything else.
[fglukq4] (score 1, diepte 2) Ah yeah definitely a good point, I guess I was referring solely to the instep. And yeah it's funny because I've read so many differing accounts of the TB, Leo, Barrie differences. To me, they go from Barrie -> Leo -> TB in terms of most tapered toe to least. And yeah that's also a good point regarding heel volume. All three lasts have narrow heels side-to-side, but depending on the pattern, they do tend to be somewhat bulbous in the fore-and-aft department.
[fglrr5r] (score 1, diepte 0) I feel like you're missing an opportunity to wear a boot inside of a larger boot?
[fgmcctm] (score 1, diepte 1) > Ellison last.

Do you mean Elston, the last used for the trench boots?

In that case, [here](http://1.bp.blogspot.com/-s-qL4SAGVHs/VPEBVJb0uWI/AAAAAAAABh4/Rh7B_cyOAyA/s1600/15_Feb27Oakstreet03.jpg) is a top-down profile shot of this last. It has plenty of taper on the medial side and that's not what OP is looking for.
[fgmgeu6] (score 1, diepte 2) Yep, sorry. I have the same feet as op and these are the only boots that don't hurt my feet. They do taper and narrow slightly but this is actually exactly what op asked for  "I have low-volume Birkenstock-shaped feet with thin ankles. Sizing up for width makes the fit sloppy and loose". The  other up side to the Elston last in the Trenchboot is their break in period is almost non existent. They were comfortable the moment i put them on and are my most comfortable boot 6 years later. I had the same problem as op, have been wearing boots my whole life. from cowboy boots to my standard issue combat boots. The OSB Trenchboot and Rancourt mocks are all I wear now.
[fgp1eyr] (score 1, diepte 3) If it works, it works! Can't argue with that
[fgm3pa3] (score 1, diepte 0) Alden Modified 

Alden Trubalance

Whites 38 Swing Last

Whites 55 Last with a combo configuration.
(33 reacties met lagere score weggelaten)

