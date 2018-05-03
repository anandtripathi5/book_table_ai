# -*- coding: utf-8 -*-
import smtplib
from email_template import email_content, email_content_part_2
from config import EMAIL_FROM_ADDRESS, SMTP_USER_NAME, \
        SMTP_PASSWORD, SMTP_HOST_NAME
from logger import log, function_logger
import email


@function_logger(log)
def send_email(email_address, name, body):
        to_address = email_address if type(email_address) is list else [email_address]
        msg = email.message.Message()
        msg['From'] = EMAIL_FROM_ADDRESS
        msg['Subject'] = "Table Booking Summary of HutPizza"
        msg['To'] = to_address[0]
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_content + body + email_content_part_2)
        try:
                server = smtplib.SMTP(SMTP_HOST_NAME)
                server.ehlo()
                server.starttls()
                server.login(SMTP_USER_NAME, SMTP_PASSWORD)
                server.sendmail(EMAIL_FROM_ADDRESS, to_address, msg.as_string())
                server.close()
                log.info('successfully sent the mail')
        except Exception as e:
                log.error("failed to send mail: {}".format(e))
