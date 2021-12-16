# Exercises

OOP Geometric Shapes

Create a module in Python (Shapes.py) applying object-oriented programming modelling very basic geometric shapes. At least on class will be created for each basic geometric shapes will be defined: Circle, Rectangle and Triangle. All of them must inherit from a "Shape" class, which will define the basic methods to be implemented for each of the geometric shapes.

The objective of the assignment is to implement different OOP concepts:

- Overload `__repr__` and `__str__` , to show the information of the geometric form. What is the difference between `__str__` and `__repr__`?
- With respect to arithmetic operators, operating 2 figures will operate with the parameters of the geometric shape. This means that if we add 2 circles, a new circle will be created are its summed radius. If you add an object of numerical type, then it will be applied to each of the attributes in the geometric shape.
- With respect to the comparison operators, the area of ​​the form will be used to compare the shapes. This will allow different types of shapes to be compared, and therefore comparators should be implemented in the "Shape" class.
- The "Shape" class must "enforce" that the child classes, implement the methods common to all child classes (raise NotImplementedError). Can all methods (arithmetic and/or relational) be implemented in the parent class "Shape"?
- Implement the code in a way that allows the creation of new geometric shapes (for example ellipse or parallelogram), without the need to modify the code of the Shape class.

Send the Shapes.py with the implementation of the classes and a Jupyter Notebook ShapesUsage.ipynb (and ShapesUsage.html) with usage examples and comment
