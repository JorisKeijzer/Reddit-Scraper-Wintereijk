# Label-batch batch_0002

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
Schrijf het resultaat naar `batch_0002.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(6 threads: 1n5i8r5, 1n5nlsu, 1nm6nlw, 1n6r1xe, 1n7gz4l, 1nm9jw0).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1n5i8r5 ===
SUBREDDIT: r/FootFunction
DATUM: 2025-09-01  SCORE: 8  REACTIES: 25
TITEL: What’s going on?
POST (source_id=post):
(These photos are a couple days apart)
Here’s some context: 
I’ve been dealing with this situation for over a month now and nobody seems to know what’s going on. It started as a couple red bumps on my toes and has progressed into this. As you can see in the photos 4 toes are swollen and they can get very itchy.  I scheduled a doctors appointment at a same day clinic a couple weeks ago, but they didn’t seem too worried about it and was more worried that my foot was blue/purple. I got injured October 2024, and I’ve been dealing with my foot turning blue/purple, randomly getting cold as a popsicle, and a cold sensation shooting up the back of my leg. I do have an appointment in November because they want to see how much blood flow Is going to my foot, but I don’t know if that has any involvement with the current situation. Any help or suggestions are greatly appreciated :)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nbstj2y] (score 33, diepte 0) Go to a doctor please
[nbswtjf] (score 17, diepte 0) I think you should ask for a neurologist appoimtment, and do the EMG/NCS to check the nerves. My leg looked the same, the doctors didnt diagnose me for more than 5 months until my nerves started deteriorating badly. It ended up being a peripheral polyneuropathy, with POTS   ...because my nerves were damaged in my legs I had blood pooling in my legs.
[nbu12q9] (score 9, diepte 0) Please go to a doctor asap. Blood looks to be pooling in your extremities - in this case your left foot. Either that, or some tissue is breaking down/bleeding, and it's looks to be more widespread than one toe. If this goes on too long you may not recover 100%
[nbwyfr4] (score 5, diepte 0) Do your feet get cold? Mine look exactly like this in winter when my Raynaud's and chilblains play up
[nbx011a] (score 5, diepte 2) I genuinely think this is poor circulation and you have severe chilblains as a result (they can be SO itchy).  But it's very strange for it to be in one foot only.
[nbx2x7b] (score 4, diepte 3 OP) They were SO itchy in the first couple weeks but have calmed down thankfully. I didn’t mention this in my post but I do have the same thing going on with my right middle finger, just only one really swollen bump.
[nbx12aq] (score 3, diepte 1 OP) Thank you for the suggestion! I have an appointment tomorrow, so I’ll definitely be requesting to see a neurologist. I’ve had X-rays and a mri done from multiple doctors and was told everything looked fine and basically brushed me off. But as we can all see, something is clearly wrong.
[nbxii04] (score 3, diepte 4) I agree it looks like chilblains. I have raynauds and have this happen often in the winter. I forget during the summer and then boom…
Icing my foot a lot from injuries I think damaged the microcirculation years ago. 
Chilblains happen from getting super cold (raynauds causes this even when it’s not that cold!), then warming up too fast. So don’t put a cold foot on something hot! Best of luck- keep us all posted!
[nby0f5k] (score 3, diepte 0) I had complex regional pain syndrome. It was excruciatingly painful and I’m not sure if you are having pain. My CRPS looked a lot like this. I also have POTS.
[nbsxgai] (score 2, diepte 1) And yeah, it also started with an injury to my leg that didnt heal properly for months
[nc1cbr5] (score 2, diepte 5) Three months.
[nbwzcgf] (score 2, diepte 1 OP) Only my left foot does, but it gets freezing cold like I buried it in snow
[nbzrva6] (score 2, diepte 2) Yes. It took nearly 8 years of intense and varied treatment and my foot is not “normal,” but I recovered. I’m so grateful.  I am 51 now and had CRPS from age 31-40 ish. I mean the physicians think of me as still having it but it being in remission. Left foot/ankle, prompted by ankle twists that blew up into PTT and CRps. I went from training for a half marathon to being completely disabled in about a span of 2 weeks and my dx was delayed because this was 20 years ago and very few doctors knew much about CRPS.
[nc2yzpm] (score 2, diepte 0 OP) Small update: First, I wanted to thank yall for your suggestions! I didn’t think my post would gain any attraction. My doctor believes it could possibly be chilblains, but requested blood work and prescribed a steroid cream. Some of the blood work is gonna take up to 2 weeks for the results, which means my post will be “dead” by then. I’ll still continue to update on what is happening just in case someone else is in the same boat.
[nbvamf4] (score 1, diepte 2) So how did you fix it or what was the solution? This started happening to me after a foot injury over a year ago and doctors don't know what it is or what to do. My feet turn a dark grayish/purple.
[nbxhnb2] (score 1, diepte 3) I'd also like to know after a foot surgery that damaged my nerves.  It turns a dark purple whenever it's not elevated and is numb.
[nc04ly4] (score 1, diepte 4) how much time ago was your surgery?
[nc2ufhz] (score 1, diepte 6) Thats scary I hope you heal well
[o5ud9rj] (score 1, diepte 6) Hi, sorry I haven't seen the comment earlier. It was the same for me, my left foot was numb up until my glutes when  I was at my worst and the right leg up until my thigh. It took me a year and a half before it started to get better. I took a lot of supplements starting from month 8 I believe when I finally reached some diagnoses, the doctors were really slow in my case unfortunately (although I read about scenarios much worse where people didn't get diagnosed for years or decades which is scary) and even then I had most answers before them...most of them didn't take my symptoms seriously, not even the ones that were clearly visible like purple swollen legs and passing out due to high HR. I found most of my answers actually here on Reddit after I realised what was happening to me - physical therapy  (magnetotherapy in the beginning then laser therapy and electricity for my feet and ankles...also ultrasound therapy for my neck) - it took me approx. 2-3 months of exercising while lying down and strengthening my glutes and thighs where I still had some muscles left. as I could not get up, walk, or put significant pressure on my feet and ankles and I had distal symmetrical foot drop my muscles on the shin bone were practically non-existent...then later I started focusing more on my feet, ankles. Nutrition is also very important - through food and supplements, I was very deficient in vitamins especially vit D, B1, B6, B9, B12 (do a very good research before supplementing and take out blood tests). I focused a lot of my time on breathing exercises, massaging my own feet for hours and hours and keeping them warm)...also other means of vagal therapy due to vagal dysfunction (my whole autonomic system started to deteriorate due to the prolonged inflammation in my body). so yeah it was a long run but I can say now that in the past 6 months I can see a huge improvement finally, I can walk without crutches, my ankles are minimally swollen and ROM came back - not yet fully but it's looking good. I am also seeing great improvements in my HR and symptoms related to my POTS (and I refused to take medications like beta blockers as I didn't want to start to take medications considering I just turned 31 when it all happened and I found many young people can get better with these tactics in cases where the doctors catch the diagnoses early) If I remember anything else I will write here. Also, If you have any other questions I can maybe answer, please feel free to ask! Hope you get better soon!
[o5udhg5] (score 1, diepte 3) Hey please see the comment I just posted!
[nbw3xpt] (score 1, diepte 0) Your toes on your other foot are not looking healthy either.
[nbyg50h] (score 1, diepte 1) "Had" as in you recovered from CRPS?
[nc050pr] (score 1, diepte 3) I have this rn (CRPS/spasticity/rigidity/equinus varus- no stroke) whats PTT?
[ncgy2vn] (score 1, diepte 4) So so sorry you’re dealing with CRPS. It’s hell. PTT - sorry. Posterial Tibial Tendonitis.
[neh08bt] (score 1, diepte 5) Oh I may have this too the tibia and gastro are where they plan injecting botoxI have many tendonitis coming out from compensation... Im sorry for you too I know what you mean!

We will get our lives back !
[nbyg811] (score 1, diepte 0) You said you got injured, but to clarify, did you injure the foot that's turning purple now?
[nbyjep0] (score 1, diepte 1 OP) Yes. My ankle will “lock up” and I will have to pop it so I can walk normally without pain. I don’t know the reasoning behind it but I got used to it for 10-15 years now. Back in October, it was just another day where it decided to “lock up” again. I popped it not thinking anything and noticed that it didn’t correct the pain, so I popped it for a second time. The pain continued throughout the day but I brushed it off until the next morning when I saw a bruise. I quickly scheduled an appointment and they noticed that my toes on my left foot were blue. They sent me somewhere else and they did an mri and xray but couldn’t find anything. So ever since then, my foot will turn blue/purple but what’s going on with my toes currently is fairly new.
[nc05hbt] (score 1, diepte 2) Oh you have something VERY similar to me. I hope you will get faster treatment than I do but my ankle get stuck and I need to do the samw but my right one cant move back now and I will get botox to reduce the rigidity. happened after an injury too and I get changes of skin colour and throbbing pain. no dramatic temperature change like you tho
[ncgyl5c] (score 1, diepte 3) Are you diagnosed with CRPS?
[negyrui] (score 1, diepte 4) They told me "focal fixed dystonia of right foot with appearance of CRPS". In two weeks or so I will get my first botox injection.
[nbykqj6] (score 1, diepte 0 OP) https://ibb.co/bgDjX1N8
https://ibb.co/DD3VjLzd
These are photos from October 2024
[nbyv8p4] (score 1, diepte 0) Is there any possibility it could be chilblains?
[nbz6xgh] (score 1, diepte 1 OP) Im not sure, I’ve never experienced this before but there is a possibility. Hopefully today I’ll be able to give some type of update
[nckaci4] (score 1, diepte 0) I am not a doctor but I advise you with extreme urgency and ultrasound doppler
[neqjrpd] (score 1, diepte 0 OP) Update: All of the bloodwork has came back and everything was normal except my ESR test. It was slightly elevated by what I’m assuming inflammation because my doctor also tested for autoimmune diseases, etc. which came back normal. The steroid cream that they prescribed has helped out tremendously and so far the swelling hasn’t came back. Also, I know the internet is the internet but I’m on the fence whether I should keep the post up or delete it. I’ve been receiving dm’s from people who have foot fetishes, and if you like my feet looking like that, I guess that’s cool but please don’t dm me 😅 I just want to help others who may be in a similar situation just not THAT situation 😂
[nfz4w3x] (score 1, diepte 0) Hi! Has your doc crossed out rheumatoid arthritis? Docs (where I'm from) don't check for it unless specifically asked, especially if you are under 50, because "yOu ArE toO YouNg To hAvE tHiS ilLneSs" even when I showed ALL the symptoms.   
Your toes look almost exactly like mine did when I was 14-17 and no one took my symptoms serious.  
First I just had these little bumps, then they became bigger, swollen and super itchy, my toes became so big the skin started to tear, sometimes they were boiling hot, sometimes cold as ice. Only when I had the same symptoms on my fingers and I couldn't move them anymore a doc took me serious and was instantly checking for R.A.  
A small dose of oral Cortisone helped me alot and I've been able to manage everything very well since a few years. Now I only have some little  symptoms in the cold winter months, never in the summer .  Your bloodwork showing higher inflammation could also be an indicator for it. Every time I have a flare up, it shows in the bloodwork. Also, how was your Vitamin D? Doc said, flare ups like these could also come from a Vitamin D deficit.   
Hope the swelling still didn't come back :)
[nfze6sl] (score 1, diepte 1 OP) Hi! When I went to my appointment a couple weeks ago, my doctor wasn’t for sure what it was but he thought maybe it could be chilblains. The only thing as far as I’m aware is that he crossed out broken toes and spider bites. I do have another appointment next month for a follow up so hopefully I’ll be told more information, but the swelling and bumps have stayed down since I’ve used the steroid cream. The only thing that hasn’t went away is the discoloration, and gets worse when I exercise or stand up for too long. I’ve been having issues with blood flow since the injury in 24’ but this situation definitely made it more prominent. You’re the first person to ask about my results for vitamin D, and yes I am deficit 😅 I do take medicine for it, but I’m still under the recommendation (supposed to be at 30 and I’m at 29.9.)My body has a hard time “accepting” medicine for vitamin deficiencies in general, so I mainly have to eat foods that have them. Trust me I totally get where your coming from with doctors saying we’re “too young” to have these issues 😂 I was diagnosed with VWD at 17 (symptoms began at 13,) which doctors love to call it an “old person” disease/disorder and would constantly remind me that it would be “rare” for me to have it lol thank you so much! I will talk to my doctor about your recommendation and eventually will give an overall update 😊
[ngnzuvf] (score 1, diepte 0) look up CRPS
[o2wj1c5] (score 1, diepte 0) Updates? I have exactly the same problem since 4 months back.
[o2wp533] (score 1, diepte 1 OP) I forget exactly what it’s called, but I had a study done on my arteries in December and the results came back normal. (They tested for blood flow) My doctor said he’s not entirely sure what is going on but his guess would be possible Raynard’s. His only advice was to “stay warm.” Thankfully the appearance of my foot has improved but I still do have the pain shooting up my calf.
[ncjh96k] (score 0, diepte 0) If you went to the doctor and they’re not too worried about it, I would get a second opinion and ask for a specialist because your foot should not be looking like that at all❤️‍🔥
I hope you get the answer you’re looking for and you heal quickly

=== THREAD 1n5nlsu ===
SUBREDDIT: r/FootFunction
DATUM: 2025-09-01  SCORE: 4  REACTIES: 19
TITEL: Upper laces keep hurting the top of my foot/front of ankle
POST (source_id=post):
The upper lace (circled in red) hurt the top of my foot. I only can lace them loose, because otherwise it digs in the top of my foot. I don't really know why this happens and these are the only shoes I got this issue with. Does anyone have an idea?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nbucoep] (score 7, diepte 0) Dont cross the laces in that area, go straight up
[nbu46zr] (score 4, diepte 0) Google shoe lace variations. You can minimize this by lacing your shoes differently.
[nbu9hy9] (score 3, diepte 1 OP) I can never find one for the top lace
[nbyoqoo] (score 2, diepte 5 OP) I have to try on my next walk. Thanks.
[nbuy0kt] (score 1, diepte 2) Try flat laces.
[nbv1md1] (score 1, diepte 1 OP) Like this? 

https://imgur.com/a/rxLqwbj
[nbvzdxo] (score 1, diepte 2) Not exactly.  From the 4th loop from the bottom go straight up on the same side to the next eyelet, then either cross or tie off.
[nbw9w21] (score 1, diepte 3 OP) Ok somewhat like this? https://imgur.com/a/zaq9BOG
[nbxeaqm] (score 1, diepte 4) Yes.  Does it feel any better?
[nburask] (score 1, diepte 0) Missed using the first eye-loop on top right?   When I broke a shoelace one day, I just threaded the longest remnant skipping every other eye-loop.  It worked, and was comfortable.
[nbuwx3w] (score 1, diepte 1 OP) Missed the top on purpose because it was too tight at my pinky toe.
[nbuzeum] (score 1, diepte 2) Oh, got it. Thanks.
[nbus66e] (score 1, diepte 0) Does your pain go back up towards the ankle above?? There's a weight exercise you can do &/or hang a weight off the front of your foot and move it upwards that area
[nbvcsop] (score 1, diepte 0) I got the laces where I like them on the bottom, tied a knot, then just tighten the top a little tighter when I put the boots on.  The bottom knot stays.  I don't know if that will work for you, it seems your foot is bothered higher up than mine.
[nbvwkcm] (score 1, diepte 0) Many people have a bump on top of their for there.  Skipping that lace works for that.
[nbw9zbn] (score 1, diepte 1 OP) Ok like this? https://imgur.com/a/zaq9BOG
[nbwtgit] (score 1, diepte 0) Maybe look into some wider toe box shoes. It has helped me
[nbxkhhw] (score 1, diepte 0) I have this in so many shoes- my foot is quite flexible. If the shoe is sturdy (this one looks to be), the foot bends at the midfoot at this spot but the shoe doesn’t bend… so the top of the foot and laces there fight.
Putting a flat piece of foam, tongue pad, or even thin piece of silicone (like what hockey players use for lace bite) helps me. Just put between the sock and shoe tongue. It kind of redistributes the laces.
Some have success with relaxing… I do if the hot spot is further down on the midfoot. But up at the top like that I find the pressure just shifts to the next set of laces.  Keep experimenting!
[nby4bp8] (score 1, diepte 0) Sometimes the tongue of the shoe is too thin or shifted, which makes the laces dig in. Adding a padded tongue cover or even using thick socks can help.
[nceec8f] (score 1, diepte 0) Do you have high arches? I have high arches. I sometimes get this same pain. My foot doctor (DPM) suggested it might be due to high arches, or the high arches aggravates a foot nerve. He also said it could be related to having a bunion (I have a bunion on my right foot and I usually only get this similar type of pain in my right foot).

=== THREAD 1nm6nlw ===
SUBREDDIT: r/Peripheralneuropathy
DATUM: 2025-09-20  SCORE: 2  REACTIES: 19
TITEL: PN without Pain?
POST (source_id=post):
I’ve had PN for years now. Unlike a lot of people I don’t have pain per se. I described it to the neurologist like my feet feel like they’ve been dipped over and over in wax and then wrapped in heavy duty aluminum foil. It’s disconcerting, and inconvenient but not painful. It started in my toes only and after 5 years it has come up to mid-calf in my legs.

The finger tips are a whole different thing. Never feel anything except if I try to use my fingertips to pry something open - think: lifting a lid. THAT sometimes almost brings me to my knees. It feels like a red hot ice pick being pushed into my fingertips. It subsides almost instantly when the pressure is removed. 

Wonder if anyone else has something like this happening?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nfb9jqq] (score 5, diepte 2) I had three separate MRIs.  Cervical, thoracic and lumbar.    Both doctors said my symptoms don’t line up with what the MRI shows.   I had a caudal epidural steroid injection two weeks ago which made my Pudendal neuralgia a lot worse, and my pins and needles feel heavier.   Not painful, but more profound.   I’m scheduled for a second injection, but I’m not doing it.
[nfawzff] (score 3, diepte 0) I have pins and needles from bottoms of feet up to knees with no pain for past 4 months.  Above my knees to my thighs is normal.   I also have pudendal neuralgia which is very painful in the saddle area.  So far, neurologist and pain management cannot explain it.   MRI and EMG negative.  Some mild spinal stenosis.  Just hoping things don’t get worse.
[nfc5733] (score 3, diepte 4) Yes.  I will get a second opinion.    I don’t know if I should get a second opinion from another neurologist or from another pain management doctor or both.
[nfcpe50] (score 2, diepte 5) IF you can, I would try getting both second opinions.  Good luck!
[nfeg6so] (score 2, diepte 1) How were you diagnosed with Pudendal
 Neuralgia? Did your Neurologist diagnose you? I suspect I may have this. It is the most excruciating pain I have ever been in. At times it literally takes my breath away. I have some other issues going on as well. I have had so many tests, but nothing really explains my pain. 

I am diabetic, and they think I went undiagnosed for years. Due to this, I have Diabetic Neuropathy. I also have had sciatic nerve pain for the past two years. It has been a long process to get diagnosed with that. I still don’t think they have my diagnosis correct. I have had MRIs of my back, and hip as well as X-rays. I have had nerve conduction studies done and that did show I have neuropathy and some sciatic nerve issues. The weird thing is that all my leg pain is on the right side. The nerve conduction study showed sciatica on my left. 

My hip MRI showed I have bilateral proximal hamstring tendinopathy. Still all my leg pan is on the right. I believe I have tendinopathy, but I also think I have Pudendal Neuralgia. It affects my saddle area and gives me so much anxiety. I am an Accountant and sit almost all day. I do set timers to get up and move around, but the pain is still there all day. 

I take 600 mg of Gabapentin 3 times a day. It does help. I know a lot of people don’t like Gabapentin, but I have not had any side effects taking it. I also take R Alpha Lipoc Acid. 

What does the treatment of Pudendal Neuralgia look like? Is this something that will just eventually go away on its own? I hope you find some relief!!
[nfb55je] (score 2, diepte 0) My hands were very painful, I had intensive acupuncture 7 days straight.
No sure if it’s due to time or due to the acupuncture, but after the acupuncture I had no pain in rest with my hands.

But my hands got weaker, after few months (couldn’t peel a banana with my right hand)
[nfbpe4z] (score 2, diepte 0) I have the same symptoms in the feet and legs. Not hands.  

Question if you don't mind.  Are you a heavy drinker?
[nfc6pqx] (score 2, diepte 1) I don’t drink alcohol.    At one time I was overweight, but three years ago I lost 70 pounds with diet and exercise.    Now I weigh 130.
[nfb4ewo] (score 1, diepte 1) Did you had a full body MRI scan? Lower back, neck and head?
[nfbeovd] (score 1, diepte 3) Did you also get a second opinion?
[nfklkyu] (score 1, diepte 5) I agree with QueenRooibos, an extra viewpoint is always welcome.
Especially if you feel something is not “right” and need more help.
[nfbgqu3] (score 1, diepte 1) Have you had an epidermal nerve fiber density test?
[nfc5tfh] (score 1, diepte 2) I haven’t had the epidermal nerve fiber test.   Does the neurologist do that?    If so, I’m wondering why he did not do it when I was there getting the EMG.
[nfcimmu] (score 1, diepte 3) You can ask, it does require special handling (overnight shipping on ice) and a lab that is able to do the test.
[nfesdt3] (score 1, diepte 2) The neurologist sent me to pelvic floor therapy.  It has provided some relief.   I still have pain all day every day, worse at night.  I bought a cushion on Amazon that helps and I bought a squatty potty.  Gabapentin does help some.   Didn’t like cymbalta and pregabalin.   My feet and shins are numb, but I think it’s referred pain from pudendal neuralgia.  I fell at the gym last week on the treadmill because I can’t feel my feet.  If you go to pain management be careful getting injections.   It made things so much worse for me.  Try not to get discouraged.   It’s easy to start thinking how you can’t go on with this pain.  Don’t give up. Join Pudendal Neuralgia group too.
[nfba0hq] (score 1, diepte 0) Have you had an emg/ncs?
[nfc6j1l] (score 1, diepte 1) Yes.   EMG was negative.   Neurologist said my problems must be related to my spine because my nerves were fine    He gave me cymbalta and zanaflex.    I tried taking both the medications, but I didn’t stick with it.  I didn’t like the way they made me feel and they didn’t seem to help.   I stuck with it for a couple of weeks but ultimately I didn’t continue them.
[nfbgnj8] (score 1, diepte 0) Yes, peripheral neuropathy can present like this.  It does not have to be painful.  An epidermal nerve fiber density test can help make the diagnosis.  A medical food such as EB-N6 from EBM medical can provide key nutrients to the peripheral nerves and may slow progression and even help rebuild the myelin sheath.
[nfc6xrd] (score 1, diepte 1) My primary care doctor had ordered B12 shots for several months, but my levels were never critically low.    Do you think I should see a podiatrist?    Initially, I was taking R-ALA and L Carnitine.   I took it for several months, but didn’t notice a difference.
[nffijob] (score 1, diepte 1 OP) I may have a cocktail once or twice a week. I’ve never been a real drinker at all.

=== THREAD 1n6r1xe ===
SUBREDDIT: r/Podiatry
DATUM: 2025-09-02  SCORE: 3  REACTIES: 17
TITEL: Will applying this late in cycle hurt my chances.
POST (source_id=post):
I’m waiting until after my mcat on 9/13 to submit my application while I gather last minute details. I’m worried applying this late will hurt my chances of acceptance. I have a 3.7gpa, two years work experience as an RN, my mcat practice tests have been around 500. I have shadowed DPM and obtained a letter of rec as well as one from an MD. 

Will applying this late hurt my chances? I’m hoping on getting into midwestern, Des Moines, scholl. Ect. 

Any input is greatly appreciated.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nc2megn] (score 8, diepte 0) No it won’t hurt you
[nc3be32] (score 3, diepte 1 OP) Thanks for the input. I definitely have taken the time to research the field. I don’t think it’s gonna be some path to freedom in anyway but it is a major upgrade from bedside nursing in countless ways. 

The complaints on these forums are 100% valid but let’s be honest, bitter podiatrists gravitate here. I’ve shadowed 4 and have talked to many more in the hospital about the career, and all my interactions have been positive. The only negative in person I’ve experienced was from an older boomer age podiatrist who was bitter about medicine in general because of insurance reimbursement changes. Insurance reimbursement drops are not in anyway unique to podiatry, and are a medicine wide problem. 
 
Can I ask why you decided to not attend?
[nc3hx2n] (score 3, diepte 0) You have such a wider range of options in your career path as an RN. Narrowing it down with DPM seems crazy to me. I’m sure it’s been suggested before but CRNA pays just as well, if not better, and finding a good job would be so much easier. Not to mention shorter time in school with no residency and much lower debt.
[nc2pdd2] (score 2, diepte 0) I applied/interviewed last year at the end of January so definitely will not hurt you!
[nc2r38y] (score 2, diepte 0) I applied this past June and got accepted two weeks before the program began. You’re good!
[nc300hq] (score 2, diepte 0) I applied in March, got an interview invite a week later and got accepted 2 weeks later! You’re totally good!
[nc30epn] (score 2, diepte 0) Almost every school is unfilled from
What I hear. If you truly want, NYCPM is always accepting…

Why leaving RN? By the the time you graduate RNs will be making more than pods… their salaries keep climbing…
[nc3emj3] (score 2, diepte 2) I’m already a decent amount of debt in, and was already in NP as well when thought about switching. I was very into the thought on surgical procedures, diabetic wound care (since I do a lot in my RN role), and terminal end education vs mid-level education. 

I realized both schools definitely oversold the extent of actual surgical, procedural kinda care in hospitals or procedural jobs outpatient clinics from big systems available that I wanted to do when advertising, like the DPMs I shadowed- there’s rarely more than a dozen of these jobs in a region let alone the country available at a given time. And despite there being less than 20k DPMs in the country, they’re somehow also saturated for their level of jobs available. Likely because not a ton of patients still seek/think of foot care, and a lot of diabetics get treated by PCP & oral diabetic regimens or insulin first. 

A lot of the work I see available is nursing home / SNF  rounds for diabetic nail care- not something I wanted to do after another 7 years of training and more debt. All to *possibly* have any hint of regret as well leaving a career side that’s a lot more flexible, and have jobs available anywhere, everywhere, even if it’s saturated (NP), but also easier to work additional jobs or telehealth, etc; whereas there isn’t a ton of flexibility, maneuverability with DPM. You commit and that’s it. 

If I was a little younger and didn’t have my other degrees/debt I likely would’ve continued. I realized I was also kinda pressuring myself because of the BBB bill changes that this would’ve been the last year to get in and use all plus loans. But realize it might’ve been for the best in my situation, as I have a life, wife, mortgage, etc. I also kept factoring in if DPM was miserable, failed, or school didn’t work out, still have an RN which you will as well, so that’s a benefit most don’t have. 

I think RN background will give you great background and prep towards a lot of the courses, as well as clinical training stuff as a lot of students come in with zero knowledge. And I think it gives a unique perspective for care when you do graduate. And if you do well in residency it may help you secure the better very rare lucky jobs available with networking. I didn’t wanna take all the risk/gamble for my personal situation when in 7 years time I may be as well off and practicing fun as I would’ve been as a DPM. But for you with possibly less to worry about/lose I think it could work out for you. That’s just why I say research :)
[nc3iwtt] (score 2, diepte 3 OP) This makes total sense considering your situation. I think I would have a hard time justifying going through with it in those circumstances. Especially already being an NP. I  just turned 25 have only 4,000$ in undergrad loans from my BSN. No kids and a partner who is 100% supportive and will help support cost of living through school.
[ndaj1uq] (score 2, diepte 2) The profession has too many problems, that aren't being addressed. It's not some hidden gem. It's  a hyper saturated, limited doctoral profession
[nc3ymx2] (score 2, diepte 0) That's not late. I'll never forget being on the interview trail 14 years ago. I was hoping to go to Scholl because the guy I shadowed went there, but they lost my app. It all worked out cause I ended up at DMU. I kept meeting the same people at interviews. I'm talking to this girl telling her that I hoped there would still be a spot for me there. She leans in, all secretive, and whispers - "Scholl still has 90 something spots left". The look on her face was something resembling confusion or horror. Nothing has changed. This was in like November. One of my DMU classmates was accepted the week before school started.
[nc3ztnx] (score 2, diepte 0) I applied in March and got interviews at every school I applied to. You’ll be fine :)
[nc70749] (score 2, diepte 0) You should be fine.
[nclrn2l] (score 1, diepte 1) Where did you come from? You’ve never posted on this forum then post on every post and pretty aggressively.
[ncltn31] (score 1, diepte 2) I think this is a better as a private message. I sent you one!
[nc38378] (score 1, diepte 0) Being also an RN, whom applied in to two of those and was accepted to both of those schools, then turned down both for now after researching this field a lot more and the schooling, I’d just encourage you to also research carefully before you do commit. Not to dissuade you as I gained a ton of respect for Podiatry and work with it everyday. But just to know what you want out of it if leaving nursing world. 

You absolutely will get in; your GPA will be over most, and some schools waive the MCAT, both the ones I did (Scholl and DMU) do if you’ve taken other entrance exams. I applied and got in at very end of cycle about 2 days after applying to both. Don’t stress out. It’s the getting through & out of DPM school that’s the more difficult part. And finding a good job, from research.
[nc4m82g] (score 1, diepte 2) "...from an older boomer age podiatrist who was bitter about medicine in general because of insurance reimbursement changes. Insurance reimbursement drops are not in anyway unique to podiatry, and are a medicine wide problem." This is worth remembering, but we need to keep it in perspective. Everyone is exposed to higher interest rates, higher grocery prices, higher home prices etc. But podiatry may be uniquely exposed to poor reimbursement rates. The APMA recently linked to some AMA data showing something unbelievable - like that \~80% of MD/DO physicians are now employed by hospitals, organizations, corporate entities - whatever. I actually thought I was making it up, but then I looked again on Google and I didn't even fudge it. Organizational employment shields these physicians from payor malfeasance. Hospitals can command higher facility reimbursement that can be used to compensate and make up for decreasing professional reimbursement. Podiatrists are much more likely to be solo, small, private etc. An APMA report from 2018 says something like \~70% of podiatrists are private - essentially the reverse of other physicians. We are directly exposed to payor behavior and payors won't negotiate with small podiatry practices. Consider that in my area a 11042 from Medicare reimburses like $120 in the office, but a hospital receives like $400 on the HOPD fee schedule - there's a much bigger pot of money for paying the FM doctor who mans it. And a year ago that $120 was $125. You can sit there and throw shade, but if you enter this profession this declining reimbursement may be your future life story. And it gets even trickier because insurance companies like contracts based on Medicare's fee schedule. As Medicare's rates decrease so do the private rates based on them.
[ne24vtr] (score 1, diepte 3) It's just as bad as physical therapy which I was accepted into a DPT program for this year but deferred. Reimbursement rates go down seemingly every year and in most places PTs don't even earn 100k for 3 years of school and 100k+ in debt. Even in VHCOL areas the max for outpatient ortho PT is about 115k. 

Then I find the same problem when I considered podiatry after submitting my apps last year, but a lot of it I see online is from greedy private practice owners underpaying. 

At this point I may end up just going down the PA path into ortho.
[ne28ag8] (score 1, diepte 4) Yeah - I refer to PT, but I don't know anything about their business model. Was just looking up some of their codes - 97110, 97140, 97530 - which according to Google AI are the sort of codes they use for Achilles tendonitis. They don't appear to be associated with killer reimbursement values.
[ne2a7z9] (score 1, diepte 5) They're not, that's why PTs don't earn much and often times are treating 2-3 patients simultaneously at "mills". Probably lucky to be bringing in 200k in reimbursements in HCOL areas, likely 150-160k everywhere else.
[nccmrr8] (score 1, diepte 1) DPm is not shift work, 100% better life/work balance.
[nd95q9a] (score 1, diepte 1) Why is it that no matter what an OP writes, you immediately tell them not to do Podiatry? It's hilarious. What is your goal by telling everyone to avoid our profession?
[nd9ft5k] (score 1, diepte 2) Weird, I don’t remember addressing you in my comment.
[nc3iu6u] (score 1, diepte 0 OP) This makes total sense considering your situation. I think I would have a hard time justifying going through with it in those circumstances. Especially already being an NP. I  just turned 25 have only 4,000$ in undergrad loans from my BSN. No kids and a partner who is 100% supportive and will help support cost of living through school.
[nc4s2b6] (score 1, diepte 1) scholl is pretty full this year. filled almost 90 i believe
[nc6t0td] (score 1, diepte 0) Wait huh? this isn’t late. Didn’t it just open like July 30th or something?
[nchd7jy] (score 1, diepte 0) No I applied in may before the school year started (3 months before start) and got in. DPM is not the same with this issue as MD/DO since there’s way less people applying DPM
[ncrgvsw] (score 1, diepte 0) Current resident. I applied 3 days before the deadline and was able to get in. You’ll be fine don’t worry!
[nd57d99] (score 1, diepte 0) Can any current NYCPM or Temple students or recents grads DM me, I’m applying soon and would like some insight. Thanks!!

=== THREAD 1n7gz4l ===
SUBREDDIT: r/PlantarFasciitis
DATUM: 2025-09-03  SCORE: 47  REACTIES: 17
TITEL: plantar fasciitis at 24 y/o
POST (source_id=post):
I got my plantar fasciitis (PF) diagnosis three weeks ago, mainly because I gained weight, have tight calf muscles, and do not warm up or stretch before playing sports. 🥲😆

I was advised to use warm compresses upon waking up and before sleeping, and to do foot exercises. However, I found that the "runner's stretch" or "calf stretch" has helped me the most. 

After doing this specific exercise, my pain is almost gone, especially when I wear my favorite Vomero 5 shoes—I can barely feel the pain anymore. 

I was also told that my tight calf muscles might be contributing to the persistent pain in my plantar fasciitis, even after stretching. 

Just wanted to share my experience, and I hope your plantar fasciitis resolves quickly too! :)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nc7npcy] (score 8, diepte 1 OP) My symptoms began three months ago. Based on what I've read in plantar fasciitis groups, I believe my case is mild. I was advised to take Celecoxib and use ketoprofen for a week. 

When I added the runner's stretching into my routine, it helped a lot since heel pain is almost gone now. When I mentioned this to my doctor, he suggested that my calf muscles might be tight, which is why the calf stretching was effective in alleviating the pain. 

What worked for me may not work for everyone, but I just wanted to share my experience with my plantar fasciitis. Thank you :)
[nc82kni] (score 7, diepte 3 OP) Again, i didn’t take any antibiotics. I was only prescribed Celexocib and Ketoprofen for a week. These meds are NSAIDs. 

Kindly read my reply bc I just shared that calf stretching might help relieve the pain. And for me, it helped a lot okay? I clearly just wanted to share my experience and routine.
[nc99qnx] (score 7, diepte 0) Thanks for sharing your experience and the specific stretch that helped you.  Hope you continue to heal and be mostly symptom free.
[ncattc9] (score 5, diepte 0) It’s a weird problem to have, and the support available is all over the shop. There’s people selling you crap, there’s influencers spouting crap about doing this and that, and podiatrists telling you something else and not to listen or anything else. 

I had it for over a year and everyone has their own solution as to what’s worked. So my suggestion is to follow professional advice and try different things if that doesn’t work.

There’s been two instances where things have helped me:
1.	I was on my third session of shockwave therapy, and between sessions the pain stopped for a week… until I went for the fourth session and it flared back up. I should have listened to my body and not the podiatrist.
2.	I just bought a massage gun, and for the last week again I’ve been without pain. I’ve been massaging every night, and as I wrote the above… maybe I should stop!
[ncb61wh] (score 3, diepte 0) Me too! Do you also dip your knee while in that position to stretch the Achilles part? It helps a lot. 

Once I start to feel straining there I do this stretch.
[ncbwgkq] (score 3, diepte 2) Just a suggestion. You can dip your head so you can force your back to line up more seamlessly. You want your hand to back to calf to feet to be as linear as you can. 

But as long as you feel the calf stretch it's fine. Gosh I do it several times a day it feels so satisfying.
[nchtou1] (score 2, diepte 2) Hey mate, not sure if you’re being serious? But go google it and you’ll find heaps of them. I’m using a Bob and Brad X6
[ncbthqa] (score 2, diepte 1 OP) Yes 😄 i have my affected foot (right) at the back then left on the front and bend it to stretch the achilles and calf :)
[ncbi4ve] (score 2, diepte 0) yeah,the calf stretch is helpful to me.
[nccb6o5] (score 2, diepte 0) How long do you hold this stretch and or how many reps? Thanks!
[ncef6wl] (score 2, diepte 0) It doesn’t discriminate against age lol
[ncgzgpi] (score 2, diepte 1 OP) https://youtu.be/vNHOj3ubzbs?si=FCwh0XJ9HjM-JySv

This one. It’s around 4:56 / Stretch #3
[nclb840] (score 2, diepte 0) I have PF in my right foot. I had PF in my left foot last year which took 4 months to resolve. It sounds absolutely right that your right calves need stretching daily. I do that stretch too, although I am convinced my problem isn't in the calves per se, but having had persistent weakness in my ankles most of my adult life.

I do strengthen my ankles with resistance band training, and did a great deal of fascia physio when I had PF on my left foot. So, because both fascias have been exercised over many months, my new right foot PF feels like somewhat of a pseudo PF. Don't know if that makes sense to anyone. I can walk on it quite well, and I even experimented with light basketball training. The discomfort was fairly bearable after training, like a 2 - 3 out of 10. I will continue exercising, but will not overdo it. I hope that I can fix this new PF, whatever it is in a matter of weeks, and not months when I originally got it.
[nccjgye] (score 1, diepte 1) Massage gun? What is that? Could you be more specific?
[nciuvia] (score 1, diepte 3) Thank you
[ncbykgc] (score 1, diepte 3 OP) Yay i’ll try this!! Thanks for the tip 🤩
[ncgz2y2] (score 1, diepte 1 OP) I hold it for 20 seconds and 3 reps 😃 i do it after I wake up, during the day, and before I sleep :)
[ncetdk9] (score 1, diepte 0) A link to which runners stretches?
[ncn3y3a] (score 1, diepte 2) Thank you so you just did that one runners stretch?
[nco2j4w] (score 1, diepte 3 OP) I do all the exercises here: https://youtu.be/uod-dBB11hs?si=ghXivpHiMLV4PIHC then I just added the runner’s stretch. 

I do this exercises upon waking up, during the day, and before I sleep :)
[ncp01r2] (score 1, diepte 4) Thank you so much for sharing
[ncqz3r2] (score 1, diepte 0) This is my go to stretch for PF. I’d also add foam roller on both calves and single calf rolls are a good addition
[ncvbuax] (score 1, diepte 0) i tried this stretch, my PF literally got 5x worse! cant even step on my foot!!!
[nd1wrb0] (score 1, diepte 0) Pretty much same situation.. what do you do to soften the calf muscles ? and what sort of warm compresses ?
[nc7gt81] (score -12, diepte 0) >I was also told that my tight calf muscles might be contributing to the persistent pain in my plantar fasciitis, even after stretching.

I do not believe that is the whole story.

* When did your symptoms first appear?
* When was the last time you took antibiotics?
[nc7ql1e] (score -17, diepte 2) And when was the last time you took antibiotics?

=== THREAD 1nm9jw0 ===
SUBREDDIT: r/Mortons_neuroma
DATUM: 2025-09-20  SCORE: 31  REACTIES: 17
TITEL: Neuroma Surgery Recovery Timeline
POST (source_id=post):
I wanted to share my neuroma resection surgery recovery timeline since I felt like it was a little hard to find that information. For context, I'm a 34 year old female and mom of 2 young kids. I had a very large neuroma between my 2nd and 3rd web space in my right foot, confirmed via MRI. My resection was 2 days ago. I also had a large neuroma resected in my left foot 11 years ago, and have had no issues since. I can't quite remember the details of my recovery, but I figured I would share in real time how this surgery recovery is going!

Day 0 (surgery day) - case itself was about 1 hour, I was at the surgery center at 730, home by 11am! They gave me a good nerve block which lasted the entire rest of the day and night. Minimal pain, I did fine with just Tylenol and Advil. I was advised to stay off my foot and anytime I am up, I have to wear the surgical shoe. I decided to use crutches and not put any weight on my foot, but my doctor said I could heel walk. Personally this was too painful for me.

Day 1 post op - barely any pain, spent most of the day with my foot elevated. Didn't need to take any pain medicine, only took Advil once.

Day 2 post op - a little more soreness today, only took Advil once. Have been up a little more just trying to help with the kids, but when I'm up and moving I have some more soreness. Still using crutches and not really putting weight on my foot.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nfblsbi] (score 9, diepte 0) Hi! I am 35 yo female with a young kid and had my surgery in Feb. Your recovery so far matches mine! I found the heel walking also too painful on the incision at the start but was able to ditch the crutches after 4 or 5 days. My recovery was extremely smooth but I worked from home and was diligent about icing and elevation for the first month. I was cleared back to low impact exercise and regular shoes at 6 weeks. However, I ended up having an allergic reaction to dissolvable sutures which slowed my wound healing significantly. I ended up having a revision surgery in July to remove a retained suture and revise the scar and now I am 100% healed. All of my MN pain has resolved and I'm back to running. No issues whatsoever, I am beyond thrilled with how it went. 

Good luck!
[nfc2ctl] (score 5, diepte 0) I wanted to share my progress in case this helps anyone! I know before the surgery I was desperately looking for a healing timeline. I’m 8 days post op today, have had no pain at all since my surgery, just a bit of discomfort when I put weight on my foot. I was told to walk since I got out of surgery without crutches, which for me ended up being true (shockingly!). Had most of my bandages removed 6 days post op and was told I can start walking around the house in flip flops or slides (I also have plantar fasciitis and the hard post op shoe has been making that flare up). I bought a pair of oofos which help but can’t wear them yet as I realized how swollen my foot was after I put them on. Definitely elevate all the time other than going to the bathroom! Today I managed to go out for dinner and put my foot up at the restaurant - got home and my stitches and ball of foot don’t feel too good so probably bit too soon for that. I still feel a pebble in the bottom of my foot sensation which apparently is normal but a little concerning! My doctor thinks I can return to normal shoes mid next week and maybe get in a flight end of next week. I am a 23 year old female and don’t have a very active lifestyle, so I guess how you heal is just up to luck.
[nfba23w] (score 3, diepte 0) Very much look forward to your future posts! Good Luck!
[nfbcigu] (score 3, diepte 0) Thanks for sharing! Hope the recovery continues to be smooth sailing!
[nfbsdhm] (score 3, diepte 1 OP) They gave me a nerve block once I was under! I was on a general anesthetic dose of a propofol infusion so I was completely out (I actually do anesthesia for a living haha) but there would be no way I would let them do this to me while awake!
[nfd3kyt] (score 3, diepte 4) Thanks so much for the insight! Wishing u a speedy bounce-back! 🫶🏽
[nfc6fa7] (score 3, diepte 0) What did they say about typical time from surgery to being able to exercise again?  Hope you feel better soon
[nfbllfe] (score 2, diepte 0) Wait so was this done by nerve block only, not general?
[nfbxqkn] (score 2, diepte 3 OP) I'm so sorry the second shot didn't help, I had the injections for my first neuroma but I felt like they caused more pain so I wound up with the surgery. This time around I had been dealing with pain for 3 years and I told my surgeon I didn't even want to bother with injections this time. But my pain was so bad and so diffuse that it was hard to localize what web space the neuroma was in so I did have the MRI too. I also wanted to postpone mine as long as possible but mine got to the point where I couldn't do anything at all, it was so limiting, and we're also going to Disney in December so I was like well I HAVE to get this thing out of me before then!

Definitely just get it done! You'll be so glad you did it!
[nhfgka5] (score 2, diepte 4) So you recovered from the first MN surgery?… But then you got a second MN on the other foot?
[nhh9a1l] (score 2, diepte 5 OP) Yes I've been fully recovered from my first surgery on my left foot! 7 years after that surgery I developed one in my right foot. It got really bad when I I was pregnant and I dealt with it for 3 years before my surgery 2 weeks ago!
[nhffuot] (score 2, diepte 1) Hi there. What do you mean by a retained suture? It stayed in there accidentally?
[nfcgbjg] (score 2, diepte 0) I am two months post op! I used an iWalk for the first few weeks- you can return before 30 days! Good luck, keep elevatin!
[nfejrsq] (score 2, diepte 1 OP) I just looked that up, that looks so cool! I feel like I'd fall on my face 😂
[nfhotjv] (score 2, diepte 0) I'm on year two after surgery and year two actually went backwards for me. The bottom of my foot became increasingly sensitive. (Despite the insision being on the top). It now seems to be improving again. 

Anyone else have this?
[nflxd40] (score 2, diepte 2) It was around the 3 months for me also.

I did have bruising come back a few timesover the next year. So seems it was re opening.

For me it seems semi random, but walking/running makes it worse. It's not as bad as before, a different problem, it's more very uncomfortable when bad, rather than the old neroma totally unwalkable. 

For me it seems to be mainly bad directly beneath the scar, but on the bottom of the foot. It's very localized. When "inflamed" massaging that area makes the scar really uncomfortable.

Hope you get some relief from your eventually!
[nflxz2e] (score 2, diepte 3) Thanks, I hope so too.  Having the neurectomy seems to have just traded one problem for another, though the current issue is not as bad as the "pebble in the shoe" thing I had before.  It's always something (grins).
[nfm3uji] (score 2, diepte 2) I have had two neurectomies  (last one was 9 months ago first one was 18 months ago) and have the same symptoms is you. Basically the dr was like well it’s better than before. I’ve tried all the things you mentioned. 

I have no solutions or recommendations except to say it sucks and I’m sorry. It’s awful.
[nhkdjoo] (score 2, diepte 4) I’m not good at describing the pain (which is never helpful at the dr) but almost like a bruise someone is pushing on all the time. I think it’s just nerve damage and so it radiates? I have no idea but my foot just hurts all the time. EXCEPT. 

I was in Ireland for 10 days recently. My foot did not hurt the entire time and we walked a TON. Came back home (Arizona) and even after making dinner last night my foot hurt. So I think I just need to move to Ireland. 

I have no idea if it’s the change in altitude or something else. I don’t think it was the cold it was like 60 degrees and we have similar weather in the winter and that hasn’t helped.
[nhfh1h4] (score 2, diepte 2) that is interesting that it is worse when you are laying down, but better when you walk? Do you think the neurectomy was worth it? I'm scheduled for one at the end of the month
[nfj7uxy] (score 2, diepte 0) Thanks for sharing! Been dealing with one in each foot since 2014. Whats saved me most was retiring the high heels and any narrow shoes. :-(  if I wear them one night I take a million steps back. 
Keep us posted on the scarring and recovery after several weeks!
[nfzw6nk] (score 2, diepte 0) Are you icing any to help with the swelling? My podiatrist recommended icing the back of the knee for 20 minutes and off for 10, since the vessels are superficial and carry the cooler blood to the foot. He said icing and elevation are the best things to do for the pain.
[nfbwqsn] (score 1, diepte 2) OMG I was likeeeee girl really? 🤣 
  
Keep us updated!! I had 2 Kenalog shots, first one was magical, 2nd not so much 😔 now I have an MRI next week to find the exact location to either tackle with another shot or potentially surgery. Wanna postpone it as long as I can being a hairdresser, but I know I just gotta get that shit outta there at some point 🙏🏽
[nfbsz4v] (score 1, diepte 1 OP) Thank you for sharing this with me! I'm so sorry to hear about your allergic reaction and needing another surgery! Such a bummer! So glad to hear that everything is good now and you're 100% healed! I'm hoping I don't have any issues with sutures, I can't wait to get back to regular activity soon it's crazy how limiting the neuroma was. It got really bad when I was pregnant with my son, who I had in February, and I was hoping it would get better but it never did. It's hard right now to not be able to do much, but I know I'll be happy that I finally got this done.
[njvxf28] (score 1, diepte 2) They think I am allergic to the dissolvable vicryl sutures that were used in the surgery and as part of that, one of them did not dissolve. Because it didn't, it was basically a foreign body that my body did not like and thus, the area wouldn't heal.

I'm almost 3mo from the revision surgery and fully good as new. It healed in full within 10 days of the revision.
[noiza66] (score 1, diepte 3) oh wow. What an experience! I'm glad to hear you're good as new now! :)
[nfc7jn2] (score 1, diepte 1 OP) Thank you for sharing your progress! This is actually very promising, amazing that you have had no pain since your surgery! I do remember that pebble feeling when I had my other one done, but it went away after about a month! Sounds like such great progress for 8 days post op!
[nfc7rbt] (score 1, diepte 1 OP) Thank you! My doctor told me I should be good to start exercising at about 6-8 weeks post-op. I hope this holds true because I haven't been able to really exercise for almost 2 years now because of the foot pain and I am desperate to get back into a fitness routine!!
[nflw83v] (score 1, diepte 1) I'm a 74M, and 17 months post-op.  I had a regular neurectomy b/t the 3rd and 4th toe.  Everybody said 6-8 weeks and I'd be back to normal.  It was more like 12-13 weeks before it got as good as it was going to.  The pebble in shoe thing is gone, but ever since the op, now I have intermittent metatarsalgia and inflammation in the entire ball of that foot.  I have burning and a pressure sensation when sitting, and even when lying down sometimes, but it gets better when I get up and walk on it.  I've tried meta-pads, toe spacers, heat, massage, PT exercises, and ice, but nothing makes it go away.  Some days it's almost completely gone, and feels great, then the next it's back and bothersome.  I wear cloud sliders around the house, never go barefoot, and tennis shoes (wide toe box) outside.  The inflammation is chronic and I just don't know how to get rid of it.  Does this sound like what you are experiencing?  What I don't understand is why it's so much worse when I'm not on my foot, but gets better when I get up and walk on it....very frustrating.
[nfm5a4p] (score 1, diepte 3) Yeah, it's not good, I agree.  I just don't understand why it burns mostly when I'm sitting, and not even on the foot.  That makes no sense to me.  Is that it is for you too?
[nhko9ne] (score 1, diepte 3) Yes, I do think it was worth it.....that pebble in the shoe thing was terrible.  Now, it's intermittent inflammation across the entire width of the ball of my foot....almost all of which is when I'm sitting at my desk.  Some days it's almost not there at all, other days you can really feel it.  If I get up and walk on it, then it's fine.  I don't understand why that would be.
[of2cac2] (score 1, diepte 4) what about your toes? do they get red when sitting down?
[nfut63n] (score 1, diepte 1) I'm a year post surgery, and the foot is worse than pre-surgery.  I've had more corticosteroid injections into the area to deal with inflammation, etc, but no luck.  I do wish I'd found this forum before I booked the surgery, there were a lot of really helpful tips on here that my podiatrists never talked about.
[ng023zi] (score 1, diepte 1 OP) No I wasn't advised to ice! But this makes so much sense though. I've been elevating a lot but maybe I should ice!
[ng02uka] (score 1, diepte 2) I hope it helps!
[o46qtzq] (score 1, diepte 0) Thanks for sharing. Any update? I also developed a neuroma in pregnancy and just had it removed 4 days ago. I’m having some stabbing pain when I walk on it after sitting for a while. That is concerning me

