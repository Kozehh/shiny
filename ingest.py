import weaviate
import json
from os import environ
import pandas as pd
import requests
from dotenv import load_dotenv
from collections import OrderedDict, defaultdict

load_dotenv()

df_exercise = pd.read_csv('./data/megaGymDataset.csv')

df_exercise = df_exercise[['Title', 'Desc', 'Type', 'BodyPart', 'Equipment', 'Level']]
df_exercise.fillna('', inplace=True)
df_exercise.drop_duplicates(inplace=True)
df_exercise.reset_index(drop=True, inplace=True)

data = df_exercise.to_dict(orient="records")


client = weaviate.Client(
    url = "https://shiny-test-uolmtiuu.weaviate.network",
    auth_client_secret=weaviate.AuthApiKey(api_key=environ["WEAVIATE_API_KEY"]),  # Replace w/ your Weaviate instance API key
    additional_headers = {
        "X-OpenAI-Api-Key": environ["OPENAI_API_KEY"]  # Replace with your inference API key
    }
)


if not client.schema.exists("Exercise"):

    class_obj = {
    "class": "Exercise",
    "vectorizer": "text2vec-openai",  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
    "moduleConfig": {
        "text2vec-openai": {},
        "generative-openai": {}  # Ensure the `generative-openai` module is used for generative queries
        }
    }

    client.schema.create_class(class_obj)


    client.batch.configure(batch_size=100)  # Configure batch
    with client.batch as batch:  # Initialize a batch process
        for i, d in enumerate(data):  # Batch import data
            print(f"importing exercise: {i+1}")
            print(d)
            properties = d
            batch.add_data_object(
                data_object=properties,
                class_name="Exercise"
            )