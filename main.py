

from utils import generate_short_id
from fastapi import FastAPI, status 
from fastapi.responses import RedirectResponse
from schemas import UrlCreate, UrlResponse, UrlMapper
    

app = FastAPI()
URL = "http://127.0.0.1:8000/"
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
def get_shortcode(shortcode : str):

    if shortcode not in url_mapping:
        return RedirectResponse("/")

    return RedirectResponse(url=url_mapping.get(shortcode), status_code = status.HTTP_301_MOVED_PERMANENTLY)

@app.get("/api/urls")
def get_all_urls():
    return url_data

@app.post("/api/create_url", response_model = UrlResponse | UrlMapper)
def get_new_url(UrlCreate : UrlCreate):

    original_url = UrlCreate.original_url
    if not original_url.startswith("https://"):
        original_url = f"https://{original_url}"
    if original_url in url_mapping.values():
        key = list(url_mapping.keys())[list(url_mapping.values()).index(original_url)]
        return {
            "original_url" : original_url,
            "new_url" : URL+key
        }

    if url_data:
        id = int(max(url_data.keys()) + 1)
    else:
        id : int = 1

    data = {
        "id" : id,
        "original_url" : original_url,
        "new_url" : generate_short_url(original_url),
        "creation_date" : "20-10-2026",
        "expiration_date" : "20-10-2027"
    }

    url_data[id] = data
    return data


@app.delete("/api/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_url(id : int):

    if id not in url_data:
        return {
            "Message" : "Invalid Id"
        }

    if id in url_data:
        shortcode = url_data[id]["new_url"].split("/")[-1]
        url_mapping.pop(shortcode)
        url_data.pop(id)

    return {
        "Message" : "Deleted"
    }