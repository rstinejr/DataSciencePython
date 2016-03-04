# -*- coding: utf-8 -*-
"""
@author: Bob Stine

First program, Data Mgmt & Visualization
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

    #print("Rows/columns in gapminder.csv: ", len(data), "/", len(data.columns))

    #conv_2_num(data, "alcconsumption")
    data = pandas.read_csv("gapminder.csv", low_memory=False)
    data["alcconsumption"] = data["alcconsumption"].convert_objects(convert_numeric = True)
    bins = numpy.linspace(data.alcconsumption.min(), data.alcconsumption.max(), 5)
    groups = data.groupby(pandas.cut(data.alcconsumption, bins))
    print("try count by bin:")
    print(groups.count().alcconsumption)
    print("done")
