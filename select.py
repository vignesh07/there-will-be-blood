import couchdb


server=couchdb.Server('http://blood.iriscouch.com:5984/')
db=server['donors']

