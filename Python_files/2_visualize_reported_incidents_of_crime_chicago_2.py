# import libraries
import pandas as pd

# import Bokeh libraries
from bokeh.io import output_file, show

# import ColumnDataSource from Bokeh
from bokeh.plotting import ColumnDataSource, figure

# create output file
output_file('crimes_arrests.html')

# locate the file
file = '../Dataset/Crimes_-_2016_to_present.csv'

# use pandas' read_csv() method
crimes = pd.read_csv(file)

# extract the District and Arrest columns
crimes_district_arrest = crimes[['District', 'Arrest']]

# extract only the dataset with arrests
c_d_arrest = crimes_district_arrest.loc[crimes_district_arrest['Arrest'] == True]

# as we did in previous example, count the number of arrests per district and remove the duplicates
c_d_arrest['Frequency_arrest'] = c_d_arrest.groupby('District')['District'].transform('count')
c_d_arrest = c_d_arrest.drop_duplicates('District')

# create the ColumnDataSource object from DataFrame
arrest_data = ColumnDataSource(c_d_arrest)

# create a figure object
plot = figure(x_axis_label='District', y_axis_label='Number of Arrests')

# use circle glyph for our figure object
plot.circle(x='District', y='Frequency_arrest', source=arrest_data, size=15)

# show the result
show(plot)
