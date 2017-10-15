import pymongo
from numpy import genfromtxt
import numpy
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient('143.215.113.53', 27017)
db = client['IAPD']
collection = db["SEC_firms_clean"]
keys = genfromtxt('supervised.csv', delimiter=',', dtype="str")[1:,0]
def getVal(doc, family, key):
    try:
        if key == "@CourtCases":
            build = []
            for thing in doc["Firm"][family][key]:
                build.append(str(thing))
            print(str(build).replace("\'","\""))
            return str(build).replace("\'","\"")
        return (str(doc["Firm"][family][key]).strip())
    except Exception as e:
        return str(None)


end = ""
for id in keys:
    stuff = ""
    doc = collection.find({"_id": ObjectId(id)}).next()
    stuff += (getVal(doc, "Info", "@BusNm")) + "|~"
    stuff += (getVal(doc, "Info", "@SECNb")) + "|~"
    stuff += (getVal(doc, "MainAddr", "@City")) + "|~"
    stuff +=(getVal(doc, "MainAddr", "@State")) + "|~"
    stuff +=(getVal(doc, "Info", "@CourtCases"))
    end += stuff + "\n"
    #print(stuff)

f = open('info.csv', 'w')
f.write(end)  # python will convert \n to os.linesep
f.close() 

