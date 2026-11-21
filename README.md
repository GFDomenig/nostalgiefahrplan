# Nostalgiefahrplan Schweiz

Öffentliche Fahrten historischer Eisenbahnen in der Schweiz, mit Direktlinks zur Buchung beim Veranstalter.

Pilotbetrieb unter https://fahrplan.belimmo.ch (für Suchmaschinen gesperrt). Geplanter definitiver Betrieb unter www.bahnkultur-rhb.ch.

## Aufbau

- `index.html`: die Webseite (Liste, Kalender, Veranstalter-Verzeichnis)
- `data/fahrten.json`: alle Daten. Nur diese Datei wird bei Aktualisierungen geändert.
- `impressum.html`: Impressum und Datenschutz
- `robots.txt`: sperrt die Pilotseite für Suchmaschinen
- `CNAME`: Domain für GitHub Pages

## Datenformat `data/fahrten.json`

- `stand`: Datum der letzten Prüfung (JJJJ-MM-TT)
- `veranstalter`: Kürzel → `n` Name, `k` Kanton(e), `w` Website, `p` übliches Angebot
- `fahrten`: Liste von Fahrten
  - `o` Kürzel des Veranstalters, `t` Titel, `r` Strecke
  - `d` Liste von Daten oder `rg` [von, bis] mit `wd` (Wochentage) für Saisonbetrieb
  - `h` Abfahrtszeit, `tr` Dampf / Elektro / Diesel, `th` Themen (Advent, Kulinarik, Familie, Zahnrad, Bergstrecke)
  - `x` Beschreibung (eigene Worte, keine kopierten Texte), `pr` Preis
  - `b` Link zur Buchung oder Info
  - `s` Quelle: `v` Veranstalter, `d` Drittquelle (Tourismusportal)
  - `st` Status: `voll` ausgebucht, `zug` Billette im Zug, `anm` Anmeldung nötig

## Aktualisierung

Wöchentlich prüft eine geplante Aufgabe die Websites der Veranstalter, passt `data/fahrten.json` an und eröffnet einen Pull Request. Nach Durchsicht und Merge ist die Änderung innert Minuten online.

Regeln für Aktualisierungen:
1. Nur Fahrten aufnehmen, deren Datum aus einer Quelle stammt; nichts aus Regelmässigkeiten hochrechnen.
2. Angaben der Veranstalter-Website gehen vor Tourismusportalen. Widersprüche im Pull Request nennen.
3. Beschreibungen in eigenen Worten, höchstens zwei Sätze.
4. Vergangene Fahrten bleiben bis Ende des folgenden Jahres in der Datei (Rückblick).
5. `stand` auf das Prüfdatum setzen.

## Umzug auf bahnkultur-rhb.ch

1. `CNAME` auf `www.bahnkultur-rhb.ch` ändern und DNS beim Registrar setzen.
2. `robots.txt` und die `noindex`-Zeilen entfernen.
3. Impressum auf die Stiftung umstellen.
4. Auf belimmo.ch eine dauerhafte Weiterleitung (301) einrichten.
