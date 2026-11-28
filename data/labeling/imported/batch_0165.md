# Label-batch batch_0165

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
Schrijf het resultaat naar `batch_0165.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1m7y5mf, 14igt3b, 12l2iqt).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1m7y5mf ===
SUBREDDIT: r/nederlands
DATUM: 2025-07-24  SCORE: 694  REACTIES: 317
TITEL: Voeten op het dashboard
POST (source_id=post):
Wie doet dit en ben je er van bewust van de gevaren bij een ongeval?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[n4v23gn] (score 788, diepte 0) Mijn ex-vriendin deed dat ook wel eens, hebben we op vakantie nog een flinke ruzie over gehad omdat ik weigerde door te rijden terwijl ze haar voeten op het dashboard had.

Uiteindelijk heb ik haar een paar gore foto's laten zien van mensen die dubbelgevouwen waren omdat ze hun voeten op het dashboard hadden en toen was ze wel genezen.
[n4v37ai] (score 394, diepte 0) Toen ik nog lesgaf in Vlaanderen kwam er een politieagent voorlichting geven aan klas 2 en die vertelde ook dat het supergevaarlijk is om de benen op het dashboard te zetten. Sommige kinderen geloofden dat niet en toen heeft hij een paar foto's laten zien. Ze waren allemaal meteen overtuigd.

Hij vroeg ook of iemand van hen de gordel onder de arm draagt. Hij had een stuk gordel bij zich en hij vroeg zo'n kind om dat even voor te doen. Toen liet hij zien wat er gebeurt bij een ongeluk: de gordel trekt strak en knalt tegen de arm aan. Hij had al eens afgerukte armen enkele meters verder van het asfalt moeten rapen. Als iemand het niet geloofde, kon hij wel wat foto's laten zien.

Het was allemaal pedagogisch niet erg verantwoord, maar die kinderen doen dat gegarandeerd nooit meer.
[n4v2g34] (score 217, diepte 0) Dit doe ik altijd als bestuurder. Je hebt niet voor niets cruise control toch? 

Denk dat die foto's wel meevallen, de medische zorg is tegenwoordig erg goed.
[n4v3zj4] (score 215, diepte 1) Bruut maar het werkt wel. Het is beter om het zo te leren dan letterlijk gevouwen te worden als een tuinstoel.
[n4v3wtt] (score 179, diepte 1) We kunnen wel eens wat meer shock gebruiken om mensen iets normaler te laten leven. Met 180 op een motor in een korte broek klinkt ook heel stoer, totdat je onderuit gaat. 

Ik heb al eens een motor onderuit zien gaan die misschien 30 reed op een normale weg in een bocht, er lag wat grind ofzo en hij gleed zo weg. Gelukkig had die persoon wel goede kleding aan, maar als dat gebeurd met 30 wil je niet weten wat er gebeurd met 180.
[n4v77iy] (score 155, diepte 1) Tijdens een code 95 cursus dag vertelde een brandweerman/EHBO instructeur dat hij ook meermaals aanwezig was bij gassies die helemaal naar achter zitten in hun auto, met de benen gestrekt om gas te geven/remmen/schakelen, en blijkbaar willen bovenbenen/heupgewrichten nog wel eens door de gluteus maximus naar buiten geduwd worden als de voorkant van de auto ingeduwd wordt en momentum de persoon naar voren schiet. Zo heeft tie, naar zeggen, eens een keer een knul uit de auto moeten halen, die met zijn heupen bij zijn knieën zat, en 2 botten uit zijn rug staken.
[n4vddit] (score 154, diepte 2) Ok… genoeg Reddit weer voor vandaag…
[n4v4yoz] (score 114, diepte 2) Dress for the slide, not for the ride.
[n4v2qg3] (score 107, diepte 1) Ja, bekijk het eens positief, teen nagels knippen gaat ook veel makkelijker als je je benen kan opvouwen!
[n4v4l60] (score 60, diepte 0) Ooit fotos gezien waarbij de scheenbenen van de knie los waren gekomen. 
Het laatste wat door die persoon zijn/haar hoofd schoot waren die scheenbenen.


Ook leuk, mensen die hun stuurairbag volplakken met glim en glitter meuk. Gratis claymore.
[n4v7hnz] (score 56, diepte 2) Zoiets was ook te zien op een van de foto's die ik mijn ex liet zien. Een meid waarbij haar linkerdijbeen bij haar rechterbil naar buiten kwam.

Lijkt me echt verschrikkelijk om zulke dingen in het echt mee te maken.
[n4v9fs3] (score 50, diepte 4) Dan was er geen reet meer aan.
[n4vha6o] (score 48, diepte 2) Mijn exschoonvader was brandweerman. Geweldig vent maar elke keer als die snacht terugkwam van een heftig ongeluk (en wij waren bij haar thuis en nog wakker) moest die boos vertellen over wat we absoluut nooit mochten doen in de auto.

Weet nog een keer dat ik er geen zin in had (want waren eigelijk bezig met iets anders) en onverschillig deed en toen liet die een foto zien waarbij het stuurwiel IN iemands romp zat. 

Tegenwoordig snap ik dat de beste man gewoon shit moest verwerken. Autos die snachts vreselijk verongelukken zijn vaak van jongen bestuurders die gewoon achterlijk doen. En als ouder is het natuurlijk gewoon eng om te bedenken dat jou kids ook een auto hebben en misschien wel voor een moment achterlijk kunnen zijn.
[n4v1cbo] (score 47, diepte 0) Niet doen! Ik doe het nooit, als de passagier dat doet zeg ik altijd direct 'niet doen!'.
[n4v5p1p] (score 41, diepte 2) Hij wordt geupvote omdat de rest van ons wel humor heeft in de vroege ochtend en begrijpen dat die een grap maakt
[n4vw4rv] (score 39, diepte 2) Onvrijwillige yoga?
[n4v5r26] (score 37, diepte 3) stel je de ravage voor als hij in z'n zwembroekje was onderuitgegaan
[n4v4t18] (score 27, diepte 2) Heb een oom die ooit onderuit ging met de motor: hij had een vol pak, met extra bescherming, daaronder een spijkerbroek en in zijn kontzak een portemonnee. Hij gleef over zijn achterste nadat hij moest uitwijken voor iemand: motorbroek weg, spijkerbroek weg èn de portemonnee volledig weggesleten, waarna uiteraard zijn achterste. Dit was met alle mogelijke bescherming.
[n4v4o57] (score 25, diepte 0) Mijn vrouw deed dit een maand geleden. Ik zag haar denken, aarzelen, trok haar benen op en legde ze op het dashboard. Iets meer denken. Benen weer naar beneden.

Is maar goed ook, want ik stond op het punt om nét hard genoeg te remmen zodat ze zo met haar kont naar het voetengedeelte zou glijden en een onvrijwillige dubbelgevouwen acrobaat zou zijn.
[n4vk783] (score 22, diepte 3) Die beste instructeur had behoorlijk heftige verhalen, zoiets als stuur in middenrif zat daar ook tussen.

Het is erg heftig als je dat als jong stel midden in de nacht ineens te horen krijgt, zeker als dat met een bepaalde toon komt en je al in een rebelse leeftijd zit, maar inderdaad, de beste meneer zat waarschijnlijk zelf ook hoog in de emotie en moest even druk kwijt.

Mijn neef is Ambulance Broeder, tijdelijke bij het Korps Commando Troepen geweest en een jaar of 10 binnen defensie gewerkt. Hij was van mening dat Ambulance Broeder zijn heftiger is dan de vorige twee banen die hij had.
[n4v16a3] (score 18, diepte 0) Sowieso goor man, of je moet een voetfetish hebben. Die dingen zitten niet voor niets het verst weg van je hoofd
[n4v27gw] (score 18, diepte 2 OP) Toen ik nog een kleine belly_bouncer was had ik ontiegelijke stinkvoeten, ondanks 2x per dag voeten wassen en schoenen/sokken wisselen.
[n4v1l6m] (score 18, diepte 1) Wat heeft het internet ons toch tot heerlijk empatische wezens gemaakt...
[n4v22vn] (score 18, diepte 3) Kun je alsjeblieft toCH gebruiken (ipv tog).
[n4v53af] (score 18, diepte 1) Ik zeg altijd dit tegen de bijrijder in zo’n geval:

Pak je telefoon eens. 
Zoek op Google naar ‘benen op Dashboard’.
Klik op ‘Afbeeldingen’

De benen gaan vanzelf weer van het dashboard.
[n4v2ecv] (score 17, diepte 1) Ik ben 1,95 en pas zelfs prima in een 108. Dus tenzij je echt een reus van ruim meer dan 2 meter bent, zal ik je adviseren om eens met je hand onder de stoel te voelen. Daar zit een hendel waarmee je de stoel naar achter kan schuiven
[n4v5feq] (score 17, diepte 2) "Met 180 op een motor in een korte broek klinkt ook heel stoer, totdat je onderuit gaat."

aka vleespotloodje
[n4v1kjd] (score 16, diepte 1) Ik denk dat dat meer zegt over hoe jij met je hygiene om gaat dan dat het daadwerkelijk goor is... Als ik soms ruik wat mensen uit hun voeten meuren als ze hun schoenen uit trekken... Damn... Maar een beetje hygiene doet een hoop en dan is er helemaal niks aan de hand.

Maar dan nog voeten van dashboard af. Voor je eigen veiligheid en omdat het gewoon asociaal is.
[n4v2h5l] (score 16, diepte 3) Heeft de Boska kaasschaaf je hiermee geholpen?
[n4v1zl8] (score 16, diepte 1) En maar meebetalen aan de achterlijk hoge zorgkosten omdat we niet om elkaar denken tot het te laat is.
[n4v66ux] (score 15, diepte 1) Het moet ook geen zwaar ongeval zijn dat een airbag af gaat. Het is echt een verschil tussen niets hebben en levenslang afzien.
[n4v5tud] (score 15, diepte 1) Ik heb 5 jaar ziekenvervoer gereden. Veel motorrijders naar het revalidatiecentrum gebracht, en dat waren dan nog degenen die de val hadden overleefd. Mij zul je nooit op zo'n ding zien.
[n4v35p4] (score 13, diepte 1) ja daarom doe ik nooit een gordel om, ik bots namelijk nooit.
[n4v3cri] (score 13, diepte 1) Het heet kruiscontrol als je je voeten op het dashboard hebt
[n4v4tg9] (score 12, diepte 0) Mijn ex deed dit en heb er toen ook al eens wat van gezegd. Nu rijd ik gewoon niet verder totdat ze hun voeten van het dashboard halen.
[n4v5pe6] (score 11, diepte 2) Ik heb zelf ook wel het idee dat sommige niet eens doorhebben wat de gevolgen zijn van hun acties. Er mag van mij zeker meer shock/gore komen. Dit is ook waarom het oude tv programma blik op de weg zo leuk vind. Ze trekken het in twijfel en doen tests (die ze ook tonen). Een agent daar zei ook: die 2 minuten tijdwinst ben je bij het volgende rode licht alweer kwijt. Ook hield de politie auto de andere auto gemakkelijk bij onder zich zelf in echt gevaar te brengen (geduld is een schone zaak)
[n4vbkb3] (score 11, diepte 1) Ik weet eigenlijk niet of dat pedagogisch onverantwoord is. Het klinkt alsof hij niet de intentie had om zo schokkend mogelijk te zijn, maar hij heeft ze heel erg duidelijk gemaakt hoe afgrijselijk die dingen kunnen aflopen. Lijkt me helder en een goede waarschuwing. Sommige dingen moet je nu eenmaal zo duidelijk gemaakt krijgen dat je het nooit meer doet.
[n4v72cs] (score 11, diepte 0) Sinds ik geen cruise control meer heb doe ik t nog zelden
[n4v39y8] (score 10, diepte 7) Niet alle mensen met dyslexie, maar jij wel
[n4v741f] (score 10, diepte 2) Yep. Ik had eens gelezen dat het zelfs bij botsingen op relatief lage snelheid (zoals 30) al voor enorm letsel kan zorgen omdat je onder de gordel door kunt glijden.
[n4vphnd] (score 10, diepte 4) Dat gewoon ik zeker. Zus van mijn Oma zat op de ambulance en het verhaal gaat (geen idee in hoe verre het ook waar is) dat die ooit een los hoofd heeft moeten pakken na een ongeluk met een motor en een trein? (volgens mij was het een trein, maar het verhaal lijkt elke keer sterker te worden als ik het weer hoor). 

Ik weet wel 1 ding zeker, ik hoef niet als eerste bij een verkeersongeluk te zijn. Al hoe wel ik gewoon maffe dingen online heb gezien als kind, lijkt me het niet nodig om die dingen in het echt te zien.
[n4vhock] (score 10, diepte 1) Voor mensen die ook op zoek zijn naar afschrikmateriaal kan ik deze post aanbevelen: [https://www.reddit.com/r/SnapshotHistory/comments/1iyqskb/in\_2007\_grainne\_kealy\_shattered\_her\_face\_when\_an/](https://www.reddit.com/r/SnapshotHistory/comments/1iyqskb/in_2007_grainne_kealy_shattered_her_face_when_an/)

Vrouw die haar complete schedel vernaggeld heeft door met haar voeten op het dashboard te zitten. Ze heeft twee jaar zonder voorhoofd geleefd. Link is SFW - geen gore, wel een beetje creepy.
[n4v4gvk] (score 10, diepte 3) Maar hoeveel makkelijk wordt het als die knie ook de ander kant kan vouwen?
[n4v7i29] (score 10, diepte 3) Breng 12 steden 13 ongelukken terug
[n4v2trl] (score 9, diepte 2) Tuurlijk is hygiene belangrijk, maar als je een hele dag gewandeld/fysiek bezig geweest ben ruiken jouw voeten ook niet lekker als je daarna direct in de auto stapt hoor.
[n4wvw78] (score 9, diepte 7) Naar mijn mening, uiteraard zolang als Oekraïne wilt door blijven vechten, is het niet de bedoeling dat wij (NAVO) zonder hulp te bieden een vrij en soevereine land laten overnemen door een agressor dat alleen maar uit is op macht, land, grondstoffen en een terugkeer naar de koude oorlog.

Liever nu materiaal en geld kwijtraken aan een conflict buiten de NAVO/EU grenzen, dan dat we een signaal afgeven dat Putler kan doen wat tie wilt en we dadelijk Materiaal, Materieel, geld en manschappen kwijtraken.
[n4v6781] (score 9, diepte 1) Kunnen allemaal heel spannend doen over pedagogisch verantwoord, maar als je moet kiezen tussen even iets vervelends horen of een levensgevaarlijke situatie dan weten we het allemaal wel.
[n4v3f9p] (score 8, diepte 2) Een echte kapitein gaat met zijn schip ten onder.
[n4v78ac] (score 8, diepte 3) r/meatcrayon al staat daat heel wat meer
[n4v9sp3] (score 8, diepte 0) Ik weiger de auto voort te bewegen met voeten op het dashboard.  
Geen zin in een onderbeen-claymore of te moeten zien hoe iemand alles breekt omdat ze dubbelvouwen onder het dashboard.   
Plus die houding blokkeert 99% van de gevallen ook nog eens het zicht naar de zijspiegel.
[n4v5juj] (score 7, diepte 4 OP) Zeker, plakje eelt per dag eraf met een stukje tenenkaas.
[n4vf7wq] (score 7, diepte 1) M’n ex deed dat ook op vakantie, gelukkig niet toen ik de auto Total loss reed, omdat ik links recht link keek, en met 70km per uur werd aangereden door Engels busje. Nog steeds blij dat we daar heel samen heel huids uitstapten!
[n4vmcg4] (score 7, diepte 2) Je bent nog steeds een beetje in de war, merk ik.
[n4v2wm7] (score 7, diepte 0) Ik rij handgeschakeld, dus sowieso lastig om te doen
[n4v3yo8] (score 7, diepte 0) ik noem het verassings yoga
[n4v4a2c] (score 6, diepte 4) Als ik een uurtje sport ook niet, want sportschoenen ademen. Werkschoenen zijn vaak dik, lomp, en ademen voor geen meter. En 9 uur is zeg maar best wel lang
[n4v2lvv] (score 6, diepte 5) Hoho, het was maar een vriendelijke vraag, niet meteen zo verhit reageren.


Was ook meer een ding om aan te geven dat als je anderen dom noemt, je schrijfwijze dan in ieder geval een beetje intelligent moet overkomen, versterkt je eigen punt.
[n4v3bm2] (score 6, diepte 3) je kunt vast nog een meer unhinged reactie verzinnen, kom maar kom maar komaaaaar.
[n4v2cco] (score 6, diepte 1 OP) Nee
[n4xeeap] (score 6, diepte 2) Zelfde geld voor een Haarklem in de auto
[n4v7ozt] (score 6, diepte 3 OP) Ja die airbag blijft met dezelfde snelheid ontploffen.
[n4v8ut1] (score 6, diepte 2) Als je nog iets verder onderuit gezakt zit. Kun je jezelf pijpen na een ongeluk.
[n4v6i9g] (score 6, diepte 3) In motorkleding heb je ook verschillende klasses van bescherming. A, AA en AAA. Hoelang je er mee over het asfalt kan glijden hangt daar ook flink van af
[n4v5vg5] (score 6, diepte 1 OP) Heel goed dit, shock & awe!
[n4v6tqj] (score 6, diepte 3 OP) Waarschijnlijk keek je haar al aan met _de blik_
[n4xhfof] (score 6, diepte 1) Neem jij nogsteeds al je exen mee in de auto?
[n4v9212] (score 6, diepte 1 OP) Lijkt mij wel, je gordel zit immers niet goed, en je kan jezelf niet schrap zetten.
[n4v4b5h] (score 5, diepte 4) Elk lichaam is anders 🤷🏼‍♀️
[n4vpyya] (score 5, diepte 5) Als iemand die geregeld drone videos kijkt op r/UkraineWar, trek ik de lijn tussen ver van mijn bed en recht naast me. Ik verheerlijk de filmpjes niet. Het is altijd vreselijk om te zien dat zoveel mensen moeten sterven voor de fantasie van een kleine dictator in Rusland.
[n4v5prq] (score 5, diepte 2) Dit is duidelijk sarcasme.
[n4v7efy] (score 5, diepte 4) Ja maar in je zwembroekje op de motor ben je natuurlijk wel veel stoerder!
[n4v77je] (score 5, diepte 2) Het wordt ook echt tijd dat we niet zo voorzichtig zijn met de zogenaamd tere (kinder-) zieltjes in het onderwijs en de opvoeding.

De gemiddelde 12/13 jarige heeft vandaag internettoegang en heeft vaak veel meer gezien dan de gemiddelde ouder/leraar onder ogen wil zien....

Of willen we nog meer snowflakes creëren dan er nu al rondlopen?
[n4v4zjh] (score 5, diepte 1) Ja.
Die klapt met zoveel geweld uit het dashbord dat in het ergste geval je benen afgerukt worden.
Maar meestal blijft het bij een beetje verkeerd omgevouwen.
[n4v9unc] (score 5, diepte 4) Ze was in haar eigen hoofd al de math aan het doen, ik hoefde niet eens ##DeBlik## te geven
[n4v7d3p] (score 5, diepte 1 OP) Jij wel.
[n51xmme] (score 4, diepte 3) Ik heb zoveel respect voor alle mensen die het werk doen waarbij ze dit soort gevallen tegen kunnen komen. Ik zou het niet kunnen.
[n4x2rs5] (score 4, diepte 6) Ik heb met je te doen
[n4vdszt] (score 4, diepte 1) >Uiteindelijk heb ik haar een paar gore foto's laten zien van mensen die dubbelgevouwen waren omdat ze hun voeten op het dashboard hadden en toen was ze wel genezen.

Goed dat je die bij de hand had. Gore fotos komen altijd van pas.
[n4v7vt3] (score 4, diepte 4) In dit geval wel erg duidelijk aan het eerste zinnetje te zien.
[n4vntq3] (score 4, diepte 5) Motorkleding is de laatste 10 jaar er flink op vooruit gegaan. Als deze schuiver 10+ jaar geleden was dan is het niet heel gek. Maak je tegenwoordig een schuiver in de juiste kleding dan kom je er zonder verwondingen van af, zelfs bij meer als 200 km/u. Kijk maar naar MotoGP coureurs die gelijk opstaan.
(256 reacties met lagere score weggelaten)

=== THREAD 14igt3b ===
SUBREDDIT: r/nederlands
DATUM: 2023-06-25  SCORE: 71  REACTIES: 221
TITEL: Blootvoets winkelen?
POST (source_id=post):
Hebben jullie wel eens iemand met blote voeten in een winkel gezien? Hebben jullie dat zelf wel eens gedaan of zou je het doen? Mag dat eigenlijk of is het iets wat wel mag maar eigenlijk ook taboe is?

Ik heb hier zelf absoluut geen behoefte aan. Maar ik vraag het omdat sommige mensen het kennlijk fijn vinden om altijd op blote voeten te leven. Alleen in Nederland heb ik nog nooit iemand dit zien doen. Ben dus nieuwsgierig naar jullie gedachten hierover.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jpg4pha] (score 204, diepte 0) Ik werk bij AH, er zijn een paar mensen die blootvoets winkelen. Het is niet verboden, het is op zijn minst onverstandig. Ondanks dat de vloer elke dag geveegd en gedweild wordt, is er geen garantie dat er niks ligt. Wat kan variëren van een sperzieboon tot een verdwaalde glassplinter.
[jpg1qjc] (score 173, diepte 0) Het schoenenkartel wil dat we altijd schoenen dragen. Maar vroeger droeg niemand schoenen, maar er waren ook nog geen winkels.
[jpg7uou] (score 78, diepte 2) Werk? Werk is diefstal door de patriarchie. Ik leef volgens  communistische homeopathische principles.
[jpgb578] (score 63, diepte 4) Daarom ook homeopatisch communisme. Mijn bijdrage aan het collectief is 1:40000 verdund
[jpg2x97] (score 48, diepte 1) Ga jij ook met paard en wagen naar het werk?
[jpg1l4p] (score 39, diepte 0) Ik heb ooit wel eens blootsvoetsmensen gezien. Ik vond het geen fraai gezicht.
[jpg4f7l] (score 36, diepte 0) Zolang je de boel niet vuil maakt zou ik niet verwachten dat het verboden zou zijn. Maar slim is het niet. Wie weet laat per ongeluk iemand een glazen pot appelmoes vallen en zijn de microstukjes glas niet goed opgeruimd. Of er ligt iets op de vloer wat niet zo goed voor je is bij het HG-schap. Of men is net de vloer aan het reinigen met zo’n machine, dat spul is niet heel vriendelijk voor je. 

En waarom ook?
[jpgjvll] (score 24, diepte 1) Ja, ik zou er geen problemen mee hebben, maar ik ben bang dat ik gewoon ergens op zal stappen.
[jpg36bm] (score 19, diepte 0) Er komt hier wel elke dag een hardlopende man langs op blote voeten. Ik zal eens vragen of hij ook zo naar de winkel gaat.
[jpg39s7] (score 18, diepte 0) De lokale supermarkt hanteert huisregels waarin je schoeisel, broek tot iig halverwege het bovenbeen of rok van eenzelfde lengte en een een shirt moet dragen. Dit omdat anders teveel mensen in bikini of Speedo proberen te winkelen.
[jpgdzw2] (score 17, diepte 4) Huh? Jij ontkent communisme? Nog nooit gehoord dat iemand dat zei...  Maar goed, doe je ding en geloof je eigen ding.
[jpg1xfp] (score 17, diepte 0) Zie het wel eens maar vind het raar en vies. En gevaarlijk, wie weet wat voor vieze scherven er op straat liggen.
[jpg3rnk] (score 17, diepte 1) Laat me raden, de appie in scheveningen
[jpg59m0] (score 16, diepte 2) Zou daar ongetwijfeld ook zo zijn, waddeneiland hier.
[jpgkklw] (score 16, diepte 2) Ja dat boeit dus niet echt veel als je altijd op blote voeten loopt

Een stukje glas voel je echt niet in je eelt
[jpgodl8] (score 16, diepte 3) Tenzij het echt een vlijmscherpe scherf is.. Maar dan is menig schoen ook niet meer veilig genoeg lol.

Verder eens, Beetje eelt doet echt wonderen.
[jpg684g] (score 16, diepte 0) Loop graag op blote voeten maar zou niet snel winkel of ander gebouw inlopen zonder. Als ik langere stukken ga lopen neem ik altijd wel even iets van slippers/sandalen mee voor als ik ergens naar binnen moet.
[jpgdd81] (score 14, diepte 5) Mwah hoezo mag ik dat niet vragen dan? Omdat je er geen goed antwoord op hebt? Lijkt me niet echt een reden om iets niet te vragen, eerder een reden om je positie te heroverwegen.

Vind het prima als je het raar vindt, dat is gewoon je mening en waarschijnlijk ook objectief waar omdat het ongebruikelijk is. Maar specifiek vies, waarom dan?
[jpg2jsc] (score 13, diepte 0) Het boeit mij niet als anderen het doen, maar zelf zou ik het nooit doen. Te bang om in glas te stappen
[jpgg4gn] (score 12, diepte 5) Ik denk dat deze commenter bedoeld dat het communisme nooit is uitgevoerd op de manier hoe het bedoeld was. Er komt altijd een of andere dictator aan de macht bij communisme (of het wordt in gang gezet door een), die misbruik maakt van het systeem en zichzelf en een klein groepje mensen machtiger en rijker maakt en de arbeidersklasse uitbuit om het systeem te dienen. Communisme in de meest pure vorm houdt in dat alle middelen en macht in handen is van het volk en dat deze eerlijk worden gedeeld zodat iedereen een fatsoenlijk bestaan heeft, maar dat gebeurt nooit in communistische landen en het is bijna onmogelijk om te bereiken omdat er altijd overal wel iemand komt opdagen die misbruik maakt van alles binnen handbereik om zichzelf te verrijken. Echte communisme is een utopie.
[jpg4dn4] (score 12, diepte 2) Scherven, scherpe steentjes, allerhande kleine scherpe vieze dingetjes die in je zool prikken.
[jpggm75] (score 12, diepte 1) Precies. Waarom zou het verboden zijn? Schoenen zijn er voor je eigen bescherming. Als jij met je blote voeten in glas of andere troep wil stappen prima. Buitenhuis draag ik altijd schoenen. Dat is het veiligst en schoonst (voor jezelf). Thuis loop ik heerlijk op blote voeten want wij houden de vloer gewoon schoon. Bij een ander op schoenen als zij dat zelf doen of anders sokken als zij de vloer ook schoon houden.
[jpg62zq] (score 12, diepte 0) Waarom zou het meer vies zijn? Schoenen zijn net zo vies en die worden binnenshuis gedragen.... of ik het zelf zou doen? Zeker niet, als vakkenvuller vaak genoeg hak potjes laten vallen en die splinters liggen overal

Edit : schoenen zijn viezer, hoevaak zit er hondenpoep onder en tenzij de blootvoeter de horlepiep danst op een hondenuitlaat veld vertrouw ik een blote voet meer
[jpgxj6l] (score 9, diepte 5) Wauw, zie meneer de 0.0025 percenter hier
[jph9z6r] (score 9, diepte 1) > En waarom ook?

Omdat op blote voeten lopen beter voor je voeten is. Daar zijn onze voeten voor geëvolueerd. Je krijgt er sterke en stabiele voeten van met een stevige laag eelt. 

Niet dat ik het doe overigens, want op de vraag “Waarom niet?” kan ik een hele waslijst aan antwoorden geven. Maar ik snap wel de reden dat sommige mensen het dus wel doen.

Als het even kan loop ik altijd op blote voeten. Thuis, op het strand, in het gras, door het water. Ik vind dat echt heerlijk.
[jph3qii] (score 9, diepte 5) Je kan het proberen, verwacht wel dat je keihard wordt uitgelachen in de rechtzaak 😂

Een winkel kan nooit 100% garantie geven dat een vloer compleet vrij is van wat dan ook. Het is dan ook gewoon eigen risico als je geen schoenen aan doet buiten
[jpgvcai] (score 9, diepte 1) Wat dacht je van een volgeladen rolcontainer over je tenen heen? Kans is klein, maar niet nul...
[jpg9dgo] (score 9, diepte 0) Toen ik nog op het strand werkte deed ik alles op blote voeten. In de pauzes ging ik naar de winkel op blote voeten, ik zat in mijn stamkroeg op blote voeten (dat was wel vies eigenlijk).

Net op vakantie geweest in Indonesië en de gidsen liepen op blote voeten door de jungle en ze waren toch een stuk behendiger dan ik.

Ik vind het niet raar of vies, maar mensen zeiden er wel eens wat van. Vooral brabo toeristen die hun vrouw aantikten en dan zeiden "hebbe da jong geen geld voor schoenen?" of zoiets, waarna vrouwlief met ogen draaide en verder ging met haar leven.
[jpgcsjr] (score 8, diepte 1) Wel een goede manier om diefstal te voorkomen
[jpg4umw] (score 8, diepte 1) Hardlopen op blote voeten is echt een ding, zal het  zelf nooit doen maar zitten wel echt voordelen aan.

https://voetenbeweging.nl/op-blote-voeten-lopen-goed-idee/
[jpgavqd] (score 8, diepte 2) Ik heb een japanse vrouw... ik heb woonkamer, wc, tuin en slaapkamer slippers. Maar ja, ik ben opgegroeid met schoenen zijn overal oke. En in 'mijn bubbel' ben ik de enigste waar schoenen binnen een no-go is
[jpgl2c3] (score 8, diepte 0) Ik loop heel graag op blote voeten. Thuis, in de tuin, soms ook op straat. Maar als ik ergens heen ga, dan heb ik schoeisel.
[jpgpjfs] (score 7, diepte 4) Ik ben niet je vriend, makker.
[jph0jyn] (score 7, diepte 2) De kans op een vol winkel wagentje van een bejaarde is toch vrij groot ook niet lekker
[jpgud9n] (score 6, diepte 5) Ik ben niet je makker, gabber
[jpgusqx] (score 6, diepte 1) Dit is een Big Shoe complot
[jpg9qgs] (score 6, diepte 3) Nee, liever niet.
[jpgvd9v] (score 5, diepte 6) Ik ben niet je makker, kameraad
[jpghf1s] (score 5, diepte 7) Ja maar dat gaat weer over wanneer je het zelf zou doen. Waarom vind je het vies als een ander het doet?
[jpgzds1] (score 5, diepte 1) Ik liep vroeger zo'n beetje de hele zomer op blote voeten. Ook gewoon door de stad enzo. Je let wat beter op de grond. Maar je krijgt ook een hele bak eelt. Dus na een tijdje is een klein stukje glas ofzo niet zo'n probleem. Ook dingen als een grindpad doen geen pijn meer.
[jpgktjk] (score 5, diepte 1) Triest
[jpgaxls] (score 5, diepte 1) Ach gut, kan je tere zieltje het anders niet aan.
[jpglcf7] (score 4, diepte 2) Dat is geen winkel of straat maat.
[jpg9yoo] (score 4, diepte 4) Gebaseerd
[jph9cnn] (score 4, diepte 6) Ja, het theoretische raamwerk achter het communisme kan ik me heel goed in vinden. Maar of het in het echt op een realistische manier zou kunnen werken? Ik denk het niet. En laten we het alsjeblieft niet nog een keer proberen.
[jpgr4tt] (score 4, diepte 2) Ligt er aan.. hoe lang geleden.
[jphuexd] (score 4, diepte 2) Jamaar scapino bestaat ook echt al super lang hoor
[jpgamr9] (score 4, diepte 2) Waarom?
[jpgc3qu] (score 4, diepte 3) Oh je vindt het vies om het zelf te doen, niet vies dat anderen het doen?
[jpg3p1x] (score 4, diepte 0) Ik doe dit alleen op vliegvelden en in het vliegtuig
[jpgd3ik] (score 4, diepte 1) Nu is asfalt een vrij nieuwe uitvinding maar harde ondergrond zeker niet. Mensen zijn de beste duurlopers van het dierenrijk (enigzins gelijk met de wolf, maar die legt het echt af in iets warmere omstandigheden) en al die miljoenen jaren hadden we geen schoeisel. Opeens sinds de jaren ´´70 moeten we dempende schoenen dragen?

Juist schoenen zorgen voor problemen met lopen, schoenen zijn regelmatig te smal waardoor tenen niet goed spreiden. En juist demping in de zool zorgt ervoor dat mensen hardere passen maken en meer op de hiel gaan lopen.
[jph2jh0] (score 4, diepte 5) Only in 'murica.

Haalde hier in mijn stad een keer mijn teen open tijdens een dagje zwemmen. Aardige jaap.

Kreeg niet eens mn ticket terug lol. 

Maar dat zwembad is ondertussen ook al gesloten dus karma heeft haar weg toch nog gevonden zegmaar. En mijn grote teen is prima 👍
[jph5sy9] (score 4, diepte 1) Ik heb een tijd terug een infectie opgelopen aan m'n voet die me mijn grote teen heeft gekost omdat ik met blote voeten op een relatief schone vloer liep. Ik ga nooit meer zonder iets aan mn voeten aan de wandel.
[jpgcnbr] (score 4, diepte 1) Drugs
[jpgep5y] (score 3, diepte 1) Denk jij echt dat ze vroeger niks bedekkends onder de voetzolen hadden bedacht?
[jphhr4v] (score 3, diepte 3) Opzich waar, maar dan ga je wel voorbij aan het feit dat de omgeving die wij (grotendeels voor onszelf) gecreëerd hebben daar niet op is aangepast. Die is in elkaar gezet met het idee dat iedereen toch wel schoenen draagt. Zie bijvoorbeeld paarden, die hebben extra bescherming nodig voor al dat beton en de stenen die ze tegenkomen op hun pad.

Nog een addendum, sommige paarden (en misschien onderhand ook mensen) zijn niet geselecteerd voor sterke hoeven en kunnen heel slecht bestaan zonder hoefijzers. Het zou dus kunnen dat we na zo'n grofweg 9000 jaar met schoenen niet meer gemakkelijk zonder kunnen.

Evolutie is niet een proces met een eindpunt, het is altijd in meer of mindere mate gaande. Ook vandaag de dag nog.
[jpgbkmy] (score 3, diepte 1) Wat is er vies aan?
[jpgwrq4] (score 3, diepte 9) Oke, maar hoe beïnvloedt het jou als iemand anders kiest om daar op te lopen met z'n blote voeten?
[jpgy067] (score 3, diepte 10) Ik trek me schoenen uit op de deurmat, precies om dit te voorkomen. Zoek het gewoon niet om continu schoon te moeten maken.
[jpgrvke] (score 3, diepte 8) Precies
[jphofy1] (score 3, diepte 1) Altijd weer die sperziebonen..
[jpg7car] (score 3, diepte 1) Ik draag zeker geen schoenen binnenhuis. Jij wel dus? Ja, dan snap ik wel waarom je denkt dat het net zo vies is.
[jpgebuq] (score 3, diepte 1) ... Eh watte?
[jpg7ij8] (score 3, diepte 0) Ik zie mensen welleens op blote voeten door de straten gaan enzo en vind het ronduit smerig om te zien eigenlijk.
[jpg8ez8] (score 3, diepte 0) Ja heb ik wel eens gezien. Ik doe het ook niet, vind het niet schoon want heb zelf enorme zweetvoeten en laat overal stempels achter... Nu zal eenieder in meer of mindere mate zweetvoeten hebben dus ik vind vies. Eigen huis, camping, gras? Prima. Maar in een winkel niet zo cool.
[jpgdjyg] (score 3, diepte 1 OP) Ja "ongeschikt" is lekker vaag. In de praktijk komt het er volgens mij op neer dat je naakt mag zijn zolang niemand je ziet die dat niet wil.
[jpgcq7k] (score 3, diepte 0) Ik ben vanochtend nog op mijn blote voeten naar de bakker gelopen . Kijkt z'n vrouw je super zuur aan.  
Super chill en als je er een probleem mee hebt wat ga je er aan doen 😁.
[jphp342] (score 3, diepte 1) Je zuur aankijken.
[jpgdv3d] (score 3, diepte 0 OP) Mijn eigen mening toch ook maar even. Ik heb er geen bezwaar tegen als mensen dit doen, maar begrijpen doe ik het niet. Het lijkt me zowel erg oncomfortabel als vies. Ik heb gewoon echt geen zin om in iets smerigs of pijnlijks te stappen en een dikke laag eelt op mijn voetzolen kweken vind ik ook niet echt apetijtelijk. 

Dat je het in de natuur doet, dat je het fijn vind de aarde of het gras onder je voeten te voelen, dát begrijp ik dan weer wel!
[jpgjkh2] (score 3, diepte 0) Blootvoets in een natuurlijke omgeving kan ik nog snappen.  Maar in de stad en winkels ligt teveel rare en gevaarlijke zooi op de  grond. In een winkel vind ik het ook niet echt fris uitziem maargoed, je hebt ook binnen no tine een karrentje op je teen.
[jpgo964] (score 3, diepte 1) Ik heb precies hetzelfde!
[jpgnvdu] (score 3, diepte 0) Ik loop relatief veel blootvoets, en vind het niet vies ofzo. Veel mensen lopen ook met hun schoenen door het huis heen, waarom is het dan raar dat ik met mijn blote voeten van buiten naar binnen loop? Mijn voeten was ik ten minste nog, mijn schoenen niet.

Echter in openbare plekken zorg ik er wel altijd voor dat ik iets van schoeisel aan doe. Naast het feit dat (heet) asfalt totaal niet fijn loopt, lijkt het me ook nog eens gevaarlijk (denk bv aan glasscherven).
[jphbjn0] (score 2, diepte 7) Ik ben niet je kameraad, kornuit.
[jpkuvpo] (score 2, diepte 6) Ik weet niet of je het interessant vind, maar dit is een filmpje over hoe het komt dat bijna alle dictatoren als slecht en egoïstisch worden gezien (en zijn) 

[https://www.youtube.com/watch?v=rStL7niR7gs](https://www.youtube.com/watch?v=rStL7niR7gs)
[jph9iqi] (score 2, diepte 2) Dat ligt er helemaal aan waar en wanneer je kijkt. Onze lichamen zijn geëvolueerd om prima op onze blote voeten te kunnen lopen, net zoals elk ander dier.
[jphfw3i] (score 2, diepte 2) Schoenenreus
[jpg4aov] (score 2, diepte 1) Ik vind het ook raar en vies. Maar scherven kom je gelukkig weinig tegen. Let er maar eens op.
[jpg7e7n] (score 2, diepte 3) Scherven en andere prikdingen. Ja oké, daar kan ik het wel mee eens zijn.
[jpge4gf] (score 2, diepte 3) De meeste dingen merk je niet zo, ik loop om het huis szomers altijs met blote voeten, en na een paar weken merkt je echt de steentjes en stukjes hout niet meer. Zelfs kleine glassplinters blijfen in de verdikte huid steken. (Zoals ik nog al eens merk als.ik in de buurt van de ondergrondse containers geweest ben.)
[jph0n2h] (score 2, diepte 11) Nja je nam de discussie over van iemand die wil dat anderen schoenen (verplicht) dragen. Je kan het best onverstandig van de ander vinden, maar als het jou verder niet beïnvloedt zie ik niet echt een goede reden om te vinden dat een ander (verplicht) schoenen aan moet. Dat is waar het mij in de basis om gaat.

Overigens vind ik het zelf wel meevallen met hoe vies het daadwerkelijk is, ook als je het zelf doet. Het vuil zit allemaal onder je voeten, zie het probleem niet zo zolang je je voeten niet in je mond stopt of er met je handen aan gaat zitten. En de (extreem onwaarschijnlijke) mogelijkheid op tetanus heb je in zo veel situaties. Maar goed dat is verder jouw mening en dat kan je vinden. Het gaat mij om het opleggen van een ander wat die wel/niet mag qua schoeisel.
(153 reacties met lagere score weggelaten)

=== THREAD 12l2iqt ===
SUBREDDIT: r/nederlands
DATUM: 2023-04-13  SCORE: 79  REACTIES: 173
TITEL: voeten op stoel in trein
POST (source_id=post):
Ik vind het zoooo aso en stoor me er mateloos aan. Toch ben ik net niet flink genoeg om er wat van te zeggen. Dan denk ik,  waarom druk maken om kleine dingen,  waarom ruzie riskeren om zoiets onbenulligs. En toch maak ik me er erg boos over en laat het me niet los. Zeker niet als ik er een half uur naar moet kijken. Het zijn vaak  jonge mensen die dit doen.  

Moet ik me gewoon niet zo aanstellen? Hoe gaan anderen hier mee om? Zegt iemand er wat van? Hoe gaat dat?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jg5j05f] (score 117, diepte 2) Aub niet de schoenen uit…😅
[jg7228q] (score 88, diepte 0) als dit je grootste probleem is met het ov dan ben je overduidelijk nog nooit in half opgeruimde en dus onopvallende kots gaan zitten op een vrijdagochtend in een mokerdrukke trein
[jg7d2kn] (score 65, diepte 2) Het was een vroege vrijdagochtend. De sprinter naar utrecht stond vol. overal waar ik keek waren mensen. 

Plots heb ik een leeg klapstoeltje bij de deur in mijn vizier. Ik stel me al voor dat ik daar zometeen neer kan ploffen en mijn zware tas op de grond kan laten zakken. 

Ik haast naar de stoel. In mijn achterhoofd vraag ik me af, "waarom zit hier nog niemand als het zo druk is?". In mijn haast en moeheid laat ik mijn zorgen achterwege en ga zitten. 

De tas staat op de grond, ik zit achterover gezakt. Heerlijk. En dan ruik ik het. De onmiskenbare geur van kots. Ik kijk om mij heen of ik iemand kan spotten die er ziekjes uit zit, voorovergebogen zit of een bijzonder vieze jas aan heeft, maar zie niets. 

Dan valt mijn oog op het glazen schot naast de klapstoel. Ik zie vage bruine vegen, een hoop. De schrik laat mijn hart sneller kloppen. Ik kijk op de grond, en ja hoor, rond de paal van het schot zitten dezelfde bruine vlekken, en druppels. Ik kon er niet meer omheen. Iemand had hier zitten kotsen, en het tevergeefs proberen op te ruimen. 

Die jas, tas en kleding zijn toen ik thuiskwam direct de was in gegaan, maar helaas moest ik eerst nog een les volgen. 

Ja dat was een kutdag. 

&#x200B;

(de stoel zelf was schoon, dus ik dacht dat er niets aan de hand was. Ik ben een beetje viezigheid wel gewend in de trein, modder en dergelijke, ik had nooit verwacht at er een kotsgeur aan vast zat) 

Zijn dit details genoeg?
[jg73c5t] (score 60, diepte 0) Kennis van me zag ooit een stel mannen fietsen in de gracht gooien. die zei er wat van, en die hebben we in zijn trouwpak begraven, ipv zijn trouwerij een paar weken later te vieren. Die heette Meindert, hebben we nog stille tocht voor gehouden, the works. Moraal van mijn verhaal? Ik ga zulke confrontaties dus niet aan, dat bewaar ik wel voor als een dierbare echt in nood is, dat risico ga ik niet lopen voor iets fysieks als treinbanken.
[jg56znh] (score 30, diepte 0) Lang geleden toen ik 13 was zei de conducteur dat het prima was zolang ik maar een krant onder mijn voeten deed. Maar ik heb geen idee of er überhaupt nog gratis kranten zijn?
[jg7ktfk] (score 26, diepte 3) Iemand vraagt om details en er komt een prachtig geschreven verhaal. Bedankt voor deze leuke anekdote!
[jg55dql] (score 24, diepte 1) ja mijn ervaring is ook dat de mensen die aso genoeg zijn voor voeten op stoelen, bellen op speaker of praten in de stiltecoupé ook de mensen zijn die geen kritiek kunnen hebben en iets te snel gaan schelden en slaan...
[jg5pgah] (score 24, diepte 1) Ik doe indd altijd mn jas of tas eronder, dan is t mn eigen probleem, vinden ze prima.
[jg7a07j] (score 23, diepte 0) Doet u dit thuis ook? Nee, ik heb thuis geen trein.
[jg724hx] (score 21, diepte 2) Jij moet nooit wetenschapper worden.
[jg71bmg] (score 19, diepte 1) En waarom zou mijn kleding vies moeten worden omdat iemand zo graag zijn poten op een zitting legt?
Ik doe niet moeilijk. Zij maken het moeilijk voor een ander en die mag er niets van vinden. Voor mij de omgekeerde wereld. Maar ik zou er niets van zeggen want mensen kunnen weinig hebben als je ze aanspreekt op goed fatsoen.
[jg76zxd] (score 17, diepte 0) Tokkies gonna tok
[jg54zd4] (score 15, diepte 0) Mensen die dit doen, zouden niet met de trein mogen rijden.

Ik zeg er niets van, voor je het weet heb je een vechtpartij of trekt er iemand een mes of zo...
[jg76n9g] (score 14, diepte 0) Alles in de trein is kut omdat 90% van dit land denkt alleen op de wereld te zijn, en dus ook in de trein
[jg7hry4] (score 11, diepte 7 OP) Juist wel. Daar leer je namelijk volzinnen, interpunctie en begrijpend nederlands. Die kennis maakt het vervolgens moeilijker om dat soort woordkots te ontcijferen.
[jg7et8x] (score 10, diepte 5) Ik moest dit oprecht meerdere keren lezen voordat ik het begreep.
[jg5ngqk] (score 10, diepte 1) Blijkbaar dus niet zo zen voor u.
[jg7cybw] (score 9, diepte 3 OP) Oke stoere boy bedankt voor je bijdrage
[jg7ahg7] (score 9, diepte 1) Vertel… details graag.
[jg7llbw] (score 9, diepte 4) graag gedaan 😎😎
[jg76d8n] (score 9, diepte 1) Tjoelker… dacht laatst nog dat toentertijd zulk nieuws ‘wereldnieuws’ was…

Deze dagen schering en inslag
[jg7aovl] (score 9, diepte 2) We hebben dat leermoment inderdaad nou niet echt met beide handen aangegrepen als maatschappij.
[jg7hxfd] (score 9, diepte 4) Dat zal je misschien zo voelen, maar dat is niet juist. https://eenvandaag.avrotros.nl/item/hoort-nederland-bij-de-strengst-straffende-landen-van-europa-het-idee-dat-we-heel-erg-soft-zijn-is/
[jg7fdoj] (score 8, diepte 0) Persoonlijk vindt ik het erger als mensen luidruchtig zitten te bellen in een stilte coupé. Zit op dit moment naast een eikel die zichzelf heeeeeel belangerijk vindt.
[jgbqi8b] (score 7, diepte 8) Wel dus. Je hebt letterlijk geen idee ervan wat de details zijn. Misschien deed die 'aanrander' het wel zojuist bij iemand die zijn dochter had verkracht. Misschien bestond het 'aanranden' uit het likken van een oor.

Maak het zelf vaak genoeg mee. Iemand die terechtstaat voor poging doodslag. In de krant staat dan: 'man krijgt 3 jaar voor het meermalen steken van het slachtoffer. Het slachtoffer is ternauwernood aan de dood ontsnapt'. Maar de krant vergeet even te vertellen dat dit 'slachtoffer' een notoire afperser is en een dag eerder met een pistool in de woning stond van de verdachte.

Overigens is allang aangetoond dat een taakstraf er vele malen vaker voor zorgt dat iemand het in de toekomst niet weer doet dan een gevangenisstraf. Wat vindt je belangrijker, dat de wereld daadwerkelijk beter wordt en leed wordt geminimaliseerd of dat jij er een harde plasser van krijgt dat iemand 20 jaar wordt weggestopt voor iets kleins?

We straffen al 25 jaar almaar harder, en de criminaliteit wordt in deze periode ook almaar harder. Gek he?
[jg5yxi1] (score 6, diepte 0) Ik erger me aan zo veel in de trein. Laatst zat ik nog in een redelijk drukke trein op zo'n vierzitter met 3 anderen. En na 1 minuut begin ik een soort kots/rook geur te ruiken alsof iemand al een jaar zn jas onderrookt en nooit doucht. En ik rook zelf ook, maar ik zorg wel altijd voor schone kleren en alles.
[jg72jkj] (score 6, diepte 1) Nee, want regulier vuil van straat is zo veel schoner.
[jg7ix9l] (score 6, diepte 1) Naja, een grotere irritatie maakt een kleinere irritatie niet minder erg. Ik vind overvolle treinen vervelender, maar ik kan me net zo goed storen aan voeten op de stoel. Verschillende situaties op verschillende momenten, niet echt te vergelijken.
[jg7jut6] (score 6, diepte 2) snap ik, heb je gelijk in. Ik heb zelf echt geen probleem met schoenen op de bank (mits de trein rustig is). Je raakt in het openbaar zo veel gore dingen aan, die schijn van schone stoelen heb ik al lang achter me gelaten
[jg7isan] (score 6, diepte 5) Als jurist is dit bij mij zo'n mateloze irritatie. Mensen die schreeuwen om strenger straffen terwijl we al in een (te) streng straffend Nederland leven. Dan denk ik echt van dit is diarree uit de onderbuik.
[jg76nx3] (score 6, diepte 1) Het is toch gewoon smerig? Sorry maar dat is echt kleuterniveau opvoeding.
[jg77se5] (score 6, diepte 2) Smerig en asociaal, ja, iets om ja een half uur aan te gaan zitten ergeren, nee.
[jg7c9ae] (score 5, diepte 3) Oetz moeten we voor dit soort zinloos geweld gewoon levenslang geven, of zelfs weer de doodstraf invoeren. We moeten als maatschappij ons beschermen tegen mensen die zonder reden anderen van het leven beroven. 

De straffen voor geweldsdelicten in Nederland zijn zo absurd laag. Ik kan mijn buurman doodslaan en tien jaar later gewoon weer verder met mijn leven. Absurd.
[jg7ap5x] (score 5, diepte 0) Herkenbaar.

Probeer te accepteren dat het niet jouw verantwoordelijkheid is.

Bedenk goed dat het NS zelf en 90% van het volk niet boeit. 

Dus het is zonde van jouw energie om je er mee bezig te houden.

In dit land krijg je stank voor dank namelijk. 

Mijn tip koop een auto, ligfiets of speed pedelec
[jg7mibc] (score 5, diepte 1) Zoals anderen vertellen dat ze zich niet aan moeten stellen?
[jg7q2lz] (score 4, diepte 3) Al die aso's die ik buiten tegenkom stemmen echt niet op de VVD hoor.

VVD'er kijken vooral naar geld, maar zijn niet aso in omgang.. 

volgens mij ben je nu gewoon je eigen sneue haat richting politiek aan het verwarren met omgangsnormen in het normale leven, die totaal los staan van welke partij iemand kiest. 

&#x200B;

En was het nog maar oud hollands, dan keken mensen tenminste nog naar elkaar om, en was er nog sociale controle.. nu is iedereen te bang om ergens iets van te zeggen omdat ze anders neergestoken worden.. en nee, dat zijn zeker geen vvd'ers.
[jg7b7lz] (score 4, diepte 0) Als ik moe was legde ik ook mijn voeten op de stoel.  
Maar wel altijd met een krant er onder én achter zodat de zitting en de rugleuning niet vies werden. Of mijn eigen rugzak of jas als er geen krant was.  
En bij elke stop hield ik de deur in de gaten of ik ruimte moest maken (dat doe ik ook als ik met een tas reis die ik op de stoel heb staan).

Een keer vroeg een controleur mij of ik thuis ook mijn voeten op de bank legde. Ik vertelde hem dat ik dat inderdaad deed en ook op de tafel, maar dat ik in huis geen schoenen droeg. Ik kon het echter mijn medepassagiers niet aandoen om mijn schoenen uit te trekken en daarom legde ik altijd iets onder mijn schoenen.

Hij kon een grijns niet onderdrukken en zei dat ik wel ruimte moest maken als er mensen kwamen.
[jg5iht8] (score 3, diepte 0) Kheb al eens iemand met zen blote voeten op de bank zien zitten 🤢
[jg6olf8] (score 3, diepte 0) Is this Dutch culture
[jg6ymxd] (score 3, diepte 1) Dankjewel. Zoek gewoon zoals normaal lekker n schoon stoeltje uit met n mooi plekje. Zolang er geen extreme dingen gebeuren boeit t me echt niks wat mensen in de trein doen (mits ik n koptelefoon op heb)
[jg7qi1y] (score 3, diepte 1) De stoelen worden er vies van en slijten harder.

Daardoor wordt mijn broek vies en zijn de onderhoudskosten van het OV hoger. En dat merk ik in mijn vervoerskosten.
[jg7qjwp] (score 3, diepte 3) Dat is pas content! 
Beschouw jezelf hartgrondelijk bedankt !
[jg7qler] (score 3, diepte 4) 🫡
[jg89u6y] (score 3, diepte 4) maar daar zijn je ogen voor. als je ziet dat het vies is hoef je er niet te gaan zitten. je kijkt buiten toch ook of een bankje onder is gekakt door vogels voor je er gaat zitten?
[jg7494u] (score 3, diepte 0) Je moet je inderdaad niet zo aanstellen. Probeer je focus te verleggen naar zaken die er wel toe doen.
[jg7hywe] (score 3, diepte 2) Ja, dus?
[jg7fr4u] (score 3, diepte 0) Het is fucking asociaal, daar ben ik het met je eens. Maar ik zou mijn mond gewoon houden als ik jou was. Er lopen zo veel debielen rond die je al om de nek vliegen als je ze verkeerd aankijkt, laat staan aanspreekt...
[jg7h1tv] (score 3, diepte 0) Ik vind het zelf ook verschrikkelijk. Het is alsof die mensen niet zijn opgevoed. Maar het dilemma blijft, accepteren we dit soort asociaal gedrag in de angst om neergestoken te worden met het risico dat dit steeds vaker voor zal komen of riskeer je je leven door iemand op zijn onacceptabele gedrag te wijzen?
Zeker als ik alleen ben zeg ik er niks van, je weet nooit welke normen en waarden iemand nog meer niet uit huis heeft meegekregen.
[jg8a3rl] (score 3, diepte 1) Mee eens. Treinen zouden dagelijks gedweild moeten worden. Als er bij mij ook duizenden mensen per dag over de vloer zouden komen, dan ga ik ook wel ff dweilen.
[jg88el2] (score 2, diepte 2) En vergeet niet 'peuken en ander afval op de grond gooien'. zucht.
[jg7r3jo] (score 2, diepte 8) Woordsalade, niet woordkots, hou t een beetje geciviliseerd. Denk aan de persoon die zojuist het kots-verhaal deelde.
[jg77qub] (score 2, diepte 3) Ik heb een geweldig leven maar ook van jouw reactie leer ik dat ik beter mijn mond kan houden. Dat jij je er niet druk om maakt wil niet zeggen dat een ander dat ook maar niet zou moeten doen. Prima dat jij het onzin vindt.
[jg7cd2x] (score 2, diepte 2) Jouw kleding is voornamelijk belangrijk voor jou. Als je je niet drippig genoeg voelt met wat anders dan brandschone kleren dan is het misschien tijd om je prioriten te gaan verleggen.  


Denken in "wij" en "zij" termen is behoorlijk kansarm.   


Jij mag er gerust wat van vinden. Doe je ook, anders kon ik niet op je reageren.
[jg71d6o] (score 2, diepte 0) Zolang de geen stront onderzit
[jlc2lsn] (score 2, diepte 3) Heb echt met plezier gelezen!
[jg8b985] (score 2, diepte 5) Klopt, maar de stoel ertegenover en ernaast blijven dan ook leeg door de stank. Gewoon niet doen. Net als afval op de grond gooien en kotsen op de grond.
[jg8yt42] (score 2, diepte 6) Je leest een kop, je leest wat sappige details en je ondertussen lees je 0 dossiers, en zeker geen uitspraken in eerdere vergelijkbare zaken.
[jgcyejl] (score 2, diepte 10) Lekkere inhoudelijke reactie van je.
[jg7mstu] (score 2, diepte 2) Schering en inslag dat mensen doodgeslagen worden omdat ze ergens iets van zeggen? Heb je hier bewijs of data voor? Volgens mij is het gelul.
[jg80z7q] (score 2, diepte 1) Verhaal deed me gelijk denken aan het liedje van lange frans en baas b "zinloos"
[jg78vyv] (score 2, diepte 3) Het hoeft je dag niet te verpesten nee, maar in eerste instantie zou.ik.me.er ook aan ergeren.
[jg7ahmf] (score 2, diepte 2) Dan ga je ergens anders zitten, of je veegt de epische hoeveelheid aan zandkorrels van je broek met je hand. Je kan daarna eventueel nog gaan janken over smerige handen.  


Bel jij de gemeentereinigingsdienst als je op een parkbankje wil gaan zitten wat er langer dan 30 seconden staat?
[jg7c2ab] (score 2, diepte 4) Niet moeilijk? Waarom doe je dan zo moeilijk over wat bacterien waarvan je zelf aangeeft er niet zo bang voor te zijn?  


Je laatste zin verklapt je leeftijd.
[jg8ien9] (score 2, diepte 6) Maar hoe weet jij dat daar iemand heeft gezeten met poepschoenen op de bank?  


Zie je poepresten? Ga er dan niet zitten.   
Zo moeilijk is het allemaal niet.
[jg8vmzo] (score 2, diepte 2) Beetje chargeren natuurlijk maar ik vind veel van mijn medemensen (ik werk elke dag met klanten van mijn werkgever) echt bizar lomp, asociaal of gewoon onvriendelijk. En dan doe ik de hele dag ook alsof ik die mensen heel aardig vind. Ik zie ook nog genoeg mooie dingen hoor, zoals mijn vriendin!
[jg8z38z] (score 2, diepte 3) Herkenbaar, ik was ooit een mensen mens, dat heeft klantenservice me na jaren wel afgeleerd. Veel mensen zijn echt onbeschoft en egocentrisch. Maar er zitten juweeltjes tussen, die maken alles weer goed!
[jg9ln02] (score 2, diepte 4) Go work at klantenservice they said, it will be fun they said
[jg7mah1] (score 2, diepte 1) klinkt als een goede mentaliteit om een land compleet naar de klote te laten gaan met alleen maar mensen die weg kijken en 0 sociaal zijn..  hier zou ik echt niet willen wonen.
[jg7grs3] (score 2, diepte 3) JBL boombox mee en op volume 10 pianomuziek draaien naast bellende persoon. Zal gauw ophouden te bellen wanneer je de box weer uitschakelen kunt
[jg7g68d] (score 2, diepte 0) Een kennis van mij zei er ooit wat van, eindigde met een gebroken neus en een hersenschudding. Gewoon laten gaan denk ik dan. Of accepteren dat de kans er is aangevallen te worden en bij voorbaat je aardappelschil mes grijpen en voor de ogen gaan.😁 Succes!
[jg7rk0r] (score 2, diepte 2) Die mededeling lost het probleem ook gewoon op. /s
[jg7k8c3] (score 2, diepte 0) Zo vind ik dat dus ook met honden op de stoelen in de trein/bus. 
Gisteren nog een grote pitbull in de bus op een stoel gezien. Wat asociaal zeg.
[jg7nf0b] (score 2, diepte 0) Vragen die opkomen: is dit jouw verantwoordelijkheid? Heb je er invloed op? Wil je er invloed op hebben? Focus je vaker op het negatieve in plaats van het positieve? Wat levert het je op als je hier mee bezig bent? Krijg je er energie van? En klopt het dat je er naar *moet* kijken? Van wie moet dat dan? Staat er iemand met een pistool op je hoofd gericht? Nou ja. Etcetera.
[jg7r1ux] (score 2, diepte 0) Honestly? De trein is tering smerig op een gemiddelde dag dat het me echt geen ene reet boeit. Op een gemiddelde ochtend kom ik de trein binnen en plakt de vloer, zijn alle vuilnisbakken overvol waardoor vuilnis buiten de bakken beland, enorm veel stof, de wc altijd zo goor dat je hem als vrouw zijnde toch nooit kan gebruiken, etc. Op een minder gemiddelde ochtend kom je de trein in en ligt er een plasje kots met alcohol blikjes ernaast. Mensen die voeten op de stoelen doen is echt de laatste van mijn zorgen.
[jg7yrcz] (score 2, diepte 0) 1e Klas kaartje kopen, kan je netjes tussen de beschaafde mensen zitten.
[jg85aar] (score 2, diepte 0) Als medewerker van Prorail gedurende 30 jaar heb ik altijd mensen aangesproken.
Kots daar kan je weinig aan doen in een rijdende trein maar schoenen op de bank??
Dan vraag ik of ze dat thuis ook doen en als dan zo'n lolbroek ja zegt? Dan wens ik ze een schoon leven toe met meer besef voor hun gedrag.
Meestal honend wordt daarop gereageerd en dan zeg ik oh sorry had niet door nog dat je al zooo diep gezakt bent.

Uiteraard ga ik grote lummels maar  1 keer vragen over thuis en schoenen, daarna laat ik ze in hun sop gaar koken.
Behalve een vrouw die haar naaldhakken in de stoel had geprikt.
Die was stomvervelend, toen heb ik via vl, de conducteur laten komen(een vrouw) die was niet mals, die naakdhakken hebben 90 euro extra gekost😃
[jg8klla] (score 2, diepte 0) Er zit letterlijk nu iemand aan de andere kant van het gangpad in z’n eentje op een vierzits met z’n schoenen uit met z’n voeten op de bank op de luidspreker (maar aan z’n oor 🤨) te bellen in de stiltecoupé. Heel agressief m’n ogen rollen is het maximale waar ik energie voor heb.
[jg8l0oz] (score 2, diepte 0) En dan dit gesprek tussen de reiziger en conducteur:

Doe je dit thuis ook 

Nee, ik heb thuis geen trein
[jgbw30l] (score 2, diepte 1 OP) Volgens mij ben jij hier de zuurpruim. Ik heb wel grotere problemen,  maar dan betekent het niet dat ik verder maar me bek moet houden toch. En als het je het allemaal zo'n onzin vind,  scroll gewoon lekker door.

Jezus ik hap ook nog.
[jgc0vmy] (score 2, diepte 5 OP) Dat kun je ook doen zonder iemand zo persoonlijk aan te vallen. Echt nergens voor nodig. Beetje beschaafd blijven kan geen kwaad.
(93 reacties met lagere score weggelaten)

