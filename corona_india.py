import pandas as pd
import requests
import datetime
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
from scipy.special import factorial
from scipy.stats import poisson

dtime=datetime.datetime.now()
res = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vSc_2y5N0I67wDU38DjDh35IZSIS30rQf7_NYZhtYYGU1jJYT6_kDx4YpF-qw0LSlGsBYP8pqM_a1Pd/pubhtml")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0]
df = pd.read_html(str(table))[0]
print(df)
'''
print(df['Date'][0])
plt.plot(df['Change in Total'],'.-r')
plt.title('Stats from '+ str(df['Date'][len(df)-1])+' to '+str(df['Date'][0]))
plt.gca().invert_xaxis()
plt.show()
'''
df.to_csv (r'corona_india_'+str(dtime.date())+'.csv', index = False, header=True)
