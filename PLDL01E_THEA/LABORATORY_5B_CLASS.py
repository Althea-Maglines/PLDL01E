import LABORATORY_5_CLASS
from PLDL01E_THEA.LABORATORY_5A_CLASS import section_width, subject_width, unit_width

student = LABORATORY_5_CLASS.Student()
student.student_subject()
section_width = 10
subject_width = 40
unit_width = 10

def display_student_information():
    print(f"\n\n\nStudent Name: {student.student_name:<30}")
