# Label-batch batch_0090

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
Schrijf het resultaat naar `batch_0090.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(1 threads: 148azkv).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 148azkv ===
SUBREDDIT: r/AmazonFC
DATUM: 2023-06-13  SCORE: 37  REACTIES: 78
TITEL: How can I make my feet less sore?
POST (source_id=post):
I work in pick 10hrs but mid shift my feet start to hurt so bad that I get to the point where I don’t wanna work no more 😭 any tips on how to improve my feet being sore

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jnz962g] (score 31, diepte 0) Insoles, re-tie your shoes after every break, compression socks, hydrate, stretch. 

Your feet swell and that causes a ton of discomfort. Re-tying my shoes after every break changed my life!
[jnzcowb] (score 29, diepte 1) Years in, still not use to it
[jnzcle5] (score 24, diepte 1) All of these and I highly recommend a warm Epsom salt soak of the feet after each shift. And take your shoes off on your breaks bonus points if you take your socks off but for the love of all things holy do that outside.
[jnz7n5c] (score 18, diepte 0) Zappos have Reebok composite toes with memory tech inserts, hover your mouse over the thumbnails to see if they have them they’re great(the green ones)You’ll also get use to it if you’re like still in your first week, take ibuprofen in the meantime.
[jnzoqu3] (score 14, diepte 0) Buy some Wintergreen Alcohol and after you take a shower rub it into your feet and calf muscles. It will heal them while you sleep. Also stretch your foot by flexing your foot up against something and leaning forward to stretch the calf muscle. Will help with the pain in your feet.
[jnzi4t6] (score 12, diepte 0) Tbh I don’t think there’s a way to get used to walking around for 10 hours. It’s just a shitty job/shift
[jnzeufv] (score 8, diepte 0) My feet were soo sore wearing my reeboks. I had calluses forming and sore achey feet every day. I ended up ordering the shoes I noticed lots of folks wearing. They are $50 on Amazon or 25 on Temu. I'm not even exaggerating when I say they changed everything. I wear them even when I'm not working that's how comfy they are. They feel like a lightweight gym shoe. If you search 'Do the best' on Amazon or temu you'll find them. If you click my comment history I commented the other day to someone asking about them and you can see a photo. They have a few different colors. I don't even use a different insole. I did order a 1/2 size up. I noticed Amazon had half sizes whereas temu didn't so keep that in mind if you need a 1/2 size.
[jnztpcq] (score 8, diepte 0) I weigh 286 lbs and it is unbearable to take the stairs after the first break. So I just camp out at the break room on the floor that I’m working on. Also bring your own lunch and stow it the refrigerator on the floor you’re working on.
[jnzbc8p] (score 6, diepte 0) By walking on your hands , or not working at Amazon on hard concrete flooring in shoes not meant to combat fatigue or vericose veins or gravity
[jo026i1] (score 6, diepte 0) Go see a foot Dr...Maybe you have a medical issues..
[jnzf71g] (score 5, diepte 0) Change of socks and shoes mid shift. Nothing else helps me
[jnzq27g] (score 5, diepte 0) I do not wear those safety shoes, luckily at my site they don't give a fk...safety shoes made my feet worse.  I will usually bring 2 pairs of shoes to work and switch them out halfway through the shift.  FP insoles are amazing, try insoles and soaking your feet in epsins salts after work and icing them.  It sucks but after a while your feet will get used to it and not hurt anymore.   Hopefully you will feel better soon !
[jo09uvm] (score 4, diepte 1) Need to try this! I've switched out my shoes mid shift sometimes that helps
[jnzpl9l] (score 4, diepte 0) Losing weight if you’re overweight helps a lot
[jo0rqll] (score 4, diepte 2) That anytime pay got us going crazy with the spending.
[jo0k9kd] (score 3, diepte 2) Oh yeah, I’ve heard you should switch what pair you wear often!
[jo07of1] (score 3, diepte 1) Can confirm those shoes are good
[jo0m5pb] (score 3, diepte 1) https://preview.redd.it/wttzeqbyst5b1.jpeg?width=1284&format=pjpg&auto=webp&v=enabled&s=453bb3a93cc99a049e43f26314ae8f0ed4de9f5e

They’re very similar to these. I suggest these if you want another pair to try!
[jnzfl74] (score 3, diepte 0) Also..alternate your footwear if possible and try to switch beteen two different pairs.  I have a couple different pairs that I swap out to give my feet and the cushioning in the shoes a break. Sneakers don't last very long.
[jnzt39v] (score 3, diepte 1) Imma try that wintergreen thing. Sounds amazing
[jnztcoi] (score 3, diepte 2) Me too
[jo0kjt5] (score 3, diepte 1) I probably gained weight and I should bring my lunch too. I'm spending too much eating out.
[jo0f1fo] (score 3, diepte 0) Get an office job and your feet will stop hurting
[jo0lwsi] (score 3, diepte 0) https://preview.redd.it/c05lbavjst5b1.jpeg?width=1284&format=pjpg&auto=webp&v=enabled&s=592283bca59ada93c3b2e413b9e74130dd06c895

I got these. Have had NO pain at all and I have like no arches. I swapped from sketchers and timberland pros. And a lot of females wear them at my SSD
[jo1k5il] (score 2, diepte 5) I think she gets new socks bc she also has super sweaty feet lmao
[jnzfrdu] (score 2, diepte 0) Salty bath, creams, legs up in the evening, streching, some power exercises for legs on one of your days off, lose some weight to have less pressure on joints, good shoes, smarter picking so your rate is high without having to kill your body
[jnzg8c0] (score 2, diepte 0) Get some of these

https://preview.redd.it/6d1p2qw8vr5b1.jpeg?width=300&format=pjpg&auto=webp&v=enabled&s=dd9841ca1fb48ae1833476b93c00a086024e4a47
[jnzh9dh] (score 2, diepte 0) Buy insoles and more comfy shoes. Try to rest your feet when you're not working. During your breaks and lunch, take your shoes off. Oh and get the hell out of pick. Using the ladder a lot hurts my feet a lot more.
[jo1zodm] (score 2, diepte 2) try vaporrub instead
[jo0o2o9] (score 2, diepte 0) Work through it and ignore it, it's what you gotta do truth be told
[jnz74b1] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[jo26pep] (score 1, diepte 1) I second the reeboks (zigtechs) super comfy, v common at my site
[jo1it5u] (score 1, diepte 3) I have a coworker that switches shoes AND socks every break, and she says it helps tremendously
[jo1jiqh] (score 1, diepte 4) Does she switch between 4 pairs or switch between 2 pairs twice each?
[jnzdbe5] (score 1, diepte 0) Compression socks, good insoles
[jo0h9fz] (score 1, diepte 1) Changing your socks helps only for a bit, I change my socks everyday at every lunch break.
[jnzfzk4] (score 1, diepte 0) Try your absolute hardest to get out of pick all them steps you gotta walk up and down is crazy.. and the amount of work they require you to do is also crazy man everybody in this sub saying they feet hurt is only in pick that’s the only common denominator
[jnzk2ug] (score 1, diepte 0) Compression socks during work, and foot soaks after work works for me.

I used to have my ex girlfriend give me massages at times. I do miss her but at times I'm glad I broke it off. Wish we were on amicable terms.
[jo2b2kd] (score 1, diepte 3) Yea that's a good one as well.
[jo142gc] (score 1, diepte 1) Would camping on the floor/pit during break and using your phone be considered a safety violation?
[jo1xp16] (score 1, diepte 2) I don’t think so unless you’re talking about actual camping like you would do at a campsite, then yes.
[jo00e8u] (score 1, diepte 0) Do you have flat feet?
[jo0119h] (score 1, diepte 0) Thick socks that are made specifically for composite or steel toe shoes. I have some made by Dickies.
[jo04jb2] (score 1, diepte 0) 2nd pair of shoes switch them out on breaks
[jo06hbi] (score 1, diepte 0) Wear a really thick pair of socks. Shoes are important as most people know, but it's nice thick athletic socks that make a difference. I prefer Nike ones but you can get some from Costco for cheaper. 

And second -- rub some thick Vaseline or equivalent at night! Wear socks with it for a bit till it gets absorbed and then take off if you feel bothered by them. You can repeat Vaseline in the morning before as well but def recommend at night! Huge difference and so comforting.
[jo0dc9p] (score 1, diepte 0) I resigned and mine were better within a week. After hurting 24/7 for 18 months. 🤷‍♂️
[jo0dxhv] (score 1, diepte 0) Get more comfortable insoles
[jo0epge] (score 1, diepte 0) Running shoes are probably the best for picking if your FC doesn’t mandate safety shoes.
[jo0sdov] (score 1, diepte 1) This is the only right answer tbh
[jo0gh4e] (score 1, diepte 1) Here’s some of the shoes I have purchased and love.

My go-to

https://www.zappos.com/p/skechers-work-workshire-composite-toe-black/product/9584280/color/3

I also like these

https://www.zappos.com/p/bogs-shale-leather-chelsea-ct-wp-oxblood/product/9686783/color/537

And finally, these bad boys are super comfy but also bright pink… they also come in a decent tan color.

https://www.zappos.com/p/moxie-trades-alice-pink/product/9623759/color/559
[jo0gweb] (score 1, diepte 2) I also have used these from Amazon, in a wide, would not recommend. I have a blister on my big toe, and like I said I don’t have wide feet. So these run super narrow. But I really liked the color…

https://www.amazon.com/gp/aw/d/B00U6IMTSC?psc=1&ref=ppx_pop_mob_b_asin_title 

And also, consider investing in a couple pairs, and alternate every day. You should not be wearing the same pair of shoes and insoles day in and day out. The foam in the shoe compresses, and can cause foot fatigue. Nurses usually change shoes within the same shift sometimes, if they have significant foot problems. So consider changing up your shoes regularly so your feet can get the proper support.
[jo0h6to] (score 1, diepte 3) For reference… I’m the only person in my entire group of new hires from the last month who’s feet don’t hurt at all when I’m at work, I work shipdock. And I’m the only person with multiple pairs of shoes because I invested my own money in them in addition to the credit, Becsuse I’m not gonna have fucked up feet.
[jo0grq8] (score 1, diepte 0) Combat boots, padded/gel insert soles & thick socks.
[jo0hxxi] (score 1, diepte 0) The right shoes, and also your feet adapt to walking that much. Mine were the same way for a while. Now i can pick all day and my feet feel fine. It was better before the shitty safety shoes were mandatory. Your body will get used to walking that much abd the pain should go away.
[jo0kfgf] (score 1, diepte 0) What I do is I re-tie my shoes every few times. I have a foot massager at home, and when I come home, I use it right away it hurts, but it helps. Using foot cream also helps a lot.
[jo0o1u0] (score 1, diepte 0) Wellness center and use the back roller on your feet
[jo0oanq] (score 1, diepte 0) Frozen water bottle, 3/4 way full. Roll your feet across it for a bit ..the cold helps reduce swelling, and the pressure massages the feet muscles. ✌️
[jo0pylo] (score 1, diepte 0) Ultraboosts from adidas. Does wonders.
[jo0vdvh] (score 1, diepte 0) amputate
[jo0wmw9] (score 1, diepte 0) double socks and loosen laces to make room
[jo0ylxt] (score 1, diepte 0) https://preview.redd.it/9oqja2bdbu5b1.jpeg?width=2266&format=pjpg&auto=webp&v=enabled&s=6722b371496143020e7c7708c785efe92dbff1c2

Get these shoes plus some Dr. Scholl insoles. Fixed my feet issues instantly.
[jo11pm0] (score 1, diepte 0) I got a foot transplant from a cadaver and I've been feeling great. Cost me 70k
[jo19xjt] (score 1, diepte 0) Massage ball, biofreeze, insoles, compression socks and stretching
[jo1gru4] (score 1, diepte 0) Insoles and warm soaks helped me a lot.
[jo2k3g3] (score 1, diepte 0) Same, I have insoles and everything. I get a huge blister on the soles of my right foot only. It’s like I heal during my off days and my second day of work the blisters come back all over again. Ughhhhh
[jo3gpkd] (score 1, diepte 0) Insoles & taking shoes off during breaks
[jo4fbtt] (score 1, diepte 0) It’s the lower back for me. So sore all day
[jo6emno] (score 1, diepte 0) Everyday when you get out of the shower rub Vicks vapor rub on your feet, cover with socks and go to bed. This will help to soften all the callus on your feet making them much more comfy.
[jnzemc9] (score 0, diepte 0) *
If you can get a pair of these. My feet no longer hurts at all.
[jnzf8uc] (score 0, diepte 0) K TAPE SAVED MY LIFE.
[jnzgfd4] (score 0, diepte 0) get some insoles. zappos sells them, you can use your credit if you have it. take some ibuprofen before your shift and take a short break if you need to. also stretching does wonders.
[jo0vifg] (score 0, diepte 1) people for real asking how to take care of their own feet 😔
[jnzjdfd] (score 0, diepte 0) I work in sortation, idk if you work on that area too. but for me, to help me make my feet hurt LESS, is definitely wear thicker socks and not thin ones. as the obvious, get insulation pads for your shoes. biggest thing, trust me, they do not care if you have your scan rate at 700 (exagerating lol) or more, they will just praise you and that's it. take your time, don't run or speed walk. know your speed and what speed you are most comfortable with on the daily and not just at work. 

when it comes to scanning, I realized when i 1st worked there I was always speed walking, but now I kind of take my time, but a good walking speed. but I suggest get ALOT of small packages 1st until you reach 120, then you can even be abit slower when grabbing bigger ones. and keep doing small ones (BUT GET ALOT. AS MUCH AS YOU CAN) if you ever getting too low. also. if you're a girl....use the restroom to your advantage lol, obviously don't go there every few minutes, but use it, when you KNOWW you can't handle it no more LMAOO

that's what helped me LMAOO...also...please...DRINK LOTS OF WATER😭😭
[jnzjm0c] (score 0, diepte 0) Go to The Good Feet store and get their shoe inserts. My ex used to be a store manager at the 28th street location in G.R., MI and they will be able to get you fitted with their inserts that will help realign you posture and back to help you stop having a lot of your feet, knee and lower back pain your experiencing. But if you do so. You need to listen to them to a T when it comes to the system the tell you to abide by. Because I would be able to tell if you weren't. Trust me, it'll change your life in a very amazing way. Hope all the best to you my friend
[jnzjmb1] (score 0, diepte 0) Go to The Good Feet store and get their shoe inserts. My ex used to be a store manager at the 28th street location in G.R., MI and they will be able to get you fitted with their inserts that will help realign you posture and back to help you stop having a lot of your feet, knee and lower back pain your experiencing. But if you do so. You need to listen to them to a T when it comes to the system the tell you to abide by. Because I would be able to tell if you weren't. Trust me, it'll change your life in a very amazing way. Hope all the best to you my friend.
[jnzo82f] (score 0, diepte 0) You might have flatter feet and the arch is too much! 
People swear by custom insoles, not to expensive and for some they work wonders. 
I personally, at least for the first 6 months or so of working would change my socks at lunch and it always helped a ton
[jo031h7] (score 0, diepte 0) I wore crocs in nursing, are you allowed to wear them if in sport mode? Only shoe that doesn’t hurt my foot and breaks in perfectly a bit nerdy but worth it for less foot pain
[jnzepnh] (score -1, diepte 0) Timberland field boots, I know it sound crazy, but I tried them Zappos shits and tried working in some air maxes..the timbs is my go to
[jnzkkt6] (score -1, diepte 0) Don't wear safety shoes. They all suck

