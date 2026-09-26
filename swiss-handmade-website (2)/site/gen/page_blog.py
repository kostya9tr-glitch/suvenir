# -*- coding: utf-8 -*-
from common import page, breadcrumbs, BRAND
from content_loader import load_blog_posts

POSTS = load_blog_posts()


def build_index():
    title = f"Blog — Handwerk, Märkte & Geschenkideen | {BRAND}"
    desc = "Blog rund um handgemachte Gipsfiguren, Magnete und Kerzen: Herstellung, Marktkalender und Geschenkideen aus dem Kanton Bern."
    crumbs_html, crumbs_ld = breadcrumbs([("Startseite", "/"), ("Blog", None)])
    cards = []
    for post in POSTS:
        cards.append(f"""<article class="blog-card">
            <div class="thumb"><span class="ph">{post['type']}</span></div>
            <div class="b-body">
              <span class="tag">{post['type']}</span>
              <h3><a href="/blog/{post['slug']}/">{post['title']}</a></h3>
              <time datetime="{post['date']}">{post['date']}</time>
              <p>{post['teaser']}</p>
            </div>
          </article>""")
    body = f"""
    {crumbs_html}
    <header class="page-hero container">
      <p class="kicker">Blog</p>
      <h1>Handwerk, Märkte &amp; Geschenkideen</h1>
      <p class="lead">Einblicke in unsere Werkstatt, Markttermine und saisonale Geschenkideen — alles rund um handgemachte Gipsfiguren, Magnete und Kerzen.</p>
    </header>
    <section class="section">
      <div class="container">
        <div class="blog-grid">
          {"".join(cards)}
        </div>
      </div>
    </section>
    """
    return page(title, desc, "/blog/", "/blog/", body, extra_jsonld=crumbs_ld)


def build_post(post, related):
    title = f"{post['title']} | {BRAND} Blog"
    desc = post['teaser']
    crumbs_html, crumbs_ld = breadcrumbs([("Startseite", "/"), ("Blog", "/blog/"), (post['title'], None)])
    related_html = "\n          ".join(
        f'<article class="blog-card"><div class="thumb"><span class="ph">{r["type"]}</span></div>'
        f'<div class="b-body"><span class="tag">{r["type"]}</span><h3><a href="/blog/{r["slug"]}/">{r["title"]}</a></h3>'
        f'<time datetime="{r["date"]}">{r["date"]}</time></div></article>'
        for r in related
    )
    article_ld = f"""<script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "{post['title']}",
    "datePublished": "{post['date']}",
    "author": {{"@type":"Organization","name":"{BRAND}"}},
    "publisher": {{"@type":"Organization","name":"{BRAND}"}}
  }}
  </script>"""
    body = f"""
    {crumbs_html}
    <section class="section" style="padding-top:24px;">
      <div class="container article">
        <span class="tag" style="color:var(--moss-dark); font-weight:700; font-size:.8rem;">{post['type']}</span>
        <h1>{post['title']}</h1>
        <p class="meta">Veröffentlicht am <time datetime="{post['date']}">{post['date']}</time></p>
        {post['body_html']}
      </div>
    </section>
    <section class="section section-alt">
      <div class="container">
        <h2 class="related-heading" style="margin-top:0;">Das könnte Sie auch interessieren</h2>
        <div class="blog-grid">
          {related_html}
        </div>
      </div>
    </section>
    """
    return page(title, desc, f"/blog/{post['slug']}/", "/blog/", body, extra_jsonld=crumbs_ld + article_ld)


def build_all():
    pages = {"blog/index.html": build_index()}
    for i, post in enumerate(POSTS):
        related = [POSTS[j] for j in range(len(POSTS)) if j != i][:3]
        pages[f"blog/{post['slug']}/index.html"] = build_post(post, related)
    return pages
