from db import connection_context
from models import User

CREATE_TABLE_USER = """
CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY,
    camel_id varchar(5) UNIQUE NOT NULL,
    name varchar(64) UNIQUE NOT NULL,
    ssn varchar(12) UNIQUE NOT NULL,
    balance integer UNIQUE DEFAULT(0),
    email varchar(100) UNIQUE NOT NULL,
    birth_date varchar(12) NOT NULL,
    phone_number varchar(20) NOT NULL
);
"""

CLEAR_TABLE_CHALLENGE = "DELETE FROM challenges"

USER_DATA = [
    User(1, camel_id="4395", email="pnguyen@conncoll.edu", name="Phong Nguyen", balance=10, ssn="909-03-4642", birth_date="16-09-2001",phone_number="860-514-8412"),
    User(2, camel_id="3048", email="jdoe@conncoll.edu", name="John Doe", balance=20, ssn="757-85-7495", birth_date="01-04-2002", phone_number="860-485-1242"),
    User(3, camel_id="1062", email="jschaeffer@conncoll.edu", name="John Schaeffer", balance=1000, ssn="778-62-8144", birth_date="25-08-1970", phone_number="860-234-7261"),
]

MIN_CHALLENGES_PER_USER = 2
MAX_CHALLENGES_PER_USER = 6


def start_database():
    with connection_context() as cur:
        cur.execute(CREATE_TABLE_USER)

        for user in USER_DATA:
            insert_cmd = f"""
                INSERT INTO users (id, camel_id, name, ssn, balance, email, birth_date, phone_number)
                VALUES (
                    '{user.id}',
                    '{user.camel_id}',
                    '{user.name}',
                    '{user.ssn}',
                    '{user.balance}',
                    '{user.email}',
                    '{user.birth_date}',
                    '{user.phone_number}'
                )
                ON CONFLICT DO NOTHING
            """
            cur.execute(insert_cmd)
