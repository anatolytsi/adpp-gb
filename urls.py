from views import Index, Contact, Categories, CreateCategory, Courses

routes = {
    '/': Index(),
    '/contact/': Contact(),
    '/categories/': Categories(),
    '/create-category/': CreateCategory(),
    '/courses/': Courses(),
    # '/create-category/': CreateCategory()
}
