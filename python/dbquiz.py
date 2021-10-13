from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# movie = db.movies.find_one({'title':'매트릭스'})
# target_point = movie['point']
#
# target_movies = list(db.movies.find({'point':target_point}))
#
# for target in target_movies:
#     print(target['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'point':'0'}})
