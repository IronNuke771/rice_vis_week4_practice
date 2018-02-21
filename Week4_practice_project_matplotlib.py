"""
This is the week 4 practice project. It uses the week 1 solution as
a starting point.
Week 1 practice project solution for Python Data Visualization
Load a county-level PNG map of the USA and draw it using matplotlib
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import math


# Houston location

USA_SVG_SIZE = [555, 352]
S_FACTOR = 75000                         # Factor that scales the population for circle size
MAX_LOG_RISK = math.log(1.50E-04, 10)    # maximum cancer risk in table
MIN_LOG_RISK = math.log(8.60E-06, 10)    # minimum cancer risk in table

def read_csv_as_list(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    table = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            table.append(row)
    return table

def compute_county_circle(population):
    """this function ratio down a county population
    to an s value tht prints 'appropriately' on map
    """
    s_size = int(int(population)/S_FACTOR)
    return s_size

def create_normalized_risk(colormap):
    """
    Initialize the colormap "jet" from matplotlib,
    Return function that takes risk and returns RGB color for use with scatter() in matplotlib
    """
    # Note that this code is tricky - remember to return a lambda expression
    # I was missing what was required for this function. Using the provided constants
    # of min and max risk values
    risk_norm = mpl.colors.Normalize(vmin = MIN_LOG_RISK, vmax = MAX_LOG_RISK)
    color_mapper = mpl.cm.ScalarMappable(norm = risk_norm, cmap = colormap)
    return lambda risk : color_mapper.to_rgba(math.log(risk, 10))

def draw_cancer_risk_data(filename,map_name,num_counties):
    """overlay cancer risk data onto USA county map
    """
    cancer_list = read_csv_as_list("cancer_risk_joined.csv", ",", '"')
    
    for row in range(num_counties):
        print(cancer_list[row])
    
    # Load map image, note that using 'rb'option in open() is critical since png files are binary
    with open(map_name, 'rb') as map_file:        # using 'r' causes Python to crash :(
        map_img = plt.imread(map_file)

    #  Get dimensions of USA map image
    ypixels, xpixels, bands = map_img.shape
    print(xpixels, ypixels, bands)
    
    # Optional code to resize plot as fixed size figure -
    DPI = 80.0                  # adjust this constant to resize your plot
    xinch = xpixels / DPI
    yinch = ypixels / DPI
    plt.figure(figsize=(xinch,yinch))
    
    # Plot USA map
    implot = plt.imshow(map_img)
    
    # Compute function that maps cancer risk to RGB colors
    risk_map = create_normalized_risk(mpl.cm.jet)
    
    # Plot scatter points for cancer data
    for row in range(num_counties):
        # calculate s value using function
        plt.scatter(x = float(cancer_list[row][-2]) * xpixels / USA_SVG_SIZE[0],
                    y = float(cancer_list[row][-1]) * ypixels / USA_SVG_SIZE[1],
                    s = compute_county_circle(cancer_list[row][3]),
                    c = risk_map(float(cancer_list[row][4]))) 
    
    plt.show()


    return ()


##draw_USA_map("USA_Counties_555x352.png")
##draw_USA_map("USA_Counties_1000x634.png")
draw_cancer_risk_data("cancer_risk_joined.csv","USA_Counties_555x352.png",1000)