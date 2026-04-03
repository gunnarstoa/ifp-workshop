#!/usr/bin/env python3
"""
IFP Workshop v2.1 Retrofit Script
Executes all 5 priorities in order.
"""

import os
import re

DOCS = "/home/gstoa/.openclaw/workspace/projects/work/workshops/ifp-workshop/docs"

# =============================================================================
# NAV BLOCK — the canonical nav used across ALL pages
# =============================================================================

def nav_block(active_href):
    """Return the full sidebar nav HTML with the correct active link."""
    links = [
        ("nav-section-title", "Getting Started"),
        ("nav-link", "./overview.html", "Workshop Overview"),
        ("nav-link", "./case-study.html", "Case Study: FictoCorp"),
        ("nav-link", "./ifp-overview.html", "IFP Suite Overview"),
        ("nav-link", "./anaplan-way.html", "Anaplan Way for Apps"),
        ("nav-section-title", "Module 1 — Platform Foundations"),
        ("nav-link", "./app-framework.html", "Application Framework"),
        ("nav-link", "./ado-overview.html", "Anaplan Data Orchestrator"),
        ("nav-link", "./model-architecture.html", "Model Architecture"),
        ("nav-section-title", "Module 2 — Configuration Workshop"),
        ("nav-link", "./config-walkthrough.html", "App Framework Walkthrough"),
        ("nav-link", "./lab-a.html", "Lab A: Configure FictoCorp"),
        ("nav-link", "./post-generation.html", "Post-Generation Checklist"),
        ("nav-link", "./data-load-ado.html", "Data Load via ADO"),
        ("nav-link", "./lab-b.html", "Lab B: Full 3-Statement"),
        ("nav-section-title", "Module 3 — Module Walkthroughs"),
        ("nav-link", "./revenue-cogs.html", "Revenue &amp; COGS Planning"),
        ("nav-link", "./opex.html", "Operating Expenses"),
        ("nav-link", "./headcount.html", "Headcount Planning"),
        ("nav-link", "./capex.html", "CapEx Planning"),
        ("nav-link", "./balance-sheet.html", "Balance Sheet &amp; Cash Flow"),
        ("nav-link", "./top-down.html", "Top-Down Planning"),
        ("nav-link", "./reporting.html", "Reporting &amp; Analysis"),
        ("nav-section-title", "Module 4 — Admin &amp; Extensions"),
        ("nav-link", "./admin-runbook.html", "Admin Runbook"),
        ("nav-link", "./currency-translation.html", "Currency Translation"),
        ("nav-link", "./extensions.html", "Common Extensions"),
        ("nav-section-title", "Reference"),
        ("nav-link", "./limitations.html", "Known Limitations"),
        ("nav-link", "./presales-demo.html", "Pre-Sales Demo Playbook"),
        ("nav-link", "./inter-module-flows.html", "Inter-Module Data Flows"),
        ("nav-link", "./whats-coming.html", "What&#39;s Coming"),
        ("nav-link", "./qanda.html", "Q&amp;A from Sessions"),
        ("nav-link", "./resources.html", "Resources &amp; Downloads"),
        ("nav-link", "./glossary.html", "Glossary"),
        ("nav-link", "./facilitator.html", "Facilitator Guide"),
    ]
    items = []
    for item in links:
        if item[0] == "nav-section-title":
            items.append(f'        <li class="nav-section-title">{item[1]}</li>')
        else:
            _, href, label = item
            active = ' active' if href == active_href else ''
            items.append(f'        <li><a class="nav-link{active}" href="{href}">{label}</a></li>')
    return "\n".join(items)


def screenshot(src, alt, caption):
    return f'<figure class="screenshot-figure"><img src="../img/{src}" alt="{alt}" class="screenshot-img" loading="lazy"><figcaption>{caption}</figcaption></figure>'


def placeholder(label, desc=""):
    desc_html = f'<div class="ss-desc">{desc}</div>' if desc else ''
    return f'<div class="screenshot-placeholder"><div class="ss-icon">📸</div><div class="ss-label">[SCREENSHOT NEEDED: {label}]</div>{desc_html}</div>'


# =============================================================================
# PRIORITY 1 — Wire screenshots into module walkthrough pages
# =============================================================================

def patch_opex():
    path = os.path.join(DOCS, "opex.html")
    content = open(path).read()
    old = '<figure class="screenshot-figure"><img src="../img/operating-expenses-2.jpg" alt="OpEx Planning page — Prior Run Rate method with growth % input" class="screenshot-img" loading="lazy"><figcaption>OpEx Planning page — Prior Run Rate method with growth % input</figcaption></figure>'
    new = "\n".join([
        screenshot("operating-expenses-1.jpg", "OpEx module — account list with planning method dropdown and current period actuals", "OpEx account list — each GL account shows its assigned planning method and current period actuals for reference"),
        screenshot("operating-expenses-2.jpg", "OpEx Planning page — Prior Run Rate method with growth % input", "Prior Run Rate method — enter growth % and number of periods back; system calculates the forecast automatically"),
        screenshot("operating-expenses-3.jpg", "OpEx Planning — Units x Rate method showing rate and volume inputs per account", "Units x Rate method — separate inputs for volume (e.g. hours) and rate; system multiplies to produce the forecast"),
        screenshot("operating-expenses-4.jpg", "OpEx Line Item Detail page — vendor/functional area breakdown per expense account", "Line Item Detail — enter individual expense items with vendor and functional area tags; summarizes back to the account"),
        screenshot("operating-expenses-5.jpg", "OpEx Allocations page — allocation rule configuration showing source account and target accounts", "Allocations setup — define source account, target accounts, and allocation method; runs after planning is complete"),
    ])
    content = content.replace(old, new)
    open(path, "w").write(content)
    print(f"  [opex.html] {old[:60]}... → 5 screenshots")


def patch_balance_sheet():
    path = os.path.join(DOCS, "balance-sheet.html")
    content = open(path).read()
    old = '<figure class="screenshot-figure"><img src="../img/balance-sheet-planning-2.jpg" alt="BS Account Planning page — showing DSO input for Accounts Receivable" class="screenshot-img" loading="lazy"><figcaption>BS Account Planning page — showing DSO input for Accounts Receivable</figcaption></figure>'
    new = "\n".join([
        screenshot("balance-sheet-planning-1.jpg", "Balance Sheet — FIN BS Manage Cash Offset Accounts mapping screen", "Cash Offset Accounts setup — every BS account must be mapped here; missing entries break the cash flow statement"),
        screenshot("balance-sheet-planning-2.jpg", "BS Account Planning page — showing DSO input for Accounts Receivable", "BS Account Planning — DSO method for Accounts Receivable; system calculates the balance from revenue and days outstanding"),
        screenshot("balance-sheet-planning-3.jpg", "BS Investments sub-schedule — new investment entry with amount, start date, rate, and IS/BS/CF impact preview", "BS Investments sub-schedule — enter investment details and preview the full financial statement impact before saving"),
        screenshot("balance-sheet-planning-4.jpg", "BS Leases sub-schedule — capital and operating lease detail entry", "BS Leases — enter lease term, amount, and type; system calculates ROU asset, liability, and P&amp;L impact automatically"),
        screenshot("balance-sheet-planning-5.jpg", "BS Balancing Routine — balance check showing Assets = Liabilities + Equity with green validation", "Balancing Routine — run after each planning cycle to confirm Assets = Liabilities + Equity; red cells indicate mismatches to investigate"),
    ])
    content = content.replace(old, new)
    open(path, "w").write(content)
    print(f"  [balance-sheet.html] → 5 screenshots")


def patch_capex():
    path = os.path.join(DOCS, "capex.html")
    content = open(path).read()
    old = '<figure class="screenshot-figure"><img src="../img/capex-2.jpg" alt="CapEx – New Asset Purchases page showing asset list with order date, in-service date, depreciation method" class="screenshot-img" loading="lazy"><figcaption>CapEx – New Asset Purchases page showing asset list with order date, in-service date, depreciation method</figcaption></figure>'
    new = "\n".join([
        screenshot("capex-1.jpg", "CapEx module — CE Asset Setup page showing asset categories and configuration", "CE Asset Setup — configure asset categories, useful life defaults, and GL account mappings before entering individual assets"),
        screenshot("capex-2.jpg", "CapEx – New Asset Purchases page showing asset list with order date, in-service date, depreciation method", "New Asset Purchases — each asset entered with order date, in-service date, cost, and depreciation method; system calculates monthly depreciation automatically"),
        screenshot("capex-3.jpg", "CapEx Disposals page — asset retirement entries with gain/loss calculation", "Asset Disposals — record retirement date and proceeds; system calculates book value at disposal date and gain/loss automatically"),
        screenshot("capex-4.jpg", "CapEx P&L Impact summary — depreciation by asset category rolling into the Income Statement", "P&amp;L Impact view — depreciation flows through to OpEx accounts in the FP model; verify the IS mapping is correct for each asset category"),
    ])
    content = content.replace(old, new)
    open(path, "w").write(content)
    print(f"  [capex.html] → 4 screenshots")


def patch_revenue_cogs():
    path = os.path.join(DOCS, "revenue-cogs.html")
    content = open(path).read()
    old = '<figure class="screenshot-figure"><img src="../img/revenue-cogs-planning-2.jpg" alt="Revenue & COGS Planning page — showing Units x Rate method inputs" class="screenshot-img" loading="lazy"><figcaption>Revenue & COGS Planning page — showing Units x Rate method inputs</figcaption></figure>'
    new = "\n".join([
        screenshot("revenue-cogs-planning-1.jpg", "Revenue & COGS — account selector showing product and customer dimension filters", "Revenue account selector — filter by product, customer, and entity; navigate between accounts using the dropdown or page grid"),
        screenshot("revenue-cogs-planning-2.jpg", "Revenue & COGS Planning page — showing Units x Rate method inputs", "Units x Rate method — enter volume (units sold, subscriptions, or hours) and rate separately; system calculates revenue and auto-applies the COGS margin"),
        screenshot("revenue-cogs-planning-3.jpg", "Revenue & COGS — Prior Run Rate method with growth percentage and adjustment inputs", "Prior Run Rate method — pulls the prior period actuals and applies the entered growth %; use the $ Adjustment for known one-time items"),
        screenshot("revenue-cogs-planning-4.jpg", "Revenue Summary page — total revenue and gross margin by product line with variance vs. prior year", "Revenue Summary — roll-up view across all product lines showing revenue, COGS, and gross margin; compare against prior year actuals or AOP"),
    ])
    content = content.replace(old, new)
    open(path, "w").write(content)
    print(f"  [revenue-cogs.html] → 4 screenshots")


def patch_top_down():
    path = os.path.join(DOCS, "top-down.html")
    content = open(path).read()
    old = '<figure class="screenshot-figure"><img src="../img/top-down-planning-2.jpg" alt="Top-Down Planning page — showing revenue and gross profit target inputs" class="screenshot-img" loading="lazy"><figcaption>Top-Down Planning page — showing revenue and gross profit target inputs</figcaption></figure>'
    new = "\n".join([
        screenshot("top-down-planning-1.jpg", "Top-Down Planning — target entry screen showing dimension selector at entity/L2 level", "Top-Down target entry — targets entered at L2 entity level for each metric; system does NOT auto-disaggregate to lower levels (manual distribution required)"),
        screenshot("top-down-planning-2.jpg", "Top-Down Planning page — showing revenue and gross profit target inputs", "TD Planning page — enter revenue, gross profit, OpEx, and FTE targets; each metric has its own row with monthly columns"),
        screenshot("top-down-planning-3.jpg", "Top-Down Summary — targets vs. bottom-up side-by-side with variance row at entity level", "TD Summary — executive view comparing submitted targets against bottom-up plan; red variance rows highlight gaps that require discussion"),
    ])
    content = content.replace(old, new)
    open(path, "w").write(content)
    print(f"  [top-down.html] → 3 screenshots")


def patch_reporting():
    path = os.path.join(DOCS, "reporting.html")
    content = open(path).read()
    old = '<figure class="screenshot-figure"><img src="../img/reporting-analysis-2.jpg" alt="Reporting & Analysis — Income Statement Report with suppression enabled" class="screenshot-img" loading="lazy"><figcaption>Reporting & Analysis — Income Statement Report with suppression enabled</figcaption></figure>'
    new = "\n".join([
        screenshot("reporting-analysis-1.jpg", "Reporting & Analysis — report selector showing IS, BS, CF, and Variance report options", "Report landing page — all available reports listed; select report type and set version/period context before opening"),
        screenshot("reporting-analysis-2.jpg", "Reporting & Analysis — Income Statement Report with suppression enabled", "IS Report — zero-suppression enabled hides empty rows; version switcher in top bar lets you toggle between AOP, forecast, and actuals"),
    ])

    old2 = '<figure class="screenshot-figure"><img src="../img/reporting-analysis-4.jpg" alt="Management Reporting Sample — executive summary with P&L and dynamic commentary" class="screenshot-img" loading="lazy"><figcaption>Management Reporting Sample — executive summary with P&L and dynamic commentary</figcaption></figure>'
    new2 = "\n".join([
        screenshot("reporting-analysis-3.jpg", "IS Variance Analysis — two-version comparison with absolute and percentage variance columns", "IS Variance Analysis — select any two versions to compare; absolute and % variance calculated automatically; sort by largest variance to prioritize review"),
        screenshot("reporting-analysis-4.jpg", "Management Reporting Sample — executive summary with P&L and dynamic commentary", "Management Reporting pack — pre-built executive summary page with P&amp;L, cash position, and commentary fields; ready to export as PDF"),
        screenshot("reporting-analysis-5.jpg", "Statistical Analysis page — trend lines and regression analysis for revenue forecasting", "Statistical Analysis — built-in trend and regression tools for forward-looking revenue analysis; feeds directly into the forecast model"),
    ])
    content = content.replace(old, new).replace(old2, new2)
    open(path, "w").write(content)
    print(f"  [reporting.html] → 5 screenshots")


def patch_headcount():
    path = os.path.join(DOCS, "headcount.html")
    content = open(path).read()
    old2 = '<figure class="screenshot-figure"><img src="../img/headcount-2.jpg" alt="HC – Job Metadata page showing job list with grade, employment type, active status" class="screenshot-img" loading="lazy"><figcaption>HC – Job Metadata page showing job list with grade, employment type, active status</figcaption></figure>'
    new2 = "\n".join([
        screenshot("headcount-1.jpg", "Headcount module — HC Admin setup screen showing structure tabs: Jobs, Pay Bands, Benefits, Payroll Attributes", "HC Admin landing — four setup tabs must be completed in sequence before any planning; Jobs first, then Pay Bands, then Benefits, then Payroll Attributes"),
        screenshot("headcount-2.jpg", "HC – Job Metadata page showing job list with grade, employment type, active status", "HC Job Metadata — each job record has a grade, employment type (FTE/contractor), and active flag; inactive jobs are hidden from planning pages"),
    ])
    old5 = '<figure class="screenshot-figure"><img src="../img/headcount-5.jpg"'
    # headcount-5 and headcount-6 need to be added after headcount-4
    old4 = '<figure class="screenshot-figure"><img src="../img/headcount-4.jpg" alt="HC – Planning page showing hires, exits, and transfers by job per department" class="screenshot-img" loading="lazy"><figcaption>HC – Planning page showing hires, exits, and transfers by job per department</figcaption></figure>'
    new4 = "\n".join([
        screenshot("headcount-4.jpg", "HC – Planning page showing hires, exits, and transfers by job per department", "HC Planning — enter planned hires, exits, and transfers for each job role; system tracks opening and closing headcount position count automatically"),
        screenshot("headcount-5.jpg", "HC – Cost Summary page showing total compensation cost by department rolled into FP model", "HC Cost Summary — total compensation cost (salary + benefits + payroll taxes) by department; runs import to push these costs into the FP model"),
        screenshot("headcount-6.jpg", "HC to FP model sync — FIN Import from HC Model action result confirmation", "HC → FP sync — after running the import action, verify the OpEx accounts tagged 'Planned in Headcount' reflect the latest HC amounts in the FP model"),
    ])
    content = content.replace(old2, new2).replace(old4, new4)
    open(path, "w").write(content)
    print(f"  [headcount.html] → 6 screenshots")


def patch_app_framework():
    """introduction-and-navigation-1.jpg → app-framework.html"""
    path = os.path.join(DOCS, "app-framework.html")
    content = open(path).read()
    old = '<figure class="screenshot-figure"><img src="../img/introduction-and-navigation-2.jpg" alt="IFP v2.0 UX — page navigation structure showing module categories" class="screenshot-img" loading="lazy"><figcaption>IFP v2.0 UX — page navigation structure showing module categories</figcaption></figure>'
    new = "\n".join([
        screenshot("introduction-and-navigation-1.jpg", "IFP Application Framework — Applications URL landing page with available applications listed", "Application Framework entry point — navigate to the Applications URL in your tenant; IFP appears as a deployable application once provisioned"),
        screenshot("introduction-and-navigation-2.jpg", "IFP v2.0 UX — page navigation structure showing module categories", "Generated UX navigation — after generation, the sidebar shows all configured modules; hidden modules do not appear here"),
    ])
    content = content.replace(old, new)
    open(path, "w").write(content)
    print(f"  [app-framework.html] → 2 screenshots (introduction-and-navigation-1 wired)")


# =============================================================================
# PRIORITY 2 — Add screenshot placeholders to text-only Show steps
# =============================================================================

def add_placeholder_to_show(path, after_marker, label, desc):
    """Insert a placeholder div after a specific string in the file."""
    content = open(path).read()
    if '[SCREENSHOT NEEDED' in content and label in content:
        print(f"  [{os.path.basename(path)}] placeholder already present, skipping")
        return
    ph = placeholder(label, desc)
    content = content.replace(after_marker, after_marker + "\n      " + ph)
    open(path, "w").write(content)
    print(f"  [{os.path.basename(path)}] placeholder added")


def patch_ifp_overview_placeholder():
    path = os.path.join(DOCS, "ifp-overview.html")
    content = open(path).read()
    marker = '<h2>What IFP Does</h2>'
    ph = placeholder("IFP landing page — module grid overview showing all 6 planning modules and Reporting & Analysis", "Capture the IFP landing page with all module cards visible — Revenue & COGS, OpEx, Headcount, CapEx, Balance Sheet, Top-Down, and Reporting")
    if '[SCREENSHOT NEEDED' not in content:
        content = content.replace(marker, marker + "\n      " + ph)
    open(path, "w").write(content)
    print("  [ifp-overview.html] placeholder added")


def patch_config_walkthrough_placeholder():
    path = os.path.join(DOCS, "config-walkthrough.html")
    content = open(path).read()
    marker = '<h2>Top-Level Configuration Questions</h2>'
    ph1 = placeholder("Application Framework — top-level question screen showing entity dimension, department, and optional dimensions", "Capture the App Framework question wizard open on the first screen — entity dimension name field and department toggle visible")
    ph2 = placeholder("Application Framework — model-specific questions screen for Financial Planning model", "Capture the FP model-specific questions section — planning scope, revenue/COGS options, currency selection")
    ph3 = placeholder("Application Framework — hierarchy configuration screen showing level count inputs and rename fields", "Capture the Hierarchy Configuration screen — level count fields and rename fields for entity and department hierarchies")
    if '[SCREENSHOT NEEDED' not in content:
        content = content.replace(marker, marker + "\n      " + ph1 + "\n      " + ph2 + "\n      " + ph3)
    open(path, "w").write(content)
    print("  [config-walkthrough.html] 3 placeholders added")


def patch_admin_runbook_placeholder():
    path = os.path.join(DOCS, "admin-runbook.html")
    content = open(path).read()
    marker = '<h2>Monthly Checklist</h2>'
    ph = placeholder("Monthly admin checklist view in Anaplan — Admin model showing current period and time settings", "Capture the Admin model open on Model Settings → Time with the current period field highlighted; show the consistent settings across all 4 models")
    if '[SCREENSHOT NEEDED' not in content:
        content = content.replace(marker, marker + "\n      " + ph)
    open(path, "w").write(content)
    print("  [admin-runbook.html] placeholder added")


def patch_extensions_placeholder():
    path = os.path.join(DOCS, "extensions.html")
    content = open(path).read()
    marker = '<ol>\n        <li><strong>Add to Planning Methods list</strong>'
    ph = placeholder("Custom planning method creation — SYS by Planning Methods module showing new method entry", "Capture the SYS by Planning Methods list module with a new custom method row added — show the code, description, and business area fields")
    if '[SCREENSHOT NEEDED' not in content:
        content = content.replace(marker, ph + "\n      " + marker)
    open(path, "w").write(content)
    print("  [extensions.html] placeholder added")


def patch_post_generation_placeholder():
    path = os.path.join(DOCS, "post-generation.html")
    content = open(path).read()
    marker = '<h2>Required Tasks</h2>'
    ph = placeholder("Freshly generated IFP app — first 4 post-generation checklist items in sequence", "Capture the PAF generation success screen, then the post-generation checklist with Review Logs, Time Settings, Version Alignment, and Spoke Model Mapping tasks visible")
    if '[SCREENSHOT NEEDED' not in content:
        content = content.replace(marker, ph + "\n      " + marker)
    open(path, "w").write(content)
    print("  [post-generation.html] placeholder added")


def patch_anaplan_way_placeholder():
    path = os.path.join(DOCS, "anaplan-way.html")
    content = open(path).read()
    # The placeholder already exists but may not be properly described
    old_ph = '<div class="screenshot-placeholder"><div class="ss-icon">📸</div><div class="ss-label">Anaplan Way for Applications — 6-phase delivery framework</div></div>'
    new_ph = '<div class="screenshot-placeholder"><div class="ss-icon">📸</div><div class="ss-label">[SCREENSHOT NEEDED: Anaplan Way for Applications — 6-phase delivery framework diagram]</div><div class="ss-desc">Capture the official Anaplan Way for Applications slide or diagram showing all 6 phases: Requirements, Configure, Generate, Data Load &amp; Publish, Application Ready, Extend &amp; Expand — with IFP-specific activities noted per phase</div></div>'
    if old_ph in content:
        content = content.replace(old_ph, new_ph)
    open(path, "w").write(content)
    print("  [anaplan-way.html] placeholder properly labeled")


def patch_lab_b_placeholder():
    path = os.path.join(DOCS, "lab-b.html")
    content = open(path).read()
    # Find the Do section and add after it
    marker = '<div class="callout-note"><span class="callout-label">ℹ Starting Point</span>'
    ph1 = placeholder("App Framework full 3-statement config screen — all modules enabled with entity, department, and 3 optional dimensions", "Capture the App Framework wizard with all 3 statement modules enabled (Revenue/COGS, OpEx, Balance Sheet), entity dimension named, department enabled, and all three optional dimensions (Geography, Functional Area, Vendor) selected")
    ph2 = placeholder("Generation success confirmation screen — PAF showing all 4 models generated with green status", "Capture the generation completion screen showing Admin, FP, HC, and CE models all generated successfully with no errors")
    ph3 = placeholder("Resulting model structure — workspace showing all 4 generated models (Admin, FP, HC, CE) in model list", "Capture the Anaplan workspace model list after generation — all 4 IFP models visible with correct naming convention")
    if '[SCREENSHOT NEEDED' not in content:
        content = content.replace(marker, ph1 + "\n      " + ph2 + "\n      " + ph3 + "\n      " + marker)
    open(path, "w").write(content)
    print("  [lab-b.html] 3 placeholders added")


# =============================================================================
# PRIORITY 3A — Build limitations.html
# =============================================================================

def build_limitations():
    active = "./limitations.html"
    nav = nav_block(active)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Known Limitations — IFP v2.1 Workshop</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  <div class="mobile-header">
    <button id="hamburger">☰</button>
    <span>IFP v2.1 Workshop</span>
  </div>

  <nav class="sidebar">
  <div class="sidebar-header">
  <div class="sidebar-title">IFP v2.1 Workshop</div>
  </div>
  <ul class="nav-list">
{nav}
      </ul>
    </nav>

  <main class="main-content">
    <div class="content-header">
      <h1>Known Limitations</h1>
      <p class="subtitle">Hard stops, workarounds, and fix timelines — review before scoping</p>
      <div class="badge-row"><span class="content-badge">Reference</span><span class="content-badge">Pre-Sales</span></div>
    </div>
    <div class="content-body">

      <div class="callout-important"><span class="callout-label">🚨 Scope Review Required</span><p>Review every limitation in this table with the customer before scoping the engagement — not after. Hard-stop limitations (High severity with no workaround) must be resolved before proceeding to a Statement of Work.</p></div>

      <h2>Limitation Reference Table</h2>
      <table>
        <thead><tr><th>Limitation</th><th>Severity</th><th>Workaround</th><th>Fix Timeline</th></tr></thead>
        <tbody>
          <tr><td><strong>BYOK requirement (AWS)</strong> — Some customers require Bring Your Own Key encryption on public cloud. ADO requires AWS and cannot be deployed in private/sovereign environments.</td><td><span style="color:#dc2626;font-weight:600">High</span></td><td>None — ADO is an AWS-native service. Customer must be willing to use AWS-hosted ADO or IFP is not suitable.</td><td>No change planned</td></tr>
          <tr><td><strong>AWS dependency</strong> — Customers who cannot use AWS (public sector, federal, sovereign cloud) cannot use ADO and therefore cannot use IFP v2.0+.</td><td><span style="color:#dc2626;font-weight:600">High</span></td><td>None. This is a hard stop. Do not scope IFP for these customers.</td><td>No change planned</td></tr>
          <tr><td><strong>8-dimension limit on Polaris models</strong> — The Polaris engine enforces a hard limit of 8 dimensions per model. Customers with complex dimensional structures may exceed this.</td><td><span style="color:#dc2626;font-weight:600">High</span></td><td>Reduce dimensions to fit within 8. Entity and Time always count. If customer requires &gt;6 additional dimensions, IFP is not suitable.</td><td>No change planned near term</td></tr>
          <tr><td><strong>Top-Down disaggregation not available</strong> — Executive targets entered at L2 level cannot be automatically disaggregated to lower levels. Users must manually distribute targets.</td><td><span style="color:#f59e0b;font-weight:600">Medium</span></td><td>Manual target distribution at each level. Plan extra configuration and training time for this workflow.</td><td>Planned for future release — no date confirmed</td></tr>
          <tr><td><strong>Finance Analyst / CoPlanner pending GA</strong> — Embedded but not yet fully released. Functionality is visible in the UX but behavior may change before GA.</td><td><span style="color:#f59e0b;font-weight:600">Medium</span></td><td>Do not demo or scope Finance Analyst / CoPlanner features until GA is confirmed. Do not include in SOW scope.</td><td>GA planned — confirm current status with Apps team</td></tr>
          <tr><td><strong>CapEx entity-level only</strong> — Capital expense planning is at the entity level only. No employee-level or project-level CapEx planning is supported.</td><td><span style="color:#f59e0b;font-weight:600">Medium</span></td><td>Use GL-level OpEx planning for project-level CapEx tracking. Dedicated CE model handles asset-level detail at entity only.</td><td>No change planned</td></tr>
          <tr><td><strong>No employee-level headcount</strong> — HC planning is job-role based, not employee-based. Individual employee records require OWP integration.</td><td><span style="color:#f59e0b;font-weight:600">Medium</span></td><td>Scope OWP alongside IFP for employee-level detail. IFP HC provides job/grade-level planning which satisfies most FP&amp;A use cases.</td><td>By design — use OWP for employee-level</td></tr>
          <tr><td><strong>5 ADO links broken out of box</strong> — Five known ADO pipeline links are missing or broken after generation: Vendor Hierarchy (FP), and SYS by J2/J3/J4 Job + Job Grade (HC).</td><td><span style="color:#f59e0b;font-weight:600">Medium</span></td><td>Create these links manually using the ADO manual setup steps in the Configuration Guide. Budget 30–60 minutes for this task during post-generation.</td><td>Fix expected in future PAF release</td></tr>
          <tr><td><strong>Basic allocations only</strong> — OpEx allocations support simple percentage-based or amount-based rules. Waterfall and reciprocal allocation methods are not available.</td><td><span style="color:#6b7280;font-weight:600">Low</span></td><td>Use manual workarounds for complex cost allocation. Scope custom development if waterfall or reciprocal allocations are required.</td><td>No timeline</td></tr>
          <tr><td><strong>End-user import templates removed in v2.0</strong> — The Excel-based data entry templates from v1.x are not available in v2.0. All data entry is via the Anaplan UX.</td><td><span style="color:#6b7280;font-weight:600">Low</span></td><td>Use native Anaplan UX for all data entry. For bulk uploads, use ADO-based flat file import pipelines.</td><td>Not planned for reintroduction</td></tr>
          <tr><td><strong>Dependent dropdowns inconsistent in generation</strong> — Dependent dropdown UX behavior does not always generate correctly. Pages may show all options rather than filtered options.</td><td><span style="color:#6b7280;font-weight:600">Low</span></td><td>Repair manually after generation by configuring the dropdown filter in the Page Builder. Typically 15–30 minutes per affected page.</td><td>No fix timeline — manual repair required</td></tr>
          <tr><td><strong>Line item codes not in generation</strong> — Line item codes must be populated manually after generation. They do not auto-populate from the configuration answers.</td><td><span style="color:#6b7280;font-weight:600">Low</span></td><td>Populate line item codes from the template model post-generation. Budget time for this in the post-generation checklist.</td><td>No fix expected near term</td></tr>
          <tr><td><strong>Naming mismatches in generation</strong> — If entity dimension name in configuration questions doesn't exactly match the hierarchy rename, modules and line items may not rename correctly throughout the model.</td><td><span style="color:#6b7280;font-weight:600">Low</span></td><td>Ensure exact name match (including capitalization) between the question response and hierarchy rename field. Review the generation log for naming errors immediately after generation.</td><td>By design — requires careful configuration</td></tr>
        </tbody>
      </table>

      <h2>Exclusion Checklist</h2>
      <p>Before scoping IFP v2.1, confirm the customer does <strong>NOT</strong> have any of the following hard stops:</p>
      <ul class="checklist">
        <li>Requires BYOK encryption on public cloud infrastructure</li>
        <li>Cannot use AWS-hosted services (public sector, federal, sovereign cloud)</li>
        <li>Requires more than 8 dimensions in any planning model</li>
        <li>Requires employee-level CapEx or headcount planning without OWP</li>
        <li>Requires waterfall or reciprocal cost allocation out of box</li>
      </ul>
      <p>If any box cannot be unchecked, stop and engage the Apps team before proceeding.</p>

      <h2>Ecosystem Gap Coverage</h2>
      <table>
        <thead><tr><th>Gap</th><th>Solution</th><th>Integration Pattern</th></tr></thead>
        <tbody>
          <tr><td>Employee-level headcount</td><td>Operational Workforce Planning (OWP)</td><td>OWP → ADO → IFP HC DAT module</td></tr>
          <tr><td>Commercial revenue planning</td><td>Consensus Margin Planning (CMP)</td><td>CMP → ADO → IFP Revenue DAT module</td></tr>
          <tr><td>Consolidation and statutory reporting</td><td>Financial Consolidation</td><td>IFP → ADO → Financial Consolidation</td></tr>
          <tr><td>Extended workforce budgeting</td><td>Workforce Budgeting (WFB)</td><td>Confirm integration pattern with Apps team</td></tr>
        </tbody>
      </table>

<div class="prevnext-nav"><a class="prevnext-btn" href="./inter-module-flows.html">← Previous</a><a class="prevnext-btn" href="./presales-demo.html">Next →</a></div>
    </div>
  </main>
  <script src="../js/nav.js"></script>
</body>
</html>"""
    open(os.path.join(DOCS, "limitations.html"), "w").write(html)
    print("  [limitations.html] built (NEW)")


# =============================================================================
# PRIORITY 3B — Upgrade whats-coming.html
# =============================================================================

def upgrade_whats_coming():
    active = "./whats-coming.html"
    nav = nav_block(active)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>What's Coming — IFP v2.1 Workshop</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  <div class="mobile-header">
    <button id="hamburger">☰</button>
    <span>IFP v2.1 Workshop</span>
  </div>

  <nav class="sidebar">
  <div class="sidebar-header">
  <div class="sidebar-title">IFP v2.1 Workshop</div>
  </div>
  <ul class="nav-list">
{nav}
      </ul>
    </nav>

  <main class="main-content">
    <div class="content-header">
      <h1>What's Coming</h1>
      <p class="subtitle">Roadmap snapshot — GA items, coming soon, and ecosystem integrations</p>
      <div class="badge-row"><span class="content-badge">Reference</span><span class="content-badge">Snapshot: March 2026</span></div>
    </div>
    <div class="content-body">

      <div class="callout-important"><span class="callout-label">📅 Frozen Snapshot</span><p><strong>Snapshot as of: March 2026 workshop session.</strong> Roadmap dates shift. Confirm all timelines with the Apps team at <a href="mailto:financeapplications@anaplan.com">financeapplications@anaplan.com</a> before quoting to a prospect.</p></div>

      <div class="callout-warning"><span class="callout-label">⚠ Quoting Roadmap Items</span><p>Do not quote roadmap items as committed delivery dates to customers or prospects. Mark all Coming Soon items as "planned, subject to change." When in doubt, say "I'll confirm with the Apps team."</p></div>

      <h2>GA vs. Coming Soon</h2>
      <table>
        <thead><tr><th>Feature</th><th>Status</th><th>Notes</th></tr></thead>
        <tbody>
          <tr><td>Application Framework (PAF) — all 4 models</td><td>✅ GA</td><td>Admin, FP, HC, CE models all generated via wizard</td></tr>
          <tr><td>Anaplan Data Orchestrator (ADO) integration</td><td>✅ GA</td><td>Replaces data hub; 5 links require manual creation post-generation</td></tr>
          <tr><td>Polaris engine — all 4 models</td><td>✅ GA</td><td>Optimized for large data volumes; 8-dimension limit applies</td></tr>
          <tr><td>Revenue &amp; COGS Planning</td><td>✅ GA</td><td>All planning methods available</td></tr>
          <tr><td>Operating Expenses</td><td>✅ GA</td><td>Including allocations (basic methods only)</td></tr>
          <tr><td>Headcount (job-level)</td><td>✅ GA</td><td>Employee-level requires OWP</td></tr>
          <tr><td>CapEx Planning</td><td>✅ GA</td><td>Entity-level only; no employee-level</td></tr>
          <tr><td>Balance Sheet &amp; Cash Flow</td><td>✅ GA</td><td>Including indirect cash flow, sub-schedules</td></tr>
          <tr><td>Top-Down Planning</td><td>✅ GA</td><td>Manual target entry only — disaggregation not yet available</td></tr>
          <tr><td>Reporting &amp; Analysis</td><td>✅ GA</td><td>IS, BS, CF reports + variance analysis + management reporting</td></tr>
          <tr><td>Currency Translation</td><td>✅ GA</td><td>Spot, average, closing, historical, and blended rates</td></tr>
          <tr><td>Multi-Currency (multi-entity)</td><td>✅ GA</td><td>Configured at generation time</td></tr>
          <tr><td>Top-Down dynamic disaggregation</td><td>🔜 Coming Soon</td><td>Planned for future release; no date confirmed</td></tr>
          <tr><td>Finance Analyst / CoPlanner</td><td>🔜 Coming Soon</td><td>Embedded in UX but not GA; do not scope or demo until confirmed</td></tr>
          <tr><td>Waterfall / reciprocal allocations</td><td>🔜 Coming Soon</td><td>No timeline — custom development required for now</td></tr>
          <tr><td>Employee-level CapEx</td><td>❌ Not planned</td><td>By design — use CE model for asset-level, OWP for employee-level</td></tr>
          <tr><td>End-user Excel import templates</td><td>❌ Not planned</td><td>Removed in v2.0; all data entry via UX or ADO flat file</td></tr>
        </tbody>
      </table>

      <h2>Application Framework Roadmap</h2>
      <ul>
        <li>Centralized upgrades via PAF — customers receive IFP improvements without manual rebuilds</li>
        <li>Order Management team takes over Application Delivery process once all apps are on AAF</li>
        <li>Partner enablement materials updated with each major release</li>
        <li>Generation issue fixes (dependent dropdowns, line item codes) targeted in future PAF releases</li>
      </ul>

      <h2>Ecosystem Integrations</h2>
      <p>These products are separate applications that integrate with IFP — they are not part of IFP itself.</p>
      <table>
        <thead><tr><th>Product</th><th>Status</th><th>What It Adds</th><th>Integration Pattern</th></tr></thead>
        <tbody>
          <tr><td><strong>Operational Workforce Planning (OWP)</strong></td><td>✅ GA</td><td>Position and employee-level headcount detail</td><td>OWP → ADO → IFP HC DAT module</td></tr>
          <tr><td><strong>Consensus Margin Planning (CMP)</strong></td><td>✅ GA</td><td>Revenue and margin planning from commercial/sales lens</td><td>CMP → ADO → IFP Revenue DAT module</td></tr>
          <tr><td><strong>Financial Consolidation</strong></td><td>✅ GA</td><td>Statutory consolidation and disclosure management downstream of IFP</td><td>IFP → ADO → Financial Consolidation</td></tr>
          <tr><td><strong>Workforce Budgeting (WFB)</strong></td><td>🔜 Coming Soon</td><td>Extended workforce cost budgeting — name TBC</td><td>Confirm integration pattern with Apps team</td></tr>
        </tbody>
      </table>

      <div class="callout-note"><span class="callout-label">ℹ Hard-Stop Limitations</span><p>Exclusion criteria and known hard-stop limitations have moved to the <a href="./limitations.html">Known Limitations</a> page. Review that page with every customer before scoping.</p></div>

      <h2>Stay Current</h2>
      <table>
        <thead><tr><th>Resource</th><th>Where</th></tr></thead>
        <tbody>
          <tr><td>Release notes and application updates</td><td>Anaplan Community — community.anaplan.com</td></tr>
          <tr><td>Updated partner training</td><td>Anaplan Enablement Portal</td></tr>
          <tr><td>Finance Applications CoE</td><td>financeapplications@anaplan.com</td></tr>
          <tr><td>General application questions</td><td>applications@anaplan.com</td></tr>
        </tbody>
      </table>

<div class="prevnext-nav"><a class="prevnext-btn" href="./inter-module-flows.html">← Previous</a><a class="prevnext-btn" href="./qanda.html">Next →</a></div>
    </div>
  </main>
  <script src="../js/nav.js"></script>
</body>
</html>"""
    open(os.path.join(DOCS, "whats-coming.html"), "w").write(html)
    print("  [whats-coming.html] upgraded (REBUILT)")


# =============================================================================
# PRIORITY 3C — Build presales-demo.html
# =============================================================================

def build_presales_demo():
    active = "./presales-demo.html"
    nav = nav_block(active)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pre-Sales Demo Playbook — IFP v2.1 Workshop</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  <div class="mobile-header">
    <button id="hamburger">☰</button>
    <span>IFP v2.1 Workshop</span>
  </div>

  <nav class="sidebar">
  <div class="sidebar-header">
  <div class="sidebar-title">IFP v2.1 Workshop</div>
  </div>
  <ul class="nav-list">
{nav}
      </ul>
    </nav>

  <main class="main-content">
    <div class="content-header">
      <h1>Pre-Sales Demo Playbook</h1>
      <p class="subtitle">Three buyer-type demo scenarios — what to show, what order, what to avoid</p>
      <div class="badge-row"><span class="content-badge">Reference</span><span class="content-badge">Pre-Sales</span></div>
    </div>
    <div class="content-body">

      <div class="callout-important"><span class="callout-label">🚨 Before Any Demo</span><p>Run through the <a href="./limitations.html">Known Limitations</a> page before every demo. Confirm the customer is not a hard-stop case (BYOK/AWS, &gt;8 dimensions, public sector). Do not proceed to a product demo with a disqualified prospect.</p></div>

      <div class="callout-warning"><span class="callout-label">⚠ Data Must Be Loaded</span><p>Never demo IFP with an empty or freshly generated application. Load the demo data set first — an empty planning grid is a deal-killer. Allow 30–60 minutes for demo environment prep before any customer call.</p></div>

      <h2>Scenario 1 — CFO / Executive</h2>
      <p><strong>Audience:</strong> CFO, VP Finance, Chief Accounting Officer, executive sponsor</p>
      <p><strong>What they care about:</strong> Time-to-deploy, risk, ROI, and whether the plan integrates across the business.</p>

      <h3>Show in This Order</h3>
      <ol>
        <li><strong>IFP landing page</strong> — show the 6-module grid; establish that this is a complete suite, not a point solution. Name each module in one sentence.</li>
        <li><strong>Top-Down Planning</strong> — open TD – Planning and show executive targets vs. bottom-up in the TD – Summary view. Lead with: "You set the target here. Your teams plan bottom-up. This page shows the gap — live."</li>
        <li><strong>Executive Dashboard</strong> — show the Reporting pack summary page. Highlight that it auto-generates from the planning data — no export, no manual copy-paste.</li>
        <li><strong>Time-to-deploy story</strong> — verbally cover: Application Framework generates the full suite in hours; partner configures in 8–10 weeks; upgrades are centrally deployed — no rebuild.</li>
      </ol>

      <h3>What NOT to Show (Before Data Is Loaded)</h3>
      <ul>
        <li>Do not open any planning grid before confirming demo data is loaded — empty grids look broken</li>
        <li>Do not show the Application Framework wizard — executives do not want to see configuration screens</li>
        <li>Do not show ADO pipeline details — this is IT content, not CFO content</li>
        <li>Do not show Finance Analyst / CoPlanner — not GA yet</li>
      </ul>

      <h3>Three Key Proof Points</h3>
      <ol>
        <li><strong>8–10 week deployment</strong> via Application Framework — not a 6-month custom build</li>
        <li><strong>Single connected suite</strong> — Revenue, OpEx, HC, CapEx, BS, and CF in one platform; no reconciliation spreadsheets</li>
        <li><strong>Centrally-managed upgrades</strong> — future releases deploy without manual rebuilds; customer stays current automatically</li>
      </ol>

      <h3>Common Objections + Factual Responses</h3>
      <table>
        <thead><tr><th>Objection</th><th>Factual Response</th></tr></thead>
        <tbody>
          <tr><td>"We already have Excel / EPM tool X."</td><td>IFP replaces spreadsheet-based consolidation by connecting all plan inputs in one model. Version comparison and variance analysis are built in — no manual reconciliation between tools.</td></tr>
          <tr><td>"8–10 weeks sounds fast. What's the catch?"</td><td>The Application Framework generates the model structure — the time savings come from not building custom models from scratch. Configuration and data load are still real work; 8–10 weeks assumes a clean, in-scope implementation.</td></tr>
          <tr><td>"We're public sector / we use a private cloud."</td><td>IFP v2.0+ requires ADO, which runs on AWS. Public sector and sovereign cloud customers cannot use IFP currently. Let's discuss what options exist — [stop and engage Apps team].</td></tr>
          <tr><td>"What about headcount planning?"</td><td>IFP includes job-level headcount planning with pay bands and cost sync to the financial plan. For employee-level detail, it integrates with Operational Workforce Planning. Most FP&amp;A teams find job-level sufficient for budget planning.</td></tr>
        </tbody>
      </table>

      <hr>

      <h2>Scenario 2 — FP&amp;A Manager</h2>
      <p><strong>Audience:</strong> FP&amp;A Manager, Senior Financial Analyst, Planning Manager, Budget Owner</p>
      <p><strong>What they care about:</strong> Planning workflow, data freshness, version comparison, how they replace their current process.</p>

      <h3>Show in This Order</h3>
      <ol>
        <li><strong>OpEx Planning page</strong> — show Progressive Disclosure: select a GL account, switch between methods. Demonstrate that only the relevant inputs appear per method. "Your team doesn't see line items that don't apply to their account."</li>
        <li><strong>Line Item Detail</strong> — show vendor/functional area tagging on one account. "This is where they get granular — without a separate spreadsheet."</li>
        <li><strong>Data load story</strong> — describe ADO: actuals come in from the ERP on a schedule via ADO pipelines. "The prior period closes, ADO runs, actuals are in — no manual upload."</li>
        <li><strong>IS Variance Analysis</strong> — open the two-version comparison. Show how to switch versions and read the variance. "This is your AOP vs. forecast comparison. Already built."</li>
        <li><strong>Version comparison workflow</strong> — briefly explain how versions are created in Admin and mapped across all 4 models.</li>
      </ol>

      <h3>What NOT to Show (Before Data Is Loaded)</h3>
      <ul>
        <li>Do not show a blank OpEx planning grid — every account should show prior period actuals for context</li>
        <li>Do not show the ADO pipeline configuration screens — focus on the outcome (data arrives), not the plumbing</li>
        <li>Do not show CapEx unless specifically asked — it adds complexity to an already content-rich demo</li>
        <li>Do not show Currency Translation unless the customer is explicitly multi-currency</li>
      </ul>

      <h3>Three Key Proof Points</h3>
      <ol>
        <li><strong>Progressive Disclosure</strong> — planners only see the inputs relevant to their account's method; fewer errors, less training</li>
        <li><strong>Automatic actuals refresh via ADO</strong> — no monthly upload task; prior period actuals flow in on schedule</li>
        <li><strong>Built-in version comparison</strong> — AOP vs. forecast, forecast vs. prior forecast — no separate reporting layer needed</li>
      </ol>

      <h3>Common Objections + Factual Responses</h3>
      <table>
        <thead><tr><th>Objection</th><th>Factual Response</th></tr></thead>
        <tbody>
          <tr><td>"We need employee-level headcount, not just job levels."</td><td>IFP HC plans at job/role level with pay bands — which covers 90% of budget planning needs. For employee-level detail, IFP integrates with Operational Workforce Planning. The two systems share data via ADO.</td></tr>
          <tr><td>"What if we need a custom planning method?"</td><td>IFP supports custom planning method extensions. The pattern is documented — add to the methods list, configure in the SYS module, wire the formula, assign to accounts. It's builder work, not custom development from scratch.</td></tr>
          <tr><td>"How long does the actuals load take each month?"</td><td>ADO pipelines run on schedule — typically 15–60 minutes depending on data volume. Once configured, it runs unattended. The admin just confirms the data loaded correctly.</td></tr>
          <tr><td>"Can our team still export to Excel?"</td><td>Anaplan supports native Excel export from any grid. For formatted reports, the management reporting pack exports to PDF. We'd scope exact export requirements during implementation.</td></tr>
        </tbody>
      </table>

      <hr>

      <h2>Scenario 3 — IT / Architect</h2>
      <p><strong>Audience:</strong> IT Director, Enterprise Architect, Integration Lead, CTO</p>
      <p><strong>What they care about:</strong> How it's built, how data moves, what they'll need to maintain, security and compliance.</p>

      <h3>Show in This Order</h3>
      <ol>
        <li><strong>Application Framework</strong> — open the Applications URL; show the wizard. "This is how the suite is deployed — a configuration wizard that generates all 4 models, UX pages, and ADO pipelines in one generation run. No model building from scratch."</li>
        <li><strong>Four-model architecture</strong> — draw or show: Admin (central config), FP (financial planning), HC (headcount), CE (CapEx). "Admin is the hub. FP is the planning hub. HC and CE are spoke models that import into FP."</li>
        <li><strong>ADO pipeline overview</strong> — open ADO; show the pipeline list. "Each pipeline is a lightweight extract-transform-load. No memory overhead in the Anaplan workspace — data stays in motion, not in memory."</li>
        <li><strong>Polaris model architecture</strong> — explain: Polaris engine, 8-dimension limit, optimized for large data volumes vs. Classic engine. "This is not the same Anaplan model you may have seen in v1.x."</li>
        <li><strong>Upgrade path</strong> — "Future versions of IFP are deployed via the Application Framework centrally. Customer doesn't rebuild — they apply the update. IT's maintenance burden is lower than a custom-built model."</li>
      </ol>

      <h3>What NOT to Show (Before Data Is Loaded)</h3>
      <ul>
        <li>Do not show planning pages to an IT audience — they are not the planning users and will focus on what's wrong with the UX</li>
        <li>Do not dive into formula details unless specifically asked — stay at architecture level</li>
        <li>Do not show Finance Analyst / CoPlanner — not GA</li>
      </ul>

      <h3>Three Key Proof Points</h3>
      <ol>
        <li><strong>Generated architecture</strong> — not a custom model; generated from configuration; consistent structure; easier to maintain and upgrade</li>
        <li><strong>ADO: lightweight pipelines</strong> — no memory overhead in the workspace; data moves via lightweight pipelines, not Anaplan actions loading data into workspace memory</li>
        <li><strong>Polaris: optimized for large data volumes</strong> — the engine is purpose-built for the data volumes typical in enterprise financial planning; 8-dimension constraint is the architectural trade-off</li>
      </ol>

      <h3>Common Objections + Factual Responses</h3>
      <table>
        <thead><tr><th>Objection</th><th>Factual Response</th></tr></thead>
        <tbody>
          <tr><td>"We can't use AWS. We're on Azure / private cloud."</td><td>ADO is an AWS-native service. IFP v2.0+ requires ADO. This is a hard stop — IFP cannot be deployed in non-AWS environments currently. We should stop and clarify your cloud requirements before proceeding.</td></tr>
          <tr><td>"8 dimensions isn't enough for our data model."</td><td>The 8-dimension limit is a Polaris architecture constraint — it applies to all IFP models. If your implementation requires more than 8 dimensions, IFP is not the right fit. We'd need to review your dimension requirements in detail.</td></tr>
          <tr><td>"How do we integrate with our ERP?"</td><td>ADO connects to your source systems via flat file or API. The typical pattern: ERP exports a flat file to a cloud storage location; ADO picks it up on a schedule and loads into the Admin model. Supported connectors include Snowflake, S3, and standard REST APIs.</td></tr>
          <tr><td>"What's the ALM / promotion path from Dev to Prod?"</td><td>Standard Anaplan ALM — Dev model is the source; promote via the ALM UI or API to Prod. ADO pipelines are promoted separately. The Application Framework generates Dev; IT manages the ALM promotion as part of go-live.</td></tr>
          <tr><td>"Who maintains this after go-live?"</td><td>The customer's admin team handles monthly tasks (period updates, version creation, data load confirmation). The partner handles major changes (new modules, extensions). Anaplan releases upgrades via the Application Framework — the admin applies them.</td></tr>
        </tbody>
      </table>

      <hr>

      <h2>Demo Environment Prep Checklist</h2>
      <ul class="checklist">
        <li>Demo workspace is a Polaris workspace (confirm in workspace settings)</li>
        <li>All 4 IFP models generated and published</li>
        <li>Demo data loaded via ADO — actuals visible in planning grids</li>
        <li>Current period set to July (gives a 6+6 split that looks complete on screen)</li>
        <li>Versions set up: AOP Base, Current Forecast Base, Prior Forecast (minimum)</li>
        <li>Management Reporting pack has data — open it and confirm it's not blank</li>
        <li>Top-Down Summary has data in both target and bottom-up columns</li>
        <li>IS Variance Analysis shows meaningful variances (not all zeros)</li>
        <li>Review Known Limitations with the team before the call</li>
        <li>Confirm customer is not a hard-stop case before proceeding</li>
      </ul>

<div class="prevnext-nav"><a class="prevnext-btn" href="./limitations.html">← Previous</a><a class="prevnext-btn" href="./inter-module-flows.html">Next →</a></div>
    </div>
  </main>
  <script src="../js/nav.js"></script>
</body>
</html>"""
    open(os.path.join(DOCS, "presales-demo.html"), "w").write(html)
    print("  [presales-demo.html] built (NEW)")


# =============================================================================
# PRIORITY 4 — Sales language fixes in ifp-overview.html
# =============================================================================

def fix_sales_language():
    path = os.path.join(DOCS, "ifp-overview.html")
    content = open(path).read()

    # Fix 1: description of IFP
    content = content.replace(
        "delivering comprehensive P&amp;L, cash flow, and balance sheet planning through a connected set of modules built on the Anaplan Application Framework and Polaris.",
        "IFP v2.0 is Anaplan&#39;s application suite for the Office of the CFO — covering P&amp;L, cash flow, and balance sheet planning through a set of modules built on the Anaplan Application Framework and Polaris."
    )

    # Fix 2: high-performance pipelines → lightweight pipelines
    content = content.replace(
        "lightweight, high-performance pipelines",
        "lightweight pipelines with no memory overhead in the workspace"
    )

    # Fix 3: superior performance
    content = content.replace(
        "Polaris engine: superior performance for large data volumes",
        "Polaris engine: optimized for large data volumes compared to the Classic engine"
    )

    # Fix 4: Delayed Time-to-Value row header
    content = content.replace(
        "<td>Delayed Time-to-Value</td>",
        "<td>Long implementation lead time</td>"
    )

    open(path, "w").write(content)
    print("  [ifp-overview.html] 4 sales language fixes applied")


# =============================================================================
# PRIORITY 5 — Version branding: v2.0 → v2.1 (workshop branding only)
# =============================================================================

def fix_version_branding():
    html_files = [f for f in os.listdir(DOCS) if f.endswith(".html")]
    count = 0
    for fname in html_files:
        path = os.path.join(DOCS, fname)
        content = open(path).read()
        orig = content

        # Page title
        content = content.replace("IFP v2.0 Workshop", "IFP v2.1 Workshop")
        # Sidebar title
        content = content.replace(">IFP v2.0 Workshop<", ">IFP v2.1 Workshop<")
        # Mobile header span
        content = content.replace(">IFP v2.0 Workshop<", ">IFP v2.1 Workshop<")

        if content != orig:
            open(path, "w").write(content)
            count += 1
    print(f"  Version branding updated in {count} files")


# =============================================================================
# NAV REBUILD — Update all existing pages to add limitations + presales-demo
# =============================================================================

def rebuild_nav_in_all_files():
    """Replace the sidebar nav block in every HTML file with the updated nav."""
    html_files = [f for f in os.listdir(DOCS) if f.endswith(".html")]
    count = 0
    for fname in html_files:
        path = os.path.join(DOCS, fname)
        content = open(path).read()
        orig = content

        # Determine active href for this file
        active_href = f"./{fname}"

        # Build new nav lines
        new_nav_items = nav_block(active_href)

        # Find and replace the nav-list content
        # Pattern: everything between <ul class="nav-list"> and </ul>
        pattern = r'(<ul class="nav-list">)\s*.*?(\s*</ul>)'
        replacement = f'<ul class="nav-list">\n{new_nav_items}\n      </ul>'
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        # Also fix sidebar title and mobile header branding
        new_content = new_content.replace(
            "<div class=\"sidebar-title\">IFP v2.0 Workshop</div>",
            "<div class=\"sidebar-title\">IFP v2.1 Workshop</div>"
        )
        new_content = new_content.replace(
            "<span>IFP v2.0 Workshop</span>",
            "<span>IFP v2.1 Workshop</span>"
        )

        if new_content != orig:
            open(path, "w").write(new_content)
            count += 1

    print(f"  Nav rebuilt in {count} files (limitations + presales-demo added)")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("\n=== PRIORITY 1: Wire screenshots ===")
    patch_opex()
    patch_balance_sheet()
    patch_capex()
    patch_revenue_cogs()
    patch_top_down()
    patch_reporting()
    patch_headcount()
    patch_app_framework()

    print("\n=== PRIORITY 2: Add placeholders ===")
    patch_ifp_overview_placeholder()
    patch_config_walkthrough_placeholder()
    patch_admin_runbook_placeholder()
    patch_extensions_placeholder()
    patch_post_generation_placeholder()
    patch_anaplan_way_placeholder()
    patch_lab_b_placeholder()

    print("\n=== PRIORITY 3: Build new pages + upgrade existing ===")
    build_limitations()
    upgrade_whats_coming()
    build_presales_demo()

    print("\n=== PRIORITY 4: Sales language fixes ===")
    fix_sales_language()

    print("\n=== PRIORITY 5: Version branding ===")
    fix_version_branding()

    print("\n=== NAV REBUILD: All files ===")
    rebuild_nav_in_all_files()

    print("\n✅ All priorities complete.")
