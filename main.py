import pyrebase
from init import *

firebase = pyrebase.initialize_app(config)
db = firebase.database()


createRoom = input("Create a room Y/N?")
createRoom = createRoom.upper()

if createRoom == "Y":
    roomName = input("Room name:")
    data = {
        "roomName": roomName,
        "roomId": db.generate_key()
    }
    db.child("rooms").push(data)
    print("Room",roomName,"has been created!")
else:
    print("All Rooms:")


allMsgs = db.child("rooms").get()
roomNameArr = []
roomIds = []

for msg in allMsgs.each():
     roomNameArr.append(msg.val().get('roomName'))
     roomIds.append(msg.val().get('roomId'))
     print(msg.val())

print(roomNameArr)

enterRoom = input("Go to room...")


if enterRoom in roomNameArr:
    ix = roomNameArr.index(enterRoom)
    print(roomIds[ix])
else:
    print("nah")