# Label-batch batch_0168

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
Schrijf het resultaat naar `batch_0168.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1eye15i, 1khmy3f, 1bmljiw, 1wt7a2n).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1eye15i ===
SUBREDDIT: r/thenetherlands
DATUM: 2024-08-22  SCORE: 0  REACTIES: 76
TITEL: Stel je hebt een week vrij nu: waar zou je naar toe gaan om het slechte weer in NL te vermijden? 
POST (source_id=post):
Vertel!

Edit: ik woon in het westen van NL. Hier waaien de sokken van je voeten af en t is bewolkt. Fijn voor iedereen in het binnenland dat bij jullie zonnetje schijnt. Maar hier niet. Hier zie ik donkere wolken boven mn hoofd.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ljcl2gs] (score 169, diepte 0) Slecht weer?
[ljcmze4] (score 50, diepte 1) exact! Ik kijk naar buiten en het is zonnig plus een aangename temp...wat is er te vermijden?
[ljco1xu] (score 20, diepte 0) Het is nog zeker tot midden september 20+ graden.
[ljcqcg4] (score 16, diepte 1) Vgm is dit een van die bot accounts waar een post laatst over ging. Klopt ook als ik de naam lees van "OP."
[ljcn1lj] (score 15, diepte 0) Zonnetje, wind, 23 graden nowhere I'd rather be! Volgende week daarentegen...
[ljcmwrp] (score 14, diepte 0) Uh, Gelderland? Daar is het minstens 25 graden vandaag.. ik wil juist dat "slechte weer" hebben
[ljcndbd] (score 14, diepte 0) Welk slechte weer?
[ljcz1mr] (score 13, diepte 0) Ik word zo ziek van mensen die zomerweer als objectief "goed" of "fijn" weer neerzetten. Is gewoon persoonlijke voorkeur. Ik zou liever weggaan als het weer een week 26°C+ is want dat is niet uit te houden. Verder naar het Noorden.
[ljclcdm] (score 10, diepte 0) Centerparcs en de hele week in het zwembad chillen
[ljcnug5] (score 10, diepte 0) Welk slechtweer?
[ljcpnbj] (score 10, diepte 0) Op de bank en de PS5 aanslingeren
[ljcnlgg] (score 9, diepte 0) Welk slecht weer? Zonnetje, perfecte temperatuur, ik ben echt benieuwd waarom je dit slecht weer noemt.
[ljcnxlz] (score 8, diepte 1) Ik denk dat OP een hekel heeft aan zon?
[ljcqhoh] (score 8, diepte 2) Hier in Gelderland is het echt perfect weer op het moment, 21 graden en heel licht bewolkt
[ljcsavx] (score 8, diepte 2) Ik heb gisteren genoten van het weer in Groningen. Af en toe een paar drupjes, maar heerlijk windje, perfecte temperatuur, en prachtige wolkenluchten.
[ljczuia] (score 7, diepte 1) Ik dacht ook al. Het is eindelijk lekker weer, niet meer zo warm and af en toe een buitje, perfect wat mij betreft.
[ljcohey] (score 7, diepte 0) Welk slecht weer?
[ljcqnre] (score 6, diepte 0) Ik zou gewoon in Nederland blijven met dit weer. 

Maar als de voorspelde 25+ graden van komende week slecht weer voor je is: Death Valley in California. Hogere temperatuur en minder regen.
[ljct12v] (score 5, diepte 0) Ik snap OP wel hoor. Op dit moment in Noord Holland Noord erg harde wind, klein buitje en grijs. Als ik een tip mag geven: t weerbericht van volgende week ziet er goed uit in Nederland, dus je hoeft niet heel ver weg om lekker weer te hebben!
[ljdmys8] (score 4, diepte 2) Allen wat jij zegt klinkt als heerlijk weer voor mij. Ik kan niet wachten tot ik weer het dekbed uit de kast kan halen.
[ljcoxvh] (score 4, diepte 1) Helemaal mee eens! Ik vindt her hier al snel te warm.
[ljcontx] (score 4, diepte 0) Het is niet ontzettend heet nu maar als er weer een hittegolf is dan het liefst naar noorwegen of finland en dan gewoon rondreizen met een tent + hostels
[ljcp6bi] (score 4, diepte 0) Is OP een bot? Want het is geen slecht weer. Er staat bij mij zelfs 28 graden in voor volgende week
[ljdn8fj] (score 4, diepte 2) Iedereen z'n voorkeur :D
[ljcl2nr] (score 3, diepte 0) Welk slecht weer? Met temperaturen net boven de 20 is het prima te doen. Pas volgende week krijgen we weer van die kut-hitte.
[ljd3p4z] (score 3, diepte 1) Hier in Amsterdam waai ik zo ongeveer omver met het stevige briesje wat hier staat. Is ook grijs, bewolkt en somber. Noem het niet echt mooi weer.
[ljcucvn] (score 2, diepte 1) overdekt toch.??
[ljcmz5z] (score 2, diepte 0) De mergelgrotten in Zuid-Limburg?
[ljcni9k] (score 2, diepte 0) Frankrijk-spanje-portugal

Eigenlijk ergens waar je kan surfen
Of naar Fontainebleau om te klimmen
Slecht weer is voor mij vooral gebrek aan golven
[ljco4qn] (score 2, diepte 1) Ericeira Portugal. Heerlijk surfen daar.
[ljcye2c] (score 2, diepte 2) Nou ja het kan ook prima gaan. Hele maand geïnterrailed. Maar één trein gemist door vertraging en er ging later een alternatief. Met een andere trein met vertraging aangekomen op eindbestemming van de dag. Voor een hele maand valt dat mee.


Dus je had pech :/
[ljd2yij] (score 2, diepte 2) Nou ja, persoonlijk kan ik me er prima op instellen dat het niet soepel loopt, en heb ik er ook nog lol in om gedurende de trip om de ellende heen te plannen om nog optijd aan te komen
[ljcxfn1] (score 2, diepte 0) Helemaal nergens. Heerlijk vind ik het nu, eindelijk weer wat verkoeling. Persoonlijk vond ik het maar een kut zomer. De ene dag 17 graden, twee dagen later 32. Dan weer 22, dan weer 30. Helemaal schijtziek werd ik er van.
[ljczdqh] (score 2, diepte 0) Op dit moment enkel zonneschijn. Wel een goede wind, waardoor het fris is. Maar niet slecht genoeg om NL te vermijden. 

Toch kan het altijd beter, maar mijn antwoord is dat niet per sé. Ik zou naar het Duitse Schwarzwald gaan. Puur omdat dat mijn favoriete vakantiebestemming is. Het weer daar is nu vergelijkbaar met hier, 22 graden - zonnig - een beetje wind. Maar de omgeving is zó veel mooier!
[ljz84bd] (score 1, diepte 2) Nah, daar moeten streepjes tussen. Voorbeeld-Botnaam6493
[ljcwqof] (score 1, diepte 2) Zeker weten
[ljd0uhx] (score 1, diepte 3) dan heeft het weer geen invloed op je zwembad
[ljcn4eo] (score 1, diepte 0) Naar bed.
[ljcofju] (score 1, diepte 2) Nog niet geweest :0
[ljco01g] (score 1, diepte 0) Interrail kopen, en een hotel boeken ergens in europa waar het leuk genoeg weer is om dingen te doen.
[ljcok96] (score 1, diepte 1) Interrail is leuk in theorie, in de praktijk stress je ‘m dood door uitvallende treinen of treinen die veel te laat komen. Been there, done that, nooit meer. Ik vlieg wel totdat treinen in Europa eindelijk een keer acceptabel werkt.
[ljco2n6] (score 1, diepte 0) Ons gematigde (Noord)zeeklimaat zorgt ervoor dat er nog wel es wat variatie is, dus als ik wat stabieler weer zou willen, zou ik afzakken naar zuidelijk Europa, naar een plek met een meer Mediterraan klimaat. Voor een weekje zou ik niet een vliegtuig in klimmen ofzo.
[ljcp6dk] (score 1, diepte 0) Naar bed
[ljcveow] (score 1, diepte 1) Dit is het enige juiste antwoord
[ljcya3j] (score 1, diepte 1) Ik zeg altijd: het is altijd weer om te gamen
[ljcsx3g] (score 1, diepte 0) Slecht weer? Ik zit ook in het westen maar de zon schijnt...
[ljct0hf] (score 1, diepte 0) Ik snap OP wel hoor. Op dit moment in Noord Holland Noord erg harde wind, klein buitje en grijs. Als ik een tip mag geven: t weerbericht van volgende week ziet er goed uit in Nederland, dus je hoeft niet heel ver weg om lekker weer te hebben!
[ljcxoja] (score 1, diepte 1 OP) Ah Fijn, eindelijk (h)erkenning
[ljevhh8] (score 1, diepte 1) Heerlijk, een open kernfusie reactor boven je hoofd, zonnebril omdat het licht te fel is, te warm om je kleren aan te doen dus een zalfje met uv blokker om je huid te beschermen tegen de straling. Zwetend je bed in, en uit. Geel gras, sjouwen met water om je planten te redden. Wat is mooi toch heerlijk.

Doe mij maar dit weer. Groetjes uit West Nederland.
[ljcua8g] (score 1, diepte 0) Den Haag hier; de zon schijnt er vrolijk op los. Strand is bijzonder aangenaam.
[ljcuuoo] (score 1, diepte 0) Valt toch wel mee met het weer? Ik zit lekker in de tuin en woon ook in het westen. 

Anyway, ga dan een weekje naar het binnenland, naar Limburg of Drenthe
[ljcyk9h] (score 1, diepte 0) Hoezo zou nu weg will gaan. Dit het perfecte zomerweer.
[ljda8xx] (score 1, diepte 1 OP) Does lief
[ljczpvs] (score 1, diepte 0) Ik zit in "het binnenland" en het waait hier al een paar dagen stevig. De temperatuur is opzich prima, had best een paar graden warmer gemogen, maar door die harde wind fiets ik mezelf toch aardig in t zweet. Had voor mij niet gehoeven, een briesje is lekkerder.
[ljd0ove] (score 1, diepte 0) Niet zo moeilijk doen. In virtual reality schijnt de zon altijd, en dankzij deze redelijke temperaturen zweet ik me niet te pleuris met m'n headset op.
[ljd297a] (score 1, diepte 0) Lyon is prins te doen met de trein voor een week
[ljddjul] (score 1, diepte 0) Naar mijn woonkamer. Lekker een weekje binnen in huis rondhangen klinkt eigenlijk wel lekker. Wat gamen, gitaar spelen, bordspelletjes er bij en geen last van het weer.
[ljdf8p5] (score 1, diepte 0) Ja kan altijd naar binnen
[ljdgvum] (score 1, diepte 0) Ik woon in Ierland. Ik ga naar Nederland voor het goede weer!
[lje5yv1] (score 1, diepte 0) 23 graden in Breda, beetje zonnig en bewolkt, zo lekker op de fiets naar huis.

  
Sorry...
[ljes0rn] (score 1, diepte 0) Om even wel wat constuctiefs te zeggen, in plaats van al die mensen die denken origineel te zijn met ‘welk slecht weer’? (Het was de afgelopen week inderdaad wat grijs en grauw) ik zou naar Spanje gaan, of ergens in de zuidelijke helft van Frankrijk.
[ljfvpvb] (score 1, diepte 0) Niet naar Panama zeg ik je, gvd wat een regen hier momenteel.
[ljj9ixy] (score 1, diepte 0) Ik zit nu in Cochem en het weer is hier top :)
Je hoeft dus niet ver weg.
[ljcpxqi] (score 0, diepte 1) Het is hier in Groningen al de halve week grauw weer en nu zie ik de zon ook al de hele ochtend niet. Man, ik heb van de week het dekbed weer uit de kast gepakt. Het werd fris s nachts. 

Sterker nog, ik zou dit weekend naar een pretpark gaan maar dat hebben we afgezegd vanwege het weer. Waar zit jij in Nederland dat het wel goed weer is? Aruba?
[ljdaprj] (score 0, diepte 2 OP) Ha nog een medestander. Ik dacht al, hangen de wollen boven mijn hoofd en niet breder?
[ljcnmvp] (score 0, diepte 0) Siracusa (vlieg op Catania) of Sorrento (vlieg op Napels).
[ljcnru2] (score 0, diepte 0) Thuis blijven.
[ljcoczx] (score 0, diepte 0) what bad weather?!
[ljcoqd0] (score 0, diepte 0) Ik ben ja nait van suiker toch
[ljcpcac] (score 0, diepte 0) Nog even geduld, volgende week gaat de zon weer schijnen
[ljcpo64] (score 0, diepte 0) Zodra het weer wat koeler wordt, zou ik wel een weekje naar Griekenland willen. 

Lekker naar de warmte!
[ljcq6w1] (score 0, diepte 0) Als geld geen issue zou zijn, de malediven.
[ljcr4pn] (score -1, diepte 0) Welk slecht weer?

=== THREAD 1khmy3f ===
SUBREDDIT: r/nederlands
DATUM: 2025-05-08  SCORE: 28  REACTIES: 67
TITEL: Blaren op voeten door werk
POST (source_id=post):
Ik werk in een magazijn en ik moet veel lopen, maar dan ook echt veel. Ik heb altijd een stappenteller aan staan, zet gemiddeld zo'n 40-45k stappen op een dag. Rond de 35 kilometer lopen dus. En geloof me op stalen werkschoenen is dat geen pretje. 

Nu vraag ik me echt af hoe ik van deze pijn in mijn voeten af kom. Ik gebruik al inleg zooltjes, maar als ik na mn werk de volgende ochtend wakker wordt kan ik oprecht niet rechtop staan.

Tips?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mr80y5l] (score 139, diepte 0) Praat met je HR afdeling en bedrijfsarts.
[mr81mkw] (score 91, diepte 0) Andere werkschoenen vragen en eventueel steunzolen laten aanmeten, je werkgever moet hier in voorzien als jij zoveel op je benen moet staan.
[mr82wli] (score 58, diepte 1) En preventiemedewerker. Er zijn genoeg comfortabele werkschoenen op de markt.
[mr82ewk] (score 31, diepte 1) Dit klopt, al weet ik dat bijv bij Hunkemöller als je hiermee aankwam je als temper ( vaak komen ze van uitzendingsbureaus and randstad etc ) je de volgende week niet meer hoeft te komen. 

Honden zijn t .
[mr811ey] (score 27, diepte 0) Van vrienden die in het verleden in magazijnen hebben gewerkt , Hunkemöller etc geven aan dat ze toen ze er na 2 jaar stopte met werken nog 3 jaar last van hadden. 

Vraag of er betere  schoenen mogelijk zijn. Vaak zijn het beveiliging schoenen maar van de goedkoopste qualiteit, die veroorzaken dat. Kans is groot dus dat je er niet vanaf komt. Niet zolang je er blijft werken
[mr81m0g] (score 17, diepte 0) Kijk naar lowa renegade werkschoenen is een hele stevige wandelschoen met stalen neus. 
Tenminstte mijn voeten gedijen het best in een stevige schoen.
Maar 35 km per dag??? 
Dan ben je 7 uur continu aan het lopen met 5 km/h bizar!
[mr82ljb] (score 12, diepte 1) Of een bedrijfsfiets voor in het magazijn. Als je 35 kilometer loopt op een dag is het een enorm gebouw.
[mr82yzt] (score 10, diepte 0) Andere werkschoenen waar je wel makkelijk op kan lopen. En qua sokken zou je kunnen kijken naar wandelsokken, die passen vaak wat beter om je voet omdat er minder stof zit bij je kleine teen. En Gehwol voetencreme, die voorkomt blaren.
[mr80yoc] (score 8, diepte 0) Ik zou even contact opnemen met jullie bedrijfsarts.
[mr8106g] (score 8, diepte 0) Tjesis. Dat zijn écht veel stappen. Misschien sneakers met stalen neuzen? Of kevlar. Wel jaloers qua beweging ;)
[mr83nkc] (score 8, diepte 1) Welkom in de wereld als orderpicker
En vooral degene waar iemand met zijn opdrachten constant in je oor tettert.

Mijn was dat ook aangeboden (als tetteraar) mag je de hele tijd 1, 2 of 3 mensen aansturen met vaknummer en aantallen.

Ooit in mijn jeugd orderpicking gedaan bij een DC van de supermarkt, maar ook toen al was het slavenwerk voor weinig
[mr8r5ow] (score 8, diepte 4) Dan koop je zelf nieuwe schoenen, je gaat je eigen voeten toch niet kapot lopen omdat je werkgever geen andere schoenen wil geven?
[mr991y3] (score 8, diepte 5) Vaak zijn deze banen minimum loon, die mensen zitten al met hun vaste lasten, huur en eten. Vaak lopen ze vast met hun uitgiftes. En die schoenen zijn vaak peper duur. Heb het hier over meer dan 180 euro. Vooral als ze aan de ‘voorwaarden’ moeten voldoen.
[mr81srp] (score 6, diepte 0) Goede werkschoenen helpen veel. Van die dingen die ik vroeger kreeg van het uitzendbureau waren echt 3x niks. Misschien dat je in overleg met de bedrijfsarts iets kunt regelen

Maar ik kan je daar verder geen specifieke merken in adviseren, ik draag zo'n schoenen tegenwoordig niet meer
[mr86k8q] (score 5, diepte 2) Zo'n elektrische monowheel zou voor een druk magazijn bij orderpicking misschien nog beter zijn. Fietsen zijn groot en lomp.
[mr9db0t] (score 5, diepte 5) Voor een minimum loontje mag je ook je eigen dure werkschoenen aanschaffen want die van €40 zijn kut. Je baas declareert zijn lunches.
[mr854e0] (score 5, diepte 0) Blijkbaar zou alpacawol of schapewol tussen je tenen steken ook helpen...mijn echtgenote doet dat ook sinds kort...en er is ook nog compeed
[mr8cpno] (score 4, diepte 2) Heelys
[mr810oi] (score 4, diepte 0) Stepje? Fiets? Golf karretje.
[mr88cn5] (score 4, diepte 2) Dan kunnen ze naar hun uitzendbureau gaan, voorheen toen ik gedetacheerd werkte kreeg ik het ook vanuit mijn uitzendbureau of detacheerder.
[mr820pp] (score 4, diepte 0) Ik loop ook veel tijdens het werk en heb mezelf bij een orthopeed zooltjes laten aanmeten. Beste cadeau aan mezelf ooit! Misschien zou je daar eens naar kunnen kijken.
[mr8430y] (score 4, diepte 1) Ik kan je vertellen, met de verkeerde schoenen ga je het nooit redden.
Ik kreeg in mijn 'inwerkjaar' van het uitzendburo schoenen, er zaten stalen neuzen en zolen in, maar de rest was het gewoon een doos met veters.

Zelf een paar DTCH gekocht en later kreeg ik de schoenen voor 'vaste' medewerkers.
Kwalitatief mijlen beter !
Ik wissel ze nog steeds af, over een maandje is het weer zover dat ik al mijn PBMs kan vervangen (nog niet nodig)
[mr832mp] (score 4, diepte 0) Ik denk dat een elektrische orderpicker oid waar je op kan staan en of zitten beter voor je is, of een bakfiets. Het is niet normaal zoveel te lopen. Misschien moet eens gekeken worden waarom je zoveel loopt en of dat niet efficiënter kan. Ik had een dergelijk probleem, extreem groot atelier met drie hallen en ongelijke vloeren en veel cursisten die op verschillende plekken werkten. Ik liep over beton en straattegels. Ik kocht Steel Blue schoenen, dat ging al veel beter, verder had ik een fietsje om tussen de hallen heen en weer te gaan wat ook goed hielp.
[mr80yfl] (score 3, diepte 0) Andere schoenen vragen aan je werkgever, of zelf investeren in goed passende werkschoenen. Mijn vriend vond Bata schoenen fijn, al liep hij er niet per se veel op.
[mr814g3] (score 3, diepte 0) Wollen sokken van t leger zou ik aanraden.
[mr81nfk] (score 3, diepte 0) Gebruik dikke hoge sokken, dr martens heeft speciale inloop sokken.
[mr82632] (score 3, diepte 0) Hoe lang werk je er? Als het vrij kort is, dan moeten je voeten nog flink eelt ontwikkelen.
Is dit niet het geval, dan ik in gesprek gaan met je teamleider of bedrijfsarts om te kijken naar andere werkschoenen.
Of een inlegzool proberen, maar dat ligt ook een beetje aan de plek waar je blaren zitten.

Zelf ben ik fan van wollen sokken in wandelschoenen, werklaarzen met harde neus. Is niet extra heet in de zomer in mijn ervaring.
[mr85r4c] (score 3, diepte 3) Ik had geluk, met mijn bijdehante smoel de helft teruggekregen van het uitzendburo.
Gewoon gevraagd of ze me liever op de vloer hebben of thuis.

Maar dat is in een bedrijf waar ik mijn 'waarde' al had laten zien, en mijn contract 95% veilig was.

Als orderpicker bij bol of Jumbo vermoed ik dat je snel buiten staat daarna
[mr8357p] (score 3, diepte 0) Damn, wat doe je in het magazijn dat je zoveel stappen moet zetten? Ik werkte ook ooit in een magazijn, kwam echt wel easy aan de 10-20k stappen, maar echt iedereen zat wel op iets van een voertuig of hoefde niet enorm veel te lopen.
[mr853c1] (score 3, diepte 1) Idd ik zat gemiddeld op 15k per dag.
Èèn keer een week 20k elke dag.

35k+ is ronduit belachelijk IMO.

Mits je per 1k 10 cent krijgt.
[mr8433j] (score 3, diepte 0) een oplossing zou zijn investeren in kwaliteit werkschoenen.

Kost een beetje maar dan heb je wel een schoen die loopt als een sneaker _en_ aan alle veiligheids regels voldoet.
[mrag40d] (score 3, diepte 0) Op een goeie werk dag haal ik 20 000 stappen (wel buiten, veelal door gras en "wandelpaden") dus weet niet of het veel helpt. Maar wat ik doe:

Wissel af en toe van schoenen. Ik heb 3 paar schoenen waar ik mee werk, alle drie liggen in m'n werkbus en tijdens m'n pauze wissel ik naar een ander paar, dit voorkomt dat een plekje in een bepaalde schoen blijft schuren en een blaar veroorzaakt (bijvoorbeeld 2 verschillende stalenneuzen schoenen, zodat het randje waar de stalenneus niet constant hetzelfde plekje raakt).  Let wel op dat de schoenen waar je tussen wisselt allemaal goed uitgelopen zijn.

Compressie sokken. Ik voelde me echt een 50 plusser toen ik ze kocht, maar het zijn nu echt mijn favoriete sokken voor werk. Dit voorkomt vochtophoping in de voeten en benen. Niet perse tegen blaren maar helpt heel erg tegen "vermoeide" benen en voeten.

Slapen met voetjes omhoog. Dit voelt echt raar in het begin, maar het went. Een dik kussen aan mijn voeteneind vind ik zelf het makkelijkst en fijnst. Dit zorgt dat het vocht wat toch naar je voeten is gezakt gedurende de dag weer makkelijk wordt verwijderd in de nacht. Net als de compressie sokken niet perse tegen blaren, wel tegen vermoeide voeten in general. (Ook ideaal bij verstuikingen of andere oorzaken van vochtophoping in de voeten!)

Verder sluit ik me aan bij de comments over op maat gemaakte inlegzooltjes (let op compatibiliteit met stalenneuzen!), bedrijfsarts en contact met je werkgever.
[mr9ejp2] (score 2, diepte 2) Draag goede wandelsokken. Met merinowol. Bijvoorbeeld een mid weight setje van DarnTough. Die dragen heerlijk, steunen je voeten, en voorkomen blaren.
[mr86do2] (score 2, diepte 0) Andere baan zoeken, dat is toch echt veel te veel iedere dag.
[mr87qn8] (score 2, diepte 0) Is er iemand die ongeveer deze afstand per dag ook moet stappen voor zijn werk? Lijkt mij heel sterk. Met deze afstanden verwacht je toch een hulpmiddel zoals een segway oid?

Wat vind de arbo hiervan?
[mr8ke5o] (score 2, diepte 0) Jezus joh. Ik zit zelf in de logistiek, ook deels als orderpicker,  en ik zet op n gemiddelde dag zo'n 14.000 stappen. Wat jij doet is niet gezond!!
[mr8kkil] (score 2, diepte 0) Idd eens met goede werkschoenen en evt zooltjes. 


Misschien kan je na je werk ook nog enkele minuten wat oefeningen of yoga doen om je hele onderlichaam nog te laten inspannen en daarna ontspannen. En rol je voeten uit op een harde bal.
[mraj0pa] (score 2, diepte 0) Ik heb Puma crossfit werkschoenen. Laag model. Loop wel geen kilometers per dag maar de schoenen zitten comfortabel. Zien eruit als sportschoenen.
[mrbetg1] (score 2, diepte 0) Betere werkschoenen, je hebt ook veilige die lekker zitten, die kosten wel meer dan een paar tientjes.
[mrn8z1j] (score 2, diepte 1 OP) Jammergenoeg wel ja. 3/4 marathon elke dag. Nou hou ik dat nog wel vol omdat ik jong ben maar wil niet weten hoe mijn 40 jarige collegas zich voelen
[mr8a45h] (score 1, diepte 1) Rolschaatsen!
[mr8abpw] (score 1, diepte 1 OP) Ik werk er nu 2-3 maanden. Het zijn vooral de blaren die vervelend zijn. Elk weekend zijn ze weg, en zodra de volgende werkweek begint zijn ze er weer
[mra0yqy] (score 1, diepte 1) Let wel op dat je niet zomaar elke soort steunzool in een veiligheidsschoen mag leggen. Moet altijd gecertificeerd worden in de schoenen.
[mrao3z7] (score 1, diepte 2) Ik neem aan dat die van een podotherapeut goed zijn? Die heeft er een hele opleiding voor gedaan, een podoloog niet.
[mrar2uv] (score 1, diepte 3) Ik zeg ook niet dat de steunzolen van een podotherapeut slecht zijn toch? Heb met veel samengewerkt. Ik meet zelf ook steunzolen aan. Het enige wat ik zeg is dat je niet zomaar elke steunzool in een veiligheidsschoen mag leggen. De zool moet aan veel regels voldoen, bijvorbeeld dikte, afdekmateriaal, van welk materiaal de zool is gemaakt, en moet daarna gecertificeerd worden in de schoen, anders ben je niet verzekerd. Naar mijn weten zijn er ook podotherapeuten die gecertificeerde zolen mogen maken voor in de veiligheidsschoenen, maar je kunt dus niet naar elke willekeurige leverancier wat betreft veiligheidszolen.
[mrbbn9i] (score 1, diepte 4) Aha, ik heb zelf geen ervaring met echt werkschoenen maar sinds ik steunzolen heb van de podotherapeut weet ik wel dat het echt heel belangrijk is dat een schoen echt goed zit en voldoende steun geeft. Ik lette er altijd wel op maar nu ben ik dus nog kieskeuriger geworden omdat ik niet weer voetproblemen wil. Niet dat dat kwam door slecht schoeisel maar in de zomer merk ik soms wel dat ik weer even schoenen aan moet in plaats van sandalen.
[mre4nmn] (score 1, diepte 3) Niet automatisch helaas. Steunzolen worden gecertificeerd in combinatie met de specifieke schoen waarvoor deze geleverd wordt. De fabrikant van de veiligheidsschoen registreert welke zolen bij hun schoenen zijn goedgekeurd. Je moet altijd dit register raadplegen voordat je steunzolen aanschaft voor je werkschoenen, en voor de zekerheid zou ik het altijd voorleggen aan je KAM/preventiemedewerker, zodat je schriftelijke goedkeuring vanuit je eigen organisatie hebt. 

Als je zelf een niet-goedgekeurde steunzool in je werkschoenen plaatst, dan is dit technisch gezien een ongeautoriseerde aanpassing van een PBM (persoonlijk berschermingsmiddel), waarmee de beschermingsgarantie van de PBM komt te vervallen. Bedrijven kunnen hier *bijzonder* moeilijk over doen, zeker wanneer er uiteindelijk een ongeluk gebeurt waarbij de PBM betrokken was.
[mr8anmo] (score 1, diepte 1 OP) Wat ik doe zou jammergenoeg niet minder kunnen. Beste optie is om naar een andere functie op zoek te gaan. Steel blue schoenen zal ik onthouden, thx
[mr94xaz] (score 1, diepte 1) OP werkt in een magazijn, dan zijn veiligheidsschoenen verplicht
[mr8aqmz] (score 1, diepte 0) Misschien toch maar naar de bedrijfsarts. Het kan zo zijn dat jij eigenlijk ongeschikt bent voor dit werk. Misschien dat ze je kunnen helpen door een andere functie aan te bieden.
[mr8cly9] (score 1, diepte 0) Voor mij hielpen blarenpleisters van de kruidvat. Maar ik moet eerlijk zijn, ik loop niet zoveel als jij
[mr8f4z0] (score 1, diepte 0) Ga praten op je werk. Als je niet kan staan, kun je ook niet werken, en moet je je arbeidsongeschikt (ziek) melden.  Dat is duurder dan andere schoenen voor je kopen. 

Tegelijkertijd: Kijk wat je zelf kunt doen. 

Dingen als: [https://www.huis-en-comfort.nl/p/teensokjes-per-paar-410832/](https://www.huis-en-comfort.nl/p/teensokjes-per-paar-410832/) en 

[https://injinji.nl/injinji-socks-linercombi-s/liner-crew-gray/18571-155#/130-maat\_injinji\_-xl](https://injinji.nl/injinji-socks-linercombi-s/liner-crew-gray/18571-155#/130-maat_injinji_-xl)

kunnen ontzettend helpen en kosten heel wat minder dan nieuwe schoenen. Waarschijnlijk krijg je na verloop van tijd eelt op je voeten, en ga je minder last hebben.
[mr8pkwg] (score 1, diepte 1) Akkoord met die teensokken. Doen veel voor blaren (afhankelijk van de plaats).
[mr8fsz5] (score 1, diepte 0) Ik werkte 3 jaar in de horeca en kreeg dat toen specifiek onder mijn rechter voet er kwam een moment dat ik dat eelt thuis gewoon zelf weg kon snijden zo dik was het maar het hielp natuurlijk niet helemaal omdat ik de volgende dag toch weer op mijn voeten moest staan al die uren.... ik kreeg ook last van mijn knieën toen heb ik schoenen gekocht van het merk "skechers" ook heb ik toen zolen laten aanmeten en die erin gezet en heb er nooit meer last van gehad.... moet wel zeggen dat het in 2018 was ik heb nu een hele andere baan..
[mrn9euw] (score 1, diepte 1 OP) 14.000?? Daar doe ik een moord voor. Ik heb geprobeert het te verminderen, langer even stilstaan of ff ergens snel zitten. Maar het gaat maar niet onder de 40k. Vorige week zelfs mijn record aangetikt, 52k stappen...
[mr8t2kr] (score 1, diepte 0) Koop goede schoenen, en een klein stepje.
[mr912jd] (score 1, diepte 0) Als ze blijven goedkope schoenen geven kan je vaker op ziekteverlof
[mr9m13s] (score 1, diepte 0) Ik heb vroeger in de evenementen gewerkt, en de beste schoenen voor hele dagen lopen zijn de meindll airstream. Zijn schoenen die ook in de bosbouw gebruikt worden. 

Zijn duur, rond de 300€ maar zijn echt de beste schoenen. Mijn langste werkdag was toen der tijd 40uur achter elkaar, heel verhaal met een aflosploeg die nooit kwam. Maar geen nergens last van, en zelf heb ik platvoeten en doorgezakte enkels. Dus ook niet het beste onderstel.
[mr9zhkr] (score 1, diepte 0) Jij hebt andere werkschoenen nodig. Goede werkschoenen kosten geen vermogen. Ik zou het zeker aankaarten. Uitval door slechte werkschoenen is veel kostbaarder dan een paar goed passende schoenen.
[mra0bb2] (score 1, diepte 0) Andere schoenen. Vaak krijg je de goedkoopste optie. 

Val vragen naar een podoloog op werk zijn kosten. 35km per dag is niet niks. En neem 2 paar schoenen voor het afwisselen. Schoenen drogen niet binnen een nacht. En goede sokken helpt ook. Desnoods wissel je nog in de pauze.
[mra23u0] (score 1, diepte 0) Wat je nog zou kunnen proberen is andere sokken. Bijvoorbeeld van die 'friction free' hardloop- of wandelsokken.
[mrd6ric] (score 1, diepte 0) Wow 40-45k?!!?!
[mrdqgf2] (score 1, diepte 0) Je hebt ook lichte sneaker stalen neuzen. Je werkgever is verplicht deze voor je te regelen als je voeten last hebben van die zware schoenen. Gewoon aangeven dus.
[mre3swk] (score 1, diepte 0) Zoals al aangegeven inderdaad met de KAM/preventiemedewerker, HR medewerker of bedrijfsarts in gesprek gaan. Als het aan de schoenen ligt, zijn het gewoon ondeugdelijke persoonlijke beschermingsmiddelen en de werkgever is verplicht om deze dan op kosten van de zaak te vervangen. Eventueel ook vragen naar een PMO (Preventief Medisch Onderzoek) waarbij wordt gekeken naar je fysieke gesteldheid en welke maatregelen genomen kunnen worden. Misschien komt hieruit dat je ongeschikt bent voor het lange lopen en daardoor niet langer binnen je positie past, maar dat is een heel stuk beter dan nu je voeten helemaal kapot lopen en daar later last van krijgen. 

Heb je de inlegzolen zelf aangeschaft/geplaatst? Hou er rekening mee dat in veel gevallen de beschermingsgarantie van je werkschoenen komt te vervallen wanneer je ze zelf aanpast, en dat je hier, mocht er ooit iets gebeuren, nog best wel eens last van kunt gaan krijgen wat betreft aansprakelijkheid en risico. Bij het aanpassen van persoonlijke beschermingsmiddelen moet je altijd overleggen met de KAM/preventiemedewerker. 

Bron: Ik neem tijdelijk de KAM/preventie afdeling bij een technisch installatiebedrijf waar, en heb de afgelopen maanden niets anders gelezen dan veiligheidsvoorschriften, reguleringen en preventiemaatregelen :)
[mrjn23o] (score 1, diepte 0) Je kan de stappenteller gebruiken als bewijs  en naar de vakbond of bedrijfsarts gaan

Dagelijks 30.km stappen met werkschoenen is echt niet meer van deze tijd, das 150km per week, jezus

En dan zeggen dat iedereen overgewicht heeft door de luie kantoorjobs

Als je bv 3 u per dag in een andere afdeling of werk met een BT of transpalet mag doen, kan het al een heel stuk beter gaan.

Ik vermoed dat je een collie_ controller bent, die de hele dag de staat/ nummers/ bestemming controlleert op genummerde transpaletten,
 in een magazijn met 20 rayons en 50 paletnummers per rayon

Eer je klaar bent met de 1000 palletten, zijn de eerste alweer in de camion geladen en kan je opnieuw beginnen aan je marathon

Dat is een job die nooit stopt, tenzij je aangeeft dat het teveel is..
[mrn8qee] (score 1, diepte 1 OP) Zoiets ja. Het is echt non stop en zitten heb je ook weinig tijd voor.
[mr850ne] (score 0, diepte 2) Nee, daar heb je zeker gelijk in. Vooral als je zoveel kilometers maakt. Maar het valt op zijn minst te proberen, zelf schoenen aanschaffen kan flink aantikken. Al zou ik zelf wel voor die optie kiezen. Alle wat je van de grond houdt moet je goed in investeren. Dat zijn schoenen, bed en stoel waar je dagelijks in zit
[mr85xjh] (score 0, diepte 0) Medische klompen! Of bijv sketchers. Ik loop rond de 10-20 k stappen per dag en deze schoenen maken het verschil.
[mr9ifmg] (score 0, diepte 0) Effe klikken op Temu!!

8D of 9D Insoles of net hoeveel dimensies ze deze keer ontdekt hebben..

Kosten een paar euries en tis alsof je met sokken op dikke vloerbedekking loopt.

Ziet er heel bobbelig uit met lichtgroene bovenkant.

Ik doe beveiliging en zit in 9 uur ook tussen de 30-40k stappen.

Bestel een paar en je voelt gelijk dat je er meer had moeten bestellen😂
(1 reacties met lagere score weggelaten)

=== THREAD 1bmljiw ===
SUBREDDIT: r/nederlands
DATUM: 2024-03-24  SCORE: 24  REACTIES: 65
TITEL: "Dit bouwwerk is handig tegen natte voeten", raadsel van dochter waar ik niet uit kom! Help
POST (source_id=post):
Mijn dochter heeft huiswerk gekregen en een van raadsels gaat hierover en ik kan echt niks er op bedenken

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kwc9kuf] (score 130, diepte 0) Ik neem aan dat het over dijken gaat.
[kwcajn7] (score 41, diepte 0) Is er enige vorm van context? Zoals wat voor vak? 

In het algemeen lijkt dit inderdaad over dijken te gaan.
[kwcbdh4] (score 32, diepte 1 OP) Vak is aardrijkskunde. Ik denk dat het inderdaad ook over dijken gaat.
[kwcb6sn] (score 29, diepte 0) Een brug
[kwcc8cb] (score 27, diepte 1) Een dam.
[kwcd3rq] (score 21, diepte 0) Badmeesterstoel
[kwcb14x] (score 15, diepte 1) Of een terp?
[kwces8b] (score 10, diepte 0) Dijk, dam, terp, Deltawerken
[kwd10g9] (score 7, diepte 2) Een dam, een dijk een kwelder, een uiterwaarde
[kwddb5d] (score 7, diepte 2) Of een gemaal
[kwf7npb] (score 7, diepte 3) Of een bergbezinkbassin of een overstort of een drainagebuis / drainageriool, of een DT riool of een DIT riool, zonder context van de vraag kunnen we zo nog wel even doorgaan haha
[kwccal4] (score 7, diepte 0) Een dam! Ik ken deze
[kwcf5la] (score 6, diepte 0) Ik gok dat dit in het kader is van 'grey of the day'. Concept dat is overgewaaid uit Scandinavië. Idee hiervan is om samen erover te brainstormen en met de juiste redenatie is geen enkel antwoord fout, dus dat scheelt 😉

Ik gok op de deltawerken!
[kwdl43n] (score 4, diepte 3) ….snap je wel het principe van een raadsel?
[kwcb3b9] (score 4, diepte 0) Huis op palen? Dijk? Gemaal? Stuwdam?
[kwdg9ua] (score 3, diepte 3) Een kwelder helpt niet tegen natte voeten. En ik weet ook niet of ik het een bouwwerk zou noemen.
[kwdfuau] (score 3, diepte 2) Ik ook maar wat een belachelijke omschrijving.

Zeg dan gewoon "dit bouwwerk houdt water weg van droge grond".

Ik had "boot" gezegd. Ga je dat fout rekenen?
[kwcc1lj] (score 3, diepte 0) De Deltawerken? Gemalen? Waterkeringen? 

Een steiger?
[kwcium1] (score 3, diepte 0) Brug, zodat je niet door het water hoeft te lopen.
[kwcz98w] (score 3, diepte 0) Laarzen.
[kwcb2a5] (score 2, diepte 0) Of een boot?
[kwccgxt] (score 2, diepte 1) Een dam heeft water aan beide kanten, een dijk is tussen land en water, dus denk dat ze dijk bedoelen aangezien je met een dam nog steeds natte voeten zou hebben.
[kwcfyd5] (score 2, diepte 1) Huehuehue goeie Herman
[kwcgrqt] (score 2, diepte 0) Een gemaal, pompt het water uit de polders.
[kwck5o8] (score 2, diepte 0) De deltawerken?
[kwcknxx] (score 2, diepte 0) De deltawerken
[kwcnfrl] (score 2, diepte 0) Guillotine denk ik
[kwcsagz] (score 2, diepte 0) Dijk
[kwcti0j] (score 2, diepte 0) Gemaal?
[kwcxsdn] (score 2, diepte 0) Stormvloedkering
[kwg7ttj] (score 2, diepte 0) Een boot
[kwcb37f] (score 1, diepte 0) Dam?
[kwcc9rt] (score 1, diepte 1) Nee, het is inderdaad een dam
[kwcqaet] (score 1, diepte 1) Mijn idee ook
[kwcbzu9] (score 1, diepte 0) Oosterscheldekering
[kwccsuo] (score 1, diepte 0) (35M) Deltawerken , dammen , stuwwen , dijken . een vlot ?
[kwdfy93] (score 1, diepte 1) Duikersklok.
[kwcd505] (score 1, diepte 0) Laat haar eigen fantasie op dit raadsel los.
[kwcds7x] (score 1, diepte 0) Een vlonderpad, uiteraard.
[kwchwv1] (score 1, diepte 0) Het hoofdkantoor van het plaatselijk waterschap, een steltenfabriek, dit kan letterlijk alles zijn.
[kwcp2h8] (score 1, diepte 0) een houten kap - laars
[kwcpu2l] (score 1, diepte 0) Een toren?
[kwcri5j] (score 1, diepte 0) Een wierde (wat die rare friesen terp noemen)
[kwcx7if] (score 1, diepte 0) Een guillotine voor voeten misschien?
[kwd3bfi] (score 1, diepte 0) Ik gok een trebuchet, zet er €500 op. Hobbymatig, dat wel
[kwd3kyy] (score 1, diepte 0) Woonboot
[kwd6xou] (score 1, diepte 0) Een steltenfabriek.
[kwd7svf] (score 1, diepte 0) Brug ?
[kwd955m] (score 1, diepte 0) Een brug helpt ook tegen natte voeten… geen brug…. plons
[kwdajif] (score 1, diepte 0) Deltawerken
[kwdfg9f] (score 1, diepte 0) Een crematorium?
[kwdivqc] (score 1, diepte 0) Een droogtoren
[kwdpe6l] (score 1, diepte 0) Wait. Molens zorgen voor laag grondwaterpeil. Dat moet hem zijn toch?
[kwdsfmo] (score 1, diepte 0) Een terp. Een toren. Een kolonie op mars. Een hele grote laser die alles bevriest. Een boot. Een luchtballon.
[kwdt6yj] (score 1, diepte 0) A-frame? 🤨
[kwdvpj5] (score 1, diepte 0) Aquaduct
[kwdwidd] (score 1, diepte 0) Deltawerken. Dit raadsel komt uit grej of the day. 

Bron: ik heb deze les gegeven aan mijn groep
[kwdxcja] (score 1, diepte 0) Dijken? Maar ik ben een aantal comments te laat zie ik
[kwdzqse] (score 1, diepte 0) Een terp.
[kwe4mga] (score 1, diepte 0) Ah de Grej of the Day. 

Dit moet wel een brug zijn. Dijk is te lastig om als ‘bouwwerk’ gezien te worden. Maar waarschijnlijk niet verkeerd met de juiste onderbouwing (woordgrap). 

Mijn zoon had onlangs Bertha 12. En omdat ik dacht dat een koe te simpel was, zijn we het internet op gegaan. Daar kwamen we er achter dat Dikke Bertha een kanon van de duisters was. Die was op 12 km te horen. Ook waren er nog eens 11 kopieën van gemaakt, dus 12 stuks. 

Bleek het toch gewoon de koe te zijn. Maar hoewel de klas hem heel vreemd aan keek, kregen we complimenten voor het uitzoekwerk. Want dat is waar Grej of the Day over gaat.
[kwg5y48] (score 1, diepte 0) brug.
[kwg6wet] (score 1, diepte 0) De Euromast waarschijnlijk
[kwgygf9] (score 1, diepte 0) Een Terp
[kwh6j8h] (score 1, diepte 0) Een ***schoener*** is een langsgetuigd zeilschip met oorspronkelijk twee, maar later ook meer masten.
[kwccu9c] (score -2, diepte 0) Gewoon aan je vrouw overlaten. Vrouwen weten toch alles beter.
[kwdl7m1] (score -3, diepte 4) Het is alvast niet uit je nek lullen.

=== THREAD 1wt7a2n ===
SUBREDDIT: r/nederlands
DATUM: 2026-09-29  SCORE: 24  REACTIES: 65
TITEL: Natte voeten tijdens het fietsen, hoe voorkomen?
POST (source_id=post):
Hoi allemaal, ik denk dat veel mensen dit wel herkennen. De laatste tijd ben ik regelmatig natgeregend tijdens het fietsen hahah.  Inmiddels heb ik een lange regenponcho gekocht, waardoor mijn lichaam redelijk droog blijft, maar mijn voeten worden nog steeds zeiknat...

Ik fiets iedere dag naar mijn werk, dus regenbuien ontwijken is voor mij niet echt een optie. Daarom ben ik benieuwd, wat gebruiken jullie om je voeten droog te houden tijdens een flinke regenbui op de fiets?

Ik kwam ook deze waterdichte schoenhoezen van hema tegen. Op het eerste gezicht lijken ze me best handig, heeft iemand hier ervaring mee? er staan namelijk geen reviews. Alle tips zijn welkom! 😊

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[pcrm583] (score 20, diepte 0) Heb dit jaren gebruikt, wel ander merk. Met goede schoenen heb je gewoon droge voeten (gebruikt op 50 minuten fietsen).
[pcrlnf3] (score 11, diepte 0) Check mantel of 12gobiking voor overschoenen. Staan ook wel goede tussen.
[pcrnbu5] (score 9, diepte 2) Jammergenoeg zijn de meeste sneakers niet of nauwelijks waterdicht. 
Persoonlijk heb ik altijd hoge waterdichte schoenen aangedaan voor fietsten, dit in combinatie met een goede regenbroek hield mij droog tijdens mijn fietstochten
[pcrlvel] (score 6, diepte 0) Ik heb een regenbroek van Decathlon met schoenhoezen eraan vast. Ideaal:
https://www.decathlon.nl/p/regenbroek-100-met-geintegreerde-schoencovers-zwart/169380/c382m8402040
[pcrman3] (score 5, diepte 1) Deze heb ik ook is perfect
[pcroc1t] (score 4, diepte 2) Ik doe hem ook aan als ik het terras ga schoonspuiten met de hogedrukreiniger, die voetflappen zijn ideaal!
[pcrmuo5] (score 4, diepte 1 OP) bij mijn sneakers gaat het er altijd doorheen... alleen mijn dr martens houden mijn voeten droog
[pcrpo2t] (score 4, diepte 0) Koop fatsoenlijke schoenen lol
[pcrlrqv] (score 3, diepte 0) Ik heb een vergelijkbaar paar. In 3 jaar geen natte schoenen meer gehad, dus lekker kopen ;)
[pcrnl2i] (score 3, diepte 2) Niet moeilijker dan een regenbroek zonder hoezen, onderste stuk van de broek kun je openen, dat zit vast met klittenband. 
Alleen eerst even het elastieken bandje onder (of achter) je voet vandaan halen.
Aantrekken gaat heel makkelijk.
[pcrmdk0] (score 3, diepte 0) Ik heb die je noemt in je post van de hema en gebruik ze voor lange wandeltochten. Vind ze echt heel fijn. Door het zakje makkelijk op te bergen en ze drogen erg snel
[pcrmrjh] (score 3, diepte 0) Wist niet dat dit bestond. Zou wel chill zijn, makkelijk mee te nemen zo. Zelf fiets ik eig nooit in de regen...
[pcruru8] (score 3, diepte 0) 1. Over schoenen zijn genoemd. 
2. Waterdichte schoenen zijn een optie. 
3. Er bestaan ook waterdichte sokken; Sealskin. 
Maar van deze opties zou je bijna vooraf moeten weten dat het gaat regenen. 

Dit pakketje lijkt mooi in de fietstas te kunnen. 

Mijn oplossing is een tasje met slecht-weer kleding op het werk te leggen. Daarin: sokken, onderbroek, schoenen trainingsbroek en een tshirt / trui. 
Natregenen is veel minder erg als er warme droge sokken op je wachten.
[pcrly7k] (score 2, diepte 1 OP) Dank! heb je ervaring met een van die twee? werkt het fijn zo schoenhoes?
[pcro1ol] (score 2, diepte 2) +1 voor 12go fijne winkel!
[pcrltp4] (score 2, diepte 0) Goeie vraag en relevant nu het weer herfst is. Ik lees even mee want zoek ook een goeie oplossing hiervoor. Gister uit werk ook weer helemaal natgeregend :(
[pcroru5] (score 2, diepte 2) Zo een broek is eigenljk net zo lastig als een overschoen, het lastige zijn de schoenen/voeten. Heb ook deze broek van de Decathlon, hij kan onderin ver open dus de schoen kan er prima doorgeen. Als je geen last hebt van natte benen omdat de poncho dat droog houdt werken overschoenen ook. Had die eerst in combinatie met een regenbroek, maar toen dus deze 2-in-1 gekocht, sneller en makkelijker. De overschoen aan de broek maakt het wel dat hij als regenbroek behoorlijk waardeloos is voor wandelen omdat je de straps onder de schoenzool snel kapot loopt, zelfde geldt voor overschoenen, maar gewoon van en naar de fiets lopen is geen probleem.
[pcrrz1b] (score 2, diepte 2) Ze zijn wel ietsje dikker dan gewone sokken, maar ben zelf wel fan.
[pcrnsua] (score 2, diepte 2) Spatwater of lichte regen zijn sneakers voldoende, althans mijn ervaring. Met harde, constante regen gebruikte ik timberland schoenen. Vergelijkbaar met Dr. Martens.

Je hebt ook van die regenbroeken met schoenflap, die werkten ook prima voor de wat lichtere buien.
[pcrt40h] (score 2, diepte 2) Dan heb je laarzen van Hunter nodig.
[pcrn8yb] (score 2, diepte 1 OP) oh wat goed! dat zakje lijkt me inderdaad ook handig
[pcrmkqa] (score 2, diepte 0) Ik heb regenlaarzen gekocht. Dan moet ik wel kijken wanneer het gaat regenen. Maar in de winter draag ik ze zoiezo iedere dag.
[pcrmltu] (score 2, diepte 0) Timberlands
[pcrnpia] (score 2, diepte 0) Zijn echt top icm regenbroek. Wil je geen regenbroek, dan waterdichte schoenen
[pcrq3my] (score 2, diepte 1) Dit, niet altijd even charmant maar wel heel fijn
[pcrwbrc] (score 2, diepte 2 OP) Ja dit dus hahah
[pcrx3gt] (score 2, diepte 3) Ik denk dat ik eerst maar eens zulke schoenhoezen ga proberen.
[pctpyfz] (score 2, diepte 1) Als dagelijkse wandelschoenendrager: helemaal eens. Al snap ik de opmerkingen van de mensen die het niet acceptabel vinden op kantoor, ik wil dat we daar als samenleving vanaf komen tbh. Wat is er tegen om wandelschoenen aan te doen als het keihard regend? Maar ja ik ben wel biased. Ik durfde het vandaag zelfs onder korte broek met lelijke wandelsokken 😅
[pctqq3o] (score 2, diepte 2) Genoeg “wandelschoenen” die er gewoon redelijk uitzien, maar ik draag meestal m’n “echte” wandelschoenen met dikke wollen sokken ja.
[pctrg38] (score 2, diepte 3) Hahah same. Vandaag was dit de combo. Als ik nog meer schijt had gehad, had ik de sokken hoog opgetrokken, maar dat liet ik vandaag maar even ;). Overigens zou ik dit niet op kantoor doen, maar met een lange broek wel hoor.

https://preview.redd.it/6slm81kxrhsh1.jpeg?width=3055&format=pjpg&auto=webp&s=9610c3b085ce69226f8d3902587508301d39dbf3
[pctrp6x] (score 2, diepte 4) Ik heb dan wel grijze of rode sokken maar m’n schoenen lijken er sprekend op
[pcrrfkc] (score 2, diepte 0) Laarzen kopen.
[pcrs91x] (score 2, diepte 0) Nieuwe balenciaga schoenen? 😂
[pcs1f04] (score 2, diepte 0) Door zo te fietsen...?

In dit geval zou een dikfiets met gashandel wel handig zijn... (/s)

https://i.redd.it/eohduixiggsh1.gif
[pcs2khu] (score 2, diepte 1 OP) Deze houding neem ik altijd aan als ik door een waterplas moet fietsen
[pcv2wqy] (score 2, diepte 0) Ik heb die en ze zijn goed.
[pcrzhya] (score 1, diepte 2) Beide winkels wel vaak besteld, Maargoed ik mountainbike ook. Zelf heb ik geen overschoenen (meer geaccepteerd dat ik natte voeten krijg), maar mensen die ik ken zijn en ze hebben er wel happy mee. Let wel op de pasvorm. Niet alle overschoenen zijn voor dagelijks gebruik. Ze zullen wel beter aansluiten op je schoen dan die van de HEMA.
[pcro91z] (score 1, diepte 1) Je bedoelt overschoenen over fietsschoenen (atb & race)? Deze zijn ‘aero’, dus nauwsluitend, bovendien is een fietschoen ook heel rank. Voor woonwerk en normale schoenen ziet de hema oplossing er veel praktischer uit.
[pcrypm1] (score 1, diepte 2) Ze hebben ook overschoenen voor mensen die niet 0,1 watt willen besparen.
[pcrmx7t] (score 1, diepte 1 OP) jaloers hahah
[pcrmn7o] (score 1, diepte 1 OP) is dit makkelijk aan en uit te krijgen? vandaar dat ik een regenponcho had gehaald, omdat ik die broeken altijd zo vervelend vind haha
[pcrpeit] (score 1, diepte 1) deze doet het ook voor mij
[pcsj36c] (score 1, diepte 2) Hoe lang zijn jullie benen? Lijkt mij ook ideaal, maar ben bang dat met mijn 36" benen het kruis tussen m'n knieën zit.
[pctghxw] (score 1, diepte 3) 34" past prima ik denk 36 ook nog wel maar even uitproberen
[pcrlw04] (score 1, diepte 0) Je kan ook sealskinz sokken gebruiken, ben daar zelf best tevreden over.

Als je schoenen nat zijn dan is het ook niet zo vervelend om er weer in te stappen, en schoenen blijven maar droog tot aan de rand. Alles wat naar beneden loopt loopt zo nog je schoenen in.
[pcrn3tg] (score 1, diepte 1 OP) oh wow! nog nooit van gehoord
[pcrm2zm] (score 1, diepte 0) Door zo’n poncho worden je schoenen extra nat, omdat alles zo naar beneden glijdt.
[pcrnw9x] (score 1, diepte 0) ik gebruik sandalen zonder sokken
[pcrvhiw] (score 1, diepte 1) Maar ik trek geen wandelschoenen aan naar mijn werk. Moet ik aparte schoenen meenemen of daar laten, ook weer zo’n gedoe.
[pcrwq8z] (score 1, diepte 2) Er zijn genoeg wandelschoenen die prima geschikt zijn voor kantoor. Bijv Ecco heeft ook een hele lijn waterdichte nette schoenen
[pcts2vz] (score 1, diepte 5) Ah ja. Ik vind opvallende sokken ook wel weer grappig. Hou van Falke. Welke draag jij? Fijne schoenen he! Ik heb deze een maand geleden gekocht. Het wide model van de lowa renegades.
[pctzhhw] (score 1, diepte 6) https://preview.redd.it/n8fo0bvjxhsh1.jpeg?width=3024&format=pjpg&auto=webp&s=a5e570cc5859251031d31087bcd8378203c25f52

Hanwag? Met Falke wollen sokken hah
[pczhh4c] (score 1, diepte 7) Nice! En ja falke is the way to go haha
[pctzq7s] (score 1, diepte 6) https://preview.redd.it/7zya3s0rxhsh1.jpeg?width=3024&format=pjpg&auto=webp&s=687e34c0051e8463696c549845ea9a01281a5e5c

  
En m’n “nette” wandelschoenen- m’n Ecco’s
[pcrtbor] (score 1, diepte 0) Ik heb sinds vorige winter vans gore-tex sh8-hi's. Naast dat ze warm zijn, heb ik er in erg nat weer nog nooit natte voeten in gehad.
[pcrwnb1] (score 1, diepte 1 OP) Jaa, dan wel ook zo pakketje voor thuis. Als ik van thuis naar kantoor ga.
[pcsea0y] (score 1, diepte 0) Overschoenen zoals dit werken perfect daartegen. Ik zou je poncho ook inruilen voor een fatsoenlijk regenpak.
[pctm3i0] (score 1, diepte 0) Droge schoenen op je werk klaar hebben staan.
[pdee8s3] (score 1, diepte 0) ik draag meestal werkschoenen of kisten die waterafstotend zijn, en anders deed ik gaiters aan om sowieso vanaf de bovenkant geen water binnen te laten en ja soms gewoon een zak om mn voeten
[pdtqqxm] (score 1, diepte 0) Dit werk top ik doe dit al jaren met me werkschoenen/scouting schoenen
[pct21gk] (score 0, diepte 0) ![gif](giphy|8jd901IasZvEPQuj7W)
[pcrlrwg] (score -1, diepte 0) Ik gebruik de auto
[pcrmmmx] (score -3, diepte 0) Ik draag dit voor de ladies
[pcrm4xq] (score -4, diepte 0) …ik neem de auto…
[pcrmmbw] (score -4, diepte 0) Hometrainer aanschaffen
[pcrldjd] (score -5, diepte 0) https://preview.redd.it/n7shrz5c0gsh1.png?width=400&format=png&auto=webp&s=a62c9fd11f37871405396e1fdb82c5305e912a57

/s
[pcrlt2m] (score -5, diepte 0) Ik ga rijdend

