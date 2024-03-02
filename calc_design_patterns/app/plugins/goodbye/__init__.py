from app.commands import Command
import logging

class GoodbyeCommand(Command):

    def execute(self, *args):
        logging.info("Goodbye")
        print("Goodbye")
