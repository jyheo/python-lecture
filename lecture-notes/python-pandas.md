layout: true
.top-line[]

---
class: center, middle
# Python - Pandas

허준영(jyheo@hansung.ac.kr)

---
## Contents


---
## Pandas
* Pandas is an open source, BSD-licensed library for the Python programming language
    - providing high-performance, easy-to-use data structures and data analysis tools
* Features
    - Tools for loading data
    - Data alignment and integrated handling of missing data.
    - Reshaping and pivoting of date sets.
    - Label-based slicing, indexing and subsetting of large data sets
    - Columns from a data structure can be deleted or inserted.
    - High performance merging and joining of data.
    - Time Series functionality.

---
## Pandas Object
* Series
    - 1D, size-immutable array
* Data Frame
    - 2D, tabular, size-mutable array
    - Most used data structure
* Panel
    - 3D, size-mutalbe array

```python
import pandas as pd
import numpy as np
```

---
## Series
* pd.Series(array, index)

```python
>>> pd.Series([1,3,5,np.nan,6,8])
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
>>> s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
>>> print(s)
a    1
b    2
c    3
dtype: int64
>>> s[0]
1
>>> s['a']
1
>>> s.values   # numpy array
array([1, 2, 3])
```

---
## Data Frame
* Data is aligned in a tabular in rows and columns
* pd.DataFrame(data, index, columns, dtype, copy)

```python
>>> pd.DataFrame(np.arange(3))
   0
0  0
1  1
2  2
>>> pd.DataFrame(np.arange(3), columns=['num'])
   num
0    0
1    1
2    2
>>> data = np.array([np.arange(3), ['a', 'b', 'c']]).T
>>> data
array([['0', 'a'],
       ['1', 'b'],
       ['2', 'c']],
      dtype='<U21')
>>> pd.DataFrame(data, columns=['num', 'alpha'])
  num alpha
0   0     a
1   1     b
2   2     c
```

---
## Data Frame
* Create data frame with Dict
```python
>>> data = {'num':[0, 1, 2], 'alpha':['a', 'b', 'c']}
>>> pd.DataFrame(data)  # by Dict
  alpha  num
0     a    0
1     b    1
2     c    2
>>> data = [{'alpha':'a', 'num':0}, {'num':1, 'alpha':'b'}, {'num':2}]
>>> pd.DataFrame(data)  # by list of Dict
  alpha  num
0     a    0
1     b    1
2   NaN    2
```

---
## Data Frame
### Column Selection
```python
>>> data = {'num': [0, 1, 2], 'alpha':['a', 'b', 'c'], 'numf':[0., 1., 2.]}
>>> df = pd.DataFrame(data)
>>> df
  alpha  num  numf
0     a    0   0.0
1     b    1   1.0
2     c    2   2.0
>>> df['num']    # Column Selection
0    0
1    1
2    2
>>> df[['num', 'numf']]
   num  numf
0    0   0.0
1    1   1.0
2    2   2.0
```

---
## Data Frame
### Column Addition and Deletion
```python
>>> df
  alpha  num  numf
0     a    0   0.0
1     b    1   1.0
2     c    2   2.0
>>> df['new'] = pd.Series([10, 20, 30])   # Add a New Column
>>> df
  alpha  num  numf  new
0     a    0   0.0   10
1     b    1   1.0   20
2     c    2   2.0   30
>>> df['num'] + df['new']   # Addition (arithmetic)
0    10
1    21
2    32
dtype: int64
>>> del df['new']    # Delete a Column
>>> df
  alpha  num  numf
0     a    0   0.0
1     b    1   1.0
2     c    2   2.0
```

---
## Data Frame
### Row Selection
* df.loc(), df.iloc(), df[]

```python
>>> data = {'num': [0, 1, 2], 'alpha':['a', 'b', 'c'], 'numf':[0., 1., 2.]}
>>> index = ['ia', 'ib', 'ic']
>>> df = pd.DataFrame(data, index=index)
>>> df
   alpha  num  numf
ia     a    0   0.0
ib     b    1   1.0
ic     c    2   2.0
>>> df.loc['ib']     # Row by index (row label)
alpha    b
num      1
numf     1
Name: ib, dtype: object
>>> df.iloc[1]       # Row by integer
alpha    b
num      1
numf     1
Name: ib, dtype: object
>>> df[:2]            # Row Selection
   alpha  num  numf
ia     a    0   0.0
ib     b    1   1.0
```

---
## Data Frame
### Row Addition and Deletion
* df.append(), df.drop()
```python
>>> df2 = pd.DataFrame([{'alpha':'d', 'num':3}], index=['id'])
>>> df2
   alpha  num
id     d    3
>>> df = df.append(df2)   # returns a View with the DataFrame, df2
>>> df
   alpha  num  numf
ia     a    0   0.0
ib     b    1   1.0
ic     c    2   2.0
id     d    3   NaN
>>> df = df.drop('id')     # returns a View without the Row
>>> df
   alpha  num  numf
ia     a    0   0.0
ib     b    1   1.0
ic     c    2   2.0
>>> df.drop(['ia', 'ib'])    # returns a View without the Rows
   alpha  num  numf
ic     c    2   2.0
>>> df     # Guess the output
```

---
## References
* https://pandas.pydata.org/pandas-docs/stable/10min.html
* https://www.tutorialspoint.com/python_pandas/
* https://pythonprogramming.net/data-analysis-python-pandas-tutorial-introduction/
* https://github.com/jvns/pandas-cookbook
* https://bitbucket.org/hrojas/learn-pandas
