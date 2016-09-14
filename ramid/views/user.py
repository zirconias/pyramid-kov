from pyramid.view import view_defaults, view_config
from ..models.user import User

USERS = []


def first(iterable, default=None):
    for item in iterable:
        return item
    return default


@view_defaults(renderer='json', route_name='users')
class UserViews:
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(route_name='get_all_users')
    def get_all(self):
        usrs = USERS
        username = self.request.params.get('username')
        page = int(self.request.params.get('page', 0))
        if username:
            usrs = [x for x in usrs if username in x.username]

        if page > 0:
            paged_users = [usrs[i:i + 2] for i in range(0, len(usrs), 2)]
            usrs = paged_users[page - 1]

        return usrs

    @view_config(route_name='add_user')
    def add_user(self):
        params = dict(self.request.params)
        newuser = User(params["username"], params["first_name"], params["last_name"], params["password"],
                       params["email"])

        USERS.append(newuser)
        return {'id': newuser.id, 'created': 'created'}

    @view_config(route_name='get_user')
    def get_user(self):
        id = self.request.matchdict['id']
        user = first(x for x in USERS if x.id == id)
        if user:
            return user
        else:
            return {'found': 'false', 'message': 'user not found'}

    @view_config(route_name='delete_user')
    def delete_user(self):
        id = self.request.matchdict['id']
        for user in USERS:
            if user.id == id:
                USERS.remove(user)
                return {'deleted': 'true', 'id': id}
            else:
                return {'deleted': 'false', 'message': 'user not found'}
        return {'deleted': 'false', 'message': 'there is no user to delete'}
