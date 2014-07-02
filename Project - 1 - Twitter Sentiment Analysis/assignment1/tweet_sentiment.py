# Author - Ankit Sablok
# Email-id - ankitsab@buffalo.edu
# Institution - University at Buffalo, The State University of New York
# Course - Introduction To Data Science

# import Python's system module
import sys

# this function reads a file line by line and returns a list of 2-tuples of the form [(word,sentiment_score)]
def returnListOfTwoTuples(file_handle):

    # this is the list that will consist all the 2-tuples of words and their sentiment scores
    listOfTuples = []

    # start iterating on the file consisting of lines
    for line in file_handle:
        # strip off any leading or trailing whitespaces using the strip() function on string or the line just read
        line = line.strip()

        # split the line on the basis of the "\t" TAB character
        splitLine = line.split("\t")

        # convert the list of strings obtained above into a tuple using the tuple() conversion function and add it to the list
        listOfTuples.append(tuple(splitLine))

    # return the list of tuples formed
    return listOfTuples

# this is the main function which acts a  driver for evaluating the sentiment scores for the tweets
def main():
    # this variable stores the file handle for the sentiment file
    sentiment_file_handle = open(sys.argv[1],'r')

    # this variable stores the file handle for the tweet file
    tweet_file_handle = open(sys.argv[2],'r')

    print returnListOfTwoTuples(sentiment_file_handle)

if __name__ == "__main__":
    main()
