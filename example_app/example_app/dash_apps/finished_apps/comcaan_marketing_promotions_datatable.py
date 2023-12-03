# from _typeshed import NoneType
from turtle import width
import pandas as pd
import plotly 
import plotly.express as px
import dash
# from dash import dash_table
from dash import dash_table
from dash import dcc
# import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output, State
# from django_pandas.io import read_frame
from django_plotly_dash import DjangoDash 
from dash_table.Format import Format, Align
from datetime import datetime as dt
import dash_bootstrap_components as dbc
import re
from django.shortcuts import render, redirect
import seaborn as sns
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go


# instantiate tools

# instantiate dash app
app = DjangoDash('comcaan_marketing_promotions_datatable'
                , serve_locally=False
                )

# getting product name for drop down options
options2 = []
for Customer_Name in df.PlayerID.unique():
    options2.append({'label': Customer_Name, 'value': Customer_Name})

app.layout = dbc.Container([
]
                           
, className='report-container')
    # , fluid=True, style={'columnCount': 1, 'rowCount': 4}

if __name__ == '__main__':
    app.run_server(debug=True)


# iline chart callback-------------------------------------------------------------------------------------------------------------------------------------
@app.callback(
     Output('heartbeat-observed', 'figure')
    ,[Input('my-date-picker-range', 'start_date')
    ,Input('my-date-picker-range', 'end_date')
    ])

def build_graph_1(start_date, end_date):
    
    return()
