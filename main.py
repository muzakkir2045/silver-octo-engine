

from utils import generate_short_id
from fastapi import FastAPI, status , responses
from pydantic import BaseModel
import webbrowser

class URL_Contents(BaseModel):
    original_url : str 

class UrlResponse(BaseModel):
    original_url : str
    new_url : str



app = FastAPI()

url_mapping = {}


def generate_short_url(long_url):
    short_id = generate_short_id(long_url)
    while short_id in url_mapping.keys():
        short_id = generate_short_id(long_url)
    
    short_url = f"http://127.0.0.1:8000/{short_id}"
    url_mapping[short_id] = long_url
    return short_url

@app.get("/{shortcode}")
def home(shortcode):

    if shortcode not in url_mapping:
        response = responses.RedirectResponse("/home")
        return response

    return responses.RedirectResponse("http://www.google.com")

@app.get("/home")
def home():
    return {"Message" : "Ok"}


@app.post("/get_new_url")
def get_new_url(URL_Contents : URL_Contents):

    
    new_url = generate_short_url(URL_Contents.original_url)

    return {"Message" : status.HTTP_201_CREATED , 
            "Data" : new_url}


