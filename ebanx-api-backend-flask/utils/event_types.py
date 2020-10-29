from enum import Enum

class EventType(Enum):
    '''
    Enum to hold all possible EventTypes
    '''
    DEPOSIT =  1
    WITHDRAW = 2
    TRANSFER = 3
