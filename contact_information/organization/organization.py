from contact_information.contact_info import ContactInfo
from file_manager.file_manager import FileManager
import os


class Organization(ContactInfo):
    def __init__(self, name, date_of_creation, email, phone, address, members):
        super().__init__(name, "", date_of_creation, email, phone, address)
        self.date_of_creation = date_of_creation
        self.members = members
        self.relative_organization_path = os.path.join(os.path.dirname(os.path.abspath("ContactManager")), "file_manager", "organization.txt")

        self.organization = f"{self.name};{self.date_of_creation};{self.email};{self.phone};{self.address};{self.members}"+ "\n"
        
    def set_info(self):
            return FileManager.file_writer(self.relative_organization_path, self.organization)
 
    def add_info(self):
            return FileManager.file_append(self.relative_organization_path, self.organization)
  
    def get_info(self):
            return FileManager.file_reader(self.relative_organization_path)
    