import LABORATORY_5_CLASS

student = LABORATORY_5_CLASS.Student()
student.student_subject()
section_width = 10
subject_width = 40
unit_width = 9
assessment_width = 40

# Displaying Student Info
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

# Displaying Subject Assessment Fee
def subject_assessment_fee():
    section, subject, unit = student.subject_info[0]
    print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width - 2}} | ")
    section, subject, unit = student.subject_info[1]
    print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width - 2}} | ")
    section, subject, unit = student.subject_info[2]
    print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width - 2}} | ")
    section, subject, unit = student.subject_info[3]
    print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width - 2}} | ")
    section, subject, unit = student.subject_info[4]
    print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width - 2}} | ")
    print(f"{' ':<{section_width + subject_width - 17}}  {'TOTAL UNITS:':<{15}} {student.sum_units():<{unit_width}}| ")

student_information()
subject_assessment_fee()