#!/usr/bin/env python
# coding: utf-8

# # Polymorphism
# 
# Polymorphism defines the ability to take different forms. Polymorphism in Python allows us to define methods in the child class with the same name as defined in their parent class. 
# 
# There are different ways to define polymorphism in OOP:
# 
# ## Class Polymorphism in Python
# We can use the concept of polymorphism while creating class methods as Python allows different classes to have methods with the same name.
# 
# We can then later generalize calling these methods by disregarding the object we are working with. Let's look at an example:

# In[1]:


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


# ## Polymorphism with Inheritance
# 
# Polymorphism in python defines methods in the child class that have the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class. Also, it is possible to modify a method in a child class that it has inherited from the parent class.
# 
# This is mostly used in cases where the method inherited from the parent class doesn’t fit the child class. This process of re-implementing a method in the child class is known as Method Overriding. Here is an example that shows polymorphism with inheritance.

# In[2]:


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"I am an animal. My name is {self.name}. I am {self.age} years old.")
    
    def make_sound(self):
        pass
    
    def sleep(self):
        print("No time to sleep!")
        
class Cat(Animal):
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")
        
    def sleep(self):
        print("Sleeping for two hours")


class Dog(Animal):
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


# In[3]:


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.sleep()


# In Python there are special methods that are usually override: 
# 
# https://docs.python.org/3/reference/datamodel.html#special-method-names
# 
# An example are the `__str__` and `__repr__` methods.
# 
# - The function `__str__` returns a string that is shown when we call the function str() on the object.
# - The function `__repr__` returns a string with a unique representation of the object. Ideally the returned string when given to eval() returns the same object.

# In[4]:


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


# In[5]:


pepe #__repr__


# In[6]:


print(pepe) #__str__


# In[ ]:




