import LABORATORY_5_CLASS

student = LABORATORY_5_CLASS.Student()
student.student_subject()
section_width = 10
subject_width = 40
unit_width = 10

def display_student_information():
    print("-" * (section_width + subject_width + unit_width + 15))
    print("                                                    Office of the Registrar")
    print("\n")
    print("CERTIFICATE OF ENROLLMENT".center(section_width + subject_width + unit_width + 15))
    print("2nd Semester, 2022 - 2023".center(section_width + subject_width + unit_width + 15))
    print(f"\nNAME: {student.student_name:<30}                     STUDENT NO: {student.student_number:<15}")
    print(f"COURSE: {student.course:<30}                   ACADEMIC YEAR: {student.academic_year:<15}")
    print("-" * (section_width + subject_width + unit_width + 15))
    print(f"{'SECTION':<{section_width}}{'SUBJECT':<{subject_width}} {'UNIT':<{unit_width}}")
    print("-" * (section_width + subject_width + unit_width + 15))

    for section, subject, unit in student.subject_info:
        print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width}}")
    print("-" * (section_width + subject_width + unit_width + 15))
    print(f"{' ':<{section_width + subject_width}} Total Units: {student.sum_units():<{unit_width}}")
    print("-" * (section_width + subject_width + unit_width + 15))

display_student_information()