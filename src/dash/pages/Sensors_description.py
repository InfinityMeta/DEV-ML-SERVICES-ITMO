import dash
from dash import html

dash.register_page(__name__, path="/sensors_description")


layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "Sensors desctiption",
                    style={"textAlign": "center", "marginBottom": "30px"},
                )
            ]
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H3("Temperature"),
                        html.P(
                            "Temperature it is a measure of how hot or cold something. The normal room temperature for most indoor spaces is typically around 20-25 degrees."
                        ),
                        html.P("It is 68-77 degrees Fahrenheit."),
                        html.P(
                            "This range is considered comfortable for most people and is often used as a standard for indoor environments, but individual preferences for room temperature can vary."
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
                    className="sensor-card",
                ),
                html.Div(
                    [
                        html.H3("Humidity", style={"textAlign": "center"}),
                        html.P(
                            "Humidity is the amount of water vapor present in the air. The ideal indoor humidity level for comfort and health is generally considered to be between 30% and 60%."
                        ),
                        html.P(
                            " It is typically measured as a percentage, representing the ratio of the actual amount of water vapor in the air to the maximum amount of water vapor the air can hold at a specific temperature."
                        ),
                        html.P(
                            "This range helps maintain a comfortable environment and reduces the risk of issues such as mold growth, respiratory problems, and dry skin."
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
                    className="sensor-card",
                ),
                html.Div(
                    [
                        html.H3("CO2CosIR"),
                        html.P(
                            "A sensor that measures CO2, COS, and IR values is likely designed to monitor air quality or environmental conditions."
                        ),
                        html.P(
                            "CO2 (Carbon Dioxide): The sensor measures the concentration of carbon dioxide in the air. "
                        ),
                        html.P(
                            "COS (Carbonyl Sulfide): The sensor measures the concentration of carbonyl sulfide in the air."
                        ),
                        html.P(
                            "IR (Infrared): The sensor may use infrared technology to detect certain gases or substances in the environment."
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
                    className="sensor-card",
                ),
            ],
            style={"display": "flex", "justifyContent": "space-around"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H3("CO2MG811"),
                        html.P(
                            "The is a carbon dioxide (CO2) sensor that utilizes the MG-811 sensor module."
                        ),
                        html.P(
                            "It typically detects the presence of carbon dioxide gas based on its specific electrochemical or optical properties."
                        ),
                        html.P(
                            "It is designed to monitor and quantify the concentration of carbon dioxide gas in the air using the MG-811 sensor module."
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
                    className="sensor-card",
                ),
                html.Div(
                    [
                        html.H3("CO", style={"textAlign": "center"}),
                        html.P(
                            "Sensor is designed to detect and measure the concentration of carbon monoxide (CO) gas."
                        ),
                        html.P(
                            "Carbon monoxide is a toxic gas that can be harmful or even deadly when inhaled in high concentrations."
                        ),
                        html.P(
                            "Exposure to elevated levels of carbon monoxide can lead to symptoms such as headaches, dizziness, nausea, confusion, and in severe cases, unconsciousness or death."
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
                    className="sensor-card",
                ),
                html.Div(
                    [
                        html.H3("MOX"),
                        html.P(
                            "Sensor  is designed to detect and measure the concentration of Metal Oxide (MOX) gas."
                        ),
                        html.P(
                            "Metal oxide sensors work by detecting changes in electrical conductivity when they come into contact with specific gases."
                        ),
                        html.P(
                            "Metal oxide sensors are commonly used in gas detection systems to monitor the presence of various gases, such as volatile organic compounds (VOCs), ammonia, carbon monoxide, hydrogen, and other gases."
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
                    className="sensor-card",
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
