# -*- coding: utf-8 -*-
from common import page, breadcrumbs, BRAND

TITLE = f"Über uns — die Werkstatt hinter {BRAND} | {BRAND}"
DESC = f"Die Geschichte von {BRAND}: handgefertigte Gipsfiguren, Magnete und Kerzen aus dem Kanton Bern — vom Guss bis zur Bemalung von Hand."


def build():
    crumbs_html, crumbs_ld = breadcrumbs([("Startseite", "/"), ("Über uns", None)])
    body = f"""
    {crumbs_html}
    <header class="page-hero container">
      <p class="kicker">Unsere Geschichte</p>
      <h1>Von der ersten Gussform bis zum Marktstand</h1>
      <p class="lead">[Platzhalter: Kurze Geschichte der Gründerin/des Gründers — wie die Werkstatt entstanden ist, seit wann gearbeitet wird, was den Beruf reizt.]</p>
    </header>

    <section class="section">
      <div class="container">
        <div class="split" style="background:var(--card); color:var(--ink); border:1px solid var(--stone-line);">
          <img src="/assets/img/markt-tisch-uebersicht.webp" width="1280" height="960"
               alt="Handgefertigte Gipsfiguren und Magnete ausgestellt auf einem Marktstand" loading="lazy">
          <div class="split-copy">
            <p class="kicker">Der Prozess</p>
            <h2 style="color:var(--ink);">Guss, Schliff, Bemalung — jeder Schritt von Hand</h2>
            <p style="color:var(--ink-soft);">[Platzhalter: Beschreibung des Herstellungsprozesses — Gipsguss in Silikonformen, Trocknungszeit, Schleifen, Grundierung, Bemalung in mehreren Schichten, Versiegelung.]</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head"><div><p class="kicker">Auf den Märkten</p><h2>Warum wir persönlich verkaufen</h2></div></div>
        <p style="max-width:64ch;">[Platzhalter: Warum der Direktverkauf auf Märkten wichtig ist — persönlicher Kontakt, direktes Feedback zu Motiven, Sichtbarkeit der Handarbeit.]</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head"><div><p class="kicker">Vertrauen</p><h2>Warum Wiederverkäufer mit uns arbeiten</h2></div></div>
        <p style="max-width:64ch;">Für Geschäfte und Hotels, die unsere Produkte listen möchten: Wir liefern verlässlich, in gleichbleibender Qualität, und stehen mit unserem Namen hinter jedem Stück. Mehr dazu auf der <a href="/grosshandel/" style="color:var(--clay); font-weight:600;">Grosshandelsseite</a>.</p>
      </div>
    </section>
    """
    return page(TITLE, DESC, "/ueber-uns/", "/ueber-uns/", body, extra_jsonld=crumbs_ld)
