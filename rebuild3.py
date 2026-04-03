#!/usr/bin/env python3
"""IFP Workshop Rebuild — Module 3, 4, Reference, Q&A"""
import sys
sys.path.insert(0, '/home/gstoa/.openclaw/workspace/projects/work/workshops/ifp-workshop')
from rebuild import page, ss, ss_img, note, warn, tip, imp, table

# ─── Module 3 ─────────────────────────────────────────────────────────────────

page("Revenue & COGS Planning", "revenue-cogs.html",
     "Planning methods by product type, UX experience, and integration with Balance Sheet",
     ["Module 3", "Module Walkthrough", "20 min"],
     ("How Revenue Planning Works", "Configurable driver-based methods per account per product — different product types can use different planning logic."),
     ("Instructor Demo", "Facilitator opens the Revenue &amp; COGS Planning page, switches between product types, and shows how the input fields change dynamically."),
     ("Try Revenue Planning", "Select each of FictoCorp's product families in turn. Note which input fields appear for each method. Enter a test value for one product."),
     """
      <h2>Key Capabilities</h2>
      <ul>
        <li><strong>Configurable per account AND per product</strong> — each product can use a different planning method for revenue and COGS</li>
        <li><strong>Progressive Disclosure UX</strong> — shows only the inputs required for the selected method</li>
        <li><strong>Context-sensitive help</strong> — selecting an account shows instructions and description on the left panel</li>
        <li>Any account without a method assigned will NOT appear on the planning page</li>
      </ul>

      <h2>Common Product Planning Setups</h2>
      """ + table(["Product Type","Accounts Used","Typical Method","Inputs"],[
          ["Physical Products","Product Sales + COGS","Units x Rate","Units sold + price per unit"],
          ["Services / Consulting","Services Sales + Services COGS","Units x Rate","Hours x rate per hour"],
          ["SaaS / Subscription","Subscription Sales + Sub COGS","Units x Rate","Subscriptions x rate per subscription"],
      ]) + ss_img("revenue-cogs-planning-2.jpg", "Revenue & COGS Planning page — showing Units x Rate method inputs") + """
      <h2>Available Planning Methods</h2>
      """ + table(["Method","Description","Best For"],[
          ["Units x Rate","Revenue = Units × Rate","Physical products, services (hours × rate), subscriptions"],
          ["Direct Input","Enter amounts manually","Simple or non-driver-based accounts"],
          ["Prior Run Rate","Prior period × (1 + growth %)","Stable recurring revenue"],
          ["Rolling Moving Average","Average of prior N periods","Smoothed trend forecasting"],
          ["COGS % of Revenue","COGS = Revenue × user-defined %","Margin-driven COGS accounts"],
      ]) + warn("Department Selector Matters", "If you select a product but see no data, check your department selector. Service revenue may only appear under Professional Services, not Sales. This is expected behavior — not a bug.") + """
      <h2>Process Pages</h2>
      """ + table(["Page","Purpose"],[
          ["Revenue &amp; COGS Planning","Main planning input — dynamic grid per product + planning method"],
          ["Revenue &amp; COGS Summary","Overview by dept/profit center, product family, and account"],
      ]) + note("V2.0 Change", "End-user import templates for loading Revenue/COGS to specific GL accounts have been removed in v2.0. Customers requiring GL-level imports need an extension."))

page("Operating Expenses", "opex.html",
     "Planning methods, line item detail, allocations, and cross-model imports",
     ["Module 3", "Module Walkthrough", "20 min"],
     ("How OpEx Planning Works", "One method per account, driver-based inputs, line item detail, and single-step allocations — all with Progressive Disclosure."),
     ("Instructor Demo", "Facilitator opens OpEx Planning, switches between accounts with different methods, demonstrates Line Item Detail, and shows an allocation rule."),
     ("Try OpEx Planning", "Find an account using Prior Run Rate. Change the growth percentage and observe the effect on the forecast. Then find an account using Line Item Detail."),
     """
      <h2>Key Capabilities</h2>
      <ul>
        <li><strong>One method per account</strong> — applies uniformly across all entities and departments (changed from v1.x)</li>
        <li>Accounts set to "Planned in Headcount" or "Planned in CapEx" are hidden from the OpEx planning grid</li>
        <li>Progressive Disclosure shows only relevant inputs for the selected method</li>
      </ul>

      <h2>Available Planning Methods</h2>
      """ + table(["Method","Description","Key Input"],[
          ["Prior Run Rate","Prior period × (1 + growth %)","Growth %, # periods to go back, $ adjustment"],
          ["Units x Rate","Units × rate","Units (e.g., hours), Rate, Adjustment"],
          ["Rolling Moving Average","Average of N prior periods","# periods for average"],
          ["Direct Input","Manual monthly entry","Enter amounts directly"],
          ["$ Amount Growth","Prior period + $ growth amount","Growth amount"],
          ["Fixed Average","Fixed average over N periods","# periods"],
          ["Line Item Detail","Amounts from Line Item Detail page","Entered on Line Item Detail page"],
          ["Planned in CapEx","Auto from CE model — data entry disabled","(none)"],
          ["Planned in Headcount","Auto from HC model — data entry disabled","(none)"],
      ]) + ss_img("operating-expenses-2.jpg", "OpEx Planning page — Prior Run Rate method with growth % input") + warn("Cross-Model Imports", "After changes in HC or CapEx models, you MUST run FIN – Import from HC Model and FIN – Import from CapEx Model. Data does NOT sync automatically. If OpEx values don't reflect HC or CapEx updates, this is always the first thing to check.") + """
      <h2>Line Item Detail</h2>
      <ul>
        <li>Enter description, then specify extra dimensions (vendor, functional area, geography)</li>
        <li>Once amounts are entered, dimension values cannot be changed without clearing amounts first</li>
        <li>Bottom grid shows sum by vendor — select a specific vendor to see all costs for that vendor</li>
        <li>Line items planned here appear in the Summary but NOT on the main OpEx planning page</li>
      </ul>

      <h2>Allocations</h2>
      <ul>
        <li>Define source (entity, dept, account), allocation % or $, and target</li>
        <li>Basis options: FTE, even spread, or manual (entered on Allocation Basis Input page)</li>
      </ul>
      """ + imp("Allocations Extension Point", "IFP v2.0 supports basic single-step allocations out of the box. For sophisticated allocations (waterfalls, multi-step, reciprocal, extra dimensions), the Profitability application is the right tool — it integrates with IFP.") + """
      <h2>Process Pages</h2>
      """ + table(["Page","Purpose"],[
          ["OpEx Planning","Main planning grid — dynamic inputs per account/method"],
          ["OpEx Line Item Detail","Enter detailed line items with extra dimensions per account"],
          ["OpEx Allocation Basis Input","Enter manual basis values by entity and department"],
          ["OpEx Allocation Rule Definition","Define source, target, and basis for each allocation rule"],
          ["OpEx Summary","Overview by entity, department, and account"],
      ]))

page("Headcount Planning", "headcount.html",
     "Job-level workforce planning — setup sequence, pay bands, planning inputs, and cost sync to FP",
     ["Module 3", "Module Walkthrough", "25 min"],
     ("How HC Planning Works", "Job-level planning (not employee-level) — centralized job library, pay bands, department mapping, and cost calculations."),
     ("Instructor Demo", "Facilitator walks through the full HC setup sequence: job metadata → dept mapping → pay bands → GL accounts → cost assumptions → planning."),
     ("Explore HC Pages", "Navigate to HC – Review/Update Job Metadata. How many valid jobs are there? Navigate to HC – Map Jobs to Departments. What is the current count of unmapped jobs?"),
     imp("Job-Level, Not Employee-Level", "IFP v2.0 HC plans at the job role level — no named employee data. For position or employee-level detail, use OWP (Operational Workforce Planning) or WFB (Workforce Budgeting), both of which integrate natively with IFP.") + """
      <h2>Setup Sequence</h2>
      <ol>
        <li>Configure Job Metadata (create jobs, set grades, employment types, active flag)</li>
        <li>Map Jobs to Departments (define which roles exist in which departments)</li>
        <li>Set Job Grade Pay Bands (compensation guardrails)</li>
        <li>Map GL Accounts (connect HC costs to FP accounts)</li>
        <li>Enter Job Cost Assumptions (specific costs per job per department)</li>
        <li>Plan Headcount (hires, exits, transfers, attrition by month)</li>
      </ol>

      <h2>Job Metadata</h2>
      """ + ss_img("headcount-2.jpg", "HC – Job Metadata page showing job list with grade, employment type, active status") + """
      <p>Required fields for a valid job: <strong>Job Code · Display Name · Job Parent · Job Grade · Employment Type · Active = TRUE</strong>. Jobs with missing fields are marked Invalid and won't appear in planning grids.</p>

      <h2>Job to Department Mapping</h2>
      <ul>
        <li>Monitor: <strong>Number of Valid Unmapped Jobs KPI</strong> — goal is zero</li>
        <li>A job can be mapped to multiple departments</li>
        <li>Allow Contingent Worker checkbox only unlocks when: (1) job is Assigned to dept AND (2) Allow Contingent Worker = TRUE globally on the job</li>
      </ul>

      <h2>Job Grade Pay Bands</h2>
      """ + ss_img("headcount-3.jpg", "HC – Job Grade Pay Bands page showing min/max salary and benefit percentages by grade") + """
      <ul>
        <li>Set min/max base salary per grade (company-wide guardrails)</li>
        <li>Bonus %, Benefits %, Overhead % as percentage of salary</li>
        <li>Regional differentiation by entity supported (different rates per country)</li>
        <li>System validates entries — max must be ≥ min; percentages must be 0–100%</li>
      </ul>

      <h2>GL Account Mappings</h2>
      <ul>
        <li>Map each HC cost category (salary, bonus, benefits, overhead, payroll taxes) to a leaf-level GL account</li>
        <li>Parent-level GL accounts trigger red validation errors</li>
        <li>Incorrect mappings push costs to wrong OpEx categories when imported to FP</li>
      </ul>

      <h2>Headcount Planning</h2>
      """ + ss_img("headcount-4.jpg", "HC – Planning page showing hires, exits, and transfers by job per department") + """
      <ul>
        <li>Manual entry: Hires · Exits · Transfers In/Out — by month for plan period</li>
        <li>Attrition is assumption-based (parameter), not manual</li>
        <li>Use suppression to show only jobs with headcount</li>
        <li>KPI cards and charts update at top of page as you enter data</li>
      </ul>

      <h2>Sync to FP</h2>
      <p>After planning: Administration → Financials Model → <strong>FIN – Import from HC Model</strong>. This pushes all HC workforce costs into the correct OpEx accounts in FP.</p>
      """ + tip("Regional Cost Profiles", "Pay bands can vary by entity — useful for international organizations where the same job grade has different compensation levels by country (e.g., India vs. US rates for the same role)."))

page("CapEx Planning", "capex.html",
     "Asset planning, depreciation, disposals, and the entity-only dimension constraint",
     ["Module 3", "Module Walkthrough", "20 min"],
     ("How CapEx Planning Works", "Individual asset or asset-class planning with automated depreciation, disposal modeling, and immediate P&amp;L/BS impact visibility."),
     ("Instructor Demo", "Facilitator opens CapEx New Asset Purchases, adds a test asset with a custom payment plan, and shows the P&amp;L and BS impact timeline."),
     ("Explore CapEx Pages", "Navigate to CapEx – General Admin. Identify the asset types configured. What accounts are mapped to each? Navigate to CapEx – New Asset Purchases and review the existing asset entries."),
     warn("Entity-Level Only", "CapEx in IFP v2.0 is planned at Entity level ONLY — no Department, Geography, or other dimensions. The entity-to-department mapping in CapEx General Admin handles distribution of depreciation to P&amp;L dimensions. Department-level CapEx requires an extension.") + """
      <h2>Admin Setup</h2>
      <h3>CapEx – General Admin</h3>
      <ul>
        <li>Asset types/classes with payment plan parameters and useful life settings</li>
        <li><strong>New in v2.0:</strong> Computer Hardware and Computer Software are now separate asset classes (accounts 1712 and 1772)</li>
        <li>Entity-to-department mapping — every entity must have a department mapped</li>
        <li>Map Net Fixed Asset Values to P&amp;L accounts</li>
        <li>Map Asset Types to Depreciation Accounts</li>
        <li>Select CWIP (Construction Work in Progress) account</li>
        <li>Select FX Rate Type for currency translation</li>
      </ul>
      """ + imp("Leaf-Level Accounts Only", "All mappings in CapEx General Admin must point to leaf-level accounts. Parent-level mappings cause calculation failures and missing data in FP.") + """
      <h2>End-User Planning Pages</h2>

      <h3>CapEx – New Asset Purchases</h3>
      """ + ss_img("capex-2.jpg", "CapEx – New Asset Purchases page showing asset list with order date, in-service date, depreciation method") + """
      <ul>
        <li>Per asset: asset class, order date, in-service date, CWIP flag, depreciation method</li>
        <li>P&amp;L and BS impact shown on timeline automatically</li>
        <li><strong>Custom payment plans</strong> — enter exact cash payment schedule for specific assets</li>
      </ul>

      <h3>Other CapEx Pages</h3>
      """ + table(["Page","Purpose"],[
          ["CapEx – Funding Details","Default payment plan (read-only); custom payment plan entry by period"],
          ["CapEx – By Asset Type","Plan at asset class level — no individual asset tracking"],
          ["CapEx – Asset Disposals","Enter disposal details; system calculates gain/loss and shows P&amp;L/BS impact"],
          ["CapEx – Net Fixed Asset Roll-Forward","Read-only report of net fixed asset roll-forward calculations"],
      ]) + """
      <h2>Sync to FP</h2>
      <p>After CapEx planning: Administration → Financials Model → <strong>FIN – Import from CapEx Model</strong>.</p>
      """ + tip("Polaris Performance Note", "When adding new assets, Polaris is optimized for bulk additions. Adding assets one at a time can be slow — batch additions where possible."))

page("Balance Sheet & Cash Flow", "balance-sheet.html",
     "Activity-based planning, cash offset accounts, balancing routine, and sub-schedules",
     ["Module 3", "Module Walkthrough", "25 min"],
     ("How BS Planning Works", "Activity-based planning — inputs represent periodic changes, not end-of-period balances. The last actual period rolls forward automatically."),
     ("Instructor Demo", "Facilitator opens BS Account Planning, demonstrates how entering activity affects the balance sheet, then runs the Balancing Routine and shows a balanced result."),
     ("Explore BS Pages", "Open BS – Account Planning. Select an AR account — what planning method is set? What inputs appear? What is the closing balance for the last actual period?"),
     note("Activity-Based Planning", "All BS inputs represent periodic ACTIVITY — not end-of-period balances. If you enter nothing, the last actual balance rolls forward. Formula: Closing Balance = Last Actual Balance ± Activity. This means a zero-input BS still produces a sensible result.") + """
      <h2>Admin Setup</h2>

      <h3>FIN – BS – Manage Planning Methods</h3>
      """ + table(["Method","Best For"],[
          ["Direct Input","General BS accounts"],
          ["Days Sales Outstanding (DSO)","Accounts receivable"],
          ["Days Payable Outstanding (DPO)","Accounts payable / trade payables"],
          ["Days Inventory Outstanding (DIO)","Inventory"],
          ["Inventory Turns","Inventory (alternative to DIO)"],
          ["Percent of A/R","Bad debt provision"],
          ["Planned in CapEx","PP&amp;E and accumulated depreciation — auto from CE model"],
      ]) + """
      <h3>FIN – BS – Manage Cash Offset Accounts</h3>
      """ + warn("New in v2.0 — Critical", "Cash Offset Accounts define how each BS account affects the cash balance. Every BS account must be categorized. Missing mappings break the cash flow statement. Cannot have more than one mapping per account — system flags duplicates.") + """
      <ul>
        <li>Select the Primary Cash Account at the top</li>
        <li>For each BS account, assign its offset category (increases in assets reduce cash; increases in liabilities increase cash)</li>
        <li>System shows red error if a duplicate mapping exists — prevents double-counting cash</li>
      </ul>

      <h2>End-User Planning Pages</h2>
      <h3>BS – Account Planning</h3>
      """ + ss_img("balance-sheet-planning-2.jpg", "BS Account Planning page — showing DSO input for Accounts Receivable") + """
      <ul>
        <li>Entity level only — no department or operational dimensions</li>
        <li>Dynamic inputs based on planning method (DSO → enter days; Direct → enter activity amounts)</li>
        <li>Adjustment available for every method</li>
      </ul>

      <h3>Sub-Schedules</h3>
      """ + table(["Page","Purpose"],[
          ["BS – Investments","New investments — enter amount, start date, duration, rate; see IS/BS/CF impact"],
          ["BS – Intangibles &amp; Financing","Intangibles, short-term debt, long-term debt instruments"],
          ["BS – Leases","Capital and operating leases — enter details and see financial impact"],
          ["BS – Joint Ventures","JV details and financial statement impact"],
          ["BS – Equities","Opening share balance, planned share issuances"],
      ]) + tip("Entity Alignment Required", "For sub-schedules: the entity in the instrument must match the entity selector on the page. Misalignment means no financial data shows below the input. This is expected behavior — not a bug.") + """
      <h3>BS – Balancing Routine</h3>
      <ul>
        <li>Runs month-by-month sequentially — July must complete before August (retained earnings roll-forward dependency)</li>
        <li>Runs for ALL entities, not just the one currently selected</li>
        <li>After running: balance sheet should be in balance based on the inputs entered</li>
      </ul>
      """ + tip("Run After Each Planning Session", "Run the Balancing Routine after each planning session where BS activity has been entered. The BS – Validations report in Reporting &amp; Analysis will show whether you're in balance."))

page("Top-Down Planning", "top-down.html",
     "Setting executive targets and reconciling against bottom-up plans",
     ["Module 3", "Module Walkthrough", "15 min"],
     ("How Top-Down Planning Works", "Set executive-level targets at L2 of each dimension hierarchy, then compare against bottom-up plans on the TD Summary page."),
     ("Instructor Demo", "Facilitator opens TD Planning, enters a revenue target, then navigates to TD Summary to show the target vs. bottom-up comparison."),
     ("Enter a Target", "Navigate to TD – Planning. Enter a revenue target for one product family at the Sales &amp; Marketing department level. Then view the result on TD – Summary."),
     imp("⚠ V2.0 Limitation: No Dynamic Disaggregation", "Dynamic top-down disaggregation (automatic cascade of high-level targets to lower levels) is NOT available in IFP v2.0. All targets must be entered manually at each level of detail. Anaplan plans to reintroduce this in a future release.") + """
      <h2>What You Can Set Targets For</h2>
      """ + table(["Category","Target Types"],[
          ["Revenue","Revenue Target + Gross Profit Target by product family and customer"],
          ["Margin","Gross Profit % target for COGS accounts"],
          ["Operating Expenses","General OpEx (excl. labor), Labor Cost, Total OpEx"],
          ["Headcount","FTE and Headcount targets (new in v2.0)"],
      ]) + """
      <h2>Planning Level</h2>
      <p>All targets are entered at <strong>Level 2</strong> of each dimension hierarchy. In USD — can be reported in local currency.</p>

      <h2>Process Pages</h2>
      """ + table(["Page","Purpose"],[
          ["TD – Planning","Manual input of all targets by dimension at L2"],
          ["TD – Summary","Targets vs. bottom-up plans side-by-side; variance calculations at L2"],
      ]) + ss_img("top-down-planning-2.jpg", "Top-Down Planning page — showing revenue and gross profit target inputs") + """
      <h2>Why Targets Don't Show on Module Summary Pages</h2>
      <p>By design — the OpEx Summary, Revenue Summary, etc. don't show TD targets. Reason: users viewing those pages may be at a more granular level (L3 entity, cost center) than the L2 targets, creating confusion. All target vs. actual comparison is consolidated on the TD pages at consistent L2.</p>

      <h2>Talk Track</h2>
      <ul>
        <li><em>"This gives your CFO a single screen to see whether the teams' bottom-up plans are aligned to executive targets."</em></li>
        <li><em>"In v2.0 targets are entered manually at L2 — dynamic disaggregation is on the roadmap for a future release."</em></li>
        <li><em>"We now support headcount and labor cost targets in addition to revenue, margin, and OpEx — that's new in v2.0."</em></li>
      </ul>
      """)

page("Reporting & Analysis", "reporting.html",
     "Financial reports, variance analysis, statistical tools, and the management reporting pack",
     ["Module 3", "Module Walkthrough", "20 min"],
     ("What's in Reporting", "Consolidated IS, BS, and CF reports plus variance analysis, two new statistical analysis tools, and a pre-built management reporting pack."),
     ("Instructor Demo", "Facilitator tours the Reporting &amp; Analysis category: IS report with suppression, BS validation, Currency Variance Analysis, and the Management Reporting Sample."),
     ("Explore Reports", "Open the Income Statement Report. Enable suppression. Switch the analysis type from Amounts to Percent of Revenue. What changes?"),
     """
      <h2>Core Financial Reports</h2>
      """ + table(["Report","Purpose"],[
          ["Income Statement Report","Ad hoc IS analysis at account level; suppression available; analysis type switcher"],
          ["IS Variance Analysis","Compare IS data across any two versions; analyze variances"],
          ["Balance Sheet Report","Detailed BS at account level; closing balance = last actual ± activity entered"],
          ["BS Variance Analysis","Compare BS data between versions"],
          ["BS &amp; CF Validations","Is the balance sheet in balance? Cash flow reconciliation."],
          ["Indirect Cash Flow","System-calculated CF + manual fine-tuning adjustments"],
          ["Currency Variance Analysis","Isolate FX rate impact between two time periods"],
      ]) + ss_img("reporting-analysis-2.jpg", "Reporting & Analysis — Income Statement Report with suppression enabled") + """
      <h2>New in V2.0: Statistical Analysis</h2>
      <h3>Product Sales Outlier Analysis</h3>
      <ul>
        <li>Statistical analysis of product-based revenue data</li>
        <li>Parameters: number of standard deviations, basis (mean or trend line)</li>
        <li>Highlights statistical outliers — useful for identifying unusual trends proactively</li>
      </ul>

      <h3>Product Correlation Analysis</h3>
      <ul>
        <li>Analyzes correlations between products across entities and geographies</li>
        <li>Shows which products move together and which are independent</li>
      </ul>

      <h2>Management Reporting Sample</h2>
      """ + ss_img("reporting-analysis-4.jpg", "Management Reporting Sample — executive summary with P&L and dynamic commentary") + """
      <ul>
        <li>Pre-built board-pack: cover page, P&amp;L, Balance Sheet, Cash Flow statement</li>
        <li><strong>Dynamic commentary</strong> — tagged to data, updates automatically as plan data changes</li>
        <li>Entity and currency selectors at top right</li>
        <li>Customers expected to customize for their own board pack format</li>
      </ul>

      <h2>Report Scaling and Display</h2>
      <ul>
        <li>Most reports scaled to thousands</li>
        <li>Use Suppress to hide zero/unused accounts</li>
        <li>Switch between: Amounts · Year-over-year change · Percentage · Percent of revenue</li>
      </ul>
      """ + note("Finance Analyst / CoPlanner", "Finance Analyst is embedded in IFP v2.0 for natural language data queries (e.g., 'What drove the variance in OpEx this quarter?'). Pending full GA availability — check with your Anaplan account team for current status."))

print("Module 3 done.")

# ─── Module 4 ─────────────────────────────────────────────────────────────────

page("Admin Runbook", "admin-runbook.html",
     "Monthly maintenance checklist, version management, planning methods, and troubleshooting",
     ["Module 4", "Admin & Extensions", "20 min"],
     ("Ongoing Administration", "What IFP model administrators need to do every month, every planning cycle, and how to troubleshoot common issues."),
     ("Instructor Review", "Facilitator walks through the monthly checklist and explains the dependency between each task."),
     ("Monthly Checklist Practice", "Using the monthly checklist, identify which tasks have dependencies on each other. In what order must they run?"),
     """
      <h2>Monthly Checklist</h2>
      <ul class="checklist">
        <li>Update Current Period in Model Settings → Time (all 4 models)</li>
        <li>Run ADO pipelines — refresh hierarchies, flat lists, attributes, actuals, and FX rates</li>
        <li>Review Admin model for any unmapped new departments, entities, or accounts from source systems</li>
      </ul>

      <h2>Planning Cycle Checklist</h2>
      <ul class="checklist">
        <li>Update time ranges if planning horizon has changed</li>
        <li>Update versions list with any new versions</li>
        <li>Run version-to-version copy actions to seed new versions from existing data</li>
        <li>Review all Administration pages — planning methods, account settings, BS/CF mappings</li>
        <li>Run FIN – Import from HC Model (after HC updates)</li>
        <li>Run FIN – Import from CapEx Model (after CE updates)</li>
      </ul>
      """ + warn("Version Names Must Match Across All Models", "Version names must be identical in Admin, FP, HC, and CE. A mismatch causes incorrect variance calculations. If variance reports look wrong, check version mappings in all Manage Versions pages first.") + """
      <h2>Version Management</h2>
      <ul>
        <li>Location: Administration → FIN/HC/CapEx – Manage Versions</li>
        <li>Map each native version to the custom comparison version list</li>
        <li>Enable custom comparison versions via <code>Override = TRUE</code> in SYS by Version Variance Comparison</li>
        <li>Run version copy actions before planners enter data in new versions</li>
      </ul>

      <h2>Troubleshooting Quick Reference</h2>
      """ + table(["Symptom","Most Likely Cause","Fix"],[
          ["Blank dashboards","Mappings missing or selective access","Check Admin mapping pages; check user roles"],
          ["HC costs not in FP","GL account mapping or import not run","Check HC – Update Mappings; run FIN – Import from HC Model"],
          ["CapEx not in FP","Mapping or import not run","Check CapEx – General Admin; run FIN – Import from CapEx Model"],
          ["ADO load errors","Source file format change","Validate source file; check ADO link mappings"],
          ["Incorrect variances","Version mapping error","Check Manage Versions in all models"],
          ["Planning grid empty","Dimensional selector at parent level","Set selector to leaf-level member"],
          ["BS not balancing","Balancing Routine not run or new accounts unmapped","Run Balancing Routine; check cash offset and CF mappings"],
      ]) + tip("Root Cause Rule", "Most IFP issues stem from missing or incorrect mappings in the Administration pages. When something doesn't work, start there."))

page("Currency Translation", "currency-translation.html",
     "Currency triangulation — one set of rates, unlimited reporting currencies",
     ["Module 4", "Admin & Extensions", "20 min"],
     ("How Currency Translation Works", "Triangulation uses a base currency as an intermediary — enabling translation to any reporting currency from a single set of loaded rates."),
     ("Instructor Demo", "Facilitator adds a new reporting currency to the Report Currency list in real time and shows how all financial data immediately appears in the new currency."),
     ("Add a Reporting Currency", "In your workspace, add a new reporting currency to the Report Currency list. Navigate to the IS Report and confirm the new currency is available."),
     """
      <h2>The Triangulation Method</h2>
      """ + ss("Currency triangulation diagram — local currencies → base currency → reporting currencies") + """
      <p>Instead of loading rates for every possible currency pair, triangulation uses a <strong>base currency</strong> (e.g., USD) as an intermediary:</p>
      <ol>
        <li>Load exchange rates: all local currencies → base currency (one set of rates)</li>
        <li>System automatically calculates reciprocal rates: base currency → any local currency (1 ÷ loaded rate)</li>
        <li>Combine: local → base rate × reciprocal base → reporting rate = local → any reporting currency</li>
      </ol>

      <h2>Adding a New Reporting Currency</h2>
      """ + tip("It's This Simple", "To add a new reporting currency: (1) add the currency to the Report Currency list, (2) give it its currency code. Done. All financial data is immediately available in that currency — no module changes, no additional rate loads.") + """
      <h2>Rate Types</h2>
      """ + table(["Rate Type","Typical Use"],[
          ["Month-end rate","Balance sheet accounts (snapshot at period end)"],
          ["Monthly average rate","Most P&amp;L accounts (average over the period)"],
          ["Historical rate","Equity section accounts (locked at original transaction rate)"],
          ["Statistical rate","Non-financial metrics (headcount, units) — always = 1; never needs loading"],
      ]) + """
      <h2>Architecture</h2>
      """ + table(["Component","Purpose"],[
          ["Currency Flat","List of all local currencies in the model"],
          ["Report Currency dimension","Currencies available for reporting — add/remove freely"],
          ["Exchange Rate data","Loaded rates: local currency → base currency"],
          ["Entity → Local Currency attribute","Each leaf entity has its local currency as an attribute"],
          ["GL Account → Rate Type attribute","Each IS and BS account has a rate type assigned"],
      ]) + note("Statistical Rate Type", "The Statistical Rate Type is used for non-financial metrics like headcount and FTE counts. These always translate at a rate of 1 (no conversion needed). You don't need to load statistical rates — the system assumes 1 automatically."))

page("Common Extensions", "extensions.html",
     "Custom planning methods, external integrations, and configure vs. extend decisions",
     ["Module 4", "Admin & Extensions", "20 min"],
     ("When to Extend", "IFP is a configurable foundation — when configuration covers the need vs. when an extension is required."),
     ("Instructor Demo", "Facilitator walks through the steps to create a custom planning method (Headcount × Rate) in a pre-built example."),
     ("Extension Design", "Looking at FictoCorp's requirements, identify 2 scenarios that would require an extension vs. 2 that can be addressed through configuration."),
     """
      <h2>Configure vs. Extend</h2>
      """ + table(["Scenario","Approach"],[
          ["Need a new planning method","Extend — add to Planning Methods list, configure SYS module, add line items, update LISS"],
          ["Need basic allocations","Configure — built in out of the box"],
          ["Need sophisticated allocations (waterfalls, multi-step)","Extend to Profitability application — integrates with IFP"],
          ["Need more than 8 dimensions","Bespoke model build — cannot configure within IFP hard limit"],
          ["Need CapEx by department","Extend — entity-to-dept mapping in General Admin for simple cases"],
          ["Need employee-level HC detail","Extend to OWP or WFB — both integrate natively with IFP HC"],
          ["Need external revenue planning","Configure — 'In another model → load to FP' option + DAT Margin Planning Import module"],
      ]) + """
      <h2>Creating a Custom Planning Method: Headcount × Rate</h2>
      <p>This example creates a method that drives expense from HC data — eliminating double-entry for headcount-driven expenses.</p>
      <ol>
        <li><strong>Add to Planning Methods list</strong> — create new entry with unique code</li>
        <li><strong>Configure in SYS by Planning Methods</strong> — set business area (expense/margin/BS), add description (shown as context help to users)</li>
        <li><strong>Add line items to input module</strong>:
          <ul>
            <li>Boolean "Is Method in Use?" — controls when calculation runs</li>
            <li>Headcount Amount — formula: actuals → from DAT module; forecast → from HC integration module</li>
            <li>Rate per Head — formula scope = Actuals version (historical calculated; forecast manually entered)</li>
            <li>Adjustment — always manual input</li>
            <li>Final Amount — if not in use → 0; if actuals → actual GL amount; else → HC × Rate + Adjustment</li>
          </ul>
        </li>
        <li><strong>Apply DCA</strong> — hide line items from users when method isn't applicable to the account</li>
        <li><strong>Update LISS</strong> — map which line items display to users and which are for the forecast method</li>
        <li><strong>Assign to accounts</strong> — change the account's method in FIN – IS – Manage Planning Methods</li>
        <li><strong>Add to Final Amount</strong> — include the new method's output in the Final Amount formula</li>
      </ol>
      """ + tip("Final Amount Is The Only Output", "The Final Amount line item is the only value pulled into downstream modules. All other calculation line items exist only for intermediate computation and don't need summarization turned on.") + """
      <h2>External Integration Patterns</h2>
      """ + table(["Integration","DAT Module","Pattern"],[
          ["OWP (Operational Workforce Planning)","DAT Headcount Planning Import","OWP → ADO → DAT module → FP calculations"],
          ["Consensus Margin Planning (CMP)","DAT Margin Planning Import","CMP → ADO → DAT module → FP calculations"],
          ["External CapEx system","DAT Capex IS + BS Planning Import","External → ADO → 2 DAT modules → FP calculations"],
          ["Project Planning (PCP)","DAT Project Planning Import","PCP → ADO → DAT module → FP calculations"],
      ]))

print("Module 4 done.")

# ─── Reference ────────────────────────────────────────────────────────────────

page("Inter-Module Data Flows", "inter-module-flows.html",
     "How all 4 models connect and data flows between them",
     ["Reference"],
     None, None, None,
     """
      <h2>Data Flow Overview</h2>
      """ + ss("IFP inter-module flow diagram — Administration feeding all modules, HC/CapEx feeding FP, all modules feeding Reporting") + """
      <h2>Module-to-Module Connections</h2>
      """ + table(["From","To","What Flows","How"],[
          ["Administration (ADO)","All Spoke Models","Planning hierarchies (Entity, Dept, IS/BS accounts)","ADO push"],
          ["Headcount (HC)","Financial Planning (FP)","Workforce costs by GL account","FIN – Import from HC Model action"],
          ["CapEx (CE)","Financial Planning (FP)","Depreciation expense, PP&amp;E, cash payments","FIN – Import from CapEx Model action"],
          ["Revenue/COGS (FP)","Balance Sheet (FP)","AR (via DSO), COGS → inventory, net income → retained earnings","Internal FP formulas"],
          ["OpEx (FP)","Balance Sheet (FP)","AP (via DPO), accrued expenses → current liabilities","Internal FP formulas"],
          ["All FP modules","Top-Down Summary (FP)","Bottom-up totals for target comparison","Internal FP formulas"],
          ["All FP modules","Reporting &amp; Analysis","Consolidated IS, BS, CF data","Internal FP formulas"],
      ]) + """
      <h2>Reporting: Available Reports</h2>
      """ + table(["Report","Source Data"],[
          ["Income Statement","Revenue/COGS + OpEx + HC (via import) + CapEx depreciation (via import)"],
          ["Balance Sheet","BS account planning + CapEx PP&amp;E + Revenue-driven AR + OpEx-driven AP"],
          ["Cash Flow (Indirect)","BS account changes mapped to CF lines + manual adjustments"],
          ["Variance Analysis (IS/BS)","Any two versions compared"],
          ["Currency Variance Analysis","FX rate changes between periods"],
          ["Product Outlier Analysis","Revenue/COGS data by product"],
          ["Management Reporting Pack","Consolidated IS + BS + CF + dynamic commentary"],
      ]) + """
      <h2>Administration as the Data Hub</h2>
      <ol>
        <li>Source systems → Admin model (via ADO)</li>
        <li>Admin model → mapping workbench (source → planning)</li>
        <li>Admin model → all spoke models (via ADO push)</li>
      </ol>
      """ + imp("Always Complete Admin Mappings First", "Every planning model (FP, HC, CE) depends on Admin model for its list structures. Always complete Admin mappings before loading actuals or starting a new planning cycle."))

page("What's Coming", "whats-coming.html",
     "Known v2.0 limitations, roadmap items, and ecosystem integrations",
     ["Reference"],
     None, None, None,
     """
      <h2>Known V2.0.0 Limitations Targeted for Future Releases</h2>
      """ + table(["Limitation","Current Behavior","Planned Fix"],[
          ["Top-Down dynamic disaggregation","Manual input at each level","To be reintroduced in a future release"],
          ["Finance Analyst / CoPlanner","Embedded but pending full availability","Full GA release planned"],
          ["ADO link failures","5 known broken links out of box","Fixes expected in future PAF releases"],
          ["Dependent dropdowns","Don't generate consistently","No fix timeline — manual repair required"],
          ["Line item codes not in generation","Must be populated manually","No fix expected near term"],
      ]) + """
      <h2>Ecosystem Integrations</h2>
      <ul>
        <li><strong>Operational Workforce Planning (OWP)</strong> — position/employee-level headcount detail; integrates natively with IFP HC</li>
        <li><strong>Workforce Budgeting (WFB)</strong> — additional workforce planning capability (name TBC)</li>
        <li><strong>Consensus Margin Planning (CMP)</strong> — revenue and margin planning from a commercial lens; feeds into IFP via DAT module</li>
        <li><strong>Financial Consolidation</strong> — downstream from IFP for consolidation and disclosure management</li>
      </ul>

      <h2>Application Framework Roadmap</h2>
      <ul>
        <li>Centralized upgrades mean customers receive IFP improvements without manual rebuilds</li>
        <li>Order Management team takes over Application Delivery process once all apps are on AAF</li>
        <li>Partner enablement materials updated with each major release</li>
      </ul>

      <h2>Stay Current</h2>
      """ + table(["Resource","Where"],[
          ["Release notes and application updates","Anaplan Community — community.anaplan.com"],
          ["Updated partner training","Anaplan Enablement Portal"],
          ["Finance Applications CoE","financeapplications@anaplan.com"],
          ["General application questions","applications@anaplan.com"],
      ]))

# Q&A — Using exact RPM callout-note pattern with section headers and <hr>
qanda_body = """
      <h2>How to Use This Page</h2>
      <p>These are real questions from IFP v2.0 technical enablement sessions, answered by the Anaplan Finance Applications team. Organized by topic for reference during customer conversations, discovery sessions, and implementation planning.</p>
      <hr>

      <h2>Application Framework &amp; Configuration</h2>

      <div class="callout-note">
        <p><strong>Q: Can I re-run the Application Framework after generation to change configuration choices?</strong></p>
        <p><strong>A:</strong> Yes — you can re-configure and re-generate. However, post-generation customizations (extensions, manual fixes, data loads) may need to be reapplied. Plan your configuration carefully upfront to minimize re-generation. Catch dimension and hierarchy decisions before starting post-gen work.</p>
      </div>

      <div class="callout-note">
        <p><strong>Q: What happens if generation fails partway through?</strong></p>
        <p><strong>A:</strong> Check the PAF configuration logs to see where it failed. Common causes: (1) missing roles — you need all 4 roles; (2) wrong default tenant — Integration Admin must generate in their default tenant; (3) source model not included in generation. Fix the issue and re-generate.</p>
      </div>

      <div class="callout-note">
        <p><strong>Q: Can a customer use their existing data hub instead of ADO?</strong></p>
        <p><strong>A:</strong> Yes — but they'll need to configure import actions during implementation instead of using ADO links. ADO is the recommended and supported path for new implementations. If a customer has an existing data hub they want to keep, factor in the import action configuration work during scoping.</p>
      </div>

      <div class="callout-note">
        <p><strong>Q: What's the maximum number of hierarchy levels? What happens if a customer needs more?</strong></p>
        <p><strong>A:</strong> Maximum 8 levels per model, minimum 2 levels. If a customer needs more, this would require a bespoke extension — the Application Framework enforces this limit. Have the dimension conversation early in discovery to identify any risk.</p>
      </div>

      <hr>
      <h2>Headcount</h2>

      <div class="callout-note">
        <p><strong>Q: Can IFP plan at the named employee level?</strong></p>
        <p><strong>A:</strong> Not directly — IFP HC plans at job/role level to protect PII. For position or employee-level detail, use OWP (Operational Workforce Planning), which integrates natively with IFP HC, or Workforce Budgeting (WFB). Both feed into IFP via the DAT Headcount Planning Import module.</p>
      </div>

      <div class="callout-note">
        <p><strong>Q: Why can't I delete a job from the job metadata page?</strong></p>
        <p><strong>A:</strong> You can only delete jobs with no headcount assigned. The system checks total FTE in HRIS Actuals — if any FTE is assigned, the Delete checkbox is read-only. Remove or reassign headcount first, then the checkbox becomes available.</p>
      </div>

      <div class="callout-note">
        <p><strong>Q: How do pay band deviations work? Do they block planning?</strong></p>
        <p><strong>A:</strong> Deviations do NOT block planning — they flag for management review. The system calculates a Cost Multiplier for each job (fully loaded cost ÷ salary). If it falls outside the min/max benchmark range from the pay band, a deviation is shown in the Insights Panel. Finance teams can review and approve exceptions.</p>
      </div>

      <hr>
      <h2>CapEx</h2>

      <div class="callout-note">
        <p><strong>Q: Can we plan CapEx by department?</strong></p>
        <p><strong>A:</strong> Not directly in v2.0 — CapEx is Entity-level only. The entity-to-department mapping in CapEx General Admin distributes depreciation to the correct P&amp;L dimensions. For full department-level CapEx planning (e.g., each department owns its own CapEx budget), an extension is required.</p>
      </div>

      <div class="callout-note">
        <p><strong>Q: What is CWIP (Construction Work in Progress)?</strong></p>
        <p><strong>A:</strong> Assets flagged as CWIP don't start depreciating until the in-service date is reached. Until then, the asset sits in the CWIP balance sheet account. This handles scenarios like a facility being built — you're spending money but it's not yet depreciating.</p>
      </div>

      <hr>
      <h2>Balance Sheet &amp; Cash Flow</h2>

      <div class="callout-note">
        <p><strong>Q: Why do BS inputs represent activity instead of balances?</strong></p>
        <p><strong>A:</strong> IFP uses a roll-forward approach: Closing Balance = Last Actual Balance ± Activity. This means entering nothing still produces a valid result — the last actual balance simply rolls forward. You only need to enter changes, not restated balances each period. This is simpler and less error-prone than balance-based input.</p>
      </div>

      <div class="callout-note">
        <p><strong>Q: The balance sheet isn't balancing — what should I check?</strong></p>
        <p><strong>A:</strong> In order: (1) Run the Balancing Routine, (2) verify all BS accounts have cash offset categories assigned, (3) verify all leaf-level BS accounts have cash flow mappings, (4) confirm FIN – Import from CapEx Model has been run recently. Most BS balance issues trace to missing cash offset or CF mappings.</p>
      </div>

      <hr>
      <h2>ADO &amp; Data</h2>

      <div class="callout-note">
        <p><strong>Q: Why do some ADO links fail to generate out of the box?</strong></p>
        <p><strong>A:</strong> Known PAF generation issue. The following are documented as broken or missing: Vendor Hierarchy (FP), SYS by J2/J3 Job (HC), SYS by J4 Job (HC — no link created at all), and Job Grade (HC). These must be created manually. This is expected and documented — plan for it in your post-generation schedule.</p>
      </div>

      <div class="callout-note">
        <p><strong>Q: In what order should I load data?</strong></p>
        <p><strong>A:</strong> Always: (1) complete Admin model source-to-planning mappings first, (2) push planning hierarchies and master data to all spoke models, (3) then load actuals. Actuals loads will fail if planning lists aren't populated yet. Source files must match the template format exactly.</p>
      </div>

      <hr>
      <h2>Currency</h2>

      <div class="callout-note">
        <p><strong>Q: How do I add a new reporting currency?</strong></p>
        <p><strong>A:</strong> Add the currency to the Report Currency list and give it its ISO code. That's it — all financial data is immediately available in the new currency via triangulation. No module changes, no additional rate loading, no code changes required.</p>
      </div>

      <div class="callout-note">
        <p><strong>Q: What is the Statistical Rate Type used for?</strong></p>
        <p><strong>A:</strong> Non-financial metrics like headcount and FTE counts. These always translate at a rate of 1 (no currency conversion makes sense for headcount). You don't need to load statistical rates — the system automatically assumes 1. This prevents headcount numbers from being multiplied by FX rates in reporting.</p>
      </div>

      <div class="callout-note">
        <p><strong>Q: What is the base currency and does it matter which one we choose?</strong></p>
        <p><strong>A:</strong> The base currency is the intermediary in the triangulation calculation — all loaded exchange rates go from local currencies INTO the base. Any currency can be the base. USD is the most common choice. The base currency itself is always available in reporting. The choice affects which rates you need to load (always local → base) but doesn't affect reporting capability.</p>
      </div>
"""

page("Q&A from Sessions", "qanda.html",
     "Real questions from IFP v2.0 technical enablement sessions — organized by topic",
     ["Reference"],
     None, None, None,
     qanda_body)

page("Resources & Downloads", "resources.html",
     "Documentation, ADO templates, provisioning, and support contacts",
     ["Reference"],
     None, None, None,
     """
      <h2>Documentation</h2>
      <ul>
        <li><strong>IFP v2.0.0 Configuration Guide</strong> — complete Application Framework question set, post-generation tasks, ADO setup, known issues</li>
        <li><strong>IFP v2.0.0 Application Admin Guide</strong> — ongoing admin runbook, monthly checklist, troubleshooting</li>
        <li><strong>IFP v2.0.0 Application Overview</strong> — suite positioning, capabilities, v1.3 vs v2.0 comparison</li>
        <li><strong>IFP v2.0.0 Process Definition Document</strong> — all process pages per module, process flow diagrams</li>
        <li><strong>IFP v2.0.0 Product Glossary</strong> — complete terminology reference</li>
        <li><strong>IFP_Provision_V2.pdf</strong> — step-by-step provisioning requirements</li>
      </ul>

      <h2>ADO Data Templates</h2>
      """ + table(["Prefix","Module","Key Files"],[
          ["IFP_DH_*","Admin model","Source Account IS/BS, Source Entity, Source Department"],
          ["IFP_FP_*","Financial Planning","Trial Balance IS/BS/Margin, Customer Hierarchy, CF Hierarchy"],
          ["IFP_HC_*","Headcount","HRIS Actuals, Job Hierarchy, Job Grade, Employment Types"],
          ["IFP_CE_*","CapEx","Asset Types, Existing Asset Depreciation, BS Subledger"],
          ["IFP_SH_*","Shared","FX Rates, Currencies, Geography, Product, Vendor, FA Hierarchies"],
      ]) + """
      <h2>Provisioning Steps</h2>
      <ul>
        <li>Request Polaris workspace via CSBP in Salesforce (min 100GB)</li>
        <li>Create Delivery Request — Application Delivery #1 (Customer), #2 (Partner), or #3 (Upgrade)</li>
        <li>Email <strong>financeapplications@anaplan.com</strong> for Finance Apps CoE support</li>
      </ul>

      <h2>Support Contacts</h2>
      """ + table(["Need","Contact"],[
          ["Workspace provisioning","financeapplications@anaplan.com"],
          ["General application questions","applications@anaplan.com"],
          ["Implementation support (first 3 projects)","Finance Apps CoE — included non-chargeable"],
          ["Community &amp; release notes","community.anaplan.com"],
          ["Help documentation","help.anaplan.com"],
      ]))

page("Glossary", "glossary.html",
     "Complete IFP v2.0.0 product terminology",
     ["Reference"],
     None, None, None,
     """
      <h2>A</h2><dl>
      <dt>Account Type</dt><dd>Defines the normal balance (debit/credit) for each account along with the appropriate sign (+/-).</dd>
      <dt>Accounts Payable (AP)</dt><dd>Money owed by a company to its suppliers for goods or services purchased on credit.</dd>
      <dt>Accounts Receivable (AR)</dt><dd>Money owed to a company by its customers for goods or services sold on credit.</dd>
      <dt>Accrual</dt><dd>An expense or revenue recognized before cash changes hands.</dd>
      <dt>ADO</dt><dd>Anaplan Data Orchestrator — the data integration layer that replaces the data hub model in IFP v2.0.</dd>
      <dt>Allocation Driver</dt><dd>A factor used to distribute costs from one area to another (e.g., FTE, manual percentage).</dd>
      <dt>AOP</dt><dd>Annual Operating Plan.</dd>
      <dt>Asset Disposal</dt><dd>Removal of an asset from a company's balance sheet through sale, retirement, or abandonment.</dd>
      <dt>Asset Type</dt><dd>Classification of assets: building and facilities, computer hardware, computer software, equipment, vehicles, leasehold improvements.</dd>
      <dt>Attrition</dt><dd>The reduction of employees due to resignation, retirement, or other reasons.</dd>
      </dl>
      <h2>B–C</h2><dl>
      <dt>Balance Sheet</dt><dd>A financial statement reporting a company's assets, liabilities, and equity at a specific point in time.</dd>
      <dt>Capital Expenditures (CapEx)</dt><dd>Funds used to acquire, upgrade, and maintain physical assets.</dd>
      <dt>Cash Flow</dt><dd>The movement of cash both into and out of a company.</dd>
      <dt>COGS % of Revenue</dt><dd>A planning method that calculates COGS as a user-defined percentage of revenue.</dd>
      <dt>Contingent Worker</dt><dd>A non-permanent worker, such as a freelancer or contractor.</dd>
      <dt>Currency Triangulation</dt><dd>A method using a base currency as intermediary to translate between any two currencies from a single set of rates.</dd>
      <dt>CWIP</dt><dd>Construction Work in Progress — assets being built that are not yet in service and not yet depreciating.</dd>
      </dl>
      <h2>D–F</h2><dl>
      <dt>Days Inventory Outstanding (DIO)</dt><dd>Measure of how long it takes a company to sell its inventory.</dd>
      <dt>Days Payables Outstanding (DPO)</dt><dd>Measure of how long it takes a company to pay its suppliers.</dd>
      <dt>Days Sales Outstanding (DSO)</dt><dd>Measure of how long it takes a company to collect payment from customers.</dd>
      <dt>Depreciation</dt><dd>The reduction in the value of an asset over time due to wear and tear.</dd>
      <dt>Driver</dt><dd>A factor that influences costs or revenues.</dd>
      <dt>Dynamic Bulk Copy</dt><dd>Functionality to copy data from a source version to a target version.</dd>
      <dt>FTE</dt><dd>Full-Time Equivalent — a measure of the number of full-time employees.</dd>
      <dt>FX Rate</dt><dd>Foreign exchange rate.</dd>
      </dl>
      <h2>G–J</h2><dl>
      <dt>Gross Margin</dt><dd>The difference between revenue and cost of goods sold.</dd>
      <dt>Headcount (HC)</dt><dd>The number of employees in an organization; also refers to the IFP Headcount planning model.</dd>
      <dt>Income Statement (P&amp;L)</dt><dd>A financial statement reporting a company's financial performance over a period of time.</dd>
      <dt>Integration Admin</dt><dd>A required Anaplan role for generating IFP applications — must generate in their default tenant.</dd>
      <dt>Job Grade</dt><dd>A classification level used to group jobs with similar compensation ranges and pay bands.</dd>
      </dl>
      <h2>L–P</h2><dl>
      <dt>Line Item Detail</dt><dd>A planning method where amounts are entered on the Line Item Detail page with extra dimension attributes.</dd>
      <dt>Net Fixed Assets</dt><dd>The book value of fixed assets, net of accumulated depreciation.</dd>
      <dt>OpEx</dt><dd>Operating Expenses.</dd>
      <dt>P&amp;L</dt><dd>Profit and Loss statement — synonymous with Income Statement.</dd>
      <dt>Polaris</dt><dd>Anaplan's calculation engine built for sparse data sets and large dimensionality — required entitlement for IFP.</dd>
      <dt>Progressive Disclosure</dt><dd>A UX design approach that shows only the inputs relevant to the current selection, reducing complexity and errors.</dd>
      </dl>
      <h2>R–V</h2><dl>
      <dt>Rolling Moving Average</dt><dd>A planning method that calculates values using a rolling average of prior periods.</dd>
      <dt>Statistical Rate Type</dt><dd>A special FX rate type for non-financial metrics (headcount, units) that always translates at a rate of 1.</dd>
      <dt>TD</dt><dd>Top Down.</dd>
      <dt>Top-Down Planning</dt><dd>A planning approach where high-level executive targets are set first, then compared against bottom-up plans.</dd>
      <dt>Trial Balance</dt><dd>A list of all general ledger accounts and their balances at a specific point in time.</dd>
      <dt>Units X Rate</dt><dd>A planning method that calculates amounts by multiplying units by a rate (e.g., hours × rate per hour).</dd>
      <dt>Version</dt><dd>A snapshot of the financial plan at a particular point in time (e.g., Current Forecast, AOP, Prior Year).</dd>
      </dl>""")

page("Facilitator Guide", "facilitator.html",
     "Workshop timing, setup checklist, debrief answer keys, and tips",
     ["Reference"],
     None, None, None,
     """
      <h2>Workshop Timing (Full Day)</h2>
      """ + table(["Time","Module","Format","Duration"],[
          ["09:00–09:30","Getting Started — Overview, FictoCorp, IFP Suite, Anaplan Way","Presentation + Discussion","30 min"],
          ["09:30–10:15","Module 1 — App Framework, ADO, Model Architecture","Presentation + Demo","45 min"],
          ["10:15–10:30","Break","—","15 min"],
          ["10:30–11:30","Config Walkthrough + Lab A Setup + Start Lab A","Presentation + Lab","60 min"],
          ["11:30–12:30","Complete Lab A + Debrief","Lab + Discussion","60 min"],
          ["12:30–13:30","Lunch","—","60 min"],
          ["13:30–14:00","Post-Gen Checklist + Data Load via ADO","Presentation","30 min"],
          ["14:00–15:00","Lab B — Full 3-Statement Configuration","Lab","60 min"],
          ["15:00–16:00","Module Walkthroughs (Revenue, OpEx, HC, CapEx, BS, Top-Down, Reporting)","Demo","60 min"],
          ["16:00–16:30","Admin Runbook, Currency Translation, Extensions, Q&amp;A","Presentation + Q&amp;A","30 min"],
      ]) + """
      <h2>Pre-Workshop Setup Checklist</h2>
      <ul class="checklist">
        <li>Polaris workspace provisioned (minimum 100GB)</li>
        <li>All participants have all 4 required roles in the tenant</li>
        <li>Finance Apps CoE added to workspace (financeapplications@anaplan.com)</li>
        <li>IFP v2.0 template model accessible in workspace</li>
        <li>ADO dataspace configured for the workshop workspace</li>
        <li>Sample data files (BOM ADO templates) uploaded to ADO Source Data</li>
        <li>Demo environment calendar set to July (6+6 forecast — displays well on screen)</li>
        <li>HC and CE spoke models mapped to workshop workspace copy</li>
        <li>Test generation completed successfully (verify all 4 models generate)</li>
      </ul>

      <h2>Lab Debrief Answer Keys</h2>

      <h3>Lab A</h3>
      <ol>
        <li>Name mismatch → modules and line items not renamed correctly throughout the model; generation inconsistencies</li>
        <li>HC Option A because job-level workforce planning is needed; CapEx Option B because Phase 1 doesn't need asset-level detail — GL-level approach is sufficient and simpler</li>
        <li>Re-generation required; Geography would be added to Revenue/COGS, OpEx, and Top-Down modules; all post-gen work must be redone</li>
        <li>Minimum 2 levels, maximum 8 levels per model</li>
        <li>The Application Framework cannot exclude models from generation — always generates all 4; delete the unused model manually</li>
      </ol>

      <h3>Lab B</h3>
      <ol>
        <li>Cash Offset Accounts define how each BS account affects cash. Missing category = missing cash movement in CF statement = incorrect cash balance</li>
        <li>Retained earnings must roll forward sequentially — July's retained earnings affect August's opening balance; cannot process August until July is complete</li>
        <li>Options: (1) entity-to-department mapping in CapEx General Admin for simple allocation; (2) custom extension with department-level CapEx input module</li>
        <li>3 levels if you need Country/Region/Sub-region granularity; 2 levels for simple Americas/EMEA split; fewer levels = better performance</li>
        <li>Direct Load: load source file as-is (hierarchies, flat lists). Transformation Load: join source data with Admin model planning mappings before loading (actuals data)</li>
      </ol>

      <h2>Common Participant Questions &amp; Answers</h2>

      <div class="callout-note">
        <p><strong>"Can we change configuration after generation?"</strong></p>
        <p><strong>A:</strong> Yes, but re-generation overwrites post-gen customizations. Scope carefully upfront. Catch dimensionality errors before starting post-gen work.</p>
      </div>

      <div class="callout-note">
        <p><strong>"Why does ADO have broken links out of the box?"</strong></p>
        <p><strong>A:</strong> Known PAF generation issues. Always check the broken links list (Vendor Hierarchy, SYS by J2/J3/J4 Job, Job Grade) and create manually before data loading. Plan for this in your project schedule.</p>
      </div>

      <div class="callout-note">
        <p><strong>"When does dynamic top-down disaggregation come back?"</strong></p>
        <p><strong>A:</strong> On the roadmap, no committed date in v2.0.0. Manual input at each level in the meantime. Set customer expectations accordingly.</p>
      </div>

      <div class="callout-note">
        <p><strong>"Can we have more than 8 dimensions?"</strong></p>
        <p><strong>A:</strong> Hard limit — 8 dimensions maximum. Customers requiring more need a bespoke model build as extension. Identify dimension requirements early in discovery.</p>
      </div>

      <h2>Tips for a Smooth Workshop</h2>
      <ul>
        <li>Have participants work in pairs for labs — one drives, one navigates the guide</li>
        <li>Pre-generate Lab A before the session so you can help debug quickly</li>
        <li>Set realistic expectations about PAF generation time (~5–10 minutes)</li>
        <li>Flag the known broken ADO links proactively — participants will hit them immediately</li>
        <li>Demo environment: always set current period to July — 6+6 layout looks much better than 9+3</li>
        <li>The "one method per account" change from v1.x is often confusing — explain it explicitly during the Config Walkthrough</li>
        <li>During BS demo: always mention the activity-based planning concept upfront — it's the most counterintuitive aspect for first-time users</li>
      </ul>
      """)

print("All pages done.")
