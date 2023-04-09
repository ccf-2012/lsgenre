from torcp.tmdbparser import TMDbNameParser
import argparse
import os


def listCategory():
    if not os.path.exists(ARGS.input_file):
        print(f"File not found: {ARGS.input_file}")
        return 
    ccfcat = None
    if ARGS.ccfcat:
        if ARGS.ccfcat in ['TV', 'tv']:
            ccfcat = 'TV'
        elif ARGS.ccfcat in ['Movie', 'movie', 'MOVIE']:
            ccfcat = 'Movie'

    p = TMDbNameParser(ARGS.tmdb_key, 'zh-CN', ccfcat_hard=ccfcat)
    with open(ARGS.input_file, encoding='utf-8') as in_file, open(ARGS.output_file, 'a', encoding='utf-8') as out_file:
        for item in in_file:
            p.parse(item.rstrip(), useTMDb=True)
            print(p.genre_ids)
            if p.genre_ids:
                if ARGS.genre_id in p.genre_ids:
                    print(">>> Output: " + item)
                    out_file.write(item)


def loadArgs():
    global ARGS
    parser = argparse.ArgumentParser(description='list media of specified category.')
    parser.add_argument('-i', '--input-file', required=True, help='file of input media list.')
    parser.add_argument('-o', '--output-file', required=True, help='file of output media list.')
    parser.add_argument('-g', '--genre-id', type=int, required=True, help='genre id to be extracted.')
    parser.add_argument('-c', '--ccfcat', help='specify the category(Movie/TV).')
    parser.add_argument('--tmdb-key', required=True, help='your TMDb key.')
    ARGS = parser.parse_args()


def main():
    loadArgs()
    listCategory()


if __name__ == '__main__':
    main()

