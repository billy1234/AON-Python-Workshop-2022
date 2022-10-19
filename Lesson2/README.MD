# Lesson 2


## Functions

In Python to make a reusable sections of code you can define [Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions).

These are a great way to package up reusable code. Typicaly a function will take parameters and can return a value.


## Data Types

Python has some built in [Data types](https://docs.python.org/3/library/stdtypes.html). Its important to understand the difference between these types.


Some of the more simple types are: **Booleans**, **Integers**, **Floats** and **Strings**.

When you declare a variable you can actually specify the type of the vairable. This will help gaurd against confusing its type.

`text_var : str = 'hello world'`

## Types of numbers

[Set Theory](https://en.wikipedia.org/wiki/Set_theory) is a field of math that deals with "Collections of objects". This models many concepts within computer science.


One verry important concept is some of the "Sets" of numbers. pulled from a slide deck from [Eastern Illinois Universitys'](https://castle.eiu.edu/~mathcs/mat2120/index/set03-2x3.pdf) website:


        ℕ — Natural or Counting numbers: {1, 2, 3, ... }

        W — Whole Numbers: {0, 1, 2, 3, ... }

        𝕀 — Integers: {... , -3, -2, -1, 0, 1, 2, 3, ... }

        ℚ — Rational numbers: {p/q | p , q ∈ 𝕀, q ≠ 0 }

        ℝ — Real Numbers: { x | x is a number that can be written
        as a decimal }

        Irrational numbers: { x | x is a real number and x cannot be written as a quotient of integers }.
        Examples are: π, √2, and 3√4

        ∅ — Empty Set: { }, the set that contains nothing


When a number is stored in Python (Or any other language) it will almost always be stored as a:

* [Integer](https://en.wikipedia.org/wiki/Integer_(computer_science)) 
* [Floating Precision Decimal](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)
* [Fixed Precision Decimal](https://en.wikipedia.org/wiki/Fixed-point_arithmetic)

All of these types of numbers will have a "Lower" and "Upper" bound. If you try to store a number that is "Too big" it will throw an error.


One thing to note is "[Signed](https://en.wikipedia.org/wiki/Signed_number_representations)" and "Unsigned" refers to if the types of numbers allow negatives. Python allows negaives for all of its number types.


## Collections

Typically we want to group lots of primitive datatypes together. To do this we use collections, the three most fundamental collections are:

* [Lists](https://docs.python.org/3/tutorial/datastructures.html) - Ordered, starts from 0 - N 

* [Sets](https://docs.python.org/3/tutorial/datastructures.html#sets) - Unorderd, supports [Set operations](https://en.wikipedia.org/wiki/Set_(mathematics)#:~:text=Basic%20operations%5Bedit%5D).

* [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) - Unordered, Maps from any value to any value.