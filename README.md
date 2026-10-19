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
label    ── Claude zet elke thread om naar het ThreadLabel-schema (vocscraper/schema.py)
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
python -m vocscraper label --limit 25
python -m vocscraper export
python -m vocscraper stats

# volledige historie sinds 2015 (duurt uren; Arctic Shift wordt rustig benaderd)
python -m vocscraper collect --source arctic

# nieuwe posts + sitewide zoeken op alle zoekwoorden (Reddit API)
python -m vocscraper collect --source reddit --sitewide
```

Alles is incrementeel: elke zoekopdracht onthoudt de nieuwste post die hij zag, en dubbele
posts worden samengevoegd. Een tweede run haalt dus alleen nieuwe posts op.

### Omgevingsvariabelen

| Variabele | Waarvoor |
|---|---|
| `ANTHROPIC_API_KEY` | labelen met Claude |
| `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET` | officiële Reddit API. Zonder deze twee wordt de trage publieke `.json` gebruikt |
| `VOC_MODEL` | Claude-model voor het labelen (standaard `claude-opus-5-5`) |
| `AUTHOR_HASH_SALT` | geheime salt voor het pseudonimiseren van gebruikersnamen |

## Automatisch draaien

`.github/workflows/scrape.yml` draait op maandag en donderdag: nieuwe posts ophalen, max. 500
threads labelen en het Excel-rapport als download bij de run zetten (Actions → run → Artifacts).
Zet onder *Settings → Secrets and variables → Actions* de secrets `ANTHROPIC_API_KEY`,
`REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET` en `AUTHOR_HASH_SALT`. Start de eerste keer handmatig
met *source = arctic* voor de volledige historie.

## Tests

```bash
python -m pytest -q    # offline, geen netwerk of API-sleutel nodig
```
