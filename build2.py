#!/usr/bin/env python3
"""IFP Workshop Builder — Module 1-4 + Reference pages"""
import os, sys
sys.path.insert(0, '/home/gstoa/.openclaw/workspace/projects/work/workshops/ifp-workshop')
from build import page, write, callout, screenshot, table, build_nav, build_prevnext

# ─── Module 1: Platform Foundations ──────────────────────────────────────────

write("app-framework.html", page("Anaplan Application Framework", "./app-framework.html", """
<h1>Anaplan Application Framework</h1>
<p>The Application Framework (AAF) is the deployment mechanism for IFP v2.0. It provisions and generates the complete IFP application package based on a series of configuration responses — replacing the static, one-time configurator from v1.x.</p>

<h2>What the Application Framework Does</h2>
<ul>
  <li><strong>Generates</strong> all 4 IFP models (Admin, Financial Planning, Headcount, CapEx) based on your configuration answers</li>
  <li><strong>Provisions</strong> UX pages, modules, lists, and ADO links automatically</li>
  <li><strong>Enables upgrades</strong> — future versions can be deployed centrally without manual rebuilds</li>
  <li><strong>Validates</strong> configuration choices and enforces constraints (e.g., max 8 dimensions)</li>
</ul>

<h2>The Four Generated Models</h2>
""" + table(
    ["Model", "Purpose", "Always Generated?"],
    [
        ["Admin", "Central configuration layer — source-to-planning mappings, metadata", "Yes"],
        ["Financial Planning (FP)", "Revenue/COGS, OpEx, Balance Sheet, Cash Flow, Top-Down", "Yes"],
        ["Headcount (HC)", "Job-level workforce planning and cost calculations", "Yes (delete if not using HC model option)"],
        ["Capital Expense (CE)", "Asset planning, depreciation, disposal modeling", "Yes (delete if not using CE model option)"],
    ]
) + callout("note", "Model Generation Behavior", "The Application Framework cannot completely exclude a model from generation. If you choose 'GL-level planning' for HC or CapEx instead of the dedicated model, both models are still generated — you must delete the unused model manually after generation.") + """
<h2>Configuration Question Flow</h2>
""" + screenshot("Application Framework — interview-style configuration wizard showing question categories") + """
<p>The wizard is divided into two layers:</p>
<ol>
  <li><strong>Top-Level Questions</strong> — define foundational structure across all 4 models (dimensions, modules to include, multi-currency, headcount/CapEx approach)</li>
  <li><strong>Model-Specific Questions</strong> — fine-tune each model's configuration (FP planning scope, HC model settings, CE model settings)</li>
</ol>
<p>Between the two layers sits the <strong>Hierarchy Configuration screen</strong> — where you set the number of levels and rename each hierarchy before generating.</p>

<h2>Hierarchy Configuration</h2>
<ul>
  <li>Add levels, delete levels, or rename hierarchy levels across all models at once</li>
  <li>Changes propagate automatically to all models where the hierarchy is used</li>
  <li><strong>Minimum 2 levels, maximum 8 levels per model</strong></li>
  <li>Number of levels shown = combined levels across all selected models (e.g., Entity at 3 levels in FP + HC + CE = 9 total)</li>
</ul>
""" + callout("warning", "Naming Convention Is Critical", "Use the EXACT same name for the hierarchy configuration AND the rename field. The name must proliferate throughout all models — a mismatch causes generation issues.") + """
<h2>After Generation</h2>
<p>Generation is just the beginning. A significant set of post-generation tasks are required before the application is usable. See <a href="./post-generation.html">Post-Generation Checklist</a> for the full list.</p>
""" + callout("important", "Known Generation Issues", "The Application Framework has documented known issues — ADO links that fail to generate, UX elements that don't generate correctly, and naming inconsistencies. All have workarounds. See Post-Generation Checklist for the complete list.")))

write("ado-overview.html", page("Anaplan Data Orchestrator (ADO)", "./ado-overview.html", """
<h1>Anaplan Data Orchestrator (ADO)</h1>
<p>ADO is Anaplan's native data integration layer. In IFP v2.0, it replaces the large, complex data hub model from v1.x — handling all master data setup and actuals loading through a lightweight, centralized pipeline architecture.</p>

<h2>What ADO Replaces</h2>
""" + table(
    ["v1.x Approach", "v2.0 ADO Approach"],
    [
        ["Large data hub model consuming workspace memory", "Lightweight mapping model — no memory overhead"],
        ["Manual import actions into data hub", "ADO links push data directly to spoke models"],
        ["Source mappings configured in data hub model", "Mappings maintained in Admin model, consumed by ADO at load time"],
        ["Separate admin model for master data", "Admin model is the mapping workbench — ADO is the pipeline"],
    ]
) + """
<h2>ADO Architecture in IFP</h2>
""" + screenshot("ADO architecture diagram — source files → Admin model → ADO pipelines → FP/HC/CE spoke models") + """
<h3>Two Types of ADO Loads</h3>
<ol>
  <li><strong>Direct loads</strong> — load source data as-is (hierarchies and flat lists that don't need planning mappings). Set up once and reuse.</li>
  <li><strong>Transformation loads</strong> — require alignment with planning structures before loading. These use transformation views to join source data with planning mappings from the Admin model.</li>
</ol>

<h2>Source-to-Planning Mapping Flow</h2>
<ol>
  <li>Load raw source data (accounts, departments, entities) into Admin model via ADO</li>
  <li>Map source items to planning items in the Admin model UX (Source → Planning)</li>
  <li>Re-sync Admin model datasets in ADO</li>
  <li>Push planning structures to all spoke models via ADO</li>
</ol>
""" + callout("tip", "Always Map Before Loading", "Complete all source-to-planning mappings in the Admin model before pushing to spoke models. Unmapped items will cause blank reports in FP, HC, and CE.") + """
<h2>ADO Transformation Views for Actuals</h2>
<p>Loading actuals (trial balance data, HRIS data) requires transformation views in ADO:</p>
<ol>
  <li>Upload source file (e.g., Trial Balance IS CSV) to ADO Source Data</li>
  <li>Bring in mapping datasets from Admin model (SYS by Source Account IS, Source Department, Source Entity)</li>
  <li>Create leaf-level mapping transformation views (filter: Is Leaf Level = true)</li>
  <li>Join mapping views to source file — adds Planning codes to source data</li>
  <li>Create final clean transformation view keeping only required columns</li>
  <li>Enable aggregation — combines source records that map to same planning dimension</li>
  <li>Map to ADO link and push to spoke model</li>
</ol>
""" + callout("note", "Same Pattern for All Actuals", "The transformation view pattern is identical for Trial Balance IS, Trial Balance BS, Trial Balance by Margin, BS Subledger, and HRIS Actuals — only the source file and column names change.") + """
<h2>Complete ADO Link Reference</h2>
<h3>Admin Model (4 links)</h3>
<ul>
  <li>Source Account IS — IFP_DH_Source Account IS.csv</li>
  <li>Source Account BS — IFP_DH_Source Account BS.csv</li>
  <li>Source Entity — IFP_DH_Source Entity.csv</li>
  <li>Source Department — IFP_DH_Source Department.csv</li>
</ul>
<h3>All Spoke Models (3 links each)</h3>
<ul>
  <li>FX Currency — IFP_SH_FX Currency.csv</li>
  <li>FX Rates — IFP_SH_FX_Rates.csv</li>
  <li>Reporting Currency — IFP_SH_Reporting Currency.csv</li>
</ul>
<h3>Financial Planning (23 links)</h3>
<p>Product, Customer, Geography, Functional Area, Vendor hierarchies + SYS modules + CF hierarchy + Trial Balance IS/BS/Margin</p>
<h3>CapEx (3 links)</h3>
<p>Asset Type, Trial Balance BS Subledger, Existing Asset Depreciation</p>
<h3>Headcount (8 links)</h3>
<p>Job Hierarchy + SYS by J1–J4 Job, Job Grade, Employment Types, HRIS Actuals</p>
""" + callout("warning", "⚠️ Known Broken ADO Links", "The following ADO links are documented as broken or missing out of the box and must be created manually: <strong>Vendor Hierarchy</strong> (FP), <strong>SYS by J2 Job</strong> (HC), <strong>SYS by J3 Job</strong> (HC), <strong>SYS by J4 Job</strong> (HC — no link generated), <strong>Job Grade</strong> (HC). Create these manually using the Config Guide ADO setup steps.")))

write("model-architecture.html", page("Model Architecture", "./model-architecture.html", """
<h1>Model Architecture</h1>
<p>IFP v2.0 is built on four Anaplan models that work together as a connected planning suite. Understanding how they relate is essential for configuration, data loading, and troubleshooting.</p>

<h2>The Four Models</h2>
""" + screenshot("IFP v2.0 model architecture diagram — Admin hub feeding FP, HC, CE spoke models") + """
""" + table(
    ["Model", "Role", "Key Contents"],
    [
        ["Admin", "Central hub — master data &amp; mappings", "Source lists, planning hierarchies, source-to-planning mapping pages"],
        ["Financial Planning (FP)", "Core planning hub", "Revenue/COGS, OpEx, Balance Sheet, Cash Flow, Top-Down, Reporting"],
        ["Headcount (HC)", "Workforce planning spoke", "Job library, pay bands, HC planning inputs, cost calculations"],
        ["Capital Expense (CE)", "CapEx planning spoke", "Asset purchases, depreciation, disposals, net fixed asset roll-forward"],
    ]
) + """
<h2>Data Flow Between Models</h2>
<ul>
  <li><strong>Admin → All Spokes (via ADO):</strong> Planning hierarchies (Entity, Dept, IS accounts, BS accounts) pushed to FP, HC, CE</li>
  <li><strong>HC → FP:</strong> Workforce costs imported via <em>FIN – Import from HC Model</em> action</li>
  <li><strong>CE → FP:</strong> CapEx depreciation and asset values imported via <em>FIN – Import from CapEx Model</em> action</li>
  <li><strong>FP → Reporting:</strong> All P&amp;L, BS, and CF data consolidated in FP's Reporting &amp; Analysis module</li>
</ul>
""" + callout("important", "Cross-Model Import Reminder", "After making changes in the HC or CapEx model, you must manually run the import action in the FP Admin pages to sync data. Changes do NOT flow automatically — this is a common source of 'missing data' issues.") + """
<h2>Architectural Decisions</h2>
""" + table(
    ["Decision", "Rationale"],
    [
        ["Native Versions", "Enables switchover dates, CURRENTVERSION() functions, formula scope, and bulk copy"],
        ["No subsets for planning", "Maximizes Polaris model performance"],
        ["ADO links replace import actions", "Greater data control, eliminates data hub memory usage"],
        ["Entity-level only for CapEx/BS", "Performance — operational dimensions (dept, geo) not needed for these modules"],
    ]
) + """
<h2>Dimensions Overview</h2>
<h3>Required Dimensions (all modules)</h3>
<p>Time · Account · Version · Entity</p>
<h3>Optional Dimensions (configurable per implementation)</h3>
""" + table(
    ["Dimension", "Used In", "Configurable Name"],
    [
        ["Department", "Revenue/COGS, OpEx, HC, Top-Down", "Yes — e.g., 'Cost Center', 'Division'"],
        ["Geography", "Revenue/COGS, OpEx, Top-Down", "Yes — e.g., 'Region', 'Location'"],
        ["Product", "Revenue/COGS, Top-Down", "Yes — e.g., 'SKU', 'Service'"],
        ["Customer", "Revenue/COGS, Top-Down", "Yes — e.g., 'Client', 'Buyer'"],
        ["Functional Area", "OpEx, Top-Down", "Yes — e.g., 'Workstream'"],
        ["Vendor", "OpEx", "Yes — e.g., 'Supplier'"],
    ]
) + callout("warning", "8-Dimension Hard Limit", "IFP v2.0 supports a maximum of 8 dimensions for the application. Customers requiring more than 8 dimensions will need a bespoke model build as an extension. Validate dimension count before configuring.")))

print("Module 1 done.")
