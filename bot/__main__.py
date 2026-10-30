from telegram import Update

from bot import application
from bot.extensions import register_extensions

register_extensions(application)

application.run_polling(allowed_updates=Update.ALL_TYPES)
