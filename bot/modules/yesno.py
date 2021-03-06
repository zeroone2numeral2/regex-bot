import re
import logging
from random import choice

from telegram.ext import RegexHandler

from bot import strings as s

logger = logging.getLogger(__name__)

YESNO_REGEX = re.compile(r".*(?:y(?:es)?\/no?|no?\/y(?:es)?)$", re.I)


def on_yesno(_, update):
    logger.info("yes/no")
    reply = choice(s.yesno_list)
    update.message.reply_text(reply)


class module:
    name = "yesno"
    handlers = (
        RegexHandler(YESNO_REGEX, on_yesno),
    )
