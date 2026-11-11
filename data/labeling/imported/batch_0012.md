# Label-batch batch_0012

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
Schrijf het resultaat naar `batch_0012.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(5 threads: 1eyxgud, 1emrx2u, 1efe7b8, n3ankq, 10wa1dw).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1eyxgud ===
SUBREDDIT: r/ChronicPain
DATUM: 2024-08-22  SCORE: 3  REACTIES: 5
TITEL: Constant Foot pain NEED HELP
POST (source_id=post):
I need answers people of the internet. Please help me if you can. I have been suffering with constant foot pain in the heel and arch for the past 5 years. I have done it all. The pain can be described as a dull, achy constant pain that lingers no matter what I do. It wakes me up in the middle of the night and makes it hard to fall asleep. I wake up with pain and go to bed with pain. The only time where the pain is less is when I am moving or running. For some reason it's less with constant motion but keep in as soon as I stop or pause and returns in vengeance. 

I have rested

Stretched

Used a night splint

Kept my feet above my heart

Had over 20+ insoles and orthotics both custom and over the counter

Taken 15mg of meloxicam (anti Inflammatory prescription) for 4 months with no change

Taken generic pain killers

Used topical pain creams 

Had an MRI that showed nothing 

Cortisone injections both feet (above and below the PF

A flurry of various footwear (all expensive and high quality including hooks and Keen)

Copper compression bands that I we are daily 

foot massages 

CBD topical creams 

I made another appointment with a different podiatrist but I am looking for a solution and I feel like I have exhausted everything. Initially I thought this was PF but now I am not sure. Maybe it's something that I don't even know. I have looked up Tarsal Tunnel syndrome or other types of foot problems like diabetic foot but I am a healthy not overweight 21 year old suffering in his quality of life. Please help if you can. Taking a minute if you know something that I do not could change my life and free me from this pain. 

I also highly doubt that this is an injury of any sort because I never did sports of any sort and have no recollection of any injury.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ljgwxja] (score 3, diepte 0) I'm sorry to hear about your persistent foot pain. It's clear you've been through a lot trying to find relief. While I can't provide a definitive diagnosis, I can offer some thoughts and suggestions that might be helpful:







Second opinion: It's good that you're seeing another podiatrist. Consider also consulting with an orthopedic specialist who focuses on foot and ankle issues.






Nerve-related conditions: Given that the pain is constant and not always affected by movement, it's worth exploring nerve-related conditions. Tarsal Tunnel Syndrome, which you mentioned, is one possibility. 







Others include:



Small fiber neuropathy




Baxter's nerve entrapment




Peripheral neuropathy




Systemic conditions: Sometimes foot pain can be a symptom of a broader issue. Consider discussing these with your doctor:






Rheumatoid arthritis


Fibromyalgia


Chronic regional pain syndrome (CRPS)






Advanced imaging: If you haven't had one, a weight-bearing CT scan or ultrasound might reveal issues that an MRI missed.






Physical therapy: A skilled physical therapist might be able to identify biomechanical issues or muscle imbalances contributing to your pain.






Alternative treatments: Some people find relief with:


Acupuncture


Dry needling


Low-level laser therapy


Extracorporeal shock wave therapy (ESWT)






Pain management specialist: If the pain persists, a pain management doctor might have additional options, such as nerve blocks or radiofrequency ablation.






Psychological support: Chronic pain can take a toll on mental health. Consider speaking with a therapist who specializes in chronic pain management.






Gait analysis: A detailed gait analysis might reveal subtle issues in how you walk or distribute weight.






Second MRI: If it's been a while since your last MRI, consider getting another one. Sometimes conditions develop or become more apparent over time.












Remember, everyone's situation is unique, and what works for one person may not work for another. Keep advocating for yourself and don't give up hope. There are often solutions, even if they're not immediately apparent.
[ljh2ru8] (score 2, diepte 0) I strongly recommend an orthopedic physician who specializes in foot issues. Good luck and take care.
[ljh9vt8] (score 2, diepte 0) Have you ever had a nerve conduction test (where they use needles to stimulate nerves) ? Because what you’re experiencing sounds like it could be severe neuropathy of the ankle which would show up during a nerve conduction study. Neuropathy can occur even if you aren’t diabetic and can cause almost constant ankle pain while not being visible on a MRI. If it is neuropathy your doctor can prescribe medications such as gabapentin, nortriptyline or devices such as a tens unit that could help. Do you have a normal range of motion? because ankle hypermobility could also cause constant foot pain.
[ljhnc1a] (score 2, diepte 0) If you're autistic, PF is one of if not the most often diagnosed comorbidity. I have both. It does sound like PF.
[ljhavpw] (score 1, diepte 1 OP) I have normal range of motion yes. But never have I had a nerve test of any sort.

=== THREAD 1emrx2u ===
SUBREDDIT: r/ChronicPain
DATUM: 2024-08-08  SCORE: 2  REACTIES: 4
TITEL: Constant Foot Pain
POST (source_id=post):
Constant foot pain

Hey there, just like the title says I have constant foot pain. And it’s ruining my quality of life. I’m a healthy in shape 21 year old man with serious foot problems. Please help if anyone has any ideas on what I could do to not be in pain all day long constantly. 

This has been an ongoing thing for the past 5+ years. 

I wake up in bed. Foot pain.
 
Work a long shift on my feet. Foot pain. 

Not be on my feet for a whole week. Foot pain. 

Often times the constant pain is so bad it wakes me up in bed in the middle of the night. 

The pain originates in the arch. Not so much in the heel. It feel like a constant compressed bruise and the only thing that changes is the pressure level of the compression. It’s always hurts. Like a nagging dull pain. I hate it. 

I have tried everything. 

Custom orthotics from the good feet store

Custom orthotics from my chiropractor

Power step insoles recommended to my by the podiatrist I saw 

20+ kinds of insoles and shoes of various types including Hoka’s and plantar fasciitis specific shoes. 

Pain creams, foot massages that give very limited and short temporary relief

Steroid shots in my feet (cortisone) 

Copper compression bands 

Toe stretchers 

The classic frozen water bottle 

15mg of meloxicam (anti inflammatory medication)

Had a MRI done on both feet and the doctors saw nothing wrong with them physically. 

I’m sure there is more. But you get it. 

Any advice would be greatly appreciated

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lh1akmf] (score 2, diepte 1 OP) Thank you so much for this reply
[lh18c9t] (score 1, diepte 0) I'm so sorry you've been dealing with constant, nagging foot pain for over 5 years now. That must be incredibly frustrating and draining, especially at just 21 years old. Chronic pain can really take a toll on one's quality of life.







Since you've already tried so many different treatment options - from orthotics to medications to alternative therapies - without finding lasting relief, it seems your case may require a more specialized, multidisciplinary approach. Here are a few suggestions:









Seek evaluation from a podiatrist at a university/teaching hospital that has a foot and ankle center. These major medical centers often have podiatrists, physical therapists, and other specialists that work together on complex cases.








Explore getting a second opinion from a different podiatrist, as sometimes a fresh set of eyes can provide new insights.








Ask about being referred to a physiatrist (rehabilitation physician). They specialize in treating musculoskeletal and neurological conditions through a whole-body approach.








Inquire about diagnostic imaging beyond the MRI - things like a bone scan, ultrasound or nerve conduction studies may reveal issues not seen on MRI.








Consider non-invasive options like extracorporeal shockwave therapy, dry needling, or even trying custom 3D-printed orthotics.








Look into chronic pain rehabilitation programs that incorporate pain psychology, biofeedback, occupational therapy, etc.










The key may be finding the right combination of medical, physical, and psychological therapies to better manage your specific foot issues. Don't lose hope - solutions could still be out there. An interdisciplinary team at a specialized center may be able to help get to the root cause. Wishing you relief soon.
[lh1avjb] (score 1, diepte 2) Cool
[lh2gitr] (score 1, diepte 0) Block Therapy. Release the fascia in the foot and calve.  I wish you the best.

=== THREAD 1efe7b8 ===
SUBREDDIT: r/ChronicPain
DATUM: 2024-07-29  SCORE: 1  REACTIES: 3
TITEL: Constant foot pain
POST (source_id=post):
Hey there, just like the title says I have constant foot pain. And it’s ruining my quality of life. I’m a healthy in shape 21 year old man with serious foot problems. Please help if anyone has any ideas on what I could do to not be in pain all day long constantly. 

This has been an ongoing thing for the past 5+ years. 

I wake up in bed. Foot pain.
 
Work a long shift on my feet. Foot pain. 

Not be on my feet for a whole week. Foot pain. 

Often times the constant pain is so bad it wakes me up in bed in the middle of the night. 

The pain originates in the arch. Not so much in the heel. It feel like a constant compressed bruise and the only thing that changes is the pressure level of the compression. It’s always hurts. Like a nagging dull pain. I hate it. 

I have tried everything. 

Custom orthotics from the good feet store

Custom orthotics from my chiropractor

Power step insoles recommended to my by the podiatrist I saw 

20+ kinds of insoles and shoes of various types including Hoka’s and plantar fasciitis specific shoes. 

Pain creams, foot massages that give very limited and short temporary relief

Steroid shots in my feet (cortisone) 

Copper compression bands 

Toe stretchers 

The classic frozen water bottle 

15mg of meloxicam (anti inflammatory medication)

Had a MRI done on both feet and the doctors saw nothing wrong with them physically. 

I’m sure there is more. But you get it. 

Any advice would be greatly appreciated

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lfkrmwa] (score 2, diepte 0) This will get downvoted to oblivion because many here are anti-AI. But I plugged your symptoms into ChatGPT and asked for suggestions to explore. Keep it mind, that these are only suggestions that it pulled up based on limited information from your post. Just like when you research on Google, it's not always going to come up with the exact right answer, but could potentially provide some avenues to look into further:

*  **Nerve Issues**: Sometimes, nerve entrapment or neuropathy can cause persistent foot pain. This might not show up on a standard MRI and may require nerve conduction studies or electromyography (EMG) for diagnosis.
* **Stress Fractures or Microtrauma**: These can be difficult to detect on standard imaging and might require specialized imaging like a bone scan or CT scan.
* **Tendonitis or Tendonopathy**: Inflammation or degeneration of the tendons in your feet, like the posterior tibial tendon or the flexor tendons, can cause chronic pain. This might need an ultrasound or MRI with specific tendon imaging protocols.
* **Muscle Imbalance or Weakness**: Sometimes, issues with muscle strength or imbalance can contribute to chronic foot pain, especially in the arch area.
* **Inflammatory Conditions**: Conditions like rheumatoid arthritis or ankylosing spondylitis can cause inflammation and pain that may affect the feet.
* **Gait Abnormalities**: Even with custom orthotics, subtle gait abnormalities or biomechanical issues might persist and contribute to ongoing pain.
[lfkol2j] (score 1, diepte 0) Could be coming from your sacral nerves.

Mine is different, razor blade cutting sensation on rear of both heals. Like you, I get this regardless of activity and will wake me easily. For me I was diagnosed with adhesive arachnoiditis at s1.

I would see if someone would check out your lumbar but also your sacral areas with a closed MRI w/contrast.

Obviously the other issue could be diabetes, but some labs could tell you if that's the area you should look.
[lfrazlb] (score 1, diepte 0) You are tried everything except strenghtening exercises.




Imo it could be plantar fascitiis or another muscles/tendona related issues.
Anyways for that kind of issues, passive methods are ineffective, medicals, orthotics and massages wont change any in the tissue.
It s capacity to tolerate loads, muscles and tendons tissues strenght and resilience.






Doctors have zero knowledge about these "fitness/sports related issues".
Probably physical therapist can be the right person to go to (most are lazy or dumb).
Anyways usually it s the right path, if the diagnosis is muscles/tendons/joints related.


Now to just write quick examples:
- MOBILITY: "ankle dorsiflexion mobility"..googles it....It s an important mobility, if lack, foot will be overloaded.
- STRENGHTENING: Calf raises (seated = easy. Standing = hard), foot curl and foot yoga are less effective but still useful.


(They wont work with just a trial of 1 day.
They should be put in a smart routine, 2 or 3 times a weeks, for few months)


An idea could be try the Calf raises. Barefoot and on a rolled up towel (hardest, big toe will push a lot).
If it is more painful and foot fascia will be sore, it can be a sign of plantar fascitis/ weak tissues , that require a gradual strenghtening.

=== THREAD n3ankq ===
SUBREDDIT: r/ChronicPain
DATUM: 2021-05-02  SCORE: 0  REACTIES: 2
TITEL: Looking for Ideas/Guidance for Right Side Condition - No Diagnosis After 9 Medical Professionals
POST (source_id=post):
With this post, I'm hoping that I can hear if any of you have had experiences similar to mine and what you did/are doing to cope/treat it. Quite frankly, with this condition that I'm about to describe, I'm getting desperate because nobody knows what's wrong with me and it seems to be getting worse as time goes on.

Essentially, I have very few ideas of other avenues left to explore so I'm hoping you will have some ideas.

I think I'm following all of the rules of the sub, I'm not looking for medical advice, I'm certainly not looking for drugs, and I've consulted many doctors.

# Personal details:
* **Stats:** 21M, 6'5", 147 lbs/66.7 kg, 17.4 BMI, white 
* **Primary Complaint:** Pain on my *entire* right side starting in November 2019 and increasing gradually in intensity since then. Since the beginning, the pain wasn't concentrated on my right side but for the past 4-5 months, it mostly has been. It seems like the pain originates in my right lower back/right hip. I will go into more depth in the "Symptoms" section.
* **Preexisting Medical Conditions:** I was diagnosed with minor scoliosis in 2016. I forget the degrees of the curve but it wasn't (and isn't) major. I've also always had some eczema-like situation going on on the back of my arms but have no idea what it is and it's never been uncomfortable. Other than that, on paper, I'm a healthy kid.
* **Substances:** No medications currently (I have tried various supplements, a steroid, and NSAIDs, however), and no alcohol.


# Symptoms:
* **Pain Description:** I would describe it as muscle pain. It's not a sharp sort of pain but more of an intense muscle ache wherever it occurs.
 * **Locations:** The pain started out being all over my back but in the past 4-5 months, it has moved into nearly all of my right side. It seems to originate in my back (~L2) and is felt distally nearly everywhere on my right side (right side headaches for the past few weeks, neck, jaw, cheek, upper back, lower back, shoulder, arm, hand, fingers, buttock, quad, hamstring, calf, achilles, toes, and foot). I don't feel the pain in all of these places at once but during any given day, I can be pretty sure that I will feel it in all right-side places at some point during that day. Essentially, I'm not in full right side pain at any given moment.
 * **Joints:** I can "click" some of my right joints on command (wrist, hip, ankle, and I used to be able to do the right side of my jaw but not anymore). Very rarely do these joints hurt or feel inflamed.
 * **Triggers:** 
     * Sitting in a chair/car seat without ice/heat causes my right hip and the right side of my back (~L2) to hurt more than normally. Sometimes, seemingly randomly, sitting will also hurt my right foot, right calf, or even right arm/shoulder. 
     * Standing for a while generally causes the area ~L2, my buttock, and sometimes right foot to start. 
     * Laying on my right side hurts my right hip. Laying on my back isn't too bad though.
     * Laying flat on my back, knees to chest hurts my right hip but not left. I think it's the hip flexor but am not sure.
 * **Most Intense Places:** Quite consistently, regardless of posture, the worst places are by far my right hip, right buttock, and right lower back. 
* **Flexibility/mobility:** Nearly perfect. I have very few issues moving and no stiffness. In a lot of cases, moving around actually feels good. The one caveat to this is my right hand which I'll cover in **Physical Asymmetry**.
* **Twitching:** I have a hunch (that could absolutely be wrong) that my muscles (shoulder, arm, back, hip) twitch a little more than the normal person. It happens maybe once or twice a day but I have no idea if this is something noteworthy.
* **Sleep:** Thankfully, most nights I am able to get to sleep without ice. Nearly every morning, like clockwork, I get a few minutes of feeling normal and quite pleasant but as soon as I start moving around or lay in bed awake for a few minutes, the pain comes back. Not sure if this is something noteworthy, either.
* **Physical Asymmetry:** 
  * When I lay on my back, the right side of my lumber spine is noticeably further off of the ground than the left side.
  * Raising only the middle finger in my right hand (think flipping off) is much harder to do than in my left (it's harder to collapse my right pointer than the left). Same with ASL "I love you". In general, hand motions that involve touching fingers with each other and collapsing them are much harder to do (and more painful) in my right hand than left hand. This situation my be due to the fact that I'm left handed, though?
  * When I lay flat on my back, fully relaxed, my right foot lays fully on the ground and my left doesn't lay flat. Not sure if this is normal human being stuff though.

# Imaging/labs:

I've had two MRIs (lumbar spine in November '20 and sacrum/pelvis in April '21). The report for the lumbar spine says I've got "mild bilateral arthropathy" in T12-L3 and moderate in L3-S1. The report from the sacrum/pelvis says nothing useful. These images could be uploaded if that would be helpful. 

[Here](https://imgur.com/a/dp148b7) is one of the X-rays that I had. Doc said that the twisting in my vertebrae could be causing some of the issue and recommended PT which had no effect after ~6 weeks.

[Here](https://imgur.com/a/w11DIAT) is all of the bloodwork that I've had done and from my understanding, there's nothing exciting here. Hopefully that's wrong.

# Timeline:

* **Nov 2019:** Jaw started clicking. In order to open it, I needed to move it to the side a little bit. Not painful or inconvenient, just different and slightly alarming. At this time, lower back started slightly hurting on *both sides* as well.
* **Spring/Summer/Fall 2020:** Pain increased in intensity slightly. I climbed and played tennis a fair amount during this time. Sitting down in a chair to do work started to become painful. Only my back was affected at this point, I hadn't started feeling pain anywhere else in my body. There were a few days where my right foot would hurt slightly but it was very low intensity. 
* **Winter 2020/Spring 2021** This is about when the pain move into being exclusively on mostly my right side, right foot started to hurt much more during this time. Jaw has stopped clicking (but has started to hurt on opening) and hip has started to hurt much more.

I didn't keep the best records during this fiasco so I apologize for the lack of details.

# Attempted solutions (in no particular order):

### Some relief:
* **Ice:** Useful for *temporarily* killing pain in most intense areas.
* **Heat:** Useful for *temporarily* killing pain in most intense areas. I ended up with erythema ab igne (hot water bottle rash) after prolonged use so I know no longer apply heat.
* **Walking:** In Nov '20 - Feb '21, I'd take daily walks (about 2 miles). They are somewhat pleasant. Pain generally subsides while on the walk but comes back afterwards.
* **TENS Unit:** Useful for *temporarily* killing pain in most intense areas.
* **Standing Desk:** Standing is much more bearable than sitting, especially with some comfortable shoes that I purchased but by no means is it comfortable, especially for prolonged periods.

### No relief:
* **Ibuprofen:** Works for the standard headache, muscle strain from sports, etc. but not at all for the pain I'm trying to describe here. I've tried different dose sizes and scheduled doses neither of which have efficacy.
* **Medrol Steroid Pack:** On February 16, 2021, I had my first dose and the following day woke up in the most pain I have had. It was both the most widespread and highest intensity. No change happened after that.
* **Glucosamine Chondroitin:** From what the rheumatologist said, GC is more of a placebo than anything. I gave it multiple multi-month attempts with no positive results.
* **Turmeric/Circumin Supplements:** No positive results from this either.
* **Inversion Table:** 1x/day for a few weeks aggravated my symptoms and actually hurt more than before.
* **Copper Jewelry:** I've been wearing a copper bracelet for a few weeks but to no avail. From what I've seen, copper doesn't have medicinal effects anyways but it's a cheap experiment.
* **Diet Changes:** I tried eating nothing but beef/water/salt for three weeks in December '20 to no avail. For the last few weeks, I've been eating no grains/sugar/processed foods, also to no avail. I suppose the next logical step is to completely remove animals and their byproducts and reintroduce grains?
* **PT:** I've tried multiple programs both on my own and with practitioners, none of which have worked. I have tried Stuart McGill's Big Three (along with most of the other things in *Back Mechanic*), the Egoscue Method, dynamic neuromuscular stabilization (DNS), and miscellaneous exercises with one of my PTs. Nothing has helped.
* **Yoga:** Sometime in Summer '20, I did a session everyday for two weeks with no improvement.
* **Stretching/Rolling:** In Dec/Nov '19 and Jan '20 I tried multiple "stretches for back pain"-type videos from Youtube for a few weeks at a time to no avail. I also tried some foam-rolling.
* **Chiropractic Adjustment:** In Summer '20, I had two sessions with my local chiropractor and received a vague diagnosis of "inflamed facet joints" after him seemingly doing nothing to actually arrive at this diagnosis. I decided to not continue this after feeling no different after each session.
* **New Chairs:** I purchased a Hermann-Miller Aeron in Summer '20 but it actually felt like it made sitting even more painful than normal. I currently have a version of the Steelcase Leap but I can't last longer than 5 minutes in it without ice.
* **Medical Professionals:** I've seen two orthopedic surgeons, two neurosuregons, two PTs, a chiropractor, family doc, and now a rheumatologist all of which has netted no diagnosis. I just got a letter on April 30 from Mayo's neurology department saying that they won't see me. Anybody know if this is a lost cause or if there's still some way to "get in"?
 
### Unattempted solutions:
* **Accupuncture:** This is an expensive service but I will likely explore it soon.
* **Steroid Injection:** I'm not jazzed up about doing one of these with a very vague idea of why we're doing it. Again though, it might be worth exploring as a ~cheap~ experiment.
* **Killing Nerves:** One of the surgeons described this procedure (I forget the jargon he used) but this doesn't seem like a good idea without a clear objective, especially since all of my right side hurts, not just my back. Maybe I'm wrong.
* **Opioids:** Highly addictive, OD possibility, etc. Not touching them.


### Other possibly relevant facts:
* I have seasonal allergies that last from Mid-March - Mid-May (Northern Hemisphere). They're probably due to juniper pollen.
* I live in a very dry climate. We have low precipitation and low humidity. 
* Sometime in 2016, I received a diagnosis for mild scoliosis but I recently saw the diagnosing physician with an updated MRI (that I had in Nov '20) and he didn't think that the scoliosis was related to the pain.
* There hasn't been any particularly traumatic event (physically or psychologically) that has happened that might have caused this ordeal. The closest thing I can recall is a March '20 ski accident but that happened after all of this started (in November '19).
* Seemingly regardless of my diet, for 3+ years, I have had mostly Type 1 stool according to [the Bristol stool scale](https://en.wikipedia.org/wiki/Bristol_stool_scale). No idea if that's related.

Thank you for reading, I'd be very appreciative to hear anything that you might have to say about this. Let me know if there's anything else that might be useful to put in this post.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gwpcjxg] (score 1, diepte 0) No idea as to what is going on but the steroid injection may actually give information.

Where I am, it takes a while to get in for an MRI so sports medicine doctors use steroid injections as a diagnostic tool while waiting.

As the injections can be done in joints and muscles, they pick one and see if it alleviates the pain. If it doesn't they try the other.

This is how we figured out my hip joint is the cause of my muscular pain/weekness.
[gwpepcn] (score 1, diepte 1 OP) Appreciate the comment. From my understanding, injections are pretty riskless. Is that your understanding as well? Is that' the case, it probably is a good call here...

What do you do about your hip joint? Does PT work for you?

=== THREAD 10wa1dw ===
SUBREDDIT: r/ChronicPain
DATUM: 2023-02-07  SCORE: 76  REACTIES: 79
TITEL: “I would kill myself if I was in your shoes.”
POST (source_id=post):
How would you respond to someone who says that to you? How would you respond if you explained your situation and disability/chronic pain to someone and they reply with “Jesus that sounds horrible! I feel so bad for you, I don’t know what I’d do I’m that situation if I was you but honestly if it was me, I would just kill myself in your situation.” I was explaining to someone what my chronic health issues were and it was on a social site and we were just explaining what our disabilities and ailments were. We were trying to get to know each other. This person really said this. They said they couldn’t imagine having my condition but that they would probably off themselves if they had my condition. I won’t go into exact details about everything I have but I do have bad tinnitus and plantar fasciitis but my tinnitus is one of my main problems but it doesn’t help that I been dealing with dry eye lately cause that’s another issue to deal with. I didn’t really know how else to respond other than tell him that I just take it one day at a time and manage the best I can but what they said still made me feel lousy but I tried to hide it. If someone says they would kill themselves if they had your condition, what would you say to them ?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j7m0g7z] (score 95, diepte 0) Even though this is an incredibly insensitive comment, you should take it as a complement to your strength of character that you ARE able to carry on while the commenter would not have the strength to live your life!

Next time tell'em "but I am a lot stronger than you"!!
[j7mjsyo] (score 56, diepte 0) Make direct eye contact and speak firmly and clearly:

"As you're NOT in my situation that's an easy thing for you to say."

Then let the fool stammer and stutter. Silence is powerful; say  nothing more. Just keep the eye contact going. You're doing what his mother should have done decades ago.
[j7mjzbc] (score 22, diepte 1) Ohhh, ***SNAP!!*** This is a GOOD one!
[j7lwo7b] (score 20, diepte 0) If it were a friend trying to empathize but they just kind of had a brain fart and said this insensitive thing to me, I'd probably take a similar approach.

But correct me if I'm wrong, it sounds like this random internet stranger was trying to antagonize you? 

If so I'd be an asshole right back to them.
[j7mlt9p] (score 20, diepte 0) I had a friend that said that to me, key word.. HAD... But I responded with, "Huh guess I should go off myself them" and walked away. Never spoke to them again. Not sure what they thought after 😅
[j7nnmt0] (score 14, diepte 0) I’m sorry you had to experience that :( Had a couple people and even a doctor say this to me before :/ I find that the best way to respond is by flipping the question back on to them ie: “are you telling me to kill myself?” They’ll start back pedaling hard. Some will try to defend themselves but just hit them with “how would you interpret that statement then?” and they’ll shut up real fast
[j7n3y4v] (score 12, diepte 0) when people say shit like this to me, i fake an emotional tailspin immediately and talk about how desperate i am to kill myself, how my entire life is meaningless, and they've just reminded me that my life is nothing but meaningless suffering. i make sure they know that i am in absolute complete agony.

it makes them so fucking uncomfortable, it kills the conversation instantly. then i can walk off feeling smug while they feel extremely awkward and uncomfy. gives me some satisfaction.
[j7nmt4d] (score 12, diepte 0) I don't think that this needs to be taken that seriously. And it especially doesn't need to be taken literally. All this person was saying was that it would be miserable to live with chronic pain (which it is). They were just being a bit hyperbolic about it. 

At least they aren't dismissing or undermining your situation by saying you're exaggerating or that it's all in your head.
[j7nmax3] (score 11, diepte 0) I mean I have that thought myself. What’s the point in living if it’s going to be like this. I can see why someone else might think the same. I’ve heard it before and honestly I’ve always taken it as them acknowledging how hard it is and how much struggle there is not that they want you to die.
[j7no02d] (score 11, diepte 0) This is definitely not the right answer but I would probably be like “Yeah? How?” Asking about the upsides/downsides of that method,  try to get them complicit in figuring out the logistics, then thank them and be like “I’m actually feeling pretty peaceful about this.“
[j7o90zu] (score 11, diepte 0) I've had this conversation and it went like this....

"Why don't you come out with us anymore?" 
Me: Because by the time I make it through my shift, it feels like my entire body is at war with itself. I am physically and mentally fatigued and to be quite honest, there is nothing I want more than to go home, take a hot shower, put on the most comfortable clothes I have and rest. 
"That sounds like so much fun, lol. Everyday, that's your new social life?"
Me: every single day, almost every hour of the day if we're being honest. I am in pain, like level 7/8 out of 10 pain, everyday, all day. Medications don't really help, conservative treatments don't help, so I try to deal with it the best way that I can. 
"I would kill myself if I lived like that. You don't do anything fun. You don't leave your house unless you have to. I'd end it all and be done with it."

Me: yeah, I've thought about it, more than what would get considered a healthy, stable amount. I've also thought about how my daughter would feel when she found my lifeless body or when my cat has to be dropped off at the shelter that I adopted him from. He's a senior cat with health issues, he's not going to he anyone's first choice but he is definitely mine. I don't stay living for myself, I do it for my kid and cat. They need me and I will fight through the pain until I don't have to anymore.
[j7lyhk3] (score 10, diepte 0) Nah bruh this is not it. Friend or stranger saying this to you, no context will make it okay. It’s a really cruel and insensitive thing to say even if it was said with relatively good intentions as an incredibly clumsy effort to empathize. Idk what id say tbh but I’d reconsider associating with said person if they think so lowly of my life that it would not be worth living for them.
[j7nur98] (score 8, diepte 1) Perfect response!
[j7mkamt] (score 8, diepte 0) That's a real asshole-thing to say so honestly feel free to be as rude back as you want to. 

I would probably go more the route of calling them out for saying a shit thing:

"At least I'm capable of knowing not to say rude shit like that"
"Wow, we're done, how about you go home and google why that is not okay to say to someone"
"I'm really glad I have a brain that doesn't come up with cruel stuff like that"
"I think you really need to eduate yourself before taking to any other disabled people in the future because this *waves hand* is not okay" 

And less the you sound weak route because I worked a lot with suicide prevention and awareness and I couldn't say something equating weakness with suicide even to such a rude person. (That is not a judgement on any of the other comments it's just very present and would make me feel bad for saying it for a long time completely failing it's purpose).
[j7n3z74] (score 7, diepte 1) Suicide Hotline Numbers If you or anyone you know are struggling, please, PLEASE reach out for help. You are worthy, you are loved and you will always be able to find assistance.

Argentina: +5402234930430

Australia: 131114

Austria: 017133374

Belgium: 106

Bosnia & Herzegovina: 080 05 03 05

Botswana: 3911270

Brazil: 212339191

Bulgaria: 0035 9249 17 223

Canada: 5147234000 (Montreal); 18662773553 (outside Montreal)

Croatia: 014833888

Denmark: +4570201201

Egypt: 7621602

Finland: 010 195 202

France: 0145394000

Germany: 08001810771

Hong Kong: +852 2382 0000

Hungary: 116123

Iceland: 1717

India: 8888817666

Ireland: +4408457909090

Italy: 800860022

Japan: +810352869090

Mexico: 5255102550

New Zealand: 0508828865

The Netherlands: 113

Norway: +4781533300

Philippines: 028969191

Poland: 5270000

Russia: 0078202577577

Spain: 914590050

South Africa: 0514445691

Sweden: 46317112400

Switzerland: 143

United Kingdom: 08006895652

USA: 18002738255

You are not alone. Please reach out.
*****
I am a bot, and this action was performed automatically.
[j7nggb4] (score 7, diepte 0) I was just discussing this with another friend who has a chronic illness and we thought most people couldn't cope with it but most of them don't admit it
[j7olq37] (score 7, diepte 1) This is the same take I have. Though every time someone tells me "You're so strong, I couldn't handle that" or "I would kill myself if I was in that situation" it feels quite empty to me. If you don't believe in reincarnation then this is the only life you get so you don't have a choice not to handle it if you want a chance at more joyful moments in the future.
[j7nwdb1] (score 7, diepte 0) My mind goes to all of the people worse off than me and still happy that I've seen overcome so much in such a gruelling lifetime. It's what gives me strength cause really, all I have is some nerve pain, throbbin feet and fucked up hands. My aunt walks at an angle with a rod in her back that the doctor at the time had told her could do everything a normal spine could 🫨

No spitefullness or resentment in her and I truthfully couldn't ever have that much steel or strength, and she doesn't even seem to know it cause she's so humble!!!
[j7p7uuc] (score 6, diepte 1) Totally agree! Those of us who endure chronic pain and ailments have nothing to prove except that we don't give up that easily! Most days, I could easily curl into a fetal position somewhere and give up, but I don't because my pain doesn't define me ... it strengthens me!
[j7ndcqn] (score 6, diepte 0) That's beyond messed up. Since I deal with depression, I'd be like well I battle depression everyday and you're not helping.
[j7nah3x] (score 5, diepte 0) I’d probably punch them square in the… face region. Who TF says that to anyone for anything ever…
[j7nqtrf] (score 5, diepte 0) ‘It’s harder than you think’ and then throw my head back and belly laugh!!!

OR get way too excited and ask them to go on.

I like to creep people out though. One of the few things I can do trapped in this miserable prison.

If it bothered me I would either ask them directly, ‘are you saying I should do it?’ Or ‘do you need any ideas, I’ve got tons?’ Or give a disgusting fake cry, because again making rude people uncomfortable is just one of the little comforts in these suffering times.
[j7o2tfd] (score 5, diepte 0) I always get ‘I don’t know how you do it, I couldn’t do it’ well I didn’t get much of a choice really did I, I didn’t wake up one day and go ya know, I wanna be in debilitating pain all the time
[j7pi3hy] (score 5, diepte 0) I like to raise my eyebrows and make it clear that I'm shocked, and say "Wow."
[j7q2vzu] (score 4, diepte 1) Seems a little snarky to me to make it into a personal attack like that.

Maybe something like "You never know how how strong you are until being strong is the only choice you have"?
[j7q6614] (score 4, diepte 1) I couldn't agree more, perfect reply to this insensitive person.
[j7psc72] (score 4, diepte 2) it's guaranteed to make them so fucking uncomfortable that they'll think twice about saying it to someone else. like, it doesn't trigger me genuinely, but if i can freak out the person who said that shit to me, maybe i can keep them from saying it to someone who would actually be triggered into emotional distress by being told they're better off dead.

at the very least it's going to leave a \*very\* lasting impression on them.
[j7q72m2] (score 3, diepte 1) A perfect response. Sheesh, what a thing to say to someone!
[j7o06iv] (score 3, diepte 3) Good human.
[j7nuo5y] (score 3, diepte 1) That’s pretty awesome actually 😂
[j7qvh6n] (score 3, diepte 1) This isba much better take than most of the people commenting here.
[j7nuzu2] (score 3, diepte 0) Beemerba had the best response, so I will just add that I probably would have responded the same way u did while thinking in my head “f*ck you” over and over. What a horrid thing to say to someone.
[j7o0yky] (score 3, diepte 0) I’m not sure if that is better than some saying “ well you don’t look like you’re in pain” or not. At least that person is sympathizing to the pain you experience.
[j7o1eve] (score 3, diepte 0) I mean, they probably lack social skills or are neurodivergent. Not everyone knows how to express empathy without relating. It's a very shitty thing to say, and also they didn't even likely realize it or else they wouldn't have said so.

Like, right now I am thinking about what an asshole I am for thinking that I kind of wish people took my chronic pain seriously enough to think that it was worth ending a life over. I'm not suicidal, but some days it is definitely difficult to think that this will always hurt, and no one can tell, and I have no idea what it is or a real diagnosis, and so when I do say something people act like it's no big deal.
[j7p1isa] (score 3, diepte 0) “Oh wow, I hadn’t considered that! That’s a good idea! Got a rope I could borrow?”
[j7pfm6s] (score 3, diepte 0) My general reply to this is: likewise, if I were as awful as you I'd kill myself.
[j7ppd0a] (score 3, diepte 0) "I've tried." It's the truth and shuts people up quickly.
[j7rbjhj] (score 2, diepte 2) I agree with you. I didn't mean to come across as snarky, but to let OP know they were exhibiting superior strength by being able to cope with their situation.  You REALLY don't know what you would be able to get through until you are there, and the people that make similar comments are full of shit, as these chronic conditions sneak up on you, gradually getting worse.  Not like you get to a fork in the road where one path is horrible suffering 24/7 and the other path-death!
[j7qk365] (score 2, diepte 1) Exactly what I was thinking. "Just shows I'm much stronger than you"
[j7rcesu] (score 2, diepte 2) I guess I took the comment as "If I had it as bad as you"  not as "I already have it much worse than you, so if you added your pain to mine"

Seemed like a stretch to assume the person that made the comment already had it much worse.

My intention was NOT to make anyone feel bad.  It was to uplift the OP.
[j7mdmf1] (score 2, diepte 0) Why do you think it hasn’t been considered? And not yet ruled out?
[j7tpu6p] (score 2, diepte 1) That's a very good response. Thank you for sharing. I'll be keeping note of it, as the same thing has been said to me before!
[j7o05ba] (score 2, diepte 2) Good bot.
[j7nk065] (score 2, diepte 0) I have gotten an incredible thick skin after living this way so long so it would roll off my back .
[j7nk8wp] (score 2, diepte 0) That's such a horrible thing for someone to say. I am so sorry that happened.

If someone said that to me I'd probably just freeze, say okay... weird take... then walk away and cry 🥲 and probably just try and never interact with them again lol
[j7npxes] (score 2, diepte 0) My friend has said this to me a few times when I explain how much pain I'm in and that I'm now really limited in exercise/physical activity. He says it jokingly and I'm sure he doesn't realize how much this all really affects me mentally. It lowkey makes me want to cry but I try to just shrug it off and change the subject. There's not really anything you can say to comments like that.
[j7s1az5] (score 2, diepte 1) Exactly
[j7ra811] (score 2, diepte 1) I could have written this myself. My son is the only reason I fight through this hell everyday. Between spinal issues and suspected Lupus, I sometimes don't want to ever wake up again.
[j7oa6li] (score 2, diepte 0) That comment says I don't know how you do it, you have more strength than I. It's a compliment.
[j7oh00o] (score 2, diepte 0) I honestly think this can sometimes be a person who is in their own way complimenting you on your strength. However, they don’t know how to just say “you’re a strong person”. They are trying to say in a way, “I couldn’t handle that - but WOW- YOU can!”
[j7osrus] (score 2, diepte 0) I am a stronger person than that
[j7p2swe] (score 2, diepte 0) Depends on how I’m feeling/my mood. 

If I’m not pissed off I might say something like “you would think that, but people have a way of learning to adapt. There are many beautiful things I would miss out on if I did that.

If they have gotten on my last nerve, I might say “why wait?”

If it’s a Christian I remind them of Romans 5:3-5
“Not only so, but we also glory in our sufferings, because we know that suffering produces perseverance; perseverance, character; and character, hope. And hope does not put us to shame, because God's love has been poured out into our hearts through the Holy Spirit, who has been given to us.”
[j7pdn6r] (score 2, diepte 0) That I think about it at least once a day, and that when it's bad multiple times a day.  See m' running away, peace at last.
[j7q3e0k] (score 2, diepte 0) Well, let’s be real, a lot of people around here already thought about it. I did. I seriously considered suicide. Not anymore, I swear! But I’ve been very deep in shit before I could manage pain, during the first years of mine. Btw I have phantom pain because an injury in my spine. And I’m a pretty rude person so I probably would answer like that “really? I will mention what you said in my suicide note! How you spell your name and surname, exactly?”
[j7q4m4i] (score 2, diepte 0) Personally, I would probably tell them that what they said was very, very inappropriate and hurtful and not appreciated. I probably also wouldn't continue to be have a relationship with them.
[j7q9uxv] (score 2, diepte 0) “I’m sorry you wouldn’t be strong enough to handle what I go through”
[j7qhw1a] (score 2, diepte 0) I get that a lot. I usually just go "oh, so should I do that right now?"
[j7r402s] (score 2, diepte 0) give them your shoes.
[j7r8kub] (score 2, diepte 0) I’m petty. I’d say you don’t have to wait to have a chronic Illness to carry out that dream. And then immediately block them
[j7rkehq] (score 2, diepte 0) This HAS been said to me. I replied, "I have thought about it. Good thing I'm not a quiter like you."
[j7t5gey] (score 2, diepte 0) I'd say yeah then you better start advocating for pain patients just in case! Because obviously you're not able to deal with it and today (in America) you will get very little to no say in how your pain is adequately managed. Good thing I've got the strength though huh?
[j7qv3zm] (score 1, diepte 1) How do you know the other commenter hasn't dealt with even worse things? Are we really put here thinking that no one in the world could possibly experience anything worse than us? Whatever the conditions explained were, the other person would be experiencing OPs pain ON TOP of their own problems they already have.
[j7rdb5y] (score 1, diepte 3) One of the most narcissistic things you can do in life is walk around thinking that everyone else has it better than you.

If you tell someone something difficult about your life, if they imagine themselves in that position, they're not just going to forget everything that they have to deal with in their own life.

Thinking that its a stretch that someone's life could be worse than yours, just because you have a condition that they don't, is already a problem.
[j7vv5a6] (score 1, diepte 4) Guess I didn't expect to be personally attacked for trying to make someone feel better.  When I read the post, I don't think I am being narcissistic to assume the comment was meant as "If my life was like that" and not as "If I had your problem on top of everything else I am dealing with"
(15 reacties met lagere score weggelaten)

