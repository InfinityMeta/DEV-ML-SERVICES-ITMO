import requests

import dash
from dash import Input, Output, State, callback, dcc, html

dash.register_page(__name__, path="/sign-in")

layout = html.Div(
    [
        html.H1(
            "ElderlySafety",
            style={
                "font-size": "48px",
                "font-weight": "bold",
                "text-shadow": "2px 2px 2px #333",
                "margin-bottom": "20px",
            },
        ),
        html.Label("Username:", style={"font-size": "24px", "display": "block"}),
        dcc.Input(
            id="username-sign-in",
            type="text",
            style={
                "width": "300px",
                "margin-bottom": "20px",
                "font-size": "18px",
            },
        ),
        html.Label("Password:", style={"font-size": "24px", "display": "block"}),
        dcc.Input(
            id="password-sign-in",
            type="password",
            style={
                "width": "300px",
                "margin-bottom": "20px",
                "font-size": "18px",
            },
        ),
        html.Button(
            "Sign in",
            id="submit-sign-in",
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
            "Not signed up yet?",
            href="/sign-up",
            style={
                "text-decoration": "underline",
                "color": "blue",
                "font-size": "18px",
                "margin-top": "20px",
                "width": "300px",
                "display": "inline-block",
            },
        ),
        html.Div(
            id="redirect-to-predict",
            style={"text-align": "center", "font-size": "20px"},
        ),
        dcc.Store(id="token", storage_type="session"),
    ],
    style={
        "width": "400px",
        "margin": "auto",
        "text-align": "center",
        "margin-top": "20px",
    },
)


@callback(
    Output("redirect-to-predict", "children"),
    Output("token", "data"),
    [Input("submit-sign-in", "n_clicks")],
    [State("username-sign-in", "value"), State("password-sign-in", "value")],
)
def authenticate(n_clicks, username, password):
    if n_clicks > 0:
        if username is None:
            return "Type the username", None
        if password is None:
            return "Type the password", None
        url = "http://localhost:8000/token"
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return (
                dcc.Location(pathname="/predict", id="redirect-to-predict"),
                response.text,
            )
        else:
            return "Authentication failed", None
    else:
        return None, None
