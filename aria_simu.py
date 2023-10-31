import pandas as pd 
import numpy as np
import datetime

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

appl['Date'] = pd.to_datetime(appl["Date"])
appl.loc["2023-02-02"]

# +
invest = np.array([10,10,10,10,10,10,10,10,10,10],dtype = float)   #liste contenant les investissements initiaux en $ pour [appl, sbux, msft, csco, qcom, meta, amzn, tsla, amd, nflx]
final = np.zeros(10, dtype = float) #liste qui contiendra l'argent en $ par entreprise le 10/30/23
company = [appl, sbux, msft, csco, qcom, meta, amzn, tsla, amd, nflx]

for i in range (len(company)):
    company[i]['Date'] = pd.to_datetime(company[i]["Date"])
    company[i].set_index('Date', inplace=True)
    rapport = company[i].iloc["2023-10-30", 5]/company[i].loc["2010-01-01", 5]
    final[i] = invest[i] * rapport

print(final)



# -


