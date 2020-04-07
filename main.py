import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



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
    diseases_list.append(cols[3].split(","))


data_dict={'age':age_list,'sex':sex_list,'diseases':diseases_list}
#betegsegek
flat_list = [item for sublist in diseases_list for item in sublist]
all_dis=list(dict.fromkeys(flat_list))
# print(len(all_dis))

numbers_of_dis=[]
for dis in all_dis:
    numbers_of_dis.append(flat_list.count(dis))

data = dict(zip(all_dis, numbers_of_dis))

# print(data)
#kor
all_age=list(dict.fromkeys(age_list))

numbers_of_age=[]
for element in all_age:
    numbers_of_age.append(all_age.count(element))

#data_age = dict(zip(all_age, numbers_of_age))



#kirajzolasok
#1 betegsegek
plt.bar(range(len(data)), list(data.values()), align='center' )
plt.xticks(range(len(data)), list(data.keys()))
plt.xticks(rotation=-90)

#2 nemek
labels=["Férfi","Nő"]
sizes=[sex_list.count("Férfi"),sex_list.count("Nő")]
fig1, ax1 = plt.subplots()
ax1.pie(sizes,labels=labels, autopct='%1.1f%%',startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#3 kor
fig3, ax3 = plt.subplots()
ax3.pie(numbers_of_age,labels=all_age, autopct='%1.1f%%',startangle=90)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.





#4 betegsegek szama
pd_data=pd.DataFrame(data_dict)


pd_data['Betegseg szam'] = pd_data.diseases.apply(lambda x: len(x))
print(pd_data)

count_of_dis=list(dict.fromkeys(pd_data['Betegseg szam']))

print(count_of_dis)



numbers_of_dis=[]
for element in pd_data["Betegseg szam"]:
    numbers_of_dis.append(element)


print(numbers_of_dis)
# print(count_of_dis)
# fig4,ax4=plt.subplots()
# ax4.pie(numbers_of_dis,labels=count_of_dis, autopct='%1.1f%%',startangle=90)
# ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.




# plt.show()



