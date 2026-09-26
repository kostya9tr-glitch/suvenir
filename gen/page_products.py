# -*- coding: utf-8 -*-
from common import page, breadcrumbs, BASE_URL, BRAND
from content_loader import load_products

GIPSFIGUREN = load_products("gipsfiguren")
KERZEN = load_products("kerzen")


def product_ld(p, category_path, category_label):
    url = f"{BASE_URL}{category_path}{p['slug']}/"
    return f"""<script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "{p['seo']}",
    "image": "{BASE_URL}/assets/img/{p['img']}",
    "description": "{p['desc']}",
    "sku": "{p['slug'].upper()}",
    "brand": {{"@type":"Brand","name":"{BRAND}"}},
    "category": "{category_label}",
    "url": "{url}",
    "offers": {{
      "@type": "Offer",
      "url": "{url}",
      "priceCurrency": "CHF",
      "price": "{p['price']}",
      "availability": "https://schema.org/InStock",
      "itemCondition": "https://schema.org/NewCondition"
    }}
  }}
  </script>"""


def build_product_page(p, category_path, category_label, category_name):
    title = f"{p['creative']} — {p['seo']} | {BRAND}"
    desc = f"{p['seo']}. Material: {p['material']}. Grösse: {p['size']}. Handgefertigt in der Schweiz."
    crumbs_html, crumbs_ld = breadcrumbs([
        ("Startseite", "/"),
        (category_name, category_path),
        (p['creative'] if p['creative'] != "[PRODUCT_NAME_CREATIVE]" else p['seo'], None),
    ])
    stripe_link = (p.get("stripe_link") or "").strip()
    if stripe_link:
        stripe_btn = f'<a href="{stripe_link}" class="btn btn-primary">Jetzt bezahlen (Stripe)</a>'
    else:
        stripe_btn = '<a href="/kontakt/" class="btn btn-primary">Auf Anfrage bestellen</a>'
    body = f"""
    {crumbs_html}
    <section class="section" style="padding-top:24px;">
      <div class="container">
        <div class="product-detail">
          <div>
            <div class="gallery-main" data-gallery-main>
              <img src="/assets/img/{p['img']}" width="{p['w']}" height="{p['h']}" alt="{p['alt']}" id="pd-main-img">
            </div>
            <div class="gallery-thumbs">
              <button type="button" data-gallery-thumb data-full-src="/assets/img/{p['img']}" data-full-alt="{p['alt']}" aria-current="true">
                <img src="/assets/img/{p['img']}" width="120" height="120" alt="" loading="lazy">
              </button>
              <button type="button" class="thumb-placeholder" data-gallery-thumb data-full-src="/assets/img/{p['img']}" data-full-alt="{p['alt']} — Ansicht von der Seite" aria-current="false" title="Weitere Ansicht folgt">
                <img src="/assets/img/{p['img']}" width="120" height="120" alt="" loading="lazy" style="filter:grayscale(.4);">
              </button>
            </div>
          </div>
          <div class="pd-info">
            <p class="sku">Art.-Nr. {p['slug'].upper()}</p>
            <h1>{p['creative']}</h1>
            <p class="seo-name">{p['seo']}</p>
            <p class="pd-price">CHF {p['price']}</p>
            <span class="pd-stock">{p['stock']}</span>
            <p>{p['desc']}</p>
            <dl class="pd-specs">
              <div><dt>Material</dt><dd>{p['material']}</dd></div>
              <div><dt>Grösse</dt><dd>{p['size']}</dd></div>
              <div><dt>Herkunft</dt><dd>Handgefertigt im Kanton Bern, Schweiz</dd></div>
            </dl>
            <div class="pd-actions">
              {stripe_btn}
              <a href="{category_path}" class="btn btn-outline">Zurück zu {category_name}</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
    return page(title, desc, f"{category_path}{p['slug']}/", category_path, body,
                extra_jsonld=crumbs_ld + product_ld(p, category_path, category_label))


def build_all_product_pages():
    pages = {}
    for p in GIPSFIGUREN:
        pages[f"gipsfiguren/{p['slug']}/index.html"] = build_product_page(
            p, "/gipsfiguren/", "Gipsfiguren", "Gipsfiguren")
    for p in KERZEN:
        pages[f"kerzen/{p['slug']}/index.html"] = build_product_page(
            p, "/kerzen/", "Kerzen", "Kerzen")
    return pages
