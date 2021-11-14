from typing import Callable


class DefaultIndex:
    def __call__(self, *args, **kwargs):
        return '200 Success', 'Welcome to my custom framework!'


class Framework:
    """My custom framework class"""

    def __init__(self, routes: dict = None):
        """
        Framework class initialization function
        Pass server routes for accessing them later
        :param routes: server routes
        """
        self.routes = routes if routes else {'/': DefaultIndex()}

    def __call__(self, environ, start_response):
        """

        :param environ: a WSGI environment
        :param start_response: a callable accepting a status code,
            a list of headers, and an optional exception context to
            start the response
        :return:
        """
        code, body = self._get_view(environ['PATH'])
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
            view = lambda: ('404 Not Found', 'Page not found!')
        return view()
