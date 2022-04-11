import dash
from dash import dcc
import pandas as pd
from dash import html
import plotly.express as px
import simplekml

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']  # Design

dfp = pd.read_pickle('a_file.pkl')  # Startexcel einlesen

fig = px.scatter_mapbox(dfp, lat="lat", lon="lon",
                        hover_name="xtf_id",
                        hover_data=['Initial Power', 'Total_Power', 'Main_Cat', 'Sub_Cat',
                                    'Plant_Cat'],
                        zoom=13,
                        height=800)
fig.update_layout(mapbox_style="open-street-map")

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)  # CSS Style
app.layout = html.Div([  # app Layout
    html.H1('Elektrizitätsproduktionsanlagen der Schweiz'),
    html.H6('Auswahl der Hauptkategorie'),  # Titel
    dcc.Checklist(  # dropdown Menue mit allen Wagen
        id='main_cat',
        options=['Wasserkraft', 'Übrige erneuerbare Energien', 'Kernenergie', 'Fossile Energieträger'],
        value=['Übrige erneuerbare Energien'],
        inline=True
    ),
    html.H6('Auswahl der Produktionskategorie'),  # Titel
    dcc.Checklist(  # dropdown Menue mit allen Wagen
        id='plant_cat',
        options=['Abwasserkraftwerk', 'Ausleitkraftwerk', 'Dotierwasserkraftwerk', 'Durchlaufkraftwerk',
                 'Trinkwasserkraftwerk', 'Pumpspeicherkraftwerk', 'Speicherkraftwerk', 'Angebaut', 'Integriert',
                 'Freistehend', 'Biomassenutzung', 'Kehrichtverbrennung', 'Abwasserreinigung'],
        value=['Abwasserkraftwerk', 'Ausleitkraftwerk', 'Dotierwasserkraftwerk', 'Durchlaufkraftwerk',
               'Trinkwasserkraftwerk', 'Pumpspeicherkraftwerk', 'Speicherkraftwerk', 'Angebaut', 'Integriert',
               'Freistehend', 'Biomassenutzung', 'Kehrichtverbrennung', 'Abwasserreinigung'],
        inline=True
    ),
    html.H6('Auswahl der Unterkategorie'),  # Titel
    dcc.Checklist(  # dropdown Menue mit allen Wagen
        id='sub_cat',
        options=['Wasserkraft', 'Photovoltaik', 'Windenergie', 'Biomasse', 'Geothermie',
                 'Kernenergie', 'Erdöl', 'Erdgas', 'Kohle', 'Abfälle'],
        value=['Photovoltaik'],
        inline=True
    ),
    html.H6('Auswahl der min bzw max Werte von Total Power'),  # Titel
    dcc.Input(id="minimum", type="number", placeholder=0, value=0),
    dcc.Input(id="maximum", type="number", placeholder=1872000, value=1872000),
    html.Div(
        [html.Button("Download as HTML", id="btn_html"),  # Knopf für HTML export
         dcc.Download(id="download")]  # id für HTML export
    ),
    dcc.Graph(  # Bild des Graph mit analyse Option
        id='map',
        figure=fig,
        style={  # Style der Map
            'width': '100%', 'height': '800px', 'lineHeight': '0px',
            'borderWidth': '0px', 'borderStyle': 'dashed',
            'borderRadius': '0px', 'textAlign': 'center', 'margin': '1px'
        }, ),
])  # Applayout


@app.callback(
    dash.dependencies.Output('map', 'figure'),  # Die geplottete figur als Output definieren
    [dash.dependencies.Input('main_cat', 'value'),
     dash.dependencies.Input('plant_cat', 'value'),
     dash.dependencies.Input('sub_cat', 'value'),
     dash.dependencies.Input('minimum', 'value'),
     dash.dependencies.Input('maximum', 'value'),
     ])
def update_output(main_cat, plant_cat, sub_cat, minimum, maximum):  # erstellen des Plot und Rückgabe plot
    global fig
    df = dfp
    df = df[df.Total_Power > minimum]
    df = df[df.Total_Power < maximum]
    df = df[df.Main_Cat.isin(main_cat)]
    df = df[df.Sub_Cat.isin(sub_cat)]
    df = df[df.Plant_Cat.isin(plant_cat)]
    fig = px.scatter_mapbox(df, lat="lat", lon="lon",
                            hover_name="xtf_id",
                            hover_data=['_x', '_y','Initial Power', 'Total_Power', 'Main_Cat', 'Sub_Cat',
                                        'Plant_Cat'],
                            zoom=13,
                            height=800)
    fig.update_layout(mapbox_style="open-street-map")
    fig.write_html("currentmap.html")
    kml = simplekml.Kml()
    for i in range(0, len(df)):
        kml.newpoint(description=df.iloc[i]['xtf_id'], coords=[(df.iloc[i]['lon'], df.iloc[i]['lat'])])
    kml.save('currentplot.kml')
    return fig

@app.callback(  # Ausgabe der HTML Version
    dash.dependencies.Output('download', 'data'),  # Output definieren
    [dash.dependencies.Input('btn_html', 'n_clicks')]  # Button HTMl als input definieren
)
def download(n_clicks):  # Ausgabe der HTML Version
    if n_clicks is None:  # Falls der button nicht gedrückt wurde
        print('Button HTML has not been pressed yet')
    else:  # Falls der Button gedrückt wurde
        return dcc.send_file(
            "currentmap.html"  # Ausgabe der HTML Datei
        )

if __name__ == '__main__':
    app.run_server(debug=False)
