import random

from telegram import Update
from telegram.ext import ContextTypes

from bot import REASONS


async def no_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """The /no command: replies with a random reason to say no."""
    await update.message.reply_text(random.choice(REASONS))
