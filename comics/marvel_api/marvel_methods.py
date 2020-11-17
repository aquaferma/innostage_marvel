import requests
from django.conf import settings
from .api_wrapper import make_request
 

def get_comics(title, page_number):
    data = {
        "title": title,
        "limit": settings.COMICS_PAGE_COUNT,
        "offset": int(page_number) * settings.COMICS_PAGE_COUNT,
        "format": "comic"
    }
    uri = "https://gateway.marvel.com/v1/public/comics"

    return make_request(uri, data)


def get_comic(comic_id):
    uri = f"https://gateway.marvel.com/v1/public/comics/{comic_id}"
    return make_request(uri, {})
    