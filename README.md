# Caviar Modern

A standalone modern dark theme for BroadcasTheNet. Flat, card-based, steel-blue
accent, streaming-service energy. Pairs with the *BTN Highlighter* userscript
for colored format tags (works fine without it too).

## Files

- **`caviar-modern.css`** — the deploy build. Plain CSS, loaded directly by the
  site via *Settings → External CSS*. This is the file the site consumes.
- **`Caviar Modern.user.css`** — the source of truth, as a Stylus userstyle
  (handy for live-testing changes before deploying).
- **`build-deploy.py`** — regenerates `caviar-modern.css` from the source
  (strips the Stylus-only `@-moz-document` wrapper and metadata).

## Updating the theme

```
python3 build-deploy.py
git add -A
git commit -m "describe the change"
git push
```

GitHub Pages serves the new CSS a minute or two after the push.
