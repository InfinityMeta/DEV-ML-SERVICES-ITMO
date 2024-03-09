import pandas as pd
import requests

import dash
from dash import Input, Output, State, callback, dash_table, dcc, html

dash.register_page(__name__, path="/my_profile")


layout = html.Div(
    [
        dcc.Store(id="token", storage_type="session"),
        dcc.Interval(id="interval-component"),
        html.H1("My Profile", style={"margin": "40px"}),
        html.Div(id="fullname-id", style={"font-size": "28px", "margin": "40px"}),
        html.Div(id="balance-id", style={"font-size": "28px", "margin": "40px"}),
        dcc.Location(id="url", refresh=False),
        html.H1("Predictions", style={"margin": "40px"}),
        html.Div(id="predictions-table", style={"margin": "40px"}),
        html.A(
            "Back to predictions",
            href="/predict",
            style={
                "textAlign": "center",
                "marginTop": "30px",
                "font-size": "30px",
                "margin": "40px",
            },
        ),
    ]
)


@callback(
    Output("fullname-id", "children"),
    Output("balance-id", "children"),
    Output("predictions-table", "children"),
    Input("interval-component", "n_intervals"),
    Input("url", "pathname"),
    State("token", "data"),
)
def update_profile_info(n_intervals, pathname, data):
    if pathname == "/my_profile":
        token = eval(data)
        headers = {"Authorization": f"{token['token_type']} {token['access_token']}"}
        response = requests.get(
            "http://localhost:8000/users/user_history", headers=headers
        )
        data = response.json()
        fullname = data.get("fullname", "Unknown")
        balance = data.get("balance", 0)
        predictions = data.get("predictions", [])
        df_predictions = pd.DataFrame(predictions)
        if len(df_predictions) == 0:
            return (
                fullname,
                f"Balance: {balance} credits",
                html.H1("Your user history is empty."),
            )
        df_predictions.drop(["id", "owner_id"], axis=1, inplace=True)
        df_predictions["creation_date"] = (
            df_predictions["creation_date"]
            .apply(lambda x: pd.to_datetime(x))
            .dt.round("S")
        )
        df_predictions = df_predictions.rename(
            columns={
                "boosting_name": "Model",
                "prediction": "Prediction",
                "balance_shift": "Balance shift",
                "creation_date": "Date",
            }
        )
        table = dash_table.DataTable(
            id="predictions",
            columns=[{"name": col, "id": col} for col in df_predictions.columns],
            data=df_predictions.to_dict("records"),
            style_data={"fontSize": "20px"},
            style_table={"overflowX": "auto"},
            style_header={
                "backgroundColor": "lightgrey",
                "fontWeight": "bold",
                "fontSize": "24px",
            },
            style_cell={
                "textAlign": "center",
                "whiteSpace": "normal",
                "height": "auto",
                "minWidth": "150px",
                "width": "150px",
                "maxWidth": "150px",
            },
            style_data_conditional=[
                {
                    "if": {"row_index": "odd"},
                    "backgroundColor": "rgb(248, 248, 248)",
                }
            ],
        )

        return fullname, f"Balance: {balance} credits", table
    else:
        return
