# EPAiV5-Session10
This report contains assignment solution for EPAiV5 Session 10 

Name: Aravind D. Chakravarti
Email: aravinddcsadguru@gmail.com

# Solution Architecture

In order to make the any object into `iterable` we need to add `__iter__` method. In python we do this by following way.

```python
class ClassName:
  def __init__(self):
    .....

  # Some other functions

  def __iter__(self):
    return self

  def __next__(self):
    return (data) 
```

The `__iter__` is something which python will use to iterate over using `__next__` method. `__next__` method fetches the next element in the object.

Now, in the solution, `polygonsequence.py` holds the class which implements the iterable Regular Convex Polygon. 

```python
class RegConvexPolygon:
    def __init__(self, circum_radius: float, largest_polygon: int) -> None:
          '''
          Initialize the convex polygon with its number of edges and circumradius.
          '''
```
The class takes `circum radius` and `largest polygon` as inputs and generate the sequence which contains information like "area", "perimeter" etc. The sequence is generated from " edges 3 to largest polygon" size. 

```python
 def __iter__(self):
        # print("RegConvexPolygon __iter__ is called")
        return self.PolygonIterator(self)

class PolygonIterator:
        '''This is iterator class. This gets called by the class
        which has data and this iterator loops over it
        '''
        def __init__(self, obj_RegConvexPolygon):
```
Because we do not want our iterator to be stuck at the last element after every `for` loop, we decomple the data and iterator. `class` `RegConvexPolygon` holds the data and other methods like `calculate_parameters` (which calculates the parameters a polygon). When we create an obect of type `RegConvexPolygon` and when we try to loop using `for`, the `RegConvexPolygon` `__iter__` returns the `PolygonIterator`, meaning, now `for` loop uses `PolygonIterator`'s `__iter__` and `__next__` methods.

