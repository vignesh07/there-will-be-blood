import tweepy 
import csv
import nltk
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords

# Twitter Access Credentials
ckey = 'rAV2mtafN5mDY2A7DwmJvQ'
csecret = 'a96tvDGKLDevbZDOTBp1CA1U5jSWeO61N0MLM3jM6G4'
atoken = '172501485-IHHymsvCrNcK5WuMygbJIxmncOl77ZK37q1JhD9o'
asecret = 'dO9c2sWqP0DIz7oozenaAhMKbrt7U6eIqxdkegoxMaRjd'

# Magic Numbers. Input here
tweets_wanted = 40
handle = "SportsCenter"
start_tweet = 1



auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

api = tweepy.API(auth)

#new_tweets = api.user_timeline(screen_name = "willowkiller", count = 200)


all_tweets = []
# Each page pulls 20 tweets
cnt = (start_tweet / 20) + 1
lim = (tweets_wanted / 20) + cnt

# Pulling the data. Each page contains 20 tweets
while (cnt <= lim) :
	new_tweets = api.user_timeline(screen_name = handle, page = cnt)         
	all_tweets.extend(new_tweets)
	cnt += 1


# Pull out only the Tweets from all the other data
op = [tweet.text.encode("utf-8") for tweet in all_tweets]


for tweets in op:
	# Language Filter
	text = wordpunct_tokenize(tweets)
	lang_count = {} 
	words = [word.lower() for word in text] 

	for language in stopwords.fileids():
		stop_set = set(stopwords.words(language))
		word_set = set(words)

		common = word_set.intersection(stop_set)
		lang_count[language] = len(common)

	lang = max(lang_count,key = lang_count.get)
	# Store in DB
	if (lang == "english"): 
		print tweets
		saveFile = open('final.csv','a')
		saveFile.write(tweets)
		saveFile.write('\n')
		saveFile.close()
				

	





