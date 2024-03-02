import sys
from app.commands import Command
import logging

class DiscordCommand(Command):
    def execute(self):
        logging.info("I WIll send something to discord")
        print(f'I WIll send something to discord')