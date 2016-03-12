# -*- coding: utf-8 -*-
"""
@author: Bob Stine

First program, Data Mgmt & Visualization
Display univariate distribution of several variables.
"""
import pandas
import numpy
 
"""
   Convert missing data to numeric, to
   avoid ugly results in the pandas and numpy 
   functions.
"""
def conv_2_num(data, index_str):
    data[index_str] = pandas.to_numeric(data[index_str], errors = 'coerce').dropna()
    return

"""
    For a given variable, identified by "index_str", 
        convert the data to numeric and drop missing data.
        define 20 equally-sized intervals between the minimum and maximum value
        return the "groups" -- the data partitioned into these intervals.
    The return value "groups" is an instance of pandas.core.groupby.DataFrameGroupBy.
    It is a list of pairs, in which the first item is a string that identifies
    the "bin" of the group, and the second item is a DataFrame of the
    selected subset of the original data.
"""
def get_groups(data, index_str):
    conv_2_num(data, index_str)    
    bins = numpy.linspace(data[index_str].min(), data[index_str].max(), 20)
    groups = data.groupby(pandas.cut(data[index_str], bins))
    return groups
    
"""
   Main routine.
"""    
if __name__ == "__main__":
    print("")    
    print("Display univariate distribution of several variables from GapMinder.")
    print("The GapMinder data set compares various statistics across some 213 countries.")
    print("")
    print("Frequency distributions by category")
    print("Left-hand column shows range of an item's values.")
    print("Right-hand column is number of observations in that range.")
    print("")
    
    data = pandas.read_csv("gapminder.csv", low_memory=False)

    print("'alcconsumption' is annual per capita consumption of pure alcohol, in liters.")
    groups = get_groups(data, "alcconsumption")
    
    for group in groups:
        #print("type of group: ", type(group),"len: ",len(group))
        #print("types of tuple elements: <", type(group[0]), ", ",type(group[1]),">")
        print(group[0],"\t",group[1]["alcconsumption"].count())
    
    #print(groups.count().alcconsumption)
    print("")
    """ 
    print("'incomperperson' is per capita income.")
    groups = get_groups(data, "incomeperperson")
    print(groups.count().incomeperperson)
    print("")
    
    print("'lifeexpectancy' is life expectancy at birth, in years.")
    groups = get_groups(data, "lifeexpectancy")
    print(groups.count().lifeexpectancy)
    print("") 
    """    
    print("done")
