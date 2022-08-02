import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import AsukaRobot.modules.hentai_strings as hentai_strings
from AsukaRobot import dispatcher
from AsukaRobot.modules.disable import DisableAbleCommandHandler
from AsukaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from AsukaRobot.modules.helper_funcs.extraction import extract_user


@run_async
def hentaipic(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(hentai_strings.HENTAIPIC_STRINGS))


@run_async
def hentaivid(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(hentai_strings.HENTAIVID_STRINGS))


HENTAIPIC_HANDLER = DisableAbleCommandHandler("hentaipic", hentaipic)
HENTAIVID_HANDLER = DisableAbleCommandHandler("hentaivid", hentaivid)

dispatcher.add_handler(HENTAIPIC_HANDLER)
dispatcher.add_handler(HENTAIVID_HANDLER)

__mod_name__ = "Hentai"
__command_list__ = [
   "hentaipic", "hentaivid",
]

__handlers__ = [
    HENTAIPIC_HANDLER, HENTAIVID_HANDLER,
]
