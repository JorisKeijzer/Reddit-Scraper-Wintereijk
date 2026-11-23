# Label-batch batch_0126

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
Schrijf het resultaat naar `batch_0126.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: kgd8lp, 380c6s, 6lo7e1).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD kgd8lp ===
SUBREDDIT: r/AdvancedRunning
DATUM: 2020-12-19  SCORE: 98  REACTIES: 68
TITEL: Recovering from Plantar Fasciitis
POST (source_id=post):
I (M, 22)have been dealing with Plantar fasciitis for the last 13 months. It pretty much destroyed my running for the past year, including the end of my college career. I’ve been doing everything I could find to fix it, including icing, foot stretching, calf stretching, massaging, wearing a therapy sock, shoe inserts, and an irritating amount of resting. 
I have had periods of time without it, but it always seems to come back. My doctor says it will go away over time, but it’s been so long already. Does anyone have any further recommendations that I could try?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gge39oy] (score 41, diepte 0) Tight / weak calves were the root cause of my PF, cured by lots of rolling and stretching and strengthening
[ggdxoxk] (score 38, diepte 0) Are you able to lift your big toe up on its own, kind of like this (in whatever pain free range of motion is available to you):
https://www.youtube.com/watch?v=kcC2ZzJIEPw

In my experience, PF is typically the result of some part of the foot not articulating sufficiently to lengthen/shorten the tissue in the foot with every step.  When that lack of changing length becomes the norm, the body gets guarded about it and tightens up preventing you from using it in that way.

The big toe is a good 1st place to check for something like that, and if its not moving comfortably through enough range of motion, acquiring a bit more range and control there may be a good place to start.
[gge6kqo] (score 27, diepte 0) There was a post here the other day about PF. 110 comments of people sharing what worked for them. For me what was interesting was lots of people saying different things worked for them, so it seems different things work for different people. Would be worth going through and seeing if there’s something you haven’t tried yet.[link](https://www.reddit.com/r/AdvancedRunning/comments/kdzaxp/what_worked_for_you_to_treat_your_plantar/?utm_source=share&utm_medium=ios_app&utm_name=iossmf)
[gge8s1y] (score 17, diepte 1) This was my experience as well. Lost over a year and a half of running to PF. Saw doctors, specialists, and PT’s, and tried countless treatments. Eventually, a sustained emphasis on rolling, stretching, and strengthening my calves did the trick.
[ggea802] (score 9, diepte 2) Nice!  Taking away the pressure can be a good way to help reduce inflammation, if thats comfortable for you.  

Note however that nothing in an insert will improve the capability of the big toe, arch or ankle to move through its expected range of motion, and its worth considering which of those could move a bit better and seek some change there as well.

The combination of reducing aggravation/inflammation in the area while also improving capability for movement in your weakest link can bring better results than either one on its own.
[gge6owh] (score 9, diepte 1 OP) Thanks, I didn’t see that.
[gge0pd6] (score 8, diepte 0) I struggled through this for years, saw a couple different podiatrists, got custom inserts, all that stuff. It didn't really help. I did more research on my own and found that the inserts were actually weakening my feet which was doing more harm than good. I slowly worked my way out of the inserts. I also bought house shoes to help me feel more comfortable around the house, especially in the morning with all the hardwood floor we had. Finally, I picked up a Foot Rubz massaging ball for $7 and it was the best money I ever spent.

My recommendation would be to get one of those Foot Rubz balls and use it 10 min here, 10 min there. It'll hurt at first but you obviously control the amount of pressure you put on it. I also would put mine in the freezer between uses.

It may not work for you entirely but just something to keep in mind. In hindsight I wish I wouldn't have wasted a year seeing two podiatrists, but it pushed me to think through my issue a little more I guess since they couldn't solve it.
[gge6pnr] (score 8, diepte 0) Similar to what others have said (and you may have already tried this) but a frozen lacrosse ball works wonders. I’ve suffered from PF too and rolling my feet out has helped tremendously, to the point where PF has disappeared but I still roll religiously. 

I’ve also noticed that rolling seems to help with muscle tightness around my ankle. And I believe this is because some of the structures that are under the foot wrap sound to the ankle and up the calf.

Also, custom orthotics are weakening your foot. Support in a shoe is good, but too much support takes the job of your arch away. You can strengthen your foot by walking around barefoot more often, and even working up to running (short and slow) barefoot.
[gge0kht] (score 7, diepte 1) Great post! That's exactly my experience.
[gge12ud] (score 7, diepte 0) Switching to barefoot did it for me: [https://www.feetremedies.com/barefoot-treatment-plantar-fasciitis/](https://www.feetremedies.com/barefoot-treatment-plantar-fasciitis/)

Now my pf only flares up when I wear shoes that have too much sole or padding.
[gge5ssx] (score 6, diepte 0) If you haven’t already, go see a physical therapist. In my experience, they can better assess the injury and have you strengthen your foot so that whatever deficiency you have can be corrected. If you have and it hurts to the point where you can’t run, it might need something more than just ice, stretching, and some strength training.
[gge3r0p] (score 5, diepte 0) I’d continue to work with PTs. Don’t just wait for it to go away—you’re doing something to cause the PF and those habits aren’t going to magically disappear. 

My PF was from an extremely deep set hip shift/pelvic floor weakness. My PTs struggled to narrow it down, but enough time and perseverance paid off. It took a Pilates focused PT clinic to eventually help me figure out the weakness causing me to use my foot improperly. I worked with my previous PTs for 1.5 years and I’ve been working with the (much more effective) PT on and off for 8 months. 

You will know when your treatment is effective. Communicate. Leave when they are being lazy with you, don’t waste your money and time.
[ggeutbp] (score 4, diepte 1) I was going to post the same feedback.  

Strengthening my feet by walking barefoot whenever possible really helped.  I'd be totally barefoot around the house, and wear Vivo Barefoot shoes when shoes were required.

I never switched to totally barefoot shoes for running, however lowering the drop and wearing Kinvaras, Hokas or racing flats also helped.

Personally, I'd avoid shoe inserts or orthotics, as they brace (and therefore weaken) the muscles your foot needs to be strong throughout your gait.
[gge8m6x] (score 3, diepte 1) I literally went to a physician today for plantar, and he told me exactly this! He is going to make an insert to take away the pressure.
[ggepo8s] (score 3, diepte 1) This general advice has worked for me with PF! I've also found yoga helpful as an indirect way for building strength and better control of my ankles/feet/toes...also because I get bored af doing isolated PT exercises
[ggfrwcl] (score 3, diepte 1) I have weak gluts and abs and a rotated pelvis. It causes PT in my right foot. Pilates and proper Physio did wonders for it.
[ggdwulg] (score 2, diepte 0) More rest. And keep up the PT

If you keep aggravating it, it’s probably because you haven’t rested long enough and you’re jumping back into running prematurely
[ggivl03] (score 2, diepte 3) Thanks, I agree. In the end the body is doing the work...
[ggg2gfo] (score 2, diepte 1) Seconded.
[ggegq96] (score 2, diepte 1) I use a lacrosse ball I found sitting in an empty field one day, works great and it was free! (For me at least)
[gggod45] (score 2, diepte 1) This is because "plantar fasciitis" can be slapped on any pain on the bottom of the foot. Sometimes that's really what's happening, sometimes it's something else.

PF is a tendon problem. Rest makes it feel good for a bit, but will never solve the problem. It needs load, preferably progressive overload at a low level of discomfort. Best to see a physio if nothing has made progress after a couple of weeks. Most places in US you can see a PT without first going to a doctor. Look for a sports clinic or an OCS or SCS designation. Those are Orthopedic Certified Specialist and Sports Certified Specialist respectively.
[gge7lye] (score 2, diepte 0) The only thing that worked for me was running in stiffer or carbon plated shoes and sleeping with a foot splint every night. Nothing else worked for me.
[gge8v3p] (score 2, diepte 0) Freezing a water bottle and using it to roll under your feet helps and is easy to do. Helps massage the foot and the cold helps with inflammation
[ggedxup] (score 2, diepte 0) My wife has been dealing with this for a while in her heel. It got to the point where she exhausted all other options and ended up having surgery. This was last week and she is still recovering so too early to say if it worked. They had to put her under with anesthesia but the actual procedure didnt take long (less than 10 minutes). They make a small incision and use an endoscope to navigate and cut the fascia in a specific way to relieve the pressure. The doctor said 80% to 90% of people report it feeling better after getting the procedure. I run a ton a miles barefoot so I personally don't know if I would have done it but its hard to say without being in her situation.
[ggee98f] (score 2, diepte 0) I had it for about six months in both feet, had cortacoid steroid injections into both feet and it fixed it within about a week!
[gger75e] (score 2, diepte 0) Have you seen a physiotherapist? I wouldn’t go because I’m stubborn and have dealt with PF for the last 8 months, trying everything under the sun. I finally went Thursday and was impressed by the assessment. I did 2 days of her recommended exercises and today I went for a 20 km run and was very surprised to be pain free. Like completely pain-free. (I was correcting my gait a little during the run per her observation of my knee pointing in the wrong direction).
[ggetlul] (score 2, diepte 0) Anecdotal evidence from me, but I would grip my toes into carpet for 5-10 minutes multiple times a day, like try and pull the carpet up with my toes. 

I read that a long time ago. It's helped me and a few of my friends.
[ggf5l1p] (score 2, diepte 0) College runner here. I have been dealing with it for the past year or so, although I had been having other achilles/calf issues as well. I went to my podiatrist and he gave me this shockwave treatment. A bit uncomfortable, but in your situation it shouldn’t deter you. I got the treatment 3 times in 3 weeks, and my doc also made me custom made orthotics. He said a big cause of the problem was my flat feet trying to fit into Nikes, which are too narrow. The shockwave treatment made a big difference in just a few days, and I’m about to get some new shoes. Also try to get a golf/lax ball to massage your foot with, and look into a night splint for your foot to wear while you sleep.
[ggf8yp7] (score 2, diepte 0) Strength and mobility are the key here. Mix in some lacrosse/golf ball work on your calves/feet as well and you've got the ticket.

Inserts are not a fix, they mask foot weakness and it'll catch up with you, even if it works for a time. Icing is totally useless.

Your doctor doesn't know what he's talking about. 

Try toe yoga, arch strengthening and calf work. Good luck mate
[ggfcapd] (score 2, diepte 0) I struggled with Plantar’s for a while too. Honestly the thing that helped me recover was doing this one exercise every morning, and doing an ice bath for my feet after I ran (either immediately after or later). The exercise I did that helped was sitting on the edge of the bed when I woke up and doing the ABC’s with my feet, drawing each letter out with the end of each foot, one foot and one letter at a time. Definitely worth trying out, good luck!
[ggglrmc] (score 2, diepte 0) To be honest, the only way I recovered from it was to stop running altogether for 6 weeks (while on holidays) and it was fine when I started running after that.
[gzoqi8y] (score 2, diepte 1) Late to the party here.  I started having issues about 2 years ago.  I can't remember how much time I took off, but things eventually got manageable.  It never really went away 100% but eventually it go to the point where it wasn't really a bother.  Since getting out of Covid lockdown I've been running more than I ever have in my life, and without a single week off (so that's been about 11 straight months or so).

The pain has been slowly creeping back up but it wasn't until 10 days ago that I realized, yep, I've gotta take a break.   I was hoping to be back in action after 1 week... nope.  was hoping 2.... probably not.  Now thinking maybe 4 will do the trick.

I can't really be bothered to figure out the exact cause... IMO it's just overuse and the best solution is just to give it a total rest, as you said, and if symptoms start appearing again then take another pre-emptive rest before it becomes a real issue.

I've been pretty active for the last 7 years, but running has only been the past 2 years or so, so I figured I'd ask around.  Do you have any thoughts on my plan? Based on your experience, do you think 4 weeks could be enough or would you recommend more?  Did you cross train or do any other exercise in the meantime?   Have symptoms ever come back for you?

Thanks if you see this.
[ggdwv84] (score 1, diepte 0) The theragun (percussion massager) really helps me. Focus on adductors, calves, and shins. I thought my PF would never go away, but I’ve been feeling lots better the last month since picking that up. Good luck!
[ggdyk0m] (score 1, diepte 1 OP) I actually got one a couple months ago. I don’t know if it’s been helping with Plantar Fasciitis, but it’s at least been helping with tightness in general (which may have relieved PF a bit).
[ggdzm4i] (score 1, diepte 1) Do you have any suggestions for how to get your calves? I feel like I have to contort into such a strange position to get a good angle on them that it's hard to relax.
[gge36vj] (score 1, diepte 2) I just sit in a chair and bend over and blast em
[ggel9m8] (score 1, diepte 3) Me too, or I sit on the ground and bend my legs and contort into strange positions. It’s cool
[gggog0z] (score 1, diepte 2) Lol toe yoga is an isolated PT exercise. I'm happy it helped you!
[gge593f] (score 1, diepte 1) That what I did and it worked. I waited to be pain free (2-3 weeks), then got use to walking with the inserts, then got back to running, with the inserts, really progressively. According to my foot doctor, my problem came from my plantar arches collapsing when I was running and it was damaging my fascia.
[gge3c4g] (score 1, diepte 0) Just to piggyback off this thread, does anyone have experience of running with PF? When I run I have pretty much no pain but then it feels slightly worse the day after... so I can run happily but have decided to take time completely off to hopefully recover quicker (which doesn’t seem to be working).

Basically I just want to know if anyone has experience running with it, as my physio has said I’m okay to run aslong as the pain stays below a 3
[ggfpby5] (score 1, diepte 1) I ran through PF. It didn’t hurt bad during runs, it was after that was bad. I started wearing Oofos pretty much anytime I’m not running and that cured me.
[gggout7] (score 1, diepte 1) PF is a tendon problem. Rest makes it feel good for a bit, but will never solve the problem. It needs load, preferably progressive overload at a low level of discomfort. Usually tendons warm up and feel better after starting an exercise. Your physio is right that pain under a 3 is ok.
[gggtb7c] (score 1, diepte 2) Yeah I have a lot of physio friends saying I need that easy load on it... I’ve started run walking just to give it a little bit! It’s just nice to hear some other stories where people have had similar issues and came out with a similar method
[gzoqydc] (score 1, diepte 2) Hey there, late to the party but figured I'd ask.  My foot pain (assuming it is PF) started about 2 years ago.  I was kind of babying it for awhile but eventually just got back into activity at some point and everything seemed to be fine.

Unfortunately I've been going really hard for the past 11-12 months without any rest, and symptoms have started to pop back up.  Last week they got pretty bad so I realized I needed a rest.  It's been about 10 days now.  I'm thinking I'll continue to take some time off, but I wonder if it wouldn't be a good idea to start introducing some walking and then light running back in.  Any thoughts?
[gzp9w2w] (score 1, diepte 3) Not really, unless you're a patient seeing me via telehealth or in the clinic. There are too many variables with the answer being 'it depends' to give advice to strangers on the internet.
[gge7ivb] (score 1, diepte 0) I have a lacrosse ball I use to roll out my feet and some bands that support my arches that have a small insert and it’s been very helpful. I also find that when I was stretching everyday (back, legs and hips especially) I tended to have less pain, and the PF gets worse when I don’t do it.
[ggeajlp] (score 1, diepte 0) Definitely start using barefoot running shoes, your arch needs to strengthen itself and your big toe needs proper room to move, it’s likely big cushioned running shoes that force bad form that have caused it
[ggean04] (score 1, diepte 0) This is not a cure-all long term solution, but a TENS unit relieved me of my PF pain for the first time in about a year. Note that it relieved me of the *pain*, but the advice others are giving are more effective for treating underlying causes!
[iftusge] (score 1, diepte 1) wow that’s amazing. I can’t seem to find a good physio
[ggexsco] (score 1, diepte 0) Similar to another post, I visited a physical therapist about my chronic planar fasciitis. I got exercises and a couple stretch adjustments that have helped when it's flaring up and seem to be a bit preventative when I am remembering to do the exercises
[ggff5l3] (score 1, diepte 0) Stop stretching for a bit to ease the tension on your fascial tissue. Once it subsides, really focus on strengthening - weighed lunges, squats, power cleans, plyometrics, and heel lifts. You want hips, back, glutes, and calves to get tuned up, coordinated, and strong.
[ggfflli] (score 1, diepte 0) I struggled with this for years. Best thing I ever did for my running was to buy a hypervolt and now I go to town on my calves every evening. It's a game-changer.
[ggfg689] (score 1, diepte 0) Dealt with this for almost 2 years and did alot of foam rolling, stretching etc.  The break through that made it go away and got rid of the tight calves was a week of slower trail running.  Everything loosened up and felt good so I started running beside the pavement whenever possible.  I am convinced that the small variabilities of foot strike angle spread the impact more and are what are allowing me to run and recover pain free.
[ggfjrxt] (score 1, diepte 0) Have you been to a Physical Therapist? A Physical Therapist is the best person to solve this problem. Many also specialize in running.
[ggfmoae] (score 1, diepte 0) Stretching and scraping. It sucks pretty badly, but does the trick for me.
[ggfqzyw] (score 1, diepte 0) Switch to a forefoot strike.  Find a zero drop shoe and start back from the ground level.  Years ago I used to get the standard running injuries (PF and the like) a few times a year.  I switched to a zero drop shoe and a forefoot strike and the only time I get injured is just from overtraining.  If you decide to do this you are going to have to go short and slow for a while and build up over the next few months, but you’ll be left with claves of steel and won’t have to deal with this again.
(8 reacties met lagere score weggelaten)

=== THREAD 380c6s ===
SUBREDDIT: r/weddingplanning
DATUM: 2015-05-31  SCORE: 13  REACTIES: 68
TITEL: Show us your wedding shoes! Colorful, sparkly, any adorable shoes!
POST (source_id=post):
I know it's been asked before but let us see what your feet will be modeling on your special day! We can never get enough shoes. :)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[crrabzv] (score 11, diepte 0) http://m.imgur.com/AuGFIKO

These are mine!!!
[crr96m8] (score 8, diepte 0) I'd like to see flats! I need to find some for my white ballgown dress :)
[crrcv1f] (score 7, diepte 1) I just posted this in a separate comment, but mine are flats. :) http://i.imgur.com/O28Mz4P.jpg
[crrayzw] (score 7, diepte 0) [Mine!](http://www.irregularchoice.com/shop/xhr-list/product/6244/just-pawed.html#/)
[crrfzts] (score 7, diepte 0) I've posted them before, but [here](http://imgur.com/Vtj55ON) they are!
[crrixth] (score 7, diepte 0) As a short gal who loves sparkles, mine are 5.5 inch heels and I absolutely LOVE them! I know it's not for everybody but I'm excited http://imgur.com/3pLTKZ3
[crr93i4] (score 6, diepte 0) http://www.dillards.com/product/Antonio-Melani-Nadelle-Platform-Jeweled-Dress-Sandals_301_-1_301_504245032

SO EXCITED about these shoes.
[crr9re1] (score 6, diepte 0) [mine!](http://imgur.com/X6VLW8E)
[crreeat] (score 6, diepte 0) http://www.rocketdog.com/flats/raylan-pretty-petal/invt/raylanpp
Definitely not as pretty as some of the others on here, but I love them!!
[crren11] (score 5, diepte 2) I wouldn't buy them from the people I did as they shipped them terribly in a bag not a box Which lead to the heel support on one to buckle as it was squashed in transit. They only offered me a 10percent discount for the damage sayong it will bounce back in a few days. A week later and the heel still buckles as I walk. Not enough that I can't wear them but it is annoying

I bought them online from Aliexpress.com.  the seller I bought from specifically was CHINA-FASHION WHOSALES STORE. Don't buy from them but there was like 20 other stores that sold these exact shoes in 4 different colours.
[crravsz] (score 5, diepte 0) These black and silver wedges (they sparkle way more in real life): http://www.dsw.com/shoe/italian+shoemakers+sage+wedge+sandal?prodId=165541&productRef=SEARCH
[crrdakl] (score 4, diepte 0) I might get something with some heel for the ceremony, and keep these for later... but currently, [these are mine](http://imgur.com/a/t3Khp)!

[And the link to the shoes on modcloth](http://www.modcloth.com/shop/shoes-flats/confection-perfection-flat-in-mint)
[crracly] (score 3, diepte 1) Omg kitties!  I love them!
[crra084] (score 3, diepte 0) I want sparkly sneakers... don't have them yet though
[crrcujr] (score 3, diepte 0) http://i.imgur.com/O28Mz4P.jpg

These are mine. They're a tad too small, but that's okay. :)
[crriczn] (score 3, diepte 0) http://www.foxtrotlawrence.com/collections/women-heels-wedges/products/fish-pump
They are literally made of tilapia leather. FISH LEATHER. 

And my dancin' shoes:
http://www.modcloth.com/shop/shoes-flats/on-second-trot-flat-in-sunshine
[crrj2o0] (score 3, diepte 0) Here are mine! I originally wanted something with color, but I loved these! 

http://www1.macys.com/shop/product/menbur-belen-evening-pumps?ID=1813162&CategoryID=13247&LinkType=#fn=PAGEINDEX%3D2%26sp%3D2%26spc%3D33%26slotId%3D25%26kws%3Dmenbur%20evening
[crrkc1y] (score 3, diepte 0) I wore these in blue!  So worth the cost,  although I only paid half of what Nordstrom is charging for them :) http://m.shop.nordstrom.com/s/badgley-mischka-jeannie-crystal-trim-open-toe-pump-women/3780104?origin=category&BaseUrl=Wedding+Shoes
[crrpew0] (score 3, diepte 0) I am blessed with a husband the same height as me, so I got to wear [these flats at my wedding.](http://www.debenhams.com/webapp/wcs/stores/servlet/prod_10701_10001_050010460221_-1)

One of my bridesmaids, however, completely killed it. I wanted to borrow her shoes all day. She wore one of these designs: http://www.irregularchoice.com/shop/womens/list/shoes-59/
[crs2e8a] (score 3, diepte 0) Check these gorgeous shoes of mine out. Seriously excited about them!

http://www.irregularchoice.com/shop/xhr-list/product/6637/i-do.html
[crsew10] (score 3, diepte 0) Mine! Probably going to get a pair of lace toms in the same color for the reception! http://i.imgur.com/PaYLldC.jpg
[crrdhni] (score 2, diepte 3) Yoox.com, but there's none left. :/ I'm not sure what the actual brand is.
[crspgih] (score 2, diepte 2) Your shoes are rad... but I'm upvoting for your tattoo.
[crsz293] (score 2, diepte 3) Haha, thanks. :)
[crrd8m1] (score 2, diepte 1) Awesome. I need some wedges since I'm getting married on the grass... where'd you get them?
[crrierj] (score 2, diepte 1) props on the HP tat :)
[crriwrl] (score 2, diepte 2) Thanks :3
[crrg0b9] (score 2, diepte 1) I love the lace! So pretty
[crrh7v9] (score 2, diepte 0) [Sparkly kate spade!] (http://m.katespade.com/sala-heels/S741531-1%2Cen_US%2Cpd.html?dwvar_S741531-1_color=670&cgid=ks-shoes-pumps) 
I hate heels, these are relatively comfortable for heels. I am sure they won't stay on all night, however.
[crrizam] (score 2, diepte 1) Super cute!
[crriv9l] (score 2, diepte 1) I love the fish skin it looks so cool!  I hate heels though. I have been ogling those mod cloth shoes but I just wish they had other colors besides yellow and orange
[crrkfmm] (score 2, diepte 1 OP) From another short gal, I need these! ♡
[crrkkij] (score 2, diepte 2) Super comfy!  I walked around the bumpy city streets for two hours before the wedding in them for photos and could have worn them all night if I wanted to (switched into flats for half of the reception). Just make sure to break them in before!  Also,  I found mine on sale at Saks 5th off 5TH outlet for like $125, so definitely shop around.
[crtmewt] (score 2, diepte 4) My dress was slightly shorter in the front so it wasn't an issue at all. [Here's what it looked like with heels on.](http://i.imgur.com/yDjCjif.jpg)
[cru4fe1] (score 2, diepte 6) Yes that is horizon from DB.
[crrpjum] (score 2, diepte 0) Badgley Mischka, I love them!!  http://www.badgleymischka.com/JAZMIN/
[crrtmr9] (score 2, diepte 0) I'm late, but these are mine! $36!!

[shoes!](http://a3.zassets.com/images/z/3/0/1/4/3/9/3014399-p-MULTIVIEW.jpg)
[crrv85a] (score 2, diepte 0) [left- ceremony shoes, right- reception shoes](http://m.imgur.com/account/meeanne/images/t4mnPpZ)
[crry3gc] (score 2, diepte 0) http://shop.guess.com/en/catalog/view/gwadabelle3 These are mine! The best part was that they were my first choice and I got them for half price! yeeeee!!!
[crryvsg] (score 2, diepte 0) [My hi top Converse!](http://i.imgur.com/TvVYucr.jpg) My dad absolutely hates that I'll be wearing them and keeps telling me how much I'm going to look back and regret it. But I am not a "fancy shoes" girls and these are so perfect for my personality. Not to mention, they are insanely comfortable!
[crs1cj0] (score 2, diepte 0) http://imgur.com/xn8D7gU these are mine!
[crsjnqe] (score 2, diepte 1 OP) I am in love with these!! The color is amazing. I'd wear them in every day life!
[crsklqd] (score 2, diepte 0) These are mine, so comfy, & photographed really well. I got both in the blue options. 

[reception shoes](https://www.katespade.com/willa-flats/S115002,en_US,pd.html?dwvar_S115002_color=122&cgid=ks-shoes-flats#start=5&cgid=ks-shoes-flats) 

[ceremony shoes](https://www.katespade.com/sala-heels/S741531-1,en_US,pd.html?dwvar_S741531-1_color=670&cgid=ks-shoes-pumps#start=33&cgid=ks-shoes-pumps)
[crttzvn] (score 2, diepte 0) I'm wearing [these](http://productshots2.modcloth.net/productshots/0144/2659/2bb59e73541571dca52ab6a23aabe0ca.jpg?1404767266) for the ceremony, then rocking orange hi-tops with grey laces for the reception. FH will wear nice shoes for the ceremony, then grey hi-tops with orange laces for the reception. Woohoo!
[crtvfx8] (score 2, diepte 1 OP) Those flats are adorable! Love the ankle ribbon! 

High tops for the win after!
[crtwn52] (score 2, diepte 1) Those are absolutely beautiful! Where did you get them, if you don't mind my asking?
[crskoq8] (score 1, diepte 1) Ooo I thought about sparkly sneakers! Kate Spade has some great ones, they come in blue on other sites and a few other colors [sparkly sneakers](https://www.katespade.com/keds-for-kate-spade-new-york-glitter-sneakers/S287693GF,en_US,pd.html?dwvar_S287693GF_color=100&cgid=ks-shoes-sneakers#start=10&cgid=ks-shoes-sneakers)
[crtwkml] (score 1, diepte 1) Do you have a floor length dress? I'm wondering how it works with a long dress, switching between heels and flats - does the dress drag in the floor when you're in flats/look just slightly shorter than it should be when you're in heels?
[crucc4k] (score 1, diepte 2) I have no idea... I haven't thought this through.

I do have a floor length dress.
[crrphny] (score 1, diepte 1) I love these!  I very nearly got them myself!
[crtwlv1] (score 1, diepte 1) Is your dress floor length? I love love love your shoes but I'm wondering how switching between heels and flats works for the dress. I'd love to plan to switch to flats but I'm having a floor length dress so I'm concerned I'll be tripping and dragging all over my reception!
[cru8juk] (score 1, diepte 2) Mine is tea length, so I won't have to worry about that. 

Are you bustling your dress? I'm not sure how a bustle effects the actual hemline, but maybe it'll work! Otherwise, you can buy gel insoles for heels, and they are awesome!
[crua8ii] (score 1, diepte 3) Oooh I didn't think of a bustle potentially affecting the hemline, I'll have to ask at the shop (I'm going to buy my dress next weekend!!) if there's a way to do that. Otherwise, I'll keep gel insoles in mind, thanks!
[crrq1sk] (score 1, diepte 2) They are from the Betsy Johnson wedding line, called the Wish pump. (The Star pump is also very similar) They have them at DSW but I actually ordered mine on Ebay for about half the price! Hope that helps! :)
[crrkh4t] (score 1, diepte 1 OP) I looked at these online today. How were they on your feet?? Comfy? I think they're adorable.
[crrlrnn] (score 1, diepte 3 OP) Thank you bunches, they sound great!! I'll go try them on tomorrow at Nordys and see how they do. I love the blue! It'll work perfectly with our wedding colors! Hopefully my tooties will agree.
[crsytdd] (score 1, diepte 3) How did it work for you with your dress length, switching from heels to flats? I really want to, but I'm concerned my dress will be too long and I'll be tripping my way through the reception!
[crtvi55] (score 1, diepte 5 OP) You ladies look amazing! The shoes look great. Blue totally works perfectly with your BMs. Are they wearing David's bridal in Horizon? ?
[cru50u6] (score 1, diepte 7 OP) That's perfect! My main concern was finding a pair that would match my lovely ladies dresses. I am going to keep my eyes open for shoes thay color. Again, you all look beautiful! :)
[cru5ams] (score 1, diepte 8) Look in unexpected places!  I just found hot pink shoes to go with my MOH dress for my best friend's (far left in the photo) wedding at Payless.  I never step foot in there because I always assume their stuff is low quality.  I also certainly didn't expect to find and be able to afford Badgley Mischka shoes for my own wedding until I stumbled upon them at the outlet mall!
[crtwjfo] (score 1, diepte 5) Ah, super cute!
[crsjtoy] (score 1, diepte 2) I have to hide them! I want to wear them so bad, especially this time of year, but they need to stay nice till my wedding next May :(
[crug6l8] (score 1, diepte 2) Modcloth! They match my dress perfectly.
[cru3hpp] (score 1, diepte 0) Late to the party, but I ordered [these](http://imgur.com/n840wqx) today, for my husband and I's second wedding in a few weeks. I wore black suede Dr. Martens to our first wedding back in November.
[cru4yob] (score 1, diepte 1 OP) Super cute! Love the patern.  Adorable for summer weddings :)
[cru59kt] (score 1, diepte 2) I thought so too! Just hoping that they are comfortable enough so I ask my husband for a dance around the midsummer pole. :)
[cruc2b5] (score 1, diepte 0) Haven't received them from China yet, so i'm hoping they're quality! For my deco theme. Thought about modcloth heeled oxfords, but they just weren't feminine enough for my liking. My dress is ivory so im hoping these arent stark white. 

Nice shoes everyone!!

http://www.amazon.com/gp/product/B00JUU9E26?psc=1&redirect=true&ref_=oh_aui_detailpage_o00_s00
[ct0hdc3] (score 1, diepte 0) http://www.redkilim.com are one of a kind colorful shoes made with kilim and leather.
[crrd9jc] (score 0, diepte 2) UH LOVE THESE. Where are they from?

=== THREAD 6lo7e1 ===
SUBREDDIT: r/weddingplanning
DATUM: 2017-07-06  SCORE: 41  REACTIES: 68
TITEL: Bride spends 5k on wedding shoes but is making bridesmaids paying for the brunch. Need advice.
POST (source_id=post):
First of all, I'm not suggesting that someone shouldn't spend 5k on their wedding shoes.. so one of my partner's best friends from childhood is getting married this summer, they are throwing a big wedding and my partner is going to be a bridesmaid for the wedding.

For the wedding, all the bridesmaids are buying their own dresses, I'm from a foreign country though I know that's not uncommon in America but the dress the bride picked costs about $400. Me and my partner are both in our early 20s and are in no position to buy a dress for $400 that will never be worn again. 

In fact, we never spent $400 on any clothes we own, ever. It took my partner 5 paychecks save the $400 to buy the dress. She bought the dress because she doesn't want to back out and hurt their relationship. My partner did express her financial difficulties to the bride but the bride didn't really seem to care.

My partner is the only bridesmaid doesn't live in the city at where the wedding's hosted. She will be taking 2 days off work unpaid to attend the wedding and it will be a 12 hours drive round trip. I will be taking a short flight and drive back with my partner. The bride didn't offer a place for my partner to stay (edit: not surprised but also did a little research, see [here](http://www.huffingtonpost.com/cheryl-seidel-/what-costs-should-the-bri_b_5340418.html). Luckily we have some friends there that we can crash with.

Recently we found out the bride spent $5,000 on her wedding shoes... and the maid of honor is asking all the bridesmaids and groomsmen to purchase a $30 customized wedding theme t-shirt for the pre-wedding events and is also asking a contribution of $30 for the bridesmaid brunch before the wedding which makes my partner really uncomfortable because we really can't afford this much to attend a stupid wedding that doesnt mean anything in the long run. The bride is also asking my partner to sing a bunch of songs at the reception...

I guess I wanted to ask you guys if it's normal for the bride to ask for this much? is this crazy or are we crazy? We will be spending about 1K+ to attend the wedding plus gifts. It's more than half of what we save from our income every year... 


~~I just think it's a lot to ask and me and my partner are not that kind of person. We only had a very small wedding, no reception, it was  just at the city hall with close family members. We were really broke at the time but we still paid for the lunch after our ceremony.~~ [EDIT: not relevant]

ugh


[UPDATE] this $30 brunch is happening at the bride's home where the dad is going to be making the brunch. WTF?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[djves1g] (score 101, diepte 0) I have nothing to say besides it all sounds awful. People might come in here and say "well that's to be expected", but I personally would be highly annoyed. You lost me at $400 dress. This is exactly why I'm letting all my bridesmaids pick their dresses from wherever and spend whatever they are comfortable with spending.
[djvf4b3] (score 63, diepte 0) > It's more than half of what we save from our income every year...

This is worrying.  In my opinion that's WAY too much to ask of someone, although in the bride's defense, she may very well not know what a big % of your savings that is.

Ultimately, it is up to you guys to make the call on whether this is financially feasible and financially worth it.  I would personally be appalled at spending more than half a year's savings on something like this.  The bride can ask what she wants, and you'll probably get varying opinions on whether it's a normal or fair amount, but in the end of the day the whole thing is your guys' financial call to make.  I'd evaluate this very carefully.  IMO anyone who is butthurt over you not wanting to trash your savings for the sake of their wedding is not someone you want to be friends with in the first place.
[djvfinh] (score 35, diepte 0) I think that your partner needs decide if being in this wedding party is worth it to her, and probably tell the bride she can't afford it.


Paying for your own dress and own travel/accommodations is pretty standard. I don't know about a "bridal brunch," but things like a shower and bachelorette party are often covered by the bridal party.


$400 is a bit expensive for a dress, but if it honestly takes 5 paychecks to save that, then a $250 dress and not paying the $60 for a shirt and brunch would probably still be a huge drain on finances.


It's likely that someone who spends $5k on shoes doesn't realize that $400 is a bank breaker for some people. If this is one of your SO's closest friends, do they have any awareness of each other's finances? Has your SO said that she can't afford this? Was there any discussion beforehand about what being in the bridal party entails? 


Whether this bride spent $5000 or $5 on her shoes, your SO has to look at the role and decide if it's worth it to her to be a bridesmaid.
[djvfyrc] (score 31, diepte 1) > I mean even Loubs, Pradas, Manolos, Choos, etc usually max out at around a grand or so.

Basically, just add stuff to it (beads, or [rhinestones](http://us.christianlouboutin.com/us_en/shop/women/dorothy.html)), and/or make it out of exotics.  

That being said, I'm having trouble finding much above $4k that's not a boot.

Edit:  Well now that I'm looking for $5000 shoes, all these $1000 shoes are starting to look cheap!  This was a terrible idea.
[djvg47e] (score 29, diepte 0) I had to spend over $1000 as a bridesmaid once and it made me so resentful I am no longer friends with the bride. I was afraid to back out of being a bridesmaid, but I wish it had because it may have saved the friendship.
[djvf4tv] (score 27, diepte 0) I'd say a $400 bridesmaid dress is beyond the realm of normal. People I know grumble at anything >$200 and I personally tried to (and did so successfully I should add!) keep my budget under that amount. 

$30 for a t-shirt I'd say is pretty normal. I paid for one for my friend's bachelorette and my husband has paid for a few for some bachelor parties. 

$30 for brunch seems like a LOT - I guess maybe if booze is included it's not terrible but I live in SF and even I am able to keep my brunches under $30. 

$1k all-in for two people travel to and attend a wedding  where one person is in the wedding is actually not too bad (which I know seems nuts but if you have to travel at all it really adds up). Between flights, accommodations, gifts and BM expenses I usually plan to pay around that if not more for just myself -- if my husband comes as well it nearly doubles.

Singing a bunch of songs at the wedding is really presumptuous - she's not paying your partner I assume and she should be treated as a guest, not a vendor. 

Also WHAT SHOES COST FIVE GRAND? I mean even Loubs, Pradas, Manolos, Choos, etc usually max out at around a grand or so. Are they encrusted in diamonds?

Overall, yeah sounds like this bride is really asking a lot out of you - especially since you both have expressed your financial troubles. I'm sorry that you're going through this and would suggest maybe reconsidering what you're getting out of this friendship after the wedding is over. Some people go crazy for weddings, for others it just amplifies poor personality traits (e.g. entitlement) that already existed.
[djvmtoc] (score 25, diepte 0) This is hard. And I'm going to be no help.

But yes, it's normal. A $400 bridesmaid dress is a something that seems like a very reasonable ask to a bride who spends $5k on wedding shoes. And yes, it's crazy.

Your edited paragraph is actually relevant. This is America's income inequality problem. The people who buy shoes that expensive actually don't understand how their requests are out of someone's budget. They think they do, because they have likely worked hard to get where they are, but they don't get it as much as they think they do.

I know. I'm marrying into a family with much MUCH more money than my own. Both families describe themselves as working/middle class. But my parents own a small Mom&Pop store in rural America. Her family members own law offices and medical practices in major cities. We both refer to these as the "small family business." Everybody works hard, but the harsh reality is that the $200/night rooms at the reception hotel are "a FABULOUS deal--thank you!" to one family, and "kinda pricey, but we can stay there if you need us to" to the other family. I had to explain that making the dress code black tie would actually be a difficult thing for my family, and my FMIL laughed and said they were really laid back and casual and no one would care if people wore tuxedos from 10 years ago. No one in my family owns a tuxedo and only a small handful rented them for prom. My FMIL is a sweet and truly generous woman who would be mortified to know this and would then immediately offer to buy everyone designer tuxedoes and gowns, which would then mortify my family, and well, anyway, you get it. Everyone is loving, but the gap is wide.

This bride doesn't know that she's asking such a big thing from you and your partner. Your partner can have a quiet, private conversation with her again and explain just what you said here about how extremely difficult the money part of the wedding is. Be explicit and blunt, despite the awkwardness. She likely thinks that "financial difficulties" meant you skipped date night once or twice to buy the dress, not saved for months. If the bride offers to pay for something because your presences are the primary important things, let her. We're quietly paying for some of our guests. Talk to the maid of honor too and say you're past your limit and you really can't be surprised with any new wedding expenses. As MOH, I've picked up the cost for bridesmaids too.

The bride may never get it. That's okay too. If nothing else, I see your sacrifice.
[djvim47] (score 17, diepte 3 OP) > Found 'em


lol this is the one:
https://goo.gl/T6VwNt
[djvfbuo] (score 13, diepte 1) > Also WHAT SHOES COST FIVE GRAND? I mean even Loubs, Pradas, Manolos, Choos, etc usually max out at around a grand or so. Are they encrusted in diamonds?

I am also curious about this!!! Maybe an exotic material?  That can really spike designer shoe prices.
[djvhvv5] (score 13, diepte 3) In the interest of being respectful, I'll just say they're not to my personal taste. 

Snake chain... I was close.
[djvfcel] (score 13, diepte 0) So literally the only thing here that i would say is normal is not offering you a place to stay. We arent covering anyones accommodations we just got them a block rate at our venue hotel $129 a night.

but $400 for a dress is insane... none of my girls are spending more than $120 and they get to pick their own.

I will say though that standing up in my brothers wedding was about $900 and i didnt need accommodations, that was local to me. and attending not even being a bridesmaids in my friends wedding was about $1000 after gift airbnb and hotel and flights / ground travel (im in the midwest this was in maine)

So i think weddings are expensive no matter how helpful or not the bride is with cost, especially if you need to travel
[djvhrvk] (score 10, diepte 2) [Found 'em](http://www.barneys.com/product/christian-louboutin-espelio-zep-platform-wedge-sandals-505129659.html)
[djvtvm3] (score 10, diepte 5) Here, I'll save you $4,539
LizForm Women Sparkle Wedding High Heels Glass Flowers Cinderella Dress Pump Silver 9.5 https://www.amazon.com/dp/B01N1NT2DW/ref=cm_sw_r_cp_apa_YWUxzbV6ZZ9J7
Edit: 
I found them cheaper
Williamsdd Cinderella Princess Crystal Shoes Glass Flower Wedding Shoes Evening Dress Heels Hot sell https://www.amazon.com/dp/B01M0UJRID/ref=cm_sw_r_cp_apa_t3Uxzb82957PV
[djvr88w] (score 10, diepte 1) I disagree about the shirts.  A bridesmaid gift should be a gift for the bridesmaid. As in a thing they might actually want.  I get that if you're giving them all the same gift it's not going to be customized to each girl's specific wants, but does ANYONE actually want a "Fling before the Ring" (or similar) tee shirt?

I hate this trend of "I'll gift you this shortie robe (which is really just a photo op for me, and is not actually a usable gift for you)"

EDIT: I do see that you said "part of." Sorry, I'm currently a super resentful bridesmaid, so I'm a little oversensitive.
[djvfauv] (score 9, diepte 0) Yes that sounds like too much. Your partner can definitely say no to doing songs at the reception, or say oh yes, I'd love to sing as your wedding gift (or, lol, tell her she'll do it at a rate of $400.) Is the brunch the morning of the wedding? She could just bring a sandwich and skip out of that too. I would definitely not spend $30 on a t-shirt I might wear once if it wasn't in my budget.    
I guess a lesson to be learned for next time--- back out as soon as the bride doesn't care about your dress budget.
[djvic8k] (score 9, diepte 1) > $5000 for wedding SHOES literally just deeply sickens me.

why do you care how much someone pays for their wedding shoes?
[djvisuk] (score 9, diepte 0) Those things all sound pretty standard for a US wedding from my extensive research (i.e. being on weddit). The dress is a bit OTT, but as someone up thread said if she's spending 5k on shoes she's unlikely to think $400 is out of order.
[djvm1qv] (score 9, diepte 0) I've gotten down votes in the past for holding this opinion so feel free to ignore it. 

What stuck out to me in your post was that you feel this is "a stupid wedding that doesn't mean anything in the long run". Your friend's marriage is meaningless? Ouch. If your partner shares that opinion, then it's clear to me you should not be putting this much money toward their 'stupid wedding.' 

I would think a discussion should be had with your partner's friend regarding your financial situation (maybe leave out the words 'stupid wedding'...) and if a compromise can't be made, you partner should bow out of the wedding party. I also think, from a brides perspective, it is likely too late for them to change the dresses that are being worn or the plans regarding the brunch, since other people have already purchased the dress and contracts have probably been signed with the brunch vendors. There are a lot of moving parts that go into planning a big wedding, so you may be SOL.

All that being said, it sounds like the bride is not being terribly thoughtful of how her choices might effect the bridal party financially. Sounds like her budget is quite large, so maybe she doesn't realize it. IMO $400 seems like a lot for a dress, especially if it requires alterations. The rest of the costs don't seem too extreme to me, but as with everything that varies from person to person and from region to region.
[djvf8i2] (score 8, diepte 1) I feel way less bad about my shoes now! But im also dying to know what 5k shoes look like haha.
[djvhs6w] (score 8, diepte 1 OP) wow thank you all for the replies..will finish reading all the comments in a bit. 

shoes info here if you're curious: https://goo.gl/T6VwNt
[djvijk1] (score 8, diepte 1) "I need to see these shoes" was my first thought as well.
[djvf6ie] (score 7, diepte 0) A $400 bridesmaid gown is definitely excessive, in my opinion. No matter how much the dress cost, though, the cost should have been discussed with the bridesmaids before the dress was decided upon. It's a bit of a sunk cost now, though.

If your partner doesn't want to back out, then that's that. She's well within her rights to say no to the t-shirt (WTF) and the bridesmaid brunch, but if she says no to contributing to the brunch, I would suggest not attending the brunch. Tell the bride you just cannot afford it. She can also definitely turn down singing at the reception! Maybe cite stage fright, or just not feeling comfortable. 

This definitely sounds like a big budget wedding. It's not crazy, but you're not crazy either. It sounds like you just have very different expectations and budgets--which is fine! You'll just have to be very clear with the bride on what you're comfortable spending. Keep in mind that she may expect your partner to pay for hair and/or makeup, which, again, your partner can absolutely say no to.
[djwcyzu] (score 7, diepte 1) > It's likely that someone who spends $5k on shoes doesn't realize that $400 is a bank breaker for some people. 

This is the issue I think, and the reason why I tell people who get asked to be bridesmaids to-- if they are concerned about finances-- try to get a sense about what kind of wedding this will be before they accept. If the bride is spending $5k just on her shoes, then that tells me her dress is probably 5k-10k as well, the venue is probably a pretty penny, catering isn't cheap (unless she is one of those kinds of people that would spend tons of money on her attire but have just finger sandwiches and soda for the guests), etc. While I think $400 is ridiculous to spend on a dress, it doesn't seem out of line with what kind of wedding this is :-/. Budget bridesmaid dresses unfortunately would look out of place. 

$400 is a sunk cost at this point. Paying for travel and accommodations is par for the course. Most bridal brunches I have heard of are paid for by the bride, but if the tshirt and the brunch are the only additional costs (e.g. No bachelorette party costs) then I would suck it up unless my friendship with this person was just over and done with.
[djvo7u0] (score 6, diepte 4) Ironically I'm looking for the exact right pair of lucite stripper heels to bedazzle into the same sort of Cinderella thing. But with clear heels.
[djvg1dt] (score 6, diepte 2) Designer snake-skin knee high boots encrusted with rhinestones?? Now I'm dying to see these shoes haha.
[djvfhht] (score 6, diepte 0) I think your partner really needs to have a heart to heart with the bride and express financial concerns. I think $400 dress is nuts, and the bride spending 5k on shoes is nuts. It is typical in the US to buy your own dress/shoes and pitch in for the bridal shower/bachelorette (which I didn't see any mention of in your post, so not sure if the bridesmaid brunch is in place of any of these). While I do think the amount being requested is a lot, what is being requested is normal -- if that makes sense. I do believe that if the bride isn't concerned about one of her bridesmaids finances getting in the way of attending the wedding then I would re-consider being a bridesmaid. I would highly suggest considering dropping out of the wedding at this point and trying to sell the bridesmaid dress (or returning if possible). Save the money and then send a nice wedding gift.
[djvtqhm] (score 5, diepte 3) Omg, I don't think I would wear these is they were $20.
[djvhnwm] (score 5, diepte 0) I think it's more the MOH asking her to pitch in for the bridal brunch and shorts, isn't it? It's pretty common for that to happen for pre-wedding events. However your partner is 1000% in her rights to say no and to also not attend these events
[djvizdz] (score 5, diepte 3) At that price point people are paying for design and materials (almost certainly exotics).  It's rude to assume that the only reason people buy high end luxury goods is to pad their egos and brag to people.  Most people who buy high end luxury goods do so because they genuinely enjoy them, and if you have the budget for something that makes you happy, why not?
[djvipn7] (score 5, diepte 1) How other people spend their money is really none of your business. 5k was a third of my wedding budget. So what? OP's friend could flush 5k down the toilet for all it effects me/you.
(38 reacties met lagere score weggelaten)

