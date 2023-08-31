import unittest
from mock import Mock, patch
# from ...calculator_app.account_app import Account
from calculator_app.account_app import Account
from calculator_app.account_app import ConnectionError
class TestAccount(unittest.TestCase):
    def setUp(self):
        self.mock_di = Mock()
        self.account = Account(self.mock_di)

    def test_account_returns_data_for_id_1(self):
        account_data = {"id": 1, "name": "test"}
        self.mock_di.get.return_value = account_data
        self.assertDictEqual(account_data, self.account.get_account(1))

    def test_account_when_connection_error_occurs(self):
        self.mock_di.get.side_effect = ConnectionError()
        self.assertEqual(
            "Connection error occurred. Try Again.",
            self.account.get_account(1)
        )

    @patch("calculator_app.account_app.requests")
    def test_get_current_balance(self, mock_requests):
        self.mock_di.status_code = 200
        self.mock_di.text = "Some text data"
        mock_requests.get.return_value = self.mock_di
        self.assertEqual({"status": 200, "data": "Some text data"}, self.account.get_current_balance(1))


if __name__ == '__main__':
    unittest.main()