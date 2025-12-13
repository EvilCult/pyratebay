from pyratebay.data_fetcher import Media, media_search, media_info, hot_media

def search_command(args) -> list[Media]:
    return media_search(args.query, args.type)

def info_command(args) -> Media:
    return media_info(args.tid)

def hot_command(args) -> list[Media]:
    return hot_media(args.type, args.limit)