import dash
from dash import html

dash.register_page(__name__, path="/pricelist")


layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "Price List", style={"textAlign": "center", "marginBottom": "30px"}
                )
            ]
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H3("CatBoost"),
                        html.P(
                            "CatBoost is a gradient boosting algorithm developed by Yandex, designed for classification and regression tasks."
                        ),
                        html.P(
                            "Balanced accuracy: 61.3 %",
                        ),
                        html.P(
                            "Price: 7 credits",
                        ),
                    ],
                    style={
                        "font-size": "24px",
                        "margin": "50px",
                        "borderRadius": "10px",
                        "backgroundColor": "#f0f0f0",
                        "padding": "20px",
                        "textAlign": "center",
                    },
                    className="model-card",
                ),
                html.Div(
                    [
                        html.H3("Sklearn GB", style={"textAlign": "center"}),
                        html.P(
                            "Scikit-learn's gradient boosting implementation offers the advantage of being flexible and customizable through hyperparameter tuning, allowing for fine-tuning of model performance."
                        ),
                        html.P(
                            "Balanced accuracy: 68.6 %",
                        ),
                        html.P(
                            "Price: 15 credits",
                        ),
                    ],
                    style={
                        "font-size": "24px",
                        "margin": "50px",
                        "borderRadius": "10px",
                        "backgroundColor": "#f0f0f0",
                        "padding": "20px",
                        "textAlign": "center",
                    },
                    className="model-card",
                ),
                html.Div(
                    [
                        html.H3("Random Forest"),
                        html.P(
                            "Random Forest offers the advantage of being robust against overfitting and noisy data, as well as having the ability to handle high-dimensional data efficiently."
                        ),
                        html.P(
                            "Balanced accuracy: 60.7 %",
                        ),
                        html.P(
                            "Price: 5 credits",
                        ),
                    ],
                    style={
                        "font-size": "24px",
                        "margin": "50px",
                        "borderRadius": "10px",
                        "backgroundColor": "#f0f0f0",
                        "padding": "20px",
                        "textAlign": "center",
                    },
                    className="model-card",
                ),
            ],
            style={"display": "flex", "justifyContent": "space-around"},
        ),
        html.A(
            "Back to predictions",
            href="/predict",
            style={"textAlign": "center", "marginTop": "30px", "font-size": "30px"},
        ),
    ],
    style={"margin": "0 auto", "width": "80%"},
)
