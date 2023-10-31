#But du programme : un investisseur investit son capital en 2010 dans 10 grandes 
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


invest = np.array([10,10,10,10,10,10,10,10,10,10],dtype = float)   #liste contenant les investissements initiaux en $ pour [appl, sbux, msft, csco, qcom, meta, amzn, tsla, amd, nflx]
final = np.zeros(10, dtype = float) #liste qui contiendra l'argent en $ par entreprise le 30/10/23
company = [appl, sbux, msft, csco, qcom, meta, amzn, tsla, amd, nflx] #liste des entreprises

#on regarde l'évolution du capital de l'investisseur entre le 1er janvier 2010 et aujourd'hui :

for i in range (len(company)):        
    company[i]['Date'] = pd.to_datetime(company[i]["Date"])
    company[i].set_index('Date', inplace=True)
    rapport = company[i].iloc["2023-10-30", 5]/company[i].loc["2010-01-01", 5]
    final[i] = invest[i] * rapport

print(final_sum())       #Ici l'argent a fructifié (ou non)




