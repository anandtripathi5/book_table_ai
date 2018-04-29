# -*- coding: utf-8 -*-
import re
import time
from datetime import datetime
import telepot

from config import hotel_name


class HutPizza(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(HutPizza, self).__init__(*args, **kwargs)
        print "Agent Started"
        # print args[0][1]

        # GET USER DETAILS BLOCK
        self.get_user_details(**args[0][1])
        self._count = 0
        self.bot_greetings = ['hey', 'hello', '/start', 'hi', 'howdy',
                                   'hows is it going?', 'yes', 'no',
                                   'continue', 'book a table',
                                   'hi book a table', 'i want to book a table',
                                   'book a table', 'nice to see you',
                                   'how are you?']
        self.table_type = ['bachelor', 'couple', 'family', 'senior citizen']
        self.current_time_hour = int(
            datetime.fromtimestamp(int(time.time()), tz=None).strftime("%H"))
        self.is_user_greet = False
        self.hotel_name = hotel_name
        self.guest_range = [str(guest_range) for guest_range in
                                range(1, 21)]

    def get_user_details(self, **kwargs):
        self.user_name = kwargs['from']['first_name']
        self.user_id = kwargs['from']['id']
        self.user_type = kwargs['from']['is_bot']
        self.user_lang = kwargs['from']['language_code']
        self.user_timestamp = kwargs['date']

    def on_chat_message(self, msg):
        # self._count += 1
        # self.sender.sendMessage("Number of message: {}, You said: {}".format(self._count, msg['text']))

        content_type, chat_type, chat_id = telepot.glance(msg)
        user_booking_time = re.match('[\d]{2}:[\d]{2}', msg['text']) or \
                       re.match('[\d]{2}\.[\d]{2}', msg['text'])
        user_phone_number = re.match('[\d]{10}', msg['text'])
        user_email_address = re.match(r"([\w.-]+)@([\w.-]+)", msg['text'])

        # process only those text which satisfy the below criteria
        if content_type == 'text' and \
                        msg['text'] in self.bot_greetings or \
                        msg['text'] in self.table_type or \
                        msg['text'] in self.guest_range or \
                        user_booking_time or user_email_address or \
                        user_phone_number:

            # greet if already not greeted
            greet = "Hello "
            if self.current_time_hour in range(00, 13):
                greet = "Good Morning "
            elif self.current_time_hour in range(12, 16):
                greet = "Good Afternoon "
            elif self.current_time_hour in range(15, 24):
                greet = "Good Evening "

            if not self.is_user_greet:
                self.sender.sendMessage(
                    '{} {}. Greetings From {} 🙋🏰!. How may we help you.'.format(
                        greet, self.user_name, self.hotel_name))
                self.is_user_greet = True

