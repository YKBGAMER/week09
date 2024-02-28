import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        self.book1 = Book('1', 'Sample Book 1', 'Author 1')
        self.book2 = Book('2', 'Sample Book 2', 'Author 2')
        self.book3 = Book('3', 'Sample Book 3', 'Author 3')
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)

    def test_add_book(self):
        self.manager.add_book(self.book3)
        self.assertIn(self.book3, self.manager.list_books())

    def test_remove_book(self):
        self.manager.remove_book('1')
        self.assertNotIn(self.book1, self.manager.list_books())

    def test_list_books(self):
        books = self.manager.list_books()
        self.assertEqual(len(books), 2)
        self.assertIn(self.book1, books)
        self.assertIn(self.book2, books)

    def test_add_duplicated_book(self):
        self.manager.add_book(self.book1)
        self.assertEqual(len(self.manager.list_books()), 2)

if __name__ == '__main__':
    unittest.main()
