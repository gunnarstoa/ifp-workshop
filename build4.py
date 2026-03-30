#!/usr/bin/env python3
"""IFP Workshop Builder — Module 3: Module Walkthroughs"""
import sys
sys.path.insert(0, '/home/gstoa/.openclaw/workspace/projects/work/workshops/ifp-workshop')
from build import page, write, callout, screenshot, table

write("revenue-cogs.html", page("Revenue & COGS Planning", "./revenue-cogs.html", """
<h1>Revenue &amp; COGS Planning</h1>
<p>Revenue and Cost of Goods Sold planning in IFP v2.0 uses configurable driver-based planning methods — different methods can be assigned to different accounts and products, giving finance teams the flexibility to plan each revenue stream the way it actually works.</p>

<h2>Key Capabilities</h2>
<ul>
  <li><strong>Configurable Planning Logic</strong> — assign distinct planning methods to each revenue and COGS account, dimensioned by product</li>
  <li><strong>Granular Driver-Based Inputs</strong> — forecast at detailed level using drivers like price, units, or percentages</li>
  <li><strong>Simplified UX</strong> — Progressive Disclosure shows only the inputs required for the selected method</li>
  <li><strong>Scenario Modeling</strong> — adjust drivers and see immediate impact on margins</li>
  <li><strong>Statistical Analysis</strong> — product correlation and covariance reporting (new in v2.0)</li>
</ul>

<h2>Planning Method Configuration</h2>
<p>Location: Administration → FIN – IS – Manage Planning Methods</p>
<ul>
  <li>Methods are assigned per <strong>account AND per product</strong> — each product can use a different method</li>
  <li>Method is at account level only — not by entity or department</li>
  <li>Any account without a method assigned will NOT appear on the Revenue/COGS planning page</li>
</ul>

<h2>Common Product Planning Setups</h2>
""" + table(
    ["Product Type", "Accounts Used", "Typical Method", "Inputs"],
    [
        ["Physical Products", "Product Sales + COGS", "Units x Rate", "Units sold + price per unit"],
        ["Services / Consulting", "Services Sales + Services COGS", "Units x Rate", "Hours x rate per hour"],
        ["SaaS / Subscription", "Subscription Sales + Sub COGS", "Units x Rate", "Subscriptions x rate per subscription"],
    ]
) + screenshot("Revenue & COGS planning page — showing Units x Rate inputs for Hardware product") + """
<h2>Available Planning Methods</h2>
""" + table(
    ["Method", "Description", "Use Case"],
    [
        ["Units x Rate", "Revenue = Units × Rate", "Physical products, services (hours × rate), subscriptions"],
        ["Direct Input", "Enter amounts manually", "Simple or non-driver-based accounts"],
        ["Prior Run Rate", "Based on prior period actuals + growth %", "Stable recurring revenue"],
        ["Rolling Moving Average", "Average of prior N periods", "Smoothed trend forecasting"],
        ["COGS % of Revenue", "COGS = Revenue × user-defined %", "Margin-driven COGS accounts"],
    ]
) + """
<h2>End-User Experience</h2>
<ul>
  <li>Select product in selector — grid updates to show only that product's accounts and methods</li>
  <li>Select department — ensure you select the department that sells that product type (e.g., Services revenue → Professional Services dept)</li>
  <li>Input fields change dynamically based on the method assigned</li>
  <li>Context-sensitive instructions shown on the left panel when an account is selected</li>
  <li>Adjustment field available for every method — add or subtract from the calculated forecast</li>
</ul>
""" + callout("tip", "Wrong Department = No Data", "If you select a product but see no data, check your department selector. Service revenue may only be collected under Professional Services, not Sales. This is expected behavior, not a bug.") + """
<h2>Process Pages</h2>
""" + table(
    ["Page", "Purpose"],
    [
        ["Revenue &amp; COGS Planning", "Main planning input — dynamic grid per product + planning method"],
        ["Revenue &amp; COGS Summary", "Overview of revenue and COGS by dept/profit center, product family, and account"],
    ]
) + """
<h2>Integration with Other Modules</h2>
<ul>
  <li>Revenue drives AR calculations in Balance Sheet (Days Sales Outstanding)</li>
  <li>COGS drives Inventory in Balance Sheet (DIO, Inventory Turns)</li>
  <li>Net margin flows to retained earnings on Balance Sheet</li>
  <li>Revenue targets can be set in Top-Down Planning and compared against bottom-up here</li>
</ul>
""" + callout("note", "V2.0 Note", "End-user import templates for loading Revenue/COGS to specific GL accounts have been removed in v2.0. Customers requiring this capability need an extension.")

, tsd=True))

write("opex.html", page("Operating Expenses", "./opex.html", """
<h1>Operating Expenses</h1>
<p>Operating Expense planning in IFP v2.0 supports multiple driver-based planning methods, line item detail, and single-step allocations — all with a Progressive Disclosure UX that shows only relevant inputs for each method.</p>

<h2>Key Capabilities</h2>
<ul>
  <li><strong>Configurable Planning Logic</strong> — assign planning methods per account (one method per account in v2.0)</li>
  <li><strong>Guided User Inputs</strong> — dynamic grid shows only the inputs required for the selected method</li>
  <li><strong>Detailed Line-Item Planning</strong> — define individual line items per expense account</li>
  <li><strong>Single Step Allocations</strong> — define allocation pools and distribute costs across departments</li>
</ul>

<h2>Planning Method Configuration</h2>
<p>Location: Administration → FIN – IS – Manage Planning Methods</p>
<ul>
  <li><strong>One method per account</strong> — applies uniformly across all entities and departments</li>
  <li>Headcount-driven accounts: set to "Planned in Headcount" — hidden from OpEx planning grid</li>
  <li>Depreciation accounts: set to "Planned in CapEx" — hidden from OpEx planning grid</li>
</ul>

<h2>Available Planning Methods</h2>
""" + table(
    ["Method", "Description", "Key Input"],
    [
        ["Prior Run Rate", "Prior period × (1 + growth %)", "Growth %, # periods to go back, $ adjustment"],
        ["Units x Rate", "Units × rate", "Units (e.g., hours), Rate, Adjustment"],
        ["Rolling Moving Average", "Average of N prior periods", "# periods for average"],
        ["Direct Input", "Manual monthly entry", "Enter amounts directly"],
        ["$ Amount Growth", "Prior period + $ growth amount", "Growth amount, # periods back"],
        ["Fixed Average", "Fixed average over N periods", "# periods"],
        ["Line Item Detail", "Amounts from Line Item Detail page", "Set on Line Item Detail page"],
        ["Planned in CapEx", "Disabled — amounts from CE model", "(none — auto-populated)"],
        ["Planned in Headcount", "Disabled — amounts from HC model", "(none — auto-populated)"],
    ]
) + screenshot("OpEx planning page — showing Prior Run Rate method with growth % input") + """
<h2>Line Item Detail</h2>
<ul>
  <li>Enter description, then specify extra dimensions (vendor, functional area, geography)</li>
  <li>Once amounts are entered, dimension values cannot be changed without clearing amounts first</li>
  <li>Bottom grid shows total by vendor — select a specific vendor to see costs for that vendor across all accounts</li>
  <li>Line items planned here do <strong>not</strong> appear on the main OpEx planning page — they appear in the Summary instead</li>
</ul>

<h2>Allocations</h2>
<ul>
  <li>Define source (entity, department, account), allocation amount/%, and target</li>
  <li>Allocation basis options: FTE, even spread, manual (% or $)</li>
  <li>Manual basis input on the Allocation Basis Input page</li>
</ul>
""" + callout("important", "Allocations Extension Note", "IFP v2.0 allocations support basic single-step allocation. For sophisticated allocations (waterfalls, multi-step, reciprocal allocations, extra dimensions), the Profitability application is the right tool — it integrates with IFP.") + """
<h2>Cross-Model Imports (Admin)</h2>
<p>Always run these after making changes in HC or CapEx models:</p>
<ul>
  <li><strong>FIN – Import from HC Model</strong> — syncs workforce costs into OpEx accounts</li>
  <li><strong>FIN – Import from CapEx Model</strong> — syncs depreciation into OpEx accounts</li>
</ul>
""" + callout("warning", "Common Mistake", "Forgetting to run cross-model imports after HC or CapEx changes. If OpEx values don't reflect HC or CapEx updates, this is always the first thing to check.") + """
<h2>Process Pages</h2>
""" + table(
    ["Page", "Purpose"],
    [
        ["OpEx Planning", "Main planning grid — dynamic inputs per account/method"],
        ["OpEx Line Item Detail", "Enter detailed line items per account with extra dimensions"],
        ["OpEx Allocation Basis Input", "Enter manual basis values by entity and department per rule"],
        ["OpEx Allocation Rule Definition", "Define source, target, and allocation basis for each rule"],
        ["OpEx Summary", "Overview by entity, department, and account"],
    ]
)))

write("headcount.html", page("Headcount Planning", "./headcount.html", """
<h1>Headcount Planning</h1>
<p>Headcount planning in IFP v2.0 is one of the most significant changes from v1.x. Planning is now at the <strong>job/role level</strong> rather than named employee level — protecting sensitive PII data and enabling consistent, enterprise-grade workforce planning.</p>

""" + callout("important", "Job-Level, Not Employee-Level", "IFP v2.0 HC plans at the job role level. No sensitive employee data is stored. For position or employee-level detail, use OWP (Operational Workforce Planning) or WFB (Workforce Budgeting), which integrate natively with IFP.") + """
<h2>Setup Sequence</h2>
<ol>
  <li>Configure Job Metadata (create jobs, set grades, employment types)</li>
  <li>Map Jobs to Departments (define which roles exist where)</li>
  <li>Set Job Grade Pay Bands (compensation guardrails)</li>
  <li>Map GL Accounts (connect HC costs to FP accounts)</li>
  <li>Enter Job Cost Assumptions (specific costs per job per dept)</li>
  <li>Plan Headcount (hires, exits, transfers, attrition)</li>
</ol>

<h2>Job Metadata (HC – Review/Update Job Metadata)</h2>
""" + screenshot("HC Job Metadata page — showing job list with grade, employment type, active/valid status") + """
<p>Each job definition requires:</p>
<ul>
  <li><strong>Job Code</strong> — unique identifier</li>
  <li><strong>Display Name</strong> — job title shown to users</li>
  <li><strong>Job Parent</strong> — hierarchy placement</li>
  <li><strong>Job Grade</strong> — links to pay band assumptions</li>
  <li><strong>Employment Type</strong> — Full-time, Part-time, Seasonal</li>
  <li><strong>Allow Contingent Worker?</strong> — global flag; can be refined per department later</li>
  <li><strong>Active?</strong> — must be TRUE for job to be available for planning</li>
</ul>
""" + callout("note", "Validity Rules", "A job is only VALID if all required fields are complete AND Active = TRUE. Invalid jobs don't appear in planning grids or department mapping.") + """
<h2>Job to Department Mapping</h2>
<ul>
  <li>Assign jobs to departments — determines where each role can be planned</li>
  <li>A job can be mapped to multiple departments</li>
  <li>Allow Contingent Worker checkbox only appears if: (1) job is Assigned to dept AND (2) job has Allow Contingent Worker = TRUE globally</li>
  <li>Monitor: <strong>Number of Valid Unmapped Jobs KPI</strong> — goal is zero</li>
</ul>

<h2>Job Grade Pay Bands</h2>
""" + screenshot("HC Job Grade Pay Bands page — showing min/max salary and benefit % by grade") + """
<ul>
  <li>Set min/max base salary per job grade (company-wide guardrails)</li>
  <li>Bonus %, Benefits %, Overhead % as percentage of salary</li>
  <li>Regional differentiation by entity (India vs. US cost profiles)</li>
  <li>Total Cost Multiplier = 1 + Bonus% + Benefits% + Overhead%</li>
  <li>System validates entries — max must be ≥ min; percentages must be 0–100%</li>
</ul>

<h2>GL Account Mappings (HC – Update Mappings)</h2>
<ul>
  <li>Map each HC cost category (salary, bonus, benefits, overhead, payroll taxes) to a specific GL account</li>
  <li>Map entities to functional area, geography, vendor for FP dimensionality</li>
  <li>Must use leaf-level GL accounts — parent accounts trigger red validation errors</li>
  <li>Incorrect mappings push costs to wrong OpEx categories in FP</li>
</ul>

<h2>Job Cost Assumptions (HC – Job Cost Assumptions)</h2>
<ul>
  <li>Enter specific base salary for each job within each department</li>
  <li>Override bonus %, benefits %, overhead % from grade defaults if needed</li>
  <li><strong>Insights Panel</strong> — shows benchmark range for the grade; flags deviation if plan exceeds band</li>
  <li>Deviations don't block planning — they flag for manager review</li>
</ul>

<h2>Headcount Planning (HC – Planning)</h2>
""" + screenshot("HC Planning page — showing hires, exits, transfers by job per department") + """
<ul>
  <li>Plan by job within department</li>
  <li>Actuals shown for closed periods</li>
  <li>Manual entry for: <strong>Hires, Exits, Transfers In/Out</strong> by month</li>
  <li>Attrition based on parameter assumption (not manual)</li>
  <li>Use suppression to show only jobs with headcount</li>
  <li>Results shown in KPI cards and charts at top of page</li>
</ul>

<h2>Reporting Pages</h2>
""" + table(
    ["Page", "Shows"],
    [
        ["HC – Cost by Account", "IS cost accounts (salary, bonus, benefits, taxes) over time"],
        ["HC – Cost by Job", "Costs broken down by job role"],
        ["HC – Detailed FTE", "Total FTE, contractor FTE, FTE by grade"],
        ["HC – Version Comparison", "Compare any two versions, variance below"],
        ["HC – Summary", "KPIs, graphs, grids overview"],
    ]
) + """
<h2>After Planning — Sync to FP</h2>
<p>Navigate to Administration → Financials Model → FIN – Import from HC Model and run the import action. This pushes all HC workforce costs into the correct OpEx accounts in the FP model.</p>
"""))

write("capex.html", page("CapEx Planning", "./capex.html", """
<h1>CapEx Planning</h1>
<p>Capital Expenditure planning in IFP v2.0 allows detailed planning at the individual asset or asset class level, with automated depreciation and immediate P&amp;L/Balance Sheet impact visibility.</p>

""" + callout("warning", "Entity-Level Only", "CapEx in IFP v2.0 is planned at Entity level ONLY — no Department, Geography, Product, or other optional dimensions. The entity-to-department mapping in CapEx General Admin distributes depreciation to the correct P&amp;L dimensions. If a customer requires CapEx by department or geography, this requires an extension.") + """
<h2>Admin Setup</h2>
<h3>CapEx – General Admin</h3>
<ul>
  <li>Asset types/classes with payment plan parameters and useful life settings</li>
  <li><strong>New in v2.0:</strong> Computer Hardware and Computer Software are now separate asset classes (accounts 1712 and 1772)</li>
  <li>Entity-to-department mapping — every entity must have a department mapped</li>
  <li>Map Net Fixed Asset Values to P&amp;L Accounts</li>
  <li>Map Asset Types to Depreciation Accounts</li>
  <li>Select CWIP (Construction Work in Progress) account</li>
  <li>Select FX Rate Type for currency translation</li>
</ul>
""" + callout("important", "Leaf-Level Accounts Only", "All mappings in CapEx General Admin must point to leaf-level list members. Parent-level mappings will cause calculation failures and missing data in the FP model.") + """
<h2>End-User Planning Pages</h2>

<h3>CapEx – New Asset Purchases</h3>
""" + screenshot("CapEx New Asset Purchases page — showing asset list with order date, in-service date, depreciation method") + """
<ul>
  <li>Plan by entity + version</li>
  <li>Per asset: asset class, order date, in-service date, CWIP flag, depreciation method</li>
  <li>See P&amp;L and BS impact on timeline automatically</li>
  <li>Custom payment plan available for specific line items</li>
</ul>

<h3>CapEx – Funding Details</h3>
<ul>
  <li>Default payment plan: view parameters (read-only for end users)</li>
  <li>Custom payment plan items: enter cash payment amounts by period manually</li>
</ul>

<h3>CapEx – By Asset Type</h3>
<ul>
  <li>Plan at asset class level (aggregate, not individual asset)</li>
  <li>Available out of box — no data in demo but fully functional</li>
  <li>Choose this when customers don't need asset-level tracking</li>
</ul>

<h3>CapEx – Asset Disposals</h3>
<ul>
  <li>Enter disposal details (gross value, accumulated depreciation, proceeds)</li>
  <li>System calculates gain/loss automatically</li>
  <li>Shows P&amp;L and BS impact of disposal</li>
</ul>

<h3>CapEx – Net Fixed Asset Roll-Forward</h3>
<ul>
  <li>Read-only report showing net fixed asset roll-forward calculations</li>
</ul>

<h2>Depreciation Automation</h2>
<ul>
  <li>Depreciation calculated automatically based on in-service date, useful life, and depreciation method</li>
  <li>Existing asset depreciation loaded via ADO (IFP_CE_Existing Asset Depreciation.csv)</li>
  <li>Depreciation expense flows to OpEx P&amp;L accounts (via CapEx general admin mapping)</li>
  <li>PP&amp;E and accumulated depreciation flow to Balance Sheet</li>
</ul>

<h2>Sync to FP Model</h2>
<p>After CapEx planning: Administration → Financials Model → FIN – Import from CapEx Model.</p>
""" + callout("tip", "Polaris Performance Note", "When adding new assets, Polaris is optimized for bulk additions. Adding assets one at a time can be slow — batch your additions where possible.")))

write("balance-sheet.html", page("Balance Sheet & Cash Flow", "./balance-sheet.html", """
<h1>Balance Sheet &amp; Cash Flow Planning</h1>
<p>Balance Sheet and Cash Flow planning in IFP v2.0 models activity-based changes to BS accounts, integrating inputs from Revenue/COGS, OpEx, Headcount, and CapEx into a complete three-statement financial view.</p>

<h2>Key Concept: Activity-Based Planning</h2>
""" + callout("note", "Activity, Not Balances", "All BS inputs represent periodic ACTIVITY — not end-of-period balances. If you enter nothing, the last actual period's balance rolls forward. Formula: Closing Balance = Last Actual Balance ± Activity Entered. This means a zero-input BS still produces a sensible result.") + """
<h2>Admin Setup</h2>

<h3>FIN – BS – Manage Planning Methods</h3>
<p>Set a planning method for each BS account:</p>
""" + table(
    ["Method", "Best For"],
    [
        ["Direct Input", "Most general BS accounts"],
        ["Days Sales Outstanding (DSO)", "Accounts receivable"],
        ["Days Payable Outstanding (DPO)", "Accounts payable / trade payables"],
        ["Days Inventory Outstanding (DIO)", "Inventory accounts"],
        ["Inventory Turns", "Inventory (alternative to DIO)"],
        ["Percent of A/R", "Bad debt provision and related accounts"],
        ["Planned in CapEx", "PP&amp;E and accumulated depreciation — auto from CE model"],
    ]
) + """
<h3>FIN – BS – Manage Cash Offset Accounts</h3>
""" + callout("warning", "New Concept in v2.0", "Cash Offset Accounts define how each BS account affects the cash balance. Increases in assets reduce cash; increases in liabilities increase cash. Every BS account must be categorized. Missing mappings break the cash flow statement.") + """
<ul>
  <li>Select the Primary Cash Account at the top</li>
  <li>For each BS account, assign its offset category</li>
  <li>Cannot have more than one mapping per account (system shows red error to prevent double-counting)</li>
</ul>

<h3>FIN – BS – Cash Flow Mappings</h3>
<ul>
  <li>Map each leaf-level BS account to a cash flow line</li>
  <li>Drives the indirect cash flow statement calculation</li>
  <li>Only leaf-level accounts should be mapped</li>
</ul>

<h2>End-User Planning Pages</h2>

<h3>BS – Account Planning</h3>
""" + screenshot("BS Account Planning page — showing DSO input for Accounts Receivable") + """
<ul>
  <li>Entity level only — no department or other operational dimensions</li>
  <li>Dynamic inputs based on planning method (DSO → enter days; DIO → enter days; Direct → enter amounts)</li>
  <li>Adjustment field available for every method</li>
</ul>

<h3>Sub-Schedules</h3>
""" + table(
    ["Page", "Purpose"],
    [
        ["BS – Investments", "Enter new investment details — see IS/BS/CF impact on timeline"],
        ["BS – Intangibles &amp; Financing", "Add intangibles, short-term debt, long-term debt instruments"],
        ["BS – Leases", "Enter capital and operating lease details"],
        ["BS – Joint Ventures", "Enter JV details and see financial statement impact"],
        ["BS – Equities", "Opening share balance, historical and planned share issuance"],
    ]
) + callout("tip", "Entity Alignment Required", "For sub-schedules (investments, leases, etc.): the entity selected in the instrument must match the entity selector on the page. Misalignment = no financial data shown below the input. This is expected behavior.") + """

<h3>BS – Balancing Routine</h3>
<ul>
  <li>Runs month-by-month sequentially (July must complete before August due to retained earnings roll-forward)</li>
  <li>Runs for ALL entities, not just the selected one</li>
  <li>After running: balance sheet should balance based on the inputs provided</li>
  <li>Balancing amounts posted to accounts specified in admin</li>
</ul>

<h3>CF – Indirect Adjustments</h3>
<ul>
  <li>Shows system-calculated indirect cash flows based on BS mappings</li>
  <li>Manual fine-tuning adjustments available per line item</li>
</ul>
"""))

write("top-down.html", page("Top-Down Planning", "./top-down.html", """
<h1>Top-Down Planning</h1>
<p>Top-Down Planning allows finance leaders to set executive-level targets and compare them against bottom-up plans from the other IFP modules. In v2.0, this is a manual input process — targets are entered at Level 2 of each dimension hierarchy.</p>

""" + callout("important", "⚠️ V2.0 Limitation: No Dynamic Disaggregation", "Dynamic top-down disaggregation (automatic cascade of high-level targets to lower levels) is NOT available in IFP v2.0. All targets must be entered manually at each desired level of detail. Anaplan plans to reintroduce dynamic disaggregation in a future release.") + """
<h2>What You Can Set Targets For</h2>
""" + table(
    ["Category", "Target Types"],
    [
        ["Revenue", "Revenue Target + Gross Profit Target"],
        ["Margin", "Gross Profit % target for COGS accounts"],
        ["Operating Expenses", "General OpEx (excl. labor), Labor Cost, Total OpEx"],
        ["Headcount", "FTE and Headcount targets"],
    ]
) + """
<h2>Planning Level</h2>
<p>Top-Down targets are entered at <strong>Level 2 of each dimension hierarchy</strong>:</p>
<ul>
  <li>Products → Product Family level (L2)</li>
  <li>Customers → All Customers grouping (L2)</li>
  <li>Departments → Function level, one above cost center (L2)</li>
  <li>Geography → Region level if used (L2)</li>
  <li>All values in <strong>USD base currency</strong> — can be reported in local currency</li>
</ul>

<h2>Process Pages</h2>

<h3>TD – Planning</h3>
""" + screenshot("Top-Down Planning page — showing revenue and gross profit target inputs by product family") + """
<ul>
  <li>Manual input at each level and slice</li>
  <li>Revenue department in demo: Sales &amp; Marketing only (only dept with revenue)</li>
  <li>OpEx targets in the "no vendor" slice (can also enter by specific vendor)</li>
  <li>Pivot available to enter values across periods more easily</li>
</ul>

<h3>TD – Summary</h3>
<ul>
  <li>Compares top-down targets vs. bottom-up plans at L2 for each dimension</li>
  <li>Side-by-side: Top-Down Revenue vs. Current Year Revenue Forecast (bottom-up)</li>
  <li>Variance calculations shown</li>
</ul>

<h2>Why Targets Don't Show on Module Summary Pages</h2>
<p>By design — OpEx Summary, Revenue Summary, etc. don't show top-down targets. Reason: users may be viewing at a more granular level (L3 entity, cost center) than the L2 targets, causing confusion. All target vs. actual comparison is consolidated on the TD pages at consistent L2.</p>

<h2>Talk Track for Customer Demos</h2>
<ul>
  <li>"This shows you the top-down target vs. what the teams are planning bottom-up — alignment is visible at a glance"</li>
  <li>"We support setting targets for revenue, margin, OpEx, and now headcount in v2.0"</li>
  <li>"Dynamic disaggregation is on the roadmap — in this release, targets are entered manually at L2"</li>
</ul>
"""))

write("reporting.html", page("Reporting & Analysis", "./reporting.html", """
<h1>Reporting &amp; Analysis</h1>
<p>Reporting &amp; Analysis in IFP v2.0 brings together the outputs from all planning modules into a comprehensive set of financial reports, dashboards, and analytical tools — including two new statistical analysis capabilities introduced in v2.0.</p>

<h2>Summary Pages (per Module)</h2>
<p>Each planning module has a Summary page — revamped in v2.0 with more KPIs, graphs, and grids. These are designed to be demo-friendly and work regardless of a customer's specific dimension choices.</p>

<h2>Core Financial Reports</h2>
""" + table(
    ["Report", "Purpose"],
    [
        ["Income Statement Report", "Ad hoc IS analysis at account level; suppression to hide unused accounts"],
        ["Income Statement Variance Analysis", "Compare IS data across versions; identify variances"],
        ["Balance Sheet Report", "Detailed BS at account level; closing balance = last actual ± activity"],
        ["Balance Sheet Variance Analysis", "Compare BS data between versions"],
        ["BS &amp; CF Validations", "Is the balance sheet in balance? Cash flow validation."],
        ["Indirect Cash Flow Report", "System-calculated + manual adjustment line items"],
        ["Currency Variance Analysis", "Isolate FX rate impact between two time periods"],
    ]
) + screenshot("Reporting page — showing Income Statement Report with suppression enabled") + """
<h2>New in V2.0: Statistical Analysis</h2>

<h3>Product Sales Outlier Analysis</h3>
<ul>
  <li>Statistical analysis of product-based revenue data</li>
  <li>Parameters: number of standard deviations, basis (mean or trend line)</li>
  <li>Highlights statistical outliers in product sales across entities/periods</li>
  <li>Useful for identifying unusual trends before they become problems</li>
</ul>

<h3>Product Correlation Analysis</h3>
<ul>
  <li>Analyzes correlations between products across entities and geographies</li>
  <li>Example: shows which products are closely correlated and which are not</li>
  <li>Useful for portfolio analysis and revenue mix decisions</li>
</ul>

<h2>Management Reporting Sample</h2>
<ul>
  <li>Pre-built board-pack style output</li>
  <li>Includes: cover page, P&amp;L, Balance Sheet, Cash Flow statement, dynamic commentary</li>
  <li>Commentary is tagged to data — updates automatically as plan data changes</li>
  <li>Entity and currency selectors at top right</li>
  <li>Customize for each customer's board pack requirements</li>
</ul>
""" + screenshot("Management Reporting Sample — executive summary with P&L and dynamic commentary") + """
<h2>Anaplan Finance Analyst (CoPlanner)</h2>
<p>Embedded AI-powered insights tool available within IFP — allows users to analyze data using natural language queries. Ask questions like "What drove the variance in OpEx this quarter?" and get immediate answers from the planning data.</p>
""" + callout("note", "Finance Analyst Availability", "Finance Analyst (CoPlanner) is embedded in IFP v2.0 but pending full availability. Check with your Anaplan account team for current status.") + """
<h2>Report Scaling and Display</h2>
<ul>
  <li>Most reports are scaled to thousands — small values may appear as 0</li>
  <li>Use Suppress to hide zero/unused accounts</li>
  <li>Switch between: Amounts / Year-over-year change / Percentage change / Percent of revenue</li>
  <li>Change fiscal year selector to view different years</li>
</ul>
"""))

print("Module 3 done.")
