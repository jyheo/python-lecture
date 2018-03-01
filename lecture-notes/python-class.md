layout: true
.top-line[]

---
class: center, middle
# Python - Class

허준영(jyheo@hansung.ac.kr)

---
## Contents
* Python is OOP
* Class & Objects
* Constructor & Methods 
* Class Variables & Destructor
* Class Methods
* Static Methods
* Inheritance
* Iterator
* Generator

---
## Python is OOP
* Python is an object-oriented programming language
* Class
    - A blueprint for an object
    - Defines a set of attributes and methods
* Object
    - An instance of a class

---
## Class & Objects
* Define a Class and make an object(instance) of the Class

```python
>>> class Orange:  # define a class
...     pass
...
>>> orange1 = Orange()  # make an object of the Orange class
>>> orange1.attr1 = 1   # add attributes to the object not the class
>>> orange1.attr2 = 'fruit'
>>> print(orange1.attr1, orange1.attr2)
1 fruit
```

---
## Constructor & Methods
* Where define attributes?
    - in the constructor or methods

```python
>>> class Orange:
...     def __init__(self):  # Constructor
...             self.attr1 = 1   # add attribute
...     def method1(self):   # Method
...             self.attr2 = 'fruit'   # add attribute
...
>>> orange1 = Orange()
>>> orange1.attr1
1
>>> orange1.attr2          # attr2 is not defined yet.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Orange' object has no attribute 'attr2'
>>> orange1.method1()      # attr2 is defined.
>>> orange1.attr2
'fruit'
```

---
## Constructor & Methods
* Arguments passing

```python
>>> class Orange:
...     def __init__(self, color='yellow'):  # 'yellow' is default value for the color
...             self.color = color
...     def print(self, num):
...             print(self.color, num)
...
>>> orange1 = Orange()   # make an instance with default argument
>>> orange2 = Orange('red')   # make an instance with argument 'red'
>>> orange1.print(1)
yellow 1
>>> orange2.print(2)
red 2
```

---
## Class Variables & Destructor
* Define variables of a Class

```python
>>> class Orange:
...     fruits = 0    # class variable
...     def __init__(self):
...             self.__class__.fruits += 1   # class variable
...     def __del__(self):   # Destructor
...             self.__class__.fruits -= 1   # class variable
...
>>> orange1 = Orange()
>>> orange1.fruits    # class variable
1
>>> Orange.fruits     # class variable
1
>>> orange2 = Orange()
>>> orange1.fruits    # class variable
2
```

---
## Class Methods
* Class methods can access only class variables

```python
>>> class Orange:
...     fruits = 0
...     def __init__(self, color):
...             self.color = color
...     def print(self):
...             print(self.color, Orange.fruits)
*...     @classmethod
*...     def red(cls):
...             cls.fruits += 1
...             return cls('red')
*...     @classmethod
*...     def yellow(cls):
...             cls.fruits += 1
...             return cls('yellow')
...
>>> o1 = Orange.red()
>>> o2 = Orange.yellow()
>>> o1.print()
red 2
>>> o2.print()
yellow 2
```

---
## Class Methods
* a Singleton implementation with class method

```python
>>> class Singleton:
...     __instance = None
...     @classmethod
...     def getInstance(cls):
...         if cls.__instance == None:
...             cls()
...         return cls.__instance
...     def __init__(self):
...         if self.__class__.__instance != None:
...             raise Exception("This is a singleton!")
...         else:
...             self.__class__.__instance = self
...
>>> s = Singleton.getInstance()
>>> print(s)
<__main__.Singleton object at 0x7f4635c71470>
>>> s2 = Singleton.getInstance()
>>> print(s2)
<__main__.Singleton object at 0x7f4635c71470>
```

* Other singleton implemtations
    - http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html

---
## Static Methods
* Neither cls nor self

```python
>>> class Orange:
...     def __init__(self, color):
...             self.color = color
...     def test(self):
...             print('instance method', self.color)
*...     @staticmethod
*...     def test2():
...             print('static method')
...
>>> o = Orange('orange')
>>> o.test()
instance method orange
>>> o.test2()
static method
>>> Orange.test2()
static method
```

---
## Inheritance

* Isinstance
* Issubclass

---
## Iterator

---
## Generator