# Label-batch batch_0153

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
Schrijf het resultaat naar `batch_0153.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 13nvk54, 1fmapry, 1x415sl, 4ss73u).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 13nvk54 ===
SUBREDDIT: r/AmazonFC
DATUM: 2023-05-21  SCORE: 41  REACTIES: 60
TITEL: Feet is killing me
POST (source_id=post):
I enjoy the work, but I don’t enjoy my feet being in severe pain after half a shift😭 I got a pair of composite toes from Zappos but it’s horrible. I know insoles can make a massive difference, I saw and felt a really comfy green spongy insole but i can’t find it so, please Rex me something!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jl138p0] (score 34, diepte 0) The insoles that come with the safety shoes might as well be cement lol
[jl12t4b] (score 18, diepte 0) Go to a podiatrist. They can make custom insoles for you that are basically indestructible.
[jl1g7jc] (score 14, diepte 1) Cement would be an improvement
[jl14j74] (score 14, diepte 0) You have to break them in. I kept squishing them any way possible and i tried the put a ziploc bag of water on the toe box and let it freeze to expand it. Also if u didnt get wide shoes your doomed, medium fit is bad
[jl1i1qm] (score 9, diepte 0) When I first started, I didn't think I would make it. I could barely walk to my car after my shift because my feet were so sore. I got some Dr. Scholl's insoles, compression socks, cusioned socks (the socks joggers and hikers wear) and new shoes a size up. This seems to be the magic combo. My feet still hurt but it's not nearly as bad.
[jl1lklo] (score 6, diepte 0) https://cadenceinsoles.com/  
Recommended by the foot doctor I went to.  You can only get the basic model online.  Mainly sold in specialty shoe stores and you can find out where in your area on the website.  An attendant at the store can help make sure they fit right.  I use the EX model and they cost about $60 bucks a pair.  Should probably note that I have fairly high arches.
[jl18ruw] (score 4, diepte 0) After being there for a year I still can’t find a comfortable safety shoe… at the end of every shift my feet end up killing me..
[jl1eyv9] (score 4, diepte 0) The toe pain after a shift is brutal 😭
[jl2at2y] (score 4, diepte 1) For me it's my heels, I think it's cause I have flat feet.
[jl1ms9s] (score 4, diepte 0) double socks and loosen your laces to make room. its how i got through 11 hour days on concrete at 325lbs
[jl2af0m] (score 4, diepte 0) Definitely get a good pair of orthotic insoles. And for a tip if you happen to be plus size, they sell orthotics for people who are heavier, which make a huge difference for your feet. The standard ones they make don’t do well for your feet if you’re caring, extra weight
[jl2q48r] (score 3, diepte 1) Second this,  I've tried many insoles to no avail going to a podiatrist made a difference.
[jl1nb3v] (score 3, diepte 3) No they won't,they will inform you you need an accommodation.
[jl1s527] (score 3, diepte 4) They won't fire you, they will ask you to get up. And you can say no you are in pain and to go get Amcare. He's a grown ass man he should be able to sit for a minute to get himself together
[jl1qg9t] (score 3, diepte 0) Timberland Pros have done me real well, first day of wearing them to now. It's been a month and a half and they're still doing great. 

https://www.zappos.com/p/timberland-pro-setra-mid-composite-safety-toe-green-tan/product/9849825/color/27963?utm_source=google&utm_medium=pla_g&utm_campaign=19821315804&utm_term=_o_56704884&utm_content=_g_146439319185_w_pla-1969145195275_l_CjwKCAjwgqejBhBAEiwAuWHioGWMVPxrXHzGhm85g3GP8s5Y_aXQ1waphA2Ik4xi7paCItkCwTAE6hoC8wcQAvD_BwE&gbraid=0AAAAADnIwa-38b95Cmne5WSgt0oEyQVXn&gbraid=0AAAAADnIwa-38b95Cmne5WSgt0oEyQVXn&gclid=CjwKCAjwgqejBhBAEiwAuWHioGWMVPxrXHzGhm85g3GP8s5Y_aXQ1waphA2Ik4xi7paCItkCwTAE6hoC8wcQAvD_BwE
[jl2kpog] (score 3, diepte 0) I gave up on Zappos shoes, they’re so damned heavy. I have a couple of pairs of Redwing composite toe boots from a former job that are incredibly comfortable, combined with thick merino wool socks and plantar fasciitis insoles, and I am usually pretty good on my feet for a shift. 

My back, however, is a different matter. I have a pronounced lumbar curve that just aches most of the time. I can only stretch it and use icy hot and/or BioFreeze pads so much. 

But my feet feel great!
[jl1m5p2] (score 2, diepte 2) People keep saying this but timb pros were the worst shoe I tried. My big toe stayed numb and I couldn't stand to bend my toes after I took them off
[jl2e5vv] (score 2, diepte 3) I got a pair myself..they hurt the sides of my feet so bad..so I'm just wearing my old shoes for now.
[jl1cnaq] (score 2, diepte 0) Literally any insole is better then no insole.  Try getting boots .5 larger and wear two pairs of socks.  Don't tie your boots really tight.
[jl1fgoe] (score 2, diepte 0) Grab a chair from the break room and sit down. Tell others to do so too.
[jl1i29r] (score 2, diepte 2) Get fired for being in pain? Sit in a chair, if it's that bad tell someone to get Amcare and they will allow the chair.
[jl1q7ir] (score 2, diepte 0) Get you some Og biggie styled timbs and some dr shoals insoles works for me ! Also been at for almost 4 years so I’m not sure my feet have feeling anymore regardless
[jl2e0uv] (score 2, diepte 1) I got pair of those not too long ago..but man, that hurt the sides of my feet. Guess gotta break them in some..
[jl2stc4] (score 2, diepte 2) Get wide ones! You have to compensate for the composite toe.
[jl4ns8p] (score 2, diepte 4) Talk to zappos customer service then, you can replace them for free with another paid and keep going until you find the right ones for you. In the meantime, try some thick woolen socks or toe caps. I'm sorry your feet hurt, I hope you find something better.
[jl20nyk] (score 2, diepte 0) Spenco insoles are the best. The green spandex ones with the black plastic arch supports.
[jl21v2x] (score 2, diepte 0) You might as well buy a pair of Dr. Scholl's. A good set should run you about $20 or so. If you are a lady then I would reccomend the Work Massaging Gel Insoles. You should be able to get them from Amazon [not posting the link]. For the men I would suggest the Heavy Duty Support Soles. Mostly for the lower back and heel pain relief 

A few other options: anything for plantar fascitis is great for anyone having to stand stationary for a majority of the shift. Another reccomendation is the custom orthotic line by Dr. Scholl's but you would need to find the machine that does the measuring. Most Walmarts and Targets have them. Don't quote me on that because things have changed in this post Covid-19 world. 

Personally, I am no podiatrist so if anything you can also consider scheduling a meeting with a podiatrist in your area. These are medical professionals that can give better advice than anyone here can give.
[jl25z4q] (score 2, diepte 0) Does anyone use compression socks? Do they help? I've been contemplating getting some
[jl28pzh] (score 2, diepte 0) It's incredibly hard work. 10 hours a day on your feet!
[jl2itmo] (score 2, diepte 0) Walmart has a pair of inserts that say something like “for fat men that do construction” you want those
[jl2sppj] (score 2, diepte 0) Please contact zappos customer service and request a different pair! They will take them back and give you new ones in a different size or style for FREE. They'll even send you a shipping label or just let you keep the old shoes. They are well known for having world class customer service and will take good care of you.
[jl3c854] (score 2, diepte 0) Get Dr Scholls ADVANCED Work insoles. Also get compression socks. Gives complete comfort, even in a cheap $15 pair of shoes.
[jl4j3t0] (score 2, diepte 0) My favorite part is after my 40 minute drive home I’d forget how how walk 😂
[jl503ru] (score 2, diepte 1) This. I live in a third floor apartment… half hour commute from the FC to home. By the time I get home and see those stairs? It’s like I’m embarking on a quest to climb Mount Everest. With one leg, in a cast, made of cement.
[jl4zsdw] (score 2, diepte 0) Friendly advice, get TWO pairs of shoes. Alternate them every other day. Your insoles need time to decompress after a ten hour shift. Wearing them every day doesn’t allow time for decompression so you just keep compressing them through your week. 

None of these shoes were intended to last the entire year. Insoles will not help once the structure of the shoe breaks down. Find a comfy pair, then buy a second. 

Don’t want to spend your own money? How much would you pay in the eighth hour on your third shift to stop the pain? Lol
[jl11g3k] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[jl4paqe] (score 1, diepte 1) Do you know how the width size chart goes? It has a whole lot of options and i dont know what any of them are😆
[jl17g1z] (score 1, diepte 0) If it’s not safety boots, I’d highly recommend ultraboosts.
[jl1gp2v] (score 1, diepte 1) And get fired? This is terrible advice
[jl1hxvz] (score 1, diepte 0) Do you wear socks or shoes in your house? Or shave your foot calluses? Callus build-up would help with your feet, fortifies them.
[jl1q930] (score 1, diepte 0) Zappos has useless shoes , go to academy or look for work boots . I spent a comfortable 200$ for some wolverine boots , added some insoles and got some running thick socks for more cushion and I can easily walk miles at work with my feet not hurting , worth the investment
[jl2yv2s] (score 1, diepte 3) I did that..still hurt, I'll figure something out...
[jl1rpcz] (score 1, diepte 0) You got soft hand bro-… wait a minute you have soft in your username that checks out. Jokes aside, you should use two insoles at the same time, sounds insane but it will make your feet more comfortable and less tired trust me.

I use Dr. Scholls Double Air Pillo (on sale at Amazon for dirt cheap) and any memory foam thick insoles online. I have the Double Air Pillo and Copper Fit Work Comfort Insoles and it works miracles. You’ll thank me later.
[jl1vw6u] (score 1, diepte 0) Are*
[jl22x51] (score 1, diepte 0) Dr scholls inserts.
[jl4o0dw] (score 1, diepte 1) They are Goated
[jl26thk] (score 1, diepte 0) Get 2-3 different pairs of shoes and insoles to switch them out during the week. Also try all the brands first and see which ones you like the most before you buy them.
[jl2pg4y] (score 1, diepte 0) Get a custom one
[jl2t2jr] (score 1, diepte 1) Also I've worn the reebok brand from them for almost 3 years now and they've always been very comfortable since I switched. Zappos team recommended them for me when I complained about my first pair.
[jl36nro] (score 1, diepte 0) Wear them more often. to loosen them up. it’s better if you can wear the a few weeks before working in them. it depends on where your feet hurt at. if it’s the sides. then you need a wider shoe. if it’s your heel. then you need to quit driving your heels into the ground when you walk.
[jl3e8pb] (score 1, diepte 0) Also, sometimes the pair of shoes you have just aren’t for your feet.

My toes are wider than the rest of my foot. I finally found a comment on a post like this about Keens shoes. One specific Keens has a really wide toe box.

If your toes are cramped, I’d suggest Keens.
[jl3p1em] (score 1, diepte 0) Thurgood or Thurgood 125s
Like having 3 sets of insoles in your shoes. May not work with tennis shoes with low heels because their so thick.
[jl3qdcl] (score 1, diepte 0 OP) Ty all for the advice 🙏 heading over to Walmart for those dr soles
[jl3s6m4] (score 1, diepte 0) You probably want to get Reebok sneaker composit shoes from Zappos.  They are the most comfortable.  At my site, it is offering insoles which help your feet.
[jl3u6g6] (score 1, diepte 0) Furuian work shoes off of Amazon. 50 bucks out your pocket BUT it saves your feet and worth it in my opinion. Stay the hell away from Zappos through Amazon. No shoes I’ve ever gotten from them have been comfortable. Can’t even bend your feet in them. Trust me I was walking 13-15 miles a shift so needed some shoes that were going to feel like clouds
[jl4wfk5] (score 1, diepte 0) Had the same problem until I switched to compression socks. Literally no pain at all.
[jl6stu9] (score 1, diepte 0) That copper fit prand that Brett Favre advertised makes some insoles..... on Amazon... the greatest thing ever invented . If they made one for your crotch it would put viagra out of business
[jl1ctwj] (score 0, diepte 1) Get tims

=== THREAD 1fmapry ===
SUBREDDIT: r/Teachers
DATUM: 2024-09-21  SCORE: 6  REACTIES: 60
TITEL: Ouch! My feet! 
POST (source_id=post):
I need to know what shoes y’all are wearing that are comfortable!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lo966nn] (score 5, diepte 0) Birkenstocks (Boston’s mostly), new balance, APL. But the big question is, do you have a dress code. I don’t.
[lo9re89] (score 4, diepte 2) You definitely have to break them in but I prefer my birks. I have plantar fasciitis and I find they feel the best and give me the best support.
[lo9ed25] (score 3, diepte 0) Birks, Hey Dudes, and On Clouds. I wear my Birkenstocks more than anything.
[lo9kmra] (score 3, diepte 3 OP) Oh wow, that is something. That sounds pretty perfect. We don’t have desks in our classroom (I teach pre-k), so when I do sit, it’s with the kids at their tables, or on the floor for circle time, or during break.
[lo9qw8s] (score 3, diepte 0) Birkenstocks, Chacos, and Taos sneakers. All have great arch support and make wide sizes for my stubby feet.
[lo9752p] (score 2, diepte 0) Ecco sneakers
[lo97s7z] (score 2, diepte 0) Birks, on cloud, brooks, Hoka
[lo9jlfw] (score 2, diepte 1 OP) On clouds are what most of my student aids wear and love.
[loatovs] (score 2, diepte 1) Brooks and Brooks only for me. Amazing shoes. They made my high arches, plantar fasciitis, and tendonitis mostly bearable for years until I finally had surgery. Still wearing them though because they're great.
[lo9jdn6] (score 2, diepte 1 OP) I’ve never heard of these. Looking them up. Thank you
[lo9t4m7] (score 2, diepte 0) Docs
[logamki] (score 2, diepte 1 OP) As much as I love all my cute shoes, I need comfort. Looks like I’ll be looking at some tennis shoes!
[loabauc] (score 2, diepte 0) I wear Converse with memory foam inserts.  Our school floor is polished concrete, which is murdering the arthritis in my feet and knees.
[loapmnw] (score 2, diepte 0) Toms
[loga1yb] (score 2, diepte 1 OP) New insoles, I feel like I need to look into getting some
[lobacqu] (score 2, diepte 0) Birks. All birds. Keds Triple Kick Canvas (my FAVE sneakers). Rykas.
[loga070] (score 2, diepte 1 OP) Thank you!
[logibfo] (score 2, diepte 2) Good luck!!!
[lo9kb6p] (score 1, diepte 1 OP) I also didn’t realize that what i know as a potato shoe is the Boston clog
[lo9jnkv] (score 1, diepte 1 OP) I’ll have to look into these, I’ve never heard of them
[loh6bfe] (score 1, diepte 2) I wore them for 7 years and would still choose them again!
[lo98oqs] (score 1, diepte 0) The more rugged flat Blundstones.
[lo9jjc4] (score 1, diepte 1 OP) Blundstones, this is a new brand to me. Thank you
[lo9jhdi] (score 1, diepte 1 OP) Oh cool! Birkenstocks are comfortable? I’ve never owned a pair. I have back problems, I want something with support. I might have to try them
[lob3188] (score 1, diepte 1) I wear Blue Ros, love my Hey Dudes but HDs do not give me enough lateral support. Wahhhh. They are cuter than a lot of other comfortable supportive shoes.
[lo9gmeh] (score 1, diepte 0) I heartily recommend Mizuno Waverider shoes.  They are excellent for comfort and support.
[lo9k4o7] (score 1, diepte 2) My wife got me some after she saw that the TV weathermen of the Midwest wore them when big storm systems came through and kept them on their feet for 12+ hours straight.
[lo9ldwt] (score 1, diepte 0) Truth is I wear cute shoes to take a pic for my friend each morning, have crocs under my desk, but usually just walk around in socks and use the crocs when I need to walk the campus. #PlantarFasciitis
[lo9okmm] (score 1, diepte 0) Birks, dr scholls, and vionic
[lo9osp6] (score 1, diepte 0) I wear Nike AF1s with a Dr. Scholl’s insole. I’m a tall dude with large feet and it keeps me comfortable throughout the day despite my foot issues lol.
[lo9x4v0] (score 1, diepte 1 OP) What insole do you use? Is it just a general Dr scholls one? I’ve never looked at those before
[lo9xgg9] (score 1, diepte 2) These are the ones I use! I wear a size 14 so didn’t have to cut them up, but if you wear a smaller size you can cut them to your size. 

[insoles.](https://a.co/d/334qqgR)
[lo9wjkv] (score 1, diepte 0) Sneakers; specifically trail runners.  They tend to come in brown and black with minimal decorative elements, have great support, and take a beating.  They're also quiet and easy to clean.
[lo9x8tb] (score 1, diepte 1 OP) Easy clean is nice! I work with younger children, messes happen!
[loa2dev] (score 1, diepte 0) Taos have good support and some cute sneaker designs! Less running-shoe-ish if you're not into that look.
[logaog5] (score 1, diepte 1 OP) Oh nice! I want
To be able to wear them with skirts and dresses
[loa5s4t] (score 1, diepte 0) I’m a man, so my input may not be helpful if you’re a woman, but I tend to wear walking/running shoes, tennis shoes, etc. A few of my colleagues wear nice shoes but the majority opt more for comfort.
[logfvtz] (score 1, diepte 2) Yep. Maybe ask for help at the store and tell the person that you’re gonna need something that’ll be comfy even after being on your feet for hours. If you’re anything like me and several of my colleagues, you spend most of the day standing or walking.
[loal6ik] (score 1, diepte 0) Sketchers step ins in black, or tennis shoes.  I can’t wear the cute ballet flats anymore.
[logai8c] (score 1, diepte 1 OP) I’m feeling my days of cute flats are over. I need support
[loamddi] (score 1, diepte 0) Veja or New Balance sneakers.
[logag5k] (score 1, diepte 1 OP) Thank you!
[loga97d] (score 1, diepte 1 OP) Do you put an insert in them?
[logc2zu] (score 1, diepte 2) Nope, I guess you could.
[loatzfv] (score 1, diepte 0) Pro tip: Crocs make a more professional looking leather/suede shoe. They're perfect if you still want the Croc comfort but need to keep a professional look.
[logaesd] (score 1, diepte 1 OP) I didn’t know crocs made professional shoes
[logn13e] (score 1, diepte 2) They're basically loafers, but they look pretty good with a pair of slacks, and in a pinch you can pull them off with a pair of dress pants. Very comfy.
[lojyc5y] (score 1, diepte 3 OP) I need comfort!
[loavqkn] (score 1, diepte 0) I rotate between my Hoka Clifton 9, Brooks Ghost Max, and New Balance 880. Pre an ongoing injury, I would wear Brooks Ghost, Birks, Doc Martens, Nike, and vans.
[logadh4] (score 1, diepte 1 OP) Which tennis shoes are your favorite?
[logasks] (score 1, diepte 2) Hokas (I wear these most often) or the New Balance. 

I like the Brooks Ghost Max but I don't find them to be as stable on the sides as the Hoka's and New Balance; they allow my foot to roll to the outside too much.
[lojyhma] (score 1, diepte 3 OP) Thank you so much!
[lob302n] (score 1, diepte 0) I wear Rothys pretty much everyday.
[loga3fx] (score 1, diepte 1 OP) I hadn’t looked at these, I will
[lob6dfk] (score 1, diepte 0) Brooks running shoes.  New insoles once or twice a year.
[loc0vc6] (score 1, diepte 0) Gravity Defyer was a miracle for my plantar fasciitis
[log9xzy] (score 1, diepte 1 OP) I hadn’t heard of these. Thank you
[locmapl] (score 1, diepte 0) Crocs - go to their website - makes shoes and sandals that are very comfortable. I'm on my feet all day long, and my feet don't hurt. Not their hideous clog things, but actual nice-looking footwear with those same comfy soles.

For cooler weather, I swear by my memory foam sole Skechers. They make boots, too.
[locmbcv] (score 1, diepte 0) Crocs - go to their website - makes shoes and sandals that are very comfortable. I'm on my feet all day long, and my feet don't hurt. Not their hideous clog things, but actual nice-looking footwear with those same comfy soles.

For cooler weather, I swear by my memory foam sole Skechers. They make boots, too.
[log9wb2] (score 1, diepte 1 OP) I didn’t realize crocs made more than one kind of shoe!
[lof0z8y] (score 1, diepte 0) Not a teacher, but still logged 85,000 steps / week as a retail picker. The shoes among my coworkers and myself varied.  Hokas if you afford them, Sketchers if you couldn't (there wear a factory outlet nearby).  But, almost everybody used aftermarket insoles.  My favorites were 3/4 length Spenco RX rigid insoles, or Dr Sholes (sp?) plantar faciitous full length insoles.  If I expected it to be a bad day (>16,000 steps during my shift), I would tape up my arches with KT tape.
[log9tjg] (score 1, diepte 1 OP) I hadn’t thought about the KT tape. I need to look into that for my partner.

=== THREAD 1x415sl ===
SUBREDDIT: r/travel
DATUM: 2026-10-12  SCORE: 22  REACTIES: 60
TITEL: Looking for wheelchair friendly ish locations to explore (Europe preferably)
POST (source_id=post):
I just got married, and we want to plan our honeymoon. We are M34 and F37. 

This will be our first holiday together as a couple, as in the previous 8yrs it was always family visits due to us being an international family. We are in Norway.

These countries are not options (as we either live there now or have lived there before)

England / UK

The Netherlands

Norway

Germany

Belgium

We both prefer city breaks where we can explore architecture, art, museums, zoo, good food etc, though also enjoy nature a lot. Appreciate this is difficult with my limitations.

Unfortunately I have a spine injury that makes me unable to walk far. I can manage 2 km in one go right now. Pain becomes unbearable if I push myself hard. 

My husband wheels me in my manual wheelchair if we have to walk long distances. I also cannot tolerate very bumpy cobblestone paths, or certain driving habits by taxi drivers (hard braking is a problem. Of course nobody can guarantee against those, but some places drive more calmly than others, we have noticed). Prefer to mostly use public transport. 

I am happy to walk a bit if there is bumpy cobblestones, but if it's the whole city then I can't do it. Italy is likely out, sadly, it has always been top of my bucket list. 

Public transport like train or tram would be great, and I am fine getting onto the train on foot, and my husband can lift the wheelchair in. I have no relevant issues in terms of balance, staircases etc, it is just distance.

We would like to go somewhere with temperatures of 20-25c. Don't mind which month, totally flexible on that. 

We prefer Europe due to travel distance, but open for other locations too.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[pfg5hmp] (score 25, diepte 0) Have you looked into Slovenia? Ljubljana's city centre is entirely pedestrianized and while the streets are covered in cobblestone pavers, they lie pretty flat so it may be more tolerable than, say, a street in Italy. There are also plenty of sidewalks, which are much smoother. (I would recommend looking up pictures/Google Street View though, since you'll be a better judge of that than me!)

[More info on accessibility around Ljubljana](https://www.visitljubljana.com/en/visitors/travel-information/essentials/accessibility-of-ljubljana-by-wheelchair)

Depending on your limitations, you can also look into a day trip to Lake Bled. There are some steep hills around town, but the path around the lake is either fully or nearly fully paved.
[pfgink3] (score 23, diepte 0) Nice France has a great accessible tram system, long flat smooth promenades
, wide sidewalks, accessible buses, a coastal train. Most of the beauty in the area is scenery and architecture, so it’s like an outdoor museum. I love the Chagall Museum but it would require a taxi uphill. Many of the hill top villages are flat in the center or have a frontage road to avoid steep climbs. Those are reached by bus. The bus in Monaco does a loop through the country (very small), so even Monaco can be visited without a lot of walking. Villefranche has an accessible route into the town from the train station. The town is hilly but has slight inclines at the far end so it’s possible to reach the seafront without too much effort or walking. Antibes is very accessible and has a TGV station. It’s my favorite town in the area and makes a great base for the area. 

Aix-en-Provence is slightly hilly but very accessible and compact. It’s my favorite city in Europe. The day tours from the tourist center offer low activity options, such as the Luberon villages market tour.


Seville is another outdoor museum that is entirely flat. The Santa Cruz district is considered one of the prettiest neighborhoods in Europe. Seville has an accessible tram system and travel to Madrid and Cordoba is fast and easy by train. Madrid and Cordoba are hilly but have accessible routes. 
Northern Spain, such as San Sebastián (spelling?) might be an option. I don’t know anything about this area. Perhaps Barcelona or Valencia? 

The Baltic countries are flat and accessible, such as Copenhagen and Stockholm. 

Don’t rule out Italy. Bologna has long smooth walkways under the porticos. Day trips to  
Ravenna and Padua are flat. 
Florence has accessible routes and buses. It’s compact and mostly flat. Even Venice has accessible routes and the accessible Vaporetto. The Vatican area of Rome is mostly flat with smooth sidewalks. The area around the Colosseum and Roman Forum has flat walkways and wide sidewalks. Both sites are accessible. The buses are accessible. Rome also has golf cart tours.
[pfg6i7e] (score 15, diepte 0) I found Vienna very easy to navigate with a stroller, so i assume it will be good with a wheel chair as well. 

Oslo is also very wheelchair friendly. Practically all public transport has wheelchair accessibility, and all new public places need to be universally accessible by law .
[pffzxl0] (score 13, diepte 0) Honestly aside from not being in Europe, I'd say Singapore!
[pfg2zsh] (score 9, diepte 0) Unfortunately my city, Lisbon is out 🥲 hills and cobblestones as far as one can see. Sorry about your injury, OP! I can't be too confident about any recommendations because I dont think in that perspective, but my last trip was to the baltics and Helsinki and I don't recall it being too difficult. Tallinn would be the worst because of the medieval old town, but Helsinki and Vilnius were quite smooth! I think the old part of riga could also be trickier, but it would only be the center, center of the town.
[pfg3srn] (score 8, diepte 0) Italy in general doesn't suit but lake garda could but you abdolutely need to drive.  There are campsites that have mobile homes adapted for wheelchairs.  These are all on the level with pools and some are next to the lake.  You just need to check whether they have proper steps or ramp into pool that you could use. Some small towns are unsuitable but many would be ok with a wheelchair.  The boat takes you to different towns as well.  
Tuscany could be an option if you get a nice hotel with a pool and relax for the mornings and go exploring for the afternoons once the tourist buses are gone.  A lot of the towns are on hills and a few have cobbles but you dont need to go far up the street.  The views are nearly   always close to car park eg san Gimignano and montepulciano.  Lots of the beauty of the area is found just driving around.  

On a completely different tack, what about south africa.  Stay in capetown for 3-4 nights, drive to hermanus, franschoek, garden route, fly home from port elizabeth.  We definitely came across lots of accommodation that would suit a wheelchair and it would make an amazing honeymoon, truly beautiful.  There is a lot about security but can only say we had an amazing time with my 81 year old mum.
[pfgfkim] (score 8, diepte 0) As an electric wheelchair user, Vienna is the most wheelchair-accessible European city I have been to. Some cobblestones, but not many, the center is walkable, and public transport is accessible (a few of the old S Bahns aren't but they come every few minutes so it's not hard to get an accessible one). I've also heard Valencia is good but haven't been.
[pffyur2] (score 6, diepte 0) not sure, but every time I have been through the balkans or balkans adjacent  counties, I have noticed very accessible cities/locations...In Bosnia, our tour guide told us its bc of the large % of public need accommodations, noticed in same in Croatia/Montenegro too
[pfghg4r] (score 6, diepte 1) Singapore is very wheelchair friendly.  Australia too, compared to Europe.  Of course, that's a bit of a trip for OP who states they prefer Europe.
[pfgbbyz] (score 6, diepte 1) Vienna is full of cobble stones and so many small steps everywhere though?
[pfircf0] (score 6, diepte 2) OMG, I absolutely don’t recommend Florence for the buses. The drivers all seem to have attended the Very Violent School of Bus Driving! Hard braking and not braking around curves. I always wondered how anyone above age 60 could remain standing on those buses. 

Other than that, I really appreciate the amount of detail  u/Loinfovoter shared.
[pfi1z37] (score 6, diepte 0) I don’t have experience of this myself, but my friend said that Barcelona is good as a wheelchair user and that the public transport system is very accessible
[pfgemrr] (score 5, diepte 0) Hey what about Denmark? Its wheel chaiir friendly esp Copenhagen but aarhus is OK (but more old houses)
[pggdrsj] (score 5, diepte 1) Barcelona was 10/10 for me.  
Rome - 1/10 - nothing worked. Starting with pre-booked accessible taxi from the airport (we got just a regular bus without ramp/lift), hotel (pre-booked, confirmed with photos, and we still got a different room…), not accessible metro, cobblestone everywhere, scooters/cars blocking the way. A mess. Just the attractions/museums were well prepared.
[pfifrzy] (score 5, diepte 0) I love Poland, especially Krakow. I don't know how  wheel chair friendly it is, but it has much better pedestrian paths. Walking around is much easier than Belgium and it's not as car centric as Belgium.
[pfg4e31] (score 4, diepte 0) My wife is in a wheelchair, my advice is to book a cabin at prairies de la mer in port grimaud.   
Contact Karin. https://www.hd-cote-d-azur.com but you might need to book via de website of prairies de la mer. It is near St tropez. The cabins are 100m from the beach. The pool is out of this world. With Nice, Cannes, Monaco, Alps within driving distance (rent a car and drive along the coast) there is lots to do. The hulpdienst used to have their own cabins and a service to the airport of Nice but something changed in the organisation. If that is not an option, there are some great opportunities at the Costa del Sol and Costa de la Luz in Spain.   


https://preview.redd.it/2qelxkhok1vh1.jpeg?width=588&format=pjpg&auto=webp&s=e06d504c72b83dec0d9b5e08d23ef9dbdc14c843
[pfiat6h] (score 4, diepte 1 OP) Thanks! We live in Norway so want to go abroad for our honeymoon. I will have a closer look at Vienna.
[pfg7zmo] (score 4, diepte 0) I would reccomend Mallorca, Spain. We spent our honeymoon there. Lovely aquarium, which is fully wheel chair accessible. Easy go get around by bus, train or metro. Beaches equipped with amphibious chairs. Bonus, frequent flights from Norway
[pficvly] (score 4, diepte 1 OP) We went there with my family some years ago, otherwise it would be a consideration :) thanks!
[pfhvdnj] (score 4, diepte 1) And with the CPH metro really no need for transportation by taxi
[pfid2e0] (score 4, diepte 1 OP) I will add it to the list! Though I have been there before (pre wheelchair). Thanks!
[pfiadpq] (score 4, diepte 1 OP) Thank you so much, I will note all down for further research. Really appreciate it.
[pgg5foo] (score 4, diepte 1) Barcelona is sensational, I'm married to a wheelchair user and we love it there. Nearly entirely accessible metro, building access is generally good, pavement surfaces are smooth and nice to wheel on. There is an assisted sea swimming service in the summer with sea wheelchairs and hoists.
[pfj18ms] (score 4, diepte 0) Vienna is a bit big, but plenty to see, relatively accessible and most sidewalks smooth.
[pfib47o] (score 3, diepte 1 OP) Thanks! The main reasons for preferring Europe is budget and whether I can handle a long journey or not - unsure at this time, but will add it to my research list
[pfif5nj] (score 3, diepte 1 OP) Thank you, I will note it down
[pfj5a7k] (score 3, diepte 0) Switzerland is very wheelchair friendly with great public transport everywhere including up mountains. Temperatures are very moderate outside of May, June, late August would work temperature wise. With your list I'd go to Basel and Zurich, with day trips to some mountainous areas.
[pfg90d9] (score 2, diepte 1) My immediate thought as to why was because of the 1990s wars and the large use of landmines..
[pfgloja] (score 2, diepte 2) Yes.
[pficg9n] (score 2, diepte 1 OP) Shame that Lisbon is out, I have never been there. I went to Riga years ago, wasn't my jam for some reason. Finland could be interesting!
[pfh26bd] (score 2, diepte 1) Wanted to also add that while a normal safari is out as its hard to get into the jeeps and tracks are way too rough, addo could be an option.  We did a day with dung beetle tours and they had a low jeep that was more like a car to get into.  Tracks are still a bit  rutted but generally OK.
[pfic4on] (score 2, diepte 2 OP) Thank you, interesting suggestions that I will look in to. Luckily we don't need to worry that much about accommodation as I only use wheelchair for long walks. I would love to see South Africa, I am just not sure I can do such a long trip right now since we are all the way away in Norway. I will look into it all
[pfialf0] (score 2, diepte 1 OP) Not looked into Slovenia, thank you for the suggestion and link, I will look into it!
[pfirqfn] (score 2, diepte 1) I passed through a corner of Slovenia on my way to Trieste, the little bit I saw was so full of charm!
[pgdcshh] (score 2, diepte 2) I see a lot of people recommending Copenhagen, which I visited two years ago. While it is true that it is flat and doesn't have cobblestones, it's also often the case that the sidewalk will have a curb so you'll end up in the bike lane—which, granted, is flat and accessible in that sense, but you'll be competing with commuters whizzing past you at 12 mph. I'd just like to push back on the assumption that biking accessibility = wheelchair accessibility. 

I've traveled a lot in Europe, particularly in Italy (for work), so DM me if you have any questions. Also, for the record I don't think *all* of Italy is off limits. I found Bologna and Padova to be decently accessible. Other more difficult cities (e.g., Rome) also work for me bc my chair is electric and I speak Italian and therefore can navigate more easily, but I wouldn't recommend them for a manual wheelchair user.
[pgflldm] (score 2, diepte 1) The old S-Bahns are fully gone as of July this year. There are still some non-accessible trains running to destinations outside Vienna, but any destination that would be of interest as a tourist will be on a line that has accessible trains running.
[pggou70] (score 2, diepte 2) Even better!
[pfizczt] (score 2, diepte 2) A few more points. 
If you visit Antibes/Nice a day trip to Menton is pleasant. It has two train stations. Get off at the second train station got a beautiful sea side walk into town then enjoy pizza and lemon gelato. 

Cordoba isn’t necessarily hilly. The walk from the train station to the historic center is downhill for about a 1km but the historic center is flat. 

Provence has small group (16 passengers) from Marseilles, Aix, and Avignon. I have done every one from Aix and I would say they are all very accommodating for people with mobility issues.
[pfifkq9] (score 2, diepte 1 OP) Thanks, I will add it to my research list!
[pfifnu9] (score 2, diepte 1 OP) Great, good to know. Thank you
[pggi2ou] (score 2, diepte 1) I was just in Basel and was thinking how everything was hilly and cobblestone... But I know that the public transit is quite good so I'm torn. I might recommend Zurich over Basel for that reason.
[pgfsagm] (score 2, diepte 0) What about Nice? It’ll offer a similar vibe to coastal Italy. All of the trams are step free and wheelchair accessible. The main promenades are paved and in good condition. You can take day trips easily via the coastal train to places like Monaco which have a series of public elevators to go up and down the hills.
[pfico5x] (score 1, diepte 1 OP) Oh I see. Sad background for the need for accessible areas, but yes that could be an option for us. Thank you
[pfin8mi] (score 1, diepte 2) No worries..i will say i've to like 60 countries and bosnia is one of my favorites!!
[pfibbma] (score 1, diepte 2 OP) Thanks! I'd love to travel further, I'm just not sure if it can be possible at this time
[pgdvsfj] (score 1, diepte 2) They did say open to other suggestions outside of Europe though.
[pgdwf0f] (score 1, diepte 2) Yeah that's definitely fair enough. May not be suitable due to budget/distance but it's very very wheelchair friendly with excellent public transport and ticks all the boxes besides the Europe one.
[pgh32w2] (score 1, diepte 2) I also am mildly immobile and loved Finland for the wide streets and easy crossings!
[pfiflly] (score 1, diepte 3) Definitely do, its a truly amazing  place, people were lovely and scenery spectacular.  They drive on the same side as us and I found it really easy to drive there, much better than europe. Long flight though!
[pfifbun] (score 1, diepte 1 OP) That is great to hear, thank you!
[pfgsdga] (score 1, diepte 0) I met a traveler in a wheelchair while in Romania this summer and he said it was much easier to get around than he had feared. He took first class train rides between the larger cities and always booked assistance. Unfortunately, there is a lot of cobblestone and the local driving habits take a bit of time to get used to.
[pfh2uy1] (score 1, diepte 0) Copenhagen had a wheelchair friendly strip laid anywhere there was uneven older ground features.
[pfifgu9] (score 1, diepte 1 OP) Oh that is awesome, thanks!
[pfh5udy] (score 1, diepte 0) I flew to Antalya, Turkey earlier this year and I noticed that among the other tourists at the passport control there were quite a few wheelchair users (plus many pensioners). Public transport is pretty extensive in town and there are also options to go a bit further to the coast. Definitely ticks the boxes for temperature (spring or autumn), food, and sightseeing - had a great time there!
[pfhl88o] (score 1, diepte 0) Maybe Denmark? Some parts of Spain? Definitely not Portugal
[pfi6fb2] (score 1, diepte 0) Denmark? Norway? I've only been to their capital cities but they seemed wheelchair friendly to me.
[pfi9vef] (score 1, diepte 1 OP) Norway is out as like I mentioned in my post, we already live here. But certainly can consider Denmark, thanks!
[pgwirm5] (score 1, diepte 0) Toronto or Vancouver both have great accessibility and many things you're looking to enjoy.
[ph1rs6c] (score 1, diepte 0) I don’t have any personal experience with wheelchair travel but curbfreecorylee is one of my favorite travel influencers on Instagram, he uses a motorized wheelchair and has traveled all over the world

=== THREAD 4ss73u ===
SUBREDDIT: r/solotravel
DATUM: 2016-07-14  SCORE: 57  REACTIES: 60
TITEL: I just landed at the airport and I have cold feet
POST (source_id=post):
I have booked a 1 month solo trip to Europe, obviously my first time going solo. Now that I am here (in Dublin), I don't know what to do. I feel home sick already and am unsure what to do or where to go. 

EDIT: Wow. Thank you everyone for the overwhelming support. After walking around a bit I did feel better for sure. It does still scare me that I have 27 days remaining but hopefully I make it through them okay.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d5bpv4s] (score 60, diepte 0) This is normal. Head to your hotel/hostel and get checked in. Then go for a walk and get something to eat. Presumably you picked Dublin for a reason. So think about that reason.
[d5bqp5u] (score 36, diepte 0) Aw man, I would kill to be in your shoes.

Solo travel is just constant problem solving.  Do you have a hostel?  If not, book one on hostelworld.  How do you get there?  Public transport?  Uber maybe?  If a bus/taxi, how will you pay?  So you better get some funds while at the airport.  Get to the hostel, chill, grab some grub, maybe a pint, and get a good nights rest.  For the next day, go do this: http://www.neweuropetours.eu/dublin/en/home
[d5brfdd] (score 31, diepte 1) > Solo travel is just constant problem solving. 

I love that!
[d5c01ej] (score 27, diepte 1) Guinness.  Guinness is the reason.
[d5bqq97] (score 18, diepte 0) Check into your accommodation, take a shower, nice fresh clothes and get outside.
Get familiar with your hotel area, see where you can grab a bite close by, see some nice coffee places and pubs.

See if you can find a coffee place with outside seating, hang around a bit, watch the world, relax. You have a month, no need to rush anything.
[d5budmy] (score 10, diepte 1) And sit around in the lobby and meet some fellow travelers. Had the same feeling when I landed in Myanmar. I stayed in the lobby of my hostel and ended up meeting a few travelers that I ended up traveling with for several day.
[d5bwlg4] (score 10, diepte 0) >I just landed at the airport and I have cold feet

>u/ironsock

Take my word for it, switching to cotton or wool will make a difference.
[d5bryq6] (score 9, diepte 0) I’m in Dublin right now. I like it a lot, but honestly there’s not a ton to do here. A lot of attractions are quite touristy. Some are still neat. I liked the Dublin Castle tour. Guinness brewery tour is a must. I’ve had very good luck asking locals what they would do. I’ve heard the best of Ireland lies out in the country, where I’m headed today. 

As for your cold feet, it’s perfectly normal. I’ve traveled solo a lot and it still happens when I get to a new place. Like others  have said, get to your room, shower, change, take a breath, and plan some things you’d like to see or do. I usually get on Google maps, download the area while on wifi so it doesn’t kill your data, and start ‘starring’ things you want to see. From there you can plan walking routes. You’ll be fine as long as you keep an open mind and a positive attitude. Drink Europe in, it’s fantastic! Good luck!
[d5bqxsv] (score 6, diepte 0) I always like chatting with my hotel/hostel front desk and asking what is going on, what they recommend, and any sites that are closed I should be aware of.
[d5bsgro] (score 6, diepte 0) Don't worry, it's completely normal. Whenever I land somewhere I always get this Laurel and Hardy-esque "here's another fine mess I've gotten myself into" thought going through my head. It turns to excitement pretty quick.
[d5bub3j] (score 5, diepte 2) And on my resume it goes.
[d5bs54y] (score 4, diepte 1) Whiskey museum, too.
[d5cf7eh] (score 4, diepte 0) You're not alone. You have us with you. Now get adventuring and report back- or else!! :-)
[d5bshhm] (score 3, diepte 0) Go to your hostel.

Have a shower. 

Check out the hostel.

Check out the surroundings.


After that, spend a short amount of time looking up things that you might like to do tomorrow.


Go get a good night sleep.
[d5bwtqd] (score 3, diepte 0) That's usually my most favorite part of every trip. There's nothing like the beginning of an adventure. 

Grab some food (you're probably pretty tired), remember why you went there, and go for a good long walk in Dublin. You'll forget about home before you know it.
[d5cyz2s] (score 2, diepte 1 OP) Well I was in Galway the first day but I'm coming back to Dublin today. As beautiful as it was, I was walking around alone and felt very lonely. And it felt as if the clock was moving so slow. I don't know how I'll last for 27 more days
[d5cz7di] (score 2, diepte 2) Try to do tours and stuff. But really, learning how to enjoy being alone is a skill and one that will serve you well in your life.
[d5c50gd] (score 2, diepte 2) I'm at the airport doing my first one, and I'm thinking the same way about this. It's challenging. In a good way
[d5bsm92] (score 2, diepte 1) Apparently their shoes are a bit chilly though.
[d5br97x] (score 2, diepte 0) Check into your hostel, ask reception what you should do, see if there's anyone you can talk to in your hostel. Don't be afraid about walking up to people and just saying hi. Daunting at first, but you get used to it, and it will soon feel like second nature.

Ask if there's a free walking tour you can do in Dublin today too.
[d5bry9k] (score 2, diepte 0) Totally understandable. I like travel but I have often felt homesick when away.

I'm in Dublin. If you need some help just shout.
[d5ch5rn] (score 2, diepte 1) haha, Cheers, I know what you mean!
[d5butn6] (score 2, diepte 0) People are nicer than you think! Don't be afraid to ask anyone, really, any strangers on the street, about where they like to go. Your hostel will help you out a lot, the workers and your roommates. The same thing happened to me last summer, but it gets way easier as you keep going!
[d5bv6u2] (score 2, diepte 0) The hardest step to take is the one to enter the plane. The second hardest is the one to exit the airport when you arrive at your destination. It's normal to feel that way. I've been travelling once every year for the past 10 years and I still have that feeling when I go to somewhere I've never been. You're going out of your comfort zone, it's a normal reaction to have cold feet. However, you'll quickly get over it and you'll have a great time.
[d5byr9s] (score 2, diepte 0) How are you feeling now?
[d5c5sse] (score 2, diepte 0) Get a good rest or nap. Secondly get yourself on one of the sandeman free walking tours to meet a couple of people but more importantly to get your bearings. I also find it helps to eat something neat... Try some irish oysters or scallops they are delicious. Go to Kehoes pub for a Guinness. I am not sure if Guinness still does this but many pubs have their seasonal flavours or experimental brews so those are worth tasting.
[d5c6nvk] (score 2, diepte 0) Put on some socks!

Then follow everyone else's good advice in this thread.
[d5c9f0e] (score 2, diepte 0) I find that treating myself to a nice meal in a place with a view and internet is a great place to start. Can get lost on the way, or look out the window, or conversation at a bar might bring up something interesting, then I look it up, aim for the convenient but expand from there, and before I know it there's a months worth of sightseeing. Have fun ironsock!
[d5c9w7w] (score 2, diepte 0) Take it slow your first day or two.  Acclimate to the neighborhood, find the grocery store and a nice cheap place for a hot meal.  Head out to the pub later and relax.
[d5cscfp] (score 1, diepte 2) I've never had one before and now I'm holding out for when I go in September!
[d5cx5ue] (score 1, diepte 3) Just go to your best irish pub-style bar nearby and get one on draft.  Bartender might not be quite as experienced with the pull, but it'll be close.
[d5iw17i] (score 1, diepte 2) Did you get a good nights sleep yet?  Cause you need to do that. I just got back from my second solo trip to Ireland last month.  I had no idea what I was doing and didn't think I could do it either. It'll come to you you just have to go for it.  You aren't going to see these people again anyway if you do something silly.

Also do the walking tours of Dublin! They meet at the spire at 12 and 3/4 I think?  Super great way to get your bearings in the city.
[d5bsfz7] (score 1, diepte 2) Sums it up perfectly!
[d5ca6s5] (score 1, diepte 2) Teeling tour as well! That place is amazing.
[d5bvmfr] (score 1, diepte 0) Yeah the first day can be a bit overhelming. Just take your time, have a walk, grab a drink in a bar with WIFI and plan your next steps.

There is no need to do a lot of cool things during your very first hours in the city. Enjoy the best part of being solo: do whatever you feel like and take it easy.
[d5bwcut] (score 1, diepte 0) Came here to say, took my first solo trip a month ago. First day was kinda overwhelming, but I went to bed, chilled out a bit, and the next day was great. Just make it through the first day!
[d5cywa1] (score 1, diepte 1 OP) I'm not usually an independant person, and really regret making this a solo trip, though no one else was willing to go this summer. 

I just really miss home already because I feel that every hour here passes by soooo slowly
[d5cywak] (score 1, diepte 1 OP) I'm not usually an independant person, and really regret making this a solo trip, though no one else was willing to go this summer. 

I just really miss home already because I feel that every hour here passes by soooo slowly
[d5dartm] (score 1, diepte 2) Go and get pissed.
[d5bx6yu] (score 1, diepte 0) Walking around is good. It will feel good to stretch your legs after cooped up on a plane.
[d5c2n5w] (score 1, diepte 0) Head outside and take a walk. Grab some food. Don't put any pressure on yourself the first day.
[d5c30tg] (score 1, diepte 0) Warm them up with a few drinks!
[d5c312v] (score 1, diepte 0) well... in dublin you have to go see the bog bodies... it looks just like they were preserved in guinness.... also go watch a irish football match...
[d5c3bgd] (score 1, diepte 0) Go see New Grange and the Valley of Tara.
[d5c3bqo] (score 1, diepte 0) What part of the city are you staying in?
[d5cyuuc] (score 1, diepte 1 OP) I was actually in Galway. Today I am coming to Dublin
[d5c3omf] (score 1, diepte 0) I felt this way when I first got to my hotel in Costa Rica. I felt overwhelmed for the first time in a non-English speaking country. I just spent about 2-3 hours in the hotel room relaxing by myself. Then I took a shower and meandered outside to get some dinner. The shower really helped for some reason!
[d5c89i6] (score 1, diepte 0) Put some socks on
[d5cytvo] (score 1, diepte 1 OP) How do you deal with the feeling of missing your friends and family, and just generally home? 

It also feels like the hours drag on so slowly. I feel bad by saying that I can't wait until this month is over.
[d5d4ri2] (score 1, diepte 2) I know that the people I miss still are going to be there when I get back. The home-world does just fine without me. And I know that while I travel, I also will be meeting new people that I will think of once I'm back home again - I look forward to to my life being enriched by the presence of good people. It's ok to miss people, I have a whole life history of always missing someone somewhere, but that just means I always have trips and friends to look forward to. And in my experience, the people, who you might be missing, would hate to know that you are missing out on fun on your grand journey just because you miss them, the people who love me want me to be out drinking in the world. Another experience of mine is that once I've spent even a week somewhere, I've developed a whole new sense of home-like attachment/loyalty to the place, whether I wanted to or not - I hope the same for you.
[d5c9xje] (score 1, diepte 0) I was right there with you about a month ago.  My cold feet came about right before my flight and remained till I landed.  Don't dwell on it too much, just do what you need to do.  Find your hostel, get settled, unpack, grab something to eat.  Something that really helped me ease into my solo journey was to keep busy.  Ask your hostel to recommend some walking tours, they are pretty handy at helping you orient yourself with your new surroundings as well as giving you ideas on what to see and do.  Its going to take a few days to warm up to this whole solo travel experience but it gets easier I promise.
[d5cfnpb] (score 1, diepte 0) Go to "The Czech Inn" and order the potato dumplings meal. You won't regret it. You're welcome.
[d5ci5to] (score 1, diepte 0) It takes me about a day to feel comfortable when I start traveling. Just remind yourself why you're traveling and why you picked the cities. It definitely helps to get some rest and food after the flight, and then and walk around. Talk to your server/barista/hostel workers. And definitely talk to other travelers. I always feel more energized and excited about traveling after talking to other travelers!
And also, make a plan for the next few days if you haven't already! You'll have things to do so you won't sit around feeling homesick haha.
[d5cs71n] (score 1, diepte 0) A good meal and a good night's sleeps can do you a world of good. You'll have a blast, enjoy it.
[d5ctup1] (score 1, diepte 0) I'd start be getting off Reddit.
[d5cxqde] (score 1, diepte 0) That was how I felt when I landed in Bangkok for my very first solo trip.   Bangkok was awful, I hated it.   It was just one big huge city and not what I expected from Thailand.    I left two days later for Chiang Mai and I loved it there.   It was so much more authentic.  That being said, I then went to Cambodia and Vietnam, and then when I flew back to Bangkok to go home, I liked Bangkok more, as I had some time to get used to it.   Still not my favorite city, but I think I would have to go back and get to know it more intimately with more time.   The first week was the hardest.   I'm sure by the 2nd week, you'll be in a groove.
[d5cys3t] (score 1, diepte 1 OP) The thing that scares me most is that I'm not really an independant person. Back home, I don't do anything alone. When I am alone, I just like to stay and home and do nothing. Also I still have 27 days which is just so much if I am already feeling like this on day 1.
[d5d1vqz] (score 1, diepte 2) Sorry if I ask, but why then did you choose to do a solo trip this long? Sounds like the opposite of what you're used to.   
I think this could end in two opposite way: you will feel like this all the time, and it will go even worse because you will be phisically and mentally tired  of all the traveling and city/countries changes, or you will break out this shell and learn to love to discover things by yourself.
[d5el087] (score 1, diepte 2) Yes, it's hard.   My first day or two, I stayed in the hostel to catch up on sleep (I was half a day behind).   I talked to some other travelers and looked on the internet for ideas to do.   Then I made a plan for the week.  Then I talked to the front desk to figure out how to get to my next destination.   It was all about putting one foot in front of the other and telling my fear to stay the fuck away.    In the end, I looked back and saw everything I had done.  All by myself.  And I had to depend on myself, no one else to get myself there.   I made friends starting the 2nd week.   Get through the first week and stay in hostels and don't be afraid to talk to people and ask what they're doing.   The hostels usually have a board with activities in the area.   It's a good time and I met all my friends from doing these activities as you kinda have to introduce yourself and be part of the group activities.   Stay strong.   You spent all this $$.   You owe it to yourself to have fun.
[d5ee362] (score 1, diepte 1 OP) Hmm I like what you said, good points. To be honest I've looked into rebooking a flight back, but the prices have been bumped up so much, that I might even spend more if I decide to cut my trip short by 2 weeks. 

So now I just need motivation to continue. So far, both mornings when I woke up I dreaded my decision to come. I mean I do feel better today than I did yesterday, but like I said, it scares me that I still have like 4 weeks to go, which is such a long time if you think about it.

