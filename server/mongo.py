import requests;
from dotenv import load_dotenv;
import os;
import pymongo;
from bson import ObjectId

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI, tlsAllowInvalidCertificates=True)

db = client["ytmanager"]
video_collection = db["videos"]

def createVideo(name, time) :
    video_collection.insert_one({"name": name, "time": time})

def readVideo() :
    videos = video_collection.find({}) # list all
    for video in videos :
        print(f"id {video['_id']} name {video['name']} time {video['time']}")

def update(vidoId, name, time) :
    video_collection.update_one({"_id": ObjectId(vidoId)}, {"$set": {"name": name, "time": time}}) # ({update who}, {update what})

def delete(vidoId) :
    video_collection.delete_one({"_id": ObjectId(vidoId)})

# print(video_collection)

def main() :
    while(1) :
        print("video manager")
        print("1. add video")
        print("2. get video")
        print("3. update video")
        print("4. delete video")
        print("5. exit")
        n = int(input("enter choice "))
        if(n == 1) :
            name = input("enter video name ")
            time = input("enter video time ")
            createVideo(name, time)
        elif(n == 2) :
            readVideo()
        elif(n == 3) :
            vidoId = input("enter video id ")
            name = input("enter video name ")
            time = input("enter video time ")
            update(vidoId, name, time)           
        elif(n == 4) :
            vidoId = input("enter video id ")
            delete(vidoId)
        else :
            break       
if __name__ == "__main__":
    main()