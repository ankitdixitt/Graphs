#!/usr/bin/env python
# coding: utf-8

# In[1]:


import fcsparser
data=fcsparser.parse("C:\\Users\\ankit\\OneDrive\\Desktop\\JR_ADS_PC_D9_1.fcs")
import pandas as pd
import numpy as np
get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


data=fcsparser.parse('C:\\Users\\ankit\\OneDrive\\Desktop\\JR_ADS_PC_D9_1.fcs',meta_data_only=True)
data, df = fcsparser.parse('C:\\Users\\ankit\\OneDrive\\Desktop\\JR_ADS_PC_D9_1.fcs', meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse('C:\\Users\\ankit\\OneDrive\\Desktop\\JR_ADS_PC_D9_2.fcs',meta_data_only=True)
data2, df2 = fcsparser.parse('C:\\Users\\ankit\\OneDrive\\Desktop\\JR_ADS_PC_D9_2.fcs', meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse('C:\\Users\\ankit\\OneDrive\\Desktop\\JR_ADS_PC_D9_3.fcs',meta_data_only=True)
data3, df3 = fcsparser.parse('C:\\Users\\ankit\\OneDrive\\Desktop\\JR_ADS_PC_D9_3.fcs', meta_data_only=False, reformat_meta=True)
#concatenating the dataframes
df_final=pd.concat([df,df2,df3])
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#D3

data=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D3_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D3_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D3_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D3_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D3_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D3_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_RS_D3',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D3_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D3_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D3_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D3_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D3_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D3_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_RS_D3',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D3_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D3_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D3_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D3_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D3_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D3_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_PC_D3',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D3_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D3_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D3_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D3_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D3_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D3_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_PC_D3',alpha=0.6,data=df_final)


# In[4]:


#D6

data=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D6_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D6_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D6_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D6_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D6_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D6_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_RS_D6',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D6_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D6_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D6_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D6_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D6_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D6_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_RS_D6',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D6_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D6_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D6_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D6_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D6_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D6_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_PC_D6',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D6_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D6_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D6_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D6_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D6_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D6_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_PC_D6',alpha=0.6,data=df_final)


# In[5]:


#D9

data=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D9_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D9_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D9_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D9_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D9_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D9_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_RS_D9',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D9_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D9_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D9_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D9_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D9_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D9_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_RS_D9',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D9_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D9_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D9_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D9_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D9_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D9_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_PC_D9',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D9_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D9_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D9_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D9_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D9_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D9_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_PC_D9',alpha=0.6,data=df_final)


# In[6]:


#D12

data=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D12_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D12_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D12_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D12_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D12_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D12_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_RS_D12',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D12_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D12_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D12_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D12_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D12_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D12_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_RS_D12',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D12_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D12_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D12_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D12_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D12_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D12_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_PC_D12',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D12_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D12_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D12_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D12_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D12_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D12_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_PC_D12',alpha=0.6,data=df_final)


# In[7]:


#D15

data=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D15_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D15_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D15_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D15_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D15_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D15_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_RS_D15',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D15_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D15_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D15_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D15_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D15_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D15_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_RS_D15',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D15_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D15_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D15_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D15_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D15_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D15_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_PC_D15',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D15_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D15_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D15_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D15_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D15_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D15_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_PC_D15',alpha=0.6,data=df_final)


# In[8]:


#D18

data=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D18_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D18_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D18_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D18_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D18_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D18_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_RS_D18',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D18_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D18_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D18_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D18_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D18_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D18_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_RS_D18',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D18_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D18_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D18_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D18_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D18_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D18_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_PC_D18',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D18_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D18_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D18_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D18_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D18_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D18_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_PC_D18',alpha=0.6,data=df_final)


# In[9]:


#D21

data=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D21_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D21_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D21_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D21_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D21_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D21_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_RS_D21',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D21_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D21_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D21_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D21_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D21_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D21_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_RS_D21',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D21_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D21_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D21_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D21_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D21_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D21_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_PC_D21',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D21_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D21_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D21_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D21_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D21_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D21_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_PC_D21',alpha=0.6,data=df_final)


# In[10]:


#D24

data=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D24_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D24_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D24_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D24_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D24_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D24_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_RS_D24',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D24_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D24_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D24_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D24_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D24_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D24_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_RS_D24',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D24_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D24_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D24_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D24_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D24_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D24_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_PC_D24',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D24_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D24_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D24_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D24_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D24_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D24_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_PC_D24',alpha=0.6,data=df_final)


# In[11]:


#D27

data=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D27_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D27_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D27_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D27_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D27_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D27_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_RS_D27',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D27_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D27_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D27_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D27_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D27_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D27_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_RS_D27',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D27_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D27_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D27_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D27_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D27_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D27_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_PC_D27',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D27_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D27_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D27_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D27_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D27_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D27_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_PC_D27',alpha=0.6,data=df_final)


# In[12]:


#D30

data=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D30_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D30_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D30_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D30_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D30_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D30_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_RS_D30',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D30_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D30_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D30_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D30_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D30_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D30_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_RS_D30',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D30_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D30_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D30_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D30_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D30_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D30_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_PC_D30',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D30_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D30_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D30_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D30_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D30_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D30_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_PC_D30',alpha=0.6,data=df_final)


# In[13]:


#D33

data=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D33_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D33_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D33_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D33_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D33_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D33_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_RS_D33',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D33_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D33_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D33_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D33_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D33_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D33_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_RS_D33',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D33_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D33_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D33_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D33_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D33_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D33_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_PC_D33',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D33_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D33_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D33_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D33_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D33_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D33_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_PC_D33',alpha=0.6,data=df_final)


# In[14]:


#D36

data=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D36_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D36_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D36_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D36_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D36_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D36_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_RS_D36',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D36_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D36_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D36_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D36_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D36_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D36_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_RS_D36',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D36_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D36_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D36_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D36_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D36_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D36_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_PC_D36',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D36_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D36_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D36_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D36_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D36_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D36_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_PC_D36',alpha=0.6,data=df_final)



# In[15]:


#D39

data=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D39_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D39_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D39_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D39_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D39_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D39_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_RS_D39',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D39_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D39_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D39_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D39_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D39_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D39_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_RS_D39',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D39_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D39_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D39_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D39_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D39_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D39_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_PC_D39',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D39_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D39_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D39_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D39_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D39_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D39_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_PC_D39',alpha=0.6,data=df_final)


# In[16]:


#D42

data=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D42_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D42_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D42_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D42_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D42_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D42_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_RS_D42',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D42_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D42_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D42_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D42_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D42_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D42_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_RS_D42',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D42_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D42_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D42_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D42_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D42_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D42_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_PC_D42',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D42_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D42_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D42_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D42_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D42_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D42_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_PC_D42',alpha=0.6,data=df_final)


# In[17]:


#D45

data=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D45_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D45_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D45_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D45_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_RS_D45_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_RS_D45_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_RS_D45',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D45_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D45_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D45_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D45_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D45_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_RS_D45_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_RS_D45',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D45_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D45_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D45_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D45_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_PC_D45_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_PC_D45_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='CD_PC_D45',data=df_final)

data=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D45_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D45_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D45_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D45_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D45_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_PC_D45_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',label='ADS_PC_D45',alpha=0.6,data=df_final)


# In[18]:


#IND0
data=fcsparser.parse("D:\\FCS files\\JR_ADS_IND0_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_IND0_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_IND0_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\FCS files\JR_ADS_IND0_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_IND0_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_IND0_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',color='red',data=df_final)


# In[19]:


#IND0
data=fcsparser.parse("D:\\FCS files\\JR_CD_IND0_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_IND0_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_IND0_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\FCS files\JR_CD_IND0_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_IND0_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_IND0_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 40000000)
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',color='AQUA',data=df_final)


# In[22]:


fig, ax = plt.subplots()
ax.set_xlim(0, 40000000)
ax.set_ylim(0, 50000000)
data=fcsparser.parse("D:\\FCS files\\JR_CD_IND0_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_CD_IND0_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_CD_IND0_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\FCS files\JR_CD_IND0_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_CD_IND0_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_CD_IND0_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])

sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',color='AQUA',data=df_final)
data=fcsparser.parse("D:\\FCS files\\JR_ADS_IND0_1.fcs",meta_data_only=True)
data, df = fcsparser.parse("D:\\FCS files\\JR_ADS_IND0_1.fcs", meta_data_only=False, reformat_meta=True)
data2=fcsparser.parse("D:\\FCS files\\JR_ADS_IND0_2.fcs",meta_data_only=True)
data2, df2 = fcsparser.parse("D:\FCS files\JR_ADS_IND0_2.fcs", meta_data_only=False, reformat_meta=True)
data3=fcsparser.parse("D:\\FCS files\\JR_ADS_IND0_3.fcs",meta_data_only=True)
data3, df3 = fcsparser.parse("D:\\FCS files\\JR_ADS_IND0_3.fcs", meta_data_only=False, reformat_meta=True)
df_final=pd.concat([df,df2,df3])
sns.set(style='white')
sns.scatterplot(x='FSC-A',y='SSC-A',color='red',data=df_final)


# In[ ]:




