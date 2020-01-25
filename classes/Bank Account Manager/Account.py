from abc import ABC
from abc import abstractmethod


class Account(ABC):

    def __init__(self, balance, withdraw_limit, interest_rate, deposit_limit):
        self._balance = balance
        self._withdraw_limit = withdraw_limit
        self._interest_rate = interest_rate
        self._deposit_limit = deposit_limit
