#Initializing
hdmf_contrib = 100

#input the company name and employee name
company_name = str(input("Enter the Company Name:"))
department = str(input("Enter the Department:"))
employee_name = str(input("Enter the Employee's Name:"))
employee_code =str(input("Enter the Employee's Code:"))
salary_date_cut_off = str(input("Cut off:"))

#input the number of rate per hour, hours per day
rate_per_hr = float(input("Enter the Employee's rate per hour:"))
hrs_per_payday = float(input("Enter the Employee's number of hours per payday:"))
num_absences_hrs = float(input("Enter the Employee's number of absences in hours:"))
num_hrs_tardiness = float(input("Enter the Employee's number of hours in tardiness:"))
overtime = float(input("Enter Employee's number of hours overtime:"))
pay_period = float(input("Enter Employee's pay period:"))


#Calculation
honorarium = hrs_per_payday * rate_per_hr
basic_pay = rate_per_hr + hrs_per_payday
gross_earning = basic_pay + overtime + honorarium
overtime_pay = hrs_per_payday * rate_per_hr
absences = num_absences_hrs * rate_per_hr
tardiness = rate_per_hr * num_hrs_tardiness

#statement for SSS
if 0 <= gross_earning < 4250:
    sss_contrib = 180
elif 4250 <= gross_earning <= 4749.99:
    sss_contrib = 202.50
elif 4750 <= gross_earning <= 5249.99:
    sss_contrib = 225
elif 5250 <= gross_earning <= 5749.99:
    sss_contrib = 247.50
elif 5750 <= gross_earning <= 6249.99:
    sss_contrib = 270
elif 6250 <= gross_earning <= 6749.99:
    sss_contrib = 292.50
elif 6750 <= gross_earning <= 7249.99:
    sss_contrib = 315.00
elif 7250 <= gross_earning <= 7749.99:
    sss_contrib = 337.50
elif 7750 <= gross_earning <= 8249.99:
    sss_contrib = 360
elif 8250 <= gross_earning <= 8749.99:
    sss_contrib = 382.50
elif 8750 <= gross_earning <= 9249.99:
    sss_contrib = 405
elif 9250 <= gross_earning <= 9749.99:
    sss_contrib = 427.50
elif 9750 <= gross_earning <= 10249.99:
    sss_contrib = 450
elif 10250 <= gross_earning <= 10749.99:
    sss_contrib = 472.50
elif 10750 <= gross_earning <= 11249.99:
    sss_contrib = 495
elif 11250 <= gross_earning <= 11749.99:
    sss_contrib = 517.50
elif 11750 <= gross_earning <= 12249.99:
    sss_contrib = 540
elif 12250 <= gross_earning <= 12749.99:
    sss_contrib = 562.50
elif 12750 <= gross_earning <= 13249.99:
    sss_contrib = 585
elif 13250 <= gross_earning <= 13749.99:
    sss_contrib = 607.50
elif 13750 <= gross_earning <= 14249.99:
    sss_contrib = 630
elif 14250 <= gross_earning <= 14749.99:
    sss_contrib = 652.50
elif 14750 <= gross_earning <= 15249.99:
    sss_contrib = 675
elif 15250 <= gross_earning <= 15749.99:
    sss_contrib = 697.50
elif 15750 <= gross_earning <= 16249.99:
    sss_contrib = 720
elif 16250 <= gross_earning <= 16749.99:
    sss_contrib = 742.50
elif 16750 <= gross_earning <= 17249.99:
    sss_contrib = 765
elif 17250 <= gross_earning <= 18249.99:
    sss_contrib = 787.50
elif 17750 <= gross_earning <= 18749.99:
    sss_contrib = 810
elif 18250 <= gross_earning <= 19749.99:
    sss_contrib = 832.50
elif 18750 <= gross_earning <= 19249.99:
    sss_contrib = 855
elif 19250 <= gross_earning <= 19749.99:
    sss_contrib = 877.50
else:
    sss_contrib = 900

#statement for witholding tax
if 0 <= gross_earning <= 20832.99:
    witholding_tax = 0.00
elif 20833 <= gross_earning <= 33332:
    witholding_tax = 0.15 / 20833
elif 33333 <= gross_earning <= 66666:
    witholding_tax = 1875 + 0.2 / 33333
elif 66667 <= gross_earning <= 166666:
    witholding_tax = 8541.80 + 0.25 / 66667
elif 166666 <= gross_earning <= 666666:
    witholding_tax = 33541.80 + 0.3 / 166667
else:
    witholding_tax = 183541.80 + 0.35 / 666667

#calculation for PhilHealth
philhealth_contrib = 0.05 * gross_earning

#calculation for deduction and net pay
deduction = absences + tardiness + witholding_tax + sss_contrib + philhealth_contrib + hdmf_contrib
net_pay = gross_earning - deduction

#displaying
print("================================================================")
print("Company Name: ", company_name)
print("Employee Code: ", employee_code)
print("Employee Name:", employee_name)
print("Department: ", department)
print("Cut off: ", salary_date_cut_off)
print("Pay Period: ", pay_period)
print("Basic Pay: ", basic_pay)
print("Overtime: ", overtime_pay)
print("Absences: ", absences)
print("Honorarium: ", honorarium)
print("Tardy: ", tardiness)
print("Withholding Tax: ",witholding_tax)
print("SSS Contribution: ", sss_contrib)
print("HDMF Contribution: ", hdmf_contrib)
print("PhilHealth Contribution: ", philhealth_contrib)
print("Deductions: ", deduction)
print("Gross Earning: ", gross_earning)
print("Net Pay: ", net_pay)
print("================================================================")
