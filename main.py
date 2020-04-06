import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# class Beteg(object):
    
#     def __init__(self,sex,age,diseases):
#         self.sex=sex
#         self.age=age
#         self.diseases=diseases.split(',')
        
#     def __str__(self):
#         return '{self.sex} {self.age} {self.diseases}'.format(self=self)
    

    


print("Start")
sex_list=[]
age_list=[]
diseases_list=[]
page = requests.get("https://koronavirus.gov.hu/elhunytak")
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table')
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    sex_list.append(cols[1])
    age_list.append(cols[2])
    diseases_list.append(cols[3])


data={'age':age_list,'sex':sex_list,'diseases':diseases_list}


labels=["Férfi","Nő"]
sizes=[sex_list.count("Férfi"),sex_list.count("Nő")]
fig1, ax1 = plt.subplots()
ax1.pie(sizes,labels=labels, autopct='%1.1f%%',startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

