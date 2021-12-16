#!/usr/bin/env python
# coding: utf-8

# 

# ## Classes  
# Classes are used to create user-defined data structures. Like integers or strings but more complex. A Class is the abstract representation of a concept, like dog, integer number, person, etc ... It doesn’t actually contain any data. 
# 
# <div class="alert alert-block alert-info"><b>Note: </b> In this notebook we build a class Person to better exemplify the concepts introduced.  </div>
# 
# 

# In[1]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"Person({self.name}, {self.age})"
    
    def __str__(self):
        return f"{self.name.title()}"
    
    def greet(self):
        print(f"Hello! I'm {self.name.title()}")


# A class is a blueprint for how something should be defined. It doesn’t actually contain any data.

# ### Classes vs Instances
# 
# The Dog class specifies that a name and an age are necessary for defining a dog, but it doesn’t contain the name or age of any specific dog.
# 
# While the class is the blueprint, an **instance** is an object that is built from a class and contains real data. An instance of the Dog class is not a blueprint anymore. It’s an actual dog with a name, for example:
# ```python
# dog1 = Dog("Boris", 7)
# ```
# <div class="alert alert-block alert-warning"><b>Example: </b>  Dale caña</div> 
# 

# 
# ### Atributes and methods
# 
# -  Atributes
#     - Instance
#     - Class
#     
# - Methods
#     - Instance
#     
#         Instance methods are functions that are defined inside a class and can only be called from an instance of that class. Just like .__init__(), an instance method’s first parameter is always self.
# 
#     - Class
# 
# 

# ### Spetial Methods
# 
# - \_\_init\_\_
# 
# The properties that all Dog objects must have are defined in a method called .__init__(). Every time a new Dog object is created, .__init__() sets the initial state of the object by assigning the values of the object’s properties. That is, .__init__() initializes each new instance of the class.
# 
# You can give .__init__() any number of parameters, but the first parameter will always be a variable called self. When a new class instance is created, the instance is automatically passed to the self parameter in .__init__() so that new attributes can be defined on the object.
# 
# 
# Attributes created in .__init__() are called instance attributes. An instance attribute’s value is specific to a particular instance of the class. All Dog objects have a name and an age, but the values for the name and age attributes will vary depending on the Dog instance.
# 
# On the other hand, class attributes are attributes that have the same value for all class instances. You can define a class attribute by assigning a value to a variable name outside of .__init__().
# 
# 
# - \_\_repr\_\_
# 
# - \_\_str\_\_

# In[2]:


class Dog:
    species = "Golden Retriever"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


# In[3]:


boris = Dog("Boris", 7)
print(boris.species)
print(boris.age)


# In[4]:


boris.age = 1
print(boris.age)


# <div class="alert alert-block alert-success">The key takeaway here is that custom objects are mutable by default. An object is mutable if it can be altered dynamically. For example, lists and dictionaries are mutable, but strings and tuples are immutable.</div>

# In[ ]:




