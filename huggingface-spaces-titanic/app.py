import gradio as gr
import numpy as np
from PIL import Image
import requests

import hopsworks
import joblib

project = hopsworks.login()
fs = project.get_feature_store()


mr = project.get_model_registry()
model = mr.get_model("titanic_modal", version=1)
model_dir = model.download()
model = joblib.load(model_dir + "/titanic_model.pkl")

dataset_api = project.get_dataset_api()

dataset_api.download("Resources/images/deadImage.png")
dataset_api.download("Resources/images/survivedImage.png")

def titanic(PassengerId, Pclass, Numeric_sex, Age, Fare):
    input_list = []
    input_list.append(PassengerId)
    input_list.append(Pclass)
    input_list.append(Numeric_sex)
    input_list.append(Age)
    input_list.append(Fare)

    # 'res' is a list of predictions returned as the label.
    res = model.predict(np.asarray(input_list).reshape(1, -1)) 
    
    l = int(res)   
    if(l == 0):
            img = Image.open("deadImage.png")            
    else:
            img = Image.open("survivedImage.png")
    
    return img
        
demo = gr.Interface(
    fn=titanic,
    title="Titanic Predictive Analytics",
    description="Experiment to predict which passenger will survived.",
    allow_flagging="never",
    inputs=[
        gr.inputs.Number(default=100, label="PassengerId"),
        gr.inputs.Number(default=2, label="Pclass"),
        gr.inputs.Number(default=1, label="Numeric_sex"),
        gr.inputs.Number(default=20, label="Age"),
        gr.inputs.Number(default=30, label="Fare"),
        ],
    outputs=gr.Image(type="pil"))

demo.launch()
