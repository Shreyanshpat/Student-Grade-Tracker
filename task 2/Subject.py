from enum import Enum


class Subject:
    def __init__(self, name: str, credit_hrs: int):
        self._name = name
        self._credit_hrs = credit_hrs

    def get_credit_hours(self):
        return self._credit_hrs

    def __repr__(self):
        return f"{self._name} : {self._credit_hrs} hours"