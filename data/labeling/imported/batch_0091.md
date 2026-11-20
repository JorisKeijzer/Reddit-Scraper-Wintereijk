# Label-batch batch_0091

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
Schrijf het resultaat naar `batch_0091.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 7kcq4e, x5l7pz, 1kxemv4).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 7kcq4e ===
SUBREDDIT: r/Military
DATUM: 2017-12-17  SCORE: 4525  REACTIES: 1007
TITEL: In 2004, the USS Princeton & 2 Super Hornets encountered an airliner-sized object with “no plumes, wings or rotors” which hovered ~50 feet above the ocean, then rapidly ascended 20,000 ft, then rapidly out-accelerated the F/18s. Yesterday- the US DoD officially released footage of the encounter.
POST (source_id=post):
**Why this is significant**: this object was seen by a AN/SPY-1 (good track), AN/APS-145 (faint return but not good enough for a track), 4x pairs of human eyeballs, and 1x AN/ASQ-228. The AN/ASQ-228 footage has been verified as real and unmodified by the US DoD.

---

####**NYT Article A**: [2 Navy Airmen and an Object That ‘Accelerated Like Nothing I’ve Ever Seen’](https://www.nytimes.com/2017/12/16/us/politics/unidentified-flying-object-navy.html)

---

####**NYT Article B**: [Glowing Auras and ‘Black Money’: The Pentagon’s Mysterious U.F.O. Program](https://www.nytimes.com/2017/12/16/us/politics/pentagon-program-ufo-harry-reid.html)

---

####**Politico Article**: [The Pentagon’s Secret Search for UFOs](https://www.politico.com/magazine/story/2017/12/16/pentagon-ufo-search-harry-reid-216111)

----

####**Article from 2015** wherein former Navy pilot interviews one of the Super Hornet pilots: [There I Was: The X-Files Edition](https://fightersweep.com/1460/x-files-edition/)

(this article goes into *much more detail* than the NYT article)

(at the time this was obviously ignored because no DoD verification of the event)

----

####[**YouTube mirror of official video**](https://www.youtube.com/watch?v=DqNNXpgB2bw)

(video is officially verified by US DoD to be unmodified sensor footage from the Super Hornet)

While the footage is short, this is the first time that the US Government has ever released official footage of a UFO encounter, and the second time *any* government ever has (the first being [Chile](https://www.youtube.com/watch?v=qXiW3WooAiI&t=1m15s)).

---

####**EDIT**: [**leaked 2nd video**](http://www.extraordinarybeliefs.com/tic-tac-aav) showing near-instantaneous acceleration and deceleration near the end

(look at around 1:10, go frame by frame)

(and then, correct me if I'm wrong, but the object appears to accelerate so fast the AN/ASQ-228 can't pan fast enough to keep the lock?)

---

####**Choice Quotes (Article A):**

>“Well, we’ve got a real-world vector for you,” the radio operator said

-

>For two weeks, the operator said, **the Princeton had been tracking mysterious aircraft.** The objects appeared suddenly at 80,000 feet, and then hurtled toward the sea, eventually stopping at 20,000 feet and hovering. Then they either dropped out of radar range or shot straight back up.

-

>It was calm that day, but the waves were breaking over something that was just below the surface. Whatever it was, it was big enough to cause the sea to churn.

-

>Hovering 50 feet above the churn was an aircraft of some kind — whitish — that was around 40 feet long and oval in shape. The craft was jumping around erratically, staying over the wave disturbance but not moving in any specific direction

-

> as he got nearer the object began ascending toward him

-

>But then the object peeled away. **“It accelerated like nothing I’ve ever seen,”**

-

>the Princeton radioed again. Radar had again picked up the strange aircraft

-

>“We were at least 40 miles away, and in less than a minute this thing was already at our cap point,”

-

>**“It had no plumes, wings or rotors and outran our F-18s.”**

>But, he added, “I want to fly one.”

---

####**Choice Quotes (Article B):**

>Officials with the program have also studied videos of encounters between unknown objects and American military aircraft — including one released in August of a whitish oval object, about the size of a commercial plane, chased by two Navy F/A-18F fighter jets from the aircraft carrier Nimitz off the coast of San Diego in 2004.

-

>the company modified buildings in Las Vegas for the storage of metal alloys and other materials that Mr. Elizondo and program contractors said had been recovered from unidentified aerial phenomena

-

>**A 2009 Pentagon briefing summary of the program prepared by its director at the time asserted that “what was considered science fiction is now science fact,” and that the United States was incapable of defending itself against some of the technologies discovered.**

-

> He expressed his frustration with the limitations placed on the program, telling Mr. Mattis that “there remains a vital need to ascertain capability and intent of these phenomena for the benefit of the armed forces and the nation.”

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[drddsl6] (score 955, diepte 0) I dont understand why this isnt on headlines on the news or the top of the front page of reddit, this is huge.
[drdeq7m] (score 756, diepte 1 OP) It autoplays when you visit the New York Times homepage.

(for 24 hours they had it at the top, but now you just need to scroll down a little bit)

In general, I think the issue is that the ""UFO scene"" has been polluted by so much nonsense, lies, fakeries, and insanity that even when something credible *does* come up, people have already learned to tune it out.

I also think the general public just isn't aware how sophisticated the sensor suites on modern ships and aircraft are.
[drdf9l7] (score 557, diepte 0) Interesting how that footage got leaked, then taken down, then reuploaded.

How does one even sneak that footage away?
[drdej0z] (score 551, diepte 1 OP) My favourite quote from the entire event is:

>“I have no idea what I saw,”

>But, he added, **“I want to fly one.”**
[drde95n] (score 447, diepte 0) I don’t know what would make me believe these accounts, but it certainly wasn’t that footage.
[drdi2rw] (score 416, diepte 0) Has anyone bothered to search the ocean (floor) in that vicinity? Yes, I know what I'm asking. Good project for Clive Cussler...
[drdkrbo] (score 392, diepte 1) we need to activate James Cameron
[drdfbek] (score 333, diepte 1 OP) Yeah that sounds like a pretty big OPSEC violation.

But to be fair, if you had just seen what they'd seen, wouldn't you want to show the world and not have the footage end up in a deep dark vault of some 3 letter agency?
[drdhtua] (score 317, diepte 0) That's X-COM, baby.
[drdmejn] (score 313, diepte 0) My theory? This is a controlled leak, but not to us.  They just make it public so it's not an implicit threat. This is tech somebody has (U.S. or otherwise), that the U.S. wanted another nation-state to know about.  The country being leaked to probably already suspects this exists, but doesn't have proof.  

One of the pilots apparently believes that the target is an 'LNS' - whatever that may be. He also opens the video by saying 'This is a fucking drone, bro.' (The subtitles are wrong.)

**Edit for folks with child comments hidden:** “L&amp;S” is the intercept track being passed from the ship, not an acronym referring to exactly what they’re looking at.

My theory isn’t original. The U.S. famously did this by broadcasting a carrier transit through the straits of Taiwan to inform China without threatening them. ‘Oops, you saw that? On the TV? Oh, guess the secret is out.’

Wanted to add on that one reason I think this is a controlled leak is that what’s known as ‘annotations’ are still present on the video. That’s all the numbers with data about the platform, sensor, and target. Normally aerial footage is released without these to mitigate any reverse engineering.  The videos certainly *can* be released this way, but the declassification process is much more involved.
[drdj7a7] (score 306, diepte 0) I've always heard thay navy fighter pilots have a cool bro sound on the radio and I like to believe that the audio from this confirms it.
[drdgh8s] (score 302, diepte 2) That's how you tell pilots from aerial truck drivers.
[drdmpn3] (score 287, diepte 1) One of the most important parts of the job is to sound cool on the radio
[drdnlq2] (score 273, diepte 3) They are pretty sophisticated
[drder20] (score 273, diepte 2 OP) As a citizen of a NATO country, I think I'd prefer it to be extraterrestrial than to be from China or Russia, given the apparent capabilities described by all of the credible witnesses.
[drdlnij] (score 272, diepte 0) Holy shit.  I totally know one of those pilots.  I was an Aircraft director on the Nimitz from 03 to 07 and Cmdr Fravor was the CAG for our deployment in 2005.  He's an awesome guy.
[drdl66h] (score 243, diepte 3) But I'm super glad someone else did
[drdjgpc] (score 230, diepte 1) This was 5 years before Manning. My guess is that it was uploaded on sipr somewhere and someone put it on their hard drive and leaked it.
[drdegtr] (score 204, diepte 0) I just hope whatever is controlling that thing is human
[drdeaey] (score 202, diepte 1 OP) Read this article which was released in over a year ago (before this video was published and before the DoD said *anything* official about this event): https://fightersweep.com/1460/x-files-edition/

It gives significantly more detail.

Read up on the author of the article, and read the comments. Make sure to look up the credentials of all the service members involved.

Additionally, a while ago there was [leaked longer footage](http://www.extraordinarybeliefs.com/tic-tac-aav), which we now know is real because it matches the DoD verified footage. Look at around **1:10**, go frame by frame. You see the object accelerate then decelerate at a rate that simply no publicly known aircraft is capable of.
[drdjloe] (score 196, diepte 1) Why? Honestly watching the video I have no idea of what to make of it. Maybe to someone who used that equipment and is used to those visuals, this means something, but to the untrained eye it is literally meaningless.

I saw the video three times and still have no idea what the hell I just saw.
[drdpmxn] (score 191, diepte 4) https://imgur.com/a/Qrxuu
[drdhn1c] (score 175, diepte 4) Why take us out? Earth is only valuable in two resources we haven't found outside it yet. Chlorophyll and animal protein. They wouldn't be running fossil fuels, there's more gold in an asteroid belt than all of earth. There's really no point to come all this way just to one shot us.
[drdh960] (score 169, diepte 3) If it is really extraterrestial, we are fucked. If it is from another country, our race might still survive. Any alien species that can travel across the vast interstellar space will outclass anything that we can throw at them. We will be at their mercy and we won't get some inspiring speech like in Independence Day; we be dead.
[drdk1um] (score 168, diepte 0) At first I thought this was going to be the DOD releasing a fun video of Santa's sleigh for all the kids... Now I'm waiting for Independence Day to become a reality...
[drdgjyq] (score 161, diepte 0) I’m surprised this isn’t getting WAY more attention on Reddit.
[drdolcw] (score 160, diepte 5) They can detect oil tankers and cargo ships from _inches_ away!!!

&nbsp;

^^(By&#32;which&#32;I&#32;mean:&#32;if&#32;systems&#32;and&#32;protocol&#32;can&#32;screw&#32;up&#32;so&#32;bad&#32;you&#32;miss&#32;a&#32;700-foot-long&#32;ship&#32;turning&#32;into&#32;your&#32;beam,&#32;maybe&#32;they&#32;can&#32;also&#32;screw&#32;up&#32;so&#32;bad&#32;that&#32;you&#32;think&#32;you&#32;see&#32;little&#32;green&#32;men.&#32;The&#32;former's&#32;a&#32;tragedy,&#32;and&#32;the&#32;latter's&#32;a&#32;comedy,&#32;but&#32;we&#32;should&#32;be&#32;aware&#32;that&#32;both&#32;are&#32;a&#32;problem.)
[drdesi5] (score 153, diepte 2 OP) Did you actually read any of the articles or watch the videos?

This clearly is not just some conspiracy theory. This isn't Cletus telling his local paper that aliens stuck metal rods up his ass after he got drunk at the bar.

This is 2 radars, a FLIR camera, and 4 credible Naval aviators all reporting the same thing- and the first time *ever* the US government has confirmed such an encounter.

For the record: I did not believe in unidentified flying objects before this event (though I've always been curious), and see no evidence that it was extraterrestrial (more likely experimental aircraft- US or Russian, or a bizarre and rare weather phenomenon).

For the sake of personal comfort, I would *love* this event to be bullshit.
[drdqplc] (score 153, diepte 1 OP) Get him to do an AMA on reddit!
[drdnu45] (score 141, diepte 3) Da comrade, talking to internet friends of America your sensor suites. Can detect object shaped like Mikoyan MiG-35?
[drdkbnk] (score 135, diepte 0) Correct me if im wrong, but didnt the air force recently admit to purposely fueling UFO rumors to disguise US experimental flight technology?
[drdk9yc] (score 133, diepte 2) Yeah I'd rather not risk my career over a video.
[drdnp3z] (score 131, diepte 4) And modern
[drdlp1q] (score 131, diepte 3) (Not saying it's a UFO) But...it isn't the camera in this case. Look at the top of the screen, where it say 4*R at the beginning of the footage, and 8L near the end. That's the relative bearing of center of field of view from the sensor platform.  If the camera moves that number changes. For this to be a trick of the camera, the pilot would have had to smoothly stomp on the right rudder and drag the nose of the plane away from target. If that was the case you'd see oscilatory roll from the wings as he corrected with aileron.
[drdnv70] (score 129, diepte 1) Ask him about this
[drdm7tn] (score 126, diepte 0) For the love of God I hope we don't make first contact while trump is in office.
[drdjjlu] (score 125, diepte 2) What makes you think the “acceleration” Isnt just the camera or sensor being jerked to the right?
[drdlst6] (score 124, diepte 2) Well seeing as how it’s probably a super secret program (not alien, just skunk works) then no, I’d probably want to keep my mouth shut. How long did the SR-71 exist before its existence became public? Who knows what is being used right now that no one even knows exists?
[drdkeak] (score 113, diepte 5) I think this is probably something that needs more emphasis.

The aliens in movies might always be coming to steal our natural resources, our women, or simply to kill us all.

But when I visit certain less developed parts of the world I really have no interest in stealing the local’s pathetic possessions. Or killing them all.

It’s classic human egoism to think aliens would view us as any more worth waging war against than squid. That our planet’s shiny rocks are so desirable.
[drdfygu] (score 112, diepte 4 OP) Because human history shows that it is very dangerous when another group has significantly more advanced technology than your group.

I'm sure many Native Americans were hoping the first reports of [enormous boats](https://i.ytimg.com/vi/nfAFdoKQork/maxresdefault.jpg) coming from the "endless waters to the east" were just fake too.

---

If it's alien we're all fucked if their intentions are remotely hostile. It could for example be a scout drone (sent out to all exoplanets in the circumstellar habitable zone of a star) collecting information to send back, and if our resources are considered valuable they'd send harvesting equipment.

It it's a US black project it means there are entities of the US government (or elite private sector) who no elected official knows about and withholds their technology from the rest of society. We know from leaked documents that even the CIA's reaction to credible UFO evidence has always been "*oh fuck we don't know what this is*". The idea of even the *CIA* not being privy to this opens up so many scary questions it doesn't bare thinking about.

If it's a Russian/Chinese black project, NATO is fucked in any future conflict.

The creepiest thing about it being man-made would be that whoever made it has interests beyond financial (or else they'd sell it to the highest bidding country's military and become a trillionaire).

---

I'd say let's all just hope it's a crazy weather phenomenon.
[drdegfj] (score 110, diepte 1) It was the lead article on the front page of nytimes.com on Saturday.
[drdkuxx] (score 108, diepte 1) *furiously researches fusion cannons and improved interceptors*
[drdih7l] (score 101, diepte 4) There's the other possibility that they are so advanced they don't need anything from our planet, and are here just to observe and study primitive, but  self aware and intelligent, alien life forms.
[drdn30d] (score 96, diepte 2) Are you able to explain a bit about these sensor suites?
[drdot8t] (score 94, diepte 3) >Well seeing as how it’s probably a super secret program (not alien, just skunk works)

honestly I wouldn't be so sure of that. and if it is the tech almost has to be alien or reverse engineered from something alien based on the way the pilots talk about it moving. 

40 foot long ovals don't just book it over 1200 mph faster than an f-18 with no wings, rotors or visible propulsion. not under any tech humans have ever invented. 

I'm sure a lot of shit is being used that no one knows exist. but I hve trouble believing that humans are at that point in technology personally to have hovering spherical aerial vehicles with no propulsion system that outruns f-18s... unless we found something else and learned from that.
[drdk4f2] (score 91, diepte 1) Hello, Commander.
[drdkwif] (score 89, diepte 1) Well if you look at the declassified documents, everything about the location is redacted.
[drdlc68] (score 87, diepte 2) > Always over the same spot, a Lat/Long about 30NM off the coast of Baja, roughly 70nm southwest of Tijuana.  

Better than nothing, but still huge. Source is the fightersweep.com link.
[drdnb80] (score 84, diepte 2) Look cool, sound cool, be cool
[drdl5j6] (score 81, diepte 2) Is this James Cameron?

Sargent James Cameron

James Prentiss Cameron

Listen...
[drdo8oe] (score 81, diepte 1) The F-117's prototypes "Hopeless Diamond" and "Have Blue" could've been easily mistaken as UFOs back in the 1970-1980's due to it's extreme angular design when most aircraft had tublar/curved designs.

EDIT: This article talked about how far they went on concealing the F-117's design, and some of the testing issues, such as the supporting pole of the mockup having a larger radar return than the plane itself, or when a crow landed on the mockup: https://arstechnica.com/tech-policy/2017/12/stealth-turns-40-looking-back-at-the-first-flight-of-have-blue/
[drdrrwl] (score 80, diepte 3) Tbh, I'm not a believer in any alien contact; but the SR71 being built when it was, with the capabilities it had, and the materials sciences employed would probably be enough to convince many people that it was alien tech.
[drdptjo] (score 78, diepte 5) Seriously please tape a damn iphone to the front of your plane
[drdl594] (score 78, diepte 2) "I gotta get me one of these!"
[drdizvo] (score 77, diepte 7) Pretty good, in cold weather they break easily so they aren't as chewy
[drdelrr] (score 74, diepte 1) I just hope it's from earth.
[drdp6id] (score 71, diepte 4) >Without going into too much detail, they can detect just about everything that we think could be useful to detect. And they do it really well.

with all this super fancy tech... do you think it might be possible to get a clear fucking image? not grainy black on white? 


just curious given how advanced you said everything is... apparently making visual contact just isn't important.
(950 reacties met lagere score weggelaten)

=== THREAD x5l7pz ===
SUBREDDIT: r/running
DATUM: 2022-09-04  SCORE: 1165  REACTIES: 374
TITEL: Why are running injuries so common for humans? I have a hard time believing our cavemen ancestors adhered to the 10% rule, performed muscle imbalance workouts, stretched consistently, or used orthotics
POST (source_id=post):
The things I can think of are that nowadays we are all probably a bit heavier, they didn't have McDonald's and donut shops

No shoes, or minimalistic sandals so all muscles in the foot were used ?

We typically run on asphalt and concrete instead of foliage covered dirt. A tradeoff perhaps on superficial injuries vs more insidious ones? 

Most of us are far more sedentary, maybe they we able to train more muscle groups through games and various gathering habits? 

Lastly, perhaps stress and less sleep? I would guess most of us experience less intense momentary stress but a more often constant kind of stress?  And since hunter gatherer types only worked~4 hours per day they probably were always well rested 

Anyway, I wanted to leave this part open and leave an open discussion, but I had to fill the minimum text post length!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[in2bgke] (score 2777, diepte 0) Anthropologist here.

Even though a lot of evidence suggests our human and proto-human ancestors were quite capable long distance runners and walkers, some of the same evidence suggests that they had absolutely brutal lives with plenty of injuries. Osteological analysis (bone research) has been used to show that plenty of our ancestors had sustained pre-mortem leg/foot injuries, suggesting the conditions they lived with. This is especially true of the Neandertals, where we see a lot of these injuries.

It's also easy to think that these people were somehow more "robust" than us because a lot of us are used to the idea of the intrepid "hunter-gatherer people," but that image has also been proven to be somewhat mythological.  Our ancestors did much more gathering than hunting (unless we're talking about hunting for insects on the ground). "Hunting" mainly consisted of scavenging for small game and carrion. They were less like tigers, and more like anteaters. 

Our ancestors were really not so different than us in terms of ability, and certainly not more robust. With the advantage of modern nutrition, medicine, and orthotics, I imagine we're tending to far less injuries than they would have if they also ran for "fitness," like we do.

EDIT: Thanks for the awards and the kind comments! I didn't expect my response to generate this much discussion. I've been a runner much longer than an anthropologist, so this was a nice mix of my interests!
[in2czy4] (score 838, diepte 1) "less like a tiger, more like an anteater" is going to be my new mantra. Thank you for this gift.
[in253fi] (score 548, diepte 0) First up, *survival* doesn't mean *comfort*.  Prehistoric people lived their lives a lot closer to the edge than we're used to.  And yeah, some of us are out here running barefoot trail ultras with no serious or chronic injuries.  It's at least plausible that similar running would have been unremarkable and safe for most folks who grew up in a culture of doing so on a frequent basis.
[in2pq43] (score 421, diepte 2) Sure, but being like an anteater can be aard vark.
[in2741s] (score 267, diepte 0) How do you know that our early ancestors did not sustain running injuries? Their average lifespan is a lot shorter, and they had much worse things to fear than running injuries, like Malaria, smallpox, or whatever disease that is prevalent at that era. Those who got injured rely on their tribal mates to cover them until they can recover, or they die.
[in2ibcf] (score 209, diepte 1) I can't help thinking of you reading this question and thinking, "My moment has come!"
[in2idtg] (score 189, diepte 2) Agreed, how can you be SURE the prehistoric people weren’t running in Nike Zoom Alphafly and didn’t go back to the tribal physiotherapist after a hard day of 400M hunting intervals?    /s
[in2dwsk] (score 180, diepte 0) Assuming that "ancestors were injury free" is your first and biggest problem here.   
Bring some evidence we can discuss otherwise it's all speculation.

Considering how far we have come i am confident to say you are most likely wrong.
[in2876n] (score 159, diepte 1) Came here to say this. Many of modern chronic medical problems are the result of living long enough to start getting it. Musculoskeletal problems, heart problems, cancer, strokes etc
[in2j3em] (score 114, diepte 2) Haha, happens more than you would think. Turns out the study of humans has more than a few applications.
[in25ist] (score 93, diepte 0) They grow up used to running and walking everywhere, so their bones, joints, muscle, and cardio was all used to it. Also they likely weighed a fair amount less than the average 1st world country person of today. Lastly I’ll end with since they did not have shoes, or shoes were very minimum to prevent cuts only and not cushion they likely had adopted running form that fit their body and did not cause injury. Sometimes today people use shoes to cushion bad form, I myself am trying to get a more natural running form and rely less on shoe cushion.
[in2ykrv] (score 91, diepte 3) Well, you know what they say: one on the tongue is worth two in the hill.
[in2hen2] (score 84, diepte 1 OP) I'm very glad you're here and I appreciate you responding to this ! :)
[in2ibmu] (score 81, diepte 2) This is a speculative post, dude. No one’s citing this Reddit post in a scientific journal. Chill
[in24ssk] (score 70, diepte 0) They walked around 100% of the time and had no such bad habits that we do today. 

It’s not that running injuries are due to running, it’s due to our lazy/sedentary lifestyle now.
[in2dmm9] (score 70, diepte 2) Maybe if someone was a lone wolf. 

Some consider the first sign of “civilization “ to be the first (granted, found) healed femur. Someone cared enough for that injured person to take care of them until they healed. 

Timeline may not be perfect but the concept is important. 

https://www.google.com/amp/s/quoteinvestigator.com/2021/07/25/femur/amp/
[in2njun] (score 68, diepte 3) Hey I am a human!  

Thanks for studying us, the vast majority of us have no idea why we are the way we are.
[in2bpba] (score 64, diepte 1) Cavemen weren't running on hard pavement surfaces, I think that's one thing that a lot of barefoot/minimal people miss.
[in27nks] (score 60, diepte 1) But it’s not a scientific study, just the opinion of a guy.
[in2esrp] (score 54, diepte 2) Ketchup
[in27ohx] (score 53, diepte 0) How common are injuries?  I would guess most injuries happen when we start up too fast or train too strenuously and have not been conditioned to moving our bodies. Taking out the self inflicted injuries caused by our eagerness to do something our bodies aren’t prepared for our bodies seem to run pretty naturally. 

Those who are living a hunter/gatherer lifestyle probably rarely run for pleasure and  conserve calories that they work so hard for. They do not have a marathon date to train for and impose artificial timelines on when they run. They likely walk more than 95% of their miles so you are really comparing apples and oranges.
[in2ikn5] (score 52, diepte 2) What part of that comment do you need a source for?
[in3adqb] (score 52, diepte 1) I'm not sure why "injury free" is even suspected. All manner of wild animals are injured in the ordinary course of their existence. There's no reason to suspect early humans should be exempt from that.
[in2jm3u] (score 51, diepte 4) Come be an anthropologist. We're a thriving yet argumentative community. No shortage of conversation!
[in2pi46] (score 42, diepte 4) Source? Famines can absolutely happen without agriculture.
[in2goru] (score 41, diepte 2) This is very true. I would have been dead 20 years ago were it not for modern Medicine and the ability to safely remove an appendix.
[in2m8uz] (score 37, diepte 2) Source for what? That living in small groups mostly outdoors alongside megafauna and without agriculture or long-term food storage brings you close to life-and-death struggle more frequently than sitting around in a city?


Or for being fine after many years running mid distance barefoot daily, and marathon+ occasionally? That's just personal anecdote.
[in3hlxb] (score 37, diepte 2) Is that why studying humans is know as ant-hropology?
[in3fuo7] (score 36, diepte 4) keep going im almost there
[in27dzd] (score 35, diepte 1) aka weekend warrior syndrome
[in4rwcl] (score 35, diepte 2) I remember hearing on a podcast that mammoth bones are far more likely to survive and be discovered so we have a biased view of our ancestry as big game hunters because the squirrel bones just don't withstand the test of time.
[in2dvjv] (score 34, diepte 2) Also when there are rocks and branches and roots underfoot you don't run as fast. Each step is more measured and cushioned, there's no straight leg striking the ground and rolling from heel to toe.
[in2euao] (score 34, diepte 2) A meniscus tear was not a death sentence, there is plenty of evidence that the tribe cared for their injured.. If this were the case, humanity would have died out because every pregnant woman would have been killed off before delivering a baby.
[in2hp1l] (score 33, diepte 4) Source?
[in2xqjj] (score 32, diepte 4) Why do you ask everybody else for sources, yet you make all these claims and then won't provide any sources? Hold yourself to a higher fucking standard, buddy.
[in2ix55] (score 32, diepte 2) You're welcome. I'm still learning more about us every day. We all are!
[in2p8fk] (score 31, diepte 0) Our ancestors probably have had every injury we have. It's just not medically studied or hard to see in the fossils. Also they probably did a lot more walking than running.
[in2fuet] (score 29, diepte 3) Shanidar I (45,000 year old Neanderthal) shows that the tribe cared for him. He was missing a lower arm/hand, had a pronounced limp but still lived to be in his 40s.
[in2i9qg] (score 29, diepte 2) > Source?

and

> Source?

and

> source?

and…really? Again?

> Source?

Dude/Dudette it’s a discussion post on a *casual* forum. Chill out…we’re bizbazzing it’s not a fucking dissertation defense.

Jesus.
[in53keg] (score 28, diepte 3) I've literally never thought of this, but the mental image of a half dozen 5'2 unkempt proto-men, wearing the tattered remnants of the one sick and elderly wooly mammoth their grandparents took down, standing in a circle around a tree throwing rocks at squirrel dreys and jumping up and down triumphantly when one manages to knock a nesting family to the ground makes the image of the powerful, primal savage melt away into a more realistic picture of a barely competent, barely surviving group of 20 year olds who just realized that if they poop on the other side of the river they doesn't get sick after they drink the water.
[in2uane] (score 25, diepte 3) This is one of the things that amuses me in the conspiracy and collapse type subs. Everyone stocks piles guns and is going to be the loan surviveor of the whatever event they are planing for.

And here I am thinking...you are one bad slip and fall away from a slow painful death if you are alone.  One bad "whoops, didn't see that barbwire on the branch I grabed..." away.
[in2wxx5] (score 25, diepte 0) where is the assumption of "caveman ancestors" having few(er) injuries coming from? that's quite the leap
[in2jcv1] (score 24, diepte 3) Now that you mention it, I am often curious about humans. Lol.
[in27c90] (score 23, diepte 1) There is a lot of evidence that tribes cared for their injured clan mates. Lots of bones show evidence of healed injuries so people were up and dying if their broke an ankle.
[in24s3z] (score 22, diepte 1) The current anthropology/biomechanics research supports that humans are built to run long distances. There are great books about this that I’m sure have been mentioned & discussed in this subreddit. Super interesting and not necessarily intuitive
[in2bzos] (score 22, diepte 2) And that guy died so it's not really a good example of not getting injured while running.
[in2ik6l] (score 22, diepte 1) While I agree with your general statement, their lifespans were not much shorter. They had a LOT of deaths in the first few years of life, but if you made it past 5 years of age, your lifespan was similar to today.
[in2gn50] (score 21, diepte 2) Also i don’t think cave man were running 5ks every day or training for a marathon so that might also be a factor
[in2n0lh] (score 21, diepte 1) The average lifespan was only low because very high mortality rate in children and young adults (wars). Once you hit a certain age you pretty much had a slightly lower chance of reaching 60-70 years. 

It pretty interesting that what has increased our average lifespan is not increasing the top but reducing early death in children and young adults allowing more to life into the 70-80 range.
[in2mqpw] (score 21, diepte 2) I would buy a t-shirt with that mantra
[in23zvv] (score 19, diepte 1) Absolute bollocks.
[in251y5] (score 19, diepte 0) Back in the cave man days they didn't run as much. And if they got injured they just died probably.
[in4edms] (score 19, diepte 4) Yeah,, but they weren't on Strava so it didn't actually happen.
[in2og6i] (score 19, diepte 2) if i had a dime for every time someone needed to say this....
[in3pbn7] (score 19, diepte 3) Jonathan a Heidt touches on this in his book “The Righteous Mind”. I found the relevant section on my kindle:

“Can the human genome respond to new selection pressures in, say, thirty generations (six hundred years)? Or would it take more than five hundred generations (ten thousand years) for a new selection pressure to produce any genetic adaptation? 

The actual speed of genetic evolution is a question that can be answered with data, and thanks to the Human Genome Project, we now have that data. Several teams have sequenced the genomes of thousands of people from every continent. Genes mutate and drift through populations, but it is possible to distinguish such random drift from cases in which genes are being “pulled” by natural selection. 

The results are astonishing, and they are exactly the opposite of Gould’s claim: genetic evolution greatly accelerated during the last 50,000 years. The rate at which genes changed in response to selection pressures began rising around 40,000 years ago, and the curve got steeper and steeper after 20,000 years ago. 

Genetic change reached a crescendo during the Holocene era, in Africa as well as in Eurasia. It makes perfect sense. In the last ten years, geneticists have discovered just how active genes are. Genes are constantly turning on and off in response to conditions such as stress, starvation, or sickness. 

Now imagine these dynamic genes building vehicles (people) who are hell-bent on exposing themselves to new climates, predators, parasites, food options, social structures, and forms of warfare. Imagine population densities skyrocketing during the Holocene, so that there are more people putting more genetic mutations into play. 

If genes and cultural adaptations coevolve in a “swirling waltz” (as Richerson and Boyd put it), and if the cultural partner suddenly starts dancing the jitterbug, the genes are going to pick up the pace too. 

This is why genetic evolution kicked into overdrive in the Holocene era, pulling along mutations such as the lactose tolerance gene, or a gene that changed the blood of Tibetans so that they could live at high altitudes. Genes for these recent traits and dozens of others have already been identified.”

— The Righteous Mind: Why Good People Are Divided by Politics and Religion by Jonathan Haidt

https://amzn.eu/2eDwtlN
[in2eesf] (score 19, diepte 0) My dog stretches many times a day. I don’t. He’s a better runner than me
[in2ie5p] (score 18, diepte 3) You can tell Darwin fuck you!
[in28d5j] (score 17, diepte 1) I assume those averages are strongly pulled down by infant mortality
[in2n317] (score 17, diepte 2) Not true, actually.   We have lots of evidence of healed fractures among Neanderthals and early Homo sapiens.  People lived in social groups and took care of injured people while they were healing.
[in2kueu] (score 17, diepte 2) Adding significant muscle mass relies on steady access to protein. Protein was the limiting nutrient for most of our ancestors.

Evidence indicates that most of our ancestors were more likely to be malnourished than muscled.
[in5clw1] (score 17, diepte 3) This is something that is very much a demonstration of confirmation bias. You see that a few species of really big animals went extinct so you disagree with an expert in the field about their work because you think this must mean we hunted a lot. 

There are innumerable reasons behind why we may have lead to the extinction of a species. Today we are killing off dozens of species every year and it isn’t because we are killing so many of those for food but because our activities are so disruptive to them. 

Perhaps humans and these other large creatures preferred similar environments and we just out competed them in those environments and drove them off. Maybe we saw them as a threat in our environments and killed them off to protect our settlements (we still do this today when we really do not have to anymore) 

Let’s also consider that there were not any modern methods of food preservation, so whereas today you could say one cow could provide the meat to a family for a year, back then you’d have to kill new cows every day or couple of days because the meat would go bad and you wouldn’t be able to eat it all. 

Try not to read what you want to think into a single fact of history
[in38lbx] (score 17, diepte 2) This article (end of section 3) outlines some genetic changes that are thought to have been selected for with the shift to agriculture, related to processing alcohol, starch, and milk:

https://www.hindawi.com/journals/ijeb/2011/484769/

I am not sure how direct a tie we can make to running ability from these changes, but an interesting question!
[in277jr] (score 16, diepte 1) Humans are one of the most efficient distance running mammals on earth. It was our primary hunting method for millennia. We are however terrible sprinters by comparison.
[in2du58] (score 16, diepte 1) This piece says about 50% of runners each year, which I was quite shocked by.

https://www.yalemedicine.org/conditions/running-injury
[in2qxmv] (score 16, diepte 6) It depends on the subfield of anthropology. There is biological, cultural, and archeology. With any of these you will need at least a masters and usually a phd in order to get a job in the actual field. I got my undergrad in cultural anthropology and the only job I qualify for is museum staff. Which is also very competitive in my area. Super interesting field but not much job outlook unless you plan to get a phd.
[in304te] (score 15, diepte 4) One of the more fascinating and realistic parts of an apocalyptic novel was in Stephen King’s The stand. There’s a chapter that talks about all the second wave victims that survived the flu but couldn’t survive their own decisions and accidents. In order for humans to survive they need to have groups of people with varying and high level skills, else it’s going to be a quicker end than one would think. It’s a rare person who has the perfect blend of abilities to survive on their own.
[in2tlmu] (score 15, diepte 1) u/likable_error  I would have thought a few thousand years of not persistance hunting (because of farming), even if we did only do it occasionally, would allow a lot of genetic variations that are not helpful to running long distance (but perhaps helpful to say riding horses, or drinking milk). Is there any evidence for us having a broader (more error prone) genetic sequence than our predecessors?
(294 reacties met lagere score weggelaten)

=== THREAD 1kxemv4 ===
SUBREDDIT: r/Military
DATUM: 2025-05-28  SCORE: 2707  REACTIES: 283
TITEL: When saluting, stand at attention with your feet together...
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[muok4ts] (score 1924, diepte 0) He thought feet together is only for a field sobriety test and didn't want to give anyone the wrong idea.
[muokwxr] (score 747, diepte 0) Return to standards needed.
[muol7hi] (score 736, diepte 0) Balance is impaired while drunk.
[muol0ab] (score 520, diepte 1) He’s got PTSD from those. Not IEDs or SAF, nope. It’s the field sobriety test. While deployed. To Bahgram Air Base.
[muoksmr] (score 511, diepte 0) But my balls are too big because of all the lethality! - Kegbreath
[muojf5g] (score 277, diepte 0) Maybe he's dizzy and needs to stand like that for balance...
[muot9pa] (score 202, diepte 1) Don't be silly, it's just because all those alpha male Red state politicians all have a ["wide stance"](https://en.wikipedia.org/wiki/Larry_Craig_scandal)
[muopwkk] (score 202, diepte 0) That’s what happens when you settle for a DUI hire.
[muoo9gr] (score 156, diepte 0) Is it weird that I automatically knew who that was just based on how he looked from the back?
[muonocm] (score 154, diepte 1) If he’d stood with his feet together he would’ve toppled over; odds are Kegseth was shitfaced at whatever this was.
[muok65c] (score 129, diepte 0) Are you kidding me?
[muosv9b] (score 122, diepte 1) I dunno. Plenty of Aussie diggers seem to manage fine on ANZAC day every year. They have rum for breakfast.
[muopwx7] (score 107, diepte 2) Thinking an alcoholic Fox News host isn't fit for a government role makes you liberal and communist? You fit right in with the orange cult.

![gif](giphy|X3nnss8PAj5aU|downsized)
[muom7mp] (score 103, diepte 0) What a fucking embarrassment
[muootp1] (score 103, diepte 0) Top man doesn't salute correctly. Whats happened to us?
[mup2qy4] (score 103, diepte 0) Having your feet apart a little helps you balance when you're hammered.
[muor5ea] (score 99, diepte 3) What does having an alcoholic SECDEF have to do with a socioeconomic ideology that envisions a society where the means of production are owned collectively?

You realize that words have actual meaning, right?
[mup54so] (score 70, diepte 1) SecDef is a DUI hire
[mup6ko5] (score 69, diepte 1) Sergeant Major?
[muoxuel] (score 64, diepte 0) Really fucking weird. There’s no fucking way his muscle memory doesn’t kick in when doing this, so I see this as a deliberate move to show that he’s too cool for school. (I’m your boss now I don’t need to follow customs and courtesies gfy). Or, he’s just drunk as some people have suggested 🤣
[muorvqu] (score 63, diepte 3) The MAGA use "communist" as a pejorative.  They don't realize that words have actual meanings. He isn't referring to a socioeconomic ideology that envisions a society where the means of production are owned collectively.  He is just using "communist" instead of "poopypants."
[mupzjgn] (score 57, diepte 2) Nah, in the US Army you can salute in civilian clothes/without a cover. If you're in morning pt clothes you'll probably end up saluting some random officer whilst both of you are sans cover.

Heck on Fort Gordon (back in my day...) I had to gate guard. After you verified that an officer was good to continue onto base, you had to salute them. Sometimes that would confuse butter bars and it led to interesting situations.

The best one I personally had was an officer who saluted me back while eating a burger...with the burger in his right hand during the salute.

I also had a dude run over the cones because he stopped holding the steering wheel to return my salute.
[muov1k0] (score 57, diepte 3) found the Russian bot
[muoox4o] (score 55, diepte 0) Shitbag Pete continues to be a shitbag. Especially at one of our most sacred grounds. 

Good job fuckhead. You've barely started and already have fucked up beyond imagination.
[muol0ci] (score 54, diepte 0) Reminds me of that time I passed out for 6 hours while cooking a pizza.
[muoypfb] (score 54, diepte 1 OP) That's assuming he wasn't a shitbag soldier to begin with. And everything about him says he was.
[muono55] (score 53, diepte 0) Literally one of the first things you learn at basic, what a f'ing embarrassment...but maybe he was hung over
[muowden] (score 51, diepte 3) I'm from Australia and I'm not military, but most of my family are and I grew up going to the returned services clubs with my dad. 

Every evening at sundown they'd play the last post and read *"The Ode."* And none of them were wearing covers. They simply stood at attention for the duration. 

I remember what dad said to me. *"Stand up. Heels together. Stand up straight. Arms by your side. Thumbs in line with your trouser crease. Stay still until everyone else isn't."*

Job done.
[mupxqxq] (score 51, diepte 1) [President Obama once saluted with a coffee cup in his head and the right lost their fucking minds.](https://www.cbsnews.com/news/outrage-ensues-after-obamas-coffee-cup-salute/) Fuck these hypocrites.
[mupbe9b] (score 50, diepte 2) They had to demolish the restroom 😂😭
[muouvg6] (score 48, diepte 2) Pretty sure liberals aren’t trying to transfer money from the sick, the poor, and veterans and hand it over to the richest people in America.  If you’re assigning hate, start with a president with a decades long animus towards black and brown people, now weaponizing that hate.
[muolff1] (score 48, diepte 0) This reminds me of the inspection I had to stand for the day after my 21st birthday 🤢
[muossem] (score 44, diepte 1) Dizzy from knocking back too many drinks.
[muotnvs] (score 43, diepte 2) I couldn't say for Army regs because I'm Air Force. Also, things can get weird/different for special occasions so I'm actually not sure in this case.

Also also, I'm not sure if SecDef follows regs of their prior service or if there's a whole separate DODI or something for that. I've never cared to look since it is not directly relevant to me (I'm not exactly on the SecDef vector...).
[muorhac] (score 43, diepte 0) He’s got a waiver for that on account of his shaky knees from the 10 Milwaukees Best he chugged in the women’s bathroom before this photo.
[muorvh2] (score 40, diepte 1) Aren't you also only supposed to salute when wearing a cover? Otherwise you simply stand to?
[mupmvjv] (score 38, diepte 3) SecDef knows better as prior military himself. Standing at attention is ingrained in us - when I got sworn in for jury duty, one of the bailiffs asked me “what service?” as he was manning the door to the courtroom when we were dismissed because he noticed how I stood, and I’d been out four years at that point.
[muopuxt] (score 37, diepte 2) Obvious bate is obvious. How's the boot taste?
[muqfrlt] (score 37, diepte 2) No, not at all.  But this is 

something the SecDef prioritizes.  Standards, standards.
[mup2f0h] (score 34, diepte 1) Nope. I wager everyone here knew it to be the same person.
[muprzug] (score 32, diepte 2) ![gif](giphy|xT9IgHCTfp8CRshfQk)
[mupa8kt] (score 32, diepte 2) Oh I love me a good Larry Craig reference!
[mup3cf9] (score 29, diepte 1) He's [tired and emotional.](https://en.m.wikipedia.org/wiki/Tired_and_emotional) 

...as a newt.
[muomm7s] (score 29, diepte 1) It’s Pete Hegseth
[muq97rs] (score 29, diepte 2) that was a pretty awful salute but it's not like they actually care about any of that and just wanted any reason to hate on Obama.
[muot03u] (score 28, diepte 1) Was the pizza okay?
[muomjjl] (score 28, diepte 0) Career specialist kicked out for racist tattoos...checks out.
[mup37t8] (score 27, diepte 3) I can't imagine being this fragile 🤣
[mup5p2o] (score 27, diepte 3) Is it fun being a loser?
[mup2fs0] (score 27, diepte 1) I'm still join the heels 35 years after my discharge (I was drafted). 
🤣
[muqj2jw] (score 27, diepte 1) He probably thinks his feet are actually together, which is the sad and hilarious part of such a sad and hilarious picture lol.
[muow3cl] (score 25, diepte 1) Terminal Guard Majors absolutely OVERFLOW with lethality and sexual power. Respect.
[muoqsb4] (score 25, diepte 1) Bush signed the 2009 Defense Authorization Act in October 2008 that allows for veterans and servicemembers not in uniform to render a military salute. I don't believe it's been rescinded. I've personally never done it, mostly because I feel ridiculous saluting without a cover and in civvies.
[muon9xc] (score 23, diepte 1) Don't need to tell any of us that.
[mupfioj] (score 21, diepte 3) Dude, your comment history reads like a list of charges at The Hague.
[mupsocw] (score 21, diepte 4) Holy shit! that history is wild!
We got:  Navy washout, conflicting time lines of service , steroids use while in service it seems , doordashing tips.

Must have ate all the paint chips while needle gunning for 3 years
[mupjne8] (score 20, diepte 0) And entry level weekend officer who’s claim to fame is running orgs in the ground and removing minority accomplishments from military websites.
[muqoxx4] (score 19, diepte 3) Ive been that butter bar lol
[mur6vqa] (score 19, diepte 4) My husband and I are not big people so our field jackets were roughly the same size. My hubby was a prior service butter bar, myself a SPC. One day he went through the gate expecting his salute. The gate guard looked at him with his ID in hand and said excuse me sir are you a Specialist 2Lt?
[muopa1j] (score 19, diepte 0) Probably still drunk
[mupvgel] (score 17, diepte 6) Dang! I didn't even put the Ram in the mix with DD.  He probably idles while waiting because it "sounds cool"...  Solid 7-12mpg
[muomsfg] (score 17, diepte 0) Why are civilians even saluting at all?
[muou219] (score 17, diepte 1) 5 years ago during covid, Trump was electioneering at Arlington cemetery, right next to buried servicemen and women. They care nil in this clown show.
[mup298x] (score 17, diepte 0) I'm surprised he's using the correct hand.
[mup2l7q] (score 16, diepte 2) And there I thought you were referencing Blackadder and the [actor's stance](https://youtu.be/42WFxAtoM-g?si=uWqjo2wrAL5EpVUa)
[muq63k8] (score 15, diepte 4) Also Australian. My Dad served in the British army during WW2 and I vividly remember him teaching me how to stand at attention the same way, when I was about 5yo

But why would Hegseth have bothered taking any notice of that 🤷‍♂️
[muptk62] (score 15, diepte 5) And doordashing in a RAM pickup?  How is that a profitable endeavour?
[mupj8h1] (score 15, diepte 3) Man, failed at the Navy and now doing doordash.
[muomgox] (score 15, diepte 1) That's not Macron lol.
[muomrgx] (score 15, diepte 0) He is an actual clown 🤡
[muoye5j] (score 15, diepte 1) Most people learn that shit in DEP
[muq8z7k] (score 15, diepte 2) and over half of them are probably apologists.  an uncomfortable amount of service members support this twat
[mups0xz] (score 14, diepte 3) Section 595 of The National Defense Authorization Act allows for ununiformed servicemembers to salute. Don’t know about civilians, guess they can do what they want.
[muomp79] (score 14, diepte 0) What a waste or was he wasted? Both, likely.
[muopvxd] (score 14, diepte 0) How will maga spin this?
[mupqqda] (score 13, diepte 3) Judging by comment history, we should be asking how those steroids tasted while on while on active duty
[muovveq] (score 13, diepte 1) You take that back.

https://preview.redd.it/rsge3nzjri3f1.png?width=1024&format=png&auto=webp&s=b39e4de142edb4fd6711edbc6da21360f06728fe
[muorx6q] (score 13, diepte 0) It’s cause of his assplug
[mup2hu1] (score 12, diepte 2) For situations like this, saluting is fine. Even indoors when not wearing cover there are times you actually do salute too. Us

In civilian clothing, saluting is not usually required, but it is an option.
[muowuqk] (score 12, diepte 1) Remember when Obama saluted with coffee in his hand while stepping off marine one? Have no doubt they will hold secdef and former officer Pete to the same standard as the cinc who never served.
(215 reacties met lagere score weggelaten)

