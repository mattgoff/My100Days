import csv
import pdb
from collections import namedtuple, defaultdict, Counter
from urllib.request import urlretrieve

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'

# urlretrieve(movie_data, movies_csv)

Movie = namedtuple("Movie", "title year score")

def get_movies_by_director(data=movies_csv):
    directors = defaultdict(list)
    with open(data, encoding="utf8") as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)
        
        return directors

directors = get_movies_by_director()
stuff = [x for x in directors['Christopher Nolan']]
for thing in stuff:
    print(thing)

cnt = Counter()
for director, movies in directors.items():
    cnt[director] += len(movies)

print(cnt.most_common(5))


