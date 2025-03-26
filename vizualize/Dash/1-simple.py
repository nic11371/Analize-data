import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hi, Dash!'),
    html.Div(children='''This is an example of a simple web application using Dash''')
])

if __name__ == '__main__':
    app.run_server(debug=True)