from weakref import WeakKeyDictionary

class Event:
    def __init__(self, name: str, data: dict = None) -> object:
        self.name = name
        self.data = data

    def getData(self) -> dict:
        return self.data

    def getName(self) -> str:
        return self.name

class CounterWeakDictionary(WeakKeyDictionary):
    def __init__(self):
        super().__init__()
        self.counter = 0

    def push(self, function):
        self[self.counter] = function
        self.counter += 1

    def delete(self, func):
        #TODO: Implement
        pass


class EventManager:
    def __init__(self):
        self.listeners = {}

    def add_listener(self, event_type, ):
        '''
        :param event_type: int. Unique identifier of a type
        :return: None
        
        When adding a listener, this method takes care of creating a creating a reference in the dict above and adding 
        the listener object to it.
        '''

        if self.listeners.get(event_type, False):
            self.listeners[event_type]
        else:
            self.listeners[event_type] = CounterWeakDictionary()