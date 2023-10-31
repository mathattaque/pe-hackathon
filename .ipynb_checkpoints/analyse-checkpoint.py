# ### Apple

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_apple=pd.read_csv("apple_doc.csv")
df_apple.head()

df_apple.columns

from datetime import datetime

df_apple['Date']=pd.to_datetime(df_apple['Date'], format='%m/%d/%Y')
df_apple.dtypes

df_apple.head()

df_apple.shape

df_applec=df_apple[df_apple["Date"].notna()]
df_applec.shape

df_apple.set_index('Date', inplace=True)

df_apple.sort_values(by=['Date'], inplace=True)
df_apple

df_apple.columns

new_col=["Fin", "Volume", "Début", "Maxi", "Mini"]
df_apple.columns=new_col
df_apple

df_apple['Fin'] = df_apple['Fin'].str.replace('$', '')
df_apple['Maxi'] = df_apple['Maxi'].str.replace('$', '')
df_apple['Mini'] = df_apple['Mini'].str.replace('$', '')
df_apple['Début'] = df_apple['Début'].str.replace('$', '')
#df_apple.drop("(Fin, Début, Maxi, Mini)", axis='columns')
df_apple

df_apple['Maxi']=df_apple['Maxi'].astype("float64")
df_apple['Mini']=df_apple['Mini'].astype("float64")
df_apple['Début']=df_apple['Début'].astype("float64")
df_apple['Fin']=df_apple['Fin'].astype("float64")
df_apple.dtypes

# %matplotlib ipympl

plt.style.use('seaborn-v0_8')
sns.set(rc={'figure.figsize': (8, 4)})

df_apple[['Volume']].plot()

df_apple[['Maxi', 'Mini']].plot()

df_apple[['Début', 'Fin']].plot()

df_apple["Moyenne"]=(df_apple["Maxi"]+df_apple["Mini"])/2
df_apple

df_apple[['Moyenne']].plot()

df_apple["Croissance%"]=100*df_apple["Moyenne"].pct_change(periods=1)
df_apple

(df_apple.tail(50))[['Croissance%']].plot()
