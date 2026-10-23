# -*- coding: utf-8 -*-
"""Builds the whole site, then writes sitemap.xml and robots.txt.

    cd tools && python build.py
"""

import datetime
import glob
import os

import build_core
import build_services
import build_blog
from common import BASE, ROOT, write

PAGES = build_core.BUILT + build_services.BUILT + build_blog.BUILT

PRIORITY = {"index.html": "1.0", "services.html": "0.9", "pricing.html": "0.9",
            "contact.html": "0.9", "blog/index.html": "0.7",
            "privacy.html": "0.3", "terms.html": "0.3"}
today = datetime.date.today().isoformat()


def priority(page):
    if page in PRIORITY:
        return PRIORITY[page]
    if page.startswith("blog/"):
        return "0.6"
    return "0.8"


urls = []
for page in PAGES:
    loc = BASE + "/" + ("" if page == "index.html" else page)
    urls.append("  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n"
                "    <changefreq>monthly</changefreq>\n    <priority>%s</priority>\n  </url>"
                % (loc, today, priority(page)))

write("sitemap.xml",
      '<?xml version="1.0" encoding="UTF-8"?>\n'
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
      + "\n".join(urls) + "\n</urlset>\n")

write("robots.txt",
      "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASE)

# GitHub Pages serves 404.html for unknown paths.
write(".nojekyll", "")

print("built %d pages + sitemap.xml + robots.txt" % len(PAGES))
for p in sorted(PAGES):
    print("  ", p)
