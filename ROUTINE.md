# Dagelijkse routine (geplande Claude Code-sessie)

Elke ochtend start er een nieuwe sessie die deze stappen volgt. Werkbranch:
`claude/clever-ptolemy-6w79vf`. De database staat op de branch `voc-data` (zie `scripts/data.sh`).

1. **Code en data ophalen**
   ```bash
   git fetch origin claude/clever-ptolemy-6w79vf
   git checkout claude/clever-ptolemy-6w79vf && git pull origin claude/clever-ptolemy-6w79vf
   pip install -q -r requirements.txt
   scripts/data.sh restore
   ```
2. **Nieuwe posts en reacties ophalen** (maximaal 45 minuten; draai op de achtergrond en wacht
   tot het klaar is). Zoekopdrachten die het langst geleden draaiden gaan eerst, dus elke dag
   schuift het verder op.
   ```bash
   python -m vocscraper collect --source arctic --max-posts 300 --time-budget 45 > data/collect.log 2>&1
   ```
3. **30 threads klaarzetten** (koper/wellness gaat voor, dan de threads met de meeste reacties)
   ```bash
   python -m vocscraper prepare-labels --limit 30
   ```
4. **Labelen** volgens `LABELING.md`: lees elke `data/labeling/batch_NNNN.md` en schrijf
   `batch_NNNN.labels.json`. Citaten letterlijk overnemen.
5. **Importeren** tot er geen FOUT-regels meer zijn:
   ```bash
   python -m vocscraper import-labels
   ```
6. **Rapport en dagverslag**
   ```bash
   python -m vocscraper export --out exports/reddit_voc.xlsx
   python -m vocscraper stats
   ```
   Schrijf `reports/JJJJ-MM-DD.md` (Nederlands, kort):
   - de stats-telling en hoeveel posts er vandaag bij kwamen,
   - de 3-5 opvallendste nieuwe inzichten uit de gelabelde threads van vandaag (pijnpunten,
     wat werkt / niet werkt, alles over koper), met letterlijke citaten en links,
   - problemen (mislukte zoekopdrachten, time-outs).
7. **Opslaan**
   ```bash
   scripts/data.sh save
   git add data/labeling exports reports
   git commit -m "Dagelijkse VOC-run JJJJ-MM-DD"
   git push -u origin claude/clever-ptolemy-6w79vf
   ```

Gaat er iets mis (archief onbereikbaar, geen nieuwe threads), sla het betreffende stap over, zet
het in het dagverslag en sla de rest gewoon op.
