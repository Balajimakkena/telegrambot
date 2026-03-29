import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
OMDB_API_KEY = "YOUR_OMDB_API_KEY"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! Send me any movie name and I will give you details like release year, director, rating, and cast."
    )


async def movie_details(update: Update, context: ContextTypes.DEFAULT_TYPE):
    movie_name = update.message.text

    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    movie_data = response.json()

    if movie_data.get("Response") == "True":
        title = movie_data.get("Title", "N/A")
        year = movie_data.get("Year", "N/A")
        director = movie_data.get("Director", "N/A")
        actors = movie_data.get("Actors", "N/A")
        rating = movie_data.get("imdbRating", "N/A")
        plot = movie_data.get("Plot", "N/A")

        message = (
            f"🎬 Movie: {title}\n"
            f"📅 Release Year: {year}\n"
            f"🎥 Director: {director}\n"
            f"⭐ IMDb Rating: {rating}\n"
            f"👥 Cast: {actors}\n\n"
            f"📝 Plot: {plot}"
        )

        await update.message.reply_text(message)
    else:
        await update.message.reply_text("Movie not found. Please send a correct movie name.")


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, movie_details))

print("Bot is running...")
app.run_polling()
