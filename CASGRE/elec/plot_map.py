import pandas as pd
import plotly.express as px

df = pd.read_pickle('a_file.pkl')

print(df)
minimum = 500
maximum = 800
main_cat =['Übrige erneuerbare Energien']
sub_cat = ['Photovoltaik']
plant_cat = ['Abwasserkraftwerk', 'Ausleitkraftwerk', 'Dotierwasserkraftwerk', 'Durchlaufkraftwerk',
                 'Trinkwasserkraftwerk', 'Pumpspeicherkraftwerk', 'Speicherkraftwerk', 'Angebaut', 'Integriert',
                 'Freistehend', 'Biomassenutzung','Kehrichtverbrennung','Abwasserreinigung']
df = df[df.Total_Power > minimum]
df = df[df.Total_Power < maximum]
df = df[df.Main_Cat.isin(main_cat)]
df = df[df.Sub_Cat.isin(sub_cat)]
df = df[df.Plant_Cat.isin(plant_cat)]
print(df)
for i in range(1, len(df)):
    print(df.iloc[i]['lat'])
fig = px.scatter_mapbox(df, lat="lat", lon="lon",
                        hover_name="xtf_id",
                        hover_data=['Initial Power', 'Total_Power', 'Main_Cat', 'Sub_Cat',
                                    'Plant_Cat'],
                        zoom=13,
                        height=800)
fig.update_layout(mapbox_style="open-street-map")
fig.show()
