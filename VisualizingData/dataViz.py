# -*- coding: utf-8 -*-
"""
Week 4 Assignment, Data Management and Visualization

@author: Bob Stine
"""
import pandas
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
   and functions. Drop "na" values.
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
    
    print("Statistical summary of per capita alcohol consumption across countries")
    print("Quantity is liters/year of pure ethanol")
    print(df["alcconsumption"].describe())
    print("")
    
    print("Statistical summary of per capita income")
    print("Quantity is US$, from year 2000")
    print(df["incomeperperson"].describe())
    print("")
    
    print("Statistical summary of life expectancy at birth")
    print("Quantity is years")
    print(df["lifeexpectancy"].describe())

    plt.figure(1)
    seaborn.distplot(df['alcconsumption'].dropna(), kde = False)
    plt.xlabel("Liters of Alcohol") 
    plt.title("Per capita alcohol consumption")
    plt.savefig("uni_alcconsumption.png",format="png")
    
    plt.figure(2)
    seaborn.distplot(df["incomeperperson"].dropna(), kde = False)
    plt.xlabel("Income, US$")
    plt.title("Per capita income in US$ from 2000")
    plt.savefig("uni_incomeperperson.png", format = "png")

    plt.figure(3)
    seaborn.distplot(df["lifeexpectancy"].dropna(), kde = False)
    plt.xlabel("Years")
    plt.title("Life expectancy at birth")
    plt.savefig("uni_lifeexpectancy.png", format = "png")
    
    plt.figure(4)
    scat_inc_alc = seaborn.regplot(x = 'alcconsumption', y='incomeperperson', 
                                   fit_reg = False, data=df)
    plt.xlabel('Alcohol Consumption')
    plt.ylabel('Per Capita Income')
    plt.title('Scatterplot, alcohol consumption and per capita income')
    plt.savefig('scat_alc_inc.png', format = 'png')


    plt.figure(5)
    scat_life_alc = seaborn.regplot(x = 'alcconsumption', y = 'lifeexpectancy',
                                    fit_reg = False, data = df)  
    plt.xlabel('Alcohol Consumption')
    plt.title('Scatterplot, alcohol consumption and life expectancy')
    plt.savefig('scat_alc_life.png', format = 'png')
    
    print("Done")