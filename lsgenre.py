from torcp.tmdbparser import TMDbNameParser
import argparse
import os


def listCategory():
    if not os.path.exists(ARGS.input_file):
        print(f"File not found: {ARGS.input_file}")
        return 
    
    p = TMDbNameParser(ARGS.tmdb_key, 'zh-CN')
    with open(ARGS.input_file) as in_file:
        with open(ARGS.output_file, 'a') as out_file:
            for item in in_file:
                p.parse(item.rstrip(), useTMDb=True)
                if p.genre_ids:
                    if ARGS.genre_id in p.genre_ids:
                        print("Output: " + item)
                        out_file.write(item+"\n")


def loadArgs():
    global ARGS
    parser = argparse.ArgumentParser(description='list media of specified category.')
    parser.add_argument('-i', '--input-file', required=True, help='file of input media list.')
    parser.add_argument('-o', '--output-file', required=True, help='file of output media list.')
    parser.add_argument('-g', '--genre-id', required=True, help='genre id to be extracted.')
    parser.add_argument('--tmdb-key', required=True, help='your TMDb key.')
    ARGS = parser.parse_args()


def main():
    loadArgs()
    listCategory()


if __name__ == '__main__':
    main()

