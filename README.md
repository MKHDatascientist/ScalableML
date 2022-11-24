# ScalableML
Scalable Machine Learning Project - Lab1

Maryam Kheirkhahzadeh, markhe@kth.se
December 2022

Subject:
Prediction survived or not survived for the titanic data set. In this project we create a feature group on hopsworks and then using a training application we will have a model on hopsworks. We use huggingface.co to connect to hopsworks.ai and predict an arbitrary record.

Data set:
I have used the data set from this link: https://raw.githubusercontent.com/ID2223KTH/id2223kth.github.io/master/assignments/lab1/titanic.csv

Data cleaning:
I have done this part using Google colab. Then I have used the cleaned dataset in titanic-feature-pipeline.py. I have cleaned the data by replacing male and female with 0 and 1 respectively, replacing nan values in pclass column with mean of the column and some other tasks.

Uploading images:
I have uploaded two pictures for dead and survived situations on hopsworks instead of using a url. The python file upload_images.py has uploaded both files using get_dataset_api function.

Implementation
We have passed these steps:
1- Creating  accounts on Modal.com, hopsworks.ai and huggingface.co.
2- Defining api-key in hopsworks
3- Defining a secret key using this api-key in modals
4- Creating feature group in hopsworks 
5- Creating view and model and hopsworks
6- Calling titanic-feature-daily.py and titanic-batch.py consequently.
7- Defining two new name spaces in huggingface. One space for defining a user-interface which takes some parameters and predicts based on the titanic model. Another space is for demonstrating some features like confusion matrix.


