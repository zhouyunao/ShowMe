
# coding: utf-8

# In[1]:


import csv


csvfile = open('Schedule_E_2017.csv','rb')
lines = csvfile.readlines()
for l in lines:
#     print (l.decode('shift_jis'))
        


# In[2]:


import pandas as pd

df = pd.read_csv('Schedule_E_2017.csv',encoding='shift_jis')
# df


# In[3]:


# df.info()


# In[4]:


grouped = df.groupby('球場')


# In[5]:


# Koboパーク宮城の行を選出    NaN削除
home = df[df.球場=='Koboパーク宮城'].dropna(how='any')


# In[6]:


get_ipython().run_line_magic('matplotlib', '')
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
# font = {'family': 'Rounded Mgen+ 1m medium'}
# matplotlib.rc('font',**font)


# In[7]:


import datetime as dt
date = list()
for d in list(home['日時']):
#     temp = dt.datetime.strptime(d,'%m/%d')
#     temp = temp.replace(year = 2017)
    date.append(d)
# date


# In[8]:


# home


# In[9]:


import matplotlib.ticker as tick


# In[10]:


matplotlib.matplotlib_fname()


# In[11]:


# fig = plt.bar(date,home['観衆'],tick_label = date)
from matplotlib.font_manager import FontProperties

font_path = '/usr/local/share/fonts/rounded-mgenplus-1m-medium.ttf'
font_prop = FontProperties(fname=font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

index = [i for i in range(66)]
plt.bar(index,home['観衆'],color="#FF5B70")
plt.xticks(index,date,rotation=90)
plt.grid(color='gray',linestyle='--')
plt.ylim([20000,28000])
plt.title('Koboパーク客数')
# plt.gca().yaxis.set_minor_locator(tick.MultipleLocator(10))
# plt.tick_params(axis='y',which='minor',width = 0.5, length = 5)
# plt.tick_params(width = 2, length = 10)
# plt.subplots_adjust(hspace=0.7,bottom=0.2)
# fig.xaxis.set_major_locator(matplotlib.mdates.AutoDateLocator)
# fig.xaxis.set_major_formatter(matplotlib.mdates.DateFormatter('%m-%d'))

