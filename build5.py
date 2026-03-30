#!/usr/bin/env python3
"""IFP Workshop Builder — Module 4 + Reference + Index"""
import sys
sys.path.insert(0, '/home/gstoa/.openclaw/workspace/projects/work/workshops/ifp-workshop')
from build import page, write, callout, screenshot, table, build_nav, PAGE_ORDER

# ─── Module 4 ─────────────────────────────────────────────────────────────────

write("admin-runbook.html", page("Admin Runbook", "./admin-runbook.html", """
<h1>Admin Runbook</h1>
<p>This runbook documents all ongoing administration tasks for IFP v2.0 — what to do every month, every planning cycle, and how to troubleshoot common issues.</p>

<h2>Monthly Checklist</h2>
<ol>
  <li><strong>Update Current Period</strong> — Model Settings → Time → update current period in all 4 models</li>
  <li><strong>Run ADO pipelines</strong> — refresh hierarchies, flat lists, attributes, actuals, and FX rates</li>
  <li><strong>Review mappings</strong> — check Admin model for any unmapped new departments, entities, or accounts from source systems</li>
</ol>

<h2>Planning Cycle Checklist</h2>
<ol>
  <li>Update time ranges if the planning horizon has changed</li>
  <li>Update the versions list with any new planning versions</li>
  <li>Run version-to-version copy actions to seed new versions from existing data</li>
  <li>Review all administration pages — planning methods, account settings, BS/CF mappings</li>
  <li>Confirm all HC and CapEx cross-model imports are up to date before opening planning</li>
</ol>

<h2>Version Management</h2>
<p>Location: Administration → FIN/HC/CapEx – Manage Versions</p>
<ul>
  <li>Map each native Anaplan version to the custom comparison version list</li>
  <li>Enable custom comparison versions via <code>Override = TRUE</code> in SYS by Version Variance Comparison</li>
  <li>Run data copy actions to seed new scenario versions</li>
  <li>Version names must be <strong>identical across Admin, FP, HC, and CE</strong></li>
</ul>
""" + callout("warning", "Version Mismatch = Incorrect Variances", "If variance reports show unexpected results, check version mappings in all Manage Versions pages. A missing or incorrect mapping is the most common cause.") + """
<h2>Planning Methods Management</h2>
<p>Location: Administration → FIN – IS – Manage Planning Methods</p>
<ul>
  <li>Review at start of each planning cycle</li>
  <li>Update when new accounts are added or business rules change</li>
  <li>Accounts with missing methods produce no forecast values downstream</li>
  <li>When adding a new custom method: add to Planning Methods list → configure in SYS module → update input module line items → update LISS → update admin mapping module</li>
</ul>

<h2>Account Settings (IS and BS)</h2>
<ul>
  <li>Review whenever new accounts are added to the Chart of Accounts</li>
  <li>IS accounts: set reporting sign (debit/credit) and account type</li>
  <li>BS accounts: set planning method, cash offset category, and cash flow mapping</li>
  <li>Incorrect signs affect report display — values may show as negative when they should be positive</li>
</ul>

<h2>Troubleshooting Quick Reference</h2>
""" + table(
    ["Symptom", "Most Likely Cause", "Fix"],
    [
        ["Blank dashboards", "Mappings missing or selective access", "Check Admin mapping pages; check user roles"],
        ["HC costs not in FP", "GL account mapping or import not run", "Check HC – Update Mappings; run FIN – Import from HC Model"],
        ["CapEx not in FP", "GL account mapping, entity-dept mapping, or import not run", "Check CapEx – General Admin; run FIN – Import from CapEx Model"],
        ["ADO load errors", "Source file format change or transformation view mismatch", "Validate source file format; check ADO link mappings"],
        ["Incorrect variances", "Version mapping error", "Check Manage Versions pages in all models"],
        ["Planning grid empty", "Dimensional selector at parent level", "Change selector to leaf-level member"],
        ["BS not balancing", "Balancing Routine not run, or new accounts unmapped", "Run Balancing Routine; check cash offset and CF mappings"],
    ]
) + callout("tip", "Root Cause 80% of Issues", "Most IFP issues stem from missing or incorrect mappings in the Administration pages. When something doesn't work, start there.")))

write("currency-translation.html", page("Currency Translation", "./currency-translation.html", """
<h1>Currency Translation</h1>
<p>IFP v2.0 uses <strong>currency triangulation</strong> — a redesigned approach that requires only a single set of exchange rates yet can translate to any number of reporting currencies instantly, without code changes.</p>

<h2>How Triangulation Works</h2>
""" + screenshot("Currency triangulation diagram — local currencies → base currency → reporting currencies") + """
<p>The method uses a <strong>base currency</strong> (e.g., USD) as an intermediary:</p>
<ol>
  <li>Load exchange rates from all local currencies → base currency (one set of rates)</li>
  <li>System automatically calculates reciprocal rates: base currency → any local currency (1 ÷ loaded rate)</li>
  <li>Combine: local → base rate × reciprocal base → reporting rate = local → reporting rate</li>
  <li>All reporting currencies are available simultaneously from the single rate set</li>
</ol>

<h2>Adding a New Reporting Currency</h2>
""" + callout("tip", "It's This Simple", "To add a new reporting currency: (1) add the currency to the Report Currency list, (2) give it its currency code. Done. All financial data is immediately available in that currency — no module changes, no additional rate loads.") + """
<h2>Architecture Components</h2>
""" + table(
    ["Component", "Purpose"],
    [
        ["Currency Flat", "List of all local currencies used in the model"],
        ["Report Currency dimension", "Currencies available for reporting — add/remove freely"],
        ["Exchange Rate data", "Loaded rates: local currency → base currency"],
        ["Rate Types", "Month-end, monthly average, historical — determines which rate applies to each GL account"],
        ["Statistical Rate Type", "Always = 1; used for non-financial metrics (headcount, units); never needs loading"],
        ["Entity → Local Currency attribute", "Each leaf entity has its local currency as an attribute"],
        ["GL Account → Rate Type attribute", "Each IS and BS account has a rate type attribute"],
    ]
) + """
<h2>Rate Types</h2>
""" + table(
    ["Rate Type", "Typical Use"],
    [
        ["Month-end rate", "Balance sheet accounts (snapshot at period end)"],
        ["Monthly average rate", "Most P&amp;L accounts (average over the period)"],
        ["Historical rate", "Equity section accounts (locked at original transaction rate)"],
        ["Statistical rate", "Non-financial metrics — always translates at 1 (no loading needed)"],
    ]
) + """
<h2>Calculation Flow</h2>
<ol>
  <li><strong>Exchange Rate Module</strong> — stores loaded rates + calculates reciprocal rates automatically</li>
  <li><strong>Rates by Rate Type for Reporting Currencies</strong> — calculates rates from each local currency → each reporting currency, per rate type</li>
  <li><strong>Rates by Entity</strong> — pre-calculates entity-level rates to avoid double lookups in output modules (Polaris optimization)</li>
  <li><strong>Output Modules</strong> — look up entity rate for GL account's rate type × financial data = translated amount</li>
</ol>
""" + callout("note", "Performance Design", "Pre-calculating rates by entity is a deliberate Polaris performance optimization. It avoids a double lookup (entity → currency → rate) in every output module calculation.")))

write("extensions.html", page("Common Extensions", "./extensions.html", """
<h1>Common Extensions</h1>
<p>IFP v2.0 is a configurable foundation — most customers extend it to meet their specific requirements. This page documents the most common extensions and how to approach them.</p>

<h2>When to Configure vs. When to Extend</h2>
""" + table(
    ["Scenario", "Approach"],
    [
        ["Need a new planning method", "Extend — add to Planning Methods list, configure in SYS module, add line items to input module, update LISS"],
        ["Need allocations (basic)", "Configure — allocation functionality is built in"],
        ["Need sophisticated allocations (waterfalls, multi-step, reciprocal)", "Extend to Profitability application — it integrates with IFP"],
        ["Need more than 8 dimensions", "Bespoke model build required — cannot configure within IFP"],
        ["Need CapEx by department", "Extend — entity-to-department mapping in General Admin handles simple cases; custom module needed for full dimensionality"],
        ["Need employee-level HC detail", "Extend to OWP or WFB — both integrate natively with IFP HC model"],
        ["Need external revenue planning", "Configure — use 'In another model → load to FP' option + DAT Margin Planning Import module"],
    ]
) + """
<h2>Creating a Custom Planning Method</h2>
<p>Example: Headcount × Rate method (drives expense from HC data rather than generic units)</p>
<ol>
  <li><strong>Add to Planning Methods list</strong> — create new entry with unique code</li>
  <li><strong>Configure in SYS by Planning Methods module</strong> — set business area applicability (expense, margin, BS), add description (shown as context help to users)</li>
  <li><strong>Add calculation line items to input module</strong> (e.g., INP Expense Planning):
    <ul>
      <li>Boolean: "Is Method in Use?" — controls when calculation runs</li>
      <li>Headcount Amount — formula: actuals → from DAT module; forecast → from HC integration module</li>
      <li>Rate per Head — formula scope = Actuals version (historical rate auto-calculated; forecast manually entered)</li>
      <li>Adjustment — always manual, no formula</li>
      <li>Final Amount — formula: if method not in use → 0; if actuals month → actual GL amount; else → HC × Rate + Adjustment</li>
    </ul>
  </li>
  <li><strong>Apply DCA (Dynamic Cell Access)</strong> — hide line items from users when method isn't applicable</li>
  <li><strong>Update Line Item Subset (LISS)</strong> — map line items to display and forecast method</li>
  <li><strong>Assign to accounts</strong> — in FIN – IS – Manage Planning Methods, change the account's method assignment</li>
  <li><strong>Add to Final Amount</strong> — ensure new method's output is included in the Final Amount formula</li>
</ol>
""" + callout("tip", "Final Amount Is The Only Output", "The Final Amount line item is the only value pulled into downstream modules. All other line items in the planning method module are for calculation purposes only — they don't need summarization turned on.") + """
<h2>Integrating External Planning Sources</h2>
""" + table(
    ["Integration", "DAT Module to Load", "Pattern"],
    [
        ["Operational Workforce Planning (OWP)", "DAT Headcount Planning Import", "OWP → ADO → DAT module → FP calculations"],
        ["Consensus Margin Planning (CMP)", "DAT Margin Planning Import", "CMP → ADO → DAT module → FP calculations"],
        ["External CapEx system", "DAT Capex IS + BS Planning Import", "External → ADO → 2 DAT modules → FP calculations"],
        ["Project Planning (PCP)", "DAT Project Planning Import", "PCP → ADO → DAT module → FP calculations"],
    ]
) + """
<h2>Top-Down to Bottom-Up Integration</h2>
<p>IFP can push Top-Down targets to downstream planning models:</p>
<ul>
  <li>Source: INP TD Expense Targets + INP TD Gross Profit Targets in FP model</li>
  <li>Targets: OWP, CMP, or other downstream Anaplan models</li>
  <li>Dimensionality: L2 of each hierarchy dimension + Version + Year (not monthly)</li>
  <li>Pattern: FP → ADO → Target Model (or direct model-to-model if ADO unavailable)</li>
</ul>
"""))

# ─── Reference ────────────────────────────────────────────────────────────────

write("inter-module-flows.html", page("Inter-Module Data Flows", "./inter-module-flows.html", """
<h1>Inter-Module Data Flows</h1>
<p>Understanding how IFP's modules connect is essential for troubleshooting, configuration, and explaining the solution to customers.</p>

<h2>High-Level Flow</h2>
""" + screenshot("IFP inter-module flow diagram — Administration feeding all modules, HC/CapEx feeding FP, all modules feeding Reporting") + """
<h2>Module-to-Module Connections</h2>
""" + table(
    ["From", "To", "What Flows", "How"],
    [
        ["Administration (ADO)", "All Spoke Models", "Planning hierarchies (Entity, Dept, IS/BS accounts)", "ADO push"],
        ["Headcount (HC)", "Financial Planning (FP)", "Workforce costs by GL account", "FIN – Import from HC Model action"],
        ["CapEx (CE)", "Financial Planning (FP)", "Depreciation expense, PP&amp;E, cash payments", "FIN – Import from CapEx Model action"],
        ["Revenue/COGS (FP)", "Balance Sheet (FP)", "AR (via DSO), COGS drives inventory, net income → retained earnings", "Internal FP model formulas"],
        ["OpEx (FP)", "Balance Sheet (FP)", "AP (via DPO), accrued expenses → current liabilities", "Internal FP model formulas"],
        ["All FP modules", "Top-Down Summary (FP)", "Bottom-up totals for target comparison", "Internal FP model formulas"],
        ["All FP modules", "Reporting &amp; Analysis (FP)", "Consolidated IS, BS, CF data", "Internal FP model formulas"],
    ]
) + """
<h2>Reporting Module: Available Reports</h2>
""" + table(
    ["Report", "Source Data"],
    [
        ["Income Statement", "Revenue/COGS + OpEx + HC (via import) + CapEx depreciation (via import)"],
        ["Balance Sheet", "BS account planning + CapEx PP&amp;E + Revenue-driven AR + OpEx-driven AP"],
        ["Cash Flow (Indirect)", "BS account changes mapped to CF lines + manual CF adjustments"],
        ["Variance Analysis (IS/BS)", "Any two versions compared"],
        ["Currency Variance Analysis", "FX rate changes between periods"],
        ["Product Outlier Analysis", "Revenue/COGS data by product"],
        ["Management Reporting Pack", "Consolidated IS + BS + CF + commentary"],
    ]
) + """
<h2>Administration as the Data Hub</h2>
<p>The Administration model is the single source of truth for planning structures:</p>
<ol>
  <li>Source systems → Admin model (via ADO)</li>
  <li>Admin model → mapping workbench (source to planning)</li>
  <li>Admin model → all spoke models (via ADO push)</li>
</ol>
<p>Every planning model (FP, HC, CE) depends on Admin model for its list structures. Always complete Admin mappings before loading actuals or starting a new planning cycle.</p>
"""))

write("whats-coming.html", page("What's Coming", "./whats-coming.html", """
<h1>What's Coming</h1>
<p>IFP v2.0.0 is the current release. This page documents known planned improvements and roadmap items.</p>

<h2>Known V2.0.0 Limitations Targeted for Future Releases</h2>
""" + table(
    ["Limitation", "Current Behavior", "Planned Fix"],
    [
        ["Top-Down dynamic disaggregation", "Manual input at each level — no auto-cascade", "Dynamic disaggregation to be reintroduced in a future release"],
        ["Finance Analyst / CoPlanner", "Embedded but pending full availability", "Full GA release planned"],
        ["ADO link failures", "5 known broken links out of box", "Fixes expected in future PAF releases"],
        ["DCA on dependent dropdowns", "Don't generate consistently", "No fix timeline — manual repair required"],
        ["Line item codes not in generation", "Must be populated manually", "No fix expected near term"],
    ]
) + """
<h2>Anaplan Application Framework — Ongoing Improvements</h2>
<ul>
  <li>Order Management team will take over the Application Delivery process once all applications are on AAF</li>
  <li>Centralized upgrades mean customers will receive IFP improvements without manual rebuilds</li>
  <li>Partner enablement materials and workshop content updated with each major release</li>
</ul>

<h2>IFP Ecosystem Integrations</h2>
<ul>
  <li><strong>Operational Workforce Planning (OWP)</strong> — native integration for position/employee-level headcount detail beyond IFP's job-level planning</li>
  <li><strong>Workforce Budgeting (WFB)</strong> — additional workforce planning capability (name TBC)</li>
  <li><strong>Consensus Margin Planning (CMP)</strong> — revenue and margin planning from a commercial lens, feeds into IFP via DAT module</li>
  <li><strong>Financial Consolidation</strong> — downstream from IFP for consolidation and disclosure management</li>
</ul>

<h2>Stay Current</h2>
<ul>
  <li>Anaplan Community — release notes and application updates</li>
  <li>Anaplan Enablement Portal — updated partner training materials</li>
  <li>Finance Applications CoE — financeapplications@anaplan.com</li>
</ul>
""", tsd=False))

write("qanda.html", page("Q&A from Sessions", "./qanda.html", """
<h1>Q&amp;A from Sessions</h1>
<p>Frequently asked questions from IFP v2.0 technical enablement sessions.</p>

<h2>Application Framework &amp; Configuration</h2>
<dl>
  <dt>Can I re-run the Application Framework to change configuration choices after generation?</dt>
  <dd>Yes — you can re-configure and re-generate. However, post-generation customizations (extensions, manual fixes) may need to be reapplied. Plan your configuration carefully upfront to minimize re-generation.</dd>

  <dt>What happens if generation fails partway through?</dt>
  <dd>Check the PAF configuration logs to see exactly where it failed. Common causes: missing roles (need all 4), wrong default tenant (Integration Admin must generate in their default tenant), or source model not included in generation. Fix the issue and re-generate.</dd>

  <dt>Can a customer use their existing data hub instead of ADO?</dt>
  <dd>Yes — but they'll need to configure import actions during implementation instead of using ADO links. ADO is the recommended and supported path for new implementations.</dd>

  <dt>What's the maximum number of hierarchy levels?</dt>
  <dd>Maximum 8 levels per model, minimum 2 levels. The hierarchy screen shows combined levels across selected models.</dd>
</dl>

<h2>Headcount</h2>
<dl>
  <dt>Can IFP plan at the employee level?</dt>
  <dd>Not directly — IFP HC plans at job/role level to protect PII. For position or employee-level detail, use OWP (Operational Workforce Planning) which integrates natively with IFP HC, or WFB (Workforce Budgeting).</dd>

  <dt>Why can't I delete a job?</dt>
  <dd>You can only delete jobs with no headcount assigned. Check the "Not In Use" indicator — if any FTE is assigned via HRIS Actuals, the Delete checkbox is read-only. Reassign or remove headcount first.</dd>

  <dt>How do pay band deviations work?</dt>
  <dd>The system calculates a Cost Multiplier for each job (fully loaded cost ÷ salary). If this falls outside the min/max benchmark multiplier range from the pay band, a deviation is flagged in the Insights Panel. Deviations don't block planning — they flag for management review.</dd>
</dl>

<h2>CapEx</h2>
<dl>
  <dt>Can I plan CapEx by department?</dt>
  <dd>Not directly in v2.0 — CapEx is Entity-level only. The entity-to-department mapping in CapEx General Admin handles distribution of depreciation to P&amp;L dimensions. For full dept-level CapEx, an extension is required.</dd>

  <dt>What is CWIP (Construction Work in Progress)?</dt>
  <dd>Assets flagged as CWIP don't start depreciating until the in-service date is reached. The asset sits in the CWIP balance sheet account until it's placed in service.</dd>
</dl>

<h2>Balance Sheet &amp; Cash Flow</h2>
<dl>
  <dt>Why do BS inputs represent activity, not balances?</dt>
  <dd>IFP's BS uses a roll-forward approach: Closing Balance = Last Actual Balance ± Activity. This means entering nothing still produces a valid result (last actual rolls forward). You only need to enter changes, not restated balances each period.</dd>

  <dt>The balance sheet isn't balancing — what do I check?</dt>
  <dd>1) Run the Balancing Routine, 2) Check all BS accounts have cash offset categories, 3) Check all cash flow mappings are complete, 4) Ensure FIN – Import from CapEx Model has been run recently.</dd>
</dl>

<h2>ADO &amp; Data</h2>
<dl>
  <dt>Why do some ADO links fail to generate out of the box?</dt>
  <dd>Known issue with the Application Framework — Vendor Hierarchy (FP), SYS by J2/J3 Job (HC), SYS by J4 Job (HC — no link created), and Job Grade (HC) are documented broken links. Create them manually using the ADO setup steps in the Config Guide.</dd>

  <dt>In what order should I load data?</dt>
  <dd>Always: hierarchies and master data first, then actuals. Push Admin model planning lists to all spoke models before loading any actuals. Source files must be in the correct format — validate against the ADO templates.</dd>
</dl>

<h2>Currency</h2>
<dl>
  <dt>How do I add a new reporting currency?</dt>
  <dd>Add the currency to the Report Currency list in the application. Give it its ISO code. That's it — all financial data is immediately available in the new currency via triangulation. No module changes or additional rate loading required.</dd>

  <dt>What is the Statistical Rate Type used for?</dt>
  <dd>Non-financial metrics like headcount and FTE counts. These metrics always translate at a rate of 1 (no conversion). You don't need to load statistical rates — the system automatically assumes a rate of 1.</dd>
</dl>
""", tsd=False))

write("resources.html", page("Resources & Downloads", "./resources.html", """
<h1>Resources &amp; Downloads</h1>

<h2>Documentation</h2>
<ul>
  <li><strong>IFP v2.0.0 Configuration Guide</strong> — complete Application Framework question set, post-generation tasks, ADO setup, known issues</li>
  <li><strong>IFP v2.0.0 Application Admin Guide</strong> — ongoing admin runbook, monthly checklist, troubleshooting</li>
  <li><strong>IFP v2.0.0 Application Overview</strong> — suite positioning, capabilities, v1.3 vs v2.0 comparison</li>
  <li><strong>IFP v2.0.0 Process Definition Document</strong> — all process pages per module, process flow diagrams</li>
  <li><strong>IFP v2.0.0 Product Glossary</strong> — complete terminology reference</li>
</ul>

<h2>Data Templates (ADO)</h2>
<p>All ADO data templates are available in the Technical Product BOM:</p>
<ul>
  <li>IFP_DH_* — Data Hub source mappings (Admin model)</li>
  <li>IFP_FP_* — Financial Planning (Trial Balance IS/BS/Margin, Customer Hierarchy, CF Hierarchy)</li>
  <li>IFP_HC_* — Headcount (HRIS Actuals, Job Hierarchy, Job Grade, Employment Types)</li>
  <li>IFP_CE_* — CapEx (Asset Types, Existing Asset Depreciation, BS Subledger)</li>
  <li>IFP_SH_* — Shared (FX Rates, Currencies, Geography, Product, Vendor, FA Hierarchies)</li>
</ul>

<h2>Provisioning</h2>
<ul>
  <li>Request Polaris workspace via CSBP in Salesforce</li>
  <li>Create Delivery Request (Application Delivery #1, #2, or #3) in Salesforce</li>
  <li>Contact: <strong>financeapplications@anaplan.com</strong> for Finance Apps CoE support</li>
  <li>Contact: <strong>applications@anaplan.com</strong> for general application questions</li>
</ul>

<h2>Support Contacts</h2>
""" + table(
    ["Need", "Contact"],
    [
        ["Workspace provisioning", "financeapplications@anaplan.com"],
        ["Application questions", "applications@anaplan.com"],
        ["Implementation support", "Briehanna Wilde (App Delivery Process)"],
        ["Partner enablement", "Anaplan Enablement Portal"],
        ["Community &amp; release notes", "community.anaplan.com"],
    ]
) + """
<h2>Helpful Links</h2>
<ul>
  <li><a href="https://community.anaplan.com" target="_blank">Anaplan Community</a></li>
  <li><a href="https://help.anaplan.com" target="_blank">Anaplan Help (help.anaplan.com)</a></li>
  <li><a href="https://support.anaplan.com" target="_blank">Anaplan Support</a></li>
</ul>
""", tsd=False))

write("glossary.html", page("Glossary", "./glossary.html", """
<h1>Glossary</h1>
<p>Complete IFP v2.0.0 product terminology reference.</p>

<h2>A</h2><dl>
<dt>Account Type</dt><dd>Defines the normal balance (debit/credit) for each account along with the appropriate sign (+/-)</dd>
<dt>Accounts Payable (AP)</dt><dd>Money owed by a company to its suppliers for goods or services purchased on credit</dd>
<dt>Accounts Receivable (AR)</dt><dd>Money owed to a company by its customers for goods or services sold on credit</dd>
<dt>Accrual</dt><dd>An expense or revenue recognized before cash changes hands</dd>
<dt>Accumulated Depreciation</dt><dd>The total amount of depreciation expense recognized for an asset over its life</dd>
<dt>Allocation Driver</dt><dd>A factor used to distribute costs from one area to another (e.g., FTE, manual percentage)</dd>
<dt>AOP</dt><dd>Annual Operating Plan</dd>
<dt>Asset Disposal</dt><dd>The removal of an asset from a company's balance sheet through sale, retirement, or abandonment</dd>
<dt>Asset Type</dt><dd>Classification of assets: building and facilities, computer hardware, computer software, equipment, vehicles, leasehold improvements</dd>
<dt>Attrition</dt><dd>The reduction of employees due to resignation, retirement, or other reasons</dd>
</dl>

<h2>B</h2><dl>
<dt>Balance Sheet</dt><dd>A financial statement reporting a company's assets, liabilities, and equity at a specific point in time</dd>
<dt>Base Salary</dt><dd>Fixed compensation paid to an employee, excluding bonuses, benefits, or other forms of compensation</dd>
</dl>

<h2>C</h2><dl>
<dt>Capital Expenditures (CapEx)</dt><dd>Funds used to acquire, upgrade, and maintain physical assets such as property, buildings, technology, or equipment</dd>
<dt>Cash Flow</dt><dd>The movement of cash both into and out of a company</dd>
<dt>COGS % of Revenue Planning Method</dt><dd>Calculates COGS based on a user-defined percentage of revenue</dd>
<dt>Contingent Worker</dt><dd>A non-permanent worker, such as a freelancer or contractor</dd>
<dt>Cost of Goods Sold (COGS)</dt><dd>The direct costs attributable to the production of the goods or services sold by a company</dd>
<dt>Currency Triangulation</dt><dd>A method using a base currency as intermediary to translate between any two currencies from a single set of rates</dd>
<dt>Currency Variance</dt><dd>Differences in financial results due to changes in foreign exchange rates</dd>
</dl>

<h2>D</h2><dl>
<dt>Days Inventory Outstanding (DIO)</dt><dd>Measure of how long it takes a company to sell its inventory</dd>
<dt>Days Payables Outstanding (DPO)</dt><dd>Measure of how long it takes a company to pay its suppliers</dd>
<dt>Days Sales Outstanding (DSO)</dt><dd>Measure of how long it takes a company to collect payment from customers</dd>
<dt>Depreciation</dt><dd>The reduction in the value of an asset over time due to wear and tear</dd>
<dt>Direct Input Planning Method</dt><dd>Allows you to directly enter amounts</dd>
<dt>Driver</dt><dd>A factor that influences costs or revenues</dd>
<dt>Dynamic Bulk Copy</dt><dd>Functionality to copy data from a source version to a target version</dd>
</dl>

<h2>E–F</h2><dl>
<dt>EBIT</dt><dd>Earnings Before Interest and Taxes</dd>
<dt>Fixed Average Planning Method</dt><dd>Calculates the average expense over a fixed number of periods</dd>
<dt>FTE</dt><dd>Full-Time Equivalent — a measure of the number of full-time employees</dd>
<dt>FX Rate</dt><dd>Foreign exchange rate</dd>
<dt>$ Growth Planning Method</dt><dd>Plan expenses based on a dollar growth amount from a prior period</dd>
</dl>

<h2>G–I</h2><dl>
<dt>Gross Margin</dt><dd>The difference between revenue and cost of goods sold</dd>
<dt>Headcount (HC)</dt><dd>The number of employees in an organization</dd>
<dt>Income Statement (P&amp;L)</dt><dd>A financial statement reporting a company's financial performance over a period of time</dd>
<dt>Inventory Turns Planning Method</dt><dd>Calculates inventory based on the number of times inventory is sold and replaced per period</dd>
</dl>

<h2>J–N</h2><dl>
<dt>Job Grade</dt><dd>A classification level used to group jobs with similar compensation ranges</dd>
<dt>Joint Venture</dt><dd>A business undertaking by two or more parties for a specific purpose</dd>
<dt>Line Item Detail</dt><dd>Detailed information for each operating expense item, including description and extra dimensions</dd>
<dt>Net Fixed Assets</dt><dd>The book value of fixed assets, net of accumulated depreciation</dd>
<dt>Net Income</dt><dd>A company's profit after all expenses, including taxes and interest</dd>
</dl>

<h2>O–P</h2><dl>
<dt>OpEx</dt><dd>Operating Expenses</dd>
<dt>P&amp;L</dt><dd>Profit and Loss statement (synonymous with Income Statement)</dd>
<dt>Payment Plan</dt><dd>The schedule for paying for capital expenditures</dd>
<dt>Percent of A/R Planning Method</dt><dd>Calculates balance sheet accounts as a percentage of accounts receivable</dd>
<dt>Prior Run Rate Planning Method</dt><dd>Calculates expenses based on a prior period's run rate</dd>
<dt>Progressive Disclosure</dt><dd>A UX design approach that shows only the inputs relevant to the current selection, reducing complexity and errors</dd>
</dl>

<h2>R–V</h2><dl>
<dt>Rolling Moving Average Planning Method</dt><dd>Calculates expenses using a rolling average of prior periods</dd>
<dt>Statistical Rate Type</dt><dd>A special FX rate type for non-financial metrics that always translates at a rate of 1</dd>
<dt>TD</dt><dd>Top Down</dd>
<dt>Top-Down Planning</dt><dd>A planning approach where high-level targets are set first, then compared against detailed bottom-up plans</dd>
<dt>Trial Balance</dt><dd>A list of all general ledger accounts and their balances at a specific point in time</dd>
<dt>Units X Rate Planning Method</dt><dd>Calculates amounts by multiplying units by a rate</dd>
<dt>Version</dt><dd>A snapshot of the financial plan at a particular point in time (e.g., Current Forecast, AOP, Prior Year)</dd>
</dl>
""", tsd=False))

write("facilitator.html", page("Facilitator Guide", "./facilitator.html", """
<h1>Facilitator Guide</h1>
<p>This guide supports workshop facilitators delivering the IFP v2.0 Technical Enablement Workshop.</p>

<h2>Workshop Timing (Full Day)</h2>
""" + table(
    ["Time", "Module", "Format", "Duration"],
    [
        ["09:00–09:30", "Getting Started — Overview, Case Study, IFP Suite", "Presentation", "30 min"],
        ["09:30–10:00", "Anaplan Way for Apps + Provisioning", "Presentation", "30 min"],
        ["10:00–10:45", "Module 1 — App Framework, ADO, Model Architecture", "Presentation + Demo", "45 min"],
        ["10:45–11:00", "Break", "—", "15 min"],
        ["11:00–12:00", "Config Walkthrough + Lab A Setup", "Presentation", "60 min"],
        ["12:00–13:00", "Lab A — Configure FictoCorp", "Hands-On Lab", "60 min"],
        ["13:00–14:00", "Lunch", "—", "60 min"],
        ["14:00–14:30", "Post-Generation Checklist + Data Load via ADO", "Presentation", "30 min"],
        ["14:30–15:30", "Lab B — Full 3-Statement Configuration", "Hands-On Lab", "60 min"],
        ["15:30–16:30", "Module Walkthroughs (key modules)", "Demo", "60 min"],
        ["16:30–17:00", "Admin Runbook, Extensions, Q&amp;A", "Presentation + Q&amp;A", "30 min"],
    ]
) + """
<h2>Pre-Workshop Setup Checklist</h2>
<ul>
  <li>✅ Workspace provisioned (minimum 100GB Polaris)</li>
  <li>✅ All participants have all 4 required roles in the tenant</li>
  <li>✅ Finance Apps CoE added to workspace (financeapplications@anaplan.com)</li>
  <li>✅ IFP v2.0 template model accessible in workspace</li>
  <li>✅ ADO dataspace configured for the workshop workspace</li>
  <li>✅ Sample data files (BOM ADO templates) uploaded to ADO Source Data</li>
  <li>✅ Demo environment calendar set to July (6+6 forecast — displays well on screen)</li>
  <li>✅ HC and CE spoke models mapped to the workshop workspace copy</li>
</ul>

<h2>Lab Debrief Answer Keys</h2>

<h3>Lab A Debrief Answers</h3>
<ol>
  <li>Name mismatch between question response and hierarchy rename → generation inconsistencies, modules/line items may not be renamed correctly throughout the model</li>
  <li>HC Option A because FictoCorp needs job-level workforce planning; CapEx Option B because Phase 1 doesn't need asset-level CapEx detail — simpler GL-level approach is sufficient</li>
  <li>Adding Geography after generation would require re-generating the application — Geography would be added to Revenue/COGS, OpEx, and Top-Down modules. All affected modules would be re-generated.</li>
  <li>Minimum 2 levels, maximum 8 levels per model</li>
  <li>The Application Framework cannot exclude a model from generation — it always generates all 4 models. You delete the unused model manually after generation.</li>
</ol>

<h3>Lab B Debrief Answers</h3>
<ol>
  <li>Cash Offset Accounts define how each BS account affects the cash balance — critical for the indirect cash flow statement. Missing category = missing cash movements = incorrect CF statement.</li>
  <li>Retained earnings must roll forward sequentially — July's retained earnings affect August's opening balance. The routine cannot process August until July's calculation is complete.</li>
  <li>Options: (1) Use entity-to-department mapping in CapEx General Admin for simple allocation, (2) Build a custom extension with department-level CapEx input module</li>
  <li>3 levels if you need Country/Region/Sub-region; 2 levels for simple Americas/EMEA split. Fewer levels = better performance and simpler planning.</li>
  <li>Direct Load = load source file as-is, no transformation (hierarchies, flat lists). Transformation Load = requires joining source data with Admin model planning mappings before loading (actuals data).</li>
</ol>

<h2>Common Participant Questions</h2>
<ul>
  <li><strong>"Can we change configuration after generation?"</strong> — Yes, but re-generation overwrites post-gen customizations. Scope carefully upfront.</li>
  <li><strong>"Why does ADO have broken links out of the box?"</strong> — Known PAF generation issues. Always check the broken links list and create manually before data loading.</li>
  <li><strong>"When does dynamic top-down disaggregation come back?"</strong> — On the roadmap, no committed date in v2.0.0. Manual input at each level in the meantime.</li>
  <li><strong>"Can we have more than 8 dimensions?"</strong> — Hard limit. Customers requiring more need a bespoke model build as extension.</li>
</ul>

<h2>Tips for a Smooth Workshop</h2>
<ul>
  <li>Have participants work in pairs for labs — one drives, one navigates the guide</li>
  <li>Pre-answer Lab A before the session so you can help debug quickly</li>
  <li>Set realistic expectations about PAF generation time (~5–10 minutes)</li>
  <li>The known broken ADO links will catch everyone — flag them proactively before Lab A</li>
  <li>Demo environment: always set current period to July before demoing — it looks much better than a 9+3 layout</li>
</ul>
""", tsd=False))

print("Module 4 + Reference done.")

# ─── Index page ───────────────────────────────────────────────────────────────

import os
ROOT = "/home/gstoa/.openclaw/workspace/projects/work/workshops/ifp-workshop"

index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IFP v2.0 Technical Enablement Workshop</title>
  <link rel="stylesheet" href="./css/style.css">
</head>
<body>
  <div class="mobile-header">
    <button id="hamburger">☰</button>
    <span>IFP v2.0 Workshop</span>
  </div>

  <nav class="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-title">IFP v2.0 Workshop</div>
    </div>
    <ul class="nav-list">
      <li class="nav-section-title">Getting Started</li>
      <li><a class="nav-link" href="./docs/overview.html">Workshop Overview</a></li>
      <li><a class="nav-link" href="./docs/case-study.html">Case Study: FictoCorp</a></li>
      <li><a class="nav-link" href="./docs/ifp-overview.html">IFP Suite Overview</a></li>
      <li><a class="nav-link" href="./docs/anaplan-way.html">Anaplan Way for Apps</a></li>
      <li class="nav-section-title">Module 1 — Platform Foundations</li>
      <li><a class="nav-link" href="./docs/app-framework.html">Application Framework</a></li>
      <li><a class="nav-link" href="./docs/ado-overview.html">Anaplan Data Orchestrator</a></li>
      <li><a class="nav-link" href="./docs/model-architecture.html">Model Architecture</a></li>
      <li class="nav-section-title">Module 2 — Configuration Workshop</li>
      <li><a class="nav-link" href="./docs/config-walkthrough.html">App Framework Walkthrough</a></li>
      <li><a class="nav-link" href="./docs/lab-a.html">Lab A: Configure FictoCorp</a></li>
      <li><a class="nav-link" href="./docs/post-generation.html">Post-Generation Checklist</a></li>
      <li><a class="nav-link" href="./docs/data-load-ado.html">Data Load via ADO</a></li>
      <li><a class="nav-link" href="./docs/lab-b.html">Lab B: Full 3-Statement</a></li>
      <li class="nav-section-title">Module 3 — Module Walkthroughs</li>
      <li><a class="nav-link" href="./docs/revenue-cogs.html">Revenue &amp; COGS Planning</a></li>
      <li><a class="nav-link" href="./docs/opex.html">Operating Expenses</a></li>
      <li><a class="nav-link" href="./docs/headcount.html">Headcount Planning</a></li>
      <li><a class="nav-link" href="./docs/capex.html">CapEx Planning</a></li>
      <li><a class="nav-link" href="./docs/balance-sheet.html">Balance Sheet &amp; Cash Flow</a></li>
      <li><a class="nav-link" href="./docs/top-down.html">Top-Down Planning</a></li>
      <li><a class="nav-link" href="./docs/reporting.html">Reporting &amp; Analysis</a></li>
      <li class="nav-section-title">Module 4 — Admin &amp; Extensions</li>
      <li><a class="nav-link" href="./docs/admin-runbook.html">Admin Runbook</a></li>
      <li><a class="nav-link" href="./docs/currency-translation.html">Currency Translation</a></li>
      <li><a class="nav-link" href="./docs/extensions.html">Common Extensions</a></li>
      <li class="nav-section-title">Reference</li>
      <li><a class="nav-link" href="./docs/inter-module-flows.html">Inter-Module Data Flows</a></li>
      <li><a class="nav-link" href="./docs/whats-coming.html">What's Coming</a></li>
      <li><a class="nav-link" href="./docs/qanda.html">Q&amp;A from Sessions</a></li>
      <li><a class="nav-link" href="./docs/resources.html">Resources &amp; Downloads</a></li>
      <li><a class="nav-link" href="./docs/glossary.html">Glossary</a></li>
      <li><a class="nav-link" href="./docs/facilitator.html">Facilitator Guide</a></li>
    </ul>
  </nav>

  <main class="main-content">
    <div class="index-hero">
      <h1>IFP v2.0 Technical Enablement Workshop</h1>
      <p>Integrated Financial Planning &nbsp;·&nbsp; Application Framework &nbsp;·&nbsp; ADO &nbsp;·&nbsp; Full 3-Statement Planning</p>
    </div>
    <div class="content-body">
      <h2>Welcome</h2>
      <p>This lab guide accompanies the <strong>IFP v2.0 Technical Enablement Workshop</strong> — a hands-on technical program for Anaplan delivery practitioners building skills on the Integrated Financial Planning application version 2.0.</p>
      <p>The workshop covers the complete deployment lifecycle: from Application Framework configuration through post-generation setup, ADO data loading, and all 7 planning module walkthroughs. Start with the <a href="./docs/overview.html">Workshop Overview</a> to understand the full structure before diving in.</p>

      <h2>Workshop Modules</h2>

      <h3 style="margin-top:1.5rem;margin-bottom:0.5rem;color:#1e3a5f;">Getting Started</h3>
      <div class="index-nav-grid">
        <a class="index-nav-card" href="./docs/overview.html">
          <div class="inc-num">Start Here</div>
          <div class="inc-title">Workshop Overview</div>
          <div class="inc-desc">Objectives, prerequisites, structure, and how to complete the workshop</div>
        </a>
        <a class="index-nav-card" href="./docs/case-study.html">
          <div class="inc-num">Case Study</div>
          <div class="inc-title">FictoCorp Industries</div>
          <div class="inc-desc">Global manufacturing company — profile, hierarchy, and your role in every lab</div>
        </a>
        <a class="index-nav-card" href="./docs/ifp-overview.html">
          <div class="inc-num">Foundation</div>
          <div class="inc-title">IFP Suite Overview</div>
          <div class="inc-desc">6 planning modules, key capabilities, v1.3 vs v2.0 differences</div>
        </a>
        <a class="index-nav-card" href="./docs/anaplan-way.html">
          <div class="inc-num">Foundation</div>
          <div class="inc-title">Anaplan Way for Apps</div>
          <div class="inc-desc">Delivery process framework, implementation phases, provisioning requirements</div>
        </a>
      </div>

      <h3 style="margin-top:1.5rem;margin-bottom:0.5rem;color:#0066cc;">⚙️ Module 1 — Platform Foundations</h3>
      <div class="index-nav-grid">
        <a class="index-nav-card" href="./docs/app-framework.html">
          <div class="inc-num">M1 · 1</div>
          <div class="inc-title">Application Framework</div>
          <div class="inc-desc">What AAF does, the 4 generated models, configuration question flow, hierarchy setup</div>
        </a>
        <a class="index-nav-card" href="./docs/ado-overview.html">
          <div class="inc-num">M1 · 2</div>
          <div class="inc-title">Anaplan Data Orchestrator</div>
          <div class="inc-desc">ADO replaces the data hub, source-to-planning mapping, transformation views, broken ADO links</div>
        </a>
        <a class="index-nav-card" href="./docs/model-architecture.html">
          <div class="inc-num">M1 · 3</div>
          <div class="inc-title">Model Architecture</div>
          <div class="inc-desc">4 models, how they connect, data flows, dimensions, architectural decisions</div>
        </a>
      </div>

      <h3 style="margin-top:1.5rem;margin-bottom:0.5rem;color:#7e22ce;">🔧 Module 2 — Configuration Workshop</h3>
      <div class="index-nav-grid">
        <a class="index-nav-card" href="./docs/config-walkthrough.html">
          <div class="inc-num">M2 · 1</div>
          <div class="inc-title">App Framework Walkthrough</div>
          <div class="inc-desc">Every configuration question — options, implications, and FictoCorp preview</div>
        </a>
        <a class="index-nav-card" href="./docs/lab-a.html">
          <div class="inc-num">Lab A</div>
          <div class="inc-title">Configure FictoCorp</div>
          <div class="inc-desc">Hands-on: Revenue/COGS + OpEx + HC configuration and generation (45–60 min)</div>
        </a>
        <a class="index-nav-card" href="./docs/post-generation.html">
          <div class="inc-num">M2 · 3</div>
          <div class="inc-title">Post-Generation Checklist</div>
          <div class="inc-desc">Required and optional tasks — broken ADO links, time settings, UX fixes, validation</div>
        </a>
        <a class="index-nav-card" href="./docs/data-load-ado.html">
          <div class="inc-num">M2 · 4</div>
          <div class="inc-title">Data Load via ADO</div>
          <div class="inc-desc">Upload files, configure Admin mappings, build transformation views, push to spokes</div>
        </a>
        <a class="index-nav-card" href="./docs/lab-b.html">
          <div class="inc-num">Lab B</div>
          <div class="inc-title">Full 3-Statement Configuration</div>
          <div class="inc-desc">Extend FictoCorp with CapEx + Balance Sheet + Cash Flow + Geography (45–60 min)</div>
        </a>
      </div>

      <h3 style="margin-top:1.5rem;margin-bottom:0.5rem;color:#0891b2;">📊 Module 3 — Module Walkthroughs</h3>
      <div class="index-nav-grid">
        <a class="index-nav-card" href="./docs/revenue-cogs.html">
          <div class="inc-num">M3 · 1</div>
          <div class="inc-title">Revenue &amp; COGS Planning</div>
          <div class="inc-desc">Planning methods by product type, UX experience, integration with BS</div>
        </a>
        <a class="index-nav-card" href="./docs/opex.html">
          <div class="inc-num">M3 · 2</div>
          <div class="inc-title">Operating Expenses</div>
          <div class="inc-desc">Planning methods, line item detail, allocations, cross-model imports</div>
        </a>
        <a class="index-nav-card" href="./docs/headcount.html">
          <div class="inc-num">M3 · 3</div>
          <div class="inc-title">Headcount Planning</div>
          <div class="inc-desc">Job setup, pay bands, department mapping, planning inputs, cost sync to FP</div>
        </a>
        <a class="index-nav-card" href="./docs/capex.html">
          <div class="inc-num">M3 · 4</div>
          <div class="inc-title">CapEx Planning</div>
          <div class="inc-desc">Asset planning, depreciation, disposals, entity-only constraint</div>
        </a>
        <a class="index-nav-card" href="./docs/balance-sheet.html">
          <div class="inc-num">M3 · 5</div>
          <div class="inc-title">Balance Sheet &amp; Cash Flow</div>
          <div class="inc-desc">Activity-based planning, cash offset accounts, balancing routine, sub-schedules</div>
        </a>
        <a class="index-nav-card" href="./docs/top-down.html">
          <div class="inc-num">M3 · 6</div>
          <div class="inc-title">Top-Down Planning</div>
          <div class="inc-desc">Target setting at L2, v2.0 manual disaggregation limitation, variance analysis</div>
        </a>
        <a class="index-nav-card" href="./docs/reporting.html">
          <div class="inc-num">M3 · 7</div>
          <div class="inc-title">Reporting &amp; Analysis</div>
          <div class="inc-desc">IS/BS/CF reports, new statistical analysis, management pack, Finance Analyst</div>
        </a>
      </div>

      <h3 style="margin-top:1.5rem;margin-bottom:0.5rem;color:#059669;">🔑 Module 4 — Administration &amp; Extensions</h3>
      <div class="index-nav-grid">
        <a class="index-nav-card" href="./docs/admin-runbook.html">
          <div class="inc-num">M4 · 1</div>
          <div class="inc-title">Admin Runbook</div>
          <div class="inc-desc">Monthly checklist, version management, planning methods, troubleshooting</div>
        </a>
        <a class="index-nav-card" href="./docs/currency-translation.html">
          <div class="inc-num">M4 · 2</div>
          <div class="inc-title">Currency Translation</div>
          <div class="inc-desc">Triangulation method, adding reporting currencies instantly, rate types</div>
        </a>
        <a class="index-nav-card" href="./docs/extensions.html">
          <div class="inc-num">M4 · 3</div>
          <div class="inc-title">Common Extensions</div>
          <div class="inc-desc">Custom planning methods, external integrations, configure vs extend decisions</div>
        </a>
      </div>

      <h3 style="margin-top:1.5rem;margin-bottom:0.5rem;color:#6b7280;">📚 Reference</h3>
      <div class="index-nav-grid">
        <a class="index-nav-card" href="./docs/inter-module-flows.html">
          <div class="inc-num">Ref</div>
          <div class="inc-title">Inter-Module Data Flows</div>
          <div class="inc-desc">How all 4 models connect and data flows between them</div>
        </a>
        <a class="index-nav-card" href="./docs/whats-coming.html">
          <div class="inc-num">Ref</div>
          <div class="inc-title">What's Coming</div>
          <div class="inc-desc">Known v2.0 limitations, roadmap items, ecosystem integrations</div>
        </a>
        <a class="index-nav-card" href="./docs/qanda.html">
          <div class="inc-num">Ref</div>
          <div class="inc-title">Q&amp;A from Sessions</div>
          <div class="inc-desc">Frequently asked questions from IFP v2.0 enablement sessions</div>
        </a>
        <a class="index-nav-card" href="./docs/resources.html">
          <div class="inc-num">Ref</div>
          <div class="inc-title">Resources &amp; Downloads</div>
          <div class="inc-desc">Documentation, ADO templates, provisioning, support contacts</div>
        </a>
        <a class="index-nav-card" href="./docs/glossary.html">
          <div class="inc-num">Ref</div>
          <div class="inc-title">Glossary</div>
          <div class="inc-desc">Complete IFP v2.0 product terminology</div>
        </a>
        <a class="index-nav-card" href="./docs/facilitator.html">
          <div class="inc-num">Ref</div>
          <div class="inc-title">Facilitator Guide</div>
          <div class="inc-desc">Workshop timing, setup checklist, debrief answer keys, tips</div>
        </a>
      </div>

    </div>
  </main>
  <script src="./js/nav.js"></script>
</body>
</html>"""

with open(os.path.join(ROOT, "index.html"), 'w') as f:
    f.write(index_html)
print("✅ index.html")

# ─── rebuild_nav.py ───────────────────────────────────────────────────────────

rebuild_nav = '''#!/usr/bin/env python3
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
      <li><a class="nav-link ACTIVE_whats-coming" href="./whats-coming.html">What\'s Coming</a></li>
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
    nav = re.sub(r" ACTIVE_[\\w-]+", "", nav)
    
    fpath = os.path.join(DOCS, fname)
    with open(fpath, "r") as f:
        content = f.read()
    
    new_content = re.sub(r"<nav class=\\"sidebar\\".*?</nav>", nav, content, flags=re.DOTALL)
    if new_content != content:
        with open(fpath, "w") as f:
            f.write(new_content)
        print(f"  Updated nav: {fname}")
        updated += 1
    else:
        print(f"  No change: {fname}")

print(f"\\nDone. Updated {updated} files.")
'''

with open(os.path.join(ROOT, "rebuild_nav.py"), 'w') as f:
    f.write(rebuild_nav)
print("✅ rebuild_nav.py")

# ─── Add CSS for new elements ─────────────────────────────────────────────────

css_additions = """
/* ============================================================
   IFP Workshop — Additional Styles
   ============================================================ */

/* Module grid on overview pages */
.module-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

.module-card {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 1rem;
  box-shadow: var(--shadow);
}

.module-card h3 {
  font-size: 0.95rem;
  margin-bottom: 0.4rem;
  color: var(--color-primary);
}

.module-card p {
  font-size: 0.85rem;
  color: var(--color-text-muted);
  margin: 0;
}

/* TSD Banner */
.tsd-banner {
  display: flex;
  gap: 1rem;
  margin: 0 0 1.5rem;
  padding: 0.75rem 1rem;
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
}

.tsd-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex: 1;
  padding: 0.5rem;
  border-radius: var(--radius);
  font-size: 0.85rem;
}

.tsd-tell { background: #eff6ff; border-left: 3px solid #3b82f6; }
.tsd-show { background: #faf5ff; border-left: 3px solid #7c3aed; }
.tsd-do   { background: #f0fdf4; border-left: 3px solid #16a34a; }

.tsd-icon { font-size: 1.2rem; }

/* Lab banner */
.lab-banner {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.5rem;
  padding: 0.75rem 1rem;
  background: #fdf4ff;
  border: 1px solid #e9d5ff;
  border-radius: var(--radius);
  font-size: 0.9rem;
}

.lab-type { font-weight: 600; color: #7e22ce; }
.lab-duration { color: var(--color-text-muted); }

/* Screenshot placeholder */
.screenshot-placeholder {
  background: #f8fafc;
  border: 2px dashed #cbd5e1;
  border-radius: var(--radius);
  padding: 2rem;
  text-align: center;
  color: var(--color-text-muted);
  margin: 1rem 0;
  font-style: italic;
}

/* Prev/Next navigation */
.prevnext-nav {
  display: flex;
  justify-content: space-between;
  margin-top: 3rem;
  padding-top: 1rem;
  border-top: 1px solid var(--color-border);
}

.prevnext-btn {
  display: inline-flex;
  align-items: center;
  padding: 0.5rem 1rem;
  background: var(--color-primary);
  color: white;
  border-radius: var(--radius);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  transition: background 0.15s;
}

.prevnext-btn:hover { background: var(--color-primary-dark); }
"""

css_path = os.path.join(ROOT, "css", "style.css")
with open(css_path, 'a') as f:
    f.write(css_additions)
print("✅ CSS additions appended")
print("\nAll done!")
