# Label-batch batch_0130

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
Schrijf het resultaat naar `batch_0130.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(6 threads: 1rusgg5, 12si6lw, 3z5m3j, 67y88a, 1uzrwx8, 1fes3hq).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1rusgg5 ===
SUBREDDIT: r/Fibromyalgia
DATUM: 2026-03-15  SCORE: 12  REACTIES: 33
TITEL: Need help / advice
POST (source_id=post):
Background

Bare with me for the long post. I’m 25M with symptoms started roughly 2 years ago following a period of severe psychological stress. Onset was fairly acute — things changed noticeably around that time and have persisted and progressed since.

My Symptoms

	∙	Widespread burning pain all over my body — not in one spot, not following any nerve pattern, just everywhere

	∙	Fasciculations (muscle twitching) — constant, all over

	∙	Terrible heat sensitivity — hot cars, hot showers, warm rooms make everything dramatically worse

	∙	Sound sensitivity — ordinary sounds feel overwhelming

	∙	Brain fog — not depression, not tiredness, a specific cognitive haziness

	∙	Fatigue — disproportionate to activity level

	∙	Stiffness

	∙	Neuropathic itching

	∙	Constant stomach gurgling / GI dysregulation

	∙	Low heart rate variability 

What makes symptoms worse:

	∙	Heat — significantly

	∙	Stillness — when I’m lying still and quiet the pain is at its absolute worst

	∙	Silence — sound sensitivity and pain both amplify

What makes symptoms better:

	∙	Movement — gentle walking or activity reduces pain noticeably

	∙	Distraction — when cognitively engaged pain is less intense

	∙	Eating — meals temporarily reduce pain (vagal activation?)

Magnesium glycinate — calms the gut gurgling and takes some edge off pain

Imaging — all normal:

	∙	MRI brain with and without contrast — mild nonspecific bilateral T2 white matter foci, nonenhancing, listed as possibly migraine/inflammatory/microangiopathic — no MS lesion pattern, no enhancement, got at 23 yrs old.

	∙	MRI cervical spine — completely normal, got at 24

	∙	MRI thoracic spine — completely normal (23)

	∙	MRI lumbar spine — completely normal

Neurophysiology: (23)

All other recents tests done at 24

	∙	EMG/NCS — completely normal

	∙	Skin biopsy (Therapath) — normal epidermal nerve fiber density (15.51 thigh, 9.14 calf) — sweat gland nerve fiber density test was technically invalid (no sweat glands identified in specimens — inconclusive, not normal)

Blood panel — extensive — all normal/negative except:

	∙	HLA-DQ2 positive (DQA1\*0501/0505, DQB1\*02XX) — celiac/gluten sensitivity gene

	∙	Everything else negative including: ANA, anti-dsDNA, anti-ENA, Sjögren’s antibodies, NMO IgG, anti-MOG, MAG IgM, GM1 IgM, anticardiolipin, ANCA, rheumatoid factor, Lyme, tick-borne panel, HCV, syphilis, HbA1c, thyroid, B12, folate, vitamin D, B1, B6, copper, ceruloplasmin, mercury, celiac HLA DQ assoc, antigliadin IgA/IgG, CBC, CMP, lipids, ESR, CK, ACE, testosterone, immunoglobulins, and more

What has NOT been tested yet:

	∙	Anti-Hu (ANNA-1)

	∙	Anti-CV2 (CRMP5)

	∙	Anti-DPPX

	∙	Anti-CASPR2

	∙	Anti-LGI1

	∙	Anti-ganglionic nAChR alpha-3

	∙	Anti-TG6 (transglutaminase 6 — gluten neuropathy specific)

	∙	SCN9A/SCN10A/SCN11A genetic panel (Nav1.7/1.8/1.9 channelopathy)

	∙	VZV IgM / VZV PCR

	∙	Alpha-galactosidase A (Fabry disease screen)

	∙	Formal autonomic testing (QSART, tilt table, thermoregulatory sweat test) — the sweat gland biopsy was invalid so autonomic small fibers have never been formally assessed

	∙	Quantitative Sensory Testing (QST)

	∙	Lumbar puncture (CSF analysis)

	∙	MR neurography

What Has Been Ruled Out

	∙	MS — no enhancing lesions, no classic MS lesion pattern, NMO and MOG negative, spine completely clean(no spinal tap done)

	∙	Structural compression — all spine MRIs normal, EMG normal

	∙	Large fiber neuropathy — EMG/NCS normal

	∙	Diabetic neuropathy — HbA1c normal

	∙	Thyroid — normal

	∙	B12 deficiency — normal

	∙	Lyme — negative

	∙	Lupus — ANA negative, anti-dsDNA negative

	∙	Sjögren’s — SS-A/SS-B negative

	∙	Vasculitis — ANCA negative

	∙	Inflammatory myopathy — CK normal

What Has NOT Been Ruled Out

	∙	Small fiber neuropathy with functional/channelopathy mechanism (normal biopsy doesn’t rule this out — biopsy measures density not function)

	∙	Autoimmune autonomic ganglionopathy (anti-ganglionic nAChR never tested)

	∙	Gluten neuropathy / celiac neurological syndrome (HLA-DQ2 positive, anti-TG6 never tested)

	∙	Nav channelopathy — SCN9A/SCN10A (never genetically tested)

	∙	Zoster sine herpete — VZV reactivation without rash (never tested, stress-triggered onset makes this relevant)

	∙	Paraneoplastic ganglionopathy — anti-Hu, anti-CV2 never tested

	∙	Anti-DPPX autoimmune hyperexcitability syndrome

My understanding is that fibromyalgia is essentially a central sensitization syndrome — and I almost certainly have central sensitization as a component of whatever this is — but fibromyalgia feels like a description of symptoms rather than a diagnosis of cause. And I feel strongly that there is an underlying cause driving the central sensitization that fibromyalgia as a label would leave unaddressed.

Has anyone here had a similar presentation? Did you get a diagnosis? Did anything help? Does this sound like fibromyalgia to you or does the full picture suggest something else?

Any advice or insights from other experiences will be helpful, where should I go next. I’ve seen neurologists and pain specialists. Tried gabapentin, nortriptyline, lyrica,  cymbalta, nortriptyline only gives me partial relief.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[oanzrpq] (score 3, diepte 0) Those symptoms would align pretty well with fibromyalgia. The only thing you can do is keep moving as much as possible. Low dose naltrexone may help but like all fibromyalgia treatments, it works for some and not others. 


Also a dude, I was diagnosed around your age and I know how awful it is to get cut down this young.
[oao0b16] (score 3, diepte 1 OP) My sleep is awful. I’ll have to take 3mg Melatonin and sometimes CBN just to sleep. Do you have muscle twitching ?
[oar26bc] (score 2, diepte 3 OP) I took LDN. Did nothing. Was on it for 4 months
[oao0j5v] (score 1, diepte 2) Yeah, both my mom and I take trazodone or we can't sleep at all. 


Muscle twitching is relatively uncommon for me but it does happen.
[oao18vb] (score 1, diepte 3 OP) FYI, When I say muscle twitches I mean Fasciculations, not spasms. And the heat sensitivity is brutal ! I will just burn all over, head to toe non stop. I work mostly sitting and I’ll get stiff muscles. It’ll feel like my whole body is getting squeezed, and feels like my blood is boiling. I’m contemplating to get a lumbar puncture if it’ll be any value at this point, I don’t know 🤷‍♂️
[oaodf0r] (score 1, diepte 4) Try a higher dose of LDN. It helped my fatigue at 4.5mg but not the pain. At 9mg per day I got significant pain relief.
[oao1spr] (score 1, diepte 0) It would be good if you could run it by a doctor who specializes in fibromyalgia. As for underlying causes, they seem to be myriad as are the symptoms. For me it’s stress and physical trauma, but sometimes kids get it, so is there a genetic component? It’s being studied.
[oao29r0] (score 1, diepte 0 OP) I have also tried neurofeedback and chiropractic adjustments with zero improvement
[oaol0f0] (score 1, diepte 0) Pretty similar to my symptoms, the muscle twitching has been driving me insane.
[oaqwmz5] (score 1, diepte 1 OP) Got any advice. The burning all over 24/7 is just not sustainable. This has been going on since October 2024 and has not gone away since ! I’ve seen so many neurologists and pain management specialists. One wanted to try a spinal cord stimulator. The other prescribed the nortryptiline. The constant 24/7 brain fog, muscle tightness, twitching ,burning, tingling and heat sensitivity and fatigue is just brutal ! I can’t get any good sleep. Have you found any meaningful relief from anything ? It’s just pure torture everyday ! I feel like crying in my sleep some nights. I take the CBD and CBN religiously and sometimes I’ll need to take so much melatonin and nortryptiline  just so I can shut my eyes. I’ll then wake up and the cycle will continue ! Even getting up I have tremendous brain fog, I’ll have no mental clarity. I don’t know what the solution is for this at this point ! Ive dropped over $1000 on a few neurofeedback sessions and chiopractic adjustments and nothing. I’m just so miserable, unhappy, very depressed. I have no joy in anything. The only time I feel sometime of relief is when I get up out of my seat and move to grab a water or a snack when I’m in the office which I am currently working in the office and the symptoms, brain fog, no mental clarity, the pain 🔥

Any advice you have ? Did you find anything that will give any relief. I also think my sympathetic nervous system is over taxed. My heart rate variability is <40 !

I need this to just go away ! No answers from neurologists and pain specialists. I had the skin biopsy which showed no SFN. I’m thinking of pursuing a spinal tap but I don’t even think that’s even worth it
[oar1zs4] (score 1, diepte 2) The burning sensation all over is actually the only symptom I don’t have. So I can’t give any advice in that. This is very new for me as well and I don’t have a lot of advice, I’m currently in a terrible flare that has me barely able to get out of bed. I wish I could help, this disease has no easy answers, maybe LDN could help you. That’s what I’m going to ask my doctor to try next.
[oarl00g] (score 1, diepte 4) I’m sorry that’s frustrating. I tried duloxetine and amitryptaline and they both do nothing for me. My HRV is usually barely above 40, but idk what it was before I got sick because I didn’t track it back then.
[oarom89] (score 1, diepte 0 OP) There’s gotta be an answer to this ! I just can’t take it anymore, I want normalcy back !
[oas89zg] (score 1, diepte 0) It does sound like small fiber neuropathy to me. I have heard from people that their punch biopsy was negative but they still had it. They didn't do your foot? Maybe they need to do that.
[oasbdfn] (score 1, diepte 1 OP) No foot, just right thigh and calf. If it is SFN, it has to be non length dependent. I know it can’t be length depended since this did not start in the hands and feet and worked up.
[oascou5] (score 1, diepte 2) It is possible they just didn't get the 'right' spot.
[oascx49] (score 1, diepte 3 OP) Maybe. I had therapath used to analyze the skin biopsy
[oasdaox] (score 1, diepte 4 OP) It did you my ENFD was within normal limits. Other than typical nerve pain meds like gabapentin, lyrica, nortriptyline, duloxetine, what else is there ?
[oasdksl] (score 1, diepte 5 OP) And is there anything that can be done about the brain fog ? And is that MRI report typical and nonspecific for the most part ? “Mild bilateral scattered nonenhancing punctate foci of increased T2 signal within the cerebral
periventricular and subcortical white matter which are nonspecific and can be seen with migraine, post
traumatic/infectious/inflammatory etiologies, lyme disease, chronic microangiopathic changes and primary
demyelinating processes.”
[oasigof] (score 1, diepte 6) I don't remember what the wording was on my mri report from my brain but the neurologist said there was proof there that I indeed have migraines. He pointed to white spots.
You could ask to try a sodium channel blocker. I started oxcarbazepine a month ago and I do think it helps some. You could also try low dose naltrexone. It helps me with fatigue and for others it works for pain. Don't know what it does for brain fog. But worth a try.
Did the neurologist not explain the mri findings? It says "primary demyelinating processes.” Doesn't that point to neuropathy? It is all so confusing and most doctors have no clue about it.
I am not familiar with Therapath. I am in the US and the lab that did mine is Sagis / crl
[oasjli3] (score 1, diepte 7 OP) I’m in the US too, neurologist was not concerned about the mri given the what the findings were and what the radiologist had put. I did try low dose naltrexone with no results, 4 months at 4.5mg. I’ll ask about a sodium channel blocker maybe. I don’t know what else is there, there aren’t much for SFN treatment. I read up on IVIG, most insurances don’t cover this treatment and it’s very expense OOP
[oaskapu] (score 1, diepte 8) IVIG only works if it's auto immune related I think. But I could be wrong. It just sucks. We are basically on our own.
[oaslo24] (score 1, diepte 9 OP) I guess so 🤷‍♂️
[oasml0o] (score 1, diepte 9 OP) Is low heart rate variability common in SFN ?
[oasrvm3] (score 1, diepte 10) I'm not sure. According to my watch mine is pretty good.
When I had my punch biopsy I had 0.1 and 0.3 instead of 3 on both feet. Neurologist said it can't get any worse. I know it's all over my body by now.
[oast1s0] (score 1, diepte 11 OP) So you have it everywhere as well, like I mean all over ! For me it feels like every square inch burns. Heat aggravates it like a shower, hot climate etc
[oasv8i3] (score 1, diepte 12) I went to the neurologist with it because after I got covid a little over 3 years ago I got blurry vision and my legs felt they were cramping up. My feet were burning and felt really numb. For years before that my feet did feel weird, as if there was sand in my shoes or something. But not a big deal. Till covid. It was a very mild one. No fever, no coughing, but it destroyed my life. My feet are totally numb now. Luckily they don't burn a lot. My thighs can hurt a lot when I overdid it, but the oxcarbazepine seems to help with that. Still have double vision sometimes. My belly sometimes does a weird thing where my diaphragm goes down instead of up when breathing out, which makes my belly look like I am 3 weeks overdue with triplets. My hands have been feeling off lately too, as if I slapped something really hard. No big things to see on mri and emg showed carpal tunnel. The feeling is not from that. The exhaustion is debilitating. Unfortunately I am also dealing with severe back issues. Had surgery almost a year ago and about to have another. I am already dreading the pain I will feel in my thighs after surgery, like I did last time. I have had heat intolerance for many years now, way before I had any issues in my feet. Lots of fun when you live in Texas and you have horses to take care of....
Sfn just sucks and people can't see it so they don't understand.
[oaswp9x] (score 1, diepte 13 OP) Exactly, I can’t account for your situation but for me, I look completely healthy on the outside but miserable everyday 24/7 in pain. People will say I look fine and it’s psychosomatic etc. I was going to see if I can get looked by Dr David Simpson out in Mount Sinai, maybe he’ll offer something different than any other neurologist I saw. EMG I had passed with flying colors, no issues there. My recent doctor I saw was Dr Norman Latov out in New York Presbyterian hospital. That’s where I got the skin biopsy and emg and those blood panels. His recommendation was to see a pain specialist. First one I saw recommended a spinal cord stimulator to be implanted, the other just handed me a prescription for nortriptyline.
[oat1vq3] (score 1, diepte 14) I was actually going to do a trial for the spinal stimulator, mostly for my severe degenerative disc disease but I was hoping for the added benefit of relieving sfn. But my back is beyond spinal stimulator so not going to do that.
You would think NYC would have competent enough doctors....
I wish you the best. Hopefully you will get some relief. It would be amazing if you could find the cause and that that is treatable. I have a feeling for mine it is a mutation in those genes you mentioned weren't tested yet. That's why I asked the neurologist for a sodium channel blocker. He had actually given me one but that one is not approved for chronic pain (journavx). It works really well when I do take it so it's very frustrating knowing there is something that helps both my back pain and sfn and we are not allowed to take it. But it got me looking into gene mutations. If you did 23andMe you can access your raw data. I do believe I found those mutations but it's hard to interpret them on your own.
[oasx6s9] (score 1, diepte 13 OP) I have no idea what caused this, before this I was at the gym 5 days a week, I did get fired from my job at that time hence the title, I thought maybe the stress caused this, I woke up like this one day and the rest was history.
[oaue6h5] (score 1, diepte 0) nossa! gabaritei nos seus sintomas. tenho absolutamente todos, e o que mais me incomoda é a dor ardente, também sinto essa dor em "pontadas" e em "facadas", e também os espamos são MUITO frequentes, eu tenho espamos o tempo todo
[oauecp9] (score 1, diepte 1 OP) Are they full spams or quivers all over, mine are fasciculations
[oaufmwo] (score 1, diepte 2) sim, são fasciculações em lugares completamente aleatórios.
eu concordo completamente com o que você disse, a impressão que eu tenho, é que o nome "fibromialgia" é o que os médicos dão para algo que eles não conseguem encontrar nos exames, e que existe uma causa maior por trás disso.
a minha saúde mental está esgotada, sonho com o dia em que acordarei e não terei mais nada disso

=== THREAD 12si6lw ===
SUBREDDIT: r/gout
DATUM: 2023-04-20  SCORE: 0  REACTIES: 23
TITEL: Copper bracelet question.
POST (source_id=post):
I just experienced my first gout flareup. Years ago, I had a buddy who wore a copper bracelet that he swore by. He claimed that the copper in contact with his skin kept the gout at bay. Can anyone confirm or deny this?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jgypol6] (score 17, diepte 0) Don't fall for it. The company who made that stuff got sued for fraudulent claims about its benefits.

If you really wanna try this, go to the hardware store and buy copper wire and make your own bracelet. Don't waste your money buying a manufactured one.
[jgyvqcd] (score 15, diepte 0) Sounds like witchdoctor shit. Document document document. When you have a flair, think about which foods you not only ate immediately before but go through your whole previous week. Change it up from there. Get meds if you can (allo). It’s a mysterious ailment with no clear cut answers. For me, chicken seems to be a trigger. Which, based on medical consensus, it shouldn’t be.
[jgz12yl] (score 14, diepte 0) It’s 100% certified bullshit designed to separate rubes from their money.
[jgz59q3] (score 10, diepte 0) This is pseudoscientific BS. It does nothing for any condition at all.
[jgz4avg] (score 8, diepte 0) If it was that simple, it would have been solved centuries ago..
[jh0evzr] (score 6, diepte 1) Well, if you wear a copper bracelet long enough, it could give you contact dermatitis. That's probably the only thing it does.
[jgzcdhn] (score 4, diepte 2) Yes, about 70 years ago, not centuries ago.
[jgz5787] (score 4, diepte 0) How would that even work?
[jh0yvw7] (score 3, diepte 1 OP) That’s exactly what I was thinking. I figured I’d ask around before potentially wasting time and money
[jgzg8g1] (score 3, diepte 0) Yes this is true, I will also had that everyone in this sub is the Easter bunny and we, has Easter bunnies, are here to save the world. Also remember to use the bracelet in your forehead and wait for the 7th moon to give you a call.
[jgzkgdv] (score 3, diepte 0) Some of these junks are harmless except to people's pockets, but some are actually harmful. I remember a bracelet or something that's marketed to release negative ions was actually radioactive! ☢️
[jh03x5j] (score 3, diepte 0) BS
[jh0k8k9] (score 3, diepte 0) Satanic black magic shit
[jgzbral] (score 2, diepte 1) Gout has been solved. Just not by copper wire or crazy supplements
[jh0kd04] (score 2, diepte 1) When you put it on your wrist you close your eyes and wish really really hard
[jh1cze8] (score 2, diepte 0) It has the same effect as a placebo. That doesn't mean it won't make someone feel better, it just means the effect is in your mind. So while it might make you feel better during a flare, maybe, the mind can't "keep gout at bay."  In other words it wouldn't prevent flares.
[jh1dlnc] (score 2, diepte 0) Otherwise drinking water from a copper pipe would do the magic also? Or taking extra copper supplements? Unfortunately not. If you asked me? A totally myth or made-up story.
[jidkimv] (score 2, diepte 0) I wrapped foil around my foot once while having an attack because I couldn’t call in sick for work. It worked for the day I couldn’t really feel the pain until I got home unwrapped it and the pain was 10000x worse 😂🥲
[jh0yzxc] (score 1, diepte 1 OP) Interesting. Thank you
[jh0z6kk] (score 1, diepte 1 OP) Dude, that’s such bullshit! I know damn well one of you is the tooth fairy
[jgzx4ma] (score 1, diepte 0) Deny deny deny deny deny deny
[jiebt2e] (score 1, diepte 1 OP) 😂😂😂
[jh05pjo] (score 0, diepte 0) I'm not sure, but I'd love it if you could put me in touch with your buddy: I have some swamp land to sell in Florida that he might be interested in!

=== THREAD 3z5m3j ===
SUBREDDIT: r/TalesFromYourServer
DATUM: 2016-01-02  SCORE: 243  REACTIES: 22
TITEL: NYE/NYD Double = My first customer demand to see a manager = free bottle of champagne. For me.
POST (source_id=post):
TL;DR: Fall on my ass, wait on bitches, manager gives me booze.

Backstory: Restaurant unexpectedly busy for NYE/NYD.  I worked Weds dinner, double NYE, double NYD. Owner buys way too many cases of REALLY expensive champagne and we're supposed to flog bottles at a special price, but it's still a bit too high for our clientele.

Our downtown does First Night, which apparently means "take your children into any restaurant you please and let them act like hellions." New Year's Eve segued from six-year-olds acting like six-year-olds to grown-ups acting like six-year-olds.  Made it through that unscathed, although our bar got totally backed up and at one point we were just opening the bottles of champagne in the server station and pouring for customers because waiting on the bar was hopeless.  Unsurprisingly, open bottles in the server station turned into servers having a drink or two like cheeky Victorian kitchen staff sneaking a nip of sherry under the stairs. 

New Year's Day started off okay but soon devolved into Land of Screaming Children again.  These children were accompanied by their hungover adults, meaning that the restaurant at some point flipped into a wall-to-wall pile of cornbread crumbs, dregs of bloody marys, and destroyed crayons. 

In the midst of Crumb Hour, we had a fully packed house and two servers -- normally we'd have three to four in that situation.  Other server and I are running our asses off, mostly because these are your standard super-needy brunch tables.  "Can we...I need a..."  

I'm coming down the center aisle in our dining room, you know, the one with hardwood floors at that "fast walk wish I could run" speed common in service. I'd been pretty aware of the children in the restaurant thus far, but I missed this little fucker and his fucking [tiny magnetic block.](https://www.momastore.org/museum/moma/ProductDisplay_Tegu%20Magnetic%20Wooden%20Block%20Set_10451_10001_188704_-1_26698_16152_188717?gclid=CNaP5sO_i8oCFZaPHwody5wNjw).  It's in the middle of the aisle. I land my heel directly on it and, with two water pitchers and a pint of porter in my hands, I slip.  Dramatically. I end up in the worst pigeon pose ever on the floor, the water pitchers intact, about a 1/4 of the beer now on the floor. 

Thank god for stretch jeans.

Mom looks horrified, kid starts laughing uproariously. The other kids at the tables start laughing. Dad jumps up and tries to help me up, but mainly just stands over me waving his arms.  I put the pitchers on a nearby table and lurch to my feet.  A baby somewhere in the room starts screaming. Of course, I'm trying to act like everything is okay, customer service smile firmly in place, "It's fine, it's fine, I'll be right with y'all." World's Best and Sweetest Hostess runs over with towels and we get everything cleaned up. 

20% tip and apology note on the ticket. Whatever, fine. I would have forgotten about it except for the fact that my right buttock now feels like it's on fire because I've pulled something. 

I take some Advil and power into the evening shift.  Things are pretty good, I've got some big tables that need separate checks but also two and four tops who are very nice. Kitchen starts running out of stuff, and then they start fucking up.  Badly.  Ticket times pop up to 35 to 45 minutes.  Expo isn't reading tickets right, so orders are getting screwed up. 

Cue the arrival of the Harpies. Four ladies who become five.  Bar slows down.  They can't decide on drinks, want beer and liquor samples, and then I can't get drinks on the table fast enough for them. I put their order in and, admittedly, forget an appetizer. It's one that I seriously wish we'd take off the menu because the fucking thing takes 14 minutes to bake and that's too long for an app when your ticket time for an entree is usually 16 to 20 minutes. So I apologize for the lateness of the app but expo has messed up an order that needs to be corrected, I apologized for that. 

It was a perfect storm of needy table / drunk basic bitches / server screw up / kitchen screw up.  And, because I was running my ass off -- my ass which still feels like it's on fire from the earlier slip and fall and it's been joined by shooting knee pain -- for the rest of my tables, I neglected to take the app off the bill, which I should have done. 

I bring the check to the table, delighted that I was finally getting rid of the harpies.  The host finds me and says "Table 48 is asking for a manager."  So I go back to the table and ask if I can help with anything.  "oh, no," they say.  "We just need a manager." 

Ok, whatever, manager is a young, attractive dude and I was like GO MANAGE THEM THEY WILL LIKE YOU. He comes back shaking his head and I immediately say "I'm so sorry!  I fucked up! That fucking app!" 

He sighs and says "Oh, okay. Listen, those women are cunts.  How much do you think we should knock off the bill to make them go away?" 

That was unexpected. This manager is normally kind of a hardass, AND [he's the one whose bell I froze inside a 2-gallon block of ice recently.](http://imgur.com/h5cWnLv) 

We take the late app and a round of drinks off. I separate the bill (doing them a favor) and drop the tickets. 

When I come back?  They've all tipped 30%.  No notes about my bad service, nothing. I don't even know -- maybe they thought the manager was the only person who could comp stuff?  Why not just ask me to take things off?  Seriously, if they'd said, "Can we get this off the bill?" I would have said "Oh dear, I'm sorry, I meant to take that off!  No problem!" 

By now I'm in serious pain.  Knee is nice and purple, hip starting to protest my weird gait thanks to favoring knee. I start knocking out sidework as my tables slow down but I really, really can't stand up much longer. I end up rolling silver where I can keep an eye on all of them and manager sits down across from me.  

"You know your total for today?" he says. 

"Uhhhhh, I haven't looked at my report yet." 

"You sold $2100." 

That's about 125 covers in our restaurant, probably more if you consider how many kids I had. I'm kinda bummed because it sure as hell felt like more. Thanks, brunch.  

"See me before you go home," and he leaves. 

I finish side work, we take some server snapchats.  When I see the manager, he gives me a bottle of the expensive champagne.  "You probably need this," he says. 

Well.  Alrighty then. 

Note: I could actually use a bottle of bourbon and an ice pack, but it's the thought that counts.  Knee looks better today, hip pain gone. Tonight and tomorrow are going to be...interesting.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cyjf7jr] (score 71, diepte 1 OP) He rings that shit way too much when on expo. 
http://imgur.com/h5cWnLv
[cyjeem8] (score 36, diepte 0) You froze his bell? What does that mean? Like a literal bell? In ice? For funsies?
[cyjp6vw] (score 31, diepte 0) Hope you reported that fall. Even if it seems like nothing at the time always report that shit so if you turn out to be seriously injured it can get taken care of later. 

I hurt my back taking the trash out once, felt like I just pulled a muscle but since then my back has been a huge problem and before that I never had any issues, but I didn't say anything about it when it happened, so I had no case.
[cyjef2o] (score 19, diepte 0) That was a rollercoaster post, hah. Damn, definitely had a harder NYE/NYD double than I did. Worked over the bells but whilst it was packed, it wasn't rushed and everyone was in a good mood. NYD was mainly people drinking the remainder of their wallets away, only a few big tables (two 10's and an 8) and a couple others actually ate food, so we had more servers than needed and I floated onto bar to help the masses get their beers. Tips were low as fuck on NYE, but more than double what I'd expect on NYD for the covers we did. Weird shift!
[cyjfc32] (score 16, diepte 2) That's fantastic
[cyjw15o] (score 15, diepte 1) The restaurant should have a doctor or some kind of medical group designated as the WC provider in case of an injury. Employers pay for that insurance, so employees should use it when needed. 

OP: Find out from your manager or the board where all the documents are posted who the provider is. Get appointment to be seen to make sure that you don't have any serious damage, especially to your knee.
[cyjszde] (score 13, diepte 0) As someone else mentioned, get that checked out right the eff now. I think you have 48-72 hours from the time of injury. Don't want that to bite you later in life.

But, damn, I remember those days, and I don't miss them :)

Happy New year!!!
[cyjfyyr] (score 10, diepte 0) Liquor samples!? What is that I have never heard of a place doing that's
[cyl15z7] (score 9, diepte 3 OP) OP doesn't smoke weed because shit makes me way paranoid and then I binge-eat Taco Bell.  I wish I was joking.
[cyjgtqi] (score 7, diepte 2) Awesome.
[cyjjxic] (score 6, diepte 2) I can't stop laughing!
[cyl1mji] (score 5, diepte 0 OP) Update: Reported injury, saw company doc, x-rays look okay, swelling is WAY better. Told to keep an eye on the knee and immediately report any ongoing issues. Thanks for the advice to see the doc -- I am terrible at getting physical health problems taken care of.  Given how much my psych meds cost, I expect them to render me invincible, honestly, and I freaking loathe the doctor.
[cyk0nhb] (score 4, diepte 0) Ah yes the bell! What a great story!
[cyl1is6] (score 3, diepte 1 OP) We do beer samples and sometimes tiny tastes of liquor if they are having a hard time deciding on something.  If a guest tells me that they've never had Scotch before, they don't like black coffee or espresso or heavily hopped beer and they want to try, oh, say a Laphroig 18 -- I'd rather give them a tiny tiny taste than throw out a whole pour after they refuse to pay for it.  (Note: not everyone who likes Islays likes those other things, but there does seem to be a strong overlap between espresso/hops drinkers and Islay fanatics.)
[cyl1nmf] (score 2, diepte 1 OP) Done, thanks!
[cyl1n3z] (score 2, diepte 1 OP) Done thanks!
[cyl4stx] (score 2, diepte 1 OP) It's the 2008 Pierre Gimonnet et Fils. In the grand scheme of things, this isn't very expensive -- retails around $80 so it probably cost the restaurant around $40. In all honesty, though, I had some (much cheaper) NV Voirin Jumel at a friend's house that was awfully good. It seems like we can get it around here at about $40 a bottle, and if I was buying wine retail, that's what I'd get.
[cykz4hj] (score 1, diepte 2) LOL!
[cyk2xum] (score 1, diepte 1) Probably not the place where OP serves, but The Brickyard in New York City (little gastropub on 9th Ave between 52nd and 53rd streets) does samples of their beers, at least. :)
[cyklnv7] (score 1, diepte 0) The wine nerd in me wants to know - What kind of champagne?
[cynz8jm] (score 1, diepte 1) Glad to read you're doing okay. This was the one bit of story I thought was missing!
[cykyg07] (score -5, diepte 2) OP probably smokes weed, like all servers ever, and will get piss tested if she reports anything.

=== THREAD 67y88a ===
SUBREDDIT: r/Disneyland
DATUM: 2017-04-27  SCORE: 45  REACTIES: 22
TITEL: Technical challenge of audio in "It's a Small World" stumps me.
POST (source_id=post):
I'm an audio engineer, and IASM **had** a technical challenge that I simply cannot figure the solution to. The solution today would be relatively simple, but I took the ride when I was a kid in the '70s, and it was the same...and I have no idea how they pulled it off.

There is a basic music track that plays in all locations. There are also variations that play locally, i.e. singing in different languages, drums, sound effects, etc. When you take the ride, there's no apparent loss of rhythm, which suggests that the basic music track is coming from a central location. This location must also be sending a synchronization signal to the local areas which keep the local variations in sync with the main rhythm. I know from experience that electronically synchronizing just *two* analog tape machines in the late '80s was expensive and often problematic...synchronizing dozens or so would be insane.

Which leads to the possibility of mechanical synchronization like film dubbers, which use sprockets to maintain sync. Having dozens of film dubbers locked together is equally expensive and probably not possible for all practical purposes, yet this is the only possible solution that I can think of. You had to have loops of magnetic tape that were all exactly the same length it terms of feet and frames, and have them all mechanically linked at a central location...with the various signals sent out to their respective speakers. 

I'm not even going to mention how much having everything on continual loops would compound the problem...and the fact that it had to run reliably for 10 hours a day, every day. 

All this in the '60s, when The Beatles were recording Sgt Pepper on 4 track analog. I have no clue how they did this, and I'm pretty good at figuring stuff like this out!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dgu6c8g] (score 25, diepte 0) This old [Wired article](https://www.wired.com/1998/03/disney-3/) has some information about audio at the parks but it is a bit old from 1998. It may prove interesting to you. 

This [Micechat](https://discuss.micechat.com/forum/disney-theme-park-news-and-discussion/disneyland-resort/8472569-small-world-tick-tock-etc) message board post talks about the tick tock clock sound not the ride songs but it is also interesting as well.
[dgu7np6] (score 22, diepte 0) NSFM I am an ex cast member from the early 80's.  I had the fortune to have met several of the sound people there.  The sound systems for the park, even then were amazing.  I never got to see the room that controlled Small World, but I did see the one under the Tiki Room.  Many many banks of older computer controlled systems.  

I found this website with a video showing some of the gear used in this attraction.  Maybe it will help.

http://entertainmentdesigner.com/history-of-theme-parks/disneylands-enchanted-tiki-room-and-the-invention-of-audio-animatronics/
[dgu7lvh] (score 8, diepte 0) Multiple tracks of audio playback was key to may of Disney's early technical successes. Audio-animatronics used channels of audio to drive individual motions in a figure. Those motions, combined with audio, created the illusion of realism for characters like Abraham Lincoln.

My guess is that's the same tech that drove the myriad audio tracks in iasw.

The idea of the audience providing the crossfade between multiple tracks is insanely impressive. And today they tackle that same problem with parade floats, where the floats and the surroundings are creating a single soundscape that changes dynamically based on exactly where you're at in the viewing area.

There was also an Imagineer that talked about it for Toy Story Mania. same basic idea of every single gameplay area in being in sync so that, even as styles differed, the rhythm was never lost from one to the next.

It really is impressive.
[dguqc57] (score 7, diepte 0) I worked on iasw back in the 90s. I can't remember whether it was analog or digital, but I do remember there being 20 or 30 tape decks stacked in two columns. Each deck was labeled for the area it covered. Underneath that was the woodblock with a microphone for the ticktock. They had recently switched that to a recorded source. Sorry I can't remember more.
[dgu86qb] (score 6, diepte 1 OP) The ride was built in 1964, at which time 4 track was state of the art, and synchronization was still way off in the future. Even if you *could* sync multitacks back then, actually doing so in a daily environment (with tape loops!) is mind boggling.

I have a department head who used to work there, I'll see if he knows!
[dgu948r] (score 6, diepte 2) Interesting. How'd they sync the movements for the Abe figure then?

Some quick Googling says it was 35mm film tape with audio signals laid down on it.

Sounds like they might have used larger tape substrate that stored multiple channels and were read by a series of heads instead of a single head.

That'd all but guarantee sync.
[dgv81pr] (score 5, diepte 1) > US$42 a day ($34, if you're 9 or under) gets you at one of the theme parks 

*sobs quietly*
[dgucz79] (score 5, diepte 5 OP) I work for a very large video game company, and am in charge of the creative and technical aspects of all voice files. I used to do sound design for movies, and before that music engineering.
[dguaceh] (score 3, diepte 1 OP) OOO thanks!
Edit: They used recorded electronic tones that would cause certain reeds to vibrate, which would close an electrical circuit. Amazing.
[dgyrhqz] (score 2, diepte 2) I even remember back in 2008 when we got our first annual pass, it was like $380 for a premium pass

Now it's over $1000 :(
[dgu9j8n] (score 2, diepte 3 OP) Yeah, those are film dubbers, and having *one* for Abe is expensive, but doable. I believe the last film dubbers that used 35mm mag were 6 tracks...that's what they used at Skywalker Ranch until they were finally replaced with digital. Total pains in the ass to run and maintain, but they sounded great.

Just from memory, you'd need a few dozen of those for IASM, functioning all day, with the tape looped. I would say that's wildly impractical to the point of being impossible but I can't really think of any other solution!
[dgu9kgy] (score 2, diepte 2) To my knowledge the music never turns off. Unless something happens like a power outage, they kept it running. Sync it once and forget about it type of deal
[dgua1y7] (score 2, diepte 3 OP) Well, you have to turn it off sometime...the machines will go down at some point. Besides, the tape is shedding oxide continuously, and you have to replace the tapes..and clean all that oxide off the tape heads!

Nowadays it's easy, since you can have a single Pro Tools rig running 128 tracks looped all day. Heck, I can do that on the machine I'm typing this on (and I do!)
[dgw6wst] (score 2, diepte 7 OP) Perhaps, but what I'm most proud of is the fact that I got to name two songs by Brian Eno.
[dguvd3f] (score 2, diepte 1 OP) No problem, thanks for the reply! The challenge of doing that in the 90s is hard enough, how they did it in the 60s blows my mind.
[dgwh13u] (score 2, diepte 0) I don't know anything about the actual audio, but I was always told that they never shut the ride down and let the audio run through the night so it's less hassle to start it back up.
[dgx6auj] (score 2, diepte 0) I worked in the park about 15 years ago and they were doing most audio on DAT. They were experimenting with solid state drives for short audio (like announcements). It was really advanced for the time so I imagine the type of technology used was in line with the Fantasound mult-track sounds used for Fantasia in theaters. They were able to do 6 tracks in 1939 so by the 60s I'm sure the technology had progressed.
[dgu8ap5] (score 1, diepte 1 OP) Thanks!
[dgucu0m] (score 1, diepte 4) Maybe periodically they replaced the tape and tried to resync it? 

And now I wonder what you do for a living XD
[dgvz9db] (score 1, diepte 6) Have I ever seen your name in the credits I'm not allowed to skip?
[dgub04p] (score 1, diepte 2) Anytime.
[dgxo9np] (score 1, diepte 1 OP) OK, so it sounds like they must have been using perhaps ten 6-track 35mm mag film dubbers, mechanically synced, running 24 hours a day on loops. 

That's *really* impressive.

=== THREAD 1uzrwx8 ===
SUBREDDIT: r/Fibromyalgia
DATUM: 2026-07-18  SCORE: 2  REACTIES: 0
TITEL: your remedies for fibro + hEDS that are not cannabis or Cymbalta
POST (source_id=post):
hi y’all, i’m wondering what is helping specifically your pain and sleep (for fibromyalgia only or comorbid with hEDS) that isn’t cannabis or Cymbalta? i have comorbid bipolar disorder so those two are not options for me because they really negatively affect my mood. i was a chronic stoner for years and it definitely helped my pain, but it just wasn’t worth the way it impacted my mental health, but i do miss the relief it gave me and the fact that it wasn’t a pharmaceutical remedy.   
things that have helped to some degree so far have been a PT who also has hEDS to guide me in stabilization exercises, vitamin D, electrolytes, resting when im flaring, trauma therapy, adding extra cushioning to my bed/car, jellibend/copper compression wrist braces, comfy and supportive shoes, lidocaine patches, cutting out alcohol and caffeine other than teas, eating a balanced diet, trying to better understand my body’s limits and developing a safer range of motion (with my PT), and staying well hydrated. im also taking nightly 300mg gabapentin which i honestly can’t tell if it’s still doing anything and 5mg cyclobenzaprine as needed for muscle pain which i think helps moderately with stiffness but not any other joint/skin/nerve etc inflammation or pain. my pain and sleep have definitely improved, but im still in daily pain with debilitating flares at times and i have trouble falling asleep (its currently 3am lol) and i almost never wake up feeling rested. any and all additional suggestions that you’ve found help you are welcome!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

=== THREAD 1fes3hq ===
SUBREDDIT: r/Hypermobility
DATUM: 2024-09-12  SCORE: 2  REACTIES: 0
TITEL: Compression Gloves!
POST (source_id=post):
(Cross posted from the EDS sub, my apologies if you see this more than once)

Hi friends! 

I’m on the market for some effective compression gloves.

I used the copper fit menthol ones in a pinch, I like the fact that they support the wrist and go up the fingers. I definitely need something a little more advanced tho.

I would prefer fingertip-less gloves, but also need the support on my distal phalanx joints so if that’s a big ask I will settle for full gloves. Im on a budget, but can save up a bit of money if the product is really worth it. 

Please share your compression glove experiences and product recs! I’m in California USA if that helps.

🩼♿️❤️

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

