import inspect
from typing import Callable


class DefaultIndex:
    """Default index view"""

    def __call__(self, *args, **kwargs):
        return '200 Success', 'Welcome to my custom framework!'


class PageNotFound404:
    """Default 404 view"""

    def __call__(self, *args, **kwargs):
        return '404 Page Not Found', ''  # TODO: a page not found template


class Framework:
    """My custom framework class"""

    def __init__(self, routes: dict = None):
        """
        Framework class initialization function
        Pass server routes for accessing them later
        :param routes: server routes
        """
        self.routes = routes if routes else {'/': DefaultIndex()}
        self._not_found_view = PageNotFound404

    def __call__(self, environ, start_response):
        """
        Framework callable
        :param environ: a WSGI environment
        :param start_response: a callable accepting a status code,
            a list of headers, and an optional exception context to
            start the response
        :return:
        """
        code, body = self._get_view(environ['PATH_INFO'])
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    def _get_view(self, path: str):
        """
        Calls view via corresponding resource
        path and returns response code and body
        :param path: resource path
        :return: (response code, body)
        """
        path = f'{path}/' if not path.endswith('/') else path
        if path in self.routes:
            view = self.routes[path]
        else:
            view = self.not_found_view
        return view()

    @property
    def not_found_view(self):
        """Not found view getter"""
        # Return a callable class instance or a function object
        return self._not_found_view() if inspect.isclass(self._not_found_view) else self._not_found_view

    @not_found_view.setter
    def not_found_view(self, not_found_cls: Callable):
        """
        Not found view setter
        :param not_found_cls: a callable function
        :return:
        """
        self._not_found_view = not_found_cls
