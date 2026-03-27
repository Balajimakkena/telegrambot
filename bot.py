print("Starting bot...")

import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import openai
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
OMDB_API_KEY = "YOUR_OMDB_API_KEY"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"


openai.api_key = OPENAI_API_KEY

# 🎬 Movie Info Function (OMDb)
def get_movie(movie_name):
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={OMDB_API_KEY}"
    data = requests.get(url).json()

    if data["Response"] == "True":
        title = data["Title"]
        rating = data["imdbRating"]
        overview = data["Plot"]
        poster = data["Poster"]

        return title, rating, overview, poster
    return None

# 🤖 AI Recommendation
def recommend(movie_name):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Suggest 5 movies similar to {movie_name}"}]
    )
    return response['choices'][0]['message']['content']

# 🎬 Handle Messages
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    movie = get_movie(text)

    if movie:
        title, rating, overview, poster = movie

        reply = f"🎬 {title}\n⭐ Rating: {rating}\n\n📖 {overview}"

        # Send poster + info
        if poster != "N/A":
            await update.message.reply_photo(photo=poster, caption=reply)
        else:
            await update.message.reply_text(reply)

        # AI Recommendations
        recs = recommend(title)
        await update.message.reply_text(f"🤖 Recommendations:\n{recs}")
    else:
        await update.message.reply_text("❌ Movie not found")

# ▶️ Start Bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))
print("Bot is running...")

app.run_polling()
