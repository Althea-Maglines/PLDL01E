import payroll_oop2

obj = payroll_oop2.Employee_Info()
company = input("Enter company name: ")
department = input("Enter employee department: ")
employee_name = input("Enter employee name: ")
employee_code = input("Enter employee number or code: ")
salary_cutoff = input("Enter salary cut off: ")
emp_data = obj.get_emp_data(company, department, employee_name, employee_code, salary_cutoff)

#data entry for basic pay computation
obj2 = payroll_oop2.Employee_Salary()
rate_pay = float(input("Enter employee rate per hour: "))
number_working_hours = float(input("Enter honorarium pay: "))
honorarium_pay = float(input("Enter honorarium pay: "))
number_absences = float(input("Enter number of absences in hours: "))

#computation for basic pay
basic_pay = obj2.get_basic_pay(rate_pay, number_working_hours)
absences_deduction = obj2.get_absences_deduction(rate_pay, number_absences)

#diplay of output
print("____________________________________________________")
print("____________________________________________________")
obj = payroll_oop2.Employee_Info()
print("Company Name: ", company)
print("Employee Department: ", department)
print("Employee Name: ", employee_name)
print("Employee Code: ", employee_code)
print("Salary Cut off: ", salary_cutoff)
obj2 = payroll_oop2.Employee_Salary()
print("Basic Pay: %.2f" % basic_pay)
print("Honorarium pay: %.2f" % honorarium_pay)
print("Employee absences deduction: %.2f" % absences_deduction)
print("____________________________________________________")
print("____________________________________________________")


