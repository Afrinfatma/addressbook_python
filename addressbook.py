print("<<<<<<<<<<<<<<<<<<<<<<Welcome to Addressbook>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


class Person:

    def __init__(self, fname, lname, address, city, state, zip, phone_no, email):
        self.firstname = fname
        self.lastname = lname
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone_no
        self.email = email

    def __str__(self):
        """
            Description: To return textual content of the Contacts class Object
            Parameters: Takes Instance (Object) of class as arguments
            Returns: Returns String Representation of object, understandable by User
        """
        return f"Full Name is {self.firstname} {self.lastname}\nFull address is {self.address},{self.city},{self.state},{self.zip}\nPhone Number & email is {self.phone} and {self.email} respectively"

def add_contacts_frm_console():
    first_name = input("First name : ")
    last_name = input("Last name : ")
    address = input("Address : ")
    city = input("City : ")
    state = input("State : ")
    zip = input(" Zip : ")
    phone_number = input(" Phone-Number : ")
    email = input("Email : ")
    contact_obj = Person(first_name, last_name, address, city, state, zip, phone_number, email)

    return contact_obj

def storing_personlist():
    """
            Description: Adding Contact Details form Console in list
            Parameters: None
            Returns: Returns a list containing objects of Person Class that is taken form Console .
        """
    while True:
        contact_obj = add_contacts_frm_console()
        contacts_list.append(contact_obj)
        contacts_add_choice = input(
            "Enter \"Y\" for adding more & \"N\" to stop adding: ")
        if (contacts_add_choice.upper() == "N"):
            break
    return contacts_list


if __name__ == '__main__':
    contacts_list = []
    storing_personlist()
    for item in contacts_list:
        print(str(item))
