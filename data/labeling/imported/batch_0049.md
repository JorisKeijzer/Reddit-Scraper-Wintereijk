# Label-batch batch_0049

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
Schrijf het resultaat naar `batch_0049.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 3smho8, 135q31x, 5g4o82).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 3smho8 ===
SUBREDDIT: r/BuyItForLife
DATUM: 2015-11-13  SCORE: 107  REACTIES: 117
TITEL: Help me. My feet are fucking killing me.
POST (source_id=post):
I just started a new job where I am on my feet walking around for about 8-10 hours a day. I am over 300 pounds. By the 5th hour, I am in so much pain, my feet are aching so bad. The dress code is business casual, occasionally business professional. I need a pair of black, nude and gray shoes that make me not want to kill myself by the end of the day.

Does anyone have any suggestions for some great shoes or insoles? 

And for the record, I am trying to lose weight and am working out on my days off to try and make this easier. Thanks everyone.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cwykoyx] (score 85, diepte 0) Contact a doctor. You might need special shoes.
[cwyl8ao] (score 57, diepte 0) No quality of shoe can counteract being 300+lbs, and on your feet 10hrs a day. You just gotta deal with it until you cut the weight, then spend money on nice shoes for good reasons.
[cwyl9yg] (score 32, diepte 1 OP) I know this is this truest answer. But in the meantime I'd like to get the best shoe I can.
[cwypse6] (score 25, diepte 0) I have been using the green superfeet insoles in my work boots for about a year now and have had good results. They are not squishy but do prevent your feet from getting that bruised pancake feeling at the end of the day. Source: Weigh 260 in my gear and work anywhere from 8 to 16 hrs on concrete.
[cwyzqvr] (score 23, diepte 1) I got orthopedic inserts custom made, it was a great choice. It cost a few hundred dollars in Canada (insurance covered half). I just wear them in aesics sneakers and it's really comfortable. However, being on your feet for that long would hurt anyway.
[cwywq5z] (score 22, diepte 1) Look, Look with your special feet!
[cwyl59q] (score 18, diepte 0) Are you a girl?  The 3 colors of shoes kinda sounds like it, and the standard "buy redwings" ain't gonna cut it if you are.

 Lots of people like clogs if they are on their feet all day(Healthcare pros, chefs) because your foot doesn't flex at all, so those muscles dont get used.  A nice pair of danskos can look ok for business casual.  The tradeoff is folks tend to roll their ankles easier.
[cwyxky9] (score 16, diepte 1) OP, please try Superfeet. They saved my feet, my legs, my back. They have a 30 day guarantee. If they don't work for you you can return them. They might take you a few days to get used to, give them a chance. Also, they are a little pricey, but worth every penny. Good socks, merino wool, will help too. Good luck!
[cwyr4f3] (score 13, diepte 2) Nothing is going to help like weight loss and time spent standing and walking. 

I've spent the better part of 17 years working standing and walking jobs. Nothing conditions your feet like standing on them. 

Buy some massaging shoes for after work, roll your feet on a spiky ball, elevate them and pamper them. But no shoe will help in the long run until you condition your feet.
[cwyy97j] (score 12, diepte 0) I'm a great big fat person. Good shoes will definitely help a bit, but honestly you will fairly quickly become accustomed to standing all day regardless of your shoes. Just like everything else, the more you do it the easier it gets. You can accelerate this process by exercising your feet, like jumping jacks or jogging.

If you are standing in the same spots every day, make sure they are providing fatigue mats, which I believe is required by law.
[cwyks11] (score 7, diepte 0) Check out Rockport. They have a good size variety, decent support and the soles give good energy return
[cwyyqh0] (score 7, diepte 2) the clog is rigid with a high arch bump, so your forefoot has very little pressure on it.  they're terrible for walking a lot for the same reason.
[cwyvzu5] (score 7, diepte 3) Good idea, a nice after work foot regimen will be something to look forward to. Maybe a nice heated foot bath.
Also, I know others are saying that nothing will be able to take the strain off your feet at 300 pounds, but as a man in your same situation I can tell you that a good shoe CAN make a hell of a difference.
Nothing will make them completely stop hurting, but some shoes/inserts will cut it down a lot.
Feet are so different from person to person, I haven't even found the perfect shoe yet, but Merrill's have been pretty good for me, I also have a stiff arch support in them to help.
[cwz0pe5] (score 6, diepte 2) I have to second this. orthopedic inserts saved my feet- I went from feeling like I was stepping on nails walking to class to running 5k's and hiking for fun.
[cwyvudf] (score 5, diepte 1) Feet don't flex in clogs? I had no idea. Thanks for mentioning this. This means clogs might help me in a different context.
[cwyw9si] (score 5, diepte 1) Just got Danskos for work a few months ago, and I had no idea why I didn't know how to walk sometimes. Thank you.
[cwz167u] (score 5, diepte 1) I use the orange and they are great. Not sure what the colors represent anymore,  but superfeet are excellent
Edit:spelling
[cwz518f] (score 5, diepte 1) Just FYI, squishy and soft is NOT what your feet need.  They need SUPPORT and structure.

To draw a comparison to the biking world, if you ride your bike more than 5 miles at a time, a soft padded seat will cause you more problems than they will help.
[cwymq42] (score 4, diepte 0) I am a big girl and I know the pain you are in.  Merrell shoes have treated me right, as well as Crocs.  There are some cute(ish) Crocs for men and women.  I wear a pair almost every day and no one has ever guessed they are Crocs.  When you get home, wear crocs rx around the house. They will help, I swear.
[cwz0bmz] (score 4, diepte 2) Ditto on the Superfeet.  They also seem to last longer than my shoes.  And they were a lot more comfortable and a hell of a lot less expensive than the custom orthotics my foot doctor prescribed.
[cwyyg8n] (score 4, diepte 0) a brief note on losing weight:  restrict calories.  don't drink anything with sugar in it (i permit myself a half teaspoon of sugar in coffee, because it helps me with the jitters).  no juice, no soda.  no diet soda except when you're having a bad day.  then get on a fucking elliptical machine every day and go as fast as you can sustain for 45 minutes.  use whatever self-loathing you have on tap to appreciate the suffering until it becomes easy to just get on and go.

until you lose weight, get compression socks to counteract the pressure on your tissue.  it may not be ideal to wear them while working, but if you put them on at night for a few hours, you will recuperate much faster.  i would probably get a very light pressure pair for wearing all day, and a higher pressure pair for recovery.

if you stand for long periods with little walking and can get away with it, get dansko professional clogs for those periods.

otherwise, i got birkenstock blue insoles from [here](http://www.feetrelief.com/).  you might want to try their birkobalance.  any 3/4 length insole will work pretty well with most shoes without messing with sizing too much.  anything with aggressive arch and metatarsal support.  you can write or call the guy and he can help you with sizing and maybe suggest an insole, but i would just buy a couple and try them in different shoes.

you might want to get one with less support that you can swap out while your feet are getting used to the support.  the support will not be comfortable, but it will prevent your feet from killing you.  i'm 200lbs, and it's taken me 2 or 3 weeks to somewhat retrain my fallen arches.

EDIT: also the walking company has lots of shoes with good support and (sometimes) semi-knowledgeable staff.  you could go there and try on a lot of shoes.

EDIT: note 2 on losing weight: [4 hour body](http://www.amazon.com/The-4-Hour-Body-Incredible-Superhuman-ebook/dp/B003EI2EH2) is actually a pretty good resource.  it's full of pop-sci bullshit speak but has lots of good information.  his diet advice is pragmatic and manageable, and will be enough to really turn shit around for you.

cut sweets, and if you find yourself eating sweets at any point, force yourself to leave at least the last bite.  it will change your brain.
[cwz2vzu] (score 4, diepte 0) Op, this isn't the answer you were looking for, but its the answer that might save your life.

I used to weigh 340 pounds, nothing "modern medicine" could do could help me. "Eat more whole grains, eat less meat, eat more than 3, smaller, meals a day, go run, eat less cholesterol".

None of this is useful advice, and will only serve to make you fatter. Yes, even running when you weigh that much is dangerous, and will lead eventually to a heart attack.

So, I decided to tell the medical industry to fuck off, and I went strictly Paleo. No grains (corn, soy, wheat, cereals, pastas, etc), no refined sugars (especially no fruit juices or candy or soda), no seed oils (corn, canola, soy, etc), no legumes, no dairy (although a little bit of hard cheeses that are low/no lactose are generally okay). Yes to meat, yes to veggies (although I skipped starches like potatoes for awhile), yes to water, yes to coconut and olive oil.

Fat and meat are not your enemy, dietary cholesterol does not lead to higher blood levels of cholesterol (in fact, the opposite), and no more eating tasteless bland rabbit food salads because some doctor told you to.

I weighed 340 on one January 1st. By the next one, exactly a year later, I weighed 215, with no increased exercise (in fact, I have a bad habit of under-exercising). And not too long after that, I weighed 184. I now weigh 198 because I took up weight lifting, but I've lost even more fat since then.

I used to hate standing and walking, now I enjoy it.

Whats the point of BIFL if you're going to die in your 50s or 60s anyhow; not much of a life, is it?

I sleep better, I have more energy, my brain is sharper. I wish I knew about Paleo years and years ago. You should try it too.
[cwyzqnn] (score 3, diepte 2) My brand!
[cwykxcv] (score 3, diepte 0) New balance.  Durham with orthotic inserts if you need something slightly dressy.  They aren't going to win any style awards but damn do my feet love them. After cruising various threads new balance in general is a popular choice for people on their feet a lot.
[cwz0pys] (score 3, diepte 4) Freeze a bottle of water and roll your foot over it at the end of the day. Especially focus on the arch. It will help you recovery and reduce the inflammation.
[cwyyu6f] (score 3, diepte 2) Check out ZCoil.  They're odd looking, but absolutely rescued me when I was over weight and got bad plantar fasciitis.

Also, since one commenter mentioned r/loseit, I'll just add r/keto (and r/ketoxx, if you're a woman).

Good luck!
[cwymsda] (score 3, diepte 0) Get shoes that have enough room to add an insole & then add one of [these](http://www.walgreens.com/store/c/profoot-care-the-2-oz.-miracle-men-custom-molding-insoles-men's-sizes-8-13/ID=prod400003-product) on top of that insole. For the base insole I'd recommend maybe Powerstep b/c they add some spring into your step to mimic high arches, but you'll have to see what is comfortable for you. If Powerstep doesn't feel right, try Spenco or Superfeet.

I wouldn't recommend doing this in most cases because you lose some stability with that much cushion in your shoes, but you're 300lbs and there probably isn't any conventional way to make that comfortable to bear for 8-10 hours.

Best of luck. Keep working on your weight and eventually you'll be looking back at this instead of coping with it.
[cwyvl86] (score 3, diepte 0) In addition to new shoes, you may want to try compression socks. [Nabee](http://nabeesocks.com/) is a brand started by a nurse, and they have some great looking designs for men too.
[cwyx9nq] (score 3, diepte 0) I work 12 hour shifts on my feet and spent quite a bit of time looking into this although I don't have the excess weight problem. The most recommended tip I saw was to actually rotate shoes during your shift. Different shoes have different pressure points on your feet and moving those pressure points around helps more than any one pair of shoes will.
[cwyz95z] (score 3, diepte 0) Some advice from someone that has lost 100 pounds:

-Calculate your TDEE and eat at least 500 kcal under that value (google works well for this)

-Track everything you eat with decent accuracy (this part is the hardest)

-Avoid drinking your calories

-Avoid eating carbs if possible (increases appetite quite a bit, /r/keto shoutout)

-Do not use food as a reward, it is only fuel

Getting into a solid strength training program will accelerate this process, so I heavily recommend it.
[cwzb9ok] (score 2, diepte 3) Mind sharing what your orthotics are like? I have 3/4 length firm ones with very high arches and memory foam padding and my feet just never seem to really improve. I've had several sets over the years and they all cost $400+
[cwzbyuv] (score 2, diepte 5) Several. They usually look at my spaceship high arches and say "We need to give you a custom orthotic" and then it just doesn't change a ton, even after several adjustments. A bit better but it's been a decade and I still have bad feet.
[cx5f310] (score 2, diepte 7) I don't see how listening to Country Music Television has anything to do with my feet


I actually just looked that disease up though, and it doesn't sound like me. CMT is nerve damage and loss of muscle and feeling... mine is more plantar fasciitis and clearly some tearing feelings on certain ligaments, expecially when I'm not warmed up. Thanks though.
[cx0oofj] (score 2, diepte 6) Try some of these: http://orthoinfo.aaos.org/topic.cfm?topic=A00667

A couple years ago I had gotten a couple bad ankle sprains from rolling my feet because I wore 8'' boots too much, and had weak muscles. These exercises helped a ton.
[cwyo4q5] (score 2, diepte 2) Then I would focus on a nice cushy sole, possibly even an gel/foam insert for an existing shoe. It's all about weight support for now, literally. BIFL criteria like nice fabrics, leather, and quality stitching won't help you, and any money you spend on that now will just be wasted - if you're 300lbs you'll likely lose a few shoe sizes when you get healthier.
[cwz6njv] (score 2, diepte 4) I've always worn closed toe Birkenstocks when working front of house and clogs working back of house.
[cwyn1ol] (score 2, diepte 1) What he said. 

You will have a better back, neck, shoulders and feet with a drop in weight. I know it's easier said than done but it never hurts to work toward a better you. You will be amazed how much better things get as you hit your goals.

In the mean time analyze your posture and look into supportive insoles and that could help correct any issues. 

I hike 4 miles everyday with New Balance shoes and they have always been great to me. I also own a pair of Rockports that are more business friendly that do me well.
[cwz6bfa] (score 2, diepte 3) Im all over with them. Currently I think Im on a pair of 710. I always go for the assembled in USA or made in USA when I get another pair. I have a pair of 501 and 750 as well.
[cwzcybn] (score 2, diepte 5) If you're in London I will give you my Us and UK size for various brands that might help you with sizing.
New Balance : 12US 11.5 UK
Nike: 11US 10UK
Adidas: 11US 11.5UK
[cwz74bg] (score 2, diepte 1) Green superfeet huh? I should get a set of those. I wear Carolinas for about 9 hours a day on concrete too.
[cwz8zl6] (score 2, diepte 2) I'd go for the orange.  I started with the green and while they were great, my feet still fatigued.  The orange gives great support and adds cushioning for those long days on concrete.  They turned a 6 hour pair of shoes into a 12 hour pair of shoes, no joke.
[cx06yb3] (score 2, diepte 1) I bought superfeet for my workboots too. First week, nothing special. Now I don't notice my feet at the end of the day. 160 lbs, residential construction.
[cwyto4c] (score 2, diepte 0) If I were you I'd go see an orthopedist and get some custom made inlays.
[cwyum31] (score 2, diepte 1) If you have flat feet or have a severe heel strike definitely go with orthotics.As far as footwear:  Try Blundstone boots.  I live in the Northwest and they have lived through 4 years of wet winters and dry summers.  Still look new.
[cwyunai] (score 2, diepte 0) I'd definitely recommend you see a foot doctor and see if you need arch supports or any other orthopedic support. Along with losing weight definitely try to have as good of posture as you can. I know there are days where I slouch a bit and my feet and back kill after work.
[cwyvuxr] (score 2, diepte 1) I second this. I doubt they'll last long, but they should last through the weight loss period, and they're not very expensive. Very comfortable.
[cwyvryn] (score 2, diepte 0) Keen shoes for sure!  Bought a pair to wear in Europe on a trip.  Walked 30 km a day without a blister or sore feet!  Good luck with everything and keep going!  The ones I wear are Kaci.  http://m.keenfootwear.com/search?q=Kaci. They come in all the colours you need!
[cwyws6j] (score 2, diepte 0) Try a shoe by Keen. They make pretty comfortable shoes and boots. They also specialize in wide sizes. Im not making a joke at your expense, I have very wide feet and have struggled all my life to find footwear that doesn't hurt. In this modern day, when the art and trade of cobbling is almost gone, Keen might work for you.
[cwyymoz] (score 2, diepte 0) Dansko.nuff said
[cwz0xnl] (score 2, diepte 0) Birkenstocks are amazingly comfortable. They make a small range of shoes that don't look completely ugly. They also make insoles which would help you a lot.
[cwz23iw] (score 2, diepte 0) Superfeet, green or orange(even better), give them a week for you to get used to them. For shoes dress casual, Ecco. Most use a TPU sole that is great for shock absorption and extremely durable. They are more up front but will last a really long time. Get 2 and rotate them. Do this soon before you really hurt your feet.
[cwz5u1n] (score 2, diepte 0) My girlfriend swears by Danskos, she's in her feet bartending and serving all day. It was amazing to see the difference it made when she started wearing them
[cwzacy1] (score 2, diepte 0) I sold footwear for a long time. With your weight, I'd heavily suggest a backpacking boot designed for long term walking under heavy load that is business casual looking. The inside of the footbed is going to make a bigger deal than an insole at your weight. The insole will help future planar fascia issues, but getting a shoe that is made to hold up weight and protect the small bones of the feet while reducing shock to the knees and hips will help a ton. 

The non-prescription insole market is dominated by one brand Super Feet. You have to be eased into them, they're not Dr Scholls gel stuff, but a hard shape to keep your arch from doing most of the shock absorption to your walk instead of the rest of the leg. The arch is the easiest to damage long term, so it's typically worth it.

In answer to your problem, might I suggest the **Lowa Rengade Low Top**. [I've sold this option time and time again.](http://www.amazon.com/Lowa-Mens-Renegade-Hiking-Shoe/dp/B00KR48R7W) They are great looking, well made, and super comfortable. The problem is that they're not super wide in my experience. You could possibly try some on at your local outdoor store (REI or whatever). You'd probably have to try the high top, but who knows.

If you want like the maximum possible comfort and could possibly get away with the look, [Asolo TPS 535](https://www.asolo.com/en/products/backpacking-en/triple-power-structure-en/tps-535-lth-v-0m2064-00-en.html) has one of the nicest designed soles of all time. The rocker helps reduce the effort of small muscles during the walk, and the shock absorption of the shoe under load is second to none. Toss some nice laces on, and maybe.
(64 reacties met lagere score weggelaten)

=== THREAD 135q31x ===
SUBREDDIT: r/medicine
DATUM: 2023-05-02  SCORE: 184  REACTIES: 114
TITEL: Back Pain and Foot Discoloration [⚠️ Med Mal Case]
POST (source_id=post):
https://expertwitness.substack.com/p/back-pain-and-foot-discoloration

tl;dr

Man with chronic back pain presents to the ED with back pain, leg pain, foot discoloration.

Seen by PA at first visit and NP at bounceback visit.

Both felt it was sciatica, and discharged him.

Leg amputated a few days later for arterial occlusion and DVT.

Plaintiffs asked for $16M, defense said no.

Plaintiffs win at trial, get $20M verdict.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jikp7xz] (score 192, diepte 0 OP) A few things I found interesting:

1. The EM group was sued too, so they’re also on the hook for the $20M. Even though the physician partners didn’t commit malpractice individually, looks like they might end up bankrupting their business because they chose to staff fast track with no supervision or collaboration.

2. This jurisdiction is a bit unique because it looks like physicians can be experts against NPs and PAs. There are some places where this lawsuit would be dismissed because physicians can’t be experts against NPs and PAs.

3. I do think this was malpractice BUT it was a harder diagnosis that I originally thought… patient led them astray at several points. Checked in with foot issues but then wouldn’t stop talking about his chronic back pain. The NP realized he had motor deficits at the second visit but the patient was like… no, it’s always that way.

4. “Fast track” is a recipe for disaster. Cognitive bias makes it hard to find that subtle emergency, which are the hard ones to diagnose anyway! Obvious emergencies are easy. Not to mention the pressure to not do big workups, which is how you diagnose subtle emergencies anyway.

EDIT: Got an anonymous comment saying that this group was set up so that ESI 4 and 5 were seen by NP/PAs. They could ask physicians for help if needed, but physicians did not see these patients unless asked. This seems quite risky because it incidentally places a ton of responsibility at the feet of the triage nurse.

EDIT 2: For all the docs thinking "I would never miss this", here is a case of a lady admitted to an inpatient service who had a very obvious femoral artery clot (way more obvious than this case) that was missed for days: https://expertwitness.substack.com/p/expert-witness-case-32
[jilcj4n] (score 130, diepte 1) I’ve found fast track to be a minefield. We did fast track as residents and I think my most notable find was a coronary artery dissection in a 23 year old female with chest pain. My attending even berated me for getting a troponin.
[jilhqg7] (score 105, diepte 2 OP) Fast track is like running through a minefield with clown shoes. Main ED is like running through a minefield but with a metal detector.
[jilrmlq] (score 88, diepte 0) While I can empathize with the challenges of this diagnosis, particularly with what appears to be the history relayed by the patient, agree with what others have said that this was mismanaged. Discolored foot is vascular compromise until proven otherwise and medicine 101. Even worse the 2nd visit with unilateral leg swelling without an ultrasound.

Saying this as a PA, this highlights my concerns with the current models of pushing APP’s into practice without appropriate supervision and support- particularly in an environment that is likely pitched to APP’s under the guise of managing non-medical emergencies when in reality should be treating chief complaints regardless of the assigned ESI as an emergency until proven otherwise. Coming from my practice which includes treating those in an observation unit, I cannot tell you the countless times things that have come our way pitched as one thing that turn out to be everything but. “Social admit” that was in reality severe cervical canal stenosis with cord compression at c4-5, “psych admit” that was RA encephalitis, “age related de conditioning” that was group d strep bacteremia with a source of undiagnosed colonic malignancy, the list goes on…

If any PA or NP is reading this - particularly new grads, those in school, or pre PA/NP - I cannot emphasize enough the importance of understanding your education only scratches the surface of what it takes to successfully practice. Only place yourself in an environment that is there to support and supervise you while simultaneously taking your own initiative to keep learning/not staying complacent.
[jilf1kj] (score 69, diepte 0) Can I willingly give a leg for 20M? Or which one of you wants to jack my leg up and we go halfsies?
[jilml4d] (score 62, diepte 2) I had myasthenic crisis, ruptured ectopic pregnancy, and DKA all in one shift.  That place is terrifying.
[jilhik4] (score 62, diepte 2 OP) Honestly if they had done a workup based only on the chief complaint of foot discoloration, and not done a history, they would have been more likely to make the correct diagnosis. A history is incredibly valuable but sometimes it can really lead you astray. I think it’s a worthwhile exercise with ED patients to look at triage note and vitals and decide on a workup, then do a history and decide on a workup, and compare those two workups in your mind.
[jillwpa] (score 54, diepte 0) Limb complaint = pulse check

This is basic clinical medicine and even though the award is pretty damn high, the malpractice verdict seems fairly clear to me.
[jil6dmi] (score 51, diepte 1) >I do think this was malpractice BUT it was a harder diagnosis that I originally thought… patient led them astray at several points. Checked in with foot issues but then wouldn’t stop talking about his chronic back pain. The NP realized he had motor deficits at the second visit but the patient was like… no, it’s always that way.

Yeah this part stuck out to me too. Not like I want to blame a patient for a bad outcome, but...this dude was definitely saying something during the exam that caused the PA and the NP to both fixate on his sciatica.
[jili1d3] (score 51, diepte 1 OP) Below knee and you can still be super functional and maybe even become an inspirational insta fitness star. Above knee would be much harder to convince me.
[jilnimg] (score 48, diepte 3) Yeah I had quite a few DKAs in fast track haha I had to go to the triage nurse and be like LISTEN not every nausea/vomiting patient is gastroenteritis needing some zofran. If they’re tachycardic please stop sending them to me!
[jil89x1] (score 45, diepte 1) For $20 mil, take both of mine and call me stumpy.
[jil6uvf] (score 38, diepte 0) $20 million seems awfully high for the loss of a leg.
[jildtn2] (score 35, diepte 1) "you should have your diagnosis by the end of the history" proponents in shambles rn
[jila6lu] (score 34, diepte 1) Clinical arguments for and against malpractice aside, your first two points seem like obvious good things. Whoever is choosing how a practice staffs patients should be accountable when those choices backfire (and this seems like a great example of that risk in action) and medical experts should be expected to testify as to appropriate standards in a medical malpractice suit. The patient is not signing up for a lower level of care just because the person they see happens to have different training.
[jiloefq] (score 32, diepte 2) I was scribing in fast track years ago and we saw a young woman who wacked her head on a cabinet standing up. She didn’t meet ct head criteria but we ordered one anyway, she went to OR with nsg for a bleed. I’ll never forget that.
[jilq6np] (score 31, diepte 4) Wait, nausea and vomiting (+\-) abd pain are ESI 3. Full stop. It should never go to fast track.
[jimdof6] (score 30, diepte 4) In Switzerland it's like an urgent care center adjacent to the actual ER to reduce ER load. 
  
More benign stuff gets triaged to the FT.
  
However, we don't do NP and PA medicine.
[jilrggh] (score 30, diepte 5) Our triage made up their own rules.
[jimi003] (score 30, diepte 5) Technically she met criteria for a CT scan. Vomiting (2 or more episodes) is one of the criteria under the Canadian CT head rule and I typically consider late vomiting to be fairly significant.
[jilhw6e] (score 29, diepte 2 OP) Agree. Poor leadership to just throw NPs and PAs out there as sacrificial lambs and cannon fodder.
[jilcd4l] (score 29, diepte 1) My roommate got 80k plus all medical bills covered when he got ran over by a car as a bicyclist.  Had a helmet, so the only real damage that has lingered was his fibula break. Ya, I know it's just the fibula and it doesn't do much. But it made him unable to fold that legs to sit on them. And he says it still something that's holding him back on his run speeds. I joke and say, not much of a loss considering most people can't even go on a run, was it worth it? And in complete seriousness, he says no. He'd have paid 80k to never have it happen in the first place. And he doesn't know how this injury will affect him in old age, it may be chronic pain he'll have to deal with.

So nah, I'd say 20 million is about right. If it doesn't hurt, then there is nothing discouraging them from staffing with NPs. 20 mil may not even be enough of a detriment because of the sheer profit of charging the patient full price for a midlevel who costs 50-75% less
[jimhdg3] (score 26, diepte 4) Worst headache she has ever had, woke up with vomiting in the middle of the night and had worsening headache. I cannot recall all the deets bc it was like 5 years ago.
[jim9omh] (score 26, diepte 0) “He had extensive arterial thrombosis extending through the superficial femoral artery, popliteal artery, posterior tibial artery, and dorsalis pedis artery.

He had a DVT in the popliteal and posterior tibial veins.”

Uhhh, this a bit extreme for a 35 year old, is he suffering from sort of hereditary thrombophilia? I feel like it would be interesting to investigate the patient’s possible coagulopathy.
[jim1pog] (score 25, diepte 1) It's utterly insane that physicians cannot be experts against nurses or PAs in any capacity. It's not like the patient physiology changes based on who they are being seen by.
[jilw147] (score 24, diepte 1) 100000% agree with all this - fellow PA.
[jimgmpx] (score 22, diepte 4) It’s essentially supposed to be used for those triaged as low acuity to get them in and out quicker. Stuff like suture removals, simple lacerations, cold symptoms, etc. 

What mine was in residency was “what the triage RN thought was low acuity” which essentially meant I saw a lot of NON low acuity.
[jim0jvl] (score 22, diepte 3) If a hospital only had to pay out like $60k each time an unsupervised midlevel fucked up so bad that somebody lost their leg, none of us will have jobs in a week.
[jimk55o] (score 21, diepte 2) Yeah, but both the PA and NP should be been like, ”Okay, but what the fuck is up with your purple foot??” Even I know that limb discoloration is more important than chronic back pain!
[jimei5s] (score 21, diepte 4) In general, these are lower acuity patients with lower acuity complaints. For instance, people with viral URI like symptoms with normal vitals, people in for medication refills, people with UTI symptoms, etc. 

Basically things that require minimal work up and have low probability of serious pathology. 

I think anyone in EM can attest that while these patients are billed as lower acuity that there are snakes in the grass that would be easy to miss but have high risk pathology.
[jilevoo] (score 21, diepte 1) I couldn't read the whole thing because of the popup, but if the loss of the leg made it so the plaintiff (a 35-year old individual) was no longer able to do their normal job that goes to quality of life and measurable harm in lost income. So $20 mill might be appropriate in that instance. If you're a surgeon and had a hand amputated at the age of 35, how would that fiscally impact your career?
[jim60tk] (score 20, diepte 2) This is where the real value of actual clinical experience and clinical acumen can be seen. In med school, our teachers always told us that real world medicine is rarely, if ever, like the clinical cases we see on boards and in books. You need to see many patients and see something several times to avoid being railroaded by patients' often inaccurate histories and basically develop a "6th" sense or "clinical instinct" that basically lights up when something just feels wrong. Even experienced doctors can make such mistakes, much less NPs and PAs who have a fraction of the training/clinical experience.
[jim7tvk] (score 19, diepte 3) What is a fast track? I am not from the US hence I am not familiar with the ED practice environment.
[jilw6so] (score 19, diepte 2) I guess I’m in the minority when I say that you couldn’t pay me 20 mil to lose even a foot.
[jilyqc5] (score 18, diepte 0) “severance” pay
[jimvwpx] (score 18, diepte 0) > He prescribed Valium and Percocet and discharged the patient home. 

dafuq?
[jime63x] (score 17, diepte 3) He was actually really humble about it but also said I was a disaster magnet on fast track lol
[jilc6zy] (score 17, diepte 1) Why not 100 million or a billion dollars? Where do these absurd numbers come from?
[jily8w8] (score 16, diepte 1) I was thinking both legs. Below the knee. Then I can get prosthetics to make me 6’ plus
[jilojoc] (score 16, diepte 1 OP) Agree. I've wondered though.... would it have been easily detected just by checking a pulse? It was clear that there was some blood flow there, based on the fact that the limb wasn't totally white and ischemic. So there very well may have been a palpable pulse (albeit possibly weaker, harder to say). We know from cardiac arrest literature that palpating pulses is a notoriously poor clinical test.  So while I think that documenting a pulse likely would have helped their legal defense, I'm not entirely convinced it would have changed the medical outcome.
[jilyl4l] (score 16, diepte 2) Personally if a limb has questionable arterial flow (whether based on history OR exam findings) I do a bedside doppler US first.

If there is any remaining doubt after that I'm sending them for formal vascular US and/or CTA
[jimgnuj] (score 16, diepte 1) 100% agree, also a PA.
[jilip6y] (score 15, diepte 2) I’m down for a CFJ disarticulation for 20M
[jimgwm2] (score 14, diepte 3) I’m going to assume there must have been some significant historical factor or physical exam finding because I would never send a “bumped head on cabinet” young female to the CT scanner.
[jimm8xe] (score 13, diepte 4) In the US, because many people don't have health insurance, the emergency room is the only way for them to get healthcare (since the ER must still treat everyone, regardless of insurance). Therefore, the ER has a problem of uninsured people (and some insured people who just come to the ER for some reason) coming in with non-emergency medical needs such as upper respiratory illness, or medication refills.

The Fast Track at my hospital is a clinic set up next to the ER. For patients deemed to be non-emergency, quick cases, they are sent over to the fast track clinic. It is usually run by a mid-level provider.

It is an attempt to decrease the workload of the ER itself, and get rid of non-emergency cases. However, it sounds like at some hospitals, all 4's and 5's are sent over to the fast track, which is dangerous since the triage nurse is not always right. 

It sounds like some other countries have the Fast Track too, but it's particularly a big thing in America for the reasons I mentioned above.
[jilajte] (score 12, diepte 2) Or maybe like an ounce of flesh from the non-dominant pinky toe for like 50k.
[jim0kf4] (score 12, diepte 1) Dad?
[jimhwja] (score 12, diepte 0) Maybe I've had the benefit of seeing cerulea dolens twice.  One presenting with back pain and a completely blue leg in a 20 something year old. Other er diagnosed with sciatica. I've also seen sciatica type presentation be dvts. 

But this seems a pretty bad miss. Blue foot? New deficits or not that's a vascular problem
[jinl503] (score 11, diepte 3) Idk, I had a patient be diagnosed with “gout” twice and treated twice by MDs who ended up actually having her rheumatologist notice her dead toe (later amputated -> septic -> died) because nobody thought to look at the bottom of her foot (well… and one was still doing the COVID “telehealth” bullshit).

Even ostensibly experienced practitioners fuck up sometimes. It’s inevitable. I’d be lying if I said I was any different (it’s just one of those unknown unknowns), and I think it’s good to retain some humility.
[jin5o19] (score 11, diepte 3) The thing is, these sorts of cases are actually just inevitable for fast track. Even if patients are completely appropriately triaged, which never happens in practice, if you send enough 20 year olds with head injuries to FT you will eventually have one with a brain bleed. Rarely, initially benign-looking fractures end up in the OR too. A small but measurable percentage of back pain patients need a CT or MRI. Sometimes a sore throat is a PTA or RPA.

Then once you factor in the intentional and unintentional mis-triaging universal to fast tracks, it makes it a genuinely dangerous place to work for inexperienced clinicians.
[jim7dmp] (score 10, diepte 2) Pretty sure I read this guy was already on disability prior to the amputation, iirc due to an issue with the other leg.
[jimdsct] (score 9, diepte 2) Yes, I had noticed that in a few other cases, and thought it was wild. What sort of legal maneuvering happened in those states such that doctors cannot stand as experts if the provider is a PA/NP? If they are expected by their employer to act in essentially the same role, seeing undifferentiated patients in an ER/urgent care, how is it acceptable to not judge them against the same standard of care? Especially since the patient probably has very little say in who they are seeing, and is playing the same amount of money.
[jin5eci] (score 8, diepte 2) Clinical experience matters. I’ve diagnosed cauda equina syndrome in an elderly patient who presented with leg swelling. Seen in the ED after a fall about a week prior by an NP who apparently doesn’t know compression deformity = fracture and told the patient her X-ray was “fine.” Then the NP discharged a previously ambulatory person who was now literally unable to walk. 

Then the patient was seen by her primary NP who started her on lasix (no history of heart failure) and completely glossed over the fact that a previously functional person was now having to literally pick her legs up with her hands because they were both so weak. 

Took an MD to piece together that her leg swelling is because she’s not fucking walking because she has cauda equina syndrome after fracturing her spine. 

But she loves her primary NP “because she listens”
[jilnv97] (score 8, diepte 3) If they see themselves as sacrificial lambs, maybe they’ll demand more physicians around?  One can dream
[jinaa9x] (score 8, diepte 3) I’ve had a non zero number of septic joints in fast track
[jimi9eq] (score 8, diepte 6) Okay you’re right. I must be suffering from the misinformation effect. I checked the ct head rules and yeah she woulda qualified with that. I forget the details of her hpi but i remember the attending saying he could go either way. Thank you for teaching me!
[jilyd4m] (score 8, diepte 3) You must be young. I’m old and have mouths to feed
[jimhe2f] (score 8, diepte 3) That’s not the point. The question is how much should a provider trying to do their job in good faith be forced to pay if they make a mistake. This isn’t a guy in a back alley with a chainsaw it’s a person who was trying to do their job and was assigned a verdict more than they will make in 2 lifetimes. It’s unfair. 

To your point should the government pay 20 million to each vet who undergoes aka?  Double limb amputation basically quadrupwork of walking so double limb would be 60 million.
[jim4bv9] (score 7, diepte 5) You sweet summer child
(52 reacties met lagere score weggelaten)

=== THREAD 5g4o82 ===
SUBREDDIT: r/BuyItForLife
DATUM: 2016-12-02  SCORE: 757  REACTIES: 111
TITEL: BIFL Insoles: Superfeet Green. 2500+ miles so far, I've been told they are still good until I completely wear through the foam.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dapkave] (score 257, diepte 0) As someone who sells these, you should really consider replacing them. Although everyone's results may vary, the average lifespan is about two years before they stop being as supportive as they should be. They're great insoles though, just get fitted, and be aware that there is an adjustment period to them.
[daptzsf] (score 216, diepte 1) > As someone who sells these, you should really consider replacing them.

Yeahhh that's what *you would say* Mr. Salesman, isn't it?
[dapqz8l] (score 133, diepte 3 OP) Well I don't have strava tracks or anything for all of it, but I wore them for about 2350 miles of the PCT through this summer, then was able to get 100 miles of the oregon coast and all of my regular jogs and hikes at home since.
[dapqetr] (score 109, diepte 2) Back it up. 2500+ miles in 4 months? Fuck off that's not real.
[dapqtas] (score 81, diepte 4 OP) I can see why you'd think that, but honestly I'm just shocked that they've lasted as long as they have and I wanted to let you guys know.
[dapp09m] (score 57, diepte 1 OP) I bought these in July :)
[dapvu4w] (score 41, diepte 4) Damn dude u salty
[daplm7l] (score 40, diepte 0) Superfeet would disagree with this.

From their FAQ:
How long will Superfeet insoles last with everyday wear?
For 80% of consumers, the insoles will last approximately 12 months depending on body weight, type of shoe and the environment they are used in (i.e. walking, running, work and sports). Because everyone is different, we cannot indicate how many miles it will take to wear a pair out. We recommend replacing your insoles every 12 months or when you purchase new shoes.

And two questions down:

How long will my Superfeet last?
It really depends on weight, gait and use. On the average, our insoles last 300-500 miles for running shoes and every day wear, approximately 12 months of use. Consider the type and size of footwear and the job the Superfeet are doing. For instance, if you wear Superfeet and work on your feet all day, the Superfeet are going to see a lot more use than a pair of Superfeet you only wear in your shoes for an hour at the gym.  

A good rule of thumb is to listen to your feet. When the Superfeet no longer feel like they are giving the same amount of support as when they were brand new, it might be a good time to consider a new pair and switch them out.
[dapiv3g] (score 38, diepte 0) Uhh can you wash them though
[dapvg5l] (score 37, diepte 4) Go get off your couch, lazy ass
[daqade0] (score 34, diepte 5) /u/byubound is likely going for the "well made and durable even if they won't last you an entire lifetime" part. Most stuff posted here doesn't last a literal lifetime but 2500 miles is pretty durable for insoles.
[dapyywx] (score 30, diepte 4) Yeah how dare he talk about cool things he's done!
[dapy9jj] (score 30, diepte 4) I knew it was a thru hiking pair, immediately. I still own my PCT pair from 2013. I've gone minimalist but I still keep these and talk them up whenever I can.
[daq6w02] (score 30, diepte 3) If anyone doesn't know. That is pretty slim.
[dapngi3] (score 27, diepte 2) /r/GoodValue, it's in the sidebar
[daplufk] (score 21, diepte 1) BIFL needs a counterpart for highly recommended items of great build quality that may not last a lifetime.
[dapn4gh] (score 21, diepte 1) Better go back in time and change my collapsing arches in utero, thanks!
[dapx2qp] (score 19, diepte 1) Apologies for the question, but are you a big person? I've had the same green pair I got for free in my daily wear sneakers since 2007 and they're just kind of gross.
[daq8gk4] (score 16, diepte 4) Concrete shoes are always meant to last a lifetime.
[daq5md2] (score 15, diepte 2) Second sentence of rule #1 of this subreddit:

"Users are encouraged to submit products that are well made and durable even if they won't last you an entire lifetime."

Or do you think there is some magical material that would make for a good supportive insole that would also *literally* last a lifetime?
[daqa7tk] (score 14, diepte 4) i don't think four month is something you can call buy it for life.
[daqaxpj] (score 14, diepte 5 OP) My 4 months of constant hiking were probably similar to a few years of casual hiking and running, at least for me. It isn't like they deteriorate with time.
[dapp2sy] (score 13, diepte 5) I'm not here to be interviewed, just letting you know there are inheritable foot issues that can be aided by arch supports. Saying that, because something wasn't but recently treated, that we don't really need it, is silly. I walk like a breaststroker, if you swim you may understand.
[dapnjva] (score 11, diepte 2) >which may seem gross

Why? Do other people normally wash insoles of all their shoes?

Also I have washed mine before, because I did some outdoor training for a few months and there were a lot of swamps n mud n shit I had to go through. Don't put it in the dryer and you're good to go.
[dapo03v] (score 11, diepte 3) Thanks for the info. 

I only use mobile and forgot to look at sidebars.
[daqczc6] (score 10, diepte 2) 'They'll ride up with wear'
[dapob9s] (score 10, diepte 3) I have what is called 'flexible flat foot,' inherited from my dad. My arch collapses when I stand. 

My feet swing out when I walk and I roll my ankles frequently. Good arched shoes are 100% necessary for some.
[dapwdrk] (score 10, diepte 3) > I'm not an expert on this

Oh don't worry, we know.
[dapjjii] (score 9, diepte 1) I haven't yet - which may seem gross, but its my guess that there wouldn't be a problem - unless the plastic/whatever they use for the support warps in a hot dryer. Not sure a dryer would even be necessary though. I could also see the edges fraying.
[dapvwix] (score 9, diepte 2) But it for life is supposed to be about these too, first rule of the sub is:

This is a subreddit emphasizing products that are durable, practical, and made to last. This is not a place for untested products or newest gadgets. Users are encouraged to submit products that are well made and durable even if they won't last you an entire lifetime.

I think too many people take the "for life" part too literally, it's a sub about well made products, even when they don't last an entire lifetime.
[dapue45] (score 8, diepte 1) I'm wondering about these.  Is there a particular model that's for overpronation?
[daq62ww] (score 8, diepte 3) Concrete would probably last a long time...
[daq8wsu] (score 8, diepte 4) As someone who is five eleven, 145lbs, yeah it is.
[dappmt5] (score 8, diepte 7) If you took a second to google the condition you'll see it is genetic and heritable. I have had to deal with both the negative physical symptoms and people makimg fun of how I walked my entire life. Sure made middle school fun.
[dapgvt9] (score 7, diepte 0) I switched to Birkenstock Blue Footbeds and threw away five pairs of Superfeet. Try 'em.
[daqd4dy] (score 6, diepte 5) but for me 2500 miles could last a lifetime! /s
[daqa1h5] (score 6, diepte 3) Wow I read six foot seven 163 lbs and was thinking you were a post or something lol
[daq25nf] (score 6, diepte 0) God, I hope they were green to begin with.
[dapjeni] (score 5, diepte 0) I can vouch for these - I have a few pairs and a sky high arch. My only issue is that they can be uncomfortable because they are very stiff, but they do the job, well.
[dapvz4l] (score 5, diepte 2) Usually something with a lower arch. Blue is a good starting point
[daq0zz9] (score 5, diepte 1) So, not BIFL material?
[dapugh8] (score 5, diepte 4) Didn't happen in this case but I feel like some subs are super condescending about not reading the sidebar, when for most users that's hidden behind a menu or two.
[dapw9s1] (score 5, diepte 0) I've been buying Spenco Polysorbs. They saved my feet after trying a few Walmart/Grocery Store "premium" insoles. If you can squeeze it and it feels soft and nice underneath your fingers, it probably won't hold up to deliver support under however much you weigh. Plus, both insoles are usually back to back, so you get to feel the double thickness of them both together, which your feet won't get. Remember, you can squeeze with about 5-10 pounds worth of force using your thumb, if that much. You weigh over a hundred pounds. Do you think that the sensation on your feet are going to hold up to what you felt squeezing them with your thumb? No, it's going to be almost nothing at all, most likely. 

I've been super happy with Spenco Polysorbs. They saved my feet when I started a new job on hard floors, and I hadn't spent 8+ constant hours on my feet regularly. Each pair lasts me about 6 months, and I can't recommend them enough.

That said, I'm always open to new and better, so I might have to try these out.
[dapptqz] (score 4, diepte 3) It could be, but I took it from a somewhat obscure chicago rock band from the 90's. But I like it! It is from now on a version of "Fick Dich" too.
[daptvsv] (score 4, diepte 3) There are several sizes and you trim the toe box to fit your shoes. Sounds weird but if you want them sized properly, go to a ski shop and talk to a master boot fitter. They can tell you what the correct size for your feet is. 

Or if you don't live somewhere with ski shops, you could go to a specialty hockey shop or anywhere that specializes in products requiring a very precise fit.
[daqa909] (score 4, diepte 1) As someone who also sells, but also needs them and had bothered to do my own research and abuse of the product, I can absolutely confirm that if you can, use them till they break. Don't listen to the "not as supportive" bs. These fuckers are made to last at least a couple years of abuse, or a few thousand miles, not 3 months. I sell more sets this way anyway. 

People are scared to throw 40 bucks at something that's gonna end up being replaced more often than their shoes. It's oldschool shark sales to scare people into frequent replacements. Don't do that.
[daqd1s4] (score 4, diepte 1) Agreed. This is like looking for a BIFL toothbrush. Some things are meant to be replaced frequently.
[daprvc7] (score 4, diepte 0) What does THAT smell like!?
[dapyok3] (score 3, diepte 6) I run out pretty often. I have a toddler and we sanitizer when we are out. This one time in the Toys R Us bathroom she rubbed the palms of her hands all over the wet floor under the sink. RIP my sanity. 

Although lately we don't go out as much because it's cold so no reason to grab the keys.
[daqoo8p] (score 3, diepte 6) > i don't think four month is something you can call buy it for life.

That's not really even sarcastic, most people would not walk that for a very very very long time.

Most people don't walk the PCT either.
[daqbphj] (score 3, diepte 2) He said ~2500 miles. They last longer?
[daqot3s] (score 3, diepte 6) Both of you must live in concentration camps.
[daq9ris] (score 3, diepte 2) That's this sub dood
[dapwf5t] (score 3, diepte 0) Definitely not BIFL. I can't find the photo but I put a 1yr old Blue insert next to a new one, and the old one was nearly flat compared to the new one.
[dapuwpw] (score 2, diepte 3) I clean my removable insoles every once in a while yeah, they get pretty gross
[dapy9rq] (score 2, diepte 4) Lucky for me I buy too many cute wallets.

Washing keys though ermmm no. I have hand sanitizer attached to my keys for a reason. 

Weirdly enough I wash my phone case because toddler.
[dapygkf] (score 2, diepte 5) > I have hand sanitizer attached to my keys for a reason. 

But do you use it on the keys to clean them or do you just hope you member to use it on your hands after handling your keys?
[dapp4dt] (score 2, diepte 2) Is your username a great version of "fick dich"?
[daq8fno] (score 2, diepte 3) I second the blue.

These things are amazing.
[daq1iwo] (score 2, diepte 2) Nope. Assumed to be replaced every few years.
[daq9qip] (score 2, diepte 5) Oh... Because they make swimming difficult
[daqu424] (score 2, diepte 7) Please rescue me.
[daq7oou] (score 2, diepte 2) Depends how you are using them, hiking, running ect
[daqf786] (score 2, diepte 1) Interesting advice regarding Powerstep & WIIVV. I have Superfeet Green, and find them to be a bit expensive. They're definitely OK insoles, but I expected the Superfeet would make more of a difference, especially for the price. 


One advantage with Superfeet is there're a lot of variants. (Downside: difficult to know which ones are best for you.) With Powerstep, I have the impression that it's even less clear which variant you should pick...


Still, I might look into it when my Superfeet are up for replacement.
[dapp74c] (score 2, diepte 1 OP) I am comparing them to a pair that only has around 50 miles on them right now. I'm curious as to what causes them to 'wear out.' The arch height and and shape are for the most part the same, besides indents where my toes go, the foam on the front of the foot being packed maybe a millimeter thinner, and the obvious loss of the green fabric on the top. I cant imagine the packing out is an issue as it isn't a cushion layer like what packs out in shoes, and it isn't like they are flattened at the arch at all. Unfortunately I don't have a new pair cut for the same shoe so I can compare exactly how they feel.
[daq978w] (score 2, diepte 4) I roll my ankles all the time. 

I didn't know that was a common thing. 

Any advice as to how to deal with it?
[dapuc0n] (score 2, diepte 1) She didn't know what to say.

I was like "Bitch, don't make me ask you again."
[dapytn3] (score 2, diepte 3) Oh my fucking god.

Bro 😂😂
[daqouur] (score 2, diepte 1) Insoles can NEVER be for "life", what the fuck are you people even thinking.
[dapz9dc] (score 2, diepte 0) I use orange Superfeet and really like them.  They have more of an arch support than the greens.
[daq8olx] (score 2, diepte 1) Did you follow the instructions and start their use slowly? Two hours the first day, four hours the next, and so on.

I can't imagine going from nothing to using them 100% of the time. My feet would be screaming after six hours the first day.
[daq7e49] (score 2, diepte 0) Get custom carbon fiber insoles from a chiropractor. Mine are showing minimal wear after 5 years. About $250
[dapq2wl] (score 1, diepte 3) because I've had them for 2 years, and with feet comes funk. just thought some hyper-hygenic person may get skeeved
[dapxwsb] (score 1, diepte 3) People wash them about as often as they wash their keys or wallet.

*shudders*
[dapuhkr] (score 1, diepte 2) That's why you don't put them in the drier..
[daqcr3d] (score 1, diepte 1) Yeah, I can almost smell these through the picture.
[daplz93] (score 1, diepte 1) Did you have them sized or did you just buy off the shelf? The support is supposed to sit at the back of the arch to take the pressure off the rest of your foot. Sometimes you have to size up or down depending on your arch shape.
[dappwij] (score 1, diepte 2) of the shelf at a chiropractor. No custom sizing I think they have 3-4 sizes.
[dapw1qg] (score 1, diepte 4) My bad - I probably just thought that because I'm a size 12 and didn't have to do anything. thanks-
[m32a5s1] (score 1, diepte 4) Do they sell super feet inserts at ski shops
(36 reacties met lagere score weggelaten)

