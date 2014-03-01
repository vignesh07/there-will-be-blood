from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import pickle
import authentication_file
import math


ckey = authentication_file.consumer_key
csecret = authentication_file.consumer_secret
atoken = authentication_file.access_token
asecret = authentication_file.access_secret

class listener(StreamListener):
	def  on_data(self, data):
		try:
			#tweet = data.split(',"text":"')[1].split('","source')[0]
			#print tweet
			data_string=json.loads(data)
			#print data_string["text"]
			to_print = data_string["text"].encode('utf-8')
			print to_print
			data_loc=data_string["user"]
			data_loca=data_loc["location"].encode('utf-8')
			print data_loca
			
				
			saveFile = open('bloodDB.csv','a')
			saveFile.write(to_print)
			saveFile.write('\n')
			saveFile.close()
			return True
		except BaseException,e:
			print 'failed',str(e)
			time.sleep(5)
			
	def on_error(self,status):
		print status

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

twitterStream = Stream(auth,listener())
#twitterStream.filter(track=["Need O+ blood","Need A+ blood","Need B+ blood","Need AB+ blood","Need A- blood","Need B- blood","Need O- blood","Need AB- blood","A positive blood","B positive blood","O positive blood","AB positive blood","A negative blood","B negative blood","AB negative blood","O negative blood"])
twitterStream.filter(track=["#MuneerTweet"])