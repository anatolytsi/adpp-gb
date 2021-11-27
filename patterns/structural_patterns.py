def route(routes: dict, url: str):
    def wrapper(cls):
        routes[url] = cls()

    return wrapper
