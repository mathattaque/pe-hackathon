# # Analyse

# Ici, nous allons mener une analyse graphique du cours de la bourse de deux entreprises américaines : Apple et Microsoft. Nous étudierons d'abord indépendamment chaque entreprise avant de confonter leurs statistiques propres dans une dernière partie.

# ### Apple

# Ici, on cherchera à mener une analyse graphique du cours de la bourse de l'entreprise américaine Apple pendant les dernières années. En particulier on devra apporter des modifications (formats, noms, tri..) au dataframe obtenu à partir d'un fichier au format .csv téléchargé sur le site nasdaq.com 

# +
#on importe les bibliothèques nécessaires à notre étude 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# +
#on créée notre dataframe à partir d'un fichier csv importé sur notre dépôt

df_apple=pd.read_csv("apple_doc.csv")
df_apple.head()

# +
#ici on cherche à convertir la colonne temporelle 'Date' à un format plus pertinent

from datetime import datetime
# -

df_apple['Date']=pd.to_datetime(df_apple['Date'], format='%m/%d/%Y')
df_apple.dtypes

df_apple.head()

df_apple.shape

# +
df_applec=df_apple[df_apple["Date"].notna()]
df_applec.shape

#au vu du résultat obtenu, il n'y a aucun NaN dans le dataframe

# +
#on indexe le dataframe par la colonne 'Date'

df_apple.set_index('Date', inplace=True)

# +
#on trie les lignes du tableau dans l'ordre chronologique

df_apple.sort_values(by=['Date'], inplace=True)
df_apple

# +
#anciens noms des colonnes

df_apple.columns

# +
#on renomme les colonnes

new_col=["Fin", "Volume", "Début", "Maxi", "Mini"]
df_apple.columns=new_col
df_apple

# +
#ici, le caractère du dollar $ nous gêne pour afficher des courbes, nous allons donc le supprimer

df_apple['Fin'] = df_apple['Fin'].str.replace('$', '')
df_apple['Maxi'] = df_apple['Maxi'].str.replace('$', '')
df_apple['Mini'] = df_apple['Mini'].str.replace('$', '')
df_apple['Début'] = df_apple['Début'].str.replace('$', '')
#df_apple.drop("(Fin, Début, Maxi, Mini)", axis='columns')
df_apple

# +
#encore dans le but d'afficher des courbes on modifie le type des colonnes

df_apple['Maxi']=df_apple['Maxi'].astype("float64")
df_apple['Mini']=df_apple['Mini'].astype("float64")
df_apple['Début']=df_apple['Début'].astype("float64")
df_apple['Fin']=df_apple['Fin'].astype("float64")
df_apple.dtypes

# +
#affichage des courbes avec seaborn

plt.style.use('seaborn-v0_8')
sns.set(rc={'figure.figsize': (10, 5)})

# +
#courbe du volume, on observe qu'elle est difficilement exploitable

df_apple[['Volume']].plot()

# +
#affichage du cours de l'action avec minimum journalier et maximum journalier

df_apple[['Maxi', 'Mini']].plot()

# +
#courbe des valeurs de la première action journalière et de la dernière action

df_apple[['Début', 'Fin']].plot()

# +
#on calcule la valeur moyenne journalière de l'action

df_apple["Moyenne"]=(df_apple["Maxi"]+df_apple["Mini"])/2
df_apple

# +
#affichage de la valeur moyenne au cours du temps

df_apple[['Moyenne']].plot()

# +
#ici on cherche à calculer la croissance journalière en pourcentage de la valeur moyenne de l'action 

df_apple["Croissance%"]=100*df_apple["Moyenne"].pct_change(periods=1)
df_apple

# +
#affichage du taux croissance en % au cours des 50 derniers jours

(df_apple.tail(50))[['Croissance%']].plot()
# -

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

sns.displot(data=df.head(100), x="Moyenne",kind="kde")

# J'ai tracé une distribution de la 
# moyenne des actions lors des 100 derniers jours. Je vais la trace pour les 5 derniers années pour comparer les deux distributions

sns.displot(data=df.head(1500), x="Moyenne",kind="kde")

# La distribution est différente et elle est plus décalée vers la gauche ce qui est cohérent avec le graphe qui montre la hausse du prix de l'action.

# ### On va maintenant comparer les deux entreprises



df_tot=pd.merge(df_apple,df,on='Date')

df_tot.head()

df_tot.rename(columns={"Volume":"vol_apple","nb actions":"vol_microsoft","Moyenne_x":"moyenne_apple","Moyenne_y":"moyenne_microsoft"},inplace= True)
df_tot[["vol_apple","vol_microsoft"]].plot()

# Apple vend plus d'actions que microsoft mais la différence de vente d'actions diminue au cours du temps

df_tot[["moyenne_apple","moyenne_microsoft"]].plot()

# Cependant, le prix moyen des actions de microsoft est plus élevé que celui d'apple et la différence du prix moyen augment au cours du temps 


