#!/usr/bin/env python3
"""
Rebuild nav sidebar across all IFP workshop HTML pages.
Run after adding new pages or changing nav structure.
Usage: python3 rebuild_nav.py
"""
import os, re

DOCS = os.path.join(os.path.dirname(__file__), "docs")

NAV_HTML = """  <nav class="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-title">IFP v2.0 Workshop</div>
    </div>
    <ul class="nav-list">
      <li class="nav-section-title">Getting Started</li>
      <li><a class="nav-link ACTIVE_overview" href="./overview.html">Workshop Overview</a></li>
      <li><a class="nav-link ACTIVE_case-study" href="./case-study.html">Case Study: FictoCorp</a></li>
      <li><a class="nav-link ACTIVE_ifp-overview" href="./ifp-overview.html">IFP Suite Overview</a></li>
      <li><a class="nav-link ACTIVE_anaplan-way" href="./anaplan-way.html">Anaplan Way for Apps</a></li>
      <li class="nav-section-title">Module 1 — Platform Foundations</li>
      <li><a class="nav-link ACTIVE_app-framework" href="./app-framework.html">Application Framework</a></li>
      <li><a class="nav-link ACTIVE_ado-overview" href="./ado-overview.html">Anaplan Data Orchestrator</a></li>
      <li><a class="nav-link ACTIVE_model-architecture" href="./model-architecture.html">Model Architecture</a></li>
      <li class="nav-section-title">Module 2 — Configuration Workshop</li>
      <li><a class="nav-link ACTIVE_config-walkthrough" href="./config-walkthrough.html">App Framework Walkthrough</a></li>
      <li><a class="nav-link ACTIVE_lab-a" href="./lab-a.html">Lab A: Configure FictoCorp</a></li>
      <li><a class="nav-link ACTIVE_post-generation" href="./post-generation.html">Post-Generation Checklist</a></li>
      <li><a class="nav-link ACTIVE_data-load-ado" href="./data-load-ado.html">Data Load via ADO</a></li>
      <li><a class="nav-link ACTIVE_lab-b" href="./lab-b.html">Lab B: Full 3-Statement</a></li>
      <li class="nav-section-title">Module 3 — Module Walkthroughs</li>
      <li><a class="nav-link ACTIVE_revenue-cogs" href="./revenue-cogs.html">Revenue &amp; COGS Planning</a></li>
      <li><a class="nav-link ACTIVE_opex" href="./opex.html">Operating Expenses</a></li>
      <li><a class="nav-link ACTIVE_headcount" href="./headcount.html">Headcount Planning</a></li>
      <li><a class="nav-link ACTIVE_capex" href="./capex.html">CapEx Planning</a></li>
      <li><a class="nav-link ACTIVE_balance-sheet" href="./balance-sheet.html">Balance Sheet &amp; Cash Flow</a></li>
      <li><a class="nav-link ACTIVE_top-down" href="./top-down.html">Top-Down Planning</a></li>
      <li><a class="nav-link ACTIVE_reporting" href="./reporting.html">Reporting &amp; Analysis</a></li>
      <li class="nav-section-title">Module 4 — Admin &amp; Extensions</li>
      <li><a class="nav-link ACTIVE_admin-runbook" href="./admin-runbook.html">Admin Runbook</a></li>
      <li><a class="nav-link ACTIVE_currency-translation" href="./currency-translation.html">Currency Translation</a></li>
      <li><a class="nav-link ACTIVE_extensions" href="./extensions.html">Common Extensions</a></li>
      <li class="nav-section-title">Reference</li>
      <li><a class="nav-link ACTIVE_inter-module-flows" href="./inter-module-flows.html">Inter-Module Data Flows</a></li>
      <li><a class="nav-link ACTIVE_whats-coming" href="./whats-coming.html">What's Coming</a></li>
      <li><a class="nav-link ACTIVE_qanda" href="./qanda.html">Q&amp;A from Sessions</a></li>
      <li><a class="nav-link ACTIVE_resources" href="./resources.html">Resources &amp; Downloads</a></li>
      <li><a class="nav-link ACTIVE_glossary" href="./glossary.html">Glossary</a></li>
      <li><a class="nav-link ACTIVE_facilitator" href="./facilitator.html">Facilitator Guide</a></li>
    </ul>
  </nav>"""

updated = 0
for fname in sorted(os.listdir(DOCS)):
    if not fname.endswith(".html"):
        continue
    slug = fname.replace(".html", "")
    nav = NAV_HTML.replace(f"ACTIVE_{slug}", f"ACTIVE_{slug} active")
    nav = re.sub(r" ACTIVE_[\w-]+", "", nav)
    
    fpath = os.path.join(DOCS, fname)
    with open(fpath, "r") as f:
        content = f.read()
    
    new_content = re.sub(r"<nav class=\"sidebar\".*?</nav>", nav, content, flags=re.DOTALL)
    if new_content != content:
        with open(fpath, "w") as f:
            f.write(new_content)
        print(f"  Updated nav: {fname}")
        updated += 1
    else:
        print(f"  No change: {fname}")

print(f"\nDone. Updated {updated} files.")
