import LABORATORY_5_CLASS

# Initialization and Getting the Values of Student Information
section_width = 10
subject_width = 40
unit_width = 10

def display_student_information():

    print(f"\n\n\nStudent Name: {student.student_name:<30} Student Number: {student.student_number:<15}")
    print(f"Student Course: {student.student_course:<30} Academic Year: {student.academic_year:<15}")

# Displaying Assessment Fee
def display_assessment_fee():
    print("-" * (section_width + subject_width + unit_width + 15))
    print("Assessment Fee")
    print("-" * (section_width + subject_width + unit_width + 15))
    print(f"Tuition Fee Lecture: {assessment.tuition_fee():<{unit_width}}")
    print(f"LPU Chronicle: {assessment.chronicle:<{unit_width}}")
    print(f"Athletic: {assessment.athletic:<{unit_width}}")
    print(f"Audio Visual Library: {assessment.audio_visual_library:<{unit_width}}")
    print(f"LycesGo: {assessment.ausg:<{unit_width}}")
    print(f"Cultural Fee: {assessment.cultural_fee:<{unit_width}}")
    print(f"Energy Cost, Aircon Classroom: {assessment.energy_cost_aircon_classroom:<{unit_width}}")
    print(f"Guidance Fee: {assessment.guidance:<{unit_width}}")
    print(f"Insurance Fee: {assessment.insurance_fee:<{unit_width}}")
    print(f"Learning Management System: {assessment.learning_management_system:<{unit_width}}")
    print(f"Library Fee: {assessment.library:<{unit_width}}")
    print(f"Medical and Dental Fee: {assessment.medical_and_dental:<{unit_width}}")
    print(f"Registration Fee: {assessment.registration:<{unit_width}}")
    print(f"Recognized Student Government: {assessment.rso:<{unit_width}}")
    print(f"Student Activities: {assessment.student_activities_fee:<{unit_width}}")
    print(f"Student Nurturance: {assessment.student_nurturance_fee:<{unit_width}}")
    print(f"Technology Fee: {assessment.technology_fee:<{unit_width}}")
    print(f"Test Papers Fee: {assessment.test_papers:<{unit_width}}")
    print('-' * (section_width + subject_width + unit_width + 15))
    print(f"Total Assessment: {assessment.assessment_amount():<{unit_width}}")
    print(f"Downpayment: {assessment.downpayment:<{unit_width}}")
    print('-' * (section_width + subject_width + unit_width + 15))
    print(f"Total Due: {assessment.total_due():<{unit_width}}")
    print('-' * (section_width + subject_width + unit_width + 15))
    print("\n")

def display_schedule_of_payment():
    print('=' * (section_width + subject_width + unit_width + 15))
    print("Schedule of Payment of outstanding balance after downpayment prior for: ")
    print('=' * (section_width + subject_width + unit_width + 15))
    print("Prelim:", assessment.total_due() / 3)
    print("Midterm:", assessment.total_due() / 3)
    print("Final:", assessment.total_due() / 3)
    print('=' * (section_width + subject_width + unit_width + 15))
    print("*There will be a 60% surcharge for late payment.")
    print('=' * (section_width + subject_width + unit_width + 15))
    print("THIS IS A TEMPORARY ASSESSMENT")
    print('=' * (section_width + subject_width + unit_width + 15))

student = LABORATORY_5_CLASS.Student()
student.student_subject()
assessment = LABORATORY_5_CLASS.AssessmentFee(student)
display_student_information()
display_assessment_fee()
display_schedule_of_payment()