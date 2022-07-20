from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Name", middlename="Middle name", lastname="Last name", nickname="Nick", title="Title",
                               company="Company name", address="Address", home_phone="phone", mobile_phone="phone", work_phone="phone", fax="Fax",
                               email="email", email2="email", email3="email", homepage="Homepage", byear="1111",
                               ayear="2222", address2="Address 2", phone2="phone", notes="Notes"))
    app.session.logout()
