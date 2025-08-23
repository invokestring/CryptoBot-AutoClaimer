from telethon import events
import asyncio
from Config import API_ID, API_HASH, PATTERN
from Handlers import HandleMessage
from Client import Client as CreateClient  
import Other

async def main():
    Other.welcome()
    client = await CreateClient("session", API_ID, API_HASH)

    @client.on(events.NewMessage())
    async def newmessage_handler(event):
        await HandleMessage(client, event.message, "send", PATTERN, "получить", {'p2p'})

    @client.on(events.MessageEdited())
    async def editedmessage_handler(event):
        await HandleMessage(client, event.message, "send", PATTERN, "получить", {'p2p'})

    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())