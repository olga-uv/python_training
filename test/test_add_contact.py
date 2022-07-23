# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(Contact(firstname="name", middlename="middlename", lastname="lastname", nickname="nick",
                               title="title", company="comp", address="adr", home_phone="phone", mobile_phone="phone",
                               work_phone="phone", fax="fax", email="email", email2="email", email3="email",
                               homepage="site", address2="adr", phone2="phone", notes="notes"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
