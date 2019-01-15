import pyrebase

config = {
    "apiKey": "AIzaSyC0HKmQOfQCSFMVhiVTEf-kddB-mLz-8Cg",
    "authDomain": "pychat-comsci.firebaseapp.com",
    "databaseURL": "https://pychat-comsci.firebaseio.com",
    "projectId": "pychat-comsci",
    "storageBucket": "pychat-comsci.appspot.com",
    "messagingSenderId": "512702370510"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
data = {"message": "Hello World!"}
db.child("users").push(data)

messages = db.child("users").get()

allMsgs = db.child("users").get()

for msg in allMsgs.each():
    print(msg.val().get('message'))



