# Labelen in een Claude Code-sessie

We labelen zonder API-sleutel: de Claude Code-sessie zelf leest de threads en vult het
`ThreadLabel`-schema in (`vocscraper/schema.py`). De kosten vallen binnen het Claude-abonnement.

## Werkwijze

1. Klaarzetten:
   ```bash
   python -m vocscraper prepare-labels --limit 40
   ```
   Dit schrijft `data/labeling/batch_NNNN.md`. Elk bestand bevat de instructies plus een paar
   threads, gescheiden door `=== THREAD <post_id> ===`.
2. Per batch: lees het bestand en schrijf `data/labeling/batch_NNNN.labels.json`:
   ```json
   [{"post_id": "abc123", "label": { ...alle velden van ThreadLabel... }}]
   ```
3. Importeren (valideert elk label tegen het schema; goedgekeurde batches gaan naar `imported/`):
   ```bash
   python -m vocscraper import-labels
   ```
   Lost fouten op en importeer opnieuw tot er geen FOUT-regels meer zijn.
4. Rapport: `python -m vocscraper export`

## Kwaliteitsregels (samengevat; de volledige tekst staat bovenaan elke batch)

- `quotes.text` is letterlijk uit de bron gekopieerd. Het rapport controleert dit automatisch.
- `source_id` is `post` of de comment-id tussen `[...]`.
- Alleen coderen wat er staat; onbekend wordt `null` of een lege lijst.
- Ook negatieve ervaringen en tegengeluiden coderen.
- Niet-relevante threads: `relevant: false`, de overige velden minimaal (lege lijsten, korte teksten).
