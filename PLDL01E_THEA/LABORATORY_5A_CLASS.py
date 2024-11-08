import LABORATORY_5_CLASS

# Initialization and getting the values of student information

student = LABORATORY_5_CLASS.Student()
student.student_subject()
assessment = LABORATORY_5_CLASS.AssessmentFee(student)
section_width = 10
subject_width = 40
unit_width = 9
assessment_width = 40

# Displaying Student Information
def student_information():
    print(" ")
    print("-" * (section_width + subject_width + unit_width + assessment_width + 13))
    print("                                                                                    Office of the Registrar")
    print("\n")
    print("CERTIFICATE OF ENROLLMENT".center(section_width + subject_width + unit_width + assessment_width + 15))
    print("2nd Semester, 2022 - 2023".center(section_width + subject_width + unit_width +assessment_width + 15))
    print(" ")
    print(" ")
    print(f"{"NAME :":<15} {student.student_name:<44} {"STUDENT NO: ":<10} {student.student_number:<10}")
    print(f"{"COURSE:":15} {student.course:<44} {"ACADEMIC YEAR:":<10} {student.academic_year:<10}")
    print("-" * (section_width + subject_width + unit_width), "|", "-" * (assessment_width + unit_width))
    print(f"{'SECTION':<{section_width}}{'SUBJECT':^{subject_width}} {'UNITS':<{unit_width - 1}} | {'ASSESSMENT OF FEES':^{assessment_width + unit_width}}")
    print(f"{'-' * (section_width + subject_width + unit_width)} | {'-' * (assessment_width + unit_width)}")

# Displaying Assessment Fee
def subject_assessment_fee():
    section, subject, unit = student.subject_info[0]
    print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width - 2}} | {'Tuition Fee Lecture:':<{assessment_width}} {assessment.tuition_fee():>{unit_width - 5}}")
    section, subject, unit = student.subject_info[1]
    print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width - 2}} | {'LPU Chronicle:':<{assessment_width}} {assessment.chronicle:>{unit_width - 5}}")
    section, subject, unit = student.subject_info[2]
    print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width - 2}} | {'Athletic:':<{assessment_width}} {assessment.athletic:>{unit_width - 5}}")
    section, subject, unit = student.subject_info[3]
    print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width - 2}} | {'Audio Visual Library:':<{assessment_width}} {assessment.audio_visual_library:>{unit_width - 5}}")
    section, subject, unit = student.subject_info[4]
    print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width - 2}} | {'LycesGo:':<{assessment_width}} {assessment.ausg:>{unit_width - 5}}")
    print(f"{' ':<{section_width + subject_width - 17}} {'TOTAL UNITS:':<{15}} {assessment.total_units:<{unit_width}} | {'Cultural Fee:':<{assessment_width + 1}} {assessment.cultural_fee:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Energy Cost, AC Classroom:':<{assessment_width + 1}} {assessment.energy_cost_aircon_classroom:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Guidance Fee:':<{assessment_width + 1}} {assessment.guidance:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Insurance Fee:':<{assessment_width + 1}} {assessment.insurance_fee:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Learning Management System:':<{assessment_width + 1}} {assessment.learning_management_system:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Library Fee:':<{assessment_width + 1}} {assessment.library_fee:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Medical and Dental Fee:':<{assessment_width + 1}} {assessment.medical_and_dental:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Registration Fee:':<{assessment_width + 1}} {assessment.registration:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Recognized Student Government:':<{assessment_width + 1}} {assessment.rso:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Student Activities:':<{assessment_width + 1}} {assessment.student_activities_fee:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Student Nurturance:':<{assessment_width + 1}} {assessment.student_nurturance_fee:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Technology Fee:':<{assessment_width + 1}} {assessment.technology_fee:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Test Papers Fee:':<{assessment_width + 1}} {assessment.test_papers:<{unit_width}}")
    print(f"{' ' * (section_width + subject_width + unit_width)} | {'-' * (assessment_width + unit_width)}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Total Assessment:':<{assessment_width}} {assessment.assessment_amount():<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Downpayment:':<{assessment_width}} {assessment.downpayment:<{unit_width}}")
    print(f"{' ' * (section_width + subject_width + unit_width)} | {'-' * (assessment_width + unit_width)}")
    print(f"{' ' * (section_width + subject_width + unit_width)} | ")
    print(f"{' ' * (section_width + subject_width + unit_width)} | ")
    print(f"{' ' * (section_width + subject_width + unit_width)} | ")
    print(f"{' ' * (section_width + subject_width + unit_width)} | ")
    print(f"{' ' * (section_width + subject_width + unit_width)} | ")
    print("\n")

# Displaying schedule of Payment
def schedule_of_payment():
    due = round(assessment.total_due() / 3, 2)
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{'-' * 47}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{'Schedule of Payment':^{47}}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{'of outstanding balance':^{47}}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{'after downpayment prior to: ':^{47}}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{' ' * 5}{'Prelim:':<{27}} {due:<{14}}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{' ' * 5}{'Midterm:':<{27}} {due:<{14}}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{' ' * 5}{'Finals:':<{27}} {due:<{14}}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{'-' * 47}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} |  {'*There will be a 6% surcharge p.a.':^{47}} ")
    print(f"{'Registrar':^{section_width + subject_width + unit_width}} |  {'for late payment':^{47}} ")

def date_printed():
     print(f"{'-' * (section_width + subject_width + unit_width)} | {'-' * (assessment_width + unit_width)}")
     print(f"{'Date Printed:':>{30}} {student.date_printed:<{28}} | {'THIS IS TEMPORARY ASSESSMENT':^{50}}")
     print(f"{'-' * (section_width + subject_width + unit_width)} | {'-' * (assessment_width + unit_width)}")
     print(f"{'THIS IS A NON-SCHOLAR STUDENT':^{59}}")

student_information()
subject_assessment_fee()
schedule_of_payment()
date_printed()

