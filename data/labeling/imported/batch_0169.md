# Label-batch batch_0169

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
Schrijf het resultaat naar `batch_0169.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1j1r5tx, r7wbfp, 1j33wbz, 1ejj4zb).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1j1r5tx ===
SUBREDDIT: r/nederlands
DATUM: 2025-03-02  SCORE: 0  REACTIES: 61
TITEL: Hoe wassen jullie je voeten?
POST (source_id=post):
Oké, ik heb dus echt een hekel aan voeten. Het wassen ervan voelt als een eindeloze taak. Ze zijn lelijk en ze beginnen altijd weer snel te stinken.

Daarom neem ik elke zondag een voetenbad en elke keer als ik douche (in de ochtend) manoeuvreer ik heel ongemakkelijk met een washandje op een been om ze te wassen. Daarna droog ik ze altijd goed af, maar na een dag lopen, BAM, stinken ze weer. Super ongemakkelijk om stinkende voeten te hebben tijdens de seks, dus ik laat eigenlijk altijd mijn sokken aan. Maar ja, na een dag zijn dat natuurlijk ook niet meer de meest frisse sokken.

Dus Reddit, wat doe ik fout?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mflr8gw] (score 15, diepte 0) Probeer zo'n ding dat de meur uit je schoenen haalt. Gebruik ook dunnere sokken want het klinkt alsof je last hebt van zwetende voeten
[mflrgnq] (score 8, diepte 0) Je kan het beste niet stinken.  
Dan is het opgelost.
[mflti8q] (score 8, diepte 0) 1. Grote kans dat je een schimmelinfectie hebt. Teennagels oké? Dan 1-4 weken elke dag Terbinafine smeren. Geen miconalzonitraat. Terbinafine.

2. Vervang al je sokken door merinowollen sokken. Zo dun mogelijk. Trap niet in bamboe.

3. Koop minimaal 2 paar goede leren schoenen en doe elke dag een ander paar aan. Ik ben zelf fan van van Lier. Ff een jaarlijks uitje naar bataviastad scheelt je de helft in aanschaf.
[mflrak0] (score 7, diepte 0) Misschien een keer voor je naar bed gaat douchen, want nu ga je met je stinkende poten naar bed toe.
[mflu2n8] (score 7, diepte 2) Best bijzonder want ik was ze eigenlijk nooit. Ik douche elke avond en ze blijven gewoon schoon en stinken niet. Ik heb wel dunne sokken aan en ik wissel elke dag met andere schoenen. Misschien is er een andere reden dat jij er zoveel last van hebt terwijl je er zoveel tijd aan kwijt bent.
[mflu24d] (score 6, diepte 2) Vers zweet stinkt niet als het goed is.
[mflttci] (score 5, diepte 0) Katoenen en wollen sokken, geen polystester of andere meuk, helpt tegen het zweten. Polyester is totaal niet adembaar. T helpt al een hele hoop. Draag in de winter vaak wollen sokken en ik heb t dan warmer en geen last van zweet. Zomer iedemdito
[mflrhbt] (score 4, diepte 1 OP) Hmm goed idee. Morgen krijg ik nieuwe schoenen binnen dus dan kan ik het gelijk goed bijhouden
[mflschq] (score 4, diepte 0) Wat voor sokken en schoenen draag je? Bamboesokken kunnen helpen bijvoorbeeld om de stank tegen te gaan. In principe horen voeten niet te stinken.
[mfm98v6] (score 3, diepte 4) In Caribisch Nederland zou ik lekker op goede sandalen (niet plastic) zonder sokken gaan zo veel mogelijk. Vooral zoveel mogelijk synthetische producten vermijden. Je hebt ook heel erg dunne wollen sokken, dat is altijd beter dan synthetisch.
[mflwmow] (score 3, diepte 3) Klopt.
[mflwk23] (score 3, diepte 2) Nee, dat is dus niet waar. Zweet is geurloos maar gaat stinken nadat het in aanraking is gekomen met bacteriën.
[mfm06dd] (score 2, diepte 2) En echt goede sokken! Bijvoorbeeld merinowol.
[mfm8d7m] (score 2, diepte 3 OP) Werkt dat ook in de tropen? Ik woon in Caribisch Nederland.
[mfmaoxu] (score 2, diepte 5 OP) Oke ga ik voor kijken thanks. Thuis loop ik op slippers of gewoon blote voeten eigenlijk. Eigenlijk draag ik alleen schoenen met uitgaan, een rit naar de supermarkt red ik altijd wel zonder nare geuren.
[mfltdel] (score 2, diepte 2) Draag jij plastic sokken? Sokken ademen en veel schoeisel eveneens.
[mfluged] (score 2, diepte 3) Ligt meestal aan je dieet. 
Als je veel knoflook hebt gegeten dan gaat je zweet er ook naar ruiken. Moet je voorstellen hoe je ruikt na een Indische maaltijd.
[mflss18] (score 2, diepte 1) Droog je ook goed tussen je tenen? Vocht tussen je tenen kan geur veroorzaken. Een beetje talkpoeder of maïzena helpt om ze droog te houden
[mflsvwg] (score 2, diepte 0) Ik gebruik soms Pedicare in de zomer. Het stinkt enorm, dus aanbrengen met een handschoen is geen overbodige luxe. Voor mij werkt het goed!
[mflta1n] (score 2, diepte 1 OP) Kijk perfect. Dit ga ik bestellen thanks :)
[mflujw4] (score 2, diepte 2) En Shoefresh heeft een apparaat genaamd Opod. Ik heb het wel eens getest, en het laat je schoenen weer normaler en frisser ruiken. Maar dat is meer een oplossing voor schoenen.
[mflw937] (score 2, diepte 4) Ik gok wel dat de voeten het eerste probleem zijn, maar als je schoenen eenmaal stinken en je er geen oplossing voor hebt blijven ze stinken. Dus dat apparaat was wel een mooie oplossing.

Als je zweetvoeten hebt, worden je voeten, sokken en schoenen vochtig. Perfect voor schimmelvorming, want vochtig. Ik ben geen pedicure, maar ik kan me wel iets voorstellen bij de andere reacties over voetschimmels.
[mflt9x6] (score 2, diepte 0) Niet je voeten met zeep wassen. Doet iets met je huid waardoor je extreem gaat zweten.
[mfltg2q] (score 2, diepte 0) Koop goede echte leren schoenen bij een goede schoenen winkel. Als je een goed paar hebt gevonden, koop dan gelijk een 2de of beter een 3de paar, hopelijk in verschillende kleuren. Draag iedere dag een ander paar. Koop goede, dunne sokken. Geen synthetische, katoen of wol. Drink tenminste 2 liter water per dag. Eet geen suiker, junkfood etc, maar gezond eten, veel fruit en rauwe groente. Je zegt dat je je voeten al goed wast en droogt, gebruik wel een ph neutrale zeep. Loop binnenshuis op blote voeten. Als dat niet goed gaat, dunne sokken. Het kan zijn dat een voetschimmel hebt, terbinafine kan daarmee helpen. Als dit met een week of 4 niet helpt, dan zou ik zeker je stink voeten eens op de behandel tafel van je huisarts leggen.
[mfm80xr] (score 2, diepte 2) Miconalzonitraat is bij een 2% concentratie voornamelijk fungistatisch, tenzij je de behandeling langdurig voortzet. Je sterft dan langzamerhand de schimmel uit door de groei te remmen. 

Terbinafine is een fungicide en dood bestaande schimmels. Het middel is effectiever en heeft een kortere behandelingsduur nodig om hetzelfde effect te bereiken. Het is wetenschappelijk bewezen dat terbinafine beter werkt.
[mfngqrg] (score 2, diepte 1) Voor voetschimmel kan ik ook de tea tree olie spray van CHI aanraden. Twee keer per dag voor het aantrekken van schone sokken je voeten ermee inspuiten. :)
[mfnp98t] (score 2, diepte 2) Je zou het misschien kunnen gebruiken om de schimmel na een behandeling langer weg te houden, maar een stevige infectie haal je daar niet mee weg.
[mfltwm5] (score 2, diepte 0) Niks meer sexy dan een bedpartner  met sokken aan!
[mfn9ul0] (score 2, diepte 3) Bedoelde het in het algemeen, of kunnen vrouwen geen bedpartners zijn?
[mflunu9] (score 2, diepte 0) ik was mn voeten niet bewust. er spoelt wel water over tijdens het douchen
[mflv1rg] (score 2, diepte 0) Wissel dagelijks je schoenen en was savonds je voeten. Dunne sokken helpen goed en ademende schoenen ook. Ik merk zelf dat het heel erg uitmaakt welke schoen ik aan heb.
[mflv7ai] (score 2, diepte 0) Draag je sokken?
[mflx333] (score 2, diepte 0) Ik heb in huis eigenlijk altijd mijn schoenen uit. Dat scheelt al enorm.
[mfmb3ds] (score 1, diepte 6) En altijd zorgen dat je schoenen droog zijn voordat je ze weer aan doet. Zelfde met sokken.
[mflrqi2] (score 1, diepte 1 OP) Hmmm 🤔 Ik snap je punt maar 2x douchen gaat hem niet worden, en mijn haar kan echt niet zonder een kam in de ochtend met nat haar. 

Maar misschien toch maar ff die voeten gaan wassen voor het slapen ja. 😂 kut dingen zijn het ook ben er bijna een half uur per dag mee bezig zo
[mflut57] (score 1, diepte 2) Je kan ook smorgen met een natte kam je haar kammen, doe ik ook anders gaat het niks worden.

Zonder washand gaat het wassen wellicht ook een stuk makkelijker, vind ik iig wel.
Een washand is nogal een nederlands onding, de rest van de wereld kent zo'n ding niet en met je vingers kom je ook makkelijker tussen je tenen enz.
[mfm8t9q] (score 1, diepte 2) >en mijn haar kan echt niet zonder een kam in de ochtend met nat haar. 


Vroegah toen ik als kind krullen had, spoot mijn moeder mijn haar elke ochtend nat met een plantenspuit voor ze het kamde. Das ook een optie
[mflrwie] (score 1, diepte 1 OP) 5ml Dior luchtje in mn thee gooien, moet vast werken!
[mflrvoz] (score 1, diepte 0) Met water
[mflsbgo] (score 1, diepte 0) Ik was m’n voeten eigenlijk nooit. Ik douche dagelijks en doe dagelijks schone sokken aan. Ik droog m’n voeten wel goed af trouwens.

Mijn man heeft vaak stinkvoeten, maar hij heeft ook altijd z’n schoenen aan en trekt niet dagelijks schone sokken aan.
[mflsxr5] (score 1, diepte 1) Ieuw, je voeten moeten wel gewoon ademen hoor. 24/7 op sokken of schoenen is een no go
[mfltefb] (score 1, diepte 1) > horen voeten niet te stinken

Waar zweet is, zal stank zijn
[mflv1td] (score 1, diepte 4) Ja in dat geval kan het wel een merkwaardige odour krijgen...
[mflsn0j] (score 1, diepte 0) Was je je voeten met gewone douchegel of zeep? Misschien heb je iets antibacterieels nodig, zoals een zeep met tea tree oil. Scrubben helpt ook om dode huidcellen te verwijderen, want bacteriën houden van die huidresten
[mflszsu] (score 1, diepte 2 OP) Talkpoeder is een goed idee ja. Ik droog ze goed af ook tussen de tenen al hoewel ik in de ochtend nog wel eens haast kan hebben.
[mfn5zwx] (score 1, diepte 3) Ook na goed drogen kunnen je voeten nog iets vochtig zijn. Even "uitdampen" voordat je sokken aantrekt kan helpen. Na het douchen ben je vaak wat warmer, ook je voeten en dan sluit je die op in schoenen waardoor de warmte niet weg kan, krijg je ook extra zweet (zweten = koelen).
[mflvfo3] (score 1, diepte 3 OP) Ik denk ook dat het probleem van de schoenen af moet komen eigenlijk ja. Vele in de thread zeggen schimmel maar ik zie daar geen aanleiding voor. 

Voor ik het huis uit ga stinken ze nooit maar dan kom ik terug vooral na stappen en dan stinken ze. Ik ga even kijken hoe makkelijk het is om aan zo'b ding te komen hier. Zou wel weer achterlijk duur worden 😂
[mflt0zt] (score 1, diepte 0) Ik gebruik soms Pedicare in de zomer. Het stinkt enorm, dus aanbrengen met een handschoen is geen overbodige luxe. Voor mij werkt het goed!
[mflv5jf] (score 1, diepte 1) waarom geen miconal? werkt best goed
[mflv269] (score 1, diepte 1 OP) Ja joh? 😂
[mfm9cti] (score 1, diepte 2) Nee
[mfn5coe] (score 1, diepte 1) In sommige gevallen is er een goed excuus voor. Als je zelfbewust bent over je voeten dan ga je daaraan denken en kun je minder genieten. Vrouwen hebben vaker koude voeten en een orgasme krijgen of uberhaupt opgewonden blijven gaat dan ook lastiger. Dus ja... Daarbij hoeven het natuurlijk geen typische witte sportsokken te zijn, er zijn ook wel charmantere opties te vinden.
[mflu61m] (score 1, diepte 0) Dagelijks onder de douche
[mflv015] (score 1, diepte 0) Voetschimmel/zwemmers eczeem? Als het droog en rood is tussen je tenen is dat wel een indicatie. Ook een hele tijd last van gehad en daar gaat ook alles van meuren. Hardnekkig maar is zalf voor
[mflvf7s] (score 1, diepte 0) Zweetvoeten is iets wat niet “normaal” is en is meestal een teken dat er ergens in een proces in je lichaam is wat niet helemaal “goed” verloopt. 

Uiteraard is het goed om synthetische materialen te vermijden. Draag dus schoenen met een binnenzool van leer, suede of katoen. Laat deze regelmatig luchten (dus niet elke dag dezelfde schoenen dragen), het liefst in de buitenlucht, want zuurstof en daglicht en kou daar houden bacteriën niet zo van. Draag sokken van wol, bamboe of 100% katoen.

Maar kijk ook zeker eens naar je voeding. Veel troep in je lichaam zorgt voor stinkend zweet. Rook je? Drink je regelmatig alcohol en frisdrank? Eet je veel bewerkte en kant-en-klare voeding? Ga daar eens mee minderen.

Drink je daarnaast voldoende water (2 liter per dag) en sport je regelmatig? Al die afvalstoffen die we dagelijks binnen krijgen worden (gelukkig) ook weer door het lichaam afgescheiden. Als dit er teveel zijn of er onvoldoende mogelijkheid is dit via de urine af te scheiden dan gaat je lichaam andere manieren zoeken om het kwijt te raken. Bijvoorbeeld dus door overmatig zweten, waarbij het zweet ook nog eens kan stinken.
[mflxrlg] (score 1, diepte 0) Ik heb m'n leven lang al willen weten
Waarom zweetvoeten zweten
Worden die voeten soms niet vaak genoeg ontsmet
Of eten de eigenaren simpelweg te vet
Zit 't in de genen opgesloten
Of hebben ze hun tenen soms gestoten
Ligt 't aan 't bloed of ligt 't aan de vaten
Hoe 't ook zei: je kunt er moeilijk over praten
Maar het is en blijft een feit
Er zijn van die voeten, die stinken altijd
Zou er iets tegen te doen zijn
Of niets tegen te doen zijn

Overigens was ik gewoon m'n voeten onder de douche. Gewoon zo met m'n hand en wat shampoo. Wat voor mij werkt zal voor jou niet werken... succes met de puzzel
[mflzgh2] (score 1, diepte 0) Sowieso geen sokken van synthetische materialen gebruiken maar van katoen
Ik heb een jaren terug een tijdje pedispray gebruikt en sindsdien geen last meer van stinkvoeten

Verder douche ik elke ochtend waardoor ze in de sop staan te plonzen, dat werkt bij mij prima
[mfm7a5k] (score 1, diepte 0) Ik heb helemaal geen n̶e̶u̶s̶ voeten.
[mfxexzc] (score 1, diepte 0) Leren schoenen, om de dag wisselen (kunnen ze drogen), katoenen of bamboe sokken, open sloffen, voeten wassen met water....
[mge1cew] (score 1, diepte 0) vaker van schoenen wisselen. Geur zit in je schoenen niet in je voeten.
[mfnqr4b] (score 0, diepte 1) Wat voor ding?
[mflsqlj] (score 0, diepte 1 OP) Hugo Boss schoenen, geen idee wat voor model het is. En gewoon ja, sokken 😂 Thuis loop ik op slippers aangezien ik in Caribisch Nederland woon.
[mfn736e] (score 0, diepte 2) OP is geen vrouw
[mfqfjnk] (score 0, diepte 4) Wat een rare vraag
[mfls4kx] (score -1, diepte 0) Damn jij moet wel echt flink stinken
[mflqt6b] (score -2, diepte 0) Je moet wat in van die visjes investeren.

=== THREAD r7wbfp ===
SUBREDDIT: r/pharmacy
DATUM: 2021-12-03  SCORE: 21  REACTIES: 58
TITEL: What shoes do you wear and recommend?
POST (source_id=post):
We're on our feet for long hours and long days, most likely on cold hard floors.

What have been your favourite brands/shoes/models for **comfort?**

&#x200B;

Edit: Hoka One Ones are dominating the recommendations!

Edit2: Bought Hoka One One Bondi

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hn2bvu6] (score 26, diepte 0) Danskos with compression socks! The socks definitely help!
[hn2l65e] (score 21, diepte 0) Hoka One Ones. Makes me wanna run everywhere.
[hn29kds] (score 12, diepte 1) +1 for ultraboost, very comfy for on your feet all day long and they look nice also imo
[hn27fu0] (score 11, diepte 0) My work line up consists of ultraboosts and prestos
[hn31qp5] (score 8, diepte 0) Brooks, Mizuno, and occasionally Superfeet inserts.
[hn59rek] (score 7, diepte 0) Clown Shoes
[hn3aal1] (score 6, diepte 1) The colors make me less depressed
[hn24hde] (score 5, diepte 1) SAS. They’re not stylish, but they feel great to stand in all day!
[hn3fhb2] (score 5, diepte 1) LOVE my Super feet inserts!!!
[hn295j1] (score 4, diepte 0) ECCO. I have never found a brand of dress shoe as comfortable and durable as ECCO. And the fit is reliable when I order online. I just ordered some hybrid dress shoes ( leather dress top with a gym shoe style sole) for the first time on cyber Monday and am anxiously awaiting their arrival.
[hn29goc] (score 3, diepte 0) I buy all my shoes for comfort, aside from shoes I'll need for very specific reasons.

Though the winter season I'll likely have my blundstones  on most days. I also find Romika (sister brand to Josef Siebel) foot beds very comfortable. Sketcher is another that I wear.
[hn32u7g] (score 3, diepte 0) Hoka One Ones, but I need to advise you, take two pairs of shoes and just change mid-day. Try it immediately, you’ll notice a difference.
[hn5m3yo] (score 3, diepte 0) Hoka Bondi. They are super ugly, but worth it. I used to only wear brooks. I can only wear them to work now on a “short shift” (8 hr). I have 3 pair of the Hoka Bondi and rotate them each day.

I also recommend compression socks. Figs are my fav, plus they have cute pill themed ones. Even though my shoes are ugly, my socks are cute. I’ve tried cheap ones from Amazon & the figs are definitely worth it.
[hn5agk0] (score 2, diepte 3) Flat feet is not an excuse for being obese. You clearly do not have flat feet or apparently even believe in their existence. It seems more like you're just a piece of shit.

I was discovered to have flat feet when I was a child because my footprint would be my entire foot. I had to wear arch building inserts to help develop an arch. I have an arch now, but I know if I don't use something with good support I might have my arch collapse and have flat feet again.
[hn5rn93] (score 2, diepte 7) Keep comments professional in this subreddit.
[hn3ly3l] (score 2, diepte 1) Those hybrids are solid as hell.  My pair served me well.  Only complaint I have is they are super squeaky on non-carpet floors
[hn2mbae] (score 2, diepte 1) The cushion really helps too
[hn2llfz] (score 2, diepte 0) Birkenstock
[hn2lx7d] (score 2, diepte 0) Crocs Neria Pro II. They’re not cute, but I don’t have nearly as much back pain now. Also, they’re super easy to clean.
[hn2y1rv] (score 2, diepte 0) Crocs.

(And Olu Kai slip ons because I decided at 25 that I was done tying shoes)
[hn5mz9y] (score 2, diepte 1) I just alternate my shoes and add day, but changing midday would be nice.
[hn3bxed] (score 2, diepte 0) Adidas ultra boosts but my podiatrist buddy says hokas are the best shoes by far, so I'm gonna look into those
[hn4i41f] (score 2, diepte 0) I love Hoka. I have one pair of tennis shoes and one pair of more cushy slip ons from the brand. Towards the end of the week I use the slip ons. I find it helps to change shoes mid day or mid week (depending on level of pain) because different shoes put pressure in different areas.
[hn5i2rk] (score 2, diepte 0) ASICS cumulus or nimbus depending on which are available in black at the time/less expensive. 

Are the Hokas good for high arches? I’m curious about them after seeing so many people recommend them!
[hn642b3] (score 2, diepte 0) I see a lot of people recommending them, but UBs are too soft for standing for long periods of time. They are made for running and are better for movement in general.
[hn1y047] (score 1, diepte 0) I wear all kinds of shoes. Dress shoes to sneakers to boots. Alden, Allen Edmonds, Vans, etc
[hn39enx] (score 1, diepte 1) I used to wear ultraboosts every day to work until I got a pair of the futurecraft 4Ds. Those shoes are on a different level. You can barely even tell you’re wearing shoes, 100% justified at $200/pair
[hn34u60] (score 1, diepte 1) I have Eccos too!
[i5cjykz] (score 1, diepte 1) Do you find they fit true to size? I may just have to go in store and try em . Can't decide on wide or regular
[i5du52l] (score 1, diepte 2) Try them. I bought them only after trying and comparing. Every foot is different.
[hn36cpr] (score 1, diepte 0) All black ultra boosts plus compression socks is a game changer.
[hn38wat] (score 1, diepte 0) Hoka one one
[hn3kxc3] (score 1, diepte 0) Nike SB Force 58 right now, was wearing Nike SB Charge before that.

I work hospital though and skate shoes look fine with my scrubs.  I wore Nike SB shoes when I was an intern at Walmart though because they are familiar to my foot and actually have a lot of support for obvious reasons.

Also… Running shoes with business casual looks awful.  Sorry not sorry.

If I have to wear business casual I wear RockPort dress shoes.
[hn3mm5r] (score 1, diepte 0) 2-4 pairs of top of the line running shoes and never the same pair twice in a row. Each pair will run you $150+
[hn3r36k] (score 1, diepte 0) ASICS Cumulus-Gel
[hn3uhv7] (score 1, diepte 0) I wear sketchers. They’re the only shoes that don’t hurt my feet
[hn3upx5] (score 1, diepte 0) On a side note. I wear compression socks. Which help a lot.
[hn3xmvn] (score 1, diepte 0) Puma brand shoes. And don’t think they’re expensive you can find them for 35. They just fit my feet well and give me some pep in my step.
[hn445zw] (score 1, diepte 0) Cloudflows as an all purpose, Trask if I wanna look put together (so they've been unused for a while lol), Trask again if I want a boot, and Adidas x White Mountaineering if I wanna be trendy. Sometimes Nike AF One's.
[hn4766y] (score 1, diepte 0) Brooks, Merrell and Crocs are my go to!
[hn4jscr] (score 1, diepte 0) Allbirds are great honestly. I recommend the weather resistant version, they’re much better engineered and only $20 more
[hn4m6ji] (score 1, diepte 0) Allegria
[hn4o6py] (score 1, diepte 0) Hoka is the best
[hn4t2us] (score 1, diepte 0) On Cloud! Had Hokas, these are better.
[hn5masg] (score 1, diepte 1) Really?! I 100% disagree. I HATE my on cloud. As far as looks go, they look way better. I wear them when I’m off, but to stand 12 hr a day- Hoka Bondi is the way to go.
[hn4vazq] (score 1, diepte 0) Skechers!
[hn4w60a] (score 1, diepte 0) Adidas cloudfoam! So comfy
[hnz95wx] (score 1, diepte 1) This made me LOL 🤡
[hn59wtv] (score 1, diepte 0) Adidas with cloudfoam. I've had a few styles, but the cloudfoam is what is good about them.
[hn5lxp3] (score 1, diepte 0) vans ultra range
[hn5qypo] (score 1, diepte 0) I just bought Ugg CA805 (so random) but boy, was I impressed. So comfy!
[hn5rpg8] (score 1, diepte 0) I wear my dress crocs
[hn5z0k5] (score 1, diepte 0) Probably the only one, but I like my zero drop shoes (have worn a few different brands). Run a lot and prefer to wear brooks or new balance when I run because of my wide toe box, but at work use zero drop shoes

Also have one of those calf stretchers I can hop on for a few minutes to help the calf’s for the long days
[hn65zbx] (score 1, diepte 0) Altra escalate
[hn7bxy3] (score 1, diepte 0) The one i used to wear as a kid w a secret compartment in the tongue lol!!!
[hn9o1ig] (score 1, diepte 0) Haven't tried Hokas yet but I can say Danskos and Ultraboost made my feet hurt. Brooks have been amazing for me. I have two pairs I swap out. Also I've been wearing calf length compression socks for about 5 years  but doc just recommended I switch to 20-30 mmHg thigh high compression.
[hnyszc5] (score 1, diepte 0 OP) Bought Hokka one ones on overwhelming advice, let's see how it goes...
[iib3tep] (score 1, diepte 1) How’s this working for you? Looking to purchase one
[iiblsxo] (score 1, diepte 2 OP) I love them, I've been wearing them a bit over 6 months and they prevent me from feeling tired despite standing for 8 hours a shift. Other shoes, I'd start feeling the burn from standing after 3 hours.
[hopyt2x] (score 1, diepte 0) I always rocked new balance 515's. Most comfortable shoe for me.

=== THREAD 1j33wbz ===
SUBREDDIT: r/pharmacy
DATUM: 2025-03-04  SCORE: 15  REACTIES: 58
TITEL: Shoes for standing
POST (source_id=post):
What kind of shoes are you guys wearing to work?  at times we are standing for a longer period of time and my feet ache so bad. It’s easier when we’re at least walking around or moving them so often. Just standing is getting harder with the pain at the end of the day. Any recommendations? Brand? Shoe-line? I’m looking a mid option. Not too cheap but not so expensive either. Somewhere in the middle. I’m open to any suggestions, thanks

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mfx0sue] (score 26, diepte 0) Brooks
[mfx8xl1] (score 14, diepte 0) I haven't tried much else but Ultraboosts have been the best things I've found.
[mfx0jhl] (score 8, diepte 0) If you have high arches Dansko clogs are nice, you break them in for 2 weeks and then they mold to your feet and you can stand for long hours without as much pain at the end of the day. That last for years. If you’re interested in other shoes the nursing reddits have great recommendations.
[mfx2xnj] (score 8, diepte 0) Dansko saved my feet. Nothing else helped.
[mfx7srn] (score 8, diepte 0) I rotate, Brooks, Hoka, On Cloud.
[mfy6k5z] (score 7, diepte 1) Brooks all the way!  Another little tip I picked up from an older pharmacist was to change shoes mid-shift.  Just a little different fit helps your feet so much!  I hope this helps!
[mfxbyp0] (score 7, diepte 0) I actually switched to barefoot shoes and my feet are so much more comfortable. When my feet would ache in work I'd take my shoes off and walk around on my socks and they felt so much better so that's why I switched to barefoot. Now I wear them exclusively all the time
[mfyfym8] (score 6, diepte 1) Hoka is my go to too.
[mfz4fr1] (score 5, diepte 2) I have multiple pairs and when I worked retail I noticed it worked best if I alternated days to give the shoes time to plump back up!
[mfx74xg] (score 5, diepte 0) Asics running shoes. Feet still a little achy but a lot better for sure.
[mfx11da] (score 4, diepte 0) i love my cloves. they’re advertised as nursing showed but they are comfy and have some fun colors!!
[mfx1k3o] (score 4, diepte 0) I’ve found I can stand pretty long with any pair of running shoes so long as I have compression socks. Have you tried those? 

Otherwise Costco has a great pair of Nikes running shoes for $30 right now that’s super comfortable.
[mfz2rkk] (score 3, diepte 1) Brooks are everything to me. Spent 3 years working as a pharmacist trying all the Nikes and new balance until I got brooks. Magic. 50
Hours on my feet in brooks feels better than a single shift in Nikes. I will never ever ever go back, and if I could buy everything from flip flops and sandals and heels and boots from brooks, I’d never own shoes from anywhere else. But sneakers for sure I will never leave brooks. I’ve now got 3 pairs and my feet have been living blissfully for the last 2 years
[mfx7zkl] (score 3, diepte 0) I rotate between adidas, dansko, kitchen crocs (no holes) and lined crocs on cold days.
[mfx82fd] (score 3, diepte 0) Dansko/Sanita clogs+ compression socks.
[mfx9ddv] (score 3, diepte 0) Danskos cured my post-pregnancy plantar fasciitis. I can’t work in anything else.
[mfy8jsg] (score 3, diepte 1) Barefoot shoes saved my feet and knees. I have Morton’s toe (big toe shorter than the next) and was getting corns pretty regularly with other athletic shoes along with aching knees. Switched to xeros and merell barefoot style shoes about 8 years ago. First several months were not very comfortable but my foot changed fit the better. It’s wider and stronger. I have no issues with corns and no knee problems…and I’m 8 years older. Barefoot zero drop all the way
[mfxml2f] (score 3, diepte 0) shoes are great but u need those anti fatigue mats. Those really make the differenxe
[mfx7i3y] (score 2, diepte 1) It takes a week, but it's the best after that.
[mfxeylh] (score 2, diepte 1) Agreed! So comfy.
[mfxg7gc] (score 2, diepte 2) Right? I’ve tried a few out there. Dress shoes were not comfortable. Dansko’s were yuck (seriously don’t know how anyone can stand them lol) Brooks felt too much like sneakers/didn’t go with the rest of my outfit. Visited a Fleet Feet and they analyzed my feet and recommended a great pair of Asics. I told them I wanted a comfortable running shoe but one that was great for standing on my feet long hours. Tried them and haven’t looked back. I even found some black ones eventually that look better with my attire. Can’t say enough good things about them!
[mg279bv] (score 2, diepte 3) I was just about to type this. I went to a Running Room and they examined my gait and recommended these. These changed my life! I stand for hours and no aches and pains unlike my previous Skechers. I do want to try On and Hokas just so I can switch between them.
[mfxacy5] (score 2, diepte 0) I got fitted for insoles. As long as they’re in whatever shoes I’m wearing, I’m good.
[mfxjl8i] (score 2, diepte 0) I've used all the shoes listed here.


My Hokas lasted about a year before falling apart. Ascii is my favorite. Get 2 pairs of shoes that you train out at the 6 hour mark of the 12 hour shift.
[mfy49o8] (score 2, diepte 0) Birkenstocks every day and my feet never hurt anymore
[mfy73xb] (score 2, diepte 0) COMPRESSION SOCKS.   Game changer.  Pricier than regulat socks, but a GAME CHANGER.
[mfy74ee] (score 2, diepte 0) Vibram five fingers all day every day. Once you've built the strength and dexterity back into your feet, you don't need anything else.
[mfybui6] (score 2, diepte 0) Hoka
[mfyftul] (score 2, diepte 0) Hoka all the way, they are a thick sole running shoe designed for running on rocks and sticks. They are expensive but thru the years I have found several pairs on discount at Zappos outlets. One time I had a brand new pair, I accidentally left at my sisters house  ( a nurse). She confiscated them and actually wore them out.
[mfyyvu0] (score 2, diepte 0) ASICS gel nimbus 25 or 26 are the best I’ve found. I’m on my 3rd pair because they do wear out unfortunately.
[mfzkdwr] (score 2, diepte 0) Get fitted for orthotics. Before i went to a foot doctor my feet ached no matter what shoes i wore. Got bursitis and it was agony. Saw the foot doctor out of desperation and he fitted me for custom orthotics which took a while to get used to but once i did, i never looked back. I switch them from whatever I’m wearing: work shoes, hiking boots, hell even in my wading boots when I’m fishing. Highly recommended because we make our living on our feet
[mgc6vp0] (score 2, diepte 0) I used to wear hokas (plus compression socks) but honestly my feet still hurt with those. I now have a pair of puma sneakers from costco (plus compression socks) and honestly my feet never hurt anymore even after like 11hrs on my feet
[mg1d8zw] (score 1, diepte 1) That’s all I wear as well
[mfycepy] (score 1, diepte 2) Oh my big toe is like that too, didn't know there was a name for it!! I only started in August with barefoot and I do love them, they are so so comfortable, I've changed all my kids to barefoot shoes too (3 of them)
[mfxeihk] (score 1, diepte 0) Dansko and Doc Marten back when I worked retail.  Nowadays I can wear gymshoes and the best ones for my feet are probably Hokas.  Compression socks are also important.  I didn't start wearing them until I was older and now I regret it.
[mfxh5mc] (score 1, diepte 0) I wore Ecco dress shoes for 20 plus years, but I’m now wearing Brookes with custom orthotics!  May look ridiculous, but damn my feet hurt!
[mfz3tho] (score 1, diepte 1) Is there a certain brand you recommend? At Walgreens we had antifatigue flooring PLUS a Mat on top and it felt like that made no difference. But when I switched shoes to brooks the difference was HUGE and immediate. Then I moved to a smaller grocery store pharmacy that doesn’t have antifatigue. My feet and knees feel great still, because of the shoes, but I’m wondering if they could be better if I got a decent anti fatigue mat? Just maybe not the styles I’d experienced before since they didn’t seem to offer relief
[mfy0ptl] (score 1, diepte 0) I wear Clarks and they have been fantastic
[mfy2agd] (score 1, diepte 0) Clark’s and compression stockings (I use the ProCompression brand).
[mfy5pyy] (score 1, diepte 0) I ordered compression socks from Amazon. I wear them daily with Sketcher memory foam sneakers.
[mfy5tpr] (score 1, diepte 0) Rotation:
Brooks, onclouds (my fav), crocs, hokas
[mfy6h8z] (score 1, diepte 0) On cloud shoes
[mfy797h] (score 1, diepte 0) Sketchers! I just switched and they are great
[mfy837x] (score 1, diepte 0) Sketchers go walk. They have the added bonus of actually looking like shoes too.
[mfya0z3] (score 1, diepte 0) This is one of the most common posts in this sub, so if you want additional recommendations beyond what’s commented in here, I’d just search the sub for “shoes”
[mfybq3g] (score 1, diepte 0) Propet. Not talked about much but the best I have found!
[mfyibjj] (score 1, diepte 0) Hoka with custom insole. It will save your back in the long run. Source: me, 21 years of experience in outpatient pharmacy setting.
[mfyr795] (score 1, diepte 0) I have been wearing Nike Air Monarchs for at least 2  decades. I've been on the lookout for something else. I've read about hiw good Hoka's are and decided to try a pair. They felt OK in the store so I bought them. Wore them to work bringing my Nikes with me. After a few hours, a lot of little things really started to bother me. They were tight across my foot, loosening the laces didn't help much.  My heel never felt as if it were all the way in the shoe. Felt like it was going to keep coming out. Couldn't get used to my toes feeling higher than my heel and that they never touched the ground. Also, I couldn't get used to being so tall!!! I returned them, tried on different brands but could not find anything that I  liked. Maybe it's running shoes I don't like. 

Are there any good WALKING shoes I should look at?
[mfyunvz] (score 1, diepte 0) No shoe will prevent the problems caused by standing in one place for hours. You need to move more. It’s hard at first but with time you can learn to move around without wreaking workflow.
[mfyyu46] (score 1, diepte 0) Allen Edmonds shoes. Expensive, but last and since I switched, less foot and back pain.
[mfzn9nv] (score 1, diepte 0) Brooks Ghost. The latest version is pretty pricey, I think mine were $140 less a DSW coupon, but you can get last year's for a lot less.
[mg0gsml] (score 1, diepte 0) I would honestly recommend Crocs if you are allowed to wear those
[mg0r2gy] (score 1, diepte 0) I was wearing Yeezy's but can't really justify supporting Kanye anymore, now I wear Adifom Q's
[mg0vu7s] (score 1, diepte 0) Oofos
[mg21faw] (score 1, diepte 0) I have Dansko, Hoka, New Balance, On Cloud and Allbirds. I rotate and never wear the same pair 2 days in a row. I’ve been doing this for 30 years! Also you need to buy support socks.
[mg2a7to] (score 1, diepte 0) I use the Sketchers Work shoes that have a full memory foam insole. Anytime I need new shoes, I just buy the same kind again because I like them so much.
[mg3pa1h] (score 1, diepte 0) ASICS Gel Nimbus 25. It feels like waking on a cloud.

Also, always buy 2 pairs of the same shoe you intend to wear 8+ hours a day and rotate them.
[mg4ve1n] (score 1, diepte 0) Hokas + compression socks for life
[mgrnrn9] (score 1, diepte 0) Merrill encore.  So comfortable and long lasting.
[mgssx8b] (score 1, diepte 0) Rieker
[n1honw8] (score 1, diepte 0 OP) Thank you guys for all the suggestions!
[mfxenfb] (score 0, diepte 0) I wear a pair of Mammut approach shoes. All black so work with uniform policy.  

I've always found that hiking shoes are great as work shoes.

=== THREAD 1ejj4zb ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2024-08-04  SCORE: 36  REACTIES: 58
TITEL: How do you guys deal with foot pain?
POST (source_id=post):
I just recently got back into the industry after an extended period of not working and it's killing my feet. Granted I'm not wearing the right foot wear to be on my feet all day (y'all know how it is). I was just curious what everyone uses to keep their feet comfortable (shoes, insoles). Thank you so much for whatever feedback. I love my job, but I need to figure this out lol

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lgdyqvo] (score 31, diepte 0) Besides the shoes/insoles, get some knee-high compression socks. It's a game-changer for pain from swelling/fluid buildup in your feet.
[lgdzilb] (score 24, diepte 0) Apart from proper footwear, posture is key. Yoga does wonders for foot and back pain.
[lgel7nr] (score 22, diepte 0) >I'm not wearing the right foot wear to be on my feet all day

....
[lgdyssy] (score 9, diepte 0) Red wing brand work shoes with insoles. Thank me later 😉
[lge52zh] (score 9, diepte 0) You'll get used to it, but I like Dr Scholl's shoes. But the biggest thing is time, seriously, for your first two weeks it's really aggravating, but it'll get better. I've left and rejoined the industry a few times and my first days are killer standing at first.
[lgdz1pq] (score 8, diepte 1 OP) This will definitely help. I've been cooking for ten years and took some time off and apparently didn't age well lol
[lge5odk] (score 7, diepte 0) I wear running shoes with good arch support.  If you're overweight.. well you know I dont' need to say it.  Standing still can lead to some pretty serious foot pain, I try to keep moving as much as I can. Offer to put away deliveries, jump on dish between tasks stuff like that helps, for me anyhow.
[lgf68o3] (score 6, diepte 1) Cut 5 potatoes, do a little twirl.
[lgea04i] (score 6, diepte 1 OP) This took me a minute lol
[lgeh6oq] (score 6, diepte 0) If you aren’t doing a regular calf stretch several times throughout the day I highly recommend you begin. Tight calves can really put a ton of strain on your plantar fascia which will give you massive pain in your feet. 

I’ve flipped to the Foodservice Equipment Sales side of things now and I still take time to stretch every couple of hours just to keep it up.
[lgermpj] (score 5, diepte 1) Things changed when I started wearing knee high compression socks!
[lgfk99d] (score 5, diepte 1) Second this. Stretching has great benefits for legs and feet. You will be surprised that stretching your hips will ease the feet ache.
[lgevuyq] (score 5, diepte 1) Yep, used to do seasonal work, the first few weeks were rough
[lge9r2w] (score 5, diepte 0) Use meters?
[lgei7x3] (score 4, diepte 0) I smoke a lot of cannabis. It seems to help.
[lggeoeh] (score 3, diepte 2) Anyone who has high arches will unfortunately have to  spend more on insoles unless they’re allowed to cook in running shoes. Getting custom inserts can do wonders. Giving up doing 14 hour shifts on concrete is better though.
[lge0od0] (score 3, diepte 1 OP) Thank you I'll set up an appointment as soon as I get a day off lol
[lge4pfu] (score 3, diepte 0) Inserts in my boots work for me
[lgfu2p1] (score 3, diepte 1 OP) Obviously I know what the issue is, for the most part. The point of the post was to get some opinions before I went I dropped money on a new pair of shoes/insoles
[lgelcfh] (score 3, diepte 0) For me it was losing weight. 

I asked a lot like you are doing and everyone was like... yeah, insoles, oh special socks... 

At the end of the day, for me, going from 90kilos to 78 was the game changer
[lgdyy3g] (score 2, diepte 1 OP) Thank you I will definitely look into them
[lgf3qe8] (score 2, diepte 1) If your shoes need insoles then your shoes suck. More than one way to skin a car and all that, expensive shoes and no insoles or cheap shoes and good insoles both work. But if you're spending money on both then you're doing it wrong.
[lgdzevc] (score 2, diepte 0) I use the sketchers cessnok(or something like that) haven’t looked back. Not waterproof but keeps most out
[lge0frq] (score 2, diepte 0) Real shoes, not crocs...and a pair of $300 inserts I got from a podiatrist. 

Before that I was limping for almost a year and didn't even realize it until I went to visit my mom and she gave me shit. _(it doesn't help that I stand on the balls of my feet all day)_
[lge1yyx] (score 2, diepte 2) Yeah, I know, right.

Like I said, I didn't even notice I was limping, foot pain is just gets normalized.
[lge25h8] (score 2, diepte 3 OP) Yeah it's no good. Thank you so much for the advice I'm definitely going to look into this
[lge32mq] (score 2, diepte 0) Birkenstock Bostons will save your feet and lower back.
[lge42ar] (score 2, diepte 0) I buy new shoes yearly   We work a lot   Take care of yourself   I get this wicked callous on my right little toe that’ll tell me when it’s time to change shoes from all the shifting
[lgi7qoa] (score 2, diepte 2) Punch out some fries ---> pirouette --> repeat
[lge9558] (score 2, diepte 0) I like New balance with a really good pair of insoles and good work socks. They have made a world of difference. Even when I was pregnant and working 12hr days they helped. Hope you find something that works for you.
[lgejjc2] (score 2, diepte 0) One thing that's helped me a lot is using something like a lacross ball to roll my feet on when I'm home. Good size and hardness to give em a good massage. Can use it to help stretch your toes out which was a gamechanger for me. Feels weird to type out lol but that's one simple tool that helped me a bunch.
[lgejjqz] (score 2, diepte 0) One thing that's helped me a lot is using something like a lacross ball to roll my feet on when I'm home. Good size and hardness to give em a good massage. Can use it to help stretch your toes out which was a gamechanger for me. Feels weird to type out lol but that's one simple tool that helped me a bunch.
[lgeuo38] (score 2, diepte 0) Get stiff orthotic insoles!! Cushy ones feel nice, but you need stiff arch support to stop the instability in the foot. I had a major foot injury, 2 surgeries, snapped tendons, 10+ broken bones in my foot. Carbon fiber insoles and stiff shoes saved my life for real
[lgfz9sj] (score 2, diepte 0) Proper foot wear is everything.  Birkenstocks make my feet and back happy.
[lgg0287] (score 2, diepte 0) Besides the obvious footwear issue, it's going to take some bit for your body to adjust to being on your feet all day again.  You haven't used those exact muscles in that way in a bit and they need time to be built back up.
[lgge1ya] (score 2, diepte 0) If you’re in a single spot for extended periods of time stand on a broken down box, it helps a lot
[lgix0ga] (score 1, diepte 1) Facts
[lgjj1vu] (score 1, diepte 2) Third this. It fixed all of my work related pain problems. And good for the mind too
[lgf2j0b] (score 1, diepte 1) Ive been wearing bistro crocs for the past 3 years or so and love them. I’ve tried a horde of shoes over the years. Everyone’s foot is different.
[lgehecp] (score 1, diepte 0) Thug it out pretty much. It doesn’t hurt until i stop working/start heading home
[lgej2qy] (score 1, diepte 0) The real answer is it never stops hurting you just get used to the pain.
[lgh5g1e] (score 1, diepte 1) Protip: freeze a small bottle of water roll your feet on it. It feels sooooo good.
[lgek28j] (score 1, diepte 0) New Balance + Footminders Insoles is the best combo for me
[lgeqkob] (score 1, diepte 0) Never had any issues. Rotate three pairs, Crocs, Chucks, bragard, go barefoot and yoga. Take care of my feet weekly.. Could be genics..
[lgfavp0] (score 1, diepte 0) Get a good pair of insoles and a good pair of shoes. Not sure your location but places like fleet feet or the new balance store can sell you the insoles and also size you properly to make sure you're wearing the right size (which, believe it or not, is a fairly common problem and makes for a large portion of the adult population).
[lgfj04l] (score 1, diepte 0) Personally I go flat arch shoes and streches before bed. If your coming back it takes some time to build that strength in your feet again. About a week maybe two.
[lgftqm4] (score 1, diepte 1) My wife just suggested sex after she puts our kid to sleep. I can't wait to see the look on her face when she sees me pull it out...a tennis ball that is 😂
[lgfmmbt] (score 1, diepte 0) Crocs the bistro style. I used to change shoes mid shift daily and never wear them past 3 months but since I've gotten the ugly fuckers I've had them 2 years and wear compression socks daily and I never have foot pain now!
[lgfov4g] (score 1, diepte 0) Proper footwear with ball of the foot heel and arch support, socks with the right combination of compression and padding (I use Darn Tough socks with mid-level cushion), and pilates.
[lgg4mzi] (score 1, diepte 0) Turned out I just had gout, I take 300mg of Allopurinol daily and I’m fine.
[lgg9ekx] (score 1, diepte 0) Buy some Birkenstocks 

They have. Break in period but after that most comfy shoes ever, in and out of the kitchen ! 

Super birkies or their slipper style pricey but worth it if you care about your back / feet!
[lgh6kci] (score 1, diepte 1 OP) This seems like a valid option.
[lggtcoe] (score 1, diepte 0) I’m 51, been doing this for almost 30 years. I gave up “cool” trendy chef shoes after battling plantar fasciitis for years. Doc martens saved my career. Ironically they are trendy again. I recommend the non slip Chelsea slip on boots with non cotton socks.
[lghg4w0] (score 1, diepte 0) Soaking in a hot tub & regular pedicures.  Foot massages can work wonders.
[lgitzd7] (score 1, diepte 0) Not slip resistant, but OCs saved me the last few months.
[lgk64nh] (score 1, diepte 0) Bring an extra pair of well ventilated socks to change halfway through your shift, especially if it’s a long one! Save my bacon many times. Get some good shoes don’t wear fucking vans.
[lgk8enf] (score 1, diepte 0) Hokas and compression socks. Have to do lots of calf stretches too.
[lgnlesi] (score 1, diepte 0) Are you overweight? 
What I noticed is that the best way to avoid any of the common pain is to be fit. It has been working.
[lgujcwq] (score 1, diepte 0) what kind of shoes are you wearing? definitely get some good insoles. I've tried every brand of insoles on the market. Ultimately, I switched from my custom insoles to this brand called [Fulton](https://walkfulton.com/) and nearly immediately my foot pain went away (and back pain). These are made from cork so they mold to your arch and absorb shock/impact. a bit pricey but obviously way more affordable than custom, and really comfortable.
[ll9y6eq] (score 1, diepte 0) Proper footwear or insoles. I'd first try insoles as they're less expensive compared to new shoes. I personally recommend akusoli, I fell in love with them:) so so comfy, especially when I know I'll be walking or standing a lot.
[lgfkuqs] (score 0, diepte 0) Tennis ball on the floor and roll it with your feet with pressure. Better than sex
[lgg9myp] (score 0, diepte 0) Cut off both my feet and replaced them with robotic feet.

