from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import pickle
import authentication_file
import math
import re
import regex
import couchdb
from gcm import GCM
import access_gcm
import urllib2

tweet_list=["#Thane #Mumbai Urgently needs A+ blood  At: Jupiter Hospital Call: 1237894560, 1236549870 #MuneerTweet Please ignore. Testing an app"
]
global_phone_list=[]
location_list=["Chennai","Bangalore","Mumbai","Delhi","Kolkata","Pondicherry","Hyderabad"]

blood_alpha =["AB Positive","AB positive","A positive","A Positive","B positive","B Positive","O positive","O Positive","AB negative","AB Negative", "A negative","A Negative","B negative","B Negative","O negative","O Negative",]
blood_alpha_numeric= ["AB-","AB -","A+","A +","AB+","AB +", "B+","B +", "O+","O +","A-","A -","B-","B -","O-","O -"]

def extract_phone(row):
	m=re.search('[+91]?[0]?[0-9]{10,}',row)
	if m is None:
		return None

	phone=str(m.group(0))
	if phone in global_phone_list:
		return "already exists"
	global_phone_list.append(phone)

	return phone 


def extract_location(row):
	for loc in location_list:
		if loc in row:
			return loc

	return ""


def extract_bloodgroup(row):
	for grp in blood_alpha:
		if grp in row:
			return grp

	for grp in blood_alpha_numeric:
		if grp in row:
			return grp

	return ""

ckey = authentication_file.consumer_key
csecret = authentication_file.consumer_secret
atoken = authentication_file.access_token
asecret = authentication_file.access_secret

tweet_list=[]
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
			print "printing json"
			print data_string
			user= data_string["user"]
			#user_id=user["id"]
			name= str(user["screen_name"])
			url="http://www.twitter.com/"+name+"/status/"+str(data_string["id"])
			print url
				
			#saveFile = open('workingdb.csv','a')
			#saveFile.write(to_print)
			#tweet_list.append(to_print)
			#saveFile.write('\n')
			#saveFile.close()
		
			
			#f=file("workingdb.csv","rU")
			#reader = csv.reader(f)

		
			
			

			row =to_print
			phone = extract_phone(row)
			location = extract_location(row)
			group = extract_bloodgroup(row)

			if (len(group)==0):
				print "ERROR"
				return True
			if("already" in phone):
				return True
			print "phone number is"
			print phone

			print "group is"
			print group

			print "location is"
			print location

			msg=group + " blood needed in "+ location+ " to donate contact: " + phone 
			data = {'message': msg,'url':url}

			#gcmm = access_gcm.gcm
			#reg_ids = access_gcm.reg_ids
			#response = gcmm.json_request(registration_ids=reg_ids, data=data)

			ws = "http://gcm4public.appspot.com/sendgcm2clients?apiKey=AIzaSyCbEFJvsCgSgGulvJMcdnkqnFFuygFvPJE&senderId=538441063246&title=There_Will_Be_Blood&message=" + group + "%2B+blood+needed+in+" + location + "+to+donate+contact:+" + phone + "&url=" + url

			print ws

			urllib2.urlopen(ws).read()


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
