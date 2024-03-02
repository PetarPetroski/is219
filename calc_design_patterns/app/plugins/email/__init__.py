import sys
from app.commands import Command
import logging

class EmailCommand(Command):
    def execute(self, *args):
        logging.info("I will email you")
        print(f'I will email you')