from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import requests

@Client.on_message(filters.command("gita"))
async def get_gita_verse(_, message: Message):
    chapter_number = message.text.split(None, 1)[1]
    api_url = f"https://mukesh-api.vercel.app/bhagwatgita/{chapter_number}"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            verse = response.json().get("verse")
            chapter_name = response.json().get("chapter_name")
            
            caption = f"""
            📖 **Bhagwat Gita Verse**
            
            📚 **Chapter:** {chapter_name}
            💬 **Verse:** {verse}
            """
            
            await message.reply_text(caption)
        
        else:
            await message.reply_text("⚠️ Error occurred while fetching the verse. Please try again.")
    
    except Exception as e:
        await message.reply_text("⚠️ An unexpected error occurred.")
        print(e)
