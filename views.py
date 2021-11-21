from patterns.creational_patterns import Engine
from wunderbar.templating import render

site = Engine()


class Index:
    """Index view"""

    def __call__(self, request):
        return '200 OK', render('index.html')


class Contact:
    """Contact view"""

    def __call__(self, request):
        return '200 OK', render('contact.html')


class Categories:
    """Categories view"""

    def __call__(self, request):
        return '200 OK', render('categories.html', objects_list=site.categories)


class CreateCategory:
    """Category creation view"""

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category = None
            if category_id := data.get('category_id'):
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)
            site.categories.add(new_category)

            return '200 OK', render('categories.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('create-category.html', categories=categories)


class Courses:
    """Courses view"""

    def __call__(self, request):
        return '200 OK', render('courses.html', objects_list=site.courses)


class CategoryCourses:
    """Category courses view"""

    def __call__(self, request):
        try:
            category = site.find_category_by_id(int(request['request_params']['id']))
            return '200 OK', render('category-courses.html', objects_list=category.courses, name=category.name,
                                    id=category.id)
        except KeyError:
            return '200 OK', 'No courses have been added yet'

