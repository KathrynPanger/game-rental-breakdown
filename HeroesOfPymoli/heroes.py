#!/usr/bin/env python
# coding: utf-8

# In[51]:


################################################################
#This file will summarize data from the "Heros of Pamoli" game#
###############################################################


# In[52]:


#import dependencies
import pandas as pd
import numpy as np


# In[53]:


#read the master data file and create a dataframe
masterFile = "Resources/purchase_data.csv"
master_df = pd.read_csv(masterFile)
master_df.head()


# In[54]:


#create the age group category for later and add to dataframe, completing my master dataframe
bins=[0,9,14,19,24,29,34,39,400]
labels=["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]
master_df["Age Group"] = pd.cut(master_df["Age"], bins, labels=labels, include_lowest=True)


# In[55]:


#Create a dataframe to display total number of players
unique_players=master_df["SN"].unique()
total_players=np.count_nonzero(unique_players)
total_players_df =pd.DataFrame([
    {"Total Players":total_players}])
total_players_df


# In[56]:


#Create a dataframe to display basic info about purchases
unique_items=master_df["Item Name"].unique()
total_unique_items=np.count_nonzero(unique_items)
average_price=master_df["Price"].mean()
total_purchases=master_df["Purchase ID"].count()
total_revenue=master_df["Price"].sum()

basic_info = pd.DataFrame([
        {"Number of Unique Items": total_unique_items,
         "Average Price":average_price,
         "Number of Purchases": total_purchases,
         "Total Revenue": total_revenue}
    ])
basic_info


# In[57]:


#create a dataframe to display the gender breakdown of players
unique_sn_df = master_df.drop_duplicates(subset='SN', keep="first")
male_players = unique_sn_df.loc[master_df["Gender"] == "Male", "Gender"]
female_players = unique_sn_df.loc[master_df["Gender"] == "Female", "Gender"]
other_players = unique_sn_df.loc[master_df["Gender"] == "Other / Non-Disclosed", "Gender"]

playerCount_df = pd.DataFrame({ 
    "Gender": ["Female", "Male", "Other"],
    "Total Count": [female_players.count(), male_players.count(), other_players.count()],
   })

percent_gender = playerCount_df["Total Count"]/total_players*100
playerCount_df["Percentage of Players"] = percent_gender

playerCount_df


# In[58]:


#Create a table of summary statistics concerning Male and Female purchases

# Use GroupBy to get most of our Gender data
grouped_gender_df = master_df.groupby(['Gender'])

#Get our data functions from grouped gender data
gender_priceMean=grouped_gender_df["Price"].mean()
gender_purchaseCount=grouped_gender_df["Purchase ID"].count()
gender_totalvalue=grouped_gender_df["Price"].sum()

#### Get the average total purchase per person. I know there's an easier way to do this, but I haven't found it yet.
#Get female average spent per person
female_df=master_df.loc[master_df["Gender"]=="Female", :] #dataset of only females
grouped_gender_sn_df = female_df.groupby(['SN'])
F_total_purchase_per=grouped_gender_sn_df["Price"].sum()
F_total_purchase_per.mean()

#Get male average spent per person
male_df=master_df.loc[master_df["Gender"]=="Male", :] #dataset of only Males
grouped_gender_sn_df = male_df.groupby(['SN'])
M_total_purchase_per=grouped_gender_sn_df["Price"].sum()
M_total_purchase_per.mean()

#Get other gender average spent per person
other_df=master_df.loc[master_df["Gender"]=="Other / Non-Disclosed", :] #dataset of only Others
grouped_gender_sn_df = other_df.groupby(['SN'])
O_total_purchase_per=grouped_gender_sn_df["Price"].sum()
O_total_purchase_per.mean()

#Put these in a list
avg_total_list=[F_total_purchase_per.mean(), M_total_purchase_per.mean(),O_total_purchase_per.mean()]
####

#Put everything in a dataframe
gender_stats_df = pd.DataFrame({"Purchase Count": gender_purchaseCount,
                                "Average Purchase Price": gender_priceMean,
                                "Total Purchase Value": gender_totalvalue,
                               "Average Total Purchase per Person": avg_total_list})

gender_stats_df


# In[59]:


#Create a table of summary statistics for players of different age ranges

master_df["Age Group"] = pd.cut(master_df["Age"], bins, labels=labels, include_lowest=True)
age_group_df=unique_sn_df.groupby("Age Group")
age_count=age_group_df["Purchase ID"].count()
age_percent =age_count/total_players
age_df = pd.DataFrame({"Total Count":age_count,
                      "Percentage of Players":age_percent})
age_df


# In[60]:


#Create Chart of Top Spenders

master_df["count"]=1
grouped_SN=master_df.groupby(["SN"])
countsum=grouped_SN.sum()
sorted_countsum=countsum.sort_values(["Price","SN"], ascending=False)
price=sorted_countsum["Price"]
count=sorted_countsum["count"]
sorted_countsum["Average Purchase Price"]=price/count
sorted_countsum["Total Purcase Value"]=price*count
top_spenders = sorted_countsum.reset_index(drop=False)
top_spenders = top_spenders.rename(columns={"count":"Purchase Count"})
top_spenders_cleaned=top_spenders.drop(['Item ID','Purchase ID', 'Age','Price'], axis=1)
top_spenders_cleaned.head()


# In[61]:


#Most Popular Items


# In[62]:


master_df.head()


# In[86]:


MP_reduced=master_df[["Item Name", "count", "Price"]]


# In[87]:


#MP_price=MP_reduced["Price"]
#MP_price


# In[88]:


MP_reduced_renamed =MP_reduced.rename(columns={"count":"Purchase Count", "Price":"Total Purchase Value"})


# In[82]:





# In[89]:


MP_grouped=MP_reduced_renamed.groupby(["Item Name"])


# In[90]:


MP_groupedbysum=MP_grouped.sum()


# In[91]:


MP_base = MP_groupedbysum.reset_index(drop=False)


# In[68]:


#MP_price =MP_base["Item Price"]


# In[69]:


#MP_total_purchase = MP_base["Purchase Count"]*MP_price


# In[70]:


#MP_base["Total Purchase Value"] = MP_total_purchase


# In[97]:


MP_purchase=MP_base.sort_values(["Total Purchase Value"], ascending=False)


# In[98]:


MP_purchase


# In[100]:


#MP_items=MP_purchase["Item Name"]


# In[103]:


#MP_purchaseCount=MP_purchase["Purchase Count"]


# In[ ]:


#MP_price=MP_reduced["Price"]


# In[104]:


#MP_total_purchase_value=MP_purchase["Total Purchase Value"]


# In[106]:


#MP_final = pd.DataFrame([
        {"Item Name": MP_items,
         "Average Purchase Price":MP_price,
         "Total Purcase Value": MP_total_purchase_value}])


# In[107]:


#MP_final


# In[ ]:




