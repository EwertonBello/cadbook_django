import json

from rest_framework.test import APITestCase

from book.tests.factories import BookFactory


class BookListCreateAPIViewTestCase(APITestCase):
    
    @property
    def list_response(self):
        return self.client.get("/api/v1/books/")

    def test_status_code(self):
        """
        Test to verify if status_code is 200
        """
        assert self.list_response.status_code == 200

    def test_return_by_length(self):
        """
        Test to verify length of return
        """
        BookFactory(title="Test1")
        BookFactory(title="Test2")

        self.assertEqual(len(json.loads(self.list_response.content)), 2)


class BookDetailAPIViewTestCase(APITestCase):
    
    @property
    def detail_response(self):
        return self.client.get("/api/v1/books/", kwargs={"book_id":1})

    def test_status_code(self):
        """
        Test to verify if status_code is 200
        """
        assert self.detail_response.status_code == 200

    def test_return_by_length(self):
        """
        Test to verify length of details book return
        Details:
            id
            title
            user(id, name, email)
            price
            pages
        """
        BookFactory(title="Test1")

        self.assertEqual(len(json.loads(self.detail_response.content)[0]), 5)
