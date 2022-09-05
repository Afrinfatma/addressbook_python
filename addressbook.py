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
        return f"Full Name is {self.firstname} {self.lastname}\nFull address is {self.address},{self.city},{self.state},{self.zip}\nPhone Number & email is {self.phone} and {self.email} "

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

def edit_delete_person_details(contacts_list):
    """
           Description: Editing Contact Details form Console i.e. by user choice
           Parameters: None
           Returns: Returns a list containing objects of Contact Class that is taken form Console i.e. User
       """
    edit_delete_contact_by_name=input("Enter the name of person whose contact details you want to edit or delete ").upper()
    try:
        for item in contacts_list:
            if item.firstname.upper()==edit_delete_contact_by_name:
                choice=input(
                    "Enter choice either you want to edit or delete:\n 1:firstname,2:lastname,3:Address,4:City,5:State,6:zip,7:phone,8:email,9:Delete ")
                if (choice == "1"):
                    fn = input("Enter updated first name: ")
                    item.first_name = fn
                elif (choice == "2"):
                    ln = input("Enter updated last name: ")
                    item.last_name = ln
                elif (choice == "3"):
                    addrs = input("Enter updated address: ")
                    item.address = addrs
                elif (choice == "4"):
                    city = input("Enter updated city: ")
                    item.city = city
                elif (choice == "5"):
                    state = input("Enter updated state: ")
                    item.state = state
                elif (choice == "6"):
                    zip = input("Enter updated zip: ")
                    item.zip = zip
                elif (choice == "7"):
                    phn_no = input("Enter updated phn number: ")
                    item.phone_number = phn_no
                elif (choice == "8"):
                    email = input("Enter updated email: ")
                    item.email = email
                elif (choice == "9"):
                    contacts_list.remove(item)
                    return contacts_list
                else:
                    print("Invalid Choice")
            else:
                print("The name u entered does not exist")

    except Exception as e:
        print(e)



if __name__ == '__main__':
    contacts_list = []
    storing_personlist()
    user_choice=input("Do you want to edit or delete the contact details\"Y\" or \"N\":").upper()
    if user_choice.upper()=='Y':
        edit_delete_person_details(contacts_list)



    for item in contacts_list:
        print(str(item))