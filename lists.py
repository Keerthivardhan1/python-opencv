Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=7
>>> y=x
>>> x=2
>>> print(x)
2
>>> print(y)
7
>>> l1 = [1,2,3]
>>> l2 = [1,2,3]
>>> l3 = l2
>>> l3 == l2
True
>>> l1 == l2
True
>>> l1 == l3
True
>>> l1 is l2
False
>>> l1 is l3
False
>>> l2 is l3
True
>>> 
...  
>>> 2
2
>>> 3
3
>>> 3
3
>>> type(range(3))
<class 'range'>
>>> type([1,2,3])
<class 'list'>
>>> l1 = [1,2,3]
>>> l2 = [5,2,88]
>>> print(merge(l1c, l2))
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(merge(l1c, l2))
NameError: name 'merge' is not defined
>>> print(merge(l1,l2))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(merge(l1,l2))
NameError: name 'merge' is not defined
