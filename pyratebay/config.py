API_URL = "https://apibay.org"
SEARCH_URL = "/q.php?q={query}&cat={typ}"
INFO_URL = "/t.php?id={tid}"
HOT_URL = "/precompiled/data_top100{recent}_{typ}.json"
HASH_URL = "magnet:?xt=urn:btih:{hash}&dn={title}"

MEDIA_TYP = {
    "all": "0",
    "movie": "207",
    "tv": "208",
    "music": "101",
    "game": "400",
    "app": "300",
}

FAKE_HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://thepiratebay.org",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://thepiratebay.org/",
    "sec-ch-ua": '"Not-A.Brand";v="99", "Google Chrome";v="157", "Chromium";v="157"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36",
}


TR_LIST = [
    "udp://tracker.opentrackr.org:1337",
    "udp://open.stealth.si:80/announce",
    "udp://tracker.torrent.eu.org:451/announce",
    "udp://tracker.bittor.pw:1337/announce",
    "udp://public.popcorn-tracker.org:6969/announce",
    "udp://tracker.dler.org:6969/announce",
    "udp://exodus.desync.com:6969",
    "udp://open.demonii.com:1337/announce",
    "udp://glotorrents.pw:6969/announce",
    "udp://tracker.coppersurfer.tk:6969",
    "udp://torrent.gresille.org:80/announce",
    "udp://p4p.arenabg.com:1337",
    "udp://tracker.internetwarriors.net:1337",
]
