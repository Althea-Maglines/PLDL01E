import LABORATORY_5_CLASS

# Initialization and getting the values of student information

student = LABORATORY_5_CLASS.Student()
student.student_subject()
assessment = LABORATORY_5_CLASS.AssessmentFee(student)
section_width = 10
subject_width = 40
unit_width = 10

# Displaying Student Information
def display_student_information():
    print(f"\n\nNAME: {student.student_name:<30}   STUDENT NO: {student.student_number:<15}")
    print(f"COURSE: {student.course:<30} ACADEMIC YEAR: {student.academic_year:<15}")
    print("-" * (section_width + subject_width + unit_width + 15))
    print(f"{'SECTION':<{section_width}}{'SUBJECT':<{subject_width}} {'UNIT':<{unit_width}}")
    print("-" * (section_width + subject_width + unit_width + 15))

    for section, subject, unit in student.subject_info:
        print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width}}")
    print("-" * (section_width + subject_width + unit_width + 15))
    print(f"{' ':<{section_width + subject_width}} Total Units: {student.sum_units():<{unit_width}}")
    print("-" * (section_width + subject_width + unit_width + 15))

# Displaying Assessment Fee
def display_assessment_fee():
    print("\n")
    print("-" * (section_width + subject_width + unit_width + 15))
    print("ASSESSMENT OF FEES")
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
    print(f"Library Fee: {assessment.library_fee:<{unit_width}}")
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

# Displaying schedule of Payment
def display_schedule_of_payment():
    print('=' * (section_width + subject_width + unit_width + 15))
    print("Schedule of Payment of outstanding balance after downpayment prior for: ".center(section_width + subject_width + unit_width + 15))
    print('=' * (section_width + subject_width + unit_width + 15))
    print(f"Prelim: {assessment.total_due() / 3}".center(section_width + subject_width + unit_width + 15))
    print(f"Midterm: {assessment.total_due() / 3}".center(section_width + subject_width + unit_width + 15))
    print(f"Final: {assessment.total_due() / 3}".center(section_width + subject_width + unit_width + 15))
    print('=' * (section_width + subject_width + unit_width + 15))
    print("*There will be a 60% surcharge for late payment.".center( section_width + subject_width + unit_width + 15))
    print('=' * (section_width + subject_width + unit_width + 15))
    print("THIS IS A TEMPORARY ASSESSMENT".center(section_width + subject_width + unit_width + 15))
    print('=' * (section_width + subject_width + unit_width + 15))
    print(f"Date Printed: {student.date_printed}".center(section_width + subject_width + unit_width + 15))
    print("NON-SCHOLAR STUDENT".center(section_width + subject_width + unit_width + 15))
    print('-' * (section_width + subject_width + unit_width + 15))

display_student_information()
display_assessment_fee()
display_schedule_of_payment()


