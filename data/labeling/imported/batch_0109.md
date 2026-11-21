# Label-batch batch_0109

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
Schrijf het resultaat naar `batch_0109.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: ls3jbr, 17ga1gl, 56brj1).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD ls3jbr ===
SUBREDDIT: r/ems
DATUM: 2021-02-25  SCORE: 198  REACTIES: 72
TITEL: Alright boys and girls; seeing this has officially re-ignited my desire to do technical rescue. Anyone stateside with first hand experience know how I can get my feet wet?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[goowc2o] (score 207, diepte 0) I think the first step is to be a dog.
[goowq5x] (score 94, diepte 1 OP) Should I do that before or after I get licensed.
[gopejoz] (score 70, diepte 2) Depends, are you a good boy?
[gooyfgj] (score 44, diepte 2) Probably before.
[gopjeei] (score 44, diepte 0) Join the US Coast Guard and become a aviation survival technician (Rescue swimmer). All are at least EMT-Bs.
[gopagok] (score 41, diepte 0) Depends on what you want to do when you say technical rescue. I think there are only 2 or 3 non-LEO Helicopter SAR teams. Intermountain Life Flight out of Utah and one out of Texas that I can't remember the name of right now. Teton County SAR has a helicopter but I'm not sure how it is utilized. Tons of ground SAR teams out there. The biggest thing is you'll most likely have to move or be prepared to spend time away in chunks to be a part of a team.
[gopg1yr] (score 27, diepte 0) Dude, @ me if you're a Newfoundland. Best boys/girls!
[gopvru9] (score 19, diepte 2) I don't know, but when they start talking spay and neuter, run.
[gopvyy0] (score 17, diepte 1) Join the Jolly Greens, and you can get shot at while doing it, too!
[gopt2ny] (score 15, diepte 1) STAR Flight is the Texas one. Based in Austin
[gopp3dq] (score 14, diepte 0) If you have a wide enough definition of technical rescue, you could find opportunities in most medium-to-large fire departments. I've not a fire fighter, so take my advice with a grain of salt, but it seems like the right department can give you a lot of opportunities to volunteer for additional training. Where I did my rotation for my EMT license, they had a USAR tractor-trailer. In the event of a USAR event, the engine crew would switch to the big truck and do their thing and then go back to being a regular engine crew.
[goqil3d] (score 12, diepte 5) Combat Medics are not actual EMT-Ps
[gopub4v] (score 12, diepte 1) I work at one of those medium-to-large fire departments with a technical rescue team. If someone's main interest is doing cool technical rescues then this is DEFINITELY NOT the route to go. You almost never go on cool rescues and the training gets boring real fast.
[gopl8c1] (score 11, diepte 2) I believe in rural areas they are trained to be paramedics and can operate at the ACLS level. According to the recruiter I asked though it’s specialty training and most are trained at the EMT-B level
[gopk42c] (score 10, diepte 1) Yup, that was my thought as well.  I believe they are trained to paramedic.
[gopjpod] (score 10, diepte 0) Become a medic then find a flight medic job. Won't be like this but my buddy does it and gets to do some cool crap sometimes.
[goqb7ai] (score 9, diepte 3) Most military medics are only EMT-Bs but have a scope of practice comparable to an AEMT or paramedic. Or just aren’t comparable. I’m an EMT-B but when operating on orders, I can run a field blood bank and do basic surgeries like escharotomies and crikes.
[goql4dr] (score 9, diepte 7) Not really, no. Their scope is the same as a basic unless they are working under a PA stateside, or are deployed somewhere else. 

They do get a lot of extra training in what you might consider "Trauma-ALS". Crics, IVs, very limited pharm. Most of it is brain dead, like "morphine auto injector" dumbed down. 

Where they really lack is the education. They don't have the training to understand a lot of the *why* they do things, just to do them. Its quite literally like taking an EMT-B and teaching them how to do IVs. Most also never actually do their job, and are terrible basics to begin with. If you put a 68W in the back of an ambulance they would be lost in the sauce.
[gopvaqn] (score 9, diepte 0) Our copter has a sar team that medics can join. Crew chiefs and pilots are LEO, but I’m a medic and dangle from a cable all the time. It’s volunteer but it’s fun.
[goqlh8r] (score 8, diepte 5) Combat medics are no medics by paramedic standards. Their training is recognized at the national level as EMT-B. Had a buddy in medic school who was an army medic, it transferred to an EMT basic license and he had to go to paramedic school once he became a civilian.

PJs, however, ARE paramedics. They actually have an entire 3 to 4 month period where they take paramedic classes and become licensed, through a specialized part of their military training program.

Thats the difference
[goptdkh] (score 7, diepte 1) Or identify as a helicopter.
[goq5n5y] (score 7, diepte 2) There's another one, I honestly forgot about star thanks! The one I'm thinking of I've seen in various flight groups, they are strictly rescue with no EMS or patient care beyond basic
[gopth4d] (score 7, diepte 1) Goodest doggos!!!!
[goqm8nx] (score 7, diepte 9) Even AEMTs have a lot more schooling. 

I'm literally a 68W turned FF/PM, I'm telling you exactly how it is.
[gor2qpw] (score 6, diepte 2) I would say that water would be the first step
[goqoyx3] (score 6, diepte 5) I’m not a W, I’m a SOAMT. Should’ve been more clear on that, sorry.
[goq0y11] (score 6, diepte 1) They are just switching to paramedic.

SAR is 'ALS' but I believe last cycle was the first class to get their national. 

Small chance of actually doing your job, but best chance out of any for tech rescue.
[goqpaom] (score 5, diepte 6) PJs are SOCM grads. SOCMs are paramedics. That includes PJ, SEAL Corpsmen, Ranger medics, Group medics, and 18Ds.
[goqs023] (score 5, diepte 7) Yes, but the term "combat medic" equates to a civilian basic emt. That's the point I'm making
[gor2f0o] (score 5, diepte 12) Nah ill judge you in private, just curious about the course, as I was pretty involved in instructing conventional forces when I was on my way out.
[gopjk17] (score 5, diepte 0) Military would be the best bet.
[gopp79i] (score 5, diepte 0) Aside from joining the military, I would look into your local SAR team. My local team does lots of high angle rope rescue training, as well as quick water rescue, due to the remoteness of our area. Might not be hanging out of a helicopter, but it can get exciting.
[gopy665] (score 5, diepte 0) Navy’s got a contract (HM-ATF) that’ll let you try out for SAR (and I believe they’re all paramedics) right off the bat. 

Might not be what you’re looking for, but it’s the first thing that came to mind
[gosbnjd] (score 5, diepte 0) Step one.  Join the airforce.
Step two. Go to special warefare selection 
Step three. Be a stud. 
Step four. Graduate as Pararescue. 
There ya go.
[goqmwb9] (score 4, diepte 4) Lol gl finding a PA who will sign off on a new whiskey to do a field escharotomy. If yours will then you better stay with them till the end of time, because most won't
[goqrtwv] (score 4, diepte 7) Special Operations Austere Medical Technician, it’s like an extremely basic SOCM. It’s a relatively new qualification intended for non-medical personnel who are often isolated from medical support.
[gopwjnm] (score 4, diepte 1) Not really.... speaking from experience
[goq88f4] (score 4, diepte 3) To be fair they should have a separate certification process. 

NREMT is designed probably 70% towards geriatric and chronically unhealthy patients.

As a FMF,SAR, Ect HM you'll be dealing with the 30% of the NR and in much greater detail.

My NR class didn't teach me anything about GSW besides a sucking chest wound. No packing, TXA, Blood products, ect... 

It's a different beast in its own right and honestly deserves its own licensing. "Trauma Paramedic" wouldn't be a bad name for it.
[goqrjuj] (score 3, diepte 6) Sorry, I'm not familiar with what a SOAMT is then. I saw you were a 35F trying to reclass to 68W and went off of that.
[goqzqls] (score 3, diepte 8) So CLS+
[gor0sho] (score 3, diepte 10) How long is SOAMT?
[goqq0q9] (score 3, diepte 3) So what do they do when someone needs ALS? BLS until they're back on the boat? Flight nurse? Do the choppers even have medical equipment beyond first aid stuff, since they're more rescue than EMS?
[goq0rrw] (score 3, diepte 2) Yes really... speaking from experience, a .01% chance is better than a 0%...

There's no such thing as a dedicated Tech Rescue team IRL. It's all fire departments or volunteers.
[goqsqf6] (score 3, diepte 3) Most of our population and call volume is suburban but most of our square milage is rural, stretching up to the mount rainier national park boundary. We definitely get rescues and cars way down the embankment. All I'm saying though is that when you combine the rate with which those calls happen with the amount of time you're off shift and the amount of times you happen to be working at a station that doesn't get assigned to technical rescues, you don't end up going on that many rescues. 

I just bring this up because I interpreted OP to mean they wanted to do lots of rescues and surely there are better places to work if that's their goal.
[goq1dfi] (score 3, diepte 0) Depending on age/physical fitness folks have already mentioned military options. One I haven't seen in this thread is Air Guard PJs(Pararescue), specifically a RQS. 212th out of Alaska seems to get to do a lot of cool shit. Colorado National Guard aviation bois boast they are like the busiest crew out there. 

For paid SAR in the US realistically you are looking at going LE. Most places the Sheriff's dept handles it. 

You can also look at REMS teams out west during fire season. No helicopter, but you should get technical rope certs.
[got4oh5] (score 2, diepte 3) The other one is Reach air in Washington County, Texas
[goshkqv] (score 2, diepte 1) North Carolina Helicopter Aquatic Rescue Team (NCHART). Civilian FFs and emts with national guard Blackhawk and Lakota crews.
[goqeolb] (score 2, diepte 4) combat medics are actual medics, and i’m sure there is probably another MOS that is also an actual medic, but the only one i know for sure is that PJs are also actual medics

EDIT: I was wrong. Further correction is not needed
[goqwdq0] (score 2, diepte 7) Unless it changed PJs are the one that have their own medical course and do not attend SOCM.
[gossfog] (score 2, diepte 4) From the sound of the the choppers are primarily rescue focused and are operated at the BLS level. Depending on the region they either devert to the nearest hospital or fly back to the boat/facility they where launched from, which is equipped to provide ALS. Paramedics are only staffed on the helicopters in highly rural regions(the recruiter I spoke to used Alaska as an example)
[gopqh93] (score 2, diepte 0) Your local training center should have courses that your department should pay for. Start with the awareness levels and then ops, and then if you are passionate about them enough get your technician level. Rope rescue and swift water are great skills to be technician level at imo. 
Good luck
[goq31jf] (score 2, diepte 2) Oh, for sure. I was under the impression they’d started getting their NR-Paramedic like a year or two ago, my b.
[gornpnp] (score 2, diepte 5) I was not SAR, but helped a buddy through ALS a few years ago.

When they got to Trauma I felt like an EMT hearing paramedics talk.
[gorokap] (score 2, diepte 6) Lol I feel that. I was just thinking the other day, about all the shit and terminology I learned on the job and picking up people from long term rehabs etc. 

Nobody tells you wtf a j tube is in EMT school, we’re just expected to know all this med surg shit on day one lol
[gpas67j] (score 1, diepte 2) First time this has ever been funny
[gophuh9] (score 1, diepte 0) I could tell you a lot about volunteer-based specialized heavy urban search and rescue in Germany, if you're interested.

We don't have helicopters though.
[goqllsw] (score 1, diepte 8) EMT + IVs is basically AEMT.

I was however referring to on deployment
[goqvf7f] (score 1, diepte 10) I'd be interested in how much of that falls on your command/ med control. My dad is an AEMT but did 22 years as a 68W and he was instrumental during the trauma based portion of medic school due to his experience and described a bunch of extra training he did but also a bunch of extra stuff he was able to do. Even now, I ask him his opinion on shootings and stabbings just to get another perspective on things and he'll ask me about weird medical calls.
[gor0pa3] (score 1, diepte 11) 68W has changed a lot in the last 30 years. Also, combat medics who saw lots of combat casualties became shit hot at treating trauma. 

They are one trick ponies though, good at trauma and basic austere medicine but nothing else. 

I was a good medic in the Army, and hed myself to really high standards. I ETSed after getting to do some instructor time and immediately went into paramedic school, and was immediately humbled. I was ahead of my peers in trauma, but incredibly behind the curve on everything else, even BLS medicine.
[goqs8j5] (score 1, diepte 8) That’s fair
[gor07d1] (score 1, diepte 9) Yeah, although that description vastly undersells the skillset and level of training jammed into SOAMT. CLS teaches you how to do shit, but not really why or how to analyze a patient. SOAMT, for example, teaches you how and why fluid resuscitation works. Nowhere close to a doctoral level, but well beyond P level.
[gor0voc] (score 1, diepte 11) A month. (Here we go!)
[gor2r42] (score 1, diepte 13) I say that because every time in the past I’ve been asked that question, it turns into “how can a month produce a competent medic”

Because it’s approximately 350 hours of instruction plus a 40-hour, 2-day capstone FTX. The first ~50 of those are NREMT-B. In comparison, my first semester of medic school was maybe 100 hours of instruction total.
[goqp9tz] (score 1, diepte 2) Where are you, though? City departments, yeah. Semi-rural mountain department? Might have to deal with lost climbers, cars that have gone off the side of a mountain road, river rescues for stranded kayakers, etc.
[gopw5n0] (score 1, diepte 1) > If you have a wide enough definition of technical rescue, you could find opportunities in most medium-to-large fire departments.

Especially departments with an [USAR](https://www.fema.gov/emergency-managers/national-preparedness/frameworks/urban-search-rescue/task-force-locations) presence.
[goqjhsa] (score 1, diepte 4) Absolutely! It’s different. I saw that some SAR guys were glad to finally, “rate” the Paramedic patch in terms of recognition/reciprocity, but let’s be real, SAR does more high speed shit.

They’re not picking up dialysis patients or meemaw that fell down and can’t get up lol
[goq6fn7] (score 1, diepte 0) A lot of Tech Rescue requirements vary from state to state. If you live in Virginia I can offer more specific guidance, but there's probably an introduction to Tech Rescue course that will start the process.

&#x200B;

I've linked the Virginia Department of Fire Programs Tech Rescue progression chart so you can see the different pathways and options. Most of the guys I know end up specializing in one or two areas of interest, rather than trying to do everything.

&#x200B;

[http://www.vafire.com/content/uploads/2018/01/VDFP-Technical-Rescue-Training-Progression-Chart.pdf](http://www.vafire.com/content/uploads/2018/01/VDFP-Technical-Rescue-Training-Progression-Chart.pdf)
[goqrb7t] (score 1, diepte 0) Join the coast guard
[gp4569x] (score 1, diepte 1) This guy knows what the fuck is up
[gosdhhg] (score 1, diepte 0) Enlist in the USCG as an AST
[goq39na] (score 0, diepte 0) This. Or move rural. I got a rescue about every other day this past spring. Most we could just go for a hike and cart em. Two or three high/low angle rescues, one cardiac arrest, and a few had to be flown out. If ya know the local flight crew, they might take you on (depending their policy) as a third if they need another medic. My captain actually got to ride for a full arrest on the bird (went from the engine to the helicopter). The local flight crew knows me (I used to work with them) so based on my weight and certifications I have a high chance of flying if they need another person.
[goqj7ry] (score -1, diepte 6) hm, nvm, guess I was wrong, their scope of practice is essentially the same, though, or at the very least more like an AEMT

=== THREAD 17ga1gl ===
SUBREDDIT: r/Target
DATUM: 2023-10-25  SCORE: 16  REACTIES: 72
TITEL: Comfy shoes
POST (source_id=post):
What are comfortable shoes you recommend for standing a long period of time. I don’t know how people do it with vans and converse, I wore my adidas ndm and towards the end of the day my feet started to hurt.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k6fuua6] (score 33, diepte 0) Hokas were my savor when I worked at Target. They have a nice wide toe box. Forget about what looks fashionable. You’ll regret it when your feet are all fucked up because of being on that title floor all day.
[k6fdl9v] (score 30, diepte 0) Don’t just buy comfortable shoes, get compression socks too.
[k6fqzih] (score 13, diepte 0) Find a style you like, and then buy two more when you're able. I work inbound and I have three pairs of the same shoes and rotate them each day so the cushion has time to decompress before I wear them again.
[k6h4srv] (score 11, diepte 1) Best advice honestly. I only wear compression socks at work now and I went from almost having shin splints every day, to not even having my feet hurt much after work.
[k6f7nf0] (score 8, diepte 0) Sketchers S-Sports. 🫵 Washable and comfy.
[k6feb4z] (score 8, diepte 0) Ultra boost
[k6goq99] (score 6, diepte 0) it depends. are you actually standing all day or do you get to move around because as you can tell by my username I know ALOT about shoes and I've worn the most comfortable shoes you can get while on register and my feet were still killing me at the end of the day, but wearing the same shoes while cart attending and my feet are totally fine at the end of the day.
[k6ggrco] (score 5, diepte 1) Wide toe box my tonsils. Topos ftw
[k6g3o47] (score 5, diepte 0) I've been having good luck with Skecher's
[k6gjidc] (score 5, diepte 0) me wearing af1’s every day 🧍🏽‍♀️
[k6fn54x] (score 4, diepte 0) Asics gel or New balance
[k6focvx] (score 4, diepte 0) On Cloud, rlly nice
[k6g0cxv] (score 4, diepte 1) I always have at least two pairs also, so they can dry out thoroughly.
[k6j9m0n] (score 4, diepte 2) what is your budget? Here's a couple suggestions going from least expensive to most expensive: Nike Pegasus 39, Nike React Infinity Flyknit 3, New Balance Fresh Foam X 1080 (get V10 and up), ultra comfy but i bit chunky looking New Balance Fresh Foam x More V4, Asics Gel Nimbus 25 (I wore these shoes to work plenty of times but I wasn't on register and they are the most comfy shoes I have ever worn) And for the hypebeast in you there is always Yeezy 350s, they are extremely comfy but are a bit expensive and you'll have to pay resale. Hopefully this helps.
[k6ihyd5] (score 4, diepte 0) Go to a Fleet Feet and get a foot scan first. From there you will know what kind of shoes you have to buy. I could never buy Vans either because I cannot wear flat, narrow shoes. I need arch support and a wider toe box.
[k6gvood] (score 3, diepte 0) nike, or any sneakers with generous toe room and thick soles
[k6hn5pk] (score 3, diepte 0) HOKA's. Hands freaking down. When I first started I couldn't even walk the next morning my feet hurt so bad. I got my first pair and within a day it was already better and once the initial soreness from my new balance shoes went away, I have had no issues. I walk 13-15K steps a day. I can't say enough good things about them.
[k6fa25g] (score 2, diepte 0) ASICS SNEAKERS for the love of everything holy don’t get sketchers, they’re completely sealed and don’t have any breathability, they’re only washable because they turn into ovens and your feet will be putting out TSUNAMIS OF SWEAT and you’ll have to wash them like every 3 days just to have them not smell
[k6fa6j0] (score 2, diepte 0) Asics are a little more pricy but will last you waaaayyyyy longer because you won’t be constantly washing them
[k6fn8mg] (score 2, diepte 0) New Balance running shoes and Dickes Dri-tech socks.
[k6i5ra9] (score 2, diepte 1 OP) Im on register but even that stupid little mat doesn’t do anything I’m looking to invest in good comfy not for looks! I’ll look at hokas ty
[k6m1y1e] (score 2, diepte 1) Altras also have a great toe box, but I recommend getting them on sierra trading post because they’re $$$
[k6mbe0e] (score 2, diepte 2) Another good one! Those Lone Peaks are so comfy. I agree with you about getting them on Sierra. More affordable than going to REI or Zappos.
[k6ga6ei] (score 2, diepte 0) New balance ftw 🙌
[k6gbbud] (score 2, diepte 0) Hoka—I switched over to them a year ago and haven’t looked back.
[k6ggqvi] (score 2, diepte 0) I’ve tried Nike and Under Armour, but my favorite so far is Brooks. You really get what you pay for, my shoes were $100
[k6gj6bq] (score 2, diepte 0) Hoka, especially if you have wide feet like me lol
[k6ln6tr] (score 2, diepte 1) same my feet hurt so bad 😭
[k6i5tyq] (score 2, diepte 1 OP) Im on register all day 😩
[k6q7xbn] (score 2, diepte 3 OP) Budget is not an issue really, I’ll check these out thank you
[k6m801t] (score 2, diepte 2) whats your budget, then i can suggest some good ones for you. I have comfy shoes that i paid $70 for but then I also have comfy shoes i paid $200 for lol. Right now my top picks are Nike Pegasus 39, Nike Pegasus Trail 3 (only the 3's though since the 4's are ugly imo), Nike React Infinity Flyknit, New Balance Fresh Foam x More Trail V3 (extremely comfy) and New Balance Fresh Foam X Hierro V7. I know alot of people say Adidas Ultraboosts are crazy comfy but I have a few pairs and I don't really like them, they aren't that comfy for me.
[k6h0t64] (score 2, diepte 0) I’m in fulfillment and love my Vans. 🤷🏼‍♀️
[k6q81zq] (score 2, diepte 1 OP) Thank you I’ll have to go to fleet feet on my day off
[k6fqtgk] (score 1, diepte 1) So good running shoes have more support and last longer for me.  Saucony and Brooks are the best.  ASICS are pretty good and New Balance work but don't last as long.  I go through 2-3 pairs a year.
[k6ffw7v] (score 1, diepte 0) I wear adidas cloud foam and they’ve never done me wrong.
[k6fr4ed] (score 1, diepte 0) So good running shoes have more support and last longer for me.  Saucony and Brooks are the best.  ASICS are pretty good and New Balance work but don't last as long.  I go through 2-3 pairs a year.
[k6gjeca] (score 1, diepte 2) Topos are really good too! Those are truly wide in the toe.
[k6fwujb] (score 1, diepte 0) Whatever type of running shoes fit your feet well. I wear Ultra Lone Peak because they have good support and a wide toe box.
[k6fzygl] (score 1, diepte 0) My go-to for years and years of retail have been Clark's Cloudsteppers. They come with memory foam insoles, but they're deep enough that you can put in your own insoles or custom ones. I also like the Dr. Scholl's ones for plantar fasciitis. Lots of padding in them for walking on those concrete and hard linoleum floors all day. They also come in narrow, regular, and wide, which is getting harder and harder to find. The toe box is big so you have room to wiggle your toes. 

Heads up- the ones I ordered from Amazon were fake. Go to a department store (Macys and JCPenney have them) or order them from their website. There's frequently coupons that work on them, but they do last a fairly long time, so the price is reasonable. The ones that aren't leather are also machine washable, just let them air dry. So that really helps with the sweaty feet and how filthy Target floors are.
[k6g3q9x] (score 1, diepte 0) Mbt
[k6g3quy] (score 1, diepte 0) I got some arch-fit sketchers that work decently if you’re on a budget - try looking into them
[k6g8tob] (score 1, diepte 0) YMMV, but for me: Rx compression socks, Dr Scholl's gel insoles, and Brooks running shoes.
[k6gaw2v] (score 1, diepte 0) I’ve been adding insoles in my AF1s, and it’s helped my joint/knee/ankle pain
[k6gbneb] (score 1, diepte 0) Asics gel or Adidas Ozweego. 

I have a pair of Hokas and they are uncomfortable for standing and walking for many hours.
[k6i5ww3] (score 1, diepte 1 OP) Im gonna have to check them out! Thank you
[k6ox6kp] (score 1, diepte 2) SAME LOL but after a while they just get so comfy and worn down to match my foot 🤣 just recently i got some other nikes idek the name of them but they’ve actually been really comfy so far!!!!
[k6gkhu8] (score 1, diepte 0) I love my docs honestly they’re super comfortable after breaking them in.
[k6jij0s] (score 1, diepte 1) Ooh if you don’t me asking what are some good ones if you are on the move? I have some nike shoes and am also debating if getting new insoles may help out a bit especially on 9 hour days
[k6gtlco] (score 1, diepte 0) I have these Dr. Scholls in white, gray, khaki and black and I LOVE THEM. Super cushy and wide enough.

https://preview.redd.it/vmke159npfwb1.jpeg?width=1284&format=pjpg&auto=webp&s=1130e421bf47e2d4e0ebd284afc96287fe63a668
[k6gxf7c] (score 1, diepte 0) Hokas, if you have the money, but i have Nike Air Maxes and sketchers.
[k6gxyq8] (score 1, diepte 0) Nike, LeBron's editions for me. I ended up buying multiple pairs on a sale that were comfortable for me. I've torn apart other shoes either on the heel of the inside, the toes tear apart, or the insole themselves tear apart within a few months. I'm in year 2 of one pair, you get what you pay for.
[k6gz8js] (score 1, diepte 0) Ariat ftw
[k6h11a6] (score 1, diepte 0) adidas retropy e5
[k6h51hx] (score 1, diepte 0) Allbirds Tree Runners
[k6h6r0u] (score 1, diepte 0) I wear Brooks. I had to buy longer laces for them, but other than that, I enjoy them for OPU.
[k6h7jw2] (score 1, diepte 1) I second Brooks. They’re great. In the winter when I was able to do drive ups and needed water proof and warm, I got snow sneakers from LL Bean. They’re so comfortable and can put multiple winters on them before I need to replace them
[k6ha8fo] (score 1, diepte 0) i wear hokas with inserts. they’re okay. i used to wear air force 1s that i had for like 3 years and they were the comfiest work shoe i’ve ever had.
[k6hb7zu] (score 1, diepte 0) Tacticalgear.com
[k6hfn1w] (score 1, diepte 0) If you’re in a cold climate and are on DU at all, I recommend Merrell boots.
[k6hhwb1] (score 1, diepte 0) I love my Hokas. They have been my savior while working through my pregnancy
[k6hjfen] (score 1, diepte 0) I wear Adidas Ultraboosts. They're expensive, but they're comfy, they work wonders for my plantar fasciitis, and they come in a ton of colors.
[k6hmt0q] (score 1, diepte 0) ASICS! Also if this is your first retail position, you’ll break your feet in soon, it was rough my first couple of weeks
[k6i60ox] (score 1, diepte 1 OP) Yeah it’s my first retail, but even then with any shoe if I stand for long period of time my feet hurt really bad :(
[k6i63cf] (score 1, diepte 2) Grab some Dr. Scholls for your shoes, I did that with my first target paycheck 😂
[k6hnpke] (score 1, diepte 0) San Antonio Shoes. SAS
[k6hnwnx] (score 1, diepte 0) I wear hokas
[k6hpny5] (score 1, diepte 0) blundstone boots!
[k6hptpi] (score 1, diepte 0) I have like 5 nmds I cycle through. I just put in shoe inserts and I have no problem all day. It's the only shoe I buy 😩
[k6i3aqn] (score 1, diepte 0) Get gel inserts for your shoes
[k6i3t7o] (score 1, diepte 0) Gel insoles inside Fila mid-top hiking boots. The gen insoles really make the difference, used them in my old Merrells as well.
[k6i8a2z] (score 1, diepte 0) On a day I know I’m not gonna be running around the store a lot, I like to wear my converse but most days I wear my af1s because they just give my feet a bit more support. I used to have a pair of ASICS that I loved wearing to work when I worked as a food manager for 2&1/2 years, those dudes were insanely comfy
[k6ikpca] (score 1, diepte 0) I'd say preferred brands would be ASICS and Hoka. They're padded all around and have some insole as well as decent arch support. Though, do buy your own insoles or get a custom fit because you will be standing a lot
[k6izldd] (score 1, diepte 0) I have went through countless amounts of shoes in the 5 years that I have worked for target. I would say that under armor are the best shoes I’ve found. Closely followed by croc tennis shoes, but my main gripe with the crocs is that they loose their grip quickly. Crocs would be my first choice if it wasn’t for this issue.
[k6jc2tu] (score 1, diepte 0) So i wore the skechers at first but then it ripped idk how so right now i got the dr.martens
*
*
[k6knao2] (score 1, diepte 0) I just wear sketchers they're comfy and the sports ones go a long way
[k6l5h1f] (score 1, diepte 0) It don’t matter what kind of comfortable shoes you wear, it still hurts. The best recommendation is compressed socks
[k6lytwz] (score 1, diepte 0) I wore crocs.  Not your everyday ones but the made for work
Crocs. Saved my
Feet and knees.
[k6q7r9c] (score 1, diepte 1 OP) I love crocs but I’m scared they’ll tell me I can’t wear them 😭

=== THREAD 56brj1 ===
SUBREDDIT: r/Teachers
DATUM: 2016-10-07  SCORE: 21  REACTIES: 72
TITEL: What kind of shoes do you all wear? Flats have effed up my feet and my feet are in terrible pain... In need of some good, quality shoes.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d8i02br] (score 16, diepte 0) I'm a big fan of Clarks and Born. Both make really great supportive shoes and they're nice enough looking that you don't feel like you're wearing old lady shoes. They're a little more expensive, but totally worth being comfortable all day.
[d8i0q3j] (score 7, diepte 0) Dansko clogs
[d8hybgb] (score 6, diepte 0) Nike frees! And I love them
[d8hyneg] (score 6, diepte 0) My wife wears some kind of foam sketchers and loves them man
[d8i5im3] (score 5, diepte 2) Cons are notoriously flat. You can go up a size and add a big insole or just get proper athletic sneakers with support.
[d8i0yi8] (score 5, diepte 0) Tieks! I've never had a better pair of flats in my life and i blister from just about anything
[d8i65ge] (score 5, diepte 1) If you have an issue like plantar fasciitis or suffer from heel pain, don't follow this advice!
[d8i9ob9] (score 5, diepte 0) TOMS. I have several different pairs and they're my favorite. They're also not super expensive. They look more professional than sneakers but are infinitely more comfortable than flats. If your feet sweat a lot, purchase your pairs about a half size up and get the Vans no-show socks (or something similar) to wear underneath them. 
I refuse to wear anything else to work and I've never had an issue with pained feet!
[d8hyhzl] (score 3, diepte 0) My Converse have been a life saver.
[d8hz5hh] (score 3, diepte 1 OP) I tried wearing my converse this week but they don't have much support, do they? I feel like they are very flat.
[d8hzenv] (score 3, diepte 0) As much as it is a fashion faux pas, non-minimalist running shoes tend to be comfortable for walking and standing for longer periods of time because they have both support and cushioning.
[d8hzh7i] (score 3, diepte 0) Birkenstock makes shoes too.  They are very comfy if a little clunky looking but you can stand in them for hours.
[d8hzrxj] (score 3, diepte 0) As a guy, I love my Rockports, I have a pair of the super light weight sport casual ones.  They're super comfortable and breathe really well so it's worth the $100+ I paid for them.  I tend to be super cheap on clothes (being a guy helps) but I will spend money on my shoes.  Good shoes can make or break a day.
[d8i6ked] (score 3, diepte 1) I wear Clarks. Cam testify most comfortable shoes I've ever owned. I wear the Walter Whites. Same color.
[d8ibd3n] (score 3, diepte 2) Really? Most of mine have been comfortable from Day 1. Different styles I suppose.
[d8hyb8p] (score 2, diepte 0) I wear a pair of comfy brown loafers about 85% of the time. Not crazy stylish, but they are insanely comfy and my feet don't feel like death when I get home.
[d8iqduk] (score 2, diepte 3) I have Chuck Taylor IIs and have worn them to teach and they're a dream! I won't go back to the originals.
[d8i94bm] (score 2, diepte 1) These are very popular on my staff - Skechers Go Walk.
[d8ibm5v] (score 2, diepte 1) I have limped since February.  Podiatrist couldn't figure it out, but 1 MRI two weeks ago and they say "traumatic bone bruising".  Starting last February, I started trying different shoes, thinking that bad shoes were the cause.  I bought a bunch of different shoes and now sport a pair of Rockport boots and running shoes at school.  I added an orthopedic insert that my podiatrist insisted on and have been healing for the past couple of weeks.  She was sending me to physical therapy, but decided that was the wrong idea after the MRI.
[d8ia7gy] (score 2, diepte 1) I'm a guy, but I also wear clarks shoes sometimes. I really like them now, but man they took FOREVER to break in.
[d8ia985] (score 2, diepte 2) You have to work your way into wearing them. 1/2 hour the first day, 1 hour the next, two hours, and so forth. If you try to wear them outright the first day, they will cause pain and discomfort. Once you get used to them, they relieve leg, feet, and back pain.
[d8i49x9] (score 2, diepte 0) I like flats but I've realized over the years I'm picky. I need them to have a soft fabric on the heel or I will get blisters and I need support. My favorites for both have actually been Crocs. They have some styles that don't look like their typical rubber and the cushion in the sole is great for standing all day
[d8i4t68] (score 2, diepte 0) [I bought these croc flats on amazon recently.](https://smile.amazon.com/crocs-Cap-Toe-Rhinestone-Flat/dp/B00REM1JCK/ref=sr_1_46?m=ATVPDKIKX0DER&s=apparel&ie=UTF8&qid=1475861468&sr=1-46&nodeID=679399011&refinements=p_89%3ACrocs%2Cp_6%3AATVPDKIKX0DER%2Cp_12%3A-7x) I'm on fall break so I haven't tested them yet with a full day of teaching, but I have spent the day in them and they are the only flats I own that did not rub my heel raw the first time I wore them!
[d8i7evd] (score 2, diepte 0) Really you need to find out what kind of shoes work for you. Go go to a store and try a bunch on.

Flats can be great if you have strong feet, pain near the ball of your foot, high arches, supinate, or lower back pain.


A more supportive shoe (arch mostly) works when you have pain near the back half of the foot, pronate, or have weak foot strength.


There are varying levels of cushion and rigidity that may work better for you. If the first thing you do when you get home is take off your shoes and enjoy walking around your house barefoot, go with a flatter shoe.


Also, spend a bit of more to get a better quality shoe.
[d8i94ze] (score 2, diepte 0) I have flat feet that pronate badly, so I need an excessive amount of support. I wear Red Wing 6 inch black boots (the 607) with Super Feet inserts. They are a little on the pricy side, but I've been wearing the some pair for four years now. The only time I get foot pain is after a long hike. Standing in front of a class is cake.
[d8itlqq] (score 2, diepte 1) People are intimidated by "work boots", but there's a reason those boots cost so much.  The quality of construction between a pair of tennis shoes and a pair of Red Wings is night and day!
[d8iuiaa] (score 2, diepte 2) That's why I've been wearing them for nearly 10 years. I'm on my second pair.
[d8i9yqw] (score 2, diepte 0) I wear all Birkenstock, all the time. I even bought a sparkly pair to wear at my wedding!
[d8ib8dj] (score 2, diepte 0) Toms del rey. They are tennis shoes, but my staff is pretty casual.
[d8id8kf] (score 2, diepte 0) If you need support, Vionic is doctor recommended and has some cute styles. I love mine and they help with my foot pain. Birkenstocks, as others have said, are also great. Look for shoes with removable insoles so you can add whatever insoles work best for you (Olukai sells some like this, toms has a style with a removable insole, LL Bean and other outdoor outfitters sometimes have cute work appropriate styles). The Walking Company is a good resource too. I have a whole folder on my computer of shoes that might work for my problem feet, so let me know if you want more suggestions and I can get them to you.
[d8ilhx8] (score 2, diepte 1 OP) Tom's are what gave me this problem! 😑
[d8hyeoc] (score 1, diepte 0) I wear flats that have comfortable insoles and kitten heels. I'll be wearing more boots soon. I stick to kitten heels for when I dress up. Just more comfortable and don't stand out as much. Payless has good comfortable options.
[d8hyfq5] (score 1, diepte 1) The two flats I wear are free Tommy hillfiger btw.
[d8ig34f] (score 1, diepte 2) They have actually recently "redesigned" them and there is now some support in them. I haven't tried on a pair of the new version but I did stick my hand in to feel it and there's definitely arch support.
[d8sjip4] (score 1, diepte 1) I have naturally flat feet and these are the only sneakers I can wear comfortably ! Arch supported shoes give me horrible pain after a while !
[d8hyswm] (score 1, diepte 0) What kind of flats are you wearing? And what kind of surface are you standing on all day?
[d8hz4ca] (score 1, diepte 1 OP) Flats like Tom's, so no support whatsoever. And I'm walking around the classroom and running around out on the blacktop during recess.
[d8ic2ev] (score 1, diepte 1) Whenever I feel like comfy shoes I put on my adidas duramo's. They look like sneakers but are really the most cushioning and soft running shoes! I even got a second pair to use my old ones as regular shoes. I got them at 37€ a pair.
[d8i8u53] (score 1, diepte 1) I have a pair. Gonna buy clogs for winter. Love them.
[d8ia2y8] (score 1, diepte 1) I wear my snow boots too and from school in the winter and rock the Birkenstock clog in the classroom. So comfy!
[d8iqo1n] (score 1, diepte 1) I am also a huge fan of both of these brands. Clarks Feature Film Mary Janes are my ultimate favorite shoe. I've also had good luck with creepers, specifically the TUK brand. That's a specific type of style, though. Naturalizer is another brand I've worn that's worked for me. They have some really cute stuff and they have an online outlet store which I love.

Soon it will be winter and the only slightly fashionable-ish boots that have stood the test of time for me are Doc Martens. I put my own insoles in them when the ones that come with the boots wear out. I've worn the same oxblood Docs all winter long (including to teach in) for the last four years. I've had too many boots where the soles have cracked from wear, but not Docs.
[d8i8isp] (score 1, diepte 1) You either love or hate Danskos. Their sole doesn't bend, so they give me shin splints. Also, too wide for me. Very supportive arch though!
[d8i1hr3] (score 1, diepte 1 OP) I'll look into them, thank you so much.
[d8i8jsm] (score 1, diepte 1) Where do you blister? I have a problem w flats cutting into the back of my ankle.
[d8i1h66] (score 1, diepte 1 OP) Thanks for the suggestion!
[d8i3kr3] (score 1, diepte 0) I love my Crocs loafers.  The look like nice boat shoes and are so comfy even after teaching all day.  They may not be as cute as some of my flats, but they are still nice, are not too casual and have saved my feet! I would highly recommend these!
[d8i4jdr] (score 1, diepte 1) Crocs makes comfy flats!
[d8i3nle] (score 1, diepte 0) I now own 7 different pairs of DC heathrows. They are lightweight and comfortable and they come in a whole bunch of different colors, patterns, and fabrics. They have laces but they are fairly ornamental as the shoes are a one piece slide on style with connected tongue.
[d8i3pj2] (score 1, diepte 1) Oh, and the best part is if you catch them at the right time on amazon you can find them for as little as 25$ although they retail for about 80$.
[d8i4i9a] (score 1, diepte 0) Insoles.
[d8i787k] (score 1, diepte 1) I wear these all the time!
[d8i5h5f] (score 1, diepte 0) Bye bye fashion, hello comfort shoes. Dansko clogs, running shoes, loafers with insoles, in summer it's flat sandals with arch support and a heel strap. Check out the comfort brands like naturalizer and Munro, and feet-friendly stores like the walking company. All of the dorkier shoe options look fine/unnoticeable with long pants. For bare legged outfits it's a bigger fashion impact and cute shoes will be harder to find.

Men's comfort oxfords, loafers, and sneakers look no different from uncomfortable versions, and they don't have the skirt problem.
[d8i5w4j] (score 1, diepte 0) Keen makes really good looking shoes that skirt the line between very comfortable and professional looking.
[d8i6eoc] (score 1, diepte 0) I use insoles in my shoes. Supports my metatarsel and helps reduce stinkyness. In a pair Adidas.
[d8i8j7v] (score 1, diepte 0) Danskos, or if you don't like leather, SpringStep.
[d8i92qc] (score 1, diepte 0) The cole haan pumps with nike air in them changed my life...while they were more expensive...they went with everything and lasted...so I bought less shoes.  So, I ended up spending the same I normally would.
[d8itlov] (score 1, diepte 1) People are intimidated by "work boots", but there's a reason those boots cost so much.  The quality of construction between a pair of tennis shoes and a pair of Red Wings is night and day!
[d8icmam] (score 1, diepte 0) In our board, we get a free orthopedic thing once every two years so I got inserts that I use in all my flats. When I'm not wearing flats and the season's changing I wear a lot of ankle boots (super comfortable) and longer boots - they never ever stop being comfortable to me. Sometimes Converse running shoes as well when I want to be casual and I love how comfortable they are.
[d8illb4] (score 1, diepte 1 OP) Thank you so much!
[d8ie4zx] (score 1, diepte 0) Danskos, baby.  They are expensive, but my current pair is on its 7th year, and they're just starting to look worn.  So great.

I also like Born shoes- they come in some cute styles.
[d8ihhmv] (score 1, diepte 0) Toms are cute and totes comfortable!
[d8ikrs7] (score 1, diepte 0) I blister everywhere. Back, side, toes, arch... they're expensive shoes for flats but once I broke them in I've never had a problem.
[d8ithtm] (score 1, diepte 0) A high quality pair of work boots like Redwings or Timberlands.  They take awhile to break in, but once they're broke in are the best by far.  Plus, they add height and authority.  My Timberlands might look uncomfortable, but in reality have a 1"+ foam sole.  You have to wear Crocs to get more cushion than that.
[d8j0zqr] (score 1, diepte 0) I wear Skechers all the time and they are fabulous. The ones I wear are from a range called bikers but there are several other similar styles and they have foam in them for foot support. I have wide and rather large feet and certain styles of Skechers are super comfortable and fit really well.
[d8j4vmc] (score 1, diepte 0) Crocs, Crocs, Crocs! Don't laugh. I had terrible plantar fasciitis and Crocs were the only thing that saved my feet. You don't have to wear the big clunky clown shoes-- they actually have some pretty cute flats and clogs. Check their web site. And if you go to a Crocs store, they give a teacher discount with ID. They are fairly inexpensive (generally around $25-45 a pair) and if you sign up on their web site they always have coupons and sales.

No, I don't work for Crocs, just a fan. :)
[d8jhg35] (score 1, diepte 1 OP) Thanks for the tip!
[d8j93is] (score 1, diepte 0) I had this problem in the beginning of the year. After lots of research - I really wanted to find something "cute," I wear Aerosoles (Super Soft Tassel Loafer) with gel inserts and Clarks (Grayson Erica). Hope this helps!
[d8jh4g9] (score 1, diepte 0) Any kind of high top sneaker or boot. Need dat ankle support for standing all day.
[d8jqsln] (score 1, diepte 0) Just to chime in, you may want to consider purchasing some aftermarket insoles. Superfeet or Powerstep are the two most recommended, I personally use Superfeet and althought a bit pricey, are very worth it.  Use their website to determine roughly what style may work best for you and don't be afraid to send them back and try another as they have a 60 day return policy on the card that SHOULD come with the inserts.  I think they do this because once you find the insert that works for you, it'll be hard to not continue using them.
[d8kt0dw] (score 1, diepte 0) Red wing boots helped me a lot. (I guess being able to dress up less formally is an art teacher privilege)

I think any sort of work boots would be fine. (Make sure you get those 15$ insoles from Dicks or other athletic store)

If you are going for something more formal, Cole Haan's Zeroground series are very nice.  They've collaborated with Nike (I think) and made a hybrid of sneakers + formal leather shoe
[d8kt5yd] (score 1, diepte 1 OP) Mmm those are a little masculine for my taste... I'm a pretty girly-girl as far as clothes and shoes go. Definitely going to look into some insoles though.
[d8ktgkr] (score 1, diepte 2) Go get those Sof Sole insoles.  They would change things a lot.

I've been using those since the days I worked at Sam's club.  They were my savior.

They are pretty 'thick', so it might be hard to fit into 'girly-girl' style shoes.
[d8i18s9] (score 0, diepte 0) I like flat shoes or shoes with a very minimal heel. Have you tried barefoot walking or looking into the idea of minimalist shoes? Basically the idea is that we grow up with our feet in unnatural shoes that act like a cast, restricting movement and impeding the growth and strengthening of normal foot structures. 

I switched from very thick, stiff tennis shoes to nike frees with thinner, more flexible soles and after I got used to them I definitely notice an improvement in how my feet feel after being up and on them all day. 

Make sure your toes have plenty of room to spread in your shoes, they don't pinch anywhere and the heel rise is less than half or a quarter of an inch.
[d8i64es] (score 0, diepte 0) I have alot of flats but I never wear them without knee highs. I could imagine without them the friction would be horrendous!

