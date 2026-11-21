# Label-batch batch_0110

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
Schrijf het resultaat naar `batch_0110.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 16yemiy, 1pf50mc, i5qru9).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 16yemiy ===
SUBREDDIT: r/Nurses
DATUM: 2023-10-03  SCORE: 67  REACTIES: 71
TITEL: Are there nursing jobs that don’t require being on your feet the entire shift?
POST (source_id=post):
So I know nursing is probably not the right profession for someone who has a degenerative foot condition but I’m wondering, if I’m able to get through school are there jobs that don’t require being on my feet constantly? I currently work as a medical assistant in an integrated health clinic and it works out because after I take a patients vitals/notes I’m able to dictate while sitting down, giving my feet a break. 

I don’t make much right now and I’m wondering if I’m able to get through school would I be able to find a job that isn’t 12 hours of being on my feet?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k38900k] (score 84, diepte 0) I worked in psych and about 80% of my day was spent sitting down and charting. It wasn’t as physically demanding compared to med surg
[k388rx5] (score 38, diepte 0) Utilization management or Case management take place mostly in an office, or remote if you're lucky.
[k38a7jz] (score 29, diepte 0) I work in an occupational health office, and it's the most sedentary I've been at a job.

NICU can have plenty of sitting time as well, if you're not working exclusively in isolettes/warmers; you're usually standing for assessments, admissions, and tasks like IV starts, but you sit down to feed the babies.

School nursing is another more sedentary job from what I understand.
[k38o4i8] (score 23, diepte 1) wound care??? Im a WC nurse. We are walking through the entire Hospital from units to units most of the time. Working at bedside and then coming back for documentation. but the distance we walk is crazy
[k38vxxq] (score 18, diepte 0) I just got a remote job as a case manager and I work from home 100%
[k389rp7] (score 16, diepte 1 OP) This gives me hope. I’ve always thought that if I did nursing I would enjoy psych. I have a bachelors in psych. Do you mind me asking if this was a inpatient/outpatient clinic?
[k38wpe6] (score 13, diepte 2) I work inpatient,  night shifts. Currently geropsych and trying not to fall asleep between my rounds. Some nights are better, some are worse.
[k38c1v4] (score 10, diepte 1) Agree. I stand up for med pass. That’s about it.
[k38fz7z] (score 10, diepte 0) I was also going to say CM or UM. But also, most of public health, depending on what you're doing.
[k38kbfs] (score 9, diepte 1) Just don’t scrub
[k38fa8o] (score 9, diepte 2) This was inpatient. I would imagine you would sit even more in an outpatient setting.
[k3cd16w] (score 8, diepte 2) Sure, 13 years experience, msn, psych/med surg/ peds

People get hired for remote with a less credentials and experience than me!
[k39glsa] (score 8, diepte 0) Acute dialysis (dialysis of hospitalized patients). Most of your shift you're sitting down monitoring your patient. And you only have 1 or 2 patients at a time.
[k388kmm] (score 7, diepte 0) Try the OR
[k39uf3f] (score 7, diepte 2) Yep. Inpatient psych and everyone needs a joint replaced or can’t physically transfer people like they used to. The question for the newbie is always which body part is the most busted up.
[k38w0n4] (score 7, diepte 1) I was always running around as a school nurse but I guess some days can be slower
[k39noug] (score 7, diepte 0) Outpatient nursing is where it's at without being on your feet nonstop.
[k38k54e] (score 6, diepte 0) Inpatient: psych, diabetes educator, wound care, infusion therapy. 
Outpatient: clinic nurse, dialysis, school nurse, telehealth
[k38hnom] (score 5, diepte 0) Case management, remote or office based. Public Health and hospice.
[k39c4aq] (score 5, diepte 0) I have found by experience  that nursing doesn't like women over 55.  I had to leave psych. I couldn't find a less physically demanding job even though I have a BSN and lots of outpatient and teaching experience. I'm currently not working and getting social security disability.    Everyone is looking for a better job. I interviewed so many times over 5 years and never got hired except for pediatric home care ventilator and or tracheostomy care patients. Which is not steady. 

Nursing uses you up And spits you out.  Don't do it.
[k3d2uvm] (score 4, diepte 1) However outpatient dialysis is on your feet, gogogo for 10+ hours lolo
[k39igv1] (score 4, diepte 0) I worked doing clinical trials. Most of that was sitting.
[k38axv0] (score 3, diepte 0) NICU, depending on which level you work in, can have a lot of downtime. In a busy level 4 not so much but a smaller level 2 or 3 you can sit between sets of cares or when feeding a baby. If I have a fussy baby I’ll hold them while charting in their room. As charge or the Resuscitation nurse I can be on my feet a lot going to deliveries, admitting babies and helping people but when I’m bedside I usually have a good amount of sitting time. Every shift is different but I would say overall certainly less demanding on the body compared to adults or even Peds (I have worked PICU and CVICU too)
[k38dpvp] (score 3, diepte 0) Home hospice. Literally all i do is sit. In the car, at patient homes, then my house to document.
[k38u1lq] (score 3, diepte 2) I do wound care at my hospital. Yeah, I walk a lot, but between seeing patients I have a 15-30 minute sit while I am charting. Which I do on the floor, I may not go back to the WC office between leaving to see the first patient and returning to clock out.
[k3awb8a] (score 3, diepte 4) 6-8, depending on the day.
[k3ax63o] (score 3, diepte 5) oh wow. here in Brooklyn we see about 15-20 patients a day. But we never work alone its always 2 of us in the patient's room
[k39svsw] (score 3, diepte 1) Dialysis nurses don’t sit around much. Especially outpatient. If it’s acute then yes.. but I would be running on the floor all day passing meds and doing assessments for my 20 patients.
[k3ametq] (score 3, diepte 1) This may be true for prison corrections where deputies pass meds, though my experience in jail corrections was that I was on my feet not less than 80% of a 12h noc shift - passing meds to half of the entire jail and pushing a med cart, once back at nurses station doing wound care and lab draws, then insulin early in the morning before breakfast.
[k38m0xr] (score 3, diepte 0) I am a clinical manager for a home health company. It’s a desk job.
[k39i49b] (score 3, diepte 1) Absolutely not. There may be some times you can sit, but the other 80% of the time you’re running around like a crazy person, moving mostly large patients, positing them, moving and lifting heavy trays, etc. And if you don’t do things fast enough you can be chastised for it. The OR can be brutal. Definitely not the place to go for a more chill environment.
[k38rycs] (score 3, diepte 0) I work nights in LTC and there's a bit of down time.
[k3947mq] (score 3, diepte 0) Quality, risk, case managers, UR review RN…. To name a few desk type nursing…
[k39l2n3] (score 3, diepte 0) Hemodialysis / aphaeresis.  Been doing it for 28 years, so there’s that.
[k3aild0] (score 3, diepte 0) Operating room
[k3ameii] (score 3, diepte 0) I work in outpatient pediatrics. I coordinate patient appointments with other clinics for continuity of care, triage patient calls, and also give vaccines/draw blood/prick fingers. I also jump in and help the medical assistants with vitals and stuff if they’re behind. I get lots of time to sit during the day!
[k3aohk0] (score 3, diepte 0) Utilization Management is a desk job. Many of these positions allow you to work remotely (work from home).
[k3baf3z] (score 3, diepte 0) I would be *very* careful with outpatient clinic nurse positions. My clinic was high paced and while we did have slow times in the clinic day- I was also on my feet a lot! You’d definitely want to follow a nurse before assuming you’ll be at a desk all day. 

Home health, home hospice, home infusion. Remote jobs through insurance agencies, remote triage, etc.
[k3j6zuk] (score 2, diepte 2) It depends what psych setting you are working in. I used to work at an acute inpatient psychiatric unit within a large medical center. I ended up leaving after being slammed to the ground by a patient. I now have permanent nerve damage in my dominant arm from shoulder to hand. Maybe smaller town isn’t as bad but I worked in a large metro area so it was busy and not a lot of sitting.
[k39mqx4] (score 2, diepte 3) hi there, how many patients do you document daily?
[k38lija] (score 2, diepte 0) Corrections.
[k3aoqz6] (score 2, diepte 2) I worked in a prison in different areas. My med pass wasn’t cell to cell, they’d like up and come to my window. Sometimes I worked in the infirmary (in-patient), and sometimes I’d work the clinics where they’d come for wound care and insulins before each meals. I’ve never sat so much at any nursing job, there was just a lot more opportunity to do so. Even when I did have to go cell to cell for max security med pass there was still a lot of opportunity to sit afterwards. I have never worked in a jail though.
[k3atoc6] (score 2, diepte 2) That's what I thought. The circulator's job is non-stop being on your feet.
[k3bnac7] (score 2, diepte 1) Can I ask your experience? Curious for future.
[k39gw5x] (score 2, diepte 0) I worked for a large primary care organization that had a call center full of nurses to call and follow up with patients after hospital discharges.  Most of them work from home.
[k3av318] (score 2, diepte 1) NICU? You're caring for critically ill / premature infants - I was on my feet A LOT!! There wasn't a lot of down time for me, but I worked in a large teaching hospital, so that may be the difference with my experience. My legs ached after a 12hr shift from being on my feet for a majority of the shift.
[k39x6c4] (score 2, diepte 0) Pacu
[k3amafp] (score 2, diepte 0) There’s training positions and research positions which are a lot of data processing. Much less standing
[k3avji3] (score 2, diepte 0) Pre-admission testing at an ambulatory surgical center. I feel like I’m sitting at a desk on the phone almost all day
[k3c309j] (score 2, diepte 1) Home hospice has quite a lot of sit time. Sitting to do paperwork in the home, sitting to educate the patient and or family in what hospice is or just sitting while providing emotional Al support. But you also will do care at times, wound management, lifting pts off the floor or transferring them to or from bed. While there is a lot of sitting when educating or providing emotional support (standing and looking down on the patient or family is rather rude), there are parts of the job that can be rather physical for the nurse. 

But there is always “wind shield time”. When you are driving to the next Pt, to the office etc. and for me hospice was the most emotionally and mentally satisfying area of nursing there is.
[k3bzn0u] (score 2, diepte 0) Nursing Informatics if you're technically inclined. I'm a total computer nerd so finding out there was a specialty focusing on that was incredible.
[k3jbynb] (score 2, diepte 0) Yes! I had hip pain from sitting/driving TOO MUCH doing hospice case management
[k3lrj37] (score 2, diepte 0) Every time I've ever been on a step down unit they are all sitting down.
[k386mhr] (score 1, diepte 0) Yes, our facility currently has about 60 openings, all of which lend themselves to sitting down between, or during, tasks.
[k3jlhmk] (score 1, diepte 1) I work NOC shift pysch. Most of my night I'm sitting and auditing or charting.... my med pass takes about 10 minutes maybe 20 and we do walk to med to them

Day shift med nurse they all come to the Window
[k3jkqaa] (score 1, diepte 1) Nicu does have a lot of sitting times, but with admissions/line placement/critical kids I have had times of being on my feet for 4+ hours straight
[k3asvn7] (score 1, diepte 1) When I worked in NICU we had our 'feeder and growers' section of the unit. These infants need to improve their feeding (or learn how to feed) and gain weight prior to discharge. A good bit of the job is sitting in a rocking chair bottle feeding the infant. These infants have transitioned to open cribs so your assignment is normally three infants in cribs within close proximity to each other, so very little walking. There's definitely more to the job than that knowledge wise, but not a physically demanding job at that point of the infant's NICU journey.
[k38cnhy] (score 1, diepte 0) Yes in research I spent most of my time sitting at a desk although there were running around days it was nothing like on med surg.
[k38ikp3] (score 1, diepte 0) Acute inpatient hemodialysis… though there is a risk of developing a hump from staring at your phone all day lol. HD patients tend to be a very sick overall in my area and there are soooo many HD patients ( and more incoming) so patients can code frequently so compressions til code team shows up. We do have transporters at our hospital, but we do have to push beds every once in awhile if transport is backed up.
[k39w2kg] (score 1, diepte 1) Which of these specialities pays the highest?
[k3c5r31] (score 1, diepte 1) School nurse here. School nursing isn’t as demanding as bed side care, however I am on my feet for at least 70% of the day. But some days are busier than others though.
[k3d26q1] (score 1, diepte 3) Do you circulate?
[k3d4bs1] (score 1, diepte 2) Absolutely. I will never work in a dialysis center again.
[k3ayogd] (score 1, diepte 2) It depends on what level nicu you are in and how critical your pt is. Compared to when I worked med surg or ER I sit a ton in between care times in NICU.
[k3ixkcn] (score 1, diepte 1) Cool
[k3cib4e] (score 1, diepte 0) I do phone/lab triage for a MedOnc center.
I had to get a standing desk bc I sit too much. Lol.
[k3izufx] (score 1, diepte 0) Hospice or home health you are not on your feet the whole shift
[k3jql75] (score 1, diepte 0) I work in QA. Also worked in clinical research. Both are pretty chill but you have to stay organized and be good with protocols.
[kk7s35y] (score 1, diepte 0) Work remote doing phone triage. Sitting all day long
[ksf9a8i] (score 1, diepte 0) Management?
[k38r03a] (score 0, diepte 0) The operating room as a circulator
[k39p1yi] (score 0, diepte 2) MY OPINION is that it’s chill compared to working in the ICU. I’m speaking from experience having worked in both - I’m not guessing.  The environment has contextual relevance that needs to be considered: A 12 hour craniotomy with a proficient staff at a teaching hospital with anesthesia techs, turn over crews, and people who pick cases = lots of sitting time.  An endo suit or eye surgery center where you do 3 procedures in an hour, have  limited resources, have to turn over your own rooms, and pick your own cases = no sitting time.
[k39thhh] (score 0, diepte 0) Nicu
[k3c3fe0] (score 0, diepte 0) Telephone nurse triage. I did it for a year. Worked from home. But it wasn’t for me because I realized how much I missed direct care and seeing people and peoples’ smiles.

=== THREAD 1pf50mc ===
SUBREDDIT: r/AmazonFC
DATUM: 2025-12-05  SCORE: 458  REACTIES: 71
TITEL: Bruh, Amazon got all our feet looking like this 🤣
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nshoumu] (score 84, diepte 0) ![gif](giphy|FY8c5SKwiNf1EtZKGs|downsized)

Oh. Yeah.
[nshfe5e] (score 44, diepte 0) Lucky mine just hurt and stink. Peak 2025 going as planned
[nsi3kn1] (score 43, diepte 0) More like this

![gif](giphy|ZSkX3V6wNhEMU)
[nshd5uw] (score 34, diepte 0) Nah not the footussy
[nshhh7p] (score 27, diepte 0) Women of Amazon could be making a nice side hustle from foot content alone. 

I have friends in the military who sell their stinky socks for like $50 a pair
[nsigvnn] (score 21, diepte 0) mine dont get stronger. they just get fucked up.  my feet are like meatloaf
[nsih06y] (score 16, diepte 1) found the foot fetish guy
[nsik2k5] (score 15, diepte 0) Bro’s feet got a six pack AND belly buttons! 😂
[nsm627a] (score 12, diepte 2) Labrador
[nskf4rc] (score 11, diepte 3) ……please change your socks
[nsj5fuw] (score 11, diepte 1) Ew
[nshlfic] (score 9, diepte 0) this but my ankle feels like it’s breaking into pieces 😭😭😭
[nsheoyw] (score 8, diepte 0) Nah😭
[nsj4lva] (score 7, diepte 1) Get clean socks!!! And rotate or dry your shoes
[nslu06q] (score 7, diepte 1) I love the dog gif...what type of dog is this cutie?
[nsil3vw] (score 6, diepte 2) standing doesn't bother me.  i'm walking like 12 miles or more a day.  even with good shoes and putting vaseline on my feet, my toes are white on the side and tore up.  they're burning right now.
[nsipmbe] (score 5, diepte 1) Um. I need in on this side hustle🤣🤣🤣
[nsiwb9j] (score 5, diepte 1) True but mostly at my arch and I limp out the building after , only liquor helped for 4 years but at year 5 the liquor started making me less productive and I started getting written up and they always try to push going to am care or taking ibuprofen or somthing else but by that time I was on the juice(alcohol vodka) and I know not to mix so I just would sleep walk every shift limping on pack wall or rebin and even induct until now I'm on flex and can work a full week and take off week if I wanted.
[nshy0vt] (score 5, diepte 0) That indirect role life ngl
[nsijolg] (score 5, diepte 1) I messed up the nerves on the bottom of my heels or something in my two and a half years at Amazon, and they always hurt when I'm walking now. Wish I could go back in time and convince myself that standing for ten hours a day wasn't going to work out well for me.
[nsl5wdl] (score 4, diepte 3) Oh my god…😭
[nsjffg9] (score 4, diepte 1) Get yourself a boot warmer for your shoes. It will keep them from stinking and also help extend the lifespan of your shoes too.
[nskivjd] (score 4, diepte 3) gross
[nslaho4] (score 4, diepte 1) 🤣🤣🤣
[nsoyhlf] (score 4, diepte 1) Gottt dang are those toes or jacked up fingers dem thangs look creepy af😂😂
[nsibhtc] (score 4, diepte 0) Your feet got abs lol
[nsjjfnu] (score 4, diepte 1) https://preview.redd.it/5wt350c8di5g1.jpeg?width=392&format=pjpg&auto=webp&s=baf07d891bbc4f8a4aa21c5f859c70e484e5aef1
[nshaw7v] (score 3, diepte 0) 😆 🤣
[nsjpl4z] (score 3, diepte 2) I usually wear the same socks everytime until I get a hole in them and I just replace that particular one.
[nsl1i5f] (score 3, diepte 4) I’ll try but I’m so used wearing the same pair week after week until a hole comes in. I do wash them every week though. 😅
[nsmdggg] (score 3, diepte 1) I didn't get to enjoy Peak 25, been in and out of the hospital with the stomach flu and severe dehydration...I will see DCA1 next year...
[nshj86h] (score 3, diepte 0) Hear me out
[nshy4tr] (score 3, diepte 0) my feet be hurting bro fr
[nsp361u] (score 3, diepte 2) Them some feet
[nsiezjt] (score 3, diepte 0) Be glad there aren't nips on them.
[nsmqe2z] (score 3, diepte 2) Same thing happened to me, so now I have permanent nerve damage in my feet.  Didn't matter what shoes, insoles, or special shoes from my podiatrist prescribed me.  Nothing helped.  My feet are so sensitive now even laying down hurts.
[nsnfjsp] (score 3, diepte 3) Laying down's fine for me, but it's always uncomfortable when I apply pressure to the bottom of my feet. Getting out of bed in the mornings suuuucks.
[nsioi48] (score 3, diepte 0) Some hotdog buns 😂😂
[nsjfwmb] (score 3, diepte 1) That’s so cool. Tell us more about that.
[nsk04f7] (score 3, diepte 0) Eww what is this 😭
[nskz8f2] (score 3, diepte 0) https://preview.redd.it/21rsp3i3rk5g1.jpeg?width=1080&format=pjpg&auto=webp&s=b70a43d74ecbc95de5e6f30ad21b5dacc5ed606f

Nawl fr cause I don’t feel the hurt anymore 🤷🏾‍♀️
[nslrsea] (score 3, diepte 0) I know it's just a meme or a joke, but for real though, most Amazon worker's feet probably look either swollen or heavily calluses.
[nsmar32] (score 3, diepte 0) what the fudge shoes are you wearing lol.
Orthofeet are so comfy and come with Amazing insoles. But they are heavy.
The Redbox flexweave has potential but I have wide feet and mens DD gives me blisters unfortunately. 
Orthofeet even comes with like extra insoles in case it's too big (I wear a 9 to 9.5 in womens and got an 8.5 in mens).
But they go to triple ds.
Man why do these sound like bra sizes.
[nsmwx6f] (score 3, diepte 0) No ma'am/ sir 🤣🤣
[nsmx8im] (score 3, diepte 0) Buy steel toe socks I work in composite Skechers can work up to 14 hrs in them  but thank God its only 11hrs this peak
[nsnof81] (score 3, diepte 0) …And that’s enough internet for today.
[nsqnzpi] (score 3, diepte 0) https://preview.redd.it/70mvorkjar5g1.jpeg?width=1024&format=pjpg&auto=webp&s=3031db01dc5418181bafbc338fbe4d25c7ae7167

More like this…… our feet are “toest”
[nsmqsln] (score 2, diepte 5) Not every day? Every week nasty

![gif](giphy|yIJrNGX9wF7eE)
[nsq7n3b] (score 2, diepte 5) This is how you grow foot fungus
[nsr9b61] (score 2, diepte 7) Dark and wet is what fungus loves. You do have to get infected by it though, and it's more or less common in certain areas. Here in Oregon it's pretty common
[nsmjdm6] (score 2, diepte 2) My socks are clean and I use a boot dryer. Nothing helps my feet just fucking wreak dog
[nsmja5z] (score 2, diepte 2) Yeah
[nsipu0d] (score 2, diepte 2) I promise you it’s not just me 😂
[nsj1co9] (score 2, diepte 2) i don’t know too much about foot arches but have you ever tried any arch support insoles while you worked there?
[nsiir8e] (score 2, diepte 0) Like abs lol
[nsimgpu] (score 2, diepte 0) Damn what does your stomach look like then?
[nsiukx5] (score 2, diepte 0) Maaan I do Amnesty and my feet are KILLING me as we speak 🤣💯
[nsiv32v] (score 2, diepte 0) My feet are nubs and I can't feel my big toe
[nsjbk6e] (score 2, diepte 0) I had athlete's foot about 2 months ago
[nsk8m1w] (score 2, diepte 2) I was picking and packing as usual, and then all of a sudden, my feet started to feel itchy. I thought it was bed bugs, but I was wrong. My dad told me it was that since I have not been moisturizing my feet, and on top of that, I'm moving my feet a whole lot. I had to pour a tub with hot water and soap for my feet. After that, I had to apply lotion.
[nsjqry5] (score 2, diepte 0) i have POTS so my feet are just super swollen at the end of shift lol
[nskrnkv] (score 2, diepte 0) This how it feels 100%, being a 40 hour+ a week spider for inbound i get to stow maybe 2times a month this is how my feet feel 😩
[nsladss] (score 2, diepte 0) 🤣🤣🤣
[nsmph17] (score 2, diepte 0) Funny my friends and I were checking our fitness last night and the were shocked that I reach the 10k almost every day, one day this week I did 31k steps
[nsnmdxk] (score 2, diepte 0) Lol that’s not an Amazon problem yo.  WTF is wrong with your feet?
[nsry6w4] (score 2, diepte 0) Because of Amazon, I naturally walk fast and I never noticed it until im walking with someone somewhere outside of work and they go “why are you walking so fast” or “why are you in a rush” lol
[nshaav1] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.com/invite/t7jARCs) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[nsus27c] (score 1, diepte 6) Shirts and pants can be worn twice everything else once atleast that's how I do it.
[nsr3zt8] (score 1, diepte 6) It’s been many years of me doing this. I’ll try to start switching socks sometimes.
[nsusl8h] (score 1, diepte 8) Got it once as a kid in eastern Washington. Though the main cause was me stepping in a puddle before school and not saying anything and wearing it all day.
[nspljz2] (score 1, diepte 3) Does the skin peel, esp between your toes? And itch? Probably athletes foot. A little anti fungal will solve the problem within a week
[nsrrg17] (score 1, diepte 4) Nah no peeling or itching just a lot of rank stank
[nsustk3] (score 1, diepte 3) I'm apparently very lucky. Don't sweat much don't have foot odor and apparently according to others only I can smell my BO (though that could be my autism lol)
[nsopiq0] (score 1, diepte 1) Not at my DS. I rate them all a 4 at best. My previous SSD was a solid 8 though
[nsp4plo] (score 1, diepte 3) ![gif](giphy|l0MYryZTmQgvHI5TG)
[nt77qpo] (score 1, diepte 1) https://preview.redd.it/k7pflt9rk96g1.jpeg?width=1290&format=pjpg&auto=webp&s=9ef57f0c8d25baf92af89a01232f1203d5833a13
[ntnwun7] (score 1, diepte 1) Ouch!
[nsogzdd] (score 1, diepte 0) Literally feel that. 😭
[nsp2i4c] (score 1, diepte 0) ![gif](giphy|dtGIRL0FDp6nnOPGb5)
[nsrevle] (score 1, diepte 0) Ouch
(7 reacties met lagere score weggelaten)

=== THREAD i5qru9 ===
SUBREDDIT: r/ProtectAndServe
DATUM: 2020-08-08  SCORE: 4291  REACTIES: 71
TITEL: In 1969, black citizens weren't allowed to swim in "white-only" swimming pools. Mr. Rogers invited a black officer on his show and asked if he wanted to cool off by dipping his feet into an inflatable pool. Mr. Rogers joined him, breaking the color barrier live on television.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[g0r3ho9] (score 698, diepte 0) To further the story, the black officer was a black man playing an officer, not an actual officer.  The actor was apprehensive about playing an officer due to conflicts of the time between police and black people.  Mr. Rogers convinced him that it was necessary for him to portray an officer so as to take a step forward in mending the stereotypes that segregated police forces had of black people and that the black community had of police.  So this episode was double-layered in its message of understanding, equality, and co-existence.
[g0qx7tn] (score 344, diepte 0) Fake news.

That's not an inflatable pool.
[g0qziyq] (score 287, diepte 0) This man was a super hero.
[g0r5qk0] (score 182, diepte 1) I was about to comment this.

The man wasn’t a police officer which kinda sucks, but it doesn’t change the message.
[g0qxq83] (score 171, diepte 1) It's in black and white so no color barrier broke either.
[g0qzj3s] (score 124, diepte 0) Wholesome Mr.Rogers.
[g0qznum] (score 108, diepte 0) Dear lord that man was a saint
[g0r3hx9] (score 103, diepte 2) Geeze, people. Next you'll tell me the trolley didn't actually go to a magical land behind the walls.
[g0raavu] (score 77, diepte 3) Oh no, that actually happened.
[g0r3v00] (score 77, diepte 0) The Civil Rights Act of 1964 made such discrimination illegal. However, there were a lot of communities and individuals who continued to discriminate. 

Mr Rogers and Officer Clemmons did this to teach children that there was no danger to share a pool with a person of color. There had been bullshit folk stories that black people contaminated pools in some way. These stories were believed by many. 

Children seeing this got the message and social change moved forward a bit.
[g0r69q1] (score 73, diepte 0) Our country is quite young; in the grand scheme of things. We've made great strides towards upholding the original intentions of our founding fathers, that "all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness". By no means is our country perfect, but I'll be damned if I ever say there is a better or more free place to live. It saddens me that a vocal minority wish to tear down what we've collectively as a country have been working to build.
[g0r5p7v] (score 59, diepte 1) Different kinds of smashing, though
[g0r8k7t] (score 56, diepte 1) I grew up in the 90's and loved watching Mr Rogers Neighborhood as a child.  When he passed during my Freshman year it was the first time I had actually cried over the death of a "celebrity".  That man had so positively shaped the heart and minds of so many young people and even helped explain some of the more delicate issues some children may experience, like divorce, nuclear war, people with disabilities (long before the ADA came to be in 1990), and even assassination.  He knew that children could handle such delicate topics as long as you were honest and gentle about it.  I think it was he that said (paraphrased) "children can tell when you're not being honest about something, they may be children but they aren't stupid"

One of my favorite childhood times was when Mr McFeely came to our school.
[g0rfyuh] (score 50, diepte 1 OP) Well thanks for pointing that out 

I just saw this on r/nextfuckinglevel and thought I'd share for y'all
[g0r23jn] (score 47, diepte 0) I wish I had Mr.Rogers in my childhood :(
[g0r38yf] (score 38, diepte 1) Because the imagery of Jesus washing the feet of the disciples is powerful in Western cultures.
[g0r9smq] (score 36, diepte 1) Fun fact: During and after Reconstruction there really wasn't any segregation in the federal workforce.  Black and whites worked alongside each other regularly.  When did that change?  When Woodrow Fucking Wilson decided that segregation should be a thing across all branches of civil service.  Everything from the post office to the military.  

People who thing Trump is a tyrant obviously never picked up a history book and read five minutes about Woodrow "I screened 'The Birth of a Nation' as the first movie in the White House" Wilson.  Trump certainly isn't our best, but Wilson got us involved in WWI, got us a federal income tax, and introduced the Federal Reserve (which has done fuck-all to prevent economic collapse) among many other terrible acts.
[g0r3hcg] (score 30, diepte 1) No its just a myth.  He never served in the military.
[g0qzyl2] (score 29, diepte 1) Because his feet are wet.
[g0r3yw9] (score 28, diepte 1) As much as you might not expect it, gov jobs (at many levels) were some of the first to desegregate. 

Sure, I'm sure plenty of small agencies took a loooong time, but the military, for instance, was one of the first notable big organizations of any sort in the US to recognize racial equality.
[g0rfgi9] (score 27, diepte 3) Yup.

And there's a large faction of politicians today that are fighting for it to happen again.  Remember half a decade ago when students on some college campuses were asking for segregated on campus housing to make "safe spaces" for students of color?  Well those students have since graduated/dropped out and are pushing for it to happen for the rest of us.  California Prop 16 states:

>Proposition 16 is a constitutional amendment that would repeal Proposition 209, passed in 1996, from the California Constitution.

Prop 209 states:

>Proposition 209 added Section 31 to the California Constitution's Declaration of Rights, which said that the state cannot discriminate against or grant preferential treatment on the basis of race, sex, color, ethnicity, or national origin in the operation of public employment, public education, and public contracting. Therefore, Proposition 209 banned the use of affirmative action involving race-based or sex-based preferences in California.

Therefore a YES vote on Prop 16 means:

>A "yes" vote supports this constitutional amendment to repeal Proposition 209 (1996), which says that the state cannot discriminate against or grant preferential treatment to persons on the basis of race, sex, color, ethnicity, or national origin in public employment, public education, and public contracting.

A NO vote means

>A "no" vote opposes this constitutional amendment, thereby keeping Proposition 209 (1996), which says that the state cannot discriminate against or grant preferential treatment to persons on the basis of race, sex, color, ethnicity, or national origin in public employment, public education, and public contracting.

We're about to see if California is about to go so far left that they will prove the Horseshoe Theory correct.  This measure is attempting to allow the state of California to discriminate based on race, sex, color, ethnicity, or national origin in public employment, public education, and public contracting.  This is the antithesis of what a "progressive" government is all about, unless this is really what "progressives" have always wanted.
[g0r68hx] (score 26, diepte 1) To explain the whole officer Clemmons story, Mr. Rogers was aware of his sexuality but was fearful of the scandal it would cause if he went public and appeared on the show, because it’s supposed to be a kids show. Later as people starting coming out he started to allow him to be open about it and always supported him having a long term partner and would often invite him and his friends to his home. So Mr. Rogers knew about it but once it became more accepted is when you saw it on the show.
[g0r883z] (score 23, diepte 1) You had me in the first half...

Thought you were a crack job.
[g0r6l4c] (score 23, diepte 1) Bob Ross was in the military during Vietnam. I think that’s how the urban legend started that Mr. Rogers was.
[g0r3my8] (score 22, diepte 0) While it was super cool that they made this scene, the "officer" is an actor, who continued to appear on the show for many years in this role. He was (is, I think he's still alive) also gay, a fact that Mr. Rogers was aware of.  It's interesting that he could wash the feet of a black (fictional) police officer on the show, but as far as I know he never openly acknowledged sexual orientation, even if in his private life he was apparently not judgmental about it.

Progress isn't a straight line.
[g0rfrmw] (score 21, diepte 1) I dont recall much "heterosexuality" on Mr Rogers either.
[g0r45vm] (score 19, diepte 2) Wait, you mean to tell me the internet was wrong?
[g0r46o3] (score 17, diepte 0) It’s always nice to see humanity in people.
[g0r5w1s] (score 17, diepte 0) Mr Rogers is who we need in front of Congress right now
[g0rfkxz] (score 16, diepte 2) > Mr McFeely came to our school

And this is the first time I've been jealous about someone meeting a celebrity in long while.
[g0r8nw7] (score 16, diepte 1) Just because you fight one good fight doesn't mean you're not supportive of the other fights.
[g0rbmye] (score 15, diepte 1) Agreed. There's plenty of things wrong with this country, but it's still better than any other place I might ever want to live.
[g0raj8o] (score 14, diepte 3) https://youtu.be/c5Y25FT7DxE
[g0r0ak6] (score 13, diepte 1) Id assume they were wet and to show that they were equals or something like that
[g0r1bs4] (score 13, diepte 0) I remember watching that episode. Obviously not when it first aired but a re-run many many years later. Isn't it amazing how far we've come and still how far we have yet to go.
[g0r5dga] (score 13, diepte 1) Good thing there's an infinite supply of humanity, otherwise Mr. Rodgers would be using up most of it.
[g0reoii] (score 12, diepte 2) When I was in school, the rumor was he was a sniper in Vietnam
[g0r5lvt] (score 12, diepte 1) I don’t know if you think this is someone’s aunts Facebook but This happens a little while ago pal
[g0rbui5] (score 12, diepte 2) Didn’t know that about segregation.  What a douche.
[g0r2dhs] (score 11, diepte 1 OP) Same I only saw this on r/nextfuckinglevel and thought i would share it for y'all
[g0r4h67] (score 11, diepte 0) Mr. Rodgers was a good man.
[g0reu6r] (score 10, diepte 3) Yeah thats what I always heard.  He was a sniper with a shitload of kills that would make Chris Kyle proud.  

Also the rumor said he was covered in tattoos and thats why he would wear long sleeves all the time.
[g0rfyv8] (score 9, diepte 2) But he did win the ultimate showdown.
[g0r9xjg] (score 9, diepte 2) Ross was just a drill instructor iirc, but I can always be wrong
[g0rg96b] (score 9, diepte 3) Oh MrMcfeely would regularly go to schools all around the greater Pittsburgh area.  Our school was K-5 and only had 330-ish students so it was rather small.  IIRC each grade only had two classes for each grade.
[g0r8t4p] (score 9, diepte 2) Yep and General Matthew “Old Iron Tits” Ridgway was an early advocate for desegregating the military.
[g0r590a] (score 9, diepte 0) I love seeing this in this subreddit
[g0r5kwf] (score 9, diepte 0) Mr. Rodgers = Pittsburgh legend!!!
[g0r5nhl] (score 9, diepte 0) We need Mr.Rodgers back
[g0r5hur] (score 8, diepte 2) Too true
[g0r7i4n] (score 8, diepte 0) Mr Rogers was a champ
[g0r977m] (score 8, diepte 0) How it should be. Good on both of them for taking the risk and handling race issues the way it should be!
[g0r9rlu] (score 8, diepte 0) The world could use Fred Rogers right now. Wish he were still here
[g0r76nz] (score 7, diepte 2) Oh thanks for that info! 

I can definitly see how the military would be eager to desegregate, segregation was a huge limit on their enlistment numbers.

Guess I gotta go watch "Da 5 bloods now" since I think it touches on that subject.
[g0r529h] (score 7, diepte 0) Mr.Rogers is a national treasure!
[g0r5p1h] (score 6, diepte 2) My comment was clearly ironic. It's sad that I had to mention that.
[g0r3n80] (score 6, diepte 0) Really interesting how segregation was seemingly in full effect with the odd exception of police... 

How does that work? Legit question.
[g0r2owi] (score 5, diepte 0) They just had to do it in black and white, didn't they?
[g0r68vi] (score 5, diepte 6) "I am so proud...of this community"-PewDiePie
[g0r5ebg] (score 5, diepte 0) Love this!
[g0rg9w1] (score 5, diepte 0) God that man was amazing
[g0r5w7a] (score 3, diepte 5) I still have hope in you :)
[g0r5rfz] (score 2, diepte 3) “Clearly”??? There’s a reason the reddit gods have us

/s
[g0r5usp] (score 2, diepte 4) I still have hope for this community
[g0rh16n] (score 1, diepte 0) Sadly, brigaders have attempted to derail a thread with so much positive potential. Because most of the positive aspects have been discussed, and most of the recent posts have attempted to fan racial flames.

For that reason, this will be locked. To those who see all the manners of good contained in the original post - thank you. Please carry those messages into the real world.
[g0r6yqj] (score 0, diepte 0) doesn’t really look like there’s any color though
/s
[g0r1thw] (score -28, diepte 0) Wasn’t Mr. Rogers a SEAL or something crazy like that

