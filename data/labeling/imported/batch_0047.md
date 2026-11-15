# Label-batch batch_0047

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
Schrijf het resultaat naar `batch_0047.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: bvrrl7, 5lt5sw, lfdtsk).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD bvrrl7 ===
SUBREDDIT: r/nursing
DATUM: 2019-06-02  SCORE: 966  REACTIES: 131
TITEL: When you schedule yourself for eight 12s in a row while you’re sitting with your feet up on your weekend off:
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[eps4nl8] (score 175, diepte 0) >eight 12s in a row

Is that legal where you are?
[eps9b3y] (score 122, diepte 0) Our hospital puts a limit on 4 12's in a row. Then you have to be off for 48hrs. I can't imagine functioning after more than 4 in a row.
[epsbxxk] (score 117, diepte 0) We have a nurse who will do 15 in a row and go on an insane vacation
[epscdcg] (score 95, diepte 1) I used to have a 7 on 7 off schedule, 7 nights in a row followed by a week off. I thought it sucked, but other people seemed to like it...
[eps9fek] (score 77, diepte 0) Weekend Nurse: Future Nurse will earn me some money!!
Future Nurse on day 8: F*@#  you Weekend Nurse
[epsga3d] (score 75, diepte 1 OP) Hello satan
[epsedpx] (score 68, diepte 0) We had a nurse who would do 12 12s in a row, on nights, every month and then fly home to Colorado (where he had wife and kids and shit) from California for ~16 days.
[epsghmu] (score 59, diepte 1) I can’t even fathom this. Are they actually a witch or something?
[ept00w5] (score 57, diepte 2) It’s a He and honestly it doesn’t seem to hurt how well he does. He’s an older, sassy gay dude and in my experience (I bartended at a gay resort), those dudes are like the energizer bunny
[epshnc4] (score 55, diepte 0) Not to be that guy, but to a lot of you in this thread: fucking why? Anything past 4 12s in a row is not only miserable, it’s unsafe, for both you and your patients. And if it’s not your own choice, then no job is worth doing that to yourself. Let’s stop the dick-measuring contest of who has worked the most 12s in a row.
[epsh9bl] (score 51, diepte 1) Jesus, I wish we had rules like that. I'm on a 13 day stretch oh 12 hour shifts and my next day off isn't for 2 more days. Send help
[epsbkvv] (score 50, diepte 1) I did 4 12s this week. 

It was not a good week.
[epsg1f3] (score 47, diepte 0) My set schedule is 6 12s, 2 days off, 6 12s, 15 days off. Love it.
[eps4tah] (score 45, diepte 1 OP) Yeah as long as you have 8 (maybe it’s 12 hours) between each shift. Not eight twelves consecutively
[epskwfm] (score 45, diepte 1) Plenty of RNs at Bay Area hospitals do this. Making 180k+ a year and commuting in from a different state that has a insanely low COL
[epsgvpc] (score 41, diepte 2) It's just a more extreme version of 12s vs 8s.  Some people swear by the extra days off, but i like my mornings/evenings free.
[epsdm0v] (score 34, diepte 1) I've worked 7 consecutive 12 hour shifts, legally. What helps me get through the work week is taking each day, one by one, and I have adequate mental facilties at the end of the work week.
[epslej1] (score 30, diepte 2) I will send you a power wheelchair.
[epspnwe] (score 29, diepte 1) The most I’ve done is 6. And management didn’t bat an eye because I misread the schedule and picked up some shifts when I thought it was just the middle of my week off. I’m an idiot.

I had a coworker who’s set schedule was thurs-tues nights, then 8 days off. She was older, single, house and car paid off, her only expenses were utilities and insurance and groceries. At least once a month, she takes that 8 days off and goes to another country, or at least somewhere in the states *very* far away, usually Alaska or Hawaii if she’s staying in the country.

Her life is amazing. But she works her ass off for it.
[epsr1l6] (score 29, diepte 3) Ehh, for half the month they also got to have their dad free from any work distractions
[epsmfaw] (score 29, diepte 3) They rent a room somewhere.  Several nurses I know go in on a single room together in a house and plan their schedules so they miss one another.  Another couple has an RV they drive down from Napa.
[epsja3c] (score 24, diepte 1) Goals.
[ept4vng] (score 23, diepte 3) Sorry I didn’t mean to make the assumption that “nurse” meant “she”, thank you for correcting me. I start crapping out mentally/emotionally after 2-3 day shifts... but I’m severely introverted and work on a high stress floor. Some people can just do this and remain unaffected. I used to be able to at a different job that had less intense charting standards (yet more patients)... I could easily do 4 on/1 off/4 on with a 45 min commute.
[epsmwg4] (score 23, diepte 1) I'm currently almost done with day 1 of 14. I work at two different facilities and also have no real responsibilities except for myself. Honestly, working between the two facilities feels like having a fresh start from being off. I work 3 days at one facility, then 3 days at the other, back to this facility for 3 days, 1 day at the other, 2 days back here than finish the rest of the week at the other. I never work one facility more than 4 days in a row, I always get to leave and go home to get a nice meal and then sleep for a solid 8-9 hours, then go back.

Not trying to outdo anyone or anything, just have a full-time job at this facility and contingent at the other facility which is offering critical staffing. Super hard to pass up $63 an hour as a contingent critical shift in southeast Michigan when my normal hourly rate is $30 an hour.
[eptkf2p] (score 21, diepte 3) >older, sassy gay dude and in my experience (I bartended at a gay resort), those dudes are like the energizer bunny

It's because by day three our blood is more iced coffee than PRBCs.
[epszsw8] (score 20, diepte 1) Is she a “good nurse” when she does this though? Like does she make a lot of mistakes, is she still able to provide compassion, etc?
[epsq9un] (score 17, diepte 2) Personally I like 12s, especially if I'm commuting.

Some senior nurses have reported to me wanting to fight 12s on account of impaired energy.

It's interesting when facilities include both.
[epsgj0s] (score 16, diepte 2) A Pioneer, yee Be
[epsn4mu] (score 16, diepte 2) There will never be a union in my state. Ever. They're HUGE on killing unions here. So, were I closer, I'd certainly think about working in a place where conditions were guaranteed to be good. I'd pay dues, and make sure to support that union. I'm glad you know you have it good with the deal there in CA, but not all of us are so lucky.
[epslg6v] (score 16, diepte 2) Wow!! Just curious, but where do they usually stay when they do this?
[eptgcix] (score 14, diepte 4) My socializing limit is the same. After day 3 I become a bit snarky and I’ve realized that I need a day off in which I talk to no one but my family to recharge.
[epsmh47] (score 13, diepte 1) 4 12's in a row is a regular rotation for most full timers where I live. 2 Dx 2 Nx, then 4-5 days off. 

We're allowed to work up to 5 12's in a row with shift swaps/OT. 6 12's requires approval above manager level (usually it's when we're really short staffed, and the nurse has to be the one who offers to come in for shift #6, no mandatory OT here).
[epsoa5j] (score 13, diepte 2) No I’m PM/nights so I get a mixture of 11a-11p, 7p-7a, 3p-3a. It’s all worth it for a 2 week vacation every month.
[epsvoiw] (score 12, diepte 3) In our contracts it says we get to choose 8,10 or 12 hour shifts
[epsdhlm] (score 12, diepte 0) Most I ever did was 7 12s in a row. Worked Thursday - Saturday for one week, had an on call day on Sunday (and of course I got called in because duh) and then worked Monday-Wednesday for the second week. I didn’t do that to myself. My asshole manager moved my on call to that Sunday. Because that’s safe.
[ept1my4] (score 12, diepte 2) I totally get what you’re saying but at the same time I’m in CT where the starting pay is 60,000...if I travel just 30 mins to the Bronx now The starting pay is 98,000. Would you really turn that down?
[epsnznb] (score 12, diepte 4) That is awesome. A win-win for everyone.
[epsrftn] (score 12, diepte 1) The residents would like to have a word with you
[ept4aqt] (score 11, diepte 2) My feet hurt just reading that
[epswcj6] (score 11, diepte 2) Today is my 4/4.  I did it last week too.  This is my penance for six days off without having to take PTO.  2/10, will probably do again but I'm gonna be mad at myself.
[ept1hph] (score 11, diepte 1) Drugs. He’s definitely on some amphetamine.
[epskx2r] (score 10, diepte 1) Money and time off
[epsmxiw] (score 10, diepte 1) I like having big chunks of time off.  My job requires me to work 13 days each month; 9 day shifts and 4 nights.  I like to do 5-6 days at a time and all my nights together.  As an NP, working that many day shifts allows me to follow the same patients.  I see a patient in the trauma bay, and then can follow them through their ICU stay or discharge.  I hate working for two days, being off for one or two and then coming back and having to round on all new people.  Also, extra shifts are always nice; I'll work 8-9 in a row if extra shifts are involved.  🤷🏻‍♀️💁🏻‍♀️
[epsixx8] (score 9, diepte 2) Also probably sucked for the kids not having their dad around for half the month. There are nursing jobs in Colorado and you cant buy back time with family. Different strokes I guess
[epsxh61] (score 9, diepte 1) I hated having a messed up sleep schedule and worked nights. I worked Thursday through Saturday, then Sunday through Tuesday. No overtime. Didn’t have kids or pets at that time so only had to sleep when I was off. By day 3 I knew my patients by heart, the workload was easier. I got the daisy award from a 6 day stretch because by that last day I knew everything about the patient down to the flavor yogurt they had eaten when family would call for updates.
[epso4an] (score 8, diepte 3) 40k is nuts!
[epsvfbj] (score 8, diepte 5) There are plenty of places... rvs and vans are all over the streets in SF.
[eptwcam] (score 7, diepte 3) Oh I have nothing against it. I myself take adderall and vyvanse.
[epsrenf] (score 7, diepte 3) I’d do this
[eptlq9y] (score 6, diepte 3) Not everyone has the energy to do that, physically and/or mentally. If you can do it without breaking down, then more power to you. But don't be surprised when others of more average energy reserves cannot, and please do not be dismissive of others' abilities.
[epu7275] (score 6, diepte 1) We have two nurses who regularly work 14+ stretches of 12s with 16s thrown in. I think the record is 45 shifts in a row. Absolute insanity. Most I’ve done is 8 and I felt like I was going to die.
[epuhtd9] (score 6, diepte 2) I don’t get it. I don’t think I would have safety concerns but I know my personality would be fucked.
[epsr8y3] (score 6, diepte 3) Missouri?
[epthe5j] (score 6, diepte 3) Same here. Sound like you work in the South. Average pay here is $23/hr base then shift diffs. Saying "union" here is likely to get you fired.
[epsrdt1] (score 6, diepte 2) I feel like the Bay Area is a haven for nursing
[epsyvb4] (score 6, diepte 2) Is there a shortage or does the COL just make t worth doing?
[eptkn2c] (score 6, diepte 3) It's probably both, California has a major housing shortage in urban areas like LA and SF. Less apartments being built, more McMansions.
[epsqy6q] (score 6, diepte 2) SE Michigan represent. I’m jealous they’re still offering up solid incentive pay, st joes has been slowing down with that lately.
[epsn14m] (score 6, diepte 1) Because we do feel bad for our patients and colleagues. 

Depending on the type of work environment, by day 5/6 you're kinda on auto-pilot anyway so it isn't that bad. We're also allowed to use our banked OT hours to get days off later so in the long time it's worth it.
[ept5vd0] (score 6, diepte 1) Depends on the job/unit/person. I see in your flair that you're a CNA. When I was a PCT, there was in way in God's green earth I could work 5 12s in a row. No way. It would be unsafe for me and patients. The physical aspect was just too much. 

As a RN in ICU, I find it easier. I have 2 pts, max. I regularly work 4 12s in a row (my choice!) so I can get more days off without using vacation. Rarely I do 5. I can do it but it's not fun.

I have a friend who thinks I'm crazy for doing that. She won't work like that and she also works 8 hr shifts. Not my style. I prefer my days off. But I don't appreciate being told it's unsafe when I'm getting 8+ hrs of sleep each night, I'm eating, I'm not super stressed, and I feel fine.
[epsu9p4] (score 5, diepte 3) 💀
[epte37l] (score 5, diepte 1) Is his assignment the same throughout that time? I suppose it would be a bit easier knowing to an extent who and what you are dealing with day in day out.
[eptw6ew] (score 5, diepte 1) That’s insane!!! But then I imagine all those days off!!!
[epsspqz] (score 5, diepte 4) Where do they park the RV in the city?
[epswfmx] (score 5, diepte 6) Yeah I’ve seen them all around GG park & outer sunset... just never thought nurses would be staying in them, figured they might park in the hospital lots or something
[eptrru9] (score 5, diepte 3) There’s a big shortage of experience RNs willing to work and live here. Housing a increasingly difficult to find and costly, so hospitals have a hard time finding those experienced RNs. Training new-grads costs time and money, and there’s no guarantee that the RNs will stay after receiving the training. Thus admins don’t favor that here. 

There’s no shortage of Bay Area new-grad RNs looking to get started in the nursing pipeline 

Ex. UCSF RN New Grad Program Winter 2018 had 5000 applicants, 300 were screened and interviewed, and 77 were hired for all 3 of the UCSF locations. 

The shear difference in COL between the Bay Area and mostly every other part of the country artificially inflates the nursing paycheck, just like every other job here. 

>worth doing

Depends on how much value you place on spending time with your family and kids, and how much commuting you can handle.
[eptb4n2] (score 4, diepte 1) My friend just finished his ten straight. 💰
[ept00kx] (score 4, diepte 2) I did 4/4 nights once. Never again.
[ept2ixf] (score 4, diepte 2) Wow forced rotation in the middle of the week sucks big time.
[epsw7pt] (score 4, diepte 1) Does she just bring a sleeping bag
[eptve4t] (score 4, diepte 2) Pilots get go pills. If it's good enough for operating a billion dollar plane in combat...
[eptx6sm] (score 4, diepte 3) RNs here definitely have it made

Most hospitals here are very supportive of their nursing staff, and unions protections are quite strong
[epsgodr] (score 4, diepte 0) Usually 8 night on l, 6 off... Regular OT.. Never seem to get that full 6 off either. But I love my job and the money.
[epslqyu] (score 4, diepte 0) When I briefly did 12s in peds, I was always wiped at the end of my third and final shift. I honestly can’t imagine doing that for 8 days. 

I used to do 7 x 8s and that sucked too.
[eptbhho] (score 3, diepte 3) Agreed. I’d be much happier working 12 8s in a row vs working 8 12s.
[eptwhjb] (score 3, diepte 3) I like snowshoeing than skiing because I actually get to use my entire body to hike up the hills! I like full body workout.
[epto081] (score 3, diepte 4) O yea I’ll do 5 if I’m suicidal
[epuryah] (score 3, diepte 4) Why/How?
[epush7f] (score 3, diepte 5) To be able to stay alert   Prescription.
[epv56jw] (score 3, diepte 1) That's common, I thought? I've heard them referred to as 13/30's. 13 days straight and 30 days off.
(48 reacties met lagere score weggelaten)

=== THREAD 5lt5sw ===
SUBREDDIT: r/BuyItForLife
DATUM: 2017-01-03  SCORE: 846  REACTIES: 125
TITEL: Four years later, it's time for some new insoles!
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dbykfq9] (score 113, diepte 1) Looks like someone had an infected ingrown toenail.
[dbycl4k] (score 84, diepte 0) You just made me check my own ugg slippers that I've had for about as long as you haha.
[dbynke8] (score 74, diepte 2) I just threw up in my mouth a little bit.
[dbyvuwo] (score 70, diepte 0) BIFAFY! (buy it for a few years)
[dbyik2m] (score 54, diepte 0) Holy sh*t I didn't know you could get new insoles!
[dbynovb] (score 40, diepte 1) Combination of got and bought?
[dbypw8a] (score 23, diepte 0) lol...UGG in BIFL.

What next....
[dbymmnu] (score 22, diepte 0) STFU!  My Ascots were feeling a bit worn in spots last week, so I was just on Nordstrom seeing what's available.  (Some are on sale.)  It never occurred to me to just replace the insoles.  Thanks man!
[dbz8cfo] (score 15, diepte 1) I strongly doubt the tread is replaceable.  Even with indoor use, you'll eventually have to replace the tread.  Ten years, three pairs of insoles, and you'll have to throw them away.  The fur on the sides and the tops isn't replaceable, either.  

Could you make these last for 30 years?  ...I sure wouldn't want to see what they look like after 30 years.
[dbyuhmj] (score 14, diepte 2) I had a two year period where I had at least one of those ingrown toenails constantly. I had them surgically repaired multiple times, the doctors had no idea why I had so many. Then suddenly, they stopped and I haven't had one in over two years.
[dbyom9s] (score 14, diepte 1) Well not officially. You can see the original ones weren't intended to be removed as they are torn out of the shoe and some of the foam left behind.  I've had my Ascots for nearly 7 years and have replaced the insole several times using different UGG replacements. Some need a slight trim to fit.
[dbygc0h] (score 13, diepte 0) Did you waterproof the exterior of the slippers at all or anything? I recently got a pair back in November and was curious if that's necessary or something people would recommend.
[dbz683q] (score 13, diepte 1 OP) Interesting observation. Thinking back, I had IT band syndrome in my left knee a couple years back. Could have something to do with it. I'm right side dominant, so maybe I naturally put more weight on that side when I'm standing around in the kitchen. Could also be some manufacturing inconsistencies. (Stream of consciousness reasoning listed in order of descending likelihood.)
[dbyv28g] (score 12, diepte 1) All shoes don't need ankle and sole support. If you need ankle support for slippers, there something really wrong with your ankles.
[dbz45v3] (score 11, diepte 3) Now swallow it again
[dbyo8n7] (score 11, diepte 2) I really hope that's a thing now
[dbyz8qz] (score 10, diepte 3) I had ingrown toenails on both big toes in 5th grade. My podiatrist had to surgically fix them and cauterize the toenail (preventing it from becoming ingrown again) three times on each side before it finally took.
[dbz2bzf] (score 10, diepte 1) I was going to mention this as well. It looks like OP may have a posture issue. During the day, pay attention to other things too, like if you always step up with the same foot. When I first started hiking, it took about six months to realize that one buttcheek always got more sore because I was always climbing the big rocks with the same foot. After I consciously alternated which foot I would step out to climb things, my body evened out a lot more and I didn't have as many muscle issues.
[dbz629q] (score 9, diepte 1 OP) I haven't done anything special to them. I've lived in a northern climate while owning them, and wear them primarily all the time when inside. The rubber soles are rugged enough for stepping outside briefly (and definitely warm enough!) but I prefer to try and avoid the snow/salt and keep them as house shoes in the German tradition.
[dbyk5p9] (score 9, diepte 1) Me either. This is awesome.
[dbze2r6] (score 9, diepte 2) UGG is a brand by the way, which happens to capitalise on the name of ugg boots, which aren't specific to the brand and just refer to any sheepskin boot/slipper. Most people here in Australia (where ugg boots originate) don't buy UGG brand (an American company), because they're exactly the same thing as the "knockoffs" which are ~$100 cheaper.

So basically your answer there is any insole made of sheepskin is going to be exactly the same.
[dbyodfc] (score 9, diepte 3) Damn. I must have celebrated too hard.
[dbzelci] (score 8, diepte 7) ))<>((
[dbz05xt] (score 8, diepte 1) Seriously, I'm a slipper connoisseur, I would go through cheap pairs in less than a year because I always wear them instead of shoes in the house.  I was gifted a pair of these probably four years back and I rolled my eyes, but I was way wrong- they are the most comfortable slippers I've ever owned and after the years they still look and feel new.  Rubber soles to protect against the occasional disaster or allow for a quick run for the mail after a rain are a huge plus too.

I haven't seen this insole trick before, but when I get there I will definitely give it a shot.  I bet I can make it to a decade before I have to though- I usually wear socks with them (for comfort) but this also keeps them funk-free.  They seriously look new aside from the insoles obviously getting matted down a bit from pressure.
[dbyrhlt] (score 8, diepte 0) Wearing same exact ugg slippers and was just thinking "fuck my big toe is breaking through the sole" where did you purchase replacement soles?
[dbyw48a] (score 8, diepte 0) Did you hurt your left side somehow? Looks like you favor your left side.
[dbzn805] (score 7, diepte 3) The "V" notch is a good trick for ingrown nails.

I just used to pull off whatever nail was there to avoid them digging in in the corners of my toe nail.

But if you let your nail grow out a little and cut a V notch into the Center of your nail, it's takes all the pressure off the corners and they no longer dig in
[dbyjo56] (score 7, diepte 0) Oh! I gought expensive Uggs slippers a month a go. Super excited to see how the are holding up!
[dbyxcn1] (score 7, diepte 1) Say what you want about uggs, fact is their moccasins are very resilient. I've had a pair for the last 8 years and they're holding up fine. A little water stained so I got a nicer pair for around my place. But the old ones are still strong errand running slippers and they last forever
[dbywwg2] (score 7, diepte 1) Sounds like you needed a different size.
[dbyuna4] (score 7, diepte 1) Do you feel better?
[dbz28wz] (score 7, diepte 0) I have a pair of LL Bean shearling moccasins that are at least a decade old, get heavy use, and haven't needed a thing.
[dbza825] (score 7, diepte 0) I can smell this photo. I don't want to. But I can.
[dbz314q] (score 6, diepte 1) why would you wear slippers outside?  i feel like this is a joke going over my head
[dbz5x91] (score 6, diepte 1 OP) I just bought them off Amazon, they make them in different sizes so I found my size and pulled the trigger. I paid just shy of $30 (for reasons of obvious urgency) but I've seen the women's versions of the insoles going for around $15.
[dbz4sel] (score 5, diepte 4) And throw up again
[dbz50n6] (score 5, diepte 5) And swallow it again
[dbz552q] (score 5, diepte 6) >And throw up again
>>And swallow it again

DON'T rinse, just repeat.
[dbzfjg6] (score 5, diepte 4) I just peel the corner out if it feels like it's trying anything fishy. Since I've done that, haven't had to go to the doctor for one in years.
[dbyrbg7] (score 5, diepte 1) Literally I own the same pair. They last for so damn long. Just avoid wearing them when it's raining or wet outside.
[dbyn72o] (score 5, diepte 0) Yeah I've got a pair of those, slightly older and slightly less worn out, but I want to 2nd this BIFL.  Those are the best slippers I've ever had and they are weirdly scent resistant.
[dbyyau5] (score 5, diepte 1) I agree. I had a pair and they lasted less than a year. I picked up some LL Bean's, they have been going strong for awhile now.
[dbzfh5v] (score 5, diepte 1) Are you Sherlock?
[dbyi1fi] (score 4, diepte 1) For suede yes, of course. For leather you could get by without but you will probably still want to manage and treat with a waterproofer and/or wax.
[dbzgavx] (score 4, diepte 2) Get the mail, grab a package from the porch, let the dog out.

I dunno, sometimes the lazy prevails.
[dbyk7x3] (score 4, diepte 1) My cat likes insoles too.  We buy him cheap ones to play with so he will leave the good ones alone.
[dbyszt6] (score 4, diepte 0) How exactly is this BIFL if you keep having to buy new insoles?
[dbz2fak] (score 4, diepte 1) The slippers are BIFL and the insoles are a replaceable part to them. Similar to how a BIFL appliance may need a filter replaced over time.
[dbyts8a] (score 4, diepte 1) Have you seen the Norwegian Knitting Evening on Netflix? That sheep was chill as hell getting shorn and was in the room watching her wool become lovingly made yarn, and then a sweater. That sheep was totally cool with all of that. (And is not for slaughter, just wool.)

If I were a sheep for slaughter, I would be indignant that not only am I dying young, but only to be turned into Uggs?! This is the true indignity.
[dbzb297] (score 4, diepte 0) I guess it wasn't for life then...
[dbzev4u] (score 3, diepte 3) Oh yeah same here, lots of bloody pus and shoving cotton underneath and all that crazy shit. Then, after years of pain, it just stopped.
[dbzhuqb] (score 3, diepte 3) You were probably wearing shoes that didn't fit right
[dbzpe0w] (score 3, diepte 3) Link us to these knockoffs?
[dbyqp46] (score 3, diepte 0) Wait you can get new insoles for that slipper...... TIL
[dbz3ads] (score 3, diepte 2) good point!
[dbz07gs] (score 3, diepte 1) I'm gonna go eat some cheese just for you!
[dbyxc2i] (score 3, diepte 0) It looks as if it was time for some new insoles before now. How much are the insoles? Can the tread be replaced?
[dbzffej] (score 2, diepte 8) Been a while since I've seen that. Thank you friend.
[dbyicxu] (score 2, diepte 1) I was gifted a pair of these for Xmas, good to know you can replace the soles!
[dbyjedz] (score 2, diepte 2) hey me too man ! my parents gave me the Ugg Clugg (according to Ugg's website)

Can the insoles also be swapped ?
[dbywt9e] (score 2, diepte 2) Don't do this. Use scotch guard or the beeswax + blow drier method.
[dbyzrc4] (score 2, diepte 3) OP's is the oiled leather version, so a little bit of leather dressing every now and then goes a long way.
[dbz548x] (score 2, diepte 1) If I'm home, I'm wearing my Ugg slippers. I wear them everywhere around the house, including outside, the backyard, driving to the grocery store... Hell, I've even painted in them. They're great! Had em going on 7 years now.
[dbzpgkr] (score 2, diepte 3) Where might someone in North America get these "knockoffs"?
[dbyjiqv] (score 2, diepte 0) My dog likes to rip the insoles of my UGG slippers out and chew the foam off the bottom of them. he leaves the fur but destroys the foam. Where did you get the new ones, how much?
[dbz63rs] (score 2, diepte 1 OP) I just bought them off Amazon, they make them in different sizes so I found my size and pulled the trigger. I paid just shy of $30 (for reasons of obvious urgency) but I've seen the women's versions of the insoles going for around $15.
[dbynfa0] (score 2, diepte 1) I have a pair like this that I wore for 5 years, probably average out to like 2 hours a day in reality.  Mine are in better shape than this and still don't stink.
[dbyqgdm] (score 2, diepte 0) I've had my Haflinger boiled wool slippers for about 4 years now. They don't need any mending and look as good as the day I got them. If anything, I wish they *would* start falling apart - I bought half a size too big by accident!
[dc09kdt] (score 2, diepte 3) I think that line only works on people who haven't looked into the practice of shearing sheep for wool.

Humans have domesticated sheep since 10,000+ years. As a result of domestication -- the slow process of altering an animal's genetic development though human-caused gene selection (basically, for the last 10,000+ years we've been killing the sheep that dont serve our needs) -- sheep have developed thick wool AND a reliance on humans to regularly shear the sheep in order for it to live a comfortable life. Basically, humans have very much fucked with the genetic profile of the sheep, and cropping the butt-flaps of sheep for slaughter so they don't get ass diseases because of dirt and poop getting stuck in their butt-wool sounds really sucky -- but it's literally the LEAST we can do for these slaughterhouse sheep because humans have removed any hope of these animals genetically regaining its original wool follicular distribution.

For proof -- look at other domesticated herd animals. Look at their butts!! Normal distribution of hair folicles over the body, and not much in the butt area. They poop, the poop falls to the ground, away from the animal, no need for butt-stuff. With sheep domesticated for their wool... this is not the case. Domestication meant keeping really woolly sheep to breed. And this has lead to an abnormal amount of butt-hole-fleece. Looking at related herd animals that were NOT domesticated in western countries, such as mountain goats, pygmy, and llama, and alpaca, their buttholes are totally fine to poop. 

This particular sheep, shorn for its wool, is a sheep on a Norweigian farm that doesn't have a practice of clipping off the area around the sheep's butthole. Again, this is a sheep from a breed raised for its fine wool qualities. Your average slaughterhouse sheep is likely treated differently. A sheep slaughtered for its hide is also likely treated very differently.

You seem to like education. Watch the Norweigian Knitting Evening on Netflix around hour 4 or 5 to see the actual sheep to which I am referring. That is a happy, calm AF sheep, who doesn't seem to object to having his wool shorn in the slightest. THIS particular sheep even gave an interview in celebration. Gurli is like the Posh Spice of sheep and sticks to a diet of grass and Norweigian sedation. You can see the sheep's butthole as the wool is shorn away ....... it is an intact butthole with normal wooly sheep butthole flap skin.

Because you really like education, you should know that if left unshorn, sheep WILL DIE OF DISEASE. Their wool never truely stops growing. If left unshorn, dirt, insects, and debris get lodged it it which cause bacterial growth, accumulation of parasites, an inability to move or relieve itself, and eventually a painful sheepy death. Which is awful, and worse than a slaughterhouse sheep having a bit of hide removed from its hindparts.

Educate yourself. I'm not being difficult here. It's the truth.

If you don't want to encourage this practice in sheep for slaughter, stop buying Uggs, because they are buying from sheep farms that remove the butthole flaps of skin.

If you want people to stop using wool citing this reason, you are very misguided and ill-informed, and will likely turn others off from your cause of preventing exploitation of animals by presenting your misinformation as fact. AND you'll cause sheep to die very not-soft deaths in the process.
[dbzxwhh] (score 2, diepte 4) Mmm that's another piece of cheese eaten thanks to you! I'm sure the cows love it!

Keep going, Please
[dbzzqrz] (score 2, diepte 6) Man you really hate animals don't you? I'm literally eating cheese because of you, therefore you aren't a vegan. Do you want pics?
[dc00527] (score 2, diepte 8) So you're not a vegan but you post stupid ass comments that make it sound you're one? 

Man you really are an idiot and probably the most miserable person on Reddit. Oh well there's another piece! Thanks!
[dc00v4n] (score 2, diepte 8) How fucking stupid are you? 

You're literally contributing to animal cruelty/climate change just by being an absolute cocksucker, you know this, yet you keep doing it.

I can't even compared your level of stupid.

You're up to 5 pieces!
[dc01op8] (score 2, diepte 10) Yeah I'm really fat. 

I'm curious, are you actually mentally challenged?
[dc01uya] (score 2, diepte 12) Ahh i see how you avoided answering the question.

I'm keeping a tally for you, don't worry, you have directly contributed to the consumption of 9 pieces of cheese. Congratulations! Vegans everywhere are proud of you!
[dc01z8v] (score 2, diepte 14) How so?
[dc01m68] (score 2, diepte 10) What? shit did you not graduate high school?
[dbzy5h0] (score 2, diepte 3) I've seen it done, doesn't look like they are bothered by it!
[dbz9xq1] (score 2, diepte 2) I like that. And what you wrote in brackets, is a good description of it all
[dbz6a30] (score 2, diepte 1 OP) Looks like the price ranges between $15 and $30 USD on Amazon. I don't believe that the tread is replaceable, but I wear them primarily as house shoes, so I doubt that I will ever need to look into that.
(45 reacties met lagere score weggelaten)

=== THREAD lfdtsk ===
SUBREDDIT: r/ems
DATUM: 2021-02-08  SCORE: 1869  REACTIES: 124
TITEL: Also don’t call 911 for your 86 year old family member with foot pain so we can take her to the Er and she contracts covid.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gmlkch4] (score 297, diepte 0) “ThErE arEnT CoViD paTieNts HeRe, aRe theRe?”

Nope. There aren’t. The hospital resorted to taking them out back, and shooting them. Now they can treat the real emergencies, like your chronic toe pain that just now warranted a hospital trip, at 8:30 on a Sunday. Your family was so concerned, that they didn’t help you into one of 5 vehicles parked outside, rather they called me, an exhausted monkey, to take your blood pressure and lead you to the ER lobby...which by the way, is infested with covid. 

Can you tell I’m over it? Lmfao
[gmllcct] (score 128, diepte 1 OP) We are all over it.

Or the nursing homes who send out patients for every little thing. We had a lady WITH COVID sent out to the Er  multiple times to change the dressing of a wound on her foot. 

The nursing homes wonder why they are 100% covid positive and then do stuff like this.
[gmlf4kp] (score 120, diepte 0) Also maybe a raise instead of clapping or bs $5 gift cards because we're "heroes"
[gmlp8ij] (score 94, diepte 2) Exactly. “Well he’s got covid” *room air sat 98%*
“But he’s altered” *Gcs 15* 
“Well we just can’t treat him here, because he could infect the other residents” 

So you lied to me in your report, and now you want *my* name, because I’m questioning your literal false narrative? Yeah I’m Steez the fuckin Sleaze, call the sup.
[gmlhklf] (score 81, diepte 0) Seriously. Had a 55-year-old woman call us last week for a complaint of lower back pain. When we arrived on scene she proceeds to tell how she was going to drive herself but thought maybe an ambulance would be a better choice, when she lives only two blocks from the ER.
[gmm0a0l] (score 61, diepte 1) Every obese patient is a lawsuit and an injury waiting to happen. And they’re always the ones unable to fathom that no, we can’t carry 500lbs of fat with just two people. They can wait for lift assistance. I’m not injuring myself so the 500lbs regular can get her knee looked at again and get told it’s cause she’s too heavy, so she goes home mad and orders a bunch of pizzas. Then I get called out there again and lo and behold, multiple dozen stacks of pizza boxes going back to November.

Every interaction with them can kill your career. Call for lift assistance. Don’t injure yourself, you’re not coming to work to get disabled and these kinds of patients will never put in any effort whatsoever and will even try to make things worse for you.
[gmm97ur] (score 58, diepte 0) Took my dad to the ER this morning for COVID-related problems.  He's on Day 8, and finally decompensated enough that staying home wasn't an option anymore - thought he might turn the corner after week 1 + serum antibody infusion... but nope.

He's not in the ICU or anything (yet), just supportive low-flow O2, fluids, and dexa/remdes combo now that he's hospitalized.

How'd they get it?  Who knows... but my 70 year old parents have been traveling around by car out of state, in state, etc. "because it's not crowded now!"  Not staying home... out vacationing, eating in restaurants, etc.

We (siblings and I) tried to tell them.  But they're our parents, so we can't "ground" them.

Finally, this morning, with me in my P100 mask, goggles and gloves, helping my dad pack for the ER (knowing he'd at least be admitted), my mom goes "we always heard COVID COVID COVID but I didn't know it was this bad."

Me: "This is mild.  Dad's going to walk to my car, and walk into the ER.  He's speaking in sentences.  He's MUCH better off than the ones I get in the ambulance."  Don't get me wrong, he's sick, and he's decompensating... but he's not "OMG ICU INTUBATE URGENT!"

Her: "We just didn't know."  Yes. you. did.  The instructions couldn't have been more clear.  STAY. HOME.  Especially you two.

/sigh

At least the PA at the ER told him "This x-ray isn't as bad as most I've seen."  Oh, and yeah, no visitors.  Period.
[gmli7py] (score 54, diepte 2) We have a written protocol (to be activated if Covid got bad enough) that was exactly this. Discourage transport unless necessary. Your attitude blows.
[gmltes3] (score 49, diepte 0) No. I just want every obese person in the US to lose weight.
[gmmq6zm] (score 49, diepte 0) Had a girl call us (911 dispatcher) the other day, she calmly said her brother was probably having an “appendic attack.” I said, ok where are you? ...she was parked at a gas station literally one block from the ER. You could throw a rock and hit it. I thought, oh hell no I’m not sending them out for this shit at 3am...she goes, “I’m not from here, I think we just need the amalamps to take him the rest of the way.” I said, “if you look up, and to the right, you can see the big hospital sign lit up up there. You’re literally a block away, maybe less. It’ll take you less time to get him there than if I (ask you these 547 EMD questions and) send the amberlaps - I’ll direct you.” Of course, during the directions, she says, “well if I bring him in instead of the whamalamps, will he go straight to the back?” ...”ma’am, if the whamalam brought him in, he’d probably still have to sit out front for a little bit.” She didn’t like that and hung up on me.

Edit: thanks for the gold :)
[gmllnll] (score 38, diepte 1 OP) Oh that would enrage me. But only on the inside, I’d probably say “yeah, an ambulance was definitely a good choice if you’re having a hard time moving around :-). Is it too hot/cold in here for you? Do you want another blanket ?
:) :)”
Hopefully that didn’t happen in the middle of the night
[gmlrxve] (score 33, diepte 2) She was ambulatory and put her pain as a 4/10 and it was our 11th call of the night, 7 hours into a 12 hour night shift. All we were asking for was just a chance to get back to station for five minutes so we could eat our cold food and use the restroom.
[gmlundr] (score 33, diepte 0) But they only have 8 cars in the driveway. It's hard for them to decide which one to drive to the ER.
[gmlppz4] (score 29, diepte 3) Exactly. We have that protocol and it WAS activated (and still is). I worked in the absolute trenches in NY when C19 ass fucked us.

https://www.health.ny.gov/professionals/ems/pdf/20-06.pdf

We regularly discouraged unnecessary pt transport because the hospitals were absolutely turbofucked. People were dying in the fucking hallways. It was a disaster. Units would go out of service for hours bc they couldn’t hand their pt off, or they’d get diverted all over Christ’s creation, and it would cripple the 911 system. 

But a bunch of keyboard EMTs and paragods who likely work in BFE are gonna be like iF yOu DoNt TrAnSpOrT yOu SuCk.

Sorry, I’m going to follow the DOH guidance.
[gmmod3q] (score 28, diepte 4) We just automatically go full ppe any time we step into certain settings here, and nursing homes are at the top of that list.
[gmm0ov8] (score 28, diepte 2 OP) That’s so true, they never try to help.
We have one who is 500 lbs and recently laughed as we were all trying to get her into the squad
[gmlcctt] (score 27, diepte 0) Thank you. Lately I’ve been doing the “are you SURE you want to go where the COVID is...?”

Edit: Jesus Christ people, I work in and around NYC where we have non-transport protocols from the DOH: https://www.health.ny.gov/professionals/ems/pdf/20-06.pdf
[gmmieti] (score 26, diepte 3) I literally just transported a covid positive patient satting 94% on room air with no complaints who originally didn’t even want to go to the hospital but the fucking nursing home staff convinced him, and they also didn’t tell us he was covid positive until we were on scene so I had to wait 10 minutes for my partner to go back to the rig to get us the PPE
[gmmf14t] (score 25, diepte 2) Our local assisted living is 100% positive and has tried to send out 1/3 of their population for IV hydration at our community hospital. *at once* the hospital and my company have resorted to giving them supplies to *not do this.*. A staffer without gloves took a patient who was going there to die of covid’s mask off before I had stepped away from bedside. It’s a miracle anyone in that hellhole survived covid.
[gmlucwh] (score 22, diepte 4) Your entire argument is predicated on the assumption that OP and myself can't distinguish who absolutely doesn't need transport and the language used to convey that to the patient being inappropriate.

Of COURSE nobody is trying to convince a STEMI patient or fall with blood thinners not to transport. Of COURSE nobody is using shame or fear to persuade a patient against transport. 

Next time everyone will be sure to accurately quote themselves instead of using paraphrased off handedness when discussing this outside of official settings. For fucks sake...
[gmll0ky] (score 22, diepte 2) Nah, that’s bs. I told a patient that was completely stable with fantastic room air sat and no difficulty breathing, that they’d be discharged from the lobby, but it’s their choice. 

Shocker. Pt taken to lobby, it’s almost like I worked in an ER during this whole thing. Charts aren’t hard, but the over exposure from people either with covid, thinking their 100 degree fever is emergent, or the people resuming their bullshit complaints, is getting in the way (once again) of us treating the legitimate emergencies.

Anyone that thinks BLS charts are hard is either overcharting, or they can’t type qwerty
[gmm5o0x] (score 22, diepte 4) We run only 6 trucks at night for a county of 126,000 people. We also have a high homeless population and a big ten university that started in person classes again last week. Add the pandemic into the mix and each shift we are run into the ground with exhaustion and barely see our station.
[gmlvkw4] (score 21, diepte 3 OP) 11 calls in 7 hours ???? Jesus Christ
I get like 12 per 24 hour shift and that’s overwhelming for me / burns me out
[gmmw43k] (score 21, diepte 1 OP) You’re my hero.
[gmm31vq] (score 20, diepte 1) I hear that, had a 71 yof call us with chief complaint of "blood poisoning" because she had a cut in her finger that wouldn't stop because of blood thinners and wanted us to taxi her to the hospital. Like come on...
[gmm87ru] (score 20, diepte 2) Fair point, but we need to also accept that there are things we as providers can do to mitigate this risk.  So often, I see people out on musculoskeletal injuries and I can guarantee you the last time they even thought about a gym was because it was next door to the burger joint.

This job is physically demanding, and we need to take some responsibility to prepare for that.  Basic mobility, strength, and cardiovascular endurance maintenance, coupled with a *minimum* of attention to what we eat is how we mitigate this risk.

There is a nasty and lethal culture of poor habits and fatalism in this field, and it's time we take *part* of the responsibility for helping build some of our own personal resilience.

None of this is to take away from the real and present risks of harm that come with the current culture of EMS that are beyond our control, but if it's getting hard to tell the difference between you and your patient, that's a pretty late sign that something is wrong.
[gml7nh0] (score 19, diepte 0) This. All of this.
[gmluxfn] (score 19, diepte 6) Sound argument. Really, you should be proud.
[gmmzjbe] (score 19, diepte 5) One single case popped up in the community in my (non-US obviously) state last week, and as well as locking down the state to make sure it doesn't spread, every single patient is now full PPE, no questions asked. 

We don't want that shit spreading.
[gmlryep] (score 18, diepte 0) Naw naw naw shut up dude. Don’t take away my free chipotle and crocs.
[gmmzu3y] (score 18, diepte 1) Ooff. I feel like you just described 90% of baby boomers (including my parents). "I didn't think the leopards would eat MY face".
[gmn5cfn] (score 18, diepte 1) The coworker who was a covid denier and convinced like 15 staff not to get vaccinated died yesterday of COVID. I’m pissed at him for throwing his life away and possibly others.
[gmmzzzr] (score 17, diepte 1) I love you. Please come work for my dispatch center.
[gmlveuf] (score 15, diepte 8) That's why we have drivers, like you, to handle the extra cleanup.
[gmlqk01] (score 13, diepte 2) https://www.health.ny.gov/professionals/ems/pdf/20-06.pdf

Following current DOH guidance IS my job. Listening to a bunch of assholes on the internet who know nothing about my area, agency, or protocols isn’t.
[gmlsco8] (score 12, diepte 0) But you see, that would make them less money. Praise, ceremonies, and tickets are cheap ways to make them appear like they give a shit.
[gmlr1dg] (score 11, diepte 2) https://www.health.ny.gov/professionals/ems/pdf/20-06.pdf

Nah, just following DOH guidance. And I have to do a PCR regardless.
[gmmarny] (score 11, diepte 3) Agreed 100%. I lift weights and watch what I eat. I ought to do more cardio for sure though.

Ive had a guy have to stop and take a break when we were taking a patient for a direct admit to the hospital one time when a CCT truck wasnt able to get there
[gmmlt0w] (score 11, diepte 0) I had a call for dehydration and the poor guy was terrified of going to the hospital until his son bullied him into going. For dehydration.
[gmluqru] (score 10, diepte 3) >	I have to do a PCR regardless.

That is true, my fault.
[gmm37sh] (score 10, diepte 2) I probably would have said “well it definitely would have saved you about $800 but we’re here now” and then taken her to the lobby.
[gmn9ow9] (score 9, diepte 5) When I deployed to NYC last spring, we had to convince people on multiple occasions TO GO to the ED because they were scared of COVID.  one lady we sat on scene for close to an hour BEGGING her to go because she was in rapid afib between 150-180, with complaints of dizziness, and had multiple short runs of vtach while we were there.  We tried to explain to her that if she stayed home there was a very good chance she would die before an ambulance got there if she worsened, and she refused to go citing her desire to die around family rather than alone in the hospital if she caught covid.  She'd lost 3 family members in the last 2 weeks due to covid and was resigned to the fact that she would die either way and she'd rather be around family.

This dude shitting on you is an asswipe who clearly hasn't seen a system pushed to the brink.  Keep fighting the good fight my friend.
[gmn705e] (score 9, diepte 2) I had a nursing home send a pt to the ER because "she has comorbitities and she just tested positive for covid"... okay? So why are we bringing her in? "I'm not sure, the provider just wanted her to go".
[gmntxvj] (score 8, diepte 2) 90% of EMS calls are non emergencies that don't necessitate ambulance transport... if you think this is a rare occurrence, you're in for a rough ride
[gmodopi] (score 8, diepte 6) Can someone with that mindset come take over running shit in the US please? I had to argue for twenty minutes to get a new N95 when I had a covid positive patient on high flow O2 after the elastic bands on the one I’ve been using for three weeks snapped.

They wanted me to staple it and continue using it.  I wish I was fucking kidding.
[gmn1xym] (score 8, diepte 4) I hope you reported that. That's failure by the facility to provide a safe working environment.
[gmnni5v] (score 8, diepte 1) I never would have believed how many times I've heard this while sitting at triage. Please keep you mask on. It's for your safety too ma'am. Yes there are sick people here.....in the emergency department 😑
[gmnpizc] (score 8, diepte 1) Lmao. I worked as a receptionist in an ER lobby. Can confirm its infested with covid. Family members walk in, I check the patients chart, patient is COVID positive. They want to visit. Covid patients can't have visitors so I tell them no. "But I live with her!" Then you should be in quarantine. Except I can't actually tell them that because of HIPAA.
[gmoe8d0] (score 7, diepte 7) > the one I’ve been using for three weeks 

What the actual eff?
[gmnc4jz] (score 7, diepte 2) Sorry. What exactly do nursing homes do if they don’t change wound dressings?
[gmm68tt] (score 7, diepte 0) And money. That would be cool too.
[gmnbchr] (score 6, diepte 6) Honestly, I think they were just fired up, made some assumptions, no big deal.

But then they doubled down on being a twat waffle. Been there, hopefully they only act this way online and not to their partners.
[gmmet18] (score 6, diepte 4) Thanks for the heads up, much appreciated. Nassau reactivated it...seems like it’s very regional.
[gmlv6v3] (score 6, diepte 4) All good, friend!
[gmnug80] (score 6, diepte 1) We were given sweatshirts and snacks than ran out within the week 🤦‍♀️
[gmmsspu] (score 6, diepte 5) I feel you so much on this. My service covers 2 counties with a population of 250k residents with 7-8 trucks almost every day because staffing levels are so low. We also have a Big 10 university, a TON of nursing facilities, and a high population of low income, medicaid/no insurance people who think an ambulance is just a taxi with nice lights. Shifts here define brutal. Its so bad we are now offering a $7500 signing bonus for new Medics.
[gmmg2cw] (score 6, diepte 4) Crazy how different our experiences can be. 11 calls in 7 hours is nearly physically impossible where I am. You can be on delay in the back hall of the hospital for 7 hours. Sometimes out transport times will be 20min there and 20 back. I couldn’t do the paperwork alone for 11 calls in 7 hours lol
[gmmlfm9] (score 6, diepte 0) Honestly I would be fine if they just didn’t tax my income for a bit.
[gmmz9fn] (score 6, diepte 1) I mean..I passed out twice from dehydration at a nascar event and told them I was fine to go home after sitting in the med Bay Area for a couple hours with some fluids then paramedics came to pick up a guy who fell and I passed out in front of them and the lady was like “so we are taking her too right” was a sad day, I just wanted to go home but I get what your saying haha
[gmn4j4k] (score 6, diepte 0) Foot pain can be a sign of cardiac arrest😤
[gmnnkrq] (score 5, diepte 3) Something tells me she’s not paying that bill.
[gmmpvpw] (score 5, diepte 1) These are the people you dont get insurance info from.  Let them see that $1200 ambulance ride and have to deal with their insurance carrier to cover it or have to reimburse them in 3 months.
[gmnr6ie] (score 5, diepte 3 OP) It was because a wound on her foot wouldn’t stop bleeding. The bandage was getting soaked in blood, and instead of changing the dressing they shipped her out. The hospital didn’t do anything for her but change the dressing. She had an appt with her wound care doctor like a day later. it was annoying
[gmn8ktt] (score 5, diepte 1) Wait they called at 8:30 instead of 2 or 3 am. They are courteous.
[gmnhuy6] (score 5, diepte 2) My patient had 2 glasses of wine and had normal vitals. Son called cause his home BP monitor gave a super low BP less than 10 minutes before our arrival. But I felt bad cause the guy was obviously terrified because of COVID but was basically pressured by his son to go
[gmpb9lq] (score 4, diepte 1) It took 2 years of B.S. to amass enough “rewards points” to redeem a $20 Amazon gift card from work 😎💪🏽

*STEP BACK FOLKS HEROS SHOPPING HERE*
[gmn8si9] (score 4, diepte 2) I’m not on at 2 or 3, therefore I can’t be boned then. However, I’d rather take the dieting for 24’s and respond from a post like the fire dept. I’m literally sitting in my truck, wasting away, then am too tired to lift when I get home.
[gmn4lpq] (score 4, diepte 2) I have 0 issue calling for a lift assist, I will wait as long as it takes. If dispatch says no, I say I’m not transporting because it’s to dangerous
(54 reacties met lagere score weggelaten)

