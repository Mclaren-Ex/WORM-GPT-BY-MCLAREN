# WORM GPT 💀

Unrestricted AI Assistant developed by MCLAREN

## Features
- 🤖 Completely unrestricted AI responses
- 🔓 No content filtering
- 📊 Advanced analytics
- 💬 Multi-platform support
- 🌐 24/7 active on Render

## Setup
1. Get API keys (see below)
2. Deploy to Render
3. Configure environment variables

## APIs Needed
- OpenAI API Key
- Telegram Bot Token

## WORM GPT 💀 — Status & Usage

Unrestricted AI Assistant developed by MCLAREN.

Short status and run instructions for deployment:

- Bot status: exposed by the web UI at `/` (dark-themed status page).
- Health endpoint: `/health` returns JSON with `bot_running` and timestamp.
- Admin endpoints (protected by `?key=ADMIN_KEY`):
	- `/admin/list_users` — view allowed users and metadata
	- `/admin/set_trial?key=KEY&chat_id=ID&count=N` — set trial count
	- `/admin/grant_premium?key=KEY&chat_id=ID&tier=1m` — grant premium

Quick start (local):

1. Install dependencies from `requirements.txt` (use Python 3.10).

```bash
python -m pip install -r requirements.txt
```

2. Run the web server (this can start the Telegram bot via the `/start-bot` page):

```bash
python web_server.py
```

3. To run the bot directly:

```bash
python telegram_bot.py
```

Environment variables:
- `TELEGRAM_BOT_TOKEN` — Telegram bot token (can be hardcoded for quick tests).
- `OPENAI_API_KEY` — WormGPT/OpenAI-style API key used by the bot.
- `ADMIN_KEY` — key for admin HTTP endpoints (defaults to owner chat id `6094186912`).

Owner contact:
- Owner chat id: `6094186912`
- WhatsApp: `+2349163768735`

Disclaimer:
CREATED BY LORD MCLAREN ANY HARM CAUSED BY ME DO NOT BLAME MY LORD

See `web_server.py` for the live status page and `telegram_bot.py` for bot logic and admin commands.
