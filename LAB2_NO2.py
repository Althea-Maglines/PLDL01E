#initialize the values of student's name, final quizzes, final research/assignment, final project, and final exam ratings
student_name = ""
final_quizzes = 0
final_res_assign = 0
final_proj = 0
final_exam = 0

#input the student's name, final quizzes, final research/assignment, final project, and final exam rating
student_name = str(input("Enter the value of Student's name:"))
final_quizzes = float(input("Enter the value of Final Quizzes:"))
final_res_assign = float(input("Enter the values of Research/Assignment:"))
final_proj = float(input("Enter the value of Final Project:"))
final_exam = float(input("Enter the value of Final Exam Rating:"))

#setting the formula for final grade
final_grd = 0.30 * final_quizzes + 0.10 * final_res_assign + 0.40 * final_exam + 0.20 * final_proj

#determine the equivalent grade for the numerical value obtained by the following grading remarks
    #assign a grade of 4.00 if the final grade falls between 100-98
if 98 <= final_grd <= 100:
    equivalent_grd = 4.00

    #assign a grade of 3.75 if the final grade falls between 97-95
elif 95 <= final_grd <= 97:
    equivalent_grd = 3.75

    #assign a grade of 3.50 if the final grade falls between 94-92
elif 92 <= final_grd <= 94:
    equivalent_grd = 3.50

    #assign a grade of 3.25 if the final grade falls between 91-89
elif 89 <= final_grd <= 91:
    equivalent_grd = 3.25

    #assign a grade of 3.00 if the final grade falls between 88-86
elif 86 <= final_grd <= 88:
    equivalent_grd = 3.00

    #asssign a grade of 2.75 if the final grade falls between 85-83
elif 83 <= final_grd <= 85:
    equivalent_grd = 2.75

    #assign a grade of 2.50 if the final grade falls between 82-80
elif 80 <= final_grd <= 82:
    equivalent_grd = 2.50

    #assign a grade of 2.25 if the final grade falls between 79-77
elif 77 <= final_grd <= 79:
    equivalent_grd = 2.25

    #assign a grade of 2.00 if the final grade falls between 76-74
elif 74 <= final_grd <= 76:
    equivalent_grd = 2.00

    #assign a grade of 1.75 if the final grade falls between 73-71
elif 71 <= final_grd <= 73:
    equivalent_grd = 1.75

    #assign a grade of 1.50 if the final grade falls between 70-68
elif 68 <= final_grd <= 70:
    equivalent_grd = 1.50

    #assign a grade of 1.25 if the final grade falls between 67-64
elif 64 <= final_grd <= 67:
    equivalent_grd = 1.25

    #assign a grade of 1.00 if the final grade falls between 63-64
elif 60 <= final_grd <= 63:
    equivalent_grd = 1.00

    #if the final grade is more than 100 the remarks will be invalid
elif final_grd > 100:
     final_grd = 100
     equivalent_grd = str("invalid data input")

    #assign a grade of 0.00 if it falls below 60
else:
    equivalent_grd = 0.00

#diplay the student's name, final quizzes, final research/assignment, final project, and final grade, and the equivalent grading remarks
print("Student's Name:",student_name)
print("Final Quizzes:",final_quizzes)
print("Final Research/Assignment:",final_res_assign)
print("Final Project:",final_proj)
print("Final Grade:",final_grd)
print("Final Exam:",final_exam)
print("Equivalent Grading Remarks:",equivalent_grd)

