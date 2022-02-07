import contextlib
import logging
import os
import sqlite3
from typing import Any, List

from rich import print

logger = logging.getLogger(__name__)

DB_FILENAME = os.path.realpath("data/test.db")


def _get_connection() -> sqlite3.Connection:
    try:
        conn = sqlite3.connect(DB_FILENAME)
    except sqlite3.Error:
        logger.exception("Unable to connect to Database")
        raise
    else:
        return conn


@contextlib.contextmanager
def connection_context():
    conn = _get_connection()
    cur = conn.cursor()

    yield cur

    conn.commit()
    cur.close()
    conn.close()


def print_query_terminal(query):
    print("-" * 50)
    print(f"[bold]Executing query:[/bold] [bold green blink]{query}[/bold green blink]")
    print(f"[bold]{'-' * 50}[/bold]")


def get_user(camel_id: str) -> List[Any]:
    """Unsafe function retrieving Users

    Args:
        camel_id (str)
    """
    query = f"""
        SELECT
            id, camel_id, name, ssn, balance, email, birth_date, phone_number
        FROM users
        WHERE
            camel_id='{camel_id}';
    """

    print_query_terminal(query)

    with connection_context() as cur:
        cur.execute(query)
        results = cur.fetchall()

        return results


def get_cards(camel_id: str) -> List[Any]:
    """Unsafe function retrieving Cards

    Args:
        camel_id (str)
    """
    query = f"""
        SELECT
            card_num, cvv
        FROM cards c
        JOIN users u
        WHERE
            u.camel_id='{camel_id}';
    """

    print_query_terminal(query)

    with connection_context() as cur:
        cur.execute(query)
        results = cur.fetchall()

        return results


##### IMPLEMENTING SAFE METHODS #####


def get_user_safe(camel_id: str) -> List[Any]:
    """Safe Method for Querying User data.
        User Input is PARAMETERIZE => Passing as ARGUMENTS

    Args:
        camel_id (str)
    """
    query = f"""
        SELECT
            id, camel_id, name, ssn, balance, email, birth_date, phone_number
        FROM users
        WHERE
            camel_id=?;
    """

    print_query_terminal(query)

    with connection_context() as cur:
        cur.execute(query, (camel_id,))
        results = cur.fetchall()

        return results


def get_cards_safe(camel_id: str) -> List[Any]:
    """Safe Method for Querying Card data.
        User Input is PARAMETERIZE => Passing as ARGUMENTS

    Args:
        camel_id (str)
    """
    query = f"""
        SELECT
            card_num, cvv
        FROM cards c
        JOIN users u
        WHERE
            u.camel_id=?;
    """

    print_query_terminal(query)

    with connection_context() as cur:
        cur.execute(query, (camel_id,))
        results = cur.fetchall()

        return results
