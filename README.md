# Predicting-the-future-of-Rice-Wheat-or-Corn-Prices
Predicting rice, wheat and corn prices based on the Kaggle dataset "Cerial Prices Changes Within Last 30 Years"

Title: What is the title of your project? Predicting the future of Rice, Wheat or Corn Prices

Project’s function: This is an overall description of your project: What is objective of the project? What is the problem you are trying to solve? I’d like to invest in agricultural products next year. I need a data analysis visualization that will consume historical data and make a prediction for agricultural products prices for or the next few years.

Dataset: Briefly describe your dataset. I’ll be using this dataset from the kraggle website: https://www.kaggle.com/datasets/timmofeyy/-cerial-
prices-changes-within-last-30-years
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

Pipeline / Architecture: Which pipeline did you use? Which tools? For this project I will be using pipeline 1.I’ll be using a modified version of the ingest_data method in the batch_ingest python program that we used in Lab 1 and 2 to pull data from the kaggle api and store it as a pkl file in a S3 Data Lake. Then I will
be using a modified version of the transform-data method from the transform python program to pull the data from the data lake, transform the one big dataset into three individual product datasets and saving the 3 pkl files in a S3 Data Warehouse. From there I will be using methods we will learn in module 6 to use TensorFlow model selection and model testing to answer the questions made in the “What questions will your project address?” section.

In the TensorFlow app that I will write I expect the following code flow;
1. Collect a dataset
2. Build your model
3. Train the network
4. Evaluate the data
5. Make predictions based on the data
6. Create graphs to visualize the results

Data Quality Assessment: Describe the quality status of the data set and the way you assessed it. I would guess the data quality is high. It's been download 1354 times in the last month. I assessed it using the methods we learned in lab 2 in the transform.py app.

Data Transformation Models used: Briefly describe the transformations and models used. Just as we did in Lab 2, I checked for and removed rows with NaN, duplicate values and outliers.

and final results that you were able to achieve. If there are any special instructions needed to execute your code (e.g., signing up to a specific API to access the dataset that is needed) those need to be listed as well. I used a dataset from Kaggle.com. Registration is required. The api key and username need to be placed in a file located at user/.kaggle/kaggle.json.

Infographic: A simple infographic describing the architecture of your data pipeline including datasets, storage, and tools used along with another final infographic describing the results of the engineering task accomplished. Examples can be provided if needed.

Code: A link to GitHub Repository https://github.com/jrnoll/Predicting-the-future-of-Rice-Wheat-or-Corn-Prices

Thorough Investigation: This critically assesses the viability of your idea: Based on the results of this project (your pilot project, your prototype, etc), from a technical leadership point of view, what are your conclusions or recommendations for continuing this project in terms of scaling it up? How would you assess the innovativeness of your project? Any technical or platform concerns, difficulties, or limitations of the pipeline for the project? Based on your experience and results, what next step would you recommend to take this project to the next level/phase?
