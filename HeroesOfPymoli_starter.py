
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[311]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[312]:


Total_players=len(purchase_data["SN"].unique())
df=pd.DataFrame({"Total Players": [Total_players]})
df


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[313]:


unique_items=len(purchase_data["Item ID"].unique())
average=purchase_data["Price"].mean()
number_of_purchases=len(purchase_data["Purchase ID"].unique())
total_revenue=purchase_data["Price"].sum()


# In[314]:


Summary_table=pd.DataFrame({"Number of Unique Items":[unique_items],
                            "Average Price":[average],
                            "Number of Purchases":[number_of_purchases],
                            "Total Revenue":[total_revenue]})
Summary_table["Average Price"] = Summary_table["Average Price"].map("${:.2f}".format)
Summary_table["Total Revenue"] = Summary_table["Total Revenue"].map("${:.2f}".format)
Summary_table


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[315]:


Group_Gender=purchase_data.groupby(["Gender"])
print(Group_Gender)
Group_Gender.count()


# In[316]:


Total_count=Group_Gender["Gender"].count()
Sum=Total_count.sum()
Percentage_of_Players=Total_count/Sum*100
Purchase_Count=Group_Gender["Purchase ID"].count()
Average_Purchase_Price=Group_Gender["Price"].mean()
Total_Purchase_Value=Group_Gender["Price"].sum()
Avg_Total_Purchase_per_Person=Total_Purchase_Value.mean()


# 
# ## Purchasing Analysis (Gender)

# In[317]:


Gender_Summary=pd.DataFrame({"Total Count":Total_count,
                             "Percentage of Players":Percentage_of_Players})
Gender_Summary["Percentage of Players"] = Gender_Summary["Percentage of Players"].map("{:.2f}".format)
Gender_Summary


# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[318]:


Purchase_Summary=pd.DataFrame({"Purchase Count":Purchase_Count,
                             "Average Purchase Price":Average_Purchase_Price,
                              "Total Purchase Value":Total_Purchase_Value,
                              "Avg Total Purchase per Person":Avg_Total_Purchase_per_Person})

Purchase_Summary["Average Purchase Price"] = Purchase_Summary["Average Purchase Price"].map("${:.2f}".format)
Purchase_Summary["Total Purchase Value"] = Purchase_Summary["Total Purchase Value"].map("${:.2f}".format)
Purchase_Summary["Avg Total Purchase per Person"] = Purchase_Summary["Avg Total Purchase per Person"].map("${:.2f}".format)
Purchase_Summary.head()


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[319]:


purchase_data.head()


# In[320]:


bins = [0, 10, 14, 19, 24, 29, 34, 39, 60]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
purchase_data["Score"] = pd.cut(purchase_data["Age"], bins, labels=group_names)


# In[321]:


Group_Age=purchase_data.groupby(["Score"])
print(Group_Age)


# In[322]:


Total_count_=Group_Age["SN"].count()
Sum_=Total_count.sum()
Percentage_of_Players_=Total_count_/Sum*100
Purchase_Count_=Group_Age["Purchase ID"].count()
Average_Purchase_Price_=Group_Age["Price"].mean()
Total_Purchase_Value_=Group_Age["Price"].sum()
Avg_Total_Purchase_per_Person_=Total_Purchase_Value_.mean()


# In[323]:


Age_Summary=pd.DataFrame({"Total Count":Total_count_,
                        "Percentage of Players":Percentage_of_Players_})
Age_Summary["Percentage of Players"] = Age_Summary["Percentage of Players"].map("{:.2f}".format)


Age_Summary


# In[329]:


PurchasingAnalysis=pd.DataFrame({"Purchase Count":Purchase_Count_,
                             "Average Purchase Price":Average_Purchase_Price_,
                              "Total Purchase Value":Total_Purchase_Value_,
                              "Avg Total Purchase per Person":Avg_Total_Purchase_per_Person_})

PurchasingAnalysis["Average Purchase Price"] = PurchasingAnalysis["Average Purchase Price"].map("${:.2f}".format)
PurchasingAnalysis["Total Purchase Value"] = PurchasingAnalysis["Total Purchase Value"].map("${:.2f}".format)
PurchasingAnalysis["Avg Total Purchase per Person"] = PurchasingAnalysis["Avg Total Purchase per Person"].map("${:.2f}".format)
PurchasingAnalysis


# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[325]:


Top_Spenders=purchase_data.groupby(["SN"])
print(Top_Spenders)


# In[326]:


Purchase_Count1=Top_Spenders["Purchase ID"].count()
Average_Purchase_Price1=Top_Spenders["Price"].mean()
Total_Purchase_Value=Purchase_Count1*Average_Purchase_Price1


# In[327]:


Age_Summary=pd.DataFrame({"Purchase Count":Purchase_Count1,
                        "Average Purchase Price":Average_Purchase_Price1,
                         "Total Purchase Value":Total_Purchase_Value})
Sort_Age_Summary = Age_Summary.sort_values("Total Purchase Value", ascending=False)
Sort_Age_Summary["Average Purchase Price"] = Sort_Age_Summary["Average Purchase Price"].map("${:.2f}".format)
Sort_Age_Summary["Total Purchase Value"] = Sort_Age_Summary["Total Purchase Value"].map("${:.2f}".format)
Sort_Age_Summary.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[328]:


Most_popular=purchase_data.groupby(["Item ID","Item Name"])
print(Most_popular)


# In[294]:


Purchase_Count2=Most_popular["Purchase ID"].count()
Item_Price=Most_popular["Price"].mean()
Total_Purchase_Value_=Purchase_Count2*Item_Price


# In[295]:


MostPopular_Summary=pd.DataFrame({"Purchase Count":Purchase_Count2,
                        "Item Price":Item_Price,
                         "Total Purchase Value":Total_Purchase_Value_})
Sort_MostPopular_Summary = MostPopular_Summary.sort_values("Purchase Count", ascending=False)
Sort_MostPopular_Summary["Item Price"] = Sort_MostPopular_Summary["Item Price"].map("${:.2f}".format)
Sort_MostPopular_Summary["Total Purchase Value"] = Sort_MostPopular_Summary["Total Purchase Value"].map("${:.2f}".format)
Sort_MostPopular_Summary.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[296]:


Sort_MostProfitable_Item = MostPopular_Summary.sort_values("Total Purchase Value", ascending=False)
Sort_MostProfitable_Item["Item Price"] = Sort_MostProfitable_Item["Item Price"].map("${:.2f}".format)
Sort_MostProfitable_Item["Total Purchase Value"] = Sort_MostProfitable_Item["Total Purchase Value"].map("${:.2f}".format)
Sort_MostProfitable_Item .head()

