# -*- coding: utf-8 -*-
import random
import re
import time
from datetime import datetime
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from config import hotel_name
from constants import PHONE_NUMBER_SIZE, BOT_GREETINGS, \
    TABLE_TYPE, MEAL_TYPE, REPLY_NOT_UNDERSTOOD, TEXT_CONTENT_TYPE, IST
from email_task import send_email
from logger import log, function_logger
from models import add_user, create_client, get_user


class HutPizza(telepot.helper.ChatHandler):
    """
    on_chat_message will be called on every reply from user
    """
    def __init__(self, *args, **kwargs):
        super(HutPizza, self).__init__(*args, include_callback_query=True,
                                       **kwargs)
        log.info("Agent Started")
        self.is_user_greet, self.update, self.book_table_type, \
            self.book_meal_type, self.user_phone, self.booking_time, \
            self.book_table_number, self.user_email, self.user_name, \
            self.user_id, self.user_type, self.user_timestamp, \
            self.confirm_booking, self.modify_booking, \
            self.returning_user = [False] * 15

        self.__set_seed_data_for_comparison()
        self.client = create_client()
        self.get_user_details(**args[0][1])

    @function_logger(log)
    def __set_seed_data_for_comparison(self):
        self.bot_greetings = BOT_GREETINGS
        self.table_type = TABLE_TYPE
        self.meal_type = MEAL_TYPE
        self.confirm_booking_type, self.cancel_booking_type, \
            self.modify_booking_type = ["confirm_booking"], \
                                        ["cancel_booking"], \
                                       ["modify"]
        self.current_time_hour = int(
            datetime.fromtimestamp(int(time.time()), tz=IST).strftime("%H"))
        self.hotel_name = hotel_name
        self.guest_range = [str(guest_range) for guest_range in
                            range(1, 21)]
        self.reply_not_understood = REPLY_NOT_UNDERSTOOD

    @function_logger(log)
    def get_user_details(self, **kwargs):
        self.user_name = kwargs['from']['first_name']
        self.user_id = kwargs['from']['id']
        self.user_type = kwargs['from']['is_bot']
        self.user_timestamp = kwargs['date']

    def on_callback_query(self, msg):
        self.on_chat_message(msg)

    @staticmethod
    def get_msg_data(msg):
        """
        function will collect data from message and process text from msg
        for future comparisons
        :param msg:
        :return: content_type, msg
        """
        if 'data' in msg:
            telepot.glance(msg, flavor='callback_query')
            msg['text'] = msg['data']
            content_type = TEXT_CONTENT_TYPE
        else:
            content_type, chat_type, chat_id = telepot.glance(msg)
        msg['text'] = msg['text'].lower()
        return content_type, msg

    @staticmethod
    def parse_user_details_from_msg(msg):
        """
        function will parse time, phone number and email address from coming
        message text
        :param msg:
        :return: user_booking_time, user_phone_number, user_email_address
        """
        user_booking_time = re.match('[\d]{2}:[\d]{2}', msg['text'])
        user_phone_number = re.match('[\d]{10}', msg['text'])
        user_email_address = re.match(r"([\w.-]+)@([\w.-]+)", msg['text'])
        return user_booking_time, user_phone_number, user_email_address

    def handler_returning_user(self):
        """
        Function will handler returning user. If returning user is encountered
        then all the details of the previous booking will set for this session
        :return:
        """
        if not self.returning_user:
            user_data = get_user(self.client, self.user_id)
            if user_data:
                self.sender.sendMessage("Hi {}, Welcome Again to HutPizza. "
                                        "Find the details of previous "
                                        "booking".format(
                                                        self.user_name)
                                        )
                self.user_email = user_data.get("email")
                self.user_phone = user_data.get("phone")
                self.book_table_type = user_data.get("table_type")
                self.book_table_number = user_data.get("table_number")
                self.booking_time = user_data.get("booking_time")
                self.book_meal_type = user_data.get("meal_type")
                self.returning_user = True

    def greet_user_function(self):
        """
        Function will greet user for the first time
        :return:
        """
        greet = "Hello "
        if self.current_time_hour in range(00, 13):
            greet = "Good Morning "
        elif self.current_time_hour in range(12, 16):
            greet = "Good Afternoon "
        elif self.current_time_hour in range(15, 24):
            greet = "Good Evening "

        if not self.is_user_greet and not self.returning_user:
            self.sender.sendMessage(
                '{} {}. Greetings From {} 🙋🏰!. How may we help you.'.format(
                    greet, self.user_name, self.hotel_name))
            self.is_user_greet = True

    def user_book_table_type(self, msg):
        """
        function will check whether incoming text containing table type, then
        book that table type for the user.
        :param msg:
        :return:
        """
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

    def user_book_meal_type(self, msg):
        """
        function will check whether incoming text containing meal type, then
        book that table type for the user.
        :param msg:
        :return:
        """
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

    def user_phone_number_update(self, msg, user_phone_number):
        """
        Function will check whether parse message is phone number and length
        of msg is 10 then will update the user phone number
        :param msg:
        :param user_phone_number:
        :return:
        """
        if user_phone_number and len(msg['text']) == PHONE_NUMBER_SIZE:
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

    def user_booking_time_update(self, msg, user_booking_time):
        """
        Function will check parse message is booking time then user's
        booking time will be updated
        :param msg:
        :param user_booking_time:
        :return:
        """
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

    def user_book_guest_number_update(self, msg):
        """
        function will update the number of guest coming to restuarant
        :param msg:
        :return:
        """
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

    def user_email_address_update(self, msg, user_email_address):
        """
        If incoming message containing email_address then it will update
        user's email address
        :param msg:
        :param user_email_address:
        :return:
        """
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

    def cancel_user_booking(self, msg):
        """
        cancel booking will delete all the user's data and user will have to
        enter details again
        :param msg:
        :return:
        """
        if msg["text"] in self.cancel_booking_type:
            # cancel booking will wipe out every data entered by user
            self.sender.sendMessage(
                "Booking Cancelled Successfully for User: {}".format(
                    self.user_name
                )
            )
            self.user_email, self.book_table_number, \
                self.booking_time, self.user_phone, \
                self.book_table_type, self.book_meal_type = [False] * 6

    def confirm_user_booking(self, msg):
        """
        If incoming message containing confirm then it will confirm booking
        for the user
        :param msg:
        :return:
        """
        if msg['text'] in self.confirm_booking_type:
            self.confirm_booking = True
            self.sender.sendMessage("Booking Confirmed")

    @function_logger(log)
    def modify_user_booking_prompt(self, msg):
        """
        Function will ask user to modify any field and user have to click on
        any field to modify
        :param msg:
        :return:
        """
        if str(msg['text']).lower() in self.modify_booking_type:
            self.modify_booking = True
            keyboard = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(
                        text='Phone Number',
                        callback_data='modifybooking-user_phone'
                    )],
                    [InlineKeyboardButton(
                        text='Email Address',
                        callback_data='modifybooking-user_email'
                    )],
                    [InlineKeyboardButton(
                        text='Table Type',
                        callback_data='modifybooking-book_table_type'
                    )],
                    [InlineKeyboardButton(
                        text='Number of Guests',
                        callback_data='modifybooking-book_table_number'
                    )],
                    [InlineKeyboardButton(
                        text='Booking Time',
                        callback_data='modifybooking-booking_time'
                    )],
                    [InlineKeyboardButton(
                        text='Meal Type',
                        callback_data='modifybooking-book_meal_type'
                    )]
                ]
            )
            self.sender.sendMessage(
                '{} Which choice you want to modify'.format(
                    self.user_name),
                reply_markup=keyboard
            )

    def book_meal_type_prompt(self):
        """
        Book meal type prompt to user if meal type is not provided
        :return:
        """
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='Vegetarian',
                                      callback_data='Veg')],
                [InlineKeyboardButton(text='Non Vegetarian',
                                      callback_data='Non Veg')]
            ]
        )
        self.sender.sendMessage(
            '{} Please select Meal type from the below choices'.format(
                self.user_name),
            reply_markup=keyboard
        )

    def book_table_type_prompt(self):
        """
        book table type prompt to user if table type is not set
        :return:
        """
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='Bachelor',
                                      callback_data='bachelor')],
                [InlineKeyboardButton(text='Couple, Date Night',
                                      callback_data='couple')],
                [InlineKeyboardButton(text='A Family Dinner',
                                      callback_data='family')],
                [InlineKeyboardButton(text='Senior Citizen',
                                      callback_data='senior citizen')]
            ]
        )
        self.sender.sendMessage(
            '{} Please select Table type from the below choices'.format(
                self.user_name),
            reply_markup=keyboard
        )

    def book_table_number_prompt(self):
        self.sender.sendMessage(
            "Please Select Total No Of Seats Required")
        self.sender.sendMessage(
            "Maximum Limit Per Customer : 20 Per Table")

    @function_logger(log)
    def confirm_cancel_modify(self):
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
            log.info("Confirm booking not set")
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
            log.info("Confirm booking is set send email")
            send_email(
                self.user_email,
                self.user_name,
                data.replace('\n\r', '<br>')
            )
            self.sender.sendMessage("Email Sent Successfully to: {}"
                                    "".format(self.user_email))
            add_user(
                self.client,
                user_id=self.user_id,
                name=self.user_name,
                email=self.user_email,
                created_on=self.user_timestamp,
                phone=self.user_phone,
                table_type=self.book_table_type,
                table_number=self.book_table_number,
                booking_time=self.booking_time,
                meal_type=self.book_meal_type
            )
            self.confirm_booking = False

    @function_logger(log)
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
        content_type, msg = self.get_msg_data(msg)
        user_booking_time, user_phone_number, user_email_address = \
            self.parse_user_details_from_msg(msg)
        self.handler_returning_user()

        # process only those text which satisfy the below criteria
        if content_type == 'text' and \
            msg['text'] in self.bot_greetings or \
            msg['text'] in self.table_type or \
            msg['text'] in self.guest_range or \
            msg['text'] in self.meal_type or \
            msg['text'] in self.confirm_booking_type or \
            msg['text'] in self.cancel_booking_type or \
            msg['text'] in self.modify_booking_type or \
                user_booking_time or user_email_address or user_phone_number:

            # greet if already not greeted
            self.greet_user_function()
            # table type check and book table
            self.user_book_table_type(msg)
            # book meal type and meal type check
            self.user_book_meal_type(msg)
            # phone number update and phone check
            self.user_phone_number_update(msg, user_phone_number)
            # book time for the table
            self.user_booking_time_update(msg, user_booking_time)
            # book table according to guest number
            self.user_book_guest_number_update(msg)
            # email update and phone check
            self.user_email_address_update(msg, user_email_address)
            # cancel booking
            self.cancel_user_booking(msg)
            # confirm booking
            self.confirm_user_booking(msg)
            # modify booking
            self.modify_user_booking_prompt(msg)

            # messages to user
            # meal type not set prompt user
            if not self.book_meal_type:
                self.book_meal_type_prompt()
            # table type not set prompt user
            elif not self.book_table_type:
                self.book_table_type_prompt()
            # guest number not set prompt user
            elif not self.book_table_number:
                self.book_table_number_prompt()
            # booking time not set prompt user
            elif self.booking_time and int(
                    self.booking_time.split(":")[0]) <= datetime.now(tz=IST).hour:
                self.booking_time = ''
                self.sender.sendMessage(
                    "Booking Time Cannot Be Current Time Or Time In Past, "
                    "Please Try Again !")
            elif not self.booking_time:
                self.sender.sendMessage("Please Select Your Booking Time")
                self.sender.sendMessage("Valid Format Example : 15:00")
            # phone number not set prompt user
            elif not self.user_phone:
                self.sender.sendMessage(
                    "Please Provide Us Your 10 Digit Mobile Number")
            # user email not set prompt user
            elif not self.user_email:
                self.sender.sendMessage(
                    "Please Provide Us Your Mail Id to Proceed")
            # every field is set prompt user to confirm/cancel/modify booking
            elif self.book_table_number and self.book_table_type and \
                    self.user_phone and self.user_email and \
                    self.book_meal_type and self.booking_time and \
                    not self.modify_booking:
                self.confirm_cancel_modify()
        # help user
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
        # status of booking
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
        # modify booking
        elif msg['text'].split('-')[0] == 'modifybooking':
            attr = msg['text'].split('-')[1]
            setattr(self, attr, False)
            self.modify_booking = False
            self.sender.sendMessage("Enter New value for {}".format(attr))
        # not understood negative cases
        else:
            self.sender.sendMessage(random.choice(self.reply_not_understood))
            self.sender.sendMessage(
                "{} please type 'help', 'status or 'modify' to get respective "
                "results".format(
                    self.user_name
                )
            )
        log.debug("user_greet: {}, book_table_type: {}"
                  "book_meal_type: {}, user_phone: {}"
                  "booking_time: {}, book_table_number: {},"
                  "user_email: {}, user_name: {}, user_id: {}"
                  "user_type: {}, user_timestamp: {}"
                  "confirm_booking: {}, modify_booking: {}. returning_user: {}"
                  "".format(self.is_user_greet,
                            self.book_table_type, self.book_meal_type,
                            self.user_phone, self.booking_time,
                            self.book_table_number, self.user_email,
                            self.user_name, self.user_id, self.user_type,
                            self.user_timestamp, self.confirm_booking,
                            self.modify_booking, self.returning_user))
