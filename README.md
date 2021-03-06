# Project Introduction

Hello, 

Welcome to our data visualisation project. 

Our project name will simply be referred to as: COVID-19 - Data Assessment: group5project

Reasoning of topic choice: 

Almost everyone has been touched by Covid-19 in one way or another. 
Whether that is through the form of: restrictions, employment life and those personally dealing with the devistating disease, we wanted to create a snapshot into the true impacts of the virus.    


Acknowledgements   
Scope of data: the sheer size of the macro economy meant we needed to decide on specific areas of measurement (e.g.) categories. 

Limitations of Data: this will not cover all industry sectors of business performance.


Categories to be used in this project

```
General population health (i.e. infections)
```

```
Labour outcomes (unemployment rates) 
```

```
Human population movements (travel)
```

```
Mining, Oil and Gas (sector performances)
```


Hypothesis

What we hope to show with our data is that Covid-19 had a significant negative effect on the afforementioned categories. 



# Project Structure
IMPORTANT**: STRUCTURE HIGHLIGHTS DATA USED WE CHOSE TO USE IN THE PRESENTATION. EVERYTHING ELSE IS SUPPLEMENTARY FOR NARRATIVES WE COULD NOT INCLUDE
```

|__Output # saved images and CSVs from cleaning and regression
    |__covid_output
    |__employment_output
    |__industry
|__Resources
    |__covid_raw
    C19_AU_2018_2021.csv
    M_C19_AU_2018_2021.csv 
|__employment_data
    employment_clean_main # cleaning file for unemployment in presentation
    employment_data_plot_main # unemployment regression file in presentation
    |__Ray Data # raw data for unemployment
|__cleaning_files
    cov_clean_AMB_v3.ipynb #cleaning file
    industry_clean_v3.ipynb
    myfunction.py
    plot_data_v3.ipynb
CoVID-19pp.pptx
```
# Usage

# Questions
1. What is the impact of Covid-19 on Australia? 
2. What is the specific effect of Covid-19 on the macro-economy of Australia? 

# Datasets
|No.|Source|Link|
|-|-|-|
|1|COVID-19 Data Repository by CSSE at John Hopkins University|https://github.com/CSSEGISandData/COVID-19|
|2|Australian Bureau of Statistics Datasets|https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia/latest-release|
|3|Australia Digital Boundary Geojson|https://github.com/rowanhogan/australian-states/blob/master/states.min.geojson|
|4|Australian Bureau of Statistics Datasets|https://www.abs.gov.au/statistics/industry/mining/mineral-and-petroleum-exploration-australia/dec-2020|
|5|Australian Bureau of Statistics Datasets|https://www.abs.gov.au/statistics/industry/tourism-and-transport/overseas-arrivals-and-departures-australia/feb-2021|



# Analysis
 - There is a positive correlation between unemployment and CoVID19. Which is what we expected.
- ![](Output/employment_output/confirmed_vs_unemployment_aus_line.png) 
![](Output/employment_output/confirmed_vs_unemployment_aus_regression.png)
 - There is negative correlation between travel/tourism and CoVID19 as expected.


 - No evidence of correlation between mining/petroleum sector and CoVID19. Which not we expected.

 

# Contributors
[@JackPan](https://www.github.com/jackxinpan)

[@RayCamo](https://github.com/rfcamo)

[@AhmadMakintha](https://github.com/makintha)

[@SimonaSuko](https://github.com/simonasuko)
