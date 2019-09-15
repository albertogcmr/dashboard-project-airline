# import dash
# import dash_html_components as html
import dash_core_components as dcc
from pipe import pipe

df2 = pipe()
data = df2.groupby('Country_ARR').count()
grafica1 = [{'x': [x], 'y': [y], 'type': 'bar', 'name': name} for x, y, name in zip(range(1, data.shape[0]), data.Id, data.index)]

data = df2[df2['Country_DEP']=='SPAIN'].groupby('Country_ARR').count()
grafica2 = [{'x': [x], 'y': [y], 'type': 'bar', 'name': name} for x, y, name in zip(range(1, data.shape[0]), data.Id, data.index)]


data = df2[df2['Country_ARR']=='SPAIN'].groupby('Country_DEP').count()
grafica3 = [{'x': [x], 'y': [y], 'type': 'bar', 'name': name} for x, y, name in zip(range(1, data.shape[0]), data.Id, data.index)]

df2['date_DEP_TIME'] = df2['DEP_TIME'].dt.date
data = df2.groupby('date_DEP_TIME').count()
grafica4 = [{'x': list(data.index), 'y': list(data.Id), 'type': 'line', 'name': list(data.index)}]


g1 = grafica1
g2 = grafica2
g3 = grafica3
g4 = grafica4


# grafica 1
graphic1 = dcc.Graph(
        id='example-graph-1',
        figure={
            'data': g1,
            'layout': {
                'title': 'Country Arrival quantity'
            }
        }, className="test"
    )

# grafica 2
graphic2 = dcc.Graph(
        id='example-graph-2',
        figure={
            'data': g2,
            'layout': {
                'title': 'Flight Departured from Spain'
            }
        }
    )


# grafica 3
graphic3 = dcc.Graph(
        id='example-graph-3',
        figure={
            'data': g3,
            'layout': {
                'title': 'Flight Arrived to Spain'
            }
        }
    )


# grafica 4
graphic4 = dcc.Graph(
        id='example-graph-4',
        figure={
            'data': g4,
            'layout': {
                'title': 'Flights by day'
            }
        }
    )

