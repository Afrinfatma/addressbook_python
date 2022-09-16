import pytest
from addressbook import Contact ,Addressbook

@pytest.fixture()
def contact_object():
    try:
        return Contact("Afrin","Fatma","Hinjewadi","Pune","Maharashtra","889667","787707667777","asdfg.z@g.com")
    except Exception as e:
        print (e)


@pytest.fixture()
def addressbook_object():
    try:
        return Addressbook("Personal")
    except Exception as e:
        print(e)

def test_fullname(contact_object):
    try:
        name="Afrin Fatma"
        print(contact_object.full_name == name)
    except Exception as e:
        print(e)

def test_addcontact(contact_object,addressbook_object):
    try:
        assert len(addressbook_object)==0
        addressbook_object.add_contact(contact_object)
        assert  len(addressbook_object)== 1
        contact_object2=Contact("Shakir","Ahmad","Hinjewadi","Pune","Maharashtra","889667","78767548777","agthfg.z@g.com")
        addressbook_object.add_contact(contact_object2)
        assert len(addressbook_object)== 2
        contact_object3 = Contact("Hashir ", "Ahmad", "Hinjewadi", "Pune", "Maharashtra", "889667", "78767548777",
                                  "agthfg.z@g.com")
        addressbook_object.add_contact(contact_object3)
        print(len(addressbook_object))
    except Exception as e:
        print (e)

def test_getcontact(addressbook_object,contact_object):
    try:
        addressbook_object.add_contact(contact_object)
        act_contact=addressbook_object.get_contact("Afrin")
        assert isinstance(act_contact,Contact)
        assert act_contact.full_name=="Afrin Fatma"
        print(act_contact.full_name)
    except Exception as e:
        print(e)

def test_editcontact(addressbook_object,contact_object):
    try:
        addressbook_object.add_contact(contact_object)
        addressbook_object.edit_contact("Afrin","fatma","YJ","JU","MP",'989766','7979969595',"asdg.z@g.com")
        assert contact_object.address=='YJ'
        print(contact_object.address)
        assert contact_object.city=='JU'
        print(contact_object.city)
    except Exception as e:
        print(e)

def test_delcontact(addressbook_object,contact_object):
    try:
        addressbook_object.add_contact(contact_object)
        assert len(addressbook_object)==1
        addressbook_object.delete_contact("Afrin")
        assert len(addressbook_object)==0
        print(len(addressbook_object))
    except Exception as e:
        print(e)