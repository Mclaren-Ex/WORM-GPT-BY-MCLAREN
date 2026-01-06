from flask import Flask, jsonify
import threading
import time
import requests
import asyncio
import os

app = Flask(__name__)

# HARDCODED API KEYS
TELEGRAM_BOT_TOKEN = "8573861614:AAH3yCPlTkKdS-Jg84OrZbsHGhmKYOL-uDM"
OPENAI_API_KEY = "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"

print("🚀 WORM GPT WEB SERVER STARTING...")
print(f"🔑 Telegram Token: {TELEGRAM_BOT_TOKEN}")
print(f"🔑 OpenAI Key: {OPENAI_API_KEY}")

class ZARENAI:
    def __init__(self):
        self.is_running = False
        self.bot_thread = None
        
    def start_bot(self):
        """Start the Telegram bot in a separate thread with proper asyncio"""
        try:
            print("🤖 BOT THREAD: Starting...")
            
            # Create a new event loop for this thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            print("✅ BOT THREAD: Event loop created")
            
            try:
                # Import and run the bot with retries on transient errors
                from telegram_bot import start_telegram_bot
                print("✅ BOT THREAD: Bot module imported")

                max_retries = 5
                delay = 5
                for attempt in range(1, max_retries + 1):
                    try:
                        # Run the async bot function
                        loop.run_until_complete(start_telegram_bot())
                        print("✅ BOT THREAD: Bot started successfully!")
                        break
                    except Exception as e:
                        print(f"❌ BOT THREAD: Attempt {attempt} failed: {e}")
                        import traceback
                        traceback.print_exc()
                        if attempt < max_retries:
                            print(f"⏳ Retrying bot start in {delay} seconds...")
                            time.sleep(delay)
                            delay *= 2
                        else:
                            print("❌ BOT THREAD: All retries failed. Giving up.")
                            raise
            finally:
                loop.close()
                
        except Exception as e:
            print(f"❌ BOT THREAD: Thread crashed: {e}")
            import traceback
            traceback.print_exc()

zaren = ZARENAI()

@app.route('/')
def home():
    bot_status = "🟢 RUNNING" if zaren.is_running else "🔴 STOPPED"
    bot_color = "#00ff00" if zaren.is_running else "#ff0000"
    
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
            <title>WORM GPT 💀</title>
        <style>
            body {{
                background: #000;
                color: #0f0;
                font-family: 'Courier New', monospace;
                margin: 0;
                padding: 40px;
                text-align: center;
            }}
            .container {{
                max-width: 800px;
                margin: 0 auto;
                border: 2px solid #0f0;
                padding: 30px;
                border-radius: 10px;
                background: #111;
            }}
            h1 {{
                color: #ff0000;
                text-shadow: 0 0 10px #ff0000;
                font-size: 3em;
                margin-bottom: 10px;
            }}
            .status {{
                background: {bot_color};
                color: #000;
                padding: 15px;
                margin: 20px 0;
                border-radius: 8px;
                font-weight: bold;
                font-size: 1.2em;
            }}
            .button {{
                display: inline-block;
                background: #0f0;
                color: #000;
                padding: 15px 30px;
                margin: 10px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                font-size: 1.1em;
                border: 2px solid #0f0;
                transition: all 0.3s;
            }}
            .button:hover {{
                background: #000;
                color: #0f0;
            }}
            .info {{
                background: #222;
                padding: 20px;
                margin: 20px 0;
                border-radius: 8px;
                border: 1px solid #0f0;
                text-align: left;
            }}
            .made-by {{
                color: #888;
                margin-top: 40px;
                font-size: 0.9em;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>WORM GPT 💀</h1>
            <div style="color: #0f0; font-size: 1.2em; margin-bottom: 20px;">
                Unrestricted AI Assistant - Live Status
            </div>
            
            <div class="status">
                🤖 BOT STATUS: {bot_status}
            </div>
            
            <div class="info">
                <h3>🔧 System Information</h3>
                <p><strong>🔑 Telegram:</strong> ✅ Hardcoded & Ready</p>
                <p><strong>🔑 OpenAI:</strong> ✅ Hardcoded & Ready</p>
                <p><strong>🌐 Web Server:</strong> ✅ Running</p>
                <p><strong>🕒 Last Update:</strong> {time.strftime("%Y-%m-%d %H:%M:%S UTC")}</p>
            </div>
            
            <div>
                <a href="/start-bot" class="button">🚀 START BOT</a>
                <a href="https://t.me/8573861614Bot" class="button" target="_blank">💬 TEST ON TELEGRAM</a>
                <a href="/health" class="button">❤️ HEALTH CHECK</a>
            </div>
            
            <div class="info">
                <h3>📋 Next Steps</h3>
                <p>1. Click "START BOT" above</p>
                <p>2. Check Render logs for startup messages</p>
                <p>3. Test your bot on Telegram</p>
                <p>4. Send any message to get AI responses</p>
            </div>
            
                <div class="made-by">
                Made By MCLAREN💀<br>
                <span style="color: #ff0000;">UNRESTRICTED • UNFILTERED • UNSTOPPABLE</span>
            </div>
        </div>
        
        <script>
            console.log('💀 WORM GPT Status Monitor Active');
            console.log('🤖 Bot Status: {bot_status}');
        </script>
    </body>
    </html>
    '''

@app.route('/start-bot')
def start_bot_route():
    print("🔄 /start-bot endpoint called - Starting bot...")
    
    if not zaren.is_running:
        zaren.is_running = True
        
        # Start bot in a separate thread
        zaren.bot_thread = threading.Thread(target=zaren.start_bot)
        zaren.bot_thread.daemon = True
        zaren.bot_thread.start()
        
        print("✅ Bot thread started successfully!")
        
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Bot Started - WORM GPT</title>
            <style>
                body { background: #000; color: #0f0; font-family: monospace; padding: 40px; text-align: center; }
                .container { max-width: 600px; margin: 0 auto; border: 2px solid #0f0; padding: 30px; }
                .success { background: #00ff00; color: #000; padding: 15px; margin: 20px 0; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>✅ BOT STARTED!</h1>
                <div class="success">
                    WORM GPT Telegram bot is now starting...
                </div>
                <p>Check the Render logs for startup progress.</p>
                <p>Then test your bot: <a href="https://t.me/8573861614Bot" style="color: #0f0;">@8573861614Bot</a></p>
                <a href="/" style="color: #0f0;">← Back to Status</a>
            </div>
        </body>
        </html>
        '''
    else:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Bot Running - WORM GPT</title>
            <style>
                body { background: #000; color: #0f0; font-family: monospace; padding: 40px; text-align: center; }
                .container { max-width: 600px; margin: 0 auto; border: 2px solid #0f0; padding: 30px; }
                .info { background: #ffff00; color: #000; padding: 15px; margin: 20px 0; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>ℹ️ BOT ALREADY RUNNING</h1>
                <div class="info">
                    WORM GPT Telegram bot is already active!
                </div>
                <p>Test your bot: <a href="https://t.me/8573861614Bot" style="color: #0f0;">@8573861614Bot</a></p>
                <a href="/" style="color: #0f0;">← Back to Status</a>
            </div>
        </body>
        </html>
        '''

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "WORM GPT 💀",
        "bot_running": zaren.is_running,
        "timestamp": time.time()
    })

# Keep-alive function to prevent Render sleep
def keep_alive():
    while True:
        try:
            requests.get('https://worm-gpt22.onrender.com/health', timeout=10)
            time.sleep(300)  # Ping every 5 minutes
        except:
            time.sleep(60)

# Start keep-alive when module loads
keep_alive_thread = threading.Thread(target=keep_alive, daemon=True)
keep_alive_thread.start()

def start_server():
    port = int(os.environ.get("PORT", 5000))
    print(f"🌐 Starting Flask server on port {port}")
    print("💀 WORM GPT - Ready for deployment!")
    print("=" * 50)
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    start_server()
