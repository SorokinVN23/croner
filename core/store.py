import abc
import datetime

from typing import Tuple

class Store(abc.ABC):

    @abc.abstractmethod
    def record_save(self, text : str):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_record_dates(self, limit : int = 30) -> Tuple:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_date_records(self, date : datetime.date) -> Tuple:
        raise NotImplementedError