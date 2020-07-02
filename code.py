import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('Solarize_Light2')
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8');

df_15 = pd.read_csv('Homicidios_2015.csv')
df_16 = pd.read_csv('Homicidios_2016.csv')
df_17 = pd.read_csv('Homicidios_2017.csv')
df_18 = pd.read_excel('homicidios-2018.xls', skipfooter=1)
df_19 = pd.read_excel('homicidios-2019.xls', skipfooter=4, skiprows=8)

df_15.columns = df_16.columns

df_15[~df_15['Fecha'].isna()]
df_16[~df_16['Fecha'].isna()]
df_17[~df_17['Fecha'].isna()]
df_18[~df_18['Fecha'].isna()]
df_19[~df_19['Fecha'].isna()]

df_15['Fecha'] = pd.to_datetime(df_15['Fecha'])
df_16['Fecha'] = pd.to_datetime(df_16['Fecha'])
df_17['Fecha'] = pd.to_datetime(df_17['Fecha'])
df_18['Fecha'] = pd.to_datetime(df_18['Fecha'])
df_19['Fecha'] = pd.to_datetime(df_19['Fecha'])

df_15 = df_15[df_15['Municipio'] == 'BOGOTÁ D.C. (CT)']
df_16 = df_16[df_16['Municipio'] == 'BOGOTÁ D.C. (CT)']
df_17 = df_17[df_17['Municipio'] == 'BOGOTÁ D.C. (CT)']
df_18 = df_18[df_18['Municipio'] == 'BOGOTÁ D.C. (CT)']
df_19 = df_19[df_19['Municipio'] == 'BOGOTÁ D.C. (CT)']

plot = pd.DataFrame()

plot['2015'] =  df_15.groupby(pd.Grouper(key='Fecha', freq='1M'))['Cantidad'].sum()
plot.index = plot.index.strftime('%B')
plot['2016'] =  df_16.groupby(pd.Grouper(key='Fecha', freq='1M'))['Cantidad'].sum().values
plot['2017'] =  df_17.groupby(pd.Grouper(key='Fecha', freq='1M'))['Cantidad'].sum().values
plot['2018'] =  df_18.groupby(pd.Grouper(key='Fecha', freq='1M'))['Cantidad'].sum().values
plot['2019'] =  df_19.groupby(pd.Grouper(key='Fecha', freq='1M'))['Cantidad'].sum().values

plot['2020'] = [79, 95, 89, 42, 99, 88, None, None, None, None, None, None]

prom = pd.DataFrame()

prom['Prom-5A'] = (plot['2015'] + plot['2016'] + plot['2017'] + plot['2018'] + plot['2019'])/5
prom['2020'] = plot['2020']
plt.figure(figsize=(10,5), dpi=300)
plt.margins(0,0.2)
plt.plot(prom.index, prom['Prom-5A']  ,label='Prom 5 Años')
plt.plot(prom.index, prom['2020']  ,label='2020')
plt.ylabel('Número de homicidios', fontsize=16, weight='bold')
plt.title('Reducción del 12% en los homicidios en el 1er semestre del 2020 Bogotá', fontsize=12)
plt.suptitle('Exceso de homicidios: 2020 vs Promedio 5 años anteriores', fontsize=18, weight='bold')
plt.xticks(rotation=45)
plt.legend()
plt.gcf().text(0.55, 0.15, '@JairoTorregrose - datos.gov.co', fontsize=10)
plt.show()

prom['Cambio'] = (prom['2020'] - prom['Prom-5A'])/prom['Prom-5A'] * 100

