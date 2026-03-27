# Roadmaps (Elevate infographics)

Static HTML infographics and small tools for client roadmaps and planning. Source lives in GitHub; the feature planning timeline is also published with **GitHub Pages**.

## Feature planning timeline

- **Source file:** `feature-planning-timeline-infographic.html` (repo root)
- **Public site (after Pages is enabled):** `https://elevatelino.github.io/roadmaps/feature-planning-timeline-infographic.html`
- **Assets:** keep `elevate-brand-refresh-vert-light-transparent.png` and `black-lines-1.png` next to the HTML (same folder)

**Check live sheet** on the page only *compares* the live Google Sheet export to the data already embedded in the HTML. It does not update the site.

### Refreshing embedded data from Google Sheets

When the sheet changes and you need the site (and “Sheet data as of”) to match:

1. From the **repository root** (this folder):

   ```bash
   python3 scripts/merge_feature_sheet.py
   ```

   That downloads the Features tab CSV and rewrites the `<script id="data">` JSON inside `feature-planning-timeline-infographic.html`.

2. Optional: keep the VP bundle copy in sync:

   ```bash
   python3 feature-planning-timeline-vp-bundle/scripts/merge_feature_sheet.py
   ```

3. Commit and push to `main`:

   ```bash
   git add feature-planning-timeline-infographic.html feature-planning-timeline-vp-bundle/feature-planning-timeline-infographic.html
   git commit -m "Refresh sheet snapshot"
   git push origin main
   ```

GitHub Pages will redeploy in a minute or two; hard-refresh the infographic URL if needed.

**Requirements:** Python 3 (stdlib only; no pip install). Network access to Google’s public CSV export URL.

## VP bundle folder

`feature-planning-timeline-vp-bundle/` is a self-contained copy for sharing (see `README.txt` inside that folder). The merge script path inside the bundle targets the HTML file next to it.

## Other files

The repo may also contain other infographics (e.g. `1800-radiator-feature-roadmap-infographic.html`, `cycle-diagram.html`) and reference assets; they are not all wired to the merge script above.
