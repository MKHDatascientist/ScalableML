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

titanic_df = pd.read_csv('Dataset/cleanedTitanic.csv')
###################################################################################################
#To create a feature group you need to give it a name and specify a primary key
titanic_fg = fs.get_or_create_feature_group(
    name="titanic_modal",
    version=55,
    primary_key=['PassengerId','Pclass','Numeric_sex','Age',"Fare"]#['PassengerId']
    ,description="TitanicDataset")

titanic_fg.insert(titanic_df, write_options={"wait_for_job" : False})

###################################################################################################
