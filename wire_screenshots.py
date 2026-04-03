#!/usr/bin/env python3
"""Wire extracted screenshots into IFP workshop HTML pages."""
import os, re

DOCS = "/home/gstoa/.openclaw/workspace/projects/work/workshops/ifp-workshop/docs"
IMG_DIR = "/home/gstoa/.openclaw/workspace/projects/work/workshops/ifp-workshop/img"

# Map page → list of (screenshot_placeholder_keyword, image_filename)
# Images are referenced relative to docs/ as ../img/filename.jpg
WIRING = {
    "headcount.html": [
        ("Job Metadata page", "headcount-2.jpg"),
        ("HC Planning page", "headcount-4.jpg"),
        ("HC Job Grade Pay Bands", "headcount-3.jpg"),
    ],
    "opex.html": [
        ("OpEx planning page", "operating-expenses-2.jpg"),
    ],
    "revenue-cogs.html": [
        ("Revenue & COGS planning page", "revenue-cogs-planning-2.jpg"),
    ],
    "capex.html": [
        ("CapEx New Asset Purchases page", "capex-2.jpg"),
    ],
    "balance-sheet.html": [
        ("BS Account Planning page", "balance-sheet-planning-2.jpg"),
    ],
    "top-down.html": [
        ("Top-Down Planning page", "top-down-planning-2.jpg"),
    ],
    "reporting.html": [
        ("Reporting page", "reporting-analysis-2.jpg"),
        ("Management Reporting Sample", "reporting-analysis-4.jpg"),
    ],
    "ado-overview.html": [
        ("ADO architecture diagram", "back-end-information-2.jpg"),
        ("ADO transformation view", "back-end-information-1.jpg"),
    ],
    "ifp-overview.html": [
        ("IFP suite", "introduction-and-navigation-1.jpg"),
    ],
    "model-architecture.html": [
        ("IFP v2.0 model architecture diagram", "back-end-information-1.jpg"),
    ],
    "app-framework.html": [
        ("Application Framework", "introduction-and-navigation-2.jpg"),
    ],
    "inter-module-flows.html": [
        ("IFP inter-module flow diagram", "back-end-information-2.jpg"),
    ],
    "currency-translation.html": [
        ("Currency triangulation diagram", "reporting-analysis-3.jpg"),
    ],
    "config-walkthrough.html": [
        ("Application Framework wizard", "back-end-information-1.jpg"),
        ("Hierarchy Configuration screen", "introduction-and-navigation-2.jpg"),
    ],
    "data-load-ado.html": [
        ("Admin model — Source to Planning", "back-end-information-2.jpg"),
        ("ADO transformation view", "back-end-information-1.jpg"),
    ],
}

def wire_page(filename, wiring_list):
    path = os.path.join(DOCS, filename)
    if not os.path.exists(path):
        print(f"  SKIP (not found): {filename}")
        return

    with open(path, 'r') as f:
        content = f.read()

    original = content
    for keyword, imgfile in wiring_list:
        # Find the screenshot placeholder div for this keyword
        pattern = r'<div class="screenshot-placeholder"><em>📸 Screenshot: ([^<]*' + re.escape(keyword.split()[0]) + r'[^<]*)</em></div>'
        replacement = f'<figure class="screenshot-figure"><img src="../img/{imgfile}" alt="\\1" class="screenshot-img" loading="lazy"><figcaption>\\1</figcaption></figure>'
        new_content = re.sub(pattern, replacement, content, count=1, flags=re.IGNORECASE)
        if new_content != content:
            content = new_content
            print(f"  ✅ Wired: {keyword[:40]} → {imgfile}")
        else:
            print(f"  ⚠️  No match for: {keyword[:40]} in {filename}")

    if content != original:
        with open(path, 'w') as f:
            f.write(content)

for page, wirings in WIRING.items():
    print(f"\n{page}")
    wire_page(page, wirings)

# Add screenshot CSS to stylesheet
css_addition = """
/* Screenshot figures */
.screenshot-figure {
  margin: 1rem 0;
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow-md);
}

.screenshot-img {
  width: 100%;
  display: block;
}

.screenshot-figure figcaption {
  padding: 0.4rem 0.75rem;
  font-size: 0.8rem;
  color: var(--color-text-muted);
  background: #f8fafc;
  border-top: 1px solid var(--color-border);
  font-style: italic;
}
"""

css_path = "/home/gstoa/.openclaw/workspace/projects/work/workshops/ifp-workshop/css/style.css"
with open(css_path, 'a') as f:
    f.write(css_addition)
print("\n✅ Screenshot CSS added")
print("\nDone.")
