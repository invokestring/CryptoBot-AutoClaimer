from telethon import TelegramClient

async def Client(SessionName, ApiId, ApiHash):
    client = TelegramClient(
        SessionName,
        ApiId,
        ApiHash,
        device_model="iPhone 13 Pro Max",
        system_version="14.8.1",
        app_version="8.4",
        lang_code="en",
        system_lang_code="en-US"
    )
    await client.start()
    return client