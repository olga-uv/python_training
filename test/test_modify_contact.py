from model.contact import Contact


def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First name"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.modify_first_contact(Contact(firstname="First Name"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)

