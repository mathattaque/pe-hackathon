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

# ### Microsoft

import pandas as pd
import seaborn as sns

df=pd.read_csv('microsoft_doc.csv')

df.head(10)

from datetime import datetime
df['Date']=pd.to_datetime(df['Date'], format='%m/%d/%Y')

# +
df.rename(columns={    "Volume": "nb actions","Open":"début","High":"max","Low":"min","Close/Last":"Fin"
    
}, inplace=True)
# -

df.set_index('Date', inplace=True)

df.head(3)

# On veut analyser l'évolution du prix de l'action en début de journée: on récupère alors la colonne début

prix=df["début"]

prix.head(4)

df.sort_values(by=["Fin"]).tail(3)

# Le maximum du prix de l'action en fin de journée les 10 dernières années  a eu lieu le 18 juillet en 2023

df.dtypes


# A cause des dollars, les types des colonnes sont des objets. On va donc changer leur type pour travailler sur ces données

df['Fin'] = df['Fin'].str.replace('$', '')

df['Fin']=df['Fin'].astype("float64")

df['début'] = df['début'].str.replace('$', '')
df['max'] = df['max'].str.replace('$', '')
df['min'] = df['min'].str.replace('$', '')
df['début']=df['début'].astype("float64")
df['max']=df['max'].astype("float64")
df['min']=df['min'].astype("float64")

df.dtypes

# +
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
sns.set(rc={'figure.figsize': (8,4)})
df[['max','min','début','Fin']].plot()
# -

df['nb actions'].plot()

df["Moyenne"]=(df["max"]+df["min"])/2

df["evol%"]=100*df["Moyenne"].pct_change(periods=1)
df

(df.head(100))["evol%"].plot()

# On a donc étudié les variations de la moyenne du prix de l'action depuis 100 jours


