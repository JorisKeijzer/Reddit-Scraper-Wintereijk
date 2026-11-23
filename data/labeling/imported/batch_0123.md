# Label-batch batch_0123

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
Schrijf het resultaat naar `batch_0123.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 16o6cvj, 52swdj, 1ac1wzk).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 16o6cvj ===
SUBREDDIT: r/gout
DATUM: 2023-09-21  SCORE: 10  REACTIES: 71
TITEL: Why do I have gout? 53M on trt. Play Pickleball 3x week. No alcohol. My left foot pain is a 8/10 in am.
POST (source_id=post):
Could I be pre diabetic? Does Baking Soda in water work to relieve it?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k1iudwr] (score 39, diepte 0) Genetics. I’m like you and I have it at age 30
[k1ivfup] (score 15, diepte 1) It takes a long time for some people (myself included) to get to this point. Gout is such a strange disease that you find yourself asking "what did I do to deserve this??" Explaining to people that your foot feels like it got ran over by a car, when they saw you yesterday, and you were fine. Then in a week or 2 you ask them if they want to go for a jog, and they say "I thought your foot was all mangled?". I did the hydration, cut alcohol, cut red meat, and was fine for 6-7 years. Then a flare every 3-4 weeks for 6 months straight. Back on the allopurinol, and just now starting to get my life back...
[k1ivnev] (score 10, diepte 0) 48 and just started this year. Trying to get used to the allopurinol now. My pain has been so bad my wife stayed up worried.
[k1jibiz] (score 9, diepte 0) WHAT THE FUCK IS PICKLEBALL
[k1jfori] (score 8, diepte 0) I think TRT can raise uric acid levels causing gout. Worth looking into but if you are on TRT you might want to also take allo
[k1iyl3k] (score 6, diepte 0) Why? Because your uric acid is too high and your body can't process it properly. Why is that? Most likely genetics.
[k1j746m] (score 5, diepte 0) Got it around 32. 40 now and after years of pain and agony I finally gave into allopurinol and have not gotten a attack for 2 years now.

Easy explanation is that some people’s body produce more uric acid.
[k1kae94] (score 4, diepte 1) Same, but age 29
Had gout since age 21.
[k1k62vf] (score 4, diepte 1) It’s in between tennis and ping pong. It’s like a wiffleball version of tennis really. Plastic ball, plastic paddle on a smaller court than tennis. Real Popular in retirement communities but I’m a 30 year old and like playing it. You can work up a good sweat if you get good and play someone else whose good.
[k1ouvqa] (score 3, diepte 2) Raise uric acid levels can cause heart and kidney issues. Some really serious stuff, so the benefits of allo outweigh the risks, with the added bonus of being unable to walk for weeks, but worth getting health checks and bloods done a couple of times a year too just in case
[k1jzzbh] (score 3, diepte 1) [Fastest growing sport in America.  Don't get left behind.](https://www.tiktok.com/@maddymomoferin/video/7194969250199670062?lang=en)
[k1kn0tz] (score 3, diepte 3) I’ve found that once I start moving, it slowly gets marginally better while I’m active. Once I rest, even for a few moments it all goes bad.
[k1jtt2o] (score 3, diepte 0) Officially diagnosed this year aged 36, my grandma diagnosed last year and she’s in her 80s!

I’ve had foot pains for 5+ years, suspected gout for a long time but kept getting brushed off sadly.

Food is a contributor in ways towards flares but ultimately genetics is why our body processes, or  well, doesn’t process uric acid in the way it should! 

It’s such a painful condition, but manageable fortunately through medicines for long term and also medicines for flares.

I’ve tried pretty much all the remedies before getting officially diagnosed - cherries, turmeric, various vitamins, yogurts, baking soda, vinegar with “mother” etc. Find a gout blog, I’ve probably done it. 

Helps with general health but didn’t do *anything* for my gout/ongoing pain. I feel yogurts do help with digestion and reducing risks, keeping hydrated definitely helps with overall health 

Two months of Allo and three on doses of colchicine and I’m feeling better. 

Long road ahead but, trust me, it’s worth getting seen to asap and on a treatment plan! Ideally medication but appreciate its not for everyone and it may end up being you trying different things to see what sticks

By all means try various remedies - but at the very least once out of a flare, get blood work done to see where you’re at as a benchmark. 

Good luck! Hope it settles soon!
[k1lhx1v] (score 3, diepte 0) Protein drinks bars will elevate a trigger, even oatmeal is a top contributor.
[k1klybo] (score 2, diepte 2 OP) Any diabetes? Do you workout? What triggered it?
[k1kohq7] (score 2, diepte 3) I am overweight now, but no diabetes and I have been losing weight. I workout both cardio and resistance training. When I first had gout, I was literally the perfect weight (BMI). I worked out, not much alcohol. No one believed it was gout until I was 25 and I ordered my own uric acid test from a lab (blood test) and then I sent the result to my doctor. I had a uric acid level of 8.6. Until then, people thought I had an infected toe. I was prescribed anti-inflammatory medication and sometimes anti-biotics. I have researched my genes after a test and I have a predisposition to gout. My dad has struggled with kidney stones throughout his life, but he is healthy (as far as I know) other than that and still leads hikes on mountains at age 75. Mom never had issues. My kidney function tests have all been normal. No idea what triggered it. When I first had it, I didn't eat much meat, but I did drink diet soda quite a bit. I am not on alopurinol 300mg and have been for four years. No flare up since I started.
[k1n83te] (score 2, diepte 4) I'm glad to hear I'm not the only one. I think my symptoms started when I was 24 and progressively got worse over the years. I didn't know I had gout until I went to the er when i was 28 to get fluid out of my knee. Been fighting it since. Now I've been told it's genetics and also from trauma etc? Or just depends on your diet ?
[k1md1gy] (score 2, diepte 2) I have to agree with you, i am on allopurinol as well and get flare-ups a few times a year, always seems to be related to dehydration or very light injuries to my feet /  toes
[k1jkyns] (score 2, diepte 2) So, tennis?
[k1k8gzv] (score 2, diepte 2 OP) Oddly, all the foot pain goes away when I play. Why? Is physical therapy or cardio good for gout symptoms?
[k1ju2ni] (score 2, diepte 1 OP) I have a good Dr. I pay directly. No insurance. They are very busy and usually don't look beyond pharma. Dr's want to cover there ass. Limited knowledge. I only trust certain ones. 

I had a surgeon tell me I needed my gal bladder removed because of some sludge. I said how about no.  He had no interest in finding the cause. I discovered fasting, whole food diet and nurse practitioner that prescribed peptides and TRT. That was 3 years ago. I'm in great shape. Reddit is awesome resource.
[k1k7j5d] (score 2, diepte 1 OP) Get bloodwork today. Glucose Tolerance test and uric acid. 

I figured Cherry juice was a not going to work. Baking soda in water seemed to help.
[k1k06kn] (score 2, diepte 0) It's worst when you get out of bed?  Does the pain extend from the heel forward?

If so, it might be plantar fasciitis.

(I've had both gout and p.f., and for months confused the latter with the former, thinking it was my most extended gout attach ever)
[k1k6ak1] (score 2, diepte 1 OP) In am, when I stand and walk. It hurts/burns from ankle forward to my big toe knuckle. Then hurts after a long sit or drive.
[k1kicav] (score 2, diepte 2) Could be gout.  Could be some kind overuse injury from pickle ball.  3x a week is a beating on the joints.
[k1k6d94] (score 2, diepte 0) Brother tomatoes sets mine off..  as soon as dropped them from my diet, no gout..  but if I dabble in to much tomatoe sauce it creeps back.
[k1k86up] (score 2, diepte 0) I feel the same way, got my first flare up at 42 but I haven't eaten red meat since I was 14. I don't drink more than one or 2 drinks a week, never beer and I'm a woman still with lots of estrogen still. At least like a person to get gout is a woman with estrogen still kicking around , never mind one that doesn't drink or eat meat. Estrogen flushes uric acid out when you pee. I drink tons of water, don't like carbonated pops. If it was genetic shouldn't there be people in my family with it? My parents don't have it, I've never heard it mentioned until my docter diagnosed me. Make it make sense.
[k1kqwdh] (score 2, diepte 0) Because your uric acid levels are high. Go see your doctor and put a plan together instead of living in pain.
[k1krgs0] (score 2, diepte 0) Genetics. I'm athletic, eat well, 6'2" and 160lbs but still have gout.
[k1nntd8] (score 2, diepte 1 OP) Agree. HFCS is garbage sweetener designed to shorten life and cause fatty liver desease. HFCS is Banned in Europe! Why? Universal Healthcare. It cost the tax payers money when people get sick. I the USA is big money if you get sick. Everything tasted better when I went to London. America not the greatest country, despite what they say.
[k1lmu5n] (score 2, diepte 1 OP) 169lbs. Got acid tested today.
[k1l2zr9] (score 2, diepte 0) They have found correlation between high uric acid and diabetes, I don’t believe they have a sound reasoning behind it. My personal theory is that people who eat a lot of junk foods tend to be obese and also consume high purine foods like processed red meats, so they end up becoming diabetic and also have high levels of Uric acid. If you are not overweight, or if you are overweight but not obese and have a moderate body fat percentage and good amount of muscle, and you have a decent diet, eat some fruits and veggies now and then, get some decent amount physical activity, not an alcoholic, then it is more genetic, and I wouldn’t be too worried about being more prone to diabetes. But you should go get checked out. Pre diabetes is completely reversible. Trt definitely increases uric acid by the way, maybe you’d benefit from starting allo.
[k1lol92] (score 2, diepte 2) They say that it doesn't really change anything, my experience says otherwise. I was not on allo, I had a 3 month period, a couple of years after I discovered that I have gout, that I was drinking like a fish. I made sure that I drank like 4 liters of water every day, about a third of that was alkaline water, never had a flare up. Had one or two instances where there was some inflammation in my foot, but that's it. I'm going to start allo now, just got my prescription, cannot wait for my body to get acclimated so I can stop getting random inflammation while lifting and drink socially and eat red meat in moderate quantities without being worried.
[k1lp1dj] (score 2, diepte 2) I understand that you don't want to stop trt, there seems to be evidence that trt will increase uric acid. Visit a rheumatologist (get referral from primary care provider). He/she/they will monitor you for 6 months or so, let them know that you would not at all mind going on allo, but you don't want to stop trt. They will eventually prescribe you. Have a rocky 6 weeks to 6 months and then live in peace.
[k20uu3n] (score 2, diepte 0) Your pickle ball could be causing very minor injury that causes a gout flare. Gout loves to show up where there are small unnoticeable other wise joint injury. Happens to me all the time. Used to be 210 booze drinking fiend, gout flare every other day. Lost 50 lbs and cycle every day. Only get a flare when I do long routes >60 miles that are causing flares in my foot or knee, or hip.
[k1kgw3d] (score 1, diepte 1) I agree you start with genetics, but as a person with gout + on Allopurinol for a couple years now, some factors consistently on my mind are:

* Injury
* Dehydration
* Age

My first go with gout, when I had no ideas or preconceived idea of what a person with gout looked like, happened because I kicked ice out of the wheel well of my wife's car. Essentially I stubbed my toe, and woke up thinking - HOLY FUCK - *I must have shattered my foot last night, went into shock, and the pain is just now hitting me*! My last flare up, also because I stubbed my toe. Even on Allopurinol, an injury can lead to a flare up.

With OP, obviously you want to just get to a doctor and figure things out, but (a) 40-50 is the most common diagnosis timeline, though these days it feels earlier. And I mean, people get hurt and dehydrated playing pickleball too, so keep an eye on that activity.
[k1k7st3] (score 1, diepte 1 OP) Are there side effects to Allo?
[k1ki1dz] (score 1, diepte 2) Yep.  Some rare, potentially fatal ones.
[k1j97av] (score 1, diepte 0) NSAIDs are your best bet. Aleve/naproxen seems to work better. Head to the doctor and have a prescription of colchicine on hand in case the attack hits again. These drugs are most effective if taken at the slightest hint of pain. Once youre at an 8/10, you just need to ride the attack out. Corticosteroids can be very helpful in getting you back down to a 3/10 but doctors generally don’t prescribe them unless you have a history.
[k1jgh9x] (score 1, diepte 0) Either genetics or lifestyle. I know i never had an issue with it til i overindulged in too much fast food/soft drink/too much meat diet.
[k1jjxlr] (score 1, diepte 1) Like giant ping pong
[k1jlcmf] (score 1, diepte 3) But with ping ping style paddles
[k1jsukf] (score 1, diepte 3 OP) Fastest growing sport in US right now. I play indoors at county rec centers. Play 2v2. Very easy to pickup. It's very social and easy to learn. Tennis? Not so much.
[lelvvqj] (score 1, diepte 2) Among the LGBT groups.
[k1kasks] (score 1, diepte 2) WIFFLEBALL?!
[k1jq4fq] (score 1, diepte 0) Beef shellfish pork preserved meat even certain vegetables can lead to gout and kidney stones.
[k1js0xn] (score 1, diepte 1 OP) A few days before I drank saki, ate steak and sushi. My iron was low so was eating more steak.

I drank water with baking soda before bed last night. I like the taste. Woke up better. Just dull pain. 3/10.
[k1klxv1] (score 1, diepte 2) Yeah steak certain seafood and saki all can blow up gout.
[k281mmg] (score 1, diepte 1 OP) My Uric acid was 5.2.
[k1kqg2u] (score 1, diepte 3) Could even be a gout attack set off by the physical insult of jumping around playing pickleball.  I've had an attack set off by bloody backyard badminton :\\

For those new to this: gut attacks are basically inflammation spirals, and if physical insult causes mild inflammation in a joint which has irate deposits, you can get an attack.  So the thinking  - and many people's experience - goes.
[k1kg2st] (score 1, diepte 0) Aleve. Allopurinol from the doc and lots of PH water.  Back in no time .  I suffered for weeks.  That combo works and stay away from any high fructose anything Chinese food my favorite unfortunately but that has worked
[k1lmz90] (score 1, diepte 1 OP) Wow. How old?
[k1qpq8x] (score 1, diepte 2) I'm 40 now. first flare up was around 30 years old. had another a few years later, then another at age 36 or so and finally went to the doctor and got on allopurinol. I run 5-6 days a week, lift weights, eat healthy (lots of vegetables, very little red meat or processed food), try to drink loads of water.. but still I'm fine being on allo the rest of my life as long as it means no more debilitating flareups.
[k1kspor] (score 1, diepte 0) Maybe diet? There’s a lot of crap they put in the food these days. I find that highly processed food is all bad for gout. Junk food, added sugars, preservatives, fillers, the list goes on. The high fructose corn syrup is what gets me flaring. That crap is in everything, especially sodas, juices, ice cream, even Ritz crackers. 

I can handle an occasional burger or beer just fine but I stay the hell away from corn syrup.
[k1nptap] (score 1, diepte 2) Well said
[k1kv5sm] (score 1, diepte 0) What is your height and weight? What is your diet like? These are likely keys to your ailment
[k1l099p] (score 1, diepte 0) What's your weight? Uric acid level?
[k1lnrx9] (score 1, diepte 2) Is 169lbs for you overweight already?

 I hope all is well for you for the blood test. maybe it's just a regular foot pain
[k1npjg5] (score 1, diepte 3 OP) Thanks. Baking soda in warm water before bed helping. I fasted (ate no food from 6pm yesterday to 130pm today) 

I'm 5'6. Stocky Irish build. Flat belly. Not fat imo. I never drink soda or beer.

I love dark chocolate, pickles, Chipotle chicken bowls. Avocados. I eat eggs every day. Only 1 cup of coffee with cream. I haven't eaten at McDonald's in years. 

Pain is 1/10. Going to work out tomorrow. Does foot massage offer an benefits? Pedicure maybe?
[k1ns4wu] (score 1, diepte 4) if that's really a gout, foot massage is a big no, and also do not put weight on the foot.

but if it's not a gout, go ahead and do workout, foot massages, pedicures etc. 

that's all i can say right now... is the pain on the big toe? or just foot in general

if it's just the foot in general, i dont think it's gout based on your self description. but best of luck
[k1l0dtq] (score 1, diepte 0) It’s your diet
[k1lnl6s] (score 1, diepte 1 OP) What are thoughts on distilled water, baking soda and alkaline water? Allo side effects? Trt is so benefitial, I can't stop it.
[k1ljnyx] (score 1, diepte 1 OP) Really? I eat cliff bars everyday 09 I have . What CAN I eat? Chicken and rice?
[k1vfrki] (score 1, diepte 2) Chicken in moderation should be fine, but unfortunately the thing about gout is that it's a indicator telling us that our bodies are not breaking down proteins correctly. And it hits us all differently.
[k1o06xj] (score 1, diepte 0) Don't do baking soda that could make you worse. Baking soda is a salt, and taking sodium in high amounts will cause a massive increase in your blood pressure. I took baking soda in high quantities and I got abdominal bleeding. Stick with allo or a big change in diet. Stay away from all kinds of sugars especially high fructose corn syrup, that will really lead to gout.
[k1o7fax] (score 1, diepte 0) Dehydrated?
[k1o9vik] (score 1, diepte 0) I got it with overconsuming sugar.. cookies, cakes, sweet snacks etc..
[k1oe8ac] (score 1, diepte 0) My podiatrist says it’s not what you eat, it’s what you make. By that she means what you eat/drink isn’t as important as how your body creates Uric acid.
[k20vn6d] (score 1, diepte 1 OP) All the pain goes away when I play. I think it's because of increased blood flow and circulation in the area . Do you take anything for it? I'm going to try deca NPP this week and see if it helps.
[k20wuy3] (score 1, diepte 2) I’ll preface anything I say with everyone is different with this disease. Allopurinol had little to no effect for me. I just mange it through healthier lifestyle and moderate excecise. Ibuprofen is the most effective for me but do my best not to take meds if I can help it. My pain also goes away when I excercise. Makes sense too. Much more circulation and movement in the joint to help clear the shit out. I would just recommend moderate excercise that is not high impact to the joints (swimming for example) or just try to go a little lower intensity on pickle ball
[k281hbp] (score 1, diepte 0 OP) Part 2.  My Uric Acid came back at 5.2.  In range(- 6.0).  I was fasting when I took the test.  My symptoms continue every morning.  I can barely walk on my left foot in am.  I played casual pickleball today and it got better slowly.  

I drank lime water with hymilan salt in afternoon and that seem to help me flush out and provide relief.  Pain gets worse if I sit long time.  Seeing Dr tomorrow.
[k1jlxrx] (score -4, diepte 0) Has physical ailment 
Asks Reddit instead of Doctor. 
Smh the world we live in.

=== THREAD 52swdj ===
SUBREDDIT: r/Teachers
DATUM: 2016-09-14  SCORE: 15  REACTIES: 69
TITEL: Male teachers, Shoes??
POST (source_id=post):
So I have been teaching for about two years and I still have yet to find a pair of shoes that both look good and don't make my feet feel awful by 4th period. I currently rock some leather oxfords from Bass, but at the end of every day my feet just feel awful and have sweat a lot more than I am ever used to. 

I'd love some boat shoes or something similar, but so many seem a little too unprofessional or colorful.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d7n13je] (score 13, diepte 0) Sneakers!  I'm sorry but my fitbit says I walk about 3.5 miles per day in class.  Damn some penny loafers or whatever else.  Sneakers my man.  Sneakers.
[d7n2g3b] (score 11, diepte 2) Ya, honestly, I work at a school that is on the tough side.  We lose 14-20 teachers per year, they aren't about to hassle me on some sneakers.
[d7n9w5c] (score 10, diepte 3) But you aren't teaching Physical Education to them either. If you are teaching "physical education" to the students, you are teaching them how to teach the subject.  For example, if I took a class in "English Education," then I would be learning about how to be an English teacher.  But you also can't say you are teaching them "physical" because that makes no sense...you can't teach an adjective.  It works in the English example because in the phrase "English Education" the word "English" takes the form of a noun but serves the function of an adjective (modifier).  Remove "education" and you are left with a noun, English...which is a subject you can teach students.  

However, when you say "physical education," the word "physical" takes the form of an adjective and functions as one as well.  Remove "education" and you're left saying, "I teach physical to the students."  The class might be able to be called Physical Education, but a PE teacher is not teaching "Physical Education" just like you argue he or she is not teaching "gym."
[d7n3t0w] (score 7, diepte 0) I got some dr scholls inserts from walmart after standing in the machine. My feet, back, and knees are much better. I swear by Rockport shoes. They are comfortable, look decent, and last forever.
[d7n45ga] (score 7, diepte 1) you Gellin' ?
[d7n19ga] (score 6, diepte 1) They make them in solid dark colors too, so you can pass them off as more professional. Only the kinders are short enough to really look all the time anyway.
[d7n26y8] (score 4, diepte 0) Clarks Oxford Loafer
[d7n2dvj] (score 4, diepte 0) Dr Scholls, Merrelll, Timberland, Nunn Bush, Skechers
[d7n44ov] (score 4, diepte 0) sneakers.  I have a nice pair of black on black New Balance
[d7n6il5] (score 4, diepte 0) I'm elementary, so I'm on my feet constantly walking around all day. Sneakers. I wear Nike Free Runs. The kids love the colors of the shoes. Admin doesn't mind. If it's ever something really important that day, I'll bring some shoes that look more professional and switch out when I need to.
[d7ndge1] (score 3, diepte 2) I rock a pair of custom black leather [Chucks](http://store.nike.com/us/en_us/pd/converse-chuck-taylor-all-star-leather-high-top-unisex-shoe/pid-11214005/pgid-11593152?cp=usns_kw_converse_null_pla%21g%21t%21nobr%21&amp;k_clickid=45161660-ef89-468d-8cbb-7a31f038ad20).  Super comfy, don't stand out like colorful sneakers so they kinda hide the fact they're not dress shoes, plus I get some street cred from my high schoolers when they do notice them.
[d7nriek] (score 3, diepte 0) While I'm still in preservice, I was once Mormon and did the whole mission thing. I had a pair of Doc Martin's that lasted me walking everywhere in them for two years and I kept them another two years after (I got rid of them because I'd stopped polishing them properly and they looked bad as a result). They are a bit heavy, but with a good insert insole, they'll last forever if you need something a bit dressier looking.
[d7r3fsc] (score 2, diepte 2) My nice shoes had the heel separate two weeks ago and it took me that long to fix them.  I have solid black sneakers.  A few students noticed, not a single teacher of admin noticed.  

What i used to do is wear work boots.  They are solid, cheap and black leather so as long as your pants don't pull up they look very professional.  I'm probably switching back to work boots if the heels separate on me again.
[d7n5ht9] (score 2, diepte 1) I'll second Clarks. I switched from Skechers after they discontinued the best teacher's shoes ever (lace up Brash) to Johnston and Murphy Shuler Bicycle Toe, but once those got too worn/ugly I tried a pair of Clarks. Super light, nice cushiony insole. 

These are my current go-to:

http://www.dsw.com/shoe/clarks+touareg+vibe+oxford?prodId=348351

If you want something less dressy and more casual, the Clarks Sherwin Limit is great as well.
[d7n2azj] (score 2, diepte 0) I think this comes up once a year. Check out- https://m.reddit.com/r/Teachers/comments/4uk00n/recommend_a_shoe_for_male_teachers/

I went with these- https://www.amazon.com/KEEN-Mens-Tumalo-Mid-Shoe/dp/B00SYYXR2M?th=1&psc=1

In the brown they're professional looking enough, comfortable and offer enough support to be on my feet all day
[d7n2jqp] (score 2, diepte 1 OP) Wow those look really cool. I am all about the brown ones too.
[d7n6fny] (score 2, diepte 0) Merrell shoes for me.
[d7n6kzh] (score 2, diepte 0) Clark's.
[d7n8grr] (score 2, diepte 0) Sanuks!  Very comfortable.  They can be kind of dorky looking, but I am known for wearing bad Hawaiian shirts every day... so I really don't care how I look.
[d7niun8] (score 2, diepte 1) I used to have a pair of the second one you linked, but I felt like they wore out too fast to be worth the money. What has been your experience?
[d7namvy] (score 2, diepte 0) Crocs makes some decent dress shoes... They aren't super fancy but they go well enough with slacks and a tie... I won't wear anything else now.
[d7nbrac] (score 2, diepte 0) Cowboy boots. Once they are broken in they will last for hours.
[d7npn1r] (score 2, diepte 1) I just recommended the same!
[d7noggs] (score 2, diepte 0) I'm surprised no one's mentioned this yet.

OP, look for a good pair of restaurant shoes; the ones waiters use with the nonslip soles. They're comfortable as they're made for people who are on their feet all goddamn day, and they look professional enough no one will bat an eye.
[d7oyq2w] (score 2, diepte 0) Stacy Adams. Some have great inner-cushioning, too.
[d7n1cre] (score 1, diepte 1 OP) I feel like teachers cannot get away with sneakers in my school unless they are actually a ~~gym~~ physical education teacher.
[d7ndos7] (score 1, diepte 4) English is your subject though. My particular subject is p.e. And therefore that is what I teach, not my location. We do not say that the English teacher teaches "classroom" because they are located within a classroom.
[d7n84bm] (score 1, diepte 3 OP) That is actually really cool, and I would like to hear more about your school.
[d7n88f9] (score 1, diepte 2 OP) That is a great looking shoe right there.
[d7nce83] (score 1, diepte 2) Like a felon
[d7nd6rp] (score 1, diepte 2) I'm so gellin' I'm like Magellan
[d7n499u] (score 1, diepte 0) I had this same problem as you until this year. I was wearing sneakers but really wanted to look a bit more professional, but also didn't want my legs to give out by the end of the day. A coworker let me in on a secret - Doc Martens. They're so freaking comfortable, I don't even look back to my sneakers anymore. Definitely worth checking out.
[d7n4m6u] (score 1, diepte 0) 4 years ago, I got a pair of Ecco (not mark ecko the grafitti artist) black dress shoes for $100.  I wore them got 3 years teaching.  I've moved to a new pair since.  They're affordable, look a bit dressier than sneakers, and are fantastic shoes.  Might be worth checking out.
[d7ncz7k] (score 1, diepte 1) This is what I was looking for someone to have said! They look great and are incredibly comfortable---and they last forever!
[d7n5l4p] (score 1, diepte 0) Keens. I had problems with just about every other shoe before them. Ecco. Cole Hahn. Bjorn. Bass. Doc Marten. Nike. New Balance. You name it. I can be on my feet all day with my Keens and them dogs don't bark.

Style: [Austin] (http://www.lhstigerhoops.org/mens-casual-dress-shoes-keen-mens-austin-casual-shoes-chocolate-brown-1007722-p-6404.html)
[d7n62nx] (score 1, diepte 0) I wear brown or black sketchers almost every day.  Not as comfortable as my every day athletic shoes but much better than anything dressier.
[d7n6grf] (score 1, diepte 0) If you can't wear sneakers look into Dansko. I made a similar inquiry here 3 years ago and people suggested the brand. I didnt want to spend the money but after tearing through pair after pair of uncomfortable  $40-75 shoes I decided to just try Dansko.  I have the Men's Wyatt loafer. I have not worn them every day but I've owned them for 2ish years now and they're going strong. I never find myself uncomfortable despite their firm foot bed. I don't know that I'd choose the same style next time, but only because these were less dressy than I hoped making the shoe less versatile.
[d7n6i0m] (score 1, diepte 0) Do not listen to people on this thread.  There is one right answer and that IS DANSKOS!!! You can't just break into em 8 hours a day.  You have to wear em like an hour or two at a time until your feet get used to them but once you get through that you don't even realize you have shoes.
[d7n72o3] (score 1, diepte 0) I have a very thin foot, but my Clairborne dress shoes have always been comfortable. Got them for like $100.
[d7n7zcn] (score 1, diepte 0) Found some Eccos on clearance. After a longer than expected break in, they're amazing and have lasted 2+ years so far
[d7n8gq8] (score 1, diepte 0) Cole Haan Lunargrands if you're in professional attire. Pricey, but they are on sale often. They have the same soles in some Nike running shoes. Pretty comfortable and nice. 

Adidas Ultra Boost if you're in casual clothes. These are pricey as well, but are the epitome of comfortable. They look great with jeans, shorts, cargos, etc.
[d7n8jc0] (score 1, diepte 0) Bostonian Flexlite

Bought them to wear at my wedding, loved them, decided to make them my work shoes as well.  Each pair lasts exactly one year.  I'm on my feet all day... the only time I have aching feet is when I stup idly decide to wear more casual shoes instead
[d7n9w6w] (score 1, diepte 0) New Balance makes some great teacher shoes. Made in USA too.
[d7ombhh] (score 1, diepte 2) I've gone through 3 pairs in 2 years or so. Not bad I feel for a $50 comfortable shoe
[d7narvo] (score 1, diepte 1) http://www.crocs.com/p/203391.html?cgid=men-footwear&cid=01R#start=96

http://www.crocs.com/p/mens-shaw-leather-loafer/202052.html?cgid=men-footwear&cid=23K#start=104

http://www.crocs.com/p/crocs-mens-walu-chukka-boot/15364.html?cgid=men-footwear&cid=26L#&origin=category&srule=CatPosition-SearchPlacement-Revenue7day-PRRating-PRReviews&start=5&sz=36&prefn1=variationSize&prefv1=&prefn2=refinementColor&prefv2=&prefn3=fitGuideFit&prefv3=&prefn4=lifestyle&prefv4=Loafers
[d7narie] (score 1, diepte 0) hmm, somebody doesn't like talking about shoes.  Went through and down-voted every post.
[d7nbkyh] (score 1, diepte 0) Aryats
[d7nc4r4] (score 1, diepte 0) Who is downvoting everything?
[d7nfrqx] (score 1, diepte 0) I highly recommend any of the ZeroGrand by Cole Hann. They are a bit pricey at $270,  but I am a high school track & field coach, so I look at shoes as an investment. Plus they come in a all types of colors and materials. If you are savvy enough you can find a good deal at an outlet or wait for a sale. They were in business with Nike for quite a long time and collaborated to come up with the a dress shoe that felt like an athletic shoe and so the ZeroGrand line was born. I own a pair and absolutely love them. 

https://m.colehaan.com/products/C22395?start=8&cgid=mens_shoes
[d7ngkaj] (score 1, diepte 0) I wear my Chucks. I love them.
[d7ngtki] (score 1, diepte 0) Sneakers in non-flashy colors or invest in insoles.
[d7nmb2a] (score 1, diepte 0) RM Williams Boots
[d7nolwf] (score 1, diepte 0) Secret is in the socks - not the shoes. Wear two pairs.

I have done this for years now (including in my past life as a waiter/bar tender) and I don't have problems. I teach drama which has me on my feet most of the class time. I wear a range of leather formal dress shoes- Florsheim, Trent Nathan, Aquila (I think they're mostly Australian brands) and once they're broken in - I'm sweet.
[d7olqs8] (score 1, diepte 1) Oh man, my feet would smell like ass if I had 2 pairs of socks.
[d7ovceb] (score 1, diepte 2) They're not thick pairs - two pairs of thin cotton socks. Easy breathey
[d7npmgl] (score 1, diepte 0) So, depends on how much you wanna spend. I'm currently student teaching, but my main goal was to get some shoes that were dressy, yet similar to sneakers. They are Cole Haan's... Called ZeroGrand. These shoes are thin, but have an appearance of a dress shoe, and a sneaker like bottom. They are pricey (over 200 online, about 150 if you live near an outlet where they have a store), but so far I have loved them and they have done wonders for me.

[Here's a link](http://www.colehaan.com/mens-zerogrand)
[d7nqckk] (score 1, diepte 0) Reebok walkers or Rockport walkers.  My feet still sweat a little, but they are well cushioned. They come in different outer coverings and include some black or brown that look professional enough.  Sneakers that don't look like sneakers.
[d7nwkw0] (score 1, diepte 0) I like Wallabees. They are super comfortable for being on your feet.
[d7nyhg3] (score 1, diepte 0) I have a pair of Keen shoes that I absolutely love. Most of their shoes are geared towards the outdoors, but they offer quite a few that work well in a business casual environment. They were a little pricey ($130), but they've held together so well that I'd buy another pair in a heartbeat. I've been wearing them to work almost every day for over 3 years, and they're still very comfortable. They still look good and aren't falling apart at all.
[d7o7qi3] (score 1, diepte 0) Solid black Memory Foam Sketchers "work shoe" line. They look good, are pretty solid, have some of the best arch support (curse my high arches) and the memory foam doesn't squish down over time so it always feels firmly cushioned instead of wearing the foam down into a mold of your feet.
They put me back about $70 but after a few long days I feel like it's a worth while investment.
[d7oheos] (score 1, diepte 0) Check out r/sneakers.

I'd suggest Ultra Boosts, or any adidas shoe with Boost tech.

Your students will think you are fly.
[d7olvov] (score 1, diepte 0) I'm experimenting with these right now. So far so good.

http://www.softstarshoes.com/adult-hawthorne-chukka-2.html

They are more like slippers than shoes, super light. I have weird snapped feet that never fit dress shoes well. These don't have molded or hard leather so they sort of just sit on your foot rather than squeeze it.
[d7n27t3] (score 0, diepte 0) Highly recommmended!
[d7n4tjl] (score 0, diepte 0) These: http://icebug.com/int/icebug-insoles/.  Worth every penny.  Just be sure to read through the site carefully.  There are a lot of options.

Also, used Allen Edmonds shoes on Ebay.  I rotate through four pair every week to keep 'em from getting too beat up.  When they do, I send 'em back to Allen Edmonds in the summer for a rebuild.  Costs $50 to $120 US to get them redone, but they come back as good as new.  Had three out of the four pair for 12-15 years and they have yet to let me down.  

The fourth of four pair was my dad's.  He bought them in (as best he can remember) 1975.  He gave them to me when he retired.  We've each had them rebuilt once and they still look/feel great.
[d7n5ek4] (score 0, diepte 0) Cole Haan Lunargrands.

I think now they call them Original Grands.  They aren't cheap, but they are comfy and they last forever.  I have a pair now that I've had for 4-5 yrs, still fine.  Their soles are similar to what you would find in a sneaker.

They have some style but aren't over the top.  You can find them on sale on their site and if you sign up for their newsletter you get a 15% off code.

I had just recently bought some Samuel Hubbard shoes, their "un sneaker" but I thought they were uncomfortable so I'm returning them.  They cost more than the Cole Haans.

Here's what I just bought.  Arrived in the mail today actually:

http://www.colehaan.com/originalgrand-moc-chukka-deep-espresso-suede-cobblestone/889203862284.html
[d7n8fzy] (score 0, diepte 0) I tend to wear hiking shoes, but they don't work if I am a bit dressier.  On those days I go with Doc Martins
[d7n8s8j] (score 0, diepte 1) Check out my previous post above for the shoes I just bought and how to get 15% off.
[d7na9pi] (score 0, diepte 0) Sketchers makes some decent looking shoes like [this](http://static3.shop.indiatimes.com/images/products/additional/original/B1018388_View_1/fashion/casuals/skechers-black-men-shoes-61893.jpg) or [this](http://wm-motorsports.com/wp-content/uploads/2015/01/sketcher-shoes-for-men-2.jpg) that fit like sneakers. I wear these most days and nobody seems bothered.
[d7n24jt] (score -7, diepte 2) Physical Education teacher. A gym is a place, you can't teach gym to a student.

=== THREAD 1ac1wzk ===
SUBREDDIT: r/hiking
DATUM: 2024-01-27  SCORE: 26  REACTIES: 69
TITEL: Hiker with Plantar fasciitis
POST (source_id=post):
G’day fellow hikers. Enjoy be had my Australian summer of hiking cut short by plantar fasciitis, which I’ve never experienced before. 
Any sufferers out there? Any tips about how to get over this quickly so I can get back to hiking? Any tips on shoes (about to buy a new pair) or innersoles?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kjrjvix] (score 36, diepte 0) Before you take a step in the morning,  stretch each calf for 3 minutes.  3 sets of 1 minute each.  Roll with a tennis ball regularly.  Fill up a tennis ball canister with ice and roll your feet on it av few times a day.  It may take a few months,  but it will work. 

Also, stretch calves regularly.
[kjrl2c5] (score 34, diepte 0) Shoe inserts with arch support can be incredibly helpful. It solved all of my problems, but I don't know enough about PF to say that it would work for you. I've been pain free for over a year.
[kjro1vh] (score 17, diepte 2) Had plantar fasciitis 20 years ago and the tennis ball stretch/exercises helped me. A PT friend also recommended this. [https://medi-dyne.com/products/prostretch-original-single](https://medi-dyne.com/products/prostretch-original-single). Used it 3x a day, then every 12 hours... etc. 

We still have it and do stretches before hiking, after driving long distances, etc.
[kjrlios] (score 17, diepte 0) I recovered from plantar faciitis.  

First, you need orthotic inserts for all of the shoes you are wearing.  Good ones.  https://www.orthofeet.com/collections/insoles-for-plantar-fasciitis


  Next, you need a plantar faciitis boot to wear at night in bed that keeps your calf and foot at a 90 angle.  WEAR IT EVERY NIGHT!  This keeps your tendon stretched out.  Something like this:

United Ortho Plantar Fasciitis Adjustable Leg Support Brace Fits Right or Left Foot for Soreness Relief, Foot Pain and Stretching, Large, Black https://a.co/d/fT8C2Mu

Last, you need to religiously do achilles stretches. Tight calves and achilles are what cause plantar faciitis. 10 reps of 20 seconds 3x/day.  Stretch as far as reasonably uncomfortable, but not too much.  It will get better over time.  https://youtu.be/vU_FVahd4HI?feature=shared

If you do these things, you are looking at 6-9 months of recovery, although it will improve as the months go on.  There is no rushing this, so don't try.

Good luck.
[kjs6dlf] (score 7, diepte 1) Yea I had quite bad PF in 2022-23 and wearing Hoka Kaha boots really helped - relatively high stack but very comfy (good for wide feet) with plenty of midsole between you and the ground.


Went to see a PT and they pointed suggested that strength training would be the most help as I wasn't really doing any. This, along with stretching as others recommended and the PF is basically gone.
[kjrnrpd] (score 6, diepte 0) Rolling a golf ball around under your foot. 

Doing some specific stretches.

Using arch supports. I use Superfeet Trailblazer. 

I found that using very rigid boots helped. They prevent my feet and ankles from flexing unnecessarily as I move. I use Asolo 520's now, and they've been really good for me.
[kjrlk3z] (score 4, diepte 1 OP) Many thanks
[kjrl5d5] (score 4, diepte 0) I do chase's exercise for training, he's got lots of stuff that can help

[newer video ](https://www.youtube.com/watch?v=gkImPA_R7uI)

[old video ](https://www.youtube.com/watch?v=Mw2PNPsx9oI)
[kjrovmi] (score 3, diepte 3 OP) That’s probably my problem.. I’m now in my 50s and I’ll go off on a 15km hike without warming up.
[kjrpjlb] (score 3, diepte 4) :( I learned my lesson... I had it for a long time before anyone realized what was going on, and at the time I worked in the mountains, so I never want to go through that again! Kept tennis balls in my office. 

The rocker is pretty effective and cheap.
[kjsobru] (score 3, diepte 1) This worked for me too. I have high arches, so really need the support when walking long distances.
[kjt537q] (score 3, diepte 1) This also worked for me, I got a pair of arch supports for all my shoes and along with the advice of my doctor to get a pair of supportive slippers for wearing around the house (no walking barefoot) I’ve been PF free. It was a slow healing process but the preventative measures have made a difference in the long run.
[kjsnoin] (score 3, diepte 1) This is the real answer. I suffer from PF and have been to a specialist twice. I still have pain and even the cortisone shot didn’t end the pain. The boot and exercises and time are the answer. I will most likely still be in pain when I step onto the AT in 45 days but it has improved from where I had been before seeing the pediatrist.
[kjsuftn] (score 3, diepte 1) While I am in complete agreement, I found switching to Hoka sneakers worked far better for me than sole inserts.  My PF was exacerbated by standing/walking on concrete all day and the Hokas make a world of difference in keeping my feet pain free after handling the PF.  Plus they have a no-questions asked manufacturer 30 day return window if they don't end up working for you.
[kjrn2j1] (score 3, diepte 0) I've been wearing hoka one ones and they have cured my issues. Hoka also makes hiking shoes/boots.
[kjt3yy0] (score 3, diepte 2) Great!
[kjrrfyd] (score 3, diepte 0) I totally screwed my feet 4 years ago by doing a thru without much conditioning, and a way too heavy pack. 

I'm just now getting to the point I can walk without pain. It took time, good shoes, and very good insoles in anything I put my feet in.
[kjs114e] (score 3, diepte 0) I've had the least problems with it when wearing out-of-fashion, rigid and heavy hiking boots by Meindl. They enable me to reach daily mileages that would leave my feet absolutely wrecked in something like trail runners if I forced my self through it. For me, heavy boots are a bit like a real 4x4 compared to a regular family car: I'm spending more energy per mile, but getting things done that would be impossible for me in lighter gear.
[kju01pa] (score 3, diepte 0) An alternative stretch I haven't seen mentioned yet is:

 take a towel and hold each end, put the middle of the towel under the ball of your foot, and pull your foot back towards you. This stretch was shown to me by a medical professional specifically for PF
[kjvno02] (score 2, diepte 1) This is the way
[kjss7lf] (score 2, diepte 2) Had you tried shock therapy? I used that for Achilles Tendonitis (it helped, a lot!) and my podiatrist said he has good results with it for PF.
[kjwmgjr] (score 2, diepte 1) My hoka hiking boots have made all the difference for me! (Granted it’s for hallux rigidus in my case.) I’ve also recently been testing out NorthFace trail shoes and insulated winter boots with Vectiv in the name that have similar rockers, and they’ve been good so far.
[kjso0w5] (score 2, diepte 0) I struggled with it for years. Stretching helped but I ultimately fixed it with a night sock. You can Google them and see what they do.

But the problem is your feet curl up at night and heal that way….. it is a constant game of healing then tearing apart that healing in the morning when you take those first steps 

Experimenting with supporting insoles can also help and at least keep you moving
[kjso61d] (score 2, diepte 1) The night sock is another type of “night boot”. The night boot is more effective, but also pretty uncomfortable when trying to sleep. I preferred the sock
[kjto8b8] (score 2, diepte 0) Avoid by: weight loss, lower pack weight, quality inserts…but if you’ve already got it, either 3 weeks or more off or suffer onward. Rest is only cure. 

Hoka’s w inserts, 20 lb. weight loss,  and cycling worked for me. 

One season I took up mountain biking instead. Solved it. Biked CO and AZT trails.
[kjuajfd] (score 2, diepte 0) Look up plantar fascia roller. Preferably one that you can freeze too.

Otherwise roll whatever you can on your foot. Tennis balls were too soft for me. Cold marbles gave me sweet relief.

Switch your shoes up on the reg. Arch support is a must

Anti Inflam meds and cream.

Rice

Bedtime splint
[mhcwlkq] (score 1, diepte 2) Can you walk barefoot now that it’s healed though? Or do you think the extra support just masks the issue?
[mhdt05h] (score 1, diepte 3) Not sure about masking the issue or not because I try not to walk barefoot around the house or on flat surfaces outside but I have had zero issues on grass or sand.
[mhi8g1z] (score 1, diepte 4) Thanks for the info!! I’m going on a 2 month trip soon with my PF feeling like it’s only half healed, and plan on going barefoot in squishy terrain (grass & sand lol) so very cool to know!
[kjuzsru] (score 1, diepte 1) This.  I tried stretching, strength training, rest, in the end, consistent arch support beat it down.  I have a pair of SOLE arch supports in all my shoes now.
[kjrlbyc] (score 1, diepte 0) Check out r/plantarfasciitis. And I recommend trying PRP if it persists after more conservative treatments, but PRP can be expensive.
[kjrlik1] (score 1, diepte 1 OP) Many thanks.
[kjstjn9] (score 1, diepte 3) I haven’t tried shock nor has my dr recommended it. I tried other fixes and herbs for 8 months before seeing the dr with no improvement. 
I love my Hokas and I have arch supports added to them. 

Also of note: I credit zero drop Altras with my initial injury.
[l5bk0el] (score 1, diepte 4) i shit you not i credit altra zero drop to the start of mine :(

transitioned and did slowly but somehow ended up with such a serious pain :(
[kjtyo80] (score 1, diepte 1) This is the post OP is looking for, it is mostly accurate. However it doesn't always take as long as 6-9 months, I have seen people recover in under 3 months many times.
[kjrm342] (score 1, diepte 0) Good info + exercises here https://www.mskcc.org/cancer-care/patient-education/plantar-fasciitis
[kjrss1b] (score 1, diepte 0) I use heel cups and get remedial massage/dry needling
[kjsdr52] (score 1, diepte 0) I have been getting over foot issues by wearing barefoot shoes on regular days, and shoes with good support and padding on hikes.
[kjtu9vn] (score 1, diepte 1) Aka night splint. I just started using one for my PF, and it's already making a difference. If OP works a desk job like me, a foot rest is also helpful to keep the feet at 90 degrees during the day.
[kjsrx4e] (score 1, diepte 0) I suffered with it for a couple of years. Go see a good foot doctor. It's possible that it will go away with minimal treatments. Mine became chronic and I had to get surgery, but I'm back to hiking again, so there are options. Surgery was basically my last option after I tried everything else.
[kjthvgq] (score 1, diepte 1) I also had surgery. Best thing ever!
[kjssg60] (score 1, diepte 0) 1)Rest first to see if goes away.   
2) custom orthotics!!!
3)ibuprofen, ice and gentle calf stretches.   
4)Roll a ball under the arch of your foot( I use a softball 🥎 but friend uses a golf ball - (that’s too small for me and hurts).   
5)Go see specialist cos this often comes with heel spurs ouch.   
6) Cortizone shots ***** worked amazingly for me BUT can lead to torn Achilles (which did happen to me)

40 years of this shit.



I’ve had this for almost 40 years. I try to do calf stretches and rolling a ball under the arch of my feet tends to help. I use a softball 🥎 or lacrosse ball. A friend says a golf ball works well for him but it’s too painful for me to use.
[kjsss7v] (score 1, diepte 0) Get a small plastic water bottle to freeze. Leave a bit of room at the top. Roll it under your foot while watching tele. Take breaks!
[kjsu14u] (score 1, diepte 1) I also went to boots and left trail runners behind. My issue had been going too hard in running shoes a bit early in the season. It began to feel like something I would always deal with but it's been a while. You'll see the other side too!
[kjst7uc] (score 1, diepte 0) Also search myofascial release of calf muscles.  It has helped many people with plantar fasciitis
[kjsv9pi] (score 1, diepte 0) After years of trying everything and anything I could, and nothing helping, a friend told me to buy new, supportive sneakers/running shoes, and wear them 24:7. Only take them off in the shower or in bed. Don’t put a foot on the floor without them on. It took a few weeks, but it’s completely gone now. Good luck!
[kjsvhqs] (score 1, diepte 0) I've had really bad PF twice in my life, and my best advice is to LET IT HEAL PROPERLY.  Do the rest, the icing, the stretches, etc.  TAKE THE TIME IT TAKES.  Otherwise you will suffer for WAY too long.  Seriously, just take the time off and let it heal.
[kjsvndj] (score 1, diepte 0) It may seem crazy but put your fingers between your toes. Most shoes smash the toes together locking up the foot, after many many years. But just work on stretching your foot. Touch it everyday, don't forget about it!! And the tennis ball thing will really work! It's a stretching technique!! The shoe insert is really just a way to sell you a fake arch... my opinion but you don't need a fake arch just learn to take care of your feet. Not trying to be mean but seriously most people never ever stretch the feet and it will fix it.
[kjsxdn3] (score 1, diepte 0) Switched from hard boots to trail runners with custom inserts. Between that and stretching I haven’t had a flare up in 5 years.
[kjszni5] (score 1, diepte 0) I solved mine with more stretching and regular use of Hoka One shoes. In fact I even wear them work. Now that it’s under control I’ve branched out to On running shoes, Alturas, and a few others. In general for me trailrunners everywhere plus stretching has been key…
[kjt011b] (score 1, diepte 0) Superfeet copper insoles saved ne
[kjt5rv0] (score 1, diepte 0) Yoga helped get my PF under control. Also, I don’t buy shoes without removable inserts - I replace with PF specific inserts. Echoing the Hoka recommendation - one one’s are amazing and yes, I replace the store insert w a PF insert. Also recommend the Hoka hiking boots.
[kjt9pq5] (score 1, diepte 0) Shoes and cushion will help, but stretching and sleeping with a [strassburg sock](https://www.google.com/gasearch?q=strassburg%20sock&source=sh/x/gs/m2/5) on is what really counts. 

For the stretches, do heel drops and lunges to stretch your calves.
[kjtaz5b] (score 1, diepte 0) P.F. presents in many ways, I believe, and what works for some may not always for others.   Mine is tended to with a lot of foot and calf stretching.   Toe pulling.  Heel dropping.   Ankle rotating.
[kjtbyyt] (score 1, diepte 0) A lot of these are great refs! I messed my PF up playing soccer. Did a Sedona hike about 3 months later while experiencing daily issues, but the stretching during the hike helped. 
One suggestion for on trail help is elastic bands. They weight nothing and are great ways to stretch lower body, and PF, after you get out of car, stopping on trail, waking in the morning. Depending on the band, you can twist and brace your foot to get some nice stretches in.
[kjtg4pg] (score 1, diepte 0) Last time my fasciitis tried to kick in again I got arch support gel pads and metatarsal pads for good measure. At first I wore both in combination and that let me walk my usual 18 miles no problem, and then I began alternating between them as I got physical therapy. Now it's gone away again.
[kjtgrxm] (score 1, diepte 0) Are you somebody who’s committed to a specific brand of shoe?

I wore a specific brand for many years because I thought they were great.  Went through a period of about five years of on and off fasciitis and tried all the various stretching, insoles, exercise, never-be-barefoot, yadda yadda stuff you’ll see recommended here.  

One day about seven years ago I bought a pair of shoes from a different brand.  Never had fasciitis again.
[kjtnryu] (score 1, diepte 0) Ush, I've been bothered by this since August. The physio gave me some exercises, like going up on your tippytoes repeatedly until your calves are tired. And do the "opposite" movement, where you roll your weight back and stand on your heels. He also advised me to change shoes several times a day.

I still feel it, but it's faded and manageable now.
[kjtp3dc] (score 1, diepte 0) Welcome to the club! Inserts can help, but I also have a few exercises I do to strengthen my feet and legs to prevent the pain. 

Queue standard disclaimer, I’m not a doctor, just a long time sufferer of plantar fasciitis. You’ll notice only a two of these specifically target the foot, but I noticed if I strengthen my entire leg it keeps things better aligned and prevents pain. Takes about 5 minutes to run through these and that’s enough to keep me pain free

1: Banded monster walks - https://youtu.be/C8H-VTSBwIQ?feature=shared

2: Single leg toe stands - https://youtu.be/ak3sZPQq-ag?si=4w16OxrIlz_ep9hh

3: Banded foot eversions - https://youtu.be/50YDq8_OA_w?si=dPtMDTlJsjswHdsu

3: Get and use a calf stretcher!!
[kjtr36r] (score 1, diepte 0) Finding and massaging tender spots in my calves has been really helpful for me!
[kjtte1i] (score 1, diepte 0) I have spouts of PF and two things I'd say are buy some OOFOS slippers for around the house and if it's relevant, try to lose some weight. Honestly I've been surprised even by a few pounds making a difference.
[kjtv0n8] (score 1, diepte 0) Custom orthotics from a podiatrist fixed mine in 2 weeks.  Suffered a year had shots in the heel (painful!) and nothing worked except the custom orthotics.  Superfeet did not work.
[kjw4dw8] (score 1, diepte 1) A golf ball works well. Even when I travel I slip one into my luggage.
[kjuclfj] (score 1, diepte 0) Don't put pressure on yourself to exercise in pain.  Take time off.  And streeeeetch .
[kjuhc4b] (score 1, diepte 0) I did allllll the things. Inserts. Stretching. Ice and heat. Physical therapy. Shots. I finally had surgery and it gave me the ability to walk without pain again. I hope yours resolves with stretches inserts!
[kjumo51] (score 1, diepte 0) Since it does seem to be suggested yet:

I preferred KTape to inserts and it’s easy to learn. I slowly reduced the tension over time as my foot healed. (mine was mild but aggravating as I was training for a marathon)
[kjvkow2] (score 1, diepte 0) Have a podiatrist make custom inserts. Only thing that works for me.
[kjw8f1b] (score 1, diepte 0) I had a chiropractor who would do the electro-thingies they use on your back on my foot then adjust both feet. At the same time I got Plantar Fasciitis insoles from a company called Abeo and decent shoes, and that combination finally got rid of the plantar fasciitis after years of trying things.
[kjy8159] (score 1, diepte 0) it hurts so bad glad this came up
[kqxxgcw] (score 1, diepte 1 OP) I was given 18 months for it to heal.
[kjya2cr] (score 1, diepte 0) Inserts.  Oboz brand hiking boots also have really good arch support…I haven’t even needed my inserts when hiking with these boots.
[kk0ewkg] (score 1, diepte 0) Superfeet green insoles, lots of calf stretches, ice, ibuprofen gel and importantly rest. All helped me but what really helped was not walking as much during lockdowns. 
Problem with a foot injury is you can rest it like other body parts. If you do 10,000 steps per day as recommended, that’s 5,000 impacts to an already injured site.
[kjro2s5] (score -1, diepte 0) No fascists in hiking.  I’ll see myself out…
[kjskzgi] (score -2, diepte 0) I take krill oil and never had the pain again.
[kjsy9qu] (score -3, diepte 0) Look for the cause of your plantar faciitis. There is something else going on. Look for vitamin deficiencies. Get thyroid levels checked. Get your home checked for environmental factors that could cause health problems, such as mold.

