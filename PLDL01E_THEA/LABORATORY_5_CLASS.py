# Class for student info
class Student:

    # Initialization
    def __init__ (self):

        # Getting the values for the student info
        self.student_name = input("Enter Student Name: ")
        self.course = input("Enter the Student Course: ")
        self.student_number = input("Enter the Student Number: ")
        self.academic_year = input("Enter the Academic Year of Student: ")
        self.date_printed = input("Enter Date of Printed: ")
        self.subject_info = []

    # Getting the Student Subjects and Units
    def student_subject(self):
        for i in range(5):
            print(f"Subject {i + 1}")
            section = input("Student Section: ")
            subject = input("Student Subject: ")
            unit = int(input("Student Unit: "))
            self.subject_info.append((section,subject,unit))

    # Getting the sum of units
    def sum_units(self):
        return sum(unit for _, _, unit in self.subject_info)

# Class for Assessment fee
class AssessmentFee:

    # Getting the Value for Student Assessment Fees
    def __init__(self, student):
        self.student = student
        self.total_units = self.student.sum_units()
        self.tuition = 0
        self.chronicle = float(input("Enter ADU Chronicle Fee: "))
        self.athletic = float(input("Enter Athletic Fee: "))
        self.audio_visual_library = float(input("Enter Audio Visual Library Fee: "))
        self.ausg = float(input("Enter AUSG Fee: "))
        self.cultural_fee = float(input("Enter Cultural Fee: "))
        self.energy_cost_aircon_classroom = float(input("Enter Energy Cost, Aircon Classroom Fee: "))
        self.guidance = float(input("Enter Guidance Fee: "))
        self.insurance_fee = float(input("Enter Insurance Fee: "))
        self.learning_management_system = float(input("Enter Learning Management System Fee: "))
        self.library_fee = float(input("Enter Library Fee: "))
        self.medical_and_dental = float(input("Enter Medical and Dental Fee: "))
        self.registration = float(input("Enter Registration Fee: "))
        self.rso = float(input("Enter RSO Fee: "))
        self.student_activities_fee = float(input("Enter Student Activities Fee: "))
        self.student_nurturance_fee = float(input("Enter Student Nurturance Fee: "))
        self.technology_fee = float(input("Enter Technology Fee: "))
        self.test_papers = float(input("Enter Test Papers Fee: "))
        self.downpayment = float(input("Enter Downpayment Fee: "))

    # Formulating a formula for the tuition fee
    def tuition_fee(self):
        self.tuition = self.total_units * 1500.00
        return self.tuition

    # Formulating a formula for total assessment amount
    def assessment_amount(self):
        return (self.tuition_fee() + self.chronicle + self.athletic + self.audio_visual_library +
                self.ausg + self.ausg + self.cultural_fee + self.energy_cost_aircon_classroom + self.guidance
                + self.insurance_fee + self.learning_management_system + self.library_fee + self.medical_and_dental +
                self.registration + self.rso + self.student_activities_fee + self.student_nurturance_fee + self.technology_fee
                + self.test_papers)

    # Formulating a formula for total due
    def total_due(self):
        return self.assessment_amount() - self.downpayment




