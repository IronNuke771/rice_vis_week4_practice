"""
This is the week 4 practice project. It uses the week 1 solution as
a starting point.
Week 1 practice project solution for Python Data Visualization
Load a county-level PNG map of the USA and draw it using matplotlib
"""

import matplotlib.pyplot as plt
import csv

# Houston location

USA_SVG_SIZE = [555, 352]
HOUSTON_POS = [302, 280]
S_FACTOR = 75000

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

def draw_USA_map(map_name):
    """
    Given the name of a PNG map of the USA (specified as a string),
    draw this map using matplotlib
    """
     
    # Load map image, note that using 'rb'option in open() is critical since png files are binary
    with open(map_name, 'rb') as map_file:        # using 'r' causes Python to crash :(
        map_img = plt.imread(map_file)

    #  Get dimensions of USA map image
    ypixels, xpixels, bands = map_img.shape
    print(xpixels, ypixels, bands)
    
    # Optional code to resize plot as fixed size figure -
##    DPI = 80.0                  # adjust this constant to resize your plot
##    xinch = xpixels / DPI
##    yinch = ypixels / DPI
##    plt.figure(figsize=(xinch,yinch))
    
    # Plot USA map
    implot = plt.imshow(map_img)
    
    # Plot green scatter point in center of map
    plt.scatter(x = xpixels / 2, y = ypixels / 2, s = 100, c = "Green")
    
    # Plot red scatter point on Houston, Tx - include code that rescale coordinates for larger PNG files
    plt.scatter(x = HOUSTON_POS[0] * xpixels / USA_SVG_SIZE[0], y = HOUSTON_POS[1] * ypixels / USA_SVG_SIZE[1], s = 100, c = "Red")

    plt.show()

def compute_county_circle(population):
    """this function ratio down a county population
    to an s value tht prints 'appropriately' on map
    """
    s_size = int(int(population)/S_FACTOR)
    return s_size

def create_riskmap(colomap):

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
    
    # Plot USA map
    implot = plt.imshow(map_img)
    

        
    
    # Plot scatter points for cancer data
    for row in range(num_counties):
        # calculate s value using function
        s_size = compute_county_circle(cancer_list[row][3])
        plt.scatter(x = float(cancer_list[row][-2]) * xpixels / USA_SVG_SIZE[0],
                    y = float(cancer_list[row][-1]) * ypixels / USA_SVG_SIZE[1],
                    s = s_size,
                    c = "Red") 
    
    plt.show()


    return ()


##draw_USA_map("USA_Counties_555x352.png")
##draw_USA_map("USA_Counties_1000x634.png")
draw_cancer_risk_data("cancer_risk_joined.csv","USA_Counties_555x352.png",20)