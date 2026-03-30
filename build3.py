#!/usr/bin/env python3
"""IFP Workshop Builder — Module 2: Configuration Workshop"""
import os, sys
sys.path.insert(0, '/home/gstoa/.openclaw/workspace/projects/work/workshops/ifp-workshop')
from build import page, write, callout, screenshot, table

write("config-walkthrough.html", page("Application Framework Walkthrough", "./config-walkthrough.html", """
<h1>Application Framework Walkthrough</h1>
<p>This page walks through every configuration question in the Application Framework wizard — what each question means, what options are available, and the implications of each choice. Read this before attempting Lab A.</p>

<h2>Top-Level Configuration Questions</h2>
<p>These questions define the foundational structure applied across all 4 models.</p>

<h3>Entity Dimension</h3>
""" + table(
    ["Setting", "Details"],
    [
        ["What is it?", "Mandatory — your primary organizational hierarchy (e.g., Business Unit, Company, Legal Entity)"],
        ["What to configure", "Name (capital letter version + lowercase version) + number of levels in hierarchy screen"],
        ["Impact", "Used in Admin, FP, HC, CE — core dimension for all aggregation and reporting"],
        ["⚠️ Critical", "Must use the EXACT same name in both the question response and the hierarchy rename — mismatches break generation"],
    ]
) + """
<h3>Department Dimension</h3>
""" + table(
    ["Option", "Implication"],
    [
        ["Yes — include Department", "Separate dept hierarchy created in all models. Enables 2D planning (entity × dept). Increases model size."],
        ["No — exclude Department", "Simpler model. Planning only by Entity. Choose this for simple/small implementations."],
    ]
) + """
<h3>Optional Dimensions</h3>
""" + table(
    ["Dimension", "Used In", "Yes — Include?", "No — Exclude?"],
    [
        ["Geography", "Revenue/COGS, OpEx, Top-Down", "Multi-dimensional planning; increases complexity", "Simpler model; less dimensional granularity"],
        ["Functional Area", "OpEx", "Enables OpEx by function/workstream", "OpEx by dept only"],
        ["Vendor", "OpEx", "Enables vendor-level expense tracking", "No vendor dimension in OpEx"],
    ]
) + callout("warning", "Removing Dimensions Later", "Removing a dimension after generation reduces dimensionality across ALL areas of the model where it is used. Dimension decisions are best made upfront — changing them later requires re-generation.") + """
<h3>Headcount Planning Approach</h3>
""" + table(
    ["Option", "What Gets Deployed", "When to Choose"],
    [
        ["Option A: IFP Role-Based HC Model", "FP + HC models. Detailed job-level HC planning flows into FP.", "Default choice for most implementations. Best practice."],
        ["Option B: GL-Level Planning in FP", "FP + HC generated, HC deleted after. HC-driven costs entered at GL account level in FP.", "Simpler — for customers who don't need job-level detail."],
        ["Option C: External Model → Load to FP", "FP + HC generated, HC deleted. Summarized HC data loaded from OWP or external system.", "When OWP or another Anaplan model is the HC system of record."],
    ]
) + """
<h3>Multi-Currency</h3>
""" + table(
    ["Option", "Implication"],
    [
        ["Yes", "Reporting Currency dimension added; FX rates required; currency triangulation enabled"],
        ["No", "Single currency model; simpler but not suitable for international organizations"],
    ]
) + """
<h3>Balance Sheet &amp; Cash Flow</h3>
""" + table(
    ["Setting", "Options"],
    [
        ["Balance Sheet in FP?", "Yes = Admin + FP include BS accounts and logic. No = P&amp;L and/or CF only."],
        ["Cash Flow Reporting?", "Yes = indirect cash flow statement generated from IS + BS activity. No = CF excluded."],
    ]
) + """
<h3>CapEx Planning Approach</h3>
""" + table(
    ["Option", "What Gets Deployed", "When to Choose"],
    [
        ["Option A: IFP CapEx Model", "FP + CE models. Detailed asset-level CapEx flows into FP.", "Asset-intensive businesses needing depreciation modeling."],
        ["Option B: GL-Level Planning in FP", "FP + CE generated, CE deleted. CapEx at GL account level in FP.", "Simple CapEx needs without asset-level detail."],
        ["Option C: External Model → Load to FP", "FP + CE generated, CE deleted. Summarized CapEx loaded externally.", "When another system manages CapEx and IFP just needs the totals."],
    ]
) + """
<h2>Financial Planning Model Questions</h2>

<h3>Margin Planning Approach</h3>
""" + table(
    ["Option", "Description"],
    [
        ["In FP Only", "Full Revenue/COGS planning within the FP model"],
        ["In Another Model → Load to FP", "Consensus Margin Planning (CMP) or external; results loaded in via DAT Margin Planning Import"],
        ["Combination", "Some margin planning in FP, some loaded from external"],
        ["Expense Only", "All margin components excluded; FP focuses on OpEx only"],
    ]
) + """
<h3>Expense Planning Questions</h3>
<ul>
  <li><strong>Expense Planning in FP?</strong> — Yes includes OpEx modules; No excludes them entirely</li>
  <li><strong>Expense dimensionality</strong> — select which optional dimensions apply to OpEx planning</li>
  <li><strong>Itemized expense dimensionality</strong> — should match expense dimensionality for consistency</li>
  <li><strong>Expense allocations?</strong> — Yes includes allocation definition and basis input modules (adds complexity)</li>
</ul>

<h2>Hierarchy Configuration Screen</h2>
""" + screenshot("Hierarchy Configuration screen — showing Entity, Dept, Product hierarchies with level settings") + """
<ul>
  <li>Accessed between Top-Level and Model-Specific questions</li>
  <li>Set number of levels (min 2, max 8 per model) for each composite hierarchy</li>
  <li>Rename hierarchies here — must match name entered in the question above</li>
  <li>Changes propagate to all models using that hierarchy</li>
</ul>
""" + callout("tip", "FictoCorp Configuration Preview", "For Lab A: Entity = 2 levels, Department = 3 levels, Product = 2 levels, Customer = 2 levels. No Geography, Vendor, or Functional Area. HC: Option A (IFP HC model). No CapEx, No Balance Sheet. Multi-currency: Yes.")))

write("lab-a.html", page("Lab A: Configure FictoCorp", "./lab-a.html", """
<h1>Lab A: Configure FictoCorp Industries</h1>
<div class="lab-banner">
  <span class="lab-type">🔬 Hands-On Lab</span>
  <span class="lab-duration">⏱ Estimated time: 45–60 minutes</span>
</div>

<h2>Objectives</h2>
<p>By the end of this lab you will be able to:</p>
<ul>
  <li>Navigate the Application Framework configuration wizard end-to-end</li>
  <li>Answer all Top-Level and FP configuration questions for a real customer scenario</li>
  <li>Configure the hierarchy screen with correct levels and naming</li>
  <li>Generate the IFP application and review the generation logs</li>
</ul>

<h2>Customer Requirements Brief — FictoCorp Phase 1</h2>
""" + callout("note", "Scope for Lab A", "Phase 1 deploys Revenue/COGS + OpEx + Headcount only. No CapEx model, no Balance Sheet. Lab B adds full 3-statement scope.") + """
""" + table(
    ["Requirement", "Decision"],
    [
        ["Entity name", "Entity (2 levels: Total FictoCorp → USA / EMEA)"],
        ["Department", "Yes — 'Department' (3 levels: All Depts → Function → Cost Center)"],
        ["Geography", "No — exclude"],
        ["Functional Area", "No — exclude"],
        ["Vendor", "No — exclude"],
        ["Headcount", "Option A: IFP Role-Based HC Model"],
        ["Multi-currency", "Yes — USD base, USD/EUR/GBP reporting"],
        ["Balance Sheet", "No — exclude for Phase 1"],
        ["Cash Flow", "No — exclude for Phase 1"],
        ["CapEx", "Option B: GL-Level in FP (delete CE after generation)"],
        ["Margin planning", "In FP only"],
        ["Product dimension", "Yes — 'Product' (2 levels: All Products → Hardware / Software)"],
        ["Customer dimension", "Yes — 'Customer' (2 levels: All Customers → Enterprise / Commercial)"],
        ["IS list name", "Planning Account IS Hierarchy (default)"],
        ["Expense planning", "Yes — dimensionality: Entity + Department"],
        ["Expense allocations", "No — exclude"],
    ]
) + """
<h2>Lab Steps</h2>
<ol>
  <li><strong>Navigate to the Application Framework</strong> — log in to your IFP workspace and open the Application Framework configurator</li>
  <li><strong>Answer Top-Level questions</strong> — use the requirements table above. Pay close attention to naming conventions.</li>
  <li><strong>Open the Hierarchy Configuration screen</strong> — set Entity to 2 levels, Department to 3 levels, rename both to match your question responses exactly</li>
  <li><strong>Answer FP model questions</strong> — margin in FP, Product (2 levels), Customer (2 levels), expense planning with Entity + Department dimensionality</li>
  <li><strong>Answer HC model questions</strong> — multi-currency: Yes, IS list name: default, Department: Yes, Job term: Job (default)</li>
  <li><strong>Generate the application</strong> — click Generate and monitor the generation logs</li>
  <li><strong>Review generation logs</strong> — identify any errors or warnings. Note which items failed to generate.</li>
  <li><strong>Delete the CE model</strong> — since we chose GL-level CapEx, the generated CE model is not needed</li>
</ol>

""" + screenshot("Application Framework wizard — Top-Level question screen") + """
""" + screenshot("Hierarchy Configuration screen — Entity 2 levels, Department 3 levels") + """
""" + screenshot("Generation success screen — showing all 4 models generated") + """

<h2>Debrief Questions</h2>
<ol>
  <li>What happens if the Entity name in the configuration question doesn't match the name in the Hierarchy Configuration screen?</li>
  <li>Why did we choose Option A for Headcount but Option B for CapEx?</li>
  <li>If FictoCorp later decides they need to add a Geography dimension, what would be the impact?</li>
  <li>What is the minimum number of hierarchy levels allowed? Maximum?</li>
  <li>Why does the Application Framework generate a CE model even when we selected GL-level CapEx?</li>
</ol>

""" + callout("tip", "Generation Issues?", "If generation fails, check: (1) do you have all 4 required roles, (2) are you in your default tenant, (3) check the configuration logs in PAF to see where failures occurred.")))

write("post-generation.html", page("Post-Generation Checklist", "./post-generation.html", """
<h1>Post-Generation Checklist</h1>
<p>Generation is not the finish line — it's the starting line. A significant set of post-generation tasks are required before the IFP application is usable. Work through this checklist in order.</p>

""" + callout("warning", "⚠️ Known Broken ADO Links — Fix First", "The following ADO links are documented as broken or missing out of the box. Create these manually before attempting any data loads: <br><strong>Financial Planning:</strong> Vendor Hierarchy<br><strong>Headcount:</strong> SYS by J2 Job, SYS by J3 Job, SYS by J4 Job (no link — create from scratch), Job Grade") + """

<h2>Required Tasks</h2>

<h3>1. Review Generation Logs</h3>
<ul>
  <li>Check PAF configuration logs for any failed modules or line items</li>
  <li>Create any missing model elements manually using the template model as reference</li>
  <li>Verify no blank action mappings exist</li>
</ul>

<h3>2. Time Settings (all models — must be consistent)</h3>
<ul>
  <li>Model Settings → Time: set fiscal year start month, current period, number of past/future years</li>
  <li><strong>Set current period to July</strong> for demo environments — gives a 6+6 forecast that displays well</li>
  <li>All 4 models must have the same current year and current period</li>
</ul>
""" + screenshot("Model Settings → Time — showing current period set to July 2026") + """

<h3>3. Version Alignment (all models)</h3>
<ul>
  <li>Create all required versions (Current Forecast Base, AOP Base, Prior Forecast, etc.)</li>
  <li>Set switchover dates</li>
  <li>Version names must be <strong>identical across all models</strong></li>
  <li>Map versions in FIN – Manage Versions, HC – Manage Versions, CapEx – Manage Versions</li>
</ul>

<h3>4. Spoke Model Mapping</h3>
<ul>
  <li>Map the HC model to your workspace copy</li>
  <li>Map the CE model to your workspace copy</li>
  <li>Without this, data cannot flow from HC/CE into FP</li>
</ul>

<h3>5. Placeholder Row Detail List Members</h3>
<p>Add placeholder members to the following lists in FP and CE models:</p>
<ul>
  <li>FP: Row Details – OpEx</li>
  <li>FP: Row Details – Allocation</li>
  <li>CE: Row Details – Asset</li>
  <li>CE: Row Details – Disposals</li>
</ul>

<h3>6. Validate Hierarchy Levels and Mirror Lists</h3>
<p>If hierarchy levels were added during configuration:</p>
<ul>
  <li>Verify new lists generated and each has a SYS module</li>
  <li>Update SYS by Mirror Entity and SYS by Mirror Department with new line items</li>
</ul>

<h3>7. Fix Dependent Dropdowns</h3>
<ul>
  <li>Dependent dropdowns don't always generate correctly</li>
  <li>Test each and fix manually if needed</li>
</ul>

<h3>8. UX Fixes</h3>
""" + table(
    ["Fix", "Pages Affected"],
    [
        ["Set page context to top level (not leaf)", "Admin source-to-planning pages, HC map jobs, BS manage cash offsets, OpEx allocation rule definition"],
        ["Check grid filters generated correctly", "All planning input pages"],
        ["Verify correct line items shown/hidden", "All planning grids"],
        ["Fix KPI card scaling (thousands/millions)", "IS report, BS report"],
        ["Fix form action fields", "BS intangibles, BS investments, BS joint ventures, BS leases, HC job metadata"],
        ["Reorder app categories (alphabetical → custom)", "All app categories"],
        ["Fix navigation links on landing page", "Home/landing page"],
        ["Fix page selector order", "All pages with selectors"],
    ]
) + """
<h3>9. Delete DEMO Actions</h3>
<ul>
  <li>Any action prefixed with "DEMO" is for manual data validation only</li>
  <li>Delete after generation (or after validating data loads)</li>
</ul>

<h3>10. Build ADO Pipelines</h3>
<p>See <a href="./data-load-ado.html">Data Load via ADO</a> for complete instructions.</p>

<h2>Optional Tasks</h2>
<ul>
  <li>Remove lists for excluded dimensions (verify not used elsewhere first)</li>
  <li>Create additional version copy actions if needed</li>
  <li>Set user roles and selective access</li>
  <li>Update time filters to show quarters (if needed)</li>
</ul>

<h2>Common Issues Quick Reference</h2>
""" + table(
    ["Symptom", "Check"],
    [
        ["Blank dashboards", "Administration dashboard mappings or selective access"],
        ["HC costs not in FP", "HC GL account mapping + run FIN – Import from HC Model"],
        ["CapEx not in FP", "GL account + entity-to-dept mapping in CapEx admin + run FIN – Import from CapEx Model"],
        ["ADO load errors", "Source file format, transformation view, link mappings"],
        ["Incorrect variances", "Version mapping in manage versions pages"],
        ["Missing data in planning grids", "Dimensional selectors set to parent — must be leaf level"],
    ]
)))

write("data-load-ado.html", page("Data Load via ADO", "./data-load-ado.html", """
<h1>Data Load via ADO</h1>
<p>After post-generation fixes, the next step is loading master data and actuals into all 4 IFP models via ADO. This page covers the complete data loading process.</p>

""" + callout("warning", "⚠️ Known Broken ADO Links — Must Fix First", "Create these manually before building any pipelines: <strong>Vendor Hierarchy</strong> (FP), <strong>SYS by J2/J3 Job</strong> (HC), <strong>SYS by J4 Job</strong> (HC — no link generated), <strong>Job Grade</strong> (HC). Use the Config Guide ADO setup steps to create them.") + """

<h2>Step 1 — Upload Source Files to ADO</h2>
<p>Upload all data template CSV files to ADO Source Data. Use the templates provided in the BOM:</p>
""" + table(
    ["File", "Module", "Type"],
    [
        ["IFP_DH_Source Account IS.csv", "Admin", "Direct load"],
        ["IFP_DH_Source Account BS.csv", "Admin", "Direct load"],
        ["IFP_DH_Source Entity.csv", "Admin", "Direct load"],
        ["IFP_DH_Source Department.csv", "Admin", "Direct load"],
        ["IFP_SH_FX Currency.csv", "All spokes", "Direct load"],
        ["IFP_SH_FX_Rates.csv", "All spokes", "Direct load"],
        ["IFP_FP_Trial Balance IS.csv", "FP", "Transformation load (via Admin mappings)"],
        ["IFP_HC_HRIS Actuals.csv", "HC", "Transformation load (via Admin mappings)"],
        ["IFP_CE_BS Subledger Trial Balance.csv", "CE", "Transformation load"],
    ]
) + """
<h2>Step 2 — Configure Admin Model Mappings</h2>
<ol>
  <li>Push source data to Admin model via ADO</li>
  <li>Navigate to Administration → Source to Planning in the UX</li>
  <li>Map all source departments → planning departments</li>
  <li>Map all source entities → planning entities</li>
  <li>Map all source IS accounts → planning IS accounts</li>
  <li>Map all source BS accounts → planning BS accounts</li>
  <li>Run "Create Departments/Entities/Accounts" actions to finalize planning lists</li>
</ol>
""" + screenshot("Admin model — Source to Planning Departments mapping page") + """
""" + callout("tip", "Set Default Mappings", "Use the 'Set Default Mappings' button to create quick 1:1 mappings for all unmapped items. Review and adjust any that need consolidation (e.g., multiple source depts → one planning dept). Goal: Unmapped KPI = 0.") + """
<h2>Step 3 — Build ADO Transformation Views for Actuals</h2>
<p>For loading actuals (Trial Balance IS, HRIS Actuals, etc.), you need transformation views in ADO:</p>
<ol>
  <li>Open the trial balance source file in ADO Source Data</li>
  <li>Bring in mapping datasets from Admin model: <code>SYS by Source Account IS Flat</code>, <code>SYS by Source Department Flat</code>, <code>SYS by Source Entity Flat</code></li>
  <li>Create leaf-level transformation views from each mapping dataset (filter: Is Leaf Level = true)</li>
  <li>Create a transformation view from the source file and join each mapping view</li>
  <li>Create a final clean view keeping only: Planning Account, Entity, Dept codes + Ending Balance + Time Period</li>
  <li>Change Ending Balance type from string to float; Time Period from string to date</li>
  <li>Enable aggregation and apply</li>
  <li>Map to the appropriate ADO link and push</li>
</ol>
""" + screenshot("ADO transformation view — join screen showing mapping view being joined to source file") + """
<h2>Step 4 — Push to Spoke Models</h2>
<p>After Admin mappings are complete and transformation views are built:</p>
<ol>
  <li>Re-sync Admin model source datasets in ADO (to pick up new mappings)</li>
  <li>Push Planning Account IS/BS hierarchies to FP, HC, CE</li>
  <li>Push Planning Entity and Department hierarchies to FP, HC, CE</li>
  <li>Push FX rates and currencies to all spoke models</li>
  <li>Push actuals (Trial Balance IS, HRIS Actuals) to FP and HC</li>
</ol>
""" + callout("note", "Load Order Matters", "Always push hierarchies and master data before pushing actuals. Actuals load will fail if planning lists aren't populated yet.") + """
<h2>Step 5 — Clone to ALM Models</h2>
<ul>
  <li>After ADO links are working in Dev, clone them to UAT and Prod</li>
  <li>Click ellipsis on each link → Clone to ALM Models → select UAT/Prod workspace</li>
</ul>

<h2>Step 6 — Validate Data Loads</h2>
<p>Use the Administration → Validate Data pages in the UX to confirm data loaded correctly:</p>
<ul>
  <li>FIN – Validate Exchange Rates</li>
  <li>FIN – Validate Trial Balance IS Data</li>
  <li>FIN – Validate Trial Balance BS Data</li>
  <li>HC – Validate Actuals</li>
  <li>HC – Validate Exchange Rates</li>
  <li>CapEx – Validate Exchange Rates</li>
  <li>CapEx – Validate Trial Balance BS Subledger</li>
</ul>
"""))

write("lab-b.html", page("Lab B: Full 3-Statement Configuration", "./lab-b.html", """
<h1>Lab B: Full 3-Statement Configuration</h1>
<div class="lab-banner">
  <span class="lab-type">🔬 Hands-On Lab</span>
  <span class="lab-duration">⏱ Estimated time: 45–60 minutes</span>
</div>

<h2>Objectives</h2>
<p>Building on Lab A, you will extend FictoCorp's IFP deployment to full 3-statement financial planning — adding CapEx, Balance Sheet, Cash Flow, and a Geography dimension.</p>

<h2>What Changes from Lab A</h2>
""" + table(
    ["Setting", "Lab A", "Lab B"],
    [
        ["CapEx", "Option B — GL level", "Option A — IFP CapEx Model"],
        ["Balance Sheet", "No", "Yes"],
        ["Cash Flow", "No", "Yes"],
        ["Geography", "No", "Yes — 'Geography' (2 levels: All Regions → Americas / EMEA)"],
        ["Models Generated", "Admin + FP + HC (CE deleted)", "Admin + FP + HC + CE (all 4 kept)"],
    ]
) + """
<h2>Customer Requirements Brief — FictoCorp Phase 2</h2>
""" + callout("note", "Starting Point", "Begin with a fresh workspace or re-run the Application Framework configuration from scratch. Do not extend Lab A's workspace.") + """
""" + table(
    ["Requirement", "Decision"],
    [
        ["All Lab A settings", "Same as Lab A (Entity, Dept, Product, Customer, HC Option A, multi-currency)"],
        ["Geography", "Yes — 'Geography' (2 levels: All Regions → Americas / EMEA)"],
        ["CapEx", "Option A: IFP CapEx Model"],
        ["Balance Sheet", "Yes"],
        ["Cash Flow", "Yes — indirect cash flow"],
        ["BS list name", "Planning Account BS Hierarchy (default)"],
        ["CF list name", "Planning Account CF Hierarchy (default)"],
    ]
) + """
<h2>Lab Steps</h2>
<ol>
  <li><strong>Configure Top-Level questions</strong> — same as Lab A, but add Geography (2 levels) and select Option A for CapEx</li>
  <li><strong>Hierarchy Configuration</strong> — add Geography hierarchy (2 levels), name it 'Geography'</li>
  <li><strong>FP questions</strong> — same as Lab A, but answer Yes to Balance Sheet and Cash Flow. Set BS and CF list names to defaults.</li>
  <li><strong>CE questions</strong> — multi-currency: Yes, IS list name: default, BS list name: default</li>
  <li><strong>Generate and review logs</strong></li>
  <li><strong>Post-Generation</strong> — complete all required tasks including CapEx general admin (entity-to-dept mapping, asset types, depreciation accounts)</li>
  <li><strong>Run FIN – Import from CapEx Model</strong> — after configuring CapEx admin</li>
  <li><strong>Configure BS</strong> — set planning methods, cash offset accounts, cash flow mappings</li>
  <li><strong>Run the Balancing Routine</strong> — ensure the balance sheet balances</li>
</ol>

<h2>Key Additional Post-Gen Tasks for Full 3-Statement</h2>
<ul>
  <li><strong>CapEx – General Admin:</strong> Set entity-to-department mapping, map asset types to depreciation accounts, select CWIP account and FX rate type</li>
  <li><strong>FIN – BS – Manage Planning Methods:</strong> Assign a method to every BS account</li>
  <li><strong>FIN – BS – Manage Cash Offset Accounts:</strong> Categorize every BS account's cash impact</li>
  <li><strong>FIN – BS – Cash Flow Mappings:</strong> Map every leaf-level BS account to a CF line</li>
  <li><strong>Run Balancing Routine</strong> after first data entry to confirm BS balances</li>
</ul>

""" + callout("warning", "CapEx Dimension Constraint", "CapEx is planned at Entity level ONLY — no Department, Geography, or other dimensions. The entity-to-department mapping in CapEx – General Admin handles distribution of depreciation costs to the correct P&amp;L dimensions.") + """

<h2>Debrief Questions</h2>
<ol>
  <li>What is the purpose of the Cash Offset Accounts mapping? What happens if an account is missing?</li>
  <li>Why does the Balancing Routine run month-by-month sequentially instead of all at once?</li>
  <li>If a customer wants to track CapEx by department, what options do they have?</li>
  <li>When would you choose Geography at 3 levels vs. 2 levels?</li>
  <li>What is the difference between Direct Load and Transformation Load in ADO?</li>
</ol>
"""))

print("Module 2 done.")
