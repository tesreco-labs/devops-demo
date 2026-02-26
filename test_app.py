import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

# add test for divide endpoint with division by zero error handled by telling the user that division by zero is not allowed instead of returning a 500 error
    def test_divide_by_zero_handled(self):
        response = self.client.get("/divide/10/0")
        self.assertEqual(response.status_code, 400)  # Expecting a bad request error for division by zero
        self.assertIn("Division by zero is not allowed", response.json["error"])

# add test for divide endpoint with valid input
    def test_divide_valid_input(self):
        response = self.client.get("/divide/10/2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], 5)

if __name__ == "__main__":
    unittest.main()

# import importlib
# def test_import_app():
#     """Simple smoke test that the `app` module imports successfully."""
#     mod = importlib.import_module("app")
#     assert mod is not None