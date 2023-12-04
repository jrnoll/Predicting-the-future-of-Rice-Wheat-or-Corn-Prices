# Predicting-the-future-of-Rice-Wheat-or-Corn-Prices
Predicting rice, wheat and corn prices based on the Kaggle dataset "Cerial Prices Changes Within Last 30 Years"

**Title:** What is the title of your project? Predicting the future of Rice, Wheat or Corn Prices

**Project’s function:** This is an overall description of your project: What is objective of the project? What is the problem you are trying to solve? I’d like to invest in agricultural products next year. I need a data analysis visualization that will consume historical data and make a prediction for agricultural products prices for or the next few years.

**Dataset: Briefly describe your dataset.** I’ll be using this dataset from the kraggle website: https://www.kaggle.com/datasets/timmofeyy/-cerial-prices-changes-within-last-30-years
This dataset has the following fields:
Year: A year starting from 1992 ending with 2022
Month: A month of the year
Price_wheat_ton: Wheat price per ton in the definite month and year
Price_wheat_ton_infl: Modern price per ton of wheat
Price_rice_ton: Price price per ton in the definite month and year
Price_rice_ton_infl: Modern rice per ton of wheat
Price_corn_ton: Corn price per ton in the definite month and year
Price_corn_ton_inf: Modern price per ton of corn
Inflation_rate: İnflation rate constantly changes according to prices.

**Pipeline / Architecture: Which pipeline did you use? Which tools?** For this project I will be using pipeline 1.

Tools & Technologies

    Cloud - Amazon Web Services
    Containerization - Docker 
    Orchestration - Airflow
    Data Lake - Amazon Web Services S3
    Data Warehouse - Amazon Web Services S3
    Data Visualization - matplotlib.pyplot
    Language - Python

**Data Quality Assessment: Describe the quality status of the data set and the way you assessed it.** The data quality is high. I assessed it using the methods we learned in lab 2 in the transform.py app.

**Data Transformation Models used: Briefly describe the transformations and models used.** Just as we did in Lab 2, I checked for and removed rows with NaN, duplicate values and outliers.

**and final results that you were able to achieve. If there are any special instructions needed to execute your code (e.g., signing up to a specific API to access the dataset that is needed) those need to be listed as well.** I used a dataset from Kaggle.com. Registration is required. The api key and username need to be placed in a file located at user/.kaggle/kaggle.json. Some of these apps can be run locally on downloaded data during developement, but they are designed to run on an Airflow docker container runing on an EC2 instance. 

**Infographic: A simple infographic describing the architecture of your data pipeline including datasets, storage, and tools used along with another final infographic describing the results of the engineering task accomplished. Examples can be provided if needed.**

![plot](https://github.com/jrnoll/Predicting-the-future-of-Rice-Wheat-or-Corn-Prices/blob/main/pipeline%201.png)

**Graphs of the results** The three Annual Price graphs were created using matplotlib.pyplot, years on the bottom, prices on the side. The Price Variations graph was created with seaborn.
![plot](https://github.com/jrnoll/Predicting-the-future-of-Rice-Wheat-or-Corn-Prices/blob/main/Corn%20Annual%20Price%20graph.png)
![plot](https://github.com/jrnoll/Predicting-the-future-of-Rice-Wheat-or-Corn-Prices/blob/main/Rice%20Annual%20Price%20Graph.png)
![plot](https://github.com/jrnoll/Predicting-the-future-of-Rice-Wheat-or-Corn-Prices/blob/main/Wheat%20Annual%20Price%20Graph.png)
![plot](https://github.com/jrnoll/Predicting-the-future-of-Rice-Wheat-or-Corn-Prices/blob/main/Price%20Variation%20in%2020225.png)

**Code: A link to GitHub Repository** https://github.com/jrnoll/Predicting-the-future-of-Rice-Wheat-or-Corn-Prices

**Thorough Investigation: This critically assesses the viability of your idea: Based on the results of this project (your pilot project, your prototype, etc), from a technical leadership point of view, what are your conclusions or recommendations for continuing this project in terms of scaling it up? How would you assess the innovativeness of your project? Any technical or platform concerns, difficulties, or limitations of the pipeline for the project? Based on your experience and results, what next step would you recommend to take this project to the next level/phase?**
This is my first experance with Machine learning and I think that I vastly over estimated the ability of machine learning to answer the questions I proposed in my project proposal. 

As far as next steps go, from what I have been able to learn about machine learning on my own in the last month I believe the keras.layers import LSTM, Dense, Dropout, keras.models Sequential and keras.layers Dense are better suited for and generally used in stock market prediction apps, and not very well suited for the cerial price predicion app I created for my final project.  As a next step, in order to improve the app performancem  I would recommed rewriting the build_train_modle app to not add layers to the model. 
