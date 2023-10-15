from contact_information.contact_info import ContactInfo
from file_manager.file_manager import FileManager
import os


class Customer(ContactInfo, FileManager):

    relative_coustumer_path = os.path.join(os.path.dirname(os.path.abspath("ContactManager")), "file_manager", "customers.txt")

    def __init__(self, name, surname, date_of_birth, email, phone, address, occupation):
        super().__init__(name, surname, date_of_birth, email, phone, address)

        try:
            Customer.counter = Customer.get_customer_counter()
        except FileNotFoundError:
             Customer.counter = 0
        except ValueError:
             Customer.counter = 0
        Customer.counter += 1

        self.occupation = occupation
        self.customer = f"{self.counter}. {self.name}, {self.surname}, {self.date_of_birth}, {self.email}, {self.phone}, {self.address}, {self.occupation}" + ";" + "\n"
    
    
    def set_info(self):
            return FileManager.file_writer(self.relative_coustumer_path, self.customer)
   
    def add_info(self):
            return FileManager.file_append(self.relative_coustumer_path, self.customer)
   
    def get_info(self):
            return FileManager.file_reader(self.relative_coustumer_path)
    
    def read_lines(self):
            return FileManager.read_lines(self.relative_coustumer_path)
    

    @classmethod
    def add_customer(cls):
        name = input("Enter customer name: ")
        surname = input("Enter customer surname: ")
        date_of_birth = input("Enter customer date of birth: ")
        email = input("Enter customer email: ")
        phone = input("Enter customer phone: ")
        address = input("Enter customer address: ")
        occupation = input("Enter customer occupation: ")
        customer = Customer(name, surname, date_of_birth, email, phone, address, occupation)
        print("Customer information has been added.")
        return customer
    

    @classmethod
    def print_customer_info(cls):
        customer_info = Customer.get_info(cls)
        print("Customer Information:")
        print(customer_info)

    @classmethod
    def get_customer_counter(cls):
        lines = Customer.read_lines(cls)
        for line in lines:
            fields = line.split(".")
            cls.counter = int(fields[0])  
        return cls.counter
    
