# input statements
salary = float(input("Please Input Salary:"))
numDependents = float(input("Please Input Number of Dependents:"))
stateTaxRate =.065
federalTaxRate =.28
dependentDeductionRate = .025
# calculate taxes here
stateTax = salary * stateTaxRate
federalTax = salary * federalTaxRate
dependentDeduction =  salary * (dependentDeductionRate * numDependents)
totalWitholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWitholding
# output statements
print ("State Tax:" + str(stateTax))
print ("Federal Tax" + str(federalTax))
print ("Dependents:" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))