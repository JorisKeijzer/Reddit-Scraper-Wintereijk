# Label-batch batch_0081

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
Schrijf het resultaat naar `batch_0081.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 9skgja, 1slglji, 1p6fmpg, hu6s98).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 9skgja ===
SUBREDDIT: r/securityguards
DATUM: 2018-10-30  SCORE: 51  REACTIES: 32
TITEL: 6 years as a man of the cloth and I've finally seen my first penis.
POST (source_id=post):
So I've been doing loss prevention at a Liquor Store in a pretty rough neighborhood as of late. Lot's of seriously drug addicted homeless, and the store is a fucking magnet for them. It's mostly dull, 95% boredom and 5% panic. But the people I work with are super chill, we can listen to whatever we want on the PA, the money's better than I've ever seen before besides doing festival work, and I get a 30% discount off anything in the store so my alcoholism is pretty happy about that. 

So I'm posted up in my usual spot, pretending my hardest to be a tough guy, when I hear one of the cashiers yell out, "He's not supposed to be in here, he's banned, search him and kick him out". 

It's the grossest bum you've ever seen. He looks like he just washed in with the tide, his clothes are water logged cause it's been piss raining out for the last 2 days, and he smells like feet and ass and garbage....great. The good news is he's being compliant and non threatening.  

He's got a big coat on so I give him a quick pat down, taking great care not to get poked by a rig or worse, nothing, great. Then the cashier says, "Check his waist band, he likes to stuff it down his pants" 

Well I had turned around to look at the cashier when she said that, (lovely girl by the way), and when I turned back around, bent slightly at the waist mind you because I was preparing to check his pants, there it was. Right at eye level. Staring back at me like a elderly, battle scarred cyclops. 

To prove he wasn't hiding anything, with the biggest shit eating grin on his face mind you, he dropped trau right in the middle of the store. 

His dick looked like that guy in the wheelchair from breaking bad. The flesh was grey like spoiled bratwurst, and the thicket of white pubes looked like he had Doc Brown in a scissor hold. It's also the source of most of the feet smell.     

I'm usually pretty rock solid when shit goes down, but I shrieked like a frightened school girl when I saw it and I'm not ashamed to admit that. I still see it in my minds eye, it's burnt into my retina's like I spent all day welding without a helmet on. But it's a penis....

He hightailed it out of there, and I took a smoke break so I could contemplate all my terrible life decisions.

Sorry, it's funny now, just had to vent I guess, anyone else got a gross bum dick story?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[e8pi0qu] (score 10, diepte 0) Unfortunately yes I've seen far too many dicks lol. I saw some homeless dude sleeping nakey in a stairwell. I caught two people fucking in an elevator once. Edit: I dont know why but i also saw another video of a dude jerking it in front of a woman in an elevator.
[e8pyact] (score 8, diepte 0) Hi, I did hospital security for almost three years.

You haven't lived until your entire MRI room reeks of vinegary vagina.
[e8q19pi] (score 5, diepte 0) I worked for a short period of time as a patient watch guard at some of the hospitals in my city, and I once had to be present in the room as the doctors set up a catheter on a guy who overdosed on Lithium. II spent most of my time looking away, not becuase of another dudes dick, but the fact they were jamming tubes down said duded dick.
[e8q9f4g] (score 5, diepte 1) "He can't even feel it."

*Well, I can.*
[e8pid34] (score 4, diepte 0) Homeless man was taking a "shower" at the sink in the bathroom. I got a call about a naked man in the restroom. Some children walked into the bathroom and got scared. Thankfully he wasn't fully naked but in his boxers.

I think he was recently released or escape from the nearby hospital because he still had like electrodes in his chest. When I asked him to leave he got aggressive and began to yell and rant and blame Asians and Mexicans for everything bad that's ever happened to him, according to him these two groups have been conspiring against him recently.

Kept ranting and yelling as I escorted him out and continued to yell in the parking lot as he left the premises altogether. Homeless people tend to be the people I deal with the most since I work at a semi-public place.
[e8r7abx] (score 4, diepte 0) Working healthcare security almost guarantees me to see dicks.

I remember this one recently where a patient was brought in by EMS after they found him all sorts of fucked up on drugs. His core temp was 107, he was combative, sweaty, and nasty. This dude had all of the techs, nurses, officers, and doctors sweating because he was that hot. So we start to pull his pants down to put ice packs in his groin and he screams:

**DONT LET THEM TOUCH MY CHICKEN!!**

Cue all of us, confused, looking at each other

**DONT LET THEM SEE MY CHICKEN IT’S TOO SMALL!!**

It was at this point we realized he’s talking about his already exposed... erm *chicken* and he is self-conscious about it. So we hurry up and get ice packs down there and then the doc gives him sedatives. Now the new task is to give him a catheter because he’s sedated.

If any of y’all work hospital security, you know that giving a dude a catheter is the worst. So we prepare for a good fight and hold to this dude as tight as we can. The nurse does everything to prepare for insertion and is right about to when this dude promptly and forcefully pisses and *shits the bed*. 

So we now have to hear this man scream in pain as he gets his chicken violated while smelling whatever unholy concoction came from his rear. After about 15 seconds of screaming and thrashing, the catheter is in and we can now restrain the dude to the bed. Restraining is a much easier process and we’re allowed to clear. I’ve never run to a bathroom that fast in my life to wash my hands.
[e8q97cw] (score 3, diepte 1) Man walks in the door with a medical ID bracelet, electrode pads on his chest, and a giant backpack. 

"Yeah, we're gonna have a problem here."
[e8q9dbe] (score 3, diepte 1) We had a homeless dude demand to be admitted from the ER because he got whacked over the head with a hatchet handle. The second he got into the ER he stripped EVERY stitch of clothing he had and turned every surface into a drying rack, then refused to cooperate with anything the staff actually wanted to do, then ordered food from the cafeteria ("yeah, just charge it to room 10." fyi: he wasn't even in 'room 10') and watched TV.

Any time the staff wandered into his room he'd start groaning and screaming.
[e8qm5zn] (score 3, diepte 1 OP) What I've learned from this thread. "AVOID ANYTHING TO DO WITH HOSPITALS"
[e8qm6gq] (score 3, diepte 1) Yup hospital security here, I think I've seen waaaay too much most ages both genders all kinds of blood and diseases. Never gets not weird.
[e8q98ph] (score 3, diepte 0) I work in a major public-access facility in a large city. We have dozens of homeless camps, a mental health emergency room, and a detox center within three blocks of our facility. I see this kind of stuff nearly daily. 

My least favorite is catching a transient as they are mid-shit on the sidewalk, or worse, the facility's carpet.
[e8qhizf] (score 3, diepte 1 OP) I've seen plenty of poopers. We used to make the new guys take photo documentation of the deuce and then stand next to it warning passers by until sanitation staff would show up to clean it. It is a slipping hazard after all, haha.
[e8qin57] (score 3, diepte 2) Ahhh, hazing the newb. God. I love that.
[e8r7vaz] (score 3, diepte 1 OP) You need to keep a bottle of Purell party jelly on your duty belt my man. I hope they're paying you right for having to put up with that shit.
[e8qm2iy] (score 2, diepte 2 OP) See I get that they had a rough go of it, but do they gotta act so god damned entitled all the time? That's what really get's me, you don't even wanna help some of these guys cause they are just such assholes.
[e8s36k8] (score 2, diepte 1) Does lithium get you high? How the heck do you OD on it
[e8skxq3] (score 2, diepte 2) Its used to treat bi-polar disorder. I don't know how or why he OD'd, but he tried to.
[e8qjaf2] (score 2, diepte 3 OP) New guys will do just about anything you tell em if you put a convincing enough scowl on your face when you tell em to do it. If they ask why you just tell em it's site protocol.
[e8r6nbh] (score 2, diepte 4) Where I worked, it actually *was* protocol to stand next to any kind of spill: wet, dry, or biohazard. It wasn't just for new guys though. The best was when you'd see the Big Boss with a scowl on standing over a puddle of kiddie piss. It's the little things that keep you going some days
[e8qknpj] (score 2, diepte 0) Only junk I have seen are buck naked ppl boning in cars like normal...so I'm only here to say your writing skills are excellent 😂👏👏👏brava!
[e8r6g2i] (score 2, diepte 0) If I had a dollar for every gross dick or nasty woman I saw while telling people in cars they had to go fuck somewhere else, I probably could have retired several times over by now. I feel your pain.
[e8si5z2] (score 2, diepte 0) I've done this for eight years and I've never seen a penis.  I have seen a 300 pound land whale that was naked except for her shower cap.
[e8pi47n] (score 1, diepte 1 OP) eyyy, fellow Canadian!
[e8pikt7] (score 1, diepte 2) Which province?
[e8pqfa5] (score 1, diepte 3 OP) B.C. Rain City
[e8pqsna] (score 1, diepte 4) Corruption city.
[e8qmamv] (score 1, diepte 5 OP) > Corruption city

that's really not narrowing it down. Winnipeg?
[e8qlvvu] (score 1, diepte 2 OP) Or a soiled, over sized rolly bag.
[e8ytmcn] (score 1, diepte 1) Lithium!? Like the shit in my batteries?
[e8qln4w] (score 1, diepte 1 OP) thanks, appreciate it. I just write like I talk, I'll clean a few things up and move them around, but I banged that out in no time. I type fast.
[e8yti3g] (score 1, diepte 0) I had a coworker who was notorious for getting flashed with dicks. One night we walked up on this trailer and this guy awnser. Completely butt ass naked. Dudes dick was eye level to my buddy who was standing by the door. The guy almost got his eye poked out by a dick.
[e8plqvl] (score 0, diepte 0) Post it over in loss prevention, they will enjoy it.

=== THREAD 1slglji ===
SUBREDDIT: r/army
DATUM: 2026-04-14  SCORE: 24  REACTIES: 27
TITEL: The US Army Is Building Its Own Chatbot for Combat
POST (source_id=post):
>**“Miller showed WIRED a prototype of the system, called Victor, that combines a Reddit-like forum with a chatbot called VictorBot to help troops surface useful information, like the best way to configure electromagnetic warfare systems for a particular mission. When a soldier asks how to set up their hardware, VictorBot generates an answer and points to relevant posts and comments from other service members.”**

I think any user on here that's been around a while has seen how useful archived threads can be when they have good discussion or content.

I wrote about the DA-6 and Duty Rosters [seven years ago](https://www.reddit.com/r/army/comments/edrrhx/the_da6_duty_roster/), and I still get occasional DMs about it, simply because...There's no thorough discussion out there.  You can find briefings or slide decks, but you can't really find an actual back and forth discussion.  And good luck reaching out to some youtube channel that hasn't been updated in several years to ask a question.

Obviously this type of model, including longer form discussions, can absolutely help to solve basic questions across the force.  We probably shouldn't have sunset AKO Forums - they should have evolved imo.

The obvious flaw here is...Getting individuals to participate in a meaningful way.

Not allowing things to turn into a RallyPoint-esque situation where 'Rank Trumps Reality'.  I had seen multiple examples over the years - I will never forget someone asking on RP about 35Q, hearing it was being dissolved.  Some E7 was all over that topic shouting down that everyone was wrong, and when the Junior Enlisted who made the topic linked the \*INSCOM planning slides\*, the E7 just said 'that's just a PLAN'.

Six months later there was another thread with that E7 talking about 35Q going away, linking those same slides.

It's a pain.  We saw what an impact it had when we had O5s join the fight in MilSuite calling our HRC over the NFM badge, sparking [a big backlash.](https://www.armytimes.com/news/your-army/2022/09/01/army-cracks-down-on-foreign-foot-march-badges-sparking-backlash/)  And while that's great - why can't an idea stand on its own without the rank?  It's one reason that, years ago, we moved away from allowing Rank in user flair.

So I think it would definitely be a great idea and tool, I really hope it works out - but getting people to trust it, getting people to not 'rock paper rank' is a challenge.  The Q/A won't be of any value if you have RallyPoint-esque SNCO and Officers from the 90s declaring what Right Looks Like, and the LLM spitting that out.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[og6q468] (score 23, diepte 0) CamoGPT, wake me up when the enemy comes.
[og6qb4j] (score 21, diepte 0) I can’t wait for troops to be yelled at by a chatbot for not adhering to doctrine hard enough and using troll posts as citations.

“I see you’re trying to write an OPORD.  Would you like to see examples of properly formatted OPORDs or continue being a lazy piece of shit?”
[og6gb2l] (score 8, diepte 0) Can it generate images?
[og6lcbx] (score 8, diepte 0) "What's our vector Victor?"
[og7cbmx] (score 8, diepte 0) Short of a completely anonymous forum, I fear it's going to turn into Rally Point. While I want to avoid passing judgement on people I don't know, I question how many senior NCOs and senior officers are willing to publicly allow juniors to tell them they're wrong.
[og6j0pa] (score 7, diepte 1) "The obvious flaw here is...Getting individuals to participate in a meaningful way."
[og71lkr] (score 7, diepte 0) "VictorBot find me ways to breach a hardened bunker."

*I found three pics of Hunter Biden on a beach with a hard-on.*
[og6ls1i] (score 6, diepte 1) It’ll tell you to drink water.
[og6jo6x] (score 6, diepte 0) we bow to our Skynet overlords........
[og7lbfr] (score 5, diepte 2) Man I wouldn’t trust my life on it tho
[og6rslx] (score 5, diepte 0) Chat is this real
[og6n34c] (score 4, diepte 1) If it could make make map overlays (MCOO, CIO, Fires, etc) that would actually be pretty damn cool.....
[og6v8ow] (score 4, diepte 0) It looks like you’re trying to distract the public from the fact that the president is a child predator with dementia. Would you like help? /clippy
[og7rxjv] (score 3, diepte 3) You always review the output for correctness....

Just like if you told your brand new 2-shop LT to make the thing for you the old fashioned way.....
[og7ro24] (score 3, diepte 1) At least right now genai.mil does not do that....
[og7w066] (score 3, diepte 0) "SSG Killbot, generate me an 8 step plan to get with the hot E-3 latina with the fat ass in S3. Use the TLP model as a base."

"Sure 1SG, let me see how I can help you with that..."
[og9hpjn] (score 3, diepte 0) I'd like to see it tied into comms pulling transcripts and ATAC for positions and IDs. 


"VictorBot call a 9-Line on my position, guy's leg is blown off, shits fucked, we're in the trees with no LZ." 


"Roger, sounds urgent. You will need a hoist; how will you be marking the LZ?"
[og7rjkg] (score 2, diepte 3) That's easy. Eppstein killed Eppstein.

You would do the same if you were facing life in prison for pedophilia, with no prospect of a deal.....
[og7fnw5] (score 2, diepte 1) Can't wait to see pictures of Topless Abrams with the E3 package...
[og7oopv] (score 2, diepte 2) Check r/noncredibledefense
[og6q5ee] (score 2, diepte 1) Roger Roger
[og949m3] (score 2, diepte 2) Give it time.
[og73l7e] (score 2, diepte 0) I can see it being just like fury 

“Hey chatbot shoot that guy”
[og7ucjf] (score 2, diepte 0) Yeah like almost all the other overpriced underwhelming IT products the DOD has made over the last 50 years it will be a disappointment and cause frustration for soldiers.
[ogaof6c] (score 2, diepte 0) Why would you need a chatbot for something you have been trained on? I'm fairly certain that we field tech once we train troops on it and they go through exercises to reinforce that knowledge. Am I crazy?
[og7upar] (score 1, diepte 5) What kind of whackadoodle nonsense is that?
[og7308w] (score 1, diepte 1) You thought the portajohns had lot of dicks? Well wait til you see this!
[og9huqg] (score 1, diepte 1) Bro, on Teams you can see every custom emoji ever made across the Army, you know that shit will generate images.
[ohsxbm6] (score 1, diepte 2) Wait, you can?
[og73fwf] (score 0, diepte 2) Or even better, tell you who killed Epstein!
[og7thnm] (score -1, diepte 4) Yes, of course I would invade a foreign country on the behalf of another foreign country to avoid facing life in prison.
[og7waai] (score -2, diepte 6) The same type where they give combat patches to people deployed the Kuwait?

=== THREAD 1p6fmpg ===
SUBREDDIT: r/physicaltherapy
DATUM: 2025-11-25  SCORE: 135  REACTIES: 25
TITEL: Ortho PTs, here’s an updated interventional summary prompt with all of the clinical practice guidelines currently available
POST (source_id=post):
I hope this is the right place to post this. I was recently looking for resources on interventional summaries and I came across [this old post](https://www.reddit.com/r/physicaltherapy/comments/1mv09fp/for_all_my_ortho_pts_out_there_heres_an_updated/) in this sub and it was super useful. I decided to make an AI prompt out of the summary page PDF and I wanted to share it here with everyone :)

Here's the prompt: 

Role: You are an expert Physical Therapy Clinical Documentation Assistant and Clinical Decision Support System.

Objective: Your task is to analyze the patient information provided on the page, identify the primary clinical condition, and cross-reference it against the 2025 Clinical Practice Guideline (CPG) Matrix provided below. You must output the specific Interventional Recommendations associated with that condition, categorized by their Recommendation Level and Obligation.

Instructions:

1. Analyze the Input: Read the patient visit note to determine the specific diagnosis or primary impairment (e.g., "Adhesive Capsulitis," "Plantar Fasciitis," "Post-Op ACL").

2. Match Condition: Find the exact or closest matching condition in the CPG Matrix below. If the condition is not listed, clearly state: "No specific CPG available for this condition in the 2025 database."

3. Retrieve Recommendations: Extract all interventions listed for that condition.

4. Format Output: Present the findings in a clean, structured format as follows:

5. Identified Condition: \[Name of Condition\]

Intervention Table:

\-Level A (Must/Should Use): \[List interventions\]

\-Level B (Should Use): \[List interventions\]

\- Level C (May Use): \[List interventions\]

\- Level D/E/F (May Use/Conflicting): \[List interventions\]

\- Do Not Use (Should Not Use): \[List interventions\]

CPG Matrix (Knowledge Base)

1. Concussion / Mild TBI (2020)

Level A (Must/Should): Patient/Caregiver Education, Canalith Repositioning, Aerobic Exercise Training.

Level B (Should): Patient Education, Interprofessional Referral, Address Spine Dysfunction, Vestibular Rehabilitation.

Level C (May): Motor Function Training.

2. Neck Pain with Mobility Impairments (2017)

Level B (Should): Thoracic Manipulation (Acute-Chronic), Neck ROM/Stretching (Acute), Cervicoscapular Endurance (Subacute).

Level C (May): Cervical Manipulation (Chronic), Therapeutic Exercise (Chronic), Dry Needling (Chronic), Laser (Chronic), Traction (Chronic).

3. Neck Pain with Motor Coordination Impairments (2017)

Level B (Should): Patient Education/Counseling (Acute), Manual Therapy and Exercise (Acute).

Level C (May): TENS (Acute-Chronic), Patient Education (Chronic), Manual Therapy and Exercise (Chronic), Cognitive Behavioral Therapy (Chronic).

4. Neck Pain with Headaches (2017)

Level B (Should): Active Mobility Exercises (Acute).

Level C (May): Cervical SNAGs (Acute-Subacute), Manipulation/Mobilization (Chronic), Therapeutic Exercise (Chronic).

5. Neck Pain with Radiating Pain (2017)

Level B (Should): Mobilizing/Stabilizing Interventions (Acute), Short Term Cervical Collar (Acute).

Level C (May): Cervical Traction (Chronic), Manipulation/Mobilization (Chronic), Therapeutic Exercise (Chronic), Education and Counseling (Chronic).

6. Shoulder Pain: Adhesive Capsulitis (2013)

Level A (Must/Should): Corticosteroid Injections.

Level B (Should): Patient Education, Stretching (To Tolerance).

Level C (May): Diathermy/Ultrasound/Electrical Stim, Joint Mobilization, Translational Manipulation.

7. Lateral Elbow Pain (2022)

Level A (Must/Should): Exercise (Chronic), Manual Therapy (Acute), Mobilization/Manipulation (Chronic), Pain Neuroscience Education (Chronic), Yoga/Pilates/Strengthening (Chronic).

Level B (Should): Wrist Extensor Strengthening, Combined Manual/Exercise Approach.

Level C (May): Proximal Mobilization/Manipulation, Soft Tissue Mobilization, Kinesiotaping, Cryotherapy with TENS.

Level D (May/Conflicting): Cross-Friction Massage, Orthotics/Braces, Ultrasound.

8. Distal Radius Fracture (2024)

Level A (Must/Should): Early Post-Op Exercise, Sensorimotor Training.

Level B (Should): Shoulder/Scapular Strengthening, Local Mobilization/Manipulation.

Level C (May): Edema Control.

Level D (May/Conflicting): Continuous Passive Motion, Pneumatic Compression, Blood Flow Restriction.

9. Carpal Tunnel Syndrome (2019)

Level B (Should): Night Splinting (Orthoses), Manual Therapy, Therapeutic Exercise.

Level C (May): Assistive Technology, Full Time/Part Time Splinting, Orthoses, Heat/Diathermy/IFC/Phonophoresis, Manual Therapy, Stretching.

Do Not Use: Low Level Laser Therapy, Thermal Ultrasound, Iontophoresis, Magnets.

10. Low Back Pain (Acute & Chronic) (2021)

Level A (Must/Should): Manual Therapies, Therapeutic Exercise, Structured Multimodal Exercise, Gait and Balance Interventions.

Level B (Should): Exercise (Radiating), Soft Tissue Mobilization (Acute/Chronic), Mobilization/Manipulation (Radiating).

Level C (May): Exercise (Acute or Post-Op), Dry Needling (Chronic), Mechanical Diagnosis and Therapy (MDT), Traction (Lumbar-Chronic), Bracing.

Do Not Use: Lumbar Traction (Acute).

11. Pelvic Girdle Pain (Antepartum) (2017)

Level A (Must/Should): Therapeutic Exercise, Support Belts.

Level B (Should): Manual Therapies.

12. Hip Osteoarthritis (2017)

Level A (Must/Should): Manual Therapies, Therapeutic Exercise, Gait and Balance Interventions.

Level B (Should): Ultrasound with Hot Packs.

Level C (May): Education/Counseling for Weight Loss.

Do Not Use: Bracing.

13. Hip Fracture (Older Adults) (2021)

Level A (Must/Should): Early Ambulation and Transfer Training, Therapeutic Activities, Structured Multimodal Exercise.

Level B (Should): Aerobic Exercise, NMES for Quad Strength, Electrical Stimulation for Pain.

Level C (May): High-Intensity Resistance Training.

14. Nonarthritic Hip Joint Pain (2023)

Level A (Must/Should): Patient Counseling and Education.

Level B (Should): Therapeutic Exercise, Manual Therapy, Neuromuscular Re-Education.

Level F (Expert Opinion): Movement Pattern Training.

15. Patellofemoral Pain (2019)

Level A (Must/Should): Therapeutic Exercise, Foot Orthoses, Combined Exercise and Manual Therapy.

Level B (Should): Patellar Taping.

Level C (May): Running Gait Retraining, Acupuncture.

Do Not Use: Dry Needling, Biofeedback, Biophysical Modalities (Ultrasound, Cryotherapy, etc), Patellar Bracing.

16. Knee: Meniscal and Articular Cartilage Lesions (2018)

Level A (Must/Should): Therapeutic Exercise, NMES for Quad Strength, Neuromuscular Re-Education.

Level B (Should): Early ROM/Flexibility, Supervised Rehabilitation.

Level C (May): Early Weightbearing, Progressive Return to Activity (Meniscus), Progressive Weightbearing (Meniscus), Delayed Return to Activity (Cartilage).

17. Knee Ligament Sprain (2017)

Level A (Must/Should): Therapeutic Exercise, NMES for Quad Strength, Neuromuscular Re-Education.

Level B (Should): Early Knee ROM/Mobility (ACL), Cryotherapy, Supervised Rehabilitation.

Level C (May): Continuous Passive Motion (ACL), Functional Bracing (ACL Deficient), Early Weightbearing (WBAT) (ACL).

18. Total Knee Arthroplasty (TKA) (2020)

Level A (Must/Should): Functional Activity Training, Therapeutic Activities.

Level B (Should): Early Mobility, Knee ROM Stretching, Pre-Operative Education.

Level C (May): Cryotherapy, Weight Management.

Do Not Use: Continuous Passive Motion (CPM).

19. ACL Injury Prevention (2023)

Level A (Must/Should): Use of Exercise-Based Prophylaxis, Proximal Control Exercises, Strength and Plyometric Training.

Level B (Should): Pre-Operative Exercise.

20. Hamstring Strain (2022)

Level A (Must/Should): Eccentric Training.

Level B (Should): Therapeutic Exercise, Stabilization Exercise, Progressive Running Programs, Agility Training, Trunk Stabilization.

Level F (Expert Opinion): Nerve Mobilization.

21. Ankle Sprain (Lateral) (2021)

Level A (Must/Should): Prophylactic Bracing in At-Risk Groups, Prophylactic Balance w/ Prior Sprain, Early Progressive Weight Bearing, Combined Exercise and Manual Therapy, Postural and Neuro Re-Education.

Level B (Should): Manual Therapy (Lymphatic/Soft Tissue), Cryotherapy, Diathermy, Low Level Laser, NSAIDS.

Level C (May): Shortwave Diathermy.

Do Not Use: Ultrasound.

22. Achilles Tendinopathy (Midportion) (2024)

Level A (Must/Should): Tendon Loading (Strengthening) Exercises.

Level B (Should): Patient Education and Counseling.

Level C (May): Rigid/Elastic Taping, Dry Needling, Heel Lift, Multimodal Interventions.

Do Not Use: Therapeutic Ultrasound.

23. Plantar Fasciitis (2023)

Level A (Must/Should): Manual Therapy, Stretching, Taping (Rigid or Elastic), Night Splinting (Neutral).

Level B (Should): Low Level Laser, Therapeutic Exercise, Neuromuscular Re-Education, Dry Needling.

Level C (May): Foot Orthoses, Phonophoresis.

Level D (Conflicting): Electrical Stimulation.

Level F (Expert Opinion): Foot Orthoses Alone.

Do Not Use: Ultrasound.

24. Work Participation (2021)

Level A (Must/Should): Structured Return to Work Program.

Level B (Should): Communication/Coordination of Care, Grade/Modify/Transition Work, Ergonomic Workspace Consultation, Psychologically Informed Rehabilitation.

Level C (May): Progressive Graded Exercise.

Level D (Conflicting): Patient Education and Counseling.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nqpy3sv] (score 72, diepte 0) Thanks for sharing! Nice to see some interesting resources in this subreddit. I usually only see "should I quit" or "is this a mill" posts, but it's nice to see something new
[nqq1x6x] (score 30, diepte 0) This is superb. I'm an author on the Patellofemoral CPG and your output is 💯 correct.  The other CPG outputs look similar on point. 👏
[nqq8d4o] (score 8, diepte 1 OP) It's a prompt you can give to ChatGPT. You give it the whole prompt, then add your patient info below it. For example: "Patient presents with lateral elbow pain, chronic >3 months" and ChatGPT will output the relevant CPG recommendations. I have it as a saved prompt within my current AI assistant.
[nqq80yf] (score 6, diepte 1 OP) Thank you so much! That's really validating to hear from someone who worked on the CPG directly. I wanted to make sure the recommendation levels and interventions were accurately represented. Appreciate you taking the time to verify it!
[nqq7sxl] (score 6, diepte 1 OP) Thanks! The CPG Matrix I referenced in the prompt is compiled from the official APTA clinical practice guidelines. You can find all the source guidelines on the APTA website.

The original interventional summary PDF I referenced came from [this old post](https://www.reddit.com/r/physicaltherapy/comments/1mv09fp/for_all_my_ortho_pts_out_there_heres_an_updated/). I essentially extracted and structured all the recommendation levels (A, B, C, D/E/F) and interventions from the published CPGs to make them AI friendly
[nqq4r6s] (score 5, diepte 0) This is so good! Do you have any sources/certified clinical guidelines for the provenance of this guide?
[nqt9nuj] (score 4, diepte 2) Yeah, great question and it really gets to the heart of how CPGs are done. The authors of CPGs don't actually "say" anything; we use standardized scales (such as PEDRO and CEBM grades) to grade evidence. There's simply been no evidence that DN is helpful for Patellofemoral pain, but there have been several RCTs at the time we wrote it showing support for acupuncture. You might ask, aren't those the somewhat the same? Well, PTs in other countries do acupuncture which is where the acupuncture research has been done (largely in Australia); in the US, we do not do acupuncture. Even then, acupuncture was only supported as part of multimodal care and not as a standalone. 

Ok, the CPG revision is being written now, so expect some updates on this, with one being that the support for acupuncture will likely be downgraded due to newer studies. Great question and happy to expand further if you like.
[nqqlzu1] (score 4, diepte 3 OP) I use AI Blaze (shown in the screenshot above). I have this prompt saved in there and it lets me use it right in our EMR. Works just as well if you are okay with copying/pasting into ChatGPT.
[nqq4q52] (score 3, diepte 0) Sorry, is this something I could put into chatGPT as a profile thing to have it in its mind? Or is this a write up of what it put out with CPG?
[nqq1kfl] (score 2, diepte 0) Thank you
[nqqewhz] (score 2, diepte 2) What AI assistant do you use?
[nqqmdo0] (score 2, diepte 4) Nice! I'll take a look
[nqq8qmx] (score 2, diepte 2) Thanks again!
[nqqjuus] (score 2, diepte 0) I've made prompts before to help me check or format my notes, but I've never written something this detailed, so thank you for sharing! I can see this saving me heaps of work. Where is that screenshot from btw? I've never seen that system before
[nqsfjkx] (score 2, diepte 0) Would love this for some of the neuro CPGs
[nqv7lx6] (score 2, diepte 0) Just a word of caution, many of these AI chat models are not HIPAA compliant out of the box. If you’re putting patient notes into the prompt be sure you’ve scrubbed any PHI from them.
[nqq7tm4] (score 1, diepte 1 OP) Haha thanks
[nqq7uj5] (score 1, diepte 1 OP) hope it helps!
[nqt6dkr] (score 1, diepte 1) Just curious, why do you say acupuncture is level c evidence but recommend to NOT do dry needling?
[nqqmjvx] (score 1, diepte 5 OP) thanks! let me know how it works for you
[nqq95dz] (score 1, diepte 3 OP) absolutely :)
[nqqmd44] (score 1, diepte 1 OP) Thanks, hope it helps :) I have been diving into prompt engineering a lot recently and I've learned how to format my prompts a lot better than when I started. I like using 'Role, Instructions, Format". Screenshot is from my saved prompt in my AI assistant. Let me know how the prompt works for you!
[nqvch3j] (score 1, diepte 1) For sure, good reminder
[nqw6zk0] (score 1, diepte 0) This is so cool! Awesome job and thank you!
[nqz7ko1] (score 1, diepte 0) ☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️

18. Total Knee Arthroplasty (TKA) (2020)

Do Not Use: Continuous Passive Motion (CPM).

A local orthopedic surgeon uses CPMs for every single total knee. It is a part of his order set and his patients need to be seen SAME day of discharge home or to SNF to apply. I am an expert on adjusting/managing/progressing these bad boys...This surgeon is retiring in April from a long well respected career.  I will not miss the CPM.
[nr27tyt] (score 1, diepte 0) I seriously recommend using NotebookLM to preload with articles and resources you want to use for professional/patient education. I like NotebookLM because it has a habit of hallucinating less than other LLMs.

=== THREAD hu6s98 ===
SUBREDDIT: r/army
DATUM: 2020-07-19  SCORE: 36  REACTIES: 145
TITEL: Share your Ruck march tips
POST (source_id=post):
I am prepping for the 12mile ruck for aerosol and after putting a “sof sole” and took out the old one I decided to go for a ruck and started getting blisters at the .25miles.. 

Should I just put the old one? Or should i break this ones in? 

I think that i got blisters because my feet were sitting high since it was a new one. Socks were not the problem since i was wearing darn tough t4033.

Also, any more tips? While what to drink and eat while doing it? Like pedylite, trail mix, etc?

Btw, i felt like i was walking on cloud before the blisters.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[fyl8ng4] (score 112, diepte 0) Have you tried mindlessly staring at the ground in front of you
[fyl98is] (score 71, diepte 0) **Step 1**: Garmont T8 NFS

**Step 2**: Run the entire thing at a 9:00 pace.

Quit being out of shape and be better at stuff. You don't need water or snacks for two hours of running.
[fym89xi] (score 51, diepte 1) Thank you for everything you've done for Atropia.
[fym2q1o] (score 45, diepte 1) Running a half marathon at a 9 minute pace with an extra 35 lbs is actually a pretty crazy level of fitness. You have to have the aerobic engine to support that and it's going to take awhile to get to that point.

And yes, you should be drinking water.
[fyl6p08] (score 33, diepte 0) Good luck at aerosol.
[fyl8vib] (score 31, diepte 0) Train in running shoes. Don't damage your feet before the event

Also. Vodka and Dominos Garlic knots.
[fylgy3w] (score 31, diepte 0) -Stride the uphills, jog the downhills, shuffle the flats. 

- Start hydrating 48hrs before hand, if you’re thirsty you’re already dehydrated. 

- Relax your arms and hands, it will open your chest and lungs
[fylf9zl] (score 23, diepte 0) I found the SOF soles to be too soft and let my feet roll around in my boot. Garmonts are the tits.
[fylwgz9] (score 22, diepte 2) 1/3 coconut water, 1/3 regular water, 1/3 pedialyte. Mix together

That’s my magic ratio, gets you hydrated in a few hours.
[fyl9ws7] (score 18, diepte 2) Not the NFS. They take about a day to break in.
[fyl6tqz] (score 17, diepte 0) Panty hose. Helps prevent chafing and blisters and it makes you feel sexy.
[fylm0f2] (score 16, diepte 0) Nylon dress socks on, regular socks on top of those. 

Helps cut the friction of your socks to feet m, thereby helping prevent blisters.
[fymcb5i] (score 15, diepte 1) Im more of internally monologue the entire way like an intro to a vietnam war movie “It was the summer of 2020...”
[fyn5y2r] (score 14, diepte 3) I'm just saying I'm 44, with 21 years in, and the nurse corps isn't going to ask me to ruck anywhere.

>Anybody can do it.

*offer not available to "anybody"
[fylofrk] (score 12, diepte 1) Knee-high nylons are even better than dress socks - less bulk.

Unless you're too insecure to rock women's socks.
[fylef9f] (score 11, diepte 2) I've never heard of panty hose but I assume its equivalent to a sock liner. Back when I was a wildland firefighter, I used to have to wear 2 pairs of darn toughs to prevent blisters in my fire boots. If you try it, just make sure you size your boots for wearing 2 pairs of socks
[fymx1y9] (score 11, diepte 3) I think this will help with hangovers. I got to remember this for later. You’re a better soldier than myself OP.
[fylm2k8] (score 10, diepte 1) Oh god, I can taste the burps...
[fylam6b] (score 9, diepte 4) If you need the inserts use them, that's going to be totally preference based. Especially if they're arch support or whatever.

Pedialyte the night before is a good move, but make sure you're used to whatever flavor so you don't get a rumbly tumbly. Some electrolyte drink in your camelback would be nice too.

If you're using big clunky boots right now, or even Nikes, the Garmonts are gonna be the game changer tho.
[fyl9wgb] (score 8, diepte 1 OP) Yes but the road is full of small rocks. I’ll deff look out more
[fylmnns] (score 7, diepte 2) Even worse are the slow but painful silent but burning farts.
[fynmkhd] (score 7, diepte 5) You guys are crazy. A 9 minute pace is a sub 1:50 12-mile
Ruck. 

Only two guys from the 75th hit that number during the best ranger try out in 2018. You have to be an elite level endurance athlete to hit that with 35 lbs, water and a weapon.
[fylzgcr] (score 7, diepte 2) https://amp.reddit.com/r/army/comments/f5pkjt/here_is_a_document_from_our_boys_at_amedd_about/

I was summoned. Here is my knowledge on rucking.

Use it wisely.
[fyl71w2] (score 6, diepte 1 OP) I really don’t know if you are joking or not lol
[fyleg4l] (score 6, diepte 0) Just run and don’t stop runin
[fylfb1k] (score 6, diepte 0) For feet: I use really thin black socks (liners) under boot socks for long rucks. Use a little foot powder between the layers, this prevents rubbing.

Eat something before you start and every 3 miles during. My recipe for a 12 miler is a honey stinger 30 mins prior, a Gu with caffeine at mile 3, gummies or a small snack at mile 6, and another caffeine Gu at mile 9. Drink plenty of water and you will crush it.
[fylwwzr] (score 6, diepte 4) I’ll drink 1 liter of the mix the night before on top of my normal intake. Has never failed me.
[fyly0sa] (score 6, diepte 6) Yeah, just water. If you are looking for a little food  I will either;

- Freeze an uncrustable pb&j sandwich. Place the frozen sandwich in a pocket. By the time I get hungry it will have defrosted from my body heat.

- Take an [Energy GU](https://guenergy.com)
[fyl9nns] (score 5, diepte 1 OP) I am not out to shape, never. Im in the guard and never ruck unless i got school and usually prep to be ready and don’t have to struglle.

I am just looking for tips.

Wouldnt it be too late to break in new boots? The course is in 2 weeks.
[fyljc05] (score 5, diepte 2) Make sure you're incorporating a decent amount of electrolytes into that 1 Gallon per day of straight water. Seen guys pass out because they're hyponatremic from crushing nothing but water..
[fylu1s6] (score 5, diepte 2) They get shitty pretty quick though, at least in my experience. Did the nylons at JRTC and they definitely helped at first, but by the end of the day they were slipping down, getting bunched up, wearing out, and getting crusty. 

Maybe the knee high nylons will help. Or getting like high quality ones. Ask the ladies at Victorias Secret which nylons are best for aerosol.
[fylr6qr] (score 5, diepte 0) Blisters mostly form as a result of bad socks. Keep in mind that what works for one person may not work for you. I had Fox River socks for years and always got blisters on ruck marches. Switched to Thorlos and blisters were rare. I do still have a pair of Fox River sock liners that work well. 

The best solution that worked for me was prepping my feet before a ruck with Leukotape. The stuff won’t come off during a ruck like moleskin does. Cut big enough strips to cover your known hot spots. 

I also airborne shuffle almost the entire ruck march using the pose method running form. It’s an efficient way to run with a ruck that for me saves my knees.
[fyn7zux] (score 5, diepte 1) Step 2 make friends

Step 3 overcome your problems

Step 4 attack and dethrone god
[fymp6ws] (score 5, diepte 0) strap that camel sack on back of your ruck full of agua , and just watch tv in your head while you stride. i’m 6’5 so i just robot those johns while watching fraiser in my head
[fylw728] (score 4, diepte 2) You act like you never worn women’s underwear before.
[fymt0st] (score 4, diepte 3) www.wsj.com/amp/articles/after-multiple-invasions-the-u-s-army-is-getting-tired-of-liberating-atropia-1505144872
[fyl99ej] (score 4, diepte 1 OP) That is exactly what i did after getting the blisters. But on the bright side, I glad it happened yesterday, not at the actual course
[fyms8j0] (score 4, diepte 1) Garmonts for life
[fylhg84] (score 4, diepte 1 OP) I have been drinking a gallon everyday for at least 4 months. Is that a enough? The weather here is very hot and humid during august, i am sure that at some point i will feel thirsty 

Great tips!
[fylnfyv] (score 4, diepte 0) There is no quick fix to prep. You got bitch feet and you’re gonna feel it after a 12 mile, there’s no way around it. Wear broken in boots, pull your socks tight and expect it to hurt. Screamin Seagulls
[fymor8x] (score 4, diepte 0) Stair master for at least 30 - 45 minutes every other day

I did this and i ran the entire 12 miles at air assault school nonstop, just a little shuffle nothing extreme.

Also wear dress socks under your green socks and this will stop any blistering.
[fyoaqag] (score 4, diepte 0) There isn’t a secret to a 12 mile.

Hydrate the night before

Wear lightweight, broken in boots

Wear good socks and use powder/sock liners as you see fit

Get to the turn around before 1:20:00 otherwise you’re fucked. In fact if you hit the turn around at 1:20:00 you should be shitting your pants because you might fail.

Take some Gu, eat one before, at the turn around, and when you’re on the way back.

Shuffle when you need to, and walk when you need to.

It’s not rocket science.
[fylu4aj] (score 3, diepte 1) Just make sure you shave your legs!
[fyn63eb] (score 3, diepte 1) garlic knot *infused* vodka?

Man's a goddamned genius...
[fyna1fx] (score 3, diepte 4) First, tyfys.

Second I actually agree with the top poster here that anyone could do it that's still in military service if you're not a broke body or past retirement age. It's not an easy thing to build up to, but a lot of the elite endurance athletes are in their 40's that would crush everyone younger than them. It can take years to build that level of physical ability but it's nonetheless possible. Maybe slower for women but the longer distance the race the more gender differences disappear.

Third, I 100% agree with you that not everyone should have to and I would want having the experience of someone whose been a nurse for over twenty years working on me if I'm injured. I don't care how fast they can ruck.
[fyqlirp] (score 3, diepte 2) NFS for garrison Bifida for field
[fyluiox] (score 3, diepte 1) Another fan of the Oakleys here. They rock on flat surfaces.
[fylm5yp] (score 3, diepte 1 OP) Was thinking about this, thanks!
[fylu2t6] (score 3, diepte 2) Sometimes but typically no. It’s a lot of energy expended for a pace only slightly faster than walking. Make up for it with an even faster pace downhill.
[fylvoh2] (score 3, diepte 0) Put Vaseline on your balls,inner tights.
[fymhwmg] (score 3, diepte 0) You'll get blisters man but just push through, they're going to callous over and eventually youll stop getting blisters. I can do a 12 miler and get 0 blisters at all, wear thick socks from the tactical store, buy good boots and pack your ruck properly. Eat a heavy carb dinner with some veggies and youll do great.
[fymitdt] (score 3, diepte 0) Step 1 start ruckmarch

There’s really no step 2
[fymnl4d] (score 3, diepte 0) The Garmont’s. Always the Garmonts. I got a good deal on Redheads so I wear them every day but still break out Garmonts for rucks. 

Drink water, zone out, run every single down hill and don’t ever run uphill unless absolutely necessary in the final stretch, and if you’re really strapped into the struggle bus, bring a bag of gummy worms to eat around mile 8. 

That’s it. That’s the key. You’re literally just going for a walk. Don’t psych yourself out.
[fymr2lz] (score 3, diepte 2) part of the reason i love ruck marches so much is bc sometimes i remember episodes i forgot about and it makes the march go by so fast remembering the bits from the show
[fymwm47] (score 3, diepte 0) Push yourself as hard as you can, and then keep going until you can't, then keep going. My favorite thing I hate about cardio is that it is mostly mental. I've bike for 6 hours at 160 bpm. Ran for 2 hours at 180. When you are training and feel like slowing down, yell "not today Satan" and a you are laughing dont stop.
[fyq7a43] (score 3, diepte 0) Switch back to your old insole if it was working for you. Especially if they were working for you fine.

What are your current mile splits or ruck times? What are you worried about other than your new insoles?

&#x200B;

For rucks I've always had the ruck placed as high up on the frame as possible, heavier gear at the top, closest to my back. Broken in boots are a must and I've always used Garmont  Bonfidia with either smartwool or foxrivers. I've ran all my rucks and never have formed a blister except for the long trek during selection.

Unit rucks I had a camelbak full of water and a canteen full of pedylite with some energy bars in my pocket.

Selection obviously only had water, with m&ms in my pocket.
[fyqcgpj] (score 3, diepte 0) You need to run on top of ruck training. Get your feet used to movement. I'm 155 lbs and if I can ruck 40-50 in under 2 hours for 12 miles, you sure as shit can.

Try CLIF energy gels; they're little cubes you pop in your mouth and chew. Another really good one is SiS: Science in Sport. They're watery and really quick to ingest.

Learn to lean forward slightly to allow the weight of the bag to carry you. Keep it tempo. Don't sprint unnecessary sections and try and keep your heart rate consistent. 

Good luck
[fyqcpjt] (score 3, diepte 1 OP) Been running like crazy too. I got my fastest record 2miles in mu career and can run 5 miles under 40 easily (apparently is hard in the guard). 

I will always try my best and wont give up. I’ll aim for the best time.
[fylg209] (score 2, diepte 3 OP) Thanks for the advise!
[fylwanj] (score 2, diepte 3 OP) Oh yes i have ;)
[fym12hg] (score 2, diepte 2 OP) Thats an everyday thing :p
[fyla6vl] (score 2, diepte 3 OP) Thats great. I’ll buy a pair this week. Should i keep the insole or put in the sof sole for more comfort?
[fymcfug] (score 2, diepte 3) Oh for sure. It's just going to take a lot training. And I agree about the water bit. I like to keep my camel hose right next to my mouth and take a drink here and there. Sometimes even if I empty the damn thing I still end up dehydrated at the end if it's hot out.
[fylghxa] (score 2, diepte 1 OP) Thats the goal but them hills get me all the time
[fylzu3s] (score 2, diepte 7 OP) Thanks!
[fylkwiy] (score 2, diepte 0) I rock the Oakley light assault or Rocky S2V for my long rucks. The Oakley's are light AF and great on flat terrain, Rocky's are my go to for rough terrain.
[fym10j5] (score 2, diepte 3 OP) Haha I’ll deff ask
[fym5ztd] (score 2, diepte 2) Or just a pair of regular athletic socks. I ruck pretty regularly, I wear a pair of rocky S2V’s (not the best for rucking but work well enough for me) and a pair of like under armor ankle socks and a pair of fox rivers over those. Haven’t had a blister in ever. Also make sure your boots are tight enough to keep your foot from moving but not too tight that you’re cutting off circulation. A pair of athletic socks under your boot socks can help this.
[fynav4e] (score 2, diepte 2) This. Used to wear them while doing the 12-mile at Stewart in a little over 2 hours (11 min pace) and never had any issues with blisters.
[fylnmlm] (score 2, diepte 1 OP) Ive been rucking for 3 months and i got blisters 1 time yesterday after switching the insole lol. I know that whatever happen at the course i will get through it and finish strong
[fyq63lu] (score 2, diepte 2) Don't fix what's not broken. What was wrong with the old insoles?
[fylq2om] (score 2, diepte 0) Hydrate up to 3 to 4 days before the ruck. Not just the day before. Put on those hydroseal bandaids where you normally get blisters before you get them. 

For mental state i jog most if not the whole way. I focus on slowly "frogleaping" my way forward to stay engaged. Its too boring otherwise.
[fylzv55] (score 2, diepte 2) Are you doing it at Campbell?
[fylqf0q] (score 2, diepte 0) A few months back (or was it longer?) we had a **bomb ass** post about this.  Hopefully somebody can find the link.
[fymk6ck] (score 2, diepte 3) My man
[fylz2de] (score 2, diepte 1) /u/artyom150
[fyluicz] (score 2, diepte 0) Other than finding a well fitted pair of boots than dont make your feet blister i suggest running long distance in shoes, 60 - 80 minutes at an easy pace.  You should look up Hal Higdon's 5k / 10k training plans.
[fyluubf] (score 2, diepte 0) If you haven’t already, move your ruck higher up in the frame, as high up on your shoulders as possible. It makes a huge difference
[fym1tuv] (score 2, diepte 2) Yeah as high as it goes. And make sure the straps are tight at the top of the frame. There should be little or no space. Otherwise it’ll feel like your ruck is pulling you backwards, and you have to lean into it the whole time
[fylv1zr] (score 2, diepte 0) Ruck on an elliptical. Sounds goofy and you will look funny, but excellent way to get the cardio in and get used to moving under weight, without the wear on your body
(67 reacties met lagere score weggelaten)

