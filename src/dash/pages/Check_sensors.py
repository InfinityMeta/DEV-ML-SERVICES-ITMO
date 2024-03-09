import requests

import dash
from dash import Input, Output, State, callback, dcc, html

dash.register_page(__name__, path="/predict")

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
        html.H1(
            "Choose a model:",
            style={
                "text-align": "center",
                "margin-bottom": "20px",
                "font-size": "28px",
            },
        ),
        html.Div(
            [
                dcc.RadioItems(
                    id="model-radio",
                    options=[
                        {"label": "CatBoost", "value": "catboost"},
                        {"label": "Sklearn GB", "value": "sklearn_gb"},
                        {"label": "Random Forest", "value": "random_forest"},
                    ],
                    labelStyle={"display": "inline-block", "margin-bottom": "10px"},
                ),
            ],
            style={"text-align": "center", "font-size": "26px"},
        ),
        dcc.Link(
            "pricelist",
            href="/pricelist",
            style={"font-size": "24px"},
        ),
        html.H1(
            "Enter values:",
            style={
                "text-align": "center",
                "margin-bottom": "20px",
                "font-size": "28px",
            },
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Label(
                            "temperature:",
                            style={"font-size": "24px", "display": "block"},
                        ),
                        dcc.Input(
                            id="temperature-predict",
                            type="text",
                            style={
                                "width": "100px",
                                "font-size": "18px",
                            },
                        ),
                    ],
                    style={"margin-right": "20px", "margin-bottom": "20px"},
                ),
                html.Div(
                    [
                        html.Label(
                            "humidity:", style={"font-size": "24px", "display": "block"}
                        ),
                        dcc.Input(
                            id="humidity-predict",
                            type="text",
                            style={
                                "width": "100px",
                                "font-size": "18px",
                            },
                        ),
                    ],
                    style={"margin-bottom": "20px"},
                ),
            ],
            style={"display": "flex", "justify-content": "center"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Label(
                            "CO2CosIR:",
                            style={"font-size": "24px", "display": "block"},
                        ),
                        dcc.Input(
                            id="CO2CosIR-predict",
                            type="text",
                            style={
                                "width": "100px",
                                "font-size": "18px",
                            },
                        ),
                    ],
                    style={"margin-right": "20px", "margin-bottom": "20px"},
                ),
                html.Div(
                    [
                        html.Label(
                            "CO2MG811:",
                            style={"font-size": "24px", "display": "block"},
                        ),
                        dcc.Input(
                            id="CO2MG811-predict",
                            type="text",
                            style={
                                "width": "100px",
                                "font-size": "18px",
                            },
                        ),
                    ],
                    style={"margin-right": "20px", "margin-bottom": "20px"},
                ),
                html.Div(
                    [
                        html.Label(
                            "CO:",
                            style={"font-size": "24px", "display": "block"},
                        ),
                        dcc.Input(
                            id="CO-predict",
                            type="text",
                            style={
                                "width": "100px",
                                "font-size": "18px",
                            },
                        ),
                    ],
                    style={"margin-bottom": "20px"},
                ),
            ],
            style={"display": "flex", "justify-content": "center"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Label(
                            "MOX1:",
                            style={"font-size": "24px", "display": "block"},
                        ),
                        dcc.Input(
                            id="MOX1-predict",
                            type="text",
                            style={
                                "width": "100px",
                                "font-size": "18px",
                            },
                        ),
                    ],
                    style={"margin-right": "20px", "margin-bottom": "20px"},
                ),
                html.Div(
                    [
                        html.Label(
                            "MOX2:",
                            style={"font-size": "24px", "display": "block"},
                        ),
                        dcc.Input(
                            id="MOX2-predict",
                            type="text",
                            style={
                                "width": "100px",
                                "font-size": "18px",
                            },
                        ),
                    ],
                    style={"margin-right": "20px", "margin-bottom": "20px"},
                ),
                html.Div(
                    [
                        html.Label(
                            "MOX3:",
                            style={"font-size": "24px", "display": "block"},
                        ),
                        dcc.Input(
                            id="MOX3-predict",
                            type="text",
                            style={
                                "width": "100px",
                                "font-size": "18px",
                            },
                        ),
                    ],
                    style={"margin-right": "20px", "margin-bottom": "20px"},
                ),
                html.Div(
                    [
                        html.Label(
                            "MOX4:",
                            style={"font-size": "24px", "display": "block"},
                        ),
                        dcc.Input(
                            id="MOX4-predict",
                            type="text",
                            style={
                                "width": "100px",
                                "font-size": "18px",
                            },
                        ),
                    ],
                    style={"margin-bottom": "20px"},
                ),
            ],
            style={"display": "flex", "justify-content": "center"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Label(
                            "inhabited:",
                            style={"font-size": "24px", "display": "block"},
                        ),
                        dcc.Input(
                            id="inhabited-predict",
                            type="text",
                            style={
                                "width": "100px",
                                "font-size": "18px",
                            },
                        ),
                    ],
                    style={"margin-right": "20px", "margin-bottom": "20px"},
                ),
                html.Div(
                    [
                        html.Label(
                            "hour:", style={"font-size": "24px", "display": "block"}
                        ),
                        dcc.Input(
                            id="hour-predict",
                            type="text",
                            style={
                                "width": "100px",
                                "font-size": "18px",
                            },
                        ),
                    ],
                    style={"margin-bottom": "20px"},
                ),
            ],
            style={"display": "flex", "justify-content": "center"},
        ),
        html.Div(
            [
                dcc.Link(
                    "sensors description",
                    href="/sensors_description",
                    style={"font-size": "24px"},
                ),
            ]
        ),
        html.Button(
            "Send values",
            id="send-values",
            n_clicks=0,
            style={
                "margin": "20px",
                "font-weight": "bold",
                "background-color": "#008080",
                "color": "white",
                "font-size": "24px",
                "border-radius": "10px",
                "width": "300px",
            },
        ),
        html.Div(
            id="output-send",
            style={"text-align": "center", "font-size": "26px"},
        ),
        html.Button(
            "Check result",
            id="check-result",
            n_clicks=0,
            style={
                "margin": "20px",
                "font-weight": "bold",
                "background-color": "#008080",
                "color": "white",
                "font-size": "24px",
                "border-radius": "10px",
                "width": "300px",
            },
        ),
        html.Div(
            id="output-predict",
            style={"text-align": "center", "font-size": "26px"},
        ),
        dcc.Link(
            "My profile",
            href="/my_profile",
            style={
                "font-size": "32px",
                "position": "absolute",
                "top": "50px",
                "right": "100px",
            },
        ),
        dcc.Store(id="token", storage_type="session"),
        dcc.Store(id="prediction_id", storage_type="session"),
    ],
    style={
        "width": "600px",
        "margin": "auto",
        "text-align": "center",
        "margin-top": "20px",
    },
)


@callback(
    Output("output-send", "children"),
    Output("prediction_id", "data", allow_duplicate=True),
    State("model-radio", "value"),
    Input("send-values", "n_clicks"),
    Input("token", "data"),
    State("temperature-predict", "value"),
    State("humidity-predict", "value"),
    State("CO2CosIR-predict", "value"),
    State("CO2MG811-predict", "value"),
    State("CO-predict", "value"),
    State("MOX1-predict", "value"),
    State("MOX2-predict", "value"),
    State("MOX3-predict", "value"),
    State("MOX4-predict", "value"),
    State("inhabited-predict", "value"),
    State("hour-predict", "value"),
    prevent_initial_call=True,
)
def send_values(
    modelname,
    n_clicks,
    token,
    temperature,
    humidity,
    CO2CosIR,
    CO2MG811,
    CO,
    MOX1,
    MOX2,
    MOX3,
    MOX4,
    inhabited,
    hour,
):
    if n_clicks > 0:
        request_body = {
            "temperature": temperature,
            "humidity": humidity,
            "CO2CosIRValue": CO2CosIR,
            "CO2MG811Value": CO2MG811,
            "COValue": CO,
            "MOX1": MOX1,
            "MOX2": MOX2,
            "MOX3": MOX3,
            "MOX4": MOX4,
            "inhabited": inhabited,
            "hour": hour,
        }
        for k, v in request_body.items():
            if v == "" or v is None:
                return f"Some fields are missed, ex: {k}", None
            elif v == "inf":
                return f"{k}: infinity value not allowed", None
            else:
                try:
                    float(v)
                except:
                    return f"{k}: not a digit", None
                request_body[k] = float(v)
        if modelname is None:
            return "Select model", None
        if token is None:
            return "Not authorized", None
        token = eval(token)
        headers = {"Authorization": f"{token['token_type']} {token['access_token']}"}
        url = f"http://localhost:8000/models/{modelname}/predict"
        response = requests.post(url, json=request_body, headers=headers)
        if response.status_code != 200:
            return eval(response.text).get("detail"), None
        return "Values successfully sent", response.json()["prediction_id"]
    else:
        return None, None


checks_cnt = 0


@callback(
    Output("output-predict", "children"),
    Output("prediction_id", "data", allow_duplicate=True),
    State("model-radio", "value"),
    Input("check-result", "n_clicks"),
    Input("prediction_id", "data"),
    Input("token", "data"),
    prevent_initial_call=True,
)
def get_prediction(modelname, n_clicks, prediction_id, token):
    global checks_cnt
    if n_clicks > 0:
        if token is None:
            return "ERROR: Not authorized", prediction_id
        if prediction_id is None:
            return "ERROR: Sensors values not sent", prediction_id
        token = eval(token)
        headers = {"Authorization": f"{token['token_type']} {token['access_token']}"}
        url = f"http://localhost:8000/models/{modelname}/predictions/{prediction_id}"
        response = requests.get(url, headers=headers)
        if response.status_code == 400:
            return f"ERROR: {eval(response.text).get('detail')}.", prediction_id
        prediction_status = response.json()["prediction_status"]
        if prediction_status == "PENDING":
            checks_cnt += 1
            return (
                f"Check № {checks_cnt}: Prediction is not prepared yet.",
                prediction_id,
            )
        if prediction_status == "SUCCESS":
            checks_cnt = 0
            return f"Your result: {response.json()['prediction_result']}", None
    else:
        return None, prediction_id
