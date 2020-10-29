class Account:
    '''
    Class Account definition. It's a model for our system, where works as an money account.
    '''
    def __init__(self, id):
        self.id = id
        self._amount = 0

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        self._amount = new_amount
