# -*- coding: utf-8 -*-
from common import page, BRAND, BASE_URL, ADDRESS_STREET, ADDRESS_CITY, PHONE, EMAIL
from content_loader import load_maerkte

MAERKTE = load_maerkte()[:3]
MAERKTE_ROWS = "\n            ".join(
    f'<div class="market-item"><span class="date">{m["date"]}</span><span class="place">{m["place"]}</span></div>'
    for m in MAERKTE
) or '<div class="market-item"><span class="place">Termine folgen in Kürze.</span></div>'

TITLE = f"{BRAND} — Gipsfiguren, Magnete & Kerzen handgemacht in der Schweiz"
DESC = f"{BRAND}: handgefertigte Gipsfiguren, Schweizer Souvenir-Magnete und Kerzen aus dem Kanton Bern. Von Hand bemalt, auf Schweizer Märkten und online."

LOCAL_BUSINESS_LD = f"""<script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "{BRAND}",
    "image": "{BASE_URL}/assets/img/markt-tisch-uebersicht.webp",
    "url": "{BASE_URL}/",
    "telephone": "{PHONE}",
    "email": "{EMAIL}",
    "priceRange": "CHF 8–40",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "{ADDRESS_STREET}",
      "addressLocality": "[Ort]",
      "addressRegion": "Bern",
      "postalCode": "[PLZ]",
      "addressCountry": "CH"
    }},
    "areaServed": "CH",
    "description": "Handgefertigte Gipsfiguren, Magnete und Kerzen aus dem Kanton Bern.",
    "makesOffer": [
      {{"@type":"Offer","itemOffered":{{"@type":"ProductGroup","name":"Gipsfiguren"}}}},
      {{"@type":"Offer","itemOffered":{{"@type":"ProductGroup","name":"Magnete"}}}},
      {{"@type":"Offer","itemOffered":{{"@type":"ProductGroup","name":"Kerzen"}}}}
    ]
  }}
  </script>"""

BODY = """
    <section class="hero">
      <div class="container hero-grid">
        <div class="hero-copy">
          <p class="kicker">Handgemacht im Kanton Bern</p>
          <h1>Gipsfiguren, Magnete &amp; Kerzen — von Hand gefertigt, nicht am Fliessband</h1>
          <p class="lead">[BRAND_NAME] fertigt seit [Jahr] jedes Stück einzeln in Gips, bemalt von Hand und gebrannte Kerzen mit Alpen-Motiven. Zu finden auf Märkten in der ganzen Schweiz — und jetzt auch online.</p>
          <div class="hero-actions">
            <a href="/gipsfiguren/" class="btn btn-primary">Sortiment entdecken</a>
            <a href="/ueber-uns/" class="btn btn-outline">Unsere Geschichte</a>
          </div>
        </div>
        <figure class="hero-media">
          <img src="/assets/img/markt-tisch-uebersicht.webp" width="1280" height="960"
               alt="Marktstand mit handbemalten Gipsfiguren, Magneten und Kerzen auf einem Holztisch"
               loading="eager" fetchpriority="high">
          <figcaption>Unser Stand — jedes Stück ein Unikat</figcaption>
        </figure>
      </div>
    </section>

    <div class="trust-strip">
      <div class="container">
        <ul>
          <li><span class="ico" aria-hidden="true">✋</span> Handgemacht in der Schweiz</li>
          <li><span class="ico" aria-hidden="true">🎨</span> Von Hand bemalt, jedes Stück ein Unikat</li>
          <li><span class="ico" aria-hidden="true">🏔️</span> Motive aus der ganzen Schweiz</li>
          <li><span class="ico" aria-hidden="true">📦</span> Auch für Wiederverkäufer</li>
        </ul>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="kicker">Unser Sortiment</p>
            <h2>Drei Handwerke, ein Werkstattprinzip</h2>
          </div>
        </div>
        <div class="cat-grid">
          <a class="cat-card" href="/gipsfiguren/">
            <img src="/assets/img/gipsfigur-eule.webp" width="900" height="900"
                 alt="Handbemalte Gipsfigur einer Eule mit bernsteinfarbenen Augen" loading="lazy">
            <div class="cat-body">
              <h3>Gipsfiguren</h3>
              <p>Katzen, Eulen und weitere Tierfiguren, Stück für Stück gegossen und von Hand bemalt.</p>
              <span class="cat-link">Gipsfiguren ansehen →</span>
            </div>
          </a>
          <a class="cat-card" href="/magnete/">
            <img src="/assets/img/magnete-gruppe-see-berge.webp" width="1280" height="960"
                 alt="Sieben Schweizer Souvenir-Magnete mit Bern, Luzern, Zermatt und weiteren Motiven" loading="lazy">
            <div class="cat-body">
              <h3>Magnete</h3>
              <p>Kühlschrankmagnete mit Motiven aus der ganzen Schweiz — laufend neue Städte und Sujets.</p>
              <span class="cat-link">Magnete ansehen →</span>
            </div>
          </a>
          <a class="cat-card" href="/kerzen/">
            <img src="/assets/img/kerze-alpen-motiv.webp" width="900" height="900"
                 alt="Handgegossene Kerze mit gemaltem Alpenmotiv und Bergsee" loading="lazy">
            <div class="cat-body">
              <h3>Kerzen</h3>
              <p>Handgegossene Kerzen mit gemalten Alpen- und Ortsmotiven, für Zuhause oder als Geschenk.</p>
              <span class="cat-link">Kerzen ansehen →</span>
            </div>
          </a>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="split">
          <img src="/assets/img/geschenkset-box.webp" width="1200" height="675"
               alt="Geschenkbox mit Magneten, einer Gipsfigur-Katze und einer Eulen-Kerze, dekoriert mit Edelweiss" loading="lazy">
          <div class="split-copy">
            <p class="kicker" style="color:#E0A88F;">Ideal zum Verschenken</p>
            <h2>Geschenksets nach Wunsch</h2>
            <p>Wir stellen auf Anfrage kleine Sets aus Magnet, Figur und Kerze zusammen — liebevoll verpackt, ideal als Mitbringsel oder Firmengeschenk.</p>
            <ul>
              <li>Freie Auswahl aus dem gesamten Sortiment</li>
              <li>Verpackung mit Karton, Papier und Naturmaterial</li>
              <li>Auch in grösseren Stückzahlen möglich</li>
            </ul>
            <a href="/kontakt/" class="btn btn-on-dark">Set anfragen</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="markets">
          <img src="/assets/img/markt-tisch-uebersicht.webp" width="1280" height="960"
               alt="Verkaufsstand mit Gipsfiguren und Magneten an einem Schweizer Markt" loading="lazy">
          <div class="markets-copy">
            <p class="kicker">Wo Sie uns finden</p>
            <h2>Wir sind regelmässig auf Märkten unterwegs</h2>
            <p>Am liebsten verkaufen wir persönlich — kommen Sie vorbei und sehen Sie die Werkstattarbeit aus nächster Nähe.</p>
            <div class="market-list" id="naechste-maerkte">
              {MAERKTE_ROWS}
            </div>
            <a href="/kontakt/#maerkte" class="btn btn-outline">Alle Termine ansehen</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="kicker">Für den Handel</p>
            <h2>Sie führen ein Geschenkgeschäft, Hotel oder Blumenladen?</h2>
            <p style="max-width:56ch;">Wir beliefern Wiederverkäufer in der ganzen Schweiz — mit verlässlicher Qualität und Motiven, die es so nicht im Grosshandelskatalog gibt.</p>
          </div>
          <a href="/grosshandel/" class="btn btn-primary">Zum Grosshandel</a>
        </div>
      </div>
    </section>
"""

BODY = BODY.replace("{MAERKTE_ROWS}", MAERKTE_ROWS)
HTML = page(TITLE, DESC, "/", "/", BODY, extra_jsonld=LOCAL_BUSINESS_LD)
