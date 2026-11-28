# Label-batch batch_0164

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
Schrijf het resultaat naar `batch_0164.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 14p48wd, 1nszc3l, 1m85xby).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 14p48wd ===
SUBREDDIT: r/ems
DATUM: 2023-07-03  SCORE: 7  REACTIES: 18
TITEL: Foot Care
POST (source_id=post):
I wear goretex boots, service requires them to be steeltoe. Second year wearing them but this year in the summer heat I've got a bit of eczema developing on the toes of one foot. What are some good boot/foot care practices?

Never had issues with goretex during my previous career, the steel toe is the difference between those boots and my current. Double sock system with a good copper sole liner, foot powder, insoles out between shifts, not making much of a difference.

Goretex is staying, not a fan of boots that soak up the fluids we're subject to or walking through horder houses without it.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jqg5rdc] (score 11, diepte 0) What socks are you wearing? I just use smart wool socks for hiking and they wick moisture well. Don’t wear the same socks every day
[jqg6mey] (score 7, diepte 2) I work in Texas where it is hot as fuck right now. I don’t have to wear steel toes though. Just one pair of wool socks works for me
[jqggfh1] (score 6, diepte 0) Copper socks are not scientific and a scam. 

Honestly, unless you have a condition then it goes back to correct fit and staying dry. 

One pair of athletic socks (try runners socks) and no powder or anything else. Take an extra pair with your work stuff. When you can, take boots off if only for a little bit and your socks to air out everything. When not working, you can try a hydrating jelly to cover the areas but not while working (don’t want the material in sock to move against your skin). If an area really irritated, then look-up how to apply mole skin over area. 

Good luck and hopefully you find the things that work for you.
[jqg6ex2] (score 5, diepte 1 OP) Outer sock varies, typically a lightweight windriver or similar hiking sock. With copper sole liner underneath to aid in moisture wick barrier and prevent rubbing. Socks changed daily, sometimes outer twice on longer shifts
[jqgb1y1] (score 5, diepte 0) Make sure your boots are drying between wears as well. Open them up best you can, make sure they’re in a place with good air flow, etc. newspaper soaks up moisture, or there’s boot fans, whatever works to get up to the toes. Let your feet breathe when you’re not working.
[jqgu8lh] (score 5, diepte 0) Are you sure it’s eczema and not athlete’s foot?
[jqgalej] (score 4, diepte 0) I’d think about some foot powder. Some recommend cornstarch based powder but I hate cornstarch, talc is the way to go for me because cornstarch gets soupy and sticky. 

Some agencies allow for a medical exemption if you can get a doctors note. Potentially you can get out of wearing steel toes and you can wear a waterproof hiking shoe like salomons. 

Maybe even consider 2 pairs of boots and just alternating between calls. Personally, I mop the station every morning so I can be nice and comfortable and walking around in socks. It lets my boots and socks stay dry.
[jqi2kv1] (score 2, diepte 3 OP) I had a few cotton/wool blend socks in rotation so pulled those out recently. Cotton sucks, will stick to strictly wool thanks
[jqi5ewk] (score 2, diepte 1 OP) Do you use any kind of disinfectant/deodorizer spray meant for sporting equipment? Considering that paired with a boot fan so the spray dries out after absorbing
[jqi4jp6] (score 2, diepte 1 OP) Fit could be better, run half size up for a thicker outer sock in the winter. No issues with blisters or rubbing even half size up because of the double sock system. I swear by the double sock after running single sock just once for a long march and peeled my heel off with a blister haha.

Did not know that copper socks weren't backed, I'm a sucker for a good label. Next time I pick up more liners I'll go with standard moitsure wick, thanks for the heads up. Also pulled any cotton blend socks out of rotation so that my outers are all wool, hopefully that helps. Cotton sucks.

Thanks for the tips, I'll try implementing them and see if theres a difference.
[jqhihqz] (score 2, diepte 1) Yeah I feel it’s less likely to be eczema, more likely to be trench foot or an infection
[jqi2df1] (score 2, diepte 1 OP) Haven't investigated it further, could be athletes but presents similar to eczema which I have a history of. Not as severe as the trench/athletes foot I've had while in the military and its responding to the same treatments as my previous eczema flare ups
[jqg68d1] (score 1, diepte 1) This. Also, if it's really that bad for you, consider bringing a spare pair of socks or two to change into throughout your shift. Good foot care is essential in this field.
[jqi3305] (score 1, diepte 1 OP) Gold Bond has been my savior for years. Stuck with it because other brands felt sticky like you mentioned, those must have veen cornstarch based.

I feel like its mostly a moisture issue with the steel toe on these longer shifts, I do have other boots to rotate out that aren't steel toe. I'll try that out and see if it makes a difference (switch to secondary if my feet feel sweaty and the steel toes need to air out). Thanks for the advice
[jqi634i] (score 1, diepte 2) I don’t usually use a spray; I’ve done pretty okay with like gold bond powder and a set up in front of a box fan if it’s bad. You could probably try vinegar in a spray bottle too.
[jqi4zt1] (score 1, diepte 1 OP) Another thing, I'll try the mole skin since its mostly between two toes where there is likely some rubbing. For a guy that keeps two sleeves of the stuff in every pack I own, I dont know why that hadn't crossed my mind. Thanks
[jqgrepf] (score 1, diepte 0) I bought 3 pairs of boots and rotate through them. I didn't buy extremely expensive boots (about $150 for each). Mine are steel toe as well. I switch between the three and wear good quality cotton socks. I have never had a problem with them. Take care of your feet, and they will take care of you. If you catch deals on boots, having three pairs won't break the bank.
[jqiprz9] (score 1, diepte 0) put new paper inside your shoes, it’s so dry it absorbs moister.

=== THREAD 1nszc3l ===
SUBREDDIT: r/nederlands
DATUM: 2025-09-28  SCORE: 261  REACTIES: 458
TITEL: Heel logisch om je kinderen dakloos achter te laten en hier warmpjes asiel af te wachten.
POST (source_id=post):
Ik heb vrijwel weinig tegen mensen die asiel aanvragen, maar dit soort types krijg ik toch een ontzettende afkeer van.

Deze man is hier in Nederland. Turkije is niet veilig voor hem en zijn gezin. Alleen meneer is hier, zijn vrouw en kinderen lopen dakloos, op blote voeten op een afgelegen gebied. Waarom is de man hier en is zijn waardevolste bezit, neem ik aan, daar in erbarmelijke omstandigheden aan het leven?

Natuurlijk is het paspoort weg en heeft hij het er ontzettend moeilijk mee dat zijn kinderen daar zijn. Daarom ga je zelf op de vlucht en laat je ze daar achter. Klinkt heel logisch. Afgeven op de man die geen onderdak aan je kinderen geeft >is gelijk racistisch natuurlijk< maar zelf geen kut doen en hier lekker de boel afwachten.

En de uitspraak duurt meneer eigenlijk wat te lang, want het is in Turkije niet veilig. Wel sneu voor vrouw, kinderen en zuslief want die hebben helemaal geen uitspraak om op te wachten. Die lopen op blote voeten langs huizen voor een onderdak.

Wat een ontzettend goed toneelstuk is deze man aan het spelen. Nogmaals je kinderen achterlaten? Zo iemand linea recta retour en verdiend de titel vader echt niet. Laat de vrouw en kinderen maar komen. 

Lulhannes.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ngpuw3e] (score 296, diepte 0) Waarom is Turkije precies onveilig eigenlijk?
[ngpywgk] (score 191, diepte 0) Ik ken een syries gezin waarvan de man naar europa is gekomen met zo'n opblaas bootje, vervolgens vanuit italie naar nederland is gelopen en uiteindelijk zijn gezin heeft kunnen laten nareizen.

Die toch is zo bar, dat je dan je jonge kinderen niet mee neemt kan ik me ergens wel voorstellen.

Wat niets zegt over deze meneer natuurlijk, maar het is soms wat genuanceerder dan je hier stelt.  
Dingen zijn zelden zwart/wit
[ngpx3g3] (score 172, diepte 1) Omdat de Turken de vluchtelingen niet willen hebben. Net zoals Egypte, Jordanie en Saodie Arabie de vluchtelingen niet willen.

Hierdoor is de lokale bevolking niet heel erg bereid om de vluchtelingen te helpen. Wat opzich niet gek is want er zijn MILJOENEN vluchtelingen in Turkije.
[ngpuiqn] (score 144, diepte 0) Hoezo is turkije niet veilig? En hoezo verwacht je dat een random turk je familie maar in huis moet nemen?
[ngs3fbw] (score 133, diepte 2) Dat is gewoon een direct gevolg van de bezuinigingen die ook dit kabinet weer doet op oa de IND. Er ligt een gigantische stapel werk en de uitvoeringsorganisaties krijgen geen geld om het weg te werken, dan loopt het natuurlijk vanzelf vast. Klinkt leuk, geen geld uitgeven aan asiel, maar het probleem wordt er groter van.
[ngpudnx] (score 128, diepte 0) Wanneer was dit filmpje gemaakt? Ik loop al een half jaar stage bij VluchtelingenWerk (juridische begeleiding voor statushouders), maar van ieder waarvan beslissing komt is aanvraag ingediend op 2023 of 2024 (maar dan moet je minderjarige kinderen hebben). Als je nu een aanvraag doet dan begint de IND over bijna drie jaar aan je aanvraag.
[ngr9314] (score 114, diepte 2) Dus als alle moslim landen die de zelfde waardes en culturen delen ze al niet willen... waarom nemen wij ze aan dan? Dit is toch gestoord
[ngq1yax] (score 103, diepte 0) Wat interessant OP, zo vat ik deze video en deze situatie helemaal niet op. Laat ik voorop stellen dat we beide te weinig weten van deze situatie om uitspraken over goed of fout te kunnen maken én dat het trekken van conclusies snel gebeurt. 
Echter kan je naast de "deze man verdient de titel vader niet"-houding, ook denken dat dit voor meneer als enige betere toekomst voor zijn gezin kan gelden. Ga er maar aan staan. Je gezin verlaten, je vaderland, alles wat je kent, omdat je daar geen kans op een normaal bestaan hebt voor je gezin. Wat een verschrikkelijk duivels dilemma, ik zou die keuze niet willen maken.  
Het is zo gemakkelijk om vanuit onze(voor mij geldt dit in ieder geval maar zal niet voor iemand anders spreken) bevoorrechte situatie deze conclusies te trekken. Noem me naïef, maar ik denk dat we best wat minder snel kunnen oordelen.
[ngs1hz7] (score 71, diepte 1) En al die tijd word je wel opgevangen, ookal krijg je na 3 en nee te horen heb je wel 3 jaar onderdak gehad. Dit systeem moet echt beter.
[ngrz5op] (score 68, diepte 3) Je bedoelt naast de miljoenen die ze al opnemen? Turkije vangt meer vluchtelingen op dan Duitsland.
[ngpy9u0] (score 67, diepte 1) Ik ken iemand die in Turkije jaren gevangen heeft gezeten omdat hij in de buurt van een protest liep. Heeft asiel gekregen.
[ngs3kqe] (score 67, diepte 0) Je hebt geen idee hoe zo’n vlucht gaat. Mensensmokkelaars zijn levensgevaarlijk en de politie in landen als Bulgarije slaat vluchtelingen lens, pakt hun geld en kleren af, en stuurt ze vervolgens terug. Wat er met de vrouwen gebeurt laat zich raden. En dat is dan nog allemaal afgezien van de nachtelijke wekenlange voettochten door de bergen. Dat iemand zijn vrouw en kinderen daar niet aan bloot wil stellen kan ik me ergens wel voorstellen. 

Toch een ander licht op de zaak dan het standaard “egoïstische asielzoeker gaat lekker van onze luxueuze AZC’s genieten en z’n gezin zoekt het maar uit” verhaaltje.
[ngq26hi] (score 49, diepte 2) Inderdaad. Turkije wil liever van ze af.
[ngqdvzi] (score 49, diepte 1) Door drie of vier andere veilige landen gelopen dus om juist hier asiel aan te vragen.
[ngs8x7n] (score 48, diepte 3) Ja echt he, en maar doen alsof die mensen blij zijn met drie en een half jaar in zo'n opvang te zitten.
[ngpvbfv] (score 48, diepte 0) U en familie komen uit Turkije? Okay veilig land, stempel donder maar op, hoe moeilijk is dat. Ben je zo door die achterstand heen.
[ngpwely] (score 46, diepte 1) Omdat er veel kalkoenen zijn
[ngs10i5] (score 43, diepte 3) Hotels en luxe villas omdat mevrouw faber opvanglocaties heeft gesloten terwijl we ze nog wel moesten opvangen? Die hotels en luxe villa’s bedoel je toch?
[ngr9cav] (score 41, diepte 3) Moslims hebben onderling ook ruzie/oorlog met elkaar.
[ngs6zhz] (score 40, diepte 2) stond drie jaar lang je leven stil...
[ngq89pw] (score 39, diepte 1) Precies. Al deze mensen hier in de comments zijn (denk ik) toevallig hier geboren en hebben het goed. Ook al denken een hoop klagers het hier soms slecht te hebben, we hebben het beter dan een heleboel mensen op deze wereld. 

Maar wat als zij zelf de pech hadden gehad om op een stukje aarde te zijn geboren waar de omstandigheden veel slechter zijn, met een onzekere en sombere toekomst? 

Ik denk dan altijd, stel je die vraag af, dan zou jij waarschijnlijk ook je geluk ergens anders proberen te vinden waar ook jij en je geliefden hopelijk meer kans op fortuin hebben in dat enige leven wat je hebt. 

En ik denk dan ook, wie ben jij (wie zijn wij) om te denken dat we meer recht daarop hebben dan andere mensen in de wereld, puur omdat we toevallig zo fortuinlijk waren om hier te zijn geboren?
[ngpwq3v] (score 37, diepte 1) Onveilig gemaakt door de 5 miljoen vluchtelingen daar. /s


Nee maar even serieus, valt reuze mee daar. Gewoon een ondankbaar mens.
[ngq1ihk] (score 32, diepte 0) Jij zou je vrouw en kinderen duizenden kilometers laten lopen met het risicl dat ze allemaal misbruikt kunnen worden? 

Beetje persoon 1.90m, 110/120 kilo kan ze allemaal de baas met weinig moeite. 🤔

Oh. In debatten kiest de politie de lokale kant en niet die van een vrouw met 2 kinderen. Dat mensen dat nog steeds niet snappen. 🤔🤔
[ngpzs1e] (score 29, diepte 0) Wat een empathie hier weer in deze subreddit.
[ngsg6vf] (score 26, diepte 3) Hoe kom je aan dat getal 4,76 miljoen? Klinkt erg suggestief. Zijn dat allemaal asielzoekers, of is het inclusief arbeidsmigranten, studenten en expats?

Die PVV-taal over migranten is ontzéttend suggestief en versimpeld. Veruit de grootste groep immigranten  (arbeidsmigranten, studenten en expats) is niet goed te verkleinen zonder grote schade aan onze eigen economie. 

Ik vind dat de PVV op dit punt véél te weinig tegenspraak krijgt.
[ngq5stx] (score 26, diepte 3) In Turkije heb je een dictator die soms nogal willekeurig te werk gaat. 

Als Nederland een alleenheerser zou hebben zou je inderdaad hier ook niet meer per definitie veilig zijn.
[ngq452q] (score 25, diepte 1) Iemand die nergens onderdak heeft.
[ngpxiz9] (score 24, diepte 2) Zat in een veilig land met zijn familie. Hij is niet vanuit Syrië hierheen gevlogen.
[ngsbzhy] (score 23, diepte 3) Als het vast loopt, leggen we ze gewoon een boete op. Dat zal dingen oplossen! /s
[ngpz17d] (score 23, diepte 1) Ligt er in zekere mate erg aan. Turkije heeft nog zat politieke vluchtelingen, vooral na het gedoe rondom de Gülen beweging, de coup, d'état poging en de daarop volgende arrestaties van studenten en dissidanten. Daarnaast worden de  Koerden toch echt onderdrukt, nog steeds. 

Voor de rest is Turkije, hoewel niet een geweldig land, voor de meesten wel veilig te noemen
[ngs9xz4] (score 22, diepte 4) Weinig inlevingsvermogen denk ik.
[ngpwjs1] (score 19, diepte 1) Hij is een Syriër.
[ngqbj3v] (score 19, diepte 2) Misschien moeten we daar wat meer mensen op zetten, dan kan het wat vlotter. Zal vast een flinke papieren rompslomp zijn, en meer mankracht helpt dan wel eens.

Maar gelukkig hebben we de afgelopen jaren enorm veel geïnvesteerd in deze sector.
[ngqa17j] (score 18, diepte 1) Absurd veel racisme tegen Koerden en andere Syrische vluchtelingen bijvoorbeeld. Ken een paar Koerden uit Turkije een daarvan had bijna een gevangenis straf gekregen omdat hij geflitst was. Racisme kan daar heel heftig zijn helemaal buiten de grote steden
[ngqfgf8] (score 18, diepte 2) Er zijn heel veel dictaturen op aarde en we gaan dus echt niet al die mensen hier opvangen. 
  
Turkije is gewoon een veilig land wat betreft asielaanvragen.
[ngqjqn7] (score 18, diepte 1) >vervolgens vanuit italie naar nederland is gelopen en uiteindelijk zijn gezin heeft kunnen laten nareizen.

Nouja.. als er echt haast achter had gezeten had dit ook vanuit Italië gekunt natuurlijk. Maar daar heeft die man natuurlijk niet over nagedacht, arme gezin voor niets gewacht.

Of Italië was misschien niet veilig genoeg, zal er tijdens het uitzoeken van mijn volgende tripje maar rekening mee houden.
[ngq2nqr] (score 18, diepte 4) Krijg nog steeds niet het gevoel dat het jou wel wat uitmaakt.
[ngq3wkc] (score 18, diepte 0) De asielketen is een perverse industrie om ons als mensen te verdelen.
[ngq4um5] (score 17, diepte 2) Beter dan doodvriezen.
[ngq1gvv] (score 16, diepte 2) Hoe word je zo hatelijk? Dat je blij kan typen dat kinderen het koud hebben?
[ngq4jtw] (score 16, diepte 2) Mijn god, wat ben jij een naargeestig, kwaadaardig mens.
[ngqnkax] (score 15, diepte 3) Oke maar daar hebben we het niet over hé. Ooit van een whataboutism gehoord, en ja er wonen hier heel veel Chinezen in Nederland die als ze terug gaan gevaar lopen maar over het algemeen zijn mensen uit China veel meer opzich zelf dan mensen uit het Midden Oosten dus je hoort er minder van.

ook vluchten de meeste Chinezen niet naar Europa want dat is niet te doen maar vaak naar andere Aziatische landen of naar Amerika wat een vele malen kleinere afstand is vooral omdat van China naar Europa komen nagenoeg onmogelijk is want dat betekent vaak door Rusland en vaak door gebieden waar voor honderden kilometers niks is.
[ngpvtcx] (score 15, diepte 1) Solliciteer bij de overheid om het tekort op te vullen dan kun je daar zeker wat in betekenen.
[ngpvnpc] (score 15, diepte 0) Ze hebben hem wijsgemaakt dat er bij aankomst in Nederland een gemeubileerde woning klaarstaat. Maar misschien mag hij nog wel naar de Efteling op onze kosten.
[ngpvubk] (score 14, diepte 1) Bij VluchtelingenWerk heb ik een cliënt die was gevlucht uit Turkije (hele gezin is Turks). Het kan wel.
[ngq4677] (score 14, diepte 2) Volgens die logica is het hier ook niet veilig. Dan is het nooit ergens veilig.
[ngq575s] (score 14, diepte 6) Veilig voor West-Europese toeristen. Maar niet voor Syriërs.
[ngs6u5s] (score 14, diepte 3) Je redeneert echt enorm zwart-wit. Turkije is als veilig bestempeld dus iedereen is veilig. Heb je er ook al bij stilgestaan dat Koerden zwaar onderdrukt worden in Turkije?
[ngscwmg] (score 14, diepte 1) Precies! De keuze was daar blijven met niets, of met vrouw en kinderen al ls een nomade gaan rondreizen, of vrouw met de kinderen achterlaten vooruitreizen en kijken of ze ergens terechtkunnen.
[ngqfmt7] (score 13, diepte 2) Kan ook in China gebeuren. 
Met die redenatie moeten we hier honderden miljoenen Chinezen opvangen.
[ngtckgl] (score 13, diepte 6) Veel vluchtelingen komen uit hun aangrenzende landen, en gezien je in het eerste land waar je terecht komt Asiel moet aanvragen, zitten er veel in Turkije en volgens de regels, hoort het wel. Ze hebben ruimte zat dus wat dat betreft zijn ze daar beter af dan in een klein land zoals NL. 

Buiten dat, denk ik dat het voor iedereen handiger is wanneer je vlucht naar een land die meer gemeen heeft met jouw eigen cultuur. Tenzij je het niet erg vind om je aan te passen en dus geen eer moord gaat plegen omdat je dochter net als je zoon, mee doet met haar leeftijdsgenoten.
[ngq9q4h] (score 13, diepte 1) Volgens de regering is Turkije niet onveilig. Maar Turkije is nu een rasechte dictatuur. Er zijn tienduizenden mensen in de gevangenis die daar niet horen. Dit zijn feiten die als zodanig worden geaccepteerd door o.a. de EU en Amnesty International. 

Er zijn dus goede redenen om het als onveilig te beschouwen. Maar het gaat erom om wat de Nederlandse overheid erover denkt en dat is dat Turkije veilig is. 

OP zegt wel dat hij bij zijn familie moet blijven maar OP moet zichzelf eraan herinneren dat hen maar een fragment van twee minuten heeft gezien. En om een gedegen oordeel te vellen over zo'n complexe keuze heb je toch wel meer info nodig. 
Hoe weet hen niet dat het mevrouw was die erop heeft aangedrongen dat meneer zo snel mogelijk naar Nederland moet reizen om asiel aan te vragen bijvoorbeeld? Of door gebrek aan financiële middelen, hij in zijn eentje moet reizen? Of dat hij niks kan betekenen in Turkije voor zijn gezin en dat dit de beste optie is? 

Zo zijn er nog veel meer vragen die beantwoord moet worden voordat men een oordeel kan vellen.
[ngs0ypg] (score 13, diepte 3) De rechter says no.
[ngpvtkk] (score 13, diepte 0) Vertel me alsjeblieft dat die vertaling niet klopt. Welke idioot laat z'n kinderen aanbellen bij een vreemde man om daar te overnachten?
[ngry7tt] (score 12, diepte 3) Istanboel alleen al heeft 3 miljoen illegalen. Verspreid over heel het land zijn het er nog meer.
[ngs5hov] (score 12, diepte 4) Aan de andere kant hebben we zonder probleem een flinke hoop ukrainse vluchtelingen succesvol geïntegreerd en zie je ze nu vlekkeloos de taal spreken en bijdragen op de arbeidsmarkt.
[ngsd8kc] (score 12, diepte 4) Zoals het ook hoort te zijn?
[ngsa0xy] (score 12, diepte 3) Wat is het verschil tussen een netto en bruto migrant?
[ngq8f74] (score 12, diepte 1) We hebben dezelfde gedachtegang; ik vind dat OP inderdaad te snel conclusies heeft getrokken.

Want als dit voor deze meneer de enige kans is om zijn familie hier naartoe te halen, in plaats van daar allemaal te sterven, dan zou dit de meest logische keuze zijn om zijn gezin daar 'tijdelijk' achter te laten.
[ngq1wu9] (score 11, diepte 1) Probleem is dus dat er veel te weinig personeel is om dat te doen. Blijkbaar zijn ze op dit moment bezig met het afhandelen van verzoeken uit 2023/2024, en verzoeken van nu komen als het goed is over 3 jaar 'n keertje aan de beurt. Er is simpelweg te weinig mankracht om die verzoeken sneller te laten verlopen.
[ngs7t2w] (score 11, diepte 5) https://www.vluchtelingenwerk.nl/nl/artikelen/nieuws/oekrainers-hebben-geen-idee-waar-ze-nog-terecht-kunnen

Ja gaat lekker met de Oekraïners in Nederland. Het zijn er overigens geen 300.000 ook nooit geweest. 

https://longreads.cbs.nl/asielenintegratie-2024/oekrainers-in-nederland/
[ngslntc] (score 11, diepte 8) Turkije heeft gedurende de Syrische burgeroorlog aan een stuk door islamitische groeperingen zoals al-nusra bewapend en gefinancierd. Niet te vergeten hun eigen strijd tegen de Koerden in het noorden van Syrië. Lekker weer domlinks het westen de schuld te geven zonder kennis van zaken te hebben.
[ngscoyz] (score 11, diepte 1) Precies dit. De man gaat ergens proberen een beter leven te zoeken en probeert dan de kinderen over te laten komen. Is vrij normaal dat als de moeder daar nog voor de kinderen kan zorgen, je niet als een nomade met de kinderen heel de wereld gaat rondreizen.
[ngsp2i5] (score 10, diepte 4) Dat wordt wel een beetje grijsgedraaid plaatje hoor.
[ngqqscl] (score 10, diepte 5) Gelukkig komen Chinezen niet massaal naar Nederland toe.
[ngqcdpb] (score 10, diepte 3) Voordat mijn familie naar Nederland kwam heeft mijn vader ook twee onbekende vrouwen met kinderen naar binnen gelaten en ze een aantal maanden onderdak geboden. Al was dat wel een andere situatie omdat zij een schuilplaats zochten nadat hun huis was plat gebombardeerd.

Maar goed die vrouwen wisten ook niet dat mijn vader zelf een zwangere vrouw en twee peuters thuis had zitten, ik bedoel voor hetzelfde geld hadden ze bij een man aangebeld die misbruik van ze wilde nemen. 

Kan me heel goed voorstellen dat als je al zo lang dakloos en angstig rond loopt met jonge kinderen, dan raak je op een gegeven moment wel de wanhoop nabij. Je denkt niet meer rationeel na en het enige aan je hoofd is om je kinderen ergens onder te brengen, ook al is het maar voor één nacht.
[ngs3qn0] (score 10, diepte 2) Italië is ook niet bepaald een land waar dit makkelijk gaat.
[ngq2uc7] (score 10, diepte 4) Nee ik snap jou gedachten niet. Denk je echt dat je het hem niet uitmaakt dat zijn kinderen daar zo rond lopen? En tegelijkertijd heb je ook nog inlevingsvermogen? Nou ja, dan vind ik je vooral dom
[ngq3dac] (score 10, diepte 5 OP) Turkije is een relatief veilig land. Dat je er voor kiest om alleen hier naar toe te gaan en niet daar een bestaan voor je kinderen op te bouwen zegt wel wat. Of dat je hier samen naar toe gaat ipv alleen. Als je weet dat ze dakloos zijn dan is alles toch beter dan ze achterlaten? Neem ze mee of bouw daar wat op. Hij woonde niet in Syrië hè?
[ngq88ud] (score 10, diepte 2) Dat is een droomscenario maar een zorgvuldige procedure, uitzoekwerk, enorme drukte en voortdurend uitkleden van de diensten door rechtse partijen gooien roet in het eten
[ngq4muy] (score 10, diepte 0) goh iedereen is heel toevallig zijn papieren en paspoort kwijt.
en uiteraard stuur je je kinderen en je vrouw niet hierheen maar worden ze allemaal achter gelaten.
[ngsdcou] (score 9, diepte 5) Een Oekraïner en een midden-oosters persoon zijn absoluut niet met elkaar te vergelijken. Andere normen en waarden, geloof, werkethiek etc.
[ngqdu6y] (score 9, diepte 1) We kennen de achtergrond van deze man niet, maar er zijn volkeren die in Turkije niet echt welkom zijn. 

Vraag eens rond over de Koerden, bijvoorbeeld
[ngquwfv] (score 9, diepte 0) Wat zijn de langetermijn plannen eigenlijk hieromtrent? Bekijk de huidige situatie en denk 40-50 jaar verder.. waar eindigt dit?
[ngs2tpf] (score 9, diepte 1) Wat een naar persoon ben je. Praten over mensen als parasieten. Bah
[ngst54m] (score 8, diepte 4) Ja, tuurlijk! In mijn ervaring willen deze mensen maar al te graag werken. Meer wil dan de gemiddelde autochtone uitkeringstrekker. Maar ze mogen niet.
(439 reacties met lagere score weggelaten)

=== THREAD 1m85xby ===
SUBREDDIT: r/nederlands
DATUM: 2025-07-24  SCORE: 585  REACTIES: 433
TITEL: Is sociale huur niet heel erg raar geregeld?
POST (source_id=post):
Oke. We subsidiëren de huren dus voor een groot deel van Nederland. Namelijk de mensen die te weinig verdienen voor andere vormen van verhuur.

Dan komen we bij het eerste bijzondere punt. We kijken namelijk niet naar de situatie van een persoon. Kies jij ervoor om slechts 24 uur te werken? Dan mag je ook een gesubsidieerde woning. Dat is toch raar? Waarom belonen we mensen die bewust minder willen werken op kosten van mensen die wel veel werken? Disclaimer: Als je ziek bent is het een ander verhaal natuurlijk. 

Volgende gekke punt. Deze woningen hebben slechts 1 inkomensgrens. Waarom laten we de huur niet meebewegen met het inkomen? Iemand die 40K verdient zou meer moeten betalen dan iemand die 20K verdient lijkt mij. Het is toch gek dat een rijtjeshuis in Amsterdam 700 euro per maand kost maar het huis van de buurman 1.5k? Lijkt mij logischer als de huurprijs meebeweegt op basis van inkomen. Nu loop je echt veel subsidie mis als je net over de grens zit. 

Dan zit je dus in zo'n huis, komt je partner erbij en kun je heerlijk gaan scheefhuren. Verdien je inmiddels veel meer dan de sociale huurgrens? Geen probleem Je blijft lekker het lage bedrag betalen. Ik snap dat je deze mensen na zoveel jaren niet kan laten verhuizen, maar verhoog dan de huur! Ik ken wel 5 opa's en oma's van mensen die een hele eengezinswoning bezetten voor maar 600 euro per maand. Kinderen zijn al lang uit huis en ze verdienen veel te veel. 

En dan nog zoiets. Huurtoeslag. Huur je sociaal? Top, jij krijgt huurtoeslag en bent nog goedkoper uit. Kun je geen sociale huurwoning krijgen? Dan heb je pech. Huurtoeslag krijg je niet op particuliere verhuur, ook al is de huur duurder. Je hebt door het woningtekort dus nog een groter probleem!

Is het niet tijd dat we dit systeem eerlijker maken? Ik denk dat als we dit doen, we heel veel geld vrij kunnen maken voor mensen die het hard nodig hebben. Ik ken zelf al meerdere mensen die inmiddels de 30 voorbij zijn en nog geen kinderen hebben. Niet omdat zij het niet willen, maar omdat je pas een benodigde woning kan krijgen na deze periode. Zo schiet Nederland zichzelf toch in de voeten?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[n4wo3zm] (score 338, diepte 0) >Huurtoeslag krijg je niet op particuliere verhuur, ook al is de huur duurder

Als de huur binnen een bepaald bedrag valt kun je voor particuliere verhuur ook huurtoeslag krijgen.
[n4wv86t] (score 159, diepte 0) Als ik iedereen om me heen spreek willen mensen het systeem liever oneerlijk houden. Mensen die gekocht hebben willen niet meer sociale huur in hun wijk. Mensen die zelf in sociale huur zitten willen er goedkoop in blijven. De stakkers die en niet gekocht hebben en niet sociaal huren zijn arm en hebben zero politieke macht. Zij zijn verder ook perfect voor deze economie om lekker te exploiteren: handige goedkope arbeidskrachten die geen maand zonder hun salaris kunnen. Hierop draait de Nederlandse economie dus Den Haag wil ze ook graag arm houden.
[n4woucv] (score 109, diepte 1) Als de huur onder de sociale huurgrens valt is het juridisch gezien ook sociale huur. of de eigenaar nou een particulier is of niet
[n4wp9a5] (score 108, diepte 0) Comrade je bent je op de verkeerde aan het richten. Laten we niet niet nog verder een miljarden kostend systeem optuigen om te checken of de bijstandsmoeder niet te veel tandenborstels op d'r badkamer heeft staan terwijl melkers binnenlopen door een doelbewust gecreëerd en in stand gehouden tekort aan betaalbare woningen.
[n4xy7iq] (score 85, diepte 1) Niet zo gek dat mensen in een koopwoning geen sociale huur willen in hun wijk. Niet iedereen die een sociale huurwoning heeft is een tokkie maar vrijwel alle tokkies wonen wel in sociale huurwoningen.
[n4wpcp4] (score 76, diepte 0) Ik reageer even iets algemener op deze:   
  
*Is het niet tijd dat we dit systeem eerlijker maken? Ik denk dat als we dit doen, we heel veel geld vrij kunnen maken voor mensen die het hard nodig hebben.*



Dat het via subsidies wordt geregeld ipv voldoende hoge netto lonen vind ik in een welvarend land zoals dat van ons absurd, zodoende principeel tegen huursubisie en andere toeslagen, draai aan andere knoppen zoals de inkomsten belasting in de laagste schalen of vergroot woningvoorraad om de vraag te doen dalen dan doen de prijzen dat ook. En er zijn ongetwijfeld meer opties binnen de huidige belastingen. Wat ook lastig is, is dat we met de huidige toeslagen en de aanvragen daarvan juist van de mensen die gemiddeld genomen niet een WO opleiding hebben wel vragen om complexe aanvragen voor allerhande toeslagen en ontheffingen goed te doen. Fouten worden hard afgestradt

Nu hebben we dubbel werk met heel veel ambtenaren, regelingen en controlesystemen, die shit kost veel geld bovenop de reguliere kosten van de belastingdienst. Een kleiner systeem zonder toeslagen zou in mijn optiek veel beter zijn.
[n4wv6ce] (score 62, diepte 2) Het kromme is dat particuliere woningen een stuk duurder zijn, maar dat je daar geen huursubsidie voor ontvangt. Terwijl je zou verwachten dat die huurders het harder kunnen gebruiken in deze markt. 

  
De woningmarkt in Nederland is op verschillende punten dramatisch. Ik heb jarenlang ingeschreven gestaan voor een sociale huurwoning. Tegen de tijd dat ik eindelijk in aanmerking kwam verdiende ik net boven de huurgrens... Lekker dan.
[n4ws0oj] (score 55, diepte 0) Ja en dan hebben we ook nog eens de taak van die huurwoningen beheren opgesplitst in 269 sociale huurverenigingen, want dat is efficiënt of zo.
[n4wrgbr] (score 53, diepte 1) Mensen snappen niet dat particulier en vrije sector niet hetzelfde zijn.
[n4wp1v2] (score 45, diepte 0) Ja, het is raar geregeld en het kan altijd beter. Weet je wat nog raarder is geregeld? Dat de allerrijksten te weinig belasting betalen. Daardoor wordt alles kapotbezuinigd en daardoor hebben we deze kapotte systemen.
[n4wt7n9] (score 38, diepte 1) Het feit dat je eerst aan de belasting verlagen denkt in plaats van aan het minimumloon verhogen is denk ik de inherent rechts economische bias die er in Nederland heerst. Je dicht dan namelijk het ene gat met het andere. Er is nou eenmaal geld nodig voor (met name) de zorg, onderwijs, infrastructuur, en sinds kort blijkbaar ook defensie. Terwijl het geld elk dag meer en meer bij een kleine groep rijke mensen ligt. 

Het zoeken van geld bij elke andere groep dan deze groep is gedoemd om te mislukken of een ander probleem te veroorzaken. men vergist zich hoe teringrijk een bepaalde groep in onze samenleving is, en dat er ene directe relatie is tussen hoe rijk zij zijn, en hoe slecht het met de mensen aan de onderkant gaat.   

Kortom, welk probleem je ook ziet in de samenleving, je losth et alleen op door er tijd en moeite in te steken. Tijd en moeite organiseerj e door er geld voor te betalen. Haal het geld. Haal het waart het zit. Belast miljonairs en miljardairs. Als ze heel hard beginnen te huilen en te dreigen dat ze vertrekken in de media naar een ander land  weetje dat het is begonnen te werken.
[n4x2jfc] (score 36, diepte 1) Ben ik niet helemaal met je eens. Een oud collega van mij huurt sociaal, 4 kamer appartement en woont in haar eentje. Dit appartement heeft ze gekregen omdat de vorige tegen de vlakte ging. Het is nieuw en een stuk groter omdat ze er niet op achteruit mocht gaan. Nou dat is nog begrijpelijk, zij het niet dat deze dame bijna een ton per jaar verdiend. Ze gaat niet meer weg, want ze zit nu in een complex waar er ook woningen verkocht worden en de koopprijs voor haar locatie is rond de 8 ton tot een miljoen. 

De huurverhoging voor scheefwonen is €100 en mag niet hoger dan de maximale huurprijs die door het puntensysteem ook weer beperkt wordt. Dat duurt dan ook jaren voordat ze daar is en ze kan het makkelijk betalen. 

Ik begrijp haar, maar het is niet helemaal fair dat zij meer dan twee keer modaal verdient, ze voor een habbekrats 3 lege slaapkamers heeft en heel veel geld overhoudt.  

Het zou een beetje hetzelfde moeten zijn als met studentenwoning na x jaar moet je als je te veel verdiend wel gewoon verhuizen. Zo kunnen mensen die echt een sociale huurwoning nodig hebben deze ook gebruiken want die wachtlijst is echt te lang.
[n4wzdsr] (score 32, diepte 3) Dan ga je toch 31 uur werken? Krijg je misschien nog huursubsidie ook!

/s
[n4wzs3n] (score 29, diepte 4) Ja had ik idd moeten doen om in aanmerking te komen. Beetje krom dat het zo wel mag. En na het verhuizen weer terug naar full-time
[n4x2vey] (score 28, diepte 2) Onzin. Huurtoeslag is alleen als er een huurprijs is van X of minder. Huurprijs hoger? Geen toeslag.

Geloof niet alles wat je hoort. Huisjesmelkers pakken hier geen cent op.
[n4wsvgl] (score 28, diepte 1) Snap ik niet waarom hier niet meer ophef over is, volgens het [CBS](https://www.cbs.nl/nl-nl/nieuws/2025/03/56-procent-vermogen-in-handen-van-10-procent-huishoudens) heeft 10% van de Nederlandse bevolking meer als de helft van het vermogen in handen. 

Oftewel 1,5 biljoen euro voor 10% van de samenleving en 1,2 biljoen voor de overige 90%.
[n4wuuvf] (score 27, diepte 0) Koop wordt ook zwaar gesubsidieerd met de hypotheekrenteaftrek
[n4wwq19] (score 27, diepte 0) Niet al je punten zijn slecht, maar ik zou het als ik jou was toch écht even wat beter onderzoeken.

Je inkomsten tellen namelijk wel degelijk mee in wat je mag huren (niet meer als je er al zit, maar wel als je nog reageert). Iemand met zeer lage inkomsten mag b.v. ook alleen zaken onder de 500 euro p/m huren (meestal hele kleine appartementjes) en mensen die meer aan de bovengrens zitten mogen juist alleen boven de 500 euro p/m huren (dit is een voorbeeldgetalletje, maar daar komt het ongeveer op neer).

Daarnaast wordt jouw huur ieder jaar met max 5% verhoogd als je teveel verdient of als je een intrekkende partner hebt en daarmee samen teveel verdient. Ik huur technisch gezien "scheef", maar mijn huur zit al ruim boven de sociale huurnorm wegens de verhogingen.  
Daarnaast gaat het ook niet meer omlaag als het eenmaal verhoogd is, ook al verdien je niets meer, dus dat is ook wat krom.

Je kunt die opa's en oma's die nog steeds goedkoop zitten niet vergelijken met huidige regels. Die hebben 60 jaar geleden een huurcontract ondertekend en toen zaten verhogingen daar nou eenmaal nog niet in.
[n4y780d] (score 25, diepte 5) Is het aan jou om te bepalen of ik genoeg werk of verdien, en of mijn partner dat ook doet?!
Sinds wanneer is leven van een modaal inkomen en een klein beetje sparen geld over de balk smijten?
Feit is dat in de huidige situatie met het huidige inkomen, kunnen we niet meer dan 250k hypotheek krijgen en sparen is leuk, maar de woningen stijgen sneller ik prijs dan dat ik ook maar zou kunnen sparen. 
Daarnaast is het echt belachelijk om te suggereren dat ik maar in een ander land moet gaan wonen gezien de woningen daar goedkoper zijn. Ik ben geboren in Nederland, ben Nederlander en blijf de rest van mijn leven hier wonen. Dit land is niet alleen van de rijken en de mensen die geluk hebben gehad omdat ze 5 jaar geleden een huis konden kopen. 

Als ik 5 jaar geleden ook al de mogelijkheid had gehad om een woning te kopen (meerdere collega’s hebben dat doen voor elkaar gekregen met een enkel modaal inkomen), had ik dat ook zeker gedaan. Helaas liep het anders. 
Moet ik daarom maar oprotten naar een ander land of op straat gezet worden gezien er geen andere opties zijn om uit een sociale huurwoning te komen?
[n4x00mh] (score 25, diepte 0) We subsidiëren ook mensen die een huis hebben met de Hypotheekrenteaftrek, ookal stuwt dit de prijzen hoger en wordt dit betaald uit belastinggeld, en hebben de rijken (mensen met een huis van 1 miljoen + ) hier meer subsidie voor dan de middenklasse. Ook absurd, toch?
[n4wom07] (score 23, diepte 1) Gaat inderdaad om de hoogte van de huur, niet of er particulier of sociaal gehuurd wordt.  
Ik huur particulier en ontvang huurtoeslag.
[n4xqoj0] (score 21, diepte 3) Voor particuliere huurwoningen onder de sociale huurgrens ontvang je ook gewoon huursubsidie hoor. Er zijn twee soorten zelfstandige huurwoningen in Nederland, sociale huurwoningen en vrije sector huurwoningen. Er zijn meerdere soorten verhuurders in Nederland, bijvoorbeeld particuliere verhuurders en institutionele verhuurders. Er is geen directe koppeling tussen de soort verhuurder en de soort huurwoning.
[n4xz6v2] (score 21, diepte 1) Ik heb al vaker voorgesteld om alle toeslagen op basis van een fulltime inkomen te bepalen. 

Iemand die 20 uur werkt tegen €15,-/u krijgt dan evenveel toeslagen als iemand die 40 uur werkt tegen €15,-/u. Dan creëer je direct een trigger om meer te gaan werken, en een eerlijker systeem. 

De arbeidsongeschikten zullen dan gecompenseerd moeten worden door een hogere uitkering, of een persoonlijke toeslag op de uitkering.

Verder moet de kinderbijslag afgeschaft worden en verdisconteerd in het kindgebonden budget. Nu profiteren de rijksten in dit land ook van kinderbijslag terwijl ze het helemaal niet nodig hebben. 

Ik vind het idee van OP om de huurtoeslag enkel inkomensafhankelijk te maken, en de huurtoeslaggrens te schrappen. In elk geval de moeite waard om te onderzoeken. 

Dan moet er ook eens heel goed gekeken worden naar de hoogte van bijstand en de toeslagen die ze dan krijgen. Gezinnen in de bijstand die netto meer te besteden hebben dan gezinnen waar vader (of moeder) de kost verdiend met hard werken en veel belasting afdragen begint steeds normaler te worden. 

Ook wil ik voorstellen dat statushouders geen voorrang meer krijgen op de sociale huurmarkt. Alleen al het vooruitzicht dat ze hier tientallen jaren in een AZC moeten wonen zal mss ook de drang om juist hierheen te komen verlagen. Hoe dan ook is het niet meer uit te leggen dat jongeren hier geen woning kunnen krijgen.

Elke asielzoeker die hier crimineel gedrag vertoont gaat linea recta retour afzender. Desnoods op de Junta-methode. In dit land is geen plaats voor dat soort tuig.
[n4wro16] (score 21, diepte 1) Het zoeken van de zondebok is ons aangeleerd, juist zodat we ons niet richten tot de beleidsmakers en melkers die als enige profiteren van het systeem.

Het is een race to the bottom zodat het renteniersbestaan van de rijken zo lang mogelijk beschermd kan worden. Tot de hele handel onvermijdelijk in elkaar stort,
[n4wqrcd] (score 21, diepte 0) Huren in de vrije sector verdwijnt in rap tempo dankzij de zogenaamd ‘betaalbare huurwet’ van minister De Jonge. In Nederland heerst nog altijd de gedachte dat meer regels beter zijn, maar helaas wil straks niemand meer verhuren.
[n4x95ku] (score 21, diepte 1) Huisjesmelkers voegen letterlijk niks toe aan de maatachappij, zal tijd worden dat we van deze parasieten af zijn.
[n4wukba] (score 20, diepte 2) Als je het minimumloon oneindig veel hoger maakt dan onze buurlanden dan krijg je nog meer arbeidsmigratie, het nettoloon verhogen van de mensen in die huurwoningen leek me dan handiger om te doen via lagere inkomsten belasting voor die groep, scheelt weer abtenaren.

Ik ben namelijk helemaal niet rechts
[n4wsta3] (score 19, diepte 2) >Het zoeken van de zondebok is ons aangeleerd

\-> Wijst onmiddellijk een nieuwe zondebok aan...
[n4ycwfr] (score 17, diepte 3) 200 eur hypotheek, lmao.
[n4wzcxa] (score 17, diepte 1) Ik zou ze liever adviseren om een goede opleiding met een goede baankans te doen zodat ze zodra ze van school kunnen meteen een hypotheek kunnen aanvragen en een huis kunnen kopen. Tegen de waardevermeerdering van een huis kun je niet opsparen en is een leuk pensioen voor later.
[n4xwtgq] (score 17, diepte 3) Ja, dankjewel. In dat geval zou ik nu dus op straat moeten staan volgens jouw regel. 
Geloof me, ik zou niks liever willen als hier uit mijn appartement weg. 
Echter valt er met €250k hypotheek niks te krijgen (buiten opknappers of huizen met andere zware nadelen), zelfs niet hier in de Achterhoek. Alleen in het noorden is er misschien nog het een en ander te krijgen voor dat bedrag.
Ik zit gewoon klem!
[n4xas9f] (score 16, diepte 2) Het verhogen van het minimum loon klinkt makkelijk maar daar zitten ook haken en ogen aan.

Als de kosten voor een medewerker hoger zijn als de economische meerwaarde die hij toevoegt is het als werkgever niet verstandig om iemand aan te nemen.

Mensen die economisch te weinig kunnen toevoegen zullen met een hoger minimum loon zonder werk komen te zitten.

Nu lossen we dat op door het minimum loon dankzij o.a. zorg en huurtoeslag kunstmatig laag te houden. Hierdoor kunnen deze mensen wel aan het werk en leveren ze economische meerwaarde naar draagkracht.
[n4xkjod] (score 16, diepte 0) Anderzijds is er decennia geleden al besloten dat er altijd een tekort aan woningen moet zijn. Op die manier wordt er (extra) waarde in huizen gepusht. Iets dat de afgelopen 10 jaar volledig uit de hand is gelopen en mogelijk een gigantische nieuwe dubbel heeft gecreëerd. Maar ja. Gesubsidieerd wonen in overgewaardeerd onroerendgoed is het probleem...
[n4ydnwr] (score 15, diepte 4) Het jammere is alleen dat er voor het bedrag tot waar je huursubsidie ontvangt tegenwoordig geen particuliere huurwoning meer kunt vinden.
[n4x8sc1] (score 15, diepte 1) Een extra belastingschijf voor inkomens boven de Balkenende-norm is iets wat ik persoonlijk graag zou willen zien. Als je meer dan €246.000 per jaar verdiend kan je echt wel meer belasting betalen over het gedeelte wat daarboven zit.
[n4x6y30] (score 14, diepte 0) Grappig om iedereen hier te zien praten over regels en subsidies en die en dat, terwijl het eigenlijke probleem alleen maar op te lossen is door te zorgen dat er voldoende woningen zijn voor iedere categorie. Sociale huurwoningen, vrije sector woningen, koopwoningen voor starters, koopwoningen voor gezinnen en ook woningen voor oudere mensen om in te leven als ze afstand hebben gedaan van het gezinsleven. 

Iedere andere oplossing (subsidies, hypotheekrente, starterskorting) lost het probleem alleen maar op voor een bepaalde groep.
[n4z894y] (score 14, diepte 0) De werkelijkheid is altijd genuanceerder dan de "ze moeten gewoon...". Voor de details zijn er goede podcasts te vinden op spotify bij Jesse Frédériks van De Correspondent, zoek op wonen.  

Het is een hele keten die kosten opjaagt en daar moet compensatie voor komen, de huurtoeslag, Ondanks dat er misbruik van gemaakt wordt is dat slechts een klein percentage. 
En nee, niet iedereen kan fulltime werken en meedoen in deze maatschappij en ja als samenleving helpen wij anderen om een menswaardig bestaan te hebben. Dat systeem werkt namelijk beter dan het "iedereen voor zich" systeem.
[n4wsm3f] (score 13, diepte 2) >Volgens mij is het overigens wel zo dat je boven de sociale huurgrens nooit subsidie kan krijgen. En als je huur onder die grens valt is het geen particuliere huur maar sociale huur.

Dat klopt dus niet. Vanaf 2026 krijg je ook bij hogere huur subsidie als je loon laag is. En een sociale huur kan ook particulier zijn. Of iets particulier is of niet hangt niet van de huurprijs af maar van wie die eigenaar is.
[n4wphx0] (score 13, diepte 0) Mensen die fatsoenlijk verdienen subsidiëren zo’n beetje de gehele onderlaag van de samenleving in toeslagen en tegemoetkomingen.
[n4wtbcz] (score 13, diepte 2) Fijn voor ze. Minder fijn voor de mensen die niet kunnen kopen en geen sociale huurwoning kunnen krijgen. Een flexibele huurmarkt is juist heel belangrijk voor de economie. Mensen moeten kunnen wonen waar ze willen werken.
(454 reacties met lagere score weggelaten)

