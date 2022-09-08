import json
import logging

from loghandler import logger


log = '%(lineno)d ** %(asctime)s ** %(message)s'
logging.basicConfig(filename='Addressbook.log', filemode='w', format=log, level=logging.DEBUG)

logging.debug("Address book Program running................")
class Contact:

    def __init__(self, fname, lname, address, city, state, zip,phone_number, email):
        self.first_name = fname
        self.last_name = lname
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number
        self.email = email

    @property
    def full_name(self):
        """
        :return: full name
        """
        try:
            return self.first_name + " " + self.last_name
        except Exception as e:
            logger.error(e)

    def to_string(self):
        try:
            return f'Full Name: {self.full_name}, Address: {self.address},City :{self.city}, State:{self.state}, Zip:{self.zip} ' \
                   f'Phone Number: {self.phone_number}, Email: {self.email} '
        except Exception as e:
            print(e)
    def to_json(self):
        try:
            return f'Full Name: {self.full_name}, Address: {self.address},City :{self.city}, State:{self.state}, Zip:{self.zip} ' \
                   f'Phone Number: {self.phone_number}, Email: {self.email} '
        except Exception as e:
            print(e)
class Addressbook:
    def __init__(self, name):
        self.name = name
        self.contact_dict = {}

    def add_contact(self, contact_obj):
        self.contact_dict.update({contact_obj.first_name: contact_obj})
        return self.contact_dict

    def get_contact(self, name):
        try:
            return self.contact_dict.get(name)
        except Exception as e:
            logger.error(e)

    def delete_contact(self, key):
        """
        this function  delete details  of contacts
        :param key: user string input
        :return: None
        """
        try:
            contact = self.get_contact(key)
            if not contact:
               print("invalid contact")

            self.contact_dict.pop(key)
            print("contact deleted successfully")
        except Exception as e:
            logger.error(e)


    def display_contact(self):
        """
        displaying contact in key and value format
        :return: None
        """
        try:
            for key, value in self.contact_dict.items():
                print(key, value.to_string())
        except Exception as e:
            print(e)
    def add_json_contact(self):
        try:
            json_result_dict={}
            for key,value in self.contact_dict.items():
                json_result_dict.update({key:value.to_json()})
                return json_result_dict
        except Exception as e:
            print(e)

if __name__ == '__main__':

    print("<<<<<<<<<<<<<<<<<<<<<<Welcome to Addressbook>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    addressbook_dict = {}
    def add_addressbook():

        try:
            addressbook_name=input("Enter the address book name :")
            print(addressbook_name)
            addressbook_obj = Addressbook(addressbook_name)
            addressbook_dict.update({addressbook_obj.name: addressbook_obj})

            return addressbook_dict
        except Exception as e:
            print(e)


    def display_addressbook():
        """
        helper function to display addressbook
        :return:
        """
        try:
            for index, addressbook_name in enumerate(addressbook_dict.keys()):
                print(index, addressbook_name)
        except Exception as e:
            print(e)



    def add_contact_address_book():
        """
        helper function for adding contacts in to address book
        :return: None
        """
        try:
            addressbook_name = input("Enter the address book name:\n")
            addressbook_object = addressbook_dict.get(addressbook_name)
            if addressbook_object is None:
                addressbook_object = Addressbook(addressbook_name)
                addressbook_dict.update({addressbook_object.name: addressbook_object})
                return

            first_name = input("Enter the first name:\n")
            last_name = input("Enter the last name:\n")
            address = input("Enter the address:\n")
            city = input("Enter the city:\n")
            state = input("Enter the state:\n")
            zip = input("Enter the zip:\n")
            phone_number = input("Enter the phone number:\n")
            email = input("Enter the email:\n")
            contact_object = Contact( first_name, last_name, address,city,state,zip, phone_number, email)
            addressbook_object.add_contact(contact_object)
        except Exception as e:
            print(e)


    def edit_contact_address_book():
        """
        helper function for updating contacts in address book
        :return: None
        """
        try:
            addressbook_name = input("Enter the address book name:\n")
            addressbook_object = addressbook_dict.get(addressbook_name)
            if addressbook_object is None:
                print("Address book does not exist")
                return
            first_name = input("Enter the contact person name:\n")
            contact_obj = addressbook_object.get_contact(first_name)
            if contact_obj is None:
                print("Contact is not available")
                return
            first_name = input("Enter the first name:\n")
            last_name = input("Enter the last name:\n")
            address = input("Enter the address:\n")
            city = input("Enter the city:\n")
            state = input("Enter the state:\n")
            zip = input("Enter the zip:\n")
            phone_number = input("Enter the phone number:\n")
            email = input("Enter the email:\n")
            # address_book_object.update_contact(sl_no, first_name, last_name, address, phone_number, email)
            contact = Contact(fname=first_name,lname=last_name,address=address, city=city, state=state, zip=zip,phone_number=phone_number,
                                  email=email)
            addressbook_object.add_contact(contact)
        except Exception as e:
            print(e)


    def get_contact_address_book():
        """
        helper function to get a contact from address book
        :return: None
        """
        try:
            addressbook_name = input("Enter the address book name:\n")
            addressbook_object = addressbook_dict.get(addressbook_name)
            if addressbook_object is None:
                print("Address book is not exist")
                return
            first_name = input("Enter the first name:\n")
            contact = addressbook_object.get_contact(first_name)
            if contact is None:
                print("contact doesn't exist")
                return
            print(contact.to_string())
        except Exception as e:
            print(e)


    def delete_contact_address_book():
        """
         Helper function to delete the contacts
        :return: None
        """
        try:
            address_book_name = input("Enter the address book name:\n")
            addressbook_obj = addressbook_dict.get(address_book_name)
            if addressbook_obj is None:
                print("Address book doesn't exist")
                return
            first_name = input("Enter the first name:\n")
            print(
            addressbook_obj.delete_contact(first_name))
        except Exception as e:
            print(e)


    def display_contact_address_book():
        """
        Helper function to display contacts
        :return: None
        """
        try:
            address_book_name = input("Enter the address book name:\n")
            address_book_object = addressbook_dict.get(address_book_name)
            if address_book_object is None:
                print("Address book doesn't exist")
                return
            address_book_object.display_contact()
        except Exception as e:
            print(e)

    def write_json_function():
        try:
            json_dict={}
            for name ,obj in addressbook_dict.items():
                json_dict.update({name:obj.add_json_contact()})
            with open ("json_addressbook.json","w")as file:
                json.dump(json_dict,file,indent=4)
        except exception as e:
            print(e)
    def read_json_function():
        try:
            with open("json_addressbook.json","r")as json_file:
                data=json.loads(json_file.read())
                print(data)
        except Exception as e:
            print (e)
        def execute_contact():
            print("Invalid! Enter the correct choice")

    choice_dict = {1: add_addressbook, 2: display_addressbook, 3: add_contact_address_book,
                   4: get_contact_address_book,5:edit_contact_address_book,
                   6: delete_contact_address_book,7: display_contact_address_book,
                   8:write_json_function,9:read_json_function}

    while True:
            print(
                "Enter the choice: \n1.Add addressbook\n2.Display addressbook\n3.Add contacts\n4.Get contacts\n5.Edit "
                "contacts\n6.Delete contacts\n7.Display contacts\n 8.Json write\n 9.Read json\n0.Exit")
            choice = int(input())
            if choice in choice_dict.keys():
                choice_dict.get(choice)()
            else:
                execute_contact()

print("this is address book ")

