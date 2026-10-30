from telegram import Message, MessageEntity
from telegram.ext import Application, MessageHandler, filters

from .direct_message import direct_message_callback
from .mention import mention_callback


class Human(filters.MessageFilter):
    """Match messages from user accounts, skipping bots, anonymous admins and channels."""

    def filter(self, message: Message) -> bool:
        return message.from_user is not None and not message.from_user.is_bot


HUMAN = Human(name="HUMAN")


def register(application: Application) -> None:
    # Commands belong to extensions/commands; unknown ones get no reply
    application.add_handlers(
        [
            MessageHandler(
                (filters.UpdateType.MESSAGE & HUMAN & ~filters.COMMAND)
                & filters.ChatType.PRIVATE,
                direct_message_callback,
            ),
            MessageHandler(
                (filters.UpdateType.MESSAGE & HUMAN & ~filters.COMMAND)
                & filters.ChatType.GROUPS
                & filters.Entity(MessageEntity.MENTION),
                mention_callback,
            ),
        ]
    )
