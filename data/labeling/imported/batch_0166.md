# Label-batch batch_0166

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
Schrijf het resultaat naar `batch_0166.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1w6jpnj, 1524tmv, 1f2d2ql).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1w6jpnj ===
SUBREDDIT: r/nederlands
DATUM: 2026-09-03  SCORE: 247  REACTIES: 144
TITEL: Blote voeten naast je hoofd tijdens de film
POST (source_id=post):
Ik ging het afgelopen weekend met mijn vriendin naar de bioscoop. In de rij achter ons zat een Tokkie die haar voeten, met tien centimeters dikke eeltlagen en zwarte voetzolen, op de stoel voor haar leunde. Ze wiebelde met die voeten, naast het hoofd van twee tienerjongens die daar zaten. Die twee gingen de hele tijd naar achteren kijken als stille hint, maar ze bleef het doen.

Wij zaten een paar stoelen verderop. Naast die Tokkie zat haar ogenschijnlijke Tokkievriend luid chips naar binnen te werken. Niet subtiel, maar echt vretend, smakkend en vingers aflikkend en afzuigend. Af en toe wreef hij het vet van zijn vingers af op zijn shirt. De hele film werd verstoord door zijn chipszakgeluid.

We gaan niet vaak naar de film, maar ik heb het gevoel dat dit soort dingen steeds meer de norm worden.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[p7njome] (score 301, diepte 0) In sommige bioscopen kan je een appje sturen naar t personeel over overlastgevende mensen, dat mag je in dit geval ook bestvoo imand anders doen
[p7nk8s6] (score 92, diepte 0) Gelukkig nooit meegemaakt maar in iedere bioscoop waar ik geweest ben laten voor de film zien naar welk nummer je smsen voor als er overlast is. Gewoon doen. De bioscoop wil ook dat je een leuke ervaring hebt.
[p7njec5] (score 63, diepte 0) Ik ga regelmatig naar de bios, ik maak dit eigenlijk nooit mee.
[p7njeyk] (score 60, diepte 0) Helaas krijgt niet iedereen in zijn opvoeding mee om rekening met anderen houden. 
En ja, ik heb ook het idee dat het alleen maar erger wordt.  En er iets van zeggen? Durf jij het?
[p7nzjf1] (score 54, diepte 2) Een keer een groep tieners uit de zaal gekregen door simpelweg een berichtje te sturen. Immers ook maar een keer gedaan maar het werkte wel.
[p7njqiu] (score 51, diepte 1 OP) Volgens mij komen er dan zwavelzuurdampen vrij.
[p7nlenx] (score 42, diepte 1) Ik ga nooit naar de bios en maak dit ook eigenlijk nooit mee
[p7njeel] (score 41, diepte 0) Aansteker onder die eeltlaag
[p7nj3n5] (score 40, diepte 0) Lijfstraffen zijn helaas verboden
[p7nlf1g] (score 34, diepte 1) Ben al even niet naar de film geweest maar dat tegenwoordig al een nummer vooraf de film verschijnt om dit soort dingen te kunnen melden zegt mij alweer genoeg
[p7nlqbb] (score 30, diepte 2) Ik maak nooit iets mee.
[p7njx3a] (score 27, diepte 1) Ja het lastige is dat de mensen die dit doen zo asociaal zijn dat het niet gaat stoppen wanneer je er iets van zegt. Beter dus meteen bij de bios melden zodat ze eruit gekickt worden
[p7nkgmf] (score 26, diepte 2) Daar zou ik ook voor kiezen.  Maar dan komt de reddit politie: waarom ga je het gesprek niet aan?  ... nou, omdat het onmogelijk is te redeneren met onredelijke mensen. 

Als alternatief stel ik voor: ouderwets hoedje met veren dragen   😉
[p7nxh8t] (score 26, diepte 1) https://preview.redd.it/ca1h4iwhndnh1.jpeg?width=1080&format=pjpg&auto=webp&s=f3f199c8dd45d66c6a6b250c6eccfd62981ffceb
[p7pwzu4] (score 24, diepte 2) Dit is iets van alle (bioscoop)tijden. Tis alleen tot 'recent' niet mogelijk om een snel appje te sturen voor dit soort zaken.
[p7nmr07] (score 20, diepte 0) ![gif](giphy|26xByFvrI1MQvtlDO)
[p7nnte5] (score 19, diepte 3) Ik vind dit soort dingen grappig. Ik vind het zelfs grappig dat jij je hier aan stoort en dat hier post.
[p7qf2ru] (score 16, diepte 3) Toen moest je even faxen naar de bioscoop
[p7qu0dp] (score 15, diepte 3) Ja same. Luidruchtige tieners die met popcorn gooiden. Zijn er mooi uitgezet. 
Bioscopen moeten dit ook wel doen, anders komen mensen niet meer.
[p7nnt3i] (score 12, diepte 3) Ik wel. Maar dit nooit
[p7nl5w2] (score 12, diepte 2) Of in het geval van tokkies gaan ze 10x erger door
[p7nknti] (score 11, diepte 0) Ik herken dit gedrag ja. Afgelopen dinsdag ook naar de film geweest en in mijn ervaring doet vooral de jeugd dit, tieners. Zo zat er een groepje met de schoenen uit ook met de sokjes op de hoofdsteun voor hen. 

Dito eetgeluiden en geslurp. Ook ligt standaard de telefoon op schoot zodat ze zo nu en dan even Snapchat kunnen checken. 

Zo zie ik elke keer dat ik ga wel dergelijke dingen. Het is inmiddels gewoon het nieuwe normaal denk ik. Het beïnvloedt wel het kijkplezier.
[p7nl45x] (score 10, diepte 1) Opvoeding 🚫  
Voeding 👍🏻
[p7nm4bp] (score 9, diepte 2) Dan zijn ze ook verantwoordelijk voor roken in de bioscoopzaal. Als je die regel overtreedt dan wordt je subiet uit de bioscoop verwijderd.
[p7s4v4b] (score 9, diepte 4) Wij ook een keer, tieners rende onder en tegen het doek aan. Blijkbaar zit er een stuk ruimte achter het doek en de muur. Ze vonden zichzelf hilarisch, wij net wat minder. Toen gooide ze popcorn de zaal in. 

Wij geappt, Vue personeel kwam binnen maar toen gingen ze snel zitten natuurlijk. Blijkt die man om het hoekje gewacht te hebben en heeft hij ze alsnog betrapt. Heel die situatie was leuker dan de film uiteindelijk.
[p7q6d9y] (score 9, diepte 2) Was 20 jaar geleden ook al zo?
[p7nkwox] (score 9, diepte 0) In de collegezaal laatst had ik een voetje in mijn kont soms. Pakte zo haar voet beet en ze schrok haha
[p7nk6t4] (score 8, diepte 1 OP) Mensen worden steeds gekker. Voor een kleine opmerking krijg je plotseling een schroevendraaier tussen je ribben.
[p7qn9i0] (score 8, diepte 4) ik nam altijd m'n postduif mee naar de cinema
[p7qnco4] (score 8, diepte 5) Rooksignalen werd vroeger nooit echt gewaardeerd in de bios
[p7pnfb6] (score 8, diepte 0) Gewoon een ander soort films gaan kijken. In filmhuizen zul je ze niet tegen komen.
[p7q2he4] (score 8, diepte 0) Op radio 2 vertelde een dj exact hetzelfde verhaal deze ochtend.
[p7nn9l0] (score 7, diepte 3) Chill maat, is een grapje
[p7odnzs] (score 7, diepte 1) Ja, ik durf dat wel in de meeste gevallen.  Dit is de enige reden waarom dit gedrag blijft bestaan en erger te worden. Omdat mensen te laf zijn om er iets aan te doen. En zelf te laf zijn om mensen die wel opstaan bijval te geven.   
  
Dit is echt de enige oplossing.  Een reddit post achteraf helpt namelijk helemaal niets.
[p7nluyf] (score 7, diepte 0) Zuig aan haar eeltteen, dan trekt ze haar voet vast weg.
[p7nyrov] (score 7, diepte 1) Kots in mijn mond door deze opmerking
[p7noh9r] (score 6, diepte 1) Dat was voor die tokkie dus niet duidelijk.
[p7nuqw9] (score 6, diepte 0) zo erg heb ik het zelf nog nooit gehad, maar mensen worden wel steeds asocialer ja.

daarentegen wil ik wel zeggen dat je prima iemand op z’n gedrag kan wijzen in de bioscoop ofwel personeel er bij halen. is 50/50 of het werkt om er zelf iets van te zeggen, maar als iemand het heel bont maakt is het gewoon een taak van het personeel daar om je bij te springen.
[p7oiu4c] (score 5, diepte 1) Is kietelen een lijfstraf?
[p7nupi9] (score 5, diepte 4) Ga eens naar de bios
[p7oe0pf] (score 5, diepte 2) Als je het tegen wil gaan zul je je zelf toch over dit soort bangerigheid heen moeten zetten.
[p7nmdzd] (score 5, diepte 2) ze gaan prima op voeding
[p7nmspe] (score 5, diepte 0) Dit is niet de norm.
[p7nniv4] (score 5, diepte 0) Amsterdam Pathé zeker? Ik ken het. Regelmatig onbeschoft publiek.
[p7npmsq] (score 5, diepte 0) in welke plaats was dit? gewoon nieuwsgierig.
[p7nyblq] (score 5, diepte 0) Bioscoop is leuk tijdens de ochtend en middag voorstellingen.
[p7qn0pe] (score 4, diepte 3) Als ik een man van aardig postuur was zou ik het wel durven. Maar als kleine vrouw meestal niet. Soms doe ik het alsnog omdat het me zo irriteert op dat moment, maar dat is dan vrij impulsief. Ik word liever niet in elkaar gemept of gestoken omdat ik zo nodig ergens wat van moest zeggen. En je weet helaas niet hoe de ander gaat reageren, zeker als het al een tokkie is. Het minste geringste kan agressie uitlokken bij domme asociale mensen.
[p7njtil] (score 4, diepte 0) Het enige wat ik doe is een gat onderin mijn popcorn bak maken, iets er doorheen steken en dan mijn vrouw wat popcorn aanbieden.
[p7no1vb] (score 4, diepte 1) Zoete of zoute popcorn?
[p7qipkd] (score 4, diepte 4) Overlast is van alle tijden. 35 jaar geleden had je ook overlast van irritante pubers.   
Alleen loste je dat vaker zelf op door een paar keer te waarschuwen en uiteindelijk een fles tegen de luidste te keilen
[p7o21k7] (score 4, diepte 2) 7.2.2 opstelling icm

Tv: LG G5 77 inch   
Surroundreciever: Marantz Cinema 40  
Eindversterker : NAD C298  
Blurayspeler: Panasonic UB9001  
Front speakers: B&W 702 s2  
Center: HTM71 s3  
Subwoofer: DB4S  
B&W Atmos : CCM683
[p7ojz66] (score 4, diepte 0) Ga naar het Filmhuis.Het publiek daar heeft tenminste enige opvoeding genoten.
[p7noarw] (score 3, diepte 1) Ik ga ook regelmatig naar de bios maar kom het steeds vaker tegen helaas. Leeftijd maakt niet uit, mensen kunnen zich gewoon niet meer gedragen lijkt 't wel.
[p7qnd9f] (score 3, diepte 2) >(buiten de randstad)

Ding ding ding
[p7q7ps6] (score 3, diepte 3 OP) Ik ben niet bang hoor. Als iemand voor of achter mij zit, dan zeg ik er wat van. Als iemand luidruchtig vreet en lawaai maakt met een chipszak, aan de andere kant van de zaal, dan is het iemand die de kritiek wegwuift en doorgaat. Het heeft geen zin om daar helemaal naartoe te lopen. Het is daarentegen niet illegaal om eetgeluiden te maken. Het personeel zal niets doen, hooguit iets over die voeten zeggen.
[p7qdkkh] (score 3, diepte 3) Ik ben oud genoeg om 'vroeger' persoonlijk mee te hebben gemaakt. Natuurlijk werd er ook toen het een en ander uitgevreten. Maar het zo openlijk schijt aan alles en iedereen hebben is mijns inziens toch echt iets van deze tijd.
[p7oqq6j] (score 3, diepte 4) En vet op je shirt maakt het mooi waterdicht. Scheelt weer een regenjas.
[p7ose1z] (score 3, diepte 2) Dit gedrag bestaat omdat de persoon dat wil. Als je er iets van moet zeggen is het al te laat. Waarom zouden ze luisteren als ze voorheen ook al schijt hadden?
[p7o0gaz] (score 3, diepte 1) Opzich raar dat je gedownvote wordt. Ik heb gister ook een asociaal stelletje aangesproken op hun luidruchtig gedrag tijdens de eerste helft van de film. 2de helft van de film was het heel stil en kon gewoon genieten van de rest van de film. Met ook nog een goed gevoel er bij :)
[p7p3bhw] (score 3, diepte 2) Vind ik ook, maar het blijft reddit. Ik ga hier ook voor gedownvote worden, maar het gros is hier dusdanig introvert dat mensen aanspreken eng is. Zie meerdere quotes in dit topic.
[p7nw6wq] (score 3, diepte 1 OP) Doe je goed. Mag ik weten hoe dat is opgezet?
[p7o35t9] (score 3, diepte 3 OP) Mooi hoor. Respect voor de NAD-eindversterker en Bowers & Wilkins-speakers. Lekker grote tv ook.
[p7pz44z] (score 3, diepte 1) Nieuwsgierigegein.

Wow. Ik bedenk dit soort grapjes gewoon op de vroege morgen met pas 1 kop koffie op.
[p7oeyh0] (score 3, diepte 1) ik denk het popcorn kraam
[p7o1ds0] (score 3, diepte 0) Heb ib rdam pathé genoeg asociaal gedrag gezien. Macdobalds mee overal commentaar op hebben. Ga ook regelmatig naar lumiere in maastricht, kan je geen chips of popcorn halen. Wel lekkere cocktails
[p7o68bg] (score 3, diepte 0) Pathe zeker?
[p7odfph] (score 3, diepte 0) Bij pathe en vue kun je een sms je sturen. Wordt aan het begin getoont zelfs. Maar ik heb nu 3 jaar lang elke winter een abbonement gehad bij een bios op 5 min lopen. In die 3 jaar heb ik maar 1x een puber aangesproken omdat ze steeds op haar telefoon zat met helderheid op 100 miljoen.

Ik denk dat je gewoon een aso stel bent tegengekomen en dat dit niks te maken heeft met "tegenwoordig"
[p7q0m3q] (score 3, diepte 0) Ik heb dit zelf ooit gedaan bij een goeie vriend van me die voor mij in de bios zat met zijn date. De bios was verder leeg want de beste mam had zijn date meegenomen naar the Dictator op een doordeweekse dag en ik was daar met een andere goeie vriend van me. 

Mooiste was dat hij eerst niet door had dat ik het was en soort van boos werd. Toen hij erachter kwam dat ik het was vond hij het echt hilarisch gelukkig.
[p7qi189] (score 3, diepte 0) Zoiets als dit kan je melden als overlast.

Bij de meeste bioscopen (in ieder geval Pathé en Kinepolis) verschijnt voor aanvang van de film altijd een nummer waarnaar je een sms kunt sturen om overlast te melden. Dan komt een medewerker zo snel mogelijk er op af om het te verhelpen.
[p7qd1iw] (score 2, diepte 1) Een keer een lik aan die tenen mag wel. En dan zijn ze zo weg.
[p7shm7r] (score 2, diepte 2) ![gif](giphy|l9FAwJOXYprFe)
[p7qn93f] (score 2, diepte 4) Volgens mij is het ook erger geworden na corona. Isolatie heeft de mens asocialer gemaakt.
[p7s82hf] (score 2, diepte 5) Sinds het wc papier op was is het ikke ikke ikke geworden, tot dat moment waren we ook nog allemaal samen tegen corona...
[p7q98yf] (score 2, diepte 2) Echt Nederlanders worden zo laf opgevoed. Conflict altijd mijden, vechten altijd uit de weg gaan, nergens wat van zeggen. Kinderen leren geen discipline meer ook.
[p7te6lt] (score 2, diepte 1) Als je wat van dit soort aso gedrag zegt is er zo’n grote kans dat je allerlei gekanker en shit over je heen krijgt dat dat dus ook amper meer een goede optie is.
[p7qvkt0] (score 2, diepte 5) En niemand die het filmde.

Serieus, ben opgehouden met rottigheid uithalen toen een medestudent van de opleiding klaarstond om een rotgeintje (waarmee we de opleiding belachelijk zouden maken) uit te halen. Het was een leuk rotgeintje op dat moment, maar je wilt niet dat je jaren later nog teruggevonden kan worden.

Dat is er in de loop der jaren ook veranderd
[p7nyjpg] (score 2, diepte 1) Helaas nier het geval bij de bios bij mij in de buurt
[p7qp1gc] (score 2, diepte 1) Meegemaakt, 1x… Weekend van Barbie. Ik was naar een andere film, kwam een groep dronken vrouwen tegen het einde van de film binnen (want ja, Pathé mag je elke zaal zomaar inlopen). Er is geappt, er is twee keer een pikkie van 16 gekomen die er niets aan deed… Tot zo ver dus de hulp hierin
[p7qsuog] (score 2, diepte 1) Met je kringspier?
[p7pzyw0] (score 2, diepte 3) Als introvert zijnde vond ik die opmerking van waarom we ons mond niet opentrekken als volwassenen erg storend.

Maar ik heb er maar niks van gezegd.
(79 reacties met lagere score weggelaten)

=== THREAD 1524tmv ===
SUBREDDIT: r/nederlands
DATUM: 2023-07-17  SCORE: 34  REACTIES: 109
TITEL: blijven je voeten groeien tot je achttiende?
POST (source_id=post):
ik ben 16 jaar en heb al schoenmaat 48 en ik heb al behoorlijk moeite met schoenen vinden. dus ik hoop zelf dat ze nu al klaar zijn met groeien maar op internet staat dat voeten meestal stoppen met groeien als je achttien bent. dat zou dus dan betekenen dat mijn voeten nog 2 jaar groeien maar dat hoop ik zelf niet.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jsbuuap] (score 66, diepte 0) Het zal per persoon verschillen, lijkt me. Ik heb al sinds mijn 12e dezelfde schoenmaat. 🤷‍♀️ (En ja, ik had grote voeten voor een 12 jarige. Voor een volwassene is het gelukkig vrij normaal.)
[jscbd5e] (score 28, diepte 0) Je voeten blijven groeien tot de eerste keer dat zonder bescherming (sokken) voetje hebr gevreeën. Tot die tijd denken ze dat ze niet groot genoeg zijn🤷🏼‍♂️
[jsbv1nu] (score 24, diepte 0) Mijn voeten zijn door blijven groeien tot rond mn 18e ongeveer. Heb nu maat 46.
[jscy1yx] (score 23, diepte 7) Toevallig en per ongeluk is niet hetzelfde
[jsd4ngj] (score 21, diepte 9) Per ongeluk is bij definitie toevallig.

Toevallig is niet bij definitie per ongeluk.

Dat noemen we een 'hyperoniem'.

IK ben de wijsneus in dezen. Ja?! OK dan.

Dombo.
[jscapvm] (score 18, diepte 0) Ik heb zelf maat 50. 20 jaar geleden was je verketterd tot gare gymschoenen of ouwe lullen leren schoenen. Tegenwoordig is er extreem veel keuze en vergeet niet dat een maat 49 van merk 1 net zo groot is als maat 50 van merk b. Meindl heeft geweldige wandelschoenen en zalando heeft skateschoenen in jouw maat, daar kan je echt even mee door. No worries.
[jsbvype] (score 13, diepte 2) Niet veel kleiner dan 46. Ik denk rond de 44 of 45. Ik hoop voor je dat je voeten snel stoppen met groeien. Grote voeten kunnen echt vervelend zijn…
[jscar4v] (score 12, diepte 1) die van mij zijn ook gestopt rond 12, helaas zijn die van mij klein gebleven haha
[jsc2dph] (score 10, diepte 5 OP) ik ben precies 1,90 me vader heeft me toevallig vandaag gemeten.
[jsc1xk4] (score 9, diepte 4) Ik heb 47.5 / 48. Je vindt heel veel opties online maar in fysieke winkels kun je het op je ballen krassen. Hoe lang ben je? Mijn voeten stopten met groeien toen ik zelf uitgegroeid was rond de 1.94cm, denk 16/17 jaar
[jsbzkvo] (score 8, diepte 1 OP) je volgens de GGD en de dokters ben ik klaar met groeien maar elke keer als ik kom ben ik steeds een beetje gegroeid volgens hun hebben ze me “fout gemeten” kan net zo goed thuis dan meten vindt ik
[jsbwvv6] (score 7, diepte 3 OP) zeg dat ik bestel nu ook alleen online toen ik 47 had kon ik ze nog net in schoenen winkels vinden maar toen ik 48 had aangetikt is het een hele opdracht geworden om in gewone schoenenwinkels schoenen te vinden.
[jsc91xj] (score 6, diepte 4) Kan je misschien (met je ouders) langs de dokter gaan. Als het fysiek niet goed is lijkt me dat er daar gekeken moet worden met bv zooltjes oid. Ik ben 2m en heb gelukkig maar maat 44 maar ik ga wel schuin lopen.
[jsc5vf8] (score 6, diepte 4) Ja bizar dat dat zo verschilt. Ik schrok een beetje van het verschil toen ik voor het eerst in Limburg was. Ik voelde me echt een reus. Gelukkig kom ik hier in amsterdam met enige regelmaat mensen van rond mijn lengte tegen. Laatst iemand in bij de alberheijn van ik denk wel ruim 230! En ook super getraind. Ik voelde opeens wat anderen bij mij moeten voelen 😅
[jscbpra] (score 6, diepte 3 OP) ja oke dat kan maar uit alle respect het is niet zo dat ik voor altijd basketbal schoenen wil dragen ik draag ook slippers etc
[jsby7hh] (score 5, diepte 0) Mijn zoon had een verlate puberteit en dus ook pas heel laat de bekende groeispurt en was om die reden bij de kinderarts. Die vroeg of de voeten al uitgegroeid waren, omdat die kennelijk als eerste stoppen met groeien...
[jsbyr7e] (score 5, diepte 0) Je voeten stoppen als een van je eerste lichaamsdelen stoppen met groeien, heb ik mij laten vertellen door een dokter (ben zelf ruim 2 meter). Na je 16de is de groei er wel uit, kan misschien nog een (half) maatje groter worden
[jsbvgdj] (score 4, diepte 0) Nou, volgens [deze](https://rondompodotherapeuten.nl/wiki/kind-de-groei) podotherapeuten stoppen ze bij jongens met groeien rond de 14/15 jaar. Dat biedt nog hoop!

"Bij meisjes groeien de voeten vanaf hun 12e levensjaar minder snel. Tussen hun 12e en 13e levensjaar stoppen ze met groeien. Voor jongens stopt het ongeveer twee jaar later, dus tussen de 14 en 15 jaar. De voet is het eerste lichaamsdeel van een kind wat volgroeit is."
[jsc5ld5] (score 4, diepte 0) Knip gewoon je tenen eraf. /S

Hoe lang ben je dan?
[jsd2nyz] (score 4, diepte 1) klopt als een bus.

met mn maatje 49 had ik vroeger (jaren 80-90) heel veel last om goede schoenen te vinden. Vandaag de dag geen probleem.
[jse4u48] (score 4, diepte 1) Wacht en merk a en 2 dan
[jscb0i1] (score 4, diepte 0) ik ben op mn 16de van 42 naar 48 ½ gegaan tot mn 20ste
[jsbvoav] (score 3, diepte 1 OP) weet je toevallig ook ongeveer welke maat je op je zestiende had?
[jscq9a7] (score 3, diepte 4) Probleem is gewoon dat het voor gewone schoenenwinkels niet interessant is om grote (en tevens kleine) aan te schaffen omdat er gewoon simpelweg niet genoeg mensen zijn die die maat hebben. 

Als ze dan van een deel van het assortiment alle maten moeten kopen, waarvan ze dan 80%+ weg kunnen gooien omdat er niemand in hun winkel komt die die maat heeft, dan is dat gewoon weggegooid geld voor die onderneming (zeker als de nieuwe collectie)  

Online is dat natuurlijk wat makkelijker omdat je dan een groter publiek hebt en een collectie eventueel nog langer kan gebruiken
[jsdin5v] (score 3, diepte 1) Mijne ook. Bepaalde merken maat 46, sommige merken 47,5. Het verschilt echt enorm per merk schoen.
[jsbw201] (score 3, diepte 1 OP) ik ben 16 en ben in een half jaar tijd van 47 naar 48 gegaan
[jsd7qxb] (score 3, diepte 1) Wat is jouw probleem?
[jsexmu6] (score 2, diepte 2) Dat scheelt weer in de kosten
[jsfkznq] (score 2, diepte 2) Kun je wel makkelijker schoenen vinden tho! Alles is altijd uitverkocht of niet beschikbaar in maat 40-43, maar maat 34-39 is er vrijwel altijd nog🙏
[jsg0xlg] (score 2, diepte 4) Misschien een optie om in de vrouwensectie te kijken. Ik koop ook regelmatig mannenschoenen omdat het aanbod in maat 43 daar groter is, en 7 van de 10 keer kunnen schoenen prima door voor unisex! 👍
[jscqtoe] (score 2, diepte 5 OP) precies.
[jsbwo9b] (score 2, diepte 2) Je moet podotherapeuten ook nooit zomaar vertrouwen. /s

Uitzonderingen op de regel zijn er altijd, jij dus blijkbaar ook.
[jsc8i89] (score 2, diepte 2) Is het fysiek ook ongemakkelijk?
[jsc8ocy] (score 2, diepte 3 OP) ja krijg snel pijn aan me benen als ik wat langer loop
[jsc9bvy] (score 2, diepte 5 OP) ik loop toevallig ook schuin
[jsbzu8t] (score 2, diepte 0) Mijn voeten stopte van de één op de andere dag met groeien. Op mn 14de maatje 46 op de groei gekocht. Uiteindelijk zijn ze blijven steken op 45, heb dat dus al sinds mn 13/14e. Ben in de lengte daarna nog wel bijna 10cm gegroeid.
[jsc0ehq] (score 2, diepte 1 OP) ik ben 1,90 me vader heeft me toevallig vandaag gemeten in de lengte zou ik het niet zo erg vinden als er iets bij komt denk ook niet meer zo veel ik hoop wel dat mijn voeten nu gestopt zijn met groeien
[jscs0hc] (score 2, diepte 1 OP) zooo hopelijk krijg ik dat niet zit ik dan met maat 55 hahaha
[jsdutv3] (score 2, diepte 2 OP) och ja je hebt altijd van zulke mensen op het internet zou er geen aandacht aan geven wordt die opgewonden van.
[jscep1v] (score 2, diepte 0) Die van mij zijn rond mijn 16e op 46 blijven steken. Er is hoop!
[jscqpxk] (score 2, diepte 0) Ik heb 46/47 en sinds de laatste paar jaar is het goed te doen om schoenen te vinden. Ongeveer 15 jaar geleden moest ik altijd genoegen nemen met welke schoen er dan ook maar in mijn maat te vinden was. Tegenwoordig is de keuze een stuk groter, maar ik ben alsnog beter af door mijn schoenen online te bestellen. Ook al zie je tegenwoordig zelfs in steeds meer winkels sokken voor maat 47-50.

Als deze trend zich doorzet zal het voor jou ook steeds makkelijker worden. 

Ik weet niet meer sinds welke leeftijd ik op deze schoenmaat zit. Het schijnt wel zo te zijn dat je voeten op late leeftijd nog 1 of 2 maten groter worden doordat ze 'inzakken'. Dit kan ook ofwel een fabel zijn, of het gevolg van een leven lang geen ondersteunende schoenen te hebben gedragen.
[jshbha9] (score 2, diepte 3 OP) ik ben wel lang maar niet “ongewoon” lang 1,90
[jsdegys] (score 2, diepte 0) Wel een zegen als je nieuwe Nike schoenen wil kopen, als er nieuwe jordans uitkomen zijn alle "normale" maten op de site uitverkocht maar de hele grote en hele kleine maten niet.
[jsfn26f] (score 1, diepte 3) Mijn vader heeft maat 38-39. Hij kan geen normale leren schoenen vinden.
[jsd3btb] (score 1, diepte 5) Behalve dan dat er voor kleine maten altijd nog de jeugd en de rest van de wereld is.
[jsf31zu] (score 1, diepte 4) Ik heb ook 48 en ik heb geen enkel problem om schoenen te vinden. Dat was toen ik 18 was ( 33 jaar geleden) wel anders. Ik loop zelf op Asics hardloopschoenen voor mijn werk, Vans & Asics vrije tijd. Mijn jongere broer heeft 49 en ook hem lukt het om schoenen te vinden. 

Nette schoenen, kisten etc ook allemaal geen probleem.
[jsfni78] (score 1, diepte 4) Legerkisten hebben ze tot maat 50. Veel verschillende modellen ook. Ik loop al jaren met veel plezier op kisten, ze gaan ook veel langer mee dan de meeste schoenen.
[jsffyn9] (score 1, diepte 1) Volgens die, volgens hem, volgens haar, volgens de dokter..... je voeten stoppen pas met groeien als de tijd is gekomen, dit kan per persoon verschillen en is puur genetisch bepaald.
[jsk0hyx] (score 1, diepte 2) Nee hoor, ik heb het enkel van deze podotherapeuten! :p
[jsc1bi3] (score 1, diepte 2) Dan heb je in verhouding relatief grote voeten. Ik zou zeggen dat het nu wel een keer moet stoppen met groeien, maar je weet het nooit zeker. Toen ik 16 was ik ook precies 1,90. Heb er nog zo'n 2 a 3 centimeter bijgekregen in de jaren daarna. Je hebt de ergste groeispurt al wel achter de rug gelukkig!
[jsc302x] (score 1, diepte 0) Dat is afwachten. Vgm waren mijn voeten wel redelijk uitgegroeid toen ik zestien was, vgm zijn ze daarna nog een halve maat gegroeid zoiets.

En dan net kut zijn natuurlijk. Ik heb zelf nu maat 48 en dat is voor veel merken op het randje van wat ze verkopen. Dus opzich kan ik nog wel schoenen vinden die ik mooi vind, maar zouden mij voeten een halve maat groter geweest zijn dan zou dat al veel lastiger zijn. Dus laten we hopen dat dit het is 😬.

Aan de andere kant ben je dan waarschijnlijk ook lang en vrouwen zijn daar gek op kan ik je vertellen. Voor wat hoort wat 🙂
[jsc3qo8] (score 1, diepte 1 OP) ik ben 1,90
[jsc4db8] (score 1, diepte 2) Zie je? Je moet er wat voor over hebben. Ik ben 2,05 maar je hebt altijd baas boven baas natuurlijk. 😅
[jsc59hq] (score 1, diepte 3 OP) jaa zeg dat ik woon in limburg daar zijn de mensen wat kleinere vergeleken met de rest van nederland en ik krijg verrassend daar al best wat blikken door mijn lengte😂
[jsc5r9j] (score 1, diepte 1 OP) 1,90
[jsc7tzw] (score 1, diepte 2) Ahh ok dan is t niet zo erg toch? Misschien kun je basketball schoenen in grote maten vinden?
[jsc75ec] (score 1, diepte 0) Ik heb 47,5 en zijn gestopt met groeien toen ik ongeveer 16,5 half was.
[jsc9029] (score 1, diepte 0) Ik ben nu 27. Toen ik 14 was had ik schoenmaat 42. Op mijn 15e maat 40. Op mijn 21e maat 39. Nu op mijn 27e 42. Dit is allemaal van hetzelfde merk schoenen en daarnaast heb ik ook mijn oude schoenen weer van zolder gehaald. Volgend jaar zijn mijn voeten vast weer gekrompen. Ik weet niet hoe dit bij mij kan, ik schommel niet extreem met gewicht/vocht oid.
[jsfas5d] (score 1, diepte 2) Die kunnen zomaar maat 48 zijn, maar ook 50!
[jsdupfx] (score 1, diepte 1 OP) get a life
[jsf439a] (score 1, diepte 2) Nee.
[jscg3rp] (score 1, diepte 0) Ik vermoed even voor het gemak dat je een man bent? Dan zullen je voeten waarschijnlijk niet heel veel meer groeien

Voor vrouwen is het iets anders, die stoppen vaak iets eerder, maar kunnen er na een zwangerschap zo maar een maatje bij krijgen (iets met doorzakken).

Wil je genoeg keus hebben? Ga dan naar wessels in Vreden (dld) daar hebben ze nette schoenen, maar ook allerlei sneakers (nike, adidas, puma heb ik zeker zien staan) in allerlei kleuren en soorten.

Voor iemand met grote voeten een snoepwinkel.
[jscglsl] (score 1, diepte 0) Mijn voeten zijn doorgegroeid tot m'n 18de, maar ik had een late groeispurt. Mijn broertje was op z'n 16de klaar en die heeft schoenmaat 48, ikzelf 44.
[jscjdw9] (score 1, diepte 0) Dat wisselt per persoon. Ik heb sinds ik een jaar of 16 ben maat 44, dat is gelukkig prima te vinden. 

Gemiddeld genomen stoppen voeten met groeien bij 14 voor vrouwen en 16 voor mannen. Ik hoop voor jou dat je een man bent, want vrouwenschoenen in maat 48 zijn denk ik nog lastiger te vinden dan voor mannen.
[jsclnck] (score 1, diepte 0) ik zit sindsdien ook op 48, probeer eens andere merken. timberlands 47 zitten goed, adidas heeft ook 46 1/3 gaan over het algemeen ook goed. nikes moet ik echt nog 48 pakken.    
hogere schoenen zitten ook fijner, is alleen iets minder praktisch nu in de zomer.
[jsclqq9] (score 1, diepte 0) Ik heb maat 47, ik vind mijn schoenen tegenwoordig gewoon online, tot nu toe veel succes gehad met timberlands
[jscs0c1] (score 1, diepte 0) zelf heb ik 46. het fijne daaraan is dat ik online altijd dingen in de aanbieding kan kopen. misschien kan je in outlets kijken? daar zijn vaak wel toffe schoenen te vinden die ze anders niet kwijt kunnen door de niet gangbare maten
[jscvvzk] (score 1, diepte 0) Hé, bij mij zijn ze gestopt rond mijn 16de, tevens ook maat 48.

Zelf heb ik voorkeur aan schoenen passen en voelen en ga ik altijd naar Caland schoenen, een speciaalzaak voor grote maten. Ze hebben een fysieke vesteging in Rotterdam en Amsterdam. De keuze valt meestal op het merk Australian footwear. 

Dat is ook niet heel vaak. Ik heb sindsdien maar 3 paar normale schoenen gekocht (één boven de enkel voor als het kouder word, en twee onder de enkel. Het eerste paar heb ik na zo'n 8/9 jaar vorig jaar eindelijk laten repareren aan de hiel na ze bijna elke week meerdere keren gedragen te hebben over die 8/9 jaar heen. Enorm goede en houdbare schoenen, iets prijziger maar je haalt het er uit op de lange termijn. En sowieso zijn de meeste schoenen van Caland van goede degelijke kwaliteit (wel dus vaak tussen de €100-180), tenminste het assortiment in Rotterdam, ben maar een keer kort bij de winkel in Amsterdam geweest.

Maar dat vooral als tip wanneer je zeker weet een beetje uitgegroeid te zijn.
[jscydxp] (score 1, diepte 0) Bij mij bleven mijn voeten ook groter worden tot mijn 18e ergens. 2 jaar besloten geleden om wat aan mijn gweicht te doen, 20 kg afgevallen en mijn schoenmaat is een maat kleiner geworden.
[jscyqaj] (score 1, diepte 0) Gestopt rond mijn 16de en heb uiteindelijk als 185cm lang iemand 42/43 gekregen.
[jscytv4] (score 1, diepte 0) Ga naar de huisarts, laat je verwijzen naar de kinderarts en laat röntgenfoto’s maken van je voeten. Kan de arts zien of ze nog kunnen groeien en of er iets tegen te doen is. Succes!
[jscyve3] (score 1, diepte 0) Verschilt pp. Enige manier om dit enigszins te voorspellen is röntgenfoto's vd voeten te laten maken om de groeischrijven te bekijken.
[jsfum6p] (score 1, diepte 1 OP) is het niet behoorlijk prijzig om zoon foto te laten maken?
[jsh6c95] (score 1, diepte 2) Dat ligt er aan. Zomaar zonder reden krijg je het waarschijnlijk niet voor elkaar. Voor hele lange kinderen wordt het wel vaker gedaan om ongeveer te voorspellen hoe ver ze nog door groeien en of ze dus evt willen ingrijpen. Kosten is eigen risico en daarna verzekerd (mits dus met een goede reden voor de foto).
[jshklkp] (score 1, diepte 4) 1.90 is inderdaad niet uitzonderlijk lang nee. Als je je echt zorgen maakt of je voeten nog groter worden, dan kan je met je huisarts gaan praten. 
Er bestaat een operatie om de groei vd voet te remmen, maar ja dat doe je natuurlijk niet zomaar even:
https://www.mmc.nl/kinderorthopedie/aandoeningen-en-behandelingen/percutane-epifysiodese/
[jsjacpq] (score 1, diepte 4 OP) ze zeiden gewoon dat ik klaar was met groeien ze lieten alleen de lengte van me ouders zien meer niet geen foto’s of iets gemaakt.
[jsd0nwk] (score 1, diepte 0) Ik ben nu 17 en heb sinds mijn 15de dezelfde schoenmaat. Ik denk dat het heel erg verschilt per persoon, vrienden van mij moeten af en toe nieuwe schoenen kopen omdat de oude niet meer passen.
[jsd1pnr] (score 1, diepte 0) 40/41 sinds mijn 13e ofzo. Ik denk dat het lastig is om er een pijl op te trekken. Maar een hobby als schoenmaker voor grote maten is misschien wat voor je. Zelf kekke schoenen en een zakcentje door mensen te helpen. Kost volgens mij niet veel meer om te beginnen dan een andere hobby.
[jsd2z8y] (score 1, diepte 0) Ik hoop het! Maar ik ben dan 35 heb heb maat 41. Soms 41,5!!
[jsd59d1] (score 1, diepte 0) Ik ga altijd naar schuurman schoenen, daar lopen de maten bij best een aantal schoenen op tot 49 of 50. Heb zelf 47 namelijk en kan er eigenlijk altijd wel wat vinden. Sneakers, wandelschoenen, leren schoenen etc.
(32 reacties met lagere score weggelaten)

=== THREAD 1f2d2ql ===
SUBREDDIT: r/nederlands
DATUM: 2024-08-27  SCORE: 74  REACTIES: 92
TITEL: Palestijnse vluchteling, dood gevonden met gebonden handen en voeten in Antwerpen.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lk5gkz8] (score 192, diepte 0) >Door de gebonden handen en voeten leek het er erg op dat de man door een derde om het leven gebracht werd.

Aan de analytische kwaliteiten van de Belgische recherche zal het niet liggen.  
In elk geval een afschuwelijke zaak. Vlucht je hier naartoe eindig je alsnog op zo'n verschrikkelijke manier.
[lk5uupu] (score 57, diepte 0) Echt weer een r/nederlands reddit momentje hier.
[lk5xnrz] (score 46, diepte 1) het eerste wat je leest is iemand die achteruit werkt om moord goed te praten
[lk5hr1o] (score 38, diepte 1) In welke wereld is Iran een goed land? Het wordt geleid door een of andere religieuze gek, er is volop cultuurpolitie en onvrijheid en internationaal gezien nucleair dreigend en midden-oosten destabiliserend. Als ik moest kiezen tussen Iran en Nederland dan wist ik het wel.
[lk5g1rd] (score 27, diepte 1) Lees anders de regels van de sub even door ouwe reus.
[lk5lbg2] (score 27, diepte 1) Iemand wordt op gruwelijke wijze vermoord en dit is het enige dat je erover te zeggen hebt?
[lk5wggz] (score 24, diepte 0) Bij de aanslag in Solingen waren er hier reacties dat het heel goed mogelijk is dat het door de Russen was opgezet als psyop. Die kregen toen aardig wat upvotes. 

Zal dat nu ook het geval zijn? Of zal de framing nu anders zijn?
[lk7dgmc] (score 22, diepte 1) Goeie opmerking, een vermoorde man gebruiken om je anti immigratie punt te maken. Lekker!
[lk5jjwd] (score 19, diepte 2) Ligt eraan, als vroom fundamentalistische moslim kun je daar prima gedijen neem ik aan. Dichter bij een soort sharia utopie dan Iran kom je bijna niet meer tegenwoordig.
[lk5ws3s] (score 19, diepte 3) Als ik je aanrijd is het dan  jouw schuld omdat je over de weg liep en je dat niet had moeten doen?
[lk5hs1e] (score 18, diepte 3 OP) Mijn aanname was niet dat de descriptie van r/nederlands van chatgpt kwam, maar ik zal vooral niet tussen jou en je complot komen.
[lk5xtdg] (score 16, diepte 1 OP) Ik vind het persoonlijk een compleet mysterie dat dit zó'n onwelkom artikel is.
[lk5mawu] (score 15, diepte 2) Waarin ben ik naïef? Het lijkt me moeilijk zelfmoord te plegen in zo'n positie. Het kan een bondage fetisjist geweest zijn waarbij het tijdens het spel mis ging, maar ook niet heel waarschijnlijk.  
Dus de conclusie moord lijkt me niet naïef. Ik zeg toch verder niks over het motief van de (nog onbekende) dader. Al helemaal niet of dat motief een lokale oorsprong heeft of terug gaat naar het land van herkomst.

Je trekt wel heel snel conclusies. Ben blij dat jij geen rechercheur bent.
[lk5u5wa] (score 15, diepte 4) Nou als wij toch in vooroordelen gaan denken, betekent dat iedere vermoorde autotochtone Nederlander een pedofiel moet zijn geweest.

"Je word toch niet zomaar vermoord, of wel?!"
[lk6oayd] (score 14, diepte 1) Forensisch gezien kan het slachtoffer een natuurlijke dood gestorven zijn.
[lk80l1a] (score 14, diepte 7) Je punt is dus: Mooi dat die dood is want hij is naar Nederland gevlucht ipv naar een ander land. Is je moeder nu trots op je? Wat een gigantische hoop haat komt er uit jou.
[lk6s4mq] (score 13, diepte 2) Dat sluit ik in de rest van het draadje ook niet uit. Hoewel hier denk ik de juridische definitie belangrijker is. Als de persoon in hulpeloze toestand is achtergelaten en toen (ongerelateerd) een hartaanval kreeg, dan nog zijn de mensen die hem zo hebben achtergelaten betrokken en hebben ze voorkomen dat hij hulp kon zoeken.  
Nu ben ik geen jurist, en zeker geen Belgisch jurist, maar mishandeling met de dood tot gevolg komt toch als gedachte in me boven.
[lk5zyql] (score 13, diepte 5) Wel een heel krom voorbeeld. De gedode man is feitelijk immers niet moedwillig op zoek gegaan naar gevaar.
[lk5yao0] (score 13, diepte 2) Echt waar? Zodra sommige mensen hier "palest..." lezen zijn ze getriggered om de meest lelijke comments te plaatsen.
[lk5xr6q] (score 13, diepte 1) Neejoh, hier zit duidelijk een groot zionistisch  complot achter.
[lk5mfpc] (score 12, diepte 6) waarom richting een pro Isreal gebied vluchten? Ik vertrouw et niet.
[lk5nrar] (score 11, diepte 4) Lijkt me nog steeds een verschrikkelijk einde...  
Verder kan je heel veel speculeren, maar heeft dat zin?
[lk5nivp] (score 11, diepte 4) Als die gasten hersenen hadden liepen ze elkaar niet constant op te blazen om een of ander denkbeeldig sprookje en had er nooit iemand hoeven vluchten. Dan kunnen ze net zo goed samen hand in hand op dat kleedje gaan liggen als ze toch naar hetzelfde sprookje bidden..
[lk5g3el] (score 10, diepte 1 OP) Welkom! Deze subreddit is vooral voor artikelen in het Nederlands (of posts over de Nederlandse taal)
[lk5lmuw] (score 9, diepte 4) Boeie Ruurd, zitten nog steeds 20 landen tussen daar en NL waar 't prima veilig is.
[lk62se5] (score 9, diepte 3 OP) Nee, die opmerking was niet echt waar
[lk5mlvs] (score 8, diepte 3) bier is geen ontbijt, ga je roes eens lekker uitslapen
[lk662uk] (score 7, diepte 2) Ohhh ja als het slachtoffer van de lugubere moord zelf een strafblad had, dan is het niet erg!
[lk5ysbv] (score 7, diepte 12) Israel die steeds blijft focussen op een terroristische moslim organisatie die als motto heeft niet te kunnen rusten tot de joodse staat weg is, is erger dan die organisatie die oproept tot genocide van de joden? Dat is pas ziek, als je je daar achter gaat lopen schuilen. Maar goed, verziekte religie/cultuur in de moslim landen hoort een een beetje bij. Misschien leuk tripje voor je?
[lkckc3k] (score 7, diepte 0) Als dit een Joodse meneer was, dan was het absolute chaos in Europa geweest.
[lk5fr2e] (score 6, diepte 1) Omdat het Antwerpen is geen Anvers.
[lk5l43d] (score 6, diepte 3) Als je hersenen had wist je dat Iran Shia is en meeste Palatijnse moslims Sunni zijn. Beetje zeggen dat de Nederlanders van spanje moeten vluchten en moeten vertrekken naar de papaal staat
[lk725fb] (score 6, diepte 9) Niemand zegt dat het veilig is onder Hamas. 
Maar beweren dat minder Hamas meer veiligheid betekend is niet echt ergens op gebaseerd. 

Naast dat Israël nog mijlenver is van het uitroeien van Hamas en ze geen enkel idee hebben wat ze vervolgens zullen gaan doen. 

Er zijn de afgelopen periode ook extreem veel meer doden gevallen onder de Israëlische aanval dan onder het regime van Hamas. 

Los van of je dat gerechtvaardigd vind of niet is het uitermate vreemd om daarvan te zeggen dat ze veiligheid brengen. 

De kans dat je huis explodeert is simpelweg vele malen groter geworden sinds het begin van de belegering van. Gaza. 

Ook maken Israëlische kolonisten het niet veiliger op de Westelijke Jordaanoever. 

Uiteindelijk is het niet eens relevant aan welke kant je staat. De bewering dat Israël voor meer veiligheid zorgt of gaat zorgen in Gaza is gewoon niet waar.
[lk7532i] (score 6, diepte 5) Dat kun je helemaal niet weten, misschien was hij in Nederland of Papoea Nieuw Guinea ook wel afgemaakt.  In z’n eigen land waarschijnlijk wel in ieder geval anders was hij niet gevlucht toch?
[lk5xte6] (score 5, diepte 12) Dat is het ook, je kunt moeilijk Hamas daar laten zitten en maar meer kwaad laten aanrichten. Israel heeft geen keuze en moet wel. Dat die baardapen op die kleedjes elke keer laten zien dat ze graag burgers voor de bus duwen kun je Israel niet kwalijk nemen.
[lk61qf2] (score 5, diepte 13) Laat me raden: jij geloofde zeker ook dat Rusland Oekraine binnenviel om de nazi's daar uit te roeien? 

Verder heb ik al benadrukt dat ik beide partijen fouten dingen zie doen, maar je hebt je intellect al laten doorschijnen. Klinkt als een gebroken plaat nu. 

Verder woon ik in de randstad dus genoeg moslim interactie hier al hoor.
[lk6ezqn] (score 4, diepte 14) Ergens heeft hij wel een punt. Hamas heeft het gebruik van menselijke schilden tot een nieuw level getilt. Dan is het logisch dat er meer burgerslachtoffers vallen.

Als Hamas een militaire basis onder een (kinder)ziekenhuis plaatst, ja dan is het toch ook een beetje Hamas haar schuld dat er bombardementen komen.

Wie zijn schuld is het als menselijke schilden sterven? De 'gijzelnemer' of 'de schutter'. 

Is een lastige... Ben blij dat ik die beslissing niet hoef te maken. Dood je onschuldige zieke kinderen om onschuldige levens te redden van je 'eigen volk'? Liever niet natuurlijk..
[lk6yk0b] (score 4, diepte 7) Ik ben het niet eens met de reactie waar jij op reageert. Maar beweren dat Israël Palestina veiliger maakt slaat natuurlijk nergens op.
[lk72t27] (score 4, diepte 9 OP) Is er minder Hamas dankzij het Israëlische beleid? Het _lijkt_ namelijk _niet_ alsof apartheid, martelkampen, massamoord en bezettingen tot minder Hamas hebben geleid.
[lk5klpw] (score 3, diepte 1) Omdat het interessant is en er weinig spannends gebeurd in Nederland.
[lk7dmqj] (score 3, diepte 7) Er loopt hamas rond in Antwerpen?😂je bent niet goed snik
[lk6wb3b] (score 3, diepte 14) Ik gok dat je op de verkeerde persoon reageert, maar mocht je toch zo’n plaat voor je kop hebben wil ik je graag vragen even te kijken naar de filmpjes van Mosab Hassan. Dit is een zoon van een van de oprichters van Hamas die je precies kan vertellen wat er mis is met die hele organisatie. Ga daarna maar opnieuw met een neutraal gezicht vertellen dat ik van het padje af ben en zeg ook maar meteen dat de zoon van de oprichter van Hamas niet weet waar Hamas voor staat en van het padje af is.
[lk64lip] (score 3, diepte 14) Ten eerste, gecondoleerd met de vele moslim interactie, dat kan niet goed zijn voor je gezondheid en je mentale gezondheid, dus waarom je er zo over denkt kan ik je niet kwalijk nemen.. 

Wat Rusland betreft, nee hoor, dat is een naar land en Oekraine heeft (net zoals Israel) het volledige recht zichzelf te verdedigen.
[lk8dviy] (score 3, diepte 7) Ik zou iemands dood over het algemeen wel vervelend noemen.
[lk5o2u1] (score 2, diepte 3) Dat is niet relevant. Deze thread voldoet gewoon aan de voorwaarden, dus ga met je geklaag naar een thread die niet aan de regels voldoet
[lk5q54e] (score 2, diepte 5) Nee hoor, ik leg gewoon wat feiten op tafel
[lk5pizw] (score 2, diepte 4) hmm ik ken iemand die zo aan zn einde is gekomen...  maar familie heeft et naar buiten gebracht als zelfmoord beetje vaag verhaal, hij deed et ook solo dus beetje triest ook.
[lk7c0gz] (score 2, diepte 5) Beetje een raar ding om de zeggen op iets wat lijk op moorde. Ik bed als het een jood was iedereen zal zeggen dat het een moord was en niet af vragen off het kinky sex was
[lk5p1r3] (score 2, diepte 7) Yep, goed dat Israel die kinderziekenhuizen bombardeert inderdaad. Aanpakken die handel, levensgevaarlijk die zieke kinderen.
[lk74pot] (score 2, diepte 11) Dat Hamas dit conflict geïnitieerd heeft betekend nog altijd niet dat Israël het veiliger maakt. 

Beide zijn namelijk waar. 

Ja. Hamas is dit begonnen en inderdaad Hamas maakt het ook onveiliger voor de eigen bevolking. 

Tegelijkertijd maken de militaire acties van Israël het ook onveiliger in Gaza. 

En Hamas is zeker niet eindverantwoordelijk. Dat is een hele vreemde stelling. 

Israël maakt gewoon zijn eigen keuzes.
[lk77ox8] (score 2, diepte 13) Het gaat niet om wat Israël moet of niet moet. 
Feit is dat Israël het niet veiliger maakt. 

Dat staat los van wie dit is begonnen en of het geweld dat Israël gebruikt gerechtvaardigd is. 

Als Israël een school bombardeert omdat daar Hamas strijders zitten dan kan het best een gerechtvaardigd bombardement zijn. Maar het zorgt er tegelijkertijd voor dat het onveiliger is. 

En wat Hamas doet is natuurlijk geen vrijbrief voor Israël om maar te doen wat ze willen. 

Israël is uiteindelijk verantwoordelijk voor zijn eigen keuzes. Het is niet de schuld van Hamas dat er Palestijnen verkracht worden in Israëlische gevangenissen. Dat is gewoon de verantwoordelijkheid van Israël.
[lk7ebmg] (score 2, diepte 15) Israel zegt dat ze geen warcrimes plegen? Dat zei Hitler ook! 

Lees je in over wat Israël doet, en de geschiedenis. Voordat je je achteraf beseft aan welke kant van de geschiedenis stond.
[lk7f3kw] (score 2, diepte 15) Je hoeft echt niemand te overtuigen van het feit dat Hamas een kwaadaardige terreurorganisatie is. 

Het blijft wel vreemd dat je blijft proberen Hamas verantwoordelijk te maken voor de acties van Israël. 

Ook als een bom op een doelwit gerechtvaardigd is gaat het ten kosten van de veiligheid. 

Zelfs in je kromme redenering dat Hamas verantwoordelijk is voor de acties van Israël is het complete onzin om te beweren dat Israël het veiliger maakt in Gaza. 

Die bewering is op geen enkele manier te onderbouwen.
[lk7dzqs] (score 2, diepte 11) Hamas is gekomen als een consequentie van de acties van Israël, dit conflict is al sinds de tweede wereldoorlog bezig dus hamas KAN niet de oorzaak zijn. Die bestond toen nog niet! Zoek eens op hoeveel massamoorden Israël heeft gepleegd VOORDAT hamas bestond
[lk72t1x] (score 2, diepte 3) Hoe precies volgens jou? Vraag ik mij oprecht af.
[lsmk4qq] (score 2, diepte 1 OP) supposedly a name was doing the rounds in antwerp, but nothing's been released publicly as far as I've heard or found

I'm sorry that you can't contact your friend, hope you find out how he's doing
[lk5ij6n] (score 1, diepte 3) Artikelen IN de Nederlandse taal, niet OVER de Nederlandse taal. \\

Voor je iemand gaat uitschelden, misschien eerst zelf even beter lezen.
[lk5yogs] (score 1, diepte 5) Zanger van inxs, is een bekend verhaal.
[lk6q2fs] (score 1, diepte 4) Wat bedoel je dan te zeggen met "niet zo naïef doen". Welke denkfout maakt degene waarop je reageert volgens jou?
[lk5n02b] (score 1, diepte 6) Wat? Israel zorgt daar niet voor? Dat is Hamas aan het doen. Israel is juist daar de boel eindelijk eens veilig aan het maken. Maar met jouw logica gaat Hamas dus Israëliërs opvangen? (Nahja dat doen ze nu onvrijwillig evengoed al..)
[lk5q9bj] (score 1, diepte 8) Nou, het gaat Israel er vooral om dat Hamas jammer genoeg steeds tussen de burgers gaat zitten, tunnels onder deze ziekenhuizen graaft en de hele bevolking gegijzeld houdt.. Dus, als Hamas weg is zijn de mensen veilig en worden er geen ziekenhuizen gebombardeerd.
[lk5vuc6] (score 1, diepte 10) Tja, ga dat maar tegen Hamas vertellen, misschien stoppen ze direct met hun terreurclubje en hoeft er nergens meer een dode te vallen. Als je als land continue door je buurland met raketten wordt bestookt en het doel van de organisatie die in dat land aan de macht is is het uitroeien van de Israëlische staat, heb je als Israel weinig keuze. Moeten ze het dan maar slikken dat die terreurbende om de haverklap aanslagen pleegt?
[lk73key] (score 1, diepte 10) Maar ook dit komt door Hamas. De enige reden dat Israel nu Palestina aanvalt is vanwege de aanslagen die Hamas keer op keer pleegt. De enige reden dat er ziekenhuizen opgeblazen worden is omdat Hamas er met militaire basissen in tunnels onder gaat zitten om hun bevolking voor de bus te duwen. Zonder Hamas geen oorlog en zonder oorlog veiligheid. Daarbij geeft Hamas (die die cijfers dus vrijgeven) niet aan of een dode een Hamas lid was of een burger. 

Als Hamas daar niet had gezeten had 7 oktober niet plaatsgevonden en waren we hier nu niet geweest. Hamas moet daar weg, voor Israel, voor Palestina en voor iedereen op deze mooie planeet. 

Sorry maar je bewijst letterlijk mijn punt met je comment.. De belegering van Gaza, waarom komt dat? Door Hamas. Hamas is eindverantwoordelijke voor alles dat daar gebeurt omdat Hamas de aanstichter is voor alles dat daar gebeurt. Vrede willen ze ook niet, ook dat slaan ze continue af.
[lk752s9] (score 1, diepte 12) Maar wat moet Israël dan? Hamas bestaat om Israel uit te roeien, dit is het doel van Hamas en zolang Israel bestaat gaat Hamas er alles aan doen om dit te regelen. Moet Israel dit lekker laten zitten en maar afwachten tot het uitgeroeid wordt nadat er keer op keer door datzelfde clubje aanslagen binnen Israel worden gepleegd? Nee natuurlijk niet. 

Hanas started this, Hamas is fully to blame.
[lk79yyy] (score 1, diepte 14) Dat is zeker de verantwoordelijkheid van Israel, gelukkig nemen zie de ook: A spokesperson for the Israel Defense Forces said that the Israeli military “rejects allegations of systemic abuse, including sexual abuse, in its detention facilities” and maintained it follows Israeli and international law. The military pointed to the arrest of the soldiers suspected in the Sde Teiman abuse case as evidence that they enforce such laws if broken.

Helaas kun je dat van Hamas niet zeggen, zij laten graag zien niks te geven om hun eigen bevolking en nemen niet de verantwoordelijkheid om het op te lossen. 

De enige reden dat die school onveiliger is is omdat Hamas daar is gaan zitten. Het doet mij een beetje denken aan dat plaatje van die fietser die een stok tussen zijn spaken stopt en dan roept dat Israel hem heeft laten vallen.
[lk7foya] (score 1, diepte 16) Sorry, maar ik moest hier toch even hard om lachen en kan niet wachten tot die spiegel voor je neus staat. Sinds het ontstaan van Israel in de huidige vorm hebben alle buurlanden uitgeroepen er alles aan te doen om dat tegen te gaan en om die joden daar uit te roeien. 

Als jij ook maar iets dat Hamas naar buiten brengt (want al die organisaties zijn in handen van dat gezellige Hamas) gelooft en zelfs zegt dat Israel vergelijkbaar is met Hitler, dan ben je echt van de kaart af. Vroeger hadden we een plek voor mensen met dat soort ideeën, helaas is dat allemaal wegbezuinigt.
[lk74otk] (score 1, diepte 10) Voor de oorlog waren de moslims uit Palestina welkom om in Israel te gaan werken. Er was een hoop meer vrijheid voor de moslims om in Israel te doen en laten wat ze wilden. Andersom is dat natuurlijk niet zo, Joden mogen niet in Palestina werken en worden daar gewoon rustig neergestoken mochten zij daar per ongeluk terecht komen. 

Zijn alle Israëlische joden goed? Nee zeker niet. Maar het clubje foute moslims is vele vele malen groter dan het clubje foute joden. Jammer dat elke keer de joden de schuld krijgen. De plaag? Joden. Economische problemen? Joden. Zelfverdediging van de zoveelste terreuraanslag van een terroristische organisatie die maar niet kan ophouden om te roepen dat Israel niet mag bestaan en moet worden uitgeroeid? Och wat zijn die joden weer fout bezig.
[lk5l6z4] (score 1, diepte 3) Nogal een aanname dat deze man dat had gewild. Niet alle moslims zijn zo orthodox. En hoewel het regime verschrikkelijk is, is de Iraanse bevolking zelf een stuk gematigder en liberaler.
[lk5xfyj] (score 1, diepte 2) De hardcore islamisten voelen zich thuis in Iran, en vinden juist dat het regime daar goed bezig is. Deze groep is in Iran een grote minderheid, maar dat zijn er nog steeds miljoenen aangezien Iran een populatie heeft van 90 miljoen.
[lk6p3yb] (score 1, diepte 2) Vlaanderen of wallonië? /s
[lk7e0o2] (score 1, diepte 7 OP) Mag ik aannemen dat je er bij de eerste de beste vermoorde Israëliër ook gelijk bij staat om uit te leggen dat 'ie dan maar weg had moeten blijven?

Schaam je oprecht kapot, man. Om op deze manier te praten over iemand die oorlog ontvlucht is alleen om hier aan een boom opgehangen te worden, puur en alleen omdat je je moslimhaat niet lang genoeg op zij kan zetten om een beetje nenselijkheid te laten zien.
[lk744bi] (score 1, diepte 0) Belgie en politie 😪
[lk96g6l] (score 1, diepte 0) Wow hoe bestaan er zulke gekke mensen ?!!!
[lsm3sye] (score 1, diepte 0) Is it possible to find out, who is that? What’s the name of this person? I want to know that because I have a Palestinian friend around that age and I cannot contact him anymore…how can I learn at least the name, to know that it’s not my friend (I hope it’s not him)…
[lk5opge] (score 0, diepte 4) Gossie, pik getrapt? Fucking hell zeg, doe rustig.
(35 reacties met lagere score weggelaten)

