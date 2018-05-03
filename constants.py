# -*- coding: utf-8 -*-
import pytz
PHONE_NUMBER_SIZE = 10
BOT_GREETINGS = ['hey', 'hello', '/start', 'hi', 'howdy',
                    'hows is it going?', 'yes', 'no',
                    'continue', 'Book a table',
                    'hi book a table', 'i want to book a table',
                    'book a table', 'nice to see you',
                    'how are you?']
TABLE_TYPE = ['bachelor', 'couple', 'family', 'senior citizen']
MEAL_TYPE = ['veg', 'non veg']
REPLY_NOT_UNDERSTOOD = ['sorry, I did not understand that.',
                        'what was that ?',
                        'sorry, I did not catch that',
                        'i’m afraid it is not clear what '
                        'you mean to say',
                        "customer's discretion is advised",
                        "Ha ha, you don't know that I am a bot"]
TEXT_CONTENT_TYPE = 'text'
IST = pytz.timezone("Asia/Calcutta")