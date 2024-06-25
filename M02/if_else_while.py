# Harjot Singh
# if_else_while.py
# Accept student names and GPAs and test if the student qualifies
# for either the Dean's List or the Honor Roll.

continue_program = True

while continue_program:
    last_name = str(input("Enter a student's last name, or 'ZZZ' to terminate program: "))
    if last_name == 'ZZZ':
        continue_program = False
        break

    first_name = str(input("Enter a student's first name: "))

    GPA = float(input("Enter a student's GPA: "))

    if (GPA >= 3.5):
        print(first_name, " ", last_name, " made the Dean's List.")
    elif (GPA >= 3.25):
        print(first_name, " ", last_name, " made the Honor's List.")
    else:
        print(first_name, last_name, " did not receive an award.")
