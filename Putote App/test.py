
from app import app
import unittest

class APITest(unittest.TestCase):

    def test_get_word(self):
        tester = app.test_client(self)
        responce = tester.get('/get_word')
        status_code = responce.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(responce.data.decode(), "TEST")
        print(responce.get_data().decode())

    def test_admin_post(self):
        tester = app.test_client(self)
        response = tester.get('/admin')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        response_data = response.get_data(as_text=True)
        self.assertIn("Admin Portal", response_data)




if __name__ == '__main__':
    unittest.main()
