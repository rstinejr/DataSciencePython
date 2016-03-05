# -*- coding: utf-8 -*-
"""
@author: Bob Stine

First program, Data Mgmt & Visualization
Display univariate distribution of several variables.
"""
import pandas
import numpy
 
def conv_2_num(data, index_str):
    data[index_str] = data[index_str].convert_objects(convert_numeric = True)
    return
    
def print_all(data, index_str):
     print(index_str, ":")
     rowdat = data[index_str]
     print(rowdat)
     print("")
     return

def print_dist(data, index_str):
    print(index_str, ":")
    dist_cnt = data[index_str].value_counts(sort=False)
    print(dist_cnt)
    print("")
    return
     
if __name__ == "__main__":
    print("Display univariate distribution of several variables from GapMinder.")
    
    data = pandas.read_csv("gapminder.csv", low_memory=False)
    print("Rows/columns in gapminder.csv: ", len(data), "/", len(data.columns))

    
    print("Frequency distributions by category")
    print("Left-hand column shows range of an item's values.")
    print("Right-hand column is number of observations in that range.")
    
    conv_2_num(data, "alcconsumption")    
    bins = numpy.linspace(0.0, data["alcconsumption"].max(), 20)
    groups = data.groupby(pandas.cut(data["alcconsumption"], bins))
    print(groups.count().alcconsumption)
    print("")
    
    conv_2_num(data, "incomeperperson")
    bins = numpy.linspace(0.0, data["incomeperperson"].max(), 20)
    groups = data.groupby(pandas.cut(data["incomeperperson"], bins))
    print(groups.count().incomeperperson)
    print("")
    
    conv_2_num(data, "lifeexpectancy")
    bins = numpy.linspace(0.0, data["lifeexpectancy"].max(), 20)
    groups = data.groupby(pandas.cut(data["lifeexpectancy"], bins))
    print(groups.count().incomeperperson)
    
    print("done")
