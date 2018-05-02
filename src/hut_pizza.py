# -*- coding: utf-8 -*-
import re
import time
from datetime import datetime
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from config import hotel_name
from email_task import send_email


class HutPizza(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(HutPizza, self).__init__(*args, include_callback_query=True, **kwargs)
        print "Agent Started"
        # print args[0][1]

        # GET USER DETAILS BLOCK
        self.get_user_details(**args[0][1])
        self._count = 0
        self.bot_greetings = ['Hey', 'Hello', '/start', 'Hi', 'Howdy',
                                   'Hows is it going?', 'yes', 'no',
                                   'Continue', 'Book a table',
                                   'Hi book a table', 'I want to book a table',
                                   'Book a table', 'Nice to see you',
                                   'How are you?']
        self.table_type = ['bachelor', 'couple', 'family', 'senior citizen']
        self.meal_type = ['Veg', 'Non Veg']
        self.confirm_booking_type = ["confirm_booking"]
        self.cancel_booking_type = ["cancel_booking"]
        self.modify_booking_type = ["modify"]
        self.current_time_hour = int(
            datetime.fromtimestamp(int(time.time()), tz=None).strftime("%H"))
        self.is_user_greet = False
        self.hotel_name = hotel_name
        self.guest_range = [str(guest_range) for guest_range in
                                range(1, 21)]
        self.update = False
        self.book_table_type = ''
        self.book_meal_type = ''
        self.user_phone = ''
        self.booking_time = ''
        self.book_table_number = ''
        self.user_email = ''
        self.confirm_booking = False
        self.modify_booking = False

    def get_user_details(self, **kwargs):
        self.user_name = kwargs['from']['first_name']
        self.user_id = kwargs['from']['id']
        self.user_type = kwargs['from']['is_bot']
        self.user_timestamp = kwargs['date']

    def on_callback_query(self, msg):
        self.on_chat_message(msg)

    def on_chat_message(self, msg):
        """
        Function will first set all the member variables of the class and after
        that it will ask user's preferences depending upon which fields are
        empty. Initially all fields are empty then user ask one thing
        corresponding to that one member variable will set then bot ask other
        question then it will set other variable like so and so
        :param msg:
        :return:
        """
        if 'data' in msg:
            query_id, from_id, data = telepot.glance(msg,
                                                     flavor='callback_query')
            msg['text'] = data
            content_type = 'text'
        else:
            content_type, chat_type, chat_id = telepot.glance(msg)
        user_booking_time = re.match('[\d]{2}:[\d]{2}', msg['text'])
        user_phone_number = re.match('[\d]{10}', msg['text'])
        user_email_address = re.match(r"([\w.-]+)@([\w.-]+)", msg['text'])

        # process only those text which satisfy the below criteria
        if content_type == 'text' and \
            msg['text'] in self.bot_greetings or \
            msg['text'] in self.table_type or \
            msg['text'] in self.guest_range or \
            msg['text'] in self.meal_type or \
            msg['text'] in self.confirm_booking_type or \
            msg['text'] in self.cancel_booking_type or \
            msg['text'].lower() in self.modify_booking_type or \
                user_booking_time or user_email_address or user_phone_number:

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

            # table type check and book table
            if msg['text'] in self.table_type:
                if self.book_table_type:
                    self.sender.sendMessage(
                        "Preference Updated Table type {} => {}".format(
                            self.book_table_type, msg['text']
                        )
                    )
                else:
                    self.sender.sendMessage(
                        "Table Type set to: {}".format(msg['text']))
                self.book_table_type = msg['text']

            # book meal type and meal type check
            if msg['text'] in self.meal_type:
                if self.book_meal_type:
                    self.sender.sendMessage(
                        "Preference Updated Meal type {} => {}".format(
                            self.book_meal_type, msg['text']
                        )
                    )
                else:
                    self.sender.sendMessage(
                        "Meal Type set to: {}".format(msg['text']))
                self.book_meal_type = msg['text']

            # phone number update and phone check
            if user_phone_number and len(msg['text']) == 10:
                if self.user_phone:
                    self.sender.sendMessage(
                        "Preference Updated Phone Number {} => {}".format(
                            self.user_phone, msg['text']
                        )
                    )
                else:
                    self.sender.sendMessage(
                        "Phone Number set to: {}".format(msg['text']))
                self.user_phone = msg['text']

            # book time for the table
            if user_booking_time:
                if self.booking_time:
                    self.sender.sendMessage(
                        "Preference Updated Booking Time {} => {}".format(
                            self.booking_time, msg['text']
                        )
                    )
                else:
                    self.sender.sendMessage(
                        "Booking Time set to: {}".format(msg['text']))
                self.booking_time = msg['text']

            # book table according to guest number
            if msg['text'] in self.guest_range:
                if self.book_table_number:
                    self.sender.sendMessage(
                        "Preference Updated Guest Numbers {} => {}".format(
                            self.book_table_number, msg['text']
                        )
                    )
                else:
                    self.sender.sendMessage(
                        "Guest Numbers set to: {}".format(msg['text']))
                self.book_table_number = msg['text']

            # email update and phone check
            if user_email_address:
                if self.user_email:
                    self.sender.sendMessage(
                        "Preference Updated Email Address {} => {}".format(
                            self.user_email, msg['text']
                        )
                    )
                else:
                    self.sender.sendMessage(
                        "Email Address set to: {}".format(msg['text']))
                self.user_email = msg['text']

            if msg["text"] in self.cancel_booking_type:
                # cancel booking will wipe out every data entered by user
                self.sender.sendMessage(
                    "Booking Cancelled Successfully for User: {}".format(
                        self.user_name
                    )
                )
                self.user_email, self.book_table_number, \
                    self.booking_time, self.user_phone, \
                    self.book_table_type, self.book_meal_type = [False]*6

            if msg['text'] in self.confirm_booking_type:
                self.confirm_booking = True
                self.sender.sendMessage("Booking Confirmed")

            if str(msg['text']).lower() in self.modify_booking_type:
                self.modify_booking = True
                keyboard = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [InlineKeyboardButton(text='Phone Number',
                                              callback_data='modifybooking-user_phone')],
                        [InlineKeyboardButton(text='Email Address',
                                              callback_data='modifybooking-user_email')],
                        [InlineKeyboardButton(text='Table Type',
                                              callback_data='modifybooking-book_table_type')],
                        [InlineKeyboardButton(text='Number of Guests',
                                              callback_data='modifybooking-book_table_number')],
                        [InlineKeyboardButton(text='Booking Time',
                                              callback_data='modifybooking-booking_time')],
                        [InlineKeyboardButton(text='Meal Type',
                                              callback_data='modifybooking-book_meal_type')]
                    ]
                )
                self.sender.sendMessage(
                    '{} Which choice you want to modify'.format(
                        self.user_name),
                    reply_markup=keyboard
                )
            # messages to user
            if not self.book_meal_type:
                keyboard = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [InlineKeyboardButton(text='Vegetarian', callback_data='Veg')],
                        [InlineKeyboardButton(text='Non Vegetarian', callback_data='Non Veg')]
                    ]
                )
                self.sender.sendMessage(
                    '{} Please select Meal type from the below choices'.format(self.user_name),
                    reply_markup=keyboard
                )

            elif not self.book_table_type:
                keyboard = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [InlineKeyboardButton(text='Bachelor', callback_data='bachelor')],
                        [InlineKeyboardButton(text='Couple, Date Night', callback_data='couple')],
                        [InlineKeyboardButton(text='A Family Dinner', callback_data='family')],
                        [InlineKeyboardButton(text='Senior Citizen', callback_data='senior citizen')]
                         ]
                )
                self.sender.sendMessage(
                    '{} Please select Table type from the below choices'.format(self.user_name),
                    reply_markup=keyboard
                )

            elif not self.book_table_number:
                self.sender.sendMessage("Please Select Total No Of Seats Required")
                self.sender.sendMessage("Maximum Limit Per Customer : 20 Per Table")

            elif self.booking_time and int(self.booking_time.split(":")[0]) <= datetime.now().hour:
                self.booking_time = ''
                self.sender.sendMessage("Booking Time Cannot Be Current Time Or Time In Past, Please Try Again !")

            elif not self.booking_time:
                self.sender.sendMessage("Please Select Your Booking Time")
                self.sender.sendMessage("Valid Format Example : 15:00")

            elif not self.user_phone:
                self.sender.sendMessage("Please Provide Us Your 10 Digit Mobile Number")

            elif not self.user_email:
                self.sender.sendMessage("Please Provide Us Your Mail Id to Proceed")

            elif self.book_table_number and self.book_table_type and \
                self.user_phone and self.user_email and self.book_meal_type \
                    and self.booking_time and not self.modify_booking:
                data = "******************************\n\r Name : {}\n\r " \
                       "Phone : {}\n\r Email : {}\n\r Booking Table Type : " \
                       "{}\n\r Seating Capacity : {}\n\r Booking Time " \
                       "(IST 24.Hr) : {}\n\r Booking Meal Type : {}\n\r***" \
                       "***************************".format(
                            self.user_name.title(), self.user_phone,
                            self.user_email, self.book_table_type.title(),
                            self.book_table_number, self.booking_time,
                            self.book_meal_type
                )
                if not self.confirm_booking:
                    self.sender.sendMessage("Summary Of Booking")
                    self.sender.sendMessage(data)
                    keyboard = InlineKeyboardMarkup(
                        inline_keyboard=[
                            [
                                InlineKeyboardButton(
                                    text='Confirm Booking',
                                    callback_data=self.confirm_booking_type[0]
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    text='Cancel Booking',
                                    callback_data=self.cancel_booking_type[0]
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    text='Modify Booking',
                                    callback_data=self.modify_booking_type[0]
                                )
                            ],
                        ]
                    )
                    self.sender.sendMessage(
                        'Please Confirm/Cancel/Modify Booking',
                        reply_markup=keyboard
                    )
                else:
                    send_email(
                        self.user_email,
                        self.user_name,
                        data.replace('\n\r', '<br>')
                    )
                    self.sender.sendMessage("Email Shot Successfully to: {}"
                                            "".format(self.user_email))
                    self.confirm_booking = False

        elif str(msg['text']).lower() == 'help':
            self.sender.sendMessage(" --- HutPizza Guide --- \n\r "
                                    "---How To Book Your Table --- \n\r "
                                    "Initiate a Conversation With Bot like"
                                    " 'Hi or Book A Table' \n\r "
                                    "-------- \n\r "
                                    "1. Select Meal Type > Veg, Non Veg \n\r "
                                    "2. Select Table Type > "
                                    "bachelor,family,couple, senior \n\r "
                                    "3. No Of Seats > Min 1 - Max 20 \n\r "
                                    "4. Enter Your Booking Time \n\r "
                                    "5. Provide Us Your Mobile Number \n\r "
                                    "6. Provide Us With Your Email \n\r "
                                    "7. Summary or order on message and on "
                                    "email \n\r "
                                    "8. Your Table Is Booked \n\r "
                                    "9. To Cancel Your Booking Order "
                                    "Type =>'cancel' \n\r "
                                    "9. To Update The Field Simply Type "
                                    "'Modify'")

        elif str(msg['text']).lower() == 'status':
            self.sender.sendMessage(
                "*****STATUS***** \n\r"
                "Booked Meal Type: {}\n\r"
                "Booked Table Type: {}\n\r"
                "Booked Seats: {}\n\r"
                "Booking Time: {}\n\r"
                "Booked User Mobile Number: {}\n\r"
                "Booked User Email Address: {}".format(
                    self.book_meal_type, self.book_table_type,
                    self.book_table_number, self.booking_time,
                    self.user_phone, self.user_email
                )
            )

        elif self.modify_booking and msg['text'].split('-')[0] == 'modifybooking':
            attr = msg['text'].split('-')[1]
            setattr(self, attr, False)
            self.modify_booking = False
            self.sender.sendMessage("Enter New value")

        else:
            self.sender.sendMessage(
                "Sorry Didn't get that, I am a bot so please corporate !"
            )
            self.sender.sendMessage(
                "{} please type 'help' to know more about me".format(
                    self.user_name
                )
            )
            self.sender.sendMessage(
                "{} please type 'status' to get the status of booking".format(
                    self.user_name
                )
            )
            self.sender.sendMessage(
                "{} please type 'modify' to modify any choice".format(
                    self.user_name
                )
            )








