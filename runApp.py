import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import os 
import dash_table
from datetime import date

app = dash.Dash(__name__)

app.layout  =  html.Div(children=[

    html.Div(
        className="app-header",
        children=[
            html.Div('Expense Tracker ', className="app-header--title", style= {"text-align":"center"})
        ]),
    html.Br(),
    html.H3('Create a base template'),
    html.Br(),
    html.H3('Create a new expense sheet'),
    html.Br(),
    html.H3('Edit a new expense sheet'),
    html.Br(),
    html.H3('Analyze'),
    html.Br()
])
if __name__ == '__main__':
	app.run_server(host = '0.0.0.0', debug = True)