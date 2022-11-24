# Lesson 7

## Visualisation

To visualise data stored in a dataframe we will be using a libary called seaborn.
Just like pandas it can be installed with pip.

        pip install seaborn

This libary also comes with some nice sample datasets. For this lesson we will be
using the 'penguins' dataset. To import this dataset as a dataframe use:

    df = sns.load_dataset('penguins')


Seaborn has a histogram, scatter and box plot :

        sns.histplot(...) # Histogram
        sns.relplot(... ) # Scatter plot (function called 'relationship plot')
        sns.catplot(... kind="box") # Box plot (function called 'category plot')