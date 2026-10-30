import json
import logging
from pathlib import Path

from environs import Env
from telegram.ext import AIORateLimiter, Application

env = Env()
env.read_env()  # .env is optional; real environment variables take precedence

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    level=logging.INFO,
)
# httpx logs every getUpdates poll at INFO, which drowns out everything else
logging.getLogger("httpx").setLevel(logging.WARNING)

REASONS = tuple(
    json.loads((Path(__file__).parent / "reasons.json").read_text(encoding="utf-8"))
)

# Throttles our outgoing requests to stay under Telegram's flood limits
application = (
    Application.builder()
    .token(env.str("TELEGRAM_TOKEN"))
    .rate_limiter(AIORateLimiter())
    .build()
)
