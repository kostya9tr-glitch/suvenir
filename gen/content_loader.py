# -*- coding: utf-8 -*-
"""
Liest die Inhalte aus /content (YAML + Markdown) — das ist der Teil,
den Decap CMS über /admin bearbeitet. Bild-Grössen (width/height)
werden automatisch aus der Bilddatei gelesen, damit im CMS niemand
Pixelmasse eintippen muss.
"""
import os
import glob
import yaml
import markdown as md

SITE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONTENT_DIR = os.path.join(SITE_DIR, "content")
IMG_DIR = os.path.join(SITE_DIR, "assets", "img")

_dim_cache = {}


def image_size(filename):
    """Gibt (width, height) eines Bilds unter assets/img zurück. Fällt auf 900x900 zurück,
    falls die Datei (noch) nicht existiert, z. B. weil sie gerade erst im CMS hochgeladen wird."""
    if not filename:
        return 900, 900
    if filename in _dim_cache:
        return _dim_cache[filename]
    path = os.path.join(IMG_DIR, os.path.basename(filename))
    try:
        from PIL import Image
        with Image.open(path) as im:
            size = im.size
    except Exception:
        size = (900, 900)
    _dim_cache[filename] = size
    return size


def _load_yaml(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or default


def load_settings():
    data = _load_yaml(os.path.join(CONTENT_DIR, "settings.yaml"), {}) or {}
    return {
        "brand": data.get("brand", "[BRAND_NAME]"),
        "address_street": data.get("address_street", "[Strasse Nr.]"),
        "address_city": data.get("address_city", "[PLZ Ort], Kanton Bern"),
        "phone": data.get("phone", "[Telefonnummer]"),
        "email": data.get("email", "info@ihre-domain.ch"),
        "base_url": (data.get("base_url") or "https://www.IHRE-DOMAIN.ch").rstrip("/"),
    }


def _finalize_product(d):
    w, h = image_size(d.get("image", ""))
    d["w"], d["h"] = w, h
    d.setdefault("stripe_link", "")
    return d


def load_products(category):
    """category: 'gipsfiguren' oder 'kerzen'"""
    folder = os.path.join(CONTENT_DIR, "produkte", category)
    items = []
    for path in sorted(glob.glob(os.path.join(folder, "*.yaml"))):
        d = _load_yaml(path, {})
        if d:
            items.append(_finalize_product(d))
    return items


def load_magnete():
    data = _load_yaml(os.path.join(CONTENT_DIR, "magnete.yaml"), {}) or {}
    items = []
    for m in data.get("items", []):
        w, h = image_size(m.get("img", ""))
        m["w"], m["h"] = w, h
        items.append(m)
    return items, data.get("placeholder_motifs", [])


def load_maerkte():
    data = _load_yaml(os.path.join(CONTENT_DIR, "maerkte.yaml"), {}) or {}
    return data.get("items", [])


def load_blog_posts():
    posts = []
    for path in sorted(glob.glob(os.path.join(CONTENT_DIR, "blog", "*.md"))):
        slug = os.path.splitext(os.path.basename(path))[0]
        raw = open(path, encoding="utf-8").read()
        if raw.startswith("---"):
            _, fm_raw, body_raw = raw.split("---", 2)
            fm = yaml.safe_load(fm_raw) or {}
        else:
            fm, body_raw = {}, raw
        posts.append({
            "slug": slug,
            "title": fm.get("title", slug),
            "date": str(fm.get("date", "")),
            "type": fm.get("type", ""),
            "teaser": fm.get("teaser", ""),
            "body_html": md.markdown(body_raw.strip()),
        })
    posts.sort(key=lambda p: p["date"])
    return posts
