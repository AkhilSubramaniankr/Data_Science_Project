#!/usr/bin/env python
# coding: utf-8

# In[3]:


###Importing libraries


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


data = pd.read_csv('telecomdata.csv')


# In[5]:


data


# In[6]:


data.head()


# In[7]:


data.info()


# In[8]:


data.shape


# In[9]:


data.nunique()


# In[12]:


data.dtypes


# In[13]:


data.columns


# In[15]:


data.describe()


# In[16]:


data.describe(include='object')


# In[17]:


###Checking Missing Values


# In[18]:


data.head(2)


# In[20]:


data.isnull().sum()


# In[22]:


data.notnull().sum()


# In[23]:


data[data.duplicated()]


# ## Analysing the 'churn' variable

# In[24]:


data.head()


# In[25]:


data['churn'].unique()


# In[26]:


A = data['churn'].value_counts()
print(A)


# In[27]:


str(483/3333*100) + "%"


# In[29]:


type(A)


# ## Donut Chart

# In[41]:


plt.pie(A, labels = ['Not Churned', 'Churned'], colors = ['red', 'yellow'], startangle = 50, shadow = True, radius = 2, explode = (0,0.2), autopct = '%1.2f%%', pctdistance = 0.75);

circle = plt.Circle((0,0), 1, color = 'white')
c = plt.gcf()

c.gca().add_artist(circle)

plt.title("Churned VS Non-Churned Customers (DSL)")
plt.show()


# ## Countplot 

# In[46]:


sns.countplot(x ='churn', data = data)
plt.show()


# ## Analyzing the 'State' Variable
# 

# In[47]:


data.head(2)


# In[48]:


data.state.nunique()


# In[49]:


data.state.value_counts()


# ### Countplot

# In[55]:


plt.figure(figsize=(20,7))

sns.countplot(x='state', data=data)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.xlabel('States', fontsize=20, color='Red')
plt.ylabel('Count', fontsize=20, color='Red')

plt.show()


# In[63]:


#Showing Churn/Not-Churn State-Wise

sns.set(style="whitegrid")

plt.figure(figsize=(20,7))

sns.countplot(x = data.state, hue = data.churn)

plt.xlabel('States', fontsize=18, color='Red')
plt.ylabel('Count', fontsize=18, color='Red')

plt.show()


# In[62]:


data.head(2)


# In[64]:


a = data.groupby("state")['churn'].mean()*100

a.sort_values()


# ### Line Chart

# In[73]:


X  = data.state.unique()
Y = data.groupby("state")['churn'].mean()

sns.set(style="darkgrid")

plt.rcParams['figure.figsize'] = (20,7)

plt.rcParams['lines.linestyle'] = '-'

plt.plot(X, Y, color = 'Black', marker = '*', markersize = '10')

plt.title("State Churn Graph", fontsize = 25, color='Red')
plt.xlabel('States', fontsize=20, color='Red')
plt.ylabel('Churn Rate', fontsize=20, color='Red')

plt.show()


# In[75]:


data.groupby("state")['churn'].mean().sort_values(ascending = False).head(5)*100


# In[76]:


data.head()


# In[77]:


c = pd.crosstab(data.state, data.churn, margins = True)

c['percentage_churn'] = c[True]/(c['All'])*100

print(c.head())
print(type(c))


# In[78]:


c.info()


# In[79]:


c.sort_values(by='percentage_churn', ascending = False).head()


# ## Analyzing the 'Area Code' Column
# 

# In[80]:


data.head()


# In[81]:


data['area code'].nunique()


# In[82]:


data['area code'].unique()


# In[83]:


data['area code'].value_counts()


# In[84]:


data.groupby('area code')['churn'].mean()*100


# In[85]:


d = pd.crosstab(data['area code'], data['churn'], margins = True)

d['Churn Percentage'] = d[True]/d['All']*100

d


# In[91]:


plt.figure(figsize = (14,5))

sns.countplot(x = 'area code', hue = 'churn', data = data)
plt.show()


# ## Analyzing the "Account Length' Column

# In[92]:


data.head()


# In[93]:


data['account length'].nunique()


# In[95]:


data['account length'].value_counts()


# In[96]:


data.groupby('account length')['churn'].mean()*100


# In[97]:


churn_data = data[data['churn'] == True]

not_churn_data = data[data['churn'] == False]


# In[99]:


churn_data.head(2)


# In[100]:


not_churn_data.head(2)


# In[101]:


churn_data.info()


# In[102]:


not_churn_data.info()


# In[103]:





# ### Histogram

# In[110]:


sns.histplot(data['account length'], color = 'blue')
plt.xlabel("Account Length", fontsize = 15)
plt.ylabel("Density", fontsize = 15)
plt.show()


# ### Distribution Plot 

# In[113]:


sns.distplot(data['account length'], color = 'blue')
plt.xlabel("Account Length", fontsize = 15)
plt.ylabel("Density", fontsize = 15)
plt.show()


# In[131]:


sns.distplot(data['account length'], color='blue', label = 'All')

sns.distplot(churn_data['account length'], color='red', hist= False, label='Churned')

sns.distplot(not_churn_data['account length'], color='yellow', hist= False, label='Not Churned')

plt.xlabel("Account Length", fontsize=15)
plt.ylabel("Density", fontsize=15)
plt.rcParams['figure.figsize'] = (15,7);

plt.legend()

plt.show()


# ## Analyzing the 'International Plan' Column

# In[132]:


data.head()


# In[133]:


data['international plan'].unique()


# In[134]:


data['international plan'].value_counts()


# In[135]:


yes_int_plan = data[(data['international plan'] == 'yes') & (data['churn'] == True)]
yes_int_plan


# In[137]:


no_int_plan = data[(data['international plan'] == 'no') & (data['churn'] == True)]
no_int_plan


# In[138]:


137/323*100


# In[139]:


346/3010*100


# In[140]:


int_plan_data = pd.crosstab(data['international plan'], data['churn'], margins = True)
int_plan_data


# In[141]:


int_plan_data['churn percent'] = int_plan_data[True]/int_plan_data['All']*100
int_plan_data


# In[142]:


int_plan_data.info()


# In[143]:


i = data['international plan'].value_counts()
i


# ### Donut Chart

# In[144]:


plt.pie(i, labels = ['No', 'Yes'], colors = ['red', 'cyan'], startangle = 50, shadow = True, radius = 2, explode = (0,0.2), autopct = '%1.2f%%', pctdistance = 0.75);

circle = plt.Circle((0,0), 1, color = 'white')
c = plt.gcf()

c.gca().add_artist(circle)

plt.title("International Plan (DSL)")
plt.rcParams['figure.figsize'] = (5,7)
plt.show()


# In[146]:


sns.countplot(x = 'international plan', hue = 'churn', data = data)
plt.rcParams['figure.figsize'] = (10,4)
plt.show()


# ## Analyzing the 'Voice Mail Plan' Column

# In[147]:


data.head()


# In[151]:


sns.countplot(x = 'voice mail plan', hue = 'churn', data = data)
plt.rcParams['figure.figsize'] = (10,5)
plt.show()


# In[152]:


vmplan = pd.crosstab(data['voice mail plan'], data['churn'], margins=True)
vmplan


# In[153]:


vmplan['churn percent'] = vmplan[True]/vmplan['All']*100
vmplan


# In[154]:


data['voice mail plan'].unique()


# In[155]:


data['voice mail plan'].value_counts()


# In[158]:


plt.pie(i, labels = ['No', 'Yes'], startangle = 90, shadow = True, radius = 1.5, explode = (0,0.1), autopct = '%1.2f%%', pctdistance = 0.75);

circle = plt.Circle((0,0), 0.8, color = 'white')
c = plt.gcf()

c.gca().add_artist(circle)

plt.title("Voice Mail Plan (DSL)")
plt.show()


# ## Analysing the 'Number Vmail Message' Column
# 

# In[10]:


data.head()


# In[11]:


data['number vmail messages'].unique()


# In[12]:


data['number vmail messages'].value_counts().head()


# In[13]:


data['number vmail messages'].describe()


# ### Distribution Plot

# In[14]:


sns.distplot(data['number vmail messages']);


# ### Box Plot 

# In[15]:


sns.boxplot(x='churn', y='number vmail messages', color='violet', meanline=True, sym='r+', data=data)

plt.figure(figsize = (5, 5))
plt.show()


# ## Analyzing the 'Customer Service Calls' Column

# In[16]:


data.head()


# In[17]:


data['customer service calls'].nunique()


# In[18]:


data['customer service calls'].unique()


# In[19]:


data['customer service calls'].value_counts()


# In[20]:


churn_data = data[data['churn']]
churn_data


# In[21]:


churn_data['customer service calls'].value_counts()


# In[22]:


cscalls = pd.crosstab(data['customer service calls'], data['churn'], margins=True)

cscalls['churn percent'] = cscalls[True] / cscalls['All'] * 100

cscalls


# ### Count Plot

# In[24]:


sns.countplot(x='customer service calls', hue='churn', color='brown', data=data)

plt.show()


# ## Analyzing the 'Per Minute Charge' 

# In[25]:


data.head()


# In[29]:


data.columns


# In[32]:


dc_pm = data['total day charge'].mean()/data['total day minutes'].mean()

ec_pm = data['total eve charge'].mean()/data['total eve minutes'].mean()

nc_pm = data['total night charge'].mean()/data['total night minutes'].mean()

intl_pm = data['total intl charge'].mean()/data['total intl minutes'].mean()

print(dc_pm)
print(ec_pm)
print(nc_pm)
print(intl_pm)


# ### Bar Plot

# In[34]:


sns.barplot(x=['day', 'evening', 'night', 'intl'], y=[dc_pm, ec_pm, nc_pm, intl_pm])

plt.show()


# In[ ]:




