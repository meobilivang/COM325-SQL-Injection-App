from dataclasses import dataclass


@dataclass
class User:
    id: int
    camel_id: str
    name: str
    email: str
    ssn: str
    balance: int
    birth_date: str
    phone_number: str


@dataclass
class Card:
    id: int
    camel_id: str
    card_num: str
    cvv: int
    exp_date: str
