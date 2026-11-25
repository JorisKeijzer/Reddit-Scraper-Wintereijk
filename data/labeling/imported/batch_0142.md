# Label-batch batch_0142

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
Schrijf het resultaat naar `batch_0142.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 18npko7, evd3xy, 33lbos).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 18npko7 ===
SUBREDDIT: r/BabyBumps
DATUM: 2023-12-21  SCORE: 27  REACTIES: 63
TITEL: Doctors are stumped about my foot pain
POST (source_id=post):
I’ll be 39 weeks tomorrow and know the end of pregnancy is near, but I am so discouraged in the last trimester by pain in my hands and feet that is only getting worse.
I have been wearing carpal tunnel wrist braces since Thanksgiving. While my right hand is somewhat improved, a few days ago I lost the ability to straighten my pinkie finger on my left hand. This is so strange because the hallmark symptom of carpal tunnel, and the one thing that made me hopeful that this would go away once baby is born, is that the media nerve only affects the thumb, index, middle and ring fingers. Indeed those fingers have been numb for me, but why is the pinkie joining in the action now? Is it something unrelated?
I wish I knew to have taken my rings off before the swelling got this bad. Doctor mentioned this week that they could cut them off. (Apparently this would happen in a c-section?)
But the real medical mystery is in my feet, which have been aching and numb for months, completely unrelated to third trimester swelling. Doctor says she hasn’t seen this in a patient before. At 6 months, I went to PCP for the foot pain. He did blood tests and referred me to a podiatrist and a physical therapist — both of whom basically said they couldn’t do anything while I’m pregnant. It has gotten so much more painful, and I hate that I am resigned to start from scratch, paying all these providers again, if symptoms persist after delivery. 
I don’t have gestational diabetes; my bp is consistently low/normal; and I have been “taking it easy,” lying horizontal with my feet elevated, since Thanksgiving. 
When I do go for a walk, I wear insoles and orthopedic shoes. Neither foot looks any different, but the pain is miserable, particularly in my right foot. It feels 24/7 like I am badly blistered after a night dancing in too-tight stilettos. Or that I survived a fire.
I’m sorry for rambling. Any advice would be appreciated.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kec2muw] (score 56, diepte 0) Different nerves can be involved in carpal tunnel, you could also have nerve compression higher up at the elbow or shoulder that's affecting pinkie fingers. I had this in my first pregnancy!

As for the foot pain, maybe nerves too? Compression around the hips or knees? 

If it's any consolation my nerve pains went away pretty much as soon as the swelling and water retention went away after delivery. You're so close!
[keca8gl] (score 39, diepte 0) I am baffled that the podiatrist AND the PT said they couldn't do anything; honestly, those statements make me nervous about the treatment plans they'd offer.

You are likely suffering nerve pain in your feet. Babies are heavy, and they displace so much as they grow, and sometimes things don't shift neatly. I'd highly recommend looking for a PT who uses massage to treat nerve pain. My PT uses a technique called myofascial release and it's been wonderful for me.
[kec2x30] (score 10, diepte 1 OP) Thank you. Giving me some hope!
[kec5gr1] (score 9, diepte 0) I had this my first pregnancy. Had to wear wrist braces, hurt so bad to even type, feet swelled up huge and hurt. I had zero issues or complicatations. Once baby was born it went away. My feet took away for the swelling but my husband would rub my ankles and that would help a lot.
[kecdrye] (score 8, diepte 2) I was also going to mention nerve compression is possible in your legs. For three plus years I had ankle pain and swelling in one leg that got worse if I drove more than 30 min or did any amount of walking. After many tests and multiple doctors it turned out to be peroneal nerve compression that had to be fixed surgically. 

So it may get better when your swelling and blood volume go back to normal but if it keeps happening definitely go see an orthopedic doc
[kecc69x] (score 7, diepte 0) I developed a numb spot on my foot during my second pregnancy in 2021. It’s been slowing going away and is much smaller today.
[kecopsd] (score 6, diepte 0) During my first pregnancy I had issues with both of my pinkies and ring fingers going numb no matter what position I slept in. It is due to ulnar nerve compression at the elbow, same mechanism for carpal tunnel in pregnancy. Your foot pain also sounds like a nerve issue related to the fluid shifts. I’m sorry you haven’t been able to get any relief! But the end is near and this should all go away shortly after delivery. 

- neurologist on my 2nd pregnancy and already having ulnar nerve issues in first trimester 😑
[kecvw7z] (score 6, diepte 0) If you are having trouble straightening your pinky, this sounds suspicious for a trigger finger to me. That is where one of the flexor tendons in your hand gets caught in an attachment to the hand rather than sliding through smoothly. It's very common! Pregnancy causes all kinds of inflammation, so I would not be surprised if it were rearing its ugly head. 

As for the feet, my differential generally includes referred nerve pain from back, sinus tarsi syndrome, morton's neuroma, lower extremity swelling. There are a variety of things that can cause that, but definitely seems neurological if you have numbness. You could get an bilateral lower extremity EMG/Nerve conduction study to determine source of numbness which is a bit of a mean test, but a helpful diagnostic tool for providers. Mention this to your primary care doctor and see if it's possible if it persists after delivery. I say this because EMGs generally take a while to get in, at least in my practice it was(I don't think it would happen before you deliver!) Best of luck to you and I hope you feel better soon!
[kec4jfi] (score 5, diepte 0) I wonder if the foot pain could also be nerve related? I once had bad sciatica that caused excruciating foot pain because of the way the nerve was pinched I guess. Stretching helped a lot, and hopefully for you delivery helps too!
[keenrd4] (score 5, diepte 1) After getting a run around with my primary care doctor while sick for 3 weeks, an urgent care doctor was like “unfortunately no one will want to treat you while you’re pregnant” like… she heard me out and gave me meds and treatment but was just being brutally honest that all other docs were gonna defer everything to my OB. It sucks.
[kec93wf] (score 4, diepte 0) I’d see an acupuncturist if you have the extra money to spend. Mine has kept me virtually pain free from Carpal Tunnel for 9 years and helped so much with the seemingly random pregnancy aches and pains. 

You’re so close to delivery that it may not be worthwhile right now, but if you breastfeed, that will also limit western medicine options after delivery. 

There are also fluid retention / swelling points for acupuncture. The first time I had mine treated, I peed out over 2 pounds of weight over 48 hours and felt so much better! My acupuncturist did say that the fluid retention points have diminishing returns into third trimester - now that I’m 36 weeks they still help, but it’s not a miracle like it was around week 20.
[kecb0u0] (score 3, diepte 1 OP) Wow good to know
[kecqm42] (score 3, diepte 1) I second this. I go to a chiropractor who specializes in pregnancy and uses the Webster method. I had severe mid back pain 2 weeks ago and my obgyn actually recommended I see a chiropractor. I was surprised as I’m currently seeing a pelvic floor PT and expected my obgyn to recommend a physical therapist. Turns out, it definitely had to do with a misalignment of my spine due to the growing belly. They checked my spine then even did a scan of my spine to show where there was compression of my nerves - exactly where I was experiencing muscle pain. I got 3 times a week to get micro adjustments now, to realign my spine as my baby grows. 

They have me lay on a special pillow with a belly hole in it, and are super gentle. Best part? I sleep better and have no more pain.
[kecqrez] (score 3, diepte 0) During my first pregnancy I had awful back pain. At one point I couldn’t walk for a few days. This pain started almost immediately when I got pregnant. Way before baby was big. Everyone I talked to about it shrugged it off. There was no way my pain could have started that early they said. 

Your pain is real and should not be ignored!

My pain went away after birth. Hopefully the same for you. I did get planter fasciitis as well though. Wearing really good running shoes all day even inside is the only thing that helped.
[ked0b72] (score 3, diepte 0) The foot thing could be tarsal tunnel (carpal tunnel but in the feet) and/or plantar fasciitis. I have both and they are rough. Suggestions that could help without medical intervention that you could do while pregnant -- calf stretches to loosen the muscles and make sure you are wearing shoes that have GOOD support. Like thick soles, think orthopedic/running shoes. The toe shouldn't be able to bend back. Also wear shoes anytime you're walking -- even if it's from bed to the bathroom (Crocs are great for this).

I DID have to get steroids to really help get over the hump though, because I was having such a bad flare this past time, but I was 6 months postpartum. My podiatrist also suggested a topical NSAID (it's over the counter), but I'm not sure about using it while pregnant. 

My shoe recommendation (if you want one or just to see the style) are Kizik Athens or Roamers. 

Again, not a doctor, but different shoes and some stretches MIGHT help at least relieve the leg pain. As far as arm... Carpal tunnel braces that keep the thumb secure, avoid repetitive movements... And hope that once you give birth it goes away?

Sorry for the long-winded response, but I hope I offered a little help! Good luck!!
[kedaosv] (score 3, diepte 0) Orthopedist here. I would go see a hand surgeon for the pinky thing and go see a foot and ankle surgeon for the foot problem.

Inability to straighten a finger could be trigger finger, which can also happen in pregnancy. It can often be treated with just a steroid injection. Really bad carpal tunnel symptoms can also be treated with steroid injections which are safe in pregnancy (which I’ve learned very few people know about…seems like everyone just suffers…)
[kec4adf] (score 2, diepte 0) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10564038/#:\~:text=Median%20Neuropathy%20at%20the%20Wrist,60%25%20depending%20on%20study%20methodology.
[kecjiip] (score 2, diepte 0) 4 pregnancies here including twins 2 months ago. After I deliver I have severe foot pains that usually lasts 3-6 months.
[kecn3px] (score 2, diepte 0) I had wild nerve stuff going on all over including carpal tunnel, femoral nerve compression, and things that just radiated all over. My hands looked deformed, and I couldn't feel my baby at my fingertips the first month after she was born, which made me very sad. But gradually over the course of about 3 months, it all receded and now I only have a few twinges in my left thigh on occasion.

I feel for you. The nerve stuff was something I hadn't even heard about until I was in it. And it was overwhelming.
[keczj5v] (score 2, diepte 1 OP) I definitely have some plantar fasciitis issues, but I don’t have flat feet. I am also hyperflexible pre-pregnancy and was wondering if relaxin (btw, who named this hormone? JK Rowling?) just loosened me up too much.
[kedfjcr] (score 2, diepte 2) Ohhhh you're hypermobile as well? Absolutely that's probably causing the issue, and not many medical professionals pick up on it, especially in pregnancy. 

You don't need to have flat feet to have this issue, I don't, but when I walk or stand my arch collapses, which shows that I have week feet and legs. This can cause a lot of pain. There are exercises you can do, I'll link some for you. It's okay if you aren't up to them while pregnant, but if you nurse the relaxin will stick around, and it will help. Also being hypermobile means you're more likely to have these issues, so knowing what to do will help a lot. I went from needing to wear my orthotics in my slippers at home to only needing them for long walks. 

Sorry the professionals didn't help you, so fucking frustrating that we have to go online for advice instead of being helped by the people who have the expertise. 

Here's the resources. Most of them refer to barefoot shoes a lot, which though I recommend once you're on top of your foot pain, aren't what I want you to focus on. It's just the barefoot shoe community are all about strengthening your feet. And I want you to be careful with these, especially the balance and hoping ones, while pregnant. (Basically you want to look at all in the first link, and work up SLOWLY to the ones in the second link.) 

[https://anyasreviews.com/foot-exercises-transitioning-barefoot-shoes/](https://anyasreviews.com/foot-exercises-transitioning-barefoot-shoes/)

[https://www.fitnessblender.com/articles/barefoot-running-injury-prevention-foot-and-ankle-strengthening-exercises](https://www.fitnessblender.com/articles/barefoot-running-injury-prevention-foot-and-ankle-strengthening-exercises)

I also recommend [getmomstrong](https://getmomstrong.com/freebie/subscribe-to-slam-opt-in/?&utm_term=getmomstrong&utm_campaign=Get+Mom+Strong+Brand+Search+2023&utm_source=adwords&utm_medium=ppc&hsa_acc=7723208191&hsa_cam=19592719862&hsa_grp=146171314715&hsa_ad=645676316282&hsa_src=g&hsa_tgt=kwd-1210198396693&hsa_kw=getmomstrong&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQiA4Y-sBhC6ARIsAGXF1g5yZ-8vtTsN4nFG0lgBwQAGjML-NRSmAA6F55nAIxz_v5-Kob6U4dMaAp9JEALw_wcB&gclsrc=aw.ds) for after pregnancy. Most of my leg and core exercises that my physio gave me are in her program. Designed for mothers and pelvic floor safe. She has a pregnancy program too, but at 39 weeks with pain maybe just wait until after. 

Let me know if you have any questions, I'm really happy to help.
[kedkgdy] (score 2, diepte 4) YUp, I wasn't able to work out at all in pregnancy. I'm pretty active outside of it, so it was a huge change for me. Don't push yourself, especially now. Your body is clearly having a really hard time, and you're nearly at the end. 

I do hope I didn't give you any pressure, just wanted you to have all the info you need to start rebuilding after, when you're ready. For now just get through the day, I remember how painful pregnancy is! It gets so much better after the baby is born!
[kecnku4] (score 2, diepte 0) Did he test for RA and lupus? The foot pain sounds like something I experienced recently (not pregnant any longer) and my doctor ordered blood work to rule these issues out. I also had severe carpal tunnel in pregnancy they persisted until a month after I gave birth. Not saying this to scare you, but for you to realize it may take a while to go away!
[ked0pgu] (score 2, diepte 2) I’ve breastfed both my kids for > 1 year and don’t have any pain/discomfort! I hope you’re able to do what works best for you and find some pain relief relatively quickly.
[kecpcwc] (score 2, diepte 0) Do you have sciatica? I have a bulging disc in my lower back and when it flares up I get numbness in my feet.
[keejqi8] (score 2, diepte 2) Hello! I'd just like to confirm that it is very possible for back issues to refer pain in the legs without any back pain being present. If you get similar pains in both feet, it is very likely that the source can come from the middle, in other words the spine. All of the nerves that travel down the legs come from the lower back. A lot of lower back issues are due to lack of mobility or stability, the latter being quite common during pregnancy. Hope you can find a physiotherapist who will look closely into this with you! As a side note, hand issues in a similar way can be referred from the neck.
[kecrv9l] (score 2, diepte 0) I don't want to upset you, but I had terrible carpal tunnel like yours that did not feel better until 3 months pp. It actually deformed my left wrist and made it look like there was a hole on top of my wrist when I'd bend my hand downward. When I got pregnant again, I went to a kinesiologist (he's also a chiropractor) because I was terrified of carpal tunnel again, and he actually fixed it. No more hole and I'm 29 weeks currently with no sign of carpal tunnel and my husband says he remembers me having it at this point last time. So I agree with the others saying to seek alternative treatment.
[ked0zv8] (score 2, diepte 1 OP) Thank you. I know things are different every pregnancy but i am now quite terrified of ever getting pregnant again. I’ll see about a kinesiologist.
[kedf2ox] (score 2, diepte 1 OP) I appreciate it. I have some plantar fasciitis stretches that I was doing in second trimester. I will try to revisit them.
[ked2v67] (score 2, diepte 0) It sounds like pregnancy induced plantar fasciitis. I would always get that when pregnant and only in one foot.
[ked5oht] (score 2, diepte 0) /r/askdocs
[ked6bhp] (score 2, diepte 0) Back in college, I kept losing feeling in my feet and legs. I went to a bunch of specialists but we didn’t solve it until I had an MRI done of my back. I had a bulged disc which I think was pressing on the nerves. I started doing stretches and continue to do stretches if it starts again. When I was pregnant, I noticed it happening again probably from the extra weight.
[ked781r] (score 2, diepte 0) I developed severe carpal tunnel during my pregnancy and both of my big toes became severely numb. I ended up having carpal tunnel surgery on my right hand 6 weeks postpartum because the pain was so bad. Then my left hand 6 weeks after that. 

However the numb big toes lasted months after pregnancy. I’m not sure when it stopped but I feel like every so often (currently 10 months post partum) I still sometimes feel the numbness but it’s definitely not as bad. It’s just unexplained and so odd. 

Not sure if this helps but just wanted to share my experience.
[ked7u6l] (score 2, diepte 0) I had such horrific foot pain from the added weight and also the way I walk being altered with the “waddle”. It got better so soon after birth! Definitely keep advocating for yourself but just hoping to give you some hope that it could be a benign pregnancy symptom.
[kedh0vw] (score 2, diepte 2) I hope you get some relief soon!
[keel1ku] (score 2, diepte 0) Hi! I had a very healthy pregnancy, but I also experienced this in my third trimester. 

Around 36 weeks my hands, wrists, and feet started to tingle and ache all the time. My feet were so painful. Sometimes it was a dull ache, sometimes sharper tingly pain. 

Good news is it COMPLETELY went away within a week of giving birth.
[keewkuk] (score 2, diepte 2) We are going on 10 months of successful breastfeeding. I lost a lot of supply when my period came back so now we combo feed but she still nurses for meals 2x a day.
[kegktnn] (score 2, diepte 0) Okay, I might be completely off, but..

A few months ago, I wasn’t pregnant, but trying. And I suddenly started having terrible pain in both my hands. It was horrible and I kept putting on bandages and suppprt to help my wrists and hands.

Then I was googling why it’s happening (I thought I had carpal tunnel too) and it came up that more vitamin B6 does it sometimes. So I stopped taking my prenatals which had Vitamin B6, and poof the pain disappeared the next day!

It might not be the same thing for you, but just wanted to share in case it is..
[kec07id] (score 1, diepte 0) BabyBumps users and moderators are not medical professionals. Responses do not replace contacting your medical provider. You should always call your provider with any concerns.

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/BabyBumps) if you have any questions or concerns.*
(31 reacties met lagere score weggelaten)

=== THREAD evd3xy ===
SUBREDDIT: r/loseit
DATUM: 2020-01-28  SCORE: 426  REACTIES: 63
TITEL: Hiking while fat....losing toenails, massive blisters.....it wasn’t the socks or the shoes or the orthotics....it was the fat and it didn’t take getting to my goal weight to end the misery....just losing 10lbs helped.....(a different kind of success story)
POST (source_id=post):
I’m a 5’ 6.5” women who got up to around 245lbs. I started losing weight and around 210lbs I went on an overnight backpacking trip that was a lot of ups and down and a 4500ft elevation gain and by the end of day 2 my feet were shot. Giant blisters, lost 3 toenails and bruising around all my toes. I used moleskin and duct tape and the tips. Was blistered anyway. Took 7 months to grow all my toenails back. 

I thought it was the shoes. I thought it was the socks because that’s what everyone says. Next summer I got new shoes and new socks that are guaranteed not to blister and the same thing happened except I just lost 2 toenails this time and the blistering and the bruising wasn’t as bad. 

I came back from that hike and happened to have an appointment with my doctor the next day. I hobbled in wearing flip flops and she took one look at me and told me I needed to see a podiatrist and probably get orthotics. I dutifully went and got the orthotics but they were so rigid I could hardly walk in them so I never wore them. 

Fast forward to summer 3 of regular backpacking and I’ve gotten down around 200lbs, same shoes, same good guaranteed no blister socks from year 2 and lo and behold.....it was the first summer I made it through with all my toenails in a long time. 

Sometimes it really just is the weight. As much as we try to be body positive no socks or shoe changes could overcome the amount of pressure I was putting on my feet and toes. 

I’m around 195 now. It’s been a long, slow weight loss process with some ups and downs. 

But I’ve kept my toenails every summer for about 4 years now and every pound I lose makes it easier on my feet and ankles and knees.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ffv4upl] (score 109, diepte 0) 'keeping all of your toenails' is the ultimate NSV
[ffvaxnc] (score 34, diepte 1 OP) So true! So sexy when painted. So weird when gone.
[ffvdjze] (score 31, diepte 3 OP) I’ve recently been to a neurologist for some wicked headaches that aren’t responding to anything. 

He wants to investigate that I might have a spinal cord fluid leak. 

He was very gentle in telling me it might be weight related. He’s the first one that even mentioned it. 

My former primary care has prescribed me Saxenda. My new one in my new town isn’t super supportive and even told me I need to slow down my weight loss goals. Doesn’t like low carb or intermittent fasting. 

🙄🙄🙄🙄
[ffvb0cy] (score 23, diepte 1 OP) Isn't that crazy? And no one wants to say.
[ffuy74d] (score 16, diepte 0) Go you! This is an awesome story!
[ffve5oc] (score 16, diepte 0) Nice! I also backpack and I'll spend a fortune on gear to cut a couple of lbs when in reality I really just need to cut 30lbs off my gut. Easier said than done, do good for you!
[ffv34e0] (score 14, diepte 0) We use nylons and wool socks over the top, game changer. Even if my shoes get soaked, the blisters stay at bay.
[ffvns7v] (score 14, diepte 3) I get shin splints from just walking!  I’m not doing all that well with weight loss.  But I keep at it.
[ffwd0f8] (score 13, diepte 1) I used to wonder why my hiking setup was never as ultralight as the experts but eventually the penny dropped - the bigger you are, the bigger your clothes, tent, sleeping mat, sleeping bag etc need to be (then add in being female which means you feel the cold more so need more layers, though there is a saving on food weight) so I was never going to be hiking with a tiny rucksack like theirs. Cutting your bodyweight has a lot of knock on benefits for backpacking.
[ffw9lyw] (score 12, diepte 3) It never occurred to me before reading your comment that of *course* shin splints can come from being too heavy to run. Brain blast over here. That explains why I magically got shin splints my senior year of high school for my last season of lacrosse, when I'd never had them for the 10 prior years of playing...coincidentally also the year I first hit my highest weight of 185. Thank you for enlightening me lol
[ffv11f3] (score 8, diepte 1 OP) Thanks! Having toenails is so nice! I didn’t realize how much I would miss them until they were gone.
[ffv3if3] (score 8, diepte 1 OP) I wear WrightSocks and no problem these days. Same concept. Double layer that rubs on each other and not skin. 

Miracle.
[ffvknap] (score 8, diepte 4) Have you read 'The Obesity Code'? Lots of interesting information in there...and may help figure out your headaches. Also, if you haven't tried it (I'm a migraine sufferer), go to a chiropractor.  I started seeing one and my headaches have diminished tremendously! I wish you luck!
[ffvo308] (score 8, diepte 3 OP) I get it. I was impressed with his decorum.
[ffvo64h] (score 7, diepte 1 OP) It’s taken me to beautiful places and it’s something my husband and I love to do together.
[ffx9uq9] (score 6, diepte 3) Wait... I'm just realizing this might be why I hate running and my dad and sister don't.... Their shins don't hurt. If I don't hurt, I enjoy running, but most of the time I hurt. It's because Im 50lbs+ overweight. Well shit.
[ffvsmko] (score 6, diepte 0) Sigh. Even at a very healthy weight, I've lost toenails from backpacking. Most hiking boots assume that your second toe is much shorter than your big toe, and mine are close to the same length. I have a big trip planned this summer, and my toenails are finally healthy after the last big trip. Guess I should do some research on better boots for my foot shape.
[ffv1oku] (score 5, diepte 0) I use leukotape to cover the spots on my feet that blister before I go for a hike, it’s amazing.
[ffv63vx] (score 5, diepte 0) Keep going sister!
[ffvnxuh] (score 5, diepte 5 OP) Nope. But I just downloaded The Diabetes Code and started it last week.  It’s two years newer. It’s given me the resolve to carry on, even without doctor support.  

I’ve been going every two weeks. Sigh. Might need a lobotomy next.
[ffvy362] (score 5, diepte 0) I thought it was just me, haha!  Went on a desert hike about a year and a half ago and lost both of my big toenails shortly after, took them such a long time to grow back. Here's to never having alien-like feet again.
[ffwm18z] (score 4, diepte 1) Hahah I always have this problem! My second toe is actually a little bit longer than my big toe and it leads to so many shoe mishaps. Basically my shoes are always a size bigger than they need to be because of that stupid toe.
[ffwohix] (score 3, diepte 1) I just use leukotape on my hotspots. I heard people raving about it for years, and finally broke down and bought some on Amazon. Now I get what all the fuss was about.
[ffvazbu] (score 3, diepte 1 OP) On it!
[ffxz2nj] (score 3, diepte 1) Lol this is me. I have a great ultralight family setup for me, my partner and our kid, now I need to get ultralight to use it well. It’s one of my primary motivations!
[ffvhdlk] (score 3, diepte 0) That’s great keep up the amazing work! This definitely happened to me at the start of my weight loss journey. I took up running at about 215 lbs and lost both my big toenails within the first few weeks . Thought it was the shoes, but I have switched back to my old shoes now at 125 and have no problems at all for the past 2 months.
[ffviuqt] (score 3, diepte 1 OP) Novel, isn’t it? I like having toenails.
[ffw2i0e] (score 3, diepte 0) You are doing great! It's amazing how such "small" changes can make a huge difference! I have super curvy toenails and suffer a lot on long hikes.
[ffwo9c4] (score 3, diepte 0) From someone who hikes regularly at altitude with lots of up/down: keep losing weight and it only gets better. You'll start seeing improvement in how easily you can breathe and in how your heart feels after steep climbs.

I packed in thirty pounds of gear the other week, and thought "holy shit, this is heavy!" Then I realized that even a year ago, I was carrying around twice that weight ON ME. No wonder the climbs seemed hard!
[ffwtxe8] (score 3, diepte 0) Awesome! Keeping hiking!
[ffx20jz] (score 3, diepte 0) I've actually lost many toenails while hiking no matter what weight I was, and I've ranged from 200+ lbs to 150 lbs. They always get so damaged on the really steep downhills because I have high arches and my shoes don't support them properly, so my toes end up jamming into the front of my boots. HOWEVER, I will say that hiking is significantly easier (although still very challenging) and more fun when you weigh less.
[ffv3jf2] (score 2, diepte 1 OP) Never heard of it. Looks like good stuff!
[ffwoks8] (score 2, diepte 2) Seconding the rec for leukotape. That stuff changed my hiking life. It's blister prevention and can be used with gauze for blister first aid all in one.
[ffw2l8d] (score 2, diepte 6) There's is a study that came out recently where they are investigating whether or not green LED lights help migraines. Results so far are extremely positive.

You should try it.

Sit in a dark room with a standard green LED light every day for 2 hours. Apparently for most people who tried this, their migraines are significantly reduced or went away within the month.

Google for reference.
[ffw5jku] (score 2, diepte 7 OP) Sigh. Unfortunately they aren’t migraines. I’ve had migraines all my life and this is something else. 

Neurologist thinks I might have a spinal cord fluid leak. 

I’ve got an MRI Friday.
[fg06x01] (score 2, diepte 8) Late to the party here, but MRI will show for sure. Not sure what kind of headaches you’re having, but I was having wicked primary stabbing headaches for years until I finally broke down and saw a neurologist.  

Turns out I had a Type I Chiari Malformation. I had decompression surgery a year ago and am 100% headache free (well, those types of headaches, anyway) 

Imaging is a good first step, hoping you get answers soon!
[fg0avgp] (score 2, diepte 9 OP) This gives me some hope. I’m about to cut my own damn head off. It’s been no answers for years. I’ve tried and failed several migraine meds to get to this point. 

This neurologist is great though. I finally feel like I’m in good hands.
[ffyjbit] (score 2, diepte 5) Great advice on the shoes and rower. Thank you! I've learned over the last 2 months that if I start by running 1x per week and building slowly while doing yoga and swimming 1-2x a week I'm Not putting as much pressure on my legs. In the past I've always gone straight to distance runs and tried to get to 3 miles in 3-4 weeks. I started at thanksgiving and have done at most 2.75 miles running and that has helped a lot. 

I'm an ex-competitive swimmer so building strength and cardio in the pool is the most intuitive for me.
[ffy201a] (score 2, diepte 2 OP) Haha. Love this. Good luck!
[ffw1zwo] (score 2, diepte 1 OP) God no. Misery. 

WrightSocks have been a miracle for me!
[ffwrf9i] (score 2, diepte 0) I love this so much. Probably the biggest reason I started fighting for my health was because I discovered hiking and a love for being in nature. Carrying the extra weight up a freakin' mountain is brutal. Like you, I went to the doctor to try and fix what was only really going to get better when I lost some weight, gained some muscle, and had a better handle on my body. 

To touch on the concern about doctors who blame weight for everything: I had an amazing doctor when I started who never mentioned weight, took my concerns seriously, believed me and helped me, but would also give me the statistics on blood pressure in people who are active 30 minutes 3x weekly and ask that I come back and tell him that I was meeting that bar.
[ffx1dt3] (score 2, diepte 1 OP) That’s a lovely way to do it. 

I recently moved and switched doctors and my new one told me I should work to lose 10lbs this year. 

Me: Lady, I am not taking that up a mountain this summer. 

My thighs and legs have never bothered me because they are so muscly. And they have hauled me to some beautiful places.
[ffx1kg9] (score 2, diepte 1 OP) Light and airy is not a concept I’m familiar with but I look forward to getting acquainted!
[ffxzyaa] (score 2, diepte 0) Way to keep it going! I used to blame anything and everything but my weight. Back, knee, ankle, and foot problems that started out with acute injuries but never healed and became chronic—when I lost the weight, they all magically alleviated.
[ffy1qox] (score 2, diepte 1 OP) It’s a hard reality to face.
[fg68vw1] (score 2, diepte 0) This really gives me hope! I have bad feet that make running near impossible and walking long distances very hard and I've been to all kids of doctors who could only sell me €200+ pairs of shoes I couldn't afford.

I then lost 25 lbs and I can now suddenly walk at least twice as long in the same shoes I already have. I hope to be able to take up running in another 25 lbs!
[ffy1yjw] (score 1, diepte 2 OP) Like actually being able to find clothes that fit......

I’m currently around an XL for most clothing brands like Outdoor Research (finally got a down jacket) but for years I wore my husband’s rain shells. They were way too big but at least they covered me.
[ffziloz] (score 1, diepte 3) So true. I'm wide at the hips, so even men's clothing often isn't big enough. All those lovely serious outdoor brands and I can buy hardly anything from them! Instead of rain trousers I have a rain kilt and that works great. Everything else is Craghoppers or Mountain Warehouse which is a budget brand that goes up to large sizes.
[ffy27wf] (score 1, diepte 2 OP) Try the WrightSocks. They’ve been amazing for me.
[ffxz8ot] (score 1, diepte 1) My plan in the future is trail runners — better, bigger toe box.
[ffy26z0] (score 1, diepte 2 OP) I like Altra for that. A lot of thru hikers use them. My husband forced me to throw out a pair that were full of holes but they were **so comfortable**.

I didn’t hike in them because I needed ankle support but I lived in them for everything else.
[ffy2gun] (score 1, diepte 3) Oh man. I have salomon boots because I need ankle support sometimes but... my zero drop Merrills are what I strongly prefer and are way more motivating to get out there. Lol I need some sort of combo boot/trail runner
[ffy563m] (score 1, diepte 4 OP) Sigh. It’s a problem. I would love high ankle Altras.
[ffwip3z] (score 1, diepte 0) Body Rubbage as a larger individual was torture .... Inner thigh burn etc ....
[ffx03po] (score 1, diepte 1 OP) I’ve never understood hiking in skirts but even at my thinnest I didn’t have the thighs for that.
[ffx0te9] (score 1, diepte 1 OP) I have had that **exact** same thought. Isn’t it wild? We are so careful about weight. Analyzing this piece of gear vs that piece for mere ounces when the chub makes all the difference. 

What really hit me one time is my husband is 6’4”  and in better shape and always carries a heavier pack. Never has a problem with his feet. 

There have been times when adding up my body weight and him with his pack and his body weight had me carrying equal to or more on my feet than him. 

No wonder my nails were falling off. Poor feet! 

Still working on the altitude part. I get over 14k and get flat out loopy, not to mention just my cardio abilities going upwards.
[ffx1fpy] (score 1, diepte 1 OP) Planning routes and applying for permits this very week!
[ffwxo9d] (score 1, diepte 0) Congrats!

I had a similar problem and I don't even hike! I noticed most of my shoes were getting uncomfortable as I was having arch pain. I thought the heels and shoe inserts coupled with my high arches were too blame. Then I lost 10 lbs and suddenly the same shoes were as comfy as could be. And to think I was "only" 27 lbs overweight at the time! I'm at a normal BMI now and I practically feel light and airy at times.
[ffz4gli] (score 1, diepte 0) I don't know much about hiking, from the comments it sounds like losing toenails is relatively common. How does that happen?
[ffz7jjh] (score 1, diepte 1 OP) For me it was too much pressure on my second toe, even though it’s not longer than my big toe. I would get blisters under the nail. 

Some blisters on the sides in the wrong socks. 

I change my socks 2x a day now when I’m hiking. Keeps them dry. 

I almost always wear ventilated boots.  Not waterproof.
[fg7cc0j] (score 1, diepte 1 OP) It’s crazy, isn’t it? 

I hope it works out for you!
[fhlq9bl] (score 1, diepte 0) I had a similar experience hiking 14ers in Colorado.  Using sock liners help with most of the issues you have.  I hiked Mt. Beirstadt and ended up losing a toe nail and had blisters on my heals down to the bone.  Not pleasant.  Couldn’t wear dress shoes for 4 months.  Wore the same boots with sock liners and had no issues.
[ffvl63k] (score -3, diepte 0) It might've been a nutrition or fungal infection or hygiene issue.  I hiked when I was that weight but I ate properly, took vitamins, got regular pedicures, wore appropriate gear, etc.  Never had an issue with my toenails.

=== THREAD 33lbos ===
SUBREDDIT: r/weddingplanning
DATUM: 2015-04-23  SCORE: 33  REACTIES: 63
TITEL: Did any of you ladies have pre-wedding depression? anxiety? cold feet?
POST (source_id=post):
I just happened to google "depression before wedding" and I am so happy to see things come up...apparently its a thing. I have been feeling completely depressed...and so stressed about this wedding that is a month away (in a foreign country also). I have been also getting cold feet out of no where, when a few weeks ago I was madly in love and couldn't wait. I just don't feel good, I feel like just going to sleep and waking up when it's over....please tell me this is normal!

edit: I am so glad I posted...feeling relieved already. You read so many things online about "if you don't KNOW hes the one" or "if you aren't excited about your wedding, GET OUT NOW" ...my cold feet are getting warm again, thank you guys for the camaraderie...

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cqm1jly] (score 19, diepte 0) I'm glad this is being talked about. I've seen a lot of "I hate my wedding" posts but no cold feet posts and I know it happens a lot.
I've gotten it but I feel like I can't talk about it because no one else does and people might think badly of me or my marriage. But it does happen and it's totally normal, even healthy. It's a huge life changing step, if people weren't nervous about it, I'd be worried.
[cqlz29i] (score 13, diepte 0) I've been rather overwhelmed by it all, personally. I keep joking with people that I am a terrible bride, because I'm not really having a whole lot of fun planning this, in fact, I kindof hate it lol. I am a really social person, and I love throwing parties and things, but even though we've done our best to keep the stress down and make this personal and reflective of us, it's still been a lot to handle and coordinate, and everyone's opinions are driving me nuts, even though I'm ignoring them. I feel bad, because while my dress is nice, and will be perfect for our day, it's not my most favorite dress ever, and I'm just rather "eh" about it. And I still would just rather go to the courthouse sometimes and just be done with it. I really do love what we're doing, the cruise will be a blast, and I absolutely can't wait to be married to FH, but I will be very glad not to ever have to do this again.

Hang in there, sounds like you have an awful lot more than me going on, I can't imagine having to try to coordinate this between countries! It will be worth it!!
[cqlyod9] (score 12, diepte 0) I think, just because of all the stress and emotions involved, weddings can have a huge effect on your mood/feelings/mental health.

I know I've personally had a couple of emotional breakdowns due to all of the stress (my FH is in another country and needs a visa to come to our wedding, for example). And I've had times where I've just thrown up my hands and been like, "You know what? I don't give a damn about this wedding anymore! Do whatever you want! You figure it out!", again, from all the stress. Whenever I encounter a serious planning issue (ex. My FH's parents can't come, and we're cutting it close for visas), I do just want to curl up in bed and have someone wake me up when everything's done so I can just show up to my own wedding. Doesn't help that I'm naturally a people pleaser and anxious person (not to mention a bit if a perfectionist), so I "give up", just to panic and remind myself that I have to do it, otherwise it's not going to get done right (or maybe at all).

I mean, I've loved planning my wedding through all of this, but I cannot wait until it's over and I can actually enjoy it.
[cqm3c03] (score 12, diepte 1) Omg the What Ifs... 

What if I become a huge bitch? What if we end up hating each other like my parents do?  What if what if what?

My FH is really sweet about those things too.  He understands my fears, and we talk about them, and I remember that I have control over those things, and I'm not my mom or my dad, and that my life is my own... And we can only just hope and work for happiness! 

I'm glad you and your FH are working together and being sweet about those things!
[cqlzj23] (score 11, diepte 0) I have so much anxiety right now that I've skipped my period entirely. 2 preg tests read negative. So I'm pretty sure it's just the stress.
[cqlzwlx] (score 7, diepte 0) I hate my wedding right now and almost called it off the other day because I have hit rock bottom. Thankfully FH understands I do have serious lows and just held me while I cried and let me get it out of my system. I am a bit better but I am still not totally thrilled with the fact it is in 28 days.
[cqm2fl2] (score 7, diepte 0) I did. About a month after we got engaged, I started having mini-panic attacks at work, not about the wedding (I was stressing about that a lot too) but about marrying HIM. It didn't help that we live an hour apart and only get to see each other on the weekends, so all week my anxiety would build up, then I'd see him on the weekend and enjoy it completely free of anxiety. Then back to work on Monday and the cycle would start all over again. 

Like another commenter mentioned, my period started getting weird too. I had two pregnancy scares in as many months, but nothing came of it. I finally switched to a higher dose pill a month ago and since then things seem to have improved.

The two things that helped with my anxiety were:

* seeing a random comment a Wedditor made about dress anxiety--she said "Whenever I have a moment of doubt, I pull it out and try it on, and I remember what I first liked about it." (quote is approximate, haha). Reading that released something in my mind--I realized that when I was getting anxious, it was based on what-if's. What if we stop loving each other? What if we just get bored? What if I become bossy? What if we realize that we don't like living together? All of those worries were based purely on speculation in my head, *not on reality*. And when I went back to "reality" with him on the weekends, all those feelings went away because I realized that what we have is what I want. 

* the other thing that REALLY helped (like, completely put a stop to the panic attacks) was talking honestly with FH about my fears. I was so reluctant to bring them up, because I didn't want to make it seem like I didn't trust him, or that I didn't want to be with him. In fact, I hadn't talked about these doubts to anybody, because all my friends know him and I felt like saying anything would be a betrayal. But one night, he asked me if I was worried about anything and all my thoughts and fears slowly came out. He admitted that he had been feeling some of the same things (less intense, but it was still good to hear that I wasn't the only one who panicked a bit). We talked through my fears and I realized that not only were they unlikely to come true based on our personalities and our history with each other, in most cases we had already discussed the issue and had made a plan to deal with it should it ever arise. Ever since, he's been really gentle with me and is always checking in to make sure I'm really feeling ok, not just saying so.
[cqmhy8c] (score 6, diepte 1) I used to love watching the wedding shows and looking at dresses and everything before I was engaged. Now that we are planning, it's become the most un-fun experience. I keep trying to think of a situation where it would be fun, like having a bigger budget, but honestly that would just give MORE options to have to weed through and decide.  I have reached a point where most things that aren't decided yet, I'm also very "eh." 

The industry make it look like the best party to plan, but really, it's the pits!
[cqm06xq] (score 6, diepte 0) I am a little prone to bouts of minor depression anyway, always have been, though not enough to medicate. I have found myself down in the dumps here and there and when my mind starts to run away with itself (I'll never be single again, being single was a huge part of my identity, I don't want to share my space, etc) I kind of sit down and wait for it to pass. Sometimes I have to do it alone, other times I make myself sit with my FH until he does something amazing or says something adorable that reminds me why I'm changing my life in such drastic ways. Still, no amount of logic in the world pulls me out of it until my brain just decides to on its own. Fortunately, it's my brain... not my heart.
[cqm29yx] (score 6, diepte 1) I'm so relieved we're having this thread. My bridesmaids are either a. Younger than me, b. Related to FH, or c. Divorced. So. I can't vent to them about being nervous.
[cqm7sdw] (score 6, diepte 0) I'd say that this is fairly normal. My depression and anxiety have really kicked it up a notch and all I feel like I can do is pray for the next three weeks to fly by. I don't want it to be OVER, I just don't want to sit around waiting anymore. I want it to be here, and not in a blushing bride excited kind of way. 

As far as the cold feet, I think getting closer to the big day really just hammers home that this is it, you're making one of the biggest commitments you will ever make in your life. Regardless of how in love you are, that's scary! Your depression and anxiety will play heavily into that fear and build upon it. Your FH's little quirks suddenly irritate you, you can't believe how he can have a certain opinion about some trivial detail, and those little things - amplified by stress and anxiety - will create that cold feet feeling. I've had random bouts of it out of nowhere as we get closer, but I just remind myself that's it's ridiculous, and I'm just overly stressed. 

I'd suggest doing active things that have nothing to do with wedding planning. FH and i go rock climbing three times a week and honestly I've never felt more free of the stress than when I'm climbing. Its also great for spending time together and remembering that this wedding is not about stress or planning or details, it's about the marriage that's ahead :) 

Sorry, kind of rambling, but i hope it helps.
[cqm4s4q] (score 5, diepte 1) I am with you on the visa issue. My FH is just coming in on a tourist one because we're only getting married and then I'm moving to him, but I am so sick to my stomach with the 'what if' scenario of being refused at immigration for some silly reason and then all these people paid all this money to fly and be with us on our wedding day... The guilt! I can't live with that guilt, man. And it's like I'm scared of jinxing everything so I still talk in hypotheticals about the wedding. It's not until he gets past immigration will I be able to relax and enjoy everything.

I'm so anxious about everything, I haven't been sleeping well lately. Yesterday I just said "fuck this" to everything I needed to do, curling up in a blanket and watched X-Files and cried because I was so tired of making decisions and people asking me a million questions wherein I have to explain shit over and over.
[cqmc84t] (score 5, diepte 0) The cold feet part is weird. I KNOW we will have a strong marriage and a wonderful life together (we already have a child together, if we can get through the first year of a baby, I feel like we can weather any storm). I keep thinking about old boyfriends, though. Things that went well, things that didn't. Tons of memories popping up. I guess it's just preparation for this final commitment...clearing out all the old stuff I might be holding on to. I feel bad whenever I inadvertently recall some happy memory with another dude, though!

But really my problem is that I am SO. STRESSED. OUT. about money. We have the money. We planned for this. Our parents are helping a little, too - which is awesome. But I have had three or four major panic episodes in the past week over the money. I feel SO guilty about spending it, I keep thinking of all the other things we could have done with it. Savings, we both need a new car, we could have just gone to the courthouse and eloped somewhere beautiful, gahhhh I just cannot seem to stop second guessing myself and I feel terrible about it all. I mean, it is like WAY too late to be doing anything different, I don't know why I even allow myself to think about it, but I can't seem to stop. It is just so expensive and it suddenly feels so dumb and like a huge imposition to everyone and I wonder if I just got carried away. I can't stop thinking about whether or not it will be "good enough" which I know is ridiculous. I worry about standing in front of all those people and having all eyes on me all day - I am super nervous about that - I don't even like being in crowds, much less the center of one! 

And then I swing back to realizing how beautiful the day will be, that it will be a memory we will cherish forever, etc etc. I feel like I'm losing my mind and will definitely be glad for May 2 to get here already. No wedding zen here...at least not yet. I am a giant ball of anxiety. I am so emotional and wish I could just chill out.
[cqm5vfd] (score 4, diepte 3) Dude, I feel you. I'm lucky that FH doesn't have to apply for a tourist visa and goes through immigration on his side. I'm actually flying over to be with him beforehand, so I can be there for the process in case there are any snafus, and it's like "Once you get through, I am going to be so relieved and celebrate on the plane ride home with ALL the mini bottles of booze!" It's just so exhausting having to explain our situation a million times to family who keeps asking. They mean well, but they don't get it. 

I can't imagine having to start grad school right after the wedding! I'm having a hard time just packing to move and saying goodbye to everyone and everything I know. It sucks to feel like I can't really enjoy anything right now. I just want to enjoy the planning process and I am so worried about everything that it's not really fun anymore. So much to do, so little time to do it.
[cqmavn7] (score 4, diepte 1) "I will be very glad not to ever have to do this again"- So True!
[cqmbgu9] (score 4, diepte 2) Thirding this....thank GOODNESS!!!
[cqm1j4a] (score 4, diepte 0) Oh, dude. People are calling me rude because I don't want to give up the one Saturday I get to sleep in. They want to throw me a bachelorette and apparently I should "just be grateful people want to do nice things for me." Right now the nicest thing someone could do for me is say "hey, I'll do your table numbers. Eat a donut and take a nap."

Also I didn't start to get nervous until we scheduled our appointment to get our marriage license, and I'm totally freaking out. I just keep imagining him at the end of the aisle and I calm down again, but good lord.
[cqm2mbb] (score 4, diepte 2) Similar situation here. Even when I've vented to my own family once, they had a variation of "Don't do it if you don't want to, don't let him rush you". 
Ugh. That's not the case, no one is rushing me, can't a girl have a weak moment once in a while? 
The worse part is that they assumed my one weak moment of insecurity was an ever present thing. Sigh.
[cqm58p2] (score 3, diepte 2) My FH is coming on a tourist visa, too. And then he's going home until his permanent residency processes, and I can't go with him because I start grad school literally two days after our wedding. Not happy.

I keep making myself sick with worry about all of the "what if"s are trying to coordinate everything with the processing times and the wedding planning and flights and everything, it's awful. And then someone comes along and goes, "Oh! Shiny ring! When are you getting married?" and I have to go, "This September. The sixth. Hopefully." and pray that they don't ask too many questions because I might just break down again (since last date we set we had to push off and that was so hard to do!). I just keep telling myself that the visa should be good enough, but I've seen enough horror stories about people being turned away at the airport after landing.

It doesn't help that my FH doesn't get that you can't plan a wedding (besides a courthouse thing) in two months or two weeks or whatever. He keeps saying, "Well, just wait until I have my visa! Or wait until I'm there! Then I'll be able to help you." That's nice... are you going to overstay your visa so we can actually have a wedding? Because this stuff takes at least six months to plan if it's not just a city hall thing.

... I think I'm going to just go and curl up under a blanket and binge watch Netflix now... thanks for the good idea, ha.
[cqm526p] (score 3, diepte 2) no way!!! Happened more than once? Oh man....You ok now?
[cqm87h2] (score 3, diepte 4) thank you :]
[cqm09w5] (score 3, diepte 0) Yeah, it's normal. I had a bit of cold feet and was anxious a while ago. I kept having doubts about the wedding. It turned out that a major source of my stress was my grad school, especially with all the projects and work going on. Once the semester was over, I was back to normal again. I'm still madly in love with my SO. I think a big part of it is stress.
[cqm7ys2] (score 3, diepte 0) I concur with everyone else, and note that SO MANY people deal with the "what ifs" or "But I don't KNOW!" and don't talk about it because it's kinda taboo in our culture nowadays. I found this site to be really helpful: http://conscious-transitions.com/blog/

She talks a lot about engagement anxiety and what ifs and why this is normal- her book is really good too.
[cqmb0zg] (score 3, diepte 1) My sister definitely had post-wedding blues. I think it made it worse that she didn't go on her honeymoon until 2 months later so she just went back to work on Monday after the wedding.
[cqmcgp8] (score 3, diepte 1) I think I'm going to have the opposite of post-wedding blues! I may not know what to do with myself, but that is FINE. I'll get to remember what it's like to have hobbies again. I am so tired of all the work and stress.
[cqmdjot] (score 3, diepte 2) Me too! OMG, I think I will be so happy to go back to real life, I won't even have to worry about getting the blues! I can't wait to be done with all this and go back to normal!
[hib6a1q] (score 3, diepte 0) I know this post is 6 years old but I am so glad this thread exists. I’m getting married in 2 days and all of a sudden I’ve been feeling so heavy but literally just a few days ago i wanted to get married right then and there. Im thinking it’s the stress + my period but I’m just glad this isn’t a unique experience
[cqms0hd] (score 2, diepte 3) So much A++. Someone asked me how it was going today, and I said it was a effing waste of time for something that's just a show for a day! I really hate dealing with emails in the middle of the day. UGH. Can't wait to resume normal life.
[cqp5hdg] (score 2, diepte 2) Yeah, I agree. "Grass is always greener", and all. That's the same thing keeping me from giving up and court housing it (that, and nonrefundable deposits); that ultimately I know I wouldn't like it as much as a "real" wedding, because that's truly what I've always wanted. It's just, being stuck in the weeds coordinating this thing is stressful.
[cqmbi6i] (score 2, diepte 1) Ha! I made mine come a week early. Thanks body!
[cqmkclk] (score 2, diepte 1) Yeah, this. I just had a few weeks of "omg what am I doing" and I've been taking care to notice the little things that I love about him, and appreciate the small moments that all add up to the big feelings. It's really helping me get through.

By the way, I am also prone to minor bouts of depression. Fist bump?
[i4snw5w] (score 2, diepte 3) Same here! I’m getting married in a week and I’m starting to get major cold feet and feeling really depressed. It’s nice to know that I’m not alone..
(45 reacties met lagere score weggelaten)

