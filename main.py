import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update
from config import TELEGRAM_BOT_TOKEN, POSTGRES_CONFIG
from database import Database
from handlers import start_handler, help_handler, user_handler, admin_handler
from utils import setup_logger

# Setup logger
logger = setup_logger(__name__)

class ZenuxvnBot:
    def __init__(self):
        self.db = Database(POSTGRES_CONFIG)
        self.application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
        self.setup_handlers()
        
    def setup_handlers(self):
        """Setup all command and message handlers"""
        self.application.add_handler(CommandHandler("start", start_handler.handle_start))
        self.application.add_handler(CommandHandler("help", help_handler.handle_help))
        self.application.add_handler(CommandHandler("user", user_handler.handle_user))
        self.application.add_handler(CommandHandler("admin", admin_handler.handle_admin))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle regular messages"""
        user_id = update.effective_user.id
        username = update.effective_user.username
        message_text = update.message.text
        
        # Log user activity
        logger.info(f"Message from {username} ({user_id}): {message_text}")
        
        # Save user to database
        await self.db.save_user(user_id, username, update.effective_user.first_name)
        
    async def start_bot(self):
        """Start the bot"""
        logger.info("Starting Zenuxvn Bot...")
        await self.application.initialize()
        await self.application.start()
        await self.application.updater.start_polling()
        
    async def stop_bot(self):
        """Stop the bot"""
        logger.info("Stopping Zenuxvn Bot...")
        await self.application.stop()

async def main():
    bot = ZenuxvnBot()
    try:
        await bot.start_bot()
    except KeyboardInterrupt:
        logger.info("Bot interrupted by user")
        await bot.stop_bot()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())