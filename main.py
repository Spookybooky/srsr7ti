import os
from pyrogram import Client, filters

app = Client(
    "my_account",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH")
)

@app.on_message(filters.me & filters.command("spam", prefixes="."))
async def spam_cmd(client, message):
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        return await message.edit("Используй: .spam [число] [текст]")
    
    count = int(args[1])
    text = args[2]
    
    await message.delete()
    for _ in range(count):
        await client.send_message(message.chat.id, text)

@app.on_message(filters.me & filters.command("help", prefixes="."))
async def help_cmd(client, message):
    await message.edit(
        "📋 Команды:\n.spam [число] [текст] — спам\n.help — список команд"
    )

app.run()
