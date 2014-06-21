# -*- coding: utf-8 -*-


import bouquet
import unittest


class BouquetTestCase(unittest.TestCase):

    def setUp(self):
        self.app = bouquet.app.test_client()

    def test_post_compliment(self):
        resp = self.app.post('/compliment', data={'sex': 'male', 'lang': 'ru', 'text': 'Ты самый лучший!'})
        assert 'Ты самый лучший!' in resp.data

    def test_get_compliments(self):
        self.app.post('/compliment', data={'sex': 'male', 'lang': 'ru', 'text': 'Ты самый лучший!'})
        self.app.post('/compliment', data={'sex': 'female', 'lang': 'ru', 'text': 'Ты самая лучшая!'})

        resp = self.app.get('/compliment')
        assert 'Ты самый лучший!' in resp.data
        assert 'Ты самая лучшая!' in resp.data

    def test_delete_compliment(self):
        self.app.post('/compliment', data={'sex': 'male', 'lang': 'ru', 'text': 'Ты самый лучший!'})
        self.app.delete('/compliment/1')

        resp = self.app.get('/compliment')
        assert 'Ты самый лучший!' not in resp.data

    def test_put_compliment(self):
        self.app.post('/compliment', data={'sex': 'male', 'lang': 'ru', 'text': 'Ты самый лучший!'})
        self.app.put('/compliment/1', data={'sex': 'female', 'lang': 'ru', 'text': 'Ты самая лучшая!'})

        resp = self.app.get('/compliment')
        assert 'Ты самый лучший!' not in resp.data
        assert 'Ты самая лучшая!' in resp.data


if __name__ == '__main__':
    unittest.main()
