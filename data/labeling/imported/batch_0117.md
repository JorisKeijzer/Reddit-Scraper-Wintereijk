# Label-batch batch_0117

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
Schrijf het resultaat naar `batch_0117.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 725oxi, 5z9c6q, 9wqfcy).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 725oxi ===
SUBREDDIT: r/xxfitness
DATUM: 2017-09-24  SCORE: 216  REACTIES: 84
TITEL: Anyone else's feet shrink since losing fat?
POST (source_id=post):
I have gone from a size 8 to a 6.5 in the last 2 years. Never thought about how gaining/losing fat affects foot size.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dnfzb1b] (score 80, diepte 0) I wish :( Size 10 before and after losing 90lbs lol My feet never held much fat to begin with though
[dngpavv] (score 60, diepte 3) 5'5. Size 10.5. Was size 11.5.... I once nearly threw a shoe through the TV when detectives on a BBC murder mystery show deduced a man was a drag queen, instead of having a girlfriend, because the shoes in the closet were large sizes. Bitch, fuck off and die in a fire. But it did give me the idea to shop for shoes on drag queen websites, which led to some fantastic shoes for large feet. so... not all bad?
[dnfyklx] (score 56, diepte 0) I think I read once that the population average of shoe sizes in the US has grown over time due to people weighing more, so it makes at least broscience levels of sense.

Source: um, I think I read it in a news article once? Someone who actually knows something, back me up.
[dng2ufk] (score 39, diepte 0) If you have less weight pressing down on your tarsals they spread less. :) So I had to buy new shoes. I only went down half a size... but also now all my wide calf boots don't fit me anymore. I have to wear big ol' boot socks with them or leg warmers.
[dngh4kv] (score 36, diepte 1) Hey, at least you don't have to buy new shoes!
[dnggzru] (score 35, diepte 0) I used to wear a 6 and now I wear a 3 in youth. One step above velcro. FML. 
On the upside? Light up shoes are awesome for walking home from the gym at night.
[dnfx12z] (score 27, diepte 0) Yes! I've only ever differed 25# and go from a tight 7.5 to a lose 7. I'd be so upset if it was more than that, clothes are expensive enough
[dngkngh] (score 27, diepte 1) That would make sense, but also, people have gotten taller and foot size is proportional to height. A woman who's 5' tall wouldn't need my big ol' size 10 feet. I tower over my Depression-era grandparents who were malnourished in childhood.
[dng1oc0] (score 24, diepte 0) Yes! I've lost 40 lbs and have gone from a 10 to a 9. It sucks because I have a pair of ankle boots that I love that are loose now, and I can't afford to buy them in a smaller size.
[dngoxgs] (score 23, diepte 2) Tell that to my size 9 hobbit feet. They didn't get the memo.

I'm 5ft 2iiiissshhhh.

😂😭
[dng2dsv] (score 20, diepte 0) Yes, my feet are at least .5 smaller.  This is not from losing weight either, only losing fat.  I actually weigh more but at a lower body fat %age.  My feet are ripped, haha.

It's sort of random depending on the shoes though.  

Mini rant #1: Shoes should be consistent!  I have trainers that are 1.5 sizes different that both fit me well.  
Mini rant #2: Has anyone noticed the shoe sizing device at shoe stores is wrong?  I tried it a few months ago and it said I'm a size 9.   I can't physically get my foot into a size 9, that is 1.5-2 sizes too small.  
Are shoes vanity sized now?  /s
[dngbaf5] (score 18, diepte 1) Wear two pairs of socks
[dngzwv5] (score 14, diepte 1) Still size 11 after losing 66 pounds 😂.
[dngc25x] (score 12, diepte 2) And use insoles.
[dng68yp] (score 11, diepte 0) Oh my goodness, this. Years ago I went from a 10 to a 9 and stayed that way for years. Recently I lost a good bit of weight and went from a 9 to 8.5 (bordering on 8 now, I think). Unfortunately in the past year I've picked up a bit of a shoe thing...but before my feet shrunk. Now I have all these high quality designer shoes that just don't fit. :( I've tried the thickest liners but it's just too much of a difference.   
  
Just as frustrating: people don't believe me. They tell me it's not possible. Like, do you want to see my old 10s? And my current 8.5s? They tell me I'm crazy.
[dnggij6] (score 10, diepte 0) Knew a guy who went from 400 lbs to 188 lbs who noticed the same thing. His explanation was that his feet were no longer flattened out like pancakes.
[dnh8nma] (score 8, diepte 4) No, just a woman with a small wallet and an already nice selection of shoes.
[dnh289j] (score 8, diepte 2) Haven't lost weight, but as a fellow size 11 female I understand the pain of having huge feet.
[dnggy8e] (score 8, diepte 3) I have two insoles in a pair of dress shoes because one foot is bigger than the other by about 1 size... totally works!
[dnh2sdk] (score 8, diepte 1) OMG you could totally get those shoes that turn into roller skates. !! Super jealous over here with my extra wide size 9 shoes
[dngzy45] (score 6, diepte 4) Oh my god. . .this is an excellent idea!
[dnh33xd] (score 6, diepte 3) You all must be men
[dngc3t9] (score 6, diepte 0) This is really interesting. I had noticed it in my fingers, but not my feet. I'll go measure my feet later!

I thought losing weight would just affect my belly, but its kind of like magic to discovery new things happening to my body.
[dngiy23] (score 6, diepte 0) I have the opposite - I didn't realise my shoes were way too small until I started running! So I've gone up a shoe size, more like 1.5 now that my feet have spread. Never felt more comfortable.
[dng6vc8] (score 5, diepte 0) Yes. I lost a total of about 70 lbs, and 1.5 shoe sizes.
[dngp1e1] (score 5, diepte 0) No, and I was really hoping they might!  My feet are a women's 13, so any decrease in size would have been brilliant.
[dnhbcbp] (score 4, diepte 1) Too real.
[dng49sr] (score 4, diepte 1) I have the same problem. I have wide feet with high arches. I mostly wear men's shoes because the height and width are more generous.
[dngyazf] (score 3, diepte 2) Silver linings!
[dngpc2v] (score 3, diepte 1) I too lost a lovely pair of wide-calf boots to weight loss. It was quite disturbing to wallow around in my boots!
[dngdqbw] (score 3, diepte 0) Yes! When I was younger and 50lbs bigger, I wore an 8.5-9. Now I comfortably wear a 7.5-8.

I honestly thought I was going crazy.
[dnh6jam] (score 3, diepte 2) 14? Oh how I feel for you! May all the correctly sized, gorgeous shoes come your way
[dngzn28] (score 3, diepte 0) I lost 87 lbs over the course of 11 months, then regained 25 lbs as muscle. [These were my shoes](https://imgur.com/a/UWMKu) before I started.
[dngkxur] (score 2, diepte 4) I'm going to try these ideas! I have a pair of boots that are too big now and I don't want to get rid of them.
[dngf8pu] (score 2, diepte 0) Yup! I have a number of shoes I really liked that no longer fit.

Also high heels are no longer unbearably painful. Now they are just “painful.”
[dnhhop4] (score 2, diepte 2) Ugh. You know what those sound like to me? Certain death. 
I have mild cerebral palsy but I have the worlds shittiest balance due to it.. my feet need to be firmly planted on the ground ha!
[dngpedp] (score 2, diepte 1) Oh woman, all my heartache. I was a size 11, sometimes 11.5. I can only imagine how you feel. 

Have you ever tried drag queen shoe websites? I got some damn fine shoes from them, over the years.
[dngq9qr] (score 2, diepte 2) Yes! I've got some gorgeous ones from them. The trouble comes when I just want a cute pair of flats and not 6 inch heels. Fortunately there seem to be more and more places that I can get bigger shoes, including in the UK. Their plus-size clothes shops have some really big shoes too. I have no idea why the sizing is so wacky but I can fit some of their size 10 shoes and have been shopping my little heart out when I'm there.

The two I've had great success with and who ship internationally are [Yours Clothing](http://yoursclothing.co.uk) and [Simply Be](http://www.simplybe.co.uk/)
[dnh7thn] (score 2, diepte 3) <3
[dnh677b] (score 2, diepte 1) I’m a size 14 and have only kind thoughts for you. Keep strong, sole sister.
[dnh7tvu] (score 2, diepte 2) They were not wearable. They were trashed. I threw them out, hon.
[dnk9wa0] (score 2, diepte 3) Understandable. You sound like me. Wear them until they are destroyed. :)
[dngphpj] (score 2, diepte 0) I'm trans and was in pretty damn good shape before transition, as things have gone along I went down two and a half sizes. It's crazy how much fine muscle is located everywhere. Dropped about 10lbs and had fat/muscle distribute in different places.
[dngvyrh] (score 2, diepte 0) When I lost weight I went from wearing an 8 1/2 to a 7.... my only guess is that the extra weight was causing my feet to splay out more and swell. It was a really unexpected side effect of weight loss.
[dngw161] (score 2, diepte 0) Yep. I never had fat on my feet, even at 275 - I was a small size 7/wide 6.5. Now that I'm at 170, my feet are swimming in my old shoes and I'm having to rebuy shoes in sometimes even down to a 5. It's bananas.
[dnhmzpg] (score 1, diepte 1) 35 at absolute most for me and I went from a 9 to an 8/8.5. What's weird is that I'm currently less than 20 lbs from my largest weight and my feet are the same smaller size? I get it for losing 50+ lbs but 20??
[dnfx2lj] (score 1, diepte 0) Same thing happened to me. Went from being a size 40 (EU), which I had been since I was around 11, to a size 38.5 at age 22. Weird!
[dnfxmgt] (score 1, diepte 0) Yes. I went from a regular 7.5 to 8 down to a narrow 6.5 to 7.
[dnfyrn1] (score 1, diepte 0) I do wear a smaller size now but tbh I think part of that is just learning that shoes aren't supposed to be so loose that they fall off? I don't think I was ever an 8.5 lol
[dng0kt3] (score 1, diepte 0) I went from a 7.5 to an 8 when I was pregnant 12 years ago. 55lbs down now and my 8s are feeling loose.
[dng9ouf] (score 1, diepte 0) I lost 123 lbs and went from a size 9 to a 8.5.  Not much but I still had to get new shoes.
[dnge226] (score 1, diepte 0) Yep, size 9 to 7.5 after losing 30 kgs about 10 years ago.
[dngg3id] (score 1, diepte 0) Yup. Well for me it was the other way around. My feet grew with my weight over the years. From a 7.5 to a 8.5. But I'm losing weight again so I'm on the border of an 8 and 8.5.
[dnggu73] (score 1, diepte 0) Yes! I’ve lost 60 lbs over 8ish years. My shoe size was a solid 8. Now I’m a weird 7-7.5, and I don’t like it. 🙅🏻
[dngh3ds] (score 1, diepte 0) I lost 100 lbs & a whole shoe size 😆
[dngi4xr] (score 1, diepte 0) Yes! I used to be a 10 now I'm a 9!!
[dngmkqy] (score 1, diepte 0) In case you needed more responses, haha, I went from a size 8 to 7 or 7.5 depending on the brand!
[dngmnzo] (score 1, diepte 0) Yup! I lost a full shoe size.
[dngojyt] (score 1, diepte 0) I just went to the store and saw my shoe size went down 1 whole size, I only lost about 18 lbs.
[dnj8dfp] (score 1, diepte 2) Have you tried torrid, avenue and lane Bryant?
[dnkkz8k] (score 1, diepte 3) I'm actually ok now - I found a new shoe passion. Um, they're super ugly by some standards but also super comfy and with all the running I've found I really love the wider toe box; I'm wearing those ones that look super weird, the Lem's and Altras.
[dngp7w0] (score 1, diepte 0) I had to throw out a bunch of shoes. Yeah. It was a bit of an eye-opener.
[dnkkyhw] (score 1, diepte 4) :D
[dngq5si] (score 1, diepte 0) I was an 8.5/9 in high school and now im a 7/7.5
[dngrv0d] (score 1, diepte 0) Mine have went from a 9 to a 7-7.5!  You are not alone!  Buying new shoes throughout the new sizes has been expensive though.  Each time I waited until I thought my feet were done shrinking.  I was wondering every time.
[dngt1u0] (score 1, diepte 0) Yep. Lost 30lbs and a whole shoe size. Buying new clothes and new shoes was very expensive but I did it happily.
[dngu1lu] (score 1, diepte 0) This makes me want to try on my docs from the 90's!
They haven't fit in forever...
[dnguwji] (score 1, diepte 0) Delete.
[dngvphf] (score 1, diepte 0) 7 1/2 to 7 with a 25 lb loss.
[dngvyqs] (score 1, diepte 0) When I lost weight I went from wearing an 8 1/2 to a 7.... my only guess is that the extra weight was causing my feet to allay out more and swell. It was a really unexpected side effect of weight loss.
[dngwr7q] (score 1, diepte 0) Yep. Happens the other way too. Used to be a straight 6 - heels would fall out of a 6.5...now I'm more like a 7.
[dngy76p] (score 1, diepte 0) I think your feet might just be less squished from your weight as well as generally less fleshy. It's unlikely that your skeletal structure of your feet has shrunken, but that being said, if you're less fleshy in the foot and less wide, then your true size is able to become apparent.
[dngzjd0] (score 1, diepte 0) I wish. As I've gotten older, my feet have grown a full size over the past 6 years.
[dnh30nq] (score 1, diepte 0) My feet became less wide and fit shoes better but still a US9.5. It is so damn hard to find cute shoes.
[dnh7c4k] (score 1, diepte 0) So this is not exactly what you're looking for, but I'm pretty sure it's perfectly normal to lose fat in obscure areas of the body.  I personally went from 203lb to my current 170lb and my *face* shrank quite a bit.  I know u/ellacofficial made a post about her *hands* shrinking.  So it's nothing to be worried about, unless you made a bet with someone about your feet staying the same size.
[dnh9gms] (score 1, diepte 0) My best friends mom lost about 70 pounds and her shoe sized shrunk. I cant remember by how much thou.
[dnhac6h] (score 1, diepte 0) I did go down from 7.5 to 6.5. The odd thing is that I am not a size that I wasn't before pregnancy. Before having children my shoe size was a 7.5 and my pants size was 4. After weight loss my shoe size is 6.5 and my pants size is 4. It drives me crazy that I have all these shoes I can't wear.
[dnhcn94] (score 1, diepte 0) Relevant, my feet went from an 8-8.5/9 after lifting. I dont know what explains that lol
[dnhjxr2] (score 1, diepte 0) YES. So glad to see I am not alone! I was 6.5 and now I am a 5.5/5 (depends on the brand of the shoe). My feet are so narrow I have to buy Dr Scholls to make my shoes fit better. I have super tiny feet for my 5'6" stature. My friend teases me all the time for it.
[dnhkuph] (score 1, diepte 0) Yes! 
I’ve only lost 10lbs but I actually started seeing the feet loss the fastest (feet, fingers, ankles, knees and wrists were the first to go, weird af)

I went from a US 8 to a 7.5 (7 even sometimes) - not too much of an issue for boots, very annoying with high heeled shoes. But I find it to have been a great problem haha
(6 reacties met lagere score weggelaten)

=== THREAD 5z9c6q ===
SUBREDDIT: r/xxfitness
DATUM: 2017-03-14  SCORE: 180  REACTIES: 78
TITEL: My fiancé has recently started going to the gym with me and she mentioned that her feet get numb (fall asleep) when she's on the elliptical for 20 minutes or more. I thought this was odd but she said that it has always been the case. Any idea what's causing this?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dewcoa3] (score 253, diepte 0) This is a pretty common issue! My understanding is it's just the pedals and the motion stimulating your nerves in a weird way.

Some things that have helped me:

* different shoes
* switching to going backwards every so often
* picking my feet up and re-positioning them on the pedal every so often
[dewcckc] (score 59, diepte 0) I wish I had advice but I'm in the same boat... really curious to see some answers on this one! 

She could have her laces tied too tight, but if she's like me her hands and feet may go numb randomly at other times too. My right hand falls asleep while I'm in bed Every. Single. Night.
[dewhk6l] (score 54, diepte 1) May also be a good idea to place feet just a tad further back on the pedal so toes don't squish into the front of it. I know that usually makes my toes go numb, but pretty much all of what you said!!
[dewcn0m] (score 37, diepte 0) Tell her to see a doctor. I had the same problem, and there are a lot of more common causes for for numbness (u/dotheraptor37 mentioned shoe laces) but for me it was a network of cysts growing in my foot that were cutting off blood flow.

EDIT: Since there seem to be a few other more extreme options floating around (compartment syndrome, OUCH!) I'll just let ya'll know my other symptoms as an "in case". My numbness, once I really looked at it, was pretty obviously related to bloodflow, as my foot and ankle would go ghost-white. After months of not getting it looked at, one of the cysts settled in right under my ankle, so I now have what appears to be an ankle immediately under my ankle. Weight loss has lessened the numbness to the point that it's bearable, but to get it actually removed would require surgery, after which there's a 50/50 chance of it returning. Mostly we just monitor it to make sure it's done growing.
[dewho1t] (score 31, diepte 1) For anyone who thinks their laces might be tied too tight, I strongly advise you to loosen your laces. I have permanent nerve damage in one foot due to having the laces tied too tightly for work. The whole top of my foot and partway up my calf can only feel limited sensation now for me.
[dewkxq9] (score 29, diepte 0) My wife subs to this and sent me a link to share my experience.

I use to have a very similar experience when doing any type of cardio activity: my feet would go numb about 20-minutes in and it would eventually subside after rest. I sought out help in doctors, physical therapists, and fitness trainers. All had similiar advice for me that it was either shin splints or that I just needed better shoes or insoles. The problem is, is that shin splints should get better with enough rest and not happen again the very first time excercised is attempted again.

The symptoms got worse without treatment and I started getting severe foot drop along with numbness. This resulted in tearing all of the anterior ligaments in my ankle when a 45-lb pack decided to take me for a ride. At this point, I started seeking out various orthopedic doctors trying to figure out what was going on. I got several more "it's just shin splints" or "you need orthodics" answers until I found my way to a doctor who finally said "I know what you have".

The doctor rolled up his pants revealing a six inch scar up each side of his shins. He told me that he was diagnosed with excercise induced compartment syndrome as a teenager and that his frustrating experience getting a diagnosis is what led him to be an orthopedic surgeon. He had me a do an intracompartment pressure test where I excercised for 20-minutes and a needle was inserted into my legs measuring internal pressure. It confirmed his suspicions which was the fascia that surrounds major muscle groups were not allowing my muscles to expand when they swell with blood under exertion.  

The "cure" for excercised induced compartment syndrome is fasciotomy surgery where the tissue that keeps muscles in place is cut open to allow the muscle to expand unimpeded. Having this done fixed my issues.

Anyway, that's my story and I always like sharing it so that if there are people out there who may have excercise induced compartment syndrome that they know it exists and can speak to their doctor about it and ask for the proper diagnostic procedure. Hope it helps.
[dewcnh8] (score 28, diepte 0) I had this, I found out that I. Old alleviate the pressure by loosening my shoelaces near the toes. Also, she should lean back a little bit so she is putting most of her weight on her heals.
[dewjsww] (score 16, diepte 2) How long ago did this begin? I had what I was told would be permanent nerve damage (meralgia paresthetica) from what was essentially having the nerves squeezed too tight for too long (from a long surgery with me strapped too tightly to the table) and my nerves repaired themselves after ~3 years. Hopefully you regain your sensation as well!
[dewfqp6] (score 16, diepte 0) When this happened to me, my shoes were too tight. I switched how I laced them to something better for high arches, and that resolved the problem.
[dewmo1n] (score 15, diepte 1) I had this my whole life until I switched to great shoes. Now I enjoy it so much!
[dewcx77] (score 14, diepte 0) I'd def see a doctor, but check both shoelaces and how tight her pants are. no joke. both joints on the legs offer places where compression wear can pinch nerves.
[dewdafo] (score 12, diepte 0) Always had this on the elliptical. I just choose other ways to get cardio in.
[dewk765] (score 12, diepte 1) [Lace like this!](https://static1.squarespace.com/static/555c964fe4b07d15252a8927/55dbbb7ee4b0aac652a9b64f/55dbbb94e4b0aac652a9c208/1440465372400/lacing-your-running-shoes-for-fit-and-function-he-and-she-eat-clean-cardio-runner-high-instep)
[dewobr5] (score 9, diepte 3) It was around 3-4 years ago that I originally damaged my nerves, and the skin on my calf is sort of.. dead? really rough? and while I've had some improvement (my foot used to be completely numb), it still feels like I have permanent pins and needles whenever someone touches my foot and it is super uncomfortable.

Hopefully over time it will improve more, as it sucks!
[dewhc1n] (score 9, diepte 1) Same here, I'll opt for the treadmill or stair master instead. I even tried the elliptical barefoot to make sure it wasn't my shoes or laces and still went numb.
[dewidpc] (score 9, diepte 0) My "used to happen to me" story is that I have something called chronic compartment syndrome that required a surgical fix. It certainly might not be the same problem as your fiancé, but it's clear that there are several potential causes that are probably worth investigating.
[dewgslr] (score 8, diepte 0) Chiming in on the "me too!" train.  I also thought it was that my shoes were too tight but loosening them didn't seem to help.  What has helped for me is to occasionally wiggle my toes or just slightly roll my ankle a bit when it starts to happen, or just every 10min or so.  I still don't know why it happens, but seems to be a good trick to prevent it for me.  My guess is its about circulation, considering I get "frost feet" at night (according to my husband, lol) and have  hypertension.
[dewejfu] (score 7, diepte 1) are you leaning on your arm when it falls asleep?
[dewsybq] (score 6, diepte 2) I switched out the laces in my gym shoes and put in these: [Kicks Silicone No-Tie Shoelaces](https://smile.amazon.com/gp/product/B01AKQ1PIY/).

Not only are my shoes now slip-ons, which I strongly prefer, but the laces never over tighten. I do mostly weight training with some machine cardio, and I've never lost or felt close to stepping out of my shoe.

My husband now uses them in most of his everyday sneakers.
[dewj3yp] (score 6, diepte 1) Does it go numb in a particular pattern? 

My arms (started with just my right) began falling asleep in bed. I would raise them up over my head thinking I was pinching a nerve in some way. I started to notice that they would be numb from my elbows to my fingers, but only my thumb, index, middle finger, and half ish of my ring finger. My doctor confirmed bilateral carpal tunnel syndrome and while it is well control by steroid injections about once a year I plan to get the surgery done.
[dewjqui] (score 6, diepte 1) :O What did they do to treat it, if anything?
[dewurff] (score 6, diepte 1) Yes! Picking up my feet and repositioning them was always a huge help to alleviate that numb feeling for me. I'd also loosen up my shoe laces a little bit. 

No idea why it happens, but the elliptical is the only machine that ever caused that sensation for me.
[dewvrlh] (score 6, diepte 1) Ugh, the surgery ruined my leg even worse. Now I have permanent nerve damage from a botched surgery. I urge anyone with CECS to be VERY careful before getting a surgery for this ailment. My issue was probably some peripheral nerve entrapments of the leg in addition to CECS from the beginning. Now I have nerves that are cut in half and the nerves in my leg are covered in neuroma. Please be careful. Don't run through CECS. I did that, and it made my CECS and nerves even worse. I now live in pain 24/7 and am out of options aside from getting a ton of surgery that may or may not work (sounds crazy, but this is one option) or being on medicine (that doesn't work) forever. I have been trying an experimental treatment for nerve entrapment and damage and am having some very small amounts of success with that.
[dewmbl2] (score 6, diepte 0) Apologies if this is a repeat, but I fixed this issue by placing more weight in my heels when using the elliptical. I was putting all of my weight in my toes, and the angle would lead to numbness. I have to focus more to keep my weight evenly distributed over my feet but it fixed the numbness.  I also think it leads to a better workout.
[dewd73x] (score 5, diepte 1) Same on the hand thing.
[dewjge5] (score 5, diepte 0) Sometimes Celiac disease can cause numbness in the extremities... if it is happening outside of exercise, I would go see a doctor!

Source: My aunt recently was diagnosed, and that was one of her symptoms.
[dewfxbw] (score 4, diepte 2) Same thing happens to me, and no. It doesn't matter what position it's in, it goes numb. No idea why.
[dex50wk] (score 4, diepte 2) If you are having numbess in all your limbs you should get your thyroid and b-12 levels checked by your doctor.
[dewei1i] (score 4, diepte 0) Oh man! This happens periodically when I run. Mostly on concrete. I try to rotate between running shoes every couple of days and it seems to keep it at bay. I've destroyed both of my ankles, thank you high school sports....but I went to PT and they never mentioned nerve damage.
[dewyz8r] (score 4, diepte 1) I've had "shin splints" for years and even told my Dr that compartment syndrome matched the symptoms better. He refused to test for it because I was military and it would make me undeployable, which I couldn't deploy anyways due to mental issues. 
I'm glad that you got help.
[dewn7ey] (score 3, diepte 1) I had a doctor tell me it was carpal tunnel. If it's the thumb, pointer and middle finger, it's carpal tunnel. If it's the whole hand, it means it is having the circulation cut off. 

I notice when I cut out wheat it goes away, and when I told my doctor she said that she has heard other people say that too. Worth a shot?
[dewmvd3] (score 3, diepte 2) The peroneal nerve, which runs the length the lower leg, is susceptible to compression which can cause symptoms like foot drop and muscle weakness. People can cause issues with the nerve just by sitting with their legs crossed for too long. I'm guessing when you sat on your ankles you were causing compression of the peroneal nerve or one of its branches which was giving the issues.
[dewmwmp] (score 3, diepte 0) I used to have this issue, and switching up the way I lace my shoes completely solved it. It also decreased bruising/pressure points/top of foot pain after long runs for me. Couple options to check out:

* For the free option, I started by switching to the straight-across lacing [shown here](http://running.competitor.com/2015/05/photos/3-ways-to-lace-up-your-running-shoes_128380)
* Later, I got a pair of these elastic shoelaces which I can lace normally but have enough stretch to be snug and super comfortable ( [LockLaces](https://www.locklaces.com/) )
[dewr9h6] (score 2, diepte 3) > my nerves repaired themselves after ~3 years.

Did they?? Glad to hear it! I have paresthesia (still figuring out why)... that is good news!
[dex04my] (score 2, diepte 1) I got tendonitis in my right arm last year and it goes numb if I bend my elbow at night. I figured out a lot of it stems from my neck and shoulder. Look into neck traction and doing physical therapy if you can!
[dewwcwn] (score 2, diepte 2) Basically we've been monitoring it since. There are a couple different options (draining it, surgery, etc.), but because we're not sure where the exact source is it's likely it'd come back. So instead I lost a bunch of weight so that when I run there's as little extraneous tissue on my foot to swell as possible. It only delays the numbness, doesn't cure it, but I don't plan on running longer than a half anytime soon so it does the trick.
[dez4nma] (score 2, diepte 2) yeah, even before i start working out this can happen to me if my shoes are too tight. my feet don't seem to swell up very much on their own but i don't have great circulation to begin with so they are really sensitive to tight footwear.
[dewhnyc] (score 2, diepte 0) This used to happen to me - my feet would also go numb when running. I switched shoes and it made a huge difference!! I actually went minimal, but probably if she goes to a running store and has them give her a good reccomendation she will be able to get something more suited to her anatomy and exercise habits.
[dewiymi] (score 2, diepte 0) I have that problem moreso on the treadmill, but I'm pretty sure that for me it's that my quads/IT bands are super tight. It seems to help when I roll out before I run.
[dewuj0b] (score 2, diepte 1) I was diagnosed with a fascial hernia years ago when I was having high ankle pain while excerising.  From my research then I think it was related to or could turn into compartment syndrome.  I also get foot numbness on an elliptical (even when not wearing shoes).
[dewr24a] (score 2, diepte 1) How do you place weight in your heels? I can't even get my heels to stay on the pedals while I move, my ankles don't bend enough to allow it.
[dewtz3q] (score 2, diepte 0) It could be nothing at all, just a change in the way her foot sits on the pedal, or a change in shoes or loosening of laces. But I'll share my story for kicks.

I'd been running about 6 miles 4 days a week for a few years and all of a sudden my right foot would start getting tingly on runs, and my toes would go numb. EVERYBODY told me, it's just your laces, your shoes are too tight. I'm not an idiot, I'd been tying my shoes the same way for at least 2 years. I had on super nice running shoes too, that were fit for the type of under/over/normal pronation that my feet do on runs. Well it ended up like this; my new running shoes, as nice as they were, were not stiff enough. My feet are super hypermobile (diagnosed with EDS after this happened), and the (excessive) movement of my foot, my big toe specifically, was causing stress on my posterior tibial tendon and my 3 middle toes. This caused my tendon so much damage that it's now somewhat of a chronic condition (posterior tibial tendonosis), the tendon ended up frayed like an overused rope. I woke up one day and couldn't walk on my foot at all, went to a doctor after a few days of that and she found out about my super hypermobile feet. Later diagnosed (because of other symptoms I have) with EDS. It also caused me to get Morton's neuroma. I wear special food pads now to help put less strain on my middle toes, I had to cut back my exercise to 3 days on and 1 day off, and of course it took me like 1 full year to be able to get back to running and my whole routine. I also got the correct running shoes, Asics are the only shoe stiff enough for me. 

Sorry for the history of my life lol. Short story is it could be nothing, but it also could be something! Monitor and try different things.
[dex0p6q] (score 2, diepte 0) Also maybe look in to placement of shoe laces. A lot of girls I run with solved this issue that way.
[dex54dv] (score 2, diepte 0) This is such a common problem i wrote an article on it [here](http://blog.pop.fitness/do-your-feet-tingle-after-the-elliptical/). 

"Have your feet ever gone numb, tingled, or just felt “funny” after using the elliptical? I know mine have!

The elliptical is an excellent device for performing low impact cardiovascular activity. It’s easy to see why it’s loved by most who use it! But when you start to feel numbness and tingling in your feet it can be pretty frightening. If this is something you’re familiar with, i’d like to offer a few suggestions to fix this issue.

 

The most common culprit is…. your shoelaces are tied too tight! I know this seems silly and too simple, but this is almost always the cause of numbness. Next time you hop on the elliptical, try tying your shoelaces tight enough for your shoe to stay on, but loose enough that you can easily move your feet within your shoe.
 

Your shoes are a size too small. Generally we have a good idea of what does and does not fit us, but sometimes you may have a shoe that is too small due to manufacturor errors, inconsistent sizing, or even feet that are in-between sizes. In my opinion, it’s best to find shoes that are comfortable with a little wiggle room! If you can swing it, go up half a size!
 

Your placing your feet improperly on the pedals. It’s important that when you use the elliptical that your entire foot is touching the pad. Downward force should be generated from the entire foot, not just the heels and not just the balls of your feet. If you are placing your feet or applying force improperly, it’s easy to see why you might experience this problem!
 

If these common solutions don’t work and you continue to experience numbness and tingling while performing cardio, we suggest heading to your doctor to ensure you don’t have an underlying medical condition (such as poor circulation, neuropathy, and more). Don’t worry, most of the time this problem is resolved simply by loosening your laces and wearing proper fitting shoes!"
[dewn13v] (score 1, diepte 3) I can change position and sensation returns or sit back, or do some simple circles exercise.

My right foot, well parts of it, are half-numb and it always feels like the sock is twisted under the ball of my foot.  

I can understand that something has changed since the time I did not have pain. My model is that something has been pressing on the nerve.

Sometimes I have to sit down and lean back a little because the numb has grown and bothers me. There is another sensation  not just numb bit I do not have a word for it.

Right now I have a sharp.paino, on use, in the segment between the first and second knuckle.
I always find these specific sharp on contraction sensation odd. They are unlike any pain I have read about. Usually small arm circles take care of it.
(33 reacties met lagere score weggelaten)

=== THREAD 9wqfcy ===
SUBREDDIT: r/Fitness
DATUM: 2018-11-13  SCORE: 104  REACTIES: 77
TITEL: Flat Feet issues + calf workouts
POST (source_id=post):
Hi y’all,

To give you the tldr, I have some bad issues from
my flat feet. They are not immobilizing issues by any means but they do really limit what I can do in terms of leg workouts. 

Basically anything that involves flexing the soles of my feet is really painful and I can barely get through one set of extensions without my feet literally giving out and not being able to walk for several minutes, not back to full comfort for maybe an hour. 

Any suggestions on to how I can build calf muscles without aggravating my feet?

EDIT:

Wow thanks for all the replies. Was not expecting such a large response! 

Perhaps I should have gone into more detail. 

I already have custom insoles and have had for years (although I skipped when I was a teenager because I was stubborn and didn’t understand the concept of long term effects)

I have been seeing orthos and podiatrists for years now. From what my most recent podiatrist has communicated to me, my flat feet are REALLY severe - he’s said that they’d benefit from a surgery even (soft tissue) and said they’re on the cusp of absolutely needing the surgery. I’m not going to do the surgery though because recovery time is a year before I can have full ability to walk without some kind of assistive device like a boot or a crutch.  

Other things he’s said: 
As much as you can, avoid walking without your insoles. My flat feet are impacting alignment in my legs and up my kinetic chain that can really screw up my posture. Walking without corrective orthotics is just not good for me.. even at home I should be wearing shoes he said.

As long as I’m using insoles I can do as I want, but he can’t do anything to drastically improve my comfort during exacerbating activity. 

To paint a more accurate picture: 

- I work as a server and manage just fine (My feet hurt yes, but it’s totally manageable) 
- Taking a long hike is pushing it but still accomplishable. 
- Running for cardio is a no. My feet will start really hurting, feeling like my foot has been hyper extending. 

I do trust the podiatrists assessment and intend to remain using the orthotics. 

I have invested a lot of time and money (in trainers) into finding ways to workout without aggravating things and have been rather successful... except with my calves. I just can’t seem to find a way to isolate them without really activating my feet in a way that is painful.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[e9ml9bj] (score 35, diepte 0) I have flat feet too - there are insoles you can get that you put into your sports shoes (I've had them in mine for \~4+ years now) and they basically have curves/bumps around the arches to help arch and strengthen it a bit. I would highly recommend you looking into getting one.
[e9mjkmd] (score 21, diepte 0) You need to do physical therapy to strengthen your arches.
[e9mkswr] (score 21, diepte 0) If anytime you flex your soles you are experiencing pain -> see a doctor/physical therapist. 

If anytime you flex your soles *with added weight* you are experiencing pain -> decrease weight severely. If the machine/weights set doesn't go low enough to eliminate pain, switch to bodyweight until you are better off.
[e9msusb] (score 21, diepte 0) I'm going to go against the grain here. I've had flat feet my entire life, went the prescription orthotic route, which helped a little, but not entirely. Once I outgrew the prescription orthotics, I went to OTC orthotics for a while.

The only thing that finally helped me was ditching arch support entirely. I'm barefoot as much as possible now. When I wear shoes, they are as minimal as possible. The only time I wear "real" shoes is when I'm at work. It was uncomfortable at first, and I definitely didn't ditch the support all at once. I eased into it. But my feet have never felt better. It's been about 3-4 years since I stopped wearing orthotics and shoes with arch support.

Of course, all that is anecdotal and specific to my situation. So, take from it what you will.
[e9moi4l] (score 13, diepte 1) Also have flat feet and azarro is right. Insoles have been a huge change for me. If you already have them and still have issues I'd recommend going to see a physio.
[e9mldwg] (score 13, diepte 0) See a physio.


Basically,  start with what they call “doming”.  Search up on YouTube.


Strengthen, glutes through clam shells, bridges, etc:


Eventually work to  half squats while maintaining your dome, progressing your squat deeper while maintaining dome.


Go to a few physio sessions they will show you all of this.   You won’t regret taking the time to correct your dysfunction.
[e9miw7y] (score 9, diepte 0) Stretch em? See a doc? I dunno if there's anyone here qualified to answer that question.
[e9mppq8] (score 9, diepte 0) Kinesiologist here: work on your intrinsic muscles of the medial longitudinal arch (aka your arch). Start off by keeping you feet flat on the ground and create an arch by pressing the ball of your big toe and heel into the ground and trying to “bring them together” 
Tactile feedback helps. Place a pencil across your arch. Try to lift your arch off the pencil, but keeping three points of contact on the groun (ie the heel, ball of big foot and ball of little foot 

Work on your abductor muscles. If you knees cave in during squat performances or any leg exercise, you should work on your glutes to help lift the arches. If you present genu valgus in your knees, that can attribute to flat feet. Work those buns! 

Good luck :)
[e9mrvgp] (score 6, diepte 2) Because "see a doctor" is the most correct answer to this question.
[e9mm4hm] (score 6, diepte 0) Flat feet since I was born.  You need arch support in your shoes.  The best is to see a foot doc for customer orthotic inserts.  The second best would be to check out Spenco brand or similar and order a few for your shoes.  

I literally cannot walk without intense pain without inserts for more than a day or two.
[e9n44ql] (score 5, diepte 2) Sorry, I don't quite remember any details about it since I got it a while ago but they were custom-made for my feet/shoes. When I get home, I'll see if I can dig up more details about them!
[e9nb0lf] (score 5, diepte 1) Same here. I have flat feet and started working out at home about a year and a half ago. Because I was at home, I always went barefoot, and apparently, that builds up a lot of stabilizing muscles in your feet. I believe it, because after a few months my feet started looking really vascular. I've since joined a gym and unfortunately can't work out barefoot, but I do the next best thing: chucks. They're flat as flat can be and they feel great to work out in.

Edit: Because other people are talking about walking around on their toes I'll add - I mostly walk without touching my heels to the ground. It has the added bonus of scaring people by appearing out of nowhere because my footsteps barely make a sound.
[e9nipa7] (score 5, diepte 1) Arch support does nothing to strengthen the foot. It's a total crutch that can help you function but it will not fix anything. So going without is how your feet can get stronger. But you need to actually use the feet and bare foot is a good way to do that.
[e9n1c95] (score 4, diepte 1) What insoles do you use?
[e9mye3c] (score 3, diepte 1) Same here! Already shared a top-level comment with similar details so I'll leave it.
[e9o1o9e] (score 3, diepte 1) +1 Arch-supporting insoles just mask the problem, which is generally weak calves. Recommend barefoot calf raises AMRAP a couple times a wekk - will help with your arches.
[e9my935] (score 3, diepte 0) I've had flat feet my entire life and wasn't going to respond but I wanted to give another option other than "get insoles" which seems to be a popular reply here.

Years ago, I couldn't walk for any length of time without shoes as it would cause my feet to hurt. However, to address this I took the "minimalist" approach of going without shoes for as much time as I could. Over time, my ability to do this increased and I also switched to wearing minimalist shoes (flat, zero-drop soles with no arch supports) during those times where being barefoot wasn't possible. 

It took over a year but now I'm most comfortable when barefoot and have no issue walking on hard flooring all day without shoes. I never have issues or pain of any kind in my feet now.

So, instead of taking the approach of propping up your feet with more and more support you could do what I did and teach them to work perfectly without any supports at all. YMMV.
[e9mtml3] (score 2, diepte 4) this sub bans medical advice first of all. While this isn't exactly medical advice, he did respond in a relatively polite manner and also suggested to stretch them. I don't know what else you're looking for. 

Most people *should* ideally have access to a Dr. That is the correct recommendation.
[e9mtnf0] (score 2, diepte 4) Then he's SOL like the rest of uninsured America when they get sick or injured.
[e9mshex] (score 2, diepte 3) Yep. I have flat feet as well. The effects are far-reaching and some are deviously subtle. It changes your posture so your hips / back are slightly off, which affects your thoracic spine and thus upper body posture. It affects your gait, obviously, but that also changes weight distribution, the way you develop power in your legs, how you use quads vs hams vs glutes, etc...

So "see a doctor" is what OP should do. Especially since they get debilitating pain. And get referred to a physiotherapist. And a sports medicine professional who works with athletes in their field.
[e9o8sx5] (score 2, diepte 1 OP) Hey friend, thanks for the reply. I’ve added some more details above that might clear things up.
[e9mmnqy] (score 2, diepte 0) Younger I had insoles to fix them, you can probably find some that maintain the arch.

I was also told to walk and run barefoot on the beach (sand), it would build up better feet.

No idea if it's in the books but if this is an option for you, it's a much prettier cardio than the treadmill and a dog would love it.
[e9o8z5q] (score 2, diepte 1 OP) I’ll look into doing that! I’ve added some more detail in my post btw. Would love to hear our thoughts with the extra info!
❤️
[e9pezrh] (score 2, diepte 4) For your calves, use a theraband and work on feet/ankle plantarflexion in a seated position. No weight bearing on feet but can still work your calves

It will take time. Esp if you may need surgery as told by your professional. 
Yes knee and hip pain can come from deadlifting and squatting with poor biomechanics. But pain in knee and hip can also be from poor posture, tight hip flexors...etc. 

I’d recommend getting a physio or kinesiologist to look at you as a whole as our bodies work as a kinetic chain. We can experience neck pain that stems from poor feet alignment. Crazy stuff our bodies can go through
[e9nsemd] (score 2, diepte 1) Yes, orthotics can hide the problem but not cure it. Going barefoot was one of the best decisions I ever made
[e9nukw2] (score 2, diepte 1) Yea. I was gonna suggest vibrams. My shoe size went down a bit after a few months of running in vibrams due to the added arch.
[e9o8u97] (score 2, diepte 1 OP) Thanks for the reply. Unfortunately based off what my podiatrist has said (as I’ve described above), I should not be walking around without corrective orthotics.
[e9mv01a] (score 2, diepte 0) I have had flat feet since I was 3. 5 decades later, for me personally shoes even with orthotics, inserts etc aren’t comfortable. And yes, I’ve even had them custom made. It wasn’t until I opened a spa and started getting monthly massages (including the feet) that my feet started feeling better.  What also helps is walking barefoot as much as possible,  it stretched and strengthened my feet. As for easy calf raises, uses stairs, no need for machines as you are using your natural body weight. Use your calves to go both upward and downward. You can start with 5 and do it throughout the day. Also, write the ABCs with your feet as you watch tv or lie in bed- you’d be surprised how much good stretching can help.
[e9mv3mg] (score 2, diepte 0) Sports medicine fellowship trained podiatrist here.  Appropriately made custom orthotics depending on the planal dominance of your deformity can help immensely.  They will not strengthen your arch, your foot structure is genetic and musculoskeletal in nature.  Think glasses for someone who can’t see.  If your deformity isn’t severe over the counter inserts can work well, my favorite if you’re in the US is the green colored superfeet brand.
[e9p3prr] (score 2, diepte 1 OP) Thanks. I'll check out your recommendation. 

Any recommendation as to how I might be able to exercise my calves without aggravating my feet?
[e9mvdw5] (score 2, diepte 0) I have flat feet and the same thing happens. I just ignore it the pain because it goes away afterwards.
[e9mvpd7] (score 2, diepte 0) What helped me have amazing feet for one summer was to jog barefoot on grass instead of the tarmac+shoes next to it. You get weird looks when you take off your running shoes as soon as you reach your running destination but it helped immensely. It even helped me to understand how i am actually supposed to run. When i finished a few rounds barefoot and went back to my shoes i could still feel how i would be running if i were barefoot and that helped alot in my movement.
[e9o821u] (score 2, diepte 1 OP) The raises are what I mean by extensions. It’s possibly the most aggravating thing I can do for my feet. Is there anything else I can do to isolate my calves?
[e9o9smz] (score 2, diepte 3 OP) Ya that’s my impression to. Overall any kind of exercise involving impact is a toughie. 

I think I might just have to weave some raises into an upper body day, so it doesn’t interfere with other leg workouts. Even then it’s tough to get through enough sets to really build they way I do with my other muscles. 

Cheers!
[e9nsrk9] (score 2, diepte 1) You just walked without support? You didn't consciously maintain an arch? Step with the blade of your foot and toes? You literally just walked around *not* thinking about how you walk and flat feet just cured themselves?
[e9nbth0] (score 2, diepte 0) Strengthen your posterior tibialis muscle.
[e9nvoow] (score 2, diepte 0) I do inserts (Super Feet), but I also find yoga poses that extend my feet help. Lightning pose has become one of my favorites.
[e9mtefc] (score 1, diepte 4) Everyone should have insurance. And if not, then its not hard to make an appointment and pay in cash.
[e9mudoi] (score 1, diepte 4) Ya, I'm incredibly flat-footed and when I got prescription orthotics it really changed a lot for me in the gym. I think that's the best course of actions + doing easy form exercises that focus on the thoracic spine.
[e9mwr2h] (score 1, diepte 2) Because giving medical advice is specifically against the rules of the sub.
[e9p39v7] (score 1, diepte 1 OP) Perhaps, but there is only so much that physical therapy accomplished. Fact is that I just have bad arches and structure and have to work with what I've got. Just can't figure out how to hit those calves though :/
[e9pfjge] (score 1, diepte 2) Same pain if you do it on one of those inclined leg press machines?
[e9plyh0] (score 1, diepte 3 OP) Leg Pressing is ok because I can push through my heels. 

If you mean using the machine to do a calf extension then the answer is yes. Still painful. the issue is the extending of the foot and flexing of my soles. Angles don't really do much to help.
[e9pojr4] (score 1, diepte 4) That is what I meant and I'm sorry to hear that. I have arch problems too that developed only recently and what I'm doing is to do like half weight calf raises by propping myself up on a metal rail at my gym and doing the raise without having all my weight on my feet and instead use your arms. Still some pain but not much issue so far. Also, doing the stationary bike with the balls of your feet strapped to the pedals instead of further back on the foot. 

I did the bike yesterday and my calves burn today and only slight pain in only one arch.
[e9pppme] (score 1, diepte 2) Cool, thanks! 

The bad news is that your calves are a big part of your foot movement. If flexing your foot is excruciating, it may always be difficult to isolate your calves. 

The good news is that isolating your calves might not be 100% necessary to see progress in them. I'm no personal trainer to give advice on this, but what I would do if I couldn't zero in on a muscle and work it super hard all at once, is I would try working it just a bit as often as I could.

For example, many people note that hikers tend to have strong legs with proportionally large calves. You mentioned a long hike is doable but uncomfortable, maybe try some shorter ones on a more regular basis, or use a stair climber or a treadmill at high incline until your feet start to feel uncomfortable. These probably hit your quads more than anything, but are not playing around on calf work either.

As a side note, have you talked to your podiatrist about referring you for physical therapy? I know I had some exercises to fight serious over-pronation when I was young that seem to have made a big difference.
[e9my6vg] (score 1, diepte 1) Also have flat feet, so thanks kind stranger!
[e9my8qy] (score 1, diepte 1) Also have flat feet, so thanks kind stranger!
[e9mmwoc] (score 1, diepte 1) I never had to have custom insoles. The brand my doctor put me in were called SuperFeet, but there are other brands. Another thing you can do is look for shoes that have a wider and more supported arch. I've had luck with several different styles of Asics as long as they have the Duomax arch.
[e9mmzts] (score 1, diepte 1) Yeah and i used to walk on toes in house for 10 mins everyday when i was younger. It helped a lot and also i still climb stairs on my toes which caused me to have nice calves without working them out.
[e9muyqq] (score 1, diepte 1) Now I'm really curious.  I've always had flat feet, but they don't seem to affect me negatively at all and have no impact on my lifts.  I noticed someone else mentioning being barefoot frequently (and how it helped them) and I too spend most of my life without shoes on.

Does this somehow have an impact and if so... how does walking around (and lifting) barefoot versus with shoes have an impact?
[e9mwufz] (score 1, diepte 2) Great question
If you haven’t had the flat feet affect you negatively at all, then you don’t need to fix it. Like the saying goes, if it isn’t broken, don’t fix it. But you can always improve! Like running, you can run a certain distance and have no issues. But you can choose to maintain (don’t “fix”) or improve your distance
It doesn’t hurt to work on the muscles of your arches anyways. It can absolutely improve your lower body exercises. 
Orthotics are great for those who have chronic pain and needs that external aid. But try working on the musculoskeletal aspect first as that will be a bigger long term fix. 
Shoes give that arch support and feeling of comfort. Those who workout barefeet are strengthening their arch secondary to whatever they are primarily strengthening. The arches are put under more pressure and the muscles hold the arch rather than the shoes. 

Hope this helps! Fire off any more questions if you need anything else :)
[e9ogbfm] (score 1, diepte 1) I have a good form during squats but only when the arch is somewhat negative because of my flat feet. I can do this arch but I can't keep it while squatting. Any advice?
(24 reacties met lagere score weggelaten)

