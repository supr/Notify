from pyramid.config import Configurator
from notify.resources import Root
from pyramid.mako_templating import renderer_factory as mako_factory

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.add_renderer(".mk", mako_factory)
    config.add_route("home", "/")
    config.add_route("subscribe", "/subscribe")
    config.add_route("publisher", "/pub-sub/{uid}")
    config.add_route("socket.io", "/socket.io/*remaining")
    config.scan('notify.views')
    #config.add_view('notify.views.my_view',
    #                context='notify:resources.Root',
    #                renderer='notify:templates/mytemplate.pt')
    config.add_static_view('static', 'notify:static')
    return config.make_wsgi_app()

