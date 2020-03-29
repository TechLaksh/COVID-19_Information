
#World  COVID-19 full complete information.

'''

Auther : Yash
Sorce : 'https://google.org/crisisresponse/covid19-map?hl=en'


'''


import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime,date


now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M:%S")
print("\n\nCurrent Date & Time =", current_time ,end=" ")
print(today)



extract_content = lambda row:[x.text.replace('\n','') for x in row ]

URL = 'https://google.org/crisisresponse/covid19-map?hl=en'

SHORT_HEADERS = ['Location', 'Confirmed cases','Cases per 1M people','Recovered','Deaths']

response = requests.get(URL).content

soup = BeautifulSoup(response,'html.parser')

header = extract_content(soup.tr.find_all('th'))


stats = []

all_data = soup.find_all('tr')

for x in all_data:
    stat = extract_content(x.find_all('td'))
    if stat:
        if len(stat) == 5:
            stat = ['',*stat]
            stats.append(stat)
        elif len(stat) == 6:
            stats.append(stat)





objects = []
for row in stats:
    objects.append(row[1])
y_pos = np.arange(len(objects))

performance = []

for row in stats:
    performance.append(row[2]  + row[3])
table = tabulate(stats,headers=SHORT_HEADERS)
print('\n\n'+table)



'''
For graph:-

plt.barh(y_pos,performance, align='center',alpha=0.5,color=(234/256.0,128/256.0,252/256.0),edgecolor=(106/256.0,27/256.0,154/256.0))

plt.yticks(y_pos,objects)
plt.xlim(1,80)
plt.xlabel('Cases')
plt.title('COVID_19')
plt.show()
'''