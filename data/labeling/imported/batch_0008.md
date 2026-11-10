# Label-batch batch_0008

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
Schrijf het resultaat naar `batch_0008.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(5 threads: 16staxr, tabn49, 112w6n7, phgz4d, 1m8k3ks).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 16staxr ===
SUBREDDIT: r/thenetherlands
DATUM: 2023-09-26  SCORE: 125  REACTIES: 45
TITEL: Hoofdverdachte Sanil B. in de Mallorca-zaak komt voorlopig niet op vrije voeten.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k2bupmo] (score 175, diepte 0) ‘Ik zit onschuldig vast’ zegt hij, nadat er dna van het slachtoffer is aangetroffen op z’n schoen. 

Deze idioot en z’n vriendjes moeten allemaal in de cel
[k2bfkhu] (score 124, diepte 0) Goedzo zulke moordenaars horen in de bak.
[k2ca8yl] (score 116, diepte 0) Ja hoor, allemaal met je vriendjes stil blijven en beroepen op je zwijgrecht over wat er echt gebeurt was die avond, maar wel volhouden dat je onschuldig bent. Vervelend voor je zeg.
[k2cqbh5] (score 78, diepte 1) Het beroepen op zwijgrecht mag nooit als aanname voor schuld gebruikt worden.
[k2crslq] (score 56, diepte 3) Sanil B zal vast schuldig zijn, daar is genoeg bewijs voor. Maar het idee dat je automatisch iets te verbergen hebt als je je beroept op het zwijgrecht is iets wat gelijk in de kiem gesmoord moet worden.
[k2e8b7u] (score 47, diepte 2) Goed dat je het zegt, maar ik mag het ze wel kwalijk nemen. Ze weten dondersgoed wat er die nacht gebeurt is, maar ze willen het niet zeggen. Daardoor blijft de familie van het slachtoffer ook in het duister. Dat zijn nare praktijken. 

Dit zijn jongetjes uit Haarlem, geen gangsters uit Chicago of Detroit.
[k2e3661] (score 40, diepte 1) Als het een van mijn vrienden was dan had ik meteen gesnitcht. Als je zo stoer bent om te vechten moet je ook de consequenties accepteren.
[k2cr12d] (score 40, diepte 2) Toch vreemd? Het Zwjjgrecht mag je altijd gebruiken, klopt en juridisch is het geen schuldbekentenis, klopt als een bus.

MAAR. Eem: er is een jongen dood. Hij werd geschopt op de grond. 7 man om hem heen. En niemand weet het? Serieus? Als je dat geloofd heb ik ook nog wel een brug die je van me mag kopen.
[k2da555] (score 35, diepte 5) > PLUS het beroepen op zwijgrecht.

Maar dat is het punt… beroepen op zwijgrecht hoort helemaal niet thuis in dat rijtje. Het heeft helemaal niks te maken met de beoordeling of iemand schuldig is.
[k2e8zj7] (score 31, diepte 4) Iedereen hier doet alsof we Sanil B. Veroordelen enkel op zijn beroep of zwijgrecht. Dat is niet zo. Het is 1) al het bewijs tegen hem, 2) het veroordeeld zijn, maar dan 3) in hoger beroep gaan, 4) volhouden dat je onschuldig bent & 5) 
weigeren te zeggen wat er die avond gebeurt is, dat is waar hij zo zwaar op wordt aangerekend. 

Als er op werk iets fout gaat, al het bewijs naar 1 persoon wijst, en die collega blijft zeggen “ik was het niet, maar ik wil niet zeggen wat er gebeurt is” zou je er ook niet bij staan met je handen in de lucht “guess we’ll never know!”  Nee, je zou zeggen dat het een slap verhaal is.
[k2elqah] (score 23, diepte 1) Het gore lef om het te zeggen alleen al. Denkt alleen aan zichzelf. Van mij mag hij zo lang mogelijk vast zodat hij de tijd heeft om te reflecteren wat hij gedaan heeft
[k2dacr7] (score 20, diepte 5) Omdat het een recht is. Als je erop beroepen bewijs was voor schuld zou het een nutteloos recht zijn.
[k2dwcg6] (score 17, diepte 7) > Dat wil niet zeggen dat je er niets uit zou kunnen afleiden.

Dat is precies wat dat wil zeggen… als een rechter er iets uit zou kunnen afleiden, dan heeft dat recht geen nut meer… 

Waarom zou iemand zich ooit op dit recht beroepen, als het wijst op schuld?
[k2e2vkr] (score 14, diepte 0) Ik heb nog nooit gevochten. Snap ook totaal niet dat zoiets in je holle hoofd naar boven komt.
[k2ct8ke] (score 13, diepte 4) Niemand zegt dat het zwijgrecht een schuldbekentenis hebt. Het is de totale collectie van feiten in deze zaak PLUS het beroepen op zwijgrecht.
[k2dxtq0] (score 12, diepte 9) Je bent niet verplicht aan je eigen veroordeling mee te werken. En elke advocaat zal altijd adviseren om je op je zwijgplicht te beroepen. 

Het is natuurlijk zo dat je ook geen berouw kan tonen als je blijft zwijgen, wat zeker invloed heeft op de hoogte van je straf als je op basis van al het andere bewijs toch veroordeeld wordt.

Het zou gek zijn om mensen schuldig te bevindin als ze zwijgen omdat je niets gedaan hebben. Dan zou er ook geen/niet genoeg bewijs moeten zijn voor een veroordeling.
[k2e9j4a] (score 10, diepte 1) Alcohol, drugs, groepsdruk..
[k2eqhk9] (score 10, diepte 2) Ja, je hebt gelijk.

Ik reageerde ook volledig vanuit onderbuik en emoties dus dat is vaak ook niet de meeste logische gedachte
[k2ek0hh] (score 9, diepte 2) Die dingen hebben mij nog nooit laten willen vechten hoor.
[k2dai6k] (score 8, diepte 3) En dat is precies waarom jij niks te zeggen hebt over iemands schuld.
[k2eagbn] (score 7, diepte 9) Volgens mij ben je er bíjna!

Als een rechter je in een strafzaak “iets kwalijk neemt” betekent dat doorgaans dat het meetelt in de straf(maat). En da’s dus precies niet de bedoeling van het zwijgrecht
[k2ctxzi] (score 6, diepte 2) Door het OM of een rechter misschien niet, maar door mij wel.
[k2epges] (score 6, diepte 3) Hilversum
[k2ektlx] (score 6, diepte 4) Alcohol neemt je remmen weg, sommigen worden daar praatgraag van, sommigen flirterig, sommigen melancholisch. En sommigen willen iemand tegen het hoofd schoppen.
[k2epoec] (score 5, diepte 4) Reken er maar op dat ik heel veel te zeggen heb over deze figuren, ook al bepaal ik niet hun schuld.
[k2eqa7h] (score 5, diepte 1) Dat is een beetje tegenstrijdig he?
[k2ew5tc] (score 5, diepte 0) Seniel B.
[k2e03cg] (score 4, diepte 11) Het zou niet uit moeten maken. Je hoeft gewoonweg niet aan je eigen veroordeling mee te werken. De politie en het OM moeten hun werk goed doen en als zij dat doen en je hebt geen berouw getoond dan werkt het wel tegen je.
[k2eks9c] (score 4, diepte 0) lekker brommen. tot nooit.
[k2embyk] (score 3, diepte 12) Nee je snapt het niet. Uiteraard zal een rechter nooit concluderen "lol ja dus" als een verdachte zich op zijn zwijgrecht beroept. Het kan ook nooit bijdragen aan het wettelijk bewijs. Wel kan het bijdragen aan de overtuiging; als jij midden in de nacht met een breekijzer op een verlaten industrieterrein wordt aangetroffen terwijl er net een diefstalmelding is gedaan, dan heb je wel wat uit te leggen. Het zwijgrecht an sich wordt dus niet tegen je gebruikt, maar wel als je geen logische verklaring geeft voor een situatie die om een uitleg schreeuwt. 

Het zwijgrecht en/of leugenachtig verklaren kan wél bij de strafmaat tegen je worden gebruikt omdat zelfreflectie en inzicht in je handelen van groot belang wordt geacht door rechters. Als mensen verantwoordelijkheid nemen is er een fundament om op verder te bouwen en eventueel te werken aan hulp bij het op orde krijgen van het leven van de verdachte. Als dat geheel ontbreekt en je nergens aan mee wilt werken, dan ligt een gevangenisstraf meer voor de hand dan een behandeling.
[k2em88w] (score 3, diepte 11) Klopt, berouw/zelfreflectie kán zorgen voor strafvermindering. Dat is niet hetzelfde als zwijgen dat zorgt voor strafvermeerdering. 

Gezien er voorbij twijfel schuld bevonden wordt als er een straf uitgedeeld wordt, is het het gebrek aan berouw/reflectie dat er voor zorgt dat die straf relatief hoog blijft, en dus niet het zwijgen dat de straf hoger maakt.
[k2ek34s] (score 3, diepte 3) Dat in combinatie met het vorige
[k2h2lo5] (score 2, diepte 2) Ben bang dat een celstraf dit soort mensen nooit anders leert denken. Het is natuurlijk een beetje over 1 kam scheren. Maar reflectie is ver te zoeken

Ik snap ook niet hoe sommige mensen deze denkwijze hebben. Op een gegeven moment verwacht je dat mensen niet hetzelfde denken als jezelf, maar bepaalde basic stuff verwacht ik bij iedereen. Maar dan kom je over deze figuren en z’n vriendjes te weten
[k2ef45d] (score 2, diepte 10) Rechters zien graag zelfreflectie bij de verdachte. Bij een beroep op het zwijgrecht is dat er niet. En als je strafmotiveringen leest zie je dat het niet nemen van verantwoordelijkheid vaak ten nadele van de verdachte wordt meegenomen.

Het zwijgrecht is een recht, maar de rechter heeft de vrijheid daar wel gevolgen aan te verbinden.
[k2ea8zb] (score 2, diepte 4) Maar wat nu als je geen enkele herinnering meer hebt aan het feit dat zwijgen geen schuld bekennen is? /s
[k2fcx9n] (score 1, diepte 11) > Het zwijgrecht is een recht, maar de rechter heeft de vrijheid daar wel gevolgen aan te verbinden.

Het kan gevolgen hebben voor de straf die worst opgelegd, maar het mag geen invloed hebben op de vraag of iemand schuldig is.
[k2ebt3a] (score 1, diepte 0) Levenslang met TBS graag.
[k2fdysu] (score 1, diepte 0) ''Het geheim van Mallorca'' is een interessante podcast op Spotify die hierover gaat.
[k2el5iq] (score 0, diepte 11) Dat vind ik dus weer kwalijk. Van mij mag je je onschuld volhouden en vind ik het onrechtvaardig dat dat tegen je wordt gebruikt. Maar als iemand je vraagt: ‘was je daar?’ En jij beroept je op je zwijgrecht, dan concludeert de rechter: ‘lol, ja dus’
[k2fn41n] (score 0, diepte 7) Het kan je wel verweten worden, maar het is geen geldige juridische grond voor wat dan ook. Reddit heeft geen rechters, en als burgers mogen wij het iemand gewoon verwijten dat ze zich op hun zwijgrecht beroepen.
[k2dy2u5] (score -1, diepte 10) Hangt van de situatie af. Ik denk dat er weinig zaken zijn waarbij dat als enige bewijs opgevoerd zal worden lol
[k2d09nm] (score -3, diepte 4) Waarom dan
[k2dc6ad] (score -6, diepte 6) Je hebt het recht te zwijgen, dat wil zeggen dat je niet verweten kan worden dat je geen verklaring af legt. Dat in tegenstelling tot bijvoorbeeld een getuige. Dat wil niet zeggen dat je er niets uit zou kunnen afleiden. 

De rechter moet vooral logisch blijven nadenken.
[k2dwqrg] (score -10, diepte 8) Nee, het wil alleen zeggen dat het je niet kwalijk genomen kan worden. Dat je niet -op straffe van een nieuw vergrijp- kan worden gedwongen tegen jezelf te getuigen.

=== THREAD tabn49 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-03-09  SCORE: 41  REACTIES: 44
TITEL: Anyone tried the Hoka Ora Recovery Slides? My feet feel better 😌
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hzzppiw] (score 18, diepte 0) Yup…. I wear them everywhere when the weather is nice.   Super comfy.  I’ve had feet issues so I wear them ALL the time at home due to hardwood floors.
[i004ls5] (score 13, diepte 1) I just retired a pair of oofos and picked up the Hoka slides. The oofos are waaayyy softer. Like marshmallows. These are cushioned, but not squishy like the oofos. They are more structured and feel like they'll last a lot longer. If you are familiar with hokas, you can expect the same kind of feeling from the Hoka recovery slides.
[i00g0we] (score 9, diepte 0) Hell yea love the things. Love my Oofos better tho
[i0050rw] (score 8, diepte 1) I work in run specialty. Oofos are extremely soft but sometimes that’s to a persons detriment. I weigh 180 and much prefer the recovery slides since they’re a bit firmer and I don’t compress the hell out of them. To each their own tho
[hzzwflb] (score 7, diepte 0) I love my Oofos but these look even comfier! Anyone know how the two compare?
[i00ye82] (score 7, diepte 2) Curious how you knew it was time to retire your pair of oofos. I've had mine for a few years now, and wasn't sure how long they've lasted for folks. 

Can't wait to add 'lifespan of your recovery slides' to the sidebar, I guess.
[i000wdz] (score 5, diepte 1) I wear mine 365 days per year with socks and I don't have any stank. Source: My wife, who has not asked me to improve my hygiene.
[i00ohfy] (score 5, diepte 2) Seconded. Oofos are softer.
[i006p8z] (score 5, diepte 0) I tried them but didn’t like the prominent arch. They didn’t feel any more comfortable than old running shoes so I returned them.
[i000nyo] (score 4, diepte 0) Rocking a pair as I type this. Gotta love the remote WFH uniform!
[i00f1pn] (score 4, diepte 1) Same. Very prominent arch support makes them uncomfortable if you have flat feet
[i01zxnw] (score 3, diepte 3) Was invited to a running event and meet with a representative at oofos, he said either 6-12 months depending on how often you wear them. Also you can use the thread on the bottom. Everyone I know that wears them until they get to slick or their is a hole in them.
[i0203ez] (score 3, diepte 2) Yeah, I wear mine more for the arch support than the softness underfoot because they aren't particularly soft.

I walk around barefoot at home 99% of the time, but after a super hard or long run if my feet are feeling super beat and tired it can be nice to walk around in these to give the stabilising muscles a bit of a break.

I'm a firm believer in varying stimuli to maximise resilience so I like minimal shoes for casual/gym wear, go barefoot at home, and don't look for or need much arch support in my running shoes, but it can be nice to take a load off when the feet need it. I could definitely see myself becoming reliant on that level of support if I wore them too much and had running shoes with that much support and stiffness too though, so I personally wouldn't recommend using this type of slide too much (unless you actually *need* the arch support, obviously).

If I wanted softness, I'd wear my Novablast's or even semi-retired runners like my Freedom 4's. I really don't get why people say shoes like the Bondi and Clifton are soft. They're supportive and protective, but Hoka's basic EVA is too stiff and dense feeling to feel soft IMO, especially as compared to any supercritical foam and especially PEBA/nylon/TPU based supercritical foams...
[i0086ss] (score 3, diepte 0) Hoka Bondi slippers
[i008pp5] (score 3, diepte 0) I have 3 pairs of these (the flips)
Somehow the v1 were better : softer, wider, better fitting
They kinda screwup something in the v2, and for a reason the v1 were not available anymore as soon as the v2 came out
[i03a0rm] (score 3, diepte 0) I literally wear mine the entire time I'm at home.  The moment I get home I put em  on.
 Most people here are saucony fans but I'm a big hoka fan. 

Work horse: hoka bondi 7
Speed work: hoka carbon x 2
[hzzr7kl] (score 2, diepte 1 OP) I plan to use these as my home slides too since we have hardwood floors as well. My fulltime job also involves standing up for most of the shift so I bit the bullet and bought these
[i0122yu] (score 2, diepte 3) Unfortunately mine were ripping. Didn't really have a choice.
[i00dt0m] (score 2, diepte 2) Agree. I’m about the same weight and the oofos didn’t work for me. I much prefer the firmness of the rubber Birkenstocks when I’m recovering, but I’d like to try these Hokas.
[i01teb0] (score 2, diepte 1) I have both and prefer the Hokas. The oofos are softer but narrower. And my foot expanded over the last year - I got measured and it’s a few mm wider this year. The oofos started to get too tight on my feet. But the Hokas have better structure and I think the muscles of my feet work less in them. I wear them to run errands after my long Sunday runs.
[hzzybs3] (score 2, diepte 0) They're the absolute best. Wear them everyday around the house. Wore Oofos before and it's a night & day difference.
[i01c539] (score 2, diepte 0) Practically live in them, absolutely indispensable.
[i01q408] (score 2, diepte 0) I wear the Hoka recovery slides all day att home. Love them and I think they are helping recovery between running sessions. For people who think they are too firm, they soften with time. The arch support is great imo.
[i01z2w7] (score 2, diepte 1 OP) The arch support is amazing it’s my first day using it and I feel really good.
[j6t822v] (score 2, diepte 3) Ok. I just hope new ora luxe don't have the same problem.
[i3ewtyt] (score 1, diepte 2) Hows the sizing on these?

I find that slides fit larger than a normal shoe, perhaps because there's no longer an upper material that envelopes the toes
[i3fauzf] (score 1, diepte 3 OP) It’s pretty tts. If you wear thick socks with it i would say size up
[i04da54] (score 1, diepte 2) Plus you can just throw them in the tub and scrub them clean.
[i001j4e] (score 1, diepte 0) I’ve really been looking into these lately. Always wear slippers around the house, but thought these would be superior. I think I’d mostly be barefoot, but any opinions if they’d fit too tight with socks?
[i01ynsu] (score 1, diepte 1 OP) They are snug with socks on. I prefer wearing it without socks.
[i00asty] (score 1, diepte 0) never tried the hokas but the oofos are awesome.
[i00dkxf] (score 1, diepte 0) was thinking about these but went with some birkenstocks instead, the lift in the back was just too much for me
[i00lmbr] (score 1, diepte 0) How do these fit to size? There are none in my area but I can order them.
[i01yvgt] (score 1, diepte 1 OP) I am 9.5 in sneakers (Hoka, Brooks, Asics, Saucony, NB) but i got 10 for these. These come in whole sizes anyway. I guess if you’re between sizes just size up since they are snug with socks on.
[i024ort] (score 1, diepte 2) Thanks! Ordered a pair for my husband and a pair for me. They’ll arrive tomorrow!
[i01chci] (score 1, diepte 0) They are amazing, great value too!
[i01z4bw] (score 1, diepte 0) My go to around my apartment after runs in the morning. I work from home and these have saved my legs so much. I have hardwood floors too and I love how structured they feel, but still soft enough to give you a little more comfort.
[i020bml] (score 1, diepte 0) I wear mine all the time inside. Inside only. I have the light sea foam green ones with the blue bottom on right now. At first they felt weird but I LOVE them lol
[i026td4] (score 1, diepte 0) I have those and I like them. My only gripe is that in the winter, my house is a firestorm of static electricity and it seems to be noticeably worse when I’m wearing them.
[j6t1u85] (score 1, diepte 1) Are you talking about the hokas? I ordered hoka one one ora luxe. And im worried about static electricity. I have alot of metal and a mini fridge in my room. And get static  with most sandals when I touch it. Do you think I will have the same problem with the hoka ora luxe?
[j6t5kro] (score 1, diepte 2) Yes, the hoka recovery slides.
[i02ljzi] (score 1, diepte 0) Don’t sleep on Skechers hyperslide. My favorite slippers to wear in the house. Your feet make direct contact with some hyper burst and it’s amazing.
[i09z2fg] (score 1, diepte 1) Shiet, if that strap wasnt stitched on I wouldve considered it. They tend to rip apart from an accident of someone stepping on the footbed itself. I just dont trust them having ripped a few in the past
[i02xa9h] (score 1, diepte 0) I practically live in mine and I am on my second pair. I had my first ones for a couple of years and they served me well. So nice to get them on after a hard run etc.
[i05p7tr] (score 1, diepte 0) I'm using the recovery flip flops at home around the house to help recover from insertional achilles tendonitis. (Nothing to rub on my sore heel = great) I did buy some Dr. Scholls gel heel lifts to set on them in the back. They stay in place at home to help keep my heel lifted a bit while I recover.

Good sandals though for sure. Nice orthotic shape with an arch and all.
[i0940j0] (score 1, diepte 0) I just went to a camping festival and wore these when we weren’t going to stages. So comfy. Wear w socks tho
[iayzdef] (score 1, diepte 0) I have a pair of clifton size 10.5, should I get the Ora in 10 or 11?
[iaz5m44] (score 1, diepte 1 OP) Just get the 11, people in between sizes say it can be snug
[iazf4kw] (score 1, diepte 2) Thanks!
[hzzs7ra] (score -2, diepte 0) Very warm in summer. If you wear it with socks in winter, socks can soon cause foul odors.

=== THREAD 112w6n7 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2023-02-15  SCORE: 2  REACTIES: 44
TITEL: Looking for a comfortable shoe to get started running
POST (source_id=post):
I got Nike Pegasus 39, used it for a couple of days and my feet really hurt, felt it's tough on the foot, so thinking of returning them and buying something else, can you suggest me a few shoes which are comfortable for short distance runs  


I weight 80Kgs/176.37lbs  
Netural Foot arch  
Just started running   


I was thinking of either going with Nike Invincible 3 or Asics Novablast 3 or Nike Infinity 3  
If you have any other suggestions I'm open to them!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j8mkei2] (score 5, diepte 2) The Pegasus is a great running shoe for beginners, but if you didn't like running with it, you have to determine what characteristics you didn't like and look for another shoe without those characteristics, and with the characteristics that you do like.

In terms of cushioning the shoe can be either soft, responsive or firm, you have to decide what you preference is to start looking for that characteristic.

In terms of stability the shoe can be more or less stable. But generally the amount of stability is in some way (but not exclusively) related to the amount of cushioning, in most cases the more cushioning the shoe have the less estable it is.

There are many shoe characteristics that are interrelated like the previous example, so you have to set your preferences and priorities and search for the best running shoe for those preferences and priorities, and be prepared to accept that maybe you wouldn't find the ideal running shoe.
[j8mqid4] (score 4, diepte 6) I am sorry but I can't help you there, I haven't run in those shoes because I don't like soft shoes.

From what I read the Nike Invincible 3 are maybe what you are looking for.
[j8mlzub] (score 4, diepte 0) Invincible 2
[j8mmhyu] (score 3, diepte 3 OP) Okay, what I didn’t like about Pegasus was it felt hard on my foot, every step I took hurt my toes and knees. I was also wondering if I got a fake one since I bought it online from and not from Nike.com 

And I think I’m definitely leaning more towards soft and cushioning shoes
[j8mnakb] (score 3, diepte 4) OK, as you have said you can try the Nike Invincible 3 or Asics Novablast 3, or maybe the Brooks Glycerin 20, New Balance Fresh Foam X 1080 v12 or Saucony Triumph 20.
[j8mnttm] (score 3, diepte 2) How about the width?
[j8mqexh] (score 3, diepte 4) I would try shoes that offer a wide option to see if it helps.
[j8msp1r] (score 3, diepte 5 OP) Got it, Thanks!
[j8mgwkq] (score 2, diepte 0) What kind of ride (soft, responsive, firm, stable, etc.) do you prefer?
[j8mhbx9] (score 2, diepte 1 OP) I’m just starting out, looking for something that is soft, responsive and stable 

This is a mixed answer I know but I don’t know how else to put it? Hope this helps 
Sorry if it’s confusing
[j8mslxq] (score 2, diepte 7 OP) Okay, thanks for helping me out!
[j8mj0e7] (score 2, diepte 0) You could try Asics Gel Nimbus, Saucony Triumph, New Balance 1080, Brooks Glycerin, Hoka Clifton
[j8mmkhe] (score 2, diepte 1 OP) Couldn’t find them anywhere here only the Invincible 3 is available
[j8mo3ng] (score 2, diepte 2) Where abouts are you? I haven’t read about the 3 but if it’s the same as the 2/better you’re golden
[j8mqim8] (score 2, diepte 4) They’re gonna feel better than the Pegasus if comfort is what you’re after. They’re heavy but blissful for easy runs.
[j8mm9p9] (score 2, diepte 0) Sounds like the shoe was either too small or you have wide feet and you don’t realise it.
[j8n4ky2] (score 2, diepte 7) To piggyback on this.. is there way of knowing how much difference the normal and wide option is?

Is it like 2mm, 5mm etc.. or is there some way to find this info out?
[j8n4pmw] (score 2, diepte 8) Should have said. I bought Clifton 9s today and absolutely love them but after about 3k I started getting rubbing at the front so I think I need a smaller but wider shoe, just for context
[j8mn1ir] (score 2, diepte 0) Not a fan of Pegasus either. The 38 caused me a foot injury.

I can recommend Gel Nimbus 23 or 24. Note that the 23 is a bit more clunky and runs warms but great for beginners and for knocking out mile after mile. The 24 is an upgrade and a lot more refined. If you opt for either of those, go half a size up.
[j8mqsmp] (score 2, diepte 3) Yes, this is the latest one released this month. I don't own it as I wasn't happy with the changes and the 'grip' of the sole. It won't suit where I run so I have switched to Novablast 3 TR. Which I am taking on their maiden voyage today funnily enough
[j8msr31] (score 2, diepte 4 OP) Okay how are the Novablast 3 TR?
[j8mqrpp] (score 2, diepte 0) I'd give the pegasus another few goes, I found the 38s really hard on the feet at first but they softened up after 50k or so and have lasted for ages since.
[j8ms6ni] (score 2, diepte 0) Try the Invincible or New Balance 1080. Both are pretty damn soft
[j8mzcxd] (score 2, diepte 0) I'm a fairly big unit (86kg) and have been running in Mizunos for years without issue. Currently on Wave Rider Neo2. Riders are great shoes for beginners, particularly heel-strikers, and are reasonably wide. I've tried Nike in the past, and found them too narrow and unforgiving (same with Adidas recently, Boston 11 tore my instep up), so this could be a nice option for you. Plus you can pick up previous versions for cheap.
[j8ngrqr] (score 2, diepte 1 OP) Will check it out, thanks!
[j8n111s] (score 2, diepte 0) If you want a soft ride try the Hoka Clifton 8. You'll probably want to get it in wide size instead of regular size. 

I suggested you get the Clifton 8 because Hoka just launced the 9 and you can get the 8 cheaper, it's basically the same shoe.
[j8ngtza] (score 2, diepte 1 OP) Okay, will check it out. Thanks!
[j8mpzd8] (score 1, diepte 5 OP) Which would be your top 2 picks from those?
[j8msr7k] (score 1, diepte 8) 👍
[j8mpppf] (score 1, diepte 1 OP) Which are top two in those?
[j8nsvri] (score 1, diepte 2) Different shoes work for different people. If possible I would recommend going to your local running store and trying on a bunch of different options, and seeing which ones feel best to you!
[j8nvb3s] (score 1, diepte 3 OP) The things is there is no local store where I stay, depending on online services is the only option or else need to travel to other cities
[j8oavaz] (score 1, diepte 4) If softness is a priority for you, I would probably try New Balance 1080 and Saucony Triumph.
[j8mpnv6] (score 1, diepte 3 OP) India
[j8mpxhv] (score 1, diepte 3 OP) https://www.nike.com/in/t/invincible-3-road-running-shoes-Wwmmlp/DR2615-001
[j8msog6] (score 1, diepte 5 OP) Okay I’m leaning towards it even though they’re bit high on the price
[j8mnojm] (score 1, diepte 1 OP) Here’s the [image](https://imgur.io/a/VUnmpKp) of shoe beside my foot, there’s one thump gap between my toe and the top of the shoe
[j8mpn4s] (score 1, diepte 3 OP) It does feel a bit tight
[j8msq8i] (score 1, diepte 6) >Got it, Thanks!

You're welcome!
[j8mpqsw] (score 1, diepte 1 OP) Okay, will check them out! 
Thanks!
[j8mqgmw] (score 1, diepte 2 OP) > Gel Nimbus 23

found Gel [Nimbus 25](https://www.asics.com/in/en-in/gel-nimbus-25/p/18683201/15720623)
[j8nmjry] (score 1, diepte 5) I just got back from a 11km in them. I wanted to love them, have been really excited but i can't find the perfect size. Half size up is just too big on the left foot. Whereas half a size down (regular size) is too tight. As a result they felt unstable and I am not used to the stack height, felt like I would roll my ankle on every turn, plus my foot would slip slightly inside the shoe. Other than that, a blister already formed on my middle toe. A shame as they are aestically really nice and so light!

A lot of people love them and I can see why. Unfortunately not for me given the weird sizing. Wish ASICS kept their sizes in check as half a size up on Gel Nimbus is a perfect fit
[j8msvyg] (score 1, diepte 1 OP) Okay, for me they hurt a lot and not comfortable
[j8mssv8] (score 1, diepte 1 OP) Okay will try them!
[jczk830] (score 1, diepte 1) Which invincible?
[jmuce1b] (score 1, diepte 0) Which ones did you go with OP?
[jmud56x] (score 1, diepte 1 OP) Ended up with Asics Gel Nimbus 25, happy with it!
[jmufy15] (score 1, diepte 2) Are they wide? I have feet width of 4.5 Inches.

=== THREAD phgz4d ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2021-09-04  SCORE: 6  REACTIES: 43
TITEL: Endorphin Speeds not for me?
POST (source_id=post):
I’ve been running in Saucony Triumph since ISOs, and recently transitioned to Triumph 19. I purchased Saucony Endorphin Speed (same size as Triumph) for a an upcoming marathon in Nov. Today was my first run in Speeds. First four miles felt great, I felt the bounce, running felt effortless. I was watching my form throughout my 8 mile run. Last two miles the outside of my right foot started to hurt and I noticed pronation (rolling my inwards). Needless to say, I’ve been wearing neutral shoes and they work fine for me.  Has anyone else experienced this? Oh also, the toe box feels slightly narrow, didn’t bother me but that could because it was a relatively short run. Should I continue training in these or do I risk injury? Really bummed, was hoping these would shave some time off on race day.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hbiwh40] (score 9, diepte 0) The Speeds wrecked my calf, did something to my gastrocnemius muscle. Not sure if it was the instability or the speed roll geometry, but I had to return them. Felt like such a fun shoe though.

I ended up getting the Puma Deviate Nitro and, even though the upper is pretty bad, it has the ride for me that I wished the Speeds had
[hbikb5k] (score 8, diepte 0) Yeah being that the foam has a bit of give it can get kinda unstable. I got very mild pronation on my left foot and running in the triumph 18 I got no issues but shows with a narrow mid foot/heel and soft midsole makes it worse. What I did which helped but didn’t completely make pronation go away was go up a half size. I’m a 9.5 and definitely need a 10 in the speeds not the case with kinvara/triumph/ and freedoms
[hbj1v27] (score 5, diepte 0) Endorphin Speeds feel waay too unstable for myself as well. You're not alone.
[hbj0o85] (score 4, diepte 1) Interesting bc the rocker is supposed to unload your calves and the speeds do that for me and I’ve had soleus issues prior to switching to them. But if I’m not careful their instability does bother my ptib. I’m on v2 and the ride feels slightly different than v1 to me but I really wish they’d made the midfoot base wider to aid stability. Might try RC2 eventually for that reason.
[hbjrxkf] (score 4, diepte 0) I agree with you, my right foot rolls in a fair bit in these; even just standing around in them, never feels like I can stand properly, is slightly better when I’m running and almost disappears at faster paces. As I’ve gotten quicker it’s becoming less of an issue. But I don’t think I’ll be getting another pair when I’ve gone through this.
[hbks3r4] (score 4, diepte 0) My initial runs in the Speed 1 had me feeling the same pronation, but as my mileage got higher and my body got used to them it’s not an issue at all anymore. I’m at 60 miles in mine (3 shoe rotation all at 50+ now) and they’re hands down the funnest shoe I’ve ever run in. To me you have to learn how to run in them and let your body be strong enough to handle it.
[hbm9zud] (score 4, diepte 0) With so many people having picked up Endo Speeds in the recent sales, I think we're now seeing a whole bunch of these stories coming in. I'll add that I ran a PR-pace 5k in mine a few weeks ago and came away with extensor tendonitis that sidelined me for nearly 3 weeks afterwards. I'm not blaming the shoes necessarily - it could have been a combination of a variety of different factors. But a 5k is an extremely short distance for me, and even running it at my hardest pace has never left me with any foot problems before. So I'm really conflicted - on the one hand, I'm pretty certain I wouldn't have PR'd without these shoes. But I don't want to pay for it with several lost weeks every time I want to run a solid race.

I'm taking them out on some longer, slightly gentler runs soon to see how they do. Hopefully my issue was more related to other factors (some recent tightness I've had in my calves, too much mileage in recent weeks, etc).
[hbinowy] (score 2, diepte 2) I personally went up a half size. My big toes had room but my little toes were scrunched. I’ve enjoyed my runs with the Speeds but also have issues with stability and my ankles have been sore but I’m only around 40 miles so far.
[hbioulb] (score 2, diepte 2) Yeah so 9.5 which is my “true to size” fit was narrow but really it was just too short in length. Width was roughly the same in the half size up but length was perfect
[hbislpp] (score 2, diepte 3 OP) You know what, yes, it’s too short as my big toe bumps up against the toe box.
[hbip9rt] (score 2, diepte 2) Def go up half size up in Speeds
[hbmqrlr] (score 2, diepte 2) No, was using as fast day/long run shoe. Maybe I should have given them more time, but I just couldn't get past 5-6K without calf pain that I have never experienced in any other shoe
[hbmwlul] (score 2, diepte 3 OP) I’m with you, I’m afraid to cause irreversible or prolonged injury as I have a race in 60 days.
[i20hk2r] (score 2, diepte 1) I've been using the speeds alot lately and have noticed them giving me some serious calf/achilles problems. I'm hoping it just clears up over time... Feels like those shoes destroy me.
[hbphhbc] (score 2, diepte 2) Give the Hoka Carbon X2 a try. They're firmer and more stable IMO.
[hbq8a4u] (score 2, diepte 3 OP) Thanks! It’s funny how you pointed to “they are firmer” Coz that’s what I dislike about Hoka, they are way too squishy, giving a weird running on mattress feeling. I’ll check them out.
[hbq8fxr] (score 2, diepte 4) The Glide line (Clifton, Bondi, Rincon) are cushy, but the Fly line is firmer. And the plate makes it much firmer as well.
[hbjg532] (score 2, diepte 0) What sort of pace were you running?  Are you a heel striker?

&#x200B;

I too been having hard time adjusting to Speeds when doing slower long runs (9-10 min miles).  I also notice at these slower pace, I'm landing more on my heel where I encounter pronation.  Even when I'm just standing, any weight near the heel is prone to instability.

The only time the shoe work best for me when running 10k at \~7:25 min pace.  When I'm landing more mid/forefoot, I don't notice heel instability.

The cushion is great and I notice faster pace.  But during my marathon training, I'm trying not to go fast and have to concentrate more on my foot planting when going slower.

I've had more success with New Balance 1080v10 during training.  It's a neutral shoe, lots of cushion, wider base that more stable.  I can cruise easy miles without thinking about my foot strike.

&#x200B;

Unless endorphin pro have any difference with stiffer plate, I'm also torn not being able to use the endorphin come race day.
[hbsu1tc] (score 2, diepte 1) I experience the same as you. When I walk or stand my foot rolls inward. I bought one pair a half size larger and another pair my normal Saucony size, both do the same. What I found works best is to tighten my laces tighter, run faster, and shorten the distance of my runs. So in other words, I use them for speed work, fartleks, etc. I can’t seem to get the longer distances perfected but as I get better at my form, I’ve found my stability issues improving.
[hbu1105] (score 2, diepte 2) I’ve got narrow feet anyways so when I tie my laces the eyelets are nearly meeting already, any tighter and my feet hurt/go to sleep. Only thing I’ve really found is going faster solves the issue, which isn’t ideal if I’m doing a 15min easy warm up before a hard session as I spend that 15min constantly worried about my ankles etc. Think when these are done I might go for something like the rebel 2 perhaps
[hbubywj] (score 2, diepte 4) Oh really? I’ve raced once in the vaporfly and loved them, had no issue with width, stability etc, just felt great. Maybe I just need to win the lottery or become an Olympian so I can get unlimited pairs of them to run in 😂
[hbjwx1y] (score 2, diepte 0) They caused me problems all over, despite initially feeling faster. It did improve in that I don't get sore now but I've yet to have a good longer run at any pace. It's possible they actually make me slower.
[hbnsxqh] (score 2, diepte 2) According to doctors of running review, the upper update on speed 2 improved heel lockdown.  still has same platform as speed 1 with narrow heel base.

[https://www.doctorsofrunning.com/2021/06/saucony-endorphin-speed-2-multiple.html](https://www.doctorsofrunning.com/2021/06/saucony-endorphin-speed-2-multiple.html)

Perhaps consider using the Triumphs or shoe that feels comfortable for long runs, and slowly build up volume/intensity with speeds on short runs.

I'd myself would opt for avoiding the injury risk especially as dates near and go with a shoe that familiar and gives no issues over the long distance.
[hbksqve] (score 2, diepte 0) Same experience as me.

Narrow toe box: ordered in my usual Saucony size (worn Triumphs, Rides, Shift etc.) and it gave me blisters on the outside of my little toe. More recently, caused some significant inflammation in my toe - felt like I'd broken it!

Instability: every time I ran in them my posterior tibial tendonitis flared up. Ironically, I have one flat foot and it was always the normal leg it bothered!! 

Sold.
[hx0qrhl] (score 2, diepte 1) I feel calf tightness just walking around in them. There’s something up with the geometry that isn’t comfortbale. I wish it was more like the rebel V2, where the moment you put them on, its like a cushion that’s an extension of your foot.
[hbl7ln3] (score 2, diepte 0) Now I’m worried as I ordered a pair last week…. My current rotation are v1080 and rincon2. 😬
[hbnvals] (score 2, diepte 1) definitely give the time and right conditions for speeds.  The high stack and squishy foam is unforgiving for anyone that relies on stability.

I've been loving my 1080 for long hauls.  I ran in stability shoes for longest time and 1080 were pretty easy to transition to as neutral shoe.
[hbilezj] (score 1, diepte 1 OP) Thank you. Did you also find the toe box of Speeds to be narrow in size 9.5? 
I am size 9.0 in Triumphs, could go half size up in Speeds.
[hbinpva] (score 1, diepte 3) 40 miles is 64.37 km
[hbisu3c] (score 1, diepte 3 OP) 40 miles is enough to get an idea of a pair of shoe is right for you or not. Hmmm..I am wondering if the problem of pronation will go away. I prefer some structure in mid foot, which is why I like Triumph.
[hbisv02] (score 1, diepte 4) 40 miles is 64.37 km
[hbm4w81] (score 1, diepte 1 OP) Were you wearing Speeds as your daily trainers?
[hbm52p4] (score 1, diepte 1 OP) Good to know, thanks. Do you know or have tried a good alternative?
[hbqc2yu] (score 1, diepte 1 OP) This is a dumb question, how do I know if I’m a heel strikers or mid foot or fore foot striker?
[hbqezbs] (score 1, diepte 2) What part of foot touches the ground first. 

Usually walking and slow speed, ppl land on their heel first. Going faster or barefoot are landing mid to forefoot. 

You can check outsole of your shoes, see whether it’s has more wear around the heel or elsewhere.
[hbjjvjy] (score 1, diepte 0) You are not the [only one.](https://www.reddit.com/r/RunningShoeGeeks/comments/pff4oq/it_was_hard_to_accept_that_the_endorphin_speeds/?utm_source=share&utm_medium=ios_app&utm_name=iossmf)
[hbu85t7] (score 1, diepte 3) I haven’t tried the rebel 2 but I read for some people they cause the same issue. I have the Nike Vaporfly Next% and have no issue with them.
[hbuemxi] (score 1, diepte 5) Yeah exactly, I’ve had mine for almost a year with about 40-50 miles on them as I only used them for a few races
[hbmwodf] (score 1, diepte 1 OP) The last few miles I had to slow down significantly.
[hbks4ov] (score 1, diepte 1) 60 miles is 96.56 km
[hbmr18r] (score 1, diepte 1 OP) Thanks. I’m training for a marathon in November, I’m afraid risking an injury. I wonder if Speeds 2 have same issue.
[hboq8c8] (score 1, diepte 2) Ya I don’t need stability so I’m hoping to use them for tempo and threshold runs mostly.  The 1080 just fits so perfectly in every way. Love that shoe.
[hh6acnd] (score 1, diepte 0) I like how they feel, but the inside of my left knee hurts on the surface.  This is the second time I have tried these shoes.  When a put a different pair on like the Reebok Symetrios, the pain goes away.  I guess these are not for me either.  If I was going to adjust to them, it would have happened already

=== THREAD 1m8k3ks ===
SUBREDDIT: r/Shoes
DATUM: 2025-07-24  SCORE: 5  REACTIES: 40
TITEL: Softest shoes ever?
POST (source_id=post):
I’m NOT looking for running shoes, and I’m NOT worried about what brand is “cool”. But, my feet have been killing me for years, and I used to always wear Nikes. But my friend got me to check out Skechers, and I got some D’LUX WALKERS (pensive) and they were INCREDIBLE. No more foot pain AT ALL. However, these shoes wore out in like a month and a half. And now the cushion is totally gone.
So my question is:
What are the absolute softest shoes I could possibly buy? 

Max cushion Skechers were good, but also wore out. I went to a store and tried on HOKAS, and they were honestly trash. And the asics nimbus 27 felt great, but I didn’t try “on cloud” yet.

I’m sorry that that’s a lot of information for 1 question. But I just don’t need a bunch of debate, and opinion. I just need THE softest shoes I could possibly buy.

Any suggestions?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[n50eydp] (score 7, diepte 0) Any fluffy-puffy-marshmallow-cloud shoe is going to wear out rather quickly. The softer, the faster. 

It’s just a matter of physics. You’re putting weight on something for hours on end, it’s going to compress down. 

The reason you think HOKAs are “trash” is likely because there’s firmness in the midsole & the foam has enough density to last longer (and be more stable).
[n509x11] (score 6, diepte 0) try replacing the insoles on the shoes you like.
[n50oeej] (score 6, diepte 2) Not necessarily. Varieties of foam each have their own characteristics re: longevity, softness, etc. If you want something to last, a higher density EVA or PU foam would be ideal. 

There is certainly a trade-off. It’s just a matter of what works best for you.

ALSO, I can’t believe I forgot this: rotate your footwear!!! Especially cushy shoes! They need time to recover from the compression that occurs during wear. You’ll get a longer life out of *both* pairs if you buy two.
[n5025dn] (score 5, diepte 0) Brooks! And I think they have a nice look to them as well
[n501356] (score 2, diepte 0) Vionic makes sneakers/walking shoes with a lot of cushioning and you can get them at places like DSW where you may get a better price. If you’re a member of Rakuten there’s a 2% rebate offered with DSW currently.
[n56me4s] (score 2, diepte 1) I switched to Brooks after wearing Hokas.  Love them...I have the Ghost Max 2 and my feet are very picky; I also wear orthotics and I love them.  I also find Allbirds very comfortable.
[n50ajgl] (score 2, diepte 0) Aside Gel Nimbus
[n50at5f] (score 2, diepte 0 OP) Thanks so much, everybody!! I’m definitely gonna go on a quest to find and try on all of these suggestions!
[n50fo43] (score 2, diepte 1 OP) So, does that mean there’s no “long lasting” solution? And that only firmer shoes last longer?
[n50nkob] (score 2, diepte 0) Don't laugh... I've gotten sneakers from the brand Dr. Scholls... those were soft and light... like a slipper. I think I may have bought them from Walmart... maybe $25-30?

I'm not real hard ln my shoes, so I can't speak to durability. But I do think they were in the work shoe section, so it's probably not completely disposable.

I suppose you could also try moccasins and just add a memory foam liner, and a glue on sole? That would be really flexible and light... letting you focus on the soft? 

Last chance, not sure if they still make Hushpuppies, but my Grandma was a teacher Nd swore by those for herself. You might legit have to look in a paper catalog like "Women Within" etc
[n50pjup] (score 2, diepte 0) try fit flops! I have some super skates I've had for years - still soft & cushiony!
[n501fty] (score 1, diepte 1 OP) Thanks so much! Will definitely check them out.
[n50b3ar] (score 1, diepte 0) I have foot pain and gel nimbus solved that. Walking on a cloud though its not quite the feel if you compare that to something like the Skechers you mentioned. And yes sketchers all wear out quickly.
[n50nd9y] (score 1, diepte 2) Not necessarily. Varieties of foam each have their own characteristics re: longevity, softness, etc. If you want something to last, a higher density EVA or PU foam would be ideal. 

There is certainly a trade-off. It’s just a matter of what works best for you.
[n50o9cy] (score 1, diepte 3) Not necessarily. Varieties of foam each have their own characteristics re: longevity, softness, etc. If you want something to last, a higher density EVA or PU foam would be ideal. 

There is certainly a trade-off. It’s just a matter of what works best for you.

EDIT — I can’t believe I forgot this: rotate your footwear!!! Especially cushy shoes! They need time to recover from the compression that occurs during wear. You’ll get a longer life out of *both* pairs if you buy two.
[n50ipwf] (score 1, diepte 0) I like altra but go to a running store and get fitted and get guidance.
[n50jjdx] (score 1, diepte 0) What makes you say the Hokas were trash?
[n54uku0] (score 1, diepte 1 OP) There is a previous response somewhere talking about the more firm midsoles, which gives them better longevity. But I tried to Bondi 9’s at the store, which are supposed to be the softest. And they were still much firmer than the other ones I tried that day.
[n55xg3y] (score 1, diepte 2) If you can find them you might try Bondi 8. Apparently there was a bit of a design change after Bondi 7, and the Bondi 9 is closer to the 7. But the 8 is like walking on marshmallows. In feel and looks, lol. I saw another thread awhile ago where someone said his wife bought him a new pair of Bondi 8s for their trip to Disney World, and I thought that sounded just amazing.
[n568i9l] (score 1, diepte 3) I wear the Bondi 8 and they’re wonderful
[n50qsfm] (score 1, diepte 0) Unpopular opinion: the ALO’s recovery shoes works best for my feet. I developed flat feet after years of bad posture so all shoes felt uncomfortable. My plantar fasciitis aren’t flexible so firm sole doesn’t work on me as well. The ALO had thick soles memory foam-like so it was helpful for prolong walking and standing.
[n51490c] (score 1, diepte 1) Second Vionic. Was turned onto the brand by my childhood best friend who is an ER doc, on her feet all day. I have 3 pair now. My newest pair are these bright red Mary Jane’s. I could walk in them all day.   But the biggest game changer for me was giving into Birkenstocks, after many years of resisting them because of their appearance. They are so comfortable after they mold to your feet. I’ve had the Arizonas in matte gold for a couple of years now. They are my most worn. Go with everything. I also have black Boston clogs that I really only wear in winter (no socks! I’ll do a lot for comfort but socks with clogs is a bridge too far, for me). I recently got the big buckle Madrid in burnt orange and they are so great!
[n51fn8i] (score 1, diepte 2) I love the gold ones. I only got those cause they were on sale but I get so many compliments on them.
I always get the soft foot bed too.
[n514mbk] (score 1, diepte 1) Why is this an unpopular opinion? I just looked them up and think they look great!
[n516ajq] (score 1, diepte 2) Apparently a lot of people said aesthetically it looks like clown shoes with the thick and rounded tip.
[n50rqrt] (score 1, diepte 0) Just wanted to pop in and agree that the ASICS gel nimbus shoes are divine! I’ve had them for four years and they have held up really well. 

I also have a pair of Brooks Ghost 16s I got recently, and they’re super comfy — I mostly use them for running, but my partner works a job where he’s on his feet all day and the Ghosts are his everyday shoe; he says they’re the most comfortable shoes he’s ever worn.
[n50smjm] (score 1, diepte 1 OP) Thanks so much!!
I saw a list today that put the nimbus 3, the Brooks glycerin max 2, and the new balance fresh foam more v5 1. Any experience with the new balance?
[n514xwg] (score 1, diepte 2) I bought the new balance, a brand I adore and have worn for decades. I felt like the extreme fresh foam feel unstable. Too much foam. YMMV. 


I still wear New Balance, but I went back to the regular running shoe I’ve worn for ages.
[n51al99] (score 1, diepte 3) NB' run small.  Order a half size larger
[n550qbz] (score 1, diepte 4) The lifestyle NB I ordered a half size larger and they are too big to wear comfortably. I stuff tissue paper into the toes when I wear them. But I rarely wear them because who wants to wear a “comfortable” pair of shoes with tissue in the toe? 

I can’t remember re: fresh foam because I was distracted by the instability.
[n51eqik] (score 1, diepte 2) I posted above, but New Balance is my favorite of all the ones I've been trying (including both of those from Books and the Gel Nimbus). 

I got the NB 880, but I did almost get the More v5 and the 1080s. They're pretty similar tbh, I'd say 1080 is the most cushy, with More and 880 having a little more firmness, but still very plush.
[n548e2b] (score 1, diepte 2) New Balance and Brooks are my go-tos. My comfiest pair of shoes ever have been the NB 327s. I don't know how much walking you're doing, but they haven't given out.

I also wear them with Superfeet insoles, as directed by my podiatrist. I have had multiple broken bones, bone spurs, and plantar fasciitis, so comfort and support is paramount.

If your feet have been killing you for years, I highly suggest seeing a podiatrist. A couple cortisone shots, better insoles, and specific stretches really helped me.
[n50v08w] (score 1, diepte 0) All these cushioned running shoes don’t last forever. Alternating pairs helps because the foam dries out and rebounds. All Nikes are not the same. The $60 ones at Kohls are not the same as a $160 pair at a running store. Also fitting your feet is super important. The shoe that feels amazing to me, might feel like rubbish to you.
[n50v35s] (score 1, diepte 0) I also like soft shoes and boots. I like Brooks Glycerin, Saucony Ride, Clarks Unstructured or Artesian. Uggs and Sam Edelman boots. Bare Traps and Sketchers flip flops. 
I haven't found any dress shoes or sandals that suit me. I'm extremely picky about fit and comfort with shoes and socks.
[n517yfw] (score 1, diepte 0) You might need arch support. I have plantar fasciitis & the Hoka Bondis & Cliftons are the most popular models for PF. Sketchers are also popular for it. 

But I must have my insoles. And they’re hard plastic. I have to mold them to my feet using the oven. I buy the SOLE brand “red active medium” and can get by with using them in some of my other shoes also, but if I’m doing a lot of walking it has to be my Hokas. It’s tough to find shoes with removal insoles, so sometimes I just rip them out so mine can fit.
[n518fdj] (score 1, diepte 0) I discovered Orthofeet after I broke my foot. 5 years later and I still wear them all the time. Love them.
[n519fg5] (score 1, diepte 0) I always say my vapormax's are like walking on a cloud. Pricey but the most comfortable shoes I've ever worn
[n51e6kt] (score 1, diepte 0) I've been on the same quest as you, lol. I will say from what I've learned (and am discovering in my testing) is the cushy/soft feels amazing at first, but after you wear them a while, your feet just sort of...want some support/firmness. (Sort of how with a super fluffy pillow, over time you'll sink lower and lower until you're flat on the bed.)

So I think the trick, for me at least, is to find something in the middle, but more than that is shoe rotation. Whenever I'm on my feet for a long time, I try to bring a second or third pair to swap between. Makes a HUGE difference, maybe even more than the actual shoe itself.

I've tried...a lot. lol Brooks, New Balance, Hoka, Asics, Altra, Topo, Saucony...

My favorite so far is the New Balance 880, but here are my other contenders. 

New Balance - 1080

Asics - Gel Kayano

Saucony - Triump

Brooks - Glycerin, Glycerin Max, Ghost Max
[n51fdd4] (score 1, diepte 0) I've been wearing hoka bondis for years.
I have a lot of weird things( failed bunionectomy despite the three screws still in my foot because of a genetic collagen disorder)
Congenitally fused tarsal coalition, and chronic anterior tibialis tendinitis.
( and that's just on my left foot 🤓)

I was on crutches for a while, but alternating my hokas with Birkenstocks and wearing my brace for tendinitis a couple times a week have been enough so that I don't even need a cane.

Imo, Hokas are the gold standard for cushy.
[n51onzr] (score 1, diepte 0) I like the gel technology in ASICS. The higher end ones tend to have more gel like the 360, they do a 180 too. The nimbus suggested are a good shout too. 
The gel doesn't wear down or compress the same way foams do. 
A good insole will always enhance too.
[n53vo5q] (score 1, diepte 0) You said Hoka are trash but did you try different styles???  Mine are Bondi and they are amazing.
[n577vwf] (score 1, diepte 0) asics novablast 5
[n5d9lkn] (score 1, diepte 0) Oofos recovery sandals and clogs.
[n5he1x3] (score 1, diepte 0) I got Brooks this year and I’ll never go with another brand. They are sooooo comfortable. I’m a nurse, and I’m on my feet…

