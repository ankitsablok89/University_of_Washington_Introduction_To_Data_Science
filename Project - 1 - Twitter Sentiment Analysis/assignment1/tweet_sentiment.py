# Author - Ankit Sablok
# Email-id - ankitsab@buffalo.edu
# Institution - University at Buffalo, The State University of New York
# Course - Introduction To Data Science

# import Python's system module and json module
import sys
import json

# this function read the tweet file and returns a list of list of constitutent words in a tweet
def returnListOfListOfWordsInATweet(tweet_file_handle):

    # start iterating through the file consisting of tweets line by line
    for tweet in tweet_file_handle:
        if '"created_at":' in tweet:
            # use the json.loads(jsonString) function to get a dictionary data structure in which we have a text field consisting of the text of the tweet
            tweetDictionary = json.loads(tweet)
            print tweetDictionary


# this is the main function which acts a  driver for evaluating the sentiment scores for the tweets
def main():
    # this variable stores the file handle for the sentiment file
    sentiment_file_handle = open(sys.argv[1],'r')

    # this variable stores the file handle for the tweet file
    tweet_file_handle = open(sys.argv[2],'r')

    returnListOfListOfWordsInATweet(tweet_file_handle)

if __name__ == "__main__":
    main()
