from views import Index, Contact, Categories, CreateCategory

routes = {
    '/': Index(),
    '/contact/': Contact(),
    '/categories/': Categories(),
    '/create-category/': CreateCategory()
}
