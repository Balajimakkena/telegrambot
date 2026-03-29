# Telegram Bot Project

A simple Telegram bot built with Python that can respond to user messages and fetch movie details using the OMDb API.

## Features

* Reply to user messages
* Search movies using the OMDb API
* Easy to customize and extend
* Built using Python and the Telegram Bot API

## Technologies Used

* Python
* python-telegram-bot
* requests
* OpenAI API
* OMDb API

## Project Structure

```text
Telegrambot/
│── bot.py
│── README.md
│── requirements.txt
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Balajimakkena/Telegram-bot-clean.git
cd Telegram-bot-clean
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Open `bot.py` and replace the placeholder values:

```python
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
OMDB_API_KEY = "YOUR_OMDB_API_KEY"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
```

## How to Run

```bash
python bot.py
```

If the bot starts successfully, you will see a message in the terminal.

## Example Commands

* `/start` – Start the bot
* Send a movie name – Get movie details

## Example Output

```text
Movie: Inception
Year: 2010
Rating: 8.8/10
Plot: A thief who steals corporate secrets through dream-sharing technology...
```

## Requirements File

Create a `requirements.txt` file with:

```text
python-telegram-bot
requests
openai
```

## Future Improvements

* Add more commands
* Improve movie recommendations
* Add error handling
* Deploy the bot online

## Author

Balaji Makkena
