import requests
import json
from urllib import parse
from pyratebay.config import FAKE_HEADERS, API_URL, SEARCH_URL, INFO_URL, MEDIA_TYP
from dataclasses import dataclass

@dataclass
class Media:
    mid      : str
    title    : str
    desc     : str | None = None
    size     : int | None = None
    seeders  : int | None = None
    leechers : int | None = None
    uploader : str | None = None
    time     : int | None = None
    info_hash: str | None = None

def media_search(query: str, media_type: str) -> list:
    media_list: list[Media] = []
    search_key: str = parse.quote(query)
    typ: str = MEDIA_TYP.get(media_type) if media_type in MEDIA_TYP else "0"
    url: str = API_URL + SEARCH_URL.format(query=search_key, typ=typ)

    response: requests.Response = requests.get(url, headers=FAKE_HEADERS)
    data: list = json.loads(response.text)

    for x in data:
        media = Media(
            mid       = x["id"],
            title     = x["name"],
            size      = x["size"] if "size" in x else None,
            seeders   = x["seeders"] if "seeders" in x else None,
            leechers  = x["leechers"] if "leechers" in x else None,
            uploader  = x["username"] if "username" in x else None,
            time      = x["added"] if "added" in x else None,
            info_hash = x["info_hash"] if "info_hash" in x else None,
        )
        media_list.append(media)

    return media_list

def media_info(mid: str) -> Media:
    pass