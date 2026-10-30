from telegram import Update
from telegram.ext import ContextTypes


async def start_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """The /start command: tells new users what the bot does."""
    await update.message.reply_text(
        "Hi! I give you a reason to say no.\n\n"
        "Send me anything, or use /no, and I'll reply with a random, creative way "
        f"to say no. In groups, mention me as @{context.bot.username}.\n\n"
        f"In any other chat, type @{context.bot.username} and pick a reason to send."
    )
