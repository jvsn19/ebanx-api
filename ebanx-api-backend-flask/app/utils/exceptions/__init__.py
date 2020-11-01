class NonExistingAccountException(Exception):
    def __init__(self, account_id):
        super().__init__(f'The account {account_id} doesn\'t exist.')
