import os
import modal
import pandas as pd

LOCAL=True

if LOCAL == False:
   stub = modal.Stub()
   image = modal.Image.debian_slim().pip_install(["hopsworks==3.0.4"]) 

   @stub.function(image=image, schedule=modal.Period(days=1), secret=modal.Secret.from_name("secret_titanic2"))#("jim-hopsworks-ai"))
   def f():
       g()


def generate_flower(name):
    import pandas as pd
    import random

    df = pd.DataFrame({ "PassengerId": 1,  #dONT FORGET
                       "Pclass": [random.randint(1,3)],
                       
                       "Numeric_sex":[random.randint(0,1)],
                       "Age": [random.uniform(100,1)],
                       "Fare": [random.uniform(250,7)]
                      })
    df['Survived'] = name
    return df


def get_random_iris_flower():
    """
    Returns a DataFrame containing one random iris flower
    """
    import pandas as pd
    import random
    #PassengerId	Pclass	Survived	Numeric_sex	  Age	Fare
   
    nots = generate_flower(0)#not survived
    s =  generate_flower(1)#survived

    # randomly pick one of these 3 and write it to the featurestore
    #pick_random = random.uniform(0,3)
    pick_random=1
    if pick_random == 1:
        iris_df = s
        print("Survived added")
    else:
        iris_df = nots
        print("Not survived added")
    

    return iris_df


def g():
    import hopsworks
    import pandas as pd

    project = hopsworks.login()
    fs = project.get_feature_store()

    titanic_df = get_random_iris_flower()

    iris_fg = fs.get_feature_group(name="titan_modal",version=53)
    iris_fg.insert(titanic_df, write_options={"wait_for_job" : False})

if __name__ == "__main__":
    if LOCAL == True :
        g()
    else:
        with stub.run():
            f()