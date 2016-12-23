# Stock_Analysis_And_Recommendation
Final Project Submission for 201612-67    
## Team Members   
Yimeng Zhou (yz2993)    
Qianwen Zheng (qz2271)     
Ye Wang (yw2883)    

## Dataset    
we get our dataset from Quandl, Wiki EOD Stock Prices   
https://www.quandl.com/data/WIKI-Wiki-EOD-Stock-Prices/documentation/documentation?modal=null    

## Tools
Python, Spark, MATLAB

## Descripton

We achieved the function of predicting short-term and long-term trends of each stock, which is realized by analyzing the trend of moving average.    

Besides, we completed stock recommendation by doing K-means Clustering of stocks.    

We also completed a linear regression model for DJIA for stock market prediction.

 
#### kmeansData.py     
The features we extract from original dataset for kmeans clustering         
#### kmeans_clustering.py       
Kmeans clustering      
#### movingAvg.py        
Calculate the 10-days, 20-days and 50-days moving average for a certain stock   
#### linear_regression_with_elastic_net.py       
Linear regression model for DJIA    
#### Kmeans.txt   
Extracted features for K-means clustering    
#### A.csv    
There are total three csv files which are all samples for calcualting moving average    
#### DJI.txt    
Input factors for linear regression
