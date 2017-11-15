import tweepy #enable python to communicate with tweeter
import csv    #comma separated values.import and export format for spreadsheets and databases.
import re     #regular expression. allow special characters to be used without invoking their special meaning.

consumer_key = 'zDYrJ2VG5JaNDsl3jA0czECbQ' #consumer keys & secret to Id consummer
consumer_secret = 'HQhU93qYisgABvt0mG7R8n5c6jCwb5BuVmxL4XX5QtwXHaVVDL'
access_key = '4520495489-phgteznAan53FiS1pTh973pfzFiJLw1UF0PAc8h'
access_secret = '5VjdCLsiZGAT9Fa97VCV1MIfvcyDWucyip2Peq6OQrrsT'


def write_tweets_to_csv(tweets):          #take an array of raw tweets as a parameter
    with open ("tweets.csv","wb")as f:
        writer= csv.writer(f)             #open a cvs file
        for tweet in tweets:
            tweet = clean_tweet(tweet)#Calls the function clean_tweet
            if tweet:
                writer.writerow([tweet])#Output received is written down in a file, can see the output on shell when markov_test.py file is run



def get_twitter_tweets(clientName):#This function will get all tweets
    all_tweets = []#creates empty list called all_tweets
    new_tweets = []

    auth = tweepy.OAuthHandler (consumer_key, consumer_secret)#Checked for security and authentication purpose
    auth.set_access_token(access_key, access_secret) #oAuthhandler allows delegated access to private ressources.
    client = tweepy.API(auth)

    new_tweets = client.user_timeline(screen_name=clientName, count=200)#Gets allthe tweets from the user timeline.

    while len(new_tweets) > 0:#prints all the tweets from all_tweets list
        for tweet in new_tweets:
            if tweet.source == 'Twitter for iPhone':
                all_tweets.append (tweet.text.encode("utf-8")) #all tweets will be decoded once in the file.
        print ("we've got %s tweets so far" % (len(all_tweets)))#its a while loop that ,jump to a for loop,then print then go back around.always less than 200
        max_id = new_tweets[-1].id - 1 #updating the tweets to the newest one.
        new_tweets = client.user_timeline(screen_name=clientName,
                                          count=200,max_id=max_id)
    return all_tweets#returns the list


def clean_tweet(tweet) :#This function checks regex and helps to get the required markov chain
    tweet = re.sub("https?\:\/\/", "", tweet)  #links
    tweet = re.sub("#\S+", "", tweet)          #hashtagtweet
    tweet = re.sub("\.?@", "", tweet)          #at mentions
    tweet = re.sub("RT.+", "", tweet)          #Retweets
    tweet = re.sub("Video\:", "", tweet)       #Videos
    tweet = re.sub("\n", "", tweet)            #new lines
    tweet = re.sub("^\.\s.", "", tweet)        #leading whitespacemarkov_tweetB.py
    tweet = re.sub("\s+", " ", tweet)          #extra whitespace
    tweet = re.sub("&amp;", "and", tweet)      #encoded ampersand
    return tweet



if __name__ == "__main__":
    tweets = get_twitter_tweets("realdonaldtrump")#all_tweets list returned from get_twitter_tweets function is stored in tweets
    write_tweets_to_csv(tweets)#Tweets stored above is passed inside write_tweets_to_csv function

    #name is the name of the scope in witch top level code execute to run it directly as a script.






