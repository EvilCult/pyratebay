API_URL    = "https://apibay.org"
SEARCH_URL = "/q.php?q={query}&cat={typ}"
INFO_URL   = "/t.php?id={tid}"

MEDIA_TYP = {
    "all"  : "0",
    "movie": "207",
    "tv"   : "208",
    "music": "101",
}

FAKE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Referer"   : "https://thepiratebay.org",
}