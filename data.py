import csv
from collections import Counter
from collections import defaultdict
import string
import re
import regex
import couchdb
#import search_blood
tweet_list=["#Thane #Mumbai Urgently needs A+ blood  At: Jupiter Hospital Call: 1237894560, 1236549870 #MuneerTweet Please ignore. Testing an app"
]
global_phone_list=[]

def extract_phone(row):

	m=re.search('[0-9]{10,}',row)
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




f=file("workingdb.csv","rU")
reader = csv.reader(f)


# Group 1= A+ 2= B+ 3= O+ 4= AB+ 5= A- 6= B- 7=AB- 8= O-

location_list=["Chennai","Bangalore","Mumbai","Delhi","Kolkata","Pondicherry","Hyderabad"]

blood_alpha =["AB Positive","AB positive","A positive","A Positive","B positive","B Positive","O positive","O Positive","AB negative","AB Negative", "A negative","A Negative","B negative","B Negative","O negative","O Negative",]
blood_alpha_numeric= ["AB-","AB -","A+","A +","B+","B +","AB+","AB +","O+","O +","A-","A -","B-","B -","O-","O -"]
f=file("workingdb.csv","rU")
reader = csv.reader(f)

while(1):
	
	for roww in reader:

		row =str(roww)
		phone = extract_phone(row)
		location = extract_location(row)
		group = extract_bloodgroup(row)

		if (len(group)==0):
			print "ERROR"

		print "phone number is"
		print phone

		print "group is"
		print group

		print "location is"
		print location

		"""server=couchdb.Server('http://blood.iriscouch.com:5984/')
		db=server['donors']

		doc_id,doc_rev= db.save({'bloodgroup':"H positive",'location':"CEG",'phone':"1223"})
		doc=db[doc_id]
		

		map_fun='''function(doc){emit(doc['location'],[doc['location'],doc['phone'],doc['bloodgroup']])}'''
		results=db.query(map_fun)

		for x in results:
		if(x.key=='Chennai'):
			print x"""

	







