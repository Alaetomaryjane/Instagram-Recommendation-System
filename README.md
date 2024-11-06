# Instagram Recommendation System

## Project Overview

This project analyzes Instagram post data to provide recommendations on the best hashtags and days to post for maximum engagement. Using various Python libraries, we explored engagement patterns, analyzed hashtag performance, and built recommendation functions to help improve social media strategy.

## Dataset Description

The dataset includes the following columns:

- **Date**: The date the post was published.
- **Impressions**: Total number of times the post was viewed.
- **From Home**: Impressions that came from users’ home feeds.
- **From Hashtags**: Impressions generated through hashtags.
- **From Explore**: Impressions originating from the Explore page.
- **From Other**: Impressions from other sources.
- **Saves**: Number of times users saved the post.
- **Comments**: Number of comments on the post.
- **Shares**: Number of times the post was shared.
- **Likes**: Number of likes the post received.
- **Profile Visits**: Number of visits to the profile from the post.
- **Follows**: Number of new followers gained from the post.
- **Conversion Rate**: Calculated metric showing the ratio of follows to impressions.
- **Caption**: Text description accompanying the post.
- **Hashtags**: Hashtags used in each post.

## Key Steps and Analysis

1. **Data Preprocessing**:
   - Converted the `Date` column to `datetime` format.
   - Extracted the `Day_of_week` to analyze trends by day.

2. **Exploding Hashtags for Individual Analysis**:
   - Created a list of hashtags for each post and expanded it to analyze each hashtag's impact individually.

3. **Engagement Analysis by Day of the Week**:
   - Calculated average impressions, likes, comments, and shares by the day of the week to identify optimal posting days.

4. **Top Hashtags by Engagement**:
   - Aggregated metrics for individual hashtags to determine which hashtags generate the most engagement.

5. **Correlation Analysis**:
   - Analyzed correlations between engagement metrics (e.g., Impressions, Likes, Comments, Shares) to identify relationships that could inform engagement strategies.

6. **Engagement Distribution**:
   - Visualized the distribution of engagement metrics (Likes, Comments, Shares) to understand the frequency and spread of each metric.

## Recommendation Systems

- **Hashtag Recommendation System**: A function that suggests top-performing hashtags based on average impressions and likes.
- **Posting Day Recommendation System**: A function that recommends the best days to post based on average impressions and likes.

## Visualizations

- **Average Impressions by Day of the Week**: A bar plot showing which days have the highest average impressions.
- **Top Hashtags by Impressions and Likes**: A horizontal bar chart comparing the top 5 hashtags by impressions and likes.
- **Correlation Heatmap**: A heatmap displaying the correlation between various engagement metrics.
- **Engagement Metrics Distribution**: KDE plots showing the spread and density of likes, comments, and shares.

## How to Use

1. **Top Hashtags**: Use `recommend_hashtags(df)` to get the best hashtags based on engagement metrics.
2. **Optimal Days**: Use `posting_day(df)` to identify the most effective days for posting content.

## Key Insights

- **Optimal Days**: Posting on Tuesdays and Mondays yields higher impressions, while Fridays generally have the lowest engagement.
- **Effective Hashtags**: Hashtags like #pythonprogrammer are highly effective for reaching a broader audience.
- **Engagement Correlations**: Impressions strongly correlate with likes and shares, suggesting that boosting impressions can increase overall engagement.
