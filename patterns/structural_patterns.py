from time import process_time as time

from .creational_patterns import Logger

logger = Logger('main')


def route(routes: dict, url: str):
    def wrapper(cls):
        routes[url] = cls()

    return wrapper


def method_debug(method):
    def wrapper(cls, *args, **kwargs):
        t = time()
        result = method(cls, *args, **kwargs)
        delta = time() - t
        logger.debug(f'Call of method "{method.__name__}" of class "{cls.__class__.__name__}" took {delta} s')
        return result

    return wrapper
