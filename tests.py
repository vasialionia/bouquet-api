import bouquet
import unittest


class BouquetTestCase(unittest.TestCase):

    def setUp(self):
        self.app = bouquet.app.test_client()

    def test_index(self):
        resp = self.app.get('/')
        assert resp.status_code == 200
        assert 'Hello World!' in resp.data


if __name__ == '__main__':
    unittest.main()
