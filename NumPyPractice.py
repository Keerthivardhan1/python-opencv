Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
x = np.array([1,2,3,4])
print(x)
[1 2 3 4]
x
array([1, 2, 3, 4])
type(x)
<class 'numpy.ndarray'>
type(x[1])
<class 'numpy.int32'>
x = np.array([[1,2,3] , [5,6,7]] , dtype ='int32')
x
array([[1, 2, 3],
       [5, 6, 7]])
#numpy takes all values in to float wvwn though it is int ----> upcasting

x.ndim
2

x.shape
(2, 3)

x.dtype
dtype('int32')

x.size
6

np.ones([3,3])
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])

np.ones([3,3] , dtype=bool)
array([[ True,  True,  True],
       [ True,  True,  True],
       [ True,  True,  True]])

np.zeros([2,2])
array([[0., 0.],
       [0., 0.]])

np.zeros([2,2] , dtype='int32')
array([[0, 0],
       [0, 0]])

np.zeros([2,2] , dtype = 'bool')
array([[False, False],
       [False, False]])

np.empty([2,2])
array([[0., 0.],
       [0., 0.]])

np.empty(4)
array([0., 0., 0., 0.])

np.arange(0 , 10 , 2)
array([0, 2, 4, 6, 8])

 
np.arange(0 , 10).reshape(5,2)
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])

np.arange(0 , 10).reshape(5,-1)
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])

np.arange(0 , 10).reshape(-1,2)
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])

#--- linespace

np.linspace(0 , 10 , 5)
array([ 0. ,  2.5,  5. ,  7.5, 10. ])

np.linspace(0 , 10 , 2 , dtype = "int32")
array([ 0, 10])

# logspace

np.logspace( 0 , 10 , base = 2)
array([1.00000000e+00, 1.15195282e+00, 1.32699530e+00, 1.52863599e+00,
       1.76091654e+00, 2.02849277e+00, 2.33672798e+00, 2.69180039e+00,
       3.10082705e+00, 3.57200647e+00, 4.11478293e+00, 4.74003581e+00,
       5.46029763e+00, 6.29000526e+00, 7.24578931e+00, 8.34680745e+00,
       9.61512839e+00, 1.10761743e+01, 1.27592302e+01, 1.46980313e+01,
       1.69314386e+01, 1.95042185e+01, 2.24679395e+01, 2.58820063e+01,
       2.98148502e+01, 3.43453008e+01, 3.95641662e+01, 4.55760529e+01,
       5.25014628e+01, 6.04792082e+01, 6.96691946e+01, 8.02556253e+01,
       9.24506940e+01, 1.06498838e+02, 1.22681637e+02, 1.41323458e+02,
       1.62797956e+02, 1.87535565e+02, 2.16032123e+02, 2.48858814e+02,
       2.86673613e+02, 3.30234477e+02, 3.80414538e+02, 4.38219601e+02,
       5.04808306e+02, 5.81515352e+02, 6.69878251e+02, 7.71668141e+02,
       8.88925293e+02, 1.02400000e+03])


# array with random distribution

np.random.rand(2,2)
array([[0.78005738, 0.33151826],
       [0.80917109, 0.53461413]])

np.random.randn(2,2)
array([[ 0.35768558,  1.79716978],
       [ 1.66333107, -0.04278852]])

# randn --- > gives normal distribution rand -- > uniform distribution

np.i(2)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    np.i(2)
  File "C:\Users\tekul\AppData\Local\Programs\Python\Python311\Lib\site-packages\numpy\__init__.py", line 311, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'i'. Did you mean: 'i0'?
np.identity(2)
                         
array([[1., 0.],
       [0., 1.]])

## ---  extracting elements from the array
                         
a = np.arange(10)
                         
a[a%2 == 0]
                         
array([0, 2, 4, 6, 8])

b = np.arange(9).reshape(3,3)
                         
b
                         
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
b[2,2]
                         
8

## get specific row
                         
## get specific row
                         
b[2 , :]
                         
array([6, 7, 8])

b[: , 2]
                         
array([2, 5, 8])

b[ 2 , ::2]
                         
array([6, 8])

# how to swape two rows in an array
                         

c = np.arange(6).reshape(2,-1)
                         

print(c)
                         
[[0 1 2]
 [3 4 5]]

c = c[[1,0] , :]
                         
print(c)
                         
[[3 4 5]
 [0 1 2]]

# create 5*2 array from 100 to 200 and disserence between two elements is 10
                         
np.arange(100 ,  200  ,  10 ).reshape(5,2)
                         
array([[100, 110],
       [120, 130],
       [140, 150],
       [160, 170],
       [180, 190]])

# reverse the collumn in the array
                         
d = np.arange(10).reshape(5,-1)
                         
print(d)
                         
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
d[: , 1] = d[ -1:0:-1 , 1]
                         
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    d[: , 1] = d[ -1:0:-1 , 1]
ValueError: could not broadcast input array from shape (4,) into shape (5,)
d[: , 1]
                         
array([1, 3, 5, 7, 9])
d[ -1:0:-1 , 1]
                         
array([9, 7, 5, 3])
d[ -1:: , 1]
                         
array([9])
d[ -1:0: , 1]
                         
array([], dtype=int32)
d[-1: , 1]
                         
array([9])
d[::-1 , 1]
                         
array([9, 7, 5, 3, 1])

d[: , 1] = d[ ::-1 , 1]
                         
print(d)
                         
[[0 9]
 [2 7]
 [4 5]
 [6 3]
 [8 1]]

## some useful conditions for exploratory data analysis
                         

e = np.arange(10)
                         
e[e>3]
                         
array([4, 5, 6, 7, 8, 9])

 ####    all mathametical oparation will be poformend by --- ** element wise *** and all + , - , * ,/ .. -> these are called univarsal funcion
                         

## statics and linear algebra
                         

s = np.arange(10)
                         
s.min()
                         
0

s.max()
                         
9

s = np.arange(10).reshape(2,-1)
                         
print(s) s.min() s.max()
                         
SyntaxError: invalid syntax
print(s)
                         
[[0 1 2 3 4]
 [5 6 7 8 9]]

s.min()
                         
0

np.min()
                         
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    np.min()
  File "<__array_function__ internals>", line 179, in amin
TypeError: _amin_dispatcher() missing 1 required positional argument: 'a'
>>> np.min(s)
...                          
0
>>> 
>>> np.min(s , axis = 2)
...                          
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    np.min(s , axis = 2)
  File "<__array_function__ internals>", line 180, in amin
  File "C:\Users\tekul\AppData\Local\Programs\Python\Python311\Lib\site-packages\numpy\core\fromnumeric.py", line 2918, in amin
    return _wrapreduction(a, np.minimum, 'min', axis, None, out,
  File "C:\Users\tekul\AppData\Local\Programs\Python\Python311\Lib\site-packages\numpy\core\fromnumeric.py", line 86, in _wrapreduction
    return ufunc.reduce(obj, axis, dtype, out, **passkwargs)
numpy.AxisError: axis 2 is out of bounds for array of dimension 2
>>> 
>>> np.min(s , axis = 1)
array([0, 5])
>>> 
>>> 
>>> # vertical staticing and horizaltol stacking
>>> 
>>> v1 = np.arange(5)
>>> v2 = np.arange(6,11)
>>> np.vstack(v1,v2)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    np.vstack(v1,v2)
  File "<__array_function__ internals>", line 179, in vstack
TypeError: _vhstack_dispatcher() takes 1 positional argument but 2 were given
>>> np.vstack([v1,v2])
array([[ 0,  1,  2,  3,  4],
       [ 6,  7,  8,  9, 10]])
>>> 
>>> np.hstack([v1,v2])
array([ 0,  1,  2,  3,  4,  6,  7,  8,  9, 10])
>>> 
>>> 
>>> np.hstack((v1,v2))
array([ 0,  1,  2,  3,  4,  6,  7,  8,  9, 10])

x=np.arange(10)
y=np.where(x%2==1,-1,x)
y
array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])