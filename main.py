#!/usr/bin/python3

from generatedata import getData
from mailer import sendEmail

if __name__ == '__main__':
    getData()
    sendEmail()