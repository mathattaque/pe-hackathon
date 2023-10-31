# But du programme : un investisseur investit son capital en 2010 dans 10 grandes 
# entreprises du NASDAQ, on cherche à connaître la valeur de son portefeuille aujourd'hui


import pandas as pd 
import numpy as np
from datetime import datetime

appl = pd.read_csv('apple_doc.csv')
sbux = pd.read_csv('starbucks_doc.csv')
msft = pd.read_csv('microsoft_doc.csv')
csco = pd.read_csv('csco_doc.csv')
qcom = pd.read_csv('qcom_doc.csv')
meta = pd.read_csv('meta_doc.csv')
amzn = pd.read_csv('amazon_doc.csv')
tsla= pd.read_csv('tesla_doc.csv')
amd = pd.read_csv('amd_doc.csv')
nflx = pd.read_csv('netflix_doc.csv')
appl.dtypes


# +
invest = np.array([10,10,10,10,10,10,10,10,10,10],dtype = float)   #liste contenant les investissements initiaux en $ pour [appl, sbux, msft, csco, qcom, meta, amzn, tsla, amd, nflx]
final = np.zeros(10, dtype = float) #liste qui contiendra l'argent en $ par entreprise le 30/10/23
company = [appl, sbux, msft, csco, qcom, meta, amzn, tsla, amd, nflx] #liste des entreprises

appl.head()
# -

for x in company:
    x['Date'] = pd.to_datetime(x['Date'])   ##on transforme toutes les dates en datetime

for x in company:
    x['Close/Last'] = x['Close/Last'].str.replace('$', '')  ##on enlève les $ qui nous gêne 
    x['High'] = x['High'].str.replace('$', '')
    x['Low'] = x['Low'].str.replace('$', '')
    x['Open'] = x['Open'].str.replace('$', '')

appl.head()  ##on vérifie les modifs 

for x in company:
    x['Close/Last'] = x['Close/Last'].astype(float)  ##on modifie en float les nombres qui étaient considérés comme des str  
    x['High'] = x['High'].astype(float)
    x['Low'] = x['Low'].astype(float)
    x['Open'] = x['Open'].astype(float)

appl.dtypes

appl.dtypes  ##on vérifie l'opération

sbux.head()

# on regarde l'évolution du capital de l'investisseur entre le 31 octobre 2013 et aujourd'hui :

for i in range (0,len(company)):        
    company[i].set_index('Date', inplace=True)

for i in range(len(company)):
    rapport = company[i].loc["2023-10-30", 'Low']/company[i].loc["2013-10-31", 'Low']
    final[i] = invest[i] * rapport

# +
S=0
for x in final:
    S+=x
    
print(S)
# -






