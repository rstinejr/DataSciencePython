# -*- coding: utf-8 -*-
"""
@author: Bob Stine

Data Mgmt & Visualization
Display univariate distribution of several variables.
"""
import pandas
import numpy
 
"""
   Convert missing data to numeric, to avoid ugly results in the pandas 
   and numpy functions. Drop "na" values.
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
    Print frequency distribution of a variable withing a DataFrameGroupBy object.
    "index_str" is the name of the variable for which we display counts
    within intervals.
"""
def print_groups(groups, index_str):
    print("   %-21s  count" % ("interval"))    
    for group in groups:
        print("%-24s    %d" % (group[0],group[1][index_str].count()))
    print("")
    return
    
"""
   Main routine.
"""    
if __name__ == "__main__":
    print("")    
    print("Display univariate distribution of several variables from GapMinder.")
    print("The GapMinder data set compares various statistics across some 213 countries.")
    print("")
    print("Frequency distributions by category")
    print("")
    
    data = pandas.read_csv("../gapminder.csv", low_memory=False)

    groups = get_groups(data, "alcconsumption")
    print("Frequency distribution of annual per capita consumption of pure alcohol, in liters.")
    print_groups(groups, "alcconsumption")

    groups = get_groups(data, "incomeperperson")
    print("Frequency distribution of annual per capita income, in US$ from 2000")
    print_groups(groups,"incomeperperson")

    data.loc[data.incomeperperson > 45000.0,'incomeperperson'] = 45000.00
    groups = get_groups(data, "incomeperperson")
    print("Frequency distribution of recoded annual per capita income")
    print_groups(groups,"incomeperperson")
   
    
    groups = get_groups(data, "lifeexpectancy")
    print("Frequency distribution of life expectancy at birth, in years.")
    print_groups(groups, "lifeexpectancy")
    
    print("done")