from telegram.ext import Application, CommandHandler, filters

from .no import no_callback
from .start import start_callback


def register(application: Application) -> None:
    application.add_handlers(
        [
            CommandHandler("no", no_callback, filters.UpdateType.MESSAGE),
            CommandHandler("start", start_callback, filters.UpdateType.MESSAGE),
        ]
    )
