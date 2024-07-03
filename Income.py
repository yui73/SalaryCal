# 定义Class
# - Salary(perMonth)
# - Insurance(perMonth)
# - Extension
# - FixedTaxFree(perMonth)
# - AnnualBonus
class Income:
    """A simple example class."""

    def __init__(self, salary,avgSalary, insurances, extension, fixedTaxFree, annualBonus):
        """Constructor of the class."""
        self.salary = salary # 数组
        self.avgSalary = avgSalary # 平均工资数组
        self.insurances = insurances # 百分比数组
        self.extension = extension
        self.fixedTaxFree = fixedTaxFree
        self.annualBonus = annualBonus
        self.insurancePer = sum(insurances)

    def get_salary(self):
        """Get the value of the instance."""
        return self.salary

    def set_salary(self, salary):
        """Set the value of the instance."""
        self.salary = salary

    def get_avgSalary(self):
        """Get the value of the instance."""
        return self.avgSalary

    def set_avgSalary(self, avgSalary):
        """Set the value of the instance."""
        self.avgSalary = avgSalary

    def get_insurances(self):
        """Get the value of the instance."""
        return self.insurances

    def set_insurances(self, insurances):
        """Set the value of the instance."""
        self.insurances = insurances

    def get_extension(self):
        """Get the value of the instance."""
        return self.extension

    def set_extension(self, extension):
        """Set the value of the instance."""
        self.extension = extension

    def get_fixedTaxFree(self):
        """Get the value of the instance."""
        return self.fixedTaxFree

    def set_fixedTaxFree(self, fixedTaxFree):
        """Set the value of the instance."""
        self.fixedTaxFree = fixedTaxFree

    def get_annualBonus(self):
        """Get the value of the instance."""
        return self.annualBonus

    def set_annualBonus(self, annualBonus):
        """Set the value of the instance."""
        self.annualBonus = annualBonus

    def get_insurancePer(self):
        """Get the value of the instance."""
        return self.insurancePer

    def set_insurancePer(self, insurancePer):
        """Set the value of the instance."""
        self.insurancePer = insurancePer
