# Label-batch batch_0027

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
Schrijf het resultaat naar `batch_0027.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(12 threads: bripuw, 1qfgm8h, 1rw77ke, 3jmgdv, ezju9p, zykm29, 1xtcqce, xcqebj, 1hbof0r, 1u0bfrr, ux868v, 3ozqpk).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD bripuw ===
SUBREDDIT: r/ChronicPain
DATUM: 2019-05-22  SCORE: 4  REACTIES: 16
TITEL: Help, husband suffers from the nerve problems in his feet. They burn all the time.
POST (source_id=post):
Dear Husband has meds from his Dr for his feet that sometimes helps. Has anyone tried something like the Tommy Copper type products or the compression socks ot ANYTHING that might help?  Please if you find that nothing helps, please tell me that too.  DH really can use a bit of relief and any thoughts are very welcome.  Thanks folks, you are the best group.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[eoe8ndg] (score 2, diepte 0) So is it from diabetic neuropathy? Does raising them help? I sometimes wear compression socks but can't tell you that it helps with the neuropathy. I have neuropathy though. Makes my legs feel better in general https://www.amazon.com/gp/product/B0769MGHJP/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1r
[eoehppp] (score 2, diepte 0) I find when I eat refined carbs, sugar or alchahol my feet hurt/burn. I had a really bad herniated disc that led to sciatica and I realized how much diet was affecting the pain. After I healed whenever I eat that stuff again my feet burn/hurt too. Keto and Intermittent fasting have helped me a lot. Also ice baths to calm the inflamation after long periods of standing
[eoek5u4] (score 2, diepte 1 OP) Thank you.  I am showing your answer to my DH.  If he will let me to change and follow a different food path, I will.  He does not ever drink but he is a Cookie Monster.  That is his weakness.
[eofsofn] (score 2, diepte 2) >diabetic neuropathy

I just re-read this. If it is Diabetic Neuropathy, 100% keto and intermittent fasting is the way to go. He has to regulate his blood sugar levels. Get him on a Keto diet and have him start with 16:8 but try and get him to 20:4.  I can almost guarantee this will work. He has to understand Insulin resistance. Check out Dr. Berg [https://www.youtube.com/watch?v=3HxP2VXjtpQ&t=1003s](https://www.youtube.com/watch?v=3HxP2VXjtpQ&t=1003s) and also  Dr.Fung's lectures on youtube [https://www.youtube.com/watch?v=Gw61ad-wedo](https://www.youtube.com/watch?v=Gw61ad-wedo) 

This will work
[eoeqyp2] (score 2, diepte 0) I hate that.  What helps me Some is compression socks (just some light ones, SB Light or Lite) and I inherited some of those specialized Scholls from Walmart (where it maps foot) with the Nike Air running shoes I found at the Goodwill.  Mine were for plantar fasciatis. It's also made me realize even low heeled boots and thinner running shoes Really aggravate it.
[eoersoy] (score 2, diepte 0) I have peripheral polyneuropathy and the only thing that helps for pain management is cannabis. If it's legal where you live, it's worth a try.
[eofaeyi] (score 2, diepte 0) Can also come from tight muscles and trigger points. I get this from my tight hips
[eohpbf9] (score 2, diepte 2) Yes but check dct by David mccoid i think static stretching won’t help
[eopnqmw] (score 2, diepte 0) I don't have diabetes but another condition that causes my feet to burn nonstop. The things that have helped me are: elevating my feet; using cooler water in the shower and having shorter showers; gabapentin; not wearing anything on my feet as much as possible; and NatraCure Cold Therapy Socks (but you have to be careful with these because of risk of ulcers, etc.) Recently, my doctor prescribed lidocaine cream to put on my feet at bedtime to numb them so they won't keep me up. Total lifesaver.
[eoea68t] (score 1, diepte 1 OP) Yes.  You are using the word that the Dr said and prescribed the meds for.
[eoftejr] (score 1, diepte 3) I sent you this link [https://www.youtube.com/watch?v=3HxP2VXjtpQ&t=1003s](https://www.youtube.com/watch?v=3HxP2VXjtpQ&t=1003s)  but Peripheral Neuropathy is talked about here(around 23:00)...check it out around 21:00 but watch the whole video. He needs to cut out sugar and carbs for sure, and also eat lots of salads(amino acids, B Vitamins), dark leafy greens, eggs(b12)
[eogwc6u] (score 1, diepte 3 OP) Thank you for the link.  I will be reading this.  Bless you reddit friend
[eoergt8] (score 1, diepte 1 OP) Thank you for the info!.  It is really appreciated.  DH wears a cheap shoe even though He has a quality medical shoes.  Maybe I can get him to rethink his shoes.  reddit hugs.
[eoesgkq] (score 1, diepte 1 OP) Sigh.  Not legal here and I predict it will be a very long time before we do.  I would definately try it.  Even the poor people that have seizures are denied and the oil that they go over the border for is taken to jail.  Stupidity at the highest levels.
[eogwnyh] (score 1, diepte 1 OP) Ok, so stretching might help him.  Definately a possibility.  Thanks reddit friend.
[eohtsuj] (score 1, diepte 3 OP) Thanks for the heads up on D Mccoid.  I will check it out.

=== THREAD 1qfgm8h ===
SUBREDDIT: r/ChronicPain
DATUM: 2026-01-17  SCORE: 2  REACTIES: 2
TITEL: Severe neuropathic foot pain after liver abscess surgery - Copper deficiency suspected?
POST (source_id=post):
45F with history of gastric bypass (2010, revised 2025), rheumatoid arthritis, and fibromyalgia.

**Timeline:**

* Nov 2025: Emergency surgery for pyogenic liver abscess (E. coli) + cholecystectomy
* Post-op: Metronidazole 500mg q8h for 19 days
* Dec 2025: Developed severe ataxia, vertigo, tremor → Metronidazole toxicity suspected → drug stopped
* Late Dec 2025: Severe burning pain in both feet began, worse in right foot (toes and ball of foot)
* Pain characteristics: Unbearable at night (7PM-morning), allodynia (can't touch or wear socks), crying from pain

**Key lab findings:**

* Copper: 45 µg/dL (ref: 80-155) — **44% below normal**
* Zinc: 133 µg/dL (ref: 60-120) — elevated
* Neutrophils: 1.60 x10³/µL (ref: 2.0-7.15) — low
* Albumin: 2.36 g/dL (ref: 3.5-5.0) — low
* Vitamin D: 15 ng/mL (was 7-8, improving with treatment)
* B12: 2,621 pg/mL (was 21,266 — dropping, liver damage resolving)

**EMG findings (Jan 16, 2026):**

* Sensory nerves (sural, superficial peroneal): **NO RESPONSE bilaterally**
* Motor nerves (peroneal): Amplitude 0.9-1.2 mV (normal >2.5) — **50-64% reduced**
* Diagnosis: **Axonal sensory-motor polyneuropathy, no active denervation**

**Current medications:**

* Pregabalin 75mg qhs
* Amitriptyline 25mg qhs
* Valproate 250mg daily
* Vitamin D3 supplementation
* Calcium + Vit D

**Questions:**

1. Does this pattern fit copper deficiency myeloneuropathy post-bariatric surgery?
2. Should copper supplementation be started empirically given the clinical picture?
3. Any other differential diagnoses to consider?
4. Recommendations for neuropathic pain management given the severity?

Thank you for any insights.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[o04pmyx] (score 1, diepte 0) NAD, but the suggestions from Gemini are the following:

~~Analyzing this case from a clinical perspective, the course of action for relief would likely involve a multi-pronged approach: halting the damage, replenishing the deficiency, and aggressive pain management.

Based on the evidence in the screenshot, here is how a medical team would typically approach this:

1 . Stopping the "Insult" (Immediate Action)

The most critical step is addressing the source of the nerve damage to prevent it from getting worse.

 * Remove Zinc Excess: The patient’s zinc is elevated (133 µg/dL). Since high zinc levels actively block copper absorption, the first step is often identifying and removing any source of excess zinc (supplements, certain denture creams, or cold remedies).

 * Confirm Metronidazole Cessation: The post notes the drug was stopped, which is vital as continued use could lead to permanent cerebellar damage or worsening neuropathy.


2 . Aggressive Copper Repletion

Since this patient has had a gastric bypass revision, oral supplements might not be enough because their gut cannot absorb them effectively.

 * IV Copper: In severe cases of myeloneuropathy (where balance and nerves are both failing), doctors often skip the gut and use intravenous (IV) copper gluconate.

 * Monitoring: Hematological signs (like the low neutrophils) usually recover within weeks of starting copper, but the neurological damage (the burning pain) takes much longer to heal and may only partially resolve if the damage to the axons was severe.


3 . Escalated Neuropathic Pain Management

The patient is currently on "starter" doses of common nerve medications. For the "unbearable" pain and allodynia described, a specialist would likely consider:

 * Dose Optimization: The current 75mg of Pregabalin and 25mg of Amitriptyline are relatively low. A neurologist might titrate these up significantly (e.g., Pregabalin doses often reach 300–600mg daily for severe neuropathy).

 * Topical Treatments: Since the patient has allodynia (pain from touch), lidocaine 5% patches or compounded creams (containing ketamine or gabapentin) can sometimes provide a local "numbing" effect without the systemic side effects of more pills.

 * Lidocaine Infusions: For patients "crying from pain," some hospitals offer IV lidocaine infusions as a "reset" for the nervous system’s pain signaling.


4 . Physical Accommodations for Allodynia

To manage the immediate "socks/touch" pain, patients are often advised to:

 * Use Bed Cradles: A metal frame that sits under the covers to keep the weight of blankets off the feet.

 * Desensitization Therapy: Working with an occupational therapist to slowly retrain the brain to process touch signals correctly.

Summary of the "Roadmap"
| Phase | Action |

|---|---|

| Step 1 | Immediate IV Copper repletion and elimination of zinc sources. |

| Step 2 | Increase doses of Pregabalin/Amitriptyline or switch to an SNRI like Duloxetine. |

| Step 3 | Long-term physical therapy to manage the "axonal" damage once copper levels stabilize. |

The "I don't know" factor: It is impossible to know if the damage is reversible. Axonal damage (nerve fiber death) is much harder to recover from than demyelination (the "insulation" wearing off). Only time and consistent treatment would tell.~~



I certainly hope you find a measure of relief and comfort. 💚

=== THREAD 1rw77ke ===
SUBREDDIT: r/ChronicPain
DATUM: 2026-03-17  SCORE: 3  REACTIES: 1
TITEL: Ache and pain in feet
POST (source_id=post):
So everything started when I did a  job 6 months ago. I knew i was exposed to asbestos and some fine dust from cutting copper and dust, Felt it in my chest, but my chest cleared up within a couple of days. However like 4 days after that I started feeling this relentless buzzing and tingling and weird sensation in my feet from the knees down but mostly the soles. almost like burning and my skin like a shell. Also weakness in the knees. My immediate thought that whatever i inhaled from that dust must be the cause. But I also remember leaning heavily on my knees while working which left bruised and marks. It’s been 6 months now, the sensations in my legs I would say went down from 7/10 to like 3/10 but sometime is flares up and shoots back up. The weakness in the knees pretty much disappeared. Went to the doctor and did blood work and chest x ray which all came back good. He told me to just let my legs heal and take magnesium and compression socks, he mentioned that this type of neuropathy should heal within 6 weeks. Im feeling lost and fearing of the possibility that i will live with it for the rest of my life. I don’t have neuropathy anywhere else except the sole of my legs. Also within the first 4 months there was relentless feeling of numbness. 

I did an EMG last week and the neurologist basically did not know what to tell me, she couldnt say anything about what going on. But said the nerves seem to be working fine and there’s no damage or need to see her again. Although the needle part of the test was only done on one leg. I have symptoms in both legs. 

Im very lost at this point. It’s been a rough 6 months and this deep aching feeling in my feet. Like i ran miles and miles or like i was beaten on my feet. And gets worse when wearing work shoes or standing for a period of time. A deep ache and tiredness with buzzing and tingling in the arch area. 

Any helpful suggestions or sharing your experience i will be thankful.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[oaxt6mq] (score 2, diepte 0) Well, that sounds like you need new work shoes/boots with orthopedic shoe insoles and tailored compression socks! 

This tingling/burning sensation could be due to venous insufficiency because of age (especially if you are over 40 y.o.) and long periods of standing or kneeling in unfavorable poses. Are your feet kinda swollen after a long day? That would also be a telltale sign, especially in combination with varicose veins!

Also, kneeling for prolonged periods of time without padding and / or shifting your weight from time to time can diminish blood flow to your legs and can cause numbness or other neurological problems! 

The symptoms you describe sound like what many nurses (like me) or doctors suffer from (or anyone who has to stand for prolonged periods of time) and in most cases it resolves with a pair of good shoes, compression socks, maybe special insoles and doing stretches and moving around for a few minutes every 15-30 minutes! 

Hope that helps!

=== THREAD 3jmgdv ===
SUBREDDIT: r/ChronicPain
DATUM: 2015-09-04  SCORE: 1  REACTIES: 9
TITEL: Micro Discectomy: Day 0 Post Op
POST (source_id=post):
Just wanted to share my progress about my micro discectomy surgery and how things went after that. 

I suffered from a herniated disc for 3 years already. It was uncomfortable and sometimes painful but it was very manageable. Tried all conservative methods available, from the scientific to the esoteric: ultrasound therapy, physical therapy, magnetic pole, acupuncture...

Then, all of a sudden, I woke up one Monday and I could barely move. 

In fact, that whole week I could barely move. After 5-6 weeks of images and doctor appointments, a bilateral micro discectomy for L4-L5 was scheduled. 

And here I am, just a few hours after it. I can stand on my feet and walk. I feel pretty beaten, but the nerve issue feels slightly better. 

I will keep posting the progress, but if you have any questions, I'll be glad to answer (patient to patient). 

EDIT:

It's relatively normal to be unable to pee after surgery. 
If you build a big volume, your urethra is gonna have a fun time (Google: Foley catheter).

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cuqnuon] (score 2, diepte 0) Thank you! It looks like I'll be in line for one of these in the near future and I'm terrified. Glad to hear you're up to posting your experiences with us. You rest up and don't push yourself too hard. You'll be on my mind. ;-)
[curf7e7] (score 2, diepte 2) I'm one of the ones that it wasn't successful for.  I have 7 herniated and 2 compressed disks. The surgery was performed on the L5 S1.. 9 months later, I was worse off than before the surgery :(
[cuqpd7v] (score 2, diepte 0) If you haven't already, you should start taking stool softeners.      
      
Hope you have a speedy recovery
[cuqsklb] (score 2, diepte 0) I had the same surgery in June and feel much better now.  Like you I couldn't get out of bed as the Sciatic pain was unbearable.  Glad to hear you're back on your feet.  Take it slow, don't bend or lift as I'm sure you've been told already.  Keep us posted!
[cuswckv] (score 2, diepte 0) How's it going? I'm currently dealing with a herniated L5 and if these epiderals don't hold help I'm in line for the same procedure
[cuqr26c] (score 1, diepte 1 OP) Thanks and good luck!

I totally understand the terror! 

Honestly, I think the drama, bureaucracy and overwhelm of "Back Surgery" are bigger than the procedure itself. 
Then, you have all the horror stories in the Internet that make it even worse. 

All considered, it's really not that bad and the success rates are very high.
[cuugmci] (score 1, diepte 1 OP) How was the radicular pain after your surgery? Mine is different but I'm not sure I would say better. It's only been 4 days now, so it might be too soon to see some improvement.
[cuusis0] (score 1, diepte 2) Mine mostly disappeared, just a trace of it still left.  After seeing the herniation, the surgeon knew immediately that I would get relief.  I will say this though, the nerves in my ankle and foot took such a zap during the Sciatica that I'm guessing there's some permanent damage as there's still some tingling but nowhere near what it was before.
[cuugl5e] (score 1, diepte 1 OP) Wish you good luck! Just posted an update.

=== THREAD ezju9p ===
SUBREDDIT: r/ChronicPain
DATUM: 2020-02-06  SCORE: 1  REACTIES: 7
TITEL: Struggling with Weight Loss
POST (source_id=post):
Long story short: I gained 40+ pounds last year after 3-4 months of constant steroids and switch to new hormonal contraceptives (Depo shots), even with no change in diet/activity. I’ve now switched to non-hormonal birth control (copper IUD) and have been off steroids for some time, but my weight hasn’t budged. I have ankylosing spondylitis (resulting in joint damage in hips/knees/SI joints, spinal cord inflammation) and fibromyalgia. I don’t take any pain meds, just daily muscle relaxers and Aleve as needed. I’m also currently a nursing student, so I spend about 24 hours/week in clinical and on my feet the whole time, but a lot of other time sitting to study. 

I eat fairly healthy, lots of water, fresh vegetables and lean meat—mostly chicken, very little red meat, and I really only eat 2 meals a day with a snack in the late evening. We go out to eat once or twice a week for dinner. I don’t drink often (less than once a week), and almost always only 1 drink at a time. BMR is about 1400 calories/day, which is approximately my daily intake. The only obvious things I know I could do is quit drinking soda, which I have tried in the past—only to end up with raging migraines, no energy, and no change in weight. 

I’m at a loss. My clothes don’t fit, I hate how I look, extra weight adds to joint problems, and I don’t know what to do.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[fgnq7gc] (score 2, diepte 0) It took a long time for my weight to come off after steroids. I don't think I did anything special. It just eventually kind of came off.
[fgop3sl] (score 2, diepte 0) It didn't take steroids for me to gain weight.  I hurt my neck and shoulder in late January 1992. I was in constant pain and still teaching p.e. and running 40 miles a week. By mid-May I had gained 55 pounds. I was told it was do to constant pain = constant stress. 

As time went on I continued to gain.  My weight has gone up another 70 pounds. And at my worse it was 15 higher than that. So, I started at 118 lbs, wearing a size 4. I never realized that I ate pretty well and could mess up when I wanted to as all the exercise I did helped keep me thin. I was at my fitest and lowest weight. Now 28 years later I weigh 249 pounds and wear a size tent maker.  It's very embarrassing.  I did get down to 228 about 3 years ago.

I never thought I would be fat, out of shape, in constant pain and struggling to like myself enough to keep working on the weight issue. But here I am. Oh well. I know my value is not tied to my weight, but my attitude about myself is, even when I think I have changed that.

I hope you find something that helps you.  Be sure to say kinder things to yourself than I do to me. The world gives us enough judgement, we need to give ourselves kindness.
[fgpkuhb] (score 2, diepte 1 OP) I absolutely agree with you about being in a good mental place. I have a history with eating disorders, and never received proper treatments. Calorie counting brings back a lot of those unhealthy, obsessive habits.
[fgo3zio] (score 1, diepte 0) I also gained about 40lbs on high dose steroids.  I'm still not off them, but I'm managed to lose about 25lbs doing the following:

\- replace sugar with nuts.  I'm eating many more calories than before, but with more from nuts and less from sugar, it seems like the calories don't 'stick' the same way.  Only downside is that nuts cost a lot more than sugar!  

\- eat at least 4 small meals per day.  Never go more than 4 hours without eating *something.*

If going off soda caused raging headache, no energy, and no change in weight, sounds like you may have been going through caffeine withdrawal.  Could you stop the sugary soda but get a similar amount of caffeine from coffee or tea?
[fgo6siw] (score 1, diepte 1 OP) It’s absolutely caffeine withdrawal. I’ve tried ditching soda and replacing with coffee—but coffee is a migraine trigger. I tried switching to diet soda (it’s not perfect, but no sugar/calories), but still no change in change in weight. 

I’ll try the smaller, more frequent meals and more nuts. Both will help during clinicals, since we don’t get a meal break during a 12 hour shift!
[fgp40g8] (score 1, diepte 0) i've found calorie tracking apps to be the *only* way i can lose any weight. i lost about eight kilos a few years ago with myfitnesspal, but gained it all back (plus another 15 kilos) when my pain increased and i couldn't be as active as i used to be when using the app. recently i've started using lifesum and have lost three kilos since the start of the year without any drastic changes. it keeps me accountable for what i eat and helps me to realise just how many calories are in any given meal, and apparently that's the only thing that works for me.

one caveat i want to mention with weight loss (especially the intentional, calorie-counting kind) is that you really have to be in a good place mentally to succeed. around september last year i got into this really bad mindset about losing weight (for many of the same reasons that you mentioned) and got stuck in a binge/restrict cycle for a few months where i gained even more weight, despite the fact i was 'dieting'. i feel like there's this disconnect between fit and healthy doctors who deal with chronic pain patients and say 'just lose weight! it's the easiest way to fix your pain!', and the actual reality of living with daily pain and what that does to a person physically and mentally, and between the two it's so easy to fall into this awful headspace that will sabotage any attempt at weight loss.
[fgqqjch] (score 1, diepte 2) i'm really sorry to hear that! it may take some time to find the best and healthiest method of weight loss for yourself, but remember, slow progress is more than no progress! best of luck :)

=== THREAD zykm29 ===
SUBREDDIT: r/ChronicPain
DATUM: 2022-12-29  SCORE: 7  REACTIES: 5
TITEL: What comfort items do you have and what works best for your pain?
POST (source_id=post):
I don't know about everybody else on this subreddit but I have quite a few tools I use to try and relieve some of my pain, or at least make myself a little more comfortable.

I have a huge, pregnancy body pillow that I simply can't sleep without, (I'm not pregnant) a stuffed animal to support my shoulders (I'm a side sleeper), a heating pad for my lower back, a copper infused memory foam pillow, copper infused mattress cover, a copper infused compression sleeve for one knee (recently realized I need one for both knees), a copper infused back brace, and was gifted a Sharper Image neck/shoulder shiatzu massager thing for Christmas which has helped a little with the insane tension in my shoulders and neck. It's not a dramatic difference but I've noticed a decrease in headaches and migraines since I've been using it.

Oh yeah, and my cat, Arya. She does her best to absorb as much of my pain and stress as she can. She knows when I'm sad, feeling beat down, or in like 10/10 pain. I'll add a picture of her in case anybody needs some warm fuzzy feels today.

I'm not sure if copper matters at all but it seems to be pretty commonly used for pain relief. I still wake up feeling like I've been hit by a bus just about every day, but any time I've gone without any or all of these things, like if I had an impromptu sleepover at a friend's house, I have definitely been 10 times more miserable than I have ever been in my own, carefully crafted ecosystem.

I'm just curious what works for other people. What are your comfort items and which one of those things would you most recommend to others.

https://preview.redd.it/w4i4zg3pcx8a1.jpg?width=3024&format=pjpg&auto=webp&s=ef2ce6f7fcf05a8faf94aec79efb58e8290bf66b

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j273h2b] (score 5, diepte 0) My rescue kitties, hands down. These three knuckleheads are as different as can be, yet each has an innate ability to know when my pain is spiking. One after another they come waddling into whatever room I'm in and start "luvin'" on my "boo-boo" spot. (almost always my spine) Love them to death and hey....who cares about the cost of replacing a few pieces of (scratched up) furniture every year when one receives such unconditional love 24/7?
[j27mrhx] (score 3, diepte 0) Hand warmers are great. Gloves. Kinesiology tape. Music, reading, word puzzles and my dog are good distractions. Keeping busy in general helps.
[j27puxo] (score 2, diepte 0) Heat pad, tiger balm, heated eye masks
[j284dbj] (score 2, diepte 0) Hot tub, soaks help with muscle and joint pain but after about 15 minutes makes the bone pain where the bent and broken hardware is hurt worse so gotta time it.
[k2odjot] (score 1, diepte 0) Love this post!! I’m super keen on the copper mattress!! Also your cat sounds very sweet

=== THREAD 1xtcqce ===
SUBREDDIT: r/ChronicPain
DATUM: 2026-11-11  SCORE: 17  REACTIES: 4
TITEL: Hand arthritis + colder weather = SUCK 😣😩
POST (source_id=post):
Hello, all!!

First and foremost…a HUGE THANK YOU to everyone who contributed to my last post ([here](https://www.reddit.com/r/ChronicPain/s/LiJSUTdiFn)). I got several other opinions and I’m getting a C4-7 ACDF on the 23rd!! 😍 My surgeon actually helped my Dad be able to walk again after he broke his lower back in 1992. ***Very*** eager to get this mess over with.

Now…for THIS post. I have arthritis in both my hands, and have always had pain and issues when the weather is colder. Until now, I’ve been able to circumvent this with moist heat, massage, copper compression gloves, and my usual prescription pain meds. Not this year. Ohhhhh no. 😓 It’s so bad, it woke me up out of a dead sleep…and I was sleeping with my compression gloves on and had taken ***all*** my pain meds. 

Any recommendations?? I’ve seen some folks talking about paraffin treatments being helpful (I’m assuming because of the warmth). I’m willing to try anything, because this sucks. 😭

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[19sgvfmtbswao] (score 1, diepte 0) That is wild that regular compression and pain meds are completely failing you now when they used to work fine. Since you already tried the usual toolkit maybe look into a small electric hand warmer you can grip inside your blankets. Waking up in that kind of agony is a special kind of hell.

=== THREAD xcqebj ===
SUBREDDIT: r/ChronicPain
DATUM: 2022-09-12  SCORE: 2  REACTIES: 1
TITEL: Brace recommendations?
POST (source_id=post):
My joints are all pretty unstable so I'd appreciate any recommendations, but I'm looking for knee braces in particular. I work on my feet for hours at a time(terrible, I know, but I love my job and I'm not ready to give it up yet) and I'm usually in a decent amount of pain by the end of the day. 

I've quickly become overwhelmed by all the different types of braces and sleeves available. I've heard good things about Tommie Copper and I plan to try that at home, but I'm looking for something a little heavier duty to give me support while I'm moving around on my feet...preferably something I can wear over jeans. 

Thanks!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[io7hi2a] (score 1, diepte 0) Copperfit seems to male decent stuff. You should get a pair of compression stockings. Might feel a little weird at first if youre used to socks all the time, but they help like you wouldnt believe. And after a couple days they'll be your favorites. Being on your feet, you need to look at your shoes. I wish I had some suggestions there for you, but sorry, only if your climbing power poles all day. Then its hard to beat a pair of Redwings, but you'll pay some big bucks. Im sure theres something comfortable and reasonable out there for just standing. Ask nurses, they're on their feet all the time. But your shoes are the base of the whole deal, you want the best you can get, even before loading up on braces. Doctors can turn you on to some custom made braces, I've got one for my knee, luckily the insurance picked up the $350 tab. Great brace, but I dunno if it was worth $350. I used to get back braces in Home Depot. Nice little brace for about $25. Thats a must if you do lifting too. Stay away from those wrap around elastic sleeves with the velcro. For knees especially, you want some side to side support....

=== THREAD 1hbof0r ===
SUBREDDIT: r/ChronicPain
DATUM: 2024-12-11  SCORE: 1  REACTIES: 1
TITEL: Compression glove suggestions
POST (source_id=post):
Anyone have a good compression glove suggestion? I've tried all the ones on amazon and I feel like they don't last very long. I've looked around at pharmacies around me and all they carry are the copper brand, which has been fine but I'm looking for something different. Also I feel like there's so many options for socks, just not gloves :(

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[m1jygb6] (score 1, diepte 0) the Arthritis Foundation recommends a brand called IMAK. I have not tried them yet myself and don’t know if it’s a paid endorsement or not. I do plan to try them when my other Amazon cheap gloves wear out. (I have 6 pairs).

=== THREAD 1u0bfrr ===
SUBREDDIT: r/ChronicPain
DATUM: 2026-06-08  SCORE: 2  REACTIES: 0
TITEL: Need hope and a community for my mother
POST (source_id=post):
Hi everyone, first of all, english is not my first langage so don’t hesitate if I need to clarify anything and thank you for taking the time to read this, it means the world to us.

My mother is now 53 years old and she suffers daily from her back. I can’t keep on watching her like this, I’m trying to see what we have missed and when we can still do to alleviate her pain. 

Let me explain what happened to her medically.

She has always been active, playing tennis for years, which left her with some ankle fragility due to repeated minor sprains over time.

In April 2019 she suffered a more serious ankle sprain that required three weeks of immobilization followed by 33 sessions of physiotherapy. Her left ankle remained blocked on the upper side, so her physiotherapist referred her to a surgeon. An MRI revealed coagulated blood that needed to be surgically removed. An X-ray also showed a crack in her Achilles tendon, though at the time it didn't seem to cause any additional pain — likely masked by the sprain itself.

In September 2020, she underwent spinal anesthesia (rachianesthesia) for the ankle surgery. The product was injected without any prior explanation. She immediately felt nauseous, and a second product was administered to counter that. The numbness in her legs lasted 7 hours instead of the 3 hours she had been told to expect. From the moment she woke up, she experienced severe migraines, nausea, and vomiting, to the point where she couldn't tolerate light or food. They told her to leave and that it was common to feel like that.

A home-care nurse reassured her, but 48 hours later when the clinic called to check on her, she explained again how she was feeling. This time the clinic told her to contact her anesthesiologist. He admitted he had caused a dural puncture (a tear in the membrane surrounding the spinal cord) and said it could be repaired using a blood patch — an epidural injection of her own blood to seal the tear. However, since he was leaving for vacation, a colleague would perform the procedure instead.

On September 4th 2020, the blood patch was performed. My mother noticed the anesthesiologist seemed irritated that day and felt that the staff was also under stress because of him. She didn't move during the procedure as she was maintained by someone, like procedure. Only 20cc of blood was taken for the blood patch. There was no pain when the needle was inserted — but when it was withdrawn, she felt an intense, sharp pain, as if the needle were still inside. That pain never left. That’s the starting point of our nightmare. 

She immediately told the nurse, who reassured her. My mother went home bent over in pain. She was encouraged to walk for her ankle recovery, but every twist of her back triggered an electric shock. Over time, and with movement, the pain began to radiate from the injection site throughout her spine — spreading in a T-shape across her shoulder blades and up to the back of her head.

Three weeks later, once internal tissues were expected to have healed, she resumed physiotherapy for her ankle. She mentioned her back to her physiotherapist, who tried to help — but the pain intensified dramatically, reaching 9 to 10 out of 10. A second attempt had the same result. She continued physiotherapy for the ankle, which gradually improved, though it never fully returned to normal and remained swollen internally.

Her back pain was constant and unbearable. Her GP prescribed painkillers that managed but did not resolve the pain, making it impossible for her to return to her desk job. Four months after surgery, at a follow-up appointment, she explained her situation and suggested the pain was caused by the anesthesiologist's error. She was not taken seriously. The surgeon referred her to a colleague specializing in back issues — and wrote a report that, as she later discovered, made no mention of her pain at all.

The back specialist prescribed a daytime back brace for four months and ordered a contrast injection X-ray to provoke and localize the pain. Unfortunately, my mother already had some pre-existing lumbar wear at L5-S1, and that was what showed up on the scan. From that point on, doctors fixated on this as the cause. The real pain was elsewhere, but they never listened to her.

After four months in the brace, her back muscles had severely weakened. Five weeks of rehabilitation physiotherapy helped somewhat, but the pain prevented any real progress. She could not carry more than 3 to 4 kilograms. Her daily pain level hovered around 7 to 8 out of 10, with persistent electric shocks at the slightest movement.

She enrolled in a pain management center. Her first appointment with a pain specialist (algologist) was in December 2021 — a particularly difficult time, as we had just lost her father and was grieving. Once again, she was not taken seriously; the doctor initially attributed her pain to depression. She insisted, telling him she believed a nerve had been damaged. He eventually agreed to prescribe gabapentin (also known as Neurontin) and high-dose tramadol. The relief was significant. When the doctor later tried to reduce the neurological medication twice, the pain returned both times — which finally prompted him to take her more seriously.

She then completed a second five-week back rehabilitation program, working with an occupational therapist, a physiotherapist, and trying mesotherapy (two sessions with no effect, discontinued by the doctor's decision), pool therapy, and strict restrictions on carrying weight.

She also consulted another back specialist for a second opinion, who confirmed that it is entirely possible to damage a nerve during a procedure without it ever being visible on imaging.

Around 2023, she began repetitive Transcranial Magnetic Stimulation (rTMS). The pain had been severely impacting her sleep and daily life for years. After the very first session, the effect was immediate — she slept extraordinarily well and, for the first time in years, was not counting the hours until her next dose of painkillers. She continued with monthly sessions. The relief would begin to fade between the 15th and 20th day of each month, returning to full intensity by the end. Due to a relocation, she had to pause rTMS from July 2024 to September 2025.

At her new pain center, her treatment was adjusted: she kept the same neurological medication but switched to extended-release tramadol throughout the day, with Ixprim (short-acting tramadol) as needed for intense pain spikes — which she takes regularly, because the pain frequently spikes.

In terms of imaging, she had an MRI of her knee at one point, which showed a mass at the back — near the popliteal fossa — corresponding to pain that radiated from her heel up to the knee between 2020 and 2021. Nothing was identified on the MRI. She had not noticed the worsening of her ankle due to the effect of the painkillers; it was only in 2025, during a routine X-ray, that a tendinitis was detected in the left ankle. The heel is severely inflamed. Anti-inflammatory medication has had little effect. She is currently undergoing mesotherapy for the ankle, which does seem to be helping. Her right ankle has improved quickly; the left is still being treated, alongside ongoing physiotherapy.

For her back, she has also tried acupuncture, osteopathy, hypnosis, and meditation — none of which provided lasting relief.

Her current rTMS protocol is monthly, targeting the left hemisphere at the top of the skull, over a 20-minute session. She takes 600mg of gabapentin per day (200mg at 7am, 2pm, and 11pm).

The pain has been present every single day since September 4th, 2020 — always originating from the same precise point, slightly to the right of her spine, at the thoraco-lumbar junction.

We are looking for possibilities that we have not thought of, stories that can help understand more what happened and how to cope with it, hope that she might return to a daily life without constant suffering like right now. 

Thank you for taking the time, I’m most grateful.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

=== THREAD ux868v ===
SUBREDDIT: r/ChronicPain
DATUM: 2022-05-25  SCORE: 1  REACTIES: 0
TITEL: Pure Copper Magnetic Bracelet - 2 Designs DG
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

=== THREAD 3ozqpk ===
SUBREDDIT: r/goodyearwelt
DATUM: 2015-10-16  SCORE: 19  REACTIES: 338
TITEL: TALK THINGS/ASK THINGS/THINGS ON YOUR FEET 10/16/15
POST (source_id=post):
^ See title.

10:18 and no one had posted this yet? Be better.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cw1uh5i] (score 21, diepte 0 OP) [What did you think I would wear today?](http://i.imgur.com/DiYgSox.jpg)

GD: BIG NEWS! I got that job! Got the call with an offer 2 hours after my interview. I'm absolutely thrilled. It's going to be way more work, but it'll be a lot more intellectually stimulating (and a 70% pay bump). I now have a real justification for getting some shell, the only question is what.
[cw1vady] (score 8, diepte 0) I received my [tan horsehide derbies](http://i.imgur.com/WyTZqka.jpg) yesterday and they turned out great. Quite a bit different than the [tan horsehide used on the service boots](http://i.imgur.com/DcIytVw.jpg)

If anyone is interested in the kangaroo service boots, they won't be released till next April (so far as scheduled).

Also, can someone provide some sizing advice for Carmina's soller last? I'm an 8.5 on the oscar and Viberg's 2030. Thanks!
[cw1wjjp] (score 8, diepte 0) Wsiwt: [Another day another pair of shitkickers.](http://i.imgur.com/nfMF89Y.jpg) Vintageish french  army double buckle combat boots.
[cw1wv72] (score 7, diepte 0) Booked my flights to Tanzania and Rwanda for December! Life is amazing and I'm so pumped right now!

Also, I got my Viberg x 14oz boots re-heeled and glued the dainite soles back to the midsole. Anyone else experience some sole separation with their dainite soles, particularly with their Vibergs? This is the second pair I've experienced it with.
[cw1ut2t] (score 6, diepte 0) **WSAYWT**:  [AE Green Rush Street](http://i.imgur.com/4yomhnO.jpg).  Welt joint is pretty f-ed up, but I've seen worse.  But I don't care since it's on the medial side and they were ~$100 2nds.  Got these in March, and the Dainite on these is a winner.

**GD**:  Finally received my two [Orion belts from Massdrop](http://i.imgur.com/80PTINS.jpg) (first time using it).  Black and Brown latigo and the brown is so dark is looks very close to the black one.

And I just [purchased my FIRST pair of shell](http://i.imgur.com/fDWKmcT.png) footwear yesterday with the BB Corporate Discount!  It was either this, Alden 4060, or waiting for a Meermin GMTO, but I couldn't pass this up.  It was under $1000 last year, but I'm still satisfied with the price.

In the past 4 months, I bought 2 Vibergs, 3 Aldens, 1 Alfred Sargent, 1 Quoddy, and now 1 Peal & Co. (Crockett & Jones).  [I think I'm done for a while.](http://i.imgur.com/gTq8S0j.png)
[cw20stj] (score 6, diepte 0) **AT**: Probably not appropriate for this sub, but would there be interest in a custom /r/goodyearwelt Ebbets cap?

I just saw their olive cap posted in /r/FMF and there being so much olive footwear around these parts it made me think of you guys. Like having a GYW stamp on a heelpad, it would be neat to have something else representative of our community. A ballcap just so happens to have the advantage of being visible in the open!

I know there aren't a lot of people that are comfortable with headwear, but perhaps this could be a good opportunity to experiment with. A wool ballcap would be add cozy comfort to the season that is upon us.

Let me know.
[cw1umh3] (score 5, diepte 0) [Vibergs on my feet](http://i.imgur.com/D7er6cB.png)

Talk things: Decided to add [these](https://www.meermin.es/articulo.php?idArt=4646#) oxfords to my faux Galway order due in the next few weeks (hopefully). I had been thinking of trying out Yanko for austerity brogues and having them hand patinaed to emulate EG's dark oak, but I didn't care for the Yanko last and these are a good bit cheaper (especially since I can save on shipping). Not counting this as breaking cop freeze since this relates back to my initial order in August.
[cw1w3j7] (score 5, diepte 1 OP) [Here ya go](https://www.reddit.com/r/goodyearwelt/comments/2ph0mu/gdsqwsaywt_121614/cmwmngc)
[cw1xxgv] (score 5, diepte 0) Mr Porter put up two new Vibergs.  Both with christy soles.
[cw1vg0m] (score 4, diepte 1) Congrats on the new job! 70% pay bump is not a joke too.

Btw, I hate you for wearing those Rider. Mine is not even changing status at Massdrop.
[cw1vpao] (score 4, diepte 1) Watches are the kind of thing that I appreciate the artist and craft of, but have no desire to indulge. I'm happy with my Orient; I don't need an Omega weighing me down.
[cw1utfd] (score 4, diepte 0) Imgur hates me, been trying to upload an album for an hour.  This is my placeholder for 6 month pics of Nick's 10bb and my RW warehouse sale haul, plus the gateway boots, 2 year old IR's.

Edit:  Here's the [album](http://imgur.com/a/DCA1U) Featuring RW 8114's and 8173's from RW Warehouse Sale. Nick's 10bb Ranger's with 6 months of Railroadin' and my gateway boots the 8111's I've had for almost 2 years but wear rather sparingly.

Considering dubbing the moc toes, would like to have a little darker and more durable look and utility.
[cw1vidw] (score 4, diepte 0) Happy Friday GYW. 

Is there a list floating around of people that will be at the SF trunk show? After this hellish week at work  I've decided I need at least a mini vacation and figured I could make a long weekend out of it if it's not too late to get my shit together. 

Any recommendations on winter gloves? Preferably leather, some shade of brown, sub  $150?
[cw1zupp] (score 4, diepte 0) [Leffot x Viberg action at the office today](http://imgur.com/Bn1yZFy)
[cw1urt3] (score 3, diepte 1) > Not counting this as breaking cop freeze since this relates back to my initial order in August.

mmmhmmmmm
[cw1usrr] (score 3, diepte 0) **WSIWT:** [Red Wing 875](https://instagram.com/p/85mL17gaNs/) courtesy if the awesome /u/sklark23.

**GD1:** After checking insurance and what not between vehicles I was looking at I think I'm now between the Impreza and the Crosstrek. The Impreza is slightly cheaper with higher insurance, and the Crosstrek is slightly more expensive with cheaper insurance. The dealership here just released 3 loaner Crosstreks with less than 3k miles on them though so I think I might be able to score a deal on one. I hate negotiating car prices so does anyone know how much I should be able to get them to knock off?


**GD2:** I think my love affair with watches might be coming to an end. Don't get me wrong I still like them a lot, but I think I'm a little more utilitarian about it. Automatics are cool but if I don't wear a watch for a couple days I don't want to have to wind it and set the time/date again. I also don't think I'm that enough of a fanatic to get one of the cases that keep them wound. Luckily this is good news for my wallet, and thanks to a Huckberry sale and an extra 20% off coupon I was able to pick up a Quartz Lum Tec M56 for $343, and I think I will likely put my Maratac and Seiko Monster up for sale this weekend.
[cw1w16c] (score 3, diepte 1) I was originally in on the tan horsehide derby pre-order with Notre but ended up backing out.

To be honest, I'm very glad I did. The horsehide looks a lot more red than the tan I thought it would be. They also look way more round that I expected. They still look great, just not what I expected.
[cw1w3sc] (score 3, diepte 2) Personally, I'm kind of glad the color is a little more red simply because I already have the boots and it's always good to have a little variety. If I didn't have the boots, I would have preferred to have the more tan color though.
[cw1ze8m] (score 3, diepte 5) yes, the same reddish tone. to be fair the preorder page had a swatch that did represent the color that they shipped. i just much prefer the original tan horsehide color on your boots and that is on the pair i just bought. also i wasn't thrilled when they switched the construction to gyw. i don't have a problem with it but prefer stitchdown if there was an alternative which i was able to find
[cw24ttz] (score 3, diepte 2) I wish there was somewhere on the planet where it was fall all year round. So I could always be wearing boots.
[cw1vzha] (score 3, diepte 1) Bad Habit Chili: (coffee and beer, duh)

2 1⁄2 hours, 30 minute prep, serves 6-8

Ingredients:

2 teaspoons oil

2 white or yellow onions, chopped

3 cloves garlic, minced

1 lb lean ground beef

1 1/4 lb beef sirloin, cubed

1 (14 1⁄2 oz) can diced tomatoes

1 can Guinness

1 cup strong coffee

2 (6 oz) cans tomato paste

1 can beef broth

3 1⁄2 tablespoons chili sauce (and/or chili powder to taste)

1 tablespoon cumin

1 tablespoon cocoa

1 teaspoon oregano

1 teaspoon cayenne

1 teaspoon coriander

1 1/2 teaspoon salt

2 tablespoons chili powder

4 (15 oz) cans kidney beans, drained

4 chili peppers, chopped

Heat oil in large pot

Cook onions, garlic and meat until brown

Add tomatoes, beer, coffee, tomato paste and beef broth

Add spices and peppers

Stir in 2 cans kidney beans

Reduce heat and simmer, partially covered, for 1 1⁄2 hours, stirring occasionally

Add 2 remaining cans of kidney beans and simmer for another 30 minutes
[cw21why] (score 3, diepte 2) Those both look really nice. I just really miss the stitchdown on these; I'm not into the way the toe box curves underneath/backwards towards the welt. :(
[cw206xd] (score 3, diepte 0) My wife is going on a girls weekend starting tomorrow. This might be the perfect time to make the GYW chilli and play video games/watch football all weekend.
[cw28v4y] (score 3, diepte 0) Rider just put the Moretti line on fall clearance. Down about another $50 off prices. 

**Use the code rbc50 for another $50 off all purchases (doesn't have to be Moretti).**

/u/akaghi

ETA: the Moretti line is Ron Rider's chisel toe Italian line. Lots of curves and sprezz if you are into dat
[cw2f3dy] (score 3, diepte 0) Finally with the flash floods I can wear my waxed flesh for a reason.  

http://i.imgur.com/YmdZUpX.jpg
[cw1uys7] (score 2, diepte 1) Textures on everything look awesome. Pant details? That zig zag pattern is pretty amazing. 

Also, congrats on the job. I hope I someday can get a 70% pay raise!
[cw1vzen] (score 2, diepte 2 OP) Thanks man! They're [these guys](https://www.jcrew.com/mens_category/PantFitGuide/Dress/BowerySlim/PRD~C8503/C8503.jsp?Nbrd=J&Nloc=en_US&Nrpp=48&Npge=1&Ntrm=bowery+slim&isSaleItem=false&color_name=BROWN&isFromSearch=true&isNewSearch=true&hash=row4) from J Crew
[cw1vzub] (score 2, diepte 2 OP) Thanks! The wait is the wooorssstttt, I didn't realize they'd be sending this out in stages.
[cw1uhr0] (score 2, diepte 0) > 10:18 and no one had posted this yet? Be better.

Because we are all trying to buy the Carmina GMTO

**QOTD**

Which fellow GYW member do you most admire for whatever reason, and what are the reasons?

**WSIWT**

[side view, Quoddy](http://i.imgur.com/Ceg8RCw.jpg)

[Top Down](http://i.imgur.com/ird0NhD.jpg)
[cw1w6gz] (score 2, diepte 3) Um, one?  I know it was Vader's fighter, but was a prototype at the time..  Not sure if they ended up making any after.  But after looking again, I actually think those are TIE bombers and interceptors, so it makes sense that there are many.  I'm thinking too hard, now I want that shirt
[cw1ukoj] (score 2, diepte 0) [Rancourt custom mocs](http://i.imgur.com/PnVUee4.jpg) today.  If you haven't experienced an RLH sole I highly recommend it.
[cw3z3gq] (score 2, diepte 2) [Here's a post I did on them](https://www.reddit.com/r/goodyearwelt/comments/24jibu/rancourt_custom_camp_moc_unboxing_and_size/)

Make up is basically:  
Camp Moc  
Natural CXL  
Reltex natural crepe sole   
Blind eyelets  
Self-laced (Natural CXL lacing)  
Flat backstay
[cw1vg0c] (score 2, diepte 2) Well my arbitrary decision not to buy shoes can be arbitrary explained away as I see fit haha
[cw1uv7y] (score 2, diepte 1) Bergs are sweet and outfit looks spot on. I can't tell if your pants are black or blue though. Either way stacks are awesome.
[cw1v6r7] (score 2, diepte 1) Sounds awesome. Can't wait to see everything!
[cw24z5g] (score 2, diepte 3) Looks like we've both put a decent amount of wear on them. What have you done as far as maintenance? I've only conditioned mine twice, but I brush them every couple of wears. I actually need to give them a bit of attention today.
[cw25bmw] (score 2, diepte 5) Yeah, the chromepak doesn't need to be conditioned super often.

The laces that came with mine were plain-Jane nylon that looked really crappy. I've had black rawhide in for a couple of months now.
[cw26ly6] (score 2, diepte 7) Yeah, my pair are 6" Roberts. I just mistakenly assumed they would come with nylon and leather.

My MiL works at western shop, so I have the hookup with rawhide.
[cw1xdlv] (score 2, diepte 1) Idk if it's the worst thing, but was trying to upload my WAYWT while waiting for my coffee and a legally blind man walked into me and almost tripped in public.  I got the public look of shame.

How was I supposed to know a blind man was going to walk into me! 😳
[cw1uzb9] (score 2, diepte 0) [English country gent who got lost in the city](http://imgur.com/wImvoDl)

[Top down](http://imgur.com/ofdxpBw)

[Boots](http://imgur.com/He23xiJ)

Hope everyone has a chance to grab the shell PTBs!
[cw1zehp] (score 2, diepte 2) Tricker's Eaton boots. They were a collab with Leathersoul
[cw1v0f0] (score 2, diepte 0) [Ace boots](http://i.imgur.com/bk3BeHb.jpg) today. [Iron Rangers](http://i.imgur.com/1QBxrEN.jpg) on a little hike yesterday, where I saw some turkey and elk. My pup lost her mind when she finally noticed the turkey's.

I should have grouted my shower yesterday, but it's so [freaking beautiful out](http://i.imgur.com/CfohR3k.jpg) that it's difficult to do anything inside.
[cw1v5hq] (score 2, diepte 0) GD : booked my flight to NY for next month. Looks like I will be meeting a few of you on the 7th. 

Work has been absolutely insane for the past week. I'm starting to feel like I did when I worked over night shifts in school. I feel disconnected from the 9 to 5. 

There will be Jay's games Monday through Wednesday next week. I'm not looking forward to getting into town. 

WSAYWT: no clients today so very casual and [vibergs](http://i.imgur.com/wYV66lZ.jpg)
[cw1ynbt] (score 2, diepte 1) Boots >>>>>>>>> derbies
[cw2cyiv] (score 2, diepte 3) Bogota might be it.
[cw1vaxi] (score 2, diepte 0) http://i.imgur.com/RSFUTaQ.jpg Rosewood Galways today. Not gonna be rainy for a while.
[cw1vvro] (score 2, diepte 1 OP) Maybe let's make a separate thread for it? That way it'll be easier to find and make plans as well.

I'll be there!
[cw1vkp1] (score 2, diepte 0) On my feet, [Chuck Taylor II Thunder aka. grey](http://i.imgur.com/jf7fgpG.jpg).

Talk thing, besides I am salty because my Rider x Massdrop is not even shipped yet,  I am actually good. Looking forward for colder temperature and finally wearing my DR leather jacket today!

Also looking forward to meet some of you at NY Styleforum event. Question, should we book some places, restaurant or bar to hangout after the event? I prefer restaurant because... food!
[cw1wqxn] (score 2, diepte 2) Sounds so good. I'm going to have to try this!
[cw1vyvh] (score 2, diepte 0) * **WSIWT:** No shoes again. Just alpaca socks. Working from home again.
* **Leather Things:**
  * Made a [bifold from the Italian Rocado SRL Shell Cordovan](http://i.imgur.com/zbAFFVD.jpg) to test it out. [It finishes](http://i.imgur.com/yCVvVBi.jpg) up very nicely. 
  * As I mentioned yesterday, I got some rare Horween shells/scraps in the mail (Ravello, Whiskey, Saddle, Cigar). [Ravello](https://cdn.shopify.com/s/files/1/0233/4285/files/IMG_3733.JPG?14995973843455615553) and the [interior](https://cdn.shopify.com/s/files/1/0233/4285/files/IMG_3729.JPG?14995973843455615553). [From left to right: natural, saddle, whiskey, ravello](https://cdn.shopify.com/s/files/1/0233/4285/files/IMG_3734.JPG?14995973843455615553). Total Horween family. From left to right: [Natural, saddle, whiskey, ravello, #2, #4, cigar, dark cognac, #8, black](https://cdn.shopify.com/s/files/1/0233/4285/files/IMG_3726.JPG?14995973843455615553)
[cw1yp22] (score 2, diepte 1) Hey Deusis, I was thinking it would be cool to have a short shell compendium as a post so we could add it to the archive. You have a lot of experience and knowledge that could be very helpful to everyone (myself absolutely included) regarding regional differences, thickness, finishes, etc
[cw1yyjv] (score 2, diepte 2) Yeah I could definitely put that together.
[cw1wjus] (score 2, diepte 0) GD: I think my Massdrop Rider Dundalks are a half size too big for me! Gah.  
WSIWT: [Viberg Boondockers](http://imgur.com/a/RcAfr)
[cw1yaxw] (score 2, diepte 1) What's your size and what color are they?  You know for science.
[cw1wzg2] (score 2, diepte 0) WSIWT: [Calf Dundalks](http://imgur.com/kbo99Gu)

GD: I have a 4 hour seminar on academic integrity today. The length suggests small group talk about your feelings break outs. This might kill me.
[cw28dsi] (score 2, diepte 3) Eh, I have no shame. I would wake up in the library constantly with pics of me sleeping in my inbox. That's actually kind of creepy now that I think about it.
[cw1xxa6] (score 2, diepte 0) WSIWT: Gustin Black 2.1s (Italian denim do fade pretty slow don't they...), [Sauce-zhan](https://www.reddit.com/search?q=sauce-zhan) brushed twill shirt, and well, [*those* Taobao Rangers](https://lh3.googleusercontent.com/_fSvzk2ySoGtytnUErzGFT4OYpjzQ4F1yQaVfzcNH9OtqIQk3lOFWXiCO69GoXHOs2EHx3qMUa-V_NS0IylXxNneS0BxJywtBo2HB_4Ye7WcFyKQVLilq3RQc-1DGfhHpL_qVRC6De7sVpVd7flS3Ib7adqCZG0fHfUBul0BlYQDJtqzwz9nhQKdKnnYmpNOs9wWa2mJ-FE4E3cUxx4nkVBiT7Q9C8bt-O3rokn5_5wSQg_R_d6SCpsKQubziDD7IJrtFVghEV_U_uA-gYB3WWMYXUSCJob6Dys9beUx5FzJ1B-wzqbDU6C1cPnBM-bsWFf_TYDCYgQrHc9MkOEovIxIbKbpjymiDkczj-8gKlyhr0e_Ocbx8t5l9YGE846hIYYVygLb69davDYe7-oYVRic5RYOw1Aiyr5KTaKLv8rTJfTowBbinBurWMhVlbm_LpiMrzqFk0NktcOf76vF7-U0enj6pdsKQE0OiligteyePPwxrDdcnZMU-HiimkpltUjPnsuLKDQfoWiq9XXUA2hG4ScVeIYIj7zPugxe5D1n=w633-h852-no). Yup, I like this name - going to call 'em Taobao Rangers from now on.

Heading to Hong Kong in November, any food/do/shoe/shopping place recommendations?
[cw2033g] (score 2, diepte 1) Both are pretty cool. Pics/links below for those interested.

[Pic 1](http://cache.mrporter.com/images/products/654034/654034_mrp_fr_l.jpg). [Link](http://www.mrporter.com/en-us/mens/viberg/scout-oiled-roughout-leather-boots/654034).

[Pic 2](http://cache.mrporter.com/images/products/654035/654035_mrp_fr_l.jpg). [Link](http://www.mrporter.com/en-us/mens/viberg/scout-roughout-leather-boots/654035).
[cw28ath] (score 2, diepte 3) I thought they were only going to be doing gyw on the more delicate leathers. What's p with this?
[cw1yd0o] (score 2, diepte 1) I have an 8.5 in Stan Smith and wear 8 in 2030.  I could probably get away with 7.5 but the width might be too tight.  I wear thicker socks for the boots.  I think 9.5 will fit you okay, especially with thicker socks.
[cw20czh] (score 2, diepte 3) What type of leather are you going to get?  I think if it's CXL or something that stretches it should be fine (will be snug at first).
[cw21gjr] (score 2, diepte 3) 9 could probably work for you. I'm around a 9E on the brannock and I can wear an 8 or 8.5.
[cw24hgp] (score 2, diepte 1 OP) I'm about the same size as you, just a hair under a 10D. Though i wear a 10 indy, and while they don't fit perfect, they're not super loose. I can wear both a 9 and a 9.5 in the 2030 last, I would guess judging based on the indys that a 9 should work for you.
[cw2886x] (score 2, diepte 1) If it isn't too painful, I would probably try and wear them for a bit and see if it compresses enough to wearable.
[cw1ymrv] (score 2, diepte 0) [Got home the other night, took off my Cordovan Macneils, and noticed this.](http://imgur.com/gh226Sa)  So I guess that's a thing I need to deal with.  It was pretty worn down already and needed replaced, so I guess that's just motivation to deal with it.
(273 reacties met lagere score weggelaten)

