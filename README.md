# Reddit Voice-of-Customer scraper: koperen inlegzolen

Verzamelt Reddit-discussies (EN, NL, DE) over voetpijn, schoenen en inlegzolen: de vragen,
de antwoorden, wat wél en níet werkt. Claude labelt elke thread volgens het codeboek uit
*03 - Voice of Customer.xlsx*. Het resultaat is een Excel-rapport.

```
config/subreddits.yaml   welke subreddits, per groep (voet, beroepen, situaties, koper/skeptici, NL, DE)
config/keywords.csv      zoekwoorden (EN uit de Keyword Bank, NL/DE concept)
        │
        ▼
collect  ── Arctic Shift (gratis archief, volledige historie)
         └─ Reddit API   (nieuwe posts + sitewide zoeken op alle zoekwoorden)
        │
        ▼
data/reddit.db (SQLite: posts, reacties, labels; gebruikersnamen alleen gehasht)
        │
        ▼
label    ── Claude (in een Claude Code-sessie, zie LABELING.md) zet elke thread om naar
            het ThreadLabel-schema (vocscraper/schema.py)
        │
        ▼
export   ── exports/reddit_voc.xlsx
```

## Het rapport

| Tabblad | Inhoud |
|---|---|
| Threads | één rij per thread: probleem (NL), regio, aandoening, beroep, situatie, eerder geprobeerd, klachten, gewenste uitkomst, merken, koper-sentiment, red flags, claimrisico |
| VOC Quotes | letterlijke citaten (Q) + NL-betekenis (T), zelfde kolommen als *Reddit VOC*; elk citaat wordt automatisch teruggezocht in de brontekst |
| Oplossingen | elke genoemde oplossing met oordeel (werkt / deels / geen effect / erger), eigen ervaring ja/nee, upvotes, link naar de reactie |
| Wat werkt (ranking) | per oplossingscategorie: aantal vermeldingen, verdeling van oordelen, netto-score, top merken |
| Problemen (telling) | hoe vaak elke regio, aandoening, situatie, productklacht en gewenste uitkomst voorkomt |
| Koper & wellness | alles wat over koper, magneten en acupressuur gezegd wordt |
| Dekking | posts per subreddit, hoeveel gelabeld en relevant |

Reddit is kwalitatieve input, geen representatieve steekproef. Een citaat is geen testimonial
voor ons product, en een reactie is geen bewijs dat iets werkt (zie hoofdstuk 7 van het blueprint).

## Gebruik

```bash
pip install -r requirements.txt

# zoekwoorden bijwerken vanuit een keyword-bank (kolom met 'SEARCH TERM' in de header)
python -m vocscraper import-keywords "01 - Copper Insoles - EN Keyword Bank.xlsx" --language en --sheet "EN Keywords"

# proefrun: een paar subreddits, max 50 posts per zoekopdracht
python -m vocscraper collect --source arctic --groups foot_core dutch --max-posts 50
python -m vocscraper prepare-labels --limit 25   # daarna labelen in Claude Code, zie LABELING.md
python -m vocscraper import-labels
python -m vocscraper export
python -m vocscraper stats

# volledige historie sinds 2015 (duurt uren; Arctic Shift wordt rustig benaderd)
python -m vocscraper collect --source arctic

# nieuwe posts + sitewide zoeken op alle zoekwoorden (Reddit API)
python -m vocscraper collect --source reddit --sitewide
```

Alles is incrementeel: elke zoekopdracht onthoudt de nieuwste post die hij zag, en dubbele
posts worden samengevoegd. Een tweede run haalt dus alleen nieuwe posts op.

### Labelen

Standaard labelt de Claude Code-sessie zelf (`prepare-labels` → labelen → `import-labels`), zonder
API-sleutel en zonder extra kosten. Wie later toch via de API wil labelen (sneller, parallel):
zet `ANTHROPIC_API_KEY` en gebruik `python -m vocscraper label`; het model kies je met `VOC_MODEL`.

### Omgevingsvariabelen (optioneel)

| Variabele | Waarvoor |
|---|---|
| `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET` | officiële Reddit API voor de nieuwste posts. Zonder deze twee wordt de publieke `.json` geprobeerd; die blokkeert Reddit vanaf cloudservers |
| `AUTHOR_HASH_SALT` | geheime salt voor het pseudonimiseren van gebruikersnamen |
| `ANTHROPIC_API_KEY`, `VOC_MODEL` | alleen voor labelen via de API |

## Tests

```bash
python -m pytest -q    # offline, geen netwerk of API-sleutel nodig
```
