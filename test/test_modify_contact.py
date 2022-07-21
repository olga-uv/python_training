from model.contact import Contact


def test_modify_first_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="First Name"))
