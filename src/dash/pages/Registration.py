import requests

import dash
from dash import Input, Output, State, callback, dcc, html

dash.register_page(__name__, path="/sign-up")

layout = html.Div(
    [
        html.H1(
            "ElderlySafety",
            style={
                "text-align": "center",
                "font-size": "48px",
                "font-weight": "bold",
                "text-shadow": "2px 2px 2px #333",
                "margin-bottom": "20px",
            },
        ),
        html.Label("Username:", style={"font-size": "24px", "display": "block"}),
        dcc.Input(
            id="username-sign-up",
            type="text",
            style={
                "width": "300px",
                "margin-bottom": "20px",
                "font-size": "18px",
            },
        ),
        html.Label("Full Name:", style={"font-size": "24px", "display": "block"}),
        dcc.Input(
            id="fullname-sign-up",
            type="text",
            style={
                "width": "300px",
                "margin-bottom": "20px",
                "font-size": "18px",
            },
        ),
        html.Label("Password:", style={"font-size": "24px", "display": "block"}),
        dcc.Input(
            id="password-sign-up",
            type="password",
            style={
                "width": "300px",
                "margin-bottom": "20px",
                "font-size": "18px",
            },
        ),
        html.Button(
            "Sign up",
            id="submit-sign-up",
            n_clicks=0,
            style={
                "margin-bottom": "10px",
                "font-weight": "bold",
                "background-color": "#008080",
                "color": "white",
                "font-size": "24px",
                "border-radius": "10px",
                "width": "300px",
            },
        ),
        dcc.Link(
            "Back to Sign in",
            href="/sign-in",
            style={
                "text-decoration": "underline",
                "color": "blue",
                "font-size": "18px",
                "margin-top": "20px",
                "width": "300px",
                "display": "inline-block",
            },
        ),
        html.Div(id="output-sign-up", style={"text-align": "center"}),
    ],
    style={
        "width": "400px",
        "margin": "auto",
        "text-align": "center",
        "margin-top": "20px",
    },
)


@callback(
    Output("output-sign-up", "children"),
    [Input("submit-sign-up", "n_clicks")],
    [
        State("username-sign-up", "value"),
        State("fullname-sign-up", "value"),
        State("password-sign-up", "value"),
    ],
)
def sign_up(n_clicks, username, fullname, password):
    if n_clicks > 0:
        if username is None:
            return "Type the username", None
        if fullname is None:
            return "Type the fullname", None
        if password is None:
            return "Type the password", None
        url = "http://localhost:8000/sign-up"
        data = {"username": username, "fullname": fullname, "password": password}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return "Successfully signed up! You need to sign in now."
        else:
            return f"Registration failed: {response.status_code}"
    else:
        return
