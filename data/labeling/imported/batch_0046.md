# Label-batch batch_0046

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
Schrijf het resultaat naar `batch_0046.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: es0ngs, 542g08, 1cidp1r).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD es0ngs ===
SUBREDDIT: r/ems
DATUM: 2020-01-21  SCORE: 1383  REACTIES: 133
TITEL: Don’t put your feet on the dash...
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ff74nhc] (score 545, diepte 1) Full disclosure: I do this in the summer because I’m super short and when I put my heels over the A/C vents it blows nice cold air into my clam
[ff72g3l] (score 284, diepte 0) Had an ex-girlfriend that would do that while I was driving.  Used to make me nuts.  I would demand she put her feet down.

Her:  God don't be such a goody goody.  Who cares!?!

Me:  I care for two reasons: 1) you're messing up my dash 2) there is an air bag there and your knees will be blown into your face if we have even a minor accident.

edit: grammar
[ff71wjf] (score 253, diepte 0) That’s not supposed to be there.
[ff7iji2] (score 180, diepte 3) A soft, labial breeze
[ff7fr7h] (score 147, diepte 1 OP) Only person so far who has correctly identified that this is a child.
[ff7fc53] (score 138, diepte 2) What a fantastic image
[ff7f9wv] (score 133, diepte 0) Lt femur compound (open) dislocation Rt hip. Most likely cause is an MVA with the child sitting and being thrown forward into either the dashboard or the back of a seat with bent knees, all the force will be transmitted through the femurs resulting in this type of injury.
[ff7h6b2] (score 88, diepte 3) The epiphyseal plates are not closed
[ff71zop] (score 67, diepte 0) Wow, talk about fucking yourself
[ff7ijo0] (score 55, diepte 1) I concur
[ff7vzjh] (score 52, diepte 4) Thats why I just refrigerate the o2 tanks and let a cannula blow tundra cold air across my rugged terrain.
[ff7g8al] (score 49, diepte 1) I'd honestly board them at this point. I despise boards , but when the whole body needs a splint...

And call for all the pain meds I had on my truck, and then some. I'll bag them IDC. It's probably preferable to the pain they're in.
[ff81tve] (score 48, diepte 4) I don't like that your comment reads like an air freshener description
[ff7s96h] (score 47, diepte 3) Lol EMTs and paramedics don't have that kind of money
[ff7no5x] (score 44, diepte 2) You need a car with those perforated seats that blow nice cool air into your clam. And taint. And starfish. A friend told me about it.
[ff7d5fi] (score 44, diepte 0) Does anyone else see the smiling clown in the middle of that guys pelvis?
[ff7j0sm] (score 39, diepte 2) Do you know many prehospital providers who second as a radiologist? 

You sound like you expected this sub Reddit to do anything beyond “ohh and ahh.”
[ff7kj3x] (score 39, diepte 2) Yuss. My guy. I always hated how once backboarding got canned, people acted like they didn’t exist. Yeah, let’s not stabilize their pelvis soup, and just let it all hang lol.
[ff7nwv8] (score 36, diepte 3) I don't doubt it for a minute. I fell from a horse at 10 flat on my coccyx and broke it. decades later still get a royal pain in the arse on occasion
[ff7rb20] (score 35, diepte 5) If you look at the top of each femur, where the round ball shaped part is there is a thin line that divides it in half, as you get older that fuses together. Imagine below for better visual.

http://img.tfd.com/medical/Davis/Tabers/th/p23.jpg
[ff7j59g] (score 34, diepte 2) That kid could very well have hip issues for the rest of their life because of this
[ff82yxo] (score 30, diepte 4) This is how Gwyneth Paltrow should have marketed her new candle
[ff7nuhf] (score 29, diepte 3) > pelvis soup

Come hell or high water, I am going to use these words in a radio patch one day.
[ff7kz7t] (score 28, diepte 2) The gluteal tuberosity seems to have redefined itself however
[ff7goa6] (score 27, diepte 2) How can you tell it’s a child?
[ff7kd91] (score 26, diepte 3) Just one of the guys
[ff7eza5] (score 26, diepte 0) I think they're injured.
[ff7k6j7] (score 26, diepte 0) Oh man oh man... position of comfort?
[ff7mg8x] (score 25, diepte 2) Out of all the ways I’ve been disappointed in my life, this is the most recent
[ff7mpz9] (score 24, diepte 3) Pelvis soup is a good medical term.
[ff76qm7] (score 22, diepte 0) Dare I say it.
*balls deep*
[ff7f9x2] (score 22, diepte 0) Oh my word! Oh how that would hurt! But also, I'd love to know how TF you stabilize that
[ff7nsom] (score 20, diepte 2) Ah I see you’re a woman of culture as well
[ff7q6iv] (score 20, diepte 5) “The bone thingy looks like its in the wrong place”
[ff8frxt] (score 19, diepte 5) “Summer Muff - By Gwyneth”

*Honey, come smell this candle!*
[ff87dku] (score 19, diepte 6) What kind of rhythm is this?
[ff843fd] (score 17, diepte 3) I'll take things I've never had for $1000, Alex

I wish I had those things, but backboard is honestly the best I've got available to me so it's what I thought of
[ff7nwsn] (score 15, diepte 2) Why didn’t I concur??
[ff7ouw5] (score 15, diepte 2) now this is just sensible. Used to do the same with the ceiling fan at home and some baby powder. Called it polar bear-ing
[ff7l3jo] (score 14, diepte 3) Dont need to be a radiologist to identify this
[ff7n0m0] (score 14, diepte 0) Just a SAR volunteer here, very little medical training, but something doesn't seem healthy about this X-Ray!
[ff7symt] (score 14, diepte 0) It's been a while since I've full-body cringed. I guess today was the day to remedy that.
[ff8rnws] (score 13, diepte 1) Pt is a female. And a child.
[ff7d313] (score 13, diepte 0) Death by snu snu
[ff7w25v] (score 13, diepte 3) That would be my best guess. Just try to stabilize as is, as best as possible.
[ff8g0ci] (score 12, diepte 5) SpO2 stats low, must upgrade to CPAP @ 25LPM
[ff7f775] (score 12, diepte 1) Well, I do now 🤡
[ff9e5kq] (score 11, diepte 1) You know damn well there isn't one when you're getting assfucked by your own femur.
[ff7xi3k] (score 11, diepte 0) Poor kid, prognosis?
[ff7zbk4] (score 10, diepte 2) Everybody's going to cite the epiphyseal plates, but I'd say that the weight distribution is the first tell.
[ff7tyjb] (score 10, diepte 2) I don’t know how you’d get the legs into anatomical position though... just leave them splayed out and cushion with pillows and padding?
[ff7ve34] (score 10, diepte 1) I saw this on my smart watch. Saw the title and scrolled down, watching it get worse and worse. It's one of those times you wish you had a slow motion camera pointed at you at all times
[ff87s6t] (score 10, diepte 0) "the leg bones connected to the... Whoops nevermind"
[ff8fjw6] (score 10, diepte 1) Judging by the title: kid puts feet on dashboard. Car gets into accident (this doesn't tell us anything about the driver - driver could be completely at fault, completely innocent or anything in between). Accident causes air bag to poof (I'm just gonna assume that's the right word in English). Air bag poof causes kid to do origami.
[ff7srhe] (score 9, diepte 1) Speculative assumption. Clinically correlate imaging with patient symptoms.
[ff7leyz] (score 9, diepte 4) That’s what I’m defining as oh and ah.
[ff7wbfm] (score 9, diepte 1) If I remember correctly, traction splint is for mid line femur fracture. This looks too far up as best as I can tell by the picture. I would stabilize and pad as much as possible in place and then give all the drugs they can handle.
[ff7wijb] (score 9, diepte 0) This poor child... that’s gonna be a long recovery.
[ff82gf4] (score 8, diepte 2) Best option would be a vacuum mattress, or if the child is small, a large vacuum splint does an excellent job. Advantage is all the natural voids of the body are supported, unlike a backboard unless you pack them with towels etc.
[ff9shal] (score 7, diepte 5) Well he's ridiculously gay, so I hope you're not expecting something sexy.
[ff84et9] (score 7, diepte 4) Just unionize your company, then you van make a little more than minimum wage 👌🏻
[ff7femf] (score 7, diepte 2) [Can't sleep... clown will eat me...](https://www.youtube.com/watch?v=U3yuFlvRyqM)
[ff7xld1] (score 7, diepte 4) Username checks out
[ff7zbuf] (score 7, diepte 4) Don't need an x-ray either I bet
[ff8gdz6] (score 6, diepte 7) The squiggly one
[ff807tr] (score 6, diepte 4) Always glad to inspire lmao
[ff80iba] (score 6, diepte 4) That’s all you can do, I imagine. They need a surgeon, bad. Luckily I’ve never had to McGyver that bad, but my medics have done some crazy sheet-diaper pelvis stabilizers on old people that fell. Really didn’t take much to get the job done.
[ff7o85r] (score 6, diepte 0) This is not the boner you were looking for
[ff7nysf] (score 5, diepte 3) I concur that you should have concurred
[ff86kt9] (score 5, diepte 4) Or a BMI that would allow airflow anyway.
[ff7zgz1] (score 5, diepte 1) Never thought I'd say it, but I think I'll pass on death by snu snu
[ff7dp0m] (score 5, diepte 1) Nah I see it
[ff7ewax] (score 5, diepte 0) Like at that point, it would be sticking outside of this person right?
[ff8p92k] (score 5, diepte 8) The bad squiggle
[ff7vxsh] (score 5, diepte 0) Will, at least it's a clean left humorous fx
[ff81xgq] (score 5, diepte 0) The longer I stare the worse it gets, much like when I find myself in front of a mirror
[ff88xow] (score 5, diepte 0) I think I see the problem.
[ff8c52n] (score 5, diepte 0) Saw this and said “NOPE” out loud
[ff9ici2] (score 4, diepte 3) - that line from the med student (or resident) in “Catch Me If You Can” is one of the funniest portraits of resident/attending/med-student relationships that I have ever seen! It makes me smirk every time I think about it. Oh, the self loathing and self doubt and deification of the knowledgable ones when you are new to medicine. So close to the truth.
[ff7nlx7] (score 4, diepte 2) https://www.amazon.com/Handheld-VersionTECH-Rechargeable-Household-Traveling/dp/B01HGI0S6O/ref=zg_bs_3015416011_1?_encoding=UTF8&psc=1&refRID=017S1M4E4H4E1BACQ5A1
(52 reacties met lagere score weggelaten)

=== THREAD 542g08 ===
SUBREDDIT: r/Frugal
DATUM: 2016-09-23  SCORE: 170  REACTIES: 131
TITEL: I work in a warehouse and I have to walk a shitton. I get my first paycheck tomorrow and first thing I'm doing is getting some reliable shoes. Can you suggest me a pair?
POST (source_id=post):
I'm only getting ~400$ for a week of work. Been working there for two weeks and my feet have been killing me. I really need a new pair, but unsure of where is the best price to quality ratio I can get. Thank you for your time.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d7ycayt] (score 61, diepte 0) Try ShoesforCrews.com. Their stuff isn't super spendy, but my fiance claims they're the only shoes that have felt good and lasted more than a month before losing support. (He works 10-12 hrs a day on conrete floors and is a big guy.) Lots of different types.
[d7yceft] (score 32, diepte 1) Yes, new balance ended my aching feet. On an informational aside, shitton is not a measure of distance. It is a measure of weight. Perhaps you meant to say a fur piece, or dam near to the holler' and back, or even further than my dog can chase a coon.
[d7yc41g] (score 30, diepte 0) My dad worked as a janitor and said that walking on concrete floors really made his feet and back hurt until he started wearing New Balance sneakers for work. If you don't need to wear boots, try those instead.
[d7ydzg5] (score 30, diepte 0) I like Merrell shoes and have had alot of luck with them. I work 12 hours on my feet too
[d7ydpmw] (score 17, diepte 1) i am constantly on my feet.   Also my job has me walking backwards a lot.  My feet were killing before I started wearing Shoes for Crews at work.  Specifically the ones called Primos.  

Also years ago when I was a waiter I wore them and then sort of forgot about them. They are the best Ive tried.
[d7yero5] (score 16, diepte 1) Specifically, the Moab. If you're wearing Merrells, then 9 times out of 10 it's the Moab. If you're wearing the Moab, then 9 times out of 10 it's the Moab Ventilator.
[d7yepo2] (score 14, diepte 4) "Time wounds all heels."

You're right; I meant idioms.
[d7ybmaa] (score 13, diepte 0) Good boots are gonna avg about 120-150 Quality drop of quickly from there. Trust me I spent too many years in pain from cheap boots. I wouldn't blink before spending 200 if the boots made my feet smile. They will easily last twice as long so be sure to take that into consideration. It's tough to say where to go but your not going to find a good selection in most big department stores you have to find a spot that sells all your hardcore construction clothes like carhart and the like. Treat you feet good and you knees,feet,back, and neck will thank you.

Source: 25 years in construction.
[d7yd7pd] (score 13, diepte 2) I appreciate the colorful aphorisms, but I'm with OP.  What's lamentable about warehouse work isn't so much the distance traveled, but the hours on your feet - a shitton of walking.  

If he had to walk to the valley and back, it would at least be a voyage with a clear purpose and a destination.  Alas, he's cursed to wander for hours, but to end up right back where he started at the end of each shift.
[d7yhwnp] (score 13, diepte 1) I've worked in restaurants my whole working life, and have always worn these. They are fine but they wear out faster than you think. They are.more suited for standing and working more than walking a lot. I would look for a shoe that had a rugged sole and great arch support. You may get laughed at but Birkenstocks are amazing for support.
[d7ybhq9] (score 12, diepte 0) Check out r/running. They have a few spreadsheets and articles that have been posted rating shoes. It gets a little intense w information. Also, runners know their shoes! Most of them want to get the best bang for their buck as well.
[d7yctrl] (score 9, diepte 2) I was an order selector for 2 years in there and that's when I realized the importance of good boots. You put a lot of miles on in The warehouse. As far as footwear goes it's very comparable. TAKE CARE OF YOUR FEET. My wife sold shoes all through high school and told me this 18 years ago and I finally started listing about 5 years ago and wish I could go back and make 20 year old me believe it.
[d7yd4h9] (score 9, diepte 0) Check out brooks man. They are life changing. Just get last years models and they arent too expensive. You're welcome.
[d7ycp9w] (score 8, diepte 0) I'd suggest Merrills or keens, both hiking shoes. Plenty come in a more sneaker-like look as opposed to the typical hiking boot style. That will start at $100 a pair most likely, but you will save yourself in the long run.

I second the advice of the posters who suggest a running shoe store or the running sub. Just because you won't be busting out a 5k doesn't mean they can't point you in the right direction.
[d7yerck] (score 8, diepte 0) Many good suggestions in this thread, but also check out the feet of your co-workers and see what they are wearing. Especially the people that have been working the job for awhile.
[d7yfzhr] (score 6, diepte 2) Professional mover?
[d7yf4md] (score 6, diepte 0) Rockports are phenomenal and very very light and comfortable.  My main shoes though are Eccos.  I bought a pair from Macy's once for about $130 I think, wore them 5 days a week for work, they lasted 7 years.  I replaced them with the exact same pair a few years ago, going strong.

Edit: Oh, and take care of your shoes!!  They'll last a hell of a lot longer and look better too.  Invest in some nice wooden shoe trees and put them in your shoes every night to maintain the form.  And use a shoehorn to put your shoes on every morning so you don't break their backs.
[d7yca6t] (score 5, diepte 1) I'll second new balance and although cheaper than other's I love my 511’s.
[d7yfb5l] (score 5, diepte 0) drop 30 bucks on a great pair of gel inserts for whatever shoes you end up getting.  Worth every penny.
[d7z4wak] (score 4, diepte 1) It is important to consider that running shoes are designed with a certain set of compromises specific to runners. OP is using their shoes very differently than runners, and therefore should have a different search criteria, albeit with some overlap.
[d7yc4lg] (score 4, diepte 1 OP) haha i dont really work in construction though, just a warehouse.. Although would it be an extreme difference wearing boots instead? I've never worn them.
[d7yfxyv] (score 4, diepte 1) Also plugging New Balance, putting out joesnewbalanceoutlet.com as one of the cheapest places I've found to pick up a pair. NB has great support and they are one of the longest lasting shoes I've found.
[d7yfuxe] (score 4, diepte 3) Maybe he guides planes on the runway?
[d7yixn1] (score 4, diepte 4) Security for celebrities.
[d7yjyki] (score 4, diepte 1) One pair lasted me two full years in restaurants, so I can vouch for SFC. They were like $45 and honestly they were pretty ugly, but it is function over fashion in food service.
[d7yuj5y] (score 4, diepte 2) Well not so much for the specific, just general idea of footwear
[d7yf025] (score 4, diepte 0) I work in a warehouse too! On my feet for nearly 12 hours and walk ~6 miles a day sometimes. I got a pair of Doc Martens leather boots for about $130 a few months ago and they're awesome so far. They did hurt my feet at first but now that they're broken in my feet don't hurt at all at the end of the day. They didn't give me blisters or anything either when they were brand new. They may be a bit pricey but they are a good investment as they should last a long time. Hope this helps!
[d7z63hv] (score 4, diepte 1) Foot doctor recommended spensco incerts...wasn't wrong. They last over a year where gels lose function in 3 or 4 weeks.
[d7yg4wt] (score 4, diepte 0) I have learned over the years that the shoes aren't the problem - it's the crappy in-soles they put in them. Now I buy whatever shoes are $20-30, and then spend the same on a good pair of orthotic in-soles.

Give it a try. Oh, and replace them every 3-6 months for optimal foot happiness.
[d7yhv8x] (score 4, diepte 0) Zero drop padded shoes are pretty great if you're on your feet all day.  I work in a pair of Altra Olympus shoes (which is that company's most padded version) and they are awesome, like walking on little clouds.  They're a bit spendy, but you can find the previous year's versions on Amazon and eBay for much cheaper.  They fit pretty true to size, but will feel almost too big at first due to the huge toe box.  They also look pretty stupid, I call them my Spice Girls shoes, but the comfort is worth it IMO.
[d7yczd2] (score 3, diepte 2) I also like the hiking boot idea if you don't need steel toe. I have assumed the whole time you needed steel toe.
[d7ye2si] (score 3, diepte 3) Those aren't aphorisms. But here's one, 'A journey of a thousand miles begins with a single step'. Sorry, I can't think of any for feet or warehouses, but I tried!
[d7yffg2] (score 3, diepte 2) I have tried to figure out what sorts of jobs require a lot of backward walking. What do you do?
[d7ymavl] (score 3, diepte 5) Red carpet unroller
[d7zh3ed] (score 3, diepte 3) Probably a tour guide somewhere
[d7zls9g] (score 3, diepte 3) cleaning carpets.  you walk backwards and clean the rug in front of you. pulling toward yourself if that makes sense.
[d7zacqx] (score 3, diepte 2) Michael Jackson impersonator?
[d7zlsx9] (score 3, diepte 3) working on that.  the facial reconstruction is almost complete.  Im already white.
[d7zb4a5] (score 3, diepte 1) I don't recommend shoes for crews. Sketchers are more expensive, but have much more comfortable and long lasting non-slip shoes.
[d7yetes] (score 3, diepte 1) I have a pair of brooks sneakers. Most expensive footwear I've ever bought and absolutely incredible. Having never worn shoes that fit my 4E feet before, they really are mind blowing.
[d7zl3xp] (score 3, diepte 2) Yes, but then the same problem lies with asking strangers on the internet.
[d7yf9ye] (score 3, diepte 0) I used to be up on my feet all day long, walking a huge campus for my job.   I worked at the City of Hope, Duarte, California near LA.  That campus has six major sites, interconnected by concrete...  and my job included walking to each building all day long.   I carried a backpack satchel with me with my shoes inside, plus water and pain med's, and  at lunch time I'd switch both socks and shoes, and had a orthotic insert fitted which I'd use in the afternoon (and could remove as needed.) I'd add or remove some of those cheap foam inserts and saw a podiatrist for more help getting differing thickness of inserts - which do break down fast.   I had a heel spur developed that was so bad I had to have surgery to remove it (after I'd jumped down from the bumper of my truck and fractured the spur off the major bone in the right heel..  the foot specialist said he'd never seen such a long spur before.)  I lost many months of work due to that injury. (This spur grew on the bottom of my foot from the calcaneus bone - the thick heel bone, pointing about 2" towards the toes along the plantar fascia tendons)  and was screamingly painful.   The surgery to remove the spur was bad enough by itself and I had already been diagnosed with plantar fasciitis previously (foot pain when I first got every morning trying to walk to the BR from the bed) 
     It was a year post surgery before I could bear any weight on the heel.  For therapy I ended up walking at the beach on sand at midday (when it was hottest) for the comfort I got from the heated sand and to decrease my skin sensitivity from not bearing weight thru the heel at the surgical site, along with heel cord stretches.    My sons eventually built me a sandbox where I could walk barefooted at home 6" deep filled with fine playground sand, 2' wide  x10' long, and we'd sometimes get it wet to change the density of the sand.... 
     At night I"d wear clean tightly fitted high top basketball shoes to sleep in, which strangely helped hold he ankle in neutral position...  and after surgery wore metal "podus splints" on both feet to keep the foot in neutral and  prevent foot drop after surgery.)  Though I still have a minor spur on the left foot I'm not willing to go thru that surgery again.   When I returned to work I had new orthotics made to soften the blow of taking each step on each foot.  I still wear orthotics to this day but can now tolerate walking barefoot for short distances and can once again tolerate standing in line at the grocery store.    Seriously, I"d be sweating bullets by the end of the day before I had  surgery, and was crying in pain at the end of each day after surgery when I tried to return to work. I ended up going off work for an additional 3 months....   Plus my return to work included an addiction to Oxy; and coming off the Oxy was one of the hardest things I'd ever done in my life.    
      ONe learned to maximize one's time in one area, sitting as much as possible before walking to a new area - I'd end up tip toe walking to avoid weight bearing and it's pain thru the heel.    (I planned out my day traveling in a circle because I hated backtracking.) My orthopedic physician had me get some supportive hard cobbly shoes with leather uppers and  ortho soles thru the podiatrist's office (looked like clunky grandma ortho shoes meant for attaching AFO braces you see polio victims wearing. 
    I remained on anti-inflammatories for years due to the foot pain which in turn caused back pain, and ten years later I'd had to have both knees replaced.  I was two years post op before I was able to walk barefooted on my heels in a regular heel, toe push-off.   I also had great difficulty driving using my right foot on the gas pedal bearing weight thru the heel as it rested on the carpet and forefoot on the gas pedal... In time I opted for a manual transmission vehicle with cruise control and learned to drive using my left foot.    

   If overweight, reduce your weight to reduce further wear and tear on your feet, knees, hips.  

Remember your posture begins when your foot hits the ground. Mucking  up your feet means your body is like a stack of domino's where you hit the first domino on the ground, the rest follow upwards.  It all comes down!
[d7yfpth] (score 3, diepte 0) Man if you want the best steel toes money can buy get red wings. Red Wings cost a lot but they are so worth it. You have to get the red wing insoles and tuff toe add on because if you don't they won't be near as comfortable or last near as long.
http://www.redwingshoes.com/red-wing-shoe/608-red-wing-shoes/608-red-wing-mens-8-inch-boot-brown
[d7yht54] (score 3, diepte 1) Don't do this, this is why Costco and REI changed their return policies
[d7ygocl] (score 3, diepte 0) Also consider getting some orthotics made.
[d7z23ur] (score 2, diepte 2) /r/goodyearwelt
[d7yivua] (score 2, diepte 2) Sweet, thanks!
[d7yc91y] (score 2, diepte 0) "zero heel drop" is a term you should become familiar with.  Check for shoemakers offering zero-drop heels.
[d7yd4ja] (score 2, diepte 1) Yes, this.  Altra.

Expensive, worth it in pain-free-back and health-care-bill-free-ness.
[d7z66mc] (score 2, diepte 2) > You may get laughed at but Birkenstocks are amazing for support.

And if you care what other people think regarding your footwear, you have bigger problems than footwear.  Buy and wear Birkies if they make your feet feel good.
[d7z7ayw] (score 2, diepte 2) Yeah, I worked at Starbucks for a couple of years in college and mine disintegrated pretty quickly. 

Still worth the cost though if you need good traction. I used some Vans after they disintegrated (was planning on quitting to start an internship and didn't want to blow another $60 on shoes) and they slipped like crazy.
[d7z6aif] (score 2, diepte 1) I bought Keens after wearing Merrill's for years. They are comfortable, but not the same. I just switched to Salmon's and they are great. Merrill's were ultra soft and cushioning, and Keens were stiffer and supportive. Salmon does both.
[d809j0c] (score 2, diepte 1) Another vote for Merrells. As a speaker, I often stand all day teaching workshops and my feet were in agony at the end of the day.

After switching to Merrells, my feet are just a little tired at the end of the day with no pain.

My son works as a dishwasher and similarly had a lot of foot and leg pain and Merrells helped him too.

Merrells is the only brand of shoes I buy now.
[d7yd02j] (score 2, diepte 0) Check to see if your employer has a shoe truck that provides shoes/boots annually. Some jobs require steel toe, slip resistant shoes. If not, I would recommend getting a good pair of insoles, much cheaper than new shoes, and makes you feel like you are walking on clouds.
[d7yd304] (score 2, diepte 0) Get a zero drop, padded shoe.  While expensive, I would think a pair of Altra running shoes would be really smart.
[d7yfqgk] (score 2, diepte 2) Yup, I also have a Goretex pair for winter. Only shoes I can get a solid year out of with my 250 lbs of manliness and lack of foresight for wearing work boots on certain days
[d7ywuri] (score 2, diepte 2) > Moab Ventilator

My current pair is wearing out so went out and saw [they are on sale for $80 on their site.](http://www.merrell.com/US/en/moab-ventilator/018468373611.html?CID=MAR-Merrell-G-Shopping-Moab-Ventilator&CAWELAID=120144300000163167&CAGPSPN=pla&CAAGID=22336440965&CATCI=pla-196848179045) Good price.
[d7z9orn] (score 2, diepte 3) This.  These boots are the best things to have ever been on my feet except maybe a pair of converse, safety toe, non slip, zipper on the side boots that I got in the Air Force.
[d7yjd3i] (score 2, diepte 1) I go between the merrell and some keens love them both. Best investment besides the shoes tho are a pair of superfeet insoles. If you really want to make them last get two pairs and switch out every other day or so. I can usually make the shoes last 1.25 - 1.5 times as long (each pair) if I do that. Gives the lining time to dry out from sweaty feet. But superfeet insoles are a must. Green or orange are great. Black if you are just standing for a long time.
[d7zlqz4] (score 2, diepte 2) ouch!
[d7zo20x] (score 2, diepte 2) lmao. when it comes to text, reddit is cancer.
[d7yfmic] (score 2, diepte 0) When we moved to Chicago I HAD to find good walking shoes.

Very expensive, totally worth every penny. First time in my entire life my feet don't ache constantly.

[Finn Comfort](http://www.finncomfort.com). I'll never buy another brand again.
[d7yfpvx] (score 2, diepte 0) Been on my feet constantly for 13 years. Love my sauconys
[d7ygvny] (score 2, diepte 0) Chippewa boots. The Apache 6in is reliable, for $10 they with resole it for you, American made and full grain leather has saved my toes from getting killed a bunch of times in the garage. I recently wore them to Disney world on a day that started at 6:00am till security walked us out of magic kingdom at 1:00am and my feet could not have been happier. High of 90-something and only one sock change. A good investment in my eyes, my grandfather used to say there are two things he has never felt bad about spending money on: a reliable pair of shoes and comfortable mattress.
[d7yhrbn] (score 2, diepte 0) I really like nike free runs, they are foam sole which is good and comfy. Or if you need boots I'd look at redback, they make some great stuff.
[d7yj1b0] (score 2, diepte 0) I work at a vet clinic. I'm on my feet almost 10 hours a day, 5+ days a week. I usually go to the Nike Outlet nearby, and shop the clearance wall. Even just sale shoes sometimes. I go through about a pair a year, for about $35.
[d7yjny9] (score 2, diepte 0) For your paycheck, I'd recommend going to your local Wal-Mart and seeing what kind of steel-toe sneakers they have. Buy the best that fit you, and then spend the money on some sturdy arch supports for your feet. 

Worse comes to worse, you can always shape and sand some pieces of wood that fit your arches, stuff them in your shoe, and wear socks so you don't get splinters.
(55 reacties met lagere score weggelaten)

=== THREAD 1cidp1r ===
SUBREDDIT: r/Frugal
DATUM: 2024-05-02  SCORE: 30  REACTIES: 131
TITEL: Any budget Croc-like shoes that are as comfortable as Crocs?
POST (source_id=post):
I have plantar fasciitis. During the summer I would love to go around barefooted but it is too hard on my feet. Crocs really help cushion my heel around the house/yard. 

Before I buy a new pair of Crocs, has anyone found any other brand that is cheaper than $50 but still as comfortable as Crocs?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l28kx2f] (score 146, diepte 0) Don't cheap out on footwear, that's not frugal. Your feet are that which bears you, treat them well...
[l28h14p] (score 102, diepte 0) Try and check out stores like TJMaxx and Marshals. I've gotten a pair there before for $25
[l28iate] (score 60, diepte 0) Having tried fake crocs and real crocs, there really is a difference in the foot support. If you don’t care about color, you can often find discounted crocs on Amazon. There’s a yoga mat shoe I like. Regular price is around $40 but I’ve picked up discontinued colors for as low as $15.
[l29ay3h] (score 33, diepte 1) I also have plantar fasciitis and my podiatrist recommended Oofos. They are more expensive than crocs but they’re awesome
[l28ente] (score 15, diepte 0) Walmart has knock-off Crocs. Go try some on
[l28i7ma] (score 15, diepte 0) If you really really love crocs, on their website there's a sale right now for buy 2 and get 30% off. You could always buy two pairs (one for now, one for later).
[l2a1ueu] (score 14, diepte 2) I found a pair of Oofos at TJMaxx for $12. My spouse loves them!
[l28zibi] (score 10, diepte 0) Consider  Okabashi Eurosport Men's Sandal. I bought mine off Amazon and they were so comfortable I bought four more pair.  They last about three summers of daily wear.  Currently about $25.  I get them slightly larger than the chart so I can wear socks in slightly cooler weather.  Besides, as a retired White guy, I think socks with sandals are mandatory.
[l2b2u10] (score 9, diepte 2) +1 for Oofos.  I’m a relatively big guy (6’4” & 220#) and I use Oofos as house slippers. I hesitated to buy them because of the cost, but they’re probably my favorite footwear ever. I wear them 8+ hours every single day. When I work from home, I put them on first thing in the morning, wear them all through the day, and take them off just before climbing into bed. When I go into the office, I can’t wait to get home and put them on again. I’m coming up on two years and thousands of hours of wear, and the comfort and arch support are still great. I suppose mileage may vary if you wear them out in public (they’re pretty ugly). Oofos have been much better than my Crocs from several years ago that started giving me foot pain within about 6 months because they lost their arch support and the soles wore thin. I highly recommend Oofos to everyone.
[l28pyyl] (score 8, diepte 1) Just saw a bunch there last week!
[l293x92] (score 8, diepte 0) If you want something cheaper than Crocs that will help plantar fasciitis and last for years, try Okabashi flip flops. They may hurt the first two weeks as your feet get broken in, but after that the plantar fasciitis goes away and the shoes will last for years as long as you get the regular thick kind, not one of the fashion styles.
[l28o39f] (score 7, diepte 1) I honestly love my Walmart shoes. I have numerous pairs of slip on sneakers that are my most comfortable.
[l2bypmj] (score 7, diepte 3) +1 for Oofos recovery flip flops. They are unbelievablly good and I’ve tried to buy cheaper versions and nothing compares.
[l2b06ui] (score 7, diepte 1) Crocs are cheap dense foam and any other cheap dense foam shoes will be as good.
[l2a3qdq] (score 7, diepte 1) Do not recommend. They are so thin.
[l29rvyy] (score 7, diepte 0) Things to not be “frugal” about:

1. Anything between you and the ground (shoes, tires, flooring, mattress, chairs, etc.)
[l28grmb] (score 6, diepte 0) They often have sales on certain colors! Check their site and Amazon
[l29bvn5] (score 6, diepte 1) This. Exploding different colors/styles and the used-but new/like new sections have saved me so much money.
[l28phwe] (score 6, diepte 0) Just buy Crocs.  Spend money on your feet.
[l28j8b9] (score 5, diepte 1) Having 2 pairs is the best! I have my house crocs and then my outside crocs
[l2b0gg1] (score 5, diepte 3) No way! Lucky!
[l28rq89] (score 5, diepte 0) Walmart has a version still I think
[l29imi2] (score 5, diepte 1) Euro sandals require socks by law
[l29a22v] (score 5, diepte 0) If you have a Costco membership I saw a lot of good reviews here on Reddit for slide sandals made from that same foam material. I think it was $11.99 and the brand is 32 degrees (?). Everyone was raving how it feels like a cloud.
[l29lt4q] (score 5, diepte 0) Crocs are not overly expensive considering how well they do on (bad feet) and the material. They literally never wear down! Are they dirty? Throw them in the tub and spray them down.
[l28frbs] (score 4, diepte 0) I bought Chung-Shi, also known as Duflex in Germany. They have been tested in Germany to have no harmful chemicals, unlike most others of these types of shoes, including Crocs. Seems like they cost 50$ at [amazon.com](http://amazon.com), more or less the same as Crocs, though.   Here in Germany you can buy very cheap ones in discount stores for maybe 10-20 euro, but I don't want to know what toxic chemicals they feature.
[l29a03h] (score 4, diepte 1) Yes!! And they have a bunch usually. I scored some Crocs for my (Sasquatch) kid on Amazon for half the stated price on Crocs website.
[l2b2yis] (score 4, diepte 3) Yes. 100%.
[l290vax] (score 4, diepte 0) If you can find Vionic on sale they are fantastic. The only shoes I don’t have to wear orthotics with.
[l29asov] (score 4, diepte 0) I don't know if it still works, but in the past, I've picked out a pair of Crocs on their website, put them in the shopping cart and just left them. In a few days I would get an email offering me a discount to buy the items left in my shopping cart.
[l29b8b4] (score 4, diepte 0) Look on Amazon. I’ve grabbed returned crocs (look for the used-like new) that were never worn for $15. Almost all the used-like new are new items just not in original packaging.
[l29q9qp] (score 4, diepte 0) I just got a pair at Ollie's for like $4. Gardening shoes.
[l2caafo] (score 3, diepte 1) I picked up a pair at Kroger for $5 on clearance. They're cushier than my husband's Crocs.
[l28hzgq] (score 3, diepte 1) This comment has been automatically removed because it mentions Temu. Due to prolific spam we do not allow **ANY** mentions of the site.
Trying to get around this filter by saying something like "T$mu" may result in a ban.

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Frugal) if you have any questions or concerns.*
[l29b3mg] (score 3, diepte 2) My doctor recommended them to me too. I haven't gone to get any yet. They're really that good?
[l28wtqd] (score 3, diepte 0) I have a pair of slip on Adidas people have mistaken as Crocs.  Just as comfortable, more stylish, imo.
[l298twd] (score 3, diepte 0) Totes brand is cheaper and good quality
[l2a6nja] (score 3, diepte 1) Oh, the 32 Degrees slides were a lucky find for me. Depending on the year, they have been huge or just a bit tight, or just right when I bought last year. My plantar issues haven't gone away, no big promises, but the 32 Degrees slides help me complete the chores per day. If Costco lets you hold the slide up to your foot and see which will work, cool. If not, they're just over $10 lol. It's a bandaid to the issue, but a very affordable one.

Especially if you have carpet in your home, I can now highly recommend a toeless sock called Happy Feet. One of my friends that also has what I call "thin-wristed issues" told me about them, I've been using for about a month and I'm going to continue. Being in a culture that focuses so heavily on fashion and the look, women especially have worn shoes that won't do us any favors. Especially if you don't come from money and have worn shoes too small, your feet have developed and existed in a way that is unhealthy. The Happy Feet socks have spacers that go between your toes. I'm a daily user, and I feel improved even when I'm not wearing them. If I remember, they were about $30 but they have decent discounts often.

Just remember, you didn't break yourself in a day, so you won't fix yourself in a day.

I also acquired a balance disc from a Kroger, a round board a few inches of the ground held up by a rounded bit of material. It helps with my thin ankles. The theory is, if you can strengthen the surrounding systems your problem areas can catch a break and heal properly. We keep it in the TV room, put on a Nicholas Cage movie or zone out on the phone while balancing. The use of the board has sculpted everything below my arms, balance is serious business. 

Good luck out there.
[l29a2ld] (score 3, diepte 0) Crocs on sale and Crocs on clearance. Will save you time which will save you stress about it being not Crocs.
[l29e1wa] (score 3, diepte 0) Am I crazy that I don't think crocs are comfortable at all? I just use mine for yard work now. My reef sandals are way more comfortable.
[l2a24dv] (score 3, diepte 0) If you’re in the US famous footwear has a deal where you can do buy one bet one, if you’re a rewards member. They do have to be full price though. 

I have bought crocs from Marshall’s for I want to say $30.
[l28l1gi] (score 2, diepte 1) I remember seeing a thing some years ago where a woman had cheap flip-flops from Wal-Mart and the chemicals in/on the plastic rotted her feet away... I swore right then I'd never buy no-name footwear...
[l2caynl] (score 2, diepte 3) It was horrifying. I can't find the post but a quick Google search brings up news stories about similar incidents.
[l28h05i] (score 2, diepte 1 OP) In the past I have scored a sale. Since they don't seem like complicated shoes to make, I've always been curious if there is a knock off that is just as good.
[l28gvpr] (score 2, diepte 0) Check secondhand sites (fb marketplace, poshmark, etc). I always see tons of Crocs for sale on those sites.
[l2c4kgf] (score 2, diepte 1) This - also check resale sites like Poshmark for ones that are new with tags
[l28n3qm] (score 2, diepte 0) Just buy ugly colored Crocs on Amazon or check out TJ Maxx!
[l28o98n] (score 2, diepte 0) Some colors are cheaper than others on Amazon so I find the cheapest ones in my size and that's the color I get. I don't need any particular color, I have a hot pink pair and a tie dye pair right now.
[l28z9m7] (score 2, diepte 0) My mom has plantar fasciitis and swears by Oofos. They're not cheap, but her feet don't hurt!
[l29b2x9] (score 2, diepte 1) I second Vionics. I have plantar fasciitis and they make all the difference. Their flip flops are great and not too unreasonable if you find them on sale.
[l2b2qhq] (score 2, diepte 1) Vionics are the ONLY sandal that I can wear. You see, I carry a bit of extra weight (🚨 understatement alert) and I suffer from severe spinal stenosis. I must have good shoes with support or not only will my feet ache, but my legs and back will be screaming! They are pricey, but I’ve had them last for 3 years with heavy daily wear. It averages out to around $30 a year, so not bad for really good quality footwear.
[l2928ok] (score 2, diepte 0) eBay is a great place to buy barely used shoes.
[l297syn] (score 2, diepte 0) They are currently having a half off sale
[l29bt1n] (score 2, diepte 0) I bought knock offs at a dollarama but it didn't go over that well they're not as thick and comfy. Sometimes marshalls/winners/tj max equivalent has them for less though.
[l29c6th] (score 2, diepte 0) [These](https://www.amazon.com/gp/product/B071XSLW77) are just as good, to me. I bought a pair last year and like em just as much as my old crocs. Although, I don't have any foot issues, so maybe they're subtly different in a way I don't notice.
[l29wtff] (score 2, diepte 1) The tread will wear down, the tops not so much
[l29zqah] (score 2, diepte 2) Wear down some, but barely. I have the same two pairs for the past 7 years and they have been used daily at times.
[l29nol0] (score 2, diepte 0) I like my crocs or hey dude for around the house. Hey dude makes a model that dries fast and has holes in the sole.
[l29wqoo] (score 2, diepte 0) Try to find a Croc warehouse in an outlet mall or online.  They may not be as pretty as you want but they’ll do the trick. 

Also, people sell them on FB Marketplace, brand new, all the time. Especially immediately after Christmas. They’ll get them as gifts and be like… “what was my mother in law thinking??”
[l2ansbq] (score 2, diepte 0) what size do you wear? My husband passed away in September last year. I had just bought him a new pair of black crocs. He didn't get to wear them. I believe the size was 12 but not quote me on that. I'll need to check when I get home. 

 I'll be happy to give them to you. Just shipping cost. I'll DM you later tonight if you want the size info. and shipping details. I'll send a pic as well.
[l2avufg] (score 2, diepte 0) The *frugal* choice here is to buy real Crocs… but watch sales, look at outlet stores, etc.
[l2az6dm] (score 2, diepte 0) i love Tevas ! best sandals ever, so comfortable.. but probably like $50. but so worth it
[l2bn5w0] (score 2, diepte 0) I have some really comfortable and durable Adidas slides that are croc like material that I've been abusing for most of a decade. I don't know what they would cost cuz I've had them for so long.
[l2bsfvh] (score 2, diepte 0) If you keep an eye out online for sales you can find crocs for under $30! I got a pair that I maybe waited a month for and it was like $26-28 something like that
[l2gkyrg] (score 2, diepte 2) I’ve seen pretty well discounted on both, but I go through Google and sometimes journeys and academy will have them on sale. I think you can set Google alerts for price drops. I just keep an eye out and eventually I’ll find a sale
[l28kz5t] (score 1, diepte 1) They are sooo much more comfortable than crocs. I have a pair for work
[l298n4e] (score 1, diepte 1) Came here to say all my favorite shoes came from Walmart!
[l29kflx] (score 1, diepte 2) I just picked up a pair of Hoka flip flops (sliders) for $20 from a local liquidation place and they are pretty awesome but I don't plan on wearing them outside due to not having toe protection.

Did not know Hoka made slippers and I already love their running shoes.
[l2asqg5] (score 1, diepte 2) What 😭 That's awful!
[l2cpxe0] (score 1, diepte 4) Thanks for the reply and info because I had no idea.
[l28gti8] (score 1, diepte 0) I think it was black Friday that crocks has certain ones listed for $30. You might monitor their sales. 

I would still get something in the meantime even if it means paying more. Health is not something to cheap out on.
[l28hmon] (score 1, diepte 1) I'm in the same position as OP right now, but I'm way more picky about color. I have a pair I love, but I've worm them into the ground. I really want my next pair to be ballerina pink and I know I won't be as happy with them if I don't get that color.
[l28igdt] (score 1, diepte 2) My wife wears Crocs, yes, pity me.
Anyway, Croc's sells their shoes direct on eBay for about $30, and my wife found $9-10 knock offs on T e m u she likes, and she prefers their knock off lined ones over Crocs lined ones.

This is my second try. I mentioned   t e m u   so the post was removed.
[l29pdnp] (score 1, diepte 3) I love them everywhere except near sand. The sand is really difficult to get off because of the texture of the flip flops and it’s like a constant exfoliant
[l2bnkhc] (score 1, diepte 3) They are fantastic. I bought some at half the price on eBay.
[l28nhig] (score 1, diepte 0) Just buy crocs, or wait till they’re on sale. I find what you try and find cheaper alternatives they’re usual not as good. I believe like must things you get what you pay for and frugal isn’t about being cheap it’s about getting a good deal. Buy something good once rather something shit twice.
[l28q1rn] (score 1, diepte 0) Mrs. maxs_tearoff wears Hoka One One's Slides—specifically the Slides 2.  They are designed for folks with plantar fasciitis.  Super comfy and last forever.

https://www.fleetfeet.com/products/womens-hoka-one-one-ora-recovery-slide-2?sku=1099674-BBLC
[l28tcc7] (score 1, diepte 1) They do. It's on the work shoes aisle.
[l28wfw3] (score 1, diepte 0) I wear Clark's flip flops I got on Amazon. Great support, lots of colors, about $35. And they aren't Crocs haha
[l293c0e] (score 1, diepte 0) I don't have plantar issues but do have other issues with the soles of my feet. Crocs help but hey dudes were a game changer. They are so much more comfortable than reg sneakers and my feet don't ache as much at the end of the day. Just a suggestion to try them out if you see a reasonably priced pair, they also can be pricey.
(49 reacties met lagere score weggelaten)

