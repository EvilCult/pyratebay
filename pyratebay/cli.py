import argparse
from pyratebay.main import search_command, info_command, hot_command

def main() -> None:
    parser = argparse.ArgumentParser(description="pyratebay, a simple command line tool for the pirate bay.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # search
    parser_search = subparsers.add_parser("search", help="Search torrent by keyword")
    parser_search.add_argument("query", type=str, help="Search keyword")
    parser_search.add_argument("-t", "--type", type=str, default="all", help="Type of content. e.g. movie, tv, music, etc.")
    parser_search.set_defaults(func=search_command)

    args = parser.parse_args()
    result = args.func(args)
    print(result)

    # info
    parser_info = subparsers.add_parser("info", help="Get torrent information by torrent id")
    parser_info.add_argument("tid", type=int, help="torrent id")
    parser_info.set_defaults(func=info_command)

    args = parser.parse_args()
    result = args.func(args)
    print(result)

    # hot
    parser_hot = subparsers.add_parser("hot", help="Get hot torrents")
    parser_hot.set_defaults(func=hot_command)

if __name__ == "__main__":
    main()