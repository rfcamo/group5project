# import dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import folium


# subplot
def mysubplot(x1_data,y1_data, y2_data, xlabel, y1_label, y2_label, xticklabel, xlim, fname):
    '''
    mysubplot is to plot 2 graphs with the same x-axis, in 2 y-axis.
    prefix - 1 is for the first data
    prefix - 2 is for the 2nd data
    xticklabel - is for labelling the x-axis
    xlim - is limitation for x-axis, for the following:
        11 - mining and petroleum
        12 - arrival and departure
    '''
    fig,ax = plt.subplots()
    # make a plot
    ax.plot(x1_data, y1_data, color="red", marker="o")
    # set x-axis label
    ax.set_xlabel("Year",fontsize=14)
    # set y-axis label
    ax.set_ylabel(y1_label,color="red",fontsize=14)

    # twin object for two different y-axis on the sample plot
    ax2=ax.twinx()
    # make a plot with different y-axis using second axis object
    ax2.plot(x1_data, y2_data,color="blue",marker="o")
    ax2.set_ylabel(y2_label,color="blue",fontsize=14)
    # ax.set_xticks(mining.index)
    ax.set_xticklabels(labels = xticklabel, rotation = 90)
    ax.grid(which='major')
    ax.set_xlim(0,xlim)
    plt.show()
    # save the plot as a file
    fig.savefig(f'../Output/industry/{fname}.png',
                format='png',
                dpi=100,
                bbox_inches='tight')

# linear regression

def myreg(xdata,ydata,xpos,ypos, title, xlabel,ylabel,fname):
    '''
    myreg is create linear regression
    '''
    slope, intercept, rval, pval, std_err = st.linregress(xdata,ydata )
    fit = slope * xdata + intercept
    # line equation to be displayed
    line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))

    # Create linear regression
    plt.plot(xdata,fit,"--", color = 'red')
    plt.annotate(line_eq,(xpos,ypos),fontsize=15,color="red")
    plt.scatter(xdata, ydata)
    # plt.annotate(line_eq,(xpos,ypos),fontsize=15,color="red")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # plt.xlim(0,xlim)
    plt.grid(which = 'major', axis = 'both')
    plt.savefig(f'../Output/industry/{fname}')
    plt.show()
    print(f"The r-squared is: {rval**2}")
    print(f"The r-squared is: {rval}")
    print(f"The p-value is: {pval}")
    if pval < 0.05:
        print(f"p-val < 0.05, hence null hypothesis is rejected")
    else:
        print(f"p-val > 0.05, there is not enough evidance to reject null hypothesis")

def mychoro(m, dataframe,col_id,col_val, legendname):
    m = folium.Map(location=[-28.314629039038312, 139.577597363054], zoom_start=4)
    url = (
    "https://raw.githubusercontent.com/rowanhogan/australian-states/master/states.min.geojson"
    )
    geodata = f"{url}"

    folium.Choropleth(
        geo_data=geodata,
        name="choropleth",
        data=dataframe,
        columns=[col_id, col_val],
        key_on="feature.id",
        fill_color="PuBuGn",
        fill_opacity=0.7,
        line_opacity=.1,
        legend_name=legendname,
        ).add_to(m)

    folium.LayerControl().add_to(m)
    m
