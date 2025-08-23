from telethon.types import ReplyInlineMarkup, KeyboardButtonUrl
import re

async def HandleMessage(client, message, send_to, pattern, keyword, exclude_params: set):
    if message.text:
        matches = re.findall(pattern, message.text, re.IGNORECASE)
        for url, param in matches:
            if param.lower() in exclude_params:
                continue
            try:
                await client.send_message(send_to, f'/start {param}')
            except Exception as e:
                print(f"❌ Ошибка: {e}")

    if message.reply_markup and isinstance(message.reply_markup, ReplyInlineMarkup):
        for row in message.reply_markup.rows:
            for button in row.buttons:
                if isinstance(button, KeyboardButtonUrl):
                    if keyword in button.text.lower():
                        match = re.match(pattern, button.url, re.IGNORECASE)
                        if match:
                            param = match.group(2)
                            if param.lower() in exclude_params:
                                continue
                            try:
                                await client.send_message(send_to, f'/start {param}')
                            except Exception as error:
                                print(f"❌ Ошибка: {error}")