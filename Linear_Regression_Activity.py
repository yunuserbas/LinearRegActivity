#!/usr/bin/env python
# coding: utf-8

# In[17]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import statsmodels.api as sm
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


df = pd.read_csv(r'C:\Users\yunus\Downloads\cereal.csv')

df


# In[15]:


print(df.isnull().sum())


# In[7]:


df.describe()


# In[64]:


df[['sugars','vitamins']].plot(kind='bar',color=['green','orange'])
plt.xlabel('cereals')
plt.ylabel('bins')
plt.show()


# In[63]:


conditions = [(df['mfr'] == 'N'),
    (df['mfr'] == 'Q'), (df['mfr'] == 'K'),
    (df['mfr'] == 'R'), (df['mfr'] == 'G'), (df['mfr'] == 'P'),
    (df['mfr'] == 'A')]
choices = ['Nabisco','Qualer Oats','Kellogs','Raslston Purina','General Mills','Post','American Home Foods Products']
df['full name'] = np.select(conditions,choices, default=0)
print(df)       


# In[61]:


sns.countplot(y='full name', data = df)
plt.show()


# In[29]:


y = df['rating']
x = df[['calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo', 'sugars', 'potass', 'vitamins', 'shelf', 'weight', 'cups']]
x.shape, y.shape


# In[40]:


mod = sm.OLS(y, x)
res = mod.fit()

print(res.summary())


# In[50]:


sns.lmplot(x='rating', y='sugars', data = df)
sns.lmplot(x='rating', y='vitamins', data = df)


# In[24]:


corr = df.corr(method='pearson')
corr


# In[ ]:




