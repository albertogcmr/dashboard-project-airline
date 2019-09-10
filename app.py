import dash
import dash_core_components as dcc
import dash_html_components as html
from graphics import graphic1, graphic2, graphic3, graphic4

# https://dash.plot.ly/getting-started

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
    html.Link(
        href=app.get_asset_url('style.css'),
        rel='stylesheet'
    ), 
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    html.Div([
        graphic1, 
        graphic2, 
    ], className='graph-row')
    , 
    html.Div([ 
        graphic3, 
        graphic4, 
    ], className='graph-row')

     
])

if __name__ == '__main__':
    app.run_server(debug=True)