#!/usr/bin/env python
# coding: utf-8

# # OOP. Example

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


# In[2]:


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []
        
    def greet(self):
        print(f"Hello! I'm {self.name.title()}. I study {self.degree}")
        
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


# In[3]:


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
            


# In[4]:


# Instantiating several objects of the Class Students
pedro = Student("Pedro", 21, "73376")
luisa = Student("Luisa", 22, "58482")
irene = Student("Irene", 22, "47363")
elena = Student("Elena", 21, "35362")
pablo = Student("Pablo", 20, "72256")

# Intantiating several objects of the Class Course
python = Course("Introduction to programming with python", "M101")
cosmo = Course("Cosmology", "M102")
particles = Course("Particle Physics", "M103")


# In[5]:


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


# In[6]:


# Let's grade the students
python.grade_students([elena, pedro, luisa, irene, pablo], [9, 8.5, 5, 9.5, 7])
cosmo.grade_students([elena, pedro, luisa, irene], [10, 7.5, 9, 7])
particles.grade_students([irene], [10])


# ### Comparison static vs. class methods

# In[7]:


# Static methods
print(f"Number of students enrolled in {cosmo.course_name}: {cosmo.get_number_of_enrolled_students()}")


# In[8]:


# Class methods
print("Calling from class:", Course.get_grade_letter(9))
print("Calling from object:", cosmo.get_grade_letter(9))


# ## Change behaviour from different classes

# In[9]:


irene.get_average_grade()


# In[10]:


# Get the transcript of records of the students enrolled in introduction to programming
for student in python.students.values():
    print(student.get_transcript_of_records())


# In[11]:


python.print_grades()


# ```python
# class Person:
#     def greet():
#         pass
#     
# class Student(Person):
#     def greet():
#         print("Hi! I'm a student")
#         
# class Teacher(Person):
#     def greet():
#         print("Hi! I'm a teacher") 
#         
# class TeachingAssistant(Person):
#     def greet():
#         print("Hi! I'm a TA")
#         
# class PhDStudent(TeachingAssistant, Student, Teacher):
#     pass
# 
# elena = PhDStudent()
# elena.greet()
# ```

# In[12]:


class Person:
    def greet(self):
        pass
    
class Student(Person):
    def greet(self):
        print("Hi! I'm a student")
        
class Teacher(Person):
    def greet(self):
        print("Hi! I'm a teacher") 
        
class TeachingAssistant(Person):
    def greet(self):
        print("Hi! I'm a TA")
        
class PhDStudent(TeachingAssistant, Student, Teacher):
    pass


# In[13]:


elena = PhDStudent()


# ```python
# class Sales:
#     def __init__(self, id):
#         self.id = id
#         id = 100
# 
# val = Sales(123)
# print (val.id)
# ```

# In[ ]:





# In[ ]:




