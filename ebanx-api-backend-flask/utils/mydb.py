from ..models import Account
from .event_types import EventType

class SingletonDB(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return _instance


class DB(metaclass = SingletonDB):
    '''
    This class is a singleton, so it should be the only DB instance across the program.

    The class is a "simulation" of a database, where you can create and delete objects
    of Account present int the 'models'
    '''
    _accounts = {}

    # Private Methods
    def _withdraw(self, **kwargs):
        pass

    def _deposit(self, **kwargs):
        pass

    @classmethod
    def _get_account(cls, account_id):
        '''
        Tries to get a valid account. If there is no account, create one
        with amount = 0
        '''
        if account_id not in cls._accounts:
            cls._accounts[account_id] = Account(account_id)
        return cls._accounts[account_id]

     # Public Methods
    @classmethod
    def event(cls, event_type, **kwargs):
        pass

    @classmethod
    def balance(cls, **kwargs):
        pass

    @classmethod
    def reset(cls):
        '''
        Resets the Database
        '''
        cls._accounts.clear()
