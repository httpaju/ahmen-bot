from pyrogram import Client, filters
from pyrogram.types import Message

# --- Configuration ---
API_ID = 22778903            # Your API ID
API_HASH = '0b5ebb13294a60a48918025d6f1d5056'  # Your API Hash
BOT_TOKEN = '7254902703:AAFcgC8cIR99LAtz7GH74ZZSnpdTyEKkxJ4'  # Replace with your new Bot Token
DATABASE_CHANNEL_ID = -1002299521243  # Your database channel ID

# Initialize the Pyrogram Client
app = Client("auto_filter_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Command to start the bot
@app.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply_text("Hello! Send me a movie name, and I'll fetch the movie for you from my database! 🎬")

# Auto-filter functionality to search for movies in the database channel
@app.on_message(filters.text & ~filters.command)
async def search_movie(client: Client, message: Message):
    query = message.text.strip().lower()
    async for msg in client.search_messages(chat_id=DATABASE_CHANNEL_ID, query=query):
        if msg.document:
            await message.reply_document(msg.document.file_id, caption=f"🎬 Here is your movie: **{msg.document.file_name}**")
            return
    await message.reply_text("❌ Sorry, I couldn't find that movie in my database.")

# Run the bot
if __name__ == "__main__":
    print("Bot is running...")
    app.run()
