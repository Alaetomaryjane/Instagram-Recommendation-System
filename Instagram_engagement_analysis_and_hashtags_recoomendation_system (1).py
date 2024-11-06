#!/usr/bin/env python
# coding: utf-8

# # <center>Instagram Recommendation System

# In[2]:


# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# Exporting data
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Instagram%20data.csv")
data.to_csv('Instagram recommendation system.csv')

# loading data
df = pd.read_csv('Instagram recommendation system.csv')
df


# In[4]:


# Overview of data
df.info()


# In[5]:


# Check statistical description of data
df.describe()


# In[6]:


# Check for null values
df.isnull().sum()


# In[7]:


# Converting Date column to type, datetime
df['Date'] = pd.to_datetime(df['Date'])

df['Day_of_week'] = df['Date'].dt.day_name()

df


# In[8]:


df['Hashtags']


# In[9]:


# Expanded Hashtags List per Post for Individual Analysis

df['Hashtags_list'] = df['Hashtags'].str.split(' ')
hashtags_xplode = df.explode('Hashtags_list')
hashtags_xplode


# In[10]:


# Average Daily Engagement Metrics by Day of the Week (Top 10 Days by Impressions)

daily_engagement = df.groupby('Day_of_week').agg({
    'Impressions': 'mean',
    'Likes': 'mean',
    'Comments': 'mean',
    'Shares': 'mean'
}).sort_values(by = 'Impressions', ascending = False).head(10)
daily_engagement


# In[11]:


# Top 10 Hashtags by Average Engagement Metrics (Impressions, Likes, Comments, Shares)

hashtag_engagement = hashtags_xplode.groupby('Hashtags_list').agg({
    'Impressions': 'mean',
    'Likes': 'mean',
    'Comments': 'mean',
    'Shares': 'mean'
}).sort_values(by = 'Impressions', ascending = False). head(10)
daily_engagement, hashtag_engagement


# In[12]:


# Average Impressions by day of the week

plt.figure(figsize = (8,6))
sns.barplot(x = daily_engagement.index, y = daily_engagement['Impressions'], palette = 'Reds')
plt.xlabel('Day of the week', fontsize = 11)
plt.ylabel('Average impressions', fontsize = 11)
plt.xticks( rotation = 40)
plt.title('Average impressions by day of the week', fontsize = 18)
plt.show()


# Summary: This chart shows that Tuesdays receive the highest average impressions, followed closely by Mondays, indicating that content posted on these two days likely reaches the widest audience. Sundays and Wednesdays also show fairly high engagement but fall below Tuesdays and Mondays. Fridays has the lowest average impressions, with Thursdays and Saturdays slightly higher but still on the lower end

# In[22]:


plt.figure(figsize = (10, 8))
sns.set(style = 'whitegrid')
top_hashtags = hashtag_engagement[['Impressions', 'Likes']].head(5)
top_hashtags.plot(kind = 'bar', color = ['#2a9d8f', '#e76f51'])
plt.title('Top 5 hashtags by Impression and Likes', fontsize = 14)
plt.xlabel('Top Hashtags', fontsize = 10)
plt.ylabel('Average Engagement', fontsize = 10)
plt.xticks(rotation = 45)
plt.show()


# This chart shows the top 5 hashtags by impressions and likes. Each hashtag, like `#pythonprogrammer` and `#pythoncoding`, generates high impressions (around 100,000), indicating strong reach. However, likes are comparatively low, suggesting limited user interaction despite visibility. These hashtags are effective for reach but may require additional strategies to boost engagement.

# In[16]:


# Checking the correlation between engagement metrics

plt.figure(figsize = (8, 6))
correlation_matrix = df[['Impressions', 'Comments', 'Likes', 'Shares', 'Saves', 'Follows']].corr()
sns.heatmap(correlation_matrix, annot = True, cmap = 'coolwarm', linewidth = 0.5)
plt.title('Correlation between Engagement Metrics')
plt.tight_layout()
plt.show()


# This indicates that there are strong positive correlations between various engagement metrics. Specifically, metrics like Impressions have high correlations with Likes (90%) and Shares (80%), suggesting that increasing Impressions can lead to more Likes and Shares. Additionally, Likes strongly correlate with Shares (87%) and Saves (94%). This means that boosting likes will likely increase shares and saves as well. These relationships suggest that overall engagement and social media strategies can be optimized by focusing on increasing certain metrics like impressions and likes.

# In[17]:


# Visualizing Engagement Metrics Distribution

plt.figure(figsize = (8,6))
sns.kdeplot(df[['Likes', 'Comments', 'Shares']])
plt.title('Ditribution of Likes, Comments, and Shares')
plt.xlabel('Engagements')
plt.ylabel('Frequency')
plt.show()


# Summary: Comments are the most consistent engagement type, with a density peak above 0.030 and a spread from 0 to 200. Shares follow, with a peak density around 0.006 and a spread from 0 to 300, suggesting occasional high engagement. Likes are the least frequent, with a lower peak at 0.001 and a wider spread from 0 to 700, indicating that they occur less frequently and are generally low in count.

# ### Hashtag Recommendation System

# In[18]:


def recommend_hashtags(df, frequent = 5):
    hashtag_performance = df.explode('Hashtags_list').groupby('Hashtags_list').agg({
        'Impressions' : 'mean',
        'Likes' : 'mean',
    }).sort_values(by = 'Impressions', ascending = False)
    
    top_hashtags = hashtag_performance.head(frequent).index.tolist()
    return top_hashtags
top_hashtags = recommend_hashtags(df)
print(f'Top 5 Recommended Hashtags: {top_hashtags}')


# ### Posting day Recommendation System

# In[19]:


def posting_day(df, top_n = 3):
    daily_feedback = df.groupby('Day_of_week').agg({
        'Impressions' : 'mean',
        'Likes' : 'mean'
    }).sort_values(by = 'Impressions', ascending = False)
    
    top_days = daily_feedback.head(top_n).index.tolist()
    return top_days
top_days = posting_day(df)
print(f'Recommended Days to Post: {top_days}')


# In[ ]:




