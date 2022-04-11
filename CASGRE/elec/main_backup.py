import dash
import dash_core_components as dcc
import pandas as pd
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']  # Design

dfp = pd.read_excel('elec_220411_BaMa.xlsx', engine="openpyxl")  # Startexcel einlesen

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)  # CSS Style
app.layout = html.Div([  # app Layout
    html.H1('Distanzsensoren der Güterwagen analyse Seite'),  # Titel
    dcc.Dropdown(  # dropdown Menue mit allen Wagen
        id='dropdown',
        options=[
            {'label': 'Sgp 7601', 'value': '7601'},
            {'label': 'Sgp 7603', 'value': '7603'},
            {'label': 'Sgp 7604', 'value': '7604'},
            {'label': 'Sgp 7605', 'value': '7605'},
            {'label': 'Sgp 7606', 'value': '7606'},
            {'label': 'Sgp 7607', 'value': '7607'},
            {'label': 'Sgp 7608', 'value': '7608'},
            {'label': 'Sgp 7609', 'value': '7609'},
            {'label': 'Sgp 7610', 'value': '7610'},
            {'label': 'Uac 7992', 'value': '7992'},
            {'label': 'Uac 7993', 'value': '7993'},
            {'label': 'Uac 7994', 'value': '7994'},
            {'label': 'Uac 7996', 'value': '7996'},
            {'label': 'Uac 7997', 'value': '7997'},
            {'label': 'Uac 7998', 'value': '7998'},
            {'label': 'Uac 7999', 'value': '7999'},
            {'label': 'Za 8134', 'value': '8134'},
            {'label': 'Re-w 8245', 'value': '8245'},
            {'label': 'Re-w 8246', 'value': '8246'},
            {'label': 'Re-w 8247', 'value': '8247'},
            {'label': 'Re-w 8249', 'value': '8249'},
            {'label': 'Re-w 8257', 'value': '8257'},
            {'label': 'Re-w 8259', 'value': '8259'},
            {'label': 'Re-w 8260', 'value': '8260'},
            {'label': 'Re-w 8263', 'value': '8263'},
            {'label': 'Re-w 8264', 'value': '8264'},
            {'label': 'Re-w 8267', 'value': '8267'},
            {'label': 'Re-w 8268', 'value': '8268'},
            {'label': 'Re-w 8269', 'value': '8269'},
            {'label': 'Re-w 8387', 'value': '8387'},
            {'label': 'Sp-w 8271', 'value': '8271'},
            {'label': 'Sp-w 8272', 'value': '8272'},
            {'label': 'Sp-w 8273', 'value': '8273'},
            {'label': 'Sp-w 8274', 'value': '8274'},
            {'label': 'Sp-w 8275', 'value': '8275'},
            {'label': 'Sp-w 8276', 'value': '8276'},
            {'label': 'Sp-w 8277', 'value': '8277'},
            {'label': 'Sp-w 8278', 'value': '8278'},
            {'label': 'Sp-w 8279', 'value': '8279'},
            {'label': 'Sp-w 8280', 'value': '8280'},
            {'label': 'Sp-w 8281', 'value': '8281'},
            {'label': 'Sp-w 8282', 'value': '8282'},
            {'label': 'Sp-w 8283', 'value': '8283'},
            {'label': 'Sp-w 8284', 'value': '8284'},
            {'label': 'Sp-w 8285', 'value': '8285'},
            {'label': 'Sp-w 8286', 'value': '8286'},
            {'label': 'Sp-w 8287', 'value': '8287'},
            {'label': 'Sp-w 8288', 'value': '8288'},
            {'label': 'Sp-w 8289', 'value': '8289'},
            {'label': 'Sp-w 8290', 'value': '8290'},
            {'label': 'Sp-w 8291', 'value': '8291'},
            {'label': 'Sp-w 8292', 'value': '8292'},
            {'label': 'Sp-w 8293', 'value': '8293'},
            {'label': 'Sp-w 8294', 'value': '8294'},
            {'label': 'Sp-w 8295', 'value': '8295'},
            {'label': 'Sp-w 8296', 'value': '8296'},
            {'label': 'Sp-w 8297', 'value': '8297'},
            {'label': 'Sp-w 8298', 'value': '8298'},
            {'label': 'Sp-w 8299', 'value': '8299'},
            {'label': 'Sp-w 8300', 'value': '8300'},
            {'label': 'Sp-w 8351', 'value': '8351'},
            {'label': 'Sp-w 8352', 'value': '8352'},
            {'label': 'Sp-w 8353', 'value': '8353'},
            {'label': 'Sp-w 8355', 'value': '8355'},
            {'label': 'Sp-w 8357', 'value': '8357'},
            {'label': 'Sp-w 8358', 'value': '8358'},
            {'label': 'Sp-w 8359', 'value': '8359'},
            {'label': 'Sp-w 8360', 'value': '8360'},
            {'label': 'Fac 8703', 'value': '8703'},
            {'label': 'Fac 8704', 'value': '8704'},
            {'label': 'Fac 8705', 'value': '8705'},
            {'label': 'Fac 8706', 'value': '8706'},
            {'label': 'Fac 8712', 'value': '8712'},
            {'label': 'Fac 8726', 'value': '8726'},
            {'label': 'Fac 8727', 'value': '8727'},
            {'label': 'Fac 8728', 'value': '8728'},
            {'label': 'Fac 8729', 'value': '8729'},
            {'label': 'Fac 8731', 'value': '8731'},
            {'label': 'Fac 8732', 'value': '8732'},
            {'label': 'Re-t 65401', 'value': '65401'},
            {'label': 'Re-t 65402', 'value': '65402'},
            {'label': 'Re-t 65403', 'value': '65403'},
            {'label': 'Re-t 65404', 'value': '65404'},
            {'label': 'Re-t 65405', 'value': '65405'},
            {'label': 'Re-t 65406', 'value': '65406'},
            {'label': 'Re-t 65407', 'value': '65407'},
            {'label': 'Re-t 65409', 'value': '65409'},
            {'label': 'Re-t 65410', 'value': '65410'},
            {'label': 'Xk 99301', 'value': '99301'},
            {'label': 'Xac 8735', 'value': '8735'},
            {'label': 'Xac 8737', 'value': '8737'},
            {'label': 'Xac 8742', 'value': '8742'},
            {'label': 'Xa-u 8768', 'value': '8768'},
            {'label': 'Xak 9387', 'value': '9387'},
            {'label': 'Xak 9388', 'value': '9388'},
            {'label': 'Xae-w 9401', 'value': '9401'},
            {'label': 'Xae-w 9402', 'value': '9402'},
            {'label': 'Xa-u 9441', 'value': '9441'},
            {'label': 'Xa-u 9443', 'value': '9443'},
            {'label': 'Xa-u 9444', 'value': '9444'},
            {'label': 'Xa-u 9445', 'value': '9445'},
            {'label': 'Xa-u 9446', 'value': '9446'},
            {'label': 'Xae-t 93105', 'value': '93105'},
            {'label': 'Xae-t 93106', 'value': '93106'},
            {'label': 'Xae-t 93107', 'value': '93107'},
            {'label': 'Xae-t 93109', 'value': '93109'}
        ],
        value='7601'
    ),
    dcc.RadioItems(id='style',  # auswählen welcher Graph wir erstellen möchten
                   options=[
                       {'label': 'Beide Sensoren zusammen über Zeit', 'value': 'beide'},
                       {'label': 'Sensor 1 über Zeit', 'value': 'sens1'},
                       {'label': 'Sensor 3 über Zeit', 'value': 'sens2'},
                       {'label': 'Beide Punkte der Höhe nach', 'value': 'high'},
                       {'label': 'Punkte nach Höhe Sensor 1', 'value': 'high1'},
                       {'label': 'Punkte nach Höhe Sensor 3', 'value': 'high3'},

                   ],
                   value='beide',  # Standart vorwahl ist beide
                   # labelStyle={'display': 'inline-block'}  # alles auf einer Linie
                   ),
    html.Div(
        [html.Button("Download as HTML", id="btn_html"),  # Knopf für HTML export
         dcc.Download(id="download")]  # id für HTML export
    ),
    html.Div(
        [html.Button("Download as Excel", id="btn_xlsx"),  # Knopf für Excel export
         dcc.Download(id="download3")]  # id für Excel export
    ),
    html.Div(
        [html.Button("Download as PDF", id="btn_kml"),  # Knopf für KML export
         dcc.Download(id="download2")]  # id für KML export
    ),
    dcc.Graph(  # Bild des Graph mit analyse Option
        id='graph_zusammen',
        figure=fig,
        style={  # Style der Map
            'width': '100%', 'height': '800px', 'lineHeight': '0px',
            'borderWidth': '0px', 'borderStyle': 'dashed',
            'borderRadius': '0px', 'textAlign': 'center', 'margin': '1px'
        }, ),
])  # Applayout


@app.callback(
    dash.dependencies.Output('map', 'figure'),  # Die geplottete figur als Output definieren
    [dash.dependencies.Input('dropdown', 'value'),  # Den gewählten Wagen als Input definieren
     dash.dependencies.Input('style', 'value'),  # Den gewählten Style einlesen
     ])
def update_output(value, style):  # erstellen des Plot und Rückgabe plot

    return fig


@app.callback(  # Ausgabe der Excel Version
    dash.dependencies.Output('download3', 'data'),  # Excel als Output definieren
    [dash.dependencies.Input('btn_xlsx', 'n_clicks')]  # Button Excel als input definieren
)
def download3(n_clicks):  # Ausgabe der Excel Version
    if n_clicks is None:  # Falls der Button noch nicht gedrückt wurde
        print('Button xlsx has not been pressed yet')
    else:  # Falls der Button gedrückt wurde
        return dcc.send_file(  # ausgabe der Excel version
            "currentgraph.xlsx"
        )


@app.callback(  # Ausgabe der HTML Version
    dash.dependencies.Output('download', 'data'),  # Output definieren
    [dash.dependencies.Input('btn_html', 'n_clicks')]  # Button HTMl als input definieren
)
def download(n_clicks):  # Ausgabe der HTML Version
    if n_clicks is None:  # Falls der button nicht gedrückt wurde
        print('Button HTML has not been pressed yet')
    else:  # Falls der Button gedrückt wurde
        return dcc.send_file(
            "currentgraph.html"  # Ausgabe der HTML Datei
        )


@app.callback(  # Ausgabe der KML Version
    dash.dependencies.Output('download2', 'data'),  # Output definieren
    [dash.dependencies.Input('btn_kml', 'n_clicks')]  # Button KML als input definieren
)
def download2(n_clicks):  # Ausgabe der KML Version
    if n_clicks is None:  # Falls der Button noch nicht gedrückt wurden
        print('Button KML has not been pressed yet')
    else:  # Falls der Button gedrückt wurde
        return dcc.send_file(
            "currentplot.pdf"  # Ausgabe der KML Datei
        )


if __name__ == '__main__':
    app.run_server(debug=False)
