from pyramid.view import view_defaults, view_config
from ramid.models.user import User
from ..models.organisation import Organisation
from .user import *

ORGANISATIONS = []


def first(iterable, default=None):
    for item in iterable:
        return item
    return default


@view_defaults(renderer='json', route_name='organisations')
class OrganisationViews:
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(route_name='get_all_organisations')
    def get_all(self):
        orgs = ORGANISATIONS
        name = self.request.params.get('name')
        page = int(self.request.params.get('page', 0))
        # return ORGANISATIONS[page:page + 2]
        if name:
            orgs = [x for x in orgs if name in x.name]

        if page > 0:
            paged_organisations = [orgs[i:i + 2] for i in range(0, len(orgs), 2)]
            orgs = paged_organisations[page - 1]

        return orgs

    @view_config(route_name='add_organisation')
    def add_organisation(self):
        print('json_body: ', self.request.json_body)

        if not str(self.request.json_body['name']).isalnum():
            return {'created': 'false', 'message': 'please enter only alpha num chars'}

        if (first(x for x in ORGANISATIONS if x.name == self.request.json_body['name'])):
            return {'created': 'false', 'message': 'name already exists'}

        neworg = Organisation(self.request.json_body)
        # neworg = Organisation(params["name"], params["description"], params["contact"])

        ORGANISATIONS.append(neworg)
        return {'id': neworg.id, 'created': 'created'}

    @view_config(route_name='get_organisation')
    def get_organisation(self):
        id = self.request.matchdict['id']
        organisation = first(x for x in ORGANISATIONS if x.id == id)
        if organisation:
            return organisation
        else:
            return {'found': 'false', 'message': 'organisation not found'}

    @view_config(route_name='update_organisation')
    def update_organisation(self):
        # print('json_body: ', self.request.json_body)
        id = self.request.matchdict['id']
        organisation = self.request.json_body
        for org in ORGANISATIONS:
            if org.id == id:
                org.name = organisation['name']
                org.description = organisation['description']
                org.contact = organisation['contact']
                return org

        return {'updated': 'false'}

    @view_config(route_name='delete_organisation')
    def delete_organisation(self):
        id = self.request.matchdict['id']
        for organisation in ORGANISATIONS:
            if organisation.id == id:
                ORGANISATIONS.remove(organisation)
                return {'deleted': 'true', 'id': id}
            else:
                return {'deleted': 'false', 'message': 'organisation not found'}
        return {'deleted': 'false', 'message': 'there is no organisation to delete'}

    @view_config(route_name='add_organisation_user')
    def add_organisation_user(self):
        id = self.request.matchdict['id']
        organisation = first(x for x in ORGANISATIONS if x.id == id)
        if organisation:
            params = dict(self.request.params)
            # newuser = User(params["username"], params["first_name"], params["last_name"], params["password"],
            #                params["email"])
            user = first(x for x in USERS if x.id == params["id_user"])
            if user:
                organisation.add_user(user)
                return organisation
            else:
                return {'found': 'false', 'message': 'user not found'}
        else:
            return {'found': 'false', 'message': 'organisation not found'}
        return {}
