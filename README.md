# no-as-a-service-telegram

Bot that gives you a reason to say no.

A Telegram bot inspired by [No-as-a-Service](https://github.com/hotheadhacker/no-as-a-service).
Send it a message, mention it in a group, use the `/no` command, or type its name in any chat,
and it replies with a random, creative way to say no.

```
you:  @no_telegram_bot can you cover my shift on Saturday?
bot:  In a different season of life, I might say yes—but not right now.
```

## Use it on Telegram

Open [@no_telegram_bot](https://t.me/no_telegram_bot) and press **Start**. Then:

- **In a DM with the bot**, send anything, or `/no`.
- **In a group**, add the bot and mention it (`@no_telegram_bot ...`) or send `/no`.
- **In any other chat**, even a DM with someone else, type `@no_telegram_bot ` (with a space)
  and pick one of the reasons above the keyboard. It's sent from you, marked
  "via @no_telegram_bot", and the bot doesn't need to be in the chat.

Channel comments are messages in the channel's linked discussion group, so for mentions there
to work the bot has to be a member of that group.

## Self-hosting

1. Message [@BotFather](https://t.me/BotFather), send `/newbot` and follow the prompts. The
   username must be unique and end in `bot`. BotFather replies with the token.
2. Configure the bot with BotFather:
   - `/setinline`: enables inline mode (typing the bot's name in any chat). Set a placeholder
     such as `Ask me anything…`.
   - `/setprivacy` → **Disable**: lets the bot see mentions in groups. Do this before adding it
     to a group; if it's already there, remove it and add it again.
3. Put the token in `.env`, or set `TELEGRAM_TOKEN` as an environment variable:

   ```sh
   cp env.example .env
   # then set TELEGRAM_TOKEN=... in .env
   ```

   The bot loads `.env` on startup if it exists. A `TELEGRAM_TOKEN` set in the environment
   takes precedence over the file.

## Running

Locally with [uv](https://docs.astral.sh/uv/):

```sh
uv sync
uv run python -m bot
```

The bot uses long polling, so it needs no public URL or open port. Only run one copy per
token at a time; a second one makes Telegram return `Conflict` errors.

If typing the bot's name in a chat shows nothing right after enabling inline mode, your
Telegram app is still using cached bot info: open the bot's chat, or restart the app.

With Docker:

```sh
docker build -t no-as-a-service-telegram .
docker run --rm --env-file .env no-as-a-service-telegram
```

On Heroku, the included `Procfile` runs the bot as a `worker` dyno. Set `TELEGRAM_TOKEN`
in the app's config vars and scale the worker to one.

## Customizing

Reasons live in `bot/reasons.json`, a plain JSON array of strings. Edit it and restart the bot.

Handlers live in `bot/extensions/`, one subpackage per kind of update: `commands/`,
`messages/` and `inline/`. On startup, every subpackage there is imported and its
`register(application)` is called.

## Credits

Reasons come from [No-as-a-Service](https://github.com/hotheadhacker/no-as-a-service)
by hotheadhacker.

## License

[MIT](LICENSE)
