from os import environ
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

C = [".", "/"]
CHANNELS = [int(chnel) for chnel in environ.get("CHANNELS", None).split()]       

authchat = filters.chat(CHANNELS) if CHANNELS else (filters.group | filters.channel)         

User = Client(
    name = "acceptUser",
    session_string = environ.get("SESSION"),
    api_id = int(environ.get("API_ID")),
    api_hash = environ.get("API_HASH")
)

@User.on_message(filters.command(["run", "approve"], C) & authchat)                     
async def approve(client: User, message: Message):
    chat=message.chat 
    try:
       await message.delete()
       await client.approve_all_chat_join_requests(chat.id) 
       await client.send_message(chat.id, "✅️ approving all joinrequest 🙏 please wait...")         
    except Exception as e:
       print(e)

@User.on_message(filters.command(["no", "remove", "decline"], C) & authchat)                     
async def decline(client: User, message: Message):
    chat=message.chat 
    try:
       await message.delete()
       await client.decline_all_chat_join_requests(chat.id) 
       await client.send_message(chat.id, "❌️ declining all joinrequest 🙏 please wait...")            
    except Exception as e:
       print(e)


print("bot started....")
User.run()
