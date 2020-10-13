from django.test import TestCase
from django.core.mail import send_mail
from taxishare.settings import MAILGUN_SERVER_NAME

class EmailTestCase(TestCase):

    def test_send_email(self):
        send_mail("test", "test", f"test@{MAILGUN_SERVER_NAME}", ["ala2017eddine@gmail.com"])