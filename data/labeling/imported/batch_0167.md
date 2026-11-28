# Label-batch batch_0167

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
Schrijf het resultaat naar `batch_0167.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1qumlif, 1wuyp29, vzmmaj).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1qumlif ===
SUBREDDIT: r/nederlands
DATUM: 2026-02-03  SCORE: 96  REACTIES: 91
TITEL: Ongeloof om ‘afschuwelijk’ filmpje in azc: beveiliger laat asielzoeker voeten kussen
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[o3b6ynf] (score 170, diepte 0) Wat ben je een ongelooflijk stuk verdriet als je dit soort dingen gaat doen. Dan zit er echt wel een steekje los.
[o3b6tyw] (score 91, diepte 0) Iedereen in die kamer ontslaan dan maar. Echt wat een achterlijke zak stront ben je.
[o3bfk9r] (score 52, diepte 2) Als dat echt zo is dan raad ik je aan contact op te nemen met de media. Bv met de schrijver van dit stuk, met Zembla of met andere onderzoeksjournalisten.

Ook als het lang geleden is.
[o3bb5i7] (score 39, diepte 1) Jarenlang op azc's gewerkt als beveiliger, naast dit zijn er nog wel meer schokkende dingen gebeurd, ook waar coa personeel bij betrokken is.
[o3b70xp] (score 35, diepte 1) Inderdaad, je zou zeggen dat iedereen die erbij stond en het liet gebeuren medeplichtig is.
[o3b74s9] (score 34, diepte 0) Stanford Prison Experiment, iemand?
[o3bfoeh] (score 33, diepte 0) "Dat dit in nederland gebeurd is onvoorstelbaar" wie os er ook maar een klein beetje verbaasd?
Walgelijke rotcultuur hebben we ontwikkeld, en mensen hier hebben de scheefgegroeide hersenen die het nog durven te verdedigen ook!
Ik schaam me om de verbaasdheid te moeten zien en om nederlander te zijn
[o3b9t60] (score 31, diepte 1) Stanford Prison Experiment was niet integer. De bewakers kregen actief instructies om harder op te treden.

https://www.eoswetenschap.eu/psyche-brein/docureeks-toont-de-mythe-van-het-stanford-experiment#:~:text=Een%20van%20de%20opvallendste%20figuren,de%20programmatie%20vind%20je%20hier
[o3bgcid] (score 26, diepte 0) Als je ziet hoe we als maatschappij spreken over asielzoekers kan dit toch geen verrassing zijn. We vonden het prima om een fascist verantwoordelijk te maken voor het asielbeleid.
[o3b7a4u] (score 23, diepte 0) Het is een filmpje van 2,5 jaar geleden, maar wat een narigheid.
[o3ba54y] (score 23, diepte 4) Volgensmij bedoelt de persoon boven je het gewoon als aanvullende informatie. Ik denk dat je er te veel achter zoekt.
[o3bavdp] (score 21, diepte 1) ‘Mijn carrière is verpest door asielzoekers’ post incoming
[o3bet58] (score 20, diepte 2) Stop je hondenfluitje maar weg en zeg gewoon wat je bedoelt, watje
[o3b7u68] (score 18, diepte 0) Helaas zijn de types die op zulke functies afkomen, niet altijd zuiver in aard.

Beveiligers, bewakers, politie, leger enzovoorts...
[o3b9nn0] (score 18, diepte 2) Klopt maar types die graag macht over anderen willen hebben kiezen eerder om bv  agent te worden dan om een bakker te worden.
[o3b7nbo] (score 17, diepte 2) Klopt, het filmpje wel.
Maar dit is 2,5 jaar geleden gebeurd, ik had duidelijker moeten zijn.
[o3bl5jf] (score 16, diepte 3) Mensen die zich aangetrokken voelen tot het beroep beveiliging, boa of agent hebben vaak een streng overmatig autoritair karakter wat achter gesloten deuren soms leidt tot taferelen zoals dit
[o3bgact] (score 13, diepte 1) Dwaal_Lamp moet toch nog even snel kijken of hij het topic om kan zetten naar vreemdelingenhaat! Stel je voor dat het vijf hele minuten lang niet gaat over hoe stom buitenlanders allemaal wel niet zijn!

Want ja, stel je voor dat je mensen die om hun geaardheid moeten vluchten uit hun thuis dan hier gaat helpen...
[o3b7ioh] (score 10, diepte 0) Bevuiliger (geen fout) gewoon op staande voet, je weet wel. Opzouten en nooit meer een VOG graag
[o3b8wpd] (score 10, diepte 0) Je weet dat ze dit filmen om met andere collega's te delen en ze belachelijk te maken. Ik zal verder niet zeggen wat ik echt denk, aangezien Reddit dat niet toestaat.
[o3bfxnf] (score 9, diepte 6) Wat ben jij een akelig figuur zeg jezus
[o3bbztd] (score 9, diepte 1 OP) https://preview.redd.it/ie9um3s509hg1.png?width=498&format=png&auto=webp&s=e6e8d996ac68b371a6a30400c4e6f6c8b0e5375f
[o3bgyle] (score 8, diepte 1) > De meeste van die gasten haten jullie met heel hun ziel

Jij haat hun met heel je ziel lijkt het vooral.
[o3bpgym] (score 8, diepte 0) Vies smerig stuk onderkruipsel. Losertje.
[o3bci4b] (score 7, diepte 3) Kan je op feesboek leese
[o3bymon] (score 7, diepte 1) Ik denk dat hier geen aanleiding voor was. Dit is gewoon iemand die macht wilt hebben over een andere. Hij zegt nog "good boy". Zijn doel was gewoon om te vernederen. Los van het feit dat geen enkele aanleiding dit oké maakt. Nederland is een rechtstaat en geen verneder staat. Deze persoon en iedereen die staat te kijken moet een werk verbod krijgen met schade vergoeding.
[o3bwn96] (score 6, diepte 2) Wat voor sfeer is daar dan, waardoor niemand iets zegt?
[o3dym1h] (score 6, diepte 3) Genoeg. Variërend van ex collega's die er op uit waren om zoveel mogelijk pijn te doen bij het ingrijpen tijdens incidenten (vechtpartijen etc) tot sexueel gerelateerde dingen en zelfs een heuze bos bordeel.
[o3c5l5x] (score 6, diepte 3) Ik bedoel die mentale gymnastiek van je, wat heeft links hier in godsnaam mee te maken, als het fout haat zijn het niet jouw partijtjes die het op moeten lossen hoor nee het is verantwoordelijkheid van links
[o3dyidj] (score 5, diepte 4) Same, ik kan een dik boek schrijven met dingen die er gebeurd zijn die gewoon niet door de beugel kunnen.

Alles wordt in de doofpot gestopt.
[o3b7ji9] (score 5, diepte 1 OP) Het filmpje is gisteren pas op het internet verschenen.
[o3b9g13] (score 5, diepte 1) In geen enkel beroep is iedereen zuiver in aard...
[o3bnymg] (score 5, diepte 1) je kan stoppen met doen alsof je geeft om LHBTI’ers. weer hen gebruiken om jouw vreemdelingenhaat te versterken, wat voorspelbaar weer
[o3br8kt] (score 5, diepte 1) Af en toe een pauze van reddit nemen mag ook heh, hersens even resetten weetjewel?
[o3dx212] (score 4, diepte 3) Is al redelijk lang geleden en wegens geheimhoudingsplicht ga ik ook niet naar de media.
[o3f629x] (score 4, diepte 4) Dat kan natuurlijk zo in je contract staan, maar ik betwijfel ten zeerste of een geheimhoudingsplicht voor dit soort zaken wel legaal is.

Je kan in gesprek gaan met iemand die juridisch advies hierover geeft. Zo kan je bij een lidmaatschao van een vakbond zoals ze FNV juridisch advies krijgen (aangezien het over afspraken met je werkgever gaat).

Je moet natuurlijk altijd op jezelf letten, maar dit is wel echt de manier om het verschil te maken. Als er dingen gebeuren die fout zijn, is het goed als mensen dat weten.
[o3buup6] (score 4, diepte 4) Ja dit is vaak terug te zien bij Amerikaanse politie en de bodycams. Zouden ze hier ook moeten doen
[o3bi1lt] (score 4, diepte 2) Wetenschappelijk niveau 0 dat “experiment”.
[o3d5jvg] (score 4, diepte 3) Dat ging over het opvolgen van autoriteiten, ook als dat opvolgen schade toebrengt. Dat relateert hier niet echt aan, tenzij Die bewaker instructie hiertoe kreeg van hogerhand, terwijl hij het eigenlijk zelf niet zag zitten.
[o3bboi8] (score 4, diepte 3) Hetzelfde fenomeen zie je bij verplegers. Maar dit zijn wel uitwassen hoor.
[o3biaer] (score 4, diepte 2) You are funny.
[o3bd2vx] (score 4, diepte 0) Zouden ze dit bedoelen met dat de asielzoekers wel eens wat dankbaarder mogen zijn?
[o3d14re] (score 4, diepte 5) Geen flauw idee waar dit allemaal op gebaseert is je hebt je weer lekker laten informeren gast, er is al heel lang gewoon een open azc dag en de financieen staan altijd vrijgegeven. Echter hebben die mensen ook gewoon recht op privacy het is toch best logisch dat niet zomaar elke dag iedereen willekeurig binnen ken lopen? En om even bij het filmpje ter zake te blijven hoe zou dit volgens jou helpen? Moet je altjjd een controleur op de beveiliger zetten 24/7? en wat nou als dat ook net zon naar mannetje blijkt te.zijn?
[o3d5s14] (score 4, diepte 7) Das geen argument en ook geen antwoord op mijn vraag, wat wil je nou concreet? wat versta je onder openheid van zake en hoe zou je deze persoon ermee helpen? Oh en nog wat ik weet dat het een openbaring is maar links is al 20 jaar oppositie. Het enige wat je droomcoalitie aan asiel gedaan heeft laatste keer is op het IND bezuinigen.
[o3bxhjx] (score 3, diepte 5) Nederlandse agenten lopen vgm al met bodycams rond voor voornamelijk hun eigen veiligheid, met het verschil dat de agent in Nederland zelf mag beslissen wanneer er wordt gefilmd. Lekker makkelijk wegkijken dus
[o3byi7v] (score 3, diepte 6) Toch vraag ik me dan af waarom ze bijvoorbeeld bij vuurwerk rellen dan niet die bodycams laten zien. Zou toch meer impact hebben als je het spul op ze af ziet vliegen lijkt me.
[o3b92dc] (score 3, diepte 1) Dit wou ik net zeggen. En daarvoor de milgram experiment. Heel interessant voor mensen om dit te zien, kan het zo op YouTube vinden.
[o3dzy3c] (score 3, diepte 1) Meneer is ontslagen om deze video 2,5 jaar geleden. 

Heeft daarna gewoon weer kunnen solliciteren met VOG én VGB als beveiliger. Nieuwe werkgever is nooit op de hoogte geweest van dit incident.
[o3bavxc] (score 3, diepte 3) Of de politiek in, zie je ook heel goed.
[o3bg0f7] (score 3, diepte 2) Echter hebben schoenverkopers vaak niet echt de macht om dit soort shit uit te halen.
[o3bf6p8] (score 3, diepte 1) Je moeder had je op moeten voeden, mensen als jij zijn wat er mis is in dit rotland
[o3djp3v] (score 3, diepte 1) Even een LGBT-er verder onderdrukken vind jij normaal?
[o3ktaz8] (score 2, diepte 5) Je weet niet waar je het over hebt kerel. Om interne misstanden te melden dien je eerst je werkgevers eigen interne procedures te volgen. In zo'n geval ben je beschermd door de wet BvK.(bescherming van klokkenluiders).

De geheimhoudingsplicht die je getekend hebt hij aanvang dienstverband houdt dus in dat je interne zaken en bedrijfsinformatie niet deeld met derden(pers bijvoorbeeld). 

Enkel in uitzonderlijke gevallen kun je interne misstanden melden aan de pers. Denk aan gevallen als dat er geen actie is ondernomen na je initiële melding, het een noodsituatie betreft enzovoort. Alleen in zulke gevallen ben je ook dan beschermd door de wet BvK.


In mijn geval is het ondertussen 8+ jaar geleden dat ik voor het laatst op een asiel locatie heb gewerkt(waaronder ter Apel). Wat betreft de misstanden die ik zelf heb waargenomen / gezien,  heb inderdaad geen zin om dit aan de pers te vertellen.
[o3bbfva] (score 2, diepte 4) Ahja goeie die was ik nog vergeten :)
[o3bc9ks] (score 2, diepte 4) Ja precies, ook bij vrijwilligers zie je het soms, maar het is zeldzaam vergeleken met bv beveiliger.

Bij de daklozen opvang zie je dat sommige beveiligers echt sadisten zijn en gewoon de dakloze pesten of erger.
[o3bezvs] (score 2, diepte 1) Alsjeblieft doe dat wel, ik denk dat dat heel erg hard nodig is. Het aantal posts en comments die hier gedeeld worden waarin mensen echt denken beter te zijn dan anderen is schrikbarend, en zelfs in deze thread zie je mensen echt hun best doen om dit soort gedrag te verdedigen, wat natuurlijk belachelijk is. 
Alsjeblieft deel je mening want je hebt gelijk en het gaat nog een keer gebeuren
[o3bamsa] (score 2, diepte 0) Sowieso ontslag. Maar misschien zou tbs ook wel op zn plek zijn....
[o3bbu64] (score 2, diepte 1 OP) Ik denk dat de gevolgen wel mee vallen. Er staat alleen dat hij niet meer werkzaam is op dit AZC.
[o3f6t26] (score 2, diepte 1) Onironisch denk ik dat ze dit bedoelen ja. 

Kijk in een gemiddelde rechtse commentsectie - zelfs op deze sub als er weer een buitenlander bad post langskomt - en je ziet dat mensen over veel ergere dingen fantaseren.
[o3be0d7] (score 2, diepte 0) Beste straf is om het paspoort om te ruilen en de beveiliger het land uit zetten
[o3c4z3h] (score 2, diepte 1) Ik vind nederland niet perse een "walgelijke rotcultuur" maar kom op, er is geen enkel land waar dit "onvoorstelbaar" zou zijn.


Als jij ook maar 1 land kan noemen waar je het onvoorstelbaar van vind dat er walgelijke dingen gebeuren ben je echt kinderlijk naïef.
[o3f72s4] (score 2, diepte 1) Als iemand dingen als dit zegt dan moet je ze toch gewoon NSBer kunnen noemen? Dat is toch gewoon een feitelijke vaststelling?
[o3br1gu] (score 2, diepte 0) Jaaa dit verbaast me niks.
[o3bynqu] (score 2, diepte 0) Inb4 beveiliger is zo'n "oprotten of aanpassen" type ondanks dat ie het gedrag toont van een middeleeuwse adelman.
[o3bbq1m] (score 1, diepte 2) Info?
[o3kmrhs] (score 1, diepte 4) Je praat onzin. Er is geen geheimoudingsplicht voor dit soort misstanden en als je echt iets wil zijn er echt veel klokkenluidersregelingen waar je gebruik van kunt maken.

Of je liegt,

Of het boeit je gewoon geen flikker wat jij hebt gedaam / wat jij hebt gezien.

Kies maar. Of ga voor de derde optie en rapporteer het. Wees een mens.
[o3m5104] (score 1, diepte 7) Je lult wederom uit je nek en doet aannames die totaal niet kloppen. Alle incidenten welke ik  heb meegemaakt zijn destijds gewoon netjes gemeld volgens de interne procedures die er voor waren.

Dat ik er geen zin in heb om er mee naar de pers te stappen klopt ook, ik zie daar persoonlijk geen nut in. Ik laat het liever bij de instanties die er over gaan. Coa, de politie etcetera.

Daarnaast waren de meeste voorvallen geen misdaden, moreel verwerpelijk dat wel en niet toegestaan volgens intern beleid uiteraard.
[o3p8ugl] (score 1, diepte 8) Stop met verstoppen achter anderen en het afreageren op derden zoals ik. Instanties kunnen niks zolang grijze muizen als jij de situatie toelaten zonder ingrijpen. Jij bent de status-quo.
[o3bx24j] (score 1, diepte 2) dit onderwerp heb ik op school gehad (psychologie). Het hele verhaal is echt ziek!
[o3epygn] (score 1, diepte 2) Sja daar valt veel van te vinden maar weinig aan te doen.
[o3c4o5x] (score 1, diepte 2) Kus mijn kontje stumper 😂
[o3dg6ju] (score 1, diepte 2) Rotland? Je mag best vertrekken hoor!🤣🤣
[o3bfoug] (score 1, diepte 1) Bron?
[o3bi94p] (score 1, diepte 0) Buiten het feit dat dit uiteraard duizend % niet kan is zeggen dat dit het 'allerergste ooit' is ook wel overdreven.
[o3h8vix] (score 1, diepte 1) ![gif](giphy|UXf2uZk1ijInyXn5A2|downsized)
[o3kuqnz] (score 1, diepte 0) Hm, de steekpartijen, verkrachtingen en moorden vind ik toch net iets veel meer schokkender.

De ophef.. ojee ..
[o3c4bap] (score 0, diepte 1) Ik woon zelf in de regio en heb echt een gore kut hekel aan 60% van het tuig wat daar zit…. Echt maar deze gast haat ik echt ! Wat ben jij een Mongool zeg, wat wil je hier mee bereiken dat de afstand tussen de asielzoekers en de bevolking nog groter wordt ? Zielig mannetje ?? Of hebben we het allemaal mis en was het een weddenschap
Of zo ? (Nog heel dom trouwens)
[o3b92np] (score 0, diepte 1) [Quis custodiet ipsos custodes?](https://nl.wikipedia.org/wiki/Quis_custodiet_ipsos_custodes%3F)
[o3d1j5y] (score 0, diepte 6) Laat ik nou net onder Ter Apel wonen, wie is er nou geinformeerd en wie niet, by design btw.
[o4kmon3] (score 0, diepte 2) Ik ben de best
(20 reacties met lagere score weggelaten)

=== THREAD 1wuyp29 ===
SUBREDDIT: r/nederlands
DATUM: 2026-10-01  SCORE: 10  REACTIES: 85
TITEL: Goede sneakers voor brede voeten
POST (source_id=post):
Ik ben vrouw en zoek goede maar ook gewoon leuke en enigszins betaalbare sneakers die geschikt zijn voor brede voeten met een hoge wreef. Daarbij moeten ze ook een stevige hielkap hebben en een goede demping. Ik heb na te lang lopen op all stars (wide fit) en teenslippers last van het gevoel van een steeds verzwikkende enkel. Het is dus tijd voor meer steun en stabiliteit.

Ik heb net een paar New Balance sneakers (740 unisex) weer ingepakt om terug te sturen naar Zalando omdat ze echt te smal zijn. Jammer! 

Ik weet dat ze op de site van New Balance verschillende breedtematen hebben maar ik vind ze zo prijzig + retourneren is voor eigen rekening, en ik ben nog teveel zoekende.

Heb jij brede voeten? Zo ja.. wat voor schoenen draag je?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[pd78hvy] (score 45, diepte 0) Als je nu last hebt en toe bent aan steun en stabiliteit rondom je voeten, dan is het misschien tijd om eens naar een fatsoenlijke winkel te gaan i.p.v. online sneakers bestellen.
[pd799k9] (score 8, diepte 1) Beste antwoord. Ga passen.
[pd79xuk] (score 7, diepte 1) Hahaha, jij bent zeker de gemene tante van de kring verjaardag.
[pd79umk] (score 6, diepte 0) Heb je je voeten wel eens op laten meten in een schoenenwinkel? Schoenen komen in breedtes aangegeven met letters. Als je die weet komt je vaak wel een stuk verder. Adidas had vroeger volgens mij verschillende breedtematen.
[pd7rm6k] (score 5, diepte 1) Sowieso
[pd7dbbv] (score 5, diepte 0) Ik draag eigenlijk enkel 'barefoot' schoenen. Dat is een beetje een niche, maar binnen die niche is er wellicht iets te vinden. Helaas weinig winkels die het aanbieden. 

Demping is natuurlijk wel een dingetje. Misschien advies vragen bij deze mensen? 

[https://www.barefootandmore.nl/dames/sportschoenen/hardloopschoenen?attr\_Breedte=Breed](https://www.barefootandmore.nl/dames/sportschoenen/hardloopschoenen?attr_Breedte=Breed)
[pd78sgg] (score 4, diepte 0) Etnies, en sowieso een hoop skate merken volgens mij. Vans zijn ook erg fijn in ieder geval.
[pd7da5f] (score 4, diepte 0) Ik gebruik alleen maar barefoot schoenen. Had altijd ontzettend last van hielspoor en dat is daarmee echt compleet verdwenen, bijkomend voordeel is dat ze ook breed zijn aan de voorkant. 

Je hebt een goede winkel in Arnhem (Barefoot and More) waar je gewoon kunt passen.
[pd7fvc1] (score 4, diepte 0) Zelf geen brede voeten maar kijk eens naar Hoka’s, die hebben wel brede modellen waar mijn vrienden met bredere voeten blij mee zijn. Betaalbaar zijn ze niet per se, maar je krijgt er veel voor terug. 

Ik heb zelf de Hoka Bondi 9 maar ook Bondi 8 en de Cliftons zijn populair. Het zijn meer hardloop/loopsneakers dus de demping is heel fijn. Vooral de Bondis zijn top voor mensen die gewoon lang op hun benen staan (zorg, horeca, of op vakantie waar je veel slentert).
[pd77jmp] (score 3, diepte 1) ![gif](giphy|ZHWwqktviL3sA)
[pd7jljq] (score 3, diepte 2) Als je blaren wil tegengaan , eerste dunne sokken en dan dikke daarover. Ooit eens gelezen en helpt echt , ik doe het altijd bij het instappen van nieuwe wandelschoenen.
[pd7gfs8] (score 3, diepte 1) Vans hebben zeker geen steun.

Adidas Superstars kan ik aanbevelen. Deze hebben wel natuurlijke steun in de zolen
[pd7cush] (score 3, diepte 0) Zoiezo alle skateschoenen, Vans, etnies, DC als ze die nog maken haha. 

Adidas heeft af en toe ook skatemodellen die ik aankrijg, Nike, sketchers, replay etc vallen overwegend te smal in de breedte maar heb nu een paar Nike air jordan 4 retro die ik wel aankrijg. Zaten een beetje krap maar leken een goede uitloopkans te hebben dus de gok gewaagd en die zitten fantastisch. Ook een tijd geluk gehad met British Knights, deze wel een maatje te groot maar dan lopen ze als sloffen, heerlijk. 

Ik heb dusdanige brede voeten en een kleine maat dat schoenen kopen echt een nachtmerrie is, veelal loop ik meerdere schoenenwinkels af voor een paar en als het echt goed zit ga ik terug om nog een paar te scoren zodat ik weer even vooruit kan. Gelukkig zijn nu de meer chunky en skatemodellen weer in de mode dus dat is geluk!
[pd7kre4] (score 3, diepte 0) Ik draag ondertussen al heel jaren de Meindl Palermo.   
Ik heb ook een brede voet en hoge wreef. In een gewone schoenwinkel vond ik nooit sneakers die pasten. Ik ging dan op een bepaald moment naar een gespecialiseerde winkel, daar vond ik wel schoenen, maar had het gevoel dat ze qua maat te klein waren (nochtans de maat was goed). Dan ben ik eens van ellende/miserie bij AS Adventure (ik woon in België, in Nederland is dit dan Bever) geweest, mijn probleem uitgelegd. Ze gaven mij een paar schoenen om te passen, schoenen zaten direct goed en ik heb nu altijd een reservepaar in huis. Ik doe deze continue aan, ze zitten echt geweldig. 

https://www.bever.nl/p/meindl-palermo-lady-gtx-wandelschoenen-dames-comfort-fit-HAACF00001.html

Dit jaar wel op zoek gegaan naar nog andere sneakers, Mephisto heeft ook goede sneakers, maar daar is het echt passen
[pd7z1nq] (score 3, diepte 0) Ik weet dat heel veel mensen het een oude mannen merk vind maar sketcers
[pd77ex9] (score 2, diepte 0) ![gif](giphy|kZiF7hNKSWFQgZUESs)
[pd77w6v] (score 2, diepte 0) Vans! Ik LEEF op die schoenen.  Zeker die Knu variant. Maar je moet wel van de style houden.
[pd798ay] (score 2, diepte 1) Ik houd van vans.

Je hebt nu ook vans voor de oude mensen, met extra dikke binnenzool er in zonder dat het er zo uit ziet aan de buitenkant. Dit zijn de enige varianten die ik dus niet gelijk zonder inlopen kan dragen, maar ik heb erg snel last van blaren bij schoenen. De classic blijft voor mij het fijnst, instappen en lopen maar
[pd78j0t] (score 2, diepte 0) Er bestaan nog steeds schoenenwinkels, ga daar anders passen. Dan heb je ook geen risico voor het terugsturen. Kan je ze daarna eventueel goedkoper online zoeken.
[pem9fsd] (score 2, diepte 1 OP) Ik heb de Asics Gel NYC gekocht en ben er heel blij mee. Geen last meer van mijn enkel en breed genoeg. Gewoon unisex. Super! Would recommend! Dank!!
[pd7aj79] (score 2, diepte 1) Dit! Bij ons in de buurt doet Bever dit, die zoeken dan ook meteen schoenen voor je uit uit hun assortiment.
[pd7dv51] (score 2, diepte 0) Naar een zaak gaan passen of een podoloog. 

En dan niet een zaak waarbij iemand de maat en prijs van de schoen op kan lezen maar een goede fatsoenlijke schoenenwinkel.
[pd7ipud] (score 2, diepte 1) Hier nog twee Hoka liefhebbers, met beide brede voeten. Clifton 9/10 zijn echt top qua zachtheid, lijkt wel alsof je op wolken loopt.
[pd9uls9] (score 2, diepte 1) Die heb ik als vrouw met brede voeten ook! Valt wel een maat kleiner bij mij. Ze zijn er in veel verschillende kleuren
[pd7jsaq] (score 2, diepte 0) Ik heb een brede voet en hoge wreef, maar zweer juist bij New Balance (wel een maat groter).
[pdkpk8f] (score 2, diepte 1) Leuke schoenen zeg! Wandelschoenen zijn de way to go. Ik snap vaak niet wat mensen er zo erg asn vinden qua looks, en bovenal vind ik comfort het belangrijkst! Ik heb nu de lowa renegade wide als dagelijkse schoen. De normale renegades pas ik niet goed in, maar deze zitten als gegoten!
[pdmbq3s] (score 2, diepte 2) Die zien er ook goed uit. Zijn die wat breder?
[pdrg97a] (score 2, diepte 3) Thanks! Yes, vandaar de "wide" ;)
[pdrmzyt] (score 2, diepte 4) Bedankt. Dan gaan we eens zoeken naar deze schoenen.
[pdsyknu] (score 2, diepte 7) Aha. Ik heb dan weer alleen hogere sokken en in de winter zelfs kniekousen af en toe haha. Draag eigenlijk alleen nog maar falke. Veel te duur, maar dan heb je ook wat
[pd80qfu] (score 2, diepte 0) Ik ben man met brede voeten, New Balance 574 heeft t altijd wel goed gedaan bij mij, en verder waren saucony sneakers de meest comfortabele schoenen die ik gehad heb, ook lekker breed.
[pd7alf3] (score 1, diepte 1) ![gif](giphy|ifH8IOSp9gyPM1oGA4)
[pd82yja] (score 1, diepte 3) Thanks voor de tip, ga ik zeker uitproberen!
[pd8qj3j] (score 1, diepte 1) Yup. Kunnen nog steeds sneakers zijn dat wel
[pem90ff] (score 1, diepte 1 OP) Je hebt helemaal gelijk
[pd78m7f] (score 1, diepte 0) Ik heb asics gel nyc, ben wel een man maar die zitten fijn! New balance heb ook ik teruggestuurd.
[pd7abfm] (score 1, diepte 0) Vriend van me heeft dit ook, die is heel tevreden met zijn Mizuno Wave Rider Beta. Hoe ze eruit zien moet wel een beetje je ding zijn, maar de mijne lopen in ieder geval zo lekker als mijn fav New Balance model.
[pd7buk0] (score 1, diepte 0) Als een hele brede-voeter is New Balance mijn merk. 

Als je schoenmaat ook bestaat in herenmodellen kan je die eens proberen, de heren schoenen worden gewoonlijk op een bredere lijst gemaakt.

De 880 fresh foams in 43-4E draag ik voor lang stappen of de hele dag recht staan. De MiUS 990v5 42.5-2E of 993 43 draag ik op rustigere dagen. Vooral de laatste 2 opties zijn niet goedkoop, maar tijdens solden kan je ze goedkoper vinden (BSTN, asphaltgold, afewstore, …). 

De NB 9060 is een brede schoen (zelfs zonder een speciale breedte maat), maar je moet wel fan zijn van het design… Kan je vaak in solden vinden op zalando. 

NB België heeft een gratis retour policy. Lijkt me vreemd dat het voor jullie anders zou zijn.  Ik zie bovenaan de NL pagina “gratis retourneren - gratis verzending vanaf 100€”. De gratis retour is voor zover ik weet ook geldig onder 100€.
[pddc7jy] (score 1, diepte 1) +1 voor DC. Ik heb in 2008 een paar gehad die me zo goed bevallen zijn dat ik in 2014 nog 3 paar (uit 2008 dus) besteld heb die nog her en der in voorraad waren. Ik ben vorig jaar begonnen aan mijn laatste paar...
[pd7e8l6] (score 1, diepte 0) Ik heb een hoge wreef en brede voeten, wat een hel om schoenen te vinden. Vrijwel alle Vans passen goed, ook de hoge modellen.
[pd7e9wx] (score 1, diepte 0) Er zijn ook lage wandelschoenen die eruit zien als sneakers. Bijvoorbeeld van Adidas. Ik zweerde bij Reebok maar dit model is helaas uit productie. Ik heb denk ik wel 4 of 5 paar versleten (ik loop erg veel).
[pd7fbb9] (score 1, diepte 0) Brooks
[pd7fmik] (score 1, diepte 0) ASICS Japan S PF .... 

En het kan sowieso geen kwaad om je maat te laten aanmeten. Links is bij mij net iets anders als rechts.  
Bever en Intersport kunnen dit voor je doen. Koop je er geen schoenen, dan weet je wel waar je staat..
[pd7j9vd] (score 1, diepte 2) Ja de Bondi’s ook! Heerlijk! Ik heb bij lang staan/lopen altijd snel last van m’n rug, en met de Hoka’s heb ik drie weken dagelijks lopen in Japan overleefd. Ik heb één dag van schoenen gewisseld (en gelijk spijt gehad van die keus). Ik ga nooit meer terug.
[pd9u2lx] (score 1, diepte 1) Ik heb heb op de Challengers 
veel lange afstanden gelopen. Speedgoats zijn voor mij helemaal perfect in de bergen en trails. Doe ze ook vaak aan naar mijn werk.
[pd7g6gx] (score 1, diepte 0) Als man zijnde en in het bezit van grote voeten: Karhu fusion 2.0

Heb er ook steunzolen in. 

Na jarenlang klooien gebruik ik nu AI om de dimensies van een goed passende schoen te vergelijken met een potentieel nieuw model. Dit werkt tot dusver aardig.
[pda36cv] (score 1, diepte 2) Bij mij vallen ze een halve maat groter. Waar ik achter ben gekomen is dat bij de Fusion 2.0 het materiaal ook nog uitmaakt voor welke maat je nodig hebt.
[pd7glp4] (score 1, diepte 0) Met schoenen ga ik naar de winkel , weet je echt of je ze past
[pd7gx3q] (score 1, diepte 0) Ik ga eens een andere tip dan anderen geven, barefoot schoenen. En nee je hoeft niet direct op five fingers door het leven, er bestaan ook medium-gewone :)

Gewoon lopen zoals het bedoeld is versterkt je spieren in je voet en been en verbetert je hele houding. Dus niet die slappe hap nog verder ondersteunen en klem zetten, maar gewoon bewegen en sterker worden. Zal je meer profijt van hebben.

Mij heeft het in elk geval van wat nek/schouder klachten af geholpen en mijn algehele houding en voetenwerk is sterker, waar ik weer van profiteer bij trailrunning.

Je zal uiteraard wel gepest worden op werk vanwege je schoenen. Maarja, dat moet je ervoor over hebben.
[pd7h0xr] (score 1, diepte 0) Deze zijn erg mooi

![gif](giphy|fROKFCrpPDcKk)
[pd7hp6g] (score 1, diepte 0) Hobi bear of schoenen met een mesh bovenkant
[pd7hvr5] (score 1, diepte 0) Mijn vrouw heeft best brede voeten en draagt eigelijk alleen Skechers. Die zitten echt prima volgens haar.
[pd7ihmy] (score 1, diepte 0) Hier ook brede poten en hoge wreef.
Skechers Uno zijn echt top voor mij, ook te krijgen in wide fit maar de normale zitten al goed voor mij.
[pd7jblx] (score 1, diepte 0) Kom vaak bij mizuno wave rider of wave prodigy uit.
[pd7jh4h] (score 1, diepte 0) Reebok club c
[pdsf71o] (score 1, diepte 5) Ben benieuwd of je ze past! Draag je ook wandelsokken? Ik vind dat zelf altijd wel prettig
[pdshbff] (score 1, diepte 6) Ik draag altijd wandelsokken (wel de lage versie, type enkelkousen).
[pd7levr] (score 1, diepte 0) sketchers heeft ook een paar modellen die speciaal voor brede voeten zijn.Ik (man) heb voor lengte ongeveer 46 en breedte ongeveer 48 en de sketchers heb ik bij de brede gewoon 46 dus geen pijn meer bij mijn voetboog
[pd7q2jl] (score 1, diepte 0) Scatchers heeft die "brede pasvorm"-modellen. Ik heb hetzelfde probleem en "brede pasvorm" modellen werken prima. Ik weet niet of andere eigenschappen geschikt zijn voor jouw doeleinden.

*Edit: vertaald uit het Engels*
[pd7r4q4] (score 1, diepte 0) Ascics heeft een Japanse serie aan schoenen waar wat bredere exemplaren tussen zitten. Maar om eerlijk te zijn adviseer ik je naar een goede schoenenwinkel te gaan nu ze nog bestaan.
[pd7szgl] (score 1, diepte 0) Barefoot sneakers, die zijn gevormd naar je voet en met een dunne zool loopt het echt heerlijk.
[pd7ubpr] (score 1, diepte 0) Goede schoenen kosten iets meer maar gaan ook langer mee.
[pd7xjkx] (score 1, diepte 0) Ik heb merrell sneakers gekocht, bij decatlon vind je ze ook. Ik was tevreden van de wandelschoenen, en wilde goede ondersteuning omdat ik dagelijks best wat kilometers stap.
[pd83qkw] (score 1, diepte 0) Als je goeie sneakers hebt gevonden ga dan ook eens langs bij een podotherapeut! Ik en mijn vrouw zweren erbij.
[pd8728l] (score 1, diepte 0) Vrouwen schoenen zijn echt belachelijk smal. Ik draag al jaren heren schoenen om die reden.
[pd8f5bm] (score 1, diepte 0) Adidas for the win, en dan vooral de Handball Spezial series.
[pd8f6a4] (score 1, diepte 0) Ik heb korte maar brede voeten en een hoge wreef. Qua lengte zou ik een 38,5 nodig hebben maar door de breedte kom ik meestal uit op maat 40. Sommige fila's passen ok. Niet het allerbeste maar wel de meest budget vriendelijke die ik heb kunnen vinden
[pd8lnnx] (score 1, diepte 0) Kijk bij mannen schoenen, zijn fsr breder
[pd9ab2u] (score 1, diepte 0) Heb je Sun69 of Hoff
[pd9rdwz] (score 1, diepte 0) Sioux.de. Skechers extra-wide werkt ook voor mij, alleen vind ik de kwaliteit van Skechers belabberd. Dat zijn echt schoenen voor een paar maanden gebruik
[pda18tb] (score 1, diepte 0) De new balance 5740 deden het goed bij mij. De 574 (en ook 740 en 9060, daarna ben ik gestopt met passen in de winkel) was helaas een smallere teleurstelling. 

Skechers wide fit of Jack Wolfskin (een maat groter) passen mij wel. Maar het is niet helemaal mijn smaak waardoor ik helaas wel comfort boven persoonlijke stijl moet zetten. Heb nog niets verder kunnen vinden.
[pdaaajr] (score 1, diepte 0) Skechers hebben een aantal schoenen die specifiek 'wide' aangemerkt staan, juist voor mensen zoals jij. Google maar eens op Skechers wide. Ik heb ze ooit eens per ongeluk besteld, dus kan bevestigen dat ze echt wijzer zijn. Zagen er dus op het oog niet wijder uit, maar waren dat wel.
[pdbg3n0] (score 1, diepte 0) Ik heb ook een brede voet met hoge wreef en geloof me...je kan beter een duurder paar kopen dat langer meegaat
[pdcstpt] (score 1, diepte 0) Reebok!
[pdd156a] (score 1, diepte 0) Ik heb precies hetzelfde probleem en zweer bij sketchers, die met luchtkussentjes. Heb recent nog andere merken geprobeerd, maar dat is net als lopen op een plank.
[pdf3d3q] (score 1, diepte 0) Heey, ik herken deze uitdaging. Ik heb het zelfde probleem als jij, daarnaast twee verschillende maten in m'n voeten en een gebroken leest. En breedtemaat k(!),geloof ik. Nou... ik heb geloof ik wel 100 schoenen geprobeerd. Niks zat goed.
Ik heb het geluk ik een voetencentrum vond waar de podotherapeut mee kon kijken bij het passen. Ze verkopen er ook schoenen. Je maakt een afspraak en ze helpen je te kijken wat voor jou werkt. Er ging een wereld voor me open, hier past een schoen me in één keer, had ik dat maar eerder gedaan... ik heb zo vaak pijn aan mijn voeten gehad. Nu sinds kort dus echt vette speakers van xsensible of zoiets. Xensible. Sensible. Ehhh. Zou het zo ff voor je opzoeken. Zo chill!
[pdf8h5d] (score 1, diepte 0) Ben erg fan van Hoka. Zeker de moeite waard om eens te passen.
[pdgfjqh] (score 1, diepte 0) New balance maar kies een ander model, bijv 530 mr werkt fantastisch!’ Nooit meer last!
[pdk2pff] (score 1, diepte 0) Ik heb zelf goede ervaring met Sketchers
[pdlpwnq] (score 1, diepte 0) Ik wilde letterlijk mijn favoriete schoenen, de new balance 740 aanraden🤣 hmm heb je de 2002 wel eens geprobeerd? Die is nog breder aan de voorkant. Wel meer een foam zool dan echt hard rubber van de 740. Ik draag eigrnlijk al een aantal jaar alleen deze twee modellen. Ik heb vroeger ook veel Adidas superstar gedragen die vond ik heerlijk. Totdat ik new balance ontdekte nu wil ik niks anders meer
(6 reacties met lagere score weggelaten)

=== THREAD vzmmaj ===
SUBREDDIT: r/thenetherlands
DATUM: 2022-07-15  SCORE: 29  REACTIES: 81
TITEL: Blote voeten?
POST (source_id=post):
Valt het jullie ook ineens op dat er heel veel mensen op blote voeten buiten lopen? Kan me niet herinneren het ooit eerder zovaak gezien te hebben, een stuk of 10 deze week..
Zit hier een filosofie achter of gewoon een trend? Is het niet gevaarlijk met glas enzo?
Iemand die het doet die wil delen waarom?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[igaaqn6] (score 73, diepte 0) Dit jaar nog niemand gezien, maar ik meen me te herinneren dat die zo'n 10 jaar geleden ineens een trend was in een bepaalde subcultuur. 
Er zat toen zeker wel een gezondheidsreden achter, dat het natuurlijker loopt dan op een zooltje van welk schoeisel dan ook.

Maar in de prehistorie liepen we vooral op zand, gras en bosgrond en niet op harde klinkers en beton.
[igb3nvp] (score 64, diepte 0) # Ja ik hier! Present!

 Ik loop heel veel op blote voeten. 

&#x200B;

&#x200B;

Reden: 

Vroegah als kind wilde ik dat al maar dat mocht niet van mijn ouders. Gevaarlijk, veel glas op straat, en veel poep.

&#x200B;

&#x200B;

Paar jaar geleden mijn voet gruwelijk gebroken en kort erna vaak last van zere voeten. Oplossing bleek: Op blote poten lopen. Heerlijk! En 1) er ligt helemaal niet zo gek veel troep op straat, ik sta eigenlijk niet in vieze rommel of scherpjes 2) ik heb meestal wel iets van een ballerina op zak ofzo voor als er ergens een onherbergzaam stuk is (in de randstad, hahahahahahahahahaha) 3) als ik nu ergens intrap, dan heb ik niet mijn moeder naast me staan die zegt dAt Is jE eIgEn ScHuLd en het gaat van mn eigenbetaalde eigenrisico af dus who cares 4) ik heb dus mijn poot gebroken op een rotmanier, met schoenen aan en alles. Ik heb met mondkapje en handjes wassen en social distancing covid, covid-gerelateerde longschade en nu long-covid opgelopen. Ik rook niet, ik drink amper, ik leefde tot voor kort heel gezond, en toch helemaal naar de klote nu. Weet je: Yolo. Ik neem het risico wel. Ik vind het top lopen. Geen zere poten, het waggelt prima, de risico's vallen alleszinds mee, en ik was gewoon thuis keurig mijn voetjes klaar geen punt zo gedaan.

&#x200B;

&#x200B;

Dus, Dat. Uiteraard ga ik nu geheid aankomende maand in een drol, een roestige spijker en een handje glas stappen, maar de afgelopen vier jaar was er niks aan de hand. Krijg er zelfs geen schimmel van, iets wat je van het zwembad niet kan zeggen. 

&#x200B;

**TL;DR: Ik ben een hobbit, AMA**
[iga8uci] (score 50, diepte 0) Ja, ik zag afgelopen week een knul op blote voeten door de stad lopen. M'n eerste gedachte was: da's niet handig langs de cafés met glas op de grond.
[igd2zkg] (score 46, diepte 1) Als puber ben ik ooit eens blootvoets naar de lokale supermarkt gelopen, want zomer en dichtbij. "Je bent je schoenen vergeten aan te trekken," zei een man die te welgekleed was voor de achterstandswijk waarin ik woonde. Jasje-dasje, u kent het wel, waar de rest van de wijk het liefst liep in joggingsbroeken en badslippers.
"Jij bent ze vergeten uit te doen," antwoorde ik puberaal-bijdehand.

Ter kennisneming: 's zomers zijn de koude tegels in de supermarkt fantastisch!
[igavs77] (score 32, diepte 0) Ik vind het heerlijk om op blote voeten te lopen maar buiten eigen huis en tuin doe ik dat niet. Bang voor glas en hondenpoep. Maar toch is niets lekkerder dan na een tijdje op ruwe tegels te hebben gelopen op gladde plavuizen te gaan staan. Daardoor lijken supermarktvloeren me heerlijk op blote voeten, maar mijn gevoel voor decorum is te groot.
[igat9yq] (score 18, diepte 0) Komt vast door de inflatie. Die mensen kunnen geen schoenen meer kopen.
[igacrw8] (score 15, diepte 0) Is me niet opgevallen. Op straat zou ik het zelf niet doen. Thuis zweer ik er echter bij. Vind het vreselijk om schoenen en sokken te moeten dragen.
[igajpgc] (score 11, diepte 1) Ja zoiets zag je toen ineens opkomen. (Die trend) iemand die ik goed kende is daar helemaal ingedoken en liep buiten zijn werk om (buschauffeur) altijd zonder schoenen.

Ik zeg zonder schoenen omdat het niet blootsvoets was. Je hebt van die "fivefingers" schoenen, een licht membraam zodat je niet zomaar met je voet in het vuil loopt en 5 uitsteeksels voor je tenen.

Anyway, inderdaad vanwege de filosofie dat de mens gebouwd is om zonder schoenen te rennen/lopen.
Het zou me niets verbazen als deze trend nu weer naar voren komt, die mensen komt vaak uit dezelfde hoek als veganisme en spiritualiteit.
[igdndp4] (score 11, diepte 2) vandaar dat ze al snel ook schoenen (sandalen)  uit gingen vinden!
[igcz5sa] (score 10, diepte 2) Damesschoenen zijn denk ik ongezonder, met hun niet-verende zool en vaak een hak. EN dan je voeten nog in een fuckpositie. 

&#x200B;

Als je op blote voeten loopt ga je anders lopen. Dat kan je ook zien op middeleeuwse prenten trouwens. Of het per se gezonder is weet ik niet, maar als je denkt dat de modern schoeisel zo gezond is: Hahahahaha. nee. Ja, als je altijd op sneaks loopt misschien. Wat voor heel veel mensen niet mogelijk of wenselijk is. Want cultuur.
[igajbtd] (score 10, diepte 0) Klinkt bar onverstandig. Tenzij je houd van dat heerlijke gevoel van bloed en glas tussen je tenen. Ieder zijn ding.
[igb4hy3] (score 9, diepte 0) Ik doe dit met regelmaat als het warm is. Het is natuurlijk fijner in de natuur, maar in de stad ook prima.

Zit niet echt een modegevoel achter, laat staan een diepgewortelde levensfilosofie. Ik vind het gewoon wel fijn, soms, om de grond te voelen waar ik op loop. Ik doe het vaak genoeg dat ik een klein laagje eelt heb, waardoor stenen nou ook weer niet zo'n marteling zijn. Ik ben het tamelijk gewend, en dan voelt het ook als onnodig gedoe om schoenen aan te doen als ik even snel naar de winkel moet oid.

Glas en hondenpoep: als je echt geen 3 stappen kunt zetten zonder er in te stappen, zou ik echt eens gaan verhuizen. Natuurlijk moet je een beetje meer uitkijken waar je loopt, maar je loopt met je schoenen toch ook niet 24/7 door glas en poep te stampen, hoop ik? En dat je dan zingt van "driewerf hoezee voor de uitvinder van de schoen die mij in staat heeft gesteld om een dansje te doen op een hondendrol"? Ik bedoel, valt al geen metrum in te krijgen, ten eerste.

Waarom? Idk, voelt gewoon wel chill soms, iets met bewust de grond voelen waar je op loopt of zo. Dit neigt al snel naar iets zweverigs, maar zodra mensen daaraan beginnen lopen mijn hobbitvoetjes liever de andere kant op.
[igbc440] (score 8, diepte 1) Idd, met harde niet meegevende ondergrond kan het op den duur niet gezond zijn lijkt me.
[igczqvu] (score 8, diepte 1) Damesschoenen hebben doorgaans helemaal geen demping, nette herenschoenen ook niet, en dan hebben we het nog niet over hakken gehad. Ik bedoel, als we dan over het gezondheidsaspect gaan hebben, dan denk ik dat er met het veranderen van regulier schoeisel en cultuur daaromheen aanzienlijk meer gezondheidswinst te behalen is.

&#x200B;

Overigens is op blote pote lope zonder demping volgens mij helemaal niet zo heel slecht. Vergeleken met je voeten in te nauwe schoenen vrummen met te harde zool en daar op te gaan stappen met amper afwikkeling. 

&#x200B;

&#x200B;

Ik vind het gezondheidsargument een beetje flauw, gezien hoe ongezond reguliere schoenen zijn. Eerlijk gezegd. En hoe er op gezond schoeisel als DE CROC wordt afegeven.
[igdn4pd] (score 8, diepte 2) Je voet afwikkelen is ook al slecht, want het zorgt voor een landing op je hiel, en omdat dan ongeveer je been gestrekt is, doet de vering van je lichaam het slecht. Zeker bij rennen is dat mogelijk de grootste reden waarom de moderne mens die rent zo vaak blessures krijgt. Die Nike air hebben te weinig air om de vele Gs van een landing om te vangen.

Op de bal van je voet landen (met een kromming in de knie), dan je hiel neerzetten zorgt ervoor dat het minder doordreunt door je lichaam. Je moet alleen spieren kweken en heel langzaam opbouwen. En door dat blootvoets te doen, voel je goed wanneer het weer tijd is om te stoppen.

Dus op blote poten lopen is niet slecht, maar luister naar je lichaam.
[igadacs] (score 8, diepte 0) Heb het nooit echt gezien, hooguit als iemand even de bak aan de straat zet of naar de afvalcontainer loopt. Zelf loop ik in en rond het huis altijd op blote voeten maar nergens anders omdat je niet weet wat er op de grond ligt.
[igan54f] (score 8, diepte 0) Collega gehad die dat deed, het kantoor zat in het centrum van A'dam. Hij zei nooit problemen te hebben met glas e.d. Ken ook iemand die het bij van die teenschoenen houd, Het is voor beide een gezondheid ding, een natuurlijkere houding tijdens het lopen.

Het zal vast nu ook een trend zijn, bepaalde influencers die het promoten, maar is al langer een ding.
[igffpww] (score 8, diepte 2) Dit leest als literatuur van de oude stempel, haha. Ik vind mooi.
[igb7z9f] (score 8, diepte 1) Ja, hier herken ik mijzelf ook in. Bijzonder hoe bang mensen zijn voor glas en hondenpoep op de grond. In de twee jaar tijd dat ik nu zoveel mogelijk op blote voeten loop, nog niet meegemaakt dat ik echt veel glas heb moeten ontwijken. En dagelijks je voeten even afspoelen is voor mensen met of zonder schoenen eigenlijk altijd wel nodig.

Altijd al heb ik last gehad van korte en brede voeten die niet zo goed in trendy schoenen pasten. Sinds twee jaar geleden tijdens de eerste lockdowns ben ik gewend geraakt aan minder schoenen dragen en nu vraag ik mij af waarom zou ik eigenlijk schoenen aan doen?
[igaxytq] (score 7, diepte 1) Boots theorie naar z'n logische extreem getild.
[igdn809] (score 6, diepte 1) Stenen zijn ook al ontzettend oud. Denk dat ze die in de prehistorie ook vaak tegen kwamen.  :)
[igczboy] (score 6, diepte 1) Ik weet niet waar jij woont, maar ik loop niet de hele dag door glas te crunchen ofzo. Heb je hier met fietsen ook last van? Lijkt me prijzig worden, steeds nieuwe schoenen en fietsbanden moeten kopen. Ik zou toch eens met je buren gaan praten.
[igctxd9] (score 6, diepte 2) >Waar ben je precies bang voor?

Voeten. Wel op blijven letten hè.
[igd7lxq] (score 6, diepte 1) Ik heb dit opgelost met barefoot schoenen. Dan lijkt het echt net alsof je op de blote voeten loopt, zo flexibel. Zeer dunne, flexibele zool waar je ook heel veel ondergrond doorheen voelt. Maar je bent wel beschermt tegen viezigheid en andere troep.
[igdenyo] (score 6, diepte 3) Je hebt tegenwoordig heel veel verschillende schoenen hierin. Ook steeds meer sneaker-achtige modellen. Gelukkig niet alleen maar de fivefingers. 
Ik koop ze bijna altijd hier https://www.barefootandmore.nl/  Of wanneer ik de maat weet ergens online.

Binnen voel je inderdaad niet veel van de ondergrond. Buiten wel, maar is per merk verschillend. In mijn vivobarefoot voel ik heel veel. Op m'n leguano's wat minder, maar die zitten heerlijk soepel (mijn favoriet). Maar voel de randjes van de stoeptegels en een gemiste eikel in de herfst is soms wat minder fijn. Door het bos ermee is heerlijk, wortels, alles voel je en "krult" je voet natuurlijk omheen.
[igd3wk7] (score 6, diepte 0) Woont zeker in hippie centraal? Geen last van hier in het noorden
[igbvuds] (score 5, diepte 0) ik kan me er iets bij voorstellen: de afgelopen twee jaar heb ik uiteraard veel meer thuis gezeten dan gewoonlijk, en als je de hele dag thuis zit en even een vuilniszak weg moet brengen, dan ga ik niet helemaal moeite doen om schoenen aan te trekken, gewoon mijn badslippers. 

Op den duur worden zelfs badslippers teveel moeite, dus dan maar blote voeten. En op den duur breidt het zich uit naar niet alleen vuilniszak om de hoek dumpen, maar ook het plastic afval 2 straten verderop dumpen, of waarom niet ook naar de supermarkt die maar 3 straten verderop zit. 

Kan me goed voorstellen dat mensen op die manier tijdens corona enzo meer schijt aan hebben gekregen om speciaal extra moeite te doen als ze even de deur uit moeten, en dat ineens escaleert naar overal heen op blote voeten. 

Magoed, is maar een theorie van mij, mensen hebben vast andere redenen.
[iga7sop] (score 4, diepte 0) Mij is het niet opgevallen. Weet wel dat er een Britse Tiktokker is die op blote voeten loopt en mensen uitdaagt om het ook te doen (@georgewoodville). Weet alleen niet of hij met zijn 300k volgers de wereld aan het veranderen is.
[igdixer] (score 4, diepte 1) Het schijnt ondanks de harde ondergrond wel beter te zijn. Naar wat ik gehoord heb lopen mensen met (verende) schoenen op zo’n manier dat iedere stap doordreunt naar je knieschijf. Vanwege de schoenen voel je het niet zo snel, maar je knieën slijten er wel sneller door. Als je op blote voeten loopt heb je nul demping, waardoor je geforceerd wordt om alle klappen met je voet zelf op te vangen. Dat schijnt juist effectiever te zijn dan verende schoenen, waardoor je knieën juist minder snel slijten, ongeacht de ondergrond. Nou was dit wel meer van toepassing op hardlopen dan wandelen, maar er zit iets in.
[igans9c] (score 4, diepte 0) In breda was altijd een man die op blote voeten liep/fietste, echter liep hij ook rond met een korte broek en tanktop in mid winter. 
Dus echt vreemd is het niet ofzo, maar anders dan het normale is het zeker
[igb1pk9] (score 4, diepte 0) Ik geef de volgende reden:

Het is fokking warm.
[igmp1fk] (score 3, diepte 2) >die mensen komt vaak uit dezelfde hoek als veganisme en spiritualiteit.

Ugh, als veganist heb ik echt een baggerhekel aan zweefteef-vegans.
[igb11zw] (score 3, diepte 1 OP) Jaa die teenschoenen kan ik me ook nog herinneren! Die zie ik eindelijk nooit meer..
[igfc8e2] (score 3, diepte 1) Het centrum van Amsterdam is toch wel de meeste ranzige plek waar je zonder schoenen kan lopen
[igapb5h] (score 3, diepte 0) Vooral kinderen, maar dat is niet ongebruikelijk in de zomer
[igdacva] (score 3, diepte 2) Maar voel je dan echt dat contrast van ruwe tegels en plavuizen? Op sokken is dat al weg. Ik neem aan dat je van die schoenen met losse tenen bedoelt en daar wil ik ook liever niet mee gezien worden.
[igb1aue] (score 3, diepte 1 OP) Dus het lag toch niet aan mij 😂
[igb7lg4] (score 3, diepte 3) Ik heb er laatst ook 1 gespot op station A'dam Zuid
[igbdpwa] (score 3, diepte 0) Ik loop regelmatig op blote voeten buiten huis. Meestal maar een klein stukje. Even de kinderen zoeken, container halen/brengen en straks op de camping loop ik het liefst de hele dag op de blote voeten. Het is makkelijk, in mijn leren sandalen krijg ik toch zweetvoeten en bovendien is het lang niet slecht voor de spieren in de voet. De eerste paar keren even goed uitkijken waar je loopt, even eelt kweken. Je went ook snel aan het opletten uiteindelijk doe je dat vanzelf ook met schoenen aan.

Ik heb normaal, met schoenen steunzolen nodig en zonder schoenen heb ik minder last van mijn voeten.
[igc4p5m] (score 3, diepte 0) Corona effect: Al die tijd thuis zonder schoenen was lekker. So fuck shoes.
[igd6oer] (score 3, diepte 0) Loop ook graag op blote voeten. Schoenen knellen teveel aan alle kanten. Maar ik loop niet op blote voeten buiten vanwege viezigheid. Oplossing: barefoot schoenen. 
Dan heb je een dunne, zeer flexibele zool die breed genoeg zijn voor je voeten om natuurlijk te kunnen bewegen. En dit zijn niet alleen maar de bekende fivefingers, je hebt tegenwoordig best leuke modellen.
Je traint op deze manier goed alle spieren in je voeten, je houding wordt beter (dus ook goed voor je bekken/rug/nek) en je doorbloeding in ie benen/voeten verbeterd. Met "normale" schoenen pak je je voeten teveel in waardoor o.a. de spieren lui worden. Krijg je uiteindelijk doorgezakte voeten of kromme tenen en dan pak je ze nog meer in met zooltjes.

Hier staat het wel aardig uitgelegd https://www.vivobarefoot.com/eu/science
En anders eens googlen op shoespiracy.
[igdaob9] (score 3, diepte 0) Ik weet niet waar je woont maar hier in Amsterdam zie je het, wellicht vanzelfsprekend, weinig. Degene die je het zien doen hebben er inderdaad een filosofie voor; het zou gezonder zijn enzo. Je zou ze kunnen plaatsen in het "extreem hipster" spectrum. Zat vroeger op de uni bij een kerel die ook op blote voeten liep, dankzij zij bijzonder slechte persoonlijke hygiene was dat niet erg aangenaam.  


Ik werk bij een brouwerij met terras, om de een of andere reden laten ouder hun kinderen daar rondkruipen en op blotte voeten rondrennen. Echt zo ontzettend dom, denk even na over waar je bent. Kijk even naar de grond, gebruik je kop. Tuurlijk proberen we het allemaal schoon te houden, maar als er honderden als niet duizenden mensen op een dag hier bier komen drinken gaat er echt veel glas stuk hoor... Maar goed, niet mijn kind, heb je gewaarschuwd, niet komen brullen als je koter straks open ligt he, ouders van het jaar 2022?!
[iga8c9v] (score 2, diepte 0) Als de veegmachine net langs is geweest durf ik het nog wel aan. Het zal een trend zijn en voor een enkeling zal er iets meer achter zitten. Wellicht komt het door de inflatie?
[igmovxo] (score 2, diepte 3) In de middeleeuwen hadden ze gewoon schoenen hoor. Er zijn inderdaad wel aanwijzingen dat "bal van de voet eerst", meer een ding was toen.
[igcia6u] (score 2, diepte 1) Je kijkt gewoon 10x zo goed als je op blote voeten loopt. Slippers geven een vals gevoel van veiligheid.
[iggnp8n] (score 2, diepte 3) En slippers beschermen tegen kleine stukjes glas, of steentjes, maar wanneer je je veilig waant stoot je keihard je teen tegen een rondslingerende baksteen. Been there, done that.
[igi8wwj] (score 2, diepte 4) Volgens mij kunnen je voeten ook redelijk tegen stukjes glas. Ik heb in een studentenhuis gewoond waar we lege bierflesjes zo op de grond gooien, dus het hele huis lag vol met glas. En we hadden een katje dat er zo doorheenliep, deed haar niks.
[igappet] (score 2, diepte 0) Gelukkig niet gezien. Ik heb een voetenfobie. Plehhhh.
[igazin7] (score 2, diepte 0) Gister in de trein. 3 mensen (afzonderlijk van elkaar) :/
[igb2zf6] (score 2, diepte 2) Nee ik dacht precies hetzelfde, waarom?
[igazq1c] (score 2, diepte 0) Ik liep van de week toevallig op blote voeten buiten. Ik dacht nog: Ha, dit doe ik echt nooit.
[igbe1zn] (score 2, diepte 0) Misschien binnen. Zelfs in de tuin doe ik losjes schoenen aan want tegels zijn niet comfortabel om op te lopen. Maar stiekem vind ik schoenen ook niet heel comfortabel, dus in huis heb ik ze wel uit.
[igcmuc6] (score 2, diepte 0) Nee eigenlijk niet. Heb zelfs een paar crocks om makkelijk in te stappen als ik vlot iets in de buurt van huis buiten moet doen. Afval wegbrengen of tuinwerk meestal.

Kan mij wel herinneren 1 keer een stuk op blote voeten gegaan te zijn toen ik eens een paar sandaaltjes droeg die er leuk uitzagen maar de bandjes verwonden na een stukje lopen mijn voeten te erg. Dus voordat ik aan bloedens toe zat besloot ik maar uit met die ondingen en voorzichtig blootsvoets te gaan. Schoeisel moet wel lekker zitten bij het lopen (was ook nepleer dus niet echt iets wat met de tijd naar je voeten vormt). Ze waren overigens oorsponkelijk van mijn zusje die er nooit last van had… zo leerde ik dat we te anders zijn betreft schoeisel. Zij kan meer dragen dan ik. Of ben ik minder gewend? Ik krijg zo snel blaren van dingen die zij met gemak probleemloos draagt.
[igd70bx] (score 2, diepte 0) Ik zag laatst een man hardlopen op blote voeten. Midden in de stad.
[igdotrr] (score 2, diepte 0) Je moet ergens op besparen toch, als het lekker warm is buiten en je loopt op je blote voeten gaan je schoenen weer een half jaar langer mee /S
[igdxu37] (score 2, diepte 0) Nee dat zie ik werkelijk nooit hier in Nederland. Ik denk toeval voor jou?  
Mensen moeten dat uiteraard helemaal zelf weten (en ik klaag ook niet als het mooie voeten zijn), maar het lijkt mij totaal niet fijn om te doen. Vies en ja, inderdaad, glass, poep, wie weet waar je allemaal in kunt stappen.
(22 reacties met lagere score weggelaten)

