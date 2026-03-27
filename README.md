# Roadmaps (Elevate infographics)

Static HTML infographics and small tools for client roadmaps and planning. Source lives in GitHub; the feature planning timeline is also published with **GitHub Pages**.

## Folder layout

| Folder | Client |
|--------|--------|
| `1-800-Radiator/` | 1-800-Radiator (feature timeline, roadmap, merge script, VP bundle) |
| `Take 5/` | Take 5 |
| `Maaco/` | Maaco (placeholder) |
| `AGN/` | AGN (placeholder) |
| `Meineke/` | Meineke (placeholder) |
| `shared/` | Common assets (Elevate logos, `black-lines` texture) used by multiple pages |

Other reference files (e.g. PDFs, `.docx`, mountain artwork) may remain at the **repository root**.

## Feature planning timeline

- **Source file:** `1-800-Radiator/feature-planning-timeline-infographic.html`
- **Public site (after Pages is enabled):** `https://elevatelino.github.io/roadmaps/1-800-Radiator/feature-planning-timeline-infographic.html`
- **Assets:** shared textures and logo live in `shared/`; paths in the HTML use `../shared/…`

**Check live sheet** on the page only *compares* the live Google Sheet export to the data already embedded in the HTML. It does not update the site.

### Refreshing embedded data from Google Sheets

When the sheet changes and you need the site (and “Sheet data as of”) to match:

1. From the **repository root**:

   ```bash
   python3 1-800-Radiator/scripts/merge_feature_sheet.py
   ```

   That downloads the Features tab CSV and rewrites the `<script id="data">` JSON inside `1-800-Radiator/feature-planning-timeline-infographic.html`.

2. Optional: keep the VP bundle copy in sync:

   ```bash
   python3 1-800-Radiator/feature-planning-timeline-vp-bundle/scripts/merge_feature_sheet.py
   ```

3. Commit and push to `main`:

   ```bash
   git add 1-800-Radiator/feature-planning-timeline-infographic.html 1-800-Radiator/feature-planning-timeline-vp-bundle/feature-planning-timeline-infographic.html
   git commit -m "Refresh sheet snapshot"
   git push origin main
   ```

GitHub Pages will redeploy in a minute or two; hard-refresh the infographic URL if needed.

**Requirements:** Python 3 (stdlib only; no pip install). Network access to Google’s public CSV export URL.

## VP bundle folder

`1-800-Radiator/feature-planning-timeline-vp-bundle/` is a self-contained copy for sharing (see `README.txt` inside that folder). It keeps its own copies of logos/textures next to the HTML.

## Other files

The repo may also contain other infographics (e.g. `Take 5/`, `cycle-diagram.html` at root) and reference assets; they are not all wired to the merge script above.
