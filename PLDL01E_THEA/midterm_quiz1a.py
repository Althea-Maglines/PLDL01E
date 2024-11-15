import midterm_quiz1

obj = midterm_quiz1.CustomerBillInfo()


def summary_info():
    print("\n\n---------------------------------------------------------------------------------------------------------------")
    print("                                                            Electric Bill                                  ")
    print("---------------------------------------------------------------------------------------------------------------")
    print("|                                       |                ")
    print("|     Balance From Previous Billing     |                       ")
    print("|                                       |                ")
    print("---------------------------------------------------------------------------------------------------------------")
    print(f"                        {obj.previous_billing}        {obj.balance_previous_billing()}")

def service_info():
    print("------------------------------------------------------------------------")
    print("Service Info")
    print("------------------------------------------------------------------------")
    print("Service ID Number: ", obj.service_id_number)
    print("Rate: ", obj.rate)
    print("Contact in the name of: ", obj.name)
    print("Service Address: ", obj.service_address)


def billing_info():
    print("------------------------------------------------------------------------")
    print("Billing Info")
    print("------------------------------------------------------------------------")
    print("Bill Date: ", obj.bill_date)
    print("Meter Reading Rate: ", obj.meter_reading_date)
    print("Bill Period: ", obj.bill_period)
    print("Due Date: ", obj.due_date)
    print("Total KWH: ", obj.total_kwh)
    print("Total current amount: ", obj.total_current_amount)
    print("Next Meter Reading: ", obj.next_meter_reading)




summary_info()
service_info()
billing_info()


