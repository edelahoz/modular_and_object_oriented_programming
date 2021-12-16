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
# **Explain init and self**
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
#     - Just like .__init__(), an instance method’s first parameter is always self.
# 
# 
# - **Class methods**: 
#     - Methods that are bound to the class and not instances of the class. 
#     - They have access to the state of the class as it takes a class parameter that points to the class and not the object instance (usually _cls_). 
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


class Person:
    specie = "Homo Sapiens Sapiens"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello! I'm {self.name.title()}.")
        
    def get_age(self):
        return self.age
    
    @classmethod 
    def print_specie(cls):
        print(f"I'm a {cls.specie}")
        
    @classmethod 
    def generate_offspring(cls, name):
        return cls(name,0)
        
    @staticmethod
    def is_adult(age):
        return age > 18
        
        
pepe = Person("pepe garcía", 22)
pepa = Person("pepa jiménez", 21)


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


# hablar de properties y modificar age por birthday calcular age a partir de birthday

# In[12]:


from datetime import date


class Person:
    specie = "Homo Sapiens Sapiens"
    
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age
        
    
    def greet(self):
        print(f"Hello! I'm {self.name.title()}.")
        
    def get_age(self):
        return self.age
    
    @classmethod 
    def print_specie(cls):
        print(f"I'm a {cls.specie}")
        
    @classmethod 
    def generate_offspring(cls, name):
        return cls(name,0)
        
    @staticmethod
    def is_adult(age):
        return age > 18


# In[13]:


pepe = Person("pepe", date(1999, 3, 20))
pepe.age


# ## Overriding
# 
# There are operators which can be re-defined. For example the arithmetic ‘+’  operator,
# With the current implementation, the statement R3 = R1 + R2 raise an error. 
# But it can be re-defined by modifying the add method definition by
# 
# - `__repr__`
#     - Ideally, the string returned by `repr()` should be the one that given to `eval()` returns the same object. 
# 
# - `__str__`

# In[14]:


pepe


# In[15]:


class Person:
    specie = "Homo Sapiens Sapiens"
    
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age
    
    def __repr__(self):
        return f"Person({self.name}, {repr(self.birthdate)})"
    
    def __str__(self):
        return f"{self.name.title()}"
    
    def greet(self):
        print(f"Hello! I'm {self.name.title()}.")
        
    def get_age(self):
        return self.age
    
    @classmethod 
    def print_specie(cls):
        print(f"I'm a {cls.specie}")
        
    @classmethod 
    def generate_offspring(cls, name):
        return cls(name,0)
        
    @staticmethod
    def is_adult(age):
        return age > 18    
    
pepe = Person("pepe garcía", date(1999, 3, 20))
pepa = Person("pepa jiménez", date(1997, 6, 5))


# In[16]:


pepe


# In[17]:


print(pepe)


# In[ ]:




