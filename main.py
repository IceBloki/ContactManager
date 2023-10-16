from contact_information.organization.organization import *
from contact_information.employees.employees import *
from contact_information.customers.customers import *


def main():

    while True:
        print("\nMenu:")
        try:
            Organization.get_organization_counter()
            print("1. Add a new organization")
            print("2. Print organization information")
            print("3. Print all organizations")
            print("4. Pick up an organization")
            print("5. Add a customer")
            print("6. Add a employee")
            print("7. Print customer information")
            print("8. Print employee information")
            print("9. Exit")
        except FileNotFoundError:
            print("1. Setup a organization")
            print("3. Print all organizations")
            print("9. Exit")
           
        
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            org = Organization.add_organization()
            Organization.add_info(org)
        elif choice == "2":
            Organization.print_organization_info()
        elif choice == "3":
            Organization.print_organizations_info()
        elif choice == "4":
            Organization.pick_organization()
        elif choice == "5":
            customer = Customer.add_customer()
            Customer.add_info(customer)
        elif choice == "6":
            employee = Employee.add_employee()
            Employee.add_info(employee)
        elif choice == "7":
            Customer.print_customer_info()
        elif choice == "8":
            Employee.print_employee_info()
        elif choice == "9":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()