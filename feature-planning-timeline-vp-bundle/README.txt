1-800-Radiator — Feature planning timeline (local bundle)
========================================================

What’s included
-----------------
- feature-planning-timeline-infographic.html — open this in a web browser
- elevate-brand-refresh-vert-light-transparent.png — logo (must stay next to the HTML)
- black-lines-1.png — background texture (must stay next to the HTML)

Keep all three items in the same folder.


How to run it (pick one)
------------------------
A) Easiest: double-click `feature-planning-timeline-infographic.html` to open it in your default browser.

B) macOS: Right-click the HTML file → Open With → Chrome (or Safari, Edge).

C) From Terminal (macOS), in this folder:
     open feature-planning-timeline-infographic.html


Internet
--------
The page loads Sansation and Titillium fonts from Google Fonts the first time. An internet connection is required for those fonts; if you’re offline, the page still works using fallback system fonts.

Optional: local web server (only if something looks wrong when opening the file directly)
----------------------------------------------------------------------------------------
From Terminal, in this folder:
     python3 -m http.server 8080
Then visit: http://localhost:8080/feature-planning-timeline-infographic.html


URL options (bookmark or share)
--------------------------------
You can append a sort preset to the file path when using a local server, for example:
     ?sort=phase
     ?sort=group

Examples:
     http://localhost:8080/feature-planning-timeline-infographic.html?sort=phase

When opening the file directly (file://), query strings work in the address bar after the path to the .html file.

Short aliases: ?sort=p (phase), ?sort=g (group). You can also use sortBy= instead of sort=.


Questions
---------
Source data is embedded in the HTML. The “Sheet data as of” line near the title is when the planning sheet was last captured into this file.

**If you need to confirm you have the latest:** click **Open in Google Sheets** on the page and compare the **Last Updated** column in the sheet to the “Sheet data as of” date. If the sheet is newer, ask whoever sent you this package (or your Elevate contact) for an updated HTML file.

**Check live sheet** sometimes works in the browser; if it doesn’t, use the Google Sheets link — you don’t need to run anything on your computer.

*(Technical staff: to regenerate the HTML from the sheet, run `python3 scripts/merge_feature_sheet.py` in the folder that contains this README and the `scripts` folder.)*
