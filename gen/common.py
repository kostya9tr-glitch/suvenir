# -*- coding: utf-8 -*-
"""
Gemeinsame Bausteine für den statischen Seitengenerator.
BRAND_NAME und WORKSHOP_ADDRESS sind bewusst als Platzhalter markiert
(siehe Website_Build_Prompt.md, Abschnitt 8).
"""

from content_loader import load_settings

_settings = load_settings()
BASE_URL = _settings["base_url"]          # in Decap CMS unter "Einstellungen" editierbar
BRAND = _settings["brand"]
ADDRESS_STREET = _settings["address_street"]
ADDRESS_CITY = _settings["address_city"]
PHONE = _settings["phone"]
EMAIL = _settings["email"]

NAV = [
    ("/", "Startseite"),
    ("/gipsfiguren/", "Gipsfiguren"),
    ("/magnete/", "Magnete"),
    ("/kerzen/", "Kerzen"),
    ("/grosshandel/", "Grosshandel", "b2b"),
    ("/ueber-uns/", "Über uns"),
    ("/kontakt/", "Kontakt"),
    ("/blog/", "Blog"),
]

FOOTER_CATEGORY_LINKS = [
    ("/gipsfiguren/", "Gipsfiguren"),
    ("/magnete/", "Magnete"),
    ("/kerzen/", "Kerzen"),
    ("/grosshandel/", "Für Wiederverkäufer"),
]
FOOTER_INFO_LINKS = [
    ("/ueber-uns/", "Über uns"),
    ("/kontakt/", "Kontakt"),
    ("/blog/", "Blog"),
    ("/kontakt/#maerkte", "Marktkalender"),
]
FOOTER_LEGAL_LINKS = [
    ("/impressum/", "Impressum"),
    ("/datenschutz/", "Datenschutz"),
]


def _nav_html(active_path):
    items = []
    for entry in NAV:
        path, label = entry[0], entry[1]
        extra_class = entry[2] if len(entry) > 2 else None
        current = ' aria-current="page"' if path == active_path else ""
        li_class = f' class="nav-{extra_class}"' if extra_class else ""
        items.append(f'<li{li_class}><a href="{path}"{current}>{label}</a></li>')
    return "\n        ".join(items)


def head(title, description, canonical_path, extra_jsonld="", robots="index, follow"):
    canonical = f"{BASE_URL}{canonical_path}"
    return f"""<meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta name="theme-color" content="#AB5236">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="/assets/css/style.css">
  {extra_jsonld}"""


def header(active_path):
    return f"""<header class="site-header">
    <div class="container header-inner">
      <a href="/" class="brand">
        <span class="mark" aria-hidden="true">G</span>
        <span>{BRAND}
          <small>Handgemacht in der Schweiz</small>
        </span>
      </a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="main-nav" aria-label="Menü öffnen">
        <span></span>
      </button>
      <nav class="main-nav" id="main-nav" aria-label="Hauptnavigation">
        <ul>
          {_nav_html(active_path)}
        </ul>
      </nav>
    </div>
  </header>"""


def footer():
    cat_links = "\n          ".join(f'<li><a href="{p}">{l}</a></li>' for p, l in FOOTER_CATEGORY_LINKS)
    info_links = "\n          ".join(f'<li><a href="{p}">{l}</a></li>' for p, l in FOOTER_INFO_LINKS)
    legal_links = "\n          ".join(f'<li><a href="{p}">{l}</a></li>' for p, l in FOOTER_LEGAL_LINKS)
    return f"""<footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <p class="footer-brand">{BRAND}</p>
        <p style="color:#CBBFA6; max-width:32ch;">Gipsfiguren, Magnete &amp; Kerzen — von Hand gefertigt in {ADDRESS_CITY}. Zu finden auf Märkten in der ganzen Schweiz.</p>
      </div>
      <div>
        <h4>Sortiment</h4>
        <ul class="footer-links">
          {cat_links}
        </ul>
      </div>
      <div>
        <h4>Service</h4>
        <ul class="footer-links">
          {info_links}
        </ul>
      </div>
      <div>
        <h4>Kontakt</h4>
        <ul class="footer-links">
          <li>{ADDRESS_STREET}, {ADDRESS_CITY}</li>
          <li><a href="tel:{PHONE}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <span>© <span data-year>2026</span> {BRAND}. Alle Rechte vorbehalten.</span>
      <ul class="footer-links" style="flex-direction:row; gap:16px;">
        {legal_links}
      </ul>
    </div>
  </footer>
  <script>document.querySelector('[data-year]').textContent = new Date().getFullYear();</script>
  <script src="/assets/js/main.js"></script>"""


def breadcrumbs(trail):
    """trail: list of (label, path_or_None_for_current)"""
    lis = []
    items_ld = []
    for i, (label, path) in enumerate(trail, start=1):
        if path:
            lis.append(f'<li><a href="{path}">{label}</a></li>')
            items_ld.append(
                f'{{"@type":"ListItem","position":{i},"name":"{label}","item":"{BASE_URL}{path}"}}'
            )
        else:
            lis.append(f'<li aria-current="page">{label}</li>')
            items_ld.append(f'{{"@type":"ListItem","position":{i},"name":"{label}"}}')
    html = f"""<nav class="breadcrumbs container" aria-label="Breadcrumb">
      <ol>
        {"".join(lis)}
      </ol>
    </nav>"""
    ld = f"""<script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{",".join(items_ld)}]}}
  </script>"""
    return html, ld


def page(title, description, canonical_path, active_path, body, extra_jsonld="", robots="index, follow"):
    return f"""<!DOCTYPE html>
<html lang="de-CH">
<head>
  {head(title, description, canonical_path, extra_jsonld, robots)}
</head>
<body>
  <script src="https://identity.netlify.com/v1/netlify-identity-widget.js"></script>
  <script>
    if (window.netlifyIdentity) {{
      window.netlifyIdentity.on("init", function (user) {{
        if (!user) {{
          window.netlifyIdentity.on("login", function () {{ document.location.href = "/admin/"; }});
        }}
      }});
    }}
  </script>
  {header(active_path)}
  <main id="main">
    {body}
  </main>
  {footer()}
</body>
</html>
"""
