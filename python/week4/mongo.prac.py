import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


# movie_list = list(db.movies.find({}, {'_id': False}))
# for movie in movie_list:
#     print(movie)
# #

avengers = db.movies.find_one({'title': '어벤져스: 엔드게임'})
sameStars = list (db.movies.find({'star': avengers['star']}))
# print(sameStars)
# for movie in sameStars:
#     print(movie)

db.movies.update_many({'star': avengers['star']}, {'$set': {'star': 0}})

for movie in sameStars:
    print(movie)