#!/usr/bin/env python
# coding: utf-8

# # Scripts
# 
# A script is a file with a sequence of instructions that are executed each time the script is called. The extension for Python files is .py. Let's see an example, we create a file called `myscript.py` with the following commands:
# ```python
# message = "Hello world!"
# print(message)
# ```
# 
# One can call the script from the current jupyter notebook:

# In[1]:


get_ipython().run_line_magic('run', 'myscript.py')


# The instructions written in `myscript.py` have been executed and we have access now to the variables defined in the script.

# In[2]:


message


# Scripts can also be executed inside a shell terminal by running the following command:
# 
# ```bash
# python path_to_script_file
# ```
# 
# If `myscript.py` is in the current working directory:
#  
# ```bash
# python myscript.py
# ```
