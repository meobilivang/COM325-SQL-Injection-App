from flask import Flask
from rich import print

from db import get_user

app = Flask(__name__)


@app.route("/")
def index():
    return (
        "Hi 👋 head out to "
        '<a href="/home">this link</a> to get started.'
    )

@app.route("/home")
def home():
    return (
        "<h1>Press here to view your profile:</h1>"
        '<a href="/users/4395">this link</a> to get started.'
    )

@app.route("/users/<camel_id>")
def view_user_profile(camel_id: str):
    print(f"[bold]{'-' * 50}[/bold]")
    print(f"[bold]Passing input:[/bold] [yellow]{camel_id}[/yellow]")

    user_info = get_user(camel_id)
    
    output = [f"""
                <li>
                    <b>ID</b>: {id} |
                    <b>Camel ID</b>: {camel_id} |
                    <b>Name</b>: {name} |
                    <b>SSN</b>: {ssn} |
                    <b>Balance</b>: {balance} |
                    <b>email</b>: {email} |
                    <b>Birth Date</b>: {birth_date} |
                    <b>Phone Number</b>: {phone_number} |
                </li>
                """ for id, camel_id, name, ssn, balance, email, birth_date, phone_number in user_info]

    disclaimer = f"""
        <p>Personal Profile of User:
            <pre><blockquote>{camel_id}</blockquote></pre>
        </p>
    """
    return f"{disclaimer}<br/><h3>Results</h3><ol>{''.join(output)}</ol>"
