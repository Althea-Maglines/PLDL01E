# Class for Electric Bill
class CustomerBillInfo:

# Initialize Electric Bill info
    def __init__(self):
        self.name = input("Enter Customer Name: ")
        self.service_id_number = int(input("Enter Service ID Number: "))
        self.previous_billing = float(input("Enter Previous Billing: "))
        self.rate = input("Enter Rate (Residential/Commercial): ")
        self.rate_per_kwh = float(input("Enter Rate Per KWH: "))
        self.service_address = input("Enter Service Address: ")
        self.bill_date = input("Enter the Billing Date: ")
        self.meter_reading_date = input("Enter Meter Reading Rate: ")
        self.bill_period = input("Enter Billing Period: ")
        self.due_date = input("Enter Due Date: ")
        self.total_current_amount = 0
        self.next_meter_reading = input("Enter Next Meter Reading: ")
        self.total_kwh = 0
        self.actual_consumption = float(input("Enter Actual Consumption: "))
        self.charges_billing_period = 0
        self.previous_bill_output = ""

    def balance_previous_billing(self):
        if self.previous_billing == 0:
            return("thank you")
        else:
            return("please pay")

    def get_computation_charges(self):
        self.charges_billing_period = self.rate_per_kwh * self.actual_consumption

    def get_computation_total_amount(self):
        self.total_current_amount = self.previous_billing + self.charges_billing_period

# Class for Bill Statement
class BillingStatement:

    # Initialization for Bill Statement
    def __init__(self):
        self.generation = 0
        self.transmission = 0
        self.system_loss = 0
        self.distribution = 0
        self.subsides = 0
        self.government_taxes = 0
        self.universal_charges = 0
        self.fit_all = 0
        self.applied_credits = 0
        self.other_charges = 0
        self.installment_due = 0

    def get_bill_statement(self, generation, transmission, system_loss, distribution, subsides, government_taxes, universal_charges, fit_all,
                           applied_credits, other_charges, installment_due):
        self.generation = generation
        self.transmission = transmission
        self.system_loss = system_loss
        self.distribution = distribution
        self.subsides = subsides
        self.government_taxes = government_taxes
        self.universal_charges = universal_charges
        self.fit_all = fit_all
        self.applied_credits = applied_credits
        self.other_charges = other_charges
        self.installment_due = installment_due





