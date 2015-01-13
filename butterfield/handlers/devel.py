import asyncio
import json
from .. import ALL


@asyncio.coroutine
def log(bot, message: ALL):
    print(message)
    yield from bot.post(
        bot.get_channel('testing')['id'],
        "```{}```".format(json.dumps(message, sort_keys=True, indent=2))
    )


@asyncio.coroutine
def emoji(bot, message: "message"):
    if ':shipit:' not in message['text']:
        return

    yield from bot.post(message['channel'], ':shipit:')
