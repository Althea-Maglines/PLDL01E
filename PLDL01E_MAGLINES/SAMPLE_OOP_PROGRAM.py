# this program is design to compute the payroll salary of an employee

class Employee:
    hmdf = 100

    # initialization or constructor method of
    def __int__(self):
        # class Employee
        self.hmdf_contribution = 100.00
        self.company_name = input("Enter Company Name: ")
        self.employee_department = input("Enter Employee Department: ")
        self.employee_name = input("Enter Employee Name: ")
        self.employee_code = input("Enter Employee Code: ")
        self.salary_cut_off = input("Enter Cut-Off Date: ")

        # input for salary computation
        self.emp_rate_per_hour = float(input("Employee rate per hour: "))
        self.emp_num_of_hours_per_payday = int(input("Employee's number of hours worked per payday: "))
        self.emp_hour_overtime = float(input("Employee overtime hours: "))
        self.honorarium_pay = float(input("Employee honorarium pay:"))
        self.emp_num_of_absences = int(input("Employee absences:"))
        self.emp_num_tardiness = int(input("Employee tardiness: "))

    def emp_salary_computation(self):
        self.basic_pay = self.emp_rate_per_hour * self.emp_num_of_hours_per_payday
        self.overtime_pay = self.emp_hour_overtime * self.emp_rate_per_hour
        self.emp_gross_earning = self.basic_pay + self.overtime_pay + self.honorarium_pay
        self.emp_absences = self.emp_num_of_absences * self.emp_rate_per_hour
        self.emp_tardiness = self.emp_num_tardiness * self.emp_rate_per_hour

    def emp_sss_contribution(self):
        # Setting condition for Employee's Gross Earning to get the SSS. Tax, Philhealth Contribution
        if self.emp_gross_earning < 0:
            self.sss_contribution = 0.00
        elif self.emp_gross_earning >= 0 and self.emp_gross_earning < 4250.00:
            self.sss_contribution = 180.00
        elif self.emp_gross_earning >= 4251 and self.emp_gross_earning <= 4749.99:
            self.sss_contribution = 202.50
        elif self.emp_gross_earning >= 4750 and self.emp_gross_earning < 5249.99:
            self.sss_contribution = 225.00
        elif self.emp_gross_earning >= 5250 and self.emp_gross_earning < 5759.99:
            self.sss_contribution = 247.50
        elif self.emp_gross_earning >= 5750 and self.emp_gross_earning < 6249.99:
            self.sss_contribution = 270.00
        elif self.emp_gross_earning >= 6250 and self.emp_gross_earning < 6749.99:
            self.sss_contribution = 292.50
        elif self.emp_gross_earning >= 6750 and self.emp_gross_earning < 7249.99:
            self.sss_contribution = 315.00
        elif self.emp_gross_earning >= 7250 and self.emp_gross_earning < 7749.99:
            self.sss_contribution = 337.50
        elif self.emp_gross_earning >= 7750 and self.emp_gross_earning < 8249.99:
            self.sss_contribution = 360.00
        elif self.emp_gross_earning >= 8250 and self.emp_gross_earning < 8749.99:
            self.sss_contribution = 382.50
        elif self.emp_gross_earning >= 8750 and self.emp_gross_earning < 9249.99:
            self.sss_contribution = 405.00
        elif self.emp_gross_earning >= 9250 and self.emp_gross_earning < 9749.99:
            self.sss_contribution = 427.50
        elif self.emp_gross_earning >= 9750 and self.emp_gross_earning < 10249.99:
            self.sss_contribution = 450.00
        elif self.emp_gross_earning >= 10250 and self.emp_gross_earning < 10749.99:
            self.sss_contribution = 472.50
        elif self.emp_gross_earning >= 10750 and self.emp_gross_earning < 11249.99:
            self.sss_contribution = 495.00
        elif self.emp_gross_earning >= 11250 and self.emp_gross_earning < 11749.99:
            self.sss_contribution = 517.50
        elif self.emp_gross_earning >= 11750 and self.emp_gross_earning < 12249.99:
            self.sss_contribution = 540.00
        elif self.emp_gross_earning >= 12250 and self.emp_gross_earning < 12749.99:
            self.sss_contribution = 562.50
        elif self.emp_gross_earning >= 12750 and self.emp_gross_earning < 13249.99:
            self.sss_contribution = 585.00
        elif self.emp_gross_earning >= 13250 and self.emp_gross_earning < 13749.99:
            self.sss_contribution = 607.50
        elif self.emp_gross_earning >= 13750 and self.emp_gross_earning < 14249.99:
            self.sss_contribution = 630.00
        elif self.emp_gross_earning >= 14250 and self.emp_gross_earning < 14749.99:
            self.sss_contribution = 652.50
        elif self.emp_gross_earning >= 14750 and self.emp_gross_earning < 15249.99:
            self.sss_contribution = 675.00
        elif self.emp_gross_earning >= 15250 and self.emp_gross_earning < 15749.99:
            self.sss_contribution = 697.50
        elif self.emp_gross_earning >= 15750 and self.emp_gross_earning < 16249.99:
            self.sss_contribution = 720.00
        elif self.emp_gross_earning >= 16250 and self.emp_gross_earning < 16749.99:
            self.sss_contribution = 742.50
        elif self.emp_gross_earning >= 16750 and self.emp_gross_earning < 17249.99:
            self.sss_contribution = 765.00
        elif self.emp_gross_earning >= 17250 and self.emp_gross_earning < 17749.99:
            self.sss_contribution = 787.50
        elif self.emp_gross_earning >= 17750 and self.emp_gross_earning < 18249.99:
            self.sss_contribution = 810.00
        elif self.emp_gross_earning >= 18250 and self.emp_gross_earning < 18749.99:
            self.sss_contribution = 832.50
        elif self.emp_gross_earning >= 18750 and self.emp_gross_earning < 19249.99:
            self.sss_contribution = 855.00
        elif self.emp_gross_earning >= 19250 and self.emp_gross_earning < 19749.99:
            self.sss_contribution = 877.50
        elif self.emp_gross_earning >= 19750 and self.emp_gross_earning < 20249.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_earning >= 20250 and self.emp_gross_earning < 20749.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_earning >= 20750 and self.emp_gross_earning < 21249.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_earning >= 22250 and self.emp_gross_earning < 21749.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_earning >= 22750 and self.emp_gross_earning < 22249.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_earning >= 23250 and self.emp_gross_earning < 22749.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_earning >= 23750 and self.emp_gross_earning < 23249.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_Earning >= 24250 and self.emp_gross_earning < 23749.99:
            self.sss_contribution = 900.00

    def emp_philhealth_contribution(self):
        # Setting conditions in getting PhilHealth Contribution
        if self.emp_gross_earning < 10000:
            self.philhealth_contribution = 0.00
        else:
            self.philhealth_contribution = self.emp_gross_earnings * 0.0450

        # Setting conditions in getting Tax Contribution
    def emp_tax_contribution(self):
        if self.emp_gross_earning < 10417:
            self.tax_contribution = 0.00
        elif self.emp_gross_earning >= 10417 and self.emp_gross_earning <= 16666:
            self.tax_contribution = ((self.emp_gross_earnings - 10417) * 0.15 + 0.00)
        elif self.emp_gross_earning >= 16667 and self.emp_gross_earning <= 33332:
            self.tax_contribution = ((self.emp_gross_earning - 16667) * 0.20 + 937.50)
        elif self.emp_gross_earning >= 33333 and self.emp_gross_earning <= 16666:
            self.tax_contribution = ((self.emp_gross_earnings - 33333) * 0.25 + 4270.70)
        elif self.emp_gross_earning >= 83333 and self.emp_gross_earning <= 33332:
            self.tax_contribution = ((self.emp_gross_earning - 83333) * 0.30 + 16770.70)
        else:
            self.tax_contribution = ((self.emp_gross_earning - 333333) * 0.35 + 91770.70)

    def emp_total_deduction(self):
        self.dedution = self.emp_absences + self.emp_tardiness + self.tax_contribution + self.sss_contribution + self.philhealth_contribution + self.hmdf_contribution

    def emp_employee_netpay(self):
        self.net_pay = self.emp_gross_earning - self.dedution
    # displayStudent method of class Employee
    def emp_displayEmployee(self):
        print("Company Name: ", self.company_name)
        print("Employee Department: ", self.employee_department)
        print("Employee Name: ", self.employee_name)
        print("Employee Code: ", self.employee_code)
        print("Cut-Off Date: ", self.salary_cut_off)
        print("Basic Pay: %.2f" % self.basic_pay)
        print("Overtime Pay: %.2f" % self.overtime_pay)
        print("Gross Income: %.2f" % self.emp_gross_earning)
        print("Absences: %.2f" % self.emp_absences)
        print("Tardiness: %.2f" % self.emp_tardiness)
        print("SSS Contribution: %.2f" % self.sss_contribution)
        print("Philhealth Contribution: %.2f" % self.philhealth_contribution)
        print("Total Dedcution: %.2f" % self.dedution)
        print("Net Income: %.2f" % self.net_pay)

emp1 = Employee()
emp1.emp_salary_computation()
emp1.emp_sss_contribution()
emp1.emp_philhealth_contribution()
emp1.emp_tax_contribution()
emp1.emp_total_deduction()
emp1.emp_employee_netpay()
emp1.emp_displayEmployee()




