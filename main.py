#data set imported from the Y-Combinator folder from: https://github.com/ali-ce/datasets
import numpy as np
import pandas as pd
from wordcloud import WordCloud

#preparing the data
data_file  = 'raw_data/Startups.csv'

y_full = pd.read_csv(data_file)

needed_columns = ['Company','Categories','Y Combinator Year', 'Headquarters (City)']
y = y_full[needed_columns]

#group by categories
ycat_grouped = y.groupby('Categories')
ycat_counts = ycat_grouped['Categories'].value_counts()
print(ycat_counts.plot.pie(y='Company'))
