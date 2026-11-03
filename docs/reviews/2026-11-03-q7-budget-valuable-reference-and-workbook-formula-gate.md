# Q7: Budget method selected; grant workbooks statically inspected

**Consumer decision:** [Nonprofit Budget Narrative](https://github.com/dh2211/nonprofit-agents/blob/e1a247b8743d53e12677774bf67f6453b7f692b1/skills/npo-budget-narrative/SKILL.md) (17/20, static) is a **VALUABLE REFERENCE** for **Finance → Budgeting**. Its practical method is to recompute rate × quantity, reconcile totals and explain the grant ask from real source evidence. One complete Git tree and MIT LICENSE pinned. **Not approved to install or use unchanged.**

**Recovered binary evidence:** GitHub can return Base64 for the three XLSX files even though its normal UTF-8 reader rejects them. We decoded the bytes and inspected the ZIP directory and underlying XML without running code. The three workbooks contain **130 formula tags**, 8 visible worksheets, no encrypted ZIP entries and no detected macro/external-link container parts or hidden sheet states. This is **static structural inspection**, not a security scan, formula recalculation or functional demonstration.

**Serious logic gap:** The Go/No-Go Scorecard checks `COUNTIF(Gates!C2:C7,"No")>0` then allows **GO** if the weighted score is high enough. Unanswered gate cells are *not* explicit `No`; for example 75 points with five blank gates follows the GO branch. Qualification disposition: **DO NOT rely on its final GO recommendation until blank gates are explicitly held** and the behavior is re-tested.

**Fictional arithmetic oracle:** Four line items (Instructors 120×$50, Materials 200×$15, Transport 60×$30, Evaluation 30×$40) sum to **$12,000**. Incorrectly claiming $2,000 for transport yields an apparent **$12,200** budget, **$200 overstated**. Required behavior is a HOLD with human reconciliation, not silent changes. We checked this arithmetic independently, **not by executing the source skill**.

**Outstanding:** The source XLSX files have not been recalculated by Excel/LibreOffice or another compatible engine, their interactive validation behavior is not qualified, no real funder eligibility policy was checked, and no sensitive financial data were accessed. Do not authorize file edits, submissions, uploads or expense claims from source exposure.

**Current bounded public shelf:** 20 conceptual Valuable References / 10 canonical domains / 19 positively represented subdomains / 0 unchanged-use approvals. The earlier Q6 19-method catalog/graph remain historical. The Q4 210/247 research-link figure is a separate baseline.

[Machine-readable evidence](../../registry/discovery/q7-budget-workbook-and-valuable-reference-20261103.json) · [Current 20-reference shelf](../../registry/consumer-positive-references-q7-20261103.json) · [Current capability graph](../assets/capability-evidence-and-valued-methods-q7-20261103.svg).
