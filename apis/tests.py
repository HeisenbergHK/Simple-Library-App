from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Author, Book


class AuthorTests(APITestCase):
    def test_create_author(self):
        data = {"name": "Author Name"}
        response = self.client.post("/api/v1/authors/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], data["name"])

    def test_read_author(self):
        author = Author.objects.create(name="Test Author")
        response = self.client.get(f"/api/v1/authors/{author.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], author.name)

    def test_update_author(self):
        author = Author.objects.create(name="Old Name")
        data = {"name": "Updated Name"}
        response = self.client.put(f"/api/v1/authors/{author.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], data["name"])

    def test_delete_author(self):
        author = Author.objects.create(name="Author to Delete")
        response = self.client.delete(f"/api/v1/authors/{author.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Try to fetch the deleted author
        response = self.client.get(f"/api/v1/authors/{author.id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class BookTests(APITestCase):
    def setUp(self):
        # Create an author to associate with the book
        self.author = Author.objects.create(name="Author Name")

    def test_create_book(self):
        data = {
            "title": "Book Title",
            "author_id": self.author.id,
            "available": True
        }
        response = self.client.post("/api/v1/books/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["available"], data["available"])
        self.assertEqual(response.data["author"]["name"], self.author.name)

    def test_read_book(self):
        book = Book.objects.create(
            title="Test Book", author=self.author, available=True
        )
        response = self.client.get(f"/api/v1/books/{book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], book.title)
        self.assertEqual(response.data["available"], book.available)
        self.assertEqual(response.data["author"]["name"], self.author.name)


    def test_update_book(self):
        book = Book.objects.create(
            title="Old Title", author=self.author, available=True
        )
        data = {
            "title": "Updated Title",
            "author_id": self.author.id,
            "available": False
        }
        response = self.client.put(f"/api/v1/books/{book.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["available"], data["available"])
        self.assertEqual(response.data["author"]["name"], self.author.name)

    def test_delete_book(self):
        book = Book.objects.create(
            title="Book to Delete", author=self.author, available=True
        )
        response = self.client.delete(f"/api/v1/books/{book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Try to fetch the deleted book
        response = self.client.get(f"/api/v1/books/{book.id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
