import uuid


def genuuid():
    return str(uuid.uuid4())


class User(object):
    # def __init__(self, username, first_name, last_name, password, email):
    #     self.id = genuuid()
    #     self.username = username
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.password = password
    #     self.email = email
    #     self.created_at = datetime.date.today()
    #     self.updated_at = datetime.date.today()

    def __init__(self, obj):
        self.__dict__ = obj
        self.id = genuuid()

    def __json__(self, request):
        return {'id': self.id, 'username': self.username, 'first_name': self.first_name,
                'last_name': self.last_name, 'email': self.email}
