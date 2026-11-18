# Label-batch batch_0077

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
Schrijf het resultaat naar `batch_0077.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 16e5znd, lfvfau, zf3u88).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 16e5znd ===
SUBREDDIT: r/Teachers
DATUM: 2023-09-09  SCORE: 17  REACTIES: 92
TITEL: How do you deal with your hurting feet?
POST (source_id=post):
I had a desk job for almost 20 years, now I'm teaching middle school and I actually enjoy it, but there's one thing really getting me down: my feet are killing me. 

I'm older, 53, and I'm heavy, neither of which helps. At the end of every day my feet are so sore that I have to run home and rest, I can't really do other things other than teaching these days. I bought some Dansko shoes, which is definitely helping, what else will help? Any chance that I will get used to being on my feet so much and won't be so sore? I can already tell that I'm a bit fitter, it's easier to go up and down the millions of stairs than it was when I started this job, but oh my gosh my feet. Anybody have any advice for me?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jztgbzy] (score 20, diepte 0) SAS shoes. Ugly as fuck. Comfortable as a cloud. Like walking on air. Expensive but they last forever. You’ll only be buying them once every few years. And they come in wide and extra wide widths. 

But also - make sure you do go to a podiatrist and make sure you don’t have any underlying issues besides the plantar fasciitis. I thought I just had that and it turns out there was also a Morton’s Neuroma in the mix too. You may need custom fit orthotics to truly alleviate the pain.
[jzteaiv] (score 15, diepte 0) Whatever special shoes but also have a high stool to sit on in front of the class, and/or have your desk in a place where you can supervise/teach etc. You don’t need to stand all the time.
[jzuv4m3] (score 7, diepte 1) >Ugly as fuck. Comfortable as a cloud.

Great slogan!
[jztz2fy] (score 6, diepte 0) I don't understand people who can wear dress shoes and still do this job.  I wear my skechers.  If admin asks me to wear dress shoes I tell them I work for a living.
[jzta957] (score 5, diepte 0 OP) Oh I forgot to add that I have plantar fasciitis on one of my feet, which is definitely not helping. Any advice on that?
[jztqs4c] (score 4, diepte 0) Also getting older and dealing with plantar fasciitis. High end ASICS runners with custom orthotics is the way for me
[jzubeqf] (score 4, diepte 0) Still wondering how some of my 90's teachers survived in high heels.....
[jzulbgy] (score 4, diepte 0) Birkenstocks. Or compression socks with supportive sneakers. The compression socks are key.
[jzur5z8] (score 4, diepte 0) I got really bad feet, like crawl on hands and knees bad.  Swear by New Balance with roll cage technology.
[jzvfjj4] (score 4, diepte 0) Small group teaching/activities. Then get a doctor’s style rolling chair. And roll around from small group to small group. Helps with classroom management and sore feet.
[jztt6hv] (score 3, diepte 1) I have plantar fasciitis in both feet and needed surgery. Casted orthotics help. Cortisone shots. And when my feet hurt I sit down.
[jzuuk82] (score 3, diepte 3) I bought a pair of Doc Martens. The combat boots. I got them because I was going for a look. Turns out they're really good for plantar fascitis.
[jzubwy6] (score 3, diepte 1) I have a tall cart and a stool. I can keep my laptop hooked to smart board and really see the whole room.
[jzu7leg] (score 3, diepte 1) I have a pair of sandals from SAS that I can wear all day. It was only flattering style I saw in there when I went and I get a ton of compliments on them. It’s worth the money.
[jzupsd7] (score 3, diepte 1 OP) Okay you're the third teacher who's told me about SAS shoes, I think I'm sold. Thank you so much for your advice, I really appreciate it.
[jzv0uqa] (score 3, diepte 2) They are hideous - but I swear to god you will have no foot pain! 😆
[jzuq9ak] (score 3, diepte 1 OP) I truly appreciate your lived in advice and I hope your feet are better now
[jzuqgo2] (score 3, diepte 1 OP) I thank heaven I work in a very casual school!
[jzuqwom] (score 3, diepte 1 OP) Thank you, I really appreciate your good advice
[jzvf7wx] (score 3, diepte 0) Shoes definitely make a difference.  I like Clark's. Also consider compression stockings. You can get a prescription or you can save lots of money by buying them on Amazon.  When you have a break,  put your feet up, even if only for 10 minutes.  Most mail salons will give a massage with your pedicure.  If you can afford it, treat yourself. At home, sit with your feet up. The best thing is if they are higher than your heart. I have a recliner but if you don't,  try getting an ottoman and putting pillows on it to raise your feet higher. Keep a chair or stool at the front of the classroom and sit for part of the lesson.  Again,  even 5 minutes here and there is helpful.  I always had a stool and it was a treat for kids to sit on it when speaking to the class. If you are still having problems, consider seeing a podiatrist who can make you a custom insert or custom shoes. Finally, any exercises that strengthen your legs, hips, and core muscles can also help.  Try squeezing and holding your leg, butt, abdomen while you are watching tv or reading. If you have access to a pool, walking in the water and swimming if you can are helpful. Some pools have exercise classes in the water. Good luck and feel better....from a fellow sufferer.
[jzupy5n] (score 2, diepte 2 OP) My heart goes out to you and everyone suffering with hurting feet!
[jzzeyiw] (score 2, diepte 5) They're wide enough, very flat and fairly firm soled. That's really what you need for plantar fascitis. And, they make you look badass
[k005a7z] (score 2, diepte 6 OP) Thank you!! I really do appreciate this.
[jzz66qf] (score 2, diepte 2 OP) I'm so sorry you've had so much trouble, my heart goes out to you and your sore feet and I appreciate your advice
[jzvjoc7] (score 2, diepte 1) So do I. It’s all about the inserts. I buy Super Feet Athletic Green Inserts. I put them in my Hey Dudes and I’m good for the day. If I have a day where my feet hurt particularly more than any other day I wear the inserts in my Brooks athletic trainers. 

Spend money on shoes and inserts. Buy new ones each year. It’s worth it.
[jzz69on] (score 2, diepte 2 OP) Thank you so much for your help
[jztdbth] (score 2, diepte 0) 54, 5-10 and 190, really high arches.

I wear Ilse Jacobsen Tulips. They're pricey, and they make my feet feel better than any shoe I've tried as a teacher.
[jzur3tf] (score 2, diepte 1 OP) I'm so happy you found a pair of shoes that help you! Thank you for the advice
[jzuykkv] (score 2, diepte 1) I need a new brand of shoes too so I just checked these out. Why oh why are they so ugly 🤣🤣
[jzvcaaq] (score 2, diepte 3) They had a few cute looking ankle boots. But everything else looking like orthotic bowling shoes.
[jztmp4m] (score 2, diepte 0) Oh, I had plantar fascitis back when it was only about 40, that was BAD and it took almost a year to fix. 

No flat flats for sure.  Get great arch support, wide toes/shoes, etc. Ask or Google for stretches to help the plantar fascitis too. If dress code is an issue, get a doctor's note.

The first few years I dealt with it I bought shoes at an Amish store,  you know they're not going to wear bad shoes.  Kids thought it was funny but it saved me.  That store now carries more "English" shoes and I still buy a lot of mine there.  Favored brands are Clarks, Skechers, Life Stride, and Taos.
[jzwbvbu] (score 2, diepte 3 OP) Ugh you said it
[jztudbd] (score 2, diepte 0) I sit and teach from my desk as much as possible.
[jzuvkev] (score 2, diepte 2) I do as well. If I ever got pushback, I'd get a 504.
[jzu7soi] (score 2, diepte 0) Have you tried wearing sneakers with gel/memory foam inserts?
[jzu83a6] (score 2, diepte 0) I’ve had feet problems and back problems in the past. I find changing the shoes I wear each day helps. My feet are comfortable in Sketcher ballet flats. I like New Balance sneakers. I know a teacher who wore croc flats. This week I wore a $6 pair of men’s Tommy Hilfiger flip flops I got at TJ Maxx. I can’t wear women’s flip flops. For me it was trial and error and not wearing the same shoe two days in a row.
[jzvdq47] (score 2, diepte 1) Seconding Birks, they're pretty much all I wear in the classroom unless it's too cold/wet to have my toes out. Fortunately living in the southeast that's not terribly often.
[jzvxtrc] (score 2, diepte 2) Birks are all I wear! Sometimes I wear my Brooks running shoes too. I definitely need supportive shoes too. Can’t understand teachers who wear heels or flat sandals all day like that
[jzurnni] (score 2, diepte 0) I clouds are great but pricey. If you have a way to get a foot message that’ll help but yea, you’ll eventually get more used to being on your feet all the time and how to give yourself breaks/sit down when you’re getting sore.
[jzz6te0] (score 2, diepte 1 OP) Thank you for your lived in advice
[jzuuzcj] (score 2, diepte 0) Rockport make fantastic walking shoes that look dressy. New balance walking shoes also very comfortable. Look for shoes with a big “box” because they have removable insoles and you can replace them with extra comfy ones.
[jzz6mby] (score 2, diepte 1 OP) Thank you!
[jzzw1kz] (score 2, diepte 2) I've found that if you're in the age group you are in, no one will bother you about what shoes you wear, btw, so do not fret about that. Also, take breaks (sit, stand, stretch, etc.) as you are able.
[jzuz69n] (score 2, diepte 0) I wear Merrell, Rockport, and Crocs.
[jzv4cso] (score 2, diepte 0) As others have said, don’t wear dress shoes. I used to and laughed to myself when I saw others all dressed up and sneakers.

I work in hard, textured floors for a non-slip lab room and it’s rough on the feet. I also circulate desks so I switched to sneakers. Some days I’ll wear dress shoes just because I want to step up my attire… I regret it every time.

Sneakers
[jzv9meh] (score 2, diepte 0) I keep an extra pair of shoes under my desk and when my feet get hot start to hurt, I switch to a cooler pair.
[jzz6y2i] (score 2, diepte 1 OP) This is actually fantastic advice and I appreciate it
[jzvdk71] (score 2, diepte 0) Doc Martens.
[jzz6pme] (score 2, diepte 1 OP) You're the second person who said that, and certainly I would like to walk around in cool boots more than hideous looking orthotic shoes
[jzzcvlk] (score 2, diepte 2) Ngl the cool factor is a big plus haha
[k0406ri] (score 2, diepte 3 OP) Boy oh boy am I going to take that advice about breaking them in, thank you friend.
[jzz6kig] (score 2, diepte 1 OP) I do swim, and I appreciate the validation that it does help! Thank you for inspiring me to go to the pool today
[k024z61] (score 2, diepte 2) You're welcome!
[jzvn90r] (score 2, diepte 0) I bought [these](http://UIN Women's Slipper Comfort Canvas Fashion Travel Art Painted Shoes Wide Toe Casual Household Slip On Mules Malaga https://a.co/d/gySmxSx). They helped so much, I ended up getting another pair. I am 46 and overweight as well. They are not cheap, but they were worth the investment.
[jzvssev] (score 2, diepte 0) Invest in a pair of Hoka sneakers. A wear sneakers almost everyday. I had plantar fasciitis from wearing fancy dress shoes even Dansko’s didn’t help! Or you could get inserts. Invest in the best ones.
[jzvswfg] (score 2, diepte 0) I worked at a school that moved from an old factory building with carpet over plywood to a brand new school with vinyl tile over concrete, and my feet and legs were immediately killing me.  All sneakers, all the time.  No more cute flats.  And consider a comfort mat in any place you stand a lot.
[jzvvm3v] (score 2, diepte 0) I am older but have always been fly! I like to dress up for school and swear by Clark's shoes. I also like Abeo, Life stride and Naturalizer. I teach elementary school and am on my feet all day. I do keep sneakers under my desk on a rare occasion that my shoes start to hurt more than normal. Good luck to you! I also swear by nightly foot soaks with Epson salt when necessary.  Take care of yourself.
[jzweqz8] (score 2, diepte 0) Compression socks and supportive insoles. 

I developed a heel spur because of being on my feet on cement floors all day.
[jzwhi34] (score 2, diepte 0) I went to the “fancy” shoe store and got a professional fit.  It’s not just size, but how you stand and walk.  I’ve worn wide shoes forever, only to find out I need a wide toe box but nothing else is wide.  I also found that zero-drop shoes work great for me.  And believe me, this is shoe vocabulary I’d never even heard of before!  Anyway, the shoes are so great that I’ve continued to go there and pay more - my feet are still sometimes tired at the end of the day, but they no longer feel like they are unmolding from the shape of my shoes for the first 30 minutes.
[jzwlxcd] (score 2, diepte 0) I use a height adjustable stool (like in a doctors office) and installed silicone wheels (for a smooth glide). I don’t use a desk and am always rolling around the room to assist students. I reserve my standing time to short lectures at the board. New shoes help. To preserve my shoes I keep several different pairs in my classroom. I wear my rugged every day shoes to work and swap them out in the classroom Mr. Rogers style.
[jzyddkx] (score 2, diepte 0) Definitely good shoes (I wear Taos, Vionic, Birkenstock, Clarks, Dansko) but I also bought a high stool that I perch on when I'm talking to the class for any length of time.
[jzyg33a] (score 2, diepte 0) I love my Dr. Scholls. Love them.
[jzz6441] (score 1, diepte 4 OP) Ooooh I want this to be true because I love the look
[jzuxgaz] (score 1, diepte 1) I’ve been dealing with Metatarsalgia lately (similar shoe needs to PF) and have had to completely revamp my shoe situation. I’ve found most of these on Poshmark at a huge discount. I’m not made of money. Haha. Here are my recommendations:

Recovery sandals: Hoka Ora Luxe or Oofos depending on the arch support needed. I put these on the second I get home and they’re totally worth it. 

Flats with good arch support: Birkenstocks, Vionic makes moccasins that feel like a cloud. 

Insoles with deep heel cups: Tread Labs makes good ones you can find on their site and on Amazon. They’re not cheap, but they’re better than buying custom.
[jzyaii5] (score 1, diepte 1) You can look up ways to tape the arch so it doesn't painfully over-stretch.
[jzz5mnr] (score 1, diepte 2 OP) I've never heard of this and I appreciate your advice
[jzw903g] (score 1, diepte 2) All better now as far as that goes. The reason I mention wider shoes is because I also got a bunion and that's no fun either. Getting older is quite a ride.
[jzuq2d5] (score 1, diepte 1 OP) Thank you for your advice!
[jzuqkev] (score 1, diepte 1 OP) I have not but I will!
[jzuqt7y] (score 1, diepte 1 OP) NO THANKS!!!!
[jzuqny9] (score 1, diepte 1 OP) Good advice! Is there a brand of compression socks you like?
[k0cmbgl] (score 1, diepte 2) I ordered mine from target and they are called “dr. Motion” nothing fancy and about ankle height. They sometimes have them at Marshall’s/TJ Maxx too
[jzz6d9x] (score 1, diepte 3 OP) Definitely can't wear heels, but I also don't want my hideous toes to show.
[jzz6ewo] (score 1, diepte 1 OP) Oh hugs to you
[jzurl5w] (score 1, diepte 0) I swear by Zcoil shoes. You can get clogs, Mary Jane type shoes, or sneaker type shoes. I prefer the covered coils. I have invested in multiple pairs since i am on my feet all day. They are life-changing!
https://zcoil.com/shop/?gclid=CjwKCAjwr_CnBhA0EiwAci5sinnfE1mFOScHlXqyjg5EHwPWN4tyiJOfTFWQ5lkrNI0BB2RyRQ6NDRoCQykQAvD_BwE
[jzus0nu] (score 1, diepte 1) You can purchase these inserts to customize your shoe and help with the Plantar Faciitis.
https://zcoil.com/z-fit-custom-arch-insoles/
[jzz6rj4] (score 1, diepte 2 OP) Thank you so much for your advice
[jzz6hbh] (score 1, diepte 1 OP) Thank you!
[jzuv32j] (score 1, diepte 0) That was my first year. Got me some boring walking shoes (*Addiction*, by Brooks, or similar), and that did it.
[k0403f2] (score 1, diepte 3 OP) Oh yes even our principal wear sneakers and casual clothes, thankfully that's not a problem but I really appreciate your advice and support.
(14 reacties met lagere score weggelaten)

=== THREAD lfvfau ===
SUBREDDIT: r/nursing
DATUM: 2021-02-09  SCORE: 131  REACTIES: 91
TITEL: The patriarchy took my feet 🦶
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gmp2t80] (score 42, diepte 0) Why do my fingers get black? Better have some more chips and cola in the middle of the night.
[gmodaao] (score 31, diepte 1 OP) You have a choice to live how you want to live, but to pretend that you can be “healthy at every weight” is idiotic.

Fat acceptance is just giving people a way to feel better about their bad choices.
[gmoka1y] (score 31, diepte 0) What a weird thing to say. I'm not on Twitter, but is this a new thing the fat acceptance groups are into? 

I'm just so confused, but I really shouldn't be. People love to be in denial.
[gmp048g] (score 30, diepte 1) Fat acceptance shouldn't be a thing, but I'm not saying it to shame you. HAES is misleading and is attempting to sell the idea that people can be healthy at every size, which may be true moment to moment, but overall will more than very likely prove to be untrue.

"Fat acceptance" should be renamed body positivity and self love, as "fat acceptance" gives the idea that being overweight or obese is okay, when medically, being obese is one of the biggest risk factors and contributors to many chronic diseases and costs the patient and health care system much more to care for an obese patient with chronic diseases that has to visit the hospital more often on average than one of a healthy weight with no chronic illnesses from their weight. 

No one deserves to be shamed, mocked, bullied, or the like because of their body, that's called prejudice. Promoting self love, self acceptance and reassurance, and body positivity is great. Promoting the idea that being obese is healthy is not.
[gmodau1] (score 26, diepte 2) Being fat is unhealthy. End of story. 

Fuck the HAES bullshit and fuck anyone who perpetuates it.
[gmogcvt] (score 24, diepte 7) That isn't fat acceptance and is not what HAES is. HAES is people saying that you can be morbidly obese and healthy which is just straight up not true.
[gmoeleg] (score 23, diepte 3) Fuck the HAES bullshit and fuck anyone who perpetuates it.
[gmoexrn] (score 20, diepte 5) Quit spreading harmful bullshit, like HAES and fat acceptance. It's just as asinine and full of bullshit as the anti-vax movement.
[gmogac9] (score 19, diepte 2) No we do know obesity is the cause for a whole host of health issues including heart disease and strokes which are real bummers. 

Sure there are some diseases that can make it a lot easier to put on weight but they are much more rare. The most common reason people are overweight is because poor diet. There is a reason that it's a bigger issue in the US than other countries, we don't mysteriously have worse genetics that predispose us to the rare diseases that cause weight gain. We just eat like shit.
[gmoikcx] (score 19, diepte 4) https://academic.oup.com/eurjpc/advance-article/doi/10.1093/eurjpc/zwaa151/6105192


No, literally being overweight makes you less healthy. It's not rocket science and it's well established. If you can find a source that is better than a peer review that looked at more than 500,000 people and their activity levels then I'd like to see it. 


It's not a correlation, stop using that word when you clearly do not know what the fuck it means. 


Again, there are some rare conditions (like PCOS) that can lead to being overweight, but that is the vast vast minority of people who are overweight. And exercise helps lose weight but it's ultimately on diet. If you break your leg and can't walk for 6 months then you need to modify your diet, most people don't and they gain weight but there is nothing stopping you from not putting on weight just because you can't move as well. 


I'm not about to sit here though and listen to some bullshit that you are out of depth on. If you want to think that people who are overweight are that way because of things outside their control that's on you, but for me I'll follow actual medical literature and try to keep my patients a healthy weight.
[gmohtau] (score 19, diepte 9) "Persuasive, peer-reviewed evidence abounds that – hold onto your stethoscope – fat is blown out of proportion as a health risk and may actually confer some protection against early death" 

Also Linda Bacon
By the way that entire above statement is total bullshit since she hasn't been able to actually prove anywhere that being overweight is in any way healthy. 


And it's not stigmatizing to say the truth. Trying to hide that being overweight leads to worse health outcomes is not going to do anybody any good. I'd much rather have a patient who has their feelings hurt but is able to face reality and put work in then one who thinks their lifestyle is perfectly healthy but then dies at 40 from a stroke.
[gmqo923] (score 19, diepte 0) As a man, I apologize for your skyrocketing A1C and your necrotic diabetic ulcers. It's all part of our plan for world dominance
[gmohy95] (score 16, diepte 9) "The real enemy, then, is not weight, but weight stigma. Fear of fat is much more harmful than actual adiposity, distracting us from true threats to our health and well-being. Let’s stop the demonization and switch our emphasis to Health At Every Size®" 

Another winner of a quote from that org. 

No actually fat is a lot more harmful to your health than fear of fat.
[gmoiazq] (score 16, diepte 9) https://academic.oup.com/eurjpc/advance-article/doi/10.1093/eurjpc/zwaa151/6105192


Here is a nice article (actual peer reviewed research with more than 500,000 participants) showing that you actually cannot be healthy at any size. Linda bacon is 100% a person trying to sell a book and an image to make money off people who are overweight and want to feel better about it. It not medicine and it is not welcome.
[gmpd4cy] (score 11, diepte 2) >To be fair, the correlation between weight and health is just that- correlation. We don't actually know if obesity is a cause for a lot of things.

This is such a reddit comment. It always amazes me how many redditors think they're so smart to be able to post some variation of "correlation does not equal causation". Do you think by saying that you're smarter than the people who have done decades of actual research in the field? You think these researchers are so stupid they don't have any idea how to tease out confounding factors, etc.? That they should just read all the reddit comments instead? If you read the studies that have been posted here they literally explain how they support causation.
[gmphvgh] (score 11, diepte 0) I wonder if there is like an equivalent to this idea but for smoking or alcoholism. Pack years are just a number, man! Health at any number of pints per day!
[gmr2wo6] (score 11, diepte 0) Ah yes the patriarchy is why your BP is 180/120 and your glucose is a God damn roller coaster
[gmpbcg1] (score 9, diepte 0) Is that a satire account? I'm too lazy to check for myself.
[gmr27gu] (score 9, diepte 1 OP) Thank you for checking your privilege.
[gmq9ch0] (score 7, diepte 0) I think this may have gotten eaten in a thread, since things got heated while I was typing it. So, hopefully this is OK...my response to those of you that think weight stigma is a good thing, or that weight alone is a true indicator of health status.

  Before I go further, we need to define what “fat” is. The majority of the medical community uses BMI to define obesity. BMI in and of itself was never meant to be used in a medical capacity. It started as a way to group people by risk level for life insurance companies- by people who had no medical background. While those risk levels by BMI were shown to relate to mortality, it’s difficult to prove whether this indicates that people were dying specifically from conditions brought on by high BMI (Nuttall 2015). 

With that said, it would be valid to claim that high BMI is a predicative indicator for mortality- if nothing else, a warning sign- if the measurement itself wasn’t so flawed. It fails to account for fat content vs muscle mass. It fails to account for bone density. It fails to account for fat placement (two women identical in height and weight will score the same, for instance, even though one has a beer belly and the other one happens to be slim with large breasts). Nuttall’s study also points out that BMI fails to account for a variety of other factors. Genetics/family histories are quite significant: “Recently (McPherson 2010) it has been reported that more than 50% of susceptibility to coronary artery disease is accounted for by genetic variants”. BMI also fails to account for socioeconomic status. It seems self-evident, but even I wouldn’t argue that a person on a diet of fast food is in the same condition as a person eating a diet of lean proteins and fresh greens, even if they were the exact same height and weight.  It’s disingenuous at best to claim that you can predict or forecast an outcome based on a flawed system of measurement. 

In any case, the Nuttall study does find an increase in mortality in people with a BMI above 30. Those numbers changed markedly depending on the location of body fat, which BMI does not account for. Others (Flagel et. al 2013) found that mortality only increased at a BMI 35 and above, compared to normal or “ideal weights”. 

The bottom line is that, yes, size and weight DO impact your health, but they don’t do so accurately according to the way that we currently define them. It’s not as simple as to say “Fat people bad”. 

Let’s assume for a moment though, that you’re both correct, and that all fat people are unhealthy and that it’s simply because they’re lazy and have no willpower. Their problems will be solved by \*diet and exercise, right? If only. The fact is that weight loss is not shown to meaningfully decrease risk factors (Tomiyama et. al 2013). Miller (1999) found that almost none the subjects in their study maintained weight loss past 3-5 years. 

\*There *are* diets that work for specific medical purposes, such as ADA, DASH, low sodium for CHF and Keto for epilepsy…just not any proven to work for weight loss long term

What this means is that we’re currently advocating to our patients for treatments that *don’t work*. Would you encourage anyone to undergo a surgery that had such a small chance of success? 

The psychological impacts of this kind of shaming can be significant (APA 2017). In particular, women can be so ashamed that they postpone important appointments in hopes that they’ll lose weight first and avoid being bullied (Fontaine et. al 1998). The aforementioned bullying is more than just patient perception; that too is supported by research (Scwartz et. al 2012). 

More than that, weight stigma has been shown to detrimentally impact diagnosis (Hebl and Xu 2001) and treatment of illness (Phelan et. al 2015). While they are associated with the maligned HAES, Bacon and Aphramor (2011) were able to demonstrate more positive health outcomes when the approach didn’t simply focus on weight. While there’s definitely an element of “voodoo” shit advocated by HAES, what they get right is the idea that the number on the scale shouldn’t be your only focus, and as a healthcare provider, you shouldn’t get so caught up in obesity that you miss something important. 

I also won’t claim to be perfect on this either. Obese patients are difficult to care for. They’re more physically taxing on the body and often require specialized equipment. When I worked EMS I could often feel my back start to twitch the moment I walked into a 4th floor apartment to a 300+ pounder. Pannus care is gross, and that moisture breeds yeast. It’s certainly not ideal, and I’m not at all saying that the people on “My 600 Pound Life” are healthy humans. 

While yes, weight and BMI do play a role in overall health, it’s a much more complicated issue than “fat people are unhealthy”, and even if that’s the approach you take, the treatment to that issue is also complicated and not nearly as cut and dry as you seem to think it is. Patients of all sizes and walks of life deserve compassionate care grounded in current research and not tainted by personal bias. They don’t need to be shamed and belittled for something that many have little control over.

I’m not going through and listing sources in APA format for a reddit post, but below you can find full text links to everything I’ve cited here. 

[https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4890841/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4890841/)

[http://www.dishlab.org/pubs/2013%20Compass.pdf](http://www.dishlab.org/pubs/2013%20Compass.pdf)

[https://jamanetwork.com/journals/jama/fullarticle/1555137](https://jamanetwork.com/journals/jama/fullarticle/1555137)

[https://www.researchgate.net/publication/13601855\_Body\_Weight\_and\_Health\_Care\_among\_Women\_in\_the\_General\_Population](https://www.researchgate.net/publication/13601855_Body_Weight_and_Health_Care_among_Women_in_the_General_Population)

[https://onlinelibrary.wiley.com/doi/full/10.1038/oby.2003.142](https://onlinelibrary.wiley.com/doi/full/10.1038/oby.2003.142)

[https://onlinelibrary.wiley.com/doi/full/10.1111/obr.12266](https://onlinelibrary.wiley.com/doi/full/10.1111/obr.12266)

[https://pubmed.ncbi.nlm.nih.gov/11477511/](https://pubmed.ncbi.nlm.nih.gov/11477511/)

[https://www.sciencedaily.com/releases/2017/08/170803092015.htm](https://www.sciencedaily.com/releases/2017/08/170803092015.htm)

[https://pubmed.ncbi.nlm.nih.gov/10449014/](https://pubmed.ncbi.nlm.nih.gov/10449014/)

[https://nutritionj.biomedcentral.com/articles/10.1186/1475-2891-10-9](https://nutritionj.biomedcentral.com/articles/10.1186/1475-2891-10-9)
[gmqvllk] (score 7, diepte 1) You still did not support your claim that weight and health are simply correlated and not directly linked. And the article I posted earlier cuts into a lot of what you put here, namely that when controlling for activity levels bmi becomes much much more important for overall health.



And I care deeply for my patients. I do not at all hate fat people, I hate people who say being fat is OK or that it doesn't directly relate to your health in a negative way.


There are more options than diets for people struggling to control their weight and whole medical programs. And even if you're overweight because a medical issue it doesn't magically take away the health risks from the weight.
[gmr3ui1] (score 7, diepte 1 OP) I had a patient a couple of months ago that had a BP of 215/144. 

It was glorious. Just had to share
[gmpkas1] (score 6, diepte 9) Linda Bacon is a moron
[gmqc9yq] (score 6, diepte 0) What the actual fuck lmao
[gmr4mym] (score 6, diepte 2) It always amazes me that people will do mental gymnastics to avoid taking responsibility for their health. At least cigarette smokers don't pull this...at least not in my experience
[gmrshu4] (score 5, diepte 0) Ah yes. The "all my life decisions are somebody else's fault."

I know these patients well
[gmqw2m2] (score 3, diepte 3) Which as it stands should be mocked.


If you want to have a body positivity moment then great, have it be about loving yourself and taking care of yourself. Don't turn it into "medicine is wrong because anybody is healthy no matter how they live" because that's just straight up wrong and dumb.
[gmqvt2u] (score 3, diepte 2) And occurs in much higher rates in people who are overweight and obese.


In fact weight loss is one of the biggest ways to get newly diagnosed T2DM under control.
[gmpv68a] (score 3, diepte 0) Lol where did u find this
[gmrkumg] (score 3, diepte 0) As a diabetic... this is hilariously wrong. I hope nobody ACTUALLY thinks this.
[gmvzrnk] (score 3, diepte 3) No I mean legitimately the HAES and fat acceptance movements say that they take health at any size as literal. 


"Persuasive, peer-reviewed evidence abounds that – hold onto your stethoscope – fat is blown out of proportion as a health risk and may actually confer some protection against early death" -Linda Bacon founder and person who runs the HAES movement. 
That statement by the way is false, the evidence shows pretty clearly that fat leads to health issues. 


They also believe that people have "natural body weights" and it's unhealthy to go below those. What is a person's natural body weight they cannot answer though, they just know it's "unhealthy" to be below it. We aren't talking actually being underweight, they think some people are naturally just obese. 

They also think that forcing weight change is only unhealthy, that it just makes you physically and emotionally worse off. (which again, total bullshit). They aren't talking about laxatives and crash diets, they think that any effort to reduce weight is unhealthy. 


It's a movement made up of honestly insane people.
[gmrylzf] (score 2, diepte 1) There is a whole belief that health problems associated with overweight are not caused by the weight itself but either by societal stigma or by dieting.
[gmrkcar] (score 2, diepte 2) Do you have a better measure to use that can be applied to all patients?


We generally try to not throw the baby out with the bathwater in medicine.
[gmrn5dp] (score 2, diepte 0) It's the frequent repeat HAU admissions for DKA that really bug me, for purposefully not following an appropriate diet and not using their insulin despite adequate supplies and the knowledge of what the consequences could be if they are non-compliant
[gmtn7y8] (score 2, diepte 0) reddit's complete inability to detect when a post is obviously made by someone who hates the group they're posing as is irritating. Lol. Promoting healthy activity levels and healthy diet without an unhealthy obsession with forcing the scale down using laxatives and crash diets *is* better for weight loss and health.
[gmtvbrz] (score 2, diepte 1) Which is only half of what HAES and fat acceptance movements are about. 

The other half is saying that weight doesn't play an impact in your health and that there aren't any issues with being overweight.
[gmqscbl] (score 1, diepte 2) The original post is false and dangerous and I think it's fake. 

I think the original post on Tumblr, or wherever it originated, was made by someone mocking fat acceptance. 

The title " the patriarchy took my feet" mocks the fat acceptance movement.
[gmqwfvu] (score 1, diepte 4) I didn’t?
[gmr3k7w] (score 1, diepte 5) If you are supporting the fat acceptance movement as it stands now then you are.
[gmr5z2p] (score 1, diepte 6) You don’t get to decide that for me. 

As an analogy, I support psychology as a field and I think there are a lot of bad studies, bad interventions, and harmful misinformation propagated by people in the mental health field. But I’m not going to throw out the whole concept of promoting mental health because Freud did too much cocaine.

Being fat is ok. Even if it was harmful to health it would be “ok”. Being “ok” means that it does not lessen their worth as a human being. Meeting people where they are at and listening to them helps get buy in from the patient. American culture is obsessed with weight loss even if a person is at a healthy weight, and a lot of times taking the focus off of weight and on to quality of life helps with that stigma.
[gmr7hef] (score 1, diepte 7) You can't pick and choose what parts of a movement to support if you support the movement. You can't say "well I support these things they did but I'm going to ignore those things"


If you have to explain what the word OK means in a specific setting then you aren't using it correctly and are just saying that being fat is acceptable, which if you are in medicine it isn't acceptable to say that it's fine for people to be unhealthy. 


Is it also "OK" for people to smoke, drink themselves to death, overdose? I would argue that it isn't "OK" and that we should be doing things about those issues. It doesn't make them less of a worthwhile person to say they are engaging in unhealthy behaviors.
(25 reacties met lagere score weggelaten)

=== THREAD zf3u88 ===
SUBREDDIT: r/Frugal
DATUM: 2022-12-07  SCORE: 1859  REACTIES: 90
TITEL: 3D Printed keyboard feet for 60 cents at library
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iz9v1z2] (score 208, diepte 0 OP) Broke off one of the feet stands of my wireless keyboard/mouse combo.   The set was purchased for about $20 and I could only find $10 replacements.  Considered purchasing a new keyboard but then would lose the combined functionality of one USB transmitter.   Also I’m very used to the size of my keyboard.  

Remembered my library has 3D printing and found the  copy needed and picked my fave color
Purple.   Total cost $0.60.  They feel stronger and fit really well.
[izamnxc] (score 193, diepte 2) I’m a librarian and we have an entire lab of stuff that’s free to use! (You have to get trained first then you just sign up for time to use it). Two 3D printers, a resin printer, laser engraver, sewing machines, embroidery machines, vinyl cutter, heat press etc. 

I wish more people knew how awesome libraries are 😀
[iza4ij6] (score 148, diepte 1) Your library has a 3D printer?!
[iza87rb] (score 49, diepte 2 OP) Yes, I can’t use it personally. But I sent the file over to them and they printed it for me and I picked up.  My library allow jobs that take up to approx.  2 hours to complete. These two little feet took about an hour.
[iza50zo] (score 37, diepte 2) A lot do!
[izaok2h] (score 36, diepte 3) Where is your awesome library of toys?
[iz9z47r] (score 34, diepte 1) Just an FYI: If it's in a part of the dryer that gets hot you might need to use a particilar type of filament.
[izapv33] (score 31, diepte 3) That is super cool. My local library only has random tools - the more useful of which seem to be booked out years. (And that’s why I now own a radon detector, boroscope, and thermal imaging camera… or so I say.)

A library that doubles as a small scale maker space is cool as hell.
[izai58s] (score 31, diepte 0) Ladies and gentlemen... Libraries must be protected and funded at all costs. Especially if you can't afford your own 3D printer.
[iz9x34w] (score 28, diepte 0) I have a 3d printer. I need to find the designs of the small plastic hinge things for my tumble dryer. Robbing bastards want £25 to replace. For a bit of plastic!

I'd do it myself but don't know what would be the simplest software to design them on.
[izaip9s] (score 23, diepte 5) Thanks. I obviously don't know how all this stuff works. You're the first person to explain how to get the file.
[izaabup] (score 12, diepte 1) This was my first functional print. "Wonder if I can find the STL... OMG, that's it exactly!"

Found the original piece buried in my laptop bag a year or so later. It's the backup now.
[iza882m] (score 12, diepte 0) Nice job. I searched online and someone showed you could use parts from those metal binder clips. Also I learned about baking soda and super glue to put plastic back together. Done some type of reaction to make a bond as strong or stronger than original plastic. I've used it more times than I can count.
[izcjdoy] (score 9, diepte 4) My county library calls it the “library of things”.
[izb0mnh] (score 9, diepte 4) Or they can both be fine options? Why do y'all have to make a competition out of the best way to replace keyboard feet? For fucks sake
[iz9vkdi] (score 9, diepte 0) That's amazing! Great resource from your library!
[izahv0o] (score 7, diepte 4) He probably means like an STL file, the 3D model you actually feed to the printer to tell it what to print.
[izbldt9] (score 7, diepte 3) My library is really nice but has none of the cool stuff. 

No video rental and no connection to Hoopla/Kanopy. No stuff like 3D printers or pots/pans like I’ve heard about elsewhere.
[izag2wb] (score 6, diepte 3) When you say you sent them the "file", you mean you sent a picture?
[izaz8g8] (score 6, diepte 2) 3D printing is a better way to keep your existing keyboard that's fully functional and leave the thrift store keyboards for someone that needs to replace their broken one :)
[izai8gb] (score 6, diepte 0) Don't check out your local library but also your neighboring libraries. Some don't have their services locked to their residents. I can get museum passes at a village library which aren't restricted to village residents but anyone who asks. They don't advertise that fact but it never hurts to give a library a call to ask.
[izbfmer] (score 5, diepte 3) Where? Every library I've ever been to barely even has usable Internet connections, let alone a friggin 3d printer.

Not hating on libraries personally I visit mine every other week, it's just that the most out there services they offer are classes on excel, game nights for teens, and about a few hundred romance ebooks, and yet I see on this sub post after post of libraries offering nearly everything someone might need to use occasionally but not often enough to justify purchasing.

I can hardly even imagine having a library offer power tools and having a 3d printer available for usage.
[izc8e98] (score 5, diepte 4) I'm in Michigan and my local branch has a 3d printer plus a lending library of tools and things like sewing machines. It's going to be dependent on what type of funding your library gets. I'm from WV originally and even that county library has one even though the population is a lot smaller. Maybe you should speak to your library about getting one!
[izaqfn9] (score 5, diepte 6) These days, the workflow is pretty easy.

You could design something (say, using an online app like [tinkercad.com](https://tinkercad.com)), and export to a supported file ("stl"). The library would take that file, run it through a program that slices it into thousands of layers ("gcode"), and send *that* file to the printer. That file is actually sort-of readable by eye -- it's thousands of lines that effectively give X,Y,Z locations for the 3d printer nozzle to go to.
[izbkvki] (score 5, diepte 3) More like a labrary! Awesome.
[izawi52] (score 5, diepte 2) 3D printers aren't the exotic expensive things they once were. Thanks to a swell in manufacturers you can get a basic working 3D printer for about $200. And for the material, the most common stuff can be found for $20 and under for a Kilogram (which is actually a pretty decent amount since most objects will print mostly hollow).
[izbm02a] (score 5, diepte 2) It's a small bracket thing to hold the hinge firm and helps seal the door. It's stupid and so obviously intentional that they've made such an important part so brittle and easily breakable as the replacements are criminally priced for such a small piece of plastic.
[izam2rc] (score 5, diepte 1) I've been modelling for 15 years and I think probably the simplest software to start (that's free) is OnShape. Modelling up little basic shapes like plastic bits really is pretty simple. Modelling is not one of those skills that takes a career to learn, really you can get pretty proficient within a week or so.
[iza8hgm] (score 5, diepte 1) I replaced the feet on mine with the little metal handles from a binder clip. Works great if you already have one lying around
[izad0gd] (score 5, diepte 1) You just have to make sure you use regular super glue (the fluid,  runny stuff) and not the gel type.
[izai4s3] (score 5, diepte 0) I definitely misunderstood this at first and thought you were bragging about stealing the keyboard feet from your local library’s keyboards. That’s super cool!
[iz9up6p] (score 4, diepte 0) Omg that's a great idea!
[iza8ml6] (score 4, diepte 2 OP) Happy Cake Day!
[izbenz7] (score 4, diepte 3) The quandary: a lot of the functional stuff is better using FDM (generally more durable), while a lot of the fun stuff comes out better with resin (finer detail).

...and that, kids, is how I ended up with two 3D printers, which is one of the least frugal things I've ever done.
[izan2pp] (score 4, diepte 1) It works: https://www.reddit.com/r/techsupportmacgyver/comments/c95o4h/broken_keyboard_feet_binder_clips_to_the_rescue/
[izc3adl] (score 3, diepte 4) My local branch doesn't have one, but the main library for the county has 3d printers. I've never used it personally but I did see it mentioned on their website. For reference, I live in Northeast Florida.
[izcbycm] (score 3, diepte 5) I mean I would but my local library nearly went under during the pandemic. The only reason it didn't was because the local school district election happened to be 100% mail in and the vote was nearly unanimous in favor of providing some property tax revenue to the library.

It was a record high voter turnout for the  school district vote. Usually it's single digits but we saw about half the city cast votes because of it being mail in ballots.
[ize646q] (score 3, diepte 7) I’m officially old because I don’t even recognise this discussion as English.
[izai6tl] (score 3, diepte 4) No, they mean a 3D Printable File, which contains a 3D model of the object you want to print.
[izb1kab] (score 3, diepte 4) How to send it you'll have to ask your library (or whoever is printing the file). You'll also need to know whether to slice it before sending it to them.  Slicing is done by turning a 3d model into a set of layers the 3d printer can use as instructions. Its done through software like Cura which is free but some printers require you to use a specific software. To get models, if you know how to use 3d modeling software, you can develop them yourself. If you can't use 3d modeling software, you can either pay someone to make a model for you or download them for free on sites like Thingiverse. A personal favorite of mine is 3d printed "Chain mail"
[ize1jcv] (score 3, diepte 6) Our library calls ours a “maker space” and they have a ton of different machines you can use. They just require you to do their orientation to use them. Just if you need help with what to look for!
[izbf408] (score 3, diepte 4) Not to mention all the things you have to print for your 3d printer.
[izazzpu] (score 3, diepte 3) I was at a thrift store and saw keyboards missing all sorts of parts, including a wire to a USB male end. Salvaging parts is better than spending hours making a new piece of lower quality.
[izb2cjq] (score 3, diepte 1) > Considered purchasing a new keyboard but then would lose the combined functionality of one USB transmitter.

A tip I've found helpful since finding it, for Logitech keyboards that use the unifying receiver(has an orange star like thing on it), you can use "logitech unifying software" from Logitech to pair new devices to a receiver

(Not even sure if your keyboard/mouse is Logitech, and I'm definitely all for saving things from ewaste when possible!  Just figured it'd be a helpful tip for people that come across it)
[izan3g9] (score 3, diepte 1) I'm a designer by trade but know close to zero when it comes to 3D modeling. That said, I've had the easiest time designing on TinkerCAD. It's a free online 3D modeling program that practically a baby could use. Truthfully I've been meaning to start trying to learn fusion again (same company, more complicated) but it's hard to leave something that takes so little effort. Try out their tutorials or use it to edit stls you find online. Dead simple, no weird or complicated buttons, and a great way to get your feet wet.
[izarwyw] (score 3, diepte 1 OP) [Feet File - Logitech K270](https://www.thingiverse.com/thing:1360979)
[izcu9so] (score 2, diepte 7) Do you live near a microcenter? I got an ender creality pro for $100, and they seem to have the deal regularly with their new customer coupons.
[izaos12] (score 2, diepte 3) How did you find the file/send it over? I’d love to get into this
[izdgpbj] (score 2, diepte 5) Yea i should check out my library again--- Brilliant idea OP thanks !! --but... how to make a copy of the left hand side foot to replace the missing righthand side keyboard foot...
[izbfmy5] (score 2, diepte 3) I'm so bummed out that the two libraries near me both say the other one is my library. I can't afford the "out of county" membership.
[izb7597] (score 2, diepte 2) My library has a whole lot of books. And some audiobooks. And movies. That's it. 

My old library had an overhead projector.
[izbbbjx] (score 2, diepte 2) Yup, lost the foot on my Corsair K70 and just looked it up. 10 minutes later I had a replacement foot. 

3d printers can be frugal as hell if you use them enough or you have access to one on the cheap (like OPs library).
[izarv27] (score 2, diepte 1) >onsidered purchasing a new keyboard but then would lose the combined functionality of one USB transmitter

FWIW, that looks like the foot of a Logitech keyboard, and many logitech devices are part of their "unifying" series where you can actually reprogram keyboards and mice to different USB receivers. So you very well might have been able to replace the keyboard and still only have one USB.

That being said, I like your solution better.
[izd7o7y] (score 2, diepte 1) I think I have the same keyboard with the same broken feet. Any chance I could pay you to print two new feet and mail them to me? 😭
[izf7cob] (score 2, diepte 3) I hate when manufacturers do that shit. Do you think a replacement could be made of metal?
[izadobi] (score 2, diepte 2) This is the answer.
[izaye54] (score 2, diepte 2) Can you provide some source? 


I'll Google search it also and if I find something post it as an edit.
[izconw2] (score 2, diepte 1) I have used the parts from metal binder clips several times and they work fine.
[izar4y9] (score 2, diepte 0) STL file?
[izau8g9] (score 2, diepte 0) I'm not sure what I expected when I read the description but for whatever reason this wasn't it lol
[izauyiz] (score 2, diepte 0) Nice, a binder clip works just as well. Just remove the metal part that you use to open the clip.
[iz9uei5] (score 1, diepte 0) Hey Kolibri17, thank you for your image contribution! We like to have discussions here on r/frugal. To avoid your post being removed; 

**If you're posting something you made, repaired or refurbished**, please leave a top-level comment under your post explaining how or why you went about it, how much it cost, how much time it took, etc., and share the recipe or materials needed. 

**If you're posting a general image**, please leave a comment explaining how it relates to frugality and any other details you'd like to share! Thank you for participating in r/frugal!    


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Frugal) if you have any questions or concerns.*
[ize8hpc] (score 1, diepte 3) That’s so smart!
[izaylz6] (score 1, diepte 2) HAPPY CAKE DAYYYYYY
[izchf02] (score 1, diepte 2) Happy cake day!  This is the first time I get to see what the cake looks like and wish someone happy cake day!
[izchofo] (score 1, diepte 2) The one nearest me does. So does the elementary school that's about to open in the neighborhood.

The future is here.
[izcrb7l] (score 1, diepte 2) Mine does as well! For mine you fill out a form online and attach the file you want printed. Then when it's ready they email and you pay by weight and time it took to print. You can pick it up at any branch you just have to say which one in the form. They also have a whole maker space in one of the libraries which is where I think they do the printing, but using the printers is beyond my skills. 

Also happy cake day! I hope you're having pizza 😁
[iza72yy] (score 1, diepte 0) I need this! One of those broke off of my keyboard at work also. Darn planned obsolescence!
[izamiiu] (score 1, diepte 0) I use the little stick on circles that go under chair legs to not scratch floors
[izc45dv] (score 1, diepte 1) [example](https://i.imgur.com/DTHaRat.jpg)
[izc4dtu] (score 1, diepte 2) Yes
[izavs61] (score 1, diepte 0) I did the same thing a few years ago. I just superglued the broken part back on and it works just fine.
[izaw8ni] (score 1, diepte 0) …I gotta check in with my library for all these funky gadgets
[izbcbcd] (score 1, diepte 0) Looks like fun. Do you have course recommendations to go from 0 to this without spending time sifting through many many YouTube tutorials to find a nugget that is useful ?
[izbdi9w] (score 1, diepte 0) I lost that exact foot!  I used the two metal handles from a binder clip to replace mine.
[izbf6ul] (score 1, diepte 0) Crosspost to r/peets
[izbgo3l] (score 1, diepte 0) I duct taped a lego.  Works suprisingly well.
[izbimy2] (score 1, diepte 0) Where were you a month ago when I needed a feet for my Logitech keyboard. I paid 10 bucks for it. 😞
[izbo9j0] (score 1, diepte 1 OP) Return it!!!
[izbj2f6] (score 1, diepte 0) My trunk wouldn’t open anymore, so I printed the broken piece at the library. Would’ve cost $25 dollars new, I printed it for free!
(10 reacties met lagere score weggelaten)

