from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession


api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
string = input('session code or press enter: ')

with TelegramClient(StringSession(string), api_id, api_hash) as client:
    print('-----------------------------------------------------')
    print(client.session.save())
    print('-----------------------------------------------------')






async def main():

    async for message in client.iter_messages(777000):

        print(message.sender.username, message.text)
        print('-----------------------------------------------------')
        break


with client:
    client.loop.run_until_complete(main())

