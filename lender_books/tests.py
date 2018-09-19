from django.test import TestCase, RequestFactory
from .models import Book


class TestBookModel(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title='Happy Feet', author='Penguin')
        Book.objects.create(title='Lego', author='build a world')
        Book.objects.create(title='Huckleberry Finn', author='WTF')

    def test_book_titles(self):
        self.assertEqual(self.book.title, 'Happy Feet')

    def test_book_details(self):
        book = Book.objects.get(title='Happy Feet')

        self.assertEqual(book.author, 'Penguin')


class TestBookViews(TestCase):
    def setUp(self):
        self.request = RequestFactory()
        self.book_one = Book.objects.create(title='Llama Drama', author='A llama who has drama')
        self.book_two = Book.objects.create(title='Curious George', author='A bad monkey')

    def test_book_detail_view(self):
        from .views import books_detail_view
        request = self.request.get('')
        response = books_detail_view(request, f'{self.book_one.id}')
        # import pdb: pdb.set_trace()
        self.assertIn(b'Llama Drama', response.content)

    def test_book_detail_status(self):
        from .views import books_detail_view
        request = self.request.get('')
        response = books_detail_view(request, f'{self.book_one.id}')
        # import pdb: pdb.set_trace()
        self.assertEqual(200, response.status_code)

