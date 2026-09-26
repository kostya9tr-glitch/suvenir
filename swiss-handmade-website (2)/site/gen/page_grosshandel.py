# -*- coding: utf-8 -*-
from common import page, breadcrumbs, BRAND

TITLE = f"Für Wiederverkäufer — Grosshandel handgemachte Geschenkartikel Schweiz | {BRAND}"
DESC = "Grosshandel für handgemachte Gipsfiguren, Magnete und Kerzen: Konditionen für Geschenkläden, Hotels und Floristen in der Schweiz. Jetzt anfragen."


def build():
    crumbs_html, crumbs_ld = breadcrumbs([("Startseite", "/"), ("Grosshandel", None)])
    body = f"""
    {crumbs_html}
    <header class="page-hero container">
      <p class="kicker">Für den Handel</p>
      <h1>Grosshandel — handgemachte Geschenkartikel aus der Schweiz</h1>
      <p class="lead">Wir beliefern Geschenkläden, Hotels, Floristen und weitere Wiederverkäufer mit handgefertigten Gipsfiguren, Magneten und Kerzen. Jedes Stück wird in unserer Werkstatt im Kanton Bern gegossen und bemalt — keine importierte Massenware.</p>
    </header>

    <section class="section">
      <div class="container">
        <div class="cat-grid" style="grid-template-columns:repeat(3,1fr);">
          <div class="cat-card" style="padding:24px;">
            <div class="cat-body" style="padding:0;">
              <h3>Mindestbestellung</h3>
              <p>[Mindestbestellwert / Mindeststückzahl — wird ergänzt]</p>
            </div>
          </div>
          <div class="cat-card" style="padding:24px;">
            <div class="cat-body" style="padding:0;">
              <h3>Konditionen</h3>
              <p>[Grosshandelsrabatt, Zahlungsziel — wird ergänzt]</p>
            </div>
          </div>
          <div class="cat-card" style="padding:24px;">
            <div class="cat-body" style="padding:0;">
              <h3>Lieferung</h3>
              <p>[Lieferzeit, Versandkosten — wird ergänzt]</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head"><div><p class="kicker">So funktioniert's</p><h2>Zusammenarbeit in drei Schritten</h2></div></div>
        <div class="cat-grid" style="grid-template-columns:repeat(3,1fr);">
          <div><h3>1. Anfrage</h3><p>Sie senden uns das Formular unten — mit Angaben zu Geschäft und Wunschsortiment.</p></div>
          <div><h3>2. Angebot</h3><p>Wir melden uns mit Sortiment, Preisen und Mindestmengen für Wiederverkäufer.</p></div>
          <div><h3>3. Lieferung</h3><p>Nach Bestätigung produzieren und liefern wir Ihre Auswahl handgefertigt.</p></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head"><div><p class="kicker">Kontakt für Wiederverkäufer</p><h2>Jetzt Grosshandelsanfrage senden</h2></div></div>
        <form class="form-grid" data-demo-form>
          <div class="form-row-2">
            <div>
              <label for="gh-name">Name</label>
              <input type="text" id="gh-name" name="name" required autocomplete="name">
            </div>
            <div>
              <label for="gh-firma">Firma / Geschäft</label>
              <input type="text" id="gh-firma" name="company" required autocomplete="organization">
            </div>
          </div>
          <div class="form-row-2">
            <div>
              <label for="gh-email">E-Mail</label>
              <input type="email" id="gh-email" name="email" required autocomplete="email">
            </div>
            <div>
              <label for="gh-ort">Ort / Kanton</label>
              <input type="text" id="gh-ort" name="location" autocomplete="address-level2">
            </div>
          </div>
          <div>
            <label for="gh-nachricht">Nachricht — Wunschsortiment, Stückzahlen</label>
            <textarea id="gh-nachricht" name="message" required></textarea>
          </div>
          <div>
            <button type="submit" class="btn btn-primary">Anfrage senden</button>
            <p class="form-note" style="margin-top:10px;">Wir zeigen auf dieser Seite bewusst keine Endkundenpreise — Grosshandelskonditionen erhalten Sie direkt von uns.</p>
          </div>
          <div class="form-success" role="status">Danke für Ihre Anfrage! Wir melden uns innerhalb weniger Werktage.</div>
        </form>
      </div>
    </section>
    """
    return page(TITLE, DESC, "/grosshandel/", "/grosshandel/", body, extra_jsonld=crumbs_ld)
