# Label-batch batch_0021

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
Schrijf het resultaat naar `batch_0021.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 6egaa4, 6blcfy, 9bo8pc).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 6egaa4 ===
SUBREDDIT: r/goodyearwelt
DATUM: 2017-05-31  SCORE: 22  REACTIES: 55
TITEL: My feet suck and I need shoes. Help me end 25 years of pain.
POST (source_id=post):
I recently visited a podiatrist for the first time after 25 years of foot problems. My feet have high arches and the bones in the top of my feet are tilted inward (I forget what this is called. I think a four-syllable word beginning with 'M.') Doctor told me my options are cheap insoles, custom insoles (which my insurance won't cover), or surgery (which my doctor described as "an extreme or desperate measure.") 

When the cheap insoles proved minimally beneficial and ill-fitting in all but one pair of shoes, one of the nurses suggested I look to New Balance. But I don't wear athletic shoes. At all. I like boots, dress shoes, or otherwise simple and clean looking shoes without obnoxious logos. I rarely wear anything other than slacks or dress pants, so wearing an athletic shoe (which I don't like anyway) would look ridiculous. 

I have a pair of [Clarks Desert Boots](https://www.clarksusa.com/us/originals/originals-mens-boots/desert-boot-black-beeswax-leather/p/26103683) (which I like but are bad for my feet), [Clarks Desert Londons](https://www.clarksusa.com/us/originals/originals-mens-shoes/desert-london-black-sde/p/26107883) (also bad for my feet), another pair I can't seem to find but look similar to [this](http://www.clarksusa.com/us/mens/mens-shoes/mens-casual-shoes/lander-cap-blue-combi/p/26124228) in shape and color but look more like converse in design (which I again like but are bad for my feet), and a pair of black [Allbirds](https://www.allbirds.com/products/mens-wool-runners?variant=29692646919) (which are hideous but were the most comfortable shoes I've ever worn for about two weeks, and are now "meh" at best).


What are my options? Or am I doomed?

Thanks in advance for your help.

Also, where can I sell my Clarks? I doubt I'll wear them anymore.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[diakyk8] (score 21, diepte 0) guy with problem feet here. 

Goodyear welt shoes might be a shitty option for you, unless you're able to drop tons and tons of money.  modern materials are easier to form and easier to design for pliability in one region and rigidity in another.

If nothing else, limiting yourself to one type of shoe does not serve the very important purpose of fixing your problem. once you fix your problem, then spend money on shoes. 

If you don't have a ton of money, maybe start by trying out different insoles. insoles run $20-50 usually, and you can easily swap them out or remove them in the middle of the day so you're not putting one type of pressure on your feet for 8 hours. 

I bought several insoles from feetrelief.com, which is a small business and the owner is awesome. I like the birkenstock cork insoles as well as the blues.  you should write the guy and ask if he has any advice. 

point being, you could drop $200 on insoles and have a good chance of buying yourself some immediate relief. bare minimum, you will gather a lot of data that you can use when you take your next step.

also. new balance has very wide shoes. if you have a new balance store nearby, check then out. 

crocs professional are good wide nonslip shoes with pretty good support. 

Dansko clogs are impossible to walk in, but can be a heaven send for standing for long periods.  

Edit: and don't get surgery for structural problems until you have exhausted all your options.

If you're fat, lose weight. I had to do it. try going to a physical therapist or deep tissue massage therapist with some knowledge of exercise physiology or the like. a Rolfing 10-series might help you a great deal by correcting postural problems that are twisting your legs and feet.

you also might have problems with the fascia of your foot that is holding your foot in an unnatural position. once your feet start hurting, I think it's likely you will incur trauma, which given the pressure most likely results in scar tissue that exacerbates problems. 

get a foot massager. it's not a complete solution, but it could really help to be able to loosen your feet up on an ongoing basis. if nothing else, the brief feeling of relief is like heaven, and I know you need it.
[dia6i9d] (score 11, diepte 2) FSA = Flexible Spending Account, HRA = Healthcare Reimbursement Account. Both are forms of paying for medical expenses at a discount. 

FSA funds are something you designate at the beginning of each benefit year as a lump sum of your annual salary taken aside to use, but the amount is always pre-tax. The catch with FSA is it's use it or lose it each year, so don't set aside too much unless you're comfortable with blowing the remaining amounts at the end of the year on a bunch of random crap (listed below). HRA is something that some companies offer as an additional benefit and typically pre-load an account with a fixed amount each year for you to use without costing you anything. 

These days both are typically done in the ways of giving you a credit card that charges from the account and just declines when you try to purchase something not eligible or have reached your annual limit.

Eligible expenses include costs of medical treatments and care, co-pays, prescriptions, and all sorts of other "medical" expenses deemed important to healthcare such as prescription glasses and sunglasses, sunscreen, most forms of birth control, bandaids, braces and wraps, the list goes on and on. And sometimes what is or isn't eligible is hilarious. Like $10 Clearsil face wash requires a Rx, but a $150 experimental "light therapy" for face cleansing is eligible...

There's official sources on all things that can or cannot be purchased. But a great way to see what types of things are eligible are to browse stores like FSAStore.com and the red check means it's eligible always, the green Rx means eligible with a prescription or physicians letter of medical necessity. 

Official government info can be found [here](https://www.healthcare.gov/have-job-based-coverage/flexible-spending-accounts/)
[dia5h1n] (score 10, diepte 0) Also keep in mind that superfeet (and any insoles) can be purchased with FSA/HRA funds. So if you plan ahead to some degree you get them without paying income tax (or at all if your employer does an HRA account for you) making them quite affordable.
[diad3na] (score 6, diepte 0) Metatarslis are the bones your thinking of. I you can find an Alden dealer that has modified last boots, try them on. They're built for high arches.
[dia5mmm] (score 5, diepte 1 OP) I'm sad to say I have no idea what you're talking about. >:/
[dia933w] (score 4, diepte 0) Whites or wescos? Don't they make the boot to our exact foot dimensions? Very pricey but beautiful and rugged looking.
[dia5blo] (score 3, diepte 0) Unsure what impact the tilted bones have, but with high arches, custom orthotics are a lifesaver.  I have a pair I wear in my work boots daily and switch to my running shoes (or at least when I ran)

Next up is Superfeet or other high arch type inserts.  I just got a pair of the dress 3/4's and thru in my AE's for a wedding last week, they helped a LOT.
[dial1pv] (score 3, diepte 4) Hah no but work for a nonprofit (lower base salary) with crazy good benefits, so anytime I get poached by recruiters I have to tear through the full benefit package to see how the compensation really compares.
[diaj56w] (score 3, diepte 2) I am a White's advocate. I'm not sure if you are anywhere where you could try some on, but try to do so. Or check out [White's ebay site.](http://www.ebay.com/usr/whitesriver?_trksid=p2047675.l2559) Call them and talk to them about getting a measuring kit to see what size you are and then browse and save a search in your size to snag a pair at a very good price. I think you might benefit from the way they build their arch support.
[diah73b] (score 3, diepte 1) Nicks Boots do that, too, but cheaper and more custom looking.
[diab07c] (score 3, diepte 0) https://www.reddit.com/r/goodyearwelt/comments/6blcfy/discussion_orthotics_a_gyw_tragedy
[diahbnx] (score 3, diepte 1) That simply is not true. Chiropodists measure the mechanics of your feet and, in the best cases, manipulate your feet to correct abnormalities. They then take a plaster cast of your foot *in the correct position*, and make an orthotic device to support that correction as you walk. I have no doubt that some orthopaedic clinics have dubious standards as chiropody and podiatry are not evenly regulated practices around the world, but I think the advice you're giving here is simply not accurate. If OP has sought advice from a physican or regulated healthcare provider, I would suggest that OP follow that advice rather than some random post on the internet purporting to have a solution to an unknown problem.

This post smacks of the "this one secret will fix all your problems" garbage. I am sure you have the best intentions in posting it, but I really think OP ought to ignore this advice entirely.
[dib7wis] (score 3, diepte 1 OP) Thanks for taking them time to write all of this. I'll check out everything you mentioned. I'm not fat, my feet are just evil. I've been considering a foot massager.
[dia5h9v] (score 2, diepte 1 OP) [These](https://www.amazon.com/Spenco-Orthotic-Support-Length-Insoles/dp/B000FPKUZ0/ref=sr_1_7_a_it?ie=UTF8&qid=1496254578&sr=8-7&keywords=spenco%2Binsoles&th=1) are the ones my doctor recommended, and the ones I bought. They've been...okay.
[diak5y6] (score 2, diepte 3 OP) Wow, thanks for that write-up!
[diapjpg] (score 2, diepte 3) An HSA, which are much more common than an HRA, would also pay for it, correct?
[diathlb] (score 2, diepte 4) Correct! HSA are more in line with FSA in that you're contributing to it and not your employer. Benefit is it does roll over year over year, downside is you manage it all yourself and can only spend what you've already contributed. Versus an FSA you can spend your annual contribution on day one of the new plan year even though you have only contributed barely anything yet, as it's paid throughout the year from each paycheck. HSA also have eligibility requirements for a high insurance deductible that FSA don't - I'm not sure the specific number since my employers plan isn't eligible.
[dia75xi] (score 2, diepte 0) Aldens are supposedly very comfortable (I do not own a pair to confirm) and I believe they started out as an orthotic company. Must have high budget or be willing to buy used.
[dia7n0l] (score 2, diepte 0) [This](http://www.theinsolestore.com/blog/superfeet-premium-insoles-color-chart/) is a great breakdown of superfeet insoles. They are about $50 but have been better than custom insoles for me. I think you can find them on Amazon as well.
[diaanjn] (score 2, diepte 1 OP) Pricey and beautiful indeed.
[dic74b8] (score 2, diepte 1 OP) This was helpful, thank you.
[diajri0] (score 2, diepte 1) Second. I don't own em, but having seen them just now for the first time I can say if I had to wear an athletic style shoe, I'd buy a pair.
[diajuk4] (score 2, diepte 1 OP) On their own they aren't, but with the rest of what I wear they look pretty goofy.
[diajzxs] (score 2, diepte 3 OP) They were downright heavenly when I first got them, but after a while they were like my other shoes, and I'm not about to spend $20 on new insoles every two weeks.
[diamoxe] (score 2, diepte 2) do you have plantar fascitis?  

what would happen to me is I could walk fine until I felt a tiny tear, and then it would hurt like knives in my feet.   

Also, check the edit on my other comment, I added suggestions.
[diazvek] (score 2, diepte 0) I've been stuck in Brooks Beasts for many years, but finally found that the Thorogood Heritage boots are reasonably comfy, with the added benefit of having enough room for orthotics.
This sucks, I know.  But for God's sake, don't be such a slave to fashion that you can't even get around just because they may not be boots.  You still have a life to live.
[dibnybg] (score 2, diepte 0) A podiatrist recommended Samuel Hubbard for shoes with removable insoles.
[dibp3bk] (score 2, diepte 1 OP) Oh, I like those quite a bit. Thanks.
[dibxu0v] (score 2, diepte 2) Hope those work out for you. I recently discovered what a difference good shoes can make to your outfit, but am struggling with the fact that it's not easy to use orthotics with them.

I haven't gotten around to trying Samuel Hubbard yet though. Best of luck with them! :-)
[diakq2s] (score 1, diepte 3) I bet you're in HR?
[diavph2] (score 1, diepte 5) Thanks for clarifying. I just got into the industry so I'm not well versed in the intricacies of it yet. This will be very helpful to a few of our clients.
[dicqsgz] (score 1, diepte 5) employers generally contribute to the employee HSA as well.
[diafwql] (score 1, diepte 1) Correct me if I'm wrong, but it seems like buying used might defeat the purpose in this scenario since they will have already conformed to someone else's foot.
[diahir4] (score 1, diepte 2) Good point. I believe that's accurate (but I'm a novice at this stuff!)
[diajv86] (score 1, diepte 3 OP) I'll check that out. Thanks.
[dialfa9] (score 1, diepte 2) Never taken a look at their stuff, anything above $200 is out of reach at the moment. And I'm a straight pig with my footwear lol
[diai5i4] (score 1, diepte 0) This is 0% helpful but I don't think Allbirds are ugly. I get compliments on them all the time.
[diajy55] (score 1, diepte 2) Yeah, they were the first athletic shoe I had bought in a real long time. Also the most comfy thing I own.
[diajwb2] (score 1, diepte 2) That makes sense. It was a bit of a step outside for me as well. But damn if they aren't comfy.
[diaku62] (score 1, diepte 4) Yeah, if you burn through the insoles, that would definitely be expensive. I'm sorry :(
[diakyof] (score 1, diepte 5 OP) Eh, I'm used to it. Granted, I thought I found the holy grail of shoes for a moment. RIP to my hope.
[dibzwm4] (score 1, diepte 1) this is really good advice
[dicmfwr] (score 1, diepte 2) Except Rolfing is Alt Med bullshit. Same with reflexology. But do the exact same thing, call it "message" and it's a good thing.
[diamfao] (score 1, diepte 0) I have to stop editing my long post, but I had a thought:  how are your feet when you're barefoot? can you go to a beach and walk on the sand? or find a sandbox and see what it's like to walk in it.
[diamkzz] (score 1, diepte 1 OP) Walking barefoot huts. I can do it for a while (and do because I kind of hate wearing shoes) but eventually it starts to hurt worse than when I wear shoes.
[diamyx8] (score 1, diepte 3 OP) Oh, I don't get that feeling. If that's what plantar fascitis is, then no. It feels more like someone is trying to bend the arch of my foot backwards.
[diapnsu] (score 1, diepte 4) plantar fascitis is inflammation of the fascia of the foot from injury, and it keeps getting reinjured, and doesn't let it heal. I don't know if it would always feel like knives.

Do you live near a beach? It might be good to walk in sand
[diav75q] (score 1, diepte 0) What state do you live in? How tall are you, how much do you weigh, and what shoe size so you wear?
[dic76y3] (score 1, diepte 1 OP) They don't *have* to be boots, I just prefer them. The only thing they have to be is subtle or elegant looking and (probably) either black or oxblood.
[dib3ej5] (score 1, diepte 0) I don't know anything about the bones, but the high arches are a problem I have.

2 things helped.

1:  http://www.feetrelief.com/feetrelief/tacco_deluxe_new.htm

These add arch support to any dress shoe or boot that doesn't have it built in already.  I've been using these in Viberg service boots and they work great.  After months of break in I find I can go without them as my foot eventually sinks in and shapes the boot to match.  It makes breaking in a lot more bearable though.  Note that inserts plus the kind of socks you wear can shift your shoes/boot size around.

2 White's boots.  I wish I had discovered White's before I bought the Vibergs.  They have built in arch support and felt good to me right from the beginning.  They've only gotten better as they've broken in.  My first pair was off the shelf but I've bought 4 more pairs all customs.  I wish they made dress shoes as well..
[dic7kuv] (score 1, diepte 1 OP) Seriously considering a pair of whites.
[dibxj60] (score 1, diepte 0) End 25 years of pain with another 2-3 weeks of pain to break-in a pair of GYW shoes? I never had (to my knowledge) shoes of my size give me any blisters but for GYW shoes lol.
[did60eb] (score 1, diepte 0) RM Williams dynamic flex craftsman. Pricey but made exactly for high arches and will last a lifetime if cared for
[div44ts] (score 1, diepte 0) Try checking out Kodiaks... they might be a great option if you're looking for classic, well-made boots. Check them out! www.kodiakboots.ca/en/lifestyle-boots/mens-boots/
[diabta0] (score 0, diepte 0) There are insole you can get on amazon for like $50 that you put in boiling water for 20 seconds then shape to your feet. Same thing they do at most orthopaedic clinics.
[diahpzn] (score -4, diepte 2) That has never been the case when I get sent to the doctors for custom insoles. But, to each their own.

=== THREAD 6blcfy ===
SUBREDDIT: r/goodyearwelt
DATUM: 2017-05-17  SCORE: 45  REACTIES: 52
TITEL: [Discussion] Orthotics: a GYW tragedy
POST (source_id=post):
Over my time here I've noticed a few folks talking about orthotic inserts. Usually, it goes something like "these shoes won't fit my orthotics". For many of us, the amazing footwear we see on GYW, from reviews to MTOs, are impossible to wear. It's tragic but I know that I will be unable to wear most of what we all collectively drool over.  (Cheers /u/Sulucniv).

But, before those of us who are welded to our orthotics give up entirely on finding stylish, well-made gyw footwear, I thought I'd make a thread in the hope we could share experiences, recommendations, and more generally what works—and what doesn't—when it comes to GYW and orthotics. 

Sure, there are orthopedic shoes and other medicinal options, but often these look more like potatoes than shoes. So I'm hoping to focus on footwear that you would be able to review on /r/GYW.

A note on terminology: by orthotics I mean custom made/often prescription inserts created specifically for you by a chiropodist (etc), not anything you can buy off the shelf at the pharmacy. But if you struggle with finding accommodating footwear for your Dr. Scholls, fair game.

So, to those of you who walk like a penguin without your inserts, this thread is especially for you. Let's help each other out. :)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dhnm70y] (score 12, diepte 0) Have you tried Alden's Modified Last?  Game changer for me.  No inserts used, the last is made for high arch, high instep, wide toe boxed, narrow heeled folks.  [Modified last video](https://www.youtube.com/watch?v=mMOfBCnFQ98)
[dhns37q] (score 7, diepte 0) Over the least few years, and about 60 pairs of shoes later, I've found that my feet are a mess.  Split-sized in length and width, neuroma in my right foot, metatarsal pain in my left foot, huge naviculars, narrow heels, partial tear in my right ATFL from soccer.

I'm probably a candidate for prescription orthotics, but I sometimes wear my Wescos with a foam insert from a pair of athletic shoes.  One thing I like about Wesco is they include a full length insert in all of their footwear.  It's usually thick black or brown leather, and it's lightly cemented onto the insole, making them easy to remove.  In my lace-to-toe [*Jobmasters*](http://i.imgur.com/lZPLnIV.jpg), I can wear them without an insert (with thick socks), or I can wear them with an insert (with medium weight socks).  These are my most comfortable stitched shoes.
[dhnnbv6] (score 6, diepte 1) Saaaaame. I don't have flat feet exactly but I have a low arch and I over pronate. Also, the widest part of the inside of my foot is my big toe and not the ball of the foot area. The modified last for me means no heel slip, and no collapsing arch. I've walked many miles in modified Indy's without pain. Well...with the exception of feet swelling and laces needing to be loosened. [Pix barefoot for context](https://imgur.com/a/y1HKG)
[dhoe2yd] (score 6, diepte 0) I should probably mention that Østmo boots are built on lasts that are based on orthotic bottoms. Not custom, mind you, but [here is what an insole that has been molded to the bottom of a last looks like.](https://imgur.com/a/eMFlV)
[dhnjmcx] (score 3, diepte 0 OP) I'll get the ball rolling with two brands I've been curious about:

1) AE's removable insert line (e.g. LGA Wingtips). Although I hate the chunky mall-shoe rubber sole and wish these had a leather or Dainite sole, that these have extra depth and a removable insert is promising. Anyone have experience with these vs the standard AE shoes like Strands?

2) Bared Footwear. Based in Australia, bared.com has extra depth and removable insoles across their line. They are made in China and not GYW, but I inquired into recraft/resole and they said it should be possible, especially with some, such as the Sodium. (A good shoe to compare style-wise vs the LGA above.) I know these might not be GYW approved, but they seem like they could be close, particularly for those of us who have had lots of difficulties in the past.

Apart from these, are there others you know of?
[dhnlil0] (score 3, diepte 1) There's also AE's Ashton Derby.

But yeah, I wear orthotics and it's impossible to wear them with my GYW shoes as there just isn't space for them. The laces get spread out on my oxfords and my instep gets painfully crushed. I've started just sucking it up and wearing them sans-orthotics but it's really not a fun experience. 

I've been coping by wearing cheaper dress shoes that can accommodate orthotics to and from work, while leaving my AE's at work, and switching in and out of them. An incredibly annoying hassle but it's the only way I'm going to be able to walk in any comfort.

This does bring up a question I've been harboring; if I had shoes custom made would they be able to shape it so that I wouldn't need orthotics? Or alternatively, would they be able to shape it to accomodate orthotics (while maintaining a traditional cork footbed) and not overly chunky silhouette?
[dhnmnmk] (score 3, diepte 3) I forgot to mention that; I've tried the Ashton's with orthotics. Removing the footbed allows for plenty of room for orthotics. I placed them in and walked around with orthotics and it felt great (just like other shoes with footbeds removed). Hope that helps!
[dhnmi95] (score 3, diepte 1) I put very thick work insoles (nearly 1/2 inch, I just measured) into my IRs, which I typically wear on my 11 hour shifts, 90% of which I'm standing. While mine are certainly not orthotics, the iron rangers have ample room for added support. 

Since you mentioned sneakers, have you tried experimenting with different soles? Maybe crepe or Christy soles could provide some added cushioning
[dhns265] (score 3, diepte 1) I wore orthotics for years as my GP Dr. recommended I see a podiatrist. 

Now, I'm not suggesting that people don't need custom fitted orthotics or that they aren't a God send for some - but for those who wear them for comfort and not dysfunction this might be of interest..

There's a researcher in kinesiology at the University of Calgary named Ferber who studies this stuff and has found with a few studies (I have no other studies to counter this point) that have shown over the counter inserts that are comfortable are equally as effective as expensive custom fitted orthotics. Below is a link to a news article outlining some of it.

https://www.google.ca/amp/s/sec.theglobeandmail.com/life/health-and-fitness/fitness/off-the-shelf-orthotics-offer-relief-of-running-injuries/article4182759/%3Fservice%3Damp

Like I said, I'm not an expert or suggesting you go against anything a doctor ever tells you - but I've had success finding a cheap insole that gives me the support I need on just my arch for $20 - sure beats my $400 orthotics. And they're low enough profile they fit in virtually any shoe. Food for thought...
[dhoeepu] (score 3, diepte 2) As a mechanical engineer and also a user of custom orthotics, I can see where this study is coming from (also I graduated from the U of C and am familiar with some of the research they have done there) but I am not sure if I can 100% support his claims of off the shelf orthotics as being **equally** as effective as custom. Also, understand that not all custom orthotics are equal. With that being said, I think this research is super interesting and I think its a pretty good question of just how much are custom orthotics worth.

The orthotics I have were made with plaster and formed by hand/mold. I have noticed a huge improvement in my foot/leg health and I am currently doing heavy volume. I do not believe in getting any custom orthotic done if it is not done by hand.

When you consider the options out there, there are some interesting comparisons. Not only that, but orthotics can be used for many things (Arch support, force/impact distribution, fixing improper foot positioning/gait etc.) You have (in general, and these are not at all encompassing):

1 Off the shelf

1.a -Non Molding: Will not necessarily form to your foot properly unless you are very close to the mold. Still can be better than nothing

1.b -Heat Molding: Will form to your foot, but the drawback is that it forms to your foot **with respect to the foot under stress**, ie. it is flattened or has a load exerted on the foot. This will impact shape. Could be a negative impact. Still I believe it is better than non heat molded off the shelf.

2 Custom

Here is where it gets tricky. There are many ways in which custom can be done, including cast by hand. Some methods include automated methods (including lasers, pressure pads, etc.) that will analyze your foot shape/dimensions, pressure distributions etc. and make a shape with the input of the professional practitioner. From my understanding, there is a large shift towards utilizing automated foot analysis on the custom level which I do not agree with.

In my opinion, while automated methods might provide a good orthotic, I personally believe that having a cast molded by hand produces the best orthotic. This is due to the orthopedist etc. actually manipulating your foot to create a cast that will not only ensure it forms perfectly to your foot, but the practitioner holds the foot in a position while it is cast to shape it in such a way that it can fix or manage the underlying problems. Think collapsed arch, metatarsal configurations, etc. that really can only be done through hands-on physical manipulation without a load (standing) being exerted on the foot. 

*Standing changes the shape of the foot and can result in the underlying problem itself. By standing on a plate or on a heated over the counter orthotic, you may not necessarily be shaping the orthotic properly to combat the problem.*

Therefore (again my opinion) bio mechanically, having a physical cast and an orthotics made from it is ideal and something you cannot get from an off the shelf or a machine prescribed orthotic. With that being said, cast orthotics are expensive and also the result will depend on the experience and quality of the practitioner. 

I think ultimately it depends on what you are trying to treat and also how much it is worth. However, from a physics and bio mechanics standpoint, I believe that there is no substitute from having a cast done with the ability to manipulate the cast on the foot by a good practitioner. 

Again, this is my opinion.
[dhnoi32] (score 3, diepte 3) I totally understand and think that is definitely the way to go if that's what your doctor recommends. However...if your foot issues are on the "mild side" the modified last might be a suitable substitute. Kinda like wearing berkinstocks in the summer. The structure is good for certain foot needs and is an ok seasonal replacement.
[dhnvwjp] (score 3, diepte 2) For flat & pronated feet, you actually need TruFlare or TruBalance last rather than Modified.

Yes Modified could accommodate our feet well, esp the widest part & waist, but the higher arch will push against the collapsed arch & cause swelling. Mine has protruding bones on side of ball & sparse gap between toes, wheres even bespoke makers found it troublesome, since I'm only slightly flat feet, but with bony instep & slender heel. 

Will report on my TruFlare V-tip fitting after a while.
[dho1qre] (score 3, diepte 4) For good width fitting - Vans, but no support. Didn't hurt at toe box & hugs the heel. Mine's 0.5 size smaller so I removed the cushioned insole with leather insole. I guess with original insole with right size would do.

I read that New Balance 991 & 587 may work out, may try it out today.
[dho6alr] (score 3, diepte 0) I have had custom orthotics for a couple of years now, and I have not had any problems fitting them into my existing shoes. 

FWIW, I have two pairs C&J - Drummonds (348 last) and Malverns (341 last) and 3 pairs of Carminas. I don't wear the narrowest lasts, but all of my shoes perfectly accommodate my orthotics. I usually just pop them in and put my shoes on. No fuss, no muss.

I don't think you are doomed to wear stereotypically ugly orthotic shoes just because you might have to wear orthotics. I suppose it might help to take your inserts with you when trying on shoes to see how it feels with them in.
[dho7igv] (score 3, diepte 0) RM Williams Dynamic Flex Craftsman has a removable insole. That would your best bet for orthotics in Chelsea boots.
[dhnm19b] (score 2, diepte 2 OP) That's a great question re: custom. I've also been thinking about it, although it would depend on the cost. My chiropodist offers custom made shoes but they are of the potato variety, since there's no attention paid to the style or construction apart from the footbed/support. I don't know if a regular cordwainer could make a shoe in such a way as to build your orthotic into the shoe unless that cordwainer also happens to be a chiropodist.

I would think, however, that a custom shoe could be made to accommodate your insert. For example, were you to stand on the orthotics and include them in your foot measurements. Especially if you're getting a custom last. But I have never had this done and I am speculating on what seems like it should be possible. Has anyone done this?

Have you had any luck with the Ashton or other AE shoes that accomodate insoles?
[dhnjrrc] (score 2, diepte 0 OP) I posted a moment ago about shoes with removable inserts, but I think it would be equally helpful to chat about shoes and boots that are more accommodating but that aren't constructed any differently. I've had some success with Viberg 2040s, but not 2030s. Admittedly, my go-to shoe is a sneaker. I'd love to change that and start building a better collection, particularly when it comes to GYW leather shoes and boots. 

What is working for folks?
[dhopic2] (score 2, diepte 3) Absolutely a great point. Those studies (the ones I read at least) focussed on comfort and less dysfunction; people rated their comfort levels in custom vs off the shelf. I think one of the huge draws of custom is that it corrects all the issues rather than knowing it's an arch this, metatarsal that. 

Ultimately, I think we can all agree foot pain sucks, and whether the answer is custom, off the shelf, or nothing, whatever works for you and your health care practitioner is best.
[dhnsihs] (score 2, diepte 1) Viberg 2040 works great for me; same with the 2045.

My preferred fit is a tight heel, snug waist, wide forefoot and high instep.

I've had good success with Wesco's Jobmaster last, Wesco Western Packer last and Wesco Motor Patrol (regular heel height) last.  The Packer and MP last fit similar to the 2040, but with a taller heel and different toe profile.  The Jobmaster last is fairly voluminous and accommodates an insert.
[dho3gwc] (score 2, diepte 5) Current Vans models are too narrow in the toe box. But the old ones that weren't the classics did fit my width. Downside is the no support and are probably the worst for my feet. 

The 587 is great but very ugly. Not sure if it would work for me because of the shape vertically, same with the 991s. 

Definitely go to a runner's shop, not a big chain. They will do a way better job at getting you what you need.
[dholm4e] (score 2, diepte 4) I mean, don't get me wrong, the Rain-lasted shoes fit me and my orthotics just fine. It's a matter of allowing the shoes to break in more, and that means, I just have to wear the shoes more often!
[dhokhfd] (score 2, diepte 1 OP) That is really neat. Your boots look sleek and don't seem to have a lot of extra depth over the instep and heel. They're also beautiful. And I don't think would work with inserts, although it is nice to see that they look like they have a  supportive footbed!
[dhope69] (score 2, diepte 0) Here's a post right up my alley.  I've been wearing custom orthorics for the past 6 years.  My feet have very high arches and supinate when I walk.  My inserts are actually hard plastic with a high arch and keep my feet from rolling inward when I walk.

I haven't found any GYW type dress or casual shoes that allow my orthotics, but as long as they're not worn for extended periods or heavy walking, I'm ok.  

I also have a wide foot, measures EE to 3E and have found that Thorogood boots have enough room for my orthotics inside.  This has been amazing and allows all day comfort (by day, sometimes it's 16-18 hours in boots)

I've also found that White's Arch-ease mimics my custom orthotics.  I have a pair of Semi Dress boots that I can wear all day, walk everywhere, and my feet and legs feel great at the end of the day.  They've because my traveling/vacation boots as they're that comfortable.  I have a pair of Drew's boots (same last) coming with safety toes for work to replace my Thorogoods and my fingers are crossed they'll allow me to ditch the orthotics in my boots.
[dhp2v4u] (score 2, diepte 1) I love my White's Semi-Dress boots. And my other pair of White's to boot. 

Heyoooo!
[dhp0nvq] (score 2, diepte 0) I wear custom orthotics in all of my shoes (about $300 a set).  They were made by a podiatrist and I have two sets.  The standard set has more support and is thicker, and a pair that is made for dress shoes that are slimmer.

The reason for my orthotics is because I have extremely flat feet.  I started getting knee pain in the last 2-3 years and wasn't sure why - I didn't injure my knees in any specific way.  Now, I no longer have the random knee pain after wearing my orthotics.

For the most part, it didn't impact too many of my shoes.  I have some poor quality phone pics comparing the orthotics against a Viberg Chelsea [here](http://imgur.com/a/dkSNQ).
[dhoka1q] (score 1, diepte 3 OP) This is a great point and it maps onto my experience. I have a couple of pairs of custom orthotics that were made by hand with plaster casts and a new one that was made by pressure plate and making a 360 scan of my feet. 

I don't use the new ones at all anymore if I can help it. The old plaster cast ones are so superior. Unfortunately, they're also big and finding shoes that accomodate them has been so frustrating. And thus this thread was born.
[dhp1zkt] (score 1, diepte 5 OP) It isn't just aesthetic — many shoes I have tried on simply don't fit. And so what I am looking for here is for shoes that might fit, first of all. I'm not really sure what you're getting at?
[dhpcjbb] (score 1, diepte 6) It was a joke, as in I endure some pain because I like the look of the shoes at the expense of comfort. If I really cared I would be wearing runners all day, but work and my interests prevent that.
[dhnoapo] (score 1, diepte 2 OP) I've heard great things about the modified last, although I am a bit hesitant to replace a custom, unique insert for a shoe with more generic support, if that makes sense?
[dhnw3t7] (score 1, diepte 3) Any suggestions on sneakers for my foot type? Caaause I can't find much that would give good support and would be wide enough in the toe box and narrow enough for the rest.
[dhoc8j6] (score 1, diepte 6) I picked Nike Lunarepic Flykit for the style, as expected no support at arch, but it's comfortable.
[dhocd75] (score 1, diepte 7) Too narrow across the toes for me...and the flywire creates pressure points.
[dhoh1kq] (score 1, diepte 8) Also the case for me. We are in the same boat.
[dhp8zfo] (score 1, diepte 6) [FYI the Vans pair, you could see the heel hugs well and just bit shy in length. Picked in sales at 70% off so won't mind] (https://imgur.com/a/fP3Sf)
[dhp9a9y] (score 1, diepte 7) Yeah, I could never do slip on because of the low volume.
[dhpipy2] (score 1, diepte 8) [I see we shared similar shape, so still could try.](https://imgur.com/a/0lKBa) My NEOC slip on works while needed 3/4 insole to grip the heel.
(22 reacties met lagere score weggelaten)

=== THREAD 9bo8pc ===
SUBREDDIT: r/goodyearwelt
DATUM: 2018-08-30  SCORE: 30  REACTIES: 52
TITEL: Inspect your Allen Edmonds Shoes That Were Bought on The Sale
POST (source_id=post):
Bought a pair of brown Normandy’s for ~$250, after the 30% deal. 

They arrived two days after I ordered them, and upon opening the box looking at the shoes, there were scratches and blemishes everywhere. Note, I did not buy a pair of factory seconds, I ordered the brand new version. 

All signs of defects that I found point to the shoe being used prior to being shipped to me. 

Scratches on the boots, sole is worn, etc. 

Your shoes might’ve not been affected, but it doesn’t hurt to check. Already sent them back for return the same day. 

[Evidence ](https://imgur.com/gallery/39hPtk7)

Edit: don’t know why I’m getting downvoted.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[e54mqtq] (score 133, diepte 0) As another owner of these boots I'm 99.9% sure this is how they're supposed to look. This is from the description of the boots:

>This boot honors the greatest generation by recreating their hard working footwear with modern materials such as soft kudu leather that is naturally distressed with scarring, pitting and scratches that make each piece as unique as the self-sacrificing men who wore them.

And between [this picture](https://www.allenedmonds.com/on/demandware.static/-/Sites-allenedmonds-catalog/default/dwbbdad600/images/pdp-overview/brown-kudu-leather2.jpg) and [C.F. Stead's website](http://www.cfstead.com/antelope/kudu-original/), it should be clear that this is not a smooth and pretty leather.

The stain and the chipping on the edge dressing are a different beast, but the imperfect character of the leather is quite clearly advertised.

EDIT: Also, keep in mind that 'brand new' doesn't necessarily mean 'unworn'. Plenty of shoes get tried on and sent back and then sent out to another customer.
[e5541jl] (score 51, diepte 0) You're being downvoted for being an idiot. "These ripped jeans I bought have holes in them!"
[e54qkmi] (score 48, diepte 0) Seriously, read the description. Read the promo material. This is all intended. 

I own a pair. They are incredibly comfortable, and they look amazing. However, they also look like they lost a fight with a belt sander. 



Direct from AE:


Why It's Great



This boot honors the greatest generation by recreating their hard working footwear with modern materials such as soft kudu leather that is naturally distressed with scarring, pitting and scratches that make each piece as unique as the self-sacrificing men who wore them. 


How It's Made



The distinctive characteristics of the leather mean no two shoes are ever alike. The vintage oil-infused outsoles and unlined uppers with natural edges give these boots a look and feel so authentic you’ll think they came straight out of your grandfather's closet.
[e54zvjy] (score 44, diepte 2) Hang on, you aren't happy with the boots so you're buying another pair? They are meant to be distressed, that's why people are down voting I think.
[e54otfg] (score 38, diepte 1) This is correct. I’ve had these boots for a year now, and even the chipping on the edge dressing is a “feature” and not a bug. I love the look of the rough kudu, but it’s definitely a personal choice.
[e54yyr7] (score 36, diepte 0) Wow, it almost looks like the animal this leather came from was walking through thorn bushes, attacked by predators, and then hunted for its hide or something. Crazy.
[e54rs1r] (score 26, diepte 0) I remember looking at these. Then I actually read the ad copy, thought to myself "buying pre-distressed shoes is even stupider than buying pre-distressed jeans" and closed the tab.

Be a savvy consumer.
[e54vt9j] (score 25, diepte 0) KUDU LEATHER is like that. The animal walks through thorny brush all day. If it doesn't come scratched up, it probably ain't kudu.
[e54n0s6] (score 23, diepte 1) Not a clue why this hide would've been made into boots. Unless you dig the look you should have no qualms returning these.
[e54k6ni] (score 17, diepte 0) This is the pair I just received, and I cannot exchange them, because they were the last ones in stock for the whole company, not sure if I should keep them, or just get my money back.  
http://imgur.com/a/1Lxqd3u
[e554f1r] (score 13, diepte 0) Kudu is well known for its purple scarring - it can be considered a feature in fact.
[e54nuby] (score 12, diepte 1 OP) I see that’s interesting. I’m going to buy another pair, see if it’s similar. 

Thank you for your insight.
[e55gnl4] (score 12, diepte 0) You're getting downvoted because you didn't read the description and what is intended as a PSA is basically misleading (unintentionally).

I'm not sure I buy AE's "naturally distressed" thing - I get the feeling there's a distressing station somewhere in Port Washington run by a guy who just knows he's supposed to smack up the shoes without knowing why - but ultimately those are delivered as intended.  I'd guess after wear and brushing all of that blends into something that looks good, and kudu is supposed to be tough as hell.
[e54l645] (score 11, diepte 1 OP) Those are horrid. Return your pair and find a different brand!
[e55ccym] (score 11, diepte 1) Normally I'd agree with you, but all Kudu leather is like this, and it's not so much about being pre-distressed as it is about the softness and suppleness, as well as the pebbly overall texture.
[e54ujp5] (score 9, diepte 1) Looks like the kudu got attacked by a predator.
[e55hupe] (score 5, diepte 1) Best comment. :-)
[e55dxw1] (score 4, diepte 2) Thanks for pointing this out - I'll probably never buy kudu, but it's good to have more information!
[e54q1ds] (score 3, diepte 1) Wow I can’t believe they would have even sent those boots out to a customer.  Those should have been sent to their “thirds” reseller.
[e58ygbz] (score 3, diepte 3) But now he knows it’s by design so thinks maybe it might be cool.  

I see a lot of complaints about blemished shoes on here.  I try to think about what they’re going to look like after I’ve had them for 6 months.  Will the blemish matter then?  On a nice pair of oxfords, maybe.  On a pair of boots?  Probably not.  

But funny to see they turn around from OP.  Unhappy with the blemishes until pointed out to him they’re supposed to be there and then “I’ll give it another try”
[e54qlof] (score 3, diepte 0) Last time I bought shoes on sale from AE I had to send them back twice, the quality controll is absolutely terrible. Before that I was lucky with just one exchange.
[e57ggjr] (score 3, diepte 1) what is wrong with pre-distressed jeans...
[e56m7qf] (score 3, diepte 1) It's kudu leather; it always looks like this.
[e54ylxh] (score 3, diepte 0) I always get shoes delivered to my local AE store. Every time I ask them to order two pairs and there are issues with at least one of them. Don't know what is happening to their QC process but it is lacking. One pair was obviously a half/whole size smaller.
[e56m09p] (score 3, diepte 1) I have a pair of OP's boots; they're actually pretty uniform for kudu. This is what my Enzo Bonafe waxy kudu boots look like, to give you an idea:

https://imgur.com/a/jgjMHn7

It's a beautiful, soft leather and the scarring is part of the charm. Boots made from this leather feel like slippers.
[e54oder] (score 2, diepte 2) Thanks, I'll return them tomorrow.  It's a shame, these fit so perfectly.
[e54twrs] (score 2, diepte 2) More like donated.
[e597o0a] (score 2, diepte 4) Yeah I'm definitely confused about the turn around, I'd rather "blemish" my boots myself through normal wear, but the pre worn look is pretty popular.
[e570kjf] (score 2, diepte 3) Your point is a good one when it comes to low-grade leather passed off as leather “with character”, but kudu is usually just like that. It is not “the cheapest most messed up leather in the market”. That would be shitty cow leather.

Good point, bad example.
[e54tv84] (score 2, diepte 0) I bought the horween sandals.  The right thong is incredibly sharp and would definitely cut my toe if I tried to wear them.  Wtf.  Going back.  Out of 5 new pair of AE shoes I have had to send 3 back for issues.  All firsts.  I was on the fence and kind of done with AE but this sale happened and I needed new sandals.  How do you fuck up a sandal?  So yeah.  I'm done.
[e54vhq1] (score 2, diepte 0) I ordered some neumora monks a long time ago that arrived with one of the shoes where the shell was separating and looked like it had water damage. AE took the return without issue but I was disappointed to say the least.
[e57gg4m] (score 2, diepte 1) no... the animal's skin isn't perfect just like most people may have scars or blemishes
[e56fz1r] (score 1, diepte 1) How much wear have your pair got?  These seem like one of those things that are so much better once they shake off the factory look...
[e56hkr4] (score 1, diepte 2) Probably 20-30 light wears. Hard to wear these hard due to the leather sole, but yeah these will look great after a strong patina.
[e56kfle] (score 1, diepte 3) Write 'em up!  ;)
[e57u5hk] (score 1, diepte 3) I keep waiting for a Normandy with a commando sole, baffles me they haven't done it standard yet.
[e5aysrf] (score 1, diepte 4) Just got the Fall/Winter catalog in the mail and they are actually making it! Looks like they are merging Normandy and Caen into one line, using the translucent commando sole from the Caen and the same brown leather as Normandy as well as a Tan color originally used on the Caen, and the Grey suede from the Caen.

Glad they are finally doing it
[e57uh7j] (score 1, diepte 1) My understanding was AE didnt use real kudu as in African antelope hide, they used Horween "kudu" which is just a distressed style tanned cow hide similar to CXL. Am I incorrect? I own two different CF Stead Kudu leather boots and neither look of feel anything close to what AE uses.
[e57r3t6] (score 1, diepte 2) I don't like buying things that are damaged.
[e54scjc] (score 1, diepte 0) I got some AE lga wingtips on sale this summer and one show had several awful blemishes. Their QC is not what it once was. Never buying a pair ever again.
[e551xnz] (score 1, diepte 0) I bought two pairs of the Surrey Chukka (waterproof suede ankle boot) and one of them had an overly thick insole and didn't seat my heel correctly. The others were fine
[e55ht2f] (score 1, diepte 0) As almost everyone has already said - given the nature of the leather (kudu) and design of boot (army boot) - these shoes are perfectly fine.
[e5d1hxb] (score 1, diepte 0) Sound’s like you need to buy some common sense!
[e54yrdj] (score -1, diepte 1 OP) Smart.
[e54og1i] (score -3, diepte 2) Yeah I'm really disappointed with Allen Edmonds right now.  My other two pairs are great, but there is really no excuse for this.  They aren't even seconds.
[e56qumc] (score -4, diepte 2) That doesn’t make it good or desirable. Just because I call shit tomatoes doesn’t make the shit tomatoes
[e54gmq5] (score -14, diepte 0) Wow, those are pretty beat up and even have stains.
[e54gqom] (score -14, diepte 1 OP) Yup. I’m pretty sure this condition wouldn’t even be acceptable for a pair of factory seconds - but who knows.
[e54p28m] (score -23, diepte 0) Lmao and I was down voted for saying "I heard to pass on seconds"
[e54tt5e] (score -25, diepte 0) I can't believe people fell for this shit marketing. Buying the cheapest most messed up leather on the market and selling it as "vintage" JFC you guys deserve these shit boots.

It's not unique to AE either, every leather company does this and none of them are good. "Wow a brand mark...!"

