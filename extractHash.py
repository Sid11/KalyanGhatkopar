import csv
import json
import pandas as pd
print('Local change')
with open('twitter_extraction.json','r') as inputfile:
    tweet= inputfile.read()

tweet_json = json.loads(tweet)

with open('output.csv', 'w') as csvfile:
    fieldnames = ['created_at', 'user', 'hashtags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    #extract all info that you want to write
    #created_at = tweet_json["created_at"]
    created_at = [x["created_at"] for x in tweet_json]
    #selecting the screen_name of the user rather than id
    #user = tweet_json["user"]["screen_name"]
    #hashtags = tweet_json["entities"]["hashtags"]
    user  = [x["user"]["screen_name"] for x in tweet_json]
    hashtags = [x["entities"]["hashtags"] for x in tweet_json]
    #creating an empty string for the hashtags in the array
    hashes = list()
    #print(hashtags)
    for hashtag in hashtags:
        #text = hashtag["text"]
        text = [x["text"] for x in hashtag]
        #append to hashes listed_count
        hashes.append(text)
    #stringify the list and write to file (will be ugly)
    writer.writerow({"created_at":created_at, "user":user,"hashtags":str(hashes) })
    
