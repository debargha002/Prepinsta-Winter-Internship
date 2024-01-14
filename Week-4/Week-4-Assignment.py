#!/usr/bin/env python
# coding: utf-8

# # Week 4 Assignment- WORLD BANK DATA

# In[63]:


# importing required libraries
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


# We will import multiple raw .csv files as follows:
# - `population`: Depicts the population, country-wise ranging from year 1960 to 2016.
# - `fertility`: Depicts the fertility rate, country-wise ranging from year 1960 to 2016.
# - `expectancy`: Depicts the expectancy rate, country-wise ranging from year 1960 to 2016.
# - `metadata`: Depicts the information about the countries along with region they belong from. Helpful for grouping up the countires for future reference.
# eference.

# In[3]:


# importing .csv files

population = pd.read_csv('E:/PrepInsta Winter Internship Program/Week 4/country_population.csv')
fertility_rate = pd.read_csv('E:/PrepInsta Winter Internship Program/Week 4/fertility_rate.csv')
life_expectancy = pd.read_csv('E:/PrepInsta Winter Internship Program/Week 4/life_expectancy.csv')
country = pd.read_csv('E:/PrepInsta Winter Internship Program/Week 4/Metadata_Country.csv')


# In[5]:


# showing first 5 rows of country data
country.head()


# In[6]:


# showing first 5 rows of population data
population.head()


# In[7]:


# showing first 5 rows of fertility rate data
fertility_rate.head()


# In[8]:


# showing first 5 rows of life expectancy data
life_expectancy.head()


# In[10]:


# creating function for data processing

def preprocess_df(df, value_name):

    #create list for years
    years = [str(y) for y in range(1960, 2017)]

    # remove unnecessary columns
    df.drop(['Country Name', 'Indicator Name', 'Indicator Code'], axis=1, inplace=True)

    # remove countries with missing values
    df.dropna(axis=0, inplace=True)

    # melting the dataframe to have years in s single column
    df = pd.melt(df,
                id_vars='Country Code',
                value_vars=years,
                var_name='Year',
                value_name=value_name)
    
    return df


# In[11]:


country = country[['Country Code', 'Region']]
population = preprocess_df(population, 'Population')
fertility_rate = preprocess_df(fertility_rate, 'Fertility Rate')
life_expectancy = preprocess_df(life_expectancy, 'Life Expectancy')


# In[14]:


# after preprocessing
country.head()


# In[15]:


population.head()


# In[16]:


fertility_rate.head()


# In[17]:


life_expectancy.head()


# In[131]:


# using "country code" and "region" columns from the country table
country = country[['Country Code', 'Region']]
country


# In[19]:


# merging population and country
df = pd.merge(country, population, how='left', on='Country Code')
df


# In[20]:


# merging life expectancy to main dataframe
df = pd.merge(df, life_expectancy, how='left', on=['Country Code', 'Year'])
df


# In[21]:


# merging fertility rate to main dataframe
df = pd.merge(df, fertility_rate, how='left', on=['Country Code', 'Year'])
df


# In[22]:


# Removing remaining lines with missing values
# They will appear if a country is in one dataset but not in another one
df.dropna(axis=0, inplace=True)


# In[132]:


# Merging the data into a single dataframe
df = pd.merge(country, population, how='left', on='Country Code')
df = pd.merge(df, life_expectancy, how='left', on=['Country Code', 'Year'])
df = pd.merge(df, fertility_rate, how='left', on=['Country Code', 'Year'])

# Removing remaining lines with missing values
df.dropna(axis=0, inplace=True)


# In[24]:


df.head()


# ## Scatter Plot showing Fertility Rate and Life Expectancy

# In[134]:


px.scatter(df,
          x= "Fertility Rate",
          y= "Life Expectancy",
           title='Fertility Rate vs Life Expectancy',
          animation_frame="Year",
          animation_group="Country Code",
          size="Population",
          color="Region",
          hover_name="Country Code",
          log_x=True,
          size_max=70,
          range_x=[1,10],
          range_y=[10,100],
          template="plotly_dark")


# ## Population comparison among Regions

# In[142]:


px.bar(df,
       x="Region",
       y="Population",
       animation_frame="Year",
       animation_group="Country Code",
       color="Region",
       range_y=[0,2500000000],
       template="plotly_dark"
      )


# ## Distribution of Fertility Rates from 1960-2016

# In[68]:


sns.set(style="darkgrid")  
plt.figure(figsize=(10, 6))

# Plot the distribution of fertility rates
sns.histplot(data=df, x='Fertility Rate', kde=False, bins=30, color='green')

# Set plot labels and title
plt.xlabel('Fertility Rate')
plt.ylabel('Frequency')
plt.title('Distribution of Fertility Rates (1960-2016)')

plt.show()


# ## Population comparison among Regions

# In[88]:


region_population = df.groupby('Region')['Population'].sum().reset_index()

px.bar(region_population,
        x='Region',
        y='Population',
        template='plotly_dark',
       title="Population comparison among Regions",
        color='Region')


# ## Life Expectancy Distribution

# In[113]:


fig = px.histogram(df,
                   x='Life Expectancy',
                   template='plotly_dark',
                   title="Life Expectancy Distribution",
                   opacity=0.7)      # Set the opacity of bars for better visibility

# Add borders to the bars
fig.update_traces(marker_line=dict(color='black', width=1))

# Show the plot
fig.show()


# ## Fertility Rate Distribution

# In[120]:


fig1 = px.histogram(df,
                   x='Fertility Rate',
                   color_discrete_sequence=['cyan'],
                   template='plotly_dark',
                    title="Fertility Rate Distribution",
                   opacity=0.7)      # Set the opacity of bars for better visibility

# Add borders to the bars
fig1.update_traces(marker_line=dict(color='black', width=1))

# Show the plot
fig1.show()


# ## Population Trends by Region

# In[126]:


region_population1 = df.groupby(['Region', 'Year'])['Population'].sum().reset_index()

fig3 = px.area(region_population,
              x='Year',
              y='Population',
              color='Region',
              line_group='Region',
              labels={'Population': 'Total Population'},
              template='plotly_dark',
              title='Population Trends by Region Over Time',
              hover_name='Region')

# Customize layout
fig3.update_layout(xaxis_title='Year',
                  yaxis_title='Total Population',
                  legend_title='Region')

# Show the plot
fig3.show()


# In[130]:


region_population = df.groupby(['Region', 'Year'])['Population'].sum().reset_index()

fig2 = px.area(region_population,
              x='Year',
              y='Population',
              color='Region',
              line_group='Region',
              labels={'Population': 'Total Population'},
              template='plotly_dark',
              title='Population Trends by Region Over Time',
              facet_col='Region',  # Arrange facets in one row
              facet_col_wrap=1,    # Only one column of facets
              height=1000,        # Adjust height for better visualization
               width= 1100,
              hover_name='Region')

# Customize layout
fig2.update_layout(xaxis_title='Year',
                  yaxis_title='Total Population',
                  legend_title='Region')

# Show the plot
fig2.show()


# In[ ]:




