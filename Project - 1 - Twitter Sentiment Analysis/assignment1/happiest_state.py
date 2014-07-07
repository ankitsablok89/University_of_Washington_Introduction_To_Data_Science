# Author - Ankit Sablok
# Email-id - ankitsab@buffalo.edu
# Institution - University at Buffalo, The State University of New York
# Course - Introduction To Data Science

# import Python's system and json modules for this problem
import sys
import json
import operator

# this dictionary object stores the mapping from the abbreviated state names to the actual state names in the US
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


# this function is used to evaluate the sentiment score of a tweet
def processTweetForSentimentScores(tweet, sentimentDictionary):

        # check if the tweet string consists of "created_at" tag
        if '"created_at"' in tweet:

            # use the json.loads(tweet) function to get a dictionary of different fields
            tweetDictionary = json.loads(tweet)

            # get the text of the tweet into this variable, as we are dealing with unicode string we have to tell Python to encode the string to a unicode string - http://www.tutorialspoint.com/python/string_encode.htm
            tweetText = tweetDictionary['text'].encode('utf-8')

            # split the tweet text on the basis of whitespace and get all the constituent words in a list
            tweetWords = tweetText.split()

            # now we proceed with evaluating the score of the tweet
            sentimentScore = 0

            for word in tweetWords:
                if word in sentimentDictionary:
                    sentimentScore = sentimentScore + sentimentDictionary[word]

            # return the sentiment score for the tweet
            return sentimentScore


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

# this function is used to find the geo-location of the tweet in the tweet file
def findGeoLocation(tweet_string):
    # get the json object corresponding to the tweet using json.loads() function
    tweetDictionary = json.loads(tweet_string)

    # after getting the dictionary object corresponding to the tweet check the type of its place key, this is how you set a conditional based on type in Python - http://stackoverflow.com/questions/14113187/how-do-you-set-a-conditional-in-python-based-on-datatypes, in the end I used the following link to loop out of a conditional statement - http://stackoverflow.com/questions/2069662/how-to-exit-an-if-clause
    if tweetDictionary['place'] is None:
        return
    else:
        # only consider the tweet if the country code is US
        if tweetDictionary['place']['country_code'] == "US":
            # store the exact location of the tweet using the full_name tag in the dictionary object in a variable
            exactLocation =  tweetDictionary['place']['full_name']

            # split the above location obtained on the basis of "," as the delimiter and store the components in a list object
            locationList = exactLocation.split(",")

            # return the location list to the calling function
            return locationList


# this function is used to evaluate the happiest state in the file of tweets
def main():

     # this variable stores the handle of the sentiment file consisting of the words and their respective sentiment scores
    sentiment_file = open(sys.argv[1], 'r')

    # this variable stores the handle of the output.txt file consisting of all the tweets generated while solving problem - 1
    tweet_file = open(sys.argv[2], 'r')

    # this variable stores the dictionary returned by the processSentimentFile function of {word:sentiment_score}, we can confirm the dictionary is correct by finding the number of keys using the help from the following link - http://stackoverflow.com/questions/2212433/counting-the-number-of-keywords-in-a-dictionary-in-python
    sentimentDictionary = processSentimentFile(sentiment_file)

    # this is the dictionary object that stores the mappings from state names to their cumulative sentiment scores of the tweets posted from that state
    stateScoreMapping = {}

    # this loop helps us to find out the geo location of the tweet in the tweet file
    for tweet in tweet_file:
        if '"created_at"' in tweet:
            # store the geo-location of a tweet in an object
            geoLocation = findGeoLocation(tweet)

            # check if the above object is a None object or not
            if geoLocation is not None:
                geoLocation[0] = geoLocation[0].encode('utf-8').strip()
                geoLocation[1] = geoLocation[1].encode('utf-8').strip()

                # filter out the name of the states from the list object received
                stateName = ""
                if geoLocation[1] == "USA":
                    stateName = geoLocation[0]
                else:
                    stateName = states[geoLocation[1]]

                # after getting the name of the state from the geo location data add the state along with the sentiment score of the tweet to the dictionary
                if stateName in stateScoreMapping:
                    stateScoreMapping[stateName] += processTweetForSentimentScores(tweet, sentimentDictionary)
                else:
                    stateScoreMapping[stateName] = processTweetForSentimentScores(tweet, sentimentDictionary)

    # this statement gives us a list representation of the dictionary sorted by their values
    stateScoreMapping = sorted(stateScoreMapping.iteritems(), key=operator.itemgetter(1))

    # as the list is sorted by sentiment scores the last element in the dictionary gives the name of the state that's most happy
    for key in states.keys():
        if states[key] == stateScoreMapping[len(stateScoreMapping) - 1][0]:
            print key
            break


if __name__ == "__main__":
    main()