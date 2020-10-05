# Note to future EG volunteers: avoid connecting to the API over the VPN; slowness may be observed.

from tmdbv3api import TMDb
from tmdbv3api import Movie

tmdb = TMDb()
tmdb.api_key = 'ca3c26eb1b4d3b51c8f1de0195429c46'

movie = Movie()
popular = movie.popular()

for p in popular:
    print(p.title)