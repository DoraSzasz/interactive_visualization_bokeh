# import libraries
import pandas as pd

# import Bokeh libraries - 2nd phase
#from bokeh.charts import Bar
#from bokeh.io import output_file, show

# create output file - 2nd phase
#output_file('crimes.html')

# locate the file
file = '../Dataset/Crimes_-_2016_to_present.csv'

# use pandas' read_csv() method
crimes = pd.read_csv(file)
print(crimes)

# extract the District column - 2nd phase
#crimes_district = crimes[['District']]

# count the frequency of crimes per District - 2nd phase
#crimes_district['Frequency'] = crimes_district.groupby('District')['District'].transform('count')

# extract the unique values only of the Districts - 2nd phase
#crimes_district_unique = crimes_district.drop_duplicates('District')

# plot the Bar chart of the frequency on the crimes in each District - 2nd phase
#bar_chart = Bar(crimes_district_unique, 'District', values='Frequency',
#               title ='Frequency of Crimes per District', legend = False)

# plot the Bar chart of the frequency on the crimes in each District - 2nd phase
#show(bar_chart)