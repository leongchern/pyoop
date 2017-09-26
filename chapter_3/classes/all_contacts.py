class ContactList(list):
    def search(self,name):
        matching_contacts=[]
        for c in self:
            if name in c.name:
                matching_contacts.append(c)
        return matching_contacts

class Contact:
    all_contacts=ContactList()

    def __init__(self, name, email):
        self.name=name
        self.email=email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self,order):
        print("If this were a real system we would send "
              "'{}' order to '{}'".format(order,self.name))

class Friend(Contact):
    def __init__(self, name,email,phone):
        super().__init__(name, email)
        self.phone= phone

class MailSender:
    def send_mail(self,message):
        print("Sending mail to " + self.email)
        # Add email logic here

class EmailableContact(MailSender, Contact):
    pass

class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code


