# Label-batch batch_0151

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
Schrijf het resultaat naar `batch_0151.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: puqio7, 1gdms3i, 1ujbk9s).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD puqio7 ===
SUBREDDIT: r/xxfitness
DATUM: 2021-09-24  SCORE: 88  REACTIES: 61
TITEL: My feet have become picky and think socks limit their potential.
POST (source_id=post):
Okay, so here's a weird question I can't seem to find any answers to....

I am disabled and so am home pretty much all day every day and thus go barefoot probably 23 hours a day, 7 days a week. I workout 6 days a week, 45-60 minutes a day, rotating between running, body combat, barre, sh'bam, weight lifting and high intensity cardio. I wear minimalist sneakers when I run and am barefoot when I do anything else. If I wear sneakers when I do anything other than running my feet cramp, and if I wear socks with my minimalist sneaks when I run my feet cramp. However, as long as I raw dog in my shoes, I can go for an hour or more no problem, nice and comfy - they felt really natural from the first time I tried them. 


So what's the deal? Anyone else have feet that have a weird sock aversion? I can walk around and do lawn work or errands in sneakers and socks, or heels or boots or flats with or without socks and no problem, but any exercise not running HAS to be barefoot, and running has to be minimalist without socks. I never used to have such picky feet. My arches are strong, have nice healthy height to them, my ankles are strong, my balance is good...It isn't really a problem, it's just so weird.

Happy friday, xxers!


EDIT/UPDATE: If anyone comes across this and is interested, after talking to my doctor and narrowing things down...we realized the timeline of my injury coming on, came along only a few months after I stopped running as my main exercise and started doing dance fitness 5 days a week....barefoot. About 8 months later I started varying my workouts up, and by then I was already having issues with my feet, and knees...and eventually my achilles tendon. I bought the minimalist shoes cause I was so comfortable barefoot....my feet at least. But the rest of my legs were rebelling. So ultimately, it was going barefoot that was giving me the trouble. So I'm back to structured shoes, I even splurged and bought birkenstock slippers so even when I'm relaxing I have solid arch support, so here's to hoping things start getting right quick. Back to socked-feet and no more cramps! Thanks for everyone's input!!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[he4sscn] (score 117, diepte 0 OP) Omg I hate naked feet in shoes and then to read some one say "but if I raw dog in my shoes".. That's too much for me.
[he4lkc2] (score 54, diepte 0) I have this exact same issue. I just can't wear them for whatever reason, they feel weird, so I just never wear socks.  

They're cramped, hot, slippery and never go completely flat in the sole of the shoe so I always feel they need adjustment.  It doesn't seem to be a common thing, I am the only one I know of who does this. I've run marathons without them and without blisters being an issue, the skin gets used to it very quickly in my experience.  

One more for sockless
[he535jp] (score 35, diepte 1) LMAO! I'm sorry, I didn't mean to cause any trauma. I'll pay for your therapy bills...in muffins. Or cookies. Or pie. Your choice.
[he4mhze] (score 28, diepte 2) I had just posted about this in a running subreddit and got heavily downvoted so it is funny to see this post.  

There are literally dozens of us!
[he4muy1] (score 28, diepte 3) That's too funny, I actually wrote the post in the running sub, titled it and everything and then was like....no, you know who will have answers, xxfitness, those peeps will know what's up. I love /r/running, but they can be kinda snobby. So I came here instead. LOL! Glad I did so the horde of us could commiserate!
[he4oeny] (score 18, diepte 0) This post title gives me so much joy. I cannot handle working out in socks. Everything just feels WRONG if I'm wearing socks. My go to shoes are the New Balance Minimus.
[he4lsr8] (score 15, diepte 1) Isn't that odd....I used to be able to wear them fine, and I used to be able to wear normal running shoes, but now those do not agree with my feet and yeah, socks just make my feet feel like they can't get a grip in the shoe. My feet are tough mfers, lots of rough skin around the edges just from walking around barefoot. I never get blisters either. 

Sockless, unite!
[he5tx3c] (score 15, diepte 2) Vitamin b12 deficiency can cause peripheral neuropathy… might be causing your sensitivity issues with your feet. Usually starts from the tips of toes and works its way up. you should get that checked. Am podiatrist
[he4t69k] (score 15, diepte 2) I've had good luck with DarnTough and SmartWool.  They're spendy but they hold up well.  Cotton and and synthetics just feel sweaty to me basically immediately.

I'm also a fan of minimalist stuff, I really like the vibram five fingers even if they look kinda silly.  I've hiked for miles in these [https://us.vibram.com/spyridon-mr-W42.html](https://us.vibram.com/spyridon-mr-W42.html) (earlier model but same idea)
[he4kxnm] (score 14, diepte 0) Is it the elastic at the top of the socks causing your issues? 

I have soft top socks, because my legs swell and it does sometimes get painful. There are all sorts of brands out there, it might be worth looking for them.
[he4pv2p] (score 14, diepte 0) What material are your socks?  Have you tried merino wool?  I loathe cotton socks at this point and lghtweight merino is cooler than cotton anyway.  I wasn't real impressed with some of the synthetic performance stuff either.
[he4r48g] (score 13, diepte 1) Oh man, I don't know.... I used to wear those when they were cool when I was in high school way back in the 1900s (lol) and it always just felt so weird... I always ended up ripping them off my feet after an hour or two. But maybe for the sake of science I can try again.....
[he50k49] (score 11, diepte 2) If they feel slippy (even if your foot is barely sliding around), perhaps you are subconsciously gripping with your toes or standing with tension?
[he4xhrs] (score 10, diepte 0) As another barefooter, running/lifting/doing anything in sneakers feels WEIRD.
[he4lyqi] (score 9, diepte 1) I've tried the tall athletic socks, the really low cut ones, the ones that have the elastic around the arch of hte foot for support, I have tried older socks that are all stretched out so they don't restrict my foot at all, and they all result in the exact same kind of cramping. It's so bizarre. I used to never have an issue with this. It's something that has just popped up in the last 18 months to two years, I'd say.
[he4qy8a] (score 9, diepte 1) I have a b12 deficiency so I wonder if that is part of it. I just, like three days ago, goty blood work done and my glucose is great so that's not the issue. But I would think if those were the cause it wouldn't matter if I was wearing socks or shoes, my feet would cramp more consistently? Maybe not. But I'll look into maybe the b12 being the issue. Thanks!
[he4wcdj] (score 9, diepte 2) I, too wore toe socks back in the house  late 1900s...but those were novelty socks apparently made by evil wizards. The newer performance ones are MUCH better, in particular because they don't have seams IN BETWEEN your GD toes. Who would want that??
[he4oa4l] (score 8, diepte 0) Try socks with individual toes. It's all I wear anymore.
[he4tp1f] (score 8, diepte 2) I 100% exclusively wear merino socks. So comfy and soft and don’t get smelly. 
But I still sometimes get normal sock bunching and slipping so not sure if they will be better for you if you’re more comfortable in bare feet. Still worth trying if you want a new sock tho
[he4yprz] (score 7, diepte 2) I support your idea of trying again! I recently developed a bone spur on my foot right where most people would get a bunion, and one of the things that angers it is regular socks pushing my big toe towards the other toes, so I've purchased several pairs of Injinji toe socks. I wear them in my minimalist sneakers with wonderful results.

I can confirm that the newfangled seam design and materials make them a lot more comfortable than the last time I tried them. Also, I would suggest attempting to trick your feet by wearing them with shoes only - the extra fabric between my smaller toes still feels weird if I notice it, but as soon as I have a shoe on, I never notice.
[he5nqst] (score 6, diepte 2) I used to get AWFUL toe cramps when I was B12 deficient! Like, I'd be working out and then get this horrible pain and if I took my shoe and sock off, you could watch my toes curling in on themselves of their own accord.
Now I take 1000 IU B12 daily and no more foot cramps since my levels got better. Maybe it is related for you?
[he4vxoo] (score 6, diepte 0) I'm also barefoot like 90% of the time (and the other 10% is minimalist shoes) and if I wear socks with a "normal" toe my feet will cramp up. They squeeze my toes too much. I wear Injinji socks with individual toes or socks that have a more rounded toe.
[he4qc7t] (score 5, diepte 1) I have this problem!! Where do you get yours?
[he50nkf] (score 5, diepte 1) >slippery

what kind of socks are you wearing? lol
[he5l7xk] (score 5, diepte 1 OP) What about wool socks?
[he4rcik] (score 5, diepte 1) I am so glad it's not just me. I thought my feet had turned into the weirdest freak feet. I just got these minimalist shoes, just some ones I got off Amazon, knock off brand for $30 but they are sooooo comfy and immediately my feet were like YESSSS THIS IS WHAT WE'VE BEEN CRYING FOR!!! lol
[he7dxdp] (score 4, diepte 2) Any other changes? Go for a sitting job to a more movement one, change your workout in that time, have you had the same shoes for the full time for running and lifting? Change the time when you lift (possibly slightly more swollen feet)? Diet changes? Weight gain or lose?

Socks seem like they could be a sign of something else going on, or maybe depending on how long you've been into fitness you're just starting to pay more attention to these smaller things. (I realize I can't lift in socks, but I got new shoes that are just too smooth for my athletics socks.)
[he4qov4] (score 4, diepte 1) I haven't tried Merino wool, I've only ever used cotton and moisture wicking materials, whatever they may be... but it can't hurt to give it a shot!
[he50o9r] (score 4, diepte 0) That’s interesting! I generally always wear socks but have noticed when I wear ill-fitting socks that slip around (especially dinky decorative thin socks or slightly too low ankle socks) that my feet feel a bit fatigued/sore. I think I’m doing a little extra gripping with my feet to keep the socks in place? I just avoid those types of socks though and stick to the ones that fit my feet well.
[he4xi0a] (score 3, diepte 2) I bought these, but it's a UK company so I'm not sure it will be any good to you. 

https://www.hj.co.uk/ladies-socks
[he52lxh] (score 3, diepte 3) That could be....they do feel slippy. But without the socks, my shoes fit like a glove, like they are molded to my feet. I'll have to make note next time I try it and see if I'm not doing that without noticing.
[he830lz] (score 3, diepte 3) ... this is interesting. I'm not vegan and I take a multivitamin so I had never thought about B12 being an issue, but I've had foot cramps and some other weird muscle cramps the last year or two that didn't really change with magnesium or general electrolytes. I also got a workup that included diabetes, celiac, iron levels due to a bone injury and no signs of an issue with any of those, just slightly low vitamin D, but I don't think I've ever had a test regarding B12. If I consume a normal amount and don't have malabsorption problems though, is there any reason I could be low in B12?
[he85ikc] (score 3, diepte 4) So I got diagnosed with low Vitamin D and B12 at the same time, and I take a supplement for both. I'm not a doctor so I can't tell you which one was responsible, but since getting my levels normal I haven't had the toe cramps since. But I think I remember my doc hypothesizing B12 as responsible for the cramps. FWIW, basically everyone in modern society has low D and would benefit from a daily vitamin, and it's a "safe" vitamin to take because it's very difficult (maybe impossible?) to reach a level that would be too high and dangerous.
[he52zx5] (score 3, diepte 3) I'll give 'em a shot, worst case is I just have an extra pair of socks to go with all the rest of my regular shoes!
[he7dl1j] (score 3, diepte 1) That's what I was thinking, I also switched to merino. Had no idea all my foot pain was from cheap cotton socks. Now, I'm miserable if I have to wear cotton socks for one day.
[he4u9nh] (score 3, diepte 0) Have you tried running-specific socks? They hug the foot closer and tend not to have seams and they don't bunch up with motion. I wonder if those features would change your situation enough to prevent cramping. 

It's also possible that lacing your shoes a bit differently (looser in the toe box, perhaps?) could alter the fit in a way that stops the cramping.
[he4yd21] (score 3, diepte 0) Have you considered Feetures with arch compression, toe socks, or bamboo socks? Do you know your socks fit right? Are you diabetic or have any circulatory, vascular or cardio issues? Seamless socks? Non binding socks? Are you sure your shoes fit properly? Most people's don't. You'd be amazed at how many things can influence stuff like this. Might even be something that's happening when you're barefoot so you're not linking cause and effect. Very hard to tell without doing a physical exam and interview.
[he52d7u] (score 3, diepte 0) Oh man, I think I'm the opposite - wearing trainers without socks is awful for me, and I hate being barefoot! I do have some really nice sports socks though - they have 'support' around the arch (just tighter elastic I think) and they're quite thick and comfy.
[he5fqh5] (score 3, diepte 0) If you're barefoot all the time, you may be interested in socks that folks who wear minimalist/barefoot shoes recommend. For example: [A Barefoot Guide to Socks That Don't Squish Your Toes](https://anyasreviews.com/barefoot-toe-socks-review/).
[hehel7o] (score 2, diepte 3) No, my life is pretty static. Only change has been a med change, but that happened after this sudden weird foot pickiness, so I'd stray away from that explanation. I"m seeing my doctor on Wed, so I should get some answers....maybe....at least, if there is a medical reason.
[he52xgq] (score 2, diepte 3) Seriously, what was the idea behind the seams? Evil wizards were totally behind those socks.....they were awful cute though!
[he52ssc] (score 2, diepte 3) I'll look into them, what's the worst case scenario, I have an extra pair of socks or two? Thanks for the idea!
[he52h52] (score 2, diepte 1) That very well could be part of the problem, because no matter how well fitted my shoes are, my feet don't feel as secure in place in my shoes when I have socks on. But without the shoes are like gloves.
[he614gx] (score 2, diepte 1) This is a great site. As someone who also loves a minimalist/barefoot lifestyle, thanks for sharing it.
[he5k3vk] (score 2, diepte 0) Ooooo, this is me too! I run half marathons sockless in minimalist shoes! For workouts, I wear zero drop cross trainers sockless. I do wear socks with my lifters but it's only because they're expensive and I'm trying to make them last for as long as possible lolol. I grew up doing martial arts and I'm Asian so being barefoot and sockless feels natural and comfortable for me. I also have sensory issues and weird little things bother me. For example, if I paint my nails, I feel like my nails can't breathe and wipe it off almost immediately. I can't do sleeves, I can't wear foundation because I feel like my skin can't breathe, etc. I feel like hating socks is part of that.
[he7dlnp] (score 2, diepte 0) Wide toe boxes help! Double check that your minimalist shoes are giving room for your toes to help you balance during squats etc.. Your socks might be squishing your toes a bit too so maybe a larger size of sock, but I find the combo of minimalist shoe + sock too slippery. So I've been lifting bare feet for now in my shoes, or if no one is at the gym I'll lift in sock feet alone (the floor is rubbery and I wipe it down after).

What kind of minimalist shoe do you have? If it works for running it might not work for weight lifting if there's too much heel or arch support or the wear points are different, though this is less likely with a true minimalist shoe.
[hehj98v] (score 2, diepte 1) +1 to it maybe being a toebox size issue.  I wouldn't be surprised if barefoot daily living has made your forefoot spread itself out a bit.  There are both shoes marketed as having wide toe boxes and just plain wide shoes.  But that's only if you want to wear socks!  Going barefoot seems to work for you and I'd say just keep doing it.  

Also many triathletes tend to run/ride barefoot so that they can get through transitions faster, so shoes geared toward that market may be more barefoot-friendly if you need to look for new ones.
[heheutw] (score 1, diepte 5) I have had a B12 deficiency on and off throughout my life, but I was always just considered low on B vitamin, which isn't as concerning as being deficient. So I take a multivitamin to address the generally low vitamin D and a specific B12 supplement for that to get some extra. Though I only started doing that recently, so hopefully that will make a difference.
[hed54ma] (score 1, diepte 3) Why do the Injiji socks have to be hand-washed?
[heehvwb] (score 1, diepte 4) They don't; I machine-wash and put mine in the dryer.
[he532h1] (score 1, diepte 3) Awesome, thanks for the recommendations, I appreciate it bunches!
[he53bfh] (score 1, diepte 1) Someone else mentioned Injinji socks, too, I"m going to look into them. Thanks for the suggestion!
[he5ufu1] (score 1, diepte 2) I've also found that mens socks have wider toes, if you don't care for toe socks
[he4wcf8] (score 1, diepte 0) I don’t like socks, I started hating them as a young adult, and I used to have normal feet. I think they affect the way my shoes fit but they caused weird nerve pinching or cramping. That being said, it used to just be a feeling while wearing the socks with certain shoes. Nowadays, though, I have a number of foot issues and have been told that going barefoot a lot and using unsupportive shoes probably caused them (I used to run in barefoot sneakers and have never tolerated wearing shoes around the house). First it was discomfort with certain shoes and socks, then overuse injuries and now I have toe capsulitis. All this to say, I wish I had listened better when my feet FIRST started speaking to me because although it was little things like this at first now it is way worse. I would consider mentioning it to a doctor and seeing if you can investigate it further.
[he5ai24] (score 1, diepte 0) This isn't uncommon when you get used to barefoot/minimalist shoes, traditional socks can pull your feet in quite a bit! Have you tried 5 toe socks or sizing up a size (or getting men's) in regular socks?
[he5fvzv] (score 1, diepte 0) I can’t function without my soft foot bags. And I’m very particular about them, so I get it.
[he5hr1w] (score 1, diepte 0) I have switched almost exclusively to Injinji socks - socks with toes. They feel so much better on my wide feet.
[he5jrwd] (score 1, diepte 0) Hmm. My feet cramp a lot but I’ve never tried running without socks. I’ll have to try it on my next run
[he5l5sv] (score 1, diepte 0) Very interesting thread, thanks for posting! I wear size 10 shoes and women’s socks are almost always some bullshit that don’t fit me. Even if it says it fits up to size 10, it doesn’t. I also have randomly gotten really bad cramping in my arch and toes when lifting and running or just stretching before. 

So maybe socks are the culprit! Who knew!
(2 reacties met lagere score weggelaten)

=== THREAD 1gdms3i ===
SUBREDDIT: r/weddingplanning
DATUM: 2024-10-27  SCORE: 196  REACTIES: 61
TITEL: The Photographer got cold feet
POST (source_id=post):
Hello Ladies! Congrats to all the beautiful brides who got married this weekend—myself included!  I had an incredible day, and honestly, at first, it didn’t even phase me that the photographer I booked just no-showed. I hired her from 11 AM to 7 PM, but by 11:30, I hadn’t heard a word. I tried calling and texting with no response. Then, when I checked her Instagram, she had posted at the exact time I was messaging her! She’d been out with local friends the night before, and even bragged about being super close to our venue. But somehow, on the day of, she’s suddenly “out of state.” (My brother even went by her place and saw her car parked there.) When I finally spoke with her, she stumbled over her words, like she couldn’t even think of a lie fast enough. While it hurt, I found some comfort knowing I’m not the only one this has happened to. And to the lovely lady who said, “Don’t sweat the small stuff, no one will notice”—thank you, because you were right! No one even knew our photographer stood us up.Still, this situation is a big deal, and I’m struggling to move past it. She has apologized and says I’ll get a refund within 7-14 days, but that’s not acceptable to me, especially since we’d booked a private garden specifically for the photoshoot. Has anyone dealt with something like this? Any advice on getting the refund faster or getting compensation for the inconvenience? Thanks in advance!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lu30h4f] (score 461, diepte 0) I would wait until I had the refund in hand, then do an honest review everywhere I could think of.
[lu30we1] (score 212, diepte 1 OP) Yea, thats where I am at with it. The irony of it all, shes taking all of her business pages down, your unable to book her. ++ On her social media page she has shes out of town, which she did right after our situation... is it just semantics, or sure, but the is why I am STRONGLY considering small claims court to her LLC. which she cant hide.
[lu35fmt] (score 210, diepte 2) Do it. And add the cost to rent the venue for a photoshoot, the cost to redo your hair and makeup, etc. i can see a judge wanting to award so,e damages and make you whole after she straight up just blew off your wedding. There are damages that come with breaching a contract. And just returning your money doesn’t really seem like enough.
[lu320rr] (score 109, diepte 0) I just can't fathom doing that to a client, especially so flippantly. As far as what can be done about it? That might depend on consumer laws in your area but IDK if there's all that much you can do to speed up the refunding and it's doubtful you'd get anything beyond what was paid without some real effort - it sucks but once you have the cash back the best you can do is just burn her to the ground with reviews.
[lu32z5f] (score 105, diepte 2) She’ll probably reactivate it after some time when she thinks you won’t post a review about her lack of professionalism.
[lu39eaz] (score 95, diepte 4) Get screenshots of those "out with friends the night before" social media posts before she deletes them.
[lu3dc8j] (score 81, diepte 5 OP) my sister was on it, like she was on first 48 and of course she took them down immediately lol
[lu45piu] (score 60, diepte 2) I mean people do get sick or have an emergency. I'd think having a contingency plan would be a sign of professionalism rather than signaling that they're careless.
[lu365ig] (score 57, diepte 0) I’d take her to Small Claims Court.
[lu35pek] (score 51, diepte 3 OP) AGREED!!!
[lu3hxl7] (score 51, diepte 0) My contract says that in the case of our photographer being ill or unable to come, a replacement photog will absolutely be present. I assume that’s pretty standard but yall please check for that wording going forward.
[lu3lblm] (score 50, diepte 2) A no call no show for something like a wedding is and should be a career ender imo. I don’t think I would have the patience and grace you described in your post in the same situation.
[lu44as3] (score 36, diepte 2) You have every right to do this but I'm going to suggest TRYING to get the refund first while she thinks you're 'cool with it.'.  Small claims will be slower and while you'll definitely WIN in court, that doesn't mean you'll COLLECT a dime.

Maximum chance of actually getting the money: 

First wait the two weeks but follow up after one week and again after two.   Act chill.  Just remind her your haven't received it.   A certain type of person WILL get the refund done, but if it starts looking like lawyer time, they may clam up.   As a small business owner, if you threaten to sue me, right or wrong, as soon as you say the words I won't have any more contact with you, I'll wait for the papers and do what my lawyer suggests, because that's his advice.  So try the 'nice route' first. 

Next send a scary letter of demand.  If you have a lawyer friend, let them write it on letterhead. This is where you make it clear what you expect and what will happen if they don't do it. 

Only third do you actually sue.


I want to be clear that I'm not suggesting the softer approach at first because THEY deserve it.   I'm trying to maximize your chances of getting your money as fast as possible because YOU deserve it.   You owe them NOTHING but bad reviews.   But I'd hate for you to skip to option 3 when option 1 or 2 might be more likely to pay off with some people. 

Just because you win in small claims doesn't mean they'll pay the judgement.  Especially if they're shutting down and don't care about reputation.
[lu35hu4] (score 30, diepte 3 OP) good point!
[lu3327k] (score 30, diepte 1 OP) AGREED!!! I am a photographer myself, who loves building business for consumers, and I could never Imagine being the person to attempt to taint someones beloved personal experience.
[lu31x7p] (score 27, diepte 1 OP) good point, CONGRATS TO EVERYONE WHO GOT MARRIED!! LOVE IS LOVE AND WHAT AN AMAZING THING FOR US ALL TO CELEBRATE IT AT THE SAME TIME.

I dont even want to see her face, if she was the only photographer left in the world, I wouldnt book her. Its that much resentment, she offered a replacement, but this was 30 mins before I had to walk down the aisle +++ I didnt book or sign a contract on if this would happen.. (we also had our gma friend come right on time, when we figure we were getting played so we didnt need a replacement)

She deleted the ig photos showing she was in town, when my mother & brother called her out for not actually being out of town. It felt real personal and I dont know the lady, I actually supported her by buying additional hours because she had a sale due to a family member passing.. just for her to "forget" and say she has me booked for next year, but on the square contract it says this year! and I sent her a vendor itinerary a week before grrrrr! I truly cant believe it lol like truly cant believe it, feel like I am in an office episode starring into camera b every 5 mins
[lu4jqp9] (score 27, diepte 1) Thank you for this. As a nonbinary fiancé I appreciate it
[lu45zhl] (score 22, diepte 2) Wedding professionals here, I never ever had a no show always been punctual but I have this clause in my contract because why would I leave the door open to get sued? We’re all human if there is an kind of emergency we need to be premeditated for that. 
Also any vendors that do not have this clause in their contract can then put you in situations like yours. 
Anyone getting their contract drafted by an attorney (which I did) should have this protection clause in it. 

As for your issue, your contract will tell you what you are entitled to. As far as the Garden, unfortunately that will most likely be a loss. 

I’m sorry this happened to you. Hope you do get your refund!
[lu36g26] (score 20, diepte 1 OP) Will DO.
[lu3r8rg] (score 14, diepte 2) YES SMALL CLAIMS COURT
[lu42an6] (score 13, diepte 2) The LLC may make it harder to get any of her personal assets but not impossible (the LLC may own nothing or very little).  

You can’t just form an LLC and poof protect yourself from liability.  You have to actually segregate personal assets from business ones and SO many people skip that step or botch it or get lazy.  It can be very easy to get past an LLC if they botched it and I’m guessing based on her lack of professionalism that she probably didn’t do it right.  So many people don’t even bother to set up a separate bank account.

I’m not a lawyer, just a CPA who has to hound clients to do it right.
[lu3311k] (score 13, diepte 2) Of course! It’s easy to overlook because many post in the subs are from a brides perspective! Totally agree!

Given that context, I would absolutely contact a lawyer and take her to small claims court. Completely unacceptable and I’m so sorry that happened
[lu37zfw] (score 12, diepte 2) However it can be hard to quantify damages, especially if she refunds you for the whole contract already, for e.g. that your private garden rental went to waste.

Good luck!
[lu3ilw4] (score 12, diepte 0) Keep all your communications and take her to court.....for your refund , the cost of the garden and mental distress.
[lu3p6rq] (score 11, diepte 0) This is such insane behavior. She didn’t even have to take the job. Like do people not know what empathy is?
[lu30v38] (score 10, diepte 0) 1) Friendly reminder that this group isn’t just brides, but also grooms and non binary folks who are all getting married and coming here for support and advice 

2) That really fucking sucks and I’m sorry. Personally, I wouldn’t accept the refund at this point, I would have her pay to reschedule the garden for a photoshoot and perform the service, and then refund me. It would be one thing to oversleep or be late, even sending a replacement. But to ditch for 8 hours unless there was a serious emergency is completely unacceptable
[lu3jqiw] (score 10, diepte 0) They should give you your refund and double
It since now you have no professional pictures. I’d reach out to her manager immediately. She needs to be fired. Sounds like if she was out with friends and family close that she got too drunk and most likely had a hangover. I’m so sorry this happened to you. So happy you are able to handle it well, because I don’t think I could have.
[lu5a7sl] (score 9, diepte 2) We made sure that all our suppliers had this clause in their contract as it showed us they had a plan should anything bad happen. 
We were just after COVID and it was one of the questions we asked of them all when interviewing as well.
[lu5uogs] (score 9, diepte 1 OP) EXACTLY!!! Her reason was it slipped her mind and she totally forgot, a family member passed and shes not okay… that would be reasonable if that was stated prior to the event, but the day of is a bit nasty work to use a person death as an excuse, because weve ALL lost someone we love that doesnt make us do bad business- i actually supported her to help w funeral cost ; soo i am left thinking was there ill intent this whole time :/
[lu3uq1i] (score 9, diepte 0) This is another reason why event insurance is so important! My wedding cancellation insurance policy explicitly covered a photographer no-show.
[lu42kuu] (score 8, diepte 2) Do NOT accept any payment from her. You may be binding yourself to accepting that as a settlement. 

Do you have any written contact with her? Something that's on paper or any correspondence? What does that say about no-show penalties or cancelations after a certain date?
[lu383wh] (score 8, diepte 0) I don't have any advice for ya that hasn't already been given, but I am so sorry. That is beyond shitty. I just can't fathom operating in this way...
[lu3jcnt] (score 8, diepte 1) It’s literally in the first rule of the sub…
[lu409fg] (score 8, diepte 1 OP) i was today years old when i discovered wedding insurance, i knew about event insurance, like for concert and tickets. but that is def something I wouldnt have mind getting!
[lu35fjr] (score 7, diepte 4) You’ll want a lawyer to review your contract / and any addition details
[lu64nz1] (score 7, diepte 3) It absolutely should be. Grooms and other planners are here and enthusiastically welcomed. We want everyone to feel they have a place here, because weddings are for and planned by everyone. It takes no time to shift language to 'hello Wedditors' and includes everyone. 

If that isn't for you, you're welcome to find another subreddit that is more your style. But that's our firm rule here.
[lu6mj8b] (score 7, diepte 3) Yeah, agree.

> And to the lovely lady who said, “Don’t sweat the small stuff, no one will notice”—thank you, because you were right! No one even knew our photographer stood us up.

This is very sweet of OP, but OP.. please know this is a MASSIVE deal. This isn't sweating the small stuff. You don't have professional photos of your wedding.
[lu3569j] (score 6, diepte 3 OP) I believe she can still be liable for the couple photoshoot that we booked, we wouldnt have booked that if it wouldve came to this. (hindsight) of course
[lu5u3z0] (score 5, diepte 3 OP) I agree!! You get more bees with honey- i def tried the nicer approach. My mother and friends def told her this is a breach of contract and shes liable to get sued. After i was able to reflect i reached out to her : she stated in a text to let her know what she could do to make it right. + gave her sone time… why am i being fair and reasonable during a time like this idk, going to court would be based off of principles w a sprinkle of petty , a judge will see it and look at the vendor crazy for not setting before court
[lu35ma7] (score 5, diepte 5 OP) Ill be on it, top of Monday!
[lu35s5k] (score 5, diepte 6) And finally I would avoid posting any reviews / additional complains on social media because it can be seen as damaging to her and that could look bad to a judge
[lu44vli] (score 5, diepte 0) If she has insurance sue her for all damages.  If she is insured you may be able to have them cough up enough to have another photographer shoot new photos with your entire wedding party and pay for ALL of it.

You absolutely go legal with this.  Save screen shots of her posts partying the night before and all that. 

If you hired an uninsured photographer I’m sorry - you should definitely speak to a litigator and have them see if it’s worth pursuing a. Insurance obviously is far far easier to claim against.
[lu6lhln] (score 4, diepte 1) I have a friend whose daughter has a combo of bipolar+ADHD, and she does really extreme no-shows to things like this. That was my first thought reading this post. 

She will do things like last minute not go on vacation with her parents which has been planned for weeks. Or talk up a party/event for weeks and then no-show the day of.

I'm curious how long this photographer has been in the business and what the heck was going on. Bailing on a wedding is MASSIVE.

/u/RomansEight28 - Did she give any sort of reasoning when she apologized?
[lu3gt7r] (score 4, diepte 1) Also so sorry about your photographer! Take her to court
[lu6j0ma] (score 4, diepte 0 OP) update: I emailed + txt her with an offer and she’s actively ignoring me while being on her socials. I found info on her website for when customers are late, NCNS, or inconvenience- could i apply her own principles to this matter and ask for those fees? Be she was late, ncns and a HUGE inconvenience
[lu36dtc] (score 3, diepte 7 OP) agreed, i can def see her trying to play that card, so I kept the info as vague - cause I am not the only one (which doesnt make it better) but easier for me to know what I need to do.
[lu5ubkg] (score 3, diepte 3 OP) Have contract - a huge paper trail of conversations, and it doesnt say anything about ncns- but on her site if a person ncns they are forbidden from booking with her ever again, ironic isnt it…
[lu8xxu8] (score 2, diepte 4) Thank you for this. Not to mention, some of us getting married don't identify as men OR women!
[luemvxn] (score 2, diepte 2) This is standard for contracts and protects the client, if the photographer for example had a car accident, unforeseen emergency etc, they would need to do everything they could to get another photographer for the client. 

I am appalled this happened to you, and definitely get legal advice. Not only a refund but the cost of redoing wedding /family photos. It’s a priceless heirloom that was just stolen basically.
[luionon] (score 2, diepte 1 OP) Good strat!
[luioosm] (score 2, diepte 2 OP) def BBB when its all said and done
[luixvdr] (score 2, diepte 3) For sure! Just be straight on your own stuff and they'll make THEMSELVES look bad for you haha
[lu6ixgw] (score 1, diepte 2) What’s a “gma friend?” Did you at least have a someone who was able to step in and substitute as photographer? 

I don’t know how this situation typically plays out in court but in a fair world damages would be many times the actual cost of services. It’s something you can never replace or do over again in real time.
[lu6is3m] (score 1, diepte 2 OP) update: I texted her with an offer and she’s actively ignoring me while being on her socials. I found info on her website for when customers are late, NCNS, or inconvenience- could i apply by her own principles and ask for those fees? Be she was late, ncns and a HUGE inconvenience
[luinre8] (score 1, diepte 2 OP) She was on a self trip on the west coast... a family member died so she wanted to. give herself a break  to find herself. a load of BULLSHIT, if you ask me. then shes trying to say we rejected her replacement, a replacement she sent during the start of the ceremony.......
[lu348l2] (score 1, diepte 0) Friendly reminder that grooms and other planners frequent the subreddit. It is best to use inclusive language like Wedditors here when anyone can answer your question and/or give advice. Thank you!
[luio2h6] (score 1, diepte 1 OP) thank you! i appreciate it
[luio13c] (score 1, diepte 1 OP) shes her own manager, and when i look back at it all, she doesn't/ didnt have her shit in order. and thats on me for giving her a chance.. smh
[lu3tj9n] (score 1, diepte 0) I would be telling everyone who'll listen, not to book her or recommend AFTER you get your money back . If there's anywhere for reviews just lay it out..her lack of consideration and lack of professionalism is astounding!
[lu40ch9] (score 1, diepte 1 OP) AGREED! I hate it had to come to this
[lu42yde] (score 1, diepte 0) Ive heard your wedding insurance can possibly help things like this. But yes, money in hand and then post a review. If you have trouble getting your money, Better business bureau, police, small claims court. Good luck!
[luiohfs] (score 1, diepte 1 OP) She then responds via email - that she's not actively ignoring me, but she answered when my husband called her. She's trying to get under my skin. and I am to a point I want to get under her skin where she doesn't ever want to pick up a camera again.
[lu76p9d] (score 1, diepte 0) Holy hell what a fucking mess, I'm so sorry
[luiopwq] (score 1, diepte 1 OP) agreed. agreed.
(9 reacties met lagere score weggelaten)

=== THREAD 1ujbk9s ===
SUBREDDIT: r/BuyItForLife
DATUM: 2026-06-30  SCORE: 24  REACTIES: 60
TITEL: sandal suggestions anyone?
POST (source_id=post):
im looking to invest in some nice sandals. id love for these to last. additionally I love the look and sustainability of leather, but I'm not set on it as long as the substitute looks nice. I plan on wearing these in all kinds of weather. i don't like near the coast but id want to be able to use them when I visit. i might be asking for too much but I'd definitely prefer them to have good arch support. suggestions?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[oumjaz7] (score 18, diepte 0) Birkenstocks are great with the caveat that they are not designed to get wet. Honestly, I'd get a pair Birkenstocks and then a pair of Crocs, Tevas, or even the cheap EVA Birkenstocks for wearing to water. If you care for your Birkenstocks (get the right size and don't wear them too tight, reseal the cork occasionally, and resole before you walk through the outsole), they could last you decades.
[oumk6zh] (score 18, diepte 0) I like my Birkenstocks but they are nowhere near BIFL.
[oumhjob] (score 16, diepte 0) Rainbow but the made in the US variant.
[oumvtev] (score 16, diepte 1) I refer to my EVAs as Birkencrocs.
[oumgx8h] (score 15, diepte 0) got a pair of birks few years back and they still going strong, the cork footbed molds to your foot after a while so arch support gets better with time
[oumkzu6] (score 10, diepte 0) Bedrock Caines. I love them and when they wear out I’ll get the resoled. Had mine for more than 7 years.
[oumpe0z] (score 9, diepte 0) Chacos. Ive had mine since 2009. Beach. Travel. Soaked. Good as new.
[ouneyjh] (score 6, diepte 1) Same. Love them but they are buy them every three years or so.
[oun6g6a] (score 6, diepte 0) Olukai hands down,  everything else is trash
[oumq35z] (score 5, diepte 0) Chacos - I've had one expensive pair and one of the cheaper pairs.  They hold up.
[oun10oa] (score 4, diepte 1) Birkenstocks! The leather ones! 

And I agree, also a pair of Tevas for the river.
[oumngxq] (score 4, diepte 0) I have some chocos that are going on 10 years of consistent use with no signs of wear.  Would recommend!
[oun3xwl] (score 4, diepte 0) Chacos, Keen (at least the older ones), or my personal favorite, Olukai's. I have a pair of Olukai's that are going on 7 years now with consistent use
[ounouol] (score 3, diepte 0) Rainbows from San Clemente, CA. They are leather with foam layers, & can be double layered. They form to your feet. They are actually comfortable unlike Birkenstocks.   
My feet and back ache in pain if I’m not in super thick comfy shoes & I can wear Rainbows all day. I couldn’t last 10 minutes in Birkenstocks. 

I used to play basketball (casually) in rainbows because they were so comfy & formed to my feet so well.

I’ve had pairs for 10+ years and only would get a new pair just because I wanted a different color or style.

If you are ever in Southern California, it it 100% worth it to drive to the factory in San Clemente to get a pair or a few.  
They sell loafers, moccasins, & many different kind of shoes as well with the same incredible comfort & durability
[oumhwv1] (score 2, diepte 0) I like my Hari Mari’s a lot
[ouolt0h] (score 2, diepte 2) "They replace the sole and footbed and they come back like new"


What is the cost of this service?
[ouncwbd] (score 2, diepte 1) Seconded! If it weren’t for my dog (twice, sent them to get straps repaired and he chewed the sole the second time) I’d be on year 5 of the originals.
[oun16il] (score 2, diepte 1) Loved these, but the sole separated on mine in two years.
[oupfgom] (score 2, diepte 1) Ecco’s are great but,  I soaked my new expensive ones  overnight in water and to my surprise the sole deliminated !  I asked Ecco’s and the store I bought them from and they told me the shoes are not meant to get wet or even walk thru puddles!  Wth?  I live in south Florida I bought these for those occasions I might get caught in a storm or go go kayaking etc.  previously I was a Ecco fan, but I’ll never buy Ecco  again
[oumt7yx] (score 2, diepte 0) Lems Switchback. I went to buy some Bedrocks and the guy who owned the store said they were the new "doing stuff you shouldn't be doing in sandals sandals" and he was 100% correct. Real rad for biking and hopping around rivers.
[ouna241] (score 2, diepte 0) I've been wearing these for a few years. Comfortable and durable.

https://www.keenfootwear.com/products/mens-newport-h2-monochrome-dark-earth
[ounbnf7] (score 1, diepte 1) Omg I loooove my birks but the arch support in them (my arch  support) is so high lol. Sometimes I wish I could get them to flatten out to be more like all of my barefoot sneakers/flats.
[ounqztb] (score 1, diepte 1) After blowing out another pair of thongs(flip flops) I recently went on a quest that lead me to either southern polished or rainbows, but rainbows were easier to get in my country. They’re amazing, and will hopefully last me a decade or more.
[oupexk6] (score 1, diepte 2) Tevas are great but,  I soaked my new expensive ones  overnight in water and to my surprise the sole deliminated !  I asked teva and the store I bought them from and they told me the shoes are not meant to get wet or even walk thru puddles!  Wth?  I live in south Florida I bought tevas for those occasions I might get caught in a storm or go go kayaking etc.  previously I was a Teva fan, but I’ll never buy tevas again
[our1vvy] (score 1, diepte 2) Chaco or Tread Lab sandles will last way longer than Teva and are amazing for river sandles. Also they would have better warranty.

Custom Chaco sandels which cost more bit more are also still made in MI and will last a really long time if you resole them.
[ow71dwd] (score 1, diepte 3) I bought chacos after all the hype to replace my last pair of Tevas and they’re so uncomfortable and notably heavier than the Tevas.
[oupfefv] (score 1, diepte 3) I'm in Edmonton, Canada. It's much cheaper to get them resoled here. $100 vs $160
[oupjf6t] (score 1, diepte 4) 100 Canadian bucks is still £57! Oof.
[ous601m] (score 1, diepte 3) Oh wow, in the US I could get a resole for 50-60 USD. New the sandals were easily $150-60. I haven’t tried in Italy but I’m seeing cobblers asking €50-€70 near me. But it’s only €90 for the cheapest sandals. So yeah…much harder to instantly opt for a resole rather than a whole new sandal for only €20 more.
[oumjz1q] (score 1, diepte 0) Piper Sandals out of San Antonio.
[ouprxfp] (score 1, diepte 1) \+1 Had my Bedrock Cairns for about a year now, work in the water and on short hikes, they are awesome so far.
[oumsaaa] (score 1, diepte 0) I like my reef flip flops and crocs.
[ouoosmx] (score 1, diepte 2) Micro plastics. Watch a video on how they are made. It’s absolutely horrible. And they seep into your feet through sweat….
[oumsfku] (score 1, diepte 0) Ecco Yucatan.
[oun3pj5] (score 1, diepte 0) Birks and get them resoled/repaired as needed.
[ouozlfs] (score 1, diepte 1) Buying older Keens seems difficult, and I have heard lots of reports that the Keens sold now wear out really fast in the sole.
[oupb1ah] (score 1, diepte 2) Yeah it really seems like their newer rubber doesn't hold up as well. I have a pair from the late 2000's that I use for water activities and they're still solid.
[oune42v] (score 1, diepte 1) 100% I have the model with the criss cross straps and they are the best, sooo much better than Birkenstocks
[ounnc86] (score 1, diepte 1) Plus 10 toes
[ouoove4] (score 1, diepte 1) Quality has gone Way Down
[oundlay] (score 1, diepte 0) Keen’s! Comfortable, supportive, cushiony, sturdy, good tread, airy, light weight.
[ounfw0k] (score 1, diepte 0) Depends on your activities in the sandals and exact style you're going for, but I've had my Keens Elle Backstrap sandals for (I think) 6+ years now, and I wear them daily for about half of the year. They're holding up amazingly well. They've fully been in rivers and the ocean a number of times as well. I've heard varying reports for Keens though, so YMMV.

Birks are great if you're willing to pay for repairs/resoles, especially if you have a verified repair store in town.
[ouoit99] (score 1, diepte 1) Taos are wonderful! They are a good travel sandal for me - I can walk for miles.
[ounjt5o] (score 1, diepte 0) Saltwater sandals?
[ouseu4a] (score 1, diepte 1) They do last forever! I think mine are around 6-7 years old? Look exactly the same.
[ousj4kp] (score 1, diepte 2) Yeah I have a pair that's at least 13 years old and they look new
[ouno7h7] (score 1, diepte 0) Luna Oso Flaco
[ouo7eud] (score 1, diepte 0) If you want some of the best flip-flops ever made….look at Scott. OG Hawaiian / Californian and indestructible.
[ouoo8qo] (score 1, diepte 0) Kinos
[ouozgav] (score 1, diepte 0) If you go the birkenstock route, there is one line they have that lasts much longer in the soles.  They have a thin read  strip around the sole.

Last time I looked they were really hard to find.
[oup0coa] (score 1, diepte 0) I’m not sure any I know are BIFL but my husband and I love our Reefs. We’ve had them for 5 years and they look almost new!
[ouq7t0x] (score 1, diepte 0) I like my Reef leather flip flops.
[ouquekd] (score 1, diepte 0) I personally find my burks great for short spurts but not comfortable for walking too long (though friends love theirs so ymmv). I’ve had chaos but they made my feet smell so bad. Again friends love theirs and get the same result but feel it’s worth it. I love love love my Naot Kayla sandals. Probably shouldn’t get wet but I wouldn’t be too worried about it. Not sure how long they’ll last but I’ve had mine for years, walked many miles, traveled with them, and still going strong. 

For beach and water, I use Tevas. The Hurricanes are great for walking too, but they aren’t “cute.” So I don’t have one pair for everything but with those 2 I’m covered.
[ousc0bw] (score 1, diepte 0) Any love for Mephisto?
[ousm04x] (score 1, diepte 0) I can not recommend Bed Rocks enough.
[ouyvtk2] (score 1, diepte 0) Chacos.
[our19r1] (score 0, diepte 2) Wear them more and it should flatten them out to your arch.

I had a friend with flat feet (could actually suction cup them to the floor flat)and and it's what he wore all the time.
[oumww0z] (score 0, diepte 1) Came here to make this recommendation
[oun9hvv] (score 0, diepte 1) I have 2 pairs of Birks. Easy slip -ons ( 2 strap (for around the house and quick trips out) and my adventure Birks which have the added ankle strap - it makes a huge difference for hiking and rougher terrain. 

Plus, I've had them both resoled many times. They replace the sole and footbed and they come back like new
[ounadm4] (score 0, diepte 0) Olu kai and teva. Bedrock, mephistos
[ounhdn1] (score 0, diepte 0) Love my Birks. I do have a dressier pair of sandals - Taos brand. They’ve lasted brilliantly.
[oumvdfq] (score -1, diepte 1) Croc Nation Stand Up!!!

