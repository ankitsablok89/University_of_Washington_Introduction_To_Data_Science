# Author - Ankit Sablok
# Email-id - ankitsab@buffalo.edu
# Institution - University at Buffalo, The State University of New York
# Course - Introduction To Data Science

# this trick is done to force the division to be floating point division reference - http://stackoverflow.com/questions/1267869/how-can-i-force-division-to-be-floating-point-in-python
from __future__ import division

# import Python's regular expression, system and json modules for this problem
import re
import sys
import json

# this function is used to process the sentiment_file and return a dictionary of {word:sentiment_score}
def processSentimentFile(sentiment_file):

    # this is the dictionary which stores the {key:value} pairs, refer this link on how to create empty dictionaries - http://stackoverflow.com/questions/8424942/creating-a-new-dict-in-python
    sentimentScores = {}

    # start reading the file line by line
    for sentimentLine in sentiment_file:
        # remove any leading or trailing whitespaces from the line, refer as to what strip does from the following link - https://docs.python.org/2/library/string.html
        sentimentLine = sentimentLine.strip()

        # this is the word,score pair obtained from splitting the string on the basis of the tab character, more information about split is at - https://docs.python.org/2/library/string.html
        word, score = sentimentLine.split('\t')

        # we add the above pair to the dictionary as follows, we convert the string to an integer using the int() function in python
        sentimentScores[word] = int(score)

    return sentimentScores

# this function processes the output tweet file and evaluates the list of sentiment scores for each tweet in the file, it makes use of the dictionary sentimentDictionary object and it also takes as input the mapWordsNotInSentimentFile object which consists of {nonSentimentFileWord:[]} pairs
def processTweetFile(tweetFile, sentimentDictionary):

    # this map stores the list of {nonSentimentFileWord:[]} pairs
    mapNonSentimentWord = {}

    # scan the tweet file line by line to evaluate the sentiment scores, we only consider tweets that have "created_at" tag in them as these are the tweets that have text
    for tweet in tweetFile:
        if '"created_at"' in tweet:
            # use the json.loads(tweet) function to get a dictionary of different fields
            tweetDictionary = json.loads(tweet)

            # get the text of the tweet into this variable, as we are dealing with unicode string we have to tell Python to encode the string to a unicode string - http://www.tutorialspoint.com/python/string_encode.htm
            tweetText = tweetDictionary['text'].encode('utf-8')

            # split the tweet text on the basis of a regular expression and get all the constituent words in a list
            regex = re.compile(r'\w(?:[-\w]*\w)?')
            tweetWords = regex.findall(tweetText)

            # now we proceed with evaluating the score of the tweet
            sentimentScore = 0

            for word in tweetWords:
                if word in sentimentDictionary:
                    sentimentScore = sentimentScore + sentimentDictionary[word]

            for word in tweetWords:
                if word.lower() not in sentimentDictionary:
                    if word.lower() not in mapNonSentimentWord:
                        mapNonSentimentWord[word.lower()] = []
                        mapNonSentimentWord[word.lower()].append(sentimentScore)
                    else:
                        mapNonSentimentWord[word.lower()].append(sentimentScore)

    return mapNonSentimentWord


# this function is used to evaluate the sentiment scores of the new terms in the tweet file
def main():

    # this variable stores the handle of the sentiment file consisting of the words and their respective sentiment scores
    sentiment_file = open(sys.argv[1], 'r')

    # this variable stores the handle of the output.txt file consisting of all the tweets generated while solving problem - 1
    tweet_file = open(sys.argv[2], 'r')

    # this variable stores the dictionary returned by the processSentimentFile function of {word:sentiment_score}, we can confirm the dictionary is correct by finding the number of keys using the help from the following link - http://stackoverflow.com/questions/2212433/counting-the-number-of-keywords-in-a-dictionary-in-python
    sentimentDictionary = processSentimentFile(sentiment_file)

    # after forming the empty map of words not in sentiment file, process the tweet file to get the words and their respective tweet score list
    mapNonSentimentWord = processTweetFile(tweet_file,sentimentDictionary)

    for nonSentimentWord in mapNonSentimentWord.keys():
        sum = 0
        for score in mapNonSentimentWord[nonSentimentWord]:
            sum = sum + score
        print nonSentimentWord, " ", sum/len(mapNonSentimentWord[nonSentimentWord])

if __name__ == '__main__':
    main()
