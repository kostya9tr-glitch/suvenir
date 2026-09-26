# -*- coding: utf-8 -*-
from common import page, breadcrumbs, BRAND, ADDRESS_STREET, ADDRESS_CITY, PHONE, EMAIL
from content_loader import load_maerkte

TITLE = f"Kontakt & Marktkalender | {BRAND}"
DESC = f"Kontaktieren Sie {BRAND}: Adresse der Werkstatt im Kanton Bern, Kontaktformular und aktuelle Markttermine."

MAP_EMBED_SRC = "https://www.google.com/maps?q=Bern,Switzerland&output=embed"


def build():
    crumbs_html, crumbs_ld = breadcrumbs([("Startseite", "/"), ("Kontakt", None)])
    markets = load_maerkte()
    market_rows = "\n            ".join(
        f'<div class="market-item"><span class="date">{m["date"]}</span><span class="place">{m["place"]}</span></div>'
        for m in markets
    ) or '<div class="market-item"><span class="place">Termine folgen in Kürze.</span></div>'
    body = f"""
    {crumbs_html}
    <header class="page-hero container">
      <p class="kicker">Kontakt</p>
      <h1>Schreiben Sie uns, oder besuchen Sie uns auf dem Markt</h1>
      <p class="lead">Für Fragen zu Produkten, individuellen Wünschen oder Grosshandel erreichen Sie uns über das Formular, telefonisch oder persönlich auf einem unserer Markttermine.</p>
    </header>

    <section class="section">
      <div class="container" style="display:grid; gap:40px; grid-template-columns:1fr; align-items:start;">
        <div style="display:grid; gap:40px; grid-template-columns:1fr;" class="kontakt-grid">
          <div>
            <h2>Werkstatt</h2>
            <p>{ADDRESS_STREET}<br>{ADDRESS_CITY}</p>
            <p><a href="tel:{PHONE}" style="color:var(--clay); font-weight:600;">{PHONE}</a><br>
               <a href="mailto:{EMAIL}" style="color:var(--clay); font-weight:600;">{EMAIL}</a></p>
            <p class="form-note">Die Werkstatt ist nicht öffentlich zugänglich — besuchen Sie uns auf einem unserer Markttermine, oder vereinbaren Sie telefonisch einen Termin.</p>
            <div class="map-embed">
              <iframe src="{MAP_EMBED_SRC}" title="Kartenausschnitt Werkstatt-Standort" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
          </div>

          <div>
            <h2>Nachricht senden</h2>
            <form class="form-grid" data-demo-form>
              <div class="form-row-2">
                <div>
                  <label for="k-name">Name</label>
                  <input type="text" id="k-name" name="name" required autocomplete="name">
                </div>
                <div>
                  <label for="k-email">E-Mail</label>
                  <input type="email" id="k-email" name="email" required autocomplete="email">
                </div>
              </div>
              <div>
                <label for="k-betreff">Betreff</label>
                <select id="k-betreff" name="subject">
                  <option>Allgemeine Frage</option>
                  <option>Bestellung / Reservation</option>
                  <option>Individuelles Motiv</option>
                  <option>Sonstiges</option>
                </select>
              </div>
              <div>
                <label for="k-nachricht">Nachricht</label>
                <textarea id="k-nachricht" name="message" required></textarea>
              </div>
              <div>
                <button type="submit" class="btn btn-primary">Nachricht senden</button>
              </div>
              <div class="form-success" role="status">Danke für Ihre Nachricht! Wir melden uns so schnell wie möglich.</div>
            </form>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt" id="maerkte">
      <div class="container">
        <div class="section-head"><div><p class="kicker">Marktkalender</p><h2>Nächste Markttermine</h2></div></div>
        <div class="market-list" style="max-width:640px;">
          {market_rows}
        </div>
      </div>
    </section>
    <style>@media(min-width:800px){{.kontakt-grid{{grid-template-columns:1fr 1fr;}}}}</style>
    """
    return page(TITLE, DESC, "/kontakt/", "/kontakt/", body, extra_jsonld=crumbs_ld)
