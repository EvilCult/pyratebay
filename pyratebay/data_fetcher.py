import json
import time
from urllib import parse

import requests

from pyratebay.config import (
    API_URL,
    FAKE_HEADERS,
    HOT_URL,
    INFO_URL,
    MEDIA_TYP,
    SEARCH_URL,
)
from pyratebay.models import Media


def media_search(query: str, media_type: str) -> list:
    media_list: list[Media] = []
    search_key: str = parse.quote(query)
    typ: str | None = MEDIA_TYP.get(media_type) if media_type in MEDIA_TYP else "0"
    url: str = f"{API_URL}{SEARCH_URL.format(query=search_key, typ=typ)}"

    try:
        response: requests.Response = requests.get(url, headers=FAKE_HEADERS)
        data: list = json.loads(response.text)
    except Exception:  # noqa: BLE001
        time.sleep(3)
        response: requests.Response = requests.get(url, headers=FAKE_HEADERS)
        data: list = json.loads(response.text)

    for x in data:
        media = Media(
            mid=x["id"],
            title=x["name"],
            size=int(x["size"]) if "size" in x else None,
            seeders=int(x["seeders"]) if "seeders" in x else None,
            leechers=int(x["leechers"]) if "leechers" in x else None,
            uploader=x.get("username", None),
            time=int(x["added"]) if "added" in x else None,
            info_hash=x.get("info_hash", None),
        )
        media_list.append(media)

    return media_list


def media_info(mid: str) -> Media:
    url: str = API_URL + INFO_URL.format(tid=mid)

    try:
        response: requests.Response = requests.get(url, headers=FAKE_HEADERS)
        data: dict = json.loads(response.text)
    except Exception:  # noqa: BLE001
        time.sleep(3)
        response: requests.Response = requests.get(url, headers=FAKE_HEADERS)
        data: dict = json.loads(response.text)

    media = Media(
        mid=data["id"],
        title=data["name"],
        desc=data["descr"] if "size" in data else None,
        size=data.get("size", None),
        seeders=data.get("seeders", None),
        leechers=data.get("leechers", None),
        uploader=data.get("username", None),
        time=data.get("added", None),
        info_hash=data.get("info_hash", None),
    )
    return media


def hot_media(media_type: str, limit: bool) -> list:
    media_list: list[Media] = []

    recent = "_48h" if limit else ""
    typ: str | None = MEDIA_TYP.get(media_type) if media_type in MEDIA_TYP else "0"
    url: str = API_URL + HOT_URL.format(typ=typ, recent=recent)

    try:
        response: requests.Response = requests.get(url, headers=FAKE_HEADERS)
        data: list = json.loads(response.text)
    except Exception:  # noqa: BLE001
        time.sleep(3)
        response: requests.Response = requests.get(url, headers=FAKE_HEADERS)
        data: list = json.loads(response.text)

    for x in data:
        media = Media(
            mid=x["id"],
            title=x["name"],
            size=x.get("size", None),
            seeders=x.get("seeders", None),
            leechers=x.get("leechers", None),
            uploader=x.get("username", None),
            time=x.get("added", None),
            info_hash=x.get("info_hash", None),
        )
        media_list.append(media)

    return media_list
