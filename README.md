# Telegram-Bot



##### Telegram Bot is application that will book your table in a restuarant considering all your preferences.

It will do the following tasks
* Will set the booking time for you
* Will set table type for like bachelor or couple etc.
* Will book table according to the number of guests registered
* Will book the meal type for your booking
* Will show you the summary of booking in textual form as well as send a email to your registered email address

## Installation
Please follow following steps
* git clone https://github.com/anandtripathi5/book_table_ai.git
* create virtual environment
```sh
virtualenv telegram
```
* Activate virtualenv
```
source telegram/bin/activate
```
* Install dependencies
```
pip install -r requirement.txt
```
* run supervisor using supervisor.conf file and pass smtp_username and password as environment variable