import sys
import logging
from app.commands import Command


class ExitCommand(Command):
    def execute(self, *args):
        logging.info("Exiting...")
        sys.exit("Exiting...")