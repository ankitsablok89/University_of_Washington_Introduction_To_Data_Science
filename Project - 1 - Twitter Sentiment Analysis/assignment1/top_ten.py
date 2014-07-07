# Author - Ankit Sablok
# Email-id - ankitsab@buffalo.edu
# Institution - University at Buffalo, The State University of New York
# Course - Introduction To Data Science

# import Python's system and json modules for this problem
import sys
import json
import operator

# this function is used to filter out the top 10 hash tags from the tweet data file "output.txt"
def main():

    # this variable stores the handle of the output.txt file consisting of all the tweets generated while solving problem - 1
    tweet_file = open(sys.argv[1], 'r')

    # this dictionary object stores the {hashtag:count} mappings
    hashTagMapping = {}

    # scan through the text of the tweet file and start filtering out the hashtags
    for tweet in tweet_file:

        # check if the tweet string consists of "created_at" tag, as these are tweets that have a text field inside them
        if '"created_at"' in tweet:
            # get the json dictionary object corresponding to the tweet
            tweetDictionary = json.loads(tweet)

            # get the list of hashtags embedded in the tweet data
            hashTagList = tweetDictionary['entities']['hashtags']

            # iterate through the hashtag list
            for i in range(len(hashTagList)):
                # this variable stores the text of the hashtag
                hashTagText = hashTagList[i]['text']

                # check if the text of the hashtag is already in the hashTagMapping or not
                if hashTagText in hashTagMapping:
                    hashTagMapping[hashTagText] += 1
                else:
                    hashTagMapping[hashTagText] = 1


    # get the sorted list representation for the hashtag mapping, sorted using the count of the hashtag's occurences
    hashTagMapping = sorted(hashTagMapping.iteritems(), key=operator.itemgetter(1))

    # reverse the list
    hashTagMapping.reverse()

    # change the keys to utf-8 strings
    hashTagMapping = [(tuple[0].encode('utf-8').strip(), tuple[1]) for tuple in hashTagMapping]

    # iterate through the list of tuples to print  the top 10 hashtags
    for i in range(10):
        print hashTagMapping[i][0], "", hashTagMapping[i][1]


if __name__ == "__main__":
    main()