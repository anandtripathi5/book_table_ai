# simple chat bot


# import sys
# import telepot
# import time
# from telepot.loop import MessageLoop
#
# def handle(msg):
#     print msg
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     if content_type == 'text':
#         bot.sendMessage(chat_id, "You said {}".format(msg['text']))
#
#
# # TOKEN = sys.argv[1]
#
# bot = telepot.Bot("565019895:AAGnzpHExod-WhJ9EehCthnC_0XvgskQ46c")
# MessageLoop(bot, handle).run_as_thread()
# print ('Listening ...')
#
# # Keep the program running.
# while 1:
#     time.sleep(10000)


# chatbot with inline keyboard

# import sys
# import telepot
# import time
# from telepot.loop import MessageLoop
# from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
#
#
# def on_chat_message(msg):
#     content_type, chat_type, chat_id = telepot.glance(msg)
#
#     keyboard = InlineKeyboardMarkup(inline_keyboard=[
#                    [InlineKeyboardButton(text='Press me', callback_data='press')],
#                ])
#
#     bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)
#
# def on_callback_query(msg):
#     query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
#     print('Callback Query:', query_id, from_id, query_data)
#
#     bot.answerCallbackQuery(query_id, text='Got it')
#
# bot = telepot.Bot("565019895:AAGnzpHExod-WhJ9EehCthnC_0XvgskQ46c")
# MessageLoop(bot, {'chat': on_chat_message,
#                   'callback_query': on_callback_query}).run_as_thread()
# print ('Listening ...')
#
# # Keep the program running.
# while 1:
#     time.sleep(10000)


# chatbot with state and timeout

import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.delegate import pave_event_space, per_chat_id, create_open


class MessageCounter(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(MessageCounter, self).__init__(*args, **kwargs)
        print args[0][1]
        self._count = 0

    def on_chat_message(self, msg):
        self._count += 1

        self.sender.sendMessage("Number of message: {}, You said: {}".format(self._count, msg['text']))

# TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.DelegatorBot("565019895:AAGnzpHExod-WhJ9EehCthnC_0XvgskQ46c", [
    pave_event_space()(
        per_chat_id(), create_open, MessageCounter, timeout = 300),
])
# timeout = 10
MessageLoop(bot).run_as_thread()

while 1:
    time.sleep(100000000)