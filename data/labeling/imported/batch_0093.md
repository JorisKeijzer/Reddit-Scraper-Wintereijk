# Label-batch batch_0093

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
Schrijf het resultaat naar `batch_0093.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 17jxy60, 68tb9p, kdzaxp).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 17jxy60 ===
SUBREDDIT: r/AdvancedRunning
DATUM: 2023-10-30  SCORE: 68  REACTIES: 161
TITEL: Can I hear from runners who have recovered from plantar fasciitis?
POST (source_id=post):
Like the title says. I am hoping to hear recovery success stories. I am working hard on it and haven't run in quite some time but still experiencing a lot of pain and discomfort. The leaves are turning and the weather is perfect and I am so sad not to be outside. Some days I feel pretty pessimistic and I would really like to hear from people who actually recovered from this condition

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k741u8h] (score 70, diepte 0) Stay diligent with the exercises. Do exercises that aren't specifically foot related (calf and ankle strengthening, rolling your calves thoroughly). When you aren't running, wear supportive footwear and never compromise. I found that I would rest by not running but then spend all day on my feet walking and that would inflame it way more than just a run.

I've had a few periods where I was fighting plantar for months. I'm going to preface this by saying it's probably not good advice, but it's never gone away completely from full, no running rest. I always end up running a few days a week and over time the pain dwindles until one day I notice I haven't felt it at all for like a week.
[k74wa8d] (score 29, diepte 0) Okay you're getting lots of well meaning advice here but I don't think a lot of it is going to solve your actual problem. You're not going to foam roll, arch support, and orthotic your way out of it. 

To address plantar fasciitis you need to understand why it's hurting in the first place, and the short answer is that it's overworked. It's overworked because you have a breakdown in how your foot is supposed to function. When you walk and run, your foot needs to be able to go from being relaxed and conforming at landing to stiff and rigid at pushoff. When your foot is unable to make that transition, you end up in your case with a foot that is having a hard time forming that rigid lever to push off of, your tiny foot muscles try their best to be as rigid as the bones in your foot would be, and you end up with overworked muscles and really painful arches. 

The calcaneus (heel) bone is supposed to be able to shift inward (invert) and outward (evert) as you walk, and that's what determines whether your foot is rigid or soft. If your calcaneus is very stiff to where it can't move, or the muscles that control it are too weak to effectively move it, you're going to have foot pain. 

So now you understand why arch support, foam rolling, ice, etc. is not going to solve the problem it will probably make it worse because your overworked plantar muscles are now being stretched and pushed on in weird ways that it doesn't like.

The strategy to address plantar pain should be to:

*  **Retrain the movement of your calcaneus**
   * We can do this with an exercise called "heel rainbows", where you lift yourself about halfway into a calf raise, using a wall for balance, and practice moving just your heels all the way outward into eversion and all the way back inward into inversion, while keeping your big toes planted on the ground. Picture an upside down windshield wiper on your car, and you're trying to reach each edge of the windshield.  You're trying to create a twist in the foot from the forefoot to the heel, and then untwist. Don't let your weight shift way out to the outsides of your feet, that's cheating the exercise. You should be able to build up to about 3 sets of 30 of these daily. They should not make you very sore but will probably be challenging at first, especially if your mobility is limited. 
* **Strengthen your plantar flexor muscles**
   * This is super straight forward. You need to be doing bent knee calf raises. Your soleus muscle is basically a direct extension of your foot muscles, and supports everything they do. It's one of the most important muscles to being able to run. Bent knee calf raises are one of the best ways to strengthen them,  You can do them while sitting, or from a semi squat while holding a wall. The most important thing is that you load them appropriately with heavy weight. Your soleus is supposed to momentarily support 2-3 times your bodyweight with each step while running. If you settle for bodyweight calf raises, you're not doing enough to prepare for running. You can start with bodyweight if it's all you can do without significant pain, but you need to gradually build up to single leg, and then weighted calf raises, all with a bent knee. Build up to about 3x20 single leg bent knee calf raises before moving to the weighted calf raises. A little pain while doing these is okay, but no more than a 3 out of 10. If you're having a lot of pain, try the heel rainbows first, right before doing the calf raises, so that your foot knows what motion to follow, when doing the calf raises, you want the rigid lever, not the soft foot. 
* **Take load off of your plantar flexors**
   * The best way to offload your plantar flexors is to shift that load somewhere else in your body, like your glutes. If your hip flexors and quads are tight and restricted, a lot of the strength to push off in your stride will come from your foot and calves instead of from your hips. Most people have restricted hips, especially if you spend most of the day sitting. Give some of these a try and see if any of them hit a spot that feels really tight and restricted, and then do at least one of them daily for at least 2-3 minutes per side: [https://www.youtube.com/watch?v=O7uXc-2Bpuk](https://www.youtube.com/watch?v=O7uXc-2Bpuk) 
* **Go for walks**
   * You have to walk before you can run. Once you have maybe a week of strength and mobility under your belt, you need to get walking. Think of it the same way you think of your running progression. Your step count is your "mileage", and you want to build up slowly and based on what you can manage with pain and fatigue. The goal is to build yourself back up to a normal level of activity in a controlled manner. Try to break it into multiple walks as well. 3x 15 minute walks is better than a 45 minute walk. Try to walk in a shoe that mimics barefoot movement for these walks. So a flexible sole, wide toe box, not too much arch support or anything like that. You're trying to build strength in your feet, so if you put a big cushy shoe on with lots of support, you won't really be accomplishing the objective. You should also try to walk around the house barefoot. Just remember your step count. If all you can do is 100 steps barefoot at first, then you have to put a shoe on, that's okay. But try to keep building on that. 

In summary, you should be able to knock this out, it shouldn't take months and months, and it shouldn't mysteriously come and go like some kind of phantom visitor. As you get proper movement back in your calcaneus and strength in your soleus, you should start to feel better very rapidly, at least to where you can walk short distances barefoot. Let me know if you have any questions.
[k74cvxc] (score 24, diepte 0) I've gone through 3 bouts in my life, and 2 bouts in the last year as I've gotten back into training.  I'm currently running 110 mpw pain free (knock on wood).

When I have it, I do eccentric heel drops from a slightly raised surface for 10-20 reps as many times per day as I can. Every time I walk past my fireplace I do it.

In addition, I do hot/cold therapy; hot bath with an ice bucket next to it and I rotate every 2-3 minutes. 

Finally, I do a ton of massaging of my calf muscle with the R8 roller and the stick and I stretch out my Achilles as much as possible.

Hang in there, it does get better!
[k74d6tz] (score 22, diepte 2) Don’t fully stop running, it won’t go away on its own. Believe me I took a full year off and it didn’t help. You need to run a little bit. Go see a sports PT, preferably one where they record and analyze your running form. You may have bad form or some deficiency and they will give you exercises to fix it. 

Again, don’t stop fully running, just run as much as you can without it getting worse, so that’s a lot of trial and error. For me it was 3 mile runs, no more than 3-4 times a week. 

After two years, it’s still there unfortunately. It comes and goes but not running did not make it go away.
[k742tg6] (score 13, diepte 0) Have you seen a physical therapist? Plantar fasciatus can be really persistent and debilitating, as you know, and the only people I know who have recovered from it religiously stuck to a prescribed foot/ankle/leg strengthening regime for several months. It's not something I've seen folks recover from just with inserts or better shoes.
[k743gaw] (score 12, diepte 1 OP) I've been in PT for 6 weeks and I haven't missed a single day of doing my home exercises. I'm doing everything I possibly can to recover and I really want to hear from people who have made a recovery to help keep me optimistic.
[k746u29] (score 11, diepte 0) I was sidelined for a full year with PF.  Every injury is different, but here's what eventually worked for me:

* [Strassburg sock](https://amzn.to/3Qf5E0p)
* Hoka Bondis
* *Easy* running & active recovery

What did not work:

* REST!
* Stretching 
* Heel lifts and other muscle work targeting the area directly
* Scraping/massaging/rolling/smashing/deep tissue stuff

The list of things that did not work is important, because these are some of the very common recommendations for PF - but in my case, I felt like they exacerbated the problem.

If I got it again, I would also try muscle work in the hips and knees - I've become a lot more aware over time that there's truth to the idea of injuries not coming from where you think they are.  That's part of why I think rest does not work - it does nothing to strengthen or fix the problem.

It sucks, but you will get through it!
[k74276s] (score 9, diepte 1 OP) Thanks for your response. At first I was running, just less, and it would often loosen up mid run. After taking many weeks off from running and seemingly not feeling any better, it's pretty tempting to just start running again and see what happens.
[k74wpf3] (score 9, diepte 2) Sample size of 1, I was given clearance from a sports podiatrist to run full volume (50+ MPW) while ultra training with PF. For me, it was liberal calf massages before running, after running, and through the day and wearing a supportive boot when around the house or sleeping. Eventually fully healed.
[k7438zb] (score 7, diepte 0) A few really basic things helped me:

- Using a theragun on the arch of the foot (not the heel) and rolling it with a bouncy ball 
- Alternating between rolling the arch of the foot with a frozen water bottle and resting it on a hot water bottle 
- Calf strengthening and stretching 

I was dealing with plantar fasciitis for a good six months and now have been pain free for over a year — good luck!!
[k744aqe] (score 7, diepte 0) I have literally just healed mine, which has bothered me for a year! What made the big difference was:
1. 4 weeks rest
2. Shock wave therapy (5 sessions one week apart)
3. Doing 15x3 one legged Calf raises every other day (with towel u der toes)

I'm surprised it worked as well as it has, now I'm slowly upping my training.
[k73zp76] (score 6, diepte 0) I only had mild-moderate PF but here is my advice:

1. [https://www.amazon.com/gp/product/B07C84LXVH/ref=ppx\_yo\_dt\_b\_search\_asin\_title?ie=UTF8&psc=1](https://www.amazon.com/gp/product/B07C84LXVH/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
2. make sure all of your non running shoes have great arch support such as Birkenstocks, Oofos, etc.
[k75eaeb] (score 5, diepte 1) I had an absolutely terrible bout of it in 2018 and recovered with inserts + better shoes, but I also religiously strength train. I was at the point of not being able to walk when getting out of bed. It was pure agony and reduced me to feeling nauseous on occasion. 

What was probably going on was that the exercises were helping but were not quite enough. The inserts tipped the balance. With those, I was pain free in two weeks and it has never returned. I run about 65 miles a week at my max.
[k75b6p1] (score 5, diepte 1) I’ll double up on calf raises. Slow on the eccentric/ down part.
Single leg if you can muster it, with support if needed.

I did firm over the counter orthotics, green Superfeet for a while. 

But the calf strengthening helped, rolling out on a lax ball too
[k74e2lj] (score 4, diepte 3 OP) I have been seeing a sports PT and they said my form was quite good (phew!) on a couple of steps here and there I was overstriding slightly and had a slight hip drop on one side, so we have been working on hip strength as part of my PT program. But overall my form was thankfully great.
[k749g08] (score 4, diepte 0) Had bad PF two years ago. Started doing calf raises on the stairs everyday, and it hasn't returned. Just me. Simple case, i guess.
[k74bykx] (score 4, diepte 0) My dad swears by plantar fasciitis inserts

He had it bad a few years ago, stopped running for a few months and started using insoles in his every day shoes. I guarantee you he never did any physio for it. Also maybe connected but he got different shoes (endorphin speed 2). Now he's been back running probably 20k a week. 

And for me when I had a flare up of plantar fasciitis once, it was 100% from running too far in a bad shoe.
[k756mso] (score 3, diepte 3 OP) This gives me some hope. How did running feel during that time? Did you have a tender spot on your heel and have to compensate for it in your stride?
[k749syf] (score 3, diepte 2) Keep doing the work!! You got this
[k74dxfw] (score 3, diepte 2) I know two folks who have recovered from debilitating pt through their exercise regime- for both it took longer than expected but it will happen- stay strong!
[k75sfgh] (score 3, diepte 2) highly recommend shockwave therapy!!! it completely cured mine while maintaining 100 mile weeks, and my dr said mine was one of the worst cases he’d ever seen. the scar tissue was > 2 std deviations thicker than what’s “normal” for pf

it was a bummer that insurance didn’t cover it, but I’d say it was worth every penny. good luck!
[k749ec6] (score 3, diepte 1 OP) Thanks so much. I have been too scared to try running in them yet but I picked up a pair of Hoka Bondis (because they seem to be super cushioned) and I have been wearing them when I have to walk around. Glad to know I'm on the right track there. I have been sleeping in a night splint too. 

I am definitely getting the sense that full rest is not specifically helping me, but on the flip side there was one day that (in my Hoka Bondis) I very gently walked for a couple of hours, and my feet felt horrible the next day.
[k74vspe] (score 3, diepte 1) My husband swears by the Strassburg sock.
[k74fks6] (score 3, diepte 0) My PF is finally starting to subside after 3 years.   I tried every thing.  Every foot/ankle/calf stretch, scraper, theragun, golf ball rolling, foot brace, recovery sandals, the works.  I was becoming resigned to the fact that my feet would always hurt.   

Then about a month ago, I was standing bare foot on my hardwood floor and I sort of splayed my toes out on the floor.  I flexed my toes backward against the hardwood, bending them as far back as I could and really focusing on all the toes other than the big toe.  I was actually just being lazy trying to pop my toes this way, but when I unflexed my toes, I felt relief in my heel.  So I did the other foot and, sure enough, it helped my heel pain.  So I started doing very deep toe stretches every day. And when running, I started focusing on making sure my toes were flexing on every stride.
 
I’m not 100% pain free yet, but I’m feeling so, so much better than I have since 2020.  Running is becoming so much more enjoyable again.  And I’m pretty sure it all boils down to the fact that I regained flexion in my toes.
[k7bn3jw] (score 3, diepte 1) Holy crap that was amazing
[k740hg1] (score 2, diepte 1) Did you wear the support running?
[k741tt9] (score 2, diepte 2) I wore it pretty much all the time (including sleeping).  I did wear it running as well although i think only some runs bc it gave me blisters on longer runs.
[k759hgi] (score 2, diepte 4) If you need to alter your stride, try to warm up more with calf massages or just walking until it’s not an issue. It was mildly uncomfortable but not painful running with
[k764hla] (score 2, diepte 2) My husband was diagnosed with plantar fasciitis after a bad running injury. He did the PT exercises religiously. He had shockwave therapy, cortisone injections, even immobilization in a walking boot for 6 weeks. Nothing worked. A different PT recommended a cushioned heel cup and no drop shoes. That was the only thing that worked!
[k78g48o] (score 2, diepte 2) Everyday for the bouncy ball, theragun and stretching. 

The frozen/hot water bottle I usually only did after a hard session when the pain was more intense. Hope that helps!
[k7489lv] (score 2, diepte 1 OP) Glad to hear you've made a recent recovery! I'll be sure to chat with my doctor about the shock wave therapy option
[k76dvkx] (score 2, diepte 3) Another vote for shockwave! I had a small tear, and shockwave got me back running after 4 sessions.
[k74avm6] (score 2, diepte 1) The towel under the toes is key. I’m convinced that kept my PF from flaring up
[k75trki] (score 2, diepte 3) It raises your big toe a little bit.   It apparently loads the plantar fascia more.
[k745ysb] (score 2, diepte 0) I think I'm almost there.

I over trained in the first half of the year. The most I'd run in a year was \~2600km and I got to 2300km by June. In my defence, everything was going great until I got a new model of shoes (same last though..) and that abruptly changed.

I shifted to cycling and kept up my volume then had a two week vacation full of walking. That and night splits has really reduced aching when I put weight on my feet after being off them for a bit.

Anecdotally, barbell squats give me a day or so of complete relief. No idea why.
[k7468dm] (score 2, diepte 0) Hi! I struggled with mild PT during Chicago marathon training last year, and it got pretty bad after the race in October. I did PT 2x/week (dropping down to 1x/week for my last month), easy running up to 4 miles only, and really focused on strength training 3x/week for three months. I rested for about a week after the marathon, then ran 20 mins max for the next month. Strength training was focused on PT exercises and lifting heavy to really build strength. I did not stop running but I did cut down volume significantly. I successfully PRed a half marathon in February and have not had pain since. I continue to strength train, and do PT exercises as warm ups for my run. I had a slight twinge during my marathon taper 2 weeks ago, but no pain since last December. I'd really suggest focusing on strength training as much as possible, with emphasis on feet, calves, and single leg exercises.
[k748y03] (score 2, diepte 1 OP) Thank you for sharing. I've been in PT for 6+ weeks. Everything I've read convinces me that sticking with PT is the most important thing I can be doing and the biggest thing that will move the needle.

Since you ran a lot while healing the injury I have a question about that. The tender spot on my heel related the PF seems to cause me to favor that foot on runs, even if my arches etc. are feeling good that day. And that's the main reason I've been avoiding running, because I don't feel like I'm striking the ground normally. Especially on downhills, which are bountiful around where I live and in my preferred sport (trail running). Did you experience anything like this? Do you have any advice?
[k749grd] (score 2, diepte 1 OP) Appreciate you sharing!
(126 reacties met lagere score weggelaten)

=== THREAD 68tb9p ===
SUBREDDIT: r/running
DATUM: 2017-05-02  SCORE: 379  REACTIES: 134
TITEL: Conclusions from 150+ studies on arch support - Myths busted...
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dh18azu] (score 124, diepte 0 OP) Sorry for not bringing the key conclusion. Here it is: 

Buy shoes without arch support (neutral shoes), unless you've had a consultation with a physician or certified coach that suggests specific shoes or orthotics.
[dh1ojgq] (score 65, diepte 0) I've worked in Running Specialty for 5+ years and have run for 15+, studied exercise science, and have personally dealt with nearly every running injury at some point - there is SO MUCH BAD INFO out there. This article is pretty decent actually, but there are exceptions to everything and there are a lot of things out there that are widely generalized. Here are a list of rules/facts that I tell people when it comes to running shoes:

1. No shoe will ever solve all your problems.
2. Just because a shoe works great for a friend, that does NOT mean it will work the same for you (and it probably won't).
3. Get fit for running shoes by someone knowledgeable. Find a highly reputable run specialty store (most good run specialty stores do not pay their employees commission).
4. Finding the perfect running shoe can be a long, trial-and-error process.
5. Most online guides about finding the proper running shoe are not accurate and/or are easily misinterpreted.
6. BUILDING STRENGTH IS THE MOST EFFECTIVE AND IMPORTANT PART OF RUNNING INJURY-FREE.

If you take nothing else away from this, at least recognize #1 and #6. I've fit thousands of people for running/walking shoes and the number one factor I've seen in people dealing with injuries is a failure to prepare their bodies for the strain of running. Too many people think they can just throw on a pair of shoes and go out and run until they are tired every time with no repercussions because "it's just running".

Many people hear words like "support","stability", and "cushion" and just assume that these are all good things, not realizing that these have specific meanings when it comes to shoe technology. Quite frankly, most people do NOT need the Brooks Beast/Ariel (though it is fantastic for some people), but sooo many people end up in that shoe because they see/hear the words "most stable" and "most cushioned". The same could be said for barefoot shoes - someone reads some over-hyped book or article that gets them hot on the idea, and then they end up injured after switching over to barefoot shoes for all their mileage. They certainly work for a small percentage of highly efficient runners, but most of us are not.

MOST running specialty stores are NOT trying to upsell you. I've worked in several stores and have never worked on commission. For me and everyone I've worked with, all we truly want are happy and healthy customers because we have nothing to gain from upselling and we'd rather hear about your successes than deal with angry customers. There are definitely stores out there that do work on commission and/or do try to upsell people, but in my experience, most run specialty stores usually do not, particularly if they are locally-owned. 

Additionally, rotating two pairs of shoes DOES help a bit because it literally gives more time for the foam in shoes to decompress after your last run, but usually only if your doing a decent amount of mileage and running everyday (or almost), and it's far from necessary. It's the same reason that it's better to not wear the shoes you run in all day, everyday. I've read studies on this topic that supported this but it was years ago and I can't find them now...if you require verified sources (generally a good practice), just ignore me and do whatever you find works best for you.

NOTE: If/when you get fit for shoes at a run specialty store - BE PREPARED TO TAKE YOUR SHOES/SOCKS OFF AND TO JOG SHORT DISTANCES IN FRONT OF PEOPLE. Everyone does it. It's the best way to figure out what shoes to recommend for you specifically. You are only limiting yourself if you are unwilling to do it. I can 100% guarantee I've seen grosser, smellier feet than yours. DON'T BE EMBARRASSED - I once fit an old man with 6 toes, ingrown toenails, and brutal bunions. Nothing is a surprise anymore.

In my experience, the runners that seem most resistant to injuries are those that are already very athletic. This may seem obvious, but it's not. This is because their core, hips, back, lateral stabilizing muscles, and lower leg muscles are already strong. Many people who take up running are doing it to lose weight/get back in shape - these people often do not have the strength of someone who, let's say, played collegiate soccer and decided to take up running afterward. In age where desk jobs are the norm, most of us do not fit into this category.

For people just starting out - running should only be one tool in your toolbox to getting back in shape. A consistent, balanced gym routine with healthy stretching/flexibility sections is going to be your best friend. Supplementing your running with other activities is vital. Your shoes will not make you a better runner, and sometimes even running more mileage won't make you a better running. In weightlifting, you wouldn't (or shouldn't) try to hit your highest bench press by simply maxing out everyday at the gym, nor should you expect to bench press 300 lbs your first time at the gym. You have to build up slowly, train other stabilizing muscles - running is the same.

Even if you've been running frequently but find yourself consistently injured and all you've tried changing is your shoes, then you probably have biomechanical weaknesses that need to be addressed. A specific shoe or orthotic might help a little bit, but you have do your maintenance work or you can't expect to get better. People don't like this idea though because it is easier to buy something than to spend even 15-20 min EVERYDAY working on strength and flexibility to fix the real problem. If a doctor/PT/chiro gives you exercises  - DO YOUR DAMN EXERCISES.

EDIT: One more note - if you take the time to get fit at a run specialty store, especially if you try on several options, please at least buy something if you can, even if it's not the shoes. I totally understand that money can be short and shoes can be expensive for many (trust me, I do this job and another on the side to barely be able to afford cost-of-living and grad school), but if we take the time to fit you and then you ask to take a picture of the shoes with your phone and leave with nothing, you're not fooling us. We know you're going to buy something online. It happens, I get it, but it does kinda suck for us - just be respectful of our time, especially if there are other customers in the store. We sell shoes at the standard shelf price - if you can find them cheaper, it's probably because they aren't the same exact shoe you tried on or it's coming from a company with way more purchasing power than a locally-owned store.
[dh14sze] (score 53, diepte 0) Now this is exactly the kind of article I'll read from start to finish! Quality content vitkarunner!
[dh1ve1j] (score 41, diepte 2) No, they're salespeople, so their bias is towards recommending you purchase one of their products. Only use arch supports if you're suffering an injury. As it says in the article, it's like wearing a wrist brace when there's nothing wrong with your wrist. All it does is inhibit the natural movement, impeding its ability to strengthen muscles and ligaments naturally.  
I wish these companies would be be held accountable for selling these products under false pretences. The amount of injuries they've caused just so they can sell their new product..
[dh14hr1] (score 28, diepte 0) I am an extreme supinator with high arches.  I found minimalist (or no) shoes to be the most uncomfortable, but I also find motion control and heavy support shoes to be extremely uncomfortable.  What's been best for me is shoes with a ton of padding and none of the motion control. 

I think my anecdotal evidence loosely aligns with the results of the study.  Padding and support won't make you less injury prone or a better runner, but it can certainly reduce discomfort.
[dh13b8k] (score 25, diepte 0) My experience is that arch support is the most painful shoe feature ever invented. I have arches slightly on the high side of normal and find it excruciatingly painful to run in shoes with arch support. Who on earth thought it was a good idea to force runners to bear weight through the middle of their arch by filling in the natural space there with padding? After experiencing chronic arch pain for two years, I switched to running in tough socks or sandals instead of traditional running shoes (all of which have some degree of arch support) and the pain is completely gone.
[dh1h5rm] (score 18, diepte 1) Guys read it. Don't just come comment on a title of a link. Not once does the article say that arch support is 100% bad. It's mostly discussing overuse.
[dh15gc0] (score 16, diepte 2) Good!

No, in all honesty this is a great submission. The only thing lacking is that OP didn't flair it (but I took care of that).
[dh15cmx] (score 15, diepte 1) I can no longer tell whether this is sarcasm or not...
[dh1bcu7] (score 13, diepte 4) The biggest fault with reddit (IMO) is that you can't include a body on a link post.

Sure, you could make a text post with the link in it, but I feel like having the ability to click straight through from the front page is nice, but then being able to attach a summary to it so that way when shit gets crowded your comment summary doesn't get buried.
[dh1fxzp] (score 12, diepte 1) These articles always seem to gloss over us supinators. I guess pronation is more common, but it's weird how they'll state a conclusion about supinators without actually discussing it.

I too don't specifically look for "arch support " (I have high arches), but definitely prefer a padded shoe.
[dh1tfma] (score 12, diepte 1) Sorry for the stupid question, but do the people who work at pro running shops count? I've gone to two separate shops where they analyzed my running form, including one where they recorded my foot motions on a treadmill, and both have suggested that I use support shoes (don't remember if I was overpronating or underpronating). I can't tell if the support shoes made any difference.
[dh15dsk] (score 10, diepte 2) Skinners. They're socks with rubbery stuff on the bottom. My longest so far is about 8 miles.
[dh145xg] (score 10, diepte 0) Me gusta :)
[dh1f0uu] (score 9, diepte 7) At first, I pictured you running in something like [this](http://i.imgur.com/EI74lxX.jpg) but I didn't realize that there was actual running sandals like [these](http://i.imgur.com/6TjG01S.png).
[dh15xzt] (score 8, diepte 5) Are you telling me people downvote out of spite? I do not believe this one bit! No siree!
[dh20l2h] (score 8, diepte 3) I agree wholeheartedly. Part of the reason why I stopped working at one of these joints is because of how much we were pressured to push things on people that they didn't need. It really seems to go against the "were here to help people" mantra that the higher-ups would try to feed us.
[dh19hz8] (score 8, diepte 0) Arch supportive shoes is what took me from pain at mile 4 to no pain at mile 10. *shrug*
[dh19rht] (score 8, diepte 0) Worked in a running store for 2 years... I just learned so much from this article
[dh1cctf] (score 8, diepte 0) I can only speak for myself, but as an extreme pronator, I believe I wouldn't be running today without my Superfeet inserts and motion control Brooks Beast shoes. I had a gait video made before and after and the difference in the twisting of my lower leg, and thus my knee joint, is just night and day. It made perfect sense that those parts that were twisting were the ones that kept getting injured. And now they haven't in 10 years.

Maybe I'm the outlier, but you couldn't convince me to ever go back.
[dh1int1] (score 8, diepte 0) My PT pushed me to get stability shoes and wear them all the time.  That, exercises, and stretches helped reduce knee pain while running.  [My doctor had showed how my pronation caused a misalignment in my knee, resulting in pain.]

My wife hates running, but wanted to try.  She went to the store and they recommended stability shoes too.  She ran about 1 mile before stopping due to knee pain.  She returned the shoes and took 3 weeks to recover.

So, yeah, you probably shouldn't run in stability shoes just because you think you're supposed to.
[dh1qcgi] (score 8, diepte 1) Exactly! Every chronic injury I've ever had was only worked through with strengthening and stretching exercises. It wasn't about the shoes--it was about my weak glutes/tight hip flexor, whatever.
[dh161hf] (score 7, diepte 3) A quality discussion-generation or summation comment to go with the article would have helped it look less like spam.
[dh14v7u] (score 6, diepte 1) You run in socks? How far?
[dh2f8d8] (score 6, diepte 1) Your wife probably has some crazy form issues if a mile caused her severe pain
[dh1ef6y] (score 5, diepte 6) Not sure what that means. They're basically just flat shoe inserts covered in ductape, with old shoelaces for the straps. World's most comfortable running shoes. Probably not very durable, so I try to keep them just for running.
[dh1e84e] (score 5, diepte 2) I discovered I liked running barefoot after I bought a pair of shoes (on the advice of the owner of my local running store) with huge arch supports, wore them to the gym, and was in so much pain after 2 miles on the treadmill I took them off and finished the run barefoot. Returned the shoes, started looking into ways to run "barefoot" while protecting against glass, stones, etc.
[dh15yql] (score 5, diepte 6) Downvoted!
[dh1ibg7] (score 5, diepte 0) After years of buying custom insoles (I have crazy high arches that even surprise the shoe salesmen) I took r/running advice and ditched them and worked on foot strength. Never going back to insoles. Thanks team!
[dh1m88c] (score 5, diepte 0) My main takeaways for next time I'm shopping or helping someone out:

- Arch type doesn't matter

- Avoid super soft cushioned shoes, they wind up increasing the stress on your body

- Unless you have had injury issues, have a diagnosed foot issue, and/or have had a gait analysis done that pointed out serious issues in your natural running form, you probably should just get a neutral shoe. 

Obviously, like many runners, I defer to an expert when buying running shoes, and go to a knowledgeable running-focused store to get good advice, but these all seem like good points to keep in mind whenever you're looking at shoes. It's nice that someone compiled all of this information into one simple document.
[dh27kv4] (score 5, diepte 1) > MOST running specialty stores are NOT trying to upsell you.

Great info otherwise, but I'm going to disagree with this one little piece. Unless you meant "MOST running specialty stores are not TRYING to upsell you".

They might be very well meaning and not encouraged to upsell explicitly ... but they work as sales people in a business. There is no avoiding the environment you are in and the behavioral biases present. That's just how humans will act when their role is a salesperson. It's a nitpick obviously but buyers should be aware that it's not just dishonest people who upsell, it's unavoidable for anyone in that position.
[dh1kvlc] (score 4, diepte 8) I learnt so much from your conversation. Still can't ​imagine running in those though
[dh2f4vg] (score 4, diepte 2) Just to add some fuel, I've been to several pro running stores, and they never recommended the "correct" brand of shoes for me. After spending time with a *fantastic* pt, I picked up some altras, which fit my foot really well.

"Pros" were putting me in brooks, nikes, rebooks, and asics, all of which were over $100 and didn't fix my issues. None of them recommended any different lacing strategies either, which just baffles my mind.

All of these stores offered great return policies, one even let me send them back after 3 months. 

That being said, I have a very weird foot which was an irregular problem. I think you should go into a specialty running store with the mindset that these people generally know alot more about running shoes than the average person, but at the end of the day you're ultimately responsible for what you buy. -
[dh1dqne] (score 4, diepte 1) The check or x are basically saying whether or not the science supports the overall claims being evaluated in one aspect.  The sentence that follows describes the finding.  So "Foot pronation is not linked to increased injury risk" is the finding, and it's an X because claims that arch support to offset injuries due to over-pronation are not supported by the science.
[dh1cwws] (score 3, diepte 3) How long does a pair last you? Looks like they are still on IndieGoGo... have they not launched?
[dh1e135] (score 3, diepte 4) Yeah, they've launched, but the backlog of orders means delivery takes ages - about three months in my case.

I don't know how long they'll last as I only got them a month ago. The coating on the ball of the foot wore down to a smooth surface almost immediately, but they haven't changed much in appearance since. I've been wearing them as everyday shoes and for running on cold/overcast days. On hot days I prefer to wear sandals to run.
[dh19szx] (score 3, diepte 1) Before there were options available, I modified my shoes to make them archless. I removed the stock insole and cut out the arch and put it back in. Then took a flat Spenco insole and put it in on top of that. It worked pretty well.
[dh1b1nd] (score 3, diepte 1) After almost 2 years of trying to cure plantar fasciitis on my own (and avoiding arch support after reading posts like this one) I finally sucked it up and went to a podiatrist. First thing they did was give me orthotics. I have very high arches, and it took me *weeks* to get used to the damn things. The ones I've got now are generic, they want me to get custom ones.

Anyway, it felt awful in them at first but I have to say I did get used to it and now it feels weird when I don't have them :/ I dunno. I tried going without, gonna give this a try for now. I've also been dry needled twice so far and just got a night splint too.

For a condition that most people say clears up within 6 months regardless of what you do to treat it, this has been extremely frustrating :/
[dh1o07b] (score 3, diepte 2) My mother had chronic PF. Turns out she has heel spurs. Might want to check that route of you haven't.
[dh283vf] (score 3, diepte 5) Haha, I love my Birkenstock. My husband teases me when I think about getting another pair. I guess the shoes + Subaru might mislead others about my sexuality, lol.

I wouldn't mind getting another set if they still sold something like the Maine shoe. The soles are so comfortable.
[dh1ocsn] (score 3, diepte 1) I have very low arches, and I also find running in shoes with arch support to be very painful. Plus the arch blisters! It took me several years of "trusting" the running shoe people who were putting me in stability shoes that ultimately hurt my feet to branch out on my own and buy a pair of neutral shoes. I had no idea until that point that it wasn't normal for my feet to ache for the entire run.
[dh14roq] (score 3, diepte 1) Isn't this a beautiful link!? Holy moly!
[dh1as85] (score 3, diepte 1) Agreed. Honestly to each his own. If high arch feels comfortable just buy it. Didn't cost considerably more....  Especially if you shop the bargain bin.
[dh15nio] (score 3, diepte 3) OK, that's what I thought, and then I saw "67% upvoted" and couldn't decide whether I had lost my mind or what.
[dh15s2l] (score 3, diepte 4) My guess is that due to recent events, there are people hitting downvotes willy-nilly and not paying attention.
(89 reacties met lagere score weggelaten)

=== THREAD kdzaxp ===
SUBREDDIT: r/AdvancedRunning
DATUM: 2020-12-16  SCORE: 93  REACTIES: 115
TITEL: What worked for you to treat your plantar fasciitis? Advice appreciated!
POST (source_id=post):
This is a first for me and I’m having trouble treating it. I was in denial about it for awhile and running through the pain, but I need to resolve this. I see a guy that specializes in myofascial release and he’s helped relieve a lot of the pain, but I can’t seem to get over the hump.

I’ve been doing towel stretches, calf raises, rolling with a lacrosse and golf ball, some light scraping, etc. I’m on week 2 of complete rest. Any insight on what personally worked for you would be very much appreciated!

Edit: Wow! I really appreciate all this feedback. Looks like some actual rest will do me some good, and gonna add some of these suggestions into my routine. Thank you!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gfzilrl] (score 34, diepte 0) For me the first time, it just took a lot of time. And I put a gel insert in my work shoes. Dunno if it helped but it was def the work shoes that gave me the PF in the first place. I’ve also been extremely careful about wearing sensible work shoes ever since. 

At the beginning of covid, I was home all day and treated my anxiety with a lot of elaborate cooking that I was going barefoot on concrete floors. Light PF struck both feet but this time I knew what it was and immediately started wearing crocs at home at all times. It went away in a relatively speedy 2-3 weeks. Now I can tolerate wandering around the house barefoot but am careful to not spend hours cooking barefoot.
[gfzi39x] (score 28, diepte 0) Rest. Ice. And rolling it out on one of those special pokey PF balls
[gfzi7p5] (score 27, diepte 0) Friends swear by the strassburg sock. I've mostly just managed mine by tossing old shoes and avoiding too much beach running.
[gfzmyhk] (score 27, diepte 0) This is what worked for me. I belive that foot strength is important, so anytime i’m at home I’m walking around barefoot to strengthen my feet. Now others swear by the exact opposite to this method, so always take advice with a grain of salt and listen to your body. I take off my running shoes immediately after the run is over and try to get some easy barefoot strides in the grass once or twice a week (not realistic in the winter if its cold, of course!). This works for prevention for me, but if your case is quite serious, rest is key.
[gfzo4r7] (score 18, diepte 0) I've suffered PF for years but magically went away when I started running with minimalist shoes. I don't think it's a coincidence.
[gfziqlt] (score 15, diepte 0) picking up marbles with my toes & scrunching a towel up with my toes helped. also new shoes, as well as focusing on speed/short distances (& low mileage) for a while. it was frustratingly slow but worth it
[gfzvqha] (score 15, diepte 1) Same. And instead of calf raises, heel drops over a step. 3x a day. 15 reps per foot. Works magic for PF and Achilles tendinitis
[gfzm7h9] (score 12, diepte 1) Cooking barefoot on hard floors is brutal, restaurant kitchens have mats they make the floor really squishy just for that reason
[gfzp7mo] (score 11, diepte 1) The socks work but they definitely take a bit of getting used to when planning to sleep in them. 

I always make sure to throw them on when I start having issues
[gfzoi0k] (score 10, diepte 1) If you don’t have one, a lacrosse ball can work too. Occasionally I’ve cup or roll out with a frozen water bottle
[gg00rfl] (score 9, diepte 2) This response thread knows what's up. Plantar fasciitis would more appropriately be called plantar fasciosis. Cell death. Cuz it ain't really inflammation. If the foot muscles were ctually used instead of sat on a bed of support, maybe it would work right and not degenerate.

 Problem is for most people with plantar fasciitis, they can't jump into it. Got to do the strengthening exercises first until the pain is gone. Then they should slowly work their way to minimalist shoes, I would recommend something with a low heel to toe drop and a wide toe box. Then, Altras which are zero drop, then go down to minimalist shoes. Should take months though to get there. In the meantime, cycle through using up your old shoes. I would recommend buying correcttoes toe spreaders also. The big toe being pushed towards the inside as it is in most shoes is stretching the abductor hallucis which is causing loss of blood flow to plantar fascia which means less cell regeneration
[gfzlfnz] (score 8, diepte 0) Rolling my calves with The Stick
[gfznt68] (score 8, diepte 0) Strasburg sock (or similar) every night.

I hated using a lax/golf ball but loved using the little trigger point mobi point massage ball.  It’s rubber and has little nubs so it doesn’t slip out from under your foot and roll away. It’s like $8, just get it.

In addition to massaging and strengthening, don’t forget flexibility!!! Draw small circles, by pointing your big toe. gradually expanding to bigger circles, or draw various shapes and letters.

I am not sure if this is legit but I think taking hot water epsom salt foot baths helped me a lot.  I filled up one of those little plastic shoe storage things with very hot water and epsom salt (usually had to wait a couple mins for the water to be cool, the point being it had to be very hot, as hot as I could tolerate, so it would last the longest amount of time) and kept a kettle of hot water on the table and added it to the bin little by little as the minutes passed by to keep it very hot.  Be very careful, I almost burned myself a couple times, but I found this helped my foot relax.  Perhaps I shoulda gotten some sort of heated foot bath...

I bought power step inserts for my casual/work shoes, and wore Birkenstock’s around the house.

Don’t be afraid to take enough rest until you can run safely without pain.  I know it will suck if it takes a while but I promise it will be worth it.
[gfzj713] (score 7, diepte 0) yeah for me it was rolling with a ball/frozen water bottle, strassburg sock and taking a lot of time off.  I think it took me 3 months to heal.  I have since moved to wide toe boxed shoes(altra) and my problem has never returned.  Although I don't know if that is what actually prevented my problem.
[gg0h228] (score 7, diepte 1) Piggybacking off this, some barefoot drills really worked for me as well. Here's what I did:

- Walked around barefoot at home, as you said.
- Took a very good amount of rest from running.
- When I did start again, I did two weeks of only short (at most 5k) runs in bare feet, on grass, with lots of strides.
- After two weeks of that, slowly built up mileage in shoes on roads again, but I still try to do barefoot strides at least once a week.

Worked a charm.
[gg0415q] (score 6, diepte 0) The quickest way is deep massage. I highly recommend doing it yourself simply by standing on a pair of dumbbells (the hex design that don't roll) or something similar for 5 - 10 minutes, once or twice a day. After a couple minutes, try to get your whole body weight on there. It should go away in two or three days. It hurts, but that's why it works. Your muscles in the bottom of your feet need to be lengthened. Simple stretching won't do it, and rolling a bottle doesn't get deep enough.
[gfzjaem] (score 5, diepte 0) Stretching the muscles that run under my feet into my calf from my toes.  Basically doing a standard calf stretch with either my big toe against the wall or my little toes.
[gg052mp] (score 5, diepte 1) Mine kept reoccurring after going away. Turns out I just had really tight calves and a little stretching solved it pretty quick. Haven’t had a problem for 2 years now
[gg0ssyk] (score 5, diepte 3) OP needs to check this out, this is the sauce. /u/not_alemur 

I had PF pain for about 6 months before stumbling upon [this video](https://www.youtube.com/watch?v=tNPfbB2sX5Q&). Before this I was stretching, resting, icing, massaging, strengthening - all throughout I didn't notice much of a difference in reduction of pain. I've been wearing the toe spacers for 2 months now and my pain is completely gone.

 It sounds like a Paid Program success story you'd see on TV, but it's the truth and I'm a firm believer in the restorative toe/foot philosophy as a way to treat foot pain. It's absolutely worth a shot, OP, especially if nothing else has worked.
[gfzpij9] (score 5, diepte 0) I went to a physio who preached FRC. I had to work on toe, ankle, knee and hip mobility. I didn’t realize how little range I had through that whole chain. Working on all of it worked things out so far.
[gfzproo] (score 5, diepte 0) Physiotherapist. She gave me very painful massage but guess what! It works!
[gg03gyp] (score 4, diepte 1) Got PF after moving to an apartment with concrete floors as well. Might get some crocs...
[gfzw1sc] (score 4, diepte 1) Why is this getting downvoted? Just because not everyone does it this way? Ridiculous.

I had terrible plantar fasciitis. Stretching my calves frequently and arch support in my shoes has done wonders. I  rarely have pain anymore - and I put in some heavy miles.
[gfzr7fh] (score 4, diepte 0) Stretching my calves. Wearing shoes with good arch support. (Not just running shoes all my shoes have to have arch support or I flare up). I slept in a night splint when it was severe in both feet.
[gg0j662] (score 4, diepte 0) A physio told me he saw a huge increase in PF cases a few years back, he put it down to the barefoot style trainer craze and timber floors. He recommended Birkenstocks for around the house as they have nice, moulded cork soles.

It took me about 18 months to get over my PF. Daily ankle mobility (trace the alphabet with your toes) and rolling on a hard ball to break down the scar tissue seemed to do the trick.
[gfzicc9] (score 3, diepte 0) Acquiring improved function in the big toe along these lines this helped me a lot:
https://www.youtube.com/watch?v=kcC2ZzJIEPw
[gg0l9q4] (score 3, diepte 1) This is exactly what worked for me after all the traditional ways did nothing. I was not a ‘barefoot’ guy but Now I’m barefoot around the house as much as possible. All my casual shoes and work shoes are ‘barefoot’ style. I do run in regular shoes (NB 1080) though. My PF went away and I’ve had no feet problems since
[gg1cjnq] (score 3, diepte 3) With the obvious caveat that this is just another anecdote, my "shin splints" stopped recurring after switching to Altras. I also rested, rolled out, and was slow about restoring volume so that my legs could adjust to the drop. It could just be that my legs eventually got stronger, but I suspect it's significant that I haven't had an issue with shin splints since switching to zero-drop.
[gfzocfp] (score 3, diepte 0) I had a terrible case of it once. I tried to run through it at first, reduced mileage, Strassburg sock, etc. Nothing worked except getting off of it and letting it heal completely. It took a long time. I think it was about 6 weeks, but once it healed, it never came back.
[gfzrz8x] (score 3, diepte 0) Lacrosse ball.
Switched to a more stable running shoe (Brooks Adren. 20)
Some various stretches provided by a PT.
[gfzsa0q] (score 3, diepte 0) Yoga did it for me. You go to downward facing dog many times through the sessions and you get to stretch the back of your legs through the bottom of your feet. My heel no longer hurts to the touch.
[gfzwgql] (score 3, diepte 0) Time and weight loss
[gfzy563] (score 3, diepte 0) Toe elevated heel raises with a towel. http://www.michaeljlord.com/blog/2017/4/1/an-unconventional-way-to-treat-plantar-fasciitis
[gg01urz] (score 3, diepte 0) Stretch your calves, and stretch your hammies/glutes.  The whole thing is connected from top to bottom
[gg0li5z] (score 2, diepte 2) Any hard ball works, I use a hockey ball.  I had plantar fasciitis and then it resulted in a painful plantar fibroma.  Once I started rolling daily both went away in a few months.  I used a high arch insole while recovering so I could still run long distances.
[gg0he0s] (score 2, diepte 2) The socks were a game changer for me. I used to sleep with one on each foot up until I ruptured the left one because I wouldn’t rest after a hard marathon effort (learned my lesson). Wearing Strassburg socks allowed me to continue to train through it for years, as well as using “the stick” on my calves.
[gfzijiy] (score 2, diepte 0) Post run dynamic legs swings and weight lifting.
[gfzrxsh] (score 2, diepte 1) I have no idea why you're getting downvoted - those socks certainly won't fix plantar but they can make running a sight more comfortable
[gg0uqfz] (score 2, diepte 2) I know. It's the best thing to do, but for some reason, nobody knows.
[ghsxsl0] (score 2, diepte 2) Can I ask you what you recall that “very good amount of rest from running” being?
[ghtxyit] (score 2, diepte 4) Damn.  But thank you.
[gg13ieb] (score 2, diepte 2) I did it when my feet were up in the air, like hanging off the edge of the bed, for a fuller range of motion.
[hz0d9pl] (score 2, diepte 4) Did it hurt more when you first used the spacers? It seemed to aggravate mine i thought or could have been stretching in addition.  How long during the day did you wear them? Did you do any other stretches? And THANK YOU!
[hz3bulj] (score 2, diepte 6) This is do helpful I really appreciate it greatly!! When I was doing PF stretches it all got way worse (weird huh?) so have been resting and instead rolling out the knots  in my calves aggressively. This brought some relief. I will definitely look at the links for those exercises/stretches thank you!
[icl4dy1] (score 2, diepte 4) I know this is an old post but that’s pretty wild. Been dealing with this in my left foot.  My PCP thinks it’s inflammation but I don’t see podiatry until next month unfortunately. What this guy is saying makes a ton of sense about it being dead tissue.
[jbaqngq] (score 2, diepte 4) Boom. That was it! Thank you. That video and explanation is a game changer to tackle this issue.
[hzrbdz7] (score 2, diepte 3) Yup toe spacers worked for me.. a fkin miracle.

Been struggling with PF for about 3-4 months now and i've tried everything. Icing, massaging, stretching, strengthening, strassburg socks, night splints, anti-inflammatory diets and supplements and none of that ever yielded to any form of a consistent healing pattern. Sometimes icing, stretching, massaging and night splints made it worse. Wasn't until i read the comments here and saw the Correct Toes video recommended by u/sauceDinho.

Honestly i was pretty skeptical at first about the toe spacers but i was getting desperate so i bought the legit ones from the actual website instead of some knock off brand and got priority shipping. And then 3 days later, wearing them only at night, and sometimes during the day (I just pop em on at night and then put a loose sock over it to keep my toes from wriggling it off) i began to actually feel progress. It's been some time since then and now i feel like I can actually stretch and massage my foot without it aggravating anything. 

I'm a rock climber. So my shoes are basically tighter than tight and yup. It's proof that right as the pandemic calmed down and i restarted my gym membership, i also coincidentally sized a half size down on my shoes, i started getting PF bad. IMO this is definitive proof that it's toe misalignment that's causing all my problems. 

I can't speak for the off brand toe spacers but the ones offered by Correct Toes worked for me. They even have little holes in between the spacers between the pinky toes and the big toes so you can jam a little bit of paper or something to make them spread a bit more if you want. 

For me personally i felt that my pinky was the offending toe. (In a climbing shoe the pinky gets mashed up pretty bad)

Anyways, hope my story and/or my review of PF and toe spacers will help someone out there.
[gg13aej] (score 2, diepte 1) This one was it for me. Started with strengthening the core and loosening up the hips and associated muscles.
[gfzthdx] (score 2, diepte 0) Get night splint too,  30$ and it really helps
Looks that you are doing everything else
Stretching, foam rolling and the scraping.  if it does not hurt , you are not doing it correctly.   I had tears in my eyes the first few times my PT was doing it

Did running after 12 weeks and kept doing exercises after each run
[gfztmgy] (score 2, diepte 0) I had plantar fasciitis that would not go away with the special sock, icing, rest, or 4 Advil a day. What helped the most was purchasing Birkenstock sandals to wear indoors and wearing my just-retired running shoes everywhere, including work. Having the support on my arch and foot at all times was the only thing that accelerated my recovery. After I started putting something comfortable between me and the ground, the pain went away completely after a month. Surprisingly, I was able to continue running through this and I can wear normal shoes again (in small doses). I had PF for about 9 months and at its worst, I could barely touch my heel without feeling pain.
[gfzujqh] (score 2, diepte 0) Tried everything. Ultimately a chiropractor knocked it out. Basically deep massaged it twice a week for about a month along with Icing it daily/rest. Going on 6-7 years of no issues ever since.
[gfzw8gu] (score 2, diepte 0) PF dogged me for at least six months, and ruined a season of mine. I was able to deal with it via many of the means listed, but to truly get rid of it, I had a physical therapist use some kind of shocking tool tool on my heel to break up the tissue and stimulate healing. I had a few sessions over a month but it worked and I haven't had problems for seven years.
[gg08btc] (score 2, diepte 0) This is what worked for me. All advice came from a podiatrist after I could barely walk in the mornings. I was so happy that she didn't recommend anything fancy or expensive:

-stretch your calves every day. It's all interconnected down there and this helps keep the lower leg long, especially if you sit for work.(still do this every day!)

-firm but gentle lacrosse ball rolling. Easy for 15 mins a few times per day.(other firm rolling device could be subbed here but lacrosse was recommended due to size and firmness)

-a shoe insert with the bump in the middle of the foot. I was recommended one that was like 14 dollars and it worked great, the doc said no need for a custom or expensive one for non-exercise purposes.

-mix up your shoes for both exercise and daily wear.

-go barefoot when practical

-rest. And when you think it's gone. Rest a bit longer. It took a solid month to get up without acute pain. And another to not feel some discomfort after exercise.


Good luck! I didn't have a recurrence for like 2 years (stopped doing most of the above) and when it came back, just repeated the list above and now just do it as part of routine, but no longer wear the insert.
[gg09gwv] (score 2, diepte 0) I had it for months and couldn’t make it go away. So first lots of rest until the flare ups calm down. Second for me was moving/stretching my feet every morning before I put my feet on the floor. I read somewhere a tip from a ballerina to “write the alphabet in the air with your feet/toes every morning.” Some mornings I do that, some I just do light foot stretches and circles before standing up. This seems to have really helped me keep the PF at bay.
[gg0jxeu] (score 2, diepte 0) I walk barefoot all the time and I also don't let my heel touch the floor when running. Those things worked for me.
[gg0mvcr] (score 2, diepte 0) I switched to minimalist shoes and started fore-foot running. Haven’t had a problem since.
(96 reacties met lagere score weggelaten)

