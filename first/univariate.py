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
    
if __name__ == "__main__":
    print("Display univariate distribution of several variables from GapMinder.")
    print("")
    print("Frequency distributions by category")
    print("Left-hand column shows range of an item's values.")
    print("Right-hand column is number of observations in that range.")
    
    data = pandas.read_csv("gapminder.csv", low_memory=False)

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
