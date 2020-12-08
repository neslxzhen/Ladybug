from abc import abstractmethod,ABC

class API(ABC):
    def __init__(self):
        return

    @abstractmethod
    def get_tokens(self)->dict:
        return NotImplemented

    def get_code(self):
        return input('Paste the authentication Code here:')
