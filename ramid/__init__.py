from pyramid.config import Configurator
from ramid.views.user import UserViews


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    # config.include('pyramid_chameleon')
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path("templates")
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('users', '/users')
    config.add_route('adduser', '/users/addUser')
    config.add_route('user', '/user/{id}')

    config.add_route('organisations', '/organisations', request_method='GET')
    config.add_route('organisation', '/organisation/{id}')

    config.add_route('add_user', 'api/users', request_method='POST')
    config.add_route('delete_user', 'api/users/{id}', request_method='DELETE')
    config.add_route('update_user', 'api/users/{id}', request_method='PUT')
    config.add_route('get_all_users', 'api/users', request_method='GET')
    config.add_route('get_user', 'api/users/{id}', request_method='GET')

    config.add_route('get_all_organisations', 'api/organisations', request_method='GET')
    config.add_route('get_organisation', 'api/organisations/{id}', request_method='GET')
    config.add_route('add_organisation', 'api/organisations', request_method='POST')
    config.add_route('update_organisation', 'api/organisations/{id}', request_method='PUT')
    config.add_route('delete_organisation', 'api/organisations/{id}', request_method='DELETE')
    config.add_route('add_organisation_user', 'api/organisations/{id}/addUser', request_method='POST')
    config.scan()
    return config.make_wsgi_app()
