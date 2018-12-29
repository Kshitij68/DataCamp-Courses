"""
We will look at Bokeh plotting interface

What are Glyphs
    Visual Shapes
        Circles, Squares, Triangles
        Rectangles, Lines, Wedges
    With properties attached to data
        Coordinates (x,y)
        Size, Color, Transparency
"""


from bokeh.io import output_file,show
from bokeh.plotting import figure

plot = figure(plot_width = 400, tools = 'pan,box_zoom')