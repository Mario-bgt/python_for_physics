import dash
from dash import dcc
import pandas as pd
from dash import html
import plotly.express as px
import simplekml

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

dfp = pd.read_pickle('a_file.pkl')

fig = px.scatter_mapbox(dfp, lat="lat", lon="lon",
                        hover_name="xtf_id",
                        hover_data=['_x','_y','Initial Power', 'Total_Power', 'Main_Cat', 'Sub_Cat',
                                    'Plant_Cat'],
                        zoom=13,
                        height=800)
fig.update_layout(mapbox_style="open-street-map")

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H1('Elektrizitätsproduktionsanlagen der Schweiz'),
    html.H6('Auswahl der Hauptkategorie'),
    dcc.Checklist(
        id='main_cat',
        options=['Wasserkraft', 'Übrige erneuerbare Energien', 'Kernenergie', 'Fossile Energieträger'],
        value=['Übrige erneuerbare Energien'],
        inline=True
    ),
    html.H6('Auswahl der Produktionskategorie'),
    dcc.Checklist(
        id='plant_cat',
        options=['Abwasserkraftwerk', 'Ausleitkraftwerk', 'Dotierwasserkraftwerk', 'Durchlaufkraftwerk',
                 'Trinkwasserkraftwerk', 'Pumpspeicherkraftwerk', 'Speicherkraftwerk', 'Angebaut', 'Integriert',
                 'Freistehend', 'Biomassenutzung', 'Kehrichtverbrennung', 'Abwasserreinigung'],
        value=['Abwasserkraftwerk', 'Ausleitkraftwerk', 'Dotierwasserkraftwerk', 'Durchlaufkraftwerk',
               'Trinkwasserkraftwerk', 'Pumpspeicherkraftwerk', 'Speicherkraftwerk', 'Angebaut', 'Integriert',
               'Freistehend', 'Biomassenutzung', 'Kehrichtverbrennung', 'Abwasserreinigung'],
        inline=True
    ),
    html.H6('Auswahl der Unterkategorie'),
    dcc.Checklist(
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
        [html.Button("Download as HTML", id="btn_html"),
         dcc.Download(id="download")]
    ),
    html.Div(
        [html.Button("Download as KML", id="btn_kml"),
         dcc.Download(id="download2")]
    ),
    html.Div(
        [html.Button("Download as XLSX", id="btn_xlsx"),
         dcc.Download(id="download3")]
    ),
    dcc.Graph(
        id='map',
        figure=fig,
        style={
            'width': '100%', 'height': '800px', 'lineHeight': '0px',
            'borderWidth': '0px', 'borderStyle': 'dashed',
            'borderRadius': '0px', 'textAlign': 'center', 'margin': '1px'
        }, ),
])  # Applayout


@app.callback(
    dash.dependencies.Output('map', 'figure'),
    [dash.dependencies.Input('main_cat', 'value'),
     dash.dependencies.Input('plant_cat', 'value'),
     dash.dependencies.Input('sub_cat', 'value'),
     dash.dependencies.Input('minimum', 'value'),
     dash.dependencies.Input('maximum', 'value'),
     ])
def update_output(main_cat, plant_cat, sub_cat, minimum, maximum):
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
    return fig


@app.callback(
    dash.dependencies.Output('download', 'data'),
    [dash.dependencies.Input('btn_html', 'n_clicks'),
     dash.dependencies.Input('main_cat', 'value'),
     dash.dependencies.Input('plant_cat', 'value'),
     dash.dependencies.Input('sub_cat', 'value'),
     dash.dependencies.Input('minimum', 'value'),
     dash.dependencies.Input('maximum', 'value'),
     ]
)
def download(n_clicks, main_cat, plant_cat, sub_cat, minimum, maximum):
    if n_clicks is None:
        print('Button HTML has not been pressed yet')
    else:
        df = dfp
        df = df[df.Total_Power > minimum]
        df = df[df.Total_Power < maximum]
        df = df[df.Main_Cat.isin(main_cat)]
        df = df[df.Sub_Cat.isin(sub_cat)]
        df = df[df.Plant_Cat.isin(plant_cat)]
        fig = px.scatter_mapbox(df, lat="lat", lon="lon",
                                hover_name="xtf_id",
                                hover_data=['_x', '_y', 'Initial Power', 'Total_Power', 'Main_Cat', 'Sub_Cat',
                                            'Plant_Cat'],
                                zoom=13,
                                height=800)
        fig.update_layout(mapbox_style="open-street-map")
        fig.write_html("currentmap.html")
        return dcc.send_file(
            "currentmap.html"
        )


@app.callback(
    dash.dependencies.Output('download2', 'data'),
    [dash.dependencies.Input('btn_kml', 'n_clicks'),
     dash.dependencies.Input('main_cat', 'value'),
     dash.dependencies.Input('plant_cat', 'value'),
     dash.dependencies.Input('sub_cat', 'value'),
     dash.dependencies.Input('minimum', 'value'),
     dash.dependencies.Input('maximum', 'value'),
     ]
)
def download(n_clicks, main_cat, plant_cat, sub_cat, minimum, maximum):
    if n_clicks is None:
        print('Button KML has not been pressed yet')
    else:
        df = dfp
        df = df[df.Total_Power > minimum]
        df = df[df.Total_Power < maximum]
        df = df[df.Main_Cat.isin(main_cat)]
        df = df[df.Sub_Cat.isin(sub_cat)]
        df = df[df.Plant_Cat.isin(plant_cat)]
        kml = simplekml.Kml()
        for i in range(0, len(df)):
            kml.newpoint(description=df.iloc[i]['xtf_id'], coords=[(df.iloc[i]['lon'], df.iloc[i]['lat'])])
        kml.save('currentplot.kml')
        return dcc.send_file("currentmap.kml")


@app.callback(
    dash.dependencies.Output('download3', 'data'),
    [dash.dependencies.Input('btn_xlsx', 'n_clicks'),
     dash.dependencies.Input('main_cat', 'value'),
     dash.dependencies.Input('plant_cat', 'value'),
     dash.dependencies.Input('sub_cat', 'value'),
     dash.dependencies.Input('minimum', 'value'),
     dash.dependencies.Input('maximum', 'value'),
     ]
)
def download(n_clicks, main_cat, plant_cat, sub_cat, minimum, maximum):
    if n_clicks is None:
        print('Button XLSX has not been pressed yet')
    else:
        df = dfp
        df = df[df.Total_Power > minimum]
        df = df[df.Total_Power < maximum]
        df = df[df.Main_Cat.isin(main_cat)]
        df = df[df.Sub_Cat.isin(sub_cat)]
        df = df[df.Plant_Cat.isin(plant_cat)]
        df.to_excel('currentmap.xlsx')
        return dcc.send_file("currentmap.xlsx")


if __name__ == '__main__':
    app.run_server(debug=False)
