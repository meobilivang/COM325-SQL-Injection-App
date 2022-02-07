import re
from calendar import c

from flask import Flask
from rich import print

from db import get_cards, get_cards_safe, get_user, get_user_safe

app = Flask(__name__)


def print_input(input):
    print(f"[bold]{'-' * 50}[/bold]")
    print(f"[bold]Passing input:[/bold] [yellow]{input}[/yellow]")


@app.route("/")
def index():
    return f"""
        <html lang="en">
            <head>
                <title>SQL Injection Lab - Julian Nguyen</title>
            </head>
            <body style="text-align: center">
                <h1>Hi COM325, hit <a href="/home">this link</a> to begin our lab 👋.</h1>
                <p>
                    <b>Note</b>: Please follow my instructions! Try not to modify the code for now.
                </p>
                <h2>Please follow my Documentation <a href="">HERE</a> for detailed instructions</h2>
            </body>
        </html>
    """


@app.route("/home")
def home():
    return f"""
        <html lang="en">
            <body style="text-align: center">
                <h1>Press here to view My Profile:</h1>
                <h2>👉<a href="/users/4395">My Profile</a>👈.</h2>
                <p>No worries, this link is totally safe 🌚</p>
            </body>
        </html>
    """


@app.route("/users/<camel_id>")
def view_user_profile(camel_id: str):
    print_input(camel_id)

    user_info = get_user(camel_id)

    output = [
        f"""
                <li>
                    <b>ID</b>: {id} |
                    <b>Camel ID</b>: {camel_id} |
                    <b>Name</b>: {name} |
                    <b>SSN</b>: {ssn} |
                    <b>Balance</b>: {balance} |
                    <b>Email</b>: {email} |
                    <b>Birth Date</b>: {birth_date} |
                    <b>Phone Number</b>: {phone_number} |
                </li>
                """
        for id, camel_id, name, ssn, balance, email, birth_date, phone_number in user_info
    ]

    # Just joking, don't mind this
    message = (
        "<h3>Oh you are doing something very very naughty 🌚</h3>"
        if (len(user_info) > 1)
        else ""
    )

    disclaimer = f"""
        <p>Personal Profile of User:
            <pre><blockquote>{camel_id}</blockquote></pre>
        </p>
    """
    return f'<br/><p>👉<a href="/users/cards/4395">My Card(s)</a>👈.</p>{disclaimer}{message}<br/><h3>Results</h3><ol>{"".join(output)}</ol>'


@app.route("/users/cards/<camel_id>")
def view_user_cards(camel_id: str):
    print_input(camel_id)

    cards_info = get_cards(camel_id)

    message = (
        "<h3>Nooo stop doing these naughty stuffs 🌚</h3>"
        if (not camel_id.isnumeric())
        else ""
    )

    output = [
        f"""
                <li>
                    <b>Card Number</b>: {card_num} |
                    <b>CVV</b>: {cvv} |
                </li>
                """
        for card_num, cvv in cards_info
    ]

    disclaimer = f"""
        <p>Card Collection of User:
            <pre><blockquote>{camel_id}</blockquote></pre>
        </p>
    """
    return f'<br/><p>👉<a href="/safe/users/4395">My Profile</a>👈.{disclaimer}{message}<br/><h3>Results</h3><ol>{"".join(output)}</ol>'


##### IMPLEMENTING SAFE METHODS ##########


def sanitize_input(input: str) -> str:
    """Sanitize input by replacing sensitive characters with empty string

    Args:
        raw_input (str)
    """
    BLANK = ""

    input = input.replace("'", BLANK).replace("--", BLANK).replace(";", BLANK)

    print(f"[bold]{'-' * 50}[/bold]")
    print(f"[bold]SANITIZE:[/bold] [yellow]{input}[/yellow]")

    return input


def sanitize_input_re(input: str) -> str:
    """Sanitize input with Regular Expression

    Args:
        raw_input (str)
    """

    # Accepts only Normal Character. Replace Special Characters by a BLANK
    input = re.sub("[^a-zA-Z0-9 \n\.]", "", input)

    print(f"[bold]{'-' * 50}[/bold]")
    print(f"[bold]SANITIZE:[/bold] [yellow]{input}[/yellow]")

    return input


@app.route("/safe/users/<camel_id>")
def view_user_profile_safe(camel_id: str):
    print_input(camel_id)

    # Safe: sanitize input
    camel_id = sanitize_input(camel_id)

    user_info = get_user(camel_id)

    # Safe: implementing User Input Parameterization
    # user_info = get_user_safe(camel_id)

    output = [
        f"""
                <li>
                    <b>ID</b>: {id} |
                    <b>Camel ID</b>: {camel_id} |
                    <b>Name</b>: {name} |
                    <b>SSN</b>: {ssn} |
                    <b>Balance</b>: {balance} |
                    <b>Email</b>: {email} |
                    <b>Birth Date</b>: {birth_date} |
                    <b>Phone Number</b>: {phone_number} |
                </li>
                """
        for id, camel_id, name, ssn, balance, email, birth_date, phone_number in user_info
    ]

    # Just joking, don't mind this
    message = (
        "<h3>Oh you are doing something very very naughty 🌚</h3>"
        if (len(user_info) > 1)
        else ""
    )

    disclaimer = f"""
        <p>Personal Profile of User:
            <pre><blockquote>{camel_id}</blockquote></pre>
        </p>
    """

    return f'<br/><p>👉<a href="/safe/users/cards/4395">My Card(s)</a>👈.</p>{disclaimer}{message}<br/><h3>Results</h3><ol>{"".join(output)}</ol>'


@app.route("/safe/users/cards/<camel_id>")
def view_user_cards_safe(camel_id: str):
    print_input(camel_id)

    # Safe: Sanitize input
    camel_id = sanitize_input(camel_id)

    cards_info = get_cards(camel_id)

    # Safe: implementing User Input Parameterization
    # cards_info = get_cards_safe(camel_id)

    message = (
        "<h3>Nooo stop doing these naughty stuffs 🌚</h3>"
        if (not camel_id.isnumeric())
        else ""
    )

    output = [
        f"""
                <li>
                    <b>Card Number</b>: {card_num} |
                    <b>CVV</b>: {cvv} |
                </li>
                """
        for card_num, cvv in cards_info
    ]

    disclaimer = f"""
        <p>Card Collection of User:
            <pre><blockquote>{camel_id}</blockquote></pre>
        </p>
    """
    return f'<br/><p>👉<a href="/safe/users/4395">My Profile</a>👈.{disclaimer}{message}<br/><h3>Results</h3><ol>{"".join(output)}</ol>'
