import datetime 
from typing import Tuple
from core.store import Store


class Core():

    def __init__(self, store : Store):
        self.store = store

    def save(self, text : str):
        self.store.record_save(text)

    def get_record_dates(self) -> Tuple:
        record_dates = self.store.get_record_dates()
        return record_dates
    
    def get_date_records(self, date: datetime.date) -> Tuple:
        rows = self.store.get_date_records(date)
        return rows