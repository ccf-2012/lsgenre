# lsgenre

* 从文本里读取，每一行都是 `电影文件名 (年){tmdb-xxxx}` ，把指定分类筛选出来输出到新文本

## 安装
```sh
git clone https://github.com/ccf-2012/lsgenre.git
pip install -r requirements.txt
```

## 使用
```
python lsgenre.py -h
usage: lsgenre.py [-h] -i INPUT_FILE -o OUTPUT_FILE -g GENRE_ID [-c CCFCAT] --tmdb-key TMDB_KEY

list media of specified category.

options:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input-file INPUT_FILE
                        file of input media list.
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        file of output media list.
  -g GENRE_ID, --genre-id GENRE_ID
                        genre id to be extracted.
  -c CCFCAT, --ccfcat CCFCAT
                        specify the category(Movie/TV).
  --tmdb-key TMDB_KEY   your TMDb key.
```

其中 GENRE_ID 为 TMDb 所定义，中文 genre 为以下之一：
```py
GENRE_LIST_cn = [{'id': 28, 'name': '动作'}, {'id': 12, 'name': '冒险'}, {'id': 16, 'name': '动画'}, {'id': 35, 'name': '喜剧'}, {'id': 80, 'name': '犯罪'}, {'id': 99, 'name': '纪录'}, {'id': 18, 'name': '剧情'}, {'id': 10751, 'name': '家庭'}, {'id': 14, 'name': '奇幻'}, {
    'id': 36, 'name': '历史'}, {'id': 27, 'name': '恐怖'}, {'id': 10402, 'name': '音乐'}, {'id': 9648, 'name': '悬疑'}, {'id': 10749, 'name': '爱情'}, {'id': 878, 'name': '科幻'}, {'id': 10770, 'name': '电视电影'}, {'id': 53, 'name': '惊悚'}, {'id': 10752, 'name': '战争'}, {'id': 37, 'name': '西部'}]
```

* 在TMDb上查看完整列表，在浏览器中打以下地址：
```sh
https://api.themoviedb.org/3/genre/movie/list?api_key=<<api_key>>&language=zh-CN
```
> 替换 `<<api_key>>` 为你的 api key

## 例子
```sh
python3 lsgenre.py -i movies.txt -o animes.txt -g 16 -c Movie --tmdb-key your_tmdb_key
```
