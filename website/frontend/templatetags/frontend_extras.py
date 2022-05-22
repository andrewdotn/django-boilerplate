from functools import cache
from html import parser
from html.parser import HTMLParser
from urllib.parse import urljoin

from django import template
from django.conf import settings
from django.contrib import staticfiles
from django.utils import safestring
from django.utils.safestring import mark_safe

register = template.Library()


class CssAndJsParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.css_links = []
        self.js_links = []

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            for (k, v) in attrs:
                if k == "src":
                    self.js_links.append(v)
        elif tag == "link":
            attr_dict = dict(attrs)

            if attr_dict.get("rel") == "stylesheet":
                self.css_links.append(attr_dict["href"])


# Could also check timestamps to determine if should re-read
@cache
def determine_build_asset_names():
    index_html = (settings.FRONTEND_DIST_DIR / "index.html").read_text()

    parser = CssAndJsParser()
    parser.feed(index_html)

    return {"css": parser.css_links, "js": parser.js_links}


@register.simple_tag()
def frontend():
    if settings.DEBUG:
        prefix = "http://localhost:3000"

        return mark_safe(
            f"""
            <script type="module" src="{prefix}/@vite/client"></script>
            <link rel="stylesheet" href="{prefix}/style.scss">
            <script async type="module" src="{prefix}/index.ts"></script>
            """
        )

    prefix_url = "/static/dist"

    def prefix(link):
        if link.startswith("/"):
            return prefix_url + link
        return f"{prefix_url}/link"

    assets = determine_build_asset_names()

    ret = []
    for css_link in assets["css"]:
        ret.append(f'<link rel="stylesheet" href="{prefix(css_link)}">')
    for js_link in assets["js"]:
        ret.append(f'<script async type="module" src="{prefix(js_link)}"></script>')
    return mark_safe("\n".join(ret))
