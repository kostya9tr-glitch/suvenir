# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from common import BASE_URL
import page_home
import page_categories as cat
import page_products as prod
import page_grosshandel
import page_ueberuns
import page_kontakt
import page_blog
import page_legal

OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

pages = {}

# Home
pages["index.html"] = page_home.HTML

# Categories
pages["gipsfiguren/index.html"] = cat.build_gipsfiguren()
pages["kerzen/index.html"] = cat.build_kerzen()
pages["magnete/index.html"] = cat.build_magnete()

# Product detail pages
pages.update(prod.build_all_product_pages())

# Grosshandel / Über uns / Kontakt
pages["grosshandel/index.html"] = page_grosshandel.build()
pages["ueber-uns/index.html"] = page_ueberuns.build()
pages["kontakt/index.html"] = page_kontakt.build()

# Blog
pages.update(page_blog.build_all())

# Legal
pages["impressum/index.html"] = page_legal.build_impressum()
pages["datenschutz/index.html"] = page_legal.build_datenschutz()

# ---- write files ----
for rel_path, html in pages.items():
    full_path = os.path.join(OUT_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(html)

print(f"{len(pages)} Seiten geschrieben nach {OUT_DIR}")

# ---- sitemap.xml (noindex-Seiten ausgeschlossen) ----
sitemap_urls = []
for rel_path in pages:
    if rel_path in ("impressum/index.html", "datenschutz/index.html"):
        continue
    if rel_path == "index.html":
        url_path = "/"
    else:
        url_path = "/" + rel_path.replace("index.html", "")
    sitemap_urls.append(url_path)

sitemap_urls = sorted(set(sitemap_urls))
sitemap_entries = "\n".join(
    f"  <url><loc>{BASE_URL}{p}</loc><changefreq>{'daily' if p=='/' else 'weekly'}</changefreq></url>"
    for p in sitemap_urls
)
sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_entries}
</urlset>
"""
with open(os.path.join(OUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print(f"sitemap.xml mit {len(sitemap_urls)} URLs geschrieben")

# ---- robots.txt ----
robots_txt = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
with open(os.path.join(OUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_txt)
print("robots.txt geschrieben")
