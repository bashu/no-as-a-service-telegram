import importlib
import pkgutil

from telegram.ext import Application


def register_extensions(application: Application) -> None:
    """Import every subpackage of bot/extensions and call its register(application)."""
    for module in pkgutil.iter_modules(__path__, f"{__name__}."):
        if module.ispkg:
            importlib.import_module(module.name).register(application)
