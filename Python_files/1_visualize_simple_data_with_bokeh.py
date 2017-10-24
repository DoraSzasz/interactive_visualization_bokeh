# import libraries

# we choose to show the output using an output file.
# the output file generated is an html file
from bokeh.io import output_file, show
from bokeh.plotting import figure

output_file('ex1.html')

# setup a basic figure object, called plot
plot = figure(plot_width=600, plot_height=600, tools='pan, box_zoom, reset')

# plot some points with square shape of size 20
plot.square(x=[1, 2, 4, 8, 10], y=[6, 2, 18, 4, 9], size=20)

# call the show() method
show(plot)