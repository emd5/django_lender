from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Book
from django.http.response import Http404


class TestBookModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test', email='test@example.com')
        self.user.set_password('hello')

        self.book = Book.objects.create(title='Huckleberry Finn', year='2013', author='Mark Twain', user=self.user)

    def test_book_titles(self):
        self.assertEqual(self.book.title, 'Huckleberry Finn')

    def test_book_author(self):
        self.assertEqual(self.book.author, 'Mark Twain')

    def test_book_year(self):
        self.assertEqual(self.book.year, '2013')

    def test_book_details(self):
        book = Book.objects.get(title='Huckleberry Finn')
        self.assertEqual(self.book.author, 'Mark Twain')


class TestBookViews(TestCase):
    def setUp(self):
        self.request = RequestFactory()

        self.user = User.objects.create(username='test', email='test@example.com')
        self.user.set_password('hello')

        self.book_one = Book.objects.create(title='Llama Drama', author='A llama who has drama', user=self.user)
        self.book_two = Book.objects.create(title='Curious George', author='A bad monkey', user=self.user)

        self.request.user = self.user

    def test_book_detail_view(self):
        from .views import books_detail_view
        request = self.request
        response = books_detail_view(request, f'{self.book_one.id}')
        # import pdb: pdb.set_trace()
        self.assertIn(b'Llama Drama', response.content)

    def test_book_detail_status(self):
        from .views import books_detail_view
        request = self.request
        response = books_detail_view(request, f'{self.book_one.id}')
        # import pdb: pdb.set_trace()
        self.assertEqual(200, response.status_code)

    def test_view_other_users_book_view_fails(self):
        from .views import books_detail_view
        request = self.request
        self.request.user = User.objects.create(username='test2', email='test2@example.com')
        self.request.user.set_password('hello')
        with self.assertRaises(Http404):
            books_detail_view(request, f'{self.book_one.id}')



