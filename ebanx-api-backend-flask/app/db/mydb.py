from ..models import Account
from ..utils.exceptions import NonExistingAccountException

class SingletonDB(type):
    _instance = None

    def __call__(cls):
        if cls._instance is None:
            cls._instance = super().__call__()
        return _instance


class CustomDatabase(metaclass = SingletonDB):
    '''
    This class is a singleton, so it should be the only DB instance across the program.

    The class is a "simulation" of a database, where you can create and delete objects
    of Account present int the 'models'
    '''
    _accounts = {}

    @classmethod
    def _withdraw(cls, **kwargs):
        '''
        Withdraw an amount in a given account.
        If the account doesn't exist, throws an
        NonExistingAccountException error
        '''
        origin = kwargs.get('origin')
        amount = int(kwargs.get('amount'))

        if not cls.has_account(origin):
            raise NonExistingAccountException(origin)

        account = cls._get_account(origin)
        account.balance = account.balance - amount

        return account

    @classmethod
    def _deposit(cls, **kwargs):
        '''
        Deposits an amount in a given account.
        If account doesn't exists, create one with amount as balance
        '''
        destination = kwargs.get('destination')
        amount = int(kwargs.get('amount'))

        if not cls.has_account(destination):
            cls._create_account(destination)

        account = cls._get_account(destination)
        account.balance = account.balance + amount

        return account

    @classmethod
    def _get_account(cls, account_id):
        '''
        Tries to get a valid account.
        '''
        return cls._accounts.get(account_id)

    @classmethod
    def _create_account(cls, account_id, amount = 0):
        '''
        Creates a new account with amount as balance.
        Default amount is 0
        '''
        cls._accounts[account_id] = Account(account_id, amount)

    @classmethod
    def has_account(cls, account_id):
        '''
        Check if account_id is associated with an account
        '''
        return cls._get_account(account_id) is not None

    @classmethod
    def event(cls, **kwargs):
        '''
        event handler method. This method handles:
        - withdrawn: remove an amount from an account
        - deposit: add an amount to an account
        - transfer: transfer an amount between origin and destiny
        '''
        event_type = kwargs.get('type')
        if event_type == 'deposit':
            changed_destination = cls._deposit(**kwargs)
            return {
                'destination': changed_destination.to_dict()
            }

        elif event_type == 'transfer':
            changed_origin = cls._withdraw(**kwargs)
            changed_destination = cls._deposit(**kwargs)

            return {
                'origin': changed_origin.to_dict(),
                'destination': changed_destination.to_dict()
            }

        elif event_type == 'withdraw':
            changed_origin = cls._withdraw(**kwargs)
            return {
                'origin': changed_origin.to_dict()
            }


    @classmethod
    def balance(cls, account_id):
        '''
        Method to return the balance of a given account
        '''
        if not cls.has_account(account_id):
            raise NonExistingAccountException(account_id)
        return cls._get_account(account_id).balance

    @classmethod
    def reset(cls):
        '''
        Resets the Database
        '''
        cls._accounts.clear()
