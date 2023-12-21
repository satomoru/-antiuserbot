from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest

api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
# os.system("clear")


string = input('paste session or press enter: ')
with TelegramClient(StringSession(string), api_id, api_hash) as client:
    #client.send_message("me", client.session.save())
    print(client.session.save(), '\n')
    

async def main():
    #guruh = 'satomoru '

    #await client(JoinChannelRequest(guruh))
    while True:

        await client.send_message("satomoru" , input('message: '))


with client:
    client.loop.run_until_complete(main())
