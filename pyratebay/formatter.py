import datetime
import textwrap
from urllib import parse

from pyratebay.config import HASH_URL, TR_LIST
from pyratebay.models import Media


def format_media_list(media_list: list[Media]) -> str:
    def list_info(media: Media) -> str:
        return (
            textwrap.dedent(f"""
            [ {media.mid} ]
            {media.title}
            Size: {fmt_size(media.size)}
            Seeders: {media.seeders}
            Leechers: {media.leechers}
            Uploader: {media.uploader}
            Time: {fmt_time(media.time)}
        """).strip()
            + "\n"
        )

    return "\n".join([list_info(media) for media in reversed(media_list)])


def format_media_info(media: Media) -> str:
    return (
        textwrap.dedent(f"""
        {media.title or "Unknown"}
        Size: {fmt_size(media.size)}
        Seeders: {media.seeders or "Unknown"}
        Leechers: {media.leechers or "Unknown"}
        Uploader: {media.uploader or "Unknown"}
        Time: {fmt_time(media.time)}
        HASH:
        {fmt_hash(media.info_hash, media.title)}

    """).strip()
        + "\n------\n"
        + (media.desc or "Unknown")
        + "\n------\n"
    )


def format_hot_list(media_list: list[Media]) -> str:
    def list_info(media: Media) -> str:
        return (
            textwrap.dedent(f"""
            [ {media.mid} ]
            {media.title} - ({fmt_size(media.size)})
            Time: {fmt_time(media.time)}
        """).strip()
            + "\n"
        )

    return "\n".join([list_info(media) for media in reversed(media_list)])


def fmt_time(ts: int | None) -> str:
    if not ts:
        return "Unknown"

    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def fmt_size(size: int | None) -> str:
    if not size:
        return "Unknown"

    read_size: float = size / 1024 / 1024
    if read_size > 1024:
        return f"{read_size / 1024:.2f} GB"
    else:
        return f"{read_size:.2f} MB"


def fmt_hash(hash: str | None, title: str | None) -> str:
    if not hash or not title:
        return "Unknown"

    url: str = HASH_URL.format(hash=hash, title=parse.quote(title))

    for x in TR_LIST:
        url += f"&tr={parse.quote(x, safe='')}"

    return url
