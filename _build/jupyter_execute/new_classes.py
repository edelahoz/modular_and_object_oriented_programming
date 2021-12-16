#!/usr/bin/env python
# coding: utf-8

# # Objects and Classes
# 
# In OOP, a **Class** is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). Classes are used to create user-defined data structures. Like integers or strings but more complex. 
# 
# A **Class** is the abstract representation of a concept, like dog, integer number, person, etc ... It doesn’t contain any data. On the other hand, an **instance** is an object that is built from a class and contains real data. Let see an example:

# In[1]:


class Person:
    specie = 'Homo Sapiens Sapiens'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
pepe = Person("pepe garcía", 22)
pepa = Person("pepa jiménez", 21)


# In the above snippet we have defined a class Person. A Person has two attributes name and age. The class itself does not have assigned values to those attributes unlike pepe. `pepe` and `pepa` are two different instances of the Class Person with a given name and age.
# 
# <div class="alert alert-block alert-info"><b>Note: </b>
# Python class names are written in CapitalizedWords notation by convention.
# </div>
# 
# 
# Classes are composed of attributes and methods.
# 
# ## Attributes 
# 
# - **Class attributes**: data that belong to the class as a whole. There is only one copy of each one for all instances of the class.
# - **Instance variables or attributes**: data that belongs to individual objects. Each object has its own copy of the attributes.
# 
# In Python **instance attributes** are defined in the `__init__()` function while **class attributes** are defined by  assigning values to variables outside `__init__()`. Usually they are defined immediately after the first line of the class name. `name` and `age` are instance attributes while `specie` is a class attribute. 
# 
# `__init__` is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
# 
# The first parameter given to `__init__`, `self` is used to represent the instance of a class. By using the `self` keyword we access the attributes and methods of the class in python. All the instance methods (see below) need this reference as the first parameter.
# 
# Attributes can be accessed with dot notation:

# In[2]:


pepa.name


# In[3]:


pepe.specie


# In[4]:


Person.specie


# The attributes values can be changed dynamically, i.e., custom objects are mutable by default.

# In[5]:


pepa.age = 45
pepa.age


# ## Methods 
# 
# - **Instance methods**: 
#     - Functions that belong to individual objects, and have access to instance variables for the specific object they are called on, inputs, and class variables. 
#     - Can only be called from an instance of that class. 
#     - In Python, the first parameter given to this type of methods is `self`, a reference to the instance. (Note that self is just a name convetion, other names can be given but it is good practice to use self.)
#     - Just like .__init__(), an instance method’s first parameter is always self.
# 
# 
# - **Class methods**: 
#     - Methods that are bound to the class and not instances of the class. 
#     - They have access to the state of the class as it takes class parameter that points to the class and not the object instance (usually `cls`) as a first parameter. 
#     - They can modify a class state that would apply across all the instances of the class. For example, a class variable that will be applicable to all the instances. 
#     - They can be called from the class itself or from instances of it.
#     - They are specified by the decorator `@classmethod`. 
# 
# - **Static methods**: 
#     - Functions that belong to a class but does not need access to any attribute. 
#     - They could be written outside the class but they are defined within a class since they are conceptually intrisically related to that class.
#     - They can be called from the class itself or from instances of it.
#     - They are specified by the decorator `@staticmethod`. 

# In[6]:


from datetime import date

class Person:
    specie = "Homo Sapiens Sapiens"
    
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        # One can calculate attributes from given inputs
        today = date.today()
        # The _ before an attribute is to indicate that the attribute should not be modified
        self._age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        
    
    def greet(self):
        print(f"Hello! I'm {self.name.title()}.")
        
    def get_age(self):
        return self._age
    
    @classmethod 
    def print_specie(cls):
        print(f"I'm a {cls.specie}")
        
    @classmethod 
    def generate_offspring(cls, name):
        return cls(name, date.today())
        
    @staticmethod
    def is_adult(age):
        return age > 18
        
        
pepe = Person("pepe garcía", date(1994, 3, 12))
pepa = Person("pepa jiménez", date(1995, 2, 18))


# In[7]:


pepito = Person.generate_offspring("pepito")
pepito.greet()
pepito.get_age()


# The class Person has now two instance methods `greet` and `get_age`, a class method `print_specie` and a static method called `hello`.

# In[8]:


pepe.greet()


# In[9]:


pepa.get_age()


# Class method vs Static Method
# 
# - A class method takes cls as the first parameter while a static method needs no specific parameters.
# - A class method can access or modify the class state while a static method can’t access or modify it.
# - In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
# 

# In[10]:


Person.print_specie()


# In[11]:


pepe.is_adult(pepe.age)


# In[18]:


pepe = Person("pepe", date(1999, 3, 20))
pepe.age

