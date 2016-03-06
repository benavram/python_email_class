# -*- coding: utf-8 -*-
"""Reusable email class
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email_settings
from smtplib import SMTPAuthenticationError, SMTPRecipientsRefused, \
SMTPHeloError, SMTPSenderRefused, SMTPDataError

class SendEmail(object):
    """SendEmail class, blah,blah, blah
    """
    def __init__(self, ):
        """ get/open smpt connection
            settings from email_settings
        """
        host = email_settings.EMAIL_HOST
        port = email_settings.EMAIL_PORT
        self.tls = email_settings.EMAIL_USE_TLS
        self.user = email_settings.UN
        self.passwd = email_settings.PW
        self.smtp_server = smtplib.SMTP(host, port)

    def get_connection(self,):
        """SendEmail class, blah,blah, blah
        """
        try:
            self.smtp_server.ehlo()
            if self.tls:
                self.smtp_server.starttls()
                self.smtp_server.ehlo()
            self.smtp_server.login(self.user, self.passwd)
            return self.smtp_server
        except SMTPAuthenticationError as error:
            print(error) # pylint: disable = C0325
            return False

    def send_mail(self, email_content, email_to, email_from=None):
        """SendEmail class, blah,blah, blah
        """
        conn = self.get_connection()
        if email_from is None:
            email_from = email_settings.DEFAULT_EMAIL_FROM

        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'blah, blah, blah . . . '
        msg['From'] = email_from
        msg['TO'] = email_to
        msg_body = MIMEText(email_content, 'plain')
        msg.attach(msg_body)
        try:
            email = conn.sendmail(email_from, email_to, msg.as_string())
        except (SMTPRecipientsRefused,
                SMTPHeloError,
                SMTPSenderRefused,
                SMTPDataError) as error:
            error_msg = "that $hit is broke yo: {0}".format(error)
            print(error_msg) # pylint: disable = C0325
        conn.close()
        return email
