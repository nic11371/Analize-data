import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, callback, dcc, html

df = pd.read_csv("vizualize/fixtures/exchange_rates.csv")
df["DATE"] = pd.to_datetime(df["DATE"])
df = df.sort_values("DATE")

app = Dash(__name__)
server = app.server

dropdown_options = [
    {"label": col, "value": col} for col in df.columns if col != "DATE"
]

app.layout = html.Div(
    [
        html.H1(children="Currency exchange rates", style={"text": "align"}),
        dcc.Dropdown(
            id="currency-dropdown",
            options=dropdown_options,
            value="AUSTRALIA - AUSTRALIAN DOLLAR",
        ),
        dcc.Graph(id="currency-graph"),
    ]
)


@app.callback(
    Output('currency-graph', 'figure'),
    [Input('currency-dropdown', 'value')]
)
def update_graph(selected_currency):
    fig = px.line(
        df, x="DATA", y=selected_currency, title=f"{selected_currency} Exchange Rate")
    return fig


if __name__ == 'main':
    app.run(debug=True)
