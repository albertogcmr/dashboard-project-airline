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
    html.Div(children=[
        html.H1(children='Ryanair Dashboard'),

        html.Div(children='''
            Authon: https://github.com/albertogcmr
        ''')], className='title')
    ,
    html.Div([
        graphic1, 
        graphic4, 
    ], className='graph-row')
    , 
    html.Div([ 
        graphic2, 
        graphic3, 
    ], className='graph-row')
    
], className='higher')

if __name__ == '__main__':
    app.run_server(debug=True)