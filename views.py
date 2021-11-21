from wunderbar.templating import render


class Index:
    """Index view"""

    def __call__(self, request):
        return '200 OK', render('index.html')


class Contact:
    """Contact view"""

    def __call__(self, request):
        return '200 OK', render('contact.html')
