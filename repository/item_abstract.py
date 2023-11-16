import abc 
from model import item_model

class ItemAbstract(abc.ABC):
    @abc.abstractmethod
    def add(self, item:item_model.Item):
        raise NotImplementedError
    
    
   