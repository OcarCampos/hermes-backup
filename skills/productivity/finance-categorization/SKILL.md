---
name: finance-categorization
description: O'car's personal finance categorization rules — which file each type of money movement goes into. Prevents double-counting, miscategorization of transfers vs expenses, and ensures budget/income/expense reports are accurate.
category: productivity
tags: [finance, csv, budget, chile]
---

# Finance Categorization Rules

**Workspace:** `/mnt/data/Developing/hermes-workspace/finance/`

## The Four Files

| File | Purpose | Trigger |
|---|---|---|
| `2026-income.csv` | Money received from work (salary, freelance) | New money enters O'car's control |
| `expenses/YYYYMM-expenses.csv` | Money permanently leaves spending pool | Rent, savings allocation, loan payments, purchases |
| `budget/YYYYMM.csv` | Monthly plan vs actual | All expenses + shared bills (50%) |
| `account-tracker.md` | Reconciliation of transfers between own accounts | Santander → Mach, → MercadoPago, → Fintual, etc. |

## Critical Rule: Transfer vs Expense

**Money moving between O'car's own accounts is NOT an expense.** It stays in his control.

**Expenses = money leaving O'car's control permanently** (rent to Francisca, savings to Fintual, loan payments to TGR/Banco Estado, purchases).

**Transfers (tracker only, NOT budget/expenses):**
- Santander → Mach (storage/purchasing account)
- Santander → MercadoPago
- Santander → Banco Estado (own loan payment — money transfers to bank, but it's a loan, not an expense)
- Any internal account-to-account movement

## Income File Rules

**Goes in `2026-income.csv`:** Only money received from external sources.
- Monthly salary from employer
- Freelance payments from clients
- **DO NOT:** Fintual investment returns, inter-account transfers, bank interest, Tricount reimbursements

**DOES NOT go in income file:**
- Fintual savings allocation (it's money already earned — moving to savings is an expense, not new income)
- Bank transfers between own accounts (Santander → Mach)
- Investment returns or dividends
- Reimbursements from Tricount (already spent, just returned)

## Budget File Rules

**Goes in `budget/YYYYMM.csv`:** Everything in `expenses/` plus shared bills at 50%.

**Bills paid 100% but logged 50%:** Electricity, water, internet, gas. O'car pays 100%, Francisca reimburses 50% via Tricount. Log 50% to budget so the report reflects actual net outflow.

**DOES NOT go in budget:**
- Inter-account transfers (Santander → Mach, → MercadoPago, → Fintual). These go to `account-tracker.md` only.

## Expenses File Rules

**Goes in `expenses/YYYYMM-expenses.csv`:** All money permanently leaving O'car's control.
- Rent to Francisca
- Fintual savings allocation (even though it's his own account — savings counts as expense because money leaves the spending pool)
- TGR CAE debt installments
- Banco Estado student loan quotas
- One-time purchases
- Bills at 100% of value (electricity, water, etc.)

**DOES NOT go in expenses:**
- Inter-account transfers (Santander → Mach, → MercadoPago)
- Fintual investment returns (dividends, market gains — those go to `fintual-portfolio.md` only)

## Fintual Special Case

Fintual savings allocation (e.g., $1.5M from monthly salary going to Fintual Reserva + Compra):
- **NOT in income file** — it's not new money received, it's savings from existing salary
- **Goes to budget** — savings = expense (money leaves spending pool)
- **Goes to expenses** — logged as Savings expense category
- **Goes to account-tracker** — only if it's a transfer from a specific account (e.g., Santander → Fintual)

## Monthly Logging Order

1. Receive salary → log to `2026-income.csv`
2. Make transfers → log inter-account transfers to `account-tracker.md` only
3. Pay bills/loans/savings → log to both `budget/YYYYMM.csv` AND `expenses/YYYYMM-expenses.csv`
4. End of month → `monthly-budget-review` skill for comparison

## Chile-Specific Notes

- **TGR CAE:** Student debt paid via government portal. Monthly installments (e.g., 24 installments total). Log as "TGR CAE" in budget and expenses.
- **Banco Estado student loan:** Quota-based repayment (e.g., 36 quotas). Log as "Banco Estado" in budget and expenses.
- **Tricount:** Francisca uses Tricount to reimburse 50% of shared bills. O'car logs 50% in budget, Francisca handles her side separately.
- **Fintual:** Chile-based robo-advisor. USD assets (GLD gold shares, IBIT Bitcoin ETF) tracked separately in CLP equivalent.

## Common Mistakes to Avoid

1. **Fintual in income file** → Wrong. Fintual is savings, not new money received. Only salary/freelance go in income.
2. **Mach/MercadoPago loads in budget** → Wrong. These are internal transfers. Only the account-tracker.
3. **100% of shared bills** → Wrong. Log 50% — the other half comes back via Tricount.
4. **Bank transfers to loan accounts as expenses** → Wrong. Paying your own loan back to yourself (Santander → Banco Estado) is a transfer. Only log the portion that goes to TGR/government as expense.
