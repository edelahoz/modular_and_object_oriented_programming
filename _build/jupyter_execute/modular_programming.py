#!/usr/bin/env python
# coding: utf-8

# # Modular programming
# 
# Modular programming refers to the process of breaking a large, unwieldy programming task into separate, smaller, more manageable subtasks or modules. Individual modules can then be cobbled together like building blocks to create a larger application.
# 
# There are several advantages to modularizing code in a large application:
# 
# - **Simplicity:** Rather than focusing on the entire problem at hand, a module typically focuses on one relatively small portion of the problem. If you’re working on a single module, you’ll have a smaller problem domain to wrap your head around. This makes development easier and less error-prone.
# 
# - **Maintainability:** Modules are typically designed so that they enforce logical boundaries between different problem domains. If modules are written in a way that minimizes interdependency, there is decreased likelihood that modifications to a single module will have an impact on other parts of the program. (You may even be able to make changes to a module without having any knowledge of the application outside that module.) This makes it more viable for a team of many programmers to work collaboratively on a large application.
# 
# - **Reusability:** Functionality defined in a single module can be easily reused (through an appropriately defined interface) by other parts of the application. This eliminates the need to duplicate code.
# 
# - **Scoping:** Modules typically define a separate namespace, which helps avoid collisions between identifiers in different areas of a program. (One of the tenets in the Zen of Python is Namespaces are one honking great idea—let’s do more of those!)
# 
# Functions, modules and packages are all constructs in Python that promote code modularization.

# ## Modules
# 
# 
# ### Importing a module
# ```python
# import module
# ```
# When the interpreter executes the above import statement, it searches for mod.py in a list of directories assembled from the following sources.
# 
# - The directory from which the input script was run or the current directory if the interpreter is being run interactively
# - The list of directories contained in the PYTHONPATH environment variable, if it is set. (The format for PYTHONPATH is OS-dependent but should mimic the PATH environment variable.)
# - An installation-dependent list of directories configured at the time Python is installed
# 

# In[1]:


import sys

sys.path


# In[2]:


import module

help(module)


# In[3]:


module.docs


# In[4]:


module.hello()


# In[5]:


from module import hello

hello()


# In[6]:


import module as mod

mod.add1(2)


# ### Executing a module as a script
# 
# Any .py file that contains a module is essentially also a Python script, and there isn’t any reason it can’t be executed like one.
# 
# ```python
# if __name__ == "__main__":
# ```

# In[7]:


get_ipython().run_line_magic('run', '-i module.py')


# Also from the terminal can be run as 
# 
#     >>python3 module.py

# ### Packages
# 
# A directory that contains many modules is called a package. A package is a module with submodules (which can have submodules themselves, etc.). A special file called __init__.py (which may be empty) tells Python that the directory is a Python package, from which modules can be imported 
