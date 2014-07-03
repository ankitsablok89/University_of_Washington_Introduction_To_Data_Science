# Author - Ankit Sablok
# Email-id - ankitsab@buffalo.edu
# Institution - University at Buffalo, The State University of New York
# Course - Introduction To Data Science

# this trick is done to force the division to be floating point division reference - http://stackoverflow.com/questions/1267869/how-can-i-force-division-to-be-floating-point-in-python
from __future__ import division

# import Python's system and json modules for this problem
import sys
import json

# this function gives us the dictionary of {term:occurrences} pairs by scanning the tweet file
def termDictionary(tweet_file):

    # this variable stores the {term:occurrences} dictionary and its empty at first
    dictionary = {}

    # scan the twwet_file line by line
    for tweet in tweet_file:
        if '"created_at"' in tweet:
            # use the json.loads(tweet) function to get a dictionary of different fields
            tweetDictionary = json.loads(tweet)

            # get the text of the tweet into this variable, as we are dealing with unicode string we have to tell Python to encode the string to a unicode string - http://www.tutorialspoint.com/python/string_encode.htm
            tweetText = tweetDictionary['text'].encode('utf-8')

            # strip off any leading or trailing whitespace from the tweet
            tweetText = tweetText.strip()

            # split the tweet text obtained above using the whitespace delimiters
            tweetTextSplit = tweetText.split()

            # scan through the list of words in the tweetTextSplit and add them to the dictionary if they are not already present in the dictionary
            for word in tweetTextSplit:
                if word in dictionary.keys():
                    dictionary[word] = dictionary[word] + 1
                else:
                    dictionary[word] = 1

    return dictionary

# this function is used to evaluate the frequency of all the terms in the output tweet file
def main():

    # this variable stores the handle of the tweet file which we use to evaluate the frequencies of all the terms
    tweet_file = open(sys.argv[1], 'r')

    # call this function to get a dictionary of {term:occurences} pairs
    dictionary = termDictionary(tweet_file)

    # this variable stores the total occurrences of all the terms in all the tweets
    totalOccurrences = 0

    # this variable stores the list of keys corressponding to the twitter dataset
    wordList = dictionary.keys()

    # iterate on the dictionary to get the total occurences value
    for words in wordList:
        totalOccurrences = totalOccurrences + dictionary[words]

    # now the only thing that remains is to print out the frequencies of all the words encounterd
    for words in wordList:
        print words, " ", dictionary[words]/totalOccurrences

if __name__ == "__main__":
    main()