# -*- coding: utf-8 -*-
"""
Week 4 Assignment, Data Management and Visualization

@author: Bob Stine
"""
import pandas
import numpy
import seaborn
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Start week 4 program")
    df = pandas.read_csv("../gapminder.csv")
    print("columns:")
    print(df.columns.values)
    print("Done")