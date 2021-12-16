#!/usr/bin/env python
# coding: utf-8

# # Inheritance and  Composition
# 
# **Inheritance** is a way of arranging objects in a hierarchy from the most general to the most specific. An object which inherits from another object is considered to be a subtype of that object. As we saw in the previous chapter, all objects in Python inherit from object. We can say that a string, an integer or a `Person` instance is an object instance. When we can describe the relationship between two objects using the phrase _is-a_, that relationship is inheritance.
# 
# Child classes can override or extend the attributes and methods of parent classes. In other words, child classes inherit all of the parent’s attributes and methods but can also specify attributes and methods that are unique to themselves.
# 
# 
# **Composition** Composition is a concept that models a has a relationship. It enables creating complex types by combining objects of other types. This means that a class Composite can contain an object of another class Component. This relationship means that a Composite has a Component. For example, we could have added an attribute birthday to the class `Person` given by a `datetime.date` object.
# 
# Composition enables you to reuse code by adding objects to other objects, as opposed to inheriting the interface and implementation of other classes. 
# 
# ## Inheritance
# 
# We have already worked with inheritance without noticing it. This is because every class you create in Python implicitly derives from object. Let's see an example:

# In[1]:


class Person:
    pass


# In[2]:


pepe = Person()
print(dir(pepe))


# Although we haven't defined anything yet in the class Person, the object pepe has several methods that are inherited from the class Object. 
# 
# <div class="alert alert-block alert-info"><b>Note: </b>User-defined exceptions must inherit from BaseException instead of Object. 
#     
# ```python
# class MyException(BaseException):
#     pass
# ```
# </div>
# 
# Let's create a `Student` class, `Researcher` class and a `TeacherAssistant` that inherits from `Person`:

# In[3]:


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

    
class Student(Person):
    def __init__(self, name, birthdate, student_id):
        super().__init__(name, birthdate) # The super() method, allows to invoke methods defined on the base class.
        self.student_id = student_id
        
class Researcher(Person):
    def __init__(self, name, birthdate, field_of_research):
        super().__init__(name, birthdate) # The super() method, allows to invoke methods defined on the base class.
        self.field = field_of_research
        
class TeacherAssistant(Person):
    def __init__(self, name, birthdate, course):
        super().__init__(name, birthdate) # The super() method, allows to invoke methods defined on the base class.
        self.course = course


# In[4]:


fulanito = Student("Fulanito Fernández", date(2000, 4, 21), "7254" )


# An object from Student has inherited the attributes and methods from the class `Person`.

# In[5]:


fulanito.print_specie()


# In[6]:


fulanito.greet()


# In[7]:


print(dir(fulanito))


# A child class can also override the parent's methods:

# In[8]:


class Student(Person):
    def __init__(self, name, birthdate, student_id):
        super().__init__(name, birthdate) # The super() method, allows to invoke methods defined on the base class.
        self.student_id = student_id
        
    def greet(self):
        print(f"Hello! I'm {self.name.title()} and I'm a student.")


# In[9]:


fulanito = Student("Fulanito Fernández", date(2000, 4, 21), "7254" )
fulanito.greet()


# ### Inheriting Multiple Classes
# 
# Python is one of the few modern programming languages that supports multiple inheritance. Multiple inheritance is the ability to derive a class from multiple base classes at the same time.

# In[10]:


class Student(Person):
    def __init__(self, name, birthdate, student_id=None, **kwargs):
        super().__init__(name, birthdate, **kwargs) 
        self.student_id = student_id 
        
    def study(self, hours):
        print(f"Studying for {hours} hours")
        time.sleep(hours)
        print("Finish studying")
        
class Researcher(Person):
    def __init__(self, name, birthdate, field=None, **kwargs):
        super().__init__(name, birthdate, **kwargs) 
        self.field = field
        
    def publish_paper(self, journal):
        print(f"{self.name} published a paper in {journal}")
        
class TeacherAssistant(Person):
    def __init__(self, name, birthdate, course=None, **kwargs):
        super().__init__(name, birthdate, **kwargs) 
        self.course = course
        
    def give_lecture(self):
        print(f"{self.name} gives a lecture on {self.course}")
            

class PhDStudent(Researcher, Student, TeacherAssistant):
    def __init__(self, name, birthdate, student_id=None, field=None, course=None):
        super().__init__(name, birthdate, student_id=student_id, field=field, course=course)  # this calls all constructors up to Foo

        


# In[11]:


elena = PhDStudent("Elena", date(1995,8,8), student_id="0102", field="Cosmology", course="Programming with Python")


# In[12]:


print(dir(elena))


# In[13]:


elena.publish_paper("JCAP")


# In[14]:


elena.give_lecture()


# **Method Resolution Order (MRO)**
# 
# In multiple inheritances, the methods are executed based on the order specified while inheriting the classes.

# In[15]:


PhDStudent.__mro__


# ## Composition
# 
# Composition is an object oriented design concept that models a has a relationship. In composition, a class known as composite contains an object of another class known to as component. In other words, a composite class has a component of another class.
# 
# Relationships like this can be one-to-one, one-to-many or many-to-many, and they can be unidirectional or bidirectional, depending on the specifics of the the roles which the objects fulfil.
# 
# Composition is more flexible than inheritance because it models a loosely coupled relationship. Changes to a component class have minimal or no effects on the composite class. Designs based on composition are more suitable to change
# 
# Let's see an example of composition. First consider two classes `Student` and `Course`. An object of Student can be enrolled in many Course, while a given Course can have many students enrolled. This following implementation shows a one-to-one relationship
# 

# In[16]:


class Student(Person):
    def __init__(self, name, birthdate, student_id=None, **kwargs):
        super().__init__(name, birthdate)
        self.student_id = student_id
        self.courses = []

    def study(self, hours):
        print(f"Studying for {hours} hours")
        time.sleep(hours)
        print("Finish studying")

    def enrol_in_course(self, course):
        self.courses.append(course)
        course.students[self.student_id] = self
        
    def get_average_grade(self):
        total = 0
        n = 0
        for course in self.courses:
            if self.student_id in course.grades.keys():
                total += course.grades[self.student_id]
                n += 1
            else:
                print(f"The grade in {course.name} is not available at the moment")
        print(f"{self.name} got an average grade of: {total / n}")
    
    def get_transcript_of_records(self):
        transcript = f"Transcript of {self.name} ({self.student_id}) \n"
        for course in self.courses:
            if self.student_id in course.grades.keys():
                transcript += f"{course.course_name} ({course.course_code}): {course.get_grade_letter(course.grades[self.student_id])} \n"
            else:
                transcript += f"{course.course_name} ({course.course_code}): - \n"
        return transcript


# In[17]:


class Course:
    __ECTS__ = 6
    
    def __init__(self, name, code, credits=None):
        self.course_name = name
        self.course_code = code
        self.credits = Course.__ECTS__ if credits is None else credits
        self.students = {}
        self.grades = {}
        
    def __repr__(self):
        return f"Course({self.course_name}, {self.course_code}, credits={self.credits})"
        
    def grade_students(self, student, grades):
        for student, grade in zip(student, grades):
            if student.student_id in self.students.keys():
                self.grades[student.student_id] = grade
            else:
                print(f"The student {student.student_id} is not enrolled in {self.course_name}")
                
    def get_number_of_enrolled_students(self):
        return len(self.students)
    
    def get_average_grade(self):
        print(f"The average grade in {self.course_name} is: {sum(list(self.grade.values())) / self.get_number_of_enrolled_students()}")
        
    def print_grades(self):
        curriculum = f"{self.course_name} ({self.course_code}) grades:\n"
        for student in self.students.values():
            if student.student_id in self.grades.keys():
                curriculum += f"{student.name} ({student.student_id}):  {self.get_grade_letter(self.grades[student.student_id])} \n"
        print(curriculum)
                
    @staticmethod
    def get_grade_letter(grade):
        if (grade >= 9) and (grade <= 10):
            return "A"
        elif (grade >= 7) and (grade < 9):
            return "B"
        elif (grade >= 6) and (grade < 7):
            return "C"
        elif (grade >= 5) and (grade < 6):
            return "D"
        elif (grade >= 0) and (grade < 5):
            return "F"
        else:
            raise ValueError(f"The input grade is not valid: {grade}")
            


# In[18]:


# Instantiating several objects of the Class Students
pedro = Student("Pedro", date(1999, 4, 2), student_id="73376")
luisa = Student("Luisa", date(1999, 9, 3), student_id="58482")
irene = Student("Irene", date(1999, 1, 22), student_id="47363")
elena = Student("Elena", date(1999, 8, 8), student_id="35362")
pablo = Student("Pablo", date(1999, 5, 12), student_id="72256")

# Intantiating several objects of the Class Course
python = Course("Introduction to programming with python", "M101")
cosmo = Course("Cosmology", "M102")
particles = Course("Particle Physics", "M103")


# In[19]:


# Let the students enroll in different courses
pedro.enrol_in_course(python)
luisa.enrol_in_course(python)
irene.enrol_in_course(python)
elena.enrol_in_course(python)
pablo.enrol_in_course(python)

elena.enrol_in_course(cosmo)
pedro.enrol_in_course(cosmo)
luisa.enrol_in_course(cosmo)

irene.enrol_in_course(particles)
pablo.enrol_in_course(particles)


# In[20]:


# Let's grade the students
python.grade_students([elena, pedro, luisa, irene, pablo], [9, 8.5, 5, 9.5, 7])
cosmo.grade_students([elena, pedro, luisa, irene], [10, 7.5, 9, 7])
particles.grade_students([irene], [10])


# In[21]:


# Get the transcript of records of the students enrolled in introduction to programming
for student in python.students.values():
    print(student.get_transcript_of_records())


# In[22]:


python.print_grades()

