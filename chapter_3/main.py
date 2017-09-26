from chapter_3.classes.all_contacts import Contact
from chapter_3.classes.all_contacts import Supplier
from chapter_3.classes.all_contacts import EmailableContact


c = Contact("Some one", "some@body.com")
s = Supplier("Sup Plya", "Sup@playa.com")
c1 = Contact("John A", "johna@example.com")
c1 = Contact("John B", "johnb@example.com")
c1 = Contact("Kanna C", "kannac@example.com")

print(c.name, c.email)
c.all_contacts

[c.name for c in Contact.all_contacts.search("John")]

# c.order("I need pliers!") # error
s.order("I need pliers!") # ok

e = EmailableContact("John Smith", "jsmith@example.net")

Contact.all_contacts
e.send_mail("Hello, this is a test email")
