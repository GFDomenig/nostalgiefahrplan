# Bahnkultur Historic RhB

Portal zur historischen Bahnkultur: öffentliche Fahrten historischer Eisenbahnen in Graubünden und der ganzen Schweiz mit Direktlinks zur Buchung, News der Stiftung Bahnkultur RhB und der Mitglieder von Historic RhB, Karte der Strecken. (Repository-Name: nostalgiefahrplan)

Pilotbetrieb unter https://fahrplan.belimmo.ch (für Suchmaschinen gesperrt). Geplanter definitiver Betrieb unter www.bahnkultur-rhb.ch.

## Aufbau

- `index.html`: die Webseite (Liste, Kalender, Veranstalter-Verzeichnis)
- `data/fahrten.json`: alle Daten. Nur diese Datei wird bei Aktualisierungen geändert.
- `impressum.html`: Impressum und Datenschutz
- `robots.txt`: sperrt die Pilotseite für Suchmaschinen
- `CNAME`: Domain für GitHub Pages
- `vendor/leaflet`: Kartenbibliothek Leaflet 1.9.4 (BSD-Lizenz), lokal eingebunden
- Karte: swisstopo Landeskarte grau, Ersatz OpenStreetMap

## Datenformat `data/fahrten.json`

- `stand`: Datum der letzten Prüfung (JJJJ-MM-TT)
- `veranstalter`: Kürzel → `n` Name, `k` Kanton(e), `w` Website, `p` übliches Angebot, `hr` true = gehört zu Historic RhB (rot hervorgehoben), `geo` Liste von [Breite, Länge] der wichtigsten Stationen für die schematische Karte
- `fahrten`: Liste von Fahrten
  - `id` feste Kennung für die Detailseite (#fahrt-id); einmal vergeben nie ändern, da Links geteilt werden
  - `o` Kürzel des Veranstalters, `t` Titel, `r` Strecke
  - `d` Liste von Daten oder `rg` [von, bis] mit `wd` (Wochentage) für Saisonbetrieb
  - `h` Abfahrtszeit, `tr` Dampf / Elektro / Diesel, `th` Themen (Advent, Kulinarik, Familie, Zahnrad, Bergstrecke)
  - `x` Beschreibung (eigene Worte, keine kopierten Texte), `pr` Preis
  - `b` Link zur Buchung oder Info
  - `s` Quelle: `v` Veranstalter, `d` Drittquelle (Tourismusportal)
  - `st` Status: `voll` ausgebucht, `zug` Billette im Zug, `anm` Anmeldung nötig

## Datenformat `data/news.json`

- `stand`: Datum der letzten Prüfung
- `quellen`: Kürzel → `n` Name, `w` Website bzw. News-Seite. `stiftung` = Stiftung Bahnkultur RhB (wird hervorgehoben)
- `news`: Liste von Meldungen
  - `q` Liste der Absender-Kürzel, `t` Titel, `x` Zusammenfassung in eigenen Worten (höchstens zwei Sätze), `u` Link zur Meldung
  - `d` Datum (JJJJ-MM-TT, optional), `dl` abweichende Datumsanzeige (optional)
  - `s` Quelle: `v` Absender selbst, `d` Drittquelle

Eigene News der Stiftung: Eintrag mit `"q":["stiftung"]` ergänzen; er erscheint hervorgehoben im News-Bereich und auf der Startseite.

## Aktualisierung

Wöchentlich prüft eine geplante Aufgabe die Websites der Veranstalter, passt `data/fahrten.json` an und eröffnet einen Pull Request. Nach Durchsicht und Merge ist die Änderung innert Minuten online.

Regeln für Aktualisierungen (Fahrten und News):
1. Nur Fahrten aufnehmen, deren Datum aus einer Quelle stammt; nichts aus Regelmässigkeiten hochrechnen.
2. Angaben der Veranstalter-Website gehen vor Tourismusportalen. Widersprüche im Pull Request nennen.
3. Beschreibungen in eigenen Worten, höchstens zwei Sätze.
4. Vergangene Fahrten bleiben bis Ende des folgenden Jahres in der Datei (Rückblick).
5. `stand` auf das Prüfdatum setzen.
6. News: keine Texte oder Bilder übernehmen, nur eigene Zusammenfassung mit Link. Meldungen älter als 12 Monate entfernen. Bei Meldungen ohne Datum kein Datum erfinden.
7. News der Stiftung (`stiftung`) nie automatisch erfassen oder ändern; sie kommen nur vom Stiftungsrat.

## Umzug auf bahnkultur-rhb.ch

1. `CNAME` auf `www.bahnkultur-rhb.ch` ändern und DNS beim Registrar setzen.
2. `robots.txt` und die `noindex`-Zeilen entfernen.
3. Impressum auf die Stiftung umstellen.
4. Auf belimmo.ch eine dauerhafte Weiterleitung (301) einrichten.
