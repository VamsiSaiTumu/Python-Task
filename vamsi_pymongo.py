import pandas as pd
import pymongo
data = pd.read_csv("climate_historic.csv")
# mydict=data.to_dict('records')
myclient= pymongo.MongoClient("mongodb://localhost:27017/")

'''created a database with name climate'''
mydb=myclient["climate"]

'''created a collection  with name historic_data'''
mycol=mydb["historic_data"]
print(mydb.list_collection_names())

mydict=data.to_dict('records')
x = mycol.insert_many(mydict)
# print(x)
# for x in mycol.find():
#     print(x)

#print(len(mydict))
'''a)records with ShelvLoc is Bad'''
# myquery = {'ShelveLoc':"Bad"}
# mydoc = mycol.find(myquery)
# for y in mydoc:
#      print(y)


'''b)records whose age is greater then 50 and US is Yes'''
# myquery = ({"$and":[{"Age": { "$gt": 50 }}, { 'US':'Yes' }]})
# mydoc=mycol.find(myquery)
# for z in mydoc:
#     print(z)

'''c)deleted the record whose price is greater than 120'''
# myquery = {"Price":{"$gt":120}}
# mydoc= mycol.find(myquery)
# for a in mydoc:
#     print(a)
# a= mycol.delete_many(myquery)
# print(a.deleted_count,"documents deleted.")



'''d)records with Urban value as yes or US value is yes'''
# myquery = ({"$or":[{"Age": { "urban":'Yes' }}, { 'US':'Yes' }]})
# mydoc=mycol.find(myquery)
# for b in mydoc:
#     print(b)

# '''E)to update the population to 200 having recors shelvolc as bad'''
# myquery={"ShelveLoc":"Bad"}
# newvalues={"$set":{"Population":200}}
# mydoc = mycol.update_many(myquery,newvalues)
# for i in mycol.find():
#     print(i)
# print ("raw:", mydoc.raw_result)
# print ("acknowledged:", mydoc.acknowledged)
# print(mydoc.modified_count, "documents updated.")


# '''F)to delete the records with sales less than 10'''
# myquery = {"Sales":{"$lt":10}}
# mydoc= mycol.find(myquery)
# for a in mydoc:
#     print(a)
# d = mycol.delete_many(myquery)
# print(d.deleted_count,"documents deleted")