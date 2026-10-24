

from utils import generate_short_id
from fastapi import FastAPI, status 
from fastapi.responses import RedirectResponse
from schemas import UrlCreate, UrlResponse
    

app = FastAPI()

url_mapping = {}

url_data = {}

def generate_short_url(long_url):
    short_id = generate_short_id(long_url)
    while short_id in url_mapping.keys():
        short_id = generate_short_id(long_url)
    short_url = f"http://127.0.0.1:8000/{short_id}"
    url_mapping[short_id] = long_url
    return short_url

@app.get("/")
def home():
    return {"Message" : "Ok"}


@app.get("/{shortcode}")
def get_shortcode(shortcode):

    if shortcode not in url_mapping:
        return RedirectResponse("/")

    return RedirectResponse(url=url_mapping[shortcode], status_code = status.HTTP_301_MOVED_PERMANENTLY)



@app.post("/get_new_url", response_model=UrlResponse)
def get_new_url(UrlCreate : UrlCreate):

    original_url = UrlCreate.original_url

    data = {
        "original_url" : UrlCreate.original_url,
        "new_url" : generate_short_url(UrlCreate.original_url),
        "creation_date" : "20-10-2026",
        "expiration_date" : "20-10-2027",
        "total_click_count" : 0
    }

    url_mapping[data["new_url"]] = data["original_url"]

    
    return data


