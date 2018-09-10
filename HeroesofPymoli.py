
# coding: utf-8

# In[3]:



import pandas as pd
import numpy as np

file_to_load = "Resources/purchase_data.csv"

purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# In[4]:


Total_players=len(purchase_data["SN"].unique())
df=pd.DataFrame({"Total Players": [Total_players]})
df


# In[5]:


unique_items=len(purchase_data["Item ID"].unique())
average=purchase_data["Price"].mean()
number_of_purchases=len(purchase_data["Purchase ID"].unique())
total_revenue=purchase_data["Price"].sum()


# In[6]:


Summary_table=pd.DataFrame({"Number of Unique Items":[unique_items],
                            "Average Price":[average],
                            "Number of Purchases":[number_of_purchases],
                            "Total Revenue":[total_revenue]})
Summary_table["Average Price"] = Summary_table["Average Price"].map("${:.2f}".format)
Summary_table["Total Revenue"] = Summary_table["Total Revenue"].map("${:.2f}".format)
Summary_table


# In[7]:


Group_Gender=purchase_data.groupby(["Gender"])
print(Group_Gender)
Group_Gender.count()


# In[8]:


Total_count=Group_Gender["Gender"].count()
Sum=Total_count.sum()
Percentage_of_Players=Total_count/Sum*100
Purchase_Count=Group_Gender["Purchase ID"].count()
Average_Purchase_Price=Group_Gender["Price"].mean()
Total_Purchase_Value=Group_Gender["Price"].sum()
Avg_Total_Purchase_per_Person=Total_Purchase_Value.mean()


# In[9]:


Gender_Summary=pd.DataFrame({"Total Count":Total_count,
                             "Percentage of Players":Percentage_of_Players})
Gender_Summary["Percentage of Players"] = Gender_Summary["Percentage of Players"].map("{:.2f}".format)
Gender_Summary


# In[10]:


Purchase_Summary=pd.DataFrame({"Purchase Count":Purchase_Count,
                             "Average Purchase Price":Average_Purchase_Price,
                              "Total Purchase Value":Total_Purchase_Value,
                              "Avg Total Purchase per Person":Avg_Total_Purchase_per_Person})

Purchase_Summary["Average Purchase Price"] = Purchase_Summary["Average Purchase Price"].map("${:.2f}".format)
Purchase_Summary["Total Purchase Value"] = Purchase_Summary["Total Purchase Value"].map("${:.2f}".format)
Purchase_Summary["Avg Total Purchase per Person"] = Purchase_Summary["Avg Total Purchase per Person"].map("${:.2f}".format)
Purchase_Summary.head()


# In[11]:


bins = [0, 10, 14, 19, 24, 29, 34, 39, 60]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
purchase_data["Score"] = pd.cut(purchase_data["Age"], bins, labels=group_names)


# In[12]:


Group_Age=purchase_data.groupby(["Score"])
print(Group_Age)


# In[13]:


Total_count_=Group_Age["SN"].count()
Sum_=Total_count.sum()
Percentage_of_Players_=Total_count_/Sum*100
Purchase_Count_=Group_Age["Purchase ID"].count()
Average_Purchase_Price_=Group_Age["Price"].mean()
Total_Purchase_Value_=Group_Age["Price"].sum()
Avg_Total_Purchase_per_Person_=Total_Purchase_Value_.mean()


# In[14]:


Age_Summary=pd.DataFrame({"Total Count":Total_count_,
                        "Percentage of Players":Percentage_of_Players_})
Age_Summary["Percentage of Players"] = Age_Summary["Percentage of Players"].map("{:.2f}".format)
Age_Summary


# In[15]:


PurchasingAnalysis=pd.DataFrame({"Purchase Count":Purchase_Count_,
                             "Average Purchase Price":Average_Purchase_Price_,
                              "Total Purchase Value":Total_Purchase_Value_,
                              "Avg Total Purchase per Person":Avg_Total_Purchase_per_Person_})

PurchasingAnalysis["Average Purchase Price"] = PurchasingAnalysis["Average Purchase Price"].map("${:.2f}".format)
PurchasingAnalysis["Total Purchase Value"] = PurchasingAnalysis["Total Purchase Value"].map("${:.2f}".format)
PurchasingAnalysis["Avg Total Purchase per Person"] = PurchasingAnalysis["Avg Total Purchase per Person"].map("${:.2f}".format)
PurchasingAnalysis


# In[16]:


Top_Spenders=purchase_data.groupby(["SN"])
print(Top_Spenders)


# In[17]:


Purchase_Count1=Top_Spenders["Purchase ID"].count()
Average_Purchase_Price1=Top_Spenders["Price"].mean()
Total_Purchase_Value=Purchase_Count1*Average_Purchase_Price1


# In[18]:


Age_Summary=pd.DataFrame({"Purchase Count":Purchase_Count1,
                        "Average Purchase Price":Average_Purchase_Price1,
                         "Total Purchase Value":Total_Purchase_Value})
Sort_Age_Summary = Age_Summary.sort_values("Total Purchase Value", ascending=False)
Sort_Age_Summary["Average Purchase Price"] = Sort_Age_Summary["Average Purchase Price"].map("${:.2f}".format)
Sort_Age_Summary["Total Purchase Value"] = Sort_Age_Summary["Total Purchase Value"].map("${:.2f}".format)
Sort_Age_Summary.head()


# In[19]:


Most_popular=purchase_data.groupby(["Item ID","Item Name"])
print(Most_popular)


# In[20]:


Purchase_Count2=Most_popular["Purchase ID"].count()
Item_Price=Most_popular["Price"].mean()
Total_Purchase_Value_=Purchase_Count2*Item_Price


# In[21]:


MostPopular_Summary=pd.DataFrame({"Purchase Count":Purchase_Count2,
                        "Item Price":Item_Price,
                         "Total Purchase Value":Total_Purchase_Value_})
Sort_MostPopular_Summary = MostPopular_Summary.sort_values("Purchase Count", ascending=False)
Sort_MostPopular_Summary["Item Price"] = Sort_MostPopular_Summary["Item Price"].map("${:.2f}".format)
Sort_MostPopular_Summary["Total Purchase Value"] = Sort_MostPopular_Summary["Total Purchase Value"].map("${:.2f}".format)
Sort_MostPopular_Summary.head()


# In[22]:


Sort_MostProfitable_Item = MostPopular_Summary.sort_values("Total Purchase Value", ascending=False)
Sort_MostProfitable_Item["Item Price"] = Sort_MostProfitable_Item["Item Price"].map("${:.2f}".format)
Sort_MostProfitable_Item["Total Purchase Value"] = Sort_MostProfitable_Item["Total Purchase Value"].map("${:.2f}".format)
Sort_MostProfitable_Item .head()

