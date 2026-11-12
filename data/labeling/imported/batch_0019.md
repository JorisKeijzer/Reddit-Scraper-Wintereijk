# Label-batch batch_0019

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
Schrijf het resultaat naar `batch_0019.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: tt6cgn, bdipgq, 6xv979).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD tt6cgn ===
SUBREDDIT: r/goodyearwelt
DATUM: 2022-03-31  SCORE: 145  REACTIES: 74
TITEL: PSA: John Doe Shoes are not using full leather insoles/footbeds
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[i2w3snw] (score 79, diepte 0) Do they advertise that they're using leather insoles?

If not then this shouldn't be a surprise. This is a company offering a 3 for two deal on shoes coming out to what... $150 a shoe?

Not a shocker. You get what you pay for.
[i2vtcqu] (score 68, diepte 0) I suspected more corner cutting than what was on the surface
[i2w6lw0] (score 42, diepte 1) Don’t be a dick. This post is more interesting than the millionth “look at my new and unique chromexel 2030 service boots”.
[i2wpk8d] (score 37, diepte 2) I love dredging up ancient goodyearwelt history and [this thread](https://www.reddit.com/r/goodyearwelt/comments/8vvbo7/our_brief_side_of_the_story_and_an_insider_view) and the comments made by JDS on every review at the time that was being posted was a fantastic dumpster fire to read.
[i2vufgm] (score 33, diepte 1) Yea I can't say my impression of JDS is good from all the posts here. They're always mostly positive but all I see are sloppily made shoes that come in beat up packaging so that not even the first impression is good.
[i2w27mh] (score 29, diepte 2) Do they advertise full leather insoles? I've never seen this be an actual issue tbh other than various internet self-flagellation about "quality" and "cost cutting".

Any place that does a like "buy two shoes get 3 free" or whatever their sale is is obviously not pursuing the pinnacle of "quality" as defined by internet shoe ~~degenerates~~ nerds.

I remain unconvinced until someone can really show that these insoles are truly a worse wearing experience.
[i2w79bh] (score 29, diepte 1) Seriously. You usually get what you pay for in life. 

If it was Viberg or Gaziano and Girling doing this I would be surprised.
[i2wakey] (score 28, diepte 2) The 3x2 deal is almost the epitome of quantity over quality. 

Back to the lack of leather insole I really don't see how anyone should be surprised either. 

JDS don't advertise leather insoles. In a further comment it's mentioned that Stridewise said in a video that they use a leather insole. With his previous track record of information, I wouldn't trust if he meant a leather topped insole or leather heel pad. Especially when the term 'insole' is constantly used in exchange for sockliner/heel pad/insert instead of the structural insole these types of shoes and boots are made on.
[i2wbmo4] (score 24, diepte 2) lmao, 2030 cxl, name a more iconic post

wait Grant Stone Diesel lol
[i2wck0m] (score 23, diepte 3) Stridewise also said Grant Stone "cut a corner" because the heel cup isn't two full layers of leather. They don't really know anything.
[i2vqfwz] (score 21, diepte 0 OP) I was planning on converting my JDS boots from single leather to double leather because I felt a lot of ball of foot pain while wearing them. While the job was happening, my cobbler noticed something funny about the bottom of the footbed and asked me if he could do some exploring. I got curious because a couple of YouTube videos gave me the impression that JDS used a full leather footbed but the blake stitch made little sense other than to secure the gemming which should be replaceable. I obviously gave the go ahead and to my surprise the footbed is made of a thin ~~1.4mm~~ 2mm liner and a 3mm fibreboard.

PS: this is also a post to flex the new Amarettos from the Viberg SS.

Edit: JDS have never clarified on what they use for insoles. When asked about the blake stitching they have never revealed that there was fibreboard.
[i2xw17m] (score 20, diepte 4) i will never forget the moment he crowned Thursday his Boots of the Year....
[i2y1x1r] (score 18, diepte 5) I actually appreciate hi$ hone$t and unbia$ed boot review$.
[i2w7c9i] (score 17, diepte 4) > you can pay the same price

Ehhh I dunno about that. Grant Stone's cheapest models come in at around $300, whereas with JDS you can get three pairs of their calf or suede MTOs for almost the price of one pair of Grant Stone Diesels. Indonesian makers aren't getting any cheaper over time either, and the only way you're getting close to JDS prices with Indo makers is if you pick one that's not super well-known, and you're picking local leathers unlike with JDS. 

I'm not the kind of person that's interested in JDS either but JDS exists in a space where you want to build a collection fast and cheap, and I dunno if any other company really offers that, not at the price they do.
[i2vvpx6] (score 15, diepte 3) Yea, with the Indonesian scene and Grant Stone,  you can pay the same price without all the concessions to subpar finishing and general aesthetic refinement. I'd love to give Jakkrabbits a go and get that exact green roughout make up that was posted here a while back. That pair was just beautiful.
[i2vuze0] (score 14, diepte 2) The box I received was okay and the finishing was mostly neat enough to not mind at the price, but for the mistakes they made with my slightly customized order I’m confident I could get much more customization and what would be considered customer service at all from an ID maker like Jakkrabbits
[i2wifx4] (score 14, diepte 3) No one is arguing with you on that dude, I just told you to be nicer. I think OPs post is interesting. I wish this sub had more construction/breakdown posts. If you don’t have anything nice to say— don’t say it.
[i2waic3] (score 13, diepte 3) OP just wanted to let people know that they don't actually use full leather insoles as claimed elsewhere... nothing wrong with that lol
[i2wgphc] (score 12, diepte 2) A company that does not advertise full leather insoles/materials and is offering a 3 for 2 deal for rock bottom prices for welted shoes construction is doing exactly that.

What. A. Shocker.

There is no misdirection or shady tactics there, it's just people having unrealistic expectations and little knowledge pretending to have more.
[i2wb2mn] (score 11, diepte 5 OP) Well I'm doing a service clearing up misinformation. Why pushback a post that corrects information?
[i2wegq6] (score 11, diepte 7 OP) If one man's anecdote was the universal experience there would be no science. Fibreboard fails, it's a fact. Hundreds of resole videos have crumbled fibreboard heel stacks and insoles, cobblers hate replacing, it falls apart. I don't get why this is the hill you want to die on.
[i2xfq49] (score 11, diepte 0) I think this is useful information, but I’m also not surprised. Unless you’re paying at least twice the price, I wouldn’t expect leather insoles. Unless any brand is advertising as 100% leather insoles, I certainly would expect fiberboard.
[i2w3m0w] (score 10, diepte 1) Ha, I actually reached out to JDS a while back to ask about that stitch line on the insole, and was told that it was just to secure the gemming. I suppose that may be true, but only partially. I guess the other purpose is clear - to adhere the fiberboard!
[i2w6f9l] (score 10, diepte 3) Rancourt does a fiberboard insole wrapped in leather for their blake/rapid stuff and I've noticed no difference between that and a typical veg tan leather insole. It's just shoe degeneracy/nerdery I think
[i2wbhou] (score 10, diepte 5) > teflon

Do you mean poron??

> I've seen complaints in this sub for Alden insoles

This sub likes to complain about a lot of stuff that doesn't really matter. The only complaint I've seen is that Alden uses what people believe to be inferior materials while charging the retail prices that they do.

>a lot of support for using conditioners on insoles

This sub really doesn't know anything about what to condition or what not to. I've seen shoes that are twice as old as I am with intact insoles I don't think they were conditioned with any regularity.
[i2w9rft] (score 10, diepte 4) That's an issue with people making content about their boots being misinformed or not knowing the details. There's a lot of misinformation out there in that style of content (YouTube).
[i2vxl99] (score 9, diepte 0) So?
[i2wdi25] (score 8, diepte 6) I personally feel this has more of a "look at the assumption I made" vibe than correction of information but I get what where you're coming from.
[i2w6un7] (score 7, diepte 3) They play very loose with the truth on their website

> If it’s too good to be true…

> There are certain corners you can’t cut while making shoes if you want them to be good quality shoes. Craftsmanship and materials. Most of the direct to consumer brands will just focus on craftsmanship. They will got to workshops on Europe and tell them. Hey guys I need to sell your shoes in $200. Make it happen. How do they make it happen? **Well, instead of using the leather, soles, midsoles of a pair of $500 shoes, they use inferior materials.** I mean who the hell is gonna notice it. The idea is to sell words as “made in Italy”, “goodyear welted”, “resolable”, “no middlemen”.

Emphasis mine. JDS doesn't do buy 2 get 3 free, it's buy 2 get 1 free and no returns/exchanges.

Fiberboard is an inferior product to leather. Leather is pretty good at holding up to water, fiberboard is not.
[i2w2tlb] (score 7, diepte 1 OP) I felt the need to explore this further because in Wyatt and Dad's video, they thought it was a full leather footbed. It doesn't have to be interesting to you as it was for me, buyers should be informed.
[i2wd6q1] (score 7, diepte 5 OP) Dude, if I was placing blame on JDS you would know it. I haven't even mentioned the shreds of hard plastic they use with shredded leather that they use for the filler. I think your pushback is misguided, this information is important to buyers.
[i2ylm0n] (score 7, diepte 0) I have had many cheap Italian or Portuguese made shoes with fully leather lined insides. Thus I don’t think that having full leather interior is too much to ask, even for this price. It’s not impossible or anything, contrary to what many others say here (“you get what you pay for!” etc.) 

But of course the cheaper the shoe, the more likely it is to have  canvas insides or something like that.

I may be biased because I live in Europe and good quality cheap shoes are not that hard to come by. I assume that many people here are from the US? I don’t know that much about the local shoe options, when it comes to more affordable stuff: I have understood that cheap stuff is usually made in Asia or Mexico?

But to be fair, many Italian shoes are Blake rapid stitched, not Goodyear.
[i2wobib] (score 6, diepte 2 OP) More people should have seen this. People on this subreddit have wondered what the stitching on the insole does for maybe 5 years now. Sadly, JDS never responds to any of my DMs or inquiries or I would have let them make this public instead of posting about it.
[i2x4giq] (score 6, diepte 3) berta ? or more central?
[i2x7ymt] (score 6, diepte 4 OP) lol berta
[i2wawo5] (score 6, diepte 4) > Fiberboard is an inferior product to leather

Citation Needed. What qualities are required in the use-case for an insole? Does fiberboard not have those qualities? Is it a common point of failure on JDS footwear? 

Everyone likes to stop at "$thing is inferior" but no one likes to show up with any proof that that's even a _potential_ issue.

>Leather is pretty good at holding up to water, fiberboard is not.

Leather isn't really. These would be veg-tanned leather insoles if anything which gets horribly stiff and fairly brittle if it gets soaked in water. Who is soaking their insoles in water?

JDS's website isn't super clear but I don't see that quote on any of the pages I've looked at. I don't see anything from JDS (not unaffiliated YTers or bloggers who claim to know shit just because they buy shoes and bought a domain).
[i2w45v7] (score 6, diepte 2) Informed of what? Treton & whoever's video isn't official product info from JDS. JDS doesn't advertise full leather insoles to begin with. And I've not seen meaningful info that this really is even an issue other than internet shoe nerdery, especially for the type of shoe JDS makes (not work boots).
[i2ydpgo] (score 6, diepte 0) Thanks OP, I found this interesting. 
Ignore all the negative comments.
This sub has always been argumentative, and for the life of me I don’t know why. Some people just feel the need to bicker.
[i2w8k7v] (score 5, diepte 4 OP) I've seen complaints in this sub for Alden insoles and a lot of support for using conditioners on insoles because it's a high wear area. Anecdotally I've never had an insole fail unless it's one of the cheaper Allen Edmonds or leather sneakers (that use fibreboard or ~~teflon~~ Texon).

Edit: Texon, not teflon
[i2wbzzt] (score 5, diepte 4) wow didn't know that, thanks for the info
[i2wl9w7] (score 5, diepte 8 OP) Some people in this community have forgotten what it's like to have only 1 shoe in rotation.
[i2wjrgd] (score 5, diepte 6) When I first read your post I thought that JDS had advertised it as a full leather footbed too, might be worth calling out that they haven’t actually said so themselves
[i2w9d1p] (score 4, diepte 4) Those Jakkrabbits were sweet.
[i2vzhxp] (score 4, diepte 1) This isn't a "loose grain" complaint, this is an actual noticeable corner being cut
[i2wklcs] (score 4, diepte 9 OP) All I'm doing is putting the information out there and people will make their own decisions with that information now available. If they're $150 boots people shouldn't know what they're buying? Touching grass in this context is complacency and ignorance. Who are you to say this is something inconsequential, you're generalizing your own experience too much. I feel like this pushback isn't reflective of the subreddit description.
[i2y362z] (score 4, diepte 0) Is this thread locked yet?
[i31841w] (score 4, diepte 1) Leather lining isn't the same thing as a leather footbed
[i2wejp1] (score 3, diepte 5) I know that Jakkrabbits are particularly affordable looking, but even just over $300 for a pair of boots with what looks like good craftsmanship I’d be happy. Adelante has boots, with much less leather selection and customization, for $285 and while I got some cool looking shark leather from JDS I feel like the overall experience was negative enough to have not added them to my collection
[i2wx0ju] (score 3, diepte 4) [Chamois](https://www.reddit.com/r/goodyearwelt/comments/sn45c7/jakkrabbits_logger_boot_in_olive_revers_chamois/?utm_source=share&utm_medium=ios_app&utm_name=iossmf) logger glory.
[i2w0qg5] (score 3, diepte 2) What effect do you expect this cut corner to have?
[i361iyl] (score 3, diepte 5) >Who is soaking their insoles in water?

Meeeeeeee!

I often work in wet conditions. I occasionally end up with water in my boots and soggy feet.

However, I also have the good sense to know that a) this is unusual and b) I can’t expect my boots to last forever. If you abuse stuff it will break, no matter how good quality it is.
[i2w79vs] (score 3, diepte 3 OP) If their company moto is no advertisement and all the money is going to labour and quality then it feels disingenuous. Again, I've seen a lot of YouTube videos that featured this brand and they don't correct for mistakes especially Stridewise's feature where he says it's a leather insole (who they have contacted before). Is it wrong to put the info out there?
[i2wc540] (score 3, diepte 4) > If their company moto

Welcome to marketing 101. Literally every company is going to say they use high-quality materials and construction and all that stuff. Short of saying Jesus himself blessed the shoes it's nothing new.

Saddleback leather might still have their leather guide up which claims that leather which is blue in the middle "isn't fully tanned" which is fucking ludicrous. It's also not illegal and they can say whatever they want.

>Is it wrong to put the info out there?

No, but your blame is misplaced on JDS when the issue is apparently bad journalism. I can write a blog that says the iPhone 15 will find you eternal love and happiness, it doesn't make it true.
[i30lutc] (score 3, diepte 0) Not surprised, they sent me the wrong boot and they never responded to any of my return requests, what a shame
[i2x2cfy] (score 2, diepte 2 OP) Thanks. I live in redneck Canada so I'm not sure that would be useful information.
[i2zpm7o] (score 2, diepte 4) Seems a bit overblown. It’s cool to have full leather insoles but I’m yet to be convinced they have any material advantage over what’s here. Plus JDS is a budget brand, really. Something’s got to give

Also…you didn’t really state a potential impact — just “it’s a high wear area”. What do you suspect will happen and why?
[i2wcbxo] (score 2, diepte 6 OP) Correction, Texon, the stuff that Bedo usually complains about when fixing shoes.
[i2wrc1p] (score 2, diepte 4) IME, I found that the foodbed on rancourts dont compress as deeply as my other GYW/HW shoes. YMMV. The rancourt pennies I have are also not as comfortable as compared to my other shoes.
[i2wil6f] (score 2, diepte 8) bc shoe nerdery/gear culture is stupid and a cancer. Just enjoy your shoes

The entire space has been monetized to hell and back in search of a perfect bang for your buck boot made with Horween leather, full leather insoles, and whatever other "quality" crap people care about. All of these "review" YTers like Rose Anvil and Stridewise don't actually know shit.

These are _$150_ boots, I'm not sure what's expected at that price point.

I'm probably just too jaded from people complaining, but it's stupid. Buy shoes you like, go outside and touch grass while wearing them, live a happy life.
[i2wt8ly] (score 2, diepte 10) > Touching grass in this context is complacency and ignorance

lmao
[i2wk16c] (score 2, diepte 7) Tbh spending lots of money on shoes and insole material probably end up cancelling each other out because your rotation would be big enough. The people who leatherboard would most likely fail for are the one pair-only types
[i2y7izu] (score 2, diepte 0) How are you able to remove the footbed..??isnt it attached to the welt?? Btw wolverine 1000mile and thorogood moctoes also have fiber board footbeds
[i3eibed] (score 1, diepte 5) Is it Skinny in Ponoka? Dudes a legend.
[i2w217s] (score 1, diepte 3 OP) Footbeds are a high wear area, that was my main concern.
[i2ztx5r] (score 1, diepte 5 OP) If you've seen a lot of Bedo's resole videos, fibreboard insoles fall apart and have to be replaced. This is less of a factor for people with many boots in rotation. Goliath, the cobbler on this subreddit has been vocal about taking care of insoles and I'm surprised people choose to disregard it.
[i340zp5] (score 1, diepte 6) People want to imagine features will have a material impact because they like to nerd out on stuff, which is fine. That it happens at all does not mean it’s going to happen to you. Plus they’re cheap boots, ffs.

When posts like this become content in this sub, then it’s no wonder why it’s dying.
[i2wu7s5] (score 1, diepte 5) The handsewns are different though, those are true moc construction so your foot is sitting on the upper leather. 

For what it's worth, I don't think footbed compression is anything that's actually desirable, just a sign of wear.
[i2wja7q] (score 1, diepte 6) I see nothing wrong or misguided about your post. Appreciate it. Do sense some contrarian mindset and or fanboy mentality perhaps.
[i2zk0io] (score 1, diepte 1 OP) Yes, the welt was detached.
[i2wm8v2] (score 0, diepte 7 OP) You're completely right. People can make that assumption by the PSA title, I will make an edit.
[i2w3kwf] (score 0, diepte 0) Boo! 👻
[i2xbbw3] (score 0, diepte 0) …and?
[i2wdip2] (score -4, diepte 6) I've spent a lot of money on shoes and never once has the insole material made an iota of difference to me.
[i2w11tt] (score -7, diepte 0) Colour me surprised /s

This post is as uninteresting as they come.

=== THREAD bdipgq ===
SUBREDDIT: r/goodyearwelt
DATUM: 2019-04-15  SCORE: 161  REACTIES: 72
TITEL: Getting Started: Quick and (not so) Dirty Shoe Care Guide
POST (source_id=post):
#Intro
Welcome to /r/goodyearwelt! This is a quick guide to get you started with how to properly care for your new shoes. This guide is divided into three major areas: general care, smooth leather, and suede/reverse/roughout leather. If your shoes are **shell cordovan or a type of exotic leather**, check out other care guides in the [wiki.](https://www.reddit.com/r/goodyearwelt/wiki/resources/basics#wiki_care) To repeat **shell cordovan is NOT covered in this guide.**

There are also great more in-depth care guides like [this one](https://www.reddit.com/r/goodyearwelt/comments/77am8t/updated_introductory_leather_care_guide/) that i recommend you read. This version is meant to be really quick and a very general baseline. 
____

# General Care
**Use shoe trees** when they're not being worn. Wider heels are preferred to the heel cup doesn't get deformed. They should fit snugly and *not* actively be stretching the shoe.

**Brush after every wear.** Yes really. It only takes maybe 30 seconds total and lots of consistent care is better than trying to make up for all of the neglect at once.

**Rotate shoes often.** Yes really. Make sure that the shoes fully dry out in between wears otherwise the internal could [degrade](https://www.reddit.com/r/malefashionadvice/comments/2ip3de/my_iron_rangers_are_dead_irreparable_after_2/) and your shoes will be **ruined**. Rotation also helps with break-in for new shoes.

**Start with minimal care and work your way up.** If you think you're shoes are really dirty and need lots of care, there is no harm in starting with simpler forms of care. Try just brushing them first. If that doesn't work, you can try wiping them down with a damp cloth. Next a conditioning routine, then maybe using actual cleaning products. 

**You're probably not going to hurt them by using a product.** Unless you do something certifiably insane or misuse a harsh cleaner like Saphir Renomat I highly doubt you are going to totally ruin your shoes using product. Harm generally comes from actually wearing the shoes and neglecting them. 

##Products
[Shoe trees](https://www.woodlore.com/shoe-trees-inserts/) - I usually go for [these](https://www.woodlore.com/shoe-trees-inserts/mens-cedar-shoe-trees/mens-combination-cedar-shoe-tree-pair/) at a minimum for heel width. 

[Horse hair brush](https://www.amazon.com/slp/horse-hair-brush/o5v7ytjq3jnf4sa) - Pretty much any brush will do. I prefer larger ones with longer and softer bristles. It's up to you though.

____

# Smooth Leather

NOTE: This is incredibly generalized as there are countless types of smooth leather, but this should cover the bases of the most common casual and dress leathers.

## General Upkeep
Follow the general care mentioned above. Brush after every wear, use shoe trees when not in use, and rotate often. Depending on what happened that day a wipe down with a damp or dry cloth might also be useful.

## Conditioning
2-4 times a year you might want to more thoroughly clean and condition them. Whenever they feel dry. Your brand-new shoes almost certainly do *not* need any care out of the box other than a quick brushing. Further, less is more. I say 2-4 times a year as a maximum. More oily leathers like Horween Chromexcel (CXL) probably don't even need it that often.

To condition my smooth leather shoes I follow these steps:

1. Brush thoroughly with a horsehair brush
2. Wipe down with a damp microfiber cloth
3. Clean welt area using a toothbrush
4. Let dry and briefly brush again
5. If applicable, tape off uppers using painter’s tape and apply edge dressing (**Note:** Some users have had adverse affects from using painter's tape. /u/sakizashi had the great recommendation to use q-tips to apply edge dressing instead.)
6. Condition lightly using a product like Bick 4, Lexol, etc.
    1. Alternate shoes
    2. Use multiple light coats rather than one heavy one
    3. Brush in between coats
7. Use a buffing product like Venetian Shoe Cream or Saphir Renovateur (optional)
   1. Follow same guidelines as in previous step
8. Brush and buff to finish
9. Laces
    1. Iron/steam flat laces if desired
    2. ~~Re-wax waxed cotton laces if needed/desired using a hard wax like beeswax~~ If they need to be re-waxed it's probably better to just replace them. Laces are relatively cheap.
    3. Re-insert laces into shoes
10. Insert shoe trees if not in already
11. Let sit for 1 day

## Cleaning
Should be done rarely and accompanied by a thorough conditioning. Reach for these products when you have significant stains from things like oil or are trying to remove polish.

### Products:  
**Lexol Leather Cleaner:** The best general purpose cleaner and is relatively gentle, you don’t have to worry much about ruining the leather using this product.  
**Saddle Soap:** A more intense cleaner and can strip some of the chemicals used in tanning processes if you’re not careful. Make sure to do a thorough conditioning after using this. I don’t really recommend using it at all.  
**Saphir Renomat:** When you really need that shit off. This is an incredibly volatile product. Use it outside in a well-ventilated area. BE CAREFUL. This product *will* strip *everything* including your nose hairs. 

## Polishing
###Process:
Everyone has their own. Generally you want to make sure the surface is clean and dry. Apply thin coats of polish to the areas that are applicable (toes and heels get wax for a high shine, the rest of the shoe just gets cream). Alternate adding polish and buffing with a bit of water. Finish with a brush and buff. There are tons of other methods and everyone has their own tricks to get a mirror shine. 

I recommend using wax polishes only on the heel and toe area where there isn't any flexion happening to get a higher shine. Use a cream polish on other portions of the shoe along with something like Venetian Shoe Cream to get a dull sheen. Using a wax polish where the shoe flexes will result in the wax flaking off and generally looking horrible. 

###Products:
**Saphir:** One of the best and most widely available. Hard to go wrong with any of their products.   
**Allen Edmonds:** great for perfectly color matching some of the exclusive colors. They also have nice cream polishes. Though shell cordovan is not covered in this guide, I am partial to their Cordovan Care Creams as well.
___

# Suede / Reverse / Rough-out

NOTE: For my sanity and character count reasons, I’m going to refer to any “fuzzy” leather as “suede” for this section of the guide unless the difference is meaningful. Generally there is no difference in how you care for rough-out versus split suede versus reverse suede leather.

## Daily Care
As stated above I recommend using shoe trees when not worn and brushing briefly after every wear with a horse hair or suede brush. I find that regular upkeep does plenty with keeping suede and roughout looking nice and don’t really use special suede sprays, conditioners, or even brushes if you like horse hair ones for daily care. If you do want a different brush I recommend a [nylon](https://www.amazon.com/Ralyn-Nylon-Suede-Brush-1ct/dp/B00JV2UYYU) or [boar’s hair](https://www.hangerproject.com/hanger-project-suede-cleaning-brush.html) brush. I’m hesitant to use a brush that contains [brass bristles](https://www.hangerproject.com/brass-suede-cleaning-brush.html) since I feel like it would be too harsh, but others have clearly had success and like it. Your call.

Suede brushes are going to be stiffer than horse hair and can more thoroughly clean suede and fluff the nap.

## Cleaning
Contrary to popular belief, suede is not afraid of water and will not be ruined if exposed to it. In fact, I recommend literally washing suede if the need arises (this should **not** be needed on a regular basis). [This video](https://www.youtube.com/watch?v=Ba5k6Ii70kY) from The Hanger Project shows a really solid cleaning and rejuvenating routine for suedes and includes shampooing them (with a suede shampoo, not the one for your hair). I would do this at most once or twice a year and have never done it myself.

I think you’ll get the most mileage out of a suede eraser and brush. I have never used a shampoo or spray of any kind and haven’t found it necessary (yet). Others here certainly love it and a protector spray will be helpful at keeping stains at bay which is useful if you’re wearing [white shoes.](https://cdn.leffot.com/wp-content/uploads/2017/04/alden-plain-toe.jpg) I prefer to be more minimal and am very happy with [the results](https://i.imgur.com/NoZcBGj.jpg) even after getting them soaked.

___

# Conclusion:

I subscribe to the idea that more frequent and minimal care (like brushing after every wear) is a better approach to longevity and nice patina/aging than thrash and trash. Feel free to experiment and go your own way, they're your shoes!

If you have questions, please ask in the daily simple questions threads and people will be more than happy to help. This is intended as a very general and quick getting started guide. If you have thoughts, comments or questions about the guide and the advice lets discuss it in the comments below!

~beans

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ekyj7q9] (score 14, diepte 9 OP) [Salt stains that were there all winter](https://i.imgur.com/WtT870h.jpg)

[Immediately after cleaning with a brush, a damp cloth, and light conditioning](https://i.imgur.com/NUZ0t30.jpg)

[Current state](https://i.imgur.com/Vo9ORMr.jpg)
[ekymgj6] (score 13, diepte 0) Nice guide.

I think i am a little more cavalier with my shoe care. They might feel a little unloved if they ever read your guide...

* Never toothbrushed my welt
* If my shoes are really muddy (esp my boots) I hit them with the hose. Ive done that to my black shell boots even. They dry out and are fine
* I never bother with taping off my edge dressing, but I use a q-tip and not a brush to ensure i get just enough on and in the right place

I do love my saphir products, the cordovan creme, renovatuer combo is the best out there IMO. Also a crepe brush is an amazing product on nubuck / suede. Highly recommend giving it a try.
[ekye6u1] (score 11, diepte 1) News flash: people that expose their footwear to harsh conditions are in the minority in this sub
[ekykm89] (score 11, diepte 0) Great guide! I wish I had read something like this (or the guides stickied to the main page) before buying half a dozen Saphir products that I'll never need :(

The lesson I learned is to be a bit skeptical of guides or advice given by people who make a living selling the products they recommend. As it is in GYW, so it is in life
[ekyenlh] (score 9, diepte 1 OP) I do work in an office. But that is also my standard care frequency for my more rugged boots that I use for hiking, hunting, yard/garage work, etc. on a frequent basis. 4 times/year is every 90 days, if you keep up with regular upkeep I have a hard time believing you need to do a thorough conditioning routine more frequently than that. 

This is *very* general advice meant to capture the most frequent cases of simple questions related to care that pop-up in the daily SQ threads. If you're exposing your shoes to harsher environments daily like working as a mechanic then obviously you're going to need a different care routine.

edit: I also said 

>Whenever they feel dry. 

in the same paragraph.
[ekyij3n] (score 8, diepte 7 OP) > This sub is a drop in the bucket.

I wrote the guide to target this sub. If I wanted to post about work boot care specifically I would write a different guide, title it differently, and post it where the demographic is more suited to it. 

This guide is 

>[a] really quick and a **very general** baseline.

>**incredibly generalized** as there are countless types of smooth leather, but this should cover the bases of the most common casual and dress leathers.

It is also meant to generally cover *everything*. From work boots to dress oxfords with a mirror shine. 

I also explicitly state:

> Feel free to experiment and go your own way, they're your shoes!

I have yet to see any shoes that need conditioning every month while also keeping up with the rest of the guide's recommendations. The exceptional cases of a logger or smoke jumper or foundry worker are very obviously not covered by this guide.
[ekyrd24] (score 6, diepte 1) If it's being exposed to grease and oil frequently, I'm not sure what adding more oil and/or wax will really do. I'll certainly concede on salt.
[ekymra2] (score 6, diepte 2) HAHA!

 I was just looking at a [different site](https://www.shoecare-shop.com/) where I bought all my shoe care stuff and they have a comparison between Saphir lotion and Renovateur. They offer this gem of advice -

>Renovateur on the other hand is richer in nourishing ingredients than Lotion. You want to use Renovateur once a week at a maximum to prevent oversaturating the leather with oils

When I originally bought all my stuff I probably didn't think twice about that line, I now realize how ridiculous it is
[ekygewd] (score 5, diepte 5) So you believe the alternative, which is that there’s a silent majority in the sub that subscribes to read comments from others whose footwear usage doesn’t align with their own? That’s interesting.
[ekyli94] (score 5, diepte 1 OP) Thanks! And I agree, I was honestly hesitant to link the video from The Hanger Project because he says the *full name* of the products a dozen times in the first ~minute of the video. After that it becomes much more bearable though.
[ekygypf] (score 4, diepte 3 OP) This is anecdotal, but I really only ever see people who almost literally never condition their shoes, or they do it far far too frequently. That usually dulls the color and flattens out any patina. 

I can't really imagine needing to condition shoes every 15 wears (30 days or 12 times/year) especially if you're keeping up with general upkeep. I feel like every ~45-50 wears (4 times/year) is still incredibly frequent for conditioning. Why do it more often and waste product and ruin the look of your shoes?

I'm willing to keep an open mind, but I really *really* don't think that kind of frequency is required.
[ekyilfj] (score 4, diepte 7 OP) > Salt only needs a few minutes to do damage.

This is just false.
[ekyl09o] (score 4, diepte 9) I personally trust /u/LL-beansandrice (wow, beansan rice, new lo strock mistake?) and GYW sub more than I trust a site called triblive.com, sorry.
[ekymym4] (score 4, diepte 1 OP) > Never toothbrushed my welt

It's a small detail. I feel like it does make a noticeable difference, but I also don't do it that often. Usually only if there's some grime or something that hasn't come up with normal brushing. 

>I use a q-tip and not a brush

That's a really nice tip for edge-dressing application. My shoes don't really require edge dressing so I do it pretty rarely.
[ekyogpj] (score 4, diepte 0) Any tips on chamois?  I've seen some suggestions to add some neatsfoot oil on it, but nothing really definitive.  I'm also surprised at how low upkeep suede is.  You don't condition them at all?
[el06hdr] (score 4, diepte 0) Excellent guide!  It was well put together.  A quick question on Suede, we always recommend to use a waterproofing spray before first wear, what on your thoughts on this?
[el11ljs] (score 4, diepte 1 OP) Are there specific cases where you find Saddle Soap does a job that Renomat or Lexol's leather cleaner doesn't? It's not exactly a bad product, but I personally haven't found a need for it that isn't covered by other safer options. 

Good point about the phrasing in the general care section!

>Brushing after every wear seems excessive

It is a bit, but I think it's easier to be in the habit of quickly brushing every time rather than sometimes. I also subscribe to the idea of more consistent minimal care rather than the cycles of neglect and rejuvenation that give really dramatic "before and after" shots.

Especially for newbies, they like to go wild with products or extremes of care. I feel like this is a pretty safe way to approach shoe/leather care that's also very general. Missing brushing a few times isn't a big deal, but it can be if you neglect your shoes all season/year.

I agree it's more than what's required, but from a habit standpoint I think it's good advice.
[ekyfhld] (score 3, diepte 3) Just because “a good chunk of GYW footwear is work boots, and motorcycle boots” doesn’t mean they’re used in situations that would get them extensively exposed to harsh conditions, which seems to be what you’re saying in your third sentence and in your original commen

So what are you trying to say, really, other than “I don’t believe you”
[ekzo3i9] (score 3, diepte 9) A night is over in a few minutes?
[ekynblm] (score 3, diepte 3 OP) I will say I do find that the sheen that I get from buffing renovateur is gone in ~10 wears so I suppose you could apply it really really frequently. But it's kind of expensive to apply to an entire shoe that often and I don't really see the need for it.
[ekz6xca] (score 3, diepte 0) Thanks for the guide! This helps the older one as well! I’m about to thoroughly clean my Thorogood Dodgeville Boots (black CXL) because they are rather dusty and have more than a few scratches/scuffs. Any recommendations for CXL specifically?
[ekzjnc2] (score 3, diepte 0) Hey Man, just wanted to say thanks for putting this together.  I'm guessing this is the 1st part of the guide that was under discussion a while ago?  Well done!
[el0jwpn] (score 3, diepte 1) I have suede shoes I have waterproofed, and pairs I have not.  Both have been caught in the rain with no ill effects.  If I have a pair I want to use exclusively for foul weather, I'll waterproof them as it's easy insurance.  Otherwise, I don't bother.
[el0kvh7] (score 3, diepte 1 OP) That’s mentioned briefly in the suede care section! I don’t use it but I think it can be helpful to prevent stains. Suede doesn’t have issues with getting wet at all so it’s an aesthetics thing to use a protector.
[el10g8j] (score 3, diepte 0) Brushing after every wear seems excessive, I know some here do, and plenty do not.  As an introductory guide, I think that's too much.  Also, in your general care guide, it can seem like your list is specific to CXL since that is the last thing you mention before jumping into the step by step.  I suggest moving the general care section up and creating a seperate section specific to Conditioning like you have with polishing.

I would also be mindful of putting personal bias in your guide.  Like Saddle Soap.  It certainly has it's place and purpose, even in shoe care.
[el1blbu] (score 3, diepte 0) I always like that GYW guides always reference that photographer with the destroyed Iron Rangers.  It’s a fine tradition showing us what not to do with shoe care.
[el2fuca] (score 2, diepte 9) I've yet to see anyone disparage boots that have been worn for work here. Quite the opposite - I think people appreciate seeing them being worn as intended.
[ekyhnxp] (score 2, diepte 5 OP) > If you have dust, dirt, and grime abosrbing that moisture on a daily basis they will dry out.

Which is why I recommend brushing them off after every wear.
[el09w1i] (score 2, diepte 1) Could you please provide a link to the crepe brush that you like and suggest?
[ekztpjo] (score 2, diepte 1 OP) One of a few! I was repeating the same info for the “care” section of the faq so I figured I’d pull it out into its own post that’s a bit more straightforward and general than the great and more in depth care guide that’s always linked in the body of SQ threads.
[ekzvpix] (score 2, diepte 2) Right on, nice job here.  If you need help with editing or proof reading or drafting, etc. just ping me and I can try to make some time to help out.
[ekzkt1c] (score 2, diepte 0) ﻿
(47 reacties met lagere score weggelaten)

=== THREAD 6xv979 ===
SUBREDDIT: r/goodyearwelt
DATUM: 2017-09-03  SCORE: 24  REACTIES: 62
TITEL: Truman Boots Co switched from leather insoles to cork.
POST (source_id=post):
Hey everyone, 

I recently got my second pair of Truman boots and I noticed they replaced the leather insole with a cork one. The footbed side has a glossy paper lining which makes everything inside the boot feel slippery. 

I asked them about this change and they told me cork insoles are better for comfort and bacteria. 

What is everyone's thoughts on this?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dmiry8q] (score 33, diepte 1) filthy casuals
[dmiunce] (score 21, diepte 0) Do you mean sock liner? The insole is the piece the upper is stitched to, and replacing that with cork would be bad and really weird. The sock liner is the piece that goes over the insole, and provides padding and covers any stitching (for Blake stitched) or nails (for most GYW and stitch down). AE is the only notable brand without sock liners that I know of. It is easily removable and replaceable and would be no concern.
[dmiuvl6] (score 18, diepte 2) Then no quality issue. Just a choice on their part, albeit not a common one. Might even be more comfy than leather. Probably will break in easily to mold to your heel. Truman can easily put in a new one when you need a new heel and/or sole, which is just fine.
[dmiwmst] (score 15, diepte 2) Seriously, this parent comment is horribly snobbish.
[dmivgjl] (score 15, diepte 1) DAE think trendy fashion pleb consumers not rugged and manly enough for tuff masculine break-in of real thick authentic heritage leather? (...even though it turns out they just changed the easily-replaced sock liner?)

alternatively, DAE gatekeep *wearing shoes*?
[dmk5g61] (score 12, diepte 0) Is this much ado about nothing?  Because it feels like much ado about nothing...
[dmiy88b] (score 11, diepte 5) tbh the only authentic shoe is an entire dead cow into which i had to force my feet
[dmistyv] (score 9, diepte 2) Is all of this undisputed, especially the last part?
[dmiv1fn] (score 9, diepte 0 OP) [Here](https://imgur.com/a/r2kYb) are some images of the cork.
[dmk5ya6] (score 9, diepte 1) That's what it feels like to me...
[dmitfws] (score 8, diepte 2) Doesn't Allen Edmonds replace the cork when they recraft? At least that's what I remember from the videos.

Haven't fully made up my mind yet but this feels like a handwelt vs GYW situation, where the benefits are almost entirely theoretical. There's always a push to romanticize The Old Ways.
[dmipcxo] (score 7, diepte 0) I think they want to produce in large scale, so using cork insole would be more consistent. But the people in this thread want the original style, leather insole and leather lining. It's their decision, I believe they did some research about the changing, and then made the decision.
[dmiy3ws] (score 7, diepte 4) Authentic to what standard? Stitchdown by machine is inauthentic relative to handstitched, isn't it?
[dmiuic8] (score 7, diepte 3) AE doesn't use cork insoles, they use a cork fill between the insole and the outsole, to fill the space created by the welt. That fill is replaceable of course. I think OP is saying Truman is using a cork insole (or maybe he means they use a cork sock liner), in which case that's replaceable.
[dmiy2ow] (score 6, diepte 3) I feel like good quality shit is more available to the average consumer than it has since the days where GYW was standard. There was an absolute explosion of affordable, made-in-USA, stitched footwear in the early 2010s, of which Truman is a part. Expansion of those operations means some cost-saving measures -- correct me if I'm wrong, but doesn't Allen Edmonds not even use sock liners for many models?

Also, I don't understand your edit to the parent comment: "many companies are moving towards a more casual, and typically therefore, lower quality direction." Can you expand?
[dmitn3p] (score 6, diepte 0) Do you mean inserts? Is this a thing you can take out of the boot? I'd be surprised if cork was strong enough to serve as a major structural component of a heavy duty boot. Do you have pictures?
[dmj08h5] (score 6, diepte 1) Nothing wrong with poron. RM Williams have been using the stuff for years in the Comfort Craftsman boot with great results. It upsets the purists and iGent-y types but Poron is great for people in the real world who just want comfortable, well-made shoes.
[dmje3vv] (score 6, diepte 0) So it's leather footbed, with a removable cork insole? I can dig it
[dmj1q54] (score 5, diepte 7) *hippo
[dmixgi6] (score 5, diepte 1) Can't really fault a company for trying to reduce costs (especially where there's no practical difference) when there are fewer and fewer people willing to spend $350+ on footwear. Just look at the stated budgets of newbies coming for advice.
[dmiy0ta] (score 5, diepte 3) I think that's subjective, and here's what I've observed: regardless of their public statements on what they strive to be, Truman has largely captured the "I want a quality workboot but don't want to spend $600+ on Viberg" market. If they creep too closely to Viberg, they lose their primary advantage there. 

What else fills this niche?
[dmjvw2x] (score 5, diepte 7) Wouldn't you expect Viberg prices to rise, as well?
[dmirmoy] (score 4, diepte 0) What is the benefit of a leather insole?
[dmizy7z] (score 3, diepte 6) *horse
[dmizyel] (score 3, diepte 3) Not sure. For example, Birkenstocks use cork and are known to last years if not decades with proper treatment, and are extremely comfortable. The cork starts off more elastic, while leather starts out stiffer, but I feel like they converge to about the same place. i.e. cork gets harder and leather gets softer?
[dmiur5j] (score 3, diepte 1 OP) yes its the sock liner, when I remove this cork liner, all the stitching and nails are exposed.
[dmiuymr] (score 3, diepte 0) I don`t think insole can be changed for cork. If it could, there would be no use for Texon Poron stuff which lower end boot manufacturers use such as Chippewa etc. 

They might be having cork footbed or smh.
[dmlw6z3] (score 3, diepte 1) Based on responses in this thread it seems like the answer and relevance depend on whom you ask.
[dmjv4wt] (score 2, diepte 5) Leather prices rise every year, as do labor costs. What are you driving at?
[dmk2gfh] (score 2, diepte 6) Haha it's interesting how we can read the same material and get such different views out of it.

To me, the broader conclusion is that some feet, once adapted, don't actually need any support at all. But this isn't possible for those who lived their whole lives in highly supportive footwear or have unusual foot morphologies. So I do think the superiority of leather insole makes more sense if you believe that support is crucial to your needs.
[dmiurdk] (score 2, diepte 5) If it's the sock liner, and not the insole, than it's fine. Cork is probably a comfy sock liner, and that's an easily replaced piece, doesn't need to last forever. If OP is right and it's the insole, then terrible. Cork will eventually split and get water logged.

Yeah OP confirmed that he meant sock liner.
[dmiv5x1] (score 2, diepte 1 OP) I have both the coach and stone rambler.
[dmj9koy] (score 2, diepte 2) Yeah, I was going to say my poron insoles  (correct term) in my dress shoes make them more comfortable since I'm on my feet a lot for work.
[dml0tp8] (score 2, diepte 1) Nothing wrong with cork. But if it bothers you, either go to a Tandy or a cobbler that has some leather laying around. Bring the cork sock liner, trace around it on the leather and cut out new ones. Can't imagine it will cost much. Most leather distributors have a scrap bin with enough of the same leather that will suffice for making new sock liners.
[dmm66c0] (score 2, diepte 5) Is your experience working in an OEM factory producing blake stitched shoes in a 3rd world country applicable to Truman manufacturing practice?
[dmmp4tw] (score 2, diepte 7) I'll give Truman the benefit of the doubt and hope that it's just glue residue that makes the insole look shiny, paired with the camera flash. Would of course like to see it firsthand and give it some scratches to confirm, but I can't imagine Truman going synthetic with their insoles. However, it wouldn't be the first time to happen. Looking at you, Florsheim.
[dmiqt64] (score 1, diepte 1) You tell that to the shareholders!
[dmjurom] (score 1, diepte 4 OP) Their prices have increase as well, the in stock boots now are around $530-540.
[dmishqb] (score 1, diepte 1) More stiff, less elastic. It is less comfortable until worn-in, whereas cork is soft from the beginning. Once worn-in though, leather is very durable, and even hard while also being precisely the shape of your foot. It is approximately the difference between a hard and soft insole. Harder ones are better (if they fit) because your foot wants support and elasticity always has a limited lifetime.

Edit: Anyway, as mentioned above it is the sock liner rather than the insole so easily replaceable either way. As such it is more a question of preference with the only difference being the frequency of replacement.
[p7okwh6] (score 1, diepte 4) No, leather remains hard and it's a bit of a myth that it 'molds to your foot'.

The cork in Birkenstocks actually molds to your foot much more and while it remains hard for a while, the upper should eventually give way and soften but it takes quite a bit of wear to reach this state.
[dmk0px4] (score 1, diepte 3) Cork is a more long-lived material than most synthetics, but the fact that elasticity will degrade is undeniable. A perfectly elastic material does not exist. Leather also stiffens with use, and that I know due to the performance of the leather insoles I use. The information about hard insoles being better than soft I learned as I researched insoles during my days in food service. 

I doubt the information is undisputed, but I feel reasonably confident in its veracity. I welcome any expert correction though, and as always if you find conflicting evidence please feel free to share
[dmk1c79] (score 1, diepte 4) >Your foot wants support

There's a lot of research lately saying this is not a given - certainly not for everyone, anyway. The whole barefoot running craze, although stretching farther than it probably should have, did arise from real science questioning modern footwear technologies. I can find a link or two in a bit, but googling "barefoot running" will probably get you the Harvard studies that laid it out.
[dmk27zm] (score 1, diepte 5) I love barefoot running! That deals with the drop between heel and toe though, specifically. I'm a firm believer in low or no heel as a better way to move. That's actually part of the reason I love leather insoles. They are "zero drop", so the same width throughout, which is what the research suggests as positive, then in addition, the natural pressure areas of your foot thin and harden only the areas that should be thin while the rest stays the same which provides only support where you benefit from it and none where you wouldn't. I love this stuff so I'm was pretty excited by that reference and I'm not sure if i'm making sense. I can upload some pictures of the sock liners I made which show what I mean if you like?

e: grammer
[dmn7enr] (score 1, diepte 7) I feel like our point of disagreement comes from the word support.

From the research I've read, the advantages of barefoot running come from the height between heel and toe, and from the lack of cushioning(the support you mean), unrelated to arch support(the support I reference). Without cushion and a raised heel we will run on the balls of our feet, which mitigates initial impact and protects our joints. Leather insoles are perfectly inline with this approach, as they do not cushion significantly. I mean, mine are literally flat, foot shaped pieces of leather. As close to barefoot as it gets without being bare foot. 

Arch support is important for those people at risk for arch collapse and flat feet, but as a preventative measure it is harmless and not referenced by the research that I've seen as it is viewed as unrelated as well as not really being supplied by the flat piece of leather in my shoe. (It really does mold to your feet though so it has the same shape as my arch)
[dmna5ni] (score 1, diepte 8) No, I think I'm not making my point clear. My interpretation of the research is that any support, whether cushioning or arch, is unnecessary if your feet are not past the point of adapting. This isn't only for running, but for walking as well. I think there's merit to the hypothesis that if you grow up wearing shoes with arch support (not just cushioning), that your feet become addicted to it. Whereas if you strengthen your feet, you no longer are at risk for arch collapse. I know I'm jumping between discussing running and walking here, but when I got into barefoot running, I noticed a market rise in my arch.

All of which is to say: I believe a significant portion of the population, provided they're not so old that their foot structure is no longer malleable, and the time to strengthen their feet appropriately, actually have no need for arch support *or* cushioning at all.

Granted, I'm not a physician, foot doctor, or whatever. This is me speaking from personal experience, interpretation of the research, and extrapolation therefrom.
[dmit78c] (score 1, diepte 1) I think one could argue that a leather insole would last longer than a cork insole.  Also, once the insole is dead, isn't that the end of the shoe/boot?  So for durability I imagine a leather insole would have benefits over cork.
[dmiunhp] (score 1, diepte 4) Thanks for the clarification. What's your take on Truman's decision here?
[dmjw67h] (score 1, diepte 6) I've always been curious about that, Birkenstocks are probably the most comfortable shoes in my closet and are made from cork. I've worn them for almost 6 years (sand, water, etc) and are still holding up well. Are they using a special cork? Is it the thickness of the cork?
[dmitkws] (score 1, diepte 0) Which boots did you get?
[dmja0ar] (score 1, diepte 2) Wondering if I'll have an unexpected surprise when my MTO winter smoke waxy's finally arrive...
[dmjkv2m] (score 1, diepte 2) I know nothing wrong with Poron. Just saying if they were able to use cork for insole they wouldn't have used insoles like Poron etc.

Probably Truman is switching to cork footbed rather than insoles.
[dml17j5] (score 1, diepte 2) The first picture show the shoe without sockliner (exposed nails & residue of adhesive that hold the sockliner down). Doesn't look like leather insole to me (glossy white under flash)?
[dmlf5xu] (score 1, diepte 3) Fairly certain that is indeed leather. Insole leather is often quite white or creamy colored. I don't even think you could use anything else with stitchdown/naildown construction since the nails that clinch the upper to the insole needs something rigid to attach to.
[dmm4v46] (score 1, diepte 4) They often cream (natural veg tan color) and rarely white but it look odd with the glossy flash reflection. Most sole leather are not finished or have matte finish.

I knew quite a lot synthetic material insole can take nail very well, they are widely used in cheap blake shoes (just don't know english name of those material) Source: working with fatories in a 3rd country in the last few years, saw many orders from fast-fashion brands that require corner-cutting everywhere.
[dmm7c3q] (score 1, diepte 6) Just reply to his doubt about material that could be used as insole, nothing more or less. Those material are source mostly from big company from italia and spain, not local; so it applicable worldwide.

With just visual from that picture, I can only doubt and hope that's not the case. If it is then no java waxed flesh option at my budget anymore.
[dmm7q1v] (score 1, diepte 7) More than fair :)
[ltltcmj] (score 1, diepte 5) it's usually Texon or a cheaper imitation.

  
real Texon lasting board material is a cotton composite fiber board.

  
used in hakes globally, in cemented, injection molded polyurethane, Blake stitched and Goodyear welted
[dmlvi8q] (score 1, diepte 0) I've been wanting to ask this but never really felt it was the right place to do so, so i'll ask it here.

I was watching a Brian The Bootmaker Video and he said he removes all the cork from Red Wings because he feels like cork doesn't hold it's shape well like leather does. Is this true?
[dmixp8f] (score 0, diepte 2) The practical difference point is arguable, but as far as the cost vs demand argument, there are brands that cater to those price ranges already so I just don't like seeing supposedly premium brands cutting corners.
[dmjv7ht] (score -1, diepte 6 OP) that they might start be around the viberg market if they become 600+ in the future.
[dmixq6j] (score -2, diepte 3) but i think its true. Keep the boots authentic
[dmiymi3] (score -5, diepte 0) I agree, and maybe it's a by product of expansion like you've said but it irks me to see companies that brand themselves premium whether it's because of their materials and/or construction methods and then they decide to cut costs like Truman and to me that just lowers the overall quality/value of the boot because it's not true to its image it once had. It just seems to me that whenever a company does that they see a subtle decline over time in product quality from style to style. Speaking of AE, I think they make a good example for this because even though they're still high quality, their burst in popularity has correlated with a DRASTIC decrease in quality control and I suppose that's just a harsh reality of the situation but it's just disappointing to me when I see that from reputable brands.
[dmixa33] (score -6, diepte 2) I like good quality shit and it's getting harder to find, shoot me for being irritated 🤷‍♂️. I did admit my ignorance of the situation in my edit, but I still think my comment on the industry is valid.
[dmipkzw] (score -9, diepte 0) Weak decision based off of weak reasons urged by weak consumers who can't break in a boot and cry about it because they grew up wearing tennis shoes and then decided to get trendy and start wearing leather goods. Been seeing a lot of companies starting to cater to these folks and although a smart business decision, it's ruining the culture and the point of wearing handmade/old-style construction footwear. 

Edit: Sorry if my comment hurt your tootsies, but I now realize it was the sock liner as has been mentioned and I'll own up to my mistake. Although I will still say it's kind of a cheap move and that it seems like many companies are moving towards a more casual, and typically therefore, lower quality direction.

