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
- Actual spending consistently well under budget (April 2026: $474k under operationally)
- TGR-type surprises handled by squeezing inflated categories, not lifestyle cuts
- Real cushion = Fintual reserves, not operational budget surplus
- "Living paycheck to paycheck is fine" — priority is Fintual savings retention
- Pets, health, one-time hardware = unbudgeted surprise categories, handled via Buffer

## Files
- Budget: `finance/budget/YYYYMM.csv`
- Expenses: `finance/expenses/YYYYMM-expenses.csv`
- Income: `finance/YYYY-income.csv`
- Account balances: `finance/account-balances.csv`
