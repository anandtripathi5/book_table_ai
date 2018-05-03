# -*- coding: utf-8 -*-

import telepot
import time
from telepot.delegate import pave_event_space, per_chat_id, create_open
from telepot.loop import MessageLoop

from config import telegram_bot_token
from src.hut_pizza import HutPizza
from src.logger import log


def bot_app_start(token):
    bot = telepot.DelegatorBot(token,
                               [
                                   pave_event_space()(
                                       per_chat_id(), create_open,
                                       HutPizza, timeout=300),
                               ])
    log.info("Bot started..........")
    MessageLoop(bot).run_as_thread()


# -------------------------------------------------------------

if __name__ == "__main__":
    bot_app_start(telegram_bot_token)
    while 1:
        time.sleep(10)
