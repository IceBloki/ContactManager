from contact_information.contact_info import ContactInfo
from file_manager.file_manager import FileManager
import os



class Organization(ContactInfo):
    
   
    relative_organization_path = os.path.join(os.path.dirname(os.path.abspath("ContactManager")), "file_manager", "organization.txt")


    def __init__(self, name, date_of_creation, email, phone, address, members):
        super().__init__(name, "", date_of_creation, email, phone, address)

        try:
            Organization.counter = Organization.get_organization_counter()
        except FileNotFoundError:
             Organization.counter = 0
        except ValueError:
             Organization.counter = 0
        Organization.counter += 1
        
        self.date_of_creation = date_of_creation
        self.members = members
        self.organization = f"{self.counter}. {self.name}, {self.date_of_creation}, {self.email}, {self.phone}, {self.address}, {self.members}"+ ";" + "\n"

 
    def set_info(self):
            return FileManager.file_writer(self.relative_organization_path, self.organization)
 
    def add_info(self):
            return FileManager.file_append(self.relative_organization_path, self.organization)
  
    def get_info(self):
            return FileManager.file_reader(self.relative_organization_path)
    
    def read_lines(self):
            return FileManager.read_lines(self.relative_organization_path)
    
    @classmethod
    def setup_organization(cls):
        name = input("Enter organization name: ")
        date_of_creation = input("Enter date of creation: ")
        email = input("Enter organization email: ")
        phone = input("Enter organization phone: ")
        address = input("Enter organization address: ")
        members = input("Enter the number of members: ")
        org = Organization(name, date_of_creation, email, phone, address, members)
        print("Organization information has been added.")
        return org
    

    @classmethod
    def print_organization_info(cls):
        org_info = Organization.get_info(cls)
        print("Organization Information:")
        print(org_info)

    @classmethod
    def get_organization_counter(cls):
        lines = Organization.read_lines(cls)
        for line in lines:
            fields = line.split(".")
            cls.counter = int(fields[0])  
        return cls.counter