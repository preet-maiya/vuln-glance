import unittest
from restserver import app as flask_app

class MyTestCase(unittest.TestCase):

    def setUp(self):
        flask_app.testing = True
        self.app = flask_app.test_client()

    def test_home(self):
        result = self.app.get('/recentcves')
        self.assertEqual(result.status, '200 OK')
    
    #def test_get_leaks_base(self):
    #    result = self.app.get('/recentcves')
    #    resp = json.loads(result.data)
    #    checks = []
    #    for leak in resp:
    #        checks.append(all(True for key in config.resp_fields if key in leak.keys()))
    #    self.assertTrue(all(checks))


if __name__ == '__main__':
    unittest.main()
