import asyncio
import json


@asyncio.coroutine
def log(bot, message):
    print(message)
    yield from bot.post(
        'C035687FU', # Sunlight's #testing
        "```{}```".format(json.dumps(message, sort_keys=True, indent=2))
    )


@asyncio.coroutine
def emoji(bot, message):
    if ':shipit:' not in message['text']:
        return

    yield from bot.post(message['channel'], ':shipit:')
