import uuid


def genuuid():
    return str(uuid.uuid4())


class Organisation:
    # def __init__(self, name, description, contact):
    #     self.id = genuuid()
    #     self.name = name
    #     self.description = description
    #     self.contact = contact
    #     self.users = []

    def __init__(self, obj):
        self.__dict__ = obj
        self.id = genuuid()

    def add_user(self, user):
        self.users.append(user)

    def __json__(self, request):
        return self.__dict__

        # def __json__(self, request):
        #     return {'id': self.id, 'name': self.name, 'description': self.description,
        #             'contact': self.contact}
