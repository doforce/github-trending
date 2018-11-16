data='\ndfdfdfd\n '
print(data.strip())
print(len(data.strip()))


test_str="c++"
rep=test_str.replace('-shuo','%23')
print(rep)

from trending import get_all_language

from pymongo import MongoClient

client = MongoClient("123.207.111.253",27017)

db = client['trending']

lang = get_all_language()

db.lang.insert_one(lang)

