from pyramid.config import Configurator
from ramid.views.user import UserViews


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('add_user', '/users', request_method='POST')
    config.add_route('delete_user', '/users/{id}', request_method='DELETE')
    config.add_route('get_all', '/users', request_method='GET')
    config.add_route('get_user', '/users/{id}', request_method='GET')

    config.scan()
    return config.make_wsgi_app()
