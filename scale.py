# Coordinates in the given array represents the different points connected to each other (x,y)
# Calculate the area of the viewport, so that points which are relatively close to each other become one single point
# The vanish factor is 1/200th the size of the area.
# The scale factor used to change the coordinates is 0.8 for zoomout and 1.25 for zoom in at each level
# Zoom level varies from Level - (-5) --> ZOOMEDOUT , Level - (0) --> Normal Zoom,  Level - (+5) ---> ZOOMEDIN
# Author: Sriganesh Navaneethakrishnan

# gets the euclidean distance 
def get_distance(p1, p2):
    return ((p2[1]-p1[1])**2 + (p2[0]-p1[0])**2)**0.5 

#finds the area of the viewport
def findArea(array):
    min_x , max_x , min_y , max_y = array[0][0], array[0][0], array[0][1], array[0][1]
    for x ,y in array:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    d = get_distance((min_x+2,min_y+2),(max_x+2,max_y+2))
    return 0.5*(d**2)

#get the new coordinates takeing into the zoom and the zoom_factor [Level of zoom and zoom in or out respectively]
def getCoordinates(array, zoom, factor):
    vanish = (0.005)*findArea(array)
    print vanish
    newArray = []
    i = 0
    scale = factor**zoom
    for x, y in array:
        if i > 0:
            d = get_distance(newArray[i-1], (x*scale,y*scale))
            print d
            if  d > vanish:
                newArray.append((x*scale,y*scale))
                i += 1
        else:
            newArray.append((x*scale, y*scale))
            i+=1
    return newArray

# finds the new path between these points based on the zoom.
def findPath(array, zoom):
    if zoom > 5 or zoom < -5:
        print "Zoom level not supported"
        return array
    newArray = []
    if zoom == 0:
        return array
    if zoom < 0:
        return getCoordinates(array, abs(zoom), 0.8)
    if zoom > 0:
        return getCoordinates(array, abs(zoom), 1.25)

array = [(20,30.5),(142.3,83.5),(31.2,-71.4),(59.78,-10.12), (-1.87,-101.7)]
print findPath(array, -6)
