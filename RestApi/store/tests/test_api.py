from pprint import pprint

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Book
from store.serializers import BookSerializers





class BookApiTestCase(APITestCase):
    def test_get(self):
        url =  'http://127.0.0.1:8000/api/v1/book/'
        # url = reverse('book-list')
        response = self.client.get(url)
        book_1 = Book.objects.create(name='NewTestBook',price=115.15,author = 'NewTestAuthor')
        book_2 = Book.objects.create(name='NewTestBook2',price=115.15,author='NewTestAuthor2')
        book_3 = Book.objects.create(name='NewTestBook3', price=115.15, author='Author3')
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BookSerializers([book_1,book_2,book_3], many=True)
        # print(serializer_data.data)
        # print(response.data == serializer_data.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data.data, response.data)

    def test_get_search(self):
        book_1 = Book.objects.create(name='NewTestBook', price=115.15, author='Author1')
        book_2 = Book.objects.create(name='NewTestBook2',price=115.15,author='Author2')
        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'Author1'})
        serializer_data = BookSerializers(book_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, dict(response.data[0]))


    def test_get_ordering(self):
        # book_1 = Book.objects.create(name='NewTestBook', price=115.15, author='Author1')
        # book_2 = Book.objects.create(name='NewTestBook2', price=115.15, author='Author2')
        # book_3 = Book.objects.create(name='NewTestBook3', price=115.15, author='Author3')
        self.setUp()
        url = reverse('book-list')
        response = self.client.get(url, data={'ordering': 'price'})
        serializer_data = BookSerializers(self.setUp(), many=True).data
        # pprint(serializer_data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data,response.data)







