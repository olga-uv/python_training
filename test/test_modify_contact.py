from model.contact import Contact


def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First name"))
    app.contact.modify_first_contact(Contact(firstname="First Name"))
