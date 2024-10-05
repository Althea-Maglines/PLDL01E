# this program is design to compute the payroll salary of an employee

class Employee:
    hmf = 100

    # initialization or constructor method of
    def __int__(self):
        # class Employee
        self.hmdf_contribution = 100.00
        self.company_name = input("Enter Company Name: ")
        self.employee_department = input("Enter Employee Department: ")
        self.employee_name = input("Enter Employee Name: ")
        self.employee.code = input("Enter Employee Code: ")
        self.slary_cut_off = input("Enter Cut-Off Date: ")

        # input for salary computation
        self.emp_rate_per_hour = float(input("Employee rate per hour:"))
        self.emp_num_of_hours_per_payday = int(input("Employee's numebr of hours worked per payday: "))
        self.emp_hour_overtime = foat(input("Employee overtime hours: "))
        self.honorarium_pay = float(input("Employee honoraium pay:" ))
        self.emp_num_of_absences = int(input("Employee absences:" ))
        self.emp_num_tardiness = int(input("Employee tardiness: "))

    def emp_sss_contibution(self):
        # Setting condition for Employee's Gross Earning to get the SSS. Tax, Philhealth Contribution
        if self.emp_gross_earning < 0:
            self.sss_contribution = 0.00
        elif self.emp_gross_earning >= 0 and self.emp_gross_earning < 4250.00:
            self.sss_contribution = 180.00
        elif self.emp_gross_earning >= 4251 and self.emp_gross_Earning <= 4749.99:
            self.sss_contribution = 202.50
        elif self.emp_gross_earning >= 4750 and self.emp_gross_earning <= 5249.99:
            self.sss_contribution = 225.00
        elif self.emp_gross_earning >= 5250 and self.emp_gross_earning <= 5759.99:
            self.sss_contribution = 247.50
        elif self.emp_gross_earning >= 5750 and self.emp_gross_earning <= 6249.99:
            self.sss_contribution = 270.00
        elif self.emp_gross_earning >= 6250 and self.emp_gross_earning <= 6749.99:
            self.sss_contribution = 292.50
        elif self.emp_gross_earning >= 6750 and self.emp_gross_Earning <= 7249.99:
            self.sss_contribution = 315.00
        elif self.emp_gross_earning >= 7250 and self.emp_gross_earning <

