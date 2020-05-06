#!/usr/bin/env python3
# A simple script to send message from command line.

import time
import logging
import argparse

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--username", "-u", help="Telegram username")
parser.add_argument("--message", "-m", help="Message to send")

# Read arguments from the command line
args = parser.parse_args()

# Import the client
from telethon.sync import TelegramClient, connection, events, errors, utils

# Define some variables so the code reads easier
session = 'session_file'
api_id = <api_id>
api_hash = '<api_hash>'

logging.basicConfig(level=logging.ERROR)


client = TelegramClient(
    session, api_id, api_hash,
#    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
#    proxy=('mtproto ip address or domain name', 443, 'secret')
)



client.start()
messages = client.send_message(args.username, args.message)
