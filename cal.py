# 定义参数
# - Salary(perMonth)
# - Insurance(perMonth)
# - Extension
# - FixedTaxFree(perMonth)
# - AnnualBonus
GradesOfTaxRate = {36000: 0.03, 144000: 0.1, 300000: 0.2, 420000: 0.25, 660000: 0.3, 960000: 0.35, 960000.01: 0.45}
# 960000.01表示大于960000
TableOfQuickCalculationDeduction = \
    {36000: 0, 144000: 2520, 300000: 16920, 420000: 31920, 660000: 52920, 960000: 85920, 960000.01: 181920}


# 定义计算函数

# 专项扣除合计 Special deductions
def calPro(income):
    ans1 = 0
    for j in income.get_avgSalary():
        temp = income.get_insurancePer() * j
        ans1 = ans1 + round(temp,2)
    print(ans1)

    # 更新抹零办法
    ans2 = 0
    for j in income.get_avgSalary():
        insurances = income.get_insurances()
        temp = int(j * insurances[0]*100)/100 + round(j*insurances[1],2) + round(j*insurances[2],2) + int(j*insurances[3])
        ans2 = ans2 +temp
    print(ans2)
    return ans2

# Combine情况

def calCombine(income):
    taxableIncomeCombine = calTaxableIncomeCombine(income)
    accountPayableCombine = calAccountPayableCombine(taxableIncomeCombine)
    annualPostTaxIncomeCombine = calAnnualPostTaxIncomeCombine(income, accountPayableCombine)
    return {'taxableIncomeCombine': taxableIncomeCombine, 'accountPayableCombine': accountPayableCombine, 'annualPostTaxIncomeCombine': annualPostTaxIncomeCombine}


# (Salary(perMonth)-FixedTaxFree(perMonth)-Insurance(perMonth)-Extension)*12 + AnnualBonus = TaxableIncomeCombine

def calTaxableIncomeCombine(income):
    taxableIncomeCombine = 0
    insurances = income.get_insurances()
    for i,j in zip(income.get_salary(),income.get_avgSalary()):
        taxableIncomeCombine = taxableIncomeCombine + (i - income.get_fixedTaxFree() - (int(j * insurances[0]*100)/100 + round(j*insurances[1],2) + round(j*insurances[2],2) + int(j*insurances[3])) - income.get_extension())
    taxableIncomeCombine = taxableIncomeCombine + income.get_annualBonus()
    return taxableIncomeCombine


# TaxableIncome * GradesOfTaxRate - QuickCalculationDeduction = AccountPayableCombine

def calAccountPayableCombine(taxableIncomeCombine):
    myRate = 0
    myQuickCalculationDeduction = 0

    for grade in GradesOfTaxRate:
        if taxableIncomeCombine <= grade:
            myRate = GradesOfTaxRate[grade]
            break

    for grade in TableOfQuickCalculationDeduction:
        if taxableIncomeCombine <= grade:
            myQuickCalculationDeduction = TableOfQuickCalculationDeduction[grade]
            break  #必须立马break

    accountPayableCombine = taxableIncomeCombine * myRate - myQuickCalculationDeduction
    return accountPayableCombine


# (Salary(perMonth)-Insurance(perMonth))*12 + AnnualBonus - AccountPayableCombine = AnnualPostTaxIncomeCombine

def calAnnualPostTaxIncomeCombine(income, accountPayableCombine):
    annualPostTaxIncomeCombine = 0
    insurances = income.get_insurances()
    for i,j in zip(income.get_salary(),income.get_avgSalary()):
        annualPostTaxIncomeCombine = annualPostTaxIncomeCombine + i - (int(j * insurances[0]*100)/100 + round(j*insurances[1],2) + round(j*insurances[2],2) + int(j*insurances[3]))
    annualPostTaxIncomeCombine = annualPostTaxIncomeCombine + income.get_annualBonus() - accountPayableCombine
    return annualPostTaxIncomeCombine

# Split

def calSplit(income):
    annualPostTaxIncomeSalaryIsolate = calSalarySplit(income)
    annualPostTaxIncomeBonusIsolate = calAnnualBonusSplit(income)
    annualPostTaxIncomeIsolate = annualPostTaxIncomeSalaryIsolate + annualPostTaxIncomeBonusIsolate
    return {'annualPostTaxIncomeSalaryIsolate':annualPostTaxIncomeSalaryIsolate, 'annualPostTaxIncomeBonusIsolate':annualPostTaxIncomeBonusIsolate,'annualPostTaxIncomeIsolate':annualPostTaxIncomeIsolate }
#  - Salary
# - (Salary(perMonth)-FixedTaxFree(perMonth)-Insurance(perMonth)-Extension)*12 = TaxableIncomeSalaryIsolate
#     - TaxableIncomeSalaryIsolate * GradesOfTaxRate - QuickCalculationDeduction = AccountPayableSalaryIsolate
#     - (Salary(perMonth)-Insurance(perMonth))*12 - AccountPayableSalaryIsolate = AnnualPostTaxIncomeSalaryIsolate
def calSalarySplit(income):
    taxableIncomeSalaryIsolate = 0
    for i,j in zip(income.get_salary(),income.get_avgSalary()):
        taxableIncomeSalaryIsolate = taxableIncomeSalaryIsolate + (i-income.get_fixedTaxFree()-round(income.get_insurancePer() * j,2)-income.get_extension())
    myRate = 0
    myQuickCalculationDeduction = 0

    for grade in GradesOfTaxRate:
        if taxableIncomeSalaryIsolate <= grade:
            myRate = GradesOfTaxRate[grade]
            break

    for grade in TableOfQuickCalculationDeduction:
        if taxableIncomeSalaryIsolate <= grade:
            myQuickCalculationDeduction = TableOfQuickCalculationDeduction[grade]
            break  # 必须立马break

    accountPayableSalaryIsolate = taxableIncomeSalaryIsolate * myRate - myQuickCalculationDeduction

    annualPostTaxIncomeSalaryIsolate = 0
    for i,j in zip(income.get_salary(),income.get_avgSalary()):
        annualPostTaxIncomeSalaryIsolate = annualPostTaxIncomeSalaryIsolate + i-income.get_insurancePer() * j

    annualPostTaxIncomeSalaryIsolate = annualPostTaxIncomeSalaryIsolate - accountPayableSalaryIsolate

    return annualPostTaxIncomeSalaryIsolate

def calAnnualBonusSplit(income):
    myRate = 0
    myQuickCalculationDeduction = 0

    for grade in GradesOfTaxRate:
        if income.get_annualBonus() <= grade:
            myRate = GradesOfTaxRate[grade]
            break

    for grade in TableOfQuickCalculationDeduction:
        if income.get_annualBonus() <= grade:
            myQuickCalculationDeduction = TableOfQuickCalculationDeduction[grade]
            break  # 必须立马break
    annualPostTaxIncomeBonusIsolate = income.get_annualBonus()-(income.get_annualBonus()*myRate-myQuickCalculationDeduction)
    return annualPostTaxIncomeBonusIsolate

#
#   - AnnualBonus
#     - AnnualBonus * GradesOfTaxRate - QuickCalculationDeduction = AccountPayableBonusIsolate
#     - AnnualBonus - AccountPayableBonusIsolate = AnnualPostTaxIncomeBonusIsolate
#   - AnnualPostTaxIncomeIsolate
#     - AnnualPostTaxIncomeSalaryIsolate + AnnualPostTaxIncomeBonusIsolate = AnnualPostTaxIncomeSalaryIsolate