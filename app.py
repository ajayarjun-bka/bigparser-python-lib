from bigparser import grid
from bigparser import auth

gridId = "57a34c80e4b017cc76c37c25"

# authId = auth.login("emailId", "password")

authId = auth.login("arjun.bka@gmail.com", "AjayArjun")

movies = grid(authId, gridId)

# headers = movies.getHeader()
# print(headers)
#
# rows = movies.getRows(searchfilter={'year': '2005'},columns=['film name ','language '])
# print(rows)


rows = movies.getRows(searchfilter={'GLOBAL': ['x-men'], 'year': ['2000','2016']},columns=['film name ', 'release date'])
print(rows)

# result = movies.getLastRow(count=2, columns=['film name ', 'language '])
# print(result)
#
# result = movies.getRange(rows=5, columns=2)
# print(result)
#
# rows = movies.getRows(searchfilter={'GLOBAL': ['x-men'], 'language ': 'english'}, sort=[{"year": "ASC"}],columns=['film name ', 'release date'])
# print(rows)