"""Bouwt de HTML voor het Google Doc met het VOC-onderzoek. Citatenbank komt uit de database.

Gebruik: python scripts/build_research_doc.py data/reddit.db uit.html"""
import html
import json
import sqlite3
import sys

DB = sys.argv[1]
OUT = sys.argv[2]

e = html.escape
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

KIND_NL = {
    "pain": "Pijn", "impact_on_life": "Impact op leven", "desire": "Wens", "objection": "Bezwaar",
    "works": "Werkt", "fails": "Werkt niet", "copper": "Koper", "buying_trigger": "Koopmoment",
}
quotes = []
for r in conn.execute(
    "SELECT p.id, p.subreddit, p.permalink, l.data FROM posts p JOIN labels l ON l.post_id = p.id WHERE l.relevant = 1"
):
    lab = json.loads(r["data"])
    for q in lab["quotes"]:
        link = f"https://redd.it/{r['id']}" if q["source_id"] == "post" else f"https://reddit.com/comments/{r['id']}/_/{q['source_id']}"
        quotes.append((q["kind"], q["text"], q["nl_meaning"], r["subreddit"], link))
order = ["impact_on_life", "pain", "desire", "objection", "fails", "works", "copper", "buying_trigger"]
quotes.sort(key=lambda x: order.index(x[0]))


def table(header, rows):
    out = ["<table border='1'><tr>" + "".join(f"<th>{e(h)}</th>" for h in header) + "</tr>"]
    for row in rows:
        out.append("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>")
    out.append("</table>")
    return "".join(out)


def q(text):
    return f"“{e(text, quote=False)}”"


parts = []
P = parts.append

P("<h1>Koperen inlegzolen: wat klanten zelf zeggen</h1>")
P("<p>Voice-of-Customer-onderzoek op Reddit, aangevuld met het eerdere onderzoek uit het Launch Blueprint "
  "en de VOC- en Keyword-spreadsheets. Stand: 9 november 2026. Bedoeld als werkdocument om samen "
  "doelgroepen, hooks en angles uit te werken.</p>")

P("<h2>Samenvatting</h2>")
P("<p><b>Mensen kopen geen koper; ze kopen het vermogen om een dag te staan en te lopen zonder dat hun voeten de rest "
  "van hun leven bepalen.</b> In de 22 Reddit-gesprekken die we diepgaand hebben gecodeerd, komt koper als "
  "werkzaam materiaal niet één keer voor. In een tweede run met 30 extra threads alleen als leerkleur of productnaam. "
  "Koper is daarmee een onderscheidend verhaal over het product, maar geen reden waarom iemand gaat zoeken.</p>")
P("<p>Wat wél steeds terugkomt:</p><ul>"
  "<li>De pijn kost mensen hun werkdag, hun inkomen en gewone dingen als boodschappen doen of de hond uitlaten.</li>"
  "<li>Ze hebben al veel geprobeerd en zijn moe van producten die tegenvallen. Ze wantrouwen verkopers en wondermiddelen.</li>"
  "<li>'Zachter' is niet automatisch beter. Te zachte zolen en schoenen worden vaak als slechter beoordeeld dan stevige.</li>"
  "<li>Een zool moet passen in de schoenen die mensen al hebben. Zolen die de voet hoger in de schoen tillen, geven nieuwe drukpunten.</li>"
  "</ul>")
P("<p><b>Advies voor de positionering (hypothese, te toetsen):</b> begin bij een herkenbare situatie (de lange dienst, de harde "
  "vloer, thuis op tegels), beloof comfort en pasvorm in plaats van genezing, en gebruik koper als materiaalverhaal "
  "(fris, onderscheidend) alleen voor zover het lab-onderbouwd is.</p>")

P("<h2>Bronnen en hoe zwaar ze wegen</h2>")
P(table(["Bron", "Omvang", "Status"], [
    ["Reddit, diepgaand gecodeerd (deze database)", "22 relevante threads, 101 letterlijke citaten, 186 oplossingen met oordeel",
     "Alle citaten automatisch teruggevonden in de brontekst"],
    ["Reddit, routine-run 9 november", "30 threads, waarvan 10 relevant",
     "Labels zijn door een technische fout niet bewaard; alleen de samenvatting is gebruikt"],
    ["Eigen VOC-sheet (03 - Voice of Customer)", "38 Reddit-fragmenten, 8 Amazon-reviewnotities", "Deels nog te hercontroleren (zie kolom Verification)"],
    ["Launch Blueprint v1.2", "Doelgroephypotheses, keyword bank, claimskader", "Werkhypotheses, geen gemeten marktgrootte"],
    ["Verzamelde ruwe data", "2.276 posts uit voet-, beroeps- en situatie-subreddits", "Grotendeels nog niet gecodeerd"],
]))
P("<p>Dit is kwalitatief onderzoek. Aantallen zeggen iets over wat we in de gelezen gesprekken zagen, niet over de markt. "
  "De Reddit-data is vooral Engelstalig en Amerikaans; Nederlandse en Duitse gesprekken zijn schaars.</p>")

P("<h2>Wie heeft het probleem</h2>")
P(table(["Groep", "Wat we zien", "In hun eigen woorden", "Kansrijk voor ons?"], [
    ["Staande beroepen: magazijn, horeca, retail, zorg, onderwijs",
     "Pijn loopt op tijdens de dienst. Diensten worden afgebroken, overuren geschrapt. Veiligheidsschoenen worden als oorzaak genoemd.",
     q("I had to clock out early today because every step on my foot felt so tender.") + "<br>" + q("This has messed up my money, life and relationship."),
     "Hoog. Duidelijk koopmoment, comfortbelofte zonder medische claim is mogelijk."],
    ["Thuis op harde vloeren / huisschoenen",
     "Artsen zeggen 'niet blootsvoets'. Mensen zoeken iets voor thuis; Oofos, Birkenstock, Crocs en Kuru worden genoemd.",
     q("They aren’t squishy at all but the have this arch support  that makes my arch actually feel supported and not feel like it’s collapsing."),
     "Hoog. Sterke aanleiding, ook gezien in de run van 9 november."],
    ["Chronische hielpijn (fasciitis plantaris)",
     "Grootste groep in de data. Jaren pijn, alles geprobeerd, wantrouwen. Zolen worden 'pleister' genoemd maar ook 'a must'.",
     q("I tried everything; every stretch, exercise, and insole on God's green earth."),
     "Middel. Grote vraag, maar hoog claimrisico. Alleen comfortpositionering."],
    ["Voorvoetklachten (Morton-neuroom, bunions)",
     "Gaat om ruimte in de schoen en drukontlasting op één plek. Zachte, verende zolen worden slecht verdragen.",
     q("I can feel the clicking thingy, like I'm stepping on a pebble."),
     "Middel. Interessant voor een dunne voorvoetvariant, niet voor een standaardzool."],
    ["Platvoeten en sporters",
     "Pijn na hardlopen, compensatie in knieën en heupen. Deel van deze groep is tegen zolen ('verzwakt je voeten').",
     q("I’m 43 and walk like a 90 yr old when I get out of bed"),
     "Middel. Let op het barefoot-kamp."],
    ["Wandelaars met brede voeten (Nederland)",
     "Combineren podozolen met breedtematen en zoeken persoonlijk advies in speciaalzaken.",
     q("Ik heb al jaren gedoe met podotherpeutische zolen, blaren, te smalle (wandel)schoenen en pijn in mijn voeten."),
     "Middel. Een van de weinige Nederlandse signalen."],
    ["Neuropathie, diabetes, circulatieklachten",
     "Gevoelloosheid, branden, verkleuring. Medisch traject.",
     q("I fell at the gym last week on the treadmill because I can’t feel my feet."),
     "Niet targeten. Wel opnemen in de FAQ als 'niet geschikt zonder advies'."],
]))

P("<h2>Hoe de pijn het leven raakt</h2>")
P("<p>Dit zijn de emoties waar advertenties op kunnen aansluiten. De sterkste citaten per thema:</p>")
P(table(["Thema", "Citaat", "Betekenis"], [
    ["Werk en inkomen", q("I leave work as if I were wearing two skis."), "Ik verlaat mijn werk alsof ik twee ski's aan heb."],
    ["Werk en inkomen", q("They help but my pain still increases throughout the day and gets unbearable toward the end"),
     "Ze helpen, maar tegen het einde van de dag wordt de pijn ondraaglijk."],
    ["Gewone dingen niet meer kunnen", q("I couldn't even do basic chores like grocery shopping either, it was really bad."),
     "Zelfs boodschappen doen lukte niet meer."],
    ["Gewone dingen niet meer kunnen", q("Now taking the dog out is a pain."), "Nu is zelfs de hond uitlaten een pijn."],
    ["Onvoorspelbaarheid", q("I could never predict on a day-to-day basis whether it would be a good day or a painful day."),
     "Ik wist nooit of het een goede of een pijnlijke dag zou worden."],
    ["Uitzichtloosheid", q("So I think I'm just stuck with painful feet."), "Ik denk dat ik gewoon vastzit aan pijnlijke voeten."],
    ["Buitengesloten", q("I remember feeling left out because it simply hurt too much for me to play."),
     "Ik voelde me buitengesloten omdat meedoen te veel pijn deed."],
    ["Wat ze terug willen", q("I was able to wear my hiking boots last weekend, which I hadn’t been able to wear in 10 years."),
     "Na tien jaar kon ik mijn wandelschoenen weer aan."],
]))

P("<h2>Wat werkt en wat niet</h2>")
P("<p>Elke genoemde oplossing in de 22 threads is gecodeerd met een oordeel. De netto-score loopt van -1,5 (maakt het erger) "
  "tot 1 (werkt). Let op de kleine aantallen.</p>")
P(table(["Categorie", "Vermeldingen", "Werkt", "Deels", "Geen effect", "Erger", "Netto-score"], [
    ["Schoenen (Hoka, Kuru, Birkenstock, Brooks, Oofos...)", "48", "31", "6", "0", "4", "0,58"],
    ["Kant-en-klare inlegzolen", "20", "13", "1", "3", "0", "0,53"],
    ["Operatie", "18", "10", "2", "1", "2", "0,39"],
    ["Medicatie en injecties", "17", "7", "3", "3", "2", "0,15"],
    ["Leefstijl (afvallen, vitamines, ander werk)", "13", "10", "0", "1", "1", "0,58"],
    ["Maatwerkzolen", "10", "5", "1", "1", "1", "0,30"],
    ["Rekken en oefeningen", "10", "5", "1", "0", "2", "0,25"],
    ["Nachtspalk of laars", "10", "5", "1", "1", "2", "0,15"],
    ["Metatarsaalpads", "6", "3", "0", "2", "0", "0,17"],
    ["Barefoot / minimalistisch", "5", "4", "1", "0", "0", "0,90"],
    ["Tapen", "5", "3", "1", "0", "0", "0,70"],
]))
P("<p>Wat dit voor ons betekent:</p><ul>"
  "<li>Schoenen en kant-en-klare zolen scoren hoger dan maatwerkzolen. Duur en 'op maat' is voor deze mensen geen garantie.</li>"
  "<li>Niemand noemt één oplossing die alles oplost. Wie herstelt, combineert meestal schoenen, zolen, rekken en rust.</li>"
  "<li>Het barefoot-kamp is klein maar uitgesproken positief over zichzelf. Zij zijn eerder een bron van bezwaren dan klanten.</li>"
  "</ul>")

P("<h2>Klachten over bestaande zolen en schoenen</h2>")
P("<p>Deze klachten zijn direct te vertalen naar productvereisten en advertentieclaims, als het product ze echt oplost.</p>")
P(table(["Klacht", "Citaat", "Eis voor ons product"], [
    ["Te zacht", q("Too soft is a real thing. I needed a firmer supportive sole"), "Stevige basis met gerichte demping in hiel en voorvoet"],
    ["Te dik, voet komt hoger in de schoen",
     q("The orthotics elevated my foot in the shoe and changed my foot mechanics when running causing excess pressure on top"),
     "Dun profiel, past in bestaande schoenen; dikte per zone vermelden"],
    ["Past niet meer in favoriete schoenen",
     q("I thought Kurus were my brand but once I put in the orthotic insoles, they didn't fit right anymore."), "Uitneembaar en op maat te knippen"],
    ["Te veel of te harde boogsteun", q("the correction was too intense and was causing me pain in the arch"), "Gematigde boog, of varianten per voettype"],
    ["Effect verdwijnt", q("I tried the Oofos slides and they feel good for a moment, then not so good."),
     "Comfort testen na een volle dienst, niet na vijf minuten; slijtvast materiaal"],
    ["Glad of instabiel", q("They are amazing sandal but a death trap when wet."), "Grip aan de bovenkant, voet mag niet schuiven"],
    ["Prijs", q("Expensive as hell but 2 weeks after wearing them, I woke up with zero pain when stepping on the floor."),
     "Duidelijk alternatief voor maatwerk van honderden euro's (zonder medische belofte)"],
]))
P("<p>Uit de eerdere VOC-sheet komen daar nog bij: zolen die na een paar maanden plat worden, een voorvoetkussen op de "
  "verkeerde plek, te weinig demping op beton en piepende zolen.</p>")

P("<h2>Bezwaren en wantrouwen</h2>")
P(table(["Bezwaar", "Citaat", "Hoe we het kunnen opvangen"], [
    ["Zolen zijn alleen een pleister", q("The insoles are just a bandaid and don’t address the issue."),
     "Niet doen alsof de zool de oorzaak oplost. Positioneren als dagelijks comfort naast rekken, kracht en rust."],
    ["Zolen verzwakken je voeten",
     q("orthotics  which though can alleviate for the short term - can unfortunately weaken further in the long term."),
     "FAQ: gematigde steun in plaats van een mal; laat de voet zelf werken."],
    ["Verkopers en influencers verkopen rommel",
     q("There’s people selling you crap, there’s influencers spouting crap about doing this and that"),
     "Eerlijke claims, echte specificaties, ruime retour. Geen 'wondermiddel'-toon."],
    ["Wellness is onzin", q("I was even getting ready to try that essential oil BS."),
     "Koper niet als genezend materiaal brengen; anders belandt het merk in dezelfde hoek."],
    ["Goedkope zolen zijn slecht", q("I recommend forking out for slightly better than Dr. Scholl's"),
     "Kwaliteit en materiaal laten zien; niet concurreren op de laagste prijs."],
]))
P("<p>In de run van 9 november kwamen daar nog bij: orthesen van chiropractors en schoenverkopers worden als oplichterij "
  "gezien, en ondersteunende zolen worden vaak 'oversold' genoemd.</p>")

P("<h2>Koper: wat we weten</h2>")
P("<ul>"
  "<li>Op Reddit praat bijna niemand over koper als werkzaam materiaal voor voeten. Er is dus geen groep die erom vraagt, maar ook geen groep die het afbrandt.</li>"
  "<li>Het blueprint noemt een gerandomiseerde studie uit 2013 waarin koperen armbanden bij reuma niet beter werkten dan placebo, "
  "en de FTC-zaak tegen Tommie Copper (2015) over onbewezen pijnclaims.</li>"
  "<li>Wat mogelijk wel kan, na lab-onderbouwing: koper als onderdeel van een frisse, geurremmende bovenlaag.</li>"
  "<li>Nog niet onderzocht: de koper- en wellnessgroepen (r/skeptic, r/ChronicPain, r/Arthritis en koperen sokken en armbanden). "
  "Die staan in de scraper klaar en zijn de logische volgende stap.</li>"
  "</ul>")

P("<h2>Merken in de gesprekken</h2>")
P(table(["Merk", "Threads", "Wat mensen zeggen"], [
    ["Oofos", "8", "Voelt direct heerlijk ('walking on clouds'), maar effect kort, glad als het nat is, en sommigen haken af."],
    ["Hoka", "6", "Vaak aangeraden, maar wisselend: binnen goed, buiten soms meteen pijn."],
    ["Birkenstock", "5", "Gewaardeerd om stevige boogsteun; 'niet zacht, wel gesteund'. Namaak zou die steun missen."],
    ["Crocs", "4", "Veilig alternatief voor thuis, ingebouwde boog."],
    ["Brooks", "4", "Ghost Max en Adrenaline genoemd als comfortabel, vaak met zolen erin."],
    ["Superfeet", "3", "Wisselend: werkt voor sommigen, in gewone schoenen weinig verschil."],
    ["Kuru", "3", "Sterke verhalen (6 uur pretpark), maar pijn kan alsnog oplopen over de dag."],
    ["FP Insoles", "2", "Reacties lijken verkapte reclame met claims als '90% schokabsorptie'. Concurrent om te volgen."],
    ["Good Feet Store", "1", "Bekend van tv-reclames, door anderen gewantrouwd."],
]))

P("<h2>Angles en hooks</h2>")
P("<p>Hypotheses om te testen. Alle hooks beloven comfort en pasvorm, geen pijnverlichting of genezing. "
  "Een hook gebruiken we alleen als het product de belofte aantoonbaar waarmaakt.</p>")
angles = [
    ("Het einde van je dienst", "Staande beroepen",
     "De pijn loopt op tijdens de dag; mensen breken diensten af.",
     ["Je dienst is lang genoeg. Je voeten hoeven niet mee te tellen.",
      "Ook om vijf uur nog prettig op je benen.",
      "Gemaakt voor de laatste uren van je dienst, niet voor de eerste vijf minuten."],
     "Draagtest over een volle dienst; slijtvastheid."),
    ("Harde vloeren, ook thuis", "Thuis op tegels en laminaat; magazijn en winkel op beton",
     "Artsen raden af om blootsvoets te lopen; mensen zoeken iets voor thuis.",
     ["Je vloer is hard. Je zool hoeft dat niet te zijn.", "Voor thuis, op tegels, de hele dag."],
     "Variant voor huisschoenen of slippers?"),
    ("Past in je eigen schoenen", "Iedereen die al zolen heeft geprobeerd",
     "Zolen maken schoenen te krap of tillen de voet op.",
     ["Comfort zonder dat je schoenen ineens knellen.", "Dun waar het moet, stevig waar het telt."],
     "Dikte per zone en pasvorm in sneakers en werkschoenen."),
    ("Stevig is niet hetzelfde als hard", "Mensen die zachte zolen en schoenen al opgaven",
     "'Too soft is a real thing'; zachte zolen voelen kort goed.",
     ["Zacht voelt fijn voor vijf minuten. Stevig blijft fijn.", "Gerichte demping, geen pudding onder je voet."],
     "Vergelijkingstest met een zachte gelzool."),
    ("Eerlijk, zonder wondermiddel", "De wantrouwige koper die 'alles al geprobeerd' heeft",
     "Groot wantrouwen tegen verkopers en wellness-claims.",
     ["Geen wondermiddel. Wel een betere basis in je schoen.", "We beloven geen genezing. Wel comfort, en je geld terug als het niet past."],
     "Retourbeleid en echte specificaties op de pagina."),
    ("Koper als materiaal", "Wellness-geïnteresseerden; mensen met zweet- en geurklachten",
     "Koper is onderscheidend, maar niemand zoekt erop.",
     ["Een frisse bovenlaag met koper.", "Het koper zie je, het comfort voel je."],
     "Labtests op geur en materiaal van het eindproduct. Zonder die tests deze angle niet gebruiken."),
    ("Wandelen met brede voeten", "Nederlandse wandelaars, vaak al met podozolen",
     "Blaren en te smalle schoenen; persoonlijk advies wordt gewaardeerd.",
     ["Brede voeten, lange wandeling, geen blaren.", "Een zool die ook in je wandelschoen met breedtemaat past."],
     "Mogelijke samenwerking met wandelspeciaalzaken."),
]
for name, who, insight, hooks, proof in angles:
    P(f"<h3>{e(name)}</h3>")
    P(f"<p><b>Voor wie:</b> {e(who)}<br><b>Inzicht:</b> {e(insight)}<br><b>Te valideren:</b> {e(proof)}</p>")
    P("<ul>" + "".join(f"<li>{e(h)}</li>" for h in hooks) + "</ul>")

P("<h2>Wat we wel en niet mogen claimen</h2>")
P(table(["Kan, na verificatie van het product", "Niet zonder specifiek bewijs en juridische toets"], [
    ["Met koper verrijkte bovenlaag (als de samenstelling klopt)", "Geneest fasciitis of hielspoor"],
    ["Demping voor dagelijks gebruik", "Vermindert ontsteking of pijn"],
    ["Op maat te knippen, dun profiel (als zo ontworpen)", "Verbetert de doorbloeding door koper"],
    ["Geurremmend (alleen met onafhankelijke test)", "Beschermt tegen bacteriën, schimmel of virussen"],
    ["Specificaties zoals boogprofiel en dikte", "Medische pijnverlichting, helpt bij neuropathie of artrose"],
]))
P("<p>Citaten van Reddit gebruiken we als inspiratie voor taal, nooit als testimonial voor ons product.</p>")

P("<h2>Open vragen en volgende stappen</h2>")
P("<ul>"
  "<li><b>Koper-onderzoek:</b> de koper- en skeptici-subreddits gericht coderen. Dat is de belangrijkste ontbrekende vraag.</li>"
  "<li><b>Staande beroepen:</b> zorg, magazijn, horeca en onderwijs verder coderen; dit lijkt de sterkste doelgroep.</li>"
  "<li><b>Nederlands en Duits:</b> Reddit levert weinig. Viva, Fok! en gutefrage.net toevoegen als bron.</li>"
  "<li><b>Amazon en YouTube:</b> reviews van zolen met en zonder koper, zoals gepland in het blueprint.</li>"
  "<li><b>Product:</b> welke dikte, boog en koperlaag hebben de samples, en welke tests liggen er?</li>"
  "<li><b>Keuze:</b> welke twee of drie angles testen we als eerste?</li>"
  "</ul>")
P("<p>De dagelijkse onderzoeksroutine draait vanaf 10 november weer en vult de database elke ochtend aan met 30 "
  "gecodeerde threads. Dit document kan dan periodiek worden bijgewerkt.</p>")

P("<h2>Bijlage: citatenbank</h2>")
P(f"<p>Alle {len(quotes)} letterlijke citaten uit de gecodeerde threads, gesorteerd op soort. Elk citaat is automatisch "
  "teruggevonden in de originele tekst. De link opent de post of de reactie.</p>")
P(table(["Soort", "Citaat (letterlijk)", "Betekenis", "Bron"], [
    [e(KIND_NL.get(k, k)), q(t), e(nl), f"<a href='{link}'>r/{e(sub)}</a>"] for k, t, nl, sub, link in quotes
]))

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("<html><head><meta charset='utf-8'></head><body>" + "\n".join(parts) + "</body></html>")
print(len(quotes), "citaten;", sum(len(p) for p in parts), "tekens")
