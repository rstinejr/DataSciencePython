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
    print("")    
    print("Display univariate distribution of several variables from GapMinder.")
    print("The GapMinder data set compares various statistics across some 213 countries.")
    print("")
    print("Frequency distributions by category")
    print("Left-hand column shows range of an item's values.")
    print("Right-hand column is number of observations in that range.")
    print("")
    
    data = pandas.read_csv("gapminder.csv", low_memory=False)

    print("'alcconsumption' is annual per capita consumption of alcohol, in liters.")
    conv_2_num(data, "alcconsumption")    
    bins = numpy.linspace(0.0, data["alcconsumption"].max(), 20)
    groups = data.groupby(pandas.cut(data["alcconsumption"], bins))
    print(groups.count().alcconsumption)
    print("")
    
    print("'incomperperson' is per capita income.")
    conv_2_num(data, "incomeperperson")
    bins = numpy.linspace(0.0, data["incomeperperson"].max(), 20)
    groups = data.groupby(pandas.cut(data["incomeperperson"], bins))
    print(groups.count().incomeperperson)
    print("")
    
    print("'lifeexpectancy' is life expectancy at birth, in years.")
    conv_2_num(data, "lifeexpectancy")
    bins = numpy.linspace(0.0, data["lifeexpectancy"].max(), 20)
    groups = data.groupby(pandas.cut(data["lifeexpectancy"], bins))
    print(groups.count().lifeexpectancy)
    
    print("done")
