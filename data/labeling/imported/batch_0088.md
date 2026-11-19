# Label-batch batch_0088

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
Schrijf het resultaat naar `batch_0088.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: eqp2br, 17u2nwv, 1j3lkpw).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD eqp2br ===
SUBREDDIT: r/physicaltherapy
DATUM: 2020-01-19  SCORE: 4  REACTIES: 79
TITEL: Treating plantar fasciitis - looking else where than the feet
POST (source_id=post):
Does anyone have evidence on treating  the hip or back to rehab plantar fasciitis?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[fevilky] (score 13, diepte 0) Plausible that a back or hip issue that causes someone to load one side more and be an aggravator. But I would treat locally mainly first though. If it’s a big enough factor then yeah address it. But beware of going deep down the rabbit hole of compensations and plausible “causes” and telling patients they have some deformity or abnormality. You have no idea how long patients will hold onto an idea that their low back is out of place from one passing comment from a health care professional.
[fexymh5] (score 6, diepte 3) If you’re just going by that abstract then you’re misinterpreting the data. And even just by the abstract and you, it clearly says that TrA was active tonically during gait which implicated the trunk muscles during gait to maintain core stability. If you don’t maintain sufficient tonic activation then you may skip into anterior pelvic tilt, hip IR, and loss of arch which may lead to excess strain on the plantar fascia
[fevub7j] (score 6, diepte 0) I have no evidence to support my claim. But you absolutely need to look at the back, hip, gait and biomechanics of the whole LE if you want to get rid plantar fasciitis. You don’t just randomly get it. It’s 100% user error. People who treat just locally will tell you plantar fasciitis takes years to get rid of. Even in people who have had it for years, If you actually address the mechanical stress causing the plantar fasciitis, in my experience it is consistently 75% better in 3 months and gone in 4-6 months.

One other issue I want to add, at least where I work, about 50-60% of patients who come in telling me they think they have PF or their dr told them they did, have something else. Tarsal tunnel, lumbar radiculopathy, and terminal nerve pain related to putting edema being the most common.

EDIT: coming out of school I thought I was awesome at treating PF. I went by the clinical practice guideline. I was so sure I knew everything. It wasn’t until I worked with and learned from a very skilled foot specialist PT that everything I knew was wrong.
[fevii89] (score 5, diepte 0) There may not be direct evidence for plantar fasciitis but just from what we know about the posterior chain and biomechanics, if the trunk and hip are weak then it may contribute to excess stress down the chain
[feybt3s] (score 3, diepte 3) Nowhere in this study does it say that trunk musculature is silent on EMG. Neither does it say that in here: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5098207/

Or here: https://journals.ke-i.org/index.php/mra/article/view/1356
[feyfmgw] (score 3, diepte 2) I’m looking for anything that would cause more force to go through the plantar fascia. It’s an engineering problem.

Some examples, but not a commutative list:
- tight hip IR causing them to torque their food on push off.
- ant pelvic tilt causing them to stand with more wt on the forefoot.
- weak glut med causing the foot to overpronate on wt bearing.
- a long leg or scoliosis causing more wt to put on one foot.

These are just some examples of stuff that ends up putting more load through the plantar fascia. Often there’s a bunch of things that need to be addressed.


When stuff is working right, gait should take very little strength.
[fewqtap] (score 3, diepte 1) There’s plenty of evidence to show that a trunk/hip strengthening program can improve gait mechanics in walking and running, so yeah, I’d say it matters

https://www.ncbi.nlm.nih.gov/m/pubmed/19083652/

https://www.ncbi.nlm.nih.gov/m/pubmed/25700607/
[fey2k99] (score 3, diepte 3) Use scihub dude.
[ff1cm6v] (score 3, diepte 0) Weak glutes <> hip internal rotation <> knee valgus <> flat feet (pes planus) <> plantar fasciitis

Obviously it's not quite that simple, but issues at the hip/back can effect the foot in some cases. If the glutes aren't capable of taking on the load that they are supposed to, that force has to go somewhere!
[fewrn0h] (score 2, diepte 2) Source? You show an obvious bias when it relates to LBP/trunk literature
[ff1umdn] (score 2, diepte 9) I don’t think “weak abdominals” has strong evidence to be linked with injury and research also shows that. However, it’s my opinion and thought process inability to access major muscle groups like abdominals and glutes and postural muscles for example, lead to inefficient movement patterns which can lead to excess movement in areas that should be more stable. Essentially people with pain or an injury often times do not move well. So teaching them how to move well can help their pain, and moving well involves the ability to engage all these major muscle groups
[ff1hlqg] (score 2, diepte 2) Yep treat what’s in front of you and do what’s most likely first. It is very easy to find what you want so confirmation bias is huge with many PTs. I think too many PTs love to make really interesting and complex and will often reach. Think about what doctors do - unless it’s something that seems really off or obviously something else, then they will assume it’s the most common issue and treat with the widest net treatments. I say this explicitly because so many PTs don’t even try the usual/recommended treatment because they want to hit that case study gone run and make things really complicated. Provide the simplest and widest net solutions first. we have the benefit of getting to see people over several weeks often once a week or more, which lends to this method of treatment. Some PTs think it’s lazy but it’s efficient. And giving people an hour of shit they don’t need to do doesn’t help them.
[fewswdo] (score 2, diepte 3) http://www.thera-bandacademy.com/elements/Clients/docs/carpes2008lowback__201201DD_022259.pdf


https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4127508/
[ff4d0vt] (score 2, diepte 0) If the have burning, tingling, numbness that is changed with posture in a lordosis start at the spine with repeated motions assessment
[feyyhw8] (score 1, diepte 5) from the Plantar fasciitis CPG: “Measures to Assess Level of Functioning, Presence of Associated Physical Impairments to Address With Treatment, and Response to Treatment
• Trunk, buttock, and thigh strength and movement coordination to control lower-limb internal rotation at loading response and hip abduction at loading response and midstance”

https://www.jospt.org/doi/pdf/10.2519/jospt.2014.0303
[fez7mqi] (score 1, diepte 5) This is not a 1:1 relationship, but if your proximal musculature (I.e. core musculature) does not stabilize, the forces are shunted elsewhere which most likely is further down the chain. Since the foot interfaces with the ground it takes more force than the knee or hip so the plantar fascia can be affected by ineffective core musculature
[fezdci1] (score 1, diepte 6) but if you tell someone with PF pain to keep their tummy tight when they walk - it wont change there current shitty pain.  Maybe im wrong dude and thats fine please tell me.

If keeping it tight doesnt help their pain then why strengthen it
[ff1s5pm] (score 1, diepte 7) Accessing their abdominals will not fix their pain, but it may have contributed to their pain. I’m not saying to ignore other aspects down the chain but we can’t ignore up the chain and just treat the injured area
[ff1styh] (score 1, diepte 8) Do you have any evidence at all that core weakness can contribute to pain/injury?

My doctoral group researched this extensively and found it to be a myth...
[ff1uxjw] (score 1, diepte 10) Thanks
[ff1vcs6] (score 1, diepte 10) Out of curiosity how much training on complex pattern generators (CPGs) did u get in PT school?  I got a ton of it (fortunately or unfortunately) and it has shaped my belief that the way we move is very innate and natural in an efficient pattern without an exercise trainer :(
[ff2rgpy] (score 1, diepte 11) I mostly got exposure to it when I learned about spinal cord injuries. I wouldn’t worry, we can change habits when it comes to mechanics, it just takes a while sometimes
[ff2yolo] (score 1, diepte 12) Thumbs up emoji!!
[fewit76] (score 1, diepte 1) agreed
[ff0v6if] (score 1, diepte 1 OP) I totally agree that patients hang on to things said especially when it comes to the back. Also, I think patients would not understand and get annoyed if I’m treating everywhere but the foot but with that said I think there is a lot of contributing factors throughout the body that can cause PF. I’ll treat the symptoms for patient satisfaction but I definitely want to fix the problem too.
[fewj1ey] (score 1, diepte 1) Thanks for posting!  A couple questions piqued my interest!  


What do you look for in/on someones back and why?

  
does a stronger hip mean we use more strength during gait?
[ff0pbgm] (score 1, diepte 1 OP) This is my exact thinking. I’m a student in my rotations and I am planning on doing my in-service on this. This is why I’m looking for evidence to back it up. There is some mechanical problem up the chain likely causing people to load the PF improperly. This clinic I’m at gets a lot of PF patients and the treatment is always the same and doesn’t seem skilled to me at all so I wanted to present on this idea of look up the chain.
[ff19bb4] (score 1, diepte 2) I’m sorry I can’t help with the evidence part, but I think it might be hard to find any evidence too specific because it’s not really something that easily fits into any kind of research. Due to how customized the tx is, it wouldn’t be something that fits into any protocol.

That said, it sounds like your clinic REALLY needs this. Basically no tx for PF should look the same.
[few7kps] (score 1, diepte 0) I had it and got rid of  it within two weeks with just foot massage.  It has threatened to come back but minor massage takes care of it.
[fewcwbl] (score 1, diepte 0) I had it and I just massaged the hell out of that foot all the time until the pain eventually dissipated.
[fews134] (score 1, diepte 2) its almost $100 for me to access.  id like to read it tho
[fezedu9] (score 1, diepte 4) Thank you!!!   


I promise I will read - but im on vacation - finally :)    I will get around to it - it is of massive importance in my field, to be frank.  


Trust me, im one of you guys - we prob share the vast majority of beliefs.    
I just dont tell my PF patints to keep their tummies tight with ambulation but im relatively new at this.  


Is that a cue I should be using with my plantar fasciitis patient?  I graduated 3 yr ago, for what thats worth... so im kinda new at this.  That cue didnt cross my mind to alter stresses at the heel.
[fezodu7] (score 1, diepte 5) Like others have said, focus on local impairments to see if that can improve their symptoms. But if you have someone with significant trunk and hip weakness, that can lead to gait impairments down the chain. So, implement trunk and core strengthening as needed and potentially this may improve gait mechanics. No need to cue an bracing necessarily
[ff1gzin] (score 1, diepte 6) What’s the point of getting a muscle stronger if it won’t be activated during gait (relaxed tummy means tummy training = wasted time IMO)
[ff1k7z8] (score 1, diepte 7) It’s not relaxed though. The articles you and I both posted showed that the core is active during gait. And strengthening is a general term. Usually with core, you’re working on motor control and endurance activities
[ff1omu0] (score 1, diepte 8) Thanks!  Soo... Motor control during exercises on a mat. But not consciously using that motor control during gait when it hurts? Cuz it wouldn’t matter anyways.. The Tummy has SUCH a weak line of pull on the heel.  I don’t have enough kool-aid and I’m sorry that we don’t see eye to eye on this but I def will check out those research articles you were gracious enough to send to me.

What if I told you that our concept that a weak core will decrease risk of pain or injury isn’t evidence based medicine.  It’s an old wives tale - which we then use to rationalize the importance of “stabilization” at other joints as well.  Find me evidence of the core as the protector from pain/injury and I’ll start giving my heel patients tighter tummies... :(
[ff1rz7i] (score 1, diepte 9) Do you consciously contract your glutes and quads when performing a sit to stand? No, probably not. But you do it anyways. If you had a patient who had trouble performing that activity, you’d give them glute and quad strengthening, right? Just because TA or glute med doesn’t attach directly to the plantar fascia doesn’t mean it can’t affect LE biomechanics. 

You’ve literally ignored all previous evidence that has been provided. I could provide you with all the evidence in the world but that’s not going to change your bias. Your personal experience with LBP has clouded your ability to take in these concepts objectively.
[ff1t45w] (score 1, diepte 10) Like I said I’m on vacation but I look forward to reading the evidence when not on vacation.  Once again I thank you for sending and I am open to learning and adjusting my views about heel pain.

I still stand by my word that core weakness doesn’t cause pain as it’s never been proven and it’s something I do actively research cuz it’s so prevalently discussed as fact for some  strange reason.
[ff1u0kx] (score 1, diepte 11) I disagree that my low back pain has prevented me from jumping on weird topics like the role of the tummy in heel pain.  Frankly I’ve always been a cynic.

But yes I have my biases.  You also have your biases (in the other direction) I believe.  But I never took to personal attacks of your ability to think clearly.
[ff1xkz3] (score 1, diepte 11) There’s plenty of evidence to show that core stability training improves low back pain and function, and there’s a physiological difference in core musculature in people with chronic LBP. It’s not necessarily proof that “core weakness” causes pain, but certainly proof that core strengthening can decrease pain. And that’s what matters when treating patients

Two articles showing decreased short term (3 months) pain reports/disability with core exercise vs general exercise
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0052082
https://natajournals.org/doi/pdf/10.4085/1062-6050-51.11.16

Article showing improved LBP and function following trunk muscle training and NMES

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4935645/

Article showing that older adults with chronic LBP have decreased erector spinae CSA and increased intramuscular fat compared to controls

https://www.ncbi.nlm.nih.gov/m/pubmed/28158957/

Edit: 
Actually, here’s some evidence that “core weakness” or decreased activation can cause LBP 
https://www.ncbi.nlm.nih.gov/m/pubmed/20193941/ 

https://www.ncbi.nlm.nih.gov/m/pubmed/22289241/
[ff1ydlq] (score 1, diepte 12) I never denied that “ There’s plenty of evidence to show that core stability training improves low back pain and function” this has been quite clear in the literature, and it is great news :)

But talk-therapy and music therapy and acupuncture also have rehabilitative powers for people in pain with functional issues.

But would anyone say that a lack of music/needles/psychotherapy are causative for why someone has pain in the first place.

Regardless of our differences I do thank you for your time and for sending me literature to review next week.
[ff1zg7x] (score 1, diepte 13) That metaphor is illogical and disingenuous. With that logic, you could argue that quad weakness doesn’t put someone at risk for knee pain/injury or rotator cuff weakness doesn’t put someone at risk for for shoulder pain/injury.
[ff1zwpu] (score 1, diepte 14) I disagree about your opinion on my metaphor.  I like my metaphor.

the knee and shoulder things are correlated and not causative, as far as I can tell.  but I’m here to learn and open to being proven wrong.
[ff1zaa2] (score 1, diepte 12) I took a look at the two links at the bottom. Thanks for sending.

1st link - this is not causation that multifidi weakness causes pain - in the abstract “ The lumbar multifidus muscles (LMM) are important stabilizers of this neutral zone, and dysfunction in these muscles is strongly associated with LBP. The dysfunction is a result of pain inhibition from the spine, and it tends to continue even after the pain has resolved, likely contributing to the high recurrence rate of LBP.”  

“Likely contributing” is the authors biases - not proven facts but the authors personal theories. I only saw the abstract for full disclosure.


2nd link - also no sign of evidence that miltifidus weakness is a causative factor in these people with pain.  It is correlated - “ Average multifidus volume was diminished by 18.1% between groups (P=.026) only at the L5-S1 levels. There was no difference between painful and pain-free sides. There were no volume differences between groups above L5, below S1, or in erector spinae at the L5-S1 levels.”

Anyways, I am grateful for your time despite the personal attack of my critical thinking skills.  My biases are different from yours but we all have our biases...
[ff204cy] (score 1, diepte 13) Okay, well then show me an article that proves that decreased core activation is not associated  with LBP. I’ve provided plenty of resources yet you’ve provided nothing other than personal feelings and experiences. 

Not trying to attack you, but you obviously are very biased
[ff20by6] (score 1, diepte 14) And you are very biased too (we all have our biases).

Why so you say the word “associated” back to me when I’m talking about causation?
[ff20r3f] (score 1, diepte 15) Because it’s essentially impossible to prove causation. You can’t create a large scale RCT with a weak core group vs control and give them exercises/activities to see who hurts their back more.
[ff2115q] (score 1, diepte 16) So you’re saying we don’t have proof of causation and I’m the nutty one who is a nonbeliever?

https://scholar.google.com/scholar?start=10&q=strong+core+prevent+injuries+&hl=en&as_sdt=0,10#d=gs_qabs&u=%23p%3DZNlYCX4tlSsJ
[ff22wy3] (score 1, diepte 17) I’m not the one trying to assert core weakness causes LBP. But there’s sufficient evidence to say that core weakness is associated with LBP and gait dysfunction so why wouldn’t you strengthen the core? You were initially against the idea of core/hip strengthening to improve gait mechanics. I provided research against that. You provided nothing. You’re stuck on core weakness being causational because you know that it’s impossible to prove 100%. But why does it matter? You have a patient with LBP? Give them core strengthening, it’s not that hard
[ff24r58] (score 1, diepte 18) I do give my patients with LBP core exercises because they are a great rehabilitation tool (like talk therapy) not due to a lack of core strengthening as a reason they are in pain.

Massively different arguments

And we were talking about heel pain until you changed the topic to back pain
[ff25zy0] (score 1, diepte 19) I didn’t change the topic. You refused to acknowledge my initial articles that proved you wrong and continued on the conversation which led to LBP. If you would have taken the time to read the articles rather than arguing over this, we probably would have stayed on topic
[ff20k27] (score 1, diepte 14) https://www.ncbi.nlm.nih.gov/m/pubmed/20006294/
[ff213l9] (score 1, diepte 15) You reply with one opinion article from 2010? That’s poor evidence at best
[ff21s5a] (score 1, diepte 16) it’s the same opinion my doctoral research group reached as a group when we were looking up the answer to the question of does a strong core prevent pain/injury.  This was in 2015...
(23 reacties met lagere score weggelaten)

=== THREAD 17u2nwv ===
SUBREDDIT: r/Serverlife
DATUM: 2023-11-13  SCORE: 8  REACTIES: 79
TITEL: S.O.S. for my feet
POST (source_id=post):
I’ve been researching and reading other subs about what shoes most servers like, I’m seeing a lot of Skechers. What else?? I am desperate, I’m getting a little older and after my shifts I can hardly walk to my car. Pretty sure I’ve got a higher arch but not sure, it’s always in the back of my heels that hurts the most. What has helped you guys? Forgive me if this has been asked too many times before.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k910qju] (score 18, diepte 0) Google best serving shoes. They're not gonna be pretty. And keep in mind that those shoes have to be broken in. We like skechers because they are relatively affordable and you get a year or two out of it. But TBH your feet, back, knees, mental health...they are all gonna need attention.
[k91j9iu] (score 11, diepte 1) I think the most I ever got out of Skechers was 4 months when I was high volume. How people get more than a year out of them is beyond me.
[k91iiti] (score 9, diepte 0) Bondi HOKA SR - are the best, in my opinion.
[k91owzu] (score 6, diepte 4) but they are comfy and better than any others I've ever found. I wouldn't even care about how they look if they provided the comfort and my feet weren't killing non-stop. I bought the recovery slides from HOKA as well to switch into after working a shift. Helped sooo much.
[k922rm1] (score 5, diepte 0) I switched to nursing after 5 years as a server and swear by compression stockings. I went from debilitating pain to being able to work 5 days in a row, 15k minimum steps per shift and feeling fine after. My favorite brand is vim and vigr
[k92je3w] (score 3, diepte 2) I can swing about 9 months but halfway through I have to get new insoles to make them last that long.
[k91i725] (score 3, diepte 0) Restaurant work was taking a big toll on my body in my 20s (about 10 years ago). I switched to Dr. Scholl's shoes and the issues I was having—hip flexor stuff, lower back pain, general leg and foot aches—went away over time. *The problem is,* I'm pretty sure Dr. Scholl's changed the quality of their shoes. So while I used to get about a year out of them, starting around 6 years ago I started getting six months out of them.

So I switched to Skechers, because they're comfortable and I got a 30% discount through my job. I'd look into that for yourself, too: especially if you work a corporate job, you can often find a place that'll give you a discount through them (like Shoes 4 Crews). Finally, if you have a weird condition with the arches of your feet or whatever, you should look into getting insoles that may help you.
[k91j6ni] (score 3, diepte 0) I finally caved and bought professional, anti-slip Birkenstocks and the difference (after breaking them in) has been absolutely staggering. I even took a break from high volume work and went back to it and wore them and was amazed at how much better I felt than all the years I wore Skechers.
[k91jp33] (score 3, diepte 0) I recently switched to danskos and am loving them. I like wearing them more than my daily shoes.
[k91lb8p] (score 3, diepte 1 OP) I’ve been looking at danskos too, kuru has come up on my feed a lot too.
[k92pxt6] (score 3, diepte 0) What helped me the most was upgrading the insoles and also wearing a different pair every day- one day is boots, one day sketchers, one day slip ons. Also, investing in a sleep number bed has CHANGED MY LIFE. I went from regular back pain to very rarely, and if I do have pain when I go to sleep it’s gone in the morning. Good luck!
[k92upuq] (score 3, diepte 0) My feet and calves appreciated when I switched to Dansko clogs.
[k96kfqz] (score 2, diepte 4) Get over it tbh, if you’re asking this question, Hokas is the answer. I have a condition that caused massive foot pain and used to be a hobbling pained mess at the end of every shift. Fuck your shoes being cute. It’s a bad idea. Have them be supportive. It’s not like Danskos are cute anyway.
[k933kk5] (score 2, diepte 2) FWIW I have high arches and hokas don’t work for me.
[k93a88o] (score 2, diepte 2) My brother just got a pair of these because he's working with USPS. They were recommended by several of his trainers. They are butt ugly but are supposed to be the saving grace when your job is walking or standing on concrete all day. $175!
[k96q1ge] (score 2, diepte 2 OP) Noooooooo. So many comments supporting Hoka SR I’d almost had my mind set. Why do you think they’re a fad? It seems like a lot of doctors recommend them and people love them
[k91mprn] (score 2, diepte 2) I went with the Tokio Supergrip in black. I love them. I wore them serving high volume and now event/guest bartending high volume and never have the sciatic and foot pain that was making me want to stay in bed for days after a hard shift.
[k91myra] (score 2, diepte 3 OP) Hell yeah, I’m really thinking about investing in a pair, I’ve served for a long time but my feet have never bothered me this much after shifts. Thank you for the insight!
[k91o1ym] (score 2, diepte 4) I found a pair new in the box on Poshmark for quite a bit less than new from Birkenstock, just FYI. And I think my overall break-in time was maybe 7 or 8 shifts. I don't wear thick socks or my toes rub a little on top. A nice thin cotton or wool sock is all it takes and my feet never sweat in them, either.
[k94axac] (score 2, diepte 5 OP) Thank you thank you, last week I bought myself some of the clog crocs, they made my toes numb and I’ve been wearing compression socks on my off days. This thread has been helpful
[k936dhi] (score 2, diepte 2) I caved and bought kurus. I got the atom. The slip resistant is advertised by them but not great in that model. They have other models with better slip resistance. That lil feature aside, my life is changed. 

I was vain and used vans made for the makers with inserts for years. They weren't worth it. Fell apart in a year and my body ached. It was always the walking to my house from my car after a shift that I thought I might need to invest in a wheelchair. The sitting down for ten minutes then standing made my lil feeties scream.

Then I used the Skechers sr max comfort. Great for like six months then started falling apart. Bought a second pair of Skechers and at the first sign of wear at 3 months I decided to invest in something better.

I've had my kuru atoms for about 4 months now. I can't rave about them enough. There's a huge difference in how I feel during and after a shift. And I'm in a better mood since I don't have aching dogs attached to numb stumps. It used to be the next morning after a long shift, standing up out of bed would hurt. Now even that had subsided. I love em. And the atoms look cute so I can still be vain.

Another thing I was doing and will still do after a particularly heinous shift is put a lacrosse ball on the ground and roll it around with my foot. It helps break up any pockets of pain. A coworker used a can of peaches. So. Whatever's clever. 

Good luck.
[k94cy2h] (score 2, diepte 3 OP) Thank you for this, I almost did the same thing with vans and some inserts. Im between kurus and the birks professional non slip kitchen shoes
[k936k36] (score 2, diepte 1) Danskos are good for high arches.
[k91lzxk] (score 2, diepte 0) I just went through this as I just started serving again. Feet were painful, swollen and my Achilles started hurting even throughout the night. I bought new insoles on an 80dollar shoes for crews and it somewhat helped. I rolled by feet lit with a golf ball and night and I took more days off. I was doing 5 days a week and I needed my body to acclimate to how much walking I was doing. It took me about a month and a half for the pain to start to subside.
[k91n0ga] (score 2, diepte 0) Have you looked at foot massaging machines like medipro as well as shoes and inserts
[k91pf2v] (score 2, diepte 2) New ones no they are not the same build quality like ones from 10 years ago that still work. Amazon has similar ones that cost half and will not crap out on you. If you get the heat option you can use it on your calves as well sitting level or in a seat. But don’t over use it at first bc it’s like people who get a massage the first time you’ll be sore. Also the percussion massaging guns work if you hit the arch of your foot it literally stops the plantar foot pain where your heel feels collapsed
[k92bd1o] (score 2, diepte 0) I highly recommend looking into custom insoles. 
I had some made by my chiro and ever since my  pain has decreased substantially. I was suffering from consistent pain in my feet, ankles, knees, & lower back. 
may be a good place to start.
[k92nc2z] (score 2, diepte 0) Could be plantar fasciitis. I saw a foot doctor for it. Lots of stretching before you even get out of bed in the morning helps. If it’s exclusive to end of shift it’s probably not that but I got insoles from powerstep and it was incredible difference
[k92pg8y] (score 2, diepte 0) I just got on cloud monsters and they have helped me a lot. Don’t listen to people, they still need to be broken in.
[k92q0ga] (score 2, diepte 0) I have non slip new balances with dr scholls gel inserts, my feet rarely hurt anymore.
[k92u9hv] (score 2, diepte 0) love my Danskos, and if they wear out, they will replace them one shoe at a time, and if your feet are a bit of a different size, you can buy them in a pair of two different sizes.
[k976tlr] (score 2, diepte 2) yes
[k98vi7t] (score 2, diepte 3 OP) I think I’m going to invest in the Fawnas, lots of good reviews and they’ll go with what we wear at work
[k930yue] (score 2, diepte 0) Lay down and put your feet up the wall.. the blood pools in the feet and needs to be redistributed
[k933925] (score 2, diepte 0) My boyfriend has plantar fasciitus(spelling wrong), and there are these foot sleeves that helped him so much. They have a gel pad in the arch. They slip over the middle of the foot and squeeze tightly. They're awesome, cheap and we were in complete shock at how well they worked.

Also, when he gets home, he uses a foot massager while eating dinner. Then, he lays down and puts his feet up for 30 minutes. Your feet need to be above your heart.
[k939cm5] (score 2, diepte 0) It's about the insoles. Get the expensive kind made for distance hiking from REI. I wear whatever shoes I want now and never have sore feet!
[k93cmzd] (score 2, diepte 1) I would like to add that I don’t buy the ankle ones I buy the loafer looking shoes
[k93dukt] (score 2, diepte 0) I wear all black asics! They have a nice thick cushion. Not non slip but I’m just extra careful when I’m walking in the kitchen and behind the bar.
[k93dx81] (score 2, diepte 0) Just got orthotics - but we get benefits and got it through work. Life changing
[k93f6fz] (score 2, diepte 0) My heels always hurt the most after my shifts. I started wearing Under Armour shoes with comfort insoles. They have helped me a lot!
[k93ouy1] (score 2, diepte 0) You probably need orthopedic inserts. I wear danskos and they have a natural tilt forward which helps alleviate pressure on the back of the foot. Once I got these I knew I'd never go back to other work shoes. 

You might want to see a specialist if the pain persists. They can get you custom inserts.
[k93rzg9] (score 2, diepte 0) I'll never give up my platform Docs. They have been the best, especially with thick socks.
[k93ttsl] (score 2, diepte 0) Dansko brand is all I wear. They’re geared toward nurses so they work great for restaurants.
[k940w8i] (score 2, diepte 0) I’m a hoka fan and have been for years, these days I work on concrete and still wear hoka. At first the walk/look bothered me but a pediatrist recommended them and it helped my feet and lower back a lot
[k94cc3m] (score 2, diepte 0) I just got some srmax Augustas. I like them waaay more than mynold shoes for crews. My coworkers do sketches but I prefer dress shoe looking work shoes. They're wonderfully slip resistant and comfortable as hell on the sole (still breaking in the uppers.)
[k9560cf] (score 2, diepte 0) Inserts help allot
[k956n8y] (score 2, diepte 0) In addition to finding comfy shoes (I like ASICS nimbus), I would also recommend keeping a second pair at work to change into. Just changing footwear can help so much.
[k95dwxh] (score 2, diepte 0) Is it possible you have plantar fasciitis? Stretching your feet for 30 seconds before getting out of bed... before putting any weight on them...can make a huge difference. You can get a pair of P.F. sleeves at most any CVS or Walgreens -type store for $10-12. They saved my feet.
[k95iszd] (score 2, diepte 0) Nah nah, shoes for crews. Look on Amazon. They last forever and get the job done.
[k96d3ql] (score 2, diepte 2) Solovair or Docs then. 🙂
[k96ujhz] (score 2, diepte 4) They are considered "better than Docs".... 

"Soul of air", with premium leather that gets better with time.
[k95thtz] (score 2, diepte 0) Everyone at my place wears Docs, Blundstones or Danskos partially due to our footwear policy but Danskos are the BEST! I started out w/ Blunnies and had foot problems, the wide toe box to support the natural shape of your foot on Danskos is the game changer. I’m on my feet 7-8 hours a day most days and the difference in how sore they are with the Blundtone boots and the Danskos non-slips is INSANE. I can’t recommend them enough, and the all black isn’t even that ugly.
[k9608wk] (score 2, diepte 0) They’re kinda pricey but the Hedley & Bennet Vans high tops are super comfortable and non slip.  Otherwise I’d say anything from Dansko or Birkenstocks will give you the best bang for your buck.  Your back will be thanking you for investing in quality footwear.
[k9b1i6s] (score 2, diepte 0) Shoes for crews is worth looking into.
[k91mkfs] (score 1, diepte 2) Oh, why? cause of how they look?
[k91mpmr] (score 1, diepte 3 OP) Yes, the soles are so big and thick! Like marshmallows
[k952c9v] (score 1, diepte 1) Hokas are a fad. End.
[k91lns6] (score 1, diepte 1 OP) Which pair did you get? The super birki or the Tokio super grip?
[k91na78] (score 1, diepte 1 OP) I actually just started looking at foot massagers today, is medipro your recommendation? I’ve looked at inserts but they all seem the same?
[k94dz7j] (score 1, diepte 3 OP) Thank you so much!
[k95yat0] (score 1, diepte 4) Massaging heat belts are nice mine lasts 2 hours on charge so it supports core while you wear. More stress you can keep off your lower back less likely sciatica can happen
[k92tq8g] (score 1, diepte 0) I just switched to Crocs Bistro, the pro literide ones. I can NOT wear regular crocs, these are a different material and insole and 100% better than the regular bistro.
[k96q4px] (score 1, diepte 1 OP) Clogs?
[k96q3q2] (score 1, diepte 1 OP) Is it the clogs exclusively that everyone is talking about here?
[k97fin3] (score 1, diepte 2) Most likely, yes, but they also make some styles that have either backs or a strap. I was having the same issue so took a recommendation from my Chef.
[k935phy] (score 1, diepte 0) Not a server, but I was a CNA for years (12 hour shifts lifting people, constantly on your feet.  

I used to go to a running store to buy my shoes.  They were a bit more expensive but they analyzed how I walked, my arches, the wear patterns of my shoes to come up with the best shoes for me.  They also told me if I needed inserts.  My feet thanked me.
[k9369b3] (score 1, diepte 0) So Shoes for Crews are my fav but i also buy inserts from tj maxx, ross, marshalls or berlingtons. They have good thick insoles for cheap.
[k937rfc] (score 1, diepte 0) I had  foot pain, and plantar fasciitis, and heel pain is a symptom. I wore these for years. Also, the non slip is incredible, need to give then a few days for the non slip to be effective due to the injection molding coating needing to wear off. I have average arches. 

[Keen Shoes.](https://www.keenfootwear.com/collections/work-shoes/products/mens-ptc-oxford-black)
[k94eenr] (score 1, diepte 1 OP) One of my coworkers does this!
[k93ckz6] (score 1, diepte 0) This is such a hot take but I buy doc martens for work and the first 3-4 days is usually hell trying to break them in but they last forever and I’m super comfy in them
[k93odf5] (score 1, diepte 0) I wear vivobarefoot shoes, but I’m also privileged to work in a restaurant where I don’t NEED  non-slip. They’ve got a wide toe box to let your feet move naturally. Similarly, they need to be broken in and you need to adjust your feet to them. But I’ve been wearing them for years now and I don’t have any foot pain. One $80 pair lasts about six months for me. 

I honestly don’t think this will help you specific OP, just sharing what works for me.
[k940bhq] (score 1, diepte 0) I got the hoka SR and they work great. Ugly ass hell but all restaurant shoes are imo
[k94304h] (score 1, diepte 0) There are some nursing shoes called Clove but they’re really nice to serve in. They’re not cheap, but they’re good.
[k95dcsd] (score 1, diepte 0) Compression socks and sole inserts
[k95ha6i] (score 1, diepte 0) I wear a zero drop boot from lems, it was life changing for me
[k95px7f] (score 1, diepte 0) What styles can you wear at work?
[k968v4u] (score 1, diepte 1 OP) Really anything as long as it’s closed toed
[k96sg7r] (score 1, diepte 3 OP) Omg what’s so great about solovair why are they $315
[k91mard] (score -1, diepte 1 OP) I’ve seen people say this I just can’t bring myself to wear them lol

=== THREAD 1j3lkpw ===
SUBREDDIT: r/Serverlife
DATUM: 2025-03-04  SCORE: 30  REACTIES: 79
TITEL: What do y’all do for sore feet?
POST (source_id=post):
I’ve been in the industry awhile and it’s catching up to me. After working so many days in a row it’s hard to get out of bed on my off days my feet hurt so bad. 

What I do now:
Epsom salt foot baths
Foot / calf massages
Regular pedis


What do y’all do?

(I know shoes matter a ton, do y’all have any that have helped?)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mg1b2wa] (score 45, diepte 0) If you are able to, try changing your shoes mid-shift. I used to do this when I worked doubles. Different shoes will have different pressure points and balance so you can change things up a bit and hopefully have less strain on the same parts of your feet and ankles. I also swear by cloud slides, I wear them around the house after being on my feet all day.
[mg15ozj] (score 30, diepte 0) I wear Hoka Bondi SR's. They're not cheap but are slip and spill resistant. Once I switched to them I noticed a huge difference. I also wear superfeet insoles. 
I roll my feet out with an orthopedic foot roller (Roll Recovery R3 roller) every morning and sometimes after a long shift.
[mg1ahhj] (score 21, diepte 0) I worked at this Japanese restaurant for years that had stairs going up to recessed seated tables in a tatami. So if you had your section that night in the tatami, all night, you'd have to kick off your shoes on the stairs (while carrying trays in both hands), walk across the tatami, get down on your knees, drop the trays. Then stand back up & slip your shoes on. All. Night. Hundreds of times. 

So I strongly suggest you invest in expensive shoes. Not shoes that you need to break in; shoes that are very comfortable the day you purchase them. Merrell's are excellent. I've worn Merrell's for over 25 years. Sorrel is great. Clark's are also very good. 

Foot soaking with Epson salts (and essential oils is nice too) after work helps.
[mg1716s] (score 14, diepte 0) Compression socks
[mg1b286] (score 13, diepte 2) Yup! I also rode my bike across 2 town to get to & from work during that time. I was in great shape!
[mg16g92] (score 12, diepte 0) Invest in good quality insoles for your shoes, it was a game changer for me
[mg2v9x5] (score 10, diepte 1) This works. 

Also change your shoes overall regularly. The material thins as time goes by. 

Also, change your insoles regularly. My feet used to absolutely kill me til i bought some new insoles. At first they didn't feel right but at the end of the night my feet felt amazing. I did just notice my feet are hurting again so.. time for new insoles!

For reference I'm a 35ish F, not this but not terribly heavy, and I use Dr Scholls Extra Support Pain Relief insoles for Women. Runs about 20$, but totally worth it. I have flat feet and it has a pretty stiff arch support that surprisingly helps.
[mg1as4d] (score 9, diepte 1) Holy shit, you basically have to be an athlete to do that job!
[mg2flal] (score 6, diepte 1) Add compression socks and you'll feel even better. I love my Hokas.
[mg164uy] (score 6, diepte 0) I always lay on my back with my legs as flat as possible against a wall for about 5 minutes. It helps immensely. Also if you have a partner who’s willing to help get them to rub your feet or massage/stretch them yourself. 

I wear Sketchers Air Cushion. They are breathable so my feet get less smelly on the 12 hour shifts and provide some good support (plus they’re super easy to wash)
[mg186od] (score 6, diepte 0) Compression socks
[mg3jz2b] (score 5, diepte 1) This trick really works, I agree. Switch shoes in the middle of the shift. When you get home, Epsom salt soak your feet and then wear really soft cushy slippers. You can also elevate your feet at home. And don’t feel bad to just rest!  You walk 10k steps minimum per shift, so when you get home, relax and rest those feet.
[mg1936x] (score 4, diepte 0) Hokas and customer inserts have helped me immensely. I’m 52 with a bad knee still working 50+ hrs a week
[mg1cjpa] (score 4, diepte 0) Heated foot and leg masagers that wrap around. I know they are expensive but they are a God send
[mg2jr0r] (score 3, diepte 2) You right! How did i forget that. Feetures for the win!
[mg1k2wl] (score 3, diepte 1) FOR LIFE!
Seriously thry save my sore old legs and feets that used to be running bars and clubs and restaurants in platform heels (it was the 90s)
I live in compression socks now lol
[mg19i22] (score 3, diepte 0) Just bought new work shoes + compression socks and it’s been life changing. I typically work 8-10 hour shifts 4/5 days a week, averaging 12-15k steps a day. Tried to cheap out buying dollar store socks and Walmart non-slips, my feet bled for 2 months before I finally bit the bullet and bought new shoes. 

I’m currently using the Non-slip Filas, they’re around $40 I’ve had them for about 3 months and they still feel great and haven’t fallen apart. I also use doctor Scholls compression socks, $12 for a pack of 3 on Amazon. 

Hopefully this advice helps, Good luck!!
[mg1dyae] (score 3, diepte 0) Acupuncture is my best friend
[mg272hj] (score 3, diepte 0) Along with all the sock and shoe advice, I bought a cheap $30 foot spa and it’s amazing. Warm bubbly water on the feet for 15-20min with a glass of wine, feels brand new.
[mg36gqn] (score 3, diepte 0) Silicone toe separators after work and/or first thing in the morning are a GAME CHANGER!  Not the giant blue ones. The smaller more fitted ones like these:  https://www.ebay.com/itm/375402706146?mkcid=16&mkevt=1&mkrid=711-127632-2357-0&ssspo=6jzU18_OTau&sssrc=4429486&ssuid=h-o-tbmPSIC&var=&widget_ver=artemis&media=COPY
[mg14rw6] (score 2, diepte 0) I've gone to barefoot shoes and wear them most days now for the last few years. Vivobarefoot more specifically. Haven't tried another brand yet
[mg3gkeh] (score 2, diepte 2) I second this, Hokas, compression socks, and I have a foot massager at home :)
[mg3nysg] (score 2, diepte 3) Yes! I have a foot massager too, heat, pressure and massage. It helps. I've waited tables for 45 years, still going strong.
[mg16g3b] (score 2, diepte 0) Merrells are okay and last a few months. 

Put your feet up when you rest at home, like propped up on a pillow. 

If you can handle it a lacrosse ball works well for knots. (You can either sit with it under your feet as you roll it on the floor or use your hands to work out knots manually).
[mg18la3] (score 2, diepte 0) Lacrosse ball
[mgega5n] (score 2, diepte 1) Absolutely this! I sell shoes and this is something I 100% recommend for my customers. Even if you're just rotating every other day, it helps a lot!
[mg3np56] (score 2, diepte 1) Love acupuncture
[mg1fg8g] (score 2, diepte 0) Stretch your Achilles tendon.
[mg2xqco] (score 2, diepte 2) It would be a lot easier for you to google it.
[mg1kkat] (score 2, diepte 0) Hokas. Seriously.  I was having chronic back and knee pain to the point I had to take weeks off of work.  Switched to hokas. Zero (I really mean ZERO) pain from there on out.   If I had to buy a new pair every week, I would. That’s how worth it they are to me. Truly life changing!!!
[mg1ljsv] (score 2, diepte 0) Treat: 

Epsom salt baths. Even if you don't want to take a whole bath, I used to sit on the side of the tub and either eat dinner, scroll on my phone or read a book for 20 minutes a few times a week. 

Stretch. Be good to your tootsies, give em some love, use your hands or a foot massager ($20 bucks) to work out the stress and give them some relief.

Frozen water bottles- roll your feet over some when you get home.

Prop them up above your heart level when you lay down. 

Also once you're home, don't sit down until you're ready to stay down for at least an hour or two, no matter how tired you are. It just makes it harder to get back up.

Prevent:

Invest in **good** insoles and shoes. If you can't afford both at the same time go for the insoles first. Then get a good pair of shoes. You don't have to spend crazy money, and remember they should last at least a few years so don't let $100 be the reason you get the crappy $30 discount bin ones. If you break it by month and throw in your own physical comfort, it's well worth the money.

Don't stand on concrete or tile if you can help it. Always pick the stress matts if you need to chill for a minute, or any other forgiving surfaces, wood, rugs, carpet ect. Also don't stand still for long periods. Even if your a host walk in place, take a lap. It helps.
[mg2gkzm] (score 2, diepte 0) The thing that made the biggest difference for me was actually walking on my days off.

I would be in a lot of pain by the end of my shift and especially at the end of the work week, and then spend my days off recovering and not doing much. It wasn’t until I increased my activity level every day that I started feeling a lot better, and no pain even at the end of long shifts. I would usually walk 8 miles during a shift, so I tried to walk at least 5 miles on my days off.

Other than that, freeze a water bottle and roll it on your feet before bed. 

Some shoe stores can take scans of your feet and recommend shoes that may work for you. 

This is all the stuff my girlfriend had me do, she’s a physical therapist.
[mg2shai] (score 2, diepte 0) Shoes on rotation.  I just found a good boot for my work finally and bought 3 pairs.  I never wear a pair 2 days in a row.
[mg3e6bu] (score 2, diepte 0) Okay. Listen. I work 3 doubles a week. I was LIMPING getting off my shifts. I bought a pair of the Hokas that everyone raved about. They absolutely destroyed my feet. I have high arches and the arches were so weirdly high and misshapen. I got a pair of the Brooks Ghost Max, which have the cushion of the Hokas without the weird arch. My feet do not hurt at all anymore. Actually life changing.
[mg3uw6e] (score 2, diepte 0) I have 3 pairs of shoes that I rotate through, compression socks help. I also semi regularly do those foot peel masks to shed tough skin.
[mg4mh2e] (score 2, diepte 0) Epsom Salt baths for sure but the best thing I ever did was switch to Hoka shoes. I’ll never wear anything else at work
[mg7eow2] (score 2, diepte 0) My added insoles did not help. I felt like they were making things WORSE. I raged and bought four different kinds, tried them all, and found my godsend. I don’t remember the brand but they’re red and cushy like memory foam, which I feel works better than the jelly kind. 

Topical lidocaine or magnesium spray directly on the feet before a shift. I use the off-brand of theraworx. 

Idk how you feel about medication but Fridays are always crazy and I swear by aleve being superior to all other pain meds. (Again, tried them all) 

And like I’ve seen a lot in this thread, YES Epsom salts and yes a foot massager and slippers.
[mgan60a] (score 2, diepte 0) Just invested in some Hokas and at first died at the price, but after a week of wearing, they’ve been serving me well. Add ons like insoles and compression socks help a ton !! I also make sure to raise my legs/not cross them during my break (avoid putting any unnecessary pressure on the legs and feet)


I soak my feet after work in warm water with epsom salt (the salt tbh is unnecessary, more of a placebo than anything). Additionally, my christmas present from my bf was a foot massager and it’s truly wonderful. Definitely all that stuff adds up and gets super pricey, but you know what the say. Never cheap out on what separates you from the ground. (I say this as I spent my last $30 on a pair of shoes from jc penny’s when I got this job lol)
[mg157sl] (score 1, diepte 0) I’m not a server myself, but the most comfy shoe I’ve ever tried was gel nimbus asics.
[mg3c6t4] (score 1, diepte 2) Any brands you recommend?
[mg4z0pq] (score 1, diepte 3) I really like the ones with padded soles and copper woven in idk the brand
But wherever you get scrubs for medical staff you get great fancy compression socks too! More expensive than amazon most of mine are from amazon
[mg3nfne] (score 1, diepte 3) Impressive. All of it.
[mg1cp41] (score 1, diepte 0) Orthofeet brand! I've tried a lot of other brands but these are awesome, they have great support and I stand on marble floors all day. Good Luck!
[mg1dd78] (score 1, diepte 0) Athletic massage gun
[mg1eq2v] (score 1, diepte 1 OP) On ur feet??? I’ll have to look into that
[mg2n9ku] (score 1, diepte 1) How do you do that?
[mg1grw6] (score 1, diepte 0) Compression socks, foot massages, and a warm bath for me, personally.
[mg1hula] (score 1, diepte 0) Support hose, seriously.  I work 12 hour shifts at a hospital and these are a godsend
[mg1kkq4] (score 1, diepte 0) I work doubles on the weekend and by the end of each night was practically hobbling to bed.   After reading people recommend them on Reddit, I bought some compression socks and wore them over this past weekend and it was a game changer.  My feet and my legs felt as if I had just worked a 4 hour shift and not two 12hr shifts back to back. Highly recommend.
[mg1ks3g] (score 1, diepte 0) Rotate through a few pairs of shoes. I switch off between one with a flexible sole and a firmer sole so that my feet aren't always trapped in the same position 


Get nice thick socks too
[mg1l1m3] (score 1, diepte 0) Rotate your foot wear and elevate your feet at night.
[mg1n5d1] (score 1, diepte 0) good insoles, good socks, soaking in hot epsom salt water after work
[mg1p57f] (score 1, diepte 0) Get some Dansko shoes.  It's what nurses wear all day.
[mg1pi7w] (score 1, diepte 0) When I was a flight attendant we all carried a tennis ball in our bag in a off min it was easy to roll one around under your foot or on a wall for your back it was a game changer
[mg1rea9] (score 1, diepte 0) For shoes, a big difference for me was getting wide size for my dress shoes.
[mg1xqtz] (score 1, diepte 0) Compression socks for sure. But honestly the biggest help was stretching regularly and doing strength training. Overtime, I noticed my legs and feet wouldn’t hurt as much after long shifts
[mg1xsgk] (score 1, diepte 0) Sounds like you need better shoes. I said fuck nonslips and got some Brooks. Absolutely life changing.
[mg3ejs6] (score 1, diepte 1) Brooks is the way.
[mg2f1ic] (score 1, diepte 0) Good shoes, compression footwear. When you're standing, rest one foot raised if you can. Feet raised at home, and wear different kinds of shoes. Lots of water, eat and rest well.
[mg2rfxe] (score 1, diepte 0) I have good shoes and my feet still get sore after working long days in a row. It helps me to kinda prop my feet up at night. I can’t do it to much or I can’t sleep but a lil incline really helps with swelling/soreness in my experience
[mg2s8pm] (score 1, diepte 0) Everyone says shoes but you should also strengthen your feet and muscles by regularly walking, running, and exercising. Time on your feet is what’s going to make you more resilient to time on your feet.
[mg2tc7b] (score 1, diepte 0) Vicks Vapor Rub on the bottoms of your feet. Then put socks on.
[mg2yc1e] (score 1, diepte 0) Birkenstocks
[mgdn4qw] (score 1, diepte 1) Birkenstocks or red wings for sure

Also consuming fish oil/omega 3's will help joints and whole body

Loose some weight to make it easier 

Don't walk barefoot inside house get slip ons with support I love my birkenstocks
[mg3aiz6] (score 1, diepte 0) My mom gave me a footbath, bubble thing. Best thing ever. 

Either that or an ice bath
[mg3as6t] (score 1, diepte 0) I'll soak em in Epsom salt before I take a shower and afterwards use a massage gun with a foam ball attachment and really work the muscles out.
[mg3c6qu] (score 1, diepte 0) honestly i’ve been wearing the crocs sneakers for over a year and i haven’t had feet pain in forever. same pair of shoes, non slips. i think they gave me blisters for the first few days when i was breaking them in and now i swear by them. we’ve even gotten rid of our floor mats and i can work a 15 hour shift with no shoe pain. now if i could only find something for my back, shoulders, neck…. 🤣
[mg3hscj] (score 1, diepte 0) I workout. I do my training before work, take a shower and go straight to my shift. It hurts to wake up next day but I do not know what was it: shift or my training.

I work less: I used to pull doubles, or do Friday pm, sat double, sun am and it sucked big time. Now only pm shifts
[mg3nk0s] (score 1, diepte 0) I wear lakai skate shoes. I also skateboard a bunch and that is honestly way worse than working doubles. My old Thai boss told me to take the semi hemispheres of a shaved coconut core (ones strong enough to support weight) and stand on them in the arches/tarsals and work your feet on them when you stretch and sit.

Losing weight helps a bunch. Get a workout or active lifestyle pumping and your doubles at work will feel like your breaktime.
[mg3q46p] (score 1, diepte 0) Thick socks, shoe inserts, and CBD balm.
[mg3sc4g] (score 1, diepte 0) I love my Altras. 

I also have ice pack slippers that I put on after a bad shift. And I lie on the floor with my feet up the wall.
[mg3uuv8] (score 1, diepte 0) The biggest thing that's helped me is exercise/stretching. Calve exercises that really stretch the muscles and tendons through your feet
[mg3whfb] (score 1, diepte 0) I like to roll the arch of my foot.  Some people use water bottles.  They make actual ones you can buy on amazon.  I have a high arch and I've always used an extra wide, metal can of aqua net hairspray.  It was actually a prop from one Halloween where I dressed up as Tracy Turnblad, lol.  It also makes my legs less achey and my whole body more aligned too.  Also, you can always get a nice peppermint foot lotion.  I have one from SallyEAnder that I love.
[mg3wntt] (score 1, diepte 0) Compression socks can help feet and calves.
[mg4bsij] (score 1, diepte 0) I wear different shoes each day. I have 3 pair and rotate them.
[mg4mm4f] (score 1, diepte 0) Crocs makes closed toed non slips with great arch support
[mg6ln7z] (score 1, diepte 0) Snibbs was the brand that sorted it out for me. Also good shoes outside of work. I like my Ons.
[mgb975w] (score 1, diepte 1) I agree about the sleeve
[mganqb5] (score 1, diepte 1) also, after being team bare foot at home all my life, ive officially become a slipper wearer around the house. i definitely need a cushion between me and tile when i didnt before
[mgdtd1z] (score 1, diepte 0) I replace the insoles of my shoes with Spenco. It took me a while to afford to replace all of the insoles in my shoes. (I swap between three ‘work’ shoes) 
But they work great and keep the pain down. I did 17 miles on a festival day at work, and two 8 mile days in a row after and I could not have done that last year. 

They’re like $25 a piece which kinda feels like buying new shoes but it’s totally worth it. I bought them for my S/O and although she was skeptical she’s on board now too.
(3 reacties met lagere score weggelaten)

