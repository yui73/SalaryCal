# SalaryPLP

## Bound

## Parameter
- Salary(perMonth)
- Insurance(perMonth)
- Extension
- FixedTaxFree(perMonth)
- AnnualBonus
- GradesOfTaxRate - map
- TableOfQuickCalculationDeduction - map

## Problem

- Combine
  - (Salary(perMonth)-FixedTaxFree(perMonth)-Insurance(perMonth)-Extension)*12 + AnnualBonus = TaxableIncomeCombine
  - TaxableIncome * GradesOfTaxRate - QuickCalculationDeduction = AccountPayableCombine
  - (Salary(perMonth)-Insurance(perMonth))*12 + AnnualBonus - AccountPayableCombine = AnnualPostTaxIncomeCombine

- Isolate
  - Salary
    - (Salary(perMonth)-FixedTaxFree(perMonth)-Insurance(perMonth)-Extension)*12 = TaxableIncomeSalaryIsolate
    - TaxableIncomeSalaryIsolate * GradesOfTaxRate - QuickCalculationDeduction = AccountPayableSalaryIsolate
    - (Salary(perMonth)-Insurance(perMonth))*12 - AccountPayableSalaryIsolate = AnnualPostTaxIncomeSalaryIsolate
  - AnnualBonus
    - AnnualBonus * GradesOfTaxRate - QuickCalculationDeduction = AccountPayableBonusIsolate
    - AnnualBonus - AccountPayableBonusIsolate = AnnualPostTaxIncomeBonusIsolate
  - AnnualPostTaxIncomeIsolate
    - AnnualPostTaxIncomeSalaryIsolate + AnnualPostTaxIncomeBonusIsolate = AnnualPostTaxIncomeSalaryIsolate
