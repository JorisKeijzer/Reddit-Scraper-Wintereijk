# Label-batch batch_0072

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
Schrijf het resultaat naar `batch_0072.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: h8unm2, 1dnpku2, i0b1jf).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD h8unm2 ===
SUBREDDIT: r/Teachers
DATUM: 2020-06-14  SCORE: 639  REACTIES: 203
TITEL: Anyone else’s district just dragging their feet about next year and potential cuts?
POST (source_id=post):
Anyone else’s district just dragging their feet on what next year may look like and what cuts there may be?? It’s sooo frustrating!! Literally only communication we have received is that our district is not looking to cut entire programs such as Art, Music, etc. but they do have concern for kindergarten teachers because enrolled is down. Problem is if those teachers get cut there will be a trickle down effect due to seniority. 


I get that they have a lot going on (and still a lot of unknowns) but I fear that I will get cut in late July or August then just have no options in terms of finding another teaching job. I’ll be forced to leave a field that I love at least for the time being. Its one of those situation where I definitely do not want to get cut but that if I’m going to, I want to know now so I can look elsewhere, if needed.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[fuswdqw] (score 183, diepte 0) Yes, and we don’t expect anything final to be decided until the end summer, or possibly after count day.

A teacher on the “reopen committee” (which has been very quiet) let slip that we would likely copy another districts plan that has already been released. It states that k-8 will only focus on ELA and math. I teach at a middle school so that would mean pretty much everyone would be laid off except for those subjects. I’m actively working on plan B.
[fut4et3] (score 162, diepte 0) Going with masks won't work, not for health reasons, but because the kids won't cooperate. We'd spend half or more of the day telling them to put the mask on, or dealing with defiant kids. 

I can see it now:. Disgruntled kid gets in teacher's face hoping to spread "the rona," because he's mad at the teacher and "old people are more likely to die."
[fute5l7] (score 149, diepte 0) Nope.  My district (even though they're getting an extra 7% more next year) is cutting about 5% of the positions district-wide.

But you know who's not getting cut? A single district office position.
[fut8sdo] (score 94, diepte 1) Well, given what scientific background knowledge kids come to me with in high school, seems like business as usual!
[futdjd4] (score 75, diepte 1) I mean, yeah. The day we were to close for shelter in place a junior came in my door (I stand in the hall or at the door for passing) and coughed on me. He doesn't like that I emailed his parents a few times and that's how he got back at me. Teachers will die for kids stupidity.
[futdhsb] (score 66, diepte 0) My favorite thing to come out of this for Texas, the TEA has set maximum class sizes at 20. How asinine is that shit? No adjustment based on the size of the room at all. I have one of the biggest rooms on campus and there’s no way 20 kids can be spaced out anywhere approaching 6 feet apart. 

TEA: “yeah, we did something. See?”
[fut685o] (score 62, diepte 0) Yup my district is dragging their feet. They sent out a survey this morning asking if anyone would be comfortable taking an unpaid year of absence so I'm guessing the budget cuts are going to be bigger than we thought. As a teacher entering their 4th year in the fall I'm scared that they're going to blindside me with a layoff in the fall when it's too late to find other teaching jobs
[futu0ag] (score 56, diepte 1) That's ridiculous. District jobs do not directly impact students. Teacher, aides, and counselors do impact.
[fut5p3x] (score 51, diepte 1) Or they’ll find it irritating and be constantly re- adjusting it, thus making the mask useless.
[futbjbv] (score 45, diepte 2) Michigan. They haven’t explicitly stated anything about layoffs, but they also haven’t said jobs are secure so it’s worrisome. I think electives will for sure be wiped out because they’re “too difficult to teach online and complicate things for students.” But again, that’s just me reading between the lines. I hope I’m wrong.
[fusx1qe] (score 42, diepte 1 OP) From the little I’ve heard, our district is also considering other area district plans but I don’t know the details of those plans. 

I teach Math which is a positive b/c that tends to be seen as a necessity but I’ve also been seeing what else is out there just in case.
[futlpo1] (score 39, diepte 2) It's only going to feel like 40 hours a day ;-)
[futii44] (score 39, diepte 1) Unpaid year of absence?  More like "hey does anyone want to just go ahead and quit?"
[futfzqw] (score 38, diepte 1) But also for health reasons. Masks are for short term exposure and wont help you if you hang out in a small room with an infected person 40 hours a day
[futrpa7] (score 37, diepte 1) I'll shine a little hope into this darkness. If teachers agree to be furloughed for a year, they may be a eligibleforunemployment assistance. And there are a LOT of high-risk teachers out there, or teachers with high-risk family members, who do NOT want to go back in the classroom at the end of the summer. I could see a lot of teachers taking them up on that, especially those who are older but not yet ready to retire.
[futxluv] (score 36, diepte 1) I saw a document from my district that had as a bullet, “teachers will have students stay seated.” Like... what makes you think children will all of a sudden be any more compliant with that than they ever were?
[futkwub] (score 34, diepte 1) Did you read that TEA also was supposed to distribute the CARES money to schools, but is keeping it? Schools were planning on using it on technology and distance learning. Instead, TEA said something about it paying for the past school year or something. Yet TEA bought millions of masks and sanitizer. I wonder how much schools will actually see...
[futbbrg] (score 33, diepte 1) Everyone? Holy crap. What state?
[futb3l2] (score 32, diepte 0) Nope because they already let me go. Hooray for actually qualifying for unemployment over the summer
[futyxxd] (score 32, diepte 2) Yes, but people in the DO are the ones that interact with financial departments.  There is so much disconnect between the district and the buildings that I'd be they couldn't find one of their own schools if you gave them a map.
[fuu9ujn] (score 31, diepte 2) My high school students:

* "Which one is the y-axis again?"
* "A variable is the thing that stays the same right?"
* "But my middle school teacher said the scientific method HAS to be in THIS EXACT ORDER!"
[futbpp7] (score 29, diepte 3) Yeah man. If kids are going back to the classroom I don't think they'll be in school the whole day just for English and math
[futuneb] (score 29, diepte 2) Don’t you wish you could just clock those kids? Lol.
[futlzom] (score 29, diepte 0) I got terminated a week or so ago for next year with reasons cited as "Classroom management and Issues with parents" and when I sent in evidence to the contrary (also stated the fact that we have been on online learning for 3 months and thus haven't had a classroom to manage...) and pushed for specifics I got nothing, and being non-tenured my union rep. pretty much said there was nothing they could do. 

&#x200B;

From what I am told from my older teacher and retired teacher friends is that every time there looks to be large budget cuts coming, my district will cut as many non-tenured as they can justify, and then if they need to cut more come August they do, and if not they hire back who they can. Considering how I hadn't heard a thing about these items from my administrators at all this year (sans one parent issue in October over a grade), I am feeling that I fell into the unfortunate category of "Nontenured during pandemic budget cuts". 

&#x200B;

So tl;dr: For some districts, these cuts could have very well already started and it could very well get worse.
[futc1ox] (score 27, diepte 4) Ah I should’ve included that - we are planning on hybrid learning for the fall so that only a few students are in the building at a time. The plan we are supposedly following has a shortened school day even when they attend.
[fusxnnp] (score 27, diepte 0) Yeah, no info here, even in a small rural district that doesn’t necessarily have to take the same precautions as larger urban districts. A lot of districts are probably waiting on Newsom’s budget here in CA, though.
[fusyjgk] (score 26, diepte 0) School board here is voting on what the plan’s going to be on Tuesday. Options from going back at full capacity with “masks and social distancing when possible” to a staggered schedule model. In either case, an optional full distance learning program will be available through the district for those who choose it. As far as cuts, an admin said those could come as late as July.
[futkmw4] (score 26, diepte 1) How are they providing the online learning? I know it’s been talked about in other districts to have a blended model. My worry is teachers will be stuck doing twice the work with monitoring online and in-person schooling.
[fuu04os] (score 25, diepte 3) Don't let your dreams be dreams. You can clock a child, and even be rewarded with free room & board by the government!
[futkb6v] (score 25, diepte 1) I’ve already seen parents say locally on social media they won’t send their kids back to school if masks are required/ enforced. Again, priorities.
[futabrh] (score 21, diepte 0) The superintendent sent out a notice to all staff that cuts are a possibility in the future.  I’m applying for a new job now. Wish me luck,  this new district interviewing is really good and it would be a dream job
[fuuhl1g] (score 18, diepte 3) As a middle school science teacher I'm sorry. We go HEAVY on graphing for this exact reason.
[futiufv] (score 18, diepte 2) Exactly how I interpreted it as well. I assume a very very small number of people actually said yes to that
[futsjqy] (score 18, diepte 2) You know I hadn't thought about that.
[futs3g2] (score 17, diepte 2) Then keep the germy things at home!
[fut14dl] (score 16, diepte 0) Private school. We are waiting and seeing but making contingency plans. 


I teach Kindergarten, so I want either full time in person instruction, or half days with an hour break in between.
[futavi6] (score 16, diepte 0) Its a scare tactic to keep people from quitting. Absolutely ridiculous. Mine is doing it too.
[futki2v] (score 15, diepte 1) Like furloughed or just quitting? That seems like the majority of people would not have that luxury. Maybe parents with their own school-age kids if they plan on keeping them at home. But money seems scarce anyway....
[futy6kx] (score 15, diepte 1) File for unemployment, and use your evidence when you have to appeal.
[fut7lw7] (score 14, diepte 1) WOW, I hadn’t even heard that as a possibility anywhere.  That’s.... something.
[fuv7xz7] (score 14, diepte 3) Oye. Fwiw I am a probably a decent science teacher and all kids need to learn about in elementary school is how to ask questions and make observations (noticing deeply). In an ideal world, we would help nourish their curiosity, so that they asked cool questions about the world on their own after just looking at stuff, but it’s hard to put that burden on people. grow plants in your class, have the kids keep journals, drawings, and ask why, if you can! NGSS is all about stuff you already do anyway - observing patterns and changes, cause and effect, all that good stuff. I have spent most of my career trying to get people to understand its not about content!
[futf0ol] (score 13, diepte 1) > Yes, and we don’t expect anything final to be decided until the end summer, or possibly after count day.

I keep having friends/family freaking out and wanting to talk to me about it and I'm just waiting until the week before before making any decisions on what I am doing this year.

It's absolutely useless to prepare now.
[fuu9doo] (score 13, diepte 2) That’s when you call 911 and file a police report that you were just assaulted by a student. Because legally that’s what just happened. Schools will either take it seriously or they will get dozens of assaults taking mace i. Their buildings.
[futfyot] (score 13, diepte 1) My kids would complain about headphones. 5 minutes of use and they would take them off and just rest one side in their ear. I’m sure they’ll complain about masks.
[futk420] (score 13, diepte 2) I was hired midyear, so I was not offered the 12 month pay option. So I'm not getting paid over the summer. But, I qualify for $390/week from the state plus an extra $600/week in Covid relief. So I'm getting unemployment checks all summer
[futgfyw] (score 12, diepte 1) We’ve heard talk about also focusing on ELA, math, with science and history kinda on the back burner (since they tests more for ELA and math). 

Our reopen committee has also been quiet, for now. I’m under the impression that we’re waiting to see what LA does.
[futg8ii] (score 12, diepte 0) Being 100% pragmatic here, but during a pandemic remote learning environment it's exceedingly difficult to execute art, music, PE, etc programs and justify their expense in favor of other student supports.

Additionally, as much as I believe in a strong Kindergarten program at every school, remote school for Kindergarten is next to worthless and during a pandemic in person Kindergarten is just asking for the spread of the disease as 5 year olds are germ spreading machines that are impossible to reason with when it comes to social distancing.  

I have the utmost respect for the Arts, Music, Kindergarten, and all the rest you are talking about... but pragmatically it doesn't make sense to fully fund those programs when we are looking at hybrid schooling or fully remote schooling due to the pandemic, and kids need the structural support of technology and connectivity just to participate.  

------------

I'm an experiential educator.  I take kids on overnight field trips to camps, backpacking camping trips, and the like.  I also take them to organic farms so they can milk cows, to aviaries so they can see how honey is made, and so on.  I am the biggest advocate in the world for experiential education.  Nothing can replace actually going to the courthouse and talking with lawyers and judges or attending a city council meeting to learn about government first hand.  The amount of personal growth a kid can achieve at a week long mindfulness camp with their peers is massive.  All those experiences are monumental, both the long expensive trips and the cheap trips to the farm.

But you know what I expect the EE budget to be this year?  Next to nothing.  You know how many trips I'm going to get to take with kids?  Probably 0.  No sharing a tent or cabin (too dangerous in pandemic times), not bus rides to meet farmers (too dangerous in pandemic times).  

The truth is, while I'm passionate about experiential education, it's not feasible this fall.  Our school usually has all grade levels 3-12 go on an overnight within the first 6 weeks of the school year in order to bond with classmates, form memorable experiences, and learn about whatever grade level subject they are studying.  Absolutely 0 of those trips will be happening.  They aren't safe to go on right now.  It's not safe to shove 8 boys and girls into a tent or 12 into a cabin for the night.  

-------------

So, if I'm in admin, I'm looking at cutting Music, Art, PE, Experiential Ed, Kindergarten, and so on.  

We're talking about sending kids to school only half time and remote schooling the other half.  It's not feasible to run a quality art program remotely.  Either you have to massively increase funding to provide all kids at home with art supplies, or you have to dummy down your art program to the point of uselessness. 

I feel for Specialist teachers.  I feel for myself as an Experiential Educator.  But we might have to just accept a year of taking a different role in schools or just not working.

I won't be doing Leadership & Team Building Workshops with kids out in the forest this fall as physical contact and mixing makes it impossible.  Music teachers won't have kids sharing instruments or singing as both are dangerous and spread disease.  Art teachers won't be able to share supplies or work with one another on projects, as you can't share common contact points.  PE Teachers can't have games where kids interact, and breathing heavily indoors spreads disease.

----------

One of the things my school is looking at doing is asking specialists to take on classroom type roles where they use their classrooms for extension work.

So the Art room is now 5th grade extension and the art teacher supports 5th graders in their academic work so that they can fit students in the school socially distanced.  The art teacher takes direction form the 5th grade teachers on what the kids need and is a 5th grade supporter for the year.

That decision hasn't been made, but it's in the discussion.
[fut9nor] (score 11, diepte 2) Yeah, our district has a giant surplus right now and could guarantee jobs if they wanted. Their silence is terrifying. It seems like they want to save as much money as possible so they can upgrade our facilities.
[futhctt] (score 11, diepte 2) I totally agree. I teach art, and art teachers are flipping out about it keeping materials sanitized. I don’t really care, I’ll figure it out if and when I return to the building. I am working on my plan b though.
[futecpt] (score 11, diepte 1) I just left a rural CA district that scheduled all the HS teachers it could at 6/6, so no planning period. They are going to wait until enrollment is finalized in August and THEN teachers can opt out of their 6th period (per contract) and then they'll hire. 

I moved to Oregon where there seems to be a little bit of hiring happening. They were smart enough here to furlough teachers one day a week while they could collect the $600/unemployment and saved a lot of money for next year.
[futjyow] (score 11, diepte 1) How do you propose students will get their educational foundations, the ability to read, to know what numbers ARE if you cut kindergarten? That would effectively hobble an entire cohort of students.
[futqbri] (score 11, diepte 4) The short form answer is: I don't.  

I expect the learning to be stunted for this entire group of children, K-12, and that their teachers for the next few years will be doing foundational work to fill in the gaps. 

That's the reality we are currently living in.

--------

In other countries (Finland) kids don't go to school until a year later than we do, and they stay in school a year longer.  That switch might be worth looking at after this year.

I don't have all the answers, and I wish I could say there was an option filled with rainbows and sunshine but there isn't.  Any move we make to limit the spread of death and disease will hurt the education process.

I should also say that I'm not "advocating" for cutting Kindergarten.  I just don't see how Kindergarten can be performed successfully under the safety protocols, thus the sad option might be diverting the funding and faculty from it to supporting students elsewhere.
[futgovz] (score 11, diepte 0) My district isn't cutting classroom positions at present, but they're also not hiring because of the uncertainty in enrollment. If enrollment is low enough, or budgetary issues look worse than currently, I imagine they'll cut late. They also might hire late if enrollment increases or remains the same (since they're not replacing positions except at Title 1 schools that are hard to fill). I don't think anyone can know much for certain this year, truly.

  I don't know your district but I am not sure it's "dragging their feet" so much as not knowing so much: what the federal government might give, what the state budgets will be, what enrollment looks like, what schooling looks like, and how many teachers leave or retire early. Schools have no idea if they'll need to quickly hire or make deep cuts.  This is going to be a bumpy ride.
(151 reacties met lagere score weggelaten)

=== THREAD 1dnpku2 ===
SUBREDDIT: r/Teachers
DATUM: 2024-06-24  SCORE: 26  REACTIES: 147
TITEL: Best women’s shoes for teaching on your feet most of day?
POST (source_id=post):
Hello all! I’m going into my third year of teaching and starting to add to my work wardrobe this summer. 

I have very high arches and being on my feet most of the day, I end up with horrible foot pain at the end of the day. 

I need some professional, business casual shoes that won’t kill my feet please! Id also love any recommendations for casual comfortable shoes as well. I’ve heard good things about Hokas, are they worth the splurge for comfort? 

Thank you all!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[la46oar] (score 32, diepte 0) Look into inserts. Then you're not as limited in the shoes you can choose from.
[la4mbqf] (score 30, diepte 0) Dansk clogs or hokas are my go to’s
[la495nv] (score 25, diepte 0) I wear running shoes everyday.
[la4ug9z] (score 23, diepte 0) Another vote for Allbirds. A little more casual (I’m a primary teacher), but I have high arches too and they are my go to. I also love that most of them are washable. More than one kindergartener has gotten mine with puke 🤮
[la6llup] (score 22, diepte 2) Every doctor in the world will give you that note
[la4iw67] (score 19, diepte 0) I wear sketchers go walk
[la4h3lp] (score 17, diepte 0) Maybe just go see a podiatrist. They could probably give some amazing recommendations.

The most comfortable.work shoes I ever had were a pair of low heel sandals. I wore them all year, even in winter. I think that I have wide feet and just need to have room for them to breathe.

One of my teacher friends swears by hokas.
[la4e5bn] (score 12, diepte 0) I wear Air Force ones every day. Lol
[la6b6n2] (score 10, diepte 2) Try Clark's. Nurses love them and they have many styles. Or orthofeet (shoes and inserts). Honestly, google what nurses love to wear (they're on their feet for 12+ hours after all), but ignore Crocs. They might be comfortable, but I can't stand looking at them (ok, that's a me problem and I know that).
[la4ecai] (score 10, diepte 0) I have absolutely fallen in love with Allbirds. They’re expensive, but they aren’t lying with their slogan “the world’s most comfortable shoe.” The sneaker styles are more comfortable than the flats, but even the flats are MUCH more comfortable than normal flats. You can save some money buying through their “Re-run” program. Those are pairs that were gently used and returned (mostly just tried on and sent back because they were the wrong size).  

For situations where I need something a bit more dressy looking, I go with Clarks, especially their Cloudstepper line with memory foam.
[la65qkb] (score 9, diepte 1) I also have extremely high arches. Dansko clogs are my favorite in the winter. I wear nothing but Birkenstocks in the warm weather.
[la4bt3o] (score 8, diepte 0) Look into inserts that help bring the floor to your feet. I also recommend brands like brooks, Birkenstock, Hoka (if you can get past the chunky shoe look), on running, and dansko. Naot and Taos shoes could work too if you don't want the sneaker look. 

I work at a comfort shoe store for my side gig and I have a bunch of teachers that shop here. Those brands are what I and those other teachers tend to reach for.
[la4g03p] (score 8, diepte 0) Earth and vionic are both brands that have worked for me for years. Vionic's selection has gotten so much better in the last 5 years. Dansko is good too.
[la486js] (score 7, diepte 0) I have gone through several pairs of Brooks sneakers and love them!! My favorites are the GTS Adrenaline and Ghost styles, but I would suggest going to a running store and trying them on before purchasing. I wear those same sneakers for long walks on a regular basis. Very worth the investment to take care of my joints IMO.
[la65k27] (score 6, diepte 1 OP) I can get away with wearing running shoes on casual days or “jeans” day, but our district dress code is pretty strict. I would probably have to get a note from a doctor in order to wear running shoes every day.
[la4h5us] (score 6, diepte 0) I wear Hokas because I've had so many stress fractures and my foot surgeon recommended them. They have a thick sole, wide toe box, and mimic the motion of a surgical boot.


Con: They look like big tennis shoes in the way that Europeans can tell you're an American just by looking at your huge white tennis shoes.
[la5hq46] (score 6, diepte 0) I'm a man but my wife and I recently switched to xeroshoes and I never want to wear another brand of shoe again. My wife wears "Cassie" all the time. They are uncomfortable at first, the sole is very thin, flat, and flexible, you are essentially barefoot, but once you get used to it it's amazing
[la6sw02] (score 5, diepte 2) Gotta have the Birks for plantar fasciitis. Standing on my feet all day teaching art on a cement floor is a killer.
[la4zfl9] (score 5, diepte 0) Clarks, Vionics, Birks and Brooks running shoes with SuperFeet insoles are what my podiatrist recommended for me. In addition, I have a huge collection of funky, fun graduated \*medical-grade, 20-30 mmHg compression socks because I do not want varicose veins.
[la50ki5] (score 5, diepte 0) Birkenstocks fit my narrow feet and I can stand and walk comfortably all day.
[la4nqbb] (score 4, diepte 0) Clarks is a decent brand for work style shoes. 
However, you could get some black sneakers.  Better for your feet. My favorite female high school teacher  wore them every day
[la56s54] (score 4, diepte 0) I wear Dansko clogs or On Cloud runners most days. Sometimes converse all stars.
[la624mm] (score 4, diepte 1) Another vote from me for Xero shoes and other barefoot/minimalist shoes (there are tons of brands out there). They’re all I wear and have for about 7 years now. My feet have never felt stronger.
[la65mpl] (score 3, diepte 1 OP) Which inserts do you recommend? I’ve tried some in the past but they were very uncomfortable and gave me blisters
[la4gfxn] (score 3, diepte 0) Hey Dudes
[la57mkd] (score 3, diepte 1) I 2nd Hey Dudes. I love mine!
[la5j1cp] (score 3, diepte 1) 3rd! Love them
[la4lpoc] (score 3, diepte 0) Good quality shoes that support your feet, fit correctly, and are comfortable are worth the money. Also I heard don't wear the same pair everyday. Though it takes $ to build a good quality shoe wardrobe. 

You may want to consult with a podiatrist or a specialist regarding orthotics. 

Good shoes also help prevent ankle, knee, hip, and back problems. 

Well-fitting shoes will pay off over the long run.
[la8yt6t] (score 3, diepte 2) Adding to this for OP: Birkenstocks makes sneakers with the same footbed. I don’t feel comfortable wearing the birk sandals to work, but the plain white leather sneakers look good enough with business casual outfits.
[la4qmmk] (score 3, diepte 0) Hoka bondi 8 is great for high arches
[la4risj] (score 3, diepte 1) They absolutely are! I’d recommend Vionic and Birkenstock as well for non athletic options.
[la4y062] (score 3, diepte 0) Olukai shoes are really comfortable and not hideous.
[la5ghwz] (score 3, diepte 0) I wear Brooks with orthotics from a podiatrist during the day, but slip into Oofos recovery slides the moment I get home.  Those Oofos are amazing!!!  They take away foot pain in seconds and actually make your feet feel great!  (If you decide to get some and you wear a half size, go DOWN to the nearest whole size.)
[la635gt] (score 3, diepte 0) I broke down and bought oofos in April. I swear they are magic. I tried every insert there is, and none of them compare.
[la5me96] (score 2, diepte 1) I just tried going that route and the orthotics hurt soooo much.
[la7v6bz] (score 2, diepte 3) I think it was still too soon. I had a trip overseas three days after I got them adjusted and I had to take them out after my feet hurt so badly I wanted to stop walking. But it's a combination of bunion, arthritis, and new shoe plus new orthotic, so I think I was just plain doing things wrong. It has made me hesitant to try them again.
[la6bs2u] (score 2, diepte 2) You can get ones for about $50 from superfeet. Sadly, they didn't work for me, but I have heard good things.

I got the custom ones from Upstep. Cost about $250. They work great. Had major problems with plantar fasciitis, and after a few weeks, it is completely gone.
[la6p5tm] (score 2, diepte 3) Second for Clark’s!
[la70ds9] (score 2, diepte 2) get the doctor's note cuz it is not worth the pain
[la4lh18] (score 2, diepte 1) Who can afford those on  teacher salary?
[la4a54m] (score 2, diepte 0) My preferred shoe used to be Asics but I have Saucony now and I really like them. These are running shoes and I don't care about color or matching my outfit or that.im all about function over fashion.
[la65tef] (score 2, diepte 1 OP) Which inserts do you recommend? Thanks for the suggestions!!
[la4cann] (score 2, diepte 0) My wife wore Brooks Brothers running shoes.  She has serious arch and pronation issues, and they were the best shoes she could find.
[la4zolw] (score 2, diepte 1) AF1 or Jordan 5s are my go-tos.
[la4fnb2] (score 2, diepte 0) Orthofeet!!!!
[la699k9] (score 2, diepte 1) hoka is a french company…
[la5lb08] (score 2, diepte 1) Big fan of these!
[la663hs] (score 2, diepte 2 OP) Any specific type of shoe from Birkenstock? Thanks!!
[la51mw1] (score 2, diepte 0) I wore through three pairs of [Clark’s Partridge](https://di2ponv0v5otw.cloudfront.net/posts/2022/05/09/6279998a108a24bf84d3f4ea/m_wp_62799d6f4eeede08cb8d7309.webp) over 9 year.  Loved em.  Dunno why I transitioned.
[la595kg] (score 2, diepte 0) Skechers: Arch fit arcade
[la5elhx] (score 2, diepte 0) All Bird, Hey Dudes, and I love my Adidas court shoes! 

I’ve read that having a rotation of shoes is the most beneficial. I’m working on slowly building a closet of good supportive shoes, and rotating out my shoes with little/no support. Also, compression socks!!! Teachers really should be wearing them because of how much time we spend on our feet. I don’t wear them everyday but try to a couple times a week.
[la7nfyy] (score 2, diepte 1) My school's dress code is very relaxed and I wear Oofos to school often.  They also have clogs.  Absolutely love Oofos, most comfortable slides/flip flops ever.  I wear Brooks to run, and occasionally to school as well.
[la70yzx] (score 2, diepte 1) Yes! I've been wearing my Cassie's to school for a good 4 years or so. Wide toe box. Up until recently the Velcro started to give out (after daily use and occasional running in them lol) and I started shopping for a new pair.. turns out that they're discontinuing that line :( I emailed them to make sure. Good thing is that Anya's always has good recommendations for flats, so I'll probably look there next.
[la8gxif] (score 2, diepte 1) Another vote for Xero—they have ballet flats that allow the foot to be naturally positioned so that the foot builds muscles as nature intended.
[la5ju8b] (score 2, diepte 0) Sketchers
[la6yk47] (score 2, diepte 0) Dansko clogs are the best shoes I have ever worn.
[la6twdt] (score 1, diepte 2) Did you get custom made ones through the podiatrist? If so, they should not hurt at all after the break in period... And during the break in period you should only be wearing them a couple hours a day to start and increase slowly over a few weeks.

I got custom orthotics made in the beginning of October. Wore them to Vegas 3 weeks in, and I was the only one in my group who did not have sore, blistered feet after our 3 day trip, including a 12 hour festival.

If they are made by an podiatrist, and you're past the break in period and they still hurt, you should definitely go back in. Mine had a 3 month period where they would fix them for free if I had issues.
[lae0cpp] (score 1, diepte 4) Definitely give them another chance and break them in properly. I have arthritis, plantar fasciitis, bunions, and tendonitis.. I also had to buy a new, wider pair of sneakers, so I was breaking them both in at the same time. I started with 1 hour a day for the first few days.
[la6q3ko] (score 1, diepte 2) Footprint Insoles are great!
[la6u3ip] (score 1, diepte 2) Definitely go to a podiatrist and have real ones made. They are about $300, but sooo worth it! They will be truly formed to your foot and you have a professional you can go back to if they are not comfortable after the break in period (you need to start slow and build up the amount of time you wear them over a few weeks).
[la7k6ey] (score 1, diepte 2) My chiropractor’s office had a custom-made-orthotics service. $400 I’d get two pair specially made for me, and they lasted years. I’d claim them as a health expense.
[la5vs3p] (score 1, diepte 1) I agree with this, but my podiatrist recommended the Dyads over the Ghosts. I will say the Ghosts were comfy though!
[la48gev] (score 1, diepte 0) I wear all birds, and I love them so much I have 5 pairs.
[la49rf2] (score 1, diepte 0) Ferragamo
[la65phc] (score 1, diepte 2 OP) The fact that I’ve never even heard of the brand means that I can’t afford it lmao
[la4qet9] (score 1, diepte 1) GT-2000 were by go to shoes for nearly a decade, but then they changed them.
[la9jc1f] (score 1, diepte 2) It all depends on your foot! If you're just gonna get a generic one get a brand called power step. Cadence is another solid brand, as is aetrex. But it all depends on your foot.
[la4ci3f] (score 1, diepte 1) Happy cake day!
[la5u1md] (score 1, diepte 1) HAPPY CAKE DAY!
[la5zojl] (score 1, diepte 1) My AF1s are my most comfortable shoes!
[la6p936] (score 1, diepte 1) I didn’t know about the Rerun program! I’ve been wanting some Allbirds for years just couldn’t pull the trigger, thank you!
[la7g9rq] (score 1, diepte 2) I kept looking at the Facebook ads for two years and it also took finding the Re-run tab on their website for me to finally pull the trigger!
[la7nmnl] (score 1, diepte 2) 😆
[la6uzf3] (score 1, diepte 1) I bought 3 pairs of sketchers 7 years ago before the school year started. I don't remember the type, but they totally fucked my feet up. I rotated them, and by the end of the 1st quarter, I literally could not walk without excruciating pain. It came on almost out of nowhere. I was a traveling teacher (I went to 4 rooms per day), and they ended up having to give me my own room so I didn't have to get around. 7 years later, I still have pain on and off if I don't wear my custom orthotics that I had made last year. I saw similar stories online of feet ruined by sketchers. I will never buy them again.
[la4kd4p] (score 1, diepte 0) For comfort and cuteness I like Rieker and SAS. I also shop at Ecco. Those are my personal favorites.
[la4lycf] (score 1, diepte 0) My go to for cute and comfy shoes are Rieker, SAS, and Ecco brands.
[la6szig] (score 1, diepte 3) Omg yes!
[la4pzub] (score 1, diepte 0) I rotate different sneakers every day. I’m a bit of a sneaker head, so they are a part of my wardrobe.
[la4qa22] (score 1, diepte 0) I suggest you go to a running store, and have them take you through the rigors of finding the best shoe for you.
[la72zyt] (score 1, diepte 3) As I understand it, it’s the same footbed and then just different shoes on top for them. I’ve worn Lugano and Arizona sandals, and the Oswego and Bend Low sneakers. They’re all great.
(66 reacties met lagere score weggelaten)

=== THREAD i0b1jf ===
SUBREDDIT: r/Teachers
DATUM: 2020-07-29  SCORE: 432  REACTIES: 146
TITEL: Is anyone else trying to figure out how to put 32-36 students six feet apart when you couldn't fit them a foot apart last year at 29?
POST (source_id=post):
No?  Yall online?  Never mind.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[fzobc1m] (score 202, diepte 0) Brought this same "conundrum" to my principal. I have 35. Told him the desks won't fit at 3 ft. apart. Not even at 2. Asked me if I could move mine out. Already had. Sighed. Rolled his eyes. Looked up from his newspaper at me like: "Well, what do  you expect 𝘮𝘦 to do about it?!" 

&#x200B;

Golly. I dunno ... 𝙮𝙤𝙪𝙧 𝙅𝙊𝘽 ... ?!
[fzoebb0] (score 137, diepte 0) Set up your room with the desks you can at 6 feet apart. Then, put the extra desks 6 feet apart in the hallway to give your principal a nice visual of their bullshit. You could also put the extra desks in his/her office, no need to distance 6 feet then.
[fzojfho] (score 104, diepte 1) *Asked if you could move your personal desk out of your own classroom*
#FFS 🙄
[fzoeop5] (score 56, diepte 0) You can make a little extra room for them by not showing up.
[fzou2a4] (score 47, diepte 1) We just have tables, 6 per room. I can squeeze 6 middle schoolers per table. So if we're socially distancing seating, I'm gonna need no more than 6 students per class to make these tables work. No problem.

/s
[fzo94h1] (score 46, diepte 0) Increase the size of the room
[fzoaobx] (score 39, diepte 0) My superintendent announced that we'd be going back to in-person classes but hasn't said anything since. I figure they're not going to do fuck-all to reduce class sizes and no one will be able to do the six feet apart thing but it'll be like an expectation that they can ding us for on observations or blame us for not following when there's an outbreak.
[fzoyraj] (score 38, diepte 2) Jesus fuck.

The very first news story about a kid bringing COVID home to their parents, I have to expect that your superintendent will be there on the news telling the world that they TOLD ALL TEACHERS to maintain social distancing in the classrooms and they just can't believe that someone would be so irresponsible.

I'm horrified for you. I have no idea what my class is going to look like (my superintendent said he's not releasing any information for at least another week) but goddamn.
[fzojfwg] (score 37, diepte 1) Or decrease the size of the students
[fzpvmj2] (score 31, diepte 2) “What do [I] expect my principal to 𝗱𝗼 about it?” 

I expect him to give a fuck. I expect him to put down his newspaper, come to my room, look around, look at my drawings upon which I've sketched every known configuration, and have a crack at figuring it out, himself. I expect him to suggest we contract a carpenter and build a temporary loft to put six to eight of the desks upon. (I then expect students to fight over those seats!☺︎︎) I expect him to contact the local town hall to see if we could borrow or rent their scaffolded seating. I expect him to contact the building inspector and fire marshal and get either approved, and if they cannot, for them to contact the state and either get a waiver or lodge a complaint. I expect him to look at the school's blueprints and rearrange class configurations to where each class 𝗰𝗮𝗻 have a room to fit 𝗮𝗹𝗹 of its students. Failing that, I expect him to contact the superintendent and invite him to see for himself. While he's here, he can inspect the other 7 classrooms and teachers in the same boat - especially the one that will have 42 desks and students. I expect him to contact the parents of my students to see if any would be willing to go virtual (ha!) or be put in another section, taught by a yet-to-be-determined-teacher (double ha!). I then expect the superintendent to contact our School Committee and the DOE, and demand they okay a hybrid or virtual model, and 𝗻𝗼𝘁 leave it solely, as it was, for the parents to decide. I expect 𝗮𝗹𝗹 to admit one 𝗰𝗮𝗻𝗻𝗼𝘁 get blood from a stone, and that I 𝗰𝗮𝗻𝗻𝗼𝘁 fit 35 students in my room and simultaneously be in compliance with what my administration is telling me I 𝗺𝘂𝘀𝘁 be in compliance. I expect him to realize this is 𝗳𝘂𝗰𝗸𝗶𝗻𝗴 𝗠𝗔𝗗𝗡𝗘𝗦𝗦. 

Then, I expect him to visit the 7 other classrooms and repeat all the above steps. 

I'm sure it goes without saying: 𝗜 expect to be disappointed, if this is what I am expecting my principal to do. But, I'll keep hoping and I'll keep going to him, because my students and I need and deserve to be safe in that room. It is 𝗡𝗢𝗧 my job to figure out for my principal, nor the superintendent, nor the school committee, nor the parents, nor the CDC, nor the WHO, nor DeVoes, nor Fauci, nor Trump how to cram 35 anxious and bewildered teenagers into a box made for half that number. 

𝗜 𝗲𝘅𝗽𝗲𝗰𝘁 𝘀𝗼𝗺𝗲𝗼𝗻𝗲 𝗯𝗲𝘀𝗶𝗱𝗲𝘀 𝗺𝘆 (𝘁𝗵𝗮𝗻𝗸 𝗚𝗢𝗗 𝗳𝗼𝗿 𝘁𝗵𝗲𝗺) 𝗰𝗼𝗹𝗹𝗲𝗮𝗴𝘂𝗲𝘀 𝘁𝗼 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗖𝗔𝗥𝗘. 

Parents chant, "Do your job! Do your job!" 

Yeah? Believe it or not, that's exactly what I'm 𝘁𝗿𝘆𝗶𝗻𝗴 to do.
[fzoxtfk] (score 30, diepte 2) High school science here.  I can definitely fit 6 in my room with 6 feet between them and maybe 9 students if they sit completely still.  I cant move my desk out as it's permanent (which is really annoying because when they installed it they put if in crooked.)
[fzoohmm] (score 30, diepte 1) Oh...that is a good one. Dang, the zing is so zingy!

In all seriousness, this is my plan. Holding out to the last minute and then quitting if I have no other option.
[fzol0xd] (score 26, diepte 2) Is this a school for ants?
[fzoyfu3] (score 25, diepte 1) My school is doing normal class size, recess, lunch, and transportation.
[fzp0nzv] (score 25, diepte 1) Mine said “ Well that is a challenge” and walked away. It’s not a challenge! It’s literally impossible in my space.
[fzp5vi7] (score 24, diepte 1) My state said the max you could put in a classroom was 1 per 35sqft (including the adults).  Made it easy to say "My room is 400 sqft, that means 10 kids and 1 adult or it's not safe."
[fzo9akn] (score 21, diepte 0) Thoughts and prayers, obviously. Sheesh. Easy.

/s
[fzq1eh2] (score 20, diepte 2) I’m sure they’re sticking up for teachers the way they always do!

/s
[fzorw4a] (score 18, diepte 1) hahaha! THIS.
[fzogtal] (score 17, diepte 0) Have you tried [duct tape](https://previews.123rf.com/images/luislouro/luislouro1302/luislouro130200049/17669810-young-boy-glued-to-the-wall-with-duct-tape-so-daddy-can-relax-and-have-a-beer.jpg)? Duct tape solves lots of problems and can be used for a [quick make-shift mask](https://clf1.medpagetoday.net/media/images/86xxx/86071.jpg) (but this person forgot to cover the nose area).
[fzozszx] (score 16, diepte 1) Have we considered 6 feet of vertical height? Maybe some desks can get attached to the ceiling?
[fzp4qo1] (score 16, diepte 2) Reschedule the kids? Tell central office that they need more teachers to enact their plan?
[fzoveif] (score 16, diepte 0) So pumped for my class of 75 socially distanced choir students....
[fzpypha] (score 13, diepte 4) Its built into the floor.  Its more of a demonstration lab bench but its really my desk.  When they installed it while building the school they put it in crooked.  If I were going back in the fall I would fake a picture of it.  They also did a poor job planning the school as they bought larger windows than what was needed.  The ceiling slants up towards the top of the window.  And there has been a leak in thd room since I have been there.  They have attempted to fix it multiple times.
[fzodc99] (score 13, diepte 0) My classroom holds 8 students. I have no idea how that’s going to work during the school year. Luckily my biggest class only has 14 students.
[fzp7i87] (score 12, diepte 1) "I honestly expected nothing, but I hoped to be proven wrong."
[fzp1g3g] (score 12, diepte 0) Why are they opening schools anywhere right now. It’s a disaster waiting to happen. I don’t understand why children and teachers are going to be the tests.  The case number is going to rise very fast.
[fzonp8d] (score 11, diepte 3) Stack them like Lincoln Logs. That's what I have to do.

My room has a official certificate of occupancy for no more that 12 people. I have to fight to get it down to 30. It usually starts the year at 35 to 37. Have to step outside to change my mind.
[fzq7e0g] (score 11, diepte 2) I am well aware - but I also know that it is their responsibility to make sure that they communicate all building needs to higher ups and not leave teachers in a more vulnerable position because they don’t want to do their job and say that the higher up’s plan WON’T work. Not for their staff, not for their building, and not for their community.
[fzpyi8k] (score 10, diepte 1) Seriously though. Do it. Oh my, imagine the impact if many teachers worked together to put all their “extra” desks 6ft apart in the parking lot!
[fzonn5x] (score 10, diepte 0) The building we’re in is old - an original of the mid-1900s.

I can barely fit in 28 students without blocking my cabinets and needed spaces. Our desks are the old one-piece tray table design and are too small for normal work, which means there is no space between people in a row by design.

Even if half my classes went online, the kids wouldn’t be properly spaced. And my room isn’t the worst layout.

To top the cake, my windows don’t open, so there’s no way to cycle in fresh air unless it’s the A/C, which pulls from the hall. I’m sure that won’t be an issue. /s

Somebody save us all.
[fzqk8dy] (score 9, diepte 1) A real teacher would do demolition work and drywall their room in the 2 hours between PD sessions before students arrive. 


Note: this is 100% sarcasm and is my "I am a male Karen with sunglasses and a goatie in front of the american flag in my profile picture on facebook" impression.
[fzp1yi5] (score 9, diepte 1) Why don’t they send the superintendent in there to fix it and have the superintendent teach the class for a few days if it’s so safe then they should have no problem being in a classroom. 

Also do they reaally think students will distance even if there is room, not to mention if one has it will they quarantine the whole class. Plus the teacher, and what if they have to quarantine the teacher, are there subs willing to risk it right now? 

Is it either work or run the risk of getting infected and dying, is that what this has come to.

Why can’t they just accept online learning is the best option and have every state do it or at least the ones with rising cases but it should be every state, and have it for the first few months at least, and wait to see if the cases go down and come to a stop almost and not put all these teachers and students in danger. It’s frustrating very frustrating.
[fzpyvxe] (score 9, diepte 5) Make a game out of it to new students. Simmering like how many poorly constructed things are in the room or how of centered things are. Lol.
[fzpyp2h] (score 9, diepte 3) We can and should expect more from bosses who are leaving all of this in our hands as though we can work space-bending magic!
[fzobyby] (score 9, diepte 0) Fairy dust!
[fzoy28s] (score 9, diepte 1) That is a thing of wonder splitting your classes like that.  Sounds like when I would give my sister "half" a cookie when we were younger.
[fzowag9] (score 9, diepte 0) We opened up in June. I was able to get 9 desks in my classroom with appropriate distance. Anymore and they would be too close.
[fzozxqm] (score 8, diepte 2) I think I'd invest in a Hazmat suit to teach in at that point.
[fzp1ejk] (score 8, diepte 0) I'm going with what I have termed the "Lord of the Flies Scenario."

I have, in the middle of my 662 sq. Ft. room (18 safe spots max" 10 desks.  Then, lining the walls is the remainder of my group desks (we have no more individual desks) with enough chairs to fit the rest of my class (average 32 kids).

I figure that will at least keep as many safe as I can.  Plus, after reading the vast amount of hate mail and attending the board meeting, the community should be fine with that.  After all, to quote a school board member, "We need to be significantly less worried about the physical health of children and their parents and more worried about their emotional health."

So, that's my plan, what's yours?
[fzpz46r] (score 7, diepte 6) Oh i always tell the students about it.  First day I normally say something like, "so if you like things being perfectly straight come check out the angle of my desk.  Then check out the ceiling."
[fzp4hdc] (score 7, diepte 1) Our district in Oregon is looking at A/B days when we’re able to return. It’ll be a hybrid model of in person and online.
[fzq2540] (score 7, diepte 2) if you're referring to cdc guidelines, etc., yes - i think it's (mostly) understood it's not (mostly) principals making these decisions. communities, parents, governments, yadda, yadda, yadda have made them. i think, however, it IS admin's job to HELP. To CARE. To realize their teachers are trying to get curriculum and lesson plans and 504s and IEPs finished and don't have TIME to spend their days figuring out how to please the higher-ups. it's NOT a teacher's job to figure out their district's overcrowding issues. is it their concern? sure! covid or no, teachers KNOW an overcrowded classroom is often a HIGHLY challenging learning environment.
[fzq615e] (score 7, diepte 4) first of all, i can't and wouldn't put the overflow in the hall or elsewhere, (although i 𝘥𝘰 own a sense of humor and thought the suggestion was terrific.) i don't know what i'd "want him to do" - because 𝘪 𝘸𝘰𝘶𝘭𝘥𝘯'𝘵 𝘬𝘯𝘰𝘸 𝙬𝙝𝙖𝙩 to do - that's why i'd be in his office. it'd be great if he'd brainstorm with me, help me figure it out, realize it's not my job and precious time is being wasted on "getting blood from a stone" -  like a poster above said. call some higher-ups. i don't know, exactly. care? help? exercise the authority he has, and i do not?
[fzor0p7] (score 7, diepte 0) We are doing an A/B spilt, so only half the kids are there at a time.  But one “half” of my first period class has 21 kids.  The other “half” has 8.  There’s no way I can appropriately space 21 teenagers.
[fzotq2h] (score 7, diepte 0) Well you could put half the desks on the floor and then suspend the other half from the ceiling. /s

(Another more sincere idea: couldn’t you agree with parents to “suspend” students from school every day and then teach them remotely? Write them up for phony offenses so they must leave school, you know? Might only work with students whose parents can work from home but it’d keep kids out of the physical classroom)
[fzpafj1] (score 6, diepte 2) I like the cut of your jib!
[fzp1f8d] (score 6, diepte 2) Good lord. Are you in Indiana, by chance? Because that’s happening here, too.
[fzqjqk2] (score 6, diepte 4) I get it, we’re all in bad positions. But someone needs to take responsibility because we’re not all going into this voluntarily. In my state it is the district’s choice, and my superintendent has stated that many decisions (including how lunch is handled, who is approved to not wear masks, and 3 foot apart seating arrangements/accommodations) are to be made on a building level.  SO, I feel perfectly fine placing blame all the way up the ladder for the myriad of bad decisions being made.

Edited to include some items that my principal has been given responsibility for
[fzokk0s] (score 6, diepte 0) Why are you trying to figure it out?  Walk in, too many desks, walk out
[fzol9qp] (score 6, diepte 0) Yeah, it's pretty easy in my classroom, which is big but not huge.

I'm going to take a rope and cut it down to 72". I'll place one chair at one end of the rope and the next chair will be placed at the other end of the rope. each chair, desk, and student will be exactly 6 feet apart so long as you measure along the same circuitous route that I used to  lay out my rope-measure.


That or I'll need to buy some 2x4s and build a loft.
[fzpa0vs] (score 6, diepte 1) No. Do not spend money
[fzpybay] (score 5, diepte 3) Texas. In a Hotspot area lol..
[fzpasa4] (score 5, diepte 2) Us too! And students under 10 do not have to wear masks, which is about 680ish kids. Adults do have to wear masks.
[fzt5qom] (score 5, diepte 2) They removed our for us.  Then after much complaint they came back.
[fzpvgxt] (score 5, diepte 3) They nailed your desk to the floor? Is it a stand alone desk or like a huge console with drawers and cabinets?
[fzpduml] (score 5, diepte 2) Recommended is 113 sq ft per person.
[fzpew1g] (score 5, diepte 5) Two 6-foot radius circles next to one another put those at the center 12 feet apart, not 6 feet apart.

Who recommends students are 12 feet apart?
[fzov1rd] (score 5, diepte 1) This is the only logical conclusion
[fzr9a22] (score 5, diepte 4) It is not unreasonable to expect a level of validation and support from the principal. They can at least acknowledge the impossible situation.

Why is it unprofessional to say to your staff that I have tried to bring your concerns to the higher ups?
[fzovb5r] (score 5, diepte 0) We’re only required to do 3 feet and I’m trying to fit in 18 desks and have room for myself 🤦🏻‍♀️. I have the smallest room in my grade level and so far have crammed 16 desks. SMH!!!
[fzoy24e] (score 5, diepte 0) I'm not even going to try. I'm going to let it be the shit show that it is. I will wear a mask and enforce wearing masks in my classroom. That is all.
[fzp40j4] (score 5, diepte 1) This is my plan. Wait for the inevitable shitshow, outbreak, and reversion to online-only.
[fzpflrw] (score 5, diepte 0) You have 36 students in a class? Thats really high!
[fzpvi2h] (score 5, diepte 1) Uhh, I have some bad news for you...
[fzq45ov] (score 5, diepte 0) I cannot believe that at the very LEAST some districts aren't splitting classes so social distancing can be attempted. That is truly mind boggling to me.
[fzolfm9] (score 4, diepte 2) I think chopping off a kid's legs might be a little extreme.
[fzqfv41] (score 4, diepte 2) Students are going to not be social distancing the minute the teacher turns their backs. Problem is, many teachers don't believe in social distancing and protocol either.
[fzpe7pg] (score 4, diepte 3) But then students are 12 feet apart?  35sqft is 6 feet apart (in theory, not practice)
[fzsr9a1] (score 4, diepte 1) Seriously.  I don't know why so many teachers think they can bend time and space to do this.  It's a legit impossible task.  

Tape out boxes on the floor where the desks can be spaced out, place the desks, push the rest into the hall and space them out in the hallway.  

If you have student's names already, label each desk with the names alphabetically and when you run out, label the ones in the hallway.  If the school doesn't solve this problem before the first day, you're going to have a fuck ton of angry phone calls and that's what will solve this shit.  The school and district are supposed to solve this.  

You can't. You can't solve this.  It's not a word puzzle in a math class which has a solution.  It doesn't.
[fzomkii] (score 4, diepte 0) It isn't possible! I guess you can push some again walls, but still not with 25+ desks. I have about ~22 kids, and my desks are 2-3ft apart unless I put them facing walls. 

You shouldn't have to spend your own money, BUT a clear curtain and a clothing rack solves the problem. You can buy the curtains from Amazon or the dollar store (around $4-6). Wal-Mart sells the clothing racks for $9.
[fzovuyq] (score 4, diepte 0) My local govt literally said "if those class sizes actually exist"
[fzp0z4o] (score 4, diepte 0) My school is running 50% on Mon/Tues, the other 50% Thurs/Fri.  Students will be virtual on days they’re not in my classroom.

I have 26 kiddos - the desks are set up in 13 groups of 2, one desk for a MT kid, the other for a ThF kid.

Mind you, I have barely any other furniture - my storage wardrobe and 2 bookshelves against the back wall, then my desk are in a corner.
(72 reacties met lagere score weggelaten)

