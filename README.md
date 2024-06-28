## Deployment: [Hugging Face](https://huggingface.co/spaces/vickyeldora/Predict_Default_Payment_Credit_Card)

## Logistic Regression, SVM, and KNN Concepts:

- Obtain data using BigQuery.
- Understand the concept of Classification with Logistic Regression, SVM, and KNN.
- Prepare data for use in Logistic Regression, SVM, and KNN models.
- Implement Logistic Regression, SVM, and KNN to make predictions.

---

## Dataset

```{attention}
Pay attention to the dataset usage instructions!
```

1. Open [Google Cloud Platform](https://console.cloud.google.com/), go to BigQuery, and open the `bigquery-public-data` tab or use [this link](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=ml_datasets&t=credit_card_default&page=table) to directly access the dataset.

2. Use the `ml_datasets` dataset from the database named `credit_card_default`.

3. Create a query with the following criteria:
   - Select **ONLY** the columns `limit_balance, sex, education_level, marital_status, age, pay_0, pay_2, pay_3, pay_4, pay_5, pay_6, bill_amt_1, bill_amt_2, bill_amt_3, bill_amt_4, bill_amt_5, bill_amt_6, pay_amt_1, pay_amt_2, pay_amt_3, pay_amt_4, pay_amt_5, pay_amt_6, default_payment_next_month`.
   
   - Convert the data types of certain columns from `STRING` to numeric types as shown below: 
     | Column | Original Data Type | New Data Type |
     | --- | --- | --- |
     | `sex` | STRING | INT |
     | `education_level` | STRING | INT |
     | `marital_status` | STRING | INT |
     | `pay_5` | STRING | FLOAT |
     | `pay_6` | STRING | FLOAT |
     | `default_payment_next_month` | STRING | INT |
   
   - The data type conversions should be performed within the same query when fetching data from Google BigQuery.
   
   - The columns above will be used as the initial dataset. Feature selection should be performed in the notebook after creating the dataset.
   
   - Limit the data to 5 x 2002 = 10010 rows.

4. Save the dataset as a CSV file named `Data-Set.csv`.

5. Copy the query created on Google Cloud Platform and include it at the top of the notebook!

---

## Problem Statement:

A credit card company has information related to credit card usage, such as demographic information about cardholders (sex, education level, marital status, age), repayment status, bill statements, and previous payments.  
The company wants to predict the likelihood of credit card users defaulting (not paying bills on time) based on the available data.

## Objective:

This project aims to build a credit card `default prediction` model using the provided dataset. The goal is to create a `classification model` using one of the three options: logistic regression, SVM, or KNN, and then evaluate the model using the F1 score to identify the best model for prediction.

---

## The notebook format:

1. The machine learning framework used should be Scikit-Learn.

2. Utilize visualization libraries such as matplotlib, seaborn, or others.

3. The notebook content should follow the outline below:
   1. Introduction
      > Contains the objective.

   2. SQL Query
      > Contains the query created to fetch data from Google Cloud Platform.

   3. Import Libraries
      > Contains all the libraries used in the project.

   4. Data Loading
      > This section includes the process of preparing data before further exploration, such as renaming columns, checking dataset size, etc.

   5. Exploratory Data Analysis (EDA)
      > This section contains data exploration on the dataset using queries, grouping, simple visualizations, and other techniques.

   6. Feature Engineering
      > This section contains the process of preparing data for model training, such as splitting data into train-test sets, data transformation (normalization, encoding, etc.), and other necessary processes.

   7. Model Definition
      > This section contains cells to define the model. Explain the reasons for using a particular algorithm/model, the hyperparameters used, the chosen metrics, and other related details.

   8. Model Training
      > This section contains only the code to train the model and the output generated. Perform several training processes with different hyperparameters to observe the results. Analyze and narrate these results in the Model Evaluation section.

   9. Model Evaluation
      > This section evaluates the model, showing its performance based on the chosen metrics. This is demonstrated through visualizations of performance trends and/or model error rates.

   10. Model Saving
       > This section contains the process of saving the model and other related files from the model-building process.
   
   11. Model Inference
       > The trained model is tested on data that is not part of the train-set or test-set. This data is in its original format, not scaled data. Use the best model based on the Model Evaluation results.

   12. Conclusion
       > Conclusions reflecting the results obtained in relation to the objective stated in the introduction.

---