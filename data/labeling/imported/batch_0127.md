# Label-batch batch_0127

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
Schrijf het resultaat naar `batch_0127.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1wifaij, 1nb2gqf, 165yi7j).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1wifaij ===
SUBREDDIT: r/Mommit
DATUM: 2026-09-17  SCORE: 337  REACTIES: 68
TITEL: The Dreaded Hand, Foot, and Mouth Disease: Remedies, ranked
POST (source_id=post):
The devil’s disease, aka Hand Foot and Mouth (or HFMD if you’re nasty) came roaring through my house this last week. I read many old Reddit posts about this evil virus and felt less alone. 

I caught HFMD, as well as my 15mo, and it sucked. I had sores on my hands and feet and one elbow (wtf), a 103° fever, sore throat, an outrageous headache, body aches, diarrhea, nausea, chills. I felt like death warmed over.

I offer my contribution to HFMD crowdsourced literature with my definitive list of remedies and what helps the most. 

For adults: 

Tylenol: 7/10: wears off quickly, sorta helps with pain, didn’t really drop fever fast 

Advil: 9/10 worked longer, brought fever down faster, attacked the chills and body aches.

Honey lemon tea: 7/10 made sore throat more bearable and it’s a liquid 

Witch hazel: 12/10: removed the itch and the soreness, and also it worked some witchy magic on the sores themselves and actually healed them, and prevented some sores from turning into blisters (they were heading that direction and the witch hazel flattened them out, made the sore go away). If you ever have to deal with HFMD, get yourself some of this magical liquid immediately. It’s in the beauty aisle, some people use it as a facial toner.

Rx hydrocortisone cream: 7/10, helped control the itch, but the feeling of the cream was sticky and would make me itch when it wore off

Calamine lotion: 6/10, soothing, feels calming, but didn’t take away itchiness 

OTC Benadryl cream: 9/10 removed a lot of the soreness and pain in my feet, no weird texture 

Cortisone 10: 8/10 helped with itch temporarily

For the toddler:  
Salt baths: 9/10 it dried out his sores really quickly and he loved playing for an hour in the bath 

Calamine: 9/10 my toddler requested we put this on. It apparently helped him a lot. 

Rx Hydrocortisone cream: 8/10 we noticed he was less uncomfortable at night with this 

Extra strength butt paste: 8/10, toddler had sores in his diaper area, does take itch away (yes, I had to use butt paste once on myself), and protects the skin. Toddler also requested we put this on. 

(For the record, requested=pointing and yelling incoherently at the object until we use it on him and then he’s instantly happy) 

I discovered Witch Hazel after he was pretty much done with the sores, so if we ever get this again, witch hazel will be my go-to from day 1. 

Best of luck out there, and buy yourself some witch hazel!!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[paa2r58] (score 61, diepte 0) What a great post! What a good Mom! Thank you. (Witch hazel does rock)
[paa66c4] (score 39, diepte 0) The worst I have ever felt and I didn’t have it “that” bad.
[paa7uu1] (score 39, diepte 1 OP) “Adults don’t get HFMD” is one of the biggest crocks of shit we tell moms, next to “breastfeeding makes you lose weight” and “putting babies to bed drowsy but awake will help them learn to sleep!” 

In the words of Dwight Schrute: FALSE.
[paa6vsa] (score 18, diepte 0) Thank you so much for this! I got it from my daughter when she was a toddler (she’s 11 now) all I ever read was “adults rarely get it, and if they do, it’s very mild” and it was one of the worst illnesses I’ve ever had in my life!! I rank it second after norovirus lol.
[paa53e2] (score 17, diepte 0) Doing the Lord’s work here with this post! We had it a few months back— totally awful. For my baby (15 mo old at the time), covering her sore-covered hands with calamine then socks was helpful.
[paa82nb] (score 11, diepte 1 OP) Same! I will take explosive diarrhea and even crapping my pants over this hell.
[paadp6b] (score 11, diepte 1 OP) The variation in how this strikes people is wild on the level of COVID. My daughter was patient zero and we had no idea because she just had a fever and sore throat. Standard kid stuff. My husband had a slight fever for 12 hours. My son looked like a leper who also dabbles in meth addiction.
[paabse2] (score 10, diepte 0) « For the record, requested=pointing and yelling incoherently at the object until we use it on him and then he’s instantly happy » this sent me because I was thinking wow your toddler seems to know the words for lots of complicated things/meds but then I laughed out loud because that’s exactly what mine would do too
[paa4nvu] (score 8, diepte 0) Oh this is excellent. I’ve heard of this devils disease and everyone I know who’s had it said they were miserable. This is great work; Thank you for sharing and taking the time to post.
[paaacuc] (score 8, diepte 0) I wish I would’ve known about the witch hazel a couple months ago when the disease came through my house! I agree ibuprofen helped better than acetaminophen. 

I’d like to add a warning that your sores will blister and peel after you start feeling better. The sores on my hands peeled a couple of weeks after I was feeling better but the sores on my feet have only just started peeling now 2 months later. I guess I should count my blessings that I haven’t lost any nails because apparently that can happen
[paacpyr] (score 8, diepte 0) My kid had no sores and a sore throat. My husband was bed bound for 8 days, couldn’t walk or do anything. Over a year later and his toenails are still cracked and peeling. It’s nuts.
[paagq8s] (score 7, diepte 2) Omg I gained more weight breastfeeding than in pregnancy. Actually I was 10 pounds lighter after I gave birth than when I got pregnant. I lost a whole 40 pounds a week after birth. There was a lot of swelling. I hate this myth. Sure you burn more calories but it's such a hard time.
[paap47z] (score 7, diepte 3 OP) You burn calories, sure, but you’re hungry ALL THE TIME too! I couldn’t lose weight if I tried. I snacked constantly.

Well here’s a nifty solution—Just get HFMD after you wean and you’ll lose your appetite and thus lose some of your breastfeeding weight too! Ask me how I know. 😉😅
[paa9tso] (score 7, diepte 1) Popsicles! We had HFM a couple months ago and me and all 3 kids felt better with popsicles. My mom also used to be an ER nurse and they used to give kids popsicles made from pedialite if they were dehydrated. I just used watered down juice and yogurt drinks but my kids were drinking plenty of water still
[paabyq5] (score 6, diepte 2) Our pediatrician suggested an OTC mix of 1:1 Benadryl and maalox and it works pretty good for our son!
[paa8f9e] (score 5, diepte 0) The villager we all need. Thank you for this 🩷
[paa8gkb] (score 5, diepte 0) Any remedies for the mouth sores?? My kid’s were so bad that he couldn’t eat or drink anything. He got dehydrated and we had to be admitted to the hospital for overnight fluids.
[paa9pms] (score 5, diepte 0) Just wanted to chime in and agree that I got it as an adult when my youngest was 18 months or so and it was HORRIFIC. Everything felt like it was on fire and hurt. 

And fwiw, I went to my dermatologist not long after for a regular skin check and he told me not to worry, my nails might look weird for 6 or so months. At which point I noticed how they’d peeled and broken off and looked weird (hadn’t noticed)… but apparently this is normal (especially if you had a non-mild case). And my did go back to normal (they were terrible to start with though). But it did get better. ❤️‍🩹
[pabc2dj] (score 4, diepte 2) I did this on my feet and took like half my foots worth of skin off. The skin underneath was not ready and it hurt to walk for a couple weeks after. Proceed with caution.
[paapj5k] (score 4, diepte 0) Amazing list!! I dread the day this gets to us. 

As a side note,  I don't remember hfmd being a think when I was a kid in the late 80s/ early 90s ) in the uk, if that makes a difference) - is or more prevalent than it used to be? More prevalent in the US? Neither... ? But if neither,  then why did I constantly hear from my parents about when we had chicken pox but never hfmd?
[paa4dag] (score 3, diepte 0) Helpful af
[paau3yl] (score 3, diepte 2) Lots of different coxsackieviruses that present differently
[pachy0g] (score 3, diepte 2) Adult presentation is a worse illness overall. Kids get blustery with short fever; some don’t get fever. Adults get brutal sore throat exhaustion fever sores etc. rough stuff.
[paab2wf] (score 3, diepte 1 OP) My kid didn’t have mouth sores that bad, he still would take some water. I gave him cold water. Other folks on here have suggested Magic Mouthwash as prescribed by a doc or a DIY version with OTC ingredients. (Check with your doc if it’s for a  young kid).
[paakubi] (score 3, diepte 1) My daughter had the sores mostly inside her mouth and throat and could not swallow, she would cry all night long for days! It was awful I’m following this up with what helped for mouth sores was making a DIY magic mouthwash. 1 part maalox and 1 part liquid childrens diphenhydramine. We would dip a cotton swab in the mixture and just dab it on her sores, we discovered this a few nights into the screaming and it worked so well!!
[paaalhh] (score 3, diepte 1 OP) Thanks to other Reddit posts , I’m on the lookout for my nails falling off. 😂  And my skin peeling like a snake!
[paabzeg] (score 3, diepte 1 OP) I was one of those weird kids who liked peeling Elmer’s Glue off her hands in elementary school. I’m weirdly hoping I get to peel my own skin off!
[pabj52a] (score 3, diepte 3) This. I love to peel but this was unlike anything I’ve ever experienced. The new skin was raw and painful.
[paajj98] (score 3, diepte 0) Thanks for this list! Couldn't have come at a better time as we just received the dreaded email alerting us 2 kids have it in our kiddos class. Yay.
[paapbk9] (score 3, diepte 1 OP) Godspeed. Insert hunger games salute here.
[paastd5] (score 3, diepte 1) I'm wondering the same thing(s), but I grew up in the US
[paareb8] (score 3, diepte 0) Oh you missed the best remedy for the sore throat!  Antacids!  Little liquid Maalox feels AMAZING, gargle it if you can.
[paax3m8] (score 3, diepte 0) Ice packs are undersold for HFM.
[paa5pi6] (score 2, diepte 0) Thank you for your service!
[paa5qe4] (score 2, diepte 0) Saving thisss ty!
[pcvlzly] (score 2, diepte 3) That’s funny, I also hate baths but have been doing them and it feels magical for some relief. I think I’m in the homestretch (at least for the initial symptoms) now that my itching is finally gone. It’s just painful now but seems to be getting better and not worse for once! What a wild virus.
[pczlp9m] (score 2, diepte 4) So glad you’re nearing the end of it (or the first stage, which was the worst for me by a huge measure)!
[pad0cfw] (score 2, diepte 2) Omg I peed a little at this😆🤣
[paai362] (score 2, diepte 0) Oh hell yeah, good info here...hard won no doubt!

I will add for the parents on a budget as well, look for plain jane witch hazel in the Rx section of the grocery store (might be behind the counter, just ask the pharmacist). It's like $2 for a huge bottle of the stuff. No gimmicks or scents or anything added. Godspeed!
[paayhmx] (score 2, diepte 1 OP) I grew up in that same timeframe in the US. I don’t remember hearing much about this as a kid. But, when I told my parents about our diseased family last week, they both (independently) commented my siblings and I all had this virus as kids. 

Wut. I have zero memory, maybe I was super little? I do remember having chickenpox when I was 3, though.
[pae9ksb] (score 2, diepte 0) Not to alarm everyone here, but my son developed Type 1 Diabetes three months after a really bad case of HFMD. 

There's some research out there that links the virus to this type of autoimmune reaction. So if your 3.5 yo suddenly starts peeing his bed every night and waking from a dead sleep screaming for water...go get his blood glucose checked.
[pafjjqf] (score 2, diepte 0) Omg, thank you. My 10 year old was sent home by the school nurse this afternoon, she had cold symptoms earlier this week and the rash started at school today. I know I'm coming down with it myself, my throat is on fire and I feel like I'm dying. We just doordashed 5 packs of witch hazel wipes.
[pch62ob] (score 2, diepte 2) God speed. I’m so sorry hope something helps!!!!
[paw7wq8] (score 2, diepte 0) Hoping I won't ever need this but this was such a good list, I saved this post.
[pbo7kfu] (score 2, diepte 0) We’re going through it right now. 7m old son had it first then passed it onto my wife and now me. Strangely enough, I copped it the worse with blisters all over my body. The worse being in your throat because you can’t eat. It’s honestly the worse thing I’ve ever experienced. Uncontrollable fever at night, temperature reaching 38.5. Shaking like a leaf and sweating profusely. Any parent that catches this and that has to continue looking after their kids with it needs some serious recognition!
[pciv3z8] (score 2, diepte 2) Hahaha that’s great logic, I didn’t think about that!!

Crazy about the salt helping so much. I also read that baking soda in a bath might help…but I’m going to get some Epsom salts just in case! Would make for a relaxing bath anyway.

Thanks sooo again for the tips and the quick reply!! May your pillow always be cool on both sides.
[paahigz] (score 1, diepte 1) Same when our house got hit a few years ago.
[paam9no] (score 1, diepte 1) I had to call the nurse line because I had never had such a high fever and thought I was lightly hallucinsting
[pah03gs] (score 1, diepte 3) That’s fair. I just don’t understand why he’s 16 months old and never had a fever, never got sick at all, and my 3 yo never got it.
[pah40tj] (score 1, diepte 4) Immunology is full of little mysteries. It’s possible he was exposed to that strain previously but had such a small exposure that his body knew how to handle it. Like grabbing something a kid who was recovering had grabbed idk.
[pb9hmu3] (score 1, diepte 2) No that’s a very common presentation of it too - esp in kids. My son had it rice and just the ugly rash but totally fine. My other son got last week and only had one big mouth ulcer we could see, no other rash, but is absolutely miserable. I think it really depends if it gets in their mouth or not.
[paaiuh3] (score 1, diepte 2) Yep learned both of those the hard way too 😭
[padfn8h] (score 1, diepte 1) Adults definitely get it. They had to do weeks of quarantine procedures in the gym and cafeteria on my brothers naval base when there was an outbreak. 

I think adults are just in a position to be exposed to it less often?
[pagcigs] (score 1, diepte 1) I’d rather have noro than HFM, noro was awful but at least it was only two days. HFM was a full week for me.
[pc5v3jy] (score 1, diepte 3) Did this last week with my toddler and now that my husband and I have it we’ll be using it for sure.
[pabim64] (score 1, diepte 1) As an adult I was prescribed an oral lidocaine rinse and it helped a lot. Not for kids though.
[pccslra] (score 1, diepte 1) How many days did you feel like you were on fire? I couldn’t sleep at all because of my hands and now this morning my entire skull and body are so itchy I wanna dieee
[pcu1r6r] (score 1, diepte 2) Several… maybe 4? My big treat was an oatmeal bath. Same stuff I used on my kids with their baby eczema. I normally hate baths, but doing that helped. And I think I would do one just before trying to sleep so that things would hurt the least at that point. I’m so sorry you’re going through it! ❤️
[padyw09] (score 1, diepte 3 OP) Uffda, good to know. This disease is truly awful.
[paekuql] (score 1, diepte 3) Yep, I nervously picked at the skin on my fingertips and they were so sore!
[paagesl] (score 1, diepte 0) My toddler just started daycare and I'm pregnant so I'm terrified of HFM. My sister got it when her kid did and she got it even worse. It was just horrible. We never got it in childhood so we had no immunity and I still don't!
[paau9v3] (score 1, diepte 0) Just wait for the finger and toenails to fall off.
[pabfdbu] (score 1, diepte 0) Thank you for this. HFMD is spreading through our toddler’s class and I am SCARED 🫨 In a class of 23 kids, THIRTEEN were out yesterday. I don’t believe all are HFMD though, I think some are just a cold, but who knows. It truly feels like the hunger games. I am PRAYING we are spared bc I was just sick with a cold for a full week (I am still coughing) and I got it from my son who just had a fever for like a day and he was all good. 🫠
[pabxgho] (score 1, diepte 0) I wish I had this the first time my toddler got it. Also another myth… you CAN get HFM more than once. Daughter’s first year in daycare she had it, then had it AGAIN a year later. Doctors then said yep the virus can mutate and you can get it again. Our whole house had it twice, but the second time was less severe.
[paes7go] (score 1, diepte 1 OP) Yup! There are a few different viruses that cause HFMD, so if you got one virus, you can get it again if you get a different virus. Fun!
[pagd3qi] (score 1, diepte 1) My son and I had it twice as well. Just awful, how can we send men to the moon but not have a vaccine for this wretched virus 😭
[paghztk] (score 1, diepte 2 OP) As I was laying in bed clutching my heating pack and cursing this evil virus, I googled HFMD & vaccines.

Here’s my TL;DR of my very scientific google research:  
So, multiple viruses cause HFMD, so it’s way more challenging to create a vaccine for it. 

There’s a strain very common in eastern and Southern Asia that can cause more severe complications (like encephalitis!), and I think they’re working on a vaxx for that specific virus. 

I will say, this made me so glad that my kids got the chickenpox vaccine and won’t have to suffer with that.
[pact6yq] (score 1, diepte 0) My husband had this close to 10 years ago (just him! In his 30s!) and the crock of dermatologist that he went to told him he'd never seen anything like it before and that he might have FUCKING LUPUS. 🤦🏽‍♀️ Ugh.
[pacznou] (score 1, diepte 0) Me sitting next to 3yr old with it, thinking about the witch hazel. How often did you apply?
[padbkpd] (score 1, diepte 1 OP) On me? Every 1-2 hours. I used it very liberally. They give you witch hazel pads to stick in your giant pad after you deliver a baby to help comfort and heal any tearing and the stitches. So it’s definitely soothing and won’t irritate skin.
[pad2y2y] (score 1, diepte 0) My 13 month old got this last year.. literally 2 weeks after we had all recovered, his finger nails started falling off! Apparently it kills the nail beds and everything has to regrow for some people. Honestly good luck to you and thanks for the great recommendations! 🙌🏻
[pae1goh] (score 1, diepte 0) this is such a great post. HFMD has gone through our house 4-5x in the past decade and I get it every time (I never get the sores, just a crazy high fever and am MISERABLE). I WISH I had thought of trying witch hazel on my kids' sores!!
[pagihq0] (score 1, diepte 1 OP) Best of luck. Hope the witch hazel works its witchy magic for you both! Take that Advil!
[pagc9dy] (score 1, diepte 0) Wow, this is so helpful and kind of you to put together. I also have made multiple HFM posts as it’s struck me twice. I felt suicidal when I had it both times— that’s how bad it was for me as an adult, it’s truly the worst virus I’ve ever experienced.
[paggejf] (score 1, diepte 1 OP) Oh it really is the worst. Sickest I’ve ever been, inclusive of Covid, strep, and (unknowingly) consuming raw chicken in a developing country. And then once your fever goes away, you get a fun rash as a souvenir! People who say this is a mild illness can kiss my ass.
(25 reacties met lagere score weggelaten)

=== THREAD 1nb2gqf ===
SUBREDDIT: r/BuyItForLife
DATUM: 2025-09-07  SCORE: 25  REACTIES: 67
TITEL: Need comfortable shoes to help with foot pain.
POST (source_id=post):
I'm a 16 male and my shoe size is 11/12 for men (USA) and I work at McDonalds, haha laugh it up. anyway I'm obese, like 270lbs, and go to the gym.   
My problem is my foot pain. I know I need to lose weight but I'd also love to have money on the side, I can pay for my gym memberships and better food. Problem is my foot pain. I work 4-5-6-7-8 hours a day, and it gets really bad. By the end of my shifts my heels are on fire, for some reasons it's only my heels. I got dr scholls insoles and I'm gonna see how those work by tommorow. I need better shoes though, if anybody has any recommendations please let me know, all I care about is comfort comfort comfort, I don't want to experience the pain anymore or I at least want to prevent it, so if anybody has any shoe brands they swear by to reduce pain, please feel free to let me know!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ncyoup3] (score 73, diepte 0) You need to see a podiatrist. 

Intense foot pain like that is not normal, especially at your age. A podiatrist is a foot doctor who can tell you what is actually happening with your feet and based on that diagnosis they can tell you what kind of shoes or inserts you need to address your medical issue.
[ncz0zir] (score 49, diepte 2) Tell your podiatrist EVERYTHING related to your foot pain.  Do not withhold any information that might be relevant to your feet.  One of the biggest disservices that you can do to yourself is not give your healthcare professional a clear picture of what they are treating/diagnosing.  If you need to; Take notes beforehand in case you get a little bit nervous with a doctor, (white-coat syndrome).

I went through a few ingrown toenails in high school as well.  It turned out I was wearing ill-footing shoes, and cheap-ass socks.  Of course, YMMV, and I would definitely discuss your footwear with your podiatrist tomorrow. 

As for shoes, you probably want something with stability.  If you have a shoe store specializing in running shoes, they can definitely help you find a shoe to help you out and will do their best to make sure you leave feeling confident in your purchase.  Having once been 360lbs, I know the struggle of finding good shoes amongst other things.  Best of luck to ya, and keep us posted in here!
[ncyx5v6] (score 34, diepte 1 OP) The irony is that I'm going to the podiatrist tommorow for an ingrown toenail! what should I ask him?
[ncyslyr] (score 12, diepte 0) Brooks has great runners for plantar fasciitis
[ncytj2u] (score 10, diepte 0) Hokas are very soft, but they might not help you. As another guy said, severe foot pain is not normal. I would see a doctor. But losing weight would likely help that and many other potential problems. 

Incidentally, you don't need to join a gym to lose weight. Often those memberships become an unending expense without benefitting you, because you don't go. The surest way of losing weight i know of is to stop drinking soda, both regular and sugar-free (which iirc triggers your blood sugar to rise just like sugary drinks). Also fruit juice and beer. 

Other than that, find a workout buddy to do literally any kind of exercise, and make a schedule. Good luck!
[ncym2wt] (score 8, diepte 0) I don't have a specific suggestion, but look for shoes for nurses
[ncz1aqg] (score 8, diepte 2) Explain the issue of your foot pain. It may be that the podiatrist tells you to try orthotics.
[ncyo3r0] (score 6, diepte 0) Hoka. They are not cheap, but you can't replace your back, feet or knees. They make an all black version used by many restraunt workers.
[ncz5oz3] (score 6, diepte 1 OP) As chance may have it I'm going to the podiatrist tomorrow for an ingrown toenail! We have medicade so everything is covered completely free, I'm going to ask him about the pain and ask what shoes or inserts I should do. Thanks!
[nczizv3] (score 6, diepte 2) Fantastic! In the meantime, gentle stretching for your feet and legs, a heating pad, and rolling your foot over a frozen water bottle for a bit after exercising or standing for a long time will all help.
[ncz8dno] (score 6, diepte 1 OP) Can't I just lose weight and have comfortable shoes at the same time? I know I'm overweight, but I don't see why I can't lose weight and have shoes that aren't killing my muscles.
[ncyr0e6] (score 5, diepte 0) Hey, congrats on the job! My husband is 350+ lbs. and swears by Hoka Bondis. They cushion the foot really well. They’re not cheap, but you can get old styles on sale. Also, if there are marathons happening near you, they usually have a shoe booth with discounted shoes from running stores. A quick fix for plantar fasciitis are Dr. Scholl’s inserts but they don’t last long and are not an alternative for good shoes.
[ncyxwy4] (score 4, diepte 1 OP) I only drink water! My problem is my diet, but I know I need to get my protein and calories in calories out! Thanks for your advice man
[ncz3xbd] (score 4, diepte 0) Hokas have helped my foot pain a lot, but they're expensive. Do you have okay health insurance? If you can get to a podiatrist they can figure out exactly where the weak points in your feet are and what kind of support will help. Doing that before investing in good sneakers will save you money in the long run. 

If they recommend physical therapy and your insurance covers it, do it. Even if you have a limited number of sessions, they can teach you useful exercises and do therapies that will lessen the immediate pain. My pt also taught me how to tape my feet for more support, the way gymnasts do. Your podiatrist or PT may also offer you a cortisone shot, and that can really really help in the short term. 

Lastly, just fyi, foot pain can easily also be caused by tightness or issues in your legs, hips, or lower back. If you have any pain in those areas, or even just muscle tightness or lack of flexibility, make sure to mention it to your doctor or pt!
[ncz84wi] (score 4, diepte 0) The pain in your heels indicates that you possibly have plantar fasciitis.  Good shoes for PF include those with wide toe boxes and zero heel drop.  Cushioned insoles might be a good choice for you as well.  Altra makes wide toe box, zero drop shoes and they offer 4 levels of cushioning depending on the model (low, medium, high, max).  I'd recommend at least the high cushioning since you're on your feet so much.  Good luck.
[nd10elq] (score 3, diepte 3) Altra shoes/ boots, have all but relieved my foot pain. Every time I put on my boots I tell anyone who will listen how much I love these boots.

By the way, did I tell you how much I love these boots 👢
[nczwku2] (score 3, diepte 3) Yes, that is the most probable outcome. I have been wearing orthotics for almost a year. I see noticeable improvement in how my feet feel.
[ncz3liu] (score 3, diepte 1) I have RA and work on my feet all day. These are my go to shoes and the ones my rheumatologist told me to get for my feet (also have hyper mobility). They last me about a year of teaching before they start to break down and I need to get insoles or replace them. I've been wearing them for about 6 years now.
[ncz014r] (score 3, diepte 2) Hey no advice on shoes, but I have been using an app called MyNetDiary that’s great. It’s a free food and exercise tracking app. You can take photos and save them to see your progress, there’s a community to help cheer each other on, and if you want to pay for the premium membership, there’s coaching and recipes too. It’s helped me lose 35 lbs so far. Good luck!
[ncytlhs] (score 3, diepte 0) Hey there. I have a similar build, and I'm a teacher. I'm on my feet all day too. All feet are different, but I use On Cloud shoes. I find those work best for my feet.
[ncyx14q] (score 3, diepte 0) PSW (similar to CNA in the US) and I work 16hr shifts regularly. These are 25k step shifts. And I'm a little on the chunky side 😉

Definitely go to a podiatrist to get a diagnosis or eliminate potential problems. Here in Ontario Canada a podiatrist is under $100 for the initial visit. It could just be your weight but it also might not be. It would make sense to rule out some problems before dumping money on a good pair of shoes that might not be right for you if you were given a diagnosis.

Another suggestion is to wear compression socks, the lightest compression is a great place to start and you can buy them fairly affordable ($20-$30pr) on Amazon. The majority of my healthcare peers swear by them - they were life changing for me.

Once you get into shoes, most brands have different cushion levels but you'll probably want something like New Balance 1080s or the Asics gel Kayano. I wear the Asics and I don't find them all that slip resistant when I'm in the kitchen. My mom worked at McDonald's when I was a kid and I remember the floors being especially greasy so keep that in mind when you're buying shoes too.
[ncylf3s] (score 2, diepte 0) Best i've had are Sketchers by far.
[ncynjgf] (score 2, diepte 0) Hokas or Sketchers.
[ncynr91] (score 2, diepte 0) I swear by Superfeet Green insoles
[nd13x4w] (score 2, diepte 1) I love Hoka and have bought so many pairs. But be careful! The Hoka bondi plush shoes may actually make your feet and legs feel worse. Consider Hoka Clifton’s which are more balanced. They also have wide options if needed.
[ndg2r33] (score 2, diepte 1) This is it. Talk to a podiatrist. Hard to give much advice without seeing your feet/stance. 

That said, basketball shoes with good insoles that match your arch and support needs will probably be the most comfortable. Powerstep Pinnacle or Superfeet seem to be the most recommended.
[nczt0sg] (score 2, diepte 1) A friend of mine of about 120+ kgs is also wearing hoka. She is standing a lot (hospital md).
[nd0di32] (score 2, diepte 1) I wouldn't wear running shoes working at McDonald's, unless I misunderstood the post. OP would need something that would give them better tracking on the floor.
[ncytxso] (score 2, diepte 0) I had a similar situation and my podiatrist directed me to New Balance.  They have a scanning device that detects the arch of your foot, and suggests shoes or inserts which support that situation.  It took a month or two for my feet to adjust, but my foot and lower back pain is totally gone.
[ncyvz0c] (score 2, diepte 0) My partner and I both are in your weight range (although much older). 

I had heel pain my whole life - tried many shoes and drug store inserts to no avail - until I saw a podiatrist. My partner had not had pain as long as I had, but as he aged, it became a problem, so we both saw a doctor about it at the same time. He was diagnosed with arthritis, I was not, but both of us were told to full length wear inserts. 

We still get them from our podiatrist every 6 months (but I don’t think they’re Rx) - ProTech Power Step. 

Made my heel pain (made worse from hours standing/walking on concrete) completely go away… unless I go back to wearing shoes without the inserts. I’m pretty sure my own heel pain has everything to do with my weight and no other issue.  Getting rid of  the heel pain has been so helpful (I also have nerve damage from a car accident that is aggravated by standing still and alleviated by moving around - so finding something that helped the heel pain I’d get from long periods of walking was HUGE for me)!
[ncywwzl] (score 2, diepte 0) We have a shoe store called Beck's that has the scanner and several kinds of shoes and inserts. I have plantar fasciitis and Achilles tendonitis. My heels and my Achilles are screaming after being on my feet. They fixed me up with a pair of Hokas and a superfeet insert. Also a pair of Aertex flip flops to wear around the house. I am doing so much better. Make sure you go to someone who is knowlegable. Hokas do different things and Superfeet is a really good insert. My biggest problem is pronation and these things all help. I have been to several podiatrists and they honestly don't do as good a job.
[nczezce] (score 2, diepte 1) I second the wide toe box and zero drop
[ncyk01a] (score 1, diepte 0) I don't know if shoes can help you with this, I'm sorry. Either way, the most comfortable ones are running shoes.
[ncypu9v] (score 1, diepte 1) There are plenty of other reasons for foot pain beyond plantar fasciitis. To say it’s specifically that without doing any orthopaedic tests isn’t helpful.
[ncyu2oe] (score 1, diepte 0) New balance 928 oil resistant version. Take out the insert and purchase a power step or navy blue redi orthotic from Amazon to replace it.  Ice at night, stretch ur ankle and heel in the am and pm (google excercise for plantar facitis/Achilles tenosynovitis.) get some OTC Diclofenac gel and rub it like u love it.
[ncyzij0] (score 1, diepte 0) Shoe itself won't fix your problem. Visit podiatrist then decide what to do. However I think most of the comments here will be Hoka and Brooks which is also right, but doesn't mean for your case as well
[ncz1dzs] (score 1, diepte 0) Hoka One One
[ncz280g] (score 1, diepte 0) I used to buy all of my shoes at a store that my podiatrist recommended in San Francisco on Lombard Street called Shoes-N-Feet.  They would help me choose the right insert for my particular problem (I needed arch support and a good heel cup.) I slowly traded out all my painful shoes and bought all "healthy" ones. My feet never hurt again. Slippers and sandals too!
[ncz6wnn] (score 1, diepte 0) Hokas or brooks ghost have helped my heel/foot pain. You can find them cheaper and only slightly used on poshmark for a good price..hokas are usually fugly looking but IMO helped tremendously with the heel pain.
[nd05iot] (score 1, diepte 2) Everyone out here gonna downvote me and kiss ass instead of being real, which is the only thing that'll help


No you can't have shoes that don't kill your feet: being on carpet or dirt would be comfortable, but not fast food flooring. It's hard for anyone to be comfortable on that unnatural surface


the barefoot shoes I suggested have extra wide toe space, which would aid in your feet being nimble ( instead of being crunched into a ballerina ended toe box with 'normal' shoes)


There's also pelvic floor exercises you can do, i could send you a sheet i got from a specialist for the whole breakdown, if you'd like


As for diet, if you can cut out wheat & sugar, you'll be a new man in no time. That shit has everyone addicted
[nd0ccdd] (score 1, diepte 3 OP) If it helps me than sure I don't mind
[nczacg2] (score 1, diepte 0) I have terrible foot pain as a result of my chemo. I just recently purchased shoes from orthofeet. They come with extra inserts for spacing and support so you can add what you need. I’ve had them about a month and I have to say I will likely stick with this brand unless something changes.
Additionally, if you are experiencing plantar fasciitis (which I had in the past) there is a United Ortho plantar fasciitis brace available on Amazon that absolutely works. 
Wishing you wellness.
[nczcr3r] (score 1, diepte 0) I love my Altra Olympus shoes for 12hr shifts of standing. I got mine almost half off at REI  Re/Supply.  It’s for lightly used gear.  You have to be a member to get the discount but I bet you could get a member to go to the checkout with you(bring cash).  I helped some Dutch tourists buy a tent there recently.   Make sure the bottoms of the shoes are sturdy(Vibram), I’ve noticed a lot of Hokas have soft bottoms that get ripped up easily
[ncze0lq] (score 1, diepte 0) >...I work at McDonalds, haha laugh it up

No shame in honest work from me. 

>By the end of my shifts my heels are on fire, for some reasons it's only my heels.

Sounds like plantar fasciitis and/or you need more arch support. 

> I need better shoes though, if anybody has any recommendations please let me know..

Bates makes a side-zip boot for military/law enforcement but (glances down thread) ask your podiatrist what you should be wearing to work on tile all day. You'll probably end up with something they recommend for Police/Nurse/Construction workers.
[nczeuek] (score 1, diepte 0) I had a podiatrist point me towards superfeet insoles and I don't wear anything without them anymore. They come in different fits depending on your arch height, so you can find one that fits like a custom imagine, which would be hundreds of dollars from the podiatrist. Dr schols are terrible, honestly you should return them. 

Also, find a shoe that gives you enough room in the toe box that your toes can splay out like they naturally would.  Nothing should be compressing your foot, and you might find that you need to size up. 

Describe the pain to your podiatrist. They should do X-rays to look for a fracture or bone spurs. You may be able to get some sort of note for work that would let you use a stool or something. 

Good luck, for pain is seriously the worst.
[nczfuej] (score 1, diepte 0) Sounds like plantar fasciitis. I’m also overweight and have been for most of my life even though I busted my ass in the gym. What worked for me was Birkenstock blue footbed inserts.  Holy shit…they were uncomfortable the first day or so pushing up my arches and then… bam, no more foot pain. One thing to consider is if you are pre-diabetic or diabetic.  One symptom is neuropathy. Simple blood test for A1c can detect it. Mounjaro is a miracle.
[nczlbvc] (score 1, diepte 0) While I don't love how they look (on me), the Hoka Bondi helped my plantar fasciitis go away and vastly improved my severe foot pain, which was due to vitamin deficiencies and wearing bad shoes
[nczrr4k] (score 1, diepte 0) I agree see a podiatrist. Might be a tarsal coalition, which is what I have. They can also give you better shoe suggestions.
[nczvywm] (score 1, diepte 0) Is there anything about your current shoes that are bothering you other than foot pain? Too tight width? Too tight on top of the foot?

Often times big boys might not have wide feet but have a large foot volume - basically a thicc foot. I think you should consider work boots. They are roomier for those kinds of feet and will have a firmer footbed which I think you will benefit from. Your weight simply might be too much for any of the common foam soled shoes. 

The trade off for boots in a kitchen environment is that they have less breathability but do have better ankle support and foot protection.
[nd02gti] (score 1, diepte 0) Definitely agree on insoles! Those should help significantly with impact absorption.

Make sure you are sitting down occasionally during your shifts as well. No matter how good your shoes are you will have pain if you stand for 8 hours straight.

Remember that McDonald's usually requires slip resistant uniform shoes, and the slip resistance does wear off, so you will have to take that into account (anything will have to either be replaceable when the soles wear off, be able to replace the soles, or be transferable between shoes)
[nd08wcs] (score 1, diepte 0) New Balance with prescription orthotics (podiatrist will fit you).  Ice and stretch at night (podiatrist will likely advise this as well).
[nd0ruyo] (score 1, diepte 0) Kuru sneakers designed for plantar fasciitis
[nd0v5ku] (score 1, diepte 0) Look for work shoes for chefs, nurses, etc Also google shoes for "people on feet all day," orthotic shoes, and read the reviews.

Dansko is quite a good one for comfortable and supportive shoes, they started as a brand specifically for nurses I think. You can also pair supportive shoes with add-on orthotic insoles for add-on comfort. 

My own thoughts based on what I've tried - I don't recommend Easy Spirit or Skechers, despite what their marketing says.
(20 reacties met lagere score weggelaten)

=== THREAD 165yi7j ===
SUBREDDIT: r/BuyItForLife
DATUM: 2023-08-31  SCORE: 47  REACTIES: 67
TITEL: Recommendation for shoe insole
POST (source_id=post):
Recommendation for shoe insoles? I know this item wont likely be a for life purchase but this group has the best recommendations. What is your favorite and why? I tried z liners and thought they were decent. Just searching for better/best.  I walk a lot everyday.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nqwys0m] (score 10, diepte 0) weird thing about insoles is ppl chase cushion when the real fix is how the heel sits. every podiatrist rant on this sub circles back to that one detail. want u wanna look for is that foam isn’t soft like running shoes and the arch isn’t dramatic. Id recc these superfeet ones, takes one wear to get used to them tho. 

just remember when the heel wobbles even a little, the whole foot has to work extra giving u that i walked alot ache feels.
[nhcq670] (score 6, diepte 0) most generic insoles are just squishy foam, so they feel nice for a week and then flatten out. the difference with something like superfeet is the structured heel cup and arch support it actually redistributes weight instead of just cushioning it.

some people with really high arches move up to the green model, and others who want something slimmer go for the carbon, but [the blues](https://DealzSphere.github.io/Orbit/?to=recommendation_for_shoe_insole) tend to be the safe pick when you’re on your feet a lot. they last way longer than the liners most shoes come with cuz of the medium arch
[n8pgctr] (score 5, diepte 0) I've had to deal with hip, back and knee pains for years, compelling me to get expensive, heavy and cumbersome custom insoles. I decided to try Stride Soles' insoles and I am pleasantly surprised. Not only are they really effective at eliminating the underlying factors causing the pains, they are also more affordable than the other custom insoles I used to get, more comfortable and lightweight, and also promise durability. I'm really looking forward to enjoying my order for a long time.
[njkfubo] (score 3, diepte 0) most generic insoles are just squishy foam, so they feel nice for a week and then flatten out. the difference with something like superfeet is the structured heel cup and arch support it actually redistributes weight instead of just cushioning it.  
  
some people with really high arches move up to the green model, and others who want something slimmer go for the carbon, but \[the blues\](https://noxohub.github.io/radar/?q=EOI65153) tend to be the safe pick when you’re on your feet a lot. they last way longer than the liners most shoes come with cuz of the medium arch
[jygyk33] (score 2, diepte 0) [Dale's Leatherworks](https://dalesleatherworks.com/collections/insoles-1) sells Leather Insoles made from Full Grain Natural Veg Tan Wickett & Craig Leather in 3 different thicknesses:  
  
Thin - 5 oz (2.0 mm) for $30  
  
Medium - 10 oz (4.0 mm) for $40  
  
Thick - 15 oz (6.0 mm) for $45
[jyh85u3] (score 2, diepte 0) Sole fit my feet perfectly with lots of support and are more durable than Superfeet. The Active series is the most durable and the Performance series is made of cork that molds to your foot.

Best prices are if you join the email list and buy directly from their website ([yoursole.com](https://yoursole.com)), they have promotions pretty frequently.
[k7nu4ob] (score 2, diepte 1 OP) Thank you for the suggestion.  I went with sole and they are amazing.  Will be purchasing another pair soon.
[lra3k73] (score 2, diepte 0) OTC insoles hardly help that much since it is not supportive or the shape is not fitting well and that is why lots of people try to get custom insoles. Comments above are correct that it is way TOO expensive ($200-$300) for orthotics from Doctors' even though product is 2x better than OTC. Nevertheless, nowadays there are custom orthotics online options like upstep and others. But if it is still too expensive or procedure too tedious for you, I tried a decent product with affordable price, (60-70) called SprinSole. They allow your to scan feet via phones (no tedious foot impression kit) and I can immediately feel the support when standing on their insoles, which is just right since it is matching our feet arch.
[m43ew3s] (score 2, diepte 0) Have you tried Stride Soles yet? My wife swears by her pair and it's been 3 years now...
[ncjoydg] (score 2, diepte 0) Generic insoles are basically just cushions but yeah, traditional podiatrists are insanely expensive even though they last significantly longer. In my time of trying insoles, I’ve found Stride to be a good middle ground since they’re custom but cost about half of what you’d pay a podiatrist.
[nd9im2f] (score 2, diepte 0) How often are you on your feet each day? Do you have any specific needs for insoles? Superfeet is the most quoted generic option, but I’ve always favored custom ones like what Stride sells.
[o4eg59p] (score 2, diepte 2) Agreed
[pa5vt1g] (score 2, diepte 0) For BIFL purposes, the thing that wears out on most insoles is the foam top layer, while a good supportive shell lasts years. Look for something with a firm base and a replaceable or durable top cover. Stride Soles' insoles are custom made by a podiatry lab from a phone scan of your feet, $249. The support structure is built to last well beyond a pair of drugstore insoles, and fit is the other half of durability: an insole that matches your foot doesn't get stomped flat in the wrong places.
[jygtzhh] (score 1, diepte 0) Hello /u/billythebeefpuppet! Thank you for your submission! The AutoMod thought that your post might be a request type post and has changed the flair accordingly, but if this was wrong feel free to change it back!

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/BuyItForLife) if you have any questions or concerns.*
[jygtzia] (score 1, diepte 0) Hello /u/billythebeefpuppet! Thank you for your submission! I justed wanted to inform you you might also want to try posting in /r/boots which is a smaller subreddit but might be or specialized for your request

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/BuyItForLife) if you have any questions or concerns.*
[jygww30] (score 1, diepte 0) Tbh, the ones you would get from your podiatrist when they make a cast of your feet. The retail ones just seem to flatten or get worn out real quick and I walk a lot too. The ones I got from my podiatrist literally lasted me years. Not even the fabric pieces have worn away on me. But of course I’m sure you would need decent insurance cause I’d imagine it being somewhat expensive.
[jyo7pet] (score 1, diepte 1) I have podiatrist ones. They are twice as good, but 10x more expensive.



Not a good value.
[jyo8nyb] (score 1, diepte 2) Hence why I mentioned “decent insurance”. Mine cost me nothing. Both on my parents’ plan before I turned 25 and my own plan after that. Guess picking a plan opens a new can of worms based on what coverage you want, deductibles, copays, network, etc.
[jyob73w] (score 1, diepte 3) Cap as fuck.



No insurance offers no copay for a specialist plus orthotics.
[jyobrpf] (score 1, diepte 4) Maybe yours doesn’t. Lol. Not going to share the PDF of mine cause it has my company name and my name all over the agreement and I don’t want that personal info out that for that but what I had under my parents was Horizon BCBS and mine currently is Aetna (not the Medicare/ Medicaid one). Both were through employers.
[jyocchq] (score 1, diepte 5) Cap
[jyocemf] (score 1, diepte 6) Lol ok bud whatever makes you sleep better at night 😂
[jyocph4] (score 1, diepte 7) Same
[lpxldzp] (score 1, diepte 5) what plan are u currently on?? im a bit curious and would like to look it up so i can consider other options and compare it to my dad's plan and coverage that im currently under so im prepared for the time i get taken off 😭😭
[lqaplyw] (score 1, diepte 6) All I can say is Aetna. Tons of plans are offered from all the providers. It’s contract based. Like my dad worked for the state of NJ and he had a god plan under BCBS. I worked for a healthcare company and sometimes the joke is if you want the best insurance then you won’t get it from working form a healthcare company. I think as of now gov’t employees and tech get a sweet contract. 

If you are going on your own then I would choose what is best from what your employer offers and read everything. Some things might not even apply to you and some might. So pick what’s best for you and your current health.
[lqeowat] (score 1, diepte 7) thanks for ur advice!! im gonna save ur comment bc i found ur explanation really helpful and im pretty sure its gonna come in handy someday

ive been trying to make small steps towards leaving out of my comfort zone and become more financially independent

having an adhd and dyscalculia combo tends to leave u financially dependent on anyone who knows stuff like basic economics and how to manage monetary and fiscal matters 💀💀
[lx1sowr] (score 1, diepte 8) You can also call your state marketplace for insurance and they (the agents on the phone youll talk to) often are very helpful in my experience! The 2 times I've been laid off/had no insurance and called them I was able to get on a plan that's affordable and actually better than my union fought for work plan (which itself was pretty good but not the cheapest)! Give it a try and I'm happy to dm you more details! I also struggle with the same flavors of brain spice so I feel you!!!
[ochfjif] (score 1, diepte 7) Lol as if youre going to get doxxed over your insurance plan. Good lord 🙄
[olbbd58] (score 1, diepte 7) I work for the govt. I now pay a quarter of what I paid in the private sector and GEHA has the deductible rolled into the overall cost of treatment. I was in the ER. A 24/7 Emergency Center/clinic in a shopping center. No deductible, nothing. This for nearly severing my left three middle fingers. Nada. Not even a line to seek treatment. Xray and 23 sutures spent almost 5hours there.  I'm new to govt. but yes, the healthcare is so low you can choose two plans simultanioisly and it's still less than the HMO. Rx was $5 lol
[mqm1b10] (score 1, diepte 5) I would imagine someone who non-facetiously uses terms like "cap" wouldn't have good insurance... Surprisingly they're so ignorant that they don't think good insurance even exists.. 


No cap
[olrkx4a] (score 1, diepte 6) did you feel cool while typing this?
[md08rfi] (score 1, diepte 4) Lol mine were free. $500 otc. My premium is higher tho. Blue cross
[lq7e4ps] (score 1, diepte 1) You are 100% correct that the podiatrist is over charging you. It makes sense though, he has a business to run so needs a good margin to support his staff, the office space, insurance, marketing, etc.. etc..

Most podiatrists simply send out the orthotic to a lab, which costs about $100-$150, which they then charge you $300+ for. It's a big rip off even though it's a good product. 

The reality is that in 2024, you can get that same orthotic and podiatrist experience online. There are sites like upstep and stridesoles which still have the doctor prescription and everything that comes along with it, for a fraction of the cost. The only difference is that you will have to do the foot mold at home instead of in a clinic. For some this tradeoff is worth it. 

I personally have really bad flat feet and need orthotics. However, I was super frustrated with the price I kept paying for my pair at the podiatrist, so I found out where my podiatrist was buying he's orthotics and just went directly to the source. I used the same prescription he had, I just wasn't willing to pay his markup.
[lzlzlav] (score 1, diepte 2) So what brand does your podiatrist use?
[m5qh8as] (score 1, diepte 3) Dr. Stephanie Kane, she recs Stride Soles
[m43efka] (score 1, diepte 1) Podiatrist ones are good, but expensive. I would look at orthotics that offer foot scanning remotely from an app like Stride Soles does, FWIW.
[mhhgwms] (score 1, diepte 1) Enhoy your cake day!
[mvmhqnp] (score 1, diepte 1) I stopped using mine because they just made most shoes too snug. I could only buy wide width. I’m a sneaker head so it’s just impossible to use the orthotic insert with most shoes. Mine were $330 or so for 2 pairs. That was with insurance.
[nt3f9o1] (score 1, diepte 2) In Canada it’s 650$ for one single pair 😢 if I didn’t have a job with benefits I would never have bought them. But they are good
[n96fwqp] (score 1, diepte 1) thanks
[mtwn4xl] (score 1, diepte 2) Hey, how's it feeling?
[mtzvphh] (score 1, diepte 3 OP) The sole insoles feel great. I bought several pairs now. One pair that I wear while working is starting to show heavy wear after a couple of years of heavy walking. They held up well in my opinion.
[mulsnmb] (score 1, diepte 4) Hell yeah, thanks for the update!
[mvmyz83] (score 1, diepte 4) Thanks so much for updating!!
[mzmddop] (score 1, diepte 4) Thank you for the update!
[n46oimi] (score 1, diepte 4) Just ordered a couple pair. Thanks!
[na1gcn6] (score 1, diepte 4) A couple of years?  Are you using the Active or Performance insoles?
[p50umqc] (score 1, diepte 4) Sole has been an absolute game changer for me. I’ve bought several pairs for both working out and everyday life. 

For me, the cork lasts about 3 months if I use them everyday so there’s that but they’re like $40 and I’d spend that on one day of relief.

They’re essentially custom because they mold to your feet, but they have a very unique arch that fits me perfect - but I can’t speak for out it would work for anyone else.
[jyies5w] (score 1, diepte 0) Treadlabs for me. 2 part system, arch support plus removable top pad. They have a no conditions warranty on the arch supports. I had one Crack after 2 years, sent them a picture, and they sent a replacement. No hassle, didn't have to send anything back to them, just the picture. Pads have no warranty  but are about 30 dollars each. 

I did the professional route 1st, doctor, 3d scan, 500 dollar custom insole... I'm happier with tread labs. But I don't have anything too odd about my feet or gaite. Just needed arch support and heel cups.. 

Close to BIFL.
[jyk1027] (score 1, diepte 0) I feel like I've answered this like three times in the past week or two. Superfeet. Green are for high arches, blue for low arches. Don't bother with the newer comofrt ones, do not buy the pink laydies ones. You want the original. They last longer than my shoes do and I move them as needed, especially with running shoes and such. My snowboots and rainboots share a pair of the winter version since those are a bit lower profile and I need fluffy sock space.
[jyxwl7z] (score 1, diepte 0) Solid leather insoles are my favorite. I cut my own from full grain shoulder leather. Might not work with all types of shoes though, I only do this on shoes where the rest of the sole is somewhat hard. Squishy oursoles like running shoes might be weird.
[jz64rfo] (score 1, diepte 0) YES!! I've tried every brand of insoles on the market. Ultimately, I switched from my custom insoles to this brand called [Fulton](https://walkfulton.com) and nearly immediately my foot pain went away (& back pain). These are made from cork so they mold to your arch and absorb shock/impact. a bit pricey but obviously way more affordable than custom, and really comfortable.
[lxw7p6y] (score 1, diepte 0) Akusoli. Not sure about the durability, though I've had them for like 4ish months now and they look like new still. I walk quite a bit every day, too, and I haven't felt like my feet are gonna fall off at the end of the day as I started wearing them.
[m3zla0t] (score 1, diepte 0) i tried sole insoles but did not like them. fp insoles are comfy but my feet slide in them a little. the best ones for me were superfeet, cloudsoles and happyfeet( memoryfoam, you can get em on amazon for 9 bucks)
[m5wmks1] (score 1, diepte 1) I agree! Been two years with my Stride Soles and the condition is still great. Obviously they are no longer as shiny, but still work well.
[m5wmztm] (score 1, diepte 1) I agree! Been two years with my Stride Soles and the condition is still great. Obviously they are no longer as shiny, but still work well.
[m4i964h] (score 1, diepte 0) checkout frido, they have some amazing insoles, and you may find the suitable one for you.
[m5shd75] (score 1, diepte 0) live
[m5stato] (score 1, diepte 0) Go with Stride Soles... they have a really nice app to scan your feet, and actually do a gait analysis. This way they can customize it for your feet and your feet only...
[mefb19h] (score 1, diepte 0) I have been using Stride Soles for about a year now and they have really held up well. It seems like it'll be bilt for life, but no way to now. Dr. Zac did say he would re-do the top and mid layer for free at any time, so that's better than my podiatrist said at least.
[mehcmb0] (score 1, diepte 0) I have been using Stride Soles for about a year now and they have really held up well. It seems like it'll be bilt for life, but no way to now. Dr. Zac did say he would re-do the top and mid layer for free at any time, so that's better than my podiatrist said at least.
[meng5v3] (score 1, diepte 0) I have been using Stride Soles for about a year now and they have really held up well. It seems like it'll be bilt for life, but no way to now. Dr. Zac did say he would re-do the top and mid layer for free at any time, so that's better than my podiatrist said at least.
[mevdnkg] (score 1, diepte 0) I have been using Stride Soles for about a year now and they have really held up well. It seems like it'll be bilt for life, but no way to now. Dr. Zac did say he would re-do the top and mid layer for free at any time, so that's better than my podiatrist said at least.
[mgqc1f4] (score 1, diepte 0) First, try some OTC insoles like superfeet, Sole, etc. But if OTC does not help like my case, I would recommend some custom insoles. BUT traditional custom insoles from my podiatrist's are so expensive and you need physically visit store. So I tried some more AFFORDABLE online custom insoles solution: fitmyfeet, sprinsole, etc, only around $80? Besides, they allow you to scan feet via phones. So if custom insoles are what you search for, my suggestion is ease in from those AFFORDABLE ones instead of blindly jumping into expensive ones.
[n1hbk2h] (score 1, diepte 1) What is otc?
[n1nzbzd] (score 1, diepte 2) Over-the-counter
[nd0rdc2] (score 1, diepte 2) Asking instead of tabbing into google and finding out  is braindead.
[njhxd19] (score 1, diepte 2) Stands for “over the counter”
[mh0aule] (score 1, diepte 0) I have been using Stride Soles for about a year now and they have really held up well. It seems like it'll be bilt for life, but no way to now. Dr. Zac did say he would re-do the top and mid layer for free at any time, so that's better than my podiatrist said at least.
[mhm4st4] (score 1, diepte 0) Thought I'd chime in here. Long term lurker in this sub. 

I can’t restate enough how much the original Stride Soles insoles have supported me through injury recovery. I was immediately impressed and even referred my sister a couple weeks after getting mine in the mail.
[mho04w4] (score 1, diepte 0) These are nothing special.

Not worth the money they charge .

Save up and get real orthotics.
[mi8m7a5] (score 1, diepte 0) Stepprs insoles are the best ones ive tried, they are cheap and lasted me over 1 year now
(49 reacties met lagere score weggelaten)

