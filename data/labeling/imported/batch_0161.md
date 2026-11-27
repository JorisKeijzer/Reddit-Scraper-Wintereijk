# Label-batch batch_0161

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
Schrijf het resultaat naar `batch_0161.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1fos9vl, 1q1rmkw, 1j5kb7a, 15tn65u).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1fos9vl ===
SUBREDDIT: r/Serverlife
DATUM: 2024-09-25  SCORE: 7  REACTIES: 59
TITEL: Advice for aching hips, legs, feet after work lol 
POST (source_id=post):
Fellow servers, I am a (proud) corporate drop out coming fresh from 4 years of sitting on my fat ass in front of a screen at home, to the relentless standing, walking, carrying, bending, and awkward manoeuvring of server life. I have no regrets, but what do you do to stop your body from aching so much when you get home? lol

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[losavbj] (score 32, diepte 0) Wearing good quality shoes is paramount. Replacing them on a regular basis is also important.
[loscuzq] (score 13, diepte 0) compression socks 🧦 you know how old white people have splotchy gross legs? it prevents tht lol
[losa8re] (score 11, diepte 0) Take a hot shower and advil.
[losoa3u] (score 11, diepte 2) If you are willing to spend money, I recommend Hoka Bondi SR. They are slip resistant and come in different colors or black. I was in so much pain I stopped working doubles and now that I bought these I feel so much better. They were 175 plus tax
[losdkrx] (score 8, diepte 0) Hokas, compression socks, laying on the ground on my back with my legs bent over the couch to get blood flow/drainage
[losemxh] (score 7, diepte 0) Weed
[losajlj] (score 6, diepte 0) Sleep. You’ll get used to it quick!
[losi9cl] (score 6, diepte 0) Exercise! Lower back and back workouts, squats, foot massage rollers, good shoes plus insoles, stretching, and massage gun. The tension and stress built on back and shoulders need to be relieved. 

Also I am not sure how old you are, hut that just comes with age too lol. But exercising legs, back, and stretching is crucial especially as you get older.

I use orthofoot.com

I get the wide shoes and add insoles on top of them
[losibcw] (score 5, diepte 0) Yoga and stay active before work. Don’t be sedentary just because you move a lot a work. I usually hit 8k steps before I start getting ready for work and then do another 6-8k at work. 

I’ve found for me, that constant movement and work makes my body hurt less. Now I have a leg up, I work at our barn 7 days a week, from 9-3 most days and then work 5-10 at the restaurant. I also hit the gym 3-4 days a week. 

If you don’t stop moving, death can’t get you 😂😂😂
[losb9x7] (score 4, diepte 1 OP) Can you recommend any brands or types? We’re allowed to wear any type of trainers (sneakers) or whatever, there’s no strict dress code or uniform, I’d like to invest in comfy trainers but not sure what’s important to look for in comfy footwear haha!
[losj3kj] (score 4, diepte 2) I use Skechers but also add extra cushion with a shoe insert. They aren’t so big and bulky like shoes for crews and Dansko’s but are still skip resistant. I love mine and get a new pair once a year (I usually get around 10k -12k steps in a shift) https://a.co/d/2MVcYQi
[loses4v] (score 4, diepte 1 OP) Wow did not know that but seems important to know!! 🤣 thanks!!
[losj0qi] (score 3, diepte 4) The danskos are not like every clog 😆 they feel great and they last a long time.  Crocks are okay too but they don't really support your feet as well imo. I find them comfy as like house shoes, not as much work shoes
[lot0zyg] (score 3, diepte 3) Sanita is also a great brand for restaurant use.  And they aren’t cushy kind of comfy, but give you crazy support for you back hips and knees.  When I made the switch, I was amazed that I didn’t wake up and walk around like a grandma for the first time in years! BUT if you are clumsy, they do pose a big risk to rolling/spraining ankles (I lasted 10plus years before doing that tho!)
[loslz3h] (score 3, diepte 3 OP) Sketchers were definitely top of mind in my considerations! I’ll check out their range :)
[losyzza] (score 3, diepte 4) Skechers been good to me for 4 months so far
[lostxi7] (score 3, diepte 4) Came here to recommend the same ones… just bought mine
[losu37v] (score 3, diepte 2) check the nursing subreddit they recommend sock & insole brands <33
[losvpan] (score 3, diepte 3 OP) 🙏 thanks for tip !
[losd5fu] (score 3, diepte 0) Stretching
[losf9gc] (score 3, diepte 2) A shoe brand that are incredibly comfortable, durable, and supportive for walking. I was putting 20k steps a day for like 5-6 months and only replaced them because they got cut on top. My lower back and knees weren’t hurting like other shoes after 3-4
[losm8dx] (score 3, diepte 0) Sit with your legs up the wall for like 30min.
[losi0ji] (score 2, diepte 2) I love my dansko clogs so much. Very comfortable but they take a little breaking in and getting used to
[losxfj9] (score 2, diepte 4) The HOKA bondi SR did not work for me. I bought two pairs and I hated them both. I over pronate already and these shoes just made it worse. I wear them and it looks like I’m walking on the sides of my feet and I technically was and it was so uncomfortable. However, the HOKA Clifton’s I love them. Best shoes ever. I wear them in combination with compression socks and it’s amazing. Only downside is, they’re not non-slip but I take my chances.
[loseh6o] (score 2, diepte 0) Targeted yoga for problem areas. I found "yoga with Adrienne" on YouTube, she's great. Look for neck/shoulder relief, and one for tired feet

Works wonders if you stick to it
[losfego] (score 2, diepte 2) I do it before bed, some leg stretches in bed. My daily goal is 30 minutes. The neck and shoulder relief video is gold. 

Once you learn the stretches, you can incorporate them in to daily life. You don't have to say "ok now it's yoga time!"
[lositai] (score 2, diepte 1 OP) Hahahah! Bet you’re in amazing shape!!
[loslx2m] (score 2, diepte 0) birkenstock tokio supergrip. best shoes I've ever worn for service.
[losm03f] (score 2, diepte 0) Your body gets used to it after a few weeks. Any time I’ve taken a break from work my feet, legs, and hips ache like hell after each shift. After a few weeks, my body readjusts and it doesn’t hurt anymore.
[losn45z] (score 2, diepte 1 OP) For real I think this is a major one!!!
[losxn99] (score 2, diepte 0) Whatever you do, do not buy work crocs. They gave me plantar fasciitis and the pain is excruciating. All day, every day.
[lot9rfq] (score 2, diepte 0) Yoga and stretching. 

Seriously. 

Every morning when I get out of bed I have a yoga routine and series of stretches. 

Signed,
40yo lifer
[lov161g] (score 2, diepte 0) Get a good pair of orthotics. I spent $700 on a pair when I was managing Chuck E Cheese, my feet felt amazing after a few weeks and this was a 60-70 hour work week, always on my feet. The orthotics were game changers, the job broke me and I'll never work another second in the restaurant business. 25+ years and happy to be gone
[lovfjnn] (score 2, diepte 0) I'm surprised no one has mentioned it already- aching lower back? Hinge at the hips!!! Whenever you have to bend over, keep your back straight, and hinge at the hips/knees. It may look a little funny but I promise you it is so much better for your back health. 

If just standing makes it ache, I'd be willing to bet that you probably didn't have the best posture when sitting for hours and years on end before, so that's why the sudden change to being upright in correct posture often may be giving you pain. I have lower back pain often due to lumbar lordosis. My favorite yoga position for lower back pain is karnapidasana. I didn't do yoga before beginning this, and I suspect my ability to accomplish it off the bat is because of my hypermobility. But it is an advanced level of an already intermediate pose, so maybe work your way up to it? It also stretches your hips and hamstrings! The pose it's derived from is halasana, and another variation is supta konasana. It's advised to avoid these if you have back pain, but that's for people with herniated discs, sciatica, whatnot. Check out the other reasons why someone should avoid doing them though in case you fit any. If not, I highly recommend these. 

Make sure you don't lock your knees when you stand. I'm guilty of this (again, hypermobility) especially when I'm standing in place washing dishes or cooking (when I serve there's way more movement happening so it's easier not to but just keep it in mind). Get good shoes, maybe wear insoles if necessary? When you get home, rest in any way that involves blood flowing out of your legs. I like to sit with my back on the floor, and my legs straight up against the wall. But you can also lay down and have your feet propped up, just anyway that keeps your legs elevated. Taking hot baths with salts for muscle aches every once in a while feels good too. 

Also, the more you work out the muscles in those surrounding areas, the less strain it puts on the joints and whatnot. You want to search for exercises that strengthen the knees and hips. This kind of stuff is important for everyone, but younger servers can get away with not doing it.. for a while. It catches up to you. Take care of yourself. It's definitely more rewarding than corpo stuff I find.

Good luck!!!
[louizlk] (score 1, diepte 1) I personally am a big epsom salt bath guy. Soak those aching bones
[losil54] (score 1, diepte 3 OP) Did not expect to hear clogs here but I am open to just about anything right now!!! 

Also got me thinking: crocs. Surely. Crocs for the win
[lotay64] (score 1, diepte 5) My only issue with my Danskos are that the instep isn’t high enough for my feet…well, that and the platform on them has caused a few too many ankle rolls lol
[losodm4] (score 1, diepte 3 OP) Thank you!!! Gonna check it out 🙏
[lotkdtz] (score 1, diepte 2) Go to a shoe store that specializes in walking shoes. Running sneakers and walking sneakers are build differently to accommodate the foot, have them do all their fancy stuff and suggest a shoe to you or a good insert for your fav shoes. 

A big one for me was to get a Thera Gun and do a leg and foot massage after my shifts and a foot before my shoes on for the day. Helps a TON! (Last job was 16hr doubles) and trust me I’ve tried a lot of the off brands… just spend the money and get a real theragun if you go that route, the cheap ones are cheap for a reason and their motors aren’t strong enough
[loypvet] (score 1, diepte 2) Crocs. Take it from a lifer. They are the best shoes in the biz.
[loset7i] (score 1, diepte 1 OP) What’s Hokas?
[losfefn] (score 1, diepte 3 OP) Amazing, will check it out online, hopefully I can get to the UK!! Thanks 🙏
[losoeqz] (score 1, diepte 3) I second Hokas
[losfjzi] (score 1, diepte 2) Brand of shoes
[losezm4] (score 1, diepte 1 OP) I loooove yoga with Adrienne!! And I know she has one video specifically for service workers as well. Definitely need to get serious about incorporating the daily yoga (or as much as I can) now!!
[losfpxl] (score 1, diepte 3 OP) Very true!!!
[losista] (score 1, diepte 1) Yassss I’m an edible girly!
[losiwwb] (score 1, diepte 1) Yesss im an edible girly but good shoes do help!
[losiq2x] (score 1, diepte 1 OP) amazing! What kind of exercises do you do out of interest?
[loskt41] (score 1, diepte 2) I mean i don’t know the exact back lat pulling machines. Also working abs. 

Since working at corporate and sitting a lot, excess normal average also plays a role. So perhaps some weight loss is needed (depends on everyone’s body type and normal range) The heavier set server i have always seen are the ones who are dead after a shift. I work with servers 50+ still doing great.

Also depends on the job, I am at a fine dining spot. But if you’re at like a diner or texas roadhouse, no matter how old you are, those heavy plates and trays will take a toll, especially if you are older.
[losmmc5] (score 1, diepte 3 OP) Yes it’s so true, I know if I lose like 5-10kg it’s gonna go easier, and I think it will happen naturally with the shift in patterns and activity etc (no more convenience snacking/binging at home from boredom). I’ve noticed before when I’ve lost a can a modest amount of weight, my hips don’t suffer anything like when I’m carrying some extra kilos.

I’m lucky I found a gig where the plates aren’t so heavy and the service is chill (it’s tapas, it all just comes out whenever). I reckon drop a few KG and I’ll be feeling better already.
[loskpzb] (score 1, diepte 2) Good I wish. Working on it, but I do have the ability to work 15 hour days without much problem at almost 40 years old. If you don’t stop moving, you can’t die. That’s my logic
[losn19w] (score 1, diepte 1 OP) Thank you!! Gonna get that out!
[lot2nvh] (score 1, diepte 0) Good shoes, Epsom salt soaks, stretches, foam rolling and a real treat once in a while is a massage
[lot2w73] (score 1, diepte 0) Good footwear is essential but insoles are a MUST! My cousins orthopedic husband recommended PowerStep insoles because they are rigid (apparently, any kind of flexible sole providers zero support. Think Dr Scholls) and give great arch support. You have to break them in, about 2 hours a day for a week or so, but after that, they are golden. Truly, I’ve replaced all the soles of my shoes with PowerStep insoles. It’s a game changer.
[lotbguc] (score 1, diepte 0) Birkenstock insoles saved my feet. Those and the extra ankle support from wearing Doc Martens boots.

Hot baths with Epsom salts are not only relaxing, but the hot water helps with pain. Better yet, if you have access to a hot tub, go for a soak whenever you can. Those jets feel SOOOO good on my feet and back. My city has a spa that offers hour long private hot tub rentals for like, $25 and I love to treat myself to one every once in a while. Hmm? Maybe I’ll go for a soak on one of my days off…

Also, elevate your feet whenever you can when you’re not on ‘em. I look goofy as fuck, but I’m always laying on the couch with my legs propped up on the back of it.
[loumx34] (score 1, diepte 0) good shoes go to a place like fleet feet that can tell you the best shoes for you and invest in an inversion table
[lov1lk3] (score 1, diepte 0) This is an issue with shoes. Get good ones and replace them often.
[loxr0jt] (score 1, diepte 1 OP) Amazing advice, TYSM for taking the time!!!
[lotpabu] (score 0, diepte 0) Lose weight

=== THREAD 1q1rmkw ===
SUBREDDIT: r/bartenders
DATUM: 2026-01-02  SCORE: 15  REACTIES: 59
TITEL: My feet are sabotaging my career, please help!!!
POST (source_id=post):
After 9 years of bartending and being on my feet every shift with no issues, my left foot’s decided to develop plantar fasciitis… I’ve got agonising pain in my inner arch/heel and it’s becoming unmanageable. I do have high arches and hyper mobile feet which doesn’t help.

I desperately need tips on shoes, insoles, stretches, or anything that actually works to stop this from becoming chronic because I want to keep bartending without destroying my body 🙏🏻🙏🏻

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nx7tjhj] (score 32, diepte 0) Alright time for a hard conversation: I fell at work in June and have been on medical leave for months after fracturing my foot in multiple places. Before this happened I was always struggling with foot and ankle pain. 

Now that I'm seeing doctors and being forced to deal with it, I have learned that the root of the vast majority of foot and ankle problems is tight calves! New research shows it accounts for nearly 90% of all issues. 

Stretch your calves every day for several minutes on each side. I also recommend calisthenics or yoga - something to improve your joint and tendon flexibility. 

Bartending can be absolutely brutal on your feet so if you plan on doing it long term please do what I didn't and start fixing the underlying issues before it's too late.
[nx7tsbp] (score 12, diepte 1 OP) Thank you. This is exactly what I was looking for. I do have incredibly tight hamstrings that then causes tight calves which is what I was wondering if that then travelles down to the plantar fascia- Nobody could actually answer that question for me and I didn’t wanna say anything just see if it was said / waiting for confirmation. You’re an absolute legend for this
[nx8c30g] (score 8, diepte 0) You need to go to a specialist and get advice. 

 It is probably worth getting inserts made specifically for your feet to minimize pain. You can do this at a podiatrist usually. Spend the money - it will be worth it. 

The various shows and inserts that are recommended here may well not be appropriate for your problem so professional help will hopefully save you money and pain in the long run
[nx7ud6r] (score 5, diepte 3 OP) I used to do ballet so I’ve got a full little set of cork balls and rollers at different sizes to stretch my feet and legs out and which I’ve gotten out of storage and started using again aswell as a frozen roller thing I stole off my mum from when her she had this issue hairdressing, also only wearing Birkenstocks around the house and not going barefoot which I’m hating so hoping to see a differences soon 🥲
[nx7rmkb] (score 4, diepte 0) Danskos. They will help you. Or just get some Ariat boots.
[nx7tywd] (score 4, diepte 2) The best stretch to start with is keeping your knee locked and placing the foot of the same leg up on a small platform - a curb or parking spot stop work great. Then just lean into it until you feel a stretch in the calf. Hold for 60 seconds and then repeat on the other side. Start with three reps of each. I also do it with a yoga block at home.
[nx8tdz4] (score 4, diepte 0) Visit a good feet store or similar and invest in a good pair of orthotics. It's really worth it and your feet and back will thank you
[nx7ugrq] (score 3, diepte 4) Good luck to you man! I'm still in the process of working my way back but it's gonna take a bit. Hope it helps.
[nx7sxoq] (score 2, diepte 2) San Antonio Shoemakers.
Hoka
 
That is for the shoe brands.

Aetrex insoles. Get the polyurethane ones with the bump in middle. 

 Do the streches.
[nx7tdsw] (score 2, diepte 2) Docs are heavy, I wear durable lightweight boots. 

If you search the sub and/or r/serverlife you'll find more posts about plantar fasciitis.
[nx7sjn3] (score 2, diepte 1 OP) Thanking youuuuu will be looking into these next pay 👀
[nxabz1s] (score 2, diepte 1) Seconding, I have sciatica and my Dansko clogs are the only shoes that have really helped
[nx7ujis] (score 2, diepte 5 OP) Good luck to you too!!! give it one day at a time you’ll be back before you know it, we’ve got this 🫡🫡
[nx8oqid] (score 2, diepte 4) I was going to suggest a ball under your foot, that's what helped me. I used a ball similar to a lacrosse ball (i picked up a 3-pack on Amazon of various sizes) and it legit cured me. I was dealing with this nonsense for over a year and once I rolled and stretched my calf DEEP, it went 95% away. Now I maintain. 

I also used the PF KT tape to get me through dance class and started using running insoles in regular shoes, all of them. My favorites are Currex brand, but almost any for running will work.
[nx80xj6] (score 2, diepte 6) That person sounds like a salesman, I have the same issues as you, also work in restaurants 10+ hours a day. dont listen to them about shots. Best thing to do is stretches like others have said, good shoes, and compression socks. also strengthening your ankles. It took a few weeks but now I basically have zero issues and can be on my feet all day again with no pain.
[nx83p96] (score 2, diepte 2) There's a huge variety of insoles. They might be third party applications, so not listed on for instance, the Timberland website, but they exist.
[nx83ppu] (score 2, diepte 0) What helped me the most (other than chucking my flip-flops and getting decent shoes) was rolling a hard ball all along the bottom of my feet in the morning before I started walking around. I used a rose quartz crystal ball just because that's what I had handy in the right size and the cool hard surface was very soothing, but any hard roughly baseball-sized ball will do.
[nx83xqk] (score 2, diepte 1 OP) I’ve been using a frozen roller w socks on each morning and night and it’s heavenly 🙏🏻🙏🏻
[nx84pfz] (score 2, diepte 2) The good news is that plantar fascitis isn't a permanent condition. After getting better shoes and doing the ball treatment for a week or so, mine cleared up completely and I've never had it show up since. It was absolutely miserable when I had it though, I could barely walk to my bedroom door in the morning my limp was so pronounced.
[nx84wo8] (score 2, diepte 3 OP) I’m glad it’s gotten better for you that gives me hope bc I’m about at that point lol I’ve been tip toeing/ hobbling everywhere to avoid that snapping pinch feeling 🥲
[nx911b0] (score 2, diepte 0) 1. Take care of yourself. Dont go cold to shift. Remember you are essentially doing mild aerobics for hours when it is busy so stretch, hydrate, and pace yourself as best possible. look up stretches' for splints/plantar.

2. I cannot understate the following: go to a good running store and get a gait analysis. Between plantar and shin splints I was dead and buried.  Discovered I pronate and have high arches. They put me in stability shoes (the inside of heel strikes first and straightens my ankles which balances my legs. Then the guy ripped out the manufactures insoles and put in Superfeet. Cost a shit ton more than what I was wearing but worth 5x the price. 

3. Running shoes are good for 500 miles, and while we are not running...we are hustling...stopping, turning, so when you find shoes that work well, buy 2 pairs and if you start to feel tired or achy legs/feet, put on the new pair and see if that helps. You will be surprised.
[nx97ru4] (score 2, diepte 0) Check out Fitville - there is an option on the sort for this type of condition. I brought some because of my neuropathy with the wide toe option and they are so comfortable.
[nx9d2fh] (score 2, diepte 0) If you can, go to a podiatrist. Mine suggested different shoes and insole. I got Brooks shoes and Dr Schol insoles. It helped, not 100% but a significant difference.
[nxdzli0] (score 2, diepte 0) Go to your local Fleet Feet if you have one. They’ll use two different devices to scan your feet and get you insoles that fit perfectly. I took my ex girlfriend for Xmas a few years back and she almost cried when she put properly fitted shoes on for the first time. I took my foreman’s daughter as well and her back pain disappeared. Well worth it.
[nxel7vd] (score 2, diepte 0) My boyfriend and I got a foot roller that massages your feet and works out kinks. We use it before bed after busy serving shifts and it cured his plantar fasciitis. 

His best advice is to stop walking so fast. We have a huge dining room so the urge to go fast is there, but between walking at a normal pace and the foot roller, he hasn't had problems in months. 

I'm also a big fan of Dr. Scholl's Workers Insoles. I put them in all my shoes and they're great for about 6 months or so.
[nxlt2v9] (score 2, diepte 1 OP) Yess I’ve been using these insoles for years now replacing them every 4-6 months!! But thank you for the advice I do rush around a fair bit so I’ll try to be mindful of that!!
[ny6c5hq] (score 2, diepte 0) Put a frozen water bottle  on the floor and roll your foot on top. I had this after working in landscaping and the cold and rolling motion was the one thing that helped.
[nx7qvw8] (score 1, diepte 0 OP) Mod note: Posting under Health/Wellness because this is about managing plantar fasciitis, preventing chronic injury, and advice on staying healthy while bartending Hope that’s okay & correct 😭🙏🏻
[nx7ra6m] (score 1, diepte 0) Shoes, insoles and socks. You need to upgrade yours. 

Ice, rest and stretching for relief.
[nx7rufr] (score 1, diepte 1 OP) I am aware and have been told this by my doctor. I and more hoping for people who have struggled with this issue and have first hand experience to be able to recommend orthopaedic brands of shoes as a very recent post on this sub talking about shoes. 80% of the comments are saying Doc Martens which is all I wear at work 😭
[nx7ukta] (score 1, diepte 6) I appreciate it
[nx9g48s] (score 1, diepte 5 OP) Yes, someone else in the thread has mentioned that running shoes and support based on high activity is the way to go so I will be looking into that thank uuuu!!!!!
[nx9ht0e] (score 1, diepte 6) You're welcome! Also, grab a foam roller and kneel on it to stretch the top of your ankles - sit back on your heels with the tops of your feet flat on the floor. It huuuuurts but it's definitely helped me as well. 

I found a YouTube video that has some shin roller suggestions that I've done before and it hurts even more than kneeling on the roller, but it truly does help if you stick with it. [Link](https://youtu.be/ENwJrIjGFcY?si=00TWkb_JgLkiSCXo)

Good luck!!
[nx939zj] (score 1, diepte 1) This is the answer, but I would like to expand it to include the importance of stretching the entire leg, as well as your back, feet, and ankles.

It is also a game changer to make sure you have wide enough shoes where you can wiggle your toes. People have mixed reviews, but Hokas are my only shoes that have never needed inserts.
[nx9w64a] (score 1, diepte 1) Im 46,started bartending at 20, about 7 years ago i started yoga because of knee/leg issues related to bartending. 
 Best decision i ever made. 
All the expensive shoes in the world dont equal what a few minutes of daily stretches do for the body.
[nx7vxsq] (score 1, diepte 0) Steroid shot.  Go to any "doc in a box" and tell them you are a full time bartender and describe your symptoms.  Ask for a steroid shot.  Almost immediate relief.  If it starts hurting again, go get another shot.  The visit cost me less than $200, shot included, with no insurance.
[nx7x42c] (score 1, diepte 1 OP) I’ve been offered quartzone shots or however it’s spelt for this but I’d rather only go down that route as a last resort 🫡
[nx7yhot] (score 1, diepte 3 OP) Respectfully, steroid injections aren’t a cure. they reduce inflammation and pain, but they don’t address the underlying cause. They help some people short-term, but they don’t work for everyone and recurrence is common (they didn’t help my mum long-term at all). There are evidence-based conservative treatments that can improve or resolve plantar fasciitis for many people (load management, footwear changes, targeted stretching/strengthening, orthotics, etc.). Saying it’s the “only solution” just isn’t accurate.
[nx82pd6] (score 1, diepte 7 OP) I genuinely appreciate the insight and I’m glad you found something conservative that worked for you!! Thank you for the reassurance that conservative methods do help 🫶🏻
[nxb4nw2] (score 1, diepte 2) > quartzone

cortisone

(not judging, just offering the answer to 'however it's spelt')
[nx7whtv] (score 1, diepte 0) Look to the footwear of other professions that stand for hours. Police and EMT boots like 5.11, or Timberland or approved shoes for US Post Office. They are available at uniform supply houses.
[nx82uyp] (score 1, diepte 1 OP) I am going to need to look into orthopaedic specialised shoes with high arch support, also hoping for light weight. I’ve had a look and there’s nothing specific about them being orthopaedic, do these come with any insoles or are they more supportive when it comes to impact absorption?
[nx83tmh] (score 1, diepte 3 OP) Alright I’ll go hunting thank you for the suggestion
[nx826or] (score 1, diepte 0) Kuru makes a solid non slip. Last year I could barely get up the stairs. Also recovery slides for home.
[nx8296m] (score 1, diepte 1 OP) Yesss I’ve been living in my birks on my days off but I will look into this brand thank you
[nx94e5o] (score 1, diepte 1) Be prepared for the cost though it’s over $1000
[nx974hi] (score 1, diepte 2) Maybe it's been a while but I got a good pair for around $300
[nx9aq3f] (score 1, diepte 3) I bought some at the good feet store over the summer, I opted for the cheapest plan and it came out to a little over 1300$
[nx9ggvv] (score 1, diepte 1 OP) Thank you I will ☺️
[nx9smo2] (score 1, diepte 0) I’ve dealt with plantar fasciitis a few times in my life. It’s is awful. The best course of treatment for me was:

Stretching my Achilles heel and calves a few times per day. 

Rolling my plantar on a frozen water bottle for a few minutes several times per day.  

More stretching of the calf and Achilles heel. 

Try that for a few weeks
[nxa77db] (score 1, diepte 0) I got one of those plantar fasciitis boots and slept in it.
[nxadop7] (score 1, diepte 0) I have plantar fasciitis and I wear Birkenstocks insoles in my shoes. They raise my arches and put less pressure on my heels. It’s been a life saver. They cost $50-60 but are totally worth it. I have 2 pairs. I teach, bartend, play upright bass and have two young boys so I am on my feet from the minute I wake up til I go to bed. Highly recommended. If you get them on Amazon, you can return them if they don’t work for you but arch support is the key.
[nxagne4] (score 1, diepte 0) are you me? I bought a snailex foot massager & use it after every shift & it's a game changer, I wear the hoka bondi in non slip, inside those I use the powerstep insoles and now I've just added in copper compression socks.  Now I can walk anywhere and work all these additions you can too
[nxb5esf] (score 1, diepte 0) Adidas ultra boost are pretty good for the feet.  There’s also some shoe brand that starts with an H
[nxb5f6a] (score 1, diepte 0) This isn't specific to plantar fasciitis (mentioned in other replies: calf stretches, time off your feet, etc) and it's mostly a copy-paste from a similar post this week, but... for footwear:

[Birkenstock Profi-Birki clogs.](https://www.birkenstock.com/us/profi-birki-polyurethane/profibirki-core-polyurethane-0-pu-u_3866.html)

I wear large shoes, and a lot of the others suggested aren't available in my size.  I started wearing these in the kitchen and I've been wearing a pair of these for at least the last twenty-five years.  I usually get a year and a half of constant use out of a pair, but recently I've been keeping my current pair at work and only using them there and they're barely worn after that same amount of time.

Get clogs.  Change into them at work.  Put the cloth bags with cedar chips in them (I'm sure they have a name I'm not remembering) in your street shoes while you work.  Reverse at end of shift.

I just had vein surgery for 'chronic venous insufficiency' and so I'll add another suggestion: start wearing compression socks.  You don't need the tight-tight ones, if you need to dip your toes into it then Walmart has Dr Scholl's compression socks that are worth a try before you commit.



So: stretch.  Address inflammation (NSAIDs in moderation).  Better shoes.  Maybe insoles or orthotics.  Consider compression socks while you're at it.
[nxb68wb] (score 1, diepte 0) I had this for awhile. My wife still has ongoing struggles. I left the industry and I’m good. But she still has to be proactive as she is only working more now. I have a bit of insight. I was able to get rid of mine using dr scholls plantar fasciitis inserts. She had to get specialized shoes to deal with the issue. There are flip flops that will relieve the pain to wear when you’re at home. You can buy them on Amazon. They Work really well. It’ll hurt most in the mornings. There is a brace that you can wear while you’re sleeping. I can’t recommend that enough. There are also exercises you can do. Stretches. Freeze a 16 oz bottle of water and run your foot over it when you’re home. Or get a little massaging ball that you freeze to work around the heel. It’ll take time but it will get better IF you actively treat it. Unfortunately all of these things will have to be done collectively to get back to normal. Good luck. I know how much it sucks.
[nxcqnaq] (score 1, diepte 0) Hoka started making non-slips. They're expensive as fuck but I 100% believe I wouldn't be able to bartend anymore if I tried to wear other shoes (been bartending for 22ish years. Developed some pretty gnarly foot problems along the way.)
[nxebelt] (score 1, diepte 0) Find an acupuncturist who's willing to put pins directly into your feet. I do it as needed, sometimes it only lasts me 3 months and others up to 6. It's been a total game changer for me
[nxlt5zz] (score 1, diepte 1 OP) Do you need to rest at all afterwards? I need to be able to work 60hr weeks I can’t afford time off at all
[o2uni4k] (score 1, diepte 2) Just for a couple hours afterwards at most, it sometimes makes you sleepy in a relaxing way
[o4h4706] (score 1, diepte 0) I had really bad plantar fasciitis several years ago. I went to a podiatrist and they gave me shots in my feet, so painful but helped. You can’t do them often bc they’ll tear the tendon if you do. I would go and they would put ice boot things on them, use ultrasound therapy, and tape up my feet. I can’t remember the frequency tho. They also gave me a splint and exercises to do. 

I later worked at a podiatrist and we only offered the shot, splints, and taping, along with exercise handouts. We also did surgery if needed. Also, you want a podiatrist that can inject in multiple points for max effect. 

If you don’t have insurance or money to pay for a podiatrist you can order splints and tape online and watch YouTube videos for instructions. Rolling a frozen water bottle or a firm tennis size ball. There’s also metal foot massage things that you can roll your foot over, they feel good bc they are cold. 

Foot massages can help and also looking into scraping. Sorry it’s so long and I’m late to the party, but these are things that have helped me.
[oo8l1fc] (score 1, diepte 0) Bartending absolutely wrecked my feet when my plantar fasciitis got bad. Good shoes helped some, but compression socks made a bigger difference than I expected, especially during long shifts. I’ve liked apolla because they actually feel supportive around the arch without being uncomfortable halfway through the night. I’d also start stretching your calves consistently because mine turned out to be way tighter than I realized
(3 reacties met lagere score weggelaten)

=== THREAD 1j5kb7a ===
SUBREDDIT: r/bartenders
DATUM: 2025-03-07  SCORE: 11  REACTIES: 59
TITEL: What are your fave shoes for working??
POST (source_id=post):
Most of the shoes I own are goth shit that are cool to wear for like an hour at a function and then I go home. Most of my jobs in the past weren't very physical, or when I was a club dancer I just wore platform heels cuz duh. I've been wearing a pair of converse and they're pretty good but after the longer shifts my feet do start to hurt, I'm mostly concerned about longterm health and developing pain in my feet or lower back. What shoes do yall like to wear for 6-7 hour shifts? 🤔

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mghmj8l] (score 18, diepte 0) Blundstones. Tough, comfortable, stylish, waterproof, and virtually no break-in period.
[mghl4ub] (score 17, diepte 0) Hoka one ones.
[mghlsqt] (score 14, diepte 0) Funnily enough i asked this exact question here a couple years ago and bought the pair of sketcher that was recommended to me. They've held up pretty well but I need to replaced the insoles. Just worked a 15 hour day today and my feet are sore but it's nothing crazy.
[mghqgqd] (score 10, diepte 0) Asics Gel Nimbus 25

These things are worth their weight in gold.
[mgi4537] (score 9, diepte 0) Birkenstocks is my preference but god are they ugly lol.
[mgmp7qt] (score 8, diepte 1) Man.  That is an ugly ass pair of shoes.
[mgjiush] (score 8, diepte 0) I’m a bigger guy and I couldn’t find shoes that were slo resistant and would hold up for more than 6 months. For the last couple years I’ve worked in the same redwing boots and I haven’t even had to have them resoled yet. They are incredibly slip resistant, even in oil, and I’ve got solid ankle support. I get new insoles on auto order every 6 months and swap them when they come in.
[mgi3m0m] (score 7, diepte 1) Yeah. I've been on the Skechers bandwagon for almost ten years. Buy a new pair every fall. New insoles winter and summer. Love them.
[mgi55yd] (score 7, diepte 0) I've tried so many different shoes and I've hated most of them. I've always liked sketchers, they're pretty inexpensive so they don't last very long. I recently purchased a pair of Hoka's and it it the best decision I've ever made!! I've even got a couple of my fellow bartenders at work wearing them now
[mgibb7z] (score 7, diepte 0) Skechers has a line of work shoes, they’re non slip and comfortable
[mgk7ein] (score 5, diepte 1) *whispers* they make insoles…and they’re magnificent.
[mghzffd] (score 4, diepte 1) This is what I wear. They were top three in Runners World alongside Hokas and they came in black when Hokas didn’t. I hate how clown shoe-y they are but I’ve been on my feet for 20 years wearing “cute shoes” and I’m paying for it.
[mgilrmb] (score 4, diepte 0) Skechers, for sure, the work ones with the nonslip. Easy to clean, comfortable, and you usually just have to replace the insoles. Only downside is they’re like this cloth ish material so if you spill something on your feet your gonna get soaked but they dry fast
[mgkckxm] (score 3, diepte 1) Are they slip safe? I do love the aesthetic.
[mgmowzc] (score 3, diepte 2) Not all of them, but they make several styles with Vibram nonslip soles.
[mgjx43r] (score 3, diepte 0) Paladiums boots are cozy and have great traction. My most recent pair is waterproof too. Swear by em.
[mgn8tq1] (score 3, diepte 0) Doc martens. They get the job done and with insoles dont hurt my feet as bad as kitchen crocs did
[mgpuzcc] (score 2, diepte 1) Agreed.  The Hoka shoes I have aren't that pretty, but I'm old and my feet aren't killing me.
[mgmx4ky] (score 2, diepte 2) Not really but they look good 😅
[mgiwqf5] (score 2, diepte 0) I like to wear my all black converse for my dayshift day, ASICS for my double shift day
[mgj9b0z] (score 2, diepte 0) Asics, just be getting the non slip sticker on the bottom
[mgjpoz6] (score 2, diepte 0) Finally got Hokas and they definitely work great.
[mgoxxqe] (score 1, diepte 1) I bought some Skechers for work no slips and they're actually pretty great.
[mgpm3p0] (score 1, diepte 1) I bought the pair that look like regular sneakers, kinda like Keds but they're Birk. Theyre cute and go with anything! Definitely expensive but if you have wide feet like I do, you'll pay any price for a properly roomy toe box
[mgim1ai] (score 1, diepte 0) Easy works are my favorites! I learned about them from nurses and have sworn by them since.
[mgioixg] (score 1, diepte 0) Custom converse Chuck Tylors. 10 hour shifts.
[mgmqjmg] (score 1, diepte 1) Do they hold up well? I feel like I wanna get a pair of these more than usual runner style shoes
[mgnlm1j] (score 1, diepte 3) Honestly that’s good enough reason for me haha
[mgj5nbx] (score 1, diepte 0) Adidas Terrex, Free Hiker 2.0 (I got the high top version) Were I work, sink always leaks (it’s also a sink were I have to pedal for the water) so these work just fine. however just like with any waterproof shoe, they’re not all that breathable.
[mgj8d9v] (score 1, diepte 0) On Cloud!!! My feet haven't felt this good in years
[mgj96ym] (score 1, diepte 0) I wear low doc martens with aetrex insoles in them. My feet/back never hurt. Everybody I have get those insoles loves them.
[mgjjdyw] (score 1, diepte 0) i wear the mise chelsea boots and my feet and back have never felt better. only downside is the non slip could def be better from shoes made by chefs.
[mgjojh4] (score 1, diepte 0) Salomon’s
[mgjpjec] (score 1, diepte 0) I was gifted a pair of Snibbs about 6 months ago and they are pretty great. They look a little silly but my only real complaint is that they are a little snug on my wide ass feet. They are just fine on a shorter shift but tomorrow night (might push 15 hours) I’ll be wearing my brooks running shoes. The snibbs I mostly use for catering/event gigs now. The brooks are about a month old and so far they are about on par with my old hokas, which were great but last about as long as a shoe a third of their price.
[mgk1kq2] (score 1, diepte 0) Red wing iron rangers. Tough to break in but water proof and I can go for days in em now
[mgk1qh7] (score 1, diepte 0) I bought hokas because of recommendations on here, wore them for 2 days and my back went out. Tried them again when my back was recovered, and they put my back into spasm again. Someone online said they are too bouncy/springy for someone with a bad back like me. They felt amazing on my knees for the time I wore them though, so it's a bummer. I have been wearing Nikes for years otherwise.
[mgk569v] (score 1, diepte 0) Wore a lot of black trainers and shoes over the years.
But Vans are genuinely the comfiest I’ve ever had.
Followed by Adidas Gazelle’s
[mgk86my] (score 1, diepte 0) Thursday boots black side zip
[mgk8jny] (score 1, diepte 0) Asics or Hokas
[mgkat6t] (score 1, diepte 0) Army boots.  Great for kicked a keg that doesnt wanna go in the fridge, they as not slippery, if glass breaks it doesnt get in your shoe because they are high. Great perk, it also helps to scare people off.
[mgkcnt0] (score 1, diepte 0) Redback boots. Or any good work Chelsea
[mgkhrpv] (score 1, diepte 0) I have to wear all black, non slip shoes, with no logo showing, my options are limited.

If I didn’t, I’d be wearing On Clouds, Hokas, or New Balance with the Fresh Foam.
[mgkjkpl] (score 1, diepte 0) Birkenstock Q0500 in black.
[These.](https://www.birkenstock.com/us/qo-500-natural-leather/qo500-professional-naturalleather-0-rubber-u_3974.html)
I have them and my feet don't hurt after long shifts anymore. Totally worth the cost imo.
[mgkjwzq] (score 1, diepte 0) I wear Nike p6000 and new balance Arishi for service
[mgktgfj] (score 1, diepte 0) Air maxs !!
[mgl3s7p] (score 1, diepte 0) Brooks!!!! They have relieved my foot pain and helped my back pain. I've had two spinal surgeries AND  a foot surgery. I suggest Brooks! 👍🏼👍🏼👍🏼
[mgl7niw] (score 1, diepte 0) I tend to lash out for when I want something proper that'll last me years with or without proper care. These lasted me about four years on 60 hour weeks despite not taking proper care of them.

https://military.eu/en/p/garmont/garmont-t8-fg-nfs-gtx-regular-tactical-boots-black-2393092?utm_source=google&utm_medium=cpc&utm_campaign=%5BGB-PMAX-MILITARY%5D+Obuwie&gad_source=1&gclid=CjwKCAiAn9a9BhBtEiwAbKg6fjFw4BymdjSX6-OhdohQrMfYqe3XOM3aCMR-MvgC6IbkmKM2g3mtGBoC9OgQAvD_BwE
[mglwvko] (score 1, diepte 0) Vessi.  Breathable and waterproof.  Can swap soles if you need different support.  Downside, not slip proof
[mgm4yp1] (score 1, diepte 0) newrocks they’re like a big platform sponge with great grip if not i like my cowboy boots it took a bit of practice but i can turn on the heel and spin which is handy when getting stuff from the backbar
[mgmr720] (score 1, diepte 0) i wear black af1s 🤣
[mgmsoux] (score 1, diepte 0) Hoka Bondi SR!!! Waterproof so when shit is dripping and wet your feet don’t get wet. Slip resistant and the cushioning is amazing. My back stopped hurting once I started wearing these. 20 years of bartending and these have been the best I’ve worn yet.
[mgn6pxm] (score 1, diepte 0) I wear ultraboost Nikes
[mgnfl5f] (score 1, diepte 0) Teva sandals for now...
[mgngjb7] (score 1, diepte 0) mozo lace up flats on shoes for crews and amazon. didng need any breaking in and overall havent had any kind of issue. also theyre cute.
[mgnvqv3] (score 1, diepte 0) Red Wings blacksmiths.   Only shoes that have ever had my feet never hurt.
[mgnw2q7] (score 1, diepte 0) I’ve been wearing popcush vans basically the whole summer, unbelievably comfortable and holding up surprisingly well. My last pair I had for 3 years and I expect these will have a similar lifespan. when it cools down I’ll switch back to either my redbacks or docs.  Redbacks have a wonderful insole.
[mgol9ux] (score 1, diepte 0) Been rocking the converse since day one over here. Never had an issue even working 16 hour doubles
[mgqc444] (score 1, diepte 0) i wear docs with a super thick sole. i think they’re ‘airwaire’ or something, the name inside has worn off. but they’re super comfy and i can step on any broken glass behind the bar no issues
[mgqk9ze] (score 1, diepte 0) I have a couple different pairs of ASICS that I rotate
[mgs8mcu] (score 1, diepte 0) I'm rocking the Condor 2s from ShoesForCrews.

  
Really thick cushioned sole helps with the fatigues of being on your feet all day and I've found that theyre basically completely nonslip.

Honestly wouldn't go back to wearing anything else, I tell all my team looking to get new shoes to check them out. 

The adage of if it touches the floor don't go cheap really applies when you're on your feet all day,
[mgtc2de] (score 1, diepte 0) I like tread safe shoes from Walmart.  They're cheap and easy to clean sticky gunk off.  I'm the type of bartender that makes a complete mess and gets everything sticky so I clean my shoes every other day.
[mgth7if] (score 1, diepte 0) New Balance 993. If it ain’t broke 🤷🏻‍♂️
[mhbtejc] (score 1, diepte 0) The work Crocs are ugly as sin but haven't let up and cost me $30 on sale. I hate them. They're so ugly. So comfortable though. My legs stopped hurting after years of docs and other stylish brands. Have never slipped. I suspect I could hopscotch down some stairs after spilling a mop bucket safely. My feet don't hurt anymore after long shifts and trust it's the same job, just different shoes for a while now. They are objectively so ugly but hey no one ever tipped me cause my shoes looked cool before anyway.
[mhi07h7] (score 1, diepte 0) sketchers canvas slip on. they’re non slip and last so long. get insoles for more comfort, but they’re great!! I’ve worn them for the past 4 years of 8-12 hr bartending shifts
[mhkaxko] (score 1, diepte 0) I go between my Hokas and Danskos, occasionally Crocs. Whatever shoes I wear, Stryda shoe insoles has been a life saver for me.
[moy5eo9] (score 1, diepte 0) Thorogoods will do you good, but really anything with a steel/composite toe will help, particularly if you work in places with a more aggressive crowd.

I've put multiple 12+ hour shifts in a row in them.

=== THREAD 15tn65u ===
SUBREDDIT: r/Costco
DATUM: 2023-08-17  SCORE: 26  REACTIES: 59
TITEL: Employees of Costco: what shoes do you wear?
POST (source_id=post):
I'm not employed by Costco directly, but a large portion of my job requires running/walking around them for hours on end. My feet do not like this and I'd like to be kinder to them. What shoes do you recommend for dealing with miles of unforgiving concrete?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jwkoik9] (score 54, diepte 0) Hokas Bondi 8. Love them.
[jwktxr0] (score 19, diepte 0) Brooks
[jwlgpkd] (score 19, diepte 0) Get fitted at a running store. Even the best shoes will be bad if they're the wrong fit for you. Source: 80 lifetimes in the service industry.
[jwku7d0] (score 15, diepte 0) Not a Costco employee, but I've had jobs on my feet all day. I recommend looking up some physical therapy stretches and exercises for the back, legs, and feet in addition to getting good shoes to help reduce the strain and discomfort.

Personally, Merrills never did me wrong but if you have a local place that does fittings nearby, that's a good option to learn what works best for your feet.
[jwkpg8d] (score 14, diepte 0) Altra paradigm and brooks adrenaline have been consistent go-tos.
[jwkuhpa] (score 13, diepte 1) Same. But it’s more important to get fitted properly at a legitimate running store and then try on various shoes in that size. Also I use superfeet insoles.
[jwkvgai] (score 13, diepte 2) Not a Costco employee but recently bought my first pair of Hokas after husband raved about his.  

Wore them on a crazy trip walking all over Chicago, DC and Boston last month. 

Done. 

Finito. 

I’m a convert.
[jwkx198] (score 11, diepte 0) Adidas ultraboosts are my go to for being on my feet. Anything with the boost sole will feel like you are walking on clouds all day
[jwkye1h] (score 8, diepte 0) Hoka Bondis and Gaviotas I ride and die for the Hoka gang
[jwm6rdr] (score 7, diepte 1) Brooks and Hokas are by far the most comfortable shoes I've ever owned. Definitely worth the money.
[jwlbjd3] (score 7, diepte 1) Can confirm. I’m a Costco employee and I probably have a dozen Ultraboosts in various colors. My feet never hurt even after walking 20k+ steps in a shift.
[jwksd80] (score 6, diepte 0) I've got a pair of black Hoka Bondi SR. Hoka is the answer! Nurses love them too. For those interested, they run about $175. If you find them for much less (like $80) you are looking at a scam website.
[jwlk5ez] (score 6, diepte 0) Hokas are popular. Im more of a boot person myself. I use keens when i dont need safety toe shoes. 
Specifically the soft toe san jose. 
The cost is decent, they last quite a while, toe box is wide, and theyre a good amount of cusion in them
[jwmsctl] (score 5, diepte 2) Same. Brooks Ghosts are my go to for comfort. I live hokas for jogging but just look goofy with most clothes
[jwkwv6k] (score 5, diepte 0) I use Aetrex insoles. Insoles imo make the biggest difference. Granted maybe cuz I kinda have flat feet. Elevates any shoe though.
[jwm2pdy] (score 5, diepte 1) If you like max-cushioning you might also be interested in Altra brand shoes.  I wear Altra Paradigms with max cushioning and wide toebox and love them.
[jwm2uza] (score 4, diepte 1) Are you me? I'm Altra Paradigm all day but I do own a pair of Brooks Adrenaline.
[jwliifc] (score 4, diepte 1) Brooks Glycerin are the most cushioned
[jwl2ht6] (score 4, diepte 0) Most people wear Hokas or Brooks, or some other sort of super cushioned walking shoes. I personally currently wear Puma Defys, and in the winter, slip-resistant Dr Martens with arch support insoles.
[jwla6py] (score 4, diepte 0) Alegria...they are dressier than tennis shoes. Basically teachers wear them! Replaceable and washable cork insoles, non slip bottoms, etc.
[jwlckhf] (score 4, diepte 0) I wear the Brooks Trace 2 working for Amazon delivery. I'm on my feet 10 hours a day on asphalt, concrete, gravel. Definitely a great walking shoe
[jwmxr3j] (score 4, diepte 0) Not a Costco employee, but a healthcare worker who worked with a podiatrist matching common brand shoes for people.

For the Costco life (long hours on your feet, concrete floors, lots of walking): great cushioning and support, especially if you pronate or supinate. A lot of folks are pronaters!

Hoka, Brooks, and Merril usually have wider size offerings which many people find comfy. Odd add that On Cloud is nice, Keen can be great, etc. Overall, get some insoles rated for standing too. Highly recommend checking out hiking boot insoles as they’re made for walking long hours on rocky terrain. And most people don’t do this, but change your insoles every 6 months. It’ll feel like a new pair of shoes! 👍🏽👍🏽
[jwm4ngc] (score 3, diepte 1) Hoka Rincon 3 here. Only shoe that doesn't activate my plantar fascitis
[jwm45on] (score 3, diepte 3) Nice.  I wore the outsoles and heels off my recent two pairs of Paradigm 2.0 from walking/hiking and finally bought a few pairs of 6.0  to replace them and really like them.  Altra is clearing-out the 6.0 since the 7.0 just came out so you can get good deals on them.  I got 50% off em during Memorial Day a few months ago so perhaps they'll have a Labor Day sale or something soon.
[jwlazxi] (score 3, diepte 0) SAS (San Antonio Shoes)

Not a Costco employee but a lot of folks in healthcare and airlines industry wear these. They’re handmade by some great folks in San Antonio.
[jwllt75] (score 3, diepte 1) Consider ArchCrafter custom shoe inserts. No need to visit a podiatrist.
[jwm2f3r] (score 3, diepte 0) Not a Costco employee but as a nurse, Hoka all the way. I do agree with others saying get fitted/try them on first though if possible.
[jwn1m0m] (score 3, diepte 0) Invest in some compression socks. Thank me later
[jwljhok] (score 2, diepte 1) Yes I love these shoots it’s the only ones I can tolerate standing all day in
[jwkxqwx] (score 2, diepte 0) I have flat feet too so you might be onto something
[jwl13zl] (score 2, diepte 0) Not a Costco employee but was a bedside nurse for several years. Recommend Hokas or Brooks. Good luck!
[jwlsvcp] (score 2, diepte 0) Before ''blind'' buying from the recommendations, I highly highly suggest you to go in-store to try it yourself. I almost bought a 200$ pair of running shoes that everybody raved about it everywhere and when I went to try it in person, it definitely wasn't for me (too narrow in the middle part, I have wide feet). Where I am from, we have a running shoe store called the running room, which is far better than your big chain sports gear stores
[jwlvf73] (score 2, diepte 0) Our PT recommended Hokas to me, and they're incredible.  So supportive and my feet never hurt.  Another coworker recommended Brooks and I tried them out but they weren't nearly as good as the Hokas.
[jwm9ff2] (score 2, diepte 0) Adidas Ultraboost and Merrell Moab 2
[jwmjpbp] (score 2, diepte 0) When I was in the warehouse I wore either Keen waterproof shoes or if I knew I would be outside I wore my Hoka's. Buying a quality shoe in the warehouse is just about the best way to spend your money imo.
[jwms17d] (score 2, diepte 0) Brooks Ghosts are the most comfortable shoe I've ever wore. The hokas are nice but look funny.
[jwmwsao] (score 2, diepte 0) On clouds!
[jwnm8o3] (score 2, diepte 0) Timberland PRO Men's Drivetrain Mid Composite Safety Toe 

PowerStep Insoles, Memory Foam, Heel and Arch Pain Relief Insole

&#x200B;

these two combinations have worked incredibly well for me.
[jwkkuly] (score 1, diepte 0) Posts that don't follow r/Costco subreddit rules may be subject to removal. 

When applicable, please make sure that you're using a descriptive post title with product name(s) mentioned as it yields better subreddit search results. Thank you.


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Costco) if you have any questions or concerns.*
[jwnrd9d] (score 1, diepte 1) Yes!!!!!
[jwm30to] (score 1, diepte 2) I've been through five pairs of paradigms. I had a pair of 4s that I out over 3000 miles into before they were a little too worn out to keep wearing at work.
[jwl1udc] (score 1, diepte 0) Don’t forget compression socks! On my last trip to Europe, these were a game changer.
[jwphfm5] (score 1, diepte 2) We talking fashion or comfort and support?
[jwlj2mi] (score 1, diepte 0) Get a pair of orthotics
[jwljy7l] (score 1, diepte 0) Nike React SFB Carbon‘s 

They’re an outdoor shoe but my feet and joints just love them to much
[jwlxkkh] (score 1, diepte 0) Currently wolverine boots but I prefer a wedge sole and the boot to be as light as possible.
[jwml4cg] (score 1, diepte 0) beach sandals
[jwmpgeq] (score 1, diepte 0) Hoka Bondi 8 SR. Happy feet!
[jwn0a9e] (score 1, diepte 0) Rei hiking boots
[jwnlovd] (score 1, diepte 0) Hoka hands down the best. Go to a running store and get fitted what style works for one may not work for you.
[jwo3cl3] (score 1, diepte 0) Getting a good pair of shoes is one thing but you also need to let the cushion replenish itself, for lack of a better term. Get like 3 pairs and wear them so you don’t wear any one pair consecutively. Makes them all last a bit longer.
[jwo715s] (score 1, diepte 0) Timberland Boots. I walk around 7/8 miles a day at work. Always comfortable
[jwod0pw] (score 1, diepte 0) HOKA Bondi SR.  You won’t regret it.
[jwos6kx] (score 1, diepte 0) Altras if you have wide toes
[jwott4d] (score 1, diepte 0) I went to a foot doctor and received customer orthotics they make a world of difference.
[jwp9w2v] (score 1, diepte 0) Hokas
[jwqelgi] (score 1, diepte 0) Toss in a pair of Active Thick footbeds from yoursole.com into a good pair of shoes and thank me later.
[jwqn3yk] (score 1, diepte 0) A pair of non-slips by Sketchers that I ought to replace.
[k0fm9lo] (score 1, diepte 0) Boots are good for me but living in the Bay Area I just get whatever shoes I can get
[jwoln6u] (score 0, diepte 1) I think anyone wearing these had to have stolen them from an elderly patient...geez! No...

