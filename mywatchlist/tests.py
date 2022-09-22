from django.test import TestCase, LiveServerTestCase
from django.urls import resolve, reverse
from django.test import Client

class MyWatchListTest(TestCase): 
    def test_urlHTML_is_exist(self):
        response = Client().get('/mywatchlist/html')
        self.assertEqual(response.status_code, 200)

    def test_urlJson_is_exist(self):
        response = Client().get('/mywatchlist/json')
        self.assertEqual(response.status_code, 200)

    def test_urlXML_is_exist(self):
        response = Client().get('/mywatchlist/xml')
        self.assertEqual(response.status_code, 200)
