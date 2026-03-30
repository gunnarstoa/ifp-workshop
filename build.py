#!/usr/bin/env python3
"""
IFP Workshop HTML Builder
Generates all pages with consistent nav, styling, and content.
"""

import os

DOCS = "/home/gstoa/.openclaw/workspace/projects/work/workshops/ifp-workshop/docs"
ROOT = "/home/gstoa/.openclaw/workspace/projects/work/workshops/ifp-workshop"

# ─── Navigation ───────────────────────────────────────────────────────────────

NAV_ITEMS = [
    ("section", "Getting Started"),
    ("link", "Workshop Overview", "./overview.html"),
    ("link", "Case Study: FictoCorp", "./case-study.html"),
    ("link", "IFP Suite Overview", "./ifp-overview.html"),
    ("link", "Anaplan Way for Apps", "./anaplan-way.html"),
    ("section", "Module 1 — Platform Foundations"),
    ("link", "Application Framework", "./app-framework.html"),
    ("link", "Anaplan Data Orchestrator", "./ado-overview.html"),
    ("link", "Model Architecture", "./model-architecture.html"),
    ("section", "Module 2 — Configuration Workshop"),
    ("link", "App Framework Walkthrough", "./config-walkthrough.html"),
    ("link", "Lab A: Configure FictoCorp", "./lab-a.html"),
    ("link", "Post-Generation Checklist", "./post-generation.html"),
    ("link", "Data Load via ADO", "./data-load-ado.html"),
    ("link", "Lab B: Full 3-Statement", "./lab-b.html"),
    ("section", "Module 3 — Module Walkthroughs"),
    ("link", "Revenue &amp; COGS Planning", "./revenue-cogs.html"),
    ("link", "Operating Expenses", "./opex.html"),
    ("link", "Headcount Planning", "./headcount.html"),
    ("link", "CapEx Planning", "./capex.html"),
    ("link", "Balance Sheet &amp; Cash Flow", "./balance-sheet.html"),
    ("link", "Top-Down Planning", "./top-down.html"),
    ("link", "Reporting &amp; Analysis", "./reporting.html"),
    ("section", "Module 4 — Admin &amp; Extensions"),
    ("link", "Admin Runbook", "./admin-runbook.html"),
    ("link", "Currency Translation", "./currency-translation.html"),
    ("link", "Common Extensions", "./extensions.html"),
    ("section", "Reference"),
    ("link", "Inter-Module Data Flows", "./inter-module-flows.html"),
    ("link", "What's Coming", "./whats-coming.html"),
    ("link", "Q&amp;A from Sessions", "./qanda.html"),
    ("link", "Resources &amp; Downloads", "./resources.html"),
    ("link", "Glossary", "./glossary.html"),
    ("link", "Facilitator Guide", "./facilitator.html"),
]

# Page order for prev/next
PAGE_ORDER = [item[2] for item in NAV_ITEMS if item[0] == "link"]

def build_nav(active_href, from_root=False):
    prefix = "./docs/" if from_root else "./"
    lines = ['<nav class="sidebar">', '<div class="sidebar-header">',
             '<div class="sidebar-title">IFP v2.0 Workshop</div>', '</div>',
             '<ul class="nav-list">']
    for item in NAV_ITEMS:
        if item[0] == "section":
            lines.append(f'<li class="nav-section-title">{item[1]}</li>')
        else:
            _, label, href = item
            adj_href = (prefix + href.lstrip("./")) if from_root else href
            active = ' active' if href == active_href else ''
            lines.append(f'<li><a class="nav-link{active}" href="{adj_href}">{label}</a></li>')
    lines += ['</ul>', '</nav>']
    return "\n".join(lines)

def build_prevnext(active_href):
    links = PAGE_ORDER
    try:
        idx = links.index(active_href)
    except ValueError:
        return ""
    prev_link = f'<a class="prevnext-btn" href="{links[idx-1]}">← Previous</a>' if idx > 0 else '<span></span>'
    next_link = f'<a class="prevnext-btn" href="{links[idx+1]}">Next →</a>' if idx < len(links)-1 else '<span></span>'
    return f'<div class="prevnext-nav">{prev_link}{next_link}</div>'

def page(title, href, body, tsd=True):
    tsd_banner = """
  <div class="tsd-banner">
    <div class="tsd-item tsd-tell">
      <span class="tsd-icon">📖</span>
      <div><strong>Tell</strong><br>Understand the concept</div>
    </div>
    <div class="tsd-item tsd-show">
      <span class="tsd-icon">👁</span>
      <div><strong>Show</strong><br>See it demonstrated</div>
    </div>
    <div class="tsd-item tsd-do">
      <span class="tsd-icon">✅</span>
      <div><strong>Do</strong><br>Apply it yourself</div>
    </div>
  </div>""" if tsd else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — IFP v2.0 Workshop</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  <div class="mobile-header">
    <button id="hamburger">☰</button>
    <span>IFP v2.0 Workshop</span>
  </div>

  {build_nav(href)}

  <main class="main-content">
    <div class="content-body">
      {tsd_banner}
      {body}
      {build_prevnext(href)}
    </div>
  </main>
  <script src="../js/nav.js"></script>
</body>
</html>"""

def write(filename, content):
    path = os.path.join(DOCS, filename)
    with open(path, 'w') as f:
        f.write(content)
    print(f"✅ {filename}")

def callout(type_, title, body):
    icons = {"tip": "💡", "warning": "⚠️", "note": "📝", "important": "🚨"}
    icon = icons.get(type_, "ℹ️")
    return f'<div class="callout callout-{type_}"><strong>{icon} {title}</strong><p>{body}</p></div>'

def screenshot(label):
    return f'<div class="screenshot-placeholder"><em>📸 Screenshot: {label}</em></div>'

def table(headers, rows):
    ths = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f"<table><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table>"

# ─── Pages ────────────────────────────────────────────────────────────────────

# Overview
write("overview.html", page("Workshop Overview", "./overview.html", """
<h1>Workshop Overview</h1>
<p>Welcome to the <strong>IFP v2.0 Technical Enablement Workshop</strong> — a hands-on program for Anaplan delivery practitioners building skills on the Integrated Financial Planning application version 2.0.</p>

<h2>What You'll Learn</h2>
<ul>
  <li>How the Anaplan Application Framework deploys and generates IFP models</li>
  <li>How ADO (Anaplan Data Orchestrator) replaces the data hub for all data integration</li>
  <li>How to answer all Application Framework configuration questions — and what each choice means</li>
  <li>Post-generation tasks required to make every IFP deployment production-ready</li>
  <li>Deep walkthroughs of all 6 planning modules plus Reporting &amp; Analysis</li>
  <li>Administration, version management, and ongoing maintenance</li>
  <li>Currency translation via triangulation</li>
  <li>How to create custom planning methods and extend the application</li>
</ul>

<h2>Prerequisites</h2>
<ul>
  <li>Anaplan model builder certification (or equivalent experience)</li>
  <li>Access to an IFP v2.0 workspace (your facilitator will provide credentials)</li>
  <li>Familiarity with basic Anaplan concepts: lists, modules, blueprints, actions, UX pages</li>
  <li>Basic understanding of financial planning (P&amp;L, Balance Sheet, Cash Flow)</li>
</ul>

<h2>Workshop Structure</h2>
""" + table(
    ["Module", "Topic", "Format"],
    [
        ["Getting Started", "IFP overview, case study, Anaplan Way", "Read"],
        ["Module 1", "Application Framework, ADO, Model Architecture", "Tell + Show"],
        ["Module 2", "Configuration Workshop — Labs A &amp; B", "Tell + Show + Do"],
        ["Module 3", "All 7 planning module walkthroughs", "Tell + Show"],
        ["Module 4", "Admin runbook, currency, extensions", "Tell + Show"],
        ["Reference", "Data flows, glossary, Q&amp;A, resources", "Reference"],
    ]
) + """
<h2>How to Use This Guide</h2>
<p>Each page follows the <strong>Tell → Show → Do</strong> pattern. Start with the <a href="./case-study.html">Case Study</a> to understand FictoCorp Industries — the fictional company used in all exercises. Then work through the modules in order.</p>
""" + callout("tip", "Lab Setup", "Before starting Lab A, ensure your IFP v2.0 workspace is provisioned and you have all 4 required roles: Application Owner, Workspace Admin, Page Builder, and Integration Admin."), tsd=False))

# Case Study
write("case-study.html", page("Case Study: FictoCorp Industries", "./case-study.html", """
<h1>Case Study: FictoCorp Industries</h1>
<p>FictoCorp Industries is the fictional company used throughout all workshop exercises. Familiarise yourself with their profile before starting any lab.</p>

<h2>Company Profile</h2>
""" + table(
    ["Attribute", "Value"],
    [
        ["Industry", "Global Manufacturing"],
        ["Headquarters", "San Francisco, CA"],
        ["Revenue", "$450M annually"],
        ["Employees", "~500 (job-based HC planning)"],
        ["Entities", "FictoCorp USA · FictoCorp EMEA"],
        ["Departments", "Sales &amp; Marketing · Operations · G&amp;A"],
        ["Products", "Hardware (H1, H2) · Software (S1, S2)"],
        ["Customers", "Enterprise · Commercial"],
        ["Base Currency", "USD"],
        ["Reporting Currencies", "USD · EUR · GBP"],
        ["Planning Scope", "Full 3-statement: Revenue/COGS + OpEx + HC + CapEx + BS/CF"],
        ["FX", "Multi-currency, triangulation method"],
    ]
) + """
<h2>Planning Challenges</h2>
<p>FictoCorp is moving off spreadsheets to Anaplan IFP v2.0. Their key challenges:</p>
<ul>
  <li>Manual, disconnected P&amp;L and headcount planning processes</li>
  <li>No unified balance sheet view — cash flow done in Excel post-close</li>
  <li>CapEx tracked in a separate system with no P&amp;L linkage</li>
  <li>Multi-currency consolidation taking 3 days per cycle</li>
  <li>Cannot model scenarios quickly enough for CFO review</li>
</ul>

<h2>Hierarchy Structure</h2>
<h3>Entity Hierarchy (2 levels)</h3>
<ul>
  <li>Total FictoCorp
    <ul>
      <li>FictoCorp USA</li>
      <li>FictoCorp EMEA</li>
    </ul>
  </li>
</ul>
<h3>Department Hierarchy (3 levels)</h3>
<ul>
  <li>All Departments
    <ul>
      <li>Sales &amp; Marketing
        <ul><li>Direct Sales · Marketing · Partner Sales</li></ul>
      </li>
      <li>Operations
        <ul><li>Manufacturing · Supply Chain · Quality</li></ul>
      </li>
      <li>G&amp;A
        <ul><li>Finance · HR · IT · Legal</li></ul>
      </li>
    </ul>
  </li>
</ul>
<h3>Product Hierarchy (2 levels)</h3>
<ul>
  <li>All Products
    <ul>
      <li>Hardware → H1 (Industrial), H2 (Commercial)</li>
      <li>Software → S1 (Platform License), S2 (SaaS)</li>
    </ul>
  </li>
</ul>

<h2>Your Role</h2>
<p>You are an Anaplan implementation consultant engaged to deploy IFP v2.0 for FictoCorp. You will configure the Application Framework, set up ADO pipelines, and walk the FictoCorp finance team through their new planning environment.</p>
""" + callout("note", "Lab A vs Lab B", "Lab A deploys Revenue/COGS + OpEx + HC only — no CapEx, no Balance Sheet. Lab B extends this to full 3-statement. Start with Lab A to learn the core configuration flow before adding complexity.")))

# IFP Overview
write("ifp-overview.html", page("IFP Suite Overview", "./ifp-overview.html", """
<h1>IFP Suite Overview</h1>
<p>Integrated Financial Planning (IFP) v2.0 is Anaplan's application suite for the Office of the CFO. It delivers comprehensive P&amp;L, cash flow, and balance sheet planning through a connected set of modules built on the Anaplan Application Framework.</p>

<h2>The Problem IFP Solves</h2>
""" + table(
    ["Problem", "How IFP Solves It"],
    [
        ["Inefficient Planning Cycles", "Automates forecasting with pre-built best practices"],
        ["Fragmented Enterprise Planning", "Serves as finance's central hub connecting all enterprise plans"],
        ["Reactive &amp; Uninformed Decisions", "Agile decision-making with built-in scenario and what-if analysis"],
        ["Delayed Time-to-Value", "Complete best-practice solution deployable in 8–10 weeks"],
        ["Rigid &amp; Inflexible Systems", "Configurable and extensible platform that scales with the business"],
    ]
) + """
<h2>Six Planning Modules</h2>
<div class="module-grid">
  <div class="module-card"><h3>💰 Revenue &amp; COGS</h3><p>Forecast revenue and margins using driver-based planning methods across products, customers, and entities.</p></div>
  <div class="module-card"><h3>📊 Operating Expenses</h3><p>Plan and manage OpEx using driver-based methods, line item detail, and single-step allocations.</p></div>
  <div class="module-card"><h3>👥 Headcount</h3><p>Forecast job-level headcount and costs, model workforce changes, and analyze plan vs. actuals.</p></div>
  <div class="module-card"><h3>🏗 CapEx</h3><p>Plan individual assets, model depreciation and disposals, see immediate P&amp;L and cash flow impact.</p></div>
  <div class="module-card"><h3>📋 Balance Sheet &amp; CF</h3><p>Model working capital with drivers, manage cash via funding logic, automate indirect cash flow.</p></div>
  <div class="module-card"><h3>🎯 Top-Down Planning</h3><p>Set executive-level targets for revenue, margin, OpEx, FTE, and labor costs. Reconcile against bottom-up.</p></div>
</div>
<p style="margin-top:1rem">Plus: <strong>Reporting &amp; Analysis</strong> — consolidated IS, BS, CF reports, variance analysis, and AI-powered insights via Anaplan Finance Analyst.</p>

<h2>Key v2.0 Features</h2>
""" + table(
    ["Feature", "What It Means"],
    [
        ["Anaplan Application Framework", "Centralized, upgradeable deployment — replaces the static v1.x configurator"],
        ["Anaplan Data Orchestrator (ADO)", "Replaces the data hub model — lightweight, high-performance data pipelines"],
        ["Job-Based Headcount", "Plans at role/job level, not employee — protects PII, enables OWP integration"],
        ["Progressive Disclosure UI", "Shows only relevant input fields per planning method — reduces errors"],
        ["Re-architected Models", "Polaris engine: superior performance and scalability for large data volumes"],
        ["Finance Analyst (CoPlanner)", "AI-powered natural language queries embedded in the application"],
    ]
) + """
<h2>v1.3 → v2.0 Key Differences</h2>
""" + table(
    ["Area", "v1.3", "v2.0"],
    [
        ["Deployment", "Static one-time configurator", "Application Framework — upgradeable"],
        ["Data Integration", "Complex data hub model", "ADO — lightweight, centralized"],
        ["Headcount", "Employee-level planning", "Job-level (PII protection), OWP integration"],
        ["UX", "Complex numbered pages", "Progressive Disclosure, descriptive names"],
        ["Admin Model", "Required separately", "Removed — all via ADO"],
        ["Performance", "Struggled at scale", "Re-architected for Polaris engine"],
    ]
) + """
<h2>Application Entitlements Required</h2>
<ul>
  <li><strong>Polaris</strong> — calculation engine powering all IFP models</li>
  <li><strong>ADO (Anaplan Data Orchestrator)</strong> — data integration layer</li>
  <li><strong>Finance Analyst / CoPlanner</strong> — AI insights (pending full availability)</li>
</ul>
""" + callout("important", "Customer Exclusion Criteria", "IFP v2.0 is NOT suitable for: customers requiring BYOK on public cloud, customers who cannot use AWS, public sector/federal organizations, or customers requiring more than 8 dimensions for their use cases.")))

# Anaplan Way
write("anaplan-way.html", page("Anaplan Way for Applications", "./anaplan-way.html", """
<h1>The Anaplan Way for Applications</h1>
<p>Every Anaplan application deployment follows the <strong>Anaplan Way for Applications</strong> — a structured delivery methodology that ensures consistent, high-quality implementations with predictable time-to-value.</p>

<h2>The Delivery Process Framework</h2>
""" + screenshot("Anaplan Way for Applications — 6-phase delivery framework diagram") + """
<ol>
  <li><strong>Requirements</strong> — Architect and customer agree on scope, dimensions, and configuration choices</li>
  <li><strong>Configure</strong> — Configure the application via the Anaplan Application Foundation (interview-style wizard)</li>
  <li><strong>Generate</strong> — Application models and UX are generated based on configuration responses</li>
  <li><strong>Data Load &amp; Publish</strong> — Import source data via ADO, sync with spoke models</li>
  <li><strong>Application Ready</strong> — Application available for user acceptance testing and go-live</li>
  <li><strong>Extend &amp; Expand</strong> — Customer extends functionality, adds other applications, or builds custom additions</li>
</ol>

<h2>Implementation Phases for IFP</h2>
""" + table(
    ["Phase", "Activities", "Who"],
    [
        ["Discover", "Requirements gathering, exclusion checklist, dimension decisions, scope agreement", "Partner + Customer"],
        ["Configure", "Run Application Framework wizard, answer all configuration questions, set hierarchy levels", "Partner (Anaplan PS available)"],
        ["Generate", "Deploy models via PAF, validate generation logs, fix known issues", "Partner"],
        ["Post-Generation", "Time/version setup, ADO pipelines, data load, UX validation, delete DEMO actions", "Partner"],
        ["Test", "UAT with customer, data validation, variance checks, user training", "Partner + Customer"],
        ["Go-Live", "Promote Dev → Prod via ALM, hand over admin responsibilities", "Partner + Customer"],
        ["Expand", "Extensions, additional modules, or new applications", "Customer + Partner"],
    ]
) + """
<h2>Provisioning Requirements</h2>
<p>Before configuring IFP v2.0, ensure the following are in place:</p>
<ul>
  <li>Polaris workspace provisioned (minimum 100GB)</li>
  <li>Delivery Request created in Salesforce (CSBP)</li>
  <li>Finance Apps CoE added to workspace (email financeapplications@anaplan.com)</li>
</ul>
<p>The generating user must have all 4 roles in the tenant:</p>
""" + table(
    ["Role", "Purpose"],
    [
        ["Application Owner", "Access to Applications URL"],
        ["Workspace Admin", "Full model access"],
        ["Page Builder", "UX page creation"],
        ["Integration Admin*", "ADO and data integration — <em>must generate in their default tenant</em>"],
    ]
) + callout("important", "Partner Tenant Note", "Integration Admins can only generate in their default tenant. If you are a partner, work with your customer to get an Anaplan account with the default tenant set to the customer's environment before generating.") + """
<h2>The Role of Partners</h2>
<p>Anaplan partners are the primary deployers of IFP applications. Partners should:</p>
<ul>
  <li>Lead the configuration workshop with the customer finance team</li>
  <li>Own post-generation setup and ADO pipeline configuration</li>
  <li>Train customer model administrators on the ongoing admin runbook</li>
  <li>Scope and deliver extensions based on customer requirements</li>
  <li>Contact financeapplications@anaplan.com for Finance CoE support during implementation</li>
</ul>
"""))

print("Getting Started pages done.")
