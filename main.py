from contact_information.organization.organization import *
from contact_information.employees.employees import *
from contact_information.customers.customers import *


def setup_organization():
    name = input("Enter organization name: ")
    date_of_creation = input("Enter date of creation: ")
    email = input("Enter organization email: ")
    phone = input("Enter organization phone: ")
    address = input("Enter organization address: ")
    members = input("Enter the number of members: ")
    org = Organization(name, date_of_creation, email, phone, address, members)
    Organization.set_info(org)
    print("Organization information has been added.")

def add_customer():
    name = input("Enter customer name: ")
    surname = input("Enter customer surname: ")
    date_of_birth = input("Enter customer date of birth: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone: ")
    address = input("Enter customer address: ")
    occupation = input("Enter customer occupation: ")
    customer = Customer(name, surname, date_of_birth, email, phone, address, occupation)
    Customer.add_info(customer)
    print("Customer information has been added.")
    return customer

def add_employee():
    name = input("Enter employee name: ")
    surname = input("Enter employee surname: ")
    date_of_birth = input("Enter employee date of birth: ")
    email = input("Enter employee email: ")
    phone = input("Enter employee phone: ")
    address = input("Enter employee address: ")
    job_title = input("Enter employee occupation: ")
    department = input("Enter employee's department: ")
    employee = Employee(name, surname, date_of_birth, email, phone, address, job_title, department)
    Employee.add_info(employee)
    print("Employee information has been added.")
    

def print_organization_info():
    org_info = Organization.get_info()
    print("Organization Information:")
    print(org_info)

def print_customers_info(customer):
    customer_info = Customer.get_info(customer)
    print("Customer Information:")
    for item in customer_info:
        # Split the stored data on semicolons and print each field
        fields = item.split(';')
        print("Name:", fields[0])
        print("Surname:", fields[1])
        print("Date of Birth:", fields[2])
        print("Email:", fields[3])
        print("Phone:", fields[4])
        print("Address:", fields[5])
        print("Occupation:", fields[6])
        print()

def print_employee_info():
    employee_info = Employee.get_info()
    print("Employee Information:")
    print(employee_info)



def main():
    """org = Organization("Velika Firma","1.1.2000","velikafirma@example.com","01/1111-111","Ulica Velike Firme 1",50)
    customer = Customer("John", "Doe", "1.1.1111", "john@example.com", "0921234567", "Zagreb", "Linux Systems Admin")
    employee = Employee("Iva", "Ivic", "2.1.1111", "iva@example.com", "0931234567", "Zagreb", "Windows Systems Admin", None)
    Customer.add_info(customer)
    print(Organization.get_info(org)"""


    while True:
        print("\nMenu:")
        print("1. Set up organization")
        print("2. Add a customer")
        print("3. Add a employee")
        print("4. Print organization information")
        print("5. Print customer information")
        print("6. Print employee information")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            setup_organization()
        elif choice == "2":
            add_customer()
        elif choice == "3":
            add_employee()
        elif choice == "4":
            print_organization_info()
        elif choice == "5":
            global customer
            print_customers_info(customer)
        elif choice == "6":
            print_employee_info()
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()