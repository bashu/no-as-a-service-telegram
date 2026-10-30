from telegram.ext import Application, InlineQueryHandler

from .no import no_callback


def register(application: Application) -> None:
    application.add_handler(InlineQueryHandler(no_callback))
