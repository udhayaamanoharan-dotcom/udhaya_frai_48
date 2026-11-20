# Judgment Framework – Complete before submission

Use this table to answer the three questions taught in class for each component. Confirm the exact wording of the three questions with your faculty rather than guessing.

| Component | What can go wrong? | What does the tool check? | What must a human decide/check? |
|---|---|---|---|
| Amount extraction | LLM invents or calculates an amount | Amount must match a number in the original note | Treasurer checks original claim and bill |
| Category | Claim assigned to wrong category | Allowed category list and budget lookup | Club/faculty confirms correct category |
| Bill detection | LLM says a missing bill is attached | Check bill-related wording in original note | Treasurer sees the actual bill |
| Approval threshold | Large or split claim is missed | Rs. 5,000 individual and same-day grouped threshold | Faculty reviews and decides |
| Budget | Claim pushes club over category limit | Running totals include only OK claims | Treasurer confirms budget records |
| CSV/reporting | Notes with commas break columns | Python CSV reader/writer | Student checks generated reports |
| LLM/API | Invalid response or service failure | Schema validation and error handling | Student/faculty reviews failure and fallback |

## Error comparison
- Wrongly marked OK: may create an unsafe payment recommendation and must be treated as the more serious error.
- Wrongly sent for review: delays a legitimate claim but allows a human to check it.

## Human checkpoint
The faculty treasurer signs every payment after seeing the bill. The tool does not pay or authorize.
