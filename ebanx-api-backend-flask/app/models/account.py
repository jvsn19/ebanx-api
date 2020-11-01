class Account:
    '''
    Class Account definition. It's a model for our system, where works as an money account.
    '''
    def __init__(self, id, balance = 0):
        self.id = id
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    def to_dict(self):
        return {"id": str(self.id), "balance": str(self._balance)}
