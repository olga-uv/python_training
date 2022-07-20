from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="New name", header="New header ", footer="New footer"))
    app.session.logout()
