# Label-batch batch_0048

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
Schrijf het resultaat naar `batch_0048.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 17b51si, 111acbz, 1b28wao).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 17b51si ===
SUBREDDIT: r/Residency
DATUM: 2023-10-18  SCORE: 569  REACTIES: 123
TITEL: AITA for telling my patient doctors love feet?
POST (source_id=post):
This morning I was finishing up an assessment of my patient, and I requested to have a look at their feet to check for pedal edema and other things. While doing that, I inadvertently said “doctors love feet“. I realized that didn’t sound right, and I quickly added, “for medical purposes, of course”. There was a very long, awkward silence, and my patient was looking at me strangely, while I palpated their feet. For clarity, we are both the same sex. I then followed up with “that didn’t come out right, I meant doctors like to look at their patients’ feet to make sure there’s nothing wrong going on“. The patient continued to look at me very strangely and didn’t say a word. Luckily they discharged today. AITA?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k5h7jw2] (score 618, diepte 0) Today I said “I want to see you pee” to a patient. 

It was a postop patient who was awaiting discharge pending spontaneous voiding after a Foley removal. Sounded weird tho
[k5h9su0] (score 397, diepte 0) Rip. You’re going to be reminded of this moment on a random night while you’re laying in bed, 10 years from now.
[k5h9jdg] (score 368, diepte 0) When I was in med school we had to do a fake patient visit to talk about goals of care including whether the patient has a living will or advanced directive. My poor friend: “sir, did your brother ever have a will to live?”
[k5hfk3a] (score 276, diepte 0) Just usual physician autism, it's fine
[k5hmaef] (score 262, diepte 0) When I was in the hospital at age 16, my surgeon who had been trying to figure out what was wrong with me came into the room one morning and said “I was thinking about you in the shower last night.” I started laughing and he realized how it sounded and went beet red.

Sorry your patient didn’t have a sense of humour!
[k5hfypr] (score 231, diepte 0) One time I was taking a history and I meant to ask “do you drink alcohol?” And instead I said “are you a drunk?”
[k5i42pc] (score 154, diepte 1) My classmate once accidentally asked if they smoked alcohol. They replied “do you??”.
[k5h8vqy] (score 151, diepte 1) I’ve definitely told patients I wanted to see them poop before I sent them home.
[k5hhk6f] (score 148, diepte 0) I’m an attending (F) and I accidentally patted a 20s M patient butt after doing a rectal exam for abscess. Didn’t even realize I did it until the nurses laughed at me when I came out of the room
[k5hnvtu] (score 147, diepte 0) it was a little weird the first time you said but it got exponentially weirder every other time you brought it up.
[k5hm1j8] (score 130, diepte 0) Not even the worst thing I’ve heard said to someone. And sounds like you quickly clarified what you meant. For a more horrifying story, when I was a med student doing ObGyn I had an attending teach me how to do papers and bimanual palpation, then proceeded to have me do it for all her patients why she wrote notes and supervised. I always described what I was about to do and said if you fell uncomfortable in anyway let me know. 

One young lady comes in and during bimanual made a strange noise. I stopped immediately and was like “I’m sorry, are you ok.”  She responded “no I’m fine” then mumbled “just felt good”.
[k5ig1kb] (score 95, diepte 0) I once tried to tell a patient I was gonna do a sedation and reduction for their dislocated shoulder and instead said, "Sir, we're gonna have to do a seduction on you."
[k5hskut] (score 88, diepte 1) It’s ok, many of us don’t have a will to live, so I feel like that’s a pretty valid question
[k5hibkm] (score 84, diepte 2) I’ve said both of these things to patients and never thought twice about it until now
[k5jldv5] (score 75, diepte 1) Love the notion of surgeons having shower thoughts about active challenging cases.
[k5hy1yj] (score 74, diepte 1) Would you like to do my bimanual exam?
[k5hrsfo] (score 72, diepte 1) I used to tell HF exac pts the only job you have while in the hospital is to pee.  They laugh.  Then I give another 40 of lasix.
[k5i1vgo] (score 69, diepte 0) I had a patient with Brown-Séquard syndrome after a stab wound to the neck who had decrease motor function on the right with sensation intact and normal motor but decreased sensation and lack of sweating on the left, and I said, “at least you save on deodorant.”
[k5ian3c] (score 67, diepte 2) “The next time you poop, don’t flush it. Tell the nurse. We want to see your poop.”
[k5hhz8p] (score 63, diepte 1) This made me laugh. Very relatable comment.
[k5hq1fq] (score 63, diepte 0) Our feet are especially good when we put them in our mouths. 

Stuff like this happens all the time. The first time I called someone’s daughter/sister/mother/brother etc their spouse, I swore I’d never make that mistake again. Guess what? Still happens sometimes. Eventually you’ll laugh about it because this really is an excellent story.
[k5icw5e] (score 61, diepte 3) “I want you to walk down the hallway. No, I want to watch you coming *and* going.”
[k5hs6yq] (score 59, diepte 0) When I was running behind in clinic one day in residency I told the patient “sorry about your wait” which sounds exactly like “sorry about your weight.”
[k5j7dv7] (score 55, diepte 0) One of my interns last year was on her ED block and needed to do a rectal on an older lady. The woman asked what she was going to do, and the intern replied “I’m going to stick my finger in your asshole”. 

10/10 patient encounter.
[k5hidj7] (score 51, diepte 0) We all say dumb shit. You're just building your collection.
[k5ia81z] (score 51, diepte 0) Well. I was doing a rectal exam and told the patient that everything felt normal. With the finger still inside him. His reply was " it definately doesn't feel normal to me!"
[k5honol] (score 49, diepte 0) YTA for lying to your patient. Fuck feet, they’re nasty.
[k5ixi83] (score 42, diepte 0) Was dead exhausted from a 48 hours shift in pediatric emergencies. Here comes this mom at 4:30 am with her son and husband and a trail of explosive diarrhea.
Just look at her dead in the eyes and said : Does he usually shit this much?, using shit and not defecate, the room went silent the nurse gave me a very concerning look until I realized what I just said. The mom straight up answered me : No he doesn't and she had more things to care about than my weird ass phrasing.
[k5i65fw] (score 39, diepte 0) I once heard someone in practice osces tell the actor "im now going to auscultate using my bell end", as he rotated his stethoscope

It happens
[k5hajbl] (score 37, diepte 0) Lol I’ve made that joke a thousand times in the neurology resident room but never in front of a patient
[k5jtguw] (score 33, diepte 4) Ha! I’ll never forget doing genital exams on a standardized patient in school, I was crazy anxious and got my wires crossed between asking him to pull down his trousers and telling him I was going to start by examining his penis, and instead asked him to pull down his penis. Also, the guy was kind of joking around with me to keep it lighthearted, and asked to see my fingernails before the DRE - and I looked the poor guy straight in the eye and said “I clipped them just for you.”
[k5l9xa5] (score 31, diepte 1) Why say many word when few word do trick
[k5jhd4n] (score 31, diepte 0) I once needed a urine sample from a patient and instead of saying, “I need you to pee for me, please” I said, “Please pee on me.” I didn’t even try to make it better or correct myself, I just put the cup down and walked out of the room tehehehehe
[k5ikxtj] (score 27, diepte 1) Done this so many times. Now I say:

To patient "Who have you brought with you today?"
To random person at bedside "Are you a friend or a family member?"
[k5hxwnl] (score 26, diepte 1) Did he appreciate it?
[k5ji0sv] (score 26, diepte 0) I once told a paraplegic patient she could just walk in to get her labs anytime.
[k5j6la5] (score 25, diepte 0) I’m a radiology resident and I was doing a voiding cystourethrogram on a 4 year old girl. At the end of the exam we use live X-ray while the patient urinates to check for reflux of urine into the ureters/kidneys. What I told mom was “I just need to get some good pictures of ‘daughters name’ peeing and then we are good to go!” 

It was hard to work those words back lol
[k5ju2rl] (score 23, diepte 0) I feel like you made it weird by following up with more comments about it.

When I was a medical student during my OSCE a patient had a "*b*urning *itching* rash". I was a nervous and stumbled over my words accidently saying "When did your bitching start?". I was mortified. I wrote a formal apology email to the fake patient and the module director. They both had no idea what I was talking about until they went back and rewatched the tape. It was fine, we all had a good laugh about it later.

Point is they probably wouldn't have even noticed if you had just stopped at the initial comment.
[k5jdv3b] (score 22, diepte 2) After that, they're AFRIAD to laugh.
[k5hkzho] (score 22, diepte 0) These shitposts are getting more and more convincing.
[k5j24n0] (score 22, diepte 2) ☠️
[k5k89gb] (score 22, diepte 1) Sometimes it's important to know when to drop the shovel
[k5hjdf9] (score 21, diepte 0) Idk sounds like a Freudian slip to me
[k5k83t5] (score 21, diepte 0) It only becomes a bit problematic if you're a podiatrist.  Regularly I'm asked if I have a foot fetish.

No ma'am. You have toe nails that are 2 inches long and and a half a centimeter high. If I did, you ruined it.
[k5iq4in] (score 20, diepte 1) Omg 😆 hahahahhaha
[k5hzgfd] (score 19, diepte 1) >Today I said “I want to see you pee” to a patient. 

And it wasn't even *your* patient, which made it **super** awkward.
[k5hvip3] (score 19, diepte 0) Why are you all so weird?
[k5j2nvg] (score 18, diepte 1) Where I'm from were actually encouraged to use day to day terms with the patients so they understand what we're talking about. Idk if I've ever said defecate to a patient 😶‍🌫️
[k5jeao5] (score 17, diepte 1) I just ask "and what is your relation?" no matter how obvious it seems.

Surprises are rare, but still helpful.
[k5jg8jk] (score 17, diepte 0) I told an attending “I haven’t felt that many breasts” while learning the breast exam in med school. He had quite a chuckle over that one.
[k5hw9e6] (score 16, diepte 0) So long as they were not a diabetic amputee you’re good.
[k5iq3en] (score 14, diepte 2) I died laughing 😂
[k5lrr7i] (score 13, diepte 1) Agreed 100%. Sometimes it’s best to just take the L and not try to explain yourself.  You’ll often just end up  making matters worse 

There’s actually a chance the patient didn’t interpret the comment as inappropriate initially. But after following up with “for medical purposes only”, that sealed the deal
[k5ifws2] (score 12, diepte 0) Somehow (I still can't quite work out how it happened) I made a pretty woman comparison with my patient being Richard Gere and me being Julia Roberts. I swear I'm normally very professional
[k5j2uia] (score 12, diepte 2) I mean I could've used something with more tact than does he usually shit this much, but oh well, atleast the job is done 🤷‍♂️
[k5j5cf7] (score 12, diepte 0) Oh god all the explaining makes this so much worse
[k5i8tsa] (score 11, diepte 2) Lol I have no idea 😂
[k5ju9ey] (score 11, diepte 1) I asked a colleague’s wife during a scan if she was his daughter. She loved it. He didn’t and told me so later.
[k5jtry5] (score 10, diepte 3) Recently had a guy with melena and pretty significant anemia, and his wife, bless her, went in and took photos of his poop every time he went to show me later. It was very helpful.
[k5k4v4b] (score 10, diepte 5) Went to a stabbing (a guy on drugs tried to stab his friend but stabbed himself), and whilst taking him to the ambulance another friend pulled me one side and gave me a plastic carrier bag and said “you might want to take this”, all that was inside was a turd.
[k5kjzpv] (score 10, diepte 2) A patient did this to me as a med student when I asked “are you sexually active”…I was flustered to say the least
[k5jm3im] (score 10, diepte 1) I’m more impressed at getting a 4 year old to pee on demand.
[k5jxhli] (score 10, diepte 0) I am a hospitalist. I always say “I hope I don’t see you again” when I discharge patients.
[k5iq5l8] (score 9, diepte 2) OP’s not even a doctor but the relative of another patient. Super awkward.
[k5ji0nh] (score 9, diepte 0) I'm not even remotely related to the medical field. But I come here for these threads.
[k5igq7l] (score 8, diepte 2) I mean…in college…
[k5lbsda] (score 8, diepte 1) Lol. For me, I was trying to ask a patient how much Weed they smoke. Sounded like a narc, when I said, "Sir, how much marijuana do you smoke". Straight from the Hello Fellow kids meme
[k5lba6k] (score 8, diepte 0) I had a male gyno once tell me reassuringly that a certain diagnosis “didn’t mean [I was] a slut.”

o.O
[k5lwfpp] (score 7, diepte 6) Lmfao, WHAT?! Now maybe it’s bc I’m not a doctor (idk, how I ended up here but now I’m so f’ing glad I did!) but WHY would you need to take his turd with you?! Is this Southpark?!  Was it Mr. Hanky?!
[k5j47jg] (score 7, diepte 1) I asked a patient and someone screening them for substance abuse resource follow-up if they were an item. Tbf in my defense the screener was casually dressed and the two of them had some good banter.
[k5jbjj4] (score 7, diepte 0) Nah most patients find it funny, reminds them you are human !
[k5ji82r] (score 7, diepte 0) You should’ve just stopped talking lmao. Every single addition just made it worse and worse.
[k5k0887] (score 7, diepte 0) This thread gave me and my healthcare-worker parents the greatest laughs in a while 🤣🤣🤣
[k5lsal9] (score 7, diepte 0) I am a female, retired.  Early in my career, I worked with a male physician.  For male patients, the digital rectal examination was vital.  Often, the patient complained about a woman performing this uncomfortable procedure. 😏  I'd hold up my two little fingers and say, "did you say you want him, **or me**, to do this rectal exam?".  It worked like a charm. 😁
[k5mr571] (score 7, diepte 0) I have (more than once) told a patient to touch their finger to my nose during a cranial nerve exam.
[k5k165g] (score 6, diepte 5) I did have a patient who came in for recurrent nosebleeds bring me a bag stuffed full of her bloody tissues from the past week, so that was fun.
[k5lxahl] (score 6, diepte 7) Y'know, for good luck.
[k5izzj4] (score 6, diepte 2) Valid response 🤣🤣😭😭🤣😭
[k5iy2t5] (score 6, diepte 0) One time I asked a patient “are you hallucinating?” in front of the entire team
[k5knhnn] (score 6, diepte 0) My SO obgyn said she has a nice healthy vagina. That kind of weirded her out. When I worked on OB I kept those thoughts to myself. I’m very clinical with patients because I feel like it can be hard to re establish after something awkward happens or is said. I probably don’t come off as fun or whatever but that’s ok.
(47 reacties met lagere score weggelaten)

=== THREAD 111acbz ===
SUBREDDIT: r/Residency
DATUM: 2023-02-13  SCORE: 1133  REACTIES: 123
TITEL: Is there any REAL (ie legal) reason that I can’t wear Heelys on wards?
POST (source_id=post):
Can you imagine cruising down the halls, smashing orders on the COW, and high fiving every sub specialist you come across, without your feet even moving ONCE?

Intern year coming up and I’m just trynna be as efficient and as fly as possible out there.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j8dwm4x] (score 587, diepte 0) A few years ago an intern used to bring a razor scooter on night shifts to get around the hospital. I was the over night consult resident at the time. We would use that shit to get around and it was amazing. We were mostly met with people who said “that’s genius”, but we occasionally had to juke and outrun the security guards. 

We made it through the whole month that way. It was so fun
[j8dr7wk] (score 552, diepte 0) I'd pay to see that.
[j8dwxo0] (score 351, diepte 0) I used heelys as an attending ER doc, this was at a single coverage community shop. Super fun. Left lots of marks on the floor though....
[j8dxd88] (score 198, diepte 1) Mind you, only on weekends. I'd think if management found out they'd throw a fit.
[j8dyw5t] (score 193, diepte 0) I had a coresident (EM) who wore vibram five fingers (the toe sock looking shoes) and, while there wasn’t a rule about it, it pissed off our department head something awful and he instituted a new no five fingers rule.
[j8e4bsw] (score 186, diepte 1) No need to clarify what specialty. EM activities 100%
[j8edvia] (score 151, diepte 0) So, all jokes aside, I did this. I was a tech in the ER, I just lurk here, so sorry 😂

Back when I was 18-20 I was stupid, more so than now, anyway, I wore heelys and would heel around. No one minded, I worked the night shift so there weren't any administrators to be mad about it. I wore them for about two years. Fast forward to 2018, there's a hurricane. I'm walking to my car  after shift and slip. I fell in the breezeway of the ER because my feet aren't fully planted cause of the wheels. I fall straight down and get an open, comminuted fracture of the patella. Bed bound for months. Literally years of recovery, surgeries, and physical therapy to finally get it back to normal. 

Please don't my reddit friend :(

P.S.Edit to add now I work in public health regulation; if I had to bet a dollar, I'd say it isn't illegal for you to wear heelys. Although, employers have a requirement to maintain the safety of employees through physical means including uniforms. If they fail to prevent you from wearing heelys, they could get in trouble. 

TLDR; I done messed up in the past and broke my patella with heelys at my hospital job. It isn't illegal for you to wear heelys but it may be illegal for your employer to not stop you from wearing heelys.
[j8dspjo] (score 132, diepte 0) Arizona (peds surgeon) did on Grey’s Anatomy so it must be fine.
[j8edama] (score 110, diepte 1) I think a requirement should be to have "Car Wash" playing on the hospital overheads
[j8dxd2r] (score 84, diepte 0) I wore heelys in high school. Ngl it was dope for skating down long hallways, but a total pain in the ass every time I had to take a normal step (say between two desks). 

I work in the OR so I’m just imagining you doing a cartoon slip off a wheel after rolling into the capo line and taking down a mayo stand holding a bunch of specimens in formalin.
[j8eomg1] (score 77, diepte 1) We had one of those mobility devices for someone with a broken leg where you put your leg on the pad and push with the other foot. Kind of like a scooter but the foot rest was at bended knee height so you could put your knee on the pad and have your leg out behind you. 

Patient must have left it behind because it was a nice one, and that thing fucking RIPPED 

We also had a CF patient with a hoverboard thing and he would hold on to his IV pole and whiz around handing out candy. Hard for security to be mad when he was supplying them with snickers bars. 

We also had a patient who went to dialysis in her bed MWF and we had a standing competition to see who could get her there the fastest. You haven’t lived until you’ve seen a 70 year old woman trying to lean into the corners and telling you to step on it. 

This is the stuff that makes hospital work doable for patients and staff. Also as charge nurse it would be my duty to give any doc on heelies a push when needed.
[j8e64g5] (score 72, diepte 1) That sounds like something that could be on a quirky show like scrubs and I love it.
[j8e56a7] (score 72, diepte 2) The only footwear more EM than this would be motorcycle boots or climbing shoes
[j8dwy85] (score 70, diepte 0) Get a yoyo for rounds, too.
[j8emesm] (score 70, diepte 1) There is also a code for “misery and unhappy” as well as “distress of the human spirit” but I don’t see admin worrying too much about these.
[j8ei8th] (score 65, diepte 0) Hometown built a new hospital. Stuck the anesthesia offices at the farthest point in the hospital from the OR. Director of anesthesia put in a formal budget request to get all of the anesthesiologists Segways. After literally months going back and forth over it the admin finally acknowledged it was a dumb place to put anesthesia and moved them across from PACU.
[j8elrk9] (score 62, diepte 2) this must have happened in the before times when people in hospitals didn't mask so much
[j8e9wk7] (score 57, diepte 2) All credits to that Intern, but it definitely could. We have a particularly large and vacuous hospital that has long hallways without patient rooms. so we could safely fly at max speed without any concerns for patient safety. 

I often felt like I was JD with the wind blowing through my hair
[j8dyzj2] (score 56, diepte 1) I am sad that this was not part of my residency experience.
[j8e2hvg] (score 52, diepte 0) I bought Heelys to do just that! The problem was using Heelys was much harder than I expected too.. I was no longer a kid and was really hard to keep my balance

I've used a hoverboard on occasion, but in med school was told that it is a hazard because it can cross contaminate rooms. 

But i say if you are confident in your Heely skills go for it! become the ultimate resident I only dreamed of becoming
[j8etg6q] (score 49, diepte 1) Oh boy do I have something to show you...
[Moonwalkers - the world's fastest shoes](https://www.kickstarter.com/projects/shiftmoonwalkers/moonwalkers-the-worlds-fastest-shoes)
[j8e7krx] (score 46, diepte 3) Along with patagonia hiking pants, birkenstock sandals and cliff bars for lunch
[j8ec8u2] (score 38, diepte 0) You should start a movement Heely's for Healing
[j8eivl0] (score 32, diepte 0) There’s an ICD 10 code specifically for Heely-related injuries, so I might guess an employer would frown upon it.
[j8eu0n8] (score 31, diepte 4) I don’t think it’s security’s call if a resident is trespassing… especially one that has a doctor’s employee badge.

On the other hand you don’t want to be the doc who has a code fall called over the PA because your heelys got stuck on a needle cap.

Seems like the better part of valor to just duck the scenario entirely.
[j8fdlzk] (score 31, diepte 1) At least that was the best place you could’ve possible been when you fell 😅

All jokes aside, that really sucks. I hope you’re doing better now.
[j8fn0xa] (score 31, diepte 1) The "start high" negotiating strategy executed to perfection.

Make a completely unreasonable request so your follow up reasonable request seems like a no brainer.
[j8elmd6] (score 29, diepte 3) Jokes on you, JD never rode his scooter without his hairmet on
[j8emy4h] (score 24, diepte 2) Serious question: what are they gonna do?
[j8etsyd] (score 24, diepte 1) One of our 75+ year old internal medicine attendings rode around the hospital on a razor scooter. She was legit. You have to have clout before you donit
[j8esiv1] (score 24, diepte 0) “Would you want us to give compressions in the event your heart stops working?” *proceeds to roll out the room*
[j8fet2h] (score 22, diepte 2) Oh for sure. The people I was just in shift with came out and picked me up haha. I will say, as much shit as all of us ER people give each other, not a single person ever said told you so. 

I'm doing fine now. It took a while, but I'm at like 95% now! Can't complain.
[j8dtwpq] (score 21, diepte 1) [https://tenor.com/OLLp.gif](https://tenor.com/OLLp.gif)
[j8e2zgs] (score 20, diepte 1) chaotic good. i love it
[j8egvuk] (score 20, diepte 0) Off topic, put the hospital I rotated through banned the word Cow because it was derogatory/insensitive, and made us refer to them as a Wow (workstation on wheels).
[j8ewfy1] (score 17, diepte 0) I had heelys when I worked in a grocery store in high school. Supervisor thought it was hilarious. Assistant manager loved our response time. Store director had an aneurysm and banned them. I still have those shoes tucked away somewhere.

I say go for it, but someone will ruin your fun.
[j8e82sx] (score 15, diepte 4) 100%, gotta have nylon swishy cargo pants
[j8g1unf] (score 15, diepte 1) As far as I am concerned, those toe shoes should be banned for being hazardous to the eyeballs. We have a CCM attending who wears them and my flght-or-flight response is automatically activated every time I run into him.
[j8fgel9] (score 14, diepte 1) This is some JD and Turk shit haha
[j8f1jp9] (score 14, diepte 0) One of my senior residents broke his ankle and was in a boot for 6 weeks. He had a kneeling scooter. We kept using it after he healed lol and it’s still in the IM resident lounge
[j8ewmgj] (score 12, diepte 3) Eeeeeeeaaaaaggggllleeee!!!!
[j8g1g0h] (score 12, diepte 2) I once nearly got a nurse to pee himself laughing when I spent the whole ride to the procedure room making Star Trek noises for all the doors. It was great fun.
[j8fwju3] (score 11, diepte 1) Same here, so I taped pictures of Owen Wilson to all of them
[j8fm3bt] (score 10, diepte 4) They're going to trespass a doctor trying to take care of her patients as quickly as possible?
[j8gd7fy] (score 10, diepte 4) Her name is Sasha.
[j8fzber] (score 10, diepte 2) The best part about that intern is that he is really a no -nonsense kinda guy. For him it was truly a logistically sound choice. It wasn’t for fun and games
[j8dz7ux] (score 10, diepte 0) This is the way:  
https://heelys.com/collections/light-up
[j8g102u] (score 9, diepte 2) Maybe a Bop It to pass around during rounds as well
[j8gzzno] (score 9, diepte 1) How does a hover board cross contaminate rooms more than my shoes?
[j8g4vsl] (score 8, diepte 3) Reminds me of a broken arm
[j8e5fcy] (score 8, diepte 2) What program? Asking for a friend XD
[j8hld9j] (score 8, diepte 1) Don't piss off the custodians, man.

(Sounds like fun though!)
[j8e3h64] (score 7, diepte 1) Yeah but we have to deal with crusty bats
[j8g353n] (score 7, diepte 2) Those look bad ass
[j8ge4bk] (score 7, diepte 3) Hey man, with your attending money you could have a pair at your doorstep in March of this year.. they'll run you a pretty penny though (between $800 to 1300 depending on how many pairs have sold already)
[j8e6qq7] (score 7, diepte 1) A bouncy ball or ball like a raquet ball are kinda nice too to fidget with while walking down the hallway.
[j8e8zji] (score 7, diepte 0) I did this as a second and third year resident in the hospital, I finished residency in 2020. Was fun.  Size 13 heelys were comical for sure.  They wouldn't let me wear them in the outpatient clinic though :\\
[j8ejhv8] (score 7, diepte 0) In the Dark Tower book 7, there’s a doctor who zips around on roller skates. I think you should turn fiction into reality lol
[j8i14cb] (score 6, diepte 2) Hey, some places still make you put on shoe covers for COVID rooms. Don't question the lack of evidence behind infection prevention policies
[j8e3gck] (score 6, diepte 0) I think one of my ICU coresidents slipped and hurt himself with those
[j8elpz2] (score 6, diepte 0) We did this ONCE. They build a new ED that was this super narrow, and unreasonably long, so you had to run back and forth all day long.  I thought it would be funny to get some Heelys… and it was for a few laps. They are uncomfortable. The wheel always sticks out of the bottom unless you remove it completely. It was basically a novelty, and I switched back to my normal shoes.
[j8ght9c] (score 5, diepte 1) This is the biggest urban legend in healthcare. Nurses hate it too!
[j8f1v0s] (score 5, diepte 0) I wore heelys on my last day on CL. Was awesome. Don't forget the yoyo.
[j8ewv4a] (score 4, diepte 3) Eh, EM docs would ride motorcycles, but I doubt they'd wear the boots.
[j8e9vt4] (score 4, diepte 0) Using heelys was not as easy as I expected it to be
[j8fdt1w] (score 4, diepte 1) Lmfao same at my hospital, because a nurse complained thinking we were calling one of our pts a cow. Was this perhaps at a tri-state academic institution 👀
[j8g342s] (score 4, diepte 2) As an over-worked CV RN, you briefly relieved my "distress of the human spirit" with this comment, so thank you. My GF was looking at me strangely and wondering why I was laughing so hard!
[j8f79q5] (score 4, diepte 1) Yeah they definitely weren't happy when I brought my orca to work
[j8esto2] (score 4, diepte 0) OSHA
[j8gwsvw] (score 3, diepte 1) I have seen that.
Love, from the ED
[j8gsj8a] (score 3, diepte 2) please tell me you came back the next day with one of those scooters people with broken legs use
[j8j5nz6] (score 3, diepte 3) that makes it even funnier
[j8e9y0w] (score 3, diepte 5) This
[j8e2pwf] (score 3, diepte 0) I imagine you causing some injury and being sued and fired... Id be careful.
[j8ehjpy] (score 3, diepte 0) #Legend.
[j8emnqb] (score 3, diepte 0) arizona robbins is that you?
[j8euudm] (score 3, diepte 0) Someone’s gonna throw the pRoFeSsIoNaLiSm bludgeon at you.
[j8fiptq] (score 3, diepte 0) If Dr. House didn't have a bum leg, he would definitely wear these.
[j8fw275] (score 3, diepte 0) Am peds pgy3 and have light up heelies. Only wear them on nights/when the hospital isn’t busy so I don’t run into people. They’re a blast and get tons of compliments
[j8gcx21] (score 3, diepte 0) I, too, am sad that Scrubs finally ended.
(45 reacties met lagere score weggelaten)

=== THREAD 1b28wao ===
SUBREDDIT: r/BuyItForLife
DATUM: 2024-02-28  SCORE: 65  REACTIES: 119
TITEL: I bought LL Bean slippers thinking they'd last - any better ideas?
POST (source_id=post):
I purchased a pair of LL Bean Wicked Good slippers in August, 2023 and by February 2024 I've nearly worn down all of the faux fur lining. Is this what I should expect or is there something better out there? 

I'm looking for women's house slippers that are warm and have hard soles. Bonus points for arch support. 

TIA!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kskge1k] (score 109, diepte 0) Very experienced knitter here.


If the shearling interior lining of your slippers is real wool, you can refresh the squish and warmth by buying "top roving" from any yarn shop and stuffing a bit of it into your slippers. The heat, oils, and friction of your skin  will "felt" the new wool to the old wool and give the slippers a new life.


Repeat as necessary for new fluffiness.
[ksk1v6z] (score 102, diepte 0) I'm not sure what people expect of these slippers. Shearling gets matted down over time. It's not something you can somehow engineer out. It's a natural product. Wearing to the soles is one thing, but this is what all shearling does.
[ksju6as] (score 33, diepte 0) Ugg Ascots have served my family well and you can replace the insoles when they wear out
[ksl7n40] (score 25, diepte 2) The LL beans have replacement shearling inserts. So basically the same thing?
[ksjvtil] (score 24, diepte 0) I have LL Bean slippers with the same issue.  They do sell [shearling insoles](https://www.llbean.com/llb/shop/72756?page=adults-shearling-insoles) that definitely brought some new life to my pair but doesn't help the wear on the heal, unfortunately.
[ksju09i] (score 23, diepte 0) Glerups are our favorites.
https://www.glerups.com/
[ksmc1a1] (score 18, diepte 1) https://www.thefeltpod.com/wool_roving_s/1977.htm


Link for your consideration
[ksjrejf] (score 16, diepte 0) I have a pair of minnetonka slippers with shearling lining I've been wearing daily since Dec 2021, sometimes all day when I work from home.  There's just now one small area near the ball of my foot where I've worn down the shearling to bare leather, otherwise they're in good shape.
[ksms9v5] (score 16, diepte 2) Just his talented butthole.
[ksjqm16] (score 13, diepte 0) Birkenstocks and good socks.
[ksm54j0] (score 10, diepte 1) Thank you for this wisdom!
[kskkge8] (score 9, diepte 1) Because you can buy slippers with replaceable insoles, unlike llbean. I have been wearing the same pairs of ugg ascots for a long time, just spend 20 bucks getting new insoles every year or two.
[ksjxkrw] (score 8, diepte 0) My Uggs are five years old and going strong.
[ksk4q0p] (score 8, diepte 0) The correct answer is Haflinger - the ones with the cork sole. Ugly as sin but they are great for your feet and last! Plus they’re felt/wool so they do a great job resisting stink.
[ksmydsf] (score 8, diepte 2) Basically. You tear off a chunk and fluff it up (the air between the fibers helps keep it warmer), and stuff it into your slippers. Shove your feet inside and wiggle your toes and feet around to get it comfy.


Stick small pieces of fluffed roving anywhere you feel like it needs extra.
[kskdig2] (score 6, diepte 2) Me too.  Minnetonka moccasins holding up better than a comparable pair of LL Beans.  Surprises me, LL Bean quality is usually pretty good.
[kskg4kl] (score 6, diepte 0) Unpopular opinion and here come the downvotes; Fuck LL Bean.

They've slid downhill since 2016 when they changed their warranty and now just profit hungry serving shareholders over consumers.

There's an ass ton of LL fanboys and shills on this sub.   
r/fuckLLBean
[kskvnkr] (score 6, diepte 1) Probably because there are morons like OP who their their slippers are faux fur and that there’s some magic material that doesn’t mat down eventually.
[ksl6f92] (score 5, diepte 2) They only shed for a couple weeks, after you break 'em in they should hold pretty well.
[ksjya0e] (score 5, diepte 0) I bought probably the same slippers for my wife (about $85) and they fell apart. Most $20 Walmart or Target slippers do better than that and some are more cushiony.
[kspdccd] (score 5, diepte 1) Listen, if those slippers won't stand up to my wearing them to hike the entire Appalachian Trail (while scuffing my toes and without ever washing my feet), they're trash and clearly not BIFL.
[ksk1yyc] (score 5, diepte 0) Glerups.  Durable, breathable and generally feel very high quality.  Plus I think they make my feet look kinda cool.  :)

https://amzn.to/4bV3Tzj
[ksk36jd] (score 5, diepte 0) Shearling does that in slippers and there's nothing you can really do to stop it. Get some leather insoles instead—they'll last much longer. My dad had a pair of the full-leather ones for 20 years.
[kskvxfz] (score 5, diepte 2) Besides leather boots, no footwear is, and even they have limits. People are crazy.
[ksmg89s] (score 5, diepte 1) wait!

  


are you Bob Mortimer the famous knitter?
[ksl7ydy] (score 5, diepte 0) My wicked good slippers became undone in less than 6 months, and they wanted to charge me to repair it. Not so wicked good.
[ksjsf3t] (score 4, diepte 2) I've never had the fuzzy Birks so I can't speak to that. I have regular leather Birks and while at times they don't protect against house-cold as much as slippers do, they are great on my arches with good hard soles. An excuse to pull out some of my big fuzzy socks that I rarely wear anymore.
[ksk6pki] (score 4, diepte 1) I was going to recommend Minnetonka also. I bought them for my husband in 2020 and they’re still going strong. Definitely worth the money so far.
[ksjyxrz] (score 4, diepte 3 OP) Thank you so much for sharing. My feet are extremely cold all of the time (right now I have on wool snowboarding socks and faux fur lined slippers and my toes are still very cold.) Based on what you said here I'm certainly intrigued by these shoes. Have you found they hold up over time?
[ksmrju6] (score 3, diepte 1) Similar to this, I wear big thick Smartwool socks with a pair of 20-year-old Crocs just for kicking around and it’s perfect.
[ksljd2l] (score 3, diepte 1) I love my Glerups, they’ve turned me into a slipper person. Mine still look good after a year of so, but I don’t expect that they’ll last forever.
[ksne306] (score 3, diepte 2) I don’t find they run hot at all! My husband recently bought a pair of UGG slippers finds them hot and starting to get stinky.  Both issues I haven’t had with daily wear of my Gerlups.
[ksndidr] (score 3, diepte 1) I've been a WFH guy for quite a while now, and gone through plenty of slippers. LLBean, Uggs, Tom's, Mahabis...all dead. I have two pairs of Glerups, and they're by far the best. I'm partial to the backless with the rubber sole.
[ksope2i] (score 3, diepte 2) It's cheaper than a new slipper
[ksk8kri] (score 3, diepte 0) Glerups with the rubber sole.
[kskfqy2] (score 3, diepte 0) Give them a call, they will replace them, since it’s been less than a year. In the future yes they will eventually mat down given what they are made of.
[ksmvfmy] (score 3, diepte 1) wait so what do you do with the roving. Just lay it in there? I have some Ugg slippers that are getting a little matted. I’ve been using a comb to fluff and redistribute the shearling where it gets bunchy but it only lasts so long.
[kskmymv] (score 3, diepte 0) OluKai.  I have a pair and I highly recommend them.
[kskvay7] (score 3, diepte 0) That’s not faux fur. That’s sheep shearling, literally wool still attached to the skin. You’re treating them poorly if you’re burning through them in a year.
[kslxkn9] (score 2, diepte 2) Especially for the 'roll out of bed and slip into slippers' action. I'd never actually done it until I got these Birks. 

So satisfying.
[kslwfnz] (score 2, diepte 1) That’s what I’ve been rocking for a few years. The outsoles are starting to fall apart though so I’m on a hunt for replacement. One issue I have is that the faux fur lining is not breathable and is not as anti microbial as shearling.
[ksmo8xn] (score 2, diepte 1) I don't wear mine anymore than it sounds like you do, but this recent pair I've gotten hasn't held up. I'm 2 months in to having them and the stitching on the upper leather is unraveling at the end. Longevity wise, I have to buy a new pair every year. Super comfy though.
[ksjrn8s] (score 2, diepte 0) The North Face Thermoball traction booties.
[kskj43z] (score 2, diepte 1) I don't love these, pretty narrow but mainly theres so much damn wool around my house it's annoying.
[ksm3u65] (score 2, diepte 2) I wear mine literally every day and they last me about four years
[ksm59ro] (score 2, diepte 2) They don’t for either of us. I own both the slide-in and the boot, my wife the boot.
No complaints and a big fan.
[kskklzs] (score 2, diepte 1) Get the ugg ascott, that insole is overpriced.
[ksk2q2u] (score 2, diepte 1) I have had some I got at Costco for several years. I don't think they're BIFL, but all in all, they are good for the price.
[ksk3zcl] (score 2, diepte 2) Yeah, relative to the value for money of the L.L. Bean slippers. They used to have a lifetime replacement warranty but no longer, at least on slippers.
[ksk27s8] (score 2, diepte 0) Uggs
[kslaq4g] (score 2, diepte 1) Agreed, I've had these and glerups and much prefer the quality of the haflingers.
[ksoygdd] (score 2, diepte 1) Came here to suggest Halflinger - I don’t know what I’d do without mine.
[kskagyj] (score 2, diepte 0) North face thermoball. Longest lasting slipper I've owned.
[ksnf79a] (score 2, diepte 3) Thanks! I’ll have to try this.
[m04nsq6] (score 2, diepte 3) this sounds so cozy, like a little rat burrowing lolol 🐀🪹
[kskmz9q] (score 2, diepte 0) OluKai.  I have a pair and I highly recommend them.
[kskx9by] (score 2, diepte 0) I wear Birkenstock Boston. It’s not really a slipper but if only worn indoors it will last a very long time. I’ve considered Glerups and Giesswein. I got my son a pair of Olukai for Christmas and I was impressed with them.
[kslbbcs] (score 2, diepte 0) My LL Bean slippers ripped after 10 months and they said that it was from normal wear.
[ksmuwqx] (score 2, diepte 0) I work from home and have been wearing Olukai slippers daily 10-12 hours for 3 years and they are fantastic.

I always wear socks with them and they don’t smell at all, and feel great.
[ksmwp32] (score 2, diepte 0) I got a pair Birkenstock house slippers after 10 pairs of Ugg shearling just to try something different.  Much more rigid sole, more arch support and stiffer in general but very comfortable and warm.
[ksjrghx] (score 1, diepte 1 OP) Good idea. I had felt topped Birks for house shoes once though and word holes in the upper pretty quickly. Do you recommend leather Birks?
[ksjw8y9] (score 1, diepte 2) Yes! I agree with furry birkenstocks. I got regular Arizona with shearling lining on mega clearance (because it was mid-summer) and wear them all winter long. 

My other pair is mahabis that lasted me years.
[kskxo7f] (score 1, diepte 2) I got the Zermatt shearling slippers a couple of winters ago and the shearling wore off most of the insole within the first few months. I still wear them though, they’re very comfortable otherwise despite the now-leather insole.
[kslpo0s] (score 1, diepte 1) The classic birks and thick wool socks is the best slipper combo.
[ksm23lr] (score 1, diepte 3) It’s been going good for several generations in my family 😌 glad to see others enjoying it
[ksl2nw3] (score 1, diepte 1) Same, I love mine about 3 years in.
[kslxpym] (score 1, diepte 2) Mine have a true shearling lining.
[ksjwvqa] (score 1, diepte 1) How would these perform in 75° home? How warm are they?
[ksjxmrg] (score 1, diepte 2) I keep my house at 65 degrees F and my feet are prone to Raynauds (vascular issue that affects blood supply when it gets cold). These slippers are the only thing that keep my feet perfectly toasty all winter. At 75 indoors, you will be very comfy and maybe even find them a bit too warm. If you don't walk around outside on sharp things, they last forever imo. I wear them to the mailbox and back too!
[ksm4to4] (score 1, diepte 1) I've been looking at these, do they run hot? I have a pair of Ugg slippers that are great but if I wear them for a long time indoors my feet start to overheat. I was hoping the lack of sheerling lining might help that.
[kspbixk] (score 1, diepte 1) I have had to refelt mine eight times, there are holes all over the *top* and the rubber is all ripped up. 2 years, indoor use only. Nothing fancy.


I spent way too much money on those slippers to have them look this bad in two years.
[kst7wv4] (score 1, diepte 1) I’ve been eyeing this for my husband, but he only prefers barefoot style shoes (wide toe bed, zero drop heel). From the photos, it looks like this would work, but as someone who wears them, would you say that’s an accurate guess?
[ksv9ucg] (score 1, diepte 2) I would agree with those two criteria.
[ktc0w4j] (score 1, diepte 3) Thanks!
[kskktp6] (score 1, diepte 1) This kind of advice does not belong in a bifl subreddit. Slippers with replaceable insoles like ugg ascott are easy to get and bifl.
[kspifma] (score 1, diepte 2) That’s not really lasting longer…just replaceable on the bottom.
[m21ry4x] (score 1, diepte 2) I bought UGG Ascots because so many people recommended them. They only come in men's sizes, but because I have small feet, I got away with buying a kids' size. But I'm not that impressed with the sole, so I'm returning them.
[ksld96r] (score 1, diepte 1) My last pair of LL bean slippers last over 8 years (2011 to 2019) of daily wear. I only threw them out because they started to get too big from stretching. No stitching broke wore through. I did repurchase because all the reviews say they aren’t are good anymore!
[ksk2m0p] (score 1, diepte 0) Carl Dyer’s
[ksk4f4r] (score 1, diepte 0) Minnetonka 100%. I’ve worn mine in rain and snow without them soaking through or when really looking wet, had my cat take a shit in one of them so I threw them in the washing machine and then the dryer with no issues. I’ve had them for four years now and have not been kind to them and they’re still comfy as fuck.
(62 reacties met lagere score weggelaten)

