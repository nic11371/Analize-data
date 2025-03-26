import pandas as pd
import plotly.express as px


# Готовим датафрейм
df = pd.read_csv('vizualize/fixtures/exchange_rates.csv')


def get_rates():
    # BEGIN (write your solution here)
    fig = px.bar(
        df,
        x="DATE",
        y="EURO AREA - EURO",
        title="Курс USD к выбранной валюте"
    )

    fig.update_layout(
        updatemenus=[
            dict(
                buttons=[
                    dict(
                        args=[{'y': [df["EURO AREA - EURO"]]}],
                        label="EURO",
                        method='update',
                        ),
                    dict(
                        args=[{'y': [
                            df['UNITED KINGDOM - UNITED KINGDOM POUND']
                        ]}],
                        label="UNITED KINGDOM POUND",
                        method='update',
                        ),
                    dict(
                        args=[{'y': [df['CHINA - YUAN']]}],
                        label="YUAN",
                        method='update'
                        )
                ],
                direction='down',
            ),
        ]
    )
    # END

    return fig
