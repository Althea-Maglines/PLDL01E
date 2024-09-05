#initilization of the value of employee's name, department, gross income, pag-ibig contribution, and total deduction
from pydoc import pager
from ssl import SSLSocket

employee_name = ""
department = ""
gross_income = 0
pag_ibig_contrib = 100.00
total_deduct = 0
net_income = 0

#input employee's name, department, gross income, and the value of rate per hour, no. of working hours per day, no. of days per week, and no. of weeks per month
employee_name = str(input("Enter the Employee's Name:"))
department = str(input("Enter the Department:"))
rate_per_hr = float(input("Enter Employee's rate per hour:"))
hr_per_day = float(input("Enter Employee's number of working hours per day:"))
days_per_week = int(input("Enter Employee's number of days per week:"))
weeks_per_month = int(input("Enter Employee's number of weeks per month:"))
philhealth_contrib = float(input("Enter the value of PhilHealth Contribution:"))
sss_contrib = float(input("Enter the value of SSS Contribution:"))

#calculations of gross income
gross_income = hr_per_day * days_per_week * weeks_per_month * rate_per_hr

#calculation of employee's total deduction
total_deduct = sss_contrib + pag_ibig_contrib + philhealth_contrib

#calculation of net income
net_income = gross_income - total_deduct

#computed gross income using the SSS contribution and PhilHealth contribution
    #if the gross income is between 0-20,000 the SSS contribution is 125.75 and PhilHealth Contribution is 100.00
if 0 <= gross_income <= 20000:
    sss_contrib = 125.75
    philhealth_contrib = 100.00

    #if the gross income is between 20,001-50,000 the SSS contribution is 2,200.50 and PhilHealth Contribution is 1,200.00
elif 20001 <= gross_income <= 50000:
    sss_contrib = 2200.50
    philhealth_contrib = 1200.00

    #if the gross income is between 50,001-75,000 the SSS contribution is 4,800.00 and PhilHealth Contribution is 6,800.00
elif 50001 <= gross_income <= 75000:
    sss_contrib = 4800.00
    philhealth_contrib = 6800.00

    # if the gross income falls at 75,0001 up the SSS contribution is 5,800.00 and PhilHealth Contribution is 8,800.00
else:
    sss_contrib = 5800.00
    philhealth_contrib = 8800.00

#display employee's name, department, computed total deduction, computed gross income, and computed net income of an employee
print("Employee's Name:", employee_name)
print("Department:",department)
print("Total Deduction:",total_deduct)
print("Gross Income:",gross_income)
print("Net Income:",net_income)













