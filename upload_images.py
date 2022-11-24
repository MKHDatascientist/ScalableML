import os
import modal
#import sklearn
LOCAL=True

#mire model train shode ro migire va run mikone as hopsworks
if LOCAL == False:
   stub = modal.Stub()
   hopsworks_image = modal.Image.debian_slim().pip_install(["hopsworks==3.0.4","joblib","seaborn","sklearn","dataframe-image"])
   @stub.function(image=hopsworks_image, schedule=modal.Period(days=1), secret=modal.Secret.from_name("secret_titanic2"))
   def f():
       g()

def g():
    import pandas as pd
    import hopsworks
    import joblib
    import datetime
    from PIL import Image
    from datetime import datetime
    import dataframe_image as dfi
    from sklearn.metrics import confusion_matrix
    from matplotlib import pyplot
    import seaborn as sns
    import requests
    import io

    project = hopsworks.login()
    fs = project.get_feature_store()
    dataset_api = project.get_dataset_api()

    img = Image.open(r"C:/Users/User/Documents/Images_SML/0.png")
    img.save("./deadImage.png")
    
    dataset_api = project.get_dataset_api()    
    dataset_api.upload("./deadImage.png", "Resources/images", overwrite=True)
   
    img = Image.open(r"C:/Users/User/Documents/Images_SML/1.png")    
    
    img.save("./survivedImage.png")
    dataset_api.upload("./survivedImage.png", "Resources/images", overwrite=True)
    
    
if __name__ == "__main__":
    if LOCAL == True :
        g()
    else:
        with stub.run():
            f()
