import csv
import pdb
from collections import namedtuple, defaultdict, Counter
from urllib.request import urlretrieve

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'

# urlretrieve(movie_data, movies_csv)

Movie = namedtuple("Movie", "title year score gross")

def get_movies_by_director(data=movies_csv):
    directors = defaultdict(list)
    with open(data, encoding="utf8") as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
                gross = int(line['gross'])
            except:
                continue

            m = Movie(title=movie, year=year, score=score, gross=gross)
            directors[director].append(m)
        return directors

directors = get_movies_by_director()

cnt = Counter()
for director, movies in directors.items():
    dir_total = 0
    for x in range(len(movies)):
        dir_total += movies[x][3]
    cnt[director] += dir_total

for xyz in cnt.most_common(25):
    print("{} - Total: {:,}".format(xyz[0], xyz[1]))


