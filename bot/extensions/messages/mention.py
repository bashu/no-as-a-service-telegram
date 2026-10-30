import random

from telegram import MessageEntity, Update
from telegram.ext import ContextTypes

from bot import REASONS


async def mention_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """If someone mentions your bot in a group, reply with a random reason to say no."""
    message = update.message

    # The handler matches any @mention; only answer the ones addressed to us
    mentions = message.parse_entities([MessageEntity.MENTION]).values()
    if f"@{context.bot.username}".casefold() in map(str.casefold, mentions):
        await message.reply_text(random.choice(REASONS))
