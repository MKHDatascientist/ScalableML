import os
from tkinter import E
import modal
#import great_expectations as ge
import hopsworks
import pandas as pd

import hops.featurestore as featureS#???
#Connecting to Hopswork feature store:

project = hopsworks.login()
fs = project.get_feature_store()

#titanic_df = pd.read_csv('https://raw.githubusercontent.com/ID2223KTH/id2223kth.github.io/master/assignments/lab1/titanic.csv')#

#titanic_df = pd.read_csv("https://raw.githubusercontent.com/ID2223KTH/id2223kth.github.io/master/assignments/lab1/titanic.csv")
#titanic_df = pd.read_csv("https://repo.hops.works/master/hopsworks-tutorials/data/iris.csv")
titanic_df = pd.read_csv('Dataset/cleanedTitanic.csv')
###################################################################################################
#To create a feature group you need to give it a name and specify a primary key
titan_fg = fs.get_or_create_feature_group(
    name="titan_modal",
    version=53,
    primary_key=['PassengerId'],# 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp','Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
    description="TitanicDataset")

titan_fg.insert(titanic_df, write_options={"wait_for_job" : False})

###################################################################################################
#expectation_suite = ge.core.ExpectationSuite(expectation_suite_name="iris_dimensions")    
#value_between(expectation_suite, "sepal_length", 4.5, 8.0)
#value_between(expectation_suite, "sepal_width", 2.1, 4.5)
#value_between(expectation_suite, "petal_length", 1.2, 7)
#value_between(expectation_suite, "petal_width", 0.2, 2.5)
#iris_fg.save_expectation_suite(expectation_suite=expectation_suite, validation_ingestion_policy="STRICT")    
    
