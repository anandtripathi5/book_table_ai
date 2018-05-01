# -*- coding: utf-8 -*-

import telepot
import time
from telepot.delegate import pave_event_space, per_chat_id, create_open
from telepot.loop import MessageLoop

from config import telegram_bot_token
from src.hut_pizza import HutPizza


def bot_app_start(token):
    bot = telepot.DelegatorBot(token,
                               [
                                   pave_event_space()(
                                       per_chat_id(), create_open,
                                       HutPizza, timeout=300),
                               ])
    print "Bot started.........."
    MessageLoop(bot).run_as_thread()
    # bot.message_loop(run_forever=True)


# -------------------------------------------------------------

if __name__ == "__main__":
    bot_app_start(telegram_bot_token)
    while 1:
        time.sleep(10)