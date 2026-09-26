# Website + Headless-CMS — Handgemachte Schweizer Souvenirs

Statischer Mehrseiten-Website nach dem technischen Briefing, **jetzt mit Admin-Oberfläche**
(Decap CMS) unter `/admin/` — Produkte, Blogartikel, Markttermine und Firmenangaben lassen
sich dort ohne Code bearbeiten, nach dem Speichern baut sich der Live-Auftritt automatisch neu.

## Wie die Teile zusammenspielen

```
content/            ← Die eigentlichen Inhalte (von Decap CMS bearbeitet)
  settings.yaml        Markenname, Adresse, Telefon, Domain
  produkte/gipsfiguren/*.yaml   Ein File pro Gipsfigur
  produkte/kerzen/*.yaml        Ein File pro Kerze
  magnete.yaml          Magnet-Galerie (Liste) + Platzhalter-Motive
  maerkte.yaml           Marktkalender (Startseite + /kontakt/)
  blog/*.md               Ein Markdown-File pro Blogartikel (Titel, Datum, Text)

gen/                 ← Python-Generator: liest content/ + baut daraus die HTML-Seiten
                        (Header/Footer/Schema.org/Breadcrumbs kommen aus gemeinsamen Bausteinen)

admin/               ← Decap-CMS-Oberfläche (config.yml definiert die Formulare oben)

index.html, gipsfiguren/, kerzen/, magnete/, grosshandel/,
ueber-uns/, kontakt/, blog/, impressum/, datenschutz/, sitemap.xml, robots.txt
                     ← Fertig gebaute, statische Website (Ergebnis von `python3 gen/runner.py`)
```

**Wichtig:** Produkttexte/-preise nie direkt in den HTML-Dateien ändern — die werden bei
jedem Build überschrieben. Änderungen gehören in `content/` (per CMS oder von Hand).

## Deployment mit Admin-Oberfläche (empfohlen: Netlify + GitHub)

Die CMS-Oberfläche unter `/admin/` braucht einen Login (Netlify Identity) und einen Ort, der
bei jedem Speichern automatisch neu baut — beides übernimmt Netlify kostenlos, wenn der Ordner
über ein **GitHub-Repository** eingebunden wird (nicht per Drag-and-drop-Upload).

1. **GitHub-Repository erstellen** und den kompletten Inhalt dieses Ordners hochladen
   (inkl. `content/`, `admin/`, `gen/`, `netlify.toml`, `requirements.txt`).
2. Auf **app.netlify.com** → *Add new site → Import an existing project* → das Repository
   auswählen. Netlify erkennt `netlify.toml` automatisch (Build-Befehl + Zielordner sind
   bereits konfiguriert).
3. **Site settings → Identity → Enable Identity.** Unter *Registration preferences*
   „Invite only" wählen (damit sich nicht x-beliebige Personen anmelden können).
4. **Identity → Services → Git Gateway → Enable Git Gateway.** Das verbindet die CMS-Logins
   mit Schreibrechten auf das Repository.
5. **Identity → Invite users** — eigene E-Mail-Adresse einladen, Einladung annehmen,
   Passwort setzen.
6. Danach: `https://ihre-seite.netlify.app/admin/` öffnen, einloggen — die Admin-Oberfläche
   mit allen Formularen (Gipsfiguren, Kerzen, Magnete, Blog, Markttermine, Einstellungen)
   ist da.

Jede Änderung im CMS wird als Commit ins GitHub-Repository geschrieben, Netlify baut daraufhin
automatisch neu (`pip3 install -r requirements.txt && python3 gen/runner.py`) und veröffentlicht
die aktualisierte Seite — meist innerhalb 1–2 Minuten.

### Domain

Unter *Site settings → Domain management* die `.ch`-Domain als Custom Domain hinterlegen und
beim Domain-Registrar die von Netlify angezeigten DNS-Einträge setzen. Danach in
`content/settings.yaml` (per CMS unter „Einstellungen") die `base_url` auf die echte Domain
anpassen — das aktualisiert automatisch `sitemap.xml`, `robots.txt` und alle Schema.org-Angaben.

## Bezahlung mit Stripe

Für jedes Produkt (Gipsfiguren, Kerzen) gibt es im CMS ein Feld **„Stripe-Zahlungslink"**:

1. Im Stripe-Dashboard einen **Payment Link** für das Produkt erstellen (unterstützt TWINT,
   Karten, CHF).
2. Den Link in das Feld einfügen und speichern.
3. Auf der Produktseite erscheint automatisch ein Button „Jetzt bezahlen (Stripe)" anstelle
   von „Auf Anfrage bestellen".

Für Magnete (Galerie ohne Einzelseiten) und Grosshandel ist aktuell kein Direktkauf vorgesehen —
passend zum Briefing, das dort auf Anfrage/Formular statt Checkout setzt.

## Lokal ansehen (ohne Netlify, nur zum Testen)

```bash
cd gen
python3 runner.py     # baut alle Seiten aus content/ neu
cd ..
python3 -m http.server 8000
# dann im Browser: http://localhost:8000/
```

`/admin/` funktioniert lokal nicht (braucht Netlify Identity + Git Gateway) — dafür immer über
die Netlify-URL gehen.

## Vor dem Live-Schalten noch zu erledigen

- `content/settings.yaml` (per CMS): echten Markennamen, Adresse, Telefon, E-Mail, Domain eintragen
- Fehlende Produktfotos ergänzen (Magnete: Zürich, Interlaken, Genf, Thun sind als
  „Foto folgt"-Platzhalter angelegt)
- Blog-Artikeltexte schreiben (Struktur & SEO-Titel stehen bereits)
- Grosshandel-Konditionen, Über-uns-Texte, Impressum/Datenschutz-Platzhalter ausfüllen
  (Rechtstexte von einer Fachperson prüfen lassen)
- Stripe-Zahlungslinks hinterlegen, sobald das Stripe-Konto eingerichtet ist
