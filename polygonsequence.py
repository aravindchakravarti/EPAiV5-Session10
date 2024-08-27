import math

class RegConvexPolygon:
    '''
    Regular Convex Polygon class. A polygon is called "Regular Convex Polygon" if and only if:
        a. Equal Side Lengths: All the sides of the polygon are of equal length.
        b. Equal Angles: All the interior angles are equal.
        c. Convexity: The polygon is convex, meaning all its interior angles are less than 180 degrees, 
           and no part of the polygon "caves in."
    '''
    def __init__(self, circum_radius: float, largest_polygon: int) -> None:
        '''
        Initialize the convex polygon with its number of edges and circumradius.
        '''
        # print("RegConvexPolygon __init__ is called")
        if  not (isinstance(circum_radius, int) or isinstance(circum_radius, float)):
            raise TypeError ('Polygons will have circum_radius of type int or float')

        if not isinstance(largest_polygon, int):
            raise TypeError ('Polygons will have edges of type int')

        if largest_polygon < 3:
            raise ValueError ('Polygon should have atleast 3 sides')

        if circum_radius <= 0:
            raise ValueError ('Polygon\'s circum radius must a valid positive real number')

        self.circum_radius = circum_radius
        self.largest_polygon = largest_polygon

    def __iter__(self):
        # print("RegConvexPolygon __iter__ is called")
        return self.PolygonIterator(self)

    def calculate_parameters(self, no_edges, circum_radius):
        '''
        Calculates various properties (e.g., area, perimeter, apothem) of the regular polygon 
        and returns them as a dictionary.
        '''
        vertices = no_edges
        interior_angle = round((no_edges - 2) * (180 / no_edges), 2)
        edge_len = round(2 * circum_radius * math.sin(math.radians(180 / no_edges)), 4)
        apothem = round(circum_radius * math.cos(math.radians(180 / no_edges)), 4)
        area = round(0.5 * no_edges * edge_len * apothem,4)
        perimeter = round(no_edges * edge_len, 4)
        area_to_peri_ratio = round(area/perimeter, 5)
        parameters = {'vertices':vertices, 
                      'interior_angle':interior_angle,
                      'edge_len':edge_len,
                      'apothem':apothem,
                      'area':area,
                      'perimeter':perimeter,
                      'a_p_ratio':area_to_peri_ratio}
        return parameters

    class PolygonIterator:
        '''This is iterator class. This gets called by the class
        which has data and this iterator loops over it
        '''
        def __init__(self, obj_RegConvexPolygon):
            '''Initializes the class with the object from which it is got called
            '''
            # print("polygonIterator __init__ is called")
            self.obj_to_iter = obj_RegConvexPolygon
            self.index = 3

        def __iter__(self):
            '''for loop uses this method to call __next__
            '''
            # print("polygonIterator __iter__ is called")
            return self

        def __next__(self):
            '''for loop uses this method ot fetch the next element in the object
            '''
            # print("polygonIterator __next__ is called")
            if self.index > self.obj_to_iter.largest_polygon:
                # We have reached the end of iteration loop. Indicate for loop to stop iteration
                raise StopIteration
            else:
                # Calculate the parameters and return to the for loop
                params = self.obj_to_iter.calculate_parameters(self.index, self.obj_to_iter.circum_radius)
                self.index= self.index+1
                return params