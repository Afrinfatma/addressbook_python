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

    def  __str__(self):
        """
            Description: To return textual content of the Contacts class Object
            Parameters: Takes Instance (Object) of class as arguments
            Returns: Returns String Representation of object, understandable by User
        """
        return f"Full Name is {self.firstname} {self.lastname}\nFull address is {self.address},{self.city},{self.state},{self.zip}\nPhone Number & email is {self.phone} and {self.email} respectively"

if __name__=='__main__':

    print("<<<<<<<<<<<<<<<<<<<<<<Welcome to Addressbook>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    person= Person("afrin","Fatma","chitkohra","patna","bihar",800002,8989887676,"xsw.com")
    try:
        print(str(person))
    except Exception as e:
        print (e)