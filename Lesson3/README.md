# Lesson 3

## Collections

Typically we want to group lots of primitive datatypes together. To do this we use collections, the three most fundamental collections are:

* [Lists](https://docs.python.org/3/tutorial/datastructures.html) - Ordered, starts from 0 - N 

* [Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) - Exactly like lists except that you cant modify them after creating them.

* [Sets](https://docs.python.org/3/tutorial/datastructures.html#sets) - Unorderd, supports [Set operations](https://en.wikipedia.org/wiki/Set_(mathematics)#:~:text=Basic%20operations%5Bedit%5D).

* [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) - Unordered, Maps from any value to any value.

Remeber its best practice to ensure all elements of a collection are the same type.

## Tables

Tables are a special kind of collection, they can be though of like lists.

However unlike the basic collections above they are 2 dimensional. Meaning they require
2 indexes to pull out a primative value.

They can be thought of like a grid, with "Rows" and "Columns"

Eg:

        1 "hi" 3.1
        4 "ya" 6.5
        7 "na" 9.4
        1 "si" 1.6
    
Everyhing in a column should be of the same type,
and all rows should be of the same length.

A single row in a table is often called a `Record`.