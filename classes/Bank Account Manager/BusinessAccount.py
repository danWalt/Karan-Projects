from Account import Account


class BusinessAccount(Account):

    def __init__(self, balance=0, withdraw_limit=100000, interest_rate=1.00,
                 deposit_limit=100000):
        super().__init__(balance, withdraw_limit, interest_rate, deposit_limit)

    def get_balance(self):
        return self._balance

    def get_withdraw_limit(self):
        return self._withdraw_limit

    def get_deposit_limit(self):
        return self._deposit_limit

    def get_interest_rate(self):
        return self._interest_rate

    def set_withdraw_limit(self, new_withdraw_limit):
        self._withdraw_limit = new_withdraw_limit

    def set_deposit_limit(self, new_deposit_limit):
        self._deposit_limit = new_deposit_limit

    def set_interest_rate(self, new_interest_rate):
        self._interest_rate = new_interest_rate

    def apply_interest(self):
        self._balance = self.get_balance() * self.get_interest_rate()

    def deposit(self, amount):
        if amount > self.get_deposit_limit():
            print(
                'Sorry, you can only deposit up to ' + self.get_deposit_limit())
        else:
            self._balance += amount

    def withdraw(self, amount):
        if amount > self.get_withdraw_limit():
            print('Sorry, you can only withdraw up to ' +
                  self.get_withdraw_limit())
        elif self.get_balance() - amount < 0:
            print('Sorry, insufficient funds')
        else:
            self._balance -= amount
