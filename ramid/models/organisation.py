import uuid


def genuuid():
    return str(uuid.uuid4())


class Organisation:
    def __init__(self, name, description, contact):
        self.id = genuuid()
        self.name = name
        self.description = description
        self.contact = contact
        self.users = []

    def add_user(self, user):
        self.users.append(user)
