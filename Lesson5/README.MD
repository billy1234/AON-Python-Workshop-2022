# Lesson 5

## Map

Sometimes you want to take a set of values and map a function to them.
Providing a new set of values. This is the functional way to apply a 
function to a collection.

Python has a built in way to do this: [Map()](https://docs.python.org/3/library/functions.html#map)

Note this returns an iterator not a list. Typicaly you will place its contents in a list:

`x = list(map(...,...))`

## Filter

Sometime when working with a collection you want to take a 'sub set'
of the data. The way to do this is provide a condtion and use this to
filter the set.

Python has a built in way to do this: [Filter()](https://docs.python.org/3/library/functions.html#filter)

Note this returns an iterator not a list. Typicaly you will place its contents in a list:


`x = list(filter(...,...))`

## Pip/Packages

To install other peoples code (called packages). You use pip first install the package. For example to `numpy` in your comand line type:

    $pip install numpy


Then at the top of your script type:

    import numpy


Two popular packages for DataScience/Statistical Computing are `numpy` and `pandas`.