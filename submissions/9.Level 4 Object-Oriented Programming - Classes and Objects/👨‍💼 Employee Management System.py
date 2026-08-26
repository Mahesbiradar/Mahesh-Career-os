
#1. Create an Employee class

class Employee:

    company = "ABC Technologies"

    def __init__(self,name,salary,employee_id,department):

        self.name = name
        self.salary = salary
        self.employee_id = employee_id
        self.department = department

    def display_details(self):

        print(f"Name: {self.name}\nSalary: {self.salary}\nEmployee Id: {self.employee_id}\nDepartment: {self.department}")


    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @staticmethod
    def is_valid_salary(salary):

        return salary > 0


# 2. Create a file (Done)



# 5. Custom Exception — Small Addition

class InvalidEmployeeRecordError(Exception):
    pass

# 3. Load employees from the file


def load_employees(filename):

    try:

        with open(filename,"r") as file:

            employees_data = []

            for line in file:

                if not line.strip():
                    continue

                try:
                    data = line.strip().split(",")

                    if len(data) != 4:
                        raise InvalidEmployeeRecordError(
                            f"Improper record format: '{line.strip()}'"
                        )

                    employee_id  = data[0].strip()
                    name = data[1].strip()

                    try:
                        salary = int(data[2].strip())

                        if not Employee.is_valid_salary(salary):
                            raise InvalidEmployeeRecordError(f"Salary must be positive: {salary}")

                    except ValueError:
                        raise InvalidEmployeeRecordError(
                            f"Improper salary format: '{data[2].strip()}'"
                        )
                    department = data[3].strip()

                    employees_data.append(Employee(name,salary,employee_id,department))

                except InvalidEmployeeRecordError as e:

                    print(f"Skipping line due to error: {e}")

                    continue  

            return employees_data


    except FileNotFoundError:
        print("File Not Exist")
        return None 



# Execution and Output Processing


data = "submissions\employees.txt"


employees_list = load_employees(data)

if employees_list :
# 4. Use previous topics

# A. Find Backend employees

    backend_employees = [emp.name for emp in employees_list if emp.department == "Backend"]


    # B. Find highest-paid employee

    heighest_paid_employee = max(employees_list,key=lambda emp:emp.salary )


    employees_dict = {emp.employee_id: emp for emp in employees_list}


    # 6. Final Output

    print("===== EMPLOYEE REPORT =====")

    print(f"Company: {Employee.company}")
    print(f"Total Employees: {len(employees_list)}")
    print("Backend Employees:")

    for name in backend_employees:
        print(name)

    print("Highest Paid:")
    print(f"{heighest_paid_employee.name} - {heighest_paid_employee.salary}")

    print("Employee IDs:")

    for ids in employees_dict.keys():

        print(ids)


