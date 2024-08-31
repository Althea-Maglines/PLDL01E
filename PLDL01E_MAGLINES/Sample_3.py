#initialization value of the net income, gross income, total deduction, name of employee, and pag-ibig deduction

net_income = 0
gross_income = 0
total_deduction = 0
employee_name = ""
pag_ibig_contri = 100.00

#input the rate per hour, number of hours per day, number of days per week, number of weeks per month, SSS contribution, PhilHealth contribution, tax contribution
employee_name = str(input("Enter Employee name:"))
rate_per_hr = float(input("Enter employee's rate per hour:"))
num_hrs_per_day = float(input("Enter employee's number of hours per day:"))
num_days_per_week = float(input("Enter employee's number of days per week:"))
num_weeks_per_mnth = float(input("Enter employee's number of weeks per month:"))
SSS_contri = float(input("Enter SSS contribution:"))
PhilHealth_contri = float(input("Enter PhilHealth contribution:"))
Tax_contri = float(input("Enter Tax contribution:"))

#computation
gross_income = rate_per_hr * num_hrs_per_day * num_days_per_week * num_weeks_per_mnth
total_deduction = SSS_contri + PhilHealth_contri + Tax_contri + pag_ibig_contri
net_income = gross_income - total_deduction

#displaying
print("Employee Name:",employee_name)
print("Net Income:",net_income)
print("Gross Income:",gross_income)
print("Total Deduction:",total_deduction)




