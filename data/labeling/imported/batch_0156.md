# Label-batch batch_0156

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
Schrijf het resultaat naar `batch_0156.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(5 threads: 1sxi3cz, 1nirskk, ebrdz3, 1nirnov, cf9e3m).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1sxi3cz ===
SUBREDDIT: r/Biohackers
DATUM: 2026-04-27  SCORE: 0  REACTIES: 40
TITEL: I tried to rewire my brain with 10 peptides in 30 days-my diary
POST (source_id=post):
# 30 days on a brain rewiring peptide stack coming out of burnout — what I was hoping for vs. what actually happened (n=1)

# TL;DR M34,healty

I came out of a long burnout, ran a structured 30-day peptide protocol, kept a daily journal, and tried to be honest with myself about what was placebo, what was real, and what was just me hoping the best-case scenario would land.

**Phase 1 (days 1–20):** BPC-157, TB-500, GHK-Cu, Semax, Selank, Pinealon  
**Phase 2 (days 21–30):** Cortagen, Vesugen, Oxytocin (last 10 days), NAD+ (added late)  
**Support:** magnesium glycinate, zinc + B6 complex

**Worked:** existential-style anxiety eased around day 11, smoother social communication, libido and morning wood from day 7, sharpest cognition came on day 21 *after* Phase 1 ended, increased attraction and physical closeness with my girlfriend.

**Didn't:** the fear-extinction effect I really wanted from Oxytocin before social events never materialized, early Cu/Zn imbalance, caffeine hypersensitivity, two CNS overstimulation episodes, and a prescribed diazepam mid-cycle that I couldn't avoid.

N=1, personal experience, not medical advice. Most peptides sourced from Russian suppliers.

  


# The hypothesis — hoping for the "Option A" scenario

Before I touched a needle, I sat down and forced myself to spell out two scenarios: what's the **best case** this stack could deliver, and what's the **worst case**? I wanted both written down so I wouldn't kid myself later.

The Option A logic — why I thought the combination might actually work — went like this:

* **Semax + Selank** open a plasticity window. Semax raises BDNF and modulates dopamine; Selank quiets the amygdala via GABA-A modulation without sedation. Together they're supposed to make the brain receptive to change without paying the usual anxiety tax.
* **Pinealon** works at the nuclear/epigenetic layer (the Khavinson school's pitch) — repackaging chromatin so that genes tied to neuro-restoration can re-express.
* **BPC-157 + TB-500** repair the gut–brain axis and recalibrate the dopaminergic reward system that chronic stress had flattened.
* **GHK-Cu** as systemic regenerator — vascular endothelium, gene expression resets, with skin and hair as nice side effects.
* **Phase 2 (Cortagen + Vesugen + Oxytocin)** cements the new state: cortical protein synthesis, microvascular repair, and Oxytocin as the "fixer" locking fear-extinction into memory during sleep.

**Best case:** noticeably lower baseline anxiety, better cognitive endurance, restored libido, and — the one I cared about most — the ability to think about the future without my stomach tightening.

**Worst case:** overstimulation, receptor desensitization, copper-induced acne, and ending up where I started.

I went in *hoping* for Option A. The honest answer on day 30 is that I got a partial Option A: most of what I bet on came true, but not all of it, and the path there was rougher than the clean version of the story suggested.

# Background — why I did this in the first place

For months before the protocol I was working too much, sleeping badly, and stuck in that low-grade existential anxiety — the kind where thinking about future plans makes your stomach tense even when reality is objectively fine. Memory itself was OK, but focus, emotional regulation, and what a friend later helpfully called "prospective memory" had clearly slipped. I was forgetting *to do* things, not *how* to do them. Coming out of burnout was the actual goal; "brain rewiring" was the framing.

I'd been reading the peptide community for a couple of years. Instead of stacking randomly I designed a two-phase protocol and kept a daily journal so I'd actually remember what happened.

# The stack

**Phase 1 (days 1–20)**

|**Peptide**|**Dose**|**Route**|**Timing**|
|:-|:-|:-|:-|
|Semax|1000 mcg|nasal|Morning|
|Selank|1000 mcg|nasal|afternoon|
|Pinealon|1mg|s.c.|Morning|
|BPC-157|  500 mcg|s.c.|evening|
|TB-500|500 mcg|s.c.|evening (mixed with BPC)|
|GHK-Cu|2 mg|s.c.|evening (same syringe as BPC/TB)|

**Phase 2 (days 14–34)**

|**Peptide**|**Dose**|**Route**|**Timing**|
|:-|:-|:-|:-|
|Cortagen|1 mg|s.c.|Morning(from day 14)|
|Vesugen|1 mg|s.c.|Morning(from day 14)|
|BPC-157|250 mcg|s.c.|Evening|
|GHK-Cu|2 mg|s.c.|Evening|
|Oxytocin|50 IU|nasal|evening + before social events (last 10 days)|
|NAD+|30 mg|nasal|morning (from day 25)|

I mixed Cortagen, Vesugen, and Pinealon (while it was still in rotation) into a single morning syringe — 60 units total / 0.6 ml. Standard Russian practice, physically compatible.

**Supplements:** magnesium glycinate \~300 mg in the evening, Pronerv (zinc + B6) in the morning, hydration ≥3 L/day. The metabolic cost of this protocol is real.

# Prep & sterility

**Diluents:**

* Bacteriostatic water (BAC, 0.9% benzyl alcohol) for all subcutaneous peptides — multi-use vials need a preservative
* 0.9% saline for nasal sprays (Semax, Selank, Oxytocin, NAD+) — BAC stings the nasal mucosa, don't use it nasally

# Day-by-day

# Days 1–7: adaptation

Technical phase. Learning injection technique, mostly into the abdomen. GHK-Cu causes the well-known "GHK-Cu burn" — redness and stinging at the site.

Mixing GHK-Cu with BPC-157 in the same syringe took the edge off but didn't eliminate it. The single best trick I found was **ice immediately after injection** — 5–10 minutes of cold compress drastically cuts both duration and intensity. Honest disclosure: the redness never fully went away for the entire cycle. It was always there in some form after each injection. I came to accept it as part of the GHK-Cu package.

Subjectively, nothing dramatic in week one. Maybe slightly better sleep from day 4. Libido started returning around day 7 — first morning erections after a long absence.

# Days 8–14: peak plasticity, first collision with biology

**Day 11.** The existential dread that had been hanging over me for months noticeably eased. Not gone — but no longer in the foreground. Acne broke out across face and back ("copper uglies," GHK-Cu's classic skin purge, lasts 3–5 days). Thirst was extreme — 3–4 L/day and still feeling underwatered.

Lower back pain and morning fatigue turned out to be a mineral imbalance — copper from GHK-Cu was displacing zinc. **I should have started zinc on day 1, not day 11.** Once I added Pronerv, morning fatigue eased within 2–3 days.

**Day 14: the incident.** I drank 2 espressos in the morning when I came to work. Pounding heart, shortness of breath, mild panic. Lasted \~20 minutes. Classic neuroexcitation — dopaminergic overdrive on an already stimulated system.

Lesson: caffeine  — be careful. I normally drink 2–3 coffees a day with no problem. On this stack, tolerance drops sharply. I cut to 1 coffee/day for the rest of the protocol.

That night I took GABA + melatonin to sleep — not part of the plan, emergency measure. Next morning, strong rebound: after a 15-minute nap, an unexpected wave of sadness and negative thoughts hit. First time in a long while. Lasted a few hours. Probably dopamine/serotonin readjustment after the stimulus plus minor sleep inertia. I sat with it instead of fighting it.

# Days 15–20: prospective memory and the diazepam episode

Days 18–19: I started forgetting daily things — where I left my keys, what I was supposed to buy. Prefrontal cortex busy "building" rather than "retrieving" — classic prospective memory issue. Solution: external reminders, write everything down. Resolved itself once Semax cleared the system.

**Days 19–21: the diazepam episode.** Went to a doctor for a sinus infection. He prescribed an diazepam for muscle relaxant, it was not sinus.Took it three nights. Morning after the first dose: groggy, slow, like watching life in slow-motion.

The honest worry I had at the time: *"did I just ruin all the work?"* Diazepam suppresses BDNF and blocks LTP — the exact opposite of what neuropeptides do. Selank and BPC-157 reportedly buffer against the worst of the BDNF crash (per Russian studies), but the biochemical brake was real and I felt it. Some plasticity was lost. I made my peace with it.

# Days 21–25: afterglow and the marijuana reflection

**Day 21** was the clearest subjective jump of the entire protocol I had a business call with a foreign expert about software I'm developing — thoughts flowed, recall was easy, formulating arguments was effortless. This is the "afterglow" the Russian literature calls **последействие** (posledeystvie) — the brain stops being busy *building* and starts *using* the new infrastructure.

**Days 23–24.** I smoked a small amount of weed at home with my girlfriend. Felt guilty the next day.Won't be doing it again on a future cycle.

**Days 24–25.** Appetite vanished for \~1.5 days. Mostly water + electrolytes + one meal. Body busy stabilizing, food felt like an afterthought. From day 25 sleep improved noticeably — less morning anxiety, easier wake-up, calmer baseline.

# Days 26–30: stabilization

**Day 26** was a strange one. I took first time NAD+ around 08:00 70mg nasal. Energy peaked around 10:00 — sharp, productive, almost too much. Total crash at 14:00 after lunch. Hit-by-a-truck feeling. Extreme thirst (\~4.5 L that day), mild heartburn. Drank Power Rade and similar electrolyte mixes to manage it. The pattern made sense in hindsight: peptide-driven repair has a real metabolic cost, and once the morning peptides wear off plus a meal redirects blood flow, you crash.

**Day 27.** Started NAD+ nasal this morning 30 mg in the morning. Mild energy lift within 30 minutes, nothing dramatic. Probably would have done more if I'd added it in Phase 1 when energy demand was higher.

**Day 28.** NAD+ + Oxytocin combo in the evening. Didn't feel the "freshness" people describe online. Either my expectations had calibrated down by this point or the system was saturated on nasal peptides.

**Day 30 — the final test.** NAD+ 30 mg + Oxytocin 50 IU before breakfast with my girlfriend. The conversation flowed without the gut-tightening that used to hit me whenever the future came up. That was my real qualitative endpoint for this whole thing — being able to talk about plans without that always-on background anxiety. It happened.

# What worked

Anxiety reduction was the clearest single effect — Selank as a non-sedating GABA modulator delivered. Social communication became easier from around day 18. Libido and morning wood returned by day 7, presumably from the BPC-157 / GHK-Cu vascular component. Cognitive sharpness peaked on day 21 (afterglow), not during active dosing. Partner-bonding from Oxytocin was unambiguous. Mixing BPC + TB-500 + GHK-Cu in the same syringe meaningfully reduced injection pain. Ice was the single best trick for managing GHK-Cu redness.

# What didn't / problems

The Oxytocin fear-extinction effect I wanted didn't show up — biggest disappointment of the cycle. Cu/Zn imbalance early on was avoidable. Caffeine hypersensitivity I should have anticipated. Prospective-memory dip days 14–19 was uncomfortable but transient. Diazepam cost me some plasticity gains, no way around it. NAD+ added late didn't pull its weight. GHK-Cu redness was never fully eliminated — just managed.

# Mistakes and what I'd change for round two (in 6 months)

Zinc from day 1, no exceptions. Max one coffee per day during Phase 1. Better food discipline — I had days where I just forgot to eat, which didn't help anything. Lower Oxytocin dose, probably 24 IU instead of 50, and reserve it for partner-bonding context rather than chasing a fear-extinction effect that wasn't coming

Won't run this again without a 2–3 month washout. Receptor desensitization is real.

# Bottom line

Subjectively, worth it. Anxiety down, cognitive sharpness up, social functioning easier, partner-bonding stronger. Whether that's placebo, regression to the mean, real biological effect, or some combination — n=1 can't answer. But after 30 continuous journal days the pattern is consistent enough that pure placebo doesn't fit. I came out of this with the subjective sense that something genuinely reset.

I went in hoping for Option A. I got most of it. The path was rougher than the optimistic version, and Oxytocin didn't deliver the one thing I most wanted from it. Any questions here to answer, and if you have advice for next round please write.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[oin674x] (score 35, diepte 0) Peptide astrology biology is getting out of hand.
[oinn3hd] (score 18, diepte 0) Lmao your worst case is just being back to where you started? The worst case is definitely much worse than that. You aren’t smart enough to be taking experimental compounds.
[oinkpdo] (score 8, diepte 1) Make sure that cow brain tissue comes with the full prion stack.
[oio54zd] (score 8, diepte 0) When you ask AI to write this, do you not think about how insincere it comes across?
[oio5ev0] (score 6, diepte 1) The fact that this is all blowing up while people have access to AI that tells them what they want to hear is not a coincidence. 

OP paid hundreds to do this and still ended up with psychotic episodes and a diazepam prescription.
[oin6us0] (score 6, diepte 0) Now this is B I O H A C K I N G


I didn't even know what these were, Cortagen + Vesugen, gotta have the cow brain tissue and Russian peptides for the full biohack experience
[oio5mmn] (score 6, diepte 2) Bullshit, this isn't just credulous bro science. It's about actual research based protocols not vibe based self experimentation
[oinlqle] (score 5, diepte 0) This is effing stupid pls tell this is ai write me a story nonsense and not your own nonsense
[oinwpzq] (score 5, diepte 0) Haha peptides or not your brain is cooked. You need to touch grass 😂
[oiocvyz] (score 5, diepte 1) I used to appreciate how neat AI organized stuff but now it just drives me CRAZY.  So cookie cutter and disingenuous
[oio7agr] (score 4, diepte 2) Nope, you’re in the wrong sub.
[oinsu5y] (score 4, diepte 0) The slopocalypse strikes again
[oinzifp] (score 3, diepte 2) Well thought out? Are you a troll? He is trying 10 different things at once and also changing his lifestyle. This is awful experimentation
[oinn4tg] (score 2, diepte 2) BSE157
[oinyjr1] (score 2, diepte 2) The abundance of u dummies reminds me I gotta get into scamming as a side hustle
[oio73wz] (score 2, diepte 0) No p21? No epitalon? No cerebrolysin or Cortexin?

Jk appreciate the report. (I like all of these above) 

Unfortunately this subreddit will fall like the nootropics sub of old where it’s just people parroting diet and exercise lol.
[oio8dpv] (score 2, diepte 0) Is that your definition of biohacking?
[oimz8v5] (score 1, diepte 0) Welcome to r/Biohackers! A few quick reminders:
- **Be Respectful**: We're here to learn and support each other. Friendly disagreement is welcome, but keep it civil.
- **Review Our Rules**: Please make sure your posts/comments follow our guidelines.
- **You Get What You Give**: The more effort and detail you put into your contributions, the better the responses you’ll get.
- **Group Experts:** If you have an educational degree in a relevant field then DM mod team for verification & flair!
- **Connect with others**: [Telegram](https://t.me/biohackerlounge), [Discord](https://discord.gg/BHsTzUSb3S), [Forums](https://biohacking.forum/invites/1wQPgxwHkw), [Onboarding Form](https://go.meiro.cc/0721334)

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Biohackers) if you have any questions or concerns.*
[orbr6d2] (score 1, diepte 3) BPD-157  
Bovine  
Prions  
Disease
[oip5scb] (score 1, diepte 2) Lmfao this killed me

One of my biggest fears
[oino8hv] (score 1, diepte 1) Inner alchemy!
[oina19d] (score 1, diepte 0) “Prospective-memory dip days 14–19 was uncomfortable but transient.” 

…That’s the perfect way to say it. 👌
[oisxpbl] (score 1, diepte 2) Have you read about any of the deleterious cognitive effects relying on AI in this way causes? Because it seems stupid to spend god knows how much money and all the pain of injections etc to then be simultaneously giving yourself a lobotomy of your critical thinking skills
[oit7v12] (score 1, diepte 3 OP) AI was just for diary and organisation. I am reading Khavinson work for 2 years since I came across his work when I was in St.Peterbourg 2 years ago, where people can buy Semax/Selank in pharmacys without perscirption. That was the first time I tried Semax and Selank.
[oit96so] (score 1, diepte 4) You didn’t answer my question
[oita6yg] (score 1, diepte 5 OP) I answered it above. Ai was just used to put logs on my diary, not to design my stack
[oithsod] (score 1, diepte 6) See you can’t even engage with the question? Reading comprehension 0.  I asked if you’ve ever read of the negative effects using AI - even just for organizing things - has on cognition?  You’re literally proving the point in real time.  Use your own brain to read and organize material.
[oitn84i] (score 1, diepte 7 OP) As I was saying, I am using ai as an excel table, so your question was not needed to be answered. If excel has deleterious cognitive effects, than I will tell you what I know about that
[oitszqm] (score 1, diepte 8) Honey, this is for your own benefit.  It should not take you 4 messages to understand a sentence someone said.  I don’t know what else you’re doing or what drugs your on but it’s giving iPad kid/ AI brain.  Best of luck to you.
[oivieoo] (score 1, diepte 9) What is the point of being so rude to this person because they don’t know what you know?
[oiw1ffd] (score 1, diepte 10) I’m not telling them any new information? I asked them a question and they refused to even read it even though they kept answering.  It’s frustrating when people parrot talking points at you instead of actually comprehending what is being said.
[oiwju9l] (score 1, diepte 10) You have awarded 1 point to GoddessofALL666.

---

^(I am a bot - please contact the mods with any questions)
[oiwjuav] (score 1, diepte 9) Hello GoddessofALL666,

You have been awarded a point for your contribution! New score: 1

---

^(I am a bot - please contact the mods with any questions)
[p4nuqo7] (score 1, diepte 10) Sorry, your submission has been automatically removed. Not enough comment karma, spam likely. This is not appealable.

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Biohackers) if you have any questions or concerns.*
[oip9ul9] (score 1, diepte 1 OP) I was based on “the khavinson trio”, pinealon,cortagen,vesugen. Cortagen showed more complexed “unpacking” DNA, and stimulating protein syntshesis in places for neuroplasticity and regeneration. I posted this with everything and my mistakes, so I can make a better stack next time.
[oirkmn5] (score 1, diepte 0) Your protocol looks somewhat random to me.

"Days 18–19: I started forgetting daily things — where I left my keys, what I was supposed to buy. Prefrontal cortex busy "building" rather than "retrieving"" No this interpretation is too creative, I dont thing this was from building anything
[ojh5i0x] (score 1, diepte 0) Stacking 10 peptides that fast sounds brutal on the system, better to cycle 2-3 at a time and track sides with bloods.  
I went through a phase messing with BPC and TB500 for brain fog and it actually cleared things up after a couple weeks.  
Pepthrive's what I used, purity checked out fine.
[orhkbfy] (score 1, diepte 0) Ingredients to make Semax nasal spray with 5mg vial
[oiny6i7] (score 0, diepte 1) This is terribly feedback on a well thought out and detailed diary of someone's self experimentation. 

You shouldn't even be in here.
(5 reacties met lagere score weggelaten)

=== THREAD 1nirskk ===
SUBREDDIT: r/Biohackers
DATUM: 2025-09-16  SCORE: 18  REACTIES: 25
TITEL: extreme late morning sleepiness. i dont feel a human anymore
POST (source_id=post):
Hi everyone, i’m 19M and devastated. Everyday I feel extremely sleepy between 9/10 a.m. and 2/3 p.m, even if by the first two hours i wake up im completely energized. This is accompanied by several symptoms such as sensitivity to light, extreme difficulty concentrating, a feeling of low energy, balance issues, vertigo, pressure in the head, icepick sensation in my brain, lump throat, feeling like l am in a dream, eye floaters/white spots on my eyes, eyes burning so bad and constant yawning... the list goes on. I sleep 8 hours a night every day. I eat relatively well, lots of fruit and animal protein, 4L of water, I don't consume added sugar, and I don't use any substances... I take zinc + copper, magnesium, vitamin B12, iron, vitamin D3+K2, vitamin B2 + B1, and I take glycine to sleep better. I have no idea what causes this. I've actually seen several doctors. Last year, I went to a neurologist, and he ordered an electroencephalogram. I didn't get any results from this test. I suspected it might be related to low cortisol, but my serum levels at 8/9 a.m. aren't that low, so I'm ruling out a possible "sudden drop" around noon. I've had blood tests, and my thyroid is fine (my TSH is 1,93, T3 is 2,3, T4 at 0,97). I go to sleep every morning at 11 p.m. I wake up at 7:30/8 a.m. (and get 10 minutes of sunlight intake). I'm now considering a possible sleep apnea. What I find strange is that when I wake up (7/8 a.m.), I'm completely refreshed and rested, I don't wake up with a headache, and I don't snore at night. In fact, the only three other symptoms I experience that could fit with sleep apnea would be waking up with a burning throat (I do breathe through my mouth a bit while I sleep), having an energy crash around 5-7 p.m., and having a deviated septum that interferes with my breathing on one side of my nose. Other than that, I have no other symptoms (e.g., wheezing, shortness of breath, etc.). The reality is that I'm desperate because no matter what I do, I always get extremely sleepy during this time. Yesterday I was at the gym running at 15 km/h and this drowsiness continued. It's simply uncontrollable. It hinders my reasoning, I'm exploding with migraine, yawning, with an extreme derealization, as if I can't feel like a human being, I'm so sleepy. Last week, I fell asleep standing up while waiting in line at the supermarket checkout, around 12:30. I previously had problems with low vitamin B1 (thiamine): brain fog. But it latter dissipated itselfs with benfotiamine regular supplementation. I'm at a suicidal level from so much mental exhaustion from going through this every day. I'm starting to think I'm developing early dementia, from how slow and incapable I feel at these times. I'm losing my life every day because of this symptom. I'm extremely disoriented about the cause of it. Typing this while I'm crying. Can any malabsorption problem cause all of this? Im from Brazil and can’t afford expensive medical care/exams. I swear by God i dont wish those symptoms for my worst enemy. Help. Any single possible advice would be appreciated. Help. I just want to feel a regular normal person… but aint being able to.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nel2xwg] (score 14, diepte 0) Classical sleep apnea/ OSA / UARS symptoms.  Get a sleep study done asap. One that counts RDI/ RERAs. Dont listen to supplement recommendations, get the study done.
[neleaez] (score 3, diepte 0) Sensitivity to light and sleepiness can be a sign of Meningitis. Get tested as soon as possible for this.
[nelenqw] (score 3, diepte 0) Consider silent or vestibular migraine causing the fatigue. You could also have some type of dysautonomia or stress related issue. I'd try replace running with a gentle walk and guided meditation for a week to see if that helps.
[nels3fg] (score 3, diepte 0) Look for inflammation in blood work, antibodies of varying types, interleukins, viral load, also check iron levels and complement cells
[nelzoj7] (score 3, diepte 0) CPAP
[neordgm] (score 3, diepte 0) I know you said you checked b12, but those symptoms particularly the eye and balance ones, are exactly what I have, although I think the deficiency was made worse by a mixture of having other conditions like hyper mobility, which is a connective tissue condition which is rarely checked for or understood, which makes you more tired, and Hashimoto’s / hypothyroidism, which I was also told that I had normal labs for years over too.


B12 tablets alone didn’t help much, and I needed b12 injections that I sourced myself, to get over then worst of it. I still feel more tired than most people, but my balance and eye symptoms are getting better finally after years of being told I had nothing wrong. Hyper mobility is something I had no idea over for years, and almost by chance it was diagnosed, so it might be worth looking into to see if anything fits. Can you bend your fingers back like 90 degrees or so? Or have loose or painful skin or joints?
[nelglrh] (score 2, diepte 1 OP) im maybe considering having an structural sleep apnea. my fear is having to use a cpap for my entire life. if i have OSA, im literally praying for it be solved with only surgeries (septoplasty, adenoid removal….). this can look petty or imature but idk what to do if a doctor tell me i need to use a cpap for my entire life. i just dont want to be “life long” treating it. the think is cause i ALWAYS felt like these, like since im 10/12yo (i always was skinny too). but thank you for the reply. its possible sleep apnea being cured (depending on your case)? I tremble all over just thinking that I could never fix this (i saw a lot of life long OSA cases).
[nelmoba] (score 2, diepte 2) Same :( felt all the time like this too. But tbh i cant take it anymore. Everything is better than this. But i am totally the opposite regarding mindset, i hope bipap gives relief else i need to undergo surgery and usually one surgery is not enough. Only if lucky. So living on hold 5 more years with 6 surgeries would be truly a shitshow
[neliu5d] (score 2, diepte 0) 1.93 TSH is high-ish tbh. Warrants further looking into to see if you have Hashimoto’s or any other antibodies. Cos when I was in college I experienced very similar problems and I got a dx a few years later.
[nem3je3] (score 2, diepte 0) When did this start? 


What exactly do you consume between waking up and getting the symptoms?
[nekyt2o] (score 1, diepte 0) Thanks for posting in /r/Biohackers! This post is automatically generated for all posts. Remember to upvote this post if you think it is relevant and suitable content for this sub and to downvote if it is not. Only report posts if they violate community guidelines - Let's democratize our moderation. If a post or comment was valuable to you then please reply with !thanks show them your support!
If you would like to get involved in project groups and upcoming opportunities, fill out our onboarding form here: https://uo5nnx2m4l0.typeform.com/to/cA1KinKJ Let's democratize our moderation. You can join our forums here: https://biohacking.forum/invites/1wQPgxwHkw, our Mastodon server here: https://science.social and our Discord server here: https://discord.gg/BHsTzUSb3S
~ Josh Universe

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Biohackers) if you have any questions or concerns.*
[nelgm1a] (score 1, diepte 2) You have awarded 1 point to DramaKlng.

---

^(I am a bot - please contact the mods with any questions)
[nhlfubz] (score 1, diepte 1 OP) and you how did you managed to correct it? are you still treating this high tsh?
[nhlgtid] (score 1, diepte 2) I have Hashimoto's so I'm probably on lifelong treatment for this. I'm using a T3+T4 protocol that gets tweaked every now and then.
[nelx1pf] (score 1, diepte 0) Sounds like you need to go to the Mayo Clinic or get a really good internist who can do a full work up.
[nemmptc] (score 1, diepte 0) How's your other vitamins? Vitamin D in particular
[nen2soh] (score 1, diepte 0) Sounds like it happens after meals, yeah? 


Are you going to the gym daily?
[nerg9e1] (score 1, diepte 0) high hemoglobin check it
[netgvsa] (score 1, diepte 0) Sleep study and get tested for epstein barr.
[nf1ofss] (score 1, diepte 0) Hi 

I've been dealing with the same thing for 10 years. And you said something very important : "I suspected it might be related to low cortisol, but my serum levels at 8/9 a.m. aren't that low, so I'm ruling out a possible "sudden drop" around noon." Serum levels are known to be unreliable at times, because they don't measure your free cortisol. So you won't know what your cortisol is at 11am or 2pm. And what you said "Everyday I feel extremely sleepy between 9/10 a.m. and 2/3 p.m," paints the picture of a dip in cortisol in 11am and 2pm, something I've experience every single day for almost decade (until i finally found a solution). My functional medicine practitioner had me run a DUTCH test to get a better picture of my cortisol pattern. And it confirmed that i had indeed low free cortisol in the daytime despite having borderline low serum cortisol [https://www.reddit.com/r/adrenalfatigue/comments/v97n3n/26m\_extreme\_fatigue\_and\_loss\_of\_libido\_for\_7\_years/](https://www.reddit.com/r/adrenalfatigue/comments/v97n3n/26m_extreme_fatigue_and_loss_of_libido_for_7_years/)

The DUTCH test showed that my metabolized cortisol was low, which often points to a slowed metabolism or hypothyroidism. My levels were actually quite similar to yours (TSH and and FT4). If i look at your results, your free T4 is at 0.97, which converts to 12.4 pmol/l (the usual range is around 12-22 pmol). It's within range but borderline low and low enough to reduce your T3 production and thus causing symptoms. As for your FT3, it's very low. You should be at least at 3.2 pg/ml. So given your numbers, you definitely have hypothyroidism. And your cognitive issues as well as your exhaustion at very specific hours are consistent with hypothyroidism and low free cortisol. Your body actually needs thyroid hormones to metabolize cortisol. What helped me? Getting on thyroid hormones, despite doctors gaslighting me "your levels are within range" "you are young, it must be in your head". 6 weeks after starting my treatment (about 18 months ago) , I regained my energy and i no longer had these energy drops at 11am and 2 pm. i could finally feel like an human being. Back then, i was often bedridden, I had severe anhedonia and i couldn't stand up for too long.

My treatment is T3 montherapy, with 3 to 4 dosages taken throughout the day. I chose this course of action (instead of T4 monotherapy and T4+T3/NDT) because my reverse T3 levels were really high and they would have increased if i had taken T4. I also had low cortisol as well as low testosterone which caused conversion issues. 

Feel free to ask if you have any questions.
[nhlakb4] (score 1, diepte 1 OP) it’s just toooo much information, and thank you for those! im reading and searching everything, i will later comment here ok?
[nhlakkn] (score 1, diepte 2) You have awarded 1 point to Out-of-line75.

---

^(I am a bot - please contact the mods with any questions)
[nib3m9v] (score 1, diepte 2) You're welcome.

Yes indeed, i only used thyroid medication (T3) taken a few hours before waking up, I didn't use any other medication to increase my cortisol. Taking T3 at specific hours during the night can help boost your cortisol (some hormones are produced in a circadian manner, that's why this method works). You can check out "Recovery with T3" &  "The CT3M handbook" books by Paul Robinson. 

I'm 29 and I'm a male.

I started feeling really bad a few years ago, with extreme fatigue, anhedonia, severe sexual dysfunction, poor concentration, insomnia...

My hypothyroidism is not related to hashimoto. I actually don't produce enough T4 because of my hypopituitarism.
[nelcto4] (score -6, diepte 0) please; 

spaces. 

kthx

=== THREAD ebrdz3 ===
SUBREDDIT: r/Supplements
DATUM: 2019-12-17  SCORE: 2  REACTIES: 23
TITEL: Peripheral Neuropathy triggered by Supplements?
POST (source_id=post):
**First of all, I'd like to apologize if you've seen me post about this issue before. I'm posting another updated post again because I did not get any helpful answers last post.**

So about 6 months ago I was on several supplements that were helping me manage my hypothyroidism symptoms and for a while, these supplements work. **For a bit of background information**, I'm 5'7, 165lbs very lean and athletic. I'm also on doctor prescribed TRT due to having secondary hypogonadism (Testosterone enanthate 175mg a week). I seem to have a bit of a sensitivity to gluten (not celiac disease but still very minor bloating after eating gluten). I don't drink, but I do smoke very occasionally (marijuana and sometimes hookah). I'm extremely health-conscious so I try to eat clean and monitor my blood markers.

Like I said, before 6 months ago I was feeling great; my energy was through the roof and I was finally enjoying life without feeling tired/run down all the time due to my hypothyroidism.

**This is what I was taking to achieve my energy increase, under the advice of a doctor ofcourse:**

**Selenium - 200mcg ED**

**Iron - 36MG ED**

**Probiotics - 30 Billion**

**Vitamin B Complex**

And for quite a while this combination of supplements had me feeling amazing, until one day everything went downhill. At the beginning I felt like I had lost agility in my legs, sometimes I'd have a bit of difficulty walking and I'd have to focus when walking a bit. Everything started getting much worse a couple of months later, and at this point, I continued to take the iron every other day instead of every day but completely **stopped the selenium and probiotics**. But stopping the Selenium & probiotic supplements did not help, I developed a constant ringing in my ears and my feet would tingle when I would sit down or lay down in bed. My feet would sometimes be tingling so much that I would literally feel the vibration through my entire body when sitting down. My legs also felt incredibly numb. I realized that the selenium had nothing to do with the problem so I continued to take it after stopping it for a little while (for an energy boost cause I felt like a zombie). As of right now I still have a very bad case of tinnitus, neuropathy in my legs and feet, pain in my ankles/legs when walking and an overall difficulty to walk.

Recently I did a copper test, here are my results:

Copper: **74 (range 80-140)**

**Ferritin results: (22/08/2019)**

Ferritin: **185 (normal 40-300)**

I started taking 2.5 mg of copper which seemed to make my feet feel extremely cold and gave me brain fog for some reason so I stopped it. I haven't checked my zinc but I'm willing to bet it could be out of the normal range.

I tried taking 25mg of Zinc & 2.5mcg of copper before bed, but that seemed to also make my feet cold and give me brain fog (not as bad as copper solo).

I read on the internet that iron supplementation could, in fact, cause low serum copper & zinc. It's been 3 days since I stopped supplementing iron and I feel like my symptoms haven't got any better. How long should I wait until I can rule out its the iron causing all my issues?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[fb7ifuk] (score 4, diepte 2) I’d probably take just a b12 supplement, to see if that helps...no complexes. Either that or track your food intake on cronometer and see what your dietary b12 intake is like, and with awareness that your actual absorption may be lower than what it’s telling you you’re getting. You don’t drink do you? 

Nerves take forever to heal. Something has damaged them, and it’ll take some time. I’d focus on a healthy diet, stay well-hydrated, and see a rheumatologist, neurologist, and if you’ve already seen them with no help, see an acupuncturist (not a chiropractor/acupuncturist but a real acupuncturist).

Eta: I see someone commented below about the testosterone...are you sure it’s not that? Have you tried stopping taking that? Some medications can cause peripheral neuropathy.
[fb749m1] (score 4, diepte 0) Saw a post a while ago in this sub where the guy had pins and needles in hands/feet and turned out to be too much B6 causing nerve damage. That was when I decided to drop the B Complex all together albeit they offering massive energy boost.
That being said, I think one should take any supplement conservatively unless instructed otherwise by a doctor, and aim to obtain most if not all nutritions from food. A balanced diet knocks out any supplementation any day.
[fb6xxqu] (score 2, diepte 0) How much B6 was in your b complex?
[fb8jxy1] (score 2, diepte 3 OP) Thanks for your input, I'll try taking b12 in the meantime.

I've never heard of testosterone causing nerve damage, and I've been taking testosterone for over 2 years. I've also never seen anyone post that testosterone gave them nerve damage. I hope that's not the case because TRT   has been life-changing for me.

I don't drink, only smoke very occasionally.

&#x200B;

EDIT: I actually tried some methyl B12 and I feel like the ringing in my ear has decreased a bit. Idk if it's placebo or not but I really hope this will work!
[fb77adi] (score 2, diepte 2) As far as I know, the neuropathy due to excess B6 takes quite some time to disappear. Whatever did cause it for you, it may take rather a lot longer than three days to rid yourself of the unpleasant symptoms. Just hang in there!

Your 10 mg doses of B6 surely were not the cause; it does not get to be a real problem with daily doses under 100 mg.
[fb77v80] (score 2, diepte 3 OP) Thank you sir, it's been 6 months of suffering and doctors haven't been able to help me :/
[fb7a192] (score 2, diepte 0) > Testosterone enanthate 175mg a week 

Could be an imbalance of steroids?

[https://www.sciencedaily.com/releases/2006/09/060926104352.htm](https://www.sciencedaily.com/releases/2006/09/060926104352.htm)
[fb6z35e] (score 1, diepte 1 OP) 10mg
[fbg769o] (score 1, diepte 3 OP) Hey man, just wanted to thank you again because I'm actually 99% sure now that I had a b12 deficiency. That being said, my memory and vision have improved but my legs are still not working like they used to.

How long does it take to recover from b12 deficiency in terms of nerve damage?
[fb6z3wt] (score 1, diepte 1 OP) Intresting.. How long did it take to feel better after cutting the dose in half?
[fb72uo9] (score 1, diepte 0) It's the b vitamins.
[fb74y35] (score 1, diepte 1 OP) Not the vitamins, i haven’t taken them in a long time.
[fb77xrs] (score 1, diepte 2) I think you should stop everything you're taking except for your actual medication. Overdose of b vitamins can present with the symptoms you're having and sometimes damage is irreversible.
[fb78pdd] (score 1, diepte 3) It also shows similarities with symptoms of a b12 deficiency. Thats usually not something you van tackle with a b complex supplemenfation.
[fb74sta] (score 1, diepte 1 OP) I wish it was that simple but I stopped taking the B complex and any other supplement along time ago. 
I only recently stopped taking iron so hopefully the iron was causing all my issues, but so far 3 days in I haven’t noticed any improvements.
[fb8kdpj] (score 1, diepte 1 OP) I really hope it's not the testosterone, 175mg a week split into 3 shots a week which is a low dose tbh compared to what steroid users take (500mg+) and it says only high doses right?
[mrsu44g] (score 1, diepte 2) Did you figure out if it was the iron?
[fb7ez71] (score 1, diepte 0) I think that this this has nothing to do with the supplements you were having, but rather did to other latent health issues.  Get some benfotiamine and ALA to see how this might help with the neuropathy symptoms, and drop everything else for now.
Your ferrtin level is high, and you might need to donate 1 or 2 units of blood.
[fb8k758] (score 1, diepte 1 OP) I thought my ferritin was in the normal range though, my red blood cells are normal too.
[fb9sza2] (score 1, diepte 2) Check this link :

[https://roguehealthandfitness.com/the-normal-value-iron-matters/](https://roguehealthandfitness.com/the-normal-value-iron-matters/)

&#x200B;

Please provide data about your fasting insulin and glucose levels as well as your triglycerides and HDL  levels, to assess how well into the diabetes zone you're into
[fb7nqb7] (score 1, diepte 0) Go get tested for diabetes type II & for multiple sclerosis. Good to have these two ruled out.
[fb8k2hd] (score 1, diepte 1 OP) I like to test my blood sugar very often, I've never been above the mid-normal range.

MS has been something that I've been wanting to test for a while.
[fkvzj8n] (score 1, diepte 0) Too much selenium can cause nerve damage.
[fkvzqc3] (score 1, diepte 0) You did not give us a Ferritin number either - Ferritin should be at least at 70.
[ntugv7z] (score 1, diepte 0) Could be B vitamins- particularly B6

=== THREAD 1nirnov ===
SUBREDDIT: r/Supplements
DATUM: 2025-09-16  SCORE: 8  REACTIES: 20
TITEL: extreme sleepiness everyday at late morning. i don’t feel human anymore.
POST (source_id=post):
Hi everyone, i’m 19M and devastated. Everyday I feel extremely sleepy between 9/10 a.m. and 2 p.m, even if by the first two hours i wake up im completely energized. This is accompanied by several symptoms such as sensitivity to light, extreme difficulty concentrating, a feeling of low energy, balance issues, vertigo, pressure in the head, icepick sensation in my brain, lump throat, feeling like l am in a dream, eye floaters/white spots on my eyes, eyes burning so bad and constant yawning... the list goes on. I sleep 8 hours a night every day. I eat relatively well, lots of fruit and animal protein, 4L of water, I don't consume added sugar, and I don't use any substances... I take zinc + copper, magnesium, vitamin B12, iron, vitamin D3+K2, vitamin B2 + B1, and I take glycine to sleep better. I have no idea what causes this. I've actually seen several doctors. Last year, I went to a neurologist, and he ordered an electroencephalogram. I didn't get any results from this test. I suspected it might be related to low cortisol, but my serum levels at 8/9 a.m. aren't that low, so I'm ruling out a possible "sudden drop" around noon. I've had blood tests, and my thyroid is fine (my TSH is 1,93, T3 is 2,3, T4 at 0,97). I go to sleep every morning at 11 p.m. I wake up at 7:30/8 a.m. (and get 10 minutes of sunlight intake). I'm now considering a possible sleep apnea. What I find strange is that when I wake up (7/8 a.m.), I'm completely refreshed and rested, I don't wake up with a headache, and I don't snore at night. In fact, the only three other symptoms I experience that could fit with sleep apnea would be waking up with a burning throat (I do breathe through my mouth a bit while I sleep), having an energy crash around 5-7 p.m., and having a deviated septum that interferes with my breathing on one side of my nose. Other than that, I have no other symptoms (e.g., wheezing, shortness of breath, etc.). The reality is that I'm desperate because no matter what I do, I always get extremely sleepy during this time. Yesterday I was at the gym running at 15 km/h and this drowsiness continued. It's simply uncontrollable. It hinders my reasoning, I'm exploding with migraine, yawning, with an extreme derealization, as if I can't feel like a human being, I'm so sleepy. Last week, I fell asleep standing up while waiting in line at the supermarket checkout, around 12:30. I previously had problems with low vitamin B1 (thiamine): brain fog. But it latter dissipated itselfs with benfotiamine regular supplementation. I'm at a suicidal level from so much mental exhaustion from going through this every day. I'm starting to think I'm developing early dementia, from how slow and incapable I feel at these times. I'm losing my life every day because of this symptom. I'm extremely disoriented about the cause of it. Typing this while I'm crying. Can any malabsorption problem cause all of this? Im from Brazil and can’t afford expensive medical care/exams. I swear by God i dont wish those symptoms for my worst enemy. Help. Any single possible advice would be appreciated. Help. I just want to feel a regular normal person… but aint being able to.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nels6i8] (score 7, diepte 0) 'having an energy crash around 5-7 p.m' and another one in the morning?

  
Extreme sleepiness, so after having your breakfast and dinner? You should your insulin levels.
[nen8iqa] (score 5, diepte 0) yeah apnea can do this.  burning throat could even be some reflux brought on by the suction effect squeezing the esophagus.  Lifting the top end of your whole bed a little to make about 5 degrees slope might help a little with both, and it's cheap.
[nelkl82] (score 2, diepte 1 OP) hi, please can you check/read again the full post?
[nenscwf] (score 2, diepte 0) Apnea.
[nekxqv3] (score 1, diepte 0) Rules of r/supplements 

1.
Do Not Suggest Prescription Drugs
Posts & Comments
Reported as: Do Not Suggest Prescription Drugs
Prescription drugs are not Supplements; do not recommend prescription medication. 
Sensible/Suggest talking to DR. can be allowable etc
                  

2.
Dangerous Grey Area Substance
Posts & Comments
Reported as: Dangerous Grey Area Substance
Potentially dangerous grey area substances can not be recommended.


3.
Be Polite
Posts & Comments
Reported as: Rude/Personal Attacks
You shouldn't ever be personally attacking another user in this subreddit.


4.
No Advertisements
Posts & Comments
Reported as: Advertisement. No selling / buying / trading posts
No advertisements. No selling/trading posts between users.”


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Supplements) if you have any questions or concerns.*
[netmcjl] (score 1, diepte 3) yes, focus on all natural cyanide and strychnine — you’ll end up in mumbo jumbo land in a flash. 🙄 

This is a group for science-based supplementation, not feel-good, meaningless religious generalities.
[netlxpq] (score 1, diepte 2) are you downvoting everyone’s helpful comments? I understand this one is problematic because they clearly didn’t read the post and then pulled out mumbo jumbo nonsense, but the rest did give good feedback.
[nennofd] (score 1, diepte 1) Agreed

I wouldn't eat within 3h of sleeping if possible, and yes maybe tilt the bed for now see if it helps with stomach healing.

Logging spo2 monitor could be had for $20-40
[neskq1j] (score 1, diepte 0) See if you have thyroid antibodies? Your thyroid levels could still be in range, but you could still have an auto immune attack on your thyroid and your numbers just don’t reflect it yet.
[netbwmf] (score 1, diepte 0) Yeah I was gonna say sounds like low cortisol. This is how I felt when my cortisol was too low.
[nelp5z7] (score 0, diepte 2) Get a blood work done and hopefully you find what you’re missing out. It looks like whatever you are taking is giving you massive side effects. Focus on natural things and return to God your creator by praying 🤲
[neldyo3] (score 0, diepte 0) Try breathing exercises (especially the 5.5s one)
[nelsxep] (score 0, diepte 0) Also zinc + copper should be taken 12h apart.
[neluude] (score 0, diepte 0) It could be possible that your supplements are doing more harm than good. I would need to know your doses of each supplement to know for sure. The body tries to attain homeostasis so if you go too high in another thing, you can be deficient in something separate. You have copper as a result of adding zinc, but what about iron? Then you have iron as a response to the copper so then what about calcium and etc. It’s a chain reaction that would be better off left alone for your body. 

Now again, doses are crucial, everything can be prevented had you use a normal dose rather than something too excessive, so please let me know.

Same with magnesium, your electrolytes can be thrown out of wack. If you take too much b vitamins (more than 100% DV) then you have to make sure you can actually pee it all out of your body by going to the bathroom every half hour or so. If you don’t, you can have a severe overflow and cause toxicity. 

Vitamin D3 and K2 is perfectly fine at levels between 40-70 but beyond that, you are better off lowering your dose (let’s say 5000 IU to 2000 IU) to maintain. I have levels of 70 from taking 5000 IUs and then I lowered my dose to 2000 IU with 50mcg K2 to maintain. 

There’s also a chance Glycine can disrupt your sleep, because that’s what happened with me. I took 3g Glycine every night and felt so tired in the morning and I found out I didn’t get enough deep sleep at all. Glycine increases neurotransmitters that help you fall asleep but disrupts the balance of other neurotransmitters that need to be decreased or stopped at sleep. 

This is me finding out everything the hard way and letting you know as well. Supplementation is tricky, but it looks like your B1 deficiency is something that needs to be addressed so that can stay. Magnesium, D3+K2 is important as well, but don’t go too overboard. Doses are important to be kept normal for body homeostasis. I would get a full blood panel of all hormones and vitamins and minerals to see what‘s too high and too low. There’s a chance your b vitamins can be insanely high and you have no idea and that’s what causing your sleepiness. Or if you take sleep supplements like magnesium and glycine at night, you just feel too out of it in the morning. All of this can only be revealed in bloodwork
[nem2si6] (score 0, diepte 0) It is a good idea to listen closely to your body and help guide doctors, who can sometimes miss important details. To do this effectively, consider keeping a detailed daily log. Note the exact times your symptoms start and stop, their intensity, what you eat, and your daily activities.  
  
This creates a clear record of patterns that can help a professional see the full picture. It will also help you clearly communicate key symptoms, such as the sensitivity to light you mentioned, which could be a useful clue.  
  
Regarding supplements, you mentioned you are already taking a number of them. It would be wise to review this entire list with a doctor.
[nem4k65] (score 0, diepte 0) What time do you eat breakfast and lunch and what do you eat?
[neniiq1] (score 0, diepte 0) Magnesium l theronate
[nenswib] (score 0, diepte 0) Migraine with derealization sounds like long covid.
[nelbk0z] (score -1, diepte 0) Hi, don’t worry I can understand the frustration. What are you currently taking in addition? Any supplements? How’s your diet like? How old are you?

=== THREAD cf9e3m ===
SUBREDDIT: r/Supplements
DATUM: 2019-07-19  SCORE: 1  REACTIES: 0
TITEL: Creatinine and gfr came back out of range
POST (source_id=post):
I did workout before I had my labs done.  But, my gfr was 51, down from 64 just six months ago. My creatinine was 1.20, bilirubin was 1.3. I understand exercise cam affect my creatinine,  but my gfr has really dropped.

I take magnesium,  zinc/copper, vit. A, K and ashwaganda.

Appreciate any thoughts on what could have caused my lab numbers. Im normal weight,  pretty fit. This didn't look good, I know.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

