# Label-batch batch_0005

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
Schrijf het resultaat naar `batch_0005.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1b31jc9, wl60y0, 1953eg3, 126jbsk).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1b31jc9 ===
SUBREDDIT: r/thenetherlands
DATUM: 2024-02-29  SCORE: 261  REACTIES: 172
TITEL: Om populisme in te dammen, moeten burgers weer vaste grond onder de voeten krijgen
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ksp85a3] (score 424, diepte 0) Goh populisme en fascisme worden populairder als er meer economische onzekerheid heerst. Wie had dat gedacht
[kspa8ad] (score 188, diepte 1) lijkt bijna alsof er een correlatie bestaat tussen armoede en radicalisering :O
[ksplf34] (score 141, diepte 0) >Hetzelfde geldt voor de PVV: op migratie rechts, maar sociaal-economisch links. 

Had deze mythe liever niet *weer* klakkeloos herhaald gezien, zucht. Verder een goed algemeen punt.
[kspajnh] (score 98, diepte 0) Ik heb het hele artikel nog niet kunnen lezen, maar dit sprong er al wel voor me uit:

>**Er wordt ook vaak vergeten dat de helft van Nederland op het vmbo zit,** dat is een hele andere wereld dan die van het HBO en de universiteit. Dit zijn dus ook de mensen die zich niet kunnen voorstellen dat de PVV onder jongeren groot is. **Juist omdat er geen breder zicht bestaat op de samenleving**, is die hoger opgeleide bovenlaag verbouwereerd over de rechts-populistische winst. 

Het artikel spreekt er niet gedetailleerd over, maar we moeten niet vergeten hoe vroeg dat geïntroduceerd wordt in ons leven en hoe diepgeworteld het inmiddels is. Vanaf het punt dat kinderen in de pubertijd gaan worden ze als het ware gesegregeerd van elkaar. Die opleidingstrajecten zijn in grote mate van elkaar gescheiden en die stromen komen minder en minder met elkaar in aanraking. En ook al heeft het denk ik niet de bewuste intentie om dat te doen, maar het maakt dat bevolkingsgroepen echt naast elkaar gaan leven. En dat heeft denk ik heel ingrijpende, negatieve gevolgen voor de cohesie van een samenleving.

Natuurlijk zijn er uitzonderingen, scholen en dorpen/buurten waar die vermenging wat meer voorkomt, maar ik denk wel dat dat de tendens is binnen de Nederlandse samenleving. En geen wonder dan dat je een dergelijke situatie krijgt als beschreven door het artikel. Die uitzonderingen die er vast zijn zijn dan wellicht een goede kans om van te leren hoe die segregatie voorkomen kan worden. Want dat naderhand rechtzetten blijkt een behoorlijk pittige kluif. Je ziet dat denk ik al in de recentelijk terugkerende discussies over bijv. MBOs meenemen in introductieweken van het HBO en de universiteit. Dat is op zich een klein ding, maar het is denk ik wel een herkenbaar symptoom. Een puist op de algemeen slecht verzorgde huid die de Nederlandse samenleving is, zeg maar.
[kspz09u] (score 85, diepte 1) Zo sociaal-economisch links, dat ze een paar jaar geleden nog een voorstel hadden gemaakt om CAO's niet-bindend te maken en daarmee effectief af te schaffen.
[kspquvq] (score 65, diepte 3) Vooral aan socialisme ontbreekt het steeds meer tegenwoordig.
[kspb3p2] (score 60, diepte 1) Dat is het dus niet. Het is gebrek aan samenhang. Er is een groep die alles regelt en dat regelt op zo'n manier dat ze *denken* dat ze het voor iedereen goed en hetzelfde regelen, maar het in feite alleen voor zichzelf regelt, omdat ze die anderen niet begrijpen. Dan krijg je kansenongelijkheid. Dat is het probleem.

Als iedereen in hetzelfde schuitje zit zou het probleem veel kleiner zijn. Maar niet iedereen zit in hetzelfde schuitje, en degenen die in het zinkende schuitje zitten roepen "help, we zinken", waarna de groep die al aan de overkant is eens op hun bouwtekening kijkt en dan terugroept "nee hoor, jullie zinken niet, we hebben het zo ontworpen dat het niet kan zinken" - en die eerste groep maar hozen terwijl ze inmiddels tot hun nek in het water staan.

Tegen dat soort domheid kun je niet op, en het is ontzettend frustrerend. Zoals ook in het artikel wordt gesteld, de groep die in het zinkende schuitje zit wordt voor dom uitgemaakt omdat ze het lef hebben het o zo goed ontworpen scheepje een zinkende schuit te vinden, maar ondertussen wordt er niet gekeken of dat schuitje niet ook daadwerkelijk aan het zinken is, want "het is toch zo goed ontworpen dus we hoeven iemand die roept dat het zinkt niet serieus te nemen". In het aller-, allergunstigste geval krijgen die mensen dan het advies om maar zwemles te gaan volgen.
[kspca5x] (score 45, diepte 2) Ik ben het niet eens met de stelling dat de regerende klasse denkt dat ze het goed doen voor iedereen. Die lui weten echt wel waar ze mee bezig zijn.
[ksrlhld] (score 44, diepte 2) >Zo sociaal-economisch links, dat ze een paar jaar geleden nog een voorstel hadden gemaakt om CAO's niet-bindend te maken en daarmee effectief af te schaffen.

Zo "economisch links" dat Wilders deze maand nogvoor het behoud van het eigenrisico in de zorg stemde terwijl die de doorslag kon maken.
[kspouk5] (score 39, diepte 4) En dan stap je dus rechtstreeks in de val die de lobbyist en spindoctors willen opzetten: dat de keuzes die nadelig uitvallen voor mensen aan de onderkant van de samenleving vooral komen van 'links' en vanuit milieuwetgeving. En dat de 'regerende klasse' of 'elite' bestaat uit stedelijk Groenlinks. Populair beeld, maar ook heel erg aantoonbaar onjuist. De macht, het geld en de invloed zit echt heel nadrukkelijk rechts. Bij de VVD en CDA, die naast een achterban aan kiezers ook nog een hele achterban aan donateurs en informeel netwerk hebben. 

Het zijn de keuzes van rechts die stelselmatig gericht zijn op het verslechteren van de positie van de onderklasse, en die bovendien elke poging proberen tegen te houden als een links stadsbestuur er iets tegen wil doen.

De CDA-lobbyist en mister Populisme-fluisteraar zetten dat in het artikel ook nadrukkelijk aan: nergens in het verhaal zie je de situaties waarin SP, Groenlinks of PvdA binnen hun bestuur werkelijk dingen hebben bereikt die de positie van mensen juist verbeteren. Nergens wordt iets gezegd over hoe vaak ze het wel hebben geprobeerd (denk minder strenge bijstand) en waarbij de rechtse regering procedeert om dat tegen te houden. 

En.. mensen in de wijk weten dat lang niet altijd. Veel kiezers zijn van die nuance niet op de hoogte. De geinterviewden in dit stuk en iedereen op enig niveau in een politiek bestuur, gemeentelijk of landelijk, weet dit wel. Dan toch doen alsof het 'links' is dat te ver afstaat van de praktijk is behoorlijk misleidend.
[kspl0gq] (score 36, diepte 2) Dit is weer liberaal VVD-beleid. We hebben meer aandacht voor mensen nodig. We hebben meer socialisme en christendemocratie nodig. ;)
[ksqmxqp] (score 36, diepte 5) Ik ben oprecht hoor... 

Nederlandse Christelijke partijen zijn niet sociaal. 

Zo stemt CDA bijvoorbeeld al jaren tegen kinderopvang toeslag omdat ze vinden dat vrouwen zelf voor de kinderen moeten zorgen. Zo heeft de CDA een grote hand in de inperking van de geestelijke gezondheidszorg in Nederland. Ze zijn ook permanent tegen beleid voor implementatie van nodige zorg voor Homo (zoals hiv preventie) of tegen adoptie van kinderen door homo koppels, Euthenasia en En als allerlaatste zijn ze er vooral om boeren belangen te behartigen wat ook niks met socialisme te maken heeft, dat is namelijk gewoon neoliberaal agricultuur beleid geweest de afgelopen 10 jaar. 

Christen unie en SGP zijn nog conservatiever. En nog meer tegen alles wat anders denkend is. Het probleem met de Nederlandse christelijke partijen is dat ze vaak heel erg hard roepen dat ze vroom en sociaal zijn, om vervolgens precies het tegenovergestelde te doen van wat Jezus predikte: Uitsluiting, verstoting en veroordeling.

Als je een sociaal Nederland wil stem dan aub op Groenlinks PvdA, SP of D66 dat zijn tenminste echte (centrum linkse) socialistische partijen.
[ksqh8ah] (score 34, diepte 3) Nou die christenen mogen thuisblijven hoor. We hebben een sociaaler Nederland nodig.
[kspmfbz] (score 31, diepte 1) Interessant betoog. Heb je ook een verklaring waarom hetzelfde fenomeen zich voordoet in landen waar de segregatie onder pubers niet plaats vindt?
[kspfjsw] (score 29, diepte 3) Je miste het punt. Ze weten wel waar ze mee bezig zijn maar de impact die het heeft op persoonlijk niveau bij mensen aan de onderkant van de samenleving ontgaat ze. Voor iemand die 1 a 2 ton per jaar verdient is het een gemakkelijke beslissing over iets dat 200 euro extra in de maand gaat kosten, bijvoorbeeld ten behoeve van het milieu. Een nobele gedachte die zij makkelijk kunnen dragen. Heel veel schouders aan de onderkant kunnen dat absoluut niet. Voor hen is 200 euro een verschil tussen een maand wel of niet normaal kunnen eten. Ook de transitie nu bijvoorbeeld naar elektrisch rijden verloopt zwaar oneerlijk. Alles is gesubsidieerd maar elektrische auto's zijn tyfus duur. Dus alleen de top kan die auto's betalen. Goedkoop rijden en goedkoop aangeschaft door subsidies die mensen aan de onderkant weer betalen middels verhoogde belastingen of accijnzen. En daar wringt het nou net. Het gaat niet eerlijk.
[ksph7sw] (score 28, diepte 2) Van de andere kant: door twee jaar uit te trekken zodat taalzwakke leerlingen hun achterstand in kunnen halen, maakt de rest van de klas wel pas op de plaats.

De enige manier om dat goed te doen, is zorgen dat docenten voldoende kunnen differentiëren. Dat vergt veel kleinere klassen (max. 10 tot 15 ipv 25 tot 30 leerlingen) en meer voorbereidingstijd voor docenten (oftewel, minder uren voor de klas). Daar hebben we het geld en de mensen niet voor, en het ziet er ook niet naar uit dat we die binnenkort gaan krijgen.
[kspyz8m] (score 28, diepte 2) De middenschool is heel mooi voor de middenmoot, maar de uitersten, gymnasium en lwoo, worden beiden diep ongelukkig van zo'n middenmaalmolen
[ksqkm6c] (score 28, diepte 1) Voor de PvdA achterban is links lullen, rechts vullen verraad. Voor de PVV is het gewoon modus operandi.
[ksqr6iq] (score 28, diepte 2) Mensen zijn nog steeds pissig op PvdA voor een paar kabinetten geleden maar tolereren wel gewoon constante leugens uit de rechtse hoek
[kspdh28] (score 25, diepte 3) Klopt. Ze roepen dat het schuitje, dat zij hebben ontworpen, zinkt omdat er buitenlanders in zitten...en omdat er te veel milieuwetten zijn...en omdat de arbeiders te veel rechten hebben...cultuuroorlog...kijk vooral niet naar ons die het schuitje hebben ontworpen.
[kspfb6f] (score 25, diepte 0) Sterk artikel, al vielen me twee dingen negatief op:

>Sybrand Buma, de beste premier die Nederland nooit heeft gehad

Een van de zwakkere CDA-leiders? Dat dacht ik niet.  


>Bestuurders hoor je vaak roepen dat je “migratie toch niet tegenhoudt”

*Asiel*migratie hou je inderdaad moeilijk tegen. Bij *arbeids*migratie, sowieso een veel grotere groep, hebben we veel meer deurtjes opengezet, dus daar kunnen we veel meer aan doen.
[ksr8pma] (score 24, diepte 8) D66 noemt zichzelf sociaal-liberaal en progressief. Niet socialistisch. 

Daarnaast stemmen ze al jaren tegen socialistisch gerichte moties.

Huurstijging per 1 juli 2024 voorkomen: Tegen
Zorgen dat binnen de huisartsenzorg eigenaarschap van private equity partijen tot het heden gaat behoren: Tegen
Opschorten van militaire samenwerking met Israël: Tegen
Fel uitspreken tegen de blokkade van Gaza en de vergeldingsacties van het IDF: Tegen
Extra middelen voor de aanpak van sociale huurwoningen met gebreken: Tegen
Alle geheime afspraken tussen belastingdienst en multinationals openbaar maken: Tegen
Stop op sluiten van ziekenhuizen: Tegen
Inzetten op woonvormen voor ouderen zonder winstoogmerk: Tegen
[ksr5p11] (score 23, diepte 6) D66 socialistisch, laat me niet lachen.
[ksrseum] (score 22, diepte 3) Wilde hij die tijdens de verkiezingen niet nota bene per direct afschaffen?
[kspi0j6] (score 21, diepte 0) ik wil hier dit artikel tegenin brengen, die ik volgens mij ook hier ben tegengekomen: https://decorrespondent.nl/15115/waarom-de-pvv-zo-groot-werd-en-nee-niet-door-geschrapte-buslijnen-guur-neoliberalisme-of-groeiende-ongelijkheid/11329427-c34e-0037-2754-969f6eb43828
(139 reacties met lagere score weggelaten)

=== THREAD wl60y0 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-08-10  SCORE: 145  REACTIES: 154
TITEL: Flat feet shoes - I’m looking for plated shoes that will fit best with these flat feet, and any other shoes for that matter
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ijrg1it] (score 428, diepte 0) I thought this was a palm against the floor haha.
[ijri9jg] (score 284, diepte 0) This is the weirdest foot I have ever seen
[ijrmbic] (score 226, diepte 1 OP) evolution
[ijrm3a8] (score 167, diepte 1 OP) I can clap my feet like hands, its a party trick
[ijrmpmy] (score 159, diepte 0) I can genuinely say I have never seen a foot like yours in my life
[ijrifuv] (score 137, diepte 0) Holy crap sorry about your feet bro 🤣😭
[ijrfpj1] (score 89, diepte 0) You've got some proper flippers there, mate.  You any good at swimming?
[ijrm47c] (score 82, diepte 1 OP) i can tread water for days
[ijrkpky] (score 81, diepte 0) What am I looking at here.
[ijrryvj] (score 57, diepte 2) I give you props for the humor you have in this!
[ijs15ea] (score 52, diepte 0) TIL I in fact do not have flat feet
[ijrwtl2] (score 44, diepte 2) Post video lmaoo
[ijrpzps] (score 41, diepte 2) Every foot has pronation.
[ijrhh0z] (score 36, diepte 0) Mine are similar, for me the metaspeed  sky works well. Different things work for different people though. Endo pro 3 and the hoka carbon 3 are others i would suggest. Even the new alphafly is supposedly wider so maybe that'll work but i couldn't say without trying
[ijrtriu] (score 35, diepte 2) This made me laugh lol 
I’m glad you’re able to take humour in your stride (even if it is a bit… flat) anyways I’ll see myself out 

Good luck finding some shoes: I’ve heard ASICS has always been kind to flat feet
[ijrips1] (score 34, diepte 0) My feet look just as flat! These are the plated shoes that work well for me. 

Endorphin Speed 1 - ran a marathon in these last year. 
Endorphin Pro 1 
Metaspeed Sky
Glideride 

I also just scored the Hyperion Elite 2 from Eastbay for 75 bucks. I tried them on and they fit really well. Just haven’t ran in them yet.
[ijrqjqh] (score 29, diepte 1) Me to. OP next time don’t post a pic
[ijsnywb] (score 24, diepte 1 OP) I can suction cup to walls and walk up them
[ijsnl6f] (score 22, diepte 1 OP) 0 pain! Just emotional pain
[ijrc3oy] (score 21, diepte 1 OP) How else are you gonna see the non existent arch
[ijrk32u] (score 20, diepte 1) LOL
[ijrnwn0] (score 18, diepte 0) How’s Bedrock these days?
[ijral7s] (score 17, diepte 0) Altra lone peak 6 is amazing.
[ijrfyk5] (score 17, diepte 1) Altra vanish carbon is plated
[ijrhoh8] (score 17, diepte 0) I have never seen a fallen:flat arch like that!!
[ijrs0le] (score 16, diepte 1) OP has also flat palm
[ijrm7zh] (score 15, diepte 1 OP) Ill check those out, Asics have always been good to me
[ijtxi82] (score 12, diepte 0) Hey Op,

I think this post is a good opportunity to add a new section for those with flat feet to the FAQ.

Once you have good suggestions that actually work for you, could you reply to this comment with a list please?

Thanks
[ijs41ta] (score 11, diepte 0) Bro, I think you need new feet. 

On another note, Brooks Beasts but put a third party plate in it. I am not sure of what other options you would have to be honest.
[ijtl7wz] (score 10, diepte 1) Why your hand have ankle?
[ijrslu4] (score 10, diepte 2) OP, I was by no means taking a dig at you with my comment. I maybe should have worded my comment a bit better. I wasnt saying your foot is the worst that I have ever seen. I was saying that I have actually NEVER seen ANY flat foot.
[ijso57f] (score 10, diepte 1 OP) Only my grandad
[ijrm5yl] (score 9, diepte 1 OP) Thats what all the orthos say
[ijsyufz] (score 9, diepte 1) Looks like a reverse arch, not flat to me.
[ijrm9on] (score 8, diepte 1 OP) Awesome, thank you for the suggestions
[ijs8yjg] (score 8, diepte 2) In reverse 😂
[ijrmooh] (score 8, diepte 0) I have a flat ass foot and collapsed ankle, looks similar ish to yours. I go back and forth between brooks adrenaline gts or new balance 860 v12 depending if there’s a sale on either. Both are gonna offer you the support you need. Nikes look cool but they fall apart after like 150miles.
[ijso6je] (score 8, diepte 1 OP) They’re great for surfing
[ijsagul] (score 7, diepte 0) Bro
[ijskfuh] (score 6, diepte 1) I was right there with you…. Until you mentioned the Aloha Fly! Haha! Our feet are still too flat for that arch pressure. Wish I could try the Metaspeed but they don’t make my size. Ditto on Carbon X and Endorphin Pro.
[ijrhqxv] (score 6, diepte 0) Try out vaporflys. I know a bunch of flat feeters that find them manageable for a full.
[ijsjde9] (score 6, diepte 1) As a PT, I feel that people get way too bogged down in how things are supposed to look. What really matters is if the involved tissues are tolerant of the load that you place upon them. If they aren’t tolerant and you’re experiencing discomfort, then you find a way to reduce load on those tissues (in this case, by adopting particular footwear) and strengthen them. If you feel fine, then there’s nothing to worry about.

You’d be surprised how many pros have flat feet and / or pronate. In fact, there are many of us that consider pronation to be a key performance indicator amongst athletes.
[ijsp8hc] (score 6, diepte 2 OP) Yeah the orthopedic said it’s a very flexible flat foot and since it doesn’t hurt there’s no need to worry about it, the only thing is if the shoe has an arch in it, then it’ll rub a blister in my foot is the only issue
[ijsnqg2] (score 6, diepte 1 OP) I didn’t get that human upgrade
[ijsova9] (score 6, diepte 0) I really take my feet for granted
[ijs45yd] (score 5, diepte 2) I have one foot like this and one with normal arch. Have my whole life. And every dr who looks at them says they’ve never seen anything like it. Which honestly is never really all that helpful. I’m following because I really struggle to find shoes that work for me.
[ijsa0ck] (score 5, diepte 0) Fellow Bedrock resident here, always worn New Balance for the width and flatness. In the other shoes category: Allen Edmonds. Best and most comfortable dress shoes ever for our kind.
[ijta6dt] (score 5, diepte 0) You could sell pics for sure.
[ijs6tny] (score 4, diepte 2) No issues for me. I would say they were flawless during the marathon. Sometimes I’d get some Achilles soreness but nothing major.
[ijrouy2] (score 4, diepte 0) I have a question for anyone with a greater understanding of biomechanics. I have similarly flat feet and a static picture would look practically identical to the original post. I started with stability shoes as I was told I over pronated on treadmill assessment. However I have run every day (streaking) for 3.5 years with no issues/injuries and have gradually transitioned to neutral shoes with no issues (hundreds of miles in neutral shoes). 

Although I have no arch is the strengthening of the ligaments/tendons causing a difference in the dynamic motion of the arch during running compared to when I first started? That is, can you have a "flat foot" statically which appears to "over-pronate" which corrects dynamically when in motion? I've not had a subsequent treadmill test to re-assess alignment, but have had no aches/pains/niggles for years.
[ijs16i7] (score 4, diepte 1) Pronation from how I understand it is a natural pattern within the walking gait. It's a biomechanical mechanism that is used to absorb a certain degree of shock when the foot hits the ground when walk or running. Once the foot is around midstance or just prior to a toe the foot will sorta re-supinate to start again and get ready for the next landing if that makes sense. 

Pronation only becomes pathological if it's excessive but what's excessive is very or particularly subjective. The way I view it is, that it's only excessive if the individual is getting some sort of pain, tiredness within the foot, arch ankle etc. This then can also relate to lower leg muscles and ligaments and how they react to movement within the ankle joints. 

And yes definitely can have a change in the positioning of the arch when in static positioning to dynamic motion. That's Essentially down to the proprioception of the body and how it feels the foot should be positioned. 

Take that with grain of salt as I am just starting some of my major studies in biomechanics but that's how I understand it.
[ijrthqn] (score 4, diepte 0) Guys stop trolling (Chuckles)
[iju17hj] (score 4, diepte 0) I’m an Australian Podiatrist specialising in gait analysis. If you would like an online analysis please feel free to book with me. There’s no charge just here to help.

https://www.unisoles.com/book-a-podiatrist/
[iju9r27] (score 4, diepte 0) This makes me very uncomfortable, I'm sorry.
[ijt6xu9] (score 3, diepte 1) ![gif](giphy|ltIFdjNAasOwVvKhvx|downsized)
[ijthcjw] (score 3, diepte 4) Lmao... where's the linktree?
[ijrohdi] (score 3, diepte 1) Did you have any issues with your arches running in your endo speed for your marathon? I had a little minor ankle/arch soreness when running a 10k race in them and I'm worried about longer events
[ijrmefa] (score 3, diepte 0) So I have flat arched wide feet , I use/I’ve used Hoka rincons, Hoka carbons, and Bondis , rincons and Bondis for short runs carbons for longer runs, i also use/have used Nike invincibles for anything between 3.5-9 miles. Both grands work. I want to try the ASICS kayanos and some sauconys next as well. Go to your local running store and tell them about your feet they might help you find something as well or at least an insole that’s works (I use an insole on all my shoes now)
[iju28yt] (score 3, diepte 1) Brooks adrenaline GTS were a game changer for me. Couldn’t run without feet pain more than 5 km. Since I bought those shoes I’ve never felt pain again. Recently I’ve run my first half marathon in them.
[ijsv2q9] (score 3, diepte 3) Exactly. Sounds like a good ortho! Meet the arch and no more!
[ijulrio] (score 3, diepte 2) Thanks for the reply. My impression was that people do get bogged down with pronation "issues" and flat footedness as a problem to solve - which didn't fit with my situation as I'd never experienced any issues despite the lack of arch. Your practical approach makes sense.
[ijt086p] (score 3, diepte 1 OP) I went to an orthopedic and he told me they would have to do a hip graph and reconstruct my foot and I’d I’d have to learn how to walk again, but he said since they don’t hurt me there’s no need
[ijsxyz6] (score 3, diepte 0) Altra shoes would be a good bet. I have flat feet too and Altra Torin 5 is good. Use Hoka Mach 4 only when I can run due to durability but both Torin and Mach don’t put any pressure on the arch.
[ijukpm2] (score 3, diepte 1) I definitely agree with this suggestion!
[ijrmj5f] (score 2, diepte 3) Uhh no. OP doesn’t need cushioning, just a plated shoe that can help with their flat feet. Altra would be a very good choice imho.
[ijsub9a] (score 2, diepte 1) I did too!
[ijswh9r] (score 2, diepte 1) For Saucony and Hoka shoes - they typically have arch support built into the inserts, so for flatter feet, perhaps it might feel more comfortable to remove them.
[ijsypat] (score 2, diepte 2) This all Hoka shoes hurt my feet until I take those inserts out lol
[ijsjb3b] (score 2, diepte 1) I have low arches and the Alphaflys were terrible for me. Returned them after one run. Maybe the Vapors are different though.
[ip708rm] (score 2, diepte 1) Kayano 29 - did u try it? Its perfect for my flat and wide foot.

I was using invincibles which i loved the bounce of but once i started using them more frequently i developed posterior tibial pain which is a symptom of flat feet even though i thought i didnt overpronate too much!.

Got the kayano 29 yesterday after reviews online and did a run, immediately felt so much better. Currently rehabbing the foot. Was skeptical because ive never had foot pain before but the kayanos 29 felt super comfortable and performed with a pretty smooth stride too!  Walking feels heavy in this shoe though...
[ijrocrb] (score 2, diepte 0) I tend to prefer something slightly firmer as I do collapse just slightly. The Vaporfly and RC Elite v2 are a little too soft for me. I feel great in the Saucony Endorphin Pro 3 or Speed 3, Puma Deviate Elite Nitro, and can get by on the Metaspeed Sky. It comes a little more down to preference of what kind of ride you want then, but these are all good options along with the Asics Metaspeed Edge v2.
[ijutigy] (score 2, diepte 3) You bet! Glad that resonates with you!
[ijsep8y] (score 2, diepte 1) no he doesn't
[ijrxxdx] (score 2, diepte 0) Look up lacing techniques for flat feet too!
[ijrzv6m] (score 2, diepte 0) I have pretty flat feet. The adizero adios pros 2 work really well for me. You just need to break them in…so don’t immediately run a marathon or something without breaking them in first. 

But ultimately you have a lot to go off. Try them out, and see what works!
[ijs3lqk] (score 2, diepte 0) Interesting foot! Is that bad for running? Any other issues?
[ijs6s5f] (score 2, diepte 0) I have flat feet too. I also nave narrow feet and supinate (which seems fairly uncommon in flat footed runners). I don't have trouble with most shoes but I find Nike and hoka have too much arch support and make me feel like all of my weight is on my arch.
[ijs83xn] (score 2, diepte 0) Do you have pain?
[ijsnmvl] (score 2, diepte 1 OP) Nope, 0 pain fortunately
[ijsemwx] (score 2, diepte 0) damn. you got them FLAT feet huh
(83 reacties met lagere score weggelaten)

=== THREAD 1953eg3 ===
SUBREDDIT: r/Shoes
DATUM: 2024-01-12  SCORE: 68  REACTIES: 103
TITEL: Got holes on the insoles of my vans. What should I do with them?
POST (source_id=post):
I had these for almost two years and I just now started noticing these holes/patches on the insoles of my vans. What should I do with them? I don't want to throw them away yet.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[khk9ih5] (score 62, diepte 0) Get a new pair
[khkfwoe] (score 40, diepte 0) You can buy new insoles for like $10
[khk8hgj] (score 20, diepte 0) Toss those stinkers out lmfao
[khknxki] (score 17, diepte 0) They have lived a good life. It’s time to lay them to rest.
[khl8lj6] (score 13, diepte 0) Telephone/power lines
[khl3ftx] (score 8, diepte 0) New insoles should fix the problem, you can retread them if needed. With the right care and repair, shoes can last alot longer than 2 years. All else fails, look up cobblers and shoe repair people in your area. Reject consumerism! Embrace repair!
[khkz7ch] (score 7, diepte 0) If the tread is good, grab new insoles
[khkcdnp] (score 6, diepte 0) Shoe liners
[khn5wg8] (score 6, diepte 2) Eh not always true. Pretty easy to tear them out. I also have to put insoles in my vans anyway as they’re too low and flat inside otherwise.
[khlv8zc] (score 5, diepte 0) Clean them up and get new insoles
[khn524x] (score 4, diepte 0) Dude come on you need a new pair of shoes.
[khl50k0] (score 3, diepte 0) Just buy a new set of insoles. You can get super cheap ones for like $6 on amazon
[khm8hsk] (score 3, diepte 0) get you some new insoles and some glue for shoes
[khmfbg0] (score 3, diepte 0) Take out those old insoles and replace them with new ones.
[khmn4rx] (score 3, diepte 0) Buy new insoles
[khn2soq] (score 2, diepte 1) With a few exceptions, most vans have glued-in insoles now
[khnm4mg] (score 2, diepte 3) Your mileage may vary. I tore out the insoles on my classics, thinking it'd just come out bc I wanted to wash them, and I put Feel Your Sole insoles in after. They just feel super weird now. I rarely wear them anymore.
[khmpj2u] (score 2, diepte 1) Never throw them on a telephone pole
[khkrjki] (score 2, diepte 0) Damn. Yard work shoes or trash them. Get a new pair in 2024!
[khktnpp] (score 2, diepte 0) As mentioned before you can replace the insole with just about any shoe liner, I sell insole sheets in various thicknesses that can be trimmed to fit any shoe. They probably use 1/8” from factory: https://mygotooz.com/products/1-8-3-mm-insole-sheet-silver-ag-2-0-1-8-bounceblu?utm_content=ios&utm_medium=product-links&utm_source=copyToPasteboard
[khl22pz] (score 2, diepte 0) Rotate them into your beater lineup .. shoes to wear when shits about to get muddy lol
[khpg9an] (score 2, diepte 1) This is the best answer I would still throw a new pair of insoles in them and grab some shoe goo glue specifically for skate shoes then you will be prepared for everything. I can’t be sure but I feel like the people telling you to toss the shoes might be more into sneakers for fashion and not sneakers for skating. Breaking in skate shoes is a big fucking deal so if the treads good it’s worth it to get insoles and once the outside starts going it’s even worth it to fix that if they’re great shoes that you can skate hard in.
[khp18fp] (score 2, diepte 1) This! Reminds me of home in the hood once upon time. The Nostalgia vibe is real with this one! Do it OP, this is the way.
[khm10wb] (score 2, diepte 0) Those at $49 at DSW. Don’t waste money on new insoles that can cost just get new Vans. Don’t waste the money on insoles for that can up to that much. Bud, these shoes have seen better days. The laces are stained. Toe boxes are separating. Paint is rubbing off the squiggly Vans line. I know it’s sad to part with a beloved shoe, but you need to man up and burn these bro.
[khm65ag] (score 2, diepte 0) Smush some gum into then and let it harden
[khpfwqu] (score 2, diepte 1) Shoe Goo specifically for skate shoes
[khmedbi] (score 2, diepte 0) Sometimes it's ok to get new shoes
[khneve0] (score 2, diepte 0) Name checks out… get rid of them man, they done.
[khwex6k] (score 1, diepte 4) I would not recommend tearing out adhered insoles BECAUSE they will change the underfoot feel. It could mess up your whole gait. OP skate in these and do a few kick flips, then retire them.
[khy1i6w] (score 1, diepte 5) Yeahhhhhhh the regret set in immediately after I heard the glue rip from the sole lol.
[ki4opqy] (score 1, diepte 1) That’s true cas the shoe is durable asf cas I skate so get a new insole
[khkg86m] (score 1, diepte 0) I saw crusty, the pic, and immediately realized..

I need Jesus.
[khlapgn] (score 1, diepte 1) I saw.... Nevermind
[khlbc06] (score 1, diepte 2) I’m sure it was the same thing 😅😂
[khkhywj] (score 1, diepte 0) I feel like you already know the answer to this question
[khkl3bo] (score 1, diepte 0) Garbage. Vulcanized shoes are the worst; they always absorb water into the soles making the insole damp and smelly
[khkyj7f] (score 1, diepte 0) How's the tread looking.......
[khl2gkt] (score 1, diepte 0) Seems you have about 3 choices. Wear them until they fall apart, buy new insoles for less than $10, or throw them away.
[khl8gdm] (score 1, diepte 0) Tie them together then launch em up on power lines
[khl94jr] (score 1, diepte 0) Tie the laces together and hurl them high into a tree at your local park
[khlbaqb] (score 1, diepte 0) Get a new pair
[khlcoma] (score 1, diepte 0) That same shit happened to mine and the insoles are glued in. Fuckin bullshit. I don't buy Vans anymore.
[khlpp4r] (score 1, diepte 0) Straight in the garbage. Time to retire
[khltyus] (score 1, diepte 0) 🤾🏾‍♀️🗑️
[khlxo9v] (score 1, diepte 0) Bronze them you baby
[khlxt68] (score 1, diepte 0) Bro it’s time
[khm1m14] (score 1, diepte 0) I think I can smell those from here…
[khm4sfd] (score 1, diepte 0) …they’re beater vans, just buy a new pair.
[khm61uc] (score 1, diepte 0) I saw throw both shoes, away!
[khm66r2] (score 1, diepte 0) Smush some gum into then and let it harden
[khm6f4k] (score 1, diepte 0) Throw em in the trash ? 🤷‍♂️
[khmak4m] (score 1, diepte 0) If you are like my mom just continue to wear them for the next 20 years or so. But really, you could buy an identical pair. They’ll never be THOSE vans but very close once broken in. I have done that with a couple items and tried with many more
[khmcwf1] (score 1, diepte 0) Those are old kicks, throw them away and buy a new pair, they only cost $ 70 bucks!
[khme1ca] (score 1, diepte 0) It looks like you’ve gully gotten your money’s worth out of them, I t’s time they were given a  Vikings funeral and burnt.
[khmetsu] (score 1, diepte 0) Use them for cleaning up 🧹 or throw away
[khmh2sk] (score 1, diepte 0) If these are the only pair of shoes you owned for 2 years it’s time to toss or donate.
[khmha74] (score 1, diepte 0) I’m sure you can get a new pair.
[khmkr7n] (score 1, diepte 0) Bondo it!
[khmosx0] (score 1, diepte 0) Throw them away and get a new pair. Or wear more than one pair of shoes
[khmotwv] (score 1, diepte 1) *Throw them away and*

*Get a new pair. Or wear more*

*Than one pair of shoes*

\- Slickdiddy313

---

^(I detect haikus. And sometimes, successfully.) ^[Learn&#32;more&#32;about&#32;me.](https://www.reddit.com/r/haikusbot/)

^(Opt out of replies: "haikusbot opt out" | Delete my comment: "haikusbot delete")
[khmvshg] (score 1, diepte 0) Get new insoles, you can take those out
[khmw9dp] (score 1, diepte 0) Buy new ones
[khmxgcb] (score 1, diepte 0) I only wear my vans for one summer or whatever it is no longer than 6 months and get the same pair but new am I the only one ??
[khn2am6] (score 1, diepte 0) Burn them.
[khn4x57] (score 1, diepte 0) Burn them
[khn6tox] (score 1, diepte 0) Wear them without socks.
[khnbhro] (score 1, diepte 0) Duct tape
[khnbii9] (score 1, diepte 0) Step 1: Make pasta 
Step 2: Let simmer with shoes in pasta
Step 3: Take out shoes put them on telephone power line outside to air dry
Step 4: Enjoy soup
[khni9xv] (score 1, diepte 0) See a podiatrist
[khnmqdf] (score 1, diepte 0) Frame them, hang them, and love them forever
[khnnpx9] (score 1, diepte 0) Get another pair! Vans are cheap enough (I mean that in a good way) that they can be replaced relatively often. I need more arch support so I don’t wear Vans anymore though.

Vans are vulcanized which makes them pretty durable. But it’s not a very technologically advanced shoe. Same with Chuck Taylor’s. It’s just an old school design. 

Also consider having multiple shoes in rotation if you don’t already. It will make each pair last longer.
[khnt7bm] (score 1, diepte 0) Throw em away and get a new pair.
[khnzqzz] (score 1, diepte 0) Let it go
[khoed8z] (score 1, diepte 0) new i soles or just go get new vans, its 60 a pair
[khofmy8] (score 1, diepte 0) My brother, please just buy a new pair
[khoh3h1] (score 1, diepte 0) Get new shoes bruh. Even a homeless man would turn these beaters down, wtf u doin in these shoes if they only 2 years old, I got timberlands from like 8 years ago and they still almost box condition…
[khoh5w5] (score 1, diepte 0) Throw them away.
[khoic9g] (score 1, diepte 0) Are people really throwing out shoes when the insoles have worn out? Even if they're glued, it's not like it cannot be removed. Many brands don't always use the best materials for insoles, they tend to fail the first but the shoes have a lot of wear in them still!
[khop1tt] (score 1, diepte 0) If the soles of your shoe aren’t worn out just replace the insoles, you may be walking wrong to where you’re putting or stepping wrong when you walk.
[khorlu7] (score 1, diepte 0) New insoles will do the job. I had a pair of woodland. It lasted for 7 years.
(34 reacties met lagere score weggelaten)

=== THREAD 126jbsk ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2023-03-30  SCORE: 126  REACTIES: 87
TITEL: Which shoe is getting the boot?
POST (source_id=post):
Due to an unsuspected shoe addiction, I have to make a tough decision and sell one of these shoes 🥲

Was hoping to get general recommendations on which shoe is not making the cut

I know it’s personal preference but was doesn’t hurt to get a second opinion!

For context, I am planning enter my next  marathon training block and train in 2 of them (1 for tempo and 1 for long runs) and racing a marathon in 1 of them… and letting go of 1 

TIA

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[je9qdcj] (score 279, diepte 0) I hear you, but have you considered just accumulating several more pairs instead?
[je9pbhp] (score 66, diepte 0) You should keep all your shoes and add the prime x strung
[jea8usz] (score 64, diepte 1) This is the way
[jeamkwc] (score 31, diepte 2) This is the way
[je9kt2v] (score 28, diepte 0) The original Alphafly is easily the best shoe there for racing the marathon. I'd keep the Saucony for training for it. Hold on to either the Adios Pro 3 or Vaporfly for racing 5K-HM based on personal preference and get rid of the other one. Given that the Adios Pro 3 is more versatile, I'd personally ditch the Vaporfly.
[jean4s5] (score 21, diepte 1 OP) You’re a terrible influence… which pair should I get next?
[je9diip] (score 15, diepte 0) I would go for the Vaporfly.

Reason why is the Endorphin Pro has you covered for a similar need and the Alphafly is the ideal shoe for the Marathon.

Adios Pro 3 will give you something different to use if you fancy something more stable.
[je9nrvy] (score 12, diepte 0) If you could only have one, I’d go VF as I find it to be the best shoe overall. But, to only sell one, I’d lose the VF as the Alphafly is a better marathon racer if it works for you. 

Alphafly to race in. Endorphin Pro for long runs. Adios Pro for tempo.
[jeayqeh] (score 12, diepte 1) For every shoe you cut off, two more shall take its place.
[jea426n] (score 12, diepte 0) Out of curiosity how much would you sell the vaporfly for? Hehe
[je9k6mw] (score 9, diepte 0) Nice rotation
[jeav9ri] (score 9, diepte 1 OP) You wouldn’t believe it 😅
[jea8js3] (score 9, diepte 1) This is the correct approach.
[jeb82bj] (score 9, diepte 2) It is known
[je9gx4o] (score 8, diepte 0) Choose between adios pro 3 and alphafly since they are often compared, or choose between endorphin pro 3 and Vaporfly for the same reason. Personally I would keep the endorphin pro 3 and select any of the other ones
[jeao7p3] (score 8, diepte 2) I'm really happy with my Endo Speeds and Pros at the moment, but I'm really interested in the Mizuno Wave Rebellion Pro.
[jebmxjs] (score 7, diepte 1) Teehee
[je9ngae] (score 6, diepte 0) I have all 4 of those shoes.  I returned the endorphin pro 3 because I just didn't love them, and would've done the same with my vaporfly if I bought from a store with a generous return policy; instead they just sit in a box.

The adios pro 3 and af1 are by far my 2 favorite shoes of all time.  Nothing comes close.
[je9u299] (score 6, diepte 0) I have almost the same decision to make. I have used AF 1 for 3 marathons and loved the comfort and speed. But I bought a pair 1/2 a size too small so my toenails have not yet fully recovered since my last marathon in September. 

Received a free pair of Adidas Pro 3 to test for Berlin Marathon. Loved the ride, but the upper became too painfull after 20k rides. I therefore used AF 1 for Berlin. I have recently on this sub found information on how to proper lace Adidas running shoes, so now they are back in contention. 

I got Vaporfly 2 very cheap 2 month ago and haves used them for speed workout. They are good but not great for me.

My latest addition is Endorphin Pro 3 on sale a month ago. Realy like the comfort of them, but I am not sure if they have the same speed for me as Adios Pro 3. I will use the for a 32 k fast run Sunday and then decide if I will use them for Hamburg Marathon next month.

Long story short: I would loose the Vaporfly
[je9cu09] (score 4, diepte 0) Alphafly
[je9jrbc] (score 4, diepte 1) I agree with this. If I had all 4 pairs the Vaporfly would barely get any use. I would probably go even further and just keep the Alphafly and Endorphin Pro 3.
[je9mo27] (score 4, diepte 0) Keep ES3 for training, VF for 13.1 or less and AF for 26.2

Adios can go. Good shoe, but these other 3 are best in their class for respective use cases.
[jealfh3] (score 4, diepte 0) Wow you’re lucky I saw this post! You def don’t want the AF. Don’t even put them on. You’ll hate it. I guess I’ll have to buy them from you. Damn.
[je9hqga] (score 3, diepte 0) Alphafly out you go.
[jeamuo5] (score 3, diepte 1) This is the only viable option
[jecazxy] (score 3, diepte 2) Hail Hydra
[jeczoxa] (score 3, diepte 1) Do you mean to tell me the 3-pair rotation is a myth?
[je9tgic] (score 3, diepte 0) Anyone know if the Speed 3 threes are the same width as the pro 3? Mine are so bulky and wide that am thinking of returning them.
[jeazo5h] (score 3, diepte 1) Can you share the link for proper lacing Adidas shoes
[je9u7ky] (score 3, diepte 0) I'd absolutely keep the Alphafly.  Haven't had a lot of experience with the VF or Adidas shoes.  Endorphin Pro isn't bad, and fairly versatile.  All that said, if you don't want that AF, you can feed my addiction.
[je9z6pw] (score 3, diepte 0) Clearly there's no consensus here. The only option is to get rid of *other* non-running shoes so you can keep all of these.
[jear4y0] (score 3, diepte 0) Would keep the Endorphin (for long runs and workouts) and the Alphafly (for racing HM and full).
[jeat3hs] (score 3, diepte 0) Adios Pro 3 is the most durable and also very versatile, probably the best one for training, imo. Vaporfly is the fastest one, Alphafly is often the best one for the marathon. I haven’t used the Endorphin Pro 3, not sure where they would fit, but at the end of the day, you can’t go wrong with any of these, it comes down to personal preference pretty much.
[jedtc97] (score 2, diepte 1) Absolutely different shoes. I would do fast 5/10k in Vaporfly's and anything above or on tired legs in adios pro 3
[je9rrcn] (score 2, diepte 1) I have all the shoes as well and returned my endorphins. I just don’t like them that much
[je9pwz9] (score 2, diepte 0) Tough choice. If the alphafly works I’d keep it, it’s still one of the best if not the best marathon shoe on the market.
the vaporfly the fastest out them all? Maybe sacrifice the saucony…
[jebt7m2] (score 2, diepte 3) Man I really love the look of the mizuno but hate that you absolutely have to be on your toes - and I like to wear my pairs after I’m done using them for running and that heel seems like it would be impossible to do so.
[jebuu4w] (score 2, diepte 4) The [Wave Rebellion Pro](https://www.mizunousa.com/wave-rebellion-pro) looks like it *might* be doable for me.

The [Wave Duel Pro](https://top4running.com/p/mizuno-wave-duel-pro-u1gd220020) looks kind of insane. I mean, I think it looks cool as an object, but I also think I'd fall down and hurt myself.
[jebccc2] (score 2, diepte 2) Which pair**s**
[jearlw6] (score 2, diepte 1) Listen to their sage advice
[jeof0pc] (score 2, diepte 1) Flair checks out
[je9qw55] (score 2, diepte 0) Whatever you do don’t you return the EP3.
[je9ri43] (score 2, diepte 0) I’m tossing the endorphins. I just don’t enjoy them like most
[jeaoatf] (score 2, diepte 1) I have several Adizero shoes and have struggled with the upper as well. Could you link me to those lacing instructions?
[jeb8nl4] (score 2, diepte 3) No problem, thanks though, I think I know what you are referring to.
[jecmhuk] (score 2, diepte 2) All of the Adizero shoes come laced over-under the eyelets instead of the usual under-over.
[jebcwwv] (score 2, diepte 1) Or a kidney.
[jea1ntz] (score 2, diepte 0) The one with the most miles. And with that money you get you can buy a newer version.
And since you saved money, buy another pair in discount while you're at it.
[jea5vx5] (score 2, diepte 0) You can sell the VF for a good amount of money while accomplishing your goals with the other shoes.
[jea8qud] (score 2, diepte 0) Sorry, you can’t sell the ekiden model, it’s too nice
[jeacqyo] (score 2, diepte 0) See, it's completely up to you, you have same number of "ditch the VF" and "ditch the AF" answers.

My opinion is the same as /u/bradymsu616
[jeagu82] (score 2, diepte 0) The Adidas!
[jeaqs5x] (score 2, diepte 0) One thing you can say from all the replies; the Adios have the least amount of people saying to ditch them. That must speak for something
[jeb809k] (score 2, diepte 0) Bye vaporfly
[jebe74h] (score 2, diepte 0) Obviously personal preference, but I don't personally care for the Vaporfly. That's the one I'd sell without hesitation.
[jecz9gh] (score 2, diepte 0) Adiós to the Adios 👋
[jed0pk0] (score 2, diepte 0) Saucony for speed, adidas for long runs, vapors to race in and drop alphas
[je9cwc1] (score 1, diepte 0) Both Nike shoes
[je9jp0g] (score 1, diepte 0) i’ll go for vf. the rest can keep
[jealxsu] (score 1, diepte 1) Why is the original Alphafly better than the current version?
[je9no8e] (score 1, diepte 0) Id say use the Adios Pro 3 for racing. Saucony for long workouts and AF for speed. Vaporfly is my least favorite among these shoes and it is the least durable as well.
[jeopb8g] (score 1, diepte 2) Just updated it, but I mainly only wear my Sauconys these days (seven pairs).
[jeb58vf] (score 1, diepte 2) I can’t find the link now, but you remove the laces and start again from the bottom(near the toes). It was impossible for me to ajust the laces enough without starting completly over from the bottom. Sorry if it is not clear. I am not a native English speaker
[jeanj66] (score 1, diepte 1 OP) I’ve somehow ended up more conflicted after posting this than before
[jeaqhmq] (score 1, diepte 2) My opinion is to chose your racing shoe, then build from here 

Get the most similar one for long run

And the most comfortable one for tempo work
[jeamees] (score 1, diepte 0) if i wanted to buy one of these which one would it be? i prefer 10k distance or under but might do a 20 a couple times a year?
[jeb285a] (score 1, diepte 0) Have you run in any of them? They all look brand new.
[jebntny] (score 1, diepte 0) Unfortunately, it appears that you wear a 10.5, or the correct answer would be to sell me your Alphaflys.  

Instead buy 2 more pairs that will make a good secondary rotation with the Vaporflys.
[jecbtnz] (score 1, diepte 0) I’ll take those Vaporflys off your hands 😬
[jeckghd] (score 1, diepte 0) Just keep them, you can’t be that desperate for $100. Just limit your future spending.
[jecyhho] (score 1, diepte 0) Send me whichever pair you don’t want and I’ll hang onto them for you.
[jedob71] (score 1, diepte 0) WOW
[jeen0h7] (score 1, diepte 0) I have done my marathons in vaporfly . Alphafly really hurt my mind foot for some reason. I sometimes use Saucony EP 2 for my 15-18 miles but it's a guaranteed blister . I don't know why . But the shoe is quite fast.  

About the Adidas , never tried that but use Boston 11 for my long runs.
[jef66ts] (score 1, diepte 0) Personally, I would boot the saucony. I like to train one day a week in race shoes to get a feel for race day and the stress the shoe adds. Unless you plan on racing in the saucony, I would get rid of those.
[jefwzgm] (score 1, diepte 0) You’re missing the endorphin elite from your collection
[je9e6av] (score 0, diepte 0) I would ditch the Adios Pro 3 (firm and the Alphafly 1 is still best long distance/marathon racer out there) or the Vaporfly (endorphin pro more versatile)
[jea03v4] (score 0, diepte 0) Hnnnnnnnnnnng
[jeajh4a] (score 0, diepte 0) NONE
[jeav841] (score 0, diepte 0) Bye bye three stripes
[jeb1gyc] (score 0, diepte 0) Any shoe without Nike ZoomX gets the immediate cut
(6 reacties met lagere score weggelaten)

