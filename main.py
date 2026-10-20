


from fastapi import FastAPI, status
from pydantic import BaseModel
import webbrowser

class URL_Contents(BaseModel):
    original_url : str 
    new_url : str


app = FastAPI()



URLS = {
    "abcdefg" : "https://www.google.com",
    "stack_overflow_web" : "https://stackoverflow.com/questions/4302027/how-can-i-open-a-url"
}

@app.get("/")
def home():
    return {"Message" : "Ok"}

@app.get("/{shortcode}")
def home(shortcode):
    return webbrowser.open(URLS[shortcode])

@app.post("/get_new_url")
def get_new_url(URL_Contents : URL_Contents):
    URLS["abcdefg"] = URL_Contents.original
    print(URL_Contents.original_url)

    return {"Message" : status.HTTP_201_CREATED , 
            "Data" : URL_Contents}


