from pyramid.view import view_defaults, view_config


@view_defaults(renderer='home.jinja2')
class UIViews:
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(route_name='users', renderer='users.jinja2')
    def users(self):
        subreq = self.request.blank(self.request.route_url('get_all_users'))
        response = self.request.invoke_subrequest(subreq)
        json_payload = response.json_body

        return dict(users=json_payload)

    @view_config(route_name='adduser', renderer='adduser.jinja2')
    def adduser(self):
        return dict()

    @view_config(route_name='user', renderer='user.jinja2')
    def user(self):
        id = self.request.matchdict['id']
        print(self.request.route_url('get_user', id=id))
        subreq = self.request.blank(self.request.route_url('get_user', id=id))
        response = self.request.invoke_subrequest(subreq)
        return dict(user=response.json_body)

    @view_config(route_name='home')
    def home(self):
        return dict()
