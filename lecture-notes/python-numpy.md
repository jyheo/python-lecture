layout: true
.top-line[]

---
class: center, middle
# Python - Numpy

허준영(jyheo@hansung.ac.kr)

---
## Contents
* Numpy
* Creating Array
* Indexing
* Slicing
* Basic Operations
* Other Operations
* Simple Statistics
* Broadcasting
* Array Reshape
* Linear Algebra
* File
* Exercise

---
## Numpy
* Extension to Python for **multi-dimensional arrays**
* Efficiency
* For scientific computing
* import Numpy
```python
>>> import numpy as np
>>> list = [1, 2, 3, 4]
>>> type(list)
<class 'list'>
>>> ary = np.array(list)
>>> type(ary)
<class 'numpy.ndarray'>
>>> list
[1, 2, 3, 4]
>>> ary
array([1, 2, 3, 4])
```

---
## Creating Array
### Creating array with List/array
* np.array( LIST )
```python
>>> d2 = np.array([[0, 1, 2], [3, 4, 5]])
>>> d2
array([[0, 1, 2],
       [3, 4, 5]])
>>> d3 = np.array([d2, d2])
>>> d3
array([[[0, 1, 2],
        [3, 4, 5]],

       [[0, 1, 2],
        [3, 4, 5]]])
>>> d2.ndim
2
>>> d2.shape
(2, 3)
>>> d3.ndim
3
>>> d3.shape
(2, 2, 3)
```

---
## Creating Array
### Creating special array
* np.arange(START, END, STEP): evenly spaced values within a given interval
* np.linspace(START, END, NUM_OF_POINTS): evenly spaced numbers over a specified interval
* np.ones(SHAPE, TYPE): a new array of given shape and type, filled with ones
* np.zeros(SHAPE, TYPE): a new array of given shape and type, filled with zeros
* np.eye(ROWS, COLS): a 2-D array with ones on the diagonal and zeros elsewhere
* np.diag(ARRAY): extract a diagonal or construct a diagonal array

---
## Creating Array
### Creating special array
```python
>>> np.arange(5)
array([0, 1, 2, 3, 4])
>>> np.arange(0, 5, 2)
array([0, 2, 4])
>>> np.linspace(0, 1, 5)
array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])
>>> np.linspace(0, 1, 5, endpoint=False)  # except end point
array([ 0. ,  0.2,  0.4,  0.6,  0.8])
>>> np.ones((2,2))
array([[ 1.,  1.],
       [ 1.,  1.]])
>>> np.zeros((2,2))
array([[ 0.,  0.],
       [ 0.,  0.]])
>>> np.eye(2)
array([[ 1.,  0.],
       [ 0.,  1.]])
>>> d = np.diag([1, 2]) # construct a diagonal array
>>> d
array([[1, 0],
       [0, 2]])
>>> np.diag(d) # extract a diagonal
array([1, 2])
```

---
## Creating Array
### Random array
* np.random.rand(SHAPE): random values in a given shape
* np.random.randn(SHAPE): normal distribution
* try **help(np.random)**

```python
>>> np.random.rand(5)   # uniform distribution
array([ 0.47890201,  0.47483496,  0.3979876 ,  0.20977161,  0.61156593])
>>> np.random.rand(2, 5)
array([[ 0.65987544,  0.80931004,  0.10713224,  0.40180672,  0.60894812],
       [ 0.74707904,  0.46808531,  0.92194004,  0.26405604,  0.60130934]])
>>> np.random.randn(5)  # normal distribution
array([ 1.24009415, -0.3490193 ,  0.43793239,  2.46981379,  0.16273478])
>>> help(np.random)
```

---
## Creating Array
### Data type for array values
* int, float, bool, complex
* Default type is float
```python
>>> np.array([1, 2, 3]).dtype
dtype('int32')
>>> np.array([1, 2, 3], dtype=float).dtype
dtype('float64')
>>> np.array([1., 2, 3]).dtype
dtype('float64')
>>> np.array([1+1j, 2+2j, 3+3j]).dtype
dtype('complex128')
>>> np.array([True, False, True]).dtype
dtype('bool')
>>> np.array([True, False, True], dtype=int).dtype
dtype('int32')
```

---
## Indexing
* Use [ ] operator
* [x, y] for 2D array
* [x, y, z] for 3D array

```python
>>> a = np.arange(10)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a[0], a[5], a[-1]
(0, 5, 9)
>>> b = np.random.rand(3, 3) # 2-dimentional array
>>> b.shape
(3, 3)
>>> b[0, 0], b[1, 1], b[2, 2]
(0.63595763265126359, 0.62567509371895325, 0.70253894348755386)
>>> np.diag(b)
array([ 0.63595763,  0.62567509,  0.70253894])
>>> c = np.random.rand(3, 3, 3)  # 3-dimentional array
>>> c.shape
(3, 3, 3)
>>> c[0, 0, 0]
0.87835050827842043
```

---
## Slicing
* Use [ : : ] operator
* [x_start: x_end: x_step, y_start: y_end: y_step] for 2D array

```python
>>> a = np.arange(10)
>>> a[5:8]
array([5, 6, 7])
>>> a[5:8] = 10     # slicing and assignment
>>> a
array([ 0,  1,  2,  3,  4, 10, 10, 10,  8,  9])
>>> b = np.reshape(np.arange(16), (4,4))
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
>>> b[1:3, 1:3]
array([[ 5,  6],
       [ 9, 10]])
>>> b[::2, ::2]
array([[ 0,  2],
       [ 8, 10]])
```

---
## Slicing
* A slicing operation creates a view on the original array
    - The original array is **not copied**

```python
>>> a = np.arange(10)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> b = a[::2]
>>> b
array([0, 2, 4, 6, 8])
>>> np.may_share_memory(a, b)
True
>>> b[2] = 999
>>> b
array([  0,   2, 999,   6,   8])
>>> a
*array([  0,   1,   2,   3, 999,   5,   6,   7,   8,   9])
>>> c = b.copy()
>>> np.may_share_memory(b, c)
False
>>> c[2] = -1
>>> b
array([  0,   2, 999,   6,   8])
>>> c
array([ 0,  2, -1,  6,  8])
```

---
## Slicing
### Boolean mask
* Extract a sub-array with the maks
    - the sub-array is **copied** from the original array

```python
>>> a = np.arange(20)
>>> a % 3 == 0
array([ True, False, False,  True, False, False,  True, False, False,
        True, False, False,  True, False, False,  True, False, False,
        True, False], dtype=bool)
>>> a[a % 3 == 0]
array([ 0,  3,  6,  9, 12, 15, 18])
>>> a[a % 3 == 0] = -1
>>> a
array([-1,  1,  2, -1,  4,  5, -1,  7,  8, -1, 10, 11, -1, 13, 14, -1, 16,
       17, -1, 19])
```

---
## Slicing
### Indxing with an array
* Extract a sub-array with the indexing array
    - the sub-array is **copied** from the original array

```python
>>> a = np.arange(20) * 10
>>> a[[5, 7]]
array([50, 70])
>>> a[[5, 7]] = -1
>>> a
array([  0,  10,  20,  30,  40,  -1,  60,  -1,  80,  90, 100, 110, 120,
       130, 140, 150, 160, 170, 180, 190])
>>> b = a[[5, 7]]
>>> b
array([-1, -1])
>>> b[0] = 999
>>> b
array([999,  -1])
>>> a
array([  0,  10,  20,  30,  40,  -1,  60,  -1,  80,  90, 100, 110, 120,
       130, 140, 150, 160, 170, 180, 190])
```

---
## Basic Operations
### Arithmetic
* +, -, \* , \*\*

```python
>>> a = np.arange(5)
>>> b = np.arange(2, 7)
>>> a
array([0, 1, 2, 3, 4])
>>> b
array([2, 3, 4, 5, 6])
>>> a + 1
array([1, 2, 3, 4, 5])
>>> a ** 2
array([ 0,  1,  4,  9, 16], dtype=int32)
>>> a + b
array([ 2,  4,  6,  8, 10])
>>> a * b       # Scalar , not Matrix Multiplication
array([ 0,  3,  8, 15, 24])
```

---
## Basic Operations
### Logical
* ==, >, <, np.Logical_or, np.logical_and

```python
>>> a = np.array([0, 1, 2, 3, 4, 5])
>>> b = np.array([1, 0, 2, 5, 3, 4])
>>> a == b
array([False, False,  True, False, False, False], dtype=bool)
>>> a > b
array([False,  True, False, False,  True,  True], dtype=bool)
>>> np.logical_and(a, b)
array([False, False,  True,  True,  True,  True], dtype=bool)
>>> np.logical_or(a, b)
array([ True,  True,  True,  True,  True,  True], dtype=bool)
```

---
## Other Operations
* np.array_equal, np.log, np.sin, np.exp

```python
>>> a = np.arange(5)
>>> b = np.arange(1, 6)
>>> c = np.arange(5)
>>> np.array_equal(a, b)
False
>>> np.array_equal(a, c)
True
>>> np.log(b)
array([ 0.        ,  0.69314718,  1.09861229,  1.38629436,  1.60943791])
>>> np.sin(a)
array([ 0.        ,  0.84147098,  0.90929743,  0.14112001, -0.7568025 ])
>>> np.exp(a)
array([  1.        ,   2.71828183,   7.3890561 ,  20.08553692,  54.59815003])
```

---
## Simple Statistics
* np.sum, np.min, np.argmin, np.all, np.any
* np.mean, np.median, np.std

```python
>>> a = np.arange(5)
>>> a
array([0, 1, 2, 3, 4])
>>> a.sum()
10
>>> np.sum(a)
10
>>> np.min(a)
0
>>> np.argmin(a)  # index of min element
0
>>> np.all(a)  # All True?
False
>>> np.any(a)  # Anyone True?
True
>>> np.mean(a)
2.0
>>> np.median(a)
2.0
>>> np.std(a)
1.4142135623730951
```

---
## Broadcasting

<img src="images/numpy_broadcasting.png" width=80%>
.footnote[From "http://www.scipy-lectures.org/_images/numpy_broadcasting.png"]

---
## Broadcasting
```python
>>> a = np.array([[0, 0, 0], [10, 10, 10], [20, 20, 20], [30, 30, 30]])
>>> b = np.array([0, 1, 2])
>>> a
array([[ 0,  0,  0],
       [10, 10, 10],
       [20, 20, 20],
       [30, 30, 30]])
>>> b
array([0, 1, 2])
>>> a + b
array([[ 0,  1,  2],
       [10, 11, 12],
       [20, 21, 22],
       [30, 31, 32]])
>>> a = np.array([[0], [10], [20], [30]])
>>> a
array([[ 0],
       [10],
       [20],
       [30]])
>>> a + b
array([[ 0,  1,  2],
       [10, 11, 12],
       [20, 21, 22],
       [30, 31, 32]])
```

---
## Array Reshape
* array.T, np.reshape()

```python
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> a
array([[1, 2, 3],
       [4, 5, 6]])
>>> b = a.T   # Transpose of a
>>> b         # T return a view
array([[1, 4],
       [2, 5],
       [3, 6]])
>>> a.shape
(2, 3)
>>> a.reshape((3, 2)) # reshape may return view or copy
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> a.reshape((3, -1)) # unspecified (-1) value is inferred
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> np.arange(4 * 4).reshape((4, 4))
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
```

---
## Linear Algebra
* Matrix Multiplication, np.dot(), np.linalg.multi_dot()

```python
>>> a
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
>>> np.dot(a, a)
array([[ 15,  18,  21],
       [ 42,  54,  66],
       [ 69,  90, 111]])
>>> a = np.arange(6).reshape((2,3))
>>> b = np.arange(15).reshape((3,5))
>>> c = np.arange(10).reshpae((5,2))
>>> np.linalg.multi_dot([a, b, c])
array([[ 680,  835],
       [2120, 2590]])
```

---
## Linear Algebra
* np.inner(), np.outer(), np.linalg.matrix_power(M, n)

```python
>>> a = [1, 2]
>>> b = [2, 3]
>>> np.inner(a, b)
8
>>> np.outer(a, b)
array([[2, 3],
       [4, 6]])
>>> m = [[1, 2], [3, 4]]
>>> np.linalg.matrix_power(m, 10)
array([[ 4783807,  6972050],
       [10458075, 15241882]])
```

---
## Linear Algebra
* Eigenvalue, eigenvector: np.linalg.eig()
* Determinant: np.linalg.det()
* Inverse of a Matrix: np.linalg.inv()

```python
>>> a = np.arange(4).reshape((2,2))
>>> a
array([[0, 1],
       [2, 3]])
>>> np.linalg.eig(a)
(array([-0.56155281,  3.56155281]), array([[-0.87192821, -0.27032301],
       [ 0.48963374, -0.96276969]]))
>>> np.linalg.det(a)
-2.0
>>> np.linalg.inv(a)
array([[-1.5,  0.5],
       [ 1. ,  0. ]])
>>> np.dot(np.linalg.inv(a), a)
array([[ 1.,  0.],
       [ 0.,  1.]])
```

---
## Linear Algebra
* np.linalg.solve(): Solve a system of linear equations

```python
*>>> # Solve the system of equations: 3 * x0 + x1 = 9 and x0 + 2 * x1 = 8
>>> a = np.array([[3,1], [1,2]])
>>> b = np.array([9,8])
>>> x = np.linalg.solve(a, b)
>>> x
array([ 2.,  3.])
>>> np.allclose(np.dot(a, x), b) # Compare with tolerance
True
```

---
## File
* np.loadtxt()
    - Load data from a text file.
    - Each row in the text file must have the same number of values.

```python
>>> from io import StringIO
>>> c = StringIO('0 1\n2 3')
>>> np.loadtxt(c)
array([[0., 1.],
       [2., 3.]])
>>> d = StringIO('M 21 72\nF 35 58')
>>> np.loadtxt(d, dtype={'names':('gender', 'age', 'weight'), 'formats':('S1', 'i4', 'f4')})
array([(b'M', 21, 72.), (b'F', 35, 58.)],
      dtype=[('gender', 'S1'), ('age', '<i4'), ('weight', '<f4')])
>>> e = StringIO('0, 1, 2\n3, 4, 5')
>>> np.loadtxt(e, delimiter=',', usecols=(0, 2))
array([[0., 2.],
       [3., 5.]])
```

---
## Exercise
### Array Manipulation
* Make following array using np.arange() and so on.
    - Hint: reshape, T
```python
[[1,  6, 11],
 [2,  7, 12],
 [3,  8, 13],
 [4,  9, 14],
 [5, 10, 15]]
```
* Make an array with only 2nd and 4th rows of the above array.
    - Hint: Slicing
* Make a random array, which shape is (10,) and find an index whose value is closest to 0.5.
    - Hint: np.abs, np.argmin

---
## Exercise
### Load, shuffle, and Slice dataset

```python
>>> ds = np.DataSource()
>>> url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/\
... pima-indians-diabetes/pima-indians-diabetes.data'
>>> f = ds.open(url)
>>> dataset = np.loadtxt(f, delimiter=',')
>>> f.close()
>>> np.random.seed(8)
>>> np.random.shuffle(dataset)
>>> X = dataset[:,0:8]
>>> Y = dataset[:,8]
```

---
## Exercise - Markov Chain
* **P** is Transition matrix, and **p** is probability distribution on the states
    1. 0 <= P[i,j] <= 1: probability to go from state i to state j
    2. Transition rule: p<sub>new</sub> = P<sup>T</sup> p<sub>old</sub>
    3. all(sum(P, axis=1) == 1), p.sum() == 1: normalization
* Write a script that works with 5 states
    - Constructs a random matrix, and normalizes each row so that it is a transition matrix.
    - Starts from a random (normalized) probability distribution p and takes 50 steps => p<sub>50</sub>
    - Computes the stationary distribution: the eigenvector of P.T with eigenvalue 1 (numerically: closest to 1) => p<sub>stationary</sub>
* Remember to normalize the eigenvector
    - Checks if p<sub>50</sub> and p<sub>stationary</sub> are equal to tolerance 1e-5

.footnote[http://www.scipy-lectures.org/intro/numpy/exercises.html#markov-chain]
