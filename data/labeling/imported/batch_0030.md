# Label-batch batch_0030

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
Schrijf het resultaat naar `batch_0030.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 8qa8gk, btngrd, 3jnf28).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 8qa8gk ===
SUBREDDIT: r/goodyearwelt
DATUM: 2018-06-11  SCORE: 79  REACTIES: 68
TITEL: Meermin Chukka Shell Cigar MTO on feet
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[e0hnsdx] (score 31, diepte 0) Girlfriend: Um, so why are we doing this?  LOL, why?  Quit joking around.  I'm serious.
[e0hl1fs] (score 17, diepte 0 OP) Some people requested a on-feet picture, so I got my girlfriend to take some. 

Enjoy, and ask away about anything.
[e0htt5n] (score 17, diepte 3) They make a *lot* of ugly shoes.
[e0hvwe2] (score 16, diepte 4) Yes! Another opportunity to post [this](https://m.imgur.com/a/dvWBD).
[e0ht1t4] (score 9, diepte 0) Cool boots man. What a refreshing break from the bulbous red work boots that proliferate here.
[e0hm3q3] (score 7, diepte 1) Surprisingly I like the light wash jeans with the chukka. If you would have asked me without seeing it I would have said it wasn’t a good match but I think the colors look pretty good next to each other.
[e0hrz4h] (score 7, diepte 1) I know there's a lot of cross-over with MFA, but GYW isn't specifically a fashion advice subreddit. If it were, we'd all shun Allen Edmonds (I can't seem to find the pic right now sadly..).
[e0hxwgs] (score 7, diepte 6) Ha - not sure where the photo with jeans is, unfortunately. I keep this one saved in my Imgur account for emergencies.
[e0i1omk] (score 6, diepte 1 OP) Yeah this is pretty much how it went down.
[e0i9a2i] (score 6, diepte 1) > not have come from the men’s department

There's literally no need for this.
[e0ieuby] (score 6, diepte 8) I meant the "jeans aren't from the men's department" ""joke""
[e0hvo47] (score 5, diepte 3) They had an option to see shoes "with pants" and it was the worst thing fashion wise ever.
[e0hma7y] (score 5, diepte 0) Reminds me of the cigar shell on the Meermins I sold \-\- it's not the rich brown that you get from Alden or Enzo (Dark Cognac is their name).
[e0hrx5z] (score 5, diepte 0) Total cost?
[e0hlmft] (score 4, diepte 0) Nice shoes...but I honestly think those jeans are too tapered. Else a great fit.
[e0hsyga] (score 4, diepte 3) LPT: anytime you hear 'but' in a sentence everything before the but is meaningless
[e0i8nz6] (score 4, diepte 3) come on no need for this
[e0hq07x] (score 4, diepte 0) I usually love shell but this just lacks something. They seem nice and it's awesome that you like them.

To me, I just feel that a step up to high-end calf would be a better investment than this shell. An Alden, EB or C&J chukka in calf... 

Is this the italian or japanese calf?
[e0i5se5] (score 4, diepte 1) Looks fine to me. All the options you mentioned for calf are still a fair bit more than Meermin Shell.
[e0iwved] (score 4, diepte 1 OP) About 400Euro,or 475USD.
[e0ia6xh] (score 4, diepte 2) In addition, we do have some women here too...
[e0hruir] (score 3, diepte 3) I do, I was just making a comment in regards to styling since the commenter mentioned the overall fit as well
[e0hsy9v] (score 3, diepte 2) Why shun AE?
[e0i9v74] (score 3, diepte 3) I'd say it's a much more constructive comment than something like 'tight jeans are so 2015 bro'. If OP doesn't mind the particular effects that Nero pointed out, then there's no issue.
[e0j0zsk] (score 3, diepte 3 OP) Maybe I stated it wrong, its gotta be GMTO. Its for groups, sorry :(
[e0i98hd] (score 3, diepte 1) Funny, I'd consider Alden calf among the absolute worst for the price.
[e0iza48] (score 3, diepte 2) Really? I was thinking CXL though!
[e0iwt75] (score 3, diepte 1 OP) Italian. I think they are nice. Alden leather looks like it's too "business" look, I bought these to be used as a more causal chukka.
[e0iymue] (score 3, diepte 2) Then that's a perfect purchase!
[e0iwwls] (score 3, diepte 1 OP) Thanks. Too many boots...
[e0ie56s] (score 3, diepte 4) > It was a joke.

It's not a very good joke.

>odd people were slagging the guys jeans on a shoe Sub.

I agree.
[e0ifwbw] (score 3, diepte 0) Lol everyone chill, the taper on the jeans is fine...
[e0imhor] (score 2, diepte 7) The hero we truly need.
[e0iww5h] (score 2, diepte 1 OP) It might get better with time? Doesn't shell get a deeper color with time?
[e0iai9a] (score 2, diepte 7) I'm not going to have a debate about how much of a "knob" anyone is or isn't. I think that unsolicited fashion advice doesn't belong in GYW and will make a comment about it in the SOTS thread that's stickied.

I just want to talk about shoes.
[e0iecwl] (score 2, diepte 7) I never thought of his posts that way. I mean he loves to talk about his pants, but other than that oddity for the most I like his contributions.

Just like I think of you as the guy with the great collection of shell Carminas including those pair of natural bluchers/ derbies.

However, if I recall correctly you got into it with a bunch of people on the Alden x Standard and Strange thread about two topics, the value of Suede and the OP's objection to your assertion that Carmina was better than Alden based on the shape of the last and their design and made out those who disagreed into villains.

We all aren't perfect all the time. Not sure its constructive to try and shame someone into silence.

P.S. You should also get TSA precheck so you too can be frustrated when they make you take off your shoes at the airport. Happened today again. I hate it. Airport floors are so gross.
[e0iwntl] (score 2, diepte 2 OP) I respect your opinion, and I know the jeans are tight. 

I am at looking for other jeans, dark, light, and black, so if you know any brands and models that would fit me and my shoes, I would appreciate it.

I know cropped jeans are fashion and shit, but I'm not doing that.
[e0iyrev] (score 2, diepte 3) I would ask around r/rawdenim. They know how certain brands and their cuts fit better than me.
[e0iwdzn] (score 2, diepte 1 OP) Yes they are from the February batch. I didn't get anything on the mail from meermin, I got a text message from FedEx, with a tracking number coming from Mallorca...
[e0ielmx] (score 2, diepte 6) nah
[e0iwr5v] (score 2, diepte 8 OP) Are they really too tight or are they just not the right fit for these pair of shoes?  All the guys I see on r/goodyearwelt are jeans that are baggy and does not have a fitted look.
[e0j28t9] (score 2, diepte 9) Rock whatever jeans you want. If you are happy, that's what matters. Cool shoes.
[e0jqu9t] (score 2, diepte 0) I love my brown shell chukkas.  I feel like they are super versatile.  Enjoy them!!
[e0hx4k5] (score 1, diepte 5) Yes! That's one that I was looking for. Isn't there one with jeans as well? I can't seem to google-fu it.
[e0jgij9] (score 1, diepte 2) It should patina somewhat, but the rich brown of the Horween shell is not there in the shell Meermin uses.  They call it cigar to attract the customers, but it's not the same.
[e0i953d] (score 1, diepte 5) I thought the part of their comment relating to style advice was off-topic for this sub and I said so and downvoted the comment. 

I think there are ways to approach it without making sarcastic quips at people along the lines of "What a surprise you're back at it again."

Remember there's a lot of cross-over with MFA so I can personally see how style advice could inadvertently be posted, especially in an "on feet" thread.

FWIW I thought the original comment in this thread was much worse.

I just want to see pictures of cool shoes and for people to be excellent to each other.
[e0ig5m3] (score 1, diepte 9) I don't think our comments on the S&S thread as a whole are that similar though their initial content was. I pointed out that the price for Alden shoes has really climbed over the years and later added that it was far faster than inflation (and had closed the gap with Viberg). I stood 

I offered no judgement on the comparable quality if Viberg to Alden or the value of the material--and that was IMO was a subtle and important difference and led to their different outcomes.

FWIW, I also think the attacks on iNero are leading for people to upvote his comment.
[e0ig9lj] (score 1, diepte 10) I mean, great. I'll upvote the dude's comments too if he turns off the BS and stops acting like's he's gotta neg the entire subreddit.

(Also, this is random-- but my comment on "steep for suede" was entirely about my own value-judgement of a suede shoe based on how I wear shoes. My meaning was that for me, I'd never spend $SHELL on suede, and at $600, that's more than the price of a lot of good shell, so I'd personally never spend that much on suede unless it was some kind of incredible circumstance.

The fact that I called it "suede" instead of "AldenTM oiled roughout tanned hyperleather" was another funny detail people absolutely latched on to, as though if I couldn't tell the difference between an Alden specialty RO suede and "regular" suede then how could I possible comment on the price of the boot itself!?
[e0jr1l0] (score 1, diepte 11) As I said on that thread, I think people latched on to it because it made it sound like you were shitting on suede specifically, rather than making the point that it doesn’t carry the upcharge of shell.
[e0j11vm] (score 1, diepte 4 OP) Done :) asked on their Daily Questions thread.
[e0izbj0] (score 1, diepte 2) Really? I just assumed MTO meant single MTO with the extra fee (20 %? maybe) on top of the ~$360 Meermin shell cost.

Now that I think of it, do they offer MTO:s at all?

They look perfectly fine, I just don't see the drag for these as I do with higher end shell.
[e0hyb28] (score 1, diepte 0) Are these from February batch? If yes, when did you received them? Still waiting for mine... :(

Edit - nevermind. I checked you other post. Hope mine will come soon. Not even shipping notification yet.
[e0jbt82] (score 1, diepte 9) What are they, 511’s?

I have 511’s and they get a little snug in the calf. 

Not too tight. If I had to say, too light a wash for slim fit.
[e0jcekg] (score 1, diepte 10 OP) No they are some unnamed brand from Zalando, but I want to upgrade my jeans to levis 511, because they are a better fit than these.
[e0jcqz6] (score 1, diepte 11) The 511 Selvedge are nice. 

I bought a lot of 511’s when they were on sale. Really disappointed with the material. They’ve kind of put me off any jeans with elastaine in them. Not digging the stretch...although I still wear a couple pairs with stretch in them..502, 541’s.

I’ve been tempted to order some Bravestars or Unbranded. Not a lot of cash for a quality product. The slim straights look really good. 

I usually just stick to Levi’s though. 
501’s might be a bit too big in the leg opening for your chukkas though.
[e0j8kss] (score 1, diepte 0) Very sharp chukkas! They look great with your jeans, but with that sleekness I wouldn’t hesitate to also wear them with coat and tie - very nice. I’m sure they’ll only improve with age - enjoy.
[e0razap] (score 1, diepte 0) ID on those jeans? I dig that fit.
[e0rersi] (score 1, diepte 1 OP) Brand from Zalando, Pier One. Thanks man.
[e0hlnze] (score 0, diepte 1) Agree
[e0hsnf2] (score 0, diepte 2) What a surprise to see you here saying, "Not to shit on OP" and then doing just that.
[e0i8si6] (score 0, diepte 4) Isn’t there? iNero has a history of going into these threads and saying stuff like this as a way of “starting a discussion” when in reality it’s just thinly-veiled insults that have no place here.

Do you disagree? You believe his post on this thread is constructive to the OP?
[e0i9z02] (score 0, diepte 6) I do too.


The only reason I call out iNero is the dude does this shit in every thread and when you point it out, he plays coy and acts like he can’t understand how you could have taken offense at his obviously condescending BS and then turns it around and tries to make out you’re the villain.

At first I thought it was just my threads and it pissed me off to some degree, but now I see it in every thread the dude touches and it pisses me off. I see it literally killing off discussion in threads that are otherwise thriving because iNero will come in and be like, “Not to be a huge contrary knob, but you look like someone shit in your soup mate. Beautiful shoes if someone else was wearing them.”
[e0if65a] (score 0, diepte 8) Well it's interesting you remember it that way, because your comment about price was almost identical to mine (I know this because you posted first and your post made me think about the price of the boots myself and express a similar opinion) yet lo and behold, iNero called ME out (strangely not you) for harping on price (I said that the price was steep and that it was my opinion-- it still is) and then of course, as soon as that happened, every one of my posts got downvoted into oblivion and every post bandwagoning and calling me out, including iNero's got upvoted. He then went and claimed to have the same opinion as me (that the price was high) and called me out AGAIN saying that even though he had that same opinion, he didn't say it to be polite. Except he specifically quoted my posts twice, bolding the cost I pointed out as steep, as though I was being incredibly unreasonable to even express that idea.

You know what I do when I go into threads? Admire beautiful shoes and talk about them.

Point out the posts where I said the OP looked bad because of the jeans he was wearing or where I called someone out like an ass for not knowing "basic" knowledge-- you won't find them because I don't stoop to those lows. Go through iNero's history, on the other hand... Again, I wouldn't be pointing any of this out if it wasn't a pattern I'm seeing in every single thread. Like clockwork, I go into threads and see iNero talking down to people about their knowledge, fashion, and even subjective shoe choices, while subtly acting like he has the high ground and everyone should be secretly laughing at the cretins he insults.

At the end of the day, I guess it's too much to ask for people to treat each other with a very minimum amount of respect and I suppose, since his posts are getting upvoted, that the rest of the sub is fine with him calling out specific users and critiquing their choices and treating them badly.
[e0ie8ao] (score -1, diepte 5) It was an ok joke. Just ok.
[e0hovr6] (score -2, diepte 1) It's not about trends. Take a look at pic 5 and 6. The shaft of the chukka breaks up the smooth transition from the jeans into the chukka. If the jeans were less tapered, a smoother transition would obviously be seen.  

It also makes your feet look big and disproportionate. Not to shit on OP, but the details are where it matters.  

That said, if you enjoy the look, you do you.
[e0ieqx8] (score -2, diepte 7) Haha. Come on. 

You don’t see the irony in a bunch dudes slagging the guys jeans for being too tight in a sub about shoe appreciation?
[e0icqty] (score -7, diepte 3) It was a joke. 

Settle down. 

I found it somewhat odd people were slagging the guys jeans on a shoe Sub.

=== THREAD btngrd ===
SUBREDDIT: r/goodyearwelt
DATUM: 2019-05-27  SCORE: 233  REACTIES: 66
TITEL: The Wide Feet Guide- Goodyearwelt Options for "EE" Shoes and Boots
POST (source_id=post):
OH NO. You stare down at your squarish feet. "I don’t want to be one of those weirdos who needs an “EE” width. Why can’t I just be normal like all the “D's”?"

Bad news, you're stuck with ogre feet. Unless you want to practice [traditional Chinese foot cosmetics](https://images.chinahighlights.com/allpicture/2017/05/f7b6429be3a340a990ed8eab.jpg), you're going to want to toss on some xtra wide footwear. 

Fear not, while [square toed shoes](https://cdn3.volusion.com/ydufg.ytpek/v/vspfiles/photos/23201NAVYBLUE-2.jpg?1422442266) are certainly a fall back option, there are actually a ton of styles and lasts that are specifically designed to look good wide (Moc-toes, Trubalance, Munson last….)

Thanks to all who contributed to the drafting discussion: /u/tehphysics, /u/Renton97, /u/likeafox, /u/leochen, /u/WRCousCous, /u/overwatcherthrowaway, /u/jim_shorts, /u/woodyfromcheers, /u/todd_ted, /u/irbilldozer, /u/TightElderberry, /u/Sixspeeddreams, /u/PeterMus, /u/doorbell87, /u/iffjbguhg, /u/swatkins818 /u/ordinary_hazard, /u/honest_panda, /u/bgusty, /u/AwesomeAndy, /u/doorbell87, /u/rocketbrainsurgery, /u/ajd578 






_____________________________________________

**How do I *really* know I have wide feet?** ^((you're in denial)^)

* **Brannock Devices:** can be used as general reference. But in my experience, employees have sized me all the way from 8D to 9D to 8EE. The shoe sizes I wear range from 9.5 in running shoes to 8EEE in dress shoes, all the way down to 7.5F in some boots. So IME the brannock is a guideline at best.

*  **Trial and error.** Look for signs and symptoms that you need a wider width. 

 * When you take the shoe or boot off does it feel like circulation is returning to your foot? (far too narrow)
 * Do you have comfortable toe room but the sides feel restrictive? (try sizing down half a size but up in width)
 * Do your feet slide around while you walk but the width feels good? (too long but good width)
 * Feet that bulge out the sides of the shoe or boot? (too narrow) 
 * Feet that spill out over onto the welt? (too narrow)
 * Ask yourself, does this shoe feel tight on the sides but good in length?


_________________________________

**Why don't I just buy shoes a half-size bigger?**

Wearing shoes that fit properly means that the shoes are designed to flex in the same way as your feet, will last longer, and show more attractive signs of wear.

If you fully size up to get more width, you will also get excess space at the front of the shoe. It will feel weird, you risk heel slip, and trust me, it will bother you because I know you are a little bit OCD if you are reading a sizing guide for $400 shoes. 
__________________________________________________

**How do I know that a shoe fits?** 


* The most important consideration is that the widest part of your foot (across the ball of your foot) fit snugly and comfortably into the widest part of the shoe. 

* You shouldn't have a boatload of extra room at your toes, though a little is fine. As you tighten the laces (if any), the shoe should feel snug all-over and not just at 1-2 pressure points. 

* Look at the shoe on the [left](http://www.nlm.nih.gov/medlineplus/ency/images/ency/fullsize/22943.jpg) - it fits. 




**But what about all the awesome skinny pointed shoes I see?**


If you try to cram your foot into a sleek little pair of tapered boots (my feet are only spilling off the edge a little bit I swear!!!) you could risk damaging your stride and developing bunions over the long term.  No one wants [bunions](https://orthoinfo.aaos.org/en/diseases--conditions/bunions/). Again, forcing your feet into ill fitting shoes and you are increasing risk for [this](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Hallux_Valgus-Aspect_pr%C3%A9_op_d%C3%A9charge.JPG/300px-Hallux_Valgus-Aspect_pr%C3%A9_op_d%C3%A9charge.JPG)

Sorry, but some shoes just [won't work out](https://imgur.com/a/INbH4Z3). Don't worry, below are a curated, but **non-exhaustive** list of higher end boots and shoes for the "EE" crowd.

For additional buying options and more detailed descriptions, please reference the [BEGINNER'S BOOT BUYING GUIDE](https://www.reddit.com/r/goodyearwelt/comments/7qxy6p/the_2018_beginners_boot_buying_guide/)

______________________________________________________________________

**BOOTS**

***Sub $350***


* **Allen Edmonds** is a solid option on sale. Look to pay about $240-$300 for a new first quality boot. They offer EE width's on most boots, most notably the Higgins Mill. As /u/woodyfromcheers
pointed out, many of their models retail for higher prices. We recommend waiting for one of their frequent sales or checking out [Factory Seconds](https://www.allenedmonds.com/factory-second-shoes/).


* **Canada West** has some selection in of EE in the [Moorby line](https://www.canadawestboots.com/moorby)  and EEE Chelseas of the [Romeo line](https://www.canadawestboots.com/romeo)
Their boots are classic workboots, their quality have been compared to just a tad below Red-wings. Retail in stores mostly, but there are a few online retailers as well. -From /u/leochen and /u/overwatcherthrowaway


* **LL Bean** stocks most of their styles in wide sizes. [Moccasin](http://www.llbean.com/llb/shop/10587?feat=592-GN1), [Boat Shoes](http://www.llbean.com/llb/shop/46112?feat=2-SR0), and [Desert Boots](http://www.llbean.com/llb/shop/65710?feat=2-SR0) that are great for semi-casual wear. Their [Bean Boots](http://www.llbean.com/llb/shop/31179?feat=592-GN1) and [Chippewa Katahdin Boots](https://www.llbean.com/llb/shop/122211?page=men-s-katahdin-iron-works-engineer-boots-ii&bc=&feat=katahdin-SR0&csp=a&attrValue_0=Brown&searchTerm=katahdin) are also very highly-regarded around MFA and elsewear.

*  **Rancourt & Co** offering moccasin and standard boots, [goes as far as EE across much of their line](https://www.rancourtandcompany.com/men-s/boots.html), but they keep minimal stock - most options are MTO with 4-6 week lead time. Shout-out to /u/likeafox for finding these.


* **Red Wing Heritage** offers EE widths for a couple Iron Rangers and Roughneck models. EE widths will be limited in stock unless ordering directly from RW. The "D" width on these will generally run wide but some, like myself, still find it too narrow. Factor seconds in EE width will be limited but it is still worthwhile checking out [Sierra Trading Post](https://www.sierra.com/s~red-wing/mens-boots~d~137/).

* **WWII Impressions** has solid [boondockers](https://www.wwiiimpressions.com/products/694) available in EE widths. Not exceptionally wide but worth checking out. Limited availability so check with Customer Service before you order. Note, the buyer pays for return shipping if it does not work out


***$350-$550***

* **Dayton**: Canadian bookmaker most known for their service boot. Their service boot last is offered up to EEE widths. As far as I know only available from Dayton directly and will build your boot on order. On ordering, you are asked to send in foot measurements and tracing. This was spot on for me and my EE feet fit fine in their EEE sizing. Expect at least 4 weeks wait time.- From /u/rocketbrainsurgery

* **Nicks** **[Boots](https://nicksboots.com/)** very similar to Whites, is also worth checking out. Nicks works off your tracings too and sends you a try on pair if you choose that option.  

 * u/todd_ted tells us after being properly sized: "I didn’t realize how badly my Danner’s (10.5 EE, 610 last) fit until I got my Nicks (8.5 F, 11067 last).  Now it’s hard to wear all the the ok fitting boots I do have as my feet move around so much in them compared to my Nicks.  My second pair of Nicks are size 9 FF in the HNW last."

* **RM Willams** have a special [Tambo](https://www.rmwilliams.com/comfort-tambo/Comfort_Tambo.html?lang=en_US)  chelsea built just like the craftsmen but on a special EEE/EEEE last, Available on RM website and from most Australian online shops. - From /u/Sixspeeddreams

* **Russell Moccasin**- not sure where to put them price-wise. Their camp mocs are $250, hunting boots run $400-700, and they also do exotics. Mainly manufacturers hunting and casual footwear using true moccasin construction. They claim to be able to fit anything from AA to 6E. Fitting instructions can be found [here](http://www.russellmoccasin.com/fitting-instructions/)." - from /u/ajd578

* **Truman-** Offers EE widths on all their lasts custom made to order for no up-charge. While no longer a GYW favorite, still worth exploring. 



* **Whites** the holy grail for wide feet. [Bakershoe](https://www.bakershoe.com/) will give you a custom sizing if you mail them a cutout and your measurements. They are overwhelmingly *spot on.* Whites goes up to FF widths so if you leave square-shaped footprints, you are set. Will have a wait time of 4-6 weeks. if the boots need to be custom made for you. [Whites ordering guide here](https://www.reddit.com/r/goodyearwelt/comments/2bz0yv/a_guide_to_ordering_custom_whites_or_nicks_boots/). 

* **Quoddy** Famous old school handsewn maker that goes up to a EEE has sizing sheet, and they are accommodating in picking the right size and width for your feet.

**$550+**

* **Alden** has many wide widths available for boots and shoes. Look for boots made on the Trubalance (Indy and others) and Barrie last as those naturally run wide. If you are truly after an EEE width, you will have to order directly from an Alden store or The Shoe Mart. May have a wait time.

* **Crockett & Jones** has lasts such as [365- the Islay](https://www.crockettandjones.com/islay-darkbrown-scotch-grain) and [378](https://www.crockettandjones.com/last-guide/) that have generous width, instep and volume. Read about their lasts [here](https://www.crockettandjones.com/last-guide/) for more in depth details and a last that might work for you.

* **Carmina**  tends to run narrow but it has the Forest lasts and a couple options in EEE.
 * Quoting /u/Renton97: "In my experience, the Forest EEE only works with the little extra room of cordovan. With calf it's a no go for my EE feet."

 * /u/swatkins818: If you go to an actual Carmina store you can get help on how to order a specially lasted shoe to fit your feet. For example, I'm normally US12.5/13EEE and my Forest last from them would actually be: UK11.5EEE w/ extended instep & 2 half leather insoles under the last. Their Detroit last is roomier than Forest as well.

* **Edward Green** has the [202 last](http://www.edwardgreen.com/discovery/202-last) available up to G widths if you want to drop $1000+

* **Trickers** [4497](https://www.trickers.com/uk/stow-marron-antique-heavy-brogue-boot.html) last  is very accommodating of wide feet. Detailed write up [here](https://www.trickers.com/uk/journal/post/4444-4497-shoe-lasts). "Both felt wider than the widest Viberg lasts when I tried both on." - /u/TightElderberry


* **Viberg**  does not offer EE widths per say, but larger lasts. Check out their 2045 last and 1035 last. Look out for other retailers such as Division Road, and Lost & Found for more make ups. While Viberg does offer custom MTO events, as of May 2019 I recommend you do not do a custom MTO based upon the numerous issues I have read about and the price hike. 

* **Wesco** is very accommodating with sizing similar to White's, they also do full custom lasted boots for additional charge. Limited reviews and experiences are available on GYW, but feedback is positive.
_____________________________________________

**Dress Shoes** - *Note there will be some overlap here with the "Boot" section. Again, this list is far from exhaustive.*

***Sub $350***

* **Allen Edmonds** again is a solid option on sale. Look to pay about $200-$300 for a new first quality shoe. They offer EE width's on most shoes. Loafers, such as the Nashua, built on the 114 last are sized about half a width down. Very comfortable though. - /u/tehphysics

 * However, be sure to check the *last* the shoe is built on. For example, the Strand and Park Avenue are built on narrow shapes so an EE Strand is not going to be very wide. Some lasts, like the 73, will be a better fit. My 8EEE strands still only fit the same as a regular Red Wing boot.

* **Rancourt** has a good selection of [loafers and boat shoes](https://www.rancourtandcompany.com/men-s/ready-made.html](https://www.rancourtandcompany.com/men-s/ready-made.html) as well as some dressier shoes closer to $400.


* **Vintage Florsheim**  (v-cleats) are much sought after. There are numerous [resources](https://vcleat.com/buying-vintage-shoes/) online and they are usually available in EE widths. Your buying options will be Ebay and second hand markets.


* Other options recommended are the  **Bass Weejuns**, **Johnston and Murphy Deerfield II Tassel-Moc Toe**, and the **Florsheim Imperials Kenmoor**. /u/tehphysics reports good experiences with these shoes but I do not see them on GYW so it may be worth some exploring on your own. 





***$350- $600***

* **Alden** has a great selection of dress shoes. Again, look at the last and try on in store if possible. If you are truly after an EEE width, you will have to order directly from an Alden store or The Shoe Mart. May have a wait time. 

* **Carmina** Check out the [Detroit](https://www.carminashoemaker.com/mens-derby-shoes/derby-puntera-lisa-531-marron) and [Forest](https://www.carminashoemaker.com/about-last) lasts. Would recommend trying on in store if possible or confirming with customer service.

* **Crockett and Jones** Should have some wider dress shoe lasts. Their [lasts](https://www.crockettandjones.com/last-guide/) are explained here.



* **Trickers** offers the [4444 lasts](https://www.trickers.com/uk/catalogsearch/result/?q=bourton&order=relevance&dir=desc) in many of their country shoes.

***$600+***



* **Edward Green** is worth looking into if you are in the market for a $1000 pair of dress shoes. Start with the [202 last](http://www.edwardgreen.com/discovery/202-last) and work from there.

_____________________________________________________________

Thanks again to everyone who helped out with this. Any additional brands, discoveries, or questions, please leave a comment and I will do my best to keep this list updated!

*Rioc45 -May 2019*

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ep0c1q4] (score 19, diepte 0) Thanks for doing this. Having had bear paws all my life it’s been a struggle to find shoes that fit. This helps a lot!
[ep0ieov] (score 9, diepte 0) Viberg 110 last is also great for wide foots.
[ep17ciw] (score 8, diepte 0) Good guide if you’re in the US.  God help those of us in Australia - none of these brands are available (except maybe Carmina and C&J, but online only so you can’t try them on and return shipping is prohibitive). The Chinese foot binding is tempting.
[ep0j97a] (score 7, diepte 0) Another option in the $350-$550 range would be ZEB. They modify their lasts based on tracings and measurements, not sure how wide or big they can go but I have been extremely pleased with my pair as have others on the sub.
[ep0fwys] (score 6, diepte 0) Depending on where you need the width, I would say Rain EEE is actually a bit more accommodating than Forest EEE.
[ep0r34n] (score 5, diepte 0) I'm looking to for a pair of moccasins or boat shoes that I can wear without socks. My problem is that my feet seem to have a fairly narrow heel and instep/bridge but flair out at the ball and toes. I've tried some LL Bean mocs, but seem get bad heal slippage with anything wide enough to my toe box. Any advice on how to address this or what brands may be of interest for my foot shape?
[ep1lqwl] (score 5, diepte 0) Most UK shoes are a good half size wider than their European counterparts and offer a broad range of sizes

Herring is a good website with lots of good options at a mid price (church loake Barker etc.)

https://www.herringshoes.co.uk/search.php?task=search&sortBy=default&sortDir=desc&Brands%5B%5D=-1&Tags%5B%5D=-1&Colours%5B%5D=-1&Sizes%5B%5D=-1&Fits%5B%5D=3&sale_search=0&ns_keyword=&submit=Go

Also consider some of the online indonesian shoe makers who will work on your measurements aren't that expensive eg txture

Also worth noting width isn't a simple linear measurement really. Some people have feet wide at the toe, some wide at the arch, some high at the arch, etc. Different lasts with the same 'E' width can fit each very differently. For this reason trying them on or sending comprehensive measurements is always preferable to buying online based on a width letter only
[ep21pnb] (score 4, diepte 1) I totally agree. I have a pair of Grenson Wide Welts (plain black derby) as well as two pairs of the Triple Welt (pickled walnut captoe boot and black Scotch-grain long wing dress shoes).  I wear a US7 EE/EEE which works out to a UK 6 G. These are all Grenson One, made in Northampton. Super comfortable.
[ep11kak] (score 3, diepte 3) [Bureau Belfast](https://www.instagram.com/p/BrPwSQWnI5d/?igshid=2ure0dx70mlj)  and [Kafka](https://www.instagram.com/p/BqPgI5cjTJU/?igshid=1tq2jg4f0m5k9) [UK](https://www.instagram.com/p/BqPkkNAjmc1/?igshid=1knoztdo11qlp) normally stock 110 lasts stuff. They’ve sold out though because it’s out of season but I’m sure they’ll have more stuff again in the Fall/Winter.
[ep0x3tg] (score 3, diepte 0) Thursday also stocks wide widths in select styles for an even more budget option.
[ep0y5t7] (score 3, diepte 0) I can't believe that Grenson wasn't mentioned in this. They have three width fittings in their shoes and are absolutely perfect fitting with their half sizes. They do boots, shoes, dress and started doing sneakers last year. They have various types, some of which are made in the UK still, where the Grenson G:Two are made in Asia and are cheaper versions.  


I have many pairs of all different designs and styles from over the years, they do collaborations with other popular companies occasionally, such as New Balance, Private White VC and most recently Rag & Bone.
[ep10pzx] (score 3, diepte 1 OP) PM me a write up paragraph with the links and I'll add it with your mention
[ep15lkd] (score 3, diepte 0) Tricker’s 4497 & 4444 lasts are generous. I’m a 10.5E Brannock & have room to spare in both. I’m speaking of the standard 5 fitting, but you can also find the even wider 6 fitting from time to time.
[ep1pz2z] (score 3, diepte 0) I need the exact opposite of this post. I have narrow feet and it seems impossible to find something where my feet don’t roll around side to side as I walk.
[ep28xe5] (score 3, diepte 0) Can personally vouch for Canada west especially if in Canada. They're super comfy with literally no break in and fit my square feet so well. Better than any red wings I've tried for fit a d quality too
[ep0bfp4] (score 2, diepte 0) Shouldn’t Wesco be in the $550+ range? I’m looking at various stockists; Division Road, Ship John, Standard & Strange, Snake Oil Provisions etc and they can get into the $700 range. Is it significantly cheaper buying through Wesco directly than one of their stockists?
[ep0c2fq] (score 2, diepte 0) Opposite problems bro. I thought I was a D width until I could perfectly fit into C width and even B width !?!? I haven’t come across a A width to know if that will fit. 

Loafers suck like hell. Got low instep because of narrow feet. I either have to spill out of loafers and Chelsea (other than SLP) or have the heels dig into me. 

Anything remotely rounded, I’ll splash around in. The only thing that fits properly is narrow curvy lasts (which seems to be the “in” style at this moment). I mean I’m not complaining, but it’s an instant NO to most workboots and chunky traditional styles. Like I know by the toe shape this stuff isn’t gonna be a good fit.  But Pointy, chisel, almond, long .... it’s all good.
(62 reacties met lagere score weggelaten)

=== THREAD 3jnf28 ===
SUBREDDIT: r/goodyearwelt
DATUM: 2015-09-04  SCORE: 31  REACTIES: 64
TITEL: [Serious] Are these shoes even good for your feet?
POST (source_id=post):
This question is for guys who are conscious about their foot dynamics and have a keen understanding of what's actually good for your feet, what isn't, and what's popularized BS.

I'd like to buy a pair of 1000 Mile boots, but I'm worried because they just seem so counterintuitive to what I've been taught about foot health.

Anyway, here are my observations and questions:

1)The shoes I see here (And in-store) are initially extremely stiff, and appear to  become malleable only up to a certain point. Overrall, they still appear to be quite rigid. Is this not bad for your feet? Doesn't the shoe need to be an excellent mould of your foot?

2) Most leather are quite thick, and don't breathe well. My feet run hot, and this is an issue for me. I know it will be if I get a pair of boots. Is there anything I can do to mitigate this? Is there a specific type of leather I should be looking at?

3) The shoes are all quite heavy because of the materials used, and I wouldn't want to be dragging around more weight than necessary. Doesn't this lead to getting tired faster?

4)The front portion of my foot isn't on the ground, but remains curved upwards, following the shape of the sole. Isn't it bad to not have all parts of the foot firmly planted?

5) Do short heels affect the way we walk? I was led to believe that flats are the healthiest.

Thanks for taking the time to answer and please don't bash me. I'm not trying to troll.

edit: why would anyone downvote this?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cuqpyn2] (score 15, diepte 0) I'm gonna answer you fairly briefly here:

1) Shoes break in. Stiff is sometimes good because you get more support. A good insole will allow for an even footplant inside the shoe, beyond that maleability isn't a terrific necessity. Sneakers accomplish this by using soft materials right out of the box - sacrificing support for easy comfort. Higher end shoes typically have to be worn quite a bit to soften the insole and make it conform to the foot, especially in the forefoot.

2) The right socks are a necessity. I always recommend darn tough socks. Even then, you're right. Sneakers and stuff are more breathable by a small margin, but higher quality shoes that fit correctly shouldn't get super swampy with the right socks.

3) You'll get used to the weight, it has no adverse effects.

4) Your foot is supported by the structure of the shoe, not by the ground. The shoe acts as an extension of your foot, so you could theoretically stand on the point of a nail and still have your foot be supported in full. The sole doesn't need to be flat to the ground, and in fact I prefer it to turn up a little because then I don't scuff my toes.

5) Flats are very bad for your feet in comparison to a normal heel height. If you're young, you're subjecting yourself to back problems and collapsed arches in the future if you wear flats too often. Cubans are best in my opinion, unless you have flat feet.
[cuquw56] (score 14, diepte 0) Honestly this just isn't well studied, and pet theories roll through the footwear world every few years, almost always connected with a product someone is selling. I do think some current trends are a bit oversold, such as ultra-supportive orthotics (for people without a specific medical need), gel, rockered soles, and ultra-wide toe boxes.

My strategy is the same as my dietary strategy, and really most of my health-related decisions:

* Don't do anything that truly hurts - even a new boot break-in shouldn't be honest-to-goodness painful in my opinion. A little stiff at first, sure, but if you are in pain there is probably a fit problem.
* Pay attention to your body - Listen to the little things, knees, hip pain, back pain, etc. Don't obsess, but notice the differences day to day and see if something you are doing is causing an issue.
* Variety, variety, variety - I have many different types of shoes and change them up all the time. Some are flat, some have arch support, some are heavy, some are light. I mix it up to keep my body from getting a repetitive stress situation. Likewise, I use a standing desk at work, and through the day go from sitting, to standing, to perching on a drafting chair, to walking around, back to standing, etc. It really helps.
[cuqs72a] (score 9, diepte 1) Regarding turn up (toe spring):

That's a good point, and often a personal one. Some think spring is necessary, but usually it isn't. Bespoke makers often like very little toe spring as it is more elegant. Work boots tend to have more toe spring, especially if their soles are especially stiff (double, triple midsole + rubber outsole) since the forefoot may not have the strength to bend the thick leather. This allows the foot to roll and avoid injury or discomfort.
[cuqs1p9] (score 8, diepte 2) To see someone about an orthotic.

A heel is good, but you're going to want support to build up your arches.
[cuqqf6i] (score 8, diepte 2) This is a true statement.  When you let a shoe do the work for your foot, your foot will get weaker.  It's like that for any part of your body.

I had multiple pairs of the minimal workout shoes, and they don't have this stability from cushioning in the uppers, makes a huge difference in how strong your ankle and calf muscles get.

I think that arch support is always a good thing though.
[cuqqcvs] (score 8, diepte 0) From my understanding.... anyone feel free to chime in to correct me.

1) Breaking in the boot definitely takes some time.  Is that bad for your foot?  I don't know the answer from a medical/health standpoint, but as some one who is still in the process of breaking in multiple pieces of footwear... I don't think it is.  Most of my footwear has actually caused me little to zero discomfort (including a pair of service boots) while breaking in.

The shoe doesn't need to be an excellent mold of your foot, rather just the right fit.  Obviously the shape of the shoe (the last) will affect how it fits/feels while worn.  Some lasts are more generous in terms of how well they fit the average person.

2) I had the same issue, and a few things help with this.... 

- Get unlined boots.  Pretty simple, if there is another layer of smooth leather lining the inside of the boot, it will make it less breathable.  However, if it is unlined it can cause a bit more break (creases and such).  Unlined breathes much better though if it is a good quality piece of leather.  The vamp of most boots are lined to make them crease better.

- Wear anything but cotton socks.  Linen, wool, cashmere, alpaca... all these wick moisture and breathe much better than cotton.  Granted they are probably more expensive that cotton, it will help you tremendously throughout the day.  It's worth the investment and to wash them frequently than to try and stick it out with cotton socks day in and day out.  I wear only wool or alpaca socks with my Dayton's... would never consider anything else.  

- Wash your feet appropriately.  This is a weird one because most people don't really think about this.  I didn't until I started doing it for a while, and it helps a **ton**.  Make sure you wash your entire foot, between the toes, the bottom, the outside, everything.  Even better if you have some kind of exfoliating scrub or use a towel every few days to help shed some dead skin, that's what will build up and cause stinky feet.

- Let your boots breathe after you wear them.  After a day of wear (4+ hours for me), let your boots sit for about 2-4 hours without shoe trees in them.  This will let them air dry inside (your feet sweat a lot no matter who you are) and then stick shoe trees inside to help keep shape and pull out any more moisture.  The less moisture by your next wear the better.  I think an air dry plus ~ 6 ish hours of shoe trees should be pretty sufficient to get a pair ready for another wear.  I have no scientific evidence to back this up... it just feels right to me at this point.

- Avoid patent leather or anything with a super heavy gloss finish.  This will make leather less breathable too, but not really too relevant to what you're looking at.

3) 1ks actually aren't too heavy if my memory serves me correctly.  As long as you aren't very weak or walking a ton of miles, you should be fine.  You'll get used to it.

4) You won't even notice this.  It may change a bit as the shoe breaks in but it isn't adverse or anything.

5) I think the height of these boots isn't enough to have a serious affect on your health/posture/knees.  I know that a higher cuban heel can help with knee stability and arch support, but I'm not 100% on the true scientific answer here so I'm going to say it should be OK.  If you want a real answer to this, maybe ask your primary care doctor and see if he can refer a podiatrist for you to ask.  Or just email one if you have one.
[cur48c4] (score 8, diepte 0) 17,398 readers and not a single podiatrist?
[cuqrtm9] (score 7, diepte 1) 1000 miles have basically no break in. I wouldn't think of them as stiff in any sense of the word.
[cuqricl] (score 5, diepte 2) Think of it this way. On one end you have a cast. Placing the foot in cast causes the muscles and soft tissue to atrophy and weaken. You may have seen this if you have broken a limb and had it casted for any significant amount of time. Less usage of the muscle reduces the stimulus to grow. Muscles will continuously adapt to the stimulus provided and thus will hypertrophy (grow) or atrophy (shrink) dependent on the stress or lack there of. That being said, support such as arch support or a metatarsal pad can be necessary if there is a structural abnormality. Don't disregard the usage of arch support from fear of over-supporting the foot like in cast. Some people need arch support no matter how much they strengthen their foot, with all apologies to barefoot running folks. I did it for a year or so and couldn't sustain it. I had to humbly accept my need for significant arch support. Hope this helps.
[cuqs82l] (score 4, diepte 2) For someone who has only worn sneakers, I can see how they may find them rigid. The insole on 1ks definitely has little break in though. They do soften up as you wear though. Not a difficult shoe to wear a lot right out of the box though, I agree
[cuqrruo] (score 4, diepte 0) 5) I read Born to Run when it came out and only run in minimalist footwear.  Personally I feel that for *walking* this is much less a deal, esp. if you have the biomechanics down.  I've injured myself several times over the years from running with conventional running shoes, entirely alleviated by a change to minimalist footwear and consequent form adjustments.  I've never injured myself walking with heavy boots, even for miles per day many days in a row in an urban environment.
[cuqyzhk] (score 4, diepte 0) Speaking as someone with a long history of foot issues -

You're going to get different answers from different people. Some will say you need to have orthotics to support and properly align your feet in shoes. Others will say that going barefoot or as close to it as possible will make your feet strong and resilient. You can even find doctors that will argue either side, though most will land on the side of "buy supportive, cushioned shoes and wear an orthotic"

In the end I think the answer is "there are different answers... take care of your feet in whatever manner seems to keep them pain-free and healthy"


That being said, here's some personal opinion from me: barefoot isn't a practical lifestyle for most people, but keeping your gait as natural and uninhibited as possible is probably healthy. If your boots don't make your feet or knees hurt, it's probably fine. If you're starting to experience foot or knee pain, try an orthotic. And don't just ignore it if it gets worse; see a doctor and do your own research/experimentation to find solutions that work for you.


To directly address your questions - and this is just my opinion -

1. Stiff is supportive. As long as it bends where it should (along the top of your foot, above the ball) without cutting into you (a sign of too much room in the boot), it's better than a shoe which will twist and squish and not support you.

2. This sounds counter-intuitive, but try it: buy wool blend socks. Not even super thin; normal/medium thickness. Wool blend socks will keep your feet dry and happy. I had thin wicking bamboo fiber socks, and my feet always felt sweaty. I switched to wearing my wool blend socks (which I wear during the winter) during the summer and my feet felt COOLER AND DRY. 

3. Sure, but you'll probably only feel that after several miles... and if you're walking that much, a boot like this probably isn't the best choice anyway.

4. I think flat angle, parallel to the ground is healthiest. I start cramping up and my achilles starts hurting when I wear shoes with heels in them like boots. It may just be my crappy feet but I do agree with you here.

5. Same as above
[cuqrc13] (score 3, diepte 2) i am generally a proponent of being barefoot, but it depends on what you're doing and what your fitness level is.  if you're 20lbs+ over ideal weight (as most americans are) and standing/walking and carrying things off and on for several hours a day, you probably want support.
[cuqrlgl] (score 3, diepte 1) > buy a pair of orthopedics

Definitely an option.

> should just go barefoot all the time

Get out. /s
[cuqzcdx] (score 3, diepte 3) I'm not sure that humans evolved to walk barefoot on concrete and asphalt all day, however.
[cur4zk7] (score 3, diepte 2) > My plan is to get a pair of 1Ks for when I go to school / to use in the winter

Unless you plan to add topy (thin rubber glued to the sole), W1K's soles are leather which is not really recommended for winter. Well, it depends on what kind of winter tho, but if it snows or at least wet, leather sole is not really suitable for winter.
[cus0zlq] (score 3, diepte 0) I like GYW shoes for their quality and looks, but I have been reading around recently about foot health.

I found these two articles by W. A. Rossi to be rather interesting:

https://nwfootankle.com/files/rossiWhyShoesMakeNormalGaitImpossible.pdf

https://nwfootankle.com/files/Rossi-FootwearTheprimarycauseofFootDisorders.pdf

I'm no expert, just a regular guy. Here are my thoughts on your questions...

1) Most shoes will need a breaking-in period, especially GYW shoes. Even after breaking in though, the GYW construction still makes it inherently stiffer. It also depends on how supple and thick the uppers are too. A construction with inherently less stiffer construction would be Blake/Mckay/Blake-Rapid constructed shoes. I'm not sure if stiffness is a good or bad thing generally, but you have to find a stiffness that you can tolerate. One situation I can think of where stiffness is beneficial is in hiking/mountaineering boots where the user is likely to put heavy loads onto it.

I would presume that a good shoes should match the 3D shape of your feet  - the closest you will get is with bespoke. Some people like the fit different though, so you have to account for preferences. I think I saw a video once (may be from GJ Cleverley) about how their clients have different preferences to how the shoes fit and feel.

One thing that I have noticed is how most people have shoes where the insoles does not match the shape of their feet. Try this: draw around the shape of your feet under load on paper. Now trace the shape of the insole of your shoes on paper. In many cases the shapes of the insoles are smaller than your feet, forcing your feet to be constricted. The articles above talk about this. I thought it was interesting as my wide feet are particularly intolerable to narrow lasts.

I recently brought a pair of wide fit Anatomic shoes - okay, they are ugly and not GYW, but they are the most comfortable shoes I've ever worn for the past few years. They were so extremely flexible, but at the cost of structure. 

2) Start off with the socks you will wear the most with your boots - try thinner wool blend or just full on merino sock. I use Smartwool PHD socks for casual wear in both light and ultra light weights. Wool manages moisture better than cotton.

Maybe look at shoes without linings - but this may affect comfort and structure of the shoes. In my opinion, don't worry about whether it has linings or not as most boots and shoes do have them. Just make sure the leather is breathable and not treated like patent or coated leather.

3) I think it generally does make you tired faster.  In backpacking, it is a commonly thought that a x amount of weight in footwear equals something like 5x of weight on your back. This is more of an issue if you wear the boots for a long time. This is why backpackers and hikers have a new ultralight philosophy now. For casual wear, it may not bee too much of a problem. Have a variety of light-heavy shoes to rotate in your collection.

4) I don't know enough about this to comment. Maybe it is related to "toe spring". 

5) I have an elementary view that flats are the healthiest as well as there is no heel lift - which means your body does not have to compensate for the change in angle to your back or whatever. The articles above by Rossi talk about this in detail which is interesting. 

Most footwear have heels though. I am still not sure what to think about this. I have an open mind and I am getting to know more about the zero-heel lift/minimalist/barefoot options as well.

At the end of the day, I think that whatever advice people give you, just do what works for you the best. It may take some trial and error, some research, compromise, or further advice, but you know your feet and body better than most people.
[cuqq65z] (score 2, diepte 1 OP) Thank you very much.
[cuqqctd] (score 2, diepte 1 OP) So, I heard (mostly through the neo-barefoot-running community) that too much cushioning and arch support both weaken the foot over the time. What are your thoughts on this?
[cuqsjsn] (score 2, diepte 1) The advice on #2 is spot on. Very in depth.
[cuqt517] (score 2, diepte 2) Thanks, yea it was a problem for me and it drove me mad. On top of that, soggy socks and feet are high up on my list if pet peeves.
[cuqsidy] (score 2, diepte 2) You'd certainly get a lot of people saying "WHAT ARE THOSE?" if you did that.
[cuqt3em] (score 2, diepte 4) Not OP, but here's a pretty good source: http://www.barefootrunning.fas.harvard.edu/
[curjdyz] (score 2, diepte 2) Two things, a low heel-to-toe drop and a thin sole.  For me, the drop is more important for foot mechanics than the thickness of the sole.

In the 70s, thick heels were added to running shoes which promoted heel striking.  This is a less efficient form or running, but people did it because the shoes allowed for it without it being obvious that it was wrong.  

I like 4mm drop in my shoes, but I've done 0mm.
[cut6ga7] (score 2, diepte 2) This definition varies but probably starts from a modern racing flat to the more minimal Vibram Five Fingers variants (espoused in the book quoted above) at the other end.  I personally run in something called a Merrell Vapor Glove (http://birthdayshoes.com/merrell-vapor-glove-2-review).
(39 reacties met lagere score weggelaten)

