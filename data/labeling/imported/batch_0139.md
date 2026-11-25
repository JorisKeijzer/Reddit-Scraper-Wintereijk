# Label-batch batch_0139

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
Schrijf het resultaat naar `batch_0139.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(8 threads: 1jqxhf3, 12mdgot, g1dos1, 15zjjmt, 15fxttl, 1f9rw2k, 1kfn7g2, 1ksbshc).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1jqxhf3 ===
SUBREDDIT: r/ehlersdanlos
DATUM: 2025-04-03  SCORE: 10  REACTIES: 52
TITEL: Which would you choose and why?
POST (source_id=post):
Obviously everyone has somewhat different experiences, but I'm wondering which of these products you would choose to prioritize purchasing and why (and alternatively, feedback on if any are gimmicks or not worth it is appreciated):
-stability shoes: brooks Ariel or adrenaline (my geneticist said I have weak ankles and my arch collapses)
-posture wearables: leaning towards alignmed brand or possibly tommie copper but that one seems less supportive/recommended from what I can tell. Am particularly considering leggings and sports bra as I think they might help with my posture and back/shoulder pain
-compression socks: maybe Wellow brand? I haven't researched these much though so if this, tell me your fav!
-body pillow or knee pillow: I get hip pain and knee pain when I sleep sometimes (side sleeper) so I was thinking about the Bearby cuddler, but I'm also open to other suggestions if you have one you love. 
-weighted blanket

I wish I could just go purchase everything on this list and try it out, but unfortunately I have to pay my mortgage and feed my cats lol

Thanks for sharing your experiences, thoughts, and tips!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mlaemqv] (score 7, diepte 0) i personally love my brooks sneakers, my ankles like to roll easily and with the brooks i have they’re stable. i went through one pair, wore them every single day till i wore them out. i got another pair, and they’re the most comfortable sneakers i’ve ever had.
[mladcic] (score 6, diepte 0) Squishmallows also save me from alot of pain while side sleeping and are cheap!
[mladagl] (score 4, diepte 0) Personally compression garments are a life saver with POTS. that and the body braid for alignment and joint pain
[mlahih2] (score 3, diepte 1 OP) Oh interesting! I’ve seen them recommended but didn’t realize it was for side sleeping specifically. Why do you think they help? Do you think they give you enough support in your legs/ankles, and do you wish you had anything for your back/shoulders? Or do you use them there too?

Also, the username checks out lol 😊
[mlb0w32] (score 3, diepte 2) I’m a back sleeper and I still sleep in an encampment of various sizes of squishmallows. I move them around and adjust their placement depending on where they are needed that night. I don’t think I’ve ever seen them referred to as specific for side sleepers.
[mlah5zj] (score 3, diepte 1 OP) Oh that’s great to hear! Which ones do you have? Do you run too or mostly just walk? Do you think you have a better idea of where your joints are/has it helped with your posture and other pain? Do you have flat feet?
[mlahhc0] (score 3, diepte 2) i have the levitate ones, i think they discontinued them but renamed them? idk it’s weird. and yes definitely, i noticed that it supports my ankle joints a lot, it does help my posture a little bit. and i do have flat feet
[mlai2kw] (score 3, diepte 3 OP) This is really helpful info! Thanks for sharing! I’ll have to look into them and see if I can figure out which ones they are 😊 were these ones recommended to you or how did you find them?
[mlaigpy] (score 3, diepte 4) no problem! and honestly i found them in dicks sporting goods just looking for a new pair of sneakers, and i tried a lot on and those were the ones that i really liked
[mlajquv] (score 3, diepte 5 OP) That’s great! Were you specifically targeting the stability ones or those ones just spoke to you? 

A few weeks ago I did try the brooks glycerin and they were SOOOO comfortable but I don’t think they were stability focused and they were so soft that I would worry they’d be more likely to cause an injury… but I also have no clue really, just thinking that seems like logical reasoning?
[mlawgrl] (score 3, diepte 0) I have lymphedema, POTS (etc etc) on top of EDS but compression garments do help! 

I love my weighted blanket but sometimes it causes pain if I’m laying the wrong way and I can’t lift it alone 

Having a good pair of shoes are essential!! I personally have rx AFOs (due to several muscular / skeletal issues) but beforehand if I didn’t have good support in shoes my life was so much worse 

Body / knee pillows have been a hame changer for me but in a pinch you can use a regular pillow between the thighs or legs to get some relief too! 

Wearables have been helpful but I asked my doctor what he thought personally would be helpful (I’ve wasted so much money on experimental braces) 

(Not listed but) 

4% lidocaine roll on cream - (you can get the generic brand for about $5 USD depending on where you live) it may not be a cure all but it takes the edge off! 

Shower chair - I don’t faint in the shower anymore and helps with fatigue! (A bit pricey around $30)

Toilet seat with handles- I got this after my spine surgery and have used it ever since (also a bit pricey around $50)
[mlb017e] (score 3, diepte 0) Squishmallows as pain pillows, I’ve gotten affordable ones on sale from Target. Compression socks. I’ve gone thru a full gamut of price ranges looking for very good ones and I have learned Doc Martins on Amazon are my preferred fav. They cost a fraction of my Jobst, which I could only afford 2 pairs, on sale, and they are heavier and come on much better funner options. Plus, they go on sale and offer coupons… they last longer and I won’t look at another brand again. 

I cannot use weighted anything on me as the pressure of just regular blankets often causes my chest to compress and I go Brady. It also can displace my ribs. I don’t really have options about shoes bcz I buy only what I can at the moment, my rent doesn’t allow me to think too far outside the box. I also cannot afford compression leggings, or other gear, even tho my Cardiologist and Primary have said I should wear more compression.
[mlak4hu] (score 2, diepte 6) i was targeting more stability, and i just feel like any brooks shoes is good, i feel like they have the shoes for anything that’s needed
[mlb2pnb] (score 2, diepte 7 OP) Cool cool! Makes total sense. Thanks for letting me ask you very invasive questions about how you chose your shoes 😂
[mlb2txa] (score 2, diepte 8) omg it’s okay i don’t mind at all!
[mlfve98] (score 2, diepte 1) Thank you- my right ankle ROLLS at the worst possible moments.

The last time I was getting off a horse, I fell off the horse and landed in a big heap on the ground because I suddenly didn’t have an ankle…it was SO embarrassing.
[mlai8od] (score 2, diepte 0) I would say no to the pillow, if you’re looking to narrow it down. I got one a few months ago (a big U-shaped one) and it hasn’t helped my hips or supported other joints more than any other pillow. On the other hand, I can’t live without my weighted blanket!
[mlal5b9] (score 2, diepte 2) For the pillow, I’m a “supported flamingo” sleeper so I tried to choose one that fit my sleep style. I’m not sure about the blanket, I got it on sale at Home Depot lol but it’s 15lbs and the love of my life
[mlatwkw] (score 2, diepte 0) Sports bras and tons of pillows for bed would definitely be my top two and they're pretty affordable. Compression stockings are life changing if you have POTS. Weighted blankets are great for anxiety but I personally had to stop using them because the weight was compressing my joints and causing extra pain, you might have better results with a lighter blanket
[mlaufis] (score 2, diepte 0) personally… I’ve loved my brooks for shoe recs, I also wear sports bras and leggings for mild support, I found the brand Comrad for compression socks of all sizes and styles, and I highly recommend a body pillow or plushies like squishmallows for support in your sleep! I’m looking into a Body Braid for posture support as well!
[mlb1z5t] (score 2, diepte 1 OP) The sock rec is amazing! Thank you! 

And interesting re: the squish mellows. They seem well loved! Is it just the price or is there something extra special about them as compared to other options?

Just wondering re: compression - would you be able to get prescription compression and have insurance cover? Is that a thing? Idk if it is but I get the budget being tight and having to make choices! Usually I buy socks for my husband and I on Black Friday… actually I do most of my shopping then to get the best deals, but I track prices throughout the year so we can purchase when on sale because otherwise we will just have holey socks and stretched out undies bc everything is so expensive these days 🥲
[mlb6xfp] (score 2, diepte 2) I hear ya! For most of the years, it’s been tricky bcz years and years ago, if I needed a splint or brace, my Dr wrote for it, and I brought it to a specific med surg pharmacy and it would be covered, these days with my Medicaid… it’s so hard. I had to pay out of pocket for all of my splints and braces except for one just this past year at the OT, simply because they had that one in my size there at the office and the rest they didn’t so instead of them ordering what I needed, they sent me home to order what I needed. 

Things are crazy expensive these days, check Prime Day in July sales. I don’t typically always wait for Black Fridays anymore, bcz most Black Friday sales now start November 1st…. It’s just not the same no more!
[mlb14ay] (score 2, diepte 0) I wear Brooks and they are good. There are no shoes that have high enough arches for me, but I really like these. If you have a Fleet Feet store near you… I highly recommend them. They take all your measurements and help you pick the best shoes. Compression socks are a must for me. But I only use ones from Amazon, because I can’t wear them long anyway. Everything puts marks in my fragile skin… but I can tolerate them for a couple hours. A body pillow helps and feels good, but I toss and turn so much that it becomes a pain to keep flipping around.
I suppose a weighted blanket is a preference, I don’t like any pressure on my body.
[mlb1gtb] (score 2, diepte 1) Oh… I have extremely high arches and they are collapsing. Fleet feet showed me how to lace my shoes differently so that helps a lot too!!! I have Glycerin GTS 21’s
[mlb47cb] (score 2, diepte 2 OP) I went to fleet feet with my husband a couple of months ago (before my diagnosis) just to try some things out bc he wanted new cross trainers, and my favs were the new glycerins! So comfy! I also have a regular/high arch that’s collapsing, but they didn’t notice the collapsing. My geneticist pointed that out. Apparently I have almost narrow feet and in particular my heels are very small but since my connective tissue in my feet is spreading out, I always thought I had wide feet! Nope, just my shoes don’t stay on my heels and it was putting weird pressure on the tops of my feet and toes 😅 

One question for you - the glycerins are soooo comfy, but do you worry they are too soft? Like do they provide enough stability to help with pronation and ankle support ?
[mlbeiog] (score 2, diepte 3) I also have small heels! I feel like they provide the most stability they can while still maintaining the comfort. Does that make sense? I have in regular and in wide… I definitely have more comfort in the wide. I size down a half size in wide. I also have a ton of problems with shoes on my heels and I have never had that in these shoes. I do also use these as my gym Shoes and I love them.
[mlb5nht] (score 2, diepte 0) BODY/ KNEE PILLOW. I cannot stress enough how much that has helped me. You spend about a third of your life sleeping; make sure you are treating your body right when you do. It helps literally everything else.
[mlbi2il] (score 2, diepte 2) Honestly, the best one I have found is a candy corn Squishmallow. I put that between my knees and then put my whole self (including the Squishmallow) into a Hug Sleep Sack and it helps IMMENSELY. The Hug Sleep Sack keeps compression on my whole body, and it keeps the Squishmallow in place when I roll over!
[mlbacg5] (score 2, diepte 0) Oh man, I want a weighed blanket... Not one with the glass beads though, a heavy knitted one
[mlc08r8] (score 2, diepte 0) At the moment, I am a BIG fan of my compression socks. The ugly, OG copper ones work wonders for neuro and circulation pain. As well as my gigantic body/pregancy/U pillow. I too am a side sleeper, and this changed my life. My knees and hips couldn't take it anymore so I took a risk on a kinda expensive pillow. Took a day or two to acclimate, but pays off every night. Another goodie is my shower bench/chair. Finally let go of my "I'm too young" pride, and that thing saves me when I need to lean, sit or help getting in and out of the shower.

This is a tough one to answer generally or overall, though. I hope everyone keeps in mind that everybody battles with different things and are progressing or residing on different ends of the spectrum. *That said, I don't believe there are any wrong answers here!!* Things that work for one, may be a waste of money to another, but that does NOT invalidate. 

I've always said I'd piss on a spark plug if it meant I would feel better. I don't care how crazy it may seem to me or anyone else, if it works, CHECK PLEASE. Who cares! It can be a sliding scale even individually, too. Things that work now may need to be adjusted or changed later and that's okay too.  Evey battle requires its own army of resources. Listen to your body, and be open to safely, of course, trying things out without any predetermined negatives or positives!
[mlcr872] (score 2, diepte 1 OP) Love that for you! Which pillow did you pick? My shoulders, knees, and hips have just been in so much pain for a while so that’s why I was considering it. 

And yes! You’re totally right. That’s actually why I made this post - I wanted to hear folks preferences and lived experiences, especially as compared to their symptoms, expectations, and decision making. Specifically because there’s so much to learn from each other (humans are often really bad at predicting thing how they will feel about something in the future/the results of a decision), and yet we still have to factor in our own symptoms and lived experiences with this kind of feedback. 

Im so thankful everyone has been so open and helpful - I know I’ve learned so much from every single answer on here!
[mlagwvr] (score 1, diepte 1 OP) Woah!! The body braid looks amazing! Did you find it helps with posture and pain a lot? Did you ever try any of the posture garments like alignmed? Wondering how they compare. 
Also, when do you wear the body braid? 
Do you have favorite compression garments?

My appointment with the cardiologist is next march (lol) but I don’t think I have POTS. I do think I have some form of dysautonomia or something though because my hands and feet are always cold, except when they turn red and swell when I’m hot. And I get dizzy in the shower or if I worked out too hard or haven’t slept or eaten enough. But the racing heartbeat doesn’t really affect me and I passed a tilt table test (my heart rate only rose like 10BPM and my blood pressure like 18/5 increase or something). So, I think I’ll benefit from this some but I am not an extreme POTS case like I know some folks experience.
[mle71ik] (score 1, diepte 2) The body braid is a GODSEND for my shoulder blade, rib, and hip pain/subluxations. Especially the rib area. Like seriously. I was bawling the other day trying to breathe through the stabs, popped it on, and could inhale deeply. It also helps with posture although I have cervical instability so I do have to be careful not to let it pitch my neck too far forwards. I also really like compression biker shorts for my SI pain and wear them together. I wear the braid when sitting, reclining in bed, or the rare occasion when I’m up and about. Just not lying down because it digs into my armpits. For the socks I buy bamboo ones off amazon! I don’t like wellow personally because they’re soooo thick and I have very bad heat intolerance but if your feet run chilly you might love them!
[mlb3gsv] (score 1, diepte 3 OP) Oh no you’re totally right… I just assumed people meant for side sleeping because I’m a side sleeper 😅 whoops! 

Also love “an encampment of squish mellows” LOL
[mlb4rsr] (score 1, diepte 4) Yep! 😂 the stackable can be holding one arm in place so I don’t move my clavicle, the round basic size can be on the other side shoulder, the massive mama bun (mine are all bunnies) can be behind my shoulders elevating my head, or under my knees taking pressure off my hips, between my knees, etc.
[mle7bv4] (score 1, diepte 2) lol! I use one on my side under my arm to support my shoulder and between my knees for my SI. Also sometimes use one as a pillow when my neck is very bad! I buy the stackables so they’re more flat. And I prop against a 24 inch one when sitting up in bad. It’s the best I’ve found compared to all the special expensive pillows out there. I also use a stackable as a wheelchair cushion
[mlaivh0] (score 1, diepte 1 OP) Ooo we love a hot take! I wouldn’t have expected a weighted blanket over a body pillow. Which weighted blanket do you have? Do you think the shape of the pillow has anything to do with how helpful it is?
[mlb0tp4] (score 1, diepte 3 OP) I toss and turn, but alternate between traditional side, “supported flamingo” (I’ve never heard this term before but I love it!), and “frog” which is actually a yoga pose but I def sleep in it sometimes lol. So that’s why I was considering the long one, seems like I could adjust for my main sleep styles. However, it’s interesting that you didn’t find it helpful and seem to be similar. Do you think that’s because it’s so big and bulky and difficult to work with, or just that it doesn’t really provide much relief like you were expecting? Something else?
[mlb95t6] (score 1, diepte 4) I don’t find it too bulky, but it just doesn’t hold me in a safe/comfortable position. I think I just need to get a mould of my body made at this point lolol. What I’d honestly really like is a massage bed so I can lay on my stomach without craning my neck or crushing my nose! I wonder if there are pillows with a face cut out…
[mlb10ff] (score 1, diepte 1 OP) So you like individual pillows? Why is that?

And good to know about the weighted blanket! What weight were you using? That’s my worry honestly, but then some folks love them
[mlb64nx] (score 1, diepte 2) I find l can customize my support more with multiple pillows instead of with one big one.

I think it was like 12 pound? It was really calming but then the pain kinda canceled it out after a bit
[mlb2ju5] (score 1, diepte 1 OP) Any favorite brands for any of those? 😊 what’s making you consider the body braid?
[mlb2fb1] (score 1, diepte 1 OP) This is a wonderful list, thank you!!

I have a shower chair from when I had knee surgery. And I’m a big fan of biofreeze and acupressure. 

I am curious about what brands you’ve tried and liked for the weighted blanket, body/knee pillows, and wearables (and particularly for the wearables, which ones gave you the most relief and why?).
(9 reacties met lagere score weggelaten)

=== THREAD 12mdgot ===
SUBREDDIT: r/ehlersdanlos
DATUM: 2023-04-14  SCORE: 7  REACTIES: 35
TITEL: compression stockings?
POST (source_id=post):
went to a cardiologist who told me that it was super obvious i've got "some kind of dysautonomia" and potentially a mild case of POTS, but since she feels that i am not severe enough to be worth medicating, told me to get compression stockings and eat a bunch more salt and see if that helped. if it doesn't help, she said she would give me the tilt table test then and consider medication. so i guess i'm gonna put my best efforts forward and try to follow those instructions and see if it helps.

in the interests of not wasting money on crappy compression stocking brands, what brands do you use? i've tried the copper fit ones because they were available at my walgreens, they definitely compress and can offer some relief to my ankle pain, but don't do anything for the dysautonomia that i've noticed.

thanks in advance!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jga4rw0] (score 12, diepte 0) I don't have a stocking reccomendation but you need to drink water as well as adding extra salt. I have POTS (Tilt table test positive). I don't wear stockings but do wear tight running  compression leggings for physical activity and find it helpful.
[jgahu40] (score 8, diepte 0) Bibipins.com. I love their stuff. I'll admit I don't have the stockings, but I have 4 pairs of compression gloves, ankle braces (2), wrist braces (2), hip braces (2), and wheelchair gloves. Love all of them.
[jga6cmg] (score 6, diepte 0) I wouldn't stress about brands. I've bought lots of them from CVS and Amazon and never had any issue based on brand. CVS is more expensive (I only get them there if I forgot to pack some while traveling). The biggest concern with compression stockings is getting the right size.  Measure your calf and thigh and if you are on the cusp of a size, go up not down.
[jga5sjr] (score 3, diepte 0) I had compression stockings custom ordered from a medical supply store, you can call stores in your area and see if they do measurements and stuff
[jgabjy7] (score 3, diepte 2) I think it was around $200? My doctor wrote a scrip in the hopes it would get covered by my insurance but it didn't xd always worth a shot tho
[jgbrqgw] (score 3, diepte 1) I now want to spend all my money here, lol.
[jgbrnkm] (score 3, diepte 0) I’ve been using [comrad stockings](https://www.comradsocks.com/collections/compression-socks/products/knee-high-compression-socks-solid?variant=39813737644066&gclid=CjwKCAjw8-OhBhB5EiwADyoY1VEEEGvwZ3wTwPKvJDljh-VEm375TPxyqo5FBcyjHxtN4waQakzQDRoC7n4QAvD_BwE) for almost a year now and love them. Definitely wait for sales (25% right now), you can usually stack codes as well. They’ve helped me a ton, especially on days when my pots acts up. 

I’ve heard a lot of really good things about vimvigr too. Never tried them myself as they’re out of my price range but they have fun patterns and stuff.
[jgbsgb1] (score 3, diepte 0) >compression stockings

Needs to be thigh high and abdominal!

Source: https://www.sciencedirect.com/science/article/pii/S0735109720379079?via%3Dihub
[jga51pa] (score 2, diepte 1 OP) yeah, she mentioned the water, i just forgot to include in the post. what compression leggings do you use, do you wear them all the time? she said i would likely need to wear compression stockings all the time.
[jga66w1] (score 2, diepte 2) Oh good! Yes it's all balance! I wear standard brands of running leggings (my favourite are lucy locket loves as they have pockets!). I wear them for times when I'm active (walking dogs, gardening, swimming, if I have lots of walking or standing to do like going to a museum etc) but not just "lounging". I personally struggle most in the heat so temperature regulation is important for me and I find these leggings don't make me too hot as most are " breathable" or "moisture wicking" as designed for sport.
[jga7ba5] (score 2, diepte 3 OP) yeah i'm also really bad with temperature regulation, i tend to run really warm all the time, so breathable is also definitely required in any kind compression garment i get. thank you for sharing!
[jga7swd] (score 2, diepte 4) No problem! Everyone is different so it's trial and error to find what works A lot of the time. Good luck!
[jgad0fk] (score 2, diepte 0) I get super cute ones here: https://vimvigr.com/

I love that they come in wool (less stinky) and also pass as ordinary knee socks. Just check with your doc to make sure you're ordering the correct compression level.
[jgddkwv] (score 2, diepte 1 OP) oh those are pretty fun. i'm probably going to stick to plain ones so i don't end up looking too girly wearing knee highs with my shorts, since i'm a dude, but i'll bookmark that and maybe get some colorful ones when pants season rolls around again since i am a bit of a sucker for fun socks. thanks for sharing it!
[jgdcvy3] (score 2, diepte 1 OP) oooh sounds like they've got some good stuff then, i'll definitely give them a look!
[jgfue3k] (score 2, diepte 2) It's definitely a site I recommend checking out. And they're disabled as well, so they definitely understand needs and quality products at decent prices. Plus, they're always so helpful when I ask questions.
[jgbrdqk] (score 2, diepte 0) Jobst ftw.
[jgdg7mq] (score 2, diepte 1 OP) thanks, got a couple of suggestions for that so i'll give their stuff a peep!
[jgbt7m1] (score 2, diepte 0) Jobst relief!
[jgdlr12] (score 2, diepte 0) These are super comfy compression socks I found on Amazon .fenglaoda Compression Socks for Women Circulation 20-30mmHg Crazy, Cute, Socks Support for Nurse, Pregnant, Running, Medical https://a.co/d/ex03vK7 Also nursemates are a good compression sock brand
[jgetuij] (score 2, diepte 2) You're welcome :)
[jge2klw] (score 2, diepte 0) I have hEDS and severe dysautonomia/PoTS. My dysautonomia specialist said class 2 compression stockings are the only type that would really make a difference but he would never recommend them to hEDS patients because they're so tight that we're likely to dislocate fingers and thumbs putting them on and taking them off. 

Instead, he recommended high compression gym leggings in a size smaller than normal - something like Fabletics anywhere motion 365. They've made a real difference to me. 

Studies show that compression to the waist is significantly better than just to the knee.  But please be careful of your fingers if you decide to go for compression socks or stockings.
[jge67mr] (score 2, diepte 2) I find the compression leggings actually help my knees because it's like wearing a well fitting ace wrap so they give support. I can't comment much on hips because mine are (thankfully) ok for the moment. 

They're definitely more gentle on your body than jeans because the fabric is softer yet super supportive.
[jge7d6v] (score 2, diepte 3 OP) that's nice to hear about the help for the knees, even wearing those elastic "jegging" type jeans was too intense on my knees, i'll have to see where i can try on some leggings and see if they work alright with my hips/knees. i think there's a fabletics not too far from here. thanks for sharing!
[jga7doe] (score 1, diepte 1 OP) oooh, didn't know that was possible. i do have some medical supply stores around, I wonder if they'd be able to do custom ones. how much did that end up costing, if you don't mind me asking?
[jgdczv5] (score 1, diepte 3 OP) i'm sure medicaid wouldn't cover it for me haha. i'll keep that in mind if i can't find a premade kind that works well for me though! i do have a compounded medication i need made custom, so i'm no stranger to custom medical needs.
[jga7hkl] (score 1, diepte 1 OP) ...hm. this might be the first part of my problem is the only brands i've been exposed to in-person around here are ones that do not have sizes, they're just...one size fits all compression socks... and i've got pretty small legs. i think i'll check amazon, lol.
[jgfttsz] (score 1, diepte 2) That's my problem hahaha. They're constantly releasing new things and I want them half because I need them, half because it's so cute.

They have a Twitter both for the store and more personal, and they've always been helpful when I ask questions.
[jgdg5h9] (score 1, diepte 1 OP) thanks for the rec! and yeah, i looked at vimvigr and it seems fun but maybe only for like, a pair or two just to be fancy, i could definitely not afford to do that daily.
[jgdd9as] (score 1, diepte 1 OP) hmm, i'm not as sure about this because my knees and hips are very sensitive to any kind of pressure--when skinny jeans were all the rage, i basically couldn't buy new pants because it would compress my knees and hips to the point of pain. do you have experience with compression garments that go over the knees/hips, and do they loosen up in those areas so they don't cause joint strain?
[jgl6dtx] (score 1, diepte 2) Yes, it's "graduated" or something compression, which I believe means it's tighter lower down and looser up top. Although, I never got into skinny jeans, so I have no comparison.
[jgdg894] (score 1, diepte 1 OP) :) thanks for the rec!
[jgdtjiv] (score 1, diepte 1 OP) sweet, i like how affordable those are for being nicer looking ones. thanks!
[jge5mfl] (score 1, diepte 1 OP) interesting. have you noticed any increase in hip pain from wearing the leggings? that's my big concern with anything that would go over one of my worse joints--my hips and knees are both pretty bad, so knee socks seems safer for my legs since it doesn't go over either of those. do the compression leggings have like... looser areas in the joints or anything to account for that issue?

i have problems with even jeans shoving my hips out of place because they're so prone to subluxation. do you find that the compression leggings help reduce your subluxations at all or do you just kinda deal with them?
[jgkjtve] (score 1, diepte 0) Vim+Vigor! Excellent options and colors, plus wide calf options. You can get cheaper mystery packs off their website.

=== THREAD g1dos1 ===
SUBREDDIT: r/Construction
DATUM: 2020-04-14  SCORE: 107  REACTIES: 21
TITEL: My live lesson in Skilled Trades, and why I now hire professionals whenever possible. Enjoy the story.
POST (source_id=post):
Ever notice how expensive plumbers are? There’s a reason for that. Cheap labor isn’t skilled, and skilled labor isn’t cheap. They’re worth it. Let me tell you about one of my scars that constantly reminds me of this fact.

I was barely eighteen, and my weirdo friends and I had just rented a city block of downtown Grand Rapids, Michigan. 26,800 square feet of the most decrepit real estate in the industrial ghetto. It was an old, ugly, brick monstrosity that had a style all its own. We loved it.

We were also young, inept, and dangerously naive. 

The last thing the landlord did after I signed my life away was point at a hatch just inside the front door and say “that’s where the main water valve is” as he jogged, giggling, to his car and got out of there as fast as possible.

The building had sat empty for well over a year, inhabited by a dozen homeless people who were burning barrels of trash for heat and using every nook and cranny as a toilet.

Don’t worry, they had used the toilets too. There were several of them scattered around the south end of the building across several floors. Every last one was a moldy heap of dried shit layered over a foot high above the seatless rim.

How the fuck do you even DO that? I cannot imagine the thought process that leads someone to look at a toilet, with no water, no hope, and a bowl already full of a dozen other people’s shit and say “yeah, there’s room, I can do this”. I don’t know who you are, freakshow-champion-vaulting-shitter, but cheers to you mate. 

I also knew that I would see you in hell before I was the one to clean those motherfucking toilets. I grew up in farm country and I’ve mucked stalls with the best of ‘em. I’ve experienced the warm joy of having a deluge of cow shit sprayed down my back in a milking parlor. I’ve cleaned plenty of toilets before, but this was a whole new level of shitpocalypse. I don’t believe there’s any job that’s “beneath” me. But there was no way in hell I was going to clean those. If I had to handle it myself, I’d just bag and tag those fuckers and toss them wholesale in a dumpster.

But I knew what it cost to replace one, and I had to find a cheaper way.

We had already run all the homeless guys out, so I had to do a little looking. It took perhaps five minutes. I found a little man in his 40’s sitting under the back loading dock. He was literally in his 40’s, he had a tiny fort of empty 40-oz beer bottles that he had used to wall off the two open sides.

“Wanna make a couple bucks?” I asked, as I knelt down and caught a glimpse inside. If he wanted privacy he shouldn’t have built a glass house.

“For...uh…. what?” he said cautiously. I imagine his mind was going to dangerous and disgusting places already, but he certainly wasn’t expecting what I was about to offer.

“The toilets inside, I need someone to clean them. You want the job?”

“What’s it pay?”, he said.

I thought for a moment, I tried to imagine what it would take to compel me to undertake such a task. Tyvek biohazard 5-layer pressurized full-body suit with a battery powered ventilator, double nitrile gloves, layers of tape sealing, booties, boots, one of those big yellow city vacuum trucks they use for cleaning out storm drains, 500 gallons of bleach, 50 gallons of quaternary cleaner, fifty-thousand dollars in my pocket, a bottle of The Balvenie, and a nymphomaniac midget to aid in my recovery from the mental trauma.

“I’ll give you a hundred bucks.”

“Each.”

You little motherfu- “Sure, deal. When can you-” he was already moving and bounding through the loading dock door before I was even standing up.

He walked through the back door, straight through the entire building, and right out the front door without saying a word or slowing down. He foraged perhaps 20 feet into the empty lot across the street and came back seconds later with an empty coffee can.

He marched directly into the first bathroom, just off the lobby in the corner of the stairs and with no gloves, no mask, no hesitation, and no fear used that rusty old coffee can to get a big scoop of dried human shit and carried it across the street into the field.

I tried very hard to just keep lunch where it was intended, standing well away, and upwind as much as possible. I told him to holler at me when he was done and made sure to stay well to the other end of the building for the next few hours.

I had to get this man some water, he was going to need it.

I enlisted the help of a couple of the guys, we stationed one man on each floor; we had a foolproof plan. We were going to open a faucet in a sink or something, on each floor. Then I would crack the main valve and slowly fill the system with water. Once the air had all vented out and the water was running smooth and clear, each person on each floor would close their valve and we’d be set. Easy, simple. I got this.

I opened the old wooden hatch inside the front door. I don’t know exactly what I was expecting, but a 2 foot wide hole, deep enough to stand waist deep in…...that wasn’t it. Deep, down inside, about a foot off the bottom, was a pair of valves with a meter in the middle. The pipe was massive. I was used to living in a house, with a main water feed that was perhaps an inch in diameter at most, usually ¾ inch. This fucker was as thick as my arm. I hadn’t yet learned that the building was originally a brewery, a century ago.

I gently, slowly, opened the outer valve, upstream of the meter. It clicked a couple times, but nothing scary happened. I opened it slowly, turn by turn, until it gave me enough resistance to know I was all the way there.

“Everyone ready?!” I yelled up the stairs. Several shouts came back, it was time.

It was also rigidly stuck.

I turned it gently; it didn’t budge. I tried harder, and the valve made it quite clear that my 130lb intellectual frame simply didn’t have enough lead in my ass to make this happen. So I hollered for Mikey.

Mikey, well...he’s a big sumbitch, and that’s exactly the kind of guy I needed at that moment. I showed him what was going on, he laughed at me, and hopped down in the hole. It held on his first attempt so he tried again with two hands. I told him to hang on a second and I was going to let everyone know it was finally time, as we’d been screwing around for several minutes to get to this stage.

I walked over to the stairs and gave a shout. Several bored and mildly irritated guys hollered back.

“Go for it,” I told him.

And he did. Mike gave a grunt, the valve gave a snap, and he started cranking for Jesus. We heard the water flow in the pipes, the meter made a tikatikatika sound and we just heard the quiet rushing of water for several seconds. We thought everything was working just fine.

That’s when the screaming started.

A lot of screaming.

From several people, on several floors, all at once.

The unintelligible cacophony was immediately understood and I shouted at Mikey to close the valve. He did, but not before the waterfall started to descend the staircase.

It’s like seeing your teacher at the grocery store dressed in leggings and a t-shirt. It’s something you’re totally familiar with, absolutely normal, and yet it just fucks with your head. I’m fine with water. I live in Michigan, water is what we do. I’ve seen lakes, rivers, creeks, and even a waterfall or two.

Stairs, groovy, seen tons of ‘em. I can go up, down, I’m even ok with the spiral ones. Being a man of grace and poise I have even accomplished the rare and difficult trick of falling up the stairs. Stairs and I, we go way back.

But this was the only time I’d ever seen a waterfall cascading down a staircase. That…..that’s fucked up, man.

I was not in any manner prepared for the sheer volume of water that came down the stairs. It was easily in the hundreds of gallons. It filled the valve hole, overran it, and poured out onto the sidewalk.

It’s ok, it’s just a broken pipe, I can do this. I can fix this. I got this.

So we went to the hardware store, and I figured it out. Copper was the fancy stuff, that shit’s expensive. Ok, so that’s out. This white stuff though, PVC, this is cheap. We can afford this. I had a long talk with the sales dude and he taught me everything he knew about how to do plumbing with PVC pipe.

It took about five minutes.

I got a pile of pipe and fittings, a can of glue, and all I needed was a tape measure and a hacksaw and I already had both of those. We’re set. We’ll have working water in a couple hours.

“Fuckin’ plumbers, what do they know. This isn’t that hard. I’m a goddamn genius of plumbing.” I thought to myself.

The plumbing system for the building was super simple. The feed came into a bathroom on the ground floor, then passed by into the White Room just behind it. That’s where the one and only water heater was, a fifty-gallon contraption that may have been there since Vietnam and made for the only part of the job I was scared of. Lighting the pilot on a water heater just puckers my ass and always has. But I’m a rugged man, a manly man, and I can light a water heater, dammit.

The water heater twin pipes (because now we have hot water!) launched vertically up through the ceiling to the second floor. They just pass on through to the third so that’s easy. On three I had my apartment, kitchen sink, toilet, bathroom sink, shower, done. It wasn’t everything in the building, but it was enough to get started and establish basic life support. Also….I’d definitely run out of pipe by then, so it would have to do for now.

Sure, all the pipe was exposed, just anchored to the brick wall. It may have looked like it was done by a one-armed blindfolded twelve year old with ADHD while cranked out on meth. But it was done, and I did it. I was radiantly proud of myself. Fuckin’ plumbers, what do they know.

We slowly turned on the water, and only had one leak. There was a spot where the plastic PVC pipe had to thread into the metal water heater and it leaked like hell. Clearly I hadn’t gotten it tight enough. But now that it was all glued together, I can’t turn the pipe.

Ok…….cut the pipe with a hacksaw, then turn it. Glue in a coupling and it’s all back together a few minutes later. Turn the water back on…...and it leaks even worse, what the fuck.

Ok, cut it apart again, this time we make a whole new end (because it was getting short now), put it all back together, bring it up slowly…..no leaks! SUCCESS!

It worked great, and I was thrilled. The stinking masses were thrilled too; finally we could have real showers!

The warm glow of success lasted maybe two whole hours. But at least that was long enough to let Shea finish the toilets, and for that we were all thankful. I gave the little fucker a hundred-dollar-bill every time he started hollering and proudly showcased a clean toilet. By the end of the day he’d made five-hundred bucks, and I never told him that it’s a damn good thing we didn’t have six toilets. I had about forty bucks left to my name. 

After he was done we forced him to go get a “clean”-er change of clothes and take a shower upstairs. He looked like the floor of a dairy barn that needed mucking. He didn’t need a washcloth, he needed a squeegee and a pressure washer.

He came down looking like a new man.

Right about then was when the fountain started in the White Room. The cold water line just launched right the fuck off the top of the water heater, leaving the fitting still inside. I was a floor above it and heard something, followed by a lot of yelling. We got the water turned off and started fixing it... again.

Thankfully, the White Room was empty except for the water heater off in the corner. It was about the size of a two-car garage, with brick walls painted stark white, and a floor drain in the middle of the room. The mess wasn’t a big deal to clean up. 

The good news was that we had enough parts to fix it. The bad news is, we didn’t have enough parts to fix it properly. So now we only had water to one toilet, and the White Room. The only running water in the building was the water heater itself, the lavatory sink for the bathroom next to it, and that one toilet. We had no money for more parts, and it was Saturday night. Even if we did have money for the parts we needed, nothing would be open for days.

But, we had a garden sprinkler. One of those with the arched bar about a foot-and-a-half long that has a row of holes in it. They spray a fan of little streams that sways back and forth. We found it in one of the many random piles of debris left by a century of previous tenants, complete with about twenty feet of only slightly crusty garden hose. This was a wonderful discovery, because we quickly realized that the only hot water source we had in the building was the hose spigot on the bottom of the water heater.

With a bit of nylon construction twine we tied the sprinkler vertically to the steel support column in the middle of the White Room, at about five feet off the floor. The hose ran down and across the room to the water heater, which was now cranked up to somewhere between Tea Kettle and Saturn-V.

We could all get showers! But we only had about ten minutes of hot water, with no temperature control, and it came from a sprinkler. The solution was simple.

We all got naked.

There comes a point when working together that you can all get so filthy and everyone stinks so bad that you just don’t give a fuck anymore. Modesty goes right out the window and nobody cares about dignity at all. Everyone stripped down right there and stood in a circle around the sprinkler. We opened the valve on the water heater and the sprinkler cracked to life, spraying a blast of water hot enough to fill the upper half of the room with steam in the first couple minutes.

We walked, slowly, around the pole like some strange naked pagen cleansing ritual and quickly worked out a system. You adjust the temperature by how close you stand to the sprinkler. You stand there, spin around a couple times to get wet, and as you step out of the water the person ahead of you hands you the bottle of dish soap - it’s what we had.

Then the next person gets the sprinkler, while you soap up with a healthy handful of Palmolive For Pots And Pans, and once they step out of the water, you pass it to them. You scrub like hell, everywhere you can, as you walk around the circle. No sponge, no washcloths, and this ain’t a loofah kind of place. You use your fingertips like God intended, and try to scrub as much crud as you can. Eventually, right around the time you’re freezing to death, about half dry/half crusty with soap, you get to the sprinkler again and rinse as much as you can. If you need, repeat the cycle.

With this system, twenty-three highly motivated people can have a hot shower that’s reasonably decent before the tank goes completely cold in about nine or ten minutes. If you just use the hose, and no sprinkler, the water goes cold in about three minutes and then you’re fucked.

It worked surprisingly well, and we all got some hilarious memories from the week of sprinkler showers. There’s no way you can endure such a thing and not get a few laughs out of it. I would not recommend this as a typical corporate team building exercise in today’s world, however.

It took a week to be able to get a couple bucks for plumbing supplies, but I pulled it off eventually. I fixed the water heater connection, and even built a proper shower in the white room and one on the second floor as well. With three seperate showers we were now living in luxury. We had hot and cold running water to the kitchen, and life was awesome.

One nice aspect of abject poverty is that you quickly learn to appreciate the little things. Hot and cold running water that is clean and safe to drink is pretty damn awesome, and the overwhelming majority of people in America take this for granted every day.

After a week or two, we did as well. Fuckin plumber’s, what do they know.

It was a beautiful June morning as dawn broke over the city. My gigantic arched-top windows in what was now my third-floor apartment were four feet wide and twelve feet high. They all faced south and west. With the sun itself blocked, dawn appeared as a wash of light crawling down from the west into the Grand River Valley and flooding the world with hope.

I crawled down half-awake from my pallet-rack and plywood bed and stepped into the shower. I turned on the water and in my zen state eased into consciousness with wonderful hot water and a bottle of some random green Amway body wash that my girlfriend’s parents had given me. All was good in my world.

Then...I woke up, very cold, in an awkward position laying on the tile floor of my single-stall shower. There was a lot of blood everywhere.

The water was spraying in a single giant stream like from a garden hose, straight from a hole in the wall where the shower head had been a moment ago. I hurt in places you don’t even know you own, and I was somewhere between scared as hell and pissed right the fuck off. I wasn’t sure whether to cry or to kill the next motherfucker I saw with a clawhammer. Either option felt like a perfectly acceptable choice at that moment.

I managed, with no small amount of difficulty, to stand up. I turned off the water, stepped out of the shower, and looked in the mirror. I looked like the drippings from a drunken fuck. I was covered head-to-toe in goosebumps and way too much blood to be only mildly concerned. The shower looked like a Manson Family Christmas Special, and I had no idea just what the fuck was going on.

It took me a while to piece it together, but as near as I could figure out, this is what had happened. The shower head had exploded off the wall when the fitting broke where it turned horizontal from coming up the wall. The old metal shower head smacked me in the forehead, and it was either that, or when the back of my head hit the wall when I fell down, that knocked me out. I was bleeding from both sides, so it’s anyone’s guess on the details.

Fuckin’ Plumbers, what do they know?

They know that you have to use purple fucking primer when you glue PVC pipe together. Because the glue is a solvent, and while it can and does bond directly to the pipe, the joint won’t last and can pop apart after a while if you don’t use the purple primer to etch the smooth surface first to give the glue something to grab on to. 

They know that you have to use teflon tape and pipe dope on threaded fittings, and which ones to use each for. They know a thousand things that I didn’t. It turns out that there’s a lot more to being a plumber than just knowing that shit flows downhill, payday’s on Friday, and “don’t chew your fingernails.”

It took me a week’s work, and another few hundred bucks, to tear apart the whole plumbing system and rebuild everything - this time with primer on all the joints before I glued them. Still, none of it was anywhere near code, but it worked, and it got us through a couple years until we could get the experienced help that we needed.

I still have that scar on my forehead. It serves as my daily reminder that “Skilled Labor Isn’t Cheap, and Cheap Labor Isn’t Skilled”. 

Plumbers, Electricians, Carpenters, HVAC Techs, and all of the other skilled trades are far too often looked down upon in our society as idiots that didn’t go to college.  I want you to remember that the next time you’re sitting there missing some manner of fundamental service in your life. When the heat won’t work, you’re sitting in the dark, or you’re standing there ankle deep in shit.

They’re expensive, because it’s a hard job that pays well, you can’t do it, and they’re a hell of a lot smarter than you gave them credit for.

They’re worth it.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
(20 reacties met lagere score weggelaten)

=== THREAD 15zjjmt ===
SUBREDDIT: r/ehlersdanlos
DATUM: 2023-08-23  SCORE: 2  REACTIES: 0
TITEL: Baby zebra looking for relief from this insane heat wave and the lovely chronic pain! TIA
POST (source_id=post):
On my long rough diagnosis journey! Seeking advice/recs for products that have worked for you! TIA!!!

Hello you beautiful zebras! I have had chronic joint and muscle pain for…. My whole life? But it got really bad about 10-12 years ago. I finally found a PCP that has referred me to the Ehlers-Danlos clinic in my area, after many years of medical gaslighting (Cincinnati), I am also suspected to have the trifecta; MCAS and POTS. 

Sooo with that being said, what are your favorite compression garments? Or really just anything useful. Until a couple months ago I’d never even heard of hEDS, and I assumed since I never actually fainted my tunnel vision/seeing stars/heat intolerance etc was just… heat intolerance? Idk. It’s wild the things you will consider normal when you have had chronic pain your entire life 🥲

So far I have Sockwell compression socks (love), copper fit compression gloves, Hokas (obsessed), and I have some compression shorts (not medical grade bc I’m over here balling on a budget!).. the heat in my area is just killing me. I have tried increasing my salt and I drink liquid IV/Gatorade/etc. just wondering if maybe any of you wonderful folx might have some magic tips/tricks for reducing pain and feeling like death in the heat!

Thank you all so much! 🦓🖤

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

=== THREAD 15fxttl ===
SUBREDDIT: r/ehlersdanlos
DATUM: 2023-08-02  SCORE: 3  REACTIES: 0
TITEL: Compression gloves
POST (source_id=post):
Anyone with wider palms have suggestions for gloves with more even compression? I just got a pair of copper fit gloves and have tried different sizes, but they all pull my hand so that it’s kind of cupped which messes with my metacarpals

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

=== THREAD 1f9rw2k ===
SUBREDDIT: r/ehlersdanlos
DATUM: 2024-09-05  SCORE: 1  REACTIES: 0
TITEL: Compression gloves with health watches 
POST (source_id=post):
Hi all! I know that there are a ton of posts about compression gloves on here already but I have kind of a specific question. I am looking for compression gloves with longer fingers and shorter wrists so I can still wear my health watch and keep track of my other conditions. I’ve had the issue with the copper compression gloves that the fingers are too short and the wrists are way too long for me to comfortably wear my watch. Ideally I would want to find gloves that would cover the middle knuckle of my fingers. Does anybody have any suggestions?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

=== THREAD 1kfn7g2 ===
SUBREDDIT: r/ehlersdanlos
DATUM: 2025-05-05  SCORE: 1  REACTIES: 0
TITEL: Bracing and splinting options
POST (source_id=post):
Currently diagnosed with hEDS. Im also a hairstylist. I recently made the decision to stop cutting hair and focus only on color as color hurts my hands less. I am looking to get some of my hand splinting and to replace my shoulder brace. 

heres the spliniting im looking to get:

(1) MCP / IP combo (or just mcp) for right hand

(1) 2 1/2/ Buddy ring for right hand

\- also need 6 regular swan splints and one more of each already mentioned for the left hand. I was going to get them from silver ring splints but everything combined is nearly $1,000. I need them to be metal because i intend on wearing them while blowdrying and the plastic swan necks will warp from the heat. I am very rough on my hands so i need something durable.

  
As for my shoulder brace im looking for something functional but with all around support. I have a labral tear, rotator cuff tear, and a type II ac separation. My current brace is the copper compression recovery brace, it does not provide enough support as i can and do still sublux while wearing it. I need it for my left shoulder and i need it to come in a small/extra small adult size option or an extra large pediatric option. I am quite skinny for a 21 yr old and i need it to feel secure or i wont wear it (im autistic, the sensory is insane).

thank you all so much for any help in advance

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

=== THREAD 1ksbshc ===
SUBREDDIT: r/ehlersdanlos
DATUM: 2025-05-21  SCORE: 1  REACTIES: 0
TITEL: Tommie Copper sale
POST (source_id=post):
Tommie Copper has a full site sale of 50% right now (5/20-5/27, 2025). Im in the US, not sure if it’s different other places or if they ship but thought I’d give a heads up!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

