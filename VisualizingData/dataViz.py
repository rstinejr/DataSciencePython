# -*- coding: utf-8 -*-
"""
Week 4 Assignment, Data Management and Visualization

@author: Bob Stine
"""
import pandas
import numpy
import seaborn
import matplotlib.pyplot as plt

"""
    Configure pandas package so that it does not impose max row
    and max column limits on display.  
    Also, provide work-around for potential runtime error when displaying
    floats.
"""
def init_pandas():
    pandas.set_option('display.max_columns', None)
    pandas.set_option('display.max_rows',    None)
    # Bug fix for display formats, with a cute little lambda function.
    pandas.set_option('display.float_format', lambda x:'%f'%x)
    return
    
"""
   Convert missing data to numeric, to avoid ugly results in the pandas 
   and numpy functions. Drop "na" values.
"""
def conv_2_num(data, index_str):
    data[index_str] = pandas.to_numeric(data[index_str], errors = 'coerce').dropna()
    return

if __name__ == "__main__":
    print("Start week 4 program")
    init_pandas()
    df = pandas.read_csv("../gapminder.csv")
    
    conv_2_num(df, "alcconsumption")
    conv_2_num(df, "incomeperperson")
    conv_2_num(df, "lifeexpectancy")

    plt.figure(1)
    plt.xlabel("Liters of Alcohol") 
    plt.title("Per capita alcohol consumption")
    seaborn.distplot(df['alcconsumption'].dropna(), kde = False)
    plt.savefig("uni_alcconsumption.png",format="png")
    
    plt.figure(2)
    plt.xlabel("Income, US$")
    plt.title("Per capita income in US$ from 2000")
    seaborn.distplot(df["incomeperperson"].dropna(), kde = False)
    plt.savefig("uni_incomeperperson.png", format = "png")

    plt.figure(3)
    plt.xlabel("Years")
    plt.title("Life expectancy at birth")
    seaborn.distplot(df["lifeexpectancy"].dropna(), kde = False)
    plt.savefig("uni_lifeexpectancy.png", format = "png")
    
    print("Done")