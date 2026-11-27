# Label-batch batch_0155

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
Schrijf het resultaat naar `batch_0155.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 15ohacx, 11xhkid, k8eumg).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 15ohacx ===
SUBREDDIT: r/Biohackers
DATUM: 2023-08-11  SCORE: 12  REACTIES: 82
TITEL: rate my stack? anything i should drop?
POST (source_id=post):
Main focus is longevity, stress reduction, cardiovascular health, brain health, mitochondrial health, and gains. I work 12 hour shifts most nights and the energy i get from this stack is amazing, I never get anger issues like i used too over the smallest things and I don’t bite my nails or do any of my other compulsive actions anymore. I can also feel myself growing in all my clothes and i’m not even working out that hard as its hard to fit in my schedule. 

I’ll probably drop the pine bark and beetroot extract next time, but other than that i can’t think of anything to add or take away. 

ED: 
Morning: 
Vitamin D3 - 5000iu
Vitamin K2 - 600mg (500mg mk-4, 100mg mk-7) 
Ashwaganda (ksm-66) - 600mg
Garlic extract - 500mg
Olive leaf extract - 680mg
Noopept - 15mg 
Neuro-mag - 144mg
Zinc picolinate - 15mg
Shilajit (Prima-vie) - 250mg
DHEA - 10mg 
Pregnenolone - 5mg
Mk-677 - 25mg 
Tudca - 250mg 
CBD - ~100mg 
THC concentrate - ~1-2 grams 

Night: 
Magnesium lysinate glycinate - 200mg 
Boron complex - 6mg
Copper - 2mg
Shilajit (Prima-vie) - 250mg 
Selenium - 25mcg
Garlic extract - 500mg
Olive leaf extract - 680mg
Beetroot extract 20:1 - 1.4g
Noopept - 15mg 
NAC - 600mg
Taurine - 10g
Fish oil - 3.2g (1.6g EPA, 1.1g DHA)
Agmatine sulfate - 2g
Creatine - 10g 
D-Ribose - 5g 
Glycine - 6 grams 
Coq-10 - 200mg
Pine pollen extract - 5g
Pine bark extract 20:1 - 300mg
Turinabol - 25mg 
Pregnenolone - 5mg
DHEA - 10mg
CBD - ~100mg 
THC concentrate - ~1-2 grams 

E2D:
Mushroom honey micro dose - .15g

E7D:
Testosterone cypionate - 400mg

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jvryf2j] (score 31, diepte 0) This is why I come to this sub. To see this glorious "health" optimization.

>I can also feel myself growing in all my clothes and i’m not even working out that hard as its hard to fit in my schedule.

Could it be the stack...... This is a mystery for Scooby Doo

Are there any other clues???

>Testosterone cypionate - 400mg

Ruh roh
[jvv5xkd] (score 18, diepte 0) This isn’t biohacking, it’s biodumping.

Besides the huge red flags of a kitchen sink stack and a full blown steroid cycle as a long term “supplement”, do you actually think strangers on the internet can make any sense of this mess and give you meaningful advice?

Presumably every one of these was included for some reason.  That reason will reflect your priorities, philosophy, issues and experiences.  And if that’s not the case for every item in here then you have an even bigger problem.  But if I see a supplement that I judge worthless, I have no way of anticipating what you think it does or if there’s some hyper niche concern that it might be useful for.  It’s a scavenger hunt inside a scavenger hunt.  The fact that you think we might be able to add value from such a disadvantaged position says a ton about how haphazard this all is.  

Which is why you can casually list 20 placebos then mention a supraphysiological dose of testosterone like it’s an afterthought.  You have no clue what’s doing what do you?  

This is why these mega-stacks are so problematic.  Even if they’re well thought out, they put you on an island where no-one else can make sense of what you’re doing and why.  You can ask about individual compounds in isolation, but integrate it all is entirely on you unless you’ve got that Brian Johnson money to pay a professional.
[jvv8fl4] (score 10, diepte 1) >Testosterone cypionate - 400mg

That's a hell of a TRT dose.  Probably not optimal for cardiovascular health.
[jvu0elu] (score 10, diepte 0) Ashwagandha should be used intermittently, as needed.
[jvta8zt] (score 9, diepte 1) Lmao this is great. That  whole stack and only one effective supp 🤣🤣
[jvvzqu9] (score 9, diepte 1) The least of his concerns.
[jvtx9h9] (score 5, diepte 1) You’re just running a science experiment on yourself bro. I’m willing to bet half of these do nothing, a quarter of them interact negatively with each other, and the other quarter maybe help?

Biochemistry is way too complex and this is just way too much shit man.
[jvuxn61] (score 5, diepte 3 OP) constant stress, processed food consumption, environmental contamination, hormones in the water supply, micro plastics found in the human heart. theres quite a few things happening.
[jvtv7xe] (score 4, diepte 0) I’m not seeing a probiotic + prebiotic. I see you’re taking some antioxidants. Antioxidant supplements have been shown to actually decrease lifespan. Taking testosterone and just having higher testosterone levels has been shown to decrease lifespan as well. So, I would drop all testosterone supplements, drop THC, drop THC and honey micro dose and the antioxidants. I would add a prebiotic + probiotic, take a multivitamin, take 1g fish oil 600mg EPA and 240mg DHA and very simple stuff. Maybe take a magnesium, calcium, zinc, or iron supplement depending on how your diet is. If you want a longevity stack then Curcumin, COQ10, NAD+, TMG, EGCG, GSH, LDN, Metformin, Rapamycin. That’s your complete longevity stack. Also, calorie restriction that’s more powerful then these supplements.
[jvuqyaf] (score 4, diepte 2) Don’t drop but you should be getting a more potent fish oil. You should look for a product with close to 1g of epa and dha per capsule. The percentage of epa/dha to total fish oil is important and what you’re currently taking isn’t optimal.
[jvtyycf] (score 3, diepte 3) I meant to reply to OP, honestly no clue how I did this. Your stack is cool 👍 OPs is a modern day human experiment. It’d be unethical if he wasn’t doing it to himself
[jvuv32m] (score 3, diepte 2) Right, seems like every young bloke today is low T & on test. Something is happening
[jvus70q] (score 3, diepte 4) Nordic naturals is great just expensive. If you want a cheaper alternative, I like viva naturals triple strength and sports research. They are both IFOS certified but more importantly have the best bang for buck while still providing a low oxidation fish oil. You can get a bottle of 180 for right around 50 bucks and will deliver the same in less pills; alternatively you can start taking 4 pills which for a lot of people say the benefits of high dose fish oil start at 4g a day.
[jvtyk0e] (score 2, diepte 3 OP) a lot of things are addicting, but what about it being addicting is specifically bad? 

i got my dad to stop his antidepressants and start micro dosing with me and he says he feels better than on 100mg sertraline ed.
[jvv919z] (score 2, diepte 5) >Drug use is a symptom of mental health disorders.

LOL
[jvxvyrk] (score 2, diepte 5) The CALERIE study is a perfect example of what I’m talking about.  It doesn’t show an improvement in all cause mortality.  It does show an improvement in certain biomarkers when a random population of people undergo calorie restriction for a couple years.

Improvements in metabolic health and blood pressure suggest that there was room in this population for improvements to be made and that caloric restriction might yield those improvements.

Specifically in the circumstances where there is some degree of metabolic syndrome caloric restriction is well understood to be an efficacious intervention.  However is that sustainable for a person’s entire life?  Does it actually yield greater longevity in humans?  What’s the quality of life like?  What about the inevitable sarcopenia that would occur when this cohort reaches an advanced age?

The control in this study is a group on an ad libitum diet, which we must presume is SAD.  There’s no comparison, for example between folks eating an optimal diet with a neutral energy balance vs. a similar calorie restricted diet.
[jvu2qqe] (score 2, diepte 0) If thats you taking the dab on your profile, im definitely going to ask why you’re on Test Cyp
[jvuleka] (score 2, diepte 0) Drop the damn fish oil
[jvutj9p] (score 2, diepte 5 OP) this bottle was like 60 something so yeah definitely going to go with one of those next time, fish oil was the one thing i didn’t want to skimp on no matter what but didn’t really want to pull the trigger on the 2x. thank you for the recommendation!
[jvva4mv] (score 2, diepte 5) >viva naturals triple strength

Same
[jvvrgav] (score 2, diepte 6) It’s not better per se.  Certainly it’s good to keep fish oil refrigerated, I keep mine in the freezer because theoretically it allows the oil to pass further down the digestive tract before dissipating, preventing the burns.  It was something I read and seems to work for me.  Nordic Naturals would freeze together and burst, however.  Works great with the Viva Naturals triple strength.
[jvuzszq] (score 2, diepte 0) Lol this is so over excessive. How long does it take you to take all your supplements and injections?
[jw4b6gg] (score 2, diepte 2) Get some blood tests done, consider lifestyle changes. Fast maybe and look at your diet. I think having such a huge amount of supps isn't the way to go. In my humble opinion. Sometimes you need to reset and see where you are now at...Anyway, all the best...
[jvteqs4] (score 1, diepte 0) Mk677 damage the heart
[jvtgsyy] (score 1, diepte 0) Do you make the microdose honey yourself?
[jvtlufr] (score 1, diepte 1 OP) yeah. i put about 5g of shrooms in a blender, turned it into powder and added it too 100g of raw honey and let it sit for a couple months.
[jvtwy2x] (score 1, diepte 1 OP) im already taking way more fish oil than that, magnesium, boron, zinc, and copper. i do drink a lot of kefir and eat a lot of yogurt, i prefer that over probiotics. i also have a curciminoid concentrate mixed with coconut oil i cook with when im feeling sick and add a ton of black pepper. 

any reason on stopping thc and the microdose mushrooms? thc has been the single most effective drug ive ever used, helps with sleep, appetite, stress, anxiety, and it got me off of harder shit.
[jvud4l8] (score 1, diepte 5) 🤡
[jvvpx01] (score 1, diepte 5) You’re a boomer aren’t you?
[jvwdqhr] (score 1, diepte 6) Millennial
[k1oj8xr] (score 1, diepte 5) There’s abusing psilocybin and there’s using it beneficially.
[jvv9f83] (score 1, diepte 2) >stopping thc and the microdose mushrooms

The data on chronic THC use is not so good.  The data on chronic CBD use is not so bad.  Most of it is fairly recent and not widely replicated.

Maybe try CBD alone?  I use 200mg nightly.
[jvty5qt] (score 1, diepte 2) I don’t take those. There’s also nothing wrong with taking curcumin or COQ10. NAD+ has been proven to be helpful. Your body makes TMG and GSH. LDN, Rapamycin, and Metformin are the only ones you need to be careful of.
[jvtz0k6] (score 1, diepte 4) Lol all good
[jweam55] (score 1, diepte 3) As an 8-year-old I had a really bad tooth infection in one of my molars. The gum was so inflamed that I couldn't even close my mouth. The dentist suggested full-anaesthesia to remove the tooth and strong anti-biotics. 

Instead, my mom placed some turmeric (from which curcumin comes from) on the tooth twice a day for a week, and it was like nothing happened.
[jvuzgvl] (score 1, diepte 2) Fully agree
[k4a7tzg] (score 1, diepte 2) He has to be careful. Because dropping one supplement abruptly without tapering can cause withdrawals in my experience.
[jvv8xh7] (score 1, diepte 1) >1g fish oil 600mg EPA and 240mg DHA

Dosage should be closer to 4g ED for cardiovascular benefits.

&#x200B;

>calorie restriction

Bryan Johnson Much?
[jvwdwe7] (score 1, diepte 2) Maybe you should read up on how calorie restriction works and why it works then come back and say something.
[jvwgio0] (score 1, diepte 3) I've done quite a bit of reading on the topic.  There's plenty of data that shows efficacy in mice.  There's very little data that shows efficacy in humans and there are a host of confounding factors.
[jvxbemw] (score 1, diepte 4) Look at the CALERIE study and the NIA study. Research backs it up.
[jw07ph1] (score 1, diepte 1) Where have antioxidants been shown to decrease lifespan? Any actual reputable sources?
[k4a7p28] (score 1, diepte 1) I’m taking Tribulus which is reported to boost testosterone. I was taking Tongkat Ali but I felt like it had too many side effects. I am not on a steroid cycle yet but I do feel Dhea and pregnenolone have helped me with feeling better after Tongkat because it messes with your hormones.
[kbl31re] (score 1, diepte 2) Literally, it’s only effective to slightly raise test levels, IF YOU HAVEN’T STOPED your natural production, via TRT
[k4a7dfn] (score 1, diepte 1) I agree with the ashwaganda because if you take it too much you will feel like a zombie. But as the other guy says it’s not impossible to drop it. Not sure about everything else.
[jvu143o] (score 1, diepte 0) That Noopept powder. Where did you get it? I swear I’ve seen that exact one marketed by a seller on Amazon with very little or no way to verify batch quality whatsoever. I could be wrong though and it is just a shady amazon store reusing the packaging and design of another company
[jvu3ett] (score 1, diepte 1 OP) yes on amazon, the specific company had semax i tried before i realized amazon was definitely not the place for that. but had a good experience so tried the noopept. it wasnt in the same little canister its in on the listing either which was weird. but it has that smell and it clumps like crazy, so i wasn’t even too worried about scanning it.
[jvvhyrq] (score 1, diepte 2) I’d be careful man, who knows what it really is. Especially for Noopept, a relatively easy substance to source from known good vendors. It takes one batch of something awful to slip through to cause a lot of destruction
[jvu3nwb] (score 1, diepte 1 OP) why lmao? and i have low total t, and just above free t.
[jwedxi0] (score 1, diepte 5 OP) https://pubmed.ncbi.nlm.nih.gov/32067074/

dont think so.
[jwevdfq] (score 1, diepte 6) damn, didnt know thay study
[jvun7a6] (score 1, diepte 1 OP) why?
[jvurb4x] (score 1, diepte 3 OP) read my description under the post it states i am taking 3.2g of fish oil a day which is over a gram of both dha and epa.
[jvurfbq] (score 1, diepte 3 OP) ah i see what you’re saying, would the nordic naturals 2x be better? i take 5 of these pills a night so over a gram of both epa and dha.
[jvva2ph] (score 1, diepte 4) Nordic Naturals gives gives me fishy burps.

I'm taking Viva Naturals  fish oil.  6.6g ED yielding >4g of EPA.  I store it in the freezer and it doesn't disrupt my digestion.  I get it from Amazon.
[jvvf58n] (score 1, diepte 5 OP) sometimes i get lemon burps from these but never a fishy taste, is it much better to store it in freezer instead of fridge?
[jvysu6a] (score 1, diepte 4) I buy omax when I buy fish oil
[k75gcg5] (score 1, diepte 1) Does fish oil do anything? I mean every time I read an article it says supplement don’t do anything. But I guess when it comes to supplement you have the believes and the non-believers. The people who have seen the miracle first hand and others who aren’t sold just yet. Reminds me of something else too
[jvulsnp] (score 1, diepte 0) I'm new to this Biohack thing and I'm curious now, so how does this affect you in any way with all these supplements?
[jvun6dm] (score 1, diepte 1 OP) i have a ton of energy all the time, im not fatigued all the time like i used to be. i also sleep like a baby everynight, my anger issues have disolved, and my digestion and skin issues went away. 

i feel noticeably wired at night before work when i take my stack.
[jvuufoy] (score 1, diepte 2) >i feel noticeably wired at night before work when i take my stack.

I don't know what field you're in but I'm curious. Do you think these supplements have improved your performance at work? 

Do you think of nootropics as potentially profitable long term in pure $ terms, or do you view them as an expense to achieve greater longevity / happiness now?
[jvuw8mv] (score 1, diepte 3 OP) i work in a car part manufacturing plant so not very cognitively demanding but more so physically demanding. there is some parts of the job such as doing quality control where i have to do a ton of paperwork and take measurements and im more focused definitively. i notice noopept also makes talking to people a breeze, normally im very anti social and keep to myself but some nights after taking it i just want to talk to everyone and words come so easy. there is also no crash or anything like with caffeine. 

i view the nootropics as an investment, im just trying to make the best possible future for myself so im teaching myself a ton of new stuff everyday, continually improving my mind with exercises, and just overall becoming a better version of myself.
[k75gsjg] (score 1, diepte 4) Supplements are an expense. So is food. But if you don’t eat, you die. If you don’t take supplements will you die? Probably not. But do supplements make your day better? Probably. If not why would you take them and then continue to take them.
[jvuuyyp] (score 1, diepte 1) none. 

there are 2 groups of people that notice benifits: 

Group 1: People that eat very poor diet.

Group 2: Strong placebo effect.
[jvutwet] (score 1, diepte 0) Any idea on what has specifically helped with the anger issues?  Also I’m surprised I’ve never heard of turinbal before - it’s peaked my interest. You like it and have a good source?
[jvuxarn] (score 1, diepte 1 OP) im thinking its a combination of the magnesiums and the taurine, i also have an ashwaganda complex with l-theanine. 

yeah tbol is a very interesting compound, how it doesn’t convert into estrogen. i definitely notice the size increase and feel good but my blood pressure got a little high so i added in some supplements to lower it and its fine now.

 i had some anavar before this and i honestly liked that so much better. it made me feel soo good, and i actually looked better in the mirror after taking it. so i’ll probably go with that again next time.
[jvv2izp] (score 1, diepte 1 OP) less than 5 mins in the morning and night. i portion them all into containers once a week when i have jack shit to do. injection takes like 5 minutes max once a week.
[kbl2oyc] (score 1, diepte 1) FACTS. Unless you have your own “blood boy” and a team of doctors to monitor her and run constant testing to see what is actually helping him what is just a placebo. Also, none of the supplements and even the US are screamed like what are you do for all the other pills that happened to be behind the counter in the pharmacy. All the people that manufacture, supplements and make money from this world will constantly tell you that you need to “upgrade your stack” and get the newest and best products. 
THEY’RE SELLING YOU AN IDEAL. and we all know ideals can only be strived for; you CAN NEVER fully attain them! Only try our best. Unless you have extremely low T and or Are a 65+ male you really don’t wanna be relying upon an external source. TRT is so misunderstood; for example, the amount of T you were taking is twice. The amount a person should have in their system, and you have peaks and valleys when you do such a large dose a week apart. You want to mimic how your body produces T(AKA smaller subcutaneous Test doses and that’s IF you actually need it.) 
Also, when you are introducing synthetic testosterone into your body, you are shutting down your natural production for at least a month, if not longer so if you are taking Ashwaganda in hopes it will raise your test levels. It won’t sense you have shut down your natural production. BTW it’s rare, BUT Some peoples natural hormone production never starts again.
[jvva3ob] (score 1, diepte 0) first off, post what you look like. I don't see the use in us rating bottles of pills. If you're taking all this and look unhealthy, then there's a converstaion to have.
[jvvdrpt] (score 1, diepte 1 OP) i wasnt looking for ratings on bottles of pills, im asking about compounds i should add or remove.
[jvvupuy] (score 1, diepte 0) Thats double trt dose for the week. .5 2x a week is a regular trt regiment.
(16 reacties met lagere score weggelaten)

=== THREAD 11xhkid ===
SUBREDDIT: r/Biohackers
DATUM: 2023-03-21  SCORE: 14  REACTIES: 57
TITEL: Is “grounding” legit? Why/why not?
POST (source_id=post):
https://www.healthline.com/health/grounding

 See above for clarification on what I mean by grounding. There’s an idea out there that spending time barefoot in the grass/mud can lower inflammation, as the the earth is magnetic and pulls things like electrons out through your feet.  

Aka: “Earthing”

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jd36kvk] (score 10, diepte 0) If you work with sensitive electronics, it's certainly a good idea.

If you mean something different, please specify.
[jd39gri] (score 7, diepte 0) 10 subjects recruited by word of mouth? That is not quite scientific. Should be an RCT randomized controled trial. 

The study itself its kind of weak. 

Also, having studies is not the same has having good and scientific studies. 

Having said this, i do it. Just not has “grounding” but has an exercise for my feet.
[jd3esk1] (score 5, diepte 3 OP) I gotcha, no I totally agree and I didn’t take it that way. I like the honesty. 

I find it very relaxing as well
[jd6ar7f] (score 5, diepte 1) I'll inverse your position... if it doesn't cost you anything,  and you think it helps... go nuts with it.
[jd64f56] (score 5, diepte 0) Dunno about the science but I do it and it feels great!!
[jd6shp8] (score 5, diepte 0) This topic has been covered before in the sub numerous times.

The reason why this is pseudoscience and does not work is due to the atmosphere around us. The earth naturally has a voltage of 100 volts per meter of air around us and a current of about 2 picoamperes per meter. At all times, we are surrounded by a significant number of ionic electric charges that move and produce magnetic fields, and standing on an earthing mat or on ground outside does not remove those electric charges. We’re basically all living in a capacitor’s soup by being on earth.

The expected contribution of grounding yourself on reducing exposure to electric fields is dwarfed by this constitutive electric field by orders of magnitude unless you are literally shuffling on carpet to produce static electricity constantly (which can produce 35,000 volts and even then that’s not going to do much to you as the amperage is tiny at like 5 milliamps and rapidly discharges on its own without the need for earthing). These charges around us also self-stabilize and discharge constantly without the need to do it artificially every time you touch something. Ask earthers what sort of voltage differential they believe earthing will actually generate and you’ll find that it’s miniscule, such that there is no conceivable way that it could make a dent compared to atmospheric voltage. The entire theory is based on not understanding electricity.

No earthing study has been well controlled or had a large enough sample size, and no earthing study has ever properly addressed the elephant in the room of atmospheric voltage being way bigger in contribution than anything earthing does. All of them are weak and discouraging, and it’s not even worth further investigation if you have a strong background in physics and understand the context around why it can’t be doing anything logically.
[jd3ealk] (score 4, diepte 2) I would love more studies on the subject. 
For example, i find it quite relaxing. 
A possible study could be to “verify the effects of grounding on relaxation and well-being”. 

I didn’t mean to bash your post and i apologize if it looked like that. 

If anything else, grounding is very peaceful.
[jd4epa3] (score 4, diepte 0) I realize this sub might be anti science at times, but in general if something sounds like exoteric made up shit and has no scientific evidence, then you should treat it as made up shit until proven otherwise.
[jd4gebh] (score 4, diepte 0) It makes sense in the way it connects you with nature.

I don't buy the grounding theory people connecting their bwds4or what not to the ground. To me that doesn't make any sense.

I can see  walking barefoot on grass, soil. Or sand as a connection to nature. Disconnection from your mind through sensory feelings in your feet etc..

I don't but it that there's anything more to it.

Also if a study doesn't have a control group day one group being barefoot and the othet just being say in the forest. I think potentially both groups will benefit, and it's not any woowo.
[jd535s1] (score 4, diepte 0) OP, 10 subjects is not even a valid test from a statistical standpoint. It's a pilot trial.
[jd37hih] (score 3, diepte 1 OP) https://pubmed.ncbi.nlm.nih.gov/25848315/
[jd5b9td] (score 3, diepte 6) Just as an example, here's something from Nature Materials on wound healing (in this case using a new kind of hydrogel): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4615579/

The level of detail, the way hypthesis are backed by a chain of evidence, the description of experiments to make them reproduceable - it's a different world.
[jd3c45x] (score 3, diepte 1 OP) I’m not great at picking apart pubmed studies, but there’s this one plus the similar articles listed with it

I know there’s not a ton of research on it yet, that’s why I posted about it. Wanted to see what other people had to say
[jd4rkvq] (score 3, diepte 1 OP) Yeah someone said, “if something sounds like hocus pocus, be scientific and assume it’s hocus pocus until science proves it, and don’t talk about it till then either”

Like hey, that’s like, not very science, man
[jd5alky] (score 3, diepte 0) Here's my hot take on the subject as a scientist/engineer.  There are a couple types of charge differentials.  You have ionic charge, molecules with a positive or negative charge these are vital to life and all neural functioning, and you have free electrons which are the ones that make you jump when you walk across carpet and touch a doorknob. 

The free electrons pretty much adjust themselves every time you touch something, say that doorknob. The earth itself is massively electrically negative with an approximate voltage difference of 200V from the atmosphere.  See lightening. 

 Ionic radicals are not going to be affected by physical contact.  That would be expecting your blood sodium levels to go down if you wear a copper bracelet.  (which I realize some people do)

I will say, that there are benefits to walking barefoot in the park.  They are not chemical or electric, but undeniably exist.  Buying a $500 mat to rest your feet on while working is not the same thing.  I would suggest instead buying an [orgone cabinet](https://en.wikipedia.org/wiki/Orgone). It's the same theory.
[jda3ed9] (score 3, diepte 2) No doesnt need an explaination. 

You dont need to explain why something doesnt exist, that is a pointless exercise. 

You asked about the earth pulling electrons out of your body if you stand outside barefoot. That isnt a real thing. How do you expect someone to explain to you why something isnt real?  Why isnt it real? Because what you asked about isnt a thing that actually happens. Thats why.
[jda7w30] (score 3, diepte 6) You can not prove a negative with "evidence". 

The "evidence" here, is that electrons, ions, your feet, and the earth DONT DO THAT. 

Why dont they do that? 

Because that is not how physics work, that is not how human physiology works, that is not how inflammation works, and that is not how ions "work". 

Why dont they work that way? 
Because this isnt vietnam. There are rules.
[jd3cgaq] (score 2, diepte 3 OP) Could you point out what’s not so conclusive about that study instead of basically just saying no to it?
[jd52coe] (score 2, diepte 4) For starters, their picture series of "accelerated wound healing" which they attribute to grounding. There is no comparison group or any other attempt to prove causality. A serious scientist would not make such claims in a publication without a trace of actual evidence. This suggests similar scientific rigour for the rest of the article.

It's just the start. Read this article, read something published in Nature, look at the difference.
[jd4ctb2] (score 2, diepte 0) https://www.healthline.com/health/grounding#risks

Seems to cover the literature. I’m still fairly skeptical about it but some evidence seems promising. I haven’t invested in any grounding technology as I heard they can break easily or be difficult to get to work properly. I do however try to walk around barefoot in the summer.

I’ll go out to get my morning sunlight (Huberman’s essential morning routine component) and walk around barefoot for a bit. I only really do it in summer however
[jd5pdjc] (score 2, diepte 2) I read the important points here as if something has no scientific backing its best to treat it as unscientific until it has some reasonable proof supporting it. This seems like a reasonably scientific approach.

The reference to esoterisicm seems like a less important point but could reasonably be used as a good indicator that something fits in a category of subject matter that rarely has scientific backing.
[jd6zp8p] (score 2, diepte 2) But there aren't any studies worthy of notice.
[jdc37gl] (score 2, diepte 4) /r/tinfoilhats?
[jd5nc8g] (score 2, diepte 0) I have always found walking on grass soothing. I have no idea if that has to do with grounding, reflexology, or the simple satisfaction of being outside in the warm sun walking in cool green grass causing a release of neurotransmitters. I would say walking outside is healthy, as long as you don’t get worms from barefoot walking in dirt.
[k79qzhs] (score 2, diepte 2) Hello! What may do you use? I’m on the hunt for one
[jd6mjvc] (score 2, diepte 0) I used to think it was kind of bullshit or maybe only a slight help at best, but then recently I learned directly that it can actually have profound effects on mood, energy, and sleep. Looking online, there seems to be a fair amount of studies that confirm this, but I haven’t read them all. 

Part of the secret seems to be TIME. As in, 20 min won’t do it. You need hours of feet on the bare ground. The more hours, the better. When I was doing 2 hours am and 2 hours pm, I was sleeping so good and feeling so great every day. Definitely a noticeable difference! And this is coming from someone who thought it was bullshit. 

I also tend to think the “devices” such as grounding mars or blankets likely don’t have the same effect? But I haven’t tried them to be able to comment specifically with experience.
[jxtxwt8] (score 2, diepte 2) Science boot licker here
[kohj28n] (score 2, diepte 1) if you're walking around 4 hours a day barefoot (assuming somewhere on grass or in nature) that will alone do wonders for your sleep, energy, mood, etc.
[l82pdey] (score 2, diepte 1) it's the sunlight
[l82qluz] (score 2, diepte 3) that's what makes me skeptical about earthing. On the days I go outside for hours in shoes lol I feel much better. That being said i just got an earthing mat, so i'm gonna try it and i might lay down just a little bit of grass outside so i can earth the proper way and see if it helps me. We know so little that we kind of don't have a choice but to try it all
[l82rik0] (score 2, diepte 5) Who knows but there's definitely something special about the beach, you're lucky you have it near you, I'm in a desert lol the ground is so dry its probably not even conductive 😂
[l82xw93] (score 2, diepte 6) I have to concur! I lived away from the beach for almost 10 years and kind of forgot how magical it is… Now after experiencing said magic, I’m literally going to build a house at the beach and live there full-time! 

I really feel the healthiest there, it really is healing! And yeah, I’d imagine grounding in the dry desert isn’t quite the same effect as grounding on a tropical beach
[l85ygow] (score 2, diepte 7) Wow. Do you mind sharing rough geographic location? Tropical beaches are the best, I've lived in Hawaii before, they are magic. Maybe I'll go find a beach one day again but for now I guess I'll water the ground before standing on it 🤣
[l876gc1] (score 2, diepte 8) Sure man I live in Thailand. Beaches here are world class and amazing. I also love Thailand as a country. Best place ever. Best people ever.
[l8bb35w] (score 2, diepte 9) Nice! Thailand looks epic, unreal pics on instagram that i see all the time, all these crazy rocks sticking out of pristine looking water and beaches it looks amazing. Do you have some spots you could recommend that are awesome to live in and maybe also affordable? One day I wanna be by the beach again. Enjoy your beach life, i can't think of anything better than that!
[jd74rgs] (score 2, diepte 0) Grounding (aka earthing) is legit. It reduced my inflammation. Visible evidence is less edema and less fingertip blistering after using a touch screen. My blood markers for inflammation also improved.

I understand both types of *grounding*. I have professional experience designing studies to conduct environmental health research for various US agencies as well as professional experience where I grounded myself to work with electronics.
[jd378po] (score 1, diepte 1 OP) Clarification added, thanks
[jd5a1gb] (score 1, diepte 5 OP) I’ll have to check nature out. I kind of thought the same thing, but was half assuming they back that up in the full article. 

I get your point. There seem to be other articles that point to plausibility, but I haven’t dug through them. Would be nice if I had full pubmed evidence
[jd6dcse] (score 1, diepte 1) I live in the middle of a big city and just had a mental image of me going out ever morning without makeup, thick glasses (because my makeup and my contact lenses filter UV light) and no shoes to walk on bare earth. Might get a wellfare check at some point lol.
[jdaauvl] (score 1, diepte 2) "studies" lol. ChatGPT could create something more convincing and scientifically sound.
[jdbg0yc] (score 1, diepte 3) My bad. I thought I was replying to a different sub.
[jd4nl8u] (score 1, diepte 0) Incoming “bUt WhErEs ThE sCiEnCe” asses
[jd5a8vh] (score 1, diepte 1 OP) I’m not using the article in the OP as any type of proof, just grabbed the first article I saw to explain what I was talking about
[jlaz7ym] (score 1, diepte 1) I always get electric/static shock when exiting my car. Weirdly enough its this particular car and no one has experienced the same within my family. Sometime I wonder about grounding and does my body has some disproportionate +/- charge.
[jlb1pxn] (score 1, diepte 2) > does my body has some disproportionate +/- charge.
Well yes, that's the static shock.  But it's not you per se, it's probably what you wear and the materials in the interior of your car.  

But touching something has the same effect as any special mats, shoes, bedding, or anything. The Earth itself carries a pretty good charge, so if you ground to that, you are just equalizing to that.
[jd630o9] (score 1, diepte 0) I believe it's legit. It's helped me on numerous occasions and i can definitely feel a difference when I do it. 

I'm a scientist at heart and have a biology degree and I can't prove or explain why it works but it does. There are things we still don't understand about how we work.  This is one of those things.
[jd77p23] (score 1, diepte 1) Same! I have all sorts of wearables and I work around law enforcement radios and such. I spend about 20 minutes on mine a few times a week and feel refreshed afterwards. Maybe I need a tinfoil hat but I like my mat.
[jdckqty] (score 1, diepte 2) Ooh I don’t have a mat I just go to the park! But curious about the mat for winter
[k9535hh] (score 1, diepte 3) If you’ve got a copper wire, tape one side to your skin and the other to the ground port in an outlet. Static will discharge must faster than thru a mat. 

A grounding pad to sleep on, that might be solid.
[jd7jsi6] (score 1, diepte 1) Hey woke MODS, something to read from CNN. These are facts. So if you censor this, you’re censoring science.  You’ll be anti-science. 

https://www.cnn.com/2020/09/01/health/eua-coronavirus-vaccine-history/index.html
[jzoed6t] (score 1, diepte 3) If the opposite of a "science bootlicker" is someone who believes in things because they sound nice, I'll gladly accept that label.
[jzouivh] (score 1, diepte 4) When you get sick(hopefully not) you will understand
[l82q9qj] (score 1, diepte 2) Interesting feedback! I definitely have noticed a decrease in all of these positive things now that I’ve been staying indoors and have a lack of sunlight
[l82r9td] (score 1, diepte 4) I will definitely say there is something to grounding / earthing. But for me doing at the beach seems to be the best, maybe the negative ions come into play as well?
[l8d9ald] (score 1, diepte 10) Honestly yes if you can afford it or figure out how to live here? I would highly recommend Thailand! I knew I wanted to live here when I first came here in 2005, but it took me quite a few years to figure out how to do that. Unfortunately getting jobs over here is pretty tough, you have to have your own business online or external income source. 

Thailand is extremely cheap and affordable in the north and essentially away from the prime beaches, but there’s beach places that are affordable by Western standards as well. Samui, Phuket, Hua Hin, Krabi are all good. Wouldn’t recommend Pattaya beach.
[meq9ib5] (score 1, diepte 11) Not to be late to the party, but what do you think the magic is about the beach? I have experienced it too. I took my first ever vacation about 5 years ago to a beach in Florida. It changed something in me and I have fantasized about living on the beach ever since. I’m a big believe in the sunlight. I definitely get a huge boost in my mood from the sun and sleep much better. Do you think it is something more? Maybe just have something beautiful to see does something.
[mecd372] (score 1, diepte 4) How’s the earthing mat working for you?
[mjnzux7] (score 1, diepte 4) How's the mat been for you?
[mjpsrux] (score 1, diepte 5) It works. You can feel it. And there's actually solid scientific evidence that's a bit hard to find at first
[mm2thnf] (score 1, diepte 6) What benefits have you noticed?
[lire2ti] (score 1, diepte 1) Sorry to bump the thread but there’s also the fact that the earth is not at some magical ground potential. It’s ground by reference only and has the same variance in electric charges as the air.
[mypuhgb] (score 1, diepte 1) It absolutely works.
[myputig] (score 1, diepte 2) Your content has been removed under Rule 4 because it contains pseudoscientific or unsubstantiated claims. This is a scientific subreddit, and pseudoscience will not be tolerated here. Please consider this a warning and note that repeated rule-breaking may result in escalating moderator action.
[jdasubs] (score 1, diepte 1) Do you use grounding mats? Or old fashion
[jdatlh3] (score 1, diepte 2) ?
[jdcazpy] (score 1, diepte 3) I was wondering if you have experience using a grounding product like this bed Mat https://earthingharmony.com/products/sheet?currency=USD&amp;variant=42388433207530&amp;gclid=Cj0KCQjw8e-gBhD0ARIsAJiDsaVZU5Ed_PedB38ip_Kja9xg3dcOyxlbMJdm6SB5O_FbSjvRuPYFk0saAuZeEALw_wcB 

How do you ground?
[jdddc6p] (score 1, diepte 4) I use a mat like that or a heavy silver-threaded blanket. That website reminded me that my hormone levels improved with overnight grounding so my MD halved my testosterone Rx
[jddf0yi] (score 1, diepte 5) What website? the one i sent? Care to explain more thats interesting
[jddfwo6] (score 1, diepte 6) Yep. Your website. It had a long list of benefits when I scrolled down. My cortisol, t, and other hormone levels improved with overnight grounding.
[jkyiwc4] (score 1, diepte 4) I’ve heard of some guy using duct tape and wire
[jd9to5m] (score 1, diepte 0) No. Because it isnt real.
[jda2cf4] (score 1, diepte 1 OP) No because no isn’t an explanation, but good try buddy
[jda6789] (score 1, diepte 3 OP) That’s a really long way of saying no because no, good effort
[jda6iez] (score 1, diepte 4) What exactly is it that you want to know?
(20 reacties met lagere score weggelaten)

=== THREAD k8eumg ===
SUBREDDIT: r/Supplements
DATUM: 2020-12-07  SCORE: 75  REACTIES: 53
TITEL: Science of Multivitamins/Multiminerals - Are Multivitamins Healthy And Effective?
POST (source_id=post):
**TL;DR:** No. Multivitamins are not particularly effective, nor healthy. It's is significantly better to do targeted supplementation. Some studies of multivitamins show positive health outcomes, some show negative outcomes, some show mixed results and some show no effects at all.

**Problem #1 - Inadequate labelling**

Two independent laboratories found that twelve out of 27 (44.4%) of the multivitamin/multimineral supplements they tested had inadequate labeling. Some provided less vitamin A, vitamin C, or folate, than claimed, some with less than 30% of the listed amounts.

Meanwhile, several products provided more than it's listed nutritional labels, for example two gummy vitamins were each discovered to contain more than 200% of folic acid than what was listed. *This is quite close to the upper tolerable intake level.*

**Problem #2 - Nutrient requirements**

For most nutrition indicators, deficiencies vary by age, gender, and even ethnicity. Take Vitamin B6 as an example - It's “Reference Daily Intake” (RDI) is 1.7, but this number changes by age, gender, during pregnancy and lactation. Furthermore, Recommended Dietary Allowance is even different from country to country and changes over time!

The Reference Daily Intake you see on nutrition labels are very simplified. A 100% of Reference Daily Intake may not be adequate for YOU depending on what life stage you're in.

**Problem #3 - Nutrient quality**

There are different forms of vitamins and minerals, and multivitamins are often filled with the cheapest and worst forms.

For instance:

\- Different Magnesium salts have differing bioavailability.

\- Vitamin D2 actually *decreases* Vitamin D in the body.

**Problem #4** \- Antagonism

Some micronutrients inhibit absorption of other micronutrients, this is called antagonism. As an example, I took the ingredients list of a typical multivitamin and listed all the antagonistic relationships:

Magnesium - Zinc

Copper - Vitamin C

Copper - Iron

Copper - Molybdenum

Copper - Zinc

Copper - Magnesium

Zinc - Vitamin B6

Iron - Manganese

Iron - Vitamin E

**Conclusion:**

Nutrient contents are often inaccurate compared to the labelling. Even if they where accurate, they may not necessarily fit your nutritional needs. Even if they were tailored to your exact needs, they may not have quality ingredients (and could actually contain ingredients that *increase* deficiencies). Even if they have quality ingredients, many nutrients inhibit absorption of each other!

[**Sources can be found here**](https://youtu.be/mZIO4lLYnqQ)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[geylw32] (score 45, diepte 0) These issues can be ameliorated by purchasing from quality companies (Thorne, Pure Encapsulations, Life Extension etc.). They put a good degree of thought and research into their multivitamin/mineral formulas. 

Far too many companies fail to maintain those standards, leading to a marketplace flooded with ineffective and sometimes harmful products.
[gexpne4] (score 19, diepte 0) Great post!! I only take omega-3 because I don't really eat too much fish, k-2 due to the fact that a person needs like a huge amount of vegetables to get a nice amount of k-2 and vitamin D cause there are not a lot of sunny days lately hahaha.
[gez6wiw] (score 18, diepte 0) >It's is significantly better to do targeted supplementation

I wouldn't make that generalization. Multivitamins are a simple and effective way to protect against an *unknown* deficiency while targeted supplementation can treat a *known* deficiency. The two concepts aren't at odds with each other, any issues relating to supplement quality would apply equally to targeted supplementation and can be ameliorated by purchasing USP verified products.
[gexyvkg] (score 14, diepte 0) Something to add is that certain synthetic forms of vitamins actually bind to the locations they’re meant to go and not only don’t work but actually prevent the the uptake of the real nutrients as well. Primary example is folate, don’t ever take synthetic folate, it’s literally worse than nothing.
[gezbu3z] (score 11, diepte 2) The fact of the matter is multivitamins are a simple and effective way to protect against unknown deficiencies. Nothing you posted challenges that fact.
[gezmzpi] (score 9, diepte 0) Good multivitamins won't include copper or iron. They should however include bioavailble form of vitamins/minerals.

And regarding the source... A video with 15 views, 0 comments, really? It feels like you posted your own video
[geynbqo] (score 8, diepte 0) Question about magnesium and zinc - if they are antagonistic why is it so commonly sold in ZMA's?

Edit: Found this study

[https://pubmed.ncbi.nlm.nih.gov/7836627/](https://pubmed.ncbi.nlm.nih.gov/7836627/)

***Objective:*** *Both zinc (Zn) and magnesium (Mg) are widely used as nutritional supplements and the possibility was considered that Zn may interfere with the absorption of Mg, similar to previously reported results \[1,2\] obtained with the same dose of supplemental Zn on the absorption of calcium (Ca).*

***Methods:*** *Mg absorption studies and metabolic balances of Mg and of Zn were carried out in three groups of adult males in a metabolic research unit during the intake of supplemental doses of 142 mg Zn as Zn sulfate (ZnSO4) during Ca intakes of 230, 500 and 800 mg/day.*

***Results:*** *The Zn intake of 142 mg/day decreased the Mg balance and Mg absorption only during the 500 mg Ca intake compared to control values. However, the overall effect of the high Zn intake of the three groups combined, regardless of the Ca intake, was a highly significant decrease of Mg absorption and of the Mg balance.*

***Conclusion:*** *Zn supplements of 142 mg/day decreased Mg absorption and the Mg balance significantly during all Ca intakes for the three groups combined.*

I have no idea why zinc and magnesium so commonly sold and advertised in a single supplement but i have always had great dreams/better sleep with ZMAs. Gonna try to test magnesium as a stand alone sleep aid this week and compare because i happen to have both magnesium and ZMA's right now.
[gez2owo] (score 8, diepte 2) 142 mg/day zinc is such a huge unnecessary dose that nobody takes
[gezws9r] (score 8, diepte 4) I didn't post anything controversial.
[geyclg0] (score 6, diepte 0) The source is just a link to a crappy YouTube video that flashes a couple studies here and there that I can barely make out.
[gez2uy8] (score 6, diepte 1) Life Extension Two Per Day is a good one.

Any Thorne one is good, but more expensive.

There are others but these are the ones I researched and liked.
[gez2h2g] (score 6, diepte 1) Exactly what I wanted to write.
[geyoglg] (score 4, diepte 0) My multivitamin is beef liver caps. Can’t beat real food.
[ghf0kv0] (score 3, diepte 1) Proof?
[ghf86xt] (score 3, diepte 3) Yeah, you are right. Looks like unmetabolized folic acid can bind to receptors and imbed itself in molecules. Unfortunately it is not yet well studied.
[gez3699] (score 3, diepte 0) I agree that multi vitamins throw up all sorts of  issues.... 

Do you take them with food? This can increase absorption of fat soluble vitamins but inhibit absorption of other things.

Phytate, tannins and fibre in food and drink all contribute to this reduction in bioavailability.

Vitamin C when taken with food, especially fats, increases production of cancer causing nitrosamines. Conversely, taken on an empty stomach, it inhibits their production.

B12  needs to be taken on an empty stomach or sublingually to be absorbed. 

Vitamin C can inhibit absorption of selenium (despite the fact  they're often paired together).

Zinc can deplete magnesium, although you need to be mega dosing the zinc.

Amino acids are generally better absorbed on an empty stomach. Many supplemental minerals are chelated. Are these rendered useless if taken with food? 

Disagree about magnesium oxide though. The 4% thing is a fallacy... 

[This article lays out the case for oxide quite nicely. ](https://www.algaecal.com/expert-insights/magnesium-oxide-delivers-more-magnesium-with-far-fewer-pills/)

[And this study shows it outquaffing citrate for fun. ](https://pubmed.ncbi.nlm.nih.gov/22433473/)
[gezjpg0] (score 3, diepte 0) I just ordered Puori's multi - seemed pretty legit: [https://puori.com/products/v-multi-vitamin-minerals](https://puori.com/products/v-multi-vitamin-minerals) I haven't had a diverse diet for months, plus I'm recovering from cancer treatment so I thought it'd aid me and my immune system / general health. Their research seems solid.
[gf03g7j] (score 3, diepte 1) This is inaccurate. A multivitamin formulated by a reputable company will contain optimal forms of nutrients in physiologically relevant amounts. A ‘super greens’ supplement can’t match the range of nutrients found in a high quality multivitamin.
[gf0mecw] (score 3, diepte 1) Antagonism doesn't mean outright blocking all absorption, just that there are caveats to consider. Absolute amounts, ratios, and form highly effect absorption. The same nutrients can be both antagonistic, and synergistic in different places in the uptake, utilization and excretion cycle for organisms, which can further be changed by stresses or lifecycle.

In the plant world, proper ratios of nutrients are very important. Potassium, Magnesium and Calcium all "compete" with each other, and these are all in the soil at the same time and clearly plants can take in all of them. However when the ratio of one to the others goes crazy, then you can end up with deficiency. If you're curious, very broadly (it depends on soils types) the ideal ratios in a soil test report for Calcium should be roughly 3 to 8 times the ppm of Magnesium, and for Potassium to be equal (preferable) or down to half of magnesium.

Also, don't confuse absolute elemental values with absolute absorption.
In ag nutrition, polyphosphates (mostly di- and tri-)are literately just chains made from chains of orthophosphate's (mono-). However only orthophosphate's can be absorbed by plants. Polyphosphates first have to break down back into orthophosphate's, which is heavily dependent on temperature. Basically if you put out polyphosphates out when it's cold, your plants might not see any of it when they need it. The upside of polyphosphates is that it can be much more concentrated (greatly reduces shipping cost), and are compatible with other elements, like iron, magnesium and zinc.
[gf047vw] (score 2, diepte 2) Fermented soybeans, but your point stands.
[gf3tzbf] (score 2, diepte 3) Ah yes natto. Very true and very potent source. Good catch.
[ghf6ato] (score 2, diepte 2) Google synthetic folic acid binding and preventing real folic acid from being used
[geyqmih] (score 2, diepte 1) Better to drop $70 on individual ones and dose them throughout the day
[geyunnp] (score 2, diepte 2) How do you figure out what you are deficient in? https://www.pixel.labcorp.com/lab-tests/vitamin doesn't seem very comprehensive. What do I tell my doctor for the type of testing, and/or where do I get a test ordered?
[gez3yix] (score 2, diepte 2) Thanks, I’ll look into them
[gf1aqiy] (score 2, diepte 1) Not sure supplement companies are covering the 26000 nutrients in our foods, so any/all supplements taken need to be considered with the view of “if my blood test showed I’m 
 low on <X>, which of the other 25999 nutrients that were contained in the foods I’m not eating am I also deficient in, but don’t know about?”

https://www.nature.com/articles/s43016-019-0005-1
[gez5inn] (score 2, diepte 2) For some reason, that study by Firoz grew legs and ran like the wind despite follow up meta analyses showing that bioavailability is more like 26%.

 Still lower than many of the other types, but with its 60% elemental content (which is much higher than most of the other forms) its a good, cost effective option.
[gez601a] (score 2, diepte 3 OP) Indeed it was the first and only study I came across when diving into the depths of nutrition research.
[gezh4ze] (score 2, diepte 0) Take GNC vitamins and get guaranteed body odor from Thiamine overdose. Over here at GNC we put an unnecessarily obscene amount of B vitamins in ours to give the user a rush and the perception that they are working by the fluorescent whiz that occurs after ingesting. However, the B vitamin Thiamine is not filtered out through the urine, its excreted through the skin.
[gg8ljve] (score 2, diepte 1) The views and comment count are irrelevant to the accuracy of the video. Some of the most inaccurate things found on the internet have been viewed by millions of people. Also, the video itself is not the source. All of the sources are in the video description.
[gg8se3r] (score 2, diepte 2) Views and comment are irrelevant indeed, but it shows that most likely it's OP video, and then he might be dishonest. He could and should have link the studies directly.
[gf07wbl] (score 2, diepte 3) I mentioned some companies in another post (Thorne, Pure Encapsulations, Life Extension). Each produces multiple multivitamin formulas, ranging from fairly basic ‘one a day’ to more comprehensive products like the Life Extension Mix. The key is that they use high quality, carefully formulated ingredients.
[gexmx34] (score 1, diepte 0) Excellent post
[gezqfd3] (score 1, diepte 1) I don’t think you get K2 from veggies FYI
[geygaxz] (score 1, diepte 0) So what is a recommended multi?
[geywyvb] (score 1, diepte 1) that's what i wanna know
[gez1wkj] (score 1, diepte 1 OP) Good question. ZMAs contain magnesium, zinc and Vitamin B6 - So I dug up the relevant research that details those specific antagonistic relationships:

* High levels of vitamin B6 might increase the need for zinc.
* Chronic and acute vitamin B6 deficiency increases intestinal uptake of zinc but serum zinc levels decrease, demonstrating an impairment in zinc utilization.
*  Supplements of high levels (142 mg/day) of zinc might reduce magnesium absorption.

Sources [\[1\]](https://pubmed.ncbi.nlm.nih.gov/7836627/), [\[2\]](https://pubmed.ncbi.nlm.nih.gov/1957821/)

ZMA is ultimately just a trademarked name for a supplement developed by Victor Conte, which *coincidentally* co-authored the only study that shows improvements in muscle strength from ZMA supplementation [\[3\]](https://www.researchgate.net/publication/288406212_Effects_of_a_novel_zinc-magnesium_formulation_on_hormones_and_strength). On the contrary, the International Society of Sports Nutrition and the Australian Institute of Sport regard it as having no clear benefits [\[4\]](https://www.webmd.com/vitamins-and-supplements/zma-supplements#1)
[geyugsu] (score 1, diepte 0) Any tips on finding out how to find what I’m deficient in? Like at home blood test or urine kits?
[gez2rwq] (score 1, diepte 1) A basic panel run by your doctors. Most doctors will perform bloodwork as part of a standard check up and test important vitamins like B12 and D.

In lieu of that, you can find online labs that offer you all sorts of test panels you can submit to a local blood draw center and send to them to get tested.
[geywv2q] (score 1, diepte 0) if magnesium and b6 is an antagonist to zinc then why is there zma?
[gez4hd6] (score 1, diepte 1 OP) I stand corrected. The 4% claim was based on [this](https://www.researchgate.net/publication/11563416_Bioavallability_of_US_commercial_magnesium_preparations) study, but upon reading your source I must agree.
[gez3xla] (score 1, diepte 0) good post, thank you
[gezp1rg] (score 1, diepte 0) Yea multi vits are such a gimmick, I thought most serious people would be taking a super greens type supplement. Loads of minerals and vitamins from natural source and more easily absorbed
[gf065ur] (score 1, diepte 2) What multi vitamin do you recommend that has these qualities?
[gezupbu] (score 1, diepte 0) Why do companies sell combined calcium, magnesium and zinc supplements if they are antagonists?
[gf08nk8] (score 1, diepte 0) Can someone tell me why multivitamins wreck my sleep? I want to take them but holy shit that sleep quality....
[gfmmdau] (score 1, diepte 0) I'm switching to Kirkland Daily Multivitamins and also taking a separate sodium ascorbate powder. I realized that instead of taking many different kinds of supplements, I can just take instead a multivitamin. My brother is already taking kirkland multivitamins and says he has better sleep. He also has chronic depression and it went away when he started taking this.
[gey4aj2] (score 0, diepte 0) I appreciate this post. Its not necessary to drop $70 a month on a Thorne multi.
[geyj8la] (score -1, diepte 1 OP) The references are linked in the description :)
[geyhyms] (score -1, diepte 0) great! Multivitamins don't work.

The best way is to take single supplements.
[gezs8vo] (score -2, diepte 3) And my magic rock is a simple and effective way to protect against the presence of unknown tigers.
(2 reacties met lagere score weggelaten)

