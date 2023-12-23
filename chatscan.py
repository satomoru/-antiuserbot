
######## @py_024
from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession
api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
		
string = input("sesson or press enter: ")
with TelegramClient(StringSession(string), api_id, api_hash) as client:
	client.send_message("me", client.session.save())
		###########
@client.on(events.NewMessage(pattern=".scan"))
async def chatscan(event):
	async for dailog in client.iter_dialogs():
		print("--------------------------\n" + dailog.name + " \n--------------------------\n id: " + str(dailog.id))
		
client.start()
client.run_until_disconnected()
	
		