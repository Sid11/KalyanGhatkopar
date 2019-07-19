#!/usr/bin/env snap

import tweepy
import csv
import json
print("Remote change Local")

# Open/create a file to append data to
csvFile = open('output.csv', 'w')

#Use csv writer
csvWriter = csv.writer(csvFile)
print('Hello Siddhesh')


class TwitterExtract:


    def __init__(self):
        print("Yes")
        print("No")
        with open('event_credentials.json', 'r') as file:

            self.credentials = json.load(file)

        self.auth = tweepy.OAuthHandler(self.credentials['CONSUMER_KEY'], self.credentials['CONSUMER_SECRET'])

        self.auth.set_access_token(self.credentials['ACCESS_TOKEN'], self.credentials['ACCESS_SECRET'])

        self.api = tweepy.API(self.auth)

        self.search_tweets = []


    def extract_tweets(self, query='pulwama attack', max_tweets=100):

        assert max_tweets <= 100

        self.search_tweets = [status for status in tweepy.Cursor(self.api.search, q=query).items(max_tweets)]

        with open('twitter_extraction.json', 'w') as file:

            file.write('[')
            print('Hello again')

            for index, tweet in enumerate(self.search_tweets):

                file.write(json.dumps(tweet._json) + (', ' if index != len(self.search_tweets) - 1 else ''))

            file.write(']')
       
    def tocsv(self):	
        for tweet in tweepy.Cursor(self.api.search,q = "pulwana attack",lang = "en").items(100):
            # Write a row to the CSV file. I use encode UTF-8
            csvWriter.writerow([tweet.text.encode('utf-8')])
            print(tweet.entities)


print('Finally happening')

extractor = TwitterExtract()
extractor.tocsv()
extractor.extract_tweets() # Pass Parameters
