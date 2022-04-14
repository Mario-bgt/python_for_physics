import pandas as pd
import simplekml
import time

start = time.time()

df = pd.read_pickle('a_file.pkl')

main_cat =['Übrige erneuerbare Energien']
sub_cat = ['Photovoltaik']
plant_cat = ['Abwasserkraftwerk', 'Ausleitkraftwerk', 'Dotierwasserkraftwerk', 'Durchlaufkraftwerk',
                 'Trinkwasserkraftwerk', 'Pumpspeicherkraftwerk', 'Speicherkraftwerk', 'Angebaut', 'Integriert',
                 'Freistehend', 'Biomassenutzung','Kehrichtverbrennung','Abwasserreinigung']
df = df[df.Total_Power > 500]
df = df[df.Main_Cat.isin(main_cat)]
df = df[df.Sub_Cat.isin(sub_cat)]
df = df[df.Plant_Cat.isin(plant_cat)]
kml = simplekml.Kml()
for i in range(0, len(df)):
    kml.newpoint(description=df.iloc[i]['xtf_id'], coords=[(df.iloc[i]['lon'], df.iloc[i]['lat'])])
kml.save('currentplot.kml')
print('kml is generated')
end = time.time()
print(end-start)
df.to_excel('Only_Photovoltaics_over_500.xlsx')


