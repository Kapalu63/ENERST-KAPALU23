class Employee:
    def __init__(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary

    # Public getter for name
    def get_name(self):
        return self.__name

    # Public setter for name
    def set_name(self, name):
        self.__name = name

    # Public getter for id
    def get_id(self):
        return self.__id

    # Public setter for id
    def set_id(self, id):
        self.__id = id

    # Public getter for salary
    def get_salary(self):
        return self.__salary

    # Public setter for salary with validation
    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = salary

# Example usage:
emp = Employee("John Doe", 123, 50000)
print(emp.get_name())  # Output: John Doe
emp.set_salary(60000)
print(emp.get_salary())  # Output: 60000
e value.

