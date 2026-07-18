#!/usr/bin/env python3
"""Rebuild caviar-modern.css (the plain-CSS deploy build BTN loads directly)
from the Stylus source "Caviar Modern.user.css". Run after any edit:

    python3 build-deploy.py
    git add -A && git commit -m "update theme" && git push
"""
import re, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
css = open("Caviar Modern.user.css", encoding="utf-8").read()
m = re.search(r'@-moz-document[^{]*\{', css)
head = css[:m.start()]
body = css[m.end():]
body = body[:body.rfind("}")]
head = re.sub(r'/\* ==UserStyle==.*?==/UserStyle== \*/\s*', '', head, flags=re.S)
banner = """/* Caviar Modern — a standalone dark theme for BroadcasTheNet.
   Deploy build (plain CSS for the site's External CSS setting).
   GENERATED from "Caviar Modern.user.css" — edit that file, then rebuild
   with:  python3 build-deploy.py
*/
"""
open("caviar-modern.css", "w").write(banner + head + body.strip() + "\n")
print("built caviar-modern.css")
