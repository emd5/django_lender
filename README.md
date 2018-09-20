# Django Lender
Set up a Docker container & first Django Lender Book Library sApplication! 

## API
Using python 3.7 scripting language with Django Framework and Docker 

### Changelog
=====

##### 2018-09-19

- [x] update views with authentication logic
- [x] update setup.py configurations to work with django_registration
- [x] update model with appropriate users and books
- [x] update testing with new test cases
- [x] included django registration templates for account registration, login/logout features
- [x] update base.html with new URLs




##### 2018-09-18
- [x] Modify the contents of the templates/ directory to include a base.html and home.html
- [x] Create a simple view controller for the home route, which renders the home.html document
- [x] Create a new app inside your project called lender_books
- [x] Add a new app to the settings.py, and configure the urls for this new app at the root level of the project
- [x] Working in the lender-books/ directory:
    - [x] Create a new model for Book, which represents an item that will be lent to another person, with the following
        attributes cover_image: An image field
    - [x] title: Text field
    - [x] author: Text field
    - [x] year: Multiple choice field for year published
    - [x] status: Multiple choice field for available or checked-out statuses
    - [x] date_added: Auto-generated date field
    - [x] last_borrowed: Auto-updated date field
- [x] Create a new template called book_list.html that inherits from base.html, which will render out a list of all books in the system for the current user
- [x] Create a new template called book_detail.html that inherits from base.html, which will render out the detail for a single book
- [x] Create a simple view controller for each of the templates defined above
- [x] Create a urls.py for this app, which connects your view controllers and their templates to your application at an appropriate route

##### 2018-09-17
- [x] Initial setup with Django and Docker




