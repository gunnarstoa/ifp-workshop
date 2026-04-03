#!/usr/bin/env python3
"""IFP Workshop Rebuild — Module 2: Configuration Workshop"""
import sys
sys.path.insert(0, '/home/gstoa/.openclaw/workspace/projects/work/workshops/ifp-workshop')
from rebuild import page, ss, ss_img, note, warn, tip, imp, table

page("Application Framework Walkthrough", "config-walkthrough.html",
     "Every configuration question — options, implications, and what to choose for FictoCorp",
     ["Module 2", "Configuration Workshop", "45 min"],
     ("All Config Questions", "Walk through every question in the Application Framework — what each controls and the trade-offs of each option."),
     ("Instructor Demo", "Facilitator opens the Application Framework and walks through each question section without yet answering them."),
     ("Preview FictoCorp Config", "Using the FictoCorp requirements, write down your answers to the Top-Level questions before starting Lab A."),
     """
      <h2>Top-Level Configuration Questions</h2>
      <p>These questions define the foundational structure applied across all 4 models.</p>

      <h3>Entity Dimension</h3>
      """ + table(["Setting","Details"],[
          ["What it is","Mandatory — your primary organizational hierarchy (e.g., Business Unit, Company, Legal Entity)"],
          ["What to configure","Name (capital + lowercase versions) + number of levels in hierarchy screen"],
          ["Impact","Used in Admin, FP, HC, CE — core dimension for all aggregation and reporting"],
      ]) + warn("Critical Naming Rule", "Use the EXACT same name in both the question response and the hierarchy rename. A mismatch causes modules and line items to not be renamed correctly throughout the model.") + """
      <h3>Department Dimension</h3>
      """ + table(["Option","Implication"],[
          ["Yes — include","Separate dept hierarchy created in all models; enables 2D planning (entity × dept); increases model size"],
          ["No — exclude","Simpler model; planning only by Entity; choose for simple or small implementations"],
      ]) + """
      <h3>Optional Dimensions</h3>
      """ + table(["Dimension","Used In","Include?","Exclude?"],[
          ["Geography","Revenue/COGS, OpEx, Top-Down","Multi-dimensional planning; more complexity","Simpler model; less dimensional granularity"],
          ["Functional Area","OpEx","Enables expense tracking by function","OpEx by dept only"],
          ["Vendor","OpEx","Enables vendor-level expense tracking","No vendor dimension in OpEx"],
      ]) + warn("Removing Dimensions Later Is Painful", "Removing a dimension after generation affects ALL areas of the model that use it. Make dimension decisions upfront — changing them later requires re-generation and re-doing all post-gen work.") + """
      <h3>Headcount Planning Approach</h3>
      """ + table(["Option","What Gets Deployed","When to Choose"],[
          ["Option A: IFP Role-Based HC Model","FP + HC models active; job-level HC costs flow into FP","Default for most implementations — best practice"],
          ["Option B: GL-Level Planning in FP","FP + HC generated; HC deleted after; HC expenses entered at GL level in FP","Simpler — for customers who don't need job-level detail"],
          ["Option C: External Model → Load to FP","FP + HC generated; HC deleted; summarized HC loaded from OWP or external","When OWP or another model is the HC system of record"],
      ]) + """
      <h3>Multi-Currency</h3>
      """ + table(["Option","Implication"],[
          ["Yes","Reporting Currency dimension added; FX rates required; triangulation enabled"],
          ["No","Single currency; simpler but not suitable for international organizations"],
      ]) + """
      <h3>Balance Sheet &amp; Cash Flow</h3>
      """ + table(["Setting","Options"],[
          ["Balance Sheet in FP?","Yes = Admin + FP include BS accounts and logic / No = P&amp;L only"],
          ["Cash Flow Reporting?","Yes = indirect cash flow statement generated / No = CF excluded"],
      ]) + """
      <h3>CapEx Planning Approach</h3>
      """ + table(["Option","What Gets Deployed","When to Choose"],[
          ["Option A: IFP CapEx Model","FP + CE models active; asset-level CapEx detail flows into FP","Asset-intensive businesses needing depreciation modeling"],
          ["Option B: GL-Level Planning in FP","FP + CE generated; CE deleted; CapEx entered at GL account level","Simple CapEx needs without asset-level detail"],
          ["Option C: External Model → Load to FP","FP + CE generated; CE deleted; summarized CapEx loaded externally","When another system manages CapEx"],
      ]) + """
      <h2>Financial Planning Model Questions</h2>
      <h3>Margin Planning Approach</h3>
      """ + table(["Option","Description"],[
          ["In FP Only","Full Revenue/COGS planning within FP model — most common"],
          ["Another Model → Load to FP","CMP or external; results loaded via DAT Margin Planning Import module"],
          ["Combination","Some in FP, some loaded from external source"],
          ["Expense Only","All margin components excluded; FP focuses on OpEx only"],
      ]) + """
      <h3>Key FP Questions Summary</h3>
      <ul>
        <li><strong>Product dimension?</strong> — Name + levels if Yes</li>
        <li><strong>Customer dimension?</strong> — Name + levels if Yes</li>
        <li><strong>IS list name</strong> — default: "Planning Account IS Hierarchy"</li>
        <li><strong>BS list name</strong> — default: "Planning Account BS Hierarchy"</li>
        <li><strong>CF list name</strong> — default: "Planning Account CF Hierarchy"</li>
        <li><strong>Expense planning?</strong> — Yes/No + dimensionality if Yes</li>
        <li><strong>Expense allocations?</strong> — Yes adds allocation modules (more complexity)</li>
      </ul>

      <h2>FictoCorp Configuration Preview</h2>
      """ + table(["Question","FictoCorp Answer"],[
          ["Entity name","Entity (2 levels)"],
          ["Department","Yes — Department (3 levels)"],
          ["Geography","No"],["Functional Area","No"],["Vendor","No"],
          ["Headcount","Option A: IFP Role-Based HC Model"],
          ["Multi-currency","Yes — USD base, USD/EUR/GBP reporting"],
          ["Balance Sheet (Lab A)","No"],["Cash Flow (Lab A)","No"],
          ["CapEx (Lab A)","Option B — GL level; delete CE after generation"],
          ["Margin planning","In FP only"],
          ["Product","Yes — Product (2 levels)"],
          ["Customer","Yes — Customer (2 levels)"],
          ["IS list name","Planning Account IS Hierarchy (default)"],
          ["Expense planning","Yes — Entity + Department dimensionality"],
          ["Expense allocations","No"],
      ]) + tip("Lab A Scope Reminder", "Lab A deploys Revenue/COGS + OpEx + HC only. Lab B will add CapEx, Balance Sheet, Cash Flow, and Geography. Answer the questions above for Lab A first."))

page("Lab A: Configure FictoCorp", "lab-a.html",
     "Hands-on: configure and generate IFP for FictoCorp Phase 1 (Revenue/COGS + OpEx + HC)",
     ["Module 2", "Lab", "45–60 min"],
     ("Customer Requirements", "FictoCorp's Phase 1 requirements — what to deploy and why the scope was chosen."),
     ("Facilitator Walkthrough", "Instructor completes the first 3 questions live, then participants continue independently."),
     ("Configure and Generate", "Complete all configuration questions, set hierarchy levels, and generate the FictoCorp Phase 1 application."),
     """
      <div class="callout-note"><span class="callout-label">ℹ Lab Scope</span><p>Phase 1 deploys <strong>Revenue/COGS + OpEx + Headcount</strong> only. No CapEx model, no Balance Sheet. Lab B will extend to the full 3-statement scope.</p></div>

      <h2>Requirements Brief — FictoCorp Phase 1</h2>
      """ + table(["Requirement","Your Configuration Choice"],[
          ["Entity name","Entity — 2 levels"],
          ["Department","Yes — Department — 3 levels"],
          ["Geography","No"],["Functional Area","No"],["Vendor","No"],
          ["Headcount approach","Option A: IFP Role-Based HC Model"],
          ["Multi-currency","Yes (USD base)"],
          ["Balance Sheet","No"],["Cash Flow","No"],
          ["CapEx approach","Option B — GL level (delete CE after generation)"],
          ["Margin planning","In FP only"],
          ["Product dimension","Yes — Product — 2 levels"],
          ["Customer dimension","Yes — Customer — 2 levels"],
          ["IS list name","Planning Account IS Hierarchy (default)"],
          ["Expense planning","Yes — Entity + Department dimensionality"],
          ["Expense allocations","No"],
      ]) + """
      <h2>Lab Steps</h2>
      <ol>
        <li><strong>Open the Application Framework</strong> — navigate to the configurator in your IFP workspace</li>
        <li><strong>Answer Top-Level questions</strong> — use the requirements table above; pay close attention to naming</li>
        <li><strong>Open Hierarchy Configuration</strong> — set Entity to 2 levels, Department to 3 levels; rename both to match your question responses exactly</li>
        <li><strong>Answer FP model questions</strong> — margin in FP, Product (2 levels), Customer (2 levels), expense with Entity + Department dimensionality, no allocations</li>
        <li><strong>Answer HC model questions</strong> — multi-currency: Yes, IS list name: default, Department: Yes, Job term: Job</li>
        <li><strong>Generate</strong> — click Generate and monitor the logs</li>
        <li><strong>Review generation logs</strong> — identify any errors; note items that failed to generate</li>
        <li><strong>Delete the CE model</strong> — since we chose GL-level CapEx, the generated CE model is not needed</li>
      </ol>

      """ + ss("Application Framework — Top-Level question screen showing Entity and dimension questions") + ss("Hierarchy Configuration screen — Entity 2 levels, Department 3 levels, both renamed") + ss("Generation success — showing all 4 models generated with log summary") + """
      <h2>Debrief Questions</h2>
      <ol>
        <li>What happens if the Entity name in the configuration question doesn't match the name in the Hierarchy Configuration screen?</li>
        <li>Why did we choose Option A for Headcount but Option B for CapEx?</li>
        <li>If FictoCorp later decides to add a Geography dimension, what would be the impact?</li>
        <li>What is the minimum number of hierarchy levels? Maximum?</li>
        <li>Why does the Application Framework generate a CE model even when we selected GL-level CapEx?</li>
      </ol>
      """ + tip("Generation Failures", "If generation fails: (1) confirm you have all 4 required roles, (2) confirm you are generating in your default tenant, (3) check PAF configuration logs to see where failures occurred."))

page("Post-Generation Checklist", "post-generation.html",
     "From raw generation to model readiness — the complete post-gen checklist",
     ["Module 2", "Configuration Workshop", "45 min", "Reference"],
     ("Why Post-Gen Matters", "Generation produces a working skeleton — but significant configuration is required before planners can use it."),
     ("Instructor Demo", "Facilitator opens a freshly-generated app and walks through the first 4 checklist items live."),
     ("Checklist Review", "Work through the full checklist and flag any items where you'd need help or more detail."),
     warn("⚠ Known Broken ADO Links — Fix These First", "The following ADO links are documented as broken or missing out of the box. Create these manually before any data loads:<br><br><strong>Financial Planning:</strong> Vendor Hierarchy<br><strong>Headcount:</strong> SYS by J2 Job · SYS by J3 Job · SYS by J4 Job (no link generated) · Job Grade<br><br>Use the ADO manual setup steps in the Configuration Guide to create them.") + """
      <h2>Required Tasks</h2>

      <h3>1. Review Generation Logs</h3>
      <ul class="checklist">
        <li>Review PAF configuration logs for failed modules or line items</li>
        <li>Create any missing model elements manually using the template model as reference</li>
        <li>Verify no blank action mappings exist</li>
        <li>Run all validation actions and resolve errors</li>
      </ul>

      <h3>2. Time Settings (all models — must be consistent)</h3>
      <ul class="checklist">
        <li>Model Settings → Time: set fiscal year start month, current period, past/future years</li>
        <li>Set current period to July for demo environments — gives 6+6 forecast that displays well on screen</li>
        <li>All 4 models must have the same current year and current period</li>
      </ul>

      <h3>3. Version Alignment (all models)</h3>
      <ul class="checklist">
        <li>Create all required versions (Current Forecast Base, AOP Base, Prior Forecast, etc.)</li>
        <li>Set switchover dates for all versions</li>
        <li>Version names must be identical across all models</li>
        <li>Map versions in FIN – Manage Versions, HC – Manage Versions, CapEx – Manage Versions</li>
      </ul>

      <h3>4. Spoke Model Mapping</h3>
      <ul class="checklist">
        <li>Map the HC model to your workspace copy</li>
        <li>Map the CE model to your workspace copy (if deployed)</li>
        <li>Without this, data cannot flow from HC/CE into FP</li>
      </ul>

      <h3>5. Placeholder Row Detail List Members</h3>
      <ul class="checklist">
        <li>FP: add placeholders to Row Details – OpEx list</li>
        <li>FP: add placeholders to Row Details – Allocation list</li>
        <li>CE: add placeholders to Row Details – Asset list</li>
        <li>CE: add placeholders to Row Details – Disposals list</li>
      </ul>

      <h3>6. UX Fixes</h3>
      """ + table(["Fix","Pages Affected"],[
          ["Set page context to top level (not leaf)","Admin source-to-planning pages, HC map jobs to departments, BS manage cash offsets, OpEx allocation rule definition"],
          ["Check grid filters generated correctly","All planning input pages"],
          ["Verify correct line items shown/hidden","All planning grids — suppress check"],
          ["Fix KPI card scaling (thousands/millions)","IS report, BS report"],
          ["Fix form action fields","BS intangibles, BS investments, BS joint ventures, BS leases, HC job metadata"],
          ["Reorder app categories (alphabetical → custom)","All app categories"],
          ["Fix navigation links on landing page","Home/landing page"],
          ["Check page selector order matches template","All pages with selectors"],
      ]) + """
      <h3>7. Delete DEMO Actions</h3>
      <ul class="checklist">
        <li>Any action prefixed with "DEMO" is for manual data validation only</li>
        <li>Delete after generation — or after validating data loads</li>
      </ul>

      <h3>8. Build ADO Pipelines</h3>
      <p>See <a href="./data-load-ado.html">Data Load via ADO</a> for complete step-by-step instructions.</p>

      <h2>Common Issues Quick Reference</h2>
      """ + table(["Symptom","Most Likely Cause","Fix"],[
          ["Blank dashboards","Mappings missing or selective access","Check Admin mapping pages; check user roles"],
          ["HC costs not in FP","GL account mapping or import not run","Check HC – Update Mappings; run FIN – Import from HC Model"],
          ["CapEx not in FP","Mapping or import not run","Check CapEx – General Admin; run FIN – Import from CapEx Model"],
          ["ADO load errors","Source file format change","Validate source file; check ADO link mappings"],
          ["Incorrect variances","Version mapping error","Check Manage Versions in all models"],
          ["Planning grid empty","Dimensional selector at parent level","Set selector to leaf-level member"],
      ]))

page("Data Load via ADO", "data-load-ado.html",
     "Upload files, configure Admin mappings, build transformation views, and push to spoke models",
     ["Module 2", "Configuration Workshop", "45 min"],
     ("The Data Loading Process", "How source data flows from ERP systems through ADO and the Admin model into all IFP spoke models."),
     ("Instructor Demo", "Facilitator opens ADO and walks through one complete example — uploading a source file, creating a transformation view, and pushing to a spoke model."),
     ("Build a Transformation View", "In your ADO workspace, locate the Trial Balance IS source file. Identify what transformation steps would be needed to load it into the FP model."),
     warn("⚠ Fix Broken ADO Links First", "Before building any pipelines, manually create: Vendor Hierarchy (FP), SYS by J2/J3/J4 Job (HC), and Job Grade (HC). These are known missing links and must exist before data can flow.") + """
      <h2>Step 1 — Upload Source Files to ADO</h2>
      """ + table(["File","Target Model","Load Type"],[
          ["IFP_DH_Source Account IS.csv","Admin","Direct load"],
          ["IFP_DH_Source Account BS.csv","Admin","Direct load"],
          ["IFP_DH_Source Entity.csv","Admin","Direct load"],
          ["IFP_DH_Source Department.csv","Admin","Direct load"],
          ["IFP_SH_FX Currency.csv","All spokes","Direct load"],
          ["IFP_SH_FX_Rates.csv","All spokes","Direct load"],
          ["IFP_FP_Trial Balance IS.csv","FP","Transformation load"],
          ["IFP_HC_HRIS Actuals.csv","HC","Transformation load"],
          ["IFP_CE_BS Subledger Trial Balance.csv","CE","Transformation load"],
      ]) + """
      <h2>Step 2 — Configure Admin Model Mappings</h2>
      <ol>
        <li>Push source data to Admin model via ADO</li>
        <li>Navigate to Administration → Source to Planning in the UX app</li>
        <li>Map all source departments → planning departments (goal: Unmapped KPI = 0)</li>
        <li>Map all source entities → planning entities</li>
        <li>Map all source IS accounts → planning IS accounts</li>
        <li>Map all source BS accounts → planning BS accounts</li>
        <li>Run "Create" actions to finalize the planning lists</li>
      </ol>
      """ + ss_img("back-end-information-2.jpg", "Admin model — source to planning mapping workbench") + tip("Set Default Mappings Button", "Use 'Set Default Mappings' to quickly create 1:1 mappings for all unmapped items. Review and adjust any that need consolidation (multiple source codes → one planning code).") + """
      <h2>Step 3 — Build ADO Transformation Views for Actuals</h2>
      <ol>
        <li>Open the trial balance source file in ADO Source Data</li>
        <li>Import mapping datasets from Admin model: <code>SYS by Source Account IS Flat</code>, <code>SYS by Source Dept Flat</code>, <code>SYS by Source Entity Flat</code></li>
        <li>Create leaf-level transformation view from each (filter: Is Leaf Level = true)</li>
        <li>Create a transformation view from the source file; join each mapping view to add Planning codes</li>
        <li>Create final clean view keeping: Planning Account, Entity, Dept + Ending Balance (float) + Time Period (date)</li>
        <li>Enable aggregation → Apply</li>
        <li>Map to ADO link and push</li>
      </ol>

      <h2>Step 4 — Push to Spoke Models</h2>
      <ul class="checklist">
        <li>Re-sync Admin model source datasets in ADO (picks up new mappings)</li>
        <li>Push Planning Account IS/BS hierarchies to FP, HC, CE</li>
        <li>Push Planning Entity and Department hierarchies to FP, HC, CE</li>
        <li>Push FX rates and currencies to all spoke models</li>
        <li>Push actuals (Trial Balance IS, HRIS Actuals) to FP and HC</li>
      </ul>
      """ + note("Load Order Matters", "Always push hierarchies and master data before pushing actuals. Actuals loads will fail if planning lists aren't populated yet.") + """
      <h2>Step 5 — Validate Data Loads</h2>
      <ul class="checklist">
        <li>FIN – Validate Exchange Rates</li>
        <li>FIN – Validate Trial Balance IS Data</li>
        <li>FIN – Validate Trial Balance BS Data (if BS deployed)</li>
        <li>HC – Validate Actuals</li>
        <li>HC – Validate Exchange Rates</li>
        <li>CapEx – Validate Exchange Rates (if CE deployed)</li>
        <li>CapEx – Validate Trial Balance BS Subledger (if CE deployed)</li>
      </ul>""")

page("Lab B: Full 3-Statement Configuration", "lab-b.html",
     "Extend FictoCorp with CapEx, Balance Sheet, Cash Flow, and Geography",
     ["Module 2", "Lab", "45–60 min"],
     ("Phase 2 Requirements", "FictoCorp is expanding to full 3-statement planning — what changes from Lab A and why."),
     ("Instructor Preview", "Facilitator shows what the full 3-statement configuration looks like vs. Lab A — highlighting the key differences."),
     ("Configure and Generate", "Complete Phase 2 configuration and generate the full FictoCorp application, including CapEx, Balance Sheet, and Cash Flow."),
     note("Starting Point", "Begin with a fresh workspace or re-run the Application Framework from scratch. Do not extend Lab A's workspace.") + """
      <h2>What Changes from Lab A</h2>
      """ + table(["Setting","Lab A","Lab B"],[
          ["CapEx","Option B — GL level","Option A — IFP CapEx Model"],
          ["Balance Sheet","No","Yes"],
          ["Cash Flow","No","Yes"],
          ["Geography","No","Yes — Geography (2 levels: All Regions → Americas · EMEA)"],
          ["Models Generated","Admin + FP + HC (CE deleted)","Admin + FP + HC + CE (all 4 kept)"],
      ]) + """
      <h2>Requirements Brief — FictoCorp Phase 2</h2>
      """ + table(["Requirement","Your Configuration Choice"],[
          ["All Lab A settings","Same — Entity, Dept, Product, Customer, HC Option A, multi-currency"],
          ["Geography","Yes — Geography (2 levels)"],
          ["CapEx","Option A: IFP CapEx Model"],
          ["Balance Sheet","Yes"],
          ["Cash Flow","Yes — indirect cash flow"],
          ["BS list name","Planning Account BS Hierarchy (default)"],
          ["CF list name","Planning Account CF Hierarchy (default)"],
          ["CE model questions","Multi-currency: Yes; IS + BS list names: defaults"],
      ]) + """
      <h2>Lab Steps</h2>
      <ol>
        <li>Configure Top-Level questions — same as Lab A, plus Geography (2 levels), CapEx Option A</li>
        <li>Hierarchy Configuration — add Geography (2 levels, name: 'Geography')</li>
        <li>FP questions — same as Lab A, plus Balance Sheet: Yes, Cash Flow: Yes</li>
        <li>CE questions — multi-currency: Yes, IS list: default, BS list: default</li>
        <li>Generate and review logs</li>
        <li>Post-generation — complete all required tasks including CapEx General Admin setup</li>
        <li>CapEx General Admin — set entity-to-dept mapping, asset types, depreciation accounts, CWIP account, FX rate type</li>
        <li>Run FIN – Import from CapEx Model</li>
        <li>FIN – BS – Manage Planning Methods — assign a method to every BS account</li>
        <li>FIN – BS – Manage Cash Offset Accounts — categorize every BS account's cash impact</li>
        <li>FIN – BS – Cash Flow Mappings — map every leaf-level BS account to a CF line</li>
        <li>Run the Balancing Routine — confirm BS balances</li>
      </ol>

      """ + warn("CapEx Dimension Constraint", "CapEx in v2.0 is planned at Entity level ONLY — no Department, Geography, or other dimensions. The entity-to-department mapping in CapEx General Admin handles distribution of depreciation costs to the correct P&amp;L dimensions.") + """
      <h2>Debrief Questions</h2>
      <ol>
        <li>What is the purpose of the Cash Offset Accounts mapping? What happens if an account is missing?</li>
        <li>Why does the Balancing Routine run month-by-month sequentially rather than all at once?</li>
        <li>If a customer wants to track CapEx by department, what are their options?</li>
        <li>When would you choose Geography at 3 levels vs. 2 levels?</li>
        <li>What is the difference between a Direct Load and a Transformation Load in ADO?</li>
      </ol>
      """ + tip("Full 3-Statement Validation", "After completing Lab B, check that the balance sheet balances by running the Balancing Routine, then navigate to Reporting &amp; Analysis → Balance Sheet &amp; Cash Flow Validations."))

print("Module 2 done.")
