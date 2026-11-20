# One-page Specification – Club Expense Claim Checker

## Purpose
Build a console-based Python tool to classify club expense claims and track each club's spending against category limits. The tool does not pay claims.

## Inputs
- `claims.csv`: at least 20 claims, in date order, with columns `id,club,date,note`.
- `budgets.csv`: category limits, with columns `category,limit_per_club`.
- Notes containing commas must be quoted as CSV fields.

## LLM JSON
Return exactly: `amount` (number or null), `category` (printing/food/travel/prizes/equipment/costumes/other), `bill` (true/false), and `summary` (10 words or fewer).

## Fact checks
- The amount must match a number explicitly written in the note. Comma-formatted values such as 1,250 are treated as 1250.
- Bill is true only when the note indicates a bill, receipt, invoice, or ticket is attached; missing or later bills are false.
- The LLM must not calculate totals or infer amounts from words.

## Decision rules – apply in this order
1. Check extracted facts against the note.
2. No amount: `needs_more_info`.
3. No bill: `needs_bill`.
4. Amount above Rs. 5,000, or same club/category/date combined amount above Rs. 5,000: `needs_approval`.
5. Club spending in the category would exceed its limit: `over_budget`.
6. Otherwise: `ok_to_pay`, and add amount to the running total.

Only `ok_to_pay` claims count toward budgets.

## Outputs
`payable.csv`, `review.csv`, `results.csv`, and `summary.txt`.

## Edge cases
- Commas inside claim notes.
- Missing or ambiguous amount.
- Amount mentioned only in words.
- LLM returns invalid JSON or an unexpected category.
- Bill is missing or promised later.
- One claim exceeds Rs. 5,000.
- Multiple same-day claims may be split to avoid approval.
- Category limit is missing or would be exceeded.
- LLM API is unavailable or returns malformed data.

## Human checkpoint
The faculty treasurer signs every payment after seeing the bill. This tool never authorizes or makes a payment.
