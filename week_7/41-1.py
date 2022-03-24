from datetime import datetime


class Saving:
    def __init__(self, created_at: datetime, amount: float):
        self._amount = amount
        self._created_at = created_at

    @property
    def created_at(self):
        return self._created_at

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if amount > 0:
            self._amount = amount


class Savings:
    def __init__(self):
        self.savings = []

    def add_saving(self, saving: Saving):
        self.savings.append(saving)

    @property
    def total(self):
        return sum([saving.amount for saving in self.savings])


s1 = Saving(datetime(2021, 2, 14), 100)
s2 = Saving(datetime(2021, 2, 15), 200)

savings = Savings()
savings.add_saving(s1)
savings.add_saving(s2)
print(savings.total)