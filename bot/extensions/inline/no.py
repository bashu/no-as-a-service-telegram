import random

from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import ContextTypes

from bot import REASONS

# How many reasons to offer above the keyboard
CHOICES = 3


async def no_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Typing @bot in any chat: offers a few random reasons to send from there."""
    indexes = random.sample(range(len(REASONS)), CHOICES)
    await update.inline_query.answer(
        [
            InlineQueryResultArticle(
                id=str(index),
                title=REASONS[index],
                input_message_content=InputTextMessageContent(REASONS[index]),
            )
            for index in indexes
        ],
        # Telegram caches answers for 5 minutes by default; ask for new reasons every time
        cache_time=0,
    )
