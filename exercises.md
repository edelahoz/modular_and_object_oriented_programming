# Exercises

### OOP Geometric Shapes


Create a module in Python (Shapes.py) applying object-oriented programming for modeling basic geometric shapes. Create at least one class for each basic geometric shape: Circle, Rectangle, and Triangle. All of them must inherit from a “Shape” class, which defines the shared methods. This assignment does not have a unique solution. The objective is to implement different OOP concepts:

- Overload __repr__ and __str__ to show the information of the geometric form. What is the difference between `__str__` and `__repr__`?

- Concerning arithmetic operators, operations between 2 figures are performed with the parameters of each geometric shape. For example, if we add 2 circles, a new circle, whose radius is the sum of the previous, is created. Regarding operations between figures and objects of numerical type, the number will be applied to each geometric shape’s attribute.

- For comparison operators, the area of the figure is used to compare among shapes. Thus, shapes of different types are comparable, i.e., comparison operators should be implemented in the “Shape” class.

- The “Shape” class must “enforce” the child classes the implementation of the shared methods (raise NotImplementedError). Can all methods (arithmetic and/or relational) be implemented in the parent class “Shape”?

- Implement the code in a way that allows the creation of new geometric shapes, e.g., ellipse or parallelogram, without modifying the Shape class.

Send Shapes.py with the implementation of the classes and a Jupyter Notebook ShapesUsage.ipynb (and ShapesUsage.html) with examples and comments.
