# -*- coding: utf-8 -*-
from common import page, breadcrumbs, BASE_URL, BRAND
from content_loader import load_products, load_magnete

GIPSFIGUREN = load_products("gipsfiguren")
KERZEN = load_products("kerzen")
MAGNETE, MAGNETE_PLACEHOLDER_MOTIFS = load_magnete()

MAGNET_FILTERS = [
    ("all", "Alle"),
    ("bern", "Bern"),
    ("zentralschweiz", "Zentralschweiz"),
    ("wallis", "Wallis"),
    ("weitere", "Weitere Regionen"),
]


def product_card(p, category_path):
    return f"""<article class="product-card" data-product-card itemscope itemtype="https://schema.org/Product">
            <a href="{category_path}{p['slug']}/" class="thumb">
              <img src="/assets/img/{p['img']}" width="{p['w']}" height="{p['h']}" alt="{p['alt']}" loading="lazy" itemprop="image">
            </a>
            <div class="info">
              <h3 itemprop="name"><a href="{category_path}{p['slug']}/">{p['creative']}</a></h3>
              <p class="sku">{p['seo']}</p>
              <div class="price-row" itemprop="offers" itemscope itemtype="https://schema.org/Offer">
                <span class="price">CHF <span itemprop="price">{p['price']}</span><meta itemprop="priceCurrency" content="CHF"></span>
                <span class="stock" itemprop="availability" content="https://schema.org/InStock">{p['stock']}</span>
              </div>
            </div>
          </article>"""


def itemlist_ld(products, category_path):
    entries = []
    for i, p in enumerate(products, start=1):
        entries.append(
            f'{{"@type":"ListItem","position":{i},"url":"{BASE_URL}{category_path}{p["slug"]}/"}}'
        )
    return f"""<script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{",".join(entries)}]}}
  </script>"""


# ---------------------------------------------------------------- Gipsfiguren
def build_gipsfiguren():
    title = f"Gipsfiguren handgemacht — Katzen, Eulen & mehr | {BRAND}"
    desc = "Handgefertigte Gipsfiguren aus dem Kanton Bern: Katzen, Eulen und weitere Tiermotive, einzeln gegossen und von Hand bemalt. Ideal als Geschenk."
    crumbs_html, crumbs_ld = breadcrumbs([("Startseite", "/"), ("Gipsfiguren", None)])
    cards = "\n          ".join(product_card(p, "/gipsfiguren/") for p in GIPSFIGUREN)
    body = f"""
    {crumbs_html}
    <header class="page-hero container">
      <p class="kicker">Sortiment</p>
      <h1>Gipsfiguren</h1>
      <p class="lead">Jede Figur beginnt als flüssiger Gips in einer Silikonform und wird nach dem Trocknen von Hand geschliffen, grundiert und bemalt. Die Motive — vor allem Katzen und Eulen — entstehen in kleinen Serien, daher variiert die Bemalung leicht von Stück zu Stück.</p>
    </header>
    <section class="section">
      <div class="container">
        <div class="product-grid">
          {cards}
          <article class="product-card" style="align-items:center; justify-content:center; text-align:center; padding:20px;">
            <p style="margin:0; color:var(--ink-soft); font-size:.9rem;">Weitere Tiermotive folgen laufend — bei Interesse an einem bestimmten Motiv einfach <a href="/kontakt/" style="color:var(--clay); font-weight:600;">anfragen</a>.</p>
          </article>
        </div>
      </div>
    </section>
    """
    return page(title, desc, "/gipsfiguren/", "/gipsfiguren/", body,
                extra_jsonld=crumbs_ld + itemlist_ld(GIPSFIGUREN, "/gipsfiguren/"))


# ---------------------------------------------------------------- Kerzen
def build_kerzen():
    title = f"Handgegossene Kerzen mit Alpenmotiv | {BRAND}"
    desc = "Handgegossene Kerzen mit gemalten Alpen- und Ortsmotiven aus dem Kanton Bern. Für Zuhause oder als besonderes Geschenk."
    crumbs_html, crumbs_ld = breadcrumbs([("Startseite", "/"), ("Kerzen", None)])
    cards = "\n          ".join(product_card(p, "/kerzen/") for p in KERZEN)
    body = f"""
    {crumbs_html}
    <header class="page-hero container">
      <p class="kicker">Sortiment</p>
      <h1>Kerzen</h1>
      <p class="lead">Unsere Kerzen werden von Hand gegossen und anschliessend mit Landschaftsmotiven bemalt — Bergseen, Gipfel und kleine Hütten. Jede Kerze ist ein Einzelstück und eignet sich als Dekoration oder Geschenk.</p>
    </header>
    <section class="section">
      <div class="container">
        <div class="product-grid">
          {cards}
          <article class="product-card" style="align-items:center; justify-content:center; text-align:center; padding:20px;">
            <p style="margin:0; color:var(--ink-soft); font-size:.9rem;">Weitere Kerzenmotive in Vorbereitung — <a href="/kontakt/" style="color:var(--clay); font-weight:600;">fragen Sie nach individuellen Motiven</a>.</p>
          </article>
        </div>
      </div>
    </section>
    """
    return page(title, desc, "/kerzen/", "/kerzen/", body,
                extra_jsonld=crumbs_ld + itemlist_ld(KERZEN, "/kerzen/"))


# ---------------------------------------------------------------- Magnete (Galerie, keine Einzel-URLs)
def build_magnete():
    title = f"Schweizer Souvenir-Magnete — Bern, Luzern, Zermatt & mehr | {BRAND}"
    desc = "Handbemalte Kühlschrankmagnete mit Motiven aus der ganzen Schweiz — Bern, Luzern, Zermatt und laufend neue Städte. Übersicht aller aktuellen Designs."
    crumbs_html, crumbs_ld = breadcrumbs([("Startseite", "/"), ("Magnete", None)])

    real_cards = []
    magnet_ld_entries = []
    for m in MAGNETE:
        in_stock = m.get("stock", True)
        stock_label = "Auf Lager" if in_stock else "Ausverkauft"
        availability = "https://schema.org/InStock" if in_stock else "https://schema.org/OutOfStock"
        real_cards.append(f"""<article class="product-card" data-product-card data-group="{m['group']}" data-name="{m['name']}" itemscope itemtype="https://schema.org/Product">
            <div class="thumb">
              <span class="badge">{m['name']}</span>
              <img src="/assets/img/{m['img']}" width="{m['w']}" height="{m['h']}" alt="{m['alt']}" loading="lazy" itemprop="image">
            </div>
            <div class="info">
              <h3 itemprop="name">Magnet {m['name']}</h3>
              <p class="sku">Motiv-Magnet, Kunststein, handbemalt</p>
              <div class="price-row" itemprop="offers" itemscope itemtype="https://schema.org/Offer">
                <span class="price">CHF <span itemprop="price">{m['price']}</span><meta itemprop="priceCurrency" content="CHF"></span>
                <span class="stock" itemprop="availability" content="{availability}">{stock_label}</span>
              </div>
            </div>
          </article>""")
        magnet_ld_entries.append(
            f'{{"@type":"Product","name":"Magnet {m["name"]}","offers":{{"@type":"Offer","price":"{m["price"]}","priceCurrency":"CHF","availability":"{availability}"}}}}'
        )

    placeholder_cards = []
    for name in MAGNETE_PLACEHOLDER_MOTIFS:
        placeholder_cards.append(f"""<article class="product-card" data-product-card data-group="weitere" data-name="{name}">
            <div class="thumb" style="display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,var(--plaster-2),var(--stone-line));">
              <span style="font-family:var(--font-display);font-style:italic;color:var(--stone);">Foto folgt</span>
            </div>
            <div class="info">
              <h3>Magnet {name} <span style="font-weight:400;color:var(--ink-soft);">[PRODUCT_NAME_SEO]</span></h3>
              <p class="sku">In Vorbereitung</p>
              <div class="price-row">
                <span class="price">CHF [PRICE]</span>
                <span class="stock" style="color:var(--ink-soft);">In Kürze</span>
              </div>
            </div>
          </article>""")

    filter_chips = "\n          ".join(
        f'<button type="button" class="filter-chip" data-group="{g}" aria-pressed="{"true" if g == "all" else "false"}">{label}</button>'
        for g, label in MAGNET_FILTERS
    )

    body = f"""
    {crumbs_html}
    <header class="page-hero container">
      <p class="kicker">Sortiment</p>
      <h1>Magnete</h1>
      <p class="lead">Über die Zeit sind viele verschiedene Magnet-Designs entstanden — von Berner Altstadtgassen bis zum Matterhorn. Da sich das Angebot laufend ändert, zeigen wir hier eine gesammelte Übersicht statt einzelner Produktseiten.</p>
    </header>
    <section class="section">
      <div class="container">
        <div class="filter-row" data-filter-chips role="group" aria-label="Nach Region filtern">
          {filter_chips}
        </div>
        <div class="filter-search">
          <span aria-hidden="true">🔍</span>
          <input type="search" data-filter-search placeholder="Ort suchen, z. B. Zermatt" aria-label="Magnet nach Ortsname suchen">
        </div>
        <div class="product-grid">
          {"".join(real_cards)}
          {"".join(placeholder_cards)}
        </div>
      </div>
    </section>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{",".join(magnet_ld_entries)}]}}
    </script>
    """
    return page(title, desc, "/magnete/", "/magnete/", body, extra_jsonld=crumbs_ld)
