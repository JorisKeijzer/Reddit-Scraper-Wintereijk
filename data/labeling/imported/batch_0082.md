# Label-batch batch_0082

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
Schrijf het resultaat naar `batch_0082.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 39ml6d, ze8138, 7spv3x).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 39ml6d ===
SUBREDDIT: r/ProtectAndServe
DATUM: 2015-06-12  SCORE: 197  REACTIES: 138
TITEL: So I had my first real foot chase.
POST (source_id=post):
Last night got into my first real foot chase. Guy just got done beating his girlfriend and also had multiple drug warrants. Get ready to cuff him and he takes off running. Chased him over 8 city blocks, lost him twice, but in the end we got him. Boy was that something. With only 6 months on i definitely learved a few things though:

*I do not tie my boots nearly tight enough


*after running two blocks and trying to watch his hands it is really hard to tell dispatch where you are

*bodycams are good but completely useless when it falls off ten feet into the chase

*two officers can see the same guy run in complete opposite directions

*thank god for homeowners who tell you he's hiding in his yard

*and finally, running 8 blocks with duty gear and boots is incredibly different then running in tennis shoes and shorts.

Just thought I'd include you guys in a fun adventure. Thanks for reading! Oh and so much paperwork....

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cs4r0id] (score 82, diepte 0) Did you say/yell anything when you caught him?

My first foot chase I kept yelling "why you runnin?" A la Will Smith in MIB.
[cs4lwha] (score 70, diepte 0) > I do not tie my boots nearly tight enough.

No one ever notices that their boots aren't tight enough until a situation like this happens lol. If they're not cutting off your blood flow, they're not tight enough.
[cs4p2cr] (score 51, diepte 2) In the words of chief wiggum, "id rather let a thousand guilty men go free than chase them down."
[cs4r9xe] (score 40, diepte 0) This seems like a nice time to reminisce about my first foot chase. As i followed the suspect he was a good amount ahead until he faced a really tall fence. He somehow scrambled over it but struggled and really slowed down. I caught up and before trying to jump the fence tried the gate door beside it. Unlocked. Opened it, caught up and win. 

Powerful lesson.
[cs4m77a] (score 36, diepte 1 OP) Pretty much things happen. That i attempted to use it and factors made it so that i couldn't. My department sees them as a tool that helps but not necessarily needed.
[cs4tvb4] (score 35, diepte 2) Those sound like the equivalent of velcro shoes for adults. Including their societal implications
[cs4m0n4] (score 32, diepte 0) > bodycams are good but completely useless when it falls off ten feet into the chase

What did your boss say?
[cs4y2qj] (score 31, diepte 1) Just found what I'm doing my first foot chase
[cs4npph] (score 28, diepte 0) Every other time running I throw a 15 lb weighted vest on.

Also, pace yourself, as the first officer, you just need to keep him in sight until backup gets there.
[cs4ozqv] (score 28, diepte 1) Chases are short.

Very rarely have I gone more than 100 yards or so.  If it's gone that long I'm probably not catching them.
[cs4pjry] (score 24, diepte 1) I have these "crazy boots" as my sgt called them last night, that are more akin to ski boots than patrol boots. They still get a decent shine but they have a twist lock instead of laces.

I get a lot of shit for wearing them but in chases they are always tight and I don't have to worry about laces catching on anything.
[cs4rlap] (score 21, diepte 2) Yet the benchmark to get hired is still being able to run 1.5 miles.
[cs4z1uz] (score 21, diepte 1) Then he blinked 2 sets of eyelids.
[cs4o6p2] (score 20, diepte 2) That's because everyone's too high to run where you are.
[cs4qv5h] (score 20, diepte 1) For a few seconds I thought, "man, he must have quick reflexes to end the chase in 10 ft!"
[cs4x7sk] (score 20, diepte 2) ayy lmao a dispatcher who's actually fit like me

#fitsquad #phonesquad
[cs4s4ha] (score 20, diepte 3) Well that's not because they care about how far you can run.  That's more to test your general cardio endurance so you can hold your own in a fight that might last a while.
[cs4m80t] (score 18, diepte 1 OP) Ha thats going to be my new rule now.
[cs4vw1i] (score 18, diepte 0) I had a door chase about three weeks ago. I have some 5.11 side zip boots that handled the chase well.

Burglary call at the very end of our shift, day shift was in briefing (of course). Went around back to help secure that side, house had a backyard that overlooked a dry ravine with a running path in the middle and steep rocky sides. Suspect comes out the back, starts to hop the fence, partner yells and identifies himself, meth kicks in and suspect takes off down the hill.

I take off after him trying to get to the smooth, flat path as quickly as possible. Get there, turn up the speed... suspect is so fast. Tweaker fast. Chase him about 1/4 mile before he runs up the other side, over a wall and into a backyard. Follow him over, he hops the wall to the front of the house, I go through the gate and lose sight if him. Other units are starting to setup a parimeter while this is going on. Ninety minutes later we catch him.

Property crimes detectives come out, we go home. I'm not primary, no paperwork. Lungs hurt and body is sore.
[cs4opjc] (score 17, diepte 0) To piggy back on your post, how the fuck do cops run for so long with all that gear on? Is it easier than it looks or are most foot chases fairly short?
[cs4uadp] (score 17, diepte 1) Work smarter, not harder? I learned that lesson long ago in retail.
[cs4tkmx] (score 16, diepte 1) Yup.  A 25 pound vest plus 45 minutes on the treadmill on an incline, and I'm toast. Of course, I fly a desk all day.
[cs4nnxm] (score 15, diepte 1) Damn. It took me YEARS to get my first foot chase.
[cs4yd22] (score 14, diepte 8) That fed money
[cs4ship] (score 14, diepte 0) >two officers can see the same guy run in opposite directions

LOL. So stressful when that happens, but so, so funny later on.
[cs4r0ar] (score 13, diepte 3 OP) Maybe 3inch by 3inch. Not positive
[cs4xrgh] (score 13, diepte 7) I have a big house
[cs4tl2o] (score 12, diepte 4) Yeah, I know, I just hate running.  I'd be one of those guys with the 0.0 sticker in my back window to annoy the people with 26.2 in their window.
[cs5298f] (score 12, diepte 3) Nooo dude the real suspect was the girl holding the geometry book
[cs4rc7t] (score 11, diepte 1) Departments don't PT test after academy. It's kind of sad. Fat cops are a joke IMO =/
[cs4tfg8] (score 10, diepte 1) Take your time, but be quick. Don't tackle. Never run in to a dark alleyway or jump a fence the same place where the subject jumped. Wait for backup (or at least wait until they're close). Never backlight your partner.
[cs4xkwu] (score 10, diepte 2) [Dispatch be like](http://wisequacks.org/wp2/wp-content/uploads/2012/12/zoen-047.jpg)
[cs4qxr2] (score 9, diepte 2) By the way, what size is the camera? It just occurred to me that I've never seen a police bodycam, just videos from them..
[cs4ut4x] (score 9, diepte 3) Now I just imagine you running after a patient who is refusing care.
[cs4u69n] (score 9, diepte 5) http://draftmag.com/wp-content/uploads/IMG_20130412_1844302.jpg
[cs4z5ak] (score 9, diepte 2) And... That's when I shot him, Chief! Ain't no alien gettin' me!
[cs512ta] (score 9, diepte 2) They were gills. He was out of breath.
[cs51xjb] (score 9, diepte 1) You outran a cephalopod? On foot? That's got to be tough.
[cs4mmnd] (score 8, diepte 0) Any advice? I don't know why, but I've been wondering lately how I'll do in a foot chase. Oh, and an exercise question. Just based on this, would you say it's better to work on sprints or distance running? I know it was only one foot pursuit, but that's one more than I've been in.
[cs4xmm9] (score 8, diepte 6) Over 500 feet to get a beer?
[cs4stmz] (score 8, diepte 1) Kinda a grey area. At the same time you want to have everyone in the best possible shape, you can't just fire them for being old or fat for a variety of reasons. Including but not limited to: workers rights, where is the line drawn and who determines it, how can you really judge who is fit for duty, how often certain depts actually are engaged in foot chase, do you have the ability to hire someone new, do you have the budget to pay for the old/fat guys pension prematurely while hiring a new guy, do you have time to even hire a new guy, hows the staffing going to work, etc etc.

There are some departments that have programs where for one hour a day you can get paid to work out, which is a win/win, but only if you can afford it.
[cs54fv0] (score 8, diepte 0) When I was new to the street, I used to chase everything. I rarely catch anything these days, but I still remember my first *foot vs car chase*:

We were on foot patrol of the entertainment strip in town, when a topless car with 3 males drove at speed and had to swerve and brake heavily to avoid drunk bar patrons on the road. I stepped out onto the road, and held my hand out to stop them as they approached. They swerved violently around me, and kept going on the wrong side of the road.

They had assumed that they were long gone, but I called it and started running. About 500 metres (1,500 feet) along I caught up with them, trapped in traffic at lights. They were not even looking for me. I ran out onto the road again and around the driver's side from behind, and before they even noticed I was there, I had removed the keys from the ignition and had the engine stopped. 

The rear passenger looked like he wanted to bail, but like the good citizen he was, he was strapped in by his seatbelt. Backup arrived before he reconsidered to chance it. 

It turned out the driver was drunk, and the car was stolen from interstate. He ended up staying longer in South Australia than he originally planned. The passengers were gang members, but we couldn't charge them with anything.

Now, I tell everyone who will listen about the time I out ran a drunk stolen V8 on the wrong side of the road - including you ;-)
[cs4wuir] (score 7, diepte 2) When you tie them, curl the toe of the boot upward so you get get them tighter.
[cs4n76k] (score 7, diepte 1 OP) It was only one but  lit was a combination of both. I'd sprint through a yard just to jog behind him for half a block.
[cs4s1si] (score 7, diepte 3) Paramedic here. Under armour valstez side zipper boots. Full size boots the weight of sneakers.
[cs4ovix] (score 7, diepte 1) On average mine havent lasted over 50-60 yards, im not a great runner, can't really do distance after I broke my knee when I was younger, but I have good reactions and can still put a good tackle in. plus we can usually tell when the suspects going to have you off and get on his toes.
[cs4rmeb] (score 7, diepte 1) If you want to know what it's like, have a midget bear-hug you from behind and wrap his legs around your waist, then try and go running through a neighborhood, jumping fences, etc.
[cs4yhtm] (score 7, diepte 2) "Dispatch I'm headed south on...standby..come on fatty give it up!"
[cs4ridc] (score 7, diepte 3) It's not uncommon for someone out of shape to be able to run really fast for a short period, especially with adrenaline kicking. But after it all wears off he's going to have a bunch of sore pulled muscles.
[cs4su4o] (score 7, diepte 1 OP) I know! Im telling dispatch he's in one place and another officer says he thought he saw him running over there. Im like no IM CURRENTLY CHASING HIM. Ha i was ticked when it happened but it was a good laugh after.
[cs4xxrf] (score 6, diepte 2) >Don't tackle

Give a little push and their forward momentum will take them to the ground, then you stop and cuff them.
[cs4wv8y] (score 6, diepte 1) It's a bit of both I'd say. And a lot of mental stamina too. You can train all you want, but at the end of the day you're running with 25-30 pounds of extra gear, big heavy boots... you're going to be a lot slower than most people.

But keep in mind that the guys who you're going to be chasing are shitheads...they smoke, do drugs, treat their bodies like shit. And they can run faster scared than you can angry. So that first little dash, they'll probably outrun you... but you need to just stick with it and keep going... as long as you have them in sight, you can run them into the ground, just don't give up.
[cs4pag8] (score 6, diepte 2) I was thinking about this recently. I'm an EMT and wear pretty heavy chippewa boots. I was running in them because I needed to go get some renewal from the DOT and I had work later that day. I realized that if I ever had to run for any reason for longer than a minute then my feet would be utterly destroyed.

So, what types of shoes do they let you wear? I always thought you were required to wear boots as LEO.
[cs50igq] (score 6, diepte 3) Hahaha. Phonesquad I love it.
[cs4sr03] (score 6, diepte 2) So strange that they don't.  Wildland fire is every year.  No fatties anywhere.
[cs53rhs] (score 6, diepte 1) That foot chase established Will Smith as the coolest dude ever to my 9 year old self.
[cs52uuw] (score 6, diepte 2) 5.11 is hit and miss. Some things are amazing, some things suck total ass.
[cs5fr8p] (score 6, diepte 0) First off, Good job on the arrest!


Not being a Dick, just asking:
What boring city do you work in? It took you 6 months to get into a foot chase? 

Here's a good tip for radio traffic (it was suggested by a vet to do it in mirror, I took it to the next level) while in a foot pursuit... When I was a rookie I had a tennis court in my community. I'm take my dog in there at night. I'd bring my handset with me and "chase" my dog. I'd call out description, direction of travel, etc. 

If someone walked by I probably looked like a retard, but it helped. By the time I got into my first foot chase (2 weeks in) i was golden.
[cs4q242] (score 5, diepte 2) That's what I was thinking. And every little bit helps after all. Many thanks.
[cs4njuu] (score 5, diepte 1) I switched from boots to professional looking, shineable sneakers for this purpose a few years back
[cs4z256] (score 5, diepte 3) I always forget how awesome the Simpsons is...
[cs4ujho] (score 5, diepte 1) Nike shocks? What country do you work in? Lol
[cs4ruy3] (score 5, diepte 3) You might have to catch Usain Bolt one day. You might be able to tire him out after a mile.
[cs4ps2f] (score 5, diepte 1 OP) Yeah i was told it was one of the longest my departments have had in a while.
[cs52i5t] (score 5, diepte 3) Keep in mind that WF is peopled by the young and the hungery. Also the crazy. Source: 13 seasons of humping a pack. (Reality check for the haters, since I hung up the keys to the big iron, and strapped on a belt and badge, I've never been more out of shape. Within two years my back went south and it is a bitch keeping my core strong when everything is out of allignment constantly. Sucks)
[cs5ac8k] (score 5, diepte 2) You see this?!  N-Y-P-D!  That means I will knock yo punk-ass down!
[cs51e4k] (score 5, diepte 1) > He's fast, tweaker fast!

I lost it.
[cs4z21g] (score 4, diepte 3) I did this once.  Dude slid like ten feet on gravel and mulch and was covered in blood. Actually had a bloodborne pathogen contact exam after because of it.
[cs4wuvg] (score 4, diepte 2) It amazes me to read when people say it was "years". I was in my first during my first week of field trading! Cannot even guess how many total over the years. Even several as a detective!
[cs54zec] (score 4, diepte 4) Seriously after a mile he is going to be at least another mile ahead.
[cs4x3oj] (score 4, diepte 5) there's a lot of different ways to be 250 lbs though.
[cs526fw] (score 4, diepte 1) I yelled "stop or I am going to Taze you!!!" 

They stopped on their face.
[cs52r0b] (score 4, diepte 1) Haha I yelled, "you're gonna need those legs when I catch you." Basketball trash talk got the best of me.
[cs4tp60] (score 4, diepte 0) Switch to shoes if you can. I like some of the black or dark gray New Balance cross trainers. I also ride bike though, so you might not be able to do that. Look up different lacing patterns online (quick Google can show you a ton of different options) for proper fit. There's even styles for boots for military regs (what I use).

Try practicing with your rig on. Obviously, you don't want to be running around outside with a rig and no uniform on, but if you can go to a private track or treadmill, it'll allow you to adjust your gear and the fit to be more comfortable when running.
[cs4zdjr] (score 3, diepte 4) The boots are censored
[cs4znk6] (score 3, diepte 3) They're made by a good company, and are department approved so that's good enough for me.
[cs55s2m] (score 3, diepte 5) [They are the Blauer, FW018 model.](http://www.blauer.com/clash-8-boot-fw018.html)
[cs4u4r4] (score 3, diepte 2) Got a link?
[cs5e6mz] (score 3, diepte 2) Navy guys often wear sidezips for just this reason, you can put them on in a hurry and they stay at the tightness you tie them at.
[cs4wx5u] (score 3, diepte 3) This is the one my brother in law said he uses. Not department issue, but he bought one of his own

http://www.amazon.com/Veho-VCC-005-MUVI-HD10-Handsfree-Camcorder-Control/dp/B004AP9FSE
(57 reacties met lagere score weggelaten)

=== THREAD ze8138 ===
SUBREDDIT: r/USPS
DATUM: 2022-12-06  SCORE: 191  REACTIES: 136
TITEL: I just stepped on this board with a nail through it. It’s pretty rusty. I don’t think it broke the skin but I moved my foot away in pain when I stepped on it. Should I tell my manager? They are probably just gonna get mad at me
POST (source_id=post):
[deleted]

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iz4urz4] (score 254, diepte 0) Tell them and get a tetanus shot if you haven't had one for some time.

Or, put it under the managers desk and wait for hilarious hijinks to ensue.

The choice is yours, good luck.
[iz598gc] (score 223, diepte 0) I cut my hand on a rusty mailbox and I told management and my sup came out grabbed all my mail and drove me to the hospital for a tetanus shot. But I guess all offices aren’t the same.
[iz5h1y6] (score 150, diepte 1) That’s a good leader right there. Rare.
[iz4y4bh] (score 148, diepte 0) Report it as an accident and get treated. Better safe then sorry.
[iz5d3ww] (score 109, diepte 0) Why does it matter if your manager gets pissed at you? The only thing you should worry about is your own safety.
[iz5rcin] (score 79, diepte 1) That's a sup I would give solid effort even when I'm not feeling it.
[iz52zx0] (score 55, diepte 0) Report that, and get a tetanus shot if needed. It’s a danger to anyone delivering there
[iz4wkk8] (score 44, diepte 0) Is this from their porch, and is the whole porch disintegrating this badly?  Refuse to deliver until they've either a) rebuilt the entire porch or b) moved the mailbox so you don't have to go up their shitty steps.
[iz5jtcu] (score 32, diepte 2) If you haven’t received your stipend it’s 100% on management. Report this and go to the emergency room if you aren’t up on your TDap.
[iz6at5v] (score 22, diepte 1) *than

It would be kinda weird to be safe then sorry.
[iz5evmc] (score 21, diepte 0) A CCA got fired at my station got stepping on a nail without proper footwear and got fired…

Union fought and lost. Be careful out there brother.
[iz5qpoe] (score 18, diepte 1) [My first thought](https://media.tenor.com/vYOVh5wLC64AAAAC/make-your-choice-jigsaw.gif)
[iz5xxfj] (score 18, diepte 2) Correct
[iz5fm8h] (score 18, diepte 1) Yeah, I’m still waiting on my uniform stipend they promised me I will get after 90 days as a CCA. That was in April lol
[iz60fl3] (score 16, diepte 1) Right? Wait til there’s a reaction and the supe is without a carrier for 2 weeks
[iz5k82g] (score 16, diepte 3) This is correct. There are no uniform requirements before you receive your allotment. As long as it's not an open toe your good go report it @op
[iz5etah] (score 14, diepte 0) Go get a shot if you don't and get tetanus it's fatal 10 to 20% of the time. Don't risk it.
[iz6brea] (score 13, diepte 1) Sounds like some of that small office hospitality.
[iz56vnh] (score 12, diepte 1) Damn that's some bad advice
[iz6brym] (score 10, diepte 2) But on the other hand, Safety First!
[iz6r7n3] (score 9, diepte 4) When I have an on the job injury, I want full medical documentation.
[iz66700] (score 9, diepte 0) I dont work for the usps, im a state employee however one thing i learned is to cover your ass. Document the injury, notify your supervisors and get it treated.
[iz5w23e] (score 6, diepte 2) If you were here in April, you're WAY past 90 days so why are you so yeah they might get mad and yell but if what you're really stressing about is getting fired it ain't gonna happen. What could happen if that injury isn't treated is you could get pretty damned sick. Get to ER or Urgent Care or wherever if you haven't already. I get so blasted pissed off as I read more and more stories like this where employees are more in fear of "THE BOSS" than getting treated for an illness or injury that should be your first priority getting taken care of. Is the job worth your life? Only you can answer that question.
[iz67fyc] (score 6, diepte 0) I only  read the first sentence and thought you wrote the customer a note in your own blood and stuck it to that nail at first...
[iz7z2u7] (score 5, diepte 2) I think reporting of all accidents is the definition of "safe then sorry".
[iz5eyii] (score 5, diepte 4) I mean you have a point there, but they might like to keep their job.
[iz6m49s] (score 5, diepte 1) Same when i fell and crushed/scraped my knee while attempting to dodge a pitbull attack minus getting a shot, i thought all offices did this
[iz8d985] (score 5, diepte 1) A lot of y'all act like we supes are literally Hitler. One of my carriers got chewed up pretty good. I got someone to finish his route and I drove him to the ER. I waited a bit but had to go close the office. I had to clock out but I went back and waited for him to be discharged and drove him home. 

I'm not saying that has a humblebrag. That's just the decent thing to do. This old guy had no family or close friends. He's my responsibility and he needed help. It's the golden rule. Easy to follow.
[iz641l2] (score 5, diepte 1) CCAs should never get fired for improper footwear when the allotment they get barely even covers uniforms
[iz647tu] (score 5, diepte 2) Welcome to the PO.  A lot shit that shouldn’t happen, does.  


Just file a grievance /s
[iz5prlp] (score 5, diepte 0) I hate to say it, but if you're wearing anything other than approved footwear, they can investigate you for being unsafe. Any time you might have a potential injury, even if you feel you can continue working, always report it. It creates a line of communication from the start in case you may need to seek treatment later on.
[iz6l04v] (score 5, diepte 2) I read on another usps post that they can get in BIG trouble for not issuing a uniform in proper timing( post was about a year in cca with no uniform)

Maybe they got you and you got them? If this makes sense?
[iz5eox6] (score 4, diepte 3) Dude who gives a shit if they get fired… they’d be dodging a bullet
[iz72yht] (score 4, diepte 7) I like discussion and trying to help out where I can. OP seemed concerned about the rusty nail but believed it didn't break skin. They should get a TDaP booster if they haven't had one in the last five years regardless of insurance or occupation for medical safety. 

The rest varies based on whether or not they sustained injury. If the OP has injury (visible, felt via pain, or both) they need to document the injury/disability/illness to the satisfaction of whatever allows them to take the appropriate benefit/disability/time off with USPS. That may or may not be an ER that gets them in and out quickly. Around here, the wait would likely be less for urgent care, and on many private insurances, the copay would be less on urgent care than ER on private insurance. On union insurance, that may not matter - my father is in a union and the copays for different types of services are pretty much equal.

There's a lot of variance, but the original post by bigdon802 mentioned going to the ER and getting TDaP if not up to date on a booster. I remarked that for TDaP alone, that an ER was probably excessive and the OP could likely get the TDaP booster easier and quicker at another site. Then bigdon802 mentioned the documentation for work related injury and I conceded that they had a good point.
[iz5lx5e] (score 4, diepte 0) This incident has the potential to infect you with Tetanus and create a serious workplace injury. It appears to have been caused by negligent maintenance practices on the premises of a customer. 

Why are you even asking?  From early childhood everyone should know that a puncture wound without a recent vaccination or booster requires immediate medical attention.  This incident is clearly an occupational injury.  Do our opinions about what you should do really matter to you?  Again, why?
[iz8h5lx] (score 3, diepte 1) Absolutely a safety issue. They can pick up their mail at the station.
[iz5tmr0] (score 3, diepte 5) Thank you!  I have waited years for a chance to deliver a proper Josey Wales quote. 

Dyin’ (or suffering a workplace injury without a paper trail), ain’t much of a living, boy!
[iz6y028] (score 3, diepte 1) he must have been new
[iz8dpnl] (score 3, diepte 2) Lol you realize this isn't the norm right? We do work for a lot of hitlers...
[iz8nr5b] (score 3, diepte 2) Yeah I got attacked by a customer once because I had to hold the mail since the locks were broken —apartment boxes. and my supervisor acted like I never told them. Then wrote me up for “not informing a supervisor of unsafe conditions” (after calling them & after writing up a report about getting attacked). I then got a 14-day suspension.

So. Yes. We work for hitlers.
[iz60v7y] (score 3, diepte 1) I have one on the knuckle of my right index finger from years of knocking on doors with packages.
[iz8gyqi] (score 3, diepte 3) Why? It's really not prudent to wait and see if you've got lockjaw before you get a tetanus shot. Treatment is much more expensive, both monetarily and time-wise, than a tetanus vaccine booster.
[iz6qabn] (score 3, diepte 3) Emergency room sounds excessive in this case, I asked my doctor about it after a cut and they said if the TDaP booster was in the past 5 years there was no need for action unless the nail/metal was particularly dirty or deep. If it wasn't within 5 years, the recommendation from my doctor was get a TDaP booster within 48 hours.

A lot of pharmacies do TDaP boosters and bill insurance - and the wait is typically less than an ER (especially these days with high COVID/Flu/RSV rates...)
[iz5o59a] (score 3, diepte 0) Hell yeah, document it. You might feel healthy now but you don't know how you will feel in a couple of days.
[iz5u0a0] (score 3, diepte 0) No I agree it's bullshit that they can fire a CCA for reporting an injury if they are on probation, but I've seen them do it. Consequently they also can fire said same CCA for not reporting it
[iz66pmy] (score 3, diepte 1) This is the way.
[iz7iknn] (score 3, diepte 0) You mean you didn’t look at your foot to see if it broke the skin?
[iz78aeg] (score 2, diepte 1) It's a workplace I jury. Doesn't it get covered by your company's worker compensation insurance and reported to OSHA? You're supposed to tell management and get a form for reporting the workplace injury within I think 24 hours.
[iz8za3n] (score 2, diepte 2) You report it immediately.
[iz86pf0] (score 2, diepte 1) I got rear-ended while stopped at a mailbox. My supervisor came out, talked to the cops, and then asked how long it was going to take me to finish the rest of my route. I wish I was joking.
[iz5a59m] (score 2, diepte 0) I stepped on a huge nail at home and was convinced I had blood pooling in my shoe. Went inside and I hadn’t broken the skin or even a scratch! This job gives us calluses.
[iz5w28y] (score 2, diepte 1) i’m still waiting for mine that i filed 6 months ago……
[iz5dq5n] (score 2, diepte 0) Too bad if the manager gets mad they’ll get over it!
[iz71p06] (score 2, diepte 6) Lol why are you weighing in on an employee discussion if you don't even know our job reqs, dude?
[iz7pbx9] (score 2, diepte 1) > proper footwear 

I'm just curious what they were wearing. I'm an RCA and the lowest tier footwear I put on are Redwing Irish Setter work boots.
[iz5xox0] (score 2, diepte 0) Report it! It’s gonna cover your ass to report it and get treatment than not report it and get disciplined or fired. Also reporting it gives you the potential for workman’s comp.
[iz5xv7b] (score 2, diepte 0) Bro you an idiot. Call the supervisor/Pm tell them your foot feels infected and is swelling you need to see the doctors right away. They are not medical professionals so they can’t offer you any “medical” advice. Tell them you want a ca17 and all those paper works
[iz60ak3] (score 2, diepte 0) You’d best report that and if anyone is mad, they have no heart or respect for you
[iz60uml] (score 2, diepte 0) If having your sup potentially be mad at you is more important than your life just walk it off I guess
[iz67gyo] (score 2, diepte 2) Snuck up on him, no barking. A little fucker did that to me too, mine only got the back of my shoe.
[iz6aaed] (score 2, diepte 1) That would’ve been awesome
[iz78a0b] (score 2, diepte 1) That's what I was seeing too 😂
[iz7za2s] (score 2, diepte 1) Yeah that's what I thought.  I was sitting here thinking how brutal that is.
[iz67i7a] (score 2, diepte 0) Report it and get a tetanus shot.  Mangers get mad?  That's their problem, not yours.  

ANY injury you get on the job, REPORT, REPORT, REPORT!  If the injury leads to something bigger, USPS has to pay for it.  

"If it's not on paper, it didn't happen"
[iz6a6v6] (score 2, diepte 1) Yeah, I’m pretty sure I got one recently. I think I’m just gonna try to walk it off. I didn’t pierce the skin and it would just make my day really hard tomorrow if I went home.
[iz6aafb] (score 2, diepte 2) As long as you’re sure you’re safe.
[iz6aijb] (score 2, diepte 3) Thanks man
[iz6knc8] (score 2, diepte 0) Will you be in trouble for walking through the yard instead of taking the walkway?


Or was no walk way available?


I can see the post office saying “we’ll you’re supposed to walk on the path to the door”
[iz74ewv] (score 2, diepte 0) ALWAYS report no matter how minor. My first aid instructor told us a story of a lady who got a small cut on her hand (or arm) at work but didn't report it & self treated. It got infected somehow with necrotizing fasciitis (flesh eating disease) and she lost her arm. There was no first aid report & she got nothing. It could've just been a scare tactic but I always told every employee under me to report it, it's never a waste of time
[iz781oc] (score 2, diepte 0) YES. If you get it later down the line there might be no way to prove it’s work related and you’ll be on the hook
[iz78krz] (score 2, diepte 0) Get a tetanus shot if you're out of date. The symptoms of tetanus are horrid. I got one after being mauled by a dog.
[iz80g96] (score 2, diepte 1) OP didn’t have time to check for a puncture. They had to hurry up and post this question. 😉
[iz63sls] (score 1, diepte 1) Never heard that
[izbh5pv] (score 1, diepte 3) Maybe you do but I dont
[iz8zilz] (score 1, diepte 2) Please transfer to my office.
[izbh216] (score 1, diepte 2) Your a good sup and thank you for your sacrifice because most sups are working 100+ hours ever 2 weeks I just don’t get why we are all at each other’s throats. We all have the same objective at the end of the day.
[iz5atbg] (score 1, diepte 0 OP) Workers comp
[iz7p657] (score 1, diepte 2) >supe is without a carrier for 2 weeks

So they'll actually have to do something then lmao
[izbzxkt] (score 1, diepte 4) I think you might've responded to the wrong person.
[izd5o2z] (score 1, diepte 5) I'm responding to the thread, and actually to everyone who commented on this subthread.
(54 reacties met lagere score weggelaten)

=== THREAD 7spv3x ===
SUBREDDIT: r/ProtectAndServe
DATUM: 2018-01-24  SCORE: 89  REACTIES: 118
TITEL: Teen refuses LAPD sergeant’s request to take her feet off of train seat - Cue outrage for police doing their jobs
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dt728ch] (score 114, diepte 1) "So we're gonna make these rules, but when you enforce them for us, we are just gonna make you the asshole."

-MTA
[dt6xsy8] (score 82, diepte 0) >The chief executive of the Metropolitan Transportation Authority on Wednesday said he was "extremely disappointed" by a Los Angeles Police Department sergeant's treatment of a young woman who was pulled from a subway train and detained because she refused to take her foot off a seat.

>"Our riders deserve better," Phil Washington said in a statement.

Seems the metro company has already thrown the sergeant under the bus, or train in this case.
[dt6kyyg] (score 55, diepte 0) There’s almost an impressive amount of stupidity on display in this video.
[dt76qxm] (score 55, diepte 2) "So there's no more rules then, got it. Gonna go play Xbox with the firefighters."
[dt6w5hn] (score 54, diepte 0) They kept saying, all these cops over her foot on the seat. After the foot on the seat, there was non-compliance, disorderly conduct and finally assault on a police officer. Fucking throw the book at people who spit on you. You know what kind of diseases you can get????
[dt6ok12] (score 44, diepte 0) What a bunch of idiots. Can’t just move a foot off a goddamn seat.
[dt70e7t] (score 41, diepte 1 OP) This job is dead.
[dt7njuh] (score 37, diepte 5) Can tell you're not a police officer. 

The escalation of an incident like this is entirely on the other girl. If a police officer asks you to do something, and you don't do it, do you seriously think cops should just shrug their shoulders and walk on?

Do you understand a police officer has a role in society, and if people are seen to just be saying 'no' and they do nothing about it, then the whole purpose of police is lost. 

>However, I'm not sure what's so hard about the cop pushing her foot down

Oh right and it would just be a case of push her foot down and that's it sorted? You're talking about an 18 year old that's so belligerant she's straight up ignoring the order of a police officer, and you think just moving her foot down is going to stop her from putting it right back up? 

You do not live in the real world, you do not know the kind of people that the police are dealing with.
[dt7318z] (score 37, diepte 0) >“This is racism!” the female witness shouted. “This is what we are! 2018, motherf*ckers like this just act like they can do whatever the f*ck they want. F*ck you guys.”

hahahaahahahahahahahahahaha
[dt6x74w] (score 32, diepte 0) What I can't ever seem to understand is what these type of people think will happen when you say "no" to the police. It's never worked out for the other people who've said it, why do you think it'll work now. Regardless of wether or not this brittle spirit will get in trouble, she just made her day that much more difficult by missing her train ride and having to be arrested. Hell you could have just done what the officer said and then put the foot back up when he leaves
[dt7759v] (score 32, diepte 0) *White supremacist cis-gendered male police officer denies young ethnic minority girl's freedom of travel as per the universal declaration of human rights*.

Retards thinking she was arrested only for having her feet on the seat. What's the other option? Walk away and set a precedence for everyone around that if you refuse, Police will give up and leave you alone? Do you see how that will go downhill quickly? 

Sad to see the agency throwing the Sergeant under the bus about the whole situation. It's an unfortunate time when we are sent into the grinder every day and things get hairy, we're dropped like a hot potato.
[dt7lt21] (score 31, diepte 3) Ask, tell, then make... the officer did his job correctly... the 18 year decided take the situation to another level where force is needed... Don’t blame the officer for doing his job...
[dt72v9r] (score 31, diepte 1) Officer discretion is him telling her to get her feet off the seat and not removing her at that point. 

The better question, is why not complying with a lawful order is ok. She made it the big deal, not the officer.
[dt76oot] (score 28, diepte 0) Why are police allowed to arrest people who break the law?
[dt785zk] (score 26, diepte 3 OP) That's my motto now.
[dt76j7o] (score 24, diepte 3) Or, and just hear me out, or he could do his job and in this case he did
[dt6v6of] (score 23, diepte 0) LAPD is wearing their hats? Shocking...
[dt70f6m] (score 23, diepte 1) I honestly want to know what goes through people's head when they think, "Someone has a tight grip on me...Imma spit on them and hopefully, they will let go."

What.
[dt7wzuo] (score 23, diepte 7 OP) Yeah that's basically what you are saying.  If she refused to comply, it either has to be escalated or the cop should just leave.
[dt6xg8a] (score 19, diepte 0) Kid has no respect for anyone anyways for having her feet on the head rest, fucking born in a barn
[dt72rrg] (score 19, diepte 1) The quoted comment annoyed me so much I nearly downvoted you. I'd say "our riders" deserve better than a metro company that prioritizes inconsiderate assholes over people that enforce the metro's own rules, but hey, what do I know?
[dt6qozh] (score 18, diepte 0) It looks like he was trying to avoid hurting her. It's not like he just ragdolled her out of the train.
[dt78saf] (score 17, diepte 0) He asked... nicely.. she said no.. he asked with more force. She said no. 

Ok... so you don’t want to follow the rules, but are angry the consequences happened?

.. the rule exists to maximize the seats available for others. So regardless of the law, just don’t be an asshole?
[dt6ynd1] (score 16, diepte 1) I PAID TO BE ON THIS BUS!! I CAN HAVE MY FEET WHEREVER I SO PLEASE, PIG!!!!!!!!!!!!
[dt7wxeq] (score 16, diepte 3 OP) > Cops pull this shit all the time

Doing their jobs?  Enforcing the laws?  Yeah I bet you hate it when that happens.
[dt75krr] (score 15, diepte 4) Mines eyes. Eyes stay in eye holes and in one piece thank you very much.


Would it help you to know I am actually missing two teeth from a fight. We found one of them and I think k I may have swallowed the other.
[dt72sby] (score 14, diepte 3) One of my biggest fears in all of Firefighting and EMS is seeing teeth scattered on the ground. Blood and broken bones? No problem. Teeth on the ground or embedded in a place other than the mouth they came out of? 

Fuck. That. Noise.
[dt704k7] (score 13, diepte 1) The amount of patience is equally impressive.
[dt7rsm4] (score 13, diepte 5) He didn't "open" an investigation. Patrol officers investigate minor issues every day. Confirming her information is part of that. 

Push her foot down? No. She can follow the rules or she can leave the train. If she refuses to leave, she can go to jail.
[dt7m8z7] (score 13, diepte 3) So should he just let her keep breaking the rules? Do you allow her to be defiant against police and act like it's okay to disobey a command? 

No, you grow up and take your feet off the seat like the 18 year old adult you are supposed to be.
[dt7360i] (score 13, diepte 1) Video says they're specifically looking to enforce "Code of Conduct" stuff right now.  Which is good.  Public transit becomes a shitstorm once people start ignoring the small stuff.  Broken Window theory and all that.  

Plus, it couldve been a simple thing... like  "Hey, can you move your foot off the seat please?  Thanks." 

What purpose does she have to be like "Nah".   I mean, hell, if anything, just do it, and when he walks away, put your foot back up.  What do you have to gain by specifically trying to oppose authority?
[dt6r7y4] (score 12, diepte 2) Can you explain how? I’m not familiar with the LA Metro’s rules but from what I read if she refuses to take her feet off the seat then she is suppose to be kicked off the train which is what this cop was trying to do.
[dt7x1gs] (score 12, diepte 5 OP) So he writes her a citation and then what?  You think that would have gone smoothly?  Wake up.
[dt82pbq] (score 12, diepte 6) The rules literally state that if you put your feet on the chair, you're going to get kicked off the train.
[dt7h3hp] (score 12, diepte 0) [So, I'm pretty sure that I found the Metro Code of Conduct](http://media.metro.net/about_us/ethics/images/codeofconduct_customer.pdf)

>Abuse and harassment of Metro representatives or patrons is prohibited in Metro
facilities and vehicles.

>A person must comply with all lawful orders and directives given by an authorized
Metro representative relative to Metro facilities or vehicles consistent with the Code,
including any instruction to leave a Metro vehicle or facility for safety reasons, for a
violation of the Code, or following a notice of ejectment or exclusion.

Aha!

I found the section of the Code of Conduct that I'm looking for:

>A person who violates the Code may be immediately ejected from the Metro facility or vehicle, without refund of any fare, by an authorized Metro representative who witnesses a violation. 

And yes, putting your feet on the seat is prohibited by the code of conduct. 

>“Stop!” she shouted, resisting with every step. “I paid to be on this train, a**hole.”

That doesn't mean Metro can't throw you off the train for not following their code of conduct.
[dt8ckc3] (score 11, diepte 6) How dare you speak facts and logical sense. Damn you to hell!
[dt6ro1o] (score 10, diepte 2) Had to break out your throwaway account for this comment, huh?
[dt725u1] (score 10, diepte 2) All I know is it's a damn good way of losing teeth
[dt7px52] (score 10, diepte 5) Firs off, it doesn't matter how small or what gender someone is. They can still fight and injure you or even kill you. 

She was asked several times to remove her feet from the seat and failed to comply. If he had just pushed her foot down she probably would have put it right back up. According the code of conduct policy he was enforcing he had the authority to remove her from the train. He was simply operating within the policies that he was given.

The officer iniated an investigation when he made contact with her in the first place. He tried to talk her out of it but she wasn't going to comply. He couldn't just walk away and do nothing. It's his job to do something.
[dt7mrmv] (score 10, diepte 2) There are no bad departments.  Just bad leadership.
[dt7celk] (score 10, diepte 1) On behalf of all the teens in the world other than that girl, thanks. We really love being lumped into one big group.
[dt797wu] (score 9, diepte 2) She actually said something to this degree -

>“There is no law that tells me that I cannot sit that way because I paid to be in there.”
[dt6qq2q] (score 9, diepte 0) Ahh, teenage angst.
[dt7o6pl] (score 9, diepte 0) "We've got your back. Except when we can get some public opinion points. Good luck with that." -MTA probably.
[dt73l6c] (score 8, diepte 4) Or opening someone's mouth to get an airway going and examining their oropharynx and finding loose teeth and pieces of teeth that you then have to pull out so they don't aspirate them.... *Shudders*
[dt739tv] (score 8, diepte 0) Hey sarge, get a freakin earpiece with a shoulder mic.
[dt7m1lm] (score 8, diepte 1) I'm assuming you're also ok with people assuming all cops are racist murderers?
[dt6saf3] (score 7, diepte 0) Man LA’s Metro sucks. They have a really weird jurisdiction issue. They should just reinstate MTA as law enforcement officers.
[dt7v89r] (score 7, diepte 2) Okay but it's so gross dude.
[dt782qg] (score 7, diepte 1 OP) Yeah why bother having laws.
[dt7aiem] (score 7, diepte 1) Because it takes one complaint of people hogging seats. Just like jay walking, we had a pedestrian go against a do not cross sign and get nailed by a car, now we are doing increased pedestrian enforcement and people are all butt hurt about it. It only takes one incident for enforcement to increase.
[dt6s13o] (score 6, diepte 2 OP) How do you equate enforcing the rules as doing whatever he wants?
[dt73zsd] (score 6, diepte 5) You can stop. Right there. No more. lol
[dt6y2z1] (score 6, diepte 1) Fucking assholes.
[dt77yl1] (score 6, diepte 1 OP) No kidding.  I can't believe that isn't policy there.
[dt7x2xn] (score 5, diepte 3 OP) Except Baltimore.
[dt7ml48] (score 5, diepte 3) Or she could just take her feet off the seat like a normal human being?
[dt7ylqb] (score 5, diepte 3) The reason LAPD/LBPD got the MTA contract back from LASD is because deputies were providing a minimal level of service. No presence on trains/buses. Minimal presence on platforms. They would mostly roll between stations in the black and white. Talking to the fare inspectors and MTA security guards the sheriffs would take their sweet time responding when they asked for help to kick someone out or for a crime in progress. 

This isn't a criticism of any deputies or even really LASD. I don't know what was going on with them internally or between them and MTA but I just know what I'm told by the conductors and current MTA security.
[dt74lsq] (score 4, diepte 2) Words are words when the guy already has a plan for them in his head. Just digging the hole deeper.
[dt82nh7] (score 4, diepte 1) They make us wear our covers for this gig
[dt7i6js] (score 4, diepte 1) Spitting on an officer is considered assault on a police officer btw. Probably the easiest way to get a felony on your record.
[dt7w6np] (score 4, diepte 1) Well the catch 22 is you can't do nothing if you expect to keep getting picked for the OT details. The system for getting details is supposed to be a lottery but it's an open secret that they have a blacklist of officers that they won't give details to anymore. 

The kicker is that MTA was encouraging coppers to enforce these "code of conduct" violations and the MTA supervisors wanted to see   that kind of activity on your log. We shall see how this affects upcoming details but I have a feeling that alot of coppers are about to get way less proactive. I guess the MTA wants the level of service the sheriffs provided (almost none) back.
[dt81bzz] (score 3, diepte 5) It's a misdemeanor and a really weak one by itself but it's your only option when someone just won't get out of your face. Most of the time the city attorney declines to prosecute it.
[dt7j9x1] (score 3, diepte 1) All the metro guys wear them. I think their OT detail
[dt7d3u3] (score 3, diepte 6) Give it time, you'll see it one day :)
[dtbrajm] (score 3, diepte 3) You don’t need to know someone to stick up for them. She picked the wrong battle, though.
[dtbunp7] (score 3, diepte 5) Cloud her judgement, emotions have.
[dt7vxfc] (score 3, diepte 1) The holy fuck... then change your goddamn rules.
[dt8keqo] (score 3, diepte 2) Why? It’s way less safe for a number of reasons. 

Honest question.
[dt7gorr] (score 3, diepte 0) California is so fucked. It's like snowflake land over there.
[dt8413i] (score 3, diepte 4) Thanks for that. 

Either the deputies saw the writing on the wall or were just lazy, either way, this is what the public fucking wants. I'd let it all go to hell, why should hard working LAPD guys risk their careers for doing their job and get punished for it? I don't see a reason.

It seems the public only wants a police presence when they shout "help, I've been [insert crime here]" and then gone the next second.
[dt809dp] (score 2, diepte 3) She was originally being taken into custody for 148 which is obstructing/delaying an investigation and while she was being cuffed she spit directly in an officer's face.
[dt81s23] (score 2, diepte 1) All of them? Like force lightning?
[dtacemi] (score 2, diepte 2) You can get flu, a cold, herpes, Hep B (maybe C too?) for sure. There's an extremely low chance of getting HIV from spit in the eye also because I believe it'd have to contain blood...but it's still not impossible. This is drilled into us where I work, and whenever someone is spit on in the eye we have to get full bloodwork done at the hospital, per policy there's a 2 hour window to start on HIV meds if you test positive. Yeah there's a small chance, but it's still present and better safe than sorry.
[dtbr5ky] (score 2, diepte 2) Everybody says she spit on the cop, the funny part is I don’t think she even knows the teen, she just saw an opportunity to cash in on some racial tension and police out rage
[dtbt6oh] (score 2, diepte 4) Exactly, it’s not sticking up for someone here, it’s a bullshit, opportunist martyr
[dtbr4ac] (score 2, diepte 1) Because these are the same people that think the world revolves around them and they have precious rights to do whatever they want, just like the assholes who think everybody should have a gun, regardless of mental health or criminal record etc., just because some moron decided two hundred years ago they should have a musket in their farmhouse, this allows them to carry a desert eagle under their jacket in case somebody cuts them off in traffic. What a world we live in.
[dt79myo] (score 2, diepte 1) Spoken like a true politician. Just a braindead idiot in a suit.
[dt7jo8e] (score 2, diepte 1) time to leave this dpt. if management doesnt support their officers, there's no way to do this job
[dt7mr09] (score 2, diepte 1) People ride the LA subway?
(37 reacties met lagere score weggelaten)

