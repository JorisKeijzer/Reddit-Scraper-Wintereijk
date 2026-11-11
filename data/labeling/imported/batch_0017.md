# Label-batch batch_0017

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
Schrijf het resultaat naar `batch_0017.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(6 threads: 11vs0rd, smmow7, 14dvttl, rd7gjs, i4s0ky, mve9xq).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 11vs0rd ===
SUBREDDIT: r/ChronicPain
DATUM: 2023-03-19  SCORE: 9  REACTIES: 31
TITEL: Chronic pain in my big toe and the ball of my foot
POST (source_id=post):
I am a 28 year old female who weighs around 52kg. For the past 20 years I have been suffering with a pain in my right foot. The ball and my big toe in my right foot are extremely painful to touch. They are swollen which prevents me from moving my big toe. It is inflamed and throbs. Because of it I cannot stand with my foot flat on the floor, I am always standing on the side of my foot. I have done this for the last 20 years. It now seems to be the case that this is having an effect on my whole foot because the pain is moving to the arch under my foot (under and inner side of my right foot). It is a constant pain, even when I am resting my foot and I get the occasional sharp pain in the arch of my foot. This seems to be having an effect on my knee, because it starting to tingle. I don’t know what triggers it, it is always there even if I wake up in the night. The best feeling is when I have tight shoes on that force my foot to be flat on the ground and when I cannot move my toe. It seems to come on when it is cold, but it can also hurt when it is warm. I do have periods where I don’t have active pain, but you could at never point press my toe or the ball of my foot even when I am not in active pain. Recently the pain hasn’t been stopping and this period has been going on for about 2-3 weeks now.
I have been to numerous doctors, but am always told that I am either imagining the pain or that my pain threshold is rather low and that is why I am in pain. I would be grateful for any ideas what this could be, thank you!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jcurh9d] (score 6, diepte 0) I’m having a similar issue flaring right now. My toe is sore and the ball of my foot stings/ burns at rest. I can’t tolerate full weight on my right foot. 

I’ve had this issue on and off for 9 years. Mine is either caused by fracturing/inflaming my sesmoids (have had both feet with hairline fractures simultaneously) or a calcium spur from AS. I’ve also had plantar fasciitis with the fracture/AS spur. I rarely get heel pain from the plantar fasciitis—it mostly impacts my arch. 

Hairline fractures to the sesamoid bones are extremely hard for imaging to capture. Mine was diagnosed at an Ortho hospital by clear X-rays, description/location of my pain, and swelling.

For a fracture, a boot can help. I use mine as my CRPS permits. 

Even if they could diagnose each instance as fracture, AS, or plantar fasciitis, doctors don’t have much more to offer, so I treat all three issues the same. 
- heating pad or ice when at rest (whichever you can tolerate and helps)
- Dancer’s pads for walking (tape in place)
- Walking boot + dancer’s pad
- OTC for inflammation
- Gently flexing my toes to prevent stiffness
- KT tape
- Arch support inserts
- Custom inserts (mine were made for plantar fasciitis with the sesamoid/spur issue in mind)

If the above doesn’t make your symptoms better, another doctor’s visit may be needed. It sucks having to fight them tooth and nail for help, but a steroid injection or torodol shot may get you on the path to healing (both have significantly reduced my healing time in the past).
[jcvifle] (score 6, diepte 0) first you have to have blood work done to rule out gout
[jcuw3zd] (score 4, diepte 2) You’re welcome! I grew up with chronic pain and know the physical, emotional, and financial drain of being bounced around by doctors so I like to share as much as often as I can. 

I forgot it in my initial list: I bought stiff-soled hiking shoes so my foot would rock more instead of bending. This is the next best substitute to the walking boot since  they don’t irritate my CRPS as much and I can wear them when both feet are flaring. The hard sole also helps keep the dancer’s pad and tape in place.

Depending on where you are, if a doctor won’t order an MRI, a low-cost standalone imaging center may be able to help. There is an imaging group in my state (US) that allows you to pay out of pocket for an MRI without an order for $650 USD. Insurance likely won’t reimburse without the doctor’s order, even if a diagnosis is given and acted on. If it is within your means and an option in your area, it may be worth it to get a report in hand.
[jcuraw6] (score 3, diepte 0) I broke my sesamoid bone that sits under your big toe knuckle. My big toe knuckle was like a golf ball when I initially did it. It took an MRI (I think...this was 7 or so years ago) to diagnose it because the bone is so small. I ended up getting the bone removed.
[jcut0qc] (score 3, diepte 1 OP) Thank you so much, this is the most helpful response I have received in the last 20 years. It has never been taken seriously by the doctors that have looked at my foot. I am going to see whether I can have an MRI to see whether my sesamoid bones have been damaged, it would be such a relief if I finally knew what was causing this pain.   
Thank you, I really do appreciate your help!
[jcuy5cx] (score 3, diepte 3 OP) I really do appreciate it and I am so sorry to hear that you also suffer with something very similar, it really is so draining and I feel like it will never get better. You've given me some great tips and I already have dancer's pads and tape in my shopping basket. Maybe some stiff soled shoes would also be something I should purchase. My foot seems to feel the best when it is in a tight shoe, where I can't move my feet. Do you also feel a sense of relief when you lift your foot in the air off the ground?   
I live in Germany so I think they would pay for my MRI. I'll be going to the doctor's tomorrow and I am going to show her all the possible conditions that have been suggested under my post.
[jcuuze3] (score 3, diepte 0) I know you said you've seen multiple doctors... have you seen a physical therapist yet?
[jcuvppd] (score 3, diepte 1 OP) No I haven't, I haven't been given any recommendations on what to do or who to see. Maybe this would be a good idea. Thanks!
[jcux9rh] (score 3, diepte 0) How can they see swelling in your foot and question a problem? Thats sort of nonsense, dont you think? I would question the quality of your medical care. Maybe give them a coupon for a free eye exam from your junk mail.

Its not much of surprise the pain is running up the leg, its all connected. Your hip and low back will be next. Have they ever done Xrays/MRI's of your foot?  If you havent seen a podiatrist, its overdue. If you have seen one, you need a better one.

I've broken so many toes, there isnt a straight one on either foot. You cant do much to them except tape them to each other and hope they heal straight. At any rate, I get a lot of foot pain. It may sound a little nuts, but Voltaren gel all over, between the toes all the way back to the heel is very helpful. You may want to get a tube to experiment. It'll help with something else eventually if it doesnt help your foot. If it does work for you, try getting an Rx from your doc for a few tubes. Even though its over the counter, a lot of times they cover this stuff and the difference in cost can be huge.

You might be used to this somewhat, since you have been "side standing" for a long time, but eventually it affects your posture sending the pain straight up the leg. "Foot bone's connected to the leg bone, leg bone's connnected to the knee bone, knee bone's connected to the thigh bone"... and so on. 

Next time you see a doc that tells you that your pain tolerance is low, tell them "You walk on the f-ing thing, then!" You're there about your foot, not pain tolerance. "Can we stick to the subject doc?" You must be an exceptional individual not to get insulted by that, but you only have to tolerate so much, and thats if theyre helping. If they arent doing anything for you, don't take that kind of crap.

You might find a foot brace a bit of help. I just peeked on line, since I was seeing TV commercials for the latest, greatest foot support appliance (I think it was Copperfit), and was going to suggest you keep an eye out for their ad, but I was stunned by the huge number and differing configurations for foot braces. Some are closer to a walking boot. There didnt seen to be much that you could wear with a shoe, but they may help when you get home and let the dogs run free. See a good foot doctor, but be careful about braces and whatnot they may offer, their stuff is usually outrageously expensive.  Make sure insurance covers it enough to be reasonable. Best of luck...
[jcwsi50] (score 3, diepte 0) Have you seen a podiatrist? Had an X-ray?

I have arthritis in both of my big toe joints and it caused a lot of misery for years. I have a set of custom orthotics now that have made an incredible difference in my foot pain.
[jcule3u] (score 2, diepte 0) This sounds a lot like Plantar fasciitis. I've had it.

Have you seen a podiatrist yet? If that's what it is, there are ways to help it feel better such as wearing the right shoes and/or cortisone injections for the swelling and pain.
[jcv1rpy] (score 2, diepte 4) I get the most relief when my foot is free of pressure, typically with my leg straight out and letting everything below my knee go limp. Sitting with my foot parallel to but off the ground is still painful but not as bad as foot flat on the ground. Pressing directly on the area hurts almost as bad as standing or walking. 

Shoes are hit or miss on pain, depending on how padded my foot is, how tight the laces are, sole stiffnesses and cushioning, and swelling that day. Walking barefoot is worse than walking with shoes.
[jcuza65] (score 2, diepte 1 OP) Believe me, I have felt like saying all those kind of things to the doctor's I have seen. I have been told, that if they chopped my hand off, that I wouldn't feel the pain in my foot anymore and would be going on about the pain in my hand. I have been reduced to tears, because of the frustration I have felt. But it has put me off going to see any doctor. Seeing as I am in so much pain recently, I just thought I will see if anybody on Reddit can help and I am so happy with all the help I have already received. The next I have my foot properly checked, I will make sure to get a proper diagnosis. Voltaren gel also sounds like a good idea, I'll give it a try. Thanks again!
[jcwpesg] (score 2, diepte 1) That was my first thought as well.
[jcxalgx] (score 2, diepte 1 OP) I had a blood test about 6 years ago and they said that it wasn't gout. But I think I should have it tested it again. Thanks!
[jcw7no6] (score 2, diepte 0) turf toe?
[jcwdrwt] (score 2, diepte 0) It really sounds like you need to see another doctor - I'd recommend seeing a podiatrist next (or again?) - they'll likely do new x-rays &amp; they can determine if further imaging is needed (like an MRI or CT scan) if they suspect issues with your tendons, ligaments or soft tissues (as x-rays aren't helpful at showing issues with soft tissues). They can also recommend &amp; fit you with specific orthotics/metatarsal pads and may refer you to PT.

I saw someone mentioned sesamoiditis, which definitely seems to fit your symptoms - the pain can come and go &amp; can cause a person to over-supinate, which is what your doing when you're walking on the side of your foot! This can negatively affect your gait, which can in turn negatively affect other parts of your foot, ankle, knee, hip, or back. 

Anyway here's some info on [sesamoiditis + sesamoid injuries of the foot](https://www.foothealthfacts.org/conditions/sesamoid-injuries-in-the-foot)

Another issue to consider is [metatarsalgia](https://www.mayoclinic.org/diseases-conditions/metatarsalgia/symptoms-causes/syc-20354790)

Good luck!
[jcwirxw] (score 2, diepte 0) Go to someone who does Reflexology or Myofascial Release. They work on foot problems daily.
[jcwphq4] (score 2, diepte 0) HAPPY 🍰 DAY!!!
[jcxasc0] (score 2, diepte 1 OP) I have had X-rays at the doctors and they always say there is nothing wrong with my foot. But after reading these comments, I should probably have an MRI, because X-rays don't necessarily show anything because the bone is so small.   
Thanks!
[jcx0dkc] (score 2, diepte 0) I have that same sort of pain and my podiatrist said it’s likely peripheral neuropathy from my T2 diabetes. Have you had your blood glucose and A1C checked?
[jcxcyiz] (score 2, diepte 1 OP) No I haven't had it checked, I'll add it to my "possible condition" list that I would like to show my doctor. Thanks!
[jcxgthn] (score 2, diepte 0) Have you ever heard of a Morton Neuroma? Check out the symptoms.   MN is nerve pain due to inflamed nerve due to being injured or compressed.
[jculwaf] (score 1, diepte 1 OP) Thanks very much for your response, I just took a closer look at Plantar fasciitis and it says that when you have it, you mostly have pain in the heel of your foot. My pain is only in the toe and the ball of my foot. I really appreciate your help!
[jcuwmn3] (score 1, diepte 1 OP) So far I haven't had it properly checked by any of the doctors I have seen, I have been to quite a few doctors already and they just think I am making it up. I cannot describe how frustrating it is. But thanks very much, this could be another option!
[jcxcuxq] (score 1, diepte 1 OP) This is also something I read about and feels like it could fit. Thanks!
[jcxd8tl] (score 1, diepte 1 OP) Thanks for the links to the pages, it really does sound a lot like sesamoiditis. It's interesting that you said x-rays wouldn't necessarily show the issue, this is something to mention to the doctor. It would be such a relief to finally know what it is. Thank you very much for your help!
[jcxktuz] (score 1, diepte 1 OP) I haven't heard of it yet, but I am going to read about it now and see if it could fit to my symptoms. Thanks!
[jcuv1zl] (score 0, diepte 0) Of course they say it's in your head. 

Has anyone evaluated you for a latent infection?  It's spreading.  

I'd see an infectious disease doctor.  There are joint infections that cause pain that can't be diagnosed without a biopsy.  It's not enough to cause changes in bloodwork typically associated with infection, but the toe joints are very small, with very little soft tissue, so they can't handle any inflammation.

=== THREAD smmow7 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-02-07  SCORE: 16  REACTIES: 30
TITEL: Seem to be worried about my shoes bulging due to flat feet, it happens even in a wide fitting. What do you think? Please see note for more info, thanks. 😊
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hvxh9el] (score 10, diepte 0) I don't have super-wide feet but noticed the same when I got mine. Feeling tends to disappear during the run personally. Noticed no issues racing a marathon, a few half's, 10k and a bunch of 5ks and training runs. Didn't get injured and had no foot pain (knock on wood). Couples blisters on the toes at first but switched to injinjis and that solved that. That new altra supershoe may be perfect for us neanderthal footed individuals when it drops!
[hvxg0ue] (score 6, diepte 0) If they feel good and you’re not getting injured then I would stop worrying about it.
[hw0j4i6] (score 5, diepte 0) Have the same thing going on with my alphaflys. I have flat feet as well and it was noticeable how much my feet stuck out. I was convinced it was going to be a problem. Took them out for a 5k, no issues, felt great! Took them out for a long run, 20 miler, and started to feel the outer edge of the insole dig into my inner arch just over halfway through. Made the end of the run miserable. Bought some blister prevention patches. Patched up both shoes putting patches over the gap between the insole and inner side of the shoe. Was nervous as race day would be the test if it worked. But it worked flawlessly! No sign of discomfort whatsoever. Bottom line, you might want to test on a longer run as well if you’re running a marathon, last thing you would want is this creeping up on you at mile 15 or so.
[hvy2olv] (score 4, diepte 0) I recently got vaporflys and i think thats just due to the design of the shoe (thin and narrow in the heel and midfoot then going to wide in the forefoot) i have thin feet and when i first put them on it felt like my foot was overhanging the inside a lot but they feel completely fine during a run and i dont really notice it as much anymore when standing/walking in them
[hw06cag] (score 4, diepte 0) If you stand at the start line of a half/full and examine how the super shoes fit on peoples feet, you’ll see that 90% of vaporflys will fit just like your picture.
[hvxq5h5] (score 3, diepte 0) Thanks for looking in to this and sharing! I have the same “problem” and am glad to hear your experience. It doesn’t sound like you wear insoles, have you thought about that? I don’t currently either but wonder if it would make any difference
[hw1ywor] (score 3, diepte 0) Rant: make sure you get feedback from doctors, PT’s, or other flat foot runners. Getting feedback from people who never walked in our shoes (pun intended) or never studied it is like men telling women what to do with their bodies. 

That being said, I’ve found with the VaporFly it didn’t become an issue until my body fatigued and couldn’t handle good running form. That’s when it becomes an issue. For me that’s around 30k. Someone made a stingy but valid point that maybe I just need more training. But until then if I’m trying to run 3:20 today, it would make sense to me to have a firmer base for the last 8 miles in a proven long distance racer. So for that, I’m the lone #bigbonedflatfootedrunner who is leaning to the Zoom Fly 4 (20 mile PB) for the next Marathon. But I agree it’s not a problem… as long as you keep good form. Love this shoe for the half.
[hvxf4zc] (score 2, diepte 0 OP) Hi all. I’ve tried to find out more information about this and whether it could set me up for injuries. I’m currently running 40 to 50 miles per week for my mental health. I think I am overthinking and anxious for no reason but will make this the last time I ask. I’ve noticed after a friend made a comment that my shoes seem to bulge and sort of overhang the soles of the shoe, I had a look back on some old pictures and noticed it’s been happening since forever. I’ve got flexible flat feet and saw a physiotherapist not long back about knee pain I was having, they didn’t seem concerned about my flat feet, I do their exercises regularly and have had no pains even while increasing my mileage. I recently bought a pair of Vaporfly for running my next half marathon but decided to take them out for a 5K and set a new PB of 20 mins. They feel great to run in but I was concerned about the overhang. Am I overthinking and being anxious over nothing? I can see it happens even in my wide fitting Altra Torin’s, but the thought of it being a problem in the future seems to be really bothering me. The Vaporfly are UK 8.5 and the Torin’s are a UK 8 wide fit. Is it something that’ll be fine and I need to just accept? Thanks so much everyone. 🙂
[hvxgzz1] (score 2, diepte 3 OP) I’ll do exactly that. Thank you again! 🙌
[hvyzxya] (score 2, diepte 1) I have quite a wide midfoot as well and I have used insoles with the idea that they push the midfoot of the shoe out of my foot's way.  Does that actually work or is it just in my head? Ehhh.... Lol

I also skip some eyelets in the middle of the shoe to give me extra room--which I'm quite confident actually helps.
[hy04r1e] (score 2, diepte 2) Great idea on skipping eyelets!
[hvyn882] (score 2, diepte 0) Ditto! I also have a wider midfoot and agree with the comments that, if you’re not getting injured, I wouldn’t worry about it. BUT just be mindful of your mechanics and how they impact you. A lot of fast shoes are intentionally designed with less stable midfoot platforms. This can definitely introduce instability and force your lower leg muscles to work harder but as long as your lower leg muscles are strong enough to handle it, then you’re golden. I had a small overuse injury related to that late last year but it’s all coming back nicely with some recovery and strengthening work. If you’re worried, you can always consult your physio on preventative exercises and stretches.
[hvynl03] (score 2, diepte 1 OP) Thanks for that! I make sure to add in stretching & strengthening exercises each day as I’ve found it has definitely made me a stronger runner. Appreciate your insight. 😊
[hvyuzq4] (score 2, diepte 2) Np!
[hvyxqvu] (score 2, diepte 1 OP) Wow, I’d never realised that before! I can see you what mean from the footage though, very inspiring to see two of the best with that! Everyone has honestly made us feel a lot better so I’m really grateful. Thank you! 😊
[hw0w17y] (score 2, diepte 2) Once you get up to speed in these shoes there's really no issue even if you have that overhang. My vaporflys fit me the same as your picture and it really doesn't lead to any sort of issues because I tend to land and kick off using the balls of my 2 little toes on each foot.
[hw0jnxx] (score 2, diepte 1 OP) That’s some sound advise! Definitely something I’ll keep in mind going forward when looking at taking on longer distances. Appreciate your insight. 😀
[hw1znmb] (score 2, diepte 1) Nice! I have these copper wraps that I’m testing in my Flys that seem to be helping as well. But this 👍!
[hw1tagq] (score 2, diepte 0) Your feet are find Nike is just too narrow. Get yourself some brooks or try the Nike Miler 2.
[hw25ae8] (score 2, diepte 1 OP) I’ve found the Miler 2 to feel very clunky when I’ve tried it on at the Nike factory. It did seem a tad more generous than typical Nike shoes however. One of the things I’ve noticed, certain shoes can irritate my foot especially if the material doesn’t have much give, I found this with the Adrenaline GTS. It’s funny that it happens in wide fits though as well. I think it’s just one of those things I need to deal with, trial and error for what feels comfortable. No problems yet with these & has been reassuring to see people’s responses for the long term! 🤞Thanks for chipping in also. 😊
[hw2c5eg] (score 2, diepte 2) It’s a big clunky shoe for sure but the Pegasus was way too narrow for my feet so got the miler instead. Suits my slow pace and heavy heel strike so I’m pretty happy with it. Good luck in your search!
[hvxgd2g] (score 1, diepte 1 OP) The Vaporfly are like having little pogo sticks on the bottoms of your feet, haha! 10 miles already on them and they feel really fun to run in. I think because of how much running has helped me, I don’t want to give it up due to injury and noticing this definitely made us anxious about the future. I guess it’s a challenge for myself to accept some uncertainty and stop stressing. Thanks a lot. 😊
[hvxgxxo] (score 1, diepte 2) Everyone’s feet are different. You appear to have a wide mid foot but that’s ok! As long as the shoes fit and your toes aren’t getting crushed and they’re not painful in any way then enjoy your running.
[hvxhe4w] (score 1, diepte 1 OP) That’s really reassuring to hear! Well done with your races as well. 💪I’ll have to keep my eye out for that Altra. I do appreciate the extra toe box space. 😄
[hvy44k5] (score 1, diepte 1 OP) I’ve noticed I have this in almost every shoe. 😆 It’s really good to hear it shouldn’t cause any problems though. Thanks a lot for sharing! 😀
[hvypyu0] (score 1, diepte 0) The vapor and Alphaflys have a ridiculously narrow midfoot, so it's no surprise to see it exaggerated with the Vaporfly.

That said, the fear around flat feet has been massively exaggerated, primarily to sell insoles and orthotics. If you don't have issues with tendonitis on the inside of your ankle/foot or in your Achilles, then there's really nothing to be stressing about. Watch a slowmo of Cheptegei or Kipchoge. They both very likely have flat feet because they have heavy pronation (not going to call it "overpronation" because clearly it isn't actually an issue), yet both train 200-225k+ per week and neither use anything other than stock shoes/footbeds.
[hw0ag8v] (score 1, diepte 1 OP) I’ll be the strange one on the start line examining everyone’s shoes now, lol! I wasn’t sure what kind of responses I’d get when posting this but definitely not worried now. Thanks for that! 😊
[hw8azd2] (score 1, diepte 1) Can you upload a photo of how did you patched your shoe?
[hw24lbq] (score 1, diepte 1 OP) I have had my physiotherapist reassure me on my musculoskeletal tests with balance, tracking etc when I had the knee pain a while back, she said to stick with neutral shoes as well. I just do the exercises and they’ve made a world of difference. So that’s definitely good advise. I appreciate your insight as well, absolutely awesome you’ve ran 30K, it’s inspiring to see the distance can be done. 😀 You’ve mentioned the Zoom Fly, a long time ago I ran in the original and adored it. Have you found the Zoom Fly 4 to be a good daily trainer to go with the Vaporfly or are you just using it for speedier/longer sessions and potentially your race? I might have to check that one out at some point. I’m going to have too many shoes. 😆
[hvxu5o3] (score 0, diepte 1 OP) I’ve tried them briefly but had a lot of discomfort, I quickly gave up on them, haha! I suppose it’ll just be a matter of trial and error, to see what we get on with and what we don’t. 😌

=== THREAD 14dvttl ===
SUBREDDIT: r/ChronicPain
DATUM: 2023-06-20  SCORE: 86  REACTIES: 30
TITEL: My back pain has been excruciating the last two weeks and today it's resulted in the dreaded foot drop.. But I try to stay silly 🙃
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jos4yjl] (score 12, diepte 0) That's how my hands do my brain all the time!!!!!


I know they get the signals to work, but my hands are "yup, nope, not happening".

Left my brain on read....I love it!
[jot56uy] (score 7, diepte 0) Ok, but bubble wrap this awesome support person you have!!!
[josh5bi] (score 6, diepte 1 OP) We hear you but respectfully decline 🤷🏻‍♀️

Appendages are so rude lol
[joug7yi] (score 6, diepte 1 OP) He's my husband 🥰
[jos6v28] (score 3, diepte 1 OP) I have so many false starts trying to get up!

I will position myself perfectly, start to get up and my whole back will seize and I plop back down and go "nope" 🫠
[joufsgc] (score 3, diepte 1 OP) Show me where I pretended not to be in pain?

Should I just wail all the time and lose my sense of humour entirely until I just kill myself? How much wallowing would be enough for you exactly?
[jougr3g] (score 3, diepte 2) Dude. I’m really sorry im completely wrong. You’re not hiding it with a smile, I didn’t read your whole post, and I got triggered because I thought of someone I know who’s very close to me who just keeps suffering in silence because he believes that that’s the best way to do things, it hurts and I just assumed incorrectly that’s what you were doing that I am sorry. 

Hope your day gets better and your back gets better too
[jov0zcq] (score 2, diepte 2) This happened to me all the time in chemo induction. I'd be like "Hello, Mr. Leg? Can we move?" And my leg would just not even hear the message.
[jos6b7o] (score 2, diepte 0) I hear that, sometimes I get up just a little to fast and my back just decides it doesn't have time to straighten out so it just leaves me hanging(and occasionally on the floor)
[jos8g2n] (score 2, diepte 0) I have a rare varient of CMT, CMT in general is chronic pain and foot drop/ hammer toes.
If your unsure have a quick google for cmt it dosnt matter if its type 1 or 2.
[josc01m] (score 2, diepte 0) Man, foot drop is so inconvenient. I have permanent loss of feeling in my foot and my foot drop flares up the longer I walk.
[jowzj4l] (score 2, diepte 7 OP) Not actually sure, I've had degeneration for many years but never pain to this degree (I actually joined this sub for pain from intersistial cystitis and atypical migraines), along with some damage in my hip from a childhood accident. Dr suspects Degenerative Disc Disease and I feel it's likely I've slipped a disc but the waitlist for imaging here is quite long so I won't have a definitive answer for a while.

Dr has given me a script for cyclobenzaprine and referral for physio in the meantime. He's told me to avoid bending, lifting, twisting, sleeping on my back and to make sure I'm getting up every half hour or so to walk.
[jovr4ho] (score 2, diepte 3 OP) My Dr is aware, my mum has degenerative disc disease that landed her in hospital many times growing up and my bestie is a paramedic so I am being monitored and reminded constantly what I should be doing/looking out for - but I appreciate it just the same 😊 better safe than sorry!
[jouwvvh] (score 2, diepte 0) That's such a good way to describe drop foot hahaha! Definitely using that
[jov4t83] (score 2, diepte 0) My leg is numb from my knee down especially my foot. I kinda tap it and ask if it’ll behave while I head to the bathroom go and come back. I treat each body part with a problem like they aren’t part of my body. They’re being an absolute twatwaffle so they don’t belong my body doesn’t like bullies.
[joyluek] (score 2, diepte 0) Not sure if I've had something similar, I feel like if I have to move in a way that is going to cause intense pain, there is difficulty getting my body to do the thing. I have to spend like half an hour verbally psyching myself up. You know that scene in Harry Potter, where hogwarts is trying to send him mail but the dursley's keep taking it, and eventually they flood their house with mail so Harry finally can read it? That's what's happening in my brain I think, I've got to overwhelm the dursleys with brain signals to move so one finally gets through
[jozfpyh] (score 2, diepte 0) Sometimes all you can do is stay silly

I've started writing down all my fun descriptions of my symptoms

Today's was "I feel like I've been microwaved"
[jos8itx] (score 1, diepte 2) Same, it's either my back or my legs but one of them will put me right back down. It's somewhat ok now that I expect it but the first time my back locked up I did a header right on the floor
[josh7ag] (score 1, diepte 1 OP) Mine feels worse with walking too.. But I'm supposed to move to help my back.. I am at a loss lol
[jotexje] (score 1, diepte 2) Try getting an upright bike
[jow1xdm] (score 1, diepte 4) I have adhesive arachnoiditis, annular tear at L4-L5, and arthritis with fluid at L4 and S1, who’s is above and below my [surgical hardware](https://imgur.com/a/sRXZUVu). 

Riding a bike is pretty low impact as well as swimming. I can do that much better than I can walk. I use a rollator full time now so it’s one of the few things i can (sometimes) do
[jow73ia] (score 1, diepte 5 OP) The issue is I can't bend, at all, without debilitating pain and was told explicitly not to by my Dr. I could see a recumbent bike helping but an upright would destroy me.
[jowv7nr] (score 1, diepte 6) I got a recumbent bike to help but it hurts my butt so bad! I don't know if it's because I'm leaning forward.. or if it doesn't have enough padding.. it just hurts.
[jowyk97] (score 1, diepte 6) I can’t use a recumbent because I’ve had two hip surgeries. Usually bending forward slightly takes some tension off of the nerves or facet joints. I’m assuming you have a herniated disc?
[jox3hen] (score 1, diepte 7) Sorry to hear that. Be sure to go to the ER if you experience any symptoms of [cauda equina syndrome.](https://imgur.com/a/Pz7q5yZ)
[jovqjh7] (score 1, diepte 2) if your foot drop is a new symptom stop walking and exercising and speak to your DR tomorrow.. any issues with bladder/bowel and its an emergency situation that needs ER immediately. 

I hope you do already know this and its not this way, just felt i needed to say it. My disc issues happened in 1991, was treated the opposite way, with bed rest and traction for weeks on end.   
DUring my third admission i was having physio in hydrotherapy pool, one night lying in bed i turned pillows and was scared by a bug. That jerk of surprise, on my side put my disc back in place.. an hour later i wasn't limping so much, next morning pain was gone! But it only lasted a few weeks.
[joug4nz] (score 0, diepte 3 OP) My issues are in L5-S1, I can't hunch over like that. That's the type of position that could completely lock my back.
[jou64tn] (score -2, diepte 0) The more you pretend like you’re not in pain the less people will be understanding and willing to help out. Pretending like you’re not in pain is just going to make your situation much much much worse because you’re also gonna really confuse your brain

=== THREAD rd7gjs ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2021-12-10  SCORE: 3  REACTIES: 29
TITEL: Any trampoline-like running shoes? Please read+++
POST (source_id=post):
I have a friend who is depressed and overweight. She recently told me that she would love to run again but that it's now hard on her joints and her plantar fasciitis. I figured a trampoline-like running shoe could be an answer? I would love to get her one as a holiday present. Her wanting to go outside and run again after being so crippled by depression and staying indoors is very hopeful so I really hope there are running shoes that will allow her to do this. I live in Canada so something that works with black ice would be even better since it's winter now but I just want to know if there is anything like this. Any suggestions are welcome. Thank you.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hnzpdy2] (score 35, diepte 0) A bouncy shoe isn't going to solve joint pain and plantar fasciitis and to look at it from that angle is just not good in general.
[hnzoc3l] (score 17, diepte 0) If plantar fasciitis is a concern, stay away from the invincible. It can be tiring on your foot if you aren’t used to running (it’s got tons of cushion, but it’s not particularly stable). 

I’d recommend the morev3, bondi or endorphin shift. All have good cushion and support. 

The biggest part for getting a new runner into the sport is making running as fun/enjoyable as possible. A big piece of that is support + injury prevention.  

Hope this helps!
[hnzki4k] (score 7, diepte 0) NB More V3 and Nike Invincible. Highly recommed the first one. They are just so good overal
[hnzqshg] (score 5, diepte 0) I wouldn’t look to shoes necessarily for preventing joint pain, I would just make sure they fit and maybe try to easing into runs on trails/softer surfaces first and slowly adding some pavement miles and just starting off slow in general.  Shoes might give you a false impression that you’re feeling good and can contribute to overuse quickly
[ho3o9pa] (score 3, diepte 2) I must be missing a lot, because the Velocity is my fun shoe 😅 I only use my Kayanos anymore to have a rotation and to take some miles out of my Velocitys.

That may change in the future as I just found out some Deviate Nitro Elite 😬
[ho08umv] (score 3, diepte 0) If you're overweight, a squashier midsole is going to be more likely to cause injuries by being far less stable than a firm midsole.

I'd go for something firmish but soft enough to be comfy, and work on slower, shorter mileage so it's less stressful on the body. Then this will ease as the weight comes down and fitness goes up, along with the distance.
[hnzazn6] (score 2, diepte 0) According to many reviews and what I have read on this subreddit, the Nike Invincible Run is a very (!) bouncy shoe with very good traction for a road shoe. Hoka is also known for its soft and very cushioned shoes. The Clifton 8 might work (also good for wide feet) and is a very enjoyable shoe but nothing special. The Adidas Adidastar could also be a solid choice.

I only have tried the Hoka Clifton 8 from the shoes mentioned above.

Lastly avoid plated shoes or shoes from On running. These are generally very firm and not very forgiving for the legs.

These are just some suggestions. In any case I strongly advice going to a specialized store / having her do a gait analysis, so that the shoes you buy her fit for her running style and foot type. I once made the mistake of buying shoes that do not fit my running style and I had to pay for that with an injury.

Good luck!
[hnzcox9] (score 2, diepte 0) Nike invincible is your best option
[hnzf6ms] (score 2, diepte 1) Dunno, but if you suggested Velocity nitro for me before starting to run, i would find it to be veryyy boring. I think to get hooked in this hobby is to find something excitement first after then Velocity like shoe as daily trainer imo.
[ho4717c] (score 2, diepte 3) There is nothing wrong finding something which is right for you. I were just expressing my own opinion and experience! All though i do have a lot of shoes in my rotation, so in that perspective our opinion have different styles and uses. 

I myself tried to hunt Deviate elite too, and had a chance to purchase it on end of summer, but instead went for endorphin speed, and other chinese carbon plated shoes so if i would had added deviate elite, my wallet would had suffered so much haha! 😅 and upcoming 2022 shoes won't help it either!
[hnzfx2n] (score 2, diepte 0) Might be a little more “out there” of an answer, but the Brooks Aurora BL is almost exactly what you’re describing. Both in feel and injury prevention.
[hnzvika] (score 2, diepte 1 OP) Thank you so much. Will look into this.
[ho0puuu] (score 2, diepte 1) Brooks in general tbh. Lots of room in the toe box, good stability options, good mileage, lots of cushioning options (glycerin namely) - Sincerely, a 260lb runner.
[hnzg15n] (score 2, diepte 0) Nike Invincible and Skechers Performance Max Road 5 are the two bounciest shoes out there.
[hnzz6tg] (score 2, diepte 0) Do you have a local running shop you can take her too?! You could tell her what you want to get her, make a day of it together, and let her try on all the different shoes that’d be good for her, and she can have that glass slipper moment when she finds the one! In other words- she’ll know best!!
[ho0c3m3] (score 2, diepte 0) I think soft shoes would be too unstable to be good for someone newer to running and injured. I think you need good form and strong stabilising muscles to wear these safely.

Also, there are some shoes here in Canada with ice grips, but they’re generally on the firmer end, because if there’s potential ice then you really need more stability in the landing to save yourself and a low stack height. Otherwise you’re walking on springs on ice, which is never a good idea!
[ho0duzk] (score 2, diepte 0) Just adding that if black ice is really an issue, no shoe is going to protect you. For that metal will help, YakTrax Run or ice screws being two popular options.
[hnz9c4n] (score 1, diepte 0) It's not quite what you asked, but actual trampolines can be a great workout
[hnz9oxm] (score 1, diepte 1 OP) Thank you. I think it's something about running outside that does it for her. She's always indoors so this is a huge thing for her to say this so I would love to help make it a reality, if possible.
[hnzg4t3] (score 1, diepte 2) Fair enough. In which case I'd take a look at both the Nike invincible and NB More v3
[hnzbscf] (score 1, diepte 1 OP) Wow! So helpful. All of this. Thank you so much!
[hnzddrc] (score 1, diepte 0) Check out the Puma Velocity Nitro. It isn’t exactly trampoline-like, but it checks all the other boxes (good grip, easy on the joints, soft so it doesn’t aggravate plantar fasciitis). Not the most exciting shoe I have ever run in, but it’s great for throwing and going outside to get in consistent mileage, which makes me think it would work for someone trying to get back into running.
[hnzsbxp] (score 1, diepte 2) That’s fair. I was trying to think of something that balanced being fun/pleasurable without potentially being too unstable (why I didn’t list the Novablast 2, even though in hindsight, that might work better for OP’s desire than the Velocity).
[hnzw1ho] (score 1, diepte 3 OP) Thanks for the add on. Will check this out too.
[hnzvx37] (score 1, diepte 2 OP) How are shoes boring or exciting? What kind of excitement can one get from shoes? Silly question, I'm sure, but I'm just learning about all this. Thank you.
[ho092xi] (score 1, diepte 3) If you ask my opinion about " i wish i knew these things before start to run" as hobby, definitely buy exciting shoe with great cushioning with great rocker design to assist you to move your step cycle faster as my first shoe. Novablast 2 or up coming Novablast 3 would had been great first pick.  Hoka March 4, Clifton series. Also other riskier choices like Endorphin speed ( might have stability issues for new runner ).

Not only those rockered shoes makes running easier but also to help you maintaining your speed easier and assist your body to run longer distance until you feel like things getting easier!
[ho0j5i7] (score 1, diepte 4 OP) Wow! Thanks so much!
[hnzvyhs] (score 1, diepte 1 OP) Thank you!
[ho0ogw1] (score 1, diepte 0) Invincible and Novablast didn’t worked with my PF. Heck, my plantar fasciitis was even caused by using the Rebel v2 for 3 straight months. See the common denominator there? All soft cushioned shoes. Or maybe weak lower leg muscles.

Either way, the only shoes that kept me running? Adidas Boston 10, Asics Magic Speed, Adidas Adios 6 and New Balance 1080 v10. Common denominator? firmer midsoles add to that more strength & conditioning, ankle mobility, regular calf stretching and leg foam rolling somehow eased up my PF.

Been enduring it since May.
[ho1mca7] (score 1, diepte 0) If she's overweight then the trampoline like feel might not work - her landing on the sole might cause more issues

Best she visits a physio first then figure out what she needs shoe-wise. She might even need some orthotics on how she pronates
[ho1untb] (score 1, diepte 0) https://runrepeat.com/guides/best-plantar-fasciitis-running-shoes
[iwckv0j] (score 1, diepte 0) The New Balance Fresh Foam More V3 running shoes are some of the most comfortable I've ever worn. I wouldn't wear them to a race, but they're great for a casual run on the road or treadmill.

https://coolideasforhome.com/nerapy?dfig=B096N7G4CR

=== THREAD i4s0ky ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2020-08-06  SCORE: 20  REACTIES: 28
TITEL: To my flat and wide feet brethren, I have the NB Fuelcell Prism & Nike React Miler. Feel free to ask me questions!
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[g0kdb08] (score 8, diepte 0) That red is so fresh
[g0klx22] (score 6, diepte 0) I know right. Im so sad when i found out im flat feet. Stability shoes is limited and heavy
[g0kg4re] (score 4, diepte 1 OP) The Pegasus 37  was a tight but ok fit but the reacts are perfect and feel really plush.
[g0km4jo] (score 4, diepte 1 OP) I had to injure my feet twice before I got a 3D scan to tell me I’ve been wearing the wrong shoe size because of my wide feet!

But yeah choices are very limited for us sadly!
[g0k673k] (score 3, diepte 1 OP) No sadly I haven’t. I am a long distance runner so my main needs are cushioning that will help me go past 10+ miles without hurting my feet.
[g0kfvr7] (score 3, diepte 0) How wide are the reacts? Tried the Pegasus before and the midfoot was too cramped
[g0kijjz] (score 3, diepte 1 OP) It’s very mild, but I’m a mild pronater. The middle section of the shoe the shoe is firmer, so when you run instead of caving in, the good lock in of the heel makes you push down on that section.
[g0klf52] (score 3, diepte 1 OP) Indeed they are!
[g6xsim5] (score 2, diepte 3 OP) The main issue I found on the standard fit was that it was tight with thin socks. When you wear running sock and your feet swell you will be in pain.
[g6xuqqh] (score 2, diepte 5 OP) I actually prefer the fit of the React. It is heavier but holds your foot very secure with no slippage, which can happen with the prism if you don’t wear the right socks.
[g6xvb7l] (score 2, diepte 6) I appreciate the quick replys, some food for thought there. All this waiting around trying to get my hands on a pair of Endorphin Speeds has me itching for a something new in the rotation.
[g0k9724] (score 2, diepte 0) What’s the width on the Prism? I was looking last night but didn’t see them in a 4E. I wear the 1500 half a size up in 2E, so maybe that would work. 

How do the Prisms hold up and cushion on your long runs?
[g0kcw9x] (score 2, diepte 1 OP) Prism is 2E. For reference I fit a 4E on a 1080V10. Prism is more of sport fit so tight but not painful tight.

Prism is more squishy but lightweight and has a decent bounce to it, heel is securely locked.

After coming from trail shoes with goretex these feel like heaven!
[g0kheoq] (score 2, diepte 0) Do the Prisms that much stability?
[g0kl5n3] (score 2, diepte 0) I didn’t know fuel cell and react miller is stability shoes.
[g0letkf] (score 2, diepte 0) With some shoes i had some trouble with thin midfeet where my foot would hang over the sole and hurt. Do these have wide midfeet?
[g0lmtj6] (score 2, diepte 1 OP) Yeah same here.

So both of these have a wider foot but offer different fits.

The Prism is a race fit that will hug your midfoot more than your forefoot.

The Miler surprised me because it has a really nice relaxed fit but still keeps your foot locked securely.
[g0t08yt] (score 2, diepte 1 OP) I was originally worried about getting white since I would of preferred the green ones but I get compliments how the white ones look.🤷‍♂️
[g0umhfs] (score 2, diepte 2) They look great!
[g0k5vlh] (score 1, diepte 0) Have you tried the Nike Zoom Vomero? They're supposed to be for people that are flat footed. They also have them in wide as well.
[g6xs5hf] (score 1, diepte 2) Hi. I do you think standard fit in the Prisms would be loose enough in the toebox and bridge across the top for someone who normally gets a wide fit
[g6xt7n3] (score 1, diepte 4) Yeah I thought that would probably be the case, thanks for that. So hows the fit of the reacts?
[g0klmrn] (score 1, diepte 0) I see. At least they aren’t bulky as kayano 27.
[g0klt0c] (score 1, diepte 1 OP) Tried them and found them uninspiring and clunky.
[g0seo8y] (score 1, diepte 0) I would kill for a pair of those sick NBs but they made the women’s sizes not nearly as badass looking... per usual
[g0vkmey] (score 1, diepte 3 OP) Thanks!
[g0kmw52] (score 0, diepte 0) ...I am from Rwanda east africa, I am training to run marathons everyday the way I can with what I have, but I want more running shoes.
...is there anybody who can help?
[g0k6mqh] (score -1, diepte 2) If you can find a specialty running shoe store, or even a Nike store, you can ask for those shoes and some have treadmills for you to try them on as you run in them shoes.

=== THREAD mve9xq ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2021-04-21  SCORE: 53  REACTIES: 28
TITEL: For my fellow wide feet sufferers, here is how you should buy the Saucony Endorphin Speed
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gvbcccf] (score 9, diepte 0 OP) This is a shoe I often see people asking about for wide feet and I recently needed an up-tempo trainer that would serve my fast long runs so I decided to pull the trigger. Another shoe I was considering was the New Balance  Rebel V2 but I need the extra cushion of stack height for my 10+ mile runs.

I usually run in a US 10, but had been reading that the Speed is a tight fit so I followed the advice of going half a size up to 10.5 and I am pleasantly surprised by the fit. If there was a shoe I would most like to find similar fit wise for a default width, I would say the Novablast. The Novablast to me at my normal size fits perfectly like the Speed with about 3mm or so extra toe length which is not an issue.

You can see from the photo that there is a little overhang and bulging of my feet. I get much more overhang in my Symmetros so this is a pleasant surprise. The only issue is the very short shoelaces probably due to my high volume feet.

To summarize, if you are a 2E/4E type. ( I am a 4E in an NB 1080V10), I would advise you to go up half a size to make sure your feet are comfortable.
[gvbwqmv] (score 7, diepte 1) i feel like the Rebel v2 has more cushion than the Speed
[gvc1n5w] (score 5, diepte 3) i am not talking what the measurements are. i own both shoes and am telling you want they feel like (to me!)

Rebel v2 is a far more cushioned road feel. Speed is a stiff ride.
[gvceg5e] (score 5, diepte 1) I’m typically a 2-4E.  I wish I sized up half, but they are pretty tolerable in my normal size.  If I buy again I’ll go up.
[gvboi5x] (score 5, diepte 0) I found the same for me. I’m wide footed and going up 1/2 size worked for me.
[gvcqr7c] (score 5, diepte 4 OP) https://www.believeintherun.com/best-wide-foot-running-shoes/
[gvclg1s] (score 4, diepte 0) Definitely a plated wide foot fam approved shoe! I love the speed and they aren’t as harsh on the feet as carbon shoes since it’s TPU here.
[gvclsrg] (score 4, diepte 1 OP) Your shoe guide was one of the key reasons I went for it.😄
[gvcmdas] (score 4, diepte 2) Makes me happy to hear that what I say has helped others! 🙂
[gvcrh1r] (score 4, diepte 5) Thanks!
[gvc296f] (score 3, diepte 4 OP) Well being plated it’s going have that stiff push hard feel, which I prefer for speedy work.
[gvcesvz] (score 3, diepte 2 OP) My understanding is that with true to size it can feel tight on the feet after 10 miles. Would you say that is true?
[gvcf2ao] (score 3, diepte 3) I have a newborn and haven’t had the time to put in 10 yet, but they feel good up to 6 for me so far.
[gvbyzqv] (score 3, diepte 0) I have a bunion on foot, therefore narrow shoes wont work but Endorphin Speed is very accommodating.  Roomy like the Clifton 6.
[gvc24yl] (score 3, diepte 2) easy fix.  Amazon.  cool colors and get length ya want.
[gvcpgam] (score 3, diepte 3) Where is the shoe guide you are referring to?
[gvc0hnd] (score 2, diepte 1) I sized up half a size and have only half inch space at the top and it’s been fine but I’m not running more than 10k in them rn. The upper also stretches a lot with use. It’s very accommodating.
[gvbvj18] (score 2, diepte 0) I can’t wait for my second pair to come! I have slightly wider than D feet and love the endorphin speeds. I tried a few other shoes and read reviews which just led me to order a second pair of speeds. Might even order a 3rd if they hurry and release the future spring colorway in the US 🤔😂.
[gvbza5k] (score 2, diepte 1 OP) Just wish the shoe laces were longer!
[gvchp8u] (score 2, diepte 1 OP) If you have a wide foot, I wouldn’t say there is much room for your foot to move around.
[h5dr5g4] (score 2, diepte 1 OP) Yeah going half a size would be best. 

The upper has a lot of volume for wide feet.
[gve4zsw] (score 1, diepte 2) As a 4E wearer, what shoes do you recommend for speed work?
[gvf3tmx] (score 1, diepte 3 OP) Your best bet for non plated shoes will be the New Balance FuelCell range since they come in wider widths than other brands. ASICS Evoride 2 I have heard also seems to work with wide feet.
[gvboyq5] (score 1, diepte 0) So, the end of your longest toe is in line with the top edge of your thumb here? That definitely seems pretty snug?
[gvbpa27] (score 1, diepte 1 OP) I always have a thumbs spacing between my toes and the top of my shoe. What you are seeing is a thumbs gap and a few extra millimetres going up half a size which isn’t an issue that will effect you.
[gvc1gxm] (score 1, diepte 0) I absolutely love these sneakers best experience in a running shoe... I want them to go on discount so I can try to get at least 2 more
[gvch679] (score 1, diepte 0) I like a snug fit, these would feel way too roomy for me
[gvdkj9a] (score 1, diepte 0) I figure I'll hijack this thread to ask, how serious is Saucony's return policy when they say shoes have to be returned unworn? Because I have pretty wide feet and I ordered my usual size 13, tried them on, but they seem too big (about an inch toe gap), but the width is perfect. Should I return them (if possible), and order 12.5 instead? I'm worried they would be too narrow.
[h5dqyc4] (score 1, diepte 0) If im wearing brooks ghost in 4E size US9.5 i Should get the saucony D width in US10?
[h5gzxx7] (score 1, diepte 2) Ok2, was just wondering do you know what other plated shoes are suitable for wide feet to your knowledge?
[h5igf41] (score 1, diepte 3 OP) This article will help

[https://www.believeintherun.com/best-wide-foot-plated-running-shoes-2021/](https://www.believeintherun.com/best-wide-foot-plated-running-shoes-2021/)
[gvbx614] (score 0, diepte 2 OP) Speed is 35.5mm heel / 27.5mm forefoot vs Rebel 22mm Forefoot / 28mm Heel

