# Label-batch batch_0004

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
Schrijf het resultaat naar `batch_0004.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(6 threads: 1nid7uh, 1n5vbte, 1n8igqz, 1n89l01, 1exo1sr, 1dyb8hx).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1nid7uh ===
SUBREDDIT: r/Mortons_neuroma
DATUM: 2025-09-16  SCORE: 20  REACTIES: 13
TITEL: How surgery went for me
POST (source_id=post):
I had a painful neuroma in my right foot for more than 10 years. Cortizone shots didn’t help. Conservative measures did not help. It got to where I could only wear hokas or oofos, and even then sometimes it would be painful. I could never predict on a day-to-day basis whether it would be a good day or a painful day. 

Finally had the surgery in July. Dorsal approach.  The surgeon said I should be recovered in six weeks. I was not! I’m a teacher, so I had to go back to work 4 weeks out. On my feet pretty much all day and it was terrible. from weeks 4 to 8 I had significant pain, limping, and difficulty functioning. Very painful nerves all over my foot. It felt like I had skinned my foot and it was bleeding, but obviously it was not.  

Went back from my postop and he recommended physical therapy. I hate physical therapy, but I have to agree it helped. I was able to get my range of motion back, regain a normal gait in walking, and figure out what to do about nerve desensitization. 

Right now I am 12 weeks out and I’d say I am 90% recovered in foot function.  I can walk without limping. As far as nerve desensitization, I still have a way to go, but I can see that there is slight progress every week. 

I am happy that I had the surgery.  It is amazing not to have that neuroma pain anymore.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nei0ihv] (score 5, diepte 0) Thank you for sharing your experience and ultimate satisfaction with the surgery despite the challenging recovery. I’m scheduled to have it in a few weeks after three years of trying conservative methods.
[neifpvx] (score 4, diepte 0) Thank you so much for your post. It's great to know that the physical therapy helped. I hate doing it too, for my other medical conditions. 

I'm trying to manage my MN, but am struggling after a couple of years.

All I can wear is UGGs in the winter, Birkenstocks in the summer, and trainers with a wide toe box (I found Nike court Traditition, work well) with my MN  insoles in. Everything else is really painful. 

All my Skechers are unwearable, because my feet can't cope with soft, springy sole shoes at all, even with my MN insoles. I miss my pretty shoes.
[nej9zc0] (score 3, diepte 0) Thanks for sharing glad your getting better! What does physical therapy involve?
[neoat6p] (score 2, diepte 1 OP) I hope it goes great!
[neoawgo] (score 2, diepte 1 OP) I understand! I was able to wear my hiking boots last weekend, which I hadn’t been able to wear in 10 years. That was very encouraging! I’m hoping I can get to my abandoned pretty shoes soon.
[nh53l44] (score 2, diepte 1) You mention Uggs. I suspect my Ugg slipper boots were the cause of my neuroma. I think the firm sole that didn’t bend and tight inside formed it. I stopped wearing them now. Never had problems before I wore Uggs.
[neob19x] (score 2, diepte 1 OP) A lot of range of motion and stretching exercises, which I could totally do at home, but I won’t. The part I really didn’t like was nerve desensitization, where they were doing scar massage, and rubbing my foot to get used to the sensation of being touched. Nerves are so weird!
[nepcbjo] (score 2, diepte 0) Thanks for the post. I have a painful Morton nueroma on my right foot between toes 3 and 4. Cortisone shot didn’t work and neither did orthotics. I was literally scheduling my surgery and I chickened out due to recovery concerns. I’m going to try cryo ablation first. I know the success rate is in the 70/80 percent range, which is good but not as high as surgery. I do believe recovery is much easier. I have read some cryo ablation recovery have been tough for some people. Hopefully mine goes well. Best of luck with your recovery.
[nep95ef] (score 1, diepte 2) Nerves are indeed super weird! I have a MN now, but about 20 years ago I had surgery on my knee where the surgeon accidentally cut a nerve. I had to do physio therapy to learn how to walk again but never had the damaged nerve addressed. I hated the sensation of being touched anywhere near my knee for a long, long time. It's only in the last few years that I can touch my own knee without feeling like I want to be sick.

I'm glad to hear your surgery worked, OP! Best of luck with the continued recovery
[nes6ni5] (score 1, diepte 3 OP) Omg I get it!!!
[nejxqme] (score 1, diepte 0) I have orthotics, Altra Torin shoes (wide), Birkenstocks and Chacos that I wear religiously.
[neob4za] (score 1, diepte 1 OP) Thank goodness there are some shoes that accommodate MN!
[nephbb1] (score 1, diepte 1 OP) I chickened out for 2 summers on mine too! Recovery has been tough for sure, but it’s worth it IMO.
[nirya60] (score 1, diepte 1) I’m a week out from surgery and chickening out too. It seems they don’t fully describe the extent of the recovery. Ugh…I get it & good luck with the other approach!
[nis6636] (score 1, diepte 2) Thanks, I was supposed to get the cryo last week but was ill. I have it scheduled for Monday.
[nepz641] (score 1, diepte 0) I'm 68 with lumbar scoliosis. I developed MT last year, and it lasted around two months, then went away. The doc said it was a result of damaged nerves from my back problem, causing issues, but after looking at subs here and elsewhere, it seems it's not just folks with back issues that have this problem.
[nfb5ldz] (score 1, diepte 0) Just had surgery on mine in between 2nd and 3rd web space 2 days ago. Had surgery on my left foot almost 11 years ago now, I remember it took me a little while to feel better after my left foot. I'm supposed to go back to work in 2.5 weeks (I'm on my feet all day) and I'm nervous I won't be ready. 😭
[nhfixo5] (score 1, diepte 1) I hope you're feeling better soon. For the one on your left foot that you did 11 years ago… How does it feel today? And was it a neurectomy that you had?… Where they cut out the neuroma?
[nhfiyri] (score 1, diepte 1) I hope you're feeling better soon. For the one on your left foot that you did 11 years ago… How does it feel today? And was it a neurectomy that you had?… Where they cut out the neuroma?
[nhh8xne] (score 1, diepte 2) Yes it was a neurectomy! 11 years later I have 0 pain in that foot, can wear any shoe I want, and activity has never bothered me. I still have numbness in between my 3rd and 4th toes, and sometimes it still feels kind of weird, but I went from being in so much pain to 0 pain and I'm so happy 11 years later I still remain pain free!!
[nhh93pw] (score 1, diepte 2) I'm honestly so glad I had the surgery in my left foot. I hope I have the same luck with the right!
[nhfib88] (score 1, diepte 0) what kind of Physical therapy, did they do for you?

=== THREAD 1n5vbte ===
SUBREDDIT: r/PlantarFasciitis
DATUM: 2025-09-01  SCORE: 22  REACTIES: 12
TITEL: What worked for me after 2.5 months
POST (source_id=post):
I have had PF since June while training to leave for the Army. It came on out of nowhere and totally crippled my ability to walk let alone run. First I’ll list what I tried in order and what I think has finally helped. Maybe someone else can benefit from it. 

(1) basic stretches. I would kill my toes back to my knee, hold it there for 20-30 seconds then release. Almost like a workout. I had an Arch rocker (highly recommend for runners in general) which helped stretch. 

(2) ibuprofen - started with 400mg each time. Helped with pain a bit but I still was limping on every step.  Towards the end I increased to 600-800 mg (3-4 Advil) every 8 hrs. 

(3) Meloxicam - helped a bit but still it still come back

(4) Cortisone shot - that puppy hurt like hell and I’m definitely not afraid of needles. They did one needle multiple times above and below the tendon to try and spread it out. Holy hell.  Going for my second tomorrow. 

(5) Night splints. - I had a soft version which was ok but I got a hard one and that was a lot better. Definitely gave some relief and help. I could only sleep with it on for 2hrs at a time. I can’t sleep normally anyway so adding that thug didn’t help. 

(6)Calf massage and exercises. I read on here about it and I think that really began to help. I’d have a dumbbell in my hand and one foot in the air and did calf raises. 

(7)Turmeric /ginger supplement - I was getting desperate and have 4 weeks until I TDS so I’d try anything. I was even getting ready to try that essential oil BS. I can’t say whether this helped or not but I will say within 3 days of taking it and the higher Advil I noticed a change. Not sure if it’s correlation or coincidence. 

(8)The surprise help was a SB Sox compression socks  got off amazon. I wore that day and night for a week, even lifting, and finally I’m back to running again. Highly recommend a PF compression socks 


Ultimately I think it was a combo of the exercise and massage, compression socks 24/7 and the higher levels of exercise by proven that worked for me. I ran the other day 2 miles with some discomfort that night and then today I did a faster 1 mile and only very minor discomfort. Hopefully this post helps someone.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nc63dq6] (score 2, diepte 3 OP) Amazon.
[nc1gr26] (score 2, diepte 1 OP) I was joking about the oil. Sorry.
[nbvomt3] (score 1, diepte 0) Did you wear full over-the-calf compression socks or PF ones that come up to the ankle that only compresses the foot? 
I’ve only tried the later but I’m paying my calves more action now.
[nbvrc6o] (score 1, diepte 1 OP) It stopped at My ankle. I don’t like contracted feeling so I could handle the full ones. This was one I could wear, put a sock over it and exercise, walk around and even go to work.
[nbw257x] (score 1, diepte 2) I can't handle the ones on calves as well, I don't know why
[nby40e2] (score 1, diepte 2) Where did u get the PF socks from please? They helped?
[nc6pbyf] (score 1, diepte 4) Ty!
[nbvrog3] (score 1, diepte 0 OP) I meant to add superfeet PF insert soles. As something I tried. I have them in. My running shoes but that’s only time I use it. I had them in regular shoes and didn’t notice  much help. 

I went from running 9 miles every other day to sad limping around the house fast.
[nbwv35x] (score 1, diepte 0) I have had it a month and a half now and reading this gives me hope!! I am doing pretty much everything you have mentioned BUT the supplements. What milligram dose did you use??
[nbwwblc] (score 1, diepte 1 OP) It was the Turmeric and Ginger bottle on Amazon by natures nutrition 1500 turmeric mg. I can’t say it definitely made a difference but after 2 months of this I would try anything. It seemed to all start to break free randomly.
[nc8ttbh] (score 1, diepte 2) Just be careful with Tumeric supplements, especially when they include black pepper. Too much of the active ingredient, curcumin, can cause serious liver problems. Black pepper is added to increase absorption, which increases the risk. I try not to exceed 500 MG per day for that reason. Can't say it's helped my PF, but that's not why I've taken it.
[nc1bko3] (score 1, diepte 0) What oil did you use ?
[nc1rmqp] (score 1, diepte 2) 😄I did use cbd it helped a little . Thanks
[nc1ig5o] (score 1, diepte 0) I have had it for 3 years and tried all the above plus had surgery. Nothing worked and now from the gastritismenius recession surgery a mnth ago I have nerve pain on the top of my foot to my big toe. I see the podiatrist tomorrow for this. Never ends! Im in physical therapy too. Wth.
[nc545rt] (score 1, diepte 0) Does ibuprofen help lower inflammation?
[nc63c1k] (score 1, diepte 1 OP) Ibuprofen (Advil) is excellent anti inflammatory. Tylenol (acetaminophen) is for pain relief too but for plantar ibuprofen is the best. When I had a back injury they had me take 800mg ibuprofen (4 Advil) 3x a day and then Tylenol in between for breakthrough pain. I did the same for this at it’s worse. So i would use the 3-4 Advil when I woke up (eat with it for sure) then Tylenol 3hrs later. And keep that rotation going if needed. Ibuprofen can be tough on your stomach while Tylenol is tough on your kidneys. So people with issues really need to check with their doctors if they can handle it. Also you don’t want to be doing it long term. I’m not a medical doctor so as I said, when dabbling above the typical OTC dosage you may want to ask your PCP.
[nc7jhr0] (score 1, diepte 0) Those tight socks suck. Too much constriction.

My PF pain is gone( still have tightness but stretching before getting out of bed takes care of that..
Took me 2 weeks.....I picked up a pair of oofos recovery sandals, cheap Ktape from CVS and a jar of tiger balm.  I already had a pair of Hoka Bondi 9s in wide toe box.

I never walked barefoot the first week and taped my feet  the mornings at night I would massage the tiger balm into PF area (first 5 days I couldn't run the heel area much as it was Soo much pain). Only walked in house wearing the oofos.. with everything above it's just down to tightness in the morning but no pain. I'm on my feet 12 to 16 hours a day.
There are lots of other shoes and recovering sandals out there. Just posting what worked for me.
[nlin7g0] (score 1, diepte 0 OP) Just an update 2 months later - it returned and I’m back to limping again. Trying PT. THE Cortisone shot must have just masked it for about 6 weeks…
[nni296h] (score 1, diepte 0) I'm currently on my fourth day of meloxicam 15 (for 30 days). I am stunned at how much it is helping me. I do feel slightly icky and am fatigued for side effects, but I am standing and walking for most of the day in my decent PF friendly shoes or Oofos with only reminder of pain if I do too much and then I stop and ice. I am sleeping more comfortably as well. 

I do understand that there's an injury there, and that meloxicam is very strong and that in a way it is masking things, but also has reduced swelling in there. I have to be mindful not to, as they say "fuck around and find out" or I'll be 😢.

I am over the moon! I am starting PT, and this level of relief will allow me to make good use of my therapy. Still wearing a felt/velcro splint at night too.

=== THREAD 1n8igqz ===
SUBREDDIT: r/bunions
DATUM: 2025-09-04  SCORE: 2  REACTIES: 12
TITEL: Boot after surgery
POST (source_id=post):
What do you wear pants-wise with a boot?  Do you need to cut off the pat leg to fit the boot?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ncf9gjf] (score 2, diepte 0) I just tucked my pants in my boot. I didn’t have problems with any type….joggers, jeans, military uniform
[ncfaosb] (score 2, diepte 1 OP) Thanks. I was trying to envision what I would do in cooler weather when I get out to the doctor or wherever.  Its difficult to roll up jeans which I usually wear and shorts wouldn't work this fall for me.
[ncfajo5] (score 2, diepte 0) I tuck mine inside the boot. I’ve been wearing joggers or wider leg pants. Nothing skinny that will squish my foot when putting them on.
[ncfatgt] (score 2, diepte 1 OP) Thanks!
[nchobiv] (score 2, diepte 1 OP) Thanks for the links!
[ncfa488] (score 1, diepte 0) Yoga pants for me, rolled up to the knee. Or shorts, or sleep pants, again rolled up.
[nch428k] (score 1, diepte 0) I wore [these shorts](https://a.co/d/2358dhP) constantly after my recent surgery.  They’re nice and stretchy and easily go over the boot.

I wore [these pants](https://a.co/d/1CgOilK) in the winter and while they don’t go around the boot perfectly easily, they kind of do and they’re very lightweight and stretchy.
[nchxgpu] (score 1, diepte 0) Tuck them in
[nckf8ui] (score 1, diepte 0) I wore wide leg yoga pants and sweatpants that covered the boot.
[nclef12] (score 1, diepte 1 OP) Thanks. I think that will be my go to.
[nclkwim] (score 1, diepte 2) I wear this style often.  They used to have an older version that was loose throughout the thighs as well.  Both styles are very comfortable and allow me to cover my boot.

https://www.jcpenney.com/p/xersion-everrestore-womens-high-rise-flare-leg-yoga-pant/ppr5008450277?pTmplType=regular&geoZip=21201&selectedSKUId=84019000034&facetSelected=color
[ncmem2s] (score 1, diepte 3 OP) Thanks. I really like these.

=== THREAD 1n89l01 ===
SUBREDDIT: r/flatfeet
DATUM: 2025-09-04  SCORE: 0  REACTIES: 11
TITEL: Are people with flat feet not meant for sports?
POST (source_id=post):
I got injured 5 years ago right after I started running, and the pain never went away. I been to countless doctors (including sports medicine) and physios, and they all have been clueless on how to resolve the problem. I wish I never ran in the first place knowing how much chronic pain it would cause

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ncdbphv] (score 6, diepte 0) I’ve had flat feet my entire life. The only sports I can do without pain is biking and swimming. When I was little, all my friends played soccer and I hated it. I remember feeling left out because it simply hurt too much for me to play.
[ncfyl92] (score 2, diepte 1) Hi I am like that, I'm actually somewhat active and do a lot of Hiit and Kettlebells BUT my knees hurt all the time. What do you recommend?
[nck8rk9] (score 2, diepte 2) Hmmm have you gotten an assessment at a physio you trust? Usually you'll likely need to give your knees a bit of a break by lowering activities for a week or so - but more importantly will want to strengthen the area that your knees are likely compensating for. This could be the feet, though if your doing hiit and comfortably a big player may actually be your glutes.  Unfortunately an assessment will probably be necessary to find out what your knees are compensating for - but I recognize not everyone has access. 

If you think its your feet - this talk goes over a lot of information over how our feet should be operating and what's behind strengthening :): 

 https://open.spotify.com/episode/5iVi3arAK9aUyCcFQqBFsL?si=6ynjxQAORWKGhRY_D7jrmw


Glutes are thankfully a little easier to activate if its not due to dormant/weakened feet muscles like im dealing with. For me what took a lot of stress off my knees are clamshells with bands - and bands are gonna be your best friend haha. Clamshells do not look cool haha but I've found they've been the easiest for me to activate and wake up the glutes. Once your knees have a bit of rest and relief - looking to have the glutes take on more of the load in something like the bulgarian split squats would be good! Though the variations of the split squad can target very different areas so try to look specifically at videos to follow that target the glutes. Our bodies generally react pretty quickly btw so in a month or so you should likely notice the difference, otherwise might be good to go back to the drawing board on what may be compensating - usually it seems like hips/glutes/feet/calves(specifically soleus) will have something weaken, and other things tighten/overwork to compensate. Hope you find some relief for your knees 🙏
[nckid9m] (score 2, diepte 3) Thank you for your great answer, I'll study all of the important points you mention.
[nce12pt] (score 2, diepte 0) I’ve had flat feet my whole life and I played basketball, ran long distance, and have been weight lifting since high school. I’m 39 now. When I turned 38, my ankles started hurting every day. I went from doing over 10k steps a day, so 3k. By this summer I was walking with a cane. I had to have reconstructive foot surgery on my right foot, which was last week. The doctor has already confirmed I’ll need it on my left foot also. I asked him how suddenly at the age of 38, my feet stopped working. He said I may have been compensating for my feet all of my life and my joints couldn’t do it anymore. An MRI stated I had a severe deformity on my right foot. My foot always stuck out to the right. I don’t know how I did any of the things I have done in my life with this condition, but it caught up to me. I am hoping I will one day can weight lift again. 🤞🏼
[nce8ljc] (score 2, diepte 0) I have very flat feet like pretty much a -3 arch according to one doctor. I couldn't run for more than 1 minutes before getting pain, so I never did. I focused on sports like cycling, swimming, walking. I will say it sucks cause basically can't do most things I wanna do.

I got my first surgery 7 weeks ago and currently in recovery, hoping this fixes it!

Do you havw custom insoles?
[ncdznad] (score 1, diepte 0) Hi there - flat feet do not inherently mean symptomatic or pain inducing. I've had flat feet all my life and play soccer, volleyball, practice muay thai,    and swim! Soccer is likely a big factor of my flat feet due to cleats haha. There are actually quite a few Olympians with flat feet! However without the arch, a lot of different parts of our body ending bearing the force/tension that our arch generally transfers - and will have to be extra cautious around these joints/knees etc. Taking on that impact. Im sorry your physio/doctors have not been able to help - a lot of traditional places send you straight to orthotics etc. A lot of us have been through the same frustrating process :(( orthotics  which though can alleviate for the short term - can unfortunately weaken further in the long term. Sounds like you likely feel pretty debilitating pain in your feet hey? Usually in the arch itself? You might need to start out with supports but eventually strengthening weakened muscles and reactivating parts of your feet would be an important step as well. And catering those exercises to your current state is really important - there's lots of exercises here i couldn't do!: https://youtu.be/xM4E3pc0lQg?si=UPizm9QFjdp1RpSj

I found precision movements cues helpful! But for example when I started i literally could not wake my pinky toe. If youre having trouble with running/walking it makes a lot of sense- id actually recommend starting out in the pool where your feet have a bit of a safer environment to rehabilitate. I've been where you are - and it feels like you kinda just accept that you cant heal but its not true! You can definitely strengthen back your feet over time - its gonna be slow but I promise you - youre not alone and you can get back on your feet :)
[nce8wl6] (score 1, diepte 0) Your particular issue may stop you playing sports, but lots of pro athletes have flat feet. Usain bolt, the fastest man on the planet, has flat feet
[ncesjh7] (score 1, diepte 0) I believe Kevin Durant, LeBron James and Michael Jordan have flat feet
[ncg2p5p] (score 1, diepte 0) The podiatrist I saw actually said lots of basketball players have flat feet. I’m not sure if that’s true or not but he pointed out that Kevin Durant has pretty bad knee pronation

=== THREAD 1exo1sr ===
SUBREDDIT: r/thenetherlands
DATUM: 2024-08-21  SCORE: 15  REACTIES: 54
TITEL: Waar wandelschoenenwinkel voor brede voeten
POST (source_id=post):
Ik heb al jaren gedoe met podotherpeutische zolen, blaren, te smalle (wandel)schoenen en pijn in mijn voeten. Tegelijkertijd ben ik een enorme fan van wandelen.

Ik zoek daarom een winkel in Nederland met een heel breed assortiment schoenen waar mensen werken die je echt goed kunnen helpen als je brede voeten en podozolen hebt. Een specialistische winkel zeg maar. Mijn podotherapeut benoemde al dat er in Duitsland veel van dat soort winkels zijn maar kon niks specifieks noemen.

Waar moet ik heen? En waar hebben jullie goede ervaringen (of andere tips)?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lj82rvf] (score 29, diepte 0) Ik ben heel blij met de Zwerfkei in Woerden. Ik weet echter niet of zij zo'n specialisme hebben dus zou ze even bellen. Ze hebben een heel breed assortiment, nemen de tijd en hebben een soort terreinpad waar je de schoenen kan proberen
[lj867th] (score 24, diepte 0) Een aantal wandelschoenen makers hebben speciale breedtematen: Meindl, Lowa, Merrel en Hanwag zeker. Veel wandelschoen speciaal zaken hebben deze niet standaard op voorraad, maar kunnen ze wel bestellen.

Veel webshops kan je de breedtematen wel direct bestellen.

Meindl heeft ook hoge kwaliteits [stadsschoenen](https://www.identity-leder.de/) met modellen voor verschillende breedtematen.

Lowa heeft ook werkschoen (chemisch bestendig, teenbescherming) uitvoeringen met breedtematen.

Een andere tip voor werk/stadsschoenen zijn [Redback](http://aussieboots.nl) chelsea boots: De AU/UK halve maten zijn even lang als de maat afgerond naar beneden (dus bijv. 11,5 zijn maat 11) maar wel extra breed.


Zie ook https://bredevoetengids.nl/
[lj8hmcw] (score 12, diepte 0) Ik heb wijde voeten en zweer bij Meindl, bijv. te koop bij Bever.
[lj880gx] (score 10, diepte 0) De Bever aan de Duwboot in Houten meet je voeten op met foto's en dergelijke, waarna de computer dan een aantal suggesties uitspuugt. Elke Bever doet dat, maar die in Houten is best groot en heeft een stevig assortiment. Goed geïnformeerd personeel en ze zijn er daar ook niet vies van om een concurrent aan te raden als zij zelf niet hebben wat je nodig hebt. Dat zou een startpunt kunnen zijn?
[lj8991v] (score 7, diepte 0) Als Arnhem in de buurt genoeg is: (of je kunt online bestellen, maar da's natuurlijk tricky als je niet weet wat je moet hebben)
https://www.barefootandmore.nl/

Barefoot schoenen zijn bijna per definitie ook altijd wat breder aan de voorkant (de hele filosofie van barefoot is dat de schoen de natuurlijke voetvorm ondersteunt in plaats van de voet te forceren in wat door de jaren heen als normaal is bestempeld)
[lj9m1wi] (score 6, diepte 1) Zwerfjkei is keigoed. Heeft ook een parcours voor het uittesten van de schoen.

Nog een tip voor vrouwen met brede voeten: kijk in de mannensectie, die schoenen zijn relatief breder :-) Jongens met smalle voeten raad ik ondertussen het omgekeerde aan.
[lj865tz] (score 6, diepte 0) Van Camp in Lunteren specialiseert in moeilijke voeten, en heeft een hele kelder vol wandelschoenen.
[lj9myn1] (score 6, diepte 1) Heb jij wel geluk gehad met het Bever personeel!

Tegenwoordig loopt daar veel wat geen idee heeft..
[ljagaeh] (score 6, diepte 1) Ik sluit mij hier helemaal bij aan, wel een klein advies voor mensen die dit overwegen: dit zijn je voeten niet gewend en het duurt een tijd om eraan te wennen. Reken op 1000 km wennen minimaal,  voor de ene persoon meer voor de ander minder. En dat is met het af en toe terug gaan naar gedempte schoenen. Het is een heel proces dat je serieus moet nemen.

Je voeten gaan een vrijheid als nooit te voren ondervinden, in de breedte en later ook in de lengte. Spieren die je al jaren niet gebruikt worden onder protest geactiveerd. Ja dat doet pijn en ja dat kan blessures opleveren. Barefoot is een delicaat proces, heeft tijd nodig en is alle moeite waard. 

Bron: ik loop alleen op barefoot schoenen (of op blote voeten). Dat is alles, verder geen ben ik geen deskundige.
[lj9mnth] (score 4, diepte 1) In Amsterdam zit ook een goede barefoot schoenenwinkel: De Trek Barefoot. Heerlijk type schoenen.
[lj8re4j] (score 4, diepte 1) Hier ook iemand meteen brede voorvoet. Meindl comfortfit all the way. Gekocht 1 week voor vakantie, tijdens vakantie meerdere wandeltochten t/m 10 km. Geen blaren geen pijn, alleen een tevreden gevoel.
[lj8okcu] (score 4, diepte 0) Soellaart in Haarlem.
[lj9ffdn] (score 3, diepte 1) Toen ik mijn schoenen kocht hadden ze een groter assortiment dan bever in brede schoenmaten. Ik weet niet hoe het nu is.
[lj9kcfr] (score 3, diepte 1) Absoluut 100 punten voor de Zwerfkei, die hebben het breedste assortiment van NL
[ljaefgk] (score 3, diepte 2) In Hoorn zit er ook een, en dat is ook een aanrader.
[lj8qc7i] (score 3, diepte 0) In het voorjaar ben ik bij Bever sport geweest en daar heb ik op een plaat/machine gestaan die een 3d analyse van je voet maakt en op basis daarvan kunnen ze specifiek schoenen voor je adviseren.
[lj947a4] (score 3, diepte 0) Soellaart in haarlem
[lj9o2lk] (score 2, diepte 2) Volgens mij doen de verkopers dat zelf al als je aangeeft dat het nog niet past. Ik heb me daar prima laten helpen. Zelf aangeven wat in het verleden goed zat en waar ik naar op zoek ben en ze komen met allerlei modellen aanzetten
[lj9qp73] (score 2, diepte 3) Geloof ik wel ja. Ik heb hele brede voeten als vrouw en kijk daarom tegenwoordig gelijk al bij de mannenrekken. Niet alleen bij wandelschoenen ;-)
[lj8c6wm] (score 2, diepte 1) idd, kan hier (met maatje 49.5 en een brede voet) goed slagen.
[ljckoyc] (score 2, diepte 1) Huh? Ik ben enkel een soort van gelobotomoniseerde zombies getroffen bij Bever, en nooit enige meting gehad. Toegegeven, twee uur rijden bij Houten vandaan. Mazzelaar!
[ljcx4ot] (score 2, diepte 2) Op het Gelderlandplein in Amstelveen!
[ljcres6] (score 2, diepte 2) Tilburg
[lj95p96] (score 2, diepte 0) Outdoor XL in Barendrecht- daar ben ik toen heel erg goed met m’n wandelschoenen en de juiste fit geholpen.
[lj9m3dy] (score 2, diepte 0) Ik hoorde dat René Vos in Gorssel (en ik zie online dat ze ook in Apeldoorn zitten) gespecialiseerd is in wandelschoenen voor niet standaard voeten.
[ljb23yk] (score 2, diepte 0) Rene vos in Gorssel
Woon daar al 20 jaar niet meer, maar koop daar nog steeds mijn wandel-en trekking schoenen
[ljacub5] (score 1, diepte 1) Zwerfkei is echt een topwinkel, voor veel meer dan alleen wandelschoenen. Qua schoenen ben ik zelf fan van de breedtematen van Hanwag, maar ik heb geen hele brede voet.
[lj87ndz] (score 1, diepte 0) Ik heb ook brede (voor) voeten en ik loop vaak in *Altra* of *Topo Atletics*, deze hebben een brede neus in de schoen. 

Op het moment de Altra superiors, wel wat minimalistische wandelschoenen:
https://www.bergfreunde.nl/altra-superior-6-trailrunningschoenen/?aid=2e28c2b6e1f0f259b46144fd5a18367e&pid=10004&bfgb=false
[lj8ck90] (score 1, diepte 0) Schutrups in Exloo is ook een begrip op dit gebied.
[lj8gkq2] (score 1, diepte 0) Afhankelijk van je locatie nog enkele extra opties:
Hoevens schoenen in Zaltbommel
Klinkenberg in Geldrop
[lj8h5e3] (score 1, diepte 0) Kom je niet in aanmerking voor orthopedische schoenen?
[lj8hio3] (score 1, diepte 0) De kievit in Hengelo (mogelijk ook andere plekken). Heb ik die van mij afgelopen jaar gekocht na jaren maar slippers en sneakers afwisselen tijdens tochten (ik had oprecht een tas met verschillende schoenen mee). Deze zomer nergens last van gehad. Ik heb ook geïnvesteerd in wandelsokken van Falke op advies van de winkel. Echt heel tevreden! Mijn schoenen zijn van Lowa.
[ljcn43g] (score 1, diepte 1) Ik loop al jaren met mijn brede voeten op Meindl, wil niet anders meer. Als 1 paar op is, na een jaar of 2 intensief gebruik, bestel ik gewoon weer een paar nieuwe, nooit problemen mee gehad. 

Ik zou alleen willen dat ze van Meindl ook schoenen met stalen neuzen maakten.
[ljcr80v] (score 1, diepte 1) Welke Bever is dat precies? Volgens mij hebben/doen ze dat niet overal.
[lj8l2w4] (score 1, diepte 0) Voor breedtematen ging ik vroeger naar Krisman in Zwolle, al weet ik niet wat het assortiment aan wandelschoenen is (kun je online vast vinden). Verder zit er in Amsterdam een winkel die specialiseert in grote maten (47+ voor mannen, voor vrouwen kleiner, maar weet ik niet precies), die hebben vast ook wel brede schoenen (wel alleen in grote maat).

Afhankelijk van hoe breed je voeten zijn kun je ook óf opzoek naar specifieke merken die standaard wat breder vallen / breedtematen hebben, óf zelfs overwegen je schoenen op maat te laten maken. Ik weet dat mijn zusje dusdanig brede voeten heeft dat ze haar schoenen op maat laat maken, dit wordt vergoed door de verzekering, maar kost je wel je volledige eigen risico.
[ljcr9hl] (score 1, diepte 1) Welke vestiging was dat?
[lj8tmm7] (score 1, diepte 0) Voor wandelen heb ik Meindl via Bever online. Gepast, mee gelopen en daarna meteen een 2e paar besteld.

Voor sneakers ben ik een fan van New Balance, de 574 is breder dan normaal. Alleen die vallen vrij klein. maat 46 komt overeen met 11,5
[lj8xma3] (score 1, diepte 0) https://www.houseofoutdoor.com/ in Maarssen. Hebben de hele mikmak, kan niet garanderen dat je daar slaagt, maar kans is groot.
[lj9hg4p] (score 1, diepte 0) Suggestie voor schoen om te proberen: Lowa Renegade GTX Mid.
[ljchy2a] (score 1, diepte 2) De Lowa Renegate GTX Mid heeft een "wide" uitvoering.
[lja3gvp] (score 1, diepte 0) Weinig hulp, maar... Ik heb irritant brede voeten en orthopedische zolen, en loop op mijn tweede set Scapino-bergschoenen. De eerste waren niet op, maar gejat. Gezien de prijs kan het best wel eens een tripje en een paspoging waard zijn...?
[ljbv4ee] (score 1, diepte 0) https://www.barefootandmore.nl/

Ik heb ook brede voeten maar draag nu niks anders meer dan Vivos. Check de website, ze verkopen schoenen die gevormd zijn als een voet.
[ljby5pl] (score 1, diepte 0) Noorloos heeft veel wandelschoenen/kisten, ook met verschillende breedtematen.
[ljcgtuw] (score 1, diepte 0) In Engeland heb je nog een aantal merken die wandelschoenen op maat maken. Zelf heb loop ik op Altberg, dat is zegmaar de Meindl van de UK. Ze hebben standaard elk model in 5 breedte maten dacht ik en kunnen de leest ook aanpassen. Je moet er wel voor afreizen naar een wandelwinkel de UK om je voet te laten inmeten, maar dat was het mij het meer dan waard.
[ljchm0f] (score 1, diepte 0) Laatst heb ik zelf gezocht naar trailrunners voor mijn wandelavonturen. In mijn onderzoek kwamen schoenen van het merk "Altra" voornamelijk naar voren voor mensen met brede voeten. Wellicht dat je kan kijken waar deze te kopen/testen zijn in Nederland. 

Wat betreft de genoemde winkels kan ik netals vele anderen hier de Zwerfkei en Soellaart aanbevelen. Beiden hebben goed personeel dat erg behulpzaam is.
[ljci2mc] (score 1, diepte 0) Er is een barefoot shoes shop in Arnhem :)
[ljf8b5c] (score 1, diepte 0) Bedoel je hoge berg schoenen? Of zijn trail runners ook goed? Dan zijn Brooks en Altra's breed in de tenen, denk er wel om ze hebben een lage "drop". Dus wel even wennen.
[ljfmvb5] (score 1, diepte 0) Ik weet niet wat er precies wat er met je voeten zijn waardoor je podotherapeutische zolen draagt. Maar mocht je wel gewoon al je tenen hebben en geen of bepaalde misvormingen hebben, dan is mijn advies is om je te verdiepen in barefoot schoenen. Met podotherapeutische zolen gaat dat wel lastig omdat de schoenen breed zijn bij de tenen en en er geen enkel steun is, de zool is velen malen dunner dan reguliere schoenen. Maar je hebt specialisten die je daarin kunnen begeleiden en thuis kun je bepaalde voetoefeneningen dingen.
[ljl9wua] (score 1, diepte 0) Ik heb goede ervaringen bij de https://www.beterlopenwinkel.nl/ mocht die bij jou in de buurt zitten :)
[ljr6pjj] (score 1, diepte 0) Misschien barefoots iets voor jou?
[ljtnxur] (score 1, diepte 0) Bij de bever kunnen ze je voeten scannen en matchen met heel veel verschillende schoenen
[ljcgly9] (score 0, diepte 1) Dat is een schoen met een smalle pasvorm, dus niet aan te raden voor OP. Kijk naar Meindl Comfort Fit of Hanwag Wide / StraightFit Extra modellen als je een smalle hak hebt
[ljci0uw] (score 0, diepte 3) Dat klopt, maar dat stond er niet bij 😉

=== THREAD 1dyb8hx ===
SUBREDDIT: r/thenetherlands
DATUM: 2024-07-08  SCORE: 1  REACTIES: 0
TITEL: Sneaker tips voor zeer brede voeten?
POST (source_id=post):
[removed]

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

