# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="asd", middlename="asd", lastname="asd", nickname="asd", title="asd",
                                        company="asd", address="asd", home="asd", mobile="asd", work="asd", fax="asd",
                                        email="asd", email2="asd", email3="asd", homepage="asd", byear="1111",
                                        ayear="2222", address2="asdf", phone2="asdf", notes="asdf"))
    app.session.logout()
