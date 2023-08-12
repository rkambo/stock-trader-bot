#!/usr/bin/python3

from generatedata import getData
from mailer import sendEmail
from dotenv import dotenv_values

config = dotenv_values(".env")

if __name__ == '__main__':
    getData()
    sendEmail([config['EMAIL']], 'Weekly Summary Report')