from contact_information.organization.organization import *
from contact_information.employees.employees import *
from contact_information.customers.customers import *


def main():

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
            org = Organization.setup_organization()
            Organization.add_info(org)
        elif choice == "2":
            customer = Customer.add_customer()
            Customer.add_info(customer)
        elif choice == "3":
            employee = Employee.add_employee()
            Employee.add_info(employee)
        elif choice == "4":
            Organization.print_organization_info()
        elif choice == "5":
            Customer.print_customer_info()
        elif choice == "6":
            Employee.print_employee_info()
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()