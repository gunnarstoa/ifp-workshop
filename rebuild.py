#!/usr/bin/env python3
"""
IFP Workshop — Full Rebuild using exact RPM HTML patterns.
Matches RPM workshop styling precisely.
"""
import os, re

DOCS = "/home/gstoa/.openclaw/workspace/projects/work/workshops/ifp-workshop/docs"
ROOT = "/home/gstoa/.openclaw/workspace/projects/work/workshops/ifp-workshop"

# ─── Nav (same structure as RPM) ─────────────────────────────────────────────

def nav(active):
    items = [
        ("s", "Getting Started"),
        ("l", "Workshop Overview", "overview.html"),
        ("l", "Case Study: FictoCorp", "case-study.html"),
        ("l", "IFP Suite Overview", "ifp-overview.html"),
        ("l", "Anaplan Way for Apps", "anaplan-way.html"),
        ("s", "Module 1 — Platform Foundations"),
        ("l", "Application Framework", "app-framework.html"),
        ("l", "Anaplan Data Orchestrator", "ado-overview.html"),
        ("l", "Model Architecture", "model-architecture.html"),
        ("s", "Module 2 — Configuration Workshop"),
        ("l", "App Framework Walkthrough", "config-walkthrough.html"),
        ("l", "Lab A: Configure FictoCorp", "lab-a.html"),
        ("l", "Post-Generation Checklist", "post-generation.html"),
        ("l", "Data Load via ADO", "data-load-ado.html"),
        ("l", "Lab B: Full 3-Statement", "lab-b.html"),
        ("s", "Module 3 — Module Walkthroughs"),
        ("l", "Revenue &amp; COGS Planning", "revenue-cogs.html"),
        ("l", "Operating Expenses", "opex.html"),
        ("l", "Headcount Planning", "headcount.html"),
        ("l", "CapEx Planning", "capex.html"),
        ("l", "Balance Sheet &amp; Cash Flow", "balance-sheet.html"),
        ("l", "Top-Down Planning", "top-down.html"),
        ("l", "Reporting &amp; Analysis", "reporting.html"),
        ("s", "Module 4 — Admin &amp; Extensions"),
        ("l", "Admin Runbook", "admin-runbook.html"),
        ("l", "Currency Translation", "currency-translation.html"),
        ("l", "Common Extensions", "extensions.html"),
        ("s", "Reference"),
        ("l", "Inter-Module Data Flows", "inter-module-flows.html"),
        ("l", "What's Coming", "whats-coming.html"),
        ("l", "Q&amp;A from Sessions", "qanda.html"),
        ("l", "Resources &amp; Downloads", "resources.html"),
        ("l", "Glossary", "glossary.html"),
        ("l", "Facilitator Guide", "facilitator.html"),
    ]
    lines = ['<nav class="sidebar">', '<div class="sidebar-header">',
             '<div class="sidebar-title">IFP v2.0 Workshop</div>', '</div>', '<ul class="nav-list">']
    for item in items:
        if item[0] == "s":
            lines.append(f'      <li class="nav-section-title">{item[1]}</li>')
        else:
            cls = 'nav-link active' if item[2] == active else 'nav-link'
            lines.append(f'      <li><a class="{cls}" href="./{item[2]}">{item[1]}</a></li>')
    lines += ['    </ul>', '  </nav>']
    return "\n  ".join(lines)

# Page order for prev/next
PAGE_ORDER = [item[2] for item in [
    ("l","","overview.html"),("l","","case-study.html"),("l","","ifp-overview.html"),("l","","anaplan-way.html"),
    ("l","","app-framework.html"),("l","","ado-overview.html"),("l","","model-architecture.html"),
    ("l","","config-walkthrough.html"),("l","","lab-a.html"),("l","","post-generation.html"),
    ("l","","data-load-ado.html"),("l","","lab-b.html"),
    ("l","","revenue-cogs.html"),("l","","opex.html"),("l","","headcount.html"),("l","","capex.html"),
    ("l","","balance-sheet.html"),("l","","top-down.html"),("l","","reporting.html"),
    ("l","","admin-runbook.html"),("l","","currency-translation.html"),("l","","extensions.html"),
    ("l","","inter-module-flows.html"),("l","","whats-coming.html"),("l","","qanda.html"),
    ("l","","resources.html"),("l","","glossary.html"),("l","","facilitator.html"),
] if item[0]=="l"]

def prevnext(active):
    try:
        idx = PAGE_ORDER.index(active)
    except ValueError:
        return ""
    prev = f'<a class="prevnext-btn" href="./{PAGE_ORDER[idx-1]}">← Previous</a>' if idx > 0 else '<span></span>'
    nxt = f'<a class="prevnext-btn" href="./{PAGE_ORDER[idx+1]}">Next →</a>' if idx < len(PAGE_ORDER)-1 else '<span></span>'
    return f'<div class="prevnext-nav">{prev}{nxt}</div>'

def page(title, filename, subtitle, badges, tsd_tell, tsd_show, tsd_do, body):
    badge_html = "".join(f'<span class="content-badge">{b}</span>' for b in badges)
    tsd_html = f"""      <div class="tsd-banner">
        <div class="tsd-step tsd-step-tell">
          <span class="tsd-step-label">📖 Tell</span>
          <span class="tsd-step-heading">{tsd_tell[0]}</span>
          <span class="tsd-step-desc">{tsd_tell[1]}</span>
        </div>
        <div class="tsd-step tsd-step-show">
          <span class="tsd-step-label">👁 Show</span>
          <span class="tsd-step-heading">{tsd_show[0]}</span>
          <span class="tsd-step-desc">{tsd_show[1]}</span>
        </div>
        <div class="tsd-step tsd-step-do">
          <span class="tsd-step-label">✅ Do</span>
          <span class="tsd-step-heading">{tsd_do[0]}</span>
          <span class="tsd-step-desc">{tsd_do[1]}</span>
        </div>
      </div>""" if tsd_tell else ""

    html = f"""<!DOCTYPE html>
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

  {nav(filename)}

  <main class="main-content">
    <div class="content-header">
      <h1>{title}</h1>
      <p class="subtitle">{subtitle}</p>
      <div class="badge-row">{badge_html}</div>
    </div>
    <div class="content-body">
{tsd_html}
{body}
{prevnext(filename)}
    </div>
  </main>
  <script src="../js/nav.js"></script>
</body>
</html>"""
    path = os.path.join(DOCS, filename)
    with open(path, 'w') as f:
        f.write(html)
    print(f"✅ {filename}")

def ss(label, desc=""):
    d = f'<div class="ss-desc">{desc}</div>' if desc else ""
    return f'<div class="screenshot-placeholder"><div class="ss-icon">📸</div><div class="ss-label">{label}</div>{d}</div>'

def ss_img(src, label):
    return f'<figure class="screenshot-figure"><img src="../img/{src}" alt="{label}" class="screenshot-img" loading="lazy"><figcaption>{label}</figcaption></figure>'

def note(label, body): return f'<div class="callout-note"><span class="callout-label">ℹ {label}</span><p>{body}</p></div>'
def warn(label, body): return f'<div class="callout-warning"><span class="callout-label">⚠ {label}</span><p>{body}</p></div>'
def tip(label, body):  return f'<div class="callout-tip"><span class="callout-label">💡 {label}</span><p>{body}</p></div>'
def imp(label, body):  return f'<div class="callout-important"><span class="callout-label">🚨 {label}</span><p>{body}</p></div>'

def table(headers, rows):
    ths = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join("<tr>"+"".join(f"<td>{c}</td>" for c in row)+"</tr>" for row in rows)
    return f"<table><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table>"

# ─── Build all pages ──────────────────────────────────────────────────────────

# OVERVIEW
page("Workshop Overview", "overview.html",
     "Objectives, prerequisites, structure, and how to complete the workshop",
     ["Getting Started", "30 min", "Reference"],
     None, None, None,
     """
      <h2>What You'll Learn</h2>
      <p>This workshop gives Anaplan delivery practitioners the skills to independently configure, deploy, and administer the Integrated Financial Planning (IFP) application v2.0 — from the Application Framework wizard through ADO data loading, post-generation setup, and all 7 planning module walkthroughs.</p>
      <ul>
        <li>Navigate the Application Framework configuration wizard and understand every question's implications</li>
        <li>Complete all required post-generation tasks to make an IFP deployment production-ready</li>
        <li>Build ADO transformation views and load source data into IFP models</li>
        <li>Configure and demo all 6 IFP planning modules plus Reporting &amp; Analysis</li>
        <li>Manage ongoing IFP administration — versions, planning methods, account settings</li>
        <li>Understand IFP's currency triangulation model</li>
        <li>Create custom planning methods and know when to extend vs. configure</li>
      </ul>

      <h2>Prerequisites</h2>
      <ul>
        <li>Anaplan model builder certification or equivalent experience</li>
        <li>Access to an IFP v2.0 workspace (your facilitator will provide credentials)</li>
        <li>Familiarity with basic Anaplan concepts: lists, modules, blueprints, actions, UX pages</li>
        <li>Basic understanding of financial planning (P&amp;L, Balance Sheet, Cash Flow)</li>
      </ul>

      <h2>Workshop Structure</h2>
      """ + table(
          ["Module", "Topic", "Format", "Approx. Time"],
          [
              ["Getting Started", "IFP overview, FictoCorp case study, Anaplan Way", "Read + Discuss", "30 min"],
              ["Module 1", "Application Framework, ADO, Model Architecture", "Presentation + Demo", "45 min"],
              ["Module 2", "Configuration Workshop — Labs A &amp; B", "Tell + Show + Do", "2.5 hrs"],
              ["Module 3", "7 Planning module walkthroughs", "Demo + Discussion", "90 min"],
              ["Module 4", "Admin runbook, currency, extensions", "Presentation", "30 min"],
              ["Reference", "Data flows, Q&amp;A, glossary, resources", "Self-service", "—"],
          ]
      ) + """
      <h2>How to Use This Guide</h2>
      <p>Each instructional page follows the <strong>Tell → Show → Do</strong> pattern. Start with the <a href="./case-study.html">Case Study</a> to understand FictoCorp Industries — the fictional company used in all exercises — then work through the modules in order.</p>
      """ + tip("Before You Start", "Confirm your workspace is provisioned and you have all 4 required roles: Application Owner, Workspace Admin, Page Builder, and Integration Admin. Generation will fail without all 4 roles."))

# CASE STUDY
page("Case Study: FictoCorp Industries", "case-study.html",
     "The fictional company used in every lab — profile, hierarchy, and your role",
     ["Getting Started", "Case Study", "10 min"],
     None, None, None,
     """
      <h2>Company Profile</h2>
      """ + table(["Attribute","Value"],[
          ["Industry","Global Manufacturing"],["Headquarters","San Francisco, CA"],
          ["Revenue","$450M annually"],["Employees","~500 (job-based headcount planning)"],
          ["Entities","FictoCorp USA · FictoCorp EMEA"],
          ["Departments","Sales &amp; Marketing · Operations · G&amp;A"],
          ["Products","Hardware (H1, H2) · Software (S1, S2)"],
          ["Customers","Enterprise · Commercial"],
          ["Base Currency","USD"],["Reporting Currencies","USD · EUR · GBP"],
          ["Planning Scope","Full 3-statement: Revenue/COGS + OpEx + HC + CapEx + BS/CF"],
      ]) + """
      <h2>Planning Challenges</h2>
      <p>FictoCorp is migrating to Anaplan IFP v2.0. Their pain points:</p>
      <ul>
        <li>Manual, disconnected P&amp;L and headcount planning — Finance and HR use separate spreadsheets</li>
        <li>No unified balance sheet view — cash flow is done in Excel after close</li>
        <li>CapEx tracked in a separate system with no P&amp;L linkage</li>
        <li>Multi-currency consolidation takes 3 days per cycle due to manual rate lookups</li>
        <li>Cannot model scenarios quickly enough for CFO weekly review</li>
      </ul>

      <h2>Hierarchy Structure</h2>
      <h3>Entity Hierarchy (2 levels)</h3>
      <ul><li>Total FictoCorp<ul><li>FictoCorp USA</li><li>FictoCorp EMEA</li></ul></li></ul>
      <h3>Department Hierarchy (3 levels)</h3>
      <ul><li>All Departments<ul>
        <li>Sales &amp; Marketing → Direct Sales · Marketing · Partner Sales</li>
        <li>Operations → Manufacturing · Supply Chain · Quality</li>
        <li>G&amp;A → Finance · HR · IT · Legal</li>
      </ul></li></ul>
      <h3>Product Hierarchy (2 levels)</h3>
      <ul><li>All Products<ul>
        <li>Hardware → H1 Industrial · H2 Commercial</li>
        <li>Software → S1 Platform License · S2 SaaS</li>
      </ul></li></ul>

      <h2>Your Role</h2>
      <p>You are an Anaplan implementation consultant engaged to deploy IFP v2.0 for FictoCorp. You will configure the Application Framework, set up ADO pipelines, and walk the FictoCorp finance team through their new planning environment.</p>
      """ + note("Lab A vs Lab B", "Lab A deploys Revenue/COGS + OpEx + HC only — no CapEx, no Balance Sheet. Lab B adds full 3-statement scope. Start with Lab A to learn the core configuration flow before adding complexity."))

# IFP OVERVIEW
page("IFP Suite Overview", "ifp-overview.html",
     "6 planning modules, key capabilities, and what changed in v2.0",
     ["Getting Started", "Foundation", "20 min"],
     ("What IFP Is", "The IFP suite: 6 modules, the problems it solves, and what's new in v2.0."),
     ("Instructor Demo", "Facilitator opens the IFP landing page and briefly tours the module categories and summary pages."),
     ("Navigate the App", "Log in to your IFP workspace and locate the landing page. Identify which module categories exist in the sidebar."),
     """
      <h2>What IFP Does</h2>
      <p>Integrated Financial Planning (IFP) v2.0 is Anaplan's application suite for the Office of the CFO — delivering comprehensive P&amp;L, cash flow, and balance sheet planning through a connected set of modules built on the Anaplan Application Framework and Polaris.</p>

      <h2>Problems IFP Solves</h2>
      """ + table(["Problem","How IFP Solves It"],[
          ["Inefficient Planning Cycles","Pre-built driver-based forecasting methods automate routine calculations"],
          ["Fragmented Enterprise Planning","Single connected platform — Revenue, OpEx, HC, CapEx, and BS in one place"],
          ["Reactive Decisions","Built-in scenario modeling and what-if analysis"],
          ["Delayed Time-to-Value","Deploy in 8–10 weeks using Application Framework best practices"],
          ["Rigid Systems","Configurable dimensions, planning methods, and extensible architecture"],
      ]) + """
      <h2>Six Planning Modules</h2>
      """ + table(["Module","What It Plans"],[
          ["💰 Revenue &amp; COGS","Revenue and margins by product, customer, entity — driver-based methods"],
          ["📊 Operating Expenses","OpEx by GL account — planning methods, line item detail, allocations"],
          ["👥 Headcount","Job-level workforce costs — pay bands, HC changes, cost sync to FP"],
          ["🏗 CapEx","Individual assets — depreciation, disposals, P&amp;L and BS impact"],
          ["📋 Balance Sheet &amp; CF","Working capital, funding logic, indirect cash flow — activity-based"],
          ["🎯 Top-Down Planning","Executive targets for revenue, margin, OpEx, FTE — vs. bottom-up"],
      ]) + """
      <p>Plus: <strong>Reporting &amp; Analysis</strong> — consolidated IS, BS, CF reports, variance analysis, statistical analysis, and management reporting pack.</p>

      <h2>What's New in v2.0</h2>
      """ + table(["Feature","What It Means"],[
          ["Anaplan Application Framework","Upgradeable, centrally-deployed app — replaces static v1.x configurator"],
          ["Anaplan Data Orchestrator (ADO)","Replaces the data hub model — lightweight, high-performance pipelines"],
          ["Job-Based Headcount","Plans at role level, not employee — protects PII, enables OWP integration"],
          ["Progressive Disclosure UI","Shows only relevant inputs per planning method — reduces errors"],
          ["Re-architected Models","Polaris engine: superior performance for large data volumes"],
      ]) + imp("Customer Exclusion Criteria", "IFP v2.0 is NOT suitable for: customers requiring BYOK on public cloud, customers who cannot use AWS (ADO requirement), public sector/federal organizations, or customers requiring more than 8 dimensions."))

# ANAPLAN WAY
page("The Anaplan Way for Applications", "anaplan-way.html",
     "Implementation methodology, delivery phases, and provisioning requirements",
     ["Getting Started", "Foundation", "20 min"],
     ("The Delivery Framework", "The 6-phase delivery process and how IFP fits within it."),
     ("Instructor Walkthrough", "Facilitator walks through the delivery framework slide and maps each phase to IFP-specific activities."),
     ("Map FictoCorp", "Looking at FictoCorp's requirements — which delivery phase are we in? What needs to happen in each phase?"),
     """
      <h2>The Delivery Process Framework</h2>
      """ + ss("Anaplan Way for Applications — 6-phase delivery framework") + """
      <ol>
        <li><strong>Requirements</strong> — Architect and customer agree on scope, dimensions, modules, and configuration choices</li>
        <li><strong>Configure</strong> — Run the Application Framework wizard; answer all configuration questions</li>
        <li><strong>Generate</strong> — Application models and UX are generated; review generation logs and fix issues</li>
        <li><strong>Data Load &amp; Publish</strong> — Import source data via ADO, sync with spoke models, validate</li>
        <li><strong>Application Ready</strong> — UAT, user training, go-live sign-off</li>
        <li><strong>Extend &amp; Expand</strong> — Customer extends functionality, adds more applications, refines over time</li>
      </ol>

      <h2>IFP-Specific Delivery Phases</h2>
      """ + table(["Phase","Key Activities","Responsible"],[
          ["Discover","Requirements gathering, exclusion checklist, dimension decisions, scope agreement","Partner + Customer"],
          ["Configure","Run App Framework wizard, answer all config questions, set hierarchy levels","Partner (with Anaplan PS support)"],
          ["Generate","Deploy models via PAF, review logs, fix known generation issues","Partner"],
          ["Post-Generation","Time/version setup, ADO pipelines, data load, UX validation, delete DEMO actions","Partner"],
          ["Test","UAT with customer, data validation, variance checks, user training","Partner + Customer"],
          ["Go-Live","Promote Dev → Prod via ALM, hand over admin responsibilities","Partner + Customer"],
          ["Expand","Extensions, additional modules, or new applications","Customer + Partner"],
      ]) + """
      <h2>Provisioning Requirements</h2>
      <p>Before configuring, ensure the following:</p>
      <ul>
        <li>Polaris workspace provisioned (minimum 100GB) — request via CSBP in Salesforce</li>
        <li>Delivery Request created in Salesforce (Application Delivery #1, #2, or #3)</li>
        <li>Finance Apps CoE added to workspace — email <strong>financeapplications@anaplan.com</strong></li>
      </ul>
      <p>The generating user must have <strong>all 4 roles</strong> in the tenant:</p>
      """ + table(["Role","Purpose"],[
          ["Application Owner","Access to Applications URL"],
          ["Workspace Admin","Full model access for generation"],
          ["Page Builder","UX page creation and editing"],
          ["Integration Admin*","ADO and data integration — must generate in default tenant"],
      ]) + imp("Partner Tenant Requirement", "Integration Admins can only generate in their default tenant. If you are a partner, work with your customer to obtain an Anaplan account whose default tenant is the customer's environment before attempting generation."))

# APP FRAMEWORK
page("Anaplan Application Framework", "app-framework.html",
     "How deployment works, the 4 generated models, and the configuration question flow",
     ["Module 1", "Platform Foundations", "30 min"],
     ("What AAF Does", "The Application Framework provisions, generates, and manages upgrades of all 4 IFP models from a single configuration session."),
     ("Instructor Demo", "Facilitator opens the Application Framework and shows the question flow structure before answering any questions."),
     ("Explore the Wizard", "Open the Application Framework in your workspace. Navigate to the Top-Level Questions — identify which dimensions are optional vs. mandatory."),
     """
      <h2>What the Application Framework Does</h2>
      <ul>
        <li><strong>Generates</strong> all 4 IFP models (Admin, FP, HC, CE) based on configuration answers</li>
        <li><strong>Provisions</strong> UX pages, modules, lists, actions, and ADO links automatically</li>
        <li><strong>Enables upgrades</strong> — future versions deployed centrally without manual rebuilds</li>
        <li><strong>Enforces constraints</strong> — validates configuration choices (e.g., 8-dimension limit)</li>
      </ul>

      <h2>The Four Generated Models</h2>
      """ + table(["Model","Purpose","Always Generated?"],[
          ["Admin","Central configuration layer — source-to-planning mappings, metadata","Yes — always"],
          ["Financial Planning (FP)","Revenue/COGS, OpEx, Balance Sheet, Cash Flow, Top-Down, Reporting","Yes — always"],
          ["Headcount (HC)","Job-level workforce planning and cost calculations","Yes — delete if choosing GL-level option"],
          ["Capital Expense (CE)","Asset planning, depreciation, disposal modeling","Yes — delete if choosing GL-level option"],
      ]) + warn("Cannot Exclude Models from Generation", "The Application Framework always generates all 4 models. If you choose GL-level planning for HC or CapEx instead of the dedicated model, the model is still generated — you must delete it manually after generation.") + """
      <h2>Configuration Question Structure</h2>
      """ + ss_img("introduction-and-navigation-2.jpg", "IFP v2.0 UX — page navigation structure showing module categories") + """
      <p>The wizard has two layers:</p>
      <ol>
        <li><strong>Top-Level Questions</strong> — define foundational structure across all 4 models: which dimensions to include, which modules to deploy, multi-currency, headcount approach, CapEx approach</li>
        <li><strong>Model-Specific Questions</strong> — fine-tune each model: FP planning scope, HC settings, CE settings</li>
      </ol>
      <p>Between the two layers: the <strong>Hierarchy Configuration screen</strong> — where you set level counts and rename each hierarchy before generation.</p>

      <h2>Hierarchy Configuration</h2>
      <ul>
        <li>Add, delete, or rename hierarchy levels across all models at once</li>
        <li>Changes propagate automatically to all models where the hierarchy is used</li>
        <li><strong>Minimum 2 levels, maximum 8 levels per model</strong></li>
        <li>Level count shown = combined levels across all selected models (Entity at 3 levels in FP + HC + CE = 9 total)</li>
      </ul>
      """ + warn("Naming Convention Is Critical", "Use the EXACT same name in the configuration question response AND the hierarchy rename. A mismatch causes generation failures where modules and line items won't be renamed correctly throughout the model.") + """
      <h2>After Generation</h2>
      <p>Generation is the starting point — a significant set of post-generation tasks are required before the application is usable. See <a href="./post-generation.html">Post-Generation Checklist</a> for the full list.</p>
      """ + note("Known Generation Issues", "The Application Framework has documented known issues — ADO links that fail to generate, UX elements that don't generate correctly, and naming inconsistencies. All have workarounds. None are blockers — plan for them in your project schedule."))

# ADO OVERVIEW
page("Anaplan Data Orchestrator (ADO)", "ado-overview.html",
     "How ADO replaces the data hub, source-to-planning mapping, and the transformation view pattern",
     ["Module 1", "Platform Foundations", "30 min"],
     ("What ADO Does in IFP", "ADO replaces the data hub model from v1.x — handling all master data and actuals loading through lightweight, centralized pipelines."),
     ("Instructor Demo", "Facilitator opens ADO and shows the Source Data, Links, and Transformation Views tabs. Walks through one example link."),
     ("Identify Your Links", "In your workspace ADO dataspace, how many links can you find? Which models do they push data to?"),
     """
      <h2>What ADO Replaces</h2>
      """ + table(["v1.x Approach","v2.0 ADO Approach"],[
          ["Large data hub model consuming workspace memory","Lightweight mapping model — no memory overhead in workspace"],
          ["Manual import actions into data hub","ADO links push data directly to spoke models"],
          ["Source mappings in data hub model","Mappings maintained in Admin model, consumed by ADO at load time"],
          ["Separate admin model for master data","Admin model is the mapping workbench; ADO is the pipeline"],
      ]) + """
      <h2>ADO Architecture in IFP</h2>
      """ + ss_img("back-end-information-2.jpg", "IFP v2.0 backend setup — model structure and ADO connections") + """
      <h3>Two Types of ADO Loads</h3>
      <ol>
        <li><strong>Direct loads</strong> — load source data as-is (hierarchies, flat lists that don't need planning mappings). Set up once and reuse without transformation.</li>
        <li><strong>Transformation loads</strong> — require alignment with planning structures before loading. These use transformation views to join source data with planning mappings from the Admin model.</li>
      </ol>

      <h2>Source-to-Planning Mapping Flow</h2>
      <ol>
        <li>Load raw source data (accounts, departments, entities) into Admin model via ADO</li>
        <li>Map source items to planning items in the Admin model UX (Source → Planning)</li>
        <li>Re-sync Admin model datasets in ADO to pick up the updated mappings</li>
        <li>Push planning structures to all spoke models via ADO links</li>
      </ol>
      """ + tip("Always Map Before Loading", "Complete all source-to-planning mappings in the Admin model before pushing actuals to spoke models. Unmapped items will cause blank reports and missing data throughout FP, HC, and CE.") + """
      <h2>Transformation Views for Actuals</h2>
      <p>Loading actuals (trial balance, HRIS data) requires transformation views that join source data with planning mappings:</p>
      <ol>
        <li>Upload source actuals file (e.g., Trial Balance IS) to ADO Source Data</li>
        <li>Bring in mapping datasets from Admin model: <code>SYS by Source Account IS Flat</code>, <code>SYS by Source Department Flat</code>, <code>SYS by Source Entity Flat</code></li>
        <li>Create leaf-level transformation views from each mapping dataset (filter: Is Leaf Level = true)</li>
        <li>Join mapping views to source file — adds planning codes to the source data</li>
        <li>Create final clean view with only required columns; change Ending Balance to float, Time Period to date</li>
        <li>Enable aggregation — combines source records mapping to the same planning dimension</li>
        <li>Map to the ADO link and push to the spoke model</li>
      </ol>
      """ + note("Same Pattern for All Actuals", "This transformation view pattern is identical for Trial Balance IS, Trial Balance BS, Trial Balance by Margin, BS Subledger, and HRIS Actuals. Only the source file columns change.") + """
      <h2>⚠️ Known Broken ADO Links</h2>
      """ + warn("These Must Be Created Manually", "The following ADO links are documented as broken or missing out of the box in IFP v2.0.0:<br><br><strong>Financial Planning:</strong> Vendor Hierarchy<br><strong>Headcount:</strong> SYS by J2 Job · SYS by J3 Job · SYS by J4 Job (no link generated at all) · Job Grade<br><br>Create all 5 manually using the ADO setup steps in the Configuration Guide before attempting data loads."))

# MODEL ARCHITECTURE
page("Model Architecture", "model-architecture.html",
     "The 4 IFP models, how they connect, and key architectural decisions",
     ["Module 1", "Platform Foundations", "20 min"],
     ("The 4-Model Architecture", "How Admin, FP, HC, and CE work together and where data flows between them."),
     ("Model Tour", "Facilitator opens the Anaplan workspace and shows each of the 4 models — their key modules and how they are structured."),
     ("Identify Data Flows", "Look at the FIN – Import from HC Model and FIN – Import from CapEx Model actions in the FP model. What do they do and when should they run?"),
     """
      <h2>The Four Models</h2>
      """ + ss_img("back-end-information-1.jpg", "IFP v2.0 back-end — model structure and connections") + table(["Model","Role","Key Contents"],[
          ["Admin","Central hub — master data &amp; mappings","Source lists, planning hierarchies, source-to-planning mapping pages"],
          ["Financial Planning (FP)","Core planning hub","Revenue/COGS, OpEx, Balance Sheet, Cash Flow, Top-Down, Reporting"],
          ["Headcount (HC)","Workforce planning spoke","Job library, pay bands, HC planning inputs, cost calculations"],
          ["Capital Expense (CE)","CapEx planning spoke","Asset purchases, depreciation, disposals, net fixed asset roll-forward"],
      ]) + """
      <h2>Data Flow Between Models</h2>
      <ul>
        <li><strong>Admin → All Spokes (via ADO):</strong> Planning hierarchies (Entity, Dept, IS/BS accounts) pushed to FP, HC, CE</li>
        <li><strong>HC → FP:</strong> Workforce costs imported via <em>FIN – Import from HC Model</em> action in FP Admin</li>
        <li><strong>CE → FP:</strong> CapEx depreciation and asset values imported via <em>FIN – Import from CapEx Model</em> action in FP Admin</li>
        <li><strong>FP → Reporting:</strong> All P&amp;L, BS, and CF data consolidated in FP's Reporting &amp; Analysis module</li>
      </ul>
      """ + imp("Cross-Model Import Reminder", "After making changes in HC or CE models, you MUST run the cross-model import action in FP Admin. Changes do NOT flow automatically. This is the most common cause of 'missing data' issues — always check this first.") + """
      <h2>Architectural Decisions</h2>
      """ + table(["Decision","Rationale"],[
          ["Native Versions","Enables switchover dates, CURRENTVERSION() functions, formula scope, and bulk copy actions"],
          ["No subsets for planning","Maximizes Polaris model performance"],
          ["ADO links replace import actions","Greater data control, eliminates data hub memory overhead in workspace"],
          ["Entity-level only for CapEx/BS","Performance optimization — operational dimensions not needed for these modules"],
      ]) + """
      <h2>Dimensions</h2>
      <h3>Required (all modules)</h3>
      <p>Time &nbsp;·&nbsp; Account &nbsp;·&nbsp; Version &nbsp;·&nbsp; Entity</p>
      <h3>Optional (configurable per implementation)</h3>
      """ + table(["Dimension","Used In","Configurable Name?"],[
          ["Department","Revenue/COGS, OpEx, HC, Top-Down","Yes — e.g., 'Cost Center', 'Division'"],
          ["Geography","Revenue/COGS, OpEx, Top-Down","Yes — e.g., 'Region', 'Location'"],
          ["Product","Revenue/COGS, Top-Down","Yes — e.g., 'SKU', 'Service'"],
          ["Customer","Revenue/COGS, Top-Down","Yes — e.g., 'Client', 'Buyer'"],
          ["Functional Area","OpEx, Top-Down","Yes — e.g., 'Workstream'"],
          ["Vendor","OpEx","Yes — e.g., 'Supplier'"],
      ]) + warn("8-Dimension Hard Limit", "IFP v2.0 supports a maximum of 8 dimensions. Customers requiring more than 8 need a bespoke model build as an extension. Always validate dimension count during the requirements phase."))

print("Getting Started + Module 1 done.")
