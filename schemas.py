

from pydantic import BaseModel, ConfigDict

"""
{    
    "shortcode" : {
        "original_url" : str,
        "custom_alias" : "optional",
        "creation_date" : str,
        "expiration_date" : str,
        "total_click_count" : int
    }
}
"""

class UrlBase(BaseModel):
    original_url : str
    custom_alias : str = None
    
    
    
class UrlCreate(UrlBase):
    pass

class UrlResponse(UrlBase):
    model_config = ConfigDict(from_attributes = True)

    id : int
    new_url : str
    creation_date : str
    expiration_date : str
    unique_visitors : int = 0
    total_visitors : int = 0

class UrlMapper(BaseModel):

    original_url : str
    new_url : str
