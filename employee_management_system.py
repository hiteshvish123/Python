#pylint: disable = C0114
#pylint: disable = C0115
#pylint: disable = C0116

def employee_data():

    while True:

        print("Enter 1 -> Add new employee details")
        print("Enter 2 -> Add the employee data toa file")
        print("Enter 3 -> Retrieve all employee records")
        print("Enter 4 -> Retrieve single employee record")
        print("Enter 5 -> Delete all employee records")
        print("Enter 6 -> Delete single employee record")

        choice1 = int(input("Enter the Choice:"))

        if choice1 == 1:
            # statement
            choice2 = int(
                input("Enter the no of employee's details to be added: "))

            for i in range(0, choice2):
                emp_data = {NAME: input("Name: "), ID: int(input("ID: ")), JOINING_DATE: int(
                    input("Date format -> DDMMYYYY: ")), PROJECT_NAME: input("Project Name: ")}
        if choice1 == 2:
            # statement
        if choice1 == 3:
            # statement
        if choice1 == 4:
            # statement
        if choice1 == 5:
            # statement
        if choice1 == 6:
            # statement
