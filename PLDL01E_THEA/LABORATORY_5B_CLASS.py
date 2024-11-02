import LABORATORY_5_CLASS
from PLDL01E_THEA.LABORATORY_5A_CLASS import section_width, subject_width, unit_width

student = LABORATORY_5_CLASS.tudent()
student.student_subject()
section_width = 10
subject_width = 40
unit_width = 10

def display_student_information():
    print(f"\n\n\nStudent Name: {student.student_name:<30}")
    print(f"Student Course: {student.course:<30} Academic Year: {student.academic_year:<15}")
    print("-" * (section_width + subject_width + unit_width + 15))
    print(F"{'Section':<{section_width}}{'Subject':<{subject_width}} {'Unit':<{unit_width}}")
    print("-" * (section_width + subject_width + unit_width + 15))

    for section, subject, unit in student.subject_info:
        print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width}}")
    print("-" * (section_width + subject_width + unit_width + 15))
    print(f"{' ':<{section_width + subject_width}} Total Units: {student.sum_units():<{unit_width}}")
    print("-" * (section_width + subject_width + unit_width + 15))
    print(f"Date Printed: {student.date_printed}")
    print('-' * (section_width + subject_width + unit_width + 15))
