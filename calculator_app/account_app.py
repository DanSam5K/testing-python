import requests

class ConnectionError(Exception):
    pass


class Account(object):
    def __init__(self, data_interface):
        self.di = data_interface

    def get_account(self, account_id):
        try:
            result = self.di.get(account_id)
        except ConnectionError:
            result = "Connection error occurred. Try Again."
        return result

    def get_current_balance(self, account_id):
        response = requests.get(f"http://some-account-uri/{account_id}")
        return {"status": response.status_code, "data": response.text}
