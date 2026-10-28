# BOffice Landing Pages

Static landing pages for [BOffice](https://boffice.co.id) (PT. Boffice Global Ventura) — All in One Business Solutions.

- `index.html` — main services (Virtual Office, Workspace, Legal, Finance & Tax, Social Media teaser)
- `sosmed.html` — Social Media Management + Automation (+ bonuses)

Languages: Indonesian / English / 中文 (auto from browser, switchable).

## Local preview

```bash
python3 -m http.server 8765
```

Open http://localhost:8765/ and http://localhost:8765/sosmed.html

## Edit copy

Edit `src/strings.py` then run:

```bash
cd src && python3 build.py
```

## Live

Published via GitHub Pages from the `main` branch root.
