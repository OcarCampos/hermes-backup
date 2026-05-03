---
name: monthly-budget-review
description: Monthly budget vs actual comparison — handles mismatched category structures between budget and expense CSVs, excludes one-time items, and captures O'car's budgeting philosophy.
---

# Monthly Budget Review Workflow

## Purpose
Compare monthly budgeted amounts against actual expenses, handling category structure mismatches and one-time items.

## Context
Budget CSVs (`YYYYMM.csv`) use `Category;Subcategory;Budgeted;Actual` — where "Category" is a top-level group (Housing, Food, Transport) and Subcategory is the line item (Rent, Electricity, Gas).
Expense CSVs (`YYYYMM-expenses.csv`) use flat category names that don't always match budget categories 1:1.

## Category Mapping (April 2026)
| Budget Category | Expense Category | Notes |
|----------------|-----------------|-------|
| Food | Food + Eating Outside + Supermarket | All food spending combined |
| Transportation | Transport | Budget uses "Transportation" |
| Education | Education | Only monthly Banco Estado; TGR down-payment excluded |
| Buffer | Buffer | SmartPlant, DGAC, etc. |
| Pets | Pets | Not in monthly budget — one-time costs |
| Housing | Housing | Rent + water + electricity + internet |
| Technology | Technology | |
| Services | Services | |

## One-Time Items to Exclude
- TGR down-payment ($1,686,058 in April) — from Fintual, not operational cash
- Vet visits, sanitary sand — unbudgeted surprises
- Hardware one-time purchases

## Monthly Budget vs Actual Script
```python
import csv
from collections import defaultdict

def load_budget(path):
    budget = defaultdict(int)
    with open(path) as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            if len(row) >= 4:
                cat = row[0].strip()
                amt_str = row[2].replace('$','').replace(',','').replace('"','')
                try:
                    budget[cat] += int(amt_str)
                except: pass
    return budget

def load_expenses(path):
    actual = defaultdict(int)
    with open(path) as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            if len(row) >= 4:
                cat = row[1].strip()
                amt_str = row[3].replace('$','').replace(',','').strip('"')
                try:
                    actual[cat] += int(amt_str)
                except: pass
    return actual

# Compare
budget = load_budget('finance/budget/202604.csv')
actual = load_expenses('finance/expenses/202604-expenses.csv')

food_actual = actual['Food'] + actual['Eating Outside'] + actual['Supermarket']
food_bud = budget['Food']
# ... etc
```

## Budget Philosophy (O'car's approach)
- Budgets are intentionally inflated to create flexibility margins
- Actual spending consistently well under budget
- TGR-type surprises handled by squeezing inflated categories, not lifestyle cuts
- Real cushion = Fintual reserves, not operational budget surplus
- "Living paycheck to paycheck is fine" — priority is Fintual savings retention
- Pets, health, one-time hardware = unbudgeted surprise categories, handled via Buffer

## Tricount Billing (Francisca Household)
Francisca shares household bills 50/50 via Tricount. O'car pays 100% of the bill, logs 50% in budget. When Francisca spends and updates Tricount, O'car's balance leverages. Logging is always 50% of the total bill regardless of who paid.

## Money Classification Rules (Critical)

### Income File — ONLY salary/freelance
- Salary from employer
- Freelance/work-related income
- **DO NOT log**: Fintual transfers, investment returns, interest earned, transfers between own accounts

### Expenses File — money leaving O'car's control
- Rent (paid to Francisca who pays landlord)
- Savings (Fintual deposits — money allocated to savings is treated as spending)
- Loan payments (TGR, Banco Estado)
- Purchases and purchases made FROM Mach/MercadoPago
- **DO NOT log**: Loading money into Mach or MercadoPago (that's a transfer, not an expense)

### Account Loads — Transfer, NOT Expense
- Mach and MercadoPago are storage/spending accounts
- Loading them from Santander = internal transfer only
- Only log the expense when money is actually SPENT from them
- Log in `account-tracker.md` for reconciliation purposes

### Fintual — Treated as Savings/Expense
- Monthly Fintual deposit goes in expenses under "Savings" category
- It is money O'car allocated from salary — equivalent to spending for tracking purposes
- Does NOT go in income file (income = only money received for working)
- Fintual investment RETURNS/interest do NOT go in income file

### Monthly Post-Salary Flow
1. Salary arrives → log in `YYYY-income.csv`
2. Transfers to Fintual (Savings) → log in `expenses/YYYYMM-expenses.csv` + `budget/YYYYMM.csv`
3. Rent to Francisca → log in expenses (Housing)
4. Loan payments (TGR, Banco Estado) → log in expenses (Education)
5. Transfers to Mach/MercadoPago → log in `account-tracker.md` ONLY (not in expenses)
6. Bills paid where Francisca shares cost via Tricount → log 50% in expenses

## Fintual Portfolio Update
- O'car provides values manually (browser automation unreliable due to React 2FA)
- Calculate market gain = current_value - previous_value - new_deposits
- Deposits logged separately from market movement
- Casa merged into Compra April 2026 (geopolitical risk — conservative profile)
- Monthly strategy: Reserva rebuild to $15M (~$500k/month), Compra $1M/month until end 2027

## Files
- Budget: `finance/budget/YYYYMM.csv`
- Expenses: `finance/expenses/YYYYMM-expenses.csv`
- Income: `finance/YYYY-income.csv`
- Account balances: `finance/account-balances.csv`
