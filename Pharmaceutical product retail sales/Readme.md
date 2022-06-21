1. Project Architecture:
  - Loading the data
  - Grouping the data by Client
  - Generate Time-series for working days 
  - scrape google trends for "toux" , our pruct is medecine for cough so we'd like to search for times of teh year where we can expect spikes in sales
  - using Traces https://traces.readthedocs.io/en/latest/ to model irreguler Time-series
2. Project Idea and motivation: Our data wrangling professor shared a dataset for phamaceutical products and the work was to make dataframes and a datawarehouse given this JSON of bills
I tried to take it a step further and make sale forecasts for the next month for every client
3. Project Technologies:  Traces ,statsModels package , pandas , Google Trens
4. Project Improvements and To-Do list:
        - implement the irreguler TS forcast
