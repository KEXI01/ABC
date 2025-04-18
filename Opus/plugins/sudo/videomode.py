
# All rights reserved.
#

from pyrogram.types import Message

import config
from strings import command
from Opus import app
from Opus.misc import SUDOERS
from Opus.utils.database import add_off, add_on
from Opus.utils.decorators.language import language


@app.on_message(command("VIDEOMODE_COMMAND") & SUDOERS)
@language
async def videoloaymode(client, message: Message, _):
    usage = _["vidmode_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "download":
        await add_on(config.YTDOWNLOADER)
        await message.reply_text(_["vidmode_2"])
    elif state == "m3u8":
        await add_off(config.YTDOWNLOADER)
        await message.reply_text(_["vidmode_3"])
    else:
        await message.reply_text(usage)
